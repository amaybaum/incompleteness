# Emission-map diagnostic v1

Research handoff, 2026-10-22. Read REPORT.md first: the candidate is conditional
and its exact-time interface fails the stated preparation-equivalence witness.
This is not a C-SPH-1 rerun or a numerical acceptance test.

Python 3.9+; standard library only. From the extracted directory:

```sh
sha256sum -c SHA256SUMS
python3 emission_map_checks.py > replay.out
cmp emission_map_checks.out replay.out
```

Successful `cmp` is silent. The checker uses explicit failure exceptions, so
`python3 -O emission_map_checks.py` retains the checks. It has no file writes,
network access or randomness; the replay redirection above writes only stdout.

The manifest covers REPORT.md, this README, the checker and expected output.
It excludes itself and the enclosing zip. Archive timestamps are fixed for
reproducible packaging. No repository writes, comments or dispatches were made.
