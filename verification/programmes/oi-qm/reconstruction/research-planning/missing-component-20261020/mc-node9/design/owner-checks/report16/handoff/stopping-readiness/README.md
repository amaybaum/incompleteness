# Bounded stopping-time readiness handoff v1

Read REPORT.md, then inspect stopping_checks.py before running:

    python3 -I stopping_checks.py
    python3 -I -O stopping_checks.py

Both should reproduce stopping_checks.out byte for byte. Standard library only;
no network or file writes by the checker. Requirements use explicit exceptions,
not assert statements. SHA256SUMS covers this README, report, checker and output.

This is a new exploratory continuation of the carrier handoff reviewed in
report15 at 709bebe8. It does not change the earlier handoff or its claims.
All rule and readiness definitions used here are restated in REPORT.md.

Earlier archive provenance:

* OI_rule_census_handoff_v1.zip:
  8705f2b267734cd3baf81a6d05d791106364a940979df9bbf43878ef81feeead
* OI_joint_readiness_handoff_v1.zip:
  72ab080972b8124a575ada927f16a452c084f0c02abd9a7964499e0ccb04b576
* OI_carrier_compatibility_handoff_v1.zip:
  14a2242c5ff83df4b2e39790f4fea985ac41e06ca31ffaf3fab14851ea069e36

The earlier archives are not dependencies of this checker.
