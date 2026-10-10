# Thread S3 — COMP-CONS: running notes (stage 2, launch 2; research only)

Directory `pt/S3/` is the only place this thread writes. Governing texts: `PROTOCOL.md` (`239dc123…`),
`PROTOCOL-AMENDMENT-1.md` (`b41aa0e7…`), `PROTOCOL-AMENDMENT-2.md` (`2a2f78f3…`), `PROTOCOL-STAGE2.md` (`38603692…`),
hash-verified at start. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` read-only at `pt/base/`. No Lean
toolchain: any Lean text is UNBUILT. No git write, CI, GitHub, publication or agents.

## N0. Start (integrity)

`.start_marker` written first (2026-10-10T07:26:30Z), before any other file in `pt/S3/` (which was empty):
inputs, stage1 and inputs2 manifests `sha256sum -c --quiet` rc=0; base HEAD = L; base status empty; the four protocol
hashes equal their recorded values.

## N1. Reading log

Read in full, in order: PROTOCOL, amendment 1, amendment 2, PROTOCOL-STAGE2; STAGE2-LAUNCH-LOG; INTEGRATION-REVIEW;
audit/C/AUDIT-C (including the narrowed B3: B3 holds for chart-invariant conditions on cones and gate *maps* of at
most three pairs; it fails as stated for conditions reading the supplied locals); C/RESULT.md, C/NOTES.md;
audit/A, audit/B, audit/D. Design modules (pt/inputs/fourcopy): FourCopyDefs (FCC famI/famII, ipW, dualW, PairAdm,
cnotTw, gateOf, EvenCycle4), FourCopyCore (fourVal, PairLinked, flatW, pairBody, tabCoord, TokenCoherent, KT4,
KT4Core, NClass, bellOf, Theta, orient, IE1, Pr, FCC, EvenCycle), FourCopyBridge (Lemma R targets 01/02, B1a,
O21 `exists_effect_of_dualW`, KT4.toCore, core_valI/II, Lemma B1), FourCopyHeadline (ie1_all, parity_all,
kt4_general_ie1, kt4_forward_ie1), FourCopyIE1 (cross_rel, link_mem, inv_*_ctrl/partner, rot_of_words, parity
witnesses), FourCopyPackage (KT4Cone, Lemma B2 with open sub-identities effA_prodA etc., chartR, twistQ3, Q3, twin).
Landed: KT4-PREM-1 result.md (whole), kt4_prem1_probe.py (whole; conventions reused), CompositeDimension.lean §L
(Lor, lor_pair_bound, isEffectOn_affOf, lor_ehom, pairVal_nonneg_of_maxCone, lor_of_forall_pair, lor_eq_smul_hom,
lor_hom), NativeGateBall/JordanClassification headers.

Exact FCC consumption in the design proof (read from FourCopyIE1/Headline, to be cited, not re-proved):
- cross_rel: PairLinked.upper at (X ∈ K, Y ∈ K' arbitrary; E, F = Bell tables of the link pairs) and .lower at
  (L, L' = Bell tables; e ∈ dualW K, f ∈ dualW K' arbitrary);
- inv_left/right_ctrl/partner: .lower at (one rotated link, one Bell table; e, f arbitrary in the full duals);
- parity: famI at four aligned-gate images (after IE1).
So the link-side arguments are gate-supplied; the target-side arguments range over full cones and full duals.

Certified elementary self-duality (anchor for one candidate): the ball's homogenized state vectors, its effect
coefficient vectors and the cone `Lor` coincide up to scale, and `Lor` contains its Euclidean dual —
`lor_hom` (CompositeDimension.lean:1679), `lor_eq_smul_hom` (:1590), `lor_ehom` (:930), `isEffectOn_affOf`
(:~913), `lor_pair_bound` (:877), `lor_of_forall_pair` (:1015). To be re-checked line by line before citing.

## N2. Productivity test, skepticism rule, decision rules (fixed before any script)

Productivity test (protocol, fixed): a finding is a gem iff (1) an exact certificate at a stated instance, (2) an
exact obstruction for a stated class of routes, or (3) an exposed hidden assumption; otherwise record-only.
Classes NEW / POSITIVE / ELABORATING / CONFIRMING / BORDERLINE. Fixed point: 3–4 passes without NEW, or answered.

Skepticism rule for favourable branches (a derivation of FCC): accept only after (a) the renaming test is written
(does the unfolded statement contain a cross term of effects of one grouping on states of the other, or a restriction
of it?); (b) each conjunct has an exact model where it is dropped and FCC fails; (c) the route is checked against the
forbidden list (IE1, IE2, Q3/PSD as premise, region tower, (o) steps, operation-level idle extension, target in other
words) and the flagged routes; (d) the principle's strength relative to FCC is fixed on stated families, with exact
witnesses for any strictness.

Renaming test, fixed now (applied to every candidate): a principle renames FCC iff its statement, with definitions
unfolded, contains as a clause (not as a derived consequence) the nonnegativity of one grouping's products of pair
effects on the other grouping's products of pair states, or a restriction of that clause to a sub-family of
arguments. Existential equivalence with FCC relative to the pair hypotheses is NOT by itself a renaming criterion
(to be justified in S3.3: relative to hcls ∧ hadm ∧ hcl ∧ hgate every quantum-compatible sufficient principle is
existentially equivalent to FCC, by the audited theorem and the classification).

## N3. Node plan (depth-first; decisive first)

- S3.1 ladder (owner's required separation): define rungs in the four-token table carrier W4 (four-copy local
  tomography built in, as Lemma B2's KT4Cone) and relate them to C's abstract-carrier N0/N1/N2. Exact items:
  (i) the four Lemma-B2 sub-identities (open `sorry`s in FourCopyPackage) as symbolic identities; (ii) exhaustive
  enumeration of linear orders and cyclic orders against the two groupings; (iii) an associative (one-grouping)
  composite with the M_tok cones, FCC −1/8; (iv) the induced pair of an A-composite: admissible but FCC fails on the
  induced pairs (exact witness).
- S3.2 candidates, decisive first: (a) self-duality at every level with state-level regrouping (grouping-blind;
  sufficiency is a two-line derivation; the decisive tests are the renaming test and drop-one countermodels);
  (b) pair-level principles with/without uniformity (single-pair chart obstruction; the two halves of self-duality
  under uniformity: K ⊆ K* foil uniform K_gen, K* ⊆ K foil uniform K_gen*); (c) token orientation coherence;
  (d) conditioning / no-restriction slot analysis (generated vs full arguments); (e) entanglement swapping,
  purification.
- S3.3 independence/obstructions; S3.4 the central question.

## N4. Scripts and runs (all `python3 -I -B`, from `pt/S3/`; Python 3.11.15, sympy 1.14.0)

- `s1_ladder.py <OIB>` (OIB = `../base/verification/lean-mathlib/OIBridge`). Pre-run edits (before run 1): the
  countercontrol I1c was rewritten so that it tests the failure of I1's product-marginal formula on prodB (the first
  draft stated a true identity, not a countercontrol); an unused variable was removed. Run 1: 33/33,
  `VERDICT S1-LADDER-EXACT`. Output kept as `s1_ladder.out`/`.err` (`.err` holds only `exit=0`).
- `s2_foils.py <OIB>`. Run 1 FAILED on a harness error: check C3 passed a 1x1 sympy Matrix (not its entry) to the
  zero test, which compares a Matrix with 0 and returns False. Kept as `s2_foils.run1.{py,out,err}` (26/27, exit 1).
  The fix (one line: take `[0, 0]` of the 1x1 product) touched only that check; run 2: 27/27,
  `VERDICT S2-FOILS-EXACT`; every other output line identical to run 1. The mathematics of C3 (reflY on the second
  token preserves the Lorentz form, so actT reflY maps maxCone onto maxCone) was never in question.
  NEW in s2: the dual foil uniform K_gen* (= maxCone n cnot maxCone): satisfies hcls, hadm, hcl, hgate and
  "dualW K <= K", fails FCC (fourVal E0 G phiW phiW = -1) and IE1 (octahedral witness H4).
- `s3_selfdual.py`. Pre-run edits (before run 1): the label of countercontrol D3c was garbled and was rewritten; an
  unused variable was removed. Run 1: 13/13, `VERDICT S3-SELFDUAL-EXACT`.
- `s4_conditioning.py`. No pre-run edits. Run 1: 11/11, `VERDICT S4-CONDITIONING-EXACT`. ESC witness on uniform
  K_gen: X = cnot(prodState e_x e_y), F = cnot(prodState e_y e_y), Y = cnot(prodState (-e_x) e_z), E = E0: -1.

## N5. Node verdicts so far (depth-first walk)

- S3.1 (decisive for the owner's separation). Ordered associativity never makes 01|23 and 02|13 both contiguous
  (L1-L2, exhaustive); stating cross-pairing needs a token identification across groupings (naturality of the 1-2
  exchange on products, B2.8); the KT4 pairs are the edges of the cycle 0-1-3-2-0 and the two groupings are its two
  non-crossing matchings (L3-L6). Associativity is blind to K02, K13 (A3, -1/8). The induced 02/13 pairs of an
  A-composite are admissible but need not compose (I4, -2): the failure is on the effect side. Full cross-pairing =
  state-level regrouping (free) + effect-level regrouping (exactly famI, famII: B2.3, B2.4). ELABORATING/NEW
  (the induced-pair witness and the state/effect split of the cross step are NEW; the rest elaborates C).
- S3.2(a) SDC: P3 & OVL4 & CSD2 => FCC (two-line derivation over B2.7). Drop-one models D1-D3; strictness X1;
  abstract-carrier form C1, C2 (no four-copy LT, no COMP-1 effect field). NEW (favourable: skepticism applied in
  N6 below).
- S3.2(b) pair level: single-pair chart obstruction (C1-C5); halves of self-duality under uniformity refuted by
  K_gen (K <= K*) and by the NEW dual foil K_gen* (K* <= K); full self-duality under uniformity: UNRESOLVED
  (exotic-cone question).
- S3.2(c) orientation coherence = coboundary = EvenCycle (O1); AG = EvenCycle on the aligned family (G1, G2);
  refuted alone by K_gen and K_gen*. NEW: AG reads only the gates.
- S3.2(d) conditioning: C1 refuted by K_gen, C2 by K_gen*, ESC by K_gen*; C1 & C2 suffice relative to the pair
  hypotheses on the aligned family [W over D + W+L]. NEW (exposed assumption: two-sided no-restriction).
- `s5_pairlevel.py`. Pre-run edit (before run 1): two countercontrols added (A2c: the 45-degree aperture is
  load-bearing; A3c: isometry is load-bearing). Run 1: 8/8, `VERDICT S5-PAIRLEVEL-EXACT`.

## N6. Skeptical pass on the favourable branch SDC (P3 & OVL4 & CSD2 => FCC)

(a) Renaming test (N2 rule). Clauses: P3 = two inclusions of product STATES into K4; OVL4 = pairwise overlaps of K4
    are >= 0; CSD2 = dualW K_p <= K_p. None is a clause "products of one grouping's effects are >= 0 on the other
    grouping's product states", nor a restriction of one. The cross clause is a derived consequence (two lines,
    s1 B2.7). Its cross-term content without CSD2 is SSCP (state-state cross positivity), which is incomparable with
    FCC on admissible closed cones (uniform K_gen: SSCP and not FCC, s2 G5 + D.W; uniform maxCone: FCC and not SSCP,
    s2 M1). PASS, with the caveat recorded: when the pairs are self-dual, SSCP and FCC coincide literally.
(b) Drop-one models: D1 (drop OVL4: M_tok), D2 (drop P3: M_tok with PSD16), D3 (drop CSD2: uniform K_gen with
    PSD16). Each shows insufficiency of the rest, not necessity.
(c) Forbidden list: no operation of any kind (so no IE1, IE2, (o) step, idle extension, region tower); no Q3/PSD
    premise (PSD16 and Q3 appear only as the satisfiability model). Flagged routes: not used.
(d) Strength: strictly stronger than FCC on admissible closed cones (s3 X1 with landed F.max); existentially
    equivalent to FCC relative to hcls & hadm & hcl & hgate (theorem [D], classification [W + L], chart-PSD16
    s3 T1/T2). The equivalence is forced for every quantum-compatible sufficient principle (S3.3), so it is not a
    renaming signal.
(e) Not supplied by SDC: the pair hypotheses; two-copy LT (W 3 typing); in the W4 form four-copy LT is built in; the
    abstract form needs bi-affine product data, TPS (C's N2) and a multiplicative inner product, and does not use
    COMP-1's prodEff_effect (the field where C's cross clause sits).
(f) Anchor: the elementary ball is self-dual for the Euclidean pairing at L [K]: lor_hom (CD:1679),
    lor_eq_smul_hom (CD:1590), lor_ehom (CD:930), isEffectOn_affOf (CD, before lor_ehom), lor_pair_bound (CD:877),
    lor_of_forall_pair (CD:1015). SDC asks that pairs and the four-token system inherit this, for the composed pairing.
Verdict: sufficiency proved [W + X]; independently motivated; not a renaming. Label for FCC: CONDITIONAL on SDC.

## N7. Passes and fixed point (§A.31)

- Pass 1 (nodes S3.1-S3.2): NEW — induced-pair witness I4 and the state/effect split of the cross step; SDC route;
  the dual foil K_gen*; AG = EvenCycle reads only gates; one-sided conditioning obstruction (two-sided
  no-restriction exposed); Lorentz exclusion and the orthogonal-image lemma (partial results on the exotic cone).
- Pass 2 (skeptical re-check of SDC, N6): ELABORATING — only the halves CSD2 and OVL4 are consumed; abstract-carrier
  form without four-copy LT or COMP-1's effect field.
- Pass 3 (hidden assumptions in the setting and in prior candidates): NEW — C's row 17 (symmetric monoidal
  composition) supplies the effect side of cross-pairing either through the passive two-grouping composite axiom
  (= N0 & N1 & N2, a renaming) or through the braiding of tokens 1, 2 idly extended to tokens 0, 3 being a state map
  (an (o)-type step, forbidden as a premise) [W]. Also: the W4 carrier builds in four-copy LT; the slot analysis is
  scoped to aligned gates.
- Pass 4 (missed candidates: strong self-duality, homogeneity, Jordan/KV, purification, no-restriction for four-token
  effects, the third grouping 03|12): ELABORATING — all per-pair forms fall under the single-pair chart obstruction;
  uniform forms reduce to the exotic-cone question; purification UNRESOLVED; four-token no-restriction with P3 is
  refuted by M_tok (the load-bearing no-restriction is the pair-level, two-sided one); 03|12 is the crossing matching.
- Pass 5 (evidence-level audit of every label: each [X] scoped to its instance; each [W] step named): CONFIRMING.
- Pass 6 (consistency with INTEGRATION-REVIEW §1-§2 and AUDIT-C; the narrowed B3 cited verbatim, not generalized):
  CONFIRMING.
Three consecutive passes (4-6) without NEW: fixed point.

## N8. Replays

All five scripts were replayed with the same arguments into `.replay.out`/`.replay.err` (08:32Z). `cmp` found every
`.out` and `.err` identical. The base status was empty and there was no `__pycache__` under `base/` afterwards. The
hashes are in RESULT §6. The s1 script hash still equals the one recorded at run 1 (`7609665c…`).

## N9. End integrity (2026-10-10T08:33:29Z)

- inputs, stage1 and inputs2 manifests: rc 0.
- Base: HEAD `9f9f8257…`, 0 status lines, no `.pyc`.
- Protocol hashes: unchanged.
- `pt/S3/`: 31 files, all this thread's, no subdirectory.
- No integrity event.

Writes after the end check:
- RESULT §6–§7 and these notes;
- no script or output was changed.
- Correction (same session, before the final hashes): the end-check file count was first written as 33. `ls -A` gives
  31: 3 records, 5 × 5 script files, 3 run-1 files. RESULT §7 and N9 now say 31.
