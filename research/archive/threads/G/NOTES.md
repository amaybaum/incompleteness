# Thread G running notes (effect-family reconstruction, P2/O1)

Certified main 6d0abf6b; worktree threads/G/wt (detached, read-only). KF = KInfFoundations.lean.

## 0. Setup / sources read
- CHARTER.md; F/LEDGER.md, F/NOTES.md, F/f_countermodels.py(.out).
- KF full outline; §A FiniteStage (KF:63-109), §B effects (KF:116-150), §E exposure (KF:811-872), §E' response (KF:884-986), §G KInf1 (KF:1013).

## 1. First structural observation (to verify in scripts)
- FiniteStage.states lives in ℝ^E: the stage's own effects are the COORDINATE functionals. Affine span of
  {coordinates, const} = all affine functionals on ℝ^E. So "affine closure of the stage's effects ∩ [0,1] on Ω"
  = fullEffects(Ω) in the operational embedding. The operational question is which closure is licensed:
  convex/coarse-graining/complement (GPT-standard) vs affine-with-[0,1]-test on Ω (= no-restriction hypothesis).
- SIC ball: response coefficients c_i = (1+3 n·n_i)/2 ∈ [-1,2] for the projective effect (1+n·r)/2 -> outside
  [0,1]^4: CM-SIC is the Ferrie–Emerson / Spekkens negativity phenomenon (citation), and the no-restriction closure
  of the SIC response effects recovers fullEffects.

## 2. Inventory progress (verified at 6d0abf6b)
- Field-neutral sources: ONLY KF FiniteStage (KF:63, p e x table; coordinates of ℝ^E) and KF §E′ response maps
  (KF:889-986; response_eq_one_forces KF:899; classical_exposed_ncard_le KF:947). No composite, ancilla,
  readout, conditioning, copy in KF (CopyNatural KF:284 is a Prop on two NOTs only).
- NativeGateBall: field-neutral reals but CONSUMES full self-dual effects (lorentz_of_effects NGB:105 quantifies
  over every unit direction) — a consumer of P2, not a source. Assumption-watch: K1 needs sharp effects
  (1+b·r)/2 for all unit b, which is stronger than SEC (SEC gives 1-s(1-b·r), s∈(0,1/2]).
- Matrix regime (imported ℂ): FiniteOperationalTheory (OA:594; closure rules avail_id/coarse/bind/prep_uniform/
  post/readout/discard), readout_is_localLuders OA:658, circuit_available OA:757, InstAvail IL:268 (op/readout/
  coarse/bind/discard, no sum), realized_of_instAvail IL:530, genTheory IL:852, genFamily_relabelling IL:893,
  QuantumArchitecture SS:83, genTheory_qm_of_quantumArchitecture SS:136, substratumClass StructuralClosure:180
  (monomials), substratum_residual SC:383, preservesDiag_conj_of_monomial SubstratumInterface:126,
  diagTheory DiagonalTheory:245 (NB: diagTheory's effects are NOT only diagonal: |0><+| preserves diag).
- Dense: DiscreteCompletion: fixedGateTheory (DC:1923ff), fixedGateTheory_not_qm DC:1948 via mixTheoryR_not_qm
  StateMixingCoupling:679 (countable class up to scalar, SMC:661), ClosureAvail DC:63 = D3 DEFINED, two debts
  unproved (discrete-completion-audit.md T8); DenseInstrumentBridge fixedGateTheory_krausDense DIB:514.
- Completion: RegionLimit inclObs RL:102 (X ↦ X⊗1, no refinement); InstrumentAvailability q3_countermodel IA:335
  (infinite-support ops not available). ObservabilityQuotient: itinerary indicators = classical response fns.

## 3. Key structural findings (to be checked in g_controls.py)
- H1 (closure-stability): Resp(p) of a fixed finite ontic realization is closed under every ONTICALLY implemented
  operation (convex mixing, complement, coarse-graining, sequential bind with ontic updates, attach/stochastic/
  readout/discard, limits): new vector = M^T c ∈ [0,1]^N. So "closure of operationally generated effects" of one
  realization = Resp(p); F2 + CM-SIC kill it on the ball.
- H2 (domination certificate): if inf_{g∈G} min_i p_i(g x) = δ > 0 then 1-h(z) ≤ (1/δ)(1-h(x)) for all h in
  Resp(p)∘G and all z; inequality is linear, survives convex hulls and pointwise limits => no proper certain
  effect at x in any closure. Criterion: Cl_G Resp(p) is SEC-complete ⇔ G·T(p) ⊇ ∂_rel Ω, T = tangency set.
- H3 (representation dependence): tight vs loose SIC (same ball), bidisk R1 (torus contacts) vs R2 (flat-face facet):
  same body, same drive group, opposite SEC verdicts.
- H4: drive not ontically implementable at fixed SIC: p∘R_t∘p^{-1} not stochastic for generic t.
- H5: matrix substratum: monomial unitaries fix the Bloch z-axis up to sign => J_off_axis fails (agrees with
  substratum_residual); effects diagonal => response on 2 configurations.
- H6: Naimark circuit (attach |0>, CNOT·(V†⊗1), read ancilla) gives V|0><0|V† — sharp effects come from the
  postulated native register readout transported by control; with monomial V stays diagonal.

## 4. Script status
- g_controls.py -> "OK -- 50 checks, 17 written notes" (output g_controls.out). Sections ONT, DOM, SIC, ONTD, BID, STG,
  MAT (incl. diagTheory measure-and-prepare), NR. Vacuous checks replaced by computed ones (loose delta from mins,
  R1 orbit minima identity, (2a+b)/2 violating DOM, antipode effect 2p_1).
- Extra findings: substratumTheory = genTheory substratumClass (RouteB:279) realizes sealed OI core (RouteB:375) with
  diagonal effects; diagTheory realizes it (DiagonalTheory:358) with full effects and no control (:390) -> OI core
  does not determine P2; full effects need no drive.
- Fixed-gate (DC:1926): countable available families (SMC:662 + InstAvail constructors) -> countably many supported
  pure states -> SEC fails on the Bloch ball without D3 (ClosureAvail DC:63, defined, not adopted). Written.

## 5. Verdicts (draft)
C1 Resp(p) INSUFFICIENT; C2 stage GPT closure INSUFFICIENT; C3 G-closure of Resp(p) INSUFFICIENT (rep-dependent) +
BLOCKED on K∞-R; C4 refinement limit BLOCKED (no refining family); C5 union over realizations BLOCKED (no source);
C6 no-restriction BLOCKED (= target); C7a substratum INSUFFICIENT; C7b quantum architecture DERIVED (R-mat only);
C7c fixed gate INSUFFICIENT w/o D3, DERIVABLE with D3; C8 native readout transported BLOCKED (no field-neutral
composite/readout; covering).
