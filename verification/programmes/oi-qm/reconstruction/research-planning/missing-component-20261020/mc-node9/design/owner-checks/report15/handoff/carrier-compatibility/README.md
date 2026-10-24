# Conditional carrier/source/detector compatibility

Read REPORT.md first for the common readiness event, full record law and scope.
This is a read-only exploratory handoff, not a quantum-equivalence verdict.

Python 3.10+, standard library only:

```sh
sha256sum -c SHA256SUMS
python3 carrier_checks.py > replay.out
cmp carrier_checks.out replay.out
python3 -O carrier_checks.py > optimized.out
cmp carrier_checks.out optimized.out
```

The checker has no randomness, file writes or network calls; shell redirection
writes stdout. Explicit checks stay active under -O. The manifest covers this
README, REPORT.md, checker and expected output, not itself or the ZIP.

No repository files or external research records were changed.
