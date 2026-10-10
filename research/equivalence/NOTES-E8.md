# NOTES-E8 — preregistration drafts S1–S4: what each would add, license and leave unsourced, and what is measured

Base L = `9f9f8257`. **Nothing here is a control plane, a preregistration or a round.** The four files under
`preregistration-drafts/` are research drafts for owner review in the native V3 format (AGENTS.md §A.39): one
`v3-round` block and one `v3-governed-paths` block each, frozen decision rules whose tokens `controls.py verdict E`
prints from measurements, an earned reading and a non-inference rule, an invariant→checkpoint table (§A.41), controls
with mutations, and predicted outputs generated from design runs measured at L. Their template is the landed native
rounds' preregistrations (KTRANS-DENSE-1, KT4-PREM-1). No `D` is designated, no pull request exists, and nothing under
`verification/` is written on this branch.

Evidence: [D] design runs on `dev-equivalence/*` branches based on L; [X] exact probes in `experiments/`; [W] the
drafts' written arguments; [A] archive records; [K] kernel at L.

**Productivity test (§A.31, fixed before the node).** A finding counts only if a draft's predicted output is generated
from a measurement taken at L and either (a) a kernel statement compiles standalone in the module the round would land,
or (b) the draft exposes a gap or hazard that would void a round run on it.

## 1. The four drafts

| draft | round | module | cells | design evidence | premise not sourced | ROADMAP wording it would license (HP-1; not applied) | ready |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | KINF-SEED-1 | `StageSeed`: three theorems, `sharpSeed_eball_of_stage` and its two existence forms | Q-SEED | runs 38083519826 (inside `EqvSeams`) and 38091534622 (standalone): build green, three prints standard | the sharp stage test (`h1`, `h0`), SC∞, the chart, K∞-Trans in either form | K∞-Seed (:1023–1024): the seed is carried to the ball along the chart and the ball's identification; its remaining content is the stage-level sharp test | for owner review |
| S2 | KINF-COPY-1 | `CopyCovariance`: §B–§D of `EqvSeams` and the swapped-gate control, twelve prints | Q-RED, Q-POS, Q-EXACT (`e2_copy_conj`, 13 checks) | runs 38083519826 and 38091534622: build green, twelve prints standard | type covariance itself (`hcov` with `hgz`, `hgΩ`, `hhΩ`) and every DIM-1 premise | K∞-Copy (:1027–1030): the weakening to type covariance of native inversion, under which DIM-1's selector applies (`dim_of_nativeGate2_conj`); not HP-1's eigenspace phrase, which rests on a written argument; hazard C6 travels with it | for owner review |
| S3 | KN-DESC-1 | `KnDescent`: twelve declarations from `EqvKnDesc` | Q-DESC, Q-IFF (one witness per direction, §A.34), Q-EXACT (`e3_compress`, 7 checks) | run 38090116254: build green, twelve prints standard, release gate red only at `lean-manuscript` | drivability at the qubit-power carriers (`hpow`) and every closure clause | Kₙ (:1058–1069): inside the K3 interfaces carrier-general drivability reduces to the carriers `Fin (2^k)` (`drivesElementary_of_pow`); "No current theorem supplies the lift" stays | for owner review; one pre-`F` revision item (unused binders, warnings only) |
| S4 | KTRANS-SEP-1 | `TransSeparation`: the body Ω₄ and the separation, fifteen prints | Q-NONELL, Q-SEP, Q-EXACT (`e8_ktrans_probe`, 12 checks) | run 38090924005: build failed at two terms; `not_affine_eball_omega4` and seven other declarations standard; repair `95beab2b` unmeasured | boundary transitivity and its dense form; none of drivability, seed, strict convexity or symmetry for any OI object | K∞-Trans (:1018–1022): on a general body the other single-system seams do not give transitivity (`kinfTrans_separation`); "and supporting-effect completeness" better omitted (§3) | **no**: checkpoint `C0`, a design run of the repaired module, precedes any `F` |

Under every outcome of every draft the obligation stays OPEN, and no draft edits the ROADMAP, a manuscript, a landed
module or another round's record. The positive control of S4 is landed at every dimension:
`boundaryTransitive_fullAut` (EffectSpace.lean:337).

## 2. Dispatches and what they measured

Three dispatches, the cap, at most one per draft:

| dispatch | draft | commit (branch) | run | Mathlib bridge job: steps |
| --- | --- | --- | --- | --- |
| 1 | S3 | `05b5756c` (`dev-equivalence/kn-desc`) | 38090116254 | 114324651733: Build success; release gate red at `lean-manuscript` only (no census family, by construction on a dev branch) |
| 2 | S4 | `195dfbee` (`dev-equivalence/omega4`) | 38090924005 | 114327010280: Build failure (`EqvOmega4.lean:157`, `:215`); gate skipped |
| 3 | S1, S2 (and E9's `EqvLevel3`) | `8c92343e` (`dev-equivalence/split-l3`) | 38091534622 | 114328799399: Build success; release gate red at `lean-manuscript` only |

Each dev branch is based on L and adds, besides its modules, one import line to `verification/lean-mathlib/OIBridge.lean`
(outside `OIBridge/`), because the bridge builds only modules imported from the root — the round-1 deviation, logged
again. S4's one dispatch was spent on the failing tree, so its proof-only repair is unmeasured.

## 3. S4's exact layer, measured (`experiments/e8_ktrans_probe.py`)

The draft's Q-EXACT rule required a check W5 (supporting-effect completeness for the full effects) that had not been
written, so its `checks:` count was a design target. The probe the round would freeze now exists and is measured. It
carries `e2_drive_trans`'s D1–D9 and C1 with their code unchanged (verified line for line), and adds:

- **W5**: the Euler identity `∇F(p)·p = 4F(p)` and the gradient gap of `F` as an explicit sum of squares,
  `F(y) − F(p) − ∇F(p)·(y − p) = (|y_x|² − |p_x|²)² + 2|p_x|²|y_x − p_x|² + (y_s − p_s)²((y_s + p_s)² + 2p_s²)`,
  identically in eight variables; the effect `e_p = (1 + ∇F(p)·y/4)/2` is `1` at `p` and `0` at `−p` at nine rational
  and two irrational boundary points; on 1669 exact grid states the nine rational `e_p` lie in `[0, 1]`. With the written
  step (the boundary states of Ω₄ in the sense of `IsBoundaryState`, KInfFoundations.lean:130, are the points with
  `F = 1`; the identity gives `∇F(p)·y = F(y) + 3 − gap ≤ 4` on Ω₄; central symmetry gives `e_p ≥ 0`), every boundary
  state is certain for a proper full effect: `SupportingEffectComplete Ω₄ (fullEffects Ω₄)`
  (KInfFoundations.lean:135, :149).
- **C2**: the ball's identities (gap `|y − p|²`), the form of `supportingEffectComplete_ball3` (KInfFoundations.lean:1053).
- **XW1, XW2** (countercontrols): the sum of squares without its middle term is not an identity; at the irrational
  boundary point `p₁ = (√15/5, 0, 0, 2√5/5)` the Euclidean-normal functional is certain at `p₁` and exceeds `1` at the
  state `(21/25, 0, 0, 21/25)`, the sign of `(3/25)(√15 + 2√5) − 1` decided in rationals (`3888/15625 > 3844/15625`).

Run 1 (decision rule fixed in the header first): 12 checks, 0 failures, both countercontrols fail as stated,
`VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS`; replay byte-identical. S4's rule, design table and predicted outputs now
quote this measurement.

**Pressure test of the favourable reading.** With the full effects, supporting-effect completeness holds on every
compact convex body in finite dimension (a nontrivial supporting hyperplane at every relative-boundary point, rescaled
into `[0, 1]` by compactness [L]); the archive already records it (`research/archive/threads/A/RESULT.md`, and
`research/archive/threads/F/LEDGER.md` row B8, the kernel candidate `supportingEffectComplete_fullEffects`, with
countercontrols showing compactness and finite dimension load-bearing [A]). W5 therefore gives Ω₄'s supporting effect
in closed form and says nothing about an available effect family, which is where K∞-1 has content
(`not_kInf1_ball3_unit`, KInfFoundations.lean:1089). For the wording: listing "supporting-effect completeness" among
Ω₄'s properties adds no information, so S4 now advises omitting HP-1's phrase.

## 4. Classification (§A.31)

- **POSITIVE**: the S1 and S2 modules compile standalone over L with no statement changed ([D]); the Kₙ descent of S3
  is kernel-checked in a design run, with the iff's two directions witnessed separately ([D]); S4's decisive step
  `not_affine_eball_omega4` built with standard axioms ([D]).
- **Gaps exposed** (each would have voided a round frozen as first drafted): S4's tree failed to build at two terms,
  so a round frozen on it would have halted — now checkpoint `C0`; S4's exact rule required an unwritten check — now
  measured (§3).
- **CONFIRMING**: W5 (§3).
- No NEW finding in the §A.31 sense: E8 is closure-mode packaging of round-1 results into round form. Every predicted
  output is generated from a measurement except S4's Q-SEP, which waits on `C0`.

## 5. Not decided here

Whether any round is opened (owner); `C0` for S4; S3's pre-`F` revision item (owner's choice); whether S1 and S2 run as
one round (they share a base and a dispatch, not a module); and, for every draft, the predicted execution tree at a
designated `D` — the census family, `controls.py` and the probe shard — which each draft lists as not yet measured.
