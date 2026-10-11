# Audit — `research/countermodels`, round 5 (head `c9ac75bd`)

Coordinator's audit of the countermodels thread's round-5 report (nodes C22 and C23; C24 and C25 carried forward by the
owner's direction of 10:38Z), from the round-4 head `644bf0a1`, against the certified base L = `9f9f8257`. Method as in
rounds 1–4, plus the owner's round-5 checks. Evidence levels: [K] kernel at L; [D] design module built in CI on a
disposable branch (not certified); [X] exact computation; [W] written; [N] numerical (not a certification);
[A] audited record.

## 1. Receipts

HO-18 v2, HO-27, HO-28, HO-33, HO-34, HO-35, HO-36, copied into `inbox/` at `7f38a089`: 7/7 byte-identical to the
overview's files at `4c4a02b1`.

## 2. Provenance

- Eight commits `644bf0a1..c9ac75bd`, all by `Claude (research countermodels)`; every changed path is under
  `research/countermodels/`. `LOG.md` and `RESULTS.md` are append-only across all eight commits (each version is a byte
  prefix of the next); no earlier row changed.
- Dev branch `dev-countermodels/c22-compact`: `6cb76f96` (one commit on L), `e4ef2e46` (one commit on `6cb76f96`),
  `a69987bd` (one commit on `e4ef2e46`); changes only under `verification/lean-mathlib/` (the root import file, the
  carried `CmSprime`, the design module `CmSprimeCompact`). The committed texts are byte-identical to the modules of the
  three dispatches: `lean/CmSprimeCompact.lean` = `a69987bd` (the green build), `.run38124380741.lean` = `6cb76f96`,
  `.run38125067948.lean` = `e4ef2e46`; the carried `CmSprime` is the round-4 module.
- The interruption of 08:34Z: of the four uncommitted files recorded, `CmSprimeCompact.run38124380741.lean` is committed
  unchanged; the recorded `CmSprimeCompact.lean` (`5b447af0`) is the `e4ef2e46` module, kept as `.run38125067948.lean`
  and then replaced under Amendment A1 (committed at `114fc688`, before the third dispatch); the recorded `LOG.md` is a
  byte prefix of the committed one; the recorded `NOTES-C23.md` (`b1683d44`, the S0 draft) is preserved here as
  `countermodels/thread-scratch/NOTES-C23.draft-0834.md` (same digest; the thread had kept it only in the session
  scratchpad, which does not survive the session).
- The C23 S0 revision, ordered from the thread's transcript (`countermodels/TRANSCRIPT-C23-EVENTS.txt`): draft written
  08:34:52Z; scratch searches `x23_tight.py`, `x23_exact.py`, `x23_exact2.py` 10:24:37–10:25:40Z (preserved in
  `thread-scratch/`; they chose the tightness parameters, as NOTES-C23 discloses); draft copied 10:26:04Z; `NOTES-C23.md`
  rewritten 10:27:15Z and 10:28:55Z (the last write of S0); `c23_torus.py` written 10:31:14Z; its pre-run edits and run 1
  in one command at 10:31:53Z; `c23_check.py` written 10:33:26Z and run 10:33:52Z; the Runs section appended 10:35:24Z.
  So S0 was fixed before either C23 script existed. The revision keeps the draft's decision rule (EXPLICIT / OBSTRUCTED
  / OPEN on the same two conditions) and tightens it: it adds the two identities, the partner, zero-pairing and
  tightness instances, the product-in-orbit instances and the independent checker as conditions.
- Logged deviations, checked: C22's third dispatch under Amendment A1 with the FAILED (design) verdict of the
  pre-registered plan kept as its own row (C22.2f); the failed preflight runs and design texts kept; the time placeholder
  "10:2xZ" corrected by a later appended note, no earlier line edited.

## 3. Replays

The three round-5 scripts replay byte-identically (stdout): `c22_preflight`, `c23_check`, `c23_torus`
(`countermodels/REPLAY-LOG.txt`); the replay of `c23_torus` regenerates `c23_certificate.json` byte-identical to the
committed file (sha256 `d5841161…`).

## 4. Independent check

`countermodels/indep_checkC5.py`, decision rule fixed in its header before run 1; reads nothing the thread wrote
(the engine's local condition is taken from the statement of `selfDual_of_local`, CmSprime.lean:705, read as a
statement); exact (Fractions, sympy), floats only in one item labelled [N]. Run 1: **INDEP-C5-FIXED**, Z1–Z5 PASS,
CC1–CC5 all False; replay identical. What it establishes, rebuilt from the definitions:

- **Z1, the group.** `R_B(t) = D(1, w)`, `CNOT D(u, v) CNOT = D(v, u)`, `X_B D(u, v) X_B = uv D(1/u, 1/v)`
  (symbolic). `G_1` and `G_2` enumerated exactly modulo phase have orders 16 and 64; every element is monomial with
  permutation in `V4 = {e, (23), (01)(23), (01)}` and phases with `φ₀φ₁ = φ₂φ₃`; the diagonal part is
  `{D(u, v) : u, v ∈ μ_{2ⁿ}}`. This confirms the membership test the thread's checker uses on the finite stages; the
  density of the dyadic points and `cl(G_∞) = T² ⋊ V4` stay [W]. Countercontrol: `1 ⊗ R_345` fails the test (CC1).
- **Z2, Lemma C23-1.** The identity `⟨h|D(u, v)X_B h⟩ = β + uvβ̄ + uα + vᾱ` and the modulus identity, in real
  coordinates. Exhaustively over the 6560 nonzero `h` with components in `{−1, 0, 1} + i{−1, 0, 1}`: the five-class
  formulas give a unimodular Gaussian-rational `(u, v)` with `⟨h|D(u, v)X_B h⟩ = 0` for every one, and the orthogonalizing
  family has rank 3 on all 2560 class-(i) vectors, rank 2 on all 1536 class-(ii) vectors and on all 2048 class-(iii)/(iv)
  vectors with one zero coordinate — the rank classification of C23-3 on the whole grid. Own seeds in all five classes.
  Countercontrol: `(u, v) = (1, 1)` does not orthogonalize the class-(i) seed (CC2).
- **Z3, the `c = 2` corner** — see finding F-C5-1 (§8).
- **Z4, Theorem C23-2(a).** With `λ = (c* − 1)/(4 − 2c*)` and `y = P_h + λd_{gh}`, identically
  `⟨y, d_k⟩ = (c* − c_k)(1 + λ) + c_k s′(1 + λc*) + c_k r` (`s = |⟨ĥ|k̂⟩|²`, `s′ = |⟨ĝh|k̂⟩|²`, `r = 1 − s − s′ ≥ 0`), so the
  witness pairs nonnegatively with every rank-one defect of weight at most `c*` on any ray, and
  `⟨d_k, d_h⟩ − (4 − 2c*) = (c* − c_k) + c_kc*s ≥ 0` (Lemma C23-5's input). Exact instance on own seeds (`(1, 2i, 3, 1)` at
  `c* = 1001/1000`, `(2, 1, 1, 3)` at `2001/2000`, both with H1): `⟨y, d_h⟩ = 0`, `(gh)†y(gh)/|gh|² = −1/1998000`, 200 orbit
  samples with pairing `≥ 0` equal to the identity. Countercontrol: the witness built at the smaller weight pairs
  `−3999/7996000` with the larger-weight copy of `d_h` (CC4).
- **Z5, Theorem C23-3.** The zero-pairing formula for balanced defects; with `gh ⊥ h` and positive pairing the local
  condition fails at `u = h`, `x = gh`; own seeds: class (i) has no partner (`{k ⊥ partners, k ⊥ h} = {0}`), classes (ii),
  (iii), (iv) have a one-dimensional partner space with zero pairing on all eight orthogonalizing `g`, and a fixed exact
  search finds a tightness violation for each (`U = D(e, 1)` near the identity; normalized `x†(UdU†)x` about
  `−7.4·10⁻²`, `−5.6·10⁻²`, `−3.8·10⁻²`). Countercontrol: a partner not proportional to `k₀` does not have zero pairing (CC5).

## 5. Citations

`cite_check_r5.py` over the thread's added text (inbox excluded): one kernel citation, JordanClassification.lean:84 at
L — `theorem psd_iff_trace_nonneg`, the kernel's PSD self-duality the citing line names (read by hand; the checker's
window rule needs the identifier on the same line). The five other citations are to Mathlib, outside the checker's
scope; each resolves at the pinned tag `v4.33.0` (`lakefile.toml` at L) to the declaration the citing line names
(`cite_mathlib_c5.out`). 6/6.

## 6. CI

Three dispatches, verified at job and step level from the saved job logs (`CI-RUNS-R5.md`): `38124380741` @ `6cb76f96`
and `38125067948` @ `e4ef2e46` Build failure in `CmSprimeCompact` (8 and 6 `sorryAx` prints); `38131214451` @ `a69987bd`
Build success, `CmSprimeCompact` 38/38 and `CmSprime` 78/78 standard, `lean-axioms` 5976 with no sorry, gate red only at
`lean-manuscript` (the two design modules); 33 jobs, 32 success. None cancelled. Tail-capped saved logs, not complete logs.

## 7. Lean statement review (C22)

`theorem_Sprime_compact`: hypotheses — `κ` compact and nonempty, `n` nonempty, `c` and the seed map continuous, unit
seeds, `1 < c k ≤ 2`, `c k < card n`, pairwise nonnegative pairings, (CC) in cap/co-cap form on every ordered pair of
positive pairing; conclusion — `surgeryC` (the closed conic hull) is self-dual and closed. The proof applies the
round-4 finite Theorem S′ to every finite subfamily and passes to the compact family through
`dualH_subset_surgeryC_of_finite` (a compactness argument with explicit bounds `τ = card n − max c` and entry bound 3).
`_ineq` (CC in inequality form) and `_C4` (`ℂ⁴`, `c < 4` automatic) are corollaries; `control_compact_single_defect`
shows non-vacuity. Matches C22.1; label CONJECTURE [D] as design evidence. C22.3's remark (`cone Z` closed for compact
`Z` with `tr ≥ τ > 0`) is [W] and not in the module, as the row states.

## 8. Finding F-C5-1 — the Bell circles are not a `G_T`-orbit (C23-2 (b)–(c))

**Statement.** C23-2(b) (NOTES-C23, row C23.2, HP-countermodels-11) asserts that at `c = 2` the only orbit admissible
for H1 is `C1′ ∪ C2′`, `C1′ = {|00⟩ + w|11⟩}`, `C2′ = {|01⟩ + w|10⟩}`. For `G_T` this is false: `CNOT ∈ G_T` carries
`|00⟩ + w|11⟩` to `(|0⟩ + w|1⟩) ⊗ |0⟩`, a product, so the `G_T`-orbit of every Bell state of `C1′ ∪ C2′` contains
products and H1 (with H3) admits no defect of weight `c > 1` on it. The argument of (b) covers the torus and `X_B`, not
`CNOT`; it was already in the 08:34Z draft. The thread's own records agree with the correction: the `D_min` formula of
G3 gives `D_min = 0` for these seeds, and C23-3(c) excludes `(h₀, 0, 0, h₃)` and `(0, h₁, h₂, 0)` by H1 because `CNOT`
maps them to products. The bridge established the correct statement in the same round (B21 G4: no `G`-orbit is
admissible at `c = 2`; `b21_ceq2` Q3–Q5 with the countercontrol without `CNOT`, replayed in the bridge audit).

**Verification [X] (Z3, CC3).** The determinant identities `det Ψ(D(u, v)h) = v(h₀h₃ − u²h₁h₂)` and
`det Ψ(CNOT D(u, v)h) = u(h₀h₂ − v²h₁h₃)`; for each of 20 Bell states (ten rational `w`, both circles) the state is
maximally entangled, its `CNOT` image is a product, and the `c = 2` defect of the image pairs `−1` with it. The four
sum-of-squares identities `S/2 ∓ x`, `S/2 ∓ y` (`x = a₀a₃ − a₁a₂`, `y = a₀a₂ − a₁a₃` in the moduli) show that
`|x| = |y| = S/2` forces `a = 0`: no `G_T`-orbit is maximally entangled throughout. Countercontrol: under `T² ⋊ ⟨X_B⟩`
alone the orbit of `|00⟩ + |11⟩` stays maximally entangled at every sampled point — `CNOT` is load-bearing.

**A sharper bound (coordinator's observation; [W] + [X] Z3(d), [N] Z3(e)).** `x + y = (a₀ − a₁)(a₂ + a₃)` and
`x − y = (a₀ + a₁)(a₃ − a₂)`, so `|x| + |y| = max(|x + y|, |x − y|) ≤ S/√2` and the orbit minimum `D_min ≤ 1/8` for every
`h`, attained exactly at `(√2/2, 0, 1/2, 1/2)` (random search: max `0.1237`). Hence H1 admits a rank-one defect orbit of
`G_T` only at weight `c ≤ 2/(1 + 1/√2) = 4 − 2√2 ≈ 1.1716`.

**Consequences.** (i) C23-2's conclusion at `c = 2` stands for a different reason — no `G_T`-orbit is H1-admissible
there — so row C23.2's verdict and C23.4 (OBSTRUCTED, which rests on C23-1 and C23-3) are unchanged; the transported
`K_T` pair is a correct computation about `(1 ⊗ H)K_T(1 ⊗ H)†`, a cone invariant under `T² ⋊ ⟨X_B⟩` but not under
`G_T`. (ii) For mixtures (c): a `G_T`-invariant defect set containing a Bell defect at `c = 2` contains the `c = 2`
defect of its `CNOT` image, which H1 excludes; the instance `(3, 2i, 2, 1)` is likewise a statement about
`T² ⋊ ⟨X_B⟩`. (iii) So C23.6's first residual item does not arise for `G_T`: under H1 every `G_T`-invariant rank-one
surgery has all weights `≤ 4 − 2√2 < 2`, and C23-2(a) applies to it — the rank-one route for `G_T` is closed with no
residual. That item remains a question for the subgroup `T² ⋊ ⟨X_B⟩` only. (iv) No label change; the wording of C23-2(b)–(c),
row C23.2, C23.6 and HP-countermodels-11 is to be corrected forward by the thread in round 6 (the proposal is not issued
in its present form).

## 9. Hypothesis classification and reading

C22: cone geometry (no operation). C23: reading invariance; `G_T`-invariance is the (b)-instance under test; H1 and H3
are introduced (composite-cone conditions, not OI premises); no OI inventory item is used; scope — the stage-6
inventory at L, level (i). Lemma C18-1, C13-O, the engine's statement (C17.1 [D]) and C22.1 [D] are cited at their
labels. The obstruction concerns the surgery and engine routes only, not every cone, every extension of OI, or
availability — as the thread states. Nothing in C23 is evidence for outcome (D) (no cone is produced).

## 10. Other observations

- **Scope of "the engine certifies nothing" (C23-3).** `selfDual_of_local` takes a finite family; what C23-3 and Z5
  establish is that its local condition fails on a pair inside every `G_T`-orbit, which also blocks any compact
  extension with the same local condition. Stating it that way is more exact; no change of substance.
- The universal orthogonal pair on the tower's closure was derived independently by both threads in round 5 (bridge
  B21 in `U(u, v)` coordinates, countermodels C23 in `D(u, v)` coordinates); the two parametrizations agree modulo phase.

## 11. Labels

No label changes: C22.1 CONJECTURE [D]; C22.2f FAILED (design); C22.3 CONDITIONAL [W]; C22.4 CONDITIONAL; C22.4f
FAILED (kept); C23.1–C23.5 CONDITIONAL, with F-C5-1's correction to C23-2(b)–(c) carried forward; C23.6 OPEN, its first
item not arising for `G_T`; C24.0, C25.0 OPEN (carried forward).

## 12. Carried to round 6 (countermodels)

- F-C5-1: correct C23-2(b)–(c), row C23.2, C23.6 and HP-countermodels-11 forward (no `G_T`-orbit H1-admissible at
  `c = 2`; the weight bound `4 − 2√2`; the Bell-circle mixtures as a `T² ⋊ ⟨X_B⟩` question only).
- C24 (T on `K_circ`) and C25 (pair cones over `Ω_h`).
- From C23.6: balanced rank-two surgeries without the engine; defects with a higher-rank subtracted part; non-surgery
  constructions; an explicit `G_T`-invariant exotic cone (existence at claim (D) [A]).
- Handoff proposals HP-countermodels-10 and -11 await issue at the round's close (-11 after the correction).
