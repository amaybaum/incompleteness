/* exact_L2.c
 *
 * Phase 1 Deliverable 2: exact enumeration trace-out at L=2, q=2.
 *
 * Approach:
 *  1. Enumerate all 2^16 = 65536 states.
 *  2. Apply wave_step() T times to get phi^T(s) for each s.
 *  3. Verify structural features:
 *     - phi is a bijection (every state has exactly one preimage)
 *     - wave_step_inverse(wave_step(s)) == s for all s (involution check)
 *     - phi has finite cycle structure (every orbit is closed)
 *  4. Partition the lattice into visible V and hidden H:
 *     - Choice B: corner-block visible = sites with x=0 (4 sites out of 8)
 *  5. For each visible-sector observable O_V, compute:
 *     <O_V>(s_V) = (1/|H|) sum_{s_H} O_V(visible part of phi^t(s_V, s_H))
 *  6. Extract effective coupling for the four operators in the Phase 1 spec.
 *
 * This is the SMALLEST nontrivial test - validates the entire pipeline.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lattice.h"

extern state_t wave_step(state_t s);
extern state_t wave_step_inverse(state_t s);

/* Partition definition: Choice B (subset partition) for L=2.
 * Visible = sites with x=0: that's sites (0,0,0), (0,1,0), (0,0,1), (0,1,1)
 * = indices 0, 2, 4, 6 (since idx = x + L*y + L*L*z with L=2)
 * Hidden = sites with x=1: indices 1, 3, 5, 7
 */
static const int VISIBLE_SITES[] = {0, 2, 4, 6};
static const int HIDDEN_SITES[]  = {1, 3, 5, 7};
#define N_VISIBLE 4
#define N_HIDDEN  4
/* Visible state space: 2^(2*4) = 256 states */
/* Hidden state space: 2^(2*4) = 256 states */

/* Extract visible portion of state s (lower 8 bits in the right order) */
static uint32_t extract_visible(state_t s) {
    uint32_t v = 0;
    for (int j = 0; j < N_VISIBLE; j++) {
        int site = VISIBLE_SITES[j];
        int f_now = get_f_now(s, site);
        int f_prev = get_f_prev(s, site);
        v |= ((uint32_t)f_now) << (2*j);
        v |= ((uint32_t)f_prev) << (2*j + 1);
    }
    return v;
}

/* Extract hidden portion of state s */
static uint32_t extract_hidden(state_t s) {
    uint32_t h = 0;
    for (int j = 0; j < N_HIDDEN; j++) {
        int site = HIDDEN_SITES[j];
        int f_now = get_f_now(s, site);
        int f_prev = get_f_prev(s, site);
        h |= ((uint32_t)f_now) << (2*j);
        h |= ((uint32_t)f_prev) << (2*j + 1);
    }
    return h;
}

/* Reconstruct full state from visible and hidden portions */
static state_t combine_vh(uint32_t v, uint32_t h) {
    state_t s = 0;
    for (int j = 0; j < N_VISIBLE; j++) {
        int site = VISIBLE_SITES[j];
        int f_now = (v >> (2*j)) & 1;
        int f_prev = (v >> (2*j + 1)) & 1;
        s = set_f_now(s, site, f_now);
        s = set_f_prev(s, site, f_prev);
    }
    for (int j = 0; j < N_HIDDEN; j++) {
        int site = HIDDEN_SITES[j];
        int f_now = (h >> (2*j)) & 1;
        int f_prev = (h >> (2*j + 1)) & 1;
        s = set_f_now(s, site, f_now);
        s = set_f_prev(s, site, f_prev);
    }
    return s;
}

/* ============================================================
 * OPERATORS: each takes a state s and returns a real-valued observable.
 * For binary fields (q=2), we map {0,1} -> {-1,+1} to give meaningful
 * correlations (Ising-like). Operator values are signed integers.
 * ============================================================
 */

/* Ising mapping for f(x,t): 0 -> -1, 1 -> +1 */
static inline int spin(int f) { return 2*f - 1; }

/* O_2: bilinear (Higgs-mass-like), summed over visible sites
 *   O_2 = sum_{x in V} f(x,t) * f(x,t)
 * With Ising mapping, this is sum of spin^2 = sum of 1 = N_VISIBLE.
 * So we need a non-trivial bilinear. Use temporal correlator:
 *   O_2 = sum_{x in V} spin(f(x,t)) * spin(f(x,t-1))
 */
static int op_bilinear(state_t s) {
    int total = 0;
    for (int j = 0; j < N_VISIBLE; j++) {
        int site = VISIBLE_SITES[j];
        total += spin(get_f_now(s, site)) * spin(get_f_prev(s, site));
    }
    return total;
}

/* O_3: trilinear (Weinberg-like)
 *   O_3 = sum_{x in V} spin(f(x,t))^2 * spin(f(x+y_hat,t))
 *   With Ising spin^2 = 1, so this is sum of spin(f at neighbor).
 *   But spin(f)^3 = spin(f) for Ising. So we need three DIFFERENT factors.
 *   Use: spin(f(x,t)) * spin(f(x+y_hat,t)) * spin(f(x+z_hat,t))
 * (three-spin correlator on a y-z face of visible sub-lattice)
 */
static int op_trilinear(state_t s) {
    int total = 0;
    for (int j = 0; j < N_VISIBLE; j++) {
        int site = VISIBLE_SITES[j];
        /* Get coordinates of this visible site */
        int x = site % L;
        int y = (site / L) % L;
        int z = site / (L*L);
        /* Need neighbors at +y and +z (both visible if x=0 lattice was chosen) */
        int site_y = site_idx(x, y+1, z);
        int site_z = site_idx(x, y, z+1);
        /* Only include if both neighbors are in visible (x-coord = 0) */
        if (site_y % L == 0 && site_z % L == 0) {
            total += spin(get_f_now(s, site)) *
                     spin(get_f_now(s, site_y)) *
                     spin(get_f_now(s, site_z));
        }
    }
    return total;
}

/* O_4: quartic (four-fermion-like)
 *   O_4 = sum over plaquettes of four spins at corners of a y-z face
 * For L=2 with visible = x=0 plane (a 2x2 face), there's only 1 plaquette.
 */
static int op_quartic(state_t s) {
    int total = 0;
    /* Sum over plaquettes in the x=0 plane (which is a 2x2 grid in y,z) */
    /* There's only one such plaquette by PBC, but we'll enumerate all 4
     * starting positions (which by PBC will give the same plaquette 4 times) */
    int prod = 1;
    int s00 = site_idx(0, 0, 0);
    int s01 = site_idx(0, 1, 0);
    int s10 = site_idx(0, 0, 1);
    int s11 = site_idx(0, 1, 1);
    prod *= spin(get_f_now(s, s00));
    prod *= spin(get_f_now(s, s01));
    prod *= spin(get_f_now(s, s10));
    prod *= spin(get_f_now(s, s11));
    total = prod;
    return total;
}

/* O_K: kinetic (gauge-boson-mass-like)
 *   O_K = sum_{x in V} (spin(f(x+y_hat,t)) - spin(f(x,t)))^2
 *   For Ising spins (+/-1), the difference is 0, +/-2, so squared is 0 or 4.
 *   We normalize by the maximum (4 per pair) implicitly.
 */
static int op_kinetic(state_t s) {
    int total = 0;
    for (int j = 0; j < N_VISIBLE; j++) {
        int site = VISIBLE_SITES[j];
        int x = site % L;
        int y = (site / L) % L;
        int z = site / (L*L);
        int site_y = site_idx(x, y+1, z);
        /* Only include if neighbor is in visible */
        if (site_y % L == 0) {
            int d = spin(get_f_now(s, site)) - spin(get_f_now(s, site_y));
            total += d*d;
        }
    }
    return total;
}

/* ============================================================
 * STRUCTURAL VALIDATION
 * ============================================================
 */

static void validate_bijection() {
    /* Check phi is a bijection: every state maps to a unique state, and
     * the inverse map gives back the original */
    char *image_seen = (char*)calloc(N_STATES, 1);
    if (!image_seen) { fprintf(stderr, "OOM\n"); exit(1); }

    long collisions = 0;
    long inverse_errors = 0;

    for (state_t s = 0; s < N_STATES; s++) {
        state_t s_next = wave_step(s);
        if (image_seen[s_next]) collisions++;
        image_seen[s_next] = 1;

        /* Verify inverse: wave_step_inverse(wave_step(s)) == s */
        state_t s_recovered = wave_step_inverse(s_next);
        if (s_recovered != s) inverse_errors++;
    }

    long unreached = 0;
    for (state_t s = 0; s < N_STATES; s++) {
        if (!image_seen[s]) unreached++;
    }

    printf("=== Bijection validation ===\n");
    printf("  Total states:      %llu\n", (unsigned long long)N_STATES);
    printf("  Image collisions:  %ld\n", collisions);
    printf("  States unreached:  %ld\n", unreached);
    printf("  Inverse errors:    %ld\n", inverse_errors);
    if (collisions == 0 && unreached == 0 && inverse_errors == 0) {
        printf("  STATUS: phi is a valid bijection.\n");
    } else {
        printf("  STATUS: BIJECTION VIOLATION.\n");
    }
    printf("\n");

    free(image_seen);
}

static void enumerate_cycles() {
    /* Enumerate orbits of phi: cycles of various lengths */
    char *visited = (char*)calloc(N_STATES, 1);
    if (!visited) { fprintf(stderr, "OOM\n"); exit(1); }

    /* Histogram of cycle lengths */
    long cycle_length_hist[N_STATES + 1];
    memset(cycle_length_hist, 0, sizeof(cycle_length_hist));

    long n_cycles = 0;
    long max_cycle = 0;

    for (state_t s_start = 0; s_start < N_STATES; s_start++) {
        if (visited[s_start]) continue;
        /* Trace the orbit of s_start */
        long cycle_len = 0;
        state_t s = s_start;
        do {
            visited[s] = 1;
            s = wave_step(s);
            cycle_len++;
        } while (s != s_start);

        cycle_length_hist[cycle_len]++;
        n_cycles++;
        if (cycle_len > max_cycle) max_cycle = cycle_len;
    }

    printf("=== Cycle structure of phi ===\n");
    printf("  Number of distinct cycles: %ld\n", n_cycles);
    printf("  Longest cycle: %ld\n", max_cycle);
    printf("  Cycle length histogram (length: count):\n");
    for (long k = 1; k <= max_cycle; k++) {
        if (cycle_length_hist[k] > 0) {
            printf("    %6ld: %6ld\n", k, cycle_length_hist[k]);
        }
    }
    printf("\n");

    free(visited);
}

/* ============================================================
 * TRACE-OUT: compute <O_V>(s_V) by averaging over hidden states
 * ============================================================
 */

static void compute_traceout(int T_max) {
    /* For each visible state v, average <O_D> over all hidden states h
     * at the chosen number of timesteps T.
     *
     * Output: variance of <O_D>_V across visible states (a measure of
     * effective coupling magnitude) and time-dependence.
     */

    long N_V = 1ULL << (2 * N_VISIBLE);  /* 256 */
    long N_H = 1ULL << (2 * N_HIDDEN);   /* 256 */

    printf("=== Trace-out: |V|=%ld, |H|=%ld ===\n", N_V, N_H);
    printf("Visible state space: %ld\n", N_V);
    printf("Hidden state space:  %ld\n", N_H);

    /* For each operator, at each time T, compute:
     *  - <O_D>_V(v) = (1/N_H) sum_h O_D(phi^T(combine(v,h)))
     *  - variance over v of <O_D>_V
     *  - magnitude |<O_D>_V|^2 averaged over v
     */

    printf("\nOperator scaling vs time T:\n");
    printf("  T  |  Var<O_2>  |  Var<O_3>  |  Var<O_4>  |  Var<O_K>\n");
    printf(" ----+------------+------------+------------+----------\n");

    for (int T = 0; T <= T_max; T++) {
        /* Compute traced observable values */
        double *avg_O2 = (double*)calloc(N_V, sizeof(double));
        double *avg_O3 = (double*)calloc(N_V, sizeof(double));
        double *avg_O4 = (double*)calloc(N_V, sizeof(double));
        double *avg_OK = (double*)calloc(N_V, sizeof(double));

        for (uint32_t v = 0; v < (uint32_t)N_V; v++) {
            double sum_O2 = 0, sum_O3 = 0, sum_O4 = 0, sum_OK = 0;
            for (uint32_t h = 0; h < (uint32_t)N_H; h++) {
                state_t s = combine_vh(v, h);
                /* Apply phi T times */
                for (int t = 0; t < T; t++) s = wave_step(s);
                sum_O2 += op_bilinear(s);
                sum_O3 += op_trilinear(s);
                sum_O4 += op_quartic(s);
                sum_OK += op_kinetic(s);
            }
            avg_O2[v] = sum_O2 / N_H;
            avg_O3[v] = sum_O3 / N_H;
            avg_O4[v] = sum_O4 / N_H;
            avg_OK[v] = sum_OK / N_H;
        }

        /* Compute variance over visible states */
        double mean[4] = {0,0,0,0}, var[4] = {0,0,0,0};
        for (uint32_t v = 0; v < (uint32_t)N_V; v++) {
            mean[0] += avg_O2[v];
            mean[1] += avg_O3[v];
            mean[2] += avg_O4[v];
            mean[3] += avg_OK[v];
        }
        mean[0] /= N_V; mean[1] /= N_V; mean[2] /= N_V; mean[3] /= N_V;
        for (uint32_t v = 0; v < (uint32_t)N_V; v++) {
            var[0] += (avg_O2[v] - mean[0]) * (avg_O2[v] - mean[0]);
            var[1] += (avg_O3[v] - mean[1]) * (avg_O3[v] - mean[1]);
            var[2] += (avg_O4[v] - mean[2]) * (avg_O4[v] - mean[2]);
            var[3] += (avg_OK[v] - mean[3]) * (avg_OK[v] - mean[3]);
        }
        var[0] /= N_V; var[1] /= N_V; var[2] /= N_V; var[3] /= N_V;

        printf("  %2d | %10.6f | %10.6f | %10.6f | %10.6f\n",
               T, var[0], var[1], var[2], var[3]);

        free(avg_O2); free(avg_O3); free(avg_O4); free(avg_OK);
    }

    /* Interpretation note printed below the table */
    printf("\nInterpretation:\n");
    printf("  Var<O_D>_V measures effective-coupling magnitude in the traced theory.\n");
    printf("  Time-dependence reveals whether trace-out information persists or decays.\n");
    printf("  Decay law gives operator-dimension-dependent suppression alpha(D).\n");
}

int main(void) {
    printf("===========================================\n");
    printf("OI Trace-Out Fractional-Power Calculation\n");
    printf("Phase 1 Deliverable 2: L=2, q=2 exact\n");
    printf("===========================================\n\n");

    validate_bijection();
    enumerate_cycles();
    compute_traceout(8);  /* Time steps 0..8 */

    return 0;
}
