# Thread B (PAIR-ACT) — working notes and node log

Protocol: `pt/PROTOCOL.md` sha256 `239dc123b07cb83f354a0f9def3cc39f5fd025fb2f6b4f3c4ba3d3e0ddfa9b23` (verified at start).
Start checks: `.start_marker` (manifest silent, base HEAD 9f9f8257…, status empty).

## N0 — reading (done before any script)

Read in full: `base/.../round-kt4-prem-1-premise-audit/result.md`; design modules `inputs/fourcopy/FourCopy{Defs,Core,
Local,IE1,Bipolar,Parity,Tables,Bridge,Headline,Package}.lean` (Euler header); landed `CompletionAction.lean` (OPACT-1),
`CompositeInterface.lean` (COMP-1), `K2Guard.lean`, `K1Bridge.lean`, `RelcSelectBlock.lean` (CtrlGate),
`CompositeDimension.lean` (DIM-1: defs, NativeGate, cnot, positivity, phiW); landed probe `kt4_prem1_probe.py`;
ledgers EQ5-PREM result + audit (Part B), DEPGRAPH §7, ASSUMPTIONS §3–4, DEPENDENCY-MAP §6–7, EQ3-AUDIT (a),
OPACT-RESULT §0–1, ROADMAP K1/K2/K∞ rows.

Proof-path uses of hgate/hinv (to be checked as [source] in b1_consumed S1):
- `kt4_general_ie1`: hinv := inv_mem_of_orth(hgate) [Lemma R]; hbs := bell_mem(hgate); hbe := bell_mem_dual(hinv);
  ie1_all(hgate) → link_mem(hgate); parity_all(hgate, hinv) → parity_witnesses → bell_mem, bell_mem_dual only.
- So hgate is consumed at product states only — (L) the link family (link_mem), (BS) the Bell state (bell_mem) — plus,
  through Lemma R, at (BD) the Bell effect (bell_mem_dual). DEPGRAPH §7.2 already notes that the pre-locals are read
  only through orthogonality and reparametrized inputs.

## N1 — B1 node 1: the consumed clause CONS  [verdict: CONFIRMING + exact]

CONS(p) := (∀ a b, actC (A_p ∘ rotWord a b) (actT B_p phiW) ∈ K_p) ∧ bellOf A_p B_p ∈ dualW K_p.
(BS) is the instance a = b = 0 of (L). Script `b1_consumed.py` run 1: 33/33 PASS, VERDICT B1-CONSUMED lists exactly
(L), (BS), (BD). Pre-run edit (before run 1): `mzero` and the det checks use `sp.cancel(sp.together(.))` instead of
`sp.simplify` (performance only; same predicate). Timing went to `b1_consumed.run1.time` (not stdout).

## N2 — B1 node 2: does CONS hold in M_max?  [verdict: NO — exact, already landed as X6]

BD fails in M_max: phiW ∉ dualW maxCone, witness dg(1,−1,1,−1) ∈ maxCone with ipW = −2 (landed probe X6). So CONS
fails in M_max, and so does open question 1's clause (products into K plus Bell table in K*). Re-verify in b1_models.

## N3 — B1 node 3: the decisive structure — orientation obstruction (Lemma O)  [verdict: NEW, gem type (2)]

σ_q: (N, A, B, A', B') ↦ (actT reflY ∘ N, A, reflY ∘ B, A', B') at one pair q. It preserves N-CLASS and flips
orient(A_q, B_q). If K_q is actT reflY-invariant (maxCone, SEP), σ_q preserves hcls, hadm, hcl, H (cones unchanged) and
IE1, and flips EvenCycle. Hence: any clause Γ invariant under σ (as hgate, CONS, OQ1, SECT, PREC, P-PROD, BD, PRP, TBP
are) with Γ ∧ hcls ∧ hadm ∧ hcl ∧ H ⇒ C must fail on every family having one actT reflY-invariant cone — in particular
in M_max and in uniform SEP. On uniform maxCone (or SEP) data the four hypotheses hold for all 16 orientation patterns,
and C ⟺ EvenCycle; a sufficient clause restricted to such data implies EvenCycle there.
Consequence: the decisive control "holds in M_max" cannot be met by any σ-invariant sufficient weakening of hgate.

Models introduced (to be certified in b1_models): M_maxD (uniform maxCone, N_13 = actT reflY∘cnot), M_maxT (uniform
maxCone, N_13 = cnotTw), M_SEP (uniform SEP, cnot), M_SEPD (uniform SEP, N_13 = actT reflY∘cnot).

## N4 — B1 node 4: a model of CONS ∧ ¬hgate  [verdict: NEW, gem type (1) + (3)]

M_pre: uniform Q3, N_13 = cnot ∘ actT reflY (pre-local B'_13 = reflY), all post-locals I. CONS holds (tables identical
to M_Q's); hgate fails (phiW ∈ Q3, N(phiW) = cnot idW = chainW ∉ maxCone); in fact no admissible cone is invariant under
this gate (N(prodState xplus z3) = phiW, N(phiW) = chainW). C holds. Exposed hidden assumption: hgate constrains the
pre-locals (on families with K_p = twistQ3(orient(A_p,B_p)), hgate ⟺ orient(A'_p,B'_p) = orient(A_p,B_p)), while C
reads only the post-locals.
M_DD: cones (Q3, twin, Q3, twin), N_23 = N_13 = actT reflY ∘ cnot (B = reflY): EvenCycle (two twisted), FCC by the
token-3 chart transport, CONS and SECT hold, hgate fails at 23 and 13 for every admissible cone (C3 chain).

PREC (gate preservation up to a local orthogonal pre-correction: ∃ C, D orthogonal, N ∘ actC C ∘ actT D maps K into K)
is sufficient by kt4_forward_ie1 itself applied to the corrected gates (same post-locals) [D]; holds in M_pre (D = reflY)
and M_DD (D = reflY, the corrected gate is cnotTw on twin). Chain under hcls ∧ hadm ∧ hcl:
hgate ⇒ PREC ⇒ SECT ⇒ OQ1 ⇒ CONS. (An earlier candidate "POST: the post-part actC A actT B cnot preserves K" was
discarded before any script: it is not implied by hgate — cnotTw preserves twin but actT reflY ∘ cnot does not.)

## N-E1 — side exploration (DEPGRAPH §7.6 open question (A2): is a gate premise needed for IE1?)  [F, lead only]

Family: K01 = K23 = K_h := maxCone ∩ {w : ipW h w ≥ 0}, K02 = K13 = maxCone, cnot gates, identity locals,
h = diag(1, t, t, 0). Written: famI holds automatically (K02* = K13* = SEP factorizes); famII ⟺ h·maxCone·h ⊆ SEP;
hadm, hcl hold; K_h is not IE1 for t > 1/2 (dg(1,−1,1,−1) ∈ K_h, its (y↔z) rotation dg(1,−1,−1,1) has ipW h = 1 − 2t).
`explore/e1_ie1_foil.py` run 1 (float, fixed seed): sampled h(Q3 ∪ twin)h stays PSD and PPT for t ≤ 0.7071 (minimum
eigenvalue +0.0043 at t = 0.7071, +0.042 at t = 0.6) and fails for t ≥ 0.72. Not certified: it needs Størmer–
Woronowicz decomposability (maxCone = Q3 + twin for qubits) and the Peres–Horodecki criterion [L, unverified], or a
self-contained positivity proof of Φ_(t,t,0)^{⊗2}. Recorded as a lead for the coordinator; no claim.

## N5 — the model matrix: `b1_models.py` run 1 (05:18)  [verdict: CONFIRMING N2–N4 + NEW refutations]

Eleven models × fourteen clauses (H0, C, hgate, PREC, SECT, SECTst, SECTef, OQ1, CONS, BS, BD, PRP, TBP, SECT′).
Pre-run edits, all before run 1 (found on re-reading the script): the chain claim `gDi(idW) == chainW` corrected to
`gDi(phiW) == chainW`; M_int's H0 set to False (hcl fails there); BS cells added; `family_value` made strict (unknown
ids raise instead of passing); checks Dloc, Dorth, W14 added; an f-string with a line break (a syntax error under
Python 3.11) replaced by a precomputed string. Run 1: 53/53 PASS.
Results: hgate, PREC, SECT, OQ1, CONS have no countermodel in the matrix and fail in every H0 ∧ ¬C model, at M_max and
at M_D. PREC/SECT/OQ1/CONS hold in M_pre and M_DD where hgate fails. Separations that hold in M_max and fail in M_D —
SECTst, BS, PRP — are refuted as replacements by M_maxD and M_maxT (H0 ∧ clause ∧ ¬C). BD, SECTef, TBP are refuted by
M_SEPD; SECT′ by M_D. Lemma O identities O1–O4, the 16 patterns O5 (8 even / 8 odd), O6 (no reach to Q3).

## N6 — amendments 1 (05:13) and 2 (05:22)

Amendment 1: a separation (holds in M_max, fails in M_D) is not sufficiency; sufficiency must be shown step by step for
every consuming use (link_mem, bell_mem, Lemma R, bell_mem_dual, parity_witnesses). Amendment 2: one label per target;
INDEPENDENT needs a countermodel satisfying every certified premise bearing on the target, each listed and checked; a
failed derivation is UNRESOLVED; keep [K]/[D]/UNBUILT, [W], [X] apart. Consequences for this thread: N7 (UNBUILT Lean
and exact diff checks), N8 (the certified-premise checklist), N10 (census), N11 (implicit consumption).

## N7 — sufficiency, step by step: `B1_UNBUILT.lean` and `b1_steps.py`  [verdict: ELABORATING; favourable — pressure-tested]

`B1_UNBUILT.lean` (UNBUILT; no Lean toolchain): CONS; link_target_of_ctrl; ie1_all_cons; parity_witnesses_cons;
parity_all_cons; kt4_general_ie1_cons (no Lemma R); kt4_forward_ie1_cons; OQ1, cons_of_oq1; SECT,
gate_sharp_mem_dualW_of_inv_pos, oq1_of_sect; cons_of_hgate; locEquiv, nclass_comp_loc, PREC, kt4_forward_ie1_prec
(one application of the design kt4_forward_ie1 to the corrected gates); isOrth3_id, prec_of_hgate. Pre-run edit to the
Lean text: `simp only [PREC] at hprec` before `choose`.
`b1_steps.py` pre-run edits: the name-boundary regex `\b` fails for names ending in a prime, replaced by
`(?![A-Za-z0-9_'])`; D.cc wording. Run 1 (05:28) FAILED at D.cc: the countercontrol was wrong, not the identity — it
asserted that for a non-orthogonal pre-local the transpose formula fails the adjointness ipW (N E) X = ipW E (adj X),
but the transpose formula is the ipW-adjoint of every such N, orthogonal or not; orthogonality is what makes the
adjoint the inverse. Fix: D.cc now checks adj ∘ N ≠ id for a non-orthogonal pre-local, and D5 states the two facts it
checks (adjointness; adjoint = inverse). Run 2: 23/23 PASS. Run 1 kept as `b1_steps.run1.*`.
Written (not in the Lean file): PREC ⇒ SECT under hcls ∧ hadm ∧ hcl — the corrected gate N′ = N ∘ actC C ∘ actT D is
N-CLASS (D2) and preserves K; products: N(prodState x y) = N′(prodState (Cᵀx) (Dᵀy)) ∈ K; inverse: Lemma R for N′ gives
N′⁻¹ K ⊆ K ⊆ maxCone, and N⁻¹ = actC C actT D ∘ N′⁻¹ with maxCone invariant under local orthogonal maps (Dmax, Dorth).
GT-COMP ⟺ SECT, both directions field by field: (⇒) prod_mem of the transported data is SECT's first half (N fixes the
unit entry, D4) and prodEff_effect of the transported effects is SECT's second half; (⇐) the two halves give those two
fields, and convexity, the unit pairing and the evaluation law hold for every N-CLASS gate (D4, D6).

## N8 — B2 sources: `b2_sources.py` run 1 (05:32)  [verdict: NEW (first item) + CONFIRMING]

NEW: the native-gate premises (IsNot, NativeGate's frame / two-sided positivity into maxCone / relT / relC, CtrlGate,
GateRel, Entangling, one common NOT) hold for cnot, g_D, g_pre, g_Tw, and g_D, g_pre preserve no admissible cone (two
steps from (xplus, z3) reach chainW). The 13-item checklist of certified premises bearing on (K, N) holds for M_max
(landed objects only) and M_D13, both violating hgate. JR ⇒ hgate by scaling (S4.jr); P-ACT2 impossible on a
product-only pair system (S4.pact); the transported evaluation law (S4.gt). B3: product-level idle extension is an
identity (S5.prod); the gate-factor version leaves Q3 and meets K2-GUARD-1 (S5.gate); the commutant version needs
rotation invariance of K (S5.comm). 27/27 PASS.

## N9 — replays (05:35)

b1_consumed (= run 1), b1_models (= run 1), b1_steps (= run 2), b2_sources (= run 1), explore/e1 (= run 1): byte-identical
(`cmp`), every `.err` is `exit=0`.

## N10 — census of the landed declarations: `b2_census.py`  [verdict: POSITIVE — the checklist is not a hand selection]

Motive (§A.19): the landed tree has 214 modules; the checklist was built from the modules the landed record cites.
Headers read for the dispositions: MicroscopicReversibility, NativeGateBall, OrientationSelection, OrientationClosure,
DerivedQ3, MonoidalCompletion, ProductAdmission, Separability, PartialTranspose, TransposeBridge, SwapLayer,
CompositeSoundness, CompositionOrder, DenseOrbit, OddChar, RelcSelectC5, RelcSelectParity, RelcSelectSqueeze,
SharpTests; definitions read: IsNot, NativeGate, Entangling (CD 205–232), NativeGateOf, EntanglingOf, CandidateCone,
CtrlGate, GateRel, PreComposite, LocallyTomographic, Composite, maxBody, minBody, JointReversible, OpDatum,
preservesBody_inducedEquiv, CopyNatural, KInf1, IsBodyGroup, TransBody, DenseBoundaryOrbit, BoundedAffine; ROADMAP P1
row (line 68) and the K2 / K∞ text (lines 995–1016, 1080–1090). The matrix-carrier modules (reversible richness,
dagger-stable implementations, H-tensor, orientation selectors) state no predicate over the pair carrier.
The COVER and MODS maps were built from exploratory listings with the R1/R2 rules and a grep for PAIR, before run 1.
Pre-run edit: `OIBridge(root)` added to MODS (it matches PAIR only through `import OIBridge.NativeGateBall`).
Run 1: invocation error — `/usr/bin/time` absent, the script did not execute (files kept as `b2_census.run1.*`).
Run 2 (bash `time`): 7/7 PASS — 215 files; 53 declarations selected and classified; the 8 Props over the pair carrier
are covered by checklist items; 16 pair-touching modules classified; three planted countercontrols detected.
Replay identical to run 2.

## N11 — implicit consumption: `b1_implicit.py`  [verdict: POSITIVE — pressure test of the favourable branch]

Question: could a tactic consume hgate/hinv without naming it (assumption, simp [*], aesop, ...), invisible to the S1
name count, so that the copied lines of the `_cons` declarations need a hypothesis they no longer have? Run 1: 7/7
PASS. Context-reading tactics in scope of hgate/hinv on the design path: linarith ×3 (parity_witnesses), linarith ×2,
omega, positivity (inv_mem_of_orth); in the UNBUILT file: linarith ×3 (parity_witnesses_cons). All read only
comparison hypotheses (Mathlib `Tactic/Linarith/Preprocessing.lean:60` filterComparisons; `Tactic/Positivity/Core.lean`
compareHyp), and the four hgate/hinv binder types are memberships, not comparisons. Replay identical.

## N12 — K2 and K∞-Act as recorded  [verdict: CONFIRMING]

ROADMAP K2 (OPEN): local tomography, the composite cone, local actions compatible with it, the composition theorem, the
antiunitary / CP bridge, the relation to K3. It does not name the native gate's action on the composite. Its local-
actions clause is idle extension at the operation level (forbidden here); a composite cone fixed to Q3 is the forbidden
Q3 premise; adding the gate's action restates hgate. K∞-Act (OPEN) for the pair system is P-ACT2: a restatement.

## N13 — physical reversibility  [verdict: CONFIRMING]

Three readings: (a) the gate and its inverse as operations on the pair state space = hgate ∧ hinv (restatement);
(b) two-sided positivity on products relative to maxCone = NativeGate.posFwd/posInv (holds for g_D, g_pre: route
refuted); (c) substratum-level reversibility (MicroscopicReversibility and the matrix-carrier modules): no certified map
to (K, N) at L (census R5), so it is not a route at L.

## N14 — fixed point

N8 was the last NEW finding; N9–N13 (replays, census, implicit consumption, K2/K∞-Act, reversibility) produced no NEW
finding — three or more consecutive passes — and the thread's questions are answered (RESULT §0). Stop.
