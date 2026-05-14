#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
static int Lc;
static inline int sidx(int x, int y, int z, int L) {
    return ((x%L+L)%L) + L*((y%L+L)%L) + L*L*((z%L+L)%L);
}
typedef uint64_t state_t;
static inline int get_now(state_t s, int i) { return (s >> (2*i)) & 1; }
static inline int get_prev(state_t s, int i) { return (s >> (2*i+1)) & 1; }
static state_t wstep(state_t s, int L) {
    state_t r = 0;
    for (int z=0; z<L; z++) for (int y=0; y<L; y++) for (int x=0; x<L; x++) {
        int i = sidx(x,y,z,L);
        int sum = get_now(s,sidx(x+1,y,z,L)) + get_now(s,sidx(x-1,y,z,L))
                + get_now(s,sidx(x,y+1,z,L)) + get_now(s,sidx(x,y-1,z,L))
                + get_now(s,sidx(x,y,z+1,L)) + get_now(s,sidx(x,y,z-1,L));
        int next = (sum + get_prev(s,i)) & 1;
        int now = get_now(s,i);
        r |= ((state_t)next) << (2*i);
        r |= ((state_t)now) << (2*i+1);
    }
    return r;
}
static uint64_t gcd_u(uint64_t a, uint64_t b) { while (b) { uint64_t t=a%b; a=b; b=t; } return a; }
static uint64_t lcm_u(uint64_t a, uint64_t b) { return a*b/gcd_u(a,b); }
int main(int argc, char *argv[]) {
    Lc = atoi(argv[1]);
    int L = Lc;
    int nb = 2*L*L*L;
    if (nb > 30) { fprintf(stderr, "too big\n"); return 1; }
    uint64_t N = 1ULL << nb;
    printf("=== 3D L=%d, 2^%d states ===\n", L, nb);
    unsigned char *vis = calloc(N/8+1, 1);
    uint64_t *cn = calloc(N+1, sizeof(uint64_t));
    uint64_t order=1, maxl=0, tot=0, num=0;
    clock_t t0 = clock();
    for (uint64_t s0=0; s0<N; s0++) {
        if (vis[s0/8] & (1u<<(s0%8))) continue;
        state_t s=s0; uint64_t len=0;
        do { vis[s/8] |= 1u<<(s%8); s = wstep(s,L); len++; } while (s != s0);
        cn[len]++; num++; tot += len; if (len>maxl) maxl=len;
        order = lcm_u(order, len);
    }
    printf("done %.2fs, %llu cycles, max=%llu, order=%llu\n",
        (double)(clock()-t0)/CLOCKS_PER_SEC,
        (unsigned long long)num, (unsigned long long)maxl, (unsigned long long)order);
    /* factor */
    printf("factorization: "); uint64_t n=order; int f=1;
    for (uint64_t p=2; p*p<=n; p++) {
        int e=0; while (n%p==0){n/=p;e++;}
        if (e) { if(!f) printf("*"); if(e==1) printf("%llu",(unsigned long long)p); else printf("%llu^%d",(unsigned long long)p,e); f=0; }
    }
    if (n>1) { if(!f) printf("*"); printf("%llu",(unsigned long long)n); }
    printf("\n");
    printf("cycle lengths:\n");
    for (uint64_t c=1; c<=maxl; c++) if (cn[c])
        printf("  %llu: %llu cycles\n", (unsigned long long)c, (unsigned long long)cn[c]);
    free(vis); free(cn);
    return 0;
}
