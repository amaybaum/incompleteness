/*
 * kite_T1a_chunked.c — Chunked version of T1a kite for large-N batch.
 *
 * Same as kite_T1a.c but takes (chunk_idx, num_chunks) and only
 * processes the k_2 indices assigned to this chunk. Outputs the
 * partial Σ^{μν} for this chunk; final result is the sum of all
 * chunks' outputs (then divided by N⁴² and multiplied by 1/2 sym
 * — but those prefactors are NOT applied per chunk; they're done
 * at the final combination step in Python).
 *
 * To get the full Σ from chunks, run all chunks 0..(num_chunks-1)
 * with the same (N, m_reg, p0, num_chunks), sum their outputs,
 * then multiply by 0.5 / N^8.
 *
 * Usage:
 *   ./kite_T1a_chunked N m_reg p0 chunk_idx num_chunks [threads]
 *
 * Example for N=10 split into 4 chunks:
 *   ./kite_T1a_chunked 10 0.2 0.628 0 4   # chunks 0
 *   ./kite_T1a_chunked 10 0.2 0.628 1 4   # chunk 1
 *   ./kite_T1a_chunked 10 0.2 0.628 2 4   # chunk 2
 *   ./kite_T1a_chunked 10 0.2 0.628 3 4   # chunk 3
 * Sum the 4 outputs, multiply by 0.5 / N^8.
 *
 * Compile: gcc -O3 -fopenmp -ffast-math -march=native kite_T1a_chunked.c -o kite_T1a_chunked -lm
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
    double s0 = 2.0*sin(k0*0.5), s1 = 2.0*sin(k1*0.5);
    double s2 = 2.0*sin(k2*0.5), s3 = 2.0*sin(k3*0.5);
    return 1.0 / (s0*s0 + s1*s1 + s2*s2 + s3*s3 + m_sq);
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
    if (argc < 6) {
        fprintf(stderr, "Usage: %s N m_reg p0 chunk_idx num_chunks [threads]\n", argv[0]);
        return 1;
    }
    int N = atoi(argv[1]);
    double m_reg = atof(argv[2]);
    double p0 = atof(argv[3]);
    int chunk_idx = atoi(argv[4]);
    int num_chunks = atoi(argv[5]);
    if (argc >= 7) omp_set_num_threads(atoi(argv[6]));

    int Npts = N*N*N*N;
    double m_sq = m_reg * m_reg;
    double p_ext[4] = {p0, 0.0, 0.0, 0.0};
    double mp[4] = {-p0, 0.0, 0.0, 0.0};

    /* Determine k_2 index range for this chunk */
    int chunk_start = (chunk_idx * Npts) / num_chunks;
    int chunk_end = ((chunk_idx + 1) * Npts) / num_chunks;
    fprintf(stderr, "Chunk %d/%d: k_2 indices [%d, %d) of %d total\n",
            chunk_idx, num_chunks, chunk_start, chunk_end, Npts);

    /* Pre-compute k_1 grid, V_L, gluon props (k_2-independent) — once for all chunks
     * but cheap so OK to repeat per-chunk. */
    double *k1_grid = (double*)malloc(Npts * 4 * sizeof(double));
    double *V_L_all = (double*)malloc(Npts * 64 * sizeof(double));
    double *D_k1_all = (double*)malloc(Npts * sizeof(double));
    double *D_pmk1_all = (double*)malloc(Npts * sizeof(double));
    if (!k1_grid || !V_L_all || !D_k1_all || !D_pmk1_all) {
        fprintf(stderr, "OOM\n"); return 2;
    }

    for (int idx = 0; idx < Npts; idx++) {
        int i0 = idx/(N*N*N), i1 = (idx/(N*N))%N, i2 = (idx/N)%N, i3 = idx%N;
        double k1[4] = {mom_at(i0,N), mom_at(i1,N), mom_at(i2,N), mom_at(i3,N)};
        for (int m = 0; m < 4; m++) k1_grid[idx*4 + m] = k1[m];

        double mk1[4] = {-k1[0], -k1[1], -k1[2], -k1[3]};
        double k1mp[4] = {k1[0]-p0, k1[1], k1[2], k1[3]};
        build_V3g(p_ext, mk1, k1mp, &V_L_all[idx * 64]);

        D_k1_all[idx] = lat_prop(k1[0], k1[1], k1[2], k1[3], m_sq);
        double pmk1[4] = {p0-k1[0], -k1[1], -k1[2], -k1[3]};
        D_pmk1_all[idx] = lat_prop(pmk1[0], pmk1[1], pmk1[2], pmk1[3], m_sq);
    }

    double Sigma_total[16];
    for (int i = 0; i < 16; i++) Sigma_total[i] = 0.0;

    #pragma omp parallel
    {
        double Sigma_local[16];
        for (int i = 0; i < 16; i++) Sigma_local[i] = 0.0;

        #pragma omp for schedule(dynamic, 8)
        for (int k2_idx = chunk_start; k2_idx < chunk_end; k2_idx++) {
            int i0 = k2_idx/(N*N*N), i1 = (k2_idx/(N*N))%N, i2 = (k2_idx/N)%N, i3 = k2_idx%N;
            double k2[4] = {mom_at(i0,N), mom_at(i1,N), mom_at(i2,N), mom_at(i3,N)};
            double mk2[4] = {-k2[0], -k2[1], -k2[2], -k2[3]};
            double D_k2 = lat_prop(k2[0], k2[1], k2[2], k2[3], m_sq);

            double V_T[64], V_R[64], V_B[64];
            double VLVT[256], VRVB[256];

            for (int k1_idx = 0; k1_idx < Npts; k1_idx++) {
                const double *k1 = &k1_grid[k1_idx * 4];

                double k2mk1[4] = {k2[0]-k1[0], k2[1]-k1[1], k2[2]-k1[2], k2[3]-k1[3]};
                build_V3g(k1, k2mk1, mk2, V_T);

                double k1mk2[4] = {k1[0]-k2[0], k1[1]-k2[1], k1[2]-k2[2], k1[3]-k2[3]};
                double pmk1pk2[4] = {p0-k1[0]+k2[0], -k1[1]+k2[1], -k1[2]+k2[2], -k1[3]+k2[3]};
                build_V3g(mp, k1mk2, pmk1pk2, V_R);

                double pmk1[4] = {p0-k1[0], -k1[1], -k1[2], -k1[3]};
                double k1mk2mp[4] = {k1[0]-k2[0]-p0, k1[1]-k2[1], k1[2]-k2[2], k1[3]-k2[3]};
                build_V3g(pmk1, k1mk2mp, k2, V_B);

                double D_k1mk2 = lat_prop(k1mk2[0], k1mk2[1], k1mk2[2], k1mk2[3], m_sq);
                double D_pmk1pk2 = lat_prop(pmk1pk2[0], pmk1pk2[1], pmk1pk2[2], pmk1pk2[3], m_sq);
                double weight = D_k1_all[k1_idx] * D_k1mk2 * D_pmk1_all[k1_idx]
                              * D_pmk1pk2 * D_k2;

                const double *V_L = &V_L_all[k1_idx * 64];

                for (int i = 0; i < 256; i++) VLVT[i] = 0.0;
                for (int nu = 0; nu < 4; nu++)
                for (int al = 0; al < 4; al++)
                for (int be = 0; be < 4; be++) {
                    double v_L = V_L[nu*16 + al*4 + be];
                    if (v_L == 0.0) continue;
                    for (int ga = 0; ga < 4; ga++)
                    for (int ep = 0; ep < 4; ep++)
                        VLVT[nu*64 + be*16 + ga*4 + ep] += v_L * V_T[al*16 + ga*4 + ep];
                }

                for (int i = 0; i < 256; i++) VRVB[i] = 0.0;
                for (int mu = 0; mu < 4; mu++)
                for (int ga = 0; ga < 4; ga++)
                for (int de = 0; de < 4; de++) {
                    double v_R = V_R[mu*16 + ga*4 + de];
                    if (v_R == 0.0) continue;
                    for (int be = 0; be < 4; be++)
                    for (int ep = 0; ep < 4; ep++)
                        VRVB[mu*64 + ga*16 + be*4 + ep] += v_R * V_B[be*16 + de*4 + ep];
                }

                for (int mu = 0; mu < 4; mu++)
                for (int nu = 0; nu < 4; nu++) {
                    double sum = 0.0;
                    for (int be = 0; be < 4; be++)
                    for (int ga = 0; ga < 4; ga++)
                    for (int ep = 0; ep < 4; ep++)
                        sum += VLVT[nu*64 + be*16 + ga*4 + ep]
                             * VRVB[mu*64 + ga*16 + be*4 + ep];
                    Sigma_local[mu*4 + nu] += weight * sum;
                }
            }
        }

        #pragma omp critical
        for (int i = 0; i < 16; i++) Sigma_total[i] += Sigma_local[i];
    }

    /* Output PARTIAL Σ — no prefactors applied. Caller sums chunks then
     * multiplies by 0.5/N^8 to get final Σ. */
    for (int i = 0; i < 16; i++) printf("%.16e ", Sigma_total[i]);
    printf("\n");

    free(k1_grid); free(V_L_all); free(D_k1_all); free(D_pmk1_all);
    return 0;
}
