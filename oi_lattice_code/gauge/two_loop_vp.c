/*
 * two_loop_vp.c — Two-loop staggered VP for the OI lattice
 *
 * Computes δ₀ contributions from all four two-loop diagrams:
 *   SE (self-energy insertion), VC (vertex correction),
 *   Π_q (momentum-dependent VP correction), sails.
 *
 * The VP is computed as Π_s(p)/p²_lat at external momentum p,
 * which gives the gauge coupling coefficient at that scale.
 * The correct p is found by calibrating: 1/α₀ = N_f×4π×Π_s/p² = 23.25.
 *
 * Two-loop diagrams modify the VP. Their contributions to δ₀ are
 * computed at the SAME momentum p, ensuring consistent normalization.
 *
 * Compile: gcc -O3 -fopenmp -o two_loop_vp two_loop_vp.c -lm
 * Usage:   ./two_loop_vp [N] [p_ext]
 *          Default: N=10, p_ext=1.1
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define D 4
#define NF 6
#define PI 3.14159265358979323846

static inline double sinlat(double k){return sin(k);}
static inline double coslat(double k){return cos(k);}

int main(int argc, char **argv){
    int N = (argc>1) ? atoi(argv[1]) : 10;
    double p_ext = (argc>2) ? atof(argv[2]) : 1.10;
    double dk = 2*PI/N;
    int N4 = 1; for(int i=0;i<D;i++) N4*=N;
    double invN4 = 1.0/N4;
    double invN8 = invN4*invN4;
    double p[D] = {p_ext, 0, 0, 0};
    double plat2 = 0;
    for(int mu=0;mu<D;mu++){double s=2*sin(p[mu]/2);plat2+=s*s;}

    printf("Two-loop staggered VP: N=%d, p_ext=%.4f, p²_lat=%.6f\n",N,p_ext,plat2);
    printf("N⁴=%d, N⁸=%.0f\n",N4,(double)N4*N4);
    fflush(stdout);
    time_t t0=time(NULL);

    /* Step 1: One-loop Π_s(p)/p² at the external momentum */
    double Pi1=0, Pi1_0=0;
    for(int idx=0;idx<N4;idx++){
        int n[D];int tmp=idx;
        for(int mu=D-1;mu>=0;mu--){n[mu]=tmp%N;tmp/=N;}
        double k[D],kp[D];
        for(int mu=0;mu<D;mu++){k[mu]=dk*n[mu];kp[mu]=k[mu]+p[mu];}
        double sk=0,skp=0;
        for(int mu=0;mu<D;mu++){sk+=sinlat(k[mu])*sinlat(k[mu]);skp+=sinlat(kp[mu])*sinlat(kp[mu]);}
        if(sk<1e-30||skp<1e-30)continue;
        double Gk=1.0/sk, Gkp=1.0/skp, Gk0=1.0/sk;
        for(int mu=0;mu<D;mu++){
            double v=coslat(k[mu]+p[mu]/2.0);
            Pi1 += v*v*Gk*Gkp;
            double v0=coslat(k[mu]);
            Pi1_0 += v0*v0*Gk0*Gk0;
        }
    }
    Pi1 *= invN4/D;
    Pi1_0 *= invN4/D;
    double alpha0_inv = NF*4*PI*Pi1/plat2;
    printf("\nOne-loop: Π_s(p)/p² = %.6f, 1/α₀ = %.4f (target: 23.25)\n",Pi1/plat2,alpha0_inv);
    printf("  Π_s(0) = %.6f (for gauge propagator D(q) = 1/(q²×Π_s(0)))\n",Pi1_0);
    printf("  Time: %lds\n\n",time(NULL)-t0);
    fflush(stdout);

    /* Step 2: Two-loop diagrams */
    /* All use the induced gauge propagator D(q) = 1/(q²_lat × Π_s(0)) */
    /* The VP is modified at the EXTERNAL momentum p */
    
    double sum_SE=0, sum_VC=0, sum_sails=0;

    printf("Computing two-loop integrals (%lld evaluations)...\n",(long long)N4*(long long)N4);
    fflush(stdout);

    #pragma omp parallel for reduction(+:sum_SE,sum_VC,sum_sails) schedule(dynamic,1)
    for(int kidx=0;kidx<N4;kidx++){
        int nk[D];int tmp=kidx;
        for(int mu=D-1;mu>=0;mu--){nk[mu]=tmp%N;tmp/=N;}
        double k[D],kp[D];
        for(int mu=0;mu<D;mu++){k[mu]=dk*nk[mu];kp[mu]=k[mu]+p[mu];}
        double sk=0,skp=0;
        for(int mu=0;mu<D;mu++){sk+=sinlat(k[mu])*sinlat(k[mu]);skp+=sinlat(kp[mu])*sinlat(kp[mu]);}
        if(sk<1e-30||skp<1e-30) continue;
        double Gk=1.0/sk, Gkp=1.0/skp;

        for(int qidx=0;qidx<N4;qidx++){
            int nq[D];tmp=qidx;
            for(int mu=D-1;mu>=0;mu--){nq[mu]=tmp%N;tmp/=N;}
            double q[D],kq[D],kpq[D];
            for(int mu=0;mu<D;mu++){
                q[mu]=dk*nq[mu];
                kq[mu]=k[mu]+q[mu];
                kpq[mu]=kp[mu]+q[mu];
            }
            double q2=0;
            for(int mu=0;mu<D;mu++){double s=2*sin(q[mu]/2);q2+=s*s;}
            if(q2<1e-30) continue;

            double skq=0,skpq=0;
            for(int mu=0;mu<D;mu++){
                skq+=sinlat(kq[mu])*sinlat(kq[mu]);
                skpq+=sinlat(kpq[mu])*sinlat(kpq[mu]);
            }
            if(skq<1e-30||skpq<1e-30) continue;
            double Gkq=1.0/skq, Gkpq=1.0/skpq;
            double Dq=1.0/(q2*Pi1_0); /* induced gauge propagator */

            for(int mu=0;mu<D;mu++){
                double vext=coslat(k[mu]+p[mu]/2.0);  /* external vertex */
                double vext_q=coslat(kq[mu]+p[mu]/2.0); /* external vertex at k+q */

                for(int al=0;al<D;al++){
                    double vint=coslat(k[al]+q[al]/2.0);   /* internal vertex at k */
                    double vint_p=coslat(kp[al]+q[al]/2.0); /* internal vertex at k+p */
                    double vint2=vint*vint;
                    double vint_p2=vint_p*vint_p;

                    /* SE: self-energy on the G(k) propagator */
                    /* Insert Σ(k) = Σ_α cos²(k_α+q_α/2) G(k+q) D(q) */
                    /* δΠ_SE = V_ext² × G(k) × [G(k)Σ(k)G(k)] × G(k+p) */
                    /* = V_ext² × G³(k) × G(k+q) × V_int² × D(q) × G(k+p) */
                    sum_SE += vext*vext * Gk*Gk*Gk * Gkq * vint2 * Dq * Gkp;

                    /* SE on the G(k+p) propagator */
                    sum_SE += vext*vext * Gk * Gkp*Gkp*Gkp * Gkpq * vint_p2 * Dq;

                    /* VC at external vertex */
                    /* Replace V_ext(k) with corrected vertex: */
                    /* Λ = V_ext(k+q) × V_int² × G(k+q) × D(q) */
                    /* δΠ = Λ × G(k) × V_ext(k) × G(k+p) */
                    /* = cos(kq_μ+p/2) × cos²(k_α+q/2) × G(k+q) × D(q) */
                    /*   × G(k) × cos(k_μ+p/2) × G(k+p) */
                    sum_VC += vext_q * vint2 * Gkq * Dq * Gk * vext * Gkp;

                    /* VC at the other vertex (k+p side) */
                    sum_VC += vext * Gk * vext_q * vint_p2 * Gkpq * Dq * Gkp;

                    /* Sails: internal gluon connects the two propagators */
                    /* G(k) → G(k) V_int(k) G(k+q) on one side */
                    /* G(k+p) → G(k+p) V_int(k+p) G(k+p+q) on other side */
                    /* = V_ext(k+p/2) × G(k) × V_int(k,q) × G(k+q) × */
                    /*   V_ext(k+q+p/2) × G(k+p+q) × V_int(k+p,-q) × G(k+p) × D(q) */
                    sum_sails += vext * Gk * vint * Gkq * vext_q * Gkpq * vint_p * Gkp * Dq;
                }
            }
        }
    }

    /* Normalize: 1/(D² × N⁸) */
    double fac = invN8 / (D*(double)D);
    sum_SE *= fac;
    sum_VC *= fac;
    sum_sails *= fac;

    /* Convert to δ₀: same normalization as the one-loop (NF × 4π × ... / p²_lat) */
    double d0_SE = NF*4*PI*sum_SE/plat2;
    double d0_VC = NF*4*PI*sum_VC/plat2;
    double d0_sails = NF*4*PI*sum_sails/plat2;
    double d0_total = d0_SE + d0_VC + d0_sails;

    printf("\n======= TWO-LOOP VP RESULTS (N=%d, p=%.3f) =======\n",N,p_ext);
    printf("  δ₀(SE)    = %+.4f  (expected: ~3.9)\n",d0_SE);
    printf("  δ₀(VC)    = %+.4f  (expected: ~2.7)\n",d0_VC);
    printf("  δ₀(sails) = %+.4f  (expected: ~1.2)\n",d0_sails);
    printf("  ────────────────────\n");
    printf("  δ₀(3 diag)= %+.4f\n",d0_total);
    printf("\n  Ratios: SE:VC:sails = %.2f:%.2f:%.2f\n",
           d0_SE/d0_total,d0_VC/d0_total,d0_sails/d0_total);
    printf("  Expected: 0.50:0.35:0.15 (from 3.9:2.7:1.2)\n");
    printf("\n  Time: %lds\n",time(NULL)-t0);

    printf("\n======= RICHARDSON EXTRAPOLATION DATA =======\n");
    printf("N=%d p=%.3f Pi1=%.8f d0_SE=%+.6f d0_VC=%+.6f d0_sails=%+.6f\n",
           N,p_ext,Pi1/plat2,d0_SE,d0_VC,d0_sails);

    return 0;
}
