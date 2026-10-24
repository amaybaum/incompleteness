# Detector-boundary diagnostic v1

Read REPORT.md first. This exploratory handoff corrects the scope of review13,
supplies an all-transverse-frame exact-clock witness, and checks specific
linear/nonlinear detector boundaries. It does not construct or accept a native
OI apparatus, and it does not reopen C-SPH-1.

Python 3.9+; standard library only:

```sh
sha256sum -c SHA256SUMS
python3 detector_boundary_checks.py > replay.out
cmp detector_boundary_checks.out replay.out
```

The checker has no file writes, randomness or network calls. The shell
redirection above writes stdout. Checks remain enabled under python3 -O.
Successful cmp is silent. The manifest covers this README, the report,
checker and expected output, excluding itself and the enclosing zip.

No repository edits, commits, comments, pushes, or workflow launches were made.
