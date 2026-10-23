# Composition lemma for raw AND aggregation under the report18 rule

Exploratory investigation, 2026-10-23; scratchpad only. Preregistration: `PREREG.md` (sha256
`677d5b8d25388811d485ce1b19181be5d105721f97d0aa6b5ae104a77c5181a8`), written before any search.

## Section A. The builder (written before any held-out size was run)

This section was written after discovery at n <= 8 and before n = 9 or n = 12 were run in any form.

### A.1 Statement

Rule: U(t+1) = H(S U(t)) xor U(t-1), H(a,b,d) = (b,d,a xor bd), S = six-neighbour XOR. Register states are coded
s = 4A + 2B + D. Generators g_v = H o T_v (T_v: xor by v in F2^3), v in F2^3.

For n >= 2 the builder B(n) is:

1. **Split.** Chain + takes inputs x_1..x_k1 with k1 = ceil(n/2); chain - takes the remaining k2 = floor(n/2).
2. **Group program.** Fix the support Omega = {0,1,2,3,4} of register states. For every 5-cycle rho on Omega fix a
   pair of 5-cycles (alpha, beta) on Omega with alpha beta alpha^-1 beta^-1 = rho (one exists for every rho; the pair
   minimising the recursive cost below is taken). Define P(inputs, rho):
   - one input x: m = 6 if both the identity and rho are products of exactly 6 generators, else m = 8 (true for all
     24 five-cycles on Omega). Fix such words w0 (identity) and w1 (rho). Step i uses translation
     s_i = w0_i xor x (w0_i xor w1_i).
   - k >= 2 inputs: f = first ceil(k/2), g = the rest; P = P(g, beta^-1) P(f, alpha^-1) P(g, beta) P(f, alpha),
     in application order. Its total permutation is rho if all its inputs are 1 and the identity otherwise.
   Chain + runs P(x_1..x_k1, rho_+) with rho_+(0) = 2; chain - runs P(rest, rho_-) with rho_-(0) = 1. The shorter
   program is padded with identity words (lengths 6, 8 or 10) to a common even length Lc.
3. **Deadline.** T(n) = Lc + 1, with Lc = L(k1) (after padding), L(1) in {6, 8},
   L(k) = L(ceil(k/2)) + L(floor(k/2)) + L'(ceil(k/2)) + L'(floor(k/2)) for the chosen conjugates, hence
   L(k) <= 8 * 4^ceil(log2 k) <= 32 k^2 and T(n) = O(n^2). Measured: T(2..8) = 7, 25, 25, 61, 61, 97, 97.
4. **Realization (receiver at the origin, all sources on the current slice at L1 distance exactly T).**
   - Chain + occupies (x,0,0), x = T-1, ..., 1: program step i is applied at x = T - i (depth d = i - 1). Chain -
     is the mirror image (-x,0,0). The chain sources at (+-T,0,0) are zero (register starts at state 0).
   - Three wings per chain, in the half-planes +y (z = 0, y > 0), -y (z = 0, y < 0) and +z (y = 0, z > 0), with seed
     fields A, B, D respectively (the same seeds for both chains). With P: D -> B -> A -> D, wing w at depth d
     delivers component P^d(f_w) of step d+1's translation; call that affine function g_w(d).
   - Wing w's source in column q = 0, ..., T-2 sits at (+-(T-1-q), q+1, 0) for +y, (+-(T-1-q), -(q+1), 0) for -y,
     (+-(T-1-q), 0, q+1) for +z, in field f_w, with value c_q = XOR of g_w(d) over d <= q with C(q,d) odd.
   - Axis sources at (0,T,0), (0,-T,0), (0,0,T), field f_w, value = XOR over both chains' wings in that half-plane of
     c_q over q with C(T-1,q) odd. They make the receiver step's injection zero.
   - Every source holds an affine function of the inputs; no previous-slice source is used.
5. **Readiness.** Every bit of the receiver cone (current B_T, previous B_(T-1)) is pinned to its builder value:
   zero, or the stated affine function. Bits outside the cone are unconstrained.
6. **Output.** The D register at the origin at tick T equals AND_n. The receiver's full triple is
   (F1, F2, F1 F2), with F1 = AND of chain +'s inputs and F2 = AND of chain -'s.

Resource counts: copies are not single-input slots here; every source cell is one affine equality. The receiver-cone
constraint count is the codimension of the ready set, C(n) = 3[v(T) + v(T-1)] - n (checked: the input-to-source
map has rank n). Workspace is one-shot: nothing is restored.

### A.2 Why it works (proof outline; each step is checked in Section B)

1. **First light.** If every initial bit within the receiver cone is zero except sources at L1 distance exactly T
   (current slice), then every cell y has U(y,t) = 0 for t < T - |y|, and U(y, T - |y|) = H(sum of the values of its
   outer neighbours at their first-light time). Neighbours on Z^3 differ in L1 norm by exactly one, inner neighbours
   are still dark, and U(y, t-2) = 0. The receiver's value at T is computed by this feed-forward layered circuit.
2. **Wing linearity.** If all sources of a wing share one seed field, every value in that wing's interior at depth d
   is a single field P^d(f). H then acts as a field rotation, products (which need B and D at once) never form, and
   the wing is a linear medium. The number of monotone paths from column q to the side cell at depth d is C(d,q).
3. **Pascal inversion.** The matrix C(d,q) mod 2 is lower unitriangular and its own inverse over F2, so any profile
   g(0..T-2) is delivered by the column values c_q above.
4. **Register.** The chain cell at depth d is H(previous chain cell + side cells), which is the register step
   c <- H(c xor s_d) with s_d an arbitrary affine triple (three wings give the three fields at every depth).
5. **Group.** The generators g_v generate S8 (|G| = 40320, computed), which contains A5 acting on Omega, where every
   5-cycle is a commutator of two 5-cycles (Barrington). The program's total is rho iff all inputs are 1.
6. **Receiver.** Chain + ends in state rho_+(0) = 2 = (0,F1,0); chain - in (0,0,F2); the axis sources cancel the
   remaining injection; H(0, F1, F2) = (F1, F2, F1 F2).

## Section B. Results (after Section A was fixed; sha256 of Section A as written: `be34414b...`, see `REPORT-sectionA.sha256`)

`composition_checks.py` (deterministic; numpy) prints a PASS/FAIL line per control and generates the verdict only if
all are green. Its saved output is `composition_checks.out`.

| Check | Result |
|---|---|
| Group | H o T_v generate a group of order 40320 = \|S8\| |
| Commutators | every 5-cycle on Omega is a commutator of two 5-cycles on Omega; each has an aligned block of length 6 or 8 |
| Pascal | C(d,q) mod 2 (40 x 40) is its own inverse |
| Reduction | full 3D dynamics equals the triangular first-light CA at the receiver, 25 random quadrant configurations |
| Machine, n = 2..8 (discovery) and n = 9, 12 (held-out) | exact AND_n on all 2^n inputs; chain + ends in (0,F1,0), chain - in (0,0,F2) |
| First-light sweep on the 3D lattice, same sizes | the builder's actual source list, swept layer by layer (each lit cell = H of the sum of its outer neighbours): exact AND_n, degree n; input-to-source map has rank n |
| Full 3D dynamics, n = 2..6 | torus side 2T+3; zero background and two dense full-torus backgrounds (everything outside the receiver cone random): exact AND_n, degree n |
| Countercontrols, n = 4, full 3D | removing the axis sources, removing one wing source, or releasing the chain-start pin (T,0,0) to 1 each break the output |
| Observation | of 40 random zero pins in the n = 3 receiver cone, released to 1 one at a time, 17 break the output: the cone pins are not all load-bearing, and the readiness count is not minimal |

Deadlines and resources (receiver-cone constraint count C(n) = 3[v(T)+v(T-1)] - n):

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 12 |
|---|---|---|---|---|---|---|---|---|---|
| T(n) | 7 | 25 | 25 | 61 | 61 | 97 | 97 | 169 | 241 |
| source cells (affine equalities) | 31 | 127 | 126 | 312 | 320 | 513 | 528 | 928 | 1342 |
| C(n) | 2854 | 125397 | 125396 | 1816819 | 1816818 | 7302929 | 7302928 | 38617167 | 111984012 |

**Against the preregistered rule.**
- Criteria 1 (zero background) and 3 (non-vacuous countercontrol) are met.
- Criterion 2 (two dense full-torus backgrounds) is met at every discovery size, n = 2..8. The checker runs n = 2..6;
  a separate run of the same code (`check3d.py 7 8`, saved as `check3d_78.out`, 554 s and 954 s) gives exact AND_7
  and AND_8 with degrees 7 and 8 on the zero background and both dense backgrounds.
- Criterion 2 is not checked by full simulation at the held-out sizes n = 9 and 12. At T = 169 and 241 the torus of
  side 2T+3 needs about 7.6 and 175 GB per state array. The held-out sizes are covered by the exact register machine
  and by the 3D first-light sweep, which implements a proved lemma rather than the raw dynamics. The lemma itself is
  checked against the raw dynamics at every size from 2 to 8.
- **By the preregistered rule as written, the outcome is therefore not "success".** The builder is stated and
  proved, and verified in full 3D at every discovery size, but at the held-out sizes only in the two reduced models.

## Section C. Branch record (depth-first)

1. **Copy-free latency-1 tip chain** (each input arrives as an axial tip in B next to the next receiver). DFS over
   229451 candidates in 600 s: the deepest chain is P5; no P6. At depth 6 the junk includes stale products (for
   example abc + abcd), which single-input copies cannot cancel. Verdict: wall for this branch within budget.
2. **First-light staircase, periodic, copy-free.** All period-2 families up to n = 8: best depth 4. Diagnosis: once
   the receiver moves, earlier inputs' boxes are 2D and contribute through Pascal path counts; turns cancel the stale
   product in SB, but the previous input persists in SA. Verdict: wall for this family.
3. **Reduction (NEW).** With all sources on the radius-T shell, the receiver's value is a feed-forward layered
   circuit (each cell = H of the sum of its outer neighbours). In a planar quadrant this is the triangular 1D
   cellular automaton u_l(i) = H(u_(l+1)(i) xor u_(l+1)(i+1)); checked against the full dynamics.
4. **Boundary chain with one wing (one injection slot per step).** Exhaustive search over self-reproducing 3-step
   stage templates whose components are XORs of {1, P_prev, P, x, x_prev}, with one-slot injections from
   {0, 1, x, x_new} combinations: none carries the product. Simulated annealing in the triangle found AND3, AND4 and
   AND5 at T = 2, 4, 6 but no pattern (the landscape is a needle). Verdict: wall for one-slot stages within the
   searched class. A side search for self-reproducing stages with full affine injection found none of length 1;
   length 2 did not finish within 1500 s. The builder in branch 5 does not need such a stage.
5. **Three wings, full affine injection (the builder).** The chain becomes a 3-bit reversible register driven by
   input-controlled translations; the generated group is S8, so Barrington's commutator construction computes AND_n
   for every n. Verdict: builder found; verified as in Section B.

## Section D. Scope and limits

- **Latency and cost.** T(n) = O(n^2) (Barrington), and the ready set pins the whole receiver cone: C(n) grows as
  O(n^6). Shorter programs (for example Cleve-type constructions, or multi-input affine reads) are not excluded and
  were not searched. A reason a single register needs repeated reads: a read-once permutation automaton's set of
  "dead" states grows by at least one per input, while only four states have D = 0. This argument was not checked
  separately.
- **Side records.** The device exposes everything it writes: the receiver triple is (F1, F2, F1 F2), and the chains
  and wings carry the program's intermediate states. One-shot: nothing is restored.
- **What it is not.** It is not a native preparation of the ready set, a clock, a minimal readiness count, an angular
  law or quantum equivalence. The rule remains the engineered report18 candidate. The construction shows
  composability of exact raw AND under that rule with a stated builder for every n; it does not show that the
  builder is efficient or physically natural.
