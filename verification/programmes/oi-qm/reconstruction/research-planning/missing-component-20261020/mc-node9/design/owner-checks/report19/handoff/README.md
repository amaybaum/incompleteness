# OI finite aggregation components, v1

Read REPORT.md first. This package supplies exact four-, five- and six-input AND components under the fixed report18 nonlinear rule. It makes no scalable/all-size construction claim.

Files:
- REPORT.md: layouts, resource counts, full-record interface, proofs and limitations.
- aggregation_checks.py: standard-library checker; stdout only, reads RECORDS.json.
- RECORDS.json: complete nonzero device-record ANF tables; omitted cells in the specified record region are zero.
- aggregation_checks.out: expected deterministic output.
- SHA256SUMS: hashes of the other files.

Run from the extracted directory using Python 3.10 or later:

    python -I aggregation_checks.py
    python -I -O aggregation_checks.py

Compare stdout byte for byte with aggregation_checks.out. No third-party packages are needed. Dense full-torus updates cover every input for two seeded backgrounds per size; exhaustive source-frontier checks use exact shrinking causal cones. Joint independence is justified by disjoint dependencies, not a brute-force enumeration of the Cartesian product. No repository modifications are required.
