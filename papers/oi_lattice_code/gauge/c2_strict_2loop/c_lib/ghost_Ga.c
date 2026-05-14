/*
 * ghost_Ga.c — C+OpenMP G_a ghost-square topology
 *
 * Mirrors G_a_ghost_square.py exactly. 4 V_ghg + 1 gluon chord; 4 ghost lines.
 * Per-(k_1, k_2): scalar dot k̂_1·(k_1+k_2-p)̂ + outer product (k_1+k_2)̂^μ (k_1-p)̂^ν
 * → only ~16 mults per (k_1, k_2). Lightest of the brute-force topologies.
 *
 * Compile: gcc -O3 -fopenmp -ffast-math -march=native ghost_Ga.c -o ghost_Ga -lm
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

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "Usage: %s N m_reg p0 [threads]\n", argv[0]); return 1; }
    int N = atoi(argv[1]);
    double m_reg = atof(argv[2]);
    double p0 = atof(argv[3]);
    if (argc >= 5) omp_set_num_threads(atoi(argv[4]));

    int Npts = N*N*N*N;
    double m_sq = m_reg * m_reg;

    /* Pre-compute k_1-only quantities */
    double *k1_grid = (double*)malloc(Npts * 4 * sizeof(double));
    double *khat_k1 = (double*)malloc(Npts * 4 * sizeof(double));      /* k̂_1 */
    double *khat_k1mp = (double*)malloc(Npts * 4 * sizeof(double));    /* (k_1-p)̂ */
    double *weight_k1 = (double*)malloc(Npts * sizeof(double));        /* D_gh(k_1) D_gh(k_1-p) */
    if (!k1_grid || !khat_k1 || !khat_k1mp || !weight_k1) { fprintf(stderr, "OOM\n"); return 2; }

    for (int idx = 0; idx < Npts; idx++) {
        int i0 = idx/(N*N*N), i1 = (idx/(N*N))%N, i2 = (idx/N)%N, i3 = idx%N;
        double k1[4] = {mom_at(i0, N), mom_at(i1, N), mom_at(i2, N), mom_at(i3, N)};
        for (int m = 0; m < 4; m++) {
            k1_grid[idx*4 + m] = k1[m];
            khat_k1[idx*4 + m] = 2.0*sin(k1[m]*0.5);
        }
        double k1mp[4] = {k1[0]-p0, k1[1], k1[2], k1[3]};
        for (int m = 0; m < 4; m++) khat_k1mp[idx*4 + m] = 2.0*sin(k1mp[m]*0.5);

        double D_gh_k1 = lat_prop_ghost(k1[0], k1[1], k1[2], k1[3]);
        double D_gh_k1mp = lat_prop_ghost(k1mp[0], k1mp[1], k1mp[2], k1mp[3]);
        weight_k1[idx] = D_gh_k1 * D_gh_k1mp;
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
            double D_gluon_k2 = lat_prop_gluon(k2[0], k2[1], k2[2], k2[3], m_sq);

            for (int k1_idx = 0; k1_idx < Npts; k1_idx++) {
                const double *k1 = &k1_grid[k1_idx * 4];
                /* L1 = k_1+k_2; L4 = k_1+k_2-p */
                double k1pk2[4] = {k1[0]+k2[0], k1[1]+k2[1], k1[2]+k2[2], k1[3]+k2[3]};
                double k1pk2mp[4] = {k1pk2[0]-p0, k1pk2[1], k1pk2[2], k1pk2[3]};
                double khat_k1pk2[4] = {2.0*sin(k1pk2[0]*0.5), 2.0*sin(k1pk2[1]*0.5),
                                        2.0*sin(k1pk2[2]*0.5), 2.0*sin(k1pk2[3]*0.5)};
                double khat_k1pk2mp[4] = {2.0*sin(k1pk2mp[0]*0.5), 2.0*sin(k1pk2mp[1]*0.5),
                                          2.0*sin(k1pk2mp[2]*0.5), 2.0*sin(k1pk2mp[3]*0.5)};

                double D_gh_L1 = lat_prop_ghost(k1pk2[0], k1pk2[1], k1pk2[2], k1pk2[3]);
                double D_gh_L4 = lat_prop_ghost(k1pk2mp[0], k1pk2mp[1], k1pk2mp[2], k1pk2mp[3]);
                double weight = weight_k1[k1_idx] * D_gh_L1 * D_gh_L4 * D_gluon_k2;

                /* Scalar dot k̂_1 · (k_1+k_2-p)̂ */
                const double *kh_k1 = &khat_k1[k1_idx * 4];
                double k1_dot_L4 = kh_k1[0]*khat_k1pk2mp[0] + kh_k1[1]*khat_k1pk2mp[1]
                                 + kh_k1[2]*khat_k1pk2mp[2] + kh_k1[3]*khat_k1pk2mp[3];

                /* Σ[μ, ν] += weight · k1_dot_L4 · (k_1+k_2)̂^μ · (k_1-p)̂^ν */
                const double *kh_k1mp = &khat_k1mp[k1_idx * 4];
                double pre = weight * k1_dot_L4;
                for (int mu = 0; mu < 4; mu++)
                for (int nu = 0; nu < 4; nu++) {
                    Sigma_local[mu*4 + nu] += pre * khat_k1pk2[mu] * kh_k1mp[nu];
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

    free(k1_grid); free(khat_k1); free(khat_k1mp); free(weight_k1);
    return 0;
}
