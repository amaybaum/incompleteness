/*
 * OI-Induced compact U(1) HMC
 * U(1) link = exp(iθ), one component per site.
 * Nf=6 staggered fermions (Dynkin index equality).
 * Compile: gcc -O3 -o oi_u1_hmc oi_u1_hmc.c -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <complex.h>

#define ND 4
#define MAX_CG 5000
#define CG_TOL 1e-10

static int L=4, VOL, NDOF, Nf=6;
static double mass=0.01, dt=0.01;
static int nsteps=20, ntraj=200, ntherm=100, nmeas=5;
static int *fwd,*bwd;
static double *eta;
static double complex *UL; /* U(1) links = exp(iθ) */
static double *P_mom;      /* Real momenta (conjugate to θ) */
static double complex *UL_save;
static double complex *phi;

static void init_geometry(void) {
    VOL=1; for(int mu=0;mu<ND;mu++) VOL*=L;
    NDOF=VOL; /* U(1): 1 color component per site */
    fwd=(int*)malloc(VOL*ND*sizeof(int));
    bwd=(int*)malloc(VOL*ND*sizeof(int));
    eta=(double*)malloc(VOL*ND*sizeof(double));
    for(int i=0;i<VOL;i++){
        int n[ND],tmp=i;
        for(int mu=ND-1;mu>=0;mu--){n[mu]=tmp%L;tmp/=L;}
        for(int mu=0;mu<ND;mu++){
            int nf[ND],nb[ND]; memcpy(nf,n,sizeof(n)); memcpy(nb,n,sizeof(n));
            nf[mu]=(n[mu]+1)%L; nb[mu]=(n[mu]-1+L)%L;
            int idx_f=0,idx_b=0;
            for(int d=0;d<ND;d++){idx_f=idx_f*L+nf[d];idx_b=idx_b*L+nb[d];}
            fwd[i*ND+mu]=idx_f; bwd[i*ND+mu]=idx_b;
            int sum=0; for(int nu=0;nu<mu;nu++) sum+=n[nu];
            eta[i*ND+mu]=(sum%2==0)?1.0:-1.0;
        }
    }
}

static void init_gauge(int hot) {
    int NL=VOL*ND;
    UL=(double complex*)malloc(NL*sizeof(double complex));
    P_mom=(double*)malloc(NL*sizeof(double));
    UL_save=(double complex*)malloc(NL*sizeof(double complex));
    for(int i=0;i<NL;i++)
        UL[i] = hot ? cexp(I*((double)rand()/RAND_MAX*2*M_PI)) : 1.0;
}

/* Dirac operator: D[i,j] = (1/2) Σ_μ η_μ(i) [U(i,μ) δ_{j,i+μ} - U*(i-μ,μ) δ_{j,i-μ}] */
static void dirac_op(double complex *y, const double complex *x) {
    memset(y,0,NDOF*sizeof(double complex));
    for(int i=0;i<VOL;i++)
        for(int mu=0;mu<ND;mu++){
            int ip=fwd[i*ND+mu], im=bwd[i*ND+mu];
            double e=eta[i*ND+mu];
            y[i] += 0.5*e*UL[i*ND+mu]*x[ip];
            y[i] -= 0.5*e*conj(UL[im*ND+mu])*x[im];
        }
}

static void DdagD_op(double complex *y, const double complex *x) {
    double complex *tmp=(double complex*)malloc(NDOF*sizeof(double complex));
    dirac_op(tmp,x); dirac_op(y,tmp);
    for(int i=0;i<NDOF;i++) y[i]=-y[i]+mass*mass*x[i];
    free(tmp);
}

static int cg_solve(double complex *x, const double complex *b) {
    double complex *r=(double complex*)malloc(NDOF*sizeof(double complex));
    double complex *p=(double complex*)malloc(NDOF*sizeof(double complex));
    double complex *Ap=(double complex*)malloc(NDOF*sizeof(double complex));
    memset(x,0,NDOF*sizeof(double complex));
    memcpy(r,b,NDOF*sizeof(double complex));
    memcpy(p,b,NDOF*sizeof(double complex));
    double rsq=0; for(int i=0;i<NDOF;i++) rsq+=creal(conj(r[i])*r[i]);
    double rsq0=rsq; int iter;
    for(iter=0;iter<MAX_CG;iter++){
        if(rsq<CG_TOL*rsq0&&rsq<CG_TOL) break;
        DdagD_op(Ap,p);
        double complex pAp=0; for(int i=0;i<NDOF;i++) pAp+=conj(p[i])*Ap[i];
        double complex alpha=rsq/pAp;
        double rsq_new=0;
        for(int i=0;i<NDOF;i++){x[i]+=alpha*p[i];r[i]-=alpha*Ap[i];rsq_new+=creal(conj(r[i])*r[i]);}
        double beta=rsq_new/rsq;
        for(int i=0;i<NDOF;i++) p[i]=r[i]+beta*p[i];
        rsq=rsq_new;
    }
    free(r);free(p);free(Ap); return iter;
}

static void gen_pf(void) {
    double complex *e_pf=(double complex*)malloc(NDOF*sizeof(double complex));
    for(int i=0;i<NDOF;i++){
        double u1=(double)rand()/RAND_MAX, u2=(double)rand()/RAND_MAX;
        if(u1<1e-15)u1=1e-15; double r=sqrt(-0.5*log(u1));
        e_pf[i]=r*cos(2*M_PI*u2)+I*r*sin(2*M_PI*u2);
    }
    dirac_op(phi,e_pf);
    for(int i=0;i<NDOF;i++) phi[i]+=mass*e_pf[i];
    free(e_pf);
}

static double ferm_action(void) {
    double complex *x=(double complex*)malloc(NDOF*sizeof(double complex));
    cg_solve(x,phi);
    double S=0; for(int i=0;i<NDOF;i++) S+=creal(conj(phi[i])*x[i]);
    free(x); return Nf*S;
}

/* U(1) force: F_μ(n) = Im[ Nf × η/2 × (U·ψ(n+μ)·χ*(n) - U·χ(n+μ)·ψ*(n)) ] */
static void ferm_force(double *F) {
    double complex *psi=(double complex*)malloc(NDOF*sizeof(double complex));
    double complex *chi=(double complex*)malloc(NDOF*sizeof(double complex));
    cg_solve(psi,phi); dirac_op(chi,psi);
    for(int n=0;n<VOL;n++)
        for(int mu=0;mu<ND;mu++){
            int np=fwd[n*ND+mu]; double e=eta[n*ND+mu]; int lk=n*ND+mu;
            double complex Upsi=UL[lk]*psi[np];
            double complex Uchi=UL[lk]*chi[np];
            double complex M=Nf*e*0.5*(Upsi*conj(chi[n])-Uchi*conj(psi[n]));
            F[lk]=cimag(M); /* Anti-Hermitian projection for U(1) */
        }
    free(psi);free(chi);
}

static double kin_energy(void) {
    double K=0; int NL=VOL*ND;
    for(int i=0;i<NL;i++) K+=P_mom[i]*P_mom[i];
    return 0.5*K;
}

static void md_integrate(void) {
    int NL=VOL*ND;
    double *F=(double*)malloc(NL*sizeof(double));
    ferm_force(F);
    for(int i=0;i<NL;i++) P_mom[i]+=0.5*dt*F[i];
    for(int step=0;step<nsteps;step++){
        for(int i=0;i<NL;i++){
            double theta=carg(UL[i])+dt*P_mom[i];
            UL[i]=cexp(I*theta);
        }
        ferm_force(F);
        double fdt=(step<nsteps-1)?dt:0.5*dt;
        for(int i=0;i<NL;i++) P_mom[i]+=fdt*F[i];
    }
    free(F);
}

static double u1_plaquette(void) {
    double plaq=0; int count=0;
    for(int n=0;n<VOL;n++)
        for(int mu=0;mu<ND;mu++)
            for(int nu=mu+1;nu<ND;nu++){
                int nm=fwd[n*ND+mu],nn_=fwd[n*ND+nu];
                double complex p=UL[n*ND+mu]*UL[nm*ND+nu]*conj(UL[nn_*ND+mu])*conj(UL[n*ND+nu]);
                plaq+=creal(p); count++;
            }
    return plaq/count;
}

int main(int argc, char *argv[]) {
    int hot=0;
    for(int i=1;i<argc;i++){
        if(!strcmp(argv[i],"-L")&&i+1<argc) L=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-Nf")&&i+1<argc) Nf=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-mass")&&i+1<argc) mass=atof(argv[++i]);
        else if(!strcmp(argv[i],"-dt")&&i+1<argc) dt=atof(argv[++i]);
        else if(!strcmp(argv[i],"-nsteps")&&i+1<argc) nsteps=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-ntraj")&&i+1<argc) ntraj=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-ntherm")&&i+1<argc) ntherm=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-nmeas")&&i+1<argc) nmeas=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-hot")) hot=1;
    }
    srand(time(NULL)); init_geometry(); init_gauge(hot);
    phi=(double complex*)malloc(NDOF*sizeof(double complex));

    printf("================================================================\n");
    printf("OI-Induced U(1) HMC: L=%d, Nf=%d, mass=%.4f\n",L,Nf,mass);
    printf("VOL=%d, NDOF=%d, dt=%.5f, nsteps=%d\n",VOL,NDOF,dt,nsteps);
    printf("================================================================\n\n");

    int accept=0; double psum=0; int pcount=0;
    time_t t0=time(NULL);

    for(int traj=1;traj<=ntherm+ntraj;traj++){
        int NL=VOL*ND;
        for(int i=0;i<NL;i++){
            double u1=(double)rand()/RAND_MAX, u2=(double)rand()/RAND_MAX;
            if(u1<1e-15)u1=1e-15;
            P_mom[i]=sqrt(-2*log(u1))*cos(2*M_PI*u2);
        }
        gen_pf();
        double K0=kin_energy(),S0=ferm_action(),H0=K0+S0;
        memcpy(UL_save,UL,NL*sizeof(double complex));
        md_integrate();
        double K1=kin_energy(),S1=ferm_action(),H1=K1+S1;
        double dH=H1-H0;
        int acc=0;
        if(dH<0||(double)rand()/RAND_MAX<exp(-dH)){acc=1;accept++;}
        else memcpy(UL,UL_save,NL*sizeof(double complex));

        int is_m=(traj>ntherm)&&((traj-ntherm)%nmeas==0);
        if(is_m){double p=u1_plaquette();psum+=p;pcount++;}
        if(traj<=10||traj%10==0||is_m){
            double p=u1_plaquette(); double el=difftime(time(NULL),t0);
            printf("Traj %4d/%d: <P>=%.6f dH=%+.4f %s [%.0fs]",
                   traj,ntherm+ntraj,p,dH,acc?"ACC":"REJ",el);
            if(pcount>0) printf("  avg=%.6f(%d)",psum/pcount,pcount);
            printf("\n"); fflush(stdout);
        }
    }

    double Pf=psum/pcount;
    double g2=2.0*(1-Pf); /* U(1): g²_eff = 2(1-P) */
    double inv_a=4*M_PI/g2;
    double ln_r=log(1.221e19/91.188);
    double b1=41.0/10;

    printf("\n================================================================\n");
    printf("U(1) RESULTS (%d meas)\n",pcount);
    printf("================================================================\n");
    printf("Acceptance: %.1f%%\n",100.0*accept/(ntherm+ntraj));
    printf("<P> = %.6f\n",Pf);
    printf("g²_eff = %.6f\n",g2);
    printf("1/α₁(cutoff) = %.4f\n",inv_a);
    printf("RG: (b₁/2π)·ln(M_Pl/M_Z) = %.2f\n",b1/(2*M_PI)*ln_r);
    printf("1/α₁(M_Z) = %.2f  (observed: 59.00)\n",inv_a+b1/(2*M_PI)*ln_r);
    printf("================================================================\n");

    free(UL);free(P_mom);free(UL_save);free(phi);free(fwd);free(bwd);free(eta);
    return 0;
}
