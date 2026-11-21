# A1-EXIT Step 2, unit S2-A (lattice qualifications): preregistered edit list

**Status.** Preregistration, pushed before any manuscript edit. Manuscript corrections only; no
Lean, registry or ledger edit; no merge; no workflow dispatch.

**Authorization.** Owner `amaybaum`, #1169 comment 7056875845 (2026-11-21): Step 2 units S2-A to
S2-E. For this unit: apply Q1's E1, E2, E3, E4 and E6; restate A4 as the owner decided
(#1169 comment 7048255658, 2026-11-20T19:08:01Z); apply rows X-41 and X-43 only as far as E1–E6 and
the A4 restatement cover them. E5 is skipped (owner). A1 and Main ledger item (ii) are out of scope.

**Goal link (§A.47).** The A1-exit objective (#1169). This unit decides whether its lattice sites
can be made true without A1: A4's lattice clause is printed on ℤ^d as the standard construction, and
each finite periodic quotient becomes a qualified case carrying Q1's wrapping conditions.

**Base.** `main` at `1c7eedc40` (contains Q1's pin `9db51884` and the ledger pin). Drift check: at
the base, `q1_census.py` and `q1_census_supp.py` reproduce Q1's committed JSON byte for byte, and
`git diff 9db51884 1c7eedc40` touches none of this unit's lines (the only change in the affected
files is Q2's SM:242/250 edit). Every old string below is exact at Q1's pin and at the base.

**Inputs.** Q1 record `verification/audits/foundations/a1exit-q1-20261120/RESULT.md` §7 (E1–E6 and
the owner A4 decision); A1-EXIT ledger `verification/audits/foundations/a1exit-ledger-20261120/`
rows X-40 to X-43.

**Exact strings.** The machine-readable list is `checks/s2a_edits.json`; the text below is generated
from it. `checks/s2a_check.py --pre` exits 0 at the base (every old string occurs exactly once in its
file and in its mirror); `--apply` applies the list; the default mode exits 0 iff every new string
occurs exactly once in its file and mirror and no old string survives outside its new string.

## Rules for the A4 restatement

- ℤ^d is printed as the standard construction, as a discrete lattice distinct from a continuous space.
- A finite periodic quotient ℤ^d/P is a qualified case "under the conditions on P stated with each
  result that uses it"; those conditions are printed by E1 (SM §4.1) and, in the book, by E4 and E6.
- No finite lattice is called an approximation or representative of ℤ^d.
- Only the lattice clause changes. The second sense of A4 (no self-copy), the independence example on
  "a periodic cubic lattice of side at least 3" (a finite example, true as stated), and A1 are untouched.
- No edited sentence states Theorem 13's Schur-complement result, so X-43's C13 condition has no site here.

## Mirrors (§A.14, §A.25)

Every book edit is applied to the chapter and to its FULL mirror (listed per edit; the mirror lines
are byte-identical to the chapter lines at the base). SM:202 is the SM restatement of A4's clause.
E1 covers SM:134/136, SM:549, SM:1237–1257 and SM:1554 without separate edits (Q1 §7). E4 covers
ch06:22, :30 and FULL:1533, :1541; E6 covers ch05:154, :156, :162, :166, :172, ch06:20 and their FULL
mirrors (Q1 §7). Not edited, with reason: "periodic-lattice class" (SM:30, :36, Sub:157 first
clause, ch00:21, ch02:70, ch02:94, ch05:15, Complexity:13, Computation:13 and FULL mirrors), true for
ℤ^d and its quotients alike; ch18:242 (a compact identification giving a finite periodic lattice as
one way to realize A1, an A1 sentence and true as a qualified case); ch19:198 = FULL:5268 ("On a
finite lattice"), listed in X-40's site column but not among this unit's authorized sites, reported
to the coordinator.

Out of scope and untouched: SM:122 and SM:252 (X-41 law conditions, unit S2-C); E5 (SM:446).

## Edits

### E1: SM:222

- Row: X-42, X-43. Source: Q1 §7 E1.
- Finding: Q1 §3, §6: the §§4.2–4.8 results are stated on Λ = ℤ^d; on a finite quotient each needs its period-lattice condition (Q1 §2), and SM:222 asserts the quotient without them.
- Old: `(under A1 and A4 [Substratum §3.1] it acts on configurations over a finite periodic quotient of $\Lambda$)`
- New: `(under A1 and A4 [Substratum §3.1] it acts on configurations over a finite periodic quotient $\Lambda/P$; the staggered and cubic results below are stated on $\Lambda$ and hold on such a quotient when $P$ admits them: the staggered phases, and the identity of Theorem 2 with the two-step stencil, require every vector of $P$ to be even off one axis; the checkerboard requires even coordinate sums; the blocked lattice, the eight Brillouin-zone corners and the staggered blocking require $P \subset 2\mathbb Z^d$; and the cubic group acts when it maps $P$ to itself)`

### E2a: SM:539

- Row: X-42. Source: Q1 §7 E2.
- Finding: Q1 C539: the spin–taste identification needs P ⊂ 2ℤ^3 on a quotient.
- Old: `The staggered-to-Dirac reconstruction identifies the two sublattices`
- New: `On $\mathbb Z^3$, and on a quotient whose period vectors all lie in $2\mathbb Z^3$, the staggered-to-Dirac reconstruction identifies the two sublattices`

### E2b: SM:539

- Row: X-42. Source: Q1 §7 E2.
- Finding: as E2a.
- Old: `For the designated checkerboard cut, the visible`
- New: `For the designated checkerboard cut on these lattices, the visible`

### E3a: SM:1506

- Row: X-42. Source: Q1 §7 E3.
- Finding: Q1 §7 E3: asserts the substratum's checkerboard, which a quotient carries only for even-sum periods.
- Old: `block-diagonal coupling, bipartite checkerboard structure) at the bilinear level`
- New: `block-diagonal coupling, bipartite checkerboard structure on $\Lambda$ and on quotients whose period vectors have even coordinate sum) at the bilinear level`

### E3b: SM:1532

- Row: X-42. Source: Q1 §7 E3.
- Finding: as E3a.
- Old: `the substratum's bipartite-lattice plus commutant structure`
- New: `the substratum's bipartite-lattice plus commutant structure (on $\Lambda$ and on quotients whose period vectors have even coordinate sum)`

### E3c: SM:1536

- Row: X-42. Source: Q1 §7 E3.
- Finding: as E3a.
- Old: `block-diagonal coupling, bipartite checkerboard structure) and the emergent-level`
- New: `block-diagonal coupling, bipartite checkerboard structure on $\Lambda$ and on quotients whose period vectors have even coordinate sum) and the emergent-level`

### E4: ch06-matter-content:24 = FULL:1535

- Row: X-42, X-43. Source: Q1 §7 E4.
- Finding: Q1 C8, C10: the eight corners need P ⊂ 2ℤ^3, the cubic relation needs an O-invariant P (4×4×6 countermodel).
- Old: `One singlet taste; three triplet tastes related by cubic symmetry.`
- New: `One singlet taste; three triplet tastes related by cubic symmetry. These are the corners and the cubic action of $\mathbb Z^3$; a finite periodic quotient of it (Chapter 2, A4) carries all eight corners when its period vectors lie in $2\mathbb Z^3$, and the cubic group acts on it when it maps the period lattice to itself.`

### E6: ch05-gauge-structure:91 = FULL:1406

- Row: X-42, X-43. Source: Q1 §7 E6.
- Finding: Q1 §6a: the book statement of Theorem 2 and its blocked reading carry no wrapping conditions.
- Old: `Matching the blocked stencil and solution classes to the normalized nearest-neighbor observer wave above is a separate step.`
- New: `Matching the blocked stencil and solution classes to the normalized nearest-neighbor observer wave above is a separate step. On a finite periodic quotient of $\mathbb Z^3$ (Chapter 2, A4), the staggered phases and this two-step identity require every period vector to be even off one axis; the blocked stencil, the hypercube corners and the spin–taste grading used below require the period vectors to lie in $2\mathbb Z^3$.`

### A4-Sub98: Substratum:98

- Row: X-40. Source: owner A4 decision (#1169 c.7048255658); ledger X-40.
- Finding: X-40: A4's lattice clause prints only a finite quotient; the owner A4 decision makes ℤ^d the standard construction, with finite quotients as qualified cases.
- Old: `(the coupling graph is a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice, $d$ being its dimension)`
- New: `(the coupling graph is the discrete lattice $\mathbb{Z}^d$, $d$ being its dimension, as the standard construction, distinct from a continuous space; a finite periodic quotient $\mathbb{Z}^d/P$ by a finite-index sublattice $P$ is admitted as a qualified case, under the conditions on $P$ stated with each result that uses it [SM §4.1])`

### A4-ch02-82: ch02-substratum:82 = FULL:712

- Row: X-40. Source: owner A4 decision; ledger X-40.
- Finding: X-40 mirror (book).
- Old: `(the coupling graph is a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice, $d$ being its dimension)`
- New: `(the coupling graph is the discrete lattice $\mathbb{Z}^d$, $d$ being its dimension, as the standard construction, distinct from a continuous space; a finite periodic quotient $\mathbb{Z}^d/P$ by a finite-index sublattice $P$ is admitted as a qualified case, under the conditions on $P$ stated with each result that uses it)`

### A4-SM202: SM:202

- Row: X-40. Source: owner A4 decision; ledger X-40.
- Finding: X-40 mirror (SM restatement of A4's clause).
- Old: `the coupling graph is a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice, so $|B(r)| \sim r^d$ below the system size and none`
- New: `the coupling graph is the discrete lattice $\mathbb Z^d$ or, as a qualified case, a finite periodic quotient $\mathbb Z^d/P$ by a finite-index sublattice $P$, so $|B(r)| \sim r^d$ (on a quotient, below the system size) and none`

### A4-ch05-65: ch05-gauge-structure:65 = FULL:1380

- Row: X-40. Source: owner A4 decision; ledger X-40.
- Finding: X-40 mirror (book).
- Old: `the coupling graph is a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice, so $|B(r)| \sim r^d$ below the system size and none`
- New: `the coupling graph is the discrete lattice $\mathbb Z^d$ or, as a qualified case, a finite periodic quotient $\mathbb Z^d/P$ by a finite-index sublattice $P$, so $|B(r)| \sim r^d$ (on a quotient, below the system size) and none`

### A4-Sub157: Substratum:157

- Row: X-41 (covered by X-40's A4 restatement). Source: ledger X-40 (A4 restatements of Q1 §6), X-41.
- Finding: X-40 lists the A4 restatements of Q1 §6 as mirrors; X-41 says these sites are covered by X-40's A4 restatement. The sentence restates A4 as making the graph a finite periodic lattice.
- Old: `whose lattice translations make the coupling graph a finite periodic lattice of rank $d$`
- New: `whose lattice translations make the coupling graph the lattice $\mathbb{Z}^d$ or, as a qualified case, a finite periodic quotient of it`

### A4-ch02-96: ch02-substratum:96 = FULL:726

- Row: X-41 (covered by X-40's A4 restatement). Source: ledger X-40 (A4 restatements of Q1 §6), X-41.
- Finding: as A4-Sub157 (book).
- Old: `Under A4 the coupling graph is a finite periodic lattice of some integer dimension $d$`
- New: `Under A4 the coupling graph is the lattice $\mathbb{Z}^d$ or, as a qualified case, a finite periodic quotient of it, of some integer dimension $d$`
