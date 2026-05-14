/* cycle_1d.c
 *
 * Phase 2 A1: 1D cycle-length enumeration for the OI substratum wave equation.
 *
 * For each L in {5, 7, 11, 13}: enumerate all 2^(2L) states, compute cycle
 * structure, find:
 *   (a) Cycle length spectrum (distinct cycle lengths and their multiplicities)
 *   (b) Order of W (LCM of cycle lengths)
 *   (c) Largest cycle, smallest cycle, mean cycle length
 *
 * Per PHASE_1_SPEC_cycle_number_theory.md, the 1D test is decisive for
 * H1 (cycle produces framework rationals) vs H3 (no connection).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

/* Wave equation step in 1D over F_2.
 * State is (f_now[x], f_prev[x]) for x = 0..L-1, packed as 2L bits:
 *   bit 2x   = f_now(x)
 *   bit 2x+1 = f_prev(x)
 *
 * Next step: f_next(x) = f(x+1) + f(x-1) + f_prev(x) mod 2
 * Then state becomes (f_next, f_now).
 */
typedef uint64_t state_t;

static int Lc = 5;

static inline int get_now(state_t s, int x) { return (s >> (2*x)) & 1; }
static inline int get_prev(state_t s, int x) { return (s >> (2*x + 1)) & 1; }

static state_t wave_step_1d(state_t s, int L) {
    state_t s_new = 0;
    for (int x = 0; x < L; x++) {
        int left  = get_now(s, (x - 1 + L) % L);
        int right = get_now(s, (x + 1) % L);
        int prev  = get_prev(s, x);
        int next  = (left + right + prev) & 1;
        int now   = get_now(s, x);
        s_new |= ((state_t)next) << (2*x);
        s_new |= ((state_t)now)  << (2*x + 1);
    }
    return s_new;
}

/* gcd for LCM */
static uint64_t gcd_u64(uint64_t a, uint64_t b) {
    while (b) { uint64_t t = a % b; a = b; b = t; }
    return a;
}
static uint64_t lcm_u64(uint64_t a, uint64_t b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_u64(a, b)) * b;
}

/* Cycle structure: enumerate all states, mark which are visited,
 * record cycle length for each unvisited state's orbit.
 */
int main(int argc, char *argv[]) {
    if (argc > 1) Lc = atoi(argv[1]);

    int L = Lc;
    int nbits = 2 * L;
    if (nbits > 30) {
        fprintf(stderr, "L=%d requires %d bits; too much memory for full enumeration\n", L, nbits);
        return 1;
    }
    uint64_t N = 1ULL << nbits;

    printf("=== L = %d (1D), state space = 2^%d = %llu ===\n", L, nbits, (unsigned long long)N);

    /* Bitmap to mark visited states */
    unsigned char *visited = calloc(N / 8 + 1, 1);
    if (!visited) { fprintf(stderr, "calloc failed\n"); return 1; }
    #define MARK(i)   (visited[(i)/8] |= (1u << ((i) % 8)))
    #define MARKED(i) (visited[(i)/8] & (1u << ((i) % 8)))

    /* Cycle length spectrum: counts[c] = number of cycles of length c */
    /* We don't know max cycle length a priori; use a map from length -> count */
    /* For L <= 13, length <= 2^26, use a flat array */
    uint64_t *counts = calloc(N + 1, sizeof(uint64_t));
    if (!counts) { fprintf(stderr, "calloc counts failed\n"); free(visited); return 1; }

    /* For each state, find its cycle */
    uint64_t order_W = 1;
    uint64_t max_len = 0, min_len = N;
    uint64_t total_states_on_cycles = 0;
    uint64_t num_cycles = 0;

    clock_t t_start = clock();

    for (uint64_t s0 = 0; s0 < N; s0++) {
        if (MARKED(s0)) continue;

        /* Trace orbit from s0 */
        state_t s = s0;
        uint64_t cycle_len = 0;
        do {
            MARK(s);
            s = wave_step_1d(s, L);
            cycle_len++;
        } while (s != s0);

        counts[cycle_len]++;
        num_cycles++;
        total_states_on_cycles += cycle_len;
        if (cycle_len > max_len) max_len = cycle_len;
        if (cycle_len < min_len) min_len = cycle_len;
        order_W = lcm_u64(order_W, cycle_len);
    }

    clock_t t_end = clock();
    double elapsed = (double)(t_end - t_start) / CLOCKS_PER_SEC;

    printf("Enumeration complete (%.2fs)\n", elapsed);
    printf("States enumerated: %llu (expected %llu)\n",
            (unsigned long long)total_states_on_cycles, (unsigned long long)N);
    printf("Number of distinct cycles: %llu\n", (unsigned long long)num_cycles);
    printf("Min cycle length: %llu\n", (unsigned long long)min_len);
    printf("Max cycle length: %llu\n", (unsigned long long)max_len);
    printf("Order of W (LCM of cycle lengths): %llu\n", (unsigned long long)order_W);
    printf("\n");

    /* Print cycle length spectrum */
    printf("Cycle length spectrum:\n");
    printf("  %-15s %-15s %-15s\n", "length", "num_cycles", "states");
    for (uint64_t c = 1; c <= max_len; c++) {
        if (counts[c] > 0) {
            printf("  %-15llu %-15llu %-15llu\n",
                   (unsigned long long)c,
                   (unsigned long long)counts[c],
                   (unsigned long long)(c * counts[c]));
        }
    }

    /* Factor the order_W */
    printf("\nFactorization of order(W) = %llu:\n  ", (unsigned long long)order_W);
    uint64_t n = order_W;
    int first = 1;
    for (uint64_t p = 2; p * p <= n; p++) {
        int e = 0;
        while (n % p == 0) { n /= p; e++; }
        if (e > 0) {
            if (!first) printf(" * ");
            if (e == 1) printf("%llu", (unsigned long long)p);
            else printf("%llu^%d", (unsigned long long)p, e);
            first = 0;
        }
    }
    if (n > 1) {
        if (!first) printf(" * ");
        printf("%llu", (unsigned long long)n);
    }
    printf("\n");

    /* Check framework-rational candidates */
    printf("\nFramework-rational candidates check:\n");
    int found_any = 0;
    /* Koide 2/9: look for length 9 with 2 cycles, or order divisible by 9 */
    if (order_W % 9 == 0) { printf("  order divisible by 9 (Koide 2/9 numerator candidate)\n"); found_any = 1; }
    if (counts[9] > 0) { printf("  cycles of length 9: %llu (Koide denominator)\n", (unsigned long long)counts[9]); found_any = 1; }
    /* Sum rule 7/6 */
    if (order_W % 7 == 0) { printf("  order divisible by 7\n"); found_any = 1; }
    if (order_W % 6 == 0) { printf("  order divisible by 6\n"); found_any = 1; }
    if (counts[7] > 0) { printf("  cycles of length 7: %llu\n", (unsigned long long)counts[7]); found_any = 1; }
    if (counts[6] > 0) { printf("  cycles of length 6: %llu\n", (unsigned long long)counts[6]); found_any = 1; }
    /* δ_0 = 10 */
    if (counts[10] > 0) { printf("  cycles of length 10: %llu\n", (unsigned long long)counts[10]); found_any = 1; }
    if (order_W % 10 == 0) { printf("  order divisible by 10\n"); found_any = 1; }
    /* A·B = 48 */
    if (counts[48] > 0) { printf("  cycles of length 48: %llu\n", (unsigned long long)counts[48]); found_any = 1; }
    if (order_W % 48 == 0) { printf("  order divisible by 48\n"); found_any = 1; }
    /* 1/alpha_0 = 23.25 = 93/4 */
    if (counts[93] > 0) { printf("  cycles of length 93: %llu\n", (unsigned long long)counts[93]); found_any = 1; }
    if (!found_any) printf("  (none of {6, 7, 9, 10, 48, 93} found in cycle structure)\n");

    printf("\n");

    free(visited);
    free(counts);
    return 0;
}
