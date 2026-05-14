/*
 * OI-Induced Gauge Theory: HMC with Dynamical Staggered Fermions
 * ================================================================
 * 
 * Simulates Z = ∫ DU |det D_OI(U)|^{2Nf} using pseudofermion HMC.
 * The gauge action is ENTIRELY induced by the fermion determinant —
 * there is no Wilson plaquette term.
 *
 * Compile: gcc -O3 -o oi_hmc oi_hmc.c -lm
 * Run:     ./oi_hmc -L 8 -Nf 6 -mass 0.01 -ntraj 200 -ntherm 100
 *
 * Author: Generated for the OI Framework coupling calculation
 * Purpose: Compute δ₀_ferm (non-perturbative fermion threshold)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <complex.h>

/* ================================================================
 * Parameters
 * ================================================================ */

#define NC 3          /* SU(3) */
#define ND 4          /* 4 dimensions */
#define MAX_CG 5000   /* Max CG iterations */
#define CG_TOL 1e-10  /* CG residual tolerance */

typedef double complex su3_mat[NC][NC];
typedef double complex su3_vec[NC];
typedef double complex color_vec[];  /* Nc-component vector at each site */

/* Global lattice parameters */
static int L = 8;        /* Lattice size */
static int VOL;           /* L^4 */
static int NDOF;          /* VOL * NC */
static int Nf = 6;        /* Number of staggered flavors */
static double mass = 0.01; /* Fermion mass */
static double dt = 0.02;  /* MD step size */
static int nsteps = 20;   /* MD steps per trajectory */
static int ntraj = 200;   /* Number of HMC trajectories */
static int ntherm = 100;  /* Thermalization trajectories */
static int nmeas = 5;     /* Measure every nmeas trajectories */

/* Lattice data */
static su3_mat *U;        /* Gauge links: U[site*ND+mu] */
static int *fwd, *bwd;    /* Neighbor tables */
static double *eta;       /* Staggered phases: eta[site*ND+mu] */

/* ================================================================
 * SU(3) Matrix Operations
 * ================================================================ */

static void su3_unit(su3_mat A) {
    for (int i = 0; i < NC; i++)
        for (int j = 0; j < NC; j++)
            A[i][j] = (i == j) ? 1.0 : 0.0;
}

static void su3_zero(su3_mat A) {
    memset(A, 0, sizeof(su3_mat));
}

static void su3_copy(su3_mat dst, const su3_mat src) {
    memcpy(dst, src, sizeof(su3_mat));
}

static void su3_mul(su3_mat C, const su3_mat A, const su3_mat B) {
    su3_mat T;
    for (int i = 0; i < NC; i++)
        for (int j = 0; j < NC; j++) {
            T[i][j] = 0;
            for (int k = 0; k < NC; k++)
                T[i][j] += A[i][k] * B[k][j];
        }
    su3_copy(C, T);
}

static void su3_mul_dag(su3_mat C, const su3_mat A, const su3_mat B) {
    /* C = A * B† */
    su3_mat T;
    for (int i = 0; i < NC; i++)
        for (int j = 0; j < NC; j++) {
            T[i][j] = 0;
            for (int k = 0; k < NC; k++)
                T[i][j] += A[i][k] * conj(B[j][k]);
        }
    su3_copy(C, T);
}

static void su3_dag_mul(su3_mat C, const su3_mat A, const su3_mat B) {
    /* C = A† * B */
    su3_mat T;
    for (int i = 0; i < NC; i++)
        for (int j = 0; j < NC; j++) {
            T[i][j] = 0;
            for (int k = 0; k < NC; k++)
                T[i][j] += conj(A[k][i]) * B[k][j];
        }
    su3_copy(C, T);
}

static double complex su3_trace(const su3_mat A) {
    return A[0][0] + A[1][1] + A[2][2];
}

static void su3_add(su3_mat C, const su3_mat A, const su3_mat B) {
    for (int i = 0; i < NC; i++)
        for (int j = 0; j < NC; j++)
            C[i][j] = A[i][j] + B[i][j];
}

static void su3_sub(su3_mat C, const su3_mat A, const su3_mat B) {
    for (int i = 0; i < NC; i++)
        for (int j = 0; j < NC; j++)
            C[i][j] = A[i][j] - B[i][j];
}

static void su3_scale(su3_mat A, double complex s) {
    for (int i = 0; i < NC; i++)
        for (int j = 0; j < NC; j++)
            A[i][j] *= s;
}

static void su3_axpy(su3_mat Y, double complex a, const su3_mat X) {
    /* Y += a*X */
    for (int i = 0; i < NC; i++)
        for (int j = 0; j < NC; j++)
            Y[i][j] += a * X[i][j];
}

/* Project to SU(3) via modified Gram-Schmidt + det fix */
static void su3_project(su3_mat A) {
    double norm;
    double complex dot;
    
    /* Normalize row 0 */
    norm = 0;
    for (int j = 0; j < NC; j++) norm += creal(A[0][j] * conj(A[0][j]));
    norm = 1.0 / sqrt(norm);
    for (int j = 0; j < NC; j++) A[0][j] *= norm;
    
    /* Orthogonalize row 1 against row 0 */
    dot = 0;
    for (int j = 0; j < NC; j++) dot += conj(A[0][j]) * A[1][j];
    for (int j = 0; j < NC; j++) A[1][j] -= dot * A[0][j];
    norm = 0;
    for (int j = 0; j < NC; j++) norm += creal(A[1][j] * conj(A[1][j]));
    norm = 1.0 / sqrt(norm);
    for (int j = 0; j < NC; j++) A[1][j] *= norm;
    
    /* Row 2 = conj(row0 × row1) */
    A[2][0] = conj(A[0][1]*A[1][2] - A[0][2]*A[1][1]);
    A[2][1] = conj(A[0][2]*A[1][0] - A[0][0]*A[1][2]);
    A[2][2] = conj(A[0][0]*A[1][1] - A[0][1]*A[1][0]);
}

/* Exponential of traceless anti-Hermitian matrix: U = exp(iH)
 * Uses Cayley-Hamilton for SU(3): exact for 3×3 */
static void su3_exp_ah(su3_mat expA, const su3_mat A) {
    /* A is traceless anti-Hermitian (iH where H is Hermitian traceless)
     * Use Taylor series truncated at order 12 (sufficient for |A| < 1) */
    su3_mat An, T;
    su3_unit(expA);
    su3_copy(An, A);
    
    double factorial = 1.0;
    for (int n = 1; n <= 12; n++) {
        factorial *= n;
        su3_axpy(expA, 1.0/factorial, An);
        su3_mul(T, An, A);
        su3_copy(An, T);
    }
    su3_project(expA);
}

/* Generate random traceless anti-Hermitian matrix (SU(3) Lie algebra) */
static void su3_random_ah(su3_mat H) {
    double r[8];
    for (int i = 0; i < 8; i++)
        r[i] = ((double)rand()/RAND_MAX - 0.5) * 2.0;
    
    /* Gell-Mann basis (×i for anti-Hermitian) */
    su3_zero(H);
    H[0][1] = I * r[0]; H[1][0] = I * r[0];           /* λ₁ */
    H[0][1] += r[1];    H[1][0] -= r[1];               /* λ₂ */
    H[0][0] += I * r[2]; H[1][1] -= I * r[2];          /* λ₃ */
    H[0][2] = I * r[3]; H[2][0] = I * r[3];            /* λ₄ */
    H[0][2] += r[4];    H[2][0] -= r[4];               /* λ₅ */
    H[1][2] = I * r[5]; H[2][1] = I * r[5];            /* λ₆ */
    H[1][2] += r[6];    H[2][1] -= r[6];               /* λ₇ */
    H[0][0] += I * r[7]/sqrt(3.0);                      /* λ₈ */
    H[1][1] += I * r[7]/sqrt(3.0);
    H[2][2] -= I * 2.0*r[7]/sqrt(3.0);
    
    /* Scale by 0.5 to keep it in the algebra */
    su3_scale(H, 0.5);
}

/* Generate Gaussian-distributed momentum (traceless anti-Hermitian) */
static void su3_gauss_ah(su3_mat P) {
    /* Box-Muller for 8 Gaussian random numbers */
    double g[8];
    for (int i = 0; i < 8; i += 2) {
        double u1 = (double)rand()/RAND_MAX;
        double u2 = (double)rand()/RAND_MAX;
        if (u1 < 1e-15) u1 = 1e-15;
        double r = sqrt(-2.0 * log(u1));
        g[i]   = r * cos(2.0 * M_PI * u2);
        g[i+1] = r * sin(2.0 * M_PI * u2);
    }
    
    su3_zero(P);
    P[0][1] = I * g[0]; P[1][0] = I * g[0];
    P[0][1] += g[1];    P[1][0] -= g[1];
    P[0][0] += I * g[2]; P[1][1] -= I * g[2];
    P[0][2] = I * g[3]; P[2][0] = I * g[3];
    P[0][2] += g[4];    P[2][0] -= g[4];
    P[1][2] = I * g[5]; P[2][1] = I * g[5];
    P[1][2] += g[6];    P[2][1] -= g[6];
    P[0][0] += I * g[7]/sqrt(3.0);
    P[1][1] += I * g[7]/sqrt(3.0);
    P[2][2] -= I * 2.0*g[7]/sqrt(3.0);
    
    su3_scale(P, 1.0/sqrt(2.0));
}

/* ================================================================
 * Lattice Geometry
 * ================================================================ */

static int site_index(int n[ND]) {
    int idx = 0;
    for (int mu = 0; mu < ND; mu++) {
        int nm = ((n[mu] % L) + L) % L;
        idx = idx * L + nm;
    }
    return idx;
}

static void init_geometry(void) {
    VOL = 1;
    for (int mu = 0; mu < ND; mu++) VOL *= L;
    NDOF = VOL * NC;
    
    fwd = (int*)malloc(VOL * ND * sizeof(int));
    bwd = (int*)malloc(VOL * ND * sizeof(int));
    eta = (double*)malloc(VOL * ND * sizeof(double));
    
    for (int i = 0; i < VOL; i++) {
        /* Decode coordinates */
        int n[ND];
        int tmp = i;
        for (int mu = ND-1; mu >= 0; mu--) {
            n[mu] = tmp % L;
            tmp /= L;
        }
        
        for (int mu = 0; mu < ND; mu++) {
            /* Forward neighbor */
            int nf[ND];
            memcpy(nf, n, sizeof(n));
            nf[mu] = (n[mu] + 1) % L;
            fwd[i*ND+mu] = site_index(nf);
            
            /* Backward neighbor */
            int nb[ND];
            memcpy(nb, n, sizeof(n));
            nb[mu] = (n[mu] - 1 + L) % L;
            bwd[i*ND+mu] = site_index(nb);
            
            /* Staggered phase η_μ(n) = (-1)^(n₀+...+n_{μ-1}) */
            int sum = 0;
            for (int nu = 0; nu < mu; nu++) sum += n[nu];
            eta[i*ND+mu] = (sum % 2 == 0) ? 1.0 : -1.0;
        }
    }
}

/* ================================================================
 * Gauge Field
 * ================================================================ */

static void init_gauge_cold(void) {
    U = (su3_mat*)malloc(VOL * ND * sizeof(su3_mat));
    for (int i = 0; i < VOL * ND; i++)
        su3_unit(U[i]);
}

static void init_gauge_hot(void) {
    U = (su3_mat*)malloc(VOL * ND * sizeof(su3_mat));
    su3_mat H, expH;
    for (int i = 0; i < VOL * ND; i++) {
        su3_random_ah(H);
        su3_scale(H, 3.0);  /* Large random perturbation */
        su3_exp_ah(expH, H);
        su3_copy(U[i], expH);
    }
}

/* ================================================================
 * Staggered Dirac Operator: D·x = y
 * D[i,j] = (1/2) Σ_μ η_μ(i) [U_μ(i)·δ_{j,i+μ} - U_μ†(i-μ)·δ_{j,i-μ}]
 * ================================================================ */

static void dirac_op(double complex *y, const double complex *x) {
    memset(y, 0, NDOF * sizeof(double complex));
    
    for (int i = 0; i < VOL; i++) {
        for (int mu = 0; mu < ND; mu++) {
            int ip = fwd[i*ND+mu];
            int im = bwd[i*ND+mu];
            double e = eta[i*ND+mu];
            
            /* Forward: +(1/2) η U_μ(i) x(i+μ) */
            for (int a = 0; a < NC; a++)
                for (int b = 0; b < NC; b++)
                    y[i*NC+a] += 0.5 * e * U[i*ND+mu][a][b] * x[ip*NC+b];
            
            /* Backward: -(1/2) η U_μ†(i-μ) x(i-μ) */
            for (int a = 0; a < NC; a++)
                for (int b = 0; b < NC; b++)
                    y[i*NC+a] -= 0.5 * e * conj(U[im*ND+mu][b][a]) * x[im*NC+b];
        }
    }
}

/* D†D + m² applied to vector */
static void DdagD_op(double complex *y, const double complex *x) {
    double complex *tmp = (double complex*)malloc(NDOF * sizeof(double complex));
    
    /* tmp = D·x */
    dirac_op(tmp, x);
    
    /* y = D†·tmp = -D·tmp (since D is anti-Hermitian for staggered) */
    /* Actually D† = -D for massless staggered, so D†D = -D² */
    /* But we want D†D + m², and D† = -D, so D†D = D·(-D) = -D² */
    /* Wait: D is anti-Hermitian means D† = -D */
    /* So D†D = (-D)D = -D² */
    /* We compute: y = -D(Dx) + m²x */
    
    dirac_op(y, tmp);
    /* y currently = D²x, we need -D²x + m²x */
    for (int i = 0; i < NDOF; i++)
        y[i] = -y[i] + mass*mass * x[i];
    
    free(tmp);
}

/* ================================================================
 * Conjugate Gradient: solve (D†D + m²) x = b
 * ================================================================ */

static int cg_solve(double complex *x, const double complex *b) {
    double complex *r = (double complex*)malloc(NDOF * sizeof(double complex));
    double complex *p = (double complex*)malloc(NDOF * sizeof(double complex));
    double complex *Ap = (double complex*)malloc(NDOF * sizeof(double complex));
    
    /* x = 0, r = b, p = b */
    memset(x, 0, NDOF * sizeof(double complex));
    memcpy(r, b, NDOF * sizeof(double complex));
    memcpy(p, b, NDOF * sizeof(double complex));
    
    double rsq = 0;
    for (int i = 0; i < NDOF; i++) rsq += creal(conj(r[i]) * r[i]);
    double rsq0 = rsq;
    
    int iter;
    for (iter = 0; iter < MAX_CG; iter++) {
        if (rsq < CG_TOL * rsq0 && rsq < CG_TOL) break;
        
        DdagD_op(Ap, p);
        
        double complex pAp = 0;
        for (int i = 0; i < NDOF; i++) pAp += conj(p[i]) * Ap[i];
        
        double complex alpha = rsq / pAp;
        
        double rsq_new = 0;
        for (int i = 0; i < NDOF; i++) {
            x[i] += alpha * p[i];
            r[i] -= alpha * Ap[i];
            rsq_new += creal(conj(r[i]) * r[i]);
        }
        
        double beta = rsq_new / rsq;
        for (int i = 0; i < NDOF; i++)
            p[i] = r[i] + beta * p[i];
        
        rsq = rsq_new;
    }
    
    free(r); free(p); free(Ap);
    return iter;
}

/* ================================================================
 * Pseudofermion Action and Force
 * ================================================================ */

/* Generate pseudofermion: φ = (D†D + m²)^{1/2} η where η ~ N(0,1) */
static double complex *phi;  /* Pseudofermion field */

static void generate_pseudofermion(void) {
    double complex *eta_pf = (double complex*)malloc(NDOF * sizeof(double complex));
    
    /* Gaussian random vector */
    for (int i = 0; i < NDOF; i++) {
        double u1 = (double)rand()/RAND_MAX;
        double u2 = (double)rand()/RAND_MAX;
        if (u1 < 1e-15) u1 = 1e-15;
        double r = sqrt(-0.5 * log(u1));
        eta_pf[i] = r * cos(2*M_PI*u2) + I * r * sin(2*M_PI*u2);
    }
    
    /* φ = (D†D + m²)^{1/2} η
     * Approximation: φ = Dη + m·η (valid for m small)
     * Better: use φ = D†η + m·η (then S = η†η is exact Gaussian) 
     * Actually for HMC: just set φ = Dη + m·η, then the action is 
     * S_F = φ†(D†D+m²)^{-1}φ = η†η (exact). */
    
    /* More precisely: φ = (D + m)η, then φ†(D†D+m²)^{-1}φ = η†(D†+m)(D†D+m²)^{-1}(D+m)η
     * This isn't right either. Standard approach:
     * φ = (D†D+m²)^{1/2} η, then S = φ†(D†D+m²)^{-1}φ = η†η.
     * But computing the square root is expensive.
     * 
     * SIMPLEST CORRECT APPROACH: 
     * Set χ = random Gaussian. Set φ = (D + m·I)χ.
     * Then S = φ†[(D†+m)(D+m)]^{-1}φ = χ†χ, which is Gaussian. ✓
     * And (D†+m)(D+m) = D†D + m(D+D†) + m² = D†D + m² (since D†=-D).
     * So S = φ†(D†D+m²)^{-1}φ. ✓
     */
    
    /* φ = D·η + m·η */
    dirac_op(phi, eta_pf);
    for (int i = 0; i < NDOF; i++)
        phi[i] += mass * eta_pf[i];
    
    free(eta_pf);
}

/* Compute fermion action S_F = Nf * φ†(D†D+m²)^{-1}φ */
static double fermion_action(void) {
    double complex *x = (double complex*)malloc(NDOF * sizeof(double complex));
    cg_solve(x, phi);
    
    double S = 0;
    for (int i = 0; i < NDOF; i++)
        S += creal(conj(phi[i]) * x[i]);
    
    free(x);
    return Nf * S;
}

/* Compute fermion force: dS_F/dA_μ(n) for MD evolution
 * F_μ(n) = -Nf * [χ(n) ⊗ ψ†(i+μ) - ψ(i+μ) ⊗ χ†(n)] × η_μ(n)/2
 * where ψ = (D†D+m²)^{-1}φ and χ = D·ψ
 * 
 * More precisely, the force is the traceless anti-Hermitian projection of:
 * F_μ(n) = Nf * η_μ(n)/2 * [U_μ(n) * (ψ(n+μ) ⊗ χ†(n))] 
 * projected onto the Lie algebra.
 */
static void fermion_force(su3_mat *F) {
    double complex *psi = (double complex*)malloc(NDOF * sizeof(double complex));
    double complex *chi = (double complex*)malloc(NDOF * sizeof(double complex));
    
    /* ψ = (D†D+m²)^{-1} φ */
    cg_solve(psi, phi);
    
    /* χ = D·ψ */
    dirac_op(chi, psi);
    
    /* Force for each link */
    for (int n = 0; n < VOL; n++) {
        for (int mu = 0; mu < ND; mu++) {
            int np = fwd[n*ND+mu];
            double e = eta[n*ND+mu];
            
            /* Outer product: M = U_μ(n) * (ψ(n+μ) ⊗ χ†(n))
             * First compute U_μ(n) * ψ(n+μ): this is a color vector */
            su3_vec Upsi;
            for (int a = 0; a < NC; a++) {
                Upsi[a] = 0;
                for (int b = 0; b < NC; b++)
                    Upsi[a] += U[n*ND+mu][a][b] * psi[np*NC+b];
            }
            
            /* M[a][b] = Upsi[a] * conj(chi[n*NC+b]) */
            su3_mat M;
            for (int a = 0; a < NC; a++)
                for (int b = 0; b < NC; b++)
                    M[a][b] = Upsi[a] * conj(chi[n*NC+b]);
            
            /* Also the backward term: U_μ(n) * (χ(n+μ) ⊗ ψ†(n)) */
            su3_vec Uchi;
            for (int a = 0; a < NC; a++) {
                Uchi[a] = 0;
                for (int b = 0; b < NC; b++)
                    Uchi[a] += U[n*ND+mu][a][b] * chi[np*NC+b];
            }
            
            for (int a = 0; a < NC; a++)
                for (int b = 0; b < NC; b++)
                    M[a][b] -= Uchi[a] * conj(psi[n*NC+b]);
            
            /* Scale by Nf * η/2 */
            su3_scale(M, Nf * e * 0.5);
            
            /* Project to traceless anti-Hermitian: F = (M - M†)/2 - tr(M-M†)/(2Nc) */
            su3_mat F_ah;
            double complex tr = 0;
            for (int a = 0; a < NC; a++) {
                for (int b = 0; b < NC; b++)
                    F_ah[a][b] = (M[a][b] - conj(M[b][a])) * 0.5;
                tr += F_ah[a][a];
            }
            tr /= NC;
            for (int a = 0; a < NC; a++)
                F_ah[a][a] -= tr;
            
            su3_copy(F[n*ND+mu], F_ah);
        }
    }
    
    free(psi);
    free(chi);
}

/* ================================================================
 * Momentum (conjugate to gauge links)
 * ================================================================ */

static su3_mat *P;  /* Momenta */

static double kinetic_energy(void) {
    double K = 0;
    for (int i = 0; i < VOL * ND; i++) {
        /* K = (1/2) Tr(P†P) = (1/2) Σ|P_{ab}|² for anti-Hermitian P */
        for (int a = 0; a < NC; a++)
            for (int b = 0; b < NC; b++)
                K += creal(P[i][a][b] * conj(P[i][a][b]));
    }
    return 0.5 * K;
}

static void refresh_momenta(void) {
    for (int i = 0; i < VOL * ND; i++)
        su3_gauss_ah(P[i]);
}

/* ================================================================
 * HMC Molecular Dynamics
 * ================================================================ */

/* Save/restore gauge field for accept/reject */
static su3_mat *U_save;

static void save_gauge(void) {
    memcpy(U_save, U, VOL * ND * sizeof(su3_mat));
}

static void restore_gauge(void) {
    memcpy(U, U_save, VOL * ND * sizeof(su3_mat));
}

/* Leapfrog integrator */
static void md_integrate(void) {
    su3_mat *F = (su3_mat*)malloc(VOL * ND * sizeof(su3_mat));
    su3_mat expP;
    
    /* Half step for momenta */
    fermion_force(F);
    for (int i = 0; i < VOL * ND; i++) {
        su3_axpy(P[i], 0.5*dt, F[i]);
    }
    
    for (int step = 0; step < nsteps; step++) {
        /* Full step for gauge links: U → exp(dt·P) · U */
        for (int i = 0; i < VOL * ND; i++) {
            su3_mat dtP;
            su3_copy(dtP, P[i]);
            su3_scale(dtP, dt);
            su3_exp_ah(expP, dtP);
            su3_mat Unew;
            su3_mul(Unew, expP, U[i]);
            su3_project(Unew);
            su3_copy(U[i], Unew);
        }
        
        /* Full step for momenta (except last) */
        fermion_force(F);
        double fdt = (step < nsteps - 1) ? dt : 0.5*dt;
        for (int i = 0; i < VOL * ND; i++) {
            su3_axpy(P[i], fdt, F[i]);
        }
    }
    
    free(F);
}

/* ================================================================
 * Measurements
 * ================================================================ */

static double measure_plaquette(void) {
    double plaq = 0;
    int count = 0;
    
    for (int n = 0; n < VOL; n++) {
        for (int mu = 0; mu < ND; mu++) {
            for (int nu = mu+1; nu < ND; nu++) {
                int np_mu = fwd[n*ND+mu];
                int np_nu = fwd[n*ND+nu];
                
                su3_mat T1, T2, P_mat;
                su3_mul(T1, U[n*ND+mu], U[np_mu*ND+nu]);
                su3_mul_dag(T2, T1, U[np_nu*ND+mu]);
                su3_mul_dag(P_mat, T2, U[n*ND+nu]);
                
                plaq += creal(su3_trace(P_mat)) / NC;
                count++;
            }
        }
    }
    return plaq / count;
}

/* ================================================================
 * Main HMC
 * ================================================================ */

int main(int argc, char *argv[]) {
    /* Parse arguments */
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-L") == 0 && i+1 < argc) L = atoi(argv[++i]);
        else if (strcmp(argv[i], "-Nf") == 0 && i+1 < argc) Nf = atoi(argv[++i]);
        else if (strcmp(argv[i], "-mass") == 0 && i+1 < argc) mass = atof(argv[++i]);
        else if (strcmp(argv[i], "-dt") == 0 && i+1 < argc) dt = atof(argv[++i]);
        else if (strcmp(argv[i], "-nsteps") == 0 && i+1 < argc) nsteps = atoi(argv[++i]);
        else if (strcmp(argv[i], "-ntraj") == 0 && i+1 < argc) ntraj = atoi(argv[++i]);
        else if (strcmp(argv[i], "-ntherm") == 0 && i+1 < argc) ntherm = atoi(argv[++i]);
        else if (strcmp(argv[i], "-nmeas") == 0 && i+1 < argc) nmeas = atoi(argv[++i]);
        else if (strcmp(argv[i], "-hot") == 0) ; /* handled below */
        else {
            fprintf(stderr, "Usage: %s [-L size] [-Nf flavors] [-mass m] "
                    "[-dt step] [-nsteps n] [-ntraj n] [-ntherm n] [-nmeas n] [-hot]\n", argv[0]);
            return 1;
        }
    }
    
    int hot_start = 0;
    for (int i = 1; i < argc; i++)
        if (strcmp(argv[i], "-hot") == 0) hot_start = 1;
    
    srand(time(NULL));
    
    /* Initialize */
    init_geometry();
    if (hot_start)
        init_gauge_hot();
    else
        init_gauge_cold();
    
    phi = (double complex*)malloc(NDOF * sizeof(double complex));
    P = (su3_mat*)malloc(VOL * ND * sizeof(su3_mat));
    U_save = (su3_mat*)malloc(VOL * ND * sizeof(su3_mat));
    
    printf("================================================================\n");
    printf("OI-Induced Gauge Theory HMC\n");
    printf("================================================================\n");
    printf("L=%d, VOL=%d, NDOF=%d\n", L, VOL, NDOF);
    printf("Nf=%d, mass=%.4f, dt=%.4f, nsteps=%d\n", Nf, mass, dt, nsteps);
    printf("ntraj=%d, ntherm=%d, nmeas=%d\n", ntraj, ntherm, nmeas);
    printf("Start: %s\n", hot_start ? "HOT" : "COLD");
    printf("Initial <P> = %.6f\n", measure_plaquette());
    printf("================================================================\n\n");
    
    /* Expected β_eff from one-loop Π_s */
    /* Π_s(L) computed analytically; for L=8: ~0.303, β_eff ≈ 10.9 */
    
    /* HMC trajectory loop */
    int accept = 0;
    double plaq_sum = 0;
    int plaq_count = 0;
    
    time_t t_start = time(NULL);
    
    for (int traj = 1; traj <= ntherm + ntraj; traj++) {
        /* 1. Refresh momenta */
        refresh_momenta();
        
        /* 2. Generate pseudofermion */
        generate_pseudofermion();
        
        /* 3. Compute initial Hamiltonian */
        double K_old = kinetic_energy();
        double S_old = fermion_action();
        double H_old = K_old + S_old;
        
        /* 4. Save gauge field */
        save_gauge();
        
        /* 5. MD integration */
        md_integrate();
        
        /* 6. Compute final Hamiltonian */
        double K_new = kinetic_energy();
        double S_new = fermion_action();
        double H_new = K_new + S_new;
        
        /* 7. Metropolis accept/reject */
        double dH = H_new - H_old;
        int accepted = 0;
        if (dH < 0 || (double)rand()/RAND_MAX < exp(-dH)) {
            accepted = 1;
            accept++;
        } else {
            restore_gauge();
        }
        
        /* 8. Measure */
        int is_meas = (traj > ntherm) && ((traj - ntherm) % nmeas == 0);
        
        if (is_meas) {
            double plaq = measure_plaquette();
            plaq_sum += plaq;
            plaq_count++;
        }
        
        /* 9. Print status */
        if (traj <= 10 || traj % 10 == 0 || is_meas) {
            double plaq = measure_plaquette();
            double elapsed = difftime(time(NULL), t_start);
            double rate = elapsed / traj;
            
            printf("Traj %4d/%d: <P>=%.6f dH=%+.4f %s [%.0fs, %.1fs/traj]",
                   traj, ntherm+ntraj, plaq, dH, 
                   accepted ? "ACC" : "REJ", elapsed, rate);
            
            if (traj > ntherm && plaq_count > 0) {
                printf("  <P>_avg=%.6f (%d meas)", plaq_sum/plaq_count, plaq_count);
            }
            printf("\n");
            fflush(stdout);
        }
    }
    
    /* Final results */
    double P_final = plaq_sum / plaq_count;
    double g2_eff = 4.0 * NC * (1.0 - P_final) / (NC*NC - 1.0);
    double inv_alpha = 4.0 * M_PI / g2_eff;
    double acc_rate = (double)accept / (ntherm + ntraj);
    
    printf("\n================================================================\n");
    printf("RESULTS\n");
    printf("================================================================\n");
    printf("Acceptance rate: %.1f%%\n", 100.0 * acc_rate);
    printf("<P> = %.6f (%d measurements)\n", P_final, plaq_count);
    printf("g²_eff = %.6f\n", g2_eff);
    printf("1/α_induced = %.4f\n", inv_alpha);
    printf("\n");
    
    /* Compute expected one-loop values */
    /* Π_s(L) values from discrete BZ computation */
    double Pi_s = 0.308;  /* default: continuum limit */
    if (L == 2) Pi_s = 0.000;  /* zero mode dominates */
    else if (L == 3) Pi_s = 0.265;
    else if (L == 4) Pi_s = 0.241;
    else if (L == 6) Pi_s = 0.265;
    else if (L == 8) Pi_s = 0.303;
    else if (L >= 12) Pi_s = 0.308;  /* near continuum */
    double inv_alpha_1loop = 6.0 * Pi_s * 4.0 * M_PI;
    double beta_1loop = 2.0 * NC * inv_alpha_1loop / (4.0 * M_PI);
    
    printf("One-loop prediction: Π_s(L=%d) ≈ %.3f\n", L, Pi_s);
    printf("  1/α₀ = 6×Π_s×4π = %.2f\n", inv_alpha_1loop);
    printf("  β_eff = %.1f\n", beta_1loop);
    printf("  1/α_induced = %.2f\n", inv_alpha);
    printf("  δ₀_ferm(L=%d) = 1/α₀ - 1/α_induced = %.2f\n", L, inv_alpha_1loop - inv_alpha);
    printf("  Required: δ₀_ferm ≈ 19.6\n");
    printf("================================================================\n");
    
    /* Cleanup */
    free(U); free(P); free(U_save); free(phi);
    free(fwd); free(bwd); free(eta);
    
    return 0;
}
