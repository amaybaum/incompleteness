# Inventory of design v6.0d against v5.5.9

Paper-only. Inputs verified by sha256 before use and not modified:

| Input | sha256 |
|---|---|
| `DESIGN-v6.0c.md` (draft corrected by v6.0d) | dd72ee5b9f1ed3718b5f1584bf88b957dbb481b0c9ac9dca3d6ff784389aa594 |
| `review-v6.0c/review.md` (ACCEPT-WITH-NITS; O-4, R-a to R-e) | 48dd41d0c0cc8b9169f61377eec7c606170b1fc6b7bb5c9aef0b5e7d4010ad20 |
| `DESIGN-v6.0b.md` (draft corrected by v6.0c) | f87dd8bee2c0a9d20beaf462351245f4735eaf056ad0485616fe391dacceb452 |
| `review-v6.0b/review.md` (ACCEPT-WITH-NITS; Q-1, O-1, N-a to N-h) | 0c41ec5aa395e7971665b156275fbffdb3fee05a283459d11a4bcf0b4a3445aa |
| `DESIGN-v6.0a.md` (draft corrected by v6.0b) | 105db5efe8803876107e525f868051593227f0cc20f0bd2fb7600ea312113585 |
| `review-v6.0a/review.md` (REJECT, R-1) | f5f4f57b6c028f0b995984be74be0c1a799e9cd3875dc4c82097a9a0167e9f2a |
| `DESIGN-v6.0.md` (draft corrected by v6.0a) | 5d4ddf784164c496d98b3194030524b20353cfcd5695fbf102eae68ced85e145 |
| `review-v6.0/review.md` (REJECT, B-1 to B-4) | 43cfe728198588eb4f01a38dd817f4d207e50494bb98c5bb20c895df4fddb0ec |
| `DESIGN-v5.5.9.md` (adopted) | cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 |
| `DESIGN-v5.5.10a.md` (unadopted; technical content of the verified reader only) | b7e45218d27a2ab2a36f6b3f837e07ea04f3df88d04120733e9487c0a3cf1ee2 |
| `review-v5.5.10/review.md` | 78dc33d3a99405cbb7150de77ad1550495643f4f3121f51795bd0312fc897a8c |
| `review-v5.5.10a/review.md` | f8eeb9c25c5dc47dd990717d4fa4a0187a0bbfb52993bb5e42fa340c5b32cd51 |
| `coord2-gitrest/FEASIBILITY.md` | f1bb95c782e5c11123cba3b2b22c68bce6d7b19a3e088de06ace1596db916b91 |
| `coord2-q10/DISPOSITION.md` | 7ae4448024bd04256cf585b722f4b97a2a9ba3dc9b449ad40fc4865bd9345f89 |
| `coord2-q10/OWNER-DECISION-20261124.md` | 39521663157964a9e227b952a32bb6cd9efed96202c647a6da5fa535754b423b |
| `impl-stage1-s1/CORRECTION-Q10.md` | 44fb8665e7f1ab3663ed0a742e713208c6688fd458e5056abbfbe24c49830c86 |
| implementation worktree `coord2-impl-wt` | commit 443e871f225a414f69bef3f1e3cab45cb30d6594 |
| `AGENTS.md` at `main` 9deb69568d8231210c7f39cb65be943dea566371 | 43a28e2653843e8a8ba87e38778cacd6815b71ee54d7977af945303d1783ce27 |
| frozen A1 plan `P` | commit 4c79be642ca631573f06b444903be75ec4f5e2b6 |

`DESIGN-v6.0d.md` was built from v6.0c by exact, once-only replacements (`work-v60d/apply_d.py`);
v6.0c was built from v6.0b by `work-v60c/apply_c.py` (parts in `work-v60c/parts/`, rows in
`work-v60c/rows.py`); v6.0b was built from v6.0a
by `work-v60b/apply_b.py`, v6.0a from v6.0 by `work-v60a/apply_a.py`, and v6.0 from v5.5.9 by
`work-v60/apply.py`. Every row status in table 2 is computed by comparing each v5.5.9 table row with
the v6.0d file line for line (`work-v60d/inventory.py`). The changes from v6.0c are mapped hunk by
hunk in `CHANGES-v6.0d.md`.
"Retained" means byte-identical; "modified" means present with changed text; "removed" means absent.

Wording (coordinator's relay of the owner, 2026-11-24): "the tool verifies which exact plan was
executed; the owner confirms that it was the approved plan. The tool itself makes no claim about
authorization." Every passage of v6.0 on exact-commit binding, outputs, outcomes and scope was
written to that rule. In v6.0a the rule is stated once normatively (sec. 1), and the output's class
names carry a fixed meaning table (sec. 5, "Class meanings"; review B-4).

## 1. Sections of v5.5.9

| v5.5.9 heading | Status | Reason |
|---|---|---|
| # Commit-independent ledger and terminology verification tool: design v5.5.9 | modified | title: version label |
| ## Status and authority | modified | rewritten for v6.0 (owner decisions, scope, procedural approval); history kept in v5.5.9 |
| ## Notation | modified | see 1a |
| ## 0. Traceability | retained | unchanged |
| ### 0.1 Owner acceptance conditions | modified | see 1a |
| ### 0.2 Review changes | modified | see 1a |
| ### 0.3 Figures | retained | unchanged |
| ## 1. Purpose, non-goals and residual limits | modified | see 1a |
| ## 2. Pipeline and subject kinds | retained | unchanged |
| ### 2.1 Pipeline stages | modified | see 1a |
| ### 2.2 Subject kinds | retained | unchanged |
| ### 2.3 Operations | retained | unchanged |
| ### 2.4 Ledger fields | retained | unchanged |
| ## 3. Historical provenance obligation `HP` (segment E..H) | retained | unchanged |
| ### 3.1 Pinned merges | retained | unchanged |
| ### 3.2 Region definition (independent of any diff algorithm) | retained | unchanged |
| ### 3.3 HP adjudication record (schema `oi-hp-adjudication/1`) | retained | unchanged |
| ### 3.4 Resumed tracking and HP/RET overlap | retained | unchanged |
| ### 3.5 Context changes in E..H | retained | unchanged |
| ## 4. Preregistered context rule | retained | unchanged |
| ### 4.1 Decision | retained | unchanged |
| ### 4.2 S0 indicators: exact definitions (R10) | retained | unchanged |
| ### 4.3 Indicator effects | retained | unchanged |
| ### 4.4 The real-tree cases at T1' | retained | unchanged |
| ## 5. Outcomes, exit codes and output | modified | see 1a |
| ## 6. Profiles, rules and record lint | retained | unchanged |
| ### 6.1 Scan profiles | retained | unchanged |
| ### 6.2 Rule schema `oi-term-rules/2` | modified | see 1a |
| ### 6.3 Records, review records, owner authorization and lint (R11, D4) | modified | renamed and rewritten: see 1a |
| ### 6.4 Deny rules DR-1, DR-3, DR-4, DR-5 (for independent review; measured in sec. 14) | retained | unchanged |
| ### 6.4.1 Rejected candidates DR-1d and DR-2 (history) | retained | unchanged |
| ### 6.5 Seed allow rules W1 and W2 (for review; not adopted) | retained | unchanged |
| ### 6.6 Residual review profile `resid` (widened in v5; for independent review) | retained | unchanged |
| ## 7. Delegation contract `delegation.json` (schema `oi-delegation/1`) | retained | unchanged |
| ### 7.1 Location and pinning | retained | unchanged |
| ### 7.2 Rules common to every class | modified | see 1a |
| ### 7.3 Classes | retained | unchanged |
| ## 8. Classification of hits and the review load | retained | unchanged |
| ### 8.1 Rules | modified | see 1a |
| ### 8.2 Review load before the amended plan can pass as written (R5) | retained | unchanged |
| ## 9. Complete list of FAIL and REVIEW conditions | retained | unchanged |
| ### FAIL (exit 20) | retained | unchanged |
| ### REVIEW_REQUIRED (exit 10) | retained | unchanged |
| ## 10. Test matrix | modified | see 1a |
| ### 10.1 Unit and mutation controls (synthetic, in memory) | retained | unchanged |
| ### 10.2 Adversarial controls (each tied to its rule) | modified | see 1a |
| ### 10.3 Real-tree controls (CI) | retained | unchanged |
| ### 10.4 Control reporting and new controls (B1-B6, S1-D1) | modified | see 1a |
| ## 11. Mapping of the mandatory sec. 11 checks (P's PREREG sec. 11) to the tool | modified | see 1a |
| ## 12. Placement and governance | retained | unchanged |
| ### 12.1 Placement | modified | see 1a |
| ### 12.2 Sec. 11 replacement text (v2 addendum 4, point 1) | retained | unchanged |
| ### 12.3 Governance | retained | unchanged |
| ## 13. Four trees | retained | unchanged |
| ### 13.1 Roles and invariants | retained | unchanged |
| ### 13.2 Controls | modified | see 1a |
| ### 13.3 Reconciliation records (schema `oi-reconciliation/1`) | retained | unchanged |
| ### 13.4 Re-resolving `M` | modified | see 1a |
| ## 14. How the figures were measured | retained | unchanged |
| ## 15. Open points for the owner | modified | see 1a |
| ## 16. Generality: a core independent of any retirement, with frozen per-retirement configuration (condition 9) | retained | unchanged |
| ### Scope | retained | unchanged |
| ### 16.1 The engine (`tools/ledger_coverage/engine/`) | modified | see 1a |
| ### 16.2 Configuration record `oi-retirement-config/1` | modified | see 1a |
| ### 16.3 Adapter interfaces (versioned) | retained | unchanged |
| ### 16.4 A1 as the first configuration: where each A1 constant goes | modified | see 1a |
| ### 16.5 Synthetic second configuration (test only) | retained | unchanged |
| ### 16.6 Fail-closed configuration validation | retained | unchanged |
| ### 16.7 Reproducibility | modified | see 1a |
| ### 16.8 Implementation step | modified | see 1a |

Totals: 45 retained, 25 modified, 0 removed headings; v6.0d adds no heading. Subsection units removed inside modified sections are listed in 1a.

### 1a. Units inside the modified sections

| v5.5.9 unit | Status | Reason |
|---|---|---|
| Status and authority: version history bullets (v5.5.9 back to v4, decision lists A-D1..A-D5, R-D1..R-D5, D1-D4, DI-1, DI-2, N3, K7) | removed (replaced by a pointer to `DESIGN-v5.5.9.md`) | history of authorization machinery; kept verbatim in v5.5.9, which stays unchanged |
| Status and authority: route authority c.7093128173, standing instructions, WN label | retained (text kept) | procedural route and figure labels |
| Status and authority: new bullets (owner decisions quoted, what v6.0 verifies and does not claim, removes, keeps, procedural approval, host reads, identifiers, Q10) | added | owner decisions of 2026-11-24 and the wording requirement |
| Goal link | modified | adds "which exact commits a run checked" and "no owner approval" |
| Notation: `F` | modified | `F` is an explicit input |
| Notation: `T`; full-id sentence | added | exact-commit binding of the tool; object integrity |
| 0.1 row 8 | modified | authorization lint removed (owner decision item 1) |
| 0.2 rows on `A`, forms, freeze ledger, authority changes, designation | removed | answers were the removed machinery |
| 0.2 rows on execution identity, B3, B4, R11 | modified | references re-pointed to retained controls |
| 0.2 new row (2026-11-24 decisions) | added | traceability |
| Sec. 1, last residual-limit bullet | modified | no "quoted authorization exists" check; approval outside the tool stated |
| Sec. 2.1 stage 2 | modified | object integrity and the tool's own files against `T` |
| Sec. 5, acceptance predicate: schema, blobs, admission, host-run bullets | modified | `/5`; `T` replaces `A.engine_pins`; no designation or `A`; consumer reads the run in its own repository; technical meaning of acceptance stated |
| Sec. 5, durable evidence: landing record | modified | "authorized landing record" -> "landing record, the result commit"; owner approval quoted, not checked |
| Sec. 5, durable evidence: recipe | modified | `A` removed, `F`, `T`, pin table added |
| Sec. 5, durable evidence: freeze-ledger events bullet | removed | freeze ledger removed |
| Sec. 5, offline replay; exit-code rules; wrapper; flags; boundary cases | retained | technical |
| Sec. 5, integrity errors: unresolvable object | modified | now includes an object that does not hash to its id |
| Sec. 5, output form schema id | modified | `oi-ledger-coverage/5`; a `/4` result is never acceptable |
| 6.3 title | modified | authorization removed; admission, identity, integrity named |
| 6.3 record kinds, writer, independent reviewer, review record | retained | review chain is technical lint, not authorization |
| 6.3 "Owner authorization" (`oi-owner-authorization/1`) | removed; replaced by "Owner approval (procedural)" | owner decision item 1 and 3; no replacement mechanism |
| 6.3 frozen configuration | modified | references records and reviews only |
| 6.3 "What the tool checks": authorization bullets | removed | authorization only |
| 6.3 "What the tool checks": reviewer-not-a-run bullet | modified | `owner` and `comment_id` cases removed |
| 6.3 "What the tool checks": lineage, predecessor clause | modified | predecessor needs its review and, if widening, its widening review; "Owner at creation" removed |
| 6.3 "What the tool checks": other bullets (hashes, schema, review binding, reviewer != author, coverage of verdicts, supersedes, cycles, ambiguous ancestry, object store) | retained | technical |
| 6.3 configuration admission and root of trust (lead) | removed | authority values |
| 6.3 authority record `A` | removed | owner decision item 1 |
| 6.3 forms | removed | owner decision item 1 |
| 6.3 Owner at creation | removed | owner decision item 1 |
| 6.3 trust root points 1-2 | removed; replaced by execution identity point 1 and object integrity | point 1's run record is kept (Actions REST); point 2 read `A` from `main` |
| 6.3 trust root point 3 (execution identity, K7) | modified (execution identity points 2-3) | `T` replaces `A.engine_pins`; the two K7 allowances lapse with their components |
| 6.3 trust root point 4 (acceptance) | modified (execution identity point 4) | consumer repeats identity in its own repository; no `A` |
| 6.3 authority changes; changes between `F` and execution; caller cannot override | removed | authorization only; unknown configuration fields still refuse (sec. 16.6) |
| 6.3 freeze ledger | removed | owner decision item 1 |
| 6.3 admission points 1-9 | modified (configuration admission 1-4) | points 2-5 and 7 (thread, edits, forms, state, owner field) removed; point 6 (pin table), 8 (optional equality), 9 (local, replay) kept; `F` and pin-table path explicit |
| 6.3 admission snapshot | modified | comment, `A`, ledger fields removed; run, `T`, tool blobs, `F`, pin table, evaluated commits and delegated evidence kept |
| 6.3 residual trust assumptions | modified | host comment, merge and history attestations, moderators, first `A` and owner account removed; Actions records, runner, git object ids, snapshot authenticity kept |
| 6.3 object integrity (verified reader); host reads | added | hash integrity of every git read (from v5.5.10a's reader, without its authority anchors); the remaining host reads stated |
| 6.3 corrections; residual limit | modified | no new authorization; identity rests on writer and reviewer |
| 6.3 widening of allow and deny rules (lists) | retained | technical |
| 6.3 widening review requirement | modified | owner authorization of the widening review removed; review coverage kept |
| 6.3 examples and fingerprints; kind-specific rules | retained | technical |
| 7.2 host-run classes | modified | "host's REST API"; pointer to host reads |
| 8.1 first row | modified | "authorized replacement image" -> "ledgered replacement image" (wording requirement) |
| 10 lead | modified | "Retired identifiers" paragraph added |
| 10.2, 10.4, 13.2 rows | per table 2 | |
| 11 lead | modified | `--freeze F` and `--pin-table` named |
| 12.1 audit directory | modified | "authorization records" removed |
| 15 item 0a | removed (id retired) | `A` and the freeze ledger |
| 15 item 1 | modified | adds the 2026-11-24 decisions to those to be cited |
| 15 items 0, 2-6 | retained | |
| 15 items 10-12 | added | review of v6.0; ESC-6 and A1 gaps unchanged; plan amendment |
| 16.1 allowlist schema ids | modified | `/5`; `oi-owner-authorization/1` removed |
| 16.2 `retirement`, `records`, `author` rows | modified | owner login informational only; authorization records removed; a retired kind is `CONFIG_INVALID` |
| 16.4 records row | modified | authorization records removed |
| 16.7 `config` fields, records, engine | modified | snapshot fields; `T` recorded |
| 16.8 S13 | modified | acceptance list |
| **v6.0a changes (against v6.0)** | | |
| Status: v6.0a bullet with the review and owner decision quoted; "What the tool verifies" shortened | modified | review B-4, N-4; owner item 6 |
| Sec. 1: normative no-approval sentence | modified | the one normative statement (N-4) |
| Sec. 5 predicate: tool blobs against the configuration's `tool` pins; repository, head repository and event; "another workflow" | modified | B-1, B-2 |
| Sec. 5 predicate: the "This predicate is technical" paragraph | removed | duplicate no-approval statement (N-4) |
| Sec. 5 "Class meanings" table | added | B-4 (fixed meaning table; no lint control, owner item 2) |
| Sec. 6.2 "approved text/location/sentence/neighbours" | modified | "fingerprinted" (N-3) |
| 6.3 owner approval paragraph: "no tool output states or implies it" | removed | duplicate (N-4) |
| 6.3 configuration admission: `--pin-table` and `--config-sha256` | removed | B-3 (pin table derived from the `PREREG.md` beside the configuration, last `Record pins` subsection); N-4 |
| 6.3 execution identity: `tool` pins, workflow pin, `repository_id`, event rule; on-`main` statement | modified | B-1, B-2; F-1 stands |
| 6.3 snapshot: head repository, event, workflow blob; "It records no approval" | modified | B-2; duplicate removed (N-4) |
| 6.3 residual trust: run's head repository and event | modified | B-2 |
| 7.2 host-run classes: event and repository clause | modified | review N-6, applied as one clause |
| 10 retired-identifier paragraph | modified | TR15 and TR50 restored; EI1-EI5 new (v6.0a; EI6-EI14 follow in v6.0b and v6.0c) |
| 11 lead: `--pin-table` | removed | B-3 |
| 13.4: `git ls-remote` failure handling | modified | N-2 |
| 15 items 10, 12 | modified | owner items 4, 6 |
| 16.2 `retirement` owner login | removed | N-4 |
| 16.2 `tool`, `repository_id` fields; lint; widening | added | B-1, B-2 |
| 16.4 destination of the tool pins and the repository id | added | B-1, B-2 |
| 16.7 run repository, head repository, event, tool pins | modified | B-1, B-2 |
| **v6.0b changes (against v6.0a)** | | |
| Status: v6.0b bullet quoting review v6.0a and the owner decision; v6.0a and v6.0 bullets shortened; identifiers | modified | owner bullets; traceability |
| 0.2 row for review v6.0a | added | traceability |
| Sec. 5 wrapper: package loaded by location after the isolation check | modified | R-1 |
| Sec. 5 predicate: execution identity points 5 and 6; `T` on `M`'s first-parent chain | modified | R-1; owner bullet 1 |
| 6.3 owner confirmation names the configuration path with `F` | modified | N2 |
| 6.3 execution identity: point 4 repeats the `uses:` check; points 5 (nothing unpinned executes: import path, workflow dependencies) and 6 (`T` on `main`) added; "not checked" paragraph removed; no option or environment value sets `tool` or `repository_id` | modified | R-1, N3, N5; owner bullets 1-3 |
| 6.3 residual trust: runner sentence conditional on point 5 | modified | N6 |
| 10 lead: EI1-EI7 | modified | owner bullet 3 |
| 13.4: `ls-remote` against the repository `repository_id` names; `T` on `M`'s chain | modified | N4; R-1 |
| 15 items 10, 12 | modified | owner bullet 6; plan item P8 |
| **v6.0c changes (against v6.0b)** | | |
| Status: v6.0c bullet quoting review v6.0b and the owner decision; v6.0b bullet shortened; identifiers EI8-EI14 | modified | owner decision; traceability |
| 0.2 row for review v6.0b | added | traceability |
| Sec. 5 wrapper: isolation check before any import not loaded at start | modified | N-g |
| Sec. 5 predicate: the consumer repeats points 1-3, the `uses:` check of point 5, and point 6 | modified | N-d |
| 6.3 execution identity point 5: scope "every run of the pinned workflow"; delegated checker runs excluded; pre-run pin check (inline step, `os.lstat`, exact path set, regular files, sha256 pins, fails before the entry point); import path wording; isolation check before the first import; workflow review checklist; fail-closed `uses:` line rule | modified | O-1 (b), Q-1, N-b, N-g, N-h |
| 6.3 execution identity point 6: ERROR at the tool unless the run record's `head_branch` is `main` | modified | N-c |
| 10 lead: EI1-EI14 | modified | traceability |
| 10.4 EI1, EI6, TR29 modified; EI8-EI14 added | modified / added | O-1, N-c, N-g |
| 15 items 10, 12 | modified | owner decision (focused review); plan item P8 |
| **v6.0d changes (against v6.0c; editorial)** | | |
| Status: v6.0d bullet quoting review v6.0c and the owner decision; identifiers EI15 | modified | traceability |
| 6.3 execution identity point 1 lists the head branch | modified | R-c |
| 6.3 point 5, pre-run check: "after the checkout and the fetch of `F`"; `GITHUB_REF` must be `refs/heads/main` and `F` a full 40-hex id; `tools` and every parent of a checked path a real directory; the rule for locating the step and extracting its program | modified | O-4, R-c, R-d, R-e |
| 6.3 point 5, `uses:` rule: the line-rule mechanism stated (no YAML parser) | modified | R-a |
| 6.3 point 5, checklist: no `continue-on-error` or `if:` after the pre-run check; no reusable workflow | modified | R-b |
| 10 lead, S13: EI1-EI15 | modified | traceability |
| 10.4 EI7, EI13, EI14 modified; EI15 added | modified / added | R-a, R-d, O-4 |
| 15 item 10: focused delta review of v6.0d against v6.0c | modified | R-c; owner decision |

## 2. Table rows of v5.5.9 (every table)

Header rows are omitted. "Kind" for a removed row: **A** = tested or answered authorization only; **A+T** = also touched a technical guarantee, re-covered by the named retained row.

### Table at v5.5.9 line 136 (sec. "Notation"; header `| Symbol | Meaning |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 138 | `E` | retained | unchanged |  |
| 139 | `H` | retained | unchanged |  |
| 140 | `T1'` | retained | unchanged |  |
| 141 | `P` | retained | unchanged |  |
| 142 | `W` | retained | unchanged |  |
| 143 | `F` | modified | explicit input of every run |  |
| 144 | `X` | retained | unchanged |  |
| 145 | `C` | retained | unchanged |  |
| 146 | `M` | retained | unchanged |  |
| 147 | `L` | retained | unchanged |  |

### Table at v5.5.9 line 161 (sec. "0.1 Owner acceptance conditions"; header `| Condition | Answered in |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 163 | 1. Distinct exit codes, including parser errors and `--he... | retained | unchanged |  |
| 164 | 2. A frozen, reviewed `delegation.json` with exact-head e... | retained | unchanged |  |
| 165 | 3. Deny-pattern coverage; adversarial FAILs, each traced ... | retained | unchanged |  |
| 166 | 4. A preregistered s3-to-context mapping; the T1' cases r... | retained | unchanged |  |
| 167 | 5. Every replacement-text and unclassified hit classified... | retained | unchanged |  |
| 168 | 6. Deterministic HP regions; full merge ids; HP/RET overl... | retained | unchanged |  |
| 169 | 7. Each mandatory sec. 11 check mapped to an operation, f... | retained | unchanged |  |
| 170 | 8. Review and authorization lint for rules, PIN_OK reason... | modified | authorization lint removed (owner decision item 1); flag F-5 |  |
| 171 | 9. Generality with strict scope limits | retained | unchanged |  |
| 172 | 9.1. A core that does not depend on any retirement | retained | unchanged |  |
| 173 | 9.2. A frozen per-retirement configuration `oi-retirement... | retained | unchanged |  |
| 174 | 9.3. A1 as the first configuration, with every A1-specifi... | retained | unchanged |  |
| 175 | 9.4. A structurally different synthetic configuration wit... | retained | unchanged |  |
| 176 | 9.5. Fail-closed configuration validation, with exit code... | retained | unchanged |  |
| 177 | 9.6. Reproducibility record | retained | unchanged |  |

### Table at v5.5.9 line 186 (sec. "0.2 Review changes"; header `| Review item | Answered in |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 188 | v1 Q1: HP class kept out of RET; attribution; tracking re... | retained | unchanged |  |
| 189 | v1 Q2: new-pattern-in-replacement; per-hit classification... | retained | unchanged |  |
| 190 | v1 Q3: preregistered context rule; BOF/EOF sentinel | retained | unchanged |  |
| 191 | v1 Q4: placement | retained | unchanged |  |
| 192 | v1 Q5: schema, fingerprints, output form, boundary cases | retained | unchanged |  |
| 193 | v2 addenda 1-4 | retained | unchanged |  |
| 194 | v3 R1: FAIL exit code; acceptance predicate; X7 | retained | unchanged |  |
| 195 | v3 R2: DR-4 against V5 and the retired (A1) entries; a co... | retained | unchanged |  |
| 196 | v3 R3: deny set strengthened; residual limit | retained | unchanged |  |
| 197 | v3 R4: sec. 11 note 1; `item7-literal` | retained | unchanged |  |
| 198 | v3 R5: sec. 8.2 profile sets and disjointness | retained | unchanged |  |
| 199 | v3 R6: region mergers; both overlap counts; per-line clas... | retained | unchanged |  |
| 200 | v3 R7: sec. 5 against `--final` | retained | unchanged |  |
| 201 | v3 R8: adapters outside the purity scope; Z9 allowlist an... | retained | unchanged |  |
| 202 | v3 R9: the two meanings of `E` | retained | unchanged |  |
| 203 | v3 R10: S0 indicators | retained | unchanged |  |
| 204 | v3 R11: ownership chain | modified | O4 retired |  |
| 205 | v4 V1: nine merger groups of 22 sites | retained | unchanged |  |
| 206 | v4 V2: `ptr` has 5 hits at T1' | retained | unchanged |  |
| 207 | v4 V3: the item-7 amendment check fails hard where the or... | retained | unchanged |  |
| 208 | v4 V4: repo-scan split 96 / 31 / 14 / 35 | retained | unchanged |  |
| 209 | v4 V5: HP obligations and merges are widening | retained | unchanged |  |
| 210 | v4 V6 and V5-D1: DR-1d and DR-2 dropped; DR-3's real witness | retained | unchanged |  |
| 211 | v4 V7: figure labels; source of v3's 86 | retained | unchanged |  |
| 212 | v4 V8 and V5-D2: `resid` widened | retained | unchanged |  |
| 213 | v4 O2-O7 (adopted) | retained | unchanged |  |
| 214 | v5 review W1, W2, O8 (v5.1) | retained | unchanged |  |
| 215 | Stage 1 D1 and S1-D1: W1 self-match, option B; self-PASS ... | retained | unchanged |  |
| 216 | Stage 1 D2: SW2 expectation | retained | unchanged |  |
| 217 | Stage 1 D3: 7 HP structure REVIEWs | retained | unchanged |  |
| 218 | Stage 1 D4: 215 region lines, LF-inclusive span | retained | unchanged |  |
| 219 | Stage 1 D5: RT-D 45 `resid` lines | retained | unchanged |  |
| 220 | Stage 1 D6: register and infinity semantics; parameters i... | retained | unchanged |  |
| 221 | Stage 1 D7: `rule-stale` scoping | retained | unchanged |  |
| 222 | Stage 1 D8: source-byte literals | retained | unchanged |  |
| 223 | Stage 1 B1: acceptance reads admission; harness results n... | retained | unchanged |  |
| 224 | Stage 1 B2: native delegated execution in a clone at `X`;... | retained | unchanged |  |
| 225 | Stage 1 B3: configuration admission from `F`'s designatio... | modified | admission from `F`'s pin table; TR4 retired |  |
| 226 | Stage 1 B4: commits of `C` classified path by path; widen... | modified | "and authorization" removed |  |
| 227 | Stage 1 B5: engine purity over adapter companions; guard ... | retained | unchanged |  |
| 228 | Stage 1 B6: control reporting with PASS, FAIL, SKIP and N... | retained | unchanged |  |
| 229 | Drift findings S2-S7 (reconciliation, landing composition... | retained | unchanged |  |
| 230 | v5.2 review V1: register and infinity on P's per-edit uni... | retained | unchanged |  |
| 231 | v5.2 review V2: `F`'s designation from the host, outside ... | removed | answer was designation from the host | A (traceability row) |
| 232 | v5.2 review V3: tool-landing class bound to exact blobs | retained | unchanged |  |
| 233 | v5.2 review V4: a control for every reconciliation condition | retained | unchanged |  |
| 234 | v5.2 review V5: context hash, location, deterministic grant | retained | unchanged |  |
| 235 | v5.2 review V6: SW2 reference, 14 sites | retained | unchanged |  |
| 236 | v5.2 review V7: native execution at `C` as well as `X` | retained | unchanged |  |
| 237 | v5.2 review V8: N10 pinned to the S6 probe | retained | unchanged |  |
| 238 | v5.2 review O1: case-insensitive negative literals | retained | unchanged |  |
| 239 | v5.3 review W1: P's edit variants selected as P selects; ... | retained | unchanged |  |
| 240 | v5.3 review W2-W4 and owner decisions A-D1 to A-D4: autho... | removed | answer was `A`, forms, thread | A (traceability row) |
| 241 | owner decision A-D5 and v5.3 review O3: durable evidence ... | retained | unchanged |  |
| 242 | owner addendum: the trust root of the authority record, b... | removed | answer was the trust root of `A` | A (traceability row) |
| 243 | v5.3 review O2: a sentence's byte offset | retained | unchanged |  |
| 244 | v5.4 review V1: P's count; offsets back to `H`; chained e... | retained | unchanged |  |
| 245 | v5.4 review V2 and R-D3: the run's commit; evaluated comm... | modified | reference renamed to execution identity |  |
| 246 | v5.4 review V3 and R-D3: the executed code bound by the host | modified | bound to the configuration's `tool` pins at `T`; controls listed |  |
| 247 | v5.4 review V4 and R-D2: every owner comment's edits; the... | removed | answer was comment edits and the freeze ledger | A (traceability row) |
| 248 | v5.4 review V5 and R-D4: the first line | removed | answer was the form first line | A (traceability row) |
| 249 | v5.4 addendum C1 and R-D4: authority changes by an owner ... | removed | answer was authority changes | A (traceability row) |
| 250 | v5.4 addendum C2 and R-D4: versioned forms | removed | answer was versioned forms | A (traceability row) |
| 251 | v5.4 addendum C3 and R-D5: admission snapshot, compressed... | retained | unchanged |  |
| 252 | v5.4 addendum C4 and R-D1: the stricter refusals stated | retained | unchanged |  |
| 253 | v5.4 review: residual-trust list | retained | unchanged |  |

### Table at v5.5.9 line 444 (sec. "2.2 Subject kinds"; header `| Kind | Anchor | Context | Source |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 446 | `site` | retained | unchanged |  |
| 447 | `splice` | retained | unchanged |  |
| 448 | `hit` | retained | unchanged |  |
| 449 | `pin` | retained | unchanged |  |
| 450 | `mirror` | retained | unchanged |  |
| 451 | `path` | retained | unchanged |  |
| 452 | `delegated` | retained | unchanged |  |

### Table at v5.5.9 line 456 (sec. "2.3 Operations"; header `| Op | Subcommand | Roles used |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 458 | A | retained | unchanged |  |
| 459 | B | retained | unchanged |  |
| 460 | C | retained | unchanged |  |
| 461 | D | retained | unchanged |  |

### Table at v5.5.9 line 495 (sec. "3.1 Pinned merges"; header `| PR | Merge commit | First parent | Sites first changed |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 497 | #1470 | retained | unchanged |  |
| 498 | #1473 | retained | unchanged |  |
| 499 | #1474 | retained | unchanged |  |
| 500 | #1472 | retained | unchanged |  |
| 501 | #1475 | retained | unchanged |  |
| 502 | #1494 | retained | unchanged |  |

### Table at v5.5.9 line 535 (sec. "3.2 Region definition (independent of any diff algorithm)"; header `| Step | Groups (sites at the pin) |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 537 | #1475 (7f28886f) | retained | unchanged |  |
| 538 | #1474 (a1f38284) | retained | unchanged |  |

### Table at v5.5.9 line 629 (sec. "4. Preregistered context rule"; header `| Frozen s3 value | Sites | 'meaning_context' |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 631 | visible (names the hypothesis); rewritten at deletion | retained | unchanged |  |
| 632 | visible (P0/P1/P2 disposition) | retained | unchanged |  |
| 633 | visible (applied splice) | retained | unchanged |  |
| 634 | visible (none: the (NR) corollary ...) | retained | unchanged |  |
| 635 | n/a | retained | unchanged |  |
| 636 | not determined: Q3 census | retained | unchanged |  |
| 637 | not determined | retained | unchanged |  |
| 638 | per unit regression audit (#1468) | retained | unchanged |  |
| 639 | per unit Q1 corrections (Step 2) | retained | unchanged |  |
| 640 | per unit Step-2 phase | retained | unchanged |  |
| 641 | per unit R6 corrections (Step 2) | retained | unchanged |  |
| 642 | per unit R1/R2 scoping | retained | unchanged |  |
| 643 | per unit Q2 | retained | unchanged |  |

### Table at v5.5.9 line 651 (sec. "4.1 Decision"; header `| Condition | Result |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 653 | `meaning_context` true, context changed, no context adjud... | retained | unchanged |  |
| 654 | `meaning_context` true, context changed, matching adjudic... | retained | unchanged |  |
| 655 | LIST or TABLE site, its structure context or its context ... | retained | unchanged |  |
| 656 | `meaning_context` false, context changed, not covered by ... | retained | unchanged |  |

### Table at v5.5.9 line 688 (sec. "4.3 Indicator effects"; header `| Indicator | Effect |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 690 | ANAPH | retained | unchanged |  |
| 691 | LIST | retained | unchanged |  |
| 692 | TABLE | retained | unchanged |  |
| 693 | PARTIAL | retained | unchanged |  |

### Table at v5.5.9 line 717 (sec. "4.3 Indicator effects"; header `| Indicator | v3 review's definitions: sites / of 52 changes | v4 definitions: s`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 719 | ANAPH | retained | unchanged |  |
| 720 | LIST | retained | unchanged |  |
| 721 | TABLE | retained | unchanged |  |
| 722 | PARTIAL | retained | unchanged |  |

### Table at v5.5.9 line 739 (sec. "4.4 The real-tree cases at T1'"; header `| Origin | Cases | Result under the rule | Resolved by |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 741 | E..H | retained | unchanged |  |
| 742 | H..T1' | retained | unchanged |  |

### Table at v5.5.9 line 752 (sec. "4.4 The real-tree cases at T1'"; header `| Origin | Sites | Result |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 754 | E..H | retained | unchanged |  |
| 755 | H..T1' | retained | unchanged |  |

### Table at v5.5.9 line 764 (sec. "5. Outcomes, exit codes and output"; header `| Outcome | Exit | Emitted when |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 766 | PASS | retained | unchanged |  |
| 767 | REVIEW_REQUIRED | retained | unchanged |  |
| 768 | FAIL | retained | unchanged |  |
| 769 | USAGE | retained | unchanged |  |
| 770 | ERROR | retained | unchanged |  |
| 771 | VOID | retained | unchanged |  |
| 772 | INTERNAL | retained | unchanged |  |

### Table at v5.5.9 line 939 (sec. "6.1 Scan profiles"; header `| Profile | Source | Applies to |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 941 | `p0-core`, `p0-para` | retained | unchanged |  |
| 942 | `ledger-ext` | retained | unchanged |  |
| 943 | `ptr` | retained | unchanged |  |
| 944 | `repo` | retained | unchanged |  |
| 945 | `count-grep` | retained | unchanged |  |
| 946 | `resid` | retained | unchanged |  |

### Table at v5.5.9 line 951 (sec. "6.1 Scan profiles"; header `| Profile | Source and scope |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 953 | `DR-1`, `DR-3`, `DR-4`, `DR-5` | retained | unchanged |  |
| 954 | `register`, `register-caps` | retained | unchanged |  |
| 955 | `infinity` | retained | unchanged |  |

### Table at v5.5.9 line 1677 (sec. "6.4 Deny rules DR-1, DR-3, DR-4, DR-5 (for independent review; measured in sec. 14)"; header `| Rule | T1' lines / sentences | H lines | Real-tree countercontrol at H |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 1679 | DR-1 | retained | unchanged |  |
| 1680 | DR-3 | retained | unchanged |  |
| 1681 | DR-4 | retained | unchanged |  |
| 1682 | DR-5 | retained | unchanged |  |

### Table at v5.5.9 line 1715 (sec. "6.4.1 Rejected candidates DR-1d and DR-2 (history)"; header `| Id | Purpose | Exact pattern (v4) | Forms it covered |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 1717 | DR-1d | retained | unchanged |  |
| 1718 | DR-2 | retained | unchanged |  |

### Table at v5.5.9 line 1840 (sec. "6.6 Residual review profile `resid` (widened in v5; for independent review)"; header `| Tree | Whole-corpus lines matched by resid-a | Lines matched by resid-b or res`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 1842 | E | retained | unchanged |  |
| 1843 | H | retained | unchanged |  |
| 1844 | T1' (whole corpus) | retained | unchanged |  |
| 1845 | T1', added text (287 splice-image lines) | retained | unchanged |  |

### Table at v5.5.9 line 1853 (sec. "6.6 Residual review profile `resid` (widened in v5; for independent review)"; header `| Line | Text near the match | Reading (the writer's, for the reviewer) |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 1855 | FULL:6265 | retained | unchanged |  |
| 1856 | book/appendix-c-objections.md:108 | retained | unchanged |  |
| 1857 | papers/Complexity.md:206 | retained | unchanged |  |
| 1858 | papers/Structure.md:1010 | retained | unchanged |  |

### Table at v5.5.9 line 1944 (sec. "7.3 Classes"; header `| Class | Paths | How the tool verifies it |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 1946 | `tex` | retained | unchanged |  |
| 1947 | `pdf` | retained | unchanged |  |
| 1948 | `record-dir` | retained | unchanged |  |
| 1949 | `sc42` | retained | unchanged |  |
| 1950 | `coverage-ledger` | retained | unchanged |  |
| 1951 | `ci` | retained | unchanged |  |

### Table at v5.5.9 line 1961 (sec. "8.1 Rules"; header `| Hit | State until classified | Resolved by |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 1963 | any profile hit in an authorized replacement image, insid... | modified | wording "ledgered replacement image" (no approval implied) |  |
| 1964 | a hit on an unchanged site line | retained | unchanged |  |
| 1965 | a hit in an HP region | retained | unchanged |  |
| 1966 | any other unheld hit | retained | unchanged |  |
| 1967 | a deny match on a tree where deny profiles run (sec. 2.3) | retained | unchanged |  |

### Table at v5.5.9 line 1987 (sec. "8.2 Review load before the amended plan can pass as written (R5)"; header `| Set | Profile set | Lines | Label |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 1989 | Hit lines in the 197 site replacement regions | retained | unchanged |  |
| 1990 | Hit lines in splices over hit lines of HP site regions | retained | unchanged |  |
| 1991 | New hit lines on non-site lines (D237, D238, D241, D242, ... | retained | unchanged |  |
| 1992 | Pre-existing unheld lines identical at H | retained | unchanged |  |
| 1993 | `resid` hits in added text, hit by no other review profile | retained | unchanged |  |
| 1994 | W1 allow rules | retained | unchanged |  |
| 1995 | W2 allow rules | retained | unchanged |  |
| 1996 | The fifth `ptr` hit, papers/GR.md:58 | retained | unchanged |  |
| 1997 | HP site adjudications, with `hit_classifications` for the... | retained | unchanged |  |
| 1998 | Meaning-context adjudications (sec. 4.4) | retained | unchanged |  |
| 1999 | Indicator adjudications (sec. 4.4) | retained | unchanged |  |

### Table at v5.5.9 line 2115 (sec. "10.1 Unit and mutation controls (synthetic, in memory)"; header `| Id | Case | Expected |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 2117 | K1 | retained | unchanged |  |
| 2118 | K2 | retained | unchanged |  |
| 2119 | K3 | retained | unchanged |  |
| 2120 | K4 | retained | unchanged |  |
| 2121 | K5 | retained | unchanged |  |
| 2122 | K6 | retained | unchanged |  |
| 2123 | K7 | retained | unchanged |  |
| 2124 | K8 | retained | unchanged |  |
| 2125 | K9 | retained | unchanged |  |
| 2126 | B1 | retained | unchanged |  |
| 2127 | B2 | retained | unchanged |  |
| 2128 | B3 | retained | unchanged |  |
| 2129 | B4 | retained | unchanged |  |
| 2130 | B5 | retained | unchanged |  |
| 2131 | B6 | retained | unchanged |  |
| 2132 | H1 | retained | unchanged |  |
| 2133 | H2 | retained | unchanged |  |
| 2134 | H3 | retained | unchanged |  |
| 2135 | H4 | retained | unchanged |  |
| 2136 | H5 | retained | unchanged |  |
| 2137 | H6 | retained | unchanged |  |
| 2138 | H7 | retained | unchanged |  |

### Table at v5.5.9 line 2145 (sec. "10.2 Adversarial controls (each tied to its rule)"; header `| Id | Case | Expected | By |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 2147 | L1 | retained | unchanged |  |
| 2148 | L2 | retained | unchanged |  |
| 2149 | L3 | retained | unchanged |  |
| 2150 | L4 | retained | unchanged |  |
| 2151 | V1 | retained | unchanged |  |
| 2152 | V2 | retained | unchanged |  |
| 2153 | V3 | retained | unchanged |  |
| 2154 | V4 | retained | unchanged |  |
| 2155 | V27 | retained | unchanged |  |
| 2156 | V5 | retained | unchanged |  |
| 2157 | V6 | retained | unchanged |  |
| 2158 | V7a | retained | unchanged |  |
| 2159 | V7b | retained | unchanged |  |
| 2160 | V7c | retained | unchanged |  |
| 2161 | V9 | retained | unchanged |  |
| 2162 | V10 | retained | unchanged |  |
| 2163 | V11 | retained | unchanged |  |
| 2164 | V12 | retained | unchanged |  |
| 2165 | V13 | retained | unchanged |  |
| 2166 | V14 | retained | unchanged |  |
| 2167 | V15 | retained | unchanged |  |
| 2168 | V16 | retained | unchanged |  |
| 2169 | V17 | retained | unchanged |  |
| 2170 | V18 | retained | unchanged |  |
| 2171 | V19 | retained | unchanged |  |
| 2172 | V20 | retained | unchanged |  |
| 2173 | V21 | retained | unchanged |  |
| 2174 | V22 | retained | unchanged |  |
| 2175 | N-W | retained | unchanged |  |
| 2176 | V23 | retained | unchanged |  |
| 2177 | V24 | retained | unchanged |  |
| 2178 | V25 | retained | unchanged |  |
| 2179 | V26 | retained | unchanged |  |
| 2180 | A1r | retained | unchanged |  |
| 2181 | A2r | retained | unchanged |  |
| 2182 | A3r | retained | unchanged |  |
| 2183 | A4r | retained | unchanged |  |
| 2184 | A5r | retained | unchanged |  |
| 2185 | A6r | retained | unchanged |  |
| 2186 | A7r | retained | unchanged |  |
| 2187 | A8r | retained | unchanged |  |
| 2188 | A9r | retained | unchanged |  |
| 2189 | A10r | retained | unchanged |  |
| 2190 | A11r | retained | unchanged |  |
| 2191 | S1r | retained | unchanged |  |
| 2192 | S2r | retained | unchanged |  |
| 2193 | N1 | retained | unchanged |  |
| 2194 | N2 | retained | unchanged |  |
| 2195 | O1 | retained | unchanged |  |
| 2196 | O2 | retained | unchanged |  |
| 2197 | O3 | retained | unchanged |  |
| 2198 | O4 | removed | authorization only: hash binding of an owner-authorization record | A; the hash binding of records and reviews stays in O2, O6, S4a |
| 2199 | O5 | modified | owner comment-id case removed (authorization); reviewer case retained |  |
| 2200 | O6 | retained | unchanged |  |
| 2201 | O7 | modified | "or authorization" removed |  |
| 2202 | O8 | retained | unchanged |  |
| 2203 | O9 | modified | authorization removed from the positive chain |  |
| 2204 | G1 | retained | unchanged |  |
| 2205 | G2 | retained | unchanged |  |
| 2206 | G3 | retained | unchanged |  |
| 2207 | X1 | retained | unchanged |  |
| 2208 | X2 | retained | unchanged |  |
| 2209 | X3 | retained | unchanged |  |
| 2210 | X4 | retained | unchanged |  |
| 2211 | X5 | retained | unchanged |  |
| 2212 | X6 | retained | unchanged |  |
| 2213 | X7 | retained | unchanged |  |
| 2214 | X8 | retained | unchanged |  |
| 2215 | X9 | retained | unchanged |  |
| 2216 | X10 | modified | the engine blob is compared with the configuration's `tool` pin instead of `A.engine_pins` |  |

### Table at v5.5.9 line 2222 (sec. "10.3 Real-tree controls (CI)"; header `| Id | Run | Rule | Reference |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 2224 | RT-A | retained | unchanged |  |
| 2225 | RT-E | retained | unchanged |  |
| 2226 | RT-H0 | retained | unchanged |  |
| 2227 | RT-T0 | retained | unchanged |  |
| 2228 | RT-T | retained | unchanged |  |
| 2229 | RT-C | retained | unchanged |  |
| 2230 | RT-D | retained | unchanged |  |
| 2231 | RT-DR | retained | unchanged |  |
| 2232 | RT-DR3W | retained | unchanged |  |
| 2233 | RT-I7 | retained | unchanged |  |
| 2234 | RT-I7A | retained | unchanged |  |
| 2235 | SW1 | retained | unchanged |  |
| 2236 | SW2 | retained | unchanged |  |

### Table at v5.5.9 line 2266 (sec. "10.4 Control reporting and new controls (B1-B6, S1-D1)"; header `| Id | Case | Expected | By |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 2268 | WB1 | retained | unchanged |  |
| 2269 | WB2 | retained | unchanged |  |
| 2270 | WB3 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2271 | WB4 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2272 | WB5 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2273 | WB6 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2274 | WB7 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2275 | WB8 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2276 | WB9 | retained | unchanged |  |
| 2277 | WB10 | retained | unchanged |  |
| 2278 | WB11 | retained | unchanged |  |
| 2279 | WB12 | retained | unchanged |  |
| 2280 | WB13 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2281 | WB14 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2282 | WB15 | modified | wording only: "approved" -> "fingerprinted" (review N-3); expectation unchanged |  |
| 2283 | X11 | retained | unchanged |  |
| 2284 | TR1 | retained | unchanged |  |
| 2285 | TR2 | modified | the pin table is the `PREREG.md` beside the configuration; `--config-sha256` removed (review B-3, N-4); expectation unchanged |  |
| 2286 | TR3 | modified | authorization record removed from the case; expectation unchanged |  |
| 2287 | TR4 | removed | authorization only: `retirement.owner` against `A.owner.id` | A |
| 2288 | TR5 | modified | positive control without `A`, designation and thread; with the derived pin table, tool and workflow pins, repository id and event |  |
| 2289 | TR6 | removed | authorization only: designation from the host, not from `F` | A |
| 2290 | TR7 | removed | authorization only: designation author id | A |
| 2291 | TR8 | removed | authorization only: designation names `F` | A; technical part (`F` mismatch): EI3 |
| 2292 | TR9 | removed | authorization values not overridable; one clause also tests an unknown configuration field; the pin-table path was among the fixed values | A+T; unknown configuration field: Z1-Z8; pin table derived, not caller-chosen: EI4 |
| 2293 | TR10 | removed | authorization only: a caller-built `F` without designation | A; technical part (`F` mismatch with the landing record): EI3; approval procedural |
| 2294 | TR11 | removed | authorization only: edited designation comment | A |
| 2295 | TR12 | removed | authorization only: supersession in the thread, pagination | A |
| 2296 | TR13 | modified | cross-reference renumbered; expectation unchanged (no "chain" outside CI) |  |
| 2297 | TR14 | modified | repository and head repository ids against the configuration's `repository_id`, at the tool and the consumer; fork `pull_request` case added (review B-2) |  |
| 2298 | TR15 | modified | v5.5.9 meaning restored (review B-1, CX-2): workflow blob compared with `tool.workflow` in the configuration at `F` instead of `A.workflow` |  |
| 2299 | TR16 | removed | authorization only: authorized thread | A |
| 2300 | TR17 | removed | authorization only: comment forms | A |
| 2301 | TR18 | removed | authorization only: withdrawal | A |
| 2302 | TR19 | removed | authorization only: deleted or hidden designation | A |
| 2303 | TR20 | removed | authorization only: numeric author id | A |
| 2304 | TR21 | removed | comment-listing failure; also the fail-closed handling of host reads | A+T; GV7 (every remaining host read fails closed) |
| 2305 | TR22 | removed | authorization only: two live designations | A |
| 2306 | TR23 | removed | authorization only: copy of `A` in `F`; merge of `A` by another account | A |
| 2307 | TR24 | removed | authorization only: caller-supplied `A` | A |
| 2308 | TR25 | removed | authorization only: `A` from another ref | A; refs never consulted for role commits: GV1 |
| 2309 | TR26 | removed | authorization only: change of `A` after `F` | A |
| 2310 | TR27 | removed | authorization only: bootstrap order of `A` | A |
| 2311 | TR28 | modified | v5.5.9 meaning restored (review B-1, CX-1): tool blobs compared with the configuration's `tool` pins instead of `A.engine_pins`; the checkout case moves to EI1 |  |
| 2312 | TR29 | modified | first case restored with its v5.5.9 meaning: ERROR at the tool (`head_branch`, N-c) and non-acceptance at the consumer against `M` from `git ls-remote` (R-1); `head_sha = X` kept; `T` mismatch added |  |
| 2313 | TR30 | retained | unchanged |  |
| 2314 | TR31 | removed | authorization only: freeze ledger binds a withdrawal | A |
| 2315 | TR32 | removed | authorization only: snapshot binds a supersession | A |
| 2316 | TR33 | removed | authorization only: edit history of owner comments | A |
| 2317 | TR34 | removed | authorization only: edit history of owner comments | A |
| 2318 | TR35 | removed | authorization only: deletion residual | A |
| 2319 | TR36 | removed | authorization only: freeze ledger missing or conflicting | A |
| 2320 | TR37 | removed | authorization only: form first line (CRLF) | A |
| 2321 | TR38 | removed | authorization only: malformed form | A |
| 2322 | TR39 | removed | authorization only: form version and key order | A |
| 2323 | TR40 | removed | authorization only: authority change without approval | A |
| 2324 | TR41 | removed | authorization only: approval hash or time | A |
| 2325 | TR42 | removed | authorization only: edited approval | A |
| 2326 | TR43 | removed | authorization only: approval by another id | A |
| 2327 | TR44 | removed | authorization only: owner-id change | A |
| 2328 | TR45 | retained | unchanged |  |
| 2329 | TR46 | retained | unchanged |  |
| 2330 | TR47 | removed | authorization only: freeze-ledger append approval (N3) | A |
| 2331 | TR48 | modified | positive K7 control against the configuration's `tool` pins, without the two allowances |  |
| 2332 | TR49 | removed | authority record at `head_sha` modified (K7 allowance) | A+T; the allowance no longer exists; any tool file off the pins: TR28, TR52 |
| 2333 | TR50 | modified | v5.5.9 meaning restored (review B-1): one-byte workflow change against the configuration's pin |  |
| 2334 | TR51 | modified | non-regular entries under the tool directory at `T`; the permitted-path substitution cases removed with the allowances |  |
| 2335 | TR52 | modified | extra file measured against the configuration's `tool.files` instead of `A.engine_pins` |  |
| 2336 | TR53 | removed | second copy of the authority record (K7) | A+T; extra tool file off the pins: TR52 |
| 2337 | TR54 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2338 | TR55 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2339 | TR56 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2340 | TR57 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2341 | TR58 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2342 | TR59 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2343 | TR60 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2344 | TR61 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2345 | TR62 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2346 | TR63 | removed | authorization only: "Owner at creation" (DI-1); `A` lineage (DI-2 for `A`) | A |
| 2347 | TR64 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2348 | TR65 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2349 | TR66 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2350 | TR67 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2351 | TR68 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2352 | TR69 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2353 | TR70 | removed | authorization only: "Owner at creation" (DI-1) | A |
| 2354 | G4 | retained | unchanged |  |
| 2355 | G5 | retained | unchanged |  |
| 2356 | G6 | retained | unchanged |  |
| 2357 | G7 | retained | unchanged |  |
| 2358 | G9 | retained | unchanged |  |
| 2359 | G8 | retained | unchanged |  |
| 2360 | R16 | retained | unchanged |  |
| 2361 | R17 | retained | unchanged |  |
| 2362 | A12r | modified | no-authorization case replaced by a review naming another superseded blob (both within the widening-review rule) |  |
| 2363 | Z9h | retained | unchanged |  |
| 2364 | S11-56 | retained | unchanged |  |
| 2365 | S11-57a | retained | unchanged |  |
| 2366 | S11-57b | retained | unchanged |  |
| 2367 | S11-57c | retained | unchanged |  |
| 2368 | S11-57d | retained | unchanged |  |
| 2369 | S11-58a-f | retained | unchanged |  |
| 2370 | S11-58g | retained | unchanged |  |
| 2371 | S11-58h | retained | unchanged |  |
| 2372 | S11-58i | retained | unchanged |  |
| 2373 | S11-58j | retained | unchanged |  |
| 2374 | S11-58k | retained | unchanged |  |
| 2375 | K10 | retained | unchanged |  |

### Table at v5.5.9 line 2388 (sec. "11. Mapping of the mandatory sec. 11 checks (P's PREREG sec. 11) to the tool"; header `| # | Original check | Tool command | Expected at a T1'-style 'X' | Countercontr`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 2390 | 1 | retained | unchanged |  |
| 2391 | 2 | retained | unchanged |  |
| 2392 | 3 | retained | unchanged |  |
| 2393 | 4 | retained | unchanged |  |
| 2394 | 5 | retained | unchanged |  |
| 2395 | 6 | retained | unchanged |  |
| 2396 | 7 | retained | unchanged |  |
| 2397 | 8 | retained | unchanged |  |
| 2398 | 9 | retained | unchanged |  |
| 2399 | 10 | retained | unchanged |  |
| 2400 | 11 | retained | unchanged |  |
| 2401 | 12 | retained | unchanged |  |
| 2402 | 13 | retained | unchanged |  |
| 2403 | 14 | retained | unchanged |  |

### Table at v5.5.9 line 2555 (sec. "13.2 Controls"; header `| Id | Case | Expected |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 2557 | N3 | retained | unchanged |  |
| 2558 | N4 | retained | unchanged |  |
| 2559 | N5 | retained | unchanged |  |
| 2560 | N6 | retained | unchanged |  |
| 2561 | N7 | retained | unchanged |  |
| 2562 | N8 | retained | unchanged |  |
| 2563 | N9 | retained | unchanged |  |
| 2564 | N10 | retained | unchanged |  |
| 2565 | N11 | retained | unchanged |  |
| 2566 | R18 | retained | unchanged |  |
| 2567 | N12 | retained | unchanged |  |
| 2568 | N13 | retained | unchanged |  |
| 2569 | N14 | retained | unchanged |  |
| 2570 | N15 | retained | unchanged |  |
| 2571 | N16 | retained | unchanged |  |
| 2572 | N17 | retained | unchanged |  |
| 2573 | N18 | retained | unchanged |  |
| 2574 | R19 | retained | unchanged |  |
| 2575 | Z11 | retained | unchanged |  |
| 2576 | S4a | retained | unchanged |  |
| 2577 | LN1 | retained | unchanged |  |
| 2578 | LN2 | retained | unchanged |  |
| 2579 | LN3 | retained | unchanged |  |
| 2580 | LN4 | modified | no-authorization case replaced by a predecessor widening without a valid widening review |  |
| 2581 | LN5 | retained | unchanged |  |
| 2582 | LN6 | retained | unchanged |  |
| 2583 | LN7 | retained | unchanged |  |
| 2584 | LN8 | retained | unchanged |  |
| 2585 | LN9 | removed | authorization only: lineage across an owner change (DI-1) | A; lineage itself: LN1-LN8, LN10 |
| 2586 | LN10 | retained | unchanged |  |
| 2587 | LN11 | removed | authorization across an owner change; also lineage with a widened predecessor (positive) | A+T; LN2 (positive lineage) and LN4 (widened predecessor, modified) |
| 2588 | LN12 | removed | authorization only: authorization of a predecessor's widening review | A; widening review of a predecessor: LN4 (modified) |

### Table at v5.5.9 line 2916 (sec. "16.1 The engine (`tools/ledger_coverage/engine/`)"; header `| Id | Case | Expected |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 2918 | Z9a | retained | unchanged |  |
| 2919 | Z9b | retained | unchanged |  |
| 2920 | Z9c | retained | unchanged |  |
| 2921 | Z9d | retained | unchanged |  |
| 2922 | Z9e | retained | unchanged |  |
| 2923 | Z9f | retained | unchanged |  |
| 2924 | Z9g | retained | unchanged |  |
| 2925 | Z9h | retained | unchanged |  |

### Table at v5.5.9 line 2940 (sec. "16.2 Configuration record `oi-retirement-config/1`"; header `| Field | Content |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 2942 | `schema` | retained | unchanged |  |
| 2943 | `config_id`, `version`, `supersedes` | retained | unchanged |  |
| 2944 | `retirement` | modified | owner login removed (review N-4) |  |
| 2945 | `roles` | retained | unchanged |  |
| 2946 | `corpus` | retained | unchanged |  |
| 2947 | `adapters.ledger` | retained | unchanged |  |
| 2948 | `adapters.sitemap` | retained | unchanged |  |
| 2949 | `adapters.replay` | retained | unchanged |  |
| 2950 | `profiles` | retained | unchanged |  |
| 2951 | `checks` | retained | unchanged |  |
| 2952 | `rules` | retained | unchanged |  |
| 2953 | `context_mapping` | retained | unchanged |  |
| 2954 | `indicators` | retained | unchanged |  |
| 2955 | `sentence` | retained | unchanged |  |
| 2956 | `hp_obligations` | retained | unchanged |  |
| 2957 | `delegation` | retained | unchanged |  |
| 2958 | `records` | modified | authorization records removed; retired kind is CONFIG_INVALID |  |
| 2959 | `operations` | retained | unchanged |  |
| 2960 | `controls` | retained | unchanged |  |
| 2961 | `author` | modified | configuration has a review, no authorization record |  |

### Table at v5.5.9 line 3021 (sec. "16.3 Adapter interfaces (versioned)"; header `| Interface | Must return |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 3023 | ledger | retained | unchanged |  |
| 3024 | sitemap | retained | unchanged |  |
| 3025 | replay | retained | unchanged |  |
| 3026 | delegation | retained | unchanged |  |

### Table at v5.5.9 line 3045 (sec. "16.4 A1 as the first configuration: where each A1 constant goes"; header `| Constant | Destination |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 3047 | `E`, record commit, `R` tree b05efdca | retained | unchanged |  |
| 3048 | `H` | retained | unchanged |  |
| 3049 | `R` paths and the Phase-0/2 record paths | retained | unchanged |  |
| 3050 | ledger and edits schema ids, `retained_unchanged`, `mirro... | retained | unchanged |  |
| 3051 | frozen function names, line-523 handling | retained | unchanged |  |
| 3052 | corpus `papers/*.md`, `book/*.md` | retained | unchanged |  |
| 3053 | profiles p0-core, p0-para, ledger-ext, ptr, repo, count-g... | retained | unchanged |  |
| 3054 | `resid` (resid-a, resid-b, resid-c), DR-1, DR-3, DR-4, DR... | retained | unchanged |  |
| 3055 | item 7 and item 11 profile sets and `final_profiles` (`it... | retained | unchanged |  |
| 3056 | DR-3's control-only witness input (`AGENTS.md` at H) | retained | unchanged |  |
| 3057 | repo scope (historical prefixes and files, generated arti... | retained | unchanged |  |
| 3058 | s3 mapping (sec. 4) | retained | unchanged |  |
| 3059 | ANAPH, LIST, TABLE, PARTIAL definitions and effects | retained | unchanged |  |
| 3060 | sentence abbreviations | retained | unchanged |  |
| 3061 | the six pinned merges and PR numbers (sec. 3.1) | retained | unchanged |  |
| 3062 | tex/pdf/record-dir/sc42/coverage-ledger/ci classes, STALE... | retained | unchanged |  |
| 3063 | W's workflow, the tool's landing paths | retained | unchanged |  |
| 3064 | every HP, context, hit classification, review and authori... | modified | authorization records removed |  |
| 3065 | controls RT-*, SW*, the sec. 11 mapping and countercontrols | retained | unchanged |  |

### Table at v5.5.9 line 3080 (sec. "16.5 Synthetic second configuration (test only)"; header `| Aspect | A1 | Synthetic |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 3082 | Ledger adapter | retained | unchanged |  |
| 3083 | Site map | retained | unchanged |  |
| 3084 | Replay | retained | unchanged |  |
| 3085 | Profiles | retained | unchanged |  |
| 3086 | HP | retained | unchanged |  |
| 3087 | Delegation | retained | unchanged |  |
| 3088 | Context field | retained | unchanged |  |
| 3089 | Indicators | retained | unchanged |  |

### Table at v5.5.9 line 3093 (sec. "16.5 Synthetic second configuration (test only)"; header `| Id | Case | Expected |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 3095 | Y1 | retained | unchanged |  |
| 3096 | Y2 | retained | unchanged |  |
| 3097 | Y3 | retained | unchanged |  |
| 3098 | Y4 | retained | unchanged |  |
| 3099 | Y5 | retained | unchanged |  |
| 3100 | Y6 | retained | unchanged |  |
| 3101 | Y7 | retained | unchanged |  |
| 3102 | Y8 | retained | unchanged |  |
| 3103 | Y9 | retained | unchanged |  |
| 3104 | Y10 | retained | unchanged |  |

### Table at v5.5.9 line 3111 (sec. "16.6 Fail-closed configuration validation"; header `| Defect | Outcome | Exit | Class |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 3113 | unknown `schema`, or unknown or mismatched adapter interf... | retained | unchanged |  |
| 3114 | missing required field, or unknown field | retained | unchanged |  |
| 3115 | operation not in `operations` | retained | unchanged |  |
| 3116 | missing or failing review chain (sec. 6.3); reviewer equa... | retained | unchanged |  |
| 3117 | hash or pin mismatch of the configuration, an adapter mod... | retained | unchanged |  |
| 3118 | inconsistency: base differs from the ledger, merge off th... | retained | unchanged |  |
| 3119 | configuration controls file absent or empty for an operation | retained | unchanged |  |

### Table at v5.5.9 line 3150 (sec. "16.8 Implementation step"; header `| Step | Work | Acceptance |`)

| Line | Row (first cell) | Status | Reason | Kind / covered by |
|---|---|---|---|---|
| 3152 | S13 | modified | acceptance list: retired TR and LN ids removed; GV1-GV7, EI1-EI15 added |  |

### Rows added in v6.0d (against v5.5.9)

| Row (first cell) | Reason |
|---|---|
| `T` | traceability / notation |
| owner decisions of 2026-11-24 on the authorization model | traceability / notation |
| v6.0 review B-1 to B-4, N-1 to N-6 (v6.0a) | traceability / notation |
| v6.0a review R-1, N1-N6 (v6.0b) | traceability / notation |
| v6.0b review Q-1, O-1 (b), N-a to N-h (v6.0c) | traceability / notation |
| GV1 | object integrity and host-read controls |
| GV2 | object integrity and host-read controls |
| GV3 | object integrity and host-read controls |
| GV4 | object integrity and host-read controls |
| GV5 | object integrity and host-read controls |
| GV6 | object integrity and host-read controls |
| GV7 | object integrity and host-read controls |
| EI1 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI2 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI3 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI4 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI5 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI6 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI7 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI8 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI9 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI10 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI11 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI12 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI13 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI14 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| EI15 | execution identity, plan identity and landing controls (v6.0a-v6.0d) |
| `tool` | configuration fields of B-1, B-2 (v6.0a) |
| `repository_id` | configuration fields of B-1, B-2 (v6.0a) |
| the tool's file and workflow pins; the repository id 1156244443 | configuration fields of B-1, B-2 (v6.0a) |

Totals over every v5.5.9 table row (headers excluded): retained 422, modified 40, removed 65.
Rows added: 30.

Control rows only (tables of sec. 10.1-10.4, 13.2, 16.1, 16.5, 16.8): retained 186, modified 28, removed 58.

## 3. Implementation modules and areas (`coord2-impl-wt` at 443e871f)

Classification only; nothing was changed. v6.0a changes are marked by their review finding (B-1 to B-3, N-4 to N-6). "Remove" means the code has no counterpart in v6.0;
"modify" means it is kept with the change stated. Line numbers refer to 443e871f.

### 3a. Entry point and engine (`tools/ledger_coverage.py`, `tools/ledger_coverage/engine/`)

| Module | Area or function | Action | v6.0 basis |
|---|---|---|---|
| `tools/ledger_coverage.py` | wrapper `_out_from`, `_internal`, `main` | modify: remove the `sys.path.insert` of `tools/` (line 51); refuse unless `sys.flags.isolated` and no `sys.path` entry lies in the checkout, as the first statement after `import sys, os` and before the module-level `import json` and every other import (N-g); load `tools/ledger_coverage/` by location (`importlib.util.spec_from_file_location` with `submodule_search_locations`); no package scan of its own (the pre-run check covers it) | sec. 5 wrapper; sec. 6.3 execution identity point 5 (R-1, EI6) |
| `engine/__init__.py`, `tools/ledger_coverage/__init__.py`, `adapters/__init__.py` | package markers | retain | |
| `engine/authority.py` (800 lines) | `Refused` (with its `__init__`), `refuse`, `parse_authority`, `compile_forms`, `parse_form`, `reserved`, `read_thread`, `owner_comments`, `comment_record`, `counts_as_approval`, `find_approval`, `_fresh`, `_ledger_extension_problem`, `_provenance_problem`, `_ledger_events`, `_ledger_append_approval`, `_ledger_authority_approval`, `added_event_ids`, `_review_problem`, `review_path`, `ledger_review_path`, `timeline_of`, `in_force`, `_verify_ledger_change`, `verify_history`, `check_ledger_landing`, `snapshot_events`, `admit` (with its nested `revoke` and `designate`) | remove | `A`, forms, thread, edits, freeze ledger, Owner at creation, authority changes |
| `engine/authority.py` | `read_pin_table`, `admitted_by_table`, `snapshot_sha` | modify (move to the configuration-admission code, e.g. `config.py`); `read_pin_table` reads the `PREREG.md` beside the configuration and keeps its last-`Record pins` rule; a missing file, subsection or malformed row refuses | sec. 6.3 configuration admission point 2 (B-3, EI4); snapshot sha256 |
| `engine/host.py` | `HostUnavailable`; `RestHost.__init__`, `detect`, `_https_get`, `_get`, `_json`; `run_record`; `runs_for`; `artifact_sha256`; `sha256`, `environment` | retain; modify `detect` (the job's own repository and run id only) and `run_record` and `runs_for` (also return `head_repository.id` and `event`) | host reads (Actions REST); B-2, N-6 |
| `engine/host.py` | `first_line`; `RestHost._graphql`, `repository`, `main_head`, `file_at`, `paths_at`, `entries_at`, `first_parent_chain`, `on_first_parent_chain`, `_tree`, `_entry`, `file_history`, `comments`, `deletion_events`; `b64` | remove | comments, GraphQL, repository history and contents through the host API |
| `engine/host.py` | `MemoryHost` | modify: keep runs, jobs and artifacts (for GV7, TR14, X11, G-controls); remove repositories, commits, threads, merges, deletions | controls of the remaining host reads |
| `engine/gitobj.py` | `Unresolvable`, `GitRepo.__init__`, `_git`, `parents`, `subject`, `blob_id`, `read` | retain (they read through the methods modified below) | review N-5 |
| `engine/gitobj.py` | `GitRepo._batch`, `_commit`, `read_blob`, `paths` | modify: recompute every object id from type, length and content; read with replacement disabled; no lazy fetch; record entry modes and refuse non-regular entries where sec. 6.3 requires | object integrity (GV1, GV4, GV6) |
| `engine/gitobj.py` | `GitRepo.resolve`, `tree_id` (via `rev-parse`), `is_ancestor` (via `merge-base`) | modify: role commits are full ids only; trees from parsed commits; ancestry from parsed parents only | object integrity (GV1, GV3) |
| `engine/gitobj.py` | `paths` via `ls-tree`; `diff_u0` | modify `paths` to parse verified trees; retain `diff_u0` (diagnostic `line_splices`, sec. 3.4; not a decision basis) | object integrity |
| `engine/gitobj.py` | `Overlay`, `_LazyTree`, `blob_id_of`, `first_parent_chain`, `on_first_parent_chain` | retain (they already walk parsed parents) | |
| `engine/cli.py` | `build_parser` | modify: remove `--plan`, `--round` and `--config-sha256`; no pin-table option | sec. 6.3 configuration admission (B-3, N-4; EI4 (b)) |
| `engine/cli.py` | `admission` | modify: drop `auth.admit`, the simulated chain and host-thread code; keep the `--freeze` requirement, configuration from `F`, the derived pin table, local-run and replay modes; add execution identity (run record with repository, head repository and event; `T` against the configuration's `tool` pins; checkout against `T`) | sec. 6.3 (B-1, B-2) |
| `engine/cli.py` | `engine_identity` | modify: record `T` and every tool blob; compare `T`'s tree with `tool.files` and the workflow pin, the workflow blob's `uses:` entries (EI7), and the checkout with `T`'s tree | execution identity point 2 (TR15, TR28, TR48, TR50, TR52, EI1) |
| `engine/cli.py` | `stages` | modify: `rec_adm` without `owner_id`; no owner timeline | |
| `engine/cli.py` | `finish_snapshot` | modify: snapshot fields of sec. 6.3 | |
| `engine/cli.py` | `resolve`, `split_ref` | modify: full ids only (GV1) | |
| `engine/cli.py` | `UsageError`, `Parser`, `out_guard`, `RecordSet`, `rule_files`, `run`, `invocation`, `write`, `counts`, `lookups`, `declared_sites`, `load_adapter_input`, `per_edit`, `op_record`, `_with_sitemap`, `parse_segments`, `op_coverage`, `hit_regions`, `site_counts`, `hit_counts`, `op_terms`, `scope_from_record`, `candidate_with_and_without`, `native_env`, `op_execution` | retain (`RecordSet` and `op_execution` pass no owner; `native_env` keeps the host for host-run classes) | operations A-D |
| `engine/config.py` | `forbidden` field list, `retirement.owner` field and comparison, `OwnerTimeline` use, authorization lookups in `load` | modify: remove; unknown fields stay `CONFIG_INVALID`; the retired record kind `CONFIG_INVALID`; add the fields `tool` and `repository_id` with their lint and widening rule | sec. 16.2, 16.6 (B-1, B-2, N-4) |
| `engine/config.py` | `stop`, `read_ref`, `admit_module`, `non_widening`, `Loaded`, the rest of `load`, `hp_chain_check` | retain | |
| `engine/records.py` | `_owner`, `_comment`, `OwnerTimeline`; authorization loop in `lint_chain`; `owner` parameters of `supersedes_problems`, `predecessor_problems`, `widening_review_problems`, `widening_review_ok` | remove / modify | sec. 6.3 (no authorization lint) |
| `engine/records.py` | `item_list_problems`, `entries_without_id`, `item_ids`, `_person`, `Store`, `lineage_id`, review part of `lint_chain`, `lineage_heads`, `reviewers_of` | retain | review lint, lineage (DI-2) |
| `engine/checker.py` | `recompute`, `admission_mode`, `deterministic_gzip`, `verify_compressed` | retain | S7; TR46 |
| `engine/checker.py` | `accept` | modify: schema `/5`; pins `{T, tool blobs, adapters, config, F, pin table}`; no designation or authority keys | sec. 5 |
| `engine/checker.py` | `accept_with_host` | modify: `T` on `M`'s first-parent chain by the verified reader (TR29), `uses:` lines of the workflow blob under the fail-closed rule (EI7); repository and head repository ids equal to `repository_id`, event `push` or `workflow_dispatch`; `head_sha == T`; `T`'s tree and workflow blob from the consumer's verified store against the configuration's `tool` pins; artifact digest; `F`, pin table and configuration path against the landing record (EI3); remove the `main` chain and `A` checks | sec. 5, execution identity point 4 |
| `engine/replay.py` | `_reader`, `evidence_problems`, `cli` | modify: snapshot without `A` and comment fields; reads through the verified reader | sec. 5 offline replay (TR45) |
| `engine/delegation.py` | `Delegation`, `Native`, `_bytes_record`, `_replayed` | retain | sec. 7 |
| `engine/delegation.py` | `host_runs` | modify: keep only runs with event `push` or `workflow_dispatch` and repository and head repository ids equal to `repository_id`; a failed read is `delegated-evidence-missing` (GV7) | sec. 7.2 (N-6) |
| `engine/purity.py` | allowlisted schema ids `oi-owner-authorization/1`, `oi-tool-authority/2`; `tool_paths` (authority record path); word `chain` stays | modify; the A1 configuration's value set now includes the `tool.files` paths, so an engine string equal to one of them (for example a module path) is a Z9 finding to be resolved by the allowlist rule of sec. 16.1 (flag F-11) | sec. 16.1 |
| `engine/purity.py` | `lint_allowlist`, `allowed`, `engine_sources`, `string_values`, `source_values`, `config_values`, `lint_sources`, `lint_engine` | retain | Z9 |
| `engine/controls_engine.py` | `chain_world`, `chain_probs`, `o_controls` | modify: drop authorization from the chain and O4; O5, O7, O9 as modified | sec. 10.2 |
| `engine/controls_engine.py` | all other control groups (`u_`, `m_`, `k_`, `b_`, `h_`, `r_`, `rule_controls`, `n2_control`, `run`, world helpers) | retain | sec. 10.1-10.2, 13 |
| `engine/schema.py` | validator | retain | |
| `engine/schemas/oi-ledger-coverage-4.schema.json` | schema | modify: new file `oi-ledger-coverage-5.schema.json` (`/4` file retired) | sec. 5 |
| `engine/outcome.py`, `context.py`, `peredit.py`, `profiles.py`, `reconcile.py`, `rules.py`, `segments.py`, `util.py`, `selftest.py`, `pipeline.py`, `execution.py` | whole modules | retain; `pipeline.py:720` and `execution.py:282` call `is_ancestor`, which becomes the parsed-parent form above | sec. 2-4, 6.1-6.2, 8, 13 |

### 3b. Adapters and control runners (`tools/ledger_coverage/adapters/`)

| Module | Area or function | Action | v6.0 basis |
|---|---|---|---|
| `a1exit_exact_edit.py`, `a1exit_sitemap.py`, `python_frozen_replay.py`, `deleg_preserve_check.py`, `deleg_record_dir.py`, `deleg_rerun_equal.py`, `deleg_fingerprint_regen.py`, `deleg_host_run.py`, `line_patch.py`, `artifact_hash.py` | whole modules | retain (`python_frozen_replay.py` sets `sys.path` to a materialization of hash-verified frozen record blobs, not to the checkout) | sec. 7, 16.3-16.5 |
| `staged_purity_lint.py`, `a1_conformance.py`, and the control runners `a1_controls.py`, `conformance_controls.py`, `host_fixture.py`, `synthetic_fixture.py` | the module-level `sys.path.insert(0, tools)` | modify: load the package by location as the entry point does | sec. 6.3 execution identity point 5 (R-1) |
| `host_fixture.py` | `authority`, `added_event_items`, `ledger_review`, `ledger_review_file`, `World` (A, ledger, thread, designations), `bootstrap`, `freeze_files` authorization part | remove; keep a reduced fixture for a freeze `F` with a pin table, a run record and artifacts | TR1-TR3, TR5, TR13, TR14, GV7 |
| `rest_fixture.py` | `FakeRest`, `HybridHost`, `old_file_history`, `as_merge_landings` (history reader over a fake REST listing, S1-P2) | remove | repository history through the host API removed |
| `synthetic_fixture.py` | `OWNER`, `AUTH_TIME`, authorization records in `Syn` (`chain`, configuration authorization), `retirement.owner` | modify: drop authorization records; keep writer, reviewer, widener | sec. 16.5 controls unchanged in outcome |
| `synthetic_fixture.py` | `y_controls`, `z_controls`, `x_controls`, `z9_controls`, `Runner`, helpers | retain (X10 as modified) | |
| `a1_controls.py` | `k1_graph` authorization fixture (line 1034); `chain_refusal` | modify: no authorization record; CHAIN-REFUSAL stays (unreviewed draft refused) | |
| `a1_controls.py` | every other function (RT-*, V-*, sweeps, Z9g, Y8) | retain | sec. 10.3, 11 |
| `a1_conformance.py` | controls (WB, S11-56..58, N3-N18, R18, R19) | retain; its import line as above | |
| `conformance_controls.py` | `TR` class and `tr_controls`; `k7`; `cfg_field_run`; `world_with_owner`, `world_with_authority`, `change_authority`, `authority_change_controls`, `ledger_controls`, `f1_controls`, `f3_controls`, `_r4_*`, `r4_b1_controls`, `r4_b2_controls`, `r4_b2_provenance_controls`, `r4_n2_controls`, `r5_k1_controls`, `r5_k2_controls`, `_point5`, `_full`, `_point7`, `_owner_change`, `_designate`, `_form`, `_ledger_*`, `_landing`, `_owner_at_creation_refusal`, `tr54_tr61`, `tr62_tr64`, `tr65`, `tr66_tr70`, `ln9_ln12`, `_auth_doc`, `ledger_event_verdicts`, `_p5`, `_fullx`, `_refused5`, `_unreviewed`, `_next`, `tr32_own`, `r6_g1`-`r6_g5`, `r6_g7`-`r6_g9`, `r7_b2`, `_r7_*`, `r7_n5*`, `s1_p2_history_controls` (implementation ids R3-F1, R3-F3, R4-B1, R4-B1-GUARDS, R4-B2, R4-B2-PROV, R4-N2, R5-K1, R5-K2, R6-G1-G5, R6-G7-G9, R6-EV, R7-B2, R7-N5*, TR32-OWN, S1-P2-*, S1-Q8) | remove, except: `tr_controls` and `k7` are rewritten for TR1-TR3, TR5, TR13-TR15, TR28, TR29, TR48, TR50-TR52, GV1-GV7 and EI1-EI15 (EI6 and EI8-EI15 as subprocess runs of the entry point, and of the pre-run check's program extracted by the rule of sec. 6.3 point 5 (the single-quoted `-c` argument of the single `run:` line of the step named `pre-run pin check`), on trees materialized under `--out` with `GITHUB_REF` and `F` set per case, as the review's `probe/run_probes.sh` does; EI9 builds its `.pyc` for the running interpreter's cache tag; EI7 on workflow blobs); R4-N2 (result bound to the run's artifact) is kept as part of the TR28-TR30 consumer controls | removed machinery |
| `conformance_controls.py` | `f2_controls` (R3-F2), `r4_b3_controls`, `_r4_class_scenario`, `r4_b3_duplicate_controls` (R4-B3, R4-B3-DUP), `r5_n6_controls` (R5-N6), `r6_g6` (R6-G6) | retain, with authorization removed from their chains | review lint, item ids, class records, lineage |
| `conformance_controls.py` | `_chain`, `_variant_doc`, `LN`, `_invalid`, `_clean`, `_ln_pat_v2`, `ln1_ln8` | modify: chain without authorization; LN4 as modified | DI-2 |
| `conformance_controls.py` | `acceptance_controls` (X11), `replay_controls` (TR45), `g_controls` (G4-G9), `r_controls` (R16, R17), `a12r`, `z9h`, `z11_s4a`, `open_controls`, `git`, `commit_files`, `write`, `main`, report helpers | retain; `acceptance_controls` and `replay_controls` modified for the `/5` snapshot; `a12r` as modified | |

### 3c. Records and documents of the landing (`verification/audits/foundations/ledger-coverage-tool-20261123/`)

| Path | Action | Reason |
|---|---|---|
| `README.md` | modify | it describes `A`, the freeze ledger, forms, "Owner at creation" and host history reads; ESC-6's separately reviewed correction of its classifications stays a separate change (sec. 15 item 11) |
| `records/side-change-classes-v1.json` | modify (re-pin) | it pins every landed path, including `engine/authority.py`, `rest_fixture.py` and `host_fixture.py`; a new version pins the v6.0 landing |
| `controls.json` | modify | the TR, LN and WB expectations as in table 2; GV1-GV7 and EI1-EI15 added |
| `rules/*.json`, `records/gr58-hit-classification-v1.json`, `records/repo-scope-v1.json`, `delegation-draft.json` | retain | no authorization content; ESC-1 to ESC-5 dispositions unchanged |

Counts over the 55 landed paths (`work-v60/landed.txt`): remove 2 (`engine/authority.py`, whose
`read_pin_table`, `admitted_by_table` and `snapshot_sha` move to the admission code, and
`adapters/rest_fixture.py`); modify 21 (the entry point `tools/ledger_coverage.py`; engine: `host.py`, `gitobj.py`, `cli.py`, `config.py`,
`records.py`, `checker.py`, `replay.py`, `purity.py`, `controls_engine.py`, `delegation.py`, the output schema;
adapters: `host_fixture.py`, `synthetic_fixture.py`, `a1_controls.py`, `conformance_controls.py`,
`a1_conformance.py`, `staged_purity_lint.py`;
records: `README.md`, `side-change-classes-v1.json`, `controls.json`); retain 32 unchanged. The
`__pycache__` files in the worktree are untracked build products, not modules.

### 3d. The pinned workflow (not in the implementation at 443e871f)

The implementation holds no workflow file (review v6.0a). The workflow that `tool.workflow` will pin is
written with the implementation of v6.0c: it receives `F` and the configuration path as inputs,
fetches `F` by full id, runs the pre-run pin check (refusing unless `GITHUB_REF` is `refs/heads/main`
and `F` a full 40-hex id) as one inline `python3 -I -S -B -c` step named `pre-run pin check`, runs the
entry point with `python3 -I -B`, uploads the result, and meets the review checklist of sec. 6.3
point 5. `engine/host.py`'s `run_record` returns `head_branch` as well (N-c), and the tool refuses
unless it is `main`.

## 4. Guarantee preservation

Each scientific or technical verification guarantee of v5.5.9, where v6.0 keeps it, and its
controls. "Unchanged" means the v5.5.9 text and controls are byte-identical in v6.0.

| # | Guarantee (v5.5.9) | v6.0 location | Controls | Status |
|---|---|---|---|---|
| G1 | Exact-commit binding of the plan: the configuration is read only from `F` and admitted only if the governing pin table lists it with its sha256; the pin table is not caller-chosen | sec. 6.3 configuration admission 1-2 (last `Record pins` subsection of the `PREREG.md` beside the configuration); sec. 5 (same `F` and pin table as the landing record) | TR1, TR2, TR3, TR5, O6, EI3, EI4 | kept (v6.0a, B-3, N-1); residual F-2 |
| G2 | The executed tool code equals independently fixed pins; extra files refused | sec. 6.3 execution identity 2; sec. 5; 16.2 `tool.files`; 16.7 | TR28, TR48, TR51, TR52, X10, EI1, Y8, Y10 | kept (v6.0a, B-1): pins held by the configuration at `F` instead of `A.engine_pins` |
| G2a | The producing workflow equals its fixed pin, and is the one that ran (event rule) | sec. 6.3 execution identity 1-2; 16.2 `tool.workflow` | TR15, TR50, EI2 | kept (v6.0a, B-1): pin held by the configuration instead of `A.workflow` |
| G3 | Evaluated commits are explicit inputs, recorded, never the run's `head_sha`; equal the landing record's | sec. 6.3 execution identity 3; sec. 5 | TR29, TR30 | kept |
| G4 | Result binding: the accepted result is the producing run's artifact, by sha256; compressed result verified; deterministic output | sec. 5; 16.7 | TR46, X10, R4-N2 (implementation), CI double run | unchanged |
| G5 | Hash integrity of objects read | sec. 6.3 object integrity (now every git read, recomputed ids, replacement and grafts ignored, parsed parents, regular entries) | GV1-GV6; integrity errors of sec. 5 | kept and extended (v5.5.9 trusted host-served contents) |
| G6 | Ledger and edit completeness: splices equal P's application of the edit list; P's selection; stricter refusals (i)-(iii) | sec. 6.1 | S11-56, S11-57a-d, S11-58a-k | unchanged |
| G7 | Unrelated-change detection: every path of `X` and of `C`'s commits in exactly one class; `unauthorized-change`, `unledgered-file-change` | sec. 7.1, 13.1 | R16, R17, H4, M-controls, row 14 countercontrol | unchanged |
| G8 | Landing composition and reconciliation conditions R1-R13 | sec. 13.1, 13.3 | N3-N18, R15, R18, R19, Z11 | unchanged |
| G9 | Corpus and mirror consistency; pins; census registry; Lean docstring-only | sec. 11 rows 8, 9, 10, 12 | sec. 11 countercontrols, SW1, SW2 | unchanged |
| G10 | Historical provenance (HP), region walk, mergers | sec. 3 | H1-H7, RT-H0, RT-T0 | unchanged; the walk's parents come from the verified reader |
| G11 | Context rule and indicators | sec. 4 | K1-K10 | unchanged |
| G12 | Profiles, deny and allow rules, fingerprints, allowances, widening | sec. 6.1, 6.2, 6.4-6.6, 6.3 widening | V1-V27, L1-L4, A1r-A11r, S1r, S2r, WB1-WB15, N-W, A12r | unchanged except the widening review needs no owner authorization (A12r modified) |
| G13 | Independent review of every record (non-author, coverage of every item, bound to the exact blob) | sec. 6.3 | O1-O3, O5-O9 | kept; only the owner-authorization layer removed (flag F-5) |
| G14 | Record lineage (DI-2) | sec. 6.3 | S4a, LN1-LN8, LN10 | kept; LN4 re-covers the widened-predecessor case of LN11 and LN12 |
| G15 | Delegated checks executed natively in clones at `X` and `C`; independent re-derivation; exact-head host evidence (TeX, PDF, SC-42, coverage ledger, Lean kernel, Mathlib, guards) | sec. 7 | G1-G9, RT-C, sec. 11 rows 3, 4, 10, 12, 13 | unchanged; host-run reads named as Actions REST (GV7) |
| G16 | Controls and countercontrols; control reporting; harness never acceptable | sec. 10, 11, 16 | X11, B6 reporting, Z1-Z11, Y1-Y10, RT-* | unchanged |
| G17 | Offline replay byte-equal except admission | sec. 5 | TR45 | unchanged in rule; the snapshot carries fewer (authorization) fields |
| G18 | Fail-closed outcomes, exit codes, wrapper, precedence | sec. 5, 9, 16.6 | X1-X9, Z1-Z8 | unchanged |
| G19 | Host-read failure never falls back | sec. 6.3 host reads | GV7 (re-covers TR21's technical part) | kept |
| G20 | Configuration independence of the engine (purity) | sec. 16.1 | Z9a-Z9h | unchanged; allowlist loses one retired schema id |
| G21 | Local runs never acceptable | sec. 6.3 admission 4 | TR13 | kept |
| G22 | Result produced in another repository or fork never accepted | sec. 6.3 execution identity 1, 4; sec. 5; 16.2 `repository_id` | TR14 | kept at the tool and the consumer (v6.0a, B-2: repository and head repository ids against `repository_id`) |
| G23 | `head_sha` on `main`'s first-parent chain (v5.5.9 TR29 first case) | sec. 6.3 execution identity point 6; sec. 5; sec. 13.4 | TR29, EI5, EI14 | kept: ERROR at the tool unless the run record's `head_branch` is `main` (v6.0c, N-c; no new read), and non-acceptance at the consumer against `M` from `git ls-remote`, walked by the verified reader (v6.0b, R-1); keeps `T` reachable from `main` (sec. A.42) |
| G23a | Nothing outside the pins executes, in every run of the pinned workflow: v5.5.9's workflow clauses "verify the tool blobs against `engine_pins` before executing" and "run the tool only from that tree" (sec. 6.3, `A.workflow`) | sec. 6.3 execution identity point 5: the pre-run pin check against the configuration's `tool.files` before the entry point runs (the first clause, restored by owner decision O-1 (b)); `-I`, loading by location and the isolation check before the first import (the second clause); the fail-closed `uses:` rule and the workflow review checklist; delegated checker runs governed by sec. 7 as in v5.5.9 | EI6-EI15, TR15, TR50; consumer repetition TR28, TR51, TR52 | kept (v6.0b R-1; v6.0c O-1, N-b, N-f, N-g, N-h) |

No guarantee in this list is weakened by a removed row: every removed row tested authorization only,
or its technical part is named in table 2 with the retained control that covers it. The four points
where v6.0 lost a technical binding together with the authority record (review B-1 to B-3: tool
code, workflow, repository, pin table) are bound again in v6.0a to the configuration at `F`, which
is technical identity, compared, and records no approval. v6.0b restores the on-`main` binding
(G23) and states what may execute (G23a), closing review v6.0a's R-1 (CX-3, CX-4). The fresh
independent review is asked to confirm this against v6.0a and v5.5.9.

## 5. AGENTS.md check (main 9deb6956)

Every rule that mentions authorization, frozen plans, owner decisions or automated writes.
Conclusion: v6.0 needs no amendment of AGENTS.md.

| Rule | What it says (relevant part) | Effect of v6.0 | Amendment needed |
|---|---|---|---|
| RULE §A.29, Layer-0 test | revisions judged by stated controls | no premise touched | no |
| Code Review Rules: freeze and head movement (§A.39) | round freezes at `F` designated by the owner | the A1 plan is not a native V3 round (P §25.2); its designation stays the owner's | no |
| §A.26 provenance integrity | quarantine, replay | replay kept (sec. 5) | no |
| §A.39 native rounds | owner designates `F` and `E`; receipts | the tool checks no V3 chronology, before or after | no |
| §A.40 CI-first | heavy work in CI; shared stores | object integrity reads any store, refuses missing objects, fetches nothing; native clones stay full clones | no |
| §A.42 items 1-8 | durable evidence; "an owner designation a record relies on is quoted in that record with its author and time" (item 7); off-`main` tracing (item 8) | v6.0 relies on item 7 exactly: the landing record quotes the owner's approval; the tool does not check it. v6.0b requires `T` on `main`'s first-parent chain, so the commit a landed result names is reachable from `main` (items 1, 3, 8; review v6.0a R-1) | no |
| §A.43 items 1-6 | PR-first; publication is not authorization; dispatch needs owner authorization | unchanged; the tool performs no dispatch or write | no |
| §A.44 structured evidence | verdicts read exit status, host step records, schema files | kept (sec. 5, 7.2) | no |
| §A.45 rules 1-7 | authorization is recorded owner comments linked from Issues; Issues confer no scientific status | v6.0 leaves authorization in this procedure; the tool reads no Issue | no |
| §A.46 | established claims; unverified premises | unchanged | no |
| §A.47 | Goal link | the design's Goal link is kept | no |
| §A.48 | canonical clarity; identifier migration needs owner approval | removed ids are retired, not renumbered; no identifier migration (flag F-6) | no |
| §A.49 rules 1-3 | checks and read-back for automated GitHub writes | the tool writes nothing to GitHub | no |
| §A.49 rule 4 | "In a governed thread ... in which a frozen plan, an authority record or an owner decision admits the owner's form comments, no automated text whose first line begins ... with `oi-` is written"; existing `oi-` comments not edited by automation | under v6.0 no authority record exists and the tool admits no form comment, so the "authority record" alternative does not arise; the rule stays correct for the other alternatives and for existing `oi-` comments; it is conditional and does not assert that an authority record exists | no (observation F-7) |
| §A.50 items 1-6 | merging, freezing and amending the plan, its trials and execution, designations need owner approval each time | this is exactly the procedural approval v6.0 relies on | no |
| §A.51 work packages | owner authorization of bounded work | unchanged | no |
| Honesty conventions, §A.28 | repo minimalism | v6.0 removes the authority record, ledger and fixtures from the landing | no |

## 6. A1 plan `P` (4c79be64) and the removed machinery

Read with `git show` in `<repo>` (the commit was present; nothing was fetched):
`PREREG.md` (7571 lines), `edits_check.py`, `preserve_check.py`, `guards_check.py`, `ledger.json`,
`edits.json` and `t0_jobs_44939798305.json`, searched for the authority record, `authority.json`,
the freeze ledger, `oi-freeze`, `oi-authority`, `oi-owner-authorization`, `ledger_coverage`,
comments, GraphQL and designation. Finding: **`P` relies on none of the removed machinery.** It
predates the tool's authority design, cites no tool path and reads no comment thread or GraphQL.

Items for the later, separately authorized plan amendment (no plan text is proposed here):

| # | Where | What depends on the removed design | Item for the amendment |
|---|---|---|---|
| P1 | v5.5.9 sec. 15 item 0a, sec. 6.3 (`A.plans`: plan id, thread, rounds, `pin_table_path`) | the planned amendment was to refer to `A`'s values and could not set them | the amendment does not refer to `A`, a plan id or round in `A`, a thread or the freeze ledger |
| P2 | v5.5.9 sec. 6.3 admission point 6 ("its content is authenticated by the owner's designation of exactly `F`") | designation checked from comments | the designation of `F` stays procedural as `P` §26.3 step 4 and §25.7 item 1 already state; the amendment states which record quotes it (§A.42 item 7) |
| P3 | v5.5.9 sec. 11 commands (with `--plan`/`--round` in the implementation) | the run's plan and round looked up in `A` | the amended sec. 11 commands carry `--freeze F` and `--config F:<path>`, and no plan id, round id or pin-table argument |
| P4 | v5.5.9 sec. 16.2 `records` and the staged A1 configuration draft (sha256 75558ee3…, outside the repository) | authorization records referenced by the configuration; `retirement.owner` compared with `A` | the frozen A1 configuration references records and reviews only; `retirement.owner`, if kept, is informational |
| P5 | v5.5.9 sec. 5 durable evidence | freeze-ledger events appended at acceptance with an `oi-freeze-ledger/1` comment | the plan's landing step names no ledger append and no form comment |
| P6 | `P` §26.3, §25.7, `preserve_check.py --plan`, `--trial-sha`, `--run-id` ("designated") | none: these are explicit commit and run arguments the checker verifies, with the owner's designation procedural | no change needed for v6.0; noted because they use the word "designated" for explicit inputs |
| P7 | `P` §0 and owner-decision quotations (#1169 comments) | none: quoted owner decisions under §A.42 item 7 | none |
| P8 | v6.0a sec. 6.3 (configuration admission point 2, execution identity), sec. 16.2 (review B-1 to B-3; owner item 4) | the tool reads its fixed reference values from the plan's frozen configuration | the plan's frozen configuration carries the `tool` pins (every tool file and the producing workflow, by blob) and the `repository_id` (1156244443 for A1), and lies beside the `PREREG.md` whose last `Record pins` subsection lists it and its review record. P's PREREG has twelve `Record pins` subsections (§26.4, §31.11, §31.14, §31.16, §31.18, §31.20, §31.21, §31.23, §31.25, §31.27, §31.29, §31.31); the one in force is the last, §31.31 (N1). The pinned workflow meets execution identity point 5 (it runs only the pre-run pin check, the entry point, fixed `git` commands and the actions it names by full commit id), and the tool commit `T` lies on `main`'s first-parent chain when the plan's checks run (v6.0b, R-1). The workflow carries the pre-run pin check and receives `F` and the configuration path as inputs (v6.0c, O-1 (b)) |

## 7. Open items and flags

Flags after v6.0d (stated, not resolved):

- **F-1. Tool commit on `main`.** Restored (v6.0b, R-1): the consumer requires `T` on `M`'s
  first-parent chain (TR29), `M` resolved by `git ls-remote` against the repository `repository_id`
  names and walked by the verified reader. The v6.0 and v6.0a statements that it is not checked are
  gone.
- **F-2. Plan record directory (residual of B-3).** The pin table is now derived: the last
  `Record pins` subsection of the `PREREG.md` beside the configuration, with no pin-table argument
  (EI4). Which directory of `F` is the plan's is still identified by the configuration path, a
  caller input that the result records and the consumer compares with the landing record (EI3). A
  second directory of `F` with its own `PREREG.md` listing its own configuration would be admitted
  if named. Fixing the directory inside the tool needs a reference value outside `F` and the
  caller, which is what the authority record held; v6.0a adds none (owner: no additional
  infrastructure), so the directory is confirmed with `F` procedurally (sec. 6.3 now names the
  configuration path in that confirmation, N2), and P8 names it in the plan. Review v6.0a judged
  this an acceptable procedural residual.
- **F-3. Repository identity.** Resolved by B-2 (`repository_id`; repository and head repository
  ids checked at the tool and the consumer; TR14 corrected).
- **F-4. Workflow.** Resolved by B-1 (`tool.workflow` pin; event rule; TR15, TR50, EI2).
- **F-5. Owner acceptance condition 8.** Its "authorization lint" part is removed as owner decision
  item 1 directs; the review found this meets the owner's decision F5.
- **F-6. Class names.** Kept as identifiers, with the fixed `class_meaning` table in every result
  (sec. 5). Human-readable texts use technical terms; as the owner directed, no text-lint control
  is added, so this is checked in review of the tool's strings.
- **F-7. AGENTS.md §A.49 rule 4** names "an authority record" conditionally; no amendment needed
  (table 5; the review agrees).
- **F-8. Verified reader.** A strengthening over v5.5.9 (the review agrees).
- **F-9. Landing documents.** README and `side-change-classes-v1.json` change with the
  implementation; ESC-6 stays separate.
- **F-10. Reconciliation row N14** still says "the record's approved text" (a reconciliation record's
  expected text, sec. 13.3 R6). It is outside N-3's scope (sec. 6.2 and the WB rows) and is left
  unchanged to keep the correction bounded; it carries no owner-approval meaning.
- **F-11. Purity value set.** With `tool.files` in the A1 configuration, its paths join Z9's value
  set; any engine string equal to one (a module path) becomes a Z9 finding for the implementation
  to resolve under sec. 16.1's allowlist rule.
- **F-12. Event rule for `ci` and `pdf` (N-6).** Applied as one clause in sec. 7.2. Exact-head
  evidence on `X` must come from a `push` or `workflow_dispatch` run in the repository
  `repository_id` names; P's own trial procedure dispatches `verify.yml` (P §26.3 step 3), which
  meets it. Evidence from another event is `delegated-evidence-missing`, never PASS.
- **F-14. Workflow run steps.** Point 5's rule on the workflow has mechanical parts (the pre-run pin
  check, EI8-EI13; the fail-closed `uses:` line rule, EI7) and a content part checked against the
  explicit checklist of sec. 6.3 point 5 when the configuration's review covers `tool.workflow`;
  the pin then fixes the content (TR15, TR50), and TR29 bounds every file of `T` to code merged on
  `main`. Parsing shell steps mechanically would add infrastructure; it is not added (review v6.0b:
  acceptable).
- **F-15. Interpreter.** The interpreter, its standard library and any packages installed in the
  runner image are part of the host-runner trust (sec. 6.3, residual trust). Isolated mode keeps
  the checkout and the environment off the import path; it does not verify the image.
- **F-16. The CX-3 tree and the pre-run check (EI14).** The pre-run check examines the entry point
  and `tools/ledger_coverage/` only, so it does not refuse a `tools/hashlib.py` beside them. Such a
  file never executes (isolation, EI6). At a branch `T'` the pre-run check itself fails (`GITHUB_REF`,
  O-4, EI15), so nothing runs; the tool's `head_branch` refusal (TR29) and the consumer's
  non-acceptance remain behind it. At an on-`main` `T` the run is unaffected.
  Widening the pre-run check to the whole `tools/` directory would refuse every legitimate tool of
  the repository and is not done.
- **F-17. Optional entry-point package scan (review v6.0b Q-1).** Not included: with the pre-run
  check (O-1 (b)) it would be a second mechanism for the same property.
- **F-18. `head_branch` (N-c).** The tool-level refusal reads the run record's `head_branch`, which
  point 1 already reads; no new host read. It is host-attested, like the rest of the run record;
  the binding check stays the consumer's first-parent walk. `head_branch` may also name a tag
  called `main` (review v6.0c, inferred); the pre-run check's `GITHUB_REF` test
  (`refs/heads/main`, O-4) tells a branch from a tag and runs before any tool code.
- **F-19. Trigger.** A run of the pinned workflow without `F` and the configuration path as inputs
  fails the pre-run check, so a `push` run cannot reach `"chain"`. Review v6.0b's procedural
  recommendation (a `workflow_dispatch`-only workflow for plan configurations, sec. A.43 item 4) is
  left to the workflow's review; EI2 is unchanged.
- **F-20. Line counts of earlier change notes (N-a).** Counting every `-` and `+` line after the two
  diff headers: v6.0 from v5.5.9 removes 577 and adds 312 (`CHANGES-v6.0`'s handback said 477 and
  295); v6.0a from v6.0 removes 106 (stated 101); v6.0a from v5.5.9 removes 594 (stated 518); v6.0b
  from v6.0a removes 30 (stated 29); v6.0b from v5.5.9 removes 596 (stated 520). The earlier counts
  missed removed lines that begin with `-`. The earlier notes are records and are not edited;
  `CHANGES-v6.0c.md` states the corrected figures.
- **F-13.** `CONFIG_UNREVIEWED` also names refusals unrelated to review (run record unreadable, a
  corrupt object, a run event or repository mismatch). The identifier is kept (review N-4: harmless).

Nothing in the corrections needed additional infrastructure or a replacement authorization
mechanism, and none weakens a guarantee of v5.5.9, v6.0 or v6.0a; F-2's residual is the one point
the bounded corrections do not close inside the tool.

Open items:

1. Focused independent delta review of v6.0d against v6.0c (owner decision; sec. 15 item 10).
2. ESC-1 to ESC-4 (unresolved A1 evidence gaps), ESC-5 (administrative) and ESC-6 (README and S1
   classification correction) stay under the accepted Q10 disposition (sec. 15 item 11).
3. The owner decisions of 2026-11-24, including the v6.0a to v6.0d decisions, are to be cited with comment
   ids once recorded (sec. 15 item 1; review N-7).
4. The plan amendment items P1-P5 and P8 of table 6, under their own authorization.
5. Implementation of v6.0d is not authorized by this design; table 3 is its scope.
6. The WN figures of v5.5.9 sec. 0.3 still need their independent recount (sec. 15 item 5).
7. **O-2** (review v6.0b, unchanged): `P` (4c79be64) is not an ancestor of `main` 9deb6956. The
   reachability of `F` from `main` at landing is a sec. A.42 item 8 question, unchanged from v5.5.9.
8. **O-3** (review v6.0b, unchanged; pre-existing, inferred): the delegated clones of `X` are checked
   out with the runner's global git configuration; a configured `filter.lfs` driver with a
   `.gitattributes` in `X` could make a working tree differ from `X`'s blobs for checkers that read
   files. To be handled in the implementation's clone step (for example disabling the filter, or
   comparing checked-out files with the blobs).
