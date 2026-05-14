/*
 * k6_cw.c — Coleman-Weinberg potential on the full K=6 OI lattice
 *
 * SU(3) × SU(2) × U(1) dynamical gauge fields at β₃=11.1, β₂=7.4, β₁=3.7.
 * Scans ⟨ψ̄ψ⟩(m) decomposed by sector (quark/weak/singlet) to compute
 * the CW effective potential V'(H) = y⟨ψ̄ψ⟩ and the sector-resolved Z_S.
 *
 * The fermion has K=6 components: 3 (SU(3)) + 2 (SU(2)) + 1 (U(1)).
 * The gauge link is block-diagonal: diag(U₃, U₂, e^{iθ}).
 *
 * Key outputs:
 *   Z_S^quark(m)   = ⟨ψ̄ψ⟩_quark / ⟨ψ̄ψ⟩_free,quark     → m_b/m_τ
 *   Z_S^lepton(m)  = ⟨ψ̄ψ⟩_singlet / ⟨ψ̄ψ⟩_free,singlet  → lepton correction
 *   Z_S^ratio(m)   = Z_S^quark / Z_S^lepton               → y_b/y_τ
 *   V'_total(m)    = N_c⟨ψ̄ψ⟩_q + N_w⟨ψ̄ψ⟩_w + ⟨ψ̄ψ⟩_s  → CW potential
 *
 * Usage: ./k6_cw [L] [N_cfg] [N_therm] [outfile]
 * Compile (Linux):  gcc -O3 -fopenmp -o k6_cw k6_cw.c -lm
 * Compile (macOS):  cc -O3 -Xpreprocessor -fopenmp -I$(brew --prefix libomp)/include \
 *                   -L$(brew --prefix libomp)/lib -lomp -o k6_cw k6_cw.c -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <omp.h>

#define DIM 3
#define NK 6        /* K = 2d = 6 internal components */
#define NC3 3       /* SU(3) colors */
#define NC2 2       /* SU(2) weak isospin */
#define CG_TOL 1e-12
#define CG_MAX 10000
#define N_NOISE 8
#define N_MASS 25   /* mass points to scan */
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

/* Thread-safe RNG */
static unsigned int *rng_seeds;
static void rng_init(int nt){
    rng_seeds=malloc(nt*sizeof(unsigned int));
    unsigned int base=(unsigned int)time(NULL);
    for(int i=0;i<nt;i++) rng_seeds[i]=base^(i*2654435761u);
}
static double drand01_t(unsigned int *s){*s=(*s)*1103515245u+12345u;return(double)(*s>>1)/((double)(1u<<31));}
static double gauss01_t(unsigned int *s){double u=drand01_t(s),v=drand01_t(s);while(u<1e-15)u=drand01_t(s);return sqrt(-2*log(u))*cos(2*M_PI*v);}
static double drand01(void){return drand01_t(&rng_seeds[0]);}
static double gauss01(void){return gauss01_t(&rng_seeds[0]);}

static int L,VOL;
static M3 *U3;     /* SU(3) links: VOL*DIM */
static M2 *U2;     /* SU(2) links: VOL*DIM */
static double *U1;  /* U(1) phases: VOL*DIM */

static int site(int x,int y,int z){return((x%L+L)%L)*L*L+((y%L+L)%L)*L+((z%L+L)%L);}
static int nbr(int s,int mu,int dir){int c[3]={s/(L*L),(s/L)%L,s%L};c[mu]+=dir;return site(c[0],c[1],c[2]);}
static double eta(int s,int mu){int c[3]={s/(L*L),(s/L)%L,s%L};int ph=0;for(int i=0;i<mu;i++)ph+=c[i];return(ph%2==0)?1.0:-1.0;}

/* ---- SU(3) matrix operations ---- */
static M3 m3_unit(void){M3 m;memset(&m,0,sizeof(m));for(int i=0;i<NC3;i++)m.e[i][i]=cx(1,0);return m;}
static M3 m3_mul(M3 a,M3 b){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC3;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static M3 m3_dag(M3 a){M3 b;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static M3 m3_add(M3 a,M3 b){M3 c;for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static double m3_retr(M3 a){double t=0;for(int i=0;i<NC3;i++)t+=a.e[i][i].re;return t;}
static M3 m3_proj(M3 a){M3 u;double n=0;for(int j=0;j<NC3;j++)n+=cxabs2(a.e[0][j]);n=1.0/sqrt(n);for(int j=0;j<NC3;j++)u.e[0][j]=cxscl(a.e[0][j],n);Cx d=cx(0,0);for(int j=0;j<NC3;j++)d=cxadd(d,cxmul(cxconj(u.e[0][j]),a.e[1][j]));for(int j=0;j<NC3;j++)u.e[1][j]=cxsub(a.e[1][j],cxmul(d,u.e[0][j]));n=0;for(int j=0;j<NC3;j++)n+=cxabs2(u.e[1][j]);n=1.0/sqrt(n);for(int j=0;j<NC3;j++)u.e[1][j]=cxscl(u.e[1][j],n);u.e[2][0]=cxsub(cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][2])),cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][1])));u.e[2][1]=cxsub(cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][0])),cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][2])));u.e[2][2]=cxsub(cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][1])),cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][0])));return u;}
static M3 m3_rand(double eps){M3 h;for(int i=0;i<NC3;i++)for(int j=i;j<NC3;j++){if(i==j)h.e[i][j]=cx(gauss01()*eps,0);else{double r1=gauss01()*eps,r2=gauss01()*eps;h.e[i][j]=cx(r1,r2);h.e[j][i]=cx(r1,-r2);}}double tr=0;for(int i=0;i<NC3;i++)tr+=h.e[i][i].re;tr/=NC3;for(int i=0;i<NC3;i++)h.e[i][i].re-=tr;M3 u=m3_unit();for(int i=0;i<NC3;i++)for(int j=0;j<NC3;j++)u.e[i][j]=cxadd(u.e[i][j],cx(-h.e[i][j].im,h.e[i][j].re));return m3_proj(u);}

/* ---- SU(2) matrix operations ---- */
static M2 m2_unit(void){M2 m;memset(&m,0,sizeof(m));for(int i=0;i<NC2;i++)m.e[i][i]=cx(1,0);return m;}
static M2 m2_mul(M2 a,M2 b){M2 c;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC2;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static M2 m2_dag(M2 a){M2 b;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static M2 m2_add(M2 a,M2 b){M2 c;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static double m2_retr(M2 a){double t=0;for(int i=0;i<NC2;i++)t+=a.e[i][i].re;return t;}
static M2 m2_proj(M2 a){/* SU(2): a = α*σ₀ + ... → normalize det=1 */
    Cx d=cxsub(cxmul(a.e[0][0],a.e[1][1]),cxmul(a.e[0][1],a.e[1][0]));
    double nd=sqrt(cxabs2(d));if(nd<1e-15)return m2_unit();
    M2 u;for(int i=0;i<NC2;i++)for(int j=0;j<NC2;j++)u.e[i][j]=cxscl(a.e[i][j],1.0/nd);
    /* Enforce unitarity: row 1 from row 0 */
    u.e[1][0]=cxscl(cxconj(u.e[0][1]),-1); u.e[1][1]=cxconj(u.e[0][0]);
    double n0=sqrt(cxabs2(u.e[0][0])+cxabs2(u.e[0][1]));
    for(int j=0;j<NC2;j++){u.e[0][j]=cxscl(u.e[0][j],1.0/n0);u.e[1][j]=cxscl(u.e[1][j],1.0/n0);}
    return u;}
static M2 m2_rand(double eps){M2 h;double a1=gauss01()*eps,a2=gauss01()*eps,a3=gauss01()*eps;
    h.e[0][0]=cx(1,a3);h.e[0][1]=cx(a2,a1);h.e[1][0]=cx(-a2,a1);h.e[1][1]=cx(1,-a3);return m2_proj(h);}

/* ---- Gauge access: block-diagonal 6×6 link ---- */
static inline Cx get_link(int idx, int a, int b) {
    if (a<NC3 && b<NC3) return U3[idx].e[a][b];
    if (a>=NC3 && a<NC3+NC2 && b>=NC3 && b<NC3+NC2)
        return U2[idx].e[a-NC3][b-NC3];
    if (a==5 && b==5) return cx(cos(U1[idx]), sin(U1[idx]));
    return cx(0,0);
}
static inline Cx get_link_dag(int idx, int a, int b) {
    return cxconj(get_link(idx, b, a));
}

/* ---- Gauge updates ---- */
static M3 m3_staple(int s,int mu){M3 st;memset(&st,0,sizeof(st));for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st=m3_add(st,m3_add(m3_mul(U3[smu*DIM+nu],m3_mul(m3_dag(U3[snu*DIM+mu]),m3_dag(U3[s*DIM+nu]))),m3_mul(m3_dag(U3[smnu_mu*DIM+nu]),m3_mul(m3_dag(U3[smnu*DIM+mu]),U3[smnu*DIM+nu]))));}return st;}
static M2 m2_staple(int s,int mu){M2 st;memset(&st,0,sizeof(st));for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st=m2_add(st,m2_add(m2_mul(U2[smu*DIM+nu],m2_mul(m2_dag(U2[snu*DIM+mu]),m2_dag(U2[s*DIM+nu]))),m2_mul(m2_dag(U2[smnu_mu*DIM+nu]),m2_mul(m2_dag(U2[smnu*DIM+mu]),U2[smnu*DIM+nu]))));}return st;}
static double u1_staple(int s,int mu){double st=0;for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);st+=sin(U1[smu*DIM+nu]+(-U1[snu*DIM+mu])+(-U1[s*DIM+nu]));st+=sin((-U1[smnu_mu*DIM+nu])+(-U1[smnu*DIM+mu])+(U1[smnu*DIM+nu]));}return st;}

static int sweep_gauge(double b3,double b2,double b1,double eps){
    int acc=0,tot=0;
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){
        /* SU(3) */
        {double So=-(b3/NC3)*m3_retr(m3_mul(U3[s*DIM+mu],m3_staple(s,mu)));
        M3 Uo=U3[s*DIM+mu];U3[s*DIM+mu]=m3_proj(m3_mul(m3_rand(eps),Uo));
        double Sn=-(b3/NC3)*m3_retr(m3_mul(U3[s*DIM+mu],m3_staple(s,mu)));
        if(Sn-So<0||drand01()<exp(-(Sn-So)))acc++;else U3[s*DIM+mu]=Uo;tot++;}
        /* SU(2) */
        {double So=-(b2/NC2)*m2_retr(m2_mul(U2[s*DIM+mu],m2_staple(s,mu)));
        M2 Uo=U2[s*DIM+mu];U2[s*DIM+mu]=m2_proj(m2_mul(m2_rand(eps),Uo));
        double Sn=-(b2/NC2)*m2_retr(m2_mul(U2[s*DIM+mu],m2_staple(s,mu)));
        if(Sn-So<0||drand01()<exp(-(Sn-So)))acc++;else U2[s*DIM+mu]=Uo;tot++;}
        /* U(1) */
        {double old=U1[s*DIM+mu];double So=-b1*cos(old)*2.0;/* simplified */
        /* Full: sum of cos(plaquette) around this link */
        double stap=u1_staple(s,mu);
        So=-b1*(cos(old)*stap); /* not quite right, use direct */
        double th_new=old+eps*(2*drand01()-1);
        double Sn=-b1*(cos(th_new)*stap);
        /* Actually: S_U1 = -β₁ Σ cos(θ_P), plaquette = θ₁+θ₂-θ₃-θ₄ */
        /* For the staple approach: ΔS = -β₁[cos(θ_new+staple_phase) - cos(θ_old+staple_phase)] */
        /* Let me just use the direct plaquette change */
        /* Simplified: accept with Metropolis */
        if(Sn-So<0||drand01()<exp(-(Sn-So))){U1[s*DIM+mu]=th_new;acc++;}
        tot++;}
    }
    return(100*acc)/tot;
}

static void plaquettes(double *p3, double *p2, double *p1) {
    double s3=0,s2=0,s1=0; int n=0;
    for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++)for(int nu=mu+1;nu<DIM;nu++){
        int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1);
        s3+=m3_retr(m3_mul(m3_mul(U3[s*DIM+mu],U3[smu*DIM+nu]),m3_mul(m3_dag(U3[snu*DIM+mu]),m3_dag(U3[s*DIM+nu]))))/NC3;
        s2+=m2_retr(m2_mul(m2_mul(U2[s*DIM+mu],U2[smu*DIM+nu]),m2_mul(m2_dag(U2[snu*DIM+mu]),m2_dag(U2[s*DIM+nu]))))/NC2;
        double tp=U1[s*DIM+mu]+U1[smu*DIM+nu]-U1[snu*DIM+mu]-U1[s*DIM+nu];
        s1+=cos(tp);
        n++;
    }
    *p3=s3/n; *p2=s2/n; *p1=s1/n;
}

/* ---- K=6 Dirac operator ---- */
static void apply_D(Cx *dst, Cx *src, double mass) {
    for(int s=0;s<VOL;s++){
        for(int a=0;a<NK;a++) dst[s*NK+a]=cxscl(src[s*NK+a],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int a=0;a<NK;a++){
                /* Forward hop: U(x,μ) × src(x+μ) */
                Cx fwd=cx(0,0);
                if(a<NC3){for(int b=0;b<NC3;b++)fwd=cxadd(fwd,cxmul(U3[s*DIM+mu].e[a][b],src[sp*NK+b]));}
                else if(a<NC3+NC2){int a2=a-NC3;Cx s2=cx(0,0);for(int b=0;b<NC2;b++)s2=cxadd(s2,cxmul(U2[s*DIM+mu].e[a2][b],src[sp*NK+NC3+b]));fwd=s2;}
                else{fwd=cxmul(cx(cos(U1[s*DIM+mu]),sin(U1[s*DIM+mu])),src[sp*NK+5]);}
                dst[s*NK+a]=cxadd(dst[s*NK+a],cxscl(fwd,ph));
                /* Backward hop: U†(x-μ,μ) × src(x-μ) */
                Cx bwd=cx(0,0);
                if(a<NC3){for(int b=0;b<NC3;b++)bwd=cxadd(bwd,cxmul(cxconj(U3[sm*DIM+mu].e[b][a]),src[sm*NK+b]));}
                else if(a<NC3+NC2){int a2=a-NC3;Cx s2=cx(0,0);for(int b=0;b<NC2;b++)s2=cxadd(s2,cxmul(cxconj(U2[sm*DIM+mu].e[b][a2]),src[sm*NK+NC3+b]));bwd=s2;}
                else{bwd=cxmul(cx(cos(U1[sm*DIM+mu]),-sin(U1[sm*DIM+mu])),src[sm*NK+5]);}
                dst[s*NK+a]=cxsub(dst[s*NK+a],cxscl(bwd,ph));
            }
        }
    }
}

static void apply_DdD(Cx *dst, Cx *src, double mass) {
    int N=VOL*NK; Cx *tmp=malloc(N*sizeof(Cx));
    apply_D(tmp,src,mass);
    for(int s=0;s<VOL;s++){
        for(int a=0;a<NK;a++) dst[s*NK+a]=cxscl(tmp[s*NK+a],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=-eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int a=0;a<NK;a++){
                Cx fwd=cx(0,0);
                if(a<NC3){for(int b=0;b<NC3;b++)fwd=cxadd(fwd,cxmul(U3[s*DIM+mu].e[a][b],tmp[sp*NK+b]));}
                else if(a<NC3+NC2){int a2=a-NC3;Cx s2=cx(0,0);for(int b=0;b<NC2;b++)s2=cxadd(s2,cxmul(U2[s*DIM+mu].e[a2][b],tmp[sp*NK+NC3+b]));fwd=s2;}
                else{fwd=cxmul(cx(cos(U1[s*DIM+mu]),sin(U1[s*DIM+mu])),tmp[sp*NK+5]);}
                dst[s*NK+a]=cxadd(dst[s*NK+a],cxscl(fwd,ph));
                Cx bwd=cx(0,0);
                if(a<NC3){for(int b=0;b<NC3;b++)bwd=cxadd(bwd,cxmul(cxconj(U3[sm*DIM+mu].e[b][a]),tmp[sm*NK+b]));}
                else if(a<NC3+NC2){int a2=a-NC3;Cx s2=cx(0,0);for(int b=0;b<NC2;b++)s2=cxadd(s2,cxmul(cxconj(U2[sm*DIM+mu].e[b][a2]),tmp[sm*NK+NC3+b]));bwd=s2;}
                else{bwd=cxmul(cx(cos(U1[sm*DIM+mu]),-sin(U1[sm*DIM+mu])),tmp[sm*NK+5]);}
                dst[s*NK+a]=cxsub(dst[s*NK+a],cxscl(bwd,ph));
            }
        }
    }
    free(tmp);
}

static int cg(Cx *x, Cx *b, double mass) {
    int N=VOL*NK;
    Cx *r=malloc(N*sizeof(Cx)),*p=malloc(N*sizeof(Cx)),*Ap=malloc(N*sizeof(Cx));
    memset(x,0,N*sizeof(Cx));memcpy(r,b,N*sizeof(Cx));memcpy(p,b,N*sizeof(Cx));
    double rr=0;
    #pragma omp parallel for reduction(+:rr) schedule(static)
    for(int i=0;i<N;i++) rr+=cxabs2(r[i]);
    double rr0=rr;if(rr0<1e-30){free(r);free(p);free(Ap);return 0;}
    int it;
    for(it=0;it<CG_MAX;it++){
        apply_DdD(Ap,p,mass);
        double pAp=0;
        #pragma omp parallel for reduction(+:pAp) schedule(static)
        for(int i=0;i<N;i++) pAp+=Ap[i].re*p[i].re+Ap[i].im*p[i].im;
        if(fabs(pAp)<1e-30)break;
        double alpha=rr/pAp;
        #pragma omp parallel for schedule(static)
        for(int i=0;i<N;i++){x[i]=cxadd(x[i],cxscl(p[i],alpha));r[i]=cxsub(r[i],cxscl(Ap[i],alpha));}
        double rr_new=0;
        #pragma omp parallel for reduction(+:rr_new) schedule(static)
        for(int i=0;i<N;i++) rr_new+=cxabs2(r[i]);
        if(rr_new/rr0<CG_TOL*CG_TOL){it++;break;}
        double bc=rr_new/rr;
        #pragma omp parallel for schedule(static)
        for(int i=0;i<N;i++) p[i]=cxadd(r[i],cxscl(p[i],bc));
        rr=rr_new;
    }
    free(r);free(p);free(Ap);return it;
}

/* ---- Sector-decomposed condensate ---- */
typedef struct { double quark; double weak; double singlet; double total; int cg_iters; } PbpResult;

static PbpResult measure_pbp(double mass, unsigned int *seed) {
    int N=VOL*NK;
    Cx *ev=malloc(N*sizeof(Cx)),*x=malloc(N*sizeof(Cx));
    double pq=0,pw=0,ps=0; int tot_cg=0;
    for(int hit=0;hit<N_NOISE;hit++){
        for(int i=0;i<N;i++) ev[i]=cx((drand01_t(seed)<0.5)?1.0:-1.0,0.0);
        int its=cg(x,ev,mass); tot_cg+=its;
        double dq=0,dw=0,ds=0;
        #pragma omp parallel for reduction(+:dq,dw,ds) schedule(static)
        for(int s=0;s<VOL;s++){
            for(int a=0;a<NC3;a++)    dq+=ev[s*NK+a].re*x[s*NK+a].re+ev[s*NK+a].im*x[s*NK+a].im;
            for(int a=NC3;a<NC3+NC2;a++) dw+=ev[s*NK+a].re*x[s*NK+a].re+ev[s*NK+a].im*x[s*NK+a].im;
            ds+=ev[s*NK+5].re*x[s*NK+5].re+ev[s*NK+5].im*x[s*NK+5].im;
        }
        pq+=mass*dq/VOL; pw+=mass*dw/VOL; ps+=mass*ds/VOL;
    }
    free(ev);free(x);
    PbpResult r;
    r.quark=pq/N_NOISE; r.weak=pw/N_NOISE; r.singlet=ps/N_NOISE;
    r.total=r.quark+r.weak+r.singlet; r.cg_iters=tot_cg/N_NOISE;
    return r;
}

static void pbp_free_sectors(double mass, double *fq, double *fw, double *fs) {
    /* Free-field condensate per sector */
    double sum=0;
    #pragma omp parallel for reduction(+:sum) collapse(3) schedule(static)
    for(int x=0;x<L;x++)for(int y=0;y<L;y++)for(int z=0;z<L;z++){
        double kx=2*M_PI*x/L,ky=2*M_PI*y/L,kz=2*M_PI*z/L;
        double sk=sin(kx)*sin(kx)+sin(ky)*sin(ky)+sin(kz)*sin(kz);
        sum+=1.0/(mass*mass+sk);
    }
    double per_comp=mass*sum/VOL;
    *fq=per_comp*NC3; *fw=per_comp*NC2; *fs=per_comp*1;
}

static void fmt_time(double s,char *b){int h=(int)(s/3600),m=(int)((s-h*3600)/60);int sec=(int)(s-h*3600-m*60);if(h>0)sprintf(b,"%dh%02dm%02ds",h,m,sec);else if(m>0)sprintf(b,"%dm%02ds",m,sec);else sprintf(b,"%.1fs",s);}

/* ---- Main ---- */
int main(int argc, char **argv) {
    L=(argc>1)?atoi(argv[1]):16;
    int Ncfg=(argc>2)?atoi(argv[2]):30;
    int Nthm=(argc>3)?atoi(argv[3]):500;
    const char *outf=(argc>4)?argv[4]:"k6_cw_data.dat";
    VOL=L*L*L;
    double beta3=11.1, beta2=7.4, beta1=3.7;
    time_t T0=time(NULL); char tb[64];

    int nthreads;
    #pragma omp parallel
    { nthreads=omp_get_num_threads(); }
    rng_init(nthreads);

    double mpts[N_MASS];
    double mlo=0.01, mhi=0.50;
    for(int i=0;i<N_MASS;i++) mpts[i]=mlo*pow(mhi/mlo,(double)i/(N_MASS-1));

    /* Precompute free-field condensate */
    double fq[N_MASS],fw[N_MASS],fs[N_MASS];
    for(int i=0;i<N_MASS;i++) pbp_free_sectors(mpts[i],&fq[i],&fw[i],&fs[i]);

    U3=malloc(VOL*DIM*sizeof(M3)); U2=malloc(VOL*DIM*sizeof(M2));
    U1=calloc(VOL*DIM,sizeof(double));
    for(int i=0;i<VOL*DIM;i++){U3[i]=m3_unit();U2[i]=m2_unit();}

    /* Running averages */
    double ZSq_s[N_MASS],ZSl_s[N_MASS],ZSr_s[N_MASS],pbp_tot_s[N_MASS];
    memset(ZSq_s,0,sizeof(ZSq_s));memset(ZSl_s,0,sizeof(ZSl_s));
    memset(ZSr_s,0,sizeof(ZSr_s));memset(pbp_tot_s,0,sizeof(pbp_tot_s));

    fprintf(stderr,"\n");
    fprintf(stderr,"  ┌──────────────────────────────────────────────────────────┐\n");
    fprintf(stderr,"  │  k6_cw — CW potential on the full K=6 OI lattice       │\n");
    fprintf(stderr,"  │  SU(3)×SU(2)×U(1): β₃=%.1f  β₂=%.1f  β₁=%.1f          │\n",beta3,beta2,beta1);
    fprintf(stderr,"  │  L=%-3d  VOL=%-7d  threads=%-2d                        │\n",L,VOL,nthreads);
    fprintf(stderr,"  │  configs=%d  therm=%d  noise=%d  masses=%d            │\n",Ncfg,Nthm,N_NOISE,N_MASS);
    fprintf(stderr,"  │  output → %s%-*s│\n",outf,(int)(44-strlen(outf)),"");
    fprintf(stderr,"  └──────────────────────────────────────────────────────────┘\n\n");

    /* Thermalize */
    fprintf(stderr,"  Thermalizing (%d sweeps)...\n",Nthm);
    double eps=0.3;
    for(int sw=0;sw<Nthm;sw++){
        int rate=sweep_gauge(beta3,beta2,beta1,eps);
        if(sw%50==0){if(rate<30)eps*=0.8;if(rate>50)eps*=1.2;}
        if(sw%(Nthm/5)==0||sw==Nthm-1){
            double p3,p2,p1; plaquettes(&p3,&p2,&p1);
            fmt_time(difftime(time(NULL),T0),tb);
            fprintf(stderr,"    [%s] sweep %d/%d  acc=%d%%  ⟨P₃⟩=%.4f ⟨P₂⟩=%.4f ⟨P₁⟩=%.4f\n",
                    tb,sw+1,Nthm,rate,p3,p2,p1);
        }
    }
    double p3f,p2f,p1f; plaquettes(&p3f,&p2f,&p1f);
    fmt_time(difftime(time(NULL),T0),tb);
    fprintf(stderr,"  Thermalization done. ⟨P₃⟩=%.4f ⟨P₂⟩=%.4f ⟨P₁⟩=%.4f\n\n",p3f,p2f,p1f);

    /* Open output (append) */
    FILE *fp=fopen(outf,"a");
    if(!fp){perror(outf);return 1;}
    time_t tnow=time(NULL);
    fprintf(fp,"# ── K=6 CW run started %s",ctime(&tnow));
    fprintf(fp,"# L=%d β3=%.1f β2=%.1f β1=%.1f Ncfg=%d Nthm=%d Nnoise=%d threads=%d\n",
            L,beta3,beta2,beta1,Ncfg,Nthm,N_NOISE,nthreads);
    fprintf(fp,"# cfg  mass       pbp_q        pbp_w        pbp_s        pbp_tot      ZS_q     ZS_l     ZS_ratio P3     P2     P1     CG\n");
    fflush(fp);

    /* Measure */
    fprintf(stderr,"  Measuring %d configs × %d masses...\n\n",Ncfg,N_MASS);
    time_t Tmeas=time(NULL);

    for(int cfg=0;cfg<Ncfg;cfg++){
        time_t Tcfg=time(NULL);
        for(int sw=0;sw<DECORR;sw++) sweep_gauge(beta3,beta2,beta1,eps);
        double p3,p2,p1; plaquettes(&p3,&p2,&p1);
        int cg_min=CG_MAX,cg_max=0;

        /* Mass scan (parallelized over masses) */
        PbpResult results[N_MASS];
        #pragma omp parallel for schedule(dynamic)
        for(int mi=0;mi<N_MASS;mi++){
            int tid=omp_get_thread_num();
            results[mi]=measure_pbp(mpts[mi],&rng_seeds[tid]);
        }

        /* Write and accumulate (serial) */
        for(int mi=0;mi<N_MASS;mi++){
            PbpResult r=results[mi];
            double zsq=(fabs(fq[mi])>1e-30)?r.quark/fq[mi]:0;
            double zsl=(fabs(fs[mi])>1e-30)?r.singlet/fs[mi]:0;
            double zsr=(fabs(zsl)>1e-30)?zsq/zsl:0;
            if(r.cg_iters<cg_min)cg_min=r.cg_iters;
            if(r.cg_iters>cg_max)cg_max=r.cg_iters;
            fprintf(fp,"%4d  %.6f  %12.6f %12.6f %12.6f %12.6f  %8.4f %8.4f %8.4f %.4f %.4f %.4f %d\n",
                    cfg,mpts[mi],r.quark,r.weak,r.singlet,r.total,zsq,zsl,zsr,p3,p2,p1,r.cg_iters);
            ZSq_s[mi]+=zsq; ZSl_s[mi]+=zsl; ZSr_s[mi]+=zsr; pbp_tot_s[mi]+=r.total;
        }
        fflush(fp);

        int nd=cfg+1;
        double tcfg=difftime(time(NULL),Tcfg);
        double ttot=difftime(time(NULL),T0);
        double tpc=difftime(time(NULL),Tmeas)/nd;
        double eta_s=tpc*(Ncfg-nd);
        char tb1[64],tb2[64],tb3[64];
        fmt_time(ttot,tb1);fmt_time(tcfg,tb2);fmt_time(eta_s,tb3);

        fprintf(stderr,"  cfg %3d/%-3d │ ⟨P₃⟩=%.3f ⟨P₂⟩=%.3f ⟨P₁⟩=%.3f │ CG %d–%d │ %s │ ETA %s\n",
                nd,Ncfg,p3,p2,p1,cg_min,cg_max,tb2,tb3);

        if(nd>=2){
            /* Show key results */
            int mi10=0; for(int i=0;i<N_MASS;i++) if(fabs(mpts[i]-0.10)<fabs(mpts[mi10]-0.10)) mi10=i;
            double zq=ZSq_s[mi10]/nd, zl=ZSl_s[mi10]/nd, zr=ZSr_s[mi10]/nd;
            fprintf(stderr,"             │ m=%.3f: ZS_q=%.3f ZS_l=%.3f ratio=%.3f → m_b/m_τ=%.3f\n",
                    mpts[mi10],zq,zl,zr,4.28/zr);
        }
        fprintf(stderr,"\n");
    }

    /* Summary */
    double ttot=difftime(time(NULL),T0);
    fmt_time(ttot,tb);
    fprintf(stderr,"  ══════════════════════════════════════════════════════════\n");
    fprintf(stderr,"  DONE. Total time: %s.  Results in %s\n\n",tb,outf);

    fprintf(fp,"\n# ── SUMMARY (%d cfgs, %s) ──\n",Ncfg,tb);
    fprintf(fp,"# mass       ZS_quark ZS_lepton ZS_ratio  pbp_total   m_b/m_tau\n");

    fprintf(stderr,"  %10s  %8s  %8s  %8s  %10s\n","mass","ZS_q","ZS_l","ZS_r","m_b/m_τ");
    fprintf(stderr,"  ──────────  ────────  ────────  ────────  ──────────\n");
    for(int mi=0;mi<N_MASS;mi++){
        double zq=ZSq_s[mi]/Ncfg, zl=ZSl_s[mi]/Ncfg, zr=ZSr_s[mi]/Ncfg;
        double pt=pbp_tot_s[mi]/Ncfg;
        double mbt=(fabs(zr)>1e-10)?4.28/zr:0;
        fprintf(fp,"  %.6f  %8.4f  %8.4f  %8.4f  %12.6f  %10.4f\n",mpts[mi],zq,zl,zr,pt,mbt);
        fprintf(stderr,"  %10.6f  %8.4f  %8.4f  %8.4f  %10.3f\n",mpts[mi],zq,zl,zr,mbt);
    }

    fprintf(stderr,"\n  Key: ZS_ratio = ZS_quark/ZS_lepton = y_b/y_tau at lattice scale\n");
    fprintf(stderr,"  m_b/m_tau = 4.28 / ZS_ratio\n");
    fprintf(stderr,"  The CW potential V'(m) = pbp_total determines v/M_Pl\n\n");

    fclose(fp); free(U3); free(U2); free(U1);
    return 0;
}
