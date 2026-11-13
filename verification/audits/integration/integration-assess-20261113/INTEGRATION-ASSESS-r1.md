# Integration assessment r1: nine draft research PRs of 2026-11-13 (#1169)

**Standing.** Read-only, dependency-aware integration assessment. It proposes landing steps and the
preparatory changes each needs; it makes none of them. It grants no merge authority: each landing
remains a separate owner decision. Landing a record on `main` establishes nothing (§A.46 items 1
and 3); every unit assessed here is a model-written, model-reviewed research record. Nothing below
changes a premise, priority, board entry or scientific status.

**Authority.**
- #1169 comment 6863414487 (`amaybaum`, 2026-11-13T19:58:05Z), item 1: "**Integration
  assessment.** A dependency-aware assessment of the accepted evidence. It prepares the smallest
  landing changes, starting with #1274 and the REC-1 housekeeping. It produces proposals and
  draft-PR updates only. **It grants no merge authority**: each landing remains a separate owner
  decision."
- #1274 comment 6863419164 (`amaybaum`, 2026-11-13T19:58:18Z): "The accepted option-(c) package
  stays **narrowly scoped**. It is T5 part (c) only, as #1169 c.6855167580 fixes it." and "Whether
  to carry the short proofs of T5(a), (b) and (d), and so close gap A1, will be assessed
  **separately**."

**Pins.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`. PR heads as listed in §1, each
fetched by branch name with full history. No branch was written. The REC-1 branch has since moved
to `2594d474` (r9 housekeeping, written in parallel, unreviewed); this assessment reads REC-1 at
`2a9f10ba` as instructed and does not assess r9. G3 unit 2 is likewise being written in parallel and
is not assessed.

***

## 0. Summary

**Proposed landing order (each step a separate owner merge decision, by merge commit):**

1. **#1274** (option-(c) package). Ready once a `STATUS.md` is added, that delta is checked, the
   final head gets its ChatGPT exact-head review and CI, and the owner decides. No dependency on
   another candidate PR.
2. **#1275** (G3 unit 1), independent of every other PR. Needs a §A.42 item 8 table, a status note
   and a green re-run of CI (its only red job failed at "Install elan"). The owner may prefer to
   land it together with unit 2 (owner question OQ-6).
3. **#1269 with the QPHEN r5 subset of #1270**: Q-868-H. Needs recorded SC-42 substitutions (3
   lines), the BRIDGE-UNIT1 gap resolved (land or narrow), the QPHEN r5 gap closed by landing the
   four files #1269 cites, a status note and an exact-head ChatGPT review (the review on file is at
   `acf28d3a`, not the head `ffc9cda4`).
4. **#1268** (REC-1), after r9's focused check and ChatGPT review, and only after the #1267
   (TUNE-1 Step 3A) and #1214 (OICORE-1) support gaps are closed by landing those records or
   narrowed by a forward revision (owner question OQ-2).
5. **#1272** (TUNE-1 sourcing), after #1268 and the #1267 gap.
6. **#1273** (Bell ladder), after #1269 and after the #1231 (Bell-scope) and #1232 (SUBSTATE L3)
   gaps are closed or narrowed; part of the #1232 dependency can be re-pointed to #1274's record
   once it lands.
7. **#1276** (synthesis), last: every unit result it ranks is from steps 1–6.

**Stays on its branch:** #1271 (its verdicts concern the #1230/#1232 drafts at off-`main` commits;
#1274 cites it only as provenance). **Of #1270:** the Q-C2-2 r14b review stays (nothing on `main`
needs it); the rest of the QPHEN chain waits for #1219; the EOI package may land only on an owner
decision (OQ-8), with an SC-42 substitution and a `claims_check` disposition.

**Merge mechanics.** Every PR is add-only, in its own directory; no two PRs touch a common path,
and each merges with current `main` without conflict (`git merge-tree --write-tree`). Each must land
by merge commit, not squash or rebase, because its reviews cite its own branch commits by id.

***

## 1. Objects and mechanical state

| PR | Unit | Head | Directory (under `verification/programmes/`) | Files | Merge with `main` | Local checks at head | CI at head |
|---|---|---|---|---|---|---|---|
| #1274 | option-(c) package | `d015131d` | `oi-qm/reconstruction/intervene-substate-results-20261113/` | 7 A | clean | all pass | green |
| #1268 | REC-1 r8 (+P0 r3) | `2a9f10ba` | `oi-qm/reconstruction/drafts/rec-1-20261113/` | 38 A | clean | all pass | green |
| #1272 | TUNE-1 sourcing r2 | `c539a60c` | `oi-qm/reconstruction/drafts/tune-1-sourcing-20261113/` | 8 A | clean | all pass | green |
| #1273 | Bell ladder r3 | `d8e4f80e` | `oi-qm/reconstruction/drafts/bell-ladder-20261113/` | 12 A | clean | all pass | green |
| #1271 | reconciliation r3 | `703ae20e` | `oi-qm/reconstruction/drafts/reconcile-1230-1232-20261113/` | 7 A | clean | all pass | green |
| #1269 | Q-868-H r3 (+ASSESS-868 r3a) | `ffc9cda4` | `oi-qm/reconstruction/drafts/q868h-20261109/` | 57 A | clean | **SC-42 FAIL** (3 hits) | **red**: SC-42 step |
| #1276 | synthesis r3 | `9eeee392` | `oi-qm/reconstruction/drafts/synthesis-1169-20261113/` | 11 A | clean | all pass | green |
| #1275 | G3 unit 1 r5 | `e81e4fb2` | `gravity/drafts/g3-offset-coupling-20261113/` | 18 A | clean | all pass | **red**: Mathlib bridge, "Install elan" |
| #1270 | recovered evidence | `4cd39871` | `oi-qm/reconstruction/drafts/recovered-1169-20261113/` | 75 A | clean | **SC-42 FAIL** (8 hits), **claims FAIL** (1) | **red**: SC-42 step; release gate |

"Local checks" are `artifact_placement_check`, `claims_check`, `staleness_check`, `voice_check`,
`duplicate_check`, `dependency_label_check --strict`, `legacy_records_check <head>`,
`citation_roles_check <head>`, and the SC-42 integration check compared byte for byte with its
committed result; the same battery on `main` passes (control). Every full 40-hex id each PR adds
resolves to an object in the repository (§A.42 item 3). No added line matches an e-mail, token,
IP-address or local-path pattern (§A.42 item 4; the SC-42 hits are a session-storage word, not a
path prefix). Details in `NOTES-r1.md`.

***

## 2. Dependency graph

### 2.1 Graph

Edges are support edges (a claim of the source uses the target's content). Provenance-only
references are not edges. "[gap]" means the support is off `main` at present.

```
main (c3b5f37a)
 ├── #1274  ── no support edge to another PR; gaps A1 (#1221), D2/D3 (#1232 L3, L2), E2 (#1231 Thm N)
 │             are carried as named conditions (narrowed)
 ├── #1275  ── main only
 ├── #1271  ── [gap] #1230 @ea12fde1, #1232 @86a413c8 (the drafts it reconciles)
 ├── #1270  ── eoi-package: supports ARP-1-MARC precondition 1 on main (cited there as provenance)
 │             qphen chain: [gap-target] for #1219 (off main) and for #1269
 │             EOI files cite FHE-SEL-1 heads cc453774/7d707bb5/83eca7cd [gap, untraced]
 ├── #1269  ── own assess-868-r3a/ (closes on landing); [gap] BRIDGE-UNIT1 (#1211, @820519cf);
 │             [gap] QPHEN r5 texts + REVIEW-PHASE1-r4 (held on #1270's branch)
 ├── #1268  ── [gap] #1267 TUNE-1 Step 3A r3 @8228b3c2; [gap] #1214 OICORE-1 @77226128
 ├── #1272  ── [gap] #1268 (REC-1 r7 rows C6, C9); [gap] #1267 (candidate name, statement (i), :896–905)
 ├── #1273  ── [gap] #1231 (Thm N, N′, Lemma G, NBA); [gap] #1232 (L3, N4); [gap] #1269 (stage-7 illustration)
 └── #1276  ── [gap] #1272, #1268 (P0 r3, r7, r8), #1273 (r3, NOTES-r3), #1274 (NEW-RESULTS);
               transitively #1231, #1232, #1221, #1267
```

Topological order among the nine: {#1274, #1275, #1271, #1270} have no candidate-PR predecessor;
#1269 needs part of #1270; #1268 needs only non-candidates; #1272 needs #1268; #1273 needs #1269
(and non-candidates); #1276 needs #1268, #1272, #1273, #1274.

### 2.2 References by PR (§A.42 item 8, one row per reference)

Classifications are each PR's own where it has a table; "assessor" marks where this assessment
differs or adds one. Content on `main` used as support is omitted unless a PR's classification of it
matters.

**#1274** (`DEPENDENCIES.md`, rows A1–L). Assessor concurs with every row.

| Ref | Content | Classification | Disposition |
|---|---|---|---|
| A1 | APPROX r4a C1–C3 (#1221 @`e41cf613`) for (T5a), (T5b), (T5d) | support off `main` | narrowed: T5(c) stated conditional on (T5a), (T5b), (T5d) as named hypotheses; unconditional headline not asserted |
| A2 | APPROX r4a §4.2 / r2 @`820519cf` (E_f class) | gap closed by self-contained statement | now provenance |
| B | BRIDGE-UNIT1 §5.1 @`820519cf` (FI-1) | support on `main` (`exists_nonMonomial_of_layerFlowExecutable`, ExecSource.lean:52; GR:266) | none |
| C | #1230 @`ea12fde1` | provenance (copied content) | none |
| D1 | #1232 @`86a413c8` | provenance (copied content) | none |
| D2 | #1232 L3 | support off `main` | narrowed (N2 conditional on L3) |
| D3 | #1232 L2, class (a)3 | support off `main` | narrowed (conditional) |
| E1 | #1231 (Sep) | closed by quotation | none |
| E2 | #1231 Theorem N | support off `main` | narrowed with D3 |
| E3, E4 | #1231 O1/O2, F1/O3 | support on `main` (Main:412, :414, :724) | none |
| F | #1233 at `7f80ee6e` (merged) | support on `main` (Main:362) | none |
| G | #1235 | provenance | none |
| H | REC-1 r7 (#1268 @`9f7d2612`) | provenance (vocabulary restated) | none |
| I | #1271 @`703ae20e` (R3:n, RV:n citations) | provenance | none |
| J | ChatGPT reviews 5857985732, 5859960068, 5892291246 | provenance | none |
| K | #1169 c.6854728636, c.6855167580 | governance provenance | none |
| X | generic checks @`86a413c8` | provenance (hand-checked in the package; accepted by REVIEW-r1, CONFIRM-r2 and review 5895564670) | none |
| — (assessor) | own branch commits `1ef60d92`, `4b40dcdc` named in the review files | support on `main` once landed by merge commit | landing mode |

**#1268** (REC-1 r8 §6; r9 adds revision-line rows, unassessed).

| Ref | Used where | Classification |
|---|---|---|
| #1267 3A r3 @`8228b3c2`: Q1/Q2 terms | §1 | support off `main` (gap) |
| #1267 3A rows 36, 37 | rows 36, 37 | support off `main` (gap) |
| #1267 3A:263–266, statement (i) | §3.1 | support off `main` (gap) for its formulation |
| #1267 3A:501 | C6 | support off `main` (gap) for C6's status word |
| #1267 3A, other cited lines (C4; rows 7, 33, 30; row 6; §5 item 2; §4) | as listed | support on `main` or provenance (concur) |
| #1214 OC1 @`77226128`: rows 46, 47 | rows 46, 47 | support off `main` (gap) |
| #1214 OC1:187, :310, :319 | C3 attribution | support off `main` (gap) |
| #1214 OC1:191, :258, :315, :355–358 | C16 | support off `main` (gap) |
| #1214 OC1:194, :313 | C17 | support off `main` (gap) |
| #1214 OC1:190, :314; :359–363 | C15; C11/§4 | support on `main`; provenance (concur) |
| revision-line references r2–r8 (commits `d7f7aac1` … `f0757fdb`, reviews 5890763675, 5890968976, 5892912758), C12 | header | housekeeping item (a): provenance rows owed; r9 in progress |
| own P0 r1–r3 and review files | §4 | in-directory, support on `main` on landing |

**#1272** (§7).

| Ref | Used where | Classification |
|---|---|---|
| REC-1 r7 (#1268 @`9f7d2612`, blob `f1ffac0e`) C6 | part (e) | support off `main` (gap) for the status word "undetermined" |
| REC-1 r7 C9 | N3.3 | support off `main` (gap) |
| REC-1 r7 C4, C11 | N1.4; (b), N3.4 | support on `main` (concur) |
| REC-1 r7 C12, three-way separation | (c); §0 | provenance (concur) |
| #1267 3A @`8228b3c2`: candidate A's name, statement (i) | §1, §2, N0.3, N1.3, N4 | support off `main` (gap) |
| #1267 3A:896–905 | N4 | support off `main` (gap) |
| #1267 3A, other lines | F-S1, F-S2, (e), §1 | provenance (concur) |

**#1273** (§6).

| Ref | Used where | Classification |
|---|---|---|
| BS: #1231 @`e1534b08` (Theorem N, N′, Lemma G, §4 bound, NBA) | stages 5–6, §0 | support off `main` (gap) |
| SB: #1232 @`86a413c8`, L3 | stage 3 | support off `main` (gap) |
| SB N4 (and routes A/B/C, N3) | stage 7, §4 route C | support off `main` (gap); assessor: N3, N4 and the A/B/C classification are carried in #1274's `NEW-RESULTS.md` §5, so after #1274 lands these rows can be re-pointed there (with a check of the Δ wording); L3 cannot (#1274 carries it only as a condition) |
| QH: #1269 @`ffc9cda4`, stage-7 illustration | stage 7 remark | support off `main` (gap); no verdict rests on it |
| QH, stage 4 | stage 4 | provenance |
| RC: REC-1 r7 (#1268 @`9f7d2612`) | vocabulary | provenance |
| reviews on #1231, #1232, #1269, #1268 | input status | provenance |

**#1271** (no table of its own; assessor).

| Ref | Used where | Classification |
|---|---|---|
| #1230 @`ea12fde1` (INTERVENE-1 r2) | §1a per-result verdicts; §2; §5 | support off `main` (gap): the verdicts are about this commit's content |
| #1232 @`86a413c8` (SUBSTATE-BRIDGE-1 r2) | §1b; §2; §5 | support off `main` (gap), as above |
| #1221, BRIDGE @`820519cf`, #1231 | §1, §4 | support off `main` where a verdict uses them (e.g. "parts (a), (b), (d) are in APPROX"); otherwise provenance |
| REC-1 Q2-F/Q2-P vocabulary (#1268) | §5 | provenance |
| `b36bba60` (own branch) | review records | support on `main` on merge-commit landing |

**#1269** (`OBJECTS.md`, "References … not on `main`").

| Ref | Used where | Classification |
|---|---|---|
| ASSESS-868 r3a and REVIEW-868-r3 | Q-868-H definition, Lemma H, w3, J-labels | in this PR's `assess-868-r3a/`; closes on landing |
| BRIDGE-UNIT1 r2–r5, REVIEW-UNIT1 r1–r4 (#1211; @`820519cf`, `handoff-20261109/1211-bridge/`) | ASSESS r3a §2 draft inputs "labelled as hypotheses" | support off `main` (open gap, as recorded) |
| QPHEN r5 SHARED-MECHANISM, QX6, QX4 and REVIEW-PHASE1-r4 (hashes `a7206701…`, `9e9c0d02…`, `7f4cd21d…`, `755c3af0…`) | ASSESS r3a §2 | support off `main` (open gap); the four files are on #1270's branch, hash-matched |
| corpus at `fd539e15` | every source | support on `main` (ancestor); assessor: drift `fd539e15` → `c3b5f37a` is not stated |
| source commit `820519cf` | preservation | provenance |
| Issues #867, #868, #914, #1147, #1169 and comments | authority, scope | provenance |

**#1276** (§8). Concur with every row; the gap rows are: TS r2 (#1272), P0 r3, R7, R8 (#1268),
BL r3 and NOTES-r3 (#1273), OC `NEW-RESULTS.md` blob `1859e8c5` (#1274), BS Theorem N/N′ (#1231),
SB L3 (#1232), APPROX r4a (#1221), TUNE-1 Step 3A (#1267, through TS). All review, owner and
planning references are provenance.

**#1275** (no item 8 table; assessor). Every cited source is on `main` at `c3b5f37a` (GR, Main,
SM, Introduction, book ch07, OIBridge, W1-1 r4, `corpus-consistency-20261026/AUDIT.md`, frozen
`ROADMAP.md`). Its own review commits (`e64b9a3c`, `1aaf87a2`, `b207fbaa`, `e0383e50`, and the
review-file commits named in the header) are support on `main` once it lands by merge commit;
#873 c.6859060590 and c.6859687612 are governance provenance; §7 literature is recalled context.
No gap; the table is owed only because §A.42 item 8 requires the trace before landing.

**#1270** (`README.md`, which states "The references the files make were not each traced").

| Ref | Classification (assessor) |
|---|---|
| ARP-1-MARC preregistration.md:124, :885; receipt line 46 (on `main`) | support on `main` for the README's "cited on `main`" statement |
| FHE-SEL-1 heads `cc453774`, `7d707bb5`, `83eca7cd` (in PACKAGE r2/r3, REVIEW-PACKAGE, GATE-DRAFT) | untraced; the package itself classes them "support off `main` (gap)" (PACKAGE.md:413) |
| #1219 @`4c7f3f86` (hash targets of the QPHEN chain) | support off `main` for the "46 of 46 match" verification statement |
| `820519cf`, `44f7c328`/`c9d14e11`, `f1336264`/`f634f8e3`, `d87547a4` and ancestors | provenance (pointers) |
| the "minimal set" and "reporting gate" owner decisions, "as relayed …; no GitHub record of it was read here" | governance: not quoted with author and time (§A.42 item 7) |

***

## 3. Landing readiness, per PR

### #1274 option-(c) package — **ready after preparation**

- **Reviews.** Independent REVIEW-r1 ACCEPT WITH CHANGES at `1ef60d92`; CONFIRM-r2 ACCEPT at
  `4b40dcdc`; ChatGPT review 5895564670 ACCEPT at the exact head `d015131d` ("ACCEPT as a scoped
  research-evidence package, with separate integration gates").
- **Gates (review 5895564670).**
  1. The [A]/[X] and [L] support labels stay on any `main` record; model ACCEPT is not
     verification; Dynkin's π–λ theorem is imported standard mathematics, not formalized.
     *Status:* met in `NEW-RESULTS.md` (Standing, evidence tags). Keep the file unchanged.
  2. Merge-time CI and mergeability, and a current owner integration decision; the #1230/#1232
     draft approvals were not recovered, and the option-(c) writer authorization is not a
     retrospective authorization of those drafts or permission to merge them. *Status:* CI green,
     merges clean; owner decision outstanding; `PROVENANCE.md` §4 records the authorization gap.
  3. No upgrade of the Q2-A / upper-bound classifications into a physical mechanism, Bell escape or
     OI↔QM result; AW-OA2-1 stays stopped. *Status:* met in the text; the status note must not
     add any.
- **Item 8.** No open gap; four gaps carried as named conditions (A1, D2, D3, E2).
- **§A.46 item 2.** Lands as the evidence for the scoped results it states (the basis #1265 used for
  OA-1 to OA-3), and it is the record #1273 and #1276 need to replace their #1232 support rows
  (N3, N4, A/B/C, G1/E2, L4, S7) by support on `main`. The owner chose option (c) as "a minimal
  landing package" (#1169 c.6854728636).
- **§A.36.** `oi-qm/reconstruction/intervene-substate-results-20261113/`: a new directory under the
  reconstruction family; compliant.
- **Superseded lines** (drafting history, to be listed in the status note, not edited):
  `PROVENANCE.md`:100 ("Nothing was committed, pushed or posted in producing the package");
  `DEPENDENCIES.md` row H ("the branch head is `cd38655c` at this writing"; it is `2594d474`, and
  `REC-1-r7.md` is still blob `f1ffac0e`); rows A1, C, D1, E1, I ("open, draft"), states at writing.
- **Do not apply the optional nit** (DEPENDENCIES.md:18): #1276 cites `DEPENDENCIES.md` by blob
  `6c127b0a` and `NEW-RESULTS.md` by blob `1859e8c5`; changing either breaks those pins. Put any
  wording note in the status file.

### #1268 REC-1 — **must wait**

- **Reviews.** Independent reviews and confirmations for r1–r8 and P0 r1–r3 in the directory
  (REVIEW-r8 ACCEPT; P0 CONFIRM-r3 ACCEPT); ChatGPT 5896999901 at the exact head `2a9f10ba`: "ACCEPT
  r8's narrow L-reading reconciliation as paper-only; two separate housekeeping items remain before
  any integration." Earlier ChatGPT reviews at `1fd0c241`, `6de32c95`, `9f7d2612`, `cd38655c`.
- **Gates.** (a) item 8 provenance rows for the revision-line references r2–r8 and C12; (b) the
  stale P5 at r8:367. Both authorized (#1268 c.6863418087) and being written as r9 (`2594d474`),
  which needs its focused check and a ChatGPT exact-head review. (c) The #1214 and #1267 support
  gaps (review 5896999901: "Existing #1214/#1267 off-main support gaps remain integration gates");
  r8:462–463 bars landing while they remain.
- **§A.46 item 2.** Needed by #1272 (C6, C9) and #1276 (P0 r3, r7, r8) as support; not by anything on
  `main`.
- **§A.36.** `drafts/rec-1-20261113/`: compliant (precedent: `drafts/tune-1-20261111/` on `main`).
- **Status lines.** `REC-1-P0-r3.md`:11 reads "WIP / UNVERIFIED … unreviewed" though CONFIRM-r3 is
  committed; to be listed as superseded in the status note.

### #1272 TUNE-1 sourcing — **must wait**

- **Reviews.** REVIEW-r1 ACCEPT WITH CHANGES; CONFIRM-r2 confirmed; ChatGPT 5892912253 ACCEPT at the
  exact head `c539a60c`.
- **Gates.** Review: "Any eventual landing needs its own dependency/CI/integration gate." The
  record's own rule (§7): each "support off `main`" row is closed by landing its source or narrowed.
  Open: REC-1 r7 C6, C9 (#1268) and #1267 (candidate name, statement (i), :896–905).
- **§A.46 item 2.** Needed by #1276 (MM-1); nothing on `main` needs it.
- **§A.36.** Compliant (TUNE-1 family under `drafts/`).
- **Status lines.** `TUNE-1-SOURCING-r2.md`:8 "WIP / UNVERIFIED author record … Independent non-author
  review, then ChatGPT review at the exact head, are the next steps": superseded.

### #1273 Bell ladder — **must wait**

- **Reviews.** REVIEW-r1 ACCEPT WITH CHANGES; CONFIRM-r2 ACCEPT WITH CHANGES; CONFIRM-r3 ACCEPT;
  ChatGPT 5892919040 at the exact head `d8e4f80e`: "ACCEPT AS A CONDITIONAL PAPER RESULT, with two
  integration safeguards."
- **Gates.** Safeguard 1: (xiv) is not silently equated with MI* over generator residues. Safeguard
  2: "complete record" is all records the embedded wing can hold or obtain in the declared window,
  heralds and failures included, in a fixed region independent of the settings. The owner adopted
  both as Q2 and Q4 (#1273 c.6860580909), with Q1 (vii) as a conditional ledger posit and Q3. r3
  already reads (xiv) as MI* only conditionally (r3:79–81) and states AL4's fixed regions; the
  status note should quote Q1–Q4 so the record carries them. Item 8 gaps: #1231, #1232 L3/N4, #1269.
- **§A.46 item 2.** Needed by #1276; nothing on `main` needs it.
- **§A.36.** Compliant.
- **Status lines.** r3:3–5 "WIP / UNVERIFIED … pending ChatGPT review at the exact head": superseded.

### #1271 reconciliation — **stays on its branch**

- **Reviews.** REVIEW-r1 ACCEPT WITH CHANGES; CONFIRM-r2 ACCEPT WITH CHANGES; ChatGPT 5892291246
  ACCEPT WITH INTEGRATION NITS at the exact head `703ae20e`. Both nits are answered in #1274's
  `PROVENANCE.md` §4–§5.
- **Item 8.** No table of its own; its verdicts are about the #1230/#1232 drafts at off-`main`
  commits, so landing it alone leaves those as gaps (§A.42 item 8: a verdict that depends on
  commits uses them).
- **§A.46 item 2.** Not needed: #1274 cites it only as provenance and restates every result it
  carries; nothing on `main` depends on it.
- **Status lines.** R3:3–6 "Nothing was committed … not yet on any branch" (historical, per #1274
  `PROVENANCE.md` §5).

### #1269 Q-868-H — **needs preparation; land with the QPHEN r5 subset of #1270**

- **Reviews.** r1 REVISE (narrow); r2 ACCEPT WITH CHANGES; CONFIRM-r3 ACCEPT; ChatGPT 5891666660
  ACCEPT WITH DOCUMENTATION NITS at `acf28d3a`. The head `ffc9cda4` adds the two nit commits
  (`3031011b`, `ffc9cda4`); no ChatGPT review is at the head.
- **Gates (review 5891666660).** Nit 1 (header status): applied at `3031011b`. Nit 2 (§10
  "second run is byte-identical"): narrowed at `3031011b`. "A separate integration decision is
  needed, together with §A.42 dependency and record-retention checks."
- **CI.** SC-42 added-text scan: 3 hits (`assess-868-r3a/ASSESS-868.md`:142, :151;
  `assess-868-r3a/review/REVIEW-868-r3.md`:67), each a session-storage word inside preserved bytes.
- **Item 8.** Open: BRIDGE-UNIT1 (#1211) and the QPHEN r5 texts (see §2.2).
- **§A.46 item 2.** Needed by #1273 (stage-7 illustration, a gap row); ASSESS-868 r3a is the input
  of an owner-accepted unit (#868 c.6742050189).
- **§A.36.** Compliant; ASSESS-868 r3a sits beside the unit that uses it.
- **Status lines.** `OBJECTS.md`:3 "WIP / UNVERIFIED research record, not for merge"; its "Status"
  bullet describing r2 as at `Q868H-UNIT1.md` "until r3": to be read with the r3 section.

### #1276 synthesis — **lands last**

- **Reviews.** REVIEW-r1 ACCEPT WITH CHANGES; CONFIRM-r2 ACCEPT WITH CHANGES (small); CONFIRM-r3
  ACCEPT; ChatGPT 5896999231 ACCEPT at the exact head `9eeee392`. Owner SQ8 (#1169 c.6863414487):
  §1's metric is the **descriptive** ranking with both sensitivities beside it, not a board change.
- **Gates.** §8: every "support off `main`" row closed or narrowed before landing; review: "The support
  from #1268/#1272/#1273/#1274 remains off main."
- **§A.46 item 2.** Nothing on `main` needs it; it is the evidence for its own ranking claim once its
  inputs are on `main`.
- **§A.36.** Compliant.
- **Status lines.** r3:3–8 "WIP / UNVERIFIED author record … The next steps are …": superseded.

### #1275 G3 unit 1 — **ready after preparation** (independent)

- **Reviews.** REVIEW-r1 REVISE; REVIEW-r2 REVISE; CONFIRM-r3 not confirmed; CONFIRM-r4 CONFIRMED
  (D-1 to D-3 applied in r5); ChatGPT 5896999577 at the exact head `e81e4fb2`: "ACCEPT as a
  conditional, paper-only source-map/coupling audit, not as a proof of dynamical zero-point
  decoupling."
- **Gates (review).** The exclusion of the convention-fixed coupling under (ii-L) is a reading of
  GR:346's order-of-derivation argument, not a no-fixed-point theorem; GR:400 is reconciled only
  conditional on §8.3; neither is promoted. Q7: (ii-L) not adopted as a §A.29 premise. Q8: the
  AW-loop wording gap goes to a separately authorized manuscript correction.
- **CI.** Mathlib bridge failed at "Install elan" and the Lean steps after it; the release-gate
  checks pass locally. A re-run is needed.
- **Item 8.** No gap; no table (owed, see §2.2).
- **§A.46 item 2.** Evidence for its scoped findings; also the record a later manuscript correction
  (F5, F7, AW-loop, AW-G12) would need on `main` (§A.42 item 2).
- **§A.36.** `verification/programmes/gravity/` does not exist on `main`; a new programme directory
  is permitted ("A round whose category is genuinely new adds a directory"). Compliant; see OQ-6.
- **Status lines.** None found in r5.

### #1270 recovered evidence — **split; most must wait**

- **Reviews.** None: no independent review file, no ChatGPT review.
- **Gates.** The PR body lists its expected CI failures. The README states that its item-8
  references "were not each traced".
- **CI.** SC-42: 8 hits in 6 files (7 in `eoi-package/`, 1 in
  `qphen-review-chain/review/REVIEW-PHASE1-r4.md`); `claims_check`: 1 (`eoi-package/eoi-audit/AUDIT-C5.md`:149).
- **§A.46 item 2, per part.**
  - `eoi-package/` (16): supports the interpretation of ARP-1-MARC precondition 1 on `main`
    (preregistration.md:885), but ARP-1-MARC classes the package as provenance
    (preregistration.md:124), so no `main` record has an item 8 gap without it. Owner question OQ-8.
  - `qphen-review-chain/` (46): four files are needed by #1269; the rest support #1219 (off `main`).
  - `qc22-r14b-review/` (11): "Cited on `main`: nothing"; needed only when Q-C2-2 resumes. §A.42
    item 5 (necessity, not exposure): stays on the branch.
- **§A.36.** The directory is acceptable: the EOI package cannot go into ARP-1-MARC's record
  directory, which `v3_verifier --receipts` (G13) freezes. The QPHEN files belong with
  `qphen-phase1-20261109/` if #1219 lands; the four #1269 needs could sit beside #1269 (OQ-7).
- **Authority.** The "minimal set" and "reporting gate" decisions are relayed, with no GitHub record
  quoted (§A.42 item 7). The README leaves open whether #1169 c.6852816462 item 2 covers the QPHEN
  chain.

***

## 4. Landing order and preparatory changes

Every step: add-only files; no change to any reviewed text; landing by merge commit; current CI
green at the final head; a ChatGPT exact-head review of the final head; a separate owner merge
decision. Main at `c3b5f37a` is the base for all nine; if `main` moves, re-run
`git merge-tree --write-tree origin/main <head>` and the local battery (§1) first, because no PR
touches another's paths.

### Step 1. #1274

Preparatory changes, on `research/optc-1230-1232-20261113`, one commit:

1. Add `intervene-substate-results-20261113/STATUS.md` (pattern of `oa-1-20261112/STATUS.md`):
   - **Accepted record and reviews:** `NEW-RESULTS.md` blob `1859e8c5…` and `DEPENDENCIES.md` blob
     `6c127b0a…` as at `d015131d`; REVIEW-r1 (ACCEPT WITH CHANGES, `1ef60d92`), CONFIRM-r2 (ACCEPT,
     `4b40dcdc`), ChatGPT review 5895564670 (ACCEPT, `d015131d`); all model reviews, not
     verification (§A.46 item 7).
   - **Authority, quoted with author and time:** #1169 c.6854728636, c.6855167580; #1274
     c.6863419164 (narrow scope: T5 part (c) only); #1169 c.6863414487 (assessment; no merge
     authority).
   - **What the record establishes**, in the labels already in `NEW-RESULTS.md` (paper arguments
     [A], conditional; [X] provenance; [L] Dynkin π–λ imported). A one-sentence "claim supported by
     this record". No added wording beyond the record (review gate 3).
   - **Not established:** T5's unconditional headline (A1); N2's necessity (D2); SLL's exclusion
     consequence (D3, E2); any physical operation; the #1230/#1232 drafts themselves.
   - **Dependencies:** a pointer to `DEPENDENCIES.md`, with one added row: own branch commits
     `1ef60d92`, `4b40dcdc`: support on `main` once landed by merge commit.
   - **Source drift:** none (`c3b5f37a` is current `main`).
   - **Superseded lines:** `PROVENANCE.md`:100; `DEPENDENCIES.md` row H (branch head now
     `2594d474`; `REC-1-r7.md` unchanged, blob `f1ffac0e`); "open, draft" states at writing (rows
     A1, C, D1, E1, I).
   - **Integration requirements** of review 5895564670, items 1–3, with how each is met, including
     that the #1230/#1232 draft approvals were not recovered and are not supplied by this landing.
   - **Landing:** mode merge commit; basis §A.46 item 2; accountable Issue #1169; T5(a), (b), (d)
     assessed separately (#1274 c.6863419164).
2. Keep `NEW-RESULTS.md`, `DEPENDENCIES.md`, `PROVENANCE.md`, `CHANGES.md` and `review/` unchanged.
3. Update the PR title and body (drop "(WIP)").
4. A focused independent check of the `STATUS.md` delta, then a ChatGPT exact-head review.

### Step 2. #1275 (any time; independent)

1. Add `g3-offset-coupling-20261113/STATUS.md`: accepted text r5 (blob `816f91a2`), review trail
   (REVIEW-r1, REVIEW-r2, CONFIRM-r3, CONFIRM-r4, ChatGPT 5896999577); authority #873 c.6859060590,
   c.6859687612 with author and time; the review's "Important limit" paragraph as the scope; the
   §A.42 item 8 table of §2.2 above; the owner's Q4/Q7/Q8 answers only if recorded on #873 (unit 2(a)
   is recorded on #873 per #1169 c.6863414487); landing mode merge commit.
2. Re-run CI at the new head; Mathlib bridge must be green.
3. Focused check of the status delta; ChatGPT exact-head review; owner decision (OQ-6: now, or with
   unit 2).

### Step 3. #1269 with four files of #1270

1. **SC-42.** Recorded substitution on the three lines (`assess-868-r3a/ASSESS-868.md`:142, :151;
   `assess-868-r3a/review/REVIEW-868-r3.md`:67), replacing the barred session-storage word with
   `working`, as #1265 (`739595fa`) and #1271 did; `OBJECTS.md` gains a "Committed bytes differ
   from the preserved source" section with each file's source blob and SHA-256, committed blob and
   SHA-256, changed lines, rule, and a statement that restoring the word reproduces the source bytes.
   OQ-4: or keep the bytes and change the check.
2. **QPHEN r5 gap.** Land the four hash-matched files (`r5/SHARED-MECHANISM.md`,
   `r5/QX6-BELL-CHSH.md`, `r5/QX4-INCOMPATIBILITY-LG.md`, `review/REVIEW-PHASE1-r4.md`; the last
   carries one SC-42 hit at line 20, same substitution) either by landing #1270's
   `qphen-review-chain/` subset first or by copying them beside #1269 with their source recorded
   (OQ-7).
3. **BRIDGE-UNIT1 gap.** Either land the cited BRIDGE-UNIT1 r2–r5 and REVIEW-UNIT1 r1–r4 files
   (hash-matched at `820519cf`, `handoff-20261109/1211-bridge/`), or state in the status note that
   ASSESS r3a uses them only as hypotheses and that Q-868-H's verdicts are conditional on them
   (narrowing); OQ-5.
4. **Status note** (`STATUS.md`): review trail including that ChatGPT 5891666660 is at `acf28d3a`
   and the head adds only the nit commits; owner records #868 c.6742050189, c.6853568040 and #1169
   c.6852816462 with author and time; the drift `fd539e15` → `main` for the cited sources (to be
   measured, as OA-1's STATUS does); superseded line `OBJECTS.md`:3.
5. ChatGPT exact-head review of the final head; CI green.

### Step 4. #1268 REC-1

1. r9 (in progress, `2594d474`): focused independent check; ChatGPT exact-head review.
2. Close the #1267 and #1214 gaps, by one of (OQ-2):
   - (a) landing #1267 (Step 3A r3; ChatGPT 5887947616 ACCEPT WITH SCOPE QUALIFICATIONS at
     `8228b3c2`) and #1214 (OICORE-1; no ChatGPT review on the PR), each after its own assessment
     with this one's checks; or
   - (b) a forward revision r10 that narrows each gap row (§1 Q1/Q2 terms; rows 36, 37, 46, 47;
     §3.1 statement (i); C3, C6, C16, C17) to a conditional or context-only statement.
3. `STATUS.md`: accepted texts (r9 or r10 and P0 r3, by blob), the full review trail with the five
   ChatGPT reviews and their heads, owner records (#1169 c.6850732002, c.6848080209, c.6848268369,
   c.6854241002, c.6854774010; #1268 c.6860582570, c.6863418087) with author and time; superseded
   lines (`REC-1-P0-r3.md`:11; r8:462–463 once the gaps are closed); §5's proposals restated as
   unapplied; landing mode merge commit.
4. ChatGPT exact-head review; owner decision.

### Step 5. #1272

1. After step 4 the REC-1 r7 rows become support on `main` ([R]): `REC-1-r7.md` is blob `f1ffac0e`
   at `9f7d2612`, `2a9f10ba` and `2594d474`. State this re-classification in the status note.
2. Close or narrow the #1267 rows (follows from step 4's choice).
3. `STATUS.md`: accepted text r2 (blob `35c5c116`), reviews, authority (#1169 c.6854241002 item 1;
   c.6854774010; c.6848268369; #1236 c.6817129920), superseded line r2:8–11.
4. ChatGPT exact-head review; owner decision.

### Step 6. #1273

1. After step 1, re-point the SB rows for N3, N4 and routes A/B/C to #1274's `NEW-RESULTS.md` §5
   (support on `main`, [A]), after checking that the Δ wording there does not change what the ladder
   uses; L3 stays a gap.
2. After step 3, the QH row becomes support on `main`.
3. Close or narrow #1231 (Theorem N/N′, Lemma G, NBA) and #1232 L3: land those records after their
   own assessment, or state stages 5–6 and stage 3's directed form as conditional on them (OQ-3).
4. `STATUS.md`: accepted text r3 (blob `0298088d`), reviews, owner #868 c.6854708572, #1169
   c.6854728636, #1273 c.6860580909 (Q1–Q4 quoted), the two safeguards; superseded lines r3:3–5.
5. ChatGPT exact-head review; owner decision.

### Step 7. #1276

1. After steps 1, 4, 5, 6, each input row of §8 becomes support on `main`; check that every cited blob
   is unchanged on `main` (`611a4d9a`, `f1ffac0e`, `615b7de8`, `35c5c116`, `0298088d`, `963d7352`,
   `1859e8c5`, `6c127b0a`) and that r9 changes no row it uses.
2. Remaining transitive gaps (#1231, #1232 L3, #1221, #1267) follow steps 4–6's choices; narrow the
   affected MM entries if those records do not land.
3. `STATUS.md`: SQ8 decision (descriptive ranking, both sensitivities, not a planning change),
   reviews, authority #1169 c.6860584645; superseded r3:3–8.
4. ChatGPT exact-head review; owner decision.

***

## 5. What must not land, or must wait

| PR / part | Disposition | Reason |
|---|---|---|
| #1268 | wait | #1214 and #1267 support gaps (review 5896999901; r8:462–463); r9 unchecked |
| #1272 | wait | gaps on #1268 (C6, C9) and #1267 |
| #1273 | wait | gaps on #1231, #1232 (L3, N4) and #1269 |
| #1276 | wait (last) | every ranked input is off `main` |
| #1269 | wait for preparation | CI red (SC-42); BRIDGE-UNIT1 and QPHEN r5 gaps; no exact-head ChatGPT review at `ffc9cda4` |
| #1271 | stays on branch | verdicts about off-`main` drafts; provenance for #1274 only; no table |
| #1270 `qc22-r14b-review/` | stays on branch | nothing on `main` cites it; §A.42 item 5 |
| #1270 `qphen-review-chain/` except the four #1269 files | wait for #1219 | supports an off-`main` frozen record only |
| #1270 `eoi-package/` | owner decision (OQ-8) | no `main` gap needs it; CI red (7 SC-42 hits, 1 `claims_check` hit); no review; item 8 untraced |
| #1270 as a whole | must not land as is | no review; CI red; untraced references; relayed owner decisions not quoted |
| any PR by squash or rebase | must not | reviews cite branch commits that must stay reachable from `main` |

***

## 6. Disposition notes

- **Integration is not promotion.** No landing proposed here establishes a claim (§A.46 item 1:
  model reviews only; nothing kernel-checked beyond the [K] statements already on `main`). Each
  status note keeps the record's own labels and adds none.
- **§A.25 flags (landing needs no manuscript edit; these are follow-ons for separately authorized
  units):**
  - #1275 F5 / AW-abs: GR:426 attributes ρ_s = ρ_crit to "Jacobson's Clausius relation"; the record
    computes 2ρ_crit for the integrated Clausius energy. A correction would need the corpus grep:
    the attribution appears only at GR:426; SM:182 states ρ_s = ρ_crit by boundary-entropy
    concordance and would be checked; no book mirror of the GR:426 sentence was found.
  - #1275 F7: `OIBridge/BohrFrequency.lean`:8–9 name `shift_normSq` and `reflect_normSq`; the
    declarations are `shift_modsq` and `reflect_modsq`. A kernel-tree docstring change, outside
    manuscript propagation.
  - #1275 AW-loop and AW-G12: GR:346 vs GR:358/:374/:400, and GR:12's clause; the review routes
    AW-loop to a separately authorized manuscript correction (Q8). `book/ch07-gravity.md`:183–187
    and its `FULL.md` mirror state requirement (ii) and would be in scope.
  - #1268 AW-P0-2: OA-2 E(b) step 4 and OA-3 N4.3 step 4 presume singleton indicators under C-PM.
    These are records on `main`. If accepted, their mutable `STATUS.md` notes would carry it
    (§A.46 item 4); the #1276 review advises independent read-only scrutiny first (SQ4). No change
    at landing.
  - #1273 Q1 labels ledger (vii) a conditional ledger posit. Main:724 lists (vii) as a posit, so no
    change appears needed; #1276 names the status word for (vii) among its cross-unit tensions T1–T7; any manuscript wording change would be its own unit.
  - #1274, #1272, #1271, #1269, #1270: none found.
- **Correctness bands:** unchanged by any landing (consistency axis, §A.23).

***

## 7. Owner questions

- **OQ-1 (#1274).** Approve the step-1 preparation (a `STATUS.md` only, reviewed texts unchanged,
  optional nit not applied because #1276 pins the blob)?
- **OQ-2 (#1268).** Close the #1267/#1214 gaps by landing those records (each needs its own
  assessment; #1214 has no exact-head ChatGPT review on its PR) or by a narrowing r10?
- **OQ-3 (#1273).** Same choice for #1231 (Theorem N/N′) and #1232 L3: land the drafts (with what
  review) or state stages 3 and 5–6 conditional on them?
- **OQ-4 (#1269, #1270).** For the SC-42 hits in preserved bytes: recorded substitution (the #1265
  and #1271 precedent), or an exemption in the check? For #1270's `claims_check` hit: an
  `EXEMPTIONS` entry (a tool change, own decision) or a recorded substitution?
- **OQ-5 (#1269).** BRIDGE-UNIT1 r2–r5 and its reviews: land them beside ASSESS-868, or narrow
  Q-868-H's dependence to a stated hypothesis?
- **OQ-6 (#1275).** Land G3 unit 1 now, or with unit 2? Is a new `verification/programmes/gravity/`
  programme the intended home?
- **OQ-7 (#1270 → #1269).** Land the four QPHEN files #1269 needs from #1270's directory, or beside
  #1269? Does #1169 c.6852816462 item 2 cover the QPHEN chain at all (the README leaves this open)?
- **OQ-8 (#1270).** Land the EOI package (owner-accepted 2026-11-08, cited by ARP-1-MARC as
  provenance), or keep it on its branch? If landed: a review, the item 8 trace of its FHE-SEL-1
  references, a GitHub record of the minimal-set decision, and OQ-4.
- **OQ-9 (T5(a), (b), (d)).** For the separate assessment: carry the short proofs (INTERVENE
  I:159–168, I:179) in a follow-on package, or land #1221 (APPROX r4a C1–C3)? Either closes gap A1
  only for the research record, not as an established claim.
