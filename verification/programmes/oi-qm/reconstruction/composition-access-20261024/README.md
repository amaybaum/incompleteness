# Finite-depth composition and access contract

Research-only checkpoint. See [REPORT.md](REPORT.md) for the self-contained
conditional theorem, its precise application boundaries, and source pins.
It does not establish a native Y reset or full OI/QM equivalence.

Run the bounded exact controls with Python 3.12 or later, standard library only:

```sh
python3 checks.py
python3 -O checks.py
```

Both commands exit zero and reproduce the retained structured `RESULT.json`
exactly. An absent result file is created; an existing mismatching result is
an error. The checks use explicit exceptions, not removable assertions.
The expected verdict is `HOLDS_WITHIN_ABSTRACT_FINITE_CONTROL_SCOPE`, with
12 local cases and 324 policy/initial-state cases. The written induction,
not this bounded enumeration, supports the theorem's finite-depth scope.
