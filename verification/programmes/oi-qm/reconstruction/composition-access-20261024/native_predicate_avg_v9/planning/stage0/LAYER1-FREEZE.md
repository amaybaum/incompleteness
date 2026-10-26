# NP-AVG-1 Stage 0: Layer 1 freeze

Layer 1 of Stage 0, the scientific specification of the two-layer freeze (owner decision O1), is frozen at commit
`f33d8d63a14b3bbaa3c1eb1e52aeffcb55b0c966` on PR #935. That is the exact commit the independent r4→r5 re-check
reviewed.

## Authorization

The owner (amaybaum), 2026-10-26: "complete the independent r4→r5 review. If it gives a clean acceptance, freeze r5 at
the reviewed SHA. Retain the freeze evidence and test results. Bring back the full enumeration proposal as a separate
authorization decision. No authorization for full enumeration or v8 execution yet."

The re-check's verdict is ACCEPT, with no required changes (`../review/STAGE0-RECHECK-r5.md`).

## The frozen object

Paths are relative to this directory. The values are read at `f33d8d63`.

| object | identifier |
|---|---|
| `r5/STAGE0-PLAN-r5.md` (the Layer-1 specification) | SHA-256 `1a30188e70804644a6ff65b3114ab82f8be40a2b056d0e2862ce595a8982847e` |
| `r5/STAGE0-CHANGES-r5.md` | SHA-256 `247859ac1579a2825e56cac3af9d968b0c71b5f196ce8050349e67bca3fd1a00` |
| `r5/` | git tree `6ea1d9b0cef22953b80a428073a85a293b31b75b` |
| `code-r5/` (design-evidence code) | git tree `81c2869b666d7e1d816afcad1807709064bf0e29` |
| `design-r5/` (design evidence, `RUN-MANIFEST`, retained outputs) | git tree `e097af20e334830e06acde6294643709304a7bd2` |

The plan's stated base condition holds: `fc452ea825b986a3babab5d110626e0019c39847` is an ancestor of `f33d8d63`.

Layer 1 fixes the masking law, the geometry, the equivalence rules, the search domain, the invariants and the
acceptance criteria, as stated in the plan. Nothing in the files above changes after this freeze. A change is an
append-only amendment, with its own independent review.

## Test results retained

- **The design evidence at `f33d8d63`,** in `design-r5/`:
  - the control suite, S6, the symmetry check, the planted families, the small exact references and the radius
    mutants;
  - the quick mutant campaign, in which all 17 mutants are killed at their named case;
  - the v8 refusal check, which refuses 36 of 36 attempts.
  
  `RUN-MANIFEST.json` lists the code and output hashes.
- **The independent replay** (`../review/STAGE0-RECHECK-r5.md` §1). Every output replays byte for byte against
  `design-r5/runs/`, and every deterministic step is also identical under `python3 -O`. The manifest's code and output
  hashes match. The replay outputs are not retained a second time, because they are byte-identical to the retained
  runs.
- **The reviewer's own probes,** in `../review/toy-r5/`:
  - `frame_adjacent`: the frozen rule gives 7/7 and 12/12; the reviewer's G mutant gives 0/7 and 0/12;
  - `guard_probe`: refuses 15 of 15, including the five r4 bypasses;
  - `guard_probe2`: new bypass attempts, each refused.
- **PR CI on `f33d8d63`:** run 40332489760, with every job green and one matrix placeholder skipped. It is a
  pull-request run, testing a synthetic merge, and is supporting evidence only.

Nothing ran on v8's configuration class. v8 setups were only constructed, to check they are refused.

## Not frozen, and not authorized

- **Layer 2.** The production enumerator, the controls, the configuration hashes and the execution certificate are
  finalized only after this freeze, and then reviewed in their own right (plan §5b).
- **The v8 enumeration, its workflow and any dispatch.** None is authorized. The full enumeration proposal, including
  the S7 CI budget and the full mutant campaign in CI, goes to the owner as a separate authorization decision.
- **Rule T's L_A = L_G = 0 consequence** is frozen at the conservative default the plan states: the geometric fact
  only, with no law statement for k > 2. It awaits owner confirmation. A law statement would need a new proof
  obligation generalising PO8, and so an amendment.
