/*
 * ghost_Gc.c — C+OpenMP G_c ghost triangle topology
 *
 * Mirrors G_c_ghost_triangle.py exactly. 1 V_3g + 3 V_ghg, 3 ghost lines triangle.
 * Vertex routing per the existing G_c file (which had earlier convention with
 * V_3g(p, -k_1, k_1-p), giving +0.5·C_A² color).
 *
 * Pre-compute V_3g (k_1-only).
 *
 * Lorentz numerator:
 *   N^{μν} = V_3g[μ,α,β] · (k_1+k_2)̂^α · (p+k_2)̂^β · k̂_2^ν
 *
 * Per (k_1, k_2): contract V_3g over (α, β) for each μ → 16 mults per μ, then
 * outer with k̂_2^ν → 16 mults. ~80 mults total, plus prop work.
 *
 * Compile: gcc -O3 -fopenmp -ffast-math -march=native ghost_Gc.c -o ghost_Gc -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

#define M_PI_VAL 3.14159265358979323846
#define EPS_GHOST 1e-12

static inline double mom_at(int i, int N) {
    int j = (i > N/2) ? i - N : i;
    return (double)j * 2.0 * M_PI_VAL / (double)N;
}

static inline double khat2_sum(double k0, double k1, double k2, double k3) {
    double s0 = 2.0*sin(k0*0.5), s1 = 2.0*sin(k1*0.5);
    double s2 = 2.0*sin(k2*0.5), s3 = 2.0*sin(k3*0.5);
    return s0*s0 + s1*s1 + s2*s2 + s3*s3;
}

static inline double lat_prop_gluon(double k0, double k1, double k2, double k3, double m_sq) {
    return 1.0 / (khat2_sum(k0, k1, k2, k3) + m_sq);
}

static inline double lat_prop_ghost(double k0, double k1, double k2, double k3) {
    double s = khat2_sum(k0, k1, k2, k3);
    return (s > EPS_GHOST) ? 1.0/s : 0.0;
}

static void build_V3g(const double *p1, const double *p2, const double *p3, double *V) {
    double p1h[4], p2h[4], p3h[4], c1[4], c2[4], c3[4];
    for (int m = 0; m < 4; m++) {
        p1h[m] = 2.0*sin(p1[m]*0.5); c1[m] = cos(p1[m]*0.5);
        p2h[m] = 2.0*sin(p2[m]*0.5); c2[m] = cos(p2[m]*0.5);
        p3h[m] = 2.0*sin(p3[m]*0.5); c3[m] = cos(p3[m]*0.5);
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
    if (argc < 4) { fprintf(stderr, "Usage: %s N m_reg p0 [threads]\n", argv[0]); return 1; }
    int N = atoi(argv[1]);
    double m_reg = atof(argv[2]);
    double p0 = atof(argv[3]);
    if (argc >= 5) omp_set_num_threads(atoi(argv[4]));

    int Npts = N*N*N*N;
    double m_sq = m_reg * m_reg;
    double p_ext[4] = {p0, 0, 0, 0};

    /* Pre-compute V_3g(p, -k_1, k_1-p) — k_2-independent, V_3g_kin[k_1, μ, α, β] */
    double *k1_grid = (double*)malloc(Npts * 4 * sizeof(double));
    double *V3g_all = (double*)malloc(Npts * 64 * sizeof(double));
    double *weight_glue = (double*)malloc(Npts * sizeof(double));
    if (!k1_grid || !V3g_all || !weight_glue) { fprintf(stderr, "OOM\n"); return 2; }

    for (int idx = 0; idx < Npts; idx++) {
        int i0 = idx/(N*N*N), i1 = (idx/(N*N))%N, i2 = (idx/N)%N, i3 = idx%N;
        double k1[4] = {mom_at(i0, N), mom_at(i1, N), mom_at(i2, N), mom_at(i3, N)};
        for (int m = 0; m < 4; m++) k1_grid[idx*4 + m] = k1[m];

        double mk1[4] = {-k1[0], -k1[1], -k1[2], -k1[3]};
        double k1mp[4] = {k1[0]-p0, k1[1], k1[2], k1[3]};
        build_V3g(p_ext, mk1, k1mp, &V3g_all[idx * 64]);

        double pmk1[4] = {p0-k1[0], -k1[1], -k1[2], -k1[3]};
        double D_LA = lat_prop_gluon(k1[0], k1[1], k1[2], k1[3], m_sq);
        double D_LB = lat_prop_gluon(pmk1[0], pmk1[1], pmk1[2], pmk1[3], m_sq);
        weight_glue[idx] = D_LA * D_LB;
    }

    double Sigma_total[16];
    for (int i = 0; i < 16; i++) Sigma_total[i] = 0.0;

    #pragma omp parallel
    {
        double Sigma_local[16];
        for (int i = 0; i < 16; i++) Sigma_local[i] = 0.0;

        #pragma omp for schedule(dynamic, 8)
        for (int k2_idx = 0; k2_idx < Npts; k2_idx++) {
            int i0 = k2_idx/(N*N*N), i1 = (k2_idx/(N*N))%N, i2 = (k2_idx/N)%N, i3 = k2_idx%N;
            double k2[4] = {mom_at(i0, N), mom_at(i1, N), mom_at(i2, N), mom_at(i3, N)};
            double khat_k2[4] = {2.0*sin(k2[0]*0.5), 2.0*sin(k2[1]*0.5),
                                 2.0*sin(k2[2]*0.5), 2.0*sin(k2[3]*0.5)};
            double pk2[4] = {p0+k2[0], k2[1], k2[2], k2[3]};
            double khat_pk2[4] = {2.0*sin(pk2[0]*0.5), 2.0*sin(pk2[1]*0.5),
                                  2.0*sin(pk2[2]*0.5), 2.0*sin(pk2[3]*0.5)};
            double D_gh_pk2 = lat_prop_ghost(pk2[0], pk2[1], pk2[2], pk2[3]);
            double D_gh_k2 = lat_prop_ghost(k2[0], k2[1], k2[2], k2[3]);
            double k2_factor = D_gh_pk2 * D_gh_k2;

            for (int k1_idx = 0; k1_idx < Npts; k1_idx++) {
                const double *k1 = &k1_grid[k1_idx * 4];
                double k1pk2[4] = {k1[0]+k2[0], k1[1]+k2[1], k1[2]+k2[2], k1[3]+k2[3]};
                double khat_k1pk2[4] = {2.0*sin(k1pk2[0]*0.5), 2.0*sin(k1pk2[1]*0.5),
                                        2.0*sin(k1pk2[2]*0.5), 2.0*sin(k1pk2[3]*0.5)};
                double D_gh_k1pk2 = lat_prop_ghost(k1pk2[0], k1pk2[1], k1pk2[2], k1pk2[3]);
                double weight = weight_glue[k1_idx] * D_gh_k1pk2 * k2_factor;

                /* V3g_pap[μ] = Σ_α Σ_β V_3g[μ, α, β] · (k_1+k_2)̂^α · (p+k_2)̂^β */
                const double *V3g = &V3g_all[k1_idx * 64];
                double V3g_pap[4];
                for (int mu = 0; mu < 4; mu++) {
                    double sum = 0.0;
                    for (int al = 0; al < 4; al++)
                    for (int be = 0; be < 4; be++) {
                        sum += V3g[mu*16 + al*4 + be] * khat_k1pk2[al] * khat_pk2[be];
                    }
                    V3g_pap[mu] = sum;
                }

                /* Σ[μ, ν] += weight · V3g_pap[μ] · k̂_2^ν */
                for (int mu = 0; mu < 4; mu++)
                for (int nu = 0; nu < 4; nu++) {
                    Sigma_local[mu*4 + nu] += weight * V3g_pap[mu] * khat_k2[nu];
                }
            }
        }

        #pragma omp critical
        for (int i = 0; i < 16; i++) Sigma_total[i] += Sigma_local[i];
    }

    /* sym 1/2, ghost-loop -1, measure (1/N^4)^2 */
    double inv_vol = 1.0 / ((double)Npts);
    double prefac = 0.5 * (-1.0) * inv_vol * inv_vol;
    for (int i = 0; i < 16; i++) Sigma_total[i] *= prefac;

    for (int i = 0; i < 16; i++) printf("%.16e ", Sigma_total[i]);
    printf("\n");

    free(k1_grid); free(V3g_all); free(weight_glue);
    return 0;
}
