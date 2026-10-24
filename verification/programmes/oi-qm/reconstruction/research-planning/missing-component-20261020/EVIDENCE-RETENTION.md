# Evidence retention for the integration record

Research only. This file records, for each checkpoint in `INTEGRATION.md`, which of the material its review relied on
is held in this repository and which is not (AGENTS §A.42). It does not re-derive or re-review anything. The review
reports in `integration-reviews/` are kept byte for byte (`integration-reviews/SHA256SUMS`) and their verdicts stand
as historical verdicts of their authors.

Three levels are kept apart: *evidence retained* (a structured result is in this repository), *computation
reproducible* (the checker and its inputs can regenerate that result) and *independently verified* (a separate
implementation or proof has checked the claim). The statuses, the same as in `INTEGRATION.md`:

- **reproducible here**: the code under review, the reviewer's own checkers and their outputs are in this repository,
  so the review's computational checks can be re-run from it;
- **author reproduced**: the author bundle with the cited sha256, held outside this repository, replays its checker
  byte for byte against its recorded output; the structured result is in `author-replays/AUTHOR-REPLAYS.json`. The
  computation is reproducible from that bundle, not from this repository, and the replay is not an independent
  verification;
- **reviewer evidence missing**: the independent review's own computations (its checkers, mutants and sources) are
  not retained, so its findings are attributed to its report;
- **on #910**: the material, with #910's own retained reviews and checkers, is held on #910's branch.

The search behind this record covered the trees and histories of every branch of the repository and the
coordinating session's disk, by file name and by the sha256 prefixes the reports give (24 October 2026). The six author
bundles were then recovered from the owner's file library as byte-identical originals (each matches the sha256 cited
in `INTEGRATION.md`; `977e8e33…` contains the other five) and replayed (Python 3.13.16); they are held outside this
repository. `author-replays/AUTHOR-REPLAYS.json` (sha256 in `author-replays/SHA256SUMS`) records, per bundle, the
checker and its sha256, the recorded output and its sha256, the invocation, the observed digests and every output
line.

## Per checkpoint

| Checkpoint (`INTEGRATION.md`) | Review | Status | Held here | Not held |
| --- | --- | --- | --- | --- |
| Bounded native instrument | `mc-node9/design/native-instrument/review/REVIEW.md`; `integration-reviews/INTEGRATION-REVIEW-1907963e.md` | reproducible here (`review/indep_degree_qm.py` needs SymPy) | `instrument_checks.py` and its output (`mc-node9/design/native-instrument/SHA256SUMS`, 6 entries); the reviewer's `review/indep_*.py`, `coordinator_weight20.py` and outputs (`review/SHA256SUMS`, 14 entries); `run_normal.out`, `run_O.out` | — |
| Selector-record boundary | `integration-reviews/SELECTOR-RECORD-REVIEW.md` | author reproduced; reviewer evidence missing | the report; the structured replay of `selector_checks.py` (normal and `-O`, byte-identical to `selector_checks.out`) | the author bundle `3d18fe9c…` (outside the repository); the reviewer's `indep.py`; the mutated copies of the author's checker that the review ran |
| Native selected-sign readout | `integration-reviews/NATIVE-SELECTOR-REVIEW.md` | author reproduced; reviewer evidence missing | the report; the structured replay of `checks.py` (normal and `-O`, byte-identical to `checks.out`) | the author bundle `c204e6f6…`, outside the repository (`checks.py`, `selector.py`, `native_checks.py`, `law_checks.py`, `relay.py`, `layout.py`, `transport_layout.py`, `checks.out`); the reviewer's `mine/` checkers (`run_bundle.py`, `dump_sources.py`, `algebra.py`, `sim.py`, `frontier_sim.py`, `geometry.py`, `laws.py`, `xplane.py`), their outputs, `t185_sources.json` and the mutants. One file of the bundle, `compiler.py`, has the sha256 prefix the report gives and is held on #910 as `native-y-continuation-20261024/parallel_v3/direct_reset/compiler.py` |
| Read-and-reset boundary | `integration-reviews/READ-RESET-REVIEW.md` | author reproduced; reviewer evidence missing | the report; the structured replay of `checks.py` (normal and `-O`, byte-identical to `checks.out`) | the author bundle `15af0674…` (outside the repository); the reviewer's `mine/` checkers (`exactlp.py`, `masks.py`, `relay_geom.py`, `relay_sim.py`, `run_bundle.py`), their outputs and the mutants m1–m11 |
| Native X read-and-reset | external review `2a51fe2a…` | author reproduced; external review and spotchecker held outside this repository, spotchecker replayed within its arithmetic scope | the structured replays of `checks.py` (normal and `-O`) and of the external spotchecker (normal; it relies on `assert`), each byte-identical to its recorded output, with the spotchecker's scope | the bundle `529185bb…` and the external review text and spotchecker (held in `88f80567…`), outside the repository |
| Combined handoff | internal; replays by the coordinating session | author reproduced; replay outputs not retained | the structured replay of the bundle's own driver `replay.py` in its default mode, byte-identical to `verification/combined_exact.out` (the native-X suite is replayed in the native-X row) (per #910's provenance records, #910 holds `compiler.py` from this bundle; see the native-selector row) | the bundle `88f80567…`; the replay outputs `combined-review/replay.out` that `INTEGRATION-REVIEW-1907963e.md` cites |
| Native-Y continuation | internal; replays by the coordinating session | author reproduced; replay outputs not retained | the structured replay of the bundle's own driver `run_replays.py`, byte-identical to `verification/COMBINED-REPLAY.out` (per #910's provenance records, #910 holds `native-y-continuation-20261024/continuation/core.py` byte for byte from this bundle) | the bundle `977e8e33…`; the replay outputs `native-y-review/replay.out` |
| Native-Y (#910) | #910's retained reviews | on #910 | — (held on #910, see `INTEGRATION.md`) | — |

## What this means for `INTEGRATION.md`

- The author checkers of the six identified bundles, and of the transfer bundle `4a232a48…` nested in them,
  reproduce their recorded outputs byte for byte; the drivers of the combined and native-Y bundles replay the
  selected checks they name. That is evidence of what the author checkers report, not an independent verification.
- The transfer bundle's checkers bear on open obligation 1 (the transport theorem), which they do not discharge; their
  replay is the last record of `author-replays/AUTHOR-REPLAYS.json`.
- The numerical findings of the selector-record, native-selector and read-and-reset reviews (for example the 7/30
  bound for input-independent random permutations and the dual-certified LP results) are those reports' findings; the
  reviewers' own computations are not retained, and no replay of them has been performed.
- The native-X external review is held with the combined bundle; its spotchecker imports no author code and replays
  byte for byte. It checks the kernel arithmetic of a stipulated 5:4:1 herald table, success 5/16, and the two-herald
  mass products; not that the native herald realizes the table, nor the native transport, which rests on open
  obligation 1. The acceptance stays the external reviewer's, within its
  stated scope.
- The coordinating session's replay outputs for the combined handoff and the native-Y continuation are not retained;
  the bundles' own replay drivers reproduce their recorded outputs.
- A later resolution is one of: the original author bundles, reviewer code and outputs are recovered, verified
  against the digests above and retained; or the affected checks are re-derived under a new, separately dated and
  retained trail, which is then recorded as such and not as the original.
