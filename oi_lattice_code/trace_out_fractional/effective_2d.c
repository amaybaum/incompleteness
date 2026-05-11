/* effective_2d.c
 *
 * 2D version: d=2, allows larger L (up to L=5 fits in 50 bits, L=7 fits in 98 -> need 2 uint64).
 *
 * Caveat: 2D is not the framework's substratum (which is d=3), so this is a
 * methodological test of whether the cycle-averaged trace-out gives non-trivial
 * scaling, not a direct framework-claim test. If the 2D scaling is integer,
 * that's consistent with the basic substratum hypothesis being wrong for
 * fractional powers. If 2D scaling is fractional, that motivates extending to 3D.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

typedef uint64_t state_t;

static int Lc = 4;
static int Tc = 1;
static int N_h_samples = 200;
static int N_v_samples = 200;

/* d=2: site (x, y) with index i = x + L*y */
static inline int site_idx_2d(int x, int y, int L) {
    x = ((x % L) + L) % L;
    y = ((y % L) + L) % L;
    return x + L*y;
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

/* 2D wave step: 4 nearest neighbors */
static state_t wave_step_2d(state_t s, int L) {
    state_t s_new = 0;
    for (int y = 0; y < L; y++) {
        for (int x = 0; x < L; x++) {
            int i = site_idx_2d(x, y, L);
            int f_prev = get_f_prev(s, i);
            int sum = 0;
            sum += get_f_now(s, site_idx_2d(x+1, y, L));
            sum += get_f_now(s, site_idx_2d(x-1, y, L));
            sum += get_f_now(s, site_idx_2d(x, y+1, L));
            sum += get_f_now(s, site_idx_2d(x, y-1, L));
            int f_next = ((sum - f_prev) % 2 + 2) % 2;
            int f_now = get_f_now(s, i);
            s_new = set_f_now(s_new, i, f_next);
            s_new = set_f_prev(s_new, i, f_now);
        }
    }
    return s_new;
}

static uint64_t rng = 67890;
static uint64_t rng_next(void) {
    rng = rng * 6364136223846793005ULL + 1442695040888963407ULL;
    return rng;
}

static inline int spin(int f) { return 2*f - 1; }

#define MAX_S 200
static int v_sites[MAX_S], h_sites[MAX_S];
static int n_v, n_h;

static void compute_partition_2d(int L) {
    n_v = 0; n_h = 0;
    for (int y = 0; y < L; y++) {
        for (int x = 0; x < L; x++) {
            int i = site_idx_2d(x, y, L);
            if (x == 0) v_sites[n_v++] = i;
            else        h_sites[n_h++] = i;
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

static double op_cycle_avg(state_t s_init, int L, long max_iter,
                            int site_a, int site_b) {
    state_t s = s_init;

    state_t t = s_init;
    state_t hare = wave_step_2d(s_init, L);
    long power = 1, lam = 1;
    while (t != hare && lam < max_iter) {
        if (power == lam) { t = hare; power *= 2; lam = 0; }
        hare = wave_step_2d(hare, L);
        lam++;
    }
    if (lam >= max_iter) return 0;
    long orbit_len = lam;

    double sum = 0;
    for (long k = 0; k < orbit_len; k++) {
        sum += spin(get_f_now(s, site_a)) * spin(get_f_now(s, site_b));
        s = wave_step_2d(s, L);
    }
    return sum / orbit_len;
}

int main(int argc, char *argv[]) {
    if (argc > 1) Lc = atoi(argv[1]);
    if (argc > 2) N_h_samples = atoi(argv[2]);
    if (argc > 3) N_v_samples = atoi(argv[3]);

    int n_sites_total = Lc * Lc;
    int n_bits = 2 * n_sites_total;
    if (n_bits > 64) {
        printf("L=%d in 2D requires %d bits > 64; not implementable here\n", Lc, n_bits);
        return 1;
    }

    compute_partition_2d(Lc);

    /* Pick 2 visible sites for the 2-point operator: first and last visible */
    int a = v_sites[0];
    int b = v_sites[n_v - 1];

    printf("====================\n");
    printf("2D L=%d, %d v sites, %d h sites, sites a=%d b=%d\n",
           Lc, n_v, n_h, a, b);
    printf("====================\n");

    double sum_O = 0, sum_O_sq = 0, sum_O_ab = 0;

    clock_t t_start = clock();

    for (int kv = 0; kv < N_v_samples; kv++) {
        uint64_t v = rng_next() & ((1ULL << (2*n_v)) - 1);
        int fa = (v >> 0) & 1;
        int fb = (v >> (2 * (n_v-1))) & 1;

        double O_avg = 0;
        int n_valid = 0;
        for (int kh = 0; kh < N_h_samples; kh++) {
            uint64_t h = rng_next();
            state_t s = combine_vh(v, h);
            double cyc = op_cycle_avg(s, Lc, 100000000, a, b);
            O_avg += cyc;
            n_valid++;
        }
        O_avg /= n_valid;

        sum_O += O_avg;
        sum_O_sq += O_avg * O_avg;
        sum_O_ab += O_avg * spin(fa) * spin(fb);
    }

    double c_0 = sum_O / N_v_samples;
    double c_ab = sum_O_ab / N_v_samples;
    double var_O = sum_O_sq / N_v_samples - c_0*c_0;

    clock_t t_end = clock();

    printf("  c_0   = %10.6f\n", c_0);
    printf("  c_ab  = %10.6f\n", c_ab);
    printf("  var(O) = %10.6f\n", var_O);
    printf("  elapsed: %.3f s\n", (double)(t_end-t_start)/CLOCKS_PER_SEC);

    return 0;
}
