/* effective_extended.c
 *
 * Extended Phase 1 v2 calculation: test 4-point operators (Option C) and
 * cycle-averaged sampling (Option B). These are the two remaining
 * possibilities for fractional-power suppression to emerge from the
 * bare substratum that the basic 2-point uniform-sampling test ruled out.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

typedef uint64_t state_t;

static int Lc = 3;
static int Tc = 1;
static int N_h_samples = 1000;

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

static uint64_t rng_state_x = 12345;
static uint64_t rng_next(void) {
    rng_state_x = rng_state_x * 6364136223846793005ULL + 1442695040888963407ULL;
    return rng_state_x;
}

static inline int spin(int f) { return 2*f - 1; }

#define MAX_SITES 300
static int v_sites[MAX_SITES], h_sites[MAX_SITES];
static int n_v, n_h;

static void compute_partition(int L) {
    n_v = 0; n_h = 0;
    for (int z = 0; z < L; z++) {
        for (int y = 0; y < L; y++) {
            for (int x = 0; x < L; x++) {
                int i = site_idx_g(x, y, z, L);
                if (x == 0) v_sites[n_v++] = i;
                else        h_sites[n_h++] = i;
            }
        }
    }
}

static state_t combine_vh(uint64_t v_state, uint64_t h_state) {
    state_t s = 0;
    for (int j = 0; j < n_v; j++) {
        int site = v_sites[j];
        s = set_f_now(s, site, (v_state >> (2*j)) & 1);
        s = set_f_prev(s, site, (v_state >> (2*j+1)) & 1);
    }
    for (int j = 0; j < n_h; j++) {
        int site = h_sites[j];
        s = set_f_now(s, site, (h_state >> (2*j)) & 1);
        s = set_f_prev(s, site, (h_state >> (2*j+1)) & 1);
    }
    return s;
}

/* 4-point operator: spin product at 4 different visible sites at time T */
static int op_4pt(state_t s_init, int L, int T, int a, int b, int c, int d) {
    state_t s = s_init;
    for (int t = 0; t < T; t++) s = wave_step(s, L);
    return spin(get_f_now(s, a)) * spin(get_f_now(s, b)) *
           spin(get_f_now(s, c)) * spin(get_f_now(s, d));
}

/* Cycle-averaged 2-point operator: instead of evaluating at fixed T,
 * iterate phi until we return to start (orbit length lambda), and average
 * the 2-point operator over the orbit. */
static double op_cycle_avg_2pt(state_t s_init, int L, int max_iter,
                                 int site_a, int site_b) {
    state_t s = s_init;
    long orbit_len = 0;
    double sum = 0;

    /* First find orbit length via Floyd's algorithm */
    state_t tortoise = s_init;
    state_t hare = wave_step(s_init, L);
    long power = 1, lam = 1;
    while (tortoise != hare && lam < max_iter) {
        if (power == lam) {
            tortoise = hare;
            power *= 2;
            lam = 0;
        }
        hare = wave_step(hare, L);
        lam++;
    }
    if (lam >= max_iter) return 0;  /* cycle too long */
    orbit_len = lam;

    /* Now average over orbit */
    for (long k = 0; k < orbit_len; k++) {
        sum += spin(get_f_now(s, site_a)) * spin(get_f_now(s, site_b));
        s = wave_step(s, L);
    }
    return sum / orbit_len;
}

int main(int argc, char *argv[]) {
    if (argc > 1) Lc = atoi(argv[1]);
    if (argc > 2) Tc = atoi(argv[2]);
    if (argc > 3) N_h_samples = atoi(argv[3]);

    printf("===========================================\n");
    printf("Extended Phase 1 v2: 4-point + cycle averaging\n");
    printf("L=%d, T=%d, N_h=%d\n", Lc, Tc, N_h_samples);
    printf("===========================================\n\n");

    compute_partition(Lc);
    printf("Visible: %d sites; Hidden: %d sites\n\n", n_v, n_h);

    /* Pick 4 visible sites for 4-point operator */
    if (n_v < 4) { fprintf(stderr, "Need at least 4 visible sites.\n"); return 1; }
    int a = v_sites[0];
    int b = v_sites[1];
    int c = v_sites[n_v / 2];
    int d = v_sites[n_v - 1];

    int N_v_samp = 200;

    /* ===== Test 1: 4-point operator with uniform-random hidden sampling ===== */
    printf("=== Test 1: 4-point operator O = spin(a)*spin(b)*spin(c)*spin(d) at time T ===\n");
    printf("    Sites a=%d, b=%d, c=%d, d=%d\n", a, b, c, d);
    printf("    %d visible state samples; %d hidden samples each\n\n", N_v_samp, N_h_samples);

    clock_t t_start = clock();

    /* Compute O_T(v) for many v, then decompose */
    double sum_O = 0, sum_O_sq = 0;
    double sum_O_abcd = 0;  /* O * spin(f_a) spin(f_b) spin(f_c) spin(f_d) for visible f */
    double sum_O_a = 0, sum_O_ab = 0;

    for (int kv = 0; kv < N_v_samp; kv++) {
        uint64_t v = rng_next() & ((1ULL << (2*n_v)) - 1);

        /* Read off visible spin values */
        int fa = (v >> 0) & 1;        /* v_sites[0] = a, position 0 */
        int fb = (v >> 2) & 1;        /* v_sites[1] = b, position 1 */
        int fc = (v >> (2 * (n_v/2))) & 1;  /* v_sites[n_v/2] = c */
        int fd = (v >> (2 * (n_v-1))) & 1;  /* v_sites[n_v-1] = d */

        double O_avg = 0;
        for (int kh = 0; kh < N_h_samples; kh++) {
            uint64_t h = rng_next();
            state_t s = combine_vh(v, h);
            O_avg += op_4pt(s, Lc, Tc, a, b, c, d);
        }
        O_avg /= N_h_samples;

        sum_O += O_avg;
        sum_O_sq += O_avg * O_avg;
        sum_O_abcd += O_avg * spin(fa) * spin(fb) * spin(fc) * spin(fd);
        sum_O_a += O_avg * spin(fa);
        sum_O_ab += O_avg * spin(fa) * spin(fb);
    }

    double c_0 = sum_O / N_v_samp;
    double c_abcd = sum_O_abcd / N_v_samp;
    double c_a = sum_O_a / N_v_samp;
    double c_ab = sum_O_ab / N_v_samp;
    double var_O = sum_O_sq / N_v_samp - c_0*c_0;

    printf("  c_0                       : %10.6f\n", c_0);
    printf("  c_abcd (visible 4-pt)     : %10.6f\n", c_abcd);
    printf("  c_a                       : %10.6f\n", c_a);
    printf("  c_ab (visible 2-pt)       : %10.6f\n", c_ab);
    printf("  variance of O over v      : %10.6f\n", var_O);
    printf("\n");

    /* ===== Test 2: Cycle-averaged 2-point operator ===== */
    printf("=== Test 2: Cycle-averaged 2-point operator ===\n");
    printf("    Site_a = %d, site_b = %d (visible sites)\n", a, b);
    printf("    %d sample (v,h) pairs; orbit-averaged each\n\n", N_v_samp);

    sum_O = sum_O_sq = sum_O_ab = sum_O_a = 0;
    int total_orbits = 0;
    long total_orbit_len = 0;
    long max_orbit = 0;

    for (int kv = 0; kv < N_v_samp; kv++) {
        uint64_t v = rng_next() & ((1ULL << (2*n_v)) - 1);
        int fa = (v >> 0) & 1;
        int fb = (v >> 2) & 1;

        /* Average over hidden samples, each weighted by cycle-average of operator */
        double O_avg = 0;
        for (int kh = 0; kh < N_h_samples; kh++) {
            uint64_t h = rng_next();
            state_t s = combine_vh(v, h);
            O_avg += op_cycle_avg_2pt(s, Lc, 10000000, a, b);
        }
        O_avg /= N_h_samples;

        sum_O += O_avg;
        sum_O_sq += O_avg * O_avg;
        sum_O_ab += O_avg * spin(fa) * spin(fb);
        sum_O_a += O_avg * spin(fa);
    }

    c_0 = sum_O / N_v_samp;
    c_ab = sum_O_ab / N_v_samp;
    c_a = sum_O_a / N_v_samp;
    var_O = sum_O_sq / N_v_samp - c_0*c_0;

    printf("  c_0                       : %10.6f\n", c_0);
    printf("  c_ab (visible 2-pt)       : %10.6f\n", c_ab);
    printf("  c_a                       : %10.6f\n", c_a);
    printf("  variance of O over v      : %10.6f\n", var_O);
    printf("\n");

    clock_t t_end = clock();
    printf("Elapsed: %.3f s\n", (double)(t_end - t_start)/CLOCKS_PER_SEC);

    printf("\n");
    printf("=== Interpretation ===\n");
    printf("Test 1: If c_abcd is non-zero and consistent across N_h, the trace-out\n");
    printf("  preserves the 4-point operator structure even though it kills 2-point.\n");
    printf("  This would indicate non-trivial effective theory at the 4-point level.\n");
    printf("\n");
    printf("Test 2: If c_ab from cycle-averaging differs from T-fixed measurement,\n");
    printf("  the orbit structure provides additional structure that uniform random\n");
    printf("  averaging misses.\n");

    return 0;
}
