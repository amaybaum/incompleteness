/* cycle_lengths.c - measure cycle lengths */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

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

static uint64_t rng = 12345;
static uint64_t rng_next(void) {
    rng = rng * 6364136223846793005ULL + 1442695040888963407ULL;
    return rng;
}

static long find_cycle(state_t start, int L, long max_iter) {
    state_t t = start;
    state_t h = wave_step(start, L);
    long power = 1, lam = 1;
    while (t != h && lam < max_iter) {
        if (power == lam) { t = h; power *= 2; lam = 0; }
        h = wave_step(h, L);
        lam++;
    }
    return (lam >= max_iter) ? -1 : lam;
}

int main(int argc, char *argv[]) {
    int L = (argc > 1) ? atoi(argv[1]) : 3;
    int n_samp = (argc > 2) ? atoi(argv[2]) : 100;
    long max_iter = (argc > 3) ? atol(argv[3]) : 10000000;

    int n_bits = 2 * L * L * L;
    if (n_bits > 64) { printf("Too big\n"); return 1; }
    uint64_t mask = (n_bits >= 64) ? (uint64_t)-1 : ((uint64_t)1 << n_bits) - 1;

    printf("L=%d, %d samples, max_iter=%ld\n", L, n_samp, max_iter);

    long min_cyc = max_iter, max_cyc = 0;
    long n_found = 0, n_timeout = 0;
    long total = 0;

    for (int k = 0; k < n_samp; k++) {
        state_t s = rng_next() & mask;
        long len = find_cycle(s, L, max_iter);
        if (len < 0) { n_timeout++; continue; }
        n_found++;
        total += len;
        if (len < min_cyc) min_cyc = len;
        if (len > max_cyc) max_cyc = len;
    }

    if (n_found > 0)
        printf("  cycle lengths: min=%ld, max=%ld, mean=%.1f\n",
               min_cyc, max_cyc, (double)total/n_found);
    printf("  timed out: %ld / %d\n", n_timeout, n_samp);

    return 0;
}
