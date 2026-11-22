# O1 restated as two obligations: coherence creation and coherence detection

**WIP / UNVERIFIED. Wording record only.** Revision r2 answers the review of `0ba83cff` (#1513 c.7066721761 and c.7066739331). It edits no manuscript, reviewed record or Issue body. It
proves nothing new and changes no status. It has not been reviewed.

- **Authority.** Owner decision #1169 c.7066541026, Decision 2. That decision approves restating O1 as
  the pair {coherence-creating operation (non-MIO), coherence-detecting operation (non-DIO)},
  possibly one element, in place of FLOW alone. It sets three provisos:
  - the two properties are stated separately;
  - the wording keeps the exact hypotheses of OPRES Theorem C and Proposition D, both (I);
  - violating MIO and violating DIO are distinct obligations, and establishing one is not presented
    as establishing the other.
- **Supporting results.** OPRES at `7669e511c4d5473f177444bc84de09081d375dc3` (#1511, reviewed):
  `verification/programmes/oi-qm/reconstruction/opres-20261121/NOTE.md` on that commit, §2
  (definitions), §3 (Lemma C, Theorems B and C, Proposition D) and §4 (CC-1). OPRES is not on `main`
  and is cited read-only.
- **The O1 it replaces.** QOPS-P2 (#1501 at `cd3672fa`) records KIN as O1's earliest import and FLOW
  as its earliest unsupported step.
- **Tracking.** Issue #1512. The companion record `NOTE.md` (Task A) is in this directory.

## 1. Definitions (as in OPRES §2)

Configuration spaces are countable unless stated otherwise. Δ is the conditional expectation onto the
configuration (diagonal) algebra, and the configuration basis is fixed physically. Let Φ be a
completely positive, trace-nonincreasing map.
- Φ is **MIO-type** (non-creating) iff Φ∘Δ = Δ∘Φ∘Δ.
- Φ **creates coherence** iff it is not MIO-type: some diagonal input has a non-diagonal output.
- Φ is **DIO-type** (non-detecting) iff Δ∘Φ = Δ∘Φ∘Δ. In the Heisenberg picture: Φ* maps the
  configuration algebra 𝒜 into 𝒜.
- Φ **detects coherence** iff it is not DIO-type: the output diagonal depends on an off-diagonal
  entry of the input.

For a unitary W on ℂ^{C_V}:
- κ_col(W) := sup_x sup_{i≠j} |W_{ix} W_{jx}|;
- κ_row(W) := sup_i sup_{v≠v′} |W_{iv} W_{iv′}|.

Both are positive iff W is non-monomial (OPRES Theorem C(c)).

## 2. The restated O1

**O1 (restated).** Let W be a non-monomial unitary on ℂ^{C_V}. Let Φ be a trace-preserving protocol:
a finite composition, with feedforward and discard, of operations O_1, …, O_n. Realizing W by Φ,
within the distances below or exactly as a postselected branch p·Ad_W with p > 0, places **two
separate obligations** on the operations O_k.

**O1-C (creation; non-MIO).**
- *Obligation.* Some O_k creates coherence.
- *Support.* OPRES Theorem C(a) and C(d).
- *Hypotheses, exactly as there.* KIN (the Born-form representation on configurations); countable
  carriers; Φ as above.
- *Statement.* If ‖Φ − Ad_W‖_⋄ < 2κ_col(W), some O_k is not MIO-type. In the exact form, a branch
  p·Ad_W needs a non-MIO element unless W is monomial.
- *Scope.* Theorem C(a) is stated on countable carriers only. Proposition D does not treat the
  creation half. On measurable carriers this record states no creation obligation beyond OPRES's
  paper remark that protocols with classical hidden laws remain classical processes (OPRES §3,
  "Creation half on measurable carriers", P).

**O1-D (detection; non-DIO).**
- *Obligation.* Some O_k detects coherence.
- *Support, countable carriers.* OPRES Theorem C(b) and C(d).
  - Hypotheses, exactly as there: KIN; countable carriers; Φ as above.
  - Statement: if ‖Φ − Ad_W‖_⋄ < 2κ_row(W), some O_k is not DIO-type. In the exact form, a branch
    p·Ad_W needs a non-DIO element unless W is monomial.
- *Support, measurable carriers.* OPRES Proposition D.
  - Hypotheses, exactly as there:
    - KIN; C_V finite; (H, ν) a standard measure space;
    - every bijection T of C_V × H used is measurable, with measurable inverse, and **nonsingular**
      for counting × ν;
    - every appended hidden state ω is a **normal** state on B(L²(H));
    - 𝒜 = ℓ^∞(C_V) ⊗̄ L^∞(H), acting by multiplication;
    - configuration readouts are instruments indexed by **countable** measurable partitions with
      projections in 𝒜, or instruments whose duals preserve 𝒜;
    - DIO-type is taken in its Heisenberg form, O*(𝒜_out) ⊆ 𝒜_in.
  - Statement: if every O_k satisfies O_k*(𝒜) ⊆ 𝒜, then ‖Φ − Ad_W‖_⋄ ≥ 2κ_row(W). So within that
    distance some O_k has a dual that leaves 𝒜.
- *Not part of the support.*
  - Remark D′ (finite visible carriers with any hidden state, (I) on the algebraic lift) was pending
    review in OPRES.
  - Conjecture D″ (singular bijections) is not proved.
  - Neither is used here.

**Labels.** O1-C and O1-D are each (I), on the hypotheses listed with them. Neither is (N). Each
states a necessary condition only.

## 3. The two obligations are distinct

- **Neither implies the other.** Discharging O1-C does not discharge O1-D, and discharging O1-D does
  not discharge O1-C. Each is witnessed separately in OPRES:
  - **Non-MIO without non-DIO.** Appending a fixed coherent state ω, such as |+⟩, creates coherence
    and is DIO-type (OPRES Lemma C). So a native coherent source alone discharges O1-C and leaves
    O1-D open. By OPRES Theorem B, such a protocol stays at diamond distance at least 2κ_row(W)
    from Ad_W.
  - **Non-DIO without non-MIO.** The destructive readout ⟨±| detects coherence and is MIO-type,
    because its output space is one-dimensional (OPRES CC-1, step 3). So a native coherence-detecting
    readout alone discharges O1-D and leaves O1-C open. By OPRES Theorem C(a), a protocol
    without a creator stays at diamond distance at least 2κ_col(W) from Ad_W.
- **One element may meet both.** A non-monomial unitary step (FLOW; `gateFlow_not_monomial`,
  `OIBridge/CoherentContinuumSource.lean`:74, K) is both non-MIO and non-DIO. Its unitary has a
  column and a row with two nonzero entries (OPRES Theorem C(c)). That one element discharges both
  obligations, and each is still checked separately.
- **No sufficiency claim.** The pair is necessary. CC-1 shows that one creator and one detector,
  with native diagonal phases and permutations, realize Hadamard exactly (OPRES §4). This record
  claims no sufficiency beyond that construction.

## 4. How Task A bears on O1-D

Task A (`NOTE.md` §0, §3) keeps three levels separate. It does not extend a result from one level to
another.

- **Effects.** For every readout procedure the corpus defines, under readings R1 and R2, the effects
  lie in 𝒜 (RA-1). This is Proved on countable carriers. On measurable carriers it holds only within
  the scope of `Main:336` and `EP:100`. No such readout discharges O1-D through its effects.
- **Instruments.** The full branch maps, including the state update, are DIO for items 2, 3
  (non-selective) and 5–10 (RA-1′). Items 11 and 12 have no update rule in the corpus. Items 1, 4 and 22
  have the `Main:664` update for the diagonal sector only, and that passage assigns coherent inputs
  to the completion and the bridge, both imports. Whether these items discharge O1-D is therefore
  **Open**. Diagonal effects do not imply a DIO update. Whether
  all native instruments are DIO is Open.
- **Operationally accessible observable algebras.** `Str:742`, `Str:788`, `Main:722` and `GR:366`
  state that the observable algebra is the full matrix algebra. Their operational meaning, and their
  compatibility with R-READ, are unresolved. A mathematically available observable algebra is not a
  set of implementable measurements. If a native instrument realizing a non-diagonal effect were
  established (premise IMPL-R5, `NOTE.md` §3.1), it would discharge O1-D.
- **Whether bare OI supplies non-DIO is Open.** This record does not declare it impossible.

**If R-READ fails.** Suppose some native readout has an effect outside 𝒜, through an open item, an
effect-only instrument or the declared full algebra.
- That readout discharges O1-D. An effect outside 𝒜 already makes the instrument non-DIO.
- It does not thereby discharge O1-C: a destructive readout is MIO-type.
- If it is a sharp, destructive, projective readout in a basis unbiased with respect to the
  configurations, then together with a coherent source |+⟩ (O1-C), CZ and an X correction it
  realizes H exactly (OPRES §8, CC-1).
- An unsharp non-diagonal effect discharges O1-D without giving exact H (OPRES §8).

**If R-READ holds at the effect level.** A non-DIO update with diagonal effects would still
discharge O1-D. For items 1, 4, 11, 12 and 22 this is not excluded.

## 5. What this record does not do

It does not restate O1 in any manuscript, ROADMAP row or reviewed record. It adopts no premise and
makes no broader quantum-operational claim. It states the approved wording and its supporting
hypotheses only.
