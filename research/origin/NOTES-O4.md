# NOTES-O4 — the dependency between Origin and the composite-action bridge

Thread `research/origin`, node O4. Base L = `9f9f8257`. Evidence levels as in NOTES-O1. Script:
`experiments/o4_dependency.py` (5 checks, 3 countercontrols; decision rule in the header before run 1; green on
run 1, byte-identical on replay). The bridge thread's branch was not read; its side is taken from the archive
records it inherits (`pt/INTEGRATION-NOTE-STAGE5.md`, `-STAGE6.md`, audited [A]). The handoff proposal is
`handoff-proposals/O4-origin-bridge-dependency.md`.

## 0. Verdict

**The two threads meet at one object: a single discrete balanced mixer on one token.**
- The bridge's isolated missing assumption (stage 6 §5) is (b) for `ball3Drive`'s flow — the substratum phase flow
  φ_t = R_z(t) about the frame axis — and its J-conjugate, the drive R_x(t). Because J = `cyc3` = R_z(π/2)R_x(π/2)
  and J R_z(t) J⁻¹ = R_x(t) [X D1, D2], that assumption is **equivalent to (b) for {φ, J}**: the phase flow and
  one discrete operation [W].
- J is itself a **discrete balanced mixer** for the frame z: it maps the pure frame state e_z to the pure balanced
  state e_x and carries the owner's witness (1, 1/2) with J⁻¹ [X D3]; a unitary lift U_J (order 3, non-monomial)
  does the same on the qubit [X D4]. J is the Discrete target in the bridge's own vocabulary.
- **What the bridge needs from Origin:** SRC(J) — that J (or any balanced mixer) is *available* on one token from a
  premise that passes the disguise test (stage 5's L1). Without it, (b) concerns an operation nothing makes
  available. O1–O2: the stated substratum does not supply it.
- **What Origin needs from the bridge:** SPEC(B) — the spectator stability of the sourced mixer: at the matrix
  level its availability at every level (equivalently context stability of a generating class containing it),
  which is exactly what remains for `oiPlusMin_iff_qm` (NOTES-O3 §4); at the pair level, (b) for it.
- **Neither supplies the other.** Spectator principles do not source operations (stage 5: every candidate
  yielding (b) contains a spectator clause; K(Z_F) carries a pair drive and fails (b)), and sourcing an operation
  at level one says nothing about the composite (stage 6: (b) is independent of everything at L).
- **What Origin adds for the bridge.** (i) At the matrix level the phase flow's spectator stability is a theorem
  (`substratumClass_contextStable` [K StructuralClosure.lean:261]), so the spectator content needed there reduces to
  that of the one mixer [W + X D5]. (ii) At the pair level the phase-flow half is not free (stage 6: no one-parameter
  rotation subgroup of either token is supplied at L, and no theorem connects the matrix carrier to `W 3`).
  (iii) Lemma P (NOTES-O3 §3): a composite model in which single-token observation is passive and repeatable
  cannot carry a balanced mixer or a drive through the native NOT on a token.

## 1. The propositions, stated precisely

- **SRC(B)** (Origin's target, OPEN). There is a premise Π passing the disguise test (no operator in its interface
  is non-monomial in the frame; no complex structure or unitary assumed) such that Π ⇒
  `T.availExt 1 Unit (fun _ => conjChannel B)` for a balanced B on a moved pair; field-neutrally, a reversible body
  automorphism mapping a pure frame state of the native readout to a balanced pure state.
- **SPEC_M(B)** (matrix spectator stability, the bridge's matrix form). For every finite R,
  `𝓘 (R × S) (tensorOf 1 B)` for a generating class 𝓘 of T (context stability restricted to B); equivalently, given
  level one inside `DerivedOI`, availability of B ⊗ 1ₙ at every level n (stage 5 D5 N1c [A]; the spectator form
  [X o3_continuous C6]).
- **SPEC_P(g)** (pair spectator stability, (b) for g). For one token τ and every ω in the pair cone K:
  `actτ g ω ∈ K`.

**Identity (I-1) [W + X D1, D2].** For a pair cone K and a token τ:
SPEC_P(R_z(t) ∀t) ∧ SPEC_P(R_x(t) ∀t) ⟺ SPEC_P(R_z(t) ∀t) ∧ SPEC_P(J).
*Proof.* (⇐) R_x(t) = J R_z(t) J⁻¹ and J⁻¹ = J², and τ ↦ actτ is a homomorphism (for `actC` directly, for `actT`
through the transpose) [W]. (⇒) R_z and R_x generate SO(3) (Euler angles), and J = R_z(π/2)R_x(π/2) [X D1]. ∎
With H1–H3 the left side forces Q3 (stage 4 Y2 [A]), so the right side does too.

**Matrix reduction (I-2) [W + X D5].** If a generating class contains the substratum class (context-stable by
theorem) and 1_R ⊗ B for every R, then 1_R ⊗ e^{−itX} = (1_R ⊗ B)(1_R ⊗ D_t)(1_R ⊗ B)† up to diagonal
corrections is in it (product closure of an architecture), so SPEC_M of the drive follows from SPEC_M(B).

## 2. The dependency chain, with both threads' pieces

```
substratum class (monomial, phases incl.)          [K] ContextStable, StructurallyClosed (StructuralClosure:261, :316)
  + SRC(B): one balanced mixer at level one           OPEN  (Origin: O1 envelope, O2 all routes FAILED / CONDITIONAL on KB-D)
  + SPEC_M(B): its spectator form at every level      OPEN  (bridge, matrix form; = what remains for oiPlusMin_iff_qm)
  ⇒ the drive at every level (O3-T1, I-2)             [W + X]
  ⇒ PhaseFreeRichness ⇒ exact finite QM               [K] derivedOI_qm_iff_phaseFree (RouteB:161), oiPlusMin_iff_qm (MinimalRepertoire:569)

pair level (W 3):
  SPEC_P(φ) ∧ SPEC_P(J)  ⟺  A_miss  (I-1)            [W + X]
  A_miss + H1–H3 ⇒ K = Q3                             [A stage 4 Y2]
  SRC(J) presupposed by SPEC_P(J) being a question about an available operation
```

## 3. What each thread can do with this

- **Origin.** SRC(B) is OPEN with a sharp envelope: on the stated access it is impossible (O1-T3, T5, T6), and a
  field-neutral source must change the observation law (Lemma P, O2-KB). The only monomial-input construction
  that meets the Discrete test (KB-D) yields a finite reversible group and so never reaches the drive.
- **Bridge.** The pair-level target can be stated as SPEC_P(φ) ∧ SPEC_P(J): one continuous flow that is
  substratum-native at the matrix level, and one discrete operation. Whether a transfer from the matrix carrier to
  `W 3` exists for the monomial class's context stability is the question that would make the first half free; the
  second half is the spectator stability of exactly the operation Origin is trying to source.
- **Suggested foil (not a claim).** Spekkens' toy theory has a discrete balanced mixer on each token, discrete
  local operations that extend to pairs, and no phase flow: it would separate SPEC_P(J) from SPEC_P(φ) if it meets
  the bridge's other premises — a check for the bridge thread, not done here.

## 4. Classification (§A.31)

- **NEW, O4-N1.** I-1: the bridge's missing assumption is the spectator stability of the substratum phase flow and
  of one discrete balanced mixer, J, which is the Discrete target in the bridge's vocabulary.
- **NEW, O4-N2.** The dependency is mutual and non-discharging: SRC (Origin) and SPEC (bridge) are each the other's
  open premise; at the matrix level SPEC reduces to one discrete operation (I-2).
- **ELABORATING, O4-E1.** Lemma P as a constraint on composite models with passive single-token observation.
