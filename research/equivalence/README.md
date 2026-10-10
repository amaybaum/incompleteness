# research/equivalence — the remaining OI–QM equivalence obligations

**Question.** Which obligations still separate the certified finite OI→QM characterization from a full OI–QM
equivalence with the quantum kinematics in the conclusion rather than the premises, what exactly blocks each, and
which can be discharged — singly or together — by theorems at L or by a named new premise whose status is honest?

**Starting checkpoint.** Branch `research/equivalence` from commit `4dc0321c` (= L `9f9f8257` +
`research/archive/`). The authoritative obligation list is `verification/ROADMAP.md` at L: the queue rows P0
(dynamical selection, two-part), P1 (Lemma 24.1 semigroup transfer; A6; physical C4; H-Bell; **K** — K1
CONDITIONAL, K2 OPEN, K∞ OPEN with eight seams K∞-Stage / Act / Drive / Trans / Seed / V4 / Copy / Geom, Kₙ OPEN;
the stochastic observer interface; H-∞), and the K-programme section (:980–1050). Read with it:
`research/archive/k-infinity/K-INF-DESIGN.md` (§15 standing table), `…/k2d/K2-LEDGER.md`, `…/sa/SA-LEDGER.md`,
`…/k2c/K2C-LEDGER.md`, `…/kn/KN-CENSUS-RESULT.md`, `…/eqreview/HINF-REVIEW.md` (H-∞ is not the availability
question; Level III is a uniqueness, not an iff), `…/eqreview/EQ2-SYNTHESIS.md`, `…/eq5/F/ASSUMPTIONS.md` (λ:
`hcl` cannot be dropped, `hgate` not necessary; `tok` unsourced), `…/eqreview/EQ5-SOURCE-AUDIT.md` (the
architecture supplies neither `TokenCoherent` nor the KT(4) inequalities), `…/opact/RESULT.md`, `…/drive/RESULT.md`,
`…/pt/INTEGRATION-NOTE-STAGE6.md` §1 (NO-MEET: the bridges each obligation would supply) and §6.

**Research plan (depth-first on the chain, one obligation to exhaustion before the next).**

- **E1 — the obligation ledger.** One row per obligation: exact statement at L (kernel object, file:line),
  status, the blocking premise or missing theorem, what it unlocks, its dependencies on the other obligations and
  on the bridge / origin / countermodels threads, and the candidate theorem statement that would discharge it.
  This ledger is the thread's standing deliverable (`LEDGER.md`), updated with every node.
- **E2 — the K∞ seams.** For each seam, decide whether a theorem at L (or a small design module) discharges it
  from the others or from a named weaker premise: K∞-Seed is discharged on the completion
  (`sharpSeed_completion`); K∞-Trans is not implied by K∞-Drive (`not_boundaryTransitive_flow`); K∞-Copy has a
  candidate weakening (the frame-preserving conjugacy class of the native inversion determined by system type:
  ROADMAP.md:1027–1029, untested). Run the exact probes named there; record each outcome.
- **E3 — Kₙ.** The lift from the elementary `d = 3` system to the complex matrix carriers of every finite size
  with their repertoire: state the obstruction exactly (the Kₙ census: no ball→carrier theorem, K2 composes
  elementary systems only, carrier generality in types) and the smallest theorem that would move it.
- **E4 — K2 and its interface to the composite action.** K2's clauses (local tomography, the composite cone,
  local actions compatible with it, the composition theorem, the antiunitary / complete-positivity bridge): which
  are now settled by stages 3–6 at the pair level (the cone is not forced; the local-action clause is (b) itself),
  which remain, and what the thread can state as a theorem schema conditional on A_miss.
- **E5 — λ's sourcing and the three-token structure.** No structure with three or more tokens exists at L; state
  what a three-token carrier would need to be, whether `tok` can be sourced from it, and whether the KT(4) route
  (design-run `kt4_forward_ie1`) can be re-derived at L.
- **E6 — H-Bell, H-∞, Level III.** Bound each exactly: what is proved, what is the scope gap, what statement at L
  would be scope-correct (H-∞: finite carriers only; Level III: uniqueness, not iff).
- **E7 — round readiness.** For each obligation, say whether a governed round could be preregistered now (a
  theorem statement with a predicted outcome and controls), and draft the preregistration skeleton for those that
  can — without creating any control plane, PR or round.

**Rules.** Exact arithmetic for probes; `python3 -I -B`; `.out` / `.err` with the exit marker; decision rules in
headers before the first run; failed runs kept; byte-identical replays; every claim in `RESULTS.md` and
`LEDGER.md` labelled CERTIFIED / CONDITIONAL (named item) / CONJECTURE / FAILED / OPEN. Claims about the kernel
cite file:line at L; a theorem's statement is quoted, not paraphrased, where a status depends on it.

**Governance.** Write only under `research/equivalence/` on this branch; never touch `main`, `papers/`, `book/`,
`verification/` or any certification record. Lean work on disposable `dev/equivalence/<topic>` branches (CI via
`workflow_dispatch`), incorporated here as [D] design modules under `research/equivalence/lean/` with commit and
run id. Push only to `origin research/equivalence`. `LOG.md` records every commit's purpose.

**Coordination.** Handoff proposals in `research/equivalence/handoff-proposals/`; received handoffs in `inbox/`,
acknowledged in `LOG.md` before use. Other threads' branches are not read.
