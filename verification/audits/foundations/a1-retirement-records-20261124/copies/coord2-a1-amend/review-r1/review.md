# Independent review, round 1: A1 plan-amendment proposal (ESC-1 to ESC-4, the dependency on P, P1–P5 and P8)

Reviewer: an independent non-author reviewer session, 2026-11-24. This is a paper-only review. Nothing was written
in the repository. There was no commit, push, GitHub write, CI run, dispatch, trial or merge. GitHub was read only by
REST GET (rulesets, PR #1477, main, compare, and the comment c.7093128173). The S1 code was run only on a copy made
outside the worktree, with `-B -I`. The worktree `coord2-impl-wt` was left clean (`git status` showed 0 entries).

## Verdict: REJECT (revise and resubmit)

The core of the ESC analysis holds and is well evidenced:

- ESC-1 option (b1) lints clean.
- The rebuilds in ESC-4 are byte-exact.
- The §32 append is append-only, and both pin parsers agree on it.
- No scientific value, edit, ledger entry or fingerprint changes.

Two findings block the proposal. Each one is a stated claim that the evidence or the tool design contradicts, and
each has a small fix. Neither requires the ESC options to be redone.

## Blocking findings

### B1. §32.10 item 1 (proposed PREREG text) and §6 claim more than the evidence shows about item 7's failing lines

**The claim.** §32.10 says: "Item 7 as frozen fails at a T1′-style `X` (seven W1 lines carry the bijection's property
count)." §6 and O-1 repeat it.

**What holds.** Three of the four W1 rules (six lines) do refer to the bijection's properties. One line is not
established.

**The line in question.** `papers/SM.md:1394` reads: "they hold for every bijection satisfying the six structural
properties".

- Rule W1-a's reason states that it counts the six properties "as SM defines them". `papers/SM.md` at T1′ and at H
  contains no such definition. Its only "six structural" occurrence is line 1394 itself (grep for `\bsix\b` and
  "structural propert" in SM.md).
- In the papers' own vocabulary, the structural conditions of an OI-class substratum are A1–A6:
  - `papers/Substratum.md:205` at H: "The structural assumptions A1–A6 exclude …"
  - `papers/Structure.md:646` at H: "OI-class substrata (satisfying A1-A6)"
- SM.md:1394 refers to "the equivalence class [(S, φ)]/G_sub". That is the same object as Structure's Proposition 9.5.

So SM.md:1394 may be a count of the posits that includes A1, which is exactly what item 7 exists to catch.

**Rule broken.** Code Review Rules, "Claim/evidence boundary": a changed status claim is stronger than its evidence.
The owner's 2026-11-24 guidance adds that item 7 may not be restated before it is understood.

**Smallest fix.** In §32.10, §6 and O-1:

- State only the measured fact: 7 lines match "six structural", and 0 match "Fourteen" or "sixth of".
- Classify the lines as in Q6 below, with SM.md:1394's referent marked as an open scientific question.
- Withdraw recommendation O-1(a) until that is adjudicated.

### B2. §32.7 and §4.3 step 7: a side-change class written after `F` contradicts v6.0c, and one frozen at `F` is impossible as written

**The claim.** The proposal says the plan-directory paths on `M` are classified "by a side-change class record written
after `F` for that purpose, as the tool's reconciliation rule allows for side changes on `M`" (§32.7). §4.3 says
"as design sec. 13.3 allows".

**What v6.0c says.**

- Sec. 6.3, "Frozen configuration": "A record added after `F` is admissible only under sec. 13.3's reconciliation
  rule".
- Sec. 13.3, first bullet: "A record written after `F` is allowed only for side changes on `M` that the freeze could
  not foresee."
- Arrangement A foresees the plan-PR merge in §32.7 itself. A post-F class for it is therefore not admissible under
  v6.0c as written.

**The alternative is also blocked.** Sec. 13.1 requires a class to pin every path it covers to its blob. The only
exemption is the class record itself, whose blob the configuration pins. A class frozen at `F` that covers the plan
directory would have to pin `retirement-config.json` and `PREREG.md`. Both of them pin, directly or through the
configuration, the class record. That is a hash cycle, so the class cannot be written.

**Consequence.** Under v6.0c as written, neither A nor C (both put the plan directory on `M` before `L`) can classify
the plan directory at `M` without a design change.

**Smallest fix.**

- Correct the "as 13.3 allows" statement.
- Add an owner and tool-design question O-9. One cycle-free form would be a side-change class that admits "every path
  under the plan's record directory whose blob at `M` equals its blob at `F`". `F` is an explicit run input, so the
  tool can check this from git objects without pinning.
- Make A conditional on that design change.

## Per-question results

### Q1. ESC-1 (v2 at H)

**Re-run** (`lint_v2.py`, output `lint_v2.out`). This ran S1 `rules.lint_rule`, with profiles from the proposed
configuration (every `pattern_sha256` asserted) and sentences from git objects.

| Lint run | Problems |
|---|---|
| v1 with `recorded_at` set to T1′ | 0 |
| v1 with `recorded_at` set to H | 0 |
| v1 with `recorded_at` set to main | 0 |
| the proposed v2 file as written | 0 |

Per fingerprint (S = sentence reproduced, C = context reproduced):

- All 11 reproduce sentence and context at T1′.
- At H and at main, 9 reproduce both.
- W1-d's two fingerprints (`ch19-open-problems.md`, `FULL.md`) reproduce the sentence only (S, no C). W1-d has
  `context_required: false` and no allowance.

D1 self-pass at H, using H's own neighbours, is `pass` for all 11 fingerprints, W1-d included. V1–V3 are confirmed.

**The v1→v2 diff.** It matches `diffs/ESC1-…diff` byte for byte. Only these change: `status`, `supersedes`,
`recorded_at` (at the top level and in all 6 rules) and the top-level `author`. S1 `file_widening(v1, v2)` returns
`[]`. `file_widening(None, v1)` returns 6 items (V4 confirmed).

**"Not a widening": correct under v6.0c sec. 6.3's enumerated list.**

- The list covers files, literals, context and negative literals, the fingerprint set, `max_instances`,
  `context_required`, a new rule without `supersedes`, and allowances. `recorded_at` is not on it.
- Moving `recorded_at` from T1′ to H only narrows `rule-stale`'s exemption. Proper ancestors of H are a subset of
  proper ancestors of T1′, so more trees are evaluated, not fewer.

**W1-d: Q10 disposition versus the writer.** Each is right relative to its own premise, and the question stays open.

- The disposition's "widening review that W1-d's context change requires" (DISPOSITION.md, option (b)) presupposes
  re-fingerprinting W1-d at the new commit. That is option b3. Under b3 the context hashes change, which is "any
  change to the fingerprint set" and therefore widening.
- The writer's b1 changes no value, so it is not widening.
- Under b1, though, W1-d's `context_sha256` values describe T1′'s neighbours, which are X's post-retirement neighbours.
  They do not describe the neighbours at the record's own `recorded_at` (H).
- Whether that passes the lint depends on how sec. 6.3 reads: "Each fingerprint must be reproduced by a sentence of
  its named file at `recorded_at`."
  - Sec. 6.2 step 3 treats the context as part of the fingerprint ("the fingerprinted location … whether or not the
    rule sets `context_required`").
  - Step 4 compares the context only "when required".
  - S1 compares it only when required (`rules.py:123`).
- For W1-d the context value is never read for a decision: it is not required and carries no allowance. b1 and b3
  therefore give identical outcomes at `X`.
- O-4 is correctly framed. It should be settled by explicit text in the adopted design.

**Additional open point, N2.** It is not settled whether the predecessor v1 must itself pass the fingerprint lint at
its own `recorded_at` (T1′). Sec. 6.3 requires a predecessor that "does [not] itself pass this lint". S1's
`predecessor_problems` runs only the review-chain lint and never `lint_rule`. If the final design reads "this lint" as
including the fingerprint lint, b1 does not remove T1′ from what a run reads. Fold this into O-4.

### Q2. ESC-2 and ESC-3

**"No record change; the gap closes once F (and P) are reachable from main": correct.**

- I verified that `edits_check.py` at P is blob `1153e039…`, sha256 `2856e58c…`, unchanged into F by construction.
- Repo-scope's lists equal `HISTORICAL_PREFIX` (lines 786–787), `HISTORICAL_FILE` (788), `ACTIVE_IN_RECORDS` (856)
  and the generated-artifact rule (862).
- The ESC-2 and ESC-3 support is the checker content. F's reachability brings it onto `main` together with its commit
  identity.

**Consistency with Q10 ("do not land P merely to satisfy citations").** Landing the plan through its own pull request
is the retirement's own course. The plan's record directory lands in `C` regardless (V7: the candidate's record
directory equals the plan's). The tool's acceptance verdict depends on `F`'s identity: admission reads the pin table
and the configuration at `F`, and the execution note records `preserve_check --plan F`. Under §A.42 item 8 that is
support, not citation, and copying files cannot replace reachability.

That distinguishes it from landing P (or T1′) for a citation's sake. It is consistent provided the owner's merge
decision for #1477 records this rationale.

**Nit N8.** "Checked by its reviewer at `F`" is circular, because the review records are part of `F`. Say "against
blob sha256 `2856e58c…` (P's `edits_check.py`, carried unchanged into `F`)".

### Q3. ESC-4 byte identity

**Re-run** (`rebuild_all.py`, output `rebuild_all.out`). This was an independent implementation: splices applied in
reverse, with overlap, `old_sha256` and `new_sha256` asserted. It covered all 44 ledgered files.

| File | Rebuild from H plus P's ledger equals T1′ blob |
|---|---|
| `papers/GR.md` | `c4a320e2…` |
| `papers/SM.md` | `c358068f…` |
| `book/ch09-universality.md` | `289d1710…` |
| `book/ch19-open-problems.md` | `f2c14959…` |
| `book/The-Incompleteness-of-Observation-FULL.md` | `c9313316…` |

- `appendix-b-derivations.md`: H equals T1′ (`f91b596d…`).
- GR.md line 58 of the rebuild has sha256 `3a7c1098…`, which equals the gr58 record's `line_sha256`. The only splices
  touching H's line 58 are D040 and D041.
- Of the 44 files, 43 rebuild exactly. The exception is `verification/coverage/LEDGER.json`, regenerated by the trial
  for item 4. It is outside the claim, and the proposal claims only the five files.

**"Deferring is invalid": correct.** v6.0c sec. 6.3 says a record added after `F` is "never for a decision on `X`".
Sec. 13.3 and control O8 say the same. GR.md:58 would then be `final-unclassified`, failing items 1 and 7 (sec. 11).

### Q4. Arrangement A

**Consistent with v6.0c execution identity and with §A.42, except for B2.**

- `T` must be on `main` (TR29).
- `F` must be reachable before `L`, because the execution note in `C` depends on `F` (§A.42 items 2, 3 and 8).
- `L` must have exactly the parents `M` and `C`, so `F` cannot arrive through `L`.

I verified the ruleset `guardrail` by REST: `strict_required_status_checks_policy: true`. #1477's head must therefore
contain `main`, as the proposal says. #1477 is open, a draft, and its head is P.

**"Merging the plan after L is invalid": correct.** The execution note in `C` would land relying on an unreachable
`F`, and the Q10 conditions bar the §A.42 item 8 exception.

**Points the proposal should address.**

- **N7, the frozen §25.2 "Landing" row.** It reads: "after merge the landing diff against its first parent is exactly
  the execution's own diff". v6.0c sec. 13.1 has the same rule ("The diff from M to L must equal the diff from H to
  C, path by path"). With the plan directory already on `M`, `L−M` omits paths that `H→C` contains. S1 accepts these
  paths (`execution.py:393-396`, `c == m`), but the frozen text and the design text do not say so. §32.7 should state
  how §25.2's equality is read for paths that `M` and `C` change to identical bytes.
- **The `preserve_check --base` route is refused at current main.** I verified that `AGENTS.md` is a ledgered file
  and changed between H and main. The frozen `--base <current main>` route (§11 item 14, §25.2) is therefore refused,
  so item 14 depends on the tool route plus a reconciliation record. The proposal notes the drift in §6. It should say
  that this makes the tool route necessary for item 14.

**A simpler variant, C′ (optional).** Complete the gate and the review at the candidate head, merge #1477 at that
head, then designate `F` as that head, now reachable through the merge's second parent. This removes A's update merge
on the plan branch after `F`. It shares B2, and it puts an undesignated plan on `main` if designation is refused. It
is not required.

### Q5. P1–P5, P8: the exact diffs

**Diffs reproduced.**

- `diff -u` of P's PREREG (git object `6931e3be…`, sha256 `bc05340f…`) against `PREREG-proposed.md` equals
  `diffs/PREREG-append-s32.diff`.
- P's PREREG is a byte prefix of the proposed one: pure append, no `-` lines.
- The staged configuration against `retirement-config.json.proposed` equals the configuration diff.
- v1 against v2 equals the ESC-1 diff.

**§32.9 is the last Record-pins subsection** (`pins_check.py`, output `pins_check.out`).

- P's last heading is `### 31.31 Record pins`, of 12 such headings. The proposed PREREG's last is
  `### 32.9 Record pins`, of 13.
- Both parsers, P's `preserve_check.read_pins` and S1's `authority.read_pin_table`, return the same 6 rows.
- The six `PINNED` digests are unchanged against §31.31.
- With the placeholders filled with dummy hex values:
  - The tool reads 10 rows, including `retirement-config.json` and the review files (its pattern allows `-`).
  - `preserve_check` still reads the 6 `PINNED` rows, which is all it checks.
- The headings §32.x collide with no heading of P. `duplicate_check.py` from `main` reports OK on P, on the proposed
  PREREG and on §32 alone.

**P1 and P5.** §32 names no authority record, plan id, round id or form comment. "freeze-ledger" appears only in
P5's required negation.

**Owner quote.** The quoted passages of c.7093128173 match the live body (REST GET; `amaybaum`,
2026-11-23T06:13:50Z, never edited).

**No recorded scientific value, edit, ledger entry or fingerprint changes.** I confirmed this from the three diffs.

**Nits.**

- **N4.** `checks.item7`, unchanged, already encodes design note 1's restated item 7: profiles `ptr`, `count-grep`,
  `resid` and `DR-1/3/4/5`, with `final_profiles`. This conflicts with "item 7 open". The `dr-deny-v1` and `resid-v1`
  reviews in the inventory are needed for item 7 only on that route. Mark them as dependent on O-1.
- **N5.** The configuration's `author` stays `implementation-writer-20261123`, although its content now has
  amendment-writer changes. v2 changes its author; the configuration should do the same.

### Q6. Consequences, and item 7 (with the owner's guidance of 2026-11-24)

**Item 7, frozen wording.** `verification/audits/foundations/a1exit-deletion-20261121/PREREG.md` at P (4c79be64),
lines 4631–4632:

> 7. Corpus grep for `\bA1\b`, "total-finiteness", "posit (ii)", "item (ii)", "finiteness posit": only the
> ledger's false positives remain; grep of posit counts ("Fourteen", "six structural", "sixth of"): zero.

**Demonstrated failure.** I ran `git grep -P` over `papers/*.md` and `book/*.md`.

| Pattern | T1′ | H |
|---|---|---|
| `\bA1\b` | 4 | 179 |
| total-finiteness | 0 | 8 |
| posit (ii) | 0 | 1 |
| item (ii) | 0 | 11 |
| finiteness posit | 0 | 13 |
| Fourteen | 0 | 1 |
| six structural | **7** | 11 |
| sixth of | 0 | 2 |

The counts equal RT-I7. The count clause requires "six structural" to be 0, so item 7 as frozen fails at a
T1′-style `X`. I verified this.

The `\bA1\b` clause, however, passes as frozen. Its 4 lines are the anomaly labels "(A1)" (W2) at appB:235 and :246
and their FULL mirrors. `LEDGER.md:304` at H states: 'The anomaly conditions "(A1)" at appB:235 and :246 are false
positives'. The ledger's rows cover "FULL mirrors" throughout. Listing those 4 lines among item 7's failures, as the
design's sec. 11 row 7 and the proposal do, reflects the tool's `item7-literal` profile, which does not implement the
"ledger's false positives" clause. It does not reflect the criterion.

**Classification against the owner's three possibilities** (this reviewer's own):

| Lines | Evidence | Classification |
|---|---|---|
| `\bA1\b`, 4 lines (W2) | The ledger names them false positives; the line content is an anomaly-cancellation condition | Not a failure of the criterion. Only the tool's literal countercontrol fails them. If the tool is to carry item 7, its implementation should honour the clause (possibility 2, applied to the check's implementation) |
| W1-b: ch09:137, FULL:2554 | Enumerates the six as "isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count". No finiteness | Possibility 1: the literal "six structural" is over-inclusive relative to its purpose (counts of the posits) |
| W1-c: ch19:198, FULL:5270 | Names statistical isotropy "one of the framework's six structural properties of the bijection" | Possibility 1 |
| W1-d: ch19:212, FULL:5284 | At H the sentence before lists "the open hypothesis A1 of finiteness" separately from "the six structural properties of the bijection", so the six exclude A1 | Possibility 1 |
| W1-a: SM.md:1394 | No definition in SM. The papers use A1–A6 for the class conditions (B1) | Unresolved. If it counts A1–A6, possibility 2: the ledger misses a site. A fix would change the 399 splices, which c.7093128173 does not authorize, so it needs an owner decision. If it counts the bijection's properties, possibility 1 |

Possibility 3 has no support. A count clause guards the recorded failure mode "a removed claim can hide in a count"
(§A.30; lessons register).

The phrase is also genuinely ambiguous in the corpus. At H, ch09:104 and FULL:2519, "six structural properties of the
substratum", did count finiteness, and the retirement edited them to "five". So any correction must classify line by
line, not exempt a phrase.

**Is O-1(a) necessary? No; a narrower fix exists.** Design note 1 replaces the grep with a broader check: the deny set
DR-1/3/4/5, `resid`, `ptr` and `count-grep`. That adds stricter machinery, but it is not needed to correct the defect
found. The narrowest correction keeps the frozen grep. It extends the "only the ledger's false positives remain"
form, which already governs the first clause, to the count clause: "zero, except lines a reviewed record classifies as
not counting the posits". The W1 records then serve as those classifications, and SM.md:1394 is adjudicated first.
Whether to adopt the broader check as well is a separate owner choice. O-1 should present both options, with this
classification.

**Trial rebuild requirements.** These are correct as stated.

- New plan-directory files enter the predicted tree (V7; I confirmed the record-directory equality rule in
  `preserve_check`).
- T0″ and T1″ must be rebuilt.
- The PREREG and the configuration change nothing that `preserve_check` or `guards_check` pin, beyond the directory
  contents.

**Existing T0′ and T1′ evidence.** It is valid evidence of what it tested and is not acceptance evidence, per
c.7093128173.

### Q7. Change inventory

Complete and exact for what it covers. The diffs, field tables and unchanged lists match the files.

**Missing or understated.**

- The side-change class and reconciliation records for the H..main drift already known: `AGENTS.md` (ledgered,
  `base-drift`), `.claude/settings.json` and the trial workflow. These are foreseeable, so they must be frozen with
  `F` (sec. 13.3), and table B should list them. §6 mentions them only in prose.
- The plan-directory side-change class under B2.
- The records item 2 and item 11 need (sec. 8.2). These are named only in §32.8.
- The §25.2 landing-diff reading (N7).

**Possible scope creep, conditional.** The `dr-deny-v1` and `resid-v1` reviews and `checks.item7` are needed only on
O-1(a)'s route (N4).

**N6, an incomplete §A.42 item 8 trace.** §4.1 says T1′ is reached only through w1-w2 v1 and gr58. In fact:

- `controls.json`, which the configuration pins, carries `control_inputs[1]` `agents-md-at-T1p` (commit T1′). No A1
  operation reads it: DR-3's countercontrol uses only `agents-md-at-H`, I verified. It is read only by
  `adapters/a1_controls.py`, whose real-tree controls (RT-DR3W, RT-I7, item11-T1p, `T = 14ac71b4…` at line 42) are
  tool-validation CI.
- `dr-deny-v1`, `resid-v1` and the README also cite T1′ (ESC-5, provenance).

§32.5 should list these as provenance. §32.4's "the tool's countercontrols … preregistered control set, which the
configuration pins" should state that T1′-reading real-tree controls are not acceptance inputs. Otherwise T1′ becomes
support.

**N3.** V6's description of the ambiguity scan is inaccurate. S1 `config.py` scans the common path of the referenced
records' directories. With records in both the plan directory and the tool directory, that is
`verification/audits/foundations/`. It is harmless today: no other record supersedes v1.

### Q8. Open questions O-1 to O-8

- **O-1:** revise as in Q6. Give the three-way classification, a narrower option, and SM.md:1394 adjudication as a
  prerequisite. Withdraw the recommendation of (a).
- **O-2:** add C′ and the dependency on O-9 (B2).
- **O-3, O-5, O-6, O-7, O-8:** sound.
- **O-4:** sound. Extend it with N2 (whether the predecessor's fingerprint lint is required).
- **Add O-9 (B2):** a cycle-free class form for the plan directory on `M`.
- **Add O-10:** the configuration's `checks.item7` and the DR/resid reviews depend on O-1 (N4).

## Verified versus inferred

**Verified** by computation or REST:

- the manifest;
- every input hash;
- the three diffs, and that the change is append-only;
- the lint at T1′, H and main, and on v2;
- self-pass at H;
- the widening comparisons;
- all 44 rebuilds, GR:58 and D040/D041;
- both pin parsers, before and after filling the placeholders;
- duplicate_check;
- the item-7 grep counts and the frozen wording;
- LEDGER.md:304;
- the ruleset and the #1477 state;
- the reachability compares (P diverged at `1c7eedc4`, ahead 50; T1′ diverged; H behind main);
- AGENTS.md being both ledgered and drifted on main;
- the owner quotes;
- the references in controls.json, the dr-deny countercontrols and repo-scope's lists.

**Inferred** (from reading code or design text):

- the S1 landing `c == m` acceptance;
- that the S1 predecessor lint omits fingerprints;
- the v6.0c readings in B2, N2 and N7;
- the scientific readings of the W1 lines and of SM.md:1394. B1 shows that SM.md:1394 is unsupported, not that it is
  wrong.

## Files

All files are under `review-r1/`. `MANIFEST.sha256` covers each of them.

- `review.md`: this review.
- `lint_v2.py` and `lint_v2.out`: the lint.
- `rebuild_all.py` and `rebuild_all.out`: the rebuilds.
- `pins_check.py` and `pins_check.out`: the pin parsers.
- `widening.out`: the widening comparisons.
- `dup.out`: duplicate_check.
- `work/`: copies of the objects read, namely P's PREREG, `preserve_check` and `edits_check`; v1; the staged
  configuration; the §32 extract; the list of ledgered files; the H..main path list; and the comment JSON.
- `tcopy/`: a read-only copy of the S1 tool and its audit directory at `443e871f`.
