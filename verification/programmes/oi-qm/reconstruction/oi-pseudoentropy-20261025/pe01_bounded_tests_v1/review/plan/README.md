# Independent review of the PE-01 stage plan

These are the review records of `../../PLAN.md`, from its first version to revision 4. The check of revision 5 and of
amendment A1 is `PRECHECK-A1.md`; its last nit, N-d, is applied in `1e025b67`. The files are byte-identical to
the reviewer's own, at the sha256 values in `SHA256SUMS`. They review the plan only. The independent review of PE-01's
results will go in `../`, as the plan's §11 states.

| Plan commit | Record | Verdict |
|---|---|---|
| `aa667c13` (first version) | `REVIEW.md` | BLOCK (narrowly), R1–R5 |
| `6e5db447` (revision 1) | `REVIEW.md`, addendum | BLOCK (narrowly), S1–S5 |
| `67a5cbe1` (revision 2) | `RECHECK-67a5cbe1.md` | BLOCK (narrowly), admissible-region floor and attribution rule |
| `fee98794` (revision 3) | `RECHECK-fee98794.md` | ACCEPT WITH NITS, N1–N5 |
| `1cbfba61` (revision 4) | `RECHECK-fee98794.md`, addendum | ACCEPT WITH NITS, N6 |
| `af38dc2d` (revision 5) and `ced675cc` (A1) | `PRECHECK-A1.md` | BLOCK (narrowly), P1–P2 |
| `7b8ca727` (A1, revised) | `PRECHECK-A1.md`, addendum | ACCEPT WITH NITS, N-d and N-e |

Revision 5 (`af38dc2d`) applies N6 and rewraps lines. It changes no other words, as a whitespace-insensitive word diff
of `1cbfba61..af38dc2d` shows. The owner's three open decisions are fixed in `../../amendments/A1-owner-decisions.md`.

**Working paths.** The records name the reviewer's working directories:
- `revpe01/` is this directory.
- `revpe01/PLAN-<sha>.md` is `PLAN.md` at that commit (`git show <sha>:<path>`). The sha256 values of the two copies
  the re-checks hashed match the committed blobs: `ca82998a…37f4` at `67a5cbe1` and `85169310…cf24` at `fee98794`.

**Design checks.** These scripts check the plan's control facts and its drafting-time tables only. They compute no
PE-01 measurement, and the AR checkpoint re-derives the tables at run time. Each was replayed, and its output is
byte-identical to the retained `.out`. Commands, from this directory:

```sh
python3 -I -B checks.py > checks.out
python3 -I -B checks_emb.py ./checks.py > checks_emb.out
python3 -I -B checks2.py ./checks.py > checks2.out
python3 -I -B checks3.py ./checks.py > checks3.out
git show fee98794:verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe01_bounded_tests_v1/PLAN.md > PLAN-fee98794.md
python3 -I -B checks4.py . PLAN-fee98794.md > checks4.out
```
