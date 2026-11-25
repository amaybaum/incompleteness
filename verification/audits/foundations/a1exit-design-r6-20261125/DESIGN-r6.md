# Ledger coverage tool: design r6 (consolidated, self-contained; final draft for owner adoption, not adopted)

## 0. Status, authority, scope and goal link

Requirement ids have the form `R6.<section code>.<n>`. Each requirement names the inventory items it
restates (Sources) and the controls of the expectation file that test it (Controls). Expected results
are stated only in the expectation file (sec. 16). Where a cited control's expectation row does not yet
list the requirement, the requirement index marks the citation, and the correspondence check of
sec. 16 requires the row to name the requirement before r6 is final. Labels in parentheses such as
(R1), (O2), (B-4), (D2) or (V5-D1) name the review finding or decision that introduced a rule; they are
not identifiers and name no control (R6.NOTE.13).

**R6.STAT.1** Status: draft, not adopted. r6 is the consolidated design of the ledger coverage tool
(`tools/ledger_coverage.py` and the package `tools/ledger_coverage/`). On its adoption by a recorded
owner decision it supersedes design v6.0e and the amendments r4 and r5, which then become historical
sources; their text, blobs and the commit at which v6.0e was implemented are kept as provenance in the
historical appendix. r6 adopts nothing before that decision, and changes no design, implementation,
control expectation or exception in force.
Sources: E-001, A-001, A-136, A-144, A-146, V1-002. Controls: none (status statement).

**R6.STAT.2** Self-containment. r6 is complete in itself. It incorporates no other document by
reference: every rule it relies on, including the anchor rules (sec. 4), the sentence splitter
(sec. 8) and the result schema (sec. 7), is stated in r6. No requirement of r6 is stated as
"unchanged" relative to another design, and a citation of an earlier design, review or record is
provenance, never a requirement.
Sources: E-007, A-001, A-136, A-144, A-146. Controls: none (form of the design; checked by the
correspondence check of sec. 16).

**R6.STAT.3** What the tool verifies. The tool verifies which exact plan was executed and what actually
ran. Every result identifies, and the run verifies against the git object store and the pins of the
configuration at `F`: the plan commit `F`; the pin table and configuration blobs; the tool commit `T`
with every tool file and the workflow; the repository and event of the producing CI run; and the
evaluated commits. The landing record that commits the result is the result commit (sec. 7, sec. 11).
The owner confirms, procedurally and outside the tool, that this was the approved plan. The tool makes
no claim about authorization (R6.PUR.11), and the output's class names carry the fixed technical
meaning of R6.OUT.21.
Sources: E-009. Controls: none (scope statement; tested through the requirements of sec. 7 and
sec. 11).

**R6.STAT.4** Owner authorization is procedural. The approvals AGENTS.md requires (sec. A.50: freezing
and designating the plan, dispatching its trials, executing it, merging into `main`; sec. A.45 rule 3
and sec. A.51 for work) are given by the owner and quoted with author and time in the record that
relies on them (AGENTS.md sec. A.42 item 7). The tool neither reads nor checks them. No check of this
design is waived by r6, and every later step keeps its own owner gate (sec. 19).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-012. Controls: none (procedural boundary).

**R6.STAT.5** Rules binding this design. The design and its control expectations follow requirements
that can be verified independently of the implementation. A difference between the implementation at
the tool commit and a requirement of r6 is a finding, classified as an owner decision or a
verification defect; it is never adopted into the design by default. No check is weakened to turn a
real-tree failure green, and no check is weakened retrospectively. No requirement is withdrawn
without a recorded trace of what verified it and where that property is verified afterwards; a retired
control keeps the disposition of the requirement it tested (sec. 33). The generality conditions of
sec. 24 to sec. 30 are mandatory within their scope.
Sources: E-018. Controls: none (design rule; enforced by review and by sec. 16).

**R6.STAT.6** Goal link (AGENTS.md sec. A.47): A1-EXIT (#1169), the exception-free verification route.
r6 decides how the tool verifies each mandatory check of the amended plan, which exact commits a run
checked, how the landing of the amended plan is decided (sec. 21) and how the records that the plan's
item 2 needs are read (sec. 22). It decides no scientific question, no row disposition, no record's
content and no owner approval.
Sources: E-020, V1-003, V2-002, A-003. Controls: none (planning link).

**R6.STAT.7** Accountable Issue: #1169, where the defects of the earlier tool are recorded.
Sources: V1-004. Controls: none (planning link).

**R6.STAT.8** Landing order. Owner decision #1169 comment 7093128173 (`amaybaum`,
2026-11-23T06:13:50Z) approved in principle that the tool lands first, that the plan's `PREREG.md` is
amended and re-frozen so that every mandatory check of its sec. 11 passes as written, and that the four
trees are distinguished (sec. 20). It superseded the execution-exception route of comment 7092885251.
The steps it held (implementation, push, pull request, merge and the plan edit) are each governed by
their own owner record; r6 releases none of them. Before adoption the decision is quoted in r6 in the
owner's own words, byte-exact from the comment if it holds them, or as the owner restates it (RE-26).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: RV-002. Controls: none (governance record).

**R6.STAT.9** Owner acceptance conditions. Each condition the owner set for the design is answered by
the r6 requirements and controls named below. The expected results of those controls are stated in
the expectation file.

| Condition | Answered by |
|---|---|
| 1. Distinct exit codes, including parser errors and `--help`, with a control | sec. 7 (R6.OUT.1 to R6.OUT.11); controls X1 to X11 |
| 2. A frozen, reviewed `delegation.json` with exact-head evidence; missing evidence is never PASS | sec. 13; RT-C expects REVIEW_REQUIRED `delegated-evidence-missing` without contract evidence |
| 3. Deny-pattern coverage; adversarial FAILs, each traced to a named rule or a FAIL condition of sec. 15 | sec. 10, 12 and 15 |
| 4. A preregistered s3-to-context mapping; the `T1'` cases resolved transparently | sec. 6 |
| 5. Every replacement-text and unclassified hit classified, with the review load stated | sec. 14 |
| 6. Deterministic HP regions; full merge ids; HP/RET overlap visible in both | sec. 5 |
| 7. Each mandatory check of the plan's sec. 11 mapped to an operation, flags, expected outcome and countercontrol | sec. 18 |
| 8. Review lint for rules, PIN_OK reasons, reconciliation records and other records; no authorization lint in the tool, owner approval procedural (R6.STAT.4) | sec. 10 and 11 |
| 9. Generality with strict scope limits | sec. 24 to 30 |
| 9.1. A core that does not depend on any retirement | sec. 24; controls Z9a to Z9h |
| 9.2. A frozen per-retirement configuration `oi-retirement-config/1`: schema, adapters, location, pinning and lint | sec. 25 and 26 |
| 9.3. A1 as the first configuration, with every A1-specific constant relocated and no check weakened | sec. 27 |
| 9.4. A structurally different synthetic configuration with positive and adversarial controls | sec. 28; controls Y1 to Y10 |
| 9.5. Fail-closed configuration validation, with exit codes and classes | sec. 29; controls Z1 to Z11 |
| 9.6. Reproducibility record | sec. 30 |

Sources: E-032. Controls: none (traceability table; each condition is tested by the controls of the
requirements it names).

**R6.STAT.10** Adoption and implementation certification (OC-2). r6's adoption and the certification of
an implementation are separate steps.
- Adoption is the owner's recorded decision on the specification. Its support is the r6 text (this
  document, the expectation file, the requirement index, the migration index and the list of
  paraphrased decisions) and its independent exact-head review, both on `main` no later than the
  adoption record lands (AGENTS.md sec. A.42 items 1, 2 and 8). Precondition: the documents and the
  review reach `main` by an ordinary merge that the owner approves (AGENTS.md sec. A.50 item 1); r6 does
  not authorize it.
- Adoption certifies no implementation. Each requirement and obligation of r6 holds or fails by its own
  controls on the tool revision. None uses the tool commit a37992449b452021001277c06c524a30c92dfb87, its
  conformance assessment or its CI runs as support; for the requirements and obligations these are
  provenance (AGENTS.md sec. A.42 item 8).
- Implementation certification is made against the tool revision after it lands on `main` (OBL-26), with
  evidence of kinds 2 and 3 (R6.EVID.7); the tool's landing decision rests on kind 1 (sec. 32).
- Every place where adoption, or an enduring claim stated in r6, still uses content that is not on
  `main` as support is listed in the adoption trace of sec. 32. Each is an open governance conflict,
  closed only by landing the content the claim needs or by narrowing the claim, never by an exception.
OPEN: off-main support of adoption.
Sources: OC-2. Controls: none (governance; verified by review and by the adoption trace of sec. 32).

***

## 1. Notation and symbols

**R6.NOTE.1** `E` = e837e3dbaa605efc867a213f3345cee14c36d8f5, the ledger pin. `E` has no other meaning
in r6. The certified execution head, which AGENTS.md sec. A.39 calls `E`, is `C` here (R6.NOTE.8).
Sources: E-021, V1-005, V2-003. Controls: none (definition).

**R6.NOTE.2** `H` = 53c6601a10419b6b333cc992474272501ab542af, the scientific base: the base of the
retirement ledger.
Sources: E-022, V1-005, V2-003. Controls: none (definition).

**R6.NOTE.3** `T1'` = 14ac71b4b0a0c0aa2d7068d6799a73f474097060, the executed trial tree: `H` plus the
399 ledgered splices. `T1'` is not reachable from `main`. A figure measured only at `T1'` is a
historical measurement unless a control whose inputs are on `main` reproduces it (sec. 31). `X_rep` is
the representative retirement candidate of R6.EVID.8, built from `H` and a ledger; it is the input of
every control whose verdict reads only what `H` and the ledger determine.
Sources: E-023, V1-005, V2-003, OC-3. Controls: none (definition).

**R6.NOTE.4** `P` = 4c79be642ca631573f06b444903be75ec4f5e2b6, the frozen plan: the plan commit holding
`ledger.json` and `edits.json`. `P` has no other meaning in r6 (R6.NOTE.12).
Sources: E-024, V1-005, V2-003. Controls: none (definition).

**R6.NOTE.5** `W` = 413b0bb88f39cad901befcf4684355c7ee39480b, `main` at the time of v3.
Sources: E-025. Controls: none (definition).

**R6.NOTE.6** `F` is the freeze of the amended plan: a commit id given to every run as an explicit
input (`--freeze`). It is the run's admitted plan commit (admission, sec. 11).
Sources: E-026, A-013. Controls: none (definition).

**R6.NOTE.7** `T` is the tool commit: the commit whose tool files a run executes, and the `head_sha` of
the producing CI run (sec. 11).
Sources: E-027. Controls: none (definition).

**R6.NOTE.8** `X` is the candidate (execution) commit. `C` is the certified execution head. `M` is
`main` at check time. `L` is the landing merge. Op C takes `C` from `--certified REV`, which defaults to
`X` (RD-33; B-10).
Sources: E-028, V1-005. Controls: none (definition).

**R6.NOTE.9** Every commit a run reads or records is a full 40-hex id; no ref name stands for one
(sec. 11, object integrity). The single exception, the re-resolution of `M` immediately before a
landing, is stated in sec. 23.
Sources: E-029. Controls: EI15.

**R6.NOTE.10** `R` is the frozen ledger record directory
`verification/audits/foundations/a1exit-ledger-20261120/`. Its tree is
b05efdca935a42b9c94ef1748c964696bf58fcd9 at 9882df8f2d41eee47790560b0e22aac03e95370f. Every run checks
`R`'s tree at each tree it evaluates against the configuration's pinned record tree; a difference is
ERROR `RECORD_TREE_MISMATCH` (R6.OUT.5). The equality at `H` and at `W` is a checked fact of the runs
that evaluate those trees, not an assumption.
Sources: E-030, V1-005, V2-003. Controls: M9.

**R6.NOTE.11** Path abbreviations: FULL is `book/The-Incompleteness-of-Observation-FULL.md`; chNN is
the book chapter file with that number.
Sources: E-031. Controls: none (definition).

**R6.NOTE.12** Terms of the record-directory rule (sec. 21). `P_cfg` is the configuration's path in `F`
(the path that `--config F:P_cfg` names), and `D_rec` is the directory part of `P_cfg` (empty for a
configuration at the repository root). An entry is a non-tree entry of a commit's tree with its mode:
regular files (`100644`, `100755`), symbolic links (`120000`) and submodules (`160000`). A path is
inside `D_rec` when it begins with `D_rec` followed by `/`; this one membership predicate is used by
every part of the rule. `F-entries` and `M-entries` are the entries inside `D_rec` at `F` and at `M`.
These names replace the earlier `P`, `D`, `E_F` and `E_M`, which collide with R6.NOTE.1 and
R6.NOTE.4; the migration index records the renaming (sec. 34).
Sources: A-014, A-013. Controls: none (definition).

**R6.NOTE.13** Identifiers and labels. Requirement ids, control ids, class identifiers, schema ids and
field names are identifiers; none is reused with another meaning (sec. 34). Review-finding and
decision labels cited in parentheses (for example R1, R6, R9, O2, O6, B-4, A-D5, C3, R-D5, D2, V5-D1)
are labels, not identifiers: where a label coincides with a control id, the label names no control.
The heading of the verbatim splitter text of sec. 8 uses "O6" as such a finding label; it names no control (B-20).
Sources: E-028. Controls: none (definition).

***

## 2. Purpose, non-goals and residual limits

**R6.PUR.1** Purpose. One evaluation pipeline verifies, for named commits:

- that the frozen record `R` is correct at its pin;
- that every ledger site and every terminology subject at a candidate is accounted for;
- that a candidate is exactly `H` plus the ledger;
- that a landing merge composes `main` with the candidate exactly.

Each mandatory check of the amended plan is one configuration of this pipeline (sec. 18).
Sources: E-051. Controls: none (purpose; each clause is tested through sec. 3 to sec. 7, 20 and 23).

**R6.PUR.2** Non-goal: scientific correctness. A PASS establishes coverage and provenance only; it is
necessary for coverage and never sufficient for correctness. It does not show that a replacement keeps
its finite-only, conditional or open qualification, that a classification rule's reading is right, or
that the frozen map's 16 fuzzy and 83 anchor relocations chose the right line at the pin. Whether a
moved sentence keeps its meaning in a new context is not decided by content matching, which shows only
that bytes are where, and what, a record says. These questions stay with the classification records'
reviewers, the plan's preservation and mirror-parity checks, the plan's independent non-author review
of the exact head, and the owner's decisions. Rule, adjudication and other records strengthen no claim;
a PASS strengthens no claim and moves no row (AGENTS.md sec. A.22, sec. A.46 item 1).
Sources: E-052, V1-008, V2-120, V1-149. Controls: none (non-goal).

**R6.PUR.3** Row dispositions. The tool reclassifies no row. Row, code and owner are carried from the
frozen map, and no record may change them. The frozen `assign()` and `s3()` functions are not re-run on
any tree later than the pin.
Sources: E-053, V1-010. Controls: H6.

**R6.PUR.4** The tool does not modify the frozen tool or any file in `R`, and its output is not a
replacement record.
Sources: V1-011. Controls: M9, RT-A.

**R6.PUR.5** Coverage scope. Op B's site and hit coverage is defined over the configuration's corpus
(for A1, `papers/*.md` and `book/*.md`). Op C checks every path of the candidate and of the other role
trees (sec. 20); a non-manuscript path (Lean, Python, JSON, the coverage ledger, TeX and PDF) is
accounted for by a ledger splice, a delegation class (sec. 13) or a side-change class, and the
delegated checks themselves stay outside the tool's semantics (R6.PUR.10). A result's
`covered_paths` lists exactly the paths its verdict covers (R6.OUT.19).
Sources: V1-009. Controls: none (scope statement; tested through sec. 13 and sec. 20).

**R6.PUR.6** The tool is the verification route for the amended plan's mandatory checks (sec. 18). It
decides no scientific question and no row disposition (R6.PUR.2, R6.PUR.3).
Sources: V1-012. Controls: none (scope statement).

**R6.PUR.7** Residual limits.

- Coverage is defined by the sites, the profiles and the rules. A removed qualifying sentence is not
  detected if it matches no profile and sits next to no context-required site.
- The context mapping and the indicators of sec. 6 are preregistered heuristics.
- A rule fingerprint recognizes only identical text. Any edited or new legitimate use returns to
  REVIEW_REQUIRED or FAIL.

Sources: E-054, RV-021. Controls: none (limit).

**R6.PUR.8** Lexically unanchored paraphrases. The deny rules close only forms with a fixed lexical
anchor. A paraphrase without such an anchor cannot be closed by a regular expression. On added text,
the outcome is at least REVIEW_REQUIRED only for the classes that the plan's pinned `resid` rule file
(sec. 12) or another review profile matches. Those classes are the content of the plan's rule files,
which are control inputs pinned at `F`, not requirements of the tool. For the rule files current when
r6 was drafted they are, informatively:

- a finiteness word together with a posit noun (posit, premise, axiom, assumption, hypothesis) within
  a 60-character window of one sentence;
- a state-space noun (configuration, state or phase space) followed by "is finite" or a similar
  copula;
- "finite set", with at most one word between;
- "substratum", "universe" or "world" followed within 40 characters by "is", "be", "being" or "are",
  an optional article and at most one word, and "finite";
- "finite number" or "finite count" of states, configurations, elements, points or sites.

A paraphrase outside the classes the pinned rule files match stays outside the tool; its detection
rests on the plan's independent review of the exact head. Constructed examples outside those classes,
which PASS when added: "the six posits of the substratum", "six assumptions about the substratum",
"The posit ledger lists fourteen.", "the fourteen-item posit ledger" and "$A_1$–$A_6$". The plan's
original literal item 7 misses each of these too. The two examples of R6.PUR.9 are not part of this
requirement.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-055. Controls: V15, V21, V26.

**R6.PUR.9** For decision at adoption (not adopted by this draft): the residual for the deny rule
DR-2. The two texts "the framework's sixth structural property, finiteness of the bijection" (control
V4) and "The framework's sixth structural property is finiteness of the substratum" (control V27)
match no deny rule once DR-2 is not in the active rule set, and PASS when added; the plan's original
literal item 7 misses both. Whether the tool's expected outcome for these texts is PASS (an accepted
residual) or FAIL (DR-2's expectation restored) is an owner decision at adoption (RD-14, Q10), with
these options:

- (a) confirm the accepted residual: V4 and V27 expect PASS, kept so that a change in their outcome
  is visible;
- (b) restore V4's FAIL expectation, which needs DR-2, or a successor rule, in the plan's active rule
  set.

The decision covers V4, V27, V27-glossary and V15 together, which rest on the same decision V5-D1
(RE-1). Until it is made, each of the four rows carries both candidate expectations, each marked
"not authoritative; decided at r6 adoption", and an `expect` of outcome DEFERRED; the gate reports
`deferred-expectation` for each and never holds on it (R6.GATE.9). Outstanding evidence, a named
blocker on adoption of this requirement: the owner decision V5-D1 that dropped DR-2 is recorded only
in paraphrase (ME-6); its text is to be recorded by the owner.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-055, RE-1. Controls: V4, V27, V27-glossary, V15.

**R6.PUR.10** Delegated checks stay outside the tool's semantics, even when their evidence is bound to
`X` or `C`. The tool checks that role fields of a record differ; it cannot check who wrote a record
(sec. 11).
Sources: E-056, RV-021. Controls: none (limit).

**R6.PUR.11** Approval is outside the tool. The tool verifies which exact plan, configuration, tool and
evaluated commits a run checked, and identifies them in its result. Whether that plan is the one the
owner approved is confirmed by the owner, procedurally (R6.STAT.4). No output, outcome, field or
control of the tool states or implies that a plan, a record, a run or a result was approved or
authorized. Admitted record directories are named "admitted", never "authorized" (sec. 21).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-057. Controls: B4-MEANING.

**R6.PUR.12** Entry type of a side change. For every side change, inside or outside `D_rec`, the tool
reads the entry's mode (R6.NOTE.12) before any read of its bytes, and never reads a symbolic link or a
submodule as file content. At the tool commit, a symbolic-link or submodule side change outside
`D_rec` reaches the side-change classifier's byte read, which refuses it; that is a verification
defect, corrected in a later tool revision with a control that plants a symbolic-link and a submodule
side change outside `D_rec`. Such an entry is REVIEW_REQUIRED `side-change-unclassified` with the
reason `not a regular file`, as inside `D_rec` (R6.RDIR.7; RE-15).
Sources: A-140. Controls: SIDE-NONREG.
***

## 3. Pipeline stages, subject kinds, operations and ledger fields

**R6.PIPE.1** Stages. Every run executes the same stages in a fixed order. A stage that fails stops all
later stages.

1. **Usage.** Arguments are parsed and the `--out` guard (R6.OUT.7) is applied.
2. **Integrity.** Objects (each verified against its id, sec. 11), the tool's own files against `T`,
   pins, record hashes, ledger hashes, the configuration and the adapter module blobs are checked.
   Configuration validation that depends on a role (the record-directory checks of sec. 21, which
   apply only where `M` is given) runs here once the roles are known (sec. 29).
3. **Controls.** The in-memory preflight controls run.
4. **Identity.** Every subject is located.
5. **Provenance.** Ledger splices, HP adjudications and reconciliations are applied.
6. **Classification.** Profiles, rules and records are applied.
7. **Outcome.** The overall result is computed.

Op B and op C rebuild the site anchors in memory from the record and pin objects, by the same
derivation as op A; they do not re-run op A's replay.

Sources: E-058, V1-035. Controls: none (no control checks the stage order directly; X1 and R6.OUT.9's
precedence depend on it).

**R6.PIPE.2** Operations. The tool has four operations, which share the code paths of the pipeline
stages:

| Op | Subcommand | Question | Roles used |
|---|---|---|---|
| A | `record` | Is the frozen record `R` correct at its own pin? It replays the frozen tool at the pin only (R6.PIPE.10) and derives the site anchors in memory; the digest of the anchor list is recorded as `record_checks.anchors_sha256`. | `E`, plus the record commit |
| B | `coverage` | Is every site of `R` accounted for at the named commit, unchanged and possibly moved, or rewritten by an identified splice of the frozen ledger, and is every hit classified? Op B never regenerates, rewrites or re-renders `R`. | `E`, `H`, `X` |
| C | `execution` | Is candidate `X` exactly `H` plus the ledger, with its preconditions met at `H` and its pins intact? Does landing `L` compose current `main` with `C` exactly (sec. 20)? | `H`, `X`, `C`, `M`, `L` |
| D | `terms` | Is every terminology hit at the named commit classified, with no deny-rule match? | one commit; with `--base B --ledger F:ledger.json`, also the added text of `B..commit` |

A change on `M` to a corpus file is decided by op C as `base-drift` (sec. 23), not by op B. Whether
op B also evaluates `L` is fixed by the conformance check of RD-35.
Sources: E-060, V2-013, V1-006, V1-007. Controls: RT-A, RT-E, RT-C, RT-D.

**R6.PIPE.3** Command line. The subcommands are `record`, `coverage`, `execution`, `terms`, `replay`,
`self-test` and `purity-lint`. Every evaluating subcommand takes `--config F:P_cfg`, `--freeze F`,
`--out DIR` and `--repo DIR`. Op A takes `--pin` and `--record`; op B takes `--commit`, `--segment`
(repeatable), `--hp` and `--classify` (repeatable), `--check` and `--final`; op C takes
`--scientific-base`, `--candidate`, the flag supplying `C` (R6.NOTE.8), `--main`, `--landing`,
`--ledger`, `--edits`, `--delegation`, `--evidence` and `--classify`; op D takes `--commit`, `--base`,
`--ledger`, `--profile`, `--check`, `--final`, `--scope`, `--rules` and `--classify`; `replay` takes
`--snapshot`. There is no `--prior` flag (R6.PIPE.8). This list is the parser at the tool commit; it is
confirmed against the requirements of r6 by the conformance checks of OD-25 and RD-33, and any
difference is a finding (R6.STAT.5).
Sources: V1-068. Controls: X3, X4, X5.

**R6.PIPE.4** Repository. The repository is given by `--repo DIR`; by default it is the repository
containing the invocation directory. `git rev-parse --git-dir` must succeed in it; otherwise the run
ends with ERROR `UNRESOLVABLE`. This safeguard is preserved from v1 and is confirmed at adoption
(RD-15).
Sources: V1-017. Controls: none.

**R6.PIPE.5** Role commits. Every role commit is given as an explicit full 40-hex id (R6.NOTE.9), and
every read is a read of `(commit, path)` through the verified object reader (sec. 11). No role is
resolved from a ref name, except the re-resolution of `M` (sec. 23).
Sources: V1-021. Controls: EI15.

**R6.PIPE.6** Segments. A segment is `FROM..TO`, given as `--segment FROM..TO` or
`--segment FROM..TO=LREV:LPATH`, repeatable and ordered. It is ledgered when it names an exact-edit
ledger of the `ledger.json` form, whose schema id is configuration content (for A1,
`a1exit deletion exact-edit ledger v2`), and unledgered otherwise. The chain starts at the pin and ends
at the named commit, and consecutive endpoints are equal; a broken chain is an integrity ERROR
(R6.OUT.5). With no `--segment`, op B uses one segment from the pin to the named commit: it is of kind `hp`
when an HP obligation of the configuration names it (as in RT-H0), and unledgered otherwise (OD-25;
B-13).
Sources: V1-022, V1-036, V1-069. Controls: none.

**R6.PIPE.7** Site state across segments. A site's state is carried between segments: `resolved`
(current file, byte span and bytes) or `unresolved` (with the segment in which it became so). An
unresolved site stays unresolved in later segments, and its item is carried forward with its origin
segment in the item's `segment` field. An HP site resumes tracking as sec. 5 states.
Sources: V1-038. Controls: none.

**R6.PIPE.8** Prior endpoint. The prior endpoint is the `FROM` of the last segment; no flag names it.
`pre_existing` on a hit or item is computed by the same scan at the prior endpoint. It is reporting
only: a caller that wants "new since the prior endpoint" reads `items[*].pre_existing` from
`result.json`, and the exit status still reports every item (R6.OUT.17). This is to be confirmed by
the conformance check of OD-25.
Sources: V1-024. Controls: none.

**R6.PIPE.9** Op A integrity. Op A first resolves the pin and the record commit and checks `R`'s tree
id and the pins. A pin that is not the recorded pin is ERROR `PIN_MISMATCH`; a record tree that is not
the pinned tree is ERROR `RECORD_TREE_MISMATCH` (R6.OUT.5).
Sources: V1-029. Controls: X1, M9.

**R6.PIPE.10** Op A replays the frozen tool only at its pin. Every read comes from the object store;
the only writes are under `--out` (R6.OUT.7).
Sources: V2-008. Controls: RT-A, X1.

**R6.PIPE.11** Op C preconditions at the base. At `H`:

- every splice's `old_sha256` matches its span;
- every edit's `old` is selected exactly once, by the per-edit selection and in-order application of
  sec. 9, and every applied edit is bound to its splice; any other relation is ERROR `LEDGER_INTEGRITY`,
  naming the edit and splice ids;
- `edits_sha256` matches;
- every edit id maps to exactly one splice, with equal hashes; the `retained_unchanged` edits map to
  none, and their site text is unchanged at `H` and at `X` (R6.PIPE.15).

Sources: V2-015, V2-016, V2-017. Controls: S11-57c, S11-58h, S11-58j.

**R6.PIPE.12** Subject kinds. Each subject kind has its own anchor and context rule.

| Kind | Anchor | Context | Source |
|---|---|---|---|
| `site` | exact pin line bytes, `pin_count`, `ordinal` | sec. 6 | frozen `sitemap.json` |
| `splice` | id, span, `old_sha256`, `new_sha256` at `H` | the image's offset in `X` | `ledger.json` at `F` |
| `hit` | file, segment, `line_sha256` (unique in its tree) | the sentence and its neighbours | profiles (sec. 9) |
| `pin` | check file, exact literal, target file, occurrence counts at `H` and at `X` | none | Python literals of tracked checks, by `ast` |
| `mirror` | edit id pair (`mirror_of`) | none | `edits.json` at `F` |
| `path` | path and blob id in each role | none | the role trees (sec. 20) |
| `delegated` | delegation entry id | none | `delegation.json` at `F` (sec. 13) |

Sources: E-059. Controls: none (definition).

**R6.PIPE.13** Where deny profiles run (O2). Deny profiles (sec. 9) are evaluated on every tree a run
evaluates except the two trees the configuration names as retired-form trees (`roles.pin` and
`roles.scientific_base`, for A1 `E` and `H`), where the retired forms are expected. In op D they are
evaluated on the named commit whatever it is, so that their countercontrols at `H` run through op D.
`result.json` lists the profiles evaluated on each tree (`profiles_evaluated`).
Sources: E-061. Controls: RT-E, RT-DR.

**R6.PIPE.14** Added text. Profiles with `applies_to: added-text` are evaluated on the splice images of
a ledgered segment. In op D they run only with `--base` and `--ledger`. For A1 these are the
configuration's `register` and `infinity` profiles and the plan's `resid` rule file (sec. 12).
Sources: E-062. Controls: RT-D, S11-5, S11-6.

**R6.PIPE.15** Ledger adapter rules. The ledger adapter (sec. 26) reads the ledger. For A1:

- `retained_unchanged` (D032, D039): each id must exist in `edits.json`, must have no splice, and must
  have its site text byte-identical at `H` and at `X`; otherwise FAIL `retained-changed`;
- every other unread ledger field is reported under `ignored_fields`;
- an unknown ledger schema id is ERROR `LEDGER_INTEGRITY`, under the role "pinned input whose content
  fails its integrity rules" (R6.OUT.5; RE-16).

Sources: E-063. Controls: CLASS-RETAINED.
***

## 4. Pin, anchors, translation and relocation, file conformance, content search

**R6.ANCH.1** Pin. The configuration's `roles.pin` is compared with the pin the sitemap adapter reads
from the frozen `sitemap.json` and `rows.json`. A difference is ERROR `PIN_MISMATCH`, exit 65, with the
fields of R6.OUT.5, produced before any frozen code runs.
Sources: V1-018. Controls: X1.

**R6.ANCH.2** Op A accepts only the pin. It never evaluates the frozen record against a later tree;
that comparison is meaningless by construction.
Sources: V1-034. Controls: X1.

**R6.ANCH.3** Record. `R`'s tree id at the record commit equals the configuration's pinned record tree
(`adapters.replay.record_tree`; for A1, b05efdca935a42b9c94ef1748c964696bf58fcd9); otherwise ERROR
`RECORD_TREE_MISMATCH`. The frozen `sitemap.json`'s `manuscript_digest` equals the digest of the pin's
corpus; this is a named equality of the replay interface (sec. 26), beside the `build` and `render`
equalities, reported in `record_checks.equalities`.
Sources: V1-019. Controls: M9, RT-A.

**R6.ANCH.4** Ledgered-segment integrity. For a ledgered segment: the ledger's `base` equals `FROM`; if
`edits_sha256` is present, the `edits.json` beside the ledger at `LREV` hashes to it; every splice's
`old_sha256` equals the SHA-256 of `FROM`'s bytes `[start, end)` and its `new_sha256` that of `new`
(UTF-8); splices in one file do not overlap; and each ledgered corpus file's `base_sha256` equals
`FROM`'s blob. A failure is an integrity ERROR, not an item: `LEDGER_INTEGRITY`, `EDITS_HASH_MISMATCH`
or `SCIENTIFIC_BASE_MISMATCH`, as R6.OUT.5 assigns (pending the conformance check of OD-4).
Sources: V1-037. Controls: M3, M4, M5.

**R6.ANCH.5** Identity normalization. The anchor is the exact UTF-8 bytes of the site's line at the
pin, without its terminating LF. A site's span is its line's bytes plus its terminating LF
(R6.ANCH.14). A corpus file that is not valid UTF-8, or that contains CR, is ERROR `ENCODING`,
exit 65.
Sources: V1-039, V1-040. Controls: M11, U1.

**R6.ANCH.6** `whitespace_only` is a diagnostic. It is computed only to label a failing site: the
site's pin bytes and the replacing bytes are compared after every whitespace run is replaced by one
space and leading and trailing whitespace is removed; Unicode normalization is not applied. It is computed only for a single-line site, in the unledgered search, on a
replace operation; otherwise it is false (B-14). It never makes a site pass. A whitespace change is not presumed meaning-free, since Markdown whitespace can
change rendering (line breaks, code blocks).
Sources: V1-041. Controls: U9.

**R6.ANCH.7** Per-site anchor fields. For every site of the frozen map: `site_id`, whose form belongs
to the sitemap adapter (for A1: the file path, a colon, the pin line number, the at-sign character and
`e837e3db`, the pin key, stable because it names the pin); `anchor_sha256`, the SHA-256 of the pin line
bytes; `pin_count`, the number of lines in the file at the pin with identical bytes; `ordinal`, the
1-based index of this line among them, ordered by byte offset; and the context hashes of sec. 6.
There are no `read` entries: a hit is held only by a tracked site (sec. 14), and the adapter interface
has no `read_entries` (sec. 26).
Sources: V1-042, V1-043, V2-005. Controls: RT-A.

**R6.ANCH.8** Override anchors. An override's `anchor` string is checked once, at the pin, to be a
substring of the pin line, and the override is bound to the site id, so it is never searched for later.
A failed check is recorded in `record_checks.pin_findings` and makes op A FAIL `record-invalid`
(R6.OUT.27), pending the check of what the code emits (RD-27).
Sources: V1-046. Controls: none.

**R6.ANCH.9** File conformance first. For each file a ledgered segment touches, the expected `TO` file
is rebuilt from `FROM` and the file's splices, applied in ascending `start`. If `TO`'s blob differs, the
file is FAIL `unauthorized-edit`, fingerprinted by the expected and actual file hashes and the segment
(R6.OUT.19). The byte ranges that differ outside all splice images, computed by a deterministic
`difflib.SequenceMatcher(autojunk=False)` comparison of expected and actual and reported as `TO` line
ranges, are diagnostics only. That file's sites are then processed by the unledgered rules
(R6.ANCH.17), every site included (R6.ANCH.10).
Sources: V1-049, V2-006. Controls: M1, M2.

**R6.ANCH.10** Adjudicated HP sites are searched. In a ledgered segment, an adjudicated HP site in a
file that does not conform, or in a file with an unledgered change, takes the unledgered search of
R6.ANCH.17 and yields its site-level item like any other site. At the tool commit such sites are
excluded from the search (the run fails closed); that is a verification defect (VD-2), corrected in a
later tool revision, with a control in which an adjudicated HP site in a ledgered segment whose file
does not conform yields its site-level item.
Sources: V2-006, V1-049. Controls: VD2-HP-SEARCH.
**R6.ANCH.11** No overlap: translation. If a site's span meets no splice span (R6.ANCH.14), the span
is translated by the cumulative length change of the preceding splices. Cross-check: the bytes at the
translated span equal the anchor bytes, and the content search of R6.ANCH.17 finds exactly that line;
any disagreement is FAIL `ambiguous`. The status is `unchanged` if the line number is the same, else
`moved`, with `line_delta`.
Sources: V1-050, V2-006. Controls: U3, U2.

**R6.ANCH.12** Translation of a pin-duplicated line. For a site whose `pin_count` is greater than 1, or
whose current text is not unique, the translation applies the duplicate rules of R6.ANCH.17 as well: a
changed count is `duplicated`; with an equal count, only occurrences whose context hash matches are
kept, and the site is resolved only if exactly one remains and its ordinal equals the recorded ordinal,
otherwise FAIL `ambiguous`. At the tool commit the translation accepts any occurrence at the translated
line without these checks; that is a verification defect (VD-3), corrected in a later tool revision,
with two controls: a duplicated site whose count changes is `duplicated`, and one whose context does
not match is `ambiguous`.
Sources: V1-050, V1-057, V2-006. Controls: VD3-COUNT, VD3-CONTEXT.
**R6.ANCH.13** Overlap: authorized replacement and removal. If splices overlap a site, the region is
the union of the site line and every overlapping splice span, extended to whole lines. The expected new
region is `FROM`'s region with those splices applied. Its image in `TO` is located by offset
translation and must equal it byte for byte. The status is then `authorized-replacement`, with
`splice_ids`, each splice's `old_sha256` and `new_sha256`, the new line range and `new_region_sha256`;
if the new region is empty, the status is `authorized-removal`. The site's current bytes become the new
region for later segments. These fields are the complete result of the overlap rule.
Sources: V1-051. Controls: U10, U11, B1, B2.

**R6.ANCH.14** Boundary cases.

- A splice overlaps a site if `start < site_end` and `end > site_start`. A zero-length splice at an
  interior offset also overlaps. A splice that only touches a site's boundary does not.
- A hit line is "in a splice image" if it contains the splice's offset in `X`. Empty images are
  included (for example D029 at Substratum.md:268).
- A removed site (empty image) has no replacement region; the line holding its offset is reported with
  the removal, not counted as a region line.
- A last line without LF is a line. Its span ends at end of file.
- A site's span is its line's bytes plus its terminating LF. A splice that starts at the site line's LF
  therefore overlaps the site, and the replacement region includes the lines it inserts.

Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-110, E-111. Controls: B1, B2, B3, B4, B6.

**R6.ANCH.15** Files not in the ledger. A corpus file that the segment's ledger does not touch must be
byte-identical between `FROM` and `TO`; a difference is FAIL `unledgered-file-change`, and that file's
sites take the unledgered rules of R6.ANCH.17.
Sources: V1-052. Controls: CLASS-UNLEDGERED.
**R6.ANCH.16** Postconditions at the candidate. Every ledgered file conforms to its base plus its
splices (R6.ANCH.9), and every splice's `new` lies at its translated span.
Sources: V2-018. Controls: M1, M2, U10.

**R6.ANCH.17** Unledgered segments: exact search. Per file: if the blob is unchanged, every site is
carried unchanged. Otherwise, for each resolved site with current bytes `t` (one line, or a multi-line
region after an earlier replacement), the occurrences `n` of `t` as whole lines in `TO` are counted:

- `n == 1` and the pin or previous count was 1: `unchanged` or `moved`;
- `n == 0`: unresolved. Diagnostic only: the deterministic line diff of `FROM` against `TO` maps the
  site's line to a replacement hunk (FAIL `unauthorized-change`, with `whitespace_only`) or to a
  deletion with no replacement (FAIL `missing`);
- `n` differs from the previous count (for example 1 to 2): FAIL `duplicated`, unresolved, regardless
  of context;
- `n` equals a previous count greater than 1: only occurrences whose context hash matches are kept; the
  site is resolved if and only if exactly one remains and its ordinal equals the recorded ordinal;
  otherwise FAIL `ambiguous`.

Sources: V1-053, V1-054, V1-055, V1-056, V1-057, V2-007. Controls: U1, U2, U4, U5, U6, U7, U8, M6, B5,
RT-E, SW1.

**R6.ANCH.18** No resolution by proximity or similarity. Nothing is ever chosen by proximity to an old
line number, and no fuzzy or similarity score resolves a site, in a ledgered or an unledgered segment.
This is a requirement of the design, verified by the controls named here and by review of the
implementation (Q10).
Sources: V1-058, V2-007. Controls: U5, U6, U7.

**R6.ANCH.19** Pins. For each string literal of each tracked Python check at `X`, extracted with `ast`
as the frozen `py_literals()` does, the tool compares its presence in the ledgered targets at `H` and
at `X`. A literal present at `H` and absent at `X` passes only if a guard-pin splice changed it or a
PIN_OK entry allows it. Every PIN_OK entry must be listed in the pin table of the plan frozen at `F`,
or in a reviewed record pinned by that freeze; otherwise the literal is FAIL `pin-broken`. Every pin
updated by a splice must occur in its target at `X`; otherwise FAIL `pin-target-missing`.
Sources: V2-020, RV-026. Controls: N1, S11-12.

***

## 5. Historical provenance obligation (`E..H`)

**R6.HP.1** Merges. The configuration record pins the merges of the HP obligation by full commit id
(for A1, sec. 27). The engine contains no merge ids. The tool cross-checks each pinned merge against
the pull-request number in its subject, and never resolves a merge from subject text. A pinned merge whose subject names another pull-request
number is ERROR `CONFIG_INVALID`, detected before any subject is evaluated (RE-31).
Sources: E-064, RV-020, V2-036. Controls: none.

**R6.HP.2** Region walk. For a site, the region is a block of whole lines. For each first-parent
commit `c` with parent `p` in `E..H`, in order, the region is updated as follows.

1. **Carried.** If the region occurs exactly once as a whole-line block in both `p` and `c`, it is
   carried unchanged.
2. **Not unique at the parent.** If it does not occur exactly once in `p`, the site is FAIL
   `provenance-ambiguous`.
3. **Changed at this commit.** Otherwise the site is changed at `c`:
   - The upper anchor is the nearest line above the block in `p` that occurs exactly once in `p` and
     exactly once in `c`. If there is none, the sentinel `BOF` is used. The lower anchor is chosen the
     same way below the block, with the sentinel `EOF`.
   - The anchors must keep their order in `c`. If they do not, the site is FAIL `provenance-ambiguous`.
   - The pre-region is the lines of `p` strictly between the anchors. The post-region is the lines of
     `c` strictly between the anchors. Both are trimmed of leading and trailing blank lines.
   - The step `{commit c, parent p, position k, pre_sha256, post_sha256}` is recorded. The post-region
     becomes the region.

These rules depend only on the two texts; no diff algorithm decides a pass. An empty post-region means
the site was removed in that step. A step at a commit that is not a pinned merge (R6.HP.1) is FAIL
`provenance-foreign`.
Sources: E-066, V2-037, RV-008. Controls: H2, H3, RT-H0.

**R6.HP.3** Region mergers (R6, V1). Two sites whose walks produce the same post-region at the same
step share that region from then on. The tool reports each such site with `region_shared_with`: the
sorted list of the other site ids, the step at which the regions merged, and the shared region's hash.
A merger is never silent. The merger groups on `E..H` are an expected result of RT-T0, stated in the
expectation file.

Informative (measured on `E..H`; the sites of a group sit two lines apart, separated by blank lines;
blank lines are never unique, so the anchors fall outside all sites of the group and their pre-regions
become one block):

| Step | Groups (sites at the pin) |
|---|---|
| #1475 (7f28886f) | FULL 4897/4899/4901/4903; FULL 4921/4923; FULL 4973/4975; ch18 166/168/170/172; ch18 190/192; ch18 242/244; papers/Methodology.md 146/148; papers/Methodology.md 367/369 |
| #1474 (a1f38284) | papers/Substratum.md 266/268 |

Sources: E-067. Controls: H7, RT-T0.

**R6.HP.4** HP adjudication record, schema `oi-hp-adjudication/1`. The record is an immutable file in
the audit directory, under the ownership chain of sec. 11. It lists each `site_id` with:

- `steps`: each step's commit (full id), parent, position, `pre_sha256` and `post_sha256`;
- the carried `row`, `code` and `owner`, which must equal the frozen values; otherwise FAIL
  `adjudication-row-changed`;
- `own_lines`: for a site with `region_shared_with`, the lines of the shared final region at `H` that
  carry this site's text, by `line_sha256`; required for every merged site of R6.HP.3, whether or not a
  splice overlaps the region; for an unshared site, the whole final region;
- `semantic_classification`: which qualification is visible on the site's own lines, with the reason;
  for a shared region each site is classified on its own lines, never only on the block;
- `splice_attribution`: for each `H..X` splice that overlaps the final region, the site ids whose own
  lines it intersects;
- `hit_classifications` for every profile hit in the final region (sec. 14), bound by `line_sha256`;
- `context`: the pin and `H` context hashes plus a semantic statement, required when sec. 6 marks the
  site and its context changed in `E..H`;
- `author`.

The record carries no owner-approval field; owner approval is procedural (R6.STAT.4), and the review
record that admits it is bound by blob (sec. 11).
Sources: E-068, V2-035. Controls: H6, H7.

**R6.HP.5** `semantic_classification` is the reviewer's judgement of what the text means. Provenance
shows where the text came from; the tool checks only that the classification is present and
fingerprinted.
Sources: V2-041. Controls: none.

**R6.HP.6** Walk recomputation. The tool recomputes the walk of R6.HP.2 and compares it with the
record. The result is:

- `provenance-adjudicated` only if every step matches exactly;
- FAIL `provenance-mismatch` if a commit or hash differs (for example the record names one merge
  where the walk gives another);
- FAIL `provenance-gap` if a step is missing or extra (a text change between listed steps);
- FAIL `provenance-foreign` or `provenance-ambiguous` as in R6.HP.2 (a change at a commit outside the
  pinned merges; a region that is not unique at a step);
- FAIL `hp-unadjudicated` if no record names the site;
- FAIL `record-invalid` if a site with `region_shared_with` has no `own_lines`, if the own lines of
  the sites sharing a region leave a non-blank region line unassigned, or if a splice overlapping the
  region is attributed to no site.

Sources: E-069, V2-038, V2-039, V2-040, RV-055. Controls: H1, H2, H3, H7, RT-H0.

**R6.HP.7** The status `provenance-adjudicated` is distinct from `moved` and `authorized-replacement`
in every count, and is counted separately under `HP` and under `RET`. A matching adjudication resolves
its site with that status; this positive case is tested by U14, restated as an HP adjudication case
(RD-9 (a)). At the tool commit an adjudicated site is marked only by its `provenance`
reference and is counted under its last segment state; the distinct status and its separate counts
are an implementation obligation (OBL-28; Q12, RE-6). An adjudication entry whose region hash
differs from the walk (U14's second case) gives FAIL `provenance-mismatch`, because the record does
not match the walk, and FAIL `stale-adjudication`, because the entry then resolves no subject
(R6.REC.10); any other class emitted for that case is a defect (Q12, RE-7).
Sources: V1-062. Controls: U14.
**R6.HP.8** Resumed tracking. An adjudicated site resumes tracking in `H..X` from its final region at
`H`, through every later segment, under the ledgered rules of R6.ANCH.9 to R6.ANCH.16 and, where its
file does not conform or has an unledgered change, under the search of R6.ANCH.17 (R6.ANCH.10). It
then becomes `authorized-replacement`, `authorized-removal`, `unchanged`, `moved` or a `RET` FAIL.
Sources: E-070, RV-009. Controls: H4, SW2.

**R6.HP.9** Separate HP and RET entries. An HP site whose `H` region is touched by any `H..X` splice
keeps two independent entries: in `HP`, its provenance status; in `RET`, its `H..X` status, with
`hp_overlap: true` and the splice ids. Neither entry is counted in the other obligation's totals. An
`E..H` edit is never reported as a retirement edit, a retirement splice is never reported as
historical, and the HP obligation is never attributed to the retirement.
Sources: E-071. Controls: H5, RT-T0, SW2.

**R6.HP.10** Every HP site appears under `RET` in `H..X` explicitly, as `authorized-replacement`,
`authorized-removal`, `unchanged`, `moved` or a failure; none is invisible to `RET`.
Sources: RV-010. Controls: RT-T0.

**R6.HP.11** Untracked overlap. Without an adjudication, an HP site stays unresolved. Its `RET` entry is
then FAIL `untracked-hp-overlap`, listing the overlapping splices. This makes the retirement's
rewrites of historical sites visible before any adjudication exists.
Sources: E-072. Controls: H5, RT-T0.

**R6.HP.12** Two overlap counts (R6). Each `RET` entry carries `region_splices` (splices overlapping the
site's final region, the decision basis) and `line_splices` (a diagnostic: splices intersecting the
site's own line, tracked through each step by `git diff -U0 --no-renames` with the myers algorithm,
carrying the site's line range through the hunks). The FAIL class and the totals use `region_splices`.
Once an adjudication exists, `line_splices` is replaced by the record's `splice_attribution`, which the
tool checks as R6.HP.6 states.
Sources: E-073. Controls: H7.

**R6.HP.13** Segment assignment. Every item is assigned to the segment in which its change occurred. A
context change on a meaning-required site (sec. 6) that occurred in `E..H` is an `HP` item. It is
resolved only by the `context` field of that site's HP adjudication, or of a context adjudication for
an unchanged site. Indicator items of sec. 6 that arise in `E..H` are also `HP` items.
Sources: E-075, RV-011. Controls: RT-H0.

**R6.HP.14** Supply of HP records. HP adjudication records enter a run as records supplied with `--hp`
or `--classify` and admitted under the ownership chain and record lint of sec. 11; a record that fails
its schema is FAIL `record-invalid` (R6.OUT.5). A record resolves a site only when every fingerprint it
carries matches exactly.
Sources: V1-023. Controls: none.

***

## 6. Context rule and indicators

**R6.CTX.1** Preregistration. The context rule was decided at S0, before any implementation output. It
is stated per frozen s3 value and per indicator. Its authority is r6's adoption. Its counts at `T1'`
are reported, never tuned.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-076. Controls: none (definition).

**R6.CTX.2** Context definition. The context of a site is the ordered pair of the nearest non-blank
line above and the nearest non-blank line below, with sentinels `BOF` and `EOF`. Its hash is
`sha256(above + 0x00 + below)`, taken at the pin (`pin_context_sha256`) and at every tree
(`current_context_sha256`).
Sources: E-077, V1-044, V2-030. Controls: K2.

**R6.CTX.3** Identity. Context is required for identity when `pin_count > 1`, or when the current text
is not unique (R6.ANCH.12, R6.ANCH.17). A context change then makes the site FAIL `ambiguous`.
Informative: all 697 pin lines are unique at `E`.
Sources: E-078, V2-031. Controls: U7.

**R6.CTX.4** Meaning. Context is required for meaning exactly when the frozen record does not establish
that the qualification is visible on the site's own line. A `per unit` status stays on the required
side: it means the qualification was established by a unit's correction, which may sit in a
neighbouring sentence. The mapping from each frozen s3 value to `meaning_context` is part of the A1
configuration (sec. 27):

| Frozen s3 value | Sites at `E` (informative) | `meaning_context` |
|---|---|---|
| visible (names the hypothesis); rewritten at deletion | 194 | false |
| visible (P0/P1/P2 disposition) | 144 | false |
| visible (applied splice) | 5 | false |
| visible (none: the (NR) corollary ...) | 3 | false |
| n/a | 136 | false |
| not determined: Q3 census | 81 | true |
| not determined | 28 | true |
| per unit regression audit (#1468) | 45 | true |
| per unit Q1 corrections (Step 2) | 28 | true |
| per unit Step-2 phase | 15 | true |
| per unit R6 corrections (Step 2) | 9 | true |
| per unit R1/R2 scoping | 8 | true |
| per unit Q2 | 1 | true |

Sources: E-079, RV-012, V2-032. Controls: K1, K3, K4.

**R6.CTX.5** The indicator ANAPH (R6.CTX.9) also sets `meaning_context` to true. A reviewed context
adjudication may set it to true for a further site. Nothing can set it to false for a site the table or
ANAPH marks.
Sources: E-080. Controls: K5.

**R6.CTX.6** Decision table.

| Condition | Result |
|---|---|
| `meaning_context` true, context changed, no context adjudication matching both hashes | FAIL `context-meaning-unverified` |
| `meaning_context` true, context changed, matching adjudication | PASS |
| LIST or TABLE site, its structure context or its context changed, no adjudication matching both context hashes and both structure hashes (R6.CTX.11) | REVIEW_REQUIRED `context-structure-changed` |
| `meaning_context` false, context changed, not covered by the row above | PASS with `context_changed: true`; requires verified identity and identical site bytes |

FAIL takes precedence: a LIST or TABLE site whose `meaning_context` is true and whose context changed is
FAIL `context-meaning-unverified`. In the last row, relocation stands on verified identity with
byte-identical line text, and the change is reported, not failed.
Sources: E-081, V2-033, V1-059. Controls: K1, K2, K3, K4, K6, K7, K8, K10.

**R6.CTX.7** Context adjudication, schema `oi-context-adjudication/1`. It records `site_id`, `segment`,
`from_context_sha256`, `to_context_sha256`, for LIST and TABLE sites also `from_structure_sha256` and
`to_structure_sha256`, and a semantic statement that the qualification is still visible or still
stated. It carries `author` and is under the ownership chain of sec. 11. It is the reviewed record that
resolves a context FAIL; the expected outcome of the real-tree control with every record present follows
from R6.CTX.6, not from a fitted count.
Sources: E-082, RV-013. Controls: K10.

**R6.CTX.8** Indicators. All four indicators are computed on the site's pin line at `E`. They were
preregistered at S0 with the definitions of R6.CTX.9, which are part of the A1 configuration
(sec. 27). A change to any of them is a configuration change and is widening (sec. 25).
Sources: E-083. Controls: none.

**R6.CTX.9** Indicator definitions.

- `strip(line)`: remove leading whitespace, then any run of blockquote markers `>` with their
  following whitespace, then one heading marker `#{1,6}` with its whitespace, then one list marker
  (`-`, `*`, `+`, or digits followed by `.` or `)`) with its whitespace, then any run of `*` and `_`.
- **ANAPH**: `strip(pin line)` matches, case-sensitively,
  `^(This|These|Such|Hence|Thus|It|Under this)\b`.
- **LIST**: the pin line matches either
  - `^\s*(>\s*)*([-*+]|\d+[.)])\s+` (a list item), or
  - `^\s*(>\s*)*(([-*+]|\d+[.)])\s+)?[*_]{0,2}\(\s*([A-Z]{1,3}\d{1,2}[a-z]?|[ivx]{1,4})\s*\)` (a
    labelled item, such as `*(A2) Determinism.*` or `(C1)`).
- **TABLE**: the pin line matches `^\s*\|`.
- **PARTIAL**: the site has a Phase-0 entry, and its `quote`, whitespace-normalized, differs from the
  whitespace-normalized pin line.

Sources: E-084. Controls: K5, K6, K7, K8, K9.

**R6.CTX.10** Indicator effects.

| Indicator | Effect |
|---|---|
| ANAPH | sets `meaning_context` true. An anaphoric line takes its referent from the line above, so a changed context changes what the line asserts. FAIL `context-meaning-unverified` until adjudicated |
| LIST | REVIEW_REQUIRED `context-structure-changed` when the site's context (R6.CTX.2) or its list context changed, unless adjudicated |
| TABLE | REVIEW_REQUIRED `context-structure-changed` when the site's context (R6.CTX.2) or its table context changed, unless adjudicated |
| PARTIAL | informational only: the site carries `partial_quote: true`. No effect on any outcome |

Sources: E-085. Controls: K5, K6, K7, K8, K9.

**R6.CTX.11** List and table context. **List context.** Walking up from the site over blank lines and
list-item lines (as LIST defines them), the first other non-blank line is the lead-in (`BOF` if none).
Walking down the same way, the first other non-blank line is the trailer (`EOF` if none). The siblings
are the non-blank item lines between them, other than the site. The list context is
`(lead-in, siblings, trailer)`, and its structure hash is the SHA-256 of its canonical JSON
(R6.OUT.19). **Table context.** The table block is the maximal run of lines matching `^\s*\|` that
contains the site. The table context is `(header, caption above, caption below)`: the block's first
line; the nearest non-blank line above the block (`BOF` if none); and the first non-blank line after
the block if it starts with `Table:` or `: `, else the empty string. Its structure hash is defined as
for lists.
Sources: E-086. Controls: K6, K7, K8.

**R6.CTX.12** For LIST and TABLE sites the neighbour context of R6.CTX.2 is kept in addition to the
structure contexts of R6.CTX.11: a change of either gives the result of R6.CTX.6.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1367. Controls: K7.

***

## 7. Outcomes, exit codes, precedence and result schema

**R6.OUT.1** Outcomes and exit codes.

| Outcome | Exit | Emitted when |
|---|---|---|
| PASS | 0 | every check holds and every control is green |
| REVIEW_REQUIRED | 10 | no FAIL item, at least one REVIEW item |
| FAIL | 20 | at least one FAIL item |
| USAGE | 64 | an argument error, `--help`, or a refused `--out` |
| ERROR | 65 | an integrity error (R6.OUT.5) |
| VOID | 70 | a preflight or self-test control failed; no verdict |
| INTERNAL | 71 | any exception caught by the tool's wrapper, recorded with its class and the failing stage |

ERROR, VOID, USAGE and INTERNAL are defined only here; sec. 15 lists the FAIL and REVIEW classes.
Sources: E-092, V1-071, V2-043, E-1079. Controls: X1, X2, X3, X4, X5, X6, X9.

**R6.OUT.2** Exit-code choice (R1). CPython exits 1 on an uncaught exception, including one raised
before the tool's wrapper is installed, and 2 when it cannot open the script; it exits 120 when
flushing standard streams fails at shutdown. None of the codes of R6.OUT.1 is one of these. The parser
overrides `ArgumentParser.error` and the `-h`/`--help` action so that both exit 64; exit 2 is therefore
excluded only for the parser's paths, and the interpreter can still return it.
Sources: E-093, RV-005. Controls: X3, X4, X5, X7, X8.

**R6.OUT.3** The wrapper. The entry point `tools/ledger_coverage.py` installs the wrapper before it
imports the tool's package, which it loads by location after the isolation check (R6.OUT.4). The
isolation check precedes every import of a module not already loaded at interpreter start (N-g). The
wrapper catches `BaseException` (including `SystemExit` raised by frozen code and `KeyboardInterrupt`)
and maps it to INTERNAL, exit 71, with a `result.json`. A failure before the wrapper is installed exits
with the interpreter's own code.
Sources: E-094. Controls: X2, X7, EI6.

**R6.OUT.4** Isolation refusal. The entry point refuses to run unless the interpreter runs in isolated
mode and no `sys.path` entry lies inside the checkout. The refusal happens before any import of a
module not loaded at interpreter start. It exits 65 and writes no `result.json`; it writes one line to
stderr, which is one JSON object naming the ERROR class `NOT_ISOLATED` and the reason (R6.REC.20). It is the second documented case
without a `result.json` (R6.OUT.6), and a run that ends this way is never acceptable. At the tool
commit the refusal writes a message with no class; that is a verification defect, corrected in a later
tool revision. The class name `NOT_ISOLATED` takes the state form of `MAIN_NOT_DESCENDANT` (RE-14); it
is a new identifier recorded in the migration index (sec. 34).
Sources: E-104, E-101, E-094. Controls: EI6.

**R6.OUT.5** Integrity errors and their classes. These produce ERROR, exit 65, with `stop.class`:

- `PIN_MISMATCH`, with the fields `expected_pin`, `record_digest`, `computed_digest` and `candidate`,
  produced before any frozen code runs;
- `RECORD_TREE_MISMATCH`, `SCIENTIFIC_BASE_MISMATCH`, `MAIN_NOT_DESCENDANT`;
- these classes, with `PIN_MISMATCH` and `EDITS_HASH_MISMATCH`, form the role "a pinned role or tree
  identity differs": ERROR with the named class (RE-17 (i));
- a ledger hash, span, overlap or base mismatch (`LEDGER_INTEGRITY`, or `SCIENTIFIC_BASE_MISMATCH` for a
  ledger base that is not `H`), an `edits_sha256` mismatch (`EDITS_HASH_MISMATCH`), and a broken
  segment chain;
- an encoding error, not UTF-8 or CR present (`ENCODING`);
- an unresolvable object, missing from the store or not hashing to its id (`UNRESOLVABLE`);
- the configuration and input classes, assigned by role:
  - `CONFIG_UNREVIEWED`: the configuration itself is not admitted from `F`'s pin table, or execution
    identity fails (for example a head branch that is not `main`);
  - `SOURCE_CHANGED`: an input that the admitted configuration pins (adapter, record, rule file,
    profile source) is missing or differs from its pin;
  - `CONFIG_INVALID`: the configuration is malformed or inconsistent; `CONFIG_UNSUPPORTED` and
    `CONFIG_INCONSISTENT` (including a record directory that is not admitted, reason
    "(directory not admitted)") as sec. 29 defines them;
  - a pinned input whose blob matches its pin but whose content fails its integrity rules: ERROR
    `LEDGER_INTEGRITY` for an unknown ledger schema id (R6.PIPE.15) and a failed edit-to-splice
    correspondence or selection (R6.PROF.8), otherwise the named integrity class; `SOURCE_CHANGED` is
    never raised for a blob that matches its pin (RE-16);
  - precedence: a malformed configuration is refused at admission first, as `CONFIG_UNREVIEWED`, in a
    chain-admitted run, and is `CONFIG_INVALID` in a control-harness run, where admission does not
    refuse it (RE-17 (ii)).

A record whose blob matches its pin but whose content fails its lint or its review is not an ERROR: it
is FAIL `record-invalid` (sec. 11), and so is a schema-invalid adjudication and a record passed with
`--classify` that the configuration does not reference. VOID carries `CONFIG_NO_CONTROLS` or
`PREFLIGHT_FAILED`. The class each integrity failure raises is confirmed by the conformance checks of
OD-4 and RD-18; a difference is a verification defect.
Sources: E-101, V1-081, V2-046. Controls: X1, M3, M4, M5, M9, M11, TT5, TT6, I2-3, I2-4, O6, Z1, Z5,
Z7, Z8.

**R6.OUT.6** USAGE. On an argument error, `--help` or a refused `--out`, nothing is written to `--out`
and `--out` is not created. One JSON object with the schema id, `outcome: "USAGE"`, `exit_status: 64`
and the parser message goes to stderr. Apart from the isolation refusal (R6.OUT.4), this is the only
case of R6.OUT.1 without a `result.json`. A run that ends with an interpreter code outside R6.OUT.1
writes none either, and is non-acceptance.
Sources: E-104, V1-082. Controls: X3, X4, X5, M10.

**R6.OUT.7** The `--out` guard and the write boundary. `--out` must not exist or must be empty, and
must not lie inside any worktree of the repository, checked with `git rev-parse --show-toplevel` from
the directory and by path prefix against every `git worktree list` entry; otherwise USAGE. The tool
writes only under `--out`: `result.json` (or, in a control harness, `control-result.json`, R6.OUT.12)
and, for op A, the replay materialization under `--out/replay/`. It writes no separate anchor file; the
anchor list's digest is `record_checks.anchors_sha256`. Every input is read from the object store. The
tool never writes a tracked file and never changes git state (sec. 24). This is to be confirmed by the
conformance check of OD-25; the property "no write outside `--out`, and the clone left clean" needs a
control of its own (RD-11).
Sources: V1-025, V1-026, V2-009. Controls: M10, X3, OUT-CONFINED.
**R6.OUT.8** VOID. If a preflight or self-test control fails, the run exits 70 without evaluating; no
verdict is given. The preflight set is stated in sec. 17.
Sources: V1-083. Controls: Z8.

**R6.OUT.9** Precedence. Evaluation order fixes precedence: USAGE, INTERNAL (at any stage), ERROR, VOID,
FAIL, REVIEW_REQUIRED, PASS. Only exit 0 with the acceptance predicate (R6.OUT.12) is acceptance.
Sources: E-102, V2-044. Controls: X6.

**R6.OUT.10** Any exit status not in R6.OUT.1 (for example 1, 2, 120, 126, 127 or a signal) is
non-acceptance, whatever `result.json` says. An exit status in R6.OUT.1 that disagrees with
`result.json` is non-acceptance.
Sources: E-100. Controls: X7, X8.

**R6.OUT.11** The exit status and `result.json` always agree. Consumers read `result.json`
(AGENTS.md sec. A.44), never stdout.
Sources: V1-073. Controls: X10.

**R6.OUT.12** Acceptance predicate. A consumer (a workflow step, the plan's checker or a reviewer)
accepts a run only if all of the following hold:

- the exit status is 0;
- `result.json` exists in `--out` and validates against schema `oi-ledger-coverage/5`;
- its `outcome` is PASS, and the independent outcome checker (R6.OUT.23) recomputes PASS from its
  `preflight`, `record_checks` and `items`;
- its recorded tool commit `T` and tool blobs equal the blobs the consumer reads itself at `T` from
  its own verified object store, and these equal the `tool` pins of the configuration at `F` (sec. 11);
  its adapter module blobs equal the configuration's pins; and its configuration
  `{path, blob_sha256}` equals the frozen one;
- `config.admission` is an object whose `mode` is `"chain"` and whose `snapshot` names the same `F`
  and the same pin table `{path, blob_sha256}` as the landing record.

The schema makes `config.admission` required. A result with a mode other than `"chain"`, or with a
top-level `"harness"` field, is never acceptable, whatever its outcome; a control harness writes
`control-result.json` with `"harness": true`, never `result.json`. Only exit 0 is acceptance, and no
flag converts REVIEW_REQUIRED to PASS.
Sources: E-095, E-099, V2-045. Controls: X10, X11, ACCEPT-SCHEMA, EI3.

**R6.OUT.13** Host-run re-verification. The result was produced in a host CI run that the consumer
verifies itself, by repeating execution identity (sec. 11):

- the host's REST API reports the run, by its run id, with `repository.id` and `head_repository.id`
  both equal to the configuration's `repository_id`, and with event `push` or `workflow_dispatch`;
- its `head_sha` is the `T` the result records, and `T`'s tree, read from the consumer's own verified
  store, holds the configuration's `tool.files` exactly and the pinned workflow blob at
  `tool.workflow.path`, which is the run's workflow path;
- the evaluated commits equal the landing record's;
- `T` is on the first-parent chain of `M`, resolved as sec. 23 states;
- the result file is that run's uploaded artifact, by sha256.

A result produced anywhere else, or by other code or another workflow, is never acceptable.
Sources: E-096. Controls: TR14, TR28-consumer, TR29, TR30, EI2-consumer.

**R6.OUT.14** Durable evidence (A-D5, C3, R-D5). Acceptance is recorded only by landing it on `main` in
a landing record, the result commit. The landing merges only with the owner's approval (AGENTS.md
sec. A.50 item 1), which the record quotes with author and time; the tool does not read or check that
quotation. The record commits:

- the result, compressed deterministically: `result.json.gz`, the gzip of the exact result bytes with
  a modification time of 0, no file name, compression level 9 and the operating-system field 255; the
  sha256 of the uncompressed bytes decides, and the compressed bytes' sha256 is recorded as well;
- the admission snapshot of sec. 11, and its sha256;
- the reproducibility recipe: the commits, including `F` and `T`; the configuration, pin table,
  engine, adapter and workflow blob hashes; the exact command; and the tool version.

CI run ids, job ids and log references are recorded as provenance only (AGENTS.md sec. A.42 item 2).
Committing a result preserves it; it never makes an invalid run acceptable. The predicate of
R6.OUT.12 is re-checked from the committed data before the landing merges.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-097. Controls: TR46.

**R6.OUT.15** Offline replay (C3, F2). `replay --snapshot <path> --out DIR` recomputes the result from
git objects and the committed snapshot alone. Admission is taken from the snapshot and written as
`"admission": {"mode": "replay", ...}`. For op C, every delegated and native class is decided from the
snapshot's delegated evidence (sec. 11). Replay does not call the host, clone the repository, build
PDFs or rerun any checker. It re-applies the tool's own verification rules of sec. 13 to the recorded
host records, hashes and checker outputs and to the git objects, for example: the TeX stamps and path
set; LEDGER.json against `H` plus its splices and the recorded census values; SC-42's committed file
against the recorded `--verbose` output; and the recorded `pdf` and `ci` records against `X`'s ids and
the artifact hash. Every recorded result file must hash to the sha256 recorded beside it. Apart from
the admission field, the replay's output equals the committed result byte for byte (canonical JSON,
R6.OUT.19), for op B and op D results as well as for op C results. A replay is never acceptable as a new
run. One thing remains host-attested and cannot be reproduced offline: that the snapshot was genuine
when it was taken.
Sources: E-098. Controls: TR45-opB.

**R6.OUT.16** Frozen code. Every call into frozen code in op A is wrapped. An exception becomes a
structured INTERNAL or ERROR with its class and message. The frozen `main()` is never called, so its
line-523 `TypeError` cannot be reached.
Sources: E-105. Controls: none.

**R6.OUT.17** Flags and REVIEW_REQUIRED (R7, V3). No flag converts REVIEW_REQUIRED to PASS, no warning
turns a failure into a pass, and no flag lowers the bar. A run of op B or op D names the plan check it
implements with `--check ID`; the configuration's `checks` table (sec. 25) gives each check its
profiles and its `final_profiles`. `--final` converts the REVIEW items of the selected check's
`final_profiles` to FAIL `final-unclassified`, and changes nothing else. `--final` without `--check`,
or with a check that has no `final_profiles`, is USAGE. The `final_profiles` are configuration content
(for A1: item 7 lists `ptr` and `count-grep`, and item 11 lists `repo`).
Sources: E-103, V1-084. Controls: X9, V23, V24, V25, V3-countercontrol.

**R6.OUT.18** Result schema `oi-ledger-coverage/5`. A result of another schema id is never acceptable.
The JSON Schema file `tools/ledger_coverage/engine/schemas/oi-ledger-coverage-5.schema.json` is the
machine form of this requirement and is covered by the correspondence check (sec. 16); it is extended
to list every field of the tables below that it does not list today. Any incompatible change to the
field list bumps the schema version. Basis: S = in the schema file at the tool commit; D = stated in a
source design and restated here; E = emitted at the tool commit and asserted by controls (RD-10);
N = restated as a named field pending the conformance check of RD-10.

Top-level fields:

| Field | Basis | Content |
|---|---|---|
| `schema` | S | the constant `oi-ledger-coverage/5` (required) |
| `outcome` | S | one of the outcomes of R6.OUT.1 (required) |
| `exit_status` | S | its exit code (required) |
| `operation` | S | the subcommand |
| `preflight` | S | list of `{id, passed}` (required) |
| `record_checks` | S, E | object or null (required); for op A: `holds`, `equalities` (the named replay equalities, R6.ANCH.3), `errors`, `frozen_self_test`, `ck_errors`, `extended_unmapped`, `pin_findings`, `anchors` (count) and `anchors_sha256` |
| `items` | S | list of items (required; below) |
| `class_meaning` | S | the constant table of R6.OUT.21 (required) |
| `engine` | S | `{blob_sha256, modules}` |
| `config` | S | `{config_id, version, path, commit, blob_sha256, admission}`; `admission` is an object with `mode` and `snapshot` (R6.OUT.12) |
| `adapters` | S | each adapter's module blob and the blob hash of every pinned input it reads (R6.OUT.25) |
| `profiles` | S | the profiles loaded, with their source blobs |
| `sites` | S | list of sites (below) |
| `hits` | S | list of hits (below) |
| `stop` | S | `{class, message, detail}` for ERROR, VOID and INTERNAL |
| `site_counts`, `finding_counts`, `hit_counts` | D | separate counts (R6.OUT.19) |
| `profiles_evaluated` | D | per evaluated tree, the profiles run on it (R6.PIPE.13) |
| `covered_paths` | D | exactly the paths the verdict covers |
| `file_conformance` | D | per segment and file: status and diagnostic ranges (R6.ANCH.9) |
| `inputs` | N | the inputs the run was given, as named fields: `operation`; `config` `{path, commit, blob_sha256}`; `freeze`; `pin`; `record` `{commit, tree}`; `commit` or `candidate`; `segments` `[{index, from, to, kind, ledger: {rev, path, sha256, edits_sha256_ok} or null}]`; `hp_records` and `classify_records` `[{rev, path, sha256}]`; `rule_files` `[{path, rev, blob_sha256, version}]`; `profiles` `[{name, source_blob, pattern_sha256}]`; `delegated_results` |
| `pins` | N | op C: `[{check_file, literal_sha256, target, base_present, c_present, resolution}]`, with `c_present` the literal's presence at the candidate `X` (R6.ANCH.19) |

The conformance check of RD-10 decides, for each member of `inputs` and `pins`, whether it is already
bound by another emitted field; the candidates at the tool commit are `operation`, `config`,
`segments`, `rule_files`, `profiles`, `records_used`, `roles`, `evaluated` and `invocation`. A member
found bound is stated as that field; any other member is emitted under its name here. No member is
withdrawn before that check.

Further top-level fields emitted at the tool commit, which no source design lists (RE-13). A field
that a control's expectation or the gate's extraction (R6.GATE.5, R6.GATE.8) reads is adopted as a
named field: `merger_groups`, `region_lines`, `side_changes` and `harness` (`harness` and `control` in a control harness only). The others are adopted as
declared diagnostics: emitted, listed in the schema file, never read for a verdict: `invocation`, `rule_files`, `hp_merges`, `records_used`, `per_edit`, `evaluated`, `segments`, `reports`, `added_text_lines`, `reconciliation_x_identity`, `delegation`, `record_directory`, `checks`, `landing_compositions`, `roles` and `control`. No field
is removed without a purpose trace (Q3). The members of `inputs` and `pins` that the conformance
check found not emitted are emitted in the tool revision (OBL-28, C-24).

Item fields: `obligation` (R6.OUT.24), `class`, `decision` (FAIL or REVIEW_REQUIRED), `subject`,
`segment` (string or null), `fingerprint` (64 hex), `resolution_needed` (object or null), and, where
applicable, `file`, `line`, `pre_existing` (R6.PIPE.8) and the explanation of R6.OUT.22.

Site fields: `site_id`, `anchor_sha256`, `state`, `current` (file, lines, sha256, or null), `pin_count`,
`ordinal`, `pin_context_sha256`, `current_context_sha256`, `context_required`, `meaning_context`,
`indicators` (`anaph`, `list`, `table`, `partial_quote`), `structure_context_sha256` (LIST and TABLE
sites), `provenance` (record id or null), `region_shared_with`, `hp_overlap`, `region_splices`,
`line_splices`, `context_changed`, `line_delta` (R6.ANCH.11), `splice_ids` with each splice's
`old_sha256` and `new_sha256`, `new_region_sha256` (R6.ANCH.13), `whitespace_only` (R6.ANCH.6) and
`pre_existing`.

Hit fields: `file`, `line`, `line_sha256`, `profiles`, `tree`, `state`, `segment`, `held_by` (the
tracked site that holds it, or null; sec. 14) and `pre_existing`.
Sources: E-106, V1-074, V1-078, V2-062, V2-063, V2-064, V2-065. Controls: ACCEPT-SCHEMA,
S7-schema-and-checker, B4-MEANING, U2, U9, U10.

**R6.OUT.19** Field rules.

- `site_counts`, `finding_counts` and `hit_counts` are separate.
- Items carry `file` and `line` where applicable, and are sorted by
  `(obligation, class, subject, segment, fingerprint)`.
- An item's fingerprint is the SHA-256 of canonical JSON (sorted keys, no whitespace, UTF-8, null as
  `null`) over fields that do not depend on any diagnostic algorithm, so that it is reproducible and
  can be matched by records. For `unauthorized-edit` those are the expected and actual file hashes and
  the segment; difflib ranges are diagnostics only.
- Every hit carries a `segment`, its profiles and the tree it was scanned in.
- No field records the repository head.
- The output is written with sorted keys, indent 1, `ensure_ascii` true and a final LF.
- An adjudication naming a segment outside the chain is reported as `out-of-scope`, which is not an
  item.

Sources: E-107, V1-076, V1-077, V2-063. Controls: S7-schema-and-checker.

**R6.OUT.20** Determinism. A result contains no timestamps, durations or host data other than the
execution identity that sec. 11 records, and every list is sorted. Two runs on the same inputs produce
byte-identical results (sec. 30).
Sources: V1-077, V2-067. Controls: REPRO-DOUBLE.
**R6.OUT.21** Class meanings (B-4). The schema carries a fixed table `class_meaning`, identical in every
result:

| Class identifier | Meaning |
|---|---|
| `authorized-replacement` | a site replaced by a splice of the frozen ledger |
| `authorized-removal` | a site removed by a splice of the frozen ledger |
| `unauthorized-edit` | a ledgered file whose bytes differ from `H` with the frozen ledger's splices applied |
| `unauthorized-change` | a change that no splice of the frozen ledger and no declared class specifies |

These identifiers are kept from v1 (AGENTS.md sec. A.48 item 3). They state nothing about owner
approval. The explanation of every item or site state in one of these classes quotes its meaning from
the table, and every human-readable text the tool writes (explanations, reasons, `resolution_needed`,
messages on stderr) uses the technical terms of this design ("specified by the frozen ledger",
"pinned", "recorded"), never approval vocabulary. That requirement on the tool's own strings is checked
in review.
Sources: E-108. Controls: B4-MEANING.

**R6.OUT.22** Explanation. Every subject (site, hit, file, pin and item) carries an explanation with:
the subject id and kind; the anchor and its hashes; the provenance chain (segment, splice ids, HP steps,
reconciliation id); the rule id and rule blob hash, or null; each matcher's result; the resulting
state; and, for REVIEW_REQUIRED, `resolution_needed`: the record kind and the fields a reviewer must
supply. The explanation is part of the JSON Schema.
Sources: E-109, V2-066. Controls: none.

**R6.OUT.23** Outcome function and independent checker (S7). The outcome is a pure function of
`preflight`, `record_checks` and `items`: VOID if a preflight control failed; otherwise FAIL if
`record_checks` is present and does not hold, or if any item's decision is FAIL; otherwise
REVIEW_REQUIRED if any item's decision is REVIEW_REQUIRED; otherwise PASS. Every output validates against the schema, and an independent checker of about 30
lines recomputes the outcome from the JSON; its result equals the tool's.
Sources: E-109, V1-075, V1-137, V2-067. Controls: S7-schema-and-checker.

**R6.OUT.24** Obligations. Every item carries exactly one obligation, from this set:

- `HP`: the historical-provenance obligation: changes and indicator items that occurred in `E..H`
  (sec. 5); `HP` items carry `segment: "E..H"`;
- `RET`: the retirement ledger segment `H..X`: changes to sites and ledgered files from `H` to `X`,
  including `untracked-hp-overlap`;
- `MAIN`: `M` and the landing: side changes on `M`, `base-drift` and the landing-composition classes
  (sec. 20, 23);
- `RECORD`: a record's own validity (`record-invalid`);
- `TERMS`: terminology subjects: profile hits and deny, literal and rule items (sec. 9, 10, 12);
- `DELEGATED`: delegated checks and their evidence (sec. 13).

Results group items by obligation. No `HP` item is counted under `RET`. These definitions are the tool commit's obligation set,
which OD-14 enumerates; each is adopted after a purpose trace (Q3) against its source, and a
difference the trace finds is a verification defect (RE-27 (a)).
Sources: V2-042. Controls: RT-H0, RT-T0, H5, RT-C.

**R6.OUT.25** Adapter inputs. The blob hash of every input an adapter reads (for A1, the Phase-0 and
Phase-2 record directories at the record commit) is recorded in the result's `adapters` list.
Sources: V1-020. Controls: none.

**R6.OUT.26** Tool identity. Each result names `T`, every tool blob and the engine hash, so that results
from a defective version are identifiable after a forward fix.
Sources: V1-143. Controls: TR48, X10.

**R6.OUT.27** Op A outcome. Op A is PASS only if `record_checks.holds` is true: every named replay
equality holds, there are no errors, the frozen self-test passes and `pin_findings` is empty. Otherwise
op A is FAIL, exit 20; a non-empty `pin_findings` gives FAIL `record-invalid` (R6.ANCH.8), pending the
check of what the code emits (RD-27).
Sources: V1-033. Controls: S11-2c, M7, M8.

**R6.OUT.28** Every hit is listed; nothing is truncated. This safeguard is preserved from v1 and is
confirmed at adoption (RD-15).
Sources: V1-067. Controls: none.

***

## 8. Sentence splitter, version 2

**R6.SPLIT.1** The sentence splitter is version 2, whose text is restated here verbatim from the
design v5.2 (`DESIGN-v5.2.md`, git blob e3edd9667d8801157c6d1074bb60d89dcd8ea458, lines 845 to 859).
In it, "O6" is a review-finding label (R6.NOTE.13), and "(sec. 14)" refers to v5.2's own section.

> **Sentence splitter, version 2 (versioned with the schema; O6).** A sentence ends at `.`, `?` or
> `!`, optionally followed by a run of closing `*` or `_`, and then by whitespace and an uppercase
> letter, a `*`, or end of paragraph. It does not end:
>
> - inside `$...$` or a backtick span;
> - after a word on the configuration's abbreviation list (A1: `sec.`, `Sec.`, `e.g.`, `i.e.`,
>   `cf.`, `Fig.`, `Eq.`, `Eqs.`, `No.`, `vs.`, `et al.`, `Ch.`, `App.`, `Thm.`, `Prop.`, `Lem.`);
> - after a single capital initial.
>
> A paragraph is a maximal run of non-blank lines, broken also before every list-item line (a line
> matching `^\s*(>\s*)*([-*+]|\d+[.)])\s+`). A sentence never crosses a paragraph boundary. Each
> line of a paragraph is stripped of leading and trailing whitespace, and the lines are joined with
> one space before splitting. Version 1 (v4) did neither: it let one "sentence" run across several
> bullets, and did not end a sentence at "...no more.** Every". Measured, version 2 changes no deny
> count at H or T1' at line or sentence level (sec. 14).

Sources: V2-049, RV-017. Controls: S11-57d, RT-DR3W.

**R6.SPLIT.2** Normative scope of the restated text. Its first two paragraphs and the first three
sentences of its last paragraph are normative. The last two sentences (the comparison with version 1
and the measurement at `H` and `T1'`) are history and a measurement, not requirements (sec. 31). The
abbreviation list is configuration content; the A1 list is the one quoted. The splitter is versioned
with the result schema: a change to the splitting rule is a new splitter version and an incompatible
schema change (R6.OUT.18). The rule has no "line boundary" condition; paragraph boundaries replace it.
Sources: V2-049, RV-017. Controls: none (scope of R6.SPLIT.1).

**R6.SPLIT.3** Conformance. Before r6 is final, the splitter of R6.SPLIT.1 is checked, by reading only,
against the implementation at the tool commit (`tools/ledger_coverage/engine/util.py`,
`sentences_of`, version 2) (OD-23). Each difference becomes an owner decision or a verification
defect; the implementation is not adopted by default (R6.STAT.5).
The check found these readings of the tool commit, which r6 states as part of the splitter
because splitting must equal P's checker (ME-1; RE-32 (a)): "uppercase" means ASCII uppercase only;
an abbreviation matches when the text before the full stop ends with a listed abbreviation, with
no word boundary (so "parsec." matches "sec."); `$$` display math is not masked; and a
`splitter_version` other than 2 is refused, as ERROR `CONFIG_INVALID` once the configuration lint
checks it (OBL-28, C-14; INTERNAL at the tool commit). Any change to these readings is verified
against P's checker under ME-1.
Sources: V2-049, RV-017. Controls: none (conformance check, OD-23).

***

## Requirements of sections 0 to 8 with no control

Statements that no control can test (status, definitions, purpose, non-goals, scope, limits,
traceability): R6.STAT.1 to R6.STAT.9, R6.NOTE.1 to R6.NOTE.8, R6.NOTE.11 to R6.NOTE.13, R6.PUR.1,
R6.PUR.2, R6.PUR.5, R6.PUR.6, R6.PUR.7, R6.PUR.10, R6.PIPE.12, R6.CTX.1 and R6.SPLIT.2. The requirement list gives each its kind and its verification (review, or the OBL ids that carry it); the correspondence check exempts them from naming a control (R6.GATE.12; RE-11 (a)).

Testable requirements with no control in the expectation file; each needs a control row before r6 is final, and each is a named blocker on the correspondence check (rows added by r6 for R6.PUR.12, R6.ANCH.10, R6.ANCH.12, R6.ANCH.15, R6.HP.7, R6.OUT.7 and R6.OUT.20 are named in those requirements):

- R6.PIPE.1 (stage order), R6.PIPE.4 (`--repo`), R6.PIPE.6 (segment chain and default segment),
  R6.PIPE.7 (state carried across segments), R6.PIPE.8 (prior endpoint), R6.PIPE.15 (only partly: CLASS-RETAINED tests `retained-changed`; `ignored_fields` and the unknown schema id have no control);
- R6.ANCH.8 (override anchors; RD-27);
- R6.HP.1 (merge cross-check), R6.HP.5 (presence of `semantic_classification`), R6.HP.14 (supply of HP records);
- R6.CTX.8 (indicator change is widening);
- R6.OUT.16 (frozen-code wrapping), R6.OUT.22 (explanation),
  R6.OUT.25 (adapter input hashes), R6.OUT.28 (no truncation; RD-15);
- R6.SPLIT.3 (conformance check, OD-23; a reading check, not a control).

Requirements whose controls cover only part of the statement: R6.OUT.4 (EI6 does not assert the
named class), R6.OUT.9 (no control plants
two outcomes at once), R6.SPLIT.1 (no control for the abbreviation, initial and backtick cases).

***

## 9. Scan profiles

Conventions of these sections. "sec. N" names a section of r6. Exit codes are those of sec. 7: PASS 0,
REVIEW_REQUIRED 10, FAIL 20, USAGE 64, ERROR 65, VOID 70, INTERNAL 71. A control id marked "(new row)" is a row r6 adds to the expectation file; no runner implements it yet. "(row restored)" marks U14, a live row of the expectation file (RD-9 (a)). "OBL-<n>" names the outstanding obligation of sec. 32 that carries the transferred item; it is a named blocker on the execution it gates and is not discharged by r6.

### 9.1 Extraction and sources

**R6.PROF.1** A scan profile is a named set of patterns. Profiles are extracted from their source
blobs by `ast` or JSON through the named extractors of sec. 25 (for example `python-ast-assign` and
`python-ast-call-arg`), never retyped. The one exception is the patterns of rule records (sec. 10,
sec. 12), which live in reviewed rule files. Each profile records its source blob id and the
SHA-256 of its extracted patterns, and `result.json` lists the profiles evaluated on each tree.
Sources: E-112, V2-022, V1-064. Controls: S11-56, RT-E, RT-DR.

**R6.PROF.2** A profile source is a pinned input of the admitted configuration. A source that is
missing, or whose blob differs from its pin, is ERROR `SOURCE_CHANGED` (exit 65) under the role rule
of R6.REC.5. A changed source enters a run only through a configuration that pins the new blob and
whose review covers it (sec. 25).
Sources: V2-025. Controls: Y10.

### 9.2 Review profiles

**R6.PROF.3** A hit of a review profile is REVIEW_REQUIRED unless it is held by a tracked site
(R6.HIT.1) or classified by a record or an allow rule (sec. 14). Each review profile declares
`applies_to`: `tree` (every line of every in-scope file of the evaluated tree) or `added-text` (the
splice images of a ledgered segment; in op D only with `--base` and `--ledger`). The profile
mechanism is the tool requirement; the list of profiles is configuration content (sec. 25, sec. 27).
The A1 configuration's review profiles are: `p0-core` and `p0-para` (Phase-0 `sites.json`, by JSON);
`ledger-ext` (`EXTENDED_PATTERNS` in `R/ledger_check.py` at the record commit, by `ast`); `ptr` (`PTR`
in P's `edits_check.py`); `repo` (`REPO_PAT` in P's `edits_check.py`, scope "active files", sec. 18
item 11); `count-grep` (the literal list of sec. 18 item 7: "Fourteen", "six structural", "sixth
of"), all with `applies_to: tree`; and `resid` (a rule record of the plan, sec. 12), with
`applies_to: added-text`.
Sources: E-113, V2-023, V2-024. Controls: U12, V7b, V15, V21, V26, RT-D.

### 9.3 Deny profiles

**R6.PROF.4** A match of a deny profile is FAIL `deny-match`. A deny profile is evaluated on every
line and on every sentence (splitter version 2, sec. 8) of every in-scope file of every tree on which
deny profiles run, not only on hits of other profiles. Deny profiles run on every tree an operation
evaluates except `E` and `H`, the retired-form trees named in the configuration (`roles.pin` and
`roles.scientific_base`); in op D they run on the named commit, whatever it is (sec. 3). A deny
matcher is a reviewed regular expression or two-part sentence test with the scope its rule record
states (sec. 10); the production scope is configuration content (sec. 27). The A1 configuration's deny
profiles are: the deny rules of the plan's rule record (sec. 12); `register` and `register-caps`
(`REG`, and `CAPS` less `CAPS_OK`, from P's `edits_check.py`); and `infinity` (`INF` less the
`NEUTRAL` disclaimer, from P's `edits_check.py`). `register`, `register-caps` and `infinity` apply to
added text only, by the per-edit unit of sec. 9.4.
Sources: E-114, RV-048. Controls: RT-E, RT-DR, V1, Y3, S11-5, S11-6.

### 9.4 The per-edit unit of `register`, `register-caps` and `infinity`

**R6.PROF.5** These profiles implement items 5 and 6 of P's plan per edit and per step of the edit
list, not per splice, as P's frozen checker defines them: P's `edits_check.py` (the blob the
configuration pins), function `static_new`, with `inf_key` and `sentences`. No approximation is
admitted. **Unit.** For every entry `e` of the edit list frozen at `F` (`edits.json`, read through the
ledger adapter's companion and bound by `edits_sha256`), the pairs evaluated are `(e.old, e.new)` and,
if `e` has them, `(e.old_step2, e.new_step2)`. Each pair is evaluated separately, as P's `static_new`
does, whichever of them P applies. Edits that the ledger lists as retained (A1: D032, D039) are
evaluated as P does (`old` against `new`). **What `old_step2` is.** `(old_step2, new_step2)` is not a
second edit applied after the first. It is an alternative version of the same edit, for a later state
of the file. P's `variant(e, text)` takes the candidates `(old, new)` and then `(old_step2,
new_step2)`, and selects the first whose `old` text occurs exactly once in `text`; if neither does, it
selects none. P's `check` and `apply_edits` apply only the selected pair.
Sources: E-116. Controls: S11-56, S11-57a, S11-57b, S11-58a-f.

**R6.PROF.6** **`register`** (REG): a FAIL for each lowercased REG token in `new` that is not among
the lowercased REG tokens of `old` (set difference per pair). **`register-caps`** (CAPS less
CAPS_OK): a FAIL for each CAPS token in `new` that is not in `old` and not in CAPS_OK, only when the
edit's own `kind` is one of the kinds named in the rule file `register-infinity-params` (A1: `ptr`,
`consistency`, `handoff`).
Sources: E-117. Controls: S11-56, S11-57a, S11-57b, S11-5.

**R6.PROF.7** **`infinity`** (INF less NEUTRAL): each of `new` and `old` is split by P's splitter,
`re.split(r'(?<=[.;:?])\s+', text)`: a sentence ends after `.`, `;`, `:` or `?` followed by whitespace.
This is not splitter version 2 (sec. 8), which does not split at `;` or `:` and so would change which
NEUTRAL spans exempt a match. In each sentence, every INF match not contained in a NEUTRAL span is an
assertion. `old` is first rewritten as P rewrites it (A1: `\bA1\b(?: \(finiteness\))?` becomes
"finiteness"). Each assertion is normalized to a key as P's `inf_key` does (lowercase; runs of
whitespace, `*` and `_` collapsed to one space; a key matching `finiteness\b.*\bfails` becomes
"finiteness fails"). A FAIL is emitted for each assertion of `new` whose key count in `new` exceeds
its count in the rewritten `old` (multiset difference, in P's order).
Sources: E-118. Controls: S11-57d, S11-6, S11-56.

**R6.PROF.8** **Both units, fail-closed.** The per-splice evaluation (each splice's image against the
`H` bytes it replaces, by the same rules) also runs, and a FAIL from either unit is a FAIL. The
integrity stage checks that the splices are exactly P's application of the edit list at `H`,
selecting as P selects:
- **Counting.** "Occurs exactly once" means P's count: non-overlapping occurrences found left to
  right (Python `str.count` on the file's text decoded as UTF-8). Under this count, `old = "aa"`
  occurs once in `"xaaay"` and is selected, as P selects it.
- **Uniqueness at `H`.** P's selection is applied to the file's text at `H` for every edit, in
  edit-list order, retained edits included. It must select a pair. If neither `old` nor `old_step2`
  occurs exactly once, the tool refuses with ERROR `LEDGER_INTEGRITY`, naming the edit and both counts.
- **Application in order.** The edits are applied in edit-list order to a running copy of each file,
  as P's `check` and `apply_edits` do. Each edit selects its pair against the running copy by the same
  rule and replaces the first occurrence of the selected `old` (Python `str.replace` with count 1).
  If no pair is selected at that point, the edit is lost and the tool refuses.
- **Offsets back to `H`.** The running copy is an ordered list of segments, each either a run of
  `H`'s original text carrying its start offset in `H`, or an image an earlier edit inserted. The
  occurrence an edit replaces, `[p, p + len(old))` in the running copy, must lie entirely inside one
  original-text segment; its `H` span is that segment's `H` start plus `p` minus the segment's start
  in the running copy. Character offsets are converted to byte offsets by the UTF-8 length of the `H`
  text before them. The segment is split around the occurrence and the image is inserted as a new
  segment.
- **Binding to the splices.** For each applied edit, the `H` byte span equals its splice's `start` and
  `end`; the splice's replaced bytes equal the selected `old`, and its image the selected `new`. A
  retained edit has `old` equal to `new` and no splice. Every splice belongs to exactly one applied
  edit.
- Any other relation is ERROR `LEDGER_INTEGRITY`, with the edit and splice ids (RE-16).

Sources: E-119, E-120. Controls: S11-57c, S11-58a-f, S11-58g, S11-58h, S11-58i, S11-58j, S11-58k.

**R6.PROF.9** **Where the tool is stricter than P.** The tool computes and records P's per-edit
result for items 5 and 6 in every case, including a refusal, so no item-5 or item-6 verdict differs
from P's. It refuses three kinds of input that P, which has no splices, would not refuse, each because
it is an invalid or ambiguous input: (i) a splice for the variant P does not select (the frozen ledger
then misrepresents the frozen edit list); (ii) one splice covering two edits (the ledger schema gives
each splice exactly one edit `id`), even where its bytes equal P's combined application; (iii) chained
edits: a later edit's selected occurrence lies wholly or partly inside an image an earlier edit
inserted, or spans the point where an earlier edit's image, possibly empty, was inserted, so that in
the segment model it crosses more than one segment. No set of disjoint splices at `H` can express such
an application, and a frozen plan containing one is invalid.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-121. Controls: S11-58g, S11-57c, S11-58j, S11-58k.

**R6.PROF.10** **Extraction of P's literals.** REG, CAPS, CAPS_OK, INF and NEUTRAL are extracted from
P's pinned blob by `python-ast-assign`. P's sentence regex is extracted from the `sentences` function
by `python-ast-call-arg`, and its `pattern_sha256` is recorded. The edit kinds, the key rule and the
rewrite are not extractable assignments; they live in the reviewed rule file
`register-infinity-params` (a record under sec. 11), with positive and negative examples, and a lint
that each equals the corresponding literal in P's `static_new` and `inf_key` source. A failed lint is
FAIL `record-invalid`.
Sources: E-123. Controls: S11-56, PROF-PARAMS-LINT (new row).

**R6.PROF.11** The landing record lists every line-level match of `register`, `register-caps` and
`infinity` in the splice images of `X`, each with the `old` match that cancels it.
The matches are taken from the splice images of the candidate `X`, never from `T1'`, which is
not reachable from `main` (RE-35).
Sources: E-126. Controls: PROF-LANDING-LIST (new row).

**R6.PROF.12** The equality of these semantics with P's `static_new`, and of the tool's selection,
counting and splitting with P's, is verified at `F` against P's checker as frozen with the plan. It is
an outstanding obligation of the plan amendment, together with the parity measurements, and is not
established by r6.
Sources: E-119. Controls: none (OBL-1, OBL-2).
***

## 10. Rule schema, rule lint, fingerprints, residual testing

### 10.1 Rule files

**R6.RULE.1** A rule file has the schema `oi-term-rules/2`. It is an immutable record under the
ownership chain of sec. 11: a change is a new file, which carries `supersedes: {path, blob_sha256}`
and the same `record_id`. A revision is identified by its blob and its `supersedes` chain; the schema
has no version field. Each rule carries `kind`: `allow` (a verified false positive) or `deny` (a
retired or prohibited claim).
Sources: E-127, V2-047. Controls: A7r, LN1, LN2, O7.

**R6.RULE.2** **Allow rule.** Its fields: `id` (never reused); `profiles` it addresses;
`scope.files`, exact paths, mirrors named explicitly; `matcher.literal`, which must contain the
trigger, defined as the profile match span of each fingerprinted sentence at `recorded_at`;
`matcher.context`, required co-occurring literals in the sentence or its neighbouring sentences (for
example the enumerated list); `matcher.negative`, literals or regexes that must not match;
`context_required`; `max_instances`, equal to the number of fingerprints; `fingerprints`, each
`{file, sentence_sha256, context_sha256, negative_allowance}`, where the optional `negative_allowance`
maps a negative literal to the number of its matches in that exact fingerprinted sentence;
`recorded_at`, the commit at which the fingerprints were taken; `positive_examples` and
`negative_examples`, at least one of each, which become controls; `reason`, the semantic reason in one
or two sentences; `author`. The reviewer and the review are a separate review record bound by blob
(sec. 11). Owner approval is procedural and is not a rule field (R6.REC.3).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-128, V2-048, RV-015. Controls: A6r, A8r, A7r, E-A6r, E-A8r, lint-ok.

**R6.RULE.3** **Deny rule.** Its fields: `id`; `pattern`, a reviewed regex, or a two-part sentence
test (a count part and a tail, both of which must match the sentence); `scope`, `all-corpus` or exact
paths; the evaluation units (line, sentence, or both) on which it runs; `positive_examples`, at least
one, which the rule must match; `negative_examples`, at least one, which the rule must not match;
`countercontrol`, a real line or sentence at a named commit that the rule matches, in a scanned file
or in a control-only input named by the controls file (no constructed text serves as a deny rule's
countercontrol); `reason`; `author`. Fingerprints and `max_instances` do not apply to deny rules, and
corpus-wide scope is allowed for them.
Sources: E-129, RV-016. Controls: A10r, A11r, RT-DR3W, RT-DR.

### 10.2 Applying an allow rule

**R6.RULE.4** For a hit, the steps run in this order:
1. If no allow rule has the hit's file in scope, with a literal covering the trigger and a context
   matcher that holds, the hit stays REVIEW_REQUIRED `unclassified`.
2. If any deny profile matches the sentence, the result is FAIL `deny-match`. Deny takes precedence.
3. The rule's negative matcher is applied to the whole sentence, with every negative literal counted.
   The allowance for the sentence is the `negative_allowance` of a fingerprint only if all of the
   following hold, and is zero otherwise: the hit's file is the fingerprint's `file`; the sentence's
   sha256 equals the fingerprint's `sentence_sha256`; the context sha256 equals the fingerprint's
   `context_sha256`, whether or not the rule sets `context_required`; and that fingerprint has not
   already granted its allowance to another sentence in this tree. If, for any negative literal, the
   sentence has more matches than the allowance grants, the result is FAIL `rule-negative-match`. The
   allowance is bound to one fingerprint, that is, one fingerprinted sentence at one fingerprinted
   location; it is never a global count and cannot be used by any other sentence, file or location.
4. If the sentence or, when required, the context differs from every fingerprint, the result is
   REVIEW_REQUIRED `rule-fingerprint-mismatch`.
5. If the rule has already been applied `max_instances` times in the tree, the result is FAIL
   `rule-overreach`.
6. Otherwise the hit is classified by the rule.

A fingerprint with no `negative_allowance` grants none. A literal's matches are counted as
non-overlapping matches of the literal (or regex) in the sentence's source bytes. The explanation of
the hit records each step with its result (sec. 7).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-130, V2-050, V2-052. Controls: L1, L2, L3, L4, S1r, V7a, V7c, A5r, A5r-generic, E-L1, E-L3,
E-S1r, rule-negative, WB1, WB4, WB6, WB7.

**R6.RULE.5** **The fingerprint's context and location.** The sentence list of a file is every
sentence of every paragraph, in file order, under splitter version 2 (sec. 8); neighbours may lie in
adjacent paragraphs. For the sentence at index `k`, `prev` is the sentence at `k-1`, or the four bytes
`BOF` if `k` is the first; `next` is the sentence at `k+1`, or `EOF` if `k` is the last. Each sentence
is taken as the splitter yields it and encoded as UTF-8. `context_sha256 = sha256(prev || 0x00 ||
next)`. "Location" in step 3 means exactly this pair of neighbours in the named file, not a line
number or byte offset: a shift of the whole region keeps the allowance, and so does a move of the
sentence together with both of its neighbours to another part of the same file; a move of the
sentence without both neighbours changes the context and loses the allowance.
Sources: E-131. Controls: WB8, WB13, WB5, WB3.

**R6.RULE.6** **One grant, deterministically.** When several sentences in one file satisfy the
conditions of step 3 for the same fingerprint (identical text with identical neighbours), the grant
goes to the one with the smallest byte offset in the file; every later one gets no allowance. A
sentence's byte offset is the byte offset, in the file as committed, of the first byte of its first
non-whitespace character.
Sources: E-132. Controls: WB14, WB9.

**R6.RULE.7** **Case.** Literal entries of an allow rule's negative matcher are matched
case-insensitively, for every allow rule; a regex entry keeps its own flags. Allowances count
case-insensitive matches. **Matching on source bytes.** Every literal of an allow or deny rule
(trigger, context, negative, fingerprinted sentence) is matched against the source bytes of the file
as committed, after the splitter's whitespace normalization (sec. 8), never against rendered text
(for example a context literal `\mathrm{SU}(3)`, as the source line holds it, not "SU(3)").
Sources: E-133. Controls: WB15, L2, V7a.

**R6.RULE.8** **`rule-stale` scoping.** REVIEW_REQUIRED `rule-stale` (a fingerprinted sentence no
longer present) is evaluated on every tree except those that are proper ancestors of the rule's
`recorded_at`, computed from parsed parents (R6.REC.17). A candidate `X`, `C`, `L` or `M`, and
`recorded_at` itself, are always evaluated. `result.json` lists, per tree, the rules not evaluated for
staleness and why. At `recorded_at` a missing fingerprint is a lint failure of the rule (R6.RULE.10),
not a `rule-stale` item.
Sources: E-134, V2-028. Controls: S2r, WB5, E-S2r, GV3.

**R6.RULE.9** **Residual testing.** No rule ever deletes text from the line or sentence before
testing. A classified hit's sentence is tested whole, with the classified literal in place: every
deny profile (step 2) and the rule's negative matcher (step 3) are applied to the whole sentence, and
every other profile's hits in it are decided on their own.
Sources: E-134, V2-051. Controls: V7a, WB2, WB12, A5r.

### 10.3 Rule lint

**R6.RULE.10** The rule lint fails a rule file, with FAIL `record-invalid` (exit 20) for the rule
file, on any of these: a path prefix, glob or missing scope in an allow rule; a literal that does not
contain the trigger (the profile match span of each fingerprinted sentence at `recorded_at`);
`max_instances` different from the fingerprint count; a duplicate or reused rule id; a `supersedes`
hash mismatch, or any failure of the lineage rule of R6.REC.7; a fingerprint not reproduced by a
sentence of its named file at `recorded_at`; a missing field; any failure of the example and
fingerprint lint of R6.REC.14; and an unreviewed widening (R6.REC.13).
Sources: V2-053, V2-057, RV-054, V2-028. Controls: A1r, A6r, A7r, A3r, A11r, E-A6r, E-A1r, E-A3r.

**R6.RULE.11** **Minimum literal.** An allow rule whose `matcher.literal` is shorter than 8
characters fails the lint (FAIL `record-invalid`), whether or not it contains the trigger. The
implementation does not enforce this today; that is a verification defect, corrected in the tool
revision.
Sources: V2-054. Controls: A2r, RULE-MINLIT (new row).

**R6.RULE.12** **No unbounded allowance.** An allow rule with zero fingerprints fails the lint (FAIL
`record-invalid`), even where `max_instances` equals the fingerprint count. Deny rules carry no
fingerprints and are not subject to this check. The implementation does not enforce this today; that
is a verification defect, corrected in the tool revision.
Sources: V2-055. Controls: RULE-ZEROFP (new row).

**R6.RULE.13** **Scope records and widening.** A hit outside every rule's scope is resolved only by
an exact-path, fingerprinted rule or record. A profile's scope (the files a profile is evaluated on)
is a reviewed scope record; prefix lists are allowed only there. Widening of allow and deny rules is
defined in R6.REC.13. For a scope record, adding a scope path to a deny profile is not widening; any
other change to a scope record is widening, and needs a widening review (R6.REC.13).
Sources: E-1065, V2-058, RV-053. Controls: A1r, A10r, A3r, Z10.

***

## 11. Records, review records, record lint, admission, execution identity, object integrity

### 11.1 Records and the ownership chain

**R6.REC.1** The chain below applies to every reviewed record kind: HP adjudications, context
adjudications, hit classifications, allow and deny rule files, scope records, side-change class
records, reconciliation records, PIN_OK entries outside `F`'s pin table, and the configuration itself.
One record is one immutable file in the audit directory of sec. 19, or in the amended plan's record
directory (sec. 21) for records frozen with the plan. Every record is read from the git object store
by its full verified object id (R6.REC.17); the working tree is never read. The tool never writes a
record.
Sources: E-135, V1-063, V1-016, RV-019. Controls: LN1, S4a, O9.

**R6.REC.2** **Writer (author).** The writer prepares the record and its evidence: the exact git
object ids, the subject's `line_sha256` or region hashes, the tool's REVIEW-mode explanation for that
subject, and the semantic statement (which qualification is visible, and why). The evidence may
include tool output, but the record states its classification in its own words. Its `author` field
names the writer. A writer may not review a record they wrote. **Independent reviewer.** A non-author
re-derives each record from the git object store, not from the writer's output: for an HP record,
recomputing the walk, checking each step's commit and hashes, and reading the pre and post text; for
a classification or context record, reading the sentence and its context at the stated tree and
judging the semantic statement. The reviewer writes a separate immutable review record, schema
`oi-review-record/1`, with `reviewer`; `reviewed`, the `{path, blob_sha256}` of exactly one record;
`method`, how each item was re-derived, naming the object ids read; `verdicts`, one entry per item id
of the reviewed record (`accept`, `reject` or `dissent`, with the reason); and `dissent`, if any. A
review that cites only a passing tool run is invalid.
Sources: E-136, V2-056, RV-019. Controls: O1, O2, O3, O5, O7, I2-5.

**R6.REC.3** **Owner approval (procedural).** The ownership chain the tool checks is the writer, the
independent reviewer and the frozen configuration's reference at `F`. The owner's approval of a
record, of the configuration, of `F` and of a landing is given under AGENTS.md (sec. A.45 rule 3,
A.50, A.51) and quoted with author and time in the record that relies on it (sec. A.42 item 7). The
tool neither reads nor checks it, and no record kind, field, comment or host read represents it.
Sources: E-137, V2-056. Controls: O9.

**R6.REC.4** **Frozen configuration.** The configuration at `F` references every record and review
record by `{path, blob_sha256}` (sec. 25). A record added after `F` is admissible only under the
reconciliation rule of sec. 23: it is valid only for a side change on `M`, and it never changes a
decision of op C on `X`.
Sources: E-138, E-165. Controls: O8, N2, O9.

### 11.2 Error classes by role

**R6.REC.5** A failing input is classified by its role, as follows. A conformance check of what the
code raises precedes adoption; each difference found is a verification defect.
- **The configuration not admitted** from `F`'s pin table (any failure of R6.REC.10 to R6.REC.11),
  including a configuration blob that is missing, differs, fails schema or lacks review: ERROR
  `CONFIG_UNREVIEWED`.
- **Execution identity** not holding (R6.REC.15, R6.REC.16), including a run record that cannot be
  read and a `head_branch` other than `main`: ERROR `CONFIG_UNREVIEWED`.
- **A pinned input missing or differing from its pin**: any input the admitted configuration pins
  (adapter, record, rule file, profile source, delegation contract, `edits.json`, `ledger.json`),
  absent at `F` at its path or with a blob whose hash differs: ERROR `SOURCE_CHANGED`.
- **A pinned input whose content fails its integrity rules**: ERROR with the class the integrity
  stage names (for example `LEDGER_INTEGRITY` and `SCIENTIFIC_BASE_MISMATCH`, and `LEDGER_INTEGRITY`
  for an unknown ledger schema id or a failed edit/splice correspondence, R6.PROF.8; RE-16).
- **A pinned role or tree identity that differs** (`PIN_MISMATCH`, `RECORD_TREE_MISMATCH`,
  `SCIENTIFIC_BASE_MISMATCH`, `MAIN_NOT_DESCENDANT`, `EDITS_HASH_MISMATCH`): ERROR with the named class
  (RE-17 (i)). A malformed configuration is refused at admission first (`CONFIG_UNREVIEWED`) in a
  chain-admitted run and is `CONFIG_INVALID` in a control-harness run (RE-17 (ii)).
- **The configuration malformed or inconsistent**: ERROR `CONFIG_INVALID`, or `CONFIG_INCONSISTENT`
  for the consistency checks of sec. 29.
- **A record whose blob matches its pin but whose content fails its lint or its review**, and a
  record supplied to the run (for example by `--classify`) that the configuration at `F` does not
  reference: FAIL `record-invalid` (exit 20). An unreferenced record is never used.

Sources: E-139, E-140, A-116. Controls: TR2, TR3, CHAIN-REFUSAL, ADM-CONFIG-AT-F, EI2, TR29-tool, O6,
I2-3, Y10, M3, M4, M5, Z1, Z11, I2-4, I2-5, GV6.

### 11.3 Record lint

**R6.REC.6** A record fails, with FAIL `record-invalid`, on any of these: a schema or field error, or
a missing field; no review record naming exactly this record's blob, or a review record naming another
blob; `reviewer` equal to `author`; a review whose `verdicts` do not cover every item id of the record,
or any item not `accept`; a duplicated item id or verdict; a `reviewer` value that points to a tool
run, a CI run, a check run or an Issue (a URL or run id rather than a person); a record entry at a
path that is not a regular file (R6.REC.17); a record not read from the git object store.
Sources: E-140, E-141. Controls: O1, O2, O3, O5, R3-F2, R4-B3, R4-B3-DUP, R5-N6, GV6.

**R6.REC.7** **Supersession and lineage**, for every record kind that carries `supersedes`. Each
`supersedes` names a `{path, blob_sha256}` that exists in the object store at or before `F` and is a
record of the same kind, schema and lineage; a first record has `supersedes: null`. A record's lineage
is its `record_id`, a non-empty string at the record's top level; for the configuration it is its
`config_id` (sec. 25). `record_id` is immutable within a lineage: a superseding record has the same
kind, schema and `record_id` as the record it names. Sharing a `record_id` within one lineage is not
reuse; a `record_id` carried by two records that do not lie on one `supersedes` chain is. Each of the
following is FAIL `record-invalid`:
- a chain naming an id or blob that never existed as a record (for example an off-repository draft);
- a record without a valid `record_id` (missing, empty or not a string) that supersedes another
  record or is named by a `supersedes`;
- a `supersedes` naming a record whose kind, schema or `record_id` differs, at any step of the chain;
- a `supersedes` naming a predecessor that does not itself pass this lint, read from the object store
  at or before `F` and verified independently of the superseding record (its own review and, where it
  widens the record it supersedes, its widening review);
- a cycle in a `supersedes` chain;
- ambiguous ancestry: two records superseding the same predecessor, among the records in the audit
  directory and the plan's record directory at `F` and the records the run reads; or a lineage with
  two heads used in one run, a head being a record of the lineage that no other record the run reads
  (the records the configuration references and every record their chains name) supersedes;
- a reused `record_id`.

Sources: E-141. Controls: S4a, LN1, LN2, LN3, LN4, LN5, LN6, LN7, LN8, LN10, R6-G6.

**R6.REC.8** **`record_id` outside lineage.** Beyond the lineage rule, `record_id` is required on the
item-2 records of sec. 22 when their item list is empty: such a record carries its `record_id`, and its
review, which the review chain binds to that `record_id` when the item list is empty, states that the
list is empty and why. A record that neither supersedes nor is superseded, and is not such an empty
item-2 record, is not required to carry `record_id`.
Sources: A-118. Controls: I2-6, LN3, LN10.

**R6.REC.9** **Item-2 records.** The context-adjudication and hit-classification records of sec. 22
reach the run exactly as every other record does: each lies in the plan's record directory, is
referenced by the configuration's `records` with its blob sha256, and has a non-author review record
under this chain. A file absent at `F` stops the run with ERROR `SOURCE_CHANGED`; a record not
referenced by the configuration is never used (`record-invalid`).
Sources: A-115, A-116. Controls: I2-3, I2-4, I2-5, I2-6.

**R6.REC.10** **Orphan and duplicate records.** Record lint checks every entry of an HP adjudication, a context
adjudication or a hit classification record on each tree and in each segment to which the record
applies, and on no other tree or segment. An entry that, there, names no subject of the run (a
`site_id` that no tracked site carries, or a `{file, line_sha256}`, with its context hashes for a
context adjudication, that matches no line of that tree) resolves nothing and is itself reported:
an HP adjudication entry as FAIL `stale-adjudication` (obligation `HP`), with v1's meaning of that
class (v1 4.6; Q12), and an entry of a context adjudication or hit classification record as FAIL
`record-invalid` (RD-9 (a)); each item names the record and the entry. Two entries that name the same
subject, in one record or in two records of the same kind, are duplicates: FAIL `record-invalid`
naming both, and neither entry is applied (RE-8). An entry that names an existing subject but
disagrees with it is decided by the subject's own rule (for example `provenance-mismatch`,
`provenance-gap`, `adjudication-row-changed`), not by this rule. An entry naming a segment outside the
chain is reported as `out-of-scope` (sec. 7), which is not a finding. Resolution is only by exact
match: a record entry resolves nothing it does not match exactly.
Sources: V1-060, RE-8, Q12. Controls: RECLINT-ORPHAN (new row), H1, H2, H6, U14.
**R6.REC.11** The tool never infers a role or a review from a passing tool result.
Sources: E-142. Controls: O5.

**R6.REC.12** **Corrections.** A correction is a new record with `supersedes` and a new review.
Nothing is edited in place, and an id is never reused. **Residual limit.** The tool can check that the
role fields differ, not who actually wrote the records; identity rests on the writer's and the
reviewer's own recorded statements.
Sources: E-161. Controls: O6, O7, A7r.

**R6.REC.13** **Widening of an allow rule.** Any of the following, compared with the superseded
version, is widening: added files; a changed or shorter literal; fewer context or negative literals;
any change to the fingerprint set, including a swap with the count unchanged; a larger
`max_instances`; `context_required` turned off; a new allow rule without `supersedes`; any
`negative_allowance` added, raised or moved to another fingerprint. **Widening of a deny rule.** A
changed pattern, a narrower scope, removed examples, or a removed or changed countercontrol.
**Widening of a scope record.** As R6.RULE.13. Widening needs a `widening_review` record by a
non-author reviewer other than the record's own reviewer, under the same chain as any review: it names
the superseding record's blob and the superseded record's blob, its `verdicts` cover every item that
differs between the two (each changed field, added file, fingerprint or allowance), and every verdict
is `accept`. A widening review that covers only some items, or names other blobs, is invalid. Widening
of a record without a valid widening review is FAIL `record-invalid`; widening of the configuration
without one is ERROR `CONFIG_UNREVIEWED` (R6.REC.5).
Sources: E-162. Controls: A1r, A2r, A3r, A4r, A9r, A10r, A12r, E-A1r, E-A2r, E-A3r, Y4, Z10.

**R6.REC.14** **Examples and fingerprints.** Each fingerprint must be reproduced by a sentence of its
named file at `recorded_at`. Each example and countercontrol must behave as stated. Every fingerprinted
sentence, read at `recorded_at` in its named file, must be classified PASS by its own rule through
steps 1-6 of R6.RULE.4, with its own allowance. Every `negative_allowance` must equal, literal by
literal, the number of matches of that negative literal in its fingerprinted sentence, and may name
only literals of the rule's negative matcher. A rule's positive examples include each fingerprinted
sentence in full, not a fragment of it. Otherwise the record fails the lint (FAIL `record-invalid`).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-163. Controls: A6r, A8r, A9r, A11r, WB10, WB11.

**R6.REC.15** **PIN_OK.** A PIN_OK entry is valid only if listed in `F`'s pin table, or in a reviewed
record that the configuration at `F` references. An entry recorded after `F` is FAIL `pin-broken`.
Sources: E-164, RV-019. Controls: N1.

### 11.4 Configuration admission

**R6.REC.16** **Configuration admission.** The run names the plan commit `F` (`--freeze F`) and the
configuration (`--config F:<path>`) as explicit inputs; neither is inferred, and both are recorded. Any
step below that fails, or cannot be completed, refuses with ERROR `CONFIG_UNREVIEWED`:
1. **`F` and the configuration.** `F` is a full commit id, read through the verified reader. The
   configuration is read only from `F`'s tree at the named path, never from a file the caller supplies
   or from another commit.
2. **The pin table.** The pin table is derived, not chosen: it is read from the file `PREREG.md` in
   the same directory of `F`'s tree as the configuration, as a regular file. Within that file it is the
   last subsection whose heading matches `^### \d+\.\d+ Record pins\b`; its rows are
   `` | `<file>` | `<sha256>` | ``, each naming a file of that directory. The configuration and its
   review record are admitted only if listed there with their sha256. Files beside the configuration
   that the table does not list are never admitted. A missing `PREREG.md`, no such subsection, or a
   malformed table row refuses. The run takes no pin-table argument.
3. **Scope of the refusal.** These refusals, including the refusal of a run without `--freeze`, apply
   to chain admission. Every invocation of the tool's command line is an attempt at chain admission.
   Control-harness admission is available only to the in-process control harness (sec. 17), and replay
   admission only to the offline replay (sec. 7); neither is reached from the command line.
4. **Local runs and replay.** A run outside a host CI job, or one whose run record cannot be read
   (R6.REC.18 point 1), cannot reach `"chain"`. The offline replay writes `config.admission` with
   `mode: "replay"` and is never acceptable as a new run.

The record directory of the plan is identified by the configuration's path, which the result
records; the landing record names it with `F`. The tool also checks that directory against the
admitted record directories of sec. 21, a constant outside the configuration (sec. 19). Whether `F`
and the configuration path are the plan commit and record directory the owner designated is confirmed
procedurally (sec. A.50 items 2 and 5), not by the tool.
Sources: E-143, E-144, E-145, E-146. Controls: TR1, TR2, TR3, TR13, EI4, ADM-CONFIG-AT-F,
CHAIN-REFUSAL, TR45-opB, X11, RDIR-16, RDIR-20.

**R6.REC.17** **Object integrity (the verified reader).** Every read of a commit, tree or blob, in a
run, by the consumer and in the offline replay, goes through one reader over a local git object store:
- **Each object verified.** Every object is requested by its full id, and its id is recomputed from
  its type, length and content. An object that is missing, or does not hash to its id, is an
  unresolvable object (ERROR, sec. 7), or refuses admission (`CONFIG_UNREVIEWED`). A commit's parents
  and tree, and a tree's entries and their modes, are parsed from the verified content.
- **Nothing but verified content.** Refs, reflogs and packed refs are never consulted for a role
  commit: every role commit is an explicit full id (sec. 1), apart from the re-resolution of `M` before
  landing (sec. 23), whose result is then read through this reader. Replace refs and grafts are never
  applied. No parent or ancestry is taken from a traversal command, a graft, the store's `shallow` file
  or a commit-graph file: first-parent chains and ancestry are computed from parsed parents only.
- **Bounded walks, no fetch.** Every walk runs between explicit commits. A parent the walk needs and
  the store lacks is an error; no object is fetched on demand. The native clones of sec. 13 are full
  clones.
- **Entries.** Records, rule files, the configuration, the pin table, the delegation contract and the
  tool's files are read only from regular-file entries (mode 100644 or 100755); any other entry at such
  a path refuses (ERROR `CONFIG_UNREVIEWED` for an admission read; FAIL `record-invalid` for a record).
- **Caching.** A cache of verified objects or parsed trees serves only bytes the reader has verified,
  is keyed by exact object or commit id, and is read-only to its users.

Sources: E-156. Controls: GV1, GV2, GV3, GV4, GV5, GV6, GV6-disk, O6, GV-CACHE, GV-CACHE-AFTER-READ,
GV-CACHE-IMMUTABLE, GV-CACHE-KEY, K1-GRAPH.

### 11.5 Execution identity

**R6.REC.18** **Execution identity.** An acceptable result is computed by the tool files and run by
the workflow that the configuration at `F` pins, in the repository it names:
1. **The run record.** The tool reads its own run record by the run id the host assigns, from the
   host's REST API in the repository the job runs in: the repository id, the head repository id, the
   event, the head branch, the workflow path and the run's `head_sha`. `T`, the tool commit, is that
   `head_sha`. The run's `repository.id` and `head_repository.id` must both equal the configuration's
   `repository_id`, and its `event` must be `push` or `workflow_dispatch`.
2. **The tool's files and the workflow.** `T`'s tree is read through the verified reader. Under
   `tools/ledger_coverage/`, together with the entry point `tools/ledger_coverage.py`, it must hold
   exactly the files of the configuration's `tool.files`, each a regular file whose blob sha256 equals
   its pin; a further file, a missing file, a differing blob, or a symlink, submodule or other
   non-regular entry refuses. The run record's workflow path must equal `tool.workflow.path`, and the
   blob at that path in `T` must equal `tool.workflow.blob_sha256`. The workflow runs the tool with
   `python3 -I -B` from a checkout of `T`. Before evaluating anything, the tool compares the entry point
   and every file under `tools/ledger_coverage/` in that checkout with `T`'s tree: the same set of
   paths, each byte-identical. Any difference, including a file on disk that `T` does not hold (for
   example a compiled-bytecode file), refuses.
3. **Evaluated commits are inputs.** The commits evaluated (`X`, `C`, `L`, `M`, `H` and `E`) are
   explicit full ids, read through the verified reader and recorded. They are never the run's
   `head_sha`.
4. **The consumer repeats it.** The consumer repeats points 1-3 and the `uses:` check of point 5 for
   the producing run itself (sec. 7), from the host's REST API and from its own verified object store,
   against the configuration at `F` that the landing record names. A run whose repository, head
   repository or event fails point 1, a `head_sha` other than the `T` the result records, or a tool or
   workflow blob that differs from the configuration's pins is non-acceptance.
5. **Nothing unpinned executes.** In every run of the pinned workflow, no file outside `tool.files`,
   the pinned workflow, the actions it names by commit id and the interpreter's own standard library
   executes in the job, before or after the tool's own checks. The delegated and native checker runs
   are outside this rule and are governed by sec. 13 (R6.DELEG.3).
6. **The tool commit is on `main`.** The tool refuses (ERROR `CONFIG_UNREVIEWED`, before any
   evaluation) unless the run record's `head_branch` is `main`. The consumer requires `T` to lie on the
   first-parent chain of `M`, the `main` resolved by `git ls-remote` as sec. 23 states, walked by the
   verified reader.

No command-line option, environment value or other configuration field sets `tool` or
`repository_id`; they are read only from the configuration at `F`.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-147, E-148, E-149, E-150, E-155. Controls: TR14, TR14-tool, TR15, TR28-tool, TR28-consumer,
TR29, TR29-tool, TR30, TR48, TR50, TR51, TR52, EI1, EI2, EI2-consumer, EI3, EI5, EI14.

**R6.REC.19** **The pre-run pin check.** The first step after the checkout and the fetch of `F`,
before the entry point or any file of the checkout runs, is one fixed inline step of the pinned
workflow, whose `name:` is exactly `pre-run pin check`, run as `python3 -I -S -B -c '<program>'` with
the program given in the workflow text on its single `run:` line, so that it executes no file of the
checkout. The workflow fetches `F` by its full id. The step refuses unless the environment value
`GITHUB_REF` is `refs/heads/main` and `F` matches `^[0-9a-f]{40}$`. It reads the configuration blob at
`F` with `git cat-file blob`, at the path the run passes to the tool as `--config`, and takes
`tool.files`. It examines the entry point and the directory `tools/ledger_coverage/` on disk with
`os.lstat`, never following a link: `tools` and every other parent directory of a checked path must be
a real directory; every entry must be a regular file or a directory; the set of regular-file paths must
equal the paths of `tool.files` exactly; and each file's sha256 must equal its pin. Any failure, a
missing `F` or configuration, or an unreadable `tool.files` fails the step, and the job ends before any
tool code runs. A workflow blob with no such step, more than one, or a `run:` value that is not one
such line is refused by the review and fails the controls, whose runner extracts the program by this
rule.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-151. Controls: EI8, EI9, EI10, EI11, EI12, EI13, EI15.

**R6.REC.20** **The import path.** The workflow invokes `python3 -I -B tools/ledger_coverage.py`. The
entry point does not insert any directory of the checkout into `sys.path`; it loads the package
`tools/ledger_coverage/` by its location. Before any import of a module not already loaded at
interpreter start (only `sys` and `os` precede it), the entry point refuses unless the interpreter runs
in isolated mode and no `sys.path` entry lies inside the checkout. The refusal is ERROR, exit 65, with
the stop class `NOT_ISOLATED`, written to stderr as one JSON object with that class and the reason (RE-14). Because it fires
before any import, it writes no `result.json`; it is, with USAGE, one of the two documented cases that
write no `result.json`. The implementation exits 65 with a message and no class today; that is a
verification defect, corrected in the tool revision.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-152. Controls: EI6.

**R6.REC.21** **The workflow's executable dependencies.** The pinned workflow executes only the
pre-run check, the entry point, fixed `git` commands and the actions it names by commit id. The tool
and the consumer check the workflow blob at `T` by a line rule on its raw text, with no YAML parser.
The blob is refused if any line:
- contains `uses`, in any letter case, and does not match
  `^\s*(- )?uses: <owner>/<repo>[/<path>]<AT><40 lowercase hex>\s*$`, where `<AT>` denotes the
  at-sign character (U+0040), written here by name, and with literal `<owner>` and `<repo>` names;
- begins, after its indentation and any number of `-` or `---` markers each followed by whitespace
  (the prefix `^\s*((-|---)\s+)*`), with `"`, `'`, `{`, `[`, `?`, `&`, `*` or `!`;
- contains a colon followed by any whitespace and then `{`, `[`, `&`, `*` or `!` (the pattern
  `:\s+[{[&*!]`).

The rule only refuses; a form it refuses that YAML would read harmlessly is written another way in the
pinned workflow.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-153. Controls: EI7, EI7-tool.

**R6.REC.22** **Workflow content review.** The rest of the workflow's content is checked against this
list when the configuration's review covers `tool.workflow`, and the pin then fixes it: its triggers and
inputs (the run receives `F` and the configuration path as inputs, and a run without them fails the
pre-run check); `permissions` read-only except artifact upload; a GitHub-hosted `runs-on`, with no
`container:` and no `services:`; no `env`, `GITHUB_ENV` or `GITHUB_PATH` change of `PATH`, `LD_*`,
`GIT_*` or `PYTHON*`; no `shell:` override; the named actions only (no `setup-*` action, and no
composite or docker action that installs or downloads executables or refers to other actions by tag);
the exact run lines (the fetch of `F`, the pre-run check, and the entry point's command); the inputs
reach the shell only through `env:`, and the fetch of `F` is `git fetch --no-tags -- origin "$F"`, with
no `run:` line interpolating `${{ inputs.* }}`; no `continue-on-error`, and no `if:` on the steps after
the pre-run check; no reusable workflow.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-154. Controls: TR15, TR50, EI7.

### 11.6 Host reads, admission object, residual trust

**R6.REC.23** **Host reads.** The tool and the consumer read from the host only GitHub Actions
records, through its REST API, each with a `GET`: the producing run's record (R6.REC.18 point 1) and
its artifact list with each artifact's sha256 digest (sec. 7); and, for the host-run classes `pdf` and
`ci` (sec. 13), the runs on the evaluated commit, their jobs and conclusions, and the `pdf` artifact's
digest. A failed or incomplete read is never a fallback to another source: admission refuses, and a
host-run class whose records cannot be read is REVIEW_REQUIRED `delegated-evidence-missing`, never
PASS. No comment, Issue, pull request, branch, commit listing, tree or file content is read through the
host's API, and its GraphQL API is not used. Every repository object is read from a local git object
store and verified against its id. Re-resolving `M` before landing (sec. 23) uses `git ls-remote`,
which reads one ref id over the git protocol.
Sources: E-157, E-013. Controls: GV7, GV7-tool, GV7-consumer.

**R6.REC.24** **The admission object.** `result.json` records `config.admission`, an object with a
`mode` field: `"chain"`, `"control-harness"` or `"replay"`. Its mode is `"chain"` only when
configuration admission and execution identity held, and only then does it carry `snapshot`:
- the run record fields read: run id, repository id, head repository id, event, workflow path and
  `head_sha` (`T`); the workflow file's blob sha256 at `T`; the tool blob hashes at `T`;
- the evaluated commits `E`, `H`, `X`, `C`, `L` and `M`;
- `F`, the pin table's `{path, blob_sha256}`, and the configuration's and its review record's
  `{path, blob_sha256}`;
- the delegated evidence, for every delegated and native class of sec. 13, at `X` and, where `C`
  differs, at `C`: the host records the tool read for the class, as the host returned them, in
  canonical JSON; the sha256 of every artifact and result file the class used; the outputs of every
  checker the tool ran natively (for each run, the checker blob sha256, the exact command line, the
  working directory, the exit status, and the complete bytes of each result file it wrote and of each
  output the class compares); and the class's own recorded re-derivations;
- the sha256 of the canonical JSON of the snapshot itself.

Only `"chain"` is acceptable (sec. 7). The control harness (sec. 17) may admit a draft configuration
without its chain; its results carry `mode: "control-harness"` (with any simulated snapshot the control
supplies, never mode `"chain"`), are written as `control-result.json` with `"harness": true`, and are
never written as an acceptable result. The offline replay writes `mode: "replay"`.
Sources: E-158, E-159, E-145. Controls: TR5, TR5-sim, X11, TR45-opB, TR46.

**R6.REC.25** **Residual trust assumptions.** The tool and the consumer trust: the host's REST
records of Actions runs (a run's repository and head repository, event, workflow path and `head_sha`;
its jobs, their names and conclusions; an artifact's sha256 digest); the host runner (that it executes
the workflow at `head_sha` faithfully, with the interpreter and standard library of its image; given
R6.REC.18 point 5, the code that ran is then the code whose blobs were read and compared); git object
ids (every object is bound to its id by recomputation, which rests on SHA-1's second-preimage
resistance against the objects in the store and on git's refusal of objects that collision-detecting
SHA-1 flags; the local store itself is not trusted); and, at acceptance time, the authenticity of the
host records in the admission snapshot, which are host-attested and not reproducible offline. The
owner's approvals are not among these: they are procedural and outside the tool. None of these is a
value the caller can choose.
Sources: E-160. Controls: TR48, GV4.

***

## 12. Rule records: deny, allow, resid

**R6.DENY.1** **Rule records are plan records.** The deny rules, the allow rules for the plan's own
cases, and the review-profile rule `resid` that a configuration uses are rule records of the plan, in
the schemas of sec. 10. They are frozen and adopted with the amended plan at `F`, after independent
review, and referenced by the configuration at `F`. The tool's requirement is the rule mechanism:
sec. 9 (profiles), sec. 10 (schema, application, lint), sec. 11 (records) and sec. 14 (hit
classification). r6 states no rule content.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1001, V2-059, V2-060, V2-061, RV-049. Controls: RT-DR, RT-D, RT-D-gr58, L1, L2.

**R6.DENY.2** **Controls on pinned rule inputs.** The controls of the rule mechanism use the rule
files current at the commit under check as pinned control inputs, named with their blobs in the
expectation file (sec. 16). Acceptance of the mechanism (sec. 18) is its behaviour on those inputs. A
changed rule file is a changed control input: the affected expectations are re-established in the
expectation file before the gate can hold.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1001. Controls: V1, V2, V3, V5, V6, V9, V10, V11, V12, V13, V14, V16, V17, V18, V19, V20,
V22, N-W, RT-DR3W.

**R6.DENY.3** **Evaluation unit.** Each deny rule record states its evaluation units: lines,
sentences (splitter version 2, sec. 8), or both. A rule evaluated on both FAILs on a match in either. A
deny FAIL item carries the rule id and the rule alternatives that matched. Which rule of the plan uses
which unit is plan content.
Sources: E-1007. Controls: RT-DR, RT-DR3W, V2, V20, V14.

**R6.DENY.4** **Review-profile rules only add review.** Adding or widening the rule of a review
profile adds REVIEW_REQUIRED items only: it never removes an item and never turns an item into PASS.
The independent review of the plan's review-profile rule content is an outstanding obligation (sec.
32).
Sources: E-1032. Controls: V15, V21, V26.

**R6.DENY.5** **Outstanding rule content.** The content of the plan's rule records is transferred to
the plan amendment as outstanding obligations, each a named blocker on the execution it gates (sec.
32): the deny rules DR-1, DR-3, DR-4 and DR-5 with their definitions and patterns (the identifiers
DR-1d and DR-2 are retired, sec. 33, and never reused); the W1 allow rules, including W1-c's
fingerprints and its `negative_allowance`; the W2 allow rules, replacing P's corresponding
`RESIDUAL_ALLOW` and `EXPLAINED` entries and its blanket `(A1)` strip; and the `resid` pattern with its
parts resid-a, resid-b and resid-c.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1001, E-1002, E-1003, E-1004, E-1005, E-1006, E-1020, E-1021, E-1022, E-1024, E-1025,
E-1026, E-1027, E-1032. Controls: none (OBL-3).
**R6.DENY.6** **Accepted residual: V4 and V27 (for decision at adoption; not adopted by this
draft).** The question: with the deny rules DR-1, DR-3, DR-4 and DR-5 and the review profiles of the
A1 configuration, the added text of control V4 ("the framework's sixth structural property, finiteness
of the bijection") and of control V27 ("The framework's sixth structural property is finiteness of the
substratum", added alone and as the edited glossary line) produce no hit of any review or deny profile.
The expectation for both would then be PASS with zero hits, recorded as an accepted residual after the
candidate rule DR-2, which caught V4, was not adopted. That decision (V5-D1) is recorded only in
paraphrase. Consequences of confirming: an added sentence that asserts finiteness as an ordinal
structural property of the bijection or substratum, in the forms of V4 and V27, passes the tool
undetected; the original item 7 check also misses it; its detection rests on review outside the tool;
V4 and V27 are kept as controls so that a change in their outcome is visible. Consequence of
restoring: V4 (and V27) expect FAIL `deny-match`, which requires a plan rule record that catches them
(DR-2 or an equivalent, plan content under R6.DENY.1, reviewed with the deny set), and the
reconciliation of that rule against the negative examples. The owner decides at adoption between (a)
confirming the PASS expectation knowingly and (b) restoring the FAIL expectation. Until then the
expectations are deferred. The decision covers V4, V27, V27-glossary and V15 together (RE-1). Until it is made, each of the four
rows carries both candidate expectations, each marked "not authoritative; decided at r6 adoption",
and the gate reports `deferred-expectation` for it and never holds (sec. 16.5).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1001, V2-080, RE-1. Controls: V4, V27, V27-glossary, V15.

***

## 13. Delegation contract and classes

### 13.1 The contract

**R6.DELEG.1** **The delegation contract.** The contract is one structured record, `delegation.json`,
schema `oi-delegation/1`, in the amended plan's record directory beside `ledger.json` and `edits.json`.
It is frozen with the plan at `F`, its SHA-256 is listed in `F`'s PREREG pin table, and it is
referenced by the configuration. The tool reads it only as `--delegation F:path`; a hash that differs
from the pin is ERROR `SOURCE_CHANGED`. It enumerates exact paths, with no globs or prefixes. Its path
set must equal what the ledger implies: `tex_sources(ledger)` for TeX, and the fixed paths of the other
classes. A changed path at `X` outside the ledger and the contract is FAIL `unauthorized-change`.
Evidence not named by the frozen contract is never accepted, however and whenever it is supplied; no
caller-supplied result is evidence for a class.
Sources: E-1033, E-1034, E-1035, E-1036, E-1037, RV-029, RV-025, RV-007, V2-019. Controls: RT-C, G4,
S11-14, G-A1.

**R6.DELEG.2** **No blanket delegation of a ledgered file.** A ledgered file is checked by op C's
conformance (its bytes equal `H` with its splices applied), or by a native class that states its
regeneration rule and verifies its rebuild at the evaluated tree (`coverage-ledger`, R6.DELEG.15). A
delegation never absorbs a ledgered file.
Sources: RV-006. Controls: RT-C, G3, G5, S11-4.

### 13.2 Native execution and evidence

**R6.DELEG.3** **Native execution.** Every delegated or native-re-execution class is executed by the
tool itself against every tree whose delegated paths are evaluated. In the integrity stage the tool
creates a disposable full clone of the repository at exact `X` under `--out` (no `--depth`, no
alternates; `X`'s commit and tree ids checked in the clone), and, when `C` differs from `X`, a second
disposable full clone at exact `C`, checked the same way. No clone runs a configured smudge filter.
Every class is executed and recorded in each clone separately, with the same independent re-derivation;
a class PASSes for the run only if it PASSes at `X` and at `C`. The checker the contract names
(preserve_check) runs only from `F`'s blob, written into a directory under `--out`, never from the
clone's own copy. A class whose rule is to re-execute the evaluated tree's own generator
(`check_sc42_integration.py` for `sc42`, `tools/proof_census.py` for `coverage-ledger`) runs that tree's
own blob in its clone. Every such run uses `python3 -I -B`, runs inside a clone under `--out`, and
never runs in the user's repository or a worktree of it; this contains preserve_check's
`git worktree add`.
Execution isolation (RE-24 (a), Q13). The trusted checkers (preserve_check and every checker the
contract names) run only from `F`'s pinned blobs. A generator that a class re-executes runs from the
evaluated tree's blob, and the evaluated tree never decides its own acceptance:
- isolation: the generator runs in its own disposable clone under `--out`, separate from the clone
  the checker reads; the run has no write access to the user's checkout and no network access; the
  interpreter is invoked with the fixed flags `-I -B` and a fixed environment;
- permitted outputs: only the generated artifact paths the class names, inside the generator's clone;
- trusted comparison: the checker run from `F`'s pinned blob compares each generated output with the
  committed artifact byte for byte; the generator's own exit status or report is never the verdict;
- failure handling: a byte difference is FAIL `regeneration-mismatch`, a generated artifact path not
  written is FAIL `regeneration-output-missing`, a run beyond the class time limit is FAIL
  `regeneration-timeout`, and a write to any other path is FAIL `regeneration-extra-write`
  (obligation `DELEGATED`); none of them is ever PASS.
Sources: E-1038, RV-039, A-057. Controls: G9, G4, G5, O3-FILTER, G-A1, DELEG-REGEN.

**R6.DELEG.4** **Recording.** The tool records, for each run, the checker's blob sha256, its exact
command line, its working directory, its exit status, and the sha256 of each result file it wrote. It
then reads the result file it produced itself; a result file supplied from outside the run is never
evidence for a class that the tool can execute.
Sources: E-1039. Controls: G4, G6.

**R6.DELEG.5** **Independent verification of results.** The tool does not take a checker's verdict
on trust. For each class it re-derives what it can from the clone: `sc42` compares the re-executed
output bytes with the committed file itself; `coverage-ledger` compares each of the seven values with
the census output it produced; `tex` checks the `% source-sha256` stamps and the path set itself, in
addition to reading preserve_check's result. A checker result that disagrees with the tool's own
re-derivation is FAIL `delegated-evidence-invalid`.
Sources: E-1040. Controls: G4, G5, G6.

**R6.DELEG.6** **Host-run classes** (`pdf`, `ci`). The evidence is the host's run and job records,
read by the tool from the host's REST API inside the job (R6.REC.23), never a file supplied by a
caller. The tool checks `head_sha = X`, the named workflow and jobs, and their conclusions, and that
the run's event is `push` or `workflow_dispatch` and its repository and head repository ids equal the
configuration's `repository_id`. For `pdf` it also checks that the PDF comparison result names
`candidate_commit` and `candidate_tree` equal to `X` (fields the amended preserve_check adds, since
`--tree` records only a path), that it was produced by preserve_check run by this tool from `F`'s blob
on PDFs built in the clone at `X`, and that the uploaded artifact's sha256 equals the result's. If any
of these is absent, the class is REVIEW_REQUIRED `delegated-evidence-missing`; if any is inconsistent,
it is FAIL `delegated-evidence-invalid`.
Sources: E-1041, RV-043. Controls: G7, S11-3, GV7-tool.

**R6.DELEG.7** **No freeze, no PASS.** Without `F`, every delegated class is REVIEW_REQUIRED
`delegated-evidence-missing` and can never be PASS; a `plan` field that is null or absent is FAIL
`delegated-evidence-invalid`. Such runs are not chain runs (R6.REC.16 point 3).
Sources: E-1042. Controls: G8.

**R6.DELEG.8** Where the environment cannot run the clone (a local run, sec. A.40), the class is
REVIEW_REQUIRED `delegated-evidence-missing`. The code path and its controls run in CI.
Sources: E-1043. Controls: G2, G-A1.

**R6.DELEG.9** **Evidence absent** (a run not made, or no result file): REVIEW_REQUIRED
`delegated-evidence-missing`.
Sources: E-1044, RV-040. Controls: G2, Y6.

**R6.DELEG.10** **Evidence defective**: FAIL `delegated-evidence-invalid`. That is any of: a schema
other than `a1exit-checker-result-v1` (whose fields are `checker`, `mode`, `plan`, `ledger_sha256`,
`ledger_base`, `candidate`, `base`, `checks`, each with `name`, `status` and `discrepancies`, and
`verdict`); `checker` other than `preserve_check.py`; `plan` other than `F`; `ledger_base` or `base`
other than `H`; `ledger_sha256` other than `F`'s ledger; `candidate` other than the evaluated tree's
full 40-hex id; a nonzero exit; `verdict` other than `pass`; a required check missing, not `pass`, or
with non-empty discrepancies; a checker blob that differs from `F`'s copy; a result file the tool did
not produce in this run, for a class it executes; a disagreement between a checker's result and the
tool's own re-derivation.
Sources: E-1045, RV-041, RV-030. Controls: G1, G4, G6, G7, G8, Y6, S11-13.

**R6.DELEG.11** A class PASSes only if every required item holds. Missing evidence is never PASS.
Sources: E-1046, E-1054. Controls: G2, RT-C, GV7-tool.

### 13.3 Classes

**R6.DELEG.12** **`tex`.** Paths: the TeX files of `tex_sources(ledger)` (A1: Complexity,
Computation, GR, Main, Methodology, SM, Structure, Substratum and FULL). Delegated: `preserve_check.py
--commit <tree> --plan F --result-json OUT` in the clone, with the commit-mode checks "candidate against
base, ledger, regenerated artifacts and plan record" and "scope assertions of amendment sec. 31" both
`pass`. Native as well: each file's last line is `% source-sha256: <sha256 of the tree's .md>`, and the
path set equals `tex_sources`; a failure of either is FAIL `delegated-evidence-invalid`.
Sources: E-1048, RV-042. Controls: G6, G1.

**R6.DELEG.13** **`pdf`.** Paths: the PDFs of the same sources. Delegated: `preserve_check.py --tree
... --pdf-compare BUILT --pdf-out OUT --plan F --result-json OUT` in the exact-head CI run on `X`, with
the check "committed PDFs against the CI build (pages, pdftotext)" `pass` and its discrepancies empty.
Required: `candidate_commit` and `candidate_tree` equal to `X`; a host run record with `head_sha = X`,
the named workflow and job, and conclusion success; the result hash equal to the uploaded artifact.
Native as well: each PDF blob differs from `H`'s.
Sources: E-1049, RV-043. Controls: G7.

**R6.DELEG.14** **`record-dir`.** Paths: the plan's record directory. Native, not delegated: every
path under the record directory at the evaluated tree equals `F`'s blob, and additions are allowed only
in the subdirectory `execution/` of the record directory, and only for the files the contract
enumerates (A1: `execution/RESULT.md` and the two `result.json` files). Anything else is FAIL
`delegated-evidence-invalid`. The classification of the record directory on `M` is sec. 21.
Sources: E-1050, RV-044, A-057. Controls: RT-C, DELEG-RECDIR (new row).

**R6.DELEG.15** **`coverage-ledger`.** Path: `verification/coverage/LEDGER.json`, a ledgered file.
Native: its bytes at the evaluated tree equal `H` plus its splices, except the fingerprint values of the
seven STALE ids; each STALE id occurs exactly once (a missing or duplicated id is FAIL); each replaced
value equals the fingerprint that `tools/proof_census.py --json` (the evaluated tree's blob, run in the
clone, exit 0) reports for that id; any other byte difference is FAIL. Each FAIL is
`delegated-evidence-invalid`.
Sources: E-1052, RV-046. Controls: G3, G5, S11-4.

**R6.DELEG.16** **`sc42`.** Path:
`verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json`.
Native re-execution only, in the clone at the evaluated tree: the clone contains
`ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf`; `python3 -I -B check_sc42_integration.py --verbose`, plain
and with `-O`, exits 0 and its stdout is byte-identical to the result file; `--self-test`, plain and
with `-O`, exits 0 and its stdout is byte-identical to the controls file, which equals `H`'s. No
delegated evidence substitutes for the re-execution.
Sources: E-1051, RV-045. Controls: G4, G9, S11-13.

**R6.DELEG.17** **`ci`.** Paths: none. Delegated: the host run and job records for the exact-head run
on `X`, each named job concluding success. The named jobs are the Lean kernel, Mathlib, the R7 guard,
`bohr_frequency_probe.py`, `guards_check.py --mutants` and `coverage_check`.
Sources: E-1053. Controls: S11-3, GV7-tool.

**R6.DELEG.18** **Outstanding.** The preserve_check gaps that the plan amendment must close, and the
decision on its gap 6, are requirements of the plan amendment, not of this design; they are outstanding
obligations, each a named blocker on the execution of the classes they affect (sec. 32).
Sources: E-1038. Controls: none (OBL-8).
***

## 14. Hit classification and review load

**R6.HIT.1** **Held.** A hit is held when it lies on a line of the region of a tracked site that is
resolved, whose classified bytes are unchanged (state `unchanged` or `moved`, identity verified), and
that is not an HP site, so that the site's frozen classification still applies; such a hit is PASS by
that classification. No other route holds a hit: there is no
read set, no `new_site_rules` regex and no read-entry route, and the ledger adapter supplies no read
entries (sec. 26).
Sources: V1-065, E-1056. Controls: U1, U2, RT-E, L2.

**R6.HIT.2** **Decision of a hit.** The first matching row decides:

| Hit | Decision | Resolved by |
|---|---|---|
| a deny match on a tree where deny profiles run (R6.PROF.4) | FAIL `deny-match` | not resolvable by a record or rule |
| held by a tracked site (R6.HIT.1) | PASS | the frozen classification |
| in an HP region | REVIEW_REQUIRED `unclassified` | the HP adjudication's `hit_classifications` |
| in a ledgered replacement image, inside or outside a site region | REVIEW_REQUIRED `new-pattern-in-replacement` when the profile's pattern is absent from the FROM region, otherwise `unclassified-in-replacement` | a hit classification record or an allow rule |
| any other unheld hit | REVIEW_REQUIRED `unclassified` | a hit classification record or an allow rule |

A hit that an allow rule addresses is decided by R6.RULE.4, which can give PASS, FAIL
`rule-negative-match` or `rule-overreach`, or REVIEW_REQUIRED `rule-fingerprint-mismatch`. A hit
matched exactly by a verified hit classification record is decided as the record states. Op C runs op
D restricted to the text of every replacement region, so that every hit in a replacement image is
decided by this table.
A hit in an HP region is REVIEW_REQUIRED `unclassified` with obligation `HP`, as the tool commit
emits it (RE-25 (a); confirmed by reading the HP-region attribution and the hit decision of the
engine at the tool commit).
Sources: V2-027, V2-021, V1-066, E-1055, E-1057, E-1058, E-1059. Controls: U12, L4, V7b, WB4, A5r, I2-7,
RT-D, HIT-REPLACEMENT (new row).

**R6.HIT.3** **Every hit listed.** Every hit is listed in the result with its profiles, decision and
class; nothing is truncated. The item of an unheld hit carries the diagnostic field `pre_existing`:
true when identical text was unheld at the prior endpoint (the FROM of the last segment, sec. 3), or
when the hit lies inside a splice whose FROM region was an unheld hit line. `pre_existing` does not
change the decision.
Sources: V1-066. Controls: RT-D, RT-T0.

**R6.HIT.4** **Hit classification record.** Schema `oi-hit-classification/1`, the file
`hit-classifications.json` in the plan's record directory (sec. 22), its classifications under the key
`classifications`, with its `record_id` (R6.REC.8). Each classification binds: `file` and
`line_sha256`, which must be unique in the tree; the segment; the splice id or HP step; the profiles and
patterns; the semantic classification (which qualification is visible, with the reason); and `author`,
under the chain of sec. 11. The record states that it classifies meaning, and that the splice
provenance is recorded separately. A line hit by several profiles needs one classification that names
every profile hit on it. It reaches the run through the `--classify` route of sec. 22.
Sources: E-1060, E-1061. Controls: I2-7, I2-4, I2-6.

**R6.HIT.5** Each hit line needs exactly one classification. A record may serve two rows of the table
of R6.HIT.2 (for example an HP region's hit that is also in a replacement image), but no line is
classified twice.
Sources: E-1066. Controls: I2-7, RT-T.

**R6.HIT.6** **Review load.** A run is PASS only when every hit it reports is held, classified by a
verified record, or classified by an allow rule. Until every record and rule the plan needs exists,
`coverage` and `terms` on the retirement's candidate are REVIEW_REQUIRED at best, and FAIL while any
FAIL item of sec. 15 remains. The review-load figures measured during design are historical (appendix).
Sources: RV-014, E-1067. Controls: RT-T, RT-D, RT-T0.

***

## 15. FAIL and REVIEW conditions (complete class list)

**R6.CLASS.1** **Completeness.** The classes below are the complete set of item classes. Every item
carries exactly one class, one decision and one obligation. A FAIL item makes the outcome FAIL (exit
20); a REVIEW_REQUIRED item, with no FAIL item, makes it REVIEW_REQUIRED (exit 10). The stop classes of
ERROR, VOID, INTERNAL and USAGE are those of sec. 7. An emitted class not in this list is a defect.
Where `class_meaning` (sec. 7) defines a class, every item of that class quotes its meaning. A failure
reported without an item is not allowed: every FAIL condition below produces at least one item. At
the tool commit the op A record checks, the replay equality, `ck_errors` and `extended_unmapped` FAIL
without an item; each emits an item in the tool revision (RE-23 (a); OBL-28, C-23).
Sources: E-1068, V2-068, V2-069, RV-057, V1-079. Controls: B4-MEANING, S7-schema-and-checker.

**R6.CLASS.2** **Sites** (FAIL; sec. 4, sec. 6, sec. 3):

| Class | Condition |
|---|---|
| `unauthorized-change` | a site change that no splice of the frozen ledger and no declared class specifies (sec. 4) |
| `missing` | a site whose anchor occurs nowhere in the evaluated tree (sec. 4) |
| `duplicated` | a site whose anchor occurs more than once where exactly one occurrence is required (sec. 4) |
| `ambiguous` | a site whose occurrence cannot be selected uniquely by count, context and ordinal, including a disagreement between translation and search (sec. 4) |
| `context-meaning-unverified` | a meaning-context site whose context changed, with no context adjudication matching both context hashes (sec. 6) |
| `retained-changed` | a ledger entry listed as retained that is absent from `edits.json`, has a splice, or whose site text differs between `H` and `X` (sec. 3) |

The PASS states of a site are `unchanged`, `moved`, `authorized-replacement`, `authorized-removal` and
`provenance-adjudicated`.
Sources: E-1069, V2-026, V1-079. Controls: U4, U5, U7, U8, H4, B5, K1, CLASS-RETAINED (new row).

**R6.CLASS.3** **Ledgered files** (FAIL):

| Class | Condition |
|---|---|
| `unauthorized-edit` | a ledgered file whose bytes differ from `H` with the frozen ledger's splices applied |
| `unledgered-file-change` | in a ledgered segment, a file not in the ledger whose bytes differ between FROM and TO; that file's sites then take the relocation rules of sec. 4 |

Sources: E-1070, V1-079. Controls: M1, M2, Y2, S11-9, CLASS-UNLEDGERED (new row).

**R6.CLASS.4** **Historical provenance** (FAIL; sec. 5):

| Class | Condition |
|---|---|
| `hp-unadjudicated` | a site changed in E..H that no HP adjudication names |
| `untracked-hp-overlap` | an HP site without an adjudication whose region at `H` an H..X splice overlaps (reported in RET, listing the splices) |
| `provenance-mismatch` | an adjudication step whose commit or hash differs from the recomputed walk |
| `provenance-gap` | an adjudication with a step missing or extra against the walk |
| `provenance-foreign` | a change at a commit outside the pinned chain |
| `provenance-ambiguous` | a region not unique as a whole-line block at a parent, or anchors that do not keep their order |
| `adjudication-row-changed` | an adjudication whose carried `row`, `code` or `owner` differs from the frozen values |
| `stale-adjudication` | an HP adjudication entry that, on a tree and in a segment to which its record applies, resolves no subject (R6.REC.10; v1 4.6) |

Sources: E-1071, V2-026, V1-061, V2-029, Q12. Controls: RT-H0, RT-T0, H1, H2, H3, H5, H6, Z10,
CLASS-PROV-AMBIGUOUS (new row), RECLINT-ORPHAN, U14.

**R6.CLASS.5** **Hits and rules** (FAIL):

| Class | Condition |
|---|---|
| `deny-match` | a deny profile matches a line or sentence on a tree where deny profiles run (R6.PROF.4), or a `register`, `register-caps` or `infinity` FAIL (R6.PROF.6, R6.PROF.7) |
| `item7-literal-match` | a match of the countercontrol profile `item7-literal` (only that profile) |
| `rule-negative-match` | an allow rule's negative matcher matches beyond the sentence's allowance (R6.RULE.4 step 3) |
| `rule-overreach` | an allow rule applied more than `max_instances` times in the tree (R6.RULE.4 step 5) |
| `record-invalid` | any failure of the record lint, rule lint or review chain (sec. 10, sec. 11), including an orphan context adjudication or hit classification entry and a duplicate record entry (R6.REC.10) and an op A record-check failure (R6.CLASS.11) |
| `final-unclassified` | under `--final`, a REVIEW item of a profile in the selected check's `final_profiles` (sec. 7) |

Sources: E-1072, V1-079. Controls: V1, S11-5, RT-I7, WB2, L3, A1r, V23, X9.

**R6.CLASS.6** **Records that match nothing.** An HP adjudication entry that matches no subject on a tree and
segment its record applies to is reported as `stale-adjudication`; a context adjudication or hit
classification entry that matches no subject, and a duplicate entry, as `record-invalid` (R6.REC.10).
An entry that names a subject and disagrees with it is reported by that subject's own class
(R6.CLASS.4); an HP adjudication entry whose region hash differs from the walk gives both
`provenance-mismatch` and `stale-adjudication` (R6.HP.7).
Sources: E-1072, Q12, RE-8. Controls: RECLINT-ORPHAN (new row), U14 (row restored), H1, H2.
**R6.CLASS.7** **Pins and mirrors** (FAIL; sec. 4):

| Class | Condition |
|---|---|
| `pin-broken` | a guard-pin literal that the pin check of sec. 4 finds broken by the evaluated change (present in its target at `H`, absent at the evaluated tree) and that no valid PIN_OK entry exempts, or a PIN_OK entry recorded after `F` (R6.REC.15) |
| `pin-target-missing` | an updated guard pin whose new literal is absent from its file, or does not occur in one of its targets (op C) |
| `mirror-mismatch` | a mirror whose text differs from its source where the plan requires byte identity |

These two pin classes are defined independently of the implementation; a difference from the tool
commit is a verification defect (RE-27 (b), RD-21).
Sources: E-1073. Controls: N1, S11-12, S11-8, CLASS-PIN-TARGET (new row).

**R6.CLASS.8** **Lean** (FAIL): `lean-code-change`, a Lean file of the evaluated tree that differs from
`H` outside comments.
Sources: E-1074. Controls: S11-10.

**R6.CLASS.9** **Delegation** (FAIL): `delegated-evidence-invalid` (R6.DELEG.10 and the class rules of
sec. 13); and `unauthorized-change` for a changed path outside the ledger and the contract
(R6.DELEG.1); and, for a re-executed generator (R6.DELEG.3), `regeneration-mismatch`,
`regeneration-output-missing`, `regeneration-timeout` and `regeneration-extra-write`.
Sources: E-1075, Q13. Controls: G1, G3, S11-13, S11-14, DELEG-REGEN.

**R6.CLASS.10** **Tree roles** (FAIL; sec. 20, sec. 23):

| Class | Condition |
|---|---|
| `candidate-parent` | an `X` whose parents are not exactly `H`, a commit of the chain from `X` to `C` with more than one parent, or a `C` that does not descend linearly from `X` |
| `landing-parents` | an `L` without exactly two parents, the second equal to `C` |
| `landing-first-parent-not-M` | an `L` whose first parent is not the recorded `M` |
| `landing-drops-main-change` | a path that only `M` changed whose content at `L` differs from `M`'s |
| `landing-conflict-unresolved` | a path both sides changed whose content at `L` differs from the computed composition (sec. 20) |
| `landing-extra-change` | any other path content at `L`, or a difference between the landing diff and the execution's own diff (sec. 20) |
| `base-drift` | a side change on `M` to a ledgered or corpus path not covered by a reconciliation record that applies (sec. 23) |

Sources: E-1076, RV-057. Controls: TT3, TT4, TT9, R15, TT10, TT7, N10, TT11, N4, N5, N16-file.

**R6.CLASS.11** **Op A record checks.** The record checks of op A (sec. 3) hold only if every replay
equality holds, the replay reports no error, the frozen self-test passes, and `record_checks.pin_findings`
is empty. A pin finding is a site whose pin line is not unique, or an override anchor that does not
occur in its pin line. When the record checks do not hold, the run is FAIL with an item of class
`record-invalid` (obligation `RECORD`) naming each failed check. The implementation today makes the
outcome FAIL through `record_checks.holds` without emitting an item; that is a verification defect,
corrected in the tool revision.
Sources: E-1077, V1-080, V1-079. Controls: S11-2c, CLASS-RECORD-CHECKS (new row).

**R6.CLASS.12** **REVIEW_REQUIRED** (exit 10):

| Class | Condition |
|---|---|
| `unclassified` | an unheld hit outside every replacement image with no record or rule that applies (R6.HIT.2), or an allow rule's step 1 not met |
| `new-pattern-in-replacement` | a hit in a ledgered replacement image whose profile pattern is absent from the FROM region, with no record or rule |
| `unclassified-in-replacement` | a hit in a ledgered replacement image whose profile pattern is present in the FROM region, with no record or rule |
| `rule-fingerprint-mismatch` | an allow rule's scope and matcher apply but its sentence or required context differs from every fingerprint (R6.RULE.4 step 4) |
| `rule-stale` | a fingerprinted sentence no longer present on a tree where staleness is evaluated (R6.RULE.8) |
| `context-structure-changed` | a LIST or TABLE site whose structure context or context changed, with no adjudication matching both context hashes and both structure hashes (sec. 6) |
| `delegated-evidence-missing` | delegated or native evidence absent, not producible in the environment, or host records unreadable (sec. 13) |
| `side-change-unclassified` | a change on `M` outside every declared class, a classified path whose blob differs from its class pin, or a path in the plan's record directory on `M` that is unequal to `F` (directory completeness, sec. 21) |

Sources: E-1078, V2-069, V1-079. Controls: U12, V7b, S1r, S2r, K6, G2, R18, R19, RDIR-2, RDIR-21,
HIT-REPLACEMENT (new row).

***

## 16. Verification architecture: expectation file, runner evidence, independent gate, correspondence check

### 16.1 Authority

**R6.GATE.1** The expected result of every control is stated once, in the expectation file of schema
`oi-control-expectations/1`. r6's prose states requirements and names the controls that test each
one; it carries no expected-result table (OD-2). `controls.json` keeps only what the engine reads:
each row's `operations` and `direction`, and the file's `control_inputs`; its `expect`, `reference`,
`case` and `by` fields are withdrawn. The decision rules are fixed with the file at adoption; reference
figures are informational, and a deviation from one is investigated, never tuned away. A runner's
predicate is a diagnostic of the runner; the verdict on a control is the gate's (R6.GATE.9). A
reference figure never decides a verdict (OD-1).
Sources: V1-114, V1-130, A-130, OD-1, OD-2. Controls: GATE-1, GATE-6, GATE-16, GATE-20.

### 16.2 Expectation file schema `oi-control-expectations/1`

**R6.GATE.2** The file is one JSON object with `schema`, `record_id`, `rows` (array) and `retired`
(array). Unknown fields are refused. Each row has the following fields.

| Field | Meaning |
|---|---|
| `id` | Control id, unique in the file; never reused (sec. 34). Mutant rows have the id `MUT:<set>:<mutant id>` (R6.GATE.10). |
| `migrated_from` | The pre-r6 id, when renamed under OD-31. |
| `requirements` | The r6 requirement ids (`R6.<CODE>.<n>`) of the requirements that name the control (at least one). |
| `runner` | `file:line` of the runner predicate. The recorded id equals `id`. `null` when no runner implements the control (the gate then reports it missing). |
| `operations` | The tool operations the control invokes; `[]` when it invokes none (mutation harness, gate, consumer predicate, pre-run step, lint library). |
| `direction` | `positive`, `adversarial` (the default) or `both`; or an object whose `of` is one of these and which records the both-directions decision of R6.CTRL.3: `exempt: "observation"`, `required: "opposite direction"` or `scope: "outside"`, each with its `why` (Q11). The engine reads the string or `of`. |
| `paired_with` | The ids of the rows that run the same input, differing only in the mutation, and so record this row's opposite direction (RE-4). |
| `predicate_kind` | `declarative` (the default) or `procedural`. |
| `case` | The case a row constructs, where the row states one outside `expect` (the gate's own controls); informational. |
| `expect` | The full declared expectation (below). A row whose `expect` is `null` cannot hold; an `expect` of outcome DEFERRED marks an expectation deferred to an owner decision (RE-1). |
| `candidate_expectations` | Deferred rows only: each candidate `{label, status, expect}`, with `status` "not authoritative; decided at r6 adoption"; no candidate is evaluated for the verdict. |
| `restored` | The expectation for the restored tree, where one is stated. |
| `procedure` | Procedural rows only: `{name, lib, evidence, note}`. `lib` names an entry of the procedure library (R6.GATE.8). `evidence` defaults to the library's evidence contract. |
| `composed_of` | For a design id split into recorded halves. A row without its own runner holds only if every component holds. A row that also has its own runner holds only if its own record holds and every component holds (GATE-26). |
| `depends_on` | Ids whose status must be PASS before this row can be PASS. Otherwise the row may only be NOT RUN with the dependency's release condition. |
| `status_allowed` | Default `["PASS"]`. `NOT RUN` is admitted only together with `not_run`. Mutant rows allow `KILLED`, `SURVIVED` or `NOT APPLIED` (R6.GATE.10). |
| `not_run` | `{reason, release_condition, release_check}`. `release_check` is a predicate the gate evaluates on the commit under check (R6.GATE.15). |
| `reference` | Informational figures, never compared for the verdict (R6.GATE.9). |
| `source` | Governing design cite: `D:` is v6.0e, `r5:`, `v1:` or `v2:`, with the approved translation named (OD-17, OD-19, OD-21, OD-22, MC-n), or the r6 requirement that states a row r6 adds. |
| `flags` | Informational notes for reviewers. |

Each row records the second direction of its control and, for an expected FAIL, the class of sec. 15
and, for a deny FAIL, the rule alternative that produces it; the gate checks each against the actual
result.
Sources: A-130, E-1080, RD-4, RD-32. Controls: GATE-12, GATE-17, GATE-26.

**R6.GATE.3** The `expect` object has these fields:

- **`outcome`.**
  - Tool outcomes: PASS, REVIEW_REQUIRED, FAIL, USAGE, ERROR, VOID, INTERNAL.
  - For subjects that are not a tool run: NO_ITEM, ITEM, ANY, NON_ACCEPTANCE, ACCEPTED, PRE_RUN_PASSED,
    PRE_RUN_FAILED, LINT_PASS, LINT_FAIL, RC_HOLDS, RC_FAILS, RESULT_EQUAL_CLEAN,
    RESULT_EQUAL_FULL_STORE, RESULT_EQUAL_WITHOUT_AMENDMENT, REPLAY_EQUAL, LANDING_VERIFIED,
    LANDING_REFUSED, RESOLVED, TEXT_EQUAL, HASH_EQUAL, PREDICATE, ORACLE, COUNTERCONTROL, REFUSED,
    NOT_REFUSED, COMPOSITE.
  - For the gate's own controls: GATE_HOLDS, GATE_FAIL, GATE_ERROR.
  - For mutant rows: KILLED, SURVIVED, NOT_APPLIED.
  - For an expectation deferred to an owner decision: DEFERRED (R6.GATE.9, `deferred-expectation`).
- **`exit`.** It defaults to the outcome's code in sec. 7: 0, 10, 20, 64, 65, 70 or 71; for the
  gate's own controls, GATE_HOLDS 0, GATE_FAIL 20 and GATE_ERROR 65. The gate always compares the
  actual exit against the stated or implied code.
- **`stop_class`.** The ERROR or VOID class in `result.json` `stop.class`.
- **`classes_exact`.** Either a list (the set of item classes of the whole result) or an object
  mapping an item filter to a list. `classes_include` is the subset form.
- **`counts`.** An object from a count key to an integer. Key grammar:
  - `finding_counts:<OBL>/<DECISION>/<class>` reads the result's `finding_counts`;
  - `site_counts:<state>`;
  - `<unit>[k=v,...]` with unit `items`, `lines`, `sentences`, `hits` or `findings`, counted over the
    result. Filter keys are item fields (`obligation`, `class`, `decision`, `rule_id`, `profile`,
    `file`, `subject`, `segment`, `state`, `path`, `literal`, `only_profile`). `|` separates
    alternatives.
- **`sites`.** A list of `{subject, ...fields}` that must hold for the named site or subject.
- **`invariants`.** A list of single-key objects from the closed vocabulary listed in the annex to this
  section (16.10). An unknown key makes the file invalid.
- **`gate_findings_include`** and **`gate_findings_exact`.** For the gate's own controls: the gate
  findings (R6.GATE.9) the self-test run must include, or must equal exactly.
- **`cases`.** A list of case expectations, each with `case`. A list of names means each named case
  separately, with the same expectation.

`$name` values are bindings that the runner's evidence manifest supplies. The gate checks each binding
against the retained mutation diff: a bound subject must be a path or site the mutant changed. An
unbound `$name` is `raw-evidence-missing`.
Sources: E-1080, OD-1, Q1. Controls: GATE-1, GATE-6, GATE-17.

**R6.GATE.4** The `retired` array entries are `{old_id, disposition, underlying}`. `underlying` is one
of `preserved-at <ids>`, `obsolete: <reason>` or `withdrawal-needs-decision` (Q4). A retired id is
never a row id, and naming it as a live control fails the correspondence check (R6.GATE.12).
Sources: Q4, OD-31. Controls: GATE-8, GATE-17.

### 16.3 Runner evidence contract

**R6.GATE.5** Every runner writes a structured record per control, in the file
`control-records.json` (schema `oi-control-records/1`): `{id, status, actual, predicate, evidence}`.
- `status` is one of PASS, FAIL and NOT RUN. A status of SKIP does not exist (RD-7): a control that is
  deliberately not run is NOT RUN, and a summary never counts NOT RUN as met.
- `actual` holds every quantity the runner asserted.
- `evidence` names the control's evidence directory.

A control-harness run writes `control-result.json` with `harness: true` and `config.admission.mode`
`"control-harness"`, never `result.json`; a consumer rejects it as a result (X11).
Sources: E-1189, E-1190, E-1191, RD-7. Controls: GATE-5, GATE-9, GATE-20, X11.

**R6.GATE.6** The mutation run writes one mutation record per mutant, in the file
`mutation-records.json` (schema `oi-mutation-records/1`): `{id, status, killed_by, mutated_file,
rule, evidence}`.
- `id` is the row id `MUT:<set>:<mutant id>`;
- `status` is one of KILLED, SURVIVED and NOT APPLIED; a mutant with no record is missing;
- `killed_by` lists the control ids whose recorded status on the mutant differs from their status on
  the base run (empty unless KILLED);
- `mutated_file` and `rule` name the change the mutant makes;
- `evidence` names the retained mutation diff and the per-control records of the mutant run.

The base run of the mutation step has every control at its expected status.
Sources: RD-1, Q8. Controls: GATE-21, GATE-22, GATE-23, GATE-24.

**R6.GATE.7** Every runner retains the raw evidence per control, under `evidence/<job>/<id>/`, with a
`manifest.json` (schema `oi-control-evidence/1`). For each case the manifest gives:
- the argv;
- the exit status file;
- `result.json` (or `control-result.json`, or the USAGE stderr JSON);
- the listing of `--out`;
- the input mutation (paths with blob ids before and after);
- the bindings;
- the sha256 of every file.

Where a runner keeps only a summary today, r6 requires the raw evidence named in the procedure library
(R6.GATE.8) to be retained:
- for sweeps, per-site item tuples, not whole results;
- for two-run comparisons, both results;
- for the purity lint, the lint report, the linted source map and the value set;
- for host-process properties, the step exit file, the marker-path listing taken after the step, the
  entry-point sentinel and the import trace;
- for an external oracle, P's outputs as files.

The evidence set is a CI artifact. Its manifest digest is recorded with the run. Retention on `main`
follows sec. A.42 when an enduring claim relies on it.
Sources: E-1189, Q1. Controls: GATE-9, GATE-10.

### 16.4 Independent extraction

**R6.GATE.8** The gate derives `actual` itself and does not trust the runner's `actual` or `status`.
It imports nothing from `tools/ledger_coverage/`.

- **Declarative, one tool run per case.** The gate reads:
  - the exit file;
  - `result.json` (`outcome`, `stop.class`, `items[]` with `obligation`, `class`, `decision`,
    `subject`, `rule_id`, `alternatives`, `segment` and `fingerprint`, `sites[]`, `finding_counts`,
    `site_counts`, `hit_counts`).

  It evaluates every `expect` field. It cross-checks `outcome` against the exit file, and it
  recomputes the outcome from `preflight`, `record_checks` and `items` with its own sec. 7 precedence
  rule.
- **Procedural, gate-evaluated.** The gate computes the predicate from retained raw evidence:
  - `rel-equal`: equality of the item tuples `(obligation, class, segment, fingerprint)` between the
    named runs;
  - `sweep`: per site, the set difference against the unmutated tuples;
  - `set`: an expected set computed from a retained tree listing;
  - `replay`: byte equality except `config.admission.mode`;
  - `hash`: equality of `engine.blob_sha256` across two results;
  - `double-run`: byte equality of the two retained `result.json` files of one operation run twice on
    equal inputs (argv, configuration blob, object ids and environment) into two fresh `--out`
    directories (REPRO-DOUBLE, R6.REPRO.2);
  - `ast`: the gate's own parser or regex applied to retained inputs (a widened rule against its
    negative examples, the workflow arm text, the clean-path predicate);
  - `rtl2`: the three-valued RT-L2 predicate (R6.GATE.16).
- **Procedural, attested with checked evidence.** Where re-execution is impractical, the gate verifies
  the retained evidence named by the library:
  - `prerun`: step exit file, marker listing, sentinel, import trace;
  - `consumer`: the acceptance clauses that decide the case, re-read from the retained result, landing
    record and snapshot (admission mode, `harness` field, F, pin table, evaluated commits, recorded
    `T`);
  - `lint`: the findings list and a non-empty linted source map;
  - `oracle`: the tool result against P's retained output;
  - `fixture`: the per-case ls-remote fixture and the landing-check exit.

  In each case the runner's value must equal the value the gate reads.

Real-tree controls run in CI, and their decision rules are the declarative `expect` fields the gate
re-evaluates; counts are informational unless `expect` states them.
Sources: V2-098, E-1190, Q1, RD-2. Controls: GATE-1, GATE-6, GATE-10, GATE-13, GATE-14, GATE-15,
GATE-25.

### 16.5 Verdict rules

**R6.GATE.9** The gate fails (GATE_FAIL, exit 20) on each of the following findings:

- `missing-id`: a row id, or a `composed_of` component, has no record;
- `unexpected-id`: a record id is not in the file;
- `duplicate-id`: two records carry one id, within a job or across jobs;
- `status-not-allowed`: the status is not in `status_allowed`, or is NOT RUN while its `release_check`
  holds;
- `declarative-mismatch`: an `expect` field differs from the gate-extracted actual;
- `procedural-failed`: the named procedure does not hold on the retained evidence, or a row with
  `composed_of` and its own runner record holds on its own record while a component does not hold;
- `raw-evidence-missing`: the manifest is absent, a named file is absent or does not match its sha256,
  or a binding is unbound or does not match the mutation;
- `status-actual-inconsistent`: the runner's status disagrees with the gate's verdict in either
  direction;
- `correspondence-orphan-row` and `correspondence-orphan-requirement` (R6.GATE.12);
- `expect-null`: a row whose `expect` is null;
- `direction-missing`: a control row in the both-directions scope of R6.CTRL.3 whose second direction
  is not recorded (no `restored`, no direction `both`, no `paired_with` and no observation exemption),
  or whose `paired_with` names an id that is not a row (RE-4);
- `deferred-expectation`: a row whose `expect` outcome is DEFERRED; it never holds while deferred
  (RE-1).

An invalid expectation file, record file, mutation record file or manifest schema is the finding
`file-invalid` and a gate ERROR (GATE_ERROR, exit 65). Otherwise the gate holds (GATE_HOLDS, exit 0).

A difference between an extracted figure and `reference` is reported as `reference-difference` and does
not change the verdict. Under sec. 31 it blocks acceptance of the implementation step until it is
explained. A status that a row's `status_allowed` admits as a limitation (R6.GATE.10) is reported as
`limitation-reported` and does not change the verdict.

The gate writes `gate-result.json` (schema `oi-control-gate/1`): one entry per row with the gate
status, the extracted actual and its findings. The status counts are reported separately; NOT RUN is
never counted as met.

A composite row (`composed_of`) preserves every component result: its entry in `gate-result.json`
lists each component's status and findings. Its aggregate status is the highest-ranked status among
its own record (where it has a runner) and its components, by the precedence ERROR > FAIL > NOT RUN
> PASS, so that an ERROR or FAIL of any component is never concealed by a component that is NOT
RUN. A composite whose aggregate is NOT RUN is NOT RUN with the release condition and release check
of each NOT RUN component, and is admitted only while each such NOT RUN is admitted; TR45 (component
TR45-opC) and EI14 (component EI14-dispatch) are such composites. A composite whose aggregate is FAIL
or ERROR fails as `status-not-allowed` (RE-30, Q14; GATE-28).
Sources: E-1190, Q1, VD-1, VD-10. Controls: GATE-1, GATE-2, GATE-3, GATE-4, GATE-9, GATE-10, GATE-12,
GATE-16, GATE-17, GATE-20, GATE-26, GATE-27, GATE-28, GATE-29.

**R6.GATE.10** Mutation evidence is gated. Each mutant of the mutation sets (`c1`, `c2`, `v60e`,
`cache` and `o9`) is a row `MUT:<set>:<mutant id>` of the expectation file; the `o9` set's mutant ids
are RDIR-m1 to RDIR-m17 (R6.CTRL.27). The mutation run distinguishes four states: killed, survived, not
applied and missing (no record).
- A row whose `status_allowed` is `["KILLED"]` holds only if the mutant is recorded KILLED with a
  non-empty `killed_by`.
- The known survivors `MUT:c2:D02`, `MUT:cache:K08`, `MUT:v60e:C08`, `MUT:v60e:H03`, `MUT:v60e:I06`,
  `MUT:v60e:P01` and `MUT:v60e:V05` allow SURVIVED, and the mutant `MUT:v60e:U01` allows NOT APPLIED;
  each is an explicit limitation tied to its named mutant, reported as `limitation-reported`.
- Any other survivor, any other mutant not applied, and any mutant whose status its row does not allow
  fails as `status-not-allowed`; a mutant with no record fails as `missing-id`.

The mutation harness and the list of mutant names land, pinned, with the tool revision; the MUT rows
then rest on the landed harness, not on CI provenance (RE-9 (a); RD-1). The survivors
`MUT:cache:K08`, `MUT:v60e:C08`, `MUT:v60e:I06` and `MUT:v60e:P01`, which have no equivalence argument,
are limitations and also verification defects, each with a distinguishing control: TR52-consumer
for C08, and one control each, added in the tool revision, for K08 (submodules in the path map), I06
(TR51's regular-files check) and P01 (the purity allowlist) (RE-10 (b); OBL-24).
Sources: RD-1, RD-5, Q8. Controls: GATE-21, GATE-22, GATE-23, GATE-24, MUT:c1:C01, MUT:c1:C02, MUT:c1:C03, MUT:c1:C04, MUT:c1:C05, MUT:c1:C06, MUT:c1:C07, MUT:c1:C08, MUT:c1:C09, MUT:c1:C10, MUT:c1:C11, MUT:c1:C12, MUT:c2:D01, MUT:c2:D02, MUT:c2:D03, MUT:cache:K01, MUT:cache:K02, MUT:cache:K03, MUT:cache:K04, MUT:cache:K05, MUT:cache:K06, MUT:cache:K07, MUT:cache:K08, MUT:o9:RDIR-m1, MUT:o9:RDIR-m10, MUT:o9:RDIR-m11, MUT:o9:RDIR-m12, MUT:o9:RDIR-m13, MUT:o9:RDIR-m14, MUT:o9:RDIR-m15, MUT:o9:RDIR-m16, MUT:o9:RDIR-m17, MUT:o9:RDIR-m2, MUT:o9:RDIR-m3, MUT:o9:RDIR-m4, MUT:o9:RDIR-m5, MUT:o9:RDIR-m6, MUT:o9:RDIR-m7, MUT:o9:RDIR-m8, MUT:o9:RDIR-m9, MUT:v60e:A01, MUT:v60e:A02, MUT:v60e:A03, MUT:v60e:A04, MUT:v60e:A05, MUT:v60e:A06, MUT:v60e:A07, MUT:v60e:A08, MUT:v60e:A09, MUT:v60e:A10, MUT:v60e:A11, MUT:v60e:A12, MUT:v60e:A13, MUT:v60e:A14, MUT:v60e:C01, MUT:v60e:C02, MUT:v60e:C03, MUT:v60e:C04, MUT:v60e:C05, MUT:v60e:C06, MUT:v60e:C07, MUT:v60e:C08, MUT:v60e:C09, MUT:v60e:C10, MUT:v60e:C11, MUT:v60e:C12, MUT:v60e:C13, MUT:v60e:C14, MUT:v60e:C15, MUT:v60e:C16, MUT:v60e:E01, MUT:v60e:E02, MUT:v60e:H01, MUT:v60e:H02, MUT:v60e:H03, MUT:v60e:I01, MUT:v60e:I02, MUT:v60e:I03, MUT:v60e:I04, MUT:v60e:I05, MUT:v60e:I06, MUT:v60e:I07, MUT:v60e:I08, MUT:v60e:I09, MUT:v60e:I10, MUT:v60e:I11, MUT:v60e:I12, MUT:v60e:I13, MUT:v60e:I14, MUT:v60e:O01, MUT:v60e:O02, MUT:v60e:P01, MUT:v60e:R01, MUT:v60e:R02, MUT:v60e:R03, MUT:v60e:U01, MUT:v60e:U02, MUT:v60e:U03, MUT:v60e:U04, MUT:v60e:U05, MUT:v60e:V01, MUT:v60e:V02, MUT:v60e:V03, MUT:v60e:V04, MUT:v60e:V05, MUT:v60e:V06, MUT:v60e:V07.

**R6.GATE.11** The acceptance list of the implementation step is the expectation file: every row is
recorded with a status its `status_allowed` admits, and the gate holds on the actual evidence (Q1). It
includes the record-directory controls RDIR-1 to RDIR-25 and RDIR-12b, RT-O9 and the item-2 controls
I2-1 to I2-8 (MC-13). The implementation of the corrections of the verification defects is a later,
separately authorized tool revision.
Sources: E-1461, MC-13, Q1. Controls: GATE-18.

### 16.6 Correspondence check

**R6.GATE.12** The gate checks the correspondence between r6 and the file in both directions:
- every row's `requirements` exist in r6's requirement list;
- every r6 requirement names at least one control id;
- every named id is a row or a `retired` entry;
- every row is named by some requirement.

The requirement list is the machine form of r6's requirement ids and their control lists, generated
from r6 and checked for drift. A row or requirement without a counterpart fails the check. A retired id
named as a live control also fails it. Requirements of a kind that no control can test (status,
definition, scope, governance and obligation statements) are listed with their kind in the requirement
list and are exempt from naming a control, provided each names its verification: `review`, or the
OBL ids that carry it, in the requirement list's field `verification`. A requirement of such a kind
that names no verification, and a testable requirement that names no control, fail the check
(RE-11 (a); GATE-8, GATE-30).
Sources: OD-2, Q1. Controls: GATE-7, GATE-8, GATE-30.

### 16.7 The gate's own controls

**R6.GATE.13** The gate's own controls are GATE-1 to GATE-30. Their expected verdicts are in the
expectation file; they are summarized here. The gate self-test runs them before the gate evaluates the
real records. A self-test failure is VOID (70).

| Id | Case | Expected verdict |
|---|---|---|
| GATE-1 | false actual value: a runner record with status PASS whose actual says exit 0 while the retained exit file and result.json say 20 | `declarative-mismatch` |
| GATE-2 | missing result: one id of the file has no record | `missing-id` |
| GATE-3 | duplicate id: two records carry one id (in one job, and separately across jobs) | `duplicate-id` |
| GATE-4 | unexpected id: a record whose id is not in the file | `unexpected-id` |
| GATE-5 | unauthorized NOT RUN: a row allowing only PASS reported NOT RUN with a reason | `status-not-allowed` |
| GATE-6 | weak runner predicate: A1r recorded PASS with a truthful actual (lint problems nonempty) while the retained result has no record-invalid item for the rule file | `declarative-mismatch` |
| GATE-7 | expectation row with no requirement: requirements empty, or naming an id absent from r6 | `correspondence-orphan-row` |
| GATE-8 | requirement with no control: an r6 requirement whose control list is empty or names an id absent from the file | `correspondence-orphan-requirement` |
| GATE-9 | raw evidence missing: a PASS record whose manifest names a result.json absent from the evidence set, or whose sha256 differs | `raw-evidence-missing` |
| GATE-10 | procedural predicate failed: SW1 tuples with one site carrying two new FAIL items while the runner records PASS | `procedural-failed` |
| GATE-11 | released NOT RUN: RT-L2 reported NOT RUN while its release check holds | `status-not-allowed` |
| GATE-12 | composite incomplete: S11-2 with S11-2c missing | `missing-id` |
| GATE-13 | RT-L2 drafted record: the run uses an unreviewed reconciliation record (drift state unresolved) | `procedural-failed` |
| GATE-14 | RT-L2 record bound to another M: reviewed record whose M blob differs from the run M | `procedural-failed` |
| GATE-15 | RT-L2 partial coverage: reviewed bound record covering one of two drifted paths | `procedural-failed` |
| GATE-16 | reference difference: RT-T0 with region_lines.count 214 against reference 215, every expect field met | holds, with `reference-difference` reported |
| GATE-17 | malformed expectation file: unknown schema id, unknown field, or NOT RUN allowed without reason and release condition | ERROR 65 (`file-invalid`) |
| GATE-18 | positive control: complete, correct records and evidence for a fixture with one row of each predicate kind and one allowed NOT RUN | holds |
| GATE-19 | RT-L2 reconciled: reviewed record bound to the exact H, M and C blobs covering every drifted path | holds |
| GATE-20 | status/actual inconsistency: runner status FAIL with an actual that meets expect | `status-actual-inconsistent` |
| GATE-21 | an unexpected survivor: a mutant whose row allows only KILLED recorded SURVIVED | `status-not-allowed` |
| GATE-22 | a missing mutant: a MUT row with no mutation record | `missing-id` |
| GATE-23 | a known survivor recorded SURVIVED and the not-applied mutant recorded NOT APPLIED (positive) | holds, with `limitation-reported` reported |
| GATE-24 | an unexpected not-applied mutant: a mutant whose row allows only KILLED recorded NOT APPLIED | `status-not-allowed` |
| GATE-25 | a double run whose two result files differ by one byte | `procedural-failed` |
| GATE-26 | a row with composed_of and its own runner record: the own record PASS, a component FAIL | `procedural-failed` |
| GATE-27 | direction missing: (a) a control row in the both-directions scope with no restored expectation, no direction both, no paired_with and no observation exemption; (b) a paired_with naming an id that is not a row | `direction-missing` |
| GATE-28 | composite precedence: (a) one component recorded FAIL and another an admitted NOT RUN; (b) the only non-PASS component an admitted NOT RUN | (a) `status-not-allowed`, the composite reported FAIL; (b) holds, the composite reported NOT RUN |
| GATE-29 | deferred expectation: a row whose expect outcome is DEFERRED, every other row holding | `deferred-expectation` |
| GATE-30 | correspondence exemption: (a) a status requirement with no control and no verification; (b) the same with verification review | (a) `correspondence-orphan-requirement`; (b) holds |

Sources: Q1, Q8, RD-2. Controls: GATE-1, GATE-2, GATE-3, GATE-4, GATE-5, GATE-6, GATE-7, GATE-8, GATE-9, GATE-10, GATE-11, GATE-12, GATE-13, GATE-14, GATE-15, GATE-16, GATE-17, GATE-18, GATE-19, GATE-20, GATE-21, GATE-22, GATE-23, GATE-24, GATE-25, GATE-26, GATE-27, GATE-28, GATE-29, GATE-30.

### 16.8 CI under sec. A.44

**R6.GATE.14** The gate is its own job step, after the runner steps, in the pinned workflow. It reads
only structured data:
- the runner steps' exit files;
- `control-records.json` and `mutation-records.json`;
- the evidence manifests and files in the run's own artifact directory;
- the expectation file and the requirement list at the commit under check.

It never parses log text. The step's exit status is the verdict. A marker step named for the fact it
records ("control expectations hold") carries the step conclusion. Runner steps may exit nonzero by
design (a control that ends in NOT RUN, or a negative-path step); the gate reads their structured
records, not their badge. The gate's output and the evidence digest are uploaded as artifacts and
recorded as provenance (sec. A.42 item 2).
Sources: V2-098, Q1. Controls: GATE-18.

### 16.9 NOT RUN rule and RT-L2

**R6.GATE.15** `NOT RUN` is allowed only where the row lists it, with a reason and a release
condition, and only while the row's `release_check` is false on the commit under check. The rows that
admit NOT RUN are RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opC and EI14-dispatch. RT-O9 is gated: its
own record-directory checks run, and only its dependent clause, RT-O9-L2, is NOT RUN while RT-L2 is
NOT RUN (Q6). RT-T is NOT RUN until the reviewed records it needs exist.
The composites TR45 and EI14 are NOT RUN by inheritance while their component is (R6.GATE.9).
EI14-dispatch's release condition is a dispatch of the pinned workflow on a branch holding `T'`,
after the tool lands, under a launch the owner approves (AGENTS.md sec. A.50, sec. A.51 item 4); it
gates acceptance of a chain-admitted result in the A1 retirement execution (RE-21; OBL-18).
Sources: V1-121, E-1190, Q6, RD-6, RD-7, RD-25, RD-26. Controls: GATE-5, GATE-11, RT-T, TR5, G-A1,
RT-L2, RT-O9, RT-O9-L2, TR45-opC, EI14-dispatch, TR45, EI14.

**R6.GATE.16** RT-L2 is three-valued:

| Result | Condition | Verdict |
|---|---|---|
| no drift | no `base-drift` at the predicted `M` | PASS |
| validly reconciled | every drifted path is covered by a reviewed reconciliation record whose review passes record lint and which is bound to the exact `H`, `M` and `C` blobs of the run | PASS |
| unresolved | anything else, including a drafted or unreviewed record | FAIL |

RT-L2 is NOT RUN until a reviewed record exists. The RT-L2 PASS recorded by CI run 45569710442, made on
a drafted record, does not establish the safeguard (sec. 31).
Sources: OD-18, Q2. Controls: RT-L2, GATE-13, GATE-14, GATE-15, GATE-19.

### 16.10 Annex: invariant vocabulary

The closed vocabulary of `invariants` keys is the following list of the 153 keys the
expectation file uses (R6.GATE.3). A key outside it makes the file invalid.

`L_blob`, `X_and_M_views_differ`, `a3_a5_evaluated`, `a5_evaluated`, `a5_unequal_paths`, `acceptable_as_new_run`,
`added_relative_to_unmutated`, `admission_mode`, `admission_mode_not`, `all`, `arm`, `baseline`,
`before_host_read`, `before_unloaded_import`, `blob_at_L`, `byte_identical`, `bytes_read_before_type_check`, `cached_map_equals_ls_tree_in_both_orders`,
`cached_paths_name_the_blob`, `candidate_and_landing_pass`, `checkers_run_from`, `class_meaning_table_equal_in_every_result`, `class_route_entry_stands`, `classed_items_missing_meaning`,
`classed_items_quoting_meaning_min`, `clean_path`, `clone_checked_out`, `clones`, `commit_paths_classified`, `compare_by`,
`component_results_preserved`, `composed_blob`, `composite_status`, `composition_evaluated`, `condition`, `config_in_landing`,
`countercontrol_class_review_landed_cycle`, `countercontrol_config_landed_cycle`, `directory_admitted`, `distinct_maps_for_distinct_trees`, `drift_state_in`, `each_listed_line`,
`each_with`, `entry_exit`, `entry_point_ran`, `equal_across`, `equal_field`, `equals`,
`error_result_carries_table`, `evaluated_in`, `every_record_verifies`, `evil_ran`, `existing_conformance_controls_unchanged`, `exit_not_in`,
`failed_conditions_include`, `file_executed`, `finding_value`, `findings`, `fixture`, `git_honours_graft`,
`git_status_porcelain_empty`, `harness_dir_files`, `has`, `have`, `hit_at_offset_in_image`, `hit_profiles_include`,
`holds`, `host_calls`, `imported_files_within`, `in_memory_commits_own_map`, `index_unchanged`, `inputs_equal`,
`items_equal_run_without_file`, `items_include`, `killed_by`, `killed_by_nonempty`, `landing_record_lists`, `lint_problems`,
`linted_paths_include`, `mappings_unchanged`, `marker_written`, `message_names`, `module_init_ran`, `mutated_literal`,
`mutated_literal_rule`, `mutation_attempts_refused`, `names_commit`, `names_edit`, `negative_example_matches_widened_rule`, `new_reader_refused_with`,
`no_error`, `no_exception`, `no_group_error`, `no_result_with_outcome`, `no_result_written`, `no_stop`,
`none`, `not_class`, `not_in_H_to_M_scan`, `nothing_cached_by_a_refusal`, `objects_fetched`, `old_style_X_vs_M_comparison_reports`,
`others_class`, `out_dir_created`, `payload_ran`, `per_failed_check`, `per_operation`, `per_site`,
`rc11_evaluated`, `reader_cases_refused_with`, `reason`, `record_admitted`, `record_checks_failed_include`, `record_directory_entries_equal`,
`record_directory_state`, `reference_graph_cycle`, `refs_unchanged`, `refused`, `replay_equality`, `representative_candidate`,
`resid_key`, `restored_of_each_component`, `result_equal_without_file`, `results_validated_min`, `retired_lines_count`, `rt_l2_status`,
`rule_active`, `same_reader_path_map_unchanged`, `same_reader_serves_verified_bytes`, `same_view_returned`, `scanned_paths_within`, `schema_errors`,
`selected_offset`, `self_test_imports_all_accepted`, `side_change_obligation`, `side_changes_classified_by`, `side_changes_exact`, `sites_resolved_by_it`,
`snapshot_T_recorded`, `snapshot_fields_all_present`, `source_map_nonempty`, `stderr_json_outcome`, `stop_class_in`, `superseding_record_used`,
`supplied_file_read_as_evidence`, `terms_and_execution_equal_clean`, `tool_and_workflow_blobs_equal_pins`, `tool_run_exit`, `value`, `value_occurs_in`,
`value_set_includes`, `walk_terminates`, `writes_only_under`.

***

## 17. Control catalogue

This section states the rules every control obeys and lists every control id. The expected result of
each control is stated once, in the expectation file of schema `oi-control-expectations/1` (sec. 16).
Nothing in this section is an expected result. Case descriptions name what a control constructs or
runs; they are not expectations. In this section `{at}` stands for the commercial at character.

**R6.CTRL.1** The control catalogue is Table 17.1. It holds one row for every live control id: the id,
the requirement ids the control tests, the runner (`file:line` of the runner predicate at the tool
commit, or the statement that no runner implements it yet), the predicate kind (`declarative` or
`procedural`, sec. 16), the declared direction or directions, and the case. Every control row of the
expectation file appears in Table 17.1 and every row of Table 17.1 appears in the expectation file;
the correspondence check of sec. 16 verifies both directions. Mutant rows (R6.CTRL.27) are not
controls of Table 17.1; Table 17.2 lists the record-directory mutants, and the expectation file
enumerates the mutants of the other sets. The unit and mutation controls are no
longer stated by reference to an earlier design: each is restated here, and its expected result is
the expectation file's. The requirement ids of Table 17.1 are the numbered requirements that name the control.
Sources: E-1082, V1-085, V2-070, E-1311, E-125. Controls: GATE-7, GATE-8, GATE-12.

**R6.CTRL.2** Control ids are identifiers, unique across the expectation file, and never reused for a
different control. A control renamed under the identifier migration of sec. 34 keeps its meaning; its
row records the old id in `migrated_from`: the v2 four-tree controls R1-R14 are TT1-TT14, the v2
provenance controls P1-P3 are H1-H3, r5's directory controls O9-1 to O9-25 and O9-12b are RDIR-1 to
RDIR-25 and RDIR-12b, and r5's mutants O9-m1 to O9-m17 are RDIR-m1 to RDIR-m17. R15-R19, RT-O9 and N4
keep their ids. Review-finding labels (for example B1-B6 as findings, S2-S7, V3, R9) are not control
ids; where cited they are quoted in prose. A control id split into separately recorded halves gives
each half its own id (EI2-consumer, EI7-tool, EI7-consumer, GV6-disk, GV7-tool, GV7-consumer,
TR14-tool, TR28-tool, TR28-consumer, TR29-tool, TR45-opB, TR45-opC, EI14-dispatch, RT-D-gr58,
V27-glossary, RT-O9-L2), recorded in the migration index; where the expectation file keeps the
parent id as a row, that row is either the remaining cases of the parent or a `composed_of` row that
holds only when every component holds (EI7, GV7, S11-2, TR28 and TR45 are composite). A retired control id
appears only in the expectation file's `retired` array, with the disposition of its underlying
requirement (sec. 33); naming a retired id as a live control fails the correspondence check.
Sources: V2-090, V2-091, V2-092, RV-056. Controls: GATE-3, GATE-4, GATE-12.

**R6.CTRL.3** Both directions. The rule that a control runs in both directions reaches the controls of
v6.0e sec. 10, with v1's unit and mutation controls, which sec. 10 keeps, and every control a source
places under it: the four-tree and reconciliation controls of v6.0e sec. 13.2 (TT1-TT14, R15-R19
with R18-engine and R19-engine, N3-N18 with N3-config-route, N16-file and N18-record, RT-X, RT-L and
RT-L2), the role tests of v2 addendum 2, and v1's mutation demonstrations RT-M and RT-SHIFT
(RE-3 (c)). An adversarial control states its mutant and also a restored case, in which the unmutated
input returns the control outcome; a positive control states a countercase on which its predicate
must not hold. Mutation controls run the mutant and the restored tree. The expectation file records
the second direction of each row in scope by direction `both`, by a `restored` expectation, or by
`paired_with`, naming the row that runs the same input and differs only in the mutation (RE-2 (c),
RE-4). A row in scope that applies no mutation and asserts no acceptance of a valid input, an
observation of unmodified inputs, is exempt; its `direction` records `exempt: "observation"` with the
reason checked for that row (RE-2 (b), Q11). Every positive control that asserts acceptance of a
valid input keeps a required opposite direction. A row in scope that records no second direction is
a verification defect that the gate reports as `direction-missing` (R6.GATE.9); a row whose stated
restored case, or whose paired row, is not executed is a verification defect (VD-RESTORE); each is
corrected in the tool revision (OBL-20) and neither is ever accepted as satisfying this requirement.
A row outside the scope that has no second direction records `scope: "outside"` with its reason;
mutant rows and the gate's own controls are outside the rule by their namespace. At the final
expectation file, of 420 control rows 267 are in scope and 153 outside; 223 rows carry a `restored`
expectation, 41 declare direction `both`, 6 name `paired_with` and 3 are exempt as observations;
42 rows in scope record no second direction (`direction-missing`), and 217 rows are flagged VD-RESTORE.
Sources: V1-101, V2-073, V1-138, Q7, RE-2, RE-3, RE-4, Q11. Controls: A11r, M1, N1, GATE-27.
**R6.CTRL.4** Each expected FAIL names the class of sec. 15 that produces it; a FAIL expectation
without a class is a defect of the expectation (G3, G5 and the countercontrols of sec. 18 items 4, 6
and 13 name their class). Each expected deny FAIL names the deny rule and the rule alternative that
produces it, as measured on the control's own text. Each countercontrol of a deny rule asserts the
target rule id on the named line or sentence, not only the outcome of the run.
Sources: E-1009, RV-052. Controls: RT-DR, RT-DR3W, A5r, V1, V2, V3, G3, G5, S11-4, S11-6, S11-13.

**R6.CTRL.5** A runner records each control with status PASS, FAIL or NOT RUN. A status of SKIP does
not exist: a control that is deliberately not run is NOT RUN. NOT RUN is admitted only for a row whose
expectation lists it together with a reason and a release condition, and only while that release
condition is false; a summary never counts NOT RUN as met. The rows that admit NOT RUN are RT-T, TR5,
G-A1, RT-L2, RT-O9-L2, TR45-opC and EI14-dispatch, and, by inheritance from those components, the
composites TR45 and EI14 (R6.GATE.9).
Sources: V2-073. Controls: RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opC, EI14-dispatch, GATE-5,
GATE-11, TR45, EI14.

**R6.CTRL.6** Unit, mutation and adversarial controls run on synthetic trees held in memory. The V
controls are splices adding the stated text to the stated file (added text) unless the case says
otherwise. Real-tree controls run on real objects in CI. Synthetic cases are read through the same
verified object reader as real ones.
Sources: V1-085, V2-073, E-1105. Controls: U1, M1, V1, RT-A.

**R6.CTRL.7** A control-only input is a pinned object (commit, path, git blob id and sha256) named by
one control in the controls file. It is read only by the control that names it, changes no profile's
scope and no production result, and adding or changing one changes the controls file and is reviewed
with it. No historical text is constructed for this purpose. DR-3's witness is such an input: the
sentence of `AGENTS.md` at `H`, lines 37-39 (blob 12a9281fb88c14395b6715a3bf4b4f6b030f433c, sha256
d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27), which RT-DR3W scans at `H` and,
as its countercontrol, in `X_rep` (R6.EVID.8), whose `AGENTS.md` is `H`'s with the ledger's splices
applied.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1011, E-1013, E-1014, E-1015, OC-3. Controls: RT-DR3W.

**R6.CTRL.8** The preflight set is U1, U4, U10, M1, K1, O9 and O1. Every run of an operation runs the
preflight controls in memory in the controls stage, before any subject is evaluated; a preflight
failure ends the run VOID (exit 70) without evaluating. U2 and U3 remain self-test controls.
Sources: V1-072. Controls: U1, U4, U10, M1, K1, O9, O1.

**R6.CTRL.9** The unit controls are U1-U12 and U14, each restated in the classes and exit codes of
sec. 7 and sec. 15 as the runner implements them. v1's result HOLDS becomes PASS (exit 0), FAILS
becomes FAIL (exit 20), and FAILS `unmapped-hit` becomes REVIEW_REQUIRED (exit 10) `unclassified`
(U12). U2 asserts the site's `line_delta`; U10 asserts the splice ids and the per-splice `old_sha256`
and `new_sha256`; U9 asserts `whitespace_only` as a diagnostic defined in sec. 7. U13 is retired with
the `read` route, and U15 is retired, its case kept as U14's wrong-region-hash case (sec. 33). U14 is restated as the
positive HP adjudication case of R6.CTRL.16.
Sources: V1-086, V1-087, V1-088, V1-089, V1-090, V1-091, V1-092, V1-093, V1-094, V1-095, V1-096, V1-097, V2-070, V2-071, E-1082. Controls: U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11, U12, U14.

**R6.CTRL.10** The mutation controls are M1-M11, each restated in the classes and exit codes of
sec. 7. v1's ERROR 2 becomes USAGE (exit 64) with nothing written (M10); v1's ERROR 3 becomes ERROR
(exit 65) with the class the pinned-input role rule of sec. 7 assigns (M3 and M4 `LEDGER_INTEGRITY`, M5
`SCIENTIFIC_BASE_MISMATCH`, M9 `RECORD_TREE_MISMATCH`); M7 and M8 are integrity ERRORs (exit 65) with
the named replay equality (`build` for M7, `render` for M8) false; M11 asserts exit 65, not a raised
exception. Each mutation control runs in both directions: the mutant gives its stated outcome and the
restored tree its control outcome.
Sources: V1-102, V1-103, V1-104, V1-105, V1-106, V1-107, V1-108, V1-109, V1-110, V1-111, V1-112, V1-132, V1-134. Controls: M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11.

**R6.CTRL.11** Two real-object demonstrations are controls in their own right: RT-M (mutation M1
applied to the in-memory T1' `papers/Main.md` under RT-T0's run) and RT-SHIFT (a shift-only mutant of
`E`, one blank line prepended in memory to `papers/Main.md` and to the FULL book file). The count of
site lines that RT-T0 resolves as moved by authorized splices elsewhere in their files is an asserted
quantity of RT-T0, not an informational figure. The per-site meaning mutant of `E` is generalized by
SW1, which deletes one token from each site at `E`.
Their expected results are the expectation file's, taken from their cited sources V1-120 and V1-124
(B-18).
Sources: V1-120, V1-122, V1-123, V1-124, V1-125, V1-126. Controls: RT-M, RT-SHIFT, RT-T0, SW1.

**R6.CTRL.12** Three controls test determinism and confinement. REPRO-DOUBLE runs one operation twice
on the same inputs into two fresh `--out` directories and compares the results byte for byte.
REPRO-PYVER builds the anchors and the sitemap under two supported Python versions and compares them.
OUT-CONFINED takes the tree listing and the git state of the clone before and after a run and
requires that nothing is written outside `--out` and that the clone is left clean.
Sources: V1-131. Controls: REPRO-DOUBLE, REPRO-PYVER, OUT-CONFINED, M10.

**R6.CTRL.13** No code path resolves a site by line-number proximity or by a similarity score; the
requirement is stated with the anchors (sec. 4) and is tested by U5, U6, U7 and by the controls of the
two anchor defects: VD2-HP-SEARCH (an adjudicated HP site in a ledgered segment whose file is
non-conforming, or has an unledgered change, is searched and yields its site-level item) and
VD3-COUNT and VD3-CONTEXT (the duplicate rule of sec. 4 applied to a pin-duplicated line in a
ledgered segment). An inspection of the code for such resolution is not a control.
Sources: V1-135. Controls: U5, U6, U7, VD2-HP-SEARCH, VD3-COUNT, VD3-CONTEXT.

**R6.CTRL.14** The rule controls are L1-L4, V1-V27 (V7a, V7b, V7c; no V8), A1r-A12r, S1r, S2r,
WB1-WB15, N-W, their engine analogues and the rule-lint controls. v2's class `rule-invalid` is
`record-invalid` (exit 20) throughout. V2 FAILs by DR-3 and V3 by DR-4; v2's fingerprint-mismatch and
residual-test basis for them is superseded, since no rule deletes text and overlap is strict (sec.
10). V1 FAILs by DR-1, alternative b. The deny rules and the seed allow rules are plan records adopted
with the amended plan; the controls use the current rule files as pinned control inputs and test the
rule mechanism (sec. 12).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1106, E-1107, E-1108, E-1109, E-1110, E-1111, E-1112, E-1113, E-1114, E-1115, E-1116, E-1117, E-1118, E-1119, E-1120, E-1121, E-1122, E-1123, E-1124, E-1125, E-1126, E-1127, E-1128, E-1129, E-1130, E-1131, E-1132, E-1133, E-1135, E-1136, E-1137, E-1138, E-1139, E-1140, E-1141, E-1142, E-1143, E-1144, E-1145, E-1146, E-1147, E-1148, E-1149, E-1150, E-1151, E-1192, E-1193, E-1194, E-1195, E-1196, E-1197, E-1198, E-1199, E-1200, E-1201, E-1202, E-1203, E-1204, E-1205, E-1206, E-1232, V2-074, V2-075, V2-076, V2-077, V2-078, V2-079, V2-081, V2-082, V2-083, V2-084, V2-085, V2-086, V2-087, V2-088, V2-089, RV-050, RV-052. Controls: A1r, A2r, A3r, A4r, A5r, A5r-generic, A6r, A7r, A8r, A9r, A10r, A11r, A12r, E-A1r, E-A2r, E-A3r, E-A6r, E-A8r, E-L1, E-L3, E-S1r, E-S2r, L1, L2, L3, L4, S1r, S2r, V1, V2, V3, V3-countercontrol, V4, V5, V6, V7a, V7b, V7c, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V27-glossary, WB1, WB2, WB3, WB4, WB5, WB6, WB7, WB8, WB9, WB10, WB11, WB12, WB13, WB14, WB15, lint-ok, rule-negative.

**R6.CTRL.15** V4 adds "the framework's sixth structural property, finiteness of the bijection" to
the file of a W1 rule. Under the deny set without DR-2 the sentence produces no hit, so the run is
PASS: this is the V4 reversal. What it permits: a reintroduction of the counted premise in the form
"sixth structural property, finiteness of ..." passes the deny profiles and the residual profile
unclassified by any FAIL, and the original item 7 misses it as well. Its consequence: the tool does
not detect that form, and detection rests on review of the residual hits. The reversal rests on an
owner decision recorded only in paraphrase. It is adopted or rejected by the owner at r6's adoption;
approving this draft does not adopt it. Until that decision, V4, V27, V27-glossary and V15 each
carry both candidate expectations, marked "not authoritative; decided at r6 adoption", and the gate
reports `deferred-expectation` for each (RE-1). If the reversal is rejected, V4's expectation is FAIL `deny-match` and the deny set
needs a rule matching that form, which is a plan-record change (sec. 12). V27 tests a sentence of the
same form and rests on the same decision, as do V27-glossary and V15, whose candidates are
REVIEW_REQUIRED `unclassified` and FAIL `deny-match`.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: V2-080, RE-1. Controls: V4, V27, V27-glossary, V15.

**R6.CTRL.16** The provenance controls are H1-H7 (H1-H3 restate v2's P1-P3), U14 and RECLINT-ORPHAN.
U14 is a positive HP adjudication case: a synthetic HP site whose provenance walk a reviewed HP
adjudication record matches, counted as `provenance-adjudicated`; its second case gives the entry a
wrong region hash and expects exactly FAIL `provenance-mismatch` and FAIL `stale-adjudication`
(R6.HP.7). RECLINT-ORPHAN plants a referenced HP adjudication record entry that matches no subject on
a tree and segment its record applies to (FAIL `stale-adjudication`), an orphan context adjudication
or hit classification entry and a duplicate entry (FAIL `record-invalid`), and the same entries on a
tree or segment the record does not apply to (no finding) (R6.REC.10). An adjudication that disagrees
with the walk, or changes a row, FAILs (H1, H2, H6).
Sources: E-1098, E-1099, E-1100, E-1101, E-1102, E-1103, E-1104, Q12, RE-8. Controls: H1, H2, H3, H4, H5, H6, H7, U14, RECLINT-ORPHAN.
**R6.CTRL.17** Split and dependent rows. RT-O9's own checks (the expected set of record-directory
entries computed independently from the stand-in `F` tree, compared exactly; no unequal path; no
`side-change-unclassified`) run and are gated whenever RT-O9 runs, independently of RT-L2. Its clause
that RT-L2 still holds is the separate row RT-O9-L2, which depends on RT-L2 and is NOT RUN with
RT-L2's release condition. TR45's op-C half is the row TR45-opC, NOT RUN until delegated evidence is
recorded by native runs at `X` and `C`. EI14's branch-dispatch half is the row EI14-dispatch, NOT RUN
until a dispatch of the pinned workflow on a branch holding `T'` is made, after the tool lands, under
a launch the owner approves; EI14's other cases stay in EI14. The consumer halves of EI7, TR15, TR50,
TR51 and TR52 are rows of their own (EI7-consumer, TR15-consumer, TR50-consumer, TR51-consumer,
TR52-consumer), implemented in the tool revision; until then the gate reports them missing.
Sources: E-1218. Controls: RT-O9, RT-O9-L2, TR45-opB, TR45-opC, EI14, EI14-dispatch, EI7,
EI7-consumer, TR15-consumer, TR50-consumer, TR51-consumer, TR52-consumer.

**R6.CTRL.18** The context controls are K1-K10 and the splice-boundary controls are B1-B6. K4's
predicate tests both of its halves (the K1 half and the K2 half).
Sources: E-1083, E-1084, E-1085, E-1087, E-1088, E-1089, E-1090, E-1091, E-1092, E-1093, E-1094, E-1095, E-1096, E-1097, E-1245. Controls: B1, B2, B3, B4, B5, B6, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10.

**R6.CTRL.19** The real-tree controls run in CI on real objects: RT-A, RT-E, RT-H0, RT-T0, RT-T, RT-C,
RT-D, RT-D-gr58, RT-DR, RT-DR3W, RT-I7, RT-I7A, SW1, SW2, item11-T1p, N-W, RT-M, RT-SHIFT, RT-X, RT-L,
RT-L2, RT-O9 and RT-O9-L2. v1's `verify-record` is `record` and `check-coverage` is `coverage`. Every
figure a runner asserts today that is reproducible from inputs on `main` (among them RT-H0's 113/7/7,
RT-A's and RT-E's 697, the RT-DR counts at `H`, RT-T0's site and region counts, RT-I7's split at `H`,
RT-I7A and RT-C, and RT-D's 45 `resid` lines) is an asserted count in the expectation file, not an
informational figure. A control whose verdict reads only what `H` and the ledger determine runs on
`X_rep` (R6.EVID.8); a figure that needs T1' itself is an acceptance reference only for a run that has
T1' among its inputs; its standing as evidence follows sec. 31. RT-C is PASS only with contract
evidence; without it the expected result is the one the expectation file states for missing
evidence. RT-T is NOT RUN until every reviewed record of sec. 14 exists. The two `not determined`
H..T1' cases of sec. 6 are RET FAILs, and RT-T's expectation says so; it does not claim that no RET
FAIL exists.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1134, E-1176, E-1177, E-1178, E-1179, E-1180, E-1181, E-1182, E-1183, E-1184, E-1185, E-1186, E-1187, E-1188, V1-115, V1-117, V1-119, V2-099, V2-100, V2-101, V2-103, V2-104, V2-105, V2-162, V2-163, V2-164, RV-028, RV-051, E-091, E-1010, V1-132, V1-136, OC-3. Controls: N-W, RT-A, RT-C, RT-D, RT-D-gr58, RT-DR, RT-DR3W, RT-E, RT-H0, RT-I7, RT-I7A, RT-L, RT-L2, RT-O9, RT-O9-L2, RT-T, RT-T0, RT-X, SW1, SW2, item11-T1p.

**R6.CTRL.20** The tree-role controls are TT1-TT14, R15-R19 with their engine forms, RL and
SIDE-NONREG, and the real-tree controls RT-X, RT-L and RT-L2, each read with `C` for the certified
head. v2's `unrelated-authorized` is read as "classified by a side-change class record, or
`record-directory`", and obligation `MAIN` is kept (sec. 20). TT2 runs v2's old-style comparison of
`X` against `M` as a countercontrol. TT7 asserts its landing run under the computed composition. TT8
asserts PASS. TT12 names its class. TT14 is evaluated in the landing check of the tool's own pull
request (sec. 19). The role tests of v2 addendum 2 map to TT1, TT13 (op C on a correctly executed
candidate), TT3, TT4, TT7, TT8, TT9, R15 (a first parent other than the recorded `M`), R16 (an
unclassified path in a commit of `C`) and R18, R19, RDIR-5 (an unclassified change on `M`).
Sources: E-1230, E-1231, E-1321, E-1329, V2-149, V2-150, V2-151, V2-152, V2-153, V2-154, V2-155, V2-156, V2-157, V2-158, V2-159, V2-160, V2-161, V2-148, E-1311, RV-ADD2-259-269. Controls: R15, R16, R17, R18, R18-engine, R19, R19-engine, RL, SIDE-NONREG, TT1, TT2, TT3, TT4, TT5, TT6, TT7, TT8, TT9, TT10, TT11, TT12, TT13, TT14.

**R6.CTRL.21** The reconciliation controls are N2-N18 with N3-config-route, N16-file, N18-record and
R8-S6. Each condition RC1-RC13 of sec. 23 has its own control: N5 (RC1), N7 (RC2), N12 (RC3), N8
(RC4), N13 (RC5), N14 (RC6), N9 (RC7), N15 (RC8), N6 (RC9), N16 (RC10), N17 (RC11), N18 (RC12) and N4
(RC13).
Sources: E-1152, E-1153, E-1312, E-1313, E-1314, E-1315, E-1316, E-1317, E-1318, E-1319, E-1320, E-1322, E-1323, E-1324, E-1325, E-1326, E-1327, E-1328. Controls: N1, N2, N3, N3-config-route, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15, N16, N16-file, N17, N18, N18-record, R8-S6.

**R6.CTRL.22** The record controls are O1-O9 (O4 retired), N1, S4a, LN1-LN8 and LN10 (LN9 retired),
and the record-lint controls R3-F2, R4-B3, R4-B3-DUP, R5-N6 and R6-G6. O1, O2, O3, O5 and O7 assert
an emitted FAIL `record-invalid`, not only a lint problem; O6 asserts the emitted outcome, not only the
absence of an ERROR.
Sources: E-1154, E-1155, E-1156, E-1157, E-1158, E-1159, E-1160, E-1161, E-1331, E-1332, E-1333, E-1334, E-1335, E-1336, E-1337, E-1338, E-1339, E-1340. Controls: LN1, LN2, LN3, LN4, LN5, LN6, LN7, LN8, LN10, O1, O2, O3, O5, O6, O7, O8, O9, R3-F2, R4-B3, R4-B3-DUP, R5-N6, R6-G6, S4a.

**R6.CTRL.23** The delegation controls are G1-G9 and G-A1; the output controls are X1-X11,
S7-schema-and-checker, ACCEPT-SCHEMA and B4-MEANING; the admission, execution-identity and
object-integrity controls are TR1-TR3, TR5, TR5-sim, TR13-TR15, TR14-tool, TR28-tool, TR28-consumer,
TR29, TR29-tool, TR30, TR45-opB, TR45-opC, TR46, TR48, TR50-TR52 and their consumer halves, EI1-EI15
with EI2-consumer, EI7-tool, EI7-consumer and EI14-dispatch, GV1-GV7 with GV6-disk, GV7-tool and
GV7-consumer, the cache controls GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE and GV-CACHE-KEY,
CHAIN-REFUSAL, ADM-CONFIG-AT-F, CONFIG-LINT, O3-FILTER and K1-GRAPH. v1's RT-A' (op A with `--pin H`)
is X1. GV4 includes the HP-merge case; EI6 includes its third case and the `json.py` and
`importlib.py` shadow files; EI5 and EI7 include their countercontrols. TR1 applies to chain
admission only.
Sources: E-1162, E-1163, E-1164, E-1224, E-1225, E-1226, E-1227, E-1228, E-1229, E-1165, E-1166, E-1167, E-1168, E-1169, E-1170, E-1171, E-1172, E-1173, E-1174, E-1207, V2-096, V2-097, E-1208, E-1209, E-1210, E-1211, E-1212, E-1213, E-1214, E-1215, E-1216, E-1217, E-1219, E-1220, E-1221, E-1222, E-1223, E-1246, E-1247, E-1248, E-1249, E-1250, E-1251, E-1252, E-1253, E-1254, E-1255, E-1256, E-1257, E-1258, E-1259, E-1260, E-1261, E-1262, E-1263, E-1264, E-1265, E-1266, E-1267, V1-116. Controls: G1, G2, G3, G4, G5, G6, G7, G8, G9, G-A1, ACCEPT-SCHEMA, B4-MEANING, S7-schema-and-checker, X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11,
ADM-CONFIG-AT-F, CHAIN-REFUSAL, CONFIG-LINT, EI1, EI2, EI2-consumer, EI3, EI4, EI5, EI6, EI7, EI7-consumer, EI7-tool, EI8, EI9, EI10, EI11, EI12, EI13, EI14, EI14-dispatch, EI15, GV1, GV2, GV3, GV4, GV5, GV6, GV6-disk, GV7, GV7-consumer, GV7-tool, GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE, GV-CACHE-KEY, K1-GRAPH, O3-FILTER, TR1, TR2, TR3, TR5, TR5-sim, TR13, TR14, TR14-tool, TR15, TR15-consumer, TR28-consumer, TR28-tool, TR29, TR29-tool, TR30, TR45-opB, TR45-opC, TR46, TR48, TR50, TR50-consumer, TR51, TR51-consumer, TR52, TR52-consumer.

**R6.CTRL.24** The plan-mapping controls are S11-1 to S11-14 (S11-2 composed of S11-2a, S11-2b and
S11-2c) and the per-edit controls S11-56, S11-57a-d, S11-58a-f and S11-58g-k. S11-56 tests the tool's
side only: the equality of its result with the plan's own checker is an outstanding obligation (sec.
18). S11-7 is implemented in the tool revision; it plants a literal and a DR-5 match and requires both
to FAIL.
Sources: E-1234, E-1235, E-1236, E-1237, E-1238, E-1239, E-1240, E-1241, E-1242, E-1243, E-1244, E-125. Controls: S11-1, S11-2, S11-2a, S11-2b, S11-2c, S11-3, S11-4, S11-5, S11-6, S11-7, S11-8, S11-9, S11-10, S11-11, S11-12, S11-13, S11-14, S11-56, S11-57a, S11-57b, S11-57c, S11-57d, S11-58a-f, S11-58g, S11-58h, S11-58i, S11-58j, S11-58k.

**R6.CTRL.25** The synthetic configuration controls are Y1-Y10, Z1-Z8, Z6b, Z9a-Z9h, Z9-STAGED, Z10
and Z11. Each of Z1-Z8 gives one defect of the fail-closed validation table of sec. 29 in the
synthetic configuration: Z1 an unknown schema, Z2 a missing required field, Z3 an unknown field, Z4
an operation not in `operations`, Z5 a reviewer equal to the author, Z6 an unknown adapter interface
version, Z7 a configuration inconsistency (three cases), Z8 an absent controls file; Z6b gives the
withdrawn argument `--config-sha256`. Z9h's case is the one in Table 17.1, which combines both of its
earlier statements. Z9-STAGED is the record of the staged purity job (its record id is `outcome`
today).
Sources: E-1233, E-1330, E-1381, E-1382, E-1383, E-1384, E-1385, E-1386, E-1387, E-1388, E-1439, E-1440, E-1441, E-1442, E-1443, E-1444, E-1445, E-1446, E-1447, E-1448, E-1457, E-1458. Controls: Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Z1, Z2, Z3, Z4, Z5, Z6, Z6b, Z7, Z8, Z9-STAGED, Z9a, Z9b, Z9c, Z9d, Z9e, Z9f, Z9g, Z9h, Z10, Z11.

**R6.CTRL.26** The record-directory controls are RDIR-1 to RDIR-25 and RDIR-12b (sec. 21), each a
separate synthetic case with `F` and `M` built by the synthetic fixture and the admitted record
directory used as `D_rec` unless the case says otherwise, and the item-2 controls I2-1 to I2-8 (sec.
22). The record-directory controls belong to the acceptance list of the tool's implementation step,
together with RT-O9 and I2-1 to I2-8.
Sources: A-061, A-062, A-063, A-064, A-065, A-066, A-067, A-068, A-069, A-070, A-071, A-072, A-073, A-074, A-075, A-076, A-077, A-078, A-079, A-080, A-081, A-082, A-083, A-084, A-085, A-086, A-120, A-121, A-122, A-123, A-124, A-125, A-126, A-127, A-060. Controls: I2-1, I2-2, I2-3, I2-4, I2-5, I2-6, I2-7, I2-8, RDIR-1, RDIR-2, RDIR-3, RDIR-4, RDIR-5, RDIR-6, RDIR-7, RDIR-8, RDIR-9, RDIR-10, RDIR-11, RDIR-12, RDIR-12b, RDIR-13, RDIR-14, RDIR-15, RDIR-16, RDIR-17, RDIR-18, RDIR-19, RDIR-20, RDIR-21, RDIR-22, RDIR-23, RDIR-24, RDIR-25.

**R6.CTRL.27** Mutation evidence is checked by the gate. Each mutant of the mutation sets at the tool
commit (`c1`, `c2`, `v60e`, `cache` and `o9`) is a row of the expectation file in its own namespace,
with the id `MUT:<set>:<mutant id>`; the `o9` set's mutant ids are RDIR-m1 to RDIR-m17. Each mutant row
names the change, the controls that distinguish it, and the result of each such control on the correct
implementation and on the mutant. The mutation run records one of four states for each mutant:
killed, survived, not applied, or missing (no record). The known limitations are named mutants: the
survivors `MUT:c2:D02`, `MUT:v60e:V05`, `MUT:v60e:I06`, `MUT:v60e:C08`, `MUT:v60e:H03`, `MUT:v60e:P01` and `MUT:cache:K08`, and
the mutant `MUT:v60e:U01`, which is not applied. A known survivor that is killed, and the unapplied mutant
applied and killed, are admitted. Any other survivor, any other mutant not applied, any mutant
missing, and any `o9` mutant not killed fails the gate. The base run of the mutation step has every
control at its expected status. r1's mutants "accept a path absent at both `F` and `M`" and "rule
evaluated before the `base-drift` test" are equivalent under sec. 21 and are not rows (sec. 33).
The harness and the mutant names land, pinned, with the tool revision (RE-9 (a)); the survivors without
an equivalence argument are also verification defects with distinguishing controls (RE-10 (b);
R6.GATE.10, OBL-24).
Sources: A-089, A-090, A-091, A-092, A-093, A-094, A-095, A-096, A-097, A-098, A-099, A-100, A-101, A-102, A-103, A-104, A-105, A-106. Controls: MUT:o9:RDIR-m1, MUT:o9:RDIR-m2, MUT:o9:RDIR-m3, MUT:o9:RDIR-m4, MUT:o9:RDIR-m5, MUT:o9:RDIR-m6, MUT:o9:RDIR-m7, MUT:o9:RDIR-m8, MUT:o9:RDIR-m9, MUT:o9:RDIR-m10, MUT:o9:RDIR-m11, MUT:o9:RDIR-m12, MUT:o9:RDIR-m13, MUT:o9:RDIR-m14, MUT:o9:RDIR-m15, MUT:o9:RDIR-m16, MUT:o9:RDIR-m17, MUT:c2:D02, MUT:v60e:V05, MUT:v60e:I06, MUT:v60e:C08, MUT:v60e:H03, MUT:v60e:P01, MUT:cache:K08, MUT:v60e:U01.

**R6.CTRL.28** The runner-only controls (A5r-generic, ACCEPT-SCHEMA, ADM-CONFIG-AT-F, B4-MEANING,
CHAIN-REFUSAL, CONFIG-LINT, E-A1r, E-A2r, E-A3r, E-A6r, E-A8r, E-L1, E-L3, E-S1r, E-S2r, GV-CACHE,
GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE, GV-CACHE-KEY, K1-GRAPH, O3-FILTER, R3-F2, R4-B3, R4-B3-DUP,
R5-N6, R6-G6, RL, S7-schema-and-checker, V3-countercontrol, Z6b, lint-ok and rule-negative: 32 rows)
are adopted as controls with expectations only after each runner predicate has been checked against
the requirement it claims to test. A predicate found weaker than that requirement, or testing a
different property, is a verification defect of the control, not an expectation. Each engine analogue
E-* is recorded as preserved at its v6.0e control unless the check finds the two identical, in which
case they are merged. Until a row is checked, its expectation is unsettled and the row cannot hold.
The unsettled rows of the draft expectation file are these 32, G-A1 and TT12 (34 rows); G-A1's
expectation is stated from the rules of sec. 13 and it remains NOT RUN, and TT12's class is
`landing-extra-change`, so that after those two the unsettled rows are the 32 runner-only rows, adopted only after the
check of OBL-25; V4, V27, V27-glossary and V15 are deferred to the owner's decision (R6.CTRL.15).
Sources: none (approved decisions on runner-only controls and null expectations). Controls:
A5r-generic, ACCEPT-SCHEMA, ADM-CONFIG-AT-F, B4-MEANING, CHAIN-REFUSAL, CONFIG-LINT, E-A1r, E-A2r,
E-A3r, E-A6r, E-A8r, E-L1, E-L3, E-S1r, E-S2r, GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE,
GV-CACHE-KEY, K1-GRAPH, O3-FILTER, R3-F2, R4-B3, R4-B3-DUP, R5-N6, R6-G6, RL, S7-schema-and-checker,
V3-countercontrol, Z6b, lint-ok, rule-negative, G-A1, TT12.

**R6.CTRL.29** The following are verification defects of controls at the tool commit. Each is
corrected in the tool revision that implements this design, and the corrected control asserts the
property named:
- TT7's landing run is computed and not asserted; it is asserted.
- TT2's old-style comparison of `X` against `M` is not run; it is implemented.
- S11-7 is implemented by no runner; it is implemented.
- A9r's negative-example check and A11r's clean-lint baseline follow a `return` and never run; they
  are made reachable, and A9r's negative-example half is asserted.
- SW1 computes and does not assert that each mutated site gives exactly one new FAIL against the
  unmutated tree; it is asserted.
- Z9f's adapter half lints an empty source map; it lints the real adapter sources.
- O1-O3, O5 and O7 check lint problems instead of an emitted FAIL `record-invalid`; O6 asserts only
  the absence of an ERROR; RT-I7 does not assert the per-literal split; S11-14 does not assert its
  landing half; item11-T1p does not assert its line count; TT8 does not assert PASS; TT12 asserts no
  named class; U2 does not assert `line_delta`; U10 does not assert the per-splice hashes; K4 checks
  only its K1 half. Each asserts the full property.
- A2r's runner shortens W1-d to `six structural`, which does not distinguish a shortening from another
  change; the case runs on W2-a, whose literal `(A1)` is a true shortening, and asserts that the
  finding is a widening by shortening (RE-20 (b)).
- A5r's expected deny FAIL names no rule alternative; it names it.
- RT-T0's runner expectation string disagrees with its own predicate; the gate makes the predicate
  and the file's expectation the same statement.
- The consumer half of EI7 is not implemented; it is implemented as EI7-consumer.
- The defects of the anchors (VD2-HP-SEARCH, VD3-COUNT, VD3-CONTEXT) and of the side-change entry
  type (SIDE-NONREG) have no control today; the controls are added.
- Every row without a second direction (R6.CTRL.3).
Sources: E-1086. Controls: TT7, TT2, S11-7, A9r, A11r, SW1, Z9f, O1, O2, O3, O5, O6, O7, RT-I7,
S11-14, item11-T1p, TT8, TT12, U2, U10, K4, A2r, A5r, RT-T0, EI7-consumer, VD2-HP-SEARCH, VD3-COUNT,
VD3-CONTEXT, SIDE-NONREG.

**R6.CTRL.30** The gate's own controls are GATE-1 to GATE-30 (sec. 16). They run in the gate's
self-test before the gate evaluates the real records.
Sources: none (gate architecture, sec. 16). Controls: GATE-1, GATE-2, GATE-3, GATE-4, GATE-5, GATE-6, GATE-7, GATE-8, GATE-9, GATE-10, GATE-11, GATE-12, GATE-13, GATE-14, GATE-15, GATE-16, GATE-17, GATE-18, GATE-19, GATE-20, GATE-21, GATE-22, GATE-23, GATE-24, GATE-25, GATE-26, GATE-27, GATE-28, GATE-29, GATE-30.

**Table 17.1. Control catalogue** (no expected results; see the expectation file).

Direction: `adv` adversarial, `pos` positive, `both` both directions recorded; `+restored` marks a
row with a recorded restored case. Kind: `decl` declarative, `proc` procedural.

| Id | Requirements | Runner | Kind | Direction | Case |
|---|---|---|---|---|---|
| U1 | R6.ANCH.5, R6.ANCH.17, R6.HIT.1, R6.CTRL.6, R6.CTRL.8, R6.CTRL.9, R6.ADAPT.3 | controls_engine.py:123 | decl | pos | candidate = pin |
| U2 | R6.ANCH.11, R6.ANCH.17, R6.OUT.18, R6.HIT.1, R6.CTRL.9, R6.CTRL.29 | controls_engine.py:126 | decl | pos | three lines inserted above a site, unledgered |
| U3 | R6.ANCH.11, R6.CTRL.9 | controls_engine.py:130 | decl | pos | same shift produced by a ledgered splice elsewhere in the file |
| U4 | R6.ANCH.17, R6.CLASS.2, R6.CTRL.8, R6.CTRL.9 | controls_engine.py:133 | decl | adv | one word changed in a site line, unledgered |
| U5 | R6.ANCH.17, R6.ANCH.18, R6.CLASS.2, R6.CTRL.9, R6.CTRL.13 | controls_engine.py:136 | decl | adv | site line copied elsewhere in the file |
| U6 | R6.ANCH.17, R6.ANCH.18, R6.CTRL.9, R6.CTRL.13 | controls_engine.py:141 | decl | pos | pin-duplicated line, counts unchanged, context matches ordinal |
| U7 | R6.ANCH.17, R6.ANCH.18, R6.CTX.3, R6.CLASS.2, R6.CTRL.9, R6.CTRL.13 | controls_engine.py:145 | decl | adv | as U6 but the two copies' contexts swapped |
| U8 | R6.ANCH.17, R6.CLASS.2, R6.CTRL.9 | controls_engine.py:148 | decl | adv | site line deleted |
| U9 | R6.ANCH.6, R6.OUT.18, R6.CTRL.9 | controls_engine.py:151 | decl | adv | whitespace-only change in a site line |
| U10 | R6.ANCH.13, R6.ANCH.16, R6.OUT.18, R6.CTRL.8, R6.CTRL.9, R6.CTRL.29, R6.ADAPT.2 | controls_engine.py:157 | decl | pos | ledgered splice rewriting a site line |
| U11 | R6.ANCH.13, R6.CTRL.9, R6.ADAPT.2 | controls_engine.py:162 | decl | pos | ledgered splice deleting a site line |
| U12 | R6.PROF.3, R6.HIT.2, R6.CLASS.12, R6.CTRL.9, R6.ADAPT.3 | controls_engine.py:166 | decl | adv | new pattern hit on a non-site line |
| U14 | R6.HP.7, R6.REC.10, R6.CLASS.4, R6.CLASS.6, R6.CTRL.9, R6.CTRL.16 | controls_engine.py (to be implemented) | decl | pos | a synthetic HP site whose provenance walk is matched by a reviewed HP adjudication record (positive) |
| M1 | R6.ANCH.9, R6.ANCH.16, R6.CLASS.3, R6.CTRL.3, R6.CTRL.6, R6.CTRL.8, R6.CTRL.10 | controls_engine.py:233 | decl | adv +restored | word changed inside a ledgered file outside every splice, not on a site |
| M2 | R6.ANCH.9, R6.ANCH.16, R6.CLASS.3, R6.CTRL.10 | controls_engine.py:236 | decl | adv | a splice applied with altered `new` text |
| M3 | R6.ANCH.4, R6.OUT.5, R6.REC.5, R6.CTRL.10, R6.ADAPT.2, R6.VALID.3 | controls_engine.py:247 | decl | adv | ledger `old_sha256` altered |
| M4 | R6.ANCH.4, R6.OUT.5, R6.REC.5, R6.CTRL.10, R6.ADAPT.2, R6.VALID.3 | controls_engine.py:249 | decl | adv | ledger span shifted by one byte |
| M5 | R6.ANCH.4, R6.OUT.5, R6.REC.5, R6.CTRL.10, R6.TREE.2, R6.ADAPT.2, R6.VALID.3 | controls_engine.py:250 | decl | adv | ledger `base` not FROM |
| M6 | R6.ANCH.17, R6.CTRL.10 | controls_engine.py:254 | decl | adv | site line moved to another file |
| M7 | R6.OUT.27, R6.CTRL.10, R6.ADAPT.3, R6.ADAPT.4, R6.ADAPT.5 | a1_controls.py:206 | decl | adv | frozen `sitemap.json` row value altered (op A) |
| M8 | R6.OUT.27, R6.CTRL.10, R6.ADAPT.4, R6.ADAPT.5 | a1_controls.py:209 | decl | adv | frozen `LEDGER.md` cell altered (op A) |
| M9 | R6.NOTE.10, R6.PUR.4, R6.PIPE.9, R6.ANCH.3, R6.OUT.5, R6.CTRL.10, R6.TREE.2 | a1_controls.py:211 | decl | adv | record tree id not the pinned one |
| M10 | R6.OUT.6, R6.OUT.7, R6.CTRL.10, R6.CTRL.12 | synthetic_fixture.py:543 | decl | adv | `--out` inside the repository checkout |
| M11 | R6.ANCH.5, R6.OUT.5, R6.CTRL.10 | controls_engine.py:258 | decl | adv | CR inserted into a corpus file |
| RT-M | R6.CTRL.11 | to be implemented (tool revision) | decl | adv | RT-T0 with mutation M1 applied to the in-memory T1' `papers/Main.md` |
| RT-SHIFT | R6.CTRL.11 | to be implemented (tool revision) | decl | pos | a shift-only mutant of E: one blank line prepended to `papers/Main.md` and to the FULL book file, in memory |
| OUT-CONFINED | R6.OUT.7, R6.CTRL.12, R6.CORE.8, R6.ADAPT.5, R6.REPRO.4 | to be implemented (tool revision) | proc | both | a run whose tree listing and git state of the clone are taken before and after, with `--out` outside every worktree |
| REPRO-DOUBLE | R6.OUT.20, R6.CTRL.12, R6.REPRO.2 | to be implemented (tool revision) | proc | both | one operation run twice on the same inputs into two fresh `--out` directories |
| REPRO-PYVER | R6.CTRL.12, R6.REPRO.3 | to be implemented (tool revision) | proc | both | the anchor and sitemap build run under two supported Python versions on the same inputs |
| VD2-HP-SEARCH | R6.ANCH.10, R6.CTRL.13, R6.CTRL.29 | to be implemented (tool revision) | decl | both | an adjudicated HP site in a ledgered segment whose file is non-conforming; separately, whose file has an unledgered change |
| VD3-CONTEXT | R6.ANCH.12, R6.CTRL.13, R6.CTRL.29 | to be implemented (tool revision) | decl | adv | a pin-duplicated site whose context does not match its ordinal in a ledgered segment |
| VD3-COUNT | R6.ANCH.12, R6.CTRL.13, R6.CTRL.29 | to be implemented (tool revision) | decl | adv | a pin-duplicated site whose occurrence count changes in a ledgered segment |
| A1r | R6.RULE.10, R6.RULE.13, R6.REC.13, R6.CLASS.5, R6.CTRL.14 | a1_controls.py:653 | decl | adv | rule scope widened to `book/` |
| A2r | R6.RULE.11, R6.REC.13, R6.CTRL.14, R6.CTRL.29 | a1_controls.py:653 | decl | adv | literal shortened to `(A1)` |
| A3r | R6.RULE.10, R6.RULE.13, R6.REC.13, R6.CTRL.14 | a1_controls.py:653 | decl | adv | fingerprint swapped, count unchanged, no widening review |
| A4r | R6.REC.13, R6.CTRL.14 | a1_controls.py:668 | decl | adv | widening review signed by the rule's author |
| A5r | R6.RULE.4, R6.RULE.9, R6.HIT.2, R6.CTRL.4, R6.CTRL.14, R6.CTRL.29 | a1_controls.py:753 | decl | adv | allow rule fingerprinting a sentence that a deny rule matches |
| A5r-generic | R6.RULE.4, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:634 | decl | adv | an allow rule fingerprinting a sentence that a deny rule matches, in the generic (non-A1) rule set |
| A6r | R6.RULE.2, R6.RULE.10, R6.REC.14, R6.CTRL.14 | a1_controls.py:653 | decl | adv | literal not covering the trigger |
| A7r | R6.RULE.1, R6.RULE.2, R6.RULE.10, R6.REC.12, R6.CTRL.14 | a1_controls.py:679 | decl | adv | reused rule id |
| A8r | R6.RULE.2, R6.REC.14, R6.CTRL.14 | a1_controls.py:653 | decl | adv | allow rule with no negative example |
| A9r | R6.REC.13, R6.REC.14, R6.CTRL.14, R6.CTRL.29 | a1_controls.py:653 | proc | adv | rule widened by one alternation |
| A10r | R6.RULE.3, R6.RULE.13, R6.REC.13, R6.CTRL.14 | a1_controls.py:653 | decl | adv | deny rule narrowed in scope |
| A11r | R6.RULE.3, R6.RULE.10, R6.REC.14, R6.CTRL.3, R6.CTRL.14, R6.CTRL.29 | a1_controls.py:653 | decl | adv +restored | deny rule whose countercontrol no longer matches |
| A12r | R6.REC.13, R6.CTRL.14 | conformance_controls.py:2494 | decl | both | a widening review whose verdicts omit one changed item; separately, one naming another superseded blob |
| E-A1r | R6.RULE.10, R6.REC.13, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:642 | decl | adv | engine analogue of A1r: a rule scope widened, evaluated by the engine rule lint on a synthetic rule file |
| E-A2r | R6.REC.13, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:643 | decl | adv | engine analogue of A2r: a literal shortened, evaluated by the engine rule lint |
| E-A3r | R6.RULE.10, R6.REC.13, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:645 | decl | adv | engine analogue of A3r: a fingerprint swapped without a widening review, evaluated by the engine rule lint |
| E-A6r | R6.RULE.2, R6.RULE.10, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:639 | decl | adv | engine analogue of A6r: a literal not covering the trigger, evaluated by the engine rule lint |
| E-A8r | R6.RULE.2, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:641 | decl | adv | engine analogue of A8r: an allow rule with no negative example, evaluated by the engine rule lint |
| E-L1 | R6.RULE.4, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:623 | decl | adv | engine analogue of L1: a fingerprinted sentence shifted by 40 lines in a synthetic tree |
| E-L3 | R6.RULE.4, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:625 | decl | adv | engine analogue of L3: a fingerprinted sentence copied inside scope in a synthetic tree |
| E-S1r | R6.RULE.4, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:628 | decl | adv | engine analogue of S1r: a fingerprinted sentence edited in a synthetic tree |
| E-S2r | R6.RULE.8, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:630 | decl | adv | engine analogue of S2r: a fingerprinted sentence deleted in a synthetic tree |
| L1 | R6.RULE.4, R6.DENY.1, R6.CTRL.14 | a1_controls.py:586 | decl | pos | the W1 sentence shifted by 40 lines |
| L2 | R6.RULE.4, R6.RULE.7, R6.DENY.1, R6.HIT.1, R6.CTRL.14 | a1_controls.py:593 | decl | pos | the W2 lines moved |
| L3 | R6.RULE.4, R6.CLASS.5, R6.CTRL.14 | a1_controls.py:595 | decl | adv | a W1 sentence copied inside scope |
| L4 | R6.RULE.4, R6.HIT.2, R6.CTRL.14 | a1_controls.py:597 | decl | adv | a W1 sentence copied outside scope |
| S1r | R6.RULE.4, R6.CLASS.12, R6.CTRL.14 | a1_controls.py:572 | decl | adv | a fingerprinted sentence edited |
| S2r | R6.RULE.8, R6.CLASS.12, R6.CTRL.14 | a1_controls.py:578 | decl | adv | a fingerprinted sentence deleted |
| V1 | R6.PROF.4, R6.DENY.2, R6.CLASS.5, R6.CTRL.4, R6.CTRL.6, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "The six structural properties of the substratum are listed in Chapter 2." |
| V2 | R6.DENY.2, R6.DENY.3, R6.CTRL.4, R6.CTRL.14 | a1_controls.py:555 | decl | adv | the W1 sentence of ch19:212 edited to "six structural properties, one of which is total finiteness," (a synthetic edit; DR-3's real witness is RT-DR3W) |
| V3 | R6.DENY.2, R6.CTRL.4, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "(A1) the substratum is finite in total" in appendix B |
| V3-countercontrol | R6.OUT.17, R6.CTRL.14, R6.CTRL.28 | a1_controls.py:425 | decl | adv | item 7 run without `--final` at H, over the retired lines of sec. 31 |
| V4 | R6.PUR.9, R6.DENY.6, R6.CTRL.14, R6.CTRL.15 | a1_controls.py:493 | decl | pos | "the framework's sixth structural property, finiteness of the bijection" |
| V5 | R6.DENY.2, R6.CTRL.14, R6.A1CFG.7 | a1_controls.py:466 | decl | adv | "**(A1) Finiteness.** The configuration space is finite." in appendix B |
| V6 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:478 | decl | adv | "the six structural properties of the substratum, including finiteness" |
| V7a | R6.RULE.4, R6.RULE.7, R6.RULE.9, R6.CTRL.14, R6.A1CFG.7 | a1_controls.py:560 | decl | adv | V2 with DR-3 removed from the profile set. Precondition: the text is an edit of a sentence fingerprinted by a W1 rule, inside that rule's scope |
| V7b | R6.PROF.3, R6.HIT.2, R6.CLASS.12, R6.CTRL.14, R6.A1CFG.7 | a1_controls.py:565 | decl | adv | V2's text placed in a file outside every W1 rule's scope, DR-3 removed |
| V7c | R6.RULE.4, R6.CTRL.14, R6.A1CFG.7 | a1_controls.py:570 | decl | adv | a W1 sentence edited with no negative literal (one word of the enumerated list changed) |
| V9 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "Six structural assumptions define the substratum." |
| V10 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "the six structural conditions on the substratum" |
| V11 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "six structural premises of the framework" |
| V12 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "the six substratum posits" |
| V13 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "the structural assumptions A1 through A6" |
| V14 | R6.DENY.2, R6.DENY.3, R6.CTRL.14 | a1_controls.py:474 | decl | adv | "A1--A6"; "A1—A6"; "(A1)–(A6)"; "A1, ..., A6" (four cases) |
| V15 | R6.PUR.8, R6.PUR.9, R6.PROF.3, R6.DENY.4, R6.DENY.6, R6.CTRL.14, R6.CTRL.15, R6.A1CFG.7 | a1_controls.py:499 | decl | adv | "the substratum's sixth axiom, finiteness" |
| V16 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "posit A1 (finiteness) holds" |
| V17 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "A1 (Finiteness): the configuration space is finite" |
| V18 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "(A1) Finiteness. The configuration space S is finite." |
| V19 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "The posit ledger has 14 items." |
| V20 | R6.DENY.2, R6.DENY.3, R6.CTRL.14 | a1_controls.py:466 | decl | adv | "the six structural properties of the bijection, the first being finiteness of S" |
| V21 | R6.PUR.8, R6.PROF.3, R6.DENY.4, R6.CTRL.14 | a1_controls.py:499 | decl | adv | "one of the posits is that the configuration space is finite" |
| V22 | R6.DENY.2, R6.CTRL.14 | a1_controls.py:485 | decl | adv | papers/Main.md:736's H sentence ("Fourteen items, ...") reinstated at a T1'-style `X` |
| V23 | R6.OUT.17, R6.CLASS.5, R6.CTRL.14, R6.A1CFG.7 | a1_controls.py:522 | decl | adv | ch02-substratum.md:136 at H ("... the substratum is a set (finite under A1) with a bijection ...") reinstated at a T1'-style `X`; run as item 7 (`terms --check item7 --final`) |
| V24 | R6.OUT.17, R6.CTRL.14, R6.A1CFG.7 | a1_controls.py:526 | decl | adv | "six structural hypotheses" added; run as item 7 with `--final` |
| V25 | R6.OUT.17, R6.CTRL.14, R6.A1CFG.7 | a1_controls.py:535 | decl | adv | the other direction of V21, V23 and V24: V23 and V24 run as item 7 without `--final`; a W2 line with its rule run as item 7 with `--final`; a `resid`-only hit (V21) run as item 7 with `--final` |
| V26 | R6.PUR.8, R6.PROF.3, R6.DENY.4, R6.CTRL.14, R6.A1CFG.7 | a1_controls.py:518 | decl | adv | added, one at a time: "a finite set with a deterministic bijection on it"; "the substratum is a finite set with a bijection on it"; "We take the substratum to be finite."; "the universe is assumed finite"; "The substratum is assumed to have a finite number of states." |
| V27 | R6.PUR.9, R6.DENY.6, R6.CTRL.14, R6.CTRL.15, R6.A1CFG.7 | a1_controls.py:493 | decl | pos | "The framework's sixth structural property is finiteness of the substratum" (the text of v4's former DR-2 countercontrol), added alone and as the edited glossary.md:13 line |
| V27-glossary | R6.PUR.9, R6.DENY.6, R6.CTRL.14, R6.CTRL.15 | a1_controls.py:507 | decl | pos | the second case of V27: the sentence as the edited glossary.md:13 line |
| WB1 | R6.RULE.4, R6.CTRL.14 | a1_conformance.py:94 | decl | pos | the W1-c sentence at T1' in ch19:198 and FULL:5270, with the W1-c fingerprints and `negative_allowance: {finit: 1}` |
| WB2 | R6.RULE.9, R6.CLASS.5, R6.CTRL.14 | a1_conformance.py:98 | decl | adv | the same sentence at the same location with one more word containing `finit` (for example a second "finite" inserted elsewhere in the sentence) |
| WB3 | R6.RULE.5, R6.CTRL.14 | a1_conformance.py:103 | decl | adv | the fingerprinted sentence copied, unchanged, to another paragraph of a file in W1-c's scope |
| WB4 | R6.RULE.4, R6.HIT.2, R6.CTRL.14 | a1_conformance.py:112 | decl | adv | the fingerprinted sentence copied to a file outside every W1 rule's scope |
| WB5 | R6.RULE.5, R6.RULE.8, R6.CTRL.14 | a1_conformance.py:120 | decl | adv | the fingerprinted sentence moved (cut and pasted) to another paragraph of the same file |
| WB6 | R6.RULE.4, R6.CTRL.14 | a1_conformance.py:125 | decl | adv | a near-copy at the fingerprinted location with one other word changed, keeping one `finit` word |
| WB7 | R6.RULE.4, R6.CTRL.14 | a1_conformance.py:129 | decl | adv | the fingerprinted sentence with its one `finit` word removed |
| WB8 | R6.RULE.5, R6.CTRL.14 | a1_conformance.py:133 | decl | pos | the fingerprinted sentence and its neighbours shifted by 40 lines (as L1) |
| WB9 | R6.RULE.6, R6.CTRL.14 | a1_conformance.py:140 | decl | adv | two fingerprints' sentences made identical in one file, so that one allowance is claimed twice |
| WB10 | R6.REC.14, R6.CTRL.14 | a1_conformance.py:165 | decl | adv | lint: a W1-c rule whose allowance is 2, or 0, or names `axiom` (absent from the sentence) |
| WB11 | R6.REC.14, R6.CTRL.14 | a1_conformance.py:173 | decl | adv | lint: a rule whose fingerprinted sentence fails its own rule (v5.1's W1-c, with no allowance) |
| WB12 | R6.RULE.9, R6.CTRL.14 | a1_conformance.py:184 | decl | adv | V7a on the W1-c sentence ("..., one of which is total finiteness,") |
| WB13 | R6.RULE.5, R6.CTRL.14 | a1_conformance.py:193 | decl | pos | the fingerprinted sentence moved together with both of its neighbours (the three sentences, unchanged) to another section of the same file |
| WB14 | R6.RULE.6, R6.CTRL.14 | a1_conformance.py:205 | proc | both | the fingerprinted sentence with both neighbours duplicated in the same file, so that two copies satisfy step 3 |
| WB15 | R6.RULE.7, R6.CTRL.14 | a1_conformance.py:210 | decl | adv | "Finiteness" (capitalized) added to a W1 sentence at its fingerprinted location |
| lint-ok | R6.RULE.2, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:638 | decl | adv | a neutral rule file presented to the rule lint |
| rule-negative | R6.RULE.4, R6.CTRL.14, R6.CTRL.28 | controls_engine.py:632 | decl | adv | a rule whose own negative example is presented to it |
| H1 | R6.HP.6, R6.REC.10, R6.CLASS.4, R6.CLASS.6, R6.CTRL.16 | controls_engine.py:379 | decl | adv | HP adjudication naming #1473 where the walk gives #1474 |
| H2 | R6.HP.2, R6.HP.6, R6.REC.10, R6.CLASS.4, R6.CLASS.6, R6.CTRL.16 | controls_engine.py:385 | decl | adv | one step listed where the walk gives two |
| H3 | R6.HP.2, R6.HP.6, R6.CLASS.4, R6.CTRL.16, R6.A1CFG.4 | controls_engine.py:388 | decl | adv | a change at an unpinned commit |
| H4 | R6.HP.8, R6.CLASS.2, R6.CTRL.16 | controls_engine.py:393 | decl | adv | an adjudicated site later rewritten outside every splice |
| H5 | R6.HP.9, R6.HP.11, R6.OUT.24, R6.CLASS.4, R6.CTRL.16 | controls_engine.py:400 | decl | adv | an HP site overlapped by a splice, with no adjudication |
| H6 | R6.PUR.3, R6.HP.4, R6.REC.10, R6.CLASS.4, R6.CTRL.16 | controls_engine.py:404 | decl | adv | an adjudication changing a site's row |
| H7 | R6.HP.3, R6.HP.4, R6.HP.6, R6.HP.12, R6.CTRL.16 | controls_engine.py:432 | decl | adv | two adjacent sites, separated by one blank line, both changed at one E..H step, and an H..X splice inside the second only |
| RECLINT-ORPHAN | R6.REC.10, R6.CLASS.4, R6.CLASS.6, R6.CTRL.16 | to be implemented (tool revision) | decl | both | a referenced HP adjudication record that matches no subject of the run |
| B1 | R6.ANCH.13, R6.ANCH.14, R6.CTRL.18 | controls_engine.py:334 | decl | pos | an empty-image splice on a site line |
| B2 | R6.ANCH.13, R6.ANCH.14, R6.CTRL.18 | controls_engine.py:343 | decl | pos | a multi-line splice (33 exist in P) |
| B3 | R6.ANCH.14, R6.CTRL.18 | controls_engine.py:353 | decl | pos | a zero-length insertion at a line boundary |
| B4 | R6.ANCH.14, R6.CTRL.18 | controls_engine.py:357 | decl | pos | a last line without LF |
| B5 | R6.ANCH.17, R6.CLASS.2, R6.CTRL.18 | controls_engine.py:361 | decl | adv | a splice making a replacement region non-unique in `X` |
| B6 | R6.ANCH.14, R6.CTRL.18 | controls_engine.py:366 | decl | pos | a splice touching a site's end offset only |
| K1 | R6.CTX.4, R6.CTX.6, R6.CLASS.2, R6.CTRL.8, R6.CTRL.18 | controls_engine.py:272 | decl | adv | the neighbour line of a meaning-context site is negated |
| K2 | R6.CTX.2, R6.CTX.6, R6.CTRL.18 | controls_engine.py:282 | decl | pos | the same next to a non-required site |
| K3 | R6.CTX.4, R6.CTX.6, R6.CTRL.18 | controls_engine.py:287 | decl | pos | two site paragraphs swapped |
| K4 | R6.CTX.4, R6.CTX.6, R6.CTRL.18, R6.CTRL.29 | controls_engine.py:292 | decl | pos | a site line moved to a distant section of the same file |
| K5 | R6.CTX.5, R6.CTX.9, R6.CTX.10, R6.CTRL.18 | controls_engine.py:297 | decl | adv | an ANAPH site ("This bound ...") whose line above is changed, s3 `visible` |
| K6 | R6.CTX.6, R6.CTX.9, R6.CTX.10, R6.CTX.11, R6.CLASS.12, R6.CTRL.18 | controls_engine.py:302 | decl | adv | a labelled item `*(A2) Determinism.*` whose list lead-in is changed |
| K7 | R6.CTX.6, R6.CTX.9, R6.CTX.10, R6.CTX.11, R6.CTX.12, R6.CTRL.18 | controls_engine.py:310 | decl | adv | a table row whose header row is changed; separately, whose neighbour row is changed |
| K8 | R6.CTX.6, R6.CTX.9, R6.CTX.10, R6.CTX.11, R6.CTRL.18 | controls_engine.py:313 | decl | adv | a list item whose trailer paragraph is changed (the Substratum.md:127 shape) |
| K9 | R6.CTX.9, R6.CTX.10, R6.CTRL.18 | controls_engine.py:320 | proc | pos | a PARTIAL site, nothing else changed |
| K10 | R6.CTX.6, R6.CTX.7, R6.CTRL.18 | controls_engine.py:281 | decl | pos | a meaning-context site with a context change and a matching context adjudication |
| N-W | R6.DENY.2, R6.CTRL.19 | a1_controls.py:600 | decl | pos | every W1 and W2 line at T1', and papers/Main.md:738 ("Thirteen items") |
| RT-A | R6.PUR.4, R6.PIPE.2, R6.PIPE.10, R6.ANCH.3, R6.ANCH.7, R6.CTRL.6, R6.CTRL.19, R6.ADAPT.4, R6.ADAPT.5, R6.A1CFG.3, R6.REPRO.3, R6.EVID.4 | a1_controls.py:171 | decl | pos | `record --pin E --record H` |
| RT-C | R6.PIPE.2, R6.OUT.24, R6.DELEG.1, R6.DELEG.2, R6.DELEG.11, R6.DELEG.14, R6.CTRL.19, R6.ADAPT.6, R6.EVID.4 | a1_controls.py:805 | decl | pos | `execution` at `X = T1'` with `F` = the amended freeze |
| RT-D | R6.PIPE.2, R6.PIPE.14, R6.PROF.3, R6.DENY.1, R6.HIT.2, R6.HIT.3, R6.HIT.6, R6.CTRL.19, R6.TREE.16, R6.EVID.4, R6.EVID.8 | a1_controls.py:374 | decl | pos | `terms --commit X_rep --base H --ledger F:ledger.json`, the ledger the pinned control input (R6.EVID.8) |
| RT-D-gr58 | R6.DENY.1, R6.CTRL.19 | a1_controls.py:389 | decl | pos | RT-D, the papers/GR.md:58 hit with its hit classification record |
| RT-DR | R6.PIPE.13, R6.PROF.1, R6.PROF.4, R6.RULE.3, R6.DENY.1, R6.DENY.3, R6.CTRL.4, R6.CTRL.19, R6.A1CFG.5, R6.A1CFG.7, R6.EVID.4 | a1_controls.py:296 | decl | adv | `terms --commit H --profile DR-1,DR-3,DR-4,DR-5` |
| RT-DR3W | R6.SPLIT.1, R6.RULE.3, R6.DENY.2, R6.DENY.3, R6.CTRL.4, R6.CTRL.7, R6.CTRL.19, R6.A1CFG.5, R6.A1CFG.7, R6.EVID.4, R6.EVID.8 | a1_controls.py:317 | decl | adv | control-only scan of `AGENTS.md` at H (blob 12a9281f..., sha256 d87acac5...) with DR-3 alone (sec. 12); countercontrol: `AGENTS.md` in `X_rep` (`H`'s with the ledger's splices; sha256 59b68984..., the bytes of `T1'`'s copy) |
| RT-E | R6.PIPE.2, R6.PIPE.13, R6.ANCH.17, R6.PROF.1, R6.PROF.4, R6.HIT.1, R6.CTRL.19, R6.ADAPT.3, R6.EVID.4 | a1_controls.py:224 | decl | pos | `coverage --commit E` |
| RT-H0 | R6.HP.2, R6.HP.6, R6.HP.13, R6.OUT.24, R6.CLASS.4, R6.CTRL.19, R6.TREE.16, R6.A1CFG.4, R6.EVID.4 | a1_controls.py:235 | decl | adv | `coverage --commit H`, no HP records |
| RT-I7 | R6.CLASS.5, R6.CTRL.19, R6.CTRL.29, R6.PLAN.8, R6.A1CFG.7, R6.EVID.4, R6.EVID.8 | a1_controls.py:327 | decl | adv | `terms --commit X_rep --profile item7-literal` (R6.EVID.8); the same at H |
| RT-I7A | R6.CTRL.19, R6.PLAN.8, R6.PLAN.18, R6.A1CFG.7, R6.EVID.4, R6.EVID.8 | a1_controls.py:342 | decl | adv | the proposed item-7 amendment check (sec. 18, item 7) at H and at `X_rep` (R6.EVID.8), no records |
| RT-L | R6.CTRL.19, R6.PLAN.15, R6.TREE.12, R6.TREE.15 | a1_controls.py:930 | decl | pos | real objects: an in-memory landing with parents (W, `T1'`), built by the composition rule and never committed |
| RT-L2 | R6.GATE.15, R6.GATE.16, R6.CTRL.5, R6.CTRL.19, R6.TREE.15, R6.RECON.20, R6.RECON.21, R6.EVID.6, R6.EVID.8 | a1_controls.py:976 | proc | pos | before the tool lands: as RT-L, at `X` = `C` = `X_rep` (R6.EVID.8), with `--main` set to the predicted `M` (a pinned `main` commit `M0` plus the tool's landing paths, R6.RECON.21) and the reviewed reconciliation record named from a commit outside those paths |
| RT-O9 | R6.GATE.15, R6.CTRL.17, R6.CTRL.19, R6.RDIR.12, R6.RDIR.14 | a1_controls.py:1025 | proc | pos | the predicted `M`: `main` plus the tool landing plus the plan's record directory as it stands at the stand-in `F` |
| RT-O9-L2 | R6.GATE.15, R6.CTRL.5, R6.CTRL.17, R6.CTRL.19, R6.RDIR.14, R6.RECON.21, R6.EVID.8 | a1_controls.py (split from RT-O9) | proc | pos | the dependent clause of RT-O9: RT-L2 on the same predicted `M` plus the record directory of a representative stand-in `F` (the pinned ledger, edit list and configuration instance), at `X_rep` (R6.EVID.8) |
| RT-T | R6.HIT.5, R6.HIT.6, R6.GATE.15, R6.CTRL.5, R6.CTRL.19, R6.PLAN.4, R6.EVID.8 | a1_controls.py:271 | decl | pos | RT-T0 with every reviewed record of sec. 14, at `X_rep` built from `F`'s ledger (R6.EVID.8) |
| RT-T0 | R6.HP.3, R6.HP.9, R6.HP.10, R6.HP.11, R6.OUT.24, R6.HIT.3, R6.HIT.6, R6.CLASS.4, R6.CTRL.11, R6.CTRL.19, R6.CTRL.29, R6.PLAN.4, R6.A1CFG.4, R6.A1CFG.6, R6.EVID.4, R6.EVID.8 | a1_controls.py:262 | decl | adv | `coverage` at `X = X_rep` (R6.EVID.8), no records; the `T1'` measurement in `reference` |
| RT-X | R6.CTRL.19, R6.TREE.6 | a1_controls.py:921 | decl | pos | real objects: `--scientific-base H --main W --candidate T1'` |
| SW1 | R6.ANCH.17, R6.CTRL.11, R6.CTRL.19, R6.CTRL.29, R6.EVID.4 | a1_controls.py:1240 | proc | adv | per-site sweep at E: each of the 697 sites, one token deleted |
| SW2 | R6.HP.8, R6.HP.9, R6.CTRL.19, R6.EVID.4 | a1_controls.py:1238 | proc | adv | per-site sweep at H: each of the 584 sites, one token deleted (segments E..H `hp`, H..X unledgered) |
| item11-T1p | R6.CTRL.19, R6.CTRL.29, R6.PLAN.12, R6.EVID.4 | a1_controls.py:396 | decl | adv | item 11 run with `--final` at T1', no records; candidate evidence for the landing decision only (exact trial tree, OBL-23) |
| R15 | R6.CLASS.10, R6.CTRL.20, R6.TREE.11, R6.TREE.18 | controls_engine.py:566 | decl | adv | an `L` whose first parent is a `main` commit other than the recorded `M` |
| R16 | R6.CTRL.20, R6.TREE.1, R6.TREE.10, R6.TREE.18 | conformance_controls.py:2469 | decl | adv | `C` = `X` plus one commit that changes an unledgered, undeclared path |
| R17 | R6.CTRL.20, R6.TREE.10, R6.TREE.18 | conformance_controls.py:2472 | decl | pos | `C` = `X` plus one commit that changes only a record path the plan admits after `F` |
| R18 | R6.CLASS.12, R6.CTRL.20, R6.TREE.5, R6.TREE.18 | a1_conformance.py:552 | decl | adv | a classified side-change path whose blob at `M` differs from its class pin |
| R18-engine | R6.CTRL.20, R6.TREE.5, R6.TREE.18 | controls_engine.py:513 | decl | adv | the engine form of R18 in the synthetic world |
| R19 | R6.CLASS.12, R6.CTRL.20, R6.PLACE.8, R6.TREE.5, R6.TREE.18 | a1_conformance.py:563 | decl | adv | a path under the tool-landing prefix on `M` that the class does not list, and separately a listed path whose blob differs from its pin |
| R19-engine | R6.CTRL.20, R6.TREE.5, R6.TREE.18 | controls_engine.py:561 | decl | adv | the engine form of R19 in the synthetic world |
| RL | R6.CTRL.20, R6.CTRL.28, R6.TREE.12 | controls_engine.py:548 | decl | adv | a landing built by the composition rule in the synthetic world |
| SIDE-NONREG | R6.PUR.12, R6.CTRL.20, R6.CTRL.29, R6.TREE.8, R6.RDIR.7 | to be implemented (tool revision) | decl | adv | a side change outside the plan record directory that is a symbolic link at `M`; separately, a submodule entry at `M` |
| TT1 | R6.CTRL.20, R6.TREE.1, R6.TREE.6, R6.TREE.16 | controls_engine.py:511 | decl | adv | `M` = `H` plus a workflow change; `X` = `H` plus splices (was R1) |
| TT2 | R6.CTRL.20, R6.CTRL.29, R6.TREE.9, R6.TREE.17 | controls_engine.py:517 | decl | adv | the same, with the old-style comparison of `X` against `M` run as a countercontrol (was R2) |
| TT3 | R6.CLASS.10, R6.CTRL.20, R6.TREE.3, R6.TREE.9 | controls_engine.py:519 | decl | adv | `X` with parent `M`, not `H` (was R3) |
| TT4 | R6.CLASS.10, R6.CTRL.20, R6.TREE.9 | controls_engine.py:521 | decl | adv | `X` as a merge (two parents) (was R4) |
| TT5 | R6.OUT.5, R6.CTRL.20, R6.TREE.1, R6.TREE.2, R6.TREE.3, R6.VALID.3 | controls_engine.py:526 | decl | adv | ledger `base` not equal to `--scientific-base` (was R5) |
| TT6 | R6.OUT.5, R6.CTRL.20, R6.TREE.1, R6.TREE.4 | controls_engine.py:532 | decl | adv | `M` not descending from `H` (was R6) |
| TT7 | R6.CLASS.10, R6.CTRL.20, R6.CTRL.29, R6.TREE.7, R6.TREE.12, R6.TREE.16, R6.TREE.17 | controls_engine.py:539 | decl | adv | `M` changes a ledgered file outside the splices; no reconciliation record (was R7) |
| TT8 | R6.CTRL.20, R6.CTRL.29, R6.TREE.12, R6.TREE.13, R6.RECON.18 | controls_engine.py:542 | decl | pos | TT7 with a reviewed reconciliation record meeting RC1-RC13 whose `l` equals the computed composition (was R8) |
| TT9 | R6.CLASS.10, R6.CTRL.20, R6.TREE.11 | controls_engine.py:550 | decl | adv | `L` with its parents swapped (was R9) |
| TT10 | R6.CLASS.10, R6.CTRL.20, R6.TREE.12 | controls_engine.py:552 | decl | adv | `L` that drops `M`'s workflow change (carries `H`'s copy) (was R10) |
| TT11 | R6.CLASS.10, R6.CTRL.20, R6.TREE.12, R6.TREE.14 | controls_engine.py:554 | decl | adv | `L` with one extra word in an unledgered file (was R11) |
| TT12 | R6.CTRL.20, R6.CTRL.28, R6.CTRL.29, R6.TREE.14 | controls_engine.py:556 | decl | adv | `L` that loses one splice of `X` (was R12) |
| TT13 | R6.CTRL.20, R6.PLACE.8, R6.TREE.5, R6.TREE.18 | controls_engine.py:559 | decl | pos | `M` contains the tool's own landing (`tools/` and the audit directory only) (was R13) |
| TT14 | R6.CTRL.20, R6.PLACE.8, R6.TREE.7 | controls_engine.py:563 | decl | adv | the tool's landing touches a ledgered path (was R14) |
| N1 | R6.ANCH.19, R6.REC.15, R6.CLASS.7, R6.CTRL.3, R6.CTRL.21 | controls_engine.py:574 | decl | adv +restored | a PIN_OK entry dated after `F` |
| N2 | R6.REC.4, R6.CTRL.21, R6.TREE.16, R6.RECON.2, R6.RECON.3 | controls_engine.py:577 | decl | adv | a reconciliation record that changes a decision on `X` |
| N3 | R6.CTRL.21, R6.RECON.1, R6.RECON.3, R6.RECON.18 | a1_conformance.py:435 | proc | adv | a valid reconciliation record naming a ledgered path that `X` changes (the AGENTS.md shape: D296 at `X`, a later section added on `M`) |
| N3-config-route | R6.CTRL.21, R6.RECON.3 | a1_conformance.py:542 | decl | adv | N3 with the reconciliation record supplied through the configuration's `records` |
| N4 | R6.CLASS.10, R6.CTRL.21, R6.RECON.1, R6.RECON.4, R6.RECON.5, R6.RECON.18 | a1_conformance.py:456 | decl | adv | the same record with its `ledger_binding` altered by one byte |
| N5 | R6.CLASS.10, R6.CTRL.21, R6.RECON.4, R6.RECON.6, R6.RECON.18 | a1_conformance.py:460 | decl | adv | `M` with one more first-parent commit changing the path, not in the record's `side_change_commits` |
| N6 | R6.CTRL.21, R6.RECON.14, R6.RECON.18 | a1_conformance.py:461 | decl | adv | a protected range at `M` altered by one byte in the composed landing |
| N7 | R6.CTRL.21, R6.RECON.7, R6.RECON.18 | a1_conformance.py:465 | decl | adv | the path's blob at `M` differs from the record's `m` |
| N8 | R6.CTRL.21, R6.TREE.13, R6.RECON.9, R6.RECON.18 | a1_conformance.py:470 | decl | adv | a splice's `old` bytes occurring twice at `M` |
| N9 | R6.CTRL.21, R6.RECON.12, R6.RECON.18 | a1_conformance.py:471 | decl | adv | the record's `l` differs from the composed blob |
| N10 | R6.CLASS.10, R6.CTRL.21, R6.TREE.12, R6.RECON.19, R6.EVID.8 | a1_conformance.py:505 | decl | adv | the composition probe, pinned: `M` = 8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d, `X` = `X_rep` (R6.EVID.8; its `AGENTS.md` is the blob of `T1'`'s copy); a landing `L` whose `AGENTS.md` is `X`'s blob 9f4fc3e830707c90ffc105842d26d5b51f01760b (it keeps D296 and drops `M`'s inserted section, bytes 46677-47031); a reconciliation record whose `l` names that same blob. Reference: the composition of `M`'s `AGENTS.md` (6b1280fa) with D296 at offset 2332, blob 86d79863821f3f8cdad86771008b2df89fd1961a |
| N11 | R6.CTRL.21, R6.TREE.12, R6.RECON.19, R6.EVID.8 | a1_conformance.py:517 | decl | pos | the same `M`, `X` and reference, with `L`'s `AGENTS.md` equal to blob 86d79863 and the record's `l` equal to it |
| N12 | R6.CTRL.21, R6.RECON.8, R6.RECON.18 | a1_conformance.py:477 | decl | adv | condition RC3: D296's `old` bytes made to occur twice at `H` in a synthetic copy |
| N13 | R6.CTRL.21, R6.TREE.13, R6.RECON.10, R6.RECON.18 | a1_conformance.py:480 | decl | adv | condition RC5: an insertion on `M` before D296's offset while the record states the identity translation |
| N14 | R6.CTRL.21, R6.RECON.11, R6.RECON.18 | a1_conformance.py:482 | decl | adv | condition RC6: the record's approved text differs from the ledger's `new`, or lines 36-39 of the composition differ from `X`'s |
| N15 | R6.CTRL.21, R6.RECON.13, R6.RECON.18 | a1_conformance.py:484 | decl | adv | condition RC8: the record's `x` differs from the ledger's `expected_sha256` for the path |
| N16 | R6.CTRL.21, R6.RECON.15, R6.RECON.18 | a1_conformance.py:488 | decl | adv | condition RC10: another ledgered file changed on `M` |
| N16-file | R6.CLASS.10, R6.CTRL.21, R6.TREE.7, R6.RECON.15 | a1_conformance.py:490 | decl | adv | N16, second half: the other ledgered file changed on `M` |
| N17 | R6.CTRL.21, R6.RECON.16, R6.RECON.18 | a1_conformance.py:493 | decl | adv | condition RC11: a changed path on `M` not covered by a pinned class, or a corpus path changed |
| N18 | R6.CTRL.21, R6.RECON.17, R6.RECON.18 | a1_conformance.py:494 | decl | adv | condition RC12: `changes_decisions_on_X` non-empty |
| N18-record | R6.CTRL.21, R6.RECON.17 | a1_conformance.py:496 | decl | adv | N18, second half: the record itself |
| R8-S6 | R6.CTRL.21, R6.RECON.19 | controls_engine.py:546 | decl | adv | engine analogue of N10: a reconciliation record whose `l` differs from the computed composition |
| LN1 | R6.RULE.1, R6.REC.1, R6.REC.7, R6.CTRL.22 | conformance_controls.py:2072 | decl | adv | (review probe E6) a record superseding a record of the same kind and schema, present at `F`, with another `record_id`; for each kind of S4a (`config_id` for the configuration) |
| LN2 | R6.RULE.1, R6.REC.7, R6.CTRL.22 | conformance_controls.py:2079 | decl | pos | (positive) a record superseding a record of the same kind, schema and `record_id` that itself passes the lint |
| LN3 | R6.REC.7, R6.REC.8, R6.CTRL.22 | conformance_controls.py:2091 | decl | adv | a superseding record whose `record_id` is missing, empty or not a string; separately, a valid superseding record whose predecessor lacks a valid `record_id` |
| LN4 | R6.REC.7, R6.CTRL.22, R6.CFG.3, R6.CFG.7 | conformance_controls.py:2127 | decl | both | a predecessor of the same lineage that fails the lint itself (no review record; separately, a verdict not `accept`; separately, a predecessor that widens its own predecessor without a valid widening review) |
| LN5 | R6.REC.7, R6.CTRL.22 | conformance_controls.py:2164 | decl | adv | a `supersedes` cycle of two records, and a self-supersession, in a synthetic in-memory store that resolves each named `{path, blob_sha256}` to the given record without rehashing (a hash cycle cannot be built from real objects) |
| LN6 | R6.REC.7, R6.CTRL.22 | conformance_controls.py:2175 | decl | adv | two records of one lineage superseding the same predecessor, both in the audit directory at `F`, only one referenced by the configuration |
| LN7 | R6.REC.7, R6.CTRL.22 | conformance_controls.py:2193 | decl | adv | two records with one `record_id` and kind, each with `supersedes: null` (separately, two chains from one first record that diverge), both read in one run |
| LN8 | R6.REC.7, R6.CTRL.22 | conformance_controls.py:2210 | decl | adv | a three-record chain whose middle record has another `record_id` (separately, another schema of the same kind) |
| LN10 | R6.REC.7, R6.REC.8, R6.CTRL.22, R6.ITEM2.4 | conformance_controls.py:2223 | decl | pos | (positive) a record with `supersedes: null` and no `record_id`, named by no `supersedes` |
| O1 | R6.REC.2, R6.REC.6, R6.CTRL.8, R6.CTRL.22, R6.CTRL.29 | controls_engine.py:462 | decl | adv | a record whose review record has `reviewer` equal to its `author` |
| O2 | R6.REC.2, R6.REC.6, R6.CTRL.22, R6.CTRL.29, R6.VALID.3 | controls_engine.py:465 | decl | adv | a review record naming another blob of the same path |
| O3 | R6.REC.2, R6.REC.6, R6.CTRL.22, R6.CTRL.29 | controls_engine.py:469 | decl | adv | a review whose `verdicts` omit one item id |
| O5 | R6.REC.2, R6.REC.6, R6.REC.11, R6.CTRL.22, R6.CTRL.29 | controls_engine.py:470 | decl | adv | a `reviewer` field holding a CI run URL |
| O6 | R6.OUT.5, R6.REC.5, R6.REC.12, R6.REC.17, R6.CTRL.22, R6.CTRL.29, R6.PLACE.7, R6.VALID.3 | controls_engine.py:473 | decl | adv | a record edited in place after `F` (blob differs from the configuration's reference) |
| O7 | R6.RULE.1, R6.REC.2, R6.REC.12, R6.CTRL.22, R6.CTRL.29 | controls_engine.py:475 | decl | adv | a superseding record with no new review |
| O8 | R6.REC.4, R6.CTRL.22, R6.RECON.2 | controls_engine.py:479 | decl | adv | a record added after `F` and used for a decision on `X` |
| O9 | R6.REC.1, R6.REC.3, R6.REC.4, R6.CTRL.8, R6.CTRL.22 | controls_engine.py:461 | decl | pos | a complete chain (record, review, configuration reference) |
| R3-F2 | R6.REC.6, R6.CTRL.22, R6.CTRL.28 | conformance_controls.py:1789 | decl | adv | a side-change class record without a review record; and the same record with a valid review |
| R4-B3 | R6.REC.6, R6.CTRL.22, R6.CTRL.28 | conformance_controls.py:1864 | decl | adv | a side-change class without an id; and a clean class record |
| R4-B3-DUP | R6.REC.6, R6.CTRL.22, R6.CTRL.28 | conformance_controls.py:1903 | decl | adv | a review record with a duplicate item id or verdict; and a class record with a duplicate class |
| R5-N6 | R6.REC.6, R6.CTRL.22, R6.CTRL.28 | conformance_controls.py:1924 | decl | adv | a class record whose `classes` field is an object instead of a list |
| R6-G6 | R6.REC.7, R6.CTRL.22, R6.CTRL.28 | conformance_controls.py:2235 | decl | adv | a record reusing another lineage's `record_id`; and the control without reuse |
| S4a | R6.REC.1, R6.REC.7, R6.CTRL.22 | conformance_controls.py:2543 | decl | adv | a record of each kind (HP, context, hit classification, rule, scope, side-change class, reconciliation, configuration) whose `supersedes` names a `{path, blob_sha256}` that does not exist in the object store, or a blob that is not a record of the same kind |
| G1 | R6.DELEG.10, R6.DELEG.12, R6.CLASS.9, R6.CTRL.23 | a1_controls.py:815 | decl | adv | delegated result whose `candidate` is an abbreviation |
| G2 | R6.DELEG.8, R6.DELEG.9, R6.DELEG.11, R6.CLASS.12, R6.CTRL.23, R6.TREE.16 | a1_controls.py:818 | decl | adv | no delegated result supplied |
| G3 | R6.DELEG.2, R6.DELEG.15, R6.CLASS.9, R6.CTRL.4, R6.CTRL.23 | a1_controls.py:823 | decl | adv | LEDGER.json with one STALE id removed |
| G4 | R6.DELEG.1, R6.DELEG.3, R6.DELEG.4, R6.DELEG.5, R6.DELEG.10, R6.DELEG.16, R6.CTRL.23 | conformance_controls.py:2332 | decl | both | `sc42` with a supplied result file claiming `verbose_equal: true`, while the clone's re-execution differs |
| G5 | R6.DELEG.2, R6.DELEG.3, R6.DELEG.5, R6.DELEG.15, R6.CTRL.4, R6.CTRL.23, R6.PLAN.6 | conformance_controls.py:2380 | decl | both | `coverage-ledger` with a supplied census JSON; one STALE value at `X` differs from the census the tool runs |
| G6 | R6.DELEG.4, R6.DELEG.5, R6.DELEG.10, R6.DELEG.12, R6.CTRL.23 | conformance_controls.py:2402 | decl | both | `tex` with a supplied preserve_check result reporting `pass`, while a TeX stamp at `X` is wrong |
| G7 | R6.DELEG.6, R6.DELEG.10, R6.DELEG.13, R6.CTRL.23 | conformance_controls.py:2430 | decl | both | `pdf` evidence whose `candidate_tree` differs from `X`'s, or whose artifact hash differs |
| G8 | R6.DELEG.7, R6.DELEG.10, R6.CTRL.23 | conformance_controls.py:2355 | decl | adv | delegated evidence with `plan: null` and no `F` |
| G9 | R6.DELEG.3, R6.DELEG.16, R6.CTRL.23 | conformance_controls.py:2343 | decl | both | `C` = `X` plus one commit that changes the SC-42 result file; the class run at `X` alone would PASS |
| G-A1 | R6.DELEG.1, R6.DELEG.3, R6.DELEG.8, R6.GATE.15, R6.CTRL.5, R6.CTRL.23, R6.CTRL.28 | conformance_controls.py:2434 | proc | adv | delegated classes run natively in clones at `X` and `C`, and host-run classes read from the host API, after the tool lands |
| ACCEPT-SCHEMA | R6.OUT.12, R6.OUT.18, R6.CTRL.23, R6.CTRL.28, R6.REPRO.1 | conformance_controls.py:514 | decl | adv | the acceptance predicate applied to a result of schema `/5` with `config.admission` of mode `chain`, and to the same result declared as schema `/4` |
| B4-MEANING | R6.PUR.11, R6.OUT.18, R6.OUT.21, R6.CLASS.1, R6.CTRL.23, R6.CTRL.28 | conformance_controls.py:1734 | decl | adv | every result: the `class_meaning` table and its quotation by each item that carries a class |
| S7-schema-and-checker | R6.OUT.18, R6.OUT.19, R6.OUT.23, R6.CLASS.1, R6.CTRL.23, R6.CTRL.28, R6.REPRO.1 | synthetic_fixture.py:555 | proc | adv | every result of the self-test and synthetic runs, validated against the result schema, with the outcome recomputed by the outcome checker |
| X1 | R6.PIPE.9, R6.PIPE.10, R6.ANCH.1, R6.ANCH.2, R6.OUT.1, R6.OUT.5, R6.CTRL.23 | a1_controls.py:176 | decl | adv | `record --pin H` |
| X2 | R6.OUT.1, R6.OUT.3, R6.CTRL.23 | synthetic_fixture.py:478 | decl | adv | an exception injected in classification |
| X3 | R6.PIPE.3, R6.OUT.1, R6.OUT.2, R6.OUT.6, R6.OUT.7, R6.CTRL.23 | synthetic_fixture.py:482 | decl | adv | an unknown flag |
| X4 | R6.PIPE.3, R6.OUT.1, R6.OUT.2, R6.OUT.6, R6.CTRL.23 | synthetic_fixture.py:485 | decl | adv | `--help` |
| X5 | R6.PIPE.3, R6.OUT.1, R6.OUT.2, R6.OUT.6, R6.CTRL.23 | synthetic_fixture.py:487 | decl | adv | a missing required argument |
| X6 | R6.OUT.1, R6.OUT.9, R6.CTRL.23 | synthetic_fixture.py:490 | decl | adv | a run whose outcome is REVIEW_REQUIRED |
| X7 | R6.OUT.2, R6.OUT.3, R6.OUT.10, R6.CTRL.23, R6.PLACE.1 | synthetic_fixture.py:504 | proc | both | the tool run with a deliberately broken import in its package (a module raising `ImportError` at import time, before the wrapper's own imports complete) |
| X8 | R6.OUT.2, R6.OUT.10, R6.CTRL.23 | synthetic_fixture.py:510 | proc | adv | the interpreter pointed at a missing script path |
| X9 | R6.OUT.1, R6.OUT.17, R6.CLASS.5, R6.CTRL.23, R6.PLAN.12 | synthetic_fixture.py:517 | decl | adv | an unexplained `repo` hit run as item 11: without `--final`; with `--final`; a REVIEW item of a profile outside item 11's `final_profiles` with `--final`; and `--final` without `--check` |
| X10 | R6.OUT.11, R6.OUT.12, R6.OUT.26, R6.CTRL.23, R6.REPRO.1, R6.EVID.3 | synthetic_fixture.py:536 | proc | both | exit 0 with a `result.json` whose outcome was edited to FAIL; exit 0 with an engine blob hash differing from the configuration's `tool` pin |
| X11 | R6.OUT.12, R6.REC.16, R6.REC.24, R6.GATE.5, R6.CTRL.23, R6.CFG.8 | conformance_controls.py:472 | proc | adv | a control-harness PASS result of RT-E, presented with the pinned engine and configuration hashes |
| ADM-CONFIG-AT-F | R6.REC.5, R6.REC.16, R6.CTRL.23, R6.CTRL.28, R6.PLAN.2, R6.CFG.1, R6.CFG.2 | conformance_controls.py:177 | decl | adv | `--config` naming a configuration at a commit other than the `--freeze` commit |
| CHAIN-REFUSAL | R6.REC.5, R6.REC.16, R6.CTRL.23, R6.CTRL.28 | a1_controls.py:1150 | decl | adv | a run under chain admission whose configuration is an unreviewed draft |
| CONFIG-LINT | R6.CTRL.23, R6.CTRL.28, R6.CFG.4, R6.CFG.6 | conformance_controls.py:1698 | decl | adv | configuration variants whose `tool`, `workflow` or `repository_id` fields are malformed; and the valid configuration |
| EI1 | R6.REC.18, R6.CTRL.23, R6.A1CFG.1 | conformance_controls.py:265 | decl | adv | the tool run directly, without the pre-run check, on a checkout of `T` in which one tool file differs from `T`'s blob (an engine module patched after checkout), or holds a file `T` does not (a compiled-bytecode file under `tools/ledger_coverage/`) |
| EI2 | R6.REC.5, R6.REC.18, R6.CTRL.23 | conformance_controls.py:274 | decl | adv | a run whose event is `pull_request` (head in the canonical repository); separately `schedule`; separately `workflow_run` |
| EI2-consumer | R6.OUT.13, R6.REC.18, R6.CTRL.23 | conformance_controls.py:600 | proc | both | the consumer half of EI2: results of runs whose event is `pull_request`, `schedule` or `workflow_run`; and a result of a `push` run |
| EI3 | R6.OUT.12, R6.REC.18, R6.CTRL.23, R6.EVID.3 | conformance_controls.py:610 | proc | adv | a result whose `F` differs from the landing record's; separately, whose pin table `{path, blob_sha256}` differs; separately, whose configuration path differs |
| EI4 | R6.REC.16, R6.CTRL.23, R6.CFG.2 | conformance_controls.py:321 | decl | adv | `F` holds the plan directory with its `PREREG.md` and a second directory whose `PREREG.md` lists another configuration: (a) that other configuration placed in the plan directory, listed only by the second `PREREG.md`; (b) a caller argument naming the second `PREREG.md` as pin table; (c) the plan's `PREREG.md` whose last `Record pins` subsection omits the configuration while an earlier one lists it; (d) no `PREREG.md` beside the configuration; separately, a malformed row in its last `Record pins` subsection |
| EI5 | R6.REC.18, R6.CTRL.23, R6.RECON.20 | conformance_controls.py:662 | proc | adv | before landing, `git ls-remote` failing; separately, returning no `refs/heads/main` line or more than one; separately, an id that is not a full 40-hex id, or that the verified reader cannot read; separately, an id other than `L`'s first parent |
| EI6 | R6.OUT.3, R6.OUT.4, R6.REC.20, R6.CTRL.23 | conformance_controls.py:1545 | proc | adv | the checkout of a `T` holding, besides the pinned files, an unpinned `tools/hashlib.py` (separately `tools/re.py`, `tools/subprocess.py`) whose module body writes a marker, the probe `review-v6.0a/cx3/hashlib_probe.py`; separately, the entry point run without `-I`, or with a checkout directory on `sys.path` |
| EI7 | R6.REC.21, R6.REC.22, R6.CTRL.17, R6.CTRL.23 | none (composite) | decl | adv | composite of EI7-tool and EI7-consumer |
| EI7-consumer | R6.CTRL.17, R6.CTRL.23, R6.CTRL.29 | to be implemented (tool revision) | proc | both | the consumer half of EI7: results produced under each workflow `uses` form of EI7 |
| EI7-tool | R6.REC.21, R6.CTRL.23 | conformance_controls.py:441 | decl | both | the tool half of EI7: each workflow `uses` form of EI7, and a conforming 40-hex `uses` line |
| EI8 | R6.REC.19, R6.CTRL.23, R6.PLACE.1 | conformance_controls.py:1339 | proc | pos | the pre-run check on a clean checkout of a `T` equal to the configuration's `tool.files` |
| EI9 | R6.REC.19, R6.CTRL.23 | conformance_controls.py:1360 | proc | adv | the pre-run check on a checkout holding `tools/ledger_coverage/engine/__pycache__/util.cpython-313.pyc`, an unchecked-hash bytecode file whose code writes a marker (review v6.0b probe P4) |
| EI10 | R6.REC.19, R6.CTRL.23 | conformance_controls.py:1388 | proc | adv | the pre-run check on a checkout holding an extension module `tools/ledger_coverage/engine/util.so` beside the pinned `util.py` (probe P7) |
| EI11 | R6.REC.19, R6.CTRL.23 | conformance_controls.py:1405 | proc | adv | the pre-run check on a checkout in which the pinned path `tools/ledger_coverage/engine/util.py` is a symlink to a payload outside the package (probe P9) |
| EI12 | R6.REC.19, R6.CTRL.23, R6.PLACE.1 | conformance_controls.py:1421 | proc | adv | the pre-run check on a checkout in which the entry point `tools/ledger_coverage.py` is a symlink to `tools/evil.py` (probe P10) |
| EI13 | R6.REC.19, R6.CTRL.23 | conformance_controls.py:1458 | proc | adv | the pre-run check, each case separately: a pinned file changed by one byte; a pinned file missing; an extra `.py` file under `tools/ledger_coverage/`; a directory entry that is neither a regular file nor a directory; `tools` a symlink to a real directory holding the pinned files, inside the checkout, and separately to an absolute path outside it (R-d); `F` not fetched; the configuration path absent at `F`; a configuration without `tool.files` |
| EI14 | R6.REC.18, R6.GATE.15, R6.CTRL.5, R6.CTRL.17, R6.CTRL.23 | conformance_controls.py:1475 | proc | adv | the review v6.0a CX-3 tree: a branch `T'` holding the pinned files and an unpinned `tools/hashlib.py` |
| EI14-dispatch | R6.GATE.15, R6.CTRL.5, R6.CTRL.17, R6.CTRL.23 | conformance_controls.py (split from EI14) | proc | adv | the branch-dispatch half of EI14: the pinned workflow dispatched on the branch `T'` |
| EI15 | R6.NOTE.9, R6.PIPE.5, R6.REC.19, R6.CTRL.23 | conformance_controls.py:1500 | proc | adv | the pre-run check, each case separately: a `workflow_dispatch` run on a branch, with `F'` a commit whose configuration pins the branch's changed tool code (review v6.0c case O-4); `GITHUB_REF` `refs/tags/main`; `F` given as `HEAD`, as an abbreviated id, or in upper case |
| GV1 | R6.REC.17, R6.CTRL.23 | conformance_controls.py:869 | proc | adv | a replace ref (`refs/replace/`) that substitutes a commit of the E..H chain, and separately one that substitutes the configuration's blob at `F`; separately, a role commit given as a ref name (`main`, a tag) |
| GV2 | R6.REC.17, R6.CTRL.23 | conformance_controls.py:882 | proc | adv | a graft file that makes a commit of the E..H chain parentless |
| GV3 | R6.RULE.8, R6.REC.17, R6.CTRL.23 | conformance_controls.py:903 | proc | adv | a commit-graph file recording false parents for a commit between `H` and `M`, and for a rule's `recorded_at` |
| GV4 | R6.REC.17, R6.REC.25, R6.CTRL.23, R6.PLACE.7 | conformance_controls.py:943 | decl | adv | a loose object whose stored content does not hash to its id, each case separately: the configuration's blob at `F`, the pin table's blob, a tree of `X`, a commit of E..H, a tool blob at `T` |
| GV5 | R6.REC.17, R6.CTRL.23 | conformance_controls.py:981 | proc | adv | a store lacking a parent that a bounded walk needs (a shallow store whose boundary lies inside E..H; separately, a partial store lacking a needed blob); and the positive direction: a shallow store that holds every object the run needs |
| GV6 | R6.REC.5, R6.REC.6, R6.REC.17, R6.CTRL.23 | conformance_controls.py:343 | decl | adv | a symlink entry at the configuration's path in `F`; separately at the pin table's path; separately at a record's path |
| GV6-disk | R6.REC.17, R6.CTRL.23 | conformance_controls.py:1008 | decl | adv | GV6 case 1 on disk: a symlink entry at the configuration's path in `F`, read from a real object store |
| GV7 | R6.REC.23, R6.CTRL.23 | none (composite) | decl | adv | composite of GV7-tool and GV7-consumer |
| GV7-consumer | R6.REC.23, R6.CTRL.23 | conformance_controls.py:624 | proc | adv | the consumer half of GV7: the artifact list failing; incomplete records |
| GV7-tool | R6.REC.23, R6.DELEG.6, R6.DELEG.11, R6.DELEG.17, R6.CTRL.23 | conformance_controls.py:379 | decl | adv | the tool half of GV7: the run record read failing; the host-run class records incomplete (four cases) |
| GV-CACHE | R6.REC.17, R6.CTRL.23, R6.CTRL.28 | conformance_controls.py:1058 | decl | adv | corrupted objects presented before and after the verified object cache is filled |
| GV-CACHE-AFTER-READ | R6.REC.17, R6.CTRL.23, R6.CTRL.28 | conformance_controls.py:1145 | decl | adv | an object read through the same verified reader after a first read, and through a new reader after the object is corrupted |
| GV-CACHE-IMMUTABLE | R6.REC.17, R6.CTRL.23, R6.CTRL.28 | conformance_controls.py:1154 | decl | adv | assignment, deletion and update attempts on the cached tree and path mappings, and on a copy of them |
| GV-CACHE-KEY | R6.REC.17, R6.CTRL.23, R6.CTRL.28 | conformance_controls.py:1122 | decl | adv | cached tree mappings for two commits, compared with `git ls-tree` of each exact commit |
| K1-GRAPH | R6.REC.17, R6.CTRL.23, R6.CTRL.28 | a1_controls.py:1139 | decl | adv | the dependency graph between the configuration, its review record and the class records in the actual layout, and in each countercontrol layout that introduces a hash cycle |
| O3-FILTER | R6.DELEG.3, R6.CTRL.23, R6.CTRL.28 | conformance_controls.py:719 | decl | adv | a clone made by the native delegation runner from a repository whose configuration names a smudge filter |
| TR1 | R6.REC.16, R6.CTRL.23, R6.CFG.8 | conformance_controls.py:157 | decl | adv | a run without `--freeze` |
| TR2 | R6.REC.5, R6.REC.16, R6.CTRL.23, R6.CFG.1, R6.CFG.2, R6.CFG.3, R6.VALID.3 | conformance_controls.py:164 | decl | adv | a configuration whose sha256 is not in the pin table of the `PREREG.md` beside it |
| TR3 | R6.REC.5, R6.REC.16, R6.CTRL.23, R6.CFG.2 | conformance_controls.py:170 | decl | adv | a review record placed beside the configuration, naming its blob, but not in `F`'s pin table |
| TR5 | R6.REC.24, R6.GATE.15, R6.CTRL.5, R6.CTRL.23, R6.PLAN.2, R6.CFG.8, R6.REPRO.1 | conformance_controls.py:151 | decl | pos | a complete run: `--freeze F` and `--config F:<path>` given; the `PREREG.md` beside the configuration, whose last `Record pins` subsection lists the configuration and its review; the run record read in a host CI job, with event `workflow_dispatch` and repository and head repository ids equal to `repository_id`; `T`'s tool files and workflow equal to the configuration's `tool` pins and to the checkout; `F` is the candidate named by `--freeze`, fetched by its full id and not required on `main`, and the run is dispatched on `main` at `T` (OBL-16 (a)) |
| TR5-sim | R6.REC.24, R6.CTRL.23 | conformance_controls.py:142 | decl | pos | TR5 simulated in memory: a complete control-harness run with every snapshot field |
| TR13 | R6.REC.16, R6.CTRL.23, R6.CFG.8 | conformance_controls.py:184 | proc | adv | a local run, all inputs otherwise valid |
| TR14 | R6.OUT.13, R6.REC.18, R6.CTRL.23 | conformance_controls.py:541 | proc | both | the same workflow and tool run in a fork, or in another repository; separately, a `pull_request` run from a fork, executed and listed in the canonical repository (its `head_repository.id` is the fork's); separately, the same results presented to a consumer that runs in a fork |
| TR14-tool | R6.REC.18, R6.CTRL.23 | conformance_controls.py:196 | decl | adv | the tool half of TR14: the run in a fork, in another repository, and as a fork `pull_request` run in the canonical repository |
| TR15 | R6.REC.18, R6.REC.22, R6.CTRL.23 | conformance_controls.py:211 | decl | adv | a run of a workflow whose blob at `T` differs from `tool.workflow.blob_sha256` (a forged result written by a changed workflow step, review counterexample CX-2); separately, a same-named workflow at a path other than `tool.workflow.path` |
| TR15-consumer | R6.CTRL.17, R6.CTRL.23 | to be implemented (tool revision) | proc | both | the consumer half of TR15: results produced by a workflow whose blob differs from its pin, or by a same-named workflow at another path |
| TR28-consumer | R6.OUT.13, R6.REC.18, R6.CTRL.23 | conformance_controls.py:578 | proc | both | the consumer half of TR28: results produced under a differing tool blob or an extra file; and an equal `T` |
| TR28-tool | R6.REC.18, R6.CTRL.23 | conformance_controls.py:219 | decl | adv | the tool half of TR28: a `T` whose tool blob differs from its pin; an extra file under `tools/ledger_coverage/` |
| TR29 | R6.OUT.13, R6.REC.18, R6.CTRL.23, R6.RECON.20 | conformance_controls.py:591 | proc | both | a run whose `head_sha` is not on `main`'s first-parent chain (a branch); separately, a run whose `head_sha` is the evaluated commit `X`; separately, a result whose recorded `T` differs from the producing run's `head_sha` |
| TR29-tool | R6.REC.5, R6.REC.18, R6.CTRL.23, R6.VALID.3 | conformance_controls.py:254 | decl | adv | the tool half of TR29: `head_sha` on a branch; `head_sha` equal to `X` |
| TR30 | R6.OUT.13, R6.REC.18, R6.CTRL.23 | conformance_controls.py:521 | proc | both | a result whose evaluated commits differ from the landing record's |
| TR45-opB | R6.OUT.15, R6.REC.16, R6.REC.24, R6.CTRL.17, R6.CTRL.23, R6.CFG.8 | conformance_controls.py:2263 | proc | both | the offline replay of an accepted op-B result from its committed snapshot; and the same with the recorded result hash altered |
| TR45-opC | R6.GATE.15, R6.CTRL.5, R6.CTRL.17, R6.CTRL.23 | to be implemented (tool revision) | proc | both | the offline replay of an accepted op-C result whose delegated classes (`tex`, `pdf`, `record-dir`, `sc42`, `coverage-ledger`, `ci`) are taken from the snapshot's delegated evidence, with no host call, clone, PDF build or checker run |
| TR46 | R6.OUT.14, R6.REC.24, R6.CTRL.23 | conformance_controls.py:526 | proc | both | a committed compressed result whose uncompressed sha256 differs from the recorded one |
| TR48 | R6.OUT.26, R6.REC.18, R6.REC.25, R6.CTRL.23, R6.PLACE.3, R6.PLACE.4 | conformance_controls.py:228 | decl | pos | a valid `T` whose `tools/ledger_coverage/` and entry point hold exactly the configuration's `tool.files`, each a regular file with its pinned blob, and whose workflow blob equals the pin; the checkout equal to `T`'s tree |
| TR50 | R6.REC.18, R6.REC.22, R6.CTRL.23 | conformance_controls.py:239 | decl | adv | the workflow at `tool.workflow.path` at `T` modified (one byte changed) |
| TR50-consumer | R6.CTRL.17, R6.CTRL.23 | to be implemented (tool revision) | proc | both | the consumer half of TR50: results produced by the modified workflow |
| TR51 | R6.REC.18, R6.CTRL.23 | conformance_controls.py:246 | decl | adv | a symlink, separately a submodule entry, under `tools/ledger_coverage/` in `T`'s tree |
| TR51-consumer | R6.CTRL.17, R6.CTRL.23 | to be implemented (tool revision) | proc | both | the consumer half of TR51: results produced from a `T` carrying a symlink or submodule entry under `tools/ledger_coverage/` |
| TR52 | R6.REC.18, R6.CTRL.23, R6.PLACE.3, R6.CFG.6 | conformance_controls.py:224 | decl | adv | an additional file under `tools/ledger_coverage/` at `T` that the configuration's `tool.files` does not name |
| TR52-consumer | R6.CTRL.17, R6.CTRL.23 | to be implemented (tool revision) | proc | both | the consumer half of TR52: results produced from a `T` carrying an additional unnamed file under `tools/ledger_coverage/` |
| S11-1 | R6.CTRL.24, R6.PLAN.1, R6.PLAN.2, R6.PLAN.3 | a1_controls.py:832 | decl | adv | sec. 18 item 1 countercontrol: one splice reverted in `X` |
| S11-2 | R6.CTRL.24, R6.PLAN.1, R6.PLAN.4 | none (composite) | decl | adv | sec. 18 item 2 countercontrols (composite of S11-2a, S11-2b, S11-2c) |
| S11-2a | R6.CTRL.24, R6.PLAN.4 | a1_controls.py:902 | decl | adv | sec. 18 item 2: an unclassified new site at E |
| S11-2b | R6.CTRL.24, R6.PLAN.4 | a1_controls.py:913 | decl | adv | sec. 18 item 2: a dropped Phase-3 site at E |
| S11-2c | R6.OUT.27, R6.CLASS.11, R6.CTRL.24, R6.PLAN.4 | a1_controls.py:218 | decl | adv | sec. 18 item 2: a J row with S1 Yes at E (op A `record_checks`) |
| S11-3 | R6.DELEG.6, R6.DELEG.17, R6.CTRL.24, R6.PLAN.1, R6.PLAN.5 | a1_controls.py:887 | decl | adv | sec. 18 item 3: delegated evidence from another `head_sha`; separately, `build.rc` nonzero |
| S11-4 | R6.DELEG.2, R6.DELEG.15, R6.CTRL.4, R6.CTRL.24, R6.PLAN.1, R6.PLAN.6 | a1_controls.py:893 | decl | adv | sec. 18 item 4: one STALE value altered; separately, an id removed |
| S11-5 | R6.PIPE.14, R6.PROF.4, R6.PROF.6, R6.CLASS.5, R6.CTRL.24, R6.PLAN.1, R6.PLAN.7 | a1_controls.py:841 | decl | adv | sec. 18 item 5: a splice adding "no longer" |
| S11-6 | R6.PIPE.14, R6.PROF.4, R6.PROF.7, R6.CTRL.4, R6.CTRL.24, R6.PLAN.1, R6.PLAN.7 | a1_controls.py:841 | decl | adv | sec. 18 item 6: a splice adding "is infinite" |
| S11-7 | R6.CTRL.24, R6.CTRL.29, R6.PLAN.1, R6.PLAN.8 | none | decl | adv | sec. 18 item 7: the H-form "Fourteen items" reinstated (as V22), run through the literal check and DR-5 |
| S11-8 | R6.CLASS.7, R6.CTRL.24, R6.PLAN.1, R6.PLAN.9 | a1_controls.py:850 | decl | adv | sec. 18 item 8: the FULL mirror text altered |
| S11-9 | R6.CLASS.3, R6.CTRL.24, R6.PLAN.1, R6.PLAN.10 | a1_controls.py:855 | decl | adv | sec. 18 item 9: one registry splice dropped |
| S11-10 | R6.CLASS.8, R6.CTRL.24, R6.PLAN.1, R6.PLAN.11 | a1_controls.py:860 | decl | adv | sec. 18 item 10: a Lean definition changed |
| S11-11 | R6.CTRL.24, R6.PLAN.1, R6.PLAN.12 | a1_controls.py:869 | decl | adv | sec. 18 item 11: a new unexplained `A1` line in a new active file |
| S11-12 | R6.ANCH.19, R6.CLASS.7, R6.CTRL.24, R6.PLAN.1, R6.PLAN.13 | a1_controls.py:864 | decl | adv | sec. 18 item 12: a guard-pin splice dropped |
| S11-13 | R6.DELEG.10, R6.DELEG.16, R6.CLASS.9, R6.CTRL.4, R6.CTRL.24, R6.PLAN.1, R6.PLAN.14 | a1_controls.py:879 | decl | adv | sec. 18 item 13: the SC-42 result file hand-edited |
| S11-14 | R6.DELEG.1, R6.CLASS.9, R6.CTRL.24, R6.CTRL.29, R6.PLAN.1, R6.PLAN.15, R6.TREE.9 | a1_controls.py:873 | decl | adv | sec. 18 item 14: an extra word in an unledgered file of `X`; separately, `L` dropping W's workflow |
| S11-56 | R6.PROF.1, R6.PROF.5, R6.PROF.6, R6.PROF.7, R6.PROF.10, R6.CTRL.24, R6.PLAN.7, R6.PLAN.16 | a1_conformance.py:278 | proc | pos | items 5 and 6 at T1': the tool's `register`, `register-caps` and `infinity` results on P's per-edit unit |
| S11-57a | R6.PROF.5, R6.PROF.6, R6.CTRL.24, R6.PLAN.7 | a1_conformance.py:299 | proc | adv | a two-variant edit: selected variant unchanged text, unapplied variant adds "now" |
| S11-57b | R6.PROF.5, R6.PROF.6, R6.CTRL.24, R6.PLAN.7 | a1_conformance.py:304 | proc | adv | the same with "no longer"; also at an `H` holding `old_step2` |
| S11-57c | R6.PIPE.11, R6.PROF.8, R6.PROF.9, R6.CTRL.24, R6.PLAN.7 | a1_conformance.py:318 | proc | adv | one splice covering two edits: one deletes "now", the other adds it elsewhere |
| S11-57d | R6.SPLIT.1, R6.PROF.7, R6.CTRL.24, R6.PLAN.7 | a1_conformance.py:326 | proc | pos | "The bound holds; the lattice is infinite." as an added pair |
| S11-58a-f | R6.PROF.5, R6.PROF.8, R6.CTRL.24 | a1_conformance.py:344 | proc | adv | one two-variant edit, with `H` holding: `old` once; `old_step2` only; neither; both once; `old` twice and `old_step2` once; both ambiguous |
| S11-58g | R6.PROF.8, R6.PROF.9, R6.CTRL.24, R6.CFG.5 | a1_conformance.py:352 | proc | adv | a splice built for `(old, new)` while P selects `(old_step2, new_step2)` |
| S11-58h | R6.PIPE.11, R6.PROF.8, R6.CTRL.24 | a1_conformance.py:358 | proc | adv | an earlier edit that destroys a later edit's `old` |
| S11-58i | R6.PROF.8, R6.CTRL.24 | a1_conformance.py:365 | proc | adv | overlap: `old = "aa"` in `"xaaay"` (non-overlapping count 1) |
| S11-58j | R6.PIPE.11, R6.PROF.8, R6.PROF.9, R6.CTRL.24 | a1_conformance.py:373 | proc | adv | chained edits: edit 1 `cat fox` → `fox cat` at `H` `"cat fox."`; edit 2 `cat` → `dog`, whose only occurrence after edit 1 lies inside edit 1's image; the ledger holds edit 1's splice |
| S11-58k | R6.PROF.8, R6.PROF.9, R6.CTRL.24 | a1_conformance.py:386 | proc | adv | chained across the image boundary: `H` = `"ab qc"`; edit 1 `{old: "ab q", new: "xy"}`; edit 2 `{old: "qc", new: "Q", old_step2: "yc", new_step2: "Q"}`. Edit 2's `old` occurs once at `H`; after edit 1 the text is `"xyc"`, `qc` no longer occurs, and P selects `yc`, which spans edit 1's image and the original `c`; the ledger holds edit 1's splice |
| Y1 | R6.CTRL.25, R6.SYN.1, R6.SYN.2 | synthetic_fixture.py:314 | decl | pos | edits applied exactly; sites moved |
| Y2 | R6.CLASS.3, R6.CTRL.25, R6.SYN.1 | synthetic_fixture.py:321 | decl | adv | one edit's new lines changed |
| Y3 | R6.PROF.4, R6.CTRL.25, R6.SYN.1 | synthetic_fixture.py:326 | decl | adv | "Axiom Z is assumed" added |
| Y4 | R6.REC.13, R6.CTRL.25, R6.CFG.7, R6.SYN.1 | synthetic_fixture.py:334 | decl | both | a legitimate "Axiom Z" hit with its allow rule |
| Y5 | R6.CTRL.25, R6.SYN.1 | synthetic_fixture.py:340 | decl | adv | a site with `kind: definition` and its neighbour changed |
| Y6 | R6.DELEG.9, R6.DELEG.10, R6.CTRL.25, R6.ADAPT.6, R6.SYN.1 | synthetic_fixture.py:349 | decl | adv | the artifact hash wrong |
| Y7 | R6.CTRL.25, R6.SYN.1, R6.VALID.2 | synthetic_fixture.py:352 | decl | adv | `record` requested |
| Y8 | R6.CTRL.25, R6.CORE.1, R6.CORE.7, R6.SYN.1, R6.SYN.2, R6.REPRO.1 | a1_controls.py:1262 | proc | pos | the A1 configuration and the synthetic one run in one CI job by the same engine blob |
| Y9 | R6.CTRL.25, R6.SYN.1 | synthetic_fixture.py:358 | decl | adv | a list-item site whose lead-in changed |
| Y10 | R6.PROF.2, R6.REC.5, R6.CTRL.25, R6.PLACE.3, R6.ADAPT.1, R6.SYN.1, R6.VALID.3 | synthetic_fixture.py:362 | decl | adv | the `line-patch/1` module edited by one byte, configuration unchanged |
| Z1 | R6.OUT.5, R6.REC.5, R6.CTRL.25, R6.CFG.4, R6.ADAPT.1, R6.VALID.1, R6.VALID.2, R6.VALID.3 | synthetic_fixture.py:385 | decl | adv | a synthetic configuration with an unknown `schema` |
| Z2 | R6.CTRL.25, R6.CFG.4, R6.VALID.1, R6.VALID.2 | synthetic_fixture.py:386 | decl | adv | a synthetic configuration missing a required field (`indicators`) |
| Z3 | R6.CTRL.25, R6.CFG.4, R6.VALID.1, R6.VALID.2 | synthetic_fixture.py:387 | decl | adv | a synthetic configuration with an unknown field |
| Z4 | R6.CTRL.25, R6.VALID.1, R6.VALID.2 | synthetic_fixture.py:388 | decl | adv | a synthetic configuration whose `operations` omit the operation run |
| Z5 | R6.OUT.5, R6.CTRL.25, R6.CFG.7, R6.VALID.1, R6.VALID.3 | synthetic_fixture.py:389 | decl | adv | a synthetic configuration whose review record names the author as reviewer |
| Z6 | R6.CTRL.25, R6.CFG.4, R6.ADAPT.1, R6.VALID.1, R6.VALID.2 | synthetic_fixture.py:390 | decl | adv | a synthetic configuration naming an adapter interface version that does not exist |
| Z6b | R6.CTRL.25, R6.CTRL.28, R6.CFG.4, R6.VALID.2 | synthetic_fixture.py:394 | decl | adv | a run given the withdrawn argument `--config-sha256` |
| Z7 | R6.OUT.5, R6.CTRL.25, R6.CFG.5, R6.CFG.6, R6.VALID.1, R6.VALID.4 | synthetic_fixture.py:395 | decl | adv | a synthetic configuration with a duplicate profile; separately, a `final_profiles` entry that is not a review profile; separately, an extractor (pattern) hash mismatch |
| Z8 | R6.OUT.5, R6.OUT.8, R6.CTRL.25, R6.CFG.4, R6.CFG.6, R6.VALID.1, R6.VALID.2 | synthetic_fixture.py:398 | decl | adv | a synthetic configuration whose controls file is absent or empty for the operation |
| Z9-STAGED | R6.CTRL.25, R6.PLACE.2, R6.RDIR.13, R6.CORE.6 | staged purity job (record id `outcome` today) | proc | both | the staged purity lint of the purity job over the staged engine tree |
| Z9a | R6.CTRL.25, R6.PLACE.2, R6.CORE.2, R6.CORE.3, R6.CORE.6, R6.A1CFG.2 | synthetic_fixture.py:570 | proc | adv | a 40-hex commit id planted as a string literal in an engine module |
| Z9b | R6.CTRL.25, R6.PLACE.2, R6.CORE.2, R6.CORE.3, R6.CORE.6, R6.A1CFG.2 | synthetic_fixture.py:570 | proc | adv | a 7-hex abbreviation planted |
| Z9c | R6.CTRL.25, R6.PLACE.2, R6.CORE.2, R6.CORE.3, R6.CORE.6, R6.A1CFG.2 | synthetic_fixture.py:571 | proc | adv | the A1 regex `\bA1\b` planted as a string literal |
| Z9d | R6.CTRL.25, R6.PLACE.2, R6.CORE.2, R6.CORE.3, R6.CORE.6, R6.A1CFG.2 | synthetic_fixture.py:571 | proc | adv | the s3 value "per unit Q2" planted |
| Z9e | R6.CTRL.25, R6.PLACE.2, R6.CORE.3, R6.CORE.5, R6.CORE.6 | synthetic_fixture.py:572 | proc | pos | the allowlisted field name `splices` used in an engine module |
| Z9f | R6.CTRL.25, R6.CTRL.29, R6.PLACE.2, R6.CORE.3, R6.CORE.6, R6.A1CFG.3 | synthetic_fixture.py:573 | proc | both | an adapter module under `adapters/` containing "a1exit deletion exact-edit ledger v2" |
| Z9g | R6.CTRL.25, R6.PLACE.2, R6.PLACE.4, R6.RDIR.13, R6.CORE.1, R6.CORE.2, R6.CORE.3, R6.CORE.4, R6.CORE.5, R6.CORE.6, R6.A1CFG.1, R6.A1CFG.2 | a1_controls.py:1169 | proc | pos | the real engine tree, with the value set extended to the adapter companions |
| Z9h | R6.CTRL.25, R6.PLACE.2, R6.CORE.3, R6.CORE.4, R6.CORE.6, R6.ADAPT.2 | a1_controls.py:1175 | proc | adv | `'guard-pin'` (a value that occurs in `edits.json`) planted in an engine module, with the adapter companions in the value set |
| Z10 | R6.RULE.13, R6.REC.13, R6.CLASS.4, R6.CTRL.25, R6.CFG.7 | synthetic_fixture.py:449 | decl | adv | the synthetic configuration superseded by a version that adds a merge to its HP obligation, with no `widening_review`; separately, with a valid widening review and a matching adjudication |
| Z11 | R6.REC.5, R6.CTRL.25, R6.TREE.5, R6.VALID.4 | conformance_controls.py:2524 | decl | adv | two class records (or one record) defining the same class id, for example `trial-workflow` |
| I2-1 | R6.CTRL.26, R6.ITEM2.1 | record_directory_controls.py:646 | proc | pos | the `item2-coverage` arm's command, read from the workflow file by the conformance controls (which already read that file) |
| I2-2 | R6.CTRL.26, R6.ITEM2.2 | record_directory_controls.py:662 | decl | pos | a meaning-context adjudication supplied through `context-adjudications.json`, matching both context hashes of a meaning-context site |
| I2-3 | R6.OUT.5, R6.REC.5, R6.REC.9, R6.CTRL.26, R6.PLACE.6, R6.ITEM2.3, R6.VALID.3 | record_directory_controls.py:675 | decl | adv | `context-adjudications.json` absent at `F` |
| I2-4 | R6.OUT.5, R6.REC.5, R6.REC.9, R6.HIT.4, R6.CTRL.26, R6.ITEM2.3, R6.VALID.3 | record_directory_controls.py:697 | decl | adv | `hit-classifications.json` present but not referenced by the configuration |
| I2-5 | R6.REC.2, R6.REC.5, R6.REC.9, R6.CTRL.26, R6.ITEM2.3 | record_directory_controls.py:709 | decl | adv | a referenced record without a valid review |
| I2-6 | R6.REC.8, R6.REC.9, R6.HIT.4, R6.CTRL.26, R6.ITEM2.4 | record_directory_controls.py:724 | decl | pos | an empty `entries` list with its `record_id`, referenced, with a valid review bound to that `record_id` |
| I2-7 | R6.HIT.2, R6.HIT.4, R6.HIT.5, R6.CTRL.26, R6.ITEM2.2 | record_directory_controls.py:747 | decl | pos | a hit classification supplied through `hit-classifications.json`, matching a hit outside any HP region by its line sha256 |
| I2-8 | R6.CTRL.26, R6.ITEM2.2 | record_directory_controls.py:774 | decl | pos | an indicator adjudication supplied through `context-adjudications.json`, matching both context hashes and both structure hashes of a LIST or TABLE site |
| RDIR-1 | R6.CTRL.26, R6.PLACE.6, R6.RDIR.6, R6.RDIR.10, R6.RDIR.12, R6.A1CFG.3 | record_directory_controls.py:242 | decl | pos | every entry of `D_rec` at `M` equal to `F` (was O9-1) |
| RDIR-2 | R6.CLASS.12, R6.CTRL.26, R6.RDIR.6, R6.RDIR.8 | record_directory_controls.py:252 | decl | adv | one file in `D_rec` modified on `M` after `F` (was O9-2) |
| RDIR-3 | R6.CTRL.26, R6.RDIR.6, R6.RDIR.8 | record_directory_controls.py:261 | decl | adv | a file added in `D_rec` on `M`, absent at `F` (was O9-3) |
| RDIR-4 | R6.CTRL.26, R6.RDIR.6, R6.RDIR.8 | record_directory_controls.py:270 | decl | adv | a file of `F` in `D_rec` deleted on `M` (absent at `H` and `M`) (was O9-4) |
| RDIR-5 | R6.CTRL.26, R6.TREE.6, R6.TREE.8, R6.TREE.18, R6.RDIR.10 | record_directory_controls.py:279 | decl | adv | a path outside `D_rec` whose blob at `M` equals its blob at `F` (was O9-5) |
| RDIR-6 | R6.CTRL.26, R6.RDIR.1 | record_directory_controls.py:287 | decl | adv | a sibling path `D-x/f` sharing `D_rec` as a string prefix, equal at `F` and `M` (was O9-6) |
| RDIR-7 | R6.CTRL.26, R6.RDIR.10 | record_directory_controls.py:296 | proc | adv | the clean-path predicate applied to paths with a `.`, `..` or empty component (was O9-7) |
| RDIR-8 | R6.CTRL.26, R6.RDIR.6, R6.RDIR.7, R6.RDIR.11, R6.RECON.16 | record_directory_controls.py:313 | decl | adv | in `D_rec`: the same blob with a mode change (`100644` to `100755`); a symbolic link at `M` where `F` has a regular file of the same bytes; a submodule entry at `M`. Each case is run through the full `execution --main` path (the `M` role) and, separately, through a reconciliation record's RC11 (was O9-8) |
| RDIR-9 | R6.CTRL.26, R6.RDIR.5, R6.VALID.4 | record_directory_controls.py:326 | decl | adv | a ledgered path, and separately a corpus path, inside `D_rec` (was O9-9) |
| RDIR-10 | R6.CTRL.26, R6.RDIR.1, R6.RDIR.4 | record_directory_controls.py:337 | proc | pos | a configuration in the root directory (was O9-10) |
| RDIR-11 | R6.CTRL.26, R6.RDIR.5, R6.VALID.1, R6.VALID.4 | record_directory_controls.py:349 | decl | adv | a path inside `D_rec` that exists at `H` (was O9-11) |
| RDIR-12 | R6.CTRL.26, R6.RDIR.5, R6.VALID.4 | record_directory_controls.py:357 | decl | adv | the admitted `D_rec`, with a side-change class the configuration references whose prefix lies inside `D_rec` (was O9-12) |
| RDIR-12b | R6.CTRL.26, R6.RDIR.4, R6.SYN.3 | record_directory_controls.py:368 | proc | adv | a configuration whose directory lies under `.github/`, with an entry inside it on `M`: (a) the directory present at `H`; (b) the directory absent at `H` (was O9-12b) |
| RDIR-13 | R6.CTRL.26, R6.RDIR.10 | record_directory_controls.py:382 | decl | adv | a path in `D_rec`, equal at `F` and `M`, that a class names with a pin differing from `M` (was O9-13) |
| RDIR-14 | R6.CTRL.26, R6.RDIR.3, R6.RDIR.11 | record_directory_controls.py:397 | decl | pos | no `--freeze` (was O9-14) |
| RDIR-15 | R6.CTRL.26, R6.RDIR.11, R6.RECON.16 | record_directory_controls.py:409 | decl | pos | a reconciliation record, `M` with `D_rec` equal to `F` (was O9-15) |
| RDIR-16 | R6.REC.16, R6.CTRL.26, R6.PLACE.4, R6.RDIR.2, R6.RDIR.4, R6.A1CFG.1, R6.VALID.1, R6.VALID.4 | record_directory_controls.py:420 | decl | adv | a configuration in a newly introduced, unrelated directory (four components, absent at `H`, holding the configuration and a file of record pins, no ledgered, corpus, class or `.github/` path) (was O9-16) |
| RDIR-17 | R6.CTRL.26, R6.RDIR.5, R6.VALID.4 | record_directory_controls.py:429 | decl | adv | a class record defining class id `record-directory` (was O9-17) |
| RDIR-18 | R6.CTRL.26, R6.RDIR.11, R6.RECON.16 | record_directory_controls.py:410 | decl | adv | a reconciliation record, `M` with one file of `D_rec` modified after `F` (was O9-18) |
| RDIR-19 | R6.CTRL.26, R6.RDIR.11, R6.RECON.16 | record_directory_controls.py:412 | decl | adv | a reconciliation record, `M` with one file of `F`'s `D_rec` deleted (was O9-19) |
| RDIR-20 | R6.REC.16, R6.CTRL.26, R6.RDIR.2, R6.RDIR.4, R6.RDIR.11, R6.RECON.16, R6.A1CFG.1, R6.VALID.4 | record_directory_controls.py:480 | decl | adv | a reconciliation record, `M` with a file of `D_rec` equal to `F`, but the run's `D_rec` not admitted (was O9-20) |
| RDIR-21 | R6.CLASS.12, R6.CTRL.26, R6.RDIR.9 | record_directory_controls.py:491 | decl | adv | a file in `D_rec` that differs between `F` and `M`, and a class pin naming it that matches `M` (was O9-21) |
| RDIR-22 | R6.CTRL.26, R6.RDIR.4 | record_directory_controls.py:502 | proc | pos | an unadmitted `D_rec` with no entry inside it on `M`, under `execution --main --freeze` (was O9-22) |
| RDIR-23 | R6.CTRL.26, R6.TREE.4, R6.RDIR.3 | record_directory_controls.py:526 | proc | pos | the admitted `D_rec` and a configuration whose run is `coverage` (no `M`) (was O9-23) |
| RDIR-24 | R6.CTRL.26, R6.TREE.5, R6.RDIR.5, R6.VALID.4 | record_directory_controls.py:450 | decl | adv | a class record admitted through `--classify` that defines the class id `record-directory` (was O9-24) |
| RDIR-25 | R6.CTRL.26, R6.RDIR.4, R6.SYN.3 | record_directory_controls.py:538 | proc | pos | the synthetic world of the conformance controls: an unadmitted `D_rec` (`syn`) present at `H`, with entries inside it on `M`, under `execution --main --freeze` (was O9-25) |
| GATE-1 | R6.GATE.1, R6.GATE.3, R6.GATE.8, R6.GATE.9, R6.GATE.13, R6.CTRL.30, R6.EVID.1 | gate self-test | decl | adv | false actual value: a runner record with status PASS whose actual says exit 0 while the retained exit file and result.json say 20 |
| GATE-2 | R6.GATE.9, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | missing result: one id of the file has no record |
| GATE-3 | R6.GATE.9, R6.GATE.13, R6.CTRL.2, R6.CTRL.30 | gate self-test | decl | adv | duplicate id: two records carry one id (in one job, and separately across jobs) |
| GATE-4 | R6.GATE.9, R6.GATE.13, R6.CTRL.2, R6.CTRL.30 | gate self-test | decl | adv | unexpected id: a record whose id is not in the file |
| GATE-5 | R6.GATE.5, R6.GATE.13, R6.GATE.15, R6.CTRL.5, R6.CTRL.30 | gate self-test | decl | adv | unadmitted NOT RUN: a row allowing only PASS reported NOT RUN with a reason |
| GATE-6 | R6.GATE.1, R6.GATE.3, R6.GATE.8, R6.GATE.13, R6.CTRL.30, R6.EVID.1 | gate self-test | decl | adv | weak runner predicate: A1r recorded PASS with a truthful actual (lint problems nonempty) while the retained result has no record-invalid item for the rule file |
| GATE-7 | R6.GATE.12, R6.GATE.13, R6.CTRL.1, R6.CTRL.30 | gate self-test | decl | adv | expectation row with no requirement: requirements empty, or naming an id absent from r6 |
| GATE-8 | R6.GATE.4, R6.GATE.12, R6.GATE.13, R6.CTRL.1, R6.CTRL.30 | gate self-test | decl | adv | requirement with no control: an r6 requirement whose control list is empty or names an id absent from the file |
| GATE-9 | R6.GATE.5, R6.GATE.7, R6.GATE.9, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | raw evidence missing: a PASS record whose manifest names a result.json absent from the evidence set, or whose sha256 differs |
| GATE-10 | R6.GATE.7, R6.GATE.8, R6.GATE.9, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | procedural predicate failed: SW1 tuples with one site carrying two new FAIL items while the runner records PASS |
| GATE-11 | R6.GATE.13, R6.GATE.15, R6.CTRL.5, R6.CTRL.30 | gate self-test | decl | adv | released NOT RUN: RT-L2 reported NOT RUN while its release check holds |
| GATE-12 | R6.GATE.2, R6.GATE.9, R6.GATE.13, R6.CTRL.1, R6.CTRL.2, R6.CTRL.30 | gate self-test | decl | adv | composite incomplete: S11-2 with S11-2c missing |
| GATE-13 | R6.GATE.8, R6.GATE.13, R6.GATE.16, R6.CTRL.30, R6.RECON.21, R6.EVID.6 | gate self-test | decl | adv | RT-L2 drafted record: the run uses an unreviewed reconciliation record (drift state unresolved) |
| GATE-14 | R6.GATE.8, R6.GATE.13, R6.GATE.16, R6.CTRL.30, R6.RECON.21 | gate self-test | decl | adv | RT-L2 record bound to another M: reviewed record whose M blob differs from the run M |
| GATE-15 | R6.GATE.8, R6.GATE.13, R6.GATE.16, R6.CTRL.30, R6.RECON.21 | gate self-test | decl | adv | RT-L2 partial coverage: reviewed bound record covering one of two drifted paths |
| GATE-16 | R6.GATE.1, R6.GATE.9, R6.GATE.13, R6.CTRL.30, R6.A1CFG.6, R6.EVID.2, R6.EVID.5 | gate self-test | decl | pos | reference difference: RT-T0 with region_lines.count 214 against reference 215, every expect field met |
| GATE-17 | R6.GATE.2, R6.GATE.3, R6.GATE.4, R6.GATE.9, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | malformed expectation file: unknown schema id, unknown field, or NOT RUN allowed without reason and release condition |
| GATE-18 | R6.GATE.11, R6.GATE.13, R6.GATE.14, R6.CTRL.30, R6.CORE.7, R6.A1CFG.7 | gate self-test | decl | pos | positive control: complete, correct records and evidence for a fixture with one row of each predicate kind and one allowed NOT RUN |
| GATE-19 | R6.GATE.13, R6.GATE.16, R6.CTRL.30, R6.RECON.21, R6.EVID.6 | gate self-test | decl | pos | RT-L2 reconciled: reviewed record bound to the exact H, M and C blobs covering every drifted path |
| GATE-20 | R6.GATE.1, R6.GATE.5, R6.GATE.9, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | status/actual inconsistency: runner status FAIL with an actual that meets expect |
| GATE-21 | R6.GATE.6, R6.GATE.10, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | an unexpected survivor: a mutant whose row allows only KILLED recorded SURVIVED |
| GATE-22 | R6.GATE.6, R6.GATE.10, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | a missing mutant: a MUT row with no mutation record |
| GATE-23 | R6.GATE.6, R6.GATE.10, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | pos | a known survivor recorded SURVIVED and the not-applied mutant recorded NOT APPLIED (positive) |
| GATE-24 | R6.GATE.6, R6.GATE.10, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | an unexpected not-applied mutant: a mutant whose row allows only KILLED recorded NOT APPLIED |
| GATE-25 | R6.GATE.8, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | a double run whose two result files differ by one byte |
| GATE-26 | R6.GATE.2, R6.GATE.9, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | a row with composed_of and its own runner record: the own record PASS, a component FAIL |
| GATE-27 | R6.GATE.9, R6.GATE.13, R6.CTRL.3, R6.CTRL.30 | gate self-test | decl | adv | direction missing: (a) a control row in the both-directions scope with no restored expectation, no direction both, no paired_with and no observation exemption; (b) a row whose paired_with names an id that is not a row |
| GATE-28 | R6.GATE.9, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | both | composite precedence: (a) a composite row whose component A is recorded FAIL and whose component B is an admitted NOT RUN; (b) a composite whose only non-PASS component is an admitted NOT RUN |
| GATE-29 | R6.GATE.9, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | adv | deferred expectation: a row whose expect outcome is DEFERRED, carrying two candidate expectations, every other row holding |
| GATE-30 | R6.GATE.12, R6.GATE.13, R6.CTRL.30 | gate self-test | decl | both | correspondence exemption: (a) a requirement of kind status with an empty control list and no verification; (b) the same requirement with verification review |
| CLASS-RETAINED | R6.PIPE.15, R6.CLASS.2 | to be implemented (tool revision) | decl | adv | a retained ledger entry absent from `edits.json`, with a splice, or with site text differing between `H` and `X` |
| CLASS-UNLEDGERED | R6.ANCH.15, R6.CLASS.3 | to be implemented (tool revision) | decl | adv | in a ledgered segment, a file not in the ledger whose bytes differ between FROM and TO |
| CLASS-PROV-AMBIGUOUS | R6.CLASS.4 | to be implemented (tool revision) | decl | adv | an HP region not unique as a whole-line block at a parent; separately, anchors out of order |
| CLASS-PIN-TARGET | R6.CLASS.7 | to be implemented (tool revision) | decl | adv | an updated guard pin whose new literal is absent from its file, or from one of its targets (op C) |
| CLASS-RECORD-CHECKS | R6.CLASS.11 | to be implemented (tool revision) | decl | adv | op A with a record check that does not hold |
| HIT-REPLACEMENT | R6.HIT.2, R6.CLASS.12 | to be implemented (tool revision) | decl | adv | a hit in a ledgered replacement image, its profile pattern absent from, and separately present in, the FROM region |
| DELEG-RECDIR | R6.DELEG.14 | to be implemented (tool revision) | decl | both | a changed path, an addition outside `execution/`, an unenumerated addition under `execution/`; and the enumerated additions |
| PROF-PARAMS-LINT | R6.PROF.10 | to be implemented (tool revision) | decl | both | a `register-infinity-params` entry differing from its literal in P's source; and all entries equal |
| PROF-LANDING-LIST | R6.PROF.11 | to be implemented (tool revision) | proc | pos | the landing record of an op C run with `register`, `register-caps` and `infinity` matches in the splice images of `X` |
| RULE-MINLIT | R6.RULE.11 | to be implemented (tool revision) | decl | adv | an allow rule whose `matcher.literal` is shorter than 8 characters, with and without the trigger |
| RULE-ZEROFP | R6.RULE.12 | to be implemented (tool revision) | decl | both | an allow rule with zero fingerprints; and a deny rule |
| TR28 | R6.REC.18, R6.CTRL.23 | composite (no runner of its own) | decl | both | composite of TR28-tool and TR28-consumer (RD-4) |
| TR45 | R6.GATE.15, R6.CTRL.5 | composite (no runner of its own) | decl | both | composite of TR45-opB and TR45-opC (RD-4, RD-26) |
| LC-1 | R6.TREE.12, R6.TREE.13 | to be implemented (tool revision) | decl | both | composition case "neither side changed": fixture and byte-exact expected landing blob of `p.md` in the expectation file (Q15) |
| LC-2 | R6.TREE.12, R6.TREE.13 | to be implemented (tool revision) | decl | both | composition case "only X/C changed": fixture and byte-exact expected landing blob of `p.md` in the expectation file (Q15) |
| LC-3 | R6.TREE.12, R6.TREE.13 | to be implemented (tool revision) | decl | both | composition case "only M changed": fixture and byte-exact expected landing blob of `p.md` in the expectation file (Q15) |
| LC-4 | R6.TREE.12, R6.TREE.13 | to be implemented (tool revision) | decl | both | composition case "both changed to equal blobs": fixture and byte-exact expected landing blob of `p.md` in the expectation file (Q15) |
| LC-5 | R6.TREE.12, R6.TREE.13 | to be implemented (tool revision) | decl | both | composition case "both changed to different blobs, ledgered path (a line prepended on M)": fixture and byte-exact expected landing blob of `p.md` in the expectation file (Q15) |
| LC-6 | R6.TREE.12, R6.TREE.13 | to be implemented (tool revision) | decl | both | composition case "both changed to different blobs, ledgered path (the spliced line moved on M)": fixture and byte-exact expected landing blob of `p.md` in the expectation file (Q15) |
| LC-7 | R6.TREE.12 | to be implemented (tool revision) | decl | adv | composition case "derived artifact": a derived artifact changed on both sides; REVIEW_REQUIRED for every candidate `L` until a regeneration verification procedure is specified and independently reviewed (expected landing blob open, RE-18, OC-4) |
| DELEG-REGEN | R6.DELEG.3, R6.CLASS.9 | to be implemented (tool revision) | proc | both | a re-executed generator in its own clone under `--out`: equal output, one-byte difference, missing output, timeout, extra write, and an evaluated tree whose checker copy accepts anything (Q13) |
| REP-BUILD | R6.EVID.8 | to be implemented (tool revision) | decl | both | the representative candidate `X_rep` built from `H`, the pinned ledger and edit list and the configuration's control instance, twice with equal ids; a ledger with one splice changed by one byte; a builder importing the engine (R6.EVID.8) |

**Table 17.2. Record-directory mutants** (set `o9`; each row names the change and the controls
that distinguish it; the results on the correct implementation and on the mutant are in the
expectation file).

| Id | Change | Distinguishing control |
|---|---|---|
| MUT:o9:RDIR-m1 | the completeness check omitted: only the `H`-to-`M` scan is used | RDIR-4 |
| MUT:o9:RDIR-m2 | the shared membership predicate (R6.RDIR.1) without the trailing `/` | RDIR-6 |
| MUT:o9:RDIR-m3 | DIR2 removed | RDIR-11 |
| MUT:o9:RDIR-m4 | the admission check (R6.RDIR.2) removed | RDIR-16 |
| MUT:o9:RDIR-m5 | mode not compared | RDIR-8 (mode case) |
| MUT:o9:RDIR-m6 | the blob at `M` compared with `H` instead of `F` | RDIR-1 |
| MUT:o9:RDIR-m7 | DIR3 removed | RDIR-12 (class-prefix case, admitted `D_rec`) |
| MUT:o9:RDIR-m8 | the clean-path test removed | RDIR-7 |
| MUT:o9:RDIR-m9 | R6.RDIR.10 row 2 bypassed: the rule applied when a class pin names `p` but differs | RDIR-13 |
| MUT:o9:RDIR-m10 | the completeness check reads bytes before checking the entry type | RDIR-8 (symbolic link and submodule cases) |
| MUT:o9:RDIR-m11 | RC11 uses the classifier without the completeness check | RDIR-19 |
| MUT:o9:RDIR-m12 | DIR5 removed | RDIR-17, RDIR-24 |
| MUT:o9:RDIR-m13 | the completeness check's items suppressed for a path a matching class pin classifies | RDIR-21 |
| MUT:o9:RDIR-m14 | a non-regular entry inside `D_rec` passed to the existing classifier | RDIR-8 (full-path cases) |
| MUT:o9:RDIR-m15 | the admission ERROR raised for a non-admitted `D_rec` that `H` holds (whenever `M` holds an entry inside it) | RDIR-25 |
| MUT:o9:RDIR-m16 | the admission ERROR raised whenever `D_rec` is non-admitted, whatever `M` holds | RDIR-22 |
| MUT:o9:RDIR-m17 | the admission ERROR removed for a non-admitted `D_rec` absent at `H` and present on `M` | RDIR-16 |

***

## 18. Mapping of the plan's mandatory checks to tool commands

The plan's mandatory checks are those of the amended retirement plan's sec. 11 (the plan's checker
P and its preregistration). This section maps each check to a tool operation and its exact command,
and names the control that tests the tool's side. Expected results are stated in the expectation
file under the named controls.

**R6.PLAN.1** Every mandatory check of the amended plan's sec. 11 is mapped to a tool operation, its
exact flags, and a control. Each mapping has a countercontrol: a mutant of the input on which the tool
gives a result other than PASS, and a FAIL naming its class of sec. 15 wherever the plan's own check
failed hard on the corresponding mutant. That the plan's own check fails on each mutant is a property
of the plan's checker, not of the tool; it is an outstanding obligation (R6.PLAN.16).
Sources: RV-018, E-1268. Controls: S11-1, S11-2, S11-3, S11-4, S11-5, S11-6, S11-7, S11-8, S11-9,
S11-10, S11-11, S11-12, S11-13, S11-14.

**R6.PLAN.2** Every command below adds `--freeze F`, `--config F:<record dir>/retirement-config.json`
and `--out DIR`, and reads `F`'s records by object id. Profiles, rules, the delegation contract and
the HP obligations come from the configuration record. A path written `F:...` is resolved through the
configuration. `X` is the execution head.
Sources: E-1268. Controls: S11-1, TR5, ADM-CONFIG-AT-F.

**R6.PLAN.3** Item 1 (every `new` string present; residual pointer scan with zero unqualified hits)
maps to `execution --scientific-base H --candidate X --ledger F:ledger.json --edits F:edits.json`
(splice postconditions) and `terms --commit X --profile ptr`. The `ptr` hit lines (four W2 lines with
their rules and papers/GR.md:58 with its hit classification record) are reference figures. The W2
rules are plan records. Countercontrol: one splice reverted in `X`.
Sources: E-1269. Controls: S11-1.

**R6.PLAN.4** Item 2 (the ledger checker's build and check, its checks CK1-CK8, and the extended scan
with zero unqualified hits) maps to `record --pin E --record F` and `coverage --commit X --segment E..H
--segment H..X=F:ledger.json --hp F:hp.json --classify F:...`, where the `--classify` arguments
include the two item-2 records of sec. 22. Countercontrols, from the frozen self-test at `E`: an
unclassified new site (S11-2a); a dropped Phase-3 site (S11-2b); a J row with S1 Yes, detected by
op A's `record_checks` (S11-2c). The run is not PASS until the reviewed records of sec. 14 exist
(RT-T0, RT-T).
Sources: E-1270. Controls: S11-2, S11-2a, S11-2b, S11-2c, RT-T0, RT-T.

**R6.PLAN.5** Item 3 (build; no dropped glyphs; page and median-character counts) maps to `execution
... --delegation F:delegation.json` with the classes `tex`, `pdf` and `ci`, under the evidence binding
of sec. 13. Countercontrol: evidence from another `head_sha`; separately, `build.rc` nonzero.
Sources: E-1271. Controls: S11-3.

**R6.PLAN.6** Item 4 (the coverage checker; STALE entries re-affirmed) maps to `execution` with the
class `coverage-ledger` and the `ci` job `coverage_check`, which the `ci` class's job list includes.
Countercontrol: one STALE value altered; separately, an id removed. The FAIL names its class.
Sources: E-1272. Controls: S11-4, G5.

**R6.PLAN.7** Items 5 and 6 (register and infinity scans of added lines with zero findings) map to
`execution` with the profiles `register` and `register-caps` (item 5) and `infinity` (item 6), each on
the plan's per-edit and per-step unit and on the per-splice unit, with the edit/splice correspondence
check (sec. 9); item 6 uses splitter version 2 (sec. 8). Countercontrols: a splice adding "no longer"
(item 5); a splice adding "is infinite" (item 6). The constructed cases S11-57a-d test the per-edit
unit. Equality of the tool's results with the plan checker's `static_new` is an outstanding
obligation (R6.PLAN.16).
Sources: E-1273, E-1274. Controls: S11-5, S11-6, S11-56, S11-57a, S11-57b, S11-57c, S11-57d.

**R6.PLAN.8** Item 7 (a corpus grep for `\bA1\b` and related terms with only ledger false positives,
and zero posit counts "Fourteen", "six structural" and "sixth of") maps, as frozen, to `terms --commit
X --profile item7-literal`. The literal check is kept as the named countercontrol `item7-literal`, with
RT-I7. Item 7 as frozen does not pass at T1' or at `X_rep`: seven lines contain the legitimate count of
the bijection's properties (W1); RT-I7 asserts the counts at `X_rep` (R6.EVID.8), and the measurement
at T1' is historical. Countercontrol: the H-form
"Fourteen items" reinstated, which must FAIL in both the literal check and DR-5 (S11-7). DR-5 is a plan
record. RT-I7A runs the proposed amendment check of R6.PLAN.18 at `H` and at `X_rep` as a test of the
mechanism.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1275, E-1283, OC-3. Controls: S11-7, RT-I7, RT-I7A.

**R6.PLAN.9** Item 8 (mirrors byte-identical) maps to `execution` with the subject `mirror`.
Countercontrol: the FULL mirror text altered.
Sources: E-1276. Controls: S11-8.

**R6.PLAN.10** Item 9 (census registry notes updated in the same commit) maps to `execution`
conformance of `verification/lean-manuscript-census.json`; its splice count in `F`'s ledger is a
reference figure. Countercontrol: one registry splice dropped.
Sources: E-1277. Controls: S11-9.

**R6.PLAN.11** Item 10 (Lean docstring-only; kernel and Mathlib builds; CI) maps to `execution` with
the subject `lean` (equal outside comments) and the class `ci`, with evidence under sec. 13.
Countercontrol: a Lean definition changed.
Sources: E-1278. Controls: S11-10.

**R6.PLAN.12** Item 11 (repository scan with `--final`, zero unexplained) maps to `terms --commit X
--check item11 --scope F:repo-scope.json --rules F:repo-rules.json --final`. Without `--final` the tool
reports an unexplained line as REVIEW_REQUIRED; under `--final` the REVIEW items of the profiles in
item 11's `final_profiles` become FAIL `final-unclassified`; no flag turns REVIEW_REQUIRED into PASS.
A premise line in a path-wide-explained file is not passed. Each line of sec. 14's item-11 review load
stays FAIL `final-unclassified` until it has an exact rule. Countercontrol: a new unexplained `A1`
line in a new active file.
Sources: E-1279, E-1289. Controls: S11-11, item11-T1p, X9.

**R6.PLAN.13** Item 12 (the guard pins, guard mutants, and the guard checks in CI) maps to `execution`
with the subject `pin` (counts at `H` and at `X`) and the class `ci`. Countercontrol: a guard-pin splice
dropped.
Sources: E-1280. Controls: S11-12.

**R6.PLAN.14** Item 13 (SC-42 regeneration and safeguards) maps to `execution` with the native class
`sc42`. Countercontrol: the result file hand-edited; the FAIL names its class.
Sources: E-1281. Controls: S11-13.

**R6.PLAN.15** Item 14 (preservation check of the candidate, against the moved base when `main`
moved) maps to `execution --scientific-base H --main M --candidate X [--landing L]` with the `tex`
contract; the candidate is checked against `H`, and the landing under sec. 20, with the record-directory
rule of sec. 21 in the `M` role. Countercontrols: an extra word in an unledgered file of `X`; separately,
an `L` dropping W's workflow. Both halves are asserted.
Sources: E-1282. Controls: S11-14, RT-L.

**R6.PLAN.16** The plan-dependent parts of R6.PLAN.1 to R6.PLAN.15 are not tool requirements. Each is
an outstanding obligation of the plan amendment (sec. 32: OBL-27 for the countercontrol and plan-side behaviours, OBL-1 and OBL-2; the exception parts, OBL-12), a named blocker on the execution it gates,
verified at `F` against the plan's checker as frozen with the plan:
- that the plan's own check fails on each countercontrol mutant where R6.PLAN.1 says so, and the
  plan-side behaviours cited in items 1, 2, 3, 4, 8, 12 and 14;
- that the tool's `register`, `register-caps` and `infinity` results, its selection, counting and
  splitting, equal the plan checker's `static_new` on the plan's per-edit unit (items 5 and 6), and
  that S11-56's equality holds;
- the parity measurements made during design (scripts not retained), which are recomputed with a
  retained script under that obligation, and otherwise stated only as measured during design and not
  retained.

An extension of the plan's recorded execution exceptions may cover only the parts identical to them:
the parameter-equality clause (ESC-2), the fingerprinted W1 and W2 sentences (ESC-1) and the line
content (ESC-4). Every other part falls under the obligations above.
Sources: E-1268, E-1269, E-1271, E-1272, E-1273, E-1274, E-1276, E-1280, E-1282. Controls: S11-56.

**R6.PLAN.17** The eight gaps of the plan's preservation checker are requirements of the plan
amendment, carried there verbatim, each an outstanding obligation (sec. 32, OBL-8) and a named blocker on the
plan execution it gates; the tool discharges none of them:
1. the candidate is the `--commit` argument as given (a ref name or an abbreviation; in `--tree` mode
   a directory path), not a resolved commit;
2. the checker's own blob is not recorded;
3. PDFs are not verified in `--commit` mode;
4. its evidence is one aggregate check with free-text discrepancies;
5. no result file is written on a crash;
6. `--commit` mode modifies the repository (`git worktree add`); the plan amendment decides this gap;
7. `set_fingerprints` skips silently when a coverage id is not found;
8. a stale docstring ("four coverage entries" against seven STALE entries).

The tool's `pdf` class and its disposable clone are mitigations on the tool side, not discharges.
Sources: RV-031, RV-032, RV-033, RV-034, RV-035, RV-036, RV-037, RV-038. Controls: none (outstanding
obligations of the plan amendment; verified at `F`, sec. 32).

**R6.PLAN.18** The following are requirements of the plan amendment, outstanding obligations (sec. 32: OBL-4, OBL-5 and OBL-9) and named blockers; the tool keeps only the mechanism (`checks` and `final_profiles` in the
configuration, sec. 25; `--final`, sec. 7):
- any restatement of item 7 is a plan amendment with its own preregistered text, an independent review
  of the deny set, the `resid` profile and the W1 rules, and the owner's authorization; it is not
  "passing as written", cannot be used in the current frozen trials, and must be adopted before any
  trial claims item 7;
- the proposed amendment check `terms --commit X --base H --ledger F:ledger.json --check item7 --final`,
  with `checks.item7` holding the profiles `ptr`, `count-grep`, `resid`, DR-1, DR-3, DR-4 and DR-5 and
  `final_profiles` `ptr` and `count-grep`: zero deny matches; every `ptr` and `count-grep` hit not
  classified by a reviewed rule or record FAIL `final-unclassified`; every unclassified `resid` hit
  REVIEW_REQUIRED;
- item 7's scope statement (`papers/*.md` and `book/*.md`), which names the active files outside it
  that still carry "the sixth structural assumption", and DR-1's ordinal alternatives as a corpus
  terminology decision;
- the wording corrections: item 4's "four entries" becomes seven; item 12's "execution head's parent"
  becomes "the ledger base `H`".
Sources: E-1284, E-1285, E-1287, E-1290. Controls: RT-I7A.

***

## 19. Placement, governance and landing paths

**R6.PLACE.1** `tools/ledger_coverage.py` is the entry point. It installs the wrapper of sec. 7 and
then imports the package.
Sources: E-1291. Controls: EI8, EI12, X7.

**R6.PLACE.2** `tools/ledger_coverage/engine/` holds the engine (sec. 24), its JSON Schemas, the
outcome checker and the in-memory self-test fixtures; no fixture file is tracked. This directory is
the purity scope of the purity lint.
Sources: E-1292, V2-114. Controls: Z9a, Z9b, Z9c, Z9d, Z9e, Z9f, Z9g, Z9h, Z9-STAGED.

**R6.PLACE.3** `tools/ledger_coverage/adapters/` holds the adapter modules: the A1 adapters, the
delegation class adapters, the synthetic configuration's adapters, and the control runners
(`a1_controls.py`, `conformance_controls.py`, `record_directory_controls.py`). It is outside the
purity scope; each module is pinned by blob in the configuration that uses it, and every tool file is
listed in the configuration's `tool.files`.
Sources: E-1293, A-128. Controls: Y10, TR48, TR52.

**R6.PLACE.4** Constants that bound what a configuration may claim form a named exception class: such
a constant lives in a pinned tool file outside the engine, never in a configuration, since a
configuration cannot admit itself. The class has one member, the tuple of admitted record directories,
exactly
`('verification/audits/foundations/a1exit-deletion-20261121',)`,
held in its own module `tools/ledger_coverage/record_authority.py` (the module keeps its name; it
predates the term "admitted record directories"). The engine contains no retirement constant. The
module is a tool file like any other: listed in `tool.files`, pinned by the tool-landing class record
and checked by the pre-run pin check. No configuration, record or command-line argument adds to the
tuple; changing it is a tool revision.
Sources: A-009, A-020, A-023, A-024. Controls: RDIR-16, MUT:o9:RDIR-m4, TR48, Z9g.

**R6.PLACE.5** A new audit directory under `verification/audits/` holds the rule files, scope records,
HP, context and hit classification records, review records, reconciliation records, and the tool's
landing record of the real-tree runs with their commits, commands, counts and results.
Sources: E-1294, V1-148, V2-115. Controls: none (placement; verified by review).

**R6.PLACE.6** The plan's `delegation.json`, `hp.json`, `retirement-config.json`, rule files,
`context-adjudications.json` and `hit-classifications.json`, frozen with the plan, live in the amended
plan's record directory.
Sources: E-1295. Controls: RDIR-1, I2-3.

**R6.PLACE.7** The tool reads every record from git objects, which `export-ignore` does not affect.
Sources: E-1296. Controls: O6, GV4.

**R6.PLACE.8** The tool's landing adds paths only under `tools/`, under its audit directory, and at
the pinned workflow path `.github/workflows/ledger-coverage.yml`, the one path outside those two. It
touches no ledgered path. The landing check of the tool's own pull request verifies both, and checks
the tool-landing head against `H`: every path the landing changes relative to its first parent lies
under those paths, none is a path the ledger based at `H` touches, and a landing that touches one is
FAIL `base-drift`.
Corpus paths that the ledger does not touch are not excluded by this check; it covers the ledgered
paths, as stated (RE-34 (a)).
Sources: V2-118, E-1298, A-129. Controls: TT14, TT13, R19.

**R6.PLACE.9** Records strengthen no claim.
Sources: E-1299. Controls: none (governance; verified by review).

**R6.PLACE.10** The tool lands on `main` before the A1 retirement, by its own independent non-author
review and its own owner merge decision. The retirement plan is then amended, as a separate reviewed
record, so that each of its mandatory checks names an operation of this tool and its exact command and
passes as written. No check is waived, replaced after the freeze, or recorded as a deviation. Landing
the tool decides nothing about the retirement: the plan amendment and its freeze, the repeated trials,
the execution and the merge each keep their own owner gate.
Sources: V2-116, V1-140. Controls: none (governance; verified by review).

**R6.PLACE.11** Every tool revision, including the one that implements this design, follows these
steps: implementation, then independent implementation review against r6; the tool's full local suite
(self-test, purity, synthetic, conformance, A1 conformance and controls, mutation), with the mutation
evidence re-established for the changed code; then one disposable CI validation run of the exact
implementation commit, which is a launch and needs the owner's approval; merge to `main` by separate
owner approval; then the post-merge verify run.
Sources: A-133, A-134, A-135. Controls: none (governance; the suite is the catalogue of sec. 17).

**R6.PLACE.12** Wiring the tool into the release gate is a separate change with its own review.
Sources: V1-144. Controls: none (governance; verified by review).

***

## 20. Four trees

**R6.TREE.1** `execution` takes the roles below as flags, each resolved once to a full commit id and
recorded in the result's `roles`:
- scientific base `H` (`--scientific-base`): what the retirement edits are relative to (spans, old
  hashes, pins, sites);
- integration base `M` (`--main`): which side changes the landing must carry;
- candidate `X` (`--candidate`): the retirement's own tree;
- certified execution head `C` (`--certified`, optional): when absent, `C` equals `X`;
- landing `L` (`--landing`, optional): the merge commit, or an in-memory merge for prediction.

`C` is the certified execution head throughout; `E` is only the ledger pin.
Sources: V2-124, E-1300. Controls: TT1, TT5, TT6, R16.

**R6.TREE.2** `H` equals the ledger's `base` and `roles.scientific_base` in the frozen configuration
record; otherwise ERROR `SCIENTIFIC_BASE_MISMATCH`. Every ledgered file's blob at `H` hashes to its
`base_sha256`; otherwise ERROR (exit 65) with the class the pinned-input role rule of sec. 7 assigns.
The anchors and the HP provenance chain end at `H`. `H` is never re-derived from `M`, `X` or `L`. The
tree of the frozen record `R` at `H` is the pinned tree; `R` and its ledger checker stay
byte-identical and are read, never replaced.
Sources: V2-125, V2-126, V2-127, V2-128, E-1301, V1-147. Controls: TT5, M5, M9.

**R6.TREE.3** Op C resolves the pre-edit tree as the ledger's `base`, which must be `H`; it never uses
`main` or the commit checked out.
Sources: V2-014. Controls: TT5, TT3.

**R6.TREE.4** `M` is resolved once and recorded. `H` is on `M`'s first-parent chain; otherwise ERROR
`MAIN_NOT_DESCENDANT`. The tree of `R` at `M` is pinned. Every path that differs between `H` and `M`
is a side change, listed with the first-parent commit on `M` that made it. Directory admission and the
conditions DIR2-DIR5 of sec. 21 are evaluated in the `M` role with `--freeze`, as role-dependent
validation.
Sources: V2-129, V2-130, E-1302. Controls: TT6, RDIR-23.

**R6.TREE.5** Side changes are classified by reviewed side-change class records (schema
`oi-side-change-classes/1`). A class binds each path it covers to its pinned blob (`git_blob` and
`blob_sha256`). A path matches a class only if its path matches and its blob at `M` equals the pin.
The tool-landing class lists every path the tool's landing commit adds under its prefixes, each with
its exact blob; a prefix only says where such paths may lie and never classifies a path by itself. The
one path a class record cannot pin is the class record itself, whose `{path, blob_sha256}` the
configuration pins. A path under a prefix that is not listed, or whose blob differs from its pin, is
REVIEW_REQUIRED `side-change-unclassified`. A class id is defined exactly once across all class records
the configuration references or `--classify` admits; two definitions of one id, in one record or
several, are ERROR `CONFIG_INCONSISTENT`. An unclassified side change is REVIEW_REQUIRED
`side-change-unclassified`. Side changes are never retirement edits. Inside the plan's record
directory the rule of sec. 21 also applies.
Sources: E-1303. Controls: R18, R18-engine, R19, R19-engine, Z11, TT13, RDIR-24.

**R6.TREE.6** A side change touching no ledgered or corpus path is classified by a side-change class
record, or as `record-directory` (sec. 21), or is unclassified. It is reported under obligation
`MAIN`, never under `RET`, and is not a retirement edit (for example the trial workflow, the tool's
landing and the plan amendment).
Sources: V2-131. Controls: TT1, RT-X, RDIR-5.

**R6.TREE.7** A side change touching a ledgered or corpus path is `base-drift` (obligation `MAIN`),
decided before any classification: the retirement's spans no longer describe `M`. It is a FAIL for the
landing unless a reconciliation record applies under sec. 23, and it never makes `X` fail. A corpus
path changed on `M` is `base-drift` and is not checked as an unledgered segment `H..M`; v2's op B on
`L` is retired (sec. 33).
Sources: V2-132, V2-133, A-052. Controls: TT7, TT14, N16-file.

**R6.TREE.8** Outside the plan's record directory the side-change scan compares blob entries between
`H` and `M`; the completeness check of sec. 21 applies inside that directory alone. The entry type of
every side change is checked before any byte is read (sec. 21).
Sources: A-137. Controls: RDIR-5, SIDE-NONREG.

**R6.TREE.9** `X` has exactly one parent, and it is `H`; otherwise FAIL `candidate-parent`. Every path
in the diff from `H` to `X` is in exactly one class: ledgered, delegated or record. Every ledgered file
equals `H` plus its splices. Every other path is byte-identical to `H`. The pins and preconditions are
evaluated at `H`, the postconditions at `X`. No check of `X` reads `M`, so a side change is never
mistaken for a reverted retirement edit.
Sources: V2-134, V2-135, V2-136, V2-137, E-1304. Controls: TT3, TT4, TT2, S11-14.

**R6.TREE.10** When `C` differs from `X`, `C` descends linearly from `X`. Each commit `c` after `X` on
that chain, with parent `p`, is classified path by path, as `X` is against `H`: every path in the diff
from `p` to `c` is in exactly one class (ledgered, delegated or record); a ledgered path equals `H`'s
bytes with the ledger's splices applied; a delegated path is checked by its class at `C`; a record
path is one the plan's record directory admits after `F`. Any other changed path is FAIL
`unauthorized-change`, naming the commit. A commit with more than one parent is FAIL
`candidate-parent`. The tree of `C` is then checked as a whole, as `X` is.
Sources: E-1305. Controls: R16, R17.

**R6.TREE.11** `L` has exactly two parents, and the second is `C`; otherwise FAIL `landing-parents`
(this includes swapped parents). The first parent equals the recorded `M`; otherwise FAIL
`landing-first-parent-not-M`. The landing record states `M`.
Sources: V2-138, E-1306. Controls: TT9, R15.

**R6.TREE.12** Each path `p` of the landing is composed as follows, with `dC = C[p] != H[p]` and
`dM = M[p] != H[p]`:
- neither changed: `L[p]` equals `H[p]`;
- only `C` changed: `L[p]` equals `C[p]`;
- only `M` changed: `L[p]` equals `M[p]`; otherwise FAIL `landing-drops-main-change`;
- both changed and `C[p]` equals `M[p]`: `L[p]` equals that blob; the path is not a conflict;
- both changed to different blobs (a conflict):
  - a ledgered path passes only if `L[p]` equals the composition: `M`'s bytes with `C`'s splices
    applied at their `M`-translated offsets (R6.TREE.13). The composition is computed and compared for
    every such path on every landing check, whether or not a reconciliation record names the path; no
    record stands in for it (sec. 23);
  - a generated artifact is REVIEW_REQUIRED (`delegated-evidence-missing`, obligation `MAIN`) until it
    is regenerated from `L`'s sources under the delegation contract; a reconciliation record is not an
    alternative to regeneration. The regeneration is verified by a procedure, to be specified explicitly
    and reviewed independently, in which the trusted checker establishes the expected output itself and
    compares bytes; the evaluated tree's claim of regeneration is never sufficient. Until that procedure
    is specified and reviewed, the path is REVIEW_REQUIRED for every candidate `L` (LC-7);
  - any other conflict, including a ledgered path whose `L[p]` differs from the composition, is FAIL
    `landing-conflict-unresolved`.

Any other path content of `L` is FAIL `landing-extra-change`.
OPEN: derived-artifact landing blob.
Sources: V2-139, V2-140, V2-142, V2-144, E-1306, E-1307, E-1308, E-1309, RV-001, OC-4. Controls: TT7, TT8,
TT10, TT11, RL, RT-L, N10, N11, LC-1, LC-2, LC-3, LC-4, LC-5, LC-6, LC-7.

**R6.TREE.13** Translation. For a ledgered path, the `M`-translated offset of a splice is the offset of
the unique occurrence at `M` of the splice's old bytes, after those old bytes, taken from `H` at the
splice's span, are verified against `old_sha256`. A composition exists only if each splice's old bytes
occur exactly once at `M` and the translated splices do not overlap; each translated span's bytes are
re-verified against `old_sha256`. "Translation" in sec. 20 and sec. 23 means the ledger's splices at
their `M`-translated offsets.
This is the one definition of translation (RE-33 (a)): the landing check, the reconciliation
conditions and the landing builder that RT-L, RT-L2, TT7, TT8 and RL use all compose by it, as the
landing check's composition at the tool commit does (unique occurrence of the old bytes at `M`,
`old_sha256` re-verified). The builder at the tool commit maps lines by similarity and falls back to
`C`'s bytes; that is a verification defect, corrected in the tool revision (OBL-28, C-18). The
landing controls LC-1 to LC-7 state, for each composition case of R6.TREE.12, the fixture bytes and
the byte-exact expected landing blob, worked independently from this definition (Q15).
Sources: E-1307. Controls: N8, N13, TT8, LC-1, LC-2, LC-3, LC-4, LC-5, LC-6.

**R6.TREE.14** The landing carries exactly the execution's own diff: the diff `M..L`, restricted to
the paths `M` did not change, equals the diff `H..C`; and the diff `C..L` equals the side changes
`H..M`, except on reconciled paths. Each departure is an item of R6.TREE.12.
Sources: V2-143, E-1310. Controls: TT11, TT12.

**R6.TREE.15** The in-memory landing used for prediction (RT-L and RT-L2) is a synthetic commit object
held by the tool's reader. No merge or ref is created in the repository.
Sources: V2-165. Controls: RT-L, RT-L2.

**R6.TREE.16** Each item carries one obligation from this set:
- `HP`: the historical provenance obligation of the segment `E..H` (sec. 5);
- `RET`: the retirement edits, the candidate checks of `X` and `C`;
- `MAIN`: the integration base and the landing: side changes, `base-drift` and the landing classes;
- `RECORD`: records, their lint, admission and application (`record-invalid`);
- `TERMS`: terminology scans (deny matches, rule states, literal matches, unclassified and
  final-unclassified hits outside HP);
- `DELEGATED`: delegated evidence under the delegation contract (sec. 13).
Sources: none (approved decision enumerating the obligation set). Controls: TT1, TT7, RT-H0, N2, RT-D,
G2.

**R6.TREE.17** The verdict of each role check is reported separately in the result. A landing check
never re-derives the retirement edits from `M`, and a candidate check never reads `M`.
Sources: RV-001. Controls: TT2, TT7.

**R6.TREE.18** The role cases are each tested: an unclassified change on `M` gives REVIEW_REQUIRED
(R18, R19, RDIR-5); a first parent other than the recorded `M` fails (R15); an unclassified path in a
commit of `C` fails (R16, with R17 for a record path admitted after `F`); R18-engine and R19-engine
are the engine forms of R18 and R19 (B-7); op C on a correctly executed candidate gives PASS (TT13).
Sources: RV-ADD2-259-269. Controls: R18, R19, RDIR-5, R15, R16, TT13, R18-engine, R19-engine, R17.

***

## 21. The plan's record directory on M

The amended plan merges its pull request into `main` before the landing `L`, so every file of the
plan's record directory is a side change on `M`. The configuration, its review record and the
preregistration cannot be pinned by a class record frozen at `F` without a hash cycle. This section's
rule classifies those files.

**R6.RDIR.1** Notation. `F` is the run's admitted plan commit (`--freeze`, sec. 11). `P_cfg` is the
configuration's path in `F` (the path `--config F:P_cfg` names), and `D_rec` is the directory part of
`P_cfg`; for a configuration in the repository root `D_rec` is empty and no path is inside it. An
entry is a non-tree entry of a commit's tree with its mode, as the object reader lists entries:
regular files (`100644`, `100755`), symbolic links (`120000`) and submodules (`160000`). A path is
inside `D_rec` when it begins with `D_rec` followed by `/`; this one membership predicate is used by
every part of the rule (completeness, classification, application and DIR3). `F-entries` and
`M-entries` are the entries inside `D_rec` at `F` and at `M`.
Sources: A-015, A-016, A-017, A-018. Controls: RDIR-6, RDIR-10, MUT:o9:RDIR-m2.

**R6.RDIR.2** Directory admission. The rule is active only for a directory the tool itself admits,
independently of any configuration: `D_rec` must equal one member of the tuple of admitted record
directories (R6.PLACE.4) by string equality. The tuple is fixed by the tool's review and landing and
pinned by every configuration's `tool.files`; no configuration, record or command-line argument can
add to it, and changing it is a tool revision. The constant guards every run of the tool, whereas a
check in the pinned workflow would guard only runs of that workflow.
Sources: A-019, A-021, A-022, A-138. Controls: RDIR-16, RDIR-20, MUT:o9:RDIR-m4.

**R6.RDIR.3** Scope of evaluation. Directory admission, the conditions DIR2-DIR5 and the completeness
check are evaluated only by an operation that evaluates `M` with an admitted `F`: the `M` role of
`execution` (`--main` with `--freeze`; item 14's candidate and landing commands and the RT-L2
safeguard), and condition RC11 of the reconciliation records it evaluates. Every other operation
(`record`, `coverage`, `terms`, `execution` without `--main`, and any operation without `--freeze`)
evaluates none of them. This is role-dependent configuration validation (sec. 29).
Sources: A-025. Controls: RDIR-23, RDIR-14.

**R6.RDIR.4** Within that scope, from `H`, `F`, `M` and the configuration, before any side change is
classified:
- DIR5 is evaluated always;
- if `D_rec` is admitted, DIR2-DIR4 are evaluated, then R6.RDIR.6 to R6.RDIR.10 apply;
- if `D_rec` is not admitted and `M` holds no entry inside `D_rec`, the rule is inactive and the run
  continues unchanged;
- if `D_rec` is not admitted and both `H` and `M` hold an entry inside `D_rec`, the rule is inactive and
  the run continues unchanged; every path inside it keeps the classification the run gives it without
  the rule;
- if `D_rec` is not admitted, `H` holds no entry inside `D_rec` and `M` holds an entry inside `D_rec`,
  the run stops with ERROR `CONFIG_INCONSISTENT` (directory not admitted). Such a `D_rec` has the shape
  of a plan's record directory introduced after `H`, and a configuration in any such directory other
  than the admitted one is refused.

A `D_rec` that is not admitted never receives a `record-directory` classification.
Sources: A-026, A-027, A-028, A-029, A-030, A-031, A-032. Controls: RDIR-10, RDIR-12b, RDIR-16,
RDIR-20, RDIR-22, RDIR-25, MUT:o9:RDIR-m15, MUT:o9:RDIR-m16, MUT:o9:RDIR-m17.

**R6.RDIR.5** The conditions. If any of DIR2-DIR5 fails, the run stops with ERROR `CONFIG_INCONSISTENT`
naming the condition, and no path is classified by the rule.
- DIR2: no entry inside `D_rec` exists at `H`.
- DIR3: no ledgered path, no corpus path (the configuration's `corpus.patterns`), no path under a prefix
  of any side-change class the configuration references, and no path under `.github/` lies inside
  `D_rec`, at `F` or at `M`.
- DIR4: `F`'s tree holds `P_cfg` and the file of record pins inside `D_rec`.
- DIR5: no side-change class in the run's admitted class set uses the class id `record-directory`, which
  is reserved for this rule. The admitted class set is every class from the class records the
  configuration references and from the class records admitted through `--classify`; a class record
  from either route that defines the id is ERROR `CONFIG_INCONSISTENT`.
The names DIR2-DIR5 replace the r5 labels D2-D5 so that they cannot be read as the residual-decision
labels RD-2 to RD-5 (RE-28; sec. 34).
Sources: A-033, A-034, A-035, A-036, A-037. Controls: RDIR-9, RDIR-11, RDIR-12, RDIR-17, RDIR-24,
MUT:o9:RDIR-m3, MUT:o9:RDIR-m7, MUT:o9:RDIR-m12.

**R6.RDIR.6** Completeness. The rule does not depend on the `H`-to-`M` side-change scan to find the
directory's files. When the rule is active, the tool compares `F-entries` and `M-entries` path by path
over their union. A path whose entries at `F` and `M` are both regular files with the same mode and the
same blob id, and whose bytes at `M` have the same sha256 as at `F`, is equal. Every other path is
unequal, with its reason: `absent at M` (in `F-entries` only), `absent at F` (in `M-entries` only),
`differs from F` (both regular, blob or mode differs), or `not a regular file` (a symbolic link or
submodule at `F` or at `M`). Because both entry sets are enumerated directly, a file of `F` deleted on
`M` is reported although it exists at neither `H` nor `M`.
Sources: A-039, A-040, A-041, A-044. Controls: RDIR-1, RDIR-2, RDIR-3, RDIR-4, RDIR-8, MUT:o9:RDIR-m1,
MUT:o9:RDIR-m5, MUT:o9:RDIR-m6.

**R6.RDIR.7** Entry type before any read. For every side change, inside `D_rec` or outside it, and in
the completeness check, the entry type is checked from the entries before any byte is read; a symbolic
link or submodule never reaches a byte read and never raises. Such a side change is REVIEW_REQUIRED
`side-change-unclassified` (`not a regular file`); inside `D_rec` the class-record classifier is never
called for it, in the `M` role and in RC11 alike, and the completeness check reports it as well.
Outside `D_rec` the tool at the tool commit passes a non-regular side change to the classifier's byte
read, which refuses it; that is a verification defect, corrected in the tool revision and tested by
SIDE-NONREG; outside `D_rec` the outcome is the same REVIEW_REQUIRED `side-change-unclassified`
(`not a regular file`) (RE-15).
Sources: A-042, A-046. Controls: RDIR-8, SIDE-NONREG, MUT:o9:RDIR-m10, MUT:o9:RDIR-m14.

**R6.RDIR.8** Each unequal path is an item REVIEW_REQUIRED `side-change-unclassified` naming the path
and its reason, whether or not the `H`-to-`M` scan lists it. An unequal path is never a FAIL and never
accepted.
Sources: A-043, A-139. Controls: RDIR-2, RDIR-3, RDIR-4.

**R6.RDIR.9** The completeness check is an independent, mandatory invariant. Its items are issued
whatever any other route decides about the same path: no class pin, class record or reconciliation
record waives an unequal path. A path that a matching class pin classifies at `M` but that differs
between `F` and `M` keeps the class route's entry in the side-change list and also carries the
completeness item, so the result is not accepting.
Sources: A-045. Controls: RDIR-21, MUT:o9:RDIR-m13.

**R6.RDIR.10** Classification inside `D_rec`. For every regular-file side change `p` found by the
`H`-to-`M` scan, the class-record classifier is applied first, with one of three outcomes:
- a class pin names `p` and matches `M`, or `p` is a class record the configuration pins: the rule is
  not applied, and the class stands;
- a class pin names `p` but differs from `M`, or `p` is a pinned class record whose sha256 differs: the
  rule is not applied, and `side-change-unclassified` stands, naming the class;
- no class pin names `p` and `p` is not a pinned class record: the rule is applied.

Where applied, `p` is classified `record-directory` exactly when the rule is active, `p` is inside
`D_rec`, no component of `p` is empty, `.` or `..`, and the completeness check finds `p` equal.
Otherwise `p` stays `side-change-unclassified` with the completeness reason, or with the reason
`outside the record directory`. A ledgered or corpus path is `base-drift` before any classification
(R6.TREE.7); by DIR3 none lies inside `D_rec`.
Sources: A-047, A-048, A-049, A-050, A-051. Controls: RDIR-1, RDIR-5, RDIR-7, RDIR-13, MUT:o9:RDIR-m8,
MUT:o9:RDIR-m9.

**R6.RDIR.11** The rule and the completeness check are one function, called with the same context
(`F`, `D_rec`, the admission check and DIR2-DIR5) by both places that classify side changes: the `M`
role of `execution` (item 14's candidate and landing commands and the RT-L2 safeguard), and condition
RC11 of a reconciliation record, which enumerates side changes on its own (sec. 23). Without
`--freeze` (control-harness runs without a stand-in `F`) the rule is inactive, the completeness check
is not evaluated, and the directory's files are `side-change-unclassified`.
Sources: A-053, A-054, A-056. Controls: RDIR-8, RDIR-14, RDIR-15, RDIR-18, RDIR-19, RDIR-20,
MUT:o9:RDIR-m11.

**R6.RDIR.12** Output. Each side change classified by the rule is listed with `class:
"record-directory"`, its first-parent commit, and its mode, blob id and sha256 at `F` and at `M`. The
result records `D_rec`, the admission match, the outcomes of DIR2-DIR5, and the completeness counts
(paths equal; paths unequal, by reason). The field list is part of the result schema (sec. 7).
Sources: A-058, A-059. Controls: RDIR-1, RT-O9.

**R6.RDIR.13** The literals the rule needs in the engine are engine enumerations: the reserved class id
`record-directory`, the reason strings (`absent at M`, `absent at F`, `differs from F`, `not a regular
file`, `outside the record directory`, `directory not admitted`) and the reserved prefix `.github/`.
The reserved class id
`record-directory` is an enumeration that the purity lint's enumeration rule admits. The reason
strings pass the lint's occurrence rule and are not allowlisted. The reserved prefix `.github/` is a
path literal that no enumeration admits; it moves to `record_authority.py`, which bounds what a
configuration may claim (OD-5's exception class), in the tool revision (RE-19 (b); OBL-28).
Sources: A-035, A-037, A-041. Controls: Z9g, Z9-STAGED.

**R6.RDIR.14** Real-tree control. RT-O9 runs `execution` on the predicted `M` (`main` plus the tool
landing plus the plan's record directory as it stands at the stand-in `F`). It computes the expected
set independently from the stand-in `F`'s tree (every entry inside `D_rec`, with its mode, blob id and
sha256) and requires the run's `record-directory` entries to equal that set exactly (no path missing,
none extra, modes and hashes equal), no unequal path, and no `side-change-unclassified`. These checks
run and are gated whenever RT-O9 runs. The further clause that RT-L2 holds on the same predicted `M` is
the separate row RT-O9-L2, which depends on RT-L2 (sec. 23).
The absence of `base-drift` on that `M`, which holds only through the drafted reconciliation record,
belongs to RT-O9-L2 with the clause that RT-L2 holds (RE-5 (a)).
Sources: A-087, A-088. Controls: RT-O9, RT-O9-L2.

***

## 22. Item-2 records

**R6.ITEM2.1** The `item2-coverage` arm of the pinned workflow `.github/workflows/ledger-coverage.yml`
passes, after its existing arguments and in this order, exactly
`--classify "$F:$D/context-adjudications.json" --classify "$F:$D/hit-classifications.json"`,
every expansion quoted. Here `$F` and `$D` are the workflow's shell variables, `$D` holding the
configuration's directory as the arm uses it for `ledger.json` and `hp.json`; they are not the
notation of sec. 21.
Sources: A-109, A-110, A-111. Controls: I2-1.

**R6.ITEM2.2** `--classify` is repeatable. An admitted record of schema `oi-context-adjudication/1` is
routed to the context collection, and every other admitted record to the hit classifications. The tool
routes by schema, not by file name. A file of the wrong schema under either name is admitted only if
the configuration references it and its review passes; its review checks that each file holds its
named kind.
Sources: A-112, A-119. Controls: I2-2, I2-7, I2-8.

**R6.ITEM2.3** `context-adjudications.json` has schema `oi-context-adjudication/1`, its adjudications
under `entries`, covering both the meaning-context and the indicator (structure) adjudications item 2
needs. `hit-classifications.json` has schema `oi-hit-classification/1`, its classifications under
`classifications`. Each lies in the plan's record directory, is referenced by the configuration's
`records` with its blob sha256, and has a non-author review record, as every other record (sec. 11): a
record the frozen configuration does not reference is never used (`record-invalid`), and a file absent
at `F` stops the run with ERROR `SOURCE_CHANGED`. Both files are required to exist.
Sources: A-113, A-114, A-117. Controls: I2-3, I2-4, I2-5.

**R6.ITEM2.4** Either file may hold an empty list when item 2 needs no record of its kind. It then still
carries its `record_id`, and its review, which the review chain binds to that `record_id` when the item
list is empty, states that the list is empty and why. This `record_id` requirement applies to empty
item-2 records only; it does not extend to other records, and a record with `supersedes: null` and no
`record_id` that no record supersedes remains valid.
Sources: A-117. Controls: I2-6, LN10.

***

## 23. Reconciliation records, re-resolving M, and the sequencing safeguard

**R6.RECON.1** A reconciliation record (schema `oi-reconciliation/1`) is reviewed and immutable, and
lives in the audit directory. It names the commits `M` and `X` and the paths it covers, its
`ledger_binding` (`ledger_base`, and the canonical sha256 of the path's `files` entry, of its splice
list and of its edit-list entries), `changes_decisions_on_X`, and for each path: `side_change_commits`,
the blob ids and sha256 at `M` (`m`, `m_sha256`), at the composed landing (`l`, `l_sha256`) and at the
candidate (`x`, `x_sha256`); for each splice its `start_H`, `end_H`, `start_M`, `new_sha256` and its
translation (`identity` or an offset); and the protected ranges at `M`, each with `start_M`, `end_M`
and `sha256`. Its review record names the reviewer, under the ownership chain of sec. 11.
Sources: V2-146. Controls: N3, N4.

**R6.RECON.2** A record written after `F` is allowed only for side changes on `M` that the freeze could
not foresee. It is under the ownership chain of sec. 11.
Sources: E-1341, RV-027. Controls: O8, N2.

**R6.RECON.3** A reconciliation record names a ledgered or corpus path that both `M` and the retirement
change (the "both changed" case of R6.TREE.12); naming a path `X` changes is therefore valid and never
by itself `record-invalid`. The record resolves conflicts by merits. It never relabels a side change as
a retirement edit or the reverse, never changes a decision of op C on `X`, and never relabels a failing
retirement check. The tool enforces this by running op C's candidate checks with and without the
reconciliation records and requiring identical items on `X`; any difference is FAIL `record-invalid`.
Sources: E-1342, V2-147, RV-027. Controls: N2, N3, N3-config-route.

**R6.RECON.4** A reconciliation record applies only if every one of its conditions RC1-RC13 holds at
the run's `M` and `L`. The tool evaluates each condition itself, from git objects, and never takes the
record's statement that it holds.
Sources: E-1343. Controls: N4, N5.

**R6.RECON.5** RC13 (ledger binding), checked first: the run's ledger has `base` equal to
`roles.scientific_base` and to the record's `ledger_base`, and the canonical sha256 (sorted keys, no
whitespace, UTF-8) of the path's `files` entry, of its splice list and of its edit-list entries equal
the record's `ledger_binding` values.
Sources: E-1344. Controls: N4.

**R6.RECON.6** RC1 (commit list): `H` is on `M`'s first-parent chain, and the first-parent commits on
`H..M` that change the path equal the record's `side_change_commits`, in order.
Sources: E-1345. Controls: N5.

**R6.RECON.7** RC2 (blob at `M`): the path's git blob id and sha256 at `M` equal the record's `m` and
`m_sha256`.
Sources: E-1346. Controls: N7.

**R6.RECON.8** RC3 (uniqueness at `H`): the path has at least one splice, and each splice's old bytes
occur exactly once at `H`, at the splice's start, hash to its `old_sha256`, and match the record's
`start_H` and `end_H`.
Sources: E-1347. Controls: N12.

**R6.RECON.9** RC4 (uniqueness at `M`): each splice's old bytes occur exactly once at `M`, at the
record's `start_M`, and the bytes there hash to `old_sha256`.
Sources: E-1347. Controls: N8.

**R6.RECON.10** RC5 (translation): each splice's translation is the one the record states. For an
`identity` translation, `H` and `M` agree byte for byte up to the splice's end and `start_M` equals the
splice's start; otherwise the offset of the unique occurrence at `M` minus the splice's start equals
the record's `start_M` minus the splice's start.
Sources: E-1347. Controls: N13.

**R6.RECON.11** RC6 (approved text): the composition exists, and at each translated splice it carries
the splice's new bytes, which hash to the ledger's `new_sha256` and equal the record's `new_sha256`; the
candidate carries the same new bytes at the splice.
At the tool commit RC6 reads the candidate's bytes at the splice's `H` offset, which is wrong after
an earlier length-changing splice in the same file; it fails closed and is a verification defect,
corrected in the tool revision with a control of two splices in one file, the first changing length
(OBL-28, C-19).
Sources: E-1349. Controls: N14.

**R6.RECON.12** RC7 (composed blob): the composition's git blob id and sha256 equal the record's `l` and
`l_sha256`.
Sources: E-1349. Controls: N9.

**R6.RECON.13** RC8 (candidate blob): the path's blob id and sha256 at `X` equal the record's `x` and
`x_sha256`, and the ledger's `expected_sha256` for the path equals that sha256.
Sources: E-1349. Controls: N15.

**R6.RECON.14** RC9 (protected bytes): the bytes of the composition after the last translated splice
equal `M`'s bytes after it, and every protected range the record lists occurs exactly once at `M` and
exactly once in the composition, with equal bytes and the recorded sha256; each protected range lies after the last translated splice
and has integer offsets (RE-29 (a)). A purpose check that this stricter form rejects no valid record
precedes adoption (OBL-28).
Sources: E-1348. Controls: N6.

**R6.RECON.15** RC10 (other ledgered files): for every ledgered file other than the record's path, the
blob at `M` equals the blob at `H`, and its sha256 at `M` equals its `base_sha256`. A difference from
the tool's evaluation of RC10 is a verification defect.
Sources: E-1350. Controls: N16, N16-file.

**R6.RECON.16** RC11 (classified side changes): every path that differs between `H` and `M`, other than
the record's path, is not a corpus path and is classified by a side-change class record or as
`record-directory`, evaluated by the one function of R6.RDIR.11 with the run's context; and, where the
record-directory rule is active, the completeness check finds no unequal path. A non-regular side
change inside `D_rec` fails RC11. A difference from the tool's evaluation of RC11 is a verification
defect.
Sources: E-1350, A-055. Controls: N17, RDIR-8, RDIR-15, RDIR-18, RDIR-19, RDIR-20, MUT:o9:RDIR-m11.

**R6.RECON.17** RC12: the record's `changes_decisions_on_X` is empty; otherwise the record is also
`record-invalid`.
Sources: E-1351. Controls: N18, N18-record.

**R6.RECON.18** If any condition fails, the record does not apply: the path stays `base-drift` (FAIL),
and the result names each failed condition. Each condition has its own control (R6.CTRL.21).
Sources: E-1352. Controls: N3, N4, N5, N6, N7, N8, N9, N12, N13, N14, N15, N16, N17, N18, TT8.

**R6.RECON.19** A record never replaces the composition. At landing, the composition rule of
R6.TREE.12 is evaluated for every path, with or without a record. A record's `l` is a prediction that
the tool checks against the composition: the landing passes for the path only if `L`'s blob equals the
composed blob and, where a record exists, the composed blob also equals the record's `l`. A record
whose `l` names any other blob (for example `X`'s copy, which drops `M`'s change) makes the path FAIL
`landing-conflict-unresolved` and the record `record-invalid`.
Sources: E-1353, V2-141. Controls: N10, N11, R8-S6.

**R6.RECON.20** Immediately before landing, `M` is re-resolved from `main` of the repository that
`repository_id` names (`git ls-remote`, read-only) and checked to equal `L`'s first parent. The landing
record quotes the resolved id and the command. A failed `git ls-remote`, an output without exactly one
`refs/heads/main` line, an id that is not a full 40-hex id or that the verified reader cannot read, or
an id other than `L`'s first parent refuses the landing. The consumer then requires `T` on `M`'s
first-parent chain.
When the re-resolved `M` differs from the predicted `M`, RT-L2 must hold on the re-resolved `M`
before the landing (RE-22 (a)).
Sources: E-1354. Controls: EI5, TR29, RT-L2.

**R6.RECON.21** Sequencing safeguard. Before the tool lands, RT-L2 runs `execution` against a predicted
`M` that contains the tool's landing paths, with an in-memory landing (R6.TREE.15), at `X` = `C` =
`X_rep` (R6.EVID.8). The reviewed reconciliation record names that `M` and so is not among its paths:
the run names it from a commit outside the tool's landing paths, and it reaches `main` in a commit
after the tool's landing commit. It requires every
side change classified, and its drift state is one of three:
- no drift: no `base-drift` at the predicted `M`; RT-L2 holds;
- validly reconciled: every drifted path is covered by a reconciliation record whose review record
  passes record lint and which is bound to the run: its `ledger_base` is the run's `H`, it names the
  run's `M`, and its `m` and `x` blob ids for each path equal the path's blobs at the run's `M` and
  `C`; RT-L2 holds;
- unresolved: anything else, including a drifted path covered only by a drafted or unreviewed record;
  RT-L2 fails.

Until a reviewed reconciliation record bound in that way exists for every drifted path, RT-L2 is NOT
RUN, with that release condition; it is never PASS on a drafted record. The RT-L2 PASS recorded by CI
run 45569710442, made on a drafted record, does not establish the safeguard. The safeguard remains an
outstanding obligation and a named blocker on the tool's landing (sec. 32, OBL-13) until RT-L2 is released and
holds. RT-O9-L2 depends on it.
Sources: E-1355, OC-3. Controls: RT-L2, RT-O9-L2, GATE-13, GATE-14, GATE-15, GATE-19.

***

## 24. Engine, purity scope (Z9), generality

**Scope (not a verifiable requirement).** Sections 24 to 30 specify one engine and two configurations
of it. They do not specify a second real retirement, a generic verifier of scientific proofs or of
semantic correctness, any reduction of A1 coverage or preservation obligations, or any postponement of
a review defect. Only the A1 adapters and one minimal synthetic adapter set are specified. Sources:
E-1373.

**R6.CORE.1** The tool has one engine. Every operation (`record`, `coverage`, `execution`, `terms`)
is a configuration of that engine, not a separate code path. The engine is retirement-independent and
contains exactly:
- the pipeline of sec. 3;
- the outcomes, exit codes, precedence, acceptance checker and result writer of sec. 7;
- the algorithms: anchors, translation and content search (sec. 4), the overlap and image rules
  (sec. 4), the region walk and merger reporting (sec. 5), the context hash, the indicator machinery
  and structure contexts with definitions supplied by the configuration (sec. 6), sentence splitting
  version 2 with the abbreviation list supplied by the configuration (sec. 8), rule application and
  record lint (sec. 10, 11);
- the four role checks (sec. 20);
- the object reader of sec. 11 (`git cat-file --batch`, with recomputed object ids);
- the adapter interface definitions (sec. 26) and the loader that admits adapter modules by pinned
  blob;
- the configuration loader and validator (sec. 25, 29);
- the purity lint Z9 (R6.CORE.3).

Sources: V2-012, E-1375. Controls: Y8, Z9g.

**R6.CORE.2** The engine contains no commit or tree id, no path of a retirement record, no
retirement terminology, regex pattern, site or hit count, PR number, delegation class, context-field
value, adapter name or checker schema. Adapters, which carry their retirement's schema strings (for
example "a1exit deletion exact-edit ledger v2"), lie outside the engine, in
`tools/ledger_coverage/adapters/`. The following literals are engine enumerations and are listed by
name in the allowlist of R6.CORE.5: the reserved side-change class id `record-directory`, the reason
strings of the record-directory rule (`absent at M`, `absent at F`, `differs from F`,
`not a regular file`, and the reasons naming DIR2-DIR5 and `directory not admitted`), and the path
prefix `.github/` used by condition DIR3. Sources: E-1376, RD-20. Controls: Z9a, Z9b, Z9c, Z9d, Z9g.

**R6.CORE.3** Z9, the purity lint, runs over the source blobs of `tools/ledger_coverage/engine/` and
the entry point `tools/ledger_coverage.py`, parsed by `ast`. Its scope is exactly those blobs; adapter
modules and `record_authority.py` are outside it. It fails on any of:
- a hexadecimal literal of 7 or more hex digits standing alone, in a string or as a number, including
  any 40-hex literal;
- a string literal equal to a string value of the value set, unless the value is on the allowlist. The
  value set is every string value occurring in the A1 configuration, in a record it references, in any
  record its adapters read (the adapter companions: `ledger.json`, `edits.json`, `sitemap.json`,
  `rows.json`, the Phase-0 `sites.json`, and every other file named in an adapter's `path` or
  `companion`), and in the synthetic configuration;
- a string literal or identifier matched by any review or deny profile of the A1 configuration.

Sources: E-1377, E-1378, RD-31. Controls: Z9a, Z9b, Z9c, Z9d, Z9e, Z9f, Z9g, Z9h.

**R6.CORE.4** The engine reads nothing from a ledger but the fields of the ledger interface
(R6.ADAPT.2). Retirement semantics such as guard-pin handling (an edit kind `guard-pin`, `pin_note`
values, a literal-piece filter, a read of a ledger field outside the interface) belong to the ledger
adapter, which returns them through the interface field `guard_pins`. With the adapter companions in the
value set, a planted `'guard-pin'` in an engine module is a lint FAIL (Z9h), and the real engine tree
with the extended value set gives no finding (Z9g). Sources: E-1378, RD-31, MC-9. Controls: Z9g, Z9h.

**R6.CORE.5** The allowlist is fixed in the engine and is itself linted to contain only:
- the interface field names of sec. 26 and of the engine's record schemas (for example `id`, `file`,
  `start`, `end`, `new`, `old_sha256`, `new_sha256`, `splices`, `sites`, `base`, `files`, `retained`,
  `mirrors`, `site_id`, `pin_line`, `carried`, `row`, `code`, `owner`, `author`, `reviewer`,
  `reviewed`, `verdicts`, `supersedes`, `path`, `blob_sha256`, `segment`);
- the engine's own schema ids, as listed by the schema files of sec. 7 and sec. 11 (among them
  `oi-ledger-coverage/5`, `oi-retirement-config/1`, `oi-term-rules/2`, `oi-delegation/1`,
  `oi-hp-adjudication/1`, `oi-context-adjudication/1`, `oi-hit-classification/1`, `oi-scope/1`,
  `oi-side-change-classes/1`, `oi-reconciliation/1`, `oi-review-record/1`);
- the engine's own enumerations: outcome names, sec. 15 class names, ERROR and configuration class
  names, extractor kinds, `review`, `deny`, `tree`, `added-text`, `accept`, `reject`, `dissent`, and the
  enumerations named in R6.CORE.2.

Allowlisting a value that also occurs in a companion (for example a control id equal to a row code)
requires that the value be an engine enumeration listed by name. Sources: E-1379, E-1378, RD-20,
OD-24. Controls: Z9e, Z9g.

**R6.CORE.6** Z9's controls run the lint on an in-memory engine tree (Z9a-Z9f) and on the real engine
tree (Z9g). Z9f's adapter half lints the real adapter sources: its linted source map is non-empty and
includes the adapter modules. Z9 runs in CI and in `self-test`; a failure in `self-test` is VOID. The
purity job records its result under the control id Z9-STAGED. Sources: E-1380, VD-9, RD-25. Controls:
Z9a, Z9b, Z9c, Z9d, Z9e, Z9f, Z9g, Z9h, Z9-STAGED.

**R6.CORE.7** Generality is accepted only if every A1 control of sec. 17 has, under the configured
engine, the outcome the expectation file states for it, compared item by item (acceptance criterion
S13, R6.A1CFG.7). The acceptance gate remains A1 correctness and fail-closed verification. Sources:
E-1374, MC-13, OD-8. Controls: GATE-18, Y8.

**R6.CORE.8** The tool never writes a tracked file, never runs a `git` command that changes refs, the
index, the object store or worktrees, and never calls a frozen tool's `main()`. Every file it writes
lies under the caller's `--out` directory. Sources: V1-027, V1-028, RD-15, RD-11. Controls:
OUT-CONFINED.

***

## 25. Configuration record, widening, admission

**R6.CFG.1** A retirement is configured by one reviewed, versioned JSON record,
`retirement-config.json`, in the retirement plan's record directory, frozen with the plan at `F` and
held under the ownership chain of sec. 11. Its SHA-256 is listed in the pin table of `F`: the last
`Record pins` subsection of the `PREREG.md` beside the configuration in `F`'s tree (sec. 11). Sources:
E-1389, E-1390. Controls: TR2, ADM-CONFIG-AT-F.

**R6.CFG.2** The tool reads the configuration only as `--config F:<path>` from the object store,
never from a caller-supplied file or another commit. A configuration that is not admitted from `F`'s
pin table (absent from it, or with a hash different from its listed SHA-256) is ERROR
`CONFIG_UNREVIEWED`, exit 65. ERROR `SOURCE_CHANGED` is reserved for an input that the admitted
configuration pins (R6.VALID.3). Sources: E-1391, OD-4. Controls: TR2, TR3, EI4, ADM-CONFIG-AT-F.

**R6.CFG.3** A change to the configuration after `F` requires a new configuration version, with
`supersedes` naming its predecessor, and a new freeze. Sources: E-1392. Controls: TR2, LN4.

**R6.CFG.4** The configuration has schema `oi-retirement-config/1`. All fields below are required
unless marked optional:
- `schema`: `oi-retirement-config/1`;
- `config_id`, `version`, `supersedes`: identity; `supersedes` is `{path, blob_sha256}` or null;
- `retirement`: name and accountable Issue;
- `roles`: `scientific_base` (full commit id); `pin` and `record_commit` (optional, for replay);
  `side_change_classes` (`{path, blob_sha256}`);
- `corpus`: an exact path list, or declared path sets with stated patterns, in a scope record
  (sec. 11);
- `adapters.ledger`: `{adapter, adapter_version, module: {path, blob_sha256}, path, blob_sha256,
  companion: [{role, path, blob_sha256}]}`;
- `adapters.sitemap`: as `adapters.ledger`, or null when the retirement has no frozen site map;
- `adapters.replay` (optional): `{adapter, adapter_version, module: {path, blob_sha256}, module_path,
  record_tree, functions}`, or null;
- `profiles`: `[{name, kind: review or deny, scope, applies_to: tree or added-text, source: {commit,
  path, blob_sha256, extractor: {kind, selector}}, pattern_sha256}]`;
- `checks`: one entry per plan check that op `terms` implements, `{id, profiles, final_profiles}`;
  `final_profiles` lists the review profiles whose REVIEW items `--final` converts for that check
  (sec. 7);
- `rules`: `[{path, blob_sha256}]`, rule files of schema `oi-term-rules/2`;
- `context_mapping`: `{source_field, values: {value: bool}, default: "invalid"}`; a value outside the
  table is a configuration error;
- `indicators`: the exact indicator definitions and effects of sec. 6, as data (patterns, word lists,
  effect per indicator);
- `sentence`: `{splitter_version, abbreviations}`, with `splitter_version` naming the splitter of
  sec. 8;
- `hp_obligations`: `[{segment: [from, to], merges: [{pr, commit, first_parent}]}]`;
- `delegation`: `{path, blob_sha256}` (`oi-delegation/1`) with `class_adapters: [{adapter,
  adapter_version, module: {path, blob_sha256}}]`, or null;
- `records`: every record and review record the run may use, `[{kind, path, blob_sha256}]`, including
  the item-2 records `context-adjudications.json` and `hit-classifications.json` (sec. 22); a kind this
  design does not define, such as `oi-owner-authorization/1`, is ERROR `CONFIG_INVALID`;
- `tool`: `{files: [{path, blob_sha256}], workflow: {path, blob_sha256}}`: every file of the tool (the
  entry point, every file under `tools/ledger_coverage/`, including `record_authority.py`) and the
  pinned workflow whose runs may produce an acceptable result (sec. 11, execution identity; sec. 19);
- `repository_id`: the numeric host id of the repository whose runs may produce an acceptable result;
- `operations`: the supported subset of `record`, `coverage`, `execution` and `terms`;
- `controls`: `{path, blob_sha256}` of the retirement's controls file, which supplies each control's
  `operations` and `direction` and the file's `control_inputs`; expected results are stated only in
  the expectation file (sec. 16);
- `author`: the configuration's writer; its review is a record under sec. 11.

Sources: E-1393, E-1394, E-1395, E-1396, E-1397, E-1398, E-1399, E-1400, E-1401, E-1402, E-1403,
E-1404, E-1405, E-1406, E-1407, E-1408, E-1409, E-1410, E-1411, E-1412, E-1413, E-1414, E-1415,
A-115, A-116, A-117, A-024, A-129, OD-1, OD-2, OD-7, OD-23, RD-32. Controls: Z1, Z2, Z3, Z6, Z6b,
CONFIG-LINT, Z8.

**R6.CFG.5** The supported extractor kinds are `json-pointer`; `python-ast-assign` (a module-level
name bound to a string, a tuple of strings, a dict of strings, or a compiled regex call with a literal
pattern); `python-ast-call-arg` (the literal first argument of a named call, such as `re.split`,
inside a named module-level function); and `literal-list`. The extractor's output must hash to the
profile's `pattern_sha256`. Sources: E-1416. Controls: Z7, S11-58g.

**R6.CFG.6** The configuration takes the record lint of sec. 11, with these additions:
- every referenced blob, adapter modules included, exists at its stated commit (or at `F`) with its
  stated hash;
- `roles.scientific_base` equals the ledger adapter's reported base;
- the `hp_obligations` segments end at `scientific_base`, and every merge is on its first-parent chain
  with its stated first parent;
- every delegation class has a class adapter;
- no profile name is duplicated, and every `final_profiles` entry of a check is a review profile
  listed in that check's `profiles`;
- every deny profile has examples in a rule file and a countercontrol named there, the countercontrol
  being a real line of a scanned file or a control-only input of the controls file;
- the controls file names at least one positive and one adversarial control per configured
  operation;
- `tool.files` names the entry point and only paths under `tools/ledger_coverage/`, each once, and
  `repository_id` is a positive integer.

Sources: E-1417, E-1418, E-1419, E-1420, E-1421, E-1422, E-1423, E-1424, OD-1. Controls: Z7, Z8,
CONFIG-LINT, TR52.

**R6.CFG.7** Widening. Every change of a configuration compared with the configuration it
supersedes is widening, and needs a `widening_review` under sec. 11, unless it is on this non-widening
list:
- adding a deny profile, a review profile or a control;
- adding a scope path to a deny profile;
- a context-mapping value changed from false to true;
- adding an entry to a check's `final_profiles`;
- removing an allow rule file.

For definiteness, each of the following is widening (the list illustrates; the rule decides): a scope
removed or narrowed; any change to a scope record other than adding a scope path to a deny profile; a
deny profile removed or changed; any profile changed; a context-mapping value changed from true to
false; any change to `indicators`; an HP obligation removed; an HP obligation added, or a merge added to
one (a new merge turns a step that would be FAIL `provenance-foreign` into an adjudicable step, and a new
obligation for a further segment turns changes that would be RET `unauthorized-change` into adjudicable
HP sites; both can increase acceptance); a delegation class added; an allow-rule file added, or a new
allow rule without `supersedes`; a side-change class added or changed; an adapter added, or an adapter's
module blob or `adapter_version` changed; any change to `tool` or `repository_id`; an extractor kind or
selector changed; a sentence abbreviation added, or `splitter_version` changed; any change to
`operations`; an entry removed from a check's `final_profiles`, or a check removed from `checks`; a
control-only input added, removed or changed; a control removed or its expected outcome relaxed. A
widening without its review is ERROR `CONFIG_UNREVIEWED` (R6.VALID.3). Sources: E-1425, E-1426,
MC-20. Controls: Z10, Z5, LN4, Y4.

**R6.CFG.8** Admission is recorded in `result.json` as the object `config.admission` with members
`mode` and `snapshot`. `mode` is one of `chain`, `replay` and `control-harness`; only `chain` is
acceptable (sec. 7, sec. 11). For `chain`, `snapshot` carries the fields sec. 11 lists: the producing
run, `T` and its tool blobs, `F`, the pin table and the evaluated commits. The requirement that a run
have `--freeze` (TR1) applies to chain admission only. Sources: OD-29, OD-28, E-1459. Controls: TR1,
TR5, TR13, TR45-opB, X11.

***

## 26. Adapter interfaces

**R6.ADAPT.1** Each adapter is a module under `tools/ledger_coverage/adapters/` that declares an
interface name, an adapter name and an integer version. The engine admits an adapter only if the
configuration names it, its module blob hash equals the configured pin, and its declared interface,
name and version equal the configured ones. An adapter the configuration does not name, or whose
declared interface, name or version differs, is ERROR `CONFIG_INVALID`. A module whose blob differs from
its pin, or which is missing, is ERROR `SOURCE_CHANGED` (an input the admitted configuration pins). The
engine holds no adapter names. Sources: E-1427, OD-4. Controls: Z1, Z6, Y10.

**R6.ADAPT.2** The ledger interface returns: `base`; `splices [{id, file, start, end, old_sha256,
new_sha256, new}]` (byte spans at `base`); `files {path: {base_sha256, expected_sha256}}`;
`retained [{id, site_ref}]`; `mirrors [{id, mirror_of}]`; `guard_pins [{id, file, pieces, targets}]`
(the updated pin literals the edit list requires, with the retirement's own selection rules applied
inside the adapter); `ignored_fields`; and its validation errors (overlap, hash, schema). Sources:
E-1428. Controls: U10, U11, M3, M4, M5, Z9h.

**R6.ADAPT.3** The sitemap interface returns: `pin`; `sites [{site_id, file, pin_line, carried: {row,
code, owner, p0_id}, context_field_value, quote}]`; and `override_anchors`. It returns no
`read_entries`: no hit is held through a read entry, and a hit is held only by a tracked site (sec. 14).
`mirror_of` is taken from the ledger interface's `mirrors`. The carried classification has no
`relocation` member; the frozen tool's placement is verified as a whole by the replay's `build`
equality (R6.ADAPT.4). Sources: E-1429, V1-045, OD-16, VD-12, RD-11. Controls: U1, U12, RT-E, M7.

**R6.ADAPT.4** The replay interface returns `{equalities: [{name, equal}], errors: [str],
self_test: bool}`. It is computed by calling the named functions of a frozen module inside the
materialization of R6.ADAPT.5, under the wrapper of sec. 7. The equality names are fixed: `digest` (the
frozen manuscript digest against the frozen site map), `build` (the rebuilt site map against the frozen
site map, deep equality) and `render` (the rendered block spliced into the frozen ledger text against the
frozen bytes). The frozen checker's returned findings and unmapped-entry lists are recorded in `errors`,
and its self-test return in `self_test`. No printed text is read. Any equality that is false, or any
replay error, is ERROR (integrity, exit 65) naming the equality. Sources: E-1430, V1-031, OD-19.
Controls: M7, M8, RT-A.

**R6.ADAPT.5** Materialization. The replay materializes, under `--out/replay/`, every corpus blob at
`roles.pin` and every file of the replayed record tree (`adapters.replay.record_tree`) and of the
record directories it names at `roles.record_commit`, read by `git cat-file --batch` from the object
store; `git archive` is not used (the repository marks audit directories `export-ignore`). The frozen
module is imported from that materialization only, with `python3 -I -B` and `sys.path` set to the
materialized copy alone. The frozen tool's `main()` is never called. Sources: V1-030, V1-028, OD-3.
Controls: RT-A, M7, M8, OUT-CONFINED.

**R6.ADAPT.6** The delegation interface is the classes of sec. 13. A class adapter has
`verify(evidence, roles) -> PASS, REVIEW or FAIL` and returns a structured reason. Sources: E-1431.
Controls: Y6, RT-C.

***

## 27. A1 as the first configuration

**R6.A1CFG.1** The A1 configuration is `a1exit-retirement-config`, version 1. Every A1 constant lies
in that configuration, in a record it pins, or in an A1 adapter module it pins, with one named
exception class: constants that bound what a configuration may claim. Its one member is the tuple of
admitted record directories, held in `tools/ledger_coverage/record_authority.py`, a tool file outside
the engine, listed in `tool.files`, pinned by the tool-landing class record and checked by the pre-run
pin check. No configuration, record or command-line argument can add to it; changing it is a tool
revision. For this revision the tuple is exactly
`('verification/audits/foundations/a1exit-deletion-20261121',)`. Sources: E-1433, A-019, A-020,
A-022, A-024, OD-5, OD-6. Controls: RDIR-16, RDIR-20, Z9g, EI1.

**R6.A1CFG.2** The A1 constants have these destinations:

| Constant | Destination |
|---|---|
| `E`, record commit, `R` tree b05efdca935a42b9c94ef1748c964696bf58fcd9 | `roles.pin`, `roles.record_commit`, `adapters.replay.record_tree` |
| `H` | `roles.scientific_base` |
| `R` paths and the Phase-0/2 record paths | `adapters.sitemap`, `adapters.replay.module_path` |
| ledger and edits schema ids, `retained_unchanged`, `mirror_of` | the `a1exit-exact-edit/2` module, `adapters.ledger.companion` |
| frozen function names, line-523 handling | the `python-frozen-replay/1` module, `adapters.replay.functions` |
| corpus `papers/*.md`, `book/*.md` | `corpus` |
| profiles p0-core, p0-para, ledger-ext, ptr, repo, count-grep, item7-literal, register, infinity | `profiles` (sources: Phase-0 `sites.json`; `R/ledger_check.py` `EXTENDED_PATTERNS`; `P` `edits_check.py` `PTR`, `REPO_PAT`, `REG`, `CAPS`, `CAPS_OK`, `INF`, `NEUTRAL`; the item 7 literals of sec. 18) |
| `resid` (resid-a, resid-b, resid-c), DR-1, DR-3, DR-4, DR-5, W1, W2, the converted `EXPLAINED` entries | rule files under `rules` (plan records adopted at `F`, sec. 12), profiles naming them |
| item 7 and item 11 profile sets and `final_profiles` (`item7`: `ptr`, `count-grep`; `item11`: `repo`) | `checks` |
| DR-3's control-only witness input (`AGENTS.md` at `H`) | `controls` |
| repo scope (historical prefixes and files, generated artifacts) | a scope record under `records` |
| s3 mapping (sec. 6) | `context_mapping` (`source_field: s3`) |
| ANAPH, LIST, TABLE, PARTIAL definitions and effects | `indicators` |
| sentence abbreviations | `sentence.abbreviations` |
| the six pinned merges and PR numbers (R6.A1CFG.4) | `hp_obligations[0]` (segment `[E, H]`) |
| tex/pdf/record-dir/sc42/coverage-ledger/ci classes, STALE ids, SC42_BASE ca3a5bb2, `tex_sources` rule, `a1exit-checker-result-v1` | `delegation.json` and the class adapters' parameters in it |
| the tool's file and workflow pins; the repository id 1156244443 | `tool`, `repository_id` |
| W's workflow, the tool's landing paths | `roles.side_change_classes` |
| every HP, context, hit classification and review record, including `context-adjudications.json` and `hit-classifications.json` | `records` |
| the admitted record-directory tuple | `record_authority.py` (the exception of R6.A1CFG.1) |
| controls RT-*, SW*, the sec. 18 mapping and countercontrols | `controls` (operations, direction, control inputs); expected results in the expectation file |

Sources: E-1434, A-019, A-020, A-022, A-115, OD-5, OD-8. Controls: Z9a, Z9b, Z9c, Z9d, Z9g.

**R6.A1CFG.3** The A1 adapters, each under `adapters/` and pinned by blob in the A1 configuration,
are:
- `a1exit-exact-edit/2`, reading `ledger.json` ("a1exit deletion exact-edit ledger v2") and
  `edits.json` ("a1exit deletion edit list v1");
- `a1exit-sitemap/2`, reading the frozen `sitemap.json` ("a1exit site map v2"), `rows.json` and the
  Phase-0 quotes;
- `python-frozen-replay/1`, replaying `ledger_check.py`'s `manuscript_digest`, `build`, `render`,
  `splice_block`, `check`, `extended_unmapped` and `self_test`;
- the delegation class adapters `preserve-check-v1` (tex, pdf), `record-dir/1`, `rerun-equal/1`
  (sc42), `fingerprint-regen/1` (coverage-ledger) and `host-run/1` (ci).

The control runner module `adapters/record_directory_controls.py` is a tool file listed in
`tool.files`. Sources: E-1432, MC-12. Controls: RT-A, Z9f, RDIR-1.

**R6.A1CFG.4** The A1 HP obligation `hp_obligations[0]` has segment `[E, H]` and these pinned merges:

| PR | Merge commit | First parent | Sites first changed |
|---|---|---|---|
| #1470 | 0cd5d5bfb4f6641c8b08706c4eb636ee730ebbf0 | 1c7eedc402eafd2bac654484fa790874a33f444d | 15 |
| #1473 | a1f38284d21338b66119c870a551a670c73e3fa7 | f1c8c6b18b245c2faaa68abb464d70ab332b7bec | 15 (plus 3 second steps of #1474) |
| #1474 | 0ba358ccf05eb461c3a5bd686062f65115c293fc | a1f38284d21338b66119c870a551a670c73e3fa7 | 23 |
| #1472 | 4de2eabd6c7c88dc214db70a813ec44b8641b630 | 0adc410c4ad8c3ff51fc77ebb2e055506d758fc8 | 12 |
| #1475 | 7f28886f4cc96fbfa7407af1fdc37de2f0e562e5 | 4de2eabd6c7c88dc214db70a813ec44b8641b630 | 48 |
| #1494 | 53c6601a10419b6b333cc992474272501ab542af (= `H`) | fd9f99cc8866bd4f4244298f819fa99d5c707fba | 0 |

The first-parent chain from `E` to `H` has 14 commits; six of them change the corpus. The column
"Sites first changed" is a reference figure (sec. 31). Sources: E-065. Controls: RT-H0, RT-T0, H3.

**R6.A1CFG.5** In production, the A1 deny profiles scan `papers/*.md` and `book/*.md` only.
`AGENTS.md` is a ledgered file outside that scope; the production scan is not widened to it or to other
ledgered non-corpus files. DR-3's witness `AGENTS.md` at `H` is a control-only input. Sources: E-1012,
OD-8. Controls: RT-DR, RT-DR3W.

**R6.A1CFG.6** Counts such as 697, 113 and 19 are not configuration. They are expectations or
reference figures of the expectation file and figures of the landing record, classified under
sec. 31. Sources: E-1435, OD-1, OD-2, ME-3. Controls: GATE-16, RT-T0.

**R6.A1CFG.7** Acceptance criterion S13: the configured engine reproduces, item by item, every A1
control outcome of sec. 17 that the expectation file states, including the record-directory controls
RDIR-1 to RDIR-25 and RDIR-12b, RT-O9 (with its dependent clause as in OBL-14) and the item-2 controls
I2-1 to I2-8. Rule outcomes (deny, allow, `resid`) are measured with the plan's rule files as pinned
control inputs; the rules themselves are plan records adopted at `F` (sec. 12, OBL-3). The expected
outcomes of V4, V27, V27-glossary and V15 are deferred until the owner's decision on the V4 reversal
at r6's adoption (RE-1, OBL-6); until then they do not count toward S13.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1436, MC-13, OD-8, RD-14. Controls: GATE-18,
V5, V15, V27, V7a, V7b, V7c, V23, V24, V25, V26, RT-I7, RT-I7A, RT-DR, RT-DR3W.

***

## 28. Synthetic configuration and git fixtures

**R6.SYN.1** `synthetic-retirement-config` is held as in-memory fixture data under
`tools/ledger_coverage/engine/` (the self-test fixtures) and is never committed as a record. Its
adapters (`line-patch/1`, `artifact-hash/1`) are modules under `adapters/`, pinned by blob in the
fixture. It differs structurally from A1:

| Aspect | A1 | Synthetic |
|---|---|---|
| Ledger adapter | `a1exit-exact-edit/2` (byte spans, hashes) | `line-patch/1`: edits `{id, file, old_line_sha256, new_lines}`, located by unique whole-line hash |
| Site map | frozen sitemap | none: sites are declared in the configuration as `{site_id, file, line_sha256, carried}` |
| Replay | yes | none; op `record` unsupported |
| Profiles | Phase-0 and the plan's regexes | one review profile `axiom-Z` (`\bAxiom Z\b`), one deny profile `Z-premise` (`\bAxiom Z\b[^.]{0,40}\b(holds|assumed)\b`) |
| HP | one obligation, six merges | one obligation, one synthetic merge |
| Delegation | six classes | one class `artifact-hash/1`: a declared file must hash to a value computed by a declared deterministic recipe |
| Context field | `s3` | `kind`, with values `{definition: true, remark: false}` |
| Indicators | ANAPH, LIST, TABLE, PARTIAL | one: LIST |

The synthetic controls run on the same executable with no code change; the A1 and synthetic
configurations are run in one CI job by the same engine blob, and both results record the same engine
hash. Sources: E-1437, E-1438. Controls: Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10.

**R6.SYN.2** Synthetic in-memory cases build their trees through the same object-reader interface
that reads git objects; nothing is committed. Sources: V1-113, RD-15. Controls: Y1, Y8.

**R6.SYN.3** The conformance git fixture is separate from the in-memory fixture. It builds the
synthetic world as git objects for the controls that need commits (`F`, `M`, the four-tree and
record-directory controls), with the synthetic configuration directory `syn` present at the synthetic
`H`; it is neither a record nor committed to the repository. `syn` is not an admitted record
directory; under `execution --main --freeze` the record-directory rule is inactive for it, and every
conformance control that runs `execution --main --freeze` keeps its expected result. Sources: E-1437,
A-086, OD-31. Controls: RDIR-25, RDIR-12b.

***

## 29. Fail-closed configuration validation

**R6.VALID.1** Static validation of the configuration runs in the integrity stage (sec. 3), before
any subject is evaluated. Role-dependent validation (directory admission and conditions DIR2-DIR5,
sec. 21; the delegation contract; duplicate class ids among `--classify` records; declared-site
uniqueness; the HP segment chain) runs only in an operation that evaluates `M` with an admitted `F`, before any side change is
classified. No configuration defect can lead to PASS. Sources: E-1449, OD-27. Controls: Z1, Z2, Z3,
Z4, Z5, Z6, Z7, Z8, RDIR-11, RDIR-16.

**R6.VALID.2** Static defects and their outcomes:

| Defect | Outcome | Exit | Class |
|---|---|---|---|
| unknown `schema`, or unknown or mismatched adapter interface, name or version | ERROR | 65 | `CONFIG_INVALID` |
| missing required field, or unknown field | ERROR | 65 | `CONFIG_INVALID` |
| operation not in `operations` | ERROR | 65 | `CONFIG_UNSUPPORTED` |
| configuration controls file absent or empty for an operation | VOID | 70 | `CONFIG_NO_CONTROLS` |

Sources: E-1450, E-1451, E-1452, E-1456. Controls: Z1, Z2, Z3, Z4, Z6, Z6b, Z8, Y7.

**R6.VALID.3** A pinned or configuration input that fails is classified by its role:
- the configuration is not admitted from `F`'s pin table, its review chain is missing or failing, its
  reviewer equals its author, or it widens without review: ERROR `CONFIG_UNREVIEWED`;
- an input that the admitted configuration pins (adapter module, record, rule file, profile source,
  companion) is missing or differs from its pin: ERROR `SOURCE_CHANGED`;
- the configuration is malformed or names an undefined record kind: ERROR `CONFIG_INVALID`;
- the configuration is internally inconsistent: ERROR `CONFIG_INCONSISTENT` (R6.VALID.4);
- an execution-identity failure, such as a producing run whose head branch is not `main`: ERROR
  `CONFIG_UNREVIEWED`;
- a pinned input whose blob matches its pin but whose content fails its integrity rules (an unknown
  ledger schema id; the ledger integrity failures of M3-M5): ERROR `LEDGER_INTEGRITY`, or the
  named integrity class (`SCIENTIFIC_BASE_MISMATCH`); never `SOURCE_CHANGED` (RE-16);
- a pinned role or tree identity that differs: ERROR with the named class (RE-17 (i)); a malformed
  configuration is refused at admission first in a chain-admitted run (`CONFIG_UNREVIEWED`) and is
  `CONFIG_INVALID` in a control-harness run (RE-17 (ii));
- a record whose blob matches its pin but whose content fails its lint or its review, or a record
  passed with `--classify` that the configuration does not reference: FAIL `record-invalid`.

All ERROR outcomes here exit 65. Sources: E-1453, E-1454, A-116, OD-4, RD-18. Controls: TR2, Z5,
Y10, O6, I2-3, I2-4, Z1, TR29-tool, M3, M4, M5, TT5, O2.

**R6.VALID.4** ERROR `CONFIG_INCONSISTENT`, exit 65, is raised for: a base that differs from the
ledger's; a merge off the chain; a context value missing; an extractor hash mismatch; a duplicate
profile; a `final_profiles` entry that is not a review profile; a side-change class id defined more than
once; and, in the role-dependent validation of R6.VALID.1, a record directory that is not admitted
while `H` holds no entry inside it and `M` holds one (reason `directory not admitted`), or a failed
condition DIR2, DIR3, DIR4 or DIR5 (reason naming the condition, with no path classified by the rule).
Sources: E-1455, A-031, A-033, A-037, OD-6, OD-27, OD-31. Controls: Z7, Z11, RDIR-9, RDIR-11,
RDIR-12, RDIR-16, RDIR-17, RDIR-20, RDIR-24.

***

## 30. Reproducibility and the double run

**R6.REPRO.1** Every `result.json` records:
- `config`: `{config_id, version, path, commit, blob_sha256, admission: {mode, snapshot}}`
  (R6.CFG.8);
- each adapter's interface, name, version, module blob hash and input blob hashes;
- each profile's name, source commit, path, blob and `pattern_sha256`;
- every rule file's path and blob, and the id of every rule applied (in each explanation);
- every record and review record used, by path and blob;
- the delegation record hash and each class adapter version;
- the HP obligation's pinned merges;
- the tool commit `T`, the run's repository, head repository and event, and the engine blob hash (the
  entry point and every engine module), each tool blob equal to its `tool` pin;
- for the record-directory rule: the directory `D_rec`, the admission match, the outcomes of DIR2-DIR5,
  and the directory-completeness counts (paths equal, paths unequal by reason), with each classified
  side change listed as in sec. 21.

The complete field list is the result schema of sec. 7. Sources: E-1459, A-058, A-059, OD-24, OD-29,
OD-6. Controls: ACCEPT-SCHEMA, S7-schema-and-checker, TR5, X10, Y8.

**R6.REPRO.2** Two runs with equal inputs produce byte-identical `result.json`. CI runs each A1
real-tree operation and the synthetic configuration twice and compares the bytes; the gate checks both
retained results. Sources: E-1460, RD-2. Controls: REPRO-DOUBLE.

**R6.REPRO.3** The anchor map derivation is deterministic: `record_checks.anchors_sha256` is equal
across two runs and across two distinct CPython minor versions, and the A1 derivation has zero pin
findings. Sources: V1-133, V1-032, RD-11. Controls: REPRO-PYVER, RT-A.

**R6.REPRO.4** A run from a clean clone, with `--out` an empty directory outside the clone, writes
only under `--out`; afterwards `git status --porcelain` in the clone is empty and its refs and index are
unchanged. Sources: V1-127, V1-131, V1-027, RD-11. Controls: OUT-CONFINED.

***

## 31. Evidence and figures

**R6.EVID.1** A figure is an acceptance reference only if a control of the expectation file asserts
it (in `expect.counts`, `expect.sites` or an invariant) and the control's inputs are reachable from
`main`. The gate compares it with the gate-extracted actual; a difference is `declarative-mismatch` and
fails the gate (sec. 16). The counts are the implementation's to report; a deviation is investigated as
a defect, never fitted. A figure qualifies for current acceptance only as evidence of kind 2 or 3
(R6.EVID.7). Sources: E-035, E-036, E-019, E-1368, V2-106, ME-3, RD-3, OD-1. Controls:
GATE-1, GATE-6.

**R6.EVID.2** A figure in a row's `reference` field is informational. A difference between it and the
extracted figure is reported as `reference-difference`; it does not change the verdict, and it blocks
acceptance of the implementation step until it is explained. The preregistered rules are the
expectations; reference figures are never the rule. Sources: E-1175, E-035, OD-2. Controls: GATE-16.

**R6.EVID.3** The tool's landing record states, for each real-tree control, the commit on `main`, the
command that regenerates its result, and the counts it reports. Sources: V1-139. Controls: EI3, X10.

**R6.EVID.4** Acceptance references. The following figures are acceptance references, each through
the control named, on the condition of R6.EVID.1. Figures whose control runs on `X_rep` are acceptance
references through runs whose inputs are all reachable from `main` (R6.EVID.8). The figure whose
control needs `T1'` itself (item11-T1p) is an acceptance reference only while the objects of `T1'` it
needs are reachable from `main`, and otherwise a historical measurement (OBL-23).

| Figure | Control | Input |
|---|---|---|
| 697 sites; replay errors 0 | RT-A, RT-E | `E`, record commit |
| 113 `E..H` site changes (`hp-unadjudicated`); 7 HP `context-meaning-unverified`; 7 HP `context-structure-changed` | RT-H0, RT-T0 | `H` |
| 9 merger groups covering 22 sites | RT-T0 | `H`, `X_rep` |
| 19 region-attributed sites with untracked HP overlap (18 line-attributed); `papers/Substratum.md:266` with splice D029 | RT-T0 | `X_rep` |
| 383 unchanged, 197 replaced, 4 removed sites; 215 region lines; 168 sites moved by `H..X_rep` splices | RT-T0 | `X_rep` |
| 5 RET `context-meaning-unverified`; 3 RET `context-structure-changed` | RT-T0 | `X_rep` |
| `resid`: 45 REVIEW lines, 17 hit by no other profile; 11 W1/W2 lines PASS | RT-D | `X_rep` |
| literal item-7 greps at `X_rep`: "six structural" 7, "Fourteen" 0, "sixth of" 0, `\bA1\b` 4 | RT-I7 | `X_rep` |
| literal item-7 greps at `H`: 11, 1, 2, 179 | RT-I7 (after RD-3) | `H` |
| deny lines at `H`: DR-1 61 (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1, 86 distinct; at `E` 95 distinct | RT-DR (after RD-3) | `H`, `E` |
| DR-3 on `AGENTS.md`: one sentence at `H` (lines 37-39), none in `X_rep` | RT-DR3W | control inputs |
| 95 retired lines, each FAIL `final-unclassified` at `H`; at `H` 86 deny, 123 `final-unclassified`, 209 FAIL lines (93 and 216 with multi-line counting); at `X_rep` 0 deny, 12 `final-unclassified` | RT-I7A (after RD-3) | `H`, `X_rep` |
| 176 `final-unclassified` lines of the `repo` profile | item11-T1p | `T1'` |
| 584 sites swept, each with exactly one new RET FAIL | SW2 | `H` |
| 697 sites swept, each with exactly one new FAIL | SW1 | `E` |
| 399 splices verified at `H`; 23 corpus files and 21 other ledgered files conform | RT-C (after RD-3) | `H` |

Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-037, E-038, E-074, E-039, E-042, E-045, E-046, E-047, E-049, E-089, E-090, ME-3, RD-3,
RD-23, MC-1, MC-2, VD-10, RD-11, OC-3. Controls: RT-A, RT-E, RT-H0, RT-T0, RT-D, RT-I7, RT-DR, RT-DR3W,
RT-I7A, item11-T1p, SW1, SW2, RT-C.

**R6.EVID.5** Historical measurements. The following figures are not acceptance references. No
control on `main` reproduces them, or they were measured with P's code, at `T1'` by scripts that are not
retained, or under definitions r6 does not use. They are provenance (sec. A.42 item 2) and are kept in
the appendix:
- the s3 categories 346 / 136 / 109 / 106 and the per-merge attribution 48 / 23 / 15 / 15 / 12, and
  the three two-step HP sites (`papers/Main.md:224`, `papers/Main.md:732`,
  `papers/Substratum.md:92`);
- "31 distinct splices" over the `H..T1'` HP overlaps;
- v4's 203 region lines and its explanation;
- v4's `resid` figures 287 / 28 / 13 and the four lines added by the v5 widening;
- P's `classify()` breakdown of the 176 `repo` lines (96 / 31 / 14 / 35), 5486 lines in historical
  records and 2 in generated artifacts;
- the 12 meaning-context total, the "per unit" alternative 8, the 52 context changes and their split
  27 / 22 / 3, and the S0 indicator counts;
- the per-sentence deny counts under the unversioned "v5 splitter";
- 84 and 86 hit lines, 200 / 116 / 93 / 16 / 7 unheld lines, 226 distinct lines needing a record, the
  `ptr` 5 lines at `T1'`, the 4677-blob history search, and the reference rates of the indicator
  definitions;
- the parity figures 2822 / 2822, 16905 / 16905, 273, 4000 cases and 401 / 399 (OBL-2);
- every figure of v6.0e sec. 14 not listed in R6.EVID.4.

Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-037, E-038, E-039, E-042, E-045, E-046, E-047, E-089, E-040, E-041, E-043, E-044, E-048,
E-088, E-1356, E-1357, E-1358, E-1359, E-1360, E-1361, E-1362, ME-2, ME-3. Controls: GATE-16.

**R6.EVID.6** CI run 45569710442 on tool commit `a37992449b452021001277c06c524a30c92dfb87` is
provenance, not support. Its RT-L2 PASS was made on a drafted, unreviewed reconciliation record under
harness admission and does not establish the sequencing safeguard of sec. 23; RT-L2 is NOT RUN until
OBL-13 is discharged. Its step 6 exited 1 with verdict PASS because RT-T was NOT RUN, as the
preregistered decision rule requires. Sources: OD-18, Q2, MC-4, E-1363. Controls: RT-L2, GATE-13,
GATE-19.

**R6.EVID.7** Evidence kinds (Q16). r6 distinguishes four kinds of evidence, and each obligation of
sec. 32 names the kind that discharges it:
1. pre-merge candidate validation: a run recorded on the exact candidate commit of a pull request
   before its landing merge. It is evidence for the landing decision and is provenance (AGENTS.md
   sec. A.42 item 2) until the candidate commit is reachable from `main`. For a native round's freeze,
   the exact-candidate validation of the candidate `F` before its designation (AGENTS.md sec. A.39;
   TR5) is evidence of this kind for the designation decision, and it qualifies as kind 2 when
   the round's landing is on `main`;
2. qualifying landing evidence: once the landing merge is on `main`, the candidate commit is reachable
   from `main`, and a run recorded on it qualifies under AGENTS.md sec. A.42 item 1 with its recipe and
   its expected result, provided every other input the run read is reachable from `main` as well;
3. post-merge confirmation: the recipe re-run on `main` after the landing merge;
4. A1 execution evidence: runs of the A1 retirement execution, gated at `F` and made under the frozen
   plan.
Every figure carries two separate attributes: obtained (the run, its commit and what it showed,
recorded as provenance) and qualifies for current acceptance (evidence of kind 2 or 3). At r6's
drafting every figure of R6.EVID.4 is obtained and none qualifies: `T1'`, `P` and the tool commit
a37992449b452021001277c06c524a30c92dfb87 are not reachable from `main` (RE-36). A figure qualifies only
after the tool revision and its inputs are reachable from `main` and its run is recorded or repeated
there. No obligation is discharged by evidence of a kind it does not name, and no gate is passed by
an exception the obligation does not state.
Sources: RE-36, Q16, ME-3, RD-23, OC-1. Controls: none (definition of evidence kinds; verified by review).

**R6.EVID.8** Representative retirement candidate (OC-3). A control whose verdict reads only the trees
that `H` and a ledger determine runs on a representative candidate `X_rep`, never on `T1'`:
- Construction. `X_rep` is a commit object held by the tool's reader (as R6.TREE.15), with exactly one
  parent, `H`, and a fixed subject. Each ledgered path carries `H`'s bytes with the ledger's splices
  applied, and its sha256 equals the ledger's `expected_sha256` for the path; the plan's record-directory
  paths carry the pinned ledger and edit list; each path of the configuration's delegated classes
  carries a fixed marker blob that differs from its blobs at `H` and at the run's `M`; every other path
  equals `H`. Its commit and tree ids are a function of `H`, the ledger, the edit list and the
  configuration alone, and the result records them. The builder imports nothing from the tool's
  engine; REP-BUILD checks it in both directions.
- Inputs. `H` and `E`, both on `main`; the ledger and edit list as pinned control inputs landed with the
  tool revision: byte copies of the retirement ledger (git blob ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e,
  sha256 2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5) and edit list (git blob
  ec384fdfbc12937b860e2f226355e8c5d94820a5, sha256
  528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1); the controls use these pinned bytes,
  and their origin in `P` is provenance. For RT-T, the ledger and edit list frozen at `F`. Further: the class, rule and scope records of the tool
  revision; the configuration's control instance, a template landed with the tool revision whose pin of
  the side-change class record is filled by the runner from the landed class record, so that the
  template names no blob that the class record pins and K1-GRAPH's acyclicity is kept; and, for the
  landing roles, a pinned `main` commit `M0`. No input is `T1'`, `P` or the tool commit
  a37992449b452021001277c06c524a30c92dfb87.
- Why the safeguard is full. A conforming candidate (R6.TREE.9: one parent, `H`; each ledgered file `H`
  plus its splices; every other path `H`'s except delegated and record paths) carries, on every ledgered
  and corpus path, exactly the bytes of `X_rep`. Op B reads only the corpus and the segments `E..H` and
  `H..X` (R6.PUR.5), and a ledgered segment is checked by the ledger, not by a walk of `X`'s history; the
  terminology scans of these controls read only ledgered and corpus paths; the drift and side-change
  verdicts of op C read only `H..M`, the ledgered and corpus path sets, and the candidate's blobs on
  drifted paths, which RC8 fixes to the ledger's `expected_sha256` (R6.TREE.7, R6.RECON.13,
  R6.RECON.21). Each verdict is therefore the same at `X_rep`, at `T1'` where `T1'` conforms, and at the
  candidate the A1 retirement executes under the same ledger. The only ancestry these controls read is
  that `H` is the candidate's parent, which `X_rep` meets by construction with `H` on `main`. The marker
  blobs make every delegated path changed by the candidate, a superset of what a conforming candidate
  changes, so a path changed on both sides is never missed.
- Scope guard. A control takes `X_rep` only where the paths its verdict reads lie in the ledgered and
  corpus paths and in `H..M`. The runner records the paths its verdict read, and the invariant
  `scanned_paths_within` fails the row otherwise. A control whose verdict reads the content of a
  delegated or record path of a particular trial tree depends on that exact tree: it keeps `T1'` as
  candidate evidence for the landing decision only, and its enduring claim stays a named provenance gap
  (OBL-23: item11-T1p).
- Expected values. The expected figures of these rows are those measured with the tool commit at `T1'`.
  They are carried to `X_rep` because the paths the verdict reads are byte-identical when `T1'`
  conforms; that comparison is recorded once as candidate evidence and supports no enduring claim. A
  difference between a figure at `X_rep` and its expectation is investigated as a defect, never fitted
  (R6.EVID.1). The `T1'` measurements stay in each row's `reference` as provenance.
- Reconciliation record placement. A reconciliation record names the `M` of its run (R6.RECON.1), so it
  cannot be among the paths of that `M`. For RT-L2 and RT-O9-L2 the reviewed record is therefore not a
  landing path of the tool: for the landing decision the run names it from a commit outside the tool's
  landing paths, and it reaches `main` in a commit after the tool's landing commit.
- Evidence, per control:

| Control | Candidate evidence for the landing decision | Reproducible evidence for the enduring claim |
|---|---|---|
| RT-L2 | kind 1: on the exact candidate commit of the tool's pull request, at `X` = `C` = `X_rep`, with the predicted `M` = `M0` plus the candidate's landing paths and the reviewed record named from outside those paths | kind 2 once the landing merge and the reviewed record are on `main`; kind 3 re-run with `M` the `main` that holds the tool and a record bound to it |
| RT-O9-L2 | as RT-L2, on the predicted `M` plus the record directory of a representative stand-in `F` that holds the pinned ledger, edit list and configuration instance | as RT-L2 |
| RT-T | kind 1: on the candidate `F` before its designation, at `X_rep` built from `F`'s ledger, with `F`'s records (OBL-16 (a)); kind 4: at the executed candidate | kind 2 once the round's landing is on `main` |
| RT-T0, RT-D, RT-I7, RT-I7A, RT-DR3W, N10, N11 | kind 1: on the exact tool candidate at `X_rep`; the `T1'` measurement stays in `reference` as provenance | kind 2 once the landing merge is on `main`; kind 3 re-run on `main` |
| REP-BUILD | kind 1: on the exact tool candidate | kind 2 and kind 3 |

item11-T1p is not among them (OBL-23).
Sources: OC-3, RD-23, RE-36. Controls: REP-BUILD, RT-L2, RT-O9-L2, RT-T, RT-T0, RT-D, RT-I7, RT-I7A, RT-DR3W,
N10, N11.

***

## 32. Outstanding obligations

Each obligation below is a named blocker on the step it gates. It stays outstanding until the stated
evidence or decision discharges it; no tool requirement discharges it by implication (Q5). The gated
steps are: the tool's landing (the tool revision that implements r6), the plan freeze `F`, the A1
retirement execution, r6's adoption, and the implementation certification of the landed tool revision
(OBL-26, R6.STAT.10).

Evidence kinds (R6.EVID.7) and the trace of each gate (Q16; the gate assignments of OBL-13 and OBL-14
are confirmed, RE-37; OBL-26's gate is the implementation certification of the landed tool
revision, OC-2). A cycle is evidence that must qualify before the merge that
makes it qualify; each cycle and each evidence that cannot qualify is an open item, and none is
resolved by an exception:

| Obligation | Gates | Evidence kind that discharges it | Trace |
|---|---|---|---|
| OBL-1 | plan freeze `F`; trials claiming items 5 or 6 | 4 (the comparison recorded at `F`), by a script landed on `main` before `F` (2) | no cycle |
| OBL-2 | plan freeze `F` | 2 (a retained script on `main` before `F`), or the narrowing | no cycle |
| OBL-3 | plan freeze `F` | 4 (reviewed rule records frozen at `F`) | no cycle |
| OBL-4 | plan freeze `F` | 4 | no cycle |
| OBL-5 | plan freeze `F`; trials claiming item 7 | 4 | no cycle |
| OBL-6 | r6's adoption; plan freeze `F` | the owner's recorded decision (none of the four kinds); 4 for the rule records | no cycle; rests on V5-D1, pending owner confirmation |
| OBL-7 | plan freeze `F`; RT-T's release | 4 | no cycle; RT-T runs at `X_rep` (OBL-15, R6.EVID.8) |
| OBL-8 | plan freeze `F`; acceptance of the affected delegated classes | 4 | no cycle |
| OBL-9 | plan freeze `F` | 4 | no cycle |
| OBL-10 | plan freeze `F` | 4 | no cycle |
| OBL-11 | plan freeze `F` | 4 | no cycle |
| OBL-12 | the A1 retirement execution | 4 | no cycle |
| OBL-13 | the tool's landing | landing decision: 1 (RT-L2 on the exact candidate commit of the tool's pull request, at `X` = `C` = `X_rep`, the predicted `M` = a pinned `main` commit `M0` plus the candidate's landing paths, the reviewed record named from outside those paths); enduring claim: 2 once the landing merge and the reviewed record (in a later commit) are on `main`, and 3 re-run against `main` | no cycle; no input is `T1'`, `P` or the tool commit a3799244 (R6.EVID.8) |
| OBL-14 | the tool's landing | as OBL-13, on the predicted `M` plus the record directory of a representative stand-in `F` (R6.EVID.8) | as OBL-13 |
| OBL-15 | plan freeze `F`; the A1 retirement execution | records at `F` (4); RT-T: 1 on the candidate `F` before its designation, at `X_rep` built from `F`'s ledger, within the exact-candidate validation (OBL-16 (a)); 4 at the executed candidate; 2 once the round's landing is on `main` | no cycle |
| OBL-16 | plan freeze `F` (TR5 (a), (b)); the round's landing (TR5 (c)); the A1 retirement execution (G-A1) | TR5 (a): 1, the exact-candidate validation of the candidate `F` before its designation; (b): the recorded designation compared with the candidate's full id (governance, by the record's reviewer); (c): 2 once the round's landing is on `main`; G-A1: 4 | no cycle: no evidence needs `F` on `main` before its designation (AGENTS.md sec. A.39) |
| OBL-17 | the A1 retirement execution | 4 | no cycle |
| OBL-18 | acceptance of a chain-admitted result in the A1 retirement execution | a dispatch after the tool lands (3-type, on a branch holding `T'`) | no cycle |
| OBL-19 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-20 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-21 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-22 | the tool's landing | the owner's advance approval and an independent review (governance), with 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-23 | the use of the R6.EVID.4 figures as acceptance references for the tool's landing | N10, N11, RT-D, RT-I7, RT-I7A, RT-DR3W, RT-T0: 1 at `X_rep` on the exact tool candidate for the landing decision; 2 and 3 for the enduring claim (R6.EVID.8); item11-T1p: 1 at `T1'` on the exact tool candidate, for the landing decision only | no cycle; item11-T1p's enduring claim is a named provenance gap while `T1'` is not reachable from `main` (open); whether a kind-1-only figure suffices for the landing gate is an owner question |
| OBL-24 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm; the harness lands with the tool revision (RE-9 (a)) | no cycle |
| OBL-25 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-26 | the implementation certification of the landed tool revision | 2 and 3 (the checks recorded against the tool revision on `main`); the conformance assessment of a37992449b452021001277c06c524a30c92dfb87 is provenance for the requirements (AGENTS.md sec. A.42 item 8) | no cycle: r6's adoption does not rest on it (R6.STAT.10); the statements that describe the tool commit are in the adoption trace |
| OBL-27 | plan freeze `F` | 4 | no cycle |
| OBL-28 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |

Adoption trace (OC-2; AGENTS.md sec. A.42 item 8). Each place where r6's adoption, or an enduring claim
stated in r6, uses content that is not on `main`, with its classification. "Support off `main`" rows are
open governance conflicts (R6.STAT.10); none is resolved by an exception:

| Where | Content not on `main` | Use | Classification |
|---|---|---|---|
| R6.STAT.10 (the adoption record) | the r6 documents and their independent exact-head review | the adoption's support | support: must be on `main` no later than the adoption record lands; precondition, an ordinary merge the owner approves (AGENTS.md sec. A.50 item 1), not authorized by r6; open until then |
| OBL-26; the runner cites of Table 17.1 and the expectation file's `runner` fields | the tool commit a37992449b452021001277c06c524a30c92dfb87 and its conformance assessment | locates the implementation and motivates obligations; no requirement rests on it | provenance for the requirements (the claim does not use the content); implementation certification is OBL-26, against the landed revision |
| the expected figures of the expectation file (R6.EVID.4) | runs of the tool commit at `H`, `E` and `T1'` | preregistered expectations, not established values (R6.EVID.1, R6.EVID.7) | provenance for adoption; the enduring figures are those of R6.EVID.8 and OBL-23 |
| statements of what the tool commit does ("at the tool commit", "today"): R6.PUR.12, R6.PIPE.3, R6.ANCH.10, R6.ANCH.12, R6.HP.7, R6.OUT.18, R6.OUT.24, R6.SPLIT.3, R6.RULE.11, R6.RULE.12, R6.REC.20, R6.HIT.2, R6.CLASS.1, R6.CLASS.11, R6.GATE.7, R6.CTRL.19, R6.CTRL.25, R6.CTRL.29, R6.TREE.13, R6.RDIR.7, R6.RECON.11, OBL-21, OBL-28; R6.EVID.6 (CI run 45569710442); R6.NOTE.3 (the content of `T1'`) | the tool commit, its conformance assessment, the CI run, `T1'` | each statement asserts a fact about that content | support off `main`: open; closed by landing the content each statement uses, or by narrowing it to the requirement and control it motivates |
| semantics defined by reference to `P`'s `edits_check.py` (blob sha256 2856e58c...d98c): R6.SPLIT.3, R6.PROF.3, R6.PROF.4, R6.PROF.5, R6.PROF.7, R6.PROF.8, R6.PROF.9, R6.PROF.10, R6.PROF.12, R6.DENY.5, R6.A1CFG.2, OBL-1 | the plan commit `P` (its record directory is on no commit reachable from `main`) | the normative meaning of these requirements | support off `main`: open; closed by landing that blob on `main` no later than the adoption record, or by r6 stating the semantics itself; the copy frozen at `F` reaches `main` only with the round's landing, after adoption |
| the external oracle of R6.GATE.7 and R6.GATE.8 (`P`'s outputs as files) | outputs of `P`'s checker | evidence for implementation certification, not for adoption | provenance for adoption; for certification, support off `main` until those outputs land |
| owner decisions recorded only in paraphrase or relayed in session: the requirements of PARAPHRASED-DECISIONS.md, R6.STAT.8, and the owner corrections OC-1 to OC-5 of 2026-11-25 | GitHub comments and session instructions | the authority of the requirements that state them | support off `main` until quoted with author and time in a record on `main` (AGENTS.md sec. A.42 item 7): open |
| inventory, review and decision labels in `Sources` (E-, V1-, V2-, A-, RD-, OD-, RE-, Q-, ME- and others) and the `source` fields citing v6.0e, r4 and r5 | the review and design records of the drafting | provenance: r6 states every rule itself (R6.STAT.2) and takes its authority from its own adoption | provenance |
| item11-T1p (OBL-23) | `T1'` | an acceptance reference that needs `T1'`'s exact tree | support off `main`: named provenance gap, open |
| controls outside OC-3's list that read `T1'` or `P`: RT-C, the `T1'` case of RT-DR, RT-M, RT-D-gr58, RT-L, S11-56, RT-O9's stand-in `F` (`P`'s record directory), and every `execution` control whose ledger and edit list are read at `P` | `T1'`, `P` | inputs of acceptance references | support off `main`: open; not re-specified by OC-3 (R6.EVID.8 states the representative candidate and the pinned ledger and edit list they could use) |

**OBL-1** P-parity of `register` and `infinity`. The engine's `register` and `infinity` profiles
implement items 5 and 6 of P's plan as P's frozen checker defines them: per edit and per step of the
edit list, not per splice, with P's selection, counting and sentence splitting (P's `edits_check.py`,
blob sha256 2856e58c...d98c, functions `static_new`, `inf_key` and `sentences`). Gates: plan freeze `F`
and any trial that claims items 5 or 6. Discharged by: a comparison, recorded at `F` by a script
retained on `main`, of the engine's outputs against P's checker as frozen with the plan. Sources:
E-115, E-1371, ME-1.

**OBL-2** Parity measurements. The figures 2822 / 2822 accepted, 16905 / 16905 refused, 273 chained
refusals, 4000 regression cases, and 401 edits binding 399 splices are recomputed with a retained
script on `main`, or are stated only as "measured during design, not retained". Gates: plan freeze `F`
(as evidence for OBL-1). Discharged by: the retained recomputation, or the narrowing. Sources: E-122,
E-124, E-1357, E-1358, E-1359, ME-2.

**OBL-3** Rule records adopted at `F`. The deny rules DR-1 (alternatives a, b, c), DR-3, DR-4 and
DR-5; the review profile `resid` (resid-a, resid-b, resid-c); the W1 allow rules with W1-c's
`negative_allowance: {"finit": 1}`; the W2 allow rules replacing the first two `RESIDUAL_ALLOW`
entries, their `EXPLAINED` substring entries and the blanket `(A1)` strip; and the converted
`EXPLAINED` entries are plan records. Each is independently reviewed and adopted with the amended
plan at `F`. Until then the controls use the current rule files as pinned control inputs. Gates: plan
freeze `F`. Discharged by: the reviewed rule records frozen at `F`. Pending owner confirmation (see PARAPHRASED-DECISIONS.md). Sources: E-1001, E-1002, E-1003,
E-1004, E-1005, E-1006, E-1020, E-1021, E-1022, E-1024, E-1025, E-1026, E-1027, OD-8.

**OBL-4** Corpus terminology decision. DR-1's ordinal alternatives also match legitimate references
to A6 as "the sixth structural assumption" in active files outside the corpus. The plan amendment
states item 7's scope (`papers/*.md`, `book/*.md`), names that usage, and states the corpus
terminology decision the ordinals encode. Gates: plan freeze `F`. Discharged by: the amendment's
scope statement. Sources: E-1008, E-1287.

**OBL-5** Item 7 restatement. Any restatement of item 7 is a plan amendment with its own
preregistered text, an independent review of the deny set, the `resid` profile and the W1 rules, and
the owner's authorization; it is adopted before any trial claims item 7. The proposed check is
`terms --commit X --base H --ledger F:ledger.json --check item7 --final`, with `checks.item7` profiles
`ptr`, `count-grep`, `resid`, DR-1, DR-3, DR-4 and DR-5 and `final_profiles` `ptr` and `count-grep`:
zero deny matches; every unclassified `ptr` and `count-grep` hit FAIL `final-unclassified`; every
unclassified `resid` hit REVIEW_REQUIRED. Gates: plan freeze `F`; any trial claiming item 7.
Discharged by: the adopted amendment. Sources: E-1284, E-1285, E-1369.

**OBL-6** Accepted residuals and the V4 reversal. With DR-1d and DR-2 dropped, "the framework's sixth
structural property, finiteness of the bijection" PASSes when added (control V4, whose expectation in
v2's demonstration was FAIL); "the substratum's sixth axiom, finiteness" is REVIEW only (V15); "The
framework's sixth structural property is finiteness of the substratum" PASSes (V27). Constructed forms
outside `resid`'s classes PASS ("the six posits of the substratum", "six assumptions about the
substratum", "The posit ledger lists fourteen.", "the fourteen-item posit ledger", and "$A_1$" joined to "$A_6$" by an en dash).
Consequence of the reversal: an added sentence of V4's form reaches PASS without review. Gates: r6's
adoption (the V4 reversal, adopted or rejected at that step); plan freeze `F` (acceptance of the residual
forms or further rules, as rule records). Discharged by: the owner's recorded decision on the V4
reversal at r6's adoption, and the reviewed rule records at `F`.
The decision covers V4, V27, V27-glossary and V15 together (RE-1).
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1365, E-1366, RD-14, Q10.

**OBL-7** The fifth `ptr` hit. `papers/GR.md:58` ("For a finite total system, ...") matches `ptr` at
`T1'` and is resolved only by its reviewed hit classification record (sec. 22), which names the `ptr`
hit. Gates: plan freeze `F` (the record frozen) and RT-T's release. Discharged by: the reviewed record
at `F` verifying under the tool. Sources: E-1023.

**OBL-8** `preserve_check.py` gaps. The amended plan closes:
- gap 1: the candidate is not a resolved commit (a ref name or abbreviation in `--commit` mode; a
  directory path in `--tree` mode);
- gap 2: the checker's own blob is not recorded; its self-check compares bytes with the plan's copy
  only when `--plan` is passed;
- gap 5: no result file on an argparse error or an uncaught exception;
- gap 7: `set_fingerprints` skips silently when a coverage id is not found.

Gap 3 (PDFs verified only by `--tree` with `--pdf-compare BUILT`) is met by the tool's `pdf` class;
gap 4 (aggregate evidence with free-text discrepancies) is met by reading only the named checks'
`status` and the emptiness of their `discrepancies`; gap 6 (`--commit` mode runs `git worktree add` in
the repository it starts from) is decided in the plan amendment; gap 8 (a docstring saying "four coverage
entries" where STALE lists seven) is corrected there. Until gaps 1, 2, 5 and 7 are closed, the affected
delegation classes are REVIEW_REQUIRED (evidence missing) or FAIL (inconsistent). Gates: plan freeze
`F`; acceptance of the affected delegated classes in the retirement execution. Discharged by: the
amended plan's checker closing each gap, and the gap 6 decision recorded. Sources: RV-031, RV-032,
RV-033, RV-034, RV-035, RV-036, RV-037, RV-038, E-1047, OD-30.

**OBL-9** Plan wording corrections. Item 4's "four entries" becomes the seven STALE ids
(`MAIN:L-3`, `STRUCTURE:P-9.5`, `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer`,
`SUBSTRATUM:T-23`, `SM:L-1c-canonical-projection-resummed-kernel`,
`SM:P-4b-symmetric-point-custodial-scalarity-component`, `SM:T-19`); item 12's "execution head's
parent" becomes "the ledger base H". Gates: plan freeze `F`. Discharged by: the amended text. Sources:
E-1290, RV-038.

**OBL-10** Plan amendment content. The amendment refers to no authority record, freeze ledger, comment
form or automated authorization check. Its frozen configuration carries the `tool` pins and the
`repository_id`, and lies beside the `PREREG.md` whose last `Record pins` subsection lists it. Its
pinned workflow meets execution-identity point 5 of sec. 11, including the pre-run pin check. Gates:
plan freeze `F`. Discharged by: the frozen amendment and configuration. Sources: E-1372.

**OBL-11** Staged A1 configuration. The A1 configuration staged for `F` pins `tool.files` (including
`record_authority.py`), `tool.workflow`, the tool-landing class record, and the `records` entries
`context-adjudications.json` and `hit-classifications.json`. Gates: plan freeze `F`. Discharged by: the
reviewed configuration listed in `F`'s pin table. Sources: A-131, RE-38.

**OBL-12** A1 evidence gaps. ESC-1 to ESC-4 stay unresolved A1 evidence gaps; ESC-5 is
administrative; ESC-6 (the correction of the S1 classifications and the landing README) stays open
until its separately reviewed change. None of them blocks the tool's landing, and r6 resolves none.
Gates: the A1 retirement execution. Discharged by: the evidence or reviewed change each names. Sources:
E-017, E-1371, ME-8.

**OBL-13** RT-L2 release. At `main`, `AGENTS.md` is `base-drift` and `.claude/settings.json` is an
unclassified side change. RT-L2 is NOT RUN until a reviewed reconciliation record for `AGENTS.md`,
bound to the exact `H`, `M` and `C` blobs of the run and passing record lint, and side-change class
records for the unclassified paths exist; it is then three-valued (sec. 23). RT-L2 runs at `X` = `C` =
`X_rep` (R6.EVID.8): its verdict reads `H..M`, the ledgered and corpus path sets and the candidate's
blobs on drifted paths, none of which depends on the identity or ancestry of `T1'`. The reviewed record
names the predicted `M` and so is not among its paths: the run names it from a commit outside the
tool's landing paths, and it reaches `main` in a commit after the tool's landing commit. Gates: the
tool's landing. Discharged by: RT-L2 run and PASS (no drift, or validly reconciled).
Evidence: for the landing decision, kind 1 (RT-L2 on the exact candidate commit of the tool's pull
request); for the enduring claim, kind 2 once the landing merge and the reviewed record are on
`main`, and kind 3 re-run against `main`, every input reachable from `main` (sec. 32 trace; RE-37
confirms the gate). The RT-L2 PASS of CI run 45569710442 (tool commit
a37992449b452021001277c06c524a30c92dfb87, `X` = `T1'`, drafted record) stays provenance (R6.EVID.6).
Sources: E-1363, OD-18, Q2, MC-4, OC-3.

**OBL-14** RT-O9's dependent clause. RT-O9's own record-directory checks run and are gated. Only its
clauses that RT-L2 still holds and that no `base-drift` occurs on the predicted `M` are an outstanding
dependent assertion, RT-O9-L2, NOT RUN while RT-L2 is NOT RUN (RE-5 (a)). RT-O9-L2 runs at `X_rep`, on
the predicted `M` plus the record directory of a representative stand-in `F` that holds the pinned
ledger, edit list and configuration instance (R6.EVID.8): `base-drift` is decided by whether a side
change touches a ledgered or corpus path (R6.TREE.7), and a record directory holds none (DIR3), so the
clause does not depend on the content of `P`'s record directory.
Gates: the tool's landing. Discharged by: RT-L2's release and PASS (OBL-13).
Evidence: as OBL-13 (RE-37 confirms the gate).
Sources: RD-6, Q6, MC-4, OC-3.

**OBL-15** Reviewed records for RT-T. RT-T is NOT RUN until every reviewed record of sec. 14's review
load exists at `F` and verifies: HP adjudications for the 113 `E..H` site changes, context
adjudications for the meaning-context sites, structure reviews, and hit classification records for the
replacement-region and unheld hit lines (including `papers/GR.md:58`). RT-T runs at `X_rep` built from
`F`'s ledger (R6.EVID.8): op B reads only the corpus and the segments `E..H` and `H..X` (R6.PUR.5),
whose bytes `H` and `F`'s ledger fix for every conforming candidate. Gates: plan freeze `F`; the A1
retirement execution. Discharged by: RT-T run and PASS with every record: before the designation of
`F`, on the candidate `F` within its exact-candidate validation (kind 1, OBL-16 (a)); in the
retirement execution, at the executed candidate (kind 4); both qualify as kind 2 once the round's
landing is on `main`.
Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
Sources: E-1062, E-1063,
RD-9, OD-20, OC-3.

**OBL-16** Native runs for G-A1 and TR5. TR5 is the exact-candidate validation of the plan freeze, in three
parts, none of which places `F` on `main` before its designation:
- (a) exact-candidate validation, before the owner designates `F` (AGENTS.md sec. A.39), with the
  round's branch held at exactly the candidate commit (AGENTS.md sec. A.43 item 3): the exact-head
  check-run of sec. A.39 on the candidate (the workflow dispatched on it, the run whose `head_sha` is
  that commit, every job green); and TR5's chain-admitted run, the pinned workflow dispatched on `main`
  at the tool commit `T` (R6.REC.18 points 1 and 6, R6.REC.19) with `--freeze` the same full commit id
  and `--config` a reviewed configuration listed in the last `Record pins` subsection of the
  `PREREG.md` beside it, holding with `config.admission.mode` `"chain"` and every snapshot field
  (R6.REC.24). The two runs are distinct because chain admission requires the `head_branch` `main`
  (R6.REC.18 point 6); each records the candidate's full id, which binds them. The candidate is fetched
  by its full id (R6.REC.19, R6.REC.22) and need not be reachable from `main`; a failed fetch fails the
  run, and TR5 stays NOT RUN;
- (b) designation identity verification: the owner's recorded designation, quoted with author and time
  in the record that relies on it (AGENTS.md sec. A.42 item 7), names a full commit id equal to the
  check-run's `head_sha` and to the `F` of TR5's snapshot; the reviewer of that record compares the
  three ids and records the comparison. The tool neither reads nor checks the designation (R6.STAT.4,
  R6.REC.23): this is a comparison of identifiers, not a check of authorization;
- (c) durable evidence verification when the round lands: once the round's landing is on `main`, the
  designated `F` is an ancestor of the certified head (sec. A.39's `E`, `C` here, R6.NOTE.1) and is
  reachable from `main`; TR5's recipe (the pinned workflow at `T`, the inputs `F` and the configuration
  path) and its expected result then qualify under AGENTS.md sec. A.42 items 1 and 7, with the round's
  receipt recording the check-run attestation (sec. A.39). Run ids and host records are provenance
  (sec. A.42 item 2), and the host attestations stay residual trust (R6.REC.25).
G-A1 needs an admitted configuration and native delegated runs in clones at `X` and `C`. Gates: plan
freeze `F` (TR5 (a) and (b)); the round's landing (TR5 (c)); the A1 retirement execution (G-A1).
Discharged by: each control run and PASS under its release condition, the identity comparison
recorded, and the round landed with its receipt holding. The dispatches of (a) are launches that need
the owner's approval (AGENTS.md sec. A.40, sec. A.50 item 5); r6 authorizes none.
Sources: RD-25, OD-1, OC-1.

**OBL-17** TR45's op-C half. The offline replay of an op-C result whose delegated classes come from the
snapshot's delegated evidence is a NOT RUN row, TR45-opC, with the release condition "delegated evidence
recorded by native runs at `X` and `C`". Gates: the A1 retirement execution. Discharged by: TR45-opC
run and PASS. Sources: RD-26.

**OBL-18** EI14's branch-dispatch half. EI14 is split; its branch-dispatch half, EI14-dispatch, is NOT
RUN until a dispatch of the pinned workflow on a branch holding `T'` is made after the tool lands,
under a launch the owner approves (sec. A.50, sec. A.51 item 4), and recorded under sec. A.44 (RE-21). Gates: acceptance of a chain-admitted result in the A1 retirement
execution. Discharged by: EI14-dispatch run and PASS.
Its composite EI14 is NOT RUN by inheritance until then (R6.GATE.9).
Sources: RD-26.

**OBL-19** Consumer halves. EI7-consumer and the consumer non-acceptance halves of TR15, TR50, TR51 and
TR52 are rows of the expectation file, implemented in the tool revision. Gates: the tool's landing.
Discharged by: each row recorded and holding under the gate. Sources: RD-26, RD-4.

**OBL-20** Missing second directions (VD-RESTORE). Every control in the both-directions scope of
R6.CTRL.3 runs in both directions. Each such control whose second direction is not recorded, or
whose stated restored case or paired row is not executed, is a verification defect until its second
direction is recorded and holds. At the final expectation file 217 rows are flagged VD-RESTORE, derived
mechanically from the per-row decisions of R6.CTRL.3 (42 of them record no second direction and are
reported as `direction-missing`). Gates: the tool's landing. Discharged by: a recorded and executed
second direction on every such row, holding under the gate.
Sources: Q7, RD-8, RE-2, RE-3, Q11.
**OBL-21** Implementation corrections. The tool revision makes these corrections, each with a
distinguishing control that holds under the gate:
- VD-1: the gate and the correspondence check (sec. 16); a planted wrong expectation fails the gate;
- VD-2: adjudicated HP sites in a non-conforming file, or a file with an unledgered change, in a
  ledgered segment are searched and yield their site-level item;
- VD-3: a pin-duplicated line is translated under the duplicate rule (count, context, ordinal);
- VD-4: TT7's landing run is asserted;
- VD-5: TT2's old-style comparison of `X` against `M` is implemented;
- VD-6: S11-7 is implemented (a literal and a DR-5 match FAIL both);
- VD-7: the unreachable checks of A9r's negative example and A11r's clean-lint baseline are made
  reachable and asserted;
- VD-8: SW1 asserts exactly one new FAIL against the unmutated tree;
- VD-9: Z9f's adapter half lints the real adapter sources;
- VD-10: O1-O3, O5, O7, O6, RT-I7, S11-14, item11-T1p, TT8, TT12, U2 and U10 emit and the gate checks
  the asserted quantities;
- VD-11: RT-T0's runner `expected` string agrees with its expectation;
- VD-12: `read_entries` are removed from the sitemap adapter and loader;
- the symlink or submodule side change outside the record directory: the entry type is checked before
  any byte read, for every side change (RD-12);
- RD-35: A2r runs on W2-a with the literal shortened to `(A1)` and asserts a widening by shortening
  (RE-20 (b)); A5r's expected deny FAIL names its rule
  alternative; K4 checks both halves; EI7's consumer half is implemented; RT-D's 45 count is asserted;
  the expectation sources' Z1-Z8 line cites are corrected; E-060's op B carries no `(and L)`, since op B
  on `L` is retired (B-9).

Gates: the tool's landing. Discharged by: each correction with its control holding. Sources: VD-1 to
VD-12, RD-12, RD-35, E-1380, E-1429.

**OBL-22** Identifier migration. The migration of sec. 34 is applied in the same tool revision as the
gate: recorded control ids, runner record ids, expectation-file ids and reason strings take their new
identifiers. It needs the owner's approval in advance and an independent non-author review (sec. A.48
item 3). Gates: the tool's landing. Discharged by: the approved and reviewed migration, verified by the
build, the gate and the correspondence check. Sources: OD-31, RD-5, RD-4, E-015.

**OBL-23** `T1'`-input evidence. The figures of R6.EVID.4 whose controls ran on `T1'` (N10, N11, RT-D,
RT-I7 at `T1'`, RT-I7A at `T1'`, RT-DR3W at `T1'`, RT-T0, item11-T1p) were measured with the tool commit
at `T1'`; those measurements are historical and are kept in the rows' `reference`.
- N10, N11, RT-D, RT-I7, RT-I7A, RT-DR3W and RT-T0 read only paths that `H` and the ledger determine,
  and run at `X_rep` (R6.EVID.8); their figures are acceptance references through those runs once
  every input is reachable from `main` (kinds 2 and 3).
- item11-T1p's `repo` scan reads the content of `T1'`'s delegated and record paths (two of its 176
  lines lie in generated artifacts, R6.EVID.5), which neither `H` nor the ledger determines: the figure
  depends on the exact trial tree. Its run on the exact tool candidate with `X` = `T1'` is candidate
  evidence for the landing decision only; its enduring claim is a named provenance gap (AGENTS.md
  sec. A.42 item 8, support off `main`) while the objects of `T1'` it needs are not reachable from
  `main`. Whether a kind-1-only figure suffices for the landing gate is an owner question.
Gates: their use as acceptance references for the tool's landing. Discharged by: the `X_rep` runs of
R6.EVID.8 recorded; for item11-T1p, the objects of `T1'` it needs reachable from `main`, or the owner's
decision on a kind-1-only figure; otherwise the figure stays a historical measurement.
The list is confirmed with RT-D and the `T1'` cases of RT-I7A and RT-DR3W (RE-36 (a)); no figure is an
acceptance reference reproduced on `main` until the tool revision lands and the run is repeated
there (R6.EVID.7).
OPEN: T1'-bound evidence cannot qualify.
Sources: RD-23, ME-3, Q10, OC-3.

**OBL-24** Mutation evidence. Mutation evidence is re-established for the changed code. Each mutant has
a row in its own namespace of the expectation file, with its killing controls as evidence, and the gate
distinguishes killed, survived, not applied and missing. The seven known survivors and the one
unapplied mutant are explicit limitations tied to their named mutants; any other survivor fails. Gates:
the tool's landing. Discharged by: the gate holding on every mutant row.
The harness and the mutant names land, pinned, with the tool revision (RE-9 (a)). The survivors
`MUT:cache:K08`, `MUT:v60e:C08`, `MUT:v60e:I06` and `MUT:v60e:P01` are also verification defects,
each discharged by its distinguishing control (RE-10 (b)).
Sources: RD-1, Q8, OD-1.

**OBL-25** Runner-only predicates. Each of the 32 runner-only predicates that RD-24 enumerates is checked against
the requirement it claims to test before it becomes an expectation; a weak or mismatched predicate is a
verification defect. The null-expectation rows are reconciled mechanically with the enumerated lists.
Gates: the tool's landing. Discharged by: every row with a settled, verified expectation. Sources:
RD-24, RD-25, Q9.

**OBL-26** Conformance certification of the tool revision. The read-only conformance checks of OD-4, OD-9,
OD-23, OD-25, OD-27, RD-10, RD-18, RD-20, RD-27 and RD-33 are completed against the tool revision that
implements r6, once it is on `main`; each difference becomes a verification defect or a residual owner
decision. This is the implementation certification of the landed tool revision, separate from r6's
adoption (R6.STAT.10). The conformance assessment recorded against the tool commit
a37992449b452021001277c06c524a30c92dfb87 motivates obligations of sec. 32; for the requirements and
obligations of r6 it is provenance (AGENTS.md sec. A.42 item 8). The statements of r6 that describe the
tool commit use it, and are listed in the adoption trace below as off-`main` support. Gates: the
implementation certification of the landed tool revision (OC-2 replaces the adoption gate that RE-37
confirmed). Discharged by: the recorded checks and their dispositions against the tool revision on
`main` (evidence kinds 2 and 3). Evidence: see the sec. 32 trace.
Sources: OD-4, OD-27, RD-18, RD-20, OC-2.

**OBL-27** Plan-side countercontrols. The plan's own check fails on each countercontrol mutant where
R6.PLAN.1 says so, and the plan-side behaviours cited in items 1, 2, 3, 4, 8, 12 and 14 of sec. 18
hold, verified at `F` against the plan's checker as frozen with the plan. Gates: plan freeze `F`.
Discharged by: the plan checker's results on each countercontrol mutant and plan-side case,
recorded at `F`. Sources: E-1268, E-1269, E-1271, E-1272, E-1273, E-1274, E-1276, E-1280, E-1282,
B-19.

**OBL-28** Implementation obligations of the tool revision. Each row is an obligation of the tool
revision that implements r6, made under its own authorization; it is a verification defect or a code
change until its distinguishing control holds under the gate, or the check it names is recorded.

| Label | Requirement | Obligation | Distinguishing control |
|---|---|---|---|
| C-1 | R6.CTRL.3, OBL-20 | a recorded and executed second direction for each VD-RESTORE row; the rows the conformance check lists with a restored case (A5r, GV7-tool, H4, H7, S11-56, S11-58a-f, TR46, X9) and G2, X6 and S11-58i settled by reading each predicate | the restored case or paired row |
| C-2 | R6.CTRL.29, OBL-21 | VD-1 to VD-12 as OBL-21 states | as OBL-21 |
| C-3 | R6.CTRL.28, OBL-25 | the weak runner predicates of E-A1r, E-A2r, E-A3r, E-A6r, E-A8r, E-S1r, E-S2r, rule-negative, A5r-generic, R4-B3-DUP, S7-schema-and-checker and V3-countercontrol | each runner emits the asserted quantity; the gate re-evaluates `expect` |
| C-4 | R6.CTRL.17, OBL-19 | rows without a runner: EI14-dispatch, EI7-consumer, RECLINT-ORPHAN, REPRO-DOUBLE, RT-O9-L2, TR15-consumer, TR50-consumer, TR51-consumer, TR52-consumer, TR45-opC and S11-7 | each implemented; `missing-id` until then |
| C-5 | R6.EVID.4 | figures not asserted today: RT-T0's 383, 18 and the D029 overlap; RT-I7's split at `H`; RT-C's 399/23/21; item11-T1p's 176; RT-D's 45 | promoted `expect.counts` |
| C-6 | R6.CTRL.4, R6.CTRL.18 | K4 asserts its K2 half; A5r names DR-3 and its alternative; V6 asserts DR-1b | the assertions named |
| C-7 | R6.GATE.5 | group-error ids and diagnostic keys recorded as records; U13, U15 and `outcome` still recorded | one failed record per member; diagnostics dropped; `outcome` recorded as Z9-STAGED |
| C-8 | R6.RULE.11, R6.RULE.12 | rule lint without the 8-character minimum and the zero-fingerprint check | RULE-MINLIT, RULE-ZEROFP |
| C-9 | R6.OUT.7 | the `--out` guard has no rev-parse check, fails open when the worktree listing fails or names another repository, and the INTERNAL handler writes without it | a planted worktree directory; a failing worktree listing |
| C-10 | R6.REPRO.4 | no control for writes outside `--out`; X7 writes to the system temporary directory | OUT-CONFINED |
| C-11 | R6.OUT.5 | `PIN_MISMATCH` without `record_digest` and `computed_digest` | the four fields asserted |
| C-12 | R6.PIPE.6 | a broken segment chain gives USAGE 64 with no result | an ERROR class with `result.json` |
| C-13 | R6.ANCH.19 | the pin check exempts removed checker literals for any splice, leaves literals new at `C` and literals away from a splice unchecked, and never feeds its freeze path | a non-guard splice removing a pinned literal FAILs |
| C-14 | R6.OUT.5, R6.SPLIT.3 | nested configuration malformation and a `splitter_version` other than 2 give INTERNAL; pin-matching content failures give `SOURCE_CHANGED` (RE-16) | a malformed nested field gives `CONFIG_INVALID`; S11-57c, S11-58a-f and S11-58g to S11-58k give `LEDGER_INTEGRITY` |
| C-15 | R6.REC.9 | a missing command-line record gives `SOURCE_CHANGED` before the admission check; a non-JSON record gives INTERNAL | both give `record-invalid` |
| C-16 | R6.VALID.3 | a configuration-referenced class or reconciliation record that is absent, non-regular or of another schema is skipped in op C | each case gives `record-invalid` |
| C-17 | R6.REC.10 | orphan HP and context records are not reported; duplicate HP entries are overwritten | RECLINT-ORPHAN |
| C-18 | R6.TREE.13 | the landing builder maps lines by similarity and falls back to `C`'s bytes | LC-1 to LC-6 |
| C-19 | R6.RECON.11 | RC6 reads the candidate at the `H` offset | two splices in one file, the first changing length |
| C-20 | R6.TREE.12 | the derived-artifact set is an engine pattern | the derived set read from the configuration |
| C-21 | R6.PUR.12, R6.RDIR.7 | the entry type is not checked before the read outside `D_rec` | SIDE-NONREG |
| C-22 | R6.OUT.4, R6.REC.20 | the isolation refusal has no class | EI6 asserts `NOT_ISOLATED` in the stderr JSON |
| C-23 | R6.CLASS.1, R6.CLASS.11 | FAILs without an item | CLASS-RECORD-CHECKS; an item per finding |
| C-24 | R6.OUT.18 | not emitted: `inputs.pin`, `inputs.record` commit and tree, prior, repository head, ledger sha256, `pins`, per-splice old and new sha256; `anchors_sha256` for op B | U2 and U10 assert the per-splice hashes |
| C-25 | R6.CLASS.2 to R6.CLASS.12, R6.PROF.2, R6.HIT.1 | no direct control for `retained-changed`, `unledgered-file-change`, `provenance-ambiguous`, `new-pattern-in-replacement`, `unclassified-in-replacement`; indirect coverage only of PROF.2, HIT.1, the delegation-hash refusal and the coverage job | the CLASS-, HIT-, PROF- and DELEG- rows |
| C-26 | R6.GATE.12 | testable requirements with no control | one control each |
| C-27 | R6.TREE.12, R6.CTRL.29 | TT7's landing not asserted; TT8's PASS not asserted; TT2 not implemented | as R6.CTRL.29 |
| C-28 | R6.GATE.10, OBL-24 | mutation evidence re-established for the changed code, changes of the killed set included | the MUT rows |
| Q12 | R6.HP.7, R6.REC.10 | adjudicated sites counted as `provenance-adjudicated`, distinct from `moved` and `authorized-replacement` and separately under `HP` and `RET`; `stale-adjudication` emitted | U14, RECLINT-ORPHAN |
| RE-13 | R6.OUT.18 | the schema file lists the adopted named fields and the declared diagnostics | ACCEPT-SCHEMA |
| RE-18 | R6.TREE.12 | a regeneration verification procedure for derived artifacts at `L` (a delegation class), specified explicitly and reviewed independently, in which the trusted checker establishes the expected output itself and compares bytes; the evaluated tree's claim of regeneration is never sufficient; REVIEW_REQUIRED until the procedure is specified, reviewed and passes (OC-4, open) | LC-7 (REVIEW_REQUIRED for every candidate `L`; its expected landing blob is open) |
| RE-19 | R6.RDIR.13 | `.github/` moved to `record_authority.py`; `record-directory` enumerated | Z9g, Z9-STAGED |
| Q13 | R6.DELEG.3, R6.CLASS.9 | execution isolation of re-executed generators | DELEG-REGEN |
| RE-27 | R6.OUT.24, R6.CLASS.7 | a purpose trace of the six obligation definitions; the pin classes defined independently | review |
| RE-29 | R6.RECON.14 | a purpose check that the stricter RC9 rejects no valid record | review; N6 |
| OC-3 | R6.EVID.8 | the representative candidate builder, the pinned ledger and edit list and the configuration's control instance land with the tool revision; the rows of R6.EVID.8 run on `X_rep` and record the paths their verdict read | REP-BUILD; `scanned_paths_within` on each row |

Gates: the tool's landing. Discharged by: each row's control holding under the gate, or its check
recorded. Sources: C-1 to C-28, Q12, RE-6, RE-13, RE-16, RE-18, RE-19, RE-23, RE-24, RE-27, RE-29,
RE-32, RE-33, OC-3, OC-4.

***

## 33. Retired identifiers and mechanisms

Each retired identifier is never reused. Each row states the disposition of the underlying
requirement: `preserved-at <ids>` (still verified there) or `obsolete: <reason>` (the property no
longer exists as a requirement).

| Identifier or mechanism | Disposition of the underlying requirement | Sources |
|---|---|---|
| U13 (hit on a line in a converted `read` entry, held by read) | obsolete: the `read` route is withdrawn; a hit is held only by a tracked site (preserved-at U1-U11), and an unheld hit is REVIEW_REQUIRED `unclassified` (preserved-at U12) | V1-098, OD-19, OD-16 |
| U15 (adjudication with a wrong `to_region_sha256`) | preserved-at U14's wrong-region-hash case (FAIL `provenance-mismatch` and `stale-adjudication`), H1, H2, H6 (an adjudication that disagrees with the walk or changes a row FAILs) and RECLINT-ORPHAN (an HP adjudication entry that matches no subject is FAIL `stale-adjudication`) | V1-100, V2-072, RD-9, Q12 |
| C1 (op C on the executed synthetic tree, PASS) | preserved-at TT1 and TT13 (op C on a correctly executed candidate gives no RET item; uniqueness tested at the base), Y6 and RL, and S11-56, S11-57a-d, S11-58a-k (application parity at the base, with OBL-1) | V2-093, OD-20, RD-17 |
| C2 (op C with C's parent differing from the base in a ledgered file, ERROR `BASE_DRIFT`) | preserved-at TT3, TT4 (FAIL `candidate-parent`), TT5 (ERROR `SCIENTIFIC_BASE_MISMATCH`), TT7 and N16-file (FAIL `base-drift`); the class name `BASE_DRIFT` is obsolete | V2-094, OD-20 |
| C3 (a pin literal removed without a guard-pin splice) | preserved-at S11-12 and N1 (FAIL `pin-broken`) | V2-095, OD-20 |
| RT-H (v1: `check-coverage --commit H`, one unledgered segment) | preserved-at RT-H0 (113 `hp-unadjudicated`, HP context items) | V1-118, OD-20, MC-1 |
| RT-H (v2: with the reviewed provenance file) | preserved-at H1-H3 (walk mismatch FAILs), RT-T0 (hits REVIEW) and RT-T (PASS with every reviewed record; NOT RUN, OBL-15) | V2-102, OD-20 |
| the `read` route (`new_site_rules[*].read` entries converted to `(file, line_sha256)`) | obsolete: holding is by tracked sites and reviewed records; hits on such lines are REVIEW_REQUIRED `unclassified` or classified by a hit classification record (sec. 14) | V1-047, E-1429, OD-16, VD-12 |
| op B on `L` (chain `E..H`, `H..X`, `X..L`) | preserved-at sec. 20 (`base-drift`, landing composition, own-diff rule; TT7, N16-file, RL, RT-L) and the MAIN obligation; op B on `L` was never implemented | V2-145, OD-13, OD-14 |
| v2 step S4b (op C and its acceptance) | preserved-at S11-56 to S11-58k (parity with P at the base) and OBL-1 | V2-108, OD-20, ME-1 |
| v2 step S5b (provenance walk) | preserved-at H1-H3 and sec. 5 | V2-109, OD-20 |
| v2 step S6b (profiles by extraction, rule engine and lint) | preserved-at sec. 9-10 (extraction, stable hash) and the L, V, A, S controls; the residual-test mutation is obsolete (MC-19); mutation evidence preserved-at OBL-24 | V2-110, OD-20, MC-19 |
| v2 step S7 (revised: schema `/2`, explanations, outcome checker) | preserved-at sec. 7 (S7, the independent outcome checker) and sec. 16 (the gate) | V2-111, OD-20, OD-1 |
| v2 step S11 (reviewed seed rule file and provenance file) | preserved-at sec. 11 (reviewed records, non-author review); the owner record is procedural | V2-112, OD-20 |
| v2 step S12 (tree roles and landing composition) | preserved-at sec. 19 (the landing check of the tool's own pull request against `H`) and TT14 | V2-113, OD-20, OD-26, OD-17 |
| v1 sec. 11 rollback (new files only, no workflow trigger, revert) | preserved-at sec. 19 (landing paths, including the pinned workflow; release gate not wired without its own review) and sec. 20 (`R` unchanged); "no workflow trigger" obsolete: the pinned workflow is required | V1-141, V2-010, OD-25, OD-7 |
| v1 sec. 11 "outputs only outside the repository, no tracked state" | obsolete: accepted results are tracked in the landing record as durable evidence (sec. 31); run outputs stay under `--out` (R6.CORE.8) | V1-142, OD-25 |
| v1 sec. 12 "not an A1-retirement gate; no substitute for the item 2 exception" | preserved-at sec. 2 (the tool decides no claim or row); the exception route is obsolete | V1-145, V2-010, OD-25 |
| v1 sec. 12 "lands only after the A1 retirement" | preserved-at sec. 19 (separate pull request, independent review, separate owner merge decision); the landing order is obsolete | V1-146, V2-010, OD-25 |
| `anchors.json` (anchor map written to `--out`) | preserved-at sec. 7 (`record_checks.anchors_sha256`, per-site anchor fields) and R6.REPRO.2, R6.REPRO.3 (deterministic rebuild) | V1-032, OD-25, OD-24 |
| `relocation` (carried sitemap member) | obsolete: the replay's `build` equality verifies the whole site map (R6.ADAPT.3, R6.ADAPT.4; M7, RT-A) | V1-045, RD-11 |
| `anchor_survives` (result field) | obsolete: a review aid, not a verdict input, never implemented; the overlap and image rules are preserved-at sec. 4 | V1-051, RD-11 |
| `self-test --real-trees` (local smoke versus CI real-tree controls; v2 demonstration command) | preserved-at sec. 16 (every control id recorded in CI with an allowed status; NOT RUN only with a reason and a release condition) and the demonstration's controls in CI (W1/W2 lines PASS in RT-D; V1-V4 and A1r-A7r; S1r), V4 subject to OBL-6 | V1-070, V2-107, V1-127, OD-25, RD-7, RD-11 |
| the status SKIP | preserved-at sec. 16's NOT RUN rule (one non-run status, always with a release condition) | V1-070, RD-7 |
| v2 "where HP is tracked" (its own Issue or row on #1169) | obsolete as tool text: sec. A.45 rule 6 governs accountable Issues | V2-119, RD-11 |
| the inspection criterion "no code path uses line proximity or similarity to resolve" | obsolete as an inspection criterion only; the prohibition on resolving anchors by proximity or similarity is preserved-at sec. 4, tested by U5-U7 and VD-3's controls | V1-135, RD-11, Q10 |
| r1's mutants "accept a path absent at F and M" and "rule evaluated before the `base-drift` test" | preserved-at RDIR-m1 and RDIR-m7, and conditions DIR2 and DIR3 (both mutants are equivalent) | A-107, Q3, Q4 |
| automated authorization machinery: the tool authority record `A` (`oi-tool-authority/2`), the comment forms `oi-freeze/1`, `oi-authority/1`, `oi-freeze-ledger/1`, "Owner at creation", the freeze ledger, the owner-authorization record `oi-owner-authorization/1` and its lint, and every read of comment threads, edit history, the GraphQL API and the comment, Issue, pull-request, branch, repository-history and file-content APIs | obsolete: authorization is not a tool property; owner approval is procedural and quoted in the relying record (sec. A.42 item 7, sec. A.50); the record kind `oi-owner-authorization/1` is ERROR `CONFIG_INVALID` (R6.CFG.4) | E-010, E-1081, ME-5 |
| DR-1d, DR-2 | obsolete: dropped deny candidates (rationale in the appendix); never reused | E-1001, E-1016 |
| v6.0e sec. 15 item 10 (focused delta review of v6.0d against v6.0c) | obsolete: r6 supersedes v6.0c and v6.0d; the claim "every guarantee of v5.5.9 is kept" is withdrawn; r6 states its own requirements and has its own review | E-1370, OD-3, ME-4, MC-11 |
| v6.0e sec. 15 item 0a; the identifiers of the unadopted drafts v5.5.10 and v5.5.10a (TR71-TR87, HV1-HV12, HS-1 to HS-7, sec. 10.5, sec. 15 items 7-9) | obsolete: never adopted; never used or reused | E-015 |

The controls O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44, TR47, TR49, TR53-TR70, LN9, LN11 and LN12 tested
the automated authorization machinery. Each id is retired and never reused, with this disposition:

| Identifier | Disposition of the underlying requirement | Sources |
|---|---|---|
| O4 | obsolete: authorization only (hash binding of an owner-authorization record); the hash binding of records and reviews preserved-at O2, O6, S4a | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2198 |
| TR4 | obsolete: authorization only (retirement.owner against A.owner.id) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2287 |
| TR6 | obsolete: authorization only (designation from the host, not from F) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2289 |
| TR7 | obsolete: authorization only (designation author id) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2290 |
| TR8 | obsolete: authorization only (designation names F); technical part (F mismatch) preserved-at EI3 | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2291 |
| TR9 | authorization part obsolete (authorization values not overridable); technical parts preserved-at Z1-Z8 (unknown configuration field) and EI4 (pin table derived, not caller-chosen) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2292 |
| TR10 | obsolete: authorization only (a caller-built F without designation); technical part (F mismatch with the landing record) preserved-at EI3; approval is procedural | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2293 |
| TR11 | obsolete: authorization only (edited designation comment) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2294 |
| TR12 | obsolete: authorization only (supersession in the thread, pagination) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2295 |
| TR16 | obsolete: authorization only (authorized thread) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2299 |
| TR17 | obsolete: authorization only (comment forms) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2300 |
| TR18 | obsolete: authorization only (withdrawal) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2301 |
| TR19 | obsolete: authorization only (deleted or hidden designation) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2302 |
| TR20 | obsolete: authorization only (numeric author id) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2303 |
| TR21 | authorization part obsolete (comment-listing failure); technical part (fail-closed handling of every host read) preserved-at GV7 (GV7-tool, GV7-consumer) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2304 |
| TR22 | obsolete: authorization only (two live designations) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2305 |
| TR23 | obsolete: authorization only (copy of A in F; merge of A by another account) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2306 |
| TR24 | obsolete: authorization only (caller-supplied A) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2307 |
| TR25 | obsolete: authorization only (A from another ref); technical part (refs never consulted for role commits) preserved-at GV1 | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2308 |
| TR26 | obsolete: authorization only (change of A after F) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2309 |
| TR27 | obsolete: authorization only (bootstrap order of A) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2310 |
| TR31 | obsolete: authorization only (freeze ledger binds a withdrawal) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2314 |
| TR32 | obsolete: authorization only (snapshot binds a supersession) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2315 |
| TR33 | obsolete: authorization only (edit history of owner comments) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2316 |
| TR34 | obsolete: authorization only (edit history of owner comments) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2317 |
| TR35 | obsolete: authorization only (deletion residual) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2318 |
| TR36 | obsolete: authorization only (freeze ledger missing or conflicting) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2319 |
| TR37 | obsolete: authorization only (form first line (CRLF)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2320 |
| TR38 | obsolete: authorization only (malformed form) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2321 |
| TR39 | obsolete: authorization only (form version and key order) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2322 |
| TR40 | obsolete: authorization only (authority change without approval) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2323 |
| TR41 | obsolete: authorization only (approval hash or time) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2324 |
| TR42 | obsolete: authorization only (edited approval) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2325 |
| TR43 | obsolete: authorization only (approval by another id) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2326 |
| TR44 | obsolete: authorization only (owner-id change) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2327 |
| TR47 | obsolete: authorization only (freeze-ledger append approval (N3)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2330 |
| TR49 | obsolete: the K7 allowance for a modified authority record at head_sha does not exist; technical part (any tool file off the pins) preserved-at TR28-tool, TR28-consumer, TR52 | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2332 |
| TR53 | authorization part obsolete (second copy of the authority record, K7); technical part (extra tool file off the pins) preserved-at TR52 | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2336 |
| TR54 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2337 |
| TR55 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2338 |
| TR56 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2339 |
| TR57 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2340 |
| TR58 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2341 |
| TR59 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2342 |
| TR60 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2343 |
| TR61 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2344 |
| TR62 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2345 |
| TR63 | obsolete: authorization only ("Owner at creation" (DI-1); A lineage (DI-2 for A)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2346 |
| TR64 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2347 |
| TR65 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2348 |
| TR66 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2349 |
| TR67 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2350 |
| TR68 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2351 |
| TR69 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2352 |
| TR70 | obsolete: authorization only ("Owner at creation" (DI-1)) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2353 |
| LN9 | obsolete: authorization only (lineage across an owner change, DI-1); lineage preserved-at LN1-LN8, LN10 | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2585 |
| LN11 | authorization part obsolete (authorization across an owner change); technical part preserved-at LN2 (positive lineage) and LN4 (widened predecessor) | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2587 |
| LN12 | obsolete: authorization only (authorization of a predecessor's widening review); widening review of a predecessor preserved-at LN4 | E-1081; INVENTORY-v6.0e table 2, v5.5.9 line 2588 |

U14 is not retired: it is restated as a positive HP adjudication case (a matching provenance
adjudication holds, and the site is counted as `provenance-adjudicated`, R6.HP.7) in sec. 5 (RD-9;
B-5). Sources: V1-099, V2-072.

***

## 34. Identifier migration index

No identifier is reused: no identifier takes a meaning different from one any record has given it.
Historical records (v1, v2, the v2 review, v6.0e, r4, r5, their reviews and inventories, the CI records)
are unchanged; this index records the successor of every identifier they use that r6 renames. The
migration is applied with the tool revision (OBL-22).

| Old identifier | New identifier | Source |
|---|---|---|
| R1-R14 (v2 four-tree controls) | TT1-TT14 (TT1 for R1, and so on) | OD-31, E-015 |
| R1-R13 (record conditions of reconciliation records) | RC1-RC13 (RC1 for R1, and so on) | OD-31, RD-5 |
| R15-R19 (four-tree controls) | R15-R19, unchanged (no collision once the record conditions are RC1-RC13) | RD-5 |
| O9-1 to O9-25 (r5 record-directory controls) | RDIR-1 to RDIR-25 | OD-31, MC-13 |
| O9-12b | RDIR-12b | OD-31 |
| O9-m1 to O9-m17 (r5 mutants) | RDIR-m1 to RDIR-m17 | RD-5 |
| RT-O9 | RT-O9, unchanged | RD-5 |
| D2-D5 (r5 directory conditions) | DIR2-DIR5 | OD-31, RE-28 |
| RT-T (v1 meaning: no records, FAIL) | RT-T0 | RD-5 |
| RT-T (v6.0e meaning: all records, NOT RUN until released) | RT-T, unchanged | RD-5 |
| runner sub-records GV7-tool, GV7-consumer, TR28-tool, TR28-consumer, TR29-tool, EI2-consumer, EI7-tool, GV6-disk, RT-D-gr58, V27-glossary, TR45-opB | the same names as control ids in their own right; GV7 and EI7 kept as composed rows | RD-4 |
| TR28 (one row) | TR28-tool and TR28-consumer | RD-4 |
| TR45 (one row) | TR45-opB and TR45-opC | RD-4, RD-26 |
| EI14 (one row) | EI14 and EI14-dispatch | RD-26 |
| EI7 consumer half | EI7-consumer (component of EI7) | RD-26 |
| S11-2 | S11-2 composed of S11-2a, S11-2b, S11-2c | RD-4 |
| Z9h (D:2291 statement) and Z9h (D:2886 statement) | one Z9h: the D:2886 statement with "with the adapter companions in the value set" | MC-9, RD-31 |
| purity job record id `outcome` | Z9-STAGED | RD-25 |
| runner-only ids R3-F2, R4-B3, R4-B3-DUP, R5-N6, R6-G6 | unchanged, as control ids with adopted expectations | RD-5, RD-24 |
| result field "authority match" | "admission match" | OD-6 |
| ERROR reason "(authority)" | "(directory not admitted)" | OD-6 |
| "authorized record directories" | "admitted record directories" | OD-6 |
| module `record_authority.py` | unchanged (historical name kept) | RD-29 |
| r5 notation `P` (configuration path) | `P_cfg` | RD-28 |
| r5 notation `D` (directory part of `P_cfg`) | `D_rec` | RD-28 |
| r5 notation `E_F`, `E_M` | F-entries, M-entries | RD-28 |
| v2 ERROR `BASE_DRIFT` | retired (sec. 33, C2); FAIL `base-drift` keeps its meaning | OD-20 |
| finding labels R5, R8, R9 and "v3 R11"; B1-B6, V5 and O9 as finding labels; N4 as the finding at D:2585 | not identifiers in r6; cited in prose (for example "v3 review finding R11"); the control ids B1-B6, V5, O9 and N4 keep their meaning | OD-31 |
| decision labels D1-D8, V5-D1, V5-D2, S1-D1 to S1-D3, R-D1, R-D3, R-D5, A-D5, DI-2, C3, C4 | quoted, not identifiers; a rule citing one restates its content | OD-31, E-014 |
| isolation refusal (no class at the tool commit) | ERROR class `NOT_ISOLATED` (new identifier) | RD-19, RE-14 |
| class name `stale-adjudication` | live with v1 4.6's meaning (an HP adjudication entry that resolves no subject); not retired | Q12, RE-8 |
| (new expectation-file fields and values) | `paired_with`, `candidate_expectations`, `direction` objects, outcome DEFERRED; gate findings `direction-missing` and `deferred-expectation` | RE-1, RE-4, Q11 |
| (new control ids) | GATE-27 to GATE-30, LC-1 to LC-7, DELEG-REGEN | RE-4, Q14, RE-1, RE-11, Q15, Q13 |
| (new item classes) | `regeneration-mismatch`, `regeneration-output-missing`, `regeneration-timeout`, `regeneration-extra-write` | Q13 |
| (new obligations and requirement) | OBL-27, OBL-28, R6.EVID.7 | B-19, C-1 to C-28, Q16 |
| mutants | each mutant id is unique in its own namespace of the expectation file and equals no control id | RD-1, RD-5 |

Retained controls, sections and items keep their ids and meaning. Removed control ids, the removed
item 0a and retired schema ids are never reused (sec. 33). Sources: E-014, E-015, OD-31, RD-5, RD-28.

***

## Appendix H. History (not normative)

This appendix records history. Nothing in it is a requirement, an expectation or an acceptance
reference.

**H.1 Status and authority history.**
- HIST-1. v1's title and v2's status: paper-only designs; v2 superseded v1 where it differed. Sources:
  V1-001, V2-001.
- HIST-2. The v1-to-v2 change table (three-state outcome, HP, four operations, explanations); the name
  clash of v2's ERROR `BASE_DRIFT` with FAIL `base-drift` is resolved in sec. 33 and sec. 34. Sources:
  V2-004.
- HIST-3. The v6.0 to v6.0e revision history: v6.0a (review items B-1 to B-4, fixed meaning table,
  ls-remote failure handling), v6.0b (tool commit on `main`'s first-parent chain, executable
  dependencies, hashlib negative control), v6.0c (the restored pre-run pin check), v6.0d (correction
  under a quoted owner decision; "v5.5.9 authoritative until adoption", a status r6 does not carry) and
  v6.0e (review-v6.0d B-1, S-1 to S-3). The stated review-v6.0d hash differs from the records-branch
  copy; the mapping is recorded in r6's provenance file. Sources: E-002, E-003, E-004, E-005, E-006.
- HIST-4. Quotes of owner decisions without a GitHub record (removal of automated authorization
  verification; preservation of technical guarantees; the route authority of #1169 comment 7093128173,
  paraphrased; D1-D4, V5-D1, V5-D2, S1-D1 to S1-D3 and the decisions of 2026-11-24). r6 relies on no
  unrecorded decision; its authority is its own adoption. Sources: E-008, E-016, E-1364, ME-5, ME-6.
- HIST-5. v6.0e's statement that it kept every guarantee of v5.5.9, with section pointers; withdrawn
  as a claim, each guarantee restated as its own r6 requirement. Sources: E-011, ME-4.
- HIST-6. r5's authorizations, basis and revision history: the authorization limited to O-9 and the
  item-2 interfaces; the Stage A V2 basis at 68bab90e; r2 (answers to r1's B1-B6), r3 (constant in
  pinned code; unequal entry REVIEW_REQUIRED), r4 (`syn/` present at `H`; the owner's constraint to
  preserve all existing controls, fixtures and expectations, scoped to the r4 implementation), r5 (the
  O9-10 correction and its authorization), r1's dropped D1, and r5's own review and adoption steps.
  Sources: A-002, A-004, A-005, A-006, A-007, A-008, A-010, A-011, A-038, A-132.
- HIST-7. r5's problem statements: the plan record directory merged before `L` appears as side changes
  on `M` and cannot be pinned without a hash cycle; the item-2 arm passed only `hp.json` and the
  `GR.md:58` record. Sources: A-012, A-108.

**H.2 Review history.**
- HIST-8. v2 review addenda 3 and 4: verdicts REVISE, checked figures (14 commits; 48 / 23 / 15 / 15 /
  12; W1 / W2 lines), addendum 4's scope and its finding that V1 and V4 matched no profile and V2 and V3
  lacked deny rules (resolved by the deny rules and the V controls), the final verdict, the instruction
  to replace v2 sec. 12 open point 1 with the delegation contract (executed in v6.0e), and the
  replacement text for v2 sec. 11 and v6.0e sec. 12.2 citing #1169 comment 7093128173 (verification
  route; no check waived; each later step keeps its own owner gate, carried in sec. 0 and sec. 19).
  Sources: RV-003, RV-004, RV-022, RV-023, RV-024, RV-047, RV-058, V2-117, E-1297, MC-18.
- HIST-9. Review-item maps: the review-item to section and control map from v1 Q1 to v6.0b Q-1 (its
  citation "v1 Q5" names no v1 item, MC-8), the answer provenance through CHANGES-v4 and CHANGES-v5,
  and r5's maps of r1 findings, r2 findings, r3-to-r4 changes and the r4-to-r5 O9-10 correction.
  Finding labels are not identifiers (sec. 34). Sources: E-033, E-034, A-141, A-142, A-143, A-145.
- HIST-10. v1's open questions Q1-Q4 and their answers: the `E..H` changes resolved by an HP obligation
  with adjudication records (Q1), per-hit classification records (Q2), the preregistered context rule
  (Q3), and placement with op C covering non-manuscript paths (Q4); v2's open points on the delegation
  list source and the posit-count profile, closed by the delegation contract or obsolete. Sources:
  V1-150, V1-151, V1-152, V1-153, V2-121, V2-122.

**H.3 Grounding and rationale.**
- HIST-11. The frozen `ledger_check.py`: its build, relocation, assignment, checks CK1-CK8, `main`
  modes and self-test; its `main('check')` raising `TypeError` at line 523 while printing PIN MISMATCH
  at `H` (unreachable, because the frozen `main()` is never called); the frozen tool's error counts at
  `H` and `T1'` and the override-anchor displacement counts (withdrawn as unused). Sources: V1-013,
  V1-014, V1-015.
- HIST-12. The analysis of P's `edits_check` (precondition-only `--commit`, `--pins` on the wrong tree,
  unanchored `--repo-scan`), expressed in r6 as the mapping of sec. 18; the rationale that `main` moves
  (tool landing, `W`, plan amendment) and that `preserve_check --base W` failed on the unledgered
  workflow. Sources: V2-011, V2-123.
- HIST-13. v1's statement that a demonstration cannot show that moved or authorized text keeps its
  meaning (carried in sec. 2), and the method of the v1 reference figures (materialization by
  `git show`, prototype relocation, hit attribution). Sources: V1-128, V1-129.
- HIST-14. The conservative reading of the context rule (neighbour-pair context plus trailer, a strict
  superset of v3) and the history of the false v3 restatement claim for item 7. Sources: E-087,
  E-1288.
- HIST-15. The drop of DR-1d and DR-2 by owner decision V5-D1: no real-tree countercontrol and no match
  in history or at `H`, `W` and `T1'`; the cost of removal (no known retired line loses FAIL; V4 and V27
  become PASS, V15 REVIEW). Sources: E-1016, E-1017, E-1019.
- HIST-16. The `resid` T1'-specific outcome (four newly matched lines REVIEW_REQUIRED `unclassified`
  until a record or rule); the general rule is carried in sec. 14. Sources: E-1030.
- HIST-17. The argument that the proposed item 7 check is not weaker than the original (95 retired `H`
  lines all FAIL); its `H` part is reproduced by RT-I7A (sec. 31). Sources: E-1286.

**H.4 Derivation figures (historical measurements of sec. 31, R6.EVID.5).**
- HIST-18. Measured at `E`: all 697 site lines unique; 135 override anchors are substrings; 2 anchors
  duplicated in their file. Sources: V1-048.
- HIST-19. The 113 `E..H` site changes by merge (#1475 48, #1474 23, #1470 15, #1473 15, #1472 12,
  #1494 0). Sources: V2-034.
- HIST-20. Hit lines and review load at `T1'`: 84 hit lines in 197 regions (86 with `count-grep`); 200
  unheld lines, 116 outside regions, split 93 / 16 / 7; 226 distinct lines needing a record or rule;
  `ptr` 5 lines; the review-load totals (107 replacement-text lines, 113 HP sites, 12 meaning-context,
  10 indicator items) and P's `classify()` breakdown of the `repo` profile. Sources: E-040, E-041,
  E-043, E-044, E-1062, E-1063, E-1064.
- HIST-21. History search: no DR-1d, DR-2 or DR-3 match in 4677 historical blobs from 794 refs, and
  none at `H`, `W` or `T1'`. Sources: E-048, E-1018.
- HIST-22. Withdrawn figures (v2 24 / 24, v3 86, v4's single merger, `ptr` 4, the `repo` split, the
  frozen tool's error counts) and the reference rates of the indicator definitions. Sources: E-050,
  E-088.
- HIST-23. `resid` reference forms and reach by tree (28 resid-a, 17 resid-b or resid-c only, 4 hit by
  resid-b; 17 REVIEW lines added at `T1'`). Sources: E-1028, E-1029, E-1031.
- HIST-24. v6.0e sec. 14 measurement notes: throwaway scripts under `work-v4/` to `work-v55/` (not
  retained); the v5.5 parity (401 edits; 20000 random cases, 2822 / 16905 / 273), the v5.4 parity (399
  splices; 4000 cases), the v5.3 units and the S6 composition blob 86d79863, the v5.2 figures (7
  structure sites at `H`, 215 region lines, RT-D 45), the v5 figures (HP walk 113 / 584, deny counts,
  item 7 counts) and the figures carried from v4 (context 52 / 12, overlaps 19 / 31, region hits 84,
  unheld 200 / 93 / 16 / 7). Figures reproduced by a control on `main` are acceptance references only
  through that control (R6.EVID.4). Sources: E-1356, E-1357, E-1358, E-1359, E-1360, E-1361, E-1362.
