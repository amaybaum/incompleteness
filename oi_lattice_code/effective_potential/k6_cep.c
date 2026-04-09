/*
 * k6_cep.c — K=6 Constraint Effective Potential
 *
 * HMC with dynamical staggered fermions + gauge-Higgs coupling.
 * Scans the background Higgs field h and measures dV/dh decomposed
 * into fermion and gauge contributions. A sign change in dV/dh
 * indicates a VEV — the electroweak scale v/M_Pl.
 *
 * Physics: The uniform Higgs background h enters two ways:
 *   1. Fermion mass: m_eff = m + h (Yukawa coupling)
 *   2. Gauge-Higgs: -h² Σ Re[U₂]₂₂ (W/Z mass from Higgs)
 *               and -h² Σ cos(θ₁/2) (hypercharge Y=1/2)
 *
 * The fermion contribution to dV/dh is always negative (drives h up).
 * The gauge-Higgs contribution competes. The VEV is where they balance.
 *
 * Compile: gcc -O3 -fopenmp -o k6_cep k6_cep.c -lm
 * Usage:   ./k6_cep [L] [mass] [higgs_h] [N_traj] [N_therm] [outfile]
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
#define CG_TOL 1e-10
#define CG_MAX 5000

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

static unsigned int rng_seed;
static double drand01(void){rng_seed=rng_seed*1103515245u+12345u;return(double)(rng_seed>>1)/((double)(1u<<31));}
static double gauss01(void){double u=drand01(),v=drand01();while(u<1e-15)u=drand01();return sqrt(-2*log(u))*cos(2*M_PI*v);}

static int L,VOL;
static M3 *U3; static M2 *U2; static double *U1;
static M3 *U3_bak; static M2 *U2_bak; static double *U1_bak;

/* Momenta (traceless anti-hermitian for SU(N), real for U(1)) */
static M3 *P3; static M2 *P2; static double *P1;

/* Pseudofermion and solution */
static Cx *phi, *chi;

static int site(int x,int y,int z){return((x%L+L)%L)*L*L+((y%L+L)%L)*L+((z%L+L)%L);}
static int nbr(int s,int mu,int dir){int c[3]={s/(L*L),(s/L)%L,s%L};c[mu]+=dir;return site(c[0],c[1],c[2]);}
static double stag_eta(int s,int mu){int c[3]={s/(L*L),(s/L)%L,s%L};int ph=0;for(int i=0;i<mu;i++)ph+=c[i];return(ph%2==0)?1.0:-1.0;}

/* ---- SU(3) operations ---- */
static M3 m3_unit(void){M3 m;memset(&m,0,sizeof(m));for(int i=0;i<NC3;i++)m.e[i][i]=cx(1,0);return m;}
static M3 m3_zero(void){M3 m;memset(&m,0,sizeof(m));return m;}
static M3 m3_mul(M3 a,M3 b){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC3;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static M3 m3_dag(M3 a){M3 b;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static M3 m3_add(M3 a,M3 b){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static M3 m3_scl(M3 a,double s){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)c.e[i][j]=cxscl(a.e[i][j],s);return c;}
static double m3_retr(M3 a){double t=0;for(int i=0;i<NC3;i++)t+=a.e[i][i].re;return t;}
/* Reproject to SU(3) via Gram-Schmidt */
static M3 m3_proj(M3 a){
    M3 u;double n;
    n=0;for(int j=0;j<NC3;j++)n+=cxabs2(a.e[0][j]);n=1.0/sqrt(n);
    for(int j=0;j<NC3;j++)u.e[0][j]=cxscl(a.e[0][j],n);
    Cx d=cx(0,0);for(int j=0;j<NC3;j++)d=cxadd(d,cxmul(cxconj(u.e[0][j]),a.e[1][j]));
    for(int j=0;j<NC3;j++)u.e[1][j]=cxsub(a.e[1][j],cxmul(d,u.e[0][j]));
    n=0;for(int j=0;j<NC3;j++)n+=cxabs2(u.e[1][j]);n=1.0/sqrt(n);
    for(int j=0;j<NC3;j++)u.e[1][j]=cxscl(u.e[1][j],n);
    u.e[2][0]=cxsub(cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][2])),cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][1])));
    u.e[2][1]=cxsub(cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][0])),cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][2])));
    u.e[2][2]=cxsub(cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][1])),cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][0])));
    return u;
}
/* Traceless anti-hermitian projection */
static M3 m3_ta(M3 a){
    M3 r;
    for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)
        r.e[i][j]=cxscl(cxsub(a.e[i][j],cxconj(a.e[j][i])),0.5);
    Cx tr=cx(0,0);for(int i=0;i<NC3;i++)tr=cxadd(tr,r.e[i][i]);
    for(int i=0;i<NC3;i++)r.e[i][i]=cxsub(r.e[i][i],cxscl(tr,1.0/NC3));
    return r;
}
/* U' = exp(eps*P)*U via Taylor to 8th order */
static M3 m3_evolve(M3 U,M3 P,double eps){
    M3 eP=m3_unit(),Pn=m3_unit();
    for(int n=1;n<=8;n++){Pn=m3_mul(Pn,m3_scl(P,eps/(double)n));eP=m3_add(eP,Pn);}
    return m3_proj(m3_mul(eP,U));
}

/* ---- SU(2) operations ---- */
static M2 m2_unit(void){M2 m;memset(&m,0,sizeof(m));for(int i=0;i<NC2;i++)m.e[i][i]=cx(1,0);return m;}
static M2 m2_zero(void){M2 m;memset(&m,0,sizeof(m));return m;}
static M2 m2_mul(M2 a,M2 b){M2 c;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC2;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static M2 m2_dag(M2 a){M2 b;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static M2 m2_add(M2 a,M2 b){M2 c;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static M2 m2_scl(M2 a,double s){M2 c;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)c.e[i][j]=cxscl(a.e[i][j],s);return c;}
static double m2_retr(M2 a){double t=0;for(int i=0;i<NC2;i++)t+=a.e[i][i].re;return t;}
static M2 m2_proj(M2 a){
    Cx d=cxsub(cxmul(a.e[0][0],a.e[1][1]),cxmul(a.e[0][1],a.e[1][0]));
    double nd=sqrt(cxabs2(d));if(nd<1e-15)return m2_unit();
    M2 u;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)u.e[i][j]=cxscl(a.e[i][j],1.0/nd);
    u.e[1][0]=cxscl(cxconj(u.e[0][1]),-1);u.e[1][1]=cxconj(u.e[0][0]);
    double n0=sqrt(cxabs2(u.e[0][0])+cxabs2(u.e[0][1]));
    for(int j=0;j<NC2;j++){u.e[0][j]=cxscl(u.e[0][j],1.0/n0);u.e[1][j]=cxscl(u.e[1][j],1.0/n0);}
    return u;
}
static M2 m2_ta(M2 a){
    M2 r;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)
        r.e[i][j]=cxscl(cxsub(a.e[i][j],cxconj(a.e[j][i])),0.5);
    Cx tr=cx(0,0);for(int i=0;i<NC2;i++)tr=cxadd(tr,r.e[i][i]);
    for(int i=0;i<NC2;i++)r.e[i][i]=cxsub(r.e[i][i],cxscl(tr,1.0/NC2));
    return r;
}
static M2 m2_evolve(M2 U,M2 P,double eps){
    M2 eP=m2_unit(),Pn=m2_unit();
    for(int n=1;n<=6;n++){Pn=m2_mul(Pn,m2_scl(P,eps/(double)n));eP=m2_add(eP,Pn);}
    return m2_proj(m2_mul(eP,U));
}

/* ---- Plaquettes and staples ---- */
static M3 m3_staple(int s,int mu){M3 st=m3_zero();for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st=m3_add(st,m3_add(m3_mul(U3[smu*DIM+nu],m3_mul(m3_dag(U3[snu*DIM+mu]),m3_dag(U3[s*DIM+nu]))),m3_mul(m3_dag(U3[smnu_mu*DIM+nu]),m3_mul(m3_dag(U3[smnu*DIM+mu]),U3[smnu*DIM+nu]))));}return st;}
static M2 m2_staple(int s,int mu){M2 st=m2_zero();for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st=m2_add(st,m2_add(m2_mul(U2[smu*DIM+nu],m2_mul(m2_dag(U2[snu*DIM+mu]),m2_dag(U2[s*DIM+nu]))),m2_mul(m2_dag(U2[smnu_mu*DIM+nu]),m2_mul(m2_dag(U2[smnu*DIM+mu]),U2[smnu*DIM+nu]))));}return st;}
static double u1_staple_re(int s,int mu){double st=0;for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st+=cos(U1[smu*DIM+nu]-U1[snu*DIM+mu]-U1[s*DIM+nu]);st+=cos(-U1[smnu_mu*DIM+nu]-U1[smnu*DIM+mu]+U1[smnu*DIM+nu]);}return st;}
static double u1_staple_im(int s,int mu){double st=0;for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st+=sin(U1[smu*DIM+nu]-U1[snu*DIM+mu]-U1[s*DIM+nu]);st+=sin(-U1[smnu_mu*DIM+nu]-U1[smnu*DIM+mu]+U1[smnu*DIM+nu]);}return st;}

static void plaquettes(double *p3,double *p2,double *p1){
    double s3=0,s2=0,s1=0;int n=0;
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++)for(int nu=mu+1;nu<DIM;nu++){
        int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1);
        s3+=m3_retr(m3_mul(m3_mul(U3[s*DIM+mu],U3[smu*DIM+nu]),m3_mul(m3_dag(U3[snu*DIM+mu]),m3_dag(U3[s*DIM+nu]))))/NC3;
        s2+=m2_retr(m2_mul(m2_mul(U2[s*DIM+mu],U2[smu*DIM+nu]),m2_mul(m2_dag(U2[snu*DIM+mu]),m2_dag(U2[s*DIM+nu]))))/NC2;
        double tp=U1[s*DIM+mu]+U1[smu*DIM+nu]-U1[snu*DIM+mu]-U1[s*DIM+nu];
        s1+=cos(tp);n++;
    }
    *p3=s3/n;*p2=s2/n;*p1=s1/n;
}

/* ---- Gauge action S_g = -β Σ Re Tr(plaq) - h² Σ gauge-Higgs coupling ---- */
static double gauge_action(double b3,double b2,double b1,double higgs_h){
    double S=0;
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++)for(int nu=mu+1;nu<DIM;nu++){
        int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1);
        S-=(b3/NC3)*m3_retr(m3_mul(m3_mul(U3[s*DIM+mu],U3[smu*DIM+nu]),m3_mul(m3_dag(U3[snu*DIM+mu]),m3_dag(U3[s*DIM+nu]))));
        S-=(b2/NC2)*m2_retr(m2_mul(m2_mul(U2[s*DIM+mu],U2[smu*DIM+nu]),m2_mul(m2_dag(U2[snu*DIM+mu]),m2_dag(U2[s*DIM+nu]))));
        double tp=U1[s*DIM+mu]+U1[smu*DIM+nu]-U1[snu*DIM+mu]-U1[s*DIM+nu];
        S-=b1*cos(tp);
    }
    /* Gauge-Higgs coupling: Higgs doublet Φ=(0,h) in unitary gauge */
    /* SU(2): -h² Σ Re[U₂(x,μ)]₂₂  (selects σ₃ direction) */
    /* U(1):  -h² Σ cos(θ₁/2)       (hypercharge Y=1/2) */
    if(higgs_h>0){
        double h2=higgs_h*higgs_h;
        for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
            S-=h2*U2[s*DIM+mu].e[1][1].re;
            S-=h2*cos(0.5*U1[s*DIM+mu]);
        }
    }
    return S;
}

/* ---- Gauge force: dS_g/dU projected to algebra ---- */
/* For SU(N): F = (β/N) * ta(U * staple†) = (β/N) * [U*V† - V*U†]/(2i) traceless */
/* Convention: P' = P + dt * F, where F = -dS/dU (note sign) */
static void compute_gauge_force(M3 *frc3,M2 *frc2,double *frc1,double b3,double b2,double b1,double higgs_h){
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
        int idx=s*DIM+mu;
        /* SU(3): F = (β₃/N_c) * ta(U * staple†) */
        M3 UV3=m3_mul(U3[idx],m3_staple(s,mu));
        frc3[idx]=m3_scl(m3_ta(UV3),-b3/NC3);
        /* SU(2) */
        M2 UV2=m2_mul(U2[idx],m2_staple(s,mu));
        frc2[idx]=m2_scl(m2_ta(UV2),-b2/NC2);
        /* U(1) */
        double th=U1[idx];
        double sre=u1_staple_re(s,mu), sim=u1_staple_im(s,mu);
        frc1[idx]=-b1*(sin(th)*sre + cos(th)*sim); /* F = -dS/dθ */

        /* Gauge-Higgs force from S_GH = -h² Re[U₂]₂₂ - h² cos(θ₁/2) */
        if(higgs_h>0){
            double h2=higgs_h*higgs_h;
            /* SU(2): -dS_GH/dU₂ projected to algebra */
            /* S_GH = -h² Re[U₂]₂₂. For U=exp(iεT)U₀: */
            /* d Re[U₂₂]/dε = Im Σ_j [T]₂ⱼ [U]ⱼ₂ */
            /* Use ta projection: W = diag(0,1), F_GH = h² ta(U×W) */
            M2 W;memset(&W,0,sizeof(W));W.e[1][1]=cx(1,0);
            M2 UW=m2_mul(U2[idx],W);
            frc2[idx]=m2_add(frc2[idx],m2_scl(m2_ta(UW),-h2));
            /* U(1): S_GH = -h² cos(θ/2), F = -dS/dθ = -h²(1/2)sin(θ/2) */
            frc1[idx]+=-h2*0.5*sin(0.5*U1[idx]);
        }
    }
}

/* ---- Dirac operator ---- */
static void apply_D(Cx *dst,Cx *src,double mass){
    for(int s=0;s<VOL;s++){
        for(int a=0;a<NK;a++) dst[s*NK+a]=cxscl(src[s*NK+a],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=stag_eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int a=0;a<NK;a++){
                Cx fwd=cx(0,0),bwd=cx(0,0);
                if(a<NC3){
                    for(int b=0;b<NC3;b++)fwd=cxadd(fwd,cxmul(U3[s*DIM+mu].e[a][b],src[sp*NK+b]));
                    for(int b=0;b<NC3;b++)bwd=cxadd(bwd,cxmul(cxconj(U3[sm*DIM+mu].e[b][a]),src[sm*NK+b]));
                }else if(a<NC3+NC2){
                    int a2=a-NC3;
                    for(int b=0;b<NC2;b++)fwd=cxadd(fwd,cxmul(U2[s*DIM+mu].e[a2][b],src[sp*NK+NC3+b]));
                    for(int b=0;b<NC2;b++)bwd=cxadd(bwd,cxmul(cxconj(U2[sm*DIM+mu].e[b][a2]),src[sm*NK+NC3+b]));
                }else{
                    fwd=cxmul(cx(cos(U1[s*DIM+mu]),sin(U1[s*DIM+mu])),src[sp*NK+5]);
                    bwd=cxmul(cx(cos(U1[sm*DIM+mu]),-sin(U1[sm*DIM+mu])),src[sm*NK+5]);
                }
                dst[s*NK+a]=cxadd(dst[s*NK+a],cxscl(fwd,ph));
                dst[s*NK+a]=cxsub(dst[s*NK+a],cxscl(bwd,ph));
            }
        }
    }
}

static void apply_DdD(Cx *dst,Cx *src,double mass){
    int N=VOL*NK;Cx *tmp=malloc(N*sizeof(Cx));apply_D(tmp,src,mass);
    /* D†: same as D but with -eta (staggered D is anti-hermitian + mass) */
    for(int s=0;s<VOL;s++){
        for(int a=0;a<NK;a++) dst[s*NK+a]=cxscl(tmp[s*NK+a],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=-stag_eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int a=0;a<NK;a++){
                Cx fwd=cx(0,0),bwd=cx(0,0);
                if(a<NC3){
                    for(int b=0;b<NC3;b++)fwd=cxadd(fwd,cxmul(U3[s*DIM+mu].e[a][b],tmp[sp*NK+b]));
                    for(int b=0;b<NC3;b++)bwd=cxadd(bwd,cxmul(cxconj(U3[sm*DIM+mu].e[b][a]),tmp[sm*NK+b]));
                }else if(a<NC3+NC2){
                    int a2=a-NC3;
                    for(int b=0;b<NC2;b++)fwd=cxadd(fwd,cxmul(U2[s*DIM+mu].e[a2][b],tmp[sp*NK+NC3+b]));
                    for(int b=0;b<NC2;b++)bwd=cxadd(bwd,cxmul(cxconj(U2[sm*DIM+mu].e[b][a2]),tmp[sm*NK+NC3+b]));
                }else{
                    fwd=cxmul(cx(cos(U1[s*DIM+mu]),sin(U1[s*DIM+mu])),tmp[sp*NK+5]);
                    bwd=cxmul(cx(cos(U1[sm*DIM+mu]),-sin(U1[sm*DIM+mu])),tmp[sm*NK+5]);
                }
                dst[s*NK+a]=cxadd(dst[s*NK+a],cxscl(fwd,ph));
                dst[s*NK+a]=cxsub(dst[s*NK+a],cxscl(bwd,ph));
            }
        }
    }
    free(tmp);
}

static int cg_solve(Cx *x,Cx *b,double mass){
    int N=VOL*NK;Cx *r=malloc(N*sizeof(Cx)),*p=malloc(N*sizeof(Cx)),*Ap=malloc(N*sizeof(Cx));
    memset(x,0,N*sizeof(Cx));memcpy(r,b,N*sizeof(Cx));memcpy(p,b,N*sizeof(Cx));
    double rr=0;for(int i=0;i<N;i++)rr+=cxabs2(r[i]);
    double rr0=rr;if(rr0<1e-30){free(r);free(p);free(Ap);return 0;}
    int it;for(it=0;it<CG_MAX;it++){
        apply_DdD(Ap,p,mass);double pAp=0;
        for(int i=0;i<N;i++)pAp+=Ap[i].re*p[i].re+Ap[i].im*p[i].im;
        if(fabs(pAp)<1e-30)break;double alpha=rr/pAp;
        for(int i=0;i<N;i++){x[i]=cxadd(x[i],cxscl(p[i],alpha));r[i]=cxsub(r[i],cxscl(Ap[i],alpha));}
        double rr_new=0;for(int i=0;i<N;i++)rr_new+=cxabs2(r[i]);
        if(rr_new/rr0<CG_TOL*CG_TOL){it++;break;}
        for(int i=0;i<N;i++)p[i]=cxadd(r[i],cxscl(p[i],rr_new/rr));
        rr=rr_new;
    }
    free(r);free(p);free(Ap);return it;
}

/* ---- Fermion force ---- */
/* S_f = phi† (D†D)^{-1} phi = chi† D†D chi where chi=(D†D)^{-1}phi */
/* dS_f/dU_{mu}(s)_{ab} involves the outer product of chi and D*chi */
/* For staggered: the force on link U_{mu}(s) in the SU(N) sector is: */
/*   F_{ab} = -eta(s,mu)/2 * [chi(s,a)^* * (D*chi)(s+mu,b) - (D*chi)(s,a)^* * chi(s+mu,b)] */
/* Projected to the algebra: f = ta(U * Outer†) */
static void compute_fermion_force(M3 *frc3,M2 *frc2,double *frc1,double mass){
    int N=VOL*NK;
    /* chi = (D†D)^{-1} phi is already computed */
    /* Compute Y = D_hop chi (hopping only, no mass term) */
    Cx *Y=malloc(N*sizeof(Cx));
    apply_D(Y,chi,0.0); /* mass=0 gives D_hop */

    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
        int idx=s*DIM+mu;
        int sp=nbr(s,mu,+1);
        double ph=-stag_eta(s,mu)*0.5; /* NOTE: -eta/2 for the force sign */

        /* SU(3): F_{ab} = -(eta/2)*[chi_a* P_b + Q_a* Y_b - Y_a* Q_b - P_a* chi_b] */
        /* P = U*Y(s+mu), Q = U*chi(s+mu) */
        {Cx P[NC3],Q[NC3];
        for(int a=0;a<NC3;a++){P[a]=cx(0,0);Q[a]=cx(0,0);
            for(int c=0;c<NC3;c++){
                P[a]=cxadd(P[a],cxmul(U3[idx].e[a][c],Y[sp*NK+c]));
                Q[a]=cxadd(Q[a],cxmul(U3[idx].e[a][c],chi[sp*NK+c]));
            }}
        M3 F;
        for(int a=0;a<NC3;a++)for(int b=0;b<NC3;b++)
            F.e[a][b]=cxscl(cxadd(cxadd(cxmul(cxconj(chi[s*NK+a]),P[b]),
                                        cxmul(cxconj(Q[a]),Y[s*NK+b])),
                            cxadd(cxscl(cxmul(cxconj(Y[s*NK+a]),Q[b]),-1),
                                  cxscl(cxmul(cxconj(P[a]),chi[s*NK+b]),-1))),ph);
        frc3[idx]=m3_add(frc3[idx],m3_ta(F));}

        /* SU(2): same formula with SU(2) gauge transport */
        {Cx P2[NC2],Q2[NC2];
        for(int a=0;a<NC2;a++){P2[a]=cx(0,0);Q2[a]=cx(0,0);
            for(int c=0;c<NC2;c++){
                P2[a]=cxadd(P2[a],cxmul(U2[idx].e[a][c],Y[sp*NK+NC3+c]));
                Q2[a]=cxadd(Q2[a],cxmul(U2[idx].e[a][c],chi[sp*NK+NC3+c]));
            }}
        M2 F;
        for(int a=0;a<NC2;a++)for(int b=0;b<NC2;b++)
            F.e[a][b]=cxscl(cxadd(cxadd(cxmul(cxconj(chi[s*NK+NC3+a]),P2[b]),
                                        cxmul(cxconj(Q2[a]),Y[s*NK+NC3+b])),
                            cxadd(cxscl(cxmul(cxconj(Y[s*NK+NC3+a]),Q2[b]),-1),
                                  cxscl(cxmul(cxconj(P2[a]),chi[s*NK+NC3+b]),-1))),ph);
        frc2[idx]=m2_add(frc2[idx],m2_ta(F));}

        /* U(1): scalar version */
        {Cx Pu=cxmul(cx(cos(U1[idx]),sin(U1[idx])),Y[sp*NK+5]);
        Cx Qu=cxmul(cx(cos(U1[idx]),sin(U1[idx])),chi[sp*NK+5]);
        /* F = -(eta/2)*[chi* P + Q* Y - Y* Q - P* chi] (scalar) */
        Cx Fval=cxscl(cxadd(cxadd(cxmul(cxconj(chi[s*NK+5]),Pu),
                                   cxmul(cxconj(Qu),Y[s*NK+5])),
                      cxadd(cxscl(cxmul(cxconj(Y[s*NK+5]),Qu),-1),
                            cxscl(cxmul(cxconj(Pu),chi[s*NK+5]),-1))),ph);
        /* For U(1), the force on theta is the imaginary part */
        frc1[idx]+=Fval.im;}
    }
    free(Y);
}

/* ---- Kinetic energy ---- */
static double kinetic_energy(void){
    double T=0;
    for(int i=0;i<VOL*DIM;i++){
        /* SU(3): -Tr(P²) for anti-hermitian P */
        for(int a=0;a<NC3;a++)for(int b=0;b<NC3;b++)T+=cxabs2(P3[i].e[a][b]);
        /* SU(2) */
        for(int a=0;a<NC2;a++)for(int b=0;b<NC2;b++)T+=cxabs2(P2[i].e[a][b]);
        /* U(1) */
        T+=P1[i]*P1[i];
    }
    return 0.5*T;
}

/* ---- Fermion action: S_f = phi† chi where chi=(D†D)^{-1}phi ---- */
static double fermion_action(double mass){
    int N=VOL*NK;
    cg_solve(chi,phi,mass);
    double S=0;
    for(int i=0;i<N;i++) S+=phi[i].re*chi[i].re+phi[i].im*chi[i].im;
    return S;
}

/* ---- Refresh pseudofermion: phi = D† * eta, eta ~ N(0,1) ---- */
static void refresh_pseudofermion(double mass){
    int N=VOL*NK;
    Cx *eta_vec=malloc(N*sizeof(Cx));
    for(int i=0;i<N;i++) eta_vec[i]=cx(gauss01()/sqrt(2.0),gauss01()/sqrt(2.0));
    /* phi = D† eta (so that phi† (D†D)^{-1} phi = eta† D (D†D)^{-1} D† eta = eta†eta) */
    /* D† = m - D_hop (staggered anti-hermiticity: D_hop† = -D_hop) */
    apply_D(phi,eta_vec,mass); /* This gives D*eta */
    /* Actually we want D†*eta. For staggered, D† has -eta phases */
    /* Let's just apply D† directly */
    for(int s=0;s<VOL;s++){
        for(int a=0;a<NK;a++) phi[s*NK+a]=cxscl(eta_vec[s*NK+a],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=-stag_eta(s,mu)*0.5; /* NOTE: negative for D† */
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int a=0;a<NK;a++){
                Cx fwd=cx(0,0),bwd=cx(0,0);
                if(a<NC3){
                    for(int b=0;b<NC3;b++)fwd=cxadd(fwd,cxmul(U3[s*DIM+mu].e[a][b],eta_vec[sp*NK+b]));
                    for(int b=0;b<NC3;b++)bwd=cxadd(bwd,cxmul(cxconj(U3[sm*DIM+mu].e[b][a]),eta_vec[sm*NK+b]));
                }else if(a<NC3+NC2){
                    int a2=a-NC3;
                    for(int b=0;b<NC2;b++)fwd=cxadd(fwd,cxmul(U2[s*DIM+mu].e[a2][b],eta_vec[sp*NK+NC3+b]));
                    for(int b=0;b<NC2;b++)bwd=cxadd(bwd,cxmul(cxconj(U2[sm*DIM+mu].e[b][a2]),eta_vec[sm*NK+NC3+b]));
                }else{
                    fwd=cxmul(cx(cos(U1[s*DIM+mu]),sin(U1[s*DIM+mu])),eta_vec[sp*NK+5]);
                    bwd=cxmul(cx(cos(U1[sm*DIM+mu]),-sin(U1[sm*DIM+mu])),eta_vec[sm*NK+5]);
                }
                phi[s*NK+a]=cxadd(phi[s*NK+a],cxscl(fwd,ph));
                phi[s*NK+a]=cxsub(phi[s*NK+a],cxscl(bwd,ph));
            }
        }
    }
    free(eta_vec);
}

/* ---- Compute total force (gauge + fermion) ---- */
static void compute_force(M3 *frc3,M2 *frc2,double *frc1,double meff,double b3,double b2,double b1,double higgs_h){
    /* Zero force arrays */
    memset(frc3,0,VOL*DIM*sizeof(M3));
    memset(frc2,0,VOL*DIM*sizeof(M2));
    memset(frc1,0,VOL*DIM*sizeof(double));
    /* Gauge force (includes gauge-Higgs coupling) */
    compute_gauge_force(frc3,frc2,frc1,b3,b2,b1,higgs_h);
    /* Fermion force (chi must be current) — uses effective mass */
    cg_solve(chi,phi,meff);
    compute_fermion_force(frc3,frc2,frc1,meff);
}

/* ---- HMC trajectory ---- */
static double do_hmc(double mass,double b3,double b2,double b1,double higgs_h,int nstep,double tau,int *acc){
    double dt=tau/nstep;
    double meff=mass+higgs_h; /* Effective fermion mass: bare + Higgs background */

    /* Save config */
    memcpy(U3_bak,U3,VOL*DIM*sizeof(M3));
    memcpy(U2_bak,U2,VOL*DIM*sizeof(M2));
    memcpy(U1_bak,U1,VOL*DIM*sizeof(double));

    /* Refresh momenta */
    for(int i=0;i<VOL*DIM;i++){
        for(int a=0;a<NC3;a++)for(int b=a;b<NC3;b++){
            if(a==b)P3[i].e[a][b]=cx(0,gauss01());
            else{double r=gauss01()/sqrt(2),im=gauss01()/sqrt(2);P3[i].e[a][b]=cx(im,r);P3[i].e[b][a]=cx(-im,r);}
        }
        double tr=0;for(int a=0;a<NC3;a++)tr+=P3[i].e[a][a].im;tr/=NC3;
        for(int a=0;a<NC3;a++)P3[i].e[a][a].im-=tr;
        double a1=gauss01(),a2=gauss01(),a3=gauss01();
        P2[i].e[0][0]=cx(0,a3);P2[i].e[0][1]=cx(a2,a1);P2[i].e[1][0]=cx(-a2,a1);P2[i].e[1][1]=cx(0,-a3);
        P1[i]=gauss01();
    }

    /* Refresh pseudofermion */
    refresh_pseudofermion(meff);

    /* Initial H */
    double H0=kinetic_energy()+gauge_action(b3,b2,b1,higgs_h)+fermion_action(meff);

    /* Force arrays */
    M3 *frc3=malloc(VOL*DIM*sizeof(M3));
    M2 *frc2=malloc(VOL*DIM*sizeof(M2));
    double *frc1=calloc(VOL*DIM,sizeof(double));

    /* Leapfrog: half step P */
    compute_force(frc3,frc2,frc1,meff,b3,b2,b1,higgs_h);
    for(int i=0;i<VOL*DIM;i++){
        P3[i]=m3_add(P3[i],m3_scl(frc3[i],dt*0.5));
        P2[i]=m2_add(P2[i],m2_scl(frc2[i],dt*0.5));
        P1[i]+=frc1[i]*dt*0.5;
    }

    for(int step=0;step<nstep;step++){
        /* Full step U */
        for(int i=0;i<VOL*DIM;i++){
            U3[i]=m3_evolve(U3[i],P3[i],dt);
            U2[i]=m2_evolve(U2[i],P2[i],dt);
            U1[i]+=P1[i]*dt;
        }
        /* Full/half step P */
        double fdt=(step<nstep-1)?dt:dt*0.5;
        compute_force(frc3,frc2,frc1,meff,b3,b2,b1,higgs_h);
        for(int i=0;i<VOL*DIM;i++){
            P3[i]=m3_add(P3[i],m3_scl(frc3[i],fdt));
            P2[i]=m2_add(P2[i],m2_scl(frc2[i],fdt));
            P1[i]+=frc1[i]*fdt;
        }
    }

    free(frc3);free(frc2);free(frc1);

    /* Final H */
    double H1=kinetic_energy()+gauge_action(b3,b2,b1,higgs_h)+fermion_action(meff);
    double dH=H1-H0;

    *acc=(dH<0||drand01()<exp(-dH))?1:0;
    if(!*acc){
        memcpy(U3,U3_bak,VOL*DIM*sizeof(M3));
        memcpy(U2,U2_bak,VOL*DIM*sizeof(M2));
        memcpy(U1,U1_bak,VOL*DIM*sizeof(double));
    }
    return dH;
}

/* ---- Measure condensate (total and sector-resolved) ---- */
static void measure_pbp_sectors(double mass,double *pbp_tot,double *pbp_su3,double *pbp_su2,double *pbp_u1){
    int N=VOL*NK;
    Cx *ev=malloc(N*sizeof(Cx)),*x=malloc(N*sizeof(Cx));
    double tot=0,s3=0,s2=0,s1=0;int Nhit=4;
    for(int hit=0;hit<Nhit;hit++){
        for(int i=0;i<N;i++) ev[i]=cx((drand01()<0.5)?1.0:-1.0,0.0);
        cg_solve(x,ev,mass);
        for(int s=0;s<VOL;s++){
            for(int a=0;a<NC3;a++){int i=s*NK+a;double d=ev[i].re*x[i].re+ev[i].im*x[i].im;s3+=d;tot+=d;}
            for(int a=0;a<NC2;a++){int i=s*NK+NC3+a;double d=ev[i].re*x[i].re+ev[i].im*x[i].im;s2+=d;tot+=d;}
            {int i=s*NK+5;double d=ev[i].re*x[i].re+ev[i].im*x[i].im;s1+=d;tot+=d;}
        }
    }
    free(ev);free(x);
    *pbp_tot=mass*tot/(VOL*Nhit);
    *pbp_su3=mass*s3/(VOL*Nhit);
    *pbp_su2=mass*s2/(VOL*Nhit);
    *pbp_u1=mass*s1/(VOL*Nhit);
}

/* ---- Measure gauge-Higgs observable: Re[U₂]₂₂ average and cos(θ₁/2) ---- */
static void measure_gh(double *reU22_avg,double *costh_avg){
    double r2=0,ct=0;
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
        r2+=U2[s*DIM+mu].e[1][1].re;
        ct+=cos(0.5*U1[s*DIM+mu]);
    }
    *reU22_avg=r2/(VOL*DIM);
    *costh_avg=ct/(VOL*DIM);
}

/* ---- Compute dV/dh decomposed into fermion and gauge contributions ---- */
/* dV/dh = dV_ferm/dh + dV_GH/dh */
/* dV_ferm/dh = -2*VOL*<pbp>  (fermion determinant derivative) */
/* dV_GH/dh = -2*h*VOL*DIM*(<Re[U2]22> + <cos(θ1/2)>)  (gauge-Higgs derivative) */
static void compute_dvdh(double mass,double higgs_h,
                         double *dvdh_total,double *dvdh_ferm,double *dvdh_gauge){
    double pbp_tot,pbp3,pbp2,pbp1;
    measure_pbp_sectors(mass,&pbp_tot,&pbp3,&pbp2,&pbp1);
    double reU22,costh;
    measure_gh(&reU22,&costh);

    *dvdh_ferm=-2.0*pbp_tot; /* per unit volume */
    *dvdh_gauge=-2.0*higgs_h*DIM*(reU22+costh);
    *dvdh_total=*dvdh_ferm + *dvdh_gauge;
}

static void fmt_time(double s,char *b){int h=(int)(s/3600),m=(int)((s-h*3600)/60);int sec=(int)(s-h*3600-m*60);if(h>0)sprintf(b,"%dh%02dm%02ds",h,m,sec);else if(m>0)sprintf(b,"%dm%02ds",m,sec);else sprintf(b,"%.1fs",s);}

/* ---- Main ---- */
int main(int argc,char **argv){
    L=(argc>1)?atoi(argv[1]):6;
    double mass=(argc>2)?atof(argv[2]):0.10;
    double higgs_h=(argc>3)?atof(argv[3]):0.0;
    int Ntraj=(argc>4)?atoi(argv[4]):50;
    int Nthm=(argc>5)?atoi(argv[5]):10;
    const char *outf=(argc>6)?argv[6]:"cep_out.dat";
    int nstep=1; double tau=0.008;
    VOL=L*L*L;
    double b3=11.1,b2=7.4,b1=3.7;
    rng_seed=(unsigned int)time(NULL);
    time_t T0=time(NULL);char tb[64];

    /* Allocate */
    U3=malloc(VOL*DIM*sizeof(M3));U3_bak=malloc(VOL*DIM*sizeof(M3));
    U2=malloc(VOL*DIM*sizeof(M2));U2_bak=malloc(VOL*DIM*sizeof(M2));
    U1=calloc(VOL*DIM,sizeof(double));U1_bak=malloc(VOL*DIM*sizeof(double));
    P3=calloc(VOL*DIM,sizeof(M3));P2=calloc(VOL*DIM,sizeof(M2));P1=calloc(VOL*DIM,sizeof(double));
    phi=calloc(VOL*NK,sizeof(Cx));chi=calloc(VOL*NK,sizeof(Cx));
    for(int i=0;i<VOL*DIM;i++){U3[i]=m3_unit();U2[i]=m2_unit();}

    fprintf(stderr,"\n  k6_cep: K=6 Constraint Effective Potential\n");
    fprintf(stderr,"  L=%d mass=%.4f h=%.4f β=(%.1f,%.1f,%.1f) nstep=%d τ=%.3f\n\n",
            L,mass,higgs_h,b3,b2,b1,nstep,tau);

    /* Pre-thermalize with Metropolis */
    fprintf(stderr,"  Pre-thermalizing (Metropolis)...\n");
    double eps=0.3;
    for(int sw=0;sw<200;sw++){
        for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
            {double So=-(b3/NC3)*m3_retr(m3_mul(U3[s*DIM+mu],m3_staple(s,mu)));M3 h;for(int i=0;i<NC3;i++)for(int j=i;j<NC3;j++){if(i==j)h.e[i][j]=cx(gauss01()*eps,0);else{double r1=gauss01()*eps,r2=gauss01()*eps;h.e[i][j]=cx(r1,r2);h.e[j][i]=cx(r1,-r2);}}double tr=0;for(int i=0;i<NC3;i++)tr+=h.e[i][i].re;tr/=NC3;for(int i=0;i<NC3;i++)h.e[i][i].re-=tr;M3 u=m3_unit();for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)u.e[i][j]=cxadd(u.e[i][j],cx(-h.e[i][j].im,h.e[i][j].re));M3 Uo=U3[s*DIM+mu];U3[s*DIM+mu]=m3_proj(m3_mul(u,Uo));double Sn=-(b3/NC3)*m3_retr(m3_mul(U3[s*DIM+mu],m3_staple(s,mu)));if(Sn-So>0&&drand01()>=exp(-(Sn-So)))U3[s*DIM+mu]=Uo;}
            {double So=-(b2/NC2)*m2_retr(m2_mul(U2[s*DIM+mu],m2_staple(s,mu)));if(higgs_h>0)So-=higgs_h*higgs_h*U2[s*DIM+mu].e[1][1].re;double a1=gauss01()*eps,a2=gauss01()*eps,a3=gauss01()*eps;M2 hh;hh.e[0][0]=cx(1,a3);hh.e[0][1]=cx(a2,a1);hh.e[1][0]=cx(-a2,a1);hh.e[1][1]=cx(1,-a3);M2 Uo=U2[s*DIM+mu];U2[s*DIM+mu]=m2_proj(m2_mul(hh,Uo));double Sn=-(b2/NC2)*m2_retr(m2_mul(U2[s*DIM+mu],m2_staple(s,mu)));if(higgs_h>0)Sn-=higgs_h*higgs_h*U2[s*DIM+mu].e[1][1].re;if(Sn-So>0&&drand01()>=exp(-(Sn-So)))U2[s*DIM+mu]=Uo;}
            {double stap_re=u1_staple_re(s,mu),stap_im=u1_staple_im(s,mu);double old=U1[s*DIM+mu];double So=-b1*(cos(old)*stap_re+sin(old)*stap_im);if(higgs_h>0)So-=higgs_h*higgs_h*cos(0.5*old);U1[s*DIM+mu]=old+eps*(2*drand01()-1);double Sn=-b1*(cos(U1[s*DIM+mu])*stap_re+sin(U1[s*DIM+mu])*stap_im);if(higgs_h>0)Sn-=higgs_h*higgs_h*cos(0.5*U1[s*DIM+mu]);if(Sn-So>0&&drand01()>=exp(-(Sn-So)))U1[s*DIM+mu]=old;}
        }
    }
    double p3,p2,p1_val;plaquettes(&p3,&p2,&p1_val);
    fprintf(stderr,"  Done. P3=%.4f P2=%.4f P1=%.4f\n\n",p3,p2,p1_val);

    FILE *fp=fopen(outf,"a");
    fprintf(fp,"# k6_cep L=%d mass=%.6f higgs_h=%.6f beta=(%.1f,%.1f,%.1f)\n",L,mass,higgs_h,b3,b2,b1);
    fprintf(fp,"# traj acc dH pbp_tot pbp_su3 pbp_su2 pbp_u1 reU22 costh dvdh_f dvdh_g dvdh_tot P3 P2 P1\n");
    fflush(fp);

    /* HMC with sector-resolved measurements */
    int total_acc=0,nmeas=0;
    double sum_dvdh=0,sum_dvdh2=0;
    double sum_pbp=0,sum_pbp2=0;

    for(int t=0;t<Ntraj+Nthm;t++){
        int acc;
        double dH=do_hmc(mass,b3,b2,b1,higgs_h,nstep,tau,&acc);
        total_acc+=acc;
        plaquettes(&p3,&p2,&p1_val);

        if(t>=Nthm){
            double pbp_tot,pbp3,pbp2v,pbp1v;
            measure_pbp_sectors(mass+higgs_h,&pbp_tot,&pbp3,&pbp2v,&pbp1v);
            double reU22,costh;
            measure_gh(&reU22,&costh);
            double dvf,dvg,dvt;
            compute_dvdh(mass+higgs_h,higgs_h,&dvt,&dvf,&dvg);

            sum_pbp+=pbp_tot;sum_pbp2+=pbp_tot*pbp_tot;
            sum_dvdh+=dvt;sum_dvdh2+=dvt*dvt;
            nmeas++;

            fprintf(fp,"%5d %d %+10.4f  %.6f %.6f %.6f %.6f  %.6f %.6f  %+.6f %+.6f %+.6f  %.4f %.4f %.4f\n",
                    t-Nthm,acc,dH,pbp_tot,pbp3,pbp2v,pbp1v,reU22,costh,dvf,dvg,dvt,p3,p2,p1_val);
            fflush(fp);
        }

        if(t%5==0||t==Ntraj+Nthm-1){
            fmt_time(difftime(time(NULL),T0),tb);
            double pm=(nmeas>0)?sum_pbp/nmeas:0;
            double dm=(nmeas>0)?sum_dvdh/nmeas:0;
            fprintf(stderr,"  traj %3d/%d [%s] %s dH=%+.3f P=(%.3f,%.3f,%.3f)",
                    t+1,Ntraj+Nthm,tb,acc?"ACC":"REJ",dH,p3,p2,p1_val);
            if(nmeas>0) fprintf(stderr," <pbp>=%.4f <dV/dh>=%+.4f",pm,dm);
            fprintf(stderr,"\n");
        }
    }

    double pm=sum_pbp/nmeas,pe=sqrt(fabs(sum_pbp2/nmeas-pm*pm)/fmax(nmeas-1,1));
    double dm=sum_dvdh/nmeas,de=sqrt(fabs(sum_dvdh2/nmeas-dm*dm)/fmax(nmeas-1,1));
    fmt_time(difftime(time(NULL),T0),tb);
    fprintf(stderr,"\n  DONE (%s). acc=%d%% <pbp>=%.6f±%.6f <dV/dh>=%+.6f±%.6f\n\n",
            tb,(100*total_acc)/(Ntraj+Nthm),pm,pe,dm,de);
    fprintf(fp,"# RESULT: mass=%.6f h=%.6f <pbp>=%.6f±%.6f <dV/dh>=%+.6f±%.6f acc=%d%%\n",
            mass,higgs_h,pm,pe,dm,de,(100*total_acc)/(Ntraj+Nthm));
    fclose(fp);

    free(U3);free(U3_bak);free(U2);free(U2_bak);free(U1);free(U1_bak);
    free(P3);free(P2);free(P1);free(phi);free(chi);
    return 0;
}
