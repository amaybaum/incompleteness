# Reading: "the six structural properties" at papers/SM.md:1394 (H = 53c6601a)

Independent reader, read-only. Did not read SP/coord2-a1-amend/ or SP/coord2-q10/.
H = 53c6601a10419b6b333cc992474272501ab542af. P = 4c79be642ca631573f06b444903be75ec4f5e2b6 (ledger only).

## 1. The sentence and its context (SM.md at H)

§8.3 "What the framework determines and what the specific bijection determines", line 1394:

> **Structural predictions** are properties of the equivalence class [(S, φ)]/$\mathcal{G}_{\text{sub}}$ — they hold for
> every bijection satisfying the six structural properties. These include, conditionally on H-link with its single-copy
> clause and H-cust (§4.5–§4.6): SU(3) × SU(2) × U(1) with multiplicities (3, 2, 1), three generations (chirality
> conditional on H-χ', §4.8) ..., one Higgs doublet ..., unique hypercharges from anomaly cancellation ..., and the
> universal induced coupling $1/\alpha_0 = 23.25$ (§6.1). ... The horizon calibration ... and the Bekenstein-Hawking
> coefficient ... hold for the same class as consistency relations conditional on H-slope ...

Same section, line 1400 (Layer 0): these properties "follow from the bijection's bounded-degree coupling structure
together with cubic-group representation theory (§4.5–§4.7); C1–C4 are diagnostics ..., not inputs". Line 1436:
"all SM predictions live at Level D × Levels G1–G2" (of [Structure §2]). Line 1372: the equivalence class is
"Level D × Level G3".

**SM never defines or enumerates "the six structural properties".** No antecedent exists anywhere in SM.md at H:
- §2.1 "Assumptions by result" (SM.md:42–52) lists five bold items: deterministic bijectivity; finite boundary
  entropy; bounded coupling degree; statistical homogeneity and isotropy; C1–C4.
- §2.3 (SM.md:60) states the construction's assumptions as "A3–A4, ... A5–A6, the nearest-neighbour restriction and
  ... H-link", and "a set S, finite under A1".
- SM uses the Substratum labels A1, A3, A4, A5, A6 (SM.md:30, 56, 60, 104, 114, 172, 202, 222, 226, 232, 240, 1257,
  1416), but never the phrase "A1–A6" and never a count "six" for them.
- Every other "six" in SM.md is links, anomaly conditions, carrier components, dimension-six, six-mass chain, etc.

## 2. Definitions and uses across the corpus at H

### A1–A6 (the substratum class conditions)
- papers/Substratum.md:90 "**Structural assumptions** (restrictions on the class of candidate substrates (S, φ))":
  (A1) Finiteness, (A2) Determinism, (A3) Bounded coupling degree, (A4) Center independence, (A5) Linearity,
  (A6) Background independence. :104 "The theorem's uniqueness claim holds under E1–E7 **and** A1–A6 jointly".
  Isotropy is not among A1–A6; it is empirical input E4.
- papers/Structure.md:140 "A1–A6 are conditions for membership in *OI's specific* universality class (Level D)";
  Structure.md:168 "Level G2 × Level D: the emergent QFT structure — SM gauge group, matter content, gauge
  invariances". Structure's Level G2 is "SM gauge group on the emergent QFT" (Structure.md:152), not a six-item list.
- Main.md:736 posit ledger: fourteen items; A1 content is item (ii); not a "six".
- book/ch02-substratum.md:74 "candidate substrates satisfying six properties:" followed by (A1)–(A6);
  ch02:120 "together with six structural assumptions and the nearest-neighbor restriction". (Mirrored in FULL:704, 750.)
  A1–A6 are called "structural assumptions" / "six properties"; nowhere in the corpus "six structural properties".

### "six structural properties" / "six properties" elsewhere (all at H)
- book/ch09-universality.md:36 "Level G2 is the structural properties of the substratum (the six properties developed
  in Chapter 5: isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count)."
  Level G1 there is "general structural axioms ... with the open hypothesis A1" — i.e. A1 is placed at G1, outside the six.
- ch09:137 "the six structural properties developed in Chapter 5 (isotropy, sublattice structure, link content,
  anomaly cancellation, taste content, generation count)". (FULL:2552.)
- ch19:198 "if the initial state of φ is statistically isotropic (one of the framework's six structural properties of
  the bijection)" — isotropy is a member, which fits the ch09 G2 list and not A1–A6. (FULL:5268.)
- ch19:212 "The framework's axioms — deterministic bijectivity, causal partition, classical probability — together with
  the open hypothesis A1 of finiteness constrain the class. The framework's six structural properties of the bijection
  (developed across Chapters 5-7) further narrow it." — A1 is placed with the axioms, separate from the six. (FULL:5282.)
- ch09:104 "The framework's universality-class commitments ... are six structural properties of the substratum":
  Finiteness (A1), Deterministic bijection, Causal partition, C1, C2, C3 (ch09:106–116). A third, different six-set,
  which does include finiteness. (FULL:2519.)
- ch05-gauge-structure.md at H contains no enumeration of six properties (the ch09 attribution to "Chapter 5" has no
  matching list there).

So the corpus uses "six (structural) properties/assumptions" for at least three different sets:
(a) A1–A6 (ch02, as "six properties"/"six structural assumptions");
(b) the Chapter-5 G2 set (isotropy, sublattice structure, link content, anomaly cancellation, taste content,
    generation count) — ch09:36, ch09:137, ch19:198, ch19:212, all as "six (structural) properties";
(c) the ch09:104 universality-class list (finiteness, bijection, causal partition, C1, C2, C3).

## 3. History

- Local clone is shallow (boundary commits 2026-11-11/12, e.g. fe505d463 is a shallow root; its "-S" hit is an
  artifact of the boundary). Earlier history was read through the GitHub REST API (read-only):
  258 commits touch papers/SM.md up to H; sampled versions at commits 1, 3, 10, 30, 60, 100, 150, 200, 258 (ascending)
  all contain "six structural properties" exactly once.
- The sentence is present in the **first** version of papers/SM.md, commit 334eef0a305c23e00a3756d8b62bf409cc035637
  (2026-05-14, "add book files"), SM_first.md:1237:
  > **Structural predictions** are properties of the equivalence class [(S, φ)]/G_sub — they hold for every bijection
  > satisfying the six structural properties. These include: SU(3) × SU(2) × U(1) with multiplicities (3, 2, 1), three
  > chiral generations ..., one Higgs doublet ..., unique hypercharges from anomaly cancellation, θ̄ = 0 at all energy
  > scales, ℏ = c³ε²/(4G), the Bekenstein-Hawking formula, and the universal induced coupling 1/α₀ = 23.25 (§6.1).
  > These are theorems.
  The origin is therefore older than the local clone and coincides with the repository import; the same commit already
  contains both candidate referents:
  - first Substratum.md:100/189 and first Structure.md:47 define A1–A6 ("structural assumptions A1-A6 (finiteness,
    determinism, bounded coupling, center independence, linearity, background independence)");
  - first ch09-universality.md:38 has the G2 list ("the six properties developed in Chapter 5: isotropy, sublattice
    structure, link content, anomaly cancellation, taste content, generation count"), and first ch09:46:
    "The derivation of the Standard Model gauge group lives at Level O2 × Level G2 — the cubic-lattice substratum with
    its six structural properties produces SU(3) × SU(2) × U(1) with three generations"; first ch09:304
    "a cubic lattice at ε = 2 l_p with the six structural properties of Chapter 5".
  - first SM §2.1 (SM_first.md:42–50) listed: deterministic bijectivity, finite boundary entropy, bounded coupling,
    homogeneity and isotropy, C1, "slow bath with capacity (C2, C3)" — five or six depending on how C2/C3 count;
    not labelled as "six" and not referred back to by §8.3.
- Authorship order within that import cannot be recovered from the repository (single import commit).

## 4. Conclusion: (iii) undetermined from SM's own text; the inferred authorial referent leans to (ii)

**Shown:**
1. SM.md has no definition, list or back-reference that fixes "the six structural properties"; the definite article
   points to nothing in SM.
2. In the whole corpus at H (and at the first import), the exact phrase "six structural properties" is used only for
   set (b) (ch09:137, ch19:198, ch19:212, first ch09:46, first ch09:304) and for set (c) (ch09:104). A1–A6 are never
   called "six structural properties"; they are "structural assumptions" (Substratum, Structure, ch02:120) or "six
   properties" (ch02:74).
3. First ch09:46 — written in the same import as the SM sentence — attaches "six structural properties" to exactly the
   claim SM:1394 makes (the cubic substratum with those properties produces SU(3)×SU(2)×U(1) with three generations).
4. Set (b) excludes A1: ch09:36 places A1 at Level G1 apart from the six; ch19:212 lists A1 with the axioms and the six
   separately; ch19:198 counts isotropy as one of the six, which A1–A6 do not contain.
5. The plan P keeps ch09:36's and ch09:137's G2 "six" and ch19:198/212's "six structural properties of the bijection"
   unchanged (no splice touches those clauses), while rewriting ch02:74/120 (A1–A6) and ch09:104/190 to "five".
   The plan therefore itself treats set (b) as not counting A1.

**Evidence for (i) (A1–A6), inferred rather than shown:**
- "every bijection satisfying ..." is condition-on-the-class phrasing, and the equivalence class [(S, φ)]/G_sub is the
  object Substratum's reconstruction fixes under E1–E7 and A1–A6; SM:1436 places all SM predictions at Level D, whose
  membership conditions are A1–A6 (Structure:140). A reader of SM alone, who has the Substratum citations (A1, A3–A6)
  and not the book, would most plausibly resolve "six" to A1–A6.
- Set (b) reading makes the sentence partly circular: "anomaly cancellation" and "generation count" are listed both as
  properties assumed and as predictions; and θ̄ = 0, ħ and the Bekenstein-Hawking formula (first version's list) are
  not consequences of set (b) alone.

**Evidence against (i):** A1–A6 omit isotropy and H-link, which the listed gauge results need (SM §2.1, §4.5–4.6);
SM's own Layer 0 (SM:1400) derives these from bounded-degree coupling plus cubic representation theory, not from A1;
and the phrase match in (2)–(4).

**Verdict.** What the sentence denotes is not fixed by SM; it is (iii) ambiguous. The authorial referent most
supported by the record is (ii), set (b) — isotropy, sublattice structure, link content, anomaly cancellation, taste
content, generation count — which does not include A1. That is an inference from parallel wording in the same import,
not a definition in SM. Set (c), which does include finiteness, is a further possible reading for which I found no
specific support in SM.

Consequence for acceptance item 7 (stated only as a fact about the text; the item's exact scope was not read): applying
every splice of P's ledger to H (all 44 files' expected sha256 verified) leaves "six structural" at
papers/SM.md:1394, book/ch09-universality.md:137, book/ch19-open-problems.md:198 and :212, and FULL.md:2554, 5270, 5284.
SM:1394 is not the only residual hit; the others are set-(b) uses the plan deliberately keeps. Whether SM:1394 is a
false positive cannot be settled from SM's text. Under (ii) it is. Under (i) it is not, and then the minimal rewrite
parallel to the plan's would change the count to five. The plan's parallel book edits (P ledger):
- D239/D240 (ch02/FULL): "The reconstruction restricts attention to candidate substrates satisfying six properties:" →
  "The reconstruction restricts attention to finite candidate substrates satisfying five properties:"
- D255/D256 (ch09:104/FULL): "are six structural properties of the substratum, organized as follows." → "are, for the
  finite OI class, five structural properties of the substratum; finiteness, stated first, is that class's scope.
  They are organized as follows."
A (i)-style rewrite of SM:1394 would be "... satisfying the five structural properties" (or "the structural
assumptions A2–A6 on a finite substratum"). Under (ii) that would be wrong, because set (b) has six members and no A1.
A rewrite that names the set removes the ambiguity under either reading. I state that as an option, not a
recommendation.
