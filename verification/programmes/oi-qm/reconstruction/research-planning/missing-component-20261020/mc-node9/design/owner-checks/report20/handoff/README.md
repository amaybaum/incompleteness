# Read-only independent review of 43400ea7

Start with `REVIEW.md`. The `source/` directory contains the unchanged files
retrieved at the exact reviewed commit. Its original checksum manifest remains
unchanged. No repository files were edited and no external messages posted.

Replay the source checker (NumPy required):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 source/composition_checks.py
PYTHONDONTWRITEBYTECODE=1 python3 -O source/composition_checks.py
```

Both outputs must match `source/composition_checks.out`. This review's separate
implementations need only the standard library and the included builder:

```sh
python3 independent_checks.py
python3 -O independent_checks.py
```

Both must match `independent_checks.out`. The checker writes only stdout and
explicitly disables bytecode-cache writes. `SHA256SUMS` covers the complete
handoff, except itself. The verified original manifests remain in `source/`.
