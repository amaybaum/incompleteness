# Codex closeout r1: #1278, #1280, #1281 (proposal, not executed)

**Standing.** A closeout and dependency-reconciliation *proposal* for the coordinator. It is to be
reviewed and signed off by the owner before anything in it is executed. Writer: Claude Code,
2026-11-15. Authority: owner `amaybaum`, #1169 c.6891808569 (2026-11-15T08:39:13Z), wave 1 item 5:
"#1278, #1280 and #1281: Claude takes over the documentary closeout and dependency reconciliation
from idle Codex. All reviewed evidence is kept, and no merge is made." Codex idle: #1169
c.6891499007 (2026-11-15T08:09:55Z).

**What was done to produce this.** Read-only: GitHub REST reads of the three PRs (body, commits,
reviews, comments, check runs), of the accountable Issues and of the upstream PRs' states; branches
fetched by name; `git show`/`git grep` against `origin/main` at `75cc51009aebcfb17c1bbf76d149760c540aac3b`
and against the RO-1 drafts on PR #1294 (branch `research/ro1-sector-c-1169-20261114` at `f86dd1f7`,
directory `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`). Byte checks
listed in §6. Nothing was pushed, committed, commented, closed, moved, merged or changed on GitHub.
No scientific claim is assessed anew here; the scientific verdicts cited are those of the recorded
reviews.

***

## 0. Summary

| PR | Current head | What it is | Review state at the head | Recommended disposition |
| --- | --- | --- | --- | --- |
| #1278 NATIVE-APPARATUS-SRC-1 | `7086bd3079b16a0340a553ca9f089d50c5591fc7` (parent `d8b74527`) | Bounded source stop: no executing native producer of the ready resource/request in the inspected packet; physical source NOT PASSED | Scientific head `d8b74527`: non-author ACCEPT 5897621232, ChatGPT ACCEPT 5898054706. Documentary child `7086bd30`: **no review yet** | **(a)** finish the focused non-author review of the `d8b74527..7086bd30` delta; then keep as a reviewed draft that is a complete §A.46(8) landing candidate awaiting a separate owner merge decision |
| #1281 SEL-DISC-1 | `3c445e6c20e832a338749c20faee5620d2b7ced5` (parent `37e19f3d`) | Conditional IC₂ discriminator: PR protocol gives `J=2`, classical-local and quantum-local comparators give `J≤1`; native protocol and principle unsourced | Scientific head `445b17f7`: REVISE 5897663327 → ACCEPT 5897727347, ChatGPT ACCEPT 5898055055. Publication child `37e19f3d`: ACCEPT 5898298958, ChatGPT 5901719219. Documentary child `3c445e6c`: **no review yet** | **(a)** as #1278, for the `37e19f3d..3c445e6c` delta |
| #1280 older-evidence packet | `b56d9271074950bf41f17a8b4ddf1ca1f1fd8273` (parent `584c757b`) | Audit/decision proposal for #1226/#1221/#1219/#1082, plus research-branch custody of four historical artifacts (147,390 bytes in a 148,006-byte ZIP) | Packet `116d6e90`: REVISE 5897770820 → ACCEPT 5897816167, ChatGPT ACCEPT (proposal only) 5898063077. Custody `584c757b`: ACCEPT 5902077541, ChatGPT ACCEPT 5902527446. Scope-proposal child `b56d9271`: **no review yet** | **(a)** focused review of the two-file `584c757b..b56d9271` delta, then keep as a reviewed custody draft. Do **not** prepare the six-path landing child now (§4.4); (c) offered to the owner only as an alternative |

All three: open, draft, unmerged; 65 commits behind `main`; exact-head ordinary CI green (26
success, 1 expected `A42 exclusion` skip each). Nothing on `main` cites any of them. Option (b) is
not recommended for #1278/#1281 because their documentary children already *are* the minimal
landing children (§2.4, §3.4); it is not recommended for #1280 because no landing basis or owner
scope selection exists yet (§4.4). Nothing is to be deleted.

***

## 1. Facts common to all three

1. **Policy.** #1283 merged as `dfeec843bec08443b25cffe34d33dc8401c3b604`; §A.46 item 8 (preserved
   research records) is operative on `main` (adopted per #1169 c.6874035457). The PR packages written
   on 2026-11-13 and at `584c757b` say #1283 is unadopted; the 2026-11-14 documentary children
   (`7086bd30`, `3c445e6c`, `b56d9271`) already cite `dfeec843` as operative.
2. **§A.46(8) conditions** (all must hold before preservation on `main`): substantive nonredundant
   result; documented scope and evidence limits; an independent non-author review **and a ChatGPT
   exact-head review**, plus the landing checks including §A.42 item 8 tracing; accountable Issue,
   verification status and remediation plan per open gap; explicit rationale and a separate recorded
   owner merge decision.
3. **ChatGPT-optional decision is scoped.** #1169 c.6891230989 makes ChatGPT review optional "for
   the S3 units authorized in c.6890079967". It does not amend §A.46(8)'s ChatGPT exact-head
   requirement for preservation records. See owner question Q1.
4. **Main drift since the PR base `c3b5f37a`.** Two first-parent merges (#1283, #1304), 63 files.
   No file under `tools/`, `.github/` or `verification/infrastructure/` changed, so the guards that
   ran on the exact heads are the guards on `main`. None of the three package directories, and none
   of the upstream source directories they copy from, exists on `main`; there are no path
   collisions.
5. **CI.** Exact-head check runs: #1278 run 43582966959, #1281 run 43583001112, #1280 run
   43583034682; each 27 check runs, 26 success and 1 skipped. These were `pull_request` runs on a
   synthetic merge with the base of 2026-11-14 ~10:00Z; #1304 landed after. Given item 4, the risk is
   low, but no run exists against current `main`.
6. **Branches kept.** `research/codex-native-apparatus-20261113` (`7086bd30`),
   `research/codex-selection-discriminator-20261113` (`3c445e6c`),
   `research/codex-older-evidence-20261113` (`b56d9271`), and two staging refs pointing at already
   reviewed ancestors, `research/codex-selection-publication-20261113` (`37e19f3d`) and
   `research/codex-preserved-evidence-20261114` (`584c757b`). All are to be kept.
7. **Codex's outstanding requests.** Each of the three documentary children ends with "focused
   independent non-author review … has not yet occurred"; Codex asked for permission to launch
   read-only review agents (PR comments 6875712875, 6875713759, 6875723764). That request is the
   open item this closeout takes over.

***

## 2. #1278 — NATIVE-APPARATUS-SRC-1 (cited "NAS" in RO-1)

### 2.1 Current state

- Head `7086bd30`, three commits: `0245523b` (WIP) → `d8b74527` (scientific r1) → `7086bd30`
  (documentary child, 2026-11-14T09:57Z). Accountable Issue #866; coordination #1032, #1169.
- Reviews: 5897621232 (coordinator relay of separate non-author review, ACCEPT at `d8b74527`, no
  findings); 5898054706 (ChatGPT exact-head ACCEPT at `d8b74527`, one nonblocking note: writer-era
  "review pending" headers). Integration assessment 6874563932 (at `d8b74527`) listed the support
  obligations: TUNE-1 sources from #1272, the O5/classical-lead review receipts, the own review
  standing.
- The documentary child adds the support those obligations name: five exact #1272 copies under
  `support/` (confirmed paper at `890fe3dd`; published paper, CONFIRM-r2, REVIEW-r1, OBJECTS at
  `c539a60c`), six verbatim review bodies in `reviews/RECEIPTS.json` (6692855851, 6692903227,
  5815049227, 6718496406, 5897621232, 5898054706), `RETENTION.md/.json`, `STATUS.md`,
  `ARTIFACTS.sha256`. In `ASSESSMENT.md` it changes only lines 3 and 167 (status wording); in
  `EVIDENCE.md` status lines plus one section. This also answers ChatGPT's nonblocking note.
- Pending: (i) focused non-author review of the delta `d8b74527..7086bd30`; (ii) ChatGPT
  confirmation of `7086bd30` if required (Q1); (iii) owner merge decision.

### 2.2 What it establishes, and at what status

A bounded negative source assessment: for the binary SM-ring rule (the G_SM/SMR conditional E-SDC
branch, not R-lin or A5) and its two-site/two-slice observer, the inspected packet identifies no
executing native producer of the joint ready input/request and lawful supply. It is a stop at a
precise first missing ingredient, **not** an impossibility theorem, not a qualified apparatus, not
an adopted premise. Evidence layer: paper-level hand reasoning and source audit, model-reviewed
(non-author + ChatGPT); no human or kernel verification. Physical source NOT PASSED. The optional
TUNE comparison carries #1272's own research-layer status and its `m+1≤ell` proviso.

### 2.3 Dependency map (§A.42 item 8)

| Citing record | Claim attached | Classification |
| --- | --- | --- |
| `main` | — | No citation found (grep of `#1278`, `pull/1278`, NATIVE-APPARATUS, the package path, all four head prefixes) |
| RO-1 `S3-U1-r5.md` §8 (and §4 rows marked [OFF]: NAS:33, :38, :70–77, :12–14, :155) | The Codex screen's ingredient rows; "a precise first missing ingredient", "not a new impossibility theorem"; two-slice projection; G_SM standing | **Support off `main`** (gap), as U1 itself records; "no §9 verdict rests on it alone" |
| RO-1 `S3-U2-r3.md` §10, §11.1 | The G_SM rows; AW-U2-2 | **Support off `main`** (gap), as recorded |
| RO-1 `U4-SOURCES-r1.md` item 1.58 | Inventory entry only ("no conclusions") | **Provenance** |
| RO-1 `S3-U4-r1.md`, `LIT-ERASER-r3.md`, `U4-CALC-r1.md`, `GAMMA-PLAN-r1.md`, `VERIFY-SL3-CC-r2.md` | — | Not cited |
| #1169 comments 6864506687, 6865063898, 6874590961, 6875729134 and others | Coordination receipts | **Provenance** (planning/governance) |
| #866 body (planning-status block) | — | Not named; the landing obligation has no row there (§A.45 rule 6; action N7) |

RO-1 cites NAS at `d8b74527`. Because `7086bd30` changes only `ASSESSMENT.md` lines 3 and 167, every
RO-1 line citation (NAS:12–14, :33, :38, :70–77, :155) resolves to the same text at the current head
(spot-checked). If #1278 lands through a merge commit, `d8b74527` becomes reachable from `main` and
these rows become **support on `main`**, with the difference (lines 3 and 167) already stated in
U1:85–93. Owner #914 c.6883249235 item 3's citation allowance names #1224, #1228 and #1281 only, not
#1278 (Q7).

Outgoing support (what #1278 itself rests on), checked against `main` now:

| Use (RETENTION.md id) | Support | Classification now |
| --- | --- | --- |
| N1 fixed rule, prior stops, OA limits | 31 objects pinned at `c3b5f37a` | **Support on `main`**. At current `main`, 29 of 31 blobs are unchanged. `AGENTS.md` differs (policy only; RETENTION N1 records it). `book/ch18-beyond.md` differs (`90ae3800` → `dd5ef436`): the one changed line is §18.9's open question on non-orientability and chirality, while #1278 consumes only §18.8 (EVIDENCE M3). Immaterial; the pin stays resolvable because `c3b5f37a` is on `main` |
| N2–N4 TUNE resource/event/precision bounds; confirmed vs. published comparison; r1 trail | Five copies in `support/`, blob-identical to `890fe3dd`/`c539a60c` (§6) | Support off `main` today; **closed on landing** by content. #1272 commits are not made ancestors; RETENTION states no ancestry premise is used |
| N5 O5/classical-lead review history | Four receipts in `RECEIPTS.json` | Off `main` today; closed on landing |
| N6 own review standing | 5897621232, 5898054706 in `RECEIPTS.json` | Closed on landing; `d8b74527` is an ancestor of the head |
| #1280 ledger/OICORE gaps | Only a disclaimer in STATUS.md:26 | **Not a dependency** (verified by grep) |

### 2.4 Recommended disposition: (a)

`7086bd30` already is the minimal landing child that integration assessment 6874563932 asked for:
exact support copies, review receipts, a claim-specific trace, status and remediation table, with the
scientific text unchanged. Preparing a further child (b) would duplicate it. What it lacks is the
focused non-author review of its own delta and, depending on Q1, a ChatGPT confirmation. After those,
it satisfies §A.46(8)'s review and tracing conditions and needs only the owner's merge decision.
Retirement (c) does not fit: the PR is reviewed active work waiting on a review and a governed
decision (§A.43 item 6).

Points the focused reviewer should check, beyond the delta's own claims:
1. Blob identity of the five copies with their originals and the twelve `ARTIFACTS.sha256` entries
   (both reproduced in §6; to be checked independently).
2. That the `ASSESSMENT.md` delta is limited to lines 3 and 167, with no scientific edit.
3. RETENTION N1–N7 against the actual uses in ASSESSMENT/EVIDENCE (§A.42 item 8).
4. The `book/ch18-beyond.md` drift (above): immaterial, and whether a one-line note is wanted.
5. Verbatim review bodies carry runtime home-directory prefixes in reviewer task identifiers (two
   lines of `RECEIPTS.json`); SC-42 does not scan JSON (Q2).

***

## 3. #1281 — SEL-DISC-1

### 3.1 Current state

- Head `3c445e6c`, five commits: `d0a09451` (WIP) → `329878be` (r1) → `445b17f7` (R1 source/status
  correction) → `37e19f3d` (owner-authorized publication cleanup: two reviewer-ID runtime prefixes
  removed from `SOURCES.md`) → `3c445e6c` (documentary child, 2026-11-14T09:57Z). Accountable Issue
  #1143; coordination #1169.
- Reviews: 5897663327 (non-author REVISE at `329878be`, R1 documentary; no mathematical blocker);
  5897727347 (focused ACCEPT at `445b17f7`, R1 closed); 5898055055 (ChatGPT ACCEPT at `445b17f7`,
  nonblocking status-header note); 5898298958 (focused publication ACCEPT at `37e19f3d`);
  5901719219 (ChatGPT publication confirmation at `37e19f3d`). An earlier exact-head CI failure
  (SC-42 local-path hits) was fixed by `37e19f3d`. Integration assessment 6874565429 listed the
  support obligations: SEL-ACCESS-1 (#1224), SEL-EXCL-1 (#1228), synthesis r3 (#1276), and the review
  receipts.
- The documentary child adds: five exact copies (`SELECTION-ACCESS-1.md` at `1b966a03`;
  `SEL-EXCL-1.md` at `0ecfddeb` and at `75681105`; `SYNTHESIS-r3.md`, `CONFIRM-r3.md` at `9eeee392`),
  eleven verbatim review bodies (5840425454, 5840851253, 5845436861, 5848321039, comment 6846240488,
  5896999231, and the five own reviews), `RETENTION.md/.json`, `STATUS.md`, an updated
  `ARTIFACTS.sha256` and `SOURCES.md`. In `ASSESSMENT.md` it changes only line 3 (status).
- Pending: focused non-author review of `37e19f3d..3c445e6c`; ChatGPT confirmation if required
  (Q1); owner merge decision.

### 3.2 What it establishes, and at what status

A conditional discriminator, D1–D8 as accepted at `445b17f7`. With the appended operational
protocol (independent fair `Z0, Z1, K`, one PR use, one fixed-schedule classical message bit), the
reversible PR countermodel gives `J=2`. Classical-local and quantum-local comparators obey `J≤1`
under the stated common-resource, all-branch and record contract. Native protocol availability and an
OI-derived information principle are unsourced. Owner #914 c.6883249235 item 4 keeps IC₂ "a
conditional discriminator, not an established physical selection law" until its four conditions are
met. Evidence layer: paper-level hand proofs, model-reviewed; not kernel-checked. No minimality,
full quantum-set selection, Born rule or physical-source PASS.

### 3.3 Dependency map (§A.42 item 8)

| Citing record | Claim attached | Classification |
| --- | --- | --- |
| `main` | — | No citation found |
| RO-1 `RO1-DEPS-r4.md` §9 (cited at `445b17f7`) | X-IC2; §5 Resources and Repeated use | **Support off `main`** (gap), "Owner item 3 (#914 c.6883249235) allows the citation" |
| RO-1 `RO1-SPEC-r3.md` (ll. 122–124, 243–244, 282, 285, 310, 321; at `445b17f7`) | The `(S, φ, μ, E, Γ, R, C)` typing; K-rec, K-res reuse; J6, J9; one-bit message row | `[R, reviewed, not merged]` → **support off `main`** (gap) |
| RO-1 `RO1-OVERLAP-r3.md` (adopted by #914 c.6883249235 item 1) | Cites SEL-DISC-1 **at `3c445e6c`**, including the STATUS.md gap table ("Open gap homes named by its newest record") | Gap homes: **provenance** (accountability). The row content O1/O2 (l. 34; ll. 46–55) is unchanged from `445b17f7`. But `3c445e6c`'s delta is unreviewed, while item 3 asks for "exact reviewed commit SHAs". **The focused review of `3c445e6c` closes this mismatch** |
| RO-1 `S3-U1-r5.md` §8; `S3-PLAN-r9.md` | P5 (l. 53), §4 (l. 79), §2 | **Support off `main`** (gap) |
| RO-1 `S3-U2-r3.md` §10 | CP-5 protocol, `J=2`, comparators, §6.3 references | **Support off `main`** (gap); F-1 to F-3 "not established" as recorded |
| RO-1 `U4-SOURCES-r1.md` item 4.8 | Inventory entry | **Provenance** |
| #1169 comments (e.g. 6865745726, 6871995883, 6874590961, 6875729134); #914 c.6883249235; #1143 c.6883250062 | Coordination; owner citation allowance and IC₂ conditions | **Provenance** (governance) |
| #1143 body (planning-status block) | — | SEL-DISC-1 has no row; SEL-ACCESS-1 does (action N7) |

Line numbering of `ASSESSMENT.md` is preserved at `3c445e6c` (only line 3 differs from `445b17f7`),
so every RO-1 line citation resolves to the same text. On a merge-commit landing, `445b17f7` and
`37e19f3d` become reachable from `main`, and the RO-1 rows above become **support on `main`**, subject
to their stated scope. The "conditional" and "not established" labels stay (§A.46 items 1 and 8:
preservation establishes no claim).

Outgoing support, checked against `main` now:

| Use (RETENTION.md id) | Support | Classification now |
| --- | --- | --- |
| S6 main sources (Main.md, OA-1-REPORT-r5, prepared-pair-source, composition-source-map, PREPARATION-SCREEN) | Pinned at `c3b5f37a` | **Support on `main`**; all five blobs are unchanged at current `main` |
| S1 SEL-MENU theorem | `support/sel-access/SELECTION-ACCESS-1.md`, blob `5c125be5` = #1224 at `1b966a03` | Off `main` today; **closed on landing** by content |
| S2 PR map and fresh/reuse grammar | Both SEL-EXCL-1 copies, blob-identical to `0ecfddeb` and `75681105` | Closed on landing; RETENTION states no ancestry premise |
| S3, S7 review history | Eleven receipts | Closed on landing |
| S4 MM-2/3/7/8 comparison | `SYNTHESIS-r3.md`, `CONFIRM-r3.md` = #1276 at `9eeee392`; receipt 5896999231 | Closed on landing for the comparison only; the synthesis's wider conclusions stay off `main` and are not premises (RETENTION "Boundaries") |
| #1280 ledger/OICORE gaps | Disclaimer only (STATUS.md:30) | **Not a dependency** |

### 3.4 Recommended disposition: (a)

Same reasoning as §2.4: `3c445e6c` is the minimal landing child the integration assessment called
for, and it lacks only its own focused review (and, per Q1, a ChatGPT confirmation). Two further
review points:
1. `reviews/RECEIPTS.json` retains, verbatim, the same runtime home-directory prefixes in reviewer
   task identifiers that the owner-authorized `37e19f3d` cleanup removed from `SOURCES.md` (six lines).
   RETENTION.md states this is deliberate: verbatim bodies, no redaction, JSON outside SC-42's scan.
   Three files on `main` already carry such identifiers in JSON or text records. This is not a
   secret under §A.42 item 4's list, but its treatment should be decided once, consistently (Q2).
2. The #1143 maintenance revision that #914 c.6883249235 item 2 assigned to Codex ("Codex holds
   in-flight #1143 work (#1281)") is **not** in #1281 and is not covered by wave 1 item 5. It is
   paused by the Codex-idle decision and needs its own writer assignment (Q6).

***

## 4. #1280 — older-evidence preservation decision packet

### 4.1 Current state

- Head `b56d9271`, five commits: `24d0fec6` → `132a4e92` (packet) → `116d6e90` (R1/R2 repairs) →
  `584c757b` (custody: ZIP of four originals, `PRESERVED-ARTIFACTS.json`, `PRESERVATION-STATUS.md`)
  → `b56d9271` (`LANDING-SCOPE-PROPOSAL.md`, `LANDING-SCOPE.json`; six proposed landing paths;
  2026-11-14T09:58Z). Accountable Issue #1169 (corrected from PR #1226 by R2).
- Reviews: 5897770820 (REVISE, R1/R2 documentary) → 5897816167 (ACCEPT at `116d6e90`); 5898063077
  (ChatGPT ACCEPT "for a bounded read-only audit and owner decision *proposal*"); 5902077541 and
  5902527446 (non-author and ChatGPT ACCEPT, "research-branch custody only", at `584c757b`).
  `b56d9271` is unreviewed; its CI is green. Integration assessment 6874562707 (at `584c757b`).
- Related new event: a fresh non-author documentary review of the actual frozen ledger
  `DISPOSITIONS-r7c.md` (SHA-256 `d3adc823…`) on #1219, review 5903131037. The historical `856fa01d…`
  identity stays unrecovered.
- Pending: focused review of `b56d9271`; the owner's scope decision; a main-retention basis; the
  frozen-ledger and OICORE version gaps (open by design); any landing review, CI and merge decision.

### 4.2 What it establishes, and at what status

No scientific result. It establishes (i) an accepted audit and owner-option proposal for four older
draft PRs: exact heads, historical CI, overlap with `main`, the 25-unit #1082 inventory as the
audit's own normalization, and preserved gaps; and (ii) independently verified **research-branch
custody** of four actual artifacts: two recovered #1221 focused review reports (R1, R2), the 84-block
matrix Page capture (M1) and its exact projection (M2). Custody is not retention on `main` and not
scientific verification. OICORE (published `a30d8d79…` vs. historical `9b82…`/`ec79…`) and the
frozen-ledger identity remain open. #1214's owner hold c.6742190639 stands.

### 4.3 Dependency map (§A.42 item 8)

| Citing record | Claim attached | Classification |
| --- | --- | --- |
| `main` | — | No citation found |
| RO-1 drafts (all) | — | **Not cited** (grep of `1280`, `older-evidence`) |
| #1278, #1281 packages | — | **Not cited**; both state the ledger/OICORE gaps are not their premises |
| #1169 comments 6872764166, 6873781833, 6874590961, 6875729134 | Custody status, decisions pending | **Provenance** (coordination) |
| #1219 review 5903131037; #1210 c.6874589871 | Actual-ledger documentary accuracy | Independent of #1280; #1280 only records it |

Incoming support needs: R1/R2 support claims made in #1221; M1/M2 support claims made in #1226 (the
#1169 dependency matrix). Neither PR is on `main`, and no record on `main` or in RO-1 uses them. So
today there is no surviving claim on `main` that needs the four artifacts (§A.42 item 5: necessity,
not exposure).

### 4.4 Recommended disposition: (a), landing deferred

1. **Finish the one pending review** of the `584c757b..b56d9271` delta (two planning files, about
   165 lines). Scope: the six-path proposal's accuracy, the unchanged eleven files and ZIP, and the
   ledger/OICORE dispositions. The PR then rests at a fully reviewed head.
2. **Keep #1280 open as a reviewed draft custody checkpoint.** Do not prepare the six-path landing
   child now, for three reasons:
   - The owner has not selected a scope (LANDING-SCOPE.json: "not selected by owner").
   - Five of the six paths do not exist yet: three new files and two rewritten. The child is real
     writing work, not reconciliation.
   - The landing basis is weak today. §A.46(2)'s support route needs a record on `main` that relies
     on the artifacts, and none does. §A.46(8) needs "a substantive, nonredundant result", which an
     audit packet plus historical review reports and a Page capture does not obviously meet; that is
     the owner's call.
   The natural trigger for a landing is the landing of #1221 or #1226. Their claims would then need
   R1/R2 or M1/M2 as support on `main`, and the six-path child becomes a support landing under
   §A.46(2).
3. **Why not (c) by default.** §A.43 item 6 retires PRs that are "only a plan or backlog
   placeholder". #1280 holds custody of actual evidence bytes and waits on a governed owner
   decision, which the same item says is "still an active PR". If the owner nevertheless prefers to
   retire it, an Issue must first carry the open work: the four artifacts and their exact blob and
   commit pins; the custody reviews; the six-path proposal; the L1 (#1210) and O1 (#1169)
   discrepancies; the conditions under which a landing becomes needed. Then close without merge,
   keeping all five refs in §1 item 6.
4. **Stale wording is left in the reviewed bytes.** `DECISION-PACKET.md` line 3 (writer-era "WIP
   pending … review") and `PRESERVATION-STATUS.md` line 61 ("#1283 … unadopted") are stale. Under the
   custody reviews' boundary they are not edited. Any eventual landing child carries a current status
   wrapper, as the six-path proposal already plans. The PR description already carries current
   status.

***

## 5. RO-1 reconciliation (cross-cutting)

- RO-1's classifications of NAS and SEL-DISC-1 as **support off `main` (gap)** are correct today.
  They become **support on `main`** only when #1278 and #1281 land, and then only at their stated
  scope; IC₂ stays conditional. Nothing in RO-1 needs editing now. After any landing, the [OFF] rows
  in `RO1-DEPS-r4.md` §9, `S3-U1-r5.md` §8 and `S3-U2-r3.md` §10 can be reclassified with the
  version difference stated, under RO-1's own authorization and review.
- `RO1-OVERLAP-r3.md` cites #1281 at the unreviewed head `3c445e6c`, unlike the other RO-1 records
  (`445b17f7`). The focused review of `3c445e6c` (action N2) resolves this without touching RO-1.
- RO-1 does not depend on #1280.
- The RO-1 minimum landing packet for #1294 (wave 2) should list #1278/#1281 as prerequisites for any
  RO-1 claim that consumes NAS or SEL-DISC-1 as support. Otherwise it should keep those rows as
  recorded gaps; landing RO-1 with an open support gap needs the §A.42 item 8 owner exception.

***

## 6. Byte and source checks performed (read-only, local)

| Check | Result |
| --- | --- |
| #1278 `ARTIFACTS.sha256` (12 entries) at `7086bd30` | 12/12 match |
| #1281 `ARTIFACTS.sha256` (11 entries) at `3c445e6c` | 11/11 match |
| #1278 copies vs. originals at `890fe3dd` / `c539a60c` (5 files) | 5/5 identical Git blobs |
| #1281 copies vs. originals at `1b966a03`, `0ecfddeb`, `75681105`, `9eeee392` (5 files) | 5/5 identical Git blobs |
| Review-body digests and byte counts in both `RECEIPTS.json` | 6/6 and 11/11 reproduce; spot-checked prefixes and suffixes against the live review bodies |
| #1278 `source-objects.json` (31) vs. current `main` | 29 unchanged; `AGENTS.md` (policy) and `book/ch18-beyond.md` (§18.9 only) changed |
| #1281 main pins (5) vs. current `main` | 5/5 unchanged |
| ASSESSMENT line stability across the documentary children | #1278: lines 3, 167 only; #1281: line 3 only |
| Copied blobs or package paths already on `main` | None |
| Exact-head check runs | 26 success + 1 skip, each |

Limits: these are identity and text checks, not a review. They do not substitute for the focused
non-author reviews in §7, which must recheck independently. No scientific content was re-derived.

***

## 7. Next actions for the coordinator

"Owner" marks an action that needs owner authorization or a decision beyond the sign-off of this
proposal. "Sign-off" marks an action that falls within wave 1 item 5 once this proposal is signed
off; it needs no separate authorization.

| # | Action | Authorization |
| --- | --- | --- |
| N0 | Present this proposal and owner questions Q1–Q7 to the owner | — |
| N1 | Check free space on the transcript filesystem (§A.40). About 11 GB free at writing | Sign-off |
| N2 | Launch three separate non-author, read-only focused reviews: #1278 `d8b74527..7086bd30`; #1281 `37e19f3d..3c445e6c`; #1280 `584c757b..b56d9271`. Include the §2.4 and §3.4 check points. No full scientific re-review | Sign-off. Codex had asked for this permission; the owner's sign-off should state that it covers N2 |
| N3 | Relay each verdict verbatim, with attribution, as a review on the exact head it reviewed | Sign-off |
| N4 | If a review requires corrections: a single-parent documentary child on the same branch (no rebase, no force-push, no merge from `main`). Inspect push-triggered workflows before pushing (§A.43 item 4). The push triggers ordinary PR CI; then a focused re-review of that child | Sign-off (documentary only). Any scientific change: **Owner** |
| N5 | ChatGPT exact-head confirmation of the final #1278 and #1281 heads, if Q1 requires it | **Owner** (Q1) |
| N6 | Append a closeout status section to each PR description: writer transfer (c.6891499007, c.6891808569 item 5), current head and reviews, remaining gates. Earlier sections stay | Sign-off |
| N7 | Planning-record maintenance (§A.45 rule 3, with a source-citing comment): rows for the #1278 landing obligation in #866's block and for the #1281 landing obligation in #1143's block, with Readiness and Authorization as recorded (`not authorized` for merge). #1280 stays under #1169 | Sign-off (recording existing decisions only; no tier or authorization change) |
| N8 | Decide whether CI against current `main` is needed before a merge decision. No tooling changed since the run. A new push (N4) runs CI automatically; a rerun or dispatch needs approval | **Owner**, only if a rerun or dispatch is wanted |
| N9 | Owner merge decision for #1278 and for #1281, each separately, after N2 to N5. Recommended landing by merge commit, so the reviewed heads become reachable (Q5) | **Owner** |
| N10 | #1280: owner chooses among keep as reviewed custody draft (recommended), select the six-path scope for a later landing child, or retire under §A.43 item 6 (§4.4 item 3) | **Owner** (Q4) |
| N11 | After any landing: notify RO-1's writer to reclassify the NAS and SEL-DISC-1 rows (§5). Do not edit RO-1 from this unit | Sign-off (notification only) |
| N12 | Keep every branch in §1 item 6; delete nothing; leave #1272, #1224, #1228, #1276, #1219, #1214, #1221, #1226 and #1082 untouched | — |

**Owner questions**

- **Q1.** Does §A.46(8)'s "ChatGPT exact-head review" need a fresh ChatGPT confirmation of the
  documentary children `7086bd30` and `3c445e6c`? Or do the ChatGPT reviews of the scientific heads,
  plus a non-author focused review of the documentary delta, satisfy it? c.6891230989 covers the S3
  units only.
- **Q2.** Should verbatim retained review bodies keep the runtime home-directory prefixes in reviewer
  task identifiers (precedent on `main`), or be redacted under §A.42 item 4, with a recorded redaction
  and a new digest? One rule for #1278, #1281 and the #1280 ZIP members.
- **Q3.** For #1278, is landing exact copies of the #1272 TUNE files acceptable, rather than waiting
  for #1272's own integration? The copies would duplicate content if #1272 later lands; that is
  harmless but redundant.
- **Q4.** #1280: which disposition (N10)?
- **Q5.** Landing method: merge commit (recommended: the reviewed heads `d8b74527`, `445b17f7` and
  `37e19f3d` become reachable, and RO-1's citations then resolve on `main`) or squash?
- **Q6.** Who writes the #1143 maintenance revision (#914 c.6883249235 item 2), now paused with
  Codex idle?
- **Q7.** Should #914 c.6883249235 item 3's off-`main` citation allowance extend to #1278 (NAS at
  `d8b74527`), as RO-1 U1 and U2 already cite it with the gap recorded?

**Not changed by this proposal.** Physical source NOT PASSED; IC₂ conditional; OI–QM equivalence
open; no premise, execution, merge, ref movement, Issue change or deletion.
