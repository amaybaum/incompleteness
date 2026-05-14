/*
 * kite_T1a.c — C+OpenMP implementation of T1a kite topology
 *
 * Computes Σ^{μν}_T1a(p_ext) per C_A^2 for the standard-QCD pure-YM
 * 2-loop gluon self-energy.
 *
 * Mirrors the numpy implementation in T1a_kite.py exactly:
 *   - Wilson V_3g_ym vertex at all 4 vertices
 *   - Lattice prop 1/(k̂² + m²) with k̂_μ = 2 sin(k_μ/2)
 *   - Symmetry factor 1/2, color factor C_A^2 (extracted)
 *   - Outer loop over k_2 (parallelized via OpenMP), inner over k_1
 *
 * Lorentz contraction strategy:
 *   K^{μν} = Σ_{α,β,γ,δ,ε} V_L[ν,α,β] V_T[α,γ,ε] V_R[μ,γ,δ] V_B[β,δ,ε]
 * factored as:
 *   VLVT[ν,β,γ,ε] = Σ_α V_L[ν,α,β] V_T[α,γ,ε]                   (1024 mults)
 *   VRVB[μ,γ,β,ε] = Σ_δ V_R[μ,γ,δ] V_B[β,δ,ε]                   (1024 mults)
 *   K[μ,ν]       = Σ_{β,γ,ε} VLVT[ν,β,γ,ε] · VRVB[μ,γ,β,ε]      (1024 mults)
 *
 * Total: ~3K multiplies per (k_1, k_2). Plus 4 vertex builds and 5 prop evals.
 *
 * V_L is k_2-INDEPENDENT, so it's pre-computed for all k_1 once at startup.
 *
 * Usage:
 *   ./kite_T1a N m_reg p0 [num_threads]
 * Output: 16 doubles (row-major Σ^{μν}, μ outer, ν inner) on stdout.
 *
 * Compile: gcc -O3 -fopenmp -ffast-math -march=native kite_T1a.c -o kite_T1a -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <omp.h>

#define MAX_N 32
#define M_PI_VAL 3.14159265358979323846

/* Compute lattice momentum at index i, BZ-shifted to [-N/2, N/2). */
static inline double mom_at(int i, int N) {
    int j = (i > N/2) ? i - N : i;
    return (double)j * 2.0 * M_PI_VAL / (double)N;
}

/* Lattice prop 1/(k̂² + m²); k̂_μ = 2 sin(k_μ/2). */
static inline double lat_prop(double k0, double k1, double k2, double k3, double m_sq) {
    double s0 = 2.0 * sin(k0 * 0.5);
    double s1 = 2.0 * sin(k1 * 0.5);
    double s2 = 2.0 * sin(k2 * 0.5);
    double s3 = 2.0 * sin(k3 * 0.5);
    return 1.0 / (s0*s0 + s1*s1 + s2*s2 + s3*s3 + m_sq);
}

/* Wilson V_3g_ym vertex tensor V[mu1, mu2, mu3] given 3 all-outgoing momenta.
 *
 * V_3g[μ1,μ2,μ3] = δ^{μ1 μ2} cos(p3_{μ1}/2) (p1h - p2h)^{μ3}
 *                + δ^{μ2 μ3} cos(p1_{μ2}/2) (p2h - p3h)^{μ1}
 *                + δ^{μ3 μ1} cos(p2_{μ3}/2) (p3h - p1h)^{μ2}
 *
 * with p̂_μ = 2 sin(p_μ/2). Stored flat as V[m1*16 + m2*4 + m3].
 */
static void build_V3g(const double *p1, const double *p2, const double *p3, double *V) {
    double p1h[4], p2h[4], p3h[4], c1[4], c2[4], c3[4];
    for (int m = 0; m < 4; m++) {
        p1h[m] = 2.0 * sin(p1[m] * 0.5); c1[m] = cos(p1[m] * 0.5);
        p2h[m] = 2.0 * sin(p2[m] * 0.5); c2[m] = cos(p2[m] * 0.5);
        p3h[m] = 2.0 * sin(p3[m] * 0.5); c3[m] = cos(p3[m] * 0.5);
    }
    for (int i = 0; i < 64; i++) V[i] = 0.0;

    for (int m1 = 0; m1 < 4; m1++) {
        for (int m2 = 0; m2 < 4; m2++) {
            for (int m3 = 0; m3 < 4; m3++) {
                double val = 0.0;
                if (m1 == m2) val += c3[m1] * (p1h[m3] - p2h[m3]);
                if (m2 == m3) val += c1[m2] * (p2h[m1] - p3h[m1]);
                if (m3 == m1) val += c2[m3] * (p3h[m2] - p1h[m2]);
                V[m1*16 + m2*4 + m3] = val;
            }
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 4) {
        fprintf(stderr, "Usage: %s N m_reg p0 [num_threads]\n", argv[0]);
        return 1;
    }
    int N = atoi(argv[1]);
    double m_reg = atof(argv[2]);
    double p0 = atof(argv[3]);
    if (argc >= 5) omp_set_num_threads(atoi(argv[4]));

    int Npts = N*N*N*N;
    double m_sq = m_reg * m_reg;
    double p_ext[4] = {p0, 0.0, 0.0, 0.0};
    double mp[4] = {-p0, 0.0, 0.0, 0.0};

    /* Pre-compute k_1 momenta and V_L tensor for all k_1 (k_2-independent).
     * V_L = V_3g(p_ext, -k_1, k_1 - p_ext) [Lorentz indices ν, α, β]
     * Memory: N^4 * 64 doubles. At N=12: 20736 * 512B = 10MB. Fine.
     */
    double *k1_grid = (double*)malloc(Npts * 4 * sizeof(double));
    double *V_L_all = (double*)malloc(Npts * 64 * sizeof(double));
    double *D_k1_all = (double*)malloc(Npts * sizeof(double));
    double *D_pmk1_all = (double*)malloc(Npts * sizeof(double));
    if (!k1_grid || !V_L_all || !D_k1_all || !D_pmk1_all) {
        fprintf(stderr, "Out of memory\n"); return 2;
    }

    for (int idx = 0; idx < Npts; idx++) {
        int i0 = idx / (N*N*N);
        int i1 = (idx / (N*N)) % N;
        int i2 = (idx / N) % N;
        int i3 = idx % N;
        double k1_local[4] = {mom_at(i0, N), mom_at(i1, N), mom_at(i2, N), mom_at(i3, N)};
        for (int m = 0; m < 4; m++) k1_grid[idx*4 + m] = k1_local[m];

        double mk1[4] = {-k1_local[0], -k1_local[1], -k1_local[2], -k1_local[3]};
        double k1mp[4] = {k1_local[0] - p_ext[0], k1_local[1], k1_local[2], k1_local[3]};
        build_V3g(p_ext, mk1, k1mp, &V_L_all[idx * 64]);

        D_k1_all[idx] = lat_prop(k1_local[0], k1_local[1], k1_local[2], k1_local[3], m_sq);
        double pmk1[4] = {p_ext[0] - k1_local[0], -k1_local[1], -k1_local[2], -k1_local[3]};
        D_pmk1_all[idx] = lat_prop(pmk1[0], pmk1[1], pmk1[2], pmk1[3], m_sq);
    }

    /* Σ^{μν} accumulator */
    double Sigma_total[16];
    for (int i = 0; i < 16; i++) Sigma_total[i] = 0.0;

    #pragma omp parallel
    {
        double Sigma_local[16];
        for (int i = 0; i < 16; i++) Sigma_local[i] = 0.0;

        #pragma omp for schedule(dynamic, 8)
        for (int k2_idx = 0; k2_idx < Npts; k2_idx++) {
            int i0 = k2_idx / (N*N*N);
            int i1 = (k2_idx / (N*N)) % N;
            int i2 = (k2_idx / N) % N;
            int i3 = k2_idx % N;
            double k2[4] = {mom_at(i0, N), mom_at(i1, N), mom_at(i2, N), mom_at(i3, N)};
            double mk2[4] = {-k2[0], -k2[1], -k2[2], -k2[3]};
            double D_k2 = lat_prop(k2[0], k2[1], k2[2], k2[3], m_sq);

            double V_T[64], V_R[64], V_B[64];
            double VLVT[256];   /* [ν, β, γ, ε] flat ν*64 + β*16 + γ*4 + ε */
            double VRVB[256];   /* [μ, γ, β, ε] flat μ*64 + γ*16 + β*4 + ε */

            for (int k1_idx = 0; k1_idx < Npts; k1_idx++) {
                const double *k1 = &k1_grid[k1_idx * 4];

                /* V_T = V_3g(k1, k2-k1, -k2)   indices [α, γ, ε] */
                double k2mk1[4] = {k2[0]-k1[0], k2[1]-k1[1], k2[2]-k1[2], k2[3]-k1[3]};
                build_V3g(k1, k2mk1, mk2, V_T);

                /* V_R = V_3g(-p, k1-k2, p-k1+k2)   indices [μ, γ, δ] */
                double k1mk2[4] = {k1[0]-k2[0], k1[1]-k2[1], k1[2]-k2[2], k1[3]-k2[3]};
                double pmk1pk2[4] = {p_ext[0]-k1[0]+k2[0], -k1[1]+k2[1], -k1[2]+k2[2], -k1[3]+k2[3]};
                build_V3g(mp, k1mk2, pmk1pk2, V_R);

                /* V_B = V_3g(p-k1, k1-k2-p, k2)   indices [β, δ, ε] */
                double pmk1[4] = {p_ext[0]-k1[0], -k1[1], -k1[2], -k1[3]};
                double k1mk2mp[4] = {k1[0]-k2[0]-p_ext[0], k1[1]-k2[1], k1[2]-k2[2], k1[3]-k2[3]};
                build_V3g(pmk1, k1mk2mp, k2, V_B);

                /* Propagators */
                double D_k1mk2 = lat_prop(k1mk2[0], k1mk2[1], k1mk2[2], k1mk2[3], m_sq);
                double D_pmk1pk2 = lat_prop(pmk1pk2[0], pmk1pk2[1], pmk1pk2[2], pmk1pk2[3], m_sq);
                double weight = D_k1_all[k1_idx] * D_k1mk2 * D_pmk1_all[k1_idx]
                              * D_pmk1pk2 * D_k2;

                /* Get V_L[ν, α, β] for this k_1 */
                const double *V_L = &V_L_all[k1_idx * 64];

                /* VLVT[ν, β, γ, ε] = Σ_α V_L[ν,α,β] V_T[α,γ,ε]
                 * Layout: V_L[ν*16 + α*4 + β], V_T[α*16 + γ*4 + ε]
                 *         VLVT[ν*64 + β*16 + γ*4 + ε]
                 */
                for (int i = 0; i < 256; i++) VLVT[i] = 0.0;
                for (int nu = 0; nu < 4; nu++)
                for (int al = 0; al < 4; al++)
                for (int be = 0; be < 4; be++) {
                    double v_L = V_L[nu*16 + al*4 + be];
                    if (v_L == 0.0) continue;
                    for (int ga = 0; ga < 4; ga++)
                    for (int ep = 0; ep < 4; ep++) {
                        VLVT[nu*64 + be*16 + ga*4 + ep] += v_L * V_T[al*16 + ga*4 + ep];
                    }
                }

                /* VRVB[μ, γ, β, ε] = Σ_δ V_R[μ,γ,δ] V_B[β,δ,ε]
                 * Layout: V_R[μ*16 + γ*4 + δ], V_B[β*16 + δ*4 + ε]
                 *         VRVB[μ*64 + γ*16 + β*4 + ε]
                 */
                for (int i = 0; i < 256; i++) VRVB[i] = 0.0;
                for (int mu = 0; mu < 4; mu++)
                for (int ga = 0; ga < 4; ga++)
                for (int de = 0; de < 4; de++) {
                    double v_R = V_R[mu*16 + ga*4 + de];
                    if (v_R == 0.0) continue;
                    for (int be = 0; be < 4; be++)
                    for (int ep = 0; ep < 4; ep++) {
                        VRVB[mu*64 + ga*16 + be*4 + ep] += v_R * V_B[be*16 + de*4 + ep];
                    }
                }

                /* K[μ, ν] = Σ_{β, γ, ε} VLVT[ν, β, γ, ε] · VRVB[μ, γ, β, ε]
                 * Note the β/γ swap between the two!
                 */
                for (int mu = 0; mu < 4; mu++) {
                    for (int nu = 0; nu < 4; nu++) {
                        double sum = 0.0;
                        for (int be = 0; be < 4; be++)
                        for (int ga = 0; ga < 4; ga++)
                        for (int ep = 0; ep < 4; ep++) {
                            sum += VLVT[nu*64 + be*16 + ga*4 + ep]
                                 * VRVB[mu*64 + ga*16 + be*4 + ep];
                        }
                        Sigma_local[mu*4 + nu] += weight * sum;
                    }
                }
            } /* k1 */
        } /* k2 (parallel for) */

        #pragma omp critical
        for (int i = 0; i < 16; i++) Sigma_total[i] += Sigma_local[i];
    }

    /* Apply 1/2 sym factor and (1/N^4)^2 measure */
    double inv_vol = 1.0 / ((double)Npts);
    double prefac = 0.5 * inv_vol * inv_vol;
    for (int i = 0; i < 16; i++) Sigma_total[i] *= prefac;

    /* Output: 16 doubles, row-major Σ[μ][ν] (matches kite_sigma return) */
    for (int i = 0; i < 16; i++) {
        printf("%.16e ", Sigma_total[i]);
    }
    printf("\n");

    free(k1_grid); free(V_L_all); free(D_k1_all); free(D_pmk1_all);
    return 0;
}
