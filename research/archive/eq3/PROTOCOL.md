# EQ3-P — composition coherence as the source of idle extension: design-only protocol

**Status.** Research and design only. Nothing produced here is adopted, frozen or governed, and governance stays frozen.
This thread was requested by the owner as an immediate action after the EQ2 review.

## The question

> Can the requirement that an operation remain valid when an independent system is added (idle extension: IE₁ at
> two copies, IE₂ at three) be derived from a genuinely observational consistency principle, without assuming quantum
> composition in advance?

The candidate principle is **composition coherence (KT∞)**: for every finite family of tokens and every partition of
it into two groups, the joint system is a valid composite (COMP-1) of the two groups. Each group is itself the joint
system of its members, with that composite's full state and effect sets.

KT∞ speaks only of states, effects and probabilities of regrouped composites; it does not mention operations.

## What is already settled (do not redo; re-verify only what you rely on)

Inputs:
- `scratchpad/eqreview/EQ2-SYNTHESIS.md`;
- `scratchpad/eq2/A/RESULT.md`, primary, with its NOTES and scripts;
- `scratchpad/eq2/B/RESULT.md`, for the two-copy machinery;
- `scratchpad/eqreview/REVIEW.md`, the coordinator's checks.

Settled facts:
- **Form is free; existence is the content.** Under local tomography the only candidate extension is `g ⊗ id` (kernel
  `isSpectatorExtension_iff`, SpectatorBridge:188; native EQ2-A a2b S0a). The content is closure,
  `(g ⊗ id)(K_S) ⊆ K_S`.
- **Product effects are blind to the failure.** Positivity of an idle extension on product effects is automatic
  (EQ2-A C12).
- **Exact three-copy countermodels.** `M_odd`, `M_tw` and `M_bs` satisfy every transport of the landed two-copy
  premises, with IE₁, EX and pair-CX, and violate IE₂ (EQ2-A a4; the coordinator's independent check 28/28).
- **KT₂.** COMP-1 on 2|2 bipartitions forces every 4-cycle of twist bits to be even, `τ = δε + c` (EQ2-A D1–D2).
- **KT∞ at six copies.** Through three Bell links on a 3|3 bipartition it forces `K₃ = Λ(K₃*)`: `T`-co-self-dual for
  c = 0, self-dual for c = 1 (written; link identities exact, a4c L5).
  - Both minimal hulls fail that test: −1/16 untwisted (a4 D4); `F`, `G ∈ B_tw*` with `tr(FG) = −½` for c = 1 (a4c).
  - `B_tw` nevertheless has LU-invariant self-positive extensions (a4d).
- **IE₁ cannot be dropped at two copies.** `K_F` = cone(Clifford·products) is closed, admissible, cnot-invariant and
  not SO(3)-invariant, and differs from Q3 and from the twin (EQ2-B b5).
- **Transposed gate class.** IE₂ with H0 excludes the gate class `T∘cnot` (coordinator, `review_eq2a_cm2` T).

## Nodes (depth-first; decisive first; a verdict at each)

- **N1 (two copies): does KT∞ imply IE₁?**
  1. Derive exactly what KT∞ gives at **four** copies. Use COMP-1 on 01|23 and on 02|13, with every pair cone equal to
     `K₂`, plus Bell-type links on (0,2) and (1,3). State precisely which products and effects are used. The
     coordinator expects `K₂ = T(K₂*)` (written, unverified). Verify the link identity exactly, give its twin analogue,
     and check that `K_F` is excluded with an exact witness.
  2. Decide whether every admissible (products ⊆ K ⊆ max), cnot-invariant cone with `K = T(K*)` is Q3 or the twin,
     with **no** local invariance assumed. Either:
     - give an exact countermodel, which makes IE₁ independent of KT∞ plus gate plus admissibility; or
     - give a theorem route with every step checked.

   Useful tools:
   - the bilinear form `B(X, Y) = tr(X Yᵀ)` (signature (10, 6) on Pauli tables);
   - B-orthogonal maps commuting with cnot;
   - linearized rigidity at Q3: the admissible co-self-dual tangent deformations;
   - the bounds `conv(SEP ∪ cnot SEP) ⊆ K ⊆ T((SEP ∪ cnot SEP)*)`.

   Pressure-test any favourable outcome.
- **N2 (three copies, EQ2-A's named wall).** Keep IE₁, as an assumption if N1 does not supply it.
  1. **c = 1:** is there an LU-invariant `K₃ = K₃*` with `B_tw ⊊ K₃ ⊊ B_tw*` (pair marginals Tw)? If there is, does it
     extend to four copies under KT∞?
  2. **c = 0:** is `PSD₈` the only LU-invariant `T`-co-self-dual cone with `BS ⊆ K₃ ⊆ BS*` (pair marginals Q)? Note
     that any alternative must be incomparable with `PSD₈`.

  Methods:
  - stabilizer-twirled sectors as necessary conditions (the GHZ sector is 8-dimensional);
  - explicit constructions: maximal LU-invariant self-positive extensions, then test self-duality;
  - proofs.

  If both answers favour uniqueness, KT∞ with IE₁ gives parity and `K₃ = PSD₈`, hence IE₂ for unitary-conjugation
  pair operations. A countermodel in either case makes IE₂ independent of KT∞.
- **N3 (fallback, only if N2 yields a KT∞ countermodel).** Does the completion (purification) principle exclude that
  countermodel? The principle: every state of a composite is the marginal of a pure state of a larger composite of
  the family.
- **N4 (literature, before any closure attempt; cheap).** Use web search if available. Mark every theorem you did not
  read at the source as unverified. Targets:
  - Barnum–Barrett–Leifer–Wilce, and Barnum–Fuchs–Renes–Wilce 2005 (influence-free states);
  - Barnum–Beigi–Boixo–Elliott–Wehner 2010;
  - Barnum–Wilce 2014 (local tomography and Jordan structure);
  - Barnum–Graydon–Wilce 2020 (composites of Euclidean Jordan algebras);
  - Müller–Ududec 2012 (self-duality from reversible computation);
  - Krumm–Müller 2019 (bits are balls);
  - Chiribella–D'Ariano–Perinotti 2010/2011 (purification);
  - Wilce (conjugates; "royal road").

  The question for the literature: does any result derive parallel composition of operations (dynamical
  monoidality, idle extension) from kinematic composite principles, or show it cannot be derived?

## Productivity test (fixed before the walk)

A finding is a **gem** iff it is one of:
1. an exact countermodel to "KT∞ (at a stated finite instance) with the named premises implies IE₁ / parity / `K₃ = PSD₈`";
2. a theorem route, every step checked, from KT∞ at a stated instance to one of those;
3. an exposed hidden assumption in the KT∞ formulation: which bipartitions, link states or effect sets it presupposes.

Otherwise it is record-only. State results for the finite instance actually used (four or six copies), never for
"KT∞" in general unless proved for all instances.

## Limits

These are the EQ2 protocol's limits (`scratchpad/eq2/PROTOCOL.md`), with these changes:
- **Writes** only inside `scratchpad/eq3/P/`.
- **Reads:** you may read `scratchpad/eq2/*` and `scratchpad/eqreview/*`, but never modify them.
- **Arithmetic and evidence:**
  - Exact arithmetic only for anything certified.
  - Floating-point runs are exploration, labelled in the filename and the header, and replayed separately. Never cite
    them as evidence: EQ2-A's float x3 returned a false negative.
  - Every verdict prints only over green controls, with a countercontrol for every favourable branch (§A.21, §A.31).
- **Scripts** run as `python3 -I -B`, with byte-identical replays recorded.
- **No outward actions:** no git writes, branches, PRs, CI, freezes, ROADMAP or manuscript edits, or premise adoption.
  Do not spawn agents. No Lean build (no toolchain); Lean text is labelled UNBUILT.

## Deliverable

`scratchpad/eq3/P/RESULT.md`, plus a running `NOTES.md` and the scripts. It opens with **0. Answer to the key
question**: positive, negative or open, with the precise finite instance and the named wall. Then come the EQ2
deliverable's seven sections:
- Finding
- Target theorems (UNBUILT)
- Hypotheses ledger
- Missing lemmas
- Formalization strategy
- Research questions
- Evidence and probe log

If writing `RESULT.md` fails, put the full report in the final message.

## Amendment 1 — owner review after the EQ2 synthesis (append-only; it refines, it does not replace)

**Milestones, in order.** An exact counterexample at any stage is a valid and valuable endpoint for that stage.
1. **Four-copy constraint.** Prove or refute the proposed co-self-duality consequence `K₂ = T(K₂*)` exactly.
2. **Cone uniqueness.** Determine whether every admissible co-self-dual cone is the quantum cone or its twin. Report the
   minimal extra structure that achieves this, by trying, in order:
   - nothing beyond admissibility and co-self-duality (countermodels are expected);
   - invariance under the native gate;
   - any further finite symmetry.

   Co-self-duality alone does not identify quantum theory. Name exactly which remaining assumption selects the PSD cone
   or the twin.
3. **IE₁.** Derive full local invariance rather than postulating it.
4. **IE₂.** Exclude all three-copy countermodels, including the twisted configurations (`M_odd`, `M_tw`, `M_bs`, and
   any `K₃` strictly between `B_tw` and `B_tw*`).
5. **General composition.** Show that the resulting constraints extend consistently to every finite number of qubit-type
   systems. Take this up only after 1–4.

**No circularity: state-level versus operation-level coherence.**
- KT∞ must be **state-level** only: regrouping systems gives mutually consistent state spaces, effects, products and
  conditioning.
- **Operation-level** coherence is excluded as a premise: "every permitted operation remains permitted when it acts on
  part of a larger system". That is idle extension itself.
- For every derivation, list each step and mark whether it uses:
  - (s) a state-level fact;
  - (2) an operation on a standalone two-token composite (allowed: it is not IE);
  - (o) an operation acting on part of a larger composite (IE: forbidden as a premise; any use makes the step circular).
- **Hidden assumptions the coordinator found in the proposed four-copy derivation**, to be stated or removed explicitly:
  - (a) **uniform composition.** All pair composites are taken to be the same cone `K₂`. Without it, KT relates the
    cones of different pairs: `K_{01}` against `T(K_{23}*)` through the links, and differently through the (03)(12)
    links. EQ2-A's assumption-watch marker 1 says this is a separate assumption.
  - (b) **link states.** The derivation uses `Φ⁺` both as a state of the link pairs and as an effect on them. With
    admissibility and invariance under the standalone pair gate, `cnot(|+⟩⟨+| ⊗ |0⟩⟨0|) = Φ⁺` supplies the state. The
    dual action of cnot on a product effect supplies the effect. Check this exactly, including the twisted orientation,
    where the link is `R_B Φ⁺`.
- **Independent content.** Do not treat composition coherence as an adopted physical principle. Classify its
  independent content:
  - QM satisfies it;
  - the transported landed premises do not imply it (the hulls fail it);
  - list what it implies and what it does not.

## Amendment 2 — owner precision for milestone 1 (append-only)

**Two inclusions, audited separately.** Treat `K₂ = T(K₂*)` as two claims, and prove or refute each on its own:
- (I) `T(K₂*) ⊆ K₂`;
- (II) `K₂ ⊆ T(K₂*)`.

Proving only one inclusion is a valid partial result, but it does not establish co-self-duality. For each inclusion,
list exactly:
- which regrouping is used, and whether it contributes products of states or products of effects;
- which conditioning rule is used, if any;
- which Bell link is used, and whether it enters as a state or as an effect;
- which uniformity or identification assumption is used.

The coordinator's expectation, to be checked and not assumed:
- (I) needs Bell **states** on the link pairs (product of states under 02|13) and products of effects under 01|23.
- (II) needs Bell **effects** on the link pairs (product of effects under 02|13) and products of states under 01|23.

**Bell effects.** Trace them to existing premises. They need two things:
- (i) the initial product effect, e.g. `e₊ ⊗ e₀`, is an effect of the pair composite. That comes from product effects
  being effects (COMP-1 `prodEff_effect`) and from the single-system effects being available (EFF-1 hypotheses).
- (ii) the dual (Heisenberg) action of the standalone pair gate maps effects to effects.

Settle whether (ii) holds automatically or needs a separate assumption:
- It is automatic if the composite's effect set is every functional with values in [0, 1] on the joint body. This is
  the `IsEffectOn` style: invariance of the state cone under the gate then gives invariance of its dual, and the gate
  fixes the unit effect.
- If the effect set is a restricted set of available tests, (ii) is a separate availability assumption.

Read the COMP-1 and EFF-1 definitions at the base to decide which case applies. Name the result either way.

**Uniform composition: chart, orientation and identification.**
- Equality of pair cones in a shared chart is stronger than abstract isomorphism of the pair composites. State which
  one the derivation uses.
- Specify how the following are fixed:
  - each token's ball chart, which is determined only up to O(3) by the single-system theorems;
  - the pair orientations (the twin differs from Q3 by a reflection on one token);
  - the transposes the Bell links induce.

  A link state defines an identification of two copies: `Φ⁺` induces the transpose, and the twisted link `R_B Φ⁺`
  induces no transpose.
- Without local invariance the pair cones are not yet classified, so twist bits are not yet defined. If the gate
  frames (z, N) are used to align the token charts, say so, and say what freedom remains.

**Outcomes to classify at the end** (the owner's table):
- coherence alone selects the quantum cone;
- coherence plus uniform composition selects it (uniformity is then an independent structural principle, not IE);
- an additional finite symmetry selects it;
- coherence yields only one inclusion;
- an exact countermodel survives everything.

Uniform composition is a structural uniformity principle: all equivalent pairs obey the same rule. It is distinct from
the closure property (IE) under investigation, so a result that needs it is neither trivial nor circular.

**The decisive question:** does consistency of states, effects and conditioning across different groupings force the
transformations permitted on smaller systems to remain valid inside larger systems, with no extended operation among
the premises?
