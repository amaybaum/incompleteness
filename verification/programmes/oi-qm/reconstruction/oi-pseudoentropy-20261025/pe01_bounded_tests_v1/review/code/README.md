# Independent review of the PE-01 code

These are the records of the independent code review of PE-01 for dispatch readiness. They are retained as evidence
only: they review the code and its controls, and they compute no PE-01 result. The independent review of PE-01's
results will go in `../`, as the plan's §11 states. The plan-review records are in `../plan/`.

`REVIEW.md` is the reviewer's record with both addenda. `mine/` holds the reviewer's independent scripts and the one
check output that the findings cite. Each file is byte-identical to the reviewer's own, except for the three redactions
listed below, at the sha256 values in `SHA256SUMS`. The reviewer's smoke outputs, mutant copies and scratch clone are
not retained.

| Head reviewed | Record | Verdict |
|---|---|---|
| `0f1391cd470ec5c8513de05ced1bad3c61050c08` | `REVIEW.md` | BLOCK (narrowly), R1–R10 and nits N1–N12 |
| `df280443791abcdbe15c957cc843ae47379b7c09` | `REVIEW.md`, Addendum | BLOCK (narrowly), R11 and nits N13–N16 |
| `07f3c127f55c48e74c15d06a344a91894da4c41a` | `REVIEW.md`, Addendum 2 | ACCEPT WITH NITS for dispatch, conditional on A2, its pin, R10 and owner approval; nits N17–N18 |

**Working paths.** The records name the reviewer's working directories:
- `<scratch>/revpe01code/` is this directory, for `REVIEW.md` and `mine/`.
- `revpe01code/repo/` was a clone of the repository at the head under review. `SRC` in the two mutant harnesses is the
  PE-01 package inside it.
- `revpe01code/mut/` and `revpe01code/mut2r/` were the mutated package copies the harnesses write. `smoke_out/`,
  `smoke2_out/`, `smoke.sh` and `smoke2.sh` were the reviewer's smoke runs. None is retained.
- `mine/driver.py` and `mine/driver2.py` are written by `mine/mutants.py` and `mine/mutants2.py` on every run. They are
  retained as the harnesses last wrote them.

**Which finding each script supports.**

| Script | Supports |
|---|---|
| `mine/brute.py` | the exactness control on adv^pred, the window counts and the D-SIGN counts |
| `mine/brute_k0.py` | the deterministic K0, worst and average, at m = 1 |
| `mine/m3check.py` | the completeness of the m = 3 canonical forms |
| `mine/lincheck.py` | the per-observer linear-filter reduction |
| `mine/resultpath.py` | the result-mode n3-clk family shard run at `0f1391cd` |
| `mine/mutants.py`, `mine/driver.py` | the mutant table at `0f1391cd` |
| `mine/mutants2.py`, `mine/driver2.py` | the mutant tables of both addenda |
| `mine/b3wcheck.py`, `mine/b3w.out` | the independent check of the B3 window average and R11 |
| `mine/bench.py`, `mine/bench3.py`, `mine/benchlp.py` | the cost measurements |

Each script takes the PE-01 package directory as its first argument, for example
`python3 -I -B mine/brute.py <package dir>`. The two harnesses read their working directory from `ROOT`, which must be
set to a scratch directory holding `repo/` before they run.

**Redactions.** Each removes the absolute path of the reviewer's session scratch directory and puts `<scratch>` in its
place. Nothing else in these files differs from the reviewer's copies.

| File | Where | sha256 of the reviewer's copy | sha256 of the retained copy |
|---|---|---|---|
| `REVIEW.md` | line 384 | `8fa5363f0ee32fbc2b5a96ee85be534d0665c372507a8e225d5bdef661ef975b` | `e79589f1dacd7fb7d1b0ec8422dd3a3178b827aaeca77c2e722d36f762c5a90b` |
| `mine/mutants.py` | line 3 (`ROOT`) | `7f0e8a22b9636da47903ef3448626868e9a3c4e8a098529da900f53681b4caf7` | `d6bb6e2a54015003f74e7ee12c60969486082a10f99bd552b015d7ae6697bbba` |
| `mine/mutants2.py` | line 3 (`ROOT`) | `703182640751e63bf454d4103b1f90f62c4d86ed5a271c140fa7ecc98f4d5159` | `809cfcd8da9fca8efa8088ad8b49043132d617960bbee28fcccb3d0a0b779504` |

The files were scanned for local absolute paths, tokens, keys, signed URLs, e-mail addresses and IP addresses before
they were committed. These three paths were the only hits.
