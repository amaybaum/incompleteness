/*
 * OI-Induced SU(2) Gauge Theory HMC
 * ===================================
 * Same structure as oi_hmc.c but for SU(2).
 * N_f = 6 staggered fermions (same as SU(3), by Dynkin index equality).
 *
 * Compile: gcc -O3 -o oi_su2_hmc oi_su2_hmc.c -lm
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <complex.h>

#define NC 2
#define ND 4
#define MAX_CG 5000
#define CG_TOL 1e-10

typedef double complex su2_mat[NC][NC];

static int L = 4, VOL, NDOF, Nf = 6;
static double mass = 0.01, dt = 0.01;
static int nsteps = 20, ntraj = 200, ntherm = 100, nmeas = 5;

/* SU(2) matrix ops */
static void m2_unit(su2_mat A) { memset(A,0,sizeof(su2_mat)); A[0][0]=A[1][1]=1; }
static void m2_zero(su2_mat A) { memset(A,0,sizeof(su2_mat)); }
static void m2_copy(su2_mat d, const su2_mat s) { memcpy(d,s,sizeof(su2_mat)); }

static void m2_mul(su2_mat C, const su2_mat A, const su2_mat B) {
    su2_mat T;
    T[0][0]=A[0][0]*B[0][0]+A[0][1]*B[1][0];
    T[0][1]=A[0][0]*B[0][1]+A[0][1]*B[1][1];
    T[1][0]=A[1][0]*B[0][0]+A[1][1]*B[1][0];
    T[1][1]=A[1][0]*B[0][1]+A[1][1]*B[1][1];
    m2_copy(C,T);
}
static void m2_mul_dag(su2_mat C, const su2_mat A, const su2_mat B) {
    su2_mat T;
    T[0][0]=A[0][0]*conj(B[0][0])+A[0][1]*conj(B[0][1]);
    T[0][1]=A[0][0]*conj(B[1][0])+A[0][1]*conj(B[1][1]);
    T[1][0]=A[1][0]*conj(B[0][0])+A[1][1]*conj(B[0][1]);
    T[1][1]=A[1][0]*conj(B[1][0])+A[1][1]*conj(B[1][1]);
    m2_copy(C,T);
}
static double complex m2_trace(const su2_mat A) { return A[0][0]+A[1][1]; }

static void m2_project(su2_mat A) {
    double complex a0=(A[0][0]+A[1][1])*0.5;
    double complex a3=(A[0][0]-A[1][1])*0.5/I;
    double complex a1=(A[0][1]+A[1][0])*0.5/I;
    double complex a2=(A[0][1]-A[1][0])*0.5;
    double r0=creal(a0),r1=creal(a1),r2=creal(a2),r3=creal(a3);
    double n=sqrt(r0*r0+r1*r1+r2*r2+r3*r3);
    if(n<1e-15){m2_unit(A);return;}
    r0/=n;r1/=n;r2/=n;r3/=n;
    A[0][0]=r0+I*r3; A[0][1]=r2+I*r1;
    A[1][0]=-r2+I*r1; A[1][1]=r0-I*r3;
}

static void m2_exp_ah(su2_mat expA, const su2_mat A) {
    su2_mat An,T; m2_unit(expA); m2_copy(An,A);
    double f=1;
    for(int n=1;n<=12;n++){
        f*=n;
        for(int i=0;i<NC;i++)for(int j=0;j<NC;j++) expA[i][j]+=An[i][j]/f;
        m2_mul(T,An,A); m2_copy(An,T);
    }
    m2_project(expA);
}

static void m2_gauss_ah(su2_mat P) {
    double g[4];
    for(int i=0;i<4;i+=2){
        double u1=(double)rand()/RAND_MAX, u2=(double)rand()/RAND_MAX;
        if(u1<1e-15)u1=1e-15;
        double r=sqrt(-2*log(u1));
        g[i]=r*cos(2*M_PI*u2); g[i+1]=r*sin(2*M_PI*u2);
    }
    /* SU(2) Lie algebra: 3 generators (Pauli/2 × i) */
    m2_zero(P);
    P[0][1]=I*g[0]+g[1]; P[1][0]=I*g[0]-g[1];
    P[0][0]=I*g[2]; P[1][1]=-I*g[2];
    for(int i=0;i<NC;i++)for(int j=0;j<NC;j++) P[i][j]/=sqrt(2.0);
}

/* Geometry */
static int *fwd, *bwd;
static double *eta;

static void init_geometry(void) {
    VOL=1; for(int mu=0;mu<ND;mu++) VOL*=L;
    NDOF=VOL*NC;
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

/* Gauge field */
static su2_mat *U, *P_mom, *U_save;

static void init_gauge(int hot) {
    int NL=VOL*ND;
    U=(su2_mat*)malloc(NL*sizeof(su2_mat));
    P_mom=(su2_mat*)malloc(NL*sizeof(su2_mat));
    U_save=(su2_mat*)malloc(NL*sizeof(su2_mat));
    for(int i=0;i<NL;i++){
        if(hot){su2_mat H; m2_gauss_ah(H);
            for(int a=0;a<NC;a++)for(int b=0;b<NC;b++) H[a][b]*=3;
            m2_exp_ah(U[i],H);
        } else m2_unit(U[i]);
    }
}

/* Dirac operator */
static void dirac_op(double complex *y, const double complex *x) {
    memset(y,0,NDOF*sizeof(double complex));
    for(int i=0;i<VOL;i++){
        for(int mu=0;mu<ND;mu++){
            int ip=fwd[i*ND+mu],im=bwd[i*ND+mu];
            double e=eta[i*ND+mu];
            for(int a=0;a<NC;a++)
                for(int b=0;b<NC;b++){
                    y[i*NC+a]+=0.5*e*U[i*ND+mu][a][b]*x[ip*NC+b];
                    y[i*NC+a]-=0.5*e*conj(U[im*ND+mu][b][a])*x[im*NC+b];
                }
        }
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
        if(rsq<CG_TOL*rsq0 && rsq<CG_TOL) break;
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

/* Pseudofermion */
static double complex *phi;

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

/* Force */
static void ferm_force(su2_mat *F) {
    double complex *psi=(double complex*)malloc(NDOF*sizeof(double complex));
    double complex *chi=(double complex*)malloc(NDOF*sizeof(double complex));
    cg_solve(psi,phi); dirac_op(chi,psi);
    for(int n=0;n<VOL;n++){
        for(int mu=0;mu<ND;mu++){
            int np=fwd[n*ND+mu]; double e=eta[n*ND+mu]; int lk=n*ND+mu;
            double complex Upsi[NC],Uchi[NC];
            for(int a=0;a<NC;a++){
                Upsi[a]=0; Uchi[a]=0;
                for(int b=0;b<NC;b++){
                    Upsi[a]+=U[lk][a][b]*psi[np*NC+b];
                    Uchi[a]+=U[lk][a][b]*chi[np*NC+b];
                }
            }
            su2_mat M;
            for(int a=0;a<NC;a++)for(int b=0;b<NC;b++)
                M[a][b]=Nf*e*0.5*(Upsi[a]*conj(chi[n*NC+b])-Uchi[a]*conj(psi[n*NC+b]));
            /* Project to traceless anti-Hermitian */
            su2_mat Fah; double complex tr=0;
            for(int a=0;a<NC;a++)for(int b=0;b<NC;b++) Fah[a][b]=(M[a][b]-conj(M[b][a]))*0.5;
            for(int a=0;a<NC;a++) tr+=Fah[a][a];
            tr/=NC; for(int a=0;a<NC;a++) Fah[a][a]-=tr;
            m2_copy(F[lk],Fah);
        }
    }
    free(psi);free(chi);
}

/* Kinetic energy */
static double kin_energy(void) {
    double K=0; int NL=VOL*ND;
    for(int i=0;i<NL;i++)
        for(int a=0;a<NC;a++)for(int b=0;b<NC;b++)
            K+=creal(P_mom[i][a][b]*conj(P_mom[i][a][b]));
    return 0.5*K;
}

/* MD integrator */
static void md_integrate(void) {
    int NL=VOL*ND;
    su2_mat *F=(su2_mat*)malloc(NL*sizeof(su2_mat));
    ferm_force(F);
    for(int i=0;i<NL;i++)
        for(int a=0;a<NC;a++)for(int b=0;b<NC;b++) P_mom[i][a][b]+=0.5*dt*F[i][a][b];
    for(int step=0;step<nsteps;step++){
        for(int i=0;i<NL;i++){
            su2_mat dtP,expP,Unew;
            m2_copy(dtP,P_mom[i]);
            for(int a=0;a<NC;a++)for(int b=0;b<NC;b++) dtP[a][b]*=dt;
            m2_exp_ah(expP,dtP); m2_mul(Unew,expP,U[i]); m2_project(Unew); m2_copy(U[i],Unew);
        }
        ferm_force(F);
        double fdt=(step<nsteps-1)?dt:0.5*dt;
        for(int i=0;i<NL;i++)
            for(int a=0;a<NC;a++)for(int b=0;b<NC;b++) P_mom[i][a][b]+=fdt*F[i][a][b];
    }
    free(F);
}

/* Plaquette */
static double plaquette(void) {
    double plaq=0; int count=0;
    for(int n=0;n<VOL;n++)
        for(int mu=0;mu<ND;mu++)
            for(int nu=mu+1;nu<ND;nu++){
                int nm=fwd[n*ND+mu],nn_=fwd[n*ND+nu];
                su2_mat T1,T2,P_mat;
                m2_mul(T1,U[n*ND+mu],U[nm*ND+nu]);
                m2_mul_dag(T2,T1,U[nn_*ND+mu]);
                m2_mul_dag(P_mat,T2,U[n*ND+nu]);
                plaq+=creal(m2_trace(P_mat))/NC; count++;
            }
    return plaq/count;
}

/* Main */
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
    printf("OI-Induced SU(2) HMC: L=%d, Nf=%d, mass=%.4f\n",L,Nf,mass);
    printf("VOL=%d, NDOF=%d, dt=%.5f, nsteps=%d\n",VOL,NDOF,dt,nsteps);
    printf("ntraj=%d, ntherm=%d, %s start\n",ntraj,ntherm,hot?"HOT":"COLD");
    printf("Initial <P> = %.6f\n",plaquette());
    printf("================================================================\n\n");

    int accept=0; double psum=0; int pcount=0;
    time_t t0=time(NULL);

    for(int traj=1;traj<=ntherm+ntraj;traj++){
        int NL=VOL*ND;
        for(int i=0;i<NL;i++) m2_gauss_ah(P_mom[i]);
        gen_pf();
        double K0=kin_energy(), S0=ferm_action(), H0=K0+S0;
        memcpy(U_save,U,NL*sizeof(su2_mat));
        md_integrate();
        double K1=kin_energy(), S1=ferm_action(), H1=K1+S1;
        double dH=H1-H0;
        int acc=0;
        if(dH<0||(double)rand()/RAND_MAX<exp(-dH)){acc=1;accept++;}
        else memcpy(U,U_save,NL*sizeof(su2_mat));

        int is_m=(traj>ntherm)&&((traj-ntherm)%nmeas==0);
        if(is_m){double p=plaquette(); psum+=p; pcount++;}
        if(traj<=10||traj%10==0||is_m){
            double p=plaquette(); double el=difftime(time(NULL),t0);
            printf("Traj %4d/%d: <P>=%.6f dH=%+.2f %s [%.0fs]",
                   traj,ntherm+ntraj,p,dH,acc?"ACC":"REJ",el);
            if(pcount>0) printf("  avg=%.6f(%d)",psum/pcount,pcount);
            printf("\n"); fflush(stdout);
        }
    }

    double Pf=psum/pcount;
    double g2=4.0*NC*(1-Pf)/(NC*NC-1.0);
    double inv_a=4*M_PI/g2;
    double ln_r=log(1.221e19/91.188);
    double b2=-19.0/6;

    printf("\n================================================================\n");
    printf("SU(2) RESULTS (%d meas)\n",pcount);
    printf("================================================================\n");
    printf("Acceptance: %.1f%%\n",100.0*accept/(ntherm+ntraj));
    printf("<P> = %.6f\n",Pf);
    printf("g²_eff = %.6f\n",g2);
    printf("1/α₂(cutoff) = %.4f\n",inv_a);
    printf("RG: (b₂/2π)·ln(M_Pl/M_Z) = %.2f\n",b2/(2*M_PI)*ln_r);
    printf("1/α₂(M_Z) = %.2f  (observed: 29.57)\n",inv_a+b2/(2*M_PI)*ln_r);
    printf("================================================================\n");

    free(U);free(P_mom);free(U_save);free(phi);free(fwd);free(bwd);free(eta);
    return 0;
}
