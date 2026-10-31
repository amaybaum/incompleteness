# PE-05 freeze candidate `d6fc056a`: confirmation

- **Method:** read-only; design checks only; nothing committed.
- **Diff:** `7736a1ce..d6fc056a`, one commit.

## Verdict: **FINDINGS (minor).**

- Every requested item checks out (1–6 below).
- One rule, IMP, can fail closed for a reason unrelated to the code under test. I recommend refining it before F, and
  fixing one typo in the same commit.
- Neither finding affects result integrity. If the stage is frozen at `d6fc056a` as it stands, an IMP misfire would
  only refuse result runs, and a pre-run amendment authorized by the owner would fix it.

## Checks

1. **The diff is exactly E1, E2, E3, the two-cell O8 quote and the CHANGES-r3 header.** It touches PLAN, NOTES and
   CHANGES-r3 only. Nothing else changed.
2. **The runner rule is substantively identical in all four places:** the ENV row, `PE05_env.check`, PLAN §10 and
   NOTES §10.
   - Python major.minor is 3.12, `numpy.__version__` is 2.2.6, `ImageOS` is `ubuntu24` and `RUNNER_ARCH` is `X64`.
   - `ImageVersion` and the full `sys.version` are recorded and never compared.
   - The only differences are `==` against "equals". `PE05_env` carries `ImageOS`, `RUNNER_ARCH` and
     `modes_checked: ["result"]`.
3. **ENV and IMP are scoped to result mode.**
   - The §5 "Run modes" bullet follows PE-01's smoke/test/result split.
   - ENV refuses "in result mode only"; IMP is enforced by collect "in result mode".
   - RP covers result-mode shards, and only result-mode shards enter `measurements.json`.
4. **The IMP exclusion.** Excluding `__main__` and the stage's own package is correct and necessary. The rule has one
   remaining defect:
   - **IMP-1 (recommended before F).** "Top-level names in `sys.modules` not in `sys.stdlib_module_names`" also
     catches modules the interpreter imports at startup through `site`, `.pth` files and `sitecustomize`. `-I` does
     not suppress `site`.
     - Here, `python3 -I -c …` on a Debian-family Python 3.13 already shows `_distutils_hack` (from
       `distutils-precedence.pth`) and `sitecustomize`.
     - Whether the setup-python 3.12 tool-cache build on ubuntu-24.04 does the same is not established. If it does,
       every result shard is refused.
     - **Fix:** measure IMP as the set of top-level names **added to `sys.modules` after the stage's entry point
       starts**. Snapshot at the first line of the entry module, before any stage or numpy import, and record the
       startup set separately. Equivalently, exclude the recorded startup set.
     - Optionally, also check that every `sys.modules` entry under the stage package has a `__file__` inside the
       stage's code directory, so that a module vendored inside the package cannot escape IMP.
5. **TH emulation:** my `th_emulation.py` on PLAN at `d6fc056a` prints **PASS**.
6. **The digests match the drafter's:**

   | Object | Digest |
   |---|---|
   | `PLAN.md` | `3d6ecb8e006353472e529bddb090d9386c11b4e8c24a8d4e53f4a9f7c4d29ad8` |
   | `NOTES.md` | `907427398782660cf2a433f06328cf7bf0b17187228e5bd19c4df1b9cf44eea3` |
   | `pe02-parameters` block | 6978 bytes, `5bf57208df091597e7d43c1850fd29403f4746db8db46667d3a37537b716e5c7` |

**Typo (fix in the same commit).** PLAN:736–737 reads "… they are not quotations. The / the approval table's row
…" ("The the").

If IMP-1 and the typo are applied, a glance at that one-commit diff is enough to confirm. Recompute all three
digests, because the IMP row and possibly `PE05_env.imports` change.
