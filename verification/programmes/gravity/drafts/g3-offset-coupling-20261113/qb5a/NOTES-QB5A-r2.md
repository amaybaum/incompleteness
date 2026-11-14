# NOTES-QB5A-r2: working log for the G3 QB5(a) preregistration, revision 2

## 1. Pins and commit state

**Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.

**Branch.** `research/g3-offset-873-20261113`, in a read-only worktree.

- Head at reading time: `660152911`.
- `2e18a2dfe` adds `qb5a/G3-QB5A-PREREG-r1.md` and `qb5a/NOTES-QB5A-r1.md`. Each is byte-identical to the
  writer's r1 (checked with `cmp`).
- `660152911` adds `qb5a/REVIEW-QB5A-PREREG-r1.md`.

**Commit state, as observed when this file was written.**

- r1 is committed at `2e18a2df` by the coordinator. NOTES-QB5A-r1 §1 said that neither file was
  committed. That was true when it was written, and it is superseded by this entry (QR-26).
- r2, NOTES-QB5A-r2 and RESPONSE-QB5A-r1 are not committed.
- The writer does not commit, push or post. The branch history records commits.

**Intended location:** `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/qb5a/`.

## 2. Authority, guidance and requests

- **Authorization.** #873 c.6872004336 (`amaybaum`, 2026-11-14T04:53:01Z), as in r1.
- **Owner guidance.** #873 c.6872277416 (`amaybaum`, 2026-11-14T05:17:28Z). The writer read it first-hand
  with `gh api` (repository issue comment, read-only). It records verbatim:

  > G3 QB5(a): The preregistration-first approach is essential. The decision rule must apply equally to
  > the corpus's own metric-dependent source terms and the disputed vacuum-offset coupling, without
  > selecting F4 or F5 to obtain a preferred result.

  It also records "No additional scientific work or merge authorization is needed now. Physical source
  remains NOT PASSED; G3 remains (C)." The guidance is now on record. OQ-6 is answered, and NOTES-QB5A-r1
  §2's "record status" is superseded.
- **The coordinator's request for r2** is a session message, not an owner record. It asks for:
  - the review's blocking and should-fix findings and its nits, applied using its replacement text;
  - the recommended OQ answers, applied as pending, with the alternatives in §15;
  - the r5-derived rationales removed, with D-9 and Δ8 justified on their own or dropped;
  - X-18's second reader to be a different agent at execution, not the writer;
  - r1 left unchanged.

## 3. Sources read for r2

- `qb5a/REVIEW-QB5A-PREREG-r1.md`, in full (880 lines).
- `qb5a/G3-QB5A-PREREG-r1.md` and `NOTES-QB5A-r1.md` (the writer's own r1, compared with `cmp`).
- #873 c.6872277416, first-hand.
- **Corpus at `c3b5f37a`, for location only.** The writer displayed the opening characters of:
  - GR:340 by sentence;
  - GR:458, :468, :693, :695 and :701;
  - SM:120;
  - Substratum.md:385–393 (the non-blank lines :385, :387, :389, :391 and :393);
  - the hits of the inventory search (§5).

  No passage was evaluated against F4 or F5, and no attribute cell was formed.
- U2Ar3:313–314 (the witness's horizon mode count) was re-read, to check that no text-control sentence
  paraphrases a W0 definition (RESPONSE QR-9 note).

## 4. Changes made on provenance grounds (QR-21; review §3 item 9)

The review found four places where r1 leaned toward coexistence and (C). Each is handled as follows.

1. **The default for unqualified assertions.** r1 had no value for an assertion in the corpus's own voice,
   so it fell to Ns and could never reject F4. r2 adds As and places it in `Com`, the commitment set, on
   both the F4 and the F5 side (pending OQ-7). If the owner declines, As still makes a row potentially
   rejecting.
2. **The hedging vocabulary.** r1's word map included hedge phrases the writer had seen quoted in r5
   ("structural reading", "not presently derived", "does not adjudicate"), and its commitment side was
   generic. r2 uses the reviewer's map, drawn from AGENTS.md §A.25 and §A.33, with commitment words added
   ("established", "shown", "lemma", "corollary", "forced", "necessary"). Some hedge phrases remain, because
   they are general status vocabulary. "take … to" is added to Ps so that the external sentence TX-4
   matches; no inventory sentence motivated it.
3. **D-9's rationale.** r1 justified the status-scope test by r5's reading of one inventory passage. That
   rationale is withdrawn. r2's reason is general: a status word attaches to what it modifies, and
   external examples fix the test (r2:506, TX-1, TX-2). The test is kept.
4. **Δ8.** It is kept, with a reason that stands on its own. F4's own statement exempts the Einstein
   tensor, a functional of the metric alone, and Δ8 asks whether that exemption extends. Its candidacy
   rests on F4's statement, and GRT decides it (r2:683–685). Its predicate is A2 = M-pure. Whether any
   row, W0 included, falls in its class is left to the tests and to the second reader.

Further changes made for the same reason:

- **Text controls.** TX-8, TX-10 and TX-12 replace three of the reviewer's sentences, which resembled a W0
  definition or inventory sentences (RESPONSE QR-9 note). This was done so that no required control value
  presets a near-paraphrase of a row.
- **Remaining limit.** The rule is still written by a writer who has read r5's per-passage readings.
  X-18's second reader, a different agent with no access to r5's readings, is the check. The writer did
  not perform that reading and will not.

## 5. The inventory search (QR-15)

**Search 1, for sourcing vocabulary.**

- Patterns:
  - "gravitational source", "source term";
  - "sources? (curvature|gravity|geometry)", "sourcing (gravity|curvature)", "as a source", "jacobson
    sourcing";
  - "in virtue of", "grounds? (the|its) (metric|curvature)";
  - "gravitat(es|ing)", "integration constant", "null flux", "feeds? back".
- Command: `git grep -n -i -E` at `c3b5f37a` over `papers/GR.md` and `papers/SM.md`.
- **Hits:** GR:340, 352, 358, 384, 400, 430, 448, 528, 530, 532, 569, 573, 577 and 581. Every hit is
  already a row, or lies within one (GR:430 in C-GR428; GR:448 in C-GR444). SM gave no hit.

**Search 2, broader.**

- GR.md patterns: "gravitationally active", "gravitat", "field equation", "einstein equation", "into
  curvature".
- SM.md patterns: "gravitat", "field equation", "einstein equation", "source".
- Hits outside the inventory, with the reason for each decision:

| Hit | Decision | Reason |
|---|---|---|
| GR:6, :886, :1002 | excluded | metadata or reference list |
| GR:26, :549, :703, :705 | excluded | introduction, summary or conclusion restatements of §7 and §6. These are propagation surfaces, not derivation sites. A status disagreement seen there is recorded as a finding, not as a row |
| GR:316, :318, :364 | excluded | the entropy formula, the GW250114 area test, the Maldacena comparison: no gravitational source term |
| GR:350 | excluded | laboratory superpositions: the H-GRAV completions, outside QB5(a) |
| GR:412, :460, :526 | excluded | observational and falsifiability paragraphs |
| GR:416 | excluded | the lead-in sentence to the Corollary, whose statement C-GR418 is a row |
| GR:458 | **added**, C-GR458 | it identifies the uniform and structured components of the boundary entropy; needed for the same-quantity table |
| GR:468 | **added**, C-GR468 | §7.3 Step 1; it defines the entropy displacement from which `ρ_E` derives |
| GR:591, :597, :685 | excluded | the theorem's falsifiability, black-hole horizons under partition-relativity, other entropic programmes |
| GR:655 | excluded | §8.5's dependency list restating §6. Its clause is excluded (§2.2) |
| GR:859, :861, :863 | excluded | Appendix A.7, the Page curve |
| SM:120 | **added**, G-SM120 | "Einstein's equations as self-consistency": Jacobson's inputs on the graph. It bears on Q5 |
| SM:14, :48, :56, :90, :132 | excluded | the abstract and assumption paragraphs; no gravitational source term |
| SM:174, :176, :186, :196 | excluded | dimension selection (d = 3). SM:186's "gravitational deficit with no source" concerns the d-filter, not the boundary law |
| SM:785, :811, :839, :1174, :1308, :1472 | excluded | gauge-sector, empirical-status and table text |
| SM:1664, :1695, :1721, :1757 | excluded | code archive and references |

**Other additions** under QR-15: C-GR418, E-GR571, G-GR701, G-GR693 and T-GR695.

**Group K** (QR-8): GR:340 split into s1–s4; GR:342; GR:346 s.1–s.3; Substratum.md:385, :387, :389, :391
and :393.

The book was not searched. The book mirrors are outside QB5(a)'s passages. X-14 governs any corpus-wide
negative statement at execution.

## 6. Decisions, updated from NOTES-QB5A-r1 §4

| # | Change |
|---|---|
| D-2 | Every carve is now an explicit predicate (QR-3). F4-law and F4-null remain carves and fail GRT-1 when no reason is stated. §8.5 (ii) states this, pending OQ-2 |
| D-4 | Δ1–Δ8 are fixed, and Δ9.k is enumerated and committed at Q-6a. "Δ8 is a writer addition. Its candidacy rests on F4's statement alone, and GRT decides it" |
| D-6 | The sorting is r5 §1.2 relativized by R-6, applied to every carve (pending OQ-3). The mirror consequence is stated in §8.5 (v) |
| D-8 | Replaced. All main-table variants are synchronic. F4-dia is a separate formalization, reported beside F5 and sorted at Stage 3 |
| D-9 | Replaced: "A status word attaches to what it modifies. The external examples fix the test" |
| D-10 | Conflict is kept. Aggregation is now complete, with As among the commitment values |
| D-11 | Replaced. Role T is any term of the field equation, on either side. IC takes precedence. NS and Conflict-R are added. Roles are per route for every row |
| D-12 | Extended. The §8.4 headline over branch × route × W0 row; no coordinate selection |
| D-19 (new) | The second reader (X-18) also classifies the W0 rows at Q-8, so that W0 cells are double-read like corpus cells |
| D-20 (new) | Owner answers are applied as pending, with alternative texts in §15. An owner answer that keeps to the alternative text is checked as a single edit; anything wider gets a full review (r2:1132–1133) |

The other decisions of NOTES-QB5A-r1 §4 stand.

## 7. Commands run

All were read-only, apart from writing the three new files.

- In the worktree:
  - `git fetch` of the branch (read-only; the worktree head was already at `660152911`);
  - `git log --oneline -3`;
  - `ls` and `wc -l` on `qb5a/`;
  - `cmp` of the committed r1 files against the writer's copies.
- `gh api repos/amaybaum/incompleteness/issues/comments/6872277416`: read only.
- `git grep -n -i -E` at `c3b5f37a` over `papers/GR.md` and `papers/SM.md`, for the two searches of §5.
- `git show c3b5f37a:papers/{GR,SM,Substratum}.md`, piped to `sed`, `awk` and `cut`, to display the
  openings of lines.
- `grep -n` on r2, for line anchors, and for the barred path strings (no hits).

No computation on OI rules was run. No check script, tool or build was run.

## 8. Off-`main` references (§A.42 item 8)

The references of NOTES-QB5A-r1 §6 carry over. The following are added.

| Reference | Claim it is attached to | Class |
|---|---|---|
| `qb5a/G3-QB5A-PREREG-r1.md` at `2e18a2df` (branch) | the base of r2 | support off `main`; lands with #1275 |
| `qb5a/REVIEW-QB5A-PREREG-r1.md` at `66015291` (branch) | QR-1 to QR-26, their replacement texts, and the recommended OQ answers | support off `main`; lands with #1275 |
| #873 c.6872277416 | the owner guidance (I-SYM; RC-W; X-5) | provenance on record; quoted with author and time |
