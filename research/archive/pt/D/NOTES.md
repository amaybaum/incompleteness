# Thread D — NCLASS-ADM — working notes (node log)

Base: L = 9f9f8257a980a1819fbbc1dc0019917cf8678626 at `pt/base/` (read-only). Protocol sha256 239dc123…fa9b23.
Start checks: `.start_marker` (manifest OK, HEAD = L, status empty).

Evidence tags as in the protocol: [K] landed at L; [D] design run ff9c3a35; [A] recorded premise; [N] new;
[X] exact computation here, replayed; [W] written; [E] exact exploration (lead); [F] floating exploration (nothing
certified).

## Reading log (what I read, in order)

1. `round-kt4-prem-1-premise-audit/result.md` in full: Q1-MAP (M_refl: uniform Q3, A_13 = reflY, N_13 = cnot; M_id;
   M_class; M_mix), Q3 source-map rows for `hcls` and `hadm`.
2. Design modules: `NClass` (FourCopyCore:132–134: four `IsOrth3` clauses and the pointwise identity
   `N ω = actC A (actT B (cnot (actC A' (actT B' ω))))`), `PairAdm` (FourCopyDefs:43:
   `CandidateCone K ∧ IsConvexCone K`), headline (FourCopyHeadline:120–130): conclusion
   `EvenCycle (fun p => orient (A p) (B p))` reads the SUPPLIED post-locals only.
3. Landed DIM-1 (CompositeDimension.lean): `IsNot` :210, `NativeGate` :218 (frame, posFwd, posInv, relT, relC),
   `Entangling` :229, `cnot` :775, `nflip` :797, `z3` :793, `nativeGate_cnot` :1160, `entangling_cnot` :1380,
   `corner_form` :1805, `gate_corner` :1885, `Mfwd/Minv` :1878/:1882, `lor_cornerMap` :1870, `gate_corner_neg` :1965.
   RELC-SELECT-1 (RelcSelectBlock.lean): `CtrlGate` :45 (NativeGate minus relT), `ctrlGate_of_nativeGate` :53,
   `dim_of_ctrlGate` :739, `three_of_ctrlGate` :753.
4. K2Guard.lean: `CandidateCone` :95–96, `prodState_mem_maxCone` :165, `reflY` :46, `no_candidateCone_cnot_reflY`
   :143. CompositeInterface.lean: `PreComposite` :223, `subset_maxBody` :467, `minPre/maxPre` :528/:557, `coeff` :602,
   `pEff` :646, `paddedPre` :848, `not_locallyTomographic_paddedPre` :885.
5. ROADMAP K1 (:984–1000, CONDITIONAL; K1 inputs unsourced, :995–996) and K2 (:1001–1006, OPEN).
6. Ledgers: ASSUMPTIONS.md (hcls [U] route = EQ2-B "IsNot ∧ CtrlGate (∧ NormPres) ⇒ N-CLASS", unbuilt; hadm [T]);
   EQ2-SYNTHESIS (EQ2-B: "every CtrlGate at d = 3 is ℓ₁∘cnot∘ℓ₂", 4-parameter tangent family, ±1 forcing,
   8/8 split; EQ2-B's own RESULT is NOT among my inputs); EQ5-SOURCE row 1 ("NormPres, derivable [W]") and row 2
   (hadm [T] via COMP-1 bounds; T1 coordinate map); DEPGRAPH §7 (per-clause deletion foils, [W]);
   K2-LEDGER §3.1–3.3 (q-map; DIM-1 consumes PTQ, not LT).

## Node plan (depth-first; decisive first)

- D1.0  decisive first check: does `M_refl`'s gate meet every landed native-gate hypothesis while failing N-CLASS?
- D1.1  gate form: IsNot ∧ CtrlGate at d = 3 ⇒ ∃ orthogonal locals with the NClass identity? (re-derive
        independently; EQ2-B's text is not available to me, so nothing of it is reused).
- D1.2  the labelling part of `hcls` (supplied locals) and whether the orientation bit is a gate invariant.
- D1.3  minimality of the sufficient set: which clauses can be dropped (countermodels), relC / IsNot in particular.
- D2.x  admissibility clause by clause; the q-map; whether local tomography (K2) is needed for hadm.
- D3    dependencies on hgate, hcl, IE1, the target.

## Node log

### D1.0 — decisive first check (M_refl's gate)
- M_refl's data at pair 13: N_13 = cnot, A_13 = reflY, other locals I. The GATE is cnot itself, which meets every
  landed native-gate hypothesis at d = 3 ([K] isNot_nflip CD:838, nativeGate_cnot CD:1160, ctrlGate_of_nativeGate
  RSB:53, entangling_cnot CD:1380) and IS N-CLASS (identity locals). M_refl fails hcls only because the SUPPLIED post-local
  A_13 = reflY is not a local of any decomposition used (NClass cnot reflY I I I fails at prodState xplus z3).
- Verdict D1.0: M_refl's gate is not a non-N-CLASS native gate. But M_refl IS a model of "every landed native-gate
  hypothesis holds for every N_p, and hcls fails": so "native-gate hypotheses ⇒ hcls" is refuted AS STATED (with the
  supplied locals). Exposed hidden assumption: hcls bundles (i) the gate form ∃ orthogonal locals and (ii) the
  labelling: the supplied locals are a decomposition. The conclusion EvenCycle reads only the supplied post-locals.
  → to be certified in d1b (C1).

### D1.1 — gate form (exploration e1, e2 [E], leads)
- e1: the four-parameter family G(s1,s2,t1,t2) (controlled-(id, nflip) on the control diagonal; coherence
  e1⊗Y ↦ e1⊗s1 S Y + e2⊗t2 T Y, e2⊗Y ↦ e1⊗t1 T Y + e2⊗s2 S Y) is cnot at (1,1,-1,1), satisfies frame, relC, relT
  symbolically; the pairing formula F = 2p_u p_x<b,Y> + 2q_u q_x<b,NY> + u'ᵀΛx' holds; inverse = (1/s1,1/s2,-1/t2,-1/t1).
- e2: zero-set form spaces. Proper M1 (π-rotation): 2-dim, span{S,T} (rotated for a general axis). Improper M1:
  diag(1,1,-1): 3-dim, every form kills Y3; diag(Rot,-1) generic: 0-dim; -I: 3-dim cross-product forms, every form
  kills Y0. → in every improper case the coherence map annihilates e_j⊗e3 or e_j⊗e0: the gate is not injective.
- Consequence to test (favourable to the framework → maximum skepticism): relC, relT, IsNot's involution/flip and
  Entangling may all be unnecessary for N-CLASS form at d = 3; candidate sufficient list: unit corner axis z, frame,
  posFwd, posInv (G a linear equivalence). Landed `gt_tangent_corners_ctrl` (RSB:126) is the tangent step under
  CtrlGate; without relC my own written tangent argument is needed (uses frame + posFwd only).
- Prior research: EQ2-B (not readable here) proved IsNot ∧ CtrlGate (∧ NormPres, "derivable [W]") ⇒ N-CLASS. My route is
  independent code and reaches the CtrlGate case as a corollary; the frame + P± version is not recorded in the ledgers
  I have.

### Amendments (read mid-run; binding)
- AMENDMENT-1 sha256 b41aa0e7…cf83, AMENDMENT-2 sha256 2a2f78f3…530a (both verified). Consequences for D:
  one label per target (N-CLASS; each hadm clause): DERIVED / CONDITIONAL / INDEPENDENT / UNRESOLVED; a restatement
  never makes a target CONDITIONAL; INDEPENDENT needs an exact countermodel of every certified premise bearing on the
  target (listed and checked), scope "the premises certified at L as stated"; a model of one route's premises only is
  "route refuted"; "sufficiency proved" kept separate from "survives the countermodels"; [K]/[D] vs [W] vs [X] kept
  separate; exact computations stated for the instance unless symbolic/exhaustive or lifted by [W].

### D1 certified so far
- d1a_zeroset.py: 20/20 first run, VERDICT ZEROSET-LEMMA-EXACT.
- d1b_classify.py: 57/57 first run (about 10 min, timing only in the shell), VERDICT D1-EXACT-STEPS-HOLD.
  Notable: the 8 sign patterns with product +1 fail posFwd at value -14/27 (exact points listed in the output);
  det cnot(prodState x y) = -(x0²+x1²)(1-x2²)(1-y0²)(y1²+y2²) ≤ 0 on ball × ball, so the orientation bit of any
  decomposition is the sign read off det of product images: a gate invariant. M_refl's supplied (reflY, I) is the
  post-local pair of NO decomposition of cnot (det would be +1 > 0).
- Strengthened statement (to be written as T1): for G : W 3 ≃ₗ W 3 and unit z, frame(z) ∧ posFwd ∧ posInv ⇒ N-CLASS.
  Characterization: N-CLASS(G) ⟺ posFwd ∧ posInv ∧ (frame(z3) after local orthogonal changes of frame on each side).
  posFwd, posInv are necessary for N-CLASS (C ⇒ A); unit z, frame cannot be dropped from the sufficient list
  (C10 countermodels), and are not implied by N-CLASS for G itself.

### D2 plan under the amendments
- hadm ⟺ ∃ COMP-1 PreComposite P of two balls (any carrier, no lt) with K = cone(q(P.Ω)), q the product-test chart;
  each direction separately. Per clause: (a) ↔ prod_mem, (b) ↔ prodEff_effect lower bound, (c) ↔ convex + cone
  definition. These are restatements through the chart → no clause is CONDITIONAL on them.
- Labels: each clause INDEPENDENT of the premises certified at L as stated: (a) M_class (landed), (b) uniform W 3 with
  cnot gates (H on an explicit carrier), (c) the scaled cnotOrbit (landed candidateCone_cnotOrbit). Lt not needed:
  paddedBall3 (landed, not locally tomographic) has an admissible product-test cone (the minimal one).

### D1 pressure test (§A.31, favourable branch) — re-walk of the written steps against the landed statements
- Step 2: corner_form (CD:1805) needs only unit z, the FIXING frame at the slice corner, and product positivity of a
  linear map; at -z3 the frame SWAPS target corners, so it is applied to actT nflip ∘ G (d1c B4: fixing at -z3) — OK.
- Step 3 needs M and M^-1 to map L into L: lor_cornerMap (CD:1870) for G with posFwd and for G.symm with posInv — OK;
  M e0 = e0 from the frame (fixes / swaps hom(±z3)) — OK; null-to-null by self-duality of L (lor_of_forall_pair
  CD:1015 one direction; the other is Cauchy–Schwarz) — OK.
- Steps 5–6 are written limit arguments (first-order terms at a zero of a nonnegative function); under CtrlGate step 5
  is landed (gt_tangent_corners_ctrl RSB:129). Step 7 is exact (d1a), universal over the sphere through W0.
- Step 8: improper R1' => every zero-set form kills Y3 (cc != -1) or Y0 (R1' = -I) => G not injective; exhaustive
  over improper R1' with R1' z3 = -z3 (they are exactly diag(Rot, -1)) — OK.
- Steps 11–13 exact (d1b C2–C6) plus written singular-value / AM-GM arguments; end-to-end instance (d1c B6) recovers
  an orthogonal a' and b' = ±a'J' from a scrambled N-CLASS gate; countercontrol CC-B returns a non-orthogonal a'.
- Consistency with prior research: EQ2-B's 16 patterns, 8 surviving (4 Q3 / 4 twin) match C7 (8 survivors; det D = ±1
  splits them 4/4). EQ5-SOURCE's "NormPres derivable" matches: every survivor preserves the (0,0) entry.
- Verdict D1.1: POSITIVE/NEW — sufficiency of {unit z, frame, posFwd, posInv} proved [W + K + X], UNBUILT Lean. Not
  needed: relT, relC, the NOT N (IsNot beyond unit), K∞-Copy, Entangling. Each of the four kept clauses has an exact
  deletion countermodel (C10). posFwd ∧ posInv are necessary for N-CLASS (N-CLASS ⇒ P±, [K] cnot_prodState_mem_maxCone
  + local invariance). Characterization: N-CLASS(G) ⟺ P±(G) ∧ ∃ local orthogonal L, L' with frame(z3)(L∘G∘L')
  [(⇐) T1 applied to L∘G∘L', P± being local-invariant; (⇒) L, L' the inverse locals, cnot_frame CD:848].

### D1.2 — orientation (C9) — NEW
- det cnot(prodState x y) ≤ 0 on ball × ball; det phiW = -1; det(actC a actT b w) = det a det b det w. Written lift:
  if NClass G A B A' B' and NClass G Ã B̃ Ã' B̃', evaluate at prodState(A'ᵀ xplus, B'ᵀ z3): -det A det B =
  det Ã det B̃ · det cnot(prodState x' y') with the last factor ≤ 0, so det A det B = det Ã det B̃. The parity in the
  conclusion is a property of the gates. M_refl's (reflY, I) is the post-local pair of NO decomposition of cnot.

### D2 — admissibility (d2_adm 37/37 first run)
- D2.0 USES (design): (a) bell_mem, link_mem, parity_witnesses, bidual nonemptiness; (b) Lemma B1 slice bound,
  bell_mem_dual via sharp_mem_dualW, parity_witnesses; (c) bipolar dualW_dualW, scaling in B1.
- D2.1 landed facts: prodState_mem_maxCone gives products ∈ maxCone (consistency of (a) with (b)), nothing about
  K_p; CandidateCone is the definition of (a) ∧ (b); COMP-1 PreComposite fields + subset_maxBody give (a), (b), (c)
  for the product-test image of ANY pre-composite of two balls (no lt) — and conversely (model carrier). So the
  COMP-1 route is a restatement of hadm through the chart (both directions), and lt is not consumed (paddedBall3).
- D2.3 per-clause countermodels (all with cnot gates, so the K1 gate premises hold):
  (a) M_class — also hcls, hcl, hgate, H [S3 + landed M_class.2]; IE1 fails.
  (b) uniform W 3 — also hcls, (a), (c), hcl, hgate, H [S4 carrier]; C holds; odd pattern: EvenCycle fails.
  (c) scaled cnotOrbit — also hcls, (a), (b), hcl, hgate; additivity fails; H NOT claimed.
- Labels (amendment 2): each clause INDEPENDENT of the premises certified at L as stated; the supplying principles
  ([N-PROD], [N-PEFF], [N-CONV] / COMP-1 fields through the chart) are restatements (recorded, not used as sources).
- Remark: DIM-1's `jointStates` is a DEFINITION (normalized maxCone). Taking K_p := maxCone makes hadm hold [K + W]
  but hgate fails for cnot (landed M_max) — not a certified identification of K_p.

### D3 — dependencies (d3_deps: run 1 FAILED on a misclassification of two design consumers; kept as run1; run 2 29/29)
- No route declaration states closedness, IE1, the parity, cone preservation, four-copy data, Q3/complex structure, or
  the target. Target-stating citations confined to the converse/minimality steps.

### Fixed point
- Passes with a NEW finding: D1.0 (labelling), D1.1 (reduced premises), D1.2 (orientation invariant), D1.3
  (deletion countermodels + characterization), D2 (lt not consumed; (c) certified-premise countermodel).
- Further passes without NEW findings: relative version (K1-BRIDGE: positivity on maxConeOf avail transports to
  maxCone under EFF-1's premises, the same one-line transport as nativeGate_of_cone_eq) — ELABORATING; the hcls/hadm
  interplay (no gate premise constrains K_p; all three countermodels have cnot gates) — CONFIRMING; the odd-pattern W 3
  variant (re-verifies DEPGRAPH's written foil for (b)) — CONFIRMING. Three consecutive passes without NEW: stop.

### End (2026-10-10T05:50:19Z)
- The d1b replay is byte-identical (.out and .err), as are all other replays.
- End integrity checks:
  - manifest exit 0;
  - base HEAD = 9f9f8257…;
  - base status empty;
  - PROTOCOL and amendments unchanged;
  - pt/D holds 51 entries, all written by this thread.
- Deviation: a temporary listing `D_listing.txt` was written to the scratchpad root, outside pt/, and then deleted.
  It is recorded in RESULT.md §7.
