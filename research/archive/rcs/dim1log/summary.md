# Mathlib bridge job log: CompositeDimension.lean warnings

Run `37299337191`, job "Mathlib bridge" id `111728066298`. Every figure below is computed by `rcs/dim1log_scripts/analyze.py` from the saved files in this directory; nothing was read off by eye.

## Provenance

- Tool call: `mcp__github__get_job_logs(owner=amaybaum, repo=incompleteness, job_id=111728066298, return_content=true, tail_lines=5000)`.
- Response fields: `job_id=111728066298`, `message='Job logs content retrieved successfully'`, `original_length=37081`, `logs_content` = 429,819 characters.
- `raw_tool_response.json`: 435,192 bytes, sha256 `aede3979c452b73c2194d76dbbce7e4ca1299a9c1217f087c473e5a1f3215897`.
- `raw.log`: 430,015 bytes, sha256 `7a617f1240ef80db656dead07aca85b4500fea5d6e7623cf35235b270cb03de3`; identical to the response's `logs_content`: yes.
- Run metadata (GitHub API, not from the log): event `workflow_dispatch`, head_sha `d849e22ba6c29810f133818d78bdab7ba833a30a`, branch `claude/dim1`, run_attempt 1, conclusion `success`; job conclusion `success`.

## 1. Coverage

- Reported original length (`original_length`): **37081**. It is not a character count: the returned window alone is 429,819 characters. Read as the full log's line count, the window is lines 32082–37081 of 37081.
- Lines returned: **5000** (split on `\n`; text ends with a newline: no; `\r` characters: 0; `splitlines()` count: 5000).
- Lines without a leading timestamp: 0. Timestamps non-decreasing through the window: yes.
- First timestamp (window line 1): `2026-10-05T10:55:11.9735682Z`
- Last timestamp (window line 5000): `2026-10-05T10:56:26.3819438Z`
- **The build line for `OIBridge.CompositeDimension` is inside the window**: 1 line(s) matching `Built|Replayed OIBridge.CompositeDimension`; `Replayed` lines: 0.
  - window line 4721 (full-log line 36802 on the line-count reading):

    ```text
    2026-10-05T10:55:27.7779162Z ⚠ [3630/3632] Built OIBridge.CompositeDimension (16s)
    ```

- The block that line opens runs over window lines 4721–4923. It ends where the next build-progress line begins, window line 4924:

  ```text
  2026-10-05T10:55:34.6852060Z ℹ [3631/3632] Built OIBridge (6.8s)
  ```

- Window lines mentioning `CompositeDimension` anywhere: 105, spanning window lines 4721–4923; all inside the block: yes. No CompositeDimension line occurs before the build line or after the block.

## 2. Lines containing both `CompositeDimension.lean` and `warning` (verbatim, in order)

Count: **17**

```text
2026-10-05T10:55:27.7779627Z warning: OIBridge/CompositeDimension.lean:768:53: This simp argument is unused:
2026-10-05T10:55:27.7781992Z warning: OIBridge/CompositeDimension.lean:768:57: This simp argument is unused:
2026-10-05T10:55:27.7783656Z warning: OIBridge/CompositeDimension.lean:1162:9: Variable name `x` is not explicitly referenced.
2026-10-05T10:55:27.7785471Z warning: OIBridge/CompositeDimension.lean:1162:14: Variable name `y` is not explicitly referenced.
2026-10-05T10:55:27.7787582Z warning: OIBridge/CompositeDimension.lean:1163:9: Variable name `x` is not explicitly referenced.
2026-10-05T10:55:27.7789389Z warning: OIBridge/CompositeDimension.lean:1163:14: Variable name `y` is not explicitly referenced.
2026-10-05T10:55:27.7791480Z warning: OIBridge/CompositeDimension.lean:2591:23: This simp argument is unused:
2026-10-05T10:55:27.7793827Z warning: OIBridge/CompositeDimension.lean:2591:52: This simp argument is unused:
2026-10-05T10:55:27.7796060Z warning: OIBridge/CompositeDimension.lean:2593:10: This simp argument is unused:
2026-10-05T10:55:27.7798238Z warning: OIBridge/CompositeDimension.lean:2607:25: This simp argument is unused:
2026-10-05T10:55:27.7800317Z warning: OIBridge/CompositeDimension.lean:2607:54: This simp argument is unused:
2026-10-05T10:55:27.7802792Z warning: OIBridge/CompositeDimension.lean:2608:70: This simp argument is unused:
2026-10-05T10:55:27.7805052Z warning: OIBridge/CompositeDimension.lean:2608:93: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
2026-10-05T10:55:27.7806056Z warning: OIBridge/CompositeDimension.lean:2863:9: Variable name `x` is not explicitly referenced.
2026-10-05T10:55:27.7807839Z warning: OIBridge/CompositeDimension.lean:2863:14: Variable name `y` is not explicitly referenced.
2026-10-05T10:55:27.7809573Z warning: OIBridge/CompositeDimension.lean:2864:9: Variable name `x` is not explicitly referenced.
2026-10-05T10:55:27.7811495Z warning: OIBridge/CompositeDimension.lean:2864:14: Variable name `y` is not explicitly referenced.
```

Window line numbers, in the same order: 4722, 4729, 4736, 4742, 4748, 4754, 4760, 4768, 4776, 4784, 4792, 4800, 4808, 4811, 4817, 4823, 4829.

Cross-checks: the same 17 lines match the Lean header pattern `warning: OIBridge/CompositeDimension.lean:<line>:<col>: …` (identical set); case-insensitive `warning` gives 17 (identical set); each line carries exactly one location: yes; `##[warning]` annotations mentioning CompositeDimension: 0; `error` lines for `CompositeDimension.lean`: 0.

### The seven requested locations

| location | present | window line | message as expected |
|---|---|---|---|
| `2591:23` | yes | 4760 | yes (log adds a trailing ':') |
| `2591:52` | yes | 4768 | yes (log adds a trailing ':') |
| `2593:10` | yes | 4776 | yes (log adds a trailing ':') |
| `2607:25` | yes | 4784 | yes (log adds a trailing ':') |
| `2607:54` | yes | 4792 | yes (log adds a trailing ':') |
| `2608:70` | yes | 4800 | yes (log adds a trailing ':') |
| `2608:93` | yes | 4808 | yes (exact) |

The seven lines, verbatim, in the table's order:

```text
2026-10-05T10:55:27.7791480Z warning: OIBridge/CompositeDimension.lean:2591:23: This simp argument is unused:
2026-10-05T10:55:27.7793827Z warning: OIBridge/CompositeDimension.lean:2591:52: This simp argument is unused:
2026-10-05T10:55:27.7796060Z warning: OIBridge/CompositeDimension.lean:2593:10: This simp argument is unused:
2026-10-05T10:55:27.7798238Z warning: OIBridge/CompositeDimension.lean:2607:25: This simp argument is unused:
2026-10-05T10:55:27.7800317Z warning: OIBridge/CompositeDimension.lean:2607:54: This simp argument is unused:
2026-10-05T10:55:27.7802792Z warning: OIBridge/CompositeDimension.lean:2608:70: This simp argument is unused:
2026-10-05T10:55:27.7805052Z warning: OIBridge/CompositeDimension.lean:2608:93: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
```

### Other `CompositeDimension.lean` warning locations present (10)

| location | window line | message |
|---|---|---|
| `768:53` | 4722 | This simp argument is unused: |
| `768:57` | 4729 | This simp argument is unused: |
| `1162:9` | 4736 | Variable name `x` is not explicitly referenced. |
| `1162:14` | 4742 | Variable name `y` is not explicitly referenced. |
| `1163:9` | 4748 | Variable name `x` is not explicitly referenced. |
| `1163:14` | 4754 | Variable name `y` is not explicitly referenced. |
| `2863:9` | 4811 | Variable name `x` is not explicitly referenced. |
| `2863:14` | 4817 | Variable name `y` is not explicitly referenced. |
| `2864:9` | 4823 | Variable name `x` is not explicitly referenced. |
| `2864:14` | 4829 | Variable name `y` is not explicitly referenced. |

## 3. Total

**17** warning lines for `CompositeDimension.lean` in the window: 7 at the requested locations and 10 elsewhere. Distinct locations: 17.

## Appendix A. Full message blocks of the seven requested warnings (verbatim)

Each block is the header line and its continuation lines, up to the next diagnostic header or build-progress line.

`2591:23` (window lines 4760–4767):

```text
2026-10-05T10:55:27.7791480Z warning: OIBridge/CompositeDimension.lean:2591:23: This simp argument is unused:
2026-10-05T10:55:27.7791855Z   LinearMap.map_add₂
2026-10-05T10:55:27.7791970Z 
2026-10-05T10:55:27.7792064Z Hint: Omit it from the simp argument list.
2026-10-05T10:55:27.7792589Z   [apply] simp only [ht, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul,
2026-10-05T10:55:27.7793044Z     hd00, hd0, hd0', hvv', eq_self_iff_true, if_true]
2026-10-05T10:55:27.7793220Z 
2026-10-05T10:55:27.7793392Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

`2591:52` (window lines 4768–4775):

```text
2026-10-05T10:55:27.7793827Z warning: OIBridge/CompositeDimension.lean:2591:52: This simp argument is unused:
2026-10-05T10:55:27.7794171Z   LinearMap.map_smul₂
2026-10-05T10:55:27.7794281Z 
2026-10-05T10:55:27.7794379Z Hint: Omit it from the simp argument list.
2026-10-05T10:55:27.7794861Z   [apply] simp only [ht, LinearMap.map_add₂, map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul,
2026-10-05T10:55:27.7795300Z     hd00, hd0, hd0', hvv', eq_self_iff_true, if_true]
2026-10-05T10:55:27.7795474Z 
2026-10-05T10:55:27.7795648Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

`2593:10` (window lines 4776–4783):

```text
2026-10-05T10:55:27.7796060Z warning: OIBridge/CompositeDimension.lean:2593:10: This simp argument is unused:
2026-10-05T10:55:27.7796373Z   eq_self_iff_true
2026-10-05T10:55:27.7796481Z 
2026-10-05T10:55:27.7796576Z Hint: Omit it from the simp argument list.
2026-10-05T10:55:27.7797010Z   [apply] simp only [ht, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply,
2026-10-05T10:55:27.7797448Z     LinearMap.smul_apply, smul_eq_mul, hd00, hd0, hd0', hvv', if_true]
2026-10-05T10:55:27.7797661Z 
2026-10-05T10:55:27.7797823Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

`2607:25` (window lines 4784–4791):

```text
2026-10-05T10:55:27.7798238Z warning: OIBridge/CompositeDimension.lean:2607:25: This simp argument is unused:
2026-10-05T10:55:27.7798575Z   LinearMap.map_add₂
2026-10-05T10:55:27.7798688Z 
2026-10-05T10:55:27.7798779Z Hint: Omit it from the simp argument list.
2026-10-05T10:55:27.7799219Z   [apply] simp only [ht, hf, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply, LinearMap.smul_apply,
2026-10-05T10:55:27.7799609Z     smul_eq_mul, hd00, hd0, hd0', hS0', hS1']
2026-10-05T10:55:27.7799754Z 
2026-10-05T10:55:27.7799919Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

`2607:54` (window lines 4792–4799):

```text
2026-10-05T10:55:27.7800317Z warning: OIBridge/CompositeDimension.lean:2607:54: This simp argument is unused:
2026-10-05T10:55:27.7800932Z   LinearMap.map_smul₂
2026-10-05T10:55:27.7801114Z 
2026-10-05T10:55:27.7801209Z Hint: Omit it from the simp argument list.
2026-10-05T10:55:27.7801644Z   [apply] simp only [ht, hf, LinearMap.map_add₂, map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply,
2026-10-05T10:55:27.7802073Z     smul_eq_mul, hd00, hd0, hd0', hS0', hS1']
2026-10-05T10:55:27.7802227Z 
2026-10-05T10:55:27.7802395Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

`2608:70` (window lines 4800–4807):

```text
2026-10-05T10:55:27.7802792Z warning: OIBridge/CompositeDimension.lean:2608:70: This simp argument is unused:
2026-10-05T10:55:27.7803097Z   hd0
2026-10-05T10:55:27.7803186Z 
2026-10-05T10:55:27.7803270Z Hint: Omit it from the simp argument list.
2026-10-05T10:55:27.7803734Z   [apply] simp only [ht, hf, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply,
2026-10-05T10:55:27.7804161Z     LinearMap.smul_apply, smul_eq_mul, hd00, hd0', hS0', hS1']
2026-10-05T10:55:27.7804360Z 
2026-10-05T10:55:27.7804521Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

`2608:93` (window lines 4808–4810):

```text
2026-10-05T10:55:27.7805052Z warning: OIBridge/CompositeDimension.lean:2608:93: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
2026-10-05T10:55:27.7805356Z 
2026-10-05T10:55:27.7805534Z Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
```

## Appendix B. Source-position control

Source: `git show d849e22ba6c29810f133818d78bdab7ba833a30a:verification/lean-mathlib/OIBridge/CompositeDimension.lean`. Its git blob id, recomputed here from the bytes piped in, is `377f0b25ed0ef58cf6269f71b816e477450131bc`, against `377f0b25ed0ef58cf6269f71b816e477450131bc` from `git rev-parse`: match. The file has 3008 newline-separated segments. For each warning, the table gives the token that begins at the reported line and (0-based, codepoint) column, next to the name the log message gives.

| location | token at position in source | named in log | match |
|---|---|---|---|
| `768:53` | `pc` | `pc` | yes |
| `768:57` | `pt` | `pt` | yes |
| `1162:9` | `x` | `x` | yes |
| `1162:14` | `y` | `y` | yes |
| `1163:9` | `x` | `x` | yes |
| `1163:14` | `y` | `y` | yes |
| `2591:23` | `LinearMap.map_add₂` | `LinearMap.map_add₂` | yes |
| `2591:52` | `LinearMap.map_smul₂` | `LinearMap.map_smul₂` | yes |
| `2593:10` | `eq_self_iff_true` | `eq_self_iff_true` | yes |
| `2607:25` | `LinearMap.map_add₂` | `LinearMap.map_add₂` | yes |
| `2607:54` | `LinearMap.map_smul₂` | `LinearMap.map_smul₂` | yes |
| `2608:70` | `hd0` | `hd0` | yes |
| `2608:93` | `<;>` | `<;>` | yes |
| `2863:9` | `x` | `x` | yes |
| `2863:14` | `y` | `y` | yes |
| `2864:9` | `x` | `x` | yes |
| `2864:14` | `y` | `y` | yes |

Matches: 17/17.

Countercontrol (the comparison discriminates): with every column shifted by +1, matches fall to 0/17; reading the columns as UTF-8 byte offsets instead of codepoints gives 13/17, failing at `768:53` (non-ASCII before the column: μ ν), `768:57` (non-ASCII before the column: μ ν), `2591:52` (non-ASCII before the column: ₂), `2607:54` (non-ASCII before the column: ₂).

- Source line 2591: inside `blockData_of_orthonormal` (declaration at line 2491; next declaration at line 2703; non-indented lines between line 2491 and line 2591: 0).
- Source line 2593: inside `blockData_of_orthonormal` (declaration at line 2491; next declaration at line 2703; non-indented lines between line 2491 and line 2593: 0).
- Source line 2607: inside `blockData_of_orthonormal` (declaration at line 2491; next declaration at line 2703; non-indented lines between line 2491 and line 2607: 0).
- Source line 2608: inside `blockData_of_orthonormal` (declaration at line 2491; next declaration at line 2703; non-indented lines between line 2491 and line 2608: 0).
