# Ledger and terminology verification tool: records (unreviewed drafts)

Status: Stage 1 implementation of the accepted design (DESIGN v5.1, sha256
0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe). **Every record in this directory is an
unreviewed draft.** None has an independent review record or an owner authorization record, and no freeze `F`
exists. Under the review chain the tool therefore refuses the configuration with ERROR `CONFIG_UNREVIEWED`
(exit 65). The real-tree controls run through the control harness of
`tools/ledger_coverage/adapters/a1_controls.py`, which admits the draft configuration without its chain and
states that in every result. A harness result is evidence about the implementation, never an acceptance of a
check of the retirement plan.

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
| `records/side-change-classes-v1.json` | `oi-side-change-classes/1` | side-change classes: the trial workflow and this tool's landing paths |

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

From the repository root, with a configuration admitted under its chain (not yet possible for these drafts):

    python3 -I -B tools/ledger_coverage.py coverage --config REV:verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json --config-sha256 SHA --commit REV --out DIR

The control runs of Stage 1:

    python3 -I -B tools/ledger_coverage.py self-test --out DIR
    python3 -I -B tools/ledger_coverage/adapters/synthetic_fixture.py DIR .
    python3 -I -B tools/ledger_coverage/adapters/a1_controls.py --repo . --config HEAD:verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json --out DIR
