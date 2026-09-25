# Verifier round V3-9 — V3 made operable for provisional pilots: RESULT

Executed from the certified execution base and from nothing else, under `AGENTS.md` §A.37: the
control plane #739, then the execution pull request, which also carries the landing.

- **`D`** — `311f06ea174501587478024a09140297b56e089a`.
- **`B`** — `d27daf20abc92450a925c64e98040b9b15f5ca05`, the merge of #739. Its parents are `D` and
  the reviewed control-plane head `1c9567206fe70eb716050e0674e4ac5b4f7134c7`, and its tree is that
  head's. Push run 36092411567 was green on all six jobs, the control-plane base check in mode `B`
  with 13 rows and 3 frozen blobs.
- **Preregistration** — blob `3b9956e0c2f6335b0bdfda02695edaec9da54559` at `B` and at `E`.
- **Shape** — non-sealing, `E` → `L`, no `P`: no guard clause, manifest record or round
  certificate (reading `R8`).
- **Status** — COMPLETE: every target reached its passing outcome. For `V39-3` the
  repository-wide conditions (the guard, `V2`, the release gate) are established by the exact-head
  run on `E`, which the `E` certification record identifies; they were not run locally.

| target | outcome | predicted |
|---|---|---|
| `V39-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `V39-1` | `BUILDER-INSTALLED`; builder blob `e08d15f6` | the same, strong |
| `V39-2` | `PILOT-RULE-INSTALLED`; `AGENTS.md` blob `864494c1`, `architecture.md` blob `f699471b` | the same, strong |
| `V39-3` | `AUTHORITY-UNCHANGED` | `AUTHORITY-UNCHANGED`, strong |
| `V39-4` | `SCOPE-HELD` | `SCOPE-HELD`, strong |

Every blob is the predicted one, so no stage diverges from the frozen text, and there is no
divergence for the owner's review. The controls show that the builder reproduces the receipts the
conformance vectors commit and that the verifier rejects each corrupted field class; they are not
evidence that the specification is right (hazard `H1`).

`tools/v3_receipt.py` builds a V3 receipt from a round's exact object ids and the host's attestation
records. `AGENTS.md` §A.39 lets a round the owner authorizes as a provisional V3 pilot run the
native lifecycle; every other round, this one included, runs under §A.37. `V1` and `V2` remain
authoritative, and no receipt has been written.

***

## `V39-0` — the base: BASE-HOLDS

The execution branch was created at exactly `B`, after `B`'s push run was green, with `main` still
at `B` and the checkout not shallow. At `B` the preregistration's blob is the frozen `3b9956e0`, and
`AGENTS.md`, `architecture.md` and `tools/v3_verifier.py` have the frozen blobs `a9687b39`,
`db36dbd1` and `ccfbe813`. The control-plane base check in mode `B` holds at `B`: 13 rows and 3
frozen blobs, no failure. At `B` the corpus held 135 vectors, and neither `tools/v3_receipt.py`,
`verification/receipts/` nor `verification/v3-seals/` existed.

***

## `V39-1` — the builder: BUILDER-INSTALLED

Stage 1, commit `d14b57842ff68a4cbe1573e0f5b2dcf219cd9637`, whose only parent is `B`. The frozen
builder text, read back from the preregistration as it stands at `B`, was written to
`tools/v3_receipt.py`.

- **Builder blob:** `e08d15f6e301bec4d32f9dab34b5c7b40fb48d1f`, the predicted one.
- **`C1`:** `tools/v3_receipt.py --self-test` exits 0, ending `v3_receipt: self-test OK`, with the
  counts the freeze records: 29 receipt commits rebuilt, each identical to the committed receipt and
  holding; the shapes complete non-sealing 24, complete sealing 2, halted with execution commits 2,
  halted without 1, more than one reconciliation 7; and every corruption failing wherever the
  receipt has the field — 29 of 29 for each class except `tree_e` and the execution delta digest
  (26 of 26) and the seal blob (2 of 2).
- **`C2`:** each of the six scratch copies with one derivation wrong exits 1, ending
  `v3_receipt: self-test FAILED`: the execution delta from `D` (26 `FAIL` lines); the landing base
  from the second parent (29); the control-plane blobs in reverse order (4); no `withdrawal` reason
  without execution commits (1); the seal blob without git's object header (2); every attestation
  on `F` (26).
- **`C3`:** `--status complete --d HEAD --f HEAD` prints
  `v3_receipt: refused (input:not-an-object-id)` and exits 2; no argument prints the usage line and
  exits 2.
- **`C4`:** `tools/v3_verifier.py` has its `D` blob; `--corpus` reports
  `CORPUS  135 vector(s), exact and as expected`; `--self-test` passes.

The commit adds `tools/v3_receipt.py`, and nothing else.

***

## `V39-2` — the rule and the preamble: PILOT-RULE-INSTALLED

Stage 2, commit `43fc30877d1eed14b200387459a2264b93ff9e74`, whose only parent is `d14b5784`. The
frozen `§A.39` text was appended to `AGENTS.md` after its last byte, and the frozen sentence
replaced the preamble sentence of `architecture.md`, both read back from the preregistration at
`B`.

- **`AGENTS.md` blob:** `864494c1a9696a3b08330da64cf9d265d6d8b92f`, the predicted one.
- **`architecture.md` blob:** `f699471b34d4f332c557f6b5452c952db49a0306`, the predicted one.
- **`C5`:** `AGENTS.md` is its `B` bytes followed by the frozen text exactly, with one
  `## §A.39 ` heading and no `§A.38`; `architecture.md` differs from its `B` bytes by the frozen
  sentence alone and no longer contains `is not operative`.
- **`C4`:** as at stage 1.

The commit changes `AGENTS.md` and `architecture.md`, and nothing else.

The scripts that ran the stages and the rehearsal, none of which is landed:

| script | SHA-256 |
|---|---|
| `exec39.py` (applies one stage's frozen text, read back from the preregistration at `B`, and runs that stage's checkpoint) | `8670548ca830ef844fb078ced5148f657bac94951bf75d115ee413dd9c1c7014` |
| `sim39.py` (the drafting-time simulation behind `F5`) | `de48273cefabb8d88d54173d44a2c676903e852eca3342ef4aff56b42e6d613f` |

***

## `V39-3` — authority: AUTHORITY-UNCHANGED

At `E`, `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`,
`verification/lean/edge_rigidity_probe.py`, `tools/v3_verifier.py` and the preregistration have
their `B` blobs, and nothing under `verification/infrastructure/v3/conformance/`,
`verification/seals/` or `verification/certificates/` changed. Neither `verification/receipts/` nor
`verification/v3-seals/` exists, and no gate, job or required check invokes the builder.

The guard's verdict (105 PASS, 0 FAIL, with `D`'s verdict map), `V2` authoritative OK, the release
gate's 19 of 19 steps and the shadow job's self-test and 135-vector corpus at `E` are taken from the
exact-head run on `E`, not run locally.

***

## `V39-4` — scope: SCOPE-HELD

`git diff --no-renames --name-status B E`:

| status | path |
|---|---|
| `M` | `AGENTS.md` |
| `A` | `tools/v3_receipt.py` |
| `M` | `verification/infrastructure/v3/architecture.md` |
| `A` | `verification/infrastructure/round-v3-9-operationalization/result.md` |

This is exactly the mutation budget: 2 modified, 2 added. Nothing on the budget's never-written list
changes.

***

## Discrepancies

None against the freeze.

***

## Chronology

The execution's commits after `B` are three: the builder (`d14b5784`), the rule and the preamble
(`43fc3087`), and this note, which is `E`. Each has exactly one parent, the first `B`. None changes
the preregistration, and the branch absorbed no later `main`. Stage commits were pushed without
waiting for continuous integration on them. Nothing has been merged.
