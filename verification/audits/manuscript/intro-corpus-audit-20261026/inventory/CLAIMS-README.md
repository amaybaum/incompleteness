# Claim inventory: `papers/Introduction.md` (audit step 2a)

**Object:** `papers/Introduction.md` at `4a260ca9d6414e4d504a629ba5a0eb3c70bd4704`, sha256
`beb0a5202419a71a8a633f5999f7f48a5e8768a922b7681b7576c470b936feb8` (hash re-checked on extraction). Line numbers in
`claims.json` refer to that blob.

**Content:** 385 claims, `I-001`–`I-385`, in document order. The entries with a `direction` object carry
24 directional sub-claims between them, `I-nnn.a`, `I-nnn.b` and `I-nnn.c`. Every `text` field was checked
mechanically to be a verbatim substring of its line, or of lines `line`–`line_end` for the one multi-line span
(Theorem 1).

This file inventories claims only. Whether a claim is supported is decided in the mapping (`MAPPING.md`) and
recorded in `FINDINGS.md`. The `status_as_stated` field records what the Introduction's wording implies, not what the
corpus establishes.

## Counts

### By section and type

| Section | IDs | Total | theorem-statement | result | negative | status | scope | numerical | attribution | definition-used |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Abstract | I-001–I-021 | 21 | 2 | 5 | 4 | 7 | 1 | 0 | 1 | 1 |
| §1.1 | I-022–I-032 | 11 | 0 | 2 | 1 | 4 | 2 | 0 | 0 | 2 |
| §1.2 | I-033–I-042 | 10 | 0 | 5 | 2 | 0 | 2 | 0 | 1 | 0 |
| §1.2 Contributions | I-043–I-052 | 10 | 0 | 0 | 0 | 4 | 2 | 0 | 4 | 0 |
| §1.2 Conventions | I-053–I-056 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| §2.1 | I-057–I-062 | 6 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 5 |
| §2.2 | I-063–I-081 | 19 | 1 | 4 | 0 | 5 | 2 | 0 | 7 | 0 |
| §2.3 | I-082–I-091 | 10 | 0 | 5 | 3 | 0 | 2 | 0 | 0 | 0 |
| §2.4 | I-092–I-110 | 19 | 7 | 4 | 0 | 5 | 1 | 0 | 0 | 2 |
| §2.5 | I-111–I-124 | 14 | 2 | 5 | 1 | 3 | 0 | 0 | 2 | 1 |
| §3.1 | I-125–I-135 | 11 | 1 | 1 | 4 | 0 | 2 | 0 | 3 | 0 |
| §3.2 | I-136–I-146 | 11 | 1 | 3 | 1 | 3 | 1 | 0 | 0 | 2 |
| §3.3 | I-147–I-158 | 12 | 0 | 8 | 2 | 1 | 0 | 0 | 0 | 1 |
| §3.4 | I-159–I-166 | 8 | 0 | 2 | 2 | 1 | 1 | 0 | 2 | 0 |
| §3.5 | I-167–I-171 | 5 | 0 | 2 | 0 | 2 | 1 | 0 | 0 | 0 |
| §4 | I-172–I-205 | 34 | 0 | 5 | 4 | 9 | 7 | 2 | 7 | 0 |
| §5 | I-206–I-245 | 40 | 1 | 6 | 6 | 12 | 7 | 4 | 3 | 1 |
| §6.1 | I-246–I-251 | 6 | 0 | 3 | 2 | 1 | 0 | 0 | 0 | 0 |
| §6.2 | I-252–I-280 | 29 | 0 | 5 | 12 | 5 | 6 | 0 | 1 | 0 |
| §6.3 | I-281–I-295 | 15 | 0 | 0 | 1 | 14 | 0 | 0 | 0 | 0 |
| §6.4 | I-296–I-307 | 12 | 2 | 3 | 3 | 3 | 1 | 0 | 0 | 0 |
| Code, data and formal verification | I-308–I-312 | 5 | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 0 |
| Appendix A | I-313–I-344 | 32 | 0 | 0 | 0 | 32 | 0 | 0 | 0 | 0 |
| Appendix B.1 | I-345–I-354 | 10 | 0 | 2 | 0 | 0 | 0 | 7 | 0 | 1 |
| Appendix B.2 | I-355–I-359 | 5 | 0 | 1 | 0 | 0 | 0 | 2 | 2 | 0 |
| Appendix B.3 | I-360–I-383 | 24 | 0 | 12 | 2 | 0 | 1 | 7 | 1 | 1 |
| References | I-384–I-385 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| **Total** | | **385** | **17** | **83** | **50** | **117** | **41** | **22** | **34** | **21** |

### By stated status level

| Level | Entries |
|---|--:|
| proved-kernel | 56 |
| proved-paper | 25 |
| conditional | 15 |
| calibration | 4 |
| numerical | 13 |
| conjecture | 11 |
| open | 47 |
| unstated | 214 |

`unstated` is the largest group because restatements, attributions and Appendix B arithmetic usually carry no status
word at the point where they are made.

### Equivalences and directional claims (§A.34)

- I-002 (line 12): set-equality (three classes; each inclusion is one direction); sub-claims I-002.a, I-002.b, I-002.c
- I-011 (line 12): equivalence (characterization); sub-claims I-011.a, I-011.b
- I-063 (line 48): set-equality (three classes; each inclusion is one direction); sub-claims I-063.a, I-063.b, I-063.c
- I-100 (line 82): equivalence ('exactly when'); sub-claims I-100.a, I-100.b
- I-105 (line 86): equivalence ('coincides with'); sub-claims I-105.a, I-105.b
- I-132 (line 106): equivalence (literature); sub-claims I-132.a, I-132.b
- I-139 (line 116): equivalence (iff); sub-claims I-139.a, I-139.b
- I-153 (line 126): converse pair presented with the preceding entry ('conversely'); sub-claims I-153.a, I-153.b
- I-296 (line 189): equivalence ('exactly'); sub-claims I-296.a, I-296.b
- I-297 (line 189): equivalence ('exactly'); sub-claims I-297.a, I-297.b
- I-336 (line 214): equivalence (iff declaration); sub-claims I-336.a, I-336.b

## Schema

| Field | Content |
|---|---|
| `id` | `I-001`… in document order (line, then character offset). |
| `section` | Abstract, `§1.1`…`§6.4`, `§1.2 Contributions`, `§1.2 Conventions`, Code/data, Appendix A, B.1–B.3, References. |
| `line` (`line_end`) | Line number at `4a260ca9`. `line_end` is present only for the multi-line Theorem 1 span. |
| `text` | A verbatim span. |
| `claim` | A one-line normalized statement. |
| `type` | One of theorem-statement, result, negative, status, scope, numerical, attribution or definition-used. |
| `status_as_stated` | An object with `level` (proved-kernel, proved-paper, conditional, calibration, numerical, conjecture, open or unstated), `hypotheses` (those named in the text) and an optional `note`. |
| `cited` | The citations given at that point: bracket citations verbatim, Lean identifiers in backticks, `Appendix A: …` where only Appendix A names the declaration. A citation marked `(sentence-final)` stands at the end of the sentence, and its coverage of this clause is inferred. |
| `direction` | `null`, or `{kind, sub_claims[]}` with one sub-claim per direction or inclusion. Each sub-claim has an `id`, `label`, `claim`, `status_as_stated` and `cited`. |
| `attention` | Optional. Ambiguities and checks for the owner or the mapper. Not a finding. |

## Extraction rules applied

1. **Atomicity.** Each entry asserts one proposition. Sentences joined by "and", ";" or ":" are split when the parts
   are separately checkable. Example: line 28's provenance, proof status and novelty of the black-hole results are
   three entries. One clause asserting two propositions about one span keeps the same `text` in two entries, as in
   I-107/I-108, "(C1) and (C3) follow from it".
2. **Every occurrence.** A claim restated in the abstract, the body, §6.2's list and §6.4's conclusion is entered at
   each site, because the audit checks every site (AGENTS.md §A.25). A restatement keeps its own wording's status.
   The abstract's Theorem 1 (I-002) is `unstated`, while the body's (I-063) is `proved-kernel`.
3. **Status attachment.** A status parenthetical that qualifies one claim goes into that claim's
   `status_as_stated`. Examples: "(proved on paper, with exact probes)" on line 84, and "it is proved on paper" on
   line 56. A status sentence or clause that stands alone, or governs several claims, gets its own `status` entry.
   Examples: "Theorem 1 is machine-checked as …", "(each with one step not machine-checked)" in the abstract, and
   "the factorization is proved, and the unboundedness is imported".
4. **Level from wording**, weakest link first:
   - "machine-checked" → proved-kernel;
   - "proved on paper", "written proof" or a bare "proved" → proved-paper;
   - "conditional on", "holds under", "needs" or "if …" → conditional;
   - "enters as an input" or "dimensional identity" → calibration;
   - "finite/exhaustive computations" or "exact enumeration" → numerical;
   - "proposal", "posited", "hypothesis" or "conjectural" → conjecture;
   - "open", "not established", "not derived", "not computed" or "not resolved" → open;
   - no status word → unstated.

   Where the text says a result is machine-checked except for a named step, the level is proved-paper and the
   `note` records the split. Examples: Theorem 2, the Corollary and the abstract's two memory/recurrence results.
   §3.2's qubit-independence sentences have no status word in the body, so they take Appendix A's machine-checked
   status, and the note says so.
5. **Definitions.** A definition is included as `definition-used` only when it is attributed to a corpus or
   literature source, or when a stated result depends on it matching the corpus. Examples: the classes S_K, D_K and
   Q_K, (C1)–(C4), Theorem 4's standing structure and conditions, faithful realization, substratum, rooted
   P-divisibility, and the B.1 and card-game models. Pure notation is excluded.
6. **Headings** are included only where they assert something: §3.3 (I-147) and §3.4 (I-159).
7. **Appendix A.** Each declaration is one `status` entry carrying its identifier and module:line, plus the "proved
   on paper" exceptions in the table. The mapping of Theorem 2's four declarations to parts (a)–(c) is not stated in
   the paper. The `claim` text gives a presumed assignment and flags it.
8. **Appendix B.** Every displayed number, matrix entry and table row is a `numerical` entry. Each inference drawn
   from the numbers ("so the family is P-indivisible") is a `result`.
9. **Literature.** Every scientific attribution is an `attribution` entry, with the locator as given. The rendered
   text alone determines `cited`. The HTML comments in the reference list ("Read first-hand …", "VERIFY …") are not
   rendered and are not claims, but entries citing [Har04] and [Sha79] note their VERIFY comments.
10. **Equivalence markers.** A `direction` object is attached to:
    - "iff", "exactly when", "coincides with", "is characterized by" and "is equivalent to";
    - the set equality S_K = D_K = Q_K, as three cyclic inclusions;
    - §6.4's "exactly" restatements;
    - line 126's "conversely" pair;
    - Appendix A's `exactAll_iff_physical_general`.

    Directions are labelled as the text presents them. Proof-dependency remarks, such as "the forward direction rests
    on Theorem 2(a) in each realization", are recorded in the sub-claim's `note`, not as separate entries.

## Borderline items excluded

These were read and left out. Reviewers checking completeness should start here.

| Line | Text (abridged) | Reason |
|---|---|---|
| 1 | Title "…From Deterministic Dynamics to Quantum Observations" | A title, not an assertion. The body's scope claims cover it. |
| 5–6 | "DRAFT PRE-PRINT", classification | Document metadata. |
| 12 | "it is stated here as one theorem" | Expository self-description. The checkable part is I-048, "each direction attributed". |
| 26 | "The paper develops one idea, OI: …" (except the clause in I-040), "§6 states what would decide each", "gravitational applications are in [GR] and [Book]" | Signposting and pointers. The provenance sentence "Proofs … are in [Main]" is kept as I-042 because it is checkable and looks too broad. |
| 28 | "It presents the established mathematical results of OI together, separates … and states two consequences …" | Expository self-description. The novelty disclaimer is kept as I-043. |
| 30 | "'proved on paper' means a written proof without a machine check" | Status vocabulary that asserts nothing. "Machine-checked" (I-053) and "exact probe" (I-054) are kept because they carry a commit and a testable standard. |
| 36 | Setting: finite C_V with \|C_V\| ≥ 2, C_H, φ, horizon K, "A law is a probability distribution …" | Definitions. \|C_V\| ≥ 2 is recorded as a hypothesis of I-063 (Theorem 1). Theorem 1 says "every finite visible alphabet", so the mapper should note the \|C_V\| ≥ 2 restriction. |
| 40 | "Three classes of law are compared [Main §3.4]" | A signpost. Its citation is carried into the S_K/D_K/Q_K entries. |
| 72 | Notation f_x, π_V, μ_p | Notation. M_t is kept (I-092). |
| 82 | "The forward direction rests on … the converse on …" | Proof structure, recorded in I-100's direction sub-claims. |
| 90 | "Write Γ_t for the *rooted* visible transition matrix …" | Notation, folded into I-111. |
| 98 | "memory without short-window indivisibility" (as an Appendix B signpost) | Covered by the §3.1 claim I-126 and by B.2. |
| 124 | "unitary dilations that reproduce the visible law at every time and compose exactly across times" | The definition of coherent lift, folded into I-149. |
| 160 | "Let U be the set of joint values … and M the message set" | Notation. |
| 197–200 | MIT License, repository paths, concept DOI, release-archive membership | Not scientific. |
| 204 | "Modules of the `OIBridge` Lean library; line numbers at commit `17b830bc`" | A table header. Module and line are recorded per declaration. |
| 219 | Heading "B.1 A minimal model" | Its minimality claim is entered once, at line 98 (I-123). |
| 232 | "Let X_0 and X_1 be independent uniform bits and X_2 = X_0 ⊕ X_1" | Example setup. No corpus attribution. |
| 238 | "obtained by exact enumeration of the equally likely cases" | Recorded as the status note on the four table rows. |
| 261 | [Main] title "…The Equivalence of Quantum Mechanics and Embedded Observation" | Bibliographic. The title asserts an equivalence that the Introduction itself denies (I-145, I-252). Raised for the owner below. |
| 263 | [GR] title "ℏ, the Bekenstein-Hawking Entropy, and the Running-Vacuum Form of Dark Energy from the Cosmological Horizon" | Bibliographic. It names derivations the Introduction does not use or claim. |
| 281–341 | HTML comments in references ("SUPPORTED", "VERIFY: content not read") | Not rendered. They are audit provenance, not manuscript claims. The reviewer should note that [CT06], [Har04] and [Sha79] carry VERIFY comments, meaning their content has not been read. |
| headings | §1, §2, §3, §4, §5, §6 and subsection titles other than §3.3 and §3.4 | Signposting. |

## Items needing the owner's or the mapper's attention (35)

These are ambiguities in what the Introduction asserts. They are not findings yet; the mapper decides each.

- **I-008** (line 12): Abstract says 'every deterministic completion carries the visible memory'; body (Theorem 2, Corollary) says readout-relevant hidden memory exists in every faithful realization exactly when M_t>0. Mapper: confirm 'deterministic completion' = 'faithful realization' and that the claim is conditional on M_t>0.
- **I-010** (line 12): 'one step' is unspecified. For Theorem 2 the body names two unchecked ingredients (time-t identification and the CMI vanishing criterion, line 82); for readback the unchecked step is history-level (C4). Mapper: check that 'one step' is accurate for each.
- **I-025** (line 20): Stated universally; it holds only when f_x is non-constant on the support of the hidden posterior. Mapper: read as 'can send'.
- **I-034** (line 26): 'produces' read as 'can produce' for memory and divisibility failure (not every marginal has them).
- **I-042** (line 26): Theorem 4 and §3.2 are cited to [GR §3.3]; §5's results to [BHa; BHb] and [GR App. A]; line 28 says §3.2–§3.3 results are proved in [GR] and [Main]. 'Proofs ... are in [Main]' is broader than the citations support.
- **I-048** (line 28): Check that every inclusion has a literature attribution: Q_K ⊆ S_K is attributed only as 'the Born rule' (line 58) and [SGD19] (line 60).
- **I-052** (line 28): The §3.2–§3.3 kernel declarations are OIBridge modules; check that [GR]/[Main] actually carry these results (especially §3.3's coherent-lift results and the qubit independence).
- **I-054** (line 30): Mapper: each 'with exact probes' claim (lines 56, 84) must be backed by probes that are exhaustive and exact-rational, per this definition.
- **I-056** (line 30): Corpus usage of 'substratum' (e.g. AGENTS.md: bijection on a cubic lattice with coupling matrix) is more specific; check consistency with Main/GR.
- **I-100** (line 82): Mapper: confirm Main §1.5 is the Corollary's location (Theorem 2 is cited to Main §3.4).
- **I-102** (line 84): 'conditional past–future information' is not defined in the Introduction (M_t? I(X_{<t};X_{>t}|X_t)?), and 'in the same form as Theorem 2' leaves the checked statement implicit. Mapper: pin down the quantity and the checked form.
- **I-105** (line 86): (C4) as defined on line 86 is a property of the visible law, so 'in a faithful realization' is idle here; line 96 also uses a realization clause ('routed readback'). Mapper: check which (C4) Main §1.3 defines and at which t.
- **I-109** (line 86): §6.3 item (4) lists '(C2) necessity' as open and conditional on a mixing hypothesis; check the two statements agree with Main.
- **I-111** (line 90): This is a rooted (from time 0) divisibility; [RHP14]/[BD16] criteria are for two-time divisibility. Mapper: check the attribution on line 90 applies to the rooted form.
- **I-114** (line 92): 'fixed hidden prior' is ambiguous (fixed in time? independent of x_0?). Mapper: match against the Lean hypothesis.
- **I-123** (line 98): 'minimal model' (6 hidden states) sits beside 'the smallest realization of Theorem 3' (the card game, 2 hidden values). The sense of 'minimal' is unstated.
- **I-124** (line 98): Minimality claim with no proof or citation and no stated measure of size; check Main/Book.
- **I-139** (line 116): Line 114 says 'at every ancilla level'; Theorem 4 says 'at every positive ancilla level'. Mapper: check which the Lean statement uses.
- **I-140** (line 118): Appendix A places physical_of_exactAll in PhysicalCharacterization, not GeneralCarrier; check it holds 'for every nonempty finite carrier' as line 118 states.
- **I-146** (line 120): Implicitly treats (i) and (ii) as supplied or not at issue; the Introduction gives no statement or citation for that.
- **I-153** (line 126): §A.34: the 'converse' has a different middle term (rooted families vs root-conditioned trajectory laws at every horizon), so the two cited results do not form an iff unless the mapper shows the two notions coincide. Also only the forward direction of an iff declaration is cited.
- **I-154** (line 126): The declaration name suggests stochasticity only; check it also establishes fixed-basis realizability.
- **I-159** (line 128): Heading is broader than the body ('the full prepare-and-measure theory of a qubit exactly'); 'carrier' is also used for Theorem 4's system ('every nonempty finite carrier', line 118).
- **I-218** (line 160): Derivation needs the blind-guess baseline 1/|M| (uniform message prior); the prior is not stated in the Introduction.
- **I-219** (line 160): Population counted (maps {0,1}²→{0,1}²? which register unread?) is unspecified.
- **I-220** (line 160): Ambiguous: sufficient/necessary for what (recovery? the bound?) is not stated.
- **I-227** (line 162): Universal 'for every bijection' claim attributed to an unpublished record; check whether BHb C1 proves it or checks it finitely.
- **I-267** (line 175): Cites GR Thm A.7, while the Page-value result is cited as GR Thms A.8–A.9 (line 162). Mapper: identify GR Thm A.7 (decoupling?) and confirm the intended theorem.
- **I-299** (line 189): Repeats the abstract's 'every deterministic completion' claim (I-008); in the body the hidden memory is readout-relevant exactly when M_t>0.
- **I-308** (line 195): Mapper: confirm toolchain versions (lean-toolchain, lake manifest) at 17b830bc.
- **I-311** (line 195): 'exactly these three' is stronger than 'within'; check every declaration's report, including small lemmas that may use fewer.
- **I-320** (line 209): Appendix A does not say which declaration proves which part of Theorem 2; mapper to assign.
- **I-336** (line 214): The body (line 118) names only the two directional declarations; Appendix A adds the iff declaration. Mapper: check the iff is assembled from these two directions.
- **I-345** (line 221): B.1 is cited to [Main §2.4] while Theorem 3 is cited to [Main §2.3]; check the model's location in Main.
- **I-383** (line 255): 'A card arrangement' read as 'any card arrangement'.

Also for the owner:
- **[Main]'s title** asserts "the Equivalence of Quantum Mechanics and Embedded Observation". The Introduction states
  that OI alone does not imply quantum mechanics (I-145) and claims no derivation of it (I-252). The two sit in the
  same paper's reference list.
