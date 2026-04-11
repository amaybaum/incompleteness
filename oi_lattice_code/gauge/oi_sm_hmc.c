/*
 * OI Framework: Full SM Gauge Structure HMC
 * ==========================================
 * 
 * Simulates Z = ∫ DU₃ DU₂ DU₁ |det D_OI(U₃,U₂,U₁)|²
 * 
 * The K=6 internal components of the OI wave equation couple to 
 * different gauge group factors:
 *   Components 0,1,2 → SU(3) [T₁ irrep, color]
 *   Components 3,4   → SU(2) [E irrep, weak isospin]
 *   Component  5     → U(1)  [A₁ irrep, hypercharge]
 *
 * The single fermion determinant generates different effective 
 * couplings for each gauge group — the C₂ splitting emerges 
 * automatically from the group-theoretic structure.
 *
 * Compile: gcc -O3 -o oi_sm_hmc oi_sm_hmc.c -lm
 * Run:     ./oi_sm_hmc -L 4 -mass 0.01 -ntraj 200 -ntherm 100
 *
 * Output: <P₃>, <P₂>, <P₁> (plaquettes for each gauge group)
 *         → 1/α₃, 1/α₂, 1/α₁ at the lattice scale
 *         → SM gauge couplings at M_Z after RG running
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <complex.h>

/* ================================================================
 * Configuration
 * ================================================================ */

#define ND 4          /* Spacetime dimensions */
#define K_TOTAL 6     /* Total internal components */
#define NC3 3         /* SU(3) colors */
#define NC2 2         /* SU(2) colors */
#define NC1 1         /* U(1) "colors" */
#define MAX_CG 5000
#define CG_TOL 1e-10

/* Component assignments */
#define K_SU3_START 0
#define K_SU3_END   3   /* Components 0,1,2 → SU(3) */
#define K_SU2_START 3
#define K_SU2_END   5   /* Components 3,4 → SU(2) */
#define K_U1_START  5
#define K_U1_END    6   /* Component 5 → U(1) */

/* Parameters */
static int L = 4;
static int VOL;
static double mass = 0.01;
static double dt = 0.01;
static int nsteps = 15;
static int ntraj = 200;
static int ntherm = 100;
static int nmeas = 5;

/* Total DOF per site = NC3*K_SU3 + NC2*K_SU2 + NC1*K_U1 = 3*3 + 2*2 + 1*1 = 14 */
#define SITE_DOF 14
static int NDOF;  /* VOL * SITE_DOF */

/* ================================================================
 * Complex matrix types
 * ================================================================ */
typedef double complex mat3x3[3][3];
typedef double complex mat2x2[2][2];

/* ================================================================
 * SU(3) operations
 * ================================================================ */
static void m3_unit(mat3x3 A) {
    memset(A, 0, sizeof(mat3x3));
    A[0][0] = A[1][1] = A[2][2] = 1.0;
}
static void m3_zero(mat3x3 A) { memset(A, 0, sizeof(mat3x3)); }
static void m3_copy(mat3x3 d, const mat3x3 s) { memcpy(d, s, sizeof(mat3x3)); }

static void m3_mul(mat3x3 C, const mat3x3 A, const mat3x3 B) {
    mat3x3 T;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++) {
            T[i][j] = 0;
            for (int k = 0; k < 3; k++) T[i][j] += A[i][k] * B[k][j];
        }
    m3_copy(C, T);
}

static void m3_mul_dag(mat3x3 C, const mat3x3 A, const mat3x3 B) {
    mat3x3 T;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++) {
            T[i][j] = 0;
            for (int k = 0; k < 3; k++) T[i][j] += A[i][k] * conj(B[j][k]);
        }
    m3_copy(C, T);
}

static double complex m3_trace(const mat3x3 A) {
    return A[0][0] + A[1][1] + A[2][2];
}

static void m3_project_su3(mat3x3 A) {
    double norm, n2;
    double complex dot;
    norm = 0;
    for (int j = 0; j < 3; j++) norm += creal(A[0][j]*conj(A[0][j]));
    norm = 1.0/sqrt(norm);
    for (int j = 0; j < 3; j++) A[0][j] *= norm;
    dot = 0;
    for (int j = 0; j < 3; j++) dot += conj(A[0][j]) * A[1][j];
    for (int j = 0; j < 3; j++) A[1][j] -= dot * A[0][j];
    n2 = 0;
    for (int j = 0; j < 3; j++) n2 += creal(A[1][j]*conj(A[1][j]));
    n2 = 1.0/sqrt(n2);
    for (int j = 0; j < 3; j++) A[1][j] *= n2;
    A[2][0] = conj(A[0][1]*A[1][2] - A[0][2]*A[1][1]);
    A[2][1] = conj(A[0][2]*A[1][0] - A[0][0]*A[1][2]);
    A[2][2] = conj(A[0][0]*A[1][1] - A[0][1]*A[1][0]);
}

static void m3_exp_ah(mat3x3 expA, const mat3x3 A) {
    mat3x3 An, T;
    m3_unit(expA);
    m3_copy(An, A);
    double f = 1.0;
    for (int n = 1; n <= 12; n++) {
        f *= n;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                expA[i][j] += An[i][j] / f;
        m3_mul(T, An, A);
        m3_copy(An, T);
    }
    m3_project_su3(expA);
}

static void m3_gauss_ah(mat3x3 P) {
    double g[8];
    for (int i = 0; i < 8; i += 2) {
        double u1 = (double)rand()/RAND_MAX;
        double u2 = (double)rand()/RAND_MAX;
        if (u1 < 1e-15) u1 = 1e-15;
        double r = sqrt(-2.0*log(u1));
        g[i] = r*cos(2*M_PI*u2);
        g[i+1] = r*sin(2*M_PI*u2);
    }
    m3_zero(P);
    P[0][1] = I*g[0]+g[1]; P[1][0] = I*g[0]-g[1];
    P[0][0] += I*g[2]; P[1][1] -= I*g[2];
    P[0][2] = I*g[3]+g[4]; P[2][0] = I*g[3]-g[4];
    P[1][2] = I*g[5]+g[6]; P[2][1] = I*g[5]-g[6];
    double s = g[7]/sqrt(3.0);
    P[0][0] += I*s; P[1][1] += I*s; P[2][2] -= I*2.0*s;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            P[i][j] /= sqrt(2.0);
}

/* ================================================================
 * SU(2) operations
 * ================================================================ */
static void m2_unit(mat2x2 A) {
    memset(A, 0, sizeof(mat2x2));
    A[0][0] = A[1][1] = 1.0;
}
static void m2_zero(mat2x2 A) { memset(A, 0, sizeof(mat2x2)); }
static void m2_copy(mat2x2 d, const mat2x2 s) { memcpy(d, s, sizeof(mat2x2)); }

static void m2_mul(mat2x2 C, const mat2x2 A, const mat2x2 B) {
    mat2x2 T;
    T[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0];
    T[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1];
    T[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0];
    T[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1];
    m2_copy(C, T);
}

static void m2_mul_dag(mat2x2 C, const mat2x2 A, const mat2x2 B) {
    mat2x2 T;
    T[0][0] = A[0][0]*conj(B[0][0]) + A[0][1]*conj(B[0][1]);
    T[0][1] = A[0][0]*conj(B[1][0]) + A[0][1]*conj(B[1][1]);
    T[1][0] = A[1][0]*conj(B[0][0]) + A[1][1]*conj(B[0][1]);
    T[1][1] = A[1][0]*conj(B[1][0]) + A[1][1]*conj(B[1][1]);
    m2_copy(C, T);
}

static double complex m2_trace(const mat2x2 A) { return A[0][0] + A[1][1]; }

static void m2_project_su2(mat2x2 A) {
    /* SU(2): A = a₀I + i(aᵢσᵢ), normalize to det=1 */
    double complex a0 = (A[0][0] + A[1][1]) * 0.5;
    double complex a3 = (A[0][0] - A[1][1]) * 0.5 / I;
    double complex a1 = (A[0][1] + A[1][0]) * 0.5 / I;
    double complex a2 = (A[0][1] - A[1][0]) * 0.5;
    double norm = sqrt(creal(a0*conj(a0) + a1*conj(a1) + a2*conj(a2) + a3*conj(a3)));
    if (norm < 1e-15) { m2_unit(A); return; }
    a0 /= norm; a1 /= norm; a2 /= norm; a3 /= norm;
    /* Take real parts for proper SU(2) */
    double r0 = creal(a0), r1 = creal(a1), r2 = creal(a2), r3 = creal(a3);
    norm = sqrt(r0*r0 + r1*r1 + r2*r2 + r3*r3);
    r0/=norm; r1/=norm; r2/=norm; r3/=norm;
    A[0][0] = r0 + I*r3;  A[0][1] = r2 + I*r1;
    A[1][0] = -r2 + I*r1; A[1][1] = r0 - I*r3;
}

static void m2_exp_ah(mat2x2 expA, const mat2x2 A) {
    mat2x2 An, T;
    m2_unit(expA);
    m2_copy(An, A);
    double f = 1.0;
    for (int n = 1; n <= 12; n++) {
        f *= n;
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                expA[i][j] += An[i][j] / f;
        m2_mul(T, An, A);
        m2_copy(An, T);
    }
    m2_project_su2(expA);
}

static void m2_gauss_ah(mat2x2 P) {
    double g[3];
    for (int i = 0; i < 2; i += 2) {
        double u1 = (double)rand()/RAND_MAX;
        double u2 = (double)rand()/RAND_MAX;
        if (u1 < 1e-15) u1 = 1e-15;
        double r = sqrt(-2.0*log(u1));
        g[i] = r*cos(2*M_PI*u2);
        if (i+1 < 3) g[i+1] = r*sin(2*M_PI*u2);
    }
    { double u1=(double)rand()/RAND_MAX,u2=(double)rand()/RAND_MAX;
      if(u1<1e-15)u1=1e-15; g[2]=sqrt(-2.0*log(u1))*cos(2*M_PI*u2); }
    m2_zero(P);
    P[0][1] = I*g[0] + g[1]; P[1][0] = I*g[0] - g[1];
    P[0][0] = I*g[2]; P[1][1] = -I*g[2];
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            P[i][j] /= sqrt(2.0);
}

/* ================================================================
 * U(1) operations (phase)
 * ================================================================ */
/* U(1) link = exp(iθ), stored as double complex */

/* ================================================================
 * Lattice Geometry
 * ================================================================ */
static int *fwd, *bwd;
static double *stag_eta;

static void init_geometry(void) {
    VOL = 1;
    for (int mu = 0; mu < ND; mu++) VOL *= L;
    NDOF = VOL * SITE_DOF;
    
    fwd = (int*)malloc(VOL * ND * sizeof(int));
    bwd = (int*)malloc(VOL * ND * sizeof(int));
    stag_eta = (double*)malloc(VOL * ND * sizeof(double));
    
    for (int i = 0; i < VOL; i++) {
        int n[ND], tmp = i;
        for (int mu = ND-1; mu >= 0; mu--) { n[mu] = tmp % L; tmp /= L; }
        for (int mu = 0; mu < ND; mu++) {
            int nf[ND], nb[ND];
            memcpy(nf, n, sizeof(n)); nf[mu] = (n[mu]+1) % L;
            memcpy(nb, n, sizeof(n)); nb[mu] = (n[mu]-1+L) % L;
            int idx_f = 0, idx_b = 0;
            for (int d = 0; d < ND; d++) { idx_f = idx_f*L+nf[d]; idx_b = idx_b*L+nb[d]; }
            fwd[i*ND+mu] = idx_f;
            bwd[i*ND+mu] = idx_b;
            int sum = 0;
            for (int nu = 0; nu < mu; nu++) sum += n[nu];
            stag_eta[i*ND+mu] = (sum%2==0) ? 1.0 : -1.0;
        }
    }
}

/* ================================================================
 * Gauge Fields: separate links for each group
 * ================================================================ */
static mat3x3 *U3;              /* SU(3) links: U3[site*ND+mu] */
static mat2x2 *U2;              /* SU(2) links: U2[site*ND+mu] */
static double complex *U1;      /* U(1) links: U1[site*ND+mu] = exp(iθ) */

static mat3x3 *P3;              /* SU(3) momenta */
static mat2x2 *P2;              /* SU(2) momenta */
static double *P1;              /* U(1) momenta (real, anti-Hermitian = imaginary) */

/* Saved copies for accept/reject */
static mat3x3 *U3_save;
static mat2x2 *U2_save;
static double complex *U1_save;

static void init_gauge(int hot) {
    int NL = VOL * ND;
    U3 = (mat3x3*)malloc(NL * sizeof(mat3x3));
    U2 = (mat2x2*)malloc(NL * sizeof(mat2x2));
    U1 = (double complex*)malloc(NL * sizeof(double complex));
    P3 = (mat3x3*)malloc(NL * sizeof(mat3x3));
    P2 = (mat2x2*)malloc(NL * sizeof(mat2x2));
    P1 = (double*)malloc(NL * sizeof(double));
    U3_save = (mat3x3*)malloc(NL * sizeof(mat3x3));
    U2_save = (mat2x2*)malloc(NL * sizeof(mat2x2));
    U1_save = (double complex*)malloc(NL * sizeof(double complex));
    
    for (int i = 0; i < NL; i++) {
        if (hot) {
            mat3x3 H3; m3_gauss_ah(H3);
            for(int a=0;a<3;a++)for(int b=0;b<3;b++) H3[a][b]*=2.0;
            m3_exp_ah(U3[i], H3);
            mat2x2 H2; m2_gauss_ah(H2);
            for(int a=0;a<2;a++)for(int b=0;b<2;b++) H2[a][b]*=2.0;
            m2_exp_ah(U2[i], H2);
            U1[i] = cexp(I * ((double)rand()/RAND_MAX * 2*M_PI));
        } else {
            m3_unit(U3[i]);
            m2_unit(U2[i]);
            U1[i] = 1.0;
        }
    }
}

/* ================================================================
 * Fermion Vector Indexing
 * 
 * At each site, the fermion vector has SITE_DOF = 14 components:
 *   [SU3_color0_k0, SU3_color1_k0, SU3_color2_k0,  (k=0, comp 0)
 *    SU3_color0_k1, SU3_color1_k1, SU3_color2_k1,  (k=1, comp 1)
 *    SU3_color0_k2, SU3_color1_k2, SU3_color2_k2,  (k=2, comp 2)
 *    SU2_color0_k3, SU2_color1_k3,                  (k=3, comp 3)
 *    SU2_color0_k4, SU2_color1_k4,                  (k=4, comp 4)
 *    U1_k5]                                          (k=5, comp 5)
 * 
 * Index: psi[site * SITE_DOF + offset]
 * SU(3) k-th component, color a: offset = k*NC3 + a  (k=0,1,2; a=0,1,2)
 * SU(2) k-th component, color a: offset = 9 + (k-3)*NC2 + a  (k=3,4; a=0,1)
 * U(1):                          offset = 13  (k=5)
 * ================================================================ */

#define IDX_SU3(k, a) ((k)*NC3 + (a))          /* k=0,1,2; a=0,1,2 */
#define IDX_SU2(k, a) (9 + ((k)-3)*NC2 + (a))  /* k=3,4;   a=0,1 */
#define IDX_U1         13                        /* k=5 */

/* ================================================================
 * Staggered Dirac Operator D·x = y
 * 
 * For each internal component k:
 *   If k ∈ {0,1,2} (SU(3)): gauge link is U3
 *   If k ∈ {3,4}   (SU(2)): gauge link is U2
 *   If k = 5       (U(1)):  gauge link is U1
 * 
 * D acts independently on each k-component, with the appropriate 
 * gauge group's link. The staggered phases η_μ(n) are the same for all k.
 * ================================================================ */

static void dirac_op(double complex *y, const double complex *x) {
    memset(y, 0, NDOF * sizeof(double complex));
    
    for (int n = 0; n < VOL; n++) {
        for (int mu = 0; mu < ND; mu++) {
            int np = fwd[n*ND+mu];
            int nm = bwd[n*ND+mu];
            double e = stag_eta[n*ND+mu];
            
            /* SU(3) components: k=0,1,2 */
            for (int k = 0; k < 3; k++) {
                for (int a = 0; a < NC3; a++) {
                    int idx_na = n*SITE_DOF + IDX_SU3(k, a);
                    /* Forward: +0.5 η U₃(n,μ)_{ab} x(n+μ)_{kb} */
                    for (int b = 0; b < NC3; b++) {
                        int idx_npb = np*SITE_DOF + IDX_SU3(k, b);
                        y[idx_na] += 0.5 * e * U3[n*ND+mu][a][b] * x[idx_npb];
                    }
                    /* Backward: -0.5 η U₃†(n-μ,μ)_{ab} x(n-μ)_{kb} */
                    for (int b = 0; b < NC3; b++) {
                        int idx_nmb = nm*SITE_DOF + IDX_SU3(k, b);
                        y[idx_na] -= 0.5 * e * conj(U3[nm*ND+mu][b][a]) * x[idx_nmb];
                    }
                }
            }
            
            /* SU(2) components: k=3,4 */
            for (int k = 3; k < 5; k++) {
                for (int a = 0; a < NC2; a++) {
                    int idx_na = n*SITE_DOF + IDX_SU2(k, a);
                    for (int b = 0; b < NC2; b++) {
                        int idx_npb = np*SITE_DOF + IDX_SU2(k, b);
                        y[idx_na] += 0.5 * e * U2[n*ND+mu][a][b] * x[idx_npb];
                    }
                    for (int b = 0; b < NC2; b++) {
                        int idx_nmb = nm*SITE_DOF + IDX_SU2(k, b);
                        y[idx_na] -= 0.5 * e * conj(U2[nm*ND+mu][b][a]) * x[idx_nmb];
                    }
                }
            }
            
            /* U(1) component: k=5 */
            {
                int idx_n5 = n*SITE_DOF + IDX_U1;
                int idx_np5 = np*SITE_DOF + IDX_U1;
                int idx_nm5 = nm*SITE_DOF + IDX_U1;
                y[idx_n5] += 0.5 * e * U1[n*ND+mu] * x[idx_np5];
                y[idx_n5] -= 0.5 * e * conj(U1[nm*ND+mu]) * x[idx_nm5];
            }
        }
    }
}

/* D†D + m² */
static void DdagD_op(double complex *y, const double complex *x) {
    double complex *tmp = (double complex*)malloc(NDOF * sizeof(double complex));
    dirac_op(tmp, x);
    dirac_op(y, tmp);
    /* D† = -D for staggered, so D†D = -D² */
    for (int i = 0; i < NDOF; i++)
        y[i] = -y[i] + mass*mass * x[i];
    free(tmp);
}

/* CG solver */
static int cg_solve(double complex *x, const double complex *b) {
    double complex *r = (double complex*)malloc(NDOF*sizeof(double complex));
    double complex *p = (double complex*)malloc(NDOF*sizeof(double complex));
    double complex *Ap = (double complex*)malloc(NDOF*sizeof(double complex));
    memset(x, 0, NDOF*sizeof(double complex));
    memcpy(r, b, NDOF*sizeof(double complex));
    memcpy(p, b, NDOF*sizeof(double complex));
    double rsq = 0;
    for (int i = 0; i < NDOF; i++) rsq += creal(conj(r[i])*r[i]);
    double rsq0 = rsq;
    int iter;
    for (iter = 0; iter < MAX_CG; iter++) {
        if (rsq < CG_TOL * rsq0 && rsq < CG_TOL) break;
        DdagD_op(Ap, p);
        double complex pAp = 0;
        for (int i = 0; i < NDOF; i++) pAp += conj(p[i])*Ap[i];
        double complex alpha = rsq / pAp;
        double rsq_new = 0;
        for (int i = 0; i < NDOF; i++) {
            x[i] += alpha * p[i];
            r[i] -= alpha * Ap[i];
            rsq_new += creal(conj(r[i])*r[i]);
        }
        double beta = rsq_new / rsq;
        for (int i = 0; i < NDOF; i++) p[i] = r[i] + beta*p[i];
        rsq = rsq_new;
    }
    free(r); free(p); free(Ap);
    return iter;
}

/* ================================================================
 * Pseudofermion
 * ================================================================ */
static double complex *phi;

static void generate_pseudofermion(void) {
    double complex *eta_pf = (double complex*)malloc(NDOF*sizeof(double complex));
    for (int i = 0; i < NDOF; i++) {
        double u1 = (double)rand()/RAND_MAX, u2 = (double)rand()/RAND_MAX;
        if (u1 < 1e-15) u1 = 1e-15;
        double r = sqrt(-0.5*log(u1));
        eta_pf[i] = r*cos(2*M_PI*u2) + I*r*sin(2*M_PI*u2);
    }
    /* φ = (D + m)η */
    dirac_op(phi, eta_pf);
    for (int i = 0; i < NDOF; i++) phi[i] += mass * eta_pf[i];
    free(eta_pf);
}

static double fermion_action(void) {
    double complex *x = (double complex*)malloc(NDOF*sizeof(double complex));
    cg_solve(x, phi);
    double S = 0;
    for (int i = 0; i < NDOF; i++) S += creal(conj(phi[i])*x[i]);
    free(x);
    return S;  /* Already includes all K=6 components */
}

/* ================================================================
 * Fermion Force — separate for each gauge group
 * ================================================================ */

static void fermion_force(mat3x3 *F3, mat2x2 *F2, double *F1_arr) {
    double complex *psi = (double complex*)malloc(NDOF*sizeof(double complex));
    double complex *chi = (double complex*)malloc(NDOF*sizeof(double complex));
    
    cg_solve(psi, phi);
    dirac_op(chi, psi);
    
    int NL = VOL*ND;
    memset(F3, 0, NL*sizeof(mat3x3));
    memset(F2, 0, NL*sizeof(mat2x2));
    memset(F1_arr, 0, NL*sizeof(double));
    
    for (int n = 0; n < VOL; n++) {
        for (int mu = 0; mu < ND; mu++) {
            int np = fwd[n*ND+mu];
            double e = stag_eta[n*ND+mu];
            int link = n*ND+mu;
            
            /* SU(3) force: sum over k=0,1,2 */
            for (int k = 0; k < 3; k++) {
                /* Compute U₃·ψ(n+μ) for this k */
                double complex Upsi[NC3], Uchi[NC3];
                for (int a = 0; a < NC3; a++) {
                    Upsi[a] = 0; Uchi[a] = 0;
                    for (int b = 0; b < NC3; b++) {
                        Upsi[a] += U3[link][a][b] * psi[np*SITE_DOF + IDX_SU3(k,b)];
                        Uchi[a] += U3[link][a][b] * chi[np*SITE_DOF + IDX_SU3(k,b)];
                    }
                }
                /* F += e/2 * (Upsi ⊗ chi†(n) - Uchi ⊗ psi†(n)) */
                for (int a = 0; a < NC3; a++)
                    for (int b = 0; b < NC3; b++) {
                        F3[link][a][b] += e*0.5 * (
                            Upsi[a] * conj(chi[n*SITE_DOF + IDX_SU3(k,b)])
                          - Uchi[a] * conj(psi[n*SITE_DOF + IDX_SU3(k,b)]));
                    }
            }
            /* Project SU(3) force to traceless anti-Hermitian */
            {
                mat3x3 *F = &F3[link];
                double complex tr = 0;
                mat3x3 Fah;
                for (int a = 0; a < 3; a++)
                    for (int b = 0; b < 3; b++)
                        Fah[a][b] = ((*F)[a][b] - conj((*F)[b][a])) * 0.5;
                for (int a = 0; a < 3; a++) tr += Fah[a][a];
                tr /= 3.0;
                for (int a = 0; a < 3; a++) Fah[a][a] -= tr;
                m3_copy(*F, Fah);
            }
            
            /* SU(2) force: sum over k=3,4 */
            for (int k = 3; k < 5; k++) {
                double complex Upsi[NC2], Uchi[NC2];
                for (int a = 0; a < NC2; a++) {
                    Upsi[a] = 0; Uchi[a] = 0;
                    for (int b = 0; b < NC2; b++) {
                        Upsi[a] += U2[link][a][b] * psi[np*SITE_DOF + IDX_SU2(k,b)];
                        Uchi[a] += U2[link][a][b] * chi[np*SITE_DOF + IDX_SU2(k,b)];
                    }
                }
                for (int a = 0; a < NC2; a++)
                    for (int b = 0; b < NC2; b++) {
                        F2[link][a][b] += e*0.5 * (
                            Upsi[a] * conj(chi[n*SITE_DOF + IDX_SU2(k,b)])
                          - Uchi[a] * conj(psi[n*SITE_DOF + IDX_SU2(k,b)]));
                    }
            }
            /* Project SU(2) force */
            {
                mat2x2 *F = &F2[link];
                double complex tr = 0;
                mat2x2 Fah;
                for (int a = 0; a < 2; a++)
                    for (int b = 0; b < 2; b++)
                        Fah[a][b] = ((*F)[a][b] - conj((*F)[b][a])) * 0.5;
                for (int a = 0; a < 2; a++) tr += Fah[a][a];
                tr /= 2.0;
                for (int a = 0; a < 2; a++) Fah[a][a] -= tr;
                m2_copy(*F, Fah);
            }
            
            /* U(1) force: k=5 only */
            {
                double complex Upsi5 = U1[link] * psi[np*SITE_DOF + IDX_U1];
                double complex Uchi5 = U1[link] * chi[np*SITE_DOF + IDX_U1];
                double complex M = e*0.5 * (
                    Upsi5 * conj(chi[n*SITE_DOF + IDX_U1])
                  - Uchi5 * conj(psi[n*SITE_DOF + IDX_U1]));
                /* Anti-Hermitian projection of U(1) = imaginary part */
                F1_arr[link] = cimag(M);
            }
        }
    }
    
    free(psi); free(chi);
}

/* ================================================================
 * Kinetic Energy
 * ================================================================ */
static double kinetic_energy(void) {
    double K = 0;
    int NL = VOL*ND;
    for (int i = 0; i < NL; i++) {
        for (int a = 0; a < 3; a++)
            for (int b = 0; b < 3; b++)
                K -= creal(P3[i][a][b] * conj(P3[i][a][b]));
        for (int a = 0; a < 2; a++)
            for (int b = 0; b < 2; b++)
                K -= creal(P2[i][a][b] * conj(P2[i][a][b]));
        K += P1[i] * P1[i];  /* U(1) momentum is real */
    }
    return 0.5 * K;
}

/* ================================================================
 * MD Integration (Leapfrog)
 * ================================================================ */
static void md_integrate(void) {
    int NL = VOL*ND;
    mat3x3 *F3 = (mat3x3*)malloc(NL*sizeof(mat3x3));
    mat2x2 *F2 = (mat2x2*)malloc(NL*sizeof(mat2x2));
    double *F1_arr = (double*)malloc(NL*sizeof(double));
    
    /* Half step momenta */
    fermion_force(F3, F2, F1_arr);
    for (int i = 0; i < NL; i++) {
        for(int a=0;a<3;a++)for(int b=0;b<3;b++) P3[i][a][b] += 0.5*dt*F3[i][a][b];
        for(int a=0;a<2;a++)for(int b=0;b<2;b++) P2[i][a][b] += 0.5*dt*F2[i][a][b];
        P1[i] += 0.5*dt*F1_arr[i];
    }
    
    for (int step = 0; step < nsteps; step++) {
        /* Full step gauge links */
        for (int i = 0; i < NL; i++) {
            /* SU(3): U → exp(dt·P)·U */
            mat3x3 dtP3, expP3, Unew3;
            m3_copy(dtP3, P3[i]);
            for(int a=0;a<3;a++)for(int b=0;b<3;b++) dtP3[a][b]*=dt;
            m3_exp_ah(expP3, dtP3);
            m3_mul(Unew3, expP3, U3[i]);
            m3_project_su3(Unew3);
            m3_copy(U3[i], Unew3);
            
            /* SU(2): U → exp(dt·P)·U */
            mat2x2 dtP2, expP2, Unew2;
            m2_copy(dtP2, P2[i]);
            for(int a=0;a<2;a++)for(int b=0;b<2;b++) dtP2[a][b]*=dt;
            m2_exp_ah(expP2, dtP2);
            m2_mul(Unew2, expP2, U2[i]);
            m2_project_su2(Unew2);
            m2_copy(U2[i], Unew2);
            
            /* U(1): θ → θ + dt·p */
            double theta = carg(U1[i]) + dt * P1[i];
            U1[i] = cexp(I * theta);
        }
        
        /* Full step momenta (half on last) */
        fermion_force(F3, F2, F1_arr);
        double fdt = (step < nsteps-1) ? dt : 0.5*dt;
        for (int i = 0; i < NL; i++) {
            for(int a=0;a<3;a++)for(int b=0;b<3;b++) P3[i][a][b] += fdt*F3[i][a][b];
            for(int a=0;a<2;a++)for(int b=0;b<2;b++) P2[i][a][b] += fdt*F2[i][a][b];
            P1[i] += fdt*F1_arr[i];
        }
    }
    
    free(F3); free(F2); free(F1_arr);
}

/* ================================================================
 * Measurements: separate plaquettes for each gauge group
 * ================================================================ */
static void measure_plaquettes(double *p3, double *p2, double *p1) {
    *p3 = *p2 = *p1 = 0;
    int count = 0;
    
    for (int n = 0; n < VOL; n++) {
        for (int mu = 0; mu < ND; mu++) {
            for (int nu = mu+1; nu < ND; nu++) {
                int np_mu = fwd[n*ND+mu];
                int np_nu = fwd[n*ND+nu];
                count++;
                
                /* SU(3) plaquette */
                mat3x3 T1, T2, P_mat;
                m3_mul(T1, U3[n*ND+mu], U3[np_mu*ND+nu]);
                m3_mul_dag(T2, T1, U3[np_nu*ND+mu]);
                m3_mul_dag(P_mat, T2, U3[n*ND+nu]);
                *p3 += creal(m3_trace(P_mat)) / NC3;
                
                /* SU(2) plaquette */
                mat2x2 S1, S2, Q_mat;
                m2_mul(S1, U2[n*ND+mu], U2[np_mu*ND+nu]);
                m2_mul_dag(S2, S1, U2[np_nu*ND+mu]);
                m2_mul_dag(Q_mat, S2, U2[n*ND+nu]);
                *p2 += creal(m2_trace(Q_mat)) / NC2;
                
                /* U(1) plaquette */
                double complex u1_plaq = U1[n*ND+mu] * U1[np_mu*ND+nu] 
                                       * conj(U1[np_nu*ND+mu]) * conj(U1[n*ND+nu]);
                *p1 += creal(u1_plaq);
            }
        }
    }
    *p3 /= count; *p2 /= count; *p1 /= count;
}

/* ================================================================
 * Main HMC
 * ================================================================ */
int main(int argc, char *argv[]) {
    int hot_start = 0;
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i],"-L") && i+1<argc) L=atoi(argv[++i]);
        else if (!strcmp(argv[i],"-mass") && i+1<argc) mass=atof(argv[++i]);
        else if (!strcmp(argv[i],"-dt") && i+1<argc) dt=atof(argv[++i]);
        else if (!strcmp(argv[i],"-nsteps") && i+1<argc) nsteps=atoi(argv[++i]);
        else if (!strcmp(argv[i],"-ntraj") && i+1<argc) ntraj=atoi(argv[++i]);
        else if (!strcmp(argv[i],"-ntherm") && i+1<argc) ntherm=atoi(argv[++i]);
        else if (!strcmp(argv[i],"-nmeas") && i+1<argc) nmeas=atoi(argv[++i]);
        else if (!strcmp(argv[i],"-hot")) hot_start=1;
    }
    
    srand(time(NULL));
    init_geometry();
    init_gauge(hot_start);
    phi = (double complex*)malloc(NDOF*sizeof(double complex));
    
    printf("================================================================\n");
    printf("OI Framework: Full SM Gauge Structure HMC\n");
    printf("================================================================\n");
    printf("L=%d, VOL=%d, NDOF=%d (= %d sites × %d dof/site)\n", L, VOL, NDOF, VOL, SITE_DOF);
    printf("K=6 components: 3→SU(3), 2→SU(2), 1→U(1)\n");
    printf("mass=%.4f, dt=%.4f, nsteps=%d\n", mass, dt, nsteps);
    printf("ntraj=%d, ntherm=%d, nmeas=%d, %s start\n", ntraj, ntherm, nmeas, hot_start?"HOT":"COLD");
    
    double p3i, p2i, p1i;
    measure_plaquettes(&p3i, &p2i, &p1i);
    printf("Initial: <P₃>=%.4f <P₂>=%.4f <P₁>=%.4f\n", p3i, p2i, p1i);
    printf("================================================================\n\n");
    
    int accept = 0;
    double p3_sum=0, p2_sum=0, p1_sum=0;
    int meas_count = 0;
    time_t t0 = time(NULL);
    
    for (int traj = 1; traj <= ntherm + ntraj; traj++) {
        /* Refresh momenta */
        int NL = VOL*ND;
        for (int i = 0; i < NL; i++) {
            m3_gauss_ah(P3[i]);
            m2_gauss_ah(P2[i]);
            double u1=(double)rand()/RAND_MAX, u2=(double)rand()/RAND_MAX;
            if(u1<1e-15)u1=1e-15;
            P1[i] = sqrt(-2.0*log(u1)) * cos(2*M_PI*u2);
        }
        
        generate_pseudofermion();
        double K_old = kinetic_energy();
        double S_old = fermion_action();
        double H_old = K_old + S_old;
        
        /* Save */
        memcpy(U3_save, U3, NL*sizeof(mat3x3));
        memcpy(U2_save, U2, NL*sizeof(mat2x2));
        memcpy(U1_save, U1, NL*sizeof(double complex));
        
        md_integrate();
        
        double K_new = kinetic_energy();
        double S_new = fermion_action();
        double H_new = K_new + S_new;
        double dH = H_new - H_old;
        
        int acc = 0;
        if (dH < 0 || (double)rand()/RAND_MAX < exp(-dH)) {
            acc = 1; accept++;
        } else {
            memcpy(U3, U3_save, NL*sizeof(mat3x3));
            memcpy(U2, U2_save, NL*sizeof(mat2x2));
            memcpy(U1, U1_save, NL*sizeof(double complex));
        }
        
        int is_meas = (traj > ntherm) && ((traj-ntherm) % nmeas == 0);
        
        if (is_meas) {
            double p3, p2, p1;
            measure_plaquettes(&p3, &p2, &p1);
            p3_sum += p3; p2_sum += p2; p1_sum += p1;
            meas_count++;
        }
        
        if (traj <= 10 || traj % 10 == 0 || is_meas) {
            double p3, p2, p1;
            measure_plaquettes(&p3, &p2, &p1);
            double elapsed = difftime(time(NULL), t0);
            printf("Traj %4d/%d: P₃=%.4f P₂=%.4f P₁=%.4f dH=%+.2f %s [%.0fs]",
                   traj, ntherm+ntraj, p3, p2, p1, dH, acc?"ACC":"REJ", elapsed);
            if (meas_count > 0) {
                printf("  avg: P₃=%.4f P₂=%.4f P₁=%.4f (%d)",
                       p3_sum/meas_count, p2_sum/meas_count, p1_sum/meas_count, meas_count);
            }
            printf("\n");
            fflush(stdout);
        }
    }
    
    /* Results */
    double P3f = p3_sum/meas_count;
    double P2f = p2_sum/meas_count;
    double P1f = p1_sum/meas_count;
    
    double g2_3 = 4.0*NC3*(1-P3f)/(NC3*NC3-1);
    double g2_2 = 4.0*NC2*(1-P2f)/(NC2*NC2-1);
    /* U(1): g²_eff = 2(1-P₁) */
    double g2_1 = 2.0*(1-P1f);
    
    double ln_ratio = log(1.221e19 / 91.188);
    double b3 = -7.0, b2 = -19.0/6, b1 = 41.0/10;
    
    printf("\n================================================================\n");
    printf("RESULTS (%d measurements)\n", meas_count);
    printf("================================================================\n");
    printf("Acceptance: %.1f%%\n", 100.0*accept/(ntherm+ntraj));
    printf("\n");
    printf("Group  |    <P>    |  g²_eff  | 1/α(cutoff) | RG term  | 1/α(M_Z) | Observed\n");
    printf("-------+-----------+----------+-------------+----------+----------+---------\n");
    printf("SU(3)  | %9.6f | %8.4f | %11.4f | %8.2f | %8.2f |    8.48\n",
           P3f, g2_3, 4*M_PI/g2_3, b3/(2*M_PI)*ln_ratio, 4*M_PI/g2_3 + b3/(2*M_PI)*ln_ratio);
    printf("SU(2)  | %9.6f | %8.4f | %11.4f | %8.2f | %8.2f |   29.57\n",
           P2f, g2_2, 4*M_PI/g2_2, b2/(2*M_PI)*ln_ratio, 4*M_PI/g2_2 + b2/(2*M_PI)*ln_ratio);
    printf("U(1)   | %9.6f | %8.4f | %11.4f | %8.2f | %8.2f |   59.00\n",
           P1f, g2_1, 4*M_PI/g2_1, b1/(2*M_PI)*ln_ratio, 4*M_PI/g2_1 + b1/(2*M_PI)*ln_ratio);
    printf("================================================================\n");
    
    /* Cleanup */
    free(U3);free(U2);free(U1);free(P3);free(P2);free(P1);
    free(U3_save);free(U2_save);free(U1_save);free(phi);
    free(fwd);free(bwd);free(stag_eta);
    
    return 0;
}
