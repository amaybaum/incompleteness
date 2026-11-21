# C14-AUDIT — wording of the foundational conditions C1–C4 across the corpus

**Status: WIP / UNVERIFIED.** The first review, of `5265e59d` (c.7066810484), returned REVISE (narrow). This revision applies it: the ch01 table correction, F2b, the added sites, the Lean C2 difference and the reviewer's ranking. The revision has not itself been reviewed. Read-only with respect to the manuscripts:
nothing here edits a paper, a chapter, `FULL.md`, the glossary or a Lean module, and nothing here
changes scientific meaning. The suggested wordings in §7 are proposals only.

- **Authority.** Owner decision on #1169 (c.7066602480, item 3): a narrow, read-only audit that
  identifies inconsistent names, definitions and theorem references, with no automatic paper
  corrections and no change of scientific meaning.
- **Starting list.** FIN-SCOPE (#1497 at `e6a51be7`,
  `verification/audits/foundations/fin-scope-design-20261121/SPEC.md` §2.5): its canonical-definition
  map and proposed copy groups. They were used as a starting list and re-derived independently (§6).
- **Tree audited.** `main` at `df6da1c6`. Every file the #1477 ledger touches is byte-identical
  between that ledger's drafting base `97070c98` and `df6da1c6`, so ledger line numbers and the
  line numbers here agree.
- **Verification layer.** Prose and status checks only: text search, reading and comparison. No
  computation, Lean build or exact check was run, and none of the findings below is a mathematical
  result. Where a finding says a cited theorem does or does not use a condition as stated, that is
  a reading of the theorem's statement in the manuscript or Lean source, not a new proof.

## 1. Method

`build_register.py` (this directory) scans `papers/*.md`, `book/*.md` (chapters, glossary, README,
`FULL.md`), the root `README.md`, `verification/README.md`, and the Lean modules that name the
conditions. It matches a word-bounded `C1`–`C4`, Cyrillic `С` included, in every typographic form:
parenthesized `(C1)`, bold run-ins `**(C1)**` and `**C1 (…)**`, italic run-ins, table rows, list
items, headings, ranges (`C1–C4`, `(C1)–(C3)`), slashed lists (`C1/C3/C4`), sub-forms (`C2-slow`,
`C2-structural`, `C2-mixing`), and Lean identifiers (`c3_necessity`, `CoreC1C4`). It writes one row
per match, giving file, line, column, condition, class, a #1477-ledger flag, the chapter source of
each `FULL.md` row, a note, and an exact excerpt of the line around the match.

- **What is kept.** Under §A.28, `register.tsv` keeps only the 542 hand-classified rows, the
  rows the findings rest on.
- **What is not kept.** The 1,553 rule-classified `reference` rows and the 101 `unrelated` rows
  are not needed by any finding, and are not committed.
- **Regenerating.** `--full` prints the whole scan to stdout, so those rows stay reproducible from
  the script without a committed copy.
- **Drift.** `python3 -I verification/audits/foundations/c14-audit-20261121/build_register.py
  --check` regenerates the kept rows and fails on any drift.

- **Counts.** 2,196 matches. Of these, 1,553 are inline references, 101 are unrelated labels, and
  542 carry a reviewed class. One guard-string line, `papers/oi_lattice_code/architecture_check.py:1086`, was added at review.
- **Reviewed rows.** Every occurrence that names, glosses, defines, applies or cites a condition
  was read in context and classified by hand. That covers the definitional paragraphs, list items,
  table rows and parenthetical glosses, the theorem citations, and every inline mention that makes
  a status claim about the conditions (for example "structural conditions", "necessary").
  A reviewed class applies to the condition(s) named in the note, on that line.
- **Inline references.** The remaining inline mentions, such as "C1, C3 and C4 govern …", are
  classed `reference` by rule. They carry no definition, and they were not individually reviewed
  beyond the status-phrase searches of §4.
- **Mirrors.** Every chapter line that mentions a condition occurs byte for byte in `FULL.md`, and
  every such `FULL.md` line has a chapter source. `FULL.md` rows inherit their source's class.
- **Excluded by construction.** `$C_4$` (a ring), `$\Delta C_2$` (a Casimir) and `$C_1,\ldots,C_k$`
  (cycles) in GR; Juno's "Condition 1/2"; and Introduction:129's "condition 4", which is
  completion condition (iv) of Main §3.4. None of these names an OI condition.

## 2. Canonical definitions

The canonical definitions are clear for definitional purposes, but the canonical file is not
uniform: Main itself departs from §1.3's typing at :326 (F2b), and §3.4's heading at Main:439
reads "The Characterization Theorem: Necessity of the Conditions" (see F3). With that
qualification, they are `papers/Main.md` §1.3: `:72` **(C1) Non-zero coupling**,
`:74` **(C2) Memory persistence**, `:76` **(C3) Sufficient memory capacity** and `:78` **(C4) History
readback**. Every other restatement cites `[Main §1.3]` or `[Main §3]`, and only these four
paragraphs carry each condition's status, dependency and realization clauses.

- **The typing of the conditions.** Main:74 types C2 as "**a physical-regime premise, not a
  structural condition** — and the distinction is load-bearing. C1, C3 and C4 are the structural
  conditions: the characterization's equivalence runs over those three (§3.4)". The same typing
  appears at Main:546, where "Condition (C2) is deliberately absent from (iii)", and at Main:636,
  "Of the three structural conditions, only (C4) is logically independent".
- **The two forms of C2.** Main:74 names two forms and says they are not equivalent.
  - (C2-structural): "a hidden record of visible history, once written, persists to the readback
    that uses it".
  - (C2-slow): "$\tau_S \ll \tau_B$". It "implies (C2-structural) under the uniform-erosion
    estimate … but not conversely: what is required is that records persist, not that the hidden
    sector evolve slowly". Unqualified "(C2)" means the persistence requirement.
- **C4 is operational.** Main:78: "it does not by itself assert a causal write-then-read cycle — a
  pre-sampled hidden variable revealed by the history satisfies it."
- **The book's canonical surface.** `book/ch01-observation.md:53–59` (`FULL.md:386–392`),
  "Condition C1 (Non-zero coupling)" through "Condition C4 (History readback)", uses Main's four
  names exactly. The glossary (`:25–31`, `FULL.md:6516–6522`) is a second book surface with two
  different names (§3).

## 3. Names in use

| | Canonical (Main §1.3) | Other names, with sites |
|---|---|---|
| C1 | Non-zero coupling | **Coupling**: glossary:25, Medicine:27, Structure:112. *coupling*: GR/ch07:24, ch09:112, ch12:42, ch15:59, ch16:196, ch18:67, Complexity:364, Structure:530. *non-trivial coupling*: GR:617, Substratum:127, SM:52, Main:153, ch18:294. *catalytic-conformational coupling*: ch13:50. *coupling, realized as catalytic feedback*: ch11:152. Application names: ch11:66, book/README:74. |
| C2 | Memory persistence | **Record persistence**: Structure:114, Complexity:27, Structure:711, Methodology:108, GR:617, Substratum:127.  **conformational timescale separation**: ch13:52. *persistence*: ch11:154. *template persistence*: ch11:66. Undefined sub-form **C2-mixing**: Structure:138, Substratum:24, :195, :367, ch02:88. |
| C3 | Sufficient memory capacity | **Hidden-sector capacity**: glossary:29. **Capacity**: Medicine:31.  *Sufficient capacity*: Structure:116, ch07:28, ch09:116, ch12:46. *capacity*: ch11:156, ch15:63, ch16:210, ch18:69, Complexity:368. *conformational landscape capacity*: ch13:54. *high-capacity hidden sector*: Main:153. *sequence capacity*: ch11:66. |
| C4 | History readback | Uniform everywhere ("history readback"), apart from the application name *template-directed readback* at book/README:74. |

Book `ch*` lines are mirrored at the `FULL.md` lines in `register.tsv` (for example ch13:52 is
FULL:3473). The ch01:249–253 table cells are failure modes under the column "What fails", not
names, and are not listed here (§4, correction).

## 4. Inconsistencies, ranked by whether they could change scientific meaning

**Ranking.** The order follows the review of `5265e59d` (c.7066810484):
F3 > F5 > F7 > F2 (with F2b) > F11 > F4/F12 > the rest. Finding IDs are identifiers, not ranks.

**Correction to `5265e59d`.** That head read the ch01:249–253 table as naming C2 "Timescale
separation" and C3 "Capacity hierarchy". It treated these as naming inconsistencies (F1, in part,
and F6), and repeated FIN-SCOPE's reading of the same rows. That reading was wrong. The table's
second column is headed "What fails": its cells name the failure mode of each limit model, not the
condition. Both naming findings are withdrawn. The real issue in the C2 row is recorded in F1
below. F6 is withdrawn with no replacement.

### 1. F3 — "necessary for an embedded observer to exist", and other necessity claims

- *Sites:*
  - Structure:110, introducing the (C1)–(C4) list at :112–118: "four conditions on a
    substratum's bijection $\varphi$ that are necessary for an embedded observer to exist
    [Main §3]".
  - Structure:734: "random permutations on finite sets typically lack the coupled-dynamics,
    slow-local-mixing, and high-capacity features required for C1–C4". This also glosses C2 as
    slow local mixing and C3 as high capacity.
  - ch18:276 (FULL:5007): "Any conscious system must implement a partition with substantial C1–C4
    structure. … The C1–C4 architecture is necessary for the non-Markovian information
    processing that conscious systems must exhibit."
  - ch18:286 (FULL:5017): "*C1–C4 architecture is necessary for non-Markovian information
    processing.*"
  - ch18:24 (FULL:4755) and ch18:296 (FULL:5027): "necessary structural conditions".
- *Canonical text.*
  - Main:70: "diagnostics of a realization rather than hypotheses of the characterization … (C2)
    is a physical-regime premise".
  - Main:546: C2 "is not needed for the equivalence".
  - SM:52: "conditions on the partition, not on the lattice".
- *How they differ.* Main proves C1 and C3 necessary only inside the memory-bearing sector, as
  consequences of C4 or of observed non-Markovianity. It proves no necessity for an observer's
  existence. It treats C2-slow as one sufficient mechanism, not a necessary one: in the fast
  shift-register bath of Main:74, C4 holds while C2-slow fails. Structure:110 also places the
  conditions on $\varphi$, where Main and SM place them on the partition and its realization.
- *Canonical heading.* The canonical paper's own heading for §3.4, Main:439, reads "The
  Characterization Theorem: Necessity of the Conditions". The body under it proves necessity only
  within the memory-bearing sector: C4 coincides with non-Markovianity in a faithful realization,
  C1 and C3 follow from it, and C2 is deliberately absent from (iii) (Main:546). A citer reading
  the heading alone could take it as necessity for an observer. The heading is a plausible source
  of F3's wording, but it does not license that wording.
- *Assessment.* A necessary-versus-diagnostic overstatement.

### 2. F5 — C4 stated as a causal write-then-read

- *Site.* Structure:118: "(C4) **History readback.** The interaction must read back what was
  written — the load-bearing memory condition."
- *Canonical text.* Main:78: "The condition is operational; it does not by itself assert a causal
  write-then-read cycle — a pre-sampled hidden variable revealed by the history satisfies it."
- *How they differ.* The Structure wording requires a written record to be read back. That is the
  cosmological *realization* clause, which Main:78 leaves "to be demonstrated". It makes C4
  strictly stronger, and it excludes witnesses Main admits: the response-table construction, and
  Medicine:88's $(v,h)\mapsto(v\oplus h,h)$.
- *Lower-risk relatives:*
  - Introduction:85, "feed the record back into what is seen", a non-technical gloss.
  - ch09:116, "the correlations the read-write cycle generates".
  - SM:1376, "the record surviving to a readback the coupling performs". This is an explicit
    hypothesis of Theorem 22, so it strengthens an assumption, not a conclusion.

### 3. F7 — C3 as storing "the interaction history"

- *Sites.*
  - Structure:116: "(C3) **Sufficient capacity.** The hidden sector must have information
    capacity enough to store the interaction history."
  - Structure:534: "sufficient information capacity to store the interaction history".
- *Canonical text.* Main:76: "enough distinguishable states to encode the observed conditional
  past–future information: $\log_2 |\mathcal{C}_H| \geq I^*$".
- *How they differ.* The interaction history is in general far larger than $I^*$, and Main:522
  denies the cumulative reading: "$m \gtrsim 2^{K I_0}$" needs "the additional hypothesis that
  the per-event contributions accumulate without hidden-state reuse or compression".

### 4. F2 — "structural conditions C1–C4" against Main's typing of C2 as not structural

- *Canonical text.*
  - Main:74: "a physical-regime premise, not a structural condition — and the distinction is
    load-bearing. C1, C3 and C4 are the structural conditions".
  - Main:636: "Of the three structural conditions".
  - glossary:29: "the framework's three structural conditions (C1, C3, C4)".
- *Sites that type all four as structural:*
  - GR:617: "[Main]'s structural conditions C1 (non-trivial coupling), C2 (record persistence — …)".
  - Structure:528: "The structural conditions for observer admission [Main §3]".
  - Structure:711: "the framework's structural conditions C1–C4".
  - ch09:88 (FULL:2503): "any substratum with the framework's structural conditions at its
    horizon. The specific cubic-lattice substratum is *one way* C1–C4 are satisfied".
  - appendix-c:172 (FULL:6327): "the C1–C4 structural conditions".
  - appendix-c:291 (FULL:6446): "C1–C4 structural conditions operating at different scales".
  - ch11:10 (FULL:2973): "the framework's structural conditions C1, C2, C3, C4".
  - ch14:107 (FULL:3707): "The framework's structural conditions C1–C4".
  - ch18:24 and ch18:296, under F3.

**F2b — the canonical paper's own slip.**

- *Site.* Main:326, mirrored at appendix-b:90 (FULL:5767): "Coherence preservation is a property
  of this realization, not an additional structural condition: (C1)–(C4) constrain coupling,
  timescales, and capacity".
- *How it differs from Main §1.3.*
  - "Not an *additional* structural condition" types all four of (C1)–(C4) as structural,
    contrary to Main:74.
  - "Timescales" glosses C2 by its C2-slow mechanism, where Main:74 says what is required is
    that records persist, not that the hidden sector evolve slowly.
  - The list omits readback, which is C4's content.
- *Assessment.* The canonical file itself carries the F2 typing at one site outside §1.3.

### 5. F11 — ch09 announces C1–C4 and lists three

- *Site.* ch09:84 (FULL:2499): "C1–C4 specify the admission criterion".
- *How it differs.* The list at ch09:112–116 has C1–C3 and no C4 entry. ch09:118 then says
  "These conditions specify the observer-admission criterion". The load-bearing condition, C4,
  is missing from a criterion stated as complete.

### 6. F4 and F12 — C1 as "substantial" coupling, and application paragraphs asserting more than C1 requires

- *F4 sites.*
  - Structure:112: "(C1) **Coupling.** The interaction between the observer's degrees of freedom
    and the rest must be substantial."
  - Structure:530: "requires substantial coupling between visible-sector and hidden-sector
    dynamics".
  - ch18:276: "substantial C1–C4 structure".
- *Canonical text.* Main:72: "$H_{\text{int}} \neq 0$: hidden degrees of freedom affect the visible
  evolution at some accessible step — the conditional law of some visible transition depends on
  the hidden state."
- *How F4 differs.* "Substantial" is a magnitude requirement that Main does not impose, and it
  drops the accessible-conditional criterion.
- *F12, application paragraphs:*
  - ch13:50 (FULL:3471): "C1 is satisfied with substantial coupling strength". It asserts
    satisfaction without the accessible-conditional witness that Main:72 and ch01:53 require.
  - ch11:152 (FULL:3115) requires two-way feedback: "the template must direct synthesis … and
    the synthesis must maintain the template". Main's C1 is one-way hidden-to-visible influence,
    and Medicine:88 says C1 "does not require the visible sector to act back on the hidden state".

### 7. The rest

**F1 — C2 named or stated by its slow-bath mechanism, and the ch01 C2 table row.**

- *Canonical text.* Main:74: (C2-slow) "implies (C2-structural) … but not conversely: what is
  required is that records persist, not that the hidden sector evolve slowly".
- *Naming sites:*
  - ch13:52 (FULL:3473): "**C2: conformational timescale separation.**" The paragraph treats
    $\tau_S/\tau_B$ only.
  - ch18:68 (FULL:4799): "C2 (memory persistence): the hidden sector must retain a record …,
    $\tau_B \gg \tau_S$ with $\tau_B$ the coarse-grained mixing time — slow hidden dynamics is
    one sufficient mechanism, not the condition itself". The item states the condition as the
    C2-slow inequality and denies that reading in the same breath.
- *The ch01 C2 table row.* ch01:252 (FULL:585) reads `| C2 | Timescale separation | Markovian
  stochastic | Thermalized observer |`.
  - The failure mode is correctly a failure mode (see the correction above).
  - Its outcome, "Markovian stochastic", holds only in the complete-erasure limit of ch01:215
    ("the record is erased instantly, $\tau_B \to 0$").
  - For a failure of timescale separation short of that limit, ch01:221 and Main:768 give
    suppression of the readback gap under effective mixing and the uniform-erosion hypothesis,
    "suppression, not exclusion" for (C2-structural) and (C4).
  - So the row's outcome needs the uniform-erosion hypothesis, and the complete-erasure limit,
    which the table does not state.

**F6 — the ch01 C3 table row (naming finding withdrawn; outcome gap recorded).**

- *Row.* ch01:253 (FULL:586) reads `| C3 | Capacity hierarchy | No observation | Coextensive with
  system |`. As the correction above says, "Capacity hierarchy" is a failure-mode cell, not a name.
- *The gap.* It has the same kind of gap as the C2 row (F1), for its own condition.
  - The outcomes "No observation" and "Coextensive with system" hold only in the extreme limit of
    ch01:229, "a trivial hidden configuration space, where the visible sector $V$ covers the total
    system $S$".
  - A capacity shortfall short of that limit gives no such outcome. ch01:229 says "A capacity
    shortfall caps the amount of memory that can be represented". The sentence after the table
    says "A hidden-sector capacity shortfall bounds accessible memory", and Main:76 states the
    bound $M_k \leq \log_2|\mathcal{C}_H|$.
  - So the row's outcome needs the zero-capacity limit, which the row does not state.

**F8 — SM Theorem 22's C1 is the coupling-graph form.**

- *Sites.* SM:1376–1378: "every edge of $G_\varphi$ is a dynamical coupling of φ, so any edge in ∂V
  produces non-trivial dynamical coupling". It is mirrored as a status at ch01:61 ("C1 is verified
  structurally") and at SM:52.
- *Canonical text.* Main:72 requires a dependence of a visible conditional, and "A C1 witness
  requires influence on an accessible visible conditional under the specified preparation."
- *How they differ.* The proof gives a boundary edge ($H_{\text{int}}\neq0$ in the graph sense) and
  addresses no preparation.

**F9 — "C2-mixing", an undefined sub-form.**

- *Sites:*
  - Structure:138 ("conditional on C2-mixing");
  - Substratum:24, :195 and :367;
  - ch02:88 (FULL:718);
  - the guard message string at `papers/oi_lattice_code/architecture_check.py:1086`:
    "reconstruction uniqueness is conditional: C2-mixing, M1, and Lemma 24.1's completeness".
- *Canonical text.* Main §1.3 defines only (C2-structural) and (C2-slow). The mixing hypothesis
  is (EM).
- *How they differ.* Substratum Theorem 23 (:193) attaches the mixing hypothesis to slow-bath C2
  only: "The slow-bath form of C2 additionally uses the stated mixing hypothesis". The citations
  attach it to the reconstruction instead. The extra hypothesis errs on the safe side, so this
  is a scope and label mismatch, not an overclaim.

**F10 — the characterization theorem cited without its hypothesis, or under another name.**

- *Canonical text.* Main:546: "Let $\mathcal{S}$ be a time-homogeneous stochastic process …".
- *Sites:*
  - Substratum:112, appendix-b:22 (FULL:5699) and appendix-b:405 (FULL:6082) cite the ⟺
    without the time-homogeneity hypothesis.
  - Substratum:127 attributes it to the "universal hidden-memory theorem" (Main:614), whose
    biconditional is a different one.
- *Not checked.* Whether the proof uses the hypothesis.

**F13 — a stale status surface in a README.**

- *Site.* `verification/README.md:680–681`: "at the cosmological cut C1 verified structurally, C2
  and C3 verified with enormous margins, C4 open".
- *Current text.* GR:46 says the constraint correlations "alone do not establish" C1. GR:48
  takes C2's timescale as a "physical input".
- *History caveat.* The README passage describes the state an earlier audit (Audit B, under
  `verification/audits/physical-realization/concrete-cut/`) repaired the corpus to at
  that time. It is accurate as a record of that repair. It is stale only as a description of the
  current text, because GR §2.2 has since moved.
  - Any correction is forward only: the mutable README's present-tense summary could be updated
    (§A.27).
  - The earlier audit's own records keep their wording. They are not rewritten to agree with the
    later text (§A.42 item 4).

**F14 — Lean `CoreC1C4`: the C2 and C3 clauses are not Main's conditions.**

- *Site.* `verification/lean-mathlib/OIBridge/IndependenceCensus.lean:22–33, 135–200`.
- *C1 and C4: instances.* `core_hidden_drives_visible` and `core_history_readback` are
  deterministic, state-level instances of Main's C1 and C4 on this carrier.
- *C2: confirmed difference.* `core_visible_period_two` is stated as `vis (swapFn (swapFn p)) =
  vis p`, "the visible stream carries a real one-bit memory". This is a consequence about the
  visible stream. It is not Main's C2, the persistence of a *hidden* record to the readback that
  uses it.
- *C3: different formulation.* `core_capacity_saturates` counts visible fibres ("exactly two
  states" per readout). It states no law and no $I^*$.
- *Users of the bundle.* By its definition or by `core_isC1C4`:
  - `OIRealization.lean:235, :254, :303`;
  - `RouteB.lean:85, :383`;
  - `MonoidalCompletion.lean:62, :700`;
  - four further users: `DiagonalTheory.lean:359`, `SubstantiveCensus.lean:398`,
    `SubstratumInterfaceAudit.lean:742` and `PhysicalC4Discharge.lean:148`.
- *Manuscript citations.* No manuscript cites the bundle directly.

**F15 — kernel scope of C3 necessity.** `c3_necessity` (`OIBridge/C3Necessity.lean:80`) is stated
over a realization with a bijective step, where Main:76 says C3 holds "in every faithful
realization". The scope difference is disclosed at Main:626, but not at the kernel citation on
Main:524.

**Different names only (no content difference).**

- Glossary:25 "Coupling" and :29 "Hidden-sector capacity".
- Medicine:27 "Coupling" and :31 "Capacity".
- Structure:114 "Record persistence", and the paper-side glosses that say "record persistence"
  where Main says "memory persistence" (Complexity:27, Methodology:108, Structure:711, GR:617,
  Substratum:127).
- Main:153's gloss "high-capacity hidden sector".
- The lower-case and application names of §3.

## 5. Theorem references checked

| Citation | Cited theorem | Uses the condition as stated? |
|---|---|---|
| Medicine:25, "(C4) holds exactly when … $M_t>0$" | Main:628 Remark (C4 coincides with (ii) in a faithful realization) and Main:614 | Yes, within faithful realizations |
| Substratum:127, :112; appendix-b:22, :405, "⟺ C1/C3/C4" | Main:546 characterization theorem | Hypothesis omitted, and misnamed at Substratum:127 (F10) |
| SM:1376–1384, Theorem 22 | its own proof | C1 in the coupling-graph sense only (F8); C3 floor as in Main:514; C2 and C4 correctly carried as hypotheses |
| Structure:138; Substratum:24, :195, :367; ch02:88, "C2-mixing" | Substratum Theorem 23 (:193) | The mixing hypothesis is attached to slow-bath C2 in the theorem, and to the reconstruction in the citations (F9) |
| Main:76; glossary:29, "C3 in every faithful realization" | Main:514 and `c3_necessity` | Paper: yes. Kernel: bijective only, disclosed at Main:626 (F15) |
| Main:72, C1 follows from C4; Main:636 | Main:628, :636 | Yes |
| `OIRealization.lean`, `RouteB.lean`, `MonoidalCompletion.lean`, "sealed C1–C4 core" | `IndependenceCensus.core_isC1C4` | C1 and C4: instances. C2 and C3: different content (F14) |
| `PhysicalC4Discharge.lean:13–20`, `RoutedReadback` | — | Explicitly "not a new condition", implying the history-level C4. Consistent |

## 6. Comparison with FIN-SCOPE's copy groups

FIN-SCOPE §2.5 lists Main:72–78 as canonical, and the copies and pending openers in its table at
`SPEC.md:480–483`. Re-derivation here confirms each listed site and the ch13:52 mismatch ("conformational timescale
separation"). It does not confirm FIN-SCOPE's ch01:252 and ch01:253 naming mismatches: those cells
sit under the column "What fails" and are not names (§4, correction). It finds the following not
in those groups:

- **The book's own definitions.** ch01:53, :55, :57 and :59 (FULL:386, :388, :390, :392), the
  "Condition C1 (Non-zero coupling)" … "Condition C4 (History readback)" paragraphs. FIN-SCOPE's
  ch01 entries are the table rows :251–253 and the openers at :203, :215 and :229.
- **Structure's string-theory list items.** Structure:530, :532 and :534 (C1–C3), and :536 (C4).
- **ch07:30 / FULL:1895,** "Status of C4 (history readback)". The C4 group lists GR:52, but not
  its book mirror.
- **Parenthetical gloss lists that define the conditions inline.** SM:22, SM:52, GR:20, GR:617,
  Substratum:127, Methodology:108, Complexity:27, Structure:711, ch18:268, :276, :294,
  appendix-b:419 (FULL:6096), book/README:74 and Introduction:85.
- **Other variant names.** The sub-form label "C2-mixing" (five sites, F9) and the gloss "C3
  (high-capacity hidden sector)" at Main:153.
- **The Lean bundle.** `IndependenceCensus.lean`, whose `CoreC1C4` names all four conditions
  (F14), and `C3Necessity.lean`.
- **Status claims the groups do not cover.** "structural conditions C1–C4" (F2, including
  ch09:88), the canonical paper's own Main:326/appendix-b:90 (F2b), and the necessity claims of F3
  (Structure:110, :734; ch18:276, :286).
- **Guard text.** The "C2-mixing" string at `papers/oi_lattice_code/architecture_check.py:1086`
  (F9).

The group sizes in FIN-SCOPE (C1 26–29, C2 26–32, C3 26–30, C4 15–18, mirrors counted) are
therefore lower bounds for the occurrences that define or gloss a condition.

## 7. The #1477 frozen ledger

The ledger was read only, at `55544cc3`:
`verification/audits/foundations/a1exit-deletion-20261121/edits.json`, 373 edits, drafting base
`97070c98`. Nothing in that branch, record or ledger was changed. The `ledger` column of
full scan (`--full`) marks 82 matches on lines that the ledger edits; the kept register carries the
flag on its hand-classified rows.

- **Ledger edits that change C-text.** Two edits change text that itself names a condition:
  - D052, Structure:140: "A1–A6 are not the same as observer-admission C1–C4;" becomes
    "Finiteness and A2–A6 are not the same as observer-admission C1–C4;".
  - D054, Structure:140: "A1 (finiteness) is related to but distinct from C3" becomes
    "finiteness is related to but distinct from C3".

  Neither changes how C1–C4 are named or defined.
- **Findings on ledger lines.** One finding sits on a ledger line: F9 at **ch02:88 / FULL:718**
  ("with M1-T, C2-mixing …"; D116/D117 edit the adjacent "under E1–E7 and A1–A6 with M1-T").
- **Other ledger lines that mention a condition** carry no finding. They are equivalent glosses
  at SM:22 (D032), GR:20 (D039) and Substratum:129 (D020), and inline references at ch03:44
  (D136–D141), ch00:95 (D102/D103), ch01:179 (D108–D111) and the other flagged lines of the
  register.
- **Constraint on any later correction.** A correction to any of these lines would have to wait
  for, or be reconciled with, the #1477 ledger. This audit proposes none.

## 8. Suggested canonical wording (proposal only; not applied, needs owner approval)

These short forms are drawn from Main §1.3 for reuse in glosses, tables and list items. They are
proposals for a later, separately authorized correction round. They are not edits, and they are
meant to carry exactly Main's content.

- **C1 — Non-zero coupling.** "Hidden degrees of freedom affect the visible evolution at some
  accessible step: the conditional law of some visible transition depends on the hidden state,
  under the specified preparation."
- **C2 — Memory persistence.** "A hidden record of visible history persists to the readback that
  uses it (C2-structural). A slow bath, $\tau_S \ll \tau_B$ (C2-slow), is one sufficient mechanism,
  not the condition. C2 is a physical-regime premise, not one of the three structural conditions."
  For tables: "Memory persistence".
- **C3 — Sufficient memory capacity.** "The hidden sector has enough distinguishable states to
  encode the observed conditional past–future information, $\log_2|\mathcal{C}_H| \geq I^*$;
  $N_H \gg N_V$ is a comfortable regime, not the condition."
- **C4 — History readback.** "At some accessible order, two visible histories with the same present
  induce different next-step laws through the hidden state. The condition is operational and does
  not by itself assert a causal write-then-read cycle."
- **Collective.** "the conditions C1–C4 (three structural conditions, C1, C3 and C4, and the
  physical-regime premise C2), diagnostics of a realization".

## 9. Open and out of scope

- No finding has been independently reviewed.
- The 1,553 rule-classified inline references (regenerable with `--full`) were not read one by one. A reference that
  restates a condition without naming it as a definition could carry a difference that this
  audit does not record.
- Whether the characterization theorem needs time-homogeneity (F10), and whether SM Theorem 22
  can be strengthened to the operational C1 (F8), are mathematical questions. This audit does not
  answer them.
- Every correction is out of scope: manuscripts, the glossary, the Lean docstrings and the
  `verification/README.md` status. Each needs separate owner approval and §A.25 propagation, with
  the #1477 ledger constraint of §7 for ch02:88/FULL:718.
