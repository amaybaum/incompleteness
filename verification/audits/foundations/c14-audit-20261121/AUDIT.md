# C14-AUDIT — wording of the foundational conditions C1–C4 across the corpus

**Status: WIP / UNVERIFIED.** Not independently reviewed. Read-only with respect to the manuscripts:
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
per match to `register.tsv`: file, line, column, condition, class, a #1477-ledger flag, the chapter
source of each `FULL.md` row, a note, and an exact excerpt of the line around the match.
`python3 -I verification/audits/foundations/c14-audit-20261121/build_register.py --check` regenerates
the register and fails on any drift.

- **Counts.** 2,194 matches. Of these, 1,580 are inline references, 101 are unrelated labels, and
  513 carry a reviewed class.
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

The canonical definitions are clear. They are `papers/Main.md` §1.3: `:72` **(C1) Non-zero coupling**,
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
| C1 | Non-zero coupling | **Coupling**: glossary:25, Medicine:27, Structure:112, ch01:251 table. *coupling*: GR/ch07:24, ch09:112, ch12:42, ch15:59, ch16:196, ch18:67, Complexity:364, Structure:530. *non-trivial coupling*: GR:617, Substratum:127, SM:52, Main:153, ch18:294. *catalytic-conformational coupling*: ch13:50. *coupling, realized as catalytic feedback*: ch11:152. Application names: ch11:66, book/README:74. |
| C2 | Memory persistence | **Record persistence**: Structure:114, Complexity:27, Structure:711, Methodology:108, GR:617, Substratum:127. **Timescale separation**: ch01:252 table. **conformational timescale separation**: ch13:52. *persistence*: ch11:154. *template persistence*: ch11:66. Undefined sub-form **C2-mixing**: Structure:138, Substratum:24, :195, :367, ch02:88. |
| C3 | Sufficient memory capacity | **Hidden-sector capacity**: glossary:29. **Capacity**: Medicine:31. **Capacity hierarchy**: ch01:253 table. *Sufficient capacity*: Structure:116, ch07:28, ch09:116, ch12:46. *capacity*: ch11:156, ch15:63, ch16:210, ch18:69, Complexity:368. *conformational landscape capacity*: ch13:54. *high-capacity hidden sector*: Main:153. *sequence capacity*: ch11:66. |
| C4 | History readback | Uniform everywhere ("history readback"), apart from the application name *template-directed readback* at book/README:74. |

Book `ch*` lines are mirrored at the `FULL.md` lines in `register.tsv` (for example ch01:252 is
FULL:585, and ch13:52 is FULL:3473).

## 4. Inconsistencies, ranked by whether they could change scientific meaning

**Ranking.** *High*: the occurrence states or implies a status or content stronger than the
canonical text, or contradicts a typing that Main calls load-bearing. *Medium*: the content differs
in a way a reader could act on, or a theorem citation leaves out or misplaces a hypothesis.
*Low*: a different name with the same content, or a scope or attribution slip that does not change
what is claimed.

### High

**F2 — "structural conditions C1–C4" against Main's typing of C2 as not structural.**

- *Canonical text.* Main:74 says "a physical-regime premise, not a structural condition — and the
  distinction is load-bearing. C1, C3 and C4 are the structural conditions". Main:636 says "Of the
  three structural conditions", and the glossary agrees at :29: "the framework's three structural
  conditions (C1, C3, C4)".
- *Sites that call all four structural:*
  - GR:617: "[Main]'s structural conditions C1 (non-trivial coupling), C2 (record persistence — …)".
  - Structure:528: "The structural conditions for observer admission [Main §3]".
  - Structure:711: "the framework's structural conditions C1–C4".
  - appendix-c:172 (FULL:6327): "the C1–C4 structural conditions".
  - appendix-c:291 (FULL:6446): "C1–C4 structural conditions operating at different scales".
  - ch11:10 (FULL:2973): "the framework's structural conditions C1, C2, C3, C4".
  - ch14:107 (FULL:3707): "The framework's structural conditions C1–C4".
  - ch18:24 (FULL:4755) and ch18:296 (FULL:5027): "necessary structural conditions".
- *How they differ.* All of these type C2 as structural, which Main explicitly denies and calls
  load-bearing. This is a status-classification mismatch in the sense of §A.25.

**F3 — "necessary for an embedded observer to exist".**

- *Site.* Structure:110, introducing the (C1)–(C4) list at :112–118: "four conditions on a
  substratum's bijection $\varphi$ that are necessary for an embedded observer to exist [Main §3]".
- *Canonical text.*
  - Main:70: "diagnostics of a realization rather than hypotheses of the characterization … (C2)
    is a physical-regime premise".
  - Main:546: C2 "is not needed for the equivalence".
  - SM:52: "conditions on the partition, not on the lattice".
- *Similar claims.* ch18:24 and ch18:296 call "the C1–C4 architecture" the "necessary structural
  conditions" for conscious information processing.
- *How they differ.* Main proves C1 and C3 necessary only as consequences inside the memory-bearing
  sector (from C4, or from observed non-Markovianity). It proves no necessity for an observer's
  existence. It treats C2-slow as one sufficient mechanism, not a necessary one: the fast
  shift-register bath at Main:74 has C4 while C2-slow fails. Structure:110 also locates the
  conditions on $\varphi$, where Main and SM locate them on the partition and its realization.
  This is a necessary-versus-diagnostic overstatement.

**F5 — C4 stated as a causal write-then-read.**

- *Site.* Structure:118: "(C4) **History readback.** The interaction must read back what was
  written — the load-bearing memory condition."
- *Canonical text.* Main:78: "The condition is operational; it does not by itself assert a causal
  write-then-read cycle — a pre-sampled hidden variable revealed by the history satisfies it."
- *How they differ.* The Structure wording requires a written record to be read back. That is the
  cosmological *realization* clause, which Main:78 lists as still "to be demonstrated", not the
  condition. It makes C4 strictly stronger, and it excludes witnesses that Main admits (the
  response-table construction, and Medicine:88's $(v,h)\mapsto(v\oplus h,h)$).
- *Lower-risk relatives.*
  - Introduction:85, "feed the record back into what is seen", a non-technical gloss.
  - ch09:116, "the correlations the read-write cycle generates".
  - SM:1376, "the record surviving to a readback the coupling performs". This one is an explicit
    hypothesis of Theorem 22, so it strengthens an assumption and not a conclusion.

### Medium

**F1 — C2 named or stated by its slow-bath mechanism.**

- *Canonical text.* Main:74: (C2-slow) "implies (C2-structural) … but not conversely: what is
  required is that records persist, not that the hidden sector evolve slowly".
- *Sites:*
  - ch01:252 (FULL:585), table row: `| C2 | Timescale separation | Markovian stochastic |
    Thermalized observer |`. The prose of the same chapter, ch01:55, uses "Memory persistence"
    and states C2 as persistence until readback.
  - ch13:52 (FULL:3473): "**C2: conformational timescale separation.**" The paragraph is about
    $\tau_S/\tau_B$ only.
  - ch18:68 (FULL:4799): "C2 (memory persistence): the hidden sector must retain a record of the
    subsystem's past across the accessible window, $\tau_B \gg \tau_S$ with $\tau_B$ the
    coarse-grained mixing time — slow hidden dynamics is one sufficient mechanism, not the
    condition itself".
- *How they differ.* ch01:252 and ch13:52 name the condition by the sufficient mechanism, which
  Main says is not the condition. ch18:68 states the condition as the C2-slow inequality and then
  denies that slow dynamics is the condition, so the item asserts and disclaims the same reading.
- *Previously found.* FIN-SCOPE found ch01:252 and ch13:52. ch18:68 is new here.

**F4 — C1 as "substantial" coupling.**

- *Sites.*
  - Structure:112: "(C1) **Coupling.** The interaction between the observer's degrees of freedom
    and the rest must be substantial."
  - Structure:530: "requires substantial coupling between visible-sector and hidden-sector
    dynamics".
- *Canonical text.* Main:72: "$H_{\text{int}} \neq 0$: hidden degrees of freedom affect the visible
  evolution at some accessible step — the conditional law of some visible transition depends on
  the hidden state."
- *How they differ.* "Substantial" is a magnitude requirement that Main does not impose: non-zero
  influence at one accessible step suffices. It also drops the accessible-conditional criterion.
- *Related application sites.*
  - ch13:50 says "C1 is satisfied with substantial coupling strength". It asserts satisfaction from
    the coupling mechanisms, without the accessible-conditional witness that Main:72 and ch01:53
    require ("Establishing C1 there requires showing that hidden variation affects an accessible
    visible conditional under a specified preparation").
  - ch11:152 makes C1 require two-way feedback: "the template must direct synthesis … and the
    synthesis must maintain the template". Main's C1 is one-way hidden-to-visible influence, and
    Medicine:88 says explicitly that C1 "does not require the visible sector to act back on the
    hidden state". Recorded as F12.

**F7 — C3 as storing "the interaction history".**

- *Sites.*
  - Structure:116: "(C3) **Sufficient capacity.** The hidden sector must have information capacity
    enough to store the interaction history."
  - Structure:534: "sufficient information capacity to store the interaction history".
- *Canonical text.* Main:76: "enough distinguishable states to encode the observed conditional
  past–future information: $\log_2 |\mathcal{C}_H| \geq I^*$".
- *How they differ.* The interaction history is in general far larger than $I^*$. Main:522 also
  denies the cumulative reading: "$m \gtrsim 2^{K I_0}$" needs "the additional hypothesis that
  the per-event contributions accumulate without hidden-state reuse or compression". The Structure
  wording is therefore a stronger and different requirement.

**F8 — SM Theorem 22's C1 is the coupling-graph form.**

- *Sites.* SM:1376–1378: "*Proof.* C1: $G_\varphi$ is connected and V is a proper subgraph, so
  ∂V ≠ ∅; every edge of $G_\varphi$ is a dynamical coupling of φ, so any edge in ∂V produces
  non-trivial dynamical coupling." The theorem is mirrored as a status at ch01:61 ("C1 is
  verified structurally under the stated update and cut") and at SM:52.
- *Canonical text.* Main:72 requires "the conditional law of some visible transition depends on
  the hidden state" and adds "A C1 witness requires influence on an accessible visible conditional
  under the specified preparation."
- *How they differ.* The proof establishes a boundary edge, which is $H_{\text{int}}\neq 0$ in the
  graph sense. It says nothing about a preparation: under a preparation that fixes the hidden
  boundary state, no visible conditional depends on it.
- *Classification.* Theorem reference. The theorem uses C1 in its structural ($H_{\text{int}}\neq
  0$) clause, not in its full operational clause. The wording "C1 verified structurally" is
  accurate only if "structurally" is read that way.

**F9 — "C2-mixing", an undefined sub-form.**

- *Sites.*
  - Structure:138: "conditional on C2-mixing".
  - Substratum:24: "M1-T; C2-mixing; the Stage-2 structural inputs".
  - Substratum:195: "the C2-mixing condition".
  - Substratum:367: "together with M1-T, C2-mixing and the nearest-neighbor premise".
  - ch02:88 (FULL:718): "with M1-T, C2-mixing and the nearest-neighbor restriction".
- *Canonical text.* Main §1.3 defines only (C2-structural) and (C2-slow). The mixing hypothesis is
  (EM) (Main:161, §4.6) or "the hidden-sector mixing hypothesis".
- *Theorem reference.* Substratum Theorem 23 (:193) does not list C2-mixing among its hypotheses.
  It says "The slow-bath form of C2 additionally uses the stated mixing hypothesis." The five
  sites list it as a condition of the reconstruction of the "local (propagating) lattice/gauge
  residue".
- *How they differ.* An extra hypothesis makes the cited statement weaker, not stronger, so this
  is the safe direction. The citation and the theorem still disagree, and the label has no
  definition.

**F14 — Lean `CoreC1C4`: the C2 and C3 clauses are surrogates with different content.**

- *Site.* `verification/lean-mathlib/OIBridge/IndependenceCensus.lean:22–33, 135–200`. The bundle
  is described as "All four OI conditions are kernel-named, and bundled as `CoreC1C4`".
- *C1 and C4: equivalent instances.* `core_hidden_drives_visible` (two states with the same
  visible readout and different next visible readouts) and `core_history_readback` (two states
  with the same present carrying the histories `0 → 0 → 0` and `1 → 0 → 1`) are deterministic,
  state-level instances of Main's C1 and C4 on this carrier.
- *C2: different formulation.* `core_visible_period_two` is "`v_{t+2} = v_t` … the visible stream
  carries a real one-bit memory". That is a property of the visible stream. Main's C2 is
  persistence of a *hidden* record to its readback.
- *C3: different formulation.* `core_capacity_saturates` counts visible fibres ("exactly two
  states" per readout). It states no law and no $I^*$, so it is not $\log_2|\mathcal{C}_H| \geq
  I^*$. The bound is recovered informally in the docstring.
- *Downstream.* `OIRealization.lean:48`, `RouteB.lean:85` and `MonoidalCompletion.lean:452` refer
  to the "sealed C1–C4 core" by this bundle. No manuscript cites `CoreC1C4` or `core_isC1C4`
  directly.
- *Risk.* A reader of "the core satisfies C1–C4" receives Lean's C2 and C3, not Main's.

### Low

**F6 — C3 named "Capacity hierarchy".**

- *Site.* ch01:253 (FULL:586): `| C3 | Capacity hierarchy | No observation | Coextensive with system |`.
- *Canonical text.* Main:76 says "Sufficient memory capacity". Main:522 adds that "the necessity
  content of (C3) is the capacity to hold the observed conditional memory, not a bound set by
  $n$". ch18:69 and the glossary at :29 add that "$N_H \gg N_V$ is the comfortable physical
  regime, not the condition".
- *How they differ.* "Hierarchy" names the $N_H \gg N_V$ regime. The limit model that this row
  summarizes (ch01:229, zero hidden capacity) is stated correctly.
- *Related.* Complexity:368 compares the hidden state space with the visible one. That is an
  application, not a definition.

**F10 — the characterization theorem cited without its hypothesis, or under another name.**

- *Canonical text.* Main:546: "*Let $\mathcal{S}$ be a time-homogeneous stochastic process on a
  finite configuration space … Then (ii) $\iff$ (iii)*", with (iii) listing C1, C3 and C4 (Main:552).
- *Sites that cite it without "time-homogeneous":*
  - Substratum:112: "accessible non-Markovianity … ⟺ C1/C3/C4 per finite accessible horizon".
  - appendix-b:22 (FULL:5699) and appendix-b:405 (FULL:6082): "accessible non-Markovianity ⟺
    C1/C3/C4 realization per accessible horizon".
- *Misattribution.* Substratum:127 attributes the ⟺ to "[Main §3.4]'s universal hidden-memory
  theorem". That theorem (Main:614, *unavoidable hidden predictive memory*) states (a)–(c), and
  its Remark gives a different biconditional, $M_t>0$ iff every faithful realization carries
  readout-relevant hidden memory.
- *Not checked here.* Whether the time-homogeneity hypothesis is used in the proof. By the review
  rule *conditional → unconditional*, a citation should either carry the hypothesis or the
  theorem should drop it.

**F11 — ch09 announces C1–C4 and lists three.** ch09:84 (FULL:2499) says "C1–C4 specify the admission
criterion". The list at :112–116 has C1–C3 and no C4 entry. :118 then says "These conditions
specify the observer-admission criterion".

**F12 — application paragraphs asserting more than the condition requires.** ch11:152 (two-way
feedback) and ch13:50 ("C1 is satisfied with substantial coupling strength"), both quoted under F4.

**F13 — a stale status surface in a README.**

- *Site.* `verification/README.md:680–681`, recording an earlier audit's repair: "at the
  cosmological cut C1 verified structurally, C2 and C3 verified with enormous margins, C4 open".
- *Current text.*
  - GR:46: "C1 requires hidden-to-visible influence on an accessible conditional [Main §1.3],
    which the constraint correlations alone do not establish".
  - GR:48: the C2 timescale is a "physical input", applied "under that assumption".
  - ch07:24–28 (FULL:1889–1893) agree with GR.
- *How they differ.* The README is not a manuscript, but it is a status surface that now
  contradicts the papers on C1 and C2.

**F15 — kernel scope of C3 necessity.**

- *The scope gap.* Main:76 and the glossary at :29 say C3 "holds in every faithful realization".
  The kernel theorem `c3_necessity` (`OIBridge/C3Necessity.lean:80`) is stated over `Realization`,
  whose step is an `Equiv`, so it covers bijective realizations only.
- *Where it is disclosed.* Main:626 says so ("stated there for bijective realizations; the same
  data-processing step for non-injective and staged completions is proved on paper").
- *Where it is not.* The kernel citation at Main:524 does not.
- This is a disclosed scope difference between layers, not an error.

**Different names only (no content difference).** Glossary:25 "Coupling" and :29 "Hidden-sector
capacity"; Medicine:27 "Coupling" and :31 "Capacity"; Structure:114 "Record persistence"; and the
lower-case and application names of §3. The paper-side gloss lists use "record persistence"
(Complexity:27, Methodology:108, Structure:711, GR:617, Substratum:127) where Main says "memory
persistence". Main itself glosses C3 as "high-capacity hidden sector" at :153.

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
`SPEC.md:480–483`. Re-derivation here confirms each listed site, and its two content mismatches
(ch01:252 "Timescale separation", ch13:52 "conformational timescale separation") and ch01:253
"Capacity hierarchy". It finds the following not in those groups:

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
- **Status claims the groups do not cover.** "structural conditions C1–C4" (F2) and "necessary
  for an embedded observer to exist" (F3).

The group sizes in FIN-SCOPE (C1 26–29, C2 26–32, C3 26–30, C4 15–18, mirrors counted) are
therefore lower bounds for the occurrences that define or gloss a condition.

## 7. The #1477 frozen ledger

The ledger was read only, at `55544cc3`:
`verification/audits/foundations/a1exit-deletion-20261121/edits.json`, 373 edits, drafting base
`97070c98`. Nothing in that branch, record or ledger was changed. The `ledger` column of
`register.tsv` marks 82 matches on lines that the ledger edits.

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
- The 1,580 rule-classified inline references were not read one by one. A reference that
  restates a condition without naming it as a definition could carry a difference that this
  audit does not record.
- Whether the characterization theorem needs time-homogeneity (F10), and whether SM Theorem 22
  can be strengthened to the operational C1 (F8), are mathematical questions. This audit does not
  answer them.
- Every correction is out of scope: manuscripts, the glossary, the Lean docstrings and the
  `verification/README.md` status. Each needs separate owner approval and §A.25 propagation, with
  the #1477 ledger constraint of §7 for ch02:88/FULL:718.
