# A41 census research — control preregistration (written before the orbit run's results)

Research thread, not a governed round. Base D41 = `78ea3c39004e97aad027ee6153051c6d372bdd55`.

Chronology, stated honestly: the tables were exported (`export41.py`), the enumerator `census41.c` was written,
and one **count-only** pass (`census41 count`, no group work, no classification) was run before this file was
written; its output (D-solutions 171 552 256, gauge classes 30 594 431) is therefore known at writing time. The
orbit run (`census41 full`) was started at the same time as this file was drafted; none of its per-orbit results,
orbit count, classification counts or controls had been read when the rules below were fixed.

## Decision rule

The census verdict (orbit count, per-orbit classification, support data) is printed as **exhaustive-exact** only
if every control C1–C10 below is green. If any control is red, the verdict is void and the note reports the red
control and the raw numbers as unverified.

## Controls

- **C1 witness.** Act 38's E = A + B + C is in the domain, is a straight line by the direct exact Laurent identity
  (Gaussian rationals, no subset tables), its canonical form is a key of the orbit table, and that orbit is
  NON-DIŢĂ (no relaxed membership of the canonical representative; no strictly-member domain solution); the orbit
  has 512 distinct gauge-normal images (discovery note) and minimum gauge-normal support 48.
- **C2 hulls.** Strict and relaxed memberships of A, B, C, A+B, A+C, B+C, A+B+C equal the discovery-note table
  (strict = relaxed in every case); each of the seven is in the domain and its orbit is in the table.
- **C3 zero.** The zero matrix is in all 18 strict and all 18 relaxed subspaces; its orbit is in the table.
- **C4 Knuth.** An independent Knuth estimator (C, same MRV order, >= 10^5 probes over several seeds) agrees with
  the exact count within 3 standard errors of the pooled estimate.
- **C5 sub-domain, two methods.** On a sub-domain fixed by two row masks, the C enumerator (`dump`, all rows) and
  an independent Python enumeration (row-by-row join from the exact Gaussian-integer pair sums, not the vanishing
  tables or the compatibility bitsets) produce the same solution **set**; every solution also passes the direct
  exact Laurent identity.
- **C6 total, three ways.** (a) count mode's Σ 2^z over gauge classes, (b) count mode with all-ones rows kept (one
  leaf per solution), (c) the orbit run's Σ over H_dom images × 2^z — all three equal.
- **C7 canonical form.** Built-in: for every new orbit, canon(canon) = canon and canon(random image) = canon
  (zero failures). Independent: the Python reference `canon_ref` (lib41) recomputes the canonical form of the
  first-found solution for a random sample of >= 2000 orbits (and every NON-DIŢĂ orbit up to 2000) and matches
  the C key. The 2048 group elements are closed under composition.
- **C8 relaxed invariance.** Built-in counter of relaxed-membership disagreements between a class, its H_dom images
  and its canonical form is 0; exact check that the group generators permute the 18 relaxed subspaces modulo gauge.
- **C9 prior run.** A per-solution classifier in act 38's DFS order (all rows, MRV lowest index, candidates
  ascending) reproduces the killed `dfs2.py` run's partial statistics at 10 420 224 solutions:
  strictly-outside-but-relaxed 229 120, outside every relaxed subspace 437 248.
- **C10 orbit table integrity.** Every canonical representative in the table (decoded from its key, Python, exact
  integer vanishing tables) is a straight line; every first-found solution is a D-solution; the table's Σ n_sol
  equals C6's total.

## Group action (fixed)

Γ = gauge ⋊ (Stab × {±1}): gauge E ↦ E + r·1ᵀ + 1·cᵀ (r, c integer vectors); g = (perm, s) ∈ Stab (act 36's
1024 index permutations of SIG's stabilizer in G_ext, with sign s = −1 on the conjugating elements) acts by
(g·E)[perm(t)] = s·E[t]; the extra sign E ↦ −E (u ↦ u⁻¹). Canonical form: the lexicographic minimum, row-major
over the 256 entries, of the gauge normal forms gn(ε·g·E), gn(E)_ij = E_ij − E_i0 − E_0j + E_00, over the 2048
pairs (g, ε).

## Orbit classification (fixed)

- NON-DIŢĂ: the canonical representative lies in none of the 18 relaxed subspaces (orbit invariant; C8).
- DIŢĂ (strict): some D-solution of the orbit lies in at least one of the 18 strict subspaces.
- RELAXED-ONLY: in some relaxed subspace, but no D-solution of the orbit in any strict one.
Strict membership is not gauge invariant (a gauge-trivial matrix is relaxed in all 18, strict in none), so the
strict class is defined through the orbit's D-solutions; per-solution counts are reported as well.
