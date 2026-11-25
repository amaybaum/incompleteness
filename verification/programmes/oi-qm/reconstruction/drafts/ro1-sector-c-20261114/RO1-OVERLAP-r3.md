# RO-1 and #1143: scope comparison and proposed split, r3

**UNREVIEWED. Proposal for owner decision.** This is the prerequisite step of RO-1 (#1169 comment
6881175735): a read-only comparison of RO-1's scope with #1143, and a proposed split. It does not
write the specification of C. It establishes no result, adopts no premise, extension E or sector
condition C, and changes no Issue's scope, tier, readiness, authorization or writer. Nothing in it
takes effect until the owner decides.

**Revision r3.** r3 applies ChatGPT's review of r2 (PR #1294 review 5906070407, ACCEPT WITH
CHANGES, at `49d90f59`): C1, the target's quantifiers (§§2, 3 O8, 4.6, 5.1), and C2, necessity
recorded as a decided scope (§4.6). Nothing else changes. Dispositions are in
`RESPONSE-REVIEW-r2.md`. r2 (`RO1-OVERLAP-r2.md`, SHA-256
`d4617d155ee4d8f593ec1bbbf350d72c4016c2fa4008e0803cfd13506848f615`) is left unchanged.

**Revision r2.** r2 puts r1 into the owner's structured format, relayed by the coordinator: one
comparison table (§3), the owner's six items answered in turn (§4), the three kinds of statement
labelled, and the recommendation followed by the owner questions (§5). r1 (`RO1-OVERLAP-r1.md`,
SHA-256 `6aa7b08ea6f0f4f9f7d94e43c232e9fa938d50dc97679c8db2e807a10609a501`) is left unchanged.
§§1–2 are r1's text unchanged. r1's §3 overlap table and §4 allocation table are merged into the
single table of §3. r1's §§4.1–4.3 are kept as §§4.5.1–4.5.3. No source was re-read, and r2 adds no
finding beyond the evidence labels and the open-question homes.

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

**Statement labels (§§3–5).**
- **[Result]**: an existing result, cited. Its evidence state is one of: *result on `main`*;
  *reviewed result off `main`* (on a draft PR or branch); *author-side or unreviewed*.
- **[Proposed obligation]**: something this note proposes that a unit should do or own. It binds no
  one until the owner decides.
- **[Unproved assumption]**: a premise this note or a source relies on that no result establishes.

Owner decisions and planning rows are cited as records. They are not results.

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
- **Quantifiers of the sector target** (stated here; each is quoted from its owner record). The
  shorthand "(quantum ⟹ C)" above is read as the later owner decision fixes it (#1169 c.6876591512:
  answer 1 "refines the earlier wording on #914", and answer 2 makes necessity optional). On that
  reading, which is this note's, it means coverage, not necessity.
  - *Coverage* (required): every finite quantum experiment family in the agreed scope is realized
    within C, in the one common model: "QM_fin ⟹ OI + E on one common substratum–observer
    realization" (#914 c.6875548603); "One fixed model, with one common extension E, must support
    subsystems realizing every quantum carrier in the agreed scope" (#1169 c.6876591512, answer 3);
    "one model that satisfies the necessary premises simultaneously" (#914 c.6877420015, item 4). A
    separate model fitted to each quantum experiment does not meet it.
  - *Soundness* (required): every physically performable experiment within C, including accessible
    preparations, interventions, compositions and complete records, is quantum (#1169 c.6876591512,
    answer 4).
  - *Necessity* (not required): that every OI realization displaying quantum behaviour satisfies C.
    "Necessity remains an optional future theorem. Models outside C may also reproduce quantum
    statistics. Membership in C need not characterize every possible quantum realization" (#1169
    c.6876591512, answer 2).
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


## 3. Comparison table

One row per topic. Evidence states: **main** = result on `main`; **off-main** = reviewed result off
`main` (draft PR or branch); **author** = author-side or unreviewed; **none** = no result. A row's
evidence entry is an existing result or the absence of one. Its allocation is a proposed
obligation.

| # | Obligation or topic | Current accountable Issue | Existing evidence or result | Proposed owner | Reason for the allocation |
|---|---|---|---|---|---|
| O1 | The object a condition acts on: `φ`, `μ`, embedding, programs, records, resources, or a tuple | #1143 (typing); #1169 (C is on the model) | **off-main:** SEL-DISC-1 §2 (l. 34), candidate realization `(S, φ, μ, E, Γ, R, C)` (#1281). Record: "C applies to the underlying model" (#1169 c.6876591512, answer 1) | shared interface | RO-1 states each clause of C on #1143's tuple, as #1143 c.6863602000 already requires of each restriction. No new typing is written. |
| O2 | What puts a model in C (membership) | #1169 (RO-1; A-QM) | **none** for C: no sector condition C is stated on `main` (LEDGER:520–524, 560). **off-main:** candidate restrictions P0–P7 with their PR, classical and quantum outcomes (SEL-DISC-1 §3, ll. 46–55) | RO-1 | Stating C is RO-1's adopted text (#914 c.6880010243). RO-1 lists P0–P7 as already tested and does not re-test them. |
| O3 | What physically confines observation to C (S-J) | #1169 (S-J row, c.6880022363) | **none** for any ground. **off-main:** SEL-MENU, passive-law criteria cannot force coverage (#1224, c.6764552825); "the observer is finite" does not yield IC₂ (SEL-DISC-1 §7, ll. 155–157). Planning question: 2026-11-09 question 1 (#1143 body) | RO-1 | S-J is #1169's row. RO-1 catalogues each candidate ground with its source and status (premise, derived or newly proposed) and its controls (`QUEUE-PROPOSAL-r4.md`:708–711). It derives none of them. |
| O4 | Native derivation of an information or access principle that would exclude PR | #1143 (STATUS gap table: "Native information principle … \| #1143") | **none:** D8, "Not supplied" (SEL-DISC-1 §9). **off-main:** the gap and its resolving condition (SEL-DISC-1 §10 item 3, l. 199) | #1143 | Existing named home. If such a principle appears in RO-1's catalogue, RO-1 records it as "open, home #1143". |
| O5 | Closure of C under permitted operations and compositions (S-A, access closure) | #1169 (S-A row, c.6880022363) | **none** for C. **off-main:** fresh-cell versus same-seed menus change the verdict (#1228; SEL-DISC-1 §4, ll. 71–77); IC₂ needs an appended one-bit message protocol (§5.1, l. 95). Record: access closure required (#1169 c.6876591512, answer 4) | RO-1 | S-A is #1169's row. The closure contract must say, for each #1143 countercontrol, whether its continuation is inside C. Whether those operations can be executed natively is O10. |
| O6 | C specified independently of quantum statistics | #1169 (adopted text); #1060 (Bell form) | **off-main:** P7, "Circular as an OI derivation" (SEL-DISC-1 l. 55). Records: #914 c.6880010243 item 3; #1060 body, BELL-QSET | RO-1 | The rule binds the definition of C. #1143's P7 verdict is taken as already established at its scope. |
| O7 | Classical contexts inside C; non-quantum behaviour allowed outside C | #1143 (controls); #914 (target) | **off-main:** classical and quantum references, D6 and §6.3 (SEL-DISC-1). Records: 2026-11-09 question 3 (#1143 body); superset amendment (#914 c.6875548603) | #1143 | #1143 holds the controls. RO-1 requires C to admit them and cites them. |
| O8 | Soundness (every physically performable experiment within C is quantum) and coverage (every quantum experiment family in scope is realized within C, in the one common model); not necessity (§2) | #914 (A-QM), with #1169 | **none** for any C. **main:** the related characterization of an extension, OI⁺ ⟺ exact finite endomorphic operational QM (LEDGER:155, 540; `papers/Main.md`:584–588), which is not a sector result. **author:** SOURCE / COVERAGE / SOUNDNESS schema (#1143 c.6777830496) | unresolved/other: #914 | Neither unit proves coverage or soundness. RO-1 states C so that both are well posed with the quantifiers of §2. It uses #1143's schema as vocabulary only. |
| O9 | Supraquantum exclusion in the physical sector; Q7 | #1060 (BELL-QSET, H-Bell, Tsirelson selection); #868 (coverage) | **main:** unrestricted OI realizes PR laws (`papers/Main.md`:360; LEDGER:140). **off-main:** PR countercontrol (#1228), IC₂ discriminator (#1281). **none** for exclusion in any C | unresolved/other: #1060 | Owner records place BELL-QSET in #1060 (#914 c.6877803663). RO-1 reports how its C bears on Q7 and adds no prerequisite to #1060 (`QUEUE-PROPOSAL-r4.md`:717–719). |
| O10 | Native availability of the operations C's closure and tests presuppose | #866; #913 (O-REUSE); #1169 (INT-AVAIL) | **off-main:** #866 source screen STOPPED / UNSOURCED (#1223; #1143 c.6764740008). **none** for a positive source | unresolved/other: #866 | Existing owners (#1143 c.6777830496, c.6772831173). RO-1 lists the availability facts C presupposes and names their homes. |
| O11 | Which relation identifies "the same model" when membership in C is decided | #1143 (O_C versus G) | **main:** complete-record law equality and the two-sided gauge relation differ, in the all-unitary class and in `PPer` at `|V|=2`, `|A|≥2` (`…/bsel-2-b4prime-20261105/B4PRIME.md`:19; Q2A and M-1 RESULT.md). These are model-reviewed hand derivations, not kernel-checked | shared interface | #1143 supplies the relations and their results. RO-1 must name one relation in its membership clause. Which one governs is an open question for the owner (§4.6). |
| O12 | The letter C | — | **none** (notation). Record class C (#1143 body; `B4PRIME.md`:72–73); resource/renewal contract `C` (SEL-DISC-1 l. 34); sector C (#914, #1169) | shared interface | Writer convention: RO-1 uses "C" for the sector only and names the others in full. No #1143 record is renamed. |

## 4. The owner's six items

### 4.1 Obligations already covered by #1143

- [Result, main] Record-class and lift-class separations: `O_C ⇒ G` is disproved for C0, C2-ch and
  C2-sel in the all-unitary class (#1139 Q2A) and in `PPer` at `|V|=2`, `|A|≥2` (M-1); B4′ dispositions;
  M-2 on the M-1 instance (§1.2). These cover O11's supply side.
- [Result, off-main] SEL-MENU (#1224); the PR countercontrol and its two menus (#1228); the P0–P7
  ledger, the conditional IC₂ exclusion and the classical and quantum references (#1281). These cover
  O1's typing, O2's candidate list, O5's countercontrols, O6's P7 verdict and O7.
- [Result, off-main] The S8-A obstruction "NOT SUPPLIED[`I₀`]" for C-pers (#1143 c.6681999486).
- [Proposed obligation, recorded by #1143 itself] The native information principle (O4) and, jointly
  with #866, the native executing protocol (STATUS gap table, #1281).

### 4.2 Obligations that belong only to RO-1

- [Proposed obligation] **O2**: stating C on the underlying model, with its consequences for
  experiment families made explicit (#1169 c.6876591512, answer 1).
- [Proposed obligation] **O3**: the catalogue of candidate confinement grounds (S-J), each classified
  as premise, derived or newly proposed, with its controls.
- [Proposed obligation] **O5**: the closure contract (S-A), stating which operations and compositions
  C is closed under, so that access closure (answer 4) can be checked.
- [Proposed obligation] **O6**: applying the rule "C independent of quantum statistics" to RO-1's
  own text.

No existing result covers any of these: [Result, none] (LEDGER:520–524, 560).

### 4.3 Shared boundaries and dependencies

- **O1, the tuple.** [Proposed obligation] RO-1 writes C on #1143's tuple. RO-1 depends on #1143's
  typing; #1143 depends on nothing in RO-1.
- **O11, model identity.** [Proposed obligation] #1143 supplies the relations; RO-1 names the one its
  membership clause uses. The choice is open (§4.6).
- **O12, notation.** [Proposed obligation] A writer convention only.
- **Dependencies on #1143, one direction only.** [Proposed obligation] RO-1 consumes #1143's accepted
  results as inputs and controls (§4.5.1). RO-1 adds no prerequisite to #1143
  (`QUEUE-PROPOSAL-r4.md`:717–719).
- **O4 to O3.** [Unproved assumption, inference] An information principle derived under O4 would be
  one candidate confinement ground under O3. No source states this link.
- **Dependencies outside the two Issues.** O8 (#914), O9 (#1060, #868) and O10 (#866, #913).

### 4.4 Possible duplicated work or conflicting definitions

- **The letter C (O12).** Three objects share the letter: #1143's record class (C0, C2-ch, C2-sel),
  SEL-DISC-1's resource/renewal contract, and the sector C. A reader could take a #1143 result "for
  C" as a sector result. The proposed convention in §3 removes the ambiguity without renaming any
  record.
- **Model identity (O11).** [Result, main] Record-law equality and the gauge relation are different
  relations. If RO-1's membership clause and #1143's tests used different ones, the same pair of lifts
  could be one model for RO-1 and two for #1143. [Proposed obligation] RO-1 names its relation
  explicitly.
- **Candidate restrictions (O2).** Duplication risk: RO-1 re-testing P0–P7 against PR.
  [Proposed obligation] RO-1 cites their outcomes and does not re-test them.
- **New discriminators (O3, O4).** Duplication risk: RO-1 proposing and testing a new PR-excluding
  restriction, which is #1143's line of work (c.6863602000). [Proposed obligation] RO-1 lists
  grounds; it does not test new ones.
- **#1143's purpose.** Conflict: #1143's Purpose and rival outcome 3 require that OI admit no
  non-quantum behaviour. The superset amendment does not require this (#914 c.6875548603,
  c.6878200172; §1.3). Under the old reading #1143 would own the whole of C. This note does not resolve
  the conflict (§5, question 2).
- **Readiness records.** #1143's body is out of date on four points (§1.3). This is not a conflict
  of definitions, but it misstates what #1143 has done.

### 4.5 The proposed division

[Proposed obligation] **RO-1 owns the specification of C:** the statement of the condition on the
model (O2), the catalogue of candidate confinement grounds (O3), the closure contract (O5) and the
non-circularity rule as applied to its own text (O6). **#1143 keeps its selection tests and native
derivations:** discriminators, countermodels, the classical and quantum controls (O7), the
record-class and lift-class questions (O11's supply side), and the native information principle
(O4). **Shared interface:** O1, O11 and O12. **Elsewhere:** O8 (#914), O9 (#1060, #868) and O10
(#866, #913). This follows the existing records: S-J and S-A are #1169 rows (§2), and #1143
describes itself as owning "the noncircular selection implication and its scoped falsifiers" (§1.1).

[Unproved assumption] The division assumes that C can be stated, and its grounds catalogued,
without first settling any open question of §4.6. If stating C requires a decision on one of them,
RO-1 stops and returns that question to the owner (§5).

The three subsections below are r1's §§4.1–4.3, unchanged apart from their numbers. Labels:
the inputs listed in §4.5.1 are [Result] items in the evidence states given in §3. Taking them as
inputs, and every item of §4.5.2, is a [Proposed obligation]. The procedure at the end of §4.5.3 is
a [Proposed obligation].

#### 4.5.1 What RO-1 takes from #1143 as input

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

#### 4.5.2 What RO-1 must not duplicate

- The PR construction, its no-signalling and reuse lemmas, the IC₂ proofs (D5–D7) and SEL-MENU.
- A new discriminator, countermodel or candidate restriction tested against PR: that is #1143's line
  of work (c.6863602000), and a new #1143 unit needs its own owner authority.
- The native derivation of an information/access bound (O4), and any native availability
  assessment (O10).
- Record-class and lift-class questions (O11); restricted lift classes are "not authorized"
  (#1143 body).
- Proofs of the sector directions, BELL-QSET or Bell-set coverage (O8, O9).

#### 4.5.3 How #1143's discriminator relates to "C independent of quantum statistics"

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


### 4.6 Open scientific questions the split must not decide implicitly

Each question stays open, and accepting the split does not answer it. RO-1 may record a question
and its consequences for C, and must not settle it by how C is worded.

| Question | Status now | Issue that keeps it open |
|---|---|---|
| Is IC₂, or any information or access principle, native to OI, derivable from independently justified premises? (O4) | [Result, none]: "Not supplied" (SEL-DISC-1 D8). [Result, off-main]: operational no-signalling alone does not imply IC₂; the accepted PR protocol violates it (SEL-DISC-1 §7, l. 155) | #1143 |
| Is the protocol IC₂ needs (independent inputs, one-bit message, fixed clock) executable natively? (O10) | [Result, none]. [Unproved assumption]: its availability is an added hypothesis (SEL-DISC-1 §5.1, l. 95) | #866, with #1143 (STATUS gap table) |
| Which relation governs membership in C: complete-record law equality, the two-sided gauge relation, or another? (O11) | [Result, main]: the two relations differ (B4′, Q2A, M-1). No result chooses between them for C | #1169 for the choice of relation for C; #1143 for the relations themselves (proposed) |
| Does coverage (every quantum experiment family in scope realized within C, in one common model) or soundness (every physically performable experiment within C quantum) hold for any stated C? (O8) | [Result, none] for any C. [Result, main]: only the extension characterization OI⁺ (LEDGER:155) | #914 (A-QM) |
| Q7: is supraquantum exclusion in the physical sector met through H-Bell, or stated on C directly? (O9) | [Result, none]. H-Bell is open (LEDGER:937; #1060) | #1060, with the ledger's Q7 under #914 |
| Can confinement grounds that depend only on passive-law data ever suffice? (O3) | [Result, off-main]: SEL-MENU says no, but only for a class that contains a full/restricted-menu pair with the same passive-law data and in which a required operation has no alternative implementation. [Unproved assumption]: that the actual OI class has these properties. SEL-DISC-1 notes that SEL-MENU "does not prove that all physical OI classes permit arbitrary menu deletion" (l. 36) | #1143 |

**Decided target scope, not an open question.** Whether necessity of C is required (that every OI
realization displaying quantum behaviour satisfies C) is decided: it is not required, and it is an
optional future theorem, unproved. Owner records: "Necessity remains an optional future theorem"
(#1169 c.6876591512, answer 2); "Necessity of C remains optional" (#914 c.6878200172). The split
neither requires nor excludes later work on it, and RO-1 does not take it up.

## 5. Recommendation and owner questions

### 5.1 Recommendation (recommendation, not adopted)

[Proposed obligation] Adopt the division of §4.5. RO-1 under #1169 writes the specification of C
(O2, O3, O5, O6) on #1143's tuple (O1). It names its model-identity relation (O11) and uses "C" only
for the sector (O12). It consumes #1143's accepted results as controls, applied after C is stated,
under a decision rule fixed in advance (§4.5.3). #1143 keeps its selection tests, its controls (O7)
and the native information principle (O4). O8 (coverage and soundness, with the quantifiers of
§2; not necessity), O9 and O10 stay with #914, #1060/#868 and #866/#913.
None of the questions in §4.6 is decided by this division. If stating C requires deciding one of
them, RO-1 stops and returns it to the owner.

### 5.2 Owner questions

1. **The split.** Adopt §4.5 / §5.1 as proposed, or modify it?
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
   rule for a clause that also excludes PR, such as IC₂? Is the procedure of §4.5.3 acceptable?
6. **Q7.** Should RO-1 present both routes (H-Bell, or the exclusion stated on C directly) with
   their consequences, or does the owner choose one first?
7. **Model identity.** Which relation identifies "the same model" for membership in C: complete-record
   law equality, the two-sided gauge relation, or another relation stated by RO-1 (O11)? And is the
   choice RO-1's to propose, or the owner's to make before RO-1 starts?
8. **#1143 planning maintenance.** The four discrepancies in §1.3 are for the owner or a maintenance
   update under §A.45 rule 3; RO-1 does not edit #1143.
9. **Codex's in-flight unit.** SEL-DISC-1's documentary child awaits focused review (#1281
   c.6875713759). Does the split change anything in that unit? This note proposes not.
10. **Notation.** Is the convention of O12 (the letter C for the sector only; full names for #1143's
    record classes and SEL-DISC-1's contract) acceptable?
