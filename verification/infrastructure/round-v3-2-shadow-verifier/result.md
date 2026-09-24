# Verifier round V3-2 — the V3 shadow verifier: RESULT

Executed on #727 from the owner-designated freeze anchor and from nothing else, under the
single-pull-request lifecycle the preregistration states as an owner-directed exception to §A.37.

- **`F` (freeze anchor)** — `e15dc06b697eefdf37f2c8b23f81d32201956dd4`, designated by the owner in
  #727's record. Its sole parent is `022e670d125bfa4b4c232613b41d3e48a2ab6339`, and it changes only
  the preregistration, whose blob at `F` is `22e26adad2865d31c75962a597c0a52a840284ff`. Exact-head
  run 35953350133 was green on all five jobs.
- **Drafting commits** — `8a40cfd62178ec1e9b1ea195dd94d1668cd312f0` and
  `022e670d125bfa4b4c232613b41d3e48a2ab6339`, superseded drafts.
- **`D`** — `9c480626ba0b3d6242bb99783356afefaf4f4bcf`.
- **Shape** — non-sealing, no `P`: no guard clause, manifest record, round certificate or
  attestation (reading `R1`).
- **Status** — COMPLETE: every target reached a passing outcome.

| target | outcome | predicted |
|---|---|---|
| `V32-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `V32-1` | `IMPLEMENTED` | `IMPLEMENTED`, strong |
| `V32-2` | `COMMIT-LOCAL` | `COMMIT-LOCAL`, strong |
| `V32-3` | `CONFORMANCE-EXACT` | `CONFORMANCE-EXACT`, moderate |
| `V32-4` | `CONTROLS-FIRE` | `CONTROLS-FIRE`, moderate |
| `V32-5` | `CENSUS-AGREES` | `CENSUS-AGREES`, strong |
| `V32-6` | `PERTURBATION-INVARIANT` | `PERTURBATION-INVARIANT`, strong |
| `V32-7` | `SPEC-GAPS-RECORDED` | `SPEC-GAPS-RECORDED`, weak |
| `V32-8` | `SHADOW-ONLY` | `SHADOW-ONLY`, strong |
| `V32-9` | `SCOPE-HELD` | `SCOPE-HELD`, strong |

`CENSUS-AGREES` is an agreement finding, not a proof of correctness: two implementations can share an
error, and this census would not detect it.

The shadow verifier is `tools/v3_verifier.py`, and it gates nothing. `V1` and `V2` remain
authoritative. V3 is not operative.

***

## `V32-0` — the base: BASE-HOLDS

The checkout was exactly `F` before any execution object existed. `F`'s parent is `022e670d`, `F`
changes only the preregistration, and the preregistration's blob at `F` is the one the designation
records. Every row of the preconditions block holds at `F` in mode `M` (11 rows), and the
control-plane base check and lint self-tests pass.

***

## `V32-1` — the implementation: IMPLEMENTED

`tools/v3_verifier.py` (blob `2c34d4d7f1adadc4bdecbad94ff8eadb7b30f974`) imports only `hashlib`,
`json`, `os`, `re`, `subprocess`, `sys` and `tempfile`. It has exactly the frozen entry points and no
authoritative mode: `--mode authoritative` is refused with the usage line. `HEAD`, a ref name and an
abbreviated id are refused before any repository read. None of the 52 round stems of the `V2`
certificate corpus occurs in its text.

It implements `S7`, `S8`, `S4`, the lifecycle predicates T1, T3, T5, T6 and T7 from `Q`, `S10`'s
publication question, and the projection of the `V2` attestation rows. It applies the `K1`–`K4`
readings and prints them at every shadow run.

***

## `V32-2` — commit-locality: COMMIT-LOCAL

The static scan of the source finds no match for any frozen pattern:

| pattern | matches |
|---|---|
| `GITHUB_` | 0 |
| `refs/remotes` | 0 |
| `refs/pull` | 0 |
| `\borigin\b` | 0 |
| `\bfetch\b` | 0 |
| `ls-remote` | 0 |
| `for-each-ref` | 0 |
| `symbolic-ref` | 0 |
| `show-ref` | 0 |
| `^\s*(import\|from)\s+(urllib\|http\|socket\|time\|datetime)\b` | 0 |

The source reads the process environment once, for `PATH`. Each of its three `subprocess.run` calls
passes an explicit environment built from that value and fixed literals. The shadow's report had one
SHA-256 under `P0`–`P3` and under a hostile environment in which `GITHUB_EVENT_NAME`,
`GITHUB_EVENT_PATH`, `GITHUB_SHA`, `GITHUB_REF`, `GIT_DIR` and `GIT_CONFIG_GLOBAL` were set to
misleading values: `36319c337377b71ed22c834539a27b76ce6b029a495d1a826cc427b3a5e4a557`.

***

## `V32-3` — the corpus: CONFORMANCE-EXACT

`verification/infrastructure/v3/conformance/` holds 84 vectors, executed as an exact set. Every
vector gave its expected verdict in its expected family. The SHA-256 of the corpus files'
bytes, concatenated in path order, is
`1e31a05dd02aae0358e74bcf637c03e9ef0d5bbe957963c06d53491cca8ba1c7`.

The frozen minimum coverage is met:

- **row 1:** G1 in both orders, one digest; G2 and its governance table;
- **row 2:** the fourteen `S7` rejections and the record-class rule;
- **row 3:** the three landed deltas and the scratch delta with LF and `é`, whose bytes are identical
  under `core.quotePath` true and false;
- **row 4:** the four canonical receipts;
- **row 5:** the nine receipt negatives, plus the two `S11` seal presence cases;
- **row 6:** every cell of `MC1`–`MC8`;
- **row 7:** one admitted and one rejected round for each of `K1`–`K4`;
- **row 8:** the three input refusals.

The expected values of rows 1 to 4 are `architecture.md`'s. The repository-built vectors compute
their receipts' digests and object ids with the shadow's own functions, so they test the lifecycle
predicates and not the digest functions. The digest functions are tested by rows 1 to 3 against
values computed outside the shadow.

`MC1`'s countercase is the refusal of a branch name as a commit argument together with the static
scan. `MC5`'s is a round verified from `Q`, then verified again after a later commit and working-tree
edits changed every file it records, with identical output; and a receipt whose recorded
control-plane blob disagrees with the one at `F`.

| vector | settlements | expected | obtained |
|---|---|---|---|
| `g5-reject-halted-execution-not-linear` | `S12`, `S3`, `G5` | FAILS `s12:` | AS-EXPECTED |
| `g6-admit-record-class-by-broader-entry` | `S7`, `G6` | HOLDS | AS-EXPECTED |
| `g6-reject-receipt-shadowed-by-execution-entry` | `S7`, `G6` | FAILS `s7:` | AS-EXPECTED |
| `g7-reject-reconciliation-changes-preregistration` | `S2`, `S9`, `G7` | FAILS `s9:` | AS-EXPECTED |
| `input-refuses-abbreviated-id` | `S1` | REFUSED `input:` | AS-EXPECTED |
| `input-refuses-head` | `S1` | REFUSED `input:` | AS-EXPECTED |
| `input-refuses-ref-name` | `S1` | REFUSED `input:` | AS-EXPECTED |
| `k1-admit-round-block-any-order` | `K1` | HOLDS | AS-EXPECTED |
| `k1-reject-round-block-incomplete` | `K1` | FAILS `t1:` | AS-EXPECTED |
| `k2-admit-blocks-only-in-preregistration` | `K2` | HOLDS | AS-EXPECTED |
| `k2-reject-amendment-repeats-governed-block` | `K2` | FAILS `t1:` | AS-EXPECTED |
| `k3-admit-two-reconciliations` | `K3` | HOLDS | AS-EXPECTED |
| `k3-reject-first-parent-regressed` | `K3` | FAILS `s9:` | AS-EXPECTED |
| `k4-admit-superseded-receipt-commit` | `K4` | HOLDS | AS-EXPECTED |
| `k4-reject-superseded-receipt-commit-changes-more` | `K4` | FAILS `s10:` | AS-EXPECTED |
| `mc1-counter-branch-tip-refused` | `S1`, `MC1` | REFUSED `input:` | AS-EXPECTED |
| `mc1-pass-ref-churn` | `S1`, `MC1` | HOLDS | AS-EXPECTED |
| `mc2-counter-first-parent-off-main` | `S9`, `MC2` | FAILS `s9:` | AS-EXPECTED |
| `mc2-counter-host-merge` | `S10`, `MC2` | FAILS `s10:` | AS-EXPECTED |
| `mc2-pass-base-drift` | `S9`, `S10`, `MC2` | HOLDS | AS-EXPECTED |
| `mc3-counter-ungoverned-path` | `S9`, `MC3` | FAILS `s9:` | AS-EXPECTED |
| `mc3-counter-unlisted-change` | `S9`, `MC3` | FAILS `s9:` | AS-EXPECTED |
| `mc3-pass-resolved-governed-path` | `S9`, `MC3` | HOLDS | AS-EXPECTED |
| `mc4-counter-merge-inside-governed-only` | `S3`, `MC4` | FAILS `s3:` | AS-EXPECTED |
| `mc4-counter-merge-inside` | `S3`, `MC4` | FAILS `s3:` | AS-EXPECTED |
| `mc4-counter-not-from-f` | `S3`, `MC4` | FAILS `s3:` | AS-EXPECTED |
| `mc4-pass-linear` | `S3`, `MC4` | HOLDS | AS-EXPECTED |
| `mc5-counter-recorded-blob-disagrees` | `S6`, `S4`, `MC5` | FAILS `s4:` | AS-EXPECTED |
| `mc5-pass-historical-subject` | `S6`, `MC5` | HOLDS | AS-EXPECTED |
| `mc6-counter-halted-receipt-carries-e` | `S12`, `S4`, `MC6` | FAILS `s4:` | AS-EXPECTED |
| `mc6-counter-landing-publishes-execution-path` | `S12`, `MC6` | FAILS `s12:` | AS-EXPECTED |
| `mc6-counter-withdrawal-leaves-added-file` | `S12`, `MC6` | FAILS `s12:` | AS-EXPECTED |
| `mc6-counter-withdrawal-without-result-note` | `S12`, `MC6` | FAILS `s12:` | AS-EXPECTED |
| `mc6-extra-halted-without-execution-commits` | `S12` | HOLDS | AS-EXPECTED |
| `mc6-pass-halted-with-withdrawal` | `S12`, `MC6` | HOLDS | AS-EXPECTED |
| `mc7-counter-seal-record-missing-from-q` | `S11`, `S10`, `MC7` | FAILS `s10:` | AS-EXPECTED |
| `mc7-pass-non-sealing` | `S11`, `MC7` | HOLDS | AS-EXPECTED |
| `mc7-pass-sealing` | `S11`, `MC7` | HOLDS | AS-EXPECTED |
| `mc8-counter-control-plane-change-after-f` | `S2`, `S3`, `MC8` | FAILS `s3:` | AS-EXPECTED |
| `mc8-counter-execution-not-from-f` | `S2`, `S3`, `MC8` | FAILS `s3:` | AS-EXPECTED |
| `mc8-pass-amendments-before-f` | `S2`, `MC8` | HOLDS | AS-EXPECTED |
| `s10-counter-receipt-commit-changes-more` | `S10` | FAILS `s10:` | AS-EXPECTED |
| `s12-counter-withdrawal-invariant-only` | `S12` | FAILS `s12:` | AS-EXPECTED |
| `s3-counter-unauthorized-execution-change` | `S3`, `S7` | FAILS `s3:` | AS-EXPECTED |
| `s4-absent-field-present-with-reason` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s4-absent-without-reason` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s4-canonical-ex-1` | `S4` | HOLDS | AS-EXPECTED |
| `s4-canonical-ex-2` | `S4` | HOLDS | AS-EXPECTED |
| `s4-canonical-ex-3` | `S4` | HOLDS | AS-EXPECTED |
| `s4-canonical-ex-4` | `S4` | HOLDS | AS-EXPECTED |
| `s4-delta-digest-without-e` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s4-duplicate-key` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s4-forbidden-present` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s4-object-id-width` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s4-required-missing` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s4-seal-in-non-sealing` | `S4`, `S11` | FAILS `s4:` | AS-EXPECTED |
| `s4-seal-missing-from-sealing` | `S4`, `S11` | FAILS `s4:` | AS-EXPECTED |
| `s4-unknown-key` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s4-unknown-reason-code` | `S4` | FAILS `s4:` | AS-EXPECTED |
| `s7-g1-order-a` | `S7` | HOLDS + digest | AS-EXPECTED |
| `s7-g1-order-b` | `S7` | HOLDS + digest | AS-EXPECTED |
| `s7-g2-nested` | `S7` | HOLDS + digest | AS-EXPECTED |
| `s7-reject-dot-segment` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-dotdot-segment` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-double-slash` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-empty-ops` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-empty-path` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-leading-slash` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-no-block` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-ops-order` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-path-cr` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-path-tab` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-path-twice` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-record-class-omits` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-two-blocks` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-two-fields` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s7-reject-unknown-class` | `S7` | FAILS `s7:` | AS-EXPECTED |
| `s8-landed-2c6a4373-56b25397` | `S8` | digest | AS-EXPECTED |
| `s8-landed-d3212b0e-50938dff` | `S8` | digest | AS-EXPECTED |
| `s8-landed-f9a99fdf-14b9d991` | `S8` | digest | AS-EXPECTED |
| `s8-scratch-lf-eacute` | `S8` | digest | AS-EXPECTED |
| `s9-counter-execution-change-dropped` | `S9` | FAILS `s9:` | AS-EXPECTED |
| `s9-counter-landing-adds-governed-path` | `S9` | FAILS `s9:` | AS-EXPECTED |
| `s9-counter-landing-status-unauthorized` | `S9` | FAILS `s9:` | AS-EXPECTED |

***

## `V32-4` — the mutation controls: CONTROLS-FIRE

Each check was disabled in turn in a scratch copy of the tool, never in the tracked file. Each of its
countercases, rejected by the unmutated tool, then verified:

| mutated check | countercase | unmutated | mutated |
|---|---|---|---|
| `S3` linearity | `mc4-counter-merge-inside-governed-only` | FAILS | HOLDS |
| `S7` authorization | `s3-counter-unauthorized-execution-change` | FAILS | HOLDS |
| `S9` condition 1 | `s9-counter-landing-status-unauthorized` | FAILS | HOLDS |
| `S9` condition 2 | `s9-counter-landing-adds-governed-path` | FAILS | HOLDS |
| `S9` condition 3 | `s9-counter-execution-change-dropped` | FAILS | HOLDS |
| `K3` first-parent rule | `k3-reject-first-parent-regressed` | FAILS | HOLDS |
| `S12` withdrawal invariant | `s12-counter-withdrawal-invariant-only` | FAILS | HOLDS |
| `S10`'s `delta(Λ, Q)` rule | `s10-counter-receipt-commit-changes-more` | FAILS | HOLDS |
| `S4` presence rules | `s4-required-missing`, `s4-forbidden-present`, `s4-absent-without-reason`, `s4-absent-field-present-with-reason` | FAILS | HOLDS |

Several countercases of the `MC` table fail two checks at once. Each mutation above was therefore
run against a countercase that fails that check alone; those seven single-check countercases are in
the corpus.

***

## `V32-5` and `V32-6` — the census and the perturbation control: CENSUS-AGREES, PERTURBATION-INVARIANT

`verification/infrastructure/round-v3-2-shadow-verifier/census.json` records the comparison at the
subject `F`. It was produced by a scratch census driver (SHA-256
`4bb982e95103a28688837582aa6ddb610ba95f4f4200a423d34240a510e05a37`), which was not landed. The
driver ran in a clone of `F` whose remote pointed at a path that does not exist. It ran the shadow
(blob `2c34d4d7`) and `V2` (blob `a475408874b850f34c31eca5e1cb4ab549601f38`) under Python 3.11.15
and git 2.43.0.

The subject carries 36 rows: 30 `landed`, compared on `X1`–`X4`, and 6 `base-only`, compared on `X0`.
That makes 126 cells per state.

| state | `V2` result | cells | classes |
|---|---|---|---|
| `P0` | shadow OK | 126 | 126 `AGREE` |
| `P1` | shadow OK | 126 | 126 `AGREE` |
| `P2` | fail-closed, `visibility:base-ref-unresolvable` | 126 | 126 `INPUT` |
| `P3` | 17 failures | 126 | 120 `AGREE`, 6 `INPUT` |

The six `P3` `INPUT` cells are the `X4` cells of `CGR`, `CV1`, `GR1`, `GR2`, `NLV` and `PFR`, where
`V2` reported `landing:zero-candidates`. No cell was `PREDICATE` or `IMPLEMENTATION`, and no row was
malformed. `V2`'s other `P3` failures are certificate-level codes outside the compared families.
The V3-only facts hold for all 30 landed rows: each is linear from its base, and each base lies on
the first-parent chain of its landing's first parent. These facts are information only; they are
not compared.

Across `P0`–`P3` and the hostile environment the shadow's report had one SHA-256,
`36319c337377b71ed22c834539a27b76ce6b029a495d1a826cc427b3a5e4a557`. Its exit status was 0 each time,
and its per-cell verdicts were identical in every state.

***

## `V32-7` — the specification: SPEC-GAPS-RECORDED

`K1`–`K4` are the readings the preregistration froze. Implementation found three further places
where `architecture.md` leaves a verifier a choice. None is a contradiction between settlements.

| gap | where | the shadow's reading | vectors |
|---|---|---|---|
| `G5` | T5 requires `W` to be a single-parent child of "the last" execution commit; `S3`'s linearity is stated for `F..E` only | every execution commit, certified or not, is linear from `F` and changes no control-plane file | `g5-reject-halted-execution-not-linear`, and `mc6-pass-halted-with-withdrawal` |
| `G6` | `S7`: the `record` class "must contain" the record directory and the receipt path | "contain" means governed, by the longest-match rule, by a `record` entry | `g6-admit-record-class-by-broader-entry`, `g6-reject-receipt-shadowed-by-execution-entry` |
| `G7` | `S2` forbids a change to a control-plane file after `F`, but `S9` admits any governed path listed in `resolved_paths`, a record-class control-plane file included | `S2` binds every commit of the round after `F`, reconciliations and receipt commits included | `g7-reject-reconciliation-changes-preregistration` |

The promotion boundary requires a specification round to settle `K1`–`K4` and `G5`–`G7` before any
promotion.

***

## `V32-8` — non-authority: SHADOW-ONLY

At `E`:

- `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard, `AGENTS.md` and
  `verification/infrastructure/v3/architecture.md` have their `F` blobs;
- the workflow's diff from `F` removes no line, and every added line is inside the one new job,
  `V3 shadow verifier`, on which no other job depends;
- the guard gives `ALL CHECKS PASS`, 105 PASS and 0 FAIL, with `D`'s verdict map;
- `V2` is authoritative OK;
- the release gate passes 19 of 19 steps.

No promotion act is present:

- the release gate and the guard do not name the shadow;
- no `verification/receipts/` directory exists;
- `AGENTS.md` is unchanged;
- the shadow has no authoritative mode;
- the host's required-check set was not touched.

***

## `V32-9` — scope: SCOPE-HELD

`git diff --name-status F E`:

| status | path |
|---|---|
| `M` | `.github/workflows/verify.yml` |
| `A` | `tools/v3_verifier.py` |
| `M` | `verification/README.md` |
| `A` | `verification/infrastructure/round-v3-2-shadow-verifier/census.json` |
| `A` | `verification/infrastructure/round-v3-2-shadow-verifier/result.md` |
| `A` | the 84 files of `verification/infrastructure/v3/conformance/` |

Nothing is deleted. Nothing under the budget's never-written list changes.

***

## Discrepancies

- **The `S4` mutation, first run.** The scratch harness's first patch for the `S4` presence rules
  disabled only the required-field branch. Three of the four countercases were therefore still
  rejected by the forbidden-field and absent-with-reason branches, and that run read
  `CONTROL-VOID`. The patch was corrected to disable the whole presence-rule loop, which is the
  control the preregistration names, and all four then fired. The tracked tool and the vectors did
  not change.
- **The shadow after stage 1.** No change was made to `tools/v3_verifier.py` after its stage-1
  commit, so the change rule was never invoked. The `G5`–`G7` readings were implemented before that
  commit.

***

## Chronology

The execution's commits after `F` are five: the shadow, the corpus, the census, the workflow job and
README paragraph, and this note, which is `E`. Each has exactly one parent, the first `F`. None
changes the preregistration, and the branch absorbed no later `main`. Nothing has been merged.
