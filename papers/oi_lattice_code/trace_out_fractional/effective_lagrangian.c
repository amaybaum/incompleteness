/* effective_lagrangian.c
 *
 * Phase 1 Deliverable 2v2: Effective Lagrangian extraction.
 *
 * For each visible state v, compute the conditional expectation:
 *   O_T(v) = (1/N_h) sum_h O(phi^T(combine(v, h)))
 *
 * where O is a chosen full-lattice operator, and average over hidden initial conditions
 * propagates information from hidden sites into the visible-sector observable.
 *
 * Then decompose O_T(v) as a function of v in the basis of visible-sector operators:
 *   O_T(v) = c_0 + sum_{i,j in V} c_{ij} spin(f_i) spin(f_j) + (higher-order)
 *
 * The coefficients c_n are the effective couplings; their scaling with L is the test.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

/* Parameters - configurable via command line */
static int Lc = 3;        /* lattice size */
static int Tc = 1;        /* time-evolution depth */
static int N_h_samples = 1000;  /* hidden states sampled per visible state */

/* For L=3, q=2: 27 sites, each with (f_now, f_prev) of 1 bit each = 54 bits */
typedef uint64_t state_t;

static inline int site_idx_g(int x, int y, int z, int L) {
    x = ((x % L) + L) % L;
    y = ((y % L) + L) % L;
    z = ((z % L) + L) % L;
    return x + L*y + L*L*z;
}

static inline int get_f_now(state_t s, int i) { return (s >> (2*i)) & 1; }
static inline int get_f_prev(state_t s, int i) { return (s >> (2*i + 1)) & 1; }
static inline state_t set_f_now(state_t s, int i, int v) {
    uint64_t mask = (uint64_t)1 << (2*i);
    return (s & ~mask) | (((uint64_t)(v & 1)) << (2*i));
}
static inline state_t set_f_prev(state_t s, int i, int v) {
    uint64_t mask = (uint64_t)1 << (2*i + 1);
    return (s & ~mask) | (((uint64_t)(v & 1)) << (2*i + 1));
}

/* Wave equation step */
static state_t wave_step(state_t s, int L) {
    state_t s_new = 0;
    for (int z = 0; z < L; z++) {
        for (int y = 0; y < L; y++) {
            for (int x = 0; x < L; x++) {
                int i = site_idx_g(x, y, z, L);
                int f_prev = get_f_prev(s, i);

                int sum = 0;
                sum += get_f_now(s, site_idx_g(x+1, y, z, L));
                sum += get_f_now(s, site_idx_g(x-1, y, z, L));
                sum += get_f_now(s, site_idx_g(x, y+1, z, L));
                sum += get_f_now(s, site_idx_g(x, y-1, z, L));
                sum += get_f_now(s, site_idx_g(x, y, z+1, L));
                sum += get_f_now(s, site_idx_g(x, y, z-1, L));

                int f_next = ((sum - f_prev) % 2 + 2) % 2;
                int f_now = get_f_now(s, i);
                s_new = set_f_now(s_new, i, f_next);
                s_new = set_f_prev(s_new, i, f_now);
            }
        }
    }
    return s_new;
}

/* PRNG */
static uint64_t rng_state_x = 12345;
static uint64_t rng_next(void) {
    rng_state_x = rng_state_x * 6364136223846793005ULL + 1442695040888963407ULL;
    return rng_state_x;
}

static inline int spin(int f) { return 2*f - 1; }

/* Visible sites for L=3: x=0 face, 9 sites with indices y + L*z (since x=0).
 * Hidden sites: x in {1, 2}, 18 sites total.
 */

#define MAX_V_SITES 36   /* up to L=2 visible plane in higher L */
#define MAX_H_SITES 200  /* up to L=6 hidden region */

static int v_sites[MAX_V_SITES];
static int h_sites[MAX_H_SITES];
static int n_v_sites, n_h_sites;

static void compute_partition(int L) {
    n_v_sites = 0; n_h_sites = 0;
    for (int z = 0; z < L; z++) {
        for (int y = 0; y < L; y++) {
            for (int x = 0; x < L; x++) {
                int i = site_idx_g(x, y, z, L);
                if (x == 0) v_sites[n_v_sites++] = i;
                else        h_sites[n_h_sites++] = i;
            }
        }
    }
}

/* Build state from visible (v_state) and hidden (h_state) bit patterns.
 * v_state has 2*n_v_sites low bits (f_now then f_prev for each visible site)
 * h_state similarly.
 */
static state_t combine_vh(uint64_t v_state, uint64_t h_state) {
    state_t s = 0;
    for (int j = 0; j < n_v_sites; j++) {
        int site = v_sites[j];
        int fn = (v_state >> (2*j)) & 1;
        int fp = (v_state >> (2*j + 1)) & 1;
        s = set_f_now(s, site, fn);
        s = set_f_prev(s, site, fp);
    }
    for (int j = 0; j < n_h_sites; j++) {
        int site = h_sites[j];
        int fn = (h_state >> (2*j)) & 1;
        int fp = (h_state >> (2*j + 1)) & 1;
        s = set_f_now(s, site, fn);
        s = set_f_prev(s, site, fp);
    }
    return s;
}

/* Random hidden state with 2*n_h_sites bits */
static uint64_t random_hidden(void) {
    /* For n_h_sites=18 we need 36 bits; use lower bits of rng */
    return rng_next();
}

/* The operator we measure: two-point correlator of f(x_a, t=T) * f(x_b, t=T)
 * where x_a, x_b are visible sites (indices 0 and last visible).
 */
static int op_2pt_T(state_t s_init, int L, int T, int site_a, int site_b) {
    state_t s = s_init;
    for (int t = 0; t < T; t++) s = wave_step(s, L);
    return spin(get_f_now(s, site_a)) * spin(get_f_now(s, site_b));
}

/* Four-point correlator: spin product at four visible sites at time T */
static int op_4pt_T(state_t s_init, int L, int T,
                    int site_a, int site_b, int site_c, int site_d) {
    state_t s = s_init;
    for (int t = 0; t < T; t++) s = wave_step(s, L);
    return spin(get_f_now(s, site_a)) * spin(get_f_now(s, site_b)) *
           spin(get_f_now(s, site_c)) * spin(get_f_now(s, site_d));
}

/* Compute O_T(v) by averaging over hidden samples */
static double compute_O_T_2pt(uint64_t v_state, int L, int T, int site_a, int site_b) {
    double sum = 0;
    for (int k = 0; k < N_h_samples; k++) {
        uint64_t h = random_hidden();
        state_t s_init = combine_vh(v_state, h);
        sum += op_2pt_T(s_init, L, T, site_a, site_b);
    }
    return sum / N_h_samples;
}

static double compute_O_T_4pt(uint64_t v_state, int L, int T,
                              int a, int b, int c, int d) {
    double sum = 0;
    for (int k = 0; k < N_h_samples; k++) {
        uint64_t h = random_hidden();
        state_t s_init = combine_vh(v_state, h);
        sum += op_4pt_T(s_init, L, T, a, b, c, d);
    }
    return sum / N_h_samples;
}

/* Sample visible states uniformly (we don't enumerate all 2^18 for L=3 - too many for stat). */
static uint64_t random_visible(void) {
    /* We need 2*n_v_sites bits; for L=3 that's 18 bits */
    return rng_next() & ((1ULL << (2 * n_v_sites)) - 1);
}

/* Extract effective coefficients by inner product with visible-operator basis.
 * For 2-point op O on visible sites a, b: c_0, c_a, c_b, c_ab.
 * The decomposition: O_T(v) = c_0 + c_a spin(f_a) + c_b spin(f_b) + c_ab spin(f_a) spin(f_b) + ...
 *
 * For symmetry reasons (uniform random over visible space), terms involving f_prev
 * separately from f_now contribute. So we should track operators in f_now AND f_prev
 * separately.
 */

int main(int argc, char *argv[]) {
    if (argc > 1) Lc = atoi(argv[1]);
    if (argc > 2) Tc = atoi(argv[2]);
    if (argc > 3) N_h_samples = atoi(argv[3]);

    printf("===========================================\n");
    printf("Phase 1 Deliverable 2v2: Effective Lagrangian extraction\n");
    printf("L = %d, T = %d, N_h_samples = %d\n", Lc, Tc, N_h_samples);
    printf("===========================================\n\n");

    compute_partition(Lc);
    printf("Partition: visible = %d sites (x=0 face), hidden = %d sites\n",
           n_v_sites, n_h_sites);
    printf("Visible state space: 2^%d = %llu states\n",
           2*n_v_sites, (unsigned long long)(1ULL << (2*n_v_sites)));
    printf("Hidden state space: 2^%d\n\n", 2*n_h_sites);

    /* Choose two visible sites for the 2-point operator */
    int site_a = v_sites[0];        /* first visible site */
    int site_b = v_sites[n_v_sites - 1];  /* last visible site */

    printf("=== 2-point correlator O = spin(f(a,T)) * spin(f(b,T)) ===\n");
    printf("    site_a = %d, site_b = %d\n", site_a, site_b);
    printf("    averaging over N_h = %d hidden samples per visible state\n", N_h_samples);
    printf("    sampling visible states (not exhaustive)\n\n");

    /* Sample N_v_samples visible states; compute O_T(v) for each */
    int N_v_samples = 200;

    double sum_O = 0, sum_O_sq = 0;
    double sum_O_times_spin_a_now = 0;
    double sum_O_times_spin_b_now = 0;
    double sum_O_times_spin_ab_now = 0;
    double sum_O_times_spin_a_prev = 0;
    double sum_O_times_spin_ab_now_prev = 0;
    double sum_spin_a_now_sq = 0, sum_spin_ab_now_sq = 0;

    clock_t t_start = clock();

    for (int kv = 0; kv < N_v_samples; kv++) {
        uint64_t v = random_visible();

        /* Extract visible spin values for site_a and site_b */
        int v_site_a_index = 0;  /* find position of site_a in v_sites */
        int v_site_b_index = n_v_sites - 1;
        int fa_now = (v >> (2*v_site_a_index)) & 1;
        int fa_prev = (v >> (2*v_site_a_index + 1)) & 1;
        int fb_now = (v >> (2*v_site_b_index)) & 1;

        double O = compute_O_T_2pt(v, Lc, Tc, site_a, site_b);

        sum_O += O;
        sum_O_sq += O*O;
        sum_O_times_spin_a_now += O * spin(fa_now);
        sum_O_times_spin_b_now += O * spin(fb_now);
        sum_O_times_spin_ab_now += O * spin(fa_now) * spin(fb_now);
        sum_O_times_spin_a_prev += O * spin(fa_prev);
        sum_O_times_spin_ab_now_prev += O * spin(fa_now) * spin(fa_prev);
        sum_spin_a_now_sq += spin(fa_now) * spin(fa_now);
        sum_spin_ab_now_sq += (spin(fa_now) * spin(fb_now)) * (spin(fa_now) * spin(fb_now));
    }

    double c_0 = sum_O / N_v_samples;
    double c_a_now = sum_O_times_spin_a_now / N_v_samples;
    double c_b_now = sum_O_times_spin_b_now / N_v_samples;
    double c_ab_now = sum_O_times_spin_ab_now / N_v_samples;
    double c_a_prev = sum_O_times_spin_a_prev / N_v_samples;
    double c_ab_now_prev = sum_O_times_spin_ab_now_prev / N_v_samples;

    double mean_O = c_0;
    double var_O = sum_O_sq / N_v_samples - mean_O*mean_O;

    clock_t t_end = clock();
    double elapsed = (double)(t_end - t_start) / CLOCKS_PER_SEC;

    printf("=== Effective coefficients (inner products) ===\n");
    printf("  c_0     (constant)              : %10.6f\n", c_0);
    printf("  c_a_now (spin f_now at a)       : %10.6f\n", c_a_now);
    printf("  c_b_now (spin f_now at b)       : %10.6f\n", c_b_now);
    printf("  c_ab_now (spin f_now a * f_now b): %10.6f\n", c_ab_now);
    printf("  c_a_prev (spin f_prev at a)     : %10.6f\n", c_a_prev);
    printf("  c_ab_now_prev (mixed a_now a_prev): %10.6f\n", c_ab_now_prev);
    printf("\n");
    printf("  Total variance of O over v:    %.6f\n", var_O);
    printf("\n");

    printf("=== Interpretation ===\n");
    printf("Non-zero c_ab_now means the effective theory has a 2-point coupling between\n");
    printf("visible sites a and b. Its magnitude is the effective coupling for this operator.\n");
    printf("\n");
    printf("If c_ab_now (or c_a_now, c_b_now) is non-zero, trace-out has produced a visible-\n");
    printf("sector EFT with that operator content. The scaling of c_ab_now with L is the\n");
    printf("fractional-power test (varies separately).\n");
    printf("\n");
    printf("Comparison to T=0 expectation:\n");
    printf("  At T=0: O = spin(f_a) * spin(f_b), purely visible. Trivially c_ab_now = 1,\n");
    printf("    all other c_n = 0.\n");
    printf("  At T>=1: linear wave eq propagates through hidden; if kernel hits hidden,\n");
    printf("    expectation over uniform h gives c_n = 0 in that channel.\n");
    printf("\n");

    printf("Elapsed: %.3f s\n", elapsed);

    return 0;
}
