/* 2D full enumeration */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

static int Lc;

static inline int sidx(int x, int y, int L) {
    return ((x%L+L)%L) + L * ((y%L+L)%L);
}
typedef uint64_t state_t;
static inline int get_now(state_t s, int i) { return (s >> (2*i)) & 1; }
static inline int get_prev(state_t s, int i) { return (s >> (2*i+1)) & 1; }

static state_t wave_step_2d(state_t s, int L) {
    state_t s_new = 0;
    for (int y = 0; y < L; y++) {
        for (int x = 0; x < L; x++) {
            int i = sidx(x, y, L);
            int sum = get_now(s, sidx(x+1,y,L)) + get_now(s, sidx(x-1,y,L))
                    + get_now(s, sidx(x,y+1,L)) + get_now(s, sidx(x,y-1,L));
            int next = (sum + get_prev(s, i)) & 1;
            int now = get_now(s, i);
            s_new |= ((state_t)next) << (2*i);
            s_new |= ((state_t)now) << (2*i + 1);
        }
    }
    return s_new;
}

static uint64_t gcd_u(uint64_t a, uint64_t b) {
    while (b) { uint64_t t = a%b; a = b; b = t; }
    return a;
}
static uint64_t lcm_u(uint64_t a, uint64_t b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_u(a, b)) * b;
}

int main(int argc, char *argv[]) {
    Lc = atoi(argv[1]);
    int L = Lc;
    int nbits = 2 * L * L;
    if (nbits > 30) {
        fprintf(stderr, "L=%d 2D requires %d bits; too big\n", L, nbits);
        return 1;
    }
    uint64_t N = 1ULL << nbits;
    printf("=== L=%d 2D, state space 2^%d=%llu ===\n", L, nbits, (unsigned long long)N);

    unsigned char *visited = calloc(N/8 + 1, 1);
    uint64_t *counts = calloc(N + 1, sizeof(uint64_t));
    if (!visited || !counts) { fprintf(stderr, "alloc fail\n"); return 1; }

    uint64_t order_W = 1, max_len = 0, total = 0, num = 0;
    clock_t t0 = clock();

    for (uint64_t s0 = 0; s0 < N; s0++) {
        if (visited[s0/8] & (1u << (s0%8))) continue;
        state_t s = s0;
        uint64_t len = 0;
        do {
            visited[s/8] |= (1u << (s%8));
            s = wave_step_2d(s, L);
            len++;
        } while (s != s0);
        counts[len]++;
        num++;
        total += len;
        if (len > max_len) max_len = len;
        order_W = lcm_u(order_W, len);
    }

    double el = (double)(clock()-t0)/CLOCKS_PER_SEC;
    printf("Enum done %.2fs, %llu cycles, max=%llu, total=%llu, order=%llu\n",
        el, (unsigned long long)num, (unsigned long long)max_len,
        (unsigned long long)total, (unsigned long long)order_W);

    /* Factor order */
    printf("Factorization of order(W) = %llu: ", (unsigned long long)order_W);
    uint64_t n = order_W; int first = 1;
    for (uint64_t p = 2; p*p <= n; p++) {
        int e = 0;
        while (n%p == 0) { n /= p; e++; }
        if (e > 0) {
            if (!first) printf(" * ");
            if (e == 1) printf("%llu", (unsigned long long)p);
            else printf("%llu^%d", (unsigned long long)p, e);
            first = 0;
        }
    }
    if (n > 1) { if (!first) printf(" * "); printf("%llu", (unsigned long long)n); }
    printf("\n");

    printf("Cycle lengths:\n");
    for (uint64_t c = 1; c <= max_len; c++) if (counts[c]) {
        printf("  len %llu: %llu cycles (%llu states)\n",
            (unsigned long long)c, (unsigned long long)counts[c],
            (unsigned long long)(c*counts[c]));
    }

    free(visited); free(counts);
    return 0;
}
