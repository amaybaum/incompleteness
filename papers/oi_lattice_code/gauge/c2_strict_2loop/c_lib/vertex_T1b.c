/*
 * vertex_T1b.c — C+OpenMP T1b vertex correction
 *
 * Mirrors T1b_vertex_correction.py exactly. Same V_3g_ym Wilson vertex,
 * same lattice prop, same momentum routing.
 *
 * Optimization: V_1, V_2 are k_2-independent. Pre-contract α between them
 * once outside outer loop:
 *   U[k_1, ν, μ, β, γ] = Σ_α V_1[ν, α, β] V_2[μ, α, γ]
 *
 * Then per (k_2, k_1):
 *   Build V_3, V_4 (each O(64))
 *   W[β, γ] = Σ_{δ, ε} V_3[β, δ, ε] V_4[γ, δ, ε]   (16 × 16 = 256 mults)
 *   Σ[μ, ν] += weight · Σ_{β, γ} U[ν, μ, β, γ] · W[β, γ]   (256 mults per μ,ν, total 16 × 256 = wait)
 *
 * Hmm let me redo: U has 4 free indices (ν, μ, β, γ); W has 2 (β, γ).
 * The dot is over (β, γ): 16 mults per (μ, ν), 16 (μ, ν) → 256 mults total.
 *
 * Per (k_1, k_2): ~256 (W) + 256 (final) ≈ 512 mults + 2 vertex builds.
 * Lighter than T1a (~3072 mults).
 *
 * Memory: U over all k_1 is N^4 × 4^4 = 256 N^4 doubles. At N=12: 5MB. Fine.
 *
 * Compile: gcc -O3 -fopenmp -ffast-math -march=native vertex_T1b.c -o vertex_T1b -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <omp.h>

#define M_PI_VAL 3.14159265358979323846

static inline double mom_at(int i, int N) {
    int j = (i > N/2) ? i - N : i;
    return (double)j * 2.0 * M_PI_VAL / (double)N;
}

static inline double lat_prop(double k0, double k1, double k2, double k3, double m_sq) {
    double s0 = 2.0 * sin(k0 * 0.5);
    double s1 = 2.0 * sin(k1 * 0.5);
    double s2 = 2.0 * sin(k2 * 0.5);
    double s3 = 2.0 * sin(k3 * 0.5);
    return 1.0 / (s0*s0 + s1*s1 + s2*s2 + s3*s3 + m_sq);
}

static void build_V3g(const double *p1, const double *p2, const double *p3, double *V) {
    double p1h[4], p2h[4], p3h[4], c1[4], c2[4], c3[4];
    for (int m = 0; m < 4; m++) {
        p1h[m] = 2.0 * sin(p1[m] * 0.5); c1[m] = cos(p1[m] * 0.5);
        p2h[m] = 2.0 * sin(p2[m] * 0.5); c2[m] = cos(p2[m] * 0.5);
        p3h[m] = 2.0 * sin(p3[m] * 0.5); c3[m] = cos(p3[m] * 0.5);
    }
    for (int i = 0; i < 64; i++) V[i] = 0.0;
    for (int m1 = 0; m1 < 4; m1++)
    for (int m2 = 0; m2 < 4; m2++)
    for (int m3 = 0; m3 < 4; m3++) {
        double val = 0.0;
        if (m1 == m2) val += c3[m1] * (p1h[m3] - p2h[m3]);
        if (m2 == m3) val += c1[m2] * (p2h[m1] - p3h[m1]);
        if (m3 == m1) val += c2[m3] * (p3h[m2] - p1h[m2]);
        V[m1*16 + m2*4 + m3] = val;
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

    /* k_2-independent precomputations */
    double *k1_grid = (double*)malloc(Npts * 4 * sizeof(double));
    double *U_all = (double*)malloc(Npts * 256 * sizeof(double));   /* U[k1, ν, μ, β, γ] */
    double *prop_k1 = (double*)malloc(Npts * sizeof(double));
    if (!k1_grid || !U_all || !prop_k1) {
        fprintf(stderr, "Out of memory\n"); return 2;
    }

    for (int idx = 0; idx < Npts; idx++) {
        int i0 = idx / (N*N*N);
        int i1 = (idx / (N*N)) % N;
        int i2 = (idx / N) % N;
        int i3 = idx % N;
        double k1[4] = {mom_at(i0, N), mom_at(i1, N), mom_at(i2, N), mom_at(i3, N)};
        for (int m = 0; m < 4; m++) k1_grid[idx*4 + m] = k1[m];

        double mk1[4] = {-k1[0], -k1[1], -k1[2], -k1[3]};
        double k1mp[4] = {k1[0]-p0, k1[1], k1[2], k1[3]};
        double pmk1[4] = {p0-k1[0], -k1[1], -k1[2], -k1[3]};

        /* V_1: V_3g(p, -k1, k1-p)  indices (ν, α, β) */
        double V_1[64], V_2[64];
        build_V3g(p_ext, mk1, k1mp, V_1);
        /* V_2: V_3g(-p, k1, p-k1)  indices (μ, α, γ) */
        build_V3g(mp, k1, pmk1, V_2);

        /* U[k1, ν, μ, β, γ] = Σ_α V_1[ν, α, β] V_2[μ, α, γ]
         * V_1[ν*16 + α*4 + β], V_2[μ*16 + α*4 + γ]
         * U[(idx*256) + ν*64 + μ*16 + β*4 + γ]
         */
        double *U_here = &U_all[idx * 256];
        for (int i = 0; i < 256; i++) U_here[i] = 0.0;
        for (int nu = 0; nu < 4; nu++)
        for (int mu = 0; mu < 4; mu++)
        for (int al = 0; al < 4; al++) {
            double v1 = V_1[nu*16 + al*4];   /* β=0 ... no, this varies. */
            (void)v1;
            for (int be = 0; be < 4; be++) {
                double v1_full = V_1[nu*16 + al*4 + be];
                if (v1_full == 0.0) continue;
                for (int ga = 0; ga < 4; ga++) {
                    U_here[nu*64 + mu*16 + be*4 + ga] += v1_full * V_2[mu*16 + al*4 + ga];
                }
            }
        }

        /* Propagator weight (k_2-independent): D(k1) · D(p-k1)² */
        double D_k1 = lat_prop(k1[0], k1[1], k1[2], k1[3], m_sq);
        double D_pmk1 = lat_prop(pmk1[0], pmk1[1], pmk1[2], pmk1[3], m_sq);
        prop_k1[idx] = D_k1 * D_pmk1 * D_pmk1;
    }

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
            double D_k2 = lat_prop(k2[0], k2[1], k2[2], k2[3], m_sq);

            double V_3[64], V_4[64], W[16];

            for (int k1_idx = 0; k1_idx < Npts; k1_idx++) {
                const double *k1 = &k1_grid[k1_idx * 4];

                /* V_3: V_3g(p-k1, -k2, k1+k2-p)  indices (β, δ, ε) */
                double pmk1[4] = {p0-k1[0], -k1[1], -k1[2], -k1[3]};
                double mk2[4] = {-k2[0], -k2[1], -k2[2], -k2[3]};
                double k1pk2mp[4] = {k1[0]+k2[0]-p0, k1[1]+k2[1], k1[2]+k2[2], k1[3]+k2[3]};
                build_V3g(pmk1, mk2, k1pk2mp, V_3);

                /* V_4: V_3g(k1-p, k2, p-k1-k2)  indices (γ, δ, ε) */
                double k1mp[4] = {k1[0]-p0, k1[1], k1[2], k1[3]};
                double pmk1mk2[4] = {p0-k1[0]-k2[0], -k1[1]-k2[1], -k1[2]-k2[2], -k1[3]-k2[3]};
                build_V3g(k1mp, k2, pmk1mk2, V_4);

                /* W[β, γ] = Σ_{δ, ε} V_3[β,δ,ε] V_4[γ,δ,ε]
                 * V_3[β*16 + δ*4 + ε], V_4[γ*16 + δ*4 + ε]
                 * W[β*4 + γ]
                 */
                for (int i = 0; i < 16; i++) W[i] = 0.0;
                for (int be = 0; be < 4; be++)
                for (int ga = 0; ga < 4; ga++) {
                    double sum = 0.0;
                    for (int de = 0; de < 4; de++)
                    for (int ep = 0; ep < 4; ep++) {
                        sum += V_3[be*16 + de*4 + ep] * V_4[ga*16 + de*4 + ep];
                    }
                    W[be*4 + ga] = sum;
                }

                /* propagator: prop_k1[k1_idx] · D(k2) · D(p-k1-k2) */
                double D_pmk1mk2 = lat_prop(pmk1mk2[0], pmk1mk2[1], pmk1mk2[2], pmk1mk2[3], m_sq);
                double weight = prop_k1[k1_idx] * D_k2 * D_pmk1mk2;

                /* Σ[μ,ν] += weight · Σ_{β,γ} U[ν,μ,β,γ] W[β,γ] */
                const double *U_here = &U_all[k1_idx * 256];
                for (int nu = 0; nu < 4; nu++)
                for (int mu = 0; mu < 4; mu++) {
                    double sum = 0.0;
                    for (int be = 0; be < 4; be++)
                    for (int ga = 0; ga < 4; ga++) {
                        sum += U_here[nu*64 + mu*16 + be*4 + ga] * W[be*4 + ga];
                    }
                    Sigma_local[mu*4 + nu] += weight * sum;
                }
            } /* k_1 */
        } /* k_2 */

        #pragma omp critical
        for (int i = 0; i < 16; i++) Sigma_total[i] += Sigma_local[i];
    }

    /* Sym 1/2, measure (1/N^4)^2 */
    double inv_vol = 1.0 / ((double)Npts);
    double prefac = 0.5 * inv_vol * inv_vol;
    for (int i = 0; i < 16; i++) Sigma_total[i] *= prefac;

    for (int i = 0; i < 16; i++) printf("%.16e ", Sigma_total[i]);
    printf("\n");

    free(k1_grid); free(U_all); free(prop_k1);
    return 0;
}
