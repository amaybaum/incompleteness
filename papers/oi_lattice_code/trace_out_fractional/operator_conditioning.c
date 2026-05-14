/* operator_conditioning.c
 *
 * REVISED Phase 1 Deliverable 2b: Static operator-conditioning calculation.
 *
 * After the initial calculation revealed that the wave equation is linear
 * mod 2 (cycle structure is trivially short, time-evolution of uniform
 * random states is exactly invariant), it became clear that the original
 * trace-out test was measuring the wrong thing.
 *
 * The trace-out fractional-power hypothesis is about operator-dimension
 * scaling, not time-evolution dynamics. The right test:
 *
 *   For each operator O_D of mass dimension D:
 *     Compute the joint distribution P(O_D(v) | partition):
 *     - At fixed v, how many h are there such that the full system has
 *       a given value of O_D evaluated on the visible part?
 *     - How does the SIZE of this conditional class scale with L
 *       and with the operator dimension D?
 *
 * If the framework's partition produces fractional-power suppression,
 * the number of hidden states compatible with a fixed visible-operator
 * value should scale as L^{D-alpha(D)} or similar, with alpha(D) being
 * the suppression exponent.
 *
 * For L=2 q=2: we can do this EXACTLY by enumerating all 2^16 states
 * and tabulating the joint distribution of visible-sector operator values.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lattice.h"

extern state_t wave_step(state_t s);

static inline int spin(int f) { return 2*f - 1; }

/* Same operators as exact_L2, on visible sites = x=0 sites */
static const int VISIBLE_SITES[] = {0, 2, 4, 6};
#define N_VISIBLE 4

static int op_bilinear(state_t s) {
    int total = 0;
    for (int j = 0; j < N_VISIBLE; j++) {
        int site = VISIBLE_SITES[j];
        total += spin(get_f_now(s, site)) * spin(get_f_prev(s, site));
    }
    return total;
}

static int op_trilinear(state_t s) {
    int total = 0;
    for (int j = 0; j < N_VISIBLE; j++) {
        int site = VISIBLE_SITES[j];
        int x = site % L;
        int y = (site / L) % L;
        int z = site / (L*L);
        int site_y = site_idx(x, y+1, z);
        int site_z = site_idx(x, y, z+1);
        if (site_y % L == 0 && site_z % L == 0) {
            total += spin(get_f_now(s, site)) *
                     spin(get_f_now(s, site_y)) *
                     spin(get_f_now(s, site_z));
        }
    }
    return total;
}

static int op_quartic(state_t s) {
    int s00 = site_idx(0, 0, 0);
    int s01 = site_idx(0, 1, 0);
    int s10 = site_idx(0, 0, 1);
    int s11 = site_idx(0, 1, 1);
    return spin(get_f_now(s, s00)) *
           spin(get_f_now(s, s01)) *
           spin(get_f_now(s, s10)) *
           spin(get_f_now(s, s11));
}

static int op_kinetic(state_t s) {
    int total = 0;
    for (int j = 0; j < N_VISIBLE; j++) {
        int site = VISIBLE_SITES[j];
        int x = site % L;
        int y = (site / L) % L;
        int z = site / (L*L);
        int site_y = site_idx(x, y+1, z);
        if (site_y % L == 0) {
            int d = spin(get_f_now(s, site)) - spin(get_f_now(s, site_y));
            total += d*d;
        }
    }
    return total;
}

int main(void) {
    printf("===========================================\n");
    printf("Static Operator Conditioning Analysis\n");
    printf("L = 2, Q = 2, exact enumeration\n");
    printf("===========================================\n\n");

    /* For each operator, build the histogram of values over all 2^16 states.
     * The width of the histogram and its log-relative entropy reveal whether
     * the operator's distribution is concentrated or spread.
     */

    /* Tabulate distributions */
    int hist_O2[9] = {0};   /* O_2 in [-4, 4] -> bins 0..8 */
    int hist_O3[9] = {0};   /* O_3 in [-4, 4] -> bins 0..8 */
    int hist_O4[3] = {0};   /* O_4 in {-1, 0, 1} -> mapped */
    int hist_OK[5] = {0};   /* O_K in {0, 4, 8, 12, 16} */

    int min_O2 = 1000, max_O2 = -1000;
    int min_O3 = 1000, max_O3 = -1000;
    int min_O4 = 1000, max_O4 = -1000;
    int min_OK = 1000, max_OK = -1000;

    for (state_t s = 0; s < N_STATES; s++) {
        int o2 = op_bilinear(s);
        int o3 = op_trilinear(s);
        int o4 = op_quartic(s);
        int ok = op_kinetic(s);

        if (o2 < min_O2) min_O2 = o2;
        if (o2 > max_O2) max_O2 = o2;
        if (o3 < min_O3) min_O3 = o3;
        if (o3 > max_O3) max_O3 = o3;
        if (o4 < min_O4) min_O4 = o4;
        if (o4 > max_O4) max_O4 = o4;
        if (ok < min_OK) min_OK = ok;
        if (ok > max_OK) max_OK = ok;
    }

    printf("=== Operator value ranges ===\n");
    printf("  O_2 (bilinear, D=4):  [%d, %d]\n", min_O2, max_O2);
    printf("  O_3 (trilinear, D=5): [%d, %d]\n", min_O3, max_O3);
    printf("  O_4 (quartic, D=6):   [%d, %d]\n", min_O4, max_O4);
    printf("  O_K (kinetic, D=4):   [%d, %d]\n", min_OK, max_OK);
    printf("\n");

    /* Now the key calculation: for each operator value, count the number
     * of full states (combinations of visible v and hidden h) that produce
     * that value. The variance / spread of these counts measures the
     * effective coupling of the operator after trace-out.
     */

    /* Joint distribution: P(O_D, partition_structure)
     * For each visible state v, what's the distribution of operator values
     * across all 256 hidden states h?
     */

    long N_V = 256, N_H = 256;

    /* For each visible state v, compute the variance of O_D over hidden states */
    double total_intra_var_O2 = 0, total_intra_var_O3 = 0;
    double total_intra_var_O4 = 0, total_intra_var_OK = 0;
    double total_mean_O2 = 0, total_mean_O3 = 0, total_mean_O4 = 0, total_mean_OK = 0;

    /* Also: variance of means across visible states */
    double *means_O2 = (double*)calloc(N_V, sizeof(double));
    double *means_O3 = (double*)calloc(N_V, sizeof(double));
    double *means_O4 = (double*)calloc(N_V, sizeof(double));
    double *means_OK = (double*)calloc(N_V, sizeof(double));

    /* Need extract/combine helpers */
    /* Visible sites: 0, 2, 4, 6 */
    /* Hidden sites:  1, 3, 5, 7 */

    for (uint32_t v = 0; v < (uint32_t)N_V; v++) {
        double sum_O2 = 0, sum_O3 = 0, sum_O4 = 0, sum_OK = 0;
        double sum_O2_sq = 0, sum_O3_sq = 0, sum_O4_sq = 0, sum_OK_sq = 0;

        for (uint32_t h = 0; h < (uint32_t)N_H; h++) {
            /* Combine v and h into full state */
            state_t s = 0;
            /* visible site indices: 0, 2, 4, 6 */
            /* For each j, bits 2j and 2j+1 of v go to bits 2*site and 2*site+1 of s */
            int v_sites[] = {0, 2, 4, 6};
            int h_sites[] = {1, 3, 5, 7};
            for (int j = 0; j < 4; j++) {
                int site = v_sites[j];
                int fn = (v >> (2*j)) & 1;
                int fp = (v >> (2*j+1)) & 1;
                s = set_f_now(s, site, fn);
                s = set_f_prev(s, site, fp);
            }
            for (int j = 0; j < 4; j++) {
                int site = h_sites[j];
                int fn = (h >> (2*j)) & 1;
                int fp = (h >> (2*j+1)) & 1;
                s = set_f_now(s, site, fn);
                s = set_f_prev(s, site, fp);
            }

            double o2 = op_bilinear(s);
            double o3 = op_trilinear(s);
            double o4 = op_quartic(s);
            double ok = op_kinetic(s);

            sum_O2 += o2;  sum_O2_sq += o2*o2;
            sum_O3 += o3;  sum_O3_sq += o3*o3;
            sum_O4 += o4;  sum_O4_sq += o4*o4;
            sum_OK += ok;  sum_OK_sq += ok*ok;
        }

        means_O2[v] = sum_O2 / N_H;
        means_O3[v] = sum_O3 / N_H;
        means_O4[v] = sum_O4 / N_H;
        means_OK[v] = sum_OK / N_H;

        total_intra_var_O2 += sum_O2_sq / N_H - means_O2[v]*means_O2[v];
        total_intra_var_O3 += sum_O3_sq / N_H - means_O3[v]*means_O3[v];
        total_intra_var_O4 += sum_O4_sq / N_H - means_O4[v]*means_O4[v];
        total_intra_var_OK += sum_OK_sq / N_H - means_OK[v]*means_OK[v];

        total_mean_O2 += means_O2[v];
        total_mean_O3 += means_O3[v];
        total_mean_O4 += means_O4[v];
        total_mean_OK += means_OK[v];
    }

    /* Variance decomposition */
    total_intra_var_O2 /= N_V;
    total_intra_var_O3 /= N_V;
    total_intra_var_O4 /= N_V;
    total_intra_var_OK /= N_V;

    double mean_O2 = total_mean_O2 / N_V;
    double mean_O3 = total_mean_O3 / N_V;
    double mean_O4 = total_mean_O4 / N_V;
    double mean_OK = total_mean_OK / N_V;

    double inter_var_O2 = 0, inter_var_O3 = 0, inter_var_O4 = 0, inter_var_OK = 0;
    for (uint32_t v = 0; v < (uint32_t)N_V; v++) {
        inter_var_O2 += (means_O2[v] - mean_O2) * (means_O2[v] - mean_O2);
        inter_var_O3 += (means_O3[v] - mean_O3) * (means_O3[v] - mean_O3);
        inter_var_O4 += (means_O4[v] - mean_O4) * (means_O4[v] - mean_O4);
        inter_var_OK += (means_OK[v] - mean_OK) * (means_OK[v] - mean_OK);
    }
    inter_var_O2 /= N_V; inter_var_O3 /= N_V; inter_var_O4 /= N_V; inter_var_OK /= N_V;

    printf("=== Variance decomposition (T=0, no dynamics applied) ===\n");
    printf("  Operator | Mean    | Intra-var (E_v[Var_h])  | Inter-var (Var_v[E_h])\n");
    printf(" ----------+---------+-------------------------+-----------------------\n");
    printf("  O_2  D=4 | %7.4f | %22.6f  | %20.6f\n", mean_O2, total_intra_var_O2, inter_var_O2);
    printf("  O_3  D=5 | %7.4f | %22.6f  | %20.6f\n", mean_O3, total_intra_var_O3, inter_var_O3);
    printf("  O_4  D=6 | %7.4f | %22.6f  | %20.6f\n", mean_O4, total_intra_var_O4, inter_var_O4);
    printf("  O_K  D=4 | %7.4f | %22.6f  | %20.6f\n", mean_OK, total_intra_var_OK, inter_var_OK);
    printf("\n");

    printf("=== Interpretation ===\n");
    printf("  Intra-variance E_v[Var_h]: how much O fluctuates within hidden\n");
    printf("    (information that the trace-out destroys -- this IS the suppression).\n");
    printf("  Inter-variance Var_v[E_h]: how much <O>_h depends on the visible v\n");
    printf("    (information the trace-out preserves -- effective coupling magnitude).\n");
    printf("\n");
    printf("  The ratio inter/total = inter / (intra + inter) measures the fraction\n");
    printf("  of operator-value information that survives the trace-out.\n");
    printf("\n");
    printf("  This ratio, computed across operators of different dimensions,\n");
    printf("  is what we want to track in scaling with L to detect fractional-power\n");
    printf("  suppression. With T=0 (no dynamics), the partition geometry alone\n");
    printf("  determines the ratio. With T>0, dynamics mixes hidden into visible.\n");

    free(means_O2); free(means_O3); free(means_O4); free(means_OK);
    return 0;
}
