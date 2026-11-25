# RO-1 and #1143: scope comparison and proposed split, r1

**UNREVIEWED. Proposal for owner decision.** This is the prerequisite step of RO-1 (#1169 comment
6881175735): a read-only comparison of RO-1's scope with #1143, and a proposed split. It does not
write the specification of C. It establishes no result, adopts no premise, extension E or sector
condition C, and changes no Issue's scope, tier, readiness, authorization or writer. Nothing in it
takes effect until the owner decides.

**Writer:** Claude Code. **Reviewer:** ChatGPT. Both named by owner decision, #914 comment
6881174757 (`amaybaum`, 2026-11-14T17:06:36Z), batch B, recorded on #1169 comment 6881175735.

**Sources read.** GitHub Issues #1143, #1169, #914 and #1060 (bodies and comments) and draft PR
#1281 (body, comments, reviews), fetched through the REST API on 2026-11-14 at about 17:07Z.
Repository files at `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`; the ledger at
`origin/records/unified-ledger-914-20261114` `9ff3b8d913abfe720273ff162f6340054cb69437`; the
discriminator at #1281 head `3c445e6c20e832a338749c20faee5620d2b7ced5`. Reading only: no
computation on OI rules, no repository edit, no GitHub write.

**Abbreviations.** "c." = Issue or PR comment id. LEDGER = `LEDGER-r8.md` in
`verification/programmes/oi-qm/reconstruction/drafts/unified-ledger-20261114/` on the ledger branch.
SEL-DISC-1 = `verification/programmes/oi-qm/reconstruction/selection-discriminator-20261113/ASSESSMENT.md`
at the #1281 head above (STATUS.md in the same directory). "Inference" marks a statement this
note derives and no source states.

***

## 1. #1143's scope

### 1.1 What it owns

- **Title and purpose.** "OI-QM-SEL: finite-dimensional operational selection and native
  distinguishability". Its Purpose (#1143 body): "Determine whether the *class of physically
  realizable OI models* is operationally equivalent to a **predeclared, independently justified class
  of quantum theories** … Determine which preparations, interventions, settings and readouts are
  physically available and exactly what is unique or underdetermined."
- **Level 1 of its selection hierarchy** (#1143 body, table): "Why the quantum operational rules,
  rather than another probability theory? Does OI realize precisely a **predeclared class of QM
  models**, potentially with multiple members, without admitting non-quantum operational behaviour?"
  Levels 2 (dynamics/QFT) and 3 (representation/state) are recorded as downstream.
- **Record-class question** (#1143 body): "For a *predeclared* operation/record class C, ask: … For
  which lift class `L` does equality of all records `O_C(U,U′)` coincide with the previously defined
  two-sided gauge relation `G(U,U′)`?" Here "C" names a record class (C0, C1, C2-ch, C2-sel;
  `verification/programmes/oi-qm/reconstruction/bsel-2-b4prime-20261105/B4PRIME.md`:72–73 on
  `main`), not the sector C.
- **Embedded-observer selection** (#1143 body, owner reformulation 2026-11-09): "The proposed
  *OI-native selection* acts on **realizations together with observer–measurement interfaces**";
  its bounded questions include whether a restriction "filters substratum laws `φ`, realization
  distributions `μ`, observer embeddings, admissible preparations/readouts, or *tuples* of these"
  (question 2), "classical-preservation controls" (question 3), a "nonquantum countermodel"
  (question 4), and "one common realization supporting classical and nonclassical contexts"
  (question 5). "The current 'no non-quantum OI behaviours' requirement is read at the complete
  operational-theory level, not as a prohibition on classical observable fragments."
- **Self-described boundary** (author-side, unreviewed; #1143 c.6777830496, "Coordination"):
  "#1143 owns only the noncircular **selection** implication and its scoped falsifiers", with
  #1169/#866 owning "a source-first physical producer and controls", #913 renewal/reuse, #868 joint
  composition, #1211 the forward-source audit.
- **Open gap homes named by its newest record** (STATUS.md gap table, #1281 head): "Native
  information principle … Derive the bound from independently justified native premises, or identify
  a native violation/unavailability | #1143"; "Native executing protocol | #1143 / #866"; "Full
  quantum selection/equivalence | #1143 / #1169".

### 1.2 What it has done

| Unit | Result at its stated scope | Evidence state | Source |
|---|---|---|---|
| Selection-target specification | Candidate C (record classes) and lift classes, known/open cells; verdict UNSOURCED | Independently reviewed | #1143 c.6665278924, c.6665288579 |
| #1139 Q2A | `O_C ⇒ G` disproved for C0, C2-ch, C2-sel in the all-unitary class | On `main`, model-reviewed hand derivation | `…/bsel-2-q2a-ce-20261105/RESULT.md`:1–5 |
| M-1 | Same disproof inside `PPer` at `|V|=2`, `|A|≥2` (alternating-W pair) | On `main`, model-reviewed, not kernel-checked | `…/oiqmsel-m1-alt-w-20261105/RESULT.md`:1–5; #1143 body, "Fixed starting evidence" |
| M-2, S8-A | C-pers on the M-1 instance; S-8 UNSOURCED, "NOT SUPPLIED[`I₀`]: classical memory only" | M-2 on `main`; S8-A reviewed, off `main` | `…/oiqmsel-m2-cpers-20261105/RESULT.md`:1–5; #1143 c.6681999486, c.6682500558 |
| B4′ | Two-sided gauge relation against complete-record equivalence | On `main` | `…/bsel-2-b4prime-20261105/B4PRIME.md`:1–12, 19 |
| SEL-ACCESS-1 (#1224) | SEL-MENU: selection criteria factoring only through passive-law data "cannot force **quantum operational coverage**" when a required operation is absent from a restricted menu; "Any successful #1143 positive selection principle must be **access-sensitive**" | Full review ACCEPT WITH NITS, focused ACCEPT at `1b966a03`; draft, off `main` | #1143 c.6764552825, c.6765757859 |
| SEL-EXCL-1 (#1228) | The weak package (reversible dynamics, embedded cut, setting-independent latent source, classical records, no-signalling, fresh-cell finite reuse) admits a PR countermodel with CHSH 4; same-seed reuse in an enlarged menu signals | Full review ACCEPT WITH NITS, focused ACCEPT at `0ecfddeb`; draft, off `main` | #1143 c.6777584931, c.6779013024 |
| SEL-DISC-1 (#1281), "the #1143 discriminator" | Conditional IC₂ test: two input bits, one PR use, one classical message bit; PR gives `J=2`, classical-local and quantum-local references give `J≤1`; native availability and native information principle unsourced | Non-author ACCEPT 5897727347, ChatGPT ACCEPT 5898055055 (at `445b17f7`), publication ACCEPT at `37e19f3d`; documentary child `3c445e6c` awaiting focused review; draft, off `main` | SEL-DISC-1 §0 (ll. 7–15), §5.2 (l. 107), §9; #1281 c.6875713759 |

The "#1143 discriminator" that RO-1 must settle its overlap with (#1169 c.6880239486, c.6881175735)
is identified as SEL-DISC-1 by the queue proposal RO-1 was adopted from: "The Codex discriminator on
#1143 (comment 6863602000: 'the smallest target-neutral restriction … that excludes the explicit
reversible PR/supraquantum countercontrol') overlaps this question" (`QUEUE-PROPOSAL-r4.md`:720–723
on the ledger branch, adopted by #914 c.6880010243).

### 1.3 Readiness, authorization and writer now

- **Labels:** `tier: foundational`, `tier: provisional`, `readiness: partly ready` (#1143, read
  2026-11-14).
- **Readiness** (#1143 body): "selection-target specification: complete. M-1 and M-2 retain their
  existing specific paper-only decisions. **SEL-ACCESS-1** … focused diff confirmation remains …
  Native physical test remains **blocked** on its unresolved source."
- **Authorization** (#1143 body table): completed units as above; "Restricted lift classes
  (dependent planning) | `not authorized`"; "Native physical test, general QFT-class proof, theorem
  promotion, manuscript change | `not authorized`". SEL-DISC-1's handoff: "Request owner authority
  for any further run" (#1143 c.6863602000). No further #1143 unit is recorded as authorized.
- **Writer.** Standing agent ownership ended on 2026-11-14 (#1169 c.6880239486: "Assign a writer for
  each bounded unit on its accountable Issue when that unit is selected"; "Work already in flight
  keeps its existing writer"). In flight: SEL-DISC-1, writer Codex (SEL-DISC-1 l. 5; #1281
  c.6875713759). Completed: SEL-ACCESS-1 and SEL-EXCL-1, writer ChatGPT (#1143 c.6764389038,
  c.6769748021). No new #1143 unit has a writer.
- **Discrepancies in #1143's planning record** (findings, not corrected here):
  - The body says SEL-ACCESS-1's focused confirmation is pending; c.6765757859 records "focused
    independent non-author agent ACCEPT" at `1b966a03`.
  - The body's authorization table has no rows for SEL-EXCL-1 (authorized c.6769748021) or
    SEL-DISC-1 (handoff c.6863602000).
  - The body's board status is "Queued"; c.6775039087 records the owner's selection of Active,
    "requested target ACTIVE, not yet applied/verified".
  - The Purpose and rival outcome 3 ("Excess or incompatible OI behaviours: an OI model has no
    operational match in `Q`; full quantum equivalence fails") predate the superset amendment, under
    which "Not required. That every OI model behaves quantum-mechanically. OI may contain non-quantum
    behaviour" (#914 c.6875548603), and "'Every OI model is quantum' is outside the adopted target"
    (#914 c.6878200172).

## 2. RO-1's scope

- **Adopted text** (#914 c.6880010243, item 3, `amaybaum`, 2026-11-14T15:45:43Z): "Choose RO-1 only.
  Mark S-J ready for the paper specification and add S-A under #1169. Have the unit state what puts a
  model in C, what physically confines observation to C, and what ensures closure under the
  permitted operations and compositions. Specify C independently of matching quantum statistics.
  Name the writer and settle the overlap with #1143 before starting."
- **Planning rows** (#1169 c.6880022363): S-J, "Confinement to sector C", Foundational, "`ready` for
  the RO-1 paper-only specification only"; S-A, "Closure within C under the permitted operations and
  compositions", tier undetermined, same readiness. S-J is "Kept separate from S-A, closure within C"
  (#1169 c.6877981234).
- **What C is** (owner decision, #1169 c.6876591512): "C applies to the underlying model. It should be
  a physically stated condition, with its consequences for experiment families defined explicitly";
  "Require coverage and soundness. Necessity remains an optional future theorem"; "Require quantum
  behaviour for every physically performable experiment within C … Access closure must prevent a
  model from qualifying through selected quantum experiments while also permitting
  stronger-than-quantum experiments."
- **The sector part of the target** (#914 c.6875548603): "For a stated, physically justified condition
  C: within OI + E, the experiment families satisfying C are exactly those of QM_fin … (C ⟹ quantum)
  and (quantum ⟹ C)"; it "adds the obligation to state the sector condition C and justify it
  physically, including why observation is confined to that sector; for Bell this includes excluding
  stronger-than-quantum correlations in the physical sector, not in all of OI."
- **Non-circularity, Bell form** (#1060 body, BELL-QSET): "The sector condition C must be independently
  physically justified and may not be chosen by testing whether the resulting correlations match
  quantum predictions."
- **Ledger rows.** A-QM: "Inclusion QM ⊆ OI + E on one common realization, and the sector equivalence
  for a physically justified C, with its coverage and soundness directions | UO" (LEDGER:139,
  identical to the owner-accepted `LEDGER-r5.md`:120). S-J and S-A have no registry row; they appear in
  §H.3: "RO-1, the paper-only specification of C (S-J, S-A), bearing on A-QM, A-BELL, A-REAL and Q7"
  (LEDGER:1269). No sector condition C is stated on `main` (LEDGER:520–524, 560). Q7 asks whether
  H-Bell is "the route by which C's recorded exclusion is to be met, or is that exclusion to be stated
  on C directly" (LEDGER:937). LEDGER's header still reads "UNREVIEWED" (LEDGER:3), while the branch
  README and `REVIEW-r8.md` record ACCEPT; the rows quoted here are unchanged from r5 or reviewed in r6.
- **What RO-1 is and is not** (`QUEUE-PROPOSAL-r4.md`:674, 708–719): "A specification of C; not itself
  a test"; its next unit is to "state C as a condition on the underlying model with its consequences
  for experiment families … list each candidate physical ground for confinement to C, with its source
  on `main`, whether it is a premise, derived or newly proposed, and its §A.29 controls"; "RO-1 adds
  no prerequisite to #1060, #868 or #1143, or to any other authorized unit."
- **Sequencing** (#1169 c.6881175735): "The owner then decides the split. The specification itself
  starts only after that decision. Everything is paper-only."

## 3. The overlap

One row per question that both could claim. "Covered" means a record exists at the stated scope;
it does not mean the question is settled.

| # | Question | #1143 record | RO-1 / #1169 record | Already covered by |
|---|---|---|---|---|
| O1 | On what object does the condition act: `φ`, `μ`, embedding, programs, records, resources, or a tuple? | 2026-11-09 question 2 (#1143 body); SEL-DISC-1 §2 (l. 34): candidate realization `(S, φ, μ, E, Γ, R, C)` | "C applies to the underlying model" (#1169 c.6876591512, answer 1) | #1143 (SEL-DISC-1 §2, accepted); #1169 fixes only that C is on the model |
| O2 | What puts a model in C (membership) | Candidate restrictions P0–P7, each tested against the PR countercontrol and classical and quantum references (SEL-DISC-1 §3, ll. 46–55); no C stated | RO-1 adopted text; A-QM | Neither states C (LEDGER:520–524). #1143 covers candidate restrictions and their test outcomes |
| O3 | What physically confines observation to C (S-J) | Embeddedness and finite access as possible sources (2026-11-09 question 1); "the observer is finite" does not yield IC₂ (SEL-DISC-1 §7, ll. 155–157); passive-law criteria cannot force coverage (SEL-MENU) | S-J row (#1169 c.6880022363) | #1169 owns S-J by owner record. #1143 covers negative constraints on what a confinement ground can be |
| O4 | Native derivation of an information/access principle that would exclude PR | SEL-DISC-1 §10 item 3 (l. 199); STATUS gap "Native information principle … | #1143" | Would be one candidate confinement ground under S-J (inference) | #1143 (named home of the open gap) |
| O5 | Closure under permitted operations and compositions (S-A, access closure) | Fresh-cell versus same-seed reuse menus change the verdict (SEL-EXCL-1; SEL-DISC-1 §4, ll. 71–77); IC₂ needs an appended one-bit message protocol (§5.1, l. 95) | S-A row; "Access closure must prevent a model from qualifying through selected quantum experiments" (#1169 c.6876591512, answer 4) | #1169 owns S-A. #1143 covers countercontrols showing that the menu decides the result |
| O6 | C specified independently of quantum statistics | P7 "Admit precisely quantum/Tsirelson-compatible tables … Circular as an OI derivation" (SEL-DISC-1 l. 55); "A condition defined by 'agrees with quantum/Tsirelson' is not an OI derivation" (#1143 c.6863602000) | Adopted text; #1060 body | Both: the rule is RO-1's constraint; #1143 has applied it to its candidates |
| O7 | Classical contexts kept inside C; non-quantum behaviour allowed outside C | 2026-11-09 question 3 and "Do not exclude ordinary classical observations" (#1143 body); SEL-DISC-1 D6 and §6.3 | Superset amendment (#914 c.6875548603) | #1143 (controls); #914 (target) |
| O8 | Soundness and coverage directions for C | SOURCE / COVERAGE / SOUNDNESS audit schema (#1143 c.6777830496, author-side, unreviewed); SEL-DISC-1 §10 item 4 | A-QM (LEDGER:139); #1169 c.6876591512, answer 2 | Neither proves either direction. A-QM is the obligation (#914 target) |
| O9 | Supraquantum exclusion in the physical sector (Bell) | PR countercontrol (SEL-EXCL-1) and IC₂ discriminator (SEL-DISC-1) | Ledger Q7 bears on RO-1 (LEDGER:937, 1269) | #1060 owns BELL-QSET, H-Bell and Tsirelson selection (#914 c.6877803663); #868 coverage |
| O10 | Native availability of the operations C's closure and tests presuppose | SEL-DISC-1 §10 items 1–2; STATUS gap "Native executing protocol | #1143 / #866" | S-A would name them (inference) | #866, #913 O-REUSE, #1169 INT-AVAIL (#1143 c.6777830496, c.6772831173) |
| O11 | Which equivalence identifies "the same model" when deciding membership | B4′, Q2A and M-1: complete-record law equality and the two-sided gauge relation differ (`B4PRIME.md`:19; #1143 body) | Membership "puts a model in C" (adopted text) | #1143 (on `main`) |
| O12 | The letter C | Record class C (#1143 body); resource/renewal contract `C` (SEL-DISC-1 l. 34) | Sector C (#914, #1169) | Notation only; no scientific overlap |

## 4. Proposed split

**Principle.** RO-1 owns the *specification* of C: the statement of the condition on the model,
the catalogue of candidate confinement grounds with their status and controls, and the closure
contract. #1143 keeps the *selection tests and native derivations* it already holds: discriminators,
countermodels, record-class and lift-class questions, and the open native information principle.
This follows the existing records: S-J and S-A are #1169 rows (§2), and #1143 describes itself as
owning "the noncircular selection implication and its scoped falsifiers" (§1.1).

| # | Proposed owner | Why |
|---|---|---|
| O1 | Shared vocabulary; #1143's typing reused | RO-1 states C on SEL-DISC-1's tuple, so that each clause of C says which component it constrains, as #1143 c.6863602000 already requires of each restriction. No new typing is written. |
| O2 | **RO-1** | Stating C is RO-1's adopted text; no record states C. RO-1 lists P0–P7 as already-tested candidates with their recorded outcomes and does not re-test them. |
| O3 | **RO-1** (catalogue and classification of grounds) | S-J is #1169's row. RO-1 lists each candidate ground with its source, whether premise, derived or newly proposed, and its controls (`QUEUE-PROPOSAL-r4.md`:708–711). |
| O4 | **#1143** | Existing home of the open gap (STATUS gap table). If an information/access principle appears in RO-1's catalogue, RO-1 records it as "open, home #1143" and attempts no derivation. |
| O5 | **RO-1** (the closure contract on C) | S-A is #1169's row. The contract must decide, for each #1143 countercontrol, whether its continuation (fresh-cell use, same-seed reuse, one-bit message) is inside C. Executability of those operations stays with O10. |
| O6 | **RO-1** (as a constraint on its own text) | The rule binds C's definition. #1143's P7 verdict is taken as already established. |
| O7 | **#1143** (controls) | RO-1 states that C must admit them and cites #1143's references. |
| O8 | Neither unit: A-QM under #914, with #1169 | RO-1 states C so that both directions are well posed and says what each would require; #1143's schema is used as vocabulary only, being unreviewed. |
| O9 | **#1060** (BELL-QSET, Q7), #868 (coverage) | RO-1 reports how its C bears on Q7 and adds no prerequisite to #1060 (`QUEUE-PROPOSAL-r4.md`:717–719). |
| O10 | **#866, #913, #1169 INT-AVAIL** | Existing owners (#1143 c.6777830496). RO-1 lists the availability facts C presupposes and names their homes. |
| O11 | **#1143** | RO-1 takes B4′/Q2A/M-1 as given and states which identity relation its membership clause uses; it does not reopen O_C versus G. |
| O12 | Writer convention | RO-1 uses "C" for the sector only and names #1143's objects as "record class C0, C2-ch …" and "resource contract". No #1143 record is renamed. |

### 4.1 What RO-1 takes from #1143 as input

At their accepted scope, as controls and constraints, not re-derived:

1. **SEL-MENU** (SEL-ACCESS-1, #1224 at `1b966a03`): any confinement ground or membership clause that
   depends only on passive-law data cannot force coverage. RO-1's grounds must be access-sensitive
   or say why the restriction to a menu is itself physical.
2. **The PR countercontrol and the two menus** (SEL-EXCL-1, #1228 at `0ecfddeb`): fixed reversible
   dynamics, an embedded cut, a setting-independent source, valid records and fresh-cell
   no-signalling together admit CHSH 4. A C built only from these does not exclude supraquantum
   behaviour; the closure contract must state the reuse grammar.
3. **The restriction ledger P0–P7 and the IC₂ discriminator** (SEL-DISC-1 §§3, 5): P3 and P4 exclude
   PR but also the quantum Bell target; P5 is not a separator; P7 is circular; IC₂ separates PR from
   the classical and quantum references only if its protocol is executable.
4. **Classical and quantum references** (SEL-DISC-1 §6; #1143 body, 2026-11-09 question 3): RO-1's C
   must keep ordinary classical contexts.
5. **The `main` records** (B4′, Q2A, M-1, M-2) and the controls #1143 preserves, including "the
   `|A|=1` rank-one case and the exact finite-horizon `S⇔D⇔Q_fb` fixed-basis correspondence" (#1143
   body).

**Evidence limit.** Items 1–3 are reviewed paper results held on draft, unmerged PRs. Under §A.42
item 8 and §A.46 item 7, a claim RO-1 lands on `main` that uses them carries a support-off-`main`
gap until their content is on `main`. A paper-only specification can cite them at their scope; it
cannot present a consequence of them as established.

### 4.2 What RO-1 must not duplicate

- The PR construction, its no-signalling and reuse lemmas, the IC₂ proofs (D5–D7) and SEL-MENU.
- A new discriminator, countermodel or candidate restriction tested against PR: that is #1143's line
  of work (c.6863602000), and a new #1143 unit needs its own owner authority.
- The native derivation of an information/access bound (O4), and any native availability
  assessment (O10).
- Record-class and lift-class questions (O11); restricted lift classes are "not authorized"
  (#1143 body).
- Proofs of the sector directions, BELL-QSET or Bell-set coverage (O8, O9).

### 4.3 How #1143's discriminator relates to "C independent of quantum statistics"

- **IC₂ is not a quantum statistic.** It "contains no quantum table or tunable Tsirelson constant"
  (SEL-DISC-1 §7, l. 162) and concerns "ordinary classical input recovery and a communication budget"
  (§5.1, l. 93). Its content does not break the rule.
- **Its motive can.** "Imposing IC₂ because it rejects PR would still be an additional physical
  premise. A native derivation must explain it independently" (SEL-DISC-1 l. 163). A clause of C
  whose only justification is that it removes PR while keeping the quantum references is chosen by
  testing against quantum predictions, which #1060 forbids. IC₂ can enter C only with a physical
  justification stated before any test, and that justification is O4, which is open.
- **Its quantum comparator is a test, not a definition.** D7 uses "quantum comparator premises, not
  derived OI operations" (SEL-DISC-1 l. 129). RO-1 may cite such results only as controls applied to
  a C already stated.
- **Proposed procedure for RO-1** (proposal): state C and each ground's justification first; then
  apply the PR countercontrol, the reuse menus, IC₂ and the classical and quantum references as
  falsifiers under a decision rule fixed in advance (§A.29: "Preregister the decision *rule*");
  reject any clause whose stated justification is a control's outcome. Applying the PR control after
  C is stated is a soundness test the target requires (#914 c.6875548603, Bell clause); it is not a
  choice of C by testing.

## 5. Owner questions the split leaves open

1. **The split.** Adopt §4 as proposed, or modify it?
2. **#1143's purpose under the superset target.** Its Purpose and rival outcome 3 require that OI admit
   no non-quantum behaviour (§1.3). Under #914 c.6875548603 that is not required. Should #1143's
   level-1 question be restated, for example as "does native OI select or exclude a given restriction",
   with the sector form owned by #1169? This note proposes no wording.
3. **Derivation homes for confinement grounds.** If RO-1 catalogues a ground that is an
   information/access principle, its derivation is proposed for #1143 (O4). For a ground of another
   kind, is the derivation a later S-J unit under #1169?
4. **Off-`main` inputs.** May RO-1 cite #1224, #1228 and #1281 at their reviewed scope while they are
   draft, with the §A.42 item 8 gap stated, or should their content land first?
5. **Admissible justification.** What counts as an independent physical justification under #1060's
   rule for a clause that also excludes PR, such as IC₂? Is the procedure of §4.3 acceptable?
6. **Q7.** Should RO-1 present both routes (H-Bell, or the exclusion stated on C directly) with
   their consequences, or does the owner choose one first?
7. **Model identity.** Which relation identifies "the same model" for membership in C: complete-record
   law equality, the two-sided gauge relation, or another relation stated by RO-1 (O11)?
8. **#1143 planning maintenance.** The four discrepancies in §1.3 are for the owner or a maintenance
   update under §A.45 rule 3; RO-1 does not edit #1143.
9. **Codex's in-flight unit.** SEL-DISC-1's documentary child awaits focused review (#1281
   c.6875713759). Does the split change anything in that unit? This note proposes not.
