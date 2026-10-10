# EQ5-PREM — sourcing the physical premises of KT(4) (research protocol; frozen at launch)

Owner's question:
> "Can existing observational principles imply the physical consistency assumptions that KT(4) currently requires?"

Owner's instructions:
- Start with the relationship between independent preparation, regrouping invariance, `TokProdState` and
  `TokenCoherent`.
- Then investigate, separately, whether physical reversibility and operational availability can supply gate
  preservation.
- "The source countermodels prove that the presently stated weak architecture is insufficient. They do not rule out
  derivations from stronger, independently motivated conditions elsewhere in the programme. Every proposed implication
  should be checked against those countermodels before investing in a Lean proof."
- "The statement that four-copy consistency forces quantum cones must not become a claim that the observational axioms
  alone force them."

## Inputs (read-only)

- Certified base `bcbc516f`: `scratchpad/eq/base/` (manifest `scratchpad/eq/base.manifest.sha256`).
- EQ4-F design package at `f0d37906`: `scratchpad/eq5/inputs/` (manifest `scratchpad/eq5/inputs.manifest.sha256`).
- EQ4-SOURCE result, scripts and notes: `scratchpad/eq5/SOURCE/`.
  - Countermodels: the anchor sum, M_ρ, M_tw, M_id and M_T, and `ball3MaxComposite` / `ball3MinComposite` with
    `cnot`.
  - Definitions: `TokProdState` and STMC.
  - The coordinator's audit: `scratchpad/eqreview/EQ5-SOURCE-AUDIT.md`.
- EQ4-F dependency graph: `scratchpad/eq5/F/DEPGRAPH.md` (§7: USES; §7.7: SUPPLIES).
- The protocol of the previous threads, `scratchpad/eq5/PROTOCOL.md`: its shared rules apply here unchanged.

## Questions

**Part A — four-token coherence.**
- A1. Make precise, as predicates on the KT(4) data, three things:
  - "independent preparation" (product states of independently prepared tokens);
  - "regrouping invariance" (the composite does not depend on how tokens are grouped);
  - their relation to `TokProdState` and `TokenCoherent`.
  - Give every implication with a separate witness per direction (§A.34), or a countermodel.
- A2. Census the programme for principles that could supply them. Read the base: landed rounds, ROADMAP, Main.md and
  the audits, at `bcbc516f`. For each candidate:
  - state it precisely;
  - classify it as LANDED ([K]), ADOPTED POSIT ([A]), TRANSPORTED ([T]) or UNSOURCED ([U]);
  - test the implication "candidate ⇒ TokProdState (or tok)" against every EQ4-SOURCE countermodel. An implication is
    refuted if a countermodel satisfies the candidate and violates the target.

  Candidates are not limited to these:
  - observational independence, spectator compositionality, and the protocol tower (PT/CT);
  - stage completion, ORD-1 composition order, CMP-1 completion, IIP-1 invariant inner product;
  - K1, K2, K∞ and Kₙ material;
  - the region tower. Flag any route through it as importing the complex matrix cone.
- A3. For each candidate that survives every countermodel:
  - give a written derivation ([W]) with exact ingredients ([X]);
  - say whether the candidate is independently motivated, or a restatement of `tok` in other words. Such a restatement
    is a relabelling, not a source.

**Part B — gate preservation (`hgate`; `hinv` is derivable from it under orthogonality and closedness).**
- B1. Make precise "physical reversibility" and "operational availability" of a pair's native gate at the level of the
  pair body. Candidates: COMP-1 `JointReversible`, `PreservesBody`, OPACT-1, K1 premises, EFF-1 / K1-BRIDGE-1
  availability.
- B2. Test each candidate implication "candidate ⇒ hgate" against the landed countermodels: the bodies of
  `ball3MaxComposite` and `ball3MinComposite` with `cnot`, and any others found.
- B3. For each survivor: a written derivation with exact ingredients, and the independence assessment as in A3.

**Part C (record only).** Record any finding that bears on closedness (`hcl`), such as stage completion's closed hull.
Do not pursue it beyond recording.

## Outcomes

Each of A and B has three possible outcomes, all of them successful:
- **SOURCED.** A landed or adopted principle implies the premise. The derivation is written; exact checks are given.
- **SOURCEABLE.** An independently motivated principle stated elsewhere in the programme (not landed) implies it.
  Name the principle and its status.
- **NOT SOURCED.** No candidate survives the countermodels. Name the weakest additional principle found, and say
  whether it is a restatement.

## Rules (in addition to PROTOCOL.md's shared rules)

**Claims and evidence.**
- Apply the P/A/C rule. A model of P ∧ ¬C shows only insufficiency. Necessity of A relative to P needs a proof of
  P ∧ C ⇒ A. Never write "required" or "necessary" without that proof.
- Check against the countermodels first. Every proposed implication is tested against every EQ4-SOURCE countermodel
  before any derivation is written.
- Use exact arithmetic only. Every verdict prints over green controls, with the decision rule fixed in the script
  header before the first run.
- Print no timing in stdout. Run scripts as `python3 -I -B`. Replay every script, which must be byte-identical. Keep
  failed runs as `.runN`.

**Scope.**
- No Lean work, and no CI.
- No git writes, no branch, PR, ROADMAP or manuscript edit, and no premise adoption.
- Spawn no agents.
- Write only in `scratchpad/eq5/PREM/`.
- Check both manifests at the start and the end.

**Circularity.**
- Flag any route that uses IE₁, IE₂, the quantum cone as a premise, the complex region tower, or an operation on part
  of a composite (an (o) step).

## Output

`scratchpad/eq5/PREM/RESULT.md` containing:
1. Answers to A1–A3, B1–B3 and C.
2. A candidate table with, for each candidate:
   - its status;
   - its implication;
   - the countermodel verdict per countermodel;
   - its independence.
3. An evidence log with hashes.
4. An integrity section.
5. A "What is not claimed" section.
