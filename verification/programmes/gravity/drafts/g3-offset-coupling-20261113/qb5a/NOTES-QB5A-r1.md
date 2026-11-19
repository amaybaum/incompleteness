# NOTES-QB5A-r1: working log for the G3 QB5(a) preregistration, revision 1

## 1. Pins and commit state

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`. At reading time
  `origin/main` in the read-only worktree resolved to the same commit.
- **Branch.** `research/g3-offset-873-20261113`, read from a read-only worktree at head
  `8d661a649` ("unit 2(b) r5, outcome (C) (WIP)").
- **Commit state, as observed when this file was written.**
  - Neither file is committed.
  - The writer does not commit, push or post.
  - The worktree was not modified.
- **Intended landing directory:** `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/`,
  beside r5. The coordinator decides.

## 2. Authority and owner guidance

**Authorization.** #873 comment 6872004336 (`amaybaum`, 2026-11-14). The QB5, QB6 and QB7 lines are
quoted in the preregistration header.

- QB5(a) authorizes the audit, paper-only.
- QB6 requires the rule to be frozen and independently reviewed before analysis.
- QB7(a) bars adopting running-vacuum sourcing as a premise.
- QB7(b) leaves the gravitating counterpart open for this investigation.

**Owner guidance.** Relayed by the coordinating session during drafting, attributed to `amaybaum`,
2026-11-14:

> "The decision rule must apply equally to the corpus's own metric-dependent source terms and the
> disputed vacuum-offset coupling, without selecting F4 or F5 to obtain a preferred result."

The coordinator's instruction attached to it asked for two things:

- the same per-term classification and the same F4 and F5 tests applied to the witness's vacuum-offset
  term, stated as a fixed invariant with a checkpoint;
- the guard against fitting kept, with a countercontrol that would catch a rule tuned to the witness.

**Record status.** This writer has seen the guidance only as a session message. No #873 comment carrying
it is known here. Under §A.42 item 7, a record that relies on an owner decision quotes it with author and
time from its record. The preregistration therefore cites it as relayed, and asks OQ-6.

**How it is built in.**

| Element | Where |
|---|---|
| Invariant I-SYM: same attributes, same predicates, no rule clause names a row | PREREG §1.3 |
| The corpus's offset coupling as rows T-GR352 and T-GR577 (Group V) | PREREG §4.2 |
| The witness rows W0-Z0, W0-ZI and W0-ZII, classified by the same tests | PREREG §4.4, node Q-8 |
| Checkpoint for I-SYM | X-5 |
| I-BLIND kept: fixed candidate space, reason-based carves, inertness of Cx rows, stage order | PREREG §1.3, X-6, X-7 |
| Countercontrol RC-W: relabelling, inertness sweep, decoy carve, decoy selector | PREREG §10.4 |

**Reconciling symmetry with blindness.** The brief asked for blindness: the witness plays no role in the
decision. The guidance asks for symmetry: the witness gets the same tests. Both hold under one
construction.

- The witness rows are classified exactly as corpus rows.
- Their stated status is read by the same test, and for a constructed row it is Cx.
- The rejecting predicates fire only on corpus commitments (D, D|cond or Rq), so a Cx row cannot move a
  Stage-2 verdict.
- This inertness follows from the uniform predicate and is tested by RC-W W-b; it is not a special
  exemption.
- The witness enters only at Stage 3, where its attributes decide which side of each admissible
  formalization it falls on.

## 3. Sources read

**Branch drafts, at `8d661a649`:**

- `G3-UNIT2B-BG-r5.md`, in full: §0, §1 (rule, K1–K5, R-1 to R-7), §2.4, §3, §4.3, §5, §6 (F4-1 to F4-8,
  F5, B-nodes), §7, §8, §9, §11, §12.
- `CONFIRM-BG-r4.md`, in full, and `CONFIRM-BG-r3.md`, in full.
- `NOTES-BG-r5.md` in full; `NOTES-BG-r3.md` §3 (the widened corpus search patterns and hits).
- `G3-UNIT2A-r3.md`: lines 1–90 (header and verdict), 190–300 (N1–N5, the three orders, Reading G,
  B_G), 300–345 (the witness's objects, conventions and law), 476–490 (controls C1–C4), 532–552 (the
  gap), 684–702 and 740–750.
- `G3-UNIT1-r5.md`: lines 156–160, 196–206 (𝒞_div), 220–226 (`Z`), 500–508 (§8.3 caveats), 594–608
  (the Jacobson route) and 668–673.

**Corpus, at `c3b5f37a`.** Read only to locate passages and line ranges, and to take the definitions the
audit needs. No passage was evaluated against F4 or F5. Only the opening characters of most lines were
displayed.

- `papers/GR.md`: the heading map; lines 12, 40, 162, 340–358, 370–412, 414–460, 462–532, 567–581, 633,
  691–697. GR:400 was read in full, to split Reading 1 from Reading 2. GR:12 was searched for the
  occurrences of "G3".
- `papers/SM.md`: lines 136–166 and the headings near them.
- `papers/Main.md` (:26, :44, :48, :54, :690), `papers/Substratum.md` (:385, :387, :389, :393) and
  `papers/Structure.md` (:136): read to confirm the identity of the premise-base lines r5 cites. They
  are not in the inventory.

`book/` was not read. The book mirrors are outside QB5(a)'s scope, which names `papers/` passages. X-14
covers any corpus-wide negative statement at execution.

## 4. Decisions made

| # | Decision | Reason |
|---|---|---|
| D-1 | Two stages. Stage 2 gives verdicts on formalizations; Stage 3 maps them to B_G. Stage 2 is committed before Stage 3 is written. | QB5(a) asks about F4 on the corpus's own commitments; B_G's outcome is a consequence. The order is checkable from the history (X-7). |
| D-2 | Every carve and scope is a predicate on attribute values. F4-law ≡ F4[Δ3] and F4-null ≡ F4[Δ4] are tested by GRT like every carve. | I-SYM; one test for every restriction of F4. QB5(a) lists scope as a question, not a given. |
| D-3 | GRT-1 to GRT-5 operationalize r5's K3 reading (NOTES-BG-r5 §3; CONFIRM-BG-r4 DF-4). | It makes "no grounded carve-out" decidable. |
| D-4 | Candidates Δ1–Δ9 are fixed now. Δ8 (M-pure) is added from F4's own exemption of the Einstein tensor. Δ9 is closed by the inventory. | Fixed candidate space (I-BLIND). Δ8 is implied by F4's statement and r5 F4-1. It is listed before any row is classified, without a claim about whether it passes. |
| D-5 | Both universal negatives (R's and (A)'s) are made relative to the frozen inventory and the candidate list, symmetrically. | CONFIRM-BG-r4 DF-2: the rule had made (B) depend on an open universal negative. Relativizing only one side would tilt the rule. OQ-2. |
| D-6 | Carve variants whose class contains the witness's quantity are counted as CoC-content at Stage 3. | Required once carves are chosen without reference to the witness. It extends r5 R-6 (F4-null). Its consequence for (A)'s reachability is stated as a property of the rule. OQ-3. |
| D-7 | A separate "F4 restricted to non-metric-defined terms" formalization is not added. That restriction is the carve Δ5, assessed by GRT. | No new formalization outside r5's family plus QB5(a)'s scopes. Δ5 covers it through the uniform carve machinery. |
| D-8 | The diachronic reading (F4-3) is an attribute (A2t), not a separate variant. | It changes whether the cycle closes for a row, which is a per-row fact. |
| D-9 | Status is read for the source role only. Status of the value, form, dependence or magnitude goes to A3v. | r5 and CONFIRM-BG-r3 CF-6: GR:374's "requires" concerns dependence, not sourcing. The test is stated generally, with external examples, and no inventory row is pre-classified. |
| D-10 | Conflicting statuses on one quantity give Conflict, which makes the cell undetermined. | Neither the strongest nor the weakest statement is chosen. A conflict is a finding, and resolving it either way would be a choice. |
| D-11 | Role T dominates a consequence statement (A1q). Consequence-ness is tested as carve Δ2. | This avoids settling a disputed role by definition. |
| D-12 | Every derived cell is computed per §8.3 branch (β0, β1), and every Stage-3 result per route (𝒞_div, Jacobson). | §8.3 is a posit (U1r5:504–505); the boundary law's form is excluded as a premise. |
| D-13 | Passages found later never enter the decisive table without an amendment; they get sensitivity lines. | The brief's rule. Applying it uniformly, before and after rendering, removes a channel for fitting. |
| D-14 | Inventory additions beyond QB5(a)'s list: Group V (owner guidance); Group Q (rows for Q3–Q6); Group C (context rows, including GR:482 from r5's K3 list and AW-entropic). | Each is listed with its reason. OQ-4. |
| D-15 | F3 is carried as rejected (r5 §3.3) and not re-audited. | Outside QB5(a). |
| D-16 | r5's §2.4 reading column and node verdicts are excluded as grounds for cells (X-13). | They are prior classifications of the same passages; using them would anchor the audit. |
| D-17 | The rule-level controls are constructed toys with external physics examples: a non-minimal scalar's curvature-coupling stress, the `f(R)` effective stress, Komar mass, dust, a bare Λ. | The brief requires constructed or external examples, not the inventory. |
| D-18 | The Stage-3 table in §8.3 is a reading aid; items 1–5 govern. | This avoids two governing texts. |

**A limit of the design.** The rule was written by a writer who has read r5's per-passage readings. The
preregistration states no cell for any inventory row (X-15). The rule's dependence on that knowledge is
open to the independent review QB6 requires; the review is the check, not this note.

## 5. Commands run

All were read-only, apart from creating this directory and writing and editing the two files.

- In the worktree:
  - `git log -1 --oneline`; `git log --oneline -8`; `git cat-file -t c3b5f37a`;
  - `git diff --stat c3b5f37a 8d661a64 -- papers/` (empty);
  - `git diff --stat c3b5f37a origin/main -- papers/…` (empty);
  - `git status --short` (clean).
- `git show c3b5f37a:papers/{GR,SM,Main,Substratum,Structure}.md`, piped to `sed`, `awk`, `grep` and `cut`
  to display line ranges and headings.
- `sed`, `grep` and `cat` on the branch drafts.
- A short Python string replacement on the preregistration file only. It made the toy-table corrections
  and computed nothing on OI rules.
- `grep` of both files for the barred path strings: no hits.

No computation on OI rules was run. No tool, check script or build was run.

## 6. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Class |
|---|---|---|
| `G3-UNIT2B-BG-r5.md` at `8d661a649` (branch) | the definitions of F4, F4-null, F4-c, F5, K1–K5, Lemma U, N3′, the set-level and diachronic readings, and the excluded list | support off `main`; lands with #1275 |
| `CONFIRM-BG-r3.md` at `651849ab`, `CONFIRM-BG-r4.md` at `905b68cc` (branch) | the soundness of F4-7; the K3 reading; DF-2's symmetry point | support off `main`; lands with #1275 |
| `G3-UNIT2A-r3.md`, `G3-UNIT1-r5.md` (branch) | the definitions of ⊳_G, N1–N5, Reading G, the witness, `Z`, 𝒞_div and the Jacobson route | support off `main`; lands with #1275 |
| `NOTES-BG-r5.md` §3 (branch) | the reading of K3 used by GRT | support off `main`; lands with #1275 |
| #873 comment 6872004336 | the authorization quotations | provenance; quoted with author and date |
| The owner guidance of 2026-11-14 (session message) | I-SYM and RC-W | provenance only until recorded on #873 (OQ-6) |
