# Ledger and terminology verification tool: records (unreviewed drafts)

Status: implementation of the frozen design v5.5.2 (sha256
835ff356200349db7689ea41ce936349015fb70f47b35a508945d681a8604323). **Every record in this directory is an
unreviewed draft**, and so is the tool authority record `tools/ledger_coverage/authority.json`. None has an
independent review record or an owner authorization record, and no freeze `F` exists. A configuration is admitted
only inside a host job of the pinned workflow, from `F`'s pin table and the owner's designation of `F` (design
sec. 6.3); every other run is refused with ERROR `CONFIG_UNREVIEWED` (exit 65). The real-tree controls run
through the control harness, which writes `control-result.json` with `"harness": true`; a harness result is
evidence about the implementation and is never acceptable.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This directory decides no
scientific question and no row disposition.

## Files

| Path | Kind | What it holds |
|---|---|---|
| `a1exit-retirement-config.json` | `oi-retirement-config/1` | the A1 configuration: roles, adapters pinned by blob, profiles with their source blobs and pattern hashes, checks, context mapping, indicators, splitter, HP obligation, delegation, records, controls |
| `controls.json` | A1 control set | the preregistered A1 controls with the design's expected outcomes, and the control-only inputs (DR-3's witness `AGENTS.md` at `H`) |
| `delegation-draft.json` | `oi-delegation/1` | a draft of the delegation contract; the contract itself belongs in the amended plan's record directory at `F` |
| `rules/dr-deny-v1.json` | `oi-term-rules/2` | deny rules DR-1 (a, b, c), DR-3, DR-4, DR-5 with examples and real-tree countercontrols |
| `rules/resid-v1.json` | `oi-term-rules/2` | the review pattern `resid` (resid-a, resid-b, resid-c) |
| `rules/w1-w2-allow-v1.json` | `oi-term-rules/2` | the seed allow rules W1 (four sentences) and W2 (two sentences), fingerprinted at T1' |
| `records/gr58-hit-classification-v1.json` | `oi-hit-classification/1` | the classification of papers/GR.md:58 at T1' |
| `records/repo-scope-v1.json` | `oi-scope/1` | the scope of the `repo` profile (item 11) |
| `rules/register-infinity-params-v1.json` | `oi-term-rules/2` | the per-edit parameters of items 5 and 6 that are not extractable assignments of the plan's checker (kind `params`), linted against that checker |
| `records/side-change-classes-v1.json` | `oi-side-change-classes/1` | the class `tool-landing` only: every path this tool's landing adds, each with its exact blob |
| `freeze/freeze-ledger.json` | `oi-freeze-ledger/1` | the empty freeze ledger (it lands on `main` with the authority record) |
| `workflow-draft/ledger-coverage.yml` | workflow | the one workflow whose runs may produce an acceptable result; its content hash is pinned in the authority record under `.github/workflows/ledger-coverage.yml`, where it must land unchanged |

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
    python3 -I -B tools/ledger_coverage/adapters/a1_conformance.py --repo . --config HEAD:verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json --out DIR
    python3 -I -B tools/ledger_coverage/adapters/a1_controls.py --repo . --config HEAD:verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json --out DIR
