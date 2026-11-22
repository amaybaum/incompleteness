# A1 deletion — preregistration of the deletion edit (planning only)

**Status.** Writer's preregistration, WIP / UNVERIFIED, not independently reviewed. Planning only: no
manuscript, generated artifact, ledger or registry file is changed by this record, and nothing in the edit
list has been applied. A1 (Main posit ledger item (ii)) remains printed as an open hypothesis, not adopted,
until a separate owner authorization of the execution.

**Reconciled.** The plan is re-pinned to merged `main` at `97070c986c28f7ff8a443cbda5890c1694dd76dd` (Step 2
complete, S2-E included; #1481 adds AGENTS.md §A.48), with the five owner decisions of #1169 comment 7058783437 and the round-5 findings
applied (§24). Execution is not authorized.

**Revision.** Revised by additive commits after the early independent review of `36a73526` (round 1,
REVISE; record on #1477) and the owner rulings of #1169 comment 7057674976, and after the round-2 delta
review of `67736e55` (ACCEPT-WITH-NITS) the round-3 delta review of `a58cf594` (ACCEPT-WITH-NITS) and the round-4 check of `f18c8677` (ACCEPT, one
non-blocking nit). §17–§20 answer the reviews finding by finding; §21–§23 record the amendments for H-11, repository-wide consistency and the configuration-space sentence; §24 the reconciliation; §25 the round-5 closure table and the owner's decisions 2–5 of #1169 comment 7059136165 (safeguards for the destructive change, the frozen H-B sentence, the guard pins). Edit IDs are stable: an ID reviewed at `36a73526` names the same edit here (its
`revised` field marks a changed replacement), and new edits take new IDs (D253–D258).

## 0. Authority, decision and goal link

**Authorization** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7057236079](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7057236079),
2026-11-21T04:24:35Z, "Owner decision record: drafting the A1 deletion preregistration"), quoted:

> **Approved, planning only.** The A1 deletion preregistration may be drafted now, in parallel with the
> remaining Step 2 work. This authorizes neither the deletion of A1 nor any manuscript change.
>
> ### Scope
> - Draft the exact proposed rewrites for all 194 pointer sites. Each gives the original text, the
>   replacement text, the location and the justifying ledger row.
> - Draft the proposed deletion of A1 (Main ledger item (ii)), with any consistency corrections that are
>   immediately necessary.
> - Classify each rewrite as mechanical, semantic, or requiring further scientific review.
> - Verify that:
>   - the 27 finite-only rows stay explicitly scoped;
>   - the 9 open rows stay open;
>   - the 9 relabelled conditions stay qualified.
> - Account for the accepted S2-C wording, the S2-D decisions and the pending S2-E changes. Keep the
>   no-change decision for ch18:40.
> - Record the baseline commit, expected dependencies, conflicts and reproducibility checks.
>
> ### Boundaries
> - No manuscript edits, no deletion of A1, no regeneration of PDF or TeX.
> - No change to any accepted Step 2 scientific conclusion.
> - The preregistration is fixed before any implementation.
> - All proposed rewrites are reconciled against the final merged Step 2 manuscripts before execution.
> - Implementation needs separate owner authorization and an independent review of the resulting changes.
> - A draft PR containing only the preregistration may be opened for early independent review.
>
> **Objective.** Remove A1 as a global assumption without silently weakening any theorem, introducing
> unjustified physical assumptions, or concealing unresolved dependencies.

**Design decision** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7057297534](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7057297534),
2026-11-21T04:30:15Z, "Owner decision record: retire A1, cardinality-neutral design"), quoted:

> - **Retire A1 permanently.** A1 is removed from the active assumptions. It is not redefined.
> - **Reserve the A1 identifier.** It is never reused (AGENTS.md §A.30).
> - **Preserve cardinality neutrality.** OI does not assume that the universe has finitely many
>   configurations, and it does not assume that it has infinitely many.
> - **Retain conditional results.**
>   - Finite-only results remain explicitly scoped.
>   - Results that need an additional probability law or another hypothesis state it openly.
> - **Preserve surviving identifiers.** A2, A3 and the other identifiers are not renumbered as part of
>   A1-EXIT.
> - **Add a regression check against new global infinity assumptions.**
>
> **Authorization boundary.** This settles the design, not its implementation. [...]
>
> **Final principle.** OI should derive what it can without imposing a global cardinality assumption,
> rather than replacing finiteness with infinity.

**Owner guidance** (`amaybaum`, in session, 2026-11-21, relayed by the coordinating session and formalized
by the decision above): "The goal is not to establish that the universe is infinite. It is to show that OI
does not need to assume whether the universe is finite or infinite."

**Owner rulings on the two §12 questions** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7057674976](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7057674976),
2026-11-21T05:05:42Z), quoted:

> | Rewrite the A1 pointer at ch18:40 | Approved, narrowly scoped |
> | Keep Structure's finite OI class | Approved, as a finite subclass |
>
> **ch18:40.** The pointer is replaced with the precise finite-recurrence condition. The statement's
> physical content and its conditional scope are preserved. The earlier no-change ruling concerned the
> inflow content.
>
> **Structure's finite OI class**
> - The class keeps its existing results and is named "finite OI class" where necessary.
> - Nothing implies that an OI-compatible substratum must be finite.
> - Its results are not extended to infinite systems without further proof.
> - A separate research Issue is opened for a cardinality-neutral OI class.
>
> **Deletion preregistration (#1477).** The review findings of round 1 (REVISE) must be resolved before
> execution is authorized. Deleting A1 remains unauthorized.

The cardinality-neutral OI class is tracked in Issue #1478.

**Goal link (§A.47).** The A1-exit objective (#1169), the owner's goal for Step 1 row A1-EXIT: "Make OI's
foundational formulation independent of the assumption that the whole universe is finite, while keeping
honest limitations on the results that still require finiteness." This record decides, for each of the 194
pointer sites and for item (ii) itself, the exact text that would replace the pointer at execution and
whether that replacement needs scientific review; it does not decide whether the deletion is executed.

## 1. Drafting base and inputs

| Input | Commit | Use |
|---|---|---|
| `main` (drafting base) | `97070c986c28f7ff8a443cbda5890c1694dd76dd` | `old` strings are exact and unique here |
| A1-EXIT ledger pin | `e837e3dbaa605efc867a213f3345cee14c36d8f5` | ledger site lines; each edit's `site` is its pin line, and the sitemap check maps the base line of its `old` string back to the pin by line alignment |
| S2-A head (#1470), pre-merge | `dd95fcd0b3f83637e9a51a7ccc527dc737d5aae7` | the retired projection (§24) |
| S2-B head (#1473), pre-merge | `5c6cdfea775313d8475b6e929bb7f48a071b525e` | the retired projection (§24) |
| S2-C head (#1474), pre-merge | `cb6d1b87e7e001ea1a4bdd6d260ca4b616d7b135` | the retired projection (§24) |
| S2-D head (#1472), pre-merge | `5efd856b3509d767e6ef84226f01b66680137c75` | the retired projection (§24) |
| S2-E head (#1475), pre-merge | `7ed84339c48bb55aa374fce1a894e988501e4e06` | the retired projection (§24) |

**Projected integration.** The Step-2 sources were merged in scratch only, in the owner's landing order
(S2-A, S2-B, S2-C, S2-D; S2-E independent), by a three-way merge of each changed `.md` file against `main`.
Three paragraphs carry edits of two units and conflict at line level: M:224 and M:732 (S2-B and S2-C) and
Sub:92 (S2-B and S2-C). Each was resolved by combining both units' word-level edits, which do not overlap;
this is the combined wording the owner's landing decision (#1169 c.7057200720, "Shared lines") requires the
catch-up review to confirm. Every `old` string of the edit list was checked unique both at the base and on
this projection (`old_step2` where the text differs; §8). The projection is a planning aid, not the
manuscript the execution will edit (§9).

**S2-E head move.** S2-E moved from `8e52b217` (the head of the first draft) to `7ed84339` (the head used
here; PR #1475). The move changes no edit: on projections with either head all 258 edits are unique, and the
in-memory application leaves the same result (residual 0 unqualified, criterion-5 0, identifiers 0). The two
projections differ only in `book/ch18-beyond.md` and its FULL mirror, at lines no edit's string touches.

**Sources read.** `verification/audits/foundations/a1exit-ledger-20261120/` (LEDGER.md §2, §3, §5, §6; rows.json
correction cells of X-00, X-01, X-02, X-45, X-46, X-54, X-70, X-74, X-75; sitemap.json); each Step-2 unit's
PREREG, RESULT and amendments on its branch head; the S2-D round-1 review and the S2-C round-2 review
records.

## 2. Principles fixed in advance

**Cardinality neutrality (owner decision).**

1. No rewrite replaces a finiteness premise with an infinity premise.
2. Results that hold either way are stated without cardinality.
3. Finite-only results keep an explicit finite scope ("on a finite representative", "for a finite
   substratum", "in its finite model", "the finite OI class").
4. Finite periodic lattices and finite subsystems stay admissible under their stated conditions (S2-A's A4
   wording: $\mathbb{Z}^d$ the standard construction, a finite periodic quotient a qualified case).
5. No normalized uniform measure on an infinite space is assumed. Every law on an infinite carrier stays an
   explicit hypothesis (the S2-B/S2-C conditions are not touched).

**No self-restating scope.** "Finite in a finite representative" restates its own label (§A.33) and is not
used; a finite-only statement names its condition ("when $S$ is finite", "for a finite substratum") or the
results that use it.

**The finite OI class (owner ruling).** Structure's class stays a finite subclass, "the finite OI class";
finiteness is worded as the class's scope, never as a condition every OI-compatible substratum must meet,
and no result of the class is extended to infinite systems. A cardinality-neutral class is Issue #1478,
outside this edit.

**Identifiers (owner decision items 1, 2, 5; §A.30).** "A1" and Main ledger "(ii)" are not printed by any
replacement and are not reused or annotated. A2–A6 and Main ledger items (i), (iii)–(xiv) keep their
identifiers; ranges "A1–A6" become "A2–A6" with finiteness stated by name where the statement uses it.
Counts change with the inventory: Main's posit ledger has thirteen items, and the reconstruction's
structural assumptions are five.

**Rewrite rule by disposition (LEDGER §5).** F row: the pointer becomes the finite-only scope. J row: the
pointer becomes the weaker condition. O row: the pointer becomes the open statement, or, for X-00–X-02, is
removed with the scope it carried. A site that names no posit and already states its proved finite scope
is retained unchanged and recorded (SM:22, GR:20).

**Classes.** *Mechanical*: the replacement is the ledger's wording or the removal of a pointer whose
sentence does not use finiteness; no claim changes. *Semantic*: the sentence is reworded beyond the
pointer, its claim and scope unchanged; the reason is given. *Needs scientific review*: the rewrite fixes a
scope or relocates content whose adequacy depends on a proof dependency a reviewer must trace; the reason
names it. A site takes the highest class of its parts.

**Step-2 wording.** The return-form qualification is S2-C's accepted wording ("(NR) concerns a time that need
not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on
$\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it"). The ledger's
queued X-20 wording (unpinned update, "the only laws known") is not used anywhere in the edit list
(`grep -c 'only laws known' edits.json` = 0).

## 3. Summary

| Measure | Count |
|---|---|
| Edit records in `edits.json` | 373 (ptr 242, consistency 36, handoff 5, lean-docstring 36, repo-active 35, guard-pin 19); 371 change text, and D032, D039 retain theirs |
| Pointer sites with a drafted rewrite | 194 of 194 (140 primary sites and 54 byte-identical FULL mirrors) |
| Pointer sites by class (a FULL mirror takes its chapter's class) | 194 sites: mechanical 121, semantic 61, needs scientific review 12 |
| Consistency corrections outside the 194 sites | 21 sites: mechanical 4, semantic 17, needs scientific review 0 |
| S2-E deferrals drafted (outside the 194) | 5 sites: mechanical 3, semantic 2, needs scientific review 0 |
| Lean docstring edits (outside the 194) | 16 sites: mechanical 16, semantic 0, needs scientific review 0 |
| Other active repository files (outside the 194) | 18 sites: mechanical 18, semantic 0, needs scientific review 0 |
| Guard pins, comments and messages updated (outside the 194) | 18 sites: mechanical 18, semantic 0, needs scientific review 0 |
| Retained unchanged (names no posit; finite scope already printed) | 2 (SM:22, GR:20) |
| Edits whose `old` string lay on a line a Step-2 unit changed (pre-merge map, §8) | 22 |
| Edits whose `old` string changed between the projection and merged `main` | 3 (D224 item (ii), D232 Sub:92, D244 Sub:56; §24) |

Checker results at the drafting base and on the projection are in §10.

## 4. Item (ii): deletion and immediately necessary consistency corrections

**M:732 (posit ledger), edits D224–D228.**

- D224 deletes item (ii) whole, from "(ii) total finiteness of the bijective representative" through "listed
  in the status Remark of §1.2; ". The list then reads "(i) … countermodel; (iii) …". The identifier (ii) is
  retired; nothing marks the gap (§A.30).
- D225 removes "(item (ii))" from item (iii).
- D226 changes "Fourteen items … not fourteen" to "Thirteen items … not thirteen". The corpus-wide grep for
  a posit count (`fourteen|14 (items|posits)` over `papers/*.md`, `book/*.md`) finds only this site.
- D227 and D228 remove the two closing references to item (ii) ("the total finiteness of item (ii) and
  items (iv)–(xiv)"; "or, for item (ii), hypothesized … named at each use").
- D253 corrects the ledger's completeness sentence, which inventories "the explicit premises that the
  derivations of this paper consume": the results that use a finite representative (the recurrence step of
  §2.3, the counting measure of Lemma 3 and §4.6 among them) carry that finite scope where they are stated,
  rather than as a listed premise (review round 1, F4).

**What item (ii) carried, and where it goes (ledger X-00 (a)–(c)).**

| Content of item (ii) | After deletion |
|---|---|
| (a) the per-result weaker sufficient conditions (NR) (with S2-B's CP-indivisibility clause), (IP), (IL), each "assumed as a hypothesis of that result and not adopted", and (REV) | Moved verbatim to the status Remark M:60 (D229) |
| (b) the finite-representative list (counting measure of Lemma 3, exact return and index $L$, orbit capacity, canonical-typicality step) | Already printed at M:60 ("The finite representative is used by …", "As for the measure on a finite representative …"); not duplicated |
| (c) deep-sector clause (factor of any cardinality, normalized state or law, own dynamics) | Already printed at M:60 by S2-B; not duplicated |
| (c) transfer clause (relabelling, decoupled enlargement, change of alphabet under the alphabet-size hypothesis, proved in the companion construction) | Moved to M:60 before "Of the two finiteness statements" (D231) |
| "the extension to the whole representative is A1 of the companion substratum construction" | Deleted with A1 (Sub:92 is deleted, D232) |

**M:60 (status Remark), edits D229–D231 and D254.** D229 replaces the posit sentence by the
finite-representative scope and the moved list, with S2-C's return-form qualification for (NR) and its
law-form qualification for (IP) and (IL): after the deletion this is Main's first mention of the three
conditions (review round 1, F3). D230 replaces the P8 sentence by ledger X-00's wording; D231 inserts the
transfer clause; D254 adds "assumed as a hypothesis and not adopted" and the return-form qualification to the
later (NR) mention in M:60. The second sentence of M:60 already states that "the two axioms and the Definition leave the
cardinality of the total configuration space open"; no further neutrality sentence is added.

**Declarations of A1.** Sub:92 (D232) and ch02:76 = FULL:706 (D233–D234) delete the (A1) entries;
gloss:11 = FULL:6502 (D235–D238) replaces the A1 entry by a "Finite representative" entry at its
alphabetical place. Theorem 23 takes the finite-substratum scope at Sub:193 and ch02:118 (X-45). With the
(A1) entry gone, A4's $\mathbb{Z}^d$ standard construction is no longer excluded by the assumption list (the
S2-A review finding on ch02:74 and Sub:90); Sub:90 itself names no assumption and is unchanged.

**Counts and ranges elsewhere.** ch02:74 = FULL:704 "six properties" → "five properties" (D239–D240);
ch02:120 = FULL:750 "six structural assumptions" → "five structural assumptions on a finite substratum"
(D241–D242; ch02:74 also takes "finite candidate substrates", review F8); ch09:104 = FULL and ch09:190 = FULL
"six structural properties/axioms" → five, with finiteness worded as the finite class's scope (D255–D258); gloss:13 "The sixth of the framework's structural assumptions A1–A6" → "The structural
assumption A6 of the reconstruction theorem (A2–A6)". Every "A1–A6" / "A1-A6" range at the base is a ptr
site or GR:673 (§7 H-1) and is rewritten; no "A2–A6" range is renumbered (checker `--static`, identifier
rule: 0 findings).

## 5. Safeguard verification and review items

### 5.1 The 27 F rows stay explicitly finite-scoped

Verdicts computed from `edits.json`: a rewritten site passes when its replacement prints a finite scope, or
when the sentence does not use finiteness, or when the theorem statement it refers to carries the finite
scope (named in the cell).

| Row | Title | ptr sites | Edits here | Verdict |
|---|---|---|---|---|
| X-10 | Lemma 3 selection clause: the counting measure is the maximal-entropy invariant measure | 0 | 6 | 6 edits at 4 sites; finite scope printed in every rewritten site |
| X-12 | μ-O and μ-R (uniform law on the actual orbit / on the record-compatible orbit union), thei | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-16 | Theorem 19 reciprocity T_ij = T_θj,θi and detailed balance; Theorem 21 | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-18 | Lemma 1c(ii) pole statement; Proposition 4b continued response; Theorem 5 kinetic H-cust c | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-22 | History readback + finite recurrence theorem: exact endpoint Γ_L = I, bound s ≤ min(k, L−1 | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-24 | L-indexed form: gap below L ⇔ non-permutation Γ_s with s < L ⇔ indivisible on {0,…,L}; "be | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-25 | Routed readback "for some n"; write/store/read clauses | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-26 | All-time rooted classification and periodicity of a fixed realization; ch18 §18.7 "finite  | 3 | 5 | 5 edits at 3 sites; finite scope printed in every rewritten site |
| X-27 | Orbit capacity log₂ p; genericity count P_perm over bijections of a finite set | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-29 | Substratum Stage 1 recurrence-cycle P-indivisibility on a finite representative | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-42 | Period-lattice conditions on the printed finite class: O_h needs O_h-invariant Λ; checkerb | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-45 | Theorem 23 (reconstruction) under E1–E7 and A1–A6; its uniqueness "within the class A1–A6" | 28 | 42 | 42 edits at 32 sites; finite scope printed; no finite qualifier is added where the sentence does not use finiteness or where the theorem statement it refers to carries the finite scope: Sub:129, Sub:212, gloss:13, gloss:13 (FULL) |
| X-46 | OI-class substrata "satisfying A1–A6" (Structure Definition 9.9, Proposition 9.5 and depen | 55 | 76 | 76 edits at 59 sites; finite scope printed; no finite qualifier is added where the sentence does not use finiteness or where the theorem statement it refers to carries the finite scope: ch09:18, ch09:18 (FULL), ch09:36, ch09:36 (FULL) |
| X-48 | Classical-dimension obstruction family: no fixed finite carrier (N < ∞ ontic configuration | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-54 | Storage and memory: "S finite capacity (under A1)" | 4 | 5 | 5 edits at 4 sites; finite scope printed; no finite qualifier is added where the sentence does not use finiteness or where the theorem statement it refers to carries the finite scope: Sub:52 |
| X-55 | Computation: finite-carrier capacity comparison; "the framework's finiteness hypothesis (A | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-56 | Exact linear rule shell splitting into cycles as motivation for (EM) | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-57 | Appendix A finite sectors; Page value as exact cycle average on a finite configuration spa | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-62 | Typicality step: equilibrium macrostate ⇒ local equilibrium via canonical typicality [31] | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-64 | RETAINED-WITH-(LE) rows: the thermal "in particular" clause, the proof's division of labou | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-65 | §4.6 finite-representative parts: the O(ε) typical-set and finite-size corrections, and th | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-70 | H-count: classical horizon temperature as a counting derivative, decoupled case | 3 | 4 | 4 edits at 3 sites; finite scope printed in every rewritten site |
| X-72 | Calibration ħ = c³ε²/(4Gσ), the 1/4, ρ_s = ρ_crit, the 2/(d−1) concordance, a₀ chain | 1 | 1 | 1 edits at 1 sites; finite scope printed in every rewritten site |
| X-73 | H-BD and the boundary-only lemma (b) with gauge corollary | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-74 | Effective finiteness: E3 bounds \|C_V × C_B\| ≤ e^{S∂}; "the interpretive premise of A1" | 0 | 0 | D029 (at Sub:268, a site the map assigns to X-53) deletes "This reading is the interpretive premise of A1."; the E3 bound under H-BD stays as printed |
| X-80 | FCLASS U1 interpretive uses: cosmic topology, consciousness, Page curve, "one way to reali | 0 | 0 | no edit; printed finite-only statement unchanged |
| X-81 | Lean: kernel predicate `SubstratumInterfaceAudit.A1` (Finite Conf) and theorems stated wit | 0 | 0 | no edit; printed finite-only statement unchanged |

### 5.2 The 9 O rows

| Row | Title | ptr sites | Edits here | State after the deletion edit |
|---|---|---|---|---|
| X-00 | Main posit ledger item (ii), total finiteness of the bijective representative, and the sta | 2 | 10 | Removed: item (ii) deleted, identifier retired (D224–D228); content re-homed at M:60 (D229–D231) |
| X-01 | Pointers to the posit: item (ii), "the total-finiteness posit", "posit A1", "(ledger item  | 62 | 71 | Removed: every pointer rewritten to the scope it carries (62 ptr sites; of the 4 unit sites, Comp:120, Meth:156 and Meth:158 are drafted in §6.3 as S2-E deferrals and Meth:517 is edited by S2-E) |
| X-02 | Declarations of A1 in companion papers, book and glossary (Substratum (A1), "finite under  | 25 | 25 | Removed: every declaration rewritten or deleted (Sub:92, ch02:76 entries deleted; gloss:11 replaced) |
| X-11 | R1: physical justification of a selected law (posit (iv), μ-G; the canonical law's physica | 0 | 0 | Stays open: no edit; M:732 (iv) keeps "not derived" |
| X-21 | A physical source of a return condition for the selected update | 0 | 0 | Stays open: no edit; no manuscript asserts a physical return for the selected update |
| X-47 | Finite-L lattice numerics and the A·B extrapolation family: finite-L Monte Carlo (L = 16–6 | 0 | 0 | Stays open: no edit (owner #1468); finite-L values untouched |
| X-63 | The twelve global-phase claims: "observers exist only in the non-equilibrium phase of (S,  | 0 | 1 | Stays open/W* as S2-D prints it; only the pointer word at Sub:56 changes (D244), S2-D content kept |
| X-71 | C1 coupled shell law: existence of a normalized invariant shell law for coupled bijections | 0 | 0 | Stays open: no edit; GR:58 keeps its finite total system and negligible-coupling scope (D040 rewrites only the pointer) |
| X-82 | O-INFLOW: finiteness excludes the incoming-stream endpoint; dropping A1 admits it | 0 | 2 | Stays open as S2-D and S2-E print it; ch18:40 keeps the no-change decision except the A1 pointer (D251–D252, owner to confirm) |

### 5.3 The 9 Relabel conditions stay qualified

A Relabel row's printed qualification ("assumed as a hypothesis … not adopted" and the observability
qualification of LEDGER §3.1) must survive every edit that touches its sites. The table counts, per edit,
qualification phrases present in `old` and absent from `new`.

| Row | Condition | Edits touching its sites | Qualification phrases removed by an edit | Verdict |
|---|---|---|---|---|
| X-13 | H-ν | none | none | qualified as Step 2 prints it; no qualification removed |
| X-15 | (IP) | none | none | qualified as Step 2 prints it; no qualification removed |
| X-17 | H-μ(sp) | none | none | qualified as Step 2 prints it; no qualification removed |
| X-20 | (NR) | D004, D045, D245 | none | qualified as Step 2 prints it; no qualification removed |
| X-23 | (NR), (FS) | none | none | qualified as Step 2 prints it; no qualification removed |
| X-41 | H-μ(φ,Θ) | D035, D036, D037, D038, D160, D161, D162, D163 | none | qualified as Step 2 prints it; no qualification removed |
| X-50 | (NR) witness | none | none | qualified as Step 2 prints it; no qualification removed |
| X-60 | (IL) | none | none | qualified as Step 2 prints it; no qualification removed |
| X-61 | (IL) | none | none | qualified as Step 2 prints it; no qualification removed |

No edit removes a qualification of a surviving condition. The qualification phrases that edits do remove
belong to A1 itself ("an open hypothesis, not adopted") and leave with it. Two edits outside these rows
carry the Relabel conditions and are listed here explicitly: D224 removes (NR), (IP) and (IL) with item (ii)
(rows X-20, X-15, X-60/X-61), and D229 prints them at M:60 with "assumed as a hypothesis of that result and not
adopted", S2-C's return-form qualification for (NR) and its law-form qualification for (IP) and (IL); D254
qualifies the later (NR) mention in M:60. The (NR) clause removed with Sub:92 (D232) reappears, with its
qualification, at Sub:137 (D245).

### 5.4 Items that need scientific review

- **Substratum.md:193** (D022; row X-45): Theorem 23 takes the finite-substratum scope with the wrapping conditions on P that X-45 and X-42 require (review round 1, F1); paper and book read the same. The ledger's further instruction to state Stage 2 on Z^d where Q1 supports it goes beyond the smallest correction and is routed to §5.4 for review, with Issue #1479 as its accountable home. Review: that Stages 1 and 3 need exactly this scope (X-29, X-70, X-71).
- **Substratum.md:216** (D026; row X-45): The bullet is rewritten from a motivation of A1 to the reason for the finite scope (X-45: Stage 1 X-29, Stage 3 X-70). Review that no other stage uses finiteness.
- **ch02-substratum.md:118** (D120, mirror D121; row X-45): Book statement of Theorem 23, the same wording as Sub:193 (D022) in the book's citation style; reviewed together with it.
- **appendix-c-objections.md:102** (D198, mirror D199; row X-01): States the owner's cardinality-neutral principle in the book; review that every result named in §C.6 matches its finite or size-independent source statement.
- **appendix-c-objections.md:110** (D208, mirror D209; row X-01): The rebuttal rests on discreteness, not finiteness; review that the boundary count N that follows is stated for the horizon and not for the whole lattice.
- **appendix-c-objections.md:112** (D210, D212, mirror D211, D213; row X-01): The condensed-matter analogy is restated for discreteness; review the analogy.
- **Main.md:732** (D224, D225, D226, D227, D228, D253; row X-00): X-00: item (ii) is deleted and its identifier retired, not reused and not annotated (§A.30; owner decision items 1, 2, 5: (iii)-(xiv) keep their numbers). Its content moves to the status Remark M:60 (weaker conditions, transfer clause); the finite-representative list and the deep-sector clause are already printed there (S2-B). The count becomes thirteen, and the completeness sentence states that finite-representative results carry their scope where stated (D253; review round 1, F4). Review: the posit count and that no result loses its stated conditions.
- **Main.md:60** (D229, D230, D254, D231; row X-00): X-00: the posit sentence becomes the finite-representative scope and receives item (ii)'s weaker-condition list (with S2-B's CP clause) and its transfer clause, verbatim apart from the connective; the P8 sentence takes ledger X-00 wording. After the deletion M:60 is Main's first mention of (NR), (IP) and (IL), so S2-C's return- and law-form qualifications are printed there and at the later (NR) mention (review round 1, F3). Review: that the transfer clause is not stronger than the companion proof.
- **Stage 2 of Theorem 23 on $\mathbb{Z}^d$ (not drafted).** Ledger X-45 also asks that, where Q1
  establishes Stage 2 on $\mathbb{Z}^d$, that stage be stated there as the standard construction. That is a
  restatement of a proof stage beyond the smallest correction the deletion needs (the finite scope with the
  wrapping conditions on $P$, D022/D120); it is recorded here for review and is not part of this edit
  (review round 1, F1). Its accountable home is Issue #1479 (§A.45 rule 6).

## 6. Edit table

Generated from `edits.json`. Line numbers are base line numbers. A FULL mirror carries strings identical to
its chapter edit. `old` strings were extended within the site line where needed to be unique in the
chapter and in FULL.

### 6.1 Pointer sites (the 194 `ptr` sites of LEDGER §5)

**M:36** · row X-01 (O) · mechanical · edits D001.
Reason: Ledger X-01: the sentence is deleted; the per-result conditions are stated in the status Remark of §1.2 (M:60, D229) and at each result.

Old:

```text
 Total finiteness remains an open physical posit, not adopted, and one sufficient condition among those each result names (status Remark, §1.2 and ledger §4.5, item (ii)).
```

New:

```text
(deleted)
```

**M:44** · row X-01 (O) · mechanical · edits D002.
Reason: Ledger X-01 pointer rule.

Old:

```text
on the bijective representative of the total-finiteness posit (§1.2 Remark, §4.5 ledger) the map acts on a finite $S$
```

New:

```text
on a finite representative (§1.2 Remark) the map acts on a finite $S$
```

**M:111** · row X-01 (O) · mechanical · edits D003.
Reason: Ledger X-01 pointer rule.

Old:

```text
under the total-finiteness posit (§1.2 Remark, §4.5 ledger) the hidden sector is also finite
```

New:

```text
on a finite representative (§1.2 Remark) the hidden sector is also finite
```

**M:129** · row X-20 (J) · semantic · edits D004.
Reason: J row: the pointer becomes the weaker condition (NR), which the corollary at M:131 introduces with its S2-C qualification.

Old:

```text
the hidden space is finite under the total-finiteness posit (§1.2, §4.5).
```

New:

```text
the theorem takes the hidden space finite, as on a finite representative (§1.2 Remark), and the corollary below takes the near-return condition (NR) in its place.
```

**M:224** · row X-01 (O) · mechanical · edits D005.
Reason: Ledger X-01 pointer rule; the S2-B and S2-C insertions later in the line are untouched.

Old:

```text
with the total-finiteness posit (§1.2 Remark, §4.5) where a result also needs the hidden sector finite
```

New:

```text
with a finite representative (§1.2 Remark) where a result also needs the hidden sector finite
```

**M:268** · row X-01 (O) · mechanical · edits D006.
Reason: Ledger X-01 pointer rule (X-31: finite hidden spaces are constructed per law).

Old:

```text
$\mathcal{C}_H$ under the total-finiteness posit, §1.2, §4.5)
```

New:

```text
$\mathcal{C}_H$ on a finite representative, §1.2)
```

**M:586** · row X-01 (O) · semantic · edits D007.
Reason: Ledger X-01 (N1) wording: the finiteness belongs to the constructed realization, not to the substratum.

Old:

```text
the construction uses no property of the substratum beyond finiteness and reversibility
```

New:

```text
the construction uses no property of the constructed finite realization beyond its finiteness and reversibility
```

**M:594** · row X-01 (O) · mechanical · edits D008.
Reason: Ledger X-01 pointer rule.

Old:

```text
the concrete OI substratum, in its finite model (ledger item (ii)), supplies
```

New:

```text
the concrete OI substratum, in its finite model, supplies
```

**M:646** · row X-26 (F) · mechanical · edits D009.
Reason: F row: ledger X-01/X-26 wording, finite-only scope.

Old:

```text
(b) the physically operative form under A1: quantitative approximation
```

New:

```text
(b) the form for a finite substratum: quantitative approximation
```

**M:708** · row X-01 (O) · semantic · edits D010, D011.
Reason: Ledger X-01 wording; the deep-sector scope clause is carried by M:60 (S2-B) and the transfer clause added there (X-00).

Old (part 1):

```text
Finiteness of the hidden sector is, in the forward construction, item (ii) of the posit ledger (§4.5), an open hypothesis, not adopted, and one sufficient condition among those stated at each use, with the deep-sector scope stated there; it is not derived from Lemma 1,
```

New (part 1):

```text
Finiteness of the hidden sector is not assumed in the forward construction: results that use a finite hidden sector are statements about finite representatives, each naming the hypotheses it consumes; it is not derived from Lemma 1,
```

Old (part 2):

```text
compatible with the finiteness hypothesized here and are not premises of it.
```

New (part 2):

```text
compatible with finite representatives and are not premises of them.
```

**M:726** · row X-01 (O) · semantic · edits D012.
Reason: Ledger X-01 ("finite in the finite representative, which is not asserted of nature"), written in the cardinality-neutral form of the owner decision.

Old:

```text
a deterministic bijection on a set, finite under the total-finiteness posit (§1.2 Remark, §4.5 ledger item (ii)), an open hypothesis, not adopted, and one sufficient condition among those stated at each use.
```

New:

```text
a deterministic bijection on a set whose cardinality is left open; results that need a finite set are stated for a finite representative (§1.2 Remark).
```

**Sub:44** · row X-54 (F) · semantic · edits D013, D014.
Reason: F row X-54: finite-only scope stated as a condition on $S$ (review round 1, F6: the ledger wording "in a finite representative" restated its own label).

Old (part 1):

```text
*finite capacity* (under A1).
```

New (part 1):

```text
*finite capacity* when $S$ is finite.
```

Old (part 2):

```text
a lossless memory, finite under A1.
```

New (part 2):

```text
a lossless memory, of finite capacity when $S$ is finite.
```

**Sub:52** · row X-54 (F) · mechanical · edits D015.
Reason: X-02 rule: the parenthesis is deleted; the next sentence states where finiteness of the total carrier is used.

Old:

```text
the OI configuration (finite under A1)
```

New:

```text
the OI configuration
```

**Sub:104** · row X-45 (F) · semantic · edits D016, D017, D018.
Reason: F row X-45: Theorem 23 is a statement about finite substrata satisfying A2–A6; no identifier is renumbered.

Old (part 1):

```text
holds under E1–E7 **and** A1–A6 jointly
```

New (part 1):

```text
holds for a finite substratum under E1–E7 **and** A2–A6 jointly
```

Old (part 2):

```text
The set A1–A6, with that premise,
```

New (part 2):

```text
The set A2–A6, with that premise and the finite scope,
```

Old (part 3):

```text
sufficiency of A1–A6 and E1–E7
```

New (part 3):

```text
sufficiency of A2–A6 and E1–E7 on a finite substratum
```

**Sub:123** · row X-45 (F) · semantic · edits D019.
Reason: F row X-45: the Stage 1 input becomes the theorem's finite scope.

Old:

```text
A1 (finiteness), A2 (determinism)
```

New:

```text
finiteness of $S$ (the scope of Theorem 23), A2 (determinism)
```

**Sub:129** · row X-45 (F) · mechanical · edits D020.
Reason: A1 is dropped without a replacement scope (review round 1, F2): C4 comes from the hidden-memory theorem and C1 from the accessible history gap, and the readback route constructs a finite hidden space rather than assuming one (M:60, "a finite hidden space is constructed, not assumed"); the recurrence-cycle P-indivisibility, which does use a finite representative, is scoped separately at Sub:137 (D245).

Old:

```text
derived from E1–E3, A1–A2 together with **M1-T**
```

New:

```text
derived from E1–E3 and A2 together with **M1-T**
```

**Sub:133** · row X-45 (F) · mechanical · edits D021.
Reason: Range rewrite; no claim changes.

Old:

```text
not a consequence of A1–A6 or of the nearest-neighbor wave equation
```

New:

```text
not a consequence of finiteness, of A2–A6 or of the nearest-neighbor wave equation
```

**Sub:193** · row X-45 (F) · needs scientific review · edits D022.
Reason: Theorem 23 takes the finite-substratum scope with the wrapping conditions on P that X-45 and X-42 require (review round 1, F1); paper and book read the same. The ledger's further instruction to state Stage 2 on Z^d where Q1 supports it goes beyond the smallest correction and is routed to §5.4 for review, with Issue #1479 as its accountable home. Review: that Stages 1 and 3 need exactly this scope (X-29, X-70, X-71).

Old:

```text
*Let E1–E7, M1-T, M1-B, A1–A6, the Stage-2
```

New:

```text
*Let $(S,\varphi)$ be a finite substratum, with A4 applying in its finite periodic case under the wrapping conditions on $P$ of Stage 2 [SM §4.1], and let E1–E7, M1-T, M1-B, A2–A6, the Stage-2
```

**Sub:205** · row X-45 (F) · mechanical · edits D023.
Reason: Range rewrite with the theorem's scope.

Old:

```text
The structural assumptions A1–A6 exclude several broad classes
```

New:

```text
The finite-substratum scope and the structural assumptions A2–A6 exclude several broad classes
```

**Sub:207** · row X-45 (F) · mechanical · edits D024.
Reason: Ledger X-45 rule "(violating A1)" -> "(outside the finite class)".

Old:

```text
- Intrinsically continuum theories (violate A1)
```

New:

```text
- Intrinsically continuum theories (outside the finite-substratum scope)
```

**Sub:212** · row X-45 (F) · semantic · edits D025.
Reason: Finiteness is a scope, not a defended assumption (owner decision: cardinality neutrality).

Old:

```text
The framework's defense of A1–A6 (in [SM §2]
```

New:

```text
The framework's defense of A2–A6 (in [SM §2]
```

**Sub:216** · row X-45 (F) · needs scientific review · edits D026.
Reason: The bullet is rewritten from a motivation of A1 to the reason for the finite scope (X-45: Stage 1 X-29, Stage 3 X-70). Review that no other stage uses finiteness.

Old:

```text
- A1 (finiteness) is motivated by E3, which does not establish it (A1 above); alternative would be an effective-finiteness argument with continuum UV completion, which the framework does not develop.
```

New:

```text
- The finite-substratum scope of Theorem 23 is used by Stage 1's exact return and Stage 3's count; E3 does not establish finiteness of $S$, and a form of those stages for a substratum of unspecified cardinality, or an effective-finiteness argument with continuum UV completion, is not developed.
```

**Sub:223** · row X-45 (F) · mechanical · edits D027.
Reason: Range rewrite with the theorem's scope.

Old:

```text
E1–E7 + A1–A6 is a consistent set
```

New:

```text
E1–E7 + A2–A6 on a finite substratum is a consistent set
```

**Sub:233** · row X-45 (F) · mechanical · edits D028.
Reason: Range rewrite with the theorem's scope.

Old:

```text
\text{Structural assumptions (A1–A6)}
```

New:

```text
\text{Finite substratum, structural assumptions (A2–A6)}
```

**Sub:268** · row X-53 (J) · mechanical · edits D029.
Reason: Ledger X-74: the sentence is deleted; the E3 bound under H-BD survives as stated.

Old:

```text
 This reading is the interpretive premise of A1.
```

New:

```text
(deleted)
```

**Sub:288** · row X-02 (O) · mechanical · edits D030.
Reason: X-02 rule: the parenthesis is deleted where finiteness is not used.

Old:

```text
$S$ is a set (finite under A1) with no complex structure
```

New:

```text
$S$ is a set with no complex structure
```

**Sub:389** · row X-02 (O) · mechanical · edits D031.
Reason: X-02 rule: the parenthesis is deleted where finiteness is not used.

Old:

```text
a set (finite under A1) with a deterministic bijection
```

New:

```text
a set with a deterministic bijection
```

**SM:22** · row X-01 (O) · mechanical · edits D032.
Reason: Retained unchanged: the site names no posit and states Main's result on a finite configuration space, its proved scope.

Old:

```text
an observer embedded in a deterministic bijection on a finite configuration space,
```

New:

```text
an observer embedded in a deterministic bijection on a finite configuration space,
```

**SM:30** · row X-02 (O) · mechanical · edits D033.
Reason: X-02 rule.

Old:

```text
uses a set (finite under A1) with a deterministic bijection of bounded coupling degree
```

New:

```text
uses a set with a deterministic bijection of bounded coupling degree
```

**SM:60** · row X-02 (O) · mechanical · edits D034.
Reason: X-02 rule.

Old:

```text
specifies a set S, finite under A1, a bijection
```

New:

```text
specifies a set S, a bijection
```

**SM:158** · row X-41 (J) · mechanical · edits D035.
Reason: J row X-41: no finiteness is used in the sentence.

Old:

```text
a single bijection on the phase space, finite under A1.
```

New:

```text
a single bijection on the phase space.
```

**SM:222** · row X-41 (J) · semantic · edits D036.
Reason: J row X-41: A4 on the lattice as the standard construction, the finite quotient a qualified case (owner A4 decision); consistent with S2-A's wording that follows.

Old:

```text
(under A1 and A4 [Substratum §3.1] it acts on configurations over a finite periodic quotient
```

New:

```text
(under A4 [Substratum §3.1] it acts on configurations over $\Lambda$ or, as a qualified case, over a finite periodic quotient
```

**SM:232** · row X-41 (J) · semantic · edits D037.
Reason: The next clause cites [Main §3.2] for finite permutations; the finite scope is kept explicit.

Old:

```text
The fundamental object is the bijection $\varphi$, finite under A1;
```

New:

```text
The fundamental object is the bijection $\varphi$, a finite permutation on a finite representative;
```

**SM:316** · row X-41 (J) · mechanical · edits D038.
Reason: X-02 rule.

Old:

```text
the fundamental bijection (finite under A1) without
```

New:

```text
the fundamental bijection without
```

**GR:20** · row X-01 (O) · mechanical · edits D039.
Reason: Retained unchanged: names no posit; Main's result on a finite configuration space at its proved scope.

Old:

```text
an observer embedded in a deterministic bijection on a finite configuration space,
```

New:

```text
an observer embedded in a deterministic bijection on a finite configuration space,
```

**GR:58** · row X-70 (F) · mechanical · edits D040, D041.
Reason: Ledger X-70 wording.

Old (part 1):

```text
Under A1, restrict the finite total system to
```

New (part 1):

```text
For a finite total system, restrict it to
```

Old (part 2):

```text
that the total system is finite (A1) and
```

New (part 2):

```text
that the total system is finite and
```

**GR:88** · row X-72 (F) · mechanical · edits D042.
Reason: F row: X-70 pointer rewrite carried to the calibration.

Old:

```text
requires H-count, including A1 and the conserved energy shell
```

New:

```text
requires H-count, including finiteness of the total system and the conserved energy shell
```

**GR:257** · row X-01 (O) · mechanical · edits D043.
Reason: Ledger X-75 wording.

Old:

```text
The concrete OI substratum under A1 — finite states
```

New:

```text
The concrete OI substratum in its finite model — finite states
```

**GR:261** · row X-01 (O) · mechanical · edits D044.
Reason: Range rewrite; the claim is unchanged.

Old:

```text
The controllability resource is not entailed by A1–A6;
```

New:

```text
The controllability resource is not entailed by finiteness or by A2–A6;
```

**GR:589** · row X-20 (J) · mechanical · edits D045.
Reason: J row X-20: the weaker condition (NR) is already named in the same sentence with its S2-C qualification.

Old:

```text
uses total finiteness ([Main §4.5], posit (ii)) via the recurrence argument
```

New:

```text
uses a finite representative ([Main §1.2]) via the recurrence argument
```

**Str:80** · row X-46 (F) · mechanical · edits D046, D047, D048.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
OI's structural conditions A1 (finiteness), A2 (deterministic bijection)
```

New (part 1):

```text
the finite OI class's structural conditions finiteness, A2 (deterministic bijection)
```

Old (part 2):

```text
*Pre-condition 3: A1-A6 compatibility under matrix-model bridge.*
```

New (part 2):

```text
*Pre-condition 3: compatibility with finiteness and A2-A6 under matrix-model bridge.*
```

Old (part 3):

```text
Whether matrix models satisfy A1-A6 is not obvious
```

New (part 3):

```text
Whether matrix models satisfy finiteness and A2-A6 is not obvious
```

**Str:86** · row X-46 (F) · mechanical · edits D049.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
substrata satisfying A1-A6; exhaustive
```

New:

```text
finite substrata satisfying A2-A6; exhaustive
```

**Str:134** · row X-46 (F) · mechanical · edits D050.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
by adding structural conditions A1–A6 [Substratum §3]:
```

New:

```text
by restricting to finite substrata and adding structural conditions A2–A6 [Substratum §3]:
```

**Str:136** · row X-46 (F) · mechanical · edits D051.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers. The retired identifier is not printed.

Old:

```text
(A1) Finiteness; (A2) Determinism
```

New:

```text
Finiteness of $S$; (A2) Determinism
```

**Str:140** · row X-46 (F) · mechanical · edits D052, D053, D054.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
A1–A6 are not the same as observer-admission C1–C4;
```

New (part 1):

```text
Finiteness and A2–A6 are not the same as observer-admission C1–C4;
```

Old (part 2):

```text
; A1–A6 are conditions for membership in *OI's specific* universality class
```

New (part 2):

```text
; finiteness and A2–A6 are conditions for membership in the finite OI class, the finite subclass of *OI's specific* universality class
```

Old (part 3):

```text
Some relations: A1 (finiteness) is related to but distinct from C3
```

New (part 3):

```text
Some relations: finiteness is related to but distinct from C3
```

**Str:196** · row X-46 (F) · mechanical · edits D055.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
plus A1–A6 + E1–E7
```

New:

```text
plus finiteness, A2–A6 + E1–E7
```

**Str:206** · row X-46 (F) · mechanical · edits D056.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
satisfying A1-A6 (which §6 establishes
```

New:

```text
satisfying finiteness and A2-A6 (which §6 establishes
```

**Str:224** · row X-46 (F) · mechanical · edits D057.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
in the sense of OI's structural condition A1, $|S| < \infty$.
```

New:

```text
in the sense of the finiteness condition $|S| < \infty$ of the finite OI class.
```

**Str:230** · row X-46 (F) · mechanical · edits D058.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
A1 would hold for a separately specified representation
```

New:

```text
finiteness would hold for a separately specified representation
```

**Str:256** · row X-46 (F) · mechanical · edits D059.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
## 6. Structural compatibility: A1–A6 under matrix-model bridges
```

New:

```text
## 6. Structural compatibility: finiteness and A2–A6 under matrix-model bridges
```

**Str:258** · row X-46 (F) · semantic · edits D060.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers. Finiteness is worded as scope, not a membership condition (review round 1, F8).

Old:

```text
OI's structural conditions A1–A6.
```

New:

```text
OI's structural conditions A2–A6, within the finite scope of the reconstruction theorem.
```

**Str:260** · row X-46 (F) · semantic · edits D061, D062.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
are: A1 (finiteness), A2 (determinism / bijection),
```

New (part 1):

```text
are: A2 (determinism / bijection),
```

Old (part 2):

```text
A6 (background independence). They are assumptions
```

New (part 2):

```text
A6 (background independence); the reconstruction theorem is stated for a finite $S$. They are assumptions
```

**Str:264** · row X-46 (F) · mechanical · edits D063.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers. Section number unchanged.

Old:

```text
### 6.1 A1 (finiteness)
```

New:

```text
### 6.1 Finiteness
```

**Str:270** · row X-46 (F) · mechanical · edits D064.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
Achieving A1 would require
```

New:

```text
Achieving finiteness would require
```

**Str:272** · row X-46 (F) · mechanical · edits D065.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
**Status.** A1 fails for continuum BFSS
```

New:

```text
**Status.** Finiteness fails for continuum BFSS
```

**Str:314** · row X-46 (F) · mechanical · edits D066.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
### 6.7 Summary of A1–A6 status
```

New:

```text
### 6.7 Summary of the status of finiteness and A2–A6
```

**Str:316** · row X-46 (F) · mechanical · edits D067.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
The tally across A1–A6:
```

New:

```text
The tally across finiteness and A2–A6:
```

**Str:320** · row X-46 (F) · mechanical · edits D068.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
| A1 (finiteness) |
```

New:

```text
| Finiteness |
```

**Str:327** · row X-46 (F) · mechanical · edits D069.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
A1 fails without a separate finite-value regulator.
```

New:

```text
Finiteness fails without a separate finite-value regulator.
```

**Str:331** · row X-46 (F) · mechanical · edits D070.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
they must satisfy the same A1–A6 that OI's reconstruction requires
```

New:

```text
they must satisfy the same finiteness and A2–A6 that OI's reconstruction requires
```

**Str:339** · row X-46 (F) · mechanical · edits D071.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
independent investigation of A1–A6 compatibility
```

New:

```text
independent investigation of compatibility with finiteness and A2–A6
```

**Str:351** · row X-46 (F) · mechanical · edits D072.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
do not satisfy OI's structural conditions A1–A6 in their standard formulation. The failures
```

New:

```text
do not satisfy the conditions of the finite OI class (finiteness and A2–A6) in their standard formulation. The failures
```

**Str:359** · row X-46 (F) · mechanical · edits D073.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
do not satisfy OI's structural conditions A1–A6 in their standard formulation, with the failures
```

New:

```text
do not satisfy the conditions of the finite OI class (finiteness and A2–A6) in their standard formulation, with the failures
```

**Str:375** · row X-46 (F) · mechanical · edits D074.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
among substrata satisfying OI's A1–A6, which
```

New:

```text
among finite substrata satisfying OI's A2–A6, which
```

**Str:560** · row X-46 (F) · mechanical · edits D075.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
supplies structural conditions A1–A6 for its local reconstruction
```

New:

```text
supplies structural conditions A2–A6, with a finite scope, for its local reconstruction
```

**Str:646** · row X-46 (F) · semantic · edits D076.
Reason: Ledger X-46 deletion wording, with the internal audit reference replaced by the manuscript reference [Substratum §3.1] (§A.27 manuscript voice).

Old:

```text
be OI-class substrata (satisfying A1-A6)
```

New:

```text
be finite OI-class substrata (finite substrata satisfying A2-A6, with A4 in its finite periodic case [Substratum §3.1])
```

**Str:701** · row X-46 (F) · mechanical · edits D077.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
structural conditions such as A1–A6.
```

New:

```text
structural conditions such as finiteness and A2–A6.
```

**Str:730** · row X-02 (O) · mechanical · edits D078.
Reason: X-02 rule.

Old:

```text
(sets with bijections, finite under A1)
```

New:

```text
(sets with bijections)
```

**Str:732** · row X-02 (O) · mechanical · edits D079.
Reason: X-02 rule.

Old:

```text
under A1 they have all the formal features of permutations on finite sets
```

New:

```text
in a finite representative they have all the formal features of permutations on finite sets
```

**Str:746** · row X-46 (F) · mechanical · edits D080.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
all three fail OI's A1–A6 (so are outside OI's specific class)
```

New:

```text
all three fail the conditions of the finite OI class, finiteness and A2–A6 (so are outside it)
```

**Str:768** · row X-45 (F) · mechanical · edits D081.
Reason: F row X-45: range rewrite.

Old:

```text
plus A1-A6 and the nearest-neighbour range
```

New:

```text
plus finiteness, A2-A6 and the nearest-neighbour range
```

**Str:866** · row X-46 (F) · mechanical · edits D082.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
The structural conditions A1-A6 are then
```

New:

```text
The structural conditions (finiteness and A2-A6) are then
```

**Str:1006** · row X-46 (F) · mechanical · edits D083.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
The per-condition A1–A6 analysis applied
```

New:

```text
The per-condition analysis (finiteness and A2–A6) applied
```

**Str:1008** · row X-46 (F) · mechanical · edits D084, D085, D086.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
Per-condition: A1 (finiteness) **fails** in the full theory
```

New (part 1):

```text
Per-condition: finiteness **fails** in the full theory
```

Old (part 2):

```text
Net: A1 and A2 fail;
```

New (part 2):

```text
Net: finiteness and A2 fail;
```

Old (part 3):

```text
mismatches at A1 and A2 being deeper
```

New (part 3):

```text
mismatches at finiteness and A2 being deeper
```

**Str:1010** · row X-46 (F) · mechanical · edits D087, D088.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
Per-condition: A1 (finiteness) **holds at any finite stage**
```

New (part 1):

```text
Per-condition: finiteness **holds at any finite stage**
```

Old (part 2):

```text
A1 fails in the limit,
```

New (part 2):

```text
finiteness fails in the limit,
```

**Str:1012** · row X-46 (F) · mechanical · edits D089, D090.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
Per-condition: A1 (finiteness) **fails** — continuum QFT.
```

New (part 1):

```text
Per-condition: finiteness **fails** — continuum QFT.
```

Old (part 2):

```text
A2, A5, A1 fail;
```

New (part 2):

```text
A2, A5 and finiteness fail;
```

**Str:1014** · row X-46 (F) · mechanical · edits D091, D092.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
All three fail A1 (finiteness) in their standard formulation
```

New (part 1):

```text
All three fail finiteness in their standard formulation
```

Old (part 2):

```text
in OI's specific universality class as that class is delimited by A1–A6.
```

New (part 2):

```text
in the finite OI class, delimited by finiteness and A2–A6.
```

**Str:1016** · row X-46 (F) · semantic · edits D093.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
are in OI's specific universality class (per A1–A6 failure)
```

New:

```text
are in the finite OI class (per failure of its conditions, finiteness and A2–A6)
```

**Str:1030** · row X-46 (F) · mechanical · edits D094.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
the OI–A1–A6 class narrower
```

New:

```text
the finite OI class (A2–A6) narrower
```

**Str:1066** · row X-46 (F) · mechanical · edits D095.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
all four fail OI's A1–A6 and are therefore outside OI's specific class
```

New:

```text
all four fail the conditions of the finite OI class, finiteness and A2–A6, and are therefore outside it
```

**Str:1237** · row X-46 (F) · mechanical · edits D096, D097.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
per-condition A1–A6 analysis b
```

New (part 1):

```text
per-condition analysis (finiteness and A2–A6) b
```

Old (part 2):

```text
from A1, A3, A4, A6 plus the SM target
```

New (part 2):

```text
from finiteness, A3, A4, A6 plus the SM target
```

**Str:1303** · row X-46 (F) · mechanical · edits D098.
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
**Per-condition A1–A6 audit for LQG
```

New:

```text
**Per-condition audit (finiteness and A2–A6) for LQG
```

**README:100** · row X-01 (O) · mechanical · edits D099.
Reason: Ledger X-01 B1 rule.

Old:

```text
finiteness posit defense;
```

New:

```text
the finite-representative scope;
```

**readers:79** · row X-01 (O) · mechanical · edits D100. Mirror: FULL:167, identical strings (D101).
Reason: Ledger X-01 B1 rule.

Old:

```text
the finiteness posit,
```

New:

```text
the finite-representative scope,
```

**ch00:95** · row X-01 (O) · semantic · edits D102. Mirror: FULL:320, identical strings (D103).
Reason: X-01 pointer rule; the posit sentence becomes the finite-representative scope.

Old:

```text
Chapter 2 uses a finite bijective representative $(S,\varphi)$ under A1, which remains open as a physical posit, not adopted, and is one sufficient condition among those the results name.
```

New:

```text
Chapter 2 uses a finite bijective representative $(S,\varphi)$ for the results stated on it, each of which names the conditions it uses.
```

**ch01:28** · row X-01 (O) · mechanical · edits D104. Mirror: FULL:361, identical strings (D105).
Reason: X-01 pointer rule (mirror of M:44).

Old:

```text
on the bijective representative of the finiteness posit A1 (Chapter 2 §2.4) the map acts on a finite system
```

New:

```text
on a finite bijective representative (Chapter 2 §2.4) the map acts on a finite system
```

**ch01:163** · row X-01 (O) · mechanical · edits D106. Mirror: FULL:496, identical strings (D107).
Reason: X-01 pointer rule (mirror of M:594).

Old:

```text
the concrete OI substratum, in its finite model (ledger item (ii)), supplies the structural architecture — closure under composition and coarse-graining, stability under an uncoupled spectator, relabelling invariance, reversibility, the exchanges of distinguishable states, and, as a stated intervention principle rather than a consequence of its finite states and bijective dynamics, the phases — but, under finite bijective read-write dynamics,
```

New:

```text
the concrete OI substratum, in its finite model, supplies the structural architecture — closure under composition and coarse-graining, stability under an uncoupled spectator, relabelling invariance, reversibility, the exchanges of distinguishable states, and, as a stated intervention principle rather than a consequence of its finite states and bijective dynamics, the phases — but, under finite bijective read-write dynamics,
```

**ch01:179** · row X-26 (F) · semantic · edits D108, D110. Mirror: FULL:512, identical strings (D109, D111).
Reason: F row X-26: the recurrence clause keeps its finite scope; the (NR) sentence and its S2-C qualification are untouched.

Old (part 1):

```text
Without A1, the near-return condition
```

New (part 1):

```text
Without finiteness of the representative, the near-return condition
```

Old (part 2):

```text
Under A1 the physical representative is finite and reversible, so it also recurs:
```

New (part 2):

```text
A finite reversible representative also recurs:
```

**ch02:8** · row X-02 (O) · mechanical · edits D112. Mirror: FULL:638, identical strings (D113).
Reason: X-02 rule.

Old:

```text
the reversible object $(S,\varphi)$, finite under A1, whose
```

New:

```text
the reversible object $(S,\varphi)$ whose
```

**ch02:16** · row X-54 (F) · semantic · edits D114. Mirror: FULL:646, identical strings (D115).
Reason: F row X-54: finite scope kept; the owner's configuration-space sentence opens the triple in place of D114's own neutrality wording, so the book has one wording (owner decision #1169 c.7058783437, book mirrors; review round 5).

Old:

```text
The framework's central object is a triple. $S$ is the set of total configurations, finite in the representative specified under the open hypothesis A1 (§2.4).
```

New:

```text
The framework's central object is a triple.

**Configuration space.** The substratum has a configuration space $S$. No restriction is imposed on its cardinality; $S$ may be finite or infinite. $S$ is the set of total configurations; the results stated for a finite substratum take it finite.
```

**ch02:88** · row X-45 (F) · mechanical · edits D116. Mirror: FULL:718, identical strings (D117).
Reason: F row X-45.

Old:

```text
under E1–E7 and A1–A6 with M1-T
```

New:

```text
for a finite substratum under E1–E7 and A2–A6 with M1-T
```

**ch02:90** · row X-45 (F) · mechanical · edits D118. Mirror: FULL:720, identical strings (D119).
Reason: F row X-45.

Old:

```text
the finiteness and determinism assumptions A1, A2,
```

New:

```text
the finite-substratum scope and the determinism assumption A2,
```

**ch02:118** · row X-45 (F) · needs scientific review · edits D120. Mirror: FULL:748, identical strings (D121).
Reason: Book statement of Theorem 23, the same wording as Sub:193 (D022) in the book's citation style; reviewed together with it.

Old:

```text
*Let E1–E7, M1-T and M1-B, and A1–A6 hold,
```

New:

```text
*Let $(S,\varphi)$ be a finite substratum, with A4 applying in its finite periodic case under the wrapping conditions on $P$ of Stage 2 (SM §4.1), and let E1–E7, M1-T and M1-B, and A2–A6 hold,
```

**ch02:122** · row X-45 (F) · mechanical · edits D122, D124, D126. Mirror: FULL:752, identical strings (D123, D125, D127).
Reason: Ledger X-45 wording.

Old (part 1):

```text
uniqueness is within the structural class A1–A6 with the nearest-neighbor restriction
```

New (part 1):

```text
uniqueness is within the class of finite substrata satisfying A2–A6, with the nearest-neighbor restriction
```

Old (part 2):

```text
(violating A1)
```

New (part 2):

```text
(outside the finite class)
```

Old (part 3):

```text
The framework's defense of A1–A6 is t
```

New (part 3):

```text
The framework's defense of A2–A6 is t
```

**ch02:136** · row X-02 (O) · mechanical · edits D128. Mirror: FULL:766, identical strings (D129).
Reason: X-02 rule.

Old:

```text
the substratum is a set (finite under A1) with a bijection on it. $\mathcal{G}
```

New:

```text
the substratum is a set with a bijection on it. $\mathcal{G}
```

**ch02:158** · row X-02 (O) · mechanical · edits D130. Mirror: FULL:788, identical strings (D131).
Reason: X-02 rule.

Old:

```text
$S$ is a set (finite under A1) with no complex structure
```

New:

```text
$S$ is a set with no complex structure
```

**ch02:212** · row X-02 (O) · mechanical · edits D132. Mirror: FULL:842, identical strings (D133).
Reason: X-02 rule.

Old:

```text
a set (finite under A1) with a deterministic bijection on it
```

New:

```text
a set with a deterministic bijection on it
```

**ch03:34** · row X-46 (F) · mechanical · edits D134. Mirror: FULL:895, identical strings (D135).
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old:

```text
substrata satisfying A1–A6 of the reconstruction theorem
```

New:

```text
finite substrata satisfying A2–A6 of the reconstruction theorem
```

**ch03:44** · row X-46 (F) · semantic · edits D136, D138, D140. Mirror: FULL:905, identical strings (D137, D139, D141).
Reason: F row X-46: the class stays the finite OI class, a finite subclass (owner ruling #1169 c.7057674976; the cardinality-neutral class is Issue #1478); "A1" is replaced by "finiteness" as the class scope, A2–A6 keep their identifiers.

Old (part 1):

```text
The structural conditions A1–A6 that define Level D
```

New (part 1):

```text
The finite scope and the structural conditions A2–A6 that define Level D
```

Old (part 2):

```text
; A1–A6 are conditions for membership in OI's *specific* universality class
```

New (part 2):

```text
; finiteness and A2–A6 are conditions for membership in the finite OI class, the finite subclass of OI's *specific* universality class
```

Old (part 3):

```text
Some A's relate to but are distinct from C's: A1 posits finiteness of the total configuration space and remains open as a physical premise.
```

New (part 3):

```text
Some of these conditions relate to but are distinct from C's: finiteness of the total configuration space is the scope of the finite class and is not asserted of nature.
```

**ch03:84** · row X-02 (O) · mechanical · edits D142. Mirror: FULL:945, identical strings (D143).
Reason: X-02 rule.

Old:

```text
the substratum is a set (finite under A1) with a bijection on it, governed
```

New:

```text
the substratum is a set with a bijection on it, governed
```

**ch03:226** · row X-01 (O) · semantic · edits D144. Mirror: FULL:1087, identical strings (D145).
Reason: Ledger X-01 B1 rule ("finiteness posit" -> finite-representative scope).

Old:

```text
Recurrence, finiteness and the other assumptions retain the statuses given in the technical sources [Main §3.1, §4.5].
```

New:

```text
Recurrence and the other assumptions retain the statuses given in the technical sources [Main §3.1, §4.5], and results that use a finite representative are stated for finite representatives.
```

**ch04:10** · row X-45 (F) · mechanical · edits D146. Mirror: FULL:1114, identical strings (D147).
Reason: F row X-45.

Old:

```text
including the structural assumptions A1–A6, site factorization
```

New:

```text
including the structural assumptions A2–A6 with the finite-substratum scope of the reconstruction theorem, site factorization
```

**ch04:26** · row X-45 (F) · semantic · edits D148, D150, D152. Mirror: FULL:1130, identical strings (D149, D151, D153).
Reason: F row X-45; the motivation of A1 is removed with the identifier (owner decision items 1, 3).

Old (part 1):

```text
The structural assumptions A1–A6 identified in Chapter 2's reconstruction theorem (finiteness, determinism, bounded coupling, center independence, linearity, background independence) are not derivable
```

New (part 1):

```text
The structural assumptions A2–A6 identified in Chapter 2's reconstruction theorem (determinism, bounded coupling, center independence, linearity, background independence), with its finite-substratum scope, are not derivable
```

Old (part 2):

```text
the class defined by A1–A6 and the nearest-neighbor restriction
```

New (part 2):

```text
the class of finite substrata defined by A2–A6 and the nearest-neighbor restriction
```

Old (part 3):

```text
The framework's defense of A1–A6 is an argument from the empirical inputs of physics, not a derivation from the foundational premise — A1 is motivated by the holographic entropy bound, A2 by
```

New (part 3):

```text
The framework's defense of A2–A6 is an argument from the empirical inputs of physics, not a derivation from the foundational premise — A2 by
```

**ch05:15** · row X-02 (O) · mechanical · edits D154. Mirror: FULL:1330, identical strings (D155).
Reason: X-02 rule.

Old:

```text
a set (finite under the open hypothesis A1) with a deterministic bijection
```

New:

```text
a set with a deterministic bijection
```

**ch05:19** · row X-45 (F) · mechanical · edits D156. Mirror: FULL:1334, identical strings (D157).
Reason: F row X-45.

Old:

```text
provides the structural assumptions A1–A6 and the stated
```

New:

```text
provides the finite-substratum scope, the structural assumptions A2–A6 and the stated
```

**ch05:23** · row X-02 (O) · mechanical · edits D158. Mirror: FULL:1338, identical strings (D159).
Reason: X-02 rule.

Old:

```text
a set $S$ (finite under the open hypothesis A1, Chapter 2 §2.4), a deterministic
```

New:

```text
a set $S$, a deterministic
```

**ch05:83** · row X-41 (J) · mechanical · edits D160. Mirror: FULL:1398, identical strings (D161).
Reason: X-02 rule (J row X-41).

Old:

```text
the substratum bijection (finite under A1) is governed
```

New:

```text
the substratum bijection is governed
```

**ch05:89** · row X-41 (J) · mechanical · edits D162. Mirror: FULL:1404, identical strings (D163).
Reason: X-02 rule (J row X-41).

Old:

```text
not the fundamental bijection (finite under A1) itself
```

New:

```text
not the fundamental bijection itself
```

**ch07:42** · row X-70 (F) · mechanical · edits D164. Mirror: FULL:1907, identical strings (D165).
Reason: Ledger X-70 wording.

Old:

```text
Under H-count the total system is finite (A1), and
```

New:

```text
Under H-count the total system is finite, and
```

**ch07:118** · row X-02 (O) · mechanical · edits D166. Mirror: FULL:1983, identical strings (D167).
Reason: X-02 rule.

Old:

```text
acting on a configuration space $S$, finite under A1.
```

New:

```text
acting on a configuration space $S$.
```

**ch09:18** · row X-46 (F) · mechanical · edits D168. Mirror: FULL:2433, identical strings (D169).
Reason: X-02 rule.

Old:

```text
a deterministic bijection (finite under A1) are not equivalent
```

New:

```text
a deterministic bijection are not equivalent
```

**ch09:36** · row X-46 (F) · mechanical · edits D170. Mirror: FULL:2451, identical strings (D171).
Reason: X-01/X-02 rule: the posit is removed from the level list.

Old:

```text
(deterministic bijection, classical probability, causal partition) with the open hypothesis A1 (finite substratum).
```

New:

```text
(deterministic bijection, classical probability, causal partition).
```

**ch09:106** · row X-46 (F) · semantic · edits D172. Mirror: FULL:2521, identical strings (D173).
Reason: F scope; cardinality-neutral wording.

Old:

```text
*Finiteness.* The substratum $S$ has finite cardinality — as a claim about nature, the open hypothesis A1, not adopted. This is load-bearing
```

New:

```text
*Finiteness.* Finite cardinality of $S$ is used by the results stated for a finite representative and is not asserted of nature. It is load-bearing
```

**ch09:182** · row X-46 (F) · semantic · edits D174. Mirror: FULL:2597, identical strings (D175).
Reason: Cardinality-neutral description of the programme.

Old:

```text
The framework is a finite deterministic-substratum program: it takes, under the open hypothesis A1, a finite configuration space with a deterministic bijection,
```

New:

```text
The framework is a deterministic-substratum program: it takes a configuration space with a deterministic bijection, finite in the representatives on which its finite-only results are stated,
```

**ch09:188** · row X-46 (F) · semantic · edits D176. Mirror: FULL:2603, identical strings (D177).
Reason: X-02 rule; the matrix-model comparison that follows uses finite dimension.

Old:

```text
acts on a configuration space finite under A1, with
```

New:

```text
acts on a configuration space, finite where the framework's finite-only results apply, with
```

**ch09:192** · row X-46 (F) · semantic · edits D178, D180, D359. Mirror: FULL:2607, identical strings (D179, D181, D360).
Reason: F row; the paraphrase of the posit is replaced by the cardinality-neutral statement.

Old (part 1):

```text
*A1 (finiteness).* The framework's representative has finite $|S|$.
```

New (part 1):

```text
*Finiteness.* The framework's finite-only results use a representative with finite $|S|$.
```

Old (part 2):

```text
Total configuration finiteness remains an open physical hypothesis (Chapter 2).
```

New (part 2):

```text
The cardinality of the total configuration space is left open.
```

Old (part 3):

```text
Matrix models with $N \to \infty$ limits violate this strictly
```

New (part 3):

```text
Matrix models with $N \to \infty$ limits lie outside that finite scope
```

**ch19:126** · row X-01 (O) · mechanical · edits D182. Mirror: FULL:5196, identical strings (D183).
Reason: X-01 pointer rule (mirror of M:594).

Old:

```text
the concrete OI substratum, in its finite model (ledger item (ii)), supplies the structural architecture — closure under composition and coarse-graining, stability under an uncoupled spectator, relabelling invariance, reversibility, the exchanges of distinguishable states, and, as a stated intervention principle rather than a consequence of its finite states and bijective dynamics, the phases — but, under finite bijective read-write dynamics 
```

New:

```text
the concrete OI substratum, in its finite model, supplies the structural architecture — closure under composition and coarse-graining, stability under an uncoupled spectator, relabelling invariance, reversibility, the exchanges of distinguishable states, and, as a stated intervention principle rather than a consequence of its finite states and bijective dynamics, the phases — but, under finite bijective read-write dynamics 
```

**ch19:212** · row X-01 (O) · mechanical · edits D184. Mirror: FULL:5282, identical strings (D185).
Reason: X-01 rule.

Old:

```text
classical probability — together with the open hypothesis A1 of finiteness constrain the class.
```

New:

```text
classical probability — constrain the class.
```

**ch19:214** · row X-01 (O) · mechanical · edits D186. Mirror: FULL:5284, identical strings (D187).
Reason: X-02 rule.

Old:

```text
deterministic bijection structure (finite under A1) is not
```

New:

```text
deterministic bijection structure is not
```

**ch19:216** · row X-01 (O) · semantic · edits D188. Mirror: FULL:5286, identical strings (D189).
Reason: Cardinality-neutral restatement.

Old:

```text
(deterministic bijectivity, on a finite set under A1, no further commitments)
```

New:

```text
(deterministic bijectivity on a set of unspecified cardinality, no further commitments)
```

**ch19:360** · row X-01 (O) · semantic · edits D190. Mirror: FULL:5430, identical strings (D191).
Reason: The question presupposes the retired hypothesis; it is removed with it.

Old:

```text
 Whether the finiteness hypothesis A1 has implications for mathematical foundations (constructivism, finitism, ultrafinitism) is not addressed.
```

New:

```text
(deleted)
```

**appC:16** · row X-01 (O) · mechanical · edits D192. Mirror: FULL:6171, identical strings (D193).
Reason: X-01 rule; follows the §C.6 heading.

Old:

```text
and finiteness (whether the framework's posit A1 is too strong).
```

New:

```text
and finiteness (whether the framework assumes a finite universe).
```

**appC:96** · row X-01 (O) · semantic · edits D194. Mirror: FULL:6251, identical strings (D195).
Reason: Ledger X-02: the objection is answered by the finite-only scope.

Old:

```text
## C.6 Finiteness: is posit A1 too strong?
```

New:

```text
## C.6 Finiteness: does the framework assume a finite universe?
```

**appC:98** · row X-01 (O) · semantic · edits D196. Mirror: FULL:6253, identical strings (D197).
Reason: Ledger X-02 rule for §C.6.

Old:

```text
concerns the framework's finiteness hypothesis — posit A1 (Chapter 2 §2.4), an open hypothesis, not adopted, takes the substratum to be a finite set $S$. Critics object that this is incompatible
```

New:

```text
concerns finiteness: several of the framework's results are stated for a finite substratum $S$. Critics object that a finite substratum is incompatible
```

**appC:102** · row X-01 (O) · needs scientific review · edits D198. Mirror: FULL:6257, identical strings (D199).
Reason: States the owner's cardinality-neutral principle in the book; review that every result named in §C.6 matches its finite or size-independent source statement.

Old:

```text
**The framework's response.** Posit A1 plays different roles in different parts of the framework's content, with different evidential supports for each role.
```

New:

```text
**The framework's response.** The framework assumes neither that the substratum is finite nor that it is infinite. Finiteness enters as the scope of the results stated for a finite representative, and it plays different roles in different parts of the framework's content.
```

**appC:104** · row X-01 (O) · semantic · edits D200. Mirror: FULL:6259, identical strings (D201).
Reason: Ledger X-02; the (NR) clause and its S2-C qualification are untouched.

Old:

```text
Posit A1 is a mathematical assumption of the results that use it, the recurrence route to P-indivisibility among them, and one sufficient condition rather than a premise of the framework:
```

New:

```text
Finiteness of the representative is a mathematical hypothesis of the results stated for a finite representative, the recurrence route to P-indivisibility among them, and not a premise of the framework:
```

**appC:106** · row X-01 (O) · semantic · edits D202. Mirror: FULL:6261, identical strings (D203).
Reason: Ledger X-02; the deep-sector clause that follows is kept.

Old:

```text
It does not establish finiteness of the total configuration space $S$. That extension is posit A1 of Chapter 2 §2.4, an open hypothesis, not adopted, read as the choice of the minimal finite representative:
```

New:

```text
It does not establish finiteness of the total configuration space $S$, and the framework does not assume it: the minimal finite representative is a choice of representative, and
```

**appC:108** · row X-01 (O) · semantic · edits D204, D206. Mirror: FULL:6263, identical strings (D205, D207).
Reason: Ledger X-02 rule for §C.6.

Old (part 1):

```text
A referee who rejects posit A1 for the universe as a whole does not thereby reject the Bekenstein bound,
```

New (part 1):

```text
A referee who denies that the universe as a whole is finite does not thereby reject the Bekenstein bound,
```

Old (part 2):

```text
does not establish finiteness of the whole of $S$, which is the open hypothesis A1. A1 agrees with mainstream physics' commitment to the Bekenstein bound on the accessible sector, and would extend beyond it.
```

New (part 2):

```text
does not establish finiteness of the whole of $S$. The framework's finite-only results agree with mainstream physics' commitment to the Bekenstein bound on the accessible sector and make no claim about the whole of $S$.
```

**appC:110** · row X-01 (O) · needs scientific review · edits D208. Mirror: FULL:6265, identical strings (D209).
Reason: The rebuttal rests on discreteness, not finiteness; review that the boundary count N that follows is stated for the horizon and not for the whole lattice.

Old:

```text
At the substratum level, the framework posits a discrete lattice,
```

New:

```text
At the substratum level, the framework posits a discrete lattice (Chapter 2 §2.4), with no claim about the number of its sites,
```

**appC:112** · row X-01 (O) · needs scientific review · edits D210, D212. Mirror: FULL:6267, identical strings (D211, D213).
Reason: The condensed-matter analogy is restated for discreteness; review the analogy.

Old (part 1):

```text
finite at the substratum level under A1 but *appearing* infinite-dimensional
```

New (part 1):

```text
discrete at the substratum level, and finite-dimensional on a finite representative, but *appearing* infinite-dimensional
```

Old (part 2):

```text
the underlying physics is finite, but the long-wavelength
```

New (part 2):

```text
the underlying physics is discrete, but the long-wavelength
```

**appC:114** · row X-01 (O) · semantic · edits D214. Mirror: FULL:6269, identical strings (D215).
Reason: Ledger X-02 rule for §C.6.

Old:

```text
A1 is therefore *compatible with* the standard QFT description as an effective continuum theory while making specific structural claims about the substratum level. The two levels of description coexist; if A1 holds, the apparent
```

New:

```text
The discrete substratum is therefore *compatible with* the standard QFT description as an effective continuum theory while making specific structural claims about the substratum level. The two levels of description coexist; on a finite representative, the apparent
```

**appC:116** · row X-01 (O) · semantic · edits D216. Mirror: FULL:6271, identical strings (D217).
Reason: Ledger X-02 rule for §C.6; cardinality-neutral.

Old:

```text
A1 is therefore not just a mathematical convenience but a structurally consequential hypothesis, motivated by the Bekenstein bound and compatible with continuum QFT.
```

New:

```text
Finiteness is therefore the stated scope of specific results, not a premise about the universe, and is compatible with continuum QFT.
```

**appC:136** · row X-01 (O) · semantic · edits D218. Mirror: FULL:6291, identical strings (D219).
Reason: Finite scope attached to the computability claim (review round 1, F5); see H-3 and D246.

Old:

```text
that $\varphi$ is a bijection on a finite set (under A1), which is trivially computable:
```

New:

```text
that on a finite representative $\varphi$ is a bijection on a finite set, which is trivially computable:
```

**gloss:13** · row X-45 (F) · mechanical · edits D220. Mirror: FULL:6504, identical strings (D221).
Reason: Range and count rewrite; A6 keeps its identifier (owner decision item 5).

Old:

```text
The sixth of the framework's structural assumptions A1–A6:
```

New:

```text
The structural assumption A6 of the reconstruction theorem (A2–A6):
```

**gloss:137** · row X-01 (O) · semantic · edits D222. Mirror: FULL:6628, identical strings (D223).
Reason: Cardinality-neutral restatement.

Old:

```text
Its total configuration space is finite in the representative specified under the open posit A1.
```

New:

```text
The cardinality of its total configuration space is left open; results stated for a finite representative take it finite.
```

**M:732** · row X-00 (O) · needs scientific review · edits D224, D225, D226, D227, D228, D253.
Reason: X-00: item (ii) is deleted and its identifier retired, not reused and not annotated (§A.30; owner decision items 1, 2, 5: (iii)-(xiv) keep their numbers). Its content moves to the status Remark M:60 (weaker conditions, transfer clause); the finite-representative list and the deep-sector clause are already printed there (S2-B). The count becomes thirteen, and the completeness sentence states that finite-representative results carry their scope where stated (D253; review round 1, F4). Review: the posit count and that no result loses its stated conditions.

Old (part 1):

```text
(ii) total finiteness of the bijective representative of the status Remark of §1.2 (an open hypothesis, not adopted), carried as one sufficient condition and not as a premise of the framework: each result that uses it names the hypotheses it consumes, and a weaker sufficient condition, where its sufficiency is proved, is stated with the result — the near-return condition (NR) for the P-indivisibility conclusion of §2.3 and for the P-indivisibility input of the CP-indivisibility theorem of §3.2 on a measurable hidden carrier, the invariant-product condition (IP) for the doubly stochastic marginal of §3.2 and the invariant-law condition (IL) for the decay estimate of §4.6, each assumed as a hypothesis of that result and not adopted, and reversibility (REV), item (iii), an alternative sufficient condition for bijectivity — while the counting-measure selection of Lemma 3, the exact return and its index $L$, the orbit capacity and the canonical-typicality step of §4.6 are statements about finite representatives — Lemma 1 delivers finiteness of the observer's distinguishable states from the finite-capacity clause of the Definition, and the extension to the whole representative is A1 of the companion substratum construction — there scoped as the gauge choice of the minimal finite representative, the cardinality of a deep sector being unobservable at the fixed visible/hidden interface when that sector is a factor of any cardinality prepared independently in a normalized state or law and evolved by its own dynamics (a unitary or isometry, or a measurable map), with product dynamics, which leaves every reduced visible channel, and hence every transition probability, unchanged (deep-sector enlargement, developed there) — consumed here by the recurrence step of §2.3 and by §4.6, whose conclusions hold on the finite representative; their transfer, where expressible through the transition probabilities, to every representative reached from it by relabelling the hidden states, by such a decoupled enlargement or, under the alphabet-size hypothesis that systems with the same coupling structure and dynamics class differing only in alphabet size have the same emergent transition probabilities, by a change of alphabet that keeps the coupling structure and dynamics class is stated and proved in the companion substratum construction, while the recurrence-scale conclusion of §2.3 is a statement about finite representatives, the remaining uses of the posit being listed in the status Remark of §1.2; 
```

New (part 1):

```text
(deleted)
```

Old (part 2):

```text
on a finite representative (item (ii)) using one *empirical* input
```

New (part 2):

```text
on a finite representative using one *empirical* input
```

Old (part 3):

```text
Fourteen items, of unequal weight, and not fourteen independent physical assumptions:
```

New (part 3):

```text
Thirteen items, of unequal weight, and not thirteen independent physical assumptions:
```

Old (part 4):

```text
the total finiteness of item (ii) and items (iv)–(xiv) lie outside the layer it treats
```

New (part 4):

```text
items (iv)–(xiv) lie outside the layer it treats
```

Old (part 5):

```text
this ledger states what is *assumed* or, for item (ii), hypothesized, and the framework's claims are conditional on the full list, item (ii) entering only as one of the sufficient conditions named at each use.
```

New (part 5):

```text
this ledger states what is *assumed*, and the framework's claims are conditional on the full list.
```

Old (part 6):

```text
as these texts stand in the same revision of the repository. It does not enumerate every physical assumption
```

New (part 6):

```text
as these texts stand in the same revision of the repository; the results that use a finite representative (the recurrence step of §2.3, the counting measure of Lemma 3 and §4.6 among them) carry that finite scope where they are stated (§1.2 Remark) rather than as a listed premise. It does not enumerate every physical assumption
```

**M:60** · row X-00 (O) · needs scientific review · edits D229, D230, D254, D231.
Reason: X-00: the posit sentence becomes the finite-representative scope and receives item (ii)'s weaker-condition list (with S2-B's CP clause) and its transfer clause, verbatim apart from the connective; the P8 sentence takes ledger X-00 wording. After the deletion M:60 is Main's first mention of (NR), (IP) and (IL), so S2-C's return- and law-form qualifications are printed there and at the later (NR) mention (review round 1, F3). Review: that the transfer clause is not stronger than the companion proof.

Old (part 1):

```text
Total finiteness of that representative is one sufficient condition for the results that use it, carried as item (ii) of the posit ledger (§4.5), the total-finiteness posit, an open hypothesis, not adopted; each such result names the hypotheses it consumes, and a weaker sufficient condition, where its sufficiency is proved, is stated with the result (§2.3, §3.2, §4.6);
```

New (part 1):

```text
The results that use that representative are statements about finite representatives; each such result names the hypotheses it consumes, and a weaker sufficient condition, where its sufficiency is proved, is stated with the result — the near-return condition (NR) for the P-indivisibility conclusion of §2.3 and for the P-indivisibility input of the CP-indivisibility theorem of §3.2 on a measurable hidden carrier, the invariant-product condition (IP) for the doubly stochastic marginal of §3.2 and the invariant-law condition (IL) for the decay estimate of §4.6, each assumed as a hypothesis of that result and not adopted ((NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it; (IP) and (IL) are conditions on a law on the whole carrier; finite-window data can test some of their consequences but cannot establish them, and do not distinguish them from a finite carrier's counting law), and reversibility (REV), item (iii) of the posit ledger (§4.5), an alternative sufficient condition for bijectivity;
```

Old (part 2):

```text
The physical reading of the characterization theorem — the identification of nature with a finite reversible substratum — is accordingly conditional on that representation choice, an empirically motivated reconstruction rather than a pure derivation; the law-level equivalence of §3.4 itself holds for every finite-horizon law.
```

New (part 2):

```text
The characterization theorem is a statement about finite-horizon laws and their finite representatives; it does not identify nature with a finite reversible substratum, and the law-level equivalence of §3.4 holds for every finite-horizon law.
```

Old (part 3):

```text
(for whose P-indivisibility conclusion the near-return condition (NR) of §2.3 is a weaker sufficient condition;
```

New (part 3):

```text
(for whose P-indivisibility conclusion the near-return condition (NR) of §2.3, assumed as a hypothesis and not adopted, is a weaker sufficient condition (it concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it);
```

Old (part 4):

```text
Of the two finiteness statements, the following results use only
```

New (part 4):

```text
The transfer of the conclusions of the recurrence step of §2.3 and of §4.6, where expressible through the transition probabilities, from a finite representative to every representative reached from it by relabelling the hidden states, by a decoupled enlargement of the kind just stated or, under the alphabet-size hypothesis that systems with the same coupling structure and dynamics class differing only in alphabet size have the same emergent transition probabilities, by a change of alphabet that keeps the coupling structure and dynamics class is stated and proved in the companion substratum construction; the recurrence-scale conclusion of §2.3 is a statement about finite representatives. Of the two finiteness statements, the following results use only
```

**Sub:92** · row X-02 (O) · semantic · edits D232.
Reason: X-02: the (A1) entry is deleted; Theorem 23 states finiteness as its scope (X-45). The E3/H-BD reading survives at Sub:268 (i), the factor freedom at Theorem 24(iii) and (NR) at Main §2.3 and Sub:137. With the entry gone, A4's Z^d standard construction is no longer excluded by the assumption list (S2-A review finding).

Old:

```text
(A1) **Finiteness.** The configuration space $S$ is finite. E3, read as a Hilbert-space dimension cutoff $\dim\mathcal H\le e^{A/4}$, bounds the observationally relevant visible sector and boundary layer $\mathcal C_V\times\mathcal C_B$ under the deep-sector influence bound H-BD of [GR §3.2]. This bound alone does not establish finiteness of every underlying sector. Theorem 24(iii) gives an exact freedom to adjoin independently prepared decoupled factors of any cardinality at a fixed interface, each in a normalized state or law with its own unitary, isometric or measurable dynamics; an unnormalizable factor is not covered. A deep sector coupled under H-BD changes the transition law by at most $2t/\tau_{BD}$ ([GR §3.2]), so its comparison is only at leading order on accessible timescales. A1 is an open hypothesis, not adopted ([Main §4.5], item (ii)), and one sufficient condition among those each result names: it remains the finite-carrier premise for the recurrence arguments, and for their P-indivisibility conclusion the near-return condition (NR) of [Main §2.3], assumed in its place and not adopted, is a weaker sufficient condition. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it.
```

New:

```text
(deleted)
```

**ch02:76** · row X-02 (O) · semantic · edits D233. Mirror: FULL:706, identical strings (D234).
Reason: X-02: the (A1) entry is deleted (book mirror of Sub:92).

Old:

```text
*(A1) Finiteness.* The configuration space $S$ is finite. Lemma 1 of Chapter 1 delivers finiteness of the observer's distinguishable states; the extension to all of $S$ is an open hypothesis, not adopted, read as the choice of the minimal finite representative and motivated by E3 (the holographic bound read as a dimension cutoff); it is one sufficient condition among those the results name. Its scope, and which results use it, are stated in [Main §1.2], Remark (status of the early commitments).
```

New:

```text
(deleted)
```

**gloss:11** · row X-01 (O) · semantic · edits D235, D237. Mirror: FULL:6502, 6562, identical strings (D236, D238).
Reason: Ledger X-02: the A1 entry is replaced by a finite-representative entry, inserted at its alphabetical place.

Old (part 1):

```text
**A1 (Finiteness).** The open hypothesis, not adopted, that the substratum has a finite total configuration space (Chapter 2 §2.4), as assumed in the minimal finite representative. Motivated physically by the Bekenstein bound at the cosmological horizon (an entropy-based bound, under the physical assumptions of input E3, of at most $e^{S_{\text{dS}}}$ effectively distinguishable states of the visible sector and boundary layer, $S_{\text{dS}} \sim 10^{122}$). It is one sufficient condition for the results that use it, each of which names the hypotheses it consumes. Discussed in Chapter 2 §2.4, with defense in Appendix C §C.6.
```

New (part 1):

```text
(deleted)
```

Old (part 2):

```text
**Frauchiger-Renner theorem.**
```

New (part 2):

```text
**Finite representative.** The minimal finite bijective representative $(S, \varphi)$ of a finite hidden dynamics, on which the results stated for a finite substratum hold — among them the exact return and its index, the counting measure and the reconstruction theorem of Chapter 2. These results are finite-only; the framework assumes neither that the substratum is finite nor that it is infinite. Lemma 1 delivers finiteness of the observer's distinguishable states. Discussed in Chapter 1 and Appendix C §C.6.

**Frauchiger-Renner theorem.**
```

### 6.2 Consistency corrections outside the 194 sites

**ch02:74** · row X-45 (F) · semantic · edits D239. Mirror: FULL:704, identical strings (D240).
Reason: Count follows the deletion of the (A1) entry (§A.30 count rule); A2–A6 keep their identifiers.

Old:

```text
The reconstruction restricts attention to candidate substrates satisfying six properties:
```

New:

```text
The reconstruction restricts attention to finite candidate substrates satisfying five properties:
```

**ch02:120** · row X-45 (F) · mechanical · edits D241. Mirror: FULL:750, identical strings (D242).
Reason: Count follows the deletion of A1; the theorem's finite scope is stated (X-45).

Old:

```text
together with six structural assumptions and the nearest-neighbor restriction
```

New:

```text
together with five structural assumptions on a finite substratum and the nearest-neighbor restriction
```

**GR:673** · row - (-) · mechanical · edits D243.
Reason: Hidden dependency H-1: the line names A1 but the ledger classifies it FREE (P0 class), so it is not among the 194 ptr sites. Range and label rewrite; no claim changes.

Old:

```text
OI's full structural conditions A1–A6 except at S3: A1 (finiteness) makes the number of configurations finite but supplies
```

New:

```text
OI's full structural conditions (finiteness and A2–A6) except at S3: finiteness makes the number of configurations finite but supplies
```

**Sub:56** · row X-63 (O) · mechanical · edits D244.
Reason: Hidden dependency H-2: S2-D (X-63/X-82) prints a pointer to A1 at Sub:56 on its branch; at deletion the pointer becomes the property it names. The S2-D content (open inflow question, conditional on an infinite carrier) is unchanged.

Old:

```text
Without A1 the question also concerns an incoming supply:
```

New:

```text
Without finiteness the question also concerns an incoming supply:
```

**Sub:137** · row X-20 (J) · semantic · edits D245.
Reason: Hidden dependency H-4: Sub:92 is the only Substratum site that states (NR) and its S2-C qualification; deleting the (A1) entry would drop the weaker condition silently. The clause is relocated, verbatim apart from the connective, to the Stage 1 recurrence sentence it qualifies (J row X-20; deletion criterion 3).

Old:

```text
also give recurrence-cycle P-indivisibility [Main §2.3].
```

New:

```text
also give recurrence-cycle P-indivisibility [Main §2.3]; the near-return condition (NR) of [Main §2.3], assumed in its place and not adopted, is a weaker sufficient condition for that P-indivisibility conclusion. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it.
```

**ch09:104** · row X-46 (F) · semantic · edits D255. Mirror: FULL:2519, identical strings (D256).
Reason: Count and wording: finiteness (ch09:106) is the scope of the finite class, not a sixth membership property (review round 1, F8); A2–A6 keep their identifiers.

Old:

```text
are six structural properties of the substratum, organized as follows.
```

New:

```text
are, for the finite OI class, five structural properties of the substratum; finiteness, stated first, is that class's scope. They are organized as follows.
```

**ch09:190** · row X-46 (F) · semantic · edits D257. Mirror: FULL:2605, identical strings (D258).
Reason: Count and wording as ch09:104 (review round 1, F8).

Old:

```text
Six structural axioms must be checked for compatibility under such a bridge.
```

New:

```text
The finite scope and five structural axioms must be checked for compatibility under such a bridge.
```

**M:42** · row - (-) · semantic · edits D259.
Reason: Owner decision #1169 c.7058446475: the approved sentence, verbatim with Main's symbol $S$ for $\mathcal S$ and the run-in bold of Main's paragraph heads, as a paragraph after the Definition and the paragraph that unpacks it ("This definition formalizes ...", review round 5 nit), before Lemma 1. No label, identifier or assumption. Nearby finite-only results keep their scope (Lemma 1, Lemma 3 by D260, the measure remark by D309, the status Remark M:60; preservation check).

Old:

```text


**Lemma 1** (Finiteness). *The finite-capacity clause
```

New:

```text


**Configuration space.** The substratum has a configuration space $S$. No restriction is imposed on its cardinality; $S$ may be finite or infinite.

**Lemma 1** (Finiteness). *The finite-capacity clause
```

**M:54** · row X-10 (F) · semantic · edits D260.
Reason: F row X-10: the counting-measure selection is a statement about finite representatives; its scope was carried by M:732 item (ii)'s list, which D224 deletes, and the configuration-space sentence two paragraphs above admits an infinite $S$, so the scope is printed in the lemma (owner condition: no finite-only result read as applying to arbitrary configuration spaces).

Old:

```text
globally, the counting measure is selected among invariant measures as the maximal-entropy one
```

New:

```text
globally, on a finite representative, the counting measure is selected among invariant measures as the maximal-entropy one
```

**Sub:42** · row - (-) · semantic · edits D261.
Reason: Owner decision #1169 c.7058446475: the approved sentence, verbatim with Substratum's symbol $S$, as the opening paragraph of §2 (the setup of $(S, \varphi)$). The next paragraph keeps its finite scope ("*finite capacity* when $S$ is finite", D013; preservation check).

Old:

```text
**Storage and memory.**
```

New:

```text
**Configuration space.** The substratum has a configuration space $S$. No restriction is imposed on its cardinality; $S$ may be finite or infinite.

**Storage and memory.**
```

**appC:138** · row - (-) · semantic · edits D246. Mirror: FULL:6293, identical strings (D247).
Reason: Hidden dependency H-3: the computability claim uses finiteness (a lookup table); the finite scope is kept and the evaluative clause is dropped with the narrowing (review round 1, F5). A size-independent form would need uniformity of the rule as a named hypothesis and is not drafted.

Old:

```text
But the bijection is in-principle computable, which is the relevant claim for foundational physics.
```

New:

```text
But on a finite representative the bijection is in-principle computable.
```

**M:58** · row X-10 (F) · semantic · edits D309.
Reason: F row X-10: the uniform probability and the uniform conditional law on $\mathcal{C}_H$ need a finite carrier; scoped as D260 scopes Lemma 3 (review round 5, must-fix 2).

Old:

```text
On the selected bijective carrier $\mathcal{C}_V \times \mathcal{C}_H$ (Lemma 2) it is the uniform probability
```

New:

```text
On the selected bijective carrier $\mathcal{C}_V \times \mathcal{C}_H$ of a finite representative (Lemma 2) it is the uniform probability
```

**ch01:26** · row - (-) · semantic · edits D310. Mirror: FULL:361, identical strings (D311).
Reason: Owner decision #1169 c.7058783437 (book mirrors): the approved sentence after ch01's Definition and the paragraph that follows it, as in Main (D259).

Old:

```text


**Lemma 1 (Finiteness).** *The observer's finite capacity
```

New:

```text


**Configuration space.** The substratum has a configuration space $S$. No restriction is imposed on its cardinality; $S$ may be finite or infinite.

**Lemma 1 (Finiteness).** *The observer's finite capacity
```

**ch01:38** · row X-10 (F) · semantic · edits D312, D349. Mirror: FULL:371, identical strings (D313, D350).
Reason: F row X-10: book mirror of D260; and the bijectivity clause takes its conditions, a finite representative (the eventual-image argument) or the posit A2 (review round 6): the configuration-space sentence above admits an infinite $S$.

Old (part 1):

```text
globally the counting measure is selected among the invariant measures
```

New (part 1):

```text
globally, on a finite representative, the counting measure is selected among the invariant measures
```

Old (part 2):

```text
**Lemma 3 (Determinism and selected measure).** *$\varphi$ is a bijection on $S$.
```

New (part 2):

```text
**Lemma 3 (Determinism and selected measure).** *On a finite representative, or under A2 (Chapter 2 §2.4), $\varphi$ is a bijection on $S$.
```

### 6.3 Sites deferred to the deletion edit by S2-E (outside the 194)

**Comp:120** · row X-01 (O) · mechanical · edits D248.
Reason: X-01 site deferred to the deletion edit by S2-E (its PREREG §3).

Old:

```text
For a fixed physical realization, the total-finiteness posit ([Main] §1.2, §4.5) remains open and unadopted.
```

New:

```text
For a fixed physical realization, finiteness of the total configuration space is not assumed ([Main] §1.2).
```

**Meth:156** · row X-01 (O) · semantic · edits D249.
Reason: X-01 site deferred to the deletion edit by S2-E (its PREREG §3); the steps keep their finite scope.

Old:

```text
that extension is not supplied by the clause: it is the structural assumption A1 of the substratum construction, counted as such in the companion paper's posit ledger ([Main §4.5], of which this rung analysis is the complementary view
```

New:

```text
that extension is not supplied by the clause, and those steps are statements about finite representatives ([Main §1.2]; the posit ledger of [Main §4.5] is the complementary view of this rung analysis
```

**Meth:158** · row X-30 (J) · semantic · edits D250.
Reason: X-01 site deferred to the deletion edit by S2-E (its PREREG §3); J row X-30 names (REV).

Old:

```text
together with finiteness of the total space, which is A1.
```

New:

```text
together with finiteness of the representative; on a carrier of unspecified cardinality bijectivity rests on the posit (REV) ([Main §4.5], item (iii)).
```

**ch18:40** · row X-82 (O) · mechanical · edits D251. Mirror: FULL:4771, identical strings (D252).
Reason: Pointer left for the deletion edit by S2-E (its PREREG §3). Pointer-only rewrite approved by owner ruling #1169 c.7057674976: "under A1" is dropped because "finite reversible" already states the condition; the physical content, its conditional scope and the X-82 no-change decision on the inflow content are kept.

Old:

```text
the finite reversible substratum dynamics, which is recurrent under A1 (§18.7);
```

New:

```text
the finite reversible substratum dynamics, which is recurrent (§18.7);
```

### 6.4 Lean docstring edits (H-11 and the repository-wide consistency decision; outside the 194)

**Manu:4** · row - (-) · mechanical · edits D262.
Reason: Module heading: the substratum conditions are finiteness of the configuration space and A2–A6; owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old:

```text
# The manuscript-axiom audit — A1–A6 against the substratum witness
```

New:

```text
# The manuscript-axiom audit — the substratum conditions against the substratum witness
```

**Manu:8** · row - (-) · mechanical · edits D263.
Reason: Replaces D259's pinned-commit form (superseded by owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly). Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old:

```text
the manuscripts' own structural assumptions are A1–A6 of
`[Substratum §3.1]`: finiteness of the configuration space, bijectivity of the dynamics, bounded
```

New:

```text
the manuscripts' conditions on a substratum are finiteness of the configuration space (the scope
of the reconstruction theorem) and A2–A6 of `[Substratum §3.1]`: bijectivity of the dynamics, bounded
```

**Manu:17** · row - (-) · mechanical · edits D264.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old:

```text
Every one of A1–A6 is a condition on a substratum
```

New:

```text
Each of these conditions is a condition on a substratum
```

**Manu:21** · row - (-) · mechanical · edits D265, D266, D267.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old (part 1):

```text
manuscript-level conjunct of A1–A6 is presently a faithful predicate of the bare theory. A1 and
A2 have exact
```

New (part 1):

```text
manuscript-level conjunct of these conditions is presently a faithful predicate of the bare theory.
Finiteness and A2 have exact
```

Old (part 2):

```text
A1's holds for every theory by the
```

New (part 2):

```text
the finiteness image holds for every theory by the
```

Old (part 3):

```text
at the substratum level A1 and A2 are
```

New (part 3):

```text
at the substratum level finiteness and A2 are
```

**Manu:68** · row - (-) · mechanical · edits D268, D269, D270, D271, D272, D273.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old (part 1):

```text
### Section A — the realized-core images of A1 and A2
```

New (part 1):

```text
### Section A — the realized-core images of finiteness and A2
```

Old (part 2):

```text
**THE REALIZED-CORE IMAGE OF A1**: the configuration space
```

New (part 2):

```text
**THE REALIZED-CORE IMAGE OF FINITENESS**: the configuration space
```

Old (part 3):

```text
It is an image
of A1, not A1: nothing identifies
```

New (part 3):

```text
It is an image
of finiteness, not finiteness of `S`: nothing identifies
```

Old (part 4):

```text
conjunct of A1–A6 has a faithful form in this interface.
```

New (part 4):

```text
conjunct of the substratum conditions has a faithful form in this interface.
```

Old (part 5):

```text
**THE A1 IMAGE HOLDS FOR EVERY THEORY**
```

New (part 5):

```text
**THE FINITENESS IMAGE HOLDS FOR EVERY THEORY**
```

Old (part 6):

```text
**THE A1 IMAGE HOLDS FOR THE WITNESS.**
```

New (part 6):

```text
**THE FINITENESS IMAGE HOLDS FOR THE WITNESS.**
```

**Subs:7** · row - (-) · mechanical · edits D274, D275, D276.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly; the kernel predicate `A1` is named as the finiteness predicate it is. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old (part 1):

```text
substratum carrying the manuscript substrate data, A1–A5 represented as stated
```

New (part 1):

```text
substratum carrying the manuscript substrate data, the finiteness predicate `A1` and A2–A5 represented as stated
```

Old (part 2):

```text
`leapEquiv`, and lattice translations; A1, A2,
  A5 are stated outright
```

New (part 2):

```text
`leapEquiv`, and lattice translations; the finiteness predicate `A1`,
  A2 and A5 are stated outright
```

Old (part 3):

```text
instance, `waveSubstratum`, and satisfies A1–A5 as stated.
```

New (part 3):

```text
instance, `waveSubstratum`, and satisfies the finiteness predicate `A1` on a finite torus and A2–A5 as stated.
```

**Subs:83** · row - (-) · mechanical · edits D277, D278, D279, D280, D281.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly; each docstring states the finiteness condition its declaration carries. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old (part 1):

```text
**(A1) FINITENESS**: the configuration space is finite.
```

New (part 1):

```text
**FINITENESS**: the configuration space is finite.
```

Old (part 2):

```text
**A1 HOLDS UNDER FINITENESS OF THE SITES AND THE ALPHABET.**
```

New (part 2):

```text
**FINITENESS HOLDS FOR FINITELY MANY SITES AND A FINITE ALPHABET.**
```

Old (part 3):

```text
**THE WAVE SUBSTRATUM SATISFIES A1** for a finite torus and alphabet.
```

New (part 3):

```text
**THE WAVE SUBSTRATUM HAS A FINITE CONFIGURATION SPACE** for a finite torus and alphabet.
```

Old (part 4):

```text
under the finiteness A1 supplies.
```

New (part 4):

```text
for finitely many sites and a finite alphabet.
```

Old (part 5):

```text
**A1 FOR THE OBSERVER THEORY'S SUBSTRATUM.**
```

New (part 5):

```text
**FINITENESS FOR THE OBSERVER THEORY'S SUBSTRATUM.**
```

**Froz:83** · row - (-) · mechanical · edits D282.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly; the condition is the declaration's own `[Fintype 𝒮.ι] [Fintype 𝒮.V]`. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old:

```text
satisfying the finiteness A1 supplies.
```

New:

```text
with finitely many sites and a finite alphabet.
```

**HexL:106** · row - (-) · mechanical · edits D283.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old:

```text
**Nothing here changes A1–A6 or their status**
```

New:

```text
**Nothing here changes the substratum conditions or their status**
```

**Hydr:88** · row - (-) · mechanical · edits D284.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old:

```text
**Nothing here changes A1–A6**
```

New:

```text
**Nothing here changes the substratum conditions**
```

**Rout:108** · row - (-) · mechanical · edits D285.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old:

```text
whose A1–A6 are not `DerivedOI`
```

New:

```text
whose substratum conditions are not `DerivedOI`
```

**Subs:48** · row - (-) · mechanical · edits D286.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old:

```text
derive a quantum architecture from A1-A6 or from the
```

New:

```text
derive a quantum architecture from the substratum conditions or from the
```

**A6In:43** · row - (-) · mechanical · edits D314, D315.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old (part 1):

```text
put the packaged carrier against `A1`–`A5`,
```

New (part 1):

```text
put the packaged carrier against the finiteness predicate `A1` and `A2`–`A5`,
```

Old (part 2):

```text
state or cubic group action enters, `A1` is not weakened,
```

New (part 2):

```text
state or cubic group action enters, the finiteness predicate `A1` is not weakened,
```

**A6In:274** · row - (-) · mechanical · edits D316, D317, D318, D319, D320.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old (part 1):

```text
**`PK3-a` — A1** on the packaged carrier
```

New (part 1):

```text
**`PK3-a` — the finiteness predicate `A1`** on the packaged carrier
```

Old (part 2):

```text
THE COMPLEX CARRIER IS NOT A SUBSTRATUM SATISFYING A1, AND THIS IS THE PROOF.**
```

New (part 2):

```text
THE COMPLEX CARRIER IS NOT A SUBSTRATUM SATISFYING THE FINITENESS PREDICATE `A1`, AND THIS IS THE PROOF.**
```

Old (part 3):

```text

`Substratum.A1` is `Finite (ι → V × V)`
```

New (part 3):

```text

The finiteness predicate `Substratum.A1` is `Finite (ι → V × V)`
```

Old (part 4):

```text
**`A1` is
not weakened**
```

New (part 4):

```text
**the finiteness predicate `A1` is
not weakened**
```

Old (part 5):

```text
a substratum satisfying
`A1`.
```

New (part 5):

```text
a substratum satisfying
the finiteness predicate `A1`.
```

**HexL:37** · row - (-) · mechanical · edits D321, D322.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old (part 1):

```text
`hexSubstratum L` satisfies `A1`,
```

New (part 1):

```text
`hexSubstratum L` satisfies the finiteness predicate `A1`,
```

Old (part 2):

```text
**`HB0-a` — A1**: the configuration space is finite.
```

New (part 2):

```text
**`HB0-a` — the finiteness predicate `A1`**: the configuration space is finite.
```

**Wave:21** · row - (-) · mechanical · edits D323, D324.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption. Docstring only; identifiers keep their names (rename proposals in PREREG §22).

Old (part 1):

```text
(control) : for `d ≥ 1` and a nontrivial alphabet, A1 fails at `L = 0`;
```

New (part 1):

```text
(control) : for `d ≥ 1` and a nontrivial alphabet, the finiteness predicate `A1` fails at `L = 0`;
```

Old (part 2):

```text
Control: for `d ≥ 1` and a nontrivial alphabet, A1 fails at `L = 0`.
```

New (part 2):

```text
Control: for `d ≥ 1` and a nontrivial alphabet, the finiteness predicate `A1` fails at `L = 0`.
```

### 6.5 Other active repository files (repository-wide consistency decision; outside the 194)

**READ:917** · row - (-) · mechanical · edits D287.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly (mutable landing page, §A.27).

Old:

```text
whose A1–A6 are not `DerivedOI`;
```

New:

```text
whose substratum conditions are not `DerivedOI`;
```

**READ:923** · row - (-) · mechanical · edits D288, D289, D290, D291.
Reason: owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly (mutable landing page, §A.27); kernel identifiers keep their names.

Old (part 1):

```text
the manuscripts' own structural assumptions A1–A6 of the Substratum paper, each quoted verbatim
and given a representability verdict
```

New (part 1):

```text
the Substratum paper's conditions on a substratum, finiteness of the configuration space (the scope
of the reconstruction theorem) and A2–A6, each given a representability verdict
```

Old (part 2):

```text
So no manuscript-level
A1–A6 conjunct is presently a faithful predicate of the bare theory. A1 and A2 have exact
```

New (part 2):

```text
So no manuscript-level
conjunct of these conditions is presently a faithful predicate of the bare theory. Finiteness and A2 have exact
```

Old (part 3):

```text
two; at the substratum level A1 and A2 are formalization gaps
```

New (part 3):

```text
two; at the substratum level finiteness and A2 are formalization gaps
```

Old (part 4):

```text
whether the witness satisfies any of
A1–A6 in the manuscript sense
```

New (part 4):

```text
whether the witness satisfies any of
these conditions in the manuscript sense
```

**lean:485** · row - (-) · mechanical · edits D292.
Reason: Registry note quotes GR:261, which D044 rewrites; §A.25 step 5, §A.35.

Old:

```text
the controllability resource is not entailed by A1-A6 is consistent with it
```

New:

```text
the controllability resource is not entailed by finiteness or by A2-A6 is consistent with it
```

**lean:494** · row - (-) · mechanical · edits D293, D294.
Reason: Registry note of the family "manuscript axioms A1-A6" (family name kept; rename proposal R-C in PREREG §22); owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly.

Old (part 1):

```text
no manuscript-level A1-A6 conjunct of Substratum 3.1 is presently a faithful predicate of the bare theory, which has no distinguished underlying substratum; A1 and A2 have exact realized-core images
```

New (part 1):

```text
no manuscript-level conjunct of the Substratum 3.1 conditions (finiteness and A2-A6) is presently a faithful predicate of the bare theory, which has no distinguished underlying substratum; finiteness and A2 have exact realized-core images
```

Old (part 2):

```text
consistent with the manuscripts' statement that the resource is not entailed by A1-A6 and with SM 4.1's open lift; asserts nothing about whether the witness satisfies any of A1-A6 in the manuscript sense
```

New (part 2):

```text
consistent with the manuscripts' statement that the resource is not entailed by finiteness or by A2-A6 and with SM 4.1's open lift; asserts nothing about whether the witness satisfies any of these conditions in the manuscript sense
```

**LEDG:330** · row - (-) · mechanical · edits D295.
Reason: Coverage-ledger assumptions field; owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly. The entry's fingerprint is unaffected (it fingerprints manuscript text).

Old:

```text
 Physical total finiteness (A1) remains open and unadopted.
```

New:

```text
 Finiteness of the total configuration space is not assumed.
```

**AGEN:38** · row - (-) · mechanical · edits D296.
Reason: Approved by owner decision #1169 c.7058783437 ("correct the obsolete A1 reference. Keep the scientific principle that the substratum uses only assumptions justified by evidence or necessary for stated results, and remove A1 from its list of posits"): only the retired posit leaves the list; nothing else in the rule changes.

Old:

```text
including total
  finiteness (A1), linearity (A5),
```

New:

```text
including
  linearity (A5),
```

**lean:984** · row - (-) · mechanical · edits D297, D298.
Reason: Registry note: "A1-A6" here means the manuscripts' structural assumptions and their status; owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly.

Old (part 1):

```text
none fixed by the manuscripts or by A1-A6;
```

New (part 1):

```text
none fixed by the manuscripts or by the substratum conditions;
```

Old (part 2):

```text
nothing changes A1-A6 or their status,
```

New (part 2):

```text
nothing changes the substratum conditions or their status,
```

**lean:993** · row - (-) · mechanical · edits D299, D334, D335.
Reason: Registry note; owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly.

Old (part 1):

```text
A1-A6 unchanged;
```

New (part 1):

```text
the substratum conditions unchanged;
```

Old (part 1):

```text
HB0: A1, A2, A3 with degree 6
```

New (part 1):

```text
HB0: the finiteness predicate `A1`, A2, A3 with degree 6
```

Old (part 2):

```text
A RIGOROUS REVERSIBLE FLUID WITNESS IN THE A1-A4, NOT-A5 CLASS
```

New (part 2):

```text
A RIGOROUS REVERSIBLE FLUID WITNESS IN THE CLASS OF A FINITE CONFIGURATION SPACE WITH A2-A4, NOT A5
```

**READ:1003** · row - (-) · mechanical · edits D325, D326.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption.

Old (part 1):

```text
lattice translations; A1, A2 and A5 are stated
outright
```

New (part 1):

```text
lattice translations; the finiteness predicate `A1`, A2 and A5 are stated
outright
```

Old (part 2):

```text
satisfies A1–A5 as stated (`waveSubstratum_A1`
```

New (part 2):

```text
satisfies the finiteness predicate `A1` and A2–A5 as stated (`waveSubstratum_A1`
```

**READ:2289** · row - (-) · mechanical · edits D327, D328.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption.

Old (part 1):

```text
`HB0`: A1, A2, A3 with
degree 6
```

New (part 1):

```text
`HB0`: the finiteness predicate `A1`, A2, A3 with
degree 6
```

Old (part 2):

```text
reversible fluid witness in the
A1–A4, ¬A5 class,
```

New (part 2):

```text
reversible fluid witness in the
class of substrata with a finite configuration space satisfying A2–A4 and not A5,
```

**READ:2465** · row - (-) · mechanical · edits D329, D330.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption.

Old (part 1):

```text
link-coupled map, `A1`–`A5` on that carrier
```

New (part 1):

```text
link-coupled map, the finiteness predicate `A1` and `A2`–`A5` on that carrier
```

Old (part 2):

```text
proved **not** to be a `Substratum` satisfying `A1`, since `A1` is finiteness. `A1` is not weakened,
```

New (part 2):

```text
proved **not** to be a `Substratum` satisfying the finiteness predicate `A1`, and the finiteness predicate `A1` is not weakened,
```

**lean:525** · row - (-) · mechanical · edits D331, D332.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption.

Old (part 1):

```text
built from the second-order rule with A1, A2, A5 stated
```

New (part 1):

```text
built from the second-order rule with the finiteness predicate `A1`, A2, A5 stated
```

Old (part 2):

```text
an instance satisfying A1-A5 (Q1)
```

New (part 2):

```text
an instance satisfying the finiteness predicate `A1` and A2-A5 (Q1)
```

**lean:534** · row - (-) · mechanical · edits D333.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption.

Old:

```text
a nontrivial alphabet A1 fails at L = 0
```

New:

```text
a nontrivial alphabet the finiteness predicate `A1` fails at L = 0
```

**lean:1050** · row - (-) · mechanical · edits D336, D337, D338, D339.
Reason: R-1/R-2 are a separate PR (#1482, owner decision #1169 c.7058783437); the prose names the kernel predicate as the finiteness predicate `A1`, accurate with or without the rename, and does not present A1 as an assumption.

Old (part 1):

```text
put the carrier against A1-A5,
```

New (part 1):

```text
put the carrier against the finiteness predicate `A1` and A2-A5,
```

Old (part 2):

```text
a computed certificate: A1 is Finite (iota -> V x V)
```

New (part 2):

```text
a computed certificate: the finiteness predicate `A1` is Finite (iota -> V x V)
```

Old (part 3):

```text
the complex carrier is NOT a Substratum satisfying A1.
```

New (part 3):

```text
the complex carrier is NOT a Substratum satisfying the finiteness predicate `A1`.
```

Old (part 4):

```text
of the manuscripts or of the lift; A1 is NOT weakened
```

New (part 4):

```text
of the manuscripts or of the lift; the finiteness predicate `A1` is NOT weakened
```

**PROG:35** · row - (-) · mechanical · edits D340, D341, D342.
Reason: Live programme charter (review round 5, must-fix 3): reclassified active; owner decision #1169 c.7058374016 (repository-wide consistency): the text describes the current theory directly.

Old (part 1):

```text
and background independence (A1–A6 of the substratum programme).
```

New (part 1):

```text
and background independence (finiteness of the representative and A2–A6 of the substratum programme).
```

Old (part 2):

```text
the present roadmap does **not** assume that A1–A6 already imply:
```

New (part 2):

```text
the present roadmap does **not** assume that finiteness and A2–A6 already imply:
```

Old (part 3):

```text
The programme should not jump directly from A1–A6 to Navier–Stokes.
```

New (part 3):

```text
The programme should not jump directly from finiteness and A2–A6 to Navier–Stokes.
```

**READ:58** · row - (-) · mechanical · edits D343.
Reason: Live programme README (review round 5, must-fix 3); the programme's own target labels A1, A2 (lines 17, 56) are unrelated labels and stay.

Old:

```text
from the structural conditions A1–A6 of the manuscripts.
```

New:

```text
from the manuscripts' structural conditions on a substratum.
```

**READ:125** · row - (-) · mechanical · edits D344, D345.
Reason: Live research README corrected on main (review round 5, must-fix 3); the finite-only condition is named.

Old (part 1):

```text
A rigorous **sufficient** replacement for total finiteness in this one
recurrence step is
```

New (part 1):

```text
A rigorous **sufficient** condition, in place of finiteness of the configuration space, for this one
recurrence step is
```

Old (part 2):

```text
is one mechanism satisfying the condition. Total finiteness is another.
```

New (part 2):

```text
is one mechanism satisfying the condition. Finiteness of the configuration space is another.
```

**PROG:231** · row - (-) · mechanical · edits D358.
Reason: Owner decision 4 (#1169 c.7059136165): the frozen H-B sentence stays byte-identical, and the live one-line state that carries it states the class by its mathematical condition beside it, so that the class name does not present A1 as a premise (PREREG §25.3).

Old:

```text
OI-compatibility of the class open (`round-h-b-reversible-fluid-substratum/result.md`).
```

New:

```text
OI-compatibility of the class open (`round-h-b-reversible-fluid-substratum/result.md`). That class is the class of substrata with a finite configuration space satisfying A2–A4 as the kernel states them, with A5 failing.
```

### 6.6 Guard pins updated with the text they pin (outside the 194)

**edge:1916** · row - (-) · mechanical · edits D300.
Reason: Pins OIBridge/SubstratumSource.lean line 48, which the Lean docstring edit rewrites. Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old:

```text
ok6 &= 'does not derive a quantum architecture from A1-A6' in _subflat
```

New:

```text
ok6 &= 'does not derive a quantum architecture from the substratum conditions' in _subflat
```

**bohr:8903** · row - (-) · mechanical · edits D301.
Reason: Pins OIBridge/SubstratumSource.lean line 48. Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old:

```text
ok71 &= 'does not derive a quantum architecture from A1-A6' in _ss_txt71
```

New:

```text
ok71 &= 'does not derive a quantum architecture from the substratum conditions' in _ss_txt71
```

**edge:3357** · row - (-) · mechanical · edits D302.
Reason: Pins verification/README.md line 917. Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old:

```text
'whose A1–A6 are not `DerivedOI`', 'which is a propagation round of its own'):
```

New:

```text
'whose substratum conditions are not `DerivedOI`', 'which is a propagation round of its own'):
```

**edge:3470** · row - (-) · mechanical · edits D303.
Reason: Pins the census note of the family "manuscript axioms A1-A6". Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old:

```text
'asserts nothing about whether the witness satisfies any of A1-A6 in the manuscript sense' in _ma_fam[0]['note']
```

New:

```text
'asserts nothing about whether the witness satisfies any of these conditions in the manuscript sense' in _ma_fam[0]['note']
```

**edge:3478** · row - (-) · mechanical · edits D304, D305.
Reason: Pins verification/README.md lines 928 and 951. Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old (part 1):

```text
'no manuscript-level A1–A6 conjunct is presently a faithful predicate of the bare theory',
```

New (part 1):

```text
'no manuscript-level conjunct of these conditions is presently a faithful predicate of the bare theory',
```

Old (part 2):

```text
'asserts nothing about whether the witness satisfies any of A1–A6 in the manuscript sense'):
```

New (part 2):

```text
'asserts nothing about whether the witness satisfies any of these conditions in the manuscript sense'):
```

**edge:9733** · row - (-) · mechanical · edits D306.
Reason: Pins the glossary entry gloss:13 = FULL:6504, which D220/D221 rewrite. Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old:

```text
The sixth of the framework's structural assumptions "
                   'A1–A6: the substratum dynamics
```

New:

```text
The structural assumption A6 of the "
                   'reconstruction theorem (A2–A6): the substratum dynamics
```

**bohr:8928** · row - (-) · mechanical · edits D307.
Reason: Message of check F71, which states the pinned SubstratumSource.lean sentence. Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old:

```text
"A1-A6 or the read-write substratum dynamics -- the round reduces the three principles to "
```

New:

```text
"the substratum conditions or the read-write substratum dynamics -- the round reduces the three principles to "
```

**edge:1908** · row - (-) · mechanical · edits D308.
Reason: Comment describing the SubstratumSource.lean pin at line 1916. Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old:

```text
# with the diagonal countermodel; no derivation from A1-A6 claimed.
```

New:

```text
# with the diagonal countermodel; no derivation from the substratum conditions claimed.
```

**edge:3369** · row - (-) · mechanical · edits D346.
Reason: Code comment, active material under AGENTS.md §A.48: states the current wording of what the guard checks. Guard pin updated in the execution commit with the text it pins (the probe runs in the required Numerical probes check).

Old:

```text
# ---- The manuscript-axiom pass: A1–A6 preregistered before the proof with a representability
# verdict each, A1 and A2 closed under faithful forms,
```

New:

```text
# ---- The manuscript-axiom pass: the substratum conditions preregistered before the proof with a representability
# verdict each, finiteness and A2 closed under faithful forms,
```

**edge:9456** · row - (-) · mechanical · edits D347.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a code comment is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the R7-HYB header comment names the class.

Old:

```text
# witness in the A1-A4, not-A5 class,
```

New:

```text
# witness in the class of a finite configuration space with A2-A4, not A5,
```

**edge:10903** · row - (-) · mechanical · edits D348.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a code comment is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the R7-A6I header comment lists the readings the guard rejects.

Old:

```text
# gauge-group derivation; A1 weakened so that the complex carrier fits;
```

New:

```text
# gauge-group derivation; the finiteness condition weakened so that the complex carrier fits;
```


**edge:3489** · row - (-) · mechanical · edits D351.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a check message is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the R7-MAX message describes the record's realized-core images.

Old:

```text
'with the preregistration commit named, records the A1 and A2 realized-core images as holding '
```

New:

```text
'with the preregistration commit named, records the realized-core images of finiteness and A2 as holding '
```

**edge:3493** · row - (-) · mechanical · edits D352.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a check message is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the R7-MAX message describes the record's non-claim.

Old:

```text
'refuted, and asserts nothing about the witness against A1–A6 in the manuscript sense or about '
```

New:

```text
'refuted, and asserts nothing about the witness against the substratum conditions in the manuscript sense or about '
```

**edge:3756** · row - (-) · mechanical · edits D353.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a check message is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the R7-SUB message lists the kernel predicates the module defines.

Old:

```text
it defines A1, A2, A3, A3Family, A4Exact, A4 and A5 verbatim as pinned
```

New:

```text
it defines the finiteness predicate, A2, A3, A3Family, A4Exact, A4 and A5 verbatim as pinned
```

**edge:9599** · row - (-) · mechanical · edits D354.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a check message is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the R7-HYB message names the class.

Old:

```text
'witness named in the A1-A4, not-A5 class, the admissibility of that class recorded OPEN -- '
```

New:

```text
'witness named in the class of a finite configuration space with A2-A4, not A5, the admissibility of that class recorded OPEN -- '
```

**edge:10967** · row - (-) · mechanical · edits D355.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a check docstring is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the docstring of check I17 describes cx3b_complex_not_A1.

Old:

```text
the PROVED FAILURE of
    A1 on the complex carrier."""
```

New:

```text
the PROVED FAILURE of
    finiteness on the complex carrier."""
```

**edge:11019** · row - (-) · mechanical · edits D356.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a check docstring is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the docstring of check I22 describes the ROADMAP section.

Old:

```text
the carrier staying outside, A1
    not weakened,
```

New:

```text
the carrier staying outside, the finiteness
    predicate not weakened,
```

**edge:11266** · row - (-) · mechanical · edits D357.
Reason: Owner decision 5 (#1169 c.7059136165): a guard keeps an A1 string only as a technical pin with a named target, a stated purpose and a passing test against that target; a check message is documentation, not a pin, so it states the condition by name (PREREG §25.4). Here: the R7-A6I message describes cx3b_complex_not_A1.

Old:

```text
'A1 at the complex carrier. The four readings are checked never identified.
```

New:

```text
'finiteness at the complex carrier. The four readings are checked never identified.
```

## 7. Hidden dependencies found

- **H-1, GR:673.** The line prints "OI's full structural conditions A1–A6 except at S3: A1 (finiteness) …"
  but the ledger classifies it FREE (P0 class), so it is not among the 194 sites. Drafted as D243
  (mechanical range and label rewrite). The ledger's map should carry it at reconciliation.
- **H-2, Sub:56 on S2-D's branch.** S2-D prints "Without A1 the question also concerns an incoming supply"
  (X-63/X-82). At deletion the pointer becomes the property it names (D244, "Without finiteness"); S2-D's
  content is unchanged.
- **H-3, appC:136/138 = FULL:6289/6293.** "Trivially computable" and "in-principle computable" use
  finiteness (a lookup table). D218 attaches the finite scope to the computability sentence and D246 keeps
  it at :138, dropping "which is the relevant claim for foundational physics" with the narrowing. A
  size-independent form would need uniformity of the rule as a named hypothesis and is not drafted.
- **H-4, Sub:92 is Substratum's only statement of (NR).** Deleting the (A1) entry would drop the weaker
  condition and its S2-C qualification from Substratum silently. D245 relocates the clause verbatim to the
  Stage 1 recurrence sentence at Sub:137 (J row X-20; deletion criterion 3).
- **H-5, Lean-manuscript census registry.** `verification/lean-manuscript-census.json` notes quote the
  manuscripts' "A1-A6" statements (the Route B note on GR:261's "not entailed by A1-A6"; the family
  "manuscript axioms A1-A6", kernel-only, no manuscript anchor). The census resolves identifiers, not
  prose, so no gate fails; the notes are corrected in the execution commit (§A.25 step 5, §A.35). The Lean
  predicate `SubstratumInterfaceAudit.A1` and its theorems (X-81) are finite-only kernel statements and are
  not renamed; no manuscript cites them after the edit (residual scan, §10).
- **H-6, coverage fingerprints.** The execution changes passages fingerprinted in
  `verification/coverage/LEDGER.json` (Main, Substratum, SM, GR, Structure); re-affirmation is a
  post-execution check (§11).
- **H-7, Theorem 23's finite scope versus S2-A.** S2-A prints A4 with $\mathbb{Z}^d$ as the standard
  construction; Theorem 23 keeps a finite-substratum scope (X-45: Stage 1 exact return, Stage 3 count). A
  finite substratum satisfying A4 is necessarily a finite periodic quotient, which D022 states; review item.
- **H-8, the posit list at M:60.** After the deletion M:60 is Main's first mention of (NR), (IP) and (IL);
  D229 and D254 print S2-C's qualifications there (resolved in round 1, F3).
- **H-9, the finite OI class (X-46).** Resolved by owner ruling (#1169 c.7057674976): the class stays a finite
  subclass, named "finite OI class" where necessary; the X-46 rewrites word finiteness as its scope; the
  cardinality-neutral class is Issue #1478.
- **H-10, `verification/README.md`, and H-11, the Lean docstrings.** Superseded by the repository-wide
  consistency decision (§22): the active text describes the current theory directly, without pinned-commit
  scoping. The README, registry, coverage-ledger, Lean-docstring and guard edits are in §6.4–§6.6.
- **H-12, guard pins.** `verification/lean/edge_rigidity_probe.py` (the R7 guard, run in the required
  Numerical probes check) and `bohr_frequency_probe.py` pin exact strings of the glossary A6 entry, of
  `verification/README.md`, of the registry and of `OIBridge/SubstratumSource.lean`. Eight such pins break
  under the edit list; each is updated by a guard-pin edit (§6.6). `edits_check.py --pins` finds them by
  comparing the string literals of every tracked Python check with the edited files (0 unresolved).

## 8. Dependency and conflict map against the Step-2 PRs

| Unit | PR | Head used | Edits that depend on it |
|---|---|---|---|
| S2-A | #1470 | `dd95fcd0` | D036 (SM:222: the replacement continues into S2-A's wording); D022, D120–D121 (Theorem 23 scope alongside the $\mathbb{Z}^d$ A4 wording) |
| S2-B | #1473 | `5c6cdfea` | D224 (item (ii) text on the branch), D229 (moved list includes S2-B's CP clause), D231 (transfer clause follows S2-B's deep-sector sentence), D232 (Sub:92 text), D005, D029 |
| S2-C | #1474 | `cb6d1b87` | D224, D232 (text on the branch), D245 (relocated S2-C wording), D004 (M:131 qualification), D045, D108–D111, D200–D201 |
| S2-D | #1472 | `5efd856b` | D244 (Sub:56 wording on the branch); D251–D252 keep S2-D's ch18:40 decision |
| S2-E | #1475 | `7ed84339` | D248–D252 (sites S2-E defers to the deletion edit); the 35 Phase-3 residual pointer lines at the base are removed by S2-E's edits, which leave zero on the projection |

Line-level dependencies (an `old` string on a line a Step-2 unit changes, or a replacement presupposing
Step-2 text):

| Edit | Site | Step-2 units changing the line | Variant used on the projection | What the edit presupposes |
|---|---|---|---|---|
| D005 | M:224 | S2-B, S2-C, S2-D, S2-E | old | S2-B, S2-C change later words of the line |
| D029 | Sub:268 | S2-B, S2-C, S2-D, S2-E | old | S2-B changes later words of the line |
| D036 | SM:222 | S2-A, S2-B, S2-C, S2-D, S2-E | old | S2-A changes the words after the old string |
| D045 | GR:589 | S2-C, S2-D, S2-E | old | S2-C appends a sentence |
| D108 | ch01:179 | S2-C, S2-D, S2-E | old | S2-C inserts between the two old strings |
| D109 | ch01:179 (FULL) | S2-C, S2-D, S2-E | old | S2-C inserts between the two old strings |
| D110 | ch01:179 | S2-C, S2-D, S2-E | old | S2-C inserts between the two old strings |
| D111 | ch01:179 (FULL) | S2-C, S2-D, S2-E | old | S2-C inserts between the two old strings |
| D200 | appC:104 | S2-C, S2-D, S2-E | old | S2-C changes later words of the line |
| D201 | appC:104 (FULL) | S2-C, S2-D, S2-E | old | S2-C changes later words of the line |
| D224 | M:732 | S2-B, S2-C, S2-D, S2-E | old_step2 | S2-B and S2-C edit inside item (ii); old_step2 is item (ii) on the projected integration |
| D225 | M:732 | S2-B, S2-C, S2-D, S2-E | old | S2-B and S2-C edit inside item (ii); old_step2 is item (ii) on the projected integration |
| D226 | M:732 | S2-B, S2-C, S2-D, S2-E | old | S2-B and S2-C edit inside item (ii); old_step2 is item (ii) on the projected integration |
| D227 | M:732 | S2-B, S2-C, S2-D, S2-E | old | S2-B and S2-C edit inside item (ii); old_step2 is item (ii) on the projected integration |
| D228 | M:732 | S2-B, S2-C, S2-D, S2-E | old | S2-B and S2-C edit inside item (ii); old_step2 is item (ii) on the projected integration |
| D253 | M:732 | S2-B, S2-C, S2-D, S2-E | old | S2-B and S2-C edit inside item (ii); old_step2 is item (ii) on the projected integration |
| D229 | M:60 | S2-B, S2-C, S2-D, S2-E | old | S2-B wording ("and for the P-indivisibility input of the CP-indivisibility theorem") is presupposed |
| D230 | M:60 | S2-B, S2-C, S2-D, S2-E | old | S2-B wording ("and for the P-indivisibility input of the CP-indivisibility theorem") is presupposed |
| D254 | M:60 | S2-B, S2-C, S2-D, S2-E | old | S2-B wording ("and for the P-indivisibility input of the CP-indivisibility theorem") is presupposed |
| D231 | M:60 | S2-B, S2-C, S2-D, S2-E | old | S2-B wording ("and for the P-indivisibility input of the CP-indivisibility theorem") is presupposed |
| D232 | Sub:92 | S2-B, S2-C, S2-D, S2-E | old_step2 | S2-B and S2-C edit inside the entry; old_step2 is the projected entry |
| D244 | Sub:56 | S2-D, S2-E | old_step2 | — |
| D248 | Comp:120 | — | old | deferred to the deletion edit by S2-E |
| D249 | Meth:156 | — | old | deferred to the deletion edit by S2-E |
| D250 | Meth:158 | — | old | deferred to the deletion edit by S2-E |
| D251 | ch18:40 | — | old | deferred to the deletion edit by S2-E |
| D252 | ch18:40 (FULL) | — | old | deferred to the deletion edit by S2-E |

**Conflicts.** None between this edit list and any Step-2 head: each `old` string (or `old_step2`) is
unique on the projection. The S2-B × S2-C shared lines (M:224, M:732, Sub:92) conflict with each other at
line level and are combined in the projection; their final merged wording is what §9 re-pins against.

## 9. Reconciliation procedure before execution

Run at the exact head `H` of `main` after S2-A to S2-E have landed and after the ledger reconciliation, and
before any execution is authorized:

1. Record `H` and the merge commit of each Step-2 PR.
2. `python3 -I -B verification/audits/foundations/a1exit-deletion-20261121/edits_check.py --commit H --simulate`.
   Every edit must find exactly one occurrence of `old` or `old_step2`; the residual pointer scan must report
   zero unqualified lines.
3. For every edit that fails, or whose site a Step-2 unit or a later commit changed (§8), redraft the
   `old` string from `H` and re-derive `new` by the same rule and from the same ledger row; record each
   change as an amendment under `amendments/` with the reason. A redraft may not change a replacement's
   claim, scope or class without a new review.
4. Rebuild the ledger site map at `H` (`ledger_check.py build`) and re-pin: every ptr site of the rebuilt
   map must have an edit, and every edit must map to a site or to §6.2/§6.3; new pointer sites found by the
   rebuild are drafted by the same rules before execution.
5. `edits_check.py --pins --commit H` (0 unresolved pins) and `edits_check.py --repo-scan --simulate --commit H`
   (0 unexplained lines; lines pending an owner decision listed) are mandatory.
6. `edits_check.py --static`: infinity-assertion scan 0 hits, register scan 0 hits, identifier rule 0
   findings, sitemap cross-check complete (194 ptr sites, or the re-pinned count with the difference
   explained), and, mandatory before execution: the **mirror-parity check** (every chapter edit byte-identical
   to its FULL mirror in `old`, `new` and their Step-2 variants, and every chapter edit mirrored) and the
   **preservation check** (D022/D120/D121 keep the finite scope and the wrapping-conditions clause; D229 keeps
   "each assumed as a hypothesis of that result and not adopted", S2-C's return and law forms and "reversibility
   (REV)"; D254 and D245 keep the (NR) qualification; D253 keeps the completeness clause), each with 0
   findings. The `--simulate` run of step 2 also checks that item (iii) of Main's posit ledger keeps "(REV)".
   A redraft under step 3 that fails either check is not executed.
7. Owner questions in §12 are answered and recorded.
8. The reconciled list, with its checker output at `H`, goes to independent review before the execution is
   authorized.

## 10. Checks run at drafting

| Command | Tree | Result |
|---|---|---|
| `edits_check.py --self-test` | — | self-test PASS (93 countercontrols) |
| `edits_check.py --pins --commit 97070c98` | merged `main` | pins check: 0 unresolved pins (literals of tracked checks that the edits would break); 0 updated pins not found in their targets |
| `edits_check.py --repo-scan --simulate --final --commit 97070c98` | merged `main` | repository-wide scan: 0 unexplained lines; RESULT PASS |
| `edits_check.py --static` | — | infinity-assertion scan (new and new_step2): 0 hits; register scan (added text, §A.32/§A.33, history phrases): 0 hits; new capitals (3+ letters): 0; identifier rule (new and new_step2): 0 findings; preservation check (required content in every replacement variant): 0 findings; mirror parity (every chapter edit byte-identical to its FULL mirror): 0 findings; sitemap cross-check: 194 ptr sites in the map, 194 with an edit; 0 findings; RESULT PASS |
| `edits_check.py --commit 97070c98` | base | uniqueness: 373 edits, 0 fail; variants used {'old': 373}; RESULT PASS |
| `edits_check.py --commit 97070c98 --simulate` | base | uniqueness: 373 edits, 0 fail; variants used {'old': 373}; simulation: residual pointer lines 5 (5 allowed as listed, 0 unqualified); simulation: criterion-5/paraphrase hits on changed lines without a scope in their sentence: 0; simulation: finite-scope and configuration-space preservation findings: 0; simulation: identifier and count findings: 0; RESULT PASS |
| `edits_check.py --tree <projection> --simulate` | projected integration (pre-merge) | (projection retired at reconciliation; see §24) |
| `guards_check.py --mutants` | simulated post-deletion tree of merged `main` | §25.6: the guards and readers pass; CC-1–CC-4 fail as named; pins P01–P30 and the three declaration names each fail under mutation; RESULT PASS |
| `preserve_check.py --verify-ledger`, `--self-test`, `--tree <simulated tree>` | ledger base `97070c98` | §25.6: RESULT PASS each |

The residual lines at the base are the S2-E Q3 sites (Comp, Meth, ch14, ch18 and their FULL mirrors), which
S2-E's branch rewrites, and the one identifier finding at the base is the "A1–A6" range in Methodology (an
S2-E site); on the projection, after the edit list, the residual is zero apart from the ledger's
false positives (the appB anomaly conditions "(A1)" and their FULL mirror) and GR:58's finite-scope wording
"For a finite total system", which the P2 pattern matches.

**Extended criterion-5 patterns added by replacement strings.** "finite model" (X5) in D043 (GR:257, "in
its finite model", ledger X-75 wording) and "finite universe" (X5) in D192–D195 (appC:16 and the §C.6
heading, in the question "does the framework assume a finite universe?"). Each is finite-scoped or
interrogative; no replacement adds X1–X4 hits.

## 11. Post-execution checks (preregistered)

At the execution head, all of the following, with outputs recorded in the execution record:

1. `edits_check.py --commit <execution head>` reports every `new` string present (the `old` strings absent);
   the residual pointer scan of the executed tree reports zero unqualified lines.
2. Ledger re-pin: `ledger_check.py build` then `ledger_check.py check` (CK1–CK8 PASS, extended scan CK4x
   0 unmapped). The extended criterion-5 scan has zero unqualified hits: every hit is finite-scoped,
   interrogative, or a stated open statement.
3. Build: `sh ./build.sh Main Substratum SM GR Structure Computation Methodology` and `sh ./build.sh --book`;
   no dropped glyphs; page count and median characters per page recorded against the pre-execution build.
4. Coverage: `python3 tools/coverage_check.py`; the edits make four entries of `verification/coverage/LEDGER.json`
   stale, and each is re-affirmed in the execution commit: `MAIN:L-3` (Lemma 3: D260, and the measure remark D309),
   `STRUCTURE:P-9.5` (Proposition 9.5 in the finite OI class), `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer`
   (the corollary at Sub:268, D029) and `SUBSTRATUM:T-23` (Theorem 23: D022). For `MAIN:L-3` and `SUBSTRATUM:T-23` the
   entry's level and delta are re-read against the new statement (a finite-representative scope; the finite-substratum
   scope with the wrapping conditions), not only the fingerprint; the other changed fingerprints are re-affirmed as
   the Step-2 units did (H-6).
5. Register scan of the diff's added lines (§A.32, §A.33): meta-commentary, reader instruction,
   revision-history words, capitals for emphasis: zero hits.
6. Infinity-assertion scan of the diff's added lines: zero hits (owner decision, item 6).
7. Corpus grep for `\bA1\b`, "total-finiteness", "posit (ii)", "item (ii)", "finiteness posit": only the
   ledger's false positives remain; grep of posit counts ("Fourteen", "six structural", "sixth of"): zero.
8. Mirrors: each chapter edit and its FULL mirror byte-identical.
9. The census registry notes (H-5) updated in the same commit.
10. Lean: the docstring-only check of `edits_check.py --static` passes for every Lean docstring edit (the
    edited file equals the original outside comments), and the Lean kernel build, the Mathlib build and the
    existing CI pass at the execution head.
11. Repository-wide audit (§22): `edits_check.py --repo-scan --final --commit <execution head>` reports zero
    unexplained lines over all tracked active files, with the exclusions it lists (historical records,
    generated artifacts, unrelated labels, guard pins, kernel identifiers kept by an owner decision), and no
    line pending an owner decision.
12. Pins: `edits_check.py --pins --commit <execution head's parent>` reports 0 unresolved pins and 0 updated pins
    missing from their targets; `guards_check.py --mutants` passes on the simulated tree; the R7 guard and
    `bohr_frequency_probe.py` pass in CI at the execution head.
13. SC-42 integration result. The book edits change the mirror prefixes that
    `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` stores
    (measured on a scratch copy of `97070c98` with all edits applied: the checks go from 1,961 to 1,971, with 26
    entries added and 16 removed, every one a "chapter line mirrored in FULL" prefix, every check `ok`, no failed
    predicate and every other field of the result unchanged; the unedited copy, the control, reproduces the
    checked-in result byte for byte; the acceptance review counted 21 and 15 before D349–D350 were added). The execution commit regenerates the file under the procedure and
    safeguards of S2-D (#1169 comment 7057200720): with `R` that directory,
    `python3 -I -B $R/check_sc42_integration.py > out.json` (exit 0) is copied to the result file;
    `python3 -I -O -B $R/check_sc42_integration.py` is byte-identical to it; `--verbose`, normal and with `-O`, is
    byte-identical to the regenerated file (the CI comparison); `--self-test`, normal and with `-O`, is
    byte-identical to the unchanged `$R/sc42-integration-controls.json` (run in a full checkout: the scratch export
    cannot decide it, its self-test differing from the controls even on the unedited control copy); every line of the diff is a stored mirror
    prefix of a line the deletion's book edits change, with every check result unchanged; and an independent
    verification of the regenerated file follows. The regeneration needs the owner's narrow approval as part of
    the execution authorization.
14. Preservation: `preserve_check.py --commit <execution head>` (with `--base <main>` if `main` has moved) reports 0
    findings, and the safeguards of §25.2 are met.

## 12. Owner questions

Answered (#1169 comment 7057674976):

1. **ch18:40.** Pointer-only rewrite approved, narrowly scoped. D251–D252 replace "which is recurrent under
   A1 (§18.7)" by "which is recurrent (§18.7)": the sentence already says "the finite reversible substratum
   dynamics", which is the finite-recurrence condition; physical content and conditional scope unchanged.
2. **The finite OI class.** Kept as a finite subclass, "finite OI class"; finiteness worded as its scope
   (review F8); cardinality-neutral class in Issue #1478.

3. **H-11.** Decided (a) (#1169 comment 7058343268), then superseded by the repository-wide consistency
   decision (#1169 comment 7058374016): the Lean docstrings describe the current theory directly (§22).

Answered (#1169 comment 7058783437):

4. **R-1 and R-2.** A separate follow-up PR (Issue #1482), not part of the deletion. The plan keeps the
   docstring edits, and every README, registry and Lean prose line that names the predicate calls it "the
   finiteness predicate `A1`" (D314–D339), accurate with or without the rename.
5. **R-C.** The family name "manuscript axioms A1-A6" is kept; its note is rewritten (D293–D294).
6. **AGENTS.md:38.** Approved (D296): only the retired posit leaves the list.
7. **Book mirrors.** Included: ch01 (D310–D311) and ch02 (D114–D115, the owner's sentence in place of D114's
   own wording), with FULL mirrors; ch01's Lemma 3 takes the finite scope (D312–D313).

No owner question is open; the declaration-name pins are ruled on (#1169 comment 7059632884, §25.4). The frozen H-B sentence stays unchanged (§25.3).

## 13. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| Step-2 branch heads (§1) | The `old_step2` strings and §8 dependencies | provenance: the strings are re-pinned against merged `main` before execution (§9); nothing here is established from them |
| PR #1470, #1472, #1473, #1474 | Unit identities | provenance |
| #1169 comments 7057236079, 7057297534, 7057200720, 7057674976, 7058343268 | Authorization, design decision, landing order, rulings on §12 | provenance (owner records) |
| Issue #1478 | The cardinality-neutral OI class, outside this edit | provenance (planning) |
| Issue #1482 | The Lean identifier renames R-1/R-2, outside this edit | provenance (planning) |
| #1169 comment 7058783437 | The five decisions and the reconciliation gate | provenance (owner record) |
| #1169 comment 7059136165 | Decisions 2–5 answered in §25 | provenance (owner record) |
| #1169 comment 7059632884 | Ruling on the declaration-name pins (§25.4) and the sole writer of #1477 | provenance (owner record) |
| #1477 round-5 review record (c.7058814130) | The findings closed in §25.1 | provenance |
| Issue #1479 | Stage 2 of Theorem 23 on $\mathbb{Z}^d$, deferred | provenance (planning; accountable home of the deferred item) |
| #1477 round-1 review record | The findings answered in §17 | provenance |
| Projected integration (scratch) | Uniqueness on the projection | provenance: reproducible from the heads by §14 |

## 14. Reproducibility

- `edits.json` is the edit list; `edits_check.py` (standard library only) checks it. Neither writes a
  manuscript.
- Base checks: `python3 -I -B verification/audits/foundations/a1exit-deletion-20261121/edits_check.py --self-test`,
  `--static`, `--commit 97070c98 --simulate`.
- Simulated post-deletion tree: `python3 -I -B .../guards_check.py --mutants` (needs `numpy` and `scipy`; about six
  minutes). Ledger and preservation: `python3 -I -B .../preserve_check.py --verify-ledger`, `--self-test`,
  `--tree <dir>` or `--commit <rev>`.
- Projection: for each `.md` file under `papers/` and `book/` that a Step-2 head changes, merge the head into
  `main`'s file with `git merge-file` (base: the merge base), in the order S2-A, S2-B, S2-C, S2-D, S2-E;
  resolve the three line-level conflicts by taking both units' word edits; write the result with the
  unchanged files to a directory and run `edits_check.py --tree <dir> --simulate`.

## 15. Verification status (§A.46 item 4)

- **Evidence level.** Exhaustive lexical checks of the edit list against the base and a projection
  (uniqueness, residual scan, infinity and register scans, identifier rule). The rewrites themselves are
  unreviewed drafting.
- **Missing.** Independent review of the edit list; the §5 scientific reviews; reconciliation against merged
  `main` (§9); owner answers to §12.
- **Accountable Issue.** #1169.
- **What resolves it.** An independent review recorded on the guiding PR, the §9 reconciliation at the
  merged head, and a separate owner authorization of the execution.

## 16. Limits

The edit list covers the 194 pointer sites, item (ii) and the consistency corrections found by the residual
scan. It does not re-audit any ledger row, change any Step-2 conclusion, or decide the regression audit
(#1468). A lexical scan cannot find a finiteness dependency that no word names; the J/F/O classifications
are the ledger's.

`--pins` reads the string literals of tracked Python checks only: a pin built at run time (formatted strings,
regular expressions, text assembled from parts) or a "must not contain" check is not modelled, and the guards
themselves are run by `guards_check.py` on the simulated post-deletion tree (§25), with the bounded checks that
read an edited file; the checks it does not run (§25.6) run in CI on the exact tree of §25.2, and the guards' pass at
the execution head is a precondition of landing.

## 17. Answer to the early review of `36a73526` (round 1, REVISE)

| Finding | Change |
|---|---|
| F1 Theorem 23 parenthesis, wrapping conditions, paper/book parity, Stage 2 on $\mathbb{Z}^d$ | D022 and D120 read "with A4 applying in its finite periodic case under the wrapping conditions on $P$ of Stage 2 [SM §4.1]" (book: "(SM §4.1)", its citation style); the $\mathbb{Z}^d$ restatement of Stage 2 is a §5.4 review item, not part of this edit, being beyond the smallest correction |
| F2 Sub:129 scope | D020 drops A1 with no replacement scope (C4 from the hidden-memory theorem, C1 from the history gap; the readback route constructs a finite hidden space, M:60); class mechanical |
| F3 M:60 qualifications | D229 prints S2-C's return- and law-form qualifications; D254 qualifies the later (NR) mention; §5.3 lists D224 and D229 |
| F4 completeness sentence | D253 |
| F5 appC:136/138 | D218 attaches the finite scope to the computability sentence; D246 keeps it and drops "the relevant claim for foundational physics" |
| F6 "finite in a finite representative" | Replaced at D012, D014, D015 (Sub:52 parenthesis deleted), D114, D176, D210, D222; none remains in any `new` string |
| F7 README and Lean docstrings | H-10 (README corrected in place at execution), H-11 (owner question 3) |
| F8 finiteness as membership | Str:258 (D060), Str:260 (D062), ch02:74 (D239), ch09:104 (D255), ch09:190 (D257); Structure's class wording follows the owner ruling (D046, D053, D057, D072, D073, D075, D080, D092, D093, D095; ch03:44 D138) |
| F9 glossary entry | D237: "of a finite hidden dynamics" |
| F10 reasons | D001's reason corrected; D250 reads "rests on the posit (REV)" |
| Checker: infinity scan | Adds "is not finite", "\|S\| = ∞/\infty", "thermodynamic limit", "unbounded size"; the exemption is only the symmetric "neither … is finite nor … is infinite" form |
| Checker: register scan | Adds the history-phrase family and capitals of three or more letters (with an acronym list) |
| Checker: identifier rule | `--simulate` checks that Main's posit ledger keeps (i) and (iii)–(xiv), prints no (ii) and says "Thirteen items … thirteen", and that the six/five counts read five; `--static` flags "Fourteen", ranges renumbered to (xiii), numeric posits and A1-ranges |
| Checker: residual scan | Adds the paraphrase pointers (e.g. "configuration finiteness … open physical hypothesis"); criterion-5 and finiteness-paraphrase hits on changed lines must be scoped in their sentence; files are listed from the commit or tree under test |
| Checker: static mode | Scans `new` and `new_step2` |
| Checker: sitemap | `--static` cross-checks every ptr edit against `sitemap.json` at its pin (declared site, part-1 line, mirror line; every ptr site covered) |
| Checker: self-test | Every fault injection of the review is a countercontrol (§10) |

## 18. Answer to the delta review of `67736e55` (round 2, ACCEPT-WITH-NITS)

| Item | Change |
|---|---|
| Must-fix 1: accountable home for Stage 2 on $\mathbb{Z}^d$ | Issue #1479, cited in §5.4 and in D022's reason |
| Must-fix 2: H-11 | Open; put to the owner (§12, question 3). If (a) is chosen, the docstring edit of `OIBridge/ManuscriptAxioms.lean` is drafted as a further amendment |
| Must-fix 3: mirror parity and preservation | Both checks added to `--static` with countercontrols, and made mandatory in §9 step 5; the posit-ledger simulation also checks that item (iii) keeps "(REV)" |
| Must-fix 4: §9 at the merged head | Unchanged: it runs after the Step-2 landings |
| Nit: ch09:104 | D255/D256: "are, for the finite OI class, five structural properties of the substratum; finiteness, stated first, is that class's scope. They are organized as follows." |
| Nit: infinity paraphrases | Added "no finite bound", "of infinite extent", "extending without end", "non-finite", "infinitely extended" and "Finiteness … fails"; the scan counts assertions a replacement introduces, reading A1 in the old string as finiteness, so the per-program statements of Structure §6 and §13.1.4 ("Finiteness fails for continuum BFSS") are not new assertions |
| Nit: history phrases | Added "Earlier versions", "originally (a posit)", "at one time", "hitherto" |
| Nit: SCOPED | Split into strong scopes and weak markers ("?", "whether", "open", disclaimers); a weak marker no longer exempts a sentence that asserts finiteness of the universe, nature, the substratum or $S$, and such assertions on changed lines are scanned |
| Nit: "item ii" | The identifier rule catches "item ii" and "posit ii" without parentheses |

## 19. Answer to the delta review of `a58cf594` (round 3, ACCEPT-WITH-NITS)

| Item | Change |
|---|---|
| Infinity comparison by content | The scan compares the multiset of normalized matched assertions in `new` against `old` (A1 read as finiteness), not their counts; "finiteness … fails" is anchored so that "fails to" does not match. Countercontrols: D065 rewritten to "The substratum is infinite for continuum BFSS" is flagged; the kept per-program "finiteness fails" sentences pass |
| `$S$` boundary | ASSERTS_FINITE uses `(?<!\w)` before its subject; countercontrol: "$S$ is finite" under a weak marker is caught |
| "finite configuration space … open matter" | A hit on "finite configuration space" or "finite cardinality" is exempted only by a strong scope, never by a weak marker; countercontrol added |

## 20. Answer to the round-4 check of `f18c8677` (ACCEPT, one non-blocking nit)

| Item | Change |
|---|---|
| Bare "on a finite" / "for a finite" scopes | Each is tied to an object: `(?:on\|for) a (?:fixed )?finite (?:\w+ )?(?:representative\|substrat\w*\|model\|set\|system\|realization)`, with "for a finite $S$" and "when $S$ is finite" kept. Countercontrol: "a deterministic bijection on a finite configuration space, an open matter for physics" is caught. The tightening exposed one unchanged sentence on a changed line, Str:339, which describes causal dynamical triangulations "with manifestly finite configuration space"; it is about another programme, not the OI substratum, and is listed in the checker's criterion-5 allow list with that reason |

## 21. Amendment: H-11

H-11 was decided (a), correct the Lean docstrings in place (owner `amaybaum`, 2026-11-21,
[#1169 comment 7058343268](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7058343268),
2026-11-21T06:03:01Z). Its instruction to scope the quotation to a pinned commit is superseded by the
repository-wide consistency decision (§22), which the owner recorded as replacing it: the docstrings
describe the current theory directly. The draft Lean edits are D262–D286 (§6.4), docstring only.

## 22. Amendment: repository-wide consistency after A1 is retired

**Owner decision** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7058374016](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7058374016),
2026-11-21T06:05:53Z, "Owner decision record: repository-wide consistency after A1 is retired"), quoted in
part:

> **This supersedes the H-11 guidance** in #1169 comment 7058343268, which scoped the Lean docstring
> quotation to a pinned commit. After A1 is removed, the current theory must be internally consistent. No
> outdated statement or comment may suggest that A1 is still an assumption. Earlier guidance to keep old
> wording in active documentation is withdrawn as too conservative.
>
> - **Manuscripts and book.** Remove or rewrite every reference that treats A1 as an active assumption.
> - **Comments and documentation.** Describe the new theory directly. They do not explain that they refer
>   to an older version.
> - **Mathematical claims.** Every result that actually needs finiteness states that condition explicitly.
> - **Lean.** Update the documentation, and review every identifier that contains `A1`. Rename misleading
>   identifiers where that is safe, and verify the proofs after renaming.
> - **Cross-references.** Update assumption counts, ranges, tables and references consistently.
> - **Final audit.** Search the whole active repository for obsolete A1 references, not only the 194
>   manuscript pointers already identified.
>
> - **Historical research records and Git history are preserved.** They document how the results were
>   established. They must not be mistaken for descriptions of the current theory.
> - **Valid finite-only results are kept.** They are not deleted because they originally relied on A1. Each
>   states its actual conditions.
>
> ### Completion criterion
> > A reader encountering the current OI theory should find no outdated assertion that A1 is an active
> > assumption, no unexplained dependency on A1, and no misleading references to the retired assumption.
> > All surviving finiteness requirements must be stated explicitly where needed.

### 22.1 Scan and classes

`edits_check.py --repo-scan` scans every tracked file of a commit for `\bA1\b`, "total finiteness",
"finiteness posit", "posit (ii)" and "A1–A6", and classifies each line:

| Class | Rule | Disposition |
|---|---|---|
| historical record (AGENTS.md §A.48 item 2) | under `verification/audits/`, `verification/programmes/`, `verification/infrastructure/`, `verification/receipts/`, `verification/seals/`, `verification/certificates/`, `evidence/`; or `verification/ROADMAP.md` (frozen), `verification/MIGRATION-MANIFEST.md`, `verification/migration-manifest.json` (grandfather list) | preserved; a mutable index presenting a record as current theory is corrected instead (the README and registry edits) |
| generated artifact | `papers/*.tex`, `papers/*.pdf`, `book/*.tex`, `book/*.pdf` | regenerated by `build.sh` |
| manuscript | `papers/*.md`, `book/*.md` | the edit list (§6.1–§6.3) |
| unrelated label | listed files or substrings: the A1 irrep, local variables, roadmap item A1, amendment or finding labels, the appB anomaly condition (A1) | kept; the reason is recorded per entry in the checker |
| guard pins | `edge_rigidity_probe.py`, `bohr_frequency_probe.py` | kept as pins of records and kernel identifiers; the pins the edits break are updated (§6.6; `--pins` 0) |
| kernel identifier | every A1 on the line is a Lean declaration name (`A1Realized`, `waveSubstratum_A1`, `` `A1` ``, …) or the programme label `A1-RIGID-1` | kept pending §22.4 |
| pending R-1 / R-C | listed lines of kernel-predicate prose and the registry family name | resolved by the owner decisions of §12 (questions 4, 5); `--final` rejects them |
| unexplained | anything else, which is active material under §A.48 item 1 (live programme charters and READMEs under `verification/programmes/` included) | must be rewritten: zero is required at execution |

### 22.2 Inventory

Lines matching the scan patterns at current `main` (`97070c98`), as is and after the in-memory application of the edit list:

| Class | Area | As is | After the edits |
|---|---|---|---|
| generated artifact | book | 63 | 63 |
| generated artifact | papers | 105 | 105 |
| guard pins | verification | 51 | 31 |
| historical record | verification | 4015 | 4015 |
| historical record label | tools | 1 | 1 |
| kernel identifier | verification | 12 | 33 |
| manuscript | book | 103 | 0 |
| manuscript | papers | 85 | 0 |
| preserved historical evidence | verification | 2 | 3 |
| pending R-1 | verification | 8 | 0 |
| registry identifier (kept) | verification | 1 | 1 |
| unexplained | AGENTS.md | 1 | 0 |
| unexplained | verification | 52 | 0 |
| unrelated label | .github | 5 | 5 |
| unrelated label | book | 4 | 4 |
| unrelated label | papers | 14 | 14 |
| unrelated label | tools | 1 | 1 |
| unrelated label | verification | 79 | 79 |
| **unexplained (total)** | | **241** | **0** |

After the in-memory application at merged `main` no line is unexplained and none is pending an owner decision
(`--final`); the requirement holds again at the execution head (§11 item 11).

**Active non-manuscript rewrites drafted (§6.4–§6.6).**

- Lean docstrings (D262–D286): `ManuscriptAxioms.lean` (the module heading, the description of the
  conditions, the realized-core image docstrings), `SubstratumInterfaceAudit.lean` (the module description
  and five docstrings, each now stating the finiteness condition its declaration carries),
  `FrozenSourcing.lean`, `HexLatticeGas.lean`, `HydroSourceAudit.lean`, `RouteB.lean`, `SubstratumSource.lean`.
  Docstring only; `--static`'s docstring-only check confirms that each edited file equals the original
  outside comments.
- `verification/README.md` (D287–D291): the Route B and manuscript-axiom paragraphs.
- `verification/lean-manuscript-census.json` (D292–D294, D297–D299): registry notes quoting the manuscripts'
  A1–A6 statements.
- `verification/coverage/LEDGER.json` (D295): an assumptions field saying "Physical total finiteness (A1)
  remains open and unadopted".
- `AGENTS.md` (D296): owner approval needed (§12, question 6).
- Guard pins (D300–D308).

**Cross-references (item 4).** No posit count, "six structural" or "item (ii)" occurs outside the
manuscripts in the active tree (grep at `0ba358cc`). The README's "Every one of the six is a condition on a
substratum" counts the six conditions (finiteness and A2–A6) its rewritten sentence lists, and stays.

### 22.3 Valid finite-only results

Every result that needs finiteness keeps it explicit: in the manuscripts by the F-row rewrites (§5.1) and the
preservation checks (§23); in Lean by the declarations' own hypotheses (`[Finite 𝒮.ι] [Finite 𝒮.V]`,
`[NeZero L] [NeZero q]`), which the docstring edits now name (D278–D282).

### 22.4 Lean identifiers containing `A1`

References counted at `0ba358cc` (Lean sources, the census registry, the R7 guard, the README, frozen
records). Manuscripts cite none of them.

| Identifier | Denotes | Lean | Registry | Guard | README | Records |
|---|---|---|---|---|---|---|
| `Substratum.A1` (`def A1 : Prop := Finite 𝒮.Conf`) | finiteness of the configuration space | 8 (`.A1`) | 0 | 2 (exact definition text) | 0 | 10 |
| `Substratum.a1_of_finite` | finiteness from finite sites and alphabet | 3 | 0 | 1 | 0 | 34 |
| `waveSubstratum_A1` | the wave substratum on a finite torus is finite | 3 | 0 | 1 | 1 | 22 |
| `obs_a1` | finiteness of the observer theory's substratum | 2 | 0 | 0 | 0 | 2 |
| `WaveUnbounded.waveZ_not_A1` | control: not finite on ℤ^d | 3 | 1 (anchor) | 0 | 0 | 8 |
| `HexLatticeGas.hexSubstratum_A1` | the hex gas on a finite torus is finite | 3 | 1 | 0 | 1 | 5 |
| `A6Instantiation.pk3a_A1` | the packaged carrier is finite | 3 | 1 | 2 | 0 | 9 |
| `A6Instantiation.cx3b_complex_not_A1` | the complex carrier is not finite | 3 | 1 | 5 | 0 | 15 |
| `ManuscriptAxioms.A1Realized` | the realized core is finite | 5 | 1 | 5 (incl. "exactly four definitions") | 1 | 10 |
| `ManuscriptAxioms.A1A2Realized` | conjunction of the two images | 3 | 0 | 2 | 0 | 7 |
| `ManuscriptAxioms.a1_every_theory` | the finiteness image holds for every theory | 4 | 1 | 1 | 1 | 2 |
| `ManuscriptAxioms.substratumTheory_A1`, `substratumTheory_A1A2` | the images hold for the witness | 6, 2 | 1, 0 | 1, 1 | 1, 0 | 5, 2 |
| registry family "manuscript axioms A1-A6" | the census family of the audit | — | 1 (name) | 2 (name, rendered row) | 0 | rendered census record |
| programme label `A1-RIGID-1` | a landed research programme | 2 (module doc) | 1 (family name) | 0 | 0 | many |

Each name denotes a true finite-only statement or a control; none asserts that the substratum is finite.

**Disposition.** By owner decision (#1169 comment 7058783437) the renames are a separate follow-up PR (Issue
#1482), with kernel, Mathlib, registry and guard verification; they are not part of the deletion. In this plan
every prose line that names the predicate calls it "the finiteness predicate `A1`" (D274–D276, D314–D339),
accurate with or without the rename and not presenting A1 as an assumption. The registry family name "manuscript
axioms A1-A6" is kept and its note rewritten. `A1-RIGID-1` names a landed programme and stays.

## 23. Amendment: the configuration-space sentence

**Owner decision** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7058446475](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7058446475),
2026-11-21T06:12:34Z, "Owner decision record: A1 stays retired; unlabelled configuration-space definition"),
quoted:

> The decision to retire A1 permanently stands (#1169 c.7057297534). A1 is not redefined.
>
> ### Approved wording
> > Configuration space. The substratum has a configuration space $\mathcal S$. No restriction is imposed
> > on its cardinality; $\mathcal S$ may be finite or infinite.
>
> This sentence goes into the foundational setup of Main and Substratum, at the point where it fits
> naturally. It adds no new assumption or identifier.
>
> ### Conditions
> - A1 is retired and its identifier is reserved permanently.
> - A2–A6 keep their existing meanings.
> - No assumption that the universe is infinite is introduced.
> - Finiteness stays explicit wherever an individual theorem requires it.
> - The new definition does not imply that results established only for finite systems apply to arbitrary
>   configuration spaces.
> - These additions are part of the preregistration and independent review of #1477.
>
> This decision updates the deletion plan. It does not authorize executing the deletion.

**Symbol.** Both papers already use $S$ for the configuration space (Main's Definition: "a total system $S$";
Substratum: "$(S, \varphi)$"), so the sentence is inserted with $S$ for $\mathcal S$, otherwise verbatim.

**Sites.**

- **Main (D259).** A paragraph of its own after the Definition of an observation (M:42), the point where
  $S$ is introduced.
- **Substratum (D261).** The opening paragraph of §2, "The Physical Interpretation of (S, φ)", before
  "Storage and memory".

**Finite-only results near the sentence, checked.**

| Paper | Result | Finite scope after the edits | Preservation |
|---|---|---|---|
| Main | Lemma 1 | "makes the visible configuration space $\mathcal{C}_V$ finite" (finite-capacity clause) | checked |
| Main | Lemma 3, uniform measure on cycles | "On each finite cycle of the reversible representative" | checked |
| Main | Lemma 3, counting-measure selection | had no printed scope once item (ii)'s list is deleted; D260 adds "on a finite representative" (F row X-10) | checked |
| Main | Status Remark M:60 | "defined here for a finite system only", "no construction is given for an infinite $S$", the finite-representative list, "On a finite set, injectivity implies surjectivity" | checked |
| Substratum | Storage and memory | "*finite capacity* when $S$ is finite", "of finite capacity when $S$ is finite" (D013) | checked |

`edits_check.py --simulate` checks each phrase in the simulated papers, and that each paper carries the
sentence exactly once. The infinity scan does not flag the sentence and still flags "S is infinite" beside it
(countercontrols). The sentence adds no label, identifier or assumption (identifier rule: 0).


## 24. Reconciliation against merged `main` at `97070c98`

**Authorization** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7058783437](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7058783437),
2026-11-21T06:42:54Z, "Owner decision record: five open questions on #1477, and the next gates"), quoted in
part:

> | Question | Decision |
> |---|---|
> | Lean predicate renames R-1/R-2 | Approved as a **separate follow-up PR**, not part of the A1 deletion. Existing proof behavior and historical records are preserved. Requires kernel, Mathlib, registry and guard verification. |
> | R-C, registry family name "manuscript axioms A1-A6" | Keep unchanged. |
> | AGENTS.md:38 | Approved: correct the obsolete A1 reference. Keep the scientific principle that the substratum uses only assumptions justified by evidence or necessary for stated results, and remove A1 from its list of posits. |
> | Configuration-space sentence in the book mirrors | Include it. The book presents the same cardinality-neutral foundation as Main and Substratum. |
> | #1481 governance wording | Keep the strict safeguards. Identifier migrations require explicit owner approval and independent review, and retired IDs are never reused. |
>
> - **Reconcile #1477 against `7f28886f`: approved.** Rebuild the deletion plan against the merged manuscripts,
>   run its §9 checks, reconcile the full repository-wide inventory, and include the five decisions above.
> - **Execute the A1 deletion: not yet authorized.** This requires finishing the reconciliation and obtaining
>   independent acceptance of the executable plan first.
>
> ### Safeguard
> Removing the global finiteness assumption must not be presented as proof that the theory works for every
> infinite system. Each result keeps its own mathematical conditions.

#1481 needs no change to this plan.

### 24.1 Re-pin

`main` at `7f28886f4cc96fbfa7407af1fdc37de2f0e562e5` contains S2-A (#1470), #1476, S2-B (#1473), S2-C (#1474),
S2-D (#1472) and S2-E (#1475). `main` then moved to `97070c986c28f7ff8a443cbda5890c1694dd76dd`, which merges #1481
and changes only `AGENTS.md` (§A.48 added; §A.28 and §A.30 amended); the manuscripts and every other edited file are
byte-identical at the two commits. The drafting base of `edits.json` is `97070c98`; D296's `old` string at
AGENTS.md:38 is still unique there and the edit applies unchanged; the projection is retired,
and no record carries `old_step2`. Edit IDs are stable against `05f29f42`. Edits whose `old` string changed:

| Edit | Site | Change | Reason |
|---|---|---|---|
| D114 | ch02-substratum.md:16 | `old` re-pinned (and `new`) | not a merged-text change: the string is extended to "The framework's central object is a triple." so the owner's sentence opens the triple in place of D114's own neutrality wording (round 5; book mirrors) |
| D115 | ch02-substratum.md:16 | `old` re-pinned (and `new`) | FULL mirror of D114 |
| D224 | Main.md:732 | `old` re-pinned | S2-B and S2-C edited item (ii); the merged text equals the projected `old_step2` byte for byte |
| D232 | Substratum.md:92 | `old` re-pinned | S2-B and S2-C edited the (A1) entry; the merged text equals the projected `old_step2` byte for byte |
| D244 | Substratum.md:56 | `old` re-pinned (and `new`) | S2-D rewrote Sub:56; the merged text equals the projected `old_step2` byte for byte |
| D259 | Main.md:42 | `old` re-pinned (and `new`) | not a merged-text change: the anchor moves to before Lemma 1, after the "This definition formalizes ..." paragraph, and the run-in becomes bold (round 5 nit) |

Every other `old` string is byte-identical at the merged head and on the projection. Replacements revised at reconciliation (their `old` unchanged): D261, D263, D274, D275, D276, D288.

New edits: D309, D310, D311, D312, D313, D349, D350, D314, D315, D316, D317, D318, D319, D320, D321, D322, D323, D324, D325, D326, D327, D328, D329, D330, D331, D332, D333, D334, D335, D336, D337, D338, D339, D340, D341, D342, D343, D344, D345, D346, D347, D348. Removed: none.


The three merged-text changes (D224, D232, D244) are exactly the `old_step2` strings the projection predicted.
The moved weaker-condition list (D229) and transfer clause (D231) were re-compared with merged item (ii): both
are verbatim apart from the connectives and the S2-C qualifications D229 adds. The 37 S2-E residual lines are
resolved: on merged `main` the in-memory application leaves no residual pointer line.

### 24.2 §9 at `97070c98`

| Check | Result |
|---|---|
| Uniqueness and simulation (`--commit 97070c98 --simulate`) | uniqueness: 350 edits, 0 fail; variants used {'old': 350}; simulation: residual pointer lines 5 (5 allowed as listed, 0 unqualified); simulation: criterion-5/paraphrase hits on changed lines without a scope in their sentence: 0; simulation: finite-scope and configuration-space preservation findings: 0; simulation: identifier and count findings: 0; RESULT PASS |
| Static: infinity, register, identifiers, preservation, mirror parity, Lean docstring-only, sitemap | infinity-assertion scan (new and new_step2): 0 hits; register scan (added text, §A.32/§A.33, history phrases): 0 hits; new capitals (3+ letters): 0; identifier rule (new and new_step2): 0 findings; preservation check (required content in every replacement variant): 0 findings; mirror parity (every chapter edit byte-identical to its FULL mirror): 0 findings; sitemap cross-check: 194 ptr sites in the map, 194 with an edit; 0 findings; RESULT PASS |
| Pins (`--pins --commit 97070c98`) | pins check: 0 unresolved pins (literals of tracked checks that the edits would break); 0 updated pins not found in their targets |
| Repository-wide scan, after the edits, with pending lines rejected (`--repo-scan --simulate --final`) | repository-wide scan: 0 unexplained lines; RESULT PASS |

### 24.3 Changes made at reconciliation

| Item | Change |
|---|---|
| R-1/R-2 (owner) | Removed from the plan (Issue #1482). Prose naming the predicate is reworded as "the finiteness predicate `A1`": Lean docstrings (D314–D324; D274–D276 reworded), README (D325–D330), registry notes (D331–D339) |
| R-C (owner) | Family name kept, reclassified "registry identifier (kept)"; note rewritten (D293–D294) |
| AGENTS.md:38 (owner) | D296 approved, class mechanical |
| Book mirrors (owner) | ch01: D310–D311 after the Definition and its paragraph; ch02: D114–D115 replace D114's own wording with the owner's sentence, one wording; ch01's Lemma 3 scoped (D312–D313); the preservation check covers ch01, ch02 and FULL (the sentence twice in FULL) |
| Safeguard (owner) | The infinity scan also rejects "every/any/arbitrary infinite system", "holds/works/applies for every configuration space", "regardless of its cardinality"; countercontrols added |
| Round 5, must-fix 1 | `--pins` checks that every literal a guard-pin edit introduces occurs, whitespace-normalized, in the simulated text of each target the record names; the reviewer's three mismatch injections are countercontrols; limits stated in §16 |
| Round 5, must-fix 2 | M:58 measure remark scoped to a finite representative (D309) |
| Round 5, must-fix 3 | Live programme charters and READMEs under `verification/programmes/` are active in the scan. Rewritten: `hydrodynamics/PROGRAMME.md` 35, 37, 57 (D340–D342); `native-y-continuation-20261024/README.md` 58 (D343); `continuous-substates/README.md` 125, 131 (D344–D345). Unrelated labels kept: the programme targets A1/A2 (`black-hole-information/PROGRAMME.md`, `native-y-continuation` lines 17, 56), table rows and amendment labels A1 in other programme READMEs |
| Round 5, must-fix 4 | Backticked prose `A1` is no longer an identifier form in the scan: only full declaration names and "the finiteness predicate `A1`" are. The reviewer's lines (README 2476, A6Instantiation 43, 74, 499, 509, 564, HexLatticeGas 37) are reworded |
| Round 5 nits | D259 after the "This definition formalizes …" paragraph with `**Configuration space.**` (the same run-in in Substratum, ch01, ch02); D276 scopes "on a finite torus" to finiteness; D263 and D288 share one wording; the `SyntaxWarning` is suppressed in `--pins` |

### 24.4 AGENTS.md §A.48

§A.48 (adopted by owner decision, #1169 comment 7058897767) governs the plan's classification. Active material —
`papers/`, `book/`, the READMEs, AGENTS.md apart from its record sections, code comments, and the Lean names and
docstrings — states the current theory (§A.48 item 1): the manuscript, README, AGENTS.md, Lean-docstring and
guard-comment edits rest on it, and the live programme charters and READMEs under `verification/programmes/` are
scanned as active. Verification records and the records §A.39, §A.42 and §A.46 govern are not edited (§A.48
item 2): the scan's "historical record" class rests on it, and the README of an audit record (for example
`verification/audits/manuscript/intro-corpus-audit-20261026/tracks/SC44-SC45-reconciliation/README.md`) stays a
record. The guard comments that named A1 as a premise are rewritten (D346–D348, comments 3369, 9456, 10903 of the R7
guard); the guard's remaining A1 strings are pins of record text, kernel names and forbidden phrases.

**Hand-off to #1482 (the Lean renames).** Under §A.48 item 3 the rename of `Substratum.A1`, its theorems and the
realized-core images is an identifier migration of kernel identifiers the census and records cite. It needs, in
advance, owner approval and acceptance by an independent non-author review; it states its clarity gain; it maps
every old identifier to its successor and reuses none; it traces and updates every reference across the active
material, the Lean modules, the census registry (§A.35), the guards and the coverage ledger in one change; it leaves
frozen and preserved records unchanged and records, in a mutable index on `main`, the successor of every old
identifier they cite; and it is verified by the build, the kernel and every check that reads the identifiers. The
prose that now says "the finiteness predicate `A1`" (D274–D276, D314–D339) is updated by that migration. Round H-B's
frozen sentence is not, and neither are the guard checks Z17, Z18 and W21 that pin it (§25.3, owner decision 4).

**Frozen sentence of round H-B.** `hydrodynamics/PROGRAMME.md` line 231 and the module docstring of
`HexLatticeGas.lean` carry the sentence "one candidate executed in the A1–A4, ¬A5 class", which the R7 guard
pins byte for byte as round H-B's frozen wording (checks Z18 and W21, and the module check), and the registry
quotes it. "A1–A4" there is the class of the Lean predicates `A1`–`A4`, `A1` being the finiteness predicate.
It stays unchanged as historical evidence (owner decision 4, #1169 c.7059136165), classified "preserved historical
evidence" in the repository scan, and the active text that relies on it states the class by its condition (§25.3).

### 24.5 Acceptance review of `5e818088` (ACCEPT-WITH-NITS)

| Item | Change |
|---|---|
| SC-42 | §11 item 13: regeneration under S2-D's safeguards (normal and `-O` runs and `--verbose` byte-identical, `--self-test` matching the unchanged controls, every diff line a mirror prefix of a book edit, independent verification), with the owner's narrow approval as part of the execution authorization |
| ch01 Lemma 3 | "$\varphi$ is a bijection on $S$" takes its conditions: "On a finite representative, or under A2 (Chapter 2 §2.4)" (the book states reversibility as A2), with the FULL mirror; added to the preservation check |
| §11 item 4 | Names `MAIN:L-3`, `STRUCTURE:P-9.5`, `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer` and `SUBSTRATUM:T-23`, with the level and delta of L-3 and T-23 re-read |
| D340 | "(finiteness of the representative and A2–A6 of the substratum programme)" |
| Safeguard | "extends to infinite substrata", "applies to infinite configuration spaces" and their variants are rejected, with countercontrols |
| H-B sentence | Class "preserved historical evidence", unchanged by this plan and by #1482 (owner decision 4; §25.3) |

## 25. Amendment: round-5 closure, safeguards for the destructive change, the frozen H-B sentence and the guard pins

**Owner decision** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7059136165](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7059136165),
2026-11-21T07:15:31Z, "Owner decision record: A1-EXIT handoff follow-up, six decisions"), decisions 2–5 quoted in
part:

> 2. **Round-5 closure on #1477.** Before acceptance, #1477 carries a closure table with one row for each of the six
>    round-5 findings (c.7058814130). Each row gives the edit IDs, the test and the verification result. The `--pins`
>    check must run against the simulated post-deletion tree, not only against the edit plan.
> 3. **Safeguards for the destructive change, before execution.** The deletion plan states whether it runs as a native
>    round under §A.39. [...] If it does not, it names the equivalent safeguards it adopts and why that is permitted.
>    At minimum these are: a frozen exact-edit ledger; a preservation checker implemented independently of the
>    deletion; mutation tests showing that both missing changes and unauthorized changes are detected; CI on the exact
>    proposed post-deletion tree before the merge.
> 4. **The frozen H-B sentence is preserved.** The sentence "A1–A4, ¬A5 class" stays unchanged as historical evidence.
>    Every active index, summary or claim that relies on it states the actual mathematical condition, without
>    presenting A1 as a current premise. #1482 may address related identifier clarity, but it does not change this
>    sentence.
> 5. **Guard strings are technical pins, under a narrow exception.** A retained A1 string inside a guard is a technical
>    pin only if all of these hold: it names its target; it states its purpose; it passes a test against that target.
>    A string that serves as user-facing documentation does not qualify.

Decision 6 leaves the deletion unauthorized; nothing in this section applies an edit.

**Goal link (§A.47).** A1-EXIT (#1169): this section decides whether the executable plan meets decisions 2–5, which
gate the owner's decision whether to authorize execution; it does not decide that question.

### 25.1 Round-5 closure table

Results at merged `main` `97070c98`, on the simulated post-deletion tree (the tree of `97070c98` with all 360 edit records
applied, written outside the repository by `guards_check.py`).

| # | Round-5 finding (#1477 c.7058814130) | Edits | Test | Result |
|---|---|---|---|---|
| 1 | `--pins` does not show that the guards pass after execution; three mismatch injections passed | guard pins D300–D306 and their target edits (each record's `targets`: D220–D221 for D306, D287 for D302); guard comments and messages D307, D308, D346–D348, D351–D357 | (a) `edits_check.py --pins`: every literal a guard-pin edit introduces must occur in the simulated text of each named target; the reviewer's three injections are self-test countercontrols. (b) `guards_check.py`: the R7 guard (`edge_rigidity_probe.py`) and `bohr_frequency_probe.py` run on the simulated post-deletion tree, with four countercontrols: CC-1 D302 omitted, CC-2 D302's literal removed from its target `verification/README.md`, CC-3 the glossary edit D220/D221 omitted while D306 is applied, CC-4 D301 omitted | (a) 0 unresolved pins, 0 updated pins missing from their targets; the three injections fail. (b) R7 guard and `bohr_frequency_probe.py` pass on the simulated tree; CC-1 fails `R7-RB1`, CC-2 fails `R7-RB1`, CC-3 fails `R7-A6P`, CC-4 fails `F71`. Closed |
| 2 | M:60 measure remark: "the uniform probability, with the uniform conditional law on 𝒞_H" needs a finite 𝒞_H | D309 | `--static` preservation (D309 keeps "of a finite representative (Lemma 2) it is the uniform probability"); the simulated Main.md read at the remark | 0 preservation findings; the simulated remark reads "On the selected bijective carrier $\mathcal{C}_V \times \mathcal{C}_H$ of a finite representative (Lemma 2) it is the uniform probability, with the uniform conditional law on $\mathcal{C}_H$ in each visible fibre". Closed |
| 3 | Live programme charters classed as historical (`hydrodynamics/PROGRAMME.md` 35, 37, 57; `native-y-continuation-20261024/README.md` 58; `continuous-substates/README.md` 125, 131) | D340–D345 | `classify()` treats `PROGRAMME.md` and `README.md` under `verification/programmes/` as active (self-test countercontrol "a live programme charter is active"); `--repo-scan --simulate --final`; the six lines read in the simulated tree | 0 unexplained lines; none of the six lines carries A1 after the edits. Closed |
| 4 | Backticked prose about the predicate (README 2476; `A6Instantiation.lean` 43, 74, 499, 509, 564; `HexLatticeGas.lean` 37) classed as a kernel identifier, so `--final` did not cover it | D274–D276, D314–D339 | the identifier form accepts only full declaration names and "the finiteness predicate `A1`" (self-test countercontrols "backticked prose `A1` is not an identifier form", "the finiteness predicate `A1` is an identifier form"); `--repo-scan --simulate --final`; the seven lines read in the simulated tree | 0 unexplained, 0 pending; each of the seven lines names "the finiteness predicate `A1`" (the kernel name is #1482's). Closed |
| 5 | Book mirrors: the owner's configuration-space sentence in the ch01 Definition and in ch02 in place of D114's own sentence | D310–D311 (ch01, FULL), D114–D115 (ch02, FULL), D312–D313 (ch01 Lemma 3) | `--simulate` preservation: the sentence exactly once in Main, Substratum, ch01 and ch02 and twice in FULL; ch01's Lemma 3 scope; `--static` mirror parity; `mirror_check.py` on the simulated tree | 0 preservation and 0 mirror-parity findings; `mirror_check`: 0 chapter lines absent from FULL. Closed |
| 6 | Nits: D259 placement and run-in; D276 scope; one wording for D263 and D288; `SyntaxWarning` from `--pins` | D259, D276, D263, D288 | the simulated Main.md read at D259; the D276, D263, D288 strings compared; `--pins` standard error | D259 stands after the "This definition formalizes …" paragraph as `**Configuration space.**`; D276 reads "satisfies the finiteness predicate `A1` on a finite torus and A2–A5 as stated"; D263 and D288 both read "finiteness of the configuration space (the scope of the reconstruction theorem) and A2–A6"; 0 `SyntaxWarning` lines. Closed |

Round 5's must-fix 5 (§9 at the merged head) is §24.2, re-run in §25.6. No round-5 finding is open.

### 25.2 The deletion and AGENTS.md §A.39

**Decision.** The deletion does not run as a native V3 round. It adopts the safeguards of §A.39's rule for
destructive transformations, which decision 3 names as its minimum, as frozen preconditions of execution.

**Why this is permitted.** Decision 3 allows either route provided the equivalent safeguards are named. A native
round's protocol record (one `v3-round` control plane, owner-designated `F` and `E` with exact-head `check-run`
attestations, a receipt `Q` that `tools/v3_verifier.py --verify-round` must hold) certifies the chronology of a
governed computation. The deletion is a text change: 371 literal splices (373 edit records, of which D032 and D039 retain their text) of manuscript, README, registry, coverage,
AGENTS.md, Lean-comment and guard-literal text, with no computational verdict, no kernel statement changed (every Lean
file is code-identical outside comments). No edited file is listed in `verification/infrastructure/legacy-records.json`, lies in one of its closed namespaces or in a receipt's record directory; the programme files it edits are live charters, active material under §A.48. What §A.39 protects
against in a destructive change (a deletion the plan did not authorize, a retained statement silently removed, a
generated tree never exercised) is covered component by component below. The owner decides whether this
substitution is accepted (decision 6).

**Retirement, stated separately (§A.39).** *Authority*: A1 is retired as an assumption (#1169 c.7057297534), and no
active text presents it as one. *Reachability*: after the edits no manuscript, README, AGENTS.md line, Lean docstring,
guard comment or guard message names A1 as a premise (`--repo-scan --simulate --final`: 0 unexplained). *Physical
presence*: the identifier survives in frozen and historical records, in the Lean names `Substratum.A1` and its
theorems (renamed only by the migration of #1482), in prose naming that predicate, in the registry family name kept
by owner decision, and in the guard pins of §25.4.

| Safeguard | Component | State |
|---|---|---|
| Frozen exact-edit ledger | `ledger.json`: 371 splices in 40 files at `97070c98`, and the two retained-site records D032, D039 listed apart; each splice records its file, the byte span of the old text at the base, the SHA-256 of the old text, the new text, its SHA-256 and the reason; the SHA-256 of `edits.json` it was built from. Ledger SHA-256: §26.4. `preserve_check.py --verify-ledger` re-derives it from `edits.json` and the base and compares | exists; frozen at the commit the owner designates when authorizing execution. A later `edits.json` change, or a base at which a ledgered file differs, needs a new ledger, a new digest and a new acceptance |
| No deletion without a ledger entry | every deletion is a splice with its literal old text and reason; nothing is inferred | exists |
| Preservation checker independent of the transformation | `preserve_check.py` imports nothing from `edits_check.py`, `guards_check.py` or any applying script; it reads the base from the object store, rebuilds every ledgered file from the base and the ledger alone, and compares every tracked file byte for byte: a ledgered file must equal the rebuilt one, any other file the base, except the regenerated artifacts of §26.2, each compared with its rebuild on the candidate; the record directory must equal the plan's (§26.4). Structural checks: a Python file changes only in string constants and comments (AST with strings blanked), a Lean file only inside comments, a JSON file only in string values. `--base REV` compares against a later `main`, and is refused unless every ledgered file is byte-identical there | exists |
| Agreement of two implementations | the tree built by `edits_check.py`'s in-memory application (`guards_check.py`) passes `preserve_check.py --tree`; the unedited base fails it, with one finding in each of the 40 ledgered files | checked (§25.6) |
| Mutation tests, missing changes | `preserve_check.py --self-test`: MT-missing-D224, MT-missing-D121, MT-missing-D302, MT-missing-D262 (each one ledgered change not made, so retired text restored) and MT-altered-D229 each fail, naming the splice | exists, PASS |
| Mutation tests, unauthorized changes | MT-extra-in-ledgered-file (a word outside every splice of Main.md), MT-extra-in-untouched-file (`tools/release_gate.py`), MT-guard-code (an operator of the R7 guard), MT-lean-code (a Lean definition), MT-added-file, MT-deleted-file, MT-record-edited (a record file present at the base), MT-coverage-beyond-fingerprints, and two ledger tamperings (old-text hash, span) each fail; a new execution record, a derived path and a re-affirmed fingerprint pass | exists, PASS |
| Mutation tests at the guard level | `guards_check.py` CC-1–CC-4 (§25.1 row 1) and the 30 pin mutants P01–P30 (§25.4) | exists, PASS |
| CI on the exact proposed post-deletion tree, before the merge | §26.3: a disposable branch carrying the predicted execution tree less its result note (the base, the 358 ledgered splices, the regenerated SC-42 result, the TeX/PDF regenerated by `sh ./build.sh` on the canonical toolchain, the re-affirmed fingerprints of the four entries of §11 item 4, the plan's record directory); `preserve_check.py` run from the plan commit passes on it, and `verify.yml` dispatched on that exact head is green | specified, not run: pushing that branch and dispatching need owner approval (§A.43 item 4). Required pre-execution item |
| Landing | the execution commit equals the CI-tested tree plus its result note under `execution/`; before merge `preserve_check.py`, run from the designated plan commit (`git show <plan>:…/preserve_check.py`, never the candidate's copy), passes `--commit <execution head> --plan <plan>`, and, if `main` has moved, `--base <current main>` passes or the ledger is re-cut; after merge the landing diff against its first parent is exactly the execution's own diff | specified; required at execution |
| Evidence (§A.42) | the exact-head CI run, the outputs of `preserve_check.py`, `guards_check.py` and `edits_check.py` at the tested head, recorded as expected results in this record directory | required at execution |
| Independent review of the executed diff | §0 boundary ("an independent review of the resulting changes") | required at execution |

### 25.3 The frozen H-B sentence

The sentence "H-B: one candidate executed in the A1–A4, ¬A5 class; OI-compatibility of the class open
(`round-h-b-reversible-fluid-substratum/result.md`)." at `verification/programmes/hydrodynamics/PROGRAMME.md:231`,
and its source wording "**a rigorous reversible fluid witness in the A1–A4, ¬A5 class**" in the module docstring of
`OIBridge/HexLatticeGas.lean` (line 94), stay byte-identical. No edit of this plan touches either string (the R7
guard's checks Z17, Z18 and W21 confirm it on the simulated tree, §25.4 P22–P24, P30), and #1482 does not change them.
In that class name "A1" is the kernel predicate `Substratum.A1`, `Finite 𝒮.Conf`; the class is that of substrata with
a finite configuration space satisfying A2–A4 as the kernel states them, with A5 failing.

Active material that relies on the sentence, with its wording after the edits:

| Site | Kind | After the edits |
|---|---|---|
| `verification/programmes/hydrodynamics/PROGRAMME.md:231` (§8, the live one-line state) | live charter; carries the frozen sentence | the sentence unchanged, followed by D358: "That class is the class of substrata with a finite configuration space satisfying A2–A4 as the kernel states them, with A5 failing." (Z18 and W21 pass with it) |
| `verification/lean-mathlib/OIBridge/HexLatticeGas.lean:91–96` ("The post-round status") | Lean module docstring; carries the source wording | unchanged: the same paragraph states the condition, "The candidate is finite, deterministic, reversible, translation-covariant and of bounded degree, inside the kernel's `Substratum` interface", and "the class obtained by dropping A5's amplitude-scale gauge principle" |
| `verification/README.md:2312–2313` (round H-B paragraph) | README summary | D328: "the execution establishes a reversible fluid witness in the class of substrata with a finite configuration space satisfying A2–A4 and not A5, and whether that class is admissible as OI physics is recorded as open" |
| `verification/lean-manuscript-census.json:993` (family "hydrodynamics round H-B") | registry note | D335: "A RIGOROUS REVERSIBLE FLUID WITNESS IN THE CLASS OF A FINITE CONFIGURATION SPACE WITH A2-A4, NOT A5"; the note's quotation "PROGRAMME.md section 8 reads 'H-B: one candidate executed in the A1-A4, not-A5 class; …'" stays, as the quotation of the frozen sentence |
| `verification/lean/edge_rigidity_probe.py:9456` (R7-HYB header comment) | guard comment | D347: "witness in the class of a finite configuration space with A2-A4, not A5" |
| `verification/lean/edge_rigidity_probe.py:9599` (R7-HYB message) | guard message | D354: "witness named in the class of a finite configuration space with A2-A4, not A5" |
| `verification/lean/edge_rigidity_probe.py:9523, 9536, 9590, 11348` | guard pins of the frozen wording | kept as technical pins P22, P23, P24, P30 (§25.4) |

Six active sites rely on the sentence; four are reworded (D328, D335, D347, D354), one gains a gloss beside it (D358)
and one already states the condition; the four guard literals are pins. The frozen records that also carry it
(`verification/ROADMAP.md:1329, 1339`, the round records under `verification/programmes/hydrodynamics/round-h-*/`,
`verification/infrastructure/round-v3-1[34]-retirement/`) are not edited. §24.4's hand-off of this sentence to #1482
is replaced by this subsection: the three lines that carry the sentence are classed "preserved historical evidence"
in the repository scan, and #1482's hand-off does not include them or the guard checks Z17, Z18
and W21 that pin them.

### 25.4 Guard A1 strings

After the edits the two guards keep 30 string literals that contain A1, all in the R7 guard; `bohr_frequency_probe.py`
keeps none. Comments, docstrings and messages that named A1 in prose are rewritten (D307, D308, D346–D348, D351–D357), so none of
them keeps A1 as documentation. `guards_check.py` checks that the inventory is complete (every A1 string of both
simulated guards is a listed pin or one of the two listed declaration names; no comment keeps one) and, with
`--mutants`, tests each pin against its target: the guard passes on the simulated tree, and fails when a positive
pin's literal is removed from its target or a negative pin's literal is inserted into it.

| Pin | Guard line | Literal | Target | Polarity | Purpose | Mutation fails |
|---|---|---|---|---|---|---|
| P01 | 3346 | `A1–A6 are not` \`DerivedOI\` | `programmes/substratum/route-b-audit.md` | + | the Route B record's outcome wording | R7-RB1 |
| P02 | 3410 | `**(A1) Finiteness.** The configuration space $S$ is finite.` | `programmes/substratum/manuscript-axiom-audit.md` | + | the audit record quotes the six axioms verbatim | R7-MAX |
| P03 | 3414 | `\| A1 finiteness \| **yes**` | the same record | + | the preregistered verdict row | R7-MAX |
| P04 | 3419 | `Status: pass complete, … No manuscript-level A1–A6 conjunct …` | the same record | + | the record's status line | R7-MAX |
| P05 | 3421 | `A1 and A2 are realized-core images, …` | the same record | + | the scope repair recorded at review | R7-MAX |
| P06 | 3425 | `\| A1 finiteness \| realized-core image holds …` | the same record | + | the outcome row | R7-MAX |
| P07 | 3453 | `A1 and A2 hold for the witness` | `OIBridge/ManuscriptAxioms.lean` | − | a superseded reading is absent from the module | R7-MAX |
| P08 | 3453 | `A1 AND A2 HOLD FOR THE WITNESS` | `OIBridge/ManuscriptAxioms.lean` | − | the same reading, capitalized | R7-MAX |
| P09 | 3456 | `A1–A6 hold for the witness` | `manuscript-axiom-audit.md` | − | an overclaim is not asserted in the record | R7-MAX |
| P10 | 3457 | `satisfies A1–A6` | `manuscript-axiom-audit.md` | − | an overclaim is not asserted | R7-MAX |
| P11 | 3461 | `A1 and A2 hold for the witness` | `manuscript-axiom-audit.md` | − | a superseded reading is not asserted | R7-MAX |
| P12 | 3468 | `manuscript axioms A1-A6` | `verification/lean-manuscript-census.json` | + | the registry family name kept by owner decision (#1169 c.7058783437) | the guard aborts (exit 1): the family lookup is empty |
| P13 | 3475 | `\| manuscript axioms A1–A6 \| 1 \| kernel-only \|` | `audits/manuscript/lean-manuscript-census.md` | + | the census record's row for the family | R7-MAX |
| P14 | 3475 | `realized-core images of A1 and A2` | the same census record | + | the census record's wording | R7-MAX |
| P15 | 3641 | `def A1 : Prop := Finite 𝒮.Conf` | `OIBridge/SubstratumInterfaceAudit.lean` | + | the kernel definition, verbatim (renamed only by #1482) | R7-SUB |
| P16 | 3703 | `Status: pass complete. Q1: A1, A2 and A5 are stated on the structure` | `programmes/substratum/interface-audit.md` | + | the interface-audit record's status line | R7-SUB |
| P17 | 3711 | `satisfies A1–A6` | `interface-audit.md` | − | an overclaim is not asserted | R7-SUB |
| P18 | 3711 | `satisfies the manuscripts' A1–A6` | `interface-audit.md` | − | an overclaim is not asserted | R7-SUB |
| P19 | 3736 | `A1–A6 as predicates of it` | `verification/README.md` | − | a superseded reading is absent from the README | R7-SUB |
| P20 | 6267 | `A1` (a `def` of that name) | `OIBridge/FrozenSourcing.lean` | − | the module defines no predicate named A1 | R7-FSS |
| P21 | 6432 | `A1` (a `def` of that name) | `OIBridge/StochasticInterface.lean` | − | the module defines no predicate named A1 | R7-SOI |
| P22 | 9523 | `**a rigorous reversible fluid witness in the A1–A4, ¬A5 class**` | `OIBridge/HexLatticeGas.lean` | + | Z17: the module keeps the frozen H-B wording | R7-HYB |
| P23 | 9536 | the frozen H-B sentence with its citation | `programmes/hydrodynamics/PROGRAMME.md` | + | Z18: §8 carries exactly the frozen sentence | R7-HYB, R7-HYE |
| P24 | 9590 | the frozen H-B sentence without its citation | the same | + | mutation control m25 is built from it | R7-HYB, R7-HYE |
| P25 | 9748 | the whole ROADMAP row P1 — A6 (it names `A1`–`A5`, `A1` and the A1–A6 package) | `verification/ROADMAP.md` | + | R7-A6P: the row byte-identical in the frozen ROADMAP | R7-A6D, R7-A6P |
| P26 | 10672 | the same row | `verification/ROADMAP.md` | + | R7-A6D A18: the same row | R7-A6D, R7-A6P |
| P27 | 10980 | `¬ (linkSubstratum … ).A1` | `OIBridge/A6Instantiation.lean` | + | I17: the kernel statement of `cx3b_complex_not_A1` | R7-A6I |
| P28 | 11031 | `` `A1` is not weakened to make it fit `` | `verification/ROADMAP.md` | + | I22: the instantiation round's ROADMAP section | R7-A6I |
| P29 | 11050 | `` `A1` is not weakened `` | `verification/README.md` | + | I23: the README paragraph, which reads "the finiteness predicate `A1` is not weakened" | R7-A6I |
| P30 | 11348 | the frozen H-B sentence with its citation | `programmes/hydrodynamics/PROGRAMME.md` | + | W21: H-B's sentence byte-identical beside H-E's | R7-HYB, R7-HYE |

Every pin names its target, states its purpose and passes its test against that target. Each targets a frozen record,
a kernel definition or statement, the frozen ROADMAP, the registry family name or a phrase that must stay absent; none
is user-facing documentation.

Two check messages keep Lean declaration names that contain A1: R7-MAX (line 3485, `A1Realized`, `A2Realized`,
`A1A2Realized`) and R7-A6I (line 11265, `cx3b_complex_not_A1`). By owner ruling (#1169 comment 7059632884) they stay
as technical pins until #1482, on three conditions: they are strictly machine-facing references, they do not appear as
active scientific assumptions, and #1482 must remove or update them. No broader exception is authorized. Here they
name the kernel declarations the check verifies, in a check message, and the prose around them names no A1 premise.
Target: `OIBridge/ManuscriptAxioms.lean` (declaring `A1Realized`, `A1A2Realized`) and `OIBridge/A6Instantiation.lean`
(declaring `cx3b_complex_not_A1`). Test: `guards_check.py --mutants` renames each in its target and the guard fails
(R7-MAX; R7-A6I).

**Items #1482 must remove or update** (with the renamed declarations): the name `A1Realized` and `A1A2Realized` in the
R7-MAX message (`edge_rigidity_probe.py:3485`) and the name `cx3b_complex_not_A1` in the R7-A6I message
(`edge_rigidity_probe.py:11265`); `guards_check.py`'s `DECL_NAMES` lists both.

### 25.5 Edits added or revised in this amendment

| Edit | Site | Change |
|---|---|---|
| D328 | README:2313 | revised: the class by its condition (§25.3) |
| D335 | census:993 | revised: the class by its condition (§25.3) |
| D347, D348 | R7 guard 9456, 10903 | revised: comments state the condition by name, without A1 |
| D351, D352 | R7-MAX message (3489, 3493) | new: "the realized-core images of finiteness and A2"; "against the substratum conditions" |
| D353 | R7-SUB message (3756) | new: "it defines the finiteness predicate, A2, A3, …" |
| D354 | R7-HYB message (9599) | new: §25.3 |
| D355, D356 | R7 docstrings of I17 and I22 (10968, 11019) | new: "finiteness on the complex carrier"; "the finiteness predicate not weakened" |
| D357 | R7-A6I message (11266) | new: "finiteness at the complex carrier" |
| D358 | PROGRAMME.md:231 | new: the class stated beside the frozen sentence |
| D261 | Sub:42 | anchor narrowed to "**Storage and memory.**" (unique at the base); the spliced text is unchanged |

All are mechanical. Edit records: 360 (ptr 242, consistency 23, handoff 5, lean-docstring 36, repo-active 35,
guard-pin 19).

### 25.6 Checks at `97070c98`

| Command | Result |
|---|---|
| `edits_check.py --self-test` | PASS (93 countercontrols) |
| `edits_check.py --static` | infinity 0, register 0, capitals 0, identifier 0, preservation 0, mirror parity 0, Lean docstring-only 0, sitemap 194/194; PASS |
| `edits_check.py --commit 97070c98 --simulate` | uniqueness 360/360; residual 5 (all allowed), unscoped 0, preservation 0, identifier 0; PASS |
| `edits_check.py --pins --commit 97070c98` | 0 unresolved, 0 updated pins missing from their targets; PASS |
| `edits_check.py --repo-scan --simulate --final --commit 97070c98` | 0 unexplained; PASS |
| `guards_check.py --mutants` | on the simulated tree: R7 guard, `bohr_frequency_probe.py`, `repertoire_lie`, `wave_period`, `gap_correspondence`, `stinespring_scope`, `canonical_measure`, `structural_chain`, `structural_core`, `cubic_isotropy` probes, `tools/lean_manuscript_census.py`, `mirror_check.py`, `citation_check.py`, `tools/dependency_label_check.py --strict` all pass; CC-1–CC-4 fail as named; inventory complete (30 pins, 2 messages naming declarations, 0 unlisted); P01–P30 each fail under mutation, and so does renaming each of the three declaration names in its target; PASS |
| `preserve_check.py --verify-ledger` | ledger re-derived identically; PASS |
| `preserve_check.py --self-test` | positive control and every named mutant as stated in §25.2; PASS |
| `preserve_check.py --tree <simulated tree>` | 0 findings; PASS. On the unedited base: FAIL, one finding in each of the 40 ledgered files |

Checks that read the edited files and are not run here, because they need the Lean toolchain, repository history, a
fresh build or many minutes, run in CI on the exact tree of §25.2: the Lean kernel and Mathlib builds, the release
gate (`coverage` fails until the changed fingerprints are re-affirmed, H-6; `staleness` until the TeX/PDF are
rebuilt), `staggered_relations_probe.py`, `kinf2_foundations_probe.py` and the round controls under
`verification/programmes/` that read an edited file.

### 25.7 Required before execution

1. The order of §26.3: the exact-tree CI run on the tree the ledger predicts at the plan commit, then the owner's
   designation of that plan commit. Pushing the disposable branch and dispatching need owner approval.
2. The derived artifacts (TeX/PDF, the SC-42 result, the four coverage fingerprints) regenerated on that branch as
   §26.2 states.
3. Independent acceptance of this reconciled plan, including decisions 2 and 3, and the owner's decision whether to
   authorize execution (decision 6).
4. The two declaration-name pins of §25.4 stay machine-facing and are on #1482's list of items to remove or update
   (owner ruling, #1169 comment 7059632884). A1 stays retired: no optional A1 hypothesis is introduced.

## 26. Amendment: answer to the acceptance review of `2b45ee72` (ACCEPT WITH CHANGES)

The independent acceptance review is recorded on #1477 (comment 7059814445). The owner's rulings of
[#1169 comment 7059632884](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7059632884) apply. They
name the sole writer of #1477. They let the two Lean declaration names in check messages stay as technical pins until
#1482, provided they are strictly machine-facing references, do not appear as active scientific assumptions and are
listed as items #1482 must remove or update; no broader exception is authorized. A1 stays retired, no optional A1
hypothesis is introduced, and the plan's design is unchanged.

**Goal link (§A.47).** A1-EXIT (#1169): this section decides whether the plan meets the review's findings, which gate
the owner's execution decision; it does not decide that question.

### 26.1 Findings and fixes

| # | Finding | Fix | Test | Result |
|---|---|---|---|---|
| 1 | The specified CI tree cannot pass both the checker and `verify.yml`: the regenerated SC-42 result is neither ledgered nor derived | `preserve_check.py` classes `sc42-integration-result.json` as a regenerated artifact: the candidate's file must be byte-identical to the SC-42 checker's `--verbose` output on the candidate, and to its `-O` output; its `--self-test`, plain and with `-O`, must equal the unchanged controls file; a candidate that is not a git checkout cannot pass. `guards_check.py --predict` builds the predicted tree with the regenerated result, and runs `verify.yml`'s four SC-42 comparisons on it | self-test MT-sc42-hand-edit, MT-sc42-not-regenerated; tree mutant on the predicted tree; `verify.yml` comparisons on the predicted tree | §26.7 |
| 2 | Derived TeX/PDF not checked; a hand-edited `papers/GR.tex` passed | TeX outputs are derived only for the ledgered sources (Computation, GR, Main, Methodology, SM, Structure, Substratum and FULL); each must be byte-identical to its rebuild from the candidate's source by `build.sh`'s recipe. A base control rebuilds the base sources first and must reproduce the base TeX (it does, with pandoc 3.1.3, for all eight). Every other TeX file must equal the base. A PDF of a ledgered source may differ and is checked by the CI build (§26.3) | self-test MT-tex-hand-edit (GR.tex), MT-tex-untouched (Juno.tex); tree mutant (GR.tex) | §26.7 |
| 3 | The record directory is unpinned: replacing `ledger.json` or `preserve_check.py` passed, and the checker read its ledger from its own checkout | `--plan REV` reads the ledger, the pin table and the record directory from REV's objects; the candidate's record directory must equal the plan's, adding files only under `execution/`; the checker's own bytes must equal the plan's `preserve_check.py`; every file of §26.4 must match its pinned digest | self-test MT-ledger-replaced, MT-checker-replaced, MT-record-added, and three pin tamperings (ledger digest, own bytes, `edits.json`); tree mutants (ledger.json, preserve_check.py) | §26.7 |
| 4 | Every coverage fingerprint could change | only the fingerprints of `MAIN:L-3`, `STRUCTURE:P-9.5`, `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer` and `SUBSTRATUM:T-23` may change, each to the value `tools/proof_census.py` computes on the candidate; every other byte of the coverage ledger is base plus D295 | self-test MT-coverage-unnamed-fingerprint, MT-coverage-named-wrong, MT-coverage-field; tree mutant | §26.7 |
| 5 | The guard inventory missed A1 inside kernel identifiers | `guards_check.py`'s inventory also matches names with A1 embedded (`\w*[a-z_]A1…`, `A1[A-Za-z_]…`, `a1_…`); the twelve occurrences in code literals are listed with target, polarity and a mutation test (§26.5) and go to the owner as a question | inventory: 0 unlisted; each of the twelve fails its guard under mutation | §26.7 |
| 6 | D210/D211 implied the infinite-dimensionality is only apparent for every discrete substratum | "discrete at the substratum level, and finite-dimensional on a finite representative, but *appearing* infinite-dimensional" | `--static`, `--simulate` | §26.7 |
| 7 | No-op splices D032, D039 (SM:22, GR:20); 356 against 358 | the two stay in `edits.json` as retained-site records and leave the ledger (`retained_unchanged`); counts read 360 edit records, 358 splices, of which none is a no-op | `--verify-ledger`; count grep | §26.7 |
| 8 | D178: "violate this strictly" had no assumption left to violate | D359 (mirror D360): "Matrix models with $N \to \infty$ limits lie outside that finite scope" | `--static`, mirror parity | §26.7 |
| 9 | ID provenance | §26.6 records the map | — | recorded |
| 10 | P12 detected by an abort, not a named failure | the mutant run names an abort by the guard line it stopped on, and a pin's mutant counts only when it fails a named check or aborts within five lines of the pin; P12 aborts at line 3470, the family lookup it pins | `guards_check.py --mutants` | §26.7 |
| 11 | PR body stale | refreshed to this plan | — | done |
| 12 | Notation: the owner's sentence has $\mathcal S$, the plan prints $S$ | owner question (§26.8), answered (§27) | — | plain $S$ (owner, c.7061062574) |

### 26.2 Regenerated artifacts

| Path | Rebuilt by | Compared |
|---|---|---|
| `papers/{Computation,GR,Main,Methodology,SM,Structure,Substratum}.tex`, `book/The-Incompleteness-of-Observation-FULL.tex` | `build.sh`'s TeX recipe (pandoc 3.1.3 `-s --pdf-engine=xelatex --include-in-header=tools/unicode-fix.tex`, `--toc --metadata=toc:false` for the book, then the `% source-sha256:` stamp) | byte for byte with the candidate's file, after a base control that reproduces the base TeX |
| the eight PDFs of the same sources | `sh ./build.sh Computation GR Main Methodology SM Structure Substratum` and `sh ./build.sh --book` in CI | no `Missing character`, `build: OK`, page counts recorded against the base build; each committed PDF equal to the CI-built one in page count and `pdftotext` text (`--pdf-compare`) |
| `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` | the SC-42 checker on the candidate (§11 item 13) | byte for byte, plain and `-O`; self-test equal to the unchanged controls |
| the fingerprints of the four stale coverage entries | `tools/proof_census.py --json` on the candidate | value for value; the rest of `verification/coverage/LEDGER.json` byte for byte |

A change to the level or delta of `MAIN:L-3` or `SUBSTRATUM:T-23` on re-reading (§11 item 4) is not in this list; it
needs a ledger re-cut and a new acceptance.

### 26.3 CI on the exact post-deletion tree

In this order, and only with owner approval for the branch push and the dispatch (§A.43 item 4); nothing here is run:

1. **Plan commit.** A commit `P` on this branch is proposed for designation; `preserve_check.py --verify-pins` and
   `--verify-ledger` pass at `P`.
2. **Predicted tree.** `guards_check.py --predict <dir>` from `P` writes the tree the ledger predicts. The CI branch
   head is a single-parent child of the ledger base whose tree is that tree with the eight PDFs rebuilt by `build.sh`
   on the canonical toolchain, less the execution result note.
3. **Checks on that exact head.** `preserve_check.py`, run from its own path in a worktree of `P` (or of the head,
   whose record copy must equal `P`'s), as `--commit <head> --plan P`, passes; the job also runs
   `sh ./build.sh Computation GR Main Methodology SM Structure Substratum` and `sh ./build.sh --book` on a copy of the
   head and requires every regenerated `.tex` byte-identical to the committed one, every PDF built with no
   `Missing character` and page counts recorded, and the committed PDFs to be the ones that job builds:
   `preserve_check.py --tree <head checkout> --pdf-compare <build copy>` requires each committed PDF's page count and
   `pdftotext` text to equal the built one's (the PDF bytes carry build dates and are not compared); `verify.yml` is dispatched on the head (`workflow_dispatch`) and every job
   is green, its SC-42 step (`cmp` of the regenerated result) included.
4. **Designation.** The owner designates `P` only after step 3 is green on the tree predicted at `P`. Any later change
   to a pinned file of §26.4 voids that run.

### 26.4 Record pins

The digests below pin the record files at this commit. `preserve_check.py` verifies them before use, reading them from
the plan commit under `--plan`.

| File | SHA-256 |
|---|---|
| `edits.json` | `d40c84d52b19f15d2644351337ac19273017f248aa02e0a9ad3233a9b99a45c5` |
| `ledger.json` | `41ac4fd9fbcf4485d34a9aa1c1b46899a86c9a88503b65208e785af2412ff0f6` |
| `edits_check.py` | `4e6cb79a71bfc9dfacd897df82a325aa8482908531bf94010a14afe7d947a8a3` |
| `guards_check.py` | `2685bd16f9cb3c1d1ce8d386cc3ba9bb8eef9dad63f66f2a2edbb277e29315fe` |
| `preserve_check.py` | `67d8dd9832ab19ead13ade999c03f6f5f82ecd333d04f5d63a63181cff6e5a74` |

### 26.5 Kernel identifiers in the guard's code literals

These name kernel declarations whose names contain A1. They sit in code literals of the R7 guard, not in check
messages, so the owner's ruling on the two messages does not cover them. They are listed here, with the test each
passes, and are put to the owner (§26.8); #1482's renames must update every one.

| Guard line | Identifier | Target | Polarity | Test (mutation fails) |
|---|---|---|---|---|
| 3380 | `a1_every_theory` | `OIBridge/ManuscriptAxioms.lean` | + | `a1_every_theory` renamed in the target |
| 3380 | `substratumTheory_A1` | `OIBridge/ManuscriptAxioms.lean` | + | `substratumTheory_A1` renamed in the target |
| 3380 | `substratumTheory_A1A2` | `OIBridge/ManuscriptAxioms.lean` | + | `substratumTheory_A1A2` renamed in the target |
| 3389 | `A1Realized` | `OIBridge/ManuscriptAxioms.lean` | + | `A1Realized` renamed in the target |
| 3389 | `A1A2Realized` | `OIBridge/ManuscriptAxioms.lean` | + | `A1A2Realized` renamed in the target |
| 3392 | `A1Realized` | `OIBridge/ManuscriptAxioms.lean` | + | `def A1Realized` altered in the target |
| 3467 | `A1Realized` | `papers/Main.md` | − | the name inserted into the target |
| 3476 | `A1Realized` | `verification/README.md` | + | `A1Realized` renamed in the target |
| 3667 | `a1_of_finite` | `OIBridge/SubstratumInterfaceAudit.lean` | + | `a1_of_finite` renamed in the target |
| 3667 | `waveSubstratum_A1` | `OIBridge/SubstratumInterfaceAudit.lean` | + | `waveSubstratum_A1` renamed in the target |
| 10978 | `cx3b_complex_not_A1` | `OIBridge/A6Instantiation.lean` | + | `theorem cx3b_complex_not_A1 (d L : ℕ)` altered in the target |
| 11216 | `cx3b_complex_not_A1` | `verification/programmes/substratum/a6-instantiation/result.md` | + | `\| `cx3b_complex_not_A1` \| `[propext, Classical.choice, Quot.sound]` \|` altered in the target |

### 26.6 Edit-ID map of the preserved work

The work kept at `preserve/w1477-565965f1` (parent `5e818088`) numbered its new edits D349–D356. They entered this
branch as single-parent commit `2b45ee72`, renumbered by +2 because `6946c967` had used D349–D350: there D349 → D351,
D350 → D352, D351 → D353, D352 → D354, D353 → D355, D354 → D356, D355 → D357, D356 → D358, with the same file, old and
new text. The new edits of this section are D359–D360.

### 26.7 Checks at `97070c98`

| Command | Result |
|---|---|
| `edits_check.py --self-test` | PASS (93 countercontrols) |
| `edits_check.py --static` | infinity 0, register 0, capitals 0, identifier 0, preservation 0, mirror parity 0, Lean docstring-only 0, sitemap 194/194; PASS |
| `edits_check.py --commit 97070c98 --simulate` | uniqueness 360/360; residual 5 (all allowed), unscoped 0, preservation 0, identifier 0; PASS |
| `edits_check.py --pins --commit 97070c98` | 0 unresolved, 0 updated pins missing from their targets; PASS |
| `edits_check.py --repo-scan --simulate --final --commit 97070c98` | 0 unexplained; PASS |
| `preserve_check.py --verify-pins`, `--verify-ledger` | pin findings 0; ledger (358 splices in 40 files, 2 retained-site records) re-derived identically; PASS |
| `preserve_check.py --self-test` | five positive controls pass (the recipe reproduces the base TeX of all eight sources; base plus ledger, rebuilt artifacts and the plan's record; an execution record under `execution/`; a rebuilt PDF; a PDF equal in pages and text to the built one); 30 mutants (23 tree mutations, 2 ledger tamperings, 3 pin tamperings, 2 PDF mismatches) each fail as named; PASS |
| `guards_check.py --mutants` | on the simulated tree: the R7 guard, `bohr_frequency_probe.py` and the 12 other checks pass; CC-1–CC-4 fail as named; inventory 0 unlisted (30 pins, 2 messages naming declarations, 12 kernel identifiers in code literals); P01–P30 each fail under mutation, P12 by an abort at line 3470; the 12 kernel identifiers and the 3 message names each fail their guard under mutation; PASS |
| `guards_check.py --predict`, then `preserve_check.py --tree <predicted> --mutants` | predicted tree: 40 files edited, 8 TeX rebuilt, 4 fingerprints re-affirmed, record directory copied, SC-42 result regenerated (it differs from the checked-in result); `verify.yml`'s SC-42 comparisons pass on it; `preserve_check.py`: 0 findings; tree mutants (GR.tex, the SC-42 result, `ledger.json`, `preserve_check.py`, a coverage fingerprint) each fail; PASS |

Not run here: the PDF build (no `xelatex` in this environment), the Lean kernel and Mathlib builds, the release gate
on the predicted tree, and the rest of `verify.yml`; they are the CI step of §26.3.

### 26.8 Owner questions

Answered by the owner at #1169 comment 7061062574 (§27): the kernel identifiers of §26.5 and the two declaration names
are retained temporarily and #1482 migrates every one; the sentence is printed with plain $S$, as recorded.

## 27. Amendment: owner decisions of #1169 comment 7061062574, and the delta-check nits

**Owner decision** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7061062574](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7061062574)), in part:
the existing `A1` kernel identifiers stay unchanged during the deletion, the two declaration names and the twelve
identifiers of §26.5 included, and #1482 must migrate every inventoried name, with no permanent exception; notation
(a), the recorded sentence with plain `S`; the non-native safeguards route is approved for #1477; the predicted-tree CI
trial is authorized as a preparation run, after the two delta-check nits are fixed; applying the edits is still not
authorized.

**Delta-check nits** (#1477 comment 7060370712).

| Nit | Fix |
|---|---|
| A. §26.3's "`git show P:…/preserve_check.py` run" does not run: the script derives its root and record directory from its own path | §26.3 step 3 runs it from its own path in a worktree of `P`, or of the head whose record copy equals `P`'s |
| B. The PDFs are not compared with the CI build | `preserve_check.py --tree <head checkout> --pdf-compare <build copy>`: each committed PDF of a ledgered source must have the page count (`pdfinfo`) and the `pdftotext` text of the PDF the CI build makes from the same tree; the bytes carry build dates and are not compared. Self-test: equal PDFs pass, a different PDF fails, a missing built PDF fails |

**Goal link (§A.47).** A1-EXIT (#1169): this section prepares the authorized predicted-tree CI trial; it decides no
execution question.

## 28. Amendment, preregistered: the A1-retirement scope fixes of the classification review, structured checker output, the corrected trial

**Owner decision** (owner `amaybaum`, 2026-11-21, recorded at
[#1169 comment 7062144714](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7062144714)), item 2 in
part: "#1477 amendment, scope (a)", covering, for trial verification, "a corrected trial commit whose parent is the
ledger base; PDFs built by the #1484 workflow; structured output from the checkers", and the two scientific fixes of
the classification review (#1477 comment 7061693815): "'finite $C_H$' stated where Theorem 24(i) and the classical case
of (iii) use the uniform prior; Theorem 24(iii) narrowed to factors with bijective dynamics (A2), together with its
mirrors (Substratum, Structure, ch02, FULL) and the Substratum:54 sentence". Item 4: applying the A1-retirement edits
remains unauthorized. #1484 is merged into `main` as `df6da1c6`.

**Goal link (§A.47).** A1-EXIT (#1169): this amendment decides whether the plan states every finite-only use of
Theorem 24 and only the membership the proof supports, and whether the trial evidence is complete; it does not decide
execution.

This section is committed before any change to `edits.json`, the ledger or the checkers (§28.6 records the order).

### 28.1 Items

1. **(i) The D232 scope.** With the (A1) entry removed (D232), Theorem 24(i) at Sub:253 and the classical case of
   (iii) at Sub:262 use the uniform hidden prior $\mathbb{1}/|\mathcal{C}_H|$, which exists only for a finite
   $\mathcal{C}_H$. Each states that scope (D361, D362).
2. **(ii) Theorem 24(iii) narrowed to bijective dynamics (A2).** Membership in $\mathcal{G}_{\text{sub}}$ is stated for
   a factor of any cardinality evolved by a bijection of its configurations, so that the enlarged pair has bijective
   dynamics (A2); the channel identity for any unitary or isometry, or for a classical factor any measurable map, is
   stated separately as a channel-preserving extension (D362–D364, D368, D370–D373). Sub:249, Sub:201 and Str:154 are
   aligned in the same pass (D365, D366, D369).
3. **(iii) Sub:54** takes the reviewer's fuller wording (D367).
4. **(iv) Structured checker output.** `preserve_check.py` and `guards_check.py` write a result file: the checker, its
   mode, the plan commit, the ledger digest, the candidate, and for each check its name, status (`pass` or `fail`) and
   discrepancies, with the verdict. The path is `--result-json PATH`; when `RUNNER_TEMP/out` exists (the #1484 workflow
   creates it and uploads it), the file is also written there as `<checker>-<mode>.json`, so the merged workflow
   uploads it without change.
5. **(v) The corrected trial.** Built from the plan commit `P2` that carries this amendment:
   - `T0`: a single-parent child of the ledger base `97070c98` whose tree is `guards_check.py --predict` at `P2` (the
     base PDFs). `a1exit-trial-verify.yml` is dispatched on `T0`. Preregistered expectation: every step passes except
     `preserve`, whose only findings are `--pdf-compare` mismatches of the eight PDFs; the run uploads the eight
     CI-built PDFs.
   - `T1`: a single-parent child of `97070c98` whose tree is `T0`'s with the eight PDFs replaced by that artifact's.
     `a1exit-trial-verify.yml` and `verify.yml` are dispatched on `T1`; every step and job must pass.
   - Neither is built, pushed or dispatched before this amendment passes its independent delta review.

### 28.2 New edits

New IDs D361–D373; no retired or earlier ID is reused, and the ledger records each as a splice against `97070c98`.
Items (ii) and (iii) change text that S2-B (#1473) put on `main`; that text is at the ledger base, so each is a new
splice there.

| Edit | Site (base line) | Class | Old → new |
|---|---|---|---|
| D361 | Sub:253 | needs scientific review | *(i) Hidden-sector relabeling.* For any bijection $\sigma: \mathcal{C}_H \to \mathcal{C}_H$, → *(i) Hidden-sector relabeling.* For finite $\mathcal{C}_H$ and any bijection $\sigma: \mathcal{C}_H \to \mathcal{C}_H$, |
| D362 | Sub:262 | needs scientific review | evolved by any measurable map $w$, with product dynamics $\varphi\times w$ and the uniform hidden prior times $\alpha$ → evolved by a bimeasurable bijection $\psi$ of $A$, with product dynamics $\varphi\times\psi$ and the uniform hidden prior on a finite $\mathcal{C}_H$ times $\alpha$ |
| D363 | Sub:257 | needs scientific review | Adjoin a factor Hilbert space $\mathcal K_A$ of any dimension, prepared independently in a density matrix $\sigma_A$ with $\operatorname{Tr}\sigma_A=1$, and evolve it by a unitary or isometry $W$ with product dynamics $U\otimes W$. → Adjoin a classical factor $A$ of any cardinality, with $\ell^2(A)$ prepared independently in a density matrix $\sigma_A$ with $\operatorname{Tr}\sigma_A=1$, and evolve it by the permutation unitary $W$ of a bijection $\psi$ of $A$, with product dynamics $U\otimes W$; the enlarged pair $(S\times A,\varphi\times\psi)$ has bijective dynamics (A2). |
| D364 | Sub:262 | needs scientific review | such as the identity on an infinite-dimensional $\mathcal K_A$ or counting measure on an infinite $A$, is not covered. → such as the identity on an infinite-dimensional $\ell^2(A)$ or counting measure on an infinite $A$, is not covered. The identity, and its proof, hold unchanged for any unitary or isometry $W$ on a Hilbert space $\mathcal K_A$ of any dimension and, for a classical factor, any measurable map $w$; such enlargements are channel-preserving extensions, not members of $\mathcal{G}_{\text{sub}}$, when their dynamics is not a bijection of configurations. |
| D365 | Sub:249 | semantic | (i) and the normalized Hilbert-space product form of (iii) preserve the coherent family → (i) and the normalized permutation product form of (iii) preserve the coherent family |
| D366 | Sub:201 | semantic | finite decoupled deep-sector enlargement of arbitrary size → decoupled deep-sector enlargement by a normalized factor of any cardinality with bijective dynamics |
| D367 | Sub:54 | semantic | The exact normalized-product-ancilla identity of Theorem 24(iii) concerns finite added factors. → The exact normalized-product-ancilla identity of Theorem 24(iii) concerns independently prepared, exactly decoupled added factors of any cardinality in a normalized state or law; an unnormalizable or coupled factor is outside it. |
| D368 | Str:53 | needs scientific review | An independently prepared, normalized factor of any dimension with exactly decoupled unitary or isometric product dynamics may be adjoined → An independently prepared, normalized classical factor of any cardinality with exactly decoupled permutation product dynamics (the channel identity also holds for unitary or isometric factor dynamics, as a channel-preserving extension) may be adjoined |
| D369 | Str:154 | semantic | independently prepared finite decoupled ancillary enlargement as exact invariances → independently prepared decoupled ancillary enlargement by a normalized factor of any cardinality with bijective dynamics as exact invariances |
| D370 | ch02:144 | needs scientific review | Adjoin a factor of any dimension to the deep hidden sector, prepare it independently in a normalized density matrix, and keep its dynamics exactly decoupled from the original system, as any unitary or isometry of the factor. → Adjoin a classical factor of any cardinality to the deep hidden sector, prepare it independently in a normalized density matrix, and keep its dynamics exactly decoupled from the original system, as a permutation of the factor's configurations; the identity also holds for any unitary or isometry of the factor, which is a channel-preserving extension rather than a member of the group. |
| D371 | FULL:774 (mirror of D370) | needs scientific review | Adjoin a factor of any dimension to the deep hidden sector, prepare it independently in a normalized density matrix, and keep its dynamics exactly decoupled from the original system, as any unitary or isometry of the factor. → Adjoin a classical factor of any cardinality to the deep hidden sector, prepare it independently in a normalized density matrix, and keep its dynamics exactly decoupled from the original system, as a permutation of the factor's configurations; the identity also holds for any unitary or isometry of the factor, which is a channel-preserving extension rather than a member of the group. |
| D372 | ch02:144 | needs scientific review | A classical factor with a probability law and any measurable dynamics likewise preserves the channel family, read as the mixture over hidden points of [Main §3.2], and every rooted population law. → A classical factor with a probability law and a bimeasurable bijection as its dynamics likewise preserves the channel family, read as the mixture over hidden points of [Main §3.2], and every rooted population law; with any measurable dynamics the identity still holds, as a channel-preserving extension. |
| D373 | FULL:774 (mirror of D372) | needs scientific review | A classical factor with a probability law and any measurable dynamics likewise preserves the channel family, read as the mixture over hidden points of [Main §3.2], and every rooted population law. → A classical factor with a probability law and a bimeasurable bijection as its dynamics likewise preserves the channel family, read as the mixture over hidden points of [Main §3.2], and every rooted population law; with any measurable dynamics the identity still holds, as a channel-preserving extension. |

### 28.3 Finiteness terms removed by the new edits (classification as in #1477 c.7061693815)

| Edit | Term removed | Class | Reason |
|---|---|---|---|
| D366 | "finite … of arbitrary size" | C | the identity needs normalization only (proof of Theorem 24(iii), Sub:266); the narrowed membership is stated |
| D367 | "finite added factors" | C | as D366; the reviewer's wording keeps independent preparation, exact decoupling and normalization |
| D369 | "finite decoupled" | C | as D366 |

D361 and D362 add a finite scope; D363, D364, D368 and D370–D373 narrow membership; D365 removes no term.

### 28.4 Preregistered checks and decision rule

The amendment passes only if all of the following hold at `97070c98`, each from the checkers at `P2`:

1. `edits_check.py --self-test`, `--static`, `--commit 97070c98 --simulate`, `--pins --commit 97070c98` and
   `--repo-scan --simulate --final --commit 97070c98` pass, with uniqueness over every record.
2. `preserve_check.py --verify-pins`, `--verify-ledger` and `--self-test` pass; the ledger is re-cut and its digest and
   the pins re-frozen in §26.4.
3. `guards_check.py --mutants` passes (the guards, the H-B checks R7-HYB and R7-HYE, the countercontrols, the
   inventory and the pin, kernel-identifier and message-name mutants).
4. `guards_check.py --predict`, then `preserve_check.py --tree <predicted> --mutants`, passes.
5. The structured result files are written and parse, and a failing check is recorded as `fail` (a self-test control).
6. The finiteness-term removals of the new edits are exactly those of §28.3.

A failure of any item stops the amendment; it is not re-run with changed thresholds.

### 28.5 Not changed

The design is unchanged: A1 stays retired, no optional A1 hypothesis is introduced, D001–D360 keep their text, and
the frozen H-B sentence stays.

### 28.6 Order

1. This section (preregistration).
2. The edits of §28.2 in `edits.json`, the checkers' result output, the re-cut ledger and pins, and the results of
   §28.4 (§28.7).
3. The independent delta review, then the corrected trial of §28.1 item 5.

### 28.7 Results at `97070c98`

Each check of §28.4 was run from the checkers in this record directory. The record pins of §26.4 are re-frozen; the
ledger has 371 splices in 40 files (373 edit records; D032 and D039 retain their text).

| §28.4 item | Result |
|---|---|
| 1 | `edits_check.py`: `--self-test` PASS (93 countercontrols); `--static` 0 findings in every scan, preservation of the ten new required texts included, sitemap 194/194; `--commit 97070c98 --simulate` 373/373 unique, residual 5 (all allowed), 0 unscoped, 0 preservation, 0 identifier; `--pins` 0/0; `--repo-scan --simulate --final` 0 unexplained |
| 2 | `preserve_check.py --verify-pins` PASS, `--verify-ledger` identical, `--self-test` PASS (38 recorded checks, none failing) |
| 3 | `guards_check.py --mutants` PASS: the 14 checks on the simulated tree (R7, with R7-HYB and R7-HYE, and F71 among them), CC-1–CC-4 failing as named, inventory 0 unlisted, P01–P30, the 12 kernel identifiers and the 3 message names each failing under mutation; 64 recorded checks, none failing |
| 4 | `guards_check.py --predict`, then `preserve_check.py --tree <predicted> --mutants`: PASS, 0 findings, the 5 tree mutants failing as required |
| 5 | Every run wrote its result file, and each parses; the self-test's result-file control (a failing check recorded as `fail` with its discrepancy, verdict `fail`) passes. A tree check run while the record directory differed from the plan recorded the finding as `fail` |
| 6 | The new edits remove "finite" in D366, D367 and D369 only, as §28.3 lists |

Not run here: the corrected trial of §28.1 item 5, which waits for the independent delta review.

## 29. Amendment: the corrected-trial design (delta-review nits N1 and N2)

The independent delta review of §28 at `453917f1` is recorded on #1477 (comment 7062890492), CONFIRMED WITH NITS. This
section is append-only. It corrects §28.1 item 5 and changes no ledger entry, edit text or checker. The owner has held
the trial (#1169 comment 7062890214); nothing here builds, pushes or dispatches it.

**Goal link (§A.47).** A1-EXIT (#1169): this section fixes what the preregistered trial expects and from which refs it
runs; it decides no execution question.

1. **N1: the `T0` expectation.** In `a1exit-trial-verify.yml` the `guards` step has no `always()` condition, so after
   `preserve` fails it is skipped, and the final gate fails. The preregistered expectation for `T0` is therefore:
   `preserve` fails with only `--pdf-compare` findings for the eight PDFs; `guards` is skipped; `result.json` and the
   PDF upload are written. `guards` is covered on `T1`, where every step must pass.
2. **N2: the dispatch refs.** `a1exit-trial-verify.yml` entered `main` at `df6da1c6`; `97070c98` does not contain it.
   - `T0` and `T1` are each verified by dispatching `a1exit-trial-verify.yml` from `main` (`df6da1c6` or later) with
     `trial_sha` set to that trial commit and `plan_sha` set to the plan head.
   - `verify.yml` on `T1` is dispatched on a branch whose head is exactly `T1`.
3. **N3 and N4 are not applied.** They are deferred to the final scientific review: N3, adding "with
   $\operatorname{Tr}\sigma_A=1$" to D364's channel-preserving extension; N4, a finite scope on the book and Structure
   summaries of Theorem 24(i) (ch02:134 = FULL:766, ch03:80/136 = FULL:943/999, Structure:154).

## 30. Amendment: one plan commit P* for the corrected trial

The check of §29 at `1cde4d8f` is recorded on #1477 (comment 7062917018), REVISE. §28.1 item 5 builds `T0` at
`P2` = `453917f1`, while §29 dispatches with `plan_sha` set to the plan head, which is now `1cde4d8f`. The tree check
compares the record directory with the plan's, so the differing PREREG.md would add a non-PDF finding, and N1's
expectation would fail. This section is append-only. It replaces the plan commit named in §28.1 item 5 and §29 item 2,
and changes no ledger entry, edit text or checker. Nothing here builds, pushes or dispatches the trial, which the owner
has held (#1169 comment 7062890214).

**Goal link (§A.47).** A1-EXIT (#1169): this section fixes which plan commit the trial is built from and checked
against; it decides no execution question.

1. **One plan commit.** `T0` and `T1` are both predicted from the same plan commit `P*`: `guards_check.py --predict`
   runs at `P*`, the trial trees carry `P*`'s record directory, and `P*` is passed as `plan_sha` to every
   `a1exit-trial-verify.yml` dispatch of `T0` and `T1`.
2. **How `P*` is fixed.** `P*` is the head of `research/a1exit-deletion-20261121` at the moment `T0` is built, and it
   is recorded with `T0`. This section moves the head, so `P*` is the commit carrying §30, or a later one if a review
   asks for more; it is never `453917f1` or `1cde4d8f`.
3. **No movement in between.** The plan branch does not move between building `T0` and the last dispatch on `T1`
   (`a1exit-trial-verify.yml` and `verify.yml`). If it moves, `T0` and `T1` are rebuilt from the new head, which
   becomes `P*`, and the dispatches are repeated against it.

## 31. Amendment, preregistered: the final scientific review's corrections, and reconciliation to `53c6601a`

**Owner decisions.** Owner `amaybaum`, 2026-11-22T05:19:53Z,
[#1169 comment 7074687817](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7074687817),
"Owner decisions on the final scientific review (#1477 c.7074137435), the A1 correction route and P2-C Node 1", quoted
in part:

> | Item | Decision |
> |---|---|
> | #1494, book Theorem 24(i) | APPROVE landing first, subject to an exact-head independent review, green CI and a clean merge |
> | §31 append-only amendment | AUTHORIZE preparation |
> | D026, D364, F4 and F7 corrections | AUTHORIZE within the amendment |
> | D022 restriction | APPROVE, explicitly keeping the open H-cont obligation |
> | Independent §31 delta review | REQUIRED |
> | New T0′/T1′ trial | REQUIRED |
> | Retirement execution | NOT AUTHORIZED |
> | F6, C2-mixing and Sub:129/135 | AUTHORIZE separate correction preparation and review; no merge yet |
>
> **§31 requirements.** The amendment must:
> - keep the original frozen ledger and the T0/T1 evidence unchanged;
> - state the corrected D026 distinction between an available mathematical return formulation and the still-unsourced return hypothesis X-21;
> - correct D364's normalization assumption, including `Tr σ_A = 1`;
> - apply the necessary finite-`C_H` restrictions to the affected summary sites;
> - correct Sub:94 so its conclusion does not exceed its finite premise;
> - include the accepted Sub:257 wording correction and the applicable review nits;
> - keep traceability from each review finding to its exact correction.
>
> F6 is not incorporated into the retirement.
>
> [...] T0′/T1′ run against the amended, independently reviewed plan. The original evidence is kept as a historical
> baseline. [...] The previous T1's successful checker results do not establish acceptance of T1′.

Owner `amaybaum`, 2026-11-22T05:34:52Z,
[#1169 comment 7074829849](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7074829849),
"Owner decision: the #1494 merge record is accepted, and §31 continues under its existing scope", quoted in part:

> - **60 failing splices.** Rebuilding the ledger and re-pinning the base hashes is necessary. Applying the old plan to `53c6601a` would not be valid.
> - **Three additional summary sites.** ch04:172, Complexity:206 and Methodology:353 are included in the scope audit and the traceability table.
> - **Stale `FULL.pdf`.** Tracking it in #1539 is acceptable for now, but the corrected PDF must be rebuilt and verified before the retirement is considered complete.
> - **Historical evidence.** P* and the original T0/T1 receipts are kept unchanged.
>
> **Additional safeguard.** The reconciliation must separate the legitimate changes caused by #1494 from unrelated drift. Every changed splice gets an explicit explanation. A passing checker alone is not sufficient scientific evidence.

The route is that of c.7074687817 item 4: #1494 lands first (merged as `53c6601a`, recorded at #1169 c.7074755696),
then this amendment and its independent delta review, then T0′/T1′, then a separate execution decision.

**Goal link (§A.47).** A1-EXIT (#1169): this amendment decides whether the plan, moved to the base `53c6601a`, keeps
every finite-only result finite-scoped at every site the final scientific review names, states the open return and
continuation conditions as open, and explains every changed splice; it does not decide execution.

**Order.** As in §28: this section is committed first; the edit-list, ledger and checker changes follow in later
additive commits; the results of §31.7 are recorded in §31.10 and the record pins in §31.11. No earlier section is
edited: where an earlier count, base or pin table differs from this section, this section governs, and the earlier text
stays as the record of P*.

### 31.1 New base and the historical baseline

- **H** = `53c6601a10419b6b333cc992474272501ab542af`, the merge of #1494 (parents `fd9f99cc` and `98e55009`). Since the
  ledger base `97070c98` `main` merged #1484 (`df6da1c6`, the dispatch-only trial workflow), #1533 (`3a12f785`, the T0
  evidence), #1537 (`fd9f99cc`, the T1 evidence) and #1494 (`53c6601a`).
- **Files changed between `97070c98` and H.** `.github/workflows/a1exit-trial-verify.yml` (added); the T0 and T1
  evidence directories `verification/audits/foundations/a1exit-trial-t0-20261121/` and `-t1-20261121/` (added);
  `book/ch02-substratum.md` and `book/The-Incompleteness-of-Observation-FULL.md` (one paragraph each, Theorem 24(i));
  `book/The-Incompleteness-of-Observation-FULL.tex` (regenerated by #1494); and
  `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` (regenerated
  by #1494, one mirror entry). No other file differs. Of these, only the two book sources are ledgered files; the TeX
  and the SC-42 result are regenerated artifacts that `preserve_check.py` compares with their rebuild on the candidate
  (the TeX base control rebuilds H's `FULL.md` and must reproduce H's `FULL.tex`).
- **Historical baseline.** P* = `55544cc36dee5b7dd5b9079c0f03be24b74c137f`, its `ledger.json` (SHA-256
  `41ac4fd9fbcf4485d34a9aa1c1b46899a86c9a88503b65208e785af2412ff0f6`, base `97070c98`), the §26.4 pins and the T0/T1
  evidence on `main` under `verification/audits/foundations/a1exit-trial-t0-20261121/` and `-t1-20261121/` are kept
  unchanged. They record that the P* plan applied correctly at `97070c98`; they do not apply at H (60 of P*'s splices
  fail their span check there, §31.2) and they do not establish acceptance of T1′.

### 31.2 Reconciliation record (§9 at H)

**Step 1.** H is recorded above. The Step-2 merge commits are those of §24.1 and are ancestors of H.

**Step 2, and the cause of every changed splice.** At H every `old` string of the 373 P* records occurs exactly once
(`edits_check.py --commit H`: 373/373). P*'s ledger, validated against H, fails the span check for exactly 60 splices:
every one lies in `book/ch02-substratum.md` or `FULL.md` after the paragraph #1494 replaced. #1494 replaced ch02 bytes
32514–32755 by bytes 32514–32876 and FULL bytes 177795–178036 by bytes 177795–178157, a net change of +121 bytes in each
file and no change of line count. For each of the 60 splices: its old text is byte-identical at H, occurs once, starts
exactly 121 bytes later, on the same line, and does not overlap the replaced paragraph; its new text is unchanged. So the
only change is the byte offset, caused by #1494, and the claim, scope and class of each replacement are unchanged because
neither its old nor its new bytes change. No splice changed for any other reason: drift 0. No splice outside these two
files fails, and the ledger's base hashes differ at H only for these two files. The comparison is the mode
`preserve_check.py --reconcile P*` added by this amendment (§31.6), which classifies each P* splice as unchanged,
shifted by the preceding change or drift, and fails on any drift.

| Edit | Site at H | Span start, P* → H | Shift | Cause | Class |
|---|---|---|---|---|---|
| D371 | FULL:774 | 179084 → 179205 | +121 | #1494 (byte shift only) | needs scientific review, unchanged |
| D373 | FULL:774 | 179546 → 179667 | +121 | #1494 (byte shift only) | needs scientific review, unchanged |
| D131 | FULL:788 | 183842 → 183963 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D133 | FULL:842 | 203592 → 203713 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D135 | FULL:895 | 218924 → 219045 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D137 | FULL:905 | 222912 → 223033 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D139 | FULL:905 | 223125 → 223246 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D141 | FULL:905 | 223241 → 223362 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D143 | FULL:945 | 233675 → 233796 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D145 | FULL:1087 | 282637 → 282758 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D147 | FULL:1114 | 288498 → 288619 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D149 | FULL:1130 | 293788 → 293909 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D151 | FULL:1130 | 294192 → 294313 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D153 | FULL:1130 | 294341 → 294462 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D155 | FULL:1330 | 359471 → 359592 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D157 | FULL:1334 | 361980 → 362101 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D159 | FULL:1338 | 362794 → 362915 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D161 | FULL:1398 | 378063 → 378184 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D163 | FULL:1404 | 379004 → 379125 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D165 | FULL:1907 | 492808 → 492929 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D167 | FULL:1983 | 517699 → 517820 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D169 | FULL:2433 | 598496 → 598617 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D171 | FULL:2451 | 601690 → 601811 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D256 | FULL:2519 | 616419 → 616540 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D173 | FULL:2521 | 616491 → 616612 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D175 | FULL:2597 | 627105 → 627226 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D177 | FULL:2603 | 628372 → 628493 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D258 | FULL:2605 | 628897 → 629018 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D179 | FULL:2607 | 628975 → 629096 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D360 | FULL:2607 | 629043 → 629164 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D181 | FULL:2607 | 629353 → 629474 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D252 | FULL:4771 | 960916 → 961037 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D183 | FULL:5196 | 1070106 → 1070227 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D185 | FULL:5282 | 1094641 → 1094762 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D187 | FULL:5284 | 1095359 → 1095480 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D189 | FULL:5286 | 1095937 → 1096058 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D191 | FULL:5430 | 1132171 → 1132292 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D193 | FULL:6171 | 1269263 → 1269384 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D195 | FULL:6251 | 1286299 → 1286420 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D197 | FULL:6253 | 1286374 → 1286495 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D199 | FULL:6257 | 1286978 → 1287099 | +121 | #1494 (byte shift only) | needs scientific review, unchanged |
| D201 | FULL:6259 | 1287176 → 1287297 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D203 | FULL:6261 | 1288488 → 1288609 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D205 | FULL:6263 | 1289280 → 1289401 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D207 | FULL:6263 | 1289661 → 1289782 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D209 | FULL:6265 | 1290224 → 1290345 | +121 | #1494 (byte shift only) | needs scientific review, unchanged |
| D211 | FULL:6267 | 1290560 → 1290681 | +121 | #1494 (byte shift only) | needs scientific review, unchanged |
| D213 | FULL:6267 | 1290809 → 1290930 | +121 | #1494 (byte shift only) | needs scientific review, unchanged |
| D215 | FULL:6269 | 1290918 → 1291039 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D217 | FULL:6271 | 1291267 → 1291388 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D219 | FULL:6291 | 1294424 → 1294545 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D247 | FULL:6293 | 1294826 → 1294947 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D236 | FULL:6502 | 1335300 → 1335421 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D221 | FULL:6504 | 1335971 → 1336092 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D238 | FULL:6562 | 1355451 → 1355572 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D223 | FULL:6628 | 1374128 → 1374249 | +121 | #1494 (byte shift only) | semantic, unchanged |
| D370 | ch02:144 | 33803 → 33924 | +121 | #1494 (byte shift only) | needs scientific review, unchanged |
| D372 | ch02:144 | 34265 → 34386 | +121 | #1494 (byte shift only) | needs scientific review, unchanged |
| D130 | ch02:158 | 38561 → 38682 | +121 | #1494 (byte shift only) | mechanical, unchanged |
| D132 | ch02:212 | 58311 → 58432 | +121 | #1494 (byte shift only) | mechanical, unchanged |

**Step 3, redrafts.** No `old` string fails or changed at H, so no record is redrafted because of the base. The five
records whose replacement changes (D026, D231, D363, D364, D369) are revised because of the findings of §31.3, not because
of the base; D369's `old` is extended to the clause before it (§31.3). Each carries a `revised` field.

**Step 4, the ledger site map.** `ledger_check.py build` reads the working tree and writes its record's `sitemap.json`
(pin `e837e3db`), a record on `main` that this plan does not edit. It is run on a scratch export of H, and the rebuilt
ptr-site set is compared with the frozen map: #1494 changed one line in ch02 and one in FULL, neither carrying a pointer
pattern, and the line count of neither file changed, so the expectation is the same 194 ptr sites at the same lines.
The new records are of kind `consistency` and are not ptr sites. The sitemap cross-check of `--static` reads the base
lines at H.

**Steps 5 and 6** are §31.7 items 1–4.

**Re-pins.** The ledger is re-cut at H: `edits.json`'s `drafting_base` becomes H (`previous_base` `97070c98`), and
`preserve_check.py --build-ledger` writes new spans and the base hashes of every ledgered file at H, including ch02 and
FULL. `FULL.tex` and the SC-42 result carry no base hash: the candidate's copy is compared with its rebuild on the
candidate. The record pins move to §31.11, which `preserve_check.py` reads (§31.6); §26.4 stays as P*'s pins.

### 31.3 Findings and their corrections

Line numbers are lines of the file at H. "FR" is the final scientific review (#1477 c.7074137435); "N1–N3 (#1494)" the
exact-head review of #1494 (#1494 c.7074737862); "N3/N4 (§29)" the delta-review nits deferred in §29 item 3.

| Finding | Edit | Site | Old → new (summary) |
|---|---|---|---|
| FR F1 (Stage 1 and Stage 3 in D026) | D026 (revised) | Sub:216 | P*'s "used by Stage 1's exact return and Stage 3's count; … a form of those stages for a substratum of unspecified cardinality … is not developed" → the two steps with no established form for a substratum of unspecified cardinality: Stage 1's exact rooted return $\Gamma_n=I$ after a non-permutation rooted map, whose step to P-indivisibility holds for a hidden prior on a measurable carrier of any cardinality (Main's Corollary (near-return), of which an exact return is a case), with (NR) a weaker sufficient condition for that conclusion, assumed and not adopted, and the source of the return hypothesis open (LEDGER X-21); Stage 3's count under H-count [GR §2.3]; E3 does not establish finiteness of $S$; no effective-finiteness argument |
| FR F2 (D022 companion, owner's restriction) | D026 (revised); D022 unchanged | Sub:216; Sub:193 | the restricted sentences appended to the same bullet: Theorem 23 keeps its finite-substratum hypothesis; Stage 2's local results are also stated on $\mathbb{Z}^d$ under their named hypotheses [SM §4.1]; the pole and continued-response statements (Lemma 1c(ii), Proposition 4b) additionally need a meromorphic continuation of the memory-resummed Schur complement that is not established (the open H-cont obligation, stated by its content); these do not extend the complete theorem |
| FR F3 = N3 (§29) | D364 (revised) | Sub:262 | "hold unchanged for any unitary or isometry $W$ on a Hilbert space $\mathcal K_A$ of any dimension and, for a classical factor, any measurable map $w$" → "hold unchanged for any density matrix $\sigma_A$ with $\operatorname{Tr}\sigma_A=1$ on a Hilbert space $\mathcal K_A$ of any dimension evolved by a unitary or isometry $W$ and, for a classical factor with $\alpha(A)=1$, any measurable map $w$" |
| FR F3 nit (Sub:257) | D363 (revised) | Sub:257 | "with $\ell^2(A)$ prepared independently in a density matrix $\sigma_A$ with …" → "prepared independently in a density matrix $\sigma_A$ on $\ell^2(A)$ with …" |
| FR F4 = N4 (§29) | D369 (revised) | Str:154 | `old` extended to "uniform hidden-coordinate relabelling and …"; "relabelling" → "relabelling of a finite $\mathcal{C}_H$"; the enlargement wording of §28 unchanged |
| FR F4 | D375, D376 | ch02:134 = FULL:764 | "uniform hidden-coordinate relabelling and independently prepared finite decoupled enlargement preserve" → "… relabelling of a finite $\mathcal{C}_H$ and …" |
| FR F4 | D377, D378 | ch02:172 = FULL:802 | "A uniform hidden-coordinate relabelling, with the uniform hidden prior," → "A uniform hidden-coordinate relabelling of a finite $\mathcal{C}_H$, with the uniform hidden prior," |
| FR F4 | D379, D380 | ch03:80 = FULL:941 | "A single hidden permutation used identically in every visible fibre" → "A single hidden permutation of a finite $\mathcal{C}_H$ used identically in every visible fibre" |
| FR F4 | D381, D382 | ch03:136 = FULL:997 | "A uniform hidden-coordinate relabelling preserves" → "A uniform hidden-coordinate relabelling of a finite $\mathcal{C}_H$ preserves" |
| FR F4 | D383, D384 | ch03:142 = FULL:1003 | "A uniform hidden-coordinate relabelling, or" → "A uniform hidden-coordinate relabelling of a finite $\mathcal{C}_H$, or" |
| N3 (#1494) | D385, D386 | ch04:172 = FULL:1276 | "Uniform hidden relabelling and an independently prepared finite decoupled enlargement give exact examples" → "Uniform hidden relabelling of a finite $\mathcal{C}_H$ and …" |
| N3 (#1494) | D387 | Complexity:206 | "uniform hidden relabelling preserves the coherent channel under its stated preparation" → "uniform relabelling of a finite set of hidden configurations preserves …" (the paper does not use $\mathcal{C}_H$) |
| N3 (#1494) | D388 | Methodology:353 | "a permutation of the hidden states applied uniformly in every visible fibre" → "a permutation of a finite set of hidden states applied uniformly in every visible fibre" |
| FR F5 | none in this plan | ch02:140 = FULL:770 | landed by #1494 (`53c6601a`) before this amendment; the plan's edits do not touch it, and §31.7 item 6 asserts it in the predicted tree |
| FR F6 | none | — | excluded: "F6 is not incorporated into the retirement" (c.7074687817); separate stream |
| FR F7 | D374 | Sub:94 | "…restricting to a bijection on that image. Bijectivity … is thus partly structural," → "…restricting to a bijection on that image; for $S$ of unspecified cardinality bijectivity is the reversibility posit (REV) of [Main §4.5]. Bijectivity … is thus, for a finite $S$, partly structural," |
| FR nit 5 | D389 | SM:252 (Lemma 1c) | "the selected counting measure of [Main] Lemma 3," → "… of [Main] Lemma 3 on a finite representative," |
| FR nit 5 | D390 | SM:334 (Proposition 4b) | "take the selected counting measure," → "take the selected counting measure on a finite representative," |
| FR nit 5 | D391 | SM:641 (Theorem 19) | "let the hidden prior be the counting measure." → "… the counting measure on a finite $\mathcal{C}_H$." |
| FR nit 6 | D231 (revised) | Main:60 | "to every representative reached from it by …" → "to every representative, or channel-preserving extension, reached from it by …" |
| N1 (#1494) | none | `FULL.pdf` | the corrected PDF is T1′'s CI-built `FULL.pdf` (§31.8); Issue #1539 |
| N2 (#1494) | ledger re-cut | ch02, FULL.md, FULL.tex, SC-42 | §31.2 re-pins; the SC-42 result is regenerated on the predicted tree, never taken from either side |

New IDs D374–D391 continue from D373; no ID is reused or renumbered. Every new record is of kind `consistency` with
`revised: "new at amendment §31"`. Classes: D374 needs scientific review; D375–D391 semantic; the revised records keep
their classes (D026, D231, D363, D364 needs scientific review; D369 semantic). Records: 391 (ptr 242, consistency 54,
handoff 5, lean-docstring 36, repo-active 35, guard-pin 19); splices 389 (D032 and D039 retain their text) in 41 files
(`papers/Complexity.md` added).

**Where the text differs from the review's, and why.**

1. *H-cont.* The label appears in no manuscript, only in verification records (O-A4). Printed in Substratum it would be
   an undefined identifier, the defect F6 names for "C2-mixing". The obligation is kept and stated by its content, as
   SM's Lemma 1c proof states it ("the pole reading assumes a meromorphic continuation of $\mathcal D$ that is not
   established here").
2. *[GR §3.1] → [GR §2.3].* H-count is stated at GR:58, in GR §2.3 ("Application"); §3.1 is the classical horizon
   temperature. Its finite scope is written "for a total system that is finite", the review's "finite total system"
   matching the residual pointer pattern P2.
3. *"an infinite configuration space" → "a substratum of unspecified cardinality".* The owner's infinity scan rejects
   "infinite configuration space" in a replacement; the plan's cardinality-neutral wording (P*'s D026, Sub:94) carries
   the same scope.
4. *(NR).* The review's "a weaker sufficient condition for it" is made "for that conclusion", the P-indivisibility
   conclusion, as Main §2.3 and D245 state it; (NR) is not a sufficient condition for an exact return.
5. *The return formulation (owner requirement).* The distinction is stated in D026: the step from an exact return
   holds for a hidden prior on a measurable carrier of any cardinality, Main's Corollary (near-return) (its hypothesis
   (NR) holds with margin $m>0$ when $\Gamma_n=I$), and what is open is a source of the return hypothesis (X-21).
6. *Nit 5.* For Lemma 1c and Proposition 4b, "the selected counting measure" is Lemma 3's, the counting law of a finite
   representative, so "on a finite representative" is the scope; Theorem 19's proof divides by $|\mathcal{C}_H|$, so
   its scope is "a finite $\mathcal{C}_H$".
7. *Methodology:353.* Only the finite scope is added. Its "which preserves every channel" states no prior; the
   uniform-prior wording is the scope of #1492, which is not landing, and is not changed here (§31.9).

### 31.4 Scope audit: every summary of Theorem 24(i) at H

A `git grep` at H over `papers/*.md` and `book/*.md` for "relabel", "hidden permutation" and "permutation of the hidden"
gives the sites below that concern hidden relabelling (the others concern alphabet relabelling, spectra, hypercharges,
carriers of operational theories or the Born rule).

| Site | Kind | Disposition |
|---|---|---|
| Sub:253 | the theorem statement | D361 (§28) |
| ch02:140 = FULL:770 | the book statement | #1494, on `main` |
| Str:154; ch02:134 = FULL:764; ch02:172 = FULL:802; ch03:80 = FULL:941; ch03:136 = FULL:997; ch03:142 = FULL:1003; ch04:172 = FULL:1276; Complexity:206; Methodology:353 | summaries stating the invariance | D369, D375–D388 |
| Methodology:467 | "give examples at the stated scope of [Substratum Theorem 24]" | no change: the scope is the theorem's |
| Main:60 (D231's sentence); Main:736 (item (ii), D224) | transfer from a finite representative | the relabelled object is a relabelling of a finite representative; D231 revised for nit 6 |
| Str:742, Str:792 | Proposition 9.5 | no change: Proposition 9.5 is stated for finite OI-class substrata (its A1-A6 clause is rewritten by the plan, `STRUCTURE:P-9.5`) |
| Sub:139, Sub:191, Sub:201, Sub:395; Str:51, Str:64, Str:206, Str:679; Computation:254; ch14:234 | generator lists | no change: they name generator (i) and state no invariance (as #1494 N3 records for Str:51, Str:206, Computation:254, ch14:234) |
| Methodology:463; ch09:258 | the members of $\mathcal G_{\text{sub}}$ described as indistinguishable | no change: they describe the members of the group, whose scope is the theorem's |
| ch02:148 = FULL:778 | proof of the scoped statement | no change |

### 31.5 Not changed

A1 stays retired, no optional A1 hypothesis is introduced, and the frozen H-B sentence stays. D001–D373 keep their text
apart from the five revised records. D022, D116/D117 and D370–D373 are unchanged (the review accepts them). F6 is not
incorporated.

### 31.6 Checker changes

- `preserve_check.py`: the record pins are read from the last `Record pins` subsection of PREREG (§31.11), so §26.4
  stays as written; `--reconcile REV` compares the ledger at REV with the current ledger and base (§31.2); a scope
  assertion check `SCOPE`, run in every candidate mode, requires each corrected sentence of §31.3 (and #1494's statement,
  F5) in the candidate, with self-test mutants that drop one; the stale coverage entries gain `SM:L-1c-…`, `SM:P-4b-…`
  and `SM:T-19` (D389–D391 change their statements).
- `guards_check.py`: the same three entries in `--predict`'s stale list.
- `edits_check.py`: `PRESERVE` entries for D026, D231, D363, D364, D369 and D374–D391, and `SIM_PRESERVE` entries for the
  corrected sentences, so a redraft that drops a scope fails `--static` and `--simulate`.

### 31.7 Preregistered checks and decision rule

The amendment passes only if all of the following hold at H, each from the checkers at the plan head that carries
§31.10:

1. `edits_check.py`: `--self-test` PASS; `--static` 0 findings in every scan (infinity, register, capitals,
   identifiers, preservation including every §31.6 entry, mirror parity, Lean docstring-only) and sitemap 194/194;
   `--commit H --simulate` 391/391 unique, residual 5 (all allowed), 0 unscoped, 0 preservation, 0 identifier;
   `--pins --commit H` 0 unresolved and 0 missing; `--repo-scan --simulate --final --commit H` 0 unexplained.
2. `preserve_check.py --reconcile 55544cc36dee5b7dd5b9079c0f03be24b74c137f`: all 371 P* splices are compared with the
   re-cut ledger at H. 366 keep their old and new bytes, of which exactly 60 are shifted, all by +121 bytes and all in
   ch02 or FULL after the #1494 paragraph, and 306 keep their span; D026, D231, D363 and D364 keep their old bytes and
   span and carry the revised replacement; D369 carries the extended old text and the revised replacement; 0 drift; the
   18 records D374–D391 are new.
3. `preserve_check.py --verify-ledger` identical; `--verify-pins` PASS against §31.11; `--self-test` PASS with the new
   scope mutants.
4. `guards_check.py --mutants` PASS (as §28.4 item 3).
5. `guards_check.py --predict`, then `preserve_check.py --tree <predicted> --mutants`: PASS, 0 findings, the scope
   assertions all present, the tree mutants failing as required. On H itself (the unedited base) the scope check fails,
   one finding per assertion that the plan adds.
6. Scope assertions, preregistered: in the predicted tree each of the following is present, and the superseded form at
   each F4 site is absent: Sub:216 "no established form for a substratum of unspecified cardinality", "Corollary
   (near-return) of [Main §2.3], of which an exact return is a case", "what is open for a substratum of unspecified
   cardinality is a source of the return hypothesis", "a meromorphic continuation of the memory-resummed Schur
   complement that is not established", "These do not by themselves extend the complete reconstruction theorem";
   Sub:262 "for any density matrix $\sigma_A$ with $\operatorname{Tr}\sigma_A=1$ on a Hilbert space" and "for a
   classical factor with $\alpha(A)=1$"; Sub:257 "a density matrix $\sigma_A$ on $\ell^2(A)$"; Sub:94 "for $S$ of
   unspecified cardinality bijectivity is the reversibility posit (REV)" and "thus, for a finite $S$, partly
   structural"; Str:154 and the book summaries "of a finite $\mathcal{C}_H$" at each of the twelve book sites and
   Str:154; Complexity:206 and Methodology:353 "of a finite set of hidden"; SM:252 and SM:334 "counting measure … on a
   finite representative"; SM:641 "the counting measure on a finite $\mathcal{C}_H$"; Main:60 "every representative,
   or channel-preserving extension,"; ch02:140 and FULL:770 "For a finite set of hidden configurations $\mathcal{C}_H$
   with the uniform hidden prior". The same strings are `preserve_check.py`'s `SCOPE` list, which T0′ and T1′ run.
7. The coverage entries changed by the plan are exactly the seven of §31.6; `tools/coverage_check.py` passes on the
   predicted tree.
8. The new and revised records remove no finiteness term: compared with the base, the only removal of "finite" among
   them is D369's, recorded in §28.3.
9. Every run writes its structured result file, and each parses.

A failure of any item stops the amendment; it is not re-run with changed thresholds.

### 31.8 The trial T0′/T1′

Built only after the independent delta review of this amendment and with the owner's approval of the trial dispatches
(§A.43 item 4):

- **P\*\*** is the head of `research/a1exit-deletion-20261121` at the moment T0′ is built; it is recorded with T0′, and
  the plan branch does not move between building T0′ and the last T1′ dispatch. If it moves, T0′ and T1′ are rebuilt
  from the new head, and the dispatches are repeated (§30).
- **T0′**: a single-parent child of H whose tree is `guards_check.py --predict` at P\*\* (H's PDFs).
  `a1exit-trial-verify.yml` is dispatched from `main` with `trial_sha` T0′ and `plan_sha` P\*\*. Expectation, as §29
  item 1: every step up to `preserve` passes; `preserve` fails with only `--pdf-compare` findings for the PDFs of the
  ledgered sources; `guards` is skipped; `result.json` and the PDF upload are written. The scope assertions of §31.7
  item 6 pass in `preserve`'s `--commit` and `--tree` runs (each is a recorded check in the structured result).
- **T1′**: a single-parent child of H whose tree is T0′'s with the PDFs of the ledgered sources replaced by T0′'s
  CI-built PDFs. `a1exit-trial-verify.yml` (from `main`, `plan_sha` P\*\*) and `verify.yml` (on a branch whose head is
  exactly T1′) are dispatched; every step and job must pass.
- **Complexity.** D387 makes `papers/Complexity.md` a ledgered source, so its TeX is rebuilt and its PDF is one of the
  PDFs `--pdf-compare` checks. The workflow on `main` builds and uploads the PDFs of seven papers and the book, not
  Complexity's, so T0′ would carry a ninth, non-mismatch finding and T1′ could not pass. Before T0′ is built, the owner
  decides between (a) adding `Complexity` to that workflow's `build.sh` list, page-count loop and upload list, a
  separate reviewed change to `main`, after which the expectation above reads nine PDFs; and (b) removing D387 from this
  plan by a further amendment and carrying Complexity:206 as a separate correction. Until that decision T0′ is not built.
- **FULL.pdf (#1539).** H distributes a `FULL.pdf` that still prints the statement #1494 corrected. T1′'s CI-built
  `FULL.pdf`, built by `build.sh --book` on the pinned toolchain from the predicted tree, is the route for the
  corrected PDF; the retirement is not complete until that PDF is verified (its `pdf-compare` check and page count in
  T1′'s structured result, and an independent check that it prints the corrected statement).
- P\*'s T0/T1 results are not evidence for T0′/T1′.

### 31.9 Recorded for the owner

1. The Complexity PDF route of §31.8, (a) or (b).
2. Methodology:353's "which preserves every channel" names no hidden prior (a uniform-prior wording is in #1492's scope,
   which is not landing). It is not an A1 consequence and is left to that stream.
3. Nit 5 makes three more coverage entries stale (SM Lemma 1c, Proposition 4b, Theorem 19), re-affirmed as the other
   four are (§11 item 4).

### 31.10 Results at `53c6601a`

Each check of §31.7 was run from the checkers at `9ba8ef10` (the commit that applies §31 and carries the §31.11 pins),
with `--plan 9ba8ef10` for `preserve_check.py`. Every run wrote its structured result file, and each parses with verdict
`pass`.

| §31.7 item | Result |
|---|---|
| 1 | `edits_check.py`: `--self-test` PASS (93 countercontrols); `--static` infinity 0, register 0, capitals 0, identifier 0, preservation 0 (every §31.6 entry included), mirror parity 0, Lean docstring-only 0, sitemap 194/194; `--commit 53c6601a --simulate` 391/391 unique, residual 5 (all allowed), 0 unscoped, 0 preservation, 0 identifier; `--pins --commit 53c6601a` 0 unresolved, 0 missing; `--repo-scan --simulate --final --commit 53c6601a` 0 unexplained |
| 2 | `preserve_check.py --reconcile 55544cc3…`: 371 P* splices; 306 unchanged, 60 shifted by the base change (each +121, in ch02 or FULL, after the #1494 paragraph), 5 revised at §31; 18 added (D374–D391); drift 0 |
| 3 | `--verify-ledger` identical; `--verify-pins` PASS (§31.11); `--self-test` PASS, 46 recorded checks, among them the scope controls (the predicted candidate carries every corrected sentence; the unedited base fails all 44 assertions the plan adds; a candidate without D391, or with a superseded form in FULL, fails) and the reconcile controls (a ledger against itself: no drift; a changed replacement: drift; splices after a base insertion, shifted by its length: explained; a span moved otherwise: drift) |
| 4 | `guards_check.py --mutants` PASS: the 14 checks on the simulated tree of 53c6601a (41 files edited by 391 records), CC-1–CC-4 failing as named, inventory 0 unlisted, P01–P30, the kernel identifiers and the message names each failing under mutation; 64 recorded checks |
| 5 | `guards_check.py --predict` (9 TeX rebuilt, 7 fingerprints re-affirmed, SC-42 result regenerated, `verify.yml`'s four SC-42 comparisons PASS), then `preserve_check.py --tree <predicted> --plan 9ba8ef10 --mutants`: 0 findings; scope assertions 31 present and 15 absent, 0 findings; the 5 tree mutants fail as required |
| 6 | as item 5: every assertion holds on the predicted tree, and the self-test shows the base fails every one the plan adds |
| 7 | the census fingerprints that differ between 53c6601a and the predicted tree are exactly `MAIN:L-3`, `SM:L-1c-canonical-projection-resummed-kernel`, `SM:P-4b-symmetric-point-custodial-scalarity-component`, `SM:T-19`, `STRUCTURE:P-9.5`, `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer`, `SUBSTRATUM:T-23`; `tools/coverage_check.py` on the predicted tree: OK |
| 8 | no new or revised record has fewer occurrences of "finit" in its replacement than in its old text; D369 still removes "finite decoupled" (§28.3) and adds "of a finite $\mathcal{C}_H$" |
| 9 | the nine result files (`edits_check.py` writes none) parse, verdict `pass` |

**Found while applying §31.**

1. *Identifier rule.* The rule against printing the retired ledger identifier "(ii)" rejects "Lemma 1c(ii)" in a
   replacement. D026 names it "the observer-operator pole statement of Lemma 1c [SM §4.1] and the continued response
   of Proposition 4b [SM §4.4]"; the content is that of §31.3.
2. *Criterion-5 scan.* D389 changes the line of SM's Lemma 1c, whose part (ii) opens "On a finite configuration space";
   that unchanged sentence states its own finite scope, and is listed in `CRIT5_ALLOW`.
3. *Drift outside the splices, flagged.* The repository scan at H finds two lines that are not at `97070c98`: the
   name and header comment of `.github/workflows/a1exit-trial-verify.yml` (#1484, merged at `df6da1c6` after the
   ledger base, not #1494). They carry the programme name A1-EXIT and "A1-retirement", which name the retirement and
   state no premise; they are classed "unrelated label" with that reason. No splice and no ledgered file is affected.
4. *Site map, step 4.* `ledger_check.py build` on scratch exports of `97070c98` and of H gives the same site set apart
   from two new sites at H, ch02:140 and FULL:770, #1494's statement, which matches the finite-scope pattern P6 and is
   not a pointer site; the ptr count is 193 in both rebuilds. The frozen map at its pin `e837e3db` has 194 ptr sites,
   and the plan's sitemap cross-check (base lines mapped back to that pin) is 194/194 at H as at `97070c98`. The
   difference of one between a rebuild and the frozen map predates the base and is not caused by #1494; it is
   reported for the delta review and changes no edit.
5. *Cost.* The tree check of item 5 took about 13 minutes here, the mutant run about 6; the T0′/T1′ runs are CI's.

Not run here: T0′/T1′ (§31.8), which wait for the delta review, the owner's Complexity decision and the dispatch approval.

### 31.11 Record pins

The digests below pin the record files from amendment §31 on; `preserve_check.py` reads the last `Record pins`
subsection of this record, so §26.4 stays as P*'s pins. The ledger has 389 splices in 41 files at `53c6601a` (391 edit
records; D032 and D039 retain their text).

| File | SHA-256 |
|---|---|
| `edits.json` | `1d5e31f7a0e80f03b2689c3bdd56892be7c1bafc325831bf5623a1c3be0af813` |
| `ledger.json` | `244da1c319f7b0932f78f907e5033b02351e02e1f0dba744be8f3a4636cba66e` |
| `edits_check.py` | `3ab6ba2ac6c0dbefee37f8589593aa259fc997980c34bd33f892015fea446e3b` |
| `guards_check.py` | `ef89e1c79a0cc3c34af1ebb981e1674edd33a534d6f98612ee06ce57005b5cee` |
| `preserve_check.py` | `08400a60ca70220344f4bb4b633a56c3b4c3fd3ce121efab2d56a07c44f91b3a` |

### 31.12 Amendment, preregistered: the delta review's R1–R3

The independent delta review of §31 at `607f7a61` is recorded on #1477 (comment 7075534457), REVISE with three findings
R1–R3; it reproduces the reconciliation of §31.2 (306 unchanged, 60 shifted, 5 revised, 18 added, drift 0) and accepts
the seven deviations of §31.3. The owner's decisions on it, owner `amaybaum`, 2026-11-22T06:50:57Z,
[#1169 comment 7075564570](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7075564570), quoted in
part:

> | Finding | Decision |
> |---|---|
> | R1, PDF checker false pass | Required fix. Each of the nine ledgered PDFs must be rebuilt in CI before its comparison can count as passing. The checker fails closed if a build is missing, fails or compares stale output. A new mutant must show that this failure is actually detected. |
> | R2, finite alphabet | Required fix. Keep the finite-alphabet condition, including `[NeZero q]`, wherever the revised claims depend on it. |
> | R3, Lean docstrings | Required fix. Scope all four ensemble claims explicitly to the finite cases actually supported. |
> | N3, nine PDFs | Apply. |
> | Optional R-1 | Accept only if it is demonstrably editorial and does not broaden any scientific claim. |
>
> The 306 unchanged, 60 shifted, 5 revised and 18 added splices must stay traceable after re-pinning. Any additional change needs an explicit explanation. Once corrected, §31 returns for another independent delta review before the freeze.

The Complexity route (a) of §31.8 was provisionally approved at #1169 comment 7075394811 (`amaybaum`,
2026-11-22T06:33:27Z) and is the workflow change #1543, confirmed with nits at #1543 comment 7075542860; c.7075564570
item 2 approves its merge under conditions.

**Goal link (§A.47).** A1-EXIT (#1169): this subsection decides whether the trial's PDF comparison can fail for every
ledgered PDF, and whether the plan's Lean-docstring, registry and README texts keep the finite instances the kernel
results take; it does not decide execution.

**Order.** This subsection is committed first; the edit-list, checker, ledger and pin changes follow; the results are
§31.13 and the record pins §31.14, which `preserve_check.py` reads as the last `Record pins` subsection. §31.1–§31.11
are not edited; where §31.8 differs from this subsection, this subsection governs.

#### 31.12.1 R1: the PDF comparison fails closed

*What §31.8 got wrong.* §31.8 says that with Complexity unbuilt "T0′ would carry a ninth, non-mismatch finding and T1′
could not pass". In fact the workflow's build directory is a worktree of the trial commit, so for a ledgered source the
workflow does not rebuild, the built directory holds the trial's own committed PDF, and `--pdf-compare` compares that
PDF with a copy of itself: it passes. T0′ would show no Complexity finding, and T1′ would pass with H's stale
`papers/Complexity.pdf`. The comparison was vacuous for any ledgered source missing from the workflow's list.

*The fix, in `preserve_check.py`'s `--pdf-compare BUILT`.* A comparison of a ledgered PDF counts as passing only when
that PDF was rebuilt by the run's CI build. The run's output directory is `BUILT/../out` (the workflow's
`$RUNNER_TEMP/out`), or `--pdf-out DIR`. For every PDF of a ledgered source the check fails, naming the PDF, when:

| Failure mode | Test | Self-test mutant |
|---|---|---|
| F-a: the build did not succeed | `build.rc` absent from the output directory, or not `0` | MT-pdf-build-failed (`build.rc` = `1`); MT-pdf-build-rc-missing |
| F-b: no build record | `pdf-pages.tsv` absent | MT-pdf-pages-missing |
| F-c: missing build | the PDF is not a row of `pdf-pages.tsv`, or absent from BUILT | MT-pdf-not-built (a ledgered PDF absent from the rows: the Complexity case) |
| F-d: the record does not describe the built file | the row's page count differs from `pdfinfo` of the built PDF | MT-pdf-pages-mismatch |
| F-e: stale output | the built PDF is byte-identical to the candidate's committed PDF (xelatex embeds a creation date and document id, so a rebuild differs in bytes; a reproducible build would make this fail, in the safe direction) | MT-pdf-stale (built = committed copy) |
| (kept) content | page count and `pdftotext` text of committed and built differ | the existing two controls |

Each mutant must fail with its named finding, and a control with every condition met must pass.

*What makes Complexity's comparison real.* #1543 adds `Complexity` to the workflow's `build.sh` list, TeX-equality
list, page-count loop and upload list. With it merged before T0′ is cut, Complexity's PDF is rebuilt and listed; the
checker change above makes any future omission fail instead of passing. #1543 changes the workflow on `main` only. The
ledger base stays H: T0′ and T1′ are children of H and carry H's copy of the workflow file, which is not a ledgered file
and is compared with H unchanged; the workflow that runs is read from `main` at dispatch. No pin or check of the plan
reads `main`'s workflow file (the repository scan's entry for it has no substring).

*N3 (#1543 c.7075542860): §31.8's T0′ expectation reads nine PDFs.* T0′: every step up to `preserve` passes;
`preserve` fails with only `--pdf-compare` text findings for the nine PDFs of the ledgered sources (H's committed PDFs
against their rebuilds from the corrected sources); `guards` is skipped; `result.json` and the upload of nine PDFs are
written. T1′: the nine PDFs replaced by T0′'s CI-built ones; every step and job of both workflows passes. A missing glyph
or a failed build fails the trial; it is not a reason to weaken a check (c.7075564570 item 2).

#### 31.12.2 R2: the finite alphabet

`waveSubstratum_A1 [NeZero L] [NeZero q]` (`SubstratumInterfaceAudit.lean:185`): the configuration space is
`(Fin d → ZMod L) → ZMod q`, and `ZMod 0 = ℤ`, so the finiteness predicate needs a finite torus and a finite alphabet.

| Record | Site | Old → new (replacement) | Why |
|---|---|---|---|
| D276 (revised) | `SubstratumInterfaceAudit.lean:7` | "the finiteness predicate `A1` on a finite torus" → "… `A1` for a finite torus and a finite alphabet" | R2 |
| D332 (revised) | census registry :525 | "the finiteness predicate `A1` and A2-A5 (Q1)" → "… `A1` (for a finite torus and a finite alphabet) and A2-A5 (Q1)" | R2 |
| D326 (revised) | `verification/README.md:1007` | "the finiteness predicate `A1` and A2–A5" → "… `A1` for a finite alphabet and A2–A5" | additional: the README sentence restates the same theorem and already says "on a finite cubic torus"; the same omission, propagated (§A.25) |

#### 31.12.3 R3: the ensemble and observer-theory headings

Each result is proved in a section whose variables carry `[Fintype 𝒮.ι] [Fintype 𝒮.V]`; `obsTheory` and
`EnsembleDetermined` are defined only there. On an infinite carrier whose non-zero orbits are all infinite, δ₀ is the
unique invariant law, so "fails for every substratum" is false outside the finite case. The headings take the instances'
scope (docstring only, no kernel change; class `lean-docstring`, checked docstring-only).

| Record | Site | Old → new | Why |
|---|---|---|---|
| D392 | `StochasticInterface.lean:113` | "FAILS FOR EVERY SUBSTRATUM WITH A LINEAR RULE AND MORE THAN ONE CONFIGURATION" → "… WITH FINITELY MANY SITES, A FINITE ALPHABET, A LINEAR RULE AND MORE THAN ONE CONFIGURATION" | R3 |
| D393 | `StochasticInterface.lean:173` | "For every substratum whose rule is linear" → "For every substratum with finitely many sites and a finite alphabet whose rule is linear" | R3 |
| D394 | `LiftSource.lean:36` | "the observer theory of every substratum has its swap layer" → "… of every substratum with finitely many sites and a finite alphabet has …" | R3 |
| D395 | `ExecSource.lean:14` | "the observer theory of every substratum executes no layer flow" → "… with finitely many sites and a finite alphabet executes …" | R3 |
| D396 | `verification/README.md:1261` | the same phrase for `obs_not_layerFlowExecutable` | additional: README restatement of D395's result (§A.25) |
| D397 | `verification/README.md:1311` | the same phrase for `obs_swap_avail_one_not_layerFlowExecutable` | additional: README restatement of D394's result |
| D398 | `verification/README.md:1639` | "every substratum (`permTheory_nonnegBounded`, `obsTheory_nonnegBounded`)" → "every substratum with finitely many sites and a finite alphabet (…)" | additional: README restatement of `FrozenSourcing.lean:82`, which D282 already scopes |

`FrozenSourcing.lean:82` needs no new record (D282). The R7 guard's R7-EXEC message (`edge_rigidity_probe.py:4709`)
describes, in a check message, the results the guard verifies ("the observer theory of every substratum executing no
layer flow"); it is not edited: it names no A1 premise, and the results it pins carry the finite instances in their
statements. New IDs D392–D398 continue from D391; none is reused.

#### 31.12.4 R-1 (optional): not applied

`SubstratumInterfaceAudit.lean:175` says `waveSubstratum` is "the manuscripts' rule on a finite cubic torus with alphabet
`ℤ/qℤ`"; the definition holds for every `L`, `L = 0` giving `ℤᵈ`. The change would add a statement about the `L = 0`
case, which `waveSubstratum_A1` excludes and the manuscripts do not use for this rule; it is not a consequence of
retiring A1 (the docstring understates, it does not generalize). It is not demonstrably editorial, so under
c.7075564570 it is left unchanged.

#### 31.12.5 Traceability after the re-pin

The `--reconcile` classification treats a record of the revised set as unchanged when its old and new bytes and span
are unchanged. The revised set becomes D026, D231, D276, D326, D332, D363, D364, D369 and the added set D374–D398.
Expected:

- against P\* (`55544cc3`): 303 unchanged, 60 shifted (as §31.2, every row unchanged), 8 revised (§31.3's five and
  R2's three), 25 added (D374–D398), drift 0; the 306 of §31.2 are the 303 plus D276, D326 and D332;
- against §31's first re-cut (`9ba8ef10`, 389 splices): 386 unchanged, 3 revised (D276, D326, D332), 7 added
  (D392–D398), drift 0.

Records: 398 (ptr 242, consistency 54, handoff 5, lean-docstring 40, repo-active 38, guard-pin 19); splices 396 in 44
files (`StochasticInterface.lean`, `LiftSource.lean` and `ExecSource.lean` newly ledgered).

#### 31.12.6 Preregistered checks and decision rule

Every item of §31.7 is re-run at H from the plan head that carries §31.13, with these changes: item 1 counts 398
records; item 2 is the two reconciliations of §31.12.5; item 3's self-test includes the R1 mutants of §31.12.1, each
failing with its named finding, and its positive control; item 6's scope assertions add R2's three phrases and R3's
seven, and the superseded forms of R3's four headings; item 7 expects the same seven coverage entries (no manuscript
statement changes). `guards_check.py --mutants` runs with `scipy` installed (F71 needs it). A failure of any item stops
the amendment; it is not re-run with changed thresholds.

#### 31.12.7 Two bases, and the validity of each trial run

The owner's requirement for T0′ (relayed for this correction round): the trial uses the workflow merged by #1543 at
`main` `413b0bb88f39cad901befcf4684355c7ee39480b`, or a later `main` that contains it unchanged, and the scientific ledger
stays pinned to H. The two bases are distinct and neither stands in for the other anywhere in §31:

| Base | Commit | Role |
|---|---|---|
| **Ledger base** | H = `53c6601a10419b6b333cc992474272501ab542af` | decides *what* is checked: the ledger's spans and base hashes, the predicted tree, and the parent of T0′ and T1′, each a single-parent child of H |
| **Workflow base** | W = `413b0bb88f39cad901befcf4684355c7ee39480b` | decides *how* the trial is checked: the `a1exit-trial-verify.yml` that is dispatched, with its nine-PDF build, TeX-equality, page-count and upload lists |

H's own copy of the workflow (eight PDFs) is a file of the trial trees, compared with H unchanged like any other file
that the ledger does not touch; it is never the workflow that runs. W changes only that workflow file relative to H
(`git diff 53c6601a 413b0bb8`: one file), so it changes no ledgered file, no base hash and no pin.

**Preregistered check of every dispatch (T0′, and both dispatches of T1′).** A run counts only if both parts hold; a run
that fails either is **void**, neither a pass nor a fail of the plan, and is repeated by a fresh dispatch:

1. *Workflow base.* The run's `result.json` fields `workflow_sha` and `ref_sha` each name a commit on `main`'s
   first-parent history that has W as an ancestor (W itself included), and at that commit the blob of
   `.github/workflows/a1exit-trial-verify.yml` equals its blob at W. For the `verify.yml` dispatch on T1′, which writes no
   `result.json`, the run record's head is exactly T1′ (§29 item 2) and part 1 does not apply.
2. *Ledger base.* The run's `trial_sha` has exactly one parent, H.

The check is `preserve_check.py --verify-run RESULT.json --workflow-base W --main REV` (`REV` the current `main`), which
reads only the structured `result.json` and the object store (§A.44), prints `RUN VALID` or `RUN VOID` with each
failing part, and writes its structured result; its self-test includes a void mutant for each part (a `workflow_sha`
without W as an ancestor, a workflow blob that differs from W's, a `ref_sha` off `main`, a `trial_sha` whose parent is
not H, and a merge `trial_sha`). The workflow's own head step already enforces part 2 against the ledger base read from
P\*\*, and this check repeats it from the record.

### 31.14 Record pins

The digests below pin the record files from §31.12 on; `preserve_check.py` reads the last `Record pins` subsection,
so §26.4 and §31.11 stay as the pins of P* and of `9ba8ef10`. The ledger has 396 splices in 44 files at `53c6601a`
(398 edit records; D032 and D039 retain their text).

| File | SHA-256 |
|---|---|
| `edits.json` | `7ce472d10eb4eae86bedec00d8cbc497d9b4682aa1ccde94f3331f218d4552ac` |
| `ledger.json` | `a6422a733ae9c31e107aed92e04e3becd2e80c30d0e71980b6083a9ab9411661` |
| `edits_check.py` | `5c0be6f81ea3292591b4037ff08dddb6f8d639c78df40521c818a6da1263bc35` |
| `guards_check.py` | `ef89e1c79a0cc3c34af1ebb981e1674edd33a534d6f98612ee06ce57005b5cee` |
| `preserve_check.py` | `fcfa3728193423281a2bf4ee0343e09184d2cfaec7de80618bbb50bdf641f056` |

#### 31.12.8 The executed workflow commit, from the host's run record

Owner decision, owner `amaybaum`, 2026-11-22T07:21:50Z,
[#1169 comment 7075869738](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7075869738), quoted in
part:

> **New safeguard, `workflow_sha`.** `workflow_sha` must identify the commit whose workflow definition actually executed, not just a commit referenced in `result.json`. The checker verifies it against the CI run's trusted metadata from the host's API (the run's workflow ref and head commit), not against a self-reported value. A self-reported SHA alone must not produce a pass.

§31.12.7's check is extended. `--verify-run RESULT.json --run-meta RUN.json`, where `RUN.json` is the host's record of
the run (`GET /repos/amaybaum/incompleteness/actions/runs/{run_id}`, saved whole beside the result), and the run counts
only if, besides §31.12.7's parts:

3. *The run record.* `RUN.json` is present and parses; its `id` equals `result.json`'s `run_id`; its `event` is
   `workflow_dispatch`; its `path` is `.github/workflows/a1exit-trial-verify.yml`; its `head_branch` is `main`; its
   `run_attempt` is 1.
4. *The executed commit.* The commit whose workflow definition executed is the run record's `head_sha`. Part 1 of
   §31.12.7 (on `main`'s first-parent history, containing W, the workflow blob equal to W's) is applied to that
   `head_sha`, and `result.json`'s self-reported `workflow_sha` and `ref_sha` must each equal it; a self-reported value
   that differs from the host's is void, and so is a run without a host record.

Self-test mutants, each void with its named finding: the run metadata missing; a `workflow_sha` in `result.json` that
differs from the run's `head_sha`; a run whose `head_sha` carries a workflow blob other than W's; a run record of another
event, another workflow path, another run id, or a re-run attempt. A valid control passes.

### 31.16 Record pins

The digests below pin the record files from §31.12.8 on (`preserve_check.py` gains the host-run-record check);
`preserve_check.py` reads the last `Record pins` subsection, so §26.4, §31.11 and §31.14 stay as the pins of P*,
`9ba8ef10` and `785b17f9`. The ledger is unchanged from §31.14: 396 splices in 44 files at `53c6601a` (398 edit
records; D032 and D039 retain their text).

| File | SHA-256 |
|---|---|
| `edits.json` | `7ce472d10eb4eae86bedec00d8cbc497d9b4682aa1ccde94f3331f218d4552ac` |
| `ledger.json` | `a6422a733ae9c31e107aed92e04e3becd2e80c30d0e71980b6083a9ab9411661` |
| `edits_check.py` | `5c0be6f81ea3292591b4037ff08dddb6f8d639c78df40521c818a6da1263bc35` |
| `guards_check.py` | `ef89e1c79a0cc3c34af1ebb981e1674edd33a534d6f98612ee06ce57005b5cee` |
| `preserve_check.py` | `6999cd3cf7e28298f050b692fc29f6733f055edef8ebcad8553a11c96914a861` |

#### 31.12.9 R-7 and R-8 of the Lean audit

Owner decision, owner `amaybaum`, 2026-11-22T07:25:13Z,
[#1169 comment 7075903147](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7075903147), quoted in
part:

> | R-7, `A6Instantiation.lean:508` | Required. Replace the global-finiteness assertion with a correctly scoped statement about finite representatives, and correct the stale `SM.md:306` citation. |
> | R-8, D319 capitalization | Approved. Capitalize "The finiteness predicate A1 is not weakened" at the sentence boundary. |
>
> - R-7 is scientifically significant: the existing statement describes the substratum itself as finite, which contradicts the intended A1 retirement.
> - The writer must preserve the valid finite-case results and independently verify the replacement citation.
> - Both changes go into the amended ledger with their own traceability entries and required-present/required-absent checks.

The source is the Lean A1-dependency audit (#1542 at `f9e91692`, its AUDIT.md §6, rows R-7 and R-8).

**R-7, the passage.** The docstring of `cx3b_complex_not_A1` (`A6Instantiation.lean`, "Bounded reading, frozen")
reads, at H: "That is **not a defect of the interface and not a defect of the manuscripts**: the manuscripts' substratum
is the finite object of `SM.md:306` and the complex carrier is the object on which the derivation of `SM.md:114` and
Theorem 5 is conducted. **`A1` is not weakened**, …".

*The citation, checked against the source.* `SM.md:306` at H, and at the module's own commit `082c3eaa`, is the Remark on
the scope of the center-dependence–mass identification of Theorem 3, which states no finiteness. The round's frozen
record (`verification/programmes/substratum/a6-instantiation/result.md`, start-state table) used `SM.md:306` for the
K-component multi-component update; at H that passage is SM:312 in §4.4, and it states the update on the observer-level
branch, "not the $\mathbb{Z}/q\mathbb{Z}$ alphabet of the substratum". The finite object the sentence contrasts with the
complex carrier is stated in two places at H:
- SM §4.1, SM:222: "under A1 and A4 [Substratum §3.1] it acts on configurations over a finite periodic quotient
  $\Lambda/P$". After the retirement (D036) it reads "under A4 [Substratum §3.1] it acts on configurations over
  $\Lambda$ or, as a qualified case, over a finite periodic quotient".
- SM §4.4, SM:312: the substratum's alphabet $\mathbb{Z}/q\mathbb{Z}$.

So the replacement cites sections, which do not go stale with line moves: `SM.md` §4.1 and §4.4.

*The edit (D399, `lean-docstring`, semantic).* "the manuscripts' substratum is the finite object of `SM.md:306`" →
"the manuscripts' finite representatives, configurations over a finite periodic quotient of the lattice (a qualified
case) with the substratum's alphabet `ℤ/qℤ` (`SM.md` §4.1, §4.4), are finite objects". This states only finiteness of the
finite representatives, not of the substratum. The finite-case result is unchanged: the kernel statement
`cx3b_complex_not_A1`, that the complex carrier does not satisfy the finiteness predicate, and the passage's distinction,
that the covariance statement comes inside the interface and the complex carrier does not.

*Consistency with D317–D320.* D399's old text ends before " and the complex\ncarrier", and D319's old text,
"**`A1` is\nnot weakened**", begins two sentences later, so the two splices are disjoint. The ledger's overlap check
(`validate_ledger`) confirms this. The sentence after D399 still reads "and the complex carrier is the object on which
…".

*Further stale citations found, not edited.* The same docstring's next theorem cites "`SM.md:306`–`:308`" for the
dynamics (`A6Instantiation.lean:539`), and `SM.md:114` here may also have moved. Neither states or implies finiteness, so
they are not consequences of the retirement. They are recorded for the Lean audit (#1542) and left unchanged, to keep the
change minimal.

**R-8 (D319 revised).** "**the finiteness predicate `A1` is\nnot weakened**" → "**The finiteness predicate `A1` is\nnot
weakened**". It opens a sentence after "… Theorem 5 is conducted.".

**Checks.** `SCOPE_PRESENT` gains D399's replacement and D319's capitalized form. `SCOPE_ABSENT` gains "the manuscripts'
substratum is the finite object of" and D319's lower-case form. `PRESERVE` gains both. `REVISED31` gains D319 and
`NEW31` gains D399. The expectations of §31.12.5 become: against P\*, 302 unchanged, 60 shifted, 9 revised, 26 added,
drift 0; against `9ba8ef10`, 385 unchanged, 4 revised, 8 added (D392–D399), drift 0. Records: 399 (lean-docstring 41);
splices 397 in 44 files.

### 31.17 Results of §31.12 at `53c6601a`

Each check was run at H from the checkers at `0702dacc` (the commit that applies §31.12.9 and carries the §31.18 pins),
with `--plan 0702dacc` for `preserve_check.py`, and `scipy` 1.18.1 installed for F71. Every run exited 0, and every result
file parses with verdict `pass`. §31.10 is not edited.

| Check | Result |
|---|---|
| `edits_check.py --self-test` | PASS (93 countercontrols) |
| `edits_check.py --static` | infinity 0, register 0, capitals 0, identifier 0, preservation 0 (every §31.6, §31.12 and §31.12.9 entry), mirror parity 0, Lean docstring-only 0, sitemap 194/194 |
| `edits_check.py --commit 53c6601a --simulate` | 399/399 unique, residual 5 (all allowed), 0 unscoped, 0 preservation, 0 identifier |
| `edits_check.py --pins --commit 53c6601a` | 0 unresolved, 0 missing |
| `edits_check.py --repo-scan --simulate --final --commit 53c6601a` | 0 unexplained |
| `preserve_check.py --verify-ledger` / `--verify-pins` | identical / PASS (§31.18) |
| `preserve_check.py --self-test` | PASS, 67 recorded checks: every R1 mutant (MT-pdf-build-failed, -build-rc-missing, -pages-missing, -not-built, -pages-mismatch, -stale, -other-document, -absent) fails with its finding and the all-conditions control passes; every `--verify-run` void mutant (run metadata missing, self-reported `workflow_sha` or `ref_sha` differing from the run's `head_sha`, a `head_sha` without W or with another workflow blob or off `main`'s first-parent history, another event, workflow, run id, attempt or branch, a `trial_sha` whose parent is not H, a merge, a non-commit) is void with its finding and the valid control passes; the scope controls (the base fails all 64 assertions the plan adds); the reconcile controls |
| `--reconcile 55544cc3…` (P\*) | 302 unchanged, 60 shifted (+121, ch02/FULL, the same 60 IDs as §31.2), 9 revised (D026, D231, D363, D364, D369; D276, D326, D332; D319), 26 added (D374–D399), drift 0. §31.2's 306 unchanged are these 302 plus D276, D326, D332 and D319, each revised by a named finding; its 5 revised and 18 added are among the 9 and 26 |
| `--reconcile 9ba8ef10…` | 385 unchanged, 4 revised (D276, D326, D332, D319), 8 added (D392–D399), drift 0 |
| `guards_check.py --mutants` | PASS: the 14 checks on the simulated tree (44 files edited by 399 records), CC-1–CC-4 failing as named, inventory 0 unlisted, every pin, kernel-identifier and message-name mutant failing; 64 recorded checks |
| `guards_check.py --predict`, then `preserve_check.py --tree --mutants` | 0 findings; scope assertions 44 present and 24 absent, 0 findings; the 5 tree mutants fail as required |
| coverage | exactly the seven census fingerprints of §31.6 change; `tools/coverage_check.py` on the predicted tree: OK |

**Ledger.** 397 splices in 44 files at H (399 edit records; D032 and D039 retain their text), SHA-256
`877c930510e0d431d5fbd60d7871d2cf03711643059e08fa9b5c91dcec31656c`.

**Departures from the text of §31.12, with reasons.**
1. *D332's wording.* §31.12.2 gives "… `A1` (for a finite torus and a finite alphabet) and A2-A5 (Q1)". The identifier
   rule rejects that form, which leaves a bare `A1`, and so does its range rule. The record reads "an instance satisfying
   the finiteness predicate `A1` and A2-A5 (Q1; the finiteness predicate for a finite torus and a finite alphabet)". The
   condition is the same, and the scope assertion checks that string.
2. *The base countercontrol.* Two required-absent forms are earlier plan text and never occur at the base: D276's "`A1`
   on a finite torus and" and D319's lower-case form. The control therefore expects 64 failures at the base
   (44 − 2 + 24 − 2). It counts each required-absent form only where the base carries it.
3. *The R1 stale test* relies on xelatex embedding a creation date and a document id, so that a rebuild differs in
   bytes. A reproducible build would make it fail, which is the safe direction.
4. *The workflow-blob mutant.* No `main` commit containing W carries a different workflow blob, so the control uses H,
   which fails the containment test as well as the blob test. Each finding is checked by its own message.
5. *Not run here:* the PDF build (no xelatex in this container), so the local tree check reports 0 PDFs rebuilt. R1's
   fail-closed comparison runs only with a CI build directory. T0′/T1′ remain unbuilt and undispatched.

### 31.18 Record pins

The digests below pin the record files from §31.12.9 on (D399, D319 revised, and their checks);
`preserve_check.py` reads the last `Record pins` subsection, so §26.4, §31.11, §31.14 and §31.16 stay as the pins of P*,
`9ba8ef10`, `785b17f9` and `3fa2d18f`. The ledger has 397 splices in 44 files at `53c6601a` (399 edit
records; D032 and D039 retain their text).

| File | SHA-256 |
|---|---|
| `edits.json` | `fff453b7165769d313a35ed8f9c1598634dd0bbfa7d23910222e5835e0e56dfe` |
| `ledger.json` | `877c930510e0d431d5fbd60d7871d2cf03711643059e08fa9b5c91dcec31656c` |
| `edits_check.py` | `97b7d6016e94b3528aaf657547ac9ed40a966b6124e87bc6c80c38576ddcfb56` |
| `guards_check.py` | `ef89e1c79a0cc3c34af1ebb981e1674edd33a534d6f98612ee06ce57005b5cee` |
| `preserve_check.py` | `16302831c36620ab26abd1d476e83d1470f1da48bb41746ff6d930329d950d55` |

#### 31.12.10 The second delta review: R5, N5–N7

The second independent delta review, at `ba19109f`, is recorded on #1477 (comment 7076440898). It is REVISE on one
finding, R5, with nits N4–N7. N4 waits for an owner decision and is not part of this subsection.

**R5: `verify_run` fails open without a host `head_sha`.** Every executed-commit check sat under
`if head is not None`. A run record with no `head_sha`, or with `head_sha` null, was therefore VALID on self-reported
SHAs alone, which the owner's safeguard (c.7075869738) excludes.

*The fix.* A `head_sha` that is missing, null or not a 40-character lowercase hex id voids the run. The comparison of
`result.json`'s `workflow_sha` and `ref_sha` with the host's `head_sha` runs unconditionally, so a missing self-report
voids the run too.

*The fail-open audit.* Every optional value read by `verify_run` and by the R1 PDF comparison was checked for a missing
value that skips a check instead of failing it:

| Value | Before | After |
|---|---|---|
| `head_sha` (run record) | missing or null: every executed-commit check skipped (R5) | void |
| `id` (run record) and `run_id` (`result.json`) | compared as `str(...)`, so if both are missing, "None" equals "None" and the check passes | void unless both are present and equal |
| `result.json` not a JSON object | exception, a crash, not a pass | void |
| `event`, `path`, `head_branch`, `run_attempt` | compared with `!=`, so missing already voids | unchanged |
| `workflow_sha`, `ref_sha` | compared only under `head is not None` | compared unconditionally |
| `trial_sha` | missing already voids | unchanged |
| the workflow blob at W or at `head_sha` | `None` already voids | unchanged |
| `--run-meta` file missing or not parsing | already void (meta `None`) | unchanged |
| R1: the set of ledgered PDFs | an empty set compared nothing and passed | fails: no ledgered PDF to compare |
| R1: `build.rc`, `pdf-pages.tsv` | missing already fails | unchanged |
| R1: a malformed `pdf-pages.tsv` row | exception, a crash, not a pass | fails: malformed build record |
| R1: a PDF missing from the record or the build | already fails | unchanged |

`scope_check`'s required-absent entries pass when a file is missing. A deleted file is a separate finding of the tree
comparison (`file deleted`), so nothing passes on that account. This is recorded, not changed.

*New void and fail mutants:*
- `head_sha` key missing;
- `head_sha` null;
- `head_sha` not a hex id;
- run id missing on both sides;
- `result.json` not an object;
- R1 with an empty PDF set;
- R1 with a malformed record row.

Each must void or fail with its named finding.

**N5.** The blob test gets an isolated mutant: `verify_run` with the host `head_sha` = W, workflow base = H and
`main` = W. W contains H and lies on `main`'s first-parent history, so the only finding is the blob, and the mutant
requires exactly that one finding. The earlier double-duty mutant stays as well.

**N6: the reason for declining R-1, restated.**
- §31.12.4's reason is wrong. The proposed text does not exceed the kernel: `WaveSubstratumUnbounded.waveZ_sites`
  proves `(waveSubstratum d 0 q α).ι = (Fin d → ℤ)` by `rfl`, and the text claims no `A1` at `L = 0`.
- The correct reason is that R-1 is not caused by the retirement. The docstring understates the definition's range and
  does not generalize a finite-only result.
- The owner accepted R-1 only if demonstrably editorial and within the change's purpose. It is left unchanged.

**N7: the order of the subsections.**
- §31.12.5 and §31.12.6 point to "§31.13" for results. The results are §31.17 for §31.12–§31.12.9, and §31.19 for this
  subsection.
- The subsections appear in commit order: 31.12.1–31.12.7, 31.14 (pins), 31.12.8, 31.16 (pins), 31.12.9, 31.17
  (results), 31.18 (pins), 31.12.10, 31.19 (results), 31.20 (pins). There is no §31.13 or §31.15.
- The pins in force are always the last `Record pins` subsection, §31.20 from this round on.

**Checks.** The full battery of §31.12.6 is re-run from the plan head that carries §31.19, with the new mutants. The
ledger and the edit list do not change in this round, so the reconciliations must reproduce §31.17's figures (against
P\*: 302/60/9/26, drift 0; against `9ba8ef10`: 385/4/8, drift 0), and the ledger SHA-256 must stay `877c9305…`.

### 31.19 Results of §31.12.10–§31.12.11 at `53c6601a`

Each check was run at H from the checkers at `fef0f158`, the commit that applies §31.12.11 and carries the §31.21 pins.
`preserve_check.py` ran with `--plan fef0f158`, and `scipy` 1.18.1 was installed. Every run exited 0, and every result file
parses with verdict `pass`.

| Check | Result |
|---|---|
| `edits_check.py --self-test` | PASS (93) |
| `edits_check.py --static` | 0 in every scan, preservation for D400 and D401 included; sitemap 194/194 |
| `edits_check.py --commit 53c6601a --simulate` | 401/401 unique; residual 5, all allowed; 0 unscoped; 0 preservation |
| `edits_check.py --pins` | 0 / 0 |
| `edits_check.py --repo-scan --simulate --final` | 0 unexplained |
| `preserve_check.py --verify-ledger` | identical |
| `preserve_check.py --verify-pins` | PASS against §31.21 |
| `preserve_check.py --self-test` | PASS, 80 recorded checks (see below) |
| `--reconcile 55544cc3…` (P\*) | 302 unchanged, 60 shifted (the same 60 IDs as §31.2), 9 revised, 28 added (D374–D401), drift 0 |
| `--reconcile 9ba8ef10…` | 385 unchanged, 4 revised, 10 added (D392–D401), drift 0 |
| `guards_check.py --mutants` | PASS, 64 checks; simulated tree of 44 files edited by 401 records |
| `--predict`, then `preserve_check.py --tree --mutants` | 0 findings; scope assertions 46 present and 25 absent, 0 findings; the tree mutants fail |
| Coverage | exactly 7 fingerprints change; `coverage_check` OK |

The self-test's 80 checks include:
- every R5 void mutant: `head_sha` missing, null, empty, upper-case or not hex; no `head_sha` together with a
  self-reported H; the run id missing on both sides; `result.json` not an object, or missing `workflow_sha`; a `trial_sha`
  given as a ref name;
- the isolated workflow-blob mutant, with exactly one finding;
- the R1 empty-set and malformed-row mutants;
- the base countercontrol: the unedited base fails all 67 scope assertions the plan adds.

The reviewer's reproduction now voids. A run record without `head_sha`, with `result.json` self-reporting
`workflow_sha` = `ref_sha` = H, gives `RUN VOID` with three findings: the missing `head_sha`, and each self-reported SHA
differing from it.

**Ledger.** 399 splices in 44 files at H (401 edit records), SHA-256
`2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5`.

**Fail-open audit, found beyond §31.12.10's table.** A `trial_sha` given as a ref name (for example `HEAD`) resolved
through `git cat-file` and was accepted. It now must be a 40-hex id, with a void mutant.

### 31.20 Record pins

The digests below pin the record files from §31.12.10 on (R5: `preserve_check.py` fails closed);
`preserve_check.py` reads the last `Record pins` subsection, so §26.4, §31.11, §31.14, §31.16 and §31.18 stay as the pins of P*,
`9ba8ef10`, `785b17f9`, `3fa2d18f` and `0702dacc`. The ledger is unchanged from §31.18: 397 splices in 44 files at `53c6601a` (399 edit
records; D032 and D039 retain their text).

| File | SHA-256 |
|---|---|
| `edits.json` | `fff453b7165769d313a35ed8f9c1598634dd0bbfa7d23910222e5835e0e56dfe` |
| `ledger.json` | `877c930510e0d431d5fbd60d7871d2cf03711643059e08fa9b5c91dcec31656c` |
| `edits_check.py` | `97b7d6016e94b3528aaf657547ac9ed40a966b6124e87bc6c80c38576ddcfb56` |
| `guards_check.py` | `ef89e1c79a0cc3c34af1ebb981e1674edd33a534d6f98612ee06ce57005b5cee` |
| `preserve_check.py` | `657a8d987bc2cc0c96f658db3c46e32add91217e414bb046e5e680b97620ecf5` |

#### 31.12.11 Owner decisions on R5 and N4–N7

Owner decision, owner `amaybaum`,
[#1169 comment 7076485257](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7076485257), quoted in
part:

> | N4, `A6Instantiation.lean:55–56` and `:506–507` | Approved. Replace the assertion that finiteness is an axiom of the interface with wording that describes finiteness as a predicate, or as an explicit condition where required. Preserve the established finite-case theorems and their assumptions. Add N4 to the ledger's traceability and to its required-present and required-absent checks. |
> | N5 and N7 | Apply them if they are non-substantive corrections consistent with the review. |
> | N6, the R-1 explanation | Correct the explanation. The kernel does cover the L = 0 case. R-1 is excluded because it is not a correction caused by the retirement. |

For R5, the decision also requires failing closed when the host's `head_sha` is absent, null, empty or malformed
(anything other than 40 lowercase hex characters). It requires verifying always against trusted host metadata, and an
audit of both checkers with a void mutant for each missing-data bypass. §31.12.10 covers these. This subsection adds the
empty-string `head_sha` mutant, which the "missing or malformed" test already voids.

**N4, two new records (`lean-docstring`, semantic).** In the kernel, `A1` is a predicate on a `Substratum`
(`Substratum.A1 : Prop := Finite 𝒮.Conf`), not a field of the structure. The complex carrier is built as a `Substratum`
(`linkSubstratum`), and `cx3b_complex_not_A1` proves that it fails the predicate. "Finiteness is the first of the
interface's axioms" therefore misdescribes the kernel, and after the retirement it also reads as a premise.

| Record | Site | Old → new |
|---|---|---|
| D400 | `A6Instantiation.lean:55–56` (module docstring, `CX3`) | "because finiteness is the first of the interface's axioms and the complex\n  carrier is infinite" → "because the interface's finiteness predicate `A1` requires a finite configuration space\n  and the complex carrier's is infinite" |
| D401 | `A6Instantiation.lean:506–507` (docstring of `cx3b_complex_not_A1`) | "because finiteness is the first of the interface's axioms\nand the complex carrier is infinite" → "because the interface's finiteness predicate `A1` requires a finite\nconfiguration space and the complex carrier's is infinite" |

- *The finite-case results are unchanged.* `cx3b_complex_not_A1`, `cx3a_complex_axioms` and their statements are
  untouched, and the passages keep the distinction that the covariance statement comes inside and the complex carrier
  does not.
- *No overlap.* D401's old text ends at "is infinite." on line 507. D399's old text begins on line 508 ("the
  manuscripts' substratum is …"), and D319's two lines later. D400 lies in the module docstring, apart from D314–D316.
  The ledger's overlap check must confirm this.
- *Checks.* `SCOPE_PRESENT` gains both new phrases, and `SCOPE_ABSENT` gains "finiteness is the first of the interface's
  axioms". `PRESERVE` gains D400 and D401, `NEW31` gains D400–D401, and the edit list grows to 401 records and 399
  splices.

**N5 and N7** are applied as §31.12.10 states: one added mutant, and one appended sentence mapping the order. Both are
non-substantive. **N6** is §31.12.10's restatement.

**Expected after the re-pin.**

| Comparison | Expected |
|---|---|
| Against P\* | 302 unchanged, 60 shifted, 9 revised, 28 added (D374–D401), drift 0 |
| Against `9ba8ef10` | 385 unchanged, 4 revised, 10 added, drift 0 |
| Results | §31.19 |
| Pins | the last `Record pins` subsection, §31.21; §31.20 stays as the pins of `2fc36b1e` |

### 31.21 Record pins

The digests below pin the record files from §31.12.11 on (N4: D400, D401; the R5 mutants of the owner decision);
`preserve_check.py` reads the last `Record pins` subsection, so §26.4, §31.11, §31.14, §31.16, §31.18 and §31.20 stay as the pins of P*,
`9ba8ef10`, `785b17f9`, `3fa2d18f`, `0702dacc` and `2fc36b1e`. The ledger has 399 splices in 44 files at `53c6601a` (401 edit
records; D032 and D039 retain their text).

| File | SHA-256 |
|---|---|
| `edits.json` | `528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1` |
| `ledger.json` | `2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5` |
| `edits_check.py` | `2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c` |
| `guards_check.py` | `ef89e1c79a0cc3c34af1ebb981e1674edd33a534d6f98612ee06ce57005b5cee` |
| `preserve_check.py` | `b9d34e5daadc38184a98cb269096fe62dd4358acdd83698608f0618fd83bfe4e` |

#### 31.12.12 The final delta review's N8–N10

The final delta review at `c176d358` is recorded on #1477 (comment 7077120504), CONFIRMED WITH NITS. The owner chose
option (a), owner `amaybaum`, 2026-11-22T09:40:16Z,
[#1169 comment 7077295004](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7077295004), quoted in
part:

> 2. **A1 plan §31: option (a).** Apply N8, N9 and N10 from the final delta review (#1477 c.7077120504).
>    - `--verify-run` checks `plan_sha` against the designated plan commit. It is tested to reject an otherwise valid run of a different plan with the same ledger base.
>    - A short independent confirmation is obtained at the new head before the freeze decision.

**N8: the run is bound to the designated plan.**
- `--verify-run` requires `--plan P**`, the plan commit the owner designates. The run is void:
  - when `--plan` is missing or is not 40 lowercase hex characters;
  - when `result.json`'s `plan_sha` is missing or malformed;
  - when the two differ.
- Where the host run record carries the dispatch inputs (an `inputs` object), its `plan_sha` must equal `--plan` too. If
  `inputs` is present but malformed, the run is void.
- The GitHub run record does not carry dispatch inputs (review item, N8). In practice, therefore, the bound is
  `result.json`'s echo of the input against the designated P\*\*. The workflow derives the ledger base from that same
  input in its head step.
- The ledger and the ledger base are read from `--plan`'s objects (`plan_files`), so the run's trial parent is checked
  against that plan's ledger base.
- What stays a qualification: a run that executed one plan while echoing another is not detectable from the host record.
  The run's own checker result files (`preserve_check-*.json`, field `plan`) record the plan its checkers were read from,
  and an independent check of T0′/T1′ can compare them.
- *Mutants*, each void with its named finding:
  - `--plan` missing;
  - `--plan` malformed;
  - `plan_sha` missing;
  - `plan_sha` malformed (upper case, or a short id);
  - `plan_sha` differing from `--plan`;
  - a host `inputs.plan_sha` differing;
  - a malformed host `inputs`;
  - the owner's test: an otherwise valid run, with `result.json`, the host record and the inputs all consistent and the
    same ledger base H, but with `plan_sha` the commit `9ba8ef10`, whose ledger base is also H, where `--plan` is the
    current plan.
- A valid control passes.

**N9.**
- `run_attempt` must be the integer 1 exactly (`type(x) is int`), so `True`, `1.0` and `"1"` void the run.
- A path listed twice in `pdf-pages.tsv` fails the PDF comparison as a duplicate build record row, and does not resolve
  last-wins.
- Each has a mutant.

**N10.** The order of the subsections, extended from §31.12.10's mapping:
- 31.12.1–31.12.7, 31.14 (pins), 31.12.8, 31.16 (pins), 31.12.9, 31.17 (results), 31.18 (pins), 31.12.10, 31.19
  (results), 31.20 (pins), 31.12.11, 31.21 (pins), 31.12.12, 31.22 (results), 31.23 (pins).
- Any later subsection follows the same rule: its text first, then its results, then its pins.
- The pins in force are always the last `Record pins` subsection.

**Checks.** The full battery is re-run. The edit list and the ledger do not change in this round. The reconciliations
must reproduce §31.19's figures: against P\*, 302/60/9/28 with drift 0; against `9ba8ef10`, 385/4/10 with drift 0. The
ledger SHA-256 must stay `2055e68f…`.

### 31.23 Record pins

The digests below pin the record files from §31.12.12 on (N8, N9: `preserve_check.py`);
`preserve_check.py` reads the last `Record pins` subsection, so §26.4, §31.11, §31.14, §31.16, §31.18, §31.20 and §31.21 stay as the pins of P*,
`9ba8ef10`, `785b17f9`, `3fa2d18f`, `0702dacc`, `2fc36b1e` and `fef0f158`. The ledger is unchanged from §31.21: 399 splices in 44 files at `53c6601a` (401 edit
records; D032 and D039 retain their text).

| File | SHA-256 |
|---|---|
| `edits.json` | `528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1` |
| `ledger.json` | `2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5` |
| `edits_check.py` | `2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c` |
| `guards_check.py` | `ef89e1c79a0cc3c34af1ebb981e1674edd33a534d6f98612ee06ce57005b5cee` |
| `preserve_check.py` | `1f1f629d22a65f8b4c1027b723c35d1ea2ff3eed9322387c0d435d342c178abb` |

### 31.22 Results of §31.12.12 at `53c6601a`

Each check was run at H from the checkers at `ea1029d5`, the commit that applies §31.12.12 and carries the §31.23 pins.
`preserve_check.py` ran with `--plan ea1029d59b0bc0de7c5e21790d6011d83738e8bd`, and `scipy` 1.18.1 was installed. Every
run exited 0, and every result file parses with verdict `pass`. In the file this subsection follows §31.23, which the
apply commit wrote first; the order of N10 is the logical order, and the pins in force are §31.23's, the last
`Record pins` subsection.

| Check | Result |
|---|---|
| `edits_check.py --self-test` | PASS (93) |
| `edits_check.py --static` | infinity 0, register 0, capitals 0, identifier 0, preservation 0, mirror parity 0, Lean docstring-only 0; sitemap 194/194 |
| `edits_check.py --commit 53c6601a --simulate` | 401/401 unique; residual 5, all allowed; 0 unscoped; 0 preservation; 0 identifier |
| `edits_check.py --pins --commit 53c6601a` | 0 unresolved, 0 missing |
| `edits_check.py --repo-scan --simulate --final --commit 53c6601a` | 0 unexplained |
| `preserve_check.py --verify-ledger` | identical |
| `preserve_check.py --verify-pins` | PASS against §31.23 |
| `preserve_check.py --self-test` | PASS, 93 recorded checks, all `pass` (see below) |
| `--reconcile 55544cc3…` (P\*) | 302 unchanged, 60 shifted, 9 revised, 28 added (D374–D401), drift 0 |
| `--reconcile 9ba8ef10…` | 385 unchanged, 4 revised, 10 added (D392–D401), drift 0 |
| `guards_check.py --mutants` | PASS, 64 checks: the 14 checks on the simulated tree (44 files edited by 401 records), F71 among them; CC-1–CC-4 failing as named; 30 listed pins, 0 unlisted strings |
| `guards_check.py --predict`, then `preserve_check.py --tree --mutants` | 44 files edited, 9 TeX rebuilt, 7 fingerprints re-affirmed; 0 findings; scope assertions 46 present and 25 absent, 0 findings; the 5 tree mutants fail as required |
| Coverage | `tools/coverage_check.py` on the predicted tree: OK, 132 canonical statements |

The figures required by §31.12.12 are reproduced: both reconciliations, and the ledger SHA-256.

The self-test's 93 checks are §31.19's 80 and 13 new ones, each failing with its named finding:
- N8: `plan_sha` null, upper case or a 12-character id; `plan_sha` differing from the designated plan; host `inputs`
  carrying another plan; host `inputs` malformed; `--plan` missing; `--plan` malformed;
- N8, the owner's test: a run of `9ba8ef10`, whose ledger base is H, with `result.json`, the host record and the inputs
  consistent, is valid against `--plan 9ba8ef10…` and void against the designated plan;
- N9: `run_attempt` `True`, `1.0` and `"1"`; a path listed twice in `pdf-pages.tsv`.

The valid control passes.

**Further probes of `verify_run`** at `ea1029d5`, loaded unchanged, with the self-test's objects (trial `556cfb08`, host
`head_sha` W) and `--plan ea1029d5…`:
- the valid control: 0 findings;
- `plan_sha` absent from `result.json` (the key, not a null value): void, "missing or not a full commit id";
- the owner's test in the shape of a real host record (no `inputs`), `plan_sha` = `9ba8ef10…`: void with exactly one
  finding, "is not the designated plan"; the same run against `--plan 9ba8ef10…` has 0 findings;
- `run_attempt` 2, or absent: void;
- `--plan` empty: void, "no designated plan".

From the command line, with `result.json` carrying `plan_sha` = `9ba8ef10…` and a valid run record:
- without `--plan`: `RUN VOID` ("no designated plan", and the plan mismatch), exit 1. `--plan` is required in the
  sense that its absence voids the run; the argument parser does not reject it;
- with `--plan ea1029d5…`: `RUN VOID`, the plan mismatch alone, exit 1;
- with `--plan 9ba8ef10…`: `RUN VALID`, and `RESULT FAIL`, exit 1, because the checker's own bytes are not
  `9ba8ef10`'s pinned copy. A run of another plan is checked with that plan's own checker.

**Where the plan of a real dispatch is recorded.** A real dispatch of `a1exit-trial-verify.yml` does not expose
`plan_sha` in the host's run record.
- The workflow at W (`413b0bb8`) takes `plan_sha` as a `workflow_dispatch` input. It sets no `run-name`, so the run's
  `display_title` is the workflow name. It writes `plan_sha` only into `result.json`, from `env.PLAN`, and names its
  artifact after `trial_sha` alone.
- The Actions run object (`GET …/actions/runs/{run_id}`) has no `inputs` field. The two existing dispatches of this
  workflow (runs 44939798305 and 44951832698, dispatched at earlier `main` commits) return 35 keys, none of them
  `inputs`, and `display_title` "A1-EXIT trial verify". Their jobs' step names are the workflow's fixed names.
- So no host data carries the plan commit, and `verify_run`'s check of `inputs` never applies to a real run. For a real
  T0′ or T1′ the plan bound rests on `result.json`'s self-reported `plan_sha` together with `--plan`.

*The limitation.* A run that executed one plan while reporting another in `result.json` is not detectable from GitHub's
host record. What does bind the plan: the workflow's head step reads the ledger base from `plan_sha`'s own
`ledger.json`; its checker steps run `plan_sha`'s pinned checkers from a worktree of that commit; and each checker's
structured result file (`preserve_check-*.json`) records, in its `plan` field, the plan it was read from. An independent
check of T0′ or T1′ compares those fields with `--plan`. These are outputs of the run, not host records.

**Not run here.**
- The PDF build: this container has no xelatex, so no PDF was rebuilt (0 PDFs checked), and the fail-closed comparison
  of §31.12.1 has not run against a real CI build.
- No real host run record has been checked; `verify_run` has run only on fixtures. Both come from T0′, which needs its
  own dispatch authorization, as does T1′.

**Ledger.** Unchanged from §31.21: 399 splices in 44 files at H (401 edit records), SHA-256
`2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5`.

#### 31.12.13 The P3 pre-audit: B1, expected skips, the trial refs, the host record and the §A.42 route

The independent P3 pre-audit of the plan at `ea1029d5` is recorded on #1477 (comment 7077602092): one blocker, B1. The
owner's decisions on it, owner `amaybaum`, 2026-11-22T10:32:44Z,
[#1169 comment 7077861392](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7077861392), quoted in
part:

> **(i) One append-only §31 amendment, then independent review.**
> - **B1.** Only page-count and extracted-text differences are allowed in T0′'s PDF comparison. T1′ must pass the comparison for all nine PDFs.
> - **Expected skips.** Expected skips are recorded by workflow and event. T0′ skips guards after the expected `preserve` failure, and still uploads its result and all nine PDFs. Any unexpected skip is a finding.
> - **T0′ branch push.** The dedicated ref, the exact trial SHA and the check of push-triggered workflows are preregistered. The push and the dispatch return to the owner for approval after the amended plan has been reviewed and frozen.
> - **Host record.** It is verified against GitHub's original run metadata. The redacted copy must keep the required fields and types, and must give the same verifier result.
>
> **(ii) The §A.42 route: verification after landing.** T0′ and T1′ still gate the execution decision. The durable evidence gap closes only after independent verification from `main`. That verification includes confirming that FULL.pdf prints the corrected Theorem 24(i) (#1539).

**Goal link (§A.47).** A1-EXIT (#1169): this subsection fixes, before T0′ is built, the decision rule by which T0′ and
T1′ are judged, the refs and records they use, and the route by which their evidence reaches `main`; it decides no
execution question and authorizes no push or dispatch.

**Order.** This text first; then the checker change and the record pins, §31.25; then the results, §31.24. The pins in
force are the last `Record pins` subsection.

**B1: the T0′ PDF expectation, superseded.**
- *Superseded text.* §31.12.1's N3 paragraph says that at T0′ "`preserve` fails with only `--pdf-compare` text findings
  for the nine PDFs". That clause is superseded by the rule below, which governs T0′ and T1′ wherever §29 item 1, §31.8
  or §31.12.1 differ from it.
- *Why.* "Text findings" was narrower than §29 item 1 and §31.8, which say "only `--pdf-compare` findings". It was also
  narrower than the content findings `pdf_compare` emits, which are of two kinds, a page count and an extracted text. At
  T0 the run reported `papers/Structure.pdf: 94 pages committed, 95 built` beside the text findings, and the owner
  accepted T0 as matching (#1169 comment 7068143470). The nine committed PDFs at H are those of T0's base, so T0′ is
  expected to repeat that page-count finding.
- *The rule for T0′.* `preserve` fails. In its structured reports the only failing check is the tree report's
  "committed PDFs against the CI build (pages, pdftotext)". Every finding of that check is one of the two content kinds,
  for one of the nine ledgered PDFs (`papers/Complexity.pdf`, `Computation`, `GR`, `Main`, `Methodology`, `SM`,
  `Structure`, `Substratum`, and `book/The-Incompleteness-of-Observation-FULL.pdf`):
  - `<pdf>: <n> pages committed, <m> built`;
  - `<pdf>: extracted text differs from the CI-built PDF`.

  Every other finding is a deviation. That covers the fail-closed findings of §31.12.1 (build failed, no build record,
  not rebuilt, record mismatch, stale, missing, malformed or duplicate row, empty set), a content finding for any other
  path, and a finding in any other check or report.
- *The rule for T1′.* The PDF comparison passes for all nine PDFs, with no finding, and every report passes.
- *In the checker.* `preserve_check.py --expect-trial T0|T1 OUT` reads the run's output directory OUT
  (`result.json`, `preserve_check-{verify-pins,verify-ledger,commit,tree}.json` and, for T1, `guards_check-mutants.json`)
  and prints `TRIAL EXPECTED` or `TRIAL DEVIATION` with each finding. With `--jobs JOBS.json`, the host's jobs record of
  the run (`GET .../actions/runs/{run_id}/jobs`, saved whole), it also checks every step conclusion; with `--built DIR`,
  the artifact's built PDFs, it checks that all nine are present. The nine PDFs are read from the plan's ledger, as
  `--pdf-compare` reads them.
- *Mutants.* The control is T0's real evidence on `main` (`a1exit-trial-t0-20261121`, eight PDFs, with the Structure
  page-count finding): it is expected under the T0 rule. Each of the following is a deviation with its named finding:
  - a fail-closed finding (a stale PDF) added to the PDF comparison;
  - a content finding for a PDF outside the ledgered set;
  - a finding in another check of the tree report;
  - a failing `--commit` report;
  - the PDF comparison check missing;
  - a T0 tree report in which the PDF comparison passes;
  - T1's real evidence with a text finding added to its PDF comparison, under the T1 rule.

  T1's real evidence (`a1exit-trial-t1-20261121`) is expected under the T1 rule.

**Expected skips, by workflow and event.** Any skip not on this list is a finding, and so is any listed step that does
not conclude as listed.

| Trial | Workflow, event | Step (job) | Conclusion | Why |
|---|---|---|---|---|
| T0′ | `a1exit-trial-verify.yml`, `workflow_dispatch` from `main` | "P's preserve_check.py --commit, then --tree --mutants --pdf-compare" (`verify`) | failure | the B1 findings |
| T0′ | same | "P's guards_check.py --mutants" (`verify`) | skipped | no `if:`, so the implicit `success()` is false after `preserve` fails |
| T0′ | same | "Every required step succeeded (a skipped step fails)" (`verify`) | failure | `if: ${{ always() }}`; it fails on `preserve` and `guards` |
| T0′ | same | "Write result.json", "Upload result.json, logs and the built PDFs" (`verify`) | success | `if: ${{ always() }}`; the upload holds `result.json` and all nine PDFs |
| T1′ | `a1exit-trial-verify.yml`, `workflow_dispatch` from `main` | none | | every step succeeds |
| T1′ | `verify.yml`, `workflow_dispatch` on the T1′ ref | "KTRANS-SEP-2 marker complete reports with an axiom outside the three" (Mathlib bridge) | skipped | `if: ${{ !cancelled() && steps.ktrans_sep2_axioms.outputs.reports == 'complete-nonstandard' }}`; false when the fifteen reports lie within the three axioms, as at T1 (run 44953482787) |

Every other step concludes `success`, every job of T1′'s `verify.yml` run concludes `success`, and no job is skipped.
The other conditional steps and jobs of `verify.yml` at H run on `workflow_dispatch` and must succeed:
- the `if: ${{ !cancelled() }}` steps of Mathlib bridge (KTOKEN-MAXCONE-1 check A3 and the first three KTRANS-SEP-2
  steps);
- the Numerical probes / A42 exclusion matrix, `if: ${{ github.event_name == 'workflow_dispatch' }}`;
- the three ARP-1-MARC steps whose conditions hold on `workflow_dispatch`;
- the Numerical probes aggregate, `if: ${{ always() }}`.

In the result step's `steps` record, T0′ has `preserve` failure and `guards` skipped, and every other step success. T1′
has every step success.

*In the checker.* `--expect-trial` applies the `a1exit-trial-verify.yml` rows to `result.json` and, with `--jobs`, to the
host's step conclusions. `--expect-verify JOBS.json` applies the `verify.yml` row to the host's jobs record of the
`verify.yml` run. Mutants:
- under `--expect-trial`, an unexpected skip (`build` skipped), `guards` failing instead of skipped, and the upload step
  not succeeding;
- under `--expect-verify`, starting from T1's real record (`ci-record.json`, expected), the marker step succeeding,
  another step skipped, and a job skipped.

**T0′ and T1′ refs.**
- *Names.* T0′ is pushed to the new ref `trial/a1exit-T0prime-<P8>`, and T1′ to `trial/a1exit-T1prime-<P8>`, where
  `<P8>` is the first eight hex digits of P\*\*. T0 and T1 used `trial/a1exit-T0-55544cc3` and
  `trial/a1exit-T1-55544cc3`. Neither ref exists before its push.
- *Exact SHA.* After each push, `git ls-remote origin refs/heads/<ref>` must print exactly the trial commit's full id.
  The ref does not move while its trial is being verified.
- *Push-triggered workflows.* A push runs the workflows of the pushed commit's tree, which for a trial commit are H's,
  since no trial commit changes a workflow file. At H four workflows have a `push` trigger:

  | Workflow | Push filter | On a trial ref |
  |---|---|---|
  | `verify.yml` | `branches: [main]` | not run |
  | `hidden-sector-replay.yml` | `branches: [main]` and paths | not run |
  | `bg2-orientation-design.yml` | paths under `verification/programmes/oi-qm/reconstruction/bekir-golomb-orientation-design/` and the workflow file | not run unless a changed file matches |
  | `bridge-compatibility-research.yml` | paths under `bridge-compatibility-audit/`, `physical-state-operation-compatibility/`, `OIBridge/BridgeFiniteProtocol.lean` and the workflow file | not run unless a changed file matches |

  *The check.* Before each push, list the files the trial commit changes against H, and against `main`, and confirm that
  none matches either path filter. Then confirm that the ref's host runs list (`GET .../actions/runs?branch=<ref>`)
  shows no push run after the push. None of the four is a governed launch: none designates, attests, dispatches or
  pushes. The pushes of T0 and T1 started no run.
- *Authorization.* Pushing either ref, the T0′ dispatch and the T1′ dispatches each need owner approval, given after
  this amended plan has been independently reviewed and frozen. Nothing in this subsection pushes or dispatches.

**The host record.**
- *What is verified.* `--verify-run` reads GitHub's original run metadata as `--run-meta`: the run object
  `GET /repos/{owner}/{repo}/actions/runs/{run_id}`, fetched from the API at check time and saved whole and unmodified.
- *The redacted copy.* A redacted copy may be retained. It removes the e-mail fields (§A.42 item 4): every key named
  `email`, which the run object carries at `head_commit.author.email` and `head_commit.committer.email`. It carries its
  own SHA-256 digest. The copy keeps every field `verify_run` reads with the same value and JSON type: `id` (integer),
  `event`, `path`, `head_branch` and `head_sha` (strings), `run_attempt` (integer), and `inputs` when present.
- *In the checker.* `--verify-run ... --run-meta ORIGINAL --run-meta-redacted COPY` voids the run unless:
  - the copy keeps each of those fields with the same value and type;
  - the copy carries no `email` key;
  - the copy equals the original with every `email` key removed, and nothing else changed;
  - `verify_run` gives identical findings on the original and on the copy.

  The copy's SHA-256 is printed.
- *Mutants.* Each of the following voids with its named finding:
  - a copy that drops `head_sha`;
  - a copy whose `id` is the string `"1"`, which `verify_run` alone would accept, since it compares `str(id)`;
  - a copy that keeps an e-mail field.

  The control is the redaction of a valid run object carrying both e-mail fields: valid, with the same findings (none)
  as the original.

**The §A.42 route.**
- T0′ and T1′ gate the execution decision, and only that.
- The durable evidence gap stays open after T1′. The trial commits and P\*\* are not on `main`, and the CI runs and
  their logs are provenance (§A.42 item 2). It closes only after landing, by independent verification from `main`. That
  verification includes confirming that the landed `FULL.pdf` prints the corrected Theorem 24(i) (#1539).
- No new temporary exception to §A.42 item 2 is added.

**Checks.** The full battery is re-run from the commit that applies this subsection and carries §31.25, with the new
mutants. The edit list and the ledger do not change, so the reconciliations must reproduce §31.22's figures: against P\*,
302/60/9/28, drift 0; against `9ba8ef10`, 385/4/10, drift 0. The ledger SHA-256 must stay `2055e68f…`. In addition, the
push-trigger check above is run on the predicted tree against H, and against `main`.

### 31.25 Record pins

The digests below pin the record files from §31.12.13 on (B1, the expected skips and the redacted host record:
`preserve_check.py`). `preserve_check.py` reads the last `Record pins` subsection, so §26.4, §31.11, §31.14, §31.16,
§31.18, §31.20, §31.21 and §31.23 stay as the pins of P*, `9ba8ef10`, `785b17f9`, `3fa2d18f`, `0702dacc`, `2fc36b1e`,
`fef0f158` and `ea1029d5`. The ledger is unchanged from §31.21: 399 splices in 44 files at `53c6601a` (401 edit records;
D032 and D039 retain their text).

| File | SHA-256 |
|---|---|
| `edits.json` | `528f146d03b29cbc3d7dc29948e3dd1d4cd26f4d36e6e009f032e24f9462dec1` |
| `ledger.json` | `2055e68f2343d00cec93bc35ecbccae21d46d1da154ee1a842663f1e4fec32b5` |
| `edits_check.py` | `2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c` |
| `guards_check.py` | `ef89e1c79a0cc3c34af1ebb981e1674edd33a534d6f98612ee06ce57005b5cee` |
| `preserve_check.py` | `95835b28a02713e26682a16a18a02dc3fd71c0164a8bb4ec342cae911a1fc7d3` |
