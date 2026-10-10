# Coordinator's audit of thread X — EXOT (stage 3, Q-SD countermodel search)

Audited: `pt/X/RESULT.md`, sha256 `69ea7b3525bfd56f6b4f5fc5ac71fa88dd3abb23acdb13f07dc0e1d7b3fe38ba`; `pt/X/NOTES.md`
`88ea03fb…` (as listed in RESULT §4); `.start_marker` `19efa59a…` (as listed). `pt/X/` holds 46 entries and no
subdirectory. Protocol: `PROTOCOL-STAGE3.md` (`1a649168…`). Thread U was audited in parallel (`pt/audit/U/AUDIT-U.md`);
neither thread read the other.

## Integrity
- **Coordinator's check, 12:57Z** (before any audit write): the six manifests (`inputs`, `stage1`, `inputs2`,
  `inputs3`, `stage2`, `inputs4`) are OK; `pt/base` HEAD is `9f9f8257…`, status clean, no bytecode; the six protocol
  hashes and `PROTOCOL-NS.sha256` are unchanged; `scratchpad/x_hashcheck.txt` is absent.
- **The start marker.** Written 11:21:46Z into a freshly created `pt/X/` (first file); sha256 as listed.
- **Hashes.** All 37 hash lines of RESULT §4 re-verified with `sha256sum -c`: OK. Every `.err` of a successful run is
  the single line `exit 0` (`28d3b9e8…`).
- **The `pt/` mtime 11:23:27Z** that X's end sweep flagged (NOTES N9) is thread U's `mkdir U` — U's start marker
  records 11:23:27Z as its creation time. Accounted; not an anomaly.
- **Procedural slip, recorded by X itself** (RESULT §5, NOTES N9): a temporary hash list was written to
  `scratchpad/x_hashcheck.txt`, outside `pt/X/`, and deleted after a `sha256sum -c` that reported all 37 lines OK. It
  held hash lines only; nothing under `pt/` outside `X/` was written; the file is absent. Classified as a minor breach
  of the write-only rule with no effect on any result or on the sibling thread's sweep (U's exclusion set did not
  include `scratchpad/`, but the file no longer existed when U's end sweep ran at 12:52Z, and U's sweep is scoped to
  `pt/`).
- **Disclosure recorded by X** (NOTES N9): during its sweep it listed the top-level names and mtimes of `pt/audit/`
  (to attribute the directory mtime) and read no file there. Names only; the protocol's not-to-be-read list names
  files and subdirectories, none of which was entered. Accepted.
- Reads: `pt/U/` never read (names and mtimes only in listings). Writes: `pt/X/` only, plus the slip above.

## Replays
Run as `python3 -I -B` from `pt/audit/X/replay/` (the scripts copied there; none reads argv or `pt/base`). All eight
reproduce stdout byte for byte (`cmp`); stderr differs only in my harness's exit-line format (`exit=0` against the
thread's `exit 0`), the first five bytes of a one-line file:

| script | checks | replay stdout |
|---|---|---|
| `x1_k1_core` | 20/20 | identical |
| `x2_k1_selfdual` | 10/10 | identical |
| `x3_g16_k4` | 20/20 | identical |
| `x4_k4_selfdual` | 6/6 | identical |
| `x5_seeds_vplus` (run 2) | 15/15 | identical |
| `x6_orth` | 6/6 | identical |
| `x7_numeric` [N] | guidance only | identical (seeds fixed) |
| `x8_fcc_crossnote` | controls green; FCC minima −1 and −1/2 | identical |

The recorded failed run (`x5_seeds_vplus.run1`, 14/15, the thread's own countercontrol object `prodState(e1,e1)` is
CNOT-fixed and so was not a control) was not re-executed; its record is consistent with RESULT §4 and NOTES N7.

## Independent check (no thread code)
`indep_checkQSD.py` (shared with the U audit; written from the landed definitions and the two result files' claims,
not from either thread's scripts; own `pauliW`, `ipW`, `cnot` = conjugation by CNOT, PSD by characteristic-polynomial
sign alternation, the surgery `Π(q) = q − (ipW(q,e)/ipW(e,e)) e`). Twenty-five checks in five sections:
- **S** spectra and the orthonormal `f_s`; `ipW(e_s, e_t) = δ/4`; `F = e_(−1,−1)`, `cnot F = e_(1,1)`, `cnot E0 = E0`.
- **H1** the two sum-of-squares identities, symbolic over the whole ball; `pauliW(prodState x y) = ρ(x) ⊗ ρ(y)`.
- **H2** the landed sign/permutation tables of `cnot` equal CNOT conjugation on all 16 basis tables; the landed
  `frame`/`relT`/`relC` predicates over all 4096 dressings select 32 gates, the (even, even) class has 8 and
  generates a group of order 16, equal to `⟨cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩`, which permutes the orbit; `⟨E0, Ad(Z⊗I)E0⟩ = −1`.
- **H3** the 2×2 determinant identity behind the rank-one surgery; `ipW(q, e_s) = tr q/2 − ⟨f_s|q|f_s⟩` for a symbolic
  Hermitian `q` (so at most one orbit constraint is violated); rank-one batteries for `E0` (51 cap vectors) and `F`
  (11), all surgeries PSD; a rank-two instance; `ipW(E0,E0) = 3`, `−E0 ∉ PSD`; countercontrol `e_{3/2}` (eigenvalues
  `−1/2, 1/4, 1/4, 1`), whose surgery fails exactly where the lemma says it must.
- **W** the witness pairs `(E0, G)`, `(F, T_ψ)`; the FCC violations `−1` (uniform `K(E0)`) and `−1/2` (uniform `K(Z_F)`,
  at `F`, with `cnot F` giving `+1/2`) through the audited identity `fourVal X Y E F = ipW(E, X F Yᵀ)`; `Y1 = E0^Γ`
  with `⟨Y1, cnot Y1⟩ = −1`; `F + cnot F = (E00 − E31)/2 ⪰ 0`.

**Runs.** Run 1 (kept as `indep_checkQSD.run1.*`): 20/25, five harness errors, no claim affected — H1b (the sign of
the bilinear term: `4 ipW(e_s, prod) = 1 + xᵀM_s y`, so the square is `|x + M_s y|²`), H1c (symbolic zero test needed
expansion), H3c (a battery too small: 9 cap vectors; enlarged to 51 with normalized eigenvectors), H3e (unnormalized
eigenvectors put the countercontrol's `k`-range outside the failing region), W3 (X's `e_(1,1)` is `F`, U's
`z_(−1,−1)`; run 1 used `cnot F`). Run 2 (kept as `.run2.*`): 24/25, the twenty other lines identical to run 1; the one
MISMATCH was again H3e, this time because my predicted failure set (`k ≥ 8`, from the sufficient direction
`w = t g − f`, `⟨w|ρ(e)|w⟩ < 0 ⇔ t² > 1/2`) was coarser than the truth: the countercontrol failed at `k = 7…14`. The
exact boundary, derived and then checked: with `v = g + t f`, `⟨q, e⟩ = t² − 2`, `⟨e, e⟩ = 11/2`, the surgery is
`vv† + τ′ρ(e)` with `τ′ = 2(2 − t²)/11`, whose `span(g, f)` block has determinant `(τ′/8)(2 − 4t² − τ′) ≥ 0 ⇔ 21t² ≤ 9`,
while the complementary block is `τ′·diag(1/4, 1) ≻ 0`; so the surgery fails iff `t² > 3/7`, i.e. exactly `k ≥ 7`
(`k = 15` is outside the cap). The countercontrol behaves as the lemma predicts; only my stated boundary was off.
Run 3 (kept as `.run3.*`) carried the corrected prediction but crashed inside the H3e line on a tuple-indexing
mistake in my patch (`r[1][0]` for `r[0]`; a `TypeError`), after printing the same 24 lines as run 2 up to H3d; the
corrected expression was tested on synthetic data before run 4. **Run 4, the final run: 25/25 CONFIRMED,
`VERDICT INDEP-QSD-CONFIRMED`**, exit 0; H3e reports failures exactly at `k = 7…14` (8 of 14 tested); every line other
than H3e is identical to run 2, and every line other than the five fixed in run 2 is identical to run 1. A second,
concurrent execution of the same script (`indep_checkQSD.replay.*`) is byte-identical to run 4 on stdout and stderr:
reproducibility of the coordinator's check, not a second proof. Final hashes: script `518b4952…`, output `cdd04849…`
(= replay), stderr `19eaf438…` (`exit=0`); kept runs: run 1 `bbeb49bd…`/`c50e5ed4…`, run 2 `cae55757…`/`61911ef2…`,
run 3 `10f144e5…`/`9705d194…` (script/output). Full hashes in the stage-3 evidence manifest.

**What the independent check establishes for X's claims.** Every certificate X's EXOTIC label rests on is
re-established by a separately written computation: the spectra and the orthonormal `f_s` (S1–S3); `F`'s identity
with an orbit vector and `cnot`'s action (S4); both H1 identities symbolically over the whole ball (H1a–b) and
`pauliW(prodState) = ρ ⊗ ρ` (H1c); `cnot` = CNOT conjugation on all 16 basis tables (H2a); the native class from the
landed predicates — 32 gates, 8 even-even, order 16, equal to `⟨cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩`, permuting the orbit
(H2b–d); the level-(ii) exclusion of `E0` and the IE1 failure (H2e); the ingredients of SD1/SD2 — the determinant
identity, the one-active-defect identity, rank-one surgery batteries for `E0` and `F`, the rank-two instance,
`ipW(E0,E0) = 3`, `−E0 ∉ PSD` — with the countercontrol `e_{3/2}` failing exactly at the derived boundary (H3a–g);
the witness pairs, both FCC violations, `Y1`, and `F + cnot F ⪰ 0` (W1–W5).

**What each layer of this audit establishes, kept apart.** The thread's own replays and the coordinator's replays
show that the thread's scripts are deterministic and that their recorded outputs are what the scripts print:
reproducibility. The concurrent replay of `indep_checkQSD.py` shows the same for the coordinator's script. Neither
is evidence of mathematical correctness. Correctness rests on three separate things: the written proofs (SD1, the
characterization, SD2, EBF, the orthogonal-image and decomposability arguments), re-derived below step by step; the
coordinator's exact checks, implemented from the landed definitions without either thread's code, with their own
countercontrols; and the convergence of two threads that never read each other on the same construction. A
reproducible script with a wrong decision rule would replay identically; that is why runs 1–3 of the coordinator's
script, each failing on a harness error of its own, are kept and listed rather than discarded.

## Written proofs reviewed

Each proof was re-derived step by step. Verdicts: CONFIRMED (no gap), CONFIRMED WITH NOTE (correct; a remark is
recorded), or a named gap.

**Lemma SD1 (single defect) — CONFIRMED.** Setting: `Q = PSD(4)`, trace pairing, `e ∉ Q`, `e ⪰ β(I − 2gg†)`.
1. Closedness: `tr e ≥ 2β > 0` (the trace of `β(I − 2gg†)` is `2β`), so `−e ∉ Q`; `(Q ∩ e*) ∩ (−ℝ₊e) = {0}`; a sum of
   closed convex cones meeting only in 0 in this sense is closed. ✓
2. `K ⊆ K*`: four nonnegative terms. ✓
3. `K* = e* ∩ (Q + ℝ₊e)`: `(A ∩ B)* = cl(A* + B*)`, `Q* = Q`, and the sum is closed by step 1. ✓
4. Reduction to (GL): correct; `s ≥ τ` follows from `⟨y, e⟩ ≥ 0`. ✓
5. From the local lemma to (GL): the set `{σ ≥ 0 : z + σe ⪰ 0}` is a closed interval (PSD is closed and convex),
   bounded because `e ∉ Q` (otherwise `z/σ + e ⪰ 0` for all large σ, and in the limit `e ⪰ 0`). At `σ_hi < τ` the
   point `w = z + σ_hi e` is PSD with `⟨w, e⟩ = ⟨e, e⟩(σ_hi − τ) < 0`, and the local lemma extends the interval. ✓
6. The local lemma: some eigenvector `u` of `w` with positive eigenvalue has `⟨u|e|u⟩ < 0`, hence `|⟨g,u⟩|² > 1/2`;
   unit `k ∈ ker w` is orthogonal to `u`, so `|⟨g,k⟩|² < 1/2` and `⟨k|e|k⟩ > 0`; `e` is positive definite on `ker w`,
   and the Schur complement of `w + εe` in the block decomposition `ker w ⊕ (ker w)⊥` tends to the positive-definite
   block of `w`, so `w + εe ≻ 0` for small ε (trivial when `ker w = 0`). ✓

**Characterization of self-dual `K(e)` — CONFIRMED WITH NOTE.** (⇐) is SD1 with `β = −λ₁`. (⇒): with `u, w` as
stated, `⟨u|e|u⟩ = ⟨w|e|w⟩ = (λ₁ + λ₂)/2 < 0` in both cases, `z = uu†` cannot move along `+e` because `w ∈ ker z`
and `⟨w|e|w⟩ < 0`, and (GL) is necessary for self-duality. *Note:* the necessity step uses only the direct
computation `⟨z + τe, k⟩ = ⟨z, q⟩ + τ⟨e, q⟩ ≥ 0` for `k = q + λe ∈ K`, so it does not depend on the dual formula of
step 3 and needs no closedness hypothesis; the trichotomy (`e ⪰ 0`; exactly one negative eigenvalue with
`λ₂ ≥ −λ₁`; otherwise) is exhaustive, so the characterization is complete as stated. The exact instances (`E0`,
`e_s`, `e_{3/4}` accepted; `e_{3/2}`, `(|φ⟩⟨φ|)^{T_B}` rejected) agree with it.

**Lemma SD2 (orthogonal defects) — CONFIRMED WITH NOTE.** The sequential surgery is valid: by orthogonality,
`⟨z_{j−1}, e_j⟩ = ⟨z, e_j⟩`, and (GL) for `e_j` applies to the PSD matrix `z_{j−1}`; closedness and the dual formula
use `tr e_i > 0` (an element `−Σ s_j e_j` of `Q` would have negative trace). *Note:* SD2 does not need U's hypothesis
"every `q ∈ Q` violates at most one constraint" (Theorem S (b)); the sequential argument handles several violated
constraints at once. For the Bell-type defects both hypotheses hold anyway (at most one of the four `f_s`-diagonal
entries of a PSD `q` can exceed `tr q/2`), so the two proofs of self-duality of `K4 = K_F` are independent and
mutually consistent.

**The instance `E0` and the instance `K4`** — the exact certificates (`pauliW(E0) − ¼(I − 2gg†) = ½ f₃f₃†`,
`pauliW(e_s) = ⅛(I − 2ψ_sψ_s†)`, `ipW(e_s, e_t) = ¼[s = t]`, the SOS identities for H1, `cnot E0 = E0`, `cnot` =
conjugation by CNOT, the group computations) are re-established in the independent check (sections S, H1, H2, H3).

**EBF (equivariant Barker–Foran) — CONFIRMED.** Steps 1–5 re-derived. Step 1 uses that `y₀ = ∫ gy dg` is the
orthogonal projection onto `V^G`, so `u = y − y₀ ⊥ V^G` and the cross terms vanish. Step 2's closedness:
`m = −Σλ_i h_i z_t ∈ M` gives `⟨m, m⟩ = −Σλ_j ⟨m, h_j z_t⟩ ≤ 0`, so `m = 0`; and `cone(G z_t)` is closed because `G z_t`
is compact and avoids 0. Step 3's case analysis (`c ≤ 0`; `c > 0` with `t* < 1` contradicting `|y₀|² ≥ t* c |u|²`;
`u = 0`) is complete. Step 4 uses that a continuous nonnegative function with zero Haar integral vanishes. Step 5
needs a nonzero element of `M`, which `V^G ≠ 0` supplies (a fixed vector `v` has `⟨v, hv⟩ = |v|² ≥ 0`, so step 2 puts
it in `M` even when `M = {0}` is the start). The theorem is non-constructive; X uses it only for the torus row and
for the "no stall" remark, both labelled [W].

**X1(a), orthogonal images via Jordan maps — CONFIRMED.** Rests on ORTH.W (audited at stage 2) and the exact
commutant dimensions [X x6 O2]. Step 1 (`M_A(p)` is a rank-two projector, `M_A` unital Jordan) ✓; step 2 (three
anticommuting Hermitian involutions, `Σ = −iS₁S₂S₃` a central involution) ✓; step 3 (`Φ(p ⊗ q) = M_A(p) M_B(q)`
from four orthogonal rank-one projectors summing to `I`) ✓; step 4 (the mixed type has commutative commutant, which
cannot host an anticommuting pair squaring to `I`) ✓; step 5 ✓. This is a second, independent proof of U's local
Wigner theorem (U proves it through slices and a cross-ratio; see AUDIT-U).

**Decomposable cones — CONFIRMED.** Pure products are extreme rays of `maxCone = dualW SEP`: for `p = prodState a b`
with `|a| = |b| = 1`, the pairing with `hom(−a)` on the control side vanishes identically, so each summand
annihilates `u = (1, −a)`; a linear functional nonnegative on the Lorentz cone and vanishing at the lightlike `u`
vanishes on the two spatial directions orthogonal to `a` (take `α → ∞` in `4αβ ≥ γ₁² + γ₂²`), hence is a multiple of
`x ↦ ⟨hom(a), x⟩`; the same on the target side gives `k_i ∝ hom(a) hom(b)ᵀ`. An extreme ray of a direct sum lies in
one summand; the pure products form a connected set covered by the two closed subsets "in `V₁`" and "in `V₂`", so
all lie in one summand, which they span. ✓

**Linear images, symmetric cones, LU-invariant cones** — the reductions are correct given the [L] inputs named
(`Aut(PSD₄)` and its closure under positive square roots; Jordan–von Neumann–Wigner; Schmidt). Labels [W + L] are
right; nothing kernel-checked is claimed for these rows.

**The cross-note (FCC) and "IE1 fails for both cones" — CONFIRMED, one argument supplied.** The FCC values are
recomputed in the independent check (W2, W3) with the audited identity `fourVal X Y E F = ipW(E, X F Yᵀ)`. For `K1`
the IE1 failure is exact: `⟨E0, Ad(Z⊗I)E0⟩ = −1` (x3 G1; independent check H2e). For `K4` the RESULT gives [W]
without an argument; here is one. A local rotation `R` preserves `Q3` and `ipW`, so `R(K4) = K(RX)` is self-dual, and
`R(K4) = K4` iff `R e_s ∈ K4` for all `s` (a self-dual cone inside a self-dual cone equals it). `R e_s = E00/2 − T′/4`
with `T′` the pure table of `ψ′ = (U ⊗ I)ψ_s`. If `ψ′ = Σ c_t ψ_t` is not one of the `ψ_t`, write
`R e_s = q + Σλ_t e_t` with `q ⪰ 0`: the trace gives `Σλ_t ≤ 1`, and `⟨ψ′|ρ(q)|ψ′⟩ ≥ 0` gives
`Σλ_t(2|c_t|² − 1) ≥ 1`, impossible when `max_t |c_t|² < 1`. So a generic local rotation moves `e_s` out of `K4`,
and IE1 fails for `K4` as well. [W, coordinator]

## Corrections (wording; no label changes)
1. §0 "no flagged premise is used": correct for the four cones; the torus row and the LU row use flagged symmetries
   as *class restrictions*, as §2 states. No change needed; recorded so the integration note quotes §2, not §0.
2. §0 "IE1 fails for both cones [W]": for `K4` the argument was missing from the record; supplied above.
3. §1 X1(a) step 5 cites K2Guard.lean:101–143 for "twin is not cnot-invariant"; the kernel facts there are
   `cnot idW = chainW` and `chainW ∉ maxCone`; the inference `twin` not invariant is [W + X] (x1 D1c), as U states it.
4. SD2 is stronger than Theorem S in one hypothesis (note above); the integration note records the two proofs as
   independent routes to the same cones.

## Verdict for integration
EXOTIC at level (i) (`K1 = K(E0)`; the family `K(e_c)`, `c ∈ (1/2, 1]`; `K({F, cnot F})`) and at level (ii)
(`K4 = K(Z_F)`), each hypothesis exact or [W] over exact certificates, controls green, no flagged premise in any
cone; the class rows as labelled ([W + L] where marked; the torus row existence-only; spectrahedral class open).
The route "uniform pair self-duality ⇒ FCC" is refuted exactly (x8; S3 rows 7 and 9). The independent check
(25/25, run 4, replay identical) confirms every exact certificate the label rests on. **Audit verdict: X's EXOTIC
stands as stated, at levels (i) and (ii).**
