/*
 * ward_chiral.c — Ward identity with L/R (even/odd sublattice) decomposition
 *
 * Decomposes condensate and effective mass by sublattice parity:
 *   L (even sites): the physical sector after trace-out
 *   R (odd sites): the hidden sector that's traced out
 *
 * If taste-breaking enters predominantly through the R sector,
 * then Z_S^L ~ 1 (physical Yukawa unmodified) and Z_S^R > 1
 * (hidden sector absorbs the taste-breaking).
 *
 * The physical y_b/y_tau is determined by the L-sector condensate.
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
static int parity(int s){int c[3]={s/(L*L),(s/L)%L,s%L};return(c[0]+c[1]+c[2])%2;}

static Mat mat_unit(void){Mat m;memset(&m,0,sizeof(m));for(int i=0;i<NC;i++)m.e[i][i]=cx(1,0);return m;}
static Mat mat_mul(Mat a,Mat b){Mat c;for(int i=0;i<NC;i++)for(int j=0;j<NC;j++){c.e[i][j]=cx(0,0);for(int k=0;k<NC;k++)c.e[i][j]=cxadd(c.e[i][j],cxmul(a.e[i][k],b.e[k][j]));}return c;}
static Mat mat_dag(Mat a){Mat b;for(int i=0;i<NC;i++)for(int j=0;j<NC;j++)b.e[i][j]=cxconj(a.e[j][i]);return b;}
static Mat mat_add(Mat a,Mat b){Mat c;for(int i=0;i<NC;i++)for(int j=0;j<NC;j++)c.e[i][j]=cxadd(a.e[i][j],b.e[i][j]);return c;}
static double mat_retr(Mat a){double t=0;for(int i=0;i<NC;i++)t+=a.e[i][i].re;return t;}
static Mat mat_proj(Mat a){Mat u;double n=0;for(int j=0;j<NC;j++)n+=cxabs2(a.e[0][j]);n=1.0/sqrt(n);for(int j=0;j<NC;j++)u.e[0][j]=cxscl(a.e[0][j],n);Cx d=cx(0,0);for(int j=0;j<NC;j++)d=cxadd(d,cxmul(cxconj(u.e[0][j]),a.e[1][j]));for(int j=0;j<NC;j++)u.e[1][j]=cxsub(a.e[1][j],cxmul(d,u.e[0][j]));n=0;for(int j=0;j<NC;j++)n+=cxabs2(u.e[1][j]);n=1.0/sqrt(n);for(int j=0;j<NC;j++)u.e[1][j]=cxscl(u.e[1][j],n);u.e[2][0]=cxsub(cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][2])),cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][1])));u.e[2][1]=cxsub(cxmul(cxconj(u.e[0][2]),cxconj(u.e[1][0])),cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][2])));u.e[2][2]=cxsub(cxmul(cxconj(u.e[0][0]),cxconj(u.e[1][1])),cxmul(cxconj(u.e[0][1]),cxconj(u.e[1][0])));return u;}
static Mat mat_rand(double eps){Mat h;for(int i=0;i<NC;i++)for(int j=i;j<NC;j++){if(i==j)h.e[i][j]=cx(gauss01()*eps,0);else{double r1=gauss01()*eps,r2=gauss01()*eps;h.e[i][j]=cx(r1,r2);h.e[j][i]=cx(r1,-r2);}}double tr=0;for(int i=0;i<NC;i++)tr+=h.e[i][i].re;tr/=NC;for(int i=0;i<NC;i++)h.e[i][i].re-=tr;Mat u=mat_unit();for(int i=0;i<NC;i++)for(int j=0;j<NC;j++)u.e[i][j]=cxadd(u.e[i][j],cx(-h.e[i][j].im,h.e[i][j].re));return mat_proj(u);}

static Mat staple(int s,int mu){Mat stap;memset(&stap,0,sizeof(stap));for(int nu=0;nu<DIM;nu++){if(nu==mu)continue;int smu=nbr(s,mu,+1),snu=nbr(s,nu,+1),smnu=nbr(s,nu,-1),smnu_mu=nbr(smnu,mu,+1);stap=mat_add(stap,mat_add(mat_mul(U[smu*DIM+nu],mat_mul(mat_dag(U[snu*DIM+mu]),mat_dag(U[s*DIM+nu]))),mat_mul(mat_dag(U[smnu_mu*DIM+nu]),mat_mul(mat_dag(U[smnu*DIM+mu]),U[smnu*DIM+nu]))));}return stap;}
static int sweep(double beta,double eps){int acc=0,tot=0;for(int s=0;s<VOL;s++)for(int mu=0;mu<DIM;mu++){double So=-(beta/NC)*mat_retr(mat_mul(U[s*DIM+mu],staple(s,mu)));Mat Uo=U[s*DIM+mu];U[s*DIM+mu]=mat_proj(mat_mul(mat_rand(eps),Uo));double Sn=-(beta/NC)*mat_retr(mat_mul(U[s*DIM+mu],staple(s,mu)));if(Sn-So<0||drand01()<exp(-(Sn-So)))acc++;else U[s*DIM+mu]=Uo;tot++;}return(100*acc)/tot;}

static void apply_D(Cx *dst, Cx *src, double mass) {
    for(int s=0;s<VOL;s++){
        for(int c=0;c<NC;c++) dst[s*NC+c]=cxscl(src[s*NC+c],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int c=0;c<NC;c++){
                Cx sum=cx(0,0);
                for(int c2=0;c2<NC;c2++) sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],src[sp*NC+c2]));
                dst[s*NC+c]=cxadd(dst[s*NC+c],cxscl(sum,ph));
            }
            for(int c=0;c<NC;c++){
                Cx sum=cx(0,0);
                for(int c2=0;c2<NC;c2++) sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),src[sm*NC+c2]));
                dst[s*NC+c]=cxsub(dst[s*NC+c],cxscl(sum,ph));
            }
        }
    }
}

static void apply_DdagD(Cx *dst, Cx *src, double mass) {
    int N=VOL*NC; Cx *tmp=malloc(N*sizeof(Cx));
    apply_D(tmp, src, mass);
    for(int s=0;s<VOL;s++){
        for(int c=0;c<NC;c++) dst[s*NC+c]=cxscl(tmp[s*NC+c],mass);
        for(int mu=0;mu<DIM;mu++){
            double ph=-eta(s,mu)*0.5;
            int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);
            for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],tmp[sp*NC+c2]));dst[s*NC+c]=cxadd(dst[s*NC+c],cxscl(sum,ph));}
            for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),tmp[sm*NC+c2]));dst[s*NC+c]=cxsub(dst[s*NC+c],cxscl(sum,ph));}
        }
    }
    free(tmp);
}

static int cg(Cx *x, Cx *b, double mass){
    int N=VOL*NC;Cx *r=malloc(N*sizeof(Cx)),*p=malloc(N*sizeof(Cx)),*Ap=malloc(N*sizeof(Cx));
    memset(x,0,N*sizeof(Cx));memcpy(r,b,N*sizeof(Cx));memcpy(p,b,N*sizeof(Cx));
    double rr=0;for(int i=0;i<N;i++)rr+=cxabs2(r[i]);double rr0=rr;if(rr0<1e-30){free(r);free(p);free(Ap);return 0;}
    int it;for(it=0;it<CG_MAX;it++){apply_DdagD(Ap,p,mass);double pAp=0;for(int i=0;i<N;i++)pAp+=Ap[i].re*p[i].re+Ap[i].im*p[i].im;if(fabs(pAp)<1e-30)break;double alpha=rr/pAp;for(int i=0;i<N;i++){x[i]=cxadd(x[i],cxscl(p[i],alpha));r[i]=cxsub(r[i],cxscl(Ap[i],alpha));}double rr_new=0;for(int i=0;i<N;i++)rr_new+=cxabs2(r[i]);if(rr_new/rr0<CG_TOL*CG_TOL){it++;break;}double bc=rr_new/rr;for(int i=0;i<N;i++)p[i]=cxadd(r[i],cxscl(p[i],bc));rr=rr_new;}
    free(r);free(p);free(Ap);return it;
}

/* Measure condensate decomposed by sublattice parity */
static void measure_condensate_LR(double mass, int nnoise,
                                   double *pbp_L, double *pbp_R) {
    int N = VOL*NC;
    Cx *eta_vec = malloc(N*sizeof(Cx));
    Cx *w = malloc(N*sizeof(Cx));
    Cx *Deta = malloc(N*sizeof(Cx));
    *pbp_L = 0; *pbp_R = 0;
    int nL = 0, nR = 0;
    for(int s=0;s<VOL;s++) { if(parity(s)==0) nL++; else nR++; }
    
    for(int hit=0; hit<nnoise; hit++) {
        for(int i=0; i<N; i++) eta_vec[i] = cx(drand01()>0.5?1:-1, 0);
        cg(w, eta_vec, mass);
        apply_D(Deta, eta_vec, mass);
        double dot_L=0, dot_R=0;
        for(int s=0; s<VOL; s++) {
            double dot_s = 0;
            for(int c=0; c<NC; c++) {
                int i = s*NC+c;
                dot_s += Deta[i].re*w[i].re + Deta[i].im*w[i].im;
            }
            if(parity(s)==0) dot_L += dot_s;
            else              dot_R += dot_s;
        }
        *pbp_L += dot_L / nL;
        *pbp_R += dot_R / nR;
    }
    *pbp_L /= nnoise;
    *pbp_R /= nnoise;
    free(eta_vec); free(w); free(Deta);
}

/* Measure correlator decomposed by sublattice parity */
static void measure_meff_LR(double mass, double *meff_full, 
                              double *meff_L, double *meff_R) {
    int N=VOL*NC;
    Cx *src=calloc(N,sizeof(Cx)),*tmp=malloc(N*sizeof(Cx)),*sol=malloc(N*sizeof(Cx));
    double *C_full=calloc(L,sizeof(double));
    double *C_L=calloc(L,sizeof(double));
    double *C_R=calloc(L,sizeof(double));
    
    for(int csrc=0;csrc<NC;csrc++){
        memset(src,0,N*sizeof(Cx)); src[csrc]=cx(1,0); /* source at origin (even site) */
        /* D† src */
        for(int s=0;s<VOL;s++){for(int c=0;c<NC;c++)tmp[s*NC+c]=cxscl(src[s*NC+c],mass);for(int mu=0;mu<DIM;mu++){double ph=-eta(s,mu)*0.5;int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],src[sp*NC+c2]));tmp[s*NC+c]=cxadd(tmp[s*NC+c],cxscl(sum,ph));}for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),src[sm*NC+c2]));tmp[s*NC+c]=cxsub(tmp[s*NC+c],cxscl(sum,ph));}}}
        cg(sol,tmp,mass);
        for(int s=0;s<VOL;s++){
            int z=s%L;
            double v2 = cxabs2(sol[s*NC+csrc]);
            C_full[z] += v2;
            if(parity(s)==0) C_L[z] += v2;
            else              C_R[z] += v2;
        }
    }
    *meff_full = (C_full[0]>0&&C_full[1]>0) ? -log(C_full[1]/C_full[0]) : 0;
    *meff_L    = (C_L[0]>0&&C_L[1]>0) ? -log(C_L[1]/C_L[0]) : 0;
    *meff_R    = (C_R[0]>0&&C_R[1]>0) ? -log(C_R[1]/C_R[0]) : 0;
    free(src);free(tmp);free(sol);free(C_full);free(C_L);free(C_R);
}

int main(int argc, char **argv) {
    L=argc>1?atoi(argv[1]):16;
    int ncfg=argc>2?atoi(argv[2]):20;
    int nthm=argc>3?atoi(argv[3]):100;
    double beta=argc>4?atof(argv[4]):11.10;
    double mass=argc>5?atof(argv[5]):0.20;
    int nnoise=8;
    
    srand(time(NULL)); VOL=L*L*L;
    U=malloc(VOL*DIM*sizeof(Mat));
    for(int i=0;i<VOL*DIM;i++) U[i]=mat_unit();
    
    printf("================================================================\n");
    printf("WARD CHIRAL: L/R decomposition, L=%d beta=%.2f m=%.3f\n",L,beta,mass);
    printf("================================================================\n");
    
    /* Free field */
    double pbpL0,pbpR0,meff0,meffL0,meffR0;
    measure_condensate_LR(mass,nnoise,&pbpL0,&pbpR0);
    measure_meff_LR(mass,&meff0,&meffL0,&meffR0);
    printf("Free: pbp_L=%.6f pbp_R=%.6f  meff=%.4f meff_L=%.4f meff_R=%.4f\n",
           pbpL0,pbpR0,meff0,meffL0,meffR0);
    printf("  pbp_L/pbp_R = %.4f (should be 1 for free field)\n\n",pbpL0/pbpR0);
    
    /* Thermalize */
    double eps=0.3;
    for(int i=0;i<nthm;i++){int a=sweep(beta,eps);if(i<20&&(i+1)%5==0){if(a>60)eps*=1.1;if(a<40)eps*=0.9;}}
    
    /* Measure */
    double sZSL=0,sZSR=0,sZSf=0,sZmL=0,sZmR=0,sZmf=0;
    int nsep=10;
    printf("  Cfg | ZS_L   ZS_R   ZS_full | Zm_L   Zm_R   Zm_full | ZS_L*Zm  ZS_R*Zm\n");
    for(int c=0;c<ncfg;c++){
        for(int i=0;i<nsep;i++) sweep(beta,eps);
        double pbpL,pbpR,meff,meffL,meffR;
        measure_condensate_LR(mass,nnoise,&pbpL,&pbpR);
        measure_meff_LR(mass,&meff,&meffL,&meffR);
        
        double ZSL=pbpL/pbpL0, ZSR=pbpR/pbpR0, ZSf=(pbpL+pbpR)/(pbpL0+pbpR0);
        double ZmL=(meffL0>0)?meffL/meffL0:0, ZmR=(meffR0>0)?meffR/meffR0:0;
        double Zmf=(meff0>0)?meff/meff0:0;
        
        sZSL+=ZSL; sZSR+=ZSR; sZSf+=ZSf;
        sZmL+=ZmL; sZmR+=ZmR; sZmf+=Zmf;
        
        if((c+1)%5==0||c==0)
            printf("  %3d | %.4f %.4f %.4f | %.4f %.4f %.4f | %.4f   %.4f\n",
                   c+1,ZSL,ZSR,ZSf,ZmL,ZmR,Zmf,ZSL*Zmf,ZSR*Zmf);
    }
    
    double aZSL=sZSL/ncfg,aZSR=sZSR/ncfg,aZSf=sZSf/ncfg;
    double aZmL=sZmL/ncfg,aZmR=sZmR/ncfg,aZmf=sZmf/ncfg;
    
    printf("\n================================================================\n");
    printf("RESULTS\n");
    printf("================================================================\n");
    printf("  Condensate Z_S:\n");
    printf("    L (even, physical): %.4f\n", aZSL);
    printf("    R (odd, traced out): %.4f\n", aZSR);
    printf("    Full:                %.4f\n", aZSf);
    printf("  Effective mass Z_m:\n");
    printf("    L (even): %.4f\n", aZmL);
    printf("    R (odd):  %.4f\n", aZmR);
    printf("    Full:     %.4f\n", aZmf);
    printf("  Ward identity:\n");
    printf("    Z_m(full) * Z_S(full) = %.4f\n", aZmf*aZSf);
    printf("    Z_m(full) * Z_S(L)    = %.4f\n", aZmf*aZSL);
    printf("    Z_m(full) * Z_S(R)    = %.4f\n", aZmf*aZSR);
    
    printf("\n  ---- Prediction ----\n");
    printf("  If physical Yukawa uses Z_S(L):\n");
    printf("    m_b/m_tau = 4.28/Z_S(L) = %.3f  (%+.1f%%)\n",
           4.28/aZSL, (4.28/aZSL/2.352-1)*100);
    printf("  If physical Yukawa uses Z_S(R):\n");
    printf("    m_b/m_tau = 4.28/Z_S(R) = %.3f  (%+.1f%%)\n",
           4.28/aZSR, (4.28/aZSR/2.352-1)*100);
    printf("  If physical Yukawa uses Z_S(full):\n");
    printf("    m_b/m_tau = 4.28/Z_S(full) = %.3f  (%+.1f%%)\n",
           4.28/aZSf, (4.28/aZSf/2.352-1)*100);
    printf("  Observed: 2.352\n");
    printf("================================================================\n");
    
    free(U);
    return 0;
}
