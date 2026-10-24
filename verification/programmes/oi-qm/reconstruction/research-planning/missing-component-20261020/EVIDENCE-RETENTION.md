# Evidence retention for the integration record

Research only. This file records, for each checkpoint in `INTEGRATION.md`, which of the material its review relied on
is held in this repository and which is not (AGENTS §A.42). It does not re-derive or re-review anything. The review
reports in `integration-reviews/` are kept byte for byte (`integration-reviews/SHA256SUMS`) and their verdicts stand
as historical verdicts of their authors.

Two statuses are distinguished:

- **reproducible here**: the code under review, the reviewer's own checkers and their outputs are in this repository,
  so the review's computational checks can be re-run from it;
- **report only**: the review report is retained, but the reviewer's code, the author bundle it replayed, or the
  outputs are not in this repository. Its findings are attributed to the report; they are not re-run here.

The search behind this record covered the trees and histories of every branch of the repository and the
coordinating session's disk, by file name and by the sha256 prefixes the reports give (24 October 2026).

## Per checkpoint

| Checkpoint (`INTEGRATION.md`) | Review | Status | Held here | Not held |
| --- | --- | --- | --- | --- |
| Bounded native instrument | `mc-node9/design/native-instrument/review/REVIEW.md`; `integration-reviews/INTEGRATION-REVIEW-1907963e.md` | reproducible here | `instrument_checks.py` and its output (`mc-node9/design/native-instrument/SHA256SUMS`, 6 entries); the reviewer's `review/indep_*.py`, `coordinator_weight20.py` and outputs (`review/SHA256SUMS`, 14 entries); `run_normal.out`, `run_O.out` | — |
| Selector-record boundary | `integration-reviews/SELECTOR-RECORD-REVIEW.md` | report only | the report | the author bundle `3d18fe9c…` with `selector_checks.py`; the reviewer's `indep.py` and its mutants |
| Native selected-sign readout | `integration-reviews/NATIVE-SELECTOR-REVIEW.md` | report only | the report | the author bundle `c204e6f6…` (`checks.py`, `selector.py`, `native_checks.py`, `law_checks.py`, `relay.py`, `layout.py`, `transport_layout.py`, `checks.out`); the reviewer's `mine/` checkers (`run_bundle.py`, `dump_sources.py`, `algebra.py`, `sim.py`, `frontier_sim.py`, `geometry.py`, `laws.py`, `xplane.py`), their outputs, `t185_sources.json` and the mutants. One file of the bundle, `compiler.py`, has the sha256 prefix the report gives and is held on #910 as `native-y-continuation-20261024/parallel_v3/direct_reset/compiler.py` |
| Read-and-reset boundary | `integration-reviews/READ-RESET-REVIEW.md` | report only | the report | the author bundle `15af0674…` and its checkers and `checks.out`; the reviewer's `mine/` checkers (`exactlp.py`, `masks.py`, `relay_geom.py`, `relay_sim.py`, `run_bundle.py`), their outputs and the mutants m1–m11 |
| Native X read-and-reset | external review `2a51fe2a…` | report only (external) | — | the bundle `529185bb…` and the external review text |
| Combined handoff | internal; replays by the coordinating session | report only | — | the bundle `88f80567…`; the replay outputs `combined-review/replay.out` that `INTEGRATION-REVIEW-1907963e.md` cites |
| Native-Y continuation | internal; replays by the coordinating session | report only | — | the bundle `977e8e33…`; the replay outputs `native-y-review/replay.out` |
| Native-Y (#910) | #910's retained reviews | reproducible on #910 | — (held on #910, see `INTEGRATION.md`) | — |

## What this means for `INTEGRATION.md`

- The numerical findings of the selector-record, native-selector and read-and-reset reviews (for example the 7/30
  bound for input-independent random permutations) are stated in `INTEGRATION.md` as those reports' findings. No
  replay of them from retained material has been performed.
- The replay statements for the combined handoff and the native-Y continuation are the coordinating session's
  reports; their outputs are not retained.
- A later resolution is one of: the original author bundles, reviewer code and outputs are recovered, verified
  against the digests above and retained; or the affected checks are re-derived under a new, separately dated and
  retained trail, which is then recorded as such and not as the original.
