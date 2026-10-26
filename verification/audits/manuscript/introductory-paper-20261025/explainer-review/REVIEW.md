# Independent re-verification: `EXPLAINER-AUDIT.md` at current main

- **Record:** `verification/audits/manuscript/introductory-paper-20261025/EXPLAINER-AUDIT.md`
  on branch `draft/oi-introductory-paper-20261025` (head `1e9c05c7`), audited at `c91bf5dd`.
  `SHA256SUMS` in the record directory checks OK for all 17 files.
- **Re-checked at:** `main` `687e885b1cfd24d6f17eee439101afc8acf07015`, and replayed at
  `c91bf5dd`. Data dirs were built with `git show`, holding `Explainer.md`, `book/*.md` and
  `papers/*.md`, in `data-c91/` and `data-687/` beside this file.
- **Tools:** the record's own `explainer-tools/shingle.py` and `eqs.py`, copied to `tools/` and
  run with `python3 -I`. I added three helpers there:
  - `shingle_range.py`: per-paragraph 5-shingle overlap against a chosen corpus;
  - `mapline.py`: maps a line at `c91` to the same line at `687` with difflib;
  - `c4ring.py`: an exact sympy check of the C₄-ring claim.
- **Read-only.** No repository file was changed. See the process note at the end for one side
  effect on the shared object store.

## Verdict: HOLDS WITH CORRECTIONS

**Replay at `c91bf5dd`.** The audit's measurements replay exactly:
- its zero-hit greps in `book/` ("Bohr", "homometric", "six-mark", "dimensionful");
- the 41 displayed equations, with 18 not found verbatim;
- the census anchor lines 274/387/421/778/956/982/1281;
- the 58 probe references;
- the 88 commits since 2026-07-25. That count includes merges; it is 49 first-parent.

**At `687e885b`.** The headline finding and the D-gauge gap have been fixed:
- The Explainer's status note no longer names any Explainer-only element.
- #921 put the full D-gauge block into book B.7.

The stale-content list still stands almost entirely, only at shifted lines. The migration
checklist still stands, with shifted lines and one changed landing text.

**Three substantive corrections to the audit itself.** Details are in §5.
- It took the then-current "C₄ ring shows the gap condition fails" claim as content to migrate.
  That claim was false and was later corrected in GR, the book and the Explainer.
- It certified the characterization row as satisfying §A.34. That claim is unsupported.
- It missed the every-horizon form of the characterization at Explainer:378 (now :373).

***

## 1. Per-finding status at `687e885b`

Explainer lines at `687e885b` are 5 below their `c91` numbers from line 8 to about 1059,
because the status note shrank from 6 lines to 1.

| # | Audit finding (at c91) | Status at 687e885b | Evidence (687e885b) |
|---|---|---|---|
| H1 | Status note `Explainer.md:3-8` names two Explainer-only elements; that is no longer true | **Superseded/fixed** (50203701, #926) | `Explainer.md:3` now reads "retained as a supplementary historical exposition … The maintained book and technical papers supersede it". It names no element, so PLAN item 3's premise now refers to text that is no longer there |
| H2 | "frozen … will not be updated" is untrue (88 post-freeze commits) | **Wording fixed; substance holds** | The note no longer says frozen. `book/README.md:110` now says "superseded by this book and the technical papers", where it used to say "as of 2026-07-26 and frozen". The file is still maintained as a mirror: 97 commits touch it since 2026-07-25 (including merges), and `verification/coverage/LEDGER.json:56,70,84,98` still call it "a mirror under AGENTS.md §A.25" |
| 1a | Extent of §5.3, 486-498 | **Holds, shifted** | Heading at 481; paragraphs at 483, 485, 487 and 493; display at 489; solution sentence at 491; `***` at 495. 487 was rewritten (C₄ ring; "comparison" replaces "derivation") |
| 1a | Companion material: Table-2 row 1033; subtlety 3 at 1054-1056; phase-locking at 309-338 | **Holds, shifted, item 3 rewritten** | Row 1028. Subtlety 3 is 1049-1051, now headed "is a conditional theorem" and carrying the full H-BG statement. Phase-locking is 304-333 |
| 1b | Appendix tables at 1001-1040: Table 1 has 8 rows, Table 2 has 15 rows, then the chain | **Holds, shifted** | Section 996-1035: Table 1 at 1002-1009, Table 2 at 1015-1029, chain at 1031-1035. Row 1003 now reads "Under the canonical measure"; row 1021 now reads "per accessible horizon" |
| 2a | Papers carry the D-gauge walkthrough fully and more strictly (GR §3.3, Main §3.1) | **Holds** | `GR.md:168-186`, unchanged except :180 (a sign convention in the exponent) and :182 (the C₄ ring and the transfer item). `Main.md:224-238` is unchanged. GR now also has the thermodynamic-orientation corollary (:188-190) and the coherent-completion classification (:192 ff.), neither of which is Explainer content |
| 2a | Book carries it only partly: Bohr completeness, dimensional obstruction, BG refutation and homometric rulers, C₄ ring and the double-difference display all missing | **Fixed by #921, except the display** | `book/appendix-b-derivations.md:432-452` = `FULL.md:6221-6241`, verbatim (B.7 diffed against FULL 6191-6267: identical). It has B.7.5a (:434-436), the dimensional obstruction (:438), B.7.5b real-to-integer transfer (:440-442), B.7.5c with its conditional proof (:444-446), scope with Bekir–Golomb, the false `BGIntegerClassification`, the rulers, "homometric" and the C₄ ring (:448), and B.7.5d antiunitary invariance (:450-452). `ch03:70` now cites "Appendix B.7". **Still absent from the book:** the explicit double-difference display and its solution δ_ik = α_i + β_k. It is only one clause in B.7.5c's proof ("the phase-coboundary relation fixes the phases", :446), and it is displayed only in `Main.md:232-238` |
| 2b | Summary tables have no tabular counterpart; rows carried in prose | **Holds** | No hits in `book/` or `papers/` for "What it establishes", "What it uses", "Key equation", "What Each Piece Does", "Every link is either" or "Mathematical Summary". Every "summary table" hit is a prediction table: `SM.md:1253`, `ch06:285`, `ch07:290`, `ch19:319`. The nearest prose analogues of the chain are `appendix-b:22` and `:465-476`. Shingle overlap of 996-1035 against the corpus is 0.03 |
| 2b | Prose carriers cited | **Hold, shifted** | B.7 is 402-478. B.4 is unchanged at 169-222. ch07 is 40-63; its prediction table is 292-307, with rows 294-296 and the tier note at 309. The Main ledger is unchanged at 712-722. Coin-and-die is ch01:135-155; Bell is ch01:169-173 |
| 3a | Kernel list: GR:182 omits the real-to-integer transfer | **Fixed** | `GR.md:182` now lists it with `real_to_integer_surrogate`, and B.7.5b carries it |
| 3a | Omissions: GR:184-186 corollary and GR:300 discrete-sampling remark | **Corollary now in book (B.7.5d); remark still GR-only** | `GR.md:300` is unchanged. No "sampling" hit in book in this sense |
| 3a | Notation: δ (Explainer) against φ (Main) | Holds | `Explainer.md:489` against `Main.md:236-238` |
| 3b-1 | Row "§4 … C1 ✓ … C4 ✓" and "satisfying … all conditions" overclaim C4 | **Holds (stale)** | `Explainer.md:1022`, `:411`. §4.2 at 401-408 verifies only C1-C3. Contradicted by `GR.md:52`, `ch07-gravity.md:12` and `:30` ("not presently discharged") |
| 3b-2 | Chain "Every link is either a proof or a calculation" | **Holds (stale)** | `Explainer.md:1035`. Against it: `ch07:294-296` and `:309` (H-slope); `GR.md:74` and `:643`; `GR.md:178` (H-BG); `Main.md:720` (C2 conditional on mixing) |
| 3b-3 | Rows for thermal matching and ε/S_BH carry no condition | **Holds (stale)** | `Explainer.md:1027`, `:1029`. H-slope appears in the Explainer only at :521, and H-balance only at :475 |
| 3b-4 | I ≥ I₀(1−kτ_S/τ_B) presented as an inequality | **Holds (stale)** | `Explainer.md:191`, with "The hidden sector remembers everything" at :193. Against it: `appendix-b-derivations.md:424` ("holds only as a leading-order estimate … generally non-monotonic") |
| 3b-5 | Rows consistent with Main's ledger, "1026 … satisfies §A.34" | **Partly wrong; see §5** | Row 1021 is the "per accessible horizon" slogan. `Main.md:715`/`:717` are prose/probe rows with no kernel witness |
| 3b-6 | Section-number drift; uncited "[10,11]" and "[19]" | **Holds** | 1009 "§3.3" next to "[Main §3.4]"; 1017 "§3.2 Bell"; 1021 "§3.4" against heading 346 "(§3.3)". [10,11] is at 1008 and [19] at 619 (it was 624 at c91, not 627). The Explainer has no reference list |
| 3c | RVM paragraph spliced into the Liouville sentence at :120 | **Fixed** (#919: d5ba48d3, bf550558, a6dee3c0) | `Explainer.md:115` is now "Where the Liouville measure comes from". No "Not a distinctive prediction" remains in the Explainer; that text is at `GR.md:378` and `ch07:211`. Attribution to 3fe27778 not re-verified |
| 4 | 41 displays; the non-verbatim ones are notational variants | **Holds** | `eqs.py`: 41 displays at both commits, with identical FOUND/notfound pattern (18 not found). Positive control: the same shingle tool with `papers/Explainer.md` left in the corpus gives 1.00 on every §5.3 paragraph |
| 4 | Unique content table | **Holds, shifted** (see §2) | Lineage 597-658; Rigidity 759-775 (stale at :771); Decompression 703-748; Weirdness 555-572; FAQ 659-702; Particles 812-865 (heading :854); Subtleties 1039-1055 |
| 4 | Main:66 cites the Explainer's Noether point (Explainer:807) | **Holds** | `Main.md:66`, `Main.tex:545`. Explainer line is now :802. Alternative citation `Substratum.md:408`, in §6.2 (heading :406) |
| 5 | Same-commit dependents | **All still exist**; see §4 | Census lines shifted +16 |

***

## 2. Content that remains Explainer-only (distinctive, not elsewhere in the corpus)

**Method.** Per-section shingle overlap at 687 against all other `book/*.md` and `papers/*.md`
(the record's tool gives values identical to c91 for unchanged sections), plus concept greps over
that same corpus.

**D-gauge walkthrough (§5.3, 481-493): nothing Explainer-only.**
- Overlap is 0.14, and paragraph-level overlap against the book alone is 0.00–0.25. The register
  differs, so comparison was by content, statement by statement:
  - the question (:483) → `GR:170`; B.7.5 proof (:428);
  - Bohr completeness (:485) → B.7.5a (:434-436);
  - the two-branch form, H-BG, the BG refutation, homometric rulers, the C₄ ring and the kernel
    list (:487) → B.7.5c and its scope (:444-448);
  - Ĥ = iħ∂_tU U† and "obligatory" (:493) → `appendix-b:438`;
  - the double-difference display and its solution (:489-491) → `Main.md:232-238`, and only as a
    clause in the book (:446).
- **To make the book self-contained**, the only §5.3 item still missing from the book is the
  explicit double-difference / phase-locking computation. It is a Main §3.1 item, not an
  Explainer-only one, and it should be taken from `Main.md:224-238` if wanted.

**Summary tables (996-1035): the tabular form only.**
- Overlap is 0.02–0.04; no counterpart table exists.
- Every row's content exists in prose (§1, row 2b), and several rows are stale (§3).

**Expository and philosophical content, verified unique at 687.**

| Explainer lines (687) | Content | Evidence |
|---|---|---|
| 597-658 | Philosophical Lineage: the seven claims (601-613), the Claim-4 fault-line survey (639-650), "What's genuinely new" (651-657), and Falque's "wall of Paradise" (631) | Overlap is 0.00–0.10. Hegel, Nietzsche, Nāgārjuna/Nagarjuna, Daoism, Whitehead, Advaita, Falque, Plotinus and "wall of Paradise" have **0 files** outside the Explainer, bibliography included. Kant is only in `Structure.md`. Cusa and Spinoza are in ch00, ch02 and ch03 |
| 703-748 | Decompression algorithm, antimatter as artifact, JPEG/MP3 analogy | Overlap 0.02–0.05. "JPEG" has 0 hits; "decompression" is only in ch03 and FULL. Contains overclaims (§3) |
| 759-775 | "Corroboration: The Rigidity Test", seven checks | Overlap 0.04. "rigidity test" and "seven independent checks" have 0 hits. Stale (§3) |
| 555-572, 659-702 | Quantum-weirdness walkthrough; FAQ | Mostly covered conceptually (ch01:290 cat; Bullet Cluster in GR, ch00 and ch19; double slit in Main, Methodology and Substratum). Unique in register only |
| 886-995 | "What Is (S, φ)?": storage, computation, arrow of time, incompleteness family, why mathematics describes physics | Not treated by the audit. Concept counterparts exist: Gödel, Turing and halting in Substratum, Computation and Complexity and in ch01, ch02, ch03, ch12 and ch14; "unreasonable effectiveness" in Methodology and Substratum; arrow of time in Substratum, GR, SM, ch02, ch03 and ch18; "incompleteness family" in Complexity, Computation, Substratum, ch01, ch02, ch12 and ch14. Overlap is 0.08–0.18. Expository, not unique in substance |

Of this content, only the lineage survey (597-658) is both unique and not stale, as the audit says.

***

## 3. Stale or contradicting content at 687e885b

Do not carry any of these into a replacement.

1. **Every-horizon characterization.** This item is new against the audit.
   - **Explainer sites.** `Explainer.md:373` says "non-Markovian on accessible timescales ⟺ it
     arises, on each finite accessible horizon, from marginalizing a deterministic bijection under
     C1, C3, C4".
   - **Why it is stale.** `Main.md:522` binds (iii) as "for some accessible order k and every
     finite accessible horizon K ≥ k+1". `Main.md:610` says "the unrestricted every-horizon form
     of (iii) is false".
   - **Where it is recorded.** Issue #931, in its comment of 2026-10-26 (#932 review). That
     comment names the same defect at `appendix-b-derivations.md:454-455` = `FULL.md:6243-6244`.
     It is open, needs its own narrow correction, and predates #932.
   - **Related slogan sites.** `Explainer.md:353` ("per finite accessible horizon") and table row
     `:1021` ("per accessible horizon") are the slogan form. The Issue body checked these slogan
     sites and listed them as not affected. If a replacement states the theorem at all, it should
     use Main:522's binding.
2. **C4 at the cosmological horizon.**
   - `:1022` gives "C1 ✓, C2 ✓, C3 ✓, C4 ✓" and `:411` says "satisfying the definition and all
     conditions".
   - Against: `GR.md:52`, `ch07-gravity.md:12` and `:30` (C4 "named …, not presently
     discharged").
3. **Unconditional chain.** `:1035` says "Every link is either a proof or a calculation". Against
   it, the following are conditional:
   - H-slope: `ch07:294-296`, `:309`; `GR.md:74`, `:643`;
   - H-BG: `GR.md:178`; B.7.5c;
   - C2 on mixing: `Main.md:720`.
4. **Unconditioned rows.** `:1027` (thermal matching) and `:1029` (ε, S_BH) carry no condition.
   The maintained rows carry "conditional on H-slope" (`ch07:294-296`).
5. **Memory bound.** `:191`, I ≥ I₀(1−kτ_S/τ_B), is presented as a bound, followed by "remembers
   everything" (:193). Against: `appendix-b:424`.
6. **Rigidity Test.**
   - `:771` says "No free parameters … The lattice spacing is fixed by the gap equation … nothing
     to tune".
   - Against: ε = 2√σ l_p with σ undetermined, in `Explainer.md:525-529` itself, `ch07:80` and
     `GR.md:160`.
7. **Decompression overclaims.**
   - `:745` says "the characterization theorem proves that no other reconstruction is possible —
     this is the unique algorithm". The audit cites this as 752; it was 750 at c91.
   - `:739` says "This resolves … *is the wave function real?*". The audit cites 746; it was 744
     at c91.
   - Against: the antiunitary twofold ambiguity (B.7.5c/d, `GR.md:178-186`) and Main:624's
     representability-not-selection scope.
8. **"No empirical inputs" heading** (`:854`).
   - The paragraph itself names d = 3 and the simple-cubic structure as empirically selected
     inputs.
   - It says the gauge group "follow[s] with no further empirical input" and does not repeat the
     H-link condition it names at `:832`.
   - Against: the glossary (`glossary.md:75`, "Conditionally on H-link") and the parity result's
     H-χ′ dependence.
   - I did not check it in depth against SM.
9. **"Universal hidden-memory theorem"** (row `:1021`).
   - Main's summary claim (2) now carries a formalization status (`Main.md:580`, `:588`, #925):
     the reading of a realization's time-t law as the joint law is not formalized.
   - The Explainer row states it bare. Minor.
10. **Section-number drift and dangling citations.** At :1008, :1009, :1017 and :1021, and [19]
    at :619 (§1, 3b-6).
11. **Subtlety 1.** The "Type II running-vacuum form" check sits in tension with
    `GR.md:378` / `ch07:211`. The audit called this corpus-wide; it was not re-examined.

**Fixed since c91, so no longer stale:**
- the Liouville/RVM splice (:115);
- the measure-uniqueness statements (:96, :109, :113, :417, row :1003);
- BLP backflow, now a one-way witness (:143);
- the C₄-ring sentence (:487) and subtlety 3 (:1049-1051), now conditional theorems in GR's
  wording;
- "accessible horizon" at :353, :373 and :1021 (but see item 1).

The Explainer has no statements touched by #930 (F28, ancilla-assisted witnesses) or by #933
(ch18 unpredictability). Greps for "ancilla-assisted", "unpredict…", "randomness" and "Page time"
find nothing relevant.

***

## 4. Migration checklist: same-commit changes for a replacement, verified at 687e885b

**CI and gate.**
- `verification/lean/edge_rigidity_probe.py`, unchanged since c91. It has 58 lines naming the
  Explainer.
  - It opens `papers/Explainer.md` and `papers/Explainer.tex` by path at 2870-2873, so a missing
    file raises an error.
  - The `_msum` loop at 2917-2923 requires the summary sentence in `papers/Explainer.md`. The
    sentence is present at `Explainer.md:381`, and also at Main:568, ch01:165, ch19:126 and
    FULL:509/5302.
  - The other path references run from 2965 to 9109.
  - It runs in CI as `edge_rigidity` (`.github/workflows/verify.yml:257`).
- `verification/lean-manuscript-census.json`. It lists `papers/Explainer.md` in `manuscripts` at
  line 6, and carries seven Explainer anchors. The lines are now **290, 403, 437, 794, 972, 998
  and 1297** (they were 274/387/421/778/956/982/1281). The anchor texts sit at
  `Explainer.md:377`, `:381` and `:383`.

  | Census line | Family | Explainer anchor | Other anchor files |
  |---|---|---|---|
  | 241 | completion classification … | :381 | GR, Main, FULL |
  | 377 | CT2 | :381 | GR, Main, FULL |
  | 414 | minimal repertoire | :381 | GR, Main, ch01, ch19, FULL |
  | 764 | OI-N passive observation | :383 | Main only |
  | 957 | act 11 | :377 | Main, ch01 |
  | 983 | act 12 | :377 | Main, ch01, ch19, glossary |
  | 1278 | act 45 | :377 | Main, ch01, ch19 |

  - Every family keeps a non-Explainer anchor.
  - Note texts at :298 and :798 also mention the Explainer.
  - `tools/lean_manuscript_census.py:78` globs `papers/*.md`.
  - §A.35 requires the registry to change in the same commit.
- `verification/coverage/LEDGER.json:46-98`. It has four `"paper": "papers/Explainer.md"` entries
  (46, 60, 74, 88), read by `tools/coverage_check.py:52`.
- Glob-based tools, all byte-identical to c91:
  - `tools/staleness_check.py:26-29`;
  - `tools/proof_census.py:82`;
  - `tools/voice_check.py:44`;
  - `tools/dependency_label_check.py:222`;
  - `papers/oi_lattice_code/citation_check.py:17`;
  - `build.sh:12` ("12 papers + book"), `:60` (source-hash stamp) and `:84` (`papers/*.md`).
- Generated artifacts: `papers/Explainer.tex`, whose stamp matches the `.md` sha256 `e1167acd…`
  at 687, and `papers/Explainer.pdf`.

**Manuscript and landing references.**
- `papers/Main.md:66` and `papers/Main.tex:545`: the Noether cross-reference. Repoint it to
  `[Substratum §6.2]` (`Substratum.md:406-408`).
- `book/README.md:110`, whose text has changed: "(superseded by this book and the technical
  papers)".
- `README.md:115`.
- `book/bibliography.md:9` = `FULL.md:6793` (it was 6763).
- `.zenodo.json:26`.
- `LICENSE:28`.
- No file under `tools/` or `.github/` names the Explainer except through the probe.

**Records.**
- **Frozen; leave unchanged:**
  - `round-cc-1-corpus-correction/controls.py:25,193` (the audit says :27);
  - `round-cc-2-corpus-correction/controls.py:27,198`;
  - `act-45-fixed-basis-image/controls.py:27-37`;
  - `round-v3-12-retirement-census/census.json`;
  - `round-v3-14-retirement/ledger.json` and `messages.json`;
  - `verification/certificates/A12P.json`, a legacy record.

  CC-1, CC-2, A45, V3-12 and V3-14 have receipts under `verification/receipts/`.
- **Mutable, wrongly listed as frozen by the audit:**
  - `verification/README.md:315,345,404,1196,1200,1242,1246,1341,1953,1960,1975,2071,2105,2176,2345`.
    This is the root landing page (§A.36). Its mentions describe where past rounds propagated,
    so they may stand as history, but they should be checked, not assumed frozen (§A.42 item 4).
  - `verification/audits/provenance-errata/errata.json:915,965,995,1014,1064,1212`. It is an
    audit record, not a receipt-governed or legacy record. The audit omits line 915.

**Book items.**
- The audit's own recommendation 1 (a B.7.5a section) is **done** by #921.
- Optional items remaining:
  - a ch07 Step-4 back-reference to B.7, which does not exist yet;
  - the double-difference display, from Main;
  - GR:300 and the GR thermodynamic-orientation corollary, if the book is to mirror GR §3.3 fully.
- The tables, if rebuilt as navigation aids, must:
  - use Main:522's witness binding;
  - mark C4 as named and not discharged;
  - mark H-slope, H-BG and the mixing condition;
  - drop the "every link" sentence.

***

## 5. Errors and overclaims in the audit itself

1. **C₄ ring: a false claim carried forward as migration content.**
   - At c91, `Explainer.md:492` and `GR.md:182` said that omitting the gap condition "fails on
     the C₄ ring".
   - The audit restated this in three places: as a "counterexample" (1a), as a book gap ("The C₄
     ring failure of the gap condition", 2a), and in recommendation 1 ("one sentence on … the C₄
     ring").
   - At 2a it checked only that SM Prop. 20 exists ("the counterexample exists as cited").
     Prop. 20 is about reciprocity and T-invariance, not about the two-branch form.
   - The maintained text now says the opposite (`GR.md:182`, `appendix-b:448`,
     `Explainer.md:487`): H̄ lies in the reflection branch, H̄ = −D_s H̄ D_s†.
   - `tools/c4ring.py` confirms this exactly at a = 1, b = 3/10. The spectrum is {±2, ±3/5}
     with degenerate gaps; the loop products are conjugate; the identity holds. A countercontrol
     with an on-site term breaks it.
   - The audit's recommendation would have propagated the false sentence.
2. **§A.34 overclaim.**
   - 3b-5 says the characterization row is consistent, "both directions witnessed at
     `Main.md:715`/`717`, which satisfies §A.34".
   - §A.34 requires separately identified *kernel* witnesses. Those ledger rows cite a prose
     construction, a prose readback lemma and probes; #931 records "Neither direction is in the
     kernel".
   - At c91, Main:522's witness quantifier was itself defective: F29, corrected by #932.
3. **Missed stale statement.** `Explainer.md:378` at c91 (now :373) states the every-horizon form
   that `Main.md:610` already called false at c91 ("the unrestricted every-horizon form of (iii)
   is false"). The audit classed the characterization rows as safe.
4. **Errata confirmed:**
   - `tools/` means `explainer-tools/` (§4 method lines 235, 237);
   - 41 displays, not 42.
5. **Minor line errors at c91:**
   - "wave function real" is at 744, not 746;
   - "unique algorithm" is at 750, not 752;
   - "[19]" is at 624, not 627;
   - round-cc-1 controls are at :25/:193, not :27;
   - errata.json also has line 915.
6. **Classification error.** `verification/README.md` and `errata.json` are listed under "Frozen
   or historical records" but are not receipt-governed or legacy records (§4 above).
7. **Scope gap.** The "What Is (S, φ)?" block (886-995 at 687) is not assessed. On checking it
   has concept-level counterparts, so the "no unique derivation" conclusion is unaffected.
8. **Count method unstated.** "88 commits" counts merges; it is 49 first-parent. This does not
   affect the finding.

The README's "Findings carried forward" were also checked:
- #919 fixed the splice;
- #921 put the D-gauge block in B.7 at `appendix-b:432` and B.7.5c at `:444`.

One wording point in the brief: #921 *added* the block to the book; GR §3.3 still carries it
(it was not "moved").

***

*Process note.* All work was read-only against `S/paper/mainwt`, a sparse linked worktree of
the partial (promisor) clone `S/ppe/repo`, which has five linked worktrees.

**What happened.** Early `git log` and `git log -S` calls that read historical blobs lazily
fetched missing objects from the promisor remote, adding packs. Git printed "Auto packing the
repository in background", which is a `gc --auto` on a shared store with dependents. §A.40
forbids that, so I report it.

**Checks afterwards:**
- `git fsck --connectivity-only` exited 0;
- every worktree HEAD resolves, and every worktree has a clean status;
- the store has 0 loose objects, 49 packs and no `gc.log`.

Every later git command passed `-c gc.auto=0`. A repack keeps all reachable objects, the HEADs
and indexes of all worktrees included. The owner of `S/ppe/repo` should still be told.
