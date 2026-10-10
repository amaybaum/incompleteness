# EQ5 — three efforts after the EQ4-F preflight: protocol (research and design only)

**Status.** The owner authorized design and research work on three efforts:
- EQ4-F, proof development;
- EQ4-SIX, research only;
- EQ4-SOURCE, research only.

Nothing here is adopted, frozen or governed. Not authorized:
- an F designation, CI dispatch or merge;
- a git write, branch, push or PR;
- a ROADMAP or manuscript edit, or premise adoption.

The preflight (run 37900638054) is recorded as an expected red run, not a completed proof.

## The question behind all three

> Does consistency between observations of larger composite systems uniquely force quantum mechanics, or does nature
> require an additional independent physical principle?

A rigorous answer in either direction is a successful outcome. Results are stated for the instance actually used, and
never for "KT∞" in general unless proved for all instances.

## Base and inputs (read-only for both threads)

- **Base:** certified main `bcbc516f`, snapshot `scratchpad/eq/base/` (manifest `scratchpad/eq/base.manifest.sha256`).
- **The preflight package:** commit `f0d37906`, copied to `scratchpad/eq5/inputs/`:
  - `FourCopyDefs.lean`, `FourCopyParity.lean`, `FourCopyPackage.lean`, `OIBridge.lean`;
  - `PREFLIGHT-RESULT.md`, `PREFLIGHT-LEDGER.md`;
  - manifest `scratchpad/eq5/inputs.manifest.sha256`.
- **Settled research (audited):**
  - `scratchpad/eq4/P/` (RESULT, NOTES, probes);
  - `scratchpad/eqreview/EQ4-AUDIT.md`, which carries corrections that take precedence over EQ4-P's text;
  - `scratchpad/eq4/F/` (FORMAL.md, design);
  - `scratchpad/eq3/P/RESULT.md` and `scratchpad/eqreview/EQ3-AUDIT.md`;
  - `scratchpad/eqreview/EQ2-SYNTHESIS.md` and `scratchpad/eqreview/INTEGRATION-DESIGN.md`.
- **Architecture records:**
  - `scratchpad/k2d/K2-LEDGER.md`, `scratchpad/sa/SA-LEDGER.md`;
  - `scratchpad/kn/KN-CENSUS-RESULT.md`, `scratchpad/k-infinity/K-INF-DESIGN.md`;
  - the base's `verification/ROADMAP.md`, `verification/lean-mathlib/OIBridge/*.lean`, `papers/*.md` and `book/*.md`.
- **Mathlib v4.33.0 source** (grep only): `/home/user/leanprover-community/mathlib4`.

## Shared rules

**Owner's P/A/C rule:**
- `P ∧ A ⇒ C` is sufficiency.
- An exact model of `P ∧ ¬C` shows only that P alone does not give C.
- Necessity of A relative to P needs a proof of `P ∧ C ⇒ A`.
- Never write "required" or "necessary" without that proof. A result that uses an unverified literature ingredient is
  conditional on it, and is stated as such.

**§A.34:** every displayed equivalence carries a separately identified witness for each direction.

**Evidence tags:**
- [K] landed kernel identifier at the base (file:line);
- [X] exact computation in the thread's directory, replayed byte for byte;
- [W] written argument;
- [E] exact exploration (a lead);
- [F] floating-point exploration (certifies nothing);
- [L, unverified] literature not read at the source.

**Scripts:**
- Run as `python3 -I -B`.
- The decision rule is stated in the header before the first run, as rules and not expected numbers.
- A VERDICT line prints only over green controls; every favourable check has a countercontrol.
- No wall-clock time or other nondeterministic value in stdout. An x13-type timing field breaks the replay; write
  timings to stderr if needed.
- Failed runs are kept as `.runN.*`, and pre-run edits are recorded.
- Every certified script is replayed byte for byte at the end, with hashes recorded.

**Integrity:**
- At start and end: check the base manifest and the inputs manifest (`sha256sum -c --quiet`).
- Write `.start_marker`.
- Record the repository HEAD read-only. The coordinator does not commit during these threads.
- If HEAD moves, inspect the reflog read-only and record what it shows. Never repair anything.
- Writes go only inside your own directory. Never modify inputs.

**Limits:**
- No outward actions: no git writes, branches, pushes, PRs or CI.
- Do not spawn agents.
- There is no Lean toolchain, so every Lean text is UNBUILT.
- Network egress is restricted. Do not route around it; mark literature [L, unverified].

**Investigation mode:** §A.31 (gem-finding, depth-first).
- Number the branch nodes, and record a verdict at each, closed by an explicit check.
- Apply maximum skepticism to every branch whose outcome favours the framework.
- Fixed point: 3–4 consecutive passes with no NEW finding.

## EQ4-SIX — six-token coherence: proof or countermodel (`scratchpad/eq5/SIX/`)

**Precise question.** Let P6 be:
- **KT restricted to the token set {0, …, 5}.** Every nonempty subset S carries one closed convex cone K_S, one body
  per token set. For every bipartition S = A ⊔ B:
  - products of states lie in K_S (`prod_mem`);
  - products of effects of the full dual sets lie in K_S* (full `IsEffectOn` effects).
- **The pair premises,** with pair cones Q3 or the twin as settled at KT(4), together with:
  - the native gate and its inverse on standalone pairs, which are (2) steps;
  - closedness.
- **The single-token cone:** the Bloch ball.

Then decide, for c = 0 and separately for c = 1:
- **(a) Proof:** P6 ⇒ K₃ = PSD₈ (c = 0), equivalently a GHZ-class element in K₃ (E3 within six tokens, as audited).
  The route must have every step checked.
- **(b) Countermodel:** exact cones (K₃, K₄, K₅, K₆) satisfying every P6 constraint with K₃ ≠ PSD₈. Each constraint
  type is certified exactly, or by a written proof whose ingredients are exact.
- **(c) Open:** the wall, sharpened beyond EQ4-P's ML1–ML3.

Either (a) or (b) is a successful outcome.

**Forbidden as premises:**
- purification;
- transitivity, in either reading;
- Choi-state availability, IE₂, or any (o)-type step (an operation on part of a larger composite);
- any principle not in P6 introduced to reach the desired conclusion.

If a further principle is genuinely needed, name it as a separate candidate A. Classify it by the P/A/C rule (is it IE₂
in disguise?). Report any result that uses it as conditional on it.

**Settled and audited (rely on, re-verify only what you use):**
- Within six tokens: uniformity, S₃ symmetry, local-filter (LU, SLOCC) invariance at five tokens, and co-self-duality
  K₃ = T(K₃*) (c = 0) or K₃ = K₃* (c = 1). BS ⊆ K₃ ⊆ BS*.
- E3 within six tokens.
- Colouring lemma; maximality certificates ν (−4) and F, G (−½).
- The five-token pair-network countermodel.
- GD-sector models K_A (c = 0) and K_tw (c = 1). The GD sector conditions do not decide the wall.

**Nodes** (depth-first, decisive first):
- **N1. The six-token constraint system.**
  - List every crossing type among families of ≤ 6 tokens after uniformity.
  - Identify which are implied by others (EQ4-P p7 is the starting point).
  - State exactly what remains on (K₃, K₄, K₅, K₆). This is the problem statement for N2–N4.
- **N2. Lift (ML1).** Does K_A, or any GHZ-free sector solution, lift to a closed, SLOCC- and filter-invariant,
  S₃-symmetric, co-self-dual K₃? Either construct a lift, or obstruct every lift using information outside GD:
  - general product filters (ML5);
  - other twirl sectors, including the ten-dimensional GHZ-coherence sector of RQ1;
  - the full 64-dimensional co-self-duality.
- **N3. Extension (ML2).** Given a candidate K₃, construct K₄, K₅, K₆ (minimal and maximal choices first) and check
  every crossing; or prove none exists.
- **N4. c = 1 (ML3)** for K_tw.
- **N5. Control, mandatory for any proof route.** The route must use a constraint that genuinely involves six tokens.
  Show explicitly where it fails for the five-token countermodel PN₅; a "proof" that PN₅ also satisfies is wrong.
- **N6. Literature,** [L, unverified]: SLOCC-invariant cones; co-self-dual cones in multipartite GPTs; Barnum–Wilce
  composites.

**Productivity test** (fixed now). A finding is a gem iff it is one of:
1. an exact certificate of (a) or (b) at a stated instance;
2. a theorem route with every step checked;
3. an exact obstruction for a stated class of lifts or extensions;
4. an exposed hidden assumption.

Otherwise it is record-only.

**Deliverable:** `scratchpad/eq5/SIX/RESULT.md`, plus `NOTES.md` and the scripts. It contains:
- 0. Answer: proved, countermodel or open, with the instance and the named wall;
- the outcome table, as in EQ4-P;
- the ledger under the P/A/C rule;
- missing lemmas and research questions;
- the evidence log with hashes.

## EQ4-SOURCE — what the architecture supplies (`scratchpad/eq5/SOURCE/`)

**Precise question.** Do `TokenCoherent` and the KT(4) inequalities (`FourCopyCoherent`, through `KT4` and Lemma B1)
follow from the existing observational and composition architecture? For every premise the headline proof uses,
distinguish:
- **USES:** what the proof consumes. This is the exact Lean hypothesis or field in `inputs/FourCopyPackage.lean`.
- **SUPPLIES:** what the framework provides.

The headline `kt4_forward` and its setting give these premises:
- `hcls` (`NClass`);
- `hadm` (`PairAdm` = `CandidateCone` ∧ `IsConvexCone`);
- `hcl` (`IsClosed`);
- `hgate`, `hinv`;
- `H : KT4`: two `PreComposite`s of the normalized pair bodies, with every field consumed by Lemma B1's planned route
  (`prod_mem`, `prodEff_effect`, `prodEff_apply`, bilinearity), plus `one_body` and `tok : TokenCoherent`;
- the setting: the `W 3` table carrier (two-copy local tomography), `pairBody` normalization, per-token charts.

**Classes** (one per premise, with anchors):
- [K] supplied by a landed kernel theorem: file:line at the base, with an exact statement match. Give the statement
  diff if it is not exact.
- [A] supplied by an adopted premise: ROADMAP or manuscript anchor, and its recorded status.
- [T] transported: a two-copy premise applied to each pair as a standalone composite. Give the two-copy source.
- [U] unsourced. Then give exactly one of:
  - **route:** a derivation from the architecture's stated premises, written and exact, with every step's premise
    named;
  - **countermodel:** an exact model of the architecture's stated premises in which the premise fails;
  - **open:** the precise missing link named.

**Specific questions:**
- **Q1.** Does the base contain any carrier or composite structure for three or more copies (COMP-1 is two-factor;
  Kₙ and K∞ are OPEN)? Which records say so?
- **Q2. TokenCoherent.** What could supply it, and is any of these present?
  - a coherence (associativity and commutativity) of composition;
  - a token or site identity in the substratum or region structure;
  - the observational protocol tower.

  Is EQ4-F's transposed-factor model (f1 W4), or another model of KT4 without `tok`, also a model of the
  architecture's stated premises?
- **Q3. The inequalities.** Given whatever four-copy structure the architecture supplies, if any:
  - do the two families follow by Lemma B1's route?
  - is the full-effect reading supplied (EFF-1 Q-SET: CONDITIONAL-FULL-EFFECTS)?
  - is the one-body clause supplied?
- **Q4. The pair-level premises** (N-CLASS, gate, inverse, admissibility, closedness): landed (DIM-1, K2-GUARD-1,
  K1-SHARP-TESTS-1, KTRANS-DENSE-1, …), transported, or unsourced?
- **Q5. Circularity.** Does any route use IE₁, IE₂, the quantum cone, or an (o)-type step?

**Deliverable:** `scratchpad/eq5/SOURCE/RESULT.md`, plus `NOTES.md` and the scripts. It contains:
- 0. Answer: does the architecture supply `TokenCoherent` and the KT(4) inequalities? Yes, no, partially or open, with
  the precise missing link;
- the USES-versus-SUPPLIES ledger, one row per premise;
- routes and countermodels;
- candidate premise formulations, phrased as proposals, not adopted, with each checked for disguised circularity;
- the evidence log with hashes.

## EQ4-F — coordinator's design work (`scratchpad/eq5/F/`; not a thread)

The coordinator produces:
- the dependency graph of the 48 open obligations;
- the hardest unresolved proof steps;
- the exact minimal assumptions of the headline;
- UNBUILT proof drafts, prioritizing the classification and bridge lemmas.

The certified result admits no `sorry`, no new axiom and no circular hypothesis. The threads do not write there.
