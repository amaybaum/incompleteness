/* A41 census enumerator (research; not a probe of any round).
 *
 * Domain D: E in {0,1}^{16x16}, row 0 = 0, such that SIG o u^E is complex Hadamard for every unit u, i.e. for every
 * row pair (i,i2) every level set of E_i - E_i2 has vanishing pair sum in SIG_i o conj(SIG_i2). For {0,1} rows with
 * the full pair sum zero (orthogonality) this is: the masks E_i & ~E_i2 and ~E_i & E_i2 both vanish.
 * All tables come from exact integer subset sums (export41.py): the test is exact.
 *
 * The search enumerates gauge classes of D: all-ones rows are excluded (an all-ones row is gauge-equivalent to the
 * zero row; the D-solutions of a class N are the 2^z choices on its z constant rows). Each class N (gauge normal form
 * N_i = E_i - E_i0) is tested for lexicographic minimality under H_dom (the 64 elements of the group with no
 * transposition whose row map fixes 0, with sign); only H_dom-minimal classes are canonicalized under the full group
 * (2048 = stabilizer x sign) and counted into the orbit table.
 *
 * Modes:  count        count D-solutions and gauge classes only (no group work)
 *         full         orbit census with checkpointing
 *         knuth S P    Knuth estimator, seed S, P probes
 *         dump         write every D-solution of the selected sub-domain (15 masks each) to stdout
 * Options: --allrows (keep all-ones rows; count mode only), --branches a:b (top-level branch index range),
 *          --state DIR (checkpoint dir), --fix r:mask (restrict row r to one mask; repeatable)
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <math.h>

typedef uint64_t u64;
static uint8_t *VAN[16][16];              /* VAN[i][i2] for i<i2: 65536 bytes */
static int NADM[16]; static uint16_t *ADM[16];
static u64 *COMP[16][16];                 /* COMP[i][r] : NADM[i] bitsets of WORDS[r] words */
static int WORDS[16];
static uint16_t GPERM[2048][256]; static int GSIGN[2048];
static uint8_t GINV[2048][256];           /* image[t] = sign * E[GINV[g][t]] */
static int HDOM[64], NHDOM = 0;
/* equations: [rel][struct] -> list */
typedef struct { int n; int idx[8]; int coef[8]; } Eq;
static Eq *EQS[2][18]; static int NEQ[2][18];

/* complete membership (all valid label matchings; 20 structures), from data41c.bin */
typedef struct { int n; Eq *e; } EqList;
typedef struct { EqList prop; int ng; int nvalid[16]; EqList *lam[16]; } CStruct;
static CStruct CS[2][32]; static int NCS = 0; static int COMPLETE = 0;
static void read_eqlist(FILE *f, EqList *L) {
    int32_t n; if (fread(&n, 4, 1, f) != 1) exit(30);
    L->n = n; L->e = calloc(n ? n : 1, sizeof(Eq));
    for (int e = 0; e < n; e++) {
        int32_t k; if (fread(&k, 4, 1, f) != 1 || k > 8) exit(31);
        L->e[e].n = k;
        for (int q = 0; q < k; q++) { int32_t a[2]; if (fread(a, 4, 2, f) != 2) exit(32); L->e[e].idx[q] = a[0]; L->e[e].coef[q] = a[1]; }
    }
}
static void load_complete(const char *path) {
    FILE *f = fopen(path, "rb"); if (!f) { perror(path); exit(33); }
    int32_t ns; if (fread(&ns, 4, 1, f) != 1 || ns > 32) exit(34); NCS = ns;
    for (int rel = 0; rel < 2; rel++) for (int s = 0; s < NCS; s++) {
        CStruct *c = &CS[rel][s]; read_eqlist(f, &c->prop);
        int32_t ng; if (fread(&ng, 4, 1, f) != 1) exit(35); c->ng = ng;
        for (int b = 0; b < ng; b++) {
            int32_t nv; if (fread(&nv, 4, 1, f) != 1) exit(36); c->nvalid[b] = nv; c->lam[b] = calloc(nv ? nv : 1, sizeof(EqList));
            for (int v = 0; v < nv; v++) read_eqlist(f, &c->lam[b][v]);
        }
    }
    fclose(f);
}
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }
static double T0;

static void load(const char *path) {
    FILE *f = fopen(path, "rb"); if (!f) { perror(path); exit(1); }
    for (int i = 0; i < 16; i++) for (int j = i + 1; j < 16; j++) {
        VAN[i][j] = malloc(65536); if (fread(VAN[i][j], 1, 65536, f) != 65536) exit(2);
    }
    for (int g = 0; g < 2048; g++) {
        if (fread(GPERM[g], 2, 256, f) != 256) exit(3);
        int16_t s; if (fread(&s, 2, 1, f) != 1) exit(3); GSIGN[g] = s;
        for (int t = 0; t < 256; t++) GINV[g][GPERM[g][t]] = (uint8_t)t;
    }
    for (int rel = 0; rel < 2; rel++) for (int s = 0; s < 18; s++) {
        int32_t n; if (fread(&n, 4, 1, f) != 1) exit(4);
        NEQ[rel][s] = n; EQS[rel][s] = calloc(n, sizeof(Eq));
        for (int e = 0; e < n; e++) {
            int32_t k; if (fread(&k, 4, 1, f) != 1) exit(4);
            if (k > 8) exit(5);
            EQS[rel][s][e].n = k;
            for (int q = 0; q < k; q++) { int32_t a[2]; if (fread(a, 4, 2, f) != 2) exit(4); EQS[rel][s][e].idx[q] = a[0]; EQS[rel][s][e].coef[q] = a[1]; }
        }
    }
    fclose(f);
    /* H_dom: no transposition (every row maps into one row) and row 0 -> row 0 */
    for (int g = 0; g < 2048; g++) {
        int ok = 1;
        for (int i = 0; i < 16 && ok; i++) { int r = GPERM[g][i * 16] / 16; for (int j = 1; j < 16; j++) if (GPERM[g][i * 16 + j] / 16 != r) { ok = 0; break; } }
        if (ok && GPERM[g][0] / 16 == 0) { if (NHDOM >= 64) { fprintf(stderr, "H_dom > 64\n"); exit(6); } HDOM[NHDOM++] = g; }
    }
    if (NHDOM != 64) { fprintf(stderr, "H_dom = %d\n", NHDOM); exit(6); }
}
static inline int van(int i, int i2, int m) { return i < i2 ? VAN[i][i2][m] : VAN[i2][i][m]; }

static int ALLROWS = 0, STATIC = 0;   /* STATIC: rows in index order instead of MRV (independent search tree) */
static int FIXMASK[16];                    /* -1 = free */
static void build_tables(void) {
    for (int i = 1; i < 16; i++) {
        ADM[i] = malloc(65536 * 2); NADM[i] = 0;
        for (int m = 0; m < 65536; m++) {
            if (!ALLROWS && m == 0xFFFF) continue;
            if (FIXMASK[i] >= 0 && m != FIXMASK[i]) continue;
            if (VAN[0][i][m] && VAN[0][i][0xFFFF ^ m]) ADM[i][NADM[i]++] = (uint16_t)m;
        }
        WORDS[i] = (NADM[i] + 63) / 64;
    }
    size_t tot = 0;
    for (int i = 1; i < 16; i++) for (int r = 1; r < 16; r++) {
        if (i == r) continue;
        size_t sz = (size_t)NADM[i] * WORDS[r];
        COMP[i][r] = calloc(sz ? sz : 1, 8); tot += sz * 8;
        for (int n = 0; n < NADM[i]; n++) {
            int a = ADM[i][n]; u64 *bs = COMP[i][r] + (size_t)n * WORDS[r];
            for (int k = 0; k < NADM[r]; k++) {
                int b = ADM[r][k];
                int m1 = a & ~b & 0xFFFF, m2 = ~a & b & 0xFFFF;
                if (van(i, r, m1) && van(i, r, m2)) bs[k >> 6] |= 1ULL << (k & 63);
            }
        }
    }
    fprintf(stderr, "tables: adm");
    for (int i = 1; i < 16; i++) fprintf(stderr, " %d", NADM[i]);
    fprintf(stderr, "; compat %.1f MB; %.1fs\n", tot / 1048576.0, now() - T0);
}

/* ---------------- canonical form ---------------- */
/* gauge normal form entries (i,j), i,j >= 1, in row-major order: 225 values in [-2,2] packed 3 bits (value+2) */
#define KW 11
typedef struct { u64 w[KW]; } Key;
static inline void pack(const int8_t *gn, Key *k) {
    memset(k, 0, sizeof(Key)); int p = 0;
    for (int i = 1; i < 16; i++) for (int j = 1; j < 16; j++, p++) {
        u64 v = (u64)(gn[i * 16 + j] + 2); k->w[(3 * p) >> 6] |= v << ((3 * p) & 63);
        if (((3 * p) & 63) > 61) k->w[((3 * p) >> 6) + 1] |= v >> (64 - ((3 * p) & 63));
    }
}
static inline void image_gn(int g, const int8_t *E, int8_t *out) {
    const uint8_t *iv = GINV[g]; int s = GSIGN[g];
    int8_t img[256];
    for (int t = 0; t < 256; t++) img[t] = (int8_t)(s * E[iv[t]]);
    for (int i = 0; i < 16; i++) for (int j = 0; j < 16; j++) out[i * 16 + j] = img[i * 16 + j] - img[i * 16] - img[j] + img[0];
}
/* compare gn(g.E) with best (a gauge-normal matrix) lexicographically; early exit. returns -1,0,1 */
static inline int cmp_image(int g, const int8_t *E, const int8_t *best) {
    const uint8_t *iv = GINV[g]; int s = GSIGN[g];
    int e00 = E[iv[0]];
    for (int i = 1; i < 16; i++) {
        int ei0 = E[iv[i * 16]];
        for (int j = 1; j < 16; j++) {
            int v = s * (E[iv[i * 16 + j]] - ei0 - E[iv[j]] + e00);
            int b = best[i * 16 + j];
            if (v != b) return v < b ? -1 : 1;
        }
    }
    return 0;
}
/* E gauge-normal (row 0 = col 0 = 0). canonical form over the 2048 elements into out (gauge normal) */
static void canon(const int8_t *E, int8_t *out) {
    memcpy(out, E, 256); int bg = -1;
    for (int g = 0; g < 2048; g++) {
        if (cmp_image(g, E, out) < 0) { image_gn(g, E, out); bg = g; }
    }
    (void)bg;
}
static int member(const int8_t *E, int rel, int s) {
    for (int e = 0; e < NEQ[rel][s]; e++) {
        const Eq *q = &EQS[rel][s][e]; int acc = 0;
        for (int k = 0; k < q->n; k++) acc += q->coef[k] * E[q->idx[k]];
        if (acc) return 0;
    }
    return 1;
}
static inline int eqs_ok(const int8_t *E, const EqList *L) {
    for (int e = 0; e < L->n; e++) { const Eq *q = &L->e[e]; int acc = 0; for (int k = 0; k < q->n; k++) acc += q->coef[k] * E[q->idx[k]]; if (acc) return 0; }
    return 1;
}
static int member_complete(const int8_t *E, int rel, int s) {
    const CStruct *c = &CS[rel][s];
    if (!eqs_ok(E, &c->prop)) return 0;
    for (int b = 0; b < c->ng; b++) {
        int any = 0; for (int v = 0; v < c->nvalid[b] && !any; v++) any = eqs_ok(E, &c->lam[b][v]);
        if (!any) return 0;
    }
    return 1;
}
static int member_mask(const int8_t *E, int rel) {
    int m = 0;
    if (COMPLETE) { for (int s = 0; s < NCS; s++) if (member_complete(E, rel, s)) m |= 1 << s; }
    else for (int s = 0; s < 18; s++) if (member(E, rel, s)) m |= 1 << s;
    return m;
}

/* ---------------- orbit table ---------------- */
typedef struct {
    Key key; uint16_t first[16];           /* first-found D-solution (row masks) */
    uint64_t n_sol, n_gauge, n_strict, n_hrep, n_strict18;
    uint32_t relmask_canon, strictmask_union;
    uint16_t min_dsupp, canon_nnz, min_gn_nnz, orbit_gauge; uint8_t used, pad[7];
} Rec;
static Rec *TAB = NULL; static size_t TCAP = 0, TN = 0;
static inline u64 khash(const Key *k) { u64 h = 1469598103934665603ULL; for (int i = 0; i < KW; i++) { h ^= k->w[i]; h *= 1099511628211ULL; h ^= h >> 29; } return h; }
static Rec *tab_find(const Key *k, int *isnew) {
    if (TN * 2 >= TCAP) {
        size_t nc = TCAP ? TCAP * 2 : (1 << 20); Rec *nt = calloc(nc, sizeof(Rec)); if (!nt) { fprintf(stderr, "OOM table\n"); exit(9); }
        for (size_t x = 0; x < TCAP; x++) if (TAB[x].used) {
            size_t h = khash(&TAB[x].key) & (nc - 1); while (nt[h].used) h = (h + 1) & (nc - 1); nt[h] = TAB[x];
        }
        free(TAB); TAB = nt; TCAP = nc;
    }
    size_t h = khash(k) & (TCAP - 1);
    while (TAB[h].used) { if (!memcmp(&TAB[h].key, k, sizeof(Key))) { *isnew = 0; return &TAB[h]; } h = (h + 1) & (TCAP - 1); }
    TAB[h].used = 1; TAB[h].key = *k; TN++; *isnew = 1; return &TAB[h];
}

/* ---------------- statistics ---------------- */
static u64 CNT_SOL = 0, CNT_GAUGE = 0, CNT_HREP = 0, CNT_STRICT = 0, CNT_RELAX_NONSTRICT_SOL = 0, CNT_NON_SOL = 0;
static u64 CNT_STRICT18 = 0, CNT_NON18_SOL = 0, CNT_RELAXONLY18_SOL = 0, CTRL_RELAX_POPC_MISMATCH = 0, CTRL_RELAX_MISMATCH18 = 0;
static u64 CTRL_RELAX_MISMATCH = 0, CTRL_CANON_NOT_IDEMP = 0, CTRL_CANON_CHECKED = 0;
static int MODE = 0; /* 0 count, 1 full, 2 knuth, 3 dump, 4 classify */
static u64 LIMIT = ~0ULL;

static int cmp_key(const void *a, const void *b) { return memcmp(a, b, 256); }

static void process_leaf(const uint16_t *rows) {
    int z = 0;
    for (int i = 1; i < 16; i++) if (rows[i] == 0 || rows[i] == 0xFFFF) z++;
    if (MODE == 0) { CNT_GAUGE++; CNT_SOL += ALLROWS ? 1 : (1ULL << z); return; }
    if (MODE == 3) { for (int i = 1; i < 16; i++) printf("%d%c", rows[i], i == 15 ? '\n' : ' '); CNT_SOL++; return; }
    if (MODE == 4) {   /* per-solution classification in enumeration order (act 38 dfs2 comparison) */
        int8_t E[256]; for (int j = 0; j < 16; j++) E[j] = 0;
        for (int i = 1; i < 16; i++) for (int j = 0; j < 16; j++) E[i * 16 + j] = (int8_t)((rows[i] >> j) & 1);
        int sm = member_mask(E, 0), rm = member_mask(E, 1);
        CNT_SOL++; if (!sm && rm) CNT_RELAX_NONSTRICT_SOL++; if (!sm && !rm) CNT_NON_SOL++; if (sm) CNT_STRICT++;
        if (CNT_SOL == LIMIT) {
            printf("CLASSIFY first %llu solutions: strict %llu strictly-outside-but-relaxed %llu outside-every-relaxed %llu\n", (unsigned long long)CNT_SOL,
                   (unsigned long long)CNT_STRICT, (unsigned long long)CNT_RELAX_NONSTRICT_SOL, (unsigned long long)CNT_NON_SOL);
            exit(0);
        }
        return;
    }
    CNT_GAUGE++;
    int8_t N[256];
    for (int j = 0; j < 16; j++) N[j] = 0;
    for (int i = 1; i < 16; i++) { int b0 = rows[i] & 1; for (int j = 0; j < 16; j++) N[i * 16 + j] = (int8_t)(((rows[i] >> j) & 1) - b0); }
    /* H_dom minimality */
    int ties = 0;
    for (int h = 0; h < 64; h++) {
        int c = cmp_image(HDOM[h], N, N);
        if (c < 0) return;
        if (c == 0) ties++;
    }
    CNT_HREP++;
    /* distinct H_dom images of N and their D-solutions */
    static int8_t imgs[64][256]; int nimg = 0;
    for (int h = 0; h < 64; h++) {
        int8_t M[256]; image_gn(HDOM[h], N, M);
        int dup = 0; for (int x = 0; x < nimg; x++) if (!memcmp(imgs[x], M, 256)) { dup = 1; break; }
        if (!dup) memcpy(imgs[nimg++], M, 256);
    }
    if (nimg * ties != 64) { fprintf(stderr, "orbit-stabilizer mismatch %d * %d\n", nimg, ties); exit(11); }
    u64 nsol = 0, nstrict = 0, nstrict18 = 0; uint32_t smask_union = 0; int mind = 999;
    int rmN = member_mask(N, 1); int relN = rmN != 0, rel18N = (rmN & 0x3FFFF) != 0;
    for (int x = 0; x < nimg; x++) {
        int8_t E[256]; int zr[16], nz = 0, supp = 0;
        for (int i = 0; i < 16; i++) {
            int lo = 0, hi = 0;
            for (int j = 0; j < 16; j++) { int v = imgs[x][i * 16 + j]; if (v < lo) lo = v; if (v > hi) hi = v; }
            if (hi - lo > 1) { fprintf(stderr, "H_dom image outside the domain\n"); exit(12); }
            for (int j = 0; j < 16; j++) { E[i * 16 + j] = (int8_t)(imgs[x][i * 16 + j] - lo); supp += E[i * 16 + j]; }
            if (i > 0 && lo == 0 && hi == 0) zr[nz++] = i;
        }
        if (supp < mind) mind = supp;
        { int rm = member_mask(E, 1); if ((rm != 0) != relN) CTRL_RELAX_MISMATCH++; if (((rm & 0x3FFFF) != 0) != rel18N) CTRL_RELAX_MISMATCH18++;
          if (__builtin_popcount(rm) != __builtin_popcount(rmN)) CTRL_RELAX_POPC_MISMATCH++; }
        for (u64 F = 0; F < (1ULL << nz); F++) {
            for (int q = 0; q < nz; q++) { int v = (F >> q) & 1; for (int j = 0; j < 16; j++) E[zr[q] * 16 + j] = (int8_t)v; }
            int sm = member_mask(E, 0);
            nsol++; if (sm) { nstrict++; smask_union |= sm; } if (sm & 0x3FFFF) nstrict18++;
        }
        for (int q = 0; q < nz; q++) for (int j = 0; j < 16; j++) E[zr[q] * 16 + j] = 0;
    }
    CNT_SOL += nsol; CNT_STRICT += nstrict;
    if (!relN) CNT_NON_SOL += nsol; else CNT_RELAX_NONSTRICT_SOL += nsol - nstrict;
    CNT_STRICT18 += nstrict18; if (!rel18N) CNT_NON18_SOL += nsol; else CNT_RELAXONLY18_SOL += nsol - nstrict18;
    /* full canonical form */
    int8_t C[256]; canon(N, C);
    Key k; pack(C, &k); int isnew;
    Rec *r = tab_find(&k, &isnew);
    if (isnew) {
        memcpy(r->first, rows, 32); r->first[0] = 0;
        r->relmask_canon = member_mask(C, 1);
        if ((r->relmask_canon != 0) != relN) CTRL_RELAX_MISMATCH++;
        if (((r->relmask_canon & 0x3FFFF) != 0) != rel18N) CTRL_RELAX_MISMATCH18++;
        if (__builtin_popcount(r->relmask_canon) != __builtin_popcount(rmN)) CTRL_RELAX_POPC_MISMATCH++;
        int nnz = 0; for (int t = 0; t < 256; t++) nnz += C[t] != 0; r->canon_nnz = nnz;
        /* all 2048 gauge normal images: distinct count, min nonzeros, idempotence of the canonical form */
        static int8_t all[2048][256]; int mn = 999;
        for (int g = 0; g < 2048; g++) {
            image_gn(g, N, all[g]); int c = 0; for (int t = 0; t < 256; t++) c += all[g][t] != 0; if (c < mn) mn = c;
        }
        qsort(all, 2048, 256, cmp_key);
        int d = 1; for (int g = 1; g < 2048; g++) if (memcmp(all[g], all[g - 1], 256)) d++;
        r->min_gn_nnz = mn; r->orbit_gauge = d;
        /* idempotence control: canon of the canonical form, and of a random image, equal C */
        int8_t C2[256]; canon(C, C2); if (memcmp(C, C2, 256)) CTRL_CANON_NOT_IDEMP++;
        int8_t Y[256]; image_gn((int)(khash(&k) % 2048), N, Y); canon(Y, C2); if (memcmp(C, C2, 256)) CTRL_CANON_NOT_IDEMP++;
        CTRL_CANON_CHECKED++;
        r->min_dsupp = 999;
    }
    r->n_sol += nsol; r->n_gauge += nimg; r->n_strict += nstrict; r->n_strict18 += nstrict18; r->n_hrep++; r->strictmask_union |= smask_union;
    if (mind < r->min_dsupp) r->min_dsupp = mind;
}

/* ---------------- DFS ---------------- */
static u64 NODES = 0;
static u64 dombuf[16][16][202];            /* [depth][row][words] */
static uint16_t CUR[16];
static int CHOSEN[16];
static int popc(const u64 *b, int w) { int c = 0; for (int x = 0; x < w; x++) c += __builtin_popcountll(b[x]); return c; }

static void rec(int depth) {
    NODES++;
    int best = -1, bc = 1 << 30, nfree = 0;
    for (int r = 1; r < 16; r++) if (!CHOSEN[r]) { nfree++; int c = STATIC ? r : popc(dombuf[depth][r], WORDS[r]); if (c < bc) { bc = c; best = r; } }
    int i = best; u64 *di = dombuf[depth][i];
    if (nfree == 1) {
        for (int w = 0; w < WORDS[i]; w++) { u64 x = di[w]; while (x) { int b = __builtin_ctzll(x); x &= x - 1; CUR[i] = ADM[i][w * 64 + b]; process_leaf(CUR); } }
        return;
    }
    CHOSEN[i] = 1;
    for (int w = 0; w < WORDS[i]; w++) {
        u64 x = di[w];
        while (x) {
            int b = __builtin_ctzll(x); x &= x - 1; int n = w * 64 + b;
            int ok = 1;
            for (int r = 1; r < 16 && ok; r++) {
                if (CHOSEN[r]) continue;
                const u64 *cp = COMP[i][r] + (size_t)n * WORDS[r]; const u64 *d = dombuf[depth][r]; u64 *nd = dombuf[depth + 1][r];
                u64 any = 0; for (int q = 0; q < WORDS[r]; q++) { nd[q] = d[q] & cp[q]; any |= nd[q]; }
                if (!any) ok = 0;
            }
            if (!ok) continue;
            CUR[i] = ADM[i][n]; rec(depth + 1);
        }
    }
    CHOSEN[i] = 0;
}

/* ---------------- Knuth estimator (same MRV order) ---------------- */
static u64 rng_s;
static u64 rnd(void) { rng_s ^= rng_s << 13; rng_s ^= rng_s >> 7; rng_s ^= rng_s << 17; return rng_s; }
static double knuth_probe(void) {
    double wgt = 1; int depth = 0; int chosen[16] = {0};
    for (int r = 1; r < 16; r++) memcpy(dombuf[1][r], dombuf[0][r], 8 * WORDS[r]);
    depth = 1;
    static u64 kids[1][1];
    (void)kids;
    static int goodn[13000];
    while (1) {
        int best = -1, bc = 1 << 30, nfree = 0;
        for (int r = 1; r < 16; r++) if (!chosen[r]) { nfree++; int c = popc(dombuf[depth][r], WORDS[r]); if (c < bc) { bc = c; best = r; } }
        int i = best;
        if (nfree == 1) return wgt * bc;
        int ng = 0;
        for (int n = 0; n < NADM[i]; n++) {
            if (!((dombuf[depth][i][n >> 6] >> (n & 63)) & 1)) continue;
            int ok = 1;
            for (int r = 1; r < 16 && ok; r++) {
                if (chosen[r] || r == i) continue;
                const u64 *cp = COMP[i][r] + (size_t)n * WORDS[r]; const u64 *d = dombuf[depth][r]; u64 any = 0;
                for (int q = 0; q < WORDS[r]; q++) any |= d[q] & cp[q];
                if (!any) ok = 0;
            }
            if (ok) goodn[ng++] = n;
        }
        if (!ng) return 0;
        wgt *= ng; int n = goodn[rnd() % ng];
        for (int r = 1; r < 16; r++) {
            if (chosen[r] || r == i) continue;
            const u64 *cp = COMP[i][r] + (size_t)n * WORDS[r];
            for (int q = 0; q < WORDS[r]; q++) dombuf[depth + 1][r][q] = dombuf[depth][r][q] & cp[q];
        }
        chosen[i] = 1; depth++;
    }
}

/* ---------------- checkpointing ---------------- */
static char STATE[512] = "";
static void save_state(int next_branch, int b_end) {
    char tmp[600], fin[600];
    snprintf(tmp, sizeof tmp, "%s/state.tmp", STATE); snprintf(fin, sizeof fin, "%s/state.bin", STATE);
    FILE *f = fopen(tmp, "wb"); if (!f) { perror(tmp); exit(20); }
    u64 hdr[24] = { 0x41434e54, (u64)next_branch, (u64)b_end, TN, CNT_SOL, CNT_GAUGE, CNT_HREP, CNT_STRICT, CNT_RELAX_NONSTRICT_SOL, CNT_NON_SOL, CTRL_RELAX_MISMATCH, CTRL_CANON_NOT_IDEMP, CTRL_CANON_CHECKED, NODES, (u64)COMPLETE, (u64)NCS,
                    CNT_STRICT18, CNT_NON18_SOL, CNT_RELAXONLY18_SOL, CTRL_RELAX_POPC_MISMATCH, CTRL_RELAX_MISMATCH18, sizeof(Rec), 0, 0 };
    fwrite(hdr, 8, 24, f);
    for (size_t x = 0; x < TCAP; x++) if (TAB[x].used) fwrite(&TAB[x], sizeof(Rec), 1, f);
    fflush(f); fsync(fileno(f)); fclose(f); rename(tmp, fin);
}
static int load_state(int *next_branch) {
    char fin[600]; snprintf(fin, sizeof fin, "%s/state.bin", STATE);
    FILE *f = fopen(fin, "rb"); if (!f) return 0;
    u64 hdr[24]; if (fread(hdr, 8, 24, f) != 24 || hdr[0] != 0x41434e54 || hdr[14] != (u64)COMPLETE) { fprintf(stderr, "bad state\n"); exit(21); }
    CNT_STRICT18 = hdr[16]; CNT_NON18_SOL = hdr[17]; CNT_RELAXONLY18_SOL = hdr[18]; CTRL_RELAX_POPC_MISMATCH = hdr[19]; CTRL_RELAX_MISMATCH18 = hdr[20];
    *next_branch = (int)hdr[1]; CNT_SOL = hdr[4]; CNT_GAUGE = hdr[5]; CNT_HREP = hdr[6]; CNT_STRICT = hdr[7]; CNT_RELAX_NONSTRICT_SOL = hdr[8]; CNT_NON_SOL = hdr[9];
    CTRL_RELAX_MISMATCH = hdr[10]; CTRL_CANON_NOT_IDEMP = hdr[11]; CTRL_CANON_CHECKED = hdr[12]; NODES = hdr[13];
    u64 n = hdr[3]; Rec r;
    for (u64 x = 0; x < n; x++) { if (fread(&r, sizeof(Rec), 1, f) != 1) exit(22); int isnew; Rec *p = tab_find(&r.key, &isnew); *p = r; }
    fclose(f); return 1;
}

int main(int argc, char **argv) {
    T0 = now();
    const char *mode = argc > 1 ? argv[1] : "count";
    int b_lo = 0, b_hi = 1 << 30; u64 seed = 1; long probes = 1000;
    for (int r = 0; r < 16; r++) FIXMASK[r] = -1;
    for (int a = 2; a < argc; a++) {
        if (!strcmp(argv[a], "--allrows")) ALLROWS = 1;
        else if (!strcmp(argv[a], "--branches")) { sscanf(argv[++a], "%d:%d", &b_lo, &b_hi); }
        else if (!strcmp(argv[a], "--state")) { snprintf(STATE, sizeof STATE, "%s", argv[++a]); }
        else if (!strcmp(argv[a], "--fix")) { int r, m; sscanf(argv[++a], "%d:%d", &r, &m); FIXMASK[r] = m; }
        else if (!strcmp(argv[a], "--seed")) seed = strtoull(argv[++a], 0, 10);
        else if (!strcmp(argv[a], "--probes")) probes = strtol(argv[++a], 0, 10);
        else if (!strcmp(argv[a], "--complete")) COMPLETE = 1;
        else if (!strcmp(argv[a], "--static")) STATIC = 1;
        else if (!strcmp(argv[a], "--limit")) LIMIT = strtoull(argv[++a], 0, 10);
    }
    MODE = !strcmp(mode, "count") ? 0 : !strcmp(mode, "full") ? 1 : !strcmp(mode, "knuth") ? 2 : !strcmp(mode, "dump") ? 3 : !strcmp(mode, "classify") ? 4 : -1;
    if (MODE < 0) { fprintf(stderr, "unknown mode\n"); return 1; }
    if (MODE == 1 && ALLROWS) { fprintf(stderr, "full mode enumerates gauge classes (no --allrows)\n"); return 1; }
    load(argc > 0 ? "data41.bin" : "");
    if (COMPLETE) { load_complete("data41c.bin"); fprintf(stderr, "complete membership: %d structures\n", NCS); }
    build_tables();
    for (int r = 1; r < 16; r++) { memset(dombuf[0][r], 0, 8 * WORDS[r]); for (int n = 0; n < NADM[r]; n++) dombuf[0][r][n >> 6] |= 1ULL << (n & 63); }
    if (MODE == 2) {
        rng_s = seed * 0x9E3779B97F4A7C15ULL + 1; double s = 0, s2 = 0, mx = 0;
        for (long p = 0; p < probes; p++) { double e = knuth_probe(); s += e; s2 += e * e; if (e > mx) mx = e; }
        double m = s / probes, sd = sqrt(s2 / probes - m * m);
        printf("KNUTH seed %llu probes %ld mean %.6g stderr %.3g max %.3g %.0fs\n", (unsigned long long)seed, probes, m, sd / sqrt((double)probes), mx, now() - T0);
        return 0;
    }
    /* top level: the MRV row at the root; branches are its candidates in order */
    int i0 = -1, bc = 1 << 30;
    for (int r = 1; r < 16; r++) { int c = STATIC ? r : NADM[r]; if (c < bc) { bc = c; i0 = r; } }
    int nb = NADM[i0]; if (b_hi > nb) b_hi = nb;
    int start = b_lo;
    if (MODE == 1 && STATE[0]) { int nbr; if (load_state(&nbr)) { start = nbr; fprintf(stderr, "resumed at branch %d, orbits %zu\n", start, TN); } }
    fprintf(stderr, "top row %d, branches [%d,%d) of %d\n", i0, start, b_hi, nb);
    double tlast = now();
    CHOSEN[i0] = 1;
    for (int n = start; n < b_hi; n++) {
        int ok = 1;
        for (int r = 1; r < 16 && ok; r++) {
            if (r == i0) continue;
            const u64 *cp = COMP[i0][r] + (size_t)n * WORDS[r]; u64 any = 0;
            for (int q = 0; q < WORDS[r]; q++) { dombuf[1][r][q] = dombuf[0][r][q] & cp[q]; any |= dombuf[1][r][q]; }
            if (!any) ok = 0;
        }
        if (ok) { CUR[i0] = ADM[i0][n]; rec(1); }
        if (MODE == 1 && STATE[0] && (now() - tlast > 600 || n + 1 == b_hi)) { save_state(n + 1, b_hi); tlast = now(); }
        fprintf(stderr, "branch %d/%d mask %d done: sol %llu gauge %llu hrep %llu orbits %zu strict %llu relaxonly %llu non %llu nodes %llu %.0fs\n",
                n, nb, ADM[i0][n], (unsigned long long)CNT_SOL, (unsigned long long)CNT_GAUGE, (unsigned long long)CNT_HREP, TN,
                (unsigned long long)CNT_STRICT, (unsigned long long)CNT_RELAX_NONSTRICT_SOL, (unsigned long long)CNT_NON_SOL, (unsigned long long)NODES, now() - T0);
    }
    printf("DONE mode %s branches [%d,%d) sol %llu gauge %llu hrep %llu orbits %zu strict %llu relaxonly %llu non %llu nodes %llu ctrl_relax_mismatch %llu ctrl_canon_not_idemp %llu/%llu %.0fs\n",
           mode, b_lo, b_hi, (unsigned long long)CNT_SOL, (unsigned long long)CNT_GAUGE, (unsigned long long)CNT_HREP, TN,
           (unsigned long long)CNT_STRICT, (unsigned long long)CNT_RELAX_NONSTRICT_SOL, (unsigned long long)CNT_NON_SOL, (unsigned long long)NODES,
           (unsigned long long)CTRL_RELAX_MISMATCH, (unsigned long long)CTRL_CANON_NOT_IDEMP, (unsigned long long)CTRL_CANON_CHECKED, now() - T0);
    printf("COMPLETE %d structures %d strict18 %llu non18 %llu relaxonly18 %llu ctrl_relax_mismatch18 %llu ctrl_relax_popc_mismatch %llu\n", COMPLETE, COMPLETE ? NCS : 18,
           (unsigned long long)CNT_STRICT18, (unsigned long long)CNT_NON18_SOL, (unsigned long long)CNT_RELAXONLY18_SOL, (unsigned long long)CTRL_RELAX_MISMATCH18, (unsigned long long)CTRL_RELAX_POPC_MISMATCH);
    if (MODE == 1 && STATE[0]) save_state(b_hi, b_hi);
    return 0;
}
