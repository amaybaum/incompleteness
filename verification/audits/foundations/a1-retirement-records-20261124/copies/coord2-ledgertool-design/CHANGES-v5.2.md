# DESIGN-v5.2: changes against DESIGN-v5.1

## Inputs

Each input's sha256 was verified before use:

| Input | sha256 |
|---|---|
| `DESIGN-v5.1.md` | 0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe |
| `review-stage1/review-stage1.md` (verdict REVISE) | 007d4ada8c19cb3103073d80f75c9721d57c908f7cd8813a7b52c568449d4b6a |
| `impl-stage1/REPORT.md` | 9093f93a002fcc2dfa5574468ed15bf37044a6434c59b2f2d81d3eecde7cad9f |
| `coord2-records/DRIFT-FINAL-NOTES.md` (addendum) | ca07a51456e3799fe3542c49ea80f0a728b883a5957aa3c6fb3a9b4d89869c81 |

The Stage 1 implementation, local commit 8c1e628a08272ad9414929fa8e003020e1cc2234, was read only. I
read `engine/execution.py`, to locate the guard-pin code, and the draft A1 configuration's
register and infinity profiles.

Owner decisions of 2026-11-23, named S1-D1 to S1-D3 in the design:

- **S1-D1:** W1, option B.
- **S1-D2:** apply D1-D8.
- **S1-D3:** specify the fixes for B1-B6.

The coordinator's addendum adds the drift findings S2-S7.

Scope and method:

- Paper-only: no repository, git or GitHub write, and no workflow run.
- New measurement scripts are in `work-v52/`. They read git objects only.
- No safeguard was weakened. Where a choice existed, I specified the stricter check.

## 1. Design corrections D1-D8 and the W1 decision

| Item | DESIGN-v5.2 sections | What changed | How verified; figures re-derived |
|---|---|---|---|
| D1 and S1-D1: W1 self-match, option B | 6.2 (fingerprint field `negative_allowance`; step 3 rewritten); 6.3 (allowance widening; self-PASS lint clause; full-sentence examples); 6.5 (W1-c paragraph); 10.4 (WB1-WB12); 10.3 RT-D and RT-I7A | See "W1 option B" below the table | `work-v52/w1c.py`. The W1-c sentence (ch19:198 = FULL:5270 at T1', one sentence under splitter v2, 404 characters) has exactly one `finit` match and no match of the other five negative literals. The other W1 sentences have none. So allowance 1 makes both lines PASS, and every control of WB2-WB12 follows from step 3 as written. Re-derived: the count of 1 |
| D2: SW2 expectation | 10.3 SW2 (and SW1 made explicit) | For each of the 584 sites, exactly one new FAIL naming it: obligation RET, `unauthorized-change`, segment H..X. The HP items at the unmutated H are unchanged. Items are compared by `(obligation, class, segment, fingerprint)` (review O3). The strict reading holds once the 7 context adjudications exist | Not re-run (about 6 min on the implementation). The 7 sites the review names are exactly the 7 E..H meaning-context sites of sec. 4.4, IR. The review measured the delta predicate at 584/584 |
| D3: 7 HP structure REVIEWs | 0.3; 4.4 (table and note); 8.2 (10 indicator adjudications); 10.3 RT-H0, RT-T0 | The E..H indicator row has no T1' condition. 7 HP items: FULL:706, 708; ch02:76, 78; Substratum.md:94, 253 (LIST); Main.md:741 (TABLE). RET stays 3 | `work-v52/struct.py`, from the sec. 4.2-4.3 definitions over sites unique at E and H: 7, the named sites. 3 of them are unique at T1', which explains v4's 3. Re-derived |
| D4: region lines 215 | 0.3; 5 (site span includes its LF, v1 sec. 4.3); 14; RT-T0 | 203 → 215 under the LF-inclusive span. Site counts and the 84 hit lines are unchanged | `work-v52/b3.py` variant: 383/197/4, 215 lines, 84 (86 with `count-grep`); without the LF, 203. Re-derived |
| D5: RT-D 45 `resid` | 0.3; RT-D | RT-D reads "45 `resid` lines REVIEW, 17 of them hit by no other review profile" | `w1c.py`: 45 added-text lines with a `resid` hit, none of them a `ptr` or `count-grep` hit. 17 is the v5 count, IR. Re-derived |
| D6: register and infinity semantics | 6.1 (deny table and new "Semantics" paragraph); 11 rows 5 and 6; 10.4 S11-56 | Stated per splice: image against the bytes it replaces at H. `register`: REG token set difference. `register-caps`: CAPS less CAPS_OK, only for named edit kinds. `infinity`: multiset difference of normalized INF keys outside NEUTRAL, with the key rule and the A1 rewrite applied to the replaced text. The edit kinds, key rules and rewrite move into a reviewed rule file (B-F2). The landing record lists the line-level matches each splice cancels. S11-56 requires parity with P's recorded 0 | Read from P's verified `edits_check.py`, lines 345-380 (`inf_key`, `static_new`), and from the implementation's draft profile parameters. Not re-measured: the 30 line-level matches are the implementation's count |
| D7: `rule-stale` scoping | 6.2 | Not evaluated on proper ancestors of `recorded_at`; always evaluated on `X`, `C`, `L`, `M` and `recorded_at`. The skipped rules are listed in `result.json`. At `recorded_at`, a missing fingerprint is a lint failure | Textual; matches the implementation's choice and the review's T12 reading |
| D8: source-byte literals | 6.2 ("Matching on source bytes"); 6.5 (W1-b and W2-b) | Every rule literal is matched on source bytes. W2-b's context literal is `\mathrm{SU}(3)`. W1-b's context literal is "isotropy, sublattice structure, link content", with the reason (V7c) | Textual. The review checked both lines' source text |

**W1 option B (D1 and S1-D1).** The full negative list is kept, `finit` included. Each W1-c
fingerprint carries `negative_allowance: {"finit": 1}`. The allowance applies only under all of
these conditions:

- the sentence's sha256 equals the fingerprint's (the exact text);
- the context sha256 equals the fingerprint's (the location), whatever `context_required` says;
- the file is the fingerprint's file;
- the fingerprint grants it once per tree.

Matches beyond the allowance are FAIL `rule-negative-match`. The allowance is never a global count.
Adding, raising or moving an allowance is widening. The new lint clause requires that every
fingerprinted sentence PASSes its own rule at `recorded_at`, and that each allowance equals the
exact literal count in its sentence.

Controls WB1-WB12 cover every case the owner named:

- positive: WB1, and WB8 (shifted by 40 lines);
- the same word added once more: WB2;
- copied elsewhere in scope: WB3;
- copied out of scope: WB4;
- moved: WB5;
- a near-copy with one word changed: WB6;
- word removed: WB7;
- a doubled claim: WB9;
- the lint: WB10 and WB11;
- V7a on W1-c: WB12.

## 2. Implementation defects B1-B6: what the design now specifies

| Item | DESIGN-v5.2 sections | What is specified | Controls |
|---|---|---|---|
| B1: harness result accepted | 5 (acceptance predicate); 6.3 (admission); 10.4; 16.7 | Acceptance requires `config.admission == "chain"`, naming the consumer's `F`, designation record and pin table. `admission` is required in the schema. A harness result is `control-result.json`, with `"harness": true` and `admission: "control-harness"`, never `result.json`, and never acceptable | X11 |
| B2: self-reported delegated evidence | 7.2 (rewritten) | The tool itself runs every delegated and re-execution class, in a disposable full clone at exact `X`, from `F`'s checker blobs, recording blob, command, working directory, exit and result hashes. It reads only results it produced. It re-derives what it can (sc42 bytes, the seven census values, the TeX stamps and path set), and a disagreement is FAIL. Host-run classes read the host API inside the job; `pdf` is bound to `X`'s commit and tree and the artifact hash. Without `F`, never PASS (T4). Locally the class is REVIEW `delegated-evidence-missing`, and the path and its controls run in CI | G4-G8 |
| B3: caller-chosen trust root | 6.3 ("Configuration admission and the root of trust") | `--freeze F` is required. `F`'s owner-designation record is read from `F`'s tree. The configuration and its own review and authorization are admitted only if listed with their sha256 in `F`'s pin table. `retirement.owner` equals the designated owner. `--config-sha256` is an extra equality check, never a root. Files beside the configuration are never admitted | TR1-TR5 |
| B4: `C` not classified; widening reviews | 13.1 (`C`); 6.3 (widening) | Each commit after `X` is classified path by path, as `X` is; a merge commit is `candidate-parent`. A widening review names both blobs, covers every changed item with `accept`, and needs an owner authorization | R16, R17, A12r |
| B5: A1 semantics in the engine | 16.1 (Z9 value set includes adapter companions; guard-pin example); 16.3 (ledger interface `guard_pins`) | Z9 extended to `ledger.json`, `edits.json`, `sitemap.json`, `rows.json`, `sites.json` and every adapter-named file. The guard-pin selection moves into the ledger adapter. The engine reads only interface fields. Allowlisting a colliding value requires an engine enumeration | Z9g (extended), Z9h |
| B6: control predicates and summaries | 10.4 (reporting); 10.3 RT-T, RT-D | Each control record carries `expected`, a predicate equal to it, `actual`, and a status of PASS, FAIL, SKIP or NOT RUN. Summaries count them separately and never count SKIP or NOT RUN as met. RT-T is NOT RUN without records. RT-D tests all 12 lines and the `resid` count. A1r-A11r must emit `record-invalid` through the pipeline. Two-direction controls assert both | (applies to all) |

I verified B1-B6 textually against the review's tables T1-T16 and the cited engine code
(`execution.py` guard-pin block, lines 251-260 at 8c1e628a). No implementation was run.

## 3. Drift findings S2-S7 (addendum): corrections alongside B1-B6

| Finding | DESIGN-v5.2 sections | Specified behaviour | Controls |
|---|---|---|---|
| S2: every reconciliation naming a path `X` changes is `record-invalid` | 13.3 | A record naming a path `X` changes is valid (the "both changed" case). Only a record that changes a decision on `X` is forbidden. The tool runs op C's candidate checks with and without the records and requires identical items on `X` | N2 (re-stated), N3 |
| S6 (serious): a record's `l` skipped the composition check | 13.1 (`L`), 13.3 | The composition is computed for every path on every landing check. A record's `l` is a prediction checked against it, never a substitute. A landing passes only if `L` equals the composition (and the record's `l`, where present). A record naming any other blob gives `landing-conflict-unresolved` and `record-invalid` | N10, N11 |
| S3: class matching by path only | 13.1 (`M`) | Each pinned path matches its class only if its blob at `M` equals the pin. Otherwise `side-change-unclassified` | R18 |
| S4: supersedes checked only for rule files | 6.3 (lint) | For every record kind, `supersedes` must name an existing record blob of the same kind and lineage, at or before `F`. A chain naming a draft or id that never existed as a record is `record-invalid` | S4a |
| S5: R13, R1 and R9 not evaluated | 13.3 | The tool evaluates each checkable condition of a reconciliation record itself, from git objects: ledger binding (the record's R13), commit list (R1), blob at `M` (R2), uniqueness and translation (R3-R5), expected blobs (R6-R8), protected bytes (R9), R10-R12. Any failure means the record does not apply, the path stays `base-drift`, and the failed condition is named | N4-N9 |
| S7: `trial-workflow` defined twice | 13.1 (`M`); 16.6 | One definition per class id across all referenced class records. A duplicate is ERROR `CONFIG_INCONSISTENT` | Z11 |

Verification: textual, against the drift notes' sec. 4 (D9-D12) and sec. 6. The S6 probe and the
record field values are the notes' measurements; I did not re-run them. Drift finding S1 (the draft
`supersedes` naming an off-repository draft) is a records question. It is not a design change, but
the S4 rule makes it `record-invalid` as specified.

## 4. Optional points of the Stage 1 review

| Point | Decision | Reason |
|---|---|---|
| O1: full-sentence examples for W1-c | adopted, in the D1 lint clause (sec. 6.3) | Needed for the self-PASS clause to be tested |
| O3: compare sweep items by `(obligation, class, segment, fingerprint)` | adopted, in D2 | It makes the SW2 predicate precise; it is stricter |
| O5: a context-adjudication PASS control | adopted as K10 (sec. 10.4) | The positive direction of sec. 4.1 row 2 had no control |
| O2, O4, O6, O7, O8 | not adopted; left for the owner | Outside D1-D8, B1-B6 and S2-S7 |

## 5. Unchanged on purpose

These were kept as in v5.1:

- every deny rule and pattern;
- `resid`;
- the context mapping;
- the indicators' definitions;
- the item-7 check;
- the exit codes;
- the ownership chain, apart from admission (B3) and widening (B4).

The figure labels of v5.1 are kept, and one new label, S1, marks figures that the implementation
measured, the Stage 1 review reproduced, and I re-derived. Version history:
`diff DESIGN-v5.1.md DESIGN-v5.2.md` gives 48 hunks before the final two textual fixes (the N2 row
and the R-name clarification in sec. 13.2).

## 6. What I could not follow or verify

- **SW2.** I did not re-run it. Its correction rests on the identity of the 7 sites and on the
  review's 584/584 measurement.
- **The register and infinity parity (S11-56).** It is specified, not measured. The unit of
  comparison is the splice, where P used the edit, and two-step edits are not separately
  addressed. The implementation reproduced P's 0 at splice level. Whether splice and edit units can
  ever disagree is for the reviewer to confirm.
- **The S2-S7 behaviours** are specified from the drift notes. I did not re-run the S6 probe.
- **The designation record's path.** v5.2 says the plan fixes it. The amended plan has to name it;
  this design cannot.
- **Comment ids.** None is held for any owner decision.
