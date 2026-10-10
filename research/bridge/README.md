# research/bridge — the composite-action bridge from embedded observation (priority 1)

**Question.** Can the composite action (b) — the native single-token operations (the drive and its off-frame
partner), idle-extended to one token of a pair, preserve the pair's state cone — be derived from an
embedded-observation principle, or is it independent of every such principle? Stage 6 (archived) proved (b)
INDEPENDENT of every premise at L that reaches the pair cone, with the explicit countermodel K(Z_F) and the missing
assumption isolated as A_miss: for one token, the cone is invariant under `R_z(t)` and `R_x(t)` for all `t`
(ball3Drive's flow and its J-conjugate; the instance of OI⁺-1 for the drive and one off-frame partner). This thread
asks what embedded observation adds, at the hidden-history level H, that L does not have at the pair level P.

**Starting checkpoint.** Branch `research/bridge` from commit `4dc0321c` (= L `9f9f8257` + `research/archive/`).
Read first, in this order: `research/archive/pt/INTEGRATION-NOTE-STAGE6.md` (§0, §3, §5), `…/pt/T6/TEST.md`
(§2.1 D1, §2.5, §5), `…/pt/R6/REASSESSMENT.md` (§6: what L provides at level H; the Main.md:552 `I_a ⊗ I_b`
marker), `…/pt/INTEGRATION-NOTE-STAGE5.md` (ζ embedded observation / observer recursion: drivability form
INDEPENDENT; literal transitivity inadmissible; extreme-ray transitivity UNRESOLVED), `…/drive/RESULT.md`
(F-D1 matrix route forces the Bloch ball; F-D2 the continuum is free on the completed body via closure; F-D3 a
stage-preserving operation has finite order), `…/opact/RESULT.md`. Kernel at L: `verification/lean-mathlib/OIBridge/
EmbeddedObservation.lean`, `OIRealization.lean` (H→M realizations of the sealed core), `CompositeInterface.lean`,
`K2Guard.lean`, `CompositeDimension.lean` (the pair carrier `W 3`, `actC`/`actT`, `cnot`), `KInfFoundations.lean`
(`ball3Drive`, `ElementaryDrivability`). Manuscripts at L: `papers/Main.md` :544–562 (realization and gluing),
`papers/GR.md` :228 (OI⁺-1), :328 (H-local-lift and companions).

**Research plan (depth-first; each node closed by an explicit check before the next).**

- **B1 — the hidden-level composite.** Define, exactly and in the smallest finite model, a pair of embedded
  observers: two systems with hidden configuration registers, visible readouts, and native operations realized as
  hidden permutations. Define the hidden composite cone K_H as the image of hidden product distributions under the
  readout. Determine the exact assumptions under which K_H is well defined and (b_H) — a local hidden permutation
  preserves K_H — is a theorem. Expected: a locality-of-registers assumption (product configuration space) does
  the work; find whether it is an existing named hypothesis (H-local-lift, H-observer-bundle: GR.md:328, SM.md:791)
  or new, and apply the disguise test to it (does it restate (b)?).
- **B2 — transcription of the embedded-observation principles.** For each principle at L that mentions embedded
  observation or observer recursion (`EmbeddedObservation`, `ObserverRecursion`, `HasParallelReferenceExtension`,
  `ContextStable`, `LayerFlowExecutable`), write its transcription to `W 3` explicitly, without presupposing the
  tensor composite, and test it against K(Z_F) by exact computation: if K(Z_F) satisfies the transcription, the
  principle does not yield (b) (record INDEPENDENT); if it excludes K(Z_F), isolate the clause that does the work
  and run the disguise test on that clause.
- **B3 — finite versus continuous.** At level H only finite-order local operations exist (F-D3), and the
  H-sourced finite operations are frame-monomial (NOT, phases, `cyc3`), which leave exotic cones (stage 4/5: the
  `d_low = 5/256` seed). Decide: can embedded observation together with the K∞ completion (closure on the
  completed body, F-D2) source an off-frame finite rotation or a dense subgroup on one token? If not, state and
  prove the no-go for finite substrata (a FAILED route with its exact obstruction); if the completion supplies a
  continuous flow, (b) for that flow is exactly A_miss — record the reduction.
- **B4 — the realization question (decisive).** Is there an embedded-observer realization (two hidden registers,
  readouts, the native gate as a hidden permutation) whose composite cone is K(Z_F)? Construct one exactly (then an
  exotic pair is realizable and INDEPENDENCE survives embedding), or prove an obstruction (then an H-level
  principle excludes K(Z_F) — the bridge). Exact finite computations on small configuration spaces are expected to
  decide instances; a general statement needs a written proof.
- **B5 — the exact content.** Whatever B1–B4 yield, state the weakest H-level principle that supplies A_miss, its
  status (assumed / theorem for which objects), its disguise test, and the theorem at L that would close it
  (statement, level, obligation it discharges: K2's local-action clause with K∞-Act / K∞-Drive).

**Rules.** Exact arithmetic only (`fractions` / `sympy`); every script run as `python3 -I -B`, stdout to `.out`,
stderr + `exit N` to `.err`; decision rule in the header before the first run; failed runs kept as `.runN.*`;
every final script replayed byte-identically. Status labels CERTIFIED / CONDITIONAL (named item) / CONJECTURE /
FAILED / OPEN on every claim in `RESULTS.md`. Q3 (the PSD cone) and the dictionary `pauliW` are comparison and
construction tools, never premises. Hidden-history (H) and pair-cone (P) statements are kept apart: an H-level
statement reaches a cone only through a proved bridge, and every bridge is stated as a theorem with its premises.
Favourable branches (a derivation) get maximum skepticism; a too-easy independence is pressure-tested against the
weakest form, not a strong one.

**Governance.** Write only under `research/bridge/` on this branch. Never touch `main`, manuscripts (`papers/`,
`book/`), `verification/` or any certification record. Lean work goes on disposable branches
`dev/bridge/<topic>` (created from this branch), where modules may be added under
`verification/lean-mathlib/OIBridge/` for a CI build via `workflow_dispatch` on that branch; a successful module
is incorporated here as a design module under `research/bridge/lean/` with the dev commit and the run id cited,
and it stays [D] until a governed round certifies it. Commit early and often; push to `origin research/bridge`
only (`git push -u origin research/bridge`). Record every commit's purpose in `LOG.md`.

**Coordination.** Results relevant to another thread are proposed in `research/bridge/handoff-proposals/` and
delivered by the coordinator through `research/HANDOFFS/` on `research/overview`; handoffs received arrive in
`research/bridge/inbox/` and are acknowledged in `LOG.md` before use. Other threads' branches are not read.
