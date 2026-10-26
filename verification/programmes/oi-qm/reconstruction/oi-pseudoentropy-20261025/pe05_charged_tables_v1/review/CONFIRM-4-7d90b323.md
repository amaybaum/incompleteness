# PE-05: final cumulative confirmation at `7d90b3234093d95d62213d772dd3c3af318c66c0`

- **Method:** read-only; design checks only; nothing committed.
- **Branch:** the remote branch head equals `7d90b323`.

## Verdict: CONFIRM FOR FREEZE at `7d90b323`

1. **IMP-1 and the typo.** The diff `d6fc056a..7d90b323` (one commit) contains exactly these two edits, plus their
   record in CHANGES-r3.
   - **IMP** now:
     - takes a startup snapshot of `sys.modules` as the entry module's first statement;
     - measures only the top-level non-stdlib names added after that snapshot, still excluding `__main__` and the
       stage package;
     - records the startup set and never compares it;
     - checks that every stage-package module loads from inside the stage's code directory;
     - in result mode, refuses a shard unless the measured set is exactly `{"numpy"}`.
   - The IMP row, `PE05_env.imports`, §10 and NOTES §10 agree.
   - PLAN §9 now reads "… not quotations. In the approval table, the row …".
2. **P1–P3 are present at `7d90b323` as asked.**
   - **P1:** all option-dependent body items are `dependent` block entries with `assumes` tags. `CH_IFF_boundary_records`
     and `EN_meaning` are among them.
   - **P2:** no commit-status claim remains in the files. The freeze commit and digests are recorded on #923.
   - **P3:** the "Fixed identifiers" bullet is present. `pe02-shard/1`, `pe02-measurements/1`, `pe02-verdict/1`,
     `pe02-rp01/1` and `pe02-parameters` are unchanged.
3. **The rename is complete.**
   - The title is "PE-05". `git grep pe02_charged` outside the stage directory finds nothing. The remaining "PE-02"
     strings are owner quotes, discussion of the name, or history.
   - The other PE-02 (computational versus physical) is untouched. #934 is retitled.
   - The nine retained review files equal my own copies, by blob.
   - The four design scripts replayed byte for byte at `7b469183`. They have not changed since.
4. **The frozen PE-01 references.**
   - **No frozen record was rewritten.**
     - The `pe01_bounded_tests_v1/` tree is the same object at `a611f943` and `7d90b323` (`0dabf420…`).
     - So is the thread `review/` tree (`a227ab33…`).
     - The PE-01 PLAN blob at its freeze `af38dc2d` equals the blob at `7d90b323` (`3ca81a06…`).
   - **Each historical README citation resolves at `7d90b323`.** README lines 1–277 are byte-identical to
     `a611f943`, whose README equals the version at the pinned commits `66578f41`, `af38dc2d` and `01eb7950`.
     - `:265` is the "First milestone" text ("PE-01 and PE-02, for one fixed generator…") at all four commits.
     - `:252` is "## Authority limits" (`:252–261`).
     - `:268–277` is the outcome rule through "closes as OPEN.".
     - `:155–159` is unaffected.
   - **No 265 → 271 shift remains.** The PE-05 entry now sits after line 277.
5. **Digests and TH (all match the drafter's):**

   | Object | sha256 |
   |---|---|
   | `PLAN.md` | `dedd129a48e53935410f0b6f428f30aed40b809526f6e1aa422baff869ca7022` |
   | `NOTES.md` | `cfddbdcf51e7261c8f1ba8d2a5e214fb723cd78deca9180375eca2042630841a` |
   | `pe02-parameters` block (7412 bytes) | `d89d3ce49c865ec31e44ff7554008fb4ce5355f0297a7d8fb8938f758ecc3a96` |

   `th_emulation.py` on PLAN at `7d90b323` prints **PASS**: no `OPEN` value, every `assumes` tag matches its
   decision, and all per-n tables, caps, CH-IFF records and the PL boundary re-derive.

**Scope.** This confirms the specification freeze only. No experimental execution is authorized.
