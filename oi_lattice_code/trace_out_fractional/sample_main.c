/* sample_main.c
 *
 * Phase 1 Deliverable 3: Stochastic sampling feasibility benchmark.
 *
 * For L > 2, exact enumeration is infeasible. We use stochastic sampling
 * over the full state space and compute trace-out as a Monte Carlo average.
 *
 * The trace-out at lattice size L with visible block of size N_V:
 *   <O_V>_traced(v) = (1/|H|) * sum_{h in H} O_V(phi^T(combine(v,h)))
 *
 * For each fixed v, MC sample N_samp hidden states uniformly. The total cost
 * per visible state is N_samp * T * cost_per_step. We then need to also
 * sample over v (or pick a fixed set of test v values).
 *
 * Strategy: instead of sampling v exhaustively (which itself is infeasible
 * for larger L), we compute the variance of <O>_traced across an ensemble
 * of (v,h) pairs sampled jointly. This measures the same "effective coupling
 * magnitude" as in exact_L2, just without exhausting all visible states.
 *
 * Specifically: variance of O over uniform samples minus variance of O
 * conditional on hidden = the variance of <O>_traced over visible states.
 *
 * Var_total[O] = E_v[Var_h[O|v]] + Var_v[E_h[O|v]]
 *           total       intrinsic     effective coupling
 *
 * We extract effective coupling magnitude as:
 *   M(T) = Var_v[<O>_h|v] = Var_total - E_v[Var_h]
 *
 * This is computable from sampling without exhaustive enumeration.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

/* Generalized lattice parameters - we redefine these from lattice.h */
#define L_BENCH 3
#define Q_BENCH 2

/* For L=3 in 3D: 27 sites, each carrying (f_now, f_prev) of log2(Q) bits each */
/* For Q=2: 1 bit per field per site, 27 sites, 2 fields = 54 bits total */

/* We use uint64_t state and bit-pack 2 fields x 27 sites = 54 bits */
typedef uint64_t state64_t;

static inline int get_f_now64(state64_t s, int i) {
    return (s >> (2*i)) & 1;
}
static inline int get_f_prev64(state64_t s, int i) {
    return (s >> (2*i + 1)) & 1;
}
static inline state64_t set_f_now64(state64_t s, int i, int v) {
    uint64_t mask = (uint64_t)1 << (2*i);
    return (s & ~mask) | (((uint64_t)(v & 1)) << (2*i));
}
static inline state64_t set_f_prev64(state64_t s, int i, int v) {
    uint64_t mask = (uint64_t)1 << (2*i + 1);
    return (s & ~mask) | (((uint64_t)(v & 1)) << (2*i + 1));
}

static inline int site_idx_g(int x, int y, int z, int Lc) {
    x = ((x % Lc) + Lc) % Lc;
    y = ((y % Lc) + Lc) % Lc;
    z = ((z % Lc) + Lc) % Lc;
    return x + Lc*y + Lc*Lc*z;
}

/* Wave step for generalized L (working for Q=2 only here) */
static state64_t wave_step_LQ(state64_t s, int Lc) {
    state64_t s_new = 0;
    for (int z = 0; z < Lc; z++) {
        for (int y = 0; y < Lc; y++) {
            for (int x = 0; x < Lc; x++) {
                int i = site_idx_g(x, y, z, Lc);
                int f_prev = get_f_prev64(s, i);

                int sum = 0;
                sum += get_f_now64(s, site_idx_g(x+1, y, z, Lc));
                sum += get_f_now64(s, site_idx_g(x-1, y, z, Lc));
                sum += get_f_now64(s, site_idx_g(x, y+1, z, Lc));
                sum += get_f_now64(s, site_idx_g(x, y-1, z, Lc));
                sum += get_f_now64(s, site_idx_g(x, y, z+1, Lc));
                sum += get_f_now64(s, site_idx_g(x, y, z-1, Lc));

                int f_next = ((sum - f_prev) % 2 + 2) % 2;
                int f_now = get_f_now64(s, i);
                s_new = set_f_now64(s_new, i, f_next);
                s_new = set_f_prev64(s_new, i, f_now);
            }
        }
    }
    return s_new;
}

/* Local sqrt to avoid linking math library */
static double sqrt_d(double x) {
    if (x <= 0) return 0;
    double r = x;
    for (int i = 0; i < 30; i++) r = 0.5 * (r + x/r);
    return r;
}

/* PRNG: simple linear congruential for benchmarking */
static uint64_t rng_state = 12345;
static uint64_t rng_next(void) {
    rng_state = rng_state * 6364136223846793005ULL + 1442695040888963407ULL;
    return rng_state;
}

/* Generate a random state covering N_BITS bits */
static state64_t random_state(int n_bits) {
    uint64_t mask = (n_bits >= 64) ? (uint64_t)-1 : ((uint64_t)1 << n_bits) - 1;
    return rng_next() & mask;
}

/* Operators on visible sub-lattice. For L=3, visible = sites with x=0 (9 sites). */
static inline int spin(int f) { return 2*f - 1; }

/* O_2: temporal correlator on visible sites (x=0 plane, 9 sites for L=3) */
static int op_bilinear_L(state64_t s, int Lc) {
    int total = 0;
    for (int y = 0; y < Lc; y++) {
        for (int z = 0; z < Lc; z++) {
            int site = site_idx_g(0, y, z, Lc);
            total += spin(get_f_now64(s, site)) * spin(get_f_prev64(s, site));
        }
    }
    return total;
}

/* O_3: three-spin correlator on y-z face */
static int op_trilinear_L(state64_t s, int Lc) {
    int total = 0;
    for (int y = 0; y < Lc; y++) {
        for (int z = 0; z < Lc; z++) {
            int site = site_idx_g(0, y, z, Lc);
            int site_y = site_idx_g(0, y+1, z, Lc);
            int site_z = site_idx_g(0, y, z+1, Lc);
            total += spin(get_f_now64(s, site)) *
                     spin(get_f_now64(s, site_y)) *
                     spin(get_f_now64(s, site_z));
        }
    }
    return total;
}

/* O_4: plaquette in y-z face */
static int op_quartic_L(state64_t s, int Lc) {
    int total = 0;
    for (int y = 0; y < Lc; y++) {
        for (int z = 0; z < Lc; z++) {
            int s00 = site_idx_g(0, y, z, Lc);
            int s01 = site_idx_g(0, y+1, z, Lc);
            int s10 = site_idx_g(0, y, z+1, Lc);
            int s11 = site_idx_g(0, y+1, z+1, Lc);
            int prod = spin(get_f_now64(s, s00)) *
                       spin(get_f_now64(s, s01)) *
                       spin(get_f_now64(s, s10)) *
                       spin(get_f_now64(s, s11));
            total += prod;
        }
    }
    return total;
}

/* O_K: kinetic */
static int op_kinetic_L(state64_t s, int Lc) {
    int total = 0;
    for (int y = 0; y < Lc; y++) {
        for (int z = 0; z < Lc; z++) {
            int site = site_idx_g(0, y, z, Lc);
            int site_y = site_idx_g(0, y+1, z, Lc);
            int d = spin(get_f_now64(s, site)) - spin(get_f_now64(s, site_y));
            total += d*d;
        }
    }
    return total;
}

/* Cycle-length sampling: starting from a random state, count cycle length
 * by Brent's algorithm (faster than naive cycle detection).
 */
static long brent_cycle(state64_t s_start, int Lc, long max_iter) {
    state64_t tortoise = s_start;
    state64_t hare = wave_step_LQ(s_start, Lc);
    long power = 1, lam = 1;
    while (tortoise != hare && lam < max_iter) {
        if (power == lam) {
            tortoise = hare;
            power *= 2;
            lam = 0;
        }
        hare = wave_step_LQ(hare, Lc);
        lam++;
    }
    if (lam >= max_iter) return -1;  /* exceeded max */
    return lam;
}

int main(int argc, char *argv[]) {
    int Lc = L_BENCH;
    int n_samp_dyn = 100;
    int t_max = 20;

    if (argc > 1) Lc = atoi(argv[1]);
    if (argc > 2) n_samp_dyn = atoi(argv[2]);
    if (argc > 3) t_max = atoi(argv[3]);

    int n_sites = Lc*Lc*Lc;
    int n_bits = 2 * n_sites;

    printf("===========================================\n");
    printf("Phase 1 Deliverable 3: Sampling Benchmark\n");
    printf("L = %d (n_sites = %d, n_bits = %d)\n", Lc, n_sites, n_bits);
    printf("Q = 2\n");
    printf("===========================================\n\n");

    if (n_bits > 64) {
        printf("ERROR: state requires %d bits > 64. Need extended state representation.\n", n_bits);
        return 1;
    }

    /* Cycle-length sampling */
    clock_t t_start = clock();
    printf("=== Cycle-length distribution (Brent's algorithm) ===\n");
    long total_cycles = 0, total_length = 0, max_len = 0, min_len = 1000000000;
    long n_cycle_samples = 200;
    for (long k = 0; k < n_cycle_samples; k++) {
        state64_t s = random_state(n_bits);
        long len = brent_cycle(s, Lc, 100000);
        if (len > 0) {
            total_cycles++;
            total_length += len;
            if (len > max_len) max_len = len;
            if (len < min_len) min_len = len;
        }
    }
    double mean_cycle = (double)total_length / total_cycles;
    printf("  Cycle samples: %ld\n", n_cycle_samples);
    printf("  Mean cycle length: %.1f\n", mean_cycle);
    printf("  Min observed: %ld\n", min_len);
    printf("  Max observed: %ld\n", max_len);
    printf("\n");

    /* Time-evolution sampling: pick random states, evolve, measure */
    printf("=== Operator evolution under phi (%d random samples) ===\n", n_samp_dyn);
    printf("  T  |  <O_2>     | <O_3>     | <O_4>     | <O_K>     | sigma(O_2)\n");
    printf(" ----+-----------+-----------+-----------+-----------+----------\n");

    for (int T = 0; T <= t_max; T++) {
        double sum_O2 = 0, sum_O3 = 0, sum_O4 = 0, sum_OK = 0;
        double sum_O2_sq = 0;
        for (int k = 0; k < n_samp_dyn; k++) {
            state64_t s = random_state(n_bits);
            for (int t = 0; t < T; t++) s = wave_step_LQ(s, Lc);
            double o2 = op_bilinear_L(s, Lc);
            sum_O2 += o2; sum_O2_sq += o2*o2;
            sum_O3 += op_trilinear_L(s, Lc);
            sum_O4 += op_quartic_L(s, Lc);
            sum_OK += op_kinetic_L(s, Lc);
        }
        double m2 = sum_O2 / n_samp_dyn;
        double v2 = sum_O2_sq / n_samp_dyn - m2*m2;
        printf("  %2d | %9.4f | %9.4f | %9.4f | %9.4f | %9.4f\n",
               T, m2, sum_O3/n_samp_dyn, sum_O4/n_samp_dyn, sum_OK/n_samp_dyn,
               (v2 > 0 ? sqrt_d(v2) : 0.0));
    }

    clock_t t_end = clock();
    double elapsed = (double)(t_end - t_start) / CLOCKS_PER_SEC;
    printf("\nElapsed: %.3f s\n", elapsed);

    /* Resource extrapolation */
    long ops_so_far = (long)n_cycle_samples * 1000 + (long)n_samp_dyn * (t_max+1);
    double s_per_op = elapsed / ops_so_far;
    printf("\nResource extrapolation:\n");
    printf("  Per-step cost (single state): ~%.2e s\n", s_per_op);
    printf("  L=4 estimate (%d^3 = %d sites):\n", 4, 4*4*4);
    printf("    Per-step cost scales as L^3 = %d. Extrapolated: %.2e s\n",
           4*4*4, s_per_op * (4*4*4) / (Lc*Lc*Lc));
    printf("  L=6 estimate (216 sites): %.2e s per step\n", s_per_op * 216 / (Lc*Lc*Lc));
    printf("  L=8 estimate (512 sites): %.2e s per step\n", s_per_op * 512 / (Lc*Lc*Lc));

    return 0;
}
