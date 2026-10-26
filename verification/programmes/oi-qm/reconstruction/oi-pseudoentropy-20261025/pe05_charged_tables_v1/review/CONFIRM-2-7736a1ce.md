# PE-05 freeze candidate `7736a1ce`: confirmation

- **Method:** read-only.
  - `git fetch`, then `git diff 7b469183 7736a1ce` and `git show` snapshots.
  - Design checks only. Nothing was executed and nothing was committed.
- **Reviewer:** the same independent reviewer as `review-confirm-PE05.md`.

## Verdict: **FINDINGS, two of them small enough to fix in one line each.** Not CONFIRM at `7736a1ce` as it stands.

- Everything the coordinator listed checks out (items 1–5 below).
- The new C3 content has two internal inconsistencies, E1 and E2. Freezing them would leave the implementer to resolve
  a refusal rule after F.
- **Fix:** amend `7736a1ce` with E1 and E2, giving a new F, and recompute the three digests. A glance at that diff is
  enough to confirm; no further review round is needed. E3 is a nit.

## Checks

1. **The diff `7b469183..7736a1ce` contains only C1–C5.**
   - README: the PE-05 entry is moved to the end of the file.
   - PLAN and NOTES: the status lines, the C3 content, and the C4 quotes. The §9 ruling cells are relabelled
     "summarized, not quoted".
   - CHANGES-r3: the C5 record and the C1–C5 table.
   - No other specification text changed. C6 is untouched.
2. **README lines 1–277 are byte-identical to `a611f943`** (`cmp` on the first 277 lines). The file is now 286 lines,
   with the PE-05 entry under "Stages added after the first milestone". PE-01's frozen citations `:265`, `:268–277` and
   `:252–261` resolve at `HEAD`.
3. **The owner quotes are verbatim**, after whitespace and line-wrap normalisation; exact substring counts below.

   | Quote | PLAN | NOTES | CHANGES-r3 |
   |---|---|---|---|
   | The 18:54 UTC approval | 1 | 1 | 1 |
   | "Approved: rename the new stage to PE-05." | 2 | 1 | 1 |
   | "PE-04 remains reserved … independent confirmation pass." | 0 | 1 | 1 |
   | "This authorizes the specification freeze, not experimental execution." | 2 | 1 | 1 |

   - PLAN quotes only the first sentence, "PE-04 remains reserved for quantum reconstruction.", as its own fragment. It
     is a verbatim prefix of the owner's text.
   - The paraphrase "authorizes specification freeze" survives only in CHANGES-r3's description of the C4 fix, where
     it is correctly marked as the paraphrase that was removed.
   - **One quoted item is not in the owner wording I was given:** the approval table's "O8 — Rename to PE-04 and
     retitle #934 before freeze", quoted in PLAN §9, NOTES §6 and CHANGES-r3. I cannot verify it. Confirm it against
     the approval table, or present it as a summary.
4. **`PE05_env`, ENV and TH.**
   - **Pins.** Python 3.12 and numpy 2.2.6 equal `RP01_env` and PE-01's workflow (`PYTHON_VERSION: "3.12"`,
     `NUMPY_VERSION: "2.2.6"`). PE-01's own replay keeps its separate `RP01_env` pin. numpy 2.2.6 has cp312
     manylinux x86_64 wheels, and PE-01's CI installed exactly this pair, so the pin can be met on GitHub-hosted
     runners. The check is Python major.minor and numpy exact, which is strict enough without being fragile.
   - **E1 (fix before freeze): the ENV row and `PE05_env.check` disagree on the runner.**
     - The ENV row says TH and collect refuse a shard whose "runner image differs from `fixed.PE05_env`".
     - `PE05_env.check` says only Python major.minor and numpy are checked, and that the image name and version are
       recorded.
     - If "image" were read to include `ImageVersion`, which changes roughly weekly on GitHub-hosted runners, the RP
       reruns and later shards would be refused.
     - State one rule. Recommended: refuse unless `ImageOS == "ubuntu24"` and `RUNNER_ARCH == "X64"`; record
       `ImageVersion` but do not compare it. Add `"ImageOS": "ubuntu24"` and `"arch": "X64"` to `PE05_env`. (The
       recorded `ImageVersion` lets an RP rerun be traced to its image without being refused by it.)
   - **E2 (fix before freeze): ENV would refuse the local smoke runs that §10 and §A.40 require.**
     - The ENV row makes TH "refuse to start" on any mismatch, with no mode scope.
     - The §10 local-smoke row and the §A.40 pre-push checks run locally, and NOTES records local Python 3.13 with no
       `ImageOS`.
     - Scope ENV to result mode, as PE-01 scoped its preflight by mode: smoke and test modes record the environment
       and are never results. Alternatively, state that local smoke must run under 3.12 / 2.2.6 with the image fields
       absent.
   - **E3 (nit, §A.41).** The block's `"imports": ["python standard library", "numpy"]` is asserted with no checkpoint
     measuring it. Either have each shard record the sorted top-level names in `sys.modules` and have ENV refuse
     anything outside the stdlib, numpy and the package itself, or drop the entry.
   - **Optional.** RP-01 runs with `RP01_env`, which pins no runner image. PE-01's workflow used `ubuntu-latest`.
     Running RP-01 on ubuntu-24.04 as well would make the two environments uniform. Byte-identity of PE-01's canonical
     JSON is not expected to depend on the image.
   - **TH.** My `th_emulation.py`, re-run on the PLAN at `7736a1ce`, prints **PASS**. All 24 `dependent` entries carry
     `assumes`, and every item equals the recorded decision. Every per-n table, cap, CH-IFF record and the PL boundary
     re-derive. No `OPEN` value or placeholder remains.
5. **Freeze digests at `7736a1ce`:**

   | Object | Digest |
   |---|---|
   | `pe02-parameters` block (bytes after the opening fence line up to the closing fence) | 6718 bytes, sha256 `23833a320f45e8c09afdd62a47d6eb92df442037580aa3ec1152d4827c55b87a`. Matches the drafter's `23833a32…b87a`. |
   | `PLAN.md` | sha256 `4c17a4b2b0dfd13b48867efec21d74504ae43427d7da07a5f6d3de24310ff9bc` |
   | `NOTES.md` | sha256 `a8a40d7c49d16d3044642600cf33b00f832642777aa88cdbc2ce861e92f9a945` |

   E1 changes the block, and E1 and E2 change PLAN, so all three must be recomputed at the new F.

**Minor.** CHANGES-r3's header still reads "Status: WIP / UNREVIEWED". It is a change log, not the specification, so
this is optional.
