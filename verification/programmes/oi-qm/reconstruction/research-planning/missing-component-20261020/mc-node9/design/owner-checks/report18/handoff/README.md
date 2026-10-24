# Nonlinear frontier handoff v1

Read REPORT.md and inspect frontier_checks.py before execution:

    python3 -I frontier_checks.py
    python3 -I -O frontier_checks.py

Both should reproduce frontier_checks.out byte-for-byte. Standard library only,
stdout only, no network. Checks use explicit exceptions, not assert statements.
SHA256SUMS covers the report, checker, output and this README.

This candidate changes the three-field update. It does not supersede the
accepted obstruction for the old rule. All definitions are self-contained.
