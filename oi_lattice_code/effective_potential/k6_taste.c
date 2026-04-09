/*
 * k6_taste.c — Taste-projected CW potential on the K=6 OI lattice
 *
 * Extends k6_cw.c with TASTE-DECOMPOSED condensate measurements.
 * The 8 staggered tastes decompose under O as A₁+T₁+T₂+A₂ (1+3+3+1).
 * Each is measured via point-split bilinears with gauge transport:
 *
 *   A₁ (Higgs):  local condensate,        displacement ξ=(0,0,0)
 *   T₁ (3 gen):  nearest-neighbor split,  ξ=(1,0,0) etc
 *   T₂ (scalar): next-nearest split,      ξ=(1,1,0) etc
 *   A₂ (pseudo): body-diagonal split,     ξ=(1,1,1)
 *
 * The signed CW potential derivative:
 *   V'_CW(m) = C_{A₁} - 3×C_{T₁} + 3×C_{T₂} - C_{A₂}
 *
 * A zero-crossing of V'_CW determines the Higgs VEV → v/M_Pl.
 *
 * Compile: gcc -O3 -fopenmp -o k6_taste k6_taste.c -lm
 * Usage:   ./k6_taste [L] [N_cfg] [N_therm] [outfile]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <omp.h>

#define DIM 3
#define NK 6
#define NC3 3
#define NC2 2
#define CG_TOL 1e-12
#define CG_MAX 10000
#define N_NOISE 8
#define N_MASS 25
#define DECORR 50

typedef struct { double re,im; } Cx;
typedef struct { Cx e[NC3][NC3]; } M3;
typedef struct { Cx e[NC2][NC2]; } M2;

static Cx cx(double r,double i){return(Cx){r,i};}
static Cx cxadd(Cx a,Cx b){return cx(a.re+b.re,a.im+b.im);}
static Cx cxsub(Cx a,Cx b){return cx(a.re-b.re,a.im-b.im);}
static Cx cxmul(Cx a,Cx b){return cx(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re);}
static Cx cxconj(Cx a){return cx(a.re,-a.im);}
static Cx cxscl(Cx a,double s){return cx(a.re*s,a.im*s);}
static double cxabs2(Cx a){return a.re*a.re+a.im*a.im;}

static unsigned int *rng_seeds;
static void rng_init(int nt){rng_seeds=malloc(nt*sizeof(unsigned int));unsigned int base=(unsigned int)time(NULL);for(int i=0;i<nt;i++)rng_seeds[i]=base^(i*2654435761u);}
static double drand01_t(unsigned int *s){*s=(*s)*1103515245u+12345u;return(double)(*s>>1)/((double)(1u<<31));}
static double gauss01_t(unsigned int *s){double u=drand01_t(s),v=drand01_t(s);while(u<1e-15)u=drand01_t(s);return sqrt(-2*log(u))*cos(2*M_PI*v);}
static double drand01(void){return drand01_t(&rng_seeds[0]);}
static double gauss01(void){return gauss01_t(&rng_seeds[0]);}

static int L,VOL;
static M3 *U3; static M2 *U2; static double *U1;

static int site(int x,int y,int z){return((x%L+L)%L)*L*L+((y%L+L)%L)*L+((z%L+L)%L);}
static int nbr(int s,int mu,int dir){int c[3]={s/(L*L),(s/L)%L,s%L};c[mu]+=dir;return site(c[0],c[1],c[2]);}
static double eta(int s,int mu){int c[3]={s/(L*L),(s/L)%L,s%L};int ph=0;for(int i=0;i<mu;i++)ph+=c[i];return(ph%2==0)?1.0:-1.0;}

/* Staggered taste phase: epsilon_xi(x) = (-1)^{sum_{mu>nu} xi_mu x_nu} */
static double taste_phase(int s, int *xi) {
    int c[3] = { s/(L*L), (s/L)%L, s%L };
    int ph = 0;
    for (int mu = 0; mu < DIM; mu++)
        for (int nu = 0; nu < mu; nu++)
            ph += xi[mu] * c[nu];
    return (ph % 2 == 0) ? 1.0 : -1.0;
}

/* ---- SU(3) ---- */
static M3 m3_unit(void){M3 m;memset(&m,0,sizeof(m));for(int i=0;i<NC3;i++)m.e[i][i]=cx(1,0);return m;}
static M3 m3_mul(M3 a,M3 b){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC3;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static M3 m3_dag(M3 a){M3 b;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static M3 m3_add(M3 a,M3 b){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static double m3_retr(M3 a){double t=0;for(int i=0;i<NC3;i++)t+=a.e[i][i].re;return t;}
static M3 m3_proj(M3 a){M3 u;double n=0;for(int j=0;j<NC3;j++)n+=cxabs2(a.e[0][j]);n=1.0/sqrt(n);for(int j=0;j<NC3;j++)u.e[0][j]=cxscl(a.e[0][j],n);Cx d=cx(0,0);for(int j=0;j<NC3;j++)d=cxadd(d,cxmul(cxconj(u.e[0][j]),a.e[1][j]));for(int j=0;j<NC3;j++)u.e[1][j]=cxsub(a.e[1][j],cxmul(d,u.e[0][j]));n=0;for(int j=0;j<NC3;j++)n+=cxabs2(u.e[1][j]);n=1.0/sqrt(n);for(int j=0;j<NC3;j++)u.e[1][j]=cxscl(u.e[1][j],n);u.e[2][0]=cxsub(cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][2])),cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][1])));u.e[2][1]=cxsub(cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][0])),cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][2])));u.e[2][2]=cxsub(cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][1])),cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][0])));return u;}
static M3 m3_rand(double eps){M3 h;for(int i=0;i<NC3;i++)for(int j=i;j<NC3;j++){if(i==j)h.e[i][j]=cx(gauss01()*eps,0);else{double r1=gauss01()*eps,r2=gauss01()*eps;h.e[i][j]=cx(r1,r2);h.e[j][i]=cx(r1,-r2);}}double tr=0;for(int i=0;i<NC3;i++)tr+=h.e[i][i].re;tr/=NC3;for(int i=0;i<NC3;i++)h.e[i][i].re-=tr;M3 u=m3_unit();for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)u.e[i][j]=cxadd(u.e[i][j],cx(-h.e[i][j].im,h.e[i][j].re));return m3_proj(u);}

/* ---- SU(2) ---- */
static M2 m2_unit(void){M2 m;memset(&m,0,sizeof(m));for(int i=0;i<NC2;i++)m.e[i][i]=cx(1,0);return m;}
static M2 m2_mul(M2 a,M2 b){M2 c;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC2;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static M2 m2_dag(M2 a){M2 b;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static M2 m2_add(M2 a,M2 b){M2 c;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static double m2_retr(M2 a){double t=0;for(int i=0;i<NC2;i++)t+=a.e[i][i].re;return t;}
static M2 m2_proj(M2 a){Cx d=cxsub(cxmul(a.e[0][0],a.e[1][1]),cxmul(a.e[0][1],a.e[1][0]));double nd=sqrt(cxabs2(d));if(nd<1e-15)return m2_unit();M2 u;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)u.e[i][j]=cxscl(a.e[i][j],1.0/nd);u.e[1][0]=cxscl(cxconj(u.e[0][1]),-1);u.e[1][1]=cxconj(u.e[0][0]);double n0=sqrt(cxabs2(u.e[0][0])+cxabs2(u.e[0][1]));for(int j=0;j<NC2;j++){u.e[0][j]=cxscl(u.e[0][j],1.0/n0);u.e[1][j]=cxscl(u.e[1][j],1.0/n0);}return u;}
static M2 m2_rand(double eps){M2 h;double a1=gauss01()*eps,a2=gauss01()*eps,a3=gauss01()*eps;h.e[0][0]=cx(1,a3);h.e[0][1]=cx(a2,a1);h.e[1][0]=cx(-a2,a1);h.e[1][1]=cx(1,-a3);return m2_proj(h);}

/* ---- Gauge transport for component a along direction mu ---- */
static Cx gauge_fwd(int s, int mu, int a, Cx *v_in) {
    int sp = nbr(s, mu, +1);
    Cx result = cx(0,0);
    if (a < NC3) {
        for (int b=0; b<NC3; b++)
            result = cxadd(result, cxmul(U3[s*DIM+mu].e[a][b], v_in[sp*NK+b]));
    } else if (a < NC3+NC2) {
        int a2 = a - NC3;
        for (int b=0; b<NC2; b++)
            result = cxadd(result, cxmul(U2[s*DIM+mu].e[a2][b], v_in[sp*NK+NC3+b]));
    } else {
        result = cxmul(cx(cos(U1[s*DIM+mu]), sin(U1[s*DIM+mu])), v_in[sp*NK+5]);
    }
    return result;
}

/* ---- Gauge updates ---- */
static M3 m3_staple(int s,int mu){M3 st;memset(&st,0,sizeof(st));for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st=m3_add(st,m3_add(m3_mul(U3[smu*DIM+nu],m3_mul(m3_dag(U3[snu*DIM+mu]),m3_dag(U3[s*DIM+nu]))),m3_mul(m3_dag(U3[smnu_mu*DIM+nu]),m3_mul(m3_dag(U3[smnu*DIM+mu]),U3[smnu*DIM+nu]))));}return st;}
static M2 m2_staple(int s,int mu){M2 st;memset(&st,0,sizeof(st));for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st=m2_add(st,m2_add(m2_mul(U2[smu*DIM+nu],m2_mul(m2_dag(U2[snu*DIM+mu]),m2_dag(U2[s*DIM+nu]))),m2_mul(m2_dag(U2[smnu_mu*DIM+nu]),m2_mul(m2_dag(U2[smnu*DIM+mu]),U2[smnu*DIM+nu]))));}return st;}
static double u1_staple(int s,int mu){double st=0;for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st+=sin(U1[smu*DIM+nu]-U1[snu*DIM+mu]-U1[s*DIM+nu]);st+=sin(-U1[smnu_mu*DIM+nu]-U1[smnu*DIM+mu]+U1[smnu*DIM+nu]);}return st;}

static int sweep_gauge(double b3,double b2,double b1,double eps){
    int acc=0,tot=0;
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
        {double So=-(b3/NC3)*m3_retr(m3_mul(U3[s*DIM+mu],m3_staple(s,mu)));M3 Uo=U3[s*DIM+mu];U3[s*DIM+mu]=m3_proj(m3_mul(m3_rand(eps),Uo));double Sn=-(b3/NC3)*m3_retr(m3_mul(U3[s*DIM+mu],m3_staple(s,mu)));if(Sn-So<0||drand01()<exp(-(Sn-So)))acc++;else U3[s*DIM+mu]=Uo;tot++;}
        {double So=-(b2/NC2)*m2_retr(m2_mul(U2[s*DIM+mu],m2_staple(s,mu)));M2 Uo=U2[s*DIM+mu];U2[s*DIM+mu]=m2_proj(m2_mul(m2_rand(eps),Uo));double Sn=-(b2/NC2)*m2_retr(m2_mul(U2[s*DIM+mu],m2_staple(s,mu)));if(Sn-So<0||drand01()<exp(-(Sn-So)))acc++;else U2[s*DIM+mu]=Uo;tot++;}
        {double stap=u1_staple(s,mu);double old=U1[s*DIM+mu];double So=-b1*cos(old)*stap;double th_new=old+eps*(2*drand01()-1);double Sn=-b1*cos(th_new)*stap;if(Sn-So<0||drand01()<exp(-(Sn-So))){U1[s*DIM+mu]=th_new;acc++;}tot++;}
    }
    return(100*acc)/tot;
}

static void plaquettes(double *p3,double *p2,double *p1){double s3=0,s2=0,s1=0;int n=0;for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++)for(int nu=mu+1;nu<DIM;nu++){int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1);s3+=m3_retr(m3_mul(m3_mul(U3[s*DIM+mu],U3[smu*DIM+nu]),m3_mul(m3_dag(U3[snu*DIM+mu]),m3_dag(U3[s*DIM+nu]))))/NC3;s2+=m2_retr(m2_mul(m2_mul(U2[s*DIM+mu],U2[smu*DIM+nu]),m2_mul(m2_dag(U2[snu*DIM+mu]),m2_dag(U2[s*DIM+nu]))))/NC2;double tp=U1[s*DIM+mu]+U1[smu*DIM+nu]-U1[snu*DIM+mu]-U1[s*DIM+nu];s1+=cos(tp);n++;}*p3=s3/n;*p2=s2/n;*p1=s1/n;}

/* ---- K=6 Dirac operator ---- */
static void apply_D(Cx *dst,Cx *src,double mass){
    for(int s=0;s<VOL;s++){
        for(int a=0;a<NK;a++) dst[s*NK+a]=cxscl(src[s*NK+a],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int a=0;a<NK;a++){
                Cx fwd=cx(0,0);
                if(a<NC3){for(int b=0;b<NC3;b++)fwd=cxadd(fwd,cxmul(U3[s*DIM+mu].e[a][b],src[sp*NK+b]));}
                else if(a<NC3+NC2){int a2=a-NC3;for(int b=0;b<NC2;b++)fwd=cxadd(fwd,cxmul(U2[s*DIM+mu].e[a2][b],src[sp*NK+NC3+b]));}
                else fwd=cxmul(cx(cos(U1[s*DIM+mu]),sin(U1[s*DIM+mu])),src[sp*NK+5]);
                dst[s*NK+a]=cxadd(dst[s*NK+a],cxscl(fwd,ph));
                Cx bwd=cx(0,0);
                if(a<NC3){for(int b=0;b<NC3;b++)bwd=cxadd(bwd,cxmul(cxconj(U3[sm*DIM+mu].e[b][a]),src[sm*NK+b]));}
                else if(a<NC3+NC2){int a2=a-NC3;for(int b=0;b<NC2;b++)bwd=cxadd(bwd,cxmul(cxconj(U2[sm*DIM+mu].e[b][a2]),src[sm*NK+NC3+b]));}
                else bwd=cxmul(cx(cos(U1[sm*DIM+mu]),-sin(U1[sm*DIM+mu])),src[sm*NK+5]);
                dst[s*NK+a]=cxsub(dst[s*NK+a],cxscl(bwd,ph));
            }
        }
    }
}

static void apply_DdD(Cx *dst,Cx *src,double mass){
    int N=VOL*NK;Cx *tmp=malloc(N*sizeof(Cx));
    apply_D(tmp,src,mass);
    for(int s=0;s<VOL;s++){
        for(int a=0;a<NK;a++) dst[s*NK+a]=cxscl(tmp[s*NK+a],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=-eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int a=0;a<NK;a++){
                Cx fwd=cx(0,0);
                if(a<NC3){for(int b=0;b<NC3;b++)fwd=cxadd(fwd,cxmul(U3[s*DIM+mu].e[a][b],tmp[sp*NK+b]));}
                else if(a<NC3+NC2){int a2=a-NC3;for(int b=0;b<NC2;b++)fwd=cxadd(fwd,cxmul(U2[s*DIM+mu].e[a2][b],tmp[sp*NK+NC3+b]));}
                else fwd=cxmul(cx(cos(U1[s*DIM+mu]),sin(U1[s*DIM+mu])),tmp[sp*NK+5]);
                dst[s*NK+a]=cxadd(dst[s*NK+a],cxscl(fwd,ph));
                Cx bwd=cx(0,0);
                if(a<NC3){for(int b=0;b<NC3;b++)bwd=cxadd(bwd,cxmul(cxconj(U3[sm*DIM+mu].e[b][a]),tmp[sm*NK+b]));}
                else if(a<NC3+NC2){int a2=a-NC3;for(int b=0;b<NC2;b++)bwd=cxadd(bwd,cxmul(cxconj(U2[sm*DIM+mu].e[b][a2]),tmp[sm*NK+NC3+b]));}
                else bwd=cxmul(cx(cos(U1[sm*DIM+mu]),-sin(U1[sm*DIM+mu])),tmp[sm*NK+5]);
                dst[s*NK+a]=cxsub(dst[s*NK+a],cxscl(bwd,ph));
            }
        }
    }
    free(tmp);
}

static int cg(Cx *x,Cx *b,double mass){
    int N=VOL*NK;Cx *r=malloc(N*sizeof(Cx)),*p=malloc(N*sizeof(Cx)),*Ap=malloc(N*sizeof(Cx));
    memset(x,0,N*sizeof(Cx));memcpy(r,b,N*sizeof(Cx));memcpy(p,b,N*sizeof(Cx));
    double rr=0;
    #pragma omp parallel for reduction(+:rr)
    for(int i=0;i<N;i++)rr+=cxabs2(r[i]);
    double rr0=rr;if(rr0<1e-30){free(r);free(p);free(Ap);return 0;}
    int it;for(it=0;it<CG_MAX;it++){
        apply_DdD(Ap,p,mass);double pAp=0;
        #pragma omp parallel for reduction(+:pAp)
        for(int i=0;i<N;i++)pAp+=Ap[i].re*p[i].re+Ap[i].im*p[i].im;
        if(fabs(pAp)<1e-30)break;double alpha=rr/pAp;
        #pragma omp parallel for
        for(int i=0;i<N;i++){x[i]=cxadd(x[i],cxscl(p[i],alpha));r[i]=cxsub(r[i],cxscl(Ap[i],alpha));}
        double rr_new=0;
        #pragma omp parallel for reduction(+:rr_new)
        for(int i=0;i<N;i++)rr_new+=cxabs2(r[i]);
        if(rr_new/rr0<CG_TOL*CG_TOL){it++;break;}
        double bc=rr_new/rr;
        #pragma omp parallel for
        for(int i=0;i<N;i++)p[i]=cxadd(r[i],cxscl(p[i],bc));
        rr=rr_new;
    }
    free(r);free(p);free(Ap);return it;
}

/* ---- Taste-projected condensate measurement ---- */
typedef struct {
    double C_A1;    /* local (Higgs taste) */
    double C_T1;    /* 1-link split (generation tastes) */
    double C_T2;    /* 2-link split */
    double C_A2;    /* 3-link split (pseudoscalar) */
    double C_total; /* sum of all */
    double V_CW;    /* signed CW combination */
    int cg_iters;
} TasteResult;

static TasteResult measure_taste(double mass, unsigned int *seed) {
    int N = VOL * NK;
    Cx *ev = malloc(N*sizeof(Cx)), *sol = malloc(N*sizeof(Cx));
    double a1=0, t1=0, t2=0, a2=0;
    int tot_cg = 0;

    for (int hit = 0; hit < N_NOISE; hit++) {
        for (int i = 0; i < N; i++)
            ev[i] = cx((drand01_t(seed)<0.5)?1.0:-1.0, 0.0);
        int its = cg(sol, ev, mass); tot_cg += its;

        double d_a1=0, d_t1=0, d_t2=0, d_a2=0;

        /* A₁: local condensate ξ=(0,0,0) */
        #pragma omp parallel for reduction(+:d_a1)
        for (int s = 0; s < VOL; s++)
            for (int a = 0; a < NK; a++)
                d_a1 += ev[s*NK+a].re*sol[s*NK+a].re + ev[s*NK+a].im*sol[s*NK+a].im;

        /* T₁: 1-link displacements ξ=(1,0,0),(0,1,0),(0,0,1) */
        for (int mu = 0; mu < DIM; mu++) {
            int xi[3] = {0,0,0}; xi[mu] = 1;
            double d_mu = 0;
            #pragma omp parallel for reduction(+:d_mu)
            for (int s = 0; s < VOL; s++) {
                double ph = taste_phase(s, xi);
                for (int a = 0; a < NK; a++) {
                    /* gauge-transported solution at s+mu */
                    Cx gsol = gauge_fwd(s, mu, a, sol);
                    d_mu += ph * (ev[s*NK+a].re*gsol.re + ev[s*NK+a].im*gsol.im);
                }
            }
            d_t1 += d_mu / 3.0;
        }

        /* T₂: 2-link displacements ξ=(1,1,0),(1,0,1),(0,1,1) */
        int t2_disps[3][3] = {{1,1,0},{1,0,1},{0,1,1}};
        for (int d = 0; d < 3; d++) {
            int mu1=-1, mu2=-1;
            for (int mu=0; mu<DIM; mu++) if(t2_disps[d][mu]) { if(mu1<0) mu1=mu; else mu2=mu; }
            int *xi = t2_disps[d];
            double d_d = 0;
            /* Transport: first along mu1, then along mu2 */
            /* Need to create an intermediate transported vector */
            Cx *tmp1 = malloc(N*sizeof(Cx));
            /* First hop: tmp1(s,a) = U_{mu1}(s,a) * sol(s+mu1,a) */
            for (int s = 0; s < VOL; s++)
                for (int a = 0; a < NK; a++)
                    tmp1[s*NK+a] = gauge_fwd(s, mu1, a, sol);
            /* Second hop: U_{mu2}(s,a) * tmp1(s+mu2,a) but we need tmp1 at s+mu2 */
            /* Actually: we want U_{mu1}(s) U_{mu2}(s+mu1) sol(s+mu1+mu2) */
            /* = gauge_fwd(s, mu1, a, [gauge_fwd(·, mu2, ·, sol)]) */
            /* Let's compute it differently: */
            /* tmp2(s,a) = U_{mu2}(s+mu1, a) * sol(s+mu1+mu2, a) */
            /* Then result = U_{mu1}(s,a) * tmp2(s+mu1, a) */
            /* But tmp2 is defined at site s+mu1, so we need sol shifted */
            /* Simpler: just do it site by site */
            #pragma omp parallel for reduction(+:d_d)
            for (int s = 0; s < VOL; s++) {
                double ph = taste_phase(s, xi);
                int s1 = nbr(s, mu1, +1);
                for (int a = 0; a < NK; a++) {
                    /* U_{mu2}(s+mu1) * sol(s+mu1+mu2) */
                    Cx hop2 = gauge_fwd(s1, mu2, a, sol);
                    /* U_{mu1}(s) * hop2 — but gauge_fwd expects a vector array */
                    /* Do it manually for each gauge group */
                    Cx hop1 = cx(0,0);
                    if (a < NC3) {
                        /* Need U3_{mu1}(s) * [U3_{mu2}(s1) * sol(s1+mu2)] */
                        /* hop2 already has the right color index mixing from gauge_fwd */
                        /* But gauge_fwd returns a scalar Cx, already contracted */
                        /* We need the full color vector first... */
                        /* Actually gauge_fwd contracts over internal indices already */
                        /* So we can't chain two gauge_fwd calls for different sites */
                        /* Need to compute the product of two link matrices first */
                        int s12 = nbr(s1, mu2, +1);
                        Cx val = cx(0,0);
                        for (int b = 0; b < NC3; b++) {
                            Cx inner = cx(0,0);
                            for (int c = 0; c < NC3; c++)
                                inner = cxadd(inner, cxmul(U3[s1*DIM+mu2].e[b][c], sol[s12*NK+c]));
                            val = cxadd(val, cxmul(U3[s*DIM+mu1].e[a][b], inner));
                        }
                        hop1 = val;
                    } else if (a < NC3+NC2) {
                        int a2 = a - NC3;
                        int s12 = nbr(s1, mu2, +1);
                        Cx val = cx(0,0);
                        for (int b = 0; b < NC2; b++) {
                            Cx inner = cx(0,0);
                            for (int c = 0; c < NC2; c++)
                                inner = cxadd(inner, cxmul(U2[s1*DIM+mu2].e[b][c], sol[s12*NK+NC3+c]));
                            val = cxadd(val, cxmul(U2[s*DIM+mu1].e[a2][b], inner));
                        }
                        hop1 = val;
                    } else {
                        int s12 = nbr(s1, mu2, +1);
                        double th1 = U1[s*DIM+mu1], th2 = U1[s1*DIM+mu2];
                        hop1 = cxmul(cx(cos(th1+th2), sin(th1+th2)), sol[s12*NK+5]);
                    }
                    d_d += ph * (ev[s*NK+a].re*hop1.re + ev[s*NK+a].im*hop1.im);
                }
            }
            free(tmp1);
            d_t2 += d_d / 3.0;
        }

        /* A₂: 3-link displacement ξ=(1,1,1), path: 0→1→2 */
        {
            int xi[3] = {1,1,1};
            double d_3 = 0;
            #pragma omp parallel for reduction(+:d_3)
            for (int s = 0; s < VOL; s++) {
                double ph = taste_phase(s, xi);
                int s0 = nbr(s, 0, +1);
                int s01 = nbr(s0, 1, +1);
                int s012 = nbr(s01, 2, +1);
                for (int a = 0; a < NK; a++) {
                    Cx hop = cx(0,0);
                    if (a < NC3) {
                        for (int b=0; b<NC3; b++) {
                            Cx h2 = cx(0,0);
                            for (int c=0; c<NC3; c++) {
                                Cx h3 = cx(0,0);
                                for (int d=0; d<NC3; d++)
                                    h3 = cxadd(h3, cxmul(U3[s01*DIM+2].e[c][d], sol[s012*NK+d]));
                                h2 = cxadd(h2, cxmul(U3[s0*DIM+1].e[b][c], h3));
                            }
                            hop = cxadd(hop, cxmul(U3[s*DIM+0].e[a][b], h2));
                        }
                    } else if (a < NC3+NC2) {
                        int a2 = a-NC3;
                        for (int b=0; b<NC2; b++) {
                            Cx h2 = cx(0,0);
                            for (int c=0; c<NC2; c++) {
                                Cx h3 = cx(0,0);
                                for (int d=0; d<NC2; d++)
                                    h3 = cxadd(h3, cxmul(U2[s01*DIM+2].e[c][d], sol[s012*NK+NC3+d]));
                                h2 = cxadd(h2, cxmul(U2[s0*DIM+1].e[b][c], h3));
                            }
                            hop = cxadd(hop, cxmul(U2[s*DIM+0].e[a2][b], h2));
                        }
                    } else {
                        double th = U1[s*DIM+0]+U1[s0*DIM+1]+U1[s01*DIM+2];
                        hop = cxmul(cx(cos(th),sin(th)), sol[s012*NK+5]);
                    }
                    d_3 += ph * (ev[s*NK+a].re*hop.re + ev[s*NK+a].im*hop.im);
                }
            }
            d_a2 = d_3;
        }

        a1 += mass*d_a1/VOL;
        t1 += mass*d_t1/VOL;
        t2 += mass*d_t2/VOL;
        a2 += mass*d_a2/VOL;
    }
    free(ev); free(sol);
    TasteResult r;
    r.C_A1 = a1/N_NOISE; r.C_T1 = t1/N_NOISE;
    r.C_T2 = t2/N_NOISE; r.C_A2 = a2/N_NOISE;
    r.C_total = r.C_A1 + 3*r.C_T1 + 3*r.C_T2 + r.C_A2;
    r.V_CW = r.C_A1 - 3*r.C_T1 + 3*r.C_T2 - r.C_A2;
    r.cg_iters = tot_cg / N_NOISE;
    return r;
}

static void fmt_time(double s,char *b){int h=(int)(s/3600),m=(int)((s-h*3600)/60);int sec=(int)(s-h*3600-m*60);if(h>0)sprintf(b,"%dh%02dm%02ds",h,m,sec);else if(m>0)sprintf(b,"%dm%02ds",m,sec);else sprintf(b,"%.1fs",s);}

/* ---- Main ---- */
int main(int argc, char **argv) {
    L=(argc>1)?atoi(argv[1]):12;
    int Ncfg=(argc>2)?atoi(argv[2]):30;
    int Nthm=(argc>3)?atoi(argv[3]):500;
    const char *outf=(argc>4)?argv[4]:"k6_taste.dat";
    VOL=L*L*L;
    double beta3=11.1, beta2=7.4, beta1=3.7;
    time_t T0=time(NULL); char tb[64];

    int nthreads;
    #pragma omp parallel
    { nthreads=omp_get_num_threads(); }
    rng_init(nthreads);

    double mpts[N_MASS];
    for(int i=0;i<N_MASS;i++) mpts[i]=0.01*pow(50.0,(double)i/(N_MASS-1));

    U3=malloc(VOL*DIM*sizeof(M3)); U2=malloc(VOL*DIM*sizeof(M2));
    U1=calloc(VOL*DIM,sizeof(double));
    for(int i=0;i<VOL*DIM;i++){U3[i]=m3_unit();U2[i]=m2_unit();}

    fprintf(stderr,"\n  k6_taste: Taste-projected CW potential\n");
    fprintf(stderr,"  SU(3)xSU(2)xU(1) β=(%.1f,%.1f,%.1f) L=%d threads=%d\n\n",beta3,beta2,beta1,L,nthreads);

    /* Thermalize */
    double eps=0.3;
    fprintf(stderr,"  Thermalizing (%d sweeps)...\n",Nthm);
    for(int sw=0;sw<Nthm;sw++){
        int rate=sweep_gauge(beta3,beta2,beta1,eps);
        if(sw%50==0){if(rate<30)eps*=0.8;if(rate>50)eps*=1.2;}
        if(sw%(Nthm/5)==0){double p3,p2,p1;plaquettes(&p3,&p2,&p1);
            fmt_time(difftime(time(NULL),T0),tb);
            fprintf(stderr,"    [%s] sweep %d: acc=%d%% P3=%.4f P2=%.4f P1=%.4f\n",tb,sw+1,rate,p3,p2,p1);}
    }
    fprintf(stderr,"  Done.\n\n");

    FILE *fp=fopen(outf,"a");
    time_t tnow=time(NULL);
    fprintf(fp,"# k6_taste L=%d beta=(%.1f,%.1f,%.1f) Ncfg=%d threads=%d\n",L,beta3,beta2,beta1,Ncfg,nthreads);
    fprintf(fp,"# started %s",ctime(&tnow));
    fprintf(fp,"# cfg  mass       C_A1         C_T1         C_T2         C_A2         C_total      V_CW         CG\n");
    fflush(fp);

    fprintf(stderr,"  Measuring %d cfgs x %d masses...\n\n",Ncfg,N_MASS);
    time_t Tmeas=time(NULL);

    /* Running averages */
    double vcw_sum[N_MASS]; memset(vcw_sum,0,sizeof(vcw_sum));

    for(int cfg=0;cfg<Ncfg;cfg++){
        time_t Tcfg=time(NULL);
        for(int sw=0;sw<DECORR;sw++) sweep_gauge(beta3,beta2,beta1,eps);

        for(int mi=0;mi<N_MASS;mi++){
            TasteResult r=measure_taste(mpts[mi],&rng_seeds[0]);
            fprintf(fp,"%4d  %.6f  %12.6f %12.6f %12.6f %12.6f %12.6f %12.6f %d\n",
                    cfg,mpts[mi],r.C_A1,r.C_T1,r.C_T2,r.C_A2,r.C_total,r.V_CW,r.cg_iters);
            vcw_sum[mi] += r.V_CW;
        }
        fflush(fp);

        int nd=cfg+1;
        double tcfg=difftime(time(NULL),Tcfg);
        double eta_s=(difftime(time(NULL),Tmeas)/nd)*(Ncfg-nd);
        char tb1[64],tb2[64];
        fmt_time(difftime(time(NULL),T0),tb1); fmt_time(eta_s,tb2);

        fprintf(stderr,"  cfg %d/%d [%s] ETA %s\n",nd,Ncfg,tb1,tb2);

        /* Check for sign change */
        if(nd>=2){
            int sign_change=-1;
            for(int mi=1;mi<N_MASS;mi++){
                double v1=vcw_sum[mi-1]/nd, v2=vcw_sum[mi]/nd;
                if(v1*v2<0){sign_change=mi;break;}
            }
            if(sign_change>=0)
                fprintf(stderr,"    *** V'_CW sign change at m ~ %.4f! ***\n",mpts[sign_change]);
            else
                fprintf(stderr,"    V'_CW(m=%.3f)=%.4f  V'_CW(m=%.3f)=%.4f (no sign change)\n",
                        mpts[0],vcw_sum[0]/nd,mpts[N_MASS-1],vcw_sum[N_MASS-1]/nd);
        }
        fprintf(stderr,"\n");
    }

    /* Summary */
    double ttot=difftime(time(NULL),T0); fmt_time(ttot,tb);
    fprintf(stderr,"  Done (%s). Summary:\n\n",tb);
    fprintf(fp,"\n# SUMMARY (%d cfgs)\n",Ncfg);
    fprintf(fp,"# mass       C_A1     C_T1     C_T2     C_A2     V_CW\n");
    fprintf(stderr,"  %8s  %8s  %8s  %8s  %8s  %10s\n","mass","C_A1","C_T1","C_T2","C_A2","V'_CW");
    fprintf(stderr,"  --------  --------  --------  --------  --------  ----------\n");
    /* Note: we'd need per-mass running sums for all channels. For simplicity,
       re-read from the raw data or add accumulators. Here just print V_CW: */
    for(int mi=0;mi<N_MASS;mi++){
        double vcw=vcw_sum[mi]/Ncfg;
        fprintf(fp,"  %.6f  %10.6f\n",mpts[mi],vcw);
        fprintf(stderr,"  %8.5f  %49s %10.6f\n",mpts[mi],"",vcw);
    }
    fprintf(stderr,"\n  If V'_CW changes sign, the zero gives v/M_Pl.\n\n");

    fclose(fp); free(U3); free(U2); free(U1);
    return 0;
}
