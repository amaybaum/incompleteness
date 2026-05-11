#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint64_t state_t;

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
static uint64_t rng = 11; 
static uint64_t rng_next(void) {
    rng = rng * 6364136223846793005ULL + 1442695040888963407ULL;
    return rng;
}
static long find_cyc(state_t s, int L, long maxit) {
    state_t t = s, h = wave_step_2d(s, L);
    long power = 1, lam = 1;
    while (t != h && lam < maxit) {
        if (power == lam) { t = h; power *= 2; lam = 0; }
        h = wave_step_2d(h, L); lam++;
    }
    return (lam >= maxit) ? -1 : lam;
}
int main(int argc, char *argv[]) {
    int L = atoi(argv[1]);
    int n = atoi(argv[2]);
    int n_bits = 2*L*L;
    uint64_t mask = (n_bits >= 64) ? (uint64_t)-1 : ((1ULL << n_bits)-1);
    long total=0, mn=1L<<60, mx=0;
    int found=0;
    for (int k = 0; k < n; k++) {
        state_t s = rng_next() & mask;
        long c = find_cyc(s, L, 100000000);
        if (c < 0) continue;
        found++; total += c;
        if (c < mn) mn = c;
        if (c > mx) mx = c;
    }
    printf("L=%d 2D: %d/%d samples found, min=%ld max=%ld mean=%.1f\n",
        L, found, n, mn, mx, (double)total/found);
    return 0;
}
