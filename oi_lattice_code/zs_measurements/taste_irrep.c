/*
 * taste_proj.c — Taste-projected Z_S
 *
 * Computes Z_S separately for:
 *   (a) Taste-singlet: momenta in reduced BZ (|n_μ| < L/4)
 *   (b) All tastes: momenta in full BZ
 *   (c) Taste-non-singlet: momenta near BZ corners
 *
 * The Higgs couples to the taste-singlet (A₁). The correct 
 * Yukawa matching uses Z_S(taste-singlet).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define DIM 3
#define NC 3
#define CG_TOL 1e-12
#define CG_MAX 10000

typedef struct { double re, im; } Cx;
typedef struct { Cx e[NC][NC]; } Mat;

static Cx cx(double r,double i){return(Cx){r,i};}
static Cx cxadd(Cx a,Cx b){return cx(a.re+b.re,a.im+b.im);}
static Cx cxsub(Cx a,Cx b){return cx(a.re-b.re,a.im-b.im);}
static Cx cxmul(Cx a,Cx b){return cx(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re);}
static Cx cxconj(Cx a){return cx(a.re,-a.im);}
static Cx cxscl(Cx a,double s){return cx(a.re*s,a.im*s);}
static double cxabs2(Cx a){return a.re*a.re+a.im*a.im;}
static double drand01(void){return(double)rand()/RAND_MAX;}
static double gauss01(void){double u=drand01(),v=drand01();while(u<1e-15)u=drand01();return sqrt(-2*log(u))*cos(2*M_PI*v);}

static int L,VOL;
static Mat *U;

static int site(int x,int y,int z){return((x%L+L)%L)*L*L+((y%L+L)%L)*L+((z%L+L)%L);}
static int nbr(int s,int mu,int dir){int c[3]={s/(L*L),(s/L)%L,s%L};c[mu]+=dir;return site(c[0],c[1],c[2]);}
static double eta(int s,int mu){int c[3]={s/(L*L),(s/L)%L,s%L};int ph=0;for(int i=0;i<mu;i++)ph+=c[i];return(ph%2==0)?1.0:-1.0;}

static Mat mat_unit(void){Mat m;memset(&m,0,sizeof(m));for(int i=0;i<NC;i++)m.e[i][i]=cx(1,0);return m;}
static Mat mat_mul(Mat a,Mat b){Mat c;for(int i=0;i<NC;i++)for(int j=0;j<NC;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static Mat mat_dag(Mat a){Mat b;for(int i=0;i<NC;i++)for(int j=0;j<NC;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static Mat mat_add(Mat a,Mat b){Mat c;for(int i=0;i<NC;i++)for(int j=0;j<NC;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static double mat_retr(Mat a){double t=0;for(int i=0;i<NC;i++)t+=a.e[i][i].re;return t;}
static Mat mat_proj(Mat a){Mat u;double n=0;for(int j=0;j<NC;j++)n+=cxabs2(a.e[0][j]);n=1.0/sqrt(n);for(int j=0;j<NC;j++)u.e[0][j]=cxscl(a.e[0][j],n);Cx d=cx(0,0);for(int j=0;j<NC;j++)d=cxadd(d,cxmul(cxconj(u.e[0][j]),a.e[1][j]));for(int j=0;j<NC;j++)u.e[1][j]=cxsub(a.e[1][j],cxmul(d,u.e[0][j]));n=0;for(int j=0;j<NC;j++)n+=cxabs2(u.e[1][j]);n=1.0/sqrt(n);for(int j=0;j<NC;j++)u.e[1][j]=cxscl(u.e[1][j],n);u.e[2][0]=cxsub(cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][2])),cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][1])));u.e[2][1]=cxsub(cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][0])),cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][2])));u.e[2][2]=cxsub(cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][1])),cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][0])));return u;}
static Mat mat_rand(double eps){Mat h;for(int i=0;i<NC;i++)for(int j=i;j<NC;j++){if(i==j)h.e[i][j]=cx(gauss01()*eps,0);else{double r1=gauss01()*eps,r2=gauss01()*eps;h.e[i][j]=cx(r1,r2);h.e[j][i]=cx(r1,-r2);}}double tr=0;for(int i=0;i<NC;i++)tr+=h.e[i][i].re;tr/=NC;for(int i=0;i<NC;i++)h.e[i][i].re-=tr;Mat u=mat_unit();for(int i=0;i<NC;i++)for(int j=0;j<NC;j++)u.e[i][j]=cxadd(u.e[i][j],cx(-h.e[i][j].im,h.e[i][j].re));return mat_proj(u);}
static Mat staple(int s,int mu){Mat stap;memset(&stap,0,sizeof(stap));for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);stap=mat_add(stap,mat_add(mat_mul(U[smu*DIM+nu],mat_mul(mat_dag(U[snu*DIM+mu]),mat_dag(U[s*DIM+nu]))),mat_mul(mat_dag(U[smnu_mu*DIM+nu]),mat_mul(mat_dag(U[smnu*DIM+mu]),U[smnu*DIM+nu]))));}return stap;}
static int sweep(double beta,double eps){int acc=0,tot=0;for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){double So=-(beta/NC)*mat_retr(mat_mul(U[s*DIM+mu],staple(s,mu)));Mat Uo=U[s*DIM+mu];U[s*DIM+mu]=mat_proj(mat_mul(mat_rand(eps),Uo));double Sn=-(beta/NC)*mat_retr(mat_mul(U[s*DIM+mu],staple(s,mu)));if(Sn-So<0||drand01()<exp(-(Sn-So)))acc++;else U[s*DIM+mu]=Uo;tot++;}return(100*acc)/tot;}

static void apply_DdagD(Cx *dst, Cx *src, double mass) {
    int N=VOL*NC; Cx *tmp=malloc(N*sizeof(Cx));
    for(int s=0;s<VOL;s++){for(int c=0;c<NC;c++)tmp[s*NC+c]=cxscl(src[s*NC+c],mass);for(int mu=0;mu<DIM;mu++){double ph=eta(s,mu)*0.5;int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],src[sp*NC+c2]));tmp[s*NC+c]=cxadd(tmp[s*NC+c],cxscl(sum,ph));}for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),src[sm*NC+c2]));tmp[s*NC+c]=cxsub(tmp[s*NC+c],cxscl(sum,ph));}}}
    for(int s=0;s<VOL;s++){for(int c=0;c<NC;c++)dst[s*NC+c]=cxscl(tmp[s*NC+c],mass);for(int mu=0;mu<DIM;mu++){double ph=-eta(s,mu)*0.5;int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],tmp[sp*NC+c2]));dst[s*NC+c]=cxadd(dst[s*NC+c],cxscl(sum,ph));}for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),tmp[sm*NC+c2]));dst[s*NC+c]=cxsub(dst[s*NC+c],cxscl(sum,ph));}}}
    free(tmp);
}

static int cg(Cx *x, Cx *b, double mass){
    int N=VOL*NC;Cx *r=malloc(N*sizeof(Cx)),*p=malloc(N*sizeof(Cx)),*Ap=malloc(N*sizeof(Cx));
    memset(x,0,N*sizeof(Cx));memcpy(r,b,N*sizeof(Cx));memcpy(p,b,N*sizeof(Cx));
    double rr=0;for(int i=0;i<N;i++)rr+=cxabs2(r[i]);double rr0=rr;if(rr0<1e-30){free(r);free(p);free(Ap);return 0;}
    int it;for(it=0;it<CG_MAX;it++){apply_DdagD(Ap,p,mass);double pAp=0;for(int i=0;i<N;i++)pAp+=Ap[i].re*p[i].re+Ap[i].im*p[i].im;if(fabs(pAp)<1e-30)break;double alpha=rr/pAp;for(int i=0;i<N;i++){x[i]=cxadd(x[i],cxscl(p[i],alpha));r[i]=cxsub(r[i],cxscl(Ap[i],alpha));}double rr_new=0;for(int i=0;i<N;i++)rr_new+=cxabs2(r[i]);if(rr_new/rr0<CG_TOL*CG_TOL){it++;break;}double bc=rr_new/rr;for(int i=0;i<N;i++)p[i]=cxadd(r[i],cxscl(p[i],bc));rr=rr_new;}
    free(r);free(p);free(Ap);return it;
}

/* Compute propagator and decompose by taste */
static void measure_taste_ZS(double mass, double *ZS_out, double *Sp0_cache) {
    int N = VOL*NC;
    Cx *src = calloc(N, sizeof(Cx));
    Cx *tmp = malloc(N*sizeof(Cx));
    Cx *sol = malloc(N*sizeof(Cx));
    
    /* S_tilde(p) for each color source */
    double *Sp_re = calloc(VOL, sizeof(double));
    double *Sp_im = calloc(VOL, sizeof(double));
    
    for(int csrc = 0; csrc < NC; csrc++) {
        memset(src, 0, N*sizeof(Cx));
        src[csrc] = cx(1,0);
        /* D† src */
        for(int s=0;s<VOL;s++){for(int c=0;c<NC;c++)tmp[s*NC+c]=cxscl(src[s*NC+c],mass);for(int mu=0;mu<DIM;mu++){double ph=-eta(s,mu)*0.5;int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],src[sp*NC+c2]));tmp[s*NC+c]=cxadd(tmp[s*NC+c],cxscl(sum,ph));}for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),src[sm*NC+c2]));tmp[s*NC+c]=cxsub(tmp[s*NC+c],cxscl(sum,ph));}}}
        cg(sol, tmp, mass);
        
        /* FT */
        for(int px=0;px<L;px++) for(int py=0;py<L;py++) for(int pz=0;pz<L;pz++) {
            int sp = px*L*L+py*L+pz;
            double kx=2*M_PI*px/L, ky=2*M_PI*py/L, kz=2*M_PI*pz/L;
            for(int xx=0;xx<L;xx++) for(int yy=0;yy<L;yy++) for(int zz=0;zz<L;zz++) {
                int sx = xx*L*L+yy*L+zz;
                double phase = -(kx*xx+ky*yy+kz*zz);
                double cp=cos(phase), sp2=sin(phase);
                Cx sv = sol[sx*NC+csrc];
                Sp_re[sp] += sv.re*cp - sv.im*sp2;
                Sp_im[sp] += sv.re*sp2 + sv.im*cp;
            }
        }
    }
    
    /* Decompose by taste irrep based on nearest BZ corner:
     * A1: (0,0,0)              — n_high = 0 — Higgs
     * T1: (π,0,0) etc          — n_high = 1 — 3 generations
     * T2: (π,π,0) etc          — n_high = 2
     * A2: (π,π,π)              — n_high = 3
     * where n_high = number of components with |n_μ| >= L/4 */
    double pbp_taste[4] = {0}, pbp0_taste[4] = {0};
    double pbp_all = 0, pbp0_all = 0;
    int n_taste[4] = {0};
    
    int Lq = L/4;
    
    for(int px=0;px<L;px++) for(int py=0;py<L;py++) for(int pz=0;pz<L;pz++) {
        int sp = px*L*L+py*L+pz;
        double Si = sqrt(Sp_re[sp]*Sp_re[sp] + Sp_im[sp]*Sp_im[sp]);
        double S0 = Sp0_cache[sp];
        
        pbp_all += Si;
        pbp0_all += S0;
        
        int nx = px<=L/2 ? px : px-L;
        int ny = py<=L/2 ? py : py-L;
        int nz = pz<=L/2 ? pz : pz-L;
        int n_high = (abs(nx)>=Lq?1:0) + (abs(ny)>=Lq?1:0) + (abs(nz)>=Lq?1:0);
        
        pbp_taste[n_high] += Si;
        pbp0_taste[n_high] += S0;
        n_taste[n_high]++;
    }
    
    /* Output: ZS per taste irrep */
    ZS_out[0] = (pbp0_taste[0]>0) ? pbp_taste[0]/pbp0_taste[0] : 1; /* A1 */
    ZS_out[1] = (pbp0_taste[1]>0) ? pbp_taste[1]/pbp0_taste[1] : 1; /* T1 */
    ZS_out[2] = (pbp0_taste[2]>0) ? pbp_taste[2]/pbp0_taste[2] : 1; /* T2 */
    ZS_out[3] = (pbp0_taste[3]>0) ? pbp_taste[3]/pbp0_taste[3] : 1; /* A2 */
    ZS_out[4] = (pbp0_all>0) ? pbp_all/pbp0_all : 1;                /* all */
    
    free(src); free(tmp); free(sol); free(Sp_re); free(Sp_im);
}

int main(int argc, char **argv) {
    L = argc>1 ? atoi(argv[1]) : 12;
    int ncfg = argc>2 ? atoi(argv[2]) : 15;
    int nthm = argc>3 ? atoi(argv[3]) : 100;
    double beta = argc>4 ? atof(argv[4]) : 11.10;
    double mass = argc>5 ? atof(argv[5]) : 0.20;
    
    srand(time(NULL)); VOL=L*L*L;
    U = malloc(VOL*DIM*sizeof(Mat));
    for(int i=0;i<VOL*DIM;i++) U[i]=mat_unit();
    
    printf("================================================================\n");
    printf("TASTE-PROJECTED Z_S: L=%d beta=%.2f m=%.3f\n", L, beta, mass);
    printf("================================================================\n");
    
    /* Free-field: compute and cache |S_free(p)| */
    double *Sp0 = calloc(VOL, sizeof(double));
    {
        int N=VOL*NC;
        Cx *src=calloc(N,sizeof(Cx)),*tmp=malloc(N*sizeof(Cx)),*sol=malloc(N*sizeof(Cx));
        double *Sp0_re=calloc(VOL,sizeof(double)),*Sp0_im=calloc(VOL,sizeof(double));
        for(int csrc=0;csrc<NC;csrc++){
            memset(src,0,N*sizeof(Cx));src[csrc]=cx(1,0);
            for(int s=0;s<VOL;s++){for(int c=0;c<NC;c++)tmp[s*NC+c]=cxscl(src[s*NC+c],mass);for(int mu=0;mu<DIM;mu++){double ph=-eta(s,mu)*0.5;int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],src[sp*NC+c2]));tmp[s*NC+c]=cxadd(tmp[s*NC+c],cxscl(sum,ph));}for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),src[sm*NC+c2]));tmp[s*NC+c]=cxsub(tmp[s*NC+c],cxscl(sum,ph));}}}
            cg(sol,tmp,mass);
            for(int px=0;px<L;px++)for(int py=0;py<L;py++)for(int pz=0;pz<L;pz++){int sp=px*L*L+py*L+pz;double kx=2*M_PI*px/L,ky=2*M_PI*py/L,kz=2*M_PI*pz/L;for(int xx=0;xx<L;xx++)for(int yy=0;yy<L;yy++)for(int zz=0;zz<L;zz++){int sx=xx*L*L+yy*L+zz;double phase=-(kx*xx+ky*yy+kz*zz);Cx sv=sol[sx*NC+csrc];Sp0_re[sp]+=sv.re*cos(phase)-sv.im*sin(phase);Sp0_im[sp]+=sv.re*sin(phase)+sv.im*cos(phase);}}
        }
        for(int sp=0;sp<VOL;sp++) Sp0[sp]=sqrt(Sp0_re[sp]*Sp0_re[sp]+Sp0_im[sp]*Sp0_im[sp]);
        free(src);free(tmp);free(sol);free(Sp0_re);free(Sp0_im);
    }
    
    /* Thermalize */
    double eps=0.3;
    for(int i=0;i<nthm;i++){int a=sweep(beta,eps);if(i<20&&(i+1)%5==0){if(a>60)eps*=1.1;if(a<40)eps*=0.9;}}
    
    /* Measure */
    double ZS_sum[5] = {0}, ZS_sum2[5] = {0};
    const char *labels[] = {"A1 (Higgs)", "T1 (3 gen)", "T2", "A2", "All"};
    int nsep = 20; /* sweeps between configs — needs to exceed autocorrelation time */
    for(int c=0;c<ncfg;c++){
        for(int i=0;i<nsep;i++)sweep(beta,eps);
        double ZS[5];
        measure_taste_ZS(mass, ZS, Sp0);
        for(int t=0;t<5;t++) { ZS_sum[t] += ZS[t]; ZS_sum2[t] += ZS[t]*ZS[t]; }
        
        if((c+1)%10==0||c==0||(c+1)==ncfg) {
            double t1_avg = ZS_sum[1]/(c+1);
            double t1_err = (c>0) ? sqrt((ZS_sum2[1]/(c+1) - t1_avg*t1_avg)/c) : 0;
            printf("  Cfg %3d: T1=%.4f  <T1>=%.4f±%.4f  → m_b/m_τ=%.3f±%.3f\n",
                   c+1, ZS[1], t1_avg, t1_err, 4.08*t1_avg, 4.08*t1_err);
        }
    }
    
    printf("\n================================================================\n");
    printf("RESULTS (L=%d, m=%.3f, %d configs, %d sep)\n", L, mass, ncfg, nsep);
    printf("================================================================\n");
    printf("  %-12s  S_int/S_free    err      4.08*ratio    err\n", "Taste");
    for(int t=0;t<5;t++) {
        double avg = ZS_sum[t]/ncfg;
        double err = (ncfg>1) ? sqrt((ZS_sum2[t]/ncfg - avg*avg)/(ncfg-1)) : 0;
        printf("  %-12s  %.4f       ±%.4f    %.3f       ±%.3f\n",
               labels[t], avg, err, 4.08*avg, 4.08*err);
    }
    printf("  Observed:                              2.352\n");
    printf("\n  Key: T1 is where the 3 physical generations live.\n");
    printf("  If T1 gives m_b/m_tau ~ 2.35, the matching is identified.\n");
    printf("================================================================\n");
    
    free(U); free(Sp0);
    return 0;
}
