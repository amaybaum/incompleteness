/*
 * k6_higgs.c — K=6 HMC with dynamical SU(2) doublet Higgs field
 *
 * The hierarchy problem: what determines v/M_Pl?
 *
 * This code promotes the Higgs from a background field to a dynamical
 * lattice variable Φ(x) = (φ₁, φ₂) — an SU(2) doublet with Y=1/2.
 * The full action is:
 *
 *   S = S_gauge + S_fermion + S_Higgs
 *
 * where S_Higgs = Σ_x { Φ†Φ + λ(Φ†Φ-1)²
 *                       - κ Σ_μ [Φ†(x) W(x,μ) Φ(x+μ) + h.c.] }
 *
 * with W(x,μ) = exp(iθ₁/2) × U₂(x,μ) — combined SU(2)×U(1) transport.
 *
 * The fermion mass is local Yukawa: m(x) = m₀ + y × |Φ(x)|
 *
 * OI-predicted parameters:
 *   λ ≈ 0      (λ(M_Pl) = 0 from composite A₁ taste)
 *   y = 0.122  (m_match = λ_Cab × g₀²)
 *   κ: scan to find the critical κ_c (phase transition → VEV)
 *
 * The VEV ⟨|Φ|⟩ determines v/M_Pl.
 *
 * Compile: gcc -O3 -fopenmp -o k6_higgs k6_higgs.c -lm
 * Usage:   ./k6_higgs [L] [m0] [kappa] [lambda] [yukawa] [Ntraj] [Nthm] [outfile]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define DIM 3
#define NK 6
#define NC3 3
#define NC2 2
#define NH 2        /* Higgs doublet: 2 complex components */
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
/* Gauge fields */
static M3 *U3, *U3_bak;
static M2 *U2, *U2_bak;
static double *U1, *U1_bak;
/* Gauge momenta */
static M3 *P3; static M2 *P2; static double *P1;
/* Higgs field: NH complex components per site */
static Cx *Phi, *Phi_bak;
/* Higgs momenta: NH complex components per site (4 real DOF) */
static Cx *Pi_h;
/* Pseudofermion and CG solution */
static Cx *phi_pf, *chi_pf;

static int site(int x,int y,int z){return((x%L+L)%L)*L*L+((y%L+L)%L)*L+((z%L+L)%L);}
static int nbr(int s,int mu,int dir){int c[3]={s/(L*L),(s/L)%L,s%L};c[mu]+=dir;return site(c[0],c[1],c[2]);}
static double stag_eta(int s,int mu){int c[3]={s/(L*L),(s/L)%L,s%L};int ph=0;for(int i=0;i<mu;i++)ph+=c[i];return(ph%2==0)?1.0:-1.0;}

/* Higgs modulus at site s */
static double phi_mod(int s){
    double r2=0;
    for(int a=0;a<NH;a++) r2+=cxabs2(Phi[s*NH+a]);
    return sqrt(r2);
}
static double phi_mod2(int s){
    double r2=0;
    for(int a=0;a<NH;a++) r2+=cxabs2(Phi[s*NH+a]);
    return r2;
}

/* ---- SU(3) operations ---- */
static M3 m3_unit(void){M3 m;memset(&m,0,sizeof(m));for(int i=0;i<NC3;i++)m.e[i][i]=cx(1,0);return m;}
static M3 m3_zero(void){M3 m;memset(&m,0,sizeof(m));return m;}
static M3 m3_mul(M3 a,M3 b){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC3;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static M3 m3_dag(M3 a){M3 b;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static M3 m3_add(M3 a,M3 b){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static M3 m3_scl(M3 a,double s){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)c.e[i][j]=cxscl(a.e[i][j],s);return c;}
static double m3_retr(M3 a){double t=0;for(int i=0;i<NC3;i++)t+=a.e[i][i].re;return t;}
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
static M3 m3_ta(M3 a){
    M3 r;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)
        r.e[i][j]=cxscl(cxsub(a.e[i][j],cxconj(a.e[j][i])),0.5);
    Cx tr=cx(0,0);for(int i=0;i<NC3;i++)tr=cxadd(tr,r.e[i][i]);
    for(int i=0;i<NC3;i++)r.e[i][i]=cxsub(r.e[i][i],cxscl(tr,1.0/NC3));
    return r;
}
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

/* ---- Combined SU(2)×U(1) transport W(x,μ) = exp(iθ₁/2) U₂(x,μ) ---- */
/* Apply W(x,μ) to a doublet vector v: result_a = exp(iθ₁/2) Σ_b U₂_{ab} v_b */
static void apply_W(Cx *dst, int s, int mu, Cx *src_sp){
    int idx=s*DIM+mu;
    Cx phase=cx(cos(0.5*U1[idx]),sin(0.5*U1[idx]));
    for(int a=0;a<NC2;a++){
        Cx tmp=cx(0,0);
        for(int b=0;b<NC2;b++) tmp=cxadd(tmp,cxmul(U2[idx].e[a][b],src_sp[b]));
        dst[a]=cxmul(phase,tmp);
    }
}
/* Apply W†(x,μ) to a doublet vector: result_a = exp(-iθ₁/2) Σ_b U₂†_{ab} v_b */
static void apply_Wdag(Cx *dst, int s, int mu, Cx *src_sm){
    int idx=s*DIM+mu;
    Cx phase=cx(cos(0.5*U1[idx]),-sin(0.5*U1[idx]));
    for(int a=0;a<NC2;a++){
        Cx tmp=cx(0,0);
        for(int b=0;b<NC2;b++) tmp=cxadd(tmp,cxmul(cxconj(U2[idx].e[b][a]),src_sm[b]));
        dst[a]=cxmul(phase,tmp);
    }
}

/* ---- Higgs action ---- */
/* S_H = Σ_x { Φ†Φ + λ(Φ†Φ-1)² - κ Σ_μ [Φ†(x) W(x,μ) Φ(x+μ) + h.c.] } */
static double higgs_action(double kappa, double lambda){
    double S=0;
    for(int s=0;s<VOL;s++){
        double r2=phi_mod2(s);
        S += r2 + lambda*(r2-1.0)*(r2-1.0);
        for(int mu=0;mu<DIM;mu++){
            int sp=nbr(s,mu,+1);
            Cx Wphi[NH];
            apply_W(Wphi, s, mu, &Phi[sp*NH]);
            double hop=0;
            for(int a=0;a<NH;a++) hop+=cxmul(cxconj(Phi[s*NH+a]),Wphi[a]).re;
            S -= 2.0*kappa*hop;
        }
    }
    return S;
}

/* ---- Gauge action ---- */
static double gauge_action(double b3,double b2,double b1){
    double S=0;
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++)for(int nu=mu+1;nu<DIM;nu++){
        int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1);
        S-=(b3/NC3)*m3_retr(m3_mul(m3_mul(U3[s*DIM+mu],U3[smu*DIM+nu]),m3_mul(m3_dag(U3[snu*DIM+mu]),m3_dag(U3[s*DIM+nu]))));
        S-=(b2/NC2)*m2_retr(m2_mul(m2_mul(U2[s*DIM+mu],U2[smu*DIM+nu]),m2_mul(m2_dag(U2[snu*DIM+mu]),m2_dag(U2[s*DIM+nu]))));
        double tp=U1[s*DIM+mu]+U1[smu*DIM+nu]-U1[snu*DIM+mu]-U1[s*DIM+nu];
        S-=b1*cos(tp);
    }
    return S;
}

/* ---- Dirac operator with local Yukawa mass ---- */
static void apply_D(Cx *dst, Cx *src, double m0, double yukawa){
    for(int s=0;s<VOL;s++){
        double meff = m0 + yukawa * phi_mod(s);
        for(int a=0;a<NK;a++) dst[s*NK+a]=cxscl(src[s*NK+a],meff);
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

static void apply_DdD(Cx *dst, Cx *src, double m0, double yukawa){
    int N=VOL*NK;
    Cx *tmp=malloc(N*sizeof(Cx));
    apply_D(tmp,src,m0,yukawa);
    for(int s=0;s<VOL;s++){
        double meff = m0 + yukawa * phi_mod(s);
        for(int a=0;a<NK;a++) dst[s*NK+a]=cxscl(tmp[s*NK+a],meff);
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

static int cg_solve(Cx *x, Cx *b, double m0, double yukawa){
    int N=VOL*NK;
    Cx *r=malloc(N*sizeof(Cx)),*p=malloc(N*sizeof(Cx)),*Ap=malloc(N*sizeof(Cx));
    memset(x,0,N*sizeof(Cx));memcpy(r,b,N*sizeof(Cx));memcpy(p,b,N*sizeof(Cx));
    double rr=0;for(int i=0;i<N;i++)rr+=cxabs2(r[i]);
    double rr0=rr;if(rr0<1e-30){free(r);free(p);free(Ap);return 0;}
    int it;for(it=0;it<CG_MAX;it++){
        apply_DdD(Ap,p,m0,yukawa);
        double pAp=0;for(int i=0;i<N;i++)pAp+=Ap[i].re*p[i].re+Ap[i].im*p[i].im;
        if(fabs(pAp)<1e-30)break;
        double alpha=rr/pAp;
        for(int i=0;i<N;i++){x[i]=cxadd(x[i],cxscl(p[i],alpha));r[i]=cxsub(r[i],cxscl(Ap[i],alpha));}
        double rr_new=0;for(int i=0;i<N;i++)rr_new+=cxabs2(r[i]);
        if(rr_new/rr0<CG_TOL*CG_TOL){it++;break;}
        for(int i=0;i<N;i++)p[i]=cxadd(r[i],cxscl(p[i],rr_new/rr));
        rr=rr_new;
    }
    free(r);free(p);free(Ap);return it;
}

/* ---- Fermion force on gauge links ---- */
static void compute_fermion_force(M3 *frc3, M2 *frc2, double *frc1, double m0, double yukawa){
    int N=VOL*NK;
    Cx *Y=malloc(N*sizeof(Cx));
    apply_D(Y,chi_pf,0.0,0.0); /* hopping only */
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
        int idx=s*DIM+mu;
        int sp=nbr(s,mu,+1);
        double ph=-stag_eta(s,mu)*0.5;
        /* SU(3) */
        {Cx P[NC3],Q[NC3];
        for(int a=0;a<NC3;a++){P[a]=cx(0,0);Q[a]=cx(0,0);
            for(int c=0;c<NC3;c++){
                P[a]=cxadd(P[a],cxmul(U3[idx].e[a][c],Y[sp*NK+c]));
                Q[a]=cxadd(Q[a],cxmul(U3[idx].e[a][c],chi_pf[sp*NK+c]));
        }}
        M3 F;
        for(int a=0;a<NC3;a++)for(int b=0;b<NC3;b++)
            F.e[a][b]=cxscl(cxadd(cxadd(cxmul(cxconj(chi_pf[s*NK+a]),P[b]),
                                        cxmul(cxconj(Q[a]),Y[s*NK+b])),
                            cxadd(cxscl(cxmul(cxconj(Y[s*NK+a]),Q[b]),-1),
                                  cxscl(cxmul(cxconj(P[a]),chi_pf[s*NK+b]),-1))),ph);
        frc3[idx]=m3_add(frc3[idx],m3_ta(F));}
        /* SU(2) */
        {Cx P2v[NC2],Q2v[NC2];
        for(int a=0;a<NC2;a++){P2v[a]=cx(0,0);Q2v[a]=cx(0,0);
            for(int c=0;c<NC2;c++){
                P2v[a]=cxadd(P2v[a],cxmul(U2[idx].e[a][c],Y[sp*NK+NC3+c]));
                Q2v[a]=cxadd(Q2v[a],cxmul(U2[idx].e[a][c],chi_pf[sp*NK+NC3+c]));
        }}
        M2 F;
        for(int a=0;a<NC2;a++)for(int b=0;b<NC2;b++)
            F.e[a][b]=cxscl(cxadd(cxadd(cxmul(cxconj(chi_pf[s*NK+NC3+a]),P2v[b]),
                                        cxmul(cxconj(Q2v[a]),Y[s*NK+NC3+b])),
                            cxadd(cxscl(cxmul(cxconj(Y[s*NK+NC3+a]),Q2v[b]),-1),
                                  cxscl(cxmul(cxconj(P2v[a]),chi_pf[s*NK+NC3+b]),-1))),ph);
        frc2[idx]=m2_add(frc2[idx],m2_ta(F));}
        /* U(1) */
        {Cx Pu=cxmul(cx(cos(U1[idx]),sin(U1[idx])),Y[sp*NK+5]);
        Cx Qu=cxmul(cx(cos(U1[idx]),sin(U1[idx])),chi_pf[sp*NK+5]);
        Cx Fval=cxscl(cxadd(cxadd(cxmul(cxconj(chi_pf[s*NK+5]),Pu),
                                   cxmul(cxconj(Qu),Y[s*NK+5])),
                      cxadd(cxscl(cxmul(cxconj(Y[s*NK+5]),Qu),-1),
                            cxscl(cxmul(cxconj(Pu),chi_pf[s*NK+5]),-1))),ph);
        frc1[idx]+=Fval.im;}
    }
    free(Y);
}

/* ---- Higgs force on Φ ---- */
/* F_Φ = -dS_H/dΦ* = -[(1-2λ+2λ|Φ|²)Φ - κ Σ_μ (W Φ(x+μ) + W†(x-μ) Φ(x-μ))] */
/* Also Yukawa force from fermion action: dS_f/dΦ* */
static void compute_higgs_force(Cx *frc_h, double kappa, double lambda,
                                double m0, double yukawa){
    for(int s=0;s<VOL;s++){
        double r2=phi_mod2(s);
        double coeff=1.0-2.0*lambda+2.0*lambda*r2; /* dV/d|Φ|² × 2 */
        /* On-site force */
        for(int a=0;a<NH;a++)
            frc_h[s*NH+a]=cxscl(Phi[s*NH+a],-coeff);
        /* Hopping force */
        for(int mu=0;mu<DIM;mu++){
            int sp=nbr(s,mu,+1), sm=nbr(s,mu,-1);
            Cx Wphi_fwd[NH], Wdphi_bwd[NH];
            apply_W(Wphi_fwd, s, mu, &Phi[sp*NH]);        /* W(x,μ) Φ(x+μ) */
            apply_Wdag(Wdphi_bwd, sm, mu, &Phi[sm*NH]);   /* W†(x-μ,μ) Φ(x-μ) */
            for(int a=0;a<NH;a++){
                frc_h[s*NH+a]=cxadd(frc_h[s*NH+a],cxscl(Wphi_fwd[a],kappa));
                frc_h[s*NH+a]=cxadd(frc_h[s*NH+a],cxscl(Wdphi_bwd[a],kappa));
            }
        }
        /* Yukawa force: dS_f/d|Φ| × d|Φ|/dΦ* = y × ⟨ψ̄ψ⟩_local × Φ/2|Φ| */
        /* This is expensive (needs local condensate). Use stochastic estimator. */
        /* For now: approximate with mean-field Yukawa force */
        /* The fermion determinant's force on Φ is handled through the */
        /* site-dependent mass in the Dirac operator — the HMC integrator */
        /* automatically accounts for it through the fermion force on Φ. */
        /* Actually: the pseudofermion action S_pf = φ†(D†D)⁻¹φ depends on Φ */
        /* through m(x) = m₀ + y|Φ(x)|. The force is: */
        /* dS_pf/dΦ*_a(s) = dS_pf/dm(s) × dm/dΦ*_a(s) */
        /*                = -y × χ†(s)χ(s) × Φ_a(s)/(2|Φ(s)|) */
        if(yukawa > 0 && phi_mod(s) > 1e-10){
            double local_chichi = 0;
            for(int k=0;k<NK;k++) local_chichi += cxabs2(chi_pf[s*NK+k]);
            double pm = phi_mod(s);
            for(int a=0;a<NH;a++){
                /* F = +y × χ†χ × Φ/(2|Φ|) — positive because we want -dS/dΦ* */
                Cx yforce = cxscl(Phi[s*NH+a], yukawa * local_chichi / (2.0*pm));
                frc_h[s*NH+a] = cxadd(frc_h[s*NH+a], yforce);
            }
        }
    }
}

/* ---- Higgs force on gauge links (from hopping term) ---- */
static void compute_higgs_gauge_force(M2 *frc2, double *frc1, double kappa){
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
        int idx=s*DIM+mu;
        int sp=nbr(s,mu,+1);
        Cx phase=cx(cos(0.5*U1[idx]),sin(0.5*U1[idx]));

        /* SU(2) force: F = 2κ ta(U₂ × H) where H_{ba} = phase × Φ_b(x+μ) Φ*_a(x) */
        /* Compute Outer_{ab} = e^{iθ/2} × Φ_a(x+μ) × Φ*_b(x)  (note: NOT transposed) */
        /* Then the force term in the action is -2κ Re Tr(U₂ × Outer†) */
        /* So F_{SU2} = -(-2κ) ta(U₂ × Outer†) ... */
        /* Let me be explicit: S_hop ∋ -2κ Re[Σ_a Φ*_a(x) × e^{iθ/2} Σ_b U₂_{ab} Φ_b(x+μ)] */
        /* = -2κ Re Tr(M) where M = U₂ × R, R_{ba} = e^{iθ/2} Φ_b(x+μ) Φ*_a(x) */
        M2 R;
        for(int a=0;a<NC2;a++)for(int b=0;b<NC2;b++)
            R.e[b][a]=cxmul(phase,cxmul(Phi[sp*NH+b],cxconj(Phi[s*NH+a])));
        M2 UR=m2_mul(U2[idx],R);
        frc2[idx]=m2_add(frc2[idx],m2_scl(m2_ta(UR),2.0*kappa));

        /* U(1) force: dS_hop/dθ = -2κ × Re[(i/2) Φ†(x) W Φ(x+μ)] */
        /* = κ Im[Φ†(x) W Φ(x+μ)] */
        /* F = -dS/dθ = -κ Im[Φ†(x) W Φ(x+μ)] */
        Cx Wphi[NH];
        apply_W(Wphi,s,mu,&Phi[sp*NH]);
        double hop_val=0;
        for(int a=0;a<NH;a++) hop_val+=cxmul(cxconj(Phi[s*NH+a]),Wphi[a]).im;
        frc1[idx]+=-kappa*hop_val;
    }
}

/* ---- Kinetic energies ---- */
static double kinetic_gauge(void){
    double T=0;
    for(int i=0;i<VOL*DIM;i++){
        for(int a=0;a<NC3;a++)for(int b=0;b<NC3;b++)T+=cxabs2(P3[i].e[a][b]);
        for(int a=0;a<NC2;a++)for(int b=0;b<NC2;b++)T+=cxabs2(P2[i].e[a][b]);
        T+=P1[i]*P1[i];
    }
    return 0.5*T;
}
static double kinetic_higgs(void){
    double T=0;
    for(int i=0;i<VOL*NH;i++) T+=cxabs2(Pi_h[i]);
    return 0.5*T;
}

/* ---- Fermion action ---- */
static double fermion_action(double m0, double yukawa){
    int N=VOL*NK;
    cg_solve(chi_pf,phi_pf,m0,yukawa);
    double S=0;
    for(int i=0;i<N;i++) S+=phi_pf[i].re*chi_pf[i].re+phi_pf[i].im*chi_pf[i].im;
    return S;
}

/* ---- Refresh pseudofermion ---- */
static void refresh_pseudofermion(double m0, double yukawa){
    int N=VOL*NK;
    Cx *eta=malloc(N*sizeof(Cx));
    for(int i=0;i<N;i++) eta[i]=cx(gauss01()/sqrt(2.0),gauss01()/sqrt(2.0));
    /* phi_pf = D† eta */
    for(int s=0;s<VOL;s++){
        double meff = m0 + yukawa * phi_mod(s);
        for(int a=0;a<NK;a++) phi_pf[s*NK+a]=cxscl(eta[s*NK+a],meff);
        for(int mu=0;mu<DIM;mu++){
            double ph=-stag_eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int a=0;a<NK;a++){
                Cx fwd=cx(0,0),bwd=cx(0,0);
                if(a<NC3){
                    for(int b=0;b<NC3;b++)fwd=cxadd(fwd,cxmul(U3[s*DIM+mu].e[a][b],eta[sp*NK+b]));
                    for(int b=0;b<NC3;b++)bwd=cxadd(bwd,cxmul(cxconj(U3[sm*DIM+mu].e[b][a]),eta[sm*NK+b]));
                }else if(a<NC3+NC2){
                    int a2=a-NC3;
                    for(int b=0;b<NC2;b++)fwd=cxadd(fwd,cxmul(U2[s*DIM+mu].e[a2][b],eta[sp*NK+NC3+b]));
                    for(int b=0;b<NC2;b++)bwd=cxadd(bwd,cxmul(cxconj(U2[sm*DIM+mu].e[b][a2]),eta[sm*NK+NC3+b]));
                }else{
                    fwd=cxmul(cx(cos(U1[s*DIM+mu]),sin(U1[s*DIM+mu])),eta[sp*NK+5]);
                    bwd=cxmul(cx(cos(U1[sm*DIM+mu]),-sin(U1[sm*DIM+mu])),eta[sm*NK+5]);
                }
                phi_pf[s*NK+a]=cxadd(phi_pf[s*NK+a],cxscl(fwd,ph));
                phi_pf[s*NK+a]=cxsub(phi_pf[s*NK+a],cxscl(bwd,ph));
            }
        }
    }
    free(eta);
}

/* ---- HMC trajectory ---- */
static double do_hmc(double m0, double yukawa, double kappa, double lambda,
                     double b3, double b2, double b1, int nstep, double tau, int *acc){
    double dt=tau/nstep;

    /* Save config */
    memcpy(U3_bak,U3,VOL*DIM*sizeof(M3));
    memcpy(U2_bak,U2,VOL*DIM*sizeof(M2));
    memcpy(U1_bak,U1,VOL*DIM*sizeof(double));
    memcpy(Phi_bak,Phi,VOL*NH*sizeof(Cx));

    /* Refresh gauge momenta */
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
    /* Refresh Higgs momenta */
    for(int i=0;i<VOL*NH;i++) Pi_h[i]=cx(gauss01(),gauss01());

    /* Refresh pseudofermion */
    refresh_pseudofermion(m0,yukawa);

    /* Initial H */
    double H0=kinetic_gauge()+kinetic_higgs()+gauge_action(b3,b2,b1)
              +higgs_action(kappa,lambda)+fermion_action(m0,yukawa);

    /* Allocate force arrays */
    M3 *frc3=malloc(VOL*DIM*sizeof(M3));
    M2 *frc2=malloc(VOL*DIM*sizeof(M2));
    double *frc1=calloc(VOL*DIM,sizeof(double));
    Cx *frc_h=malloc(VOL*NH*sizeof(Cx));

    /* Leapfrog */
    for(int step=0;step<=nstep;step++){
        double fdt = (step==0||step==nstep) ? dt*0.5 : dt;

        /* Compute all forces */
        memset(frc3,0,VOL*DIM*sizeof(M3));
        memset(frc2,0,VOL*DIM*sizeof(M2));
        memset(frc1,0,VOL*DIM*sizeof(double));
        memset(frc_h,0,VOL*NH*sizeof(Cx));

        /* Gauge force (plaquette) */
        for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
            int idx=s*DIM+mu;
            M3 UV3=m3_mul(U3[idx],m3_staple(s,mu));
            frc3[idx]=m3_scl(m3_ta(UV3),-b3/NC3);
            M2 UV2=m2_mul(U2[idx],m2_staple(s,mu));
            frc2[idx]=m2_scl(m2_ta(UV2),-b2/NC2);
            double th=U1[idx];
            frc1[idx]=-b1*(sin(th)*u1_staple_re(s,mu)+cos(th)*u1_staple_im(s,mu));
        }

        /* Fermion force on gauge */
        cg_solve(chi_pf,phi_pf,m0,yukawa);
        compute_fermion_force(frc3,frc2,frc1,m0,yukawa);

        /* Higgs force on gauge (from hopping term) */
        compute_higgs_gauge_force(frc2,frc1,kappa);

        /* Higgs force on Φ */
        compute_higgs_force(frc_h,kappa,lambda,m0,yukawa);

        /* Update momenta (half/full step) */
        for(int i=0;i<VOL*DIM;i++){
            P3[i]=m3_add(P3[i],m3_scl(frc3[i],fdt));
            P2[i]=m2_add(P2[i],m2_scl(frc2[i],fdt));
            P1[i]+=frc1[i]*fdt;
        }
        /* Update Higgs momenta: factor 2 from Wirtinger derivative */
        /* For complex field: dπ/dt = -2 ∂S/∂Φ*, but frc_h = -∂S/∂Φ* */
        for(int i=0;i<VOL*NH;i++){
            Pi_h[i].re+=2.0*frc_h[i].re*fdt;
            Pi_h[i].im+=2.0*frc_h[i].im*fdt;
        }

        /* Update fields (except last step) */
        if(step<nstep){
            for(int i=0;i<VOL*DIM;i++){
                U3[i]=m3_evolve(U3[i],P3[i],dt);
                U2[i]=m2_evolve(U2[i],P2[i],dt);
                U1[i]+=P1[i]*dt;
            }
            for(int i=0;i<VOL*NH;i++){
                Phi[i].re+=Pi_h[i].re*dt;
                Phi[i].im+=Pi_h[i].im*dt;
            }
        }
    }

    free(frc3);free(frc2);free(frc1);free(frc_h);

    /* Final H */
    double H1=kinetic_gauge()+kinetic_higgs()+gauge_action(b3,b2,b1)
              +higgs_action(kappa,lambda)+fermion_action(m0,yukawa);
    double dH=H1-H0;

    *acc=(dH<0||drand01()<exp(-dH))?1:0;
    if(!*acc){
        memcpy(U3,U3_bak,VOL*DIM*sizeof(M3));
        memcpy(U2,U2_bak,VOL*DIM*sizeof(M2));
        memcpy(U1,U1_bak,VOL*DIM*sizeof(double));
        memcpy(Phi,Phi_bak,VOL*NH*sizeof(Cx));
    }
    return dH;
}

/* ---- Measurements ---- */
static double measure_phi_mod(void){
    double s=0;
    for(int x=0;x<VOL;x++) s+=phi_mod(x);
    return s/VOL;
}
static double measure_phi_mod2(void){
    double s=0;
    for(int x=0;x<VOL;x++) s+=phi_mod2(x);
    return s/VOL;
}
static double measure_pbp(double m0, double yukawa){
    int N=VOL*NK;
    Cx *ev=malloc(N*sizeof(Cx)),*x=malloc(N*sizeof(Cx));
    double pbp=0;int Nhit=4;
    for(int hit=0;hit<Nhit;hit++){
        for(int i=0;i<N;i++) ev[i]=cx((drand01()<0.5)?1.0:-1.0,0.0);
        cg_solve(x,ev,m0,yukawa);
        for(int i=0;i<N;i++) pbp+=ev[i].re*x[i].re+ev[i].im*x[i].im;
    }
    free(ev);free(x);
    double meff_avg = m0 + yukawa * measure_phi_mod();
    return meff_avg*pbp/(VOL*Nhit);
}
/* Gauge-invariant Higgs link correlator — the CORRECT order parameter */
/* ⟨hop⟩ = (1/DIM×V) Σ_{x,μ} Re[Φ†(x) W(x,μ) Φ(x+μ)] */
/* W(x,μ) = exp(iθ₁/2) U₂(x,μ) — gauge-covariant transport */
/* Symmetric: ⟨hop⟩ ~ 0 (random Φ dirs). Broken: ⟨hop⟩ ~ v² (aligned) */
static double measure_hop(void){
    double h=0;
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
        int sp=nbr(s,mu,+1);
        Cx Wphi[NH];
        apply_W(Wphi, s, mu, &Phi[sp*NH]);
        for(int a=0;a<NH;a++)
            h+=cxmul(cxconj(Phi[s*NH+a]),Wphi[a]).re;
    }
    return h/(VOL*DIM);
}
/* Higgs susceptibility χ = V × (⟨|Φ|²⟩ - ⟨|Φ|⟩²) */
/* Magnetization: M = |Σ_x Φ(x)| / V — the ORDER PARAMETER */
/* Symmetric phase: M ~ 1/√V (random walk). Broken phase: M ~ v (VEV) */
static double measure_magnetization(void){
    Cx sum[NH];
    for(int a=0;a<NH;a++) sum[a]=cx(0,0);
    for(int s=0;s<VOL;s++)
        for(int a=0;a<NH;a++)
            sum[a]=cxadd(sum[a],Phi[s*NH+a]);
    double mag2=0;
    for(int a=0;a<NH;a++) mag2+=cxabs2(sum[a]);
    return sqrt(mag2)/VOL;
}
static void fmt_time(double s,char *b){int h=(int)(s/3600),m=(int)((s-h*3600)/60);int sec=(int)(s-h*3600-m*60);if(h>0)sprintf(b,"%dh%02dm%02ds",h,m,sec);else if(m>0)sprintf(b,"%dm%02ds",m,sec);else sprintf(b,"%.1fs",s);}

/* ---- Main ---- */
int main(int argc,char **argv){
    L=(argc>1)?atoi(argv[1]):6;
    double m0=(argc>2)?atof(argv[2]):0.10;
    double kappa=(argc>3)?atof(argv[3]):0.20;
    double lambda=(argc>4)?atof(argv[4]):0.00;
    double yukawa=(argc>5)?atof(argv[5]):0.122;
    int Ntraj=(argc>6)?atoi(argv[6]):50;
    int Nthm=(argc>7)?atoi(argv[7]):10;
    const char *outf=(argc>8)?argv[8]:"higgs_out.dat";
    int nstep=10; double tau=0.008;
    VOL=L*L*L;
    double b3=11.1,b2=7.4,b1=3.7;
    rng_seed=(unsigned int)time(NULL);
    time_t T0=time(NULL);char tb[64];

    /* Allocate */
    U3=malloc(VOL*DIM*sizeof(M3));U3_bak=malloc(VOL*DIM*sizeof(M3));
    U2=malloc(VOL*DIM*sizeof(M2));U2_bak=malloc(VOL*DIM*sizeof(M2));
    U1=calloc(VOL*DIM,sizeof(double));U1_bak=malloc(VOL*DIM*sizeof(double));
    P3=calloc(VOL*DIM,sizeof(M3));P2=calloc(VOL*DIM,sizeof(M2));P1=calloc(VOL*DIM,sizeof(double));
    Phi=malloc(VOL*NH*sizeof(Cx));Phi_bak=malloc(VOL*NH*sizeof(Cx));
    Pi_h=calloc(VOL*NH,sizeof(Cx));
    phi_pf=calloc(VOL*NK,sizeof(Cx));chi_pf=calloc(VOL*NK,sizeof(Cx));

    /* Initialize gauge to unit, Higgs to random near |Φ|=1 */
    for(int i=0;i<VOL*DIM;i++){U3[i]=m3_unit();U2[i]=m2_unit();}
    for(int s=0;s<VOL;s++){
        double r1=0.5+0.5*drand01(), th1=2*M_PI*drand01();
        double r2=0.5+0.5*drand01(), th2=2*M_PI*drand01();
        Phi[s*NH+0]=cx(r1*cos(th1),r1*sin(th1));
        Phi[s*NH+1]=cx(r2*cos(th2),r2*sin(th2));
    }

    fprintf(stderr,"\n  k6_higgs: K=6 HMC with dynamical Higgs\n");
    fprintf(stderr,"  L=%d m0=%.4f κ=%.4f λ=%.4f y=%.4f β=(%.1f,%.1f,%.1f)\n\n",
            L,m0,kappa,lambda,yukawa,b3,b2,b1);

    /* Pre-thermalize gauge with Metropolis */
    fprintf(stderr,"  Pre-thermalizing gauge (Metropolis)...\n");
    double eps=0.3;
    for(int sw=0;sw<100;sw++){
        for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
            {double So=-(b3/NC3)*m3_retr(m3_mul(U3[s*DIM+mu],m3_staple(s,mu)));M3 h;for(int i=0;i<NC3;i++)for(int j=i;j<NC3;j++){if(i==j)h.e[i][j]=cx(gauss01()*eps,0);else{double r1=gauss01()*eps,r2=gauss01()*eps;h.e[i][j]=cx(r1,r2);h.e[j][i]=cx(r1,-r2);}}double tr=0;for(int i=0;i<NC3;i++)tr+=h.e[i][i].re;tr/=NC3;for(int i=0;i<NC3;i++)h.e[i][i].re-=tr;M3 u=m3_unit();for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)u.e[i][j]=cxadd(u.e[i][j],cx(-h.e[i][j].im,h.e[i][j].re));M3 Uo=U3[s*DIM+mu];U3[s*DIM+mu]=m3_proj(m3_mul(u,Uo));double Sn=-(b3/NC3)*m3_retr(m3_mul(U3[s*DIM+mu],m3_staple(s,mu)));if(Sn-So>0&&drand01()>=exp(-(Sn-So)))U3[s*DIM+mu]=Uo;}
            {double So=-(b2/NC2)*m2_retr(m2_mul(U2[s*DIM+mu],m2_staple(s,mu)));double a1=gauss01()*eps,a2=gauss01()*eps,a3=gauss01()*eps;M2 hh;hh.e[0][0]=cx(1,a3);hh.e[0][1]=cx(a2,a1);hh.e[1][0]=cx(-a2,a1);hh.e[1][1]=cx(1,-a3);M2 Uo=U2[s*DIM+mu];U2[s*DIM+mu]=m2_proj(m2_mul(hh,Uo));double Sn=-(b2/NC2)*m2_retr(m2_mul(U2[s*DIM+mu],m2_staple(s,mu)));if(Sn-So>0&&drand01()>=exp(-(Sn-So)))U2[s*DIM+mu]=Uo;}
            {double stap_re=u1_staple_re(s,mu),stap_im=u1_staple_im(s,mu);double old=U1[s*DIM+mu];double So=-b1*(cos(old)*stap_re+sin(old)*stap_im);U1[s*DIM+mu]=old+eps*(2*drand01()-1);double Sn=-b1*(cos(U1[s*DIM+mu])*stap_re+sin(U1[s*DIM+mu])*stap_im);if(Sn-So>0&&drand01()>=exp(-(Sn-So)))U1[s*DIM+mu]=old;}
        }
    }
    double p3,p2,p1_val;plaquettes(&p3,&p2,&p1_val);
    fprintf(stderr,"  Done. P3=%.4f P2=%.4f P1=%.4f ⟨|Φ|⟩=%.4f\n\n",p3,p2,p1_val,measure_phi_mod());

    FILE *fp=fopen(outf,"a");
    fprintf(fp,"# k6_higgs L=%d m0=%.6f kappa=%.6f lambda=%.6f yukawa=%.6f beta=(%.1f,%.1f,%.1f)\n",
            L,m0,kappa,lambda,yukawa,b3,b2,b1);
    fprintf(fp,"# traj acc dH phi_mod phi_mod2 hop magnet pbp P3 P2 P1\n");
    fflush(fp);

    /* HMC */
    int total_acc=0,nmeas=0;
    double sum_pm=0,sum_pm2=0,sum_r2=0,sum_r22=0;
    double sum_mag=0,sum_mag2=0;
    double sum_hop=0,sum_hop2=0;

    for(int t=0;t<Ntraj+Nthm;t++){
        int acc;
        double dH=do_hmc(m0,yukawa,kappa,lambda,b3,b2,b1,nstep,tau,&acc);
        total_acc+=acc;
        plaquettes(&p3,&p2,&p1_val);

        if(t>=Nthm){
            double pm=measure_phi_mod();
            double r2=measure_phi_mod2();
            double hop=measure_hop();
            double mag=measure_magnetization();
            double pbp=measure_pbp(m0,yukawa);
            sum_pm+=pm;sum_pm2+=pm*pm;
            sum_r2+=r2;sum_r22+=r2*r2;
            sum_mag+=mag;sum_mag2+=mag*mag;
            sum_hop+=hop;sum_hop2+=hop*hop;
            nmeas++;
            fprintf(fp,"%5d %d %+10.4f  %.6f %.6f %.6f %.6f %.6f  %.4f %.4f %.4f\n",
                    t-Nthm,acc,dH,pm,r2,hop,mag,pbp,p3,p2,p1_val);
            fflush(fp);
        }

        if(t%5==0||t==Ntraj+Nthm-1){
            fmt_time(difftime(time(NULL),T0),tb);
            double pm_avg=(nmeas>0)?sum_pm/nmeas:measure_phi_mod();
            double hop_avg=(nmeas>0)?sum_hop/nmeas:0;
            fprintf(stderr,"  traj %3d/%d [%s] %s dH=%+.3f ⟨|Φ|⟩=%.4f ⟨hop⟩=%.4f P=(%.3f,%.3f,%.3f)\n",
                    t+1,Ntraj+Nthm,tb,acc?"ACC":"REJ",dH,pm_avg,hop_avg,p3,p2,p1_val);
        }
    }

    double pm_avg=sum_pm/nmeas, pm_err=sqrt(fabs(sum_pm2/nmeas-pm_avg*pm_avg)/fmax(nmeas-1,1));
    double r2_avg=sum_r2/nmeas;
    double hop_avg=sum_hop/nmeas, hop_err=sqrt(fabs(sum_hop2/nmeas-hop_avg*hop_avg)/fmax(nmeas-1,1));
    double chi_hop=VOL*(sum_hop2/nmeas - hop_avg*hop_avg);
    fmt_time(difftime(time(NULL),T0),tb);
    fprintf(stderr,"\n  DONE (%s). acc=%d%%\n",tb,(100*total_acc)/(Ntraj+Nthm));
    fprintf(stderr,"  ⟨|Φ|⟩=%.6f±%.6f  ⟨hop⟩=%.6f±%.6f  χ_hop=%.4f\n\n",
            pm_avg,pm_err,hop_avg,hop_err,chi_hop);
    fprintf(fp,"# RESULT: kappa=%.6f lambda=%.6f yukawa=%.6f ⟨|Φ|⟩=%.6f±%.6f ⟨hop⟩=%.6f±%.6f chi_hop=%.4f acc=%d%%\n",
            kappa,lambda,yukawa,pm_avg,pm_err,hop_avg,hop_err,chi_hop,(100*total_acc)/(Ntraj+Nthm));
    fclose(fp);

    free(U3);free(U3_bak);free(U2);free(U2_bak);free(U1);free(U1_bak);
    free(P3);free(P2);free(P1);free(Phi);free(Phi_bak);free(Pi_h);
    free(phi_pf);free(chi_pf);
    return 0;
}
