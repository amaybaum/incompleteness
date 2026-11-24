# Ledger and terminology verification tool: records (unreviewed drafts)

Status: implementation of design v5.5.9 (sha256
cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9), adopted by the owner on 2026-11-24 as an amendment of
the adopted v5.5.8 and of the frozen v5.5.3. **Every record in this directory is an
unreviewed draft.** None has an independent review record or an owner authorization record, and no freeze `F` exists.
The tool authority record `A` (`tools/ledger_coverage/authority.json`), the empty freeze ledger at the path `A` names
and the acceptance workflow whose content hash `A` pins are not part of this landing: each lands later, `A` first and
the empty freeze ledger in its own merge after it, approved under "Owner at creation" (design sec. 6.3 and sec. 15
item 0a). Until `A` is on `main`, every chain run refuses. A configuration is admitted
only inside a host job of the pinned workflow, from `F`'s pin table and the owner's designation of `F` (design
sec. 6.3); every other run is refused with ERROR `CONFIG_UNREVIEWED` (exit 65). The real-tree controls run
through the control harness, which writes `control-result.json` with `"harness": true`; a harness result is
evidence about the implementation and is never acceptable.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This directory decides no
scientific question and no row disposition.

## Files

| Path | Kind | What it holds |
|---|---|---|
| `controls.json` | A1 control set | the preregistered A1 controls with the design's expected outcomes, and the control-only inputs (DR-3's witness `AGENTS.md` at `H`) |
| `delegation-draft.json` | `oi-delegation/1` | a draft of the delegation contract; the contract itself belongs in the amended plan's record directory at `F` |
| `rules/dr-deny-v1.json` | `oi-term-rules/2` | deny rules DR-1 (a, b, c), DR-3, DR-4, DR-5 with examples and real-tree countercontrols |
| `rules/resid-v1.json` | `oi-term-rules/2` | the review pattern `resid` (resid-a, resid-b, resid-c) |
| `rules/w1-w2-allow-v1.json` | `oi-term-rules/2` | the seed allow rules W1 (four sentences) and W2 (two sentences), fingerprinted at T1' |
| `records/gr58-hit-classification-v1.json` | `oi-hit-classification/1` | the classification of papers/GR.md:58 at T1' |
| `records/repo-scope-v1.json` | `oi-scope/1` | the scope of the `repo` profile (item 11) |
| `rules/register-infinity-params-v1.json` | `oi-term-rules/2` | the per-edit parameters of items 5 and 6 that are not extractable assignments of the plan's checker (kind `params`), linted against that checker |
| `records/side-change-classes-v1.json` | `oi-side-change-classes/1` | the class `tool-landing` only: every path this tool's landing adds, each with its exact blob |

The A1 configuration `retirement-config.json` (`oi-retirement-config/1`) is not part of this landing. It
belongs in the retirement plan's record directory, `verification/audits/foundations/a1exit-deletion-20261121/`,
frozen with the plan at `F` with its review and authorization (design sec. 16.2), and it pins the class record
above; the class record pins every other path of this landing. Until then it exists only as an unreviewed,
unauthorized draft outside the repository, and the A1 controls read it with `--staged-config`.

The empty freeze ledger carries the fields `schema` (`"oi-freeze-ledger/1"`) and `events` (`[]`) and no other: the
ledger is append-only, and a change to any field other than `events` refuses (design sec. 6.3), so any further field
would be fixed for every later version.

## Host reads

On the host, the history of `A` and of the freeze ledger is read from `main`'s first-parent chain: the chain is
followed through the host's commit listing of `main` (which is not filtered by path), and each commit's blob of the
path is compared with its first parent's, merge commits included. The host's path-filtered commit listing is not
used: it omits a merge commit whose path equals its second parent's, which is how a pull-request merge lands a file.
The reads are bounded; a listing that ends before the root commit, a truncated tree, a host error, a reached bound or
bytes that differ from their tree entry refuse admission (ERROR `CONFIG_UNREVIEWED`).

## Comments in governed threads

No automated comment whose first line begins with `oi-` is posted in the authority thread or in a plan thread that `A`
lists; every form comment (`oi-freeze/`, `oi-authority/`, `oi-freeze-ledger/`) is posted by the owner by hand (owner
decision, `amaybaum`, 2026-11-24). The host attributes comments written through the owner's credentials to the
owner's numeric id, so the tool cannot tell them from the owner's own, and one owner comment whose first line begins
with such a prefix but does not match a form exactly, or that is ever edited, makes every admission in that thread
refuse (design sec. 6.3, admission point 3).

## Limitations (stated, not closed)

The tool verifies coverage and provenance. It does not establish complete semantic detection, and a PASS
says nothing about the meaning of any replacement text (design sec. 1).

- Deny rules close only forms with a fixed lexical anchor. Paraphrases without one are, at best, REVIEW
  through `resid`, and only for the classes design sec. 1 lists.
- Accepted residuals that PASS when added (design sec. 15 items 2 and 3), each kept as a control with that
  expected outcome: "the framework's sixth structural property, finiteness of the bijection" (V4); "The
  framework's sixth structural property is finiteness of the substratum" (V27); "the substratum's sixth axiom,
  finiteness" is REVIEW only (V15); "the six posits of the substratum", "six assumptions about the
  substratum", "The posit ledger lists fourteen.", "the fourteen-item posit ledger" and "$A_1$–$A_6$" match no
  deny rule and no `resid` alternative. The original literal item-7 check misses each of them too.
- Context rules and S0 indicators are preregistered heuristics. Rule fingerprints recognize identical text
  only. The tool checks that role fields differ and that a quoted authorization exists, not who wrote them.

## Reproduction

From the repository root, inside a host job of the pinned workflow, with a designated freeze F whose pin table lists the configuration, its review and its authorization:

    python3 -I -B tools/ledger_coverage.py coverage --config F:PATH --freeze F --plan PLAN --round ROUND --commit REV --out DIR

The control runs:

    python3 -I -B tools/ledger_coverage.py self-test --out DIR
    python3 -I -B tools/ledger_coverage/adapters/synthetic_fixture.py DIR .
    python3 -I -B tools/ledger_coverage/adapters/conformance_controls.py DIR
With `CFG=HEAD:verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json` and `STAGED` the
staged draft (the runners read it into an in-memory stand-in for `F`, `HEAD`'s tree plus that file at its plan
path):

    python3 -I -B tools/ledger_coverage/adapters/staged_purity_lint.py --repo . --config $CFG --staged-config STAGED --out DIR
    python3 -I -B tools/ledger_coverage/adapters/a1_conformance.py --repo . --config $CFG --staged-config STAGED --out DIR
    python3 -I -B tools/ledger_coverage/adapters/a1_controls.py --repo . --config $CFG --staged-config STAGED --main MAIN --out DIR

`MAIN` is the `main` commit against which the sequencing safeguard (design sec. 13.4, control RT-L2) predicts `main`
plus this landing; the runner exits with status 2 without it.

## References to commits not on `main`

The A1 controls (`a1_conformance.py`, `a1_controls.py`, `controls.json`) and the draft A1 records in `rules/` and
`records/` read the frozen plan `P` (4c79be642ca631573f06b444903be75ec4f5e2b6) and the trial candidate `T1'`
(14ac71b4b0a0c0aa2d7068d6799a73f474097060), neither of which is reachable from `main`. Every result of those controls,
and every fingerprint or extraction those records take at `P` or `T1'`, is provenance only: no claim made from
`main` rests on it until the content it reads is on `main`. The engine, the synthetic controls and the conformance
controls (`self-test`, `synthetic_fixture.py`, `conformance_controls.py`) read no commit outside their own fixtures.
