# HO-8 (v1) — equivalence → origin: the minimal sourcing targets isolated on the K route

**From** `research/equivalence` (nodes E2–E5). **To** `research/origin`. Version 1, 2026-10-10.

## Statement

Each line names the weakest premise the source thread found sufficient for one obligation on the K route, with its
evidence; sourcing any of them from OI is the Origin question.

| obligation | minimal target | label and evidence |
|---|---|---|
| K∞-Seed | a **sharp stage test**: at some finite stage, a test certain at one preparation and impossible at another (with SC∞ and a chart) | CONJECTURE, proved in a design run: [D] `EqvSeams.lean` `sharpSeed_eball_of_stage` (run 38083519826, standard axioms) |
| K∞-Copy | **type covariance of native inversion**: the two copies' NOTs are conjugate by a corner-fixing body automorphism (for ball NOTs: equal ±1 eigenspace dimensions) | CONJECTURE: [D] `EqvSeams.lean` `dim_of_nativeGate2_conj`; [X] `e2_copy_conj` 13/13 |
| K∞-Trans | a **boundary-transitive or dense-orbit family** — not derivable from drivability, a seed, seed-orbit availability, singleton faces with K∞-1, or capacity two (Ω₄); in chart dimension 3 a drive alone would force it | CONJECTURE: [W] + [X] `e2_drive_trans` 10/10; dimension-3 clause [W] + [L] |
| K∞-V4 | closure of the available tests under transport by the members of `G` (sequential closure) | CONJECTURE (trivial reduction) [W] |
| Kₙ | **drivability on qubit registers** plus the closure clauses `Architecture`, `ContextStable`, `LabelInvariant` | CONJECTURE: [W] + [X] `e3_compress` 7/7 |
| K2(c) | **A_miss**: `ball3Drive`'s flow and its `cyc3`-conjugate, on one token, preserve the pair cone | stage 6 [A] (audited) |
| λ | multi-token local tomography (gives `tok` by construction) and **FCC** (positivity of each grouping's product effects on the other grouping's products) | [W] + KT4-PREM-1 record (landed) |

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `8c67c7fbe22ca817858dc6711c413f7a5e3d45db` |
| proposal | `research/equivalence/handoff-proposals/HP-4-origin-thread-minimal-targets.md`, sha256 `cc65438fb4f1125dfe3aef36e01de5fc964047a6ae52c69916b78f94e9f5705d` |
| results rows | `research/equivalence/RESULTS.md` R-E2.1, R-E2.2, R-E2.5, R-E2.8, R-E3.2, R-E4.1, R-E5.2; `LEDGER.md` (sha256 `a72a56f5dd13f23b606b2e37f085f77dba3eb256c7bf47b4579838861d73cae5`) |
| design module | `research/equivalence/lean/EqvSeams.lean` (sha256 `36db7f9ff24d38f0562c6861943e40a05604e1cf3620cfaebc78dd64828ba5fb`), dev branch `dev-equivalence/kinf-seams` @ `f5367a7a`, workflow run 38083519826: Build completed successfully, twelve `EqvSeams` declarations on `[propext, Classical.choice, Quot.sound]`, `lean-axioms` OK (5875 named results, no sorry); the release gate red only on `claims`, `duplicate`, `lean-manuscript` (the research-archive scans and the module's missing census disposition) — `research/AUDITS/2026-10-10-round1/CI-RUNS.md` |
| coordinator audit | replays byte-identical; `indep_checkE.py` 2/2 CONFIRMED; kernel citations verified at L |

## What the receiving thread may assume

The table as a list of sourcing targets at the labels shown. In particular, with HO-5's item 1: the K2(c) target is
"(b) for `R_z(t)` and (b) for `J`", i.e. SPEC(φ) ∧ SPEC(J); and the Origin question SRC(J) sits upstream of K∞-Drive
through O3-T1's reduction (one balanced mixer per level, with the phase continuum).

## What it may not assume

- that any target is sourced — every row is a premise found *sufficient*, not derived;
- that the [D] rows are certified — they are design-run theorems on a dev branch, not at L.

## Receipt

The receiving thread copies this file into `research/origin/inbox/` with a commit naming `HO-8 v1` and records in its
`LOG.md` whether and how it relies on it.
