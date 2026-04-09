/*
 * metropolis_plaquette.c — Pure-gauge Wilson plaquette via Metropolis
 *
 * Computes the average plaquette ⟨P⟩ for pure SU(2) or SU(3) lattice gauge
 * theory with the standard Wilson action
 *
 *      S = (β/N_c) Σ_p (N_c − Re Tr U_p)
 *
 * using a multi-hit Metropolis update. Each link is updated by proposing
 * U_new = R × U_old, where R is a small SU(N) random rotation, and
 * accepting with probability min(1, exp(−ΔS)).
 *
 * Multi-hit Metropolis is slower than heat-bath but is also far simpler and
 * easier to verify. For the parameters of interest (4⁴ lattices, ~10³–10⁴
 * sweeps), it runs in seconds and produces correct equilibrium averages.
 *
 * Conventions:
 *   β = 2 N_c / g₀² (standard Wilson convention)
 *   ⟨P⟩ = (1 / (V × N_dim(N_dim−1)/2 × N_c)) Σ_x Σ_{μ<ν} Re Tr P_{μν}(x)
 *
 * Defaults match the values referenced in
 *   Maybaum, "The Standard Model from a Cubic Lattice," §6.4
 *   - SU(2) at β = 7.4 on a 4⁴ lattice
 *   - SU(3) at β = 11.1 on a 4⁴ lattice
 *
 * Compile:  gcc -O3 -o metropolis_plaquette metropolis_plaquette.c -lm
 * Usage:    ./metropolis_plaquette [Nc] [L] [beta] [ntherm] [nmeas] [nsep] [n_hits] [step]
 *           Defaults: Nc=3, L=4, beta=11.1, ntherm=2000, nmeas=2000, nsep=2,
 *                     n_hits=10, step=0.3
 *
 * To reproduce both SM §6.4 numbers, run:
 *   ./metropolis_plaquette 2 4 7.4   2000 2000 2 10 0.3
 *   ./metropolis_plaquette 3 4 11.1  2000 2000 2 10 0.3
 *
 * Tip: monitor the acceptance rate printed during thermalization. If it is
 *      consistently below ~30% or above ~70%, adjust the `step` parameter
 *      (smaller step → higher acceptance, larger step → lower acceptance).
 *      Target acceptance for Metropolis is 40–60%.
 *
 * Author: Generated as part of the OI lattice code release.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define ND 4                        /* spacetime dimensions */
#define MAX_NC 3                    /* supports SU(2) and SU(3) */

/* ---------- Globals (set in main) ---------- */
static int Nc = 3;
static int L  = 4;
static int VOL;
static double beta = 11.1;
static int n_hits = 10;
static double step = 0.3;

/* ---------- xorshift RNG (sufficient for Metropolis) ---------- */
static unsigned long long rng_state = 0;

static void rng_seed(unsigned long long s) {
    rng_state = s ? s : 88172645463325252ull;
}

static double rng_uniform(void) {
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 7;
    rng_state ^= rng_state << 17;
    /* return uniform double in (0, 1) */
    return ((double)((rng_state >> 11) | 1) + 1.0) / 9007199254740994.0;
}

static double rng_gauss(void) {
    /* Box-Muller; returns one Gaussian per call (the second is discarded) */
    double u1 = rng_uniform();
    double u2 = rng_uniform();
    return sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2);
}

/* ---------- Geometry: 4D hypercubic lattice with periodic BCs ---------- */
static int site_idx(int nx, int ny, int nz, int nt) {
    return ((nt*L + nz)*L + ny)*L + nx;
}

static void site_coords(int s, int *nx, int *ny, int *nz, int *nt) {
    *nx = s % L;       s /= L;
    *ny = s % L;       s /= L;
    *nz = s % L;       s /= L;
    *nt = s;
}

static int neighbor(int s, int mu, int sign) {
    int n[ND];
    site_coords(s, &n[0], &n[1], &n[2], &n[3]);
    n[mu] = (n[mu] + sign + L) % L;
    return site_idx(n[0], n[1], n[2], n[3]);
}

/* ---------- Complex Nc×Nc matrix ---------- */
typedef struct { double re, im; } Cx;
typedef struct { Cx e[3][3]; } Mat;

static Cx cx(double r, double i) { Cx z; z.re = r; z.im = i; return z; }
static Cx cxadd(Cx a, Cx b)      { return cx(a.re + b.re, a.im + b.im); }
static Cx cxsub(Cx a, Cx b)      { return cx(a.re - b.re, a.im - b.im); }
static Cx cxmul(Cx a, Cx b)      { return cx(a.re*b.re - a.im*b.im, a.re*b.im + a.im*b.re); }
static Cx cxconj(Cx a)           { return cx(a.re, -a.im); }
static double cxabs2(Cx a)       { return a.re*a.re + a.im*a.im; }

static void mat_zero(Mat *A) { memset(A, 0, sizeof(*A)); }

static void mat_unit(Mat *A) {
    mat_zero(A);
    for (int i = 0; i < Nc; i++) A->e[i][i] = cx(1, 0);
}

static void mat_mul(Mat *C, const Mat *A, const Mat *B) {
    Mat tmp; mat_zero(&tmp);
    for (int i = 0; i < Nc; i++)
    for (int j = 0; j < Nc; j++) {
        Cx s = cx(0, 0);
        for (int k = 0; k < Nc; k++)
            s = cxadd(s, cxmul(A->e[i][k], B->e[k][j]));
        tmp.e[i][j] = s;
    }
    *C = tmp;
}

static void mat_dag(Mat *D, const Mat *A) {
    Mat tmp; mat_zero(&tmp);
    for (int i = 0; i < Nc; i++)
    for (int j = 0; j < Nc; j++)
        tmp.e[i][j] = cxconj(A->e[j][i]);
    *D = tmp;
}

static void mat_add(Mat *C, const Mat *A, const Mat *B) {
    Mat tmp; mat_zero(&tmp);
    for (int i = 0; i < Nc; i++)
    for (int j = 0; j < Nc; j++)
        tmp.e[i][j] = cxadd(A->e[i][j], B->e[i][j]);
    *C = tmp;
}

static void mat_sub(Mat *C, const Mat *A, const Mat *B) {
    Mat tmp; mat_zero(&tmp);
    for (int i = 0; i < Nc; i++)
    for (int j = 0; j < Nc; j++)
        tmp.e[i][j] = cxsub(A->e[i][j], B->e[i][j]);
    *C = tmp;
}

static double mat_retrace(const Mat *A) {
    double t = 0;
    for (int i = 0; i < Nc; i++) t += A->e[i][i].re;
    return t;
}

/* Reunitarize via modified Gram-Schmidt */
static void mat_reunit(Mat *A) {
    /* Row 0 */
    double n0 = 0;
    for (int j = 0; j < Nc; j++) n0 += cxabs2(A->e[0][j]);
    n0 = 1.0 / sqrt(n0);
    for (int j = 0; j < Nc; j++) {
        A->e[0][j].re *= n0;
        A->e[0][j].im *= n0;
    }
    /* Row 1 */
    Cx dot = cx(0, 0);
    for (int j = 0; j < Nc; j++)
        dot = cxadd(dot, cxmul(cxconj(A->e[0][j]), A->e[1][j]));
    for (int j = 0; j < Nc; j++)
        A->e[1][j] = cxsub(A->e[1][j], cxmul(dot, A->e[0][j]));
    double n1 = 0;
    for (int j = 0; j < Nc; j++) n1 += cxabs2(A->e[1][j]);
    n1 = 1.0 / sqrt(n1);
    for (int j = 0; j < Nc; j++) {
        A->e[1][j].re *= n1;
        A->e[1][j].im *= n1;
    }
    if (Nc == 3) {
        /* Row 2 = (row 0 × row 1)*  (cross product, then conjugate) */
        Cx a = A->e[0][0], b = A->e[0][1], c = A->e[0][2];
        Cx d = A->e[1][0], e = A->e[1][1], f = A->e[1][2];
        A->e[2][0] = cxconj(cxsub(cxmul(b, f), cxmul(c, e)));
        A->e[2][1] = cxconj(cxsub(cxmul(c, d), cxmul(a, f)));
        A->e[2][2] = cxconj(cxsub(cxmul(a, e), cxmul(b, d)));
    }
}

/* ---------- Random small SU(N) rotation ---------- */
/* For SU(2): build U = exp(i ε σ⃗·n̂) for random unit vector n̂, small ε */
static void random_su2(Mat *R, double eps) {
    double n[3];
    do {
        n[0] = rng_gauss();
        n[1] = rng_gauss();
        n[2] = rng_gauss();
    } while (n[0]*n[0] + n[1]*n[1] + n[2]*n[2] < 1e-10);
    double nrm = 1.0 / sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);
    for (int i = 0; i < 3; i++) n[i] *= nrm;
    double angle = eps * (2.0 * rng_uniform() - 1.0);
    double c = cos(angle), s = sin(angle);
    mat_zero(R);
    R->e[0][0] = cx( c,  s * n[2]);
    R->e[0][1] = cx( s * n[1],  s * n[0]);
    R->e[1][0] = cx(-s * n[1],  s * n[0]);
    R->e[1][1] = cx( c, -s * n[2]);
    if (Nc == 3) R->e[2][2] = cx(1, 0);
}

/* For SU(3): random update via three sequential SU(2) sub-rotations on
 * the (0,1), (0,2), (1,2) blocks. This generates SU(3) elements, with
 * step size controlled by `eps`. */
static void random_su2_in_su3(Mat *R, int p, int q, double eps) {
    double n[3];
    do {
        n[0] = rng_gauss();
        n[1] = rng_gauss();
        n[2] = rng_gauss();
    } while (n[0]*n[0] + n[1]*n[1] + n[2]*n[2] < 1e-10);
    double nrm = 1.0 / sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);
    for (int i = 0; i < 3; i++) n[i] *= nrm;
    double angle = eps * (2.0 * rng_uniform() - 1.0);
    double c = cos(angle), s = sin(angle);
    mat_unit(R);
    R->e[p][p] = cx( c,  s * n[2]);
    R->e[p][q] = cx( s * n[1],  s * n[0]);
    R->e[q][p] = cx(-s * n[1],  s * n[0]);
    R->e[q][q] = cx( c, -s * n[2]);
}

/* ---------- Field storage: U[site][mu] ---------- */
static Mat *U_field = NULL;
#define U(s, mu) (U_field[(s)*ND + (mu)])

static void allocate_field(void) {
    VOL = 1;
    for (int mu = 0; mu < ND; mu++) VOL *= L;
    U_field = (Mat*) calloc((size_t)VOL * ND, sizeof(Mat));
}

static void cold_start(void) {
    for (int s = 0; s < VOL; s++)
        for (int mu = 0; mu < ND; mu++)
            mat_unit(&U(s, mu));
}

/* ---------- Plaquette ---------- */
static double avg_plaquette(void) {
    double sum = 0;
    long n_plaq = 0;
    for (int s = 0; s < VOL; s++) {
        for (int mu = 0; mu < ND; mu++)
        for (int nu = mu + 1; nu < ND; nu++) {
            int s_mu = neighbor(s, mu, +1);
            int s_nu = neighbor(s, nu, +1);
            Mat A, B, P, Udag1, Udag2;
            mat_mul(&A, &U(s, mu), &U(s_mu, nu));
            mat_dag(&Udag1, &U(s_nu, mu));
            mat_mul(&B, &A, &Udag1);
            mat_dag(&Udag2, &U(s, nu));
            mat_mul(&P, &B, &Udag2);
            sum += mat_retrace(&P);
            n_plaq++;
        }
    }
    return sum / ((double)n_plaq * Nc);
}

/* ---------- Staple sum for link (s, mu) ---------- */
/* A_total = Σ_{ν≠μ} [ U_ν(s+μ̂) U_μ†(s+ν̂) U_ν†(s)
 *                   + U_ν†(s+μ̂−ν̂) U_μ†(s−ν̂) U_ν(s−ν̂) ] */
static void staple_sum(Mat *S, int s, int mu) {
    mat_zero(S);
    int s_mu = neighbor(s, mu, +1);
    Mat A, B, Udag, Tmp;
    for (int nu = 0; nu < ND; nu++) {
        if (nu == mu) continue;
        int s_nu = neighbor(s, nu, +1);
        int s_nm = neighbor(s, nu, -1);
        int s_mu_nm = neighbor(s_mu, nu, -1);

        /* Forward staple */
        mat_dag(&Udag, &U(s_nu, mu));
        mat_mul(&A, &U(s_mu, nu), &Udag);
        mat_dag(&Udag, &U(s, nu));
        mat_mul(&B, &A, &Udag);
        mat_add(&Tmp, S, &B);
        *S = Tmp;

        /* Backward staple */
        Mat Unm_nu_dag, Unm_mu_dag;
        mat_dag(&Unm_nu_dag, &U(s_mu_nm, nu));
        mat_dag(&Unm_mu_dag, &U(s_nm, mu));
        mat_mul(&A, &Unm_nu_dag, &Unm_mu_dag);
        mat_mul(&B, &A, &U(s_nm, nu));
        mat_add(&Tmp, S, &B);
        *S = Tmp;
    }
}

/* ---------- Local action contribution from link U(s, mu) ---------- */
/* S_local = -(β/N_c) Re Tr(U(s, mu) × A_total) where A_total is the staple */
static double local_action(const Mat *U_link, const Mat *staple) {
    Mat M;
    mat_mul(&M, U_link, staple);
    return -(beta / Nc) * mat_retrace(&M);
}

/* ---------- Multi-hit Metropolis update of one link ---------- */
static long n_acc = 0, n_try = 0;

static void metropolis_link(int s, int mu) {
    Mat S;
    staple_sum(&S, s, mu);
    double S_old = local_action(&U(s, mu), &S);
    for (int hit = 0; hit < n_hits; hit++) {
        Mat R, U_new, U_old;
        U_old = U(s, mu);
        if (Nc == 2) {
            random_su2(&R, step);
        } else {
            /* Cycle through 3 SU(2) subgroups */
            int sub = hit % 3;
            int p = (sub == 0) ? 0 : (sub == 1) ? 0 : 1;
            int q = (sub == 0) ? 1 : (sub == 1) ? 2 : 2;
            random_su2_in_su3(&R, p, q, step);
        }
        mat_mul(&U_new, &R, &U_old);
        double S_new = local_action(&U_new, &S);
        double dS = S_new - S_old;
        n_try++;
        if (dS <= 0 || rng_uniform() < exp(-dS)) {
            U(s, mu) = U_new;
            S_old = S_new;
            n_acc++;
        }
    }
    mat_reunit(&U(s, mu));
}

/* ---------- One sweep through the lattice ---------- */
static void sweep(void) {
    for (int s = 0; s < VOL; s++)
        for (int mu = 0; mu < ND; mu++)
            metropolis_link(s, mu);
}

/* ---------- Main ---------- */
int main(int argc, char *argv[]) {
    int ntherm = 2000, nmeas = 2000, nsep = 2;

    if (argc > 1) Nc     = atoi(argv[1]);
    if (argc > 2) L      = atoi(argv[2]);
    if (argc > 3) beta   = atof(argv[3]);
    if (argc > 4) ntherm = atoi(argv[4]);
    if (argc > 5) nmeas  = atoi(argv[5]);
    if (argc > 6) nsep   = atoi(argv[6]);
    if (argc > 7) n_hits = atoi(argv[7]);
    if (argc > 8) step   = atof(argv[8]);

    if (Nc != 2 && Nc != 3) {
        fprintf(stderr, "Error: Nc must be 2 or 3 (got %d)\n", Nc);
        return 1;
    }

    rng_seed((unsigned long long)time(NULL) ^ 0x9E3779B97F4A7C15ull);
    allocate_field();
    cold_start();

    printf("# Pure-gauge Wilson plaquette via multi-hit Metropolis\n");
    printf("# Nc      = %d\n", Nc);
    printf("# L       = %d  (4D lattice volume = %d)\n", L, VOL);
    printf("# beta    = %.4f  (g₀² = 2 N_c / β = %.4f)\n",
           beta, 2.0 * Nc / beta);
    printf("# ntherm  = %d sweeps\n", ntherm);
    printf("# nmeas   = %d measurements\n", nmeas);
    printf("# nsep    = %d sweeps between measurements\n", nsep);
    printf("# n_hits  = %d Metropolis hits per link\n", n_hits);
    printf("# step    = %.3f (random rotation amplitude)\n", step);
    printf("#\n");

    /* Thermalization */
    printf("# Thermalizing...\n");
    n_acc = n_try = 0;
    for (int i = 0; i < ntherm; i++) {
        sweep();
        if ((i + 1) % 200 == 0) {
            double acc = (double)n_acc / fmax(1.0, (double)n_try);
            printf("#   sweep %5d  ⟨P⟩ = %.6f  acc = %.3f\n",
                   i + 1, avg_plaquette(), acc);
            n_acc = n_try = 0;
        }
    }

    /* Production */
    printf("# Measuring...\n");
    double sum = 0, sum2 = 0;
    n_acc = n_try = 0;
    for (int m = 0; m < nmeas; m++) {
        for (int i = 0; i < nsep; i++) sweep();
        double P = avg_plaquette();
        sum  += P;
        sum2 += P * P;
        if ((m + 1) % 200 == 0) {
            double mean = sum / (m + 1);
            double err  = (m > 0)
                ? sqrt((sum2 / (m + 1) - mean * mean) / m)
                : 0;
            double acc = (double)n_acc / fmax(1.0, (double)n_try);
            printf("#   meas %5d  ⟨P⟩ = %.6f ± %.6f  acc = %.3f\n",
                   m + 1, mean, err, acc);
        }
    }

    /* Final */
    double mean = sum / nmeas;
    double err  = (nmeas > 1)
        ? sqrt((sum2 / nmeas - mean * mean) / (nmeas - 1))
        : 0;

    printf("\n");
    printf("============================================================\n");
    printf("RESULT: SU(%d) at β = %.4f on %d⁴ lattice\n", Nc, beta, L);
    printf("  ⟨P⟩ = %.6f ± %.6f\n", mean, err);
    printf("============================================================\n");

    /* Reference comparisons */
    if (Nc == 2 && fabs(beta - 7.4) < 0.01 && L == 4) {
        printf("\n");
        printf("SM §6.4 reports ⟨P⟩_SU(2)(β=7.4) = 0.783\n");
        printf("Difference from this run: %+.4f\n", mean - 0.783);
    }
    if (Nc == 3 && fabs(beta - 11.1) < 0.01 && L == 4) {
        printf("\n");
        printf("SM §6.4 reports ⟨P⟩_SU(3)(β=11.1) = 0.806\n");
        printf("Difference from this run: %+.4f\n", mean - 0.806);
        printf("Note: 1-loop perturbative ⟨P⟩ ≈ %.4f\n",
               1.0 - (2.0 / Nc / beta) * (Nc * Nc - 1) / (4.0 * Nc));
    }

    free(U_field);
    return 0;
}
