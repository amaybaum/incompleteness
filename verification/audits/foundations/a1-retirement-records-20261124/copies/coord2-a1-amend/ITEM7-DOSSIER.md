# Item 7 of the frozen A1 plan: what it checks, why it fails, and what follows

## 0. Status

**Paper-only and read-only.** No repository file was changed and nothing was written to GitHub. The dossier proposes
no amendment, and none is authorized. The owner's words (owner `amaybaum`, 2026-11-24, relayed in session): "No
amendment to the frozen plan is authorized yet."

**Owner request** (owner `amaybaum`, 2026-11-24, relayed in session; not yet recorded on GitHub), quoted: "We should
not change an acceptance criterion merely because we discovered that the proposed retirement fails it. For the review,
please provide the exact original wording of item 7, the demonstrated failure, the proposed replacement wording and the
scientific consequences of that replacement."

**Goal link (§A.47).** A1-EXIT (#1169). This dossier decides nothing. It supplies the evidence for the owner's choice
among (a) correcting the criterion, (b) correcting the implementation, and (c) removing or replacing the criterion.

**Labels used below.** A statement marked **[shown]** was checked from git objects or recorded outputs in this
session. A statement marked **[inference]** is a judgement about meaning, and needs scientific review.

Sources:

- `P` = `4c79be642ca631573f06b444903be75ec4f5e2b6`, the frozen plan.
- `H` = `53c6601a10419b6b333cc992474272501ab542af`, the ledger base, on `main`.
- T1′ = `14ac71b4b0a0c0aa2d7068d6799a73f474097060`. Its manuscripts equal `H` plus `P`'s ledger, byte for byte
  (PROPOSAL.md sec. 2, V5).
- Tool design v6.0c, a draft: `DESIGN-v6.0c.md`, sha256 `dd72ee5b…4aa594`.
- The independent S1 review's control results: `review-stage1-s1/results/full/a1-controls.json`, sha256
  `832ba5ccf79aac18bd15cf062c181f95afc3015a33146fb54e6a8d65a3e10942`.

## 1. The frozen wording and the text that defines its terms

### 1.1 Item 7, verbatim

From `verification/audits/foundations/a1exit-deletion-20261121/PREREG.md` at `P`, §11 "Post-execution checks
(preregistered)", which opens "At the execution head, all of the following, with outputs recorded in the execution
record:":

```text
 4631  7. Corpus grep for `\bA1\b`, "total-finiteness", "posit (ii)", "item (ii)", "finiteness posit": only the
 4632     ledger's false positives remain; grep of posit counts ("Fourteen", "six structural", "sixth of"): zero.
```

**The tree it runs on.** Item 7 runs at the execution head `X`, a single-parent child of `H` whose tree applies the
ledger. The grep's scope is not stated in item 7 itself. The plan's own count grep (§4, below) and the tool design take
it as `papers/*.md` and `book/*.md`.

**Frozen text that defines its terms.**

The "ledger's false positives" are named in `P` §10:

```text
 4600  S2-E's branch rewrites, and the one identifier finding at the base is the "A1–A6" range in Methodology (an
 4601  S2-E site); on the projection, after the edit list, the residual is zero apart from the ledger's
 4602  false positives (the appB anomaly conditions "(A1)" and their FULL mirror) and GR:58's finite-scope wording
 4603  "For a finite total system", which the P2 pattern matches.
```

The plan's posit-count grep for D226 (§4):

```text
  206  - D226 changes "Fourteen items … not fourteen" to "Thirteen items … not thirteen". The corpus-wide grep for
  207    a posit count (`fourteen|14 (items|posits)` over `papers/*.md`, `book/*.md`) finds only this site.
```

The counts the plan rewrites (§4):

```text
  237  S2-A review finding on ch02:74 and Sub:90); Sub:90 itself names no assumption and is unchanged.
  238  
  239  **Counts and ranges elsewhere.** ch02:74 = FULL:704 "six properties" → "five properties" (D239–D240);
  240  ch02:120 = FULL:750 "six structural assumptions" → "five structural assumptions on a finite substratum"
  241  (D241–D242; ch02:74 also takes "finite candidate substrates", review F8); ch09:104 = FULL and ch09:190 = FULL
  242  "six structural properties/axioms" → five, with finiteness worded as the finite class's scope (D255–D258); gloss:13 "The sixth of the framework's structural assumptions A1–A6" → "The structural
  243  assumption A6 of the reconstruction theorem (A2–A6)". Every "A1–A6" / "A1-A6" range at the base is a ptr
  244  site or GR:673 (§7 H-1) and is rewritten; no "A2–A6" range is renumbered (checker `--static`, identifier
```

The plan's cross-reference statement (§22.2):

```text
 4894  **Cross-references (item 4).** No posit count, "six structural" or "item (ii)" occurs outside the
 4895  manuscripts in the active tree (grep at `0ba358cc`). The README's "Every one of the six is a condition on a
 4896  substratum" counts the six conditions (finiteness and A2–A6) its rewritten sentence lists, and stays.
```

**How the plan implemented this check.** The plan's checker `edits_check.py` at `P` (`identifier_sim`, run by
`--simulate`) tests these exact retired phrasings, not the bare literal "six structural":

```text
  330      for path, t in sim.items():
  331          for pat, msg in ((r'satisfying six properties', 'reconstruction properties still "six"'),
  332                           (r'six structural assumptions', '"six structural assumptions" survives'),
  333                           (r'sixth of the framework\'s structural assumptions', '"sixth of the ... assumptions" survives'),
  334                           (r'are six structural properties of the substratum', 'ch09 "six structural properties" survives'),
  335                           (r'Six structural axioms must be checked', 'ch09 "Six structural axioms" survives'),
  336                           (r'\bA1\s*[–-]\s*A6\b', 'A1–A6 range survives')):
  337              if re.search(pat, t):
  338                  out.append('%s: %s' % (path, msg))
```

### 1.2 Terms that are not frozen

The profiles `count-grep`, `item7-literal`, `ptr` and `resid`, the deny rules DR-1, DR-3, DR-4 and DR-5, and the allow
rules W1 and W2 are constructs of the tool design (v6.0c draft, sec. 6.4-6.6). They exist as unreviewed draft records
in the tool landing (`rules/dr-deny-v1.json`, `rules/resid-v1.json`, `rules/w1-w2-allow-v1.json`). **None of them is
part of the frozen plan, and none of them defines item 7.** Sec. 5 uses them only because the design's proposed
replacement is written in their terms.

## 2. What item 7 checks, and why

**In plain terms.** After the retirement, the manuscripts (papers and book) must not:

- refer to A1 or to the retired ledger item by any of its names, except the listed false positives, which are the
  appendix B anomaly label "(A1)" and its mirror; or
- state any posit count that would include A1: "Fourteen" posits, "six structural" assumptions or properties, or "the
  sixth of" a list that starts at A1.

The first half catches surviving pointers. The second half catches counts that silently keep A1 in the tally after
its entry is deleted.

**The scientific purpose the plan states.** Item 7 has no purpose sentence of its own. Its purpose follows from the
owner's objective and design decision, which `P` §0 quotes:

```text
   49  > **Objective.** Remove A1 as a global assumption without silently weakening any theorem, introducing
   50  > unjustified physical assumptions, or concealing unresolved dependencies.
```

```text
   57  > - **Reserve the A1 identifier.** It is never reused (AGENTS.md §A.30).
   58  > - **Preserve cardinality neutrality.** OI does not assume that the universe has finitely many
   59  >   configurations, and it does not assume that it has infinitely many.
   60  > - **Retain conditional results.**
   61  >   - Finite-only results remain explicitly scoped.
   62  >   - Results that need an additional probability law or another hypothesis state it openly.
   63  > - **Preserve surviving identifiers.** A2, A3 and the other identifiers are not renumbered as part of
   64  >   A1-EXIT.
```

The plan's own rewrites show what the count half is for. "Fourteen items" becomes "Thirteen" (D226). "six structural
assumptions" and "six structural properties of the substratum" become five (D239–D242, D255–D258). "The sixth of the
framework's structural assumptions A1–A6" is rewritten. All of these are counts in which A1 is one of the counted
items. **[inference]** The purpose of the count half is therefore that no active text counts a set that includes the
retired A1. It is not meant to ban the word "six" in other counts.

## 3. The demonstrated failure

### 3.1 Evidence

**[shown]** The literal grep over `papers/*.md` and `book/*.md` (`git grep -P`, read-only, this session):

| Pattern | at `H` | at T1′ |
|---|---|---|
| `\bA1\b` | 179 | 4 |
| `total-finiteness` | 8 | 0 |
| `posit \(ii\)` | 1 | 0 |
| `item \(ii\)` | 11 | 0 |
| `finiteness posit` | 13 | 0 |
| `Fourteen` | 1 | 0 |
| `six structural` | 11 | **7** |
| `sixth of` | 2 | 0 |

**[shown]** The tool's control RT-I7, as the independent S1 review ran it (`a1-controls.json`, status PASS):

```text
"RT-I7": { "actual": { "H":   { "A1_lines": 179, "exit": 20, "lines": 14,
                                "literals": { "Fourteen": 1, "six structural": 11, "sixth of": 2 } },
                       "T1p": { "A1_lines": 4, "exit": 20, "lines": 7,
                                "literals": { "six structural": 7 } } },
           "expected": "FAIL at both; T1': 7 / 0 / 0, A1 4; H: 11 / 1 / 2, A1 179", "status": "PASS" }
```

The design's row (v6.0c sec. 10.3):

```text
 2171  | RT-I7 | `terms --commit T1' --profile item7-literal`; the same at H | FAIL `item7-literal-match` at both | T1': exactly 7 "six structural" lines (SM.md:1394, ch09:137, ch19:198 and 212, FULL:2554, 5270 and 5284), 0 "Fourteen", 0 "sixth of"; `\bA1\b` 4 (the W2 lines). H: 11 / 1 / 2; `\bA1\b` 179 |
 2172  | RT-I7A | the proposed item-7 amendment check (sec. 11 note 1) at H and at T1', no records | FAIL at both. Every one of the 95 retired lines of sec. 0.3 is FAIL (`final-unclassified`), none only REVIEW | H: 86 `deny-match` lines and 123 `final-unclassified` lines (209 FAIL lines), counting line-level deny matches only; with every line of a matching multi-line sentence counted, 93 and 216, the 123 unchanged (O8). T1': 0 deny lines; 12 `final-unclassified` lines (the 7 W1 lines, the 4 W2 lines, GR.md:58), which become PASS once W1 (with W1-c's allowance), W2 and GR.md:58's record exist |
```

**[shown]** The plan's own implementation passes at the post-deletion tree. `P` §31.10 item 1 records "`--commit
53c6601a --simulate` 391/391 unique, residual 5 (all allowed), 0 unscoped, 0 preservation, 0 identifier". The T1′
trial, run 45080985924, passed every step. `identifier_sim` never runs the bare literal (sec. 1.1). The tool design
says the same: "The plan's own implementation never ran the literal grep."

### 3.2 Which half fails

- **The pointer half passes. [shown]** The 4 `\bA1\b` lines at T1′ are `book/appendix-b-derivations.md:235` and
  `:246`, and `FULL.md:5914` and `:5925`. They are the anomaly conditions "(A1) $\mathrm{SU}(3)^3$ anomaly" and "(A1)
  is automatically satisfied", which are exactly the false positives `P` §10 names. The other four pointer terms have
  0 hits.
- **The count half fails, on 7 lines of 4 distinct sentences. [shown]**

  | Sentence | Lines at T1′ | Lines at `H` | Changed by the plan? |
  |---|---|---|---|
  | S1 | `papers/SM.md:1394` | `SM.md:1394` | no |
  | S2 | `book/ch09-universality.md:137` = `FULL.md:2554` | `:137` = `:2552` | no |
  | S3 | `book/ch19-open-problems.md:198` = `FULL.md:5270` | `:198` = `:5268` | no |
  | S4 | `book/ch19-open-problems.md:212` = `FULL.md:5284` | `:212` = `:5282` | its preceding clause is edited |

  The sentences, verbatim (the full fingerprinted sentences):

- **W1-a** (`papers/SM.md`):
  > **Structural predictions** are properties of the equivalence class [(S, φ)]/$\mathcal{G}_{\text{sub}}$ — they hold for every bijection satisfying the six structural properties.
- **W1-b** (`book/ch09-universality.md`, `book/The-Incompleteness-of-Observation-FULL.md`):
  > Tier 2 results follow from the framework's structural commitments to the substratum's properties — the six structural properties developed in Chapter 5 (isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count) — combined with the universality-class conditions C1–C4.
- **W1-c** (`book/ch19-open-problems.md`, `book/The-Incompleteness-of-Observation-FULL.md`):
  > On a finite periodic quotient of $\mathbb{Z}^3$, a qualified case of A4 (Chapter 2), the notion of "causally disconnected regions" is modified — the lattice's coupling graph determines causal structure, and if the initial state of $\varphi$ is statistically isotropic (one of the framework's six structural properties of the bijection), isotropy is built in rather than requiring inflation to produce it.
- **W1-d** (`book/ch19-open-problems.md`, `book/The-Incompleteness-of-Observation-FULL.md`):
  > The framework's six structural properties of the bijection (developed across Chapters 5-7) further narrow it.

- **[shown]** All 7 of these lines exist at `H`, unchanged apart from S4's context. The 7 other count hits at `H` are
  the retired counts the plan rewrites: ch02:120 and FULL:750 ("six structural assumptions"), ch09:104 and FULL:2519
  ("six structural properties of the substratum"), glossary:13 and FULL:6504 ("The sixth of the framework's structural
  assumptions A1–A6"), and Main:736 ("Fourteen items"). None of these survives at T1′.

So item 7 fails for one reason only: the literal "six structural" matches four sentences that the plan does not edit.

## 4. Classification of each failure

The test for each sentence: does the "six" it counts include A1? A1–A6 at `H` are the following (`papers/Substratum.md`
at `H`; each line cut at 170 characters and marked "…" by this dossier):

```text
   92  (A1) **Finiteness.** The configuration space $S$ is finite. E3, read as a Hilbert-space dimension cutoff $\dim\mathcal H\le e^{A/4}$, bounds the observationally re …
   93  
   94  (A2) **Determinism.** $\varphi: S \to S$ is a bijection (deterministic, reversible dynamics). (Two-part status, per the dilemma argument of [Main §1.2]: a non-inje …
   95  
   96  (A3) **Bounded coupling degree.** Each site is coupled to a bounded number of neighbors in $\varphi$'s action. (Required for locality and the emergence of a coupli …
   97  
   98  (A4) **Center independence.** The dynamics $\varphi$ does not depend on a choice of "center" site, in two senses used below: $\varphi$ commutes with lattice transl …
   99  
  100  (A5) **Linearity.** The selected wave-equation model assumes a linear update. First differences independent of the base point give exactly the affine rules [SM §4. …
  101  
  102  (A6) **Background independence.** The dynamics is covariant under spatially-varying internal-index transformations: a site-dependent transformation $G(\mathbf{n})$ …
  103  
  104  The theorem's uniqueness claim holds under E1–E7 **and** A1–A6 jointly, with the nearest-neighbor premise of Stage 2(b); removing any of A3–A6 either requires new  …
```

A1–A6 are therefore finiteness, determinism, bounded coupling degree, center independence, linearity and background
independence.

### S2 (`ch09:137` = `FULL:2554`): (a) the criterion is too broad here

- **[shown]** The sentence lists its six: "isotropy, sublattice structure, link content, anomaly cancellation, taste
  content, generation count". `ch09:36` (at `H` and at T1′) calls these "the six properties developed in Chapter 5",
  which are Level G2. Finiteness is not among them, and neither is any of A1–A6.
- **[shown]** The plan's checker deliberately does not target this sentence (sec. 1.1).
- **Classification: (a).** A correct sentence counting a set without A1 is flagged. Changing it would alter correct
  text to satisfy a grep.

### S3 (`ch19:198` = `FULL:5270`): (a)

- **[shown]** The sentence names isotropy as "one of the framework's six structural properties of the bijection".
  Isotropy is the first item of the Chapter-5 list (`ch09:36`, `:137`) and is not one of A1–A6. In Substratum,
  isotropy is the empirical input E4.
- **[inference]** "the six structural properties of the bijection" here is the Chapter-5 set.
- Its "finite periodic quotient" describes A4's qualified lattice case, not a finiteness posit.
- **Classification: (a).**

### S4 (`ch19:212` = `FULL:5284`): (a), on inference

- **[shown]** At `H` the paragraph read: "The framework's axioms — deterministic bijectivity, causal partition,
  classical probability — together with the open hypothesis A1 of finiteness constrain the class. The framework's six
  structural properties of the bijection (developed across Chapters 5-7) further narrow it." The plan's edit removes
  only "together with the open hypothesis A1 of finiteness".
- **[inference]** At `H`, A1 was named in the first sentence as one of the constraints, separately from the "six
  structural properties", which "further narrow" the class. They are "developed across Chapters 5-7", whereas A1–A6 are
  stated in Chapter 2. The six therefore did not include A1, and they match the Chapter-5 set.
- **Classification: (a).** This needs scientific review, because "developed across Chapters 5-7" differs slightly
  from `ch09`'s "developed in Chapter 5".

### S1 (`SM.md:1394`): undetermined; candidate (b)

The criterion may be correct here, with the planned edits leaving an A1-inclusive count.

**[shown]**

- No other line of `papers/SM.md` at T1′ or at `H` defines "six structural properties". The only "structural
  propert…" hits are line 1040 ("The structural property is that $A_1$ …", about the mixing generator) and line 1394
  itself.
- The draft W1-a rule says it "Counts the bijection's six structural properties as SM defines them". That reason is
  **not supported**: SM contains no such definition.
- The book's reconstruction section at `H` reads: "The reconstruction restricts attention to candidate substrates
  satisfying six properties:" (`ch02:74`). Those six are A1–A6, and the plan rewrites this to "finite candidate
  substrates satisfying five properties" (D239). `P`'s checker targets the same phrasing ("satisfying six
  properties").
- SM:1394 lists as structural predictions the gauge group, the three generations and the anomaly-fixed hypercharges.
  At `H`, Substratum states that the reconstruction yielding these holds "under E1–E7 **and** A1–A6 jointly". At T1′
  it reads "for a finite substratum under E1–E7 **and** A2–A6".
- SM:1394 appears in no site map, ledger row or Phase-0 site list (`git grep` of `verification/` at `H` finds it only
  in a numeric-token regression snapshot). No classification of it by the plan exists.

**[inference]**

- "every bijection satisfying the six structural properties", in a paper whose predictions rest on the reconstruction
  theorem, most plausibly means A1–A6, in the same phrasing as `ch02:74`.
- The other reading, the Chapter-5 G2 set, would include "anomaly cancellation" and "generation count". That would make
  the sentence say the predictions hold for every bijection satisfying properties that include those same predictions,
  which is less plausible.
- If the A1–A6 reading is right, SM:1394 is a pointer site the plan missed. After the retirement it would keep a count
  that includes A1. That is exactly what item 7 exists to catch.

**Classification: (b) candidate, pending scientific review.**

- If review confirms the A1–A6 reading, the plan's implementation, not the criterion, is at fault, and SM:1394 needs an
  edit (sec. 6).
- If review establishes the Chapter-5 reading, SM:1394 joins S2–S4 under (a). Even then the sentence names a count
  with no referent in its own paper, which a scope note or citation would fix.

### (c) Is the criterion unnecessary?

No, on the evidence. The count half is the only check in the plan that searches unedited text for A1-inclusive counts.

- `identifier_sim` tests only the phrasings the plan already knew about.
- The literal grep is what surfaced SM:1394, which no plan record classifies.
- Removing the count half would remove the only line of defence against counts the edit list missed.

### Summary

| Failure | Classification | Strength |
|---|---|---|
| `\bA1\b` half | no failure: only the listed false positives remain | [shown] |
| S2: ch09:137, FULL:2554 | (a) | [shown]: the list is in the sentence |
| S3: ch19:198, FULL:5270 | (a) | [shown] facts, [inference] reading |
| S4: ch19:212, FULL:5284 | (a) | [inference] from the `H` paragraph's structure |
| S1: SM:1394 | (b) candidate, undetermined | [shown] that SM defines no six and that the W1-a reason is unsupported; [inference] the A1–A6 reading |

## 5. Replacement wordings and their consequences

### 5.1 The design's proposal, verbatim (v6.0c, sec. 11 table row 7 and note 1)

```text
 2302  | 7 | corpus grep: only ledger false positives for `\bA1\b` and related terms; posit counts ("Fourteen", "six structural", "sixth of"): zero | as frozen: `terms --commit X --profile item7-literal` | **FAIL** at T1': 7 "six structural" lines (W1), 0 "Fourteen", 0 "sixth of"; `\bA1\b` 4 lines (W2). Item 7 as frozen does not pass at T1' (RT-I7) | the H-form "Fourteen items" reinstated (V22): FAIL in both the literal check and DR-5. See note 1 for the proposed amendment |
```

```text
 2311  **Note 1 (item 7; owner decision D1).** Item 7 as frozen fails at T1': seven lines contain the
 2312  legitimate count of the bijection's properties (W1). The tool keeps that literal check as the named
 2313  countercontrol `item7-literal`, with the expected FAILs of RT-I7.
 2314  
 2315  - Any restatement of item 7 is a **plan amendment**. It needs its own preregistered text, an
 2316    independent review of the deny set (sec. 6.4), the `resid` profile (sec. 6.6) and the W1 rules,
 2317    and the owner's authorization. It is not "passing as written", and it cannot be used in the
 2318    current frozen trials. Under the exception-free route, the amendment must be adopted before any
 2319    trial can claim item 7.
 2320  - The check this design proposes for that amendment: `terms --commit X --base H --ledger
 2321    F:ledger.json --check item7 --final`, where the configuration's `checks.item7` (sec. 16.2) has
 2322    profiles `ptr`, `count-grep`, `resid`, DR-1, DR-3, DR-4 and DR-5 and `final_profiles` `ptr` and
 2323    `count-grep`. It requires zero deny matches; every `ptr` and `count-grep` hit not classified by a
 2324    reviewed rule or record is FAIL `final-unclassified`; every unclassified `resid` hit is
 2325    REVIEW_REQUIRED.
 2326  - **Failure behaviour is not weakened (V3).** The original item 7 fails hard on any `\bA1\b` line
 2327    that is not a ledger false positive and on any posit-count literal. In the proposed check every
 2328    such line is a `ptr` or `count-grep` hit, so it is FAIL unless a reviewed record classifies it,
 2329    which is the counterpart of the original's "ledger false positive". At H, 95 retired lines carry
 2330    `\bA1\b` or a `count-grep` literal and match no deny rule; under v4's check they were only
 2331    REVIEW, and under this check all 95 are FAIL (RT-I7A). Counts with no records: at H, 86 deny lines
 2332    (line-level matches; 93 if each line of a matching multi-line sentence is counted) and 123
 2333    `final-unclassified` lines; at T1', 0 deny lines and 12 `final-unclassified` lines (the 7
 2334    W1 lines, the 4 W2 lines and papers/GR.md:58), which pass once their rules and record exist.
 2335    Countercontrols: V23 and V24 FAIL; V25 shows the other direction. `resid` hits stay REVIEW: the
 2336    original check does not fail them at all, so keeping them REVIEW is stricter than the original,
 2337    not weaker.
 2338  - **Scope (O7).** Item 7's scope is `papers/*.md` and `book/*.md`. Active files outside it still
 2339    carry "the sixth structural assumption" for A6, whose count includes A1 (for example
 2340    `verification/README.md:2320` and `A6Instantiation.lean:15` at T1'). The amendment's scope
 2341    statement names this, and DR-1's ordinal alternatives are a corpus terminology decision
 2342    (sec. 6.4).
 2343  - v3's claim that the restatement "changes the check's text, not its decision on any retired form"
 2344    was false for v3's seed set: the H sentence "Fourteen items, of unequal weight, ..."
 2345    (papers/Main.md:736) escaped DR-1..DR-4. With DR-5 it is a FAIL (RT-DR, V22). The claim is not
 2346    repeated for the v5 set: whether that set preserves the original prohibition on every retired
 2347    form is the independent review's question. The lexically unanchored paraphrases remain a stated
 2348    residual limit (sec. 1), covered at least by REVIEW through `resid` for the classes sec. 1 names.
 2349  - The plan's own implementation never ran the literal grep. It checked the retired phrases of
 2350    `identifier_sim()`, P lines 331-335.
```

The design proposes a check, not a sentence. Written as an item, it would read:

```diff
-7. Corpus grep for `\bA1\b`, "total-finiteness", "posit (ii)", "item (ii)", "finiteness posit": only the
-   ledger's false positives remain; grep of posit counts ("Fourteen", "six structural", "sixth of"): zero.
+7. `terms --commit X --base H --ledger F:ledger.json --check item7 --final` passes: no line of `papers/*.md` or
+   `book/*.md` matches a deny rule DR-1, DR-3, DR-4 or DR-5; every line that `ptr` or the posit-count literals
+   ("Fourteen", "six structural", "sixth of") match is classified by a reviewed allow rule or hit record frozen
+   with the plan; lines that `resid` matches are reported for review.
```

**What it stops catching.** Nothing, by itself. A literal hit is still FAIL unless a reviewed record classifies it.
The judgement moves from the grep into reviewed records (W1, W2, the GR.md:58 record). The consequence follows: under
the draft W1-a, **SM:1394 would PASS** on a reason that sec. 4 shows unsupported. The replacement is safe only if each
allow record is reviewed against the A1–A6 question, and W1-a as drafted should not be accepted.

**What it adds.**

- Deny rules that FAIL reworded A1-inclusive counts the literal misses. DR-1, for example, catches "seven structural
  axioms" and "the six substratum premises". RT-I7A shows all 95 retired lines at `H` FAIL.
- REVIEW (not FAIL) for finiteness paraphrases (`resid`).

Residual limits the design states: "the framework's sixth structural property, finiteness of the bijection" PASSes
(V4), and so does "The framework's sixth structural property is finiteness of the substratum" (V27). The original
item 7 misses both too.

**Controls the design defines.**

- V22: the H sentence "Fourteen items, …" reinstated → FAIL (DR-5).
- V24: "six structural hypotheses" added → FAIL `final-unclassified`.
- V23: "(finite under A1)" reinstated → FAIL.
- RT-I7A at T1′: 12 lines `final-unclassified` (S1–S4's 7, W2's 4 and GR.md:58), which PASS only with their records.

### 5.2 A narrower alternative: keep the grep, list the exceptions

This keeps the frozen check and its strictness, and adds an explicit exception list, as the pointer half already has
for "the ledger's false positives":

```diff
 7. Corpus grep for `\bA1\b`, "total-finiteness", "posit (ii)", "item (ii)", "finiteness posit": only the
-   ledger's false positives remain; grep of posit counts ("Fourteen", "six structural", "sixth of"): zero.
+   ledger's false positives remain; grep of posit counts ("Fourteen", "six structural", "sixth of"): zero, apart
+   from the lines listed in §<n>, each a sentence, quoted in full with its sha256, that counts a set not containing
+   A1, with that set named. A listed line passes only if its sentence is byte-identical to the quoted one.
```

The proposed list contains only S2, S3 and S4, six lines in all, each paired with its FULL mirror. **SM:1394 is not
listed.**

**Consequences.**

- *It stops catching* an A1-inclusive count only if one is written into exactly those three sentences. Any change to a
  listed sentence re-fails it.
- *It still catches* every other "Fourteen", "six structural" or "sixth of" line anywhere in the manuscripts.
- *It does not add* the design's deny rules. Reworded counts such as "seven structural axioms" stay as uncaught as they
  are under the frozen item.

**Control and countercontrol [shown, by `git grep` at `H` and T1′].**

| Tree | Lines that still fail under 5.2 | Expected |
|---|---|---|
| `H` | 8: the 7 retired count lines of sec. 3.2, plus SM:1394 | fail |
| T1′ | 1: SM:1394 | fail until SM:1394 is resolved |
| `H`'s "Fourteen items" (Main:736) or ch02:120's "six structural assumptions" reinstated into T1′ | the reinstated line, plus SM:1394 | fail (a genuine reassertion is caught) |

### 5.3 What either replacement still needs

The scientific question on SM:1394 (sec. 4) is the same under both. If it is (b), the remedy is an edit, not a change
to the criterion.

## 6. The edit correction if SM:1394 is (b)

**The correction.** One new edit record and its splice. Nothing else in the ledger changes.

- **ID:** the next unused ID, D402. `edits.json` at `P` has 401 records, D001–D401.
- **File and old text:** `papers/SM.md`, unique at `H`:
  "they hold for every bijection satisfying the six structural properties."
- **Candidate new text** (the plan's own form for the reconstruction class, as in Substratum:104 and ch02:76 at T1′):
  "they hold for every bijection on a finite substratum satisfying the structural assumptions A2–A6
  [Substratum §3.1]."
  - It names A2–A6 rather than counting them.
  - It carries the finite scope that the plan keeps on the reconstruction (F-row principle, `P` §5.1).
  - It reuses no identifier.
  - The wording is for the scientific reviewer to settle.
- **Class:** semantic, outside the 194 sites; site class "consistency correction outside the 194", as in `P` §6.2.
  It needs scientific review.

**What it requires.**

- Append-only amendment text recording the finding and the edit.
- A new `edits.json` and a new `ledger.json`. The splice is in `papers/SM.md`, already a ledgered file, so the ledger
  grows to 400 splices in 44 files and 402 edit records. Their sha256 values change, and so do the next `Record pins`
  rows. No other edit or splice changes.
- Re-running the checkers' battery and the pre-freeze gate. `edits_check` `--static` (register, infinity and
  identifier scans of the new text), `--simulate`, `preserve_check --verify-ledger`, `guards_check --predict` and
  `--mutants`, the coverage check (whether any SM census fingerprint changes; not measured here), and the SC-42
  regeneration.
- `papers/SM.tex` is regenerated (already a ledgered TeX source).
- A new T0″/T1″, which the amendment needs anyway (PROPOSAL.md sec. 6).
- **Effect on PROPOSAL.md's ESC-1:** rule W1-a would leave `w1-w2-allow-v2.json`. Removing an allow rule is not
  widening. The other W1 rules would stay. PROPOSAL.md is not changed here.
- An independent scientific review of the SM:1394 reading and of the new text, and the owner's approval of the
  amendment (§A.50 item 2).

**If review finds (a) instead:** no edit. Under 5.2, SM:1394 joins the exception list with its named set. Under 5.1,
W1-a's reason must cite where that set is defined.

## 7. Limits

- The meaning of each sentence (sec. 4) is a reading of the text, not a proof, and it needs scientific review. Facts
  marked [shown] were checked from git objects in this session, or quoted from the S1 review's control results.
- Item 7's grep scope (`papers/*.md`, `book/*.md`) follows the plan's §4 grep and the design. Item 7 itself states no
  scope. The design notes A6 ordinals such as "the sixth structural assumption" in `verification/README.md:2320` and
  `A6Instantiation.lean:15` at T1′, outside that scope (design sec. 11 note 1, "Scope (O7)"). They are not examined
  here.
- No tool run, CI run or trial was made. The 5.2 control figures come from the same `git grep` counts as sec. 3.
