/*
 * rimom.c — RI-MOM scalar density Z_S at specific momentum scale
 *
 * Instead of the all-momenta condensate, compute Z_S(mu) from
 * the momentum-space propagator at |p| = mu.
 *
 * Method:
 *  1. Point source at origin → S(x,0) via CG
 *  2. Fourier transform → S_tilde(p) for all lattice momenta
 *  3. Define Sigma(p) = Tr[S_tilde(p)] / Tr[S_tilde_free(p)]
 *     This is the momentum-dependent "dressing factor"
 *  4. Z_S(mu) = average of Sigma(p) over momenta in shell |p| ~ mu
 *  5. Compare Z_S(mu) at different mu to the all-momenta Z_S
 *
 * The tree-level propagator: S_free(p) = m / (m^2 + sum sin^2(p_i))
 * The interacting propagator includes self-energy corrections.
 * The ratio at each p gives the local Z_S(p).
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
    int N=VOL*NC;
    Cx *tmp=malloc(N*sizeof(Cx));
    /* D */
    for(int s=0;s<VOL;s++){for(int c=0;c<NC;c++)tmp[s*NC+c]=cxscl(src[s*NC+c],mass);for(int mu=0;mu<DIM;mu++){double ph=eta(s,mu)*0.5;int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],src[sp*NC+c2]));tmp[s*NC+c]=cxadd(tmp[s*NC+c],cxscl(sum,ph));}for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),src[sm*NC+c2]));tmp[s*NC+c]=cxsub(tmp[s*NC+c],cxscl(sum,ph));}}}
    /* D† */
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

/* Compute propagator S(x,0) and Fourier transform to get S_tilde(p) */
static void measure_prop_mom(double mass, double *Sp_re, double *Sp_im) {
    /* Sp_re[s], Sp_im[s] = Tr[S_tilde(p_s)] where p_s = 2*pi*coords(s)/L */
    int N = VOL*NC;
    Cx *src = calloc(N, sizeof(Cx));
    Cx *tmp = malloc(N*sizeof(Cx));
    Cx *sol = malloc(N*sizeof(Cx));
    
    /* S(x,0) for each source color, then FT */
    memset(Sp_re, 0, VOL*sizeof(double));
    memset(Sp_im, 0, VOL*sizeof(double));
    
    for(int csrc = 0; csrc < NC; csrc++) {
        memset(src, 0, N*sizeof(Cx));
        src[csrc] = cx(1,0); /* point source at origin, color csrc */
        
        /* D† src */
        for(int s=0;s<VOL;s++){for(int c=0;c<NC;c++)tmp[s*NC+c]=cxscl(src[s*NC+c],mass);for(int mu=0;mu<DIM;mu++){double ph=-eta(s,mu)*0.5;int sp=nbr(s,mu,+1),sm=nbr(s,mu,-1);for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(U[s*DIM+mu].e[c][c2],src[sp*NC+c2]));tmp[s*NC+c]=cxadd(tmp[s*NC+c],cxscl(sum,ph));}for(int c=0;c<NC;c++){Cx sum=cx(0,0);for(int c2=0;c2<NC;c2++)sum=cxadd(sum,cxmul(cxconj(U[sm*DIM+mu].e[c2][c]),src[sm*NC+c2]));tmp[s*NC+c]=cxsub(tmp[s*NC+c],cxscl(sum,ph));}}}
        
        /* sol = (D†D)^{-1} D† src = D^{-1} src */
        cg(sol, tmp, mass);
        
        /* FT: S_tilde(p) = sum_x exp(-i p.x) S(x,0) */
        /* S(x,0)_{csrc,csrc} = sol[x*NC+csrc] (diagonal in color for point src) */
        for(int px=0; px<L; px++) for(int py=0; py<L; py++) for(int pz=0; pz<L; pz++) {
            int sp = px*L*L + py*L + pz; /* momentum index */
            double kx = 2*M_PI*px/L, ky = 2*M_PI*py/L, kz = 2*M_PI*pz/L;
            
            for(int xx=0; xx<L; xx++) for(int yy=0; yy<L; yy++) for(int zz=0; zz<L; zz++) {
                int sx = xx*L*L + yy*L + zz;
                double phase = -(kx*xx + ky*yy + kz*zz);
                double cp = cos(phase), sp2 = sin(phase);
                Cx sv = sol[sx*NC + csrc];
                Sp_re[sp] += sv.re*cp - sv.im*sp2;
                Sp_im[sp] += sv.re*sp2 + sv.im*cp;
            }
        }
    }
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
    printf("RI-MOM Z_S: L=%d beta=%.2f m=%.3f\n", L, beta, mass);
    printf("================================================================\n");
    
    /* Free-field propagator in momentum space */
    double *Sp0_re = calloc(VOL, sizeof(double));
    double *Sp0_im = calloc(VOL, sizeof(double));
    measure_prop_mom(mass, Sp0_re, Sp0_im);
    
    /* Bin momenta by |p|^2 */
    int nbins = 3*L*L/4 + 1;
    double *free_bin = calloc(nbins, sizeof(double));
    int *bin_count = calloc(nbins, sizeof(int));
    
    for(int px=0;px<L;px++) for(int py=0;py<L;py++) for(int pz=0;pz<L;pz++) {
        int sp = px*L*L+py*L+pz;
        int nx = px <= L/2 ? px : px-L;
        int ny = py <= L/2 ? py : py-L;
        int nz = pz <= L/2 ? pz : pz-L;
        int p2 = nx*nx + ny*ny + nz*nz;
        if(p2 < nbins) {
            free_bin[p2] += sqrt(Sp0_re[sp]*Sp0_re[sp] + Sp0_im[sp]*Sp0_im[sp]);
            bin_count[p2]++;
        }
    }
    
    printf("  Free-field |S(p)| by |p|^2:\n");
    for(int b=0;b<10&&b<nbins;b++) {
        if(bin_count[b]>0) {
            double phat2 = 0;
            /* compute sum sin^2(2*pi*n/L) for this bin */
            /* approximate: phat2 ~ (2*pi/L)^2 * b for small b */
            phat2 = b * (2*M_PI/L)*(2*M_PI/L);
            double Sfree_theory = NC * mass / (mass*mass + phat2);
            printf("    |p|^2=%d (n=%d): |S|=%.4f, theory=%.4f, ratio=%.4f\n",
                   b, bin_count[b], free_bin[b]/bin_count[b], 
                   Sfree_theory, (free_bin[b]/bin_count[b])/Sfree_theory);
        }
    }
    
    /* Thermalize */
    double eps=0.3;
    for(int i=0;i<nthm;i++){int a=sweep(beta,eps);if(i<20&&(i+1)%5==0){if(a>60)eps*=1.1;if(a<40)eps*=0.9;}}
    
    /* Measure */
    /* Accumulate ratio S_int(p)/S_free(p) in momentum bins */
    double *ratio_sum = calloc(nbins, sizeof(double));
    int *ratio_count = calloc(nbins, sizeof(int));
    int total_cfgs = 0;
    
    double *Sp_re = calloc(VOL, sizeof(double));
    double *Sp_im = calloc(VOL, sizeof(double));
    
    for(int c=0; c<ncfg; c++) {
        for(int i=0;i<5;i++) sweep(beta,eps);
        
        measure_prop_mom(mass, Sp_re, Sp_im);
        
        /* Compute ratio |S_int(p)| / |S_free(p)| for each momentum */
        for(int px=0;px<L;px++) for(int py=0;py<L;py++) for(int pz=0;pz<L;pz++) {
            int sp = px*L*L+py*L+pz;
            int nx = px<=L/2?px:px-L;
            int ny = py<=L/2?py:py-L;
            int nz = pz<=L/2?pz:pz-L;
            int p2 = nx*nx+ny*ny+nz*nz;
            
            double Sf = sqrt(Sp0_re[sp]*Sp0_re[sp]+Sp0_im[sp]*Sp0_im[sp]);
            double Si = sqrt(Sp_re[sp]*Sp_re[sp]+Sp_im[sp]*Sp_im[sp]);
            
            if(Sf > 1e-15 && p2 < nbins) {
                ratio_sum[p2] += Si/Sf;
                ratio_count[p2]++;
            }
        }
        total_cfgs++;
        
        if((c+1)%5==0||c==0) {
            /* Print Z_S at a few momentum scales */
            printf("  Cfg %2d:", c+1);
            for(int b=0; b<=3 && b<nbins; b++) {
                if(ratio_count[b]>0) {
                    double ZS = 1.0 / (ratio_sum[b]/ratio_count[b]);
                    printf(" ZS(p2=%d)=%.3f", b, ZS);
                }
            }
            printf("\n");
        }
    }
    
    printf("\n================================================================\n");
    printf("Z_S(mu) vs momentum scale (L=%d, %d configs)\n", L, ncfg);
    printf("================================================================\n");
    printf("  %6s %6s %8s %8s %10s\n", "|p|^2", "n_mom", "S_int/S0", "Z_S", "4.28*ratio");
    
    for(int b=0; b<nbins && b<=3*L; b++) {
        if(ratio_count[b] > 0) {
            double avg_ratio = ratio_sum[b] / ratio_count[b];
            double ZS = 1.0 / avg_ratio;          /* Z_S = S_free/S_int */
            /* m_b/m_tau = R_SM / Z_S, where R_SM = 4.28 is the 2-loop RGE factor
             * from M_Pl to M_Z for the SM (SM.md §7.5, line 844).
             * Since avg_ratio = S_int/S_free = 1/Z_S, 4.28 * avg_ratio = 4.28/Z_S. */
            double pred = 4.28 * avg_ratio;
            double phat = sqrt(b) * 2*M_PI/L;
            if(b <= 12) {
                printf("  %6d %6d %8.4f %8.4f %10.3f\n",
                       b, ratio_count[b]/total_cfgs, avg_ratio, ZS, pred);
            }
        }
    }
    
    /* All-momenta Z_S as a single number for comparison to k6_hmc.c's condensate.
     * Note: the RI-MOM cross-check is most useful at SPECIFIC |p|^2 bins
     * (especially |p|^2=5 at L=16 — see past session data), not the
     * all-momenta average, which includes BZ corners where staggered taste-
     * breaking makes the ratio scheme-dependent. */
    double avg_ratio_all = 0; int nb_used = 0;
    for(int b=1; b<nbins; b++) {  /* skip b=0 (zero mode) */
        if(ratio_count[b]>0 && bin_count[b]>0) {
            avg_ratio_all += ratio_sum[b]/ratio_count[b];
            nb_used++;
        }
    }
    if(nb_used>0) avg_ratio_all /= nb_used;
    double ZS_all = (avg_ratio_all>0) ? 1.0/avg_ratio_all : 0;
    printf("\n  All-|p| average ratio S_int/S_free = %.4f  →  Z_S = %.3f  →  m_b/m_tau = %.3f\n",
           avg_ratio_all, ZS_all, 4.28 * avg_ratio_all);
    printf("  Observed: 2.352\n");
    printf("  Note: this cross-check is most diagnostic at |p|^2=5 (24 momenta, away from zero and BZ corner).\n");
    
    free(U);free(Sp0_re);free(Sp0_im);free(Sp_re);free(Sp_im);
    free(free_bin);free(bin_count);free(ratio_sum);free(ratio_count);
    return 0;
}
