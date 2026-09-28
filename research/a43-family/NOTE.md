# a43 research note — the Diţă locus beyond act 40's H3 (disposable pre-freeze research; not a round)

Branch `claude/a43-family-generalization-research`, based at D41 = `78ea3c39004e97aad027ee6153051c6d372bdd55`. Nothing here is
a certificate, a preregistration or a verdict. Every assertion below is exact arithmetic (Gaussian rationals; characters in `Z^d`
with values in `G = <i, z, w> = Z/4 x Z^2`); floats are used nowhere. Mode: gem-finding (§A.31). Conjectures were committed
before their tests: `conjectures-stated-before-testing.md`, commits `f926fb83` (K1–K7), `bb491954` (K8, K9), `8433c54b` (K10),
`b677d943` (K10′, before the hold-out).

**Notion used.** Unless marked "sorted", every locus, count and union below is computed over **all labellings** (every
within-class matching of rows, the index-map datum act 36–40's searches fix to the sorted order; see §2), strict and relaxed
separately; the sorted-labelling result is computed alongside and reported as such. For both strict and relaxed forms the matching
of each class `b ≥ 1` to class 0 is chosen independently per class (the strict condition for class `b` involves only `σ_0` and
`σ_b`; `σ_0` is fixed by the free global relabelling of `a`), which keeps the union exact and tractable. Act 40's five faces are
used as a control only in the sorted notion (§0); the all-labellings H3 computation in §2 is a byproduct of this thread's
diagnosis, not the coordinator's audit of act 40, and is reported for that audit to compare against, not in place of it.

## 0. Controls first

| control | result | log |
| --- | --- | --- |
| the frozen act-40 probe, copied verbatim (blob `4b718e79`), run here | `OK`, 22 PASS | `control_probe40.log` |
| the d-parameter harness (`lib43.py`) on H3 | 46 candidates, 30 nonempty, strict = relaxed, all coordinate, five faces; **key-by-key identical** to the frozen 3-dim classifier | `c0_control_h3.log` |
| d = 0 classifier at SIG, frozen (sorted) notion | 18 structures (act 37's census) | `c0_control_h3.log` |
| act 38's pieces table (hulls of A, B, C and pairwise spans) | reproduced | `c0_control_h3.log` |
| witness set | 416 regenerated `{0,1}` lines (`a38/first_wit.pkl`) → **53 orbits** (gauge × stabilizer 1024 × sign), all exactly straight (direct Laurent identity) and in no census hull | `s1_orbits.log` |
| splitter enumeration vs direct exact joint-realizability test | 0 disagreements (enumerated splitters all pass; 208 random non-splitters all fail) | `s2_atoms.log` |
| countercontrols: gauge atom added to H3 (strict must separate from relaxed); act 40's perturbed-C family; hull family (B, C) | relaxed = five faces × free u4, strict differs; frozen countercontrol reproduced (30 candidates, face u3 = 1); (B, C) locus = whole torus | `cc_controls.log` |
| flip identities as matrix identities at 120 exact points | u1 → −u1 is rows 7↔15, u3 → −u3 is columns 2↔8, u2 → −u2 is neither | `cc_controls.log` |

## 1. Families studied (exact definitions)

**Atoms.** For a `{0,1}` straight line `E`, a *splitter* is a `0/1` sub-support `P ≤ E` with `{P, E−P}` jointly realizable
(`SIG ∘ u^P v^(E−P)` unitary on the whole 2-torus: every joint level set of every row-pair difference has vanishing pair sum).
Every piece of any jointly realizable `0/1` decomposition of `E` is a splitter, so every such decomposition coarsens the partition of
`supp E` into *atoms* (cells equivalent iff every splitter contains both or neither).

- In **415 of 416** witnesses the splitter family is Boolean (`#splitters = 2^#atoms`), every atom is a **16-cell rectangle
  `R × K`** (shapes 2×8, 4×4, 8×2, and 1×16 full rows, which are gauge-trivial), and the atom family is jointly realizable. So the
  *atom family* `F_E(u) = SIG ∘ ∏_k u_k^{P_k}` is the unique finest jointly realizable `0/1` family through `E`. For act 38's
  witness the atoms are exactly act 38's `A` (2×8), `B` (4×4), `C` (8×2): H3 is the atom family of its line (**POSITIVE**: act 39's
  choice of pieces is canonical, not one decomposition among several).
- The exception (one member of orbit 7) has 7 atoms (four 1×8, not straight individually) and 48 splitters; its atom family is not
  jointly realizable. **BORDERLINE**, not pursued: another member of the same orbit has a Boolean atom family.
- Library: 34 distinct atoms across the 416; 22 straight essential rectangles, 4 gauge rows, 8 non-straight 1×8 (the exception).
- Families classified: the essential atom family (gauge atoms dropped) of the fewest-atom member of each of the 53 orbits:
  d = 3 (10 orbits, H3's orbit among them), 4 (26), 5 (14), 6 (3). Plus: act 37's arc; 22 + 16 random library families (§5).
- Collection bias, stated: the 8×2 atom `C` occurs in all 416 witnesses (the collector's search order); the 416 are a DFS prefix, not
  a census, and nothing here is a statement about the `{0,1}` census or about minimal support.

## 2. The hidden assumption: within-class alignment (NEW)

A Diţă index map of shape `m × n` fixes, beyond the column blocks and row classes, **which member of each row class plays X-row
`a`** (`H[σ_b(a), cp[c][d]] = X[a][c] D[c][b] Y_c[b][d]`). The orderings of `d`, `c` and `b` are free, and a global relabelling of
`a` is free; `σ_b` for `b ≥ 1` is not, when `m ≥ 3` (4×4 and 8×2 shapes; for `m = 2` with flat `X` it is immaterial). The
structure searches of acts 36–38 (`dita_orientations`, `structures`) and act 40's `conditions` take `σ_b` = **sorted order** for
every class. The candidate enumeration (blocks, classes) is alignment-free and complete; the loci are computed for one alignment
per candidate.

`align.py` computes the alignment-free locus exactly: `L = Prop ∩ ⋂_b ⋃_{σ_b} L_b(σ_b)` (a finite union of flats; DFS over `σ_b`).

The parallel census thread found the same gap and the same fifth 4×4 structure independently (coordinator message; code in
`wt-a41-census-research/research/a41-census/`: `fifth.py`, `matchings.py`, `matchlib.py`); the two findings were reached separately.

Findings, each confirmed by an **independent** method (`v1_explicit.py`: exact Gaussian search over all permutations, then an
explicit build of `X`, `D`, `Y_c` and an entrywise check of all 256 entries plus flat unitarity; no flat calculus):

- **SIG has 20 Diţă structures, not 18.** The two extra (column and row form) have blocks
  `((0,6,8,14),(1,7,9,15),(2,4,10,12),(3,5,11,13))` and classes `((0,2,9,11),(1,3,8,10),(4,6,13,15),(5,7,12,14))` — act 37's
  `k3` index sets with blocks and classes exchanged — with alignment `[(0,2,9,11),(8,10,1,3),(4,6,13,15),(12,14,5,7)]`.
  Explicit exact factorizations verified (`v1_explicit.log`). Act 37's probe-layer sentence "the census of the stratum point's Diţă
  structures is exhaustive, eighteen structures" holds for the sorted-alignment notion only.
- **Positive control of the diagnosis:** SIG with rows 7↔15 swapped is a row permutation of SIG; the sorted notion finds 12
  structures there, the alignment-free notion 20 (`c1_alignment.log`).
- **Act 40's verdict survives.** For H3 the alignment-free union of the loci is still exactly the five faces, strictly and up to
  diagonal equivalence — by `align.py` (`c1_alignment.log`) and, independently, by brute force over **every** alignment using only
  the frozen probe's own `classify`, `conditions`, `solve`, `Flat` (`v2_bruteforce_h3.log`, 26 × 13 824 + 10 × 40 320 + 10 × 128
  alignments). Explicit exact search at 22 points (the frozen probe's 17 plus 5) finds no structure off the five faces
  (`v3_points_h3.log`; its sorted-alignment counts equal the frozen section-7 counts exactly).
- **Act 40's intermediate statements are notion-dependent.** Alignment-free: **43** nonempty candidate loci (not 30), and **not**
  all cut out by coordinate characters — four loci contain the non-coordinate points `u1 = ±z⁻², u2 = 1, u3 = ±1`. Structure
  counts: `(1,1,1)` 20 (frozen control: 18, "exactly act 37's census"), `(−1,1,1)` 20 (12), `(1,1,−1)` 20 (12), `(−1,−1,−1)` **4**
  (frozen control: "one 2×8 structure per orientation, M_COL and M_ROW"), `(1,u,−1)` 4 (3), `(u,1,1)` 8 (7), `(−1,1,u)` 5 (4),
  `(±z⁻²,1,1)` 10 (7). The frozen sentence's union and its only-if direction are unaffected; its sub-claims "the thirty nonempty
  loci are cut out by coordinate characters alone" and the two structure-count controls are statements about the sorted notion.
- **Act 37's arc** `SIG ∘ u^W`: strictly, away from `u = 1` only the frozen 2×8 class (both orientations) — act 37's exclusivity
  holds; at `u = 1`, 20 structures. Up to diagonal equivalence, `u = −1` admits **20** structures (explicit exact:
  `v4_relaxed_explicit.log`, diagonal `D1` built and the strict factorization of `D1·H` verified). Act 37's sentence is strict
  ("is a Diţă matrix"), so this is outside it, not against it. **NEW (relaxed-only exceptional point of act 37's arc).**
- Across all 53 orbits the sorted-notion union equals the alignment-free union (`SORT` 53/53) although 2003 vs 3123 nonempty
  candidate loci — **POSITIVE for act 40-style verdicts, unexplained** (no proof that the sorted notion always reaches the union).

## 3. The mechanism of the ±1 faces (NEW, theorem-shaped)

**Flip lemma.** Rows of `SIG = F4(z) ⊗ F4(w)` have a ±1 ratio vector only for index shifts by 2 in `a` or `b`. H3's atom `A =
{7, 15} × {c odd}` satisfies `SIG ∘ (−1)^A = τ_{7,15} SIG` (a row swap), and `A, B, C` are τ-invariant; hence
`H3(−u1, u2, u3) = τ_{7,15} · H3(u1, u2, u3)` **for all u** (checked as a matrix identity at 120 exact points, and a one-line
monomial identity). Likewise `C` flips to the column swap `σ_{2,8}`: `H3(u1, u2, −u3) = H3(u1, u2, u3) · σ_{2,8}`. Diţă-ness
(general index maps, strict and relaxed) is invariant under index permutations, so the locus is invariant under `u1 ↦ −u1` and
`u3 ↦ −u3`. Consequences, all verified: the faces `u1 = −1`, `u3 = −1` are the images of `u1 = +1`, `u3 = +1`; **`M_COL =
τ_{7,15}(t2 column)` and `M_ROW = σ_{2,8}(t1 row)`** (act 38's exceptional maps are transports of census maps; index sets checked,
`c3_transport_mcol.log`); the points
`u1 = ±z⁻²` come in a pair; predicted count equalities `count(−1,1,1) = count(1,1,1) = count(1,1,−1) = 20`,
`count(−1,−1,−1) = count(1,−1,1) = 4`, `count(−z⁻²,1,1) = count(z⁻²,1,1)` — stated before `v3` finished and confirmed there.

**Why `u2 = −1` is absent (orthogonality lemma).** If flipping the rectangle `R × K` made row `i ∈ R` equal `λ` times another row
`π(i)`, then `⟨row_i ∘ (−1)^K, row_i⟩ = 16 − 2|K|` must equal `λ⟨row_{π(i)}, row_i⟩ = 0`, so `|K| = 8`; column-side likewise
`|R| = 8`. A 16-cell rectangle flip is one-sided monomial only if it is 2×8 or 8×2. `B` is 4×4: its flip is not even monomially
equivalent to SIG (checked exactly), so no symmetry produces `u2 = −1`. Across the essential atoms of all 53 orbits: every 4×4 flip
is neither permutation nor monomial (72/72), every 8×2 flip is a column permutation (53/53), 2×8 flips are row permutations (71)
or row permutations with row phases (26) (`d_flips.py`). The last kind is what separates strict from relaxed loci (K10′).

## 4. Conjectures and outcomes

| id | statement (short) | outcome | class |
| --- | --- | --- | --- |
| K1 | all loci coordinate, strict = relaxed, maximal loci codim-1 | **false** (holds 14/53): codim-2 components (orbits 13, 14, 23, 28), strict ≠ relaxed (4, 8, 10, 14, 28, 32), non-coordinate points inside loci | falsified |
| K2 | `u_k = +1` face iff the other atoms' span lies in a SIG structure | 53/53 (tautology; harness control) | CONFIRMING |
| K3 | every atom has its +1 face | **false** (10/53) | falsified |
| K4 | −1 face iff +1 face and atom 2×8 or 8×2 | **false** (49/53; orbits 4, 8, 10, 32: 2×8 atom, +1 face, no strict −1 face) | falsified |
| K5 | no −1 face without the +1 face | 53/53 | CONFIRMING |
| K7 | witness line's exceptional set is `{±1}` iff some −1 face | 53/53; every one of the 53 witness lines has exceptional set exactly `{1, −1}` in all three notions | ELABORATING (act 38 generalized) |
| K8 | strict −1 faces = flips that are index permutations with the transported rest Diţă | 53/53 | POSITIVE |
| K9 | alignment-free union is a union of coordinate subtori `{u_S = s}` | 53/53 | POSITIVE |
| K10 | relaxed union = permutation predictor | 22/26 retro — **false** (fails exactly where strict ≠ relaxed) | falsified |
| **K10′** | strict union = ⋃ `T(S,s)` over sign points whose flip `SIG ∘ ∏ s_k^{P_k}` is an index permutation with the transported remaining atoms identically strict-Diţă in one of SIG's 20 structures; relaxed union = the same with "permutation times one-sided diagonal phases" and relaxed membership | retro 26/26 (fitted); **hold-out orbits 26–52: 27/27 strict and 27/27 relaxed**; random library families: 24/24 (weak) and 16/16 witnesses (§5) | POSITIVE (best candidate) |

## 5. Out-of-collection test (random library families)

`s6_random_families.py`: families of 2–4 straight library atoms, randomly transported by stabilizer elements, jointly realizable.
Batch 1 (seed 4343, 24 families): K10′ strict and relaxed 24/24, but 23 are hull families (union = whole torus) — a weak test;
the one witness (d = 3) has strict union `u1 = 1, u2 = 1, u3 = 1` and relaxed union with `u1 = −1`, `u3 = −1` added, both predicted.
Batch 2 (seed 4344, witnesses only — sum in none of SIG's 20 structures, relaxed — d = 3–5, 16 families from 1359 draws, three
with overlapping supports): **K10′ strict 16/16, relaxed 16/16**; six of them have strict ≠ relaxed unions, all predicted
(`s6b_random_witnesses.log`). A relaxed-only face was also checked explicitly: at a generic Gaussian-rational point of orbit 4's
face `u2 = −1`, 0 strict structures and 1 up to diagonal equivalence (`v4_relaxed_explicit.log`).

## 6. The best candidate general statement

> For a jointly realizable family `F(u) = SIG ∘ ∏_k u_k^{P_k}` of 16-cell rectangle atoms through the stratum point, the set of
> `u` at which `F(u)` admits a Diţă structure (any shape and index map, including the within-class alignment) is a union of
> coordinate subtori `T(S, s) = {u_k = s_k, k ∈ S}`, `s ∈ {±1}^S`; `T(S, s)` belongs to it iff the sign point
> `SIG ∘ ∏_{k∈S} s_k^{P_k}` is an index permutation of `SIG` (up to diagonal phases on the permuted side, for the relaxed notion)
> and the remaining atoms, transported by that permutation, lie identically in one of `SIG`'s twenty Diţă structures.

Evidence level: exact computation (all labellings) on 53 witness orbits (27 of them a committed hold-out) plus 40 random library
families (16 of them witnesses, 3 with overlapping supports); not proved. The
"if" half is a theorem (transport + permutation invariance of the Diţă property). The "only if" half — no Diţă point off such
subtori, in particular none at non-sign values and none at sign points whose flip is not monomial — is the empirical content.
Counter-examples: none found for K10′. Individual candidate loci are **not** coordinate (non-coordinate points exist); only the
union is.

## 7. What is theorem-shaped for a future native round (kernel vs probe)

- **Kernel, cheap:** (i) the two extra SIG structures as explicit strict Diţă factorizations (act 40-style face lemmas; exact
  entries); (ii) the flip identities `H3(−u1,·) = τ_{7,15} H3(u1,·)` and `H3(·,−u3) = H3(·,u3) σ_{2,8}` and the transport of
  a strict Diţă product along index permutations — this re-derives act 40's `A40-1` faces `u1 = −1`, `u3 = −1` from the +1 faces
  and identifies `M_COL`, `M_ROW` as transports; (iii) the orthogonality lemma (a rectangle flip is one-sided monomial only if
  `|K| = n/2` or `|R| = n/2`).
- **Probe:** an alignment-free re-certification of act 40's only-if direction (union unchanged; 43 nonempty loci; non-coordinate
  points) and of act 37's census (20 structures); K10′ over the 53 orbits.
- **Scope decision needed before any round:** what "index map" means in acts 36–40's frozen sentences. If it includes the
  within-class alignment (the ordinary meaning of a Diţă index map), act 37's census count and act 40's "cut out by coordinate
  characters alone" / structure-count controls are statements about a restricted notion, while act 40's classification itself
  holds under the general notion (this thread's computation, two independent exact codes).

## 8. Caveats

- The 416 witnesses are a DFS prefix of one collector (row 0 = 0 domain), strongly biased (atom `C` in all); hold-out orbits share
  atoms with the formation orbits, so the hold-out is not independent in the statistical sense.
- One orbit member (orbit 7) has a non-Boolean splitter family; atom families of other members were used.
- "Structure" throughout means the monomial conditions (proportionality + rank one, strict or relaxed); flat unitarity of the
  factors is verified explicitly only in `v1`/`v3`/`v4` (it follows from unitarity of `H` for every structure checked).
- Not claimed: anything about the `{0,1}` census, minimal support, other stratum points, or physics.
- Contamination record: aggregate tallies over orbits 26–28 were seen before K10′ was committed (no per-orbit locus); K8 was
  written after the sorted-notion face lists of orbits 0–13 had been seen.

## Files

`lib43.py` (library; loads the frozen probe copy), `splitters.py`, `align.py`, stages `s1`–`s6`, verifications `v1`–`v4`,
controls `c0`–`c3`, `cc_controls.py`, tests `t_k8.py`, `t_k10.py`, diagnostic `d_flips.py`; logs `*.log`; data `*.pkl`.
