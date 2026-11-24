# Confirmation review of design v6.0e against v6.0d

Reviewer: independent, non-author. Review only. Nothing was written in the repository or the
worktree, and there was no commit, push, GitHub write, GraphQL call or CI run. No operation was
refused. This review checks only the delta from v6.0d: B-1 and S-1 to S-3 of `review-v6.0d/review.md`.

## Objects verified

| Object | sha256 | Result |
|---|---|---|
| `DESIGN-v6.0e.md` | 4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131 | match |
| `INVENTORY-v6.0e.md` | ce3abd51df3ce12b9ee05accf4eb235869c4745556a73ca7c850db771a2720f0 | match |
| `CHANGES-v6.0e.md` | 44639266d1e6c9f76eb68636bf47804751bdea61092e4a0ca177d9fafbbcd332 | match |
| `CHANGES-v6.0e-from-v6.0d.diff` | f73d9e7171ee120f39f4635921d00ae9c462f445c61475f001a702b138cd4ada | match; byte-identical to the regenerated `diff -u DESIGN-v6.0d.md DESIGN-v6.0e.md` |
| `DESIGN-v6.0d.md` | 1927e1356c7491ff00861e963d43308232e6ee51622ff5916b4f7921d32ef923 | match |
| `CHANGES-v6.0e-from-v5.5.9.diff` | (not given) | its body equals the regenerated diff |

**Recounted.** From v6.0d: 9 hunks, 12 lines removed, 22 added. From v5.5.9: 596 removed, 563
added. Both equal the counts in CHANGES.

## Verdict: ACCEPT-WITH-NITS

There is no blocking finding.

- B-1 is fixed. The rule as v6.0e states it refuses every form in my probe set and passes both
  conforming workflows.
- S-1 to S-3 are applied.
- All 9 hunks map to B-1 or S-1 to S-3, and nothing else changed.

There is one editorial nit, T-1.

## Key question for this delta

*Does any change let an incorrect scientific result pass that v6.0d, v6.0c or v5.5.9 rejected?*

**No.** The changes are of three kinds:

- **B-1 only widens what the line rule refuses.** The rule is stricter than v6.0d's in every case.
- **S-2 adds a refusal item to the workflow checklist.**
- **S-1 and S-3 are text only:** pointers and the quotation.

No acceptance condition, consumer check or control outcome is relaxed. The only row that changes is
EI7, which gains refused cases (`probe/rows-v60d-v60e.txt`: 513 retained, 1 modified, none added
or removed).

## Check 1: hunk map

| # | Change | Source | Verified |
|---|---|---|---|
| 1 | title; v6.0e status bullet | traceability (S-1) | yes |
| 2 | the v6.0d owner instruction quoted in full | S-3 | yes. The coordinator confirms that the full instruction includes "If the delta review passes, bring v6.0d for adoption." |
| 3, 6, 8, 9 | `INVENTORY-v6.0c.md` replaced by `INVENTORY-v6.0e.md` at the old v6.0d lines 234, 2079, 2777 and 2785 | S-1 | yes |
| 4 | the prefix `^\s*((-|---)\s+)*`; the value pattern `:\s+[{[&*!]` | B-1 | yes |
| 5 | checklist: inputs reach the shell only through `env:`; `git fetch --no-tags -- origin "$F"`; no `${{ inputs.* }}` in a `run:` line | S-2 | yes |
| 7 | EI7 gains the seven B-1 forms | B-1 | yes |

The inventory diff carries only the matching bookkeeping. The identifiers are unchanged: no new id
is added and none is reused. No authorization wording is added.

## Check 2: B-1 rule re-probed

I implemented the rule from the v6.0e text in `probe/line_rule_v60e.py`. It does not reuse my
v6.0d `--fixed` code.

- **Clause 1:** a line containing `uses` in any letter case that does not match the exact form.
- **Clause 2:** after the prefix `^\s*((-|---)\s+)*`, a first character among `" ' { [ ? & * !`.
- **Clause 3:** the pattern `:\s+[{[&*!]`.

I ran it over the 24 workflow files in `review-v6.0d/probe/wf/` (output in
`probe/line_rule_v60e.out`):

- **Refused forms.** All 22 refuse: r01-r14 and r20-r27. This includes the tab variants r21
  (`-<TAB>"\x75ses"`) and r26 (`steps:<TAB>[`), the `---` whole-document form r25, and the nested
  dash r24.
- **Conforming workflows.** c01 and c02 pass. c02 is the complete pinned workflow, and its
  sha256 aaa761c4... is unchanged from the v6.0d review. It already passes `F` through `env:` and
  uses `git fetch --no-tags -- origin "$F"`, so it also meets the S-2 checklist item.
- **Result:** 0 unexpected results. This agrees with the writer's independent implementation
  (`work-v60e/line_rule_v60e.out`).

## Check 3: S-1, S-2, S-3

- **S-1: applied.** One citation of `INVENTORY-v6.0c.md` remains, at v6.0e line 47. It sits inside
  the v6.0c status bullet and describes v6.0c's own inventory, in the same way the earlier bullets
  cite theirs, so it is correct to leave it.
- **S-2: applied as a checklist item.** It changes no control or acceptance outcome; the workflow
  review enforces it.
- **S-3: applied.**

## Nit

**T-1 (editorial, optional).** The v6.0e status bullet does not state its own adoption condition.
The adoption sentence that remains belongs to the v6.0d bullet ("v6.0d is authoritative only after
that review returns ACCEPT ..."). `INVENTORY-v6.0e.md` open item 1 states the path: v6.0e is
brought for adoption if this review passes.

A sentence in the v6.0e bullet would make the status self-contained: "v6.0e is authoritative only
after the owner adopts it; until then the authoritative design is v5.5.9." This does not affect
the verdict.

## Files

- `review.md`
- `probe/line_rule_v60e.py` and `probe/line_rule_v60e.out`
- `probe/rows_cmp.py` and `probe/rows-v60d-v60e.txt`
- `MANIFEST.sha256`

The workflow inputs are in `../review-v6.0d/probe/wf/`, unchanged and covered by that review's
manifest.
