# Native readiness flag boundary v1

Inspect REPORT.md and flag_checks.py before running:

    python3 -I flag_checks.py
    python3 -I -O flag_checks.py

Both reproduce flag_checks.out byte-for-byte. Requirements use exceptions
rather than assert. No network or file writes by the checker. SHA256SUMS covers
this README, REPORT.md, flag_checks.py and flag_checks.out.

This exploratory continuation follows report16 at 280cf250, but imports no
code or data from that report. It supplies a conditional prepared-prior lemma
and a restricted single-raw-flag obstruction, not an unrestricted detector,
clock, OI no-go, or quantum-equivalence verdict.
