# Focused independent delta review of design v6.0d against v6.0c

Reviewer: independent, non-author. Review only. Nothing was written in the repository or in the
tool worktree, and there was no commit, push, GitHub write, GraphQL call or CI run. Every file this
review wrote is under `review-v6.0d/`; the throwaway probe trees are under the session workspace
(`rv60d<tmp>/`). No operation was refused.

## Objects verified

| Object | sha256 | Result |
|---|---|---|
| `DESIGN-v6.0d.md` | 1927e1356c7491ff00861e963d43308232e6ee51622ff5916b4f7921d32ef923 | match |
| `INVENTORY-v6.0d.md` | 9936495b1cc7a93448a09f1111d2085e6e779f6f67de7c1f1a203e7e940b0c1a | match |
| `CHANGES-v6.0d.md` | 89206acaa63b1243563660f01eb1d2fa0190744fac896bbfd9a5ac7512bcd81d | match |
| `CHANGES-v6.0d-from-v6.0c.diff` | d6b87ed0367fd52175532692cc0ab1c67d9a628ea760d270dfca701870c5d1de | match; byte-identical to the regenerated `diff -u DESIGN-v6.0c.md DESIGN-v6.0d.md`, header lines included |
| `DESIGN-v6.0c.md` | dd72ee5b9f1ed3718b5f1584bf88b957dbb481b0c9ac9dca3d6ff784389aa594 | match |
| `review-v6.0c/review.md` | 48dd41d0c0cc8b9169f61377eec7c606170b1fc6b7bb5c9aef0b5e7d4010ad20 | match |
| `coord2-impl-wt` | HEAD 443e871f | unchanged and clean after the probes |

## Verdict: REJECT

The verdict is REJECT because of one blocking finding, B-1. B-1 is a one-line fix to the text of
the `uses:` line rule. After that fix, I would accept v6.0d with the nits below.

v6.0d is otherwise correct:

- The O-4 test is right, sits first in the pre-run step, and works. EI15 and its countercontrol
  behave as stated.
- R-b, R-c, R-d and R-e are applied as stated.
- A conforming pinned workflow, with the pre-run program on one single-quoted `run:` line, can be
  written so that it passes the line rule. I wrote one, and it does.
- All 10 hunks map to O-4 or R-a to R-e. No authorization machinery is added, and no id is reused.

## Key question for the delta

*Does any v6.0d change let an incorrect scientific result pass that v6.0c or v5.5.9 would have
rejected? Is there any regression relative to v6.0c?*

**No.** Every v6.0d change only adds refusals. A legitimate run on `main` (a `push` or
`workflow_dispatch`) has `GITHUB_REF = refs/heads/main` and is unaffected (probe EI8). The consumer
checks are unchanged.

B-1 is not a regression either:

- v6.0c had the same `uses:` rule, and its looser wording admitted at least as much.
- v5.5.9 had no mechanical `uses:` check at all.
- The workflow content is still fixed by review and by its pin (TR15, TR50).

## Blocking finding

### B-1. The R-a line rule admits forms the text says it refuses (reproducible)

The R-a text says the rule refuses quoted or escaped keys, flow collections, complex keys, tags,
anchors and aliases "at the start of an entry". `CHANGES-v6.0d.md` claims "It never admits a form
the text says it refuses." I implemented the rule exactly as the text states it
(`probe/line_rule.py`). The second clause then admits the following YAML. PyYAML reads each as a
step with `uses: ./x`:

| Workflow line | Literal rule | PyYAML reads |
|---|---|---|
| `      -  "\x75ses": ./x` (two spaces after `-`) | PASS | `{'uses': './x'}` |
| `      -  {"\x75ses": ./x}` | PASS | `{'uses': './x'}` |
| `      -  !!str "\x75ses": ./x` | PASS | `{'uses': './x'}` |
| `      - - "\x75ses": ./x` (nested sequence) | PASS | `[{'uses': './x'}]` |
| `--- {"name":"w","on":"workflow_dispatch","jobs":{"a":{"runs-on":"ubuntu-24.04","steps":[{"\x75ses":"./x"}]}}}` (a whole workflow as one flow mapping after a document marker) | PASS | `{'uses': './x'}` |
| `-<TAB>"\x75ses": ./x`; `steps:<TAB>[ {"\x75ses": ./x} ]` | PASS | PyYAML rejects tabs here; a YAML 1.2 parser may accept them (not verified) |

Why the rule misses them:

- "After its indentation and an optional `- `" removes exactly one dash and one space, so the
  character the rule tests next is a space or a `-`.
- The rule never removes `---`.
- The value patterns (`: {` and the rest) require exactly one space after the colon.

Whether GitHub's parser accepts these forms is inferred, not verified; it accepted none of them in
any check I could run. Even so, the rule as written does not meet the property it claims, which is
the pass condition of this review.

There is no acceptance consequence. The pinned workflow is reviewed against the checklist, and its
pin fixes it (TR15, TR50).

**Smallest fix (wording; demonstrated with `line_rule.py --fixed`):**

- Read "after its indentation and any number of `-` or `---` markers, each followed by whitespace",
  that is `^\s*((-|---)\s+)*`.
- Read the value patterns as a colon followed by any whitespace and then `{`, `[`, `&`, `*` or `!`,
  that is `:\s+[{[&*!]`.
- Add the two-space form and the `---` form to EI7.

With the fix, all 22 refused forms refuse (the literal rule admits 7 of them), and both conforming workflows still pass
(`probe/line_rule.out`).

## Item 2: the O-4 test, probed

The test is correct as written. `GITHUB_REF` must equal `refs/heads/main` exactly, and `F` must
fully match `^[0-9a-f]{40}$`. It is placed first in the pre-run step, before the configuration
read and the file walk.

I ran the program as `probe/run_probes.sh` runs it: extracted by the R-e rule from the conforming
workflow `probe/wf/c02_full_pinned_workflow.yml`, on materialized git trees of 443e871f's tool files
(Python 3.13.18). There were 25 cases (`probe/run_probes.out`):

| Case | Result |
|---|---|
| EI8: clean tree, `refs/heads/main`, plan `F` | OK; entry point runs; no marker |
| EI15: branch dispatch (`refs/heads/feature`) with a chosen `F'` pinning changed code | FAIL before the entry point; no marker |
| Countercontrol: the same changed tree and `F'` with `refs/heads/main` | OK; the marker is written. The ref test is what refuses, and the changed code would run only if it were on `main` |
| EI15: `refs/tags/main` | FAIL |
| EI15: `F` given as `HEAD`, as 12 hex characters, in upper case | FAIL in each case |
| `GITHUB_REF` unset; `refs/heads/main-x`; `F` with a trailing newline | FAIL in each case |
| EI13 (R-d): `tools` a symlink inside the checkout; `tools` a symlink to an absolute path outside it | FAIL ("tools is not a real directory") |
| An inner parent (`engine`) as a symlink | FAIL (non-regular entry) |
| v6.0c regression set under `refs/heads/main`: P4, P7, P9, P10, one changed byte, a missing file, an extra file, a FIFO, configuration absent, `F` not fetched | FAIL in each case; no marker |
| EI14: CX-3 dispatched on a branch | FAIL (`GITHUB_REF`) |
| EI14: CX-3 at an on-`main` `T` | OK; the planted files never execute |

EI15 tests the cases it states, and EI8 serves as its countercontrol. EI14's revised expectation
follows from O-4 and adds no requirement.

## Item 3: can the pinned workflow be written to pass the rule?

**Yes.** `probe/wf/c02_full_pinned_workflow.yml` passes both the literal rule and the fixed rule.
It holds:

- `workflow_dispatch` inputs, read-only permissions and a GitHub-hosted `runs-on`;
- `actions/checkout` and `actions/upload-artifact` pinned by 40-hex ids;
- the fetch of `F`;
- one step named `pre-run pin check` whose single `run:` line is
  `python3 -I -S -B -c 'exec("...")'`. The program carries its newlines as `\n` escapes inside a
  Python string, so it is one physical line;
- the entry point.

The program implements every check of point 5, including O-4 and R-d, in 1606 bytes. Its
constraints are:

- no `'`;
- no `: ` and no ` #`, which a YAML plain scalar cannot contain anyway, so this also covers `: {`;
- no `uses` in any letter case.

All are easy to meet. The writer's flag is accurate: the rule refuses some harmless forms, such as
flow-style `branches: [main]`, which must be written as a block sequence.

## Nits (non-blocking)

- **S-1. Stale pointers.** `DESIGN-v6.0d.md` lines 234, 2079, 2777 and 2785 still cite
  `INVENTORY-v6.0c.md`, and the v6.0d status bullet does not name `INVENTORY-v6.0d.md`. These are
  traceability only.
- **S-2. Input handling, recommended for the workflow review; not a new requirement.** The
  sentence "only code merged on `main` can therefore execute" also depends on how inputs reach the
  shell. The fetch of `F` precedes the pre-run step, so `F` is used before the O-4 test validates
  it.
  - Pass the inputs through `env:` and quote them: `git fetch --no-tags -- origin "$F"`, as in
    `c02`.
  - Never interpolate `${{ inputs.* }}` into a `run:` line.
  - The checklist's "exact run lines" already lets the review enforce this.
- **S-3.** The status bullet quotes the owner's instruction without its last sentence ("If the
  delta review passes, bring v6.0d for adoption."). The truncation is harmless.

## Item 4: R-b to R-e

| Nit | Applied | Note |
|---|---|---|
| R-b | yes | Checklist: no `continue-on-error`, no `if:` after the pre-run check, no reusable workflow |
| R-c | yes | Point 1 lists the head branch; "after the checkout and the fetch of `F`"; inventory row P8 corrected; sec. 15 item 10 no longer says "requirement 5" (see S-1 for the remaining stale pointers) |
| R-d | yes | `tools` and every parent must be a real directory; EI13 gains both symlink cases, which my probe reproduces |
| R-e | yes | The rule is unambiguous: the step whose `name:` is exactly `pre-run pin check`, its single `run:` line, and the single-quoted `-c` argument taken verbatim. A blob with no such step, more than one, or another `run:` form is refused. My extractor (`probe/extract.py`) implements it without choices. Inventory table 3b names the runner, sets `GITHUB_REF` and `F` per case, and builds EI9's `.pyc` for the running interpreter's cache tag |

## Hunk map (10 hunks)

| # | Content | Source | Verified |
|---|---|---|---|
| 1 | title; v6.0d status bullet | owner decision; traceability | yes (S-3) |
| 2 | identifier EI15 | O-4 | yes |
| 3 | point 1 lists the head branch | R-c | yes |
| 4 | "after the checkout and the fetch of `F`"; the `GITHUB_REF` and 40-hex test first; real parent directories; step location and extraction | O-4, R-c, R-d, R-e | yes |
| 5 | the `uses:` line rule, without a YAML parser | R-a | the text is applied as written, but it is incomplete (B-1) |
| 6 | checklist additions | R-b | yes |
| 7, 10 | EI1-EI15 (sec. 10 lead, S13) | traceability | yes |
| 8 | EI7 forms; EI13 symlink cases; EI14 under O-4; EI15 | R-a, R-d, O-4 (EI14 forced by O-4) | yes |
| 9 | sec. 15 item 10 | R-c; owner decision | yes |

Nothing else changed. The inventory diff is consistent with these hunks.

## Item 6: rows, identifiers and authorization

**Rows** (`rows/rows-v60c-v60d.txt`): from v6.0c to v6.0d, 509 rows are retained, 4 modified (EI7,
EI13, EI14, S13), 1 added (EI15) and none removed. This equals the CHANGES file.

**Line counts:** from v6.0c, 22 removed and 57 added; from v5.5.9, 596 removed and 553 added. Both
recounted equal.

**Identifiers:**

- EI15 appears nowhere outside the v6.0d files, and in no v5.5.10 or v5.5.10a file.
- EI7, EI13 and EI14 gain cases within their meaning.
- No id is reused.

**Authorization:**

- The added lines that mention the owner are the quoted decision and the procedural adoption
  sentence.
- The O-4 test reads a runner value and an id format; it is not an approval check.
- The delta adds no new requirement beyond O-4 and the nits.

## Files

- `review.md`
- `probe/`:
  - `line_rule.py` and `line_rule.out`: the literal rule and the candidate fix on 24 workflow blobs;
  - `wf/*.yml`: the refused forms `r01`-`r27`, the conforming `c01` and the full pinned workflow
    `c02`;
  - `extract.py`: the R-e extractor;
  - `prerun_src.py`: the program source that `c02` embeds;
  - `run_probes.sh` and `run_probes.out`;
  - `entry_v60c.py`, `marker_mod.py`, `make_pyc.py`, `ext_util.c`, copied from the v6.0c review.
- `rows/`
- `MANIFEST.sha256`
