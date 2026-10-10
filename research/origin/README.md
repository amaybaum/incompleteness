# research/origin — the Discrete and Continuous Origin targets

**Question (the owner's note 3, verbatim in `research/archive/pt/audit/stage3-inputs/OWNER-NOTE3-ORIGIN-RUNGS.md`).**
- *Discrete Origin:* derive an accessible, physically sourced, discrete, **non-monomial** coherent mixer from the
  substratum — together with its permitted preparation, reuse and readout protocol — without assuming the desired
  quantum operation, and establish an exact interference witness with the available preparations and
  measurements. Operational test: `|0⟩ —H→ |+⟩ —H→ |0⟩` with probability 1; with complete path dephasing between
  the mixers, 1/2. A non-ones-fixing operation is necessary (`instAvail_unitary_fixes_ones`) but not sufficient
  (`Z = diag(1, −1)` moves the all-ones ray and creates no coherence).
- *Continuous Origin:* derive the continuously driven transition of the minimal repertoire; `oiPlusMin_iff_qm`
  then supplies the complete finite operational theory under the other stated hypotheses.
- The first is deliberately weaker; success there establishes neither the second nor a unique selection of
  quantum theory over classical constructions. Methodological requirement for both: the operation must be derived
  from OI's substratum, not introduced through an interface already containing the desired coherence.

**Starting checkpoint.** Branch `research/origin` from commit `4dc0321c` (= L `9f9f8257` + `research/archive/`).
Read first: the owner's note; `research/archive/drive/RESULT.md` (DRIVE: a new premise is necessary; F-D1 the
matrix route forces the Bloch ball; F-D2 the continuum is free on the completed body via closure; F-D3 a
stage-preserving operation has finite order), `…/opact/RESULT.md` (an extra premise is necessary for operations;
the weakest is RESPECT + FiniteRank), `…/oistage/RESULT.md` (the protocol tower; NG1 finite Ω ⇒ polytope; NG2
passive + reversible step excludes strictly convex bodies), `…/rank/RESULT.md`, `…/quotient/RESULT.md` (no 4D
invariant effect space with unit), `…/k-infinity/K-INF-DESIGN.md`, `…/pt/S2/` (the class `𝒞_mono` of
frame-monomial operations creates no coherence in the frame basis), `…/pt/INTEGRATION-NOTE-STAGE5.md` §1 (L0–L3:
the drive is not sourced at any level). Kernel at L: `verification/lean-mathlib/OIBridge/AncillaInterference.lean`
(`HasAncillaQubitInterference`, `mix_seed`, `interference_branch`), `PhaseSource.lean` (`permClass_onesFixing`),
`InstrumentRealization.lean` (`instAvail_unitary_fixes_ones`), `StructuralClosure.lean` (the monomial substratum
class), `KInfFoundations.lean` (`ball3Drive`, `ElementaryDrivability`), `CompletedOI.lean` / `CarrierGeneralOIPlus.lean`
(`oiPlusMin_iff_qm` and its hypotheses). ROADMAP.md rows K∞-Act, K∞-Drive (:1014–1017).

**Research plan (depth-first).**

- **O1 — the no-go envelope, exact.** State and prove precisely which classes of substratum access are
  monomial-only (permutation classes with readback ⇒ ones-fixing ⇒ no mixer), so that every candidate mechanism
  is tested against a sharp boundary rather than a slogan. Record as FAILED routes the mechanisms the envelope
  kills.
- **O2 — candidate mechanisms for a discrete mixer.** Enumerate, from the substratum's own resources
  (A1–A6, link coupling, ancilla coupling with readback, coarse-graining / time averaging, the completion's
  closure), every mechanism that could induce a non-monomial operation on a visible qubit. For each, build the
  smallest exact finite model, compute the induced operation on the visible state, and test (i) non-monomiality,
  (ii) the H-sandwich witness (P = 1; dephased 1/2) with the available preparations and measurements, (iii) the
  disguise test (does the mechanism's interface already contain the coherence?). Exact arithmetic; one mechanism
  at a time to exhaustion.
- **O3 — Continuous Origin.** Determine which premise supplies a one-parameter family of transitions (the drive)
  on the minimal repertoire: relate to K∞-Act / K∞-Drive and the DRIVE findings; isolate the minimal added content
  and its disguise test; connect to `oiPlusMin_iff_qm`'s hypotheses and state exactly what remains once a drive is
  sourced.
- **O4 — the dependency on the composite action.** The drive that Origin would source is the operation whose
  spectator stability (b) needs (stage 6's A_miss). Record the exact dependency between Origin and the bridge
  thread as a handoff proposal, with the proposition each needs from the other.

**Rules.** Exact arithmetic only; `python3 -I -B`; `.out` / `.err` with the exit marker; decision rules in
headers before the first run; failed runs kept; byte-identical replays; every claim in `RESULTS.md` labelled
CERTIFIED / CONDITIONAL (named item) / CONJECTURE / FAILED / OPEN. No mechanism is accepted whose interface
already contains the coherence it produces (the owner's methodological requirement is the disguise test here).

**Governance.** Write only under `research/origin/` on this branch; never touch `main`, `papers/`, `book/`,
`verification/` or any certification record. Lean work on disposable `dev/origin/<topic>` branches (CI via
`workflow_dispatch`), incorporated here as [D] design modules under `research/origin/lean/` with commit and run
id. Push only to `origin research/origin`. `LOG.md` records every commit's purpose.

**Coordination.** Handoff proposals in `research/origin/handoff-proposals/`; received handoffs in `inbox/`,
acknowledged in `LOG.md` before use. Other threads' branches are not read.
