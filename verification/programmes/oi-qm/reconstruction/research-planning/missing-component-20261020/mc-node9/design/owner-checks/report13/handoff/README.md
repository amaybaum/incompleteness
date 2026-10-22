# Joint-record diagnostic v1

Read REPORT.md first. This exploratory handoff confirms the attempt-count leak
and gives a new joint clock/read witness in a modified, station-oriented source
whose herald laws agree exactly. It is not a native OI detector implementation
or a C-SPH-1 acceptance run.

Python 3.9+; standard library only:

```sh
sha256sum -c SHA256SUMS
python3 joint_record_checks.py > replay.out
cmp joint_record_checks.out replay.out
```

Successful cmp is silent. The checker has no file writes, network access, or
randomness. The shell redirection above writes stdout. Checks remain enabled
under python3 -O. Decimal output summarizes exact rational calculations.

No repository writes, comments, pushes, or workflow launches were made.
The manifest excludes itself and the enclosing archive; archive timestamps
are fixed for reproducible packaging.
