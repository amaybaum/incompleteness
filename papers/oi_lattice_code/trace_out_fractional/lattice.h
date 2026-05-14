/* lattice.h
 *
 * State representation for the OI substratum trace-out calculation.
 *
 * Lattice: d=3 cubic, L^3 sites, q-valued field at each site.
 * State at each site encodes (f(x,t), f(x,t-1)) for wave-equation bijection.
 * For q=2, per-site state is 2 bits; total state for L=2 is L^3 * 2 = 16 bits.
 *
 * State is stored as a single uint32_t (sufficient for L=2 q=2; extend for larger).
 *
 * Site indexing: site (x,y,z) with 0 <= x,y,z < L is index i = x + L*y + L*L*z.
 * Per-site bits: bit 2*i is f(x,t), bit 2*i+1 is f(x,t-1).
 */

#ifndef LATTICE_H
#define LATTICE_H

#include <stdint.h>
#include <stddef.h>

#define L 2
#define D 3
#define Q 2
#define N_SITES (L*L*L)
#define STATE_BITS (2 * N_SITES)
#define N_STATES (1ULL << STATE_BITS)  /* 2^16 = 65536 */

typedef uint32_t state_t;

/* Extract f(x,t) at site i from state s */
static inline int get_f_now(state_t s, int i) {
    return (s >> (2*i)) & 1;
}

/* Extract f(x,t-1) at site i from state s */
static inline int get_f_prev(state_t s, int i) {
    return (s >> (2*i + 1)) & 1;
}

/* Compute linear site index from (x,y,z) with periodic boundary conditions */
static inline int site_idx(int x, int y, int z) {
    x = ((x % L) + L) % L;
    y = ((y % L) + L) % L;
    z = ((z % L) + L) % L;
    return x + L*y + L*L*z;
}

/* Set f(x,t) at site i in state s (returns modified state) */
static inline state_t set_f_now(state_t s, int i, int v) {
    state_t mask = (state_t)1 << (2*i);
    return (s & ~mask) | (((state_t)(v & 1)) << (2*i));
}

/* Set f(x,t-1) at site i in state s */
static inline state_t set_f_prev(state_t s, int i, int v) {
    state_t mask = (state_t)1 << (2*i + 1);
    return (s & ~mask) | (((state_t)(v & 1)) << (2*i + 1));
}

#endif
