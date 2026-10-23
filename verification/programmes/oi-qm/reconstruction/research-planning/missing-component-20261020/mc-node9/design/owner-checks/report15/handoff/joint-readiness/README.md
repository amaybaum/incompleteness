# Joint readiness and detector reuse

Read REPORT.md for the exact ensemble, observation scope, proofs and limitations.
This is a read-only exploratory handoff, not an OI/QM equivalence acceptance.

Python 3.10+; standard library only:

```sh
sha256sum -c SHA256SUMS
python3 joint_readiness_checks.py > replay.out
cmp joint_readiness_checks.out replay.out
python3 -O joint_readiness_checks.py > optimized.out
cmp joint_readiness_checks.out optimized.out
```

The checker itself performs no file writes or network calls and uses no
randomness. The shell redirects stdout. Explicit checks remain active under
-O. SHA256SUMS covers the report, README, checker and expected stdout, excluding
the manifest itself and the enclosing ZIP. No compiled code is needed.

No repository edits, commits, comments, pushes or workflow launches were made.
