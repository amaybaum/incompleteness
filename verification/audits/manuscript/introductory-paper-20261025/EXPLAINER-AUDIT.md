> **Status: unreviewed audit record.** Its findings are provisional until
> reviewed. Apart from this block, it differs from the auditor's report
> (sha256 f2fedace546787037101196ebf4fd7152a7f84e00b28d857083a69c351a57685)
> only in three scratch-directory phrases replaced by relative descriptions.
> See `README.md`, which also lists two errata in it.

# Audit: what replacing `papers/Explainer.md` would lose

Commit audited: `c91bf5dd84b6415e1c59820ae0333f3b062d10b6` (main). All `file:line` references
are at that commit. `Explainer.md` has 1064 lines. Copies of every `book/*.md` and `papers/*.md`
were extracted to a scratch directory with `git show`. The two search scripts are in
`explainer-tools/` (`shingle.py`, `eqs.py`).

**Headline.** The status note at `papers/Explainer.md:3-8` says two elements are available only
in the Explainer. That is no longer true. The D-gauge walkthrough (§5.3) is carried in full, and
more strictly, by `papers/GR.md` §3.3 and `papers/Main.md` §3.1. It is carried only in part by
the book. The appendix summary tables have no tabular counterpart anywhere, but every row's
content is carried in prose, and several rows are now stale against the maintained sources. The
note's "frozen … will not be updated" is also untrue in practice: 88 commits since 2026-07-25 have
edited the file as a §A.25 mirror, and CI and the census registry depend on it.

***

## 1. Extent of the two elements

### 1a. D-gauge walkthrough: "Frequencies and the D-Gauge Question (§5.3)", `Explainer.md:486-498`

- **Bounds.** Heading at 486; the section ends at 498; `***` at 500. The section has no
  subsections. It has four bold-led paragraphs:
  - 488 **The problem.** $T_{ij}=|U_{ij}|^2$ discards phase.
  - 490 **What is proved (Bohr-frequency completeness).** The return-probability expansion
    $|U_{ii}(t)|^2=\sum|V_{ik}|^2|V_{il}|^2e^{-i(E_k-E_l)t}$, positivity, and linear independence
    of characters.
  - 492 **Conditional two-branch reconstruction.** Covers $m\ge3$, G1–G3 for both
    Hamiltonians, and H-BG. The result is $H'=DHD^\dagger+E_0$ or $H'=-D\bar HD^\dagger+E_0$.
    The paragraph also covers the six-mark exceptional correspondence and its reversal, the
    refutation of `BGIntegerClassification` by a reflected homometric ruler, and the
    $C_4$-ring counterexample ([SM] Prop. 20). It lists what is established independently:
    Bohr-frequency completeness, the real-to-integer transfer, congruent reconstruction and the
    positive six-mode obstruction.
  - 494–496 **One displayed equation**, the double-difference condition
    $\delta_{ik}-\delta_{il}-\delta_{jk}+\delta_{jl}=0 \pmod{2\pi}$, with solution
    $\delta_{ik}=\alpha_i+\beta_k$.
  - 498 **The dimensional obstruction.** $\hat H=i\hbar\,\partial_tU\,U^\dagger$; dimensionless
    data cannot fix $\hbar$, so Step 4 is obligatory.
- **Figures.** None; the Explainer has no figures.
- **Equations.** One display (494) and inline formulas at 490 and 492.
- **Companion material outside §5.3.** It is referenced from the appendix:
  - Table-2 row at 1033.
  - Appendix subtlety 3, "The D-gauge reconstruction requires genericity", at 1054-1056.
  - The phase-locking section, `Explainer.md:309-338`, which carries the $a_{ij}^{kl}$
    coefficients and the double-difference structure in the Main notation.

### 1b. Appendix summary tables: "Appendix: Mathematical Summary Tables", `Explainer.md:1001-1040`

**Table 1, "Sections 1–2: What Each Piece Does"** (heading 1003). Header at 1005. Columns:
*Component | What it establishes | What it uses*. Eight rows, 1007-1014:

| Line | Component |
|---|---|
| 1007 | Definition + Lemmas 1–3 |
| 1008 | Partition-relativity (§1.4) |
| 1009 | Emergent stochasticity (§2.1) |
| 1010 | P-indivisibility proof (§2.3) |
| 1011 | Accessible-timescale lemma (§2.3), "C1–C3, plus C4 holding quantitatively … $I\ge p_0\delta^2/\ln2$" |
| 1012 | Coin-and-die model (§2.4) |
| 1013 | Stochastic-quantum correspondence (§3.1), "Barandes [10,11] or Stinespring" |
| 1014 | Necessity proof (§3.3), "C1/C3/C4 … C2 conditional on the mixing hypothesis" |

**Table 2, "Sections 3–6: The Logical Flow"** (heading 1016). Header at 1018. Columns:
*Step | What it establishes | Key equation*. Fifteen rows, 1020-1034:

| Line | Step |
|---|---|
| 1020 | §3.1 correspondence ($\le n^3$; $S\iff D\iff Q_{\rm fb}$) |
| 1021 | §3.1 phase-locking, under H-BG |
| 1022 | §3.2 Bell analysis |
| 1023 | §3.3 necessity of C1 |
| 1024 | §3.3 necessity of C2 |
| 1025 | §3.3 necessity of C3 |
| 1026 | §3.4 characterization theorem |
| 1027 | §4 cosmological horizon, "C1 ✓, C2 ✓, C3 ✓, C4 ✓" |
| 1028 | §5.1 classical temperature $T_{\rm cl}$ |
| 1029 | §5.2 Step 1, uniqueness |
| 1030 | §5.2 Step 2, boundary-only |
| 1031 | §5.2 Step 3, $\hbar=\beta c^3\epsilon^2/G$ |
| 1032 | §5.2 Step 4, $\beta=1/(4\sigma)$ |
| 1033 | §5.3 Bohr-frequency completeness |
| 1034 | §6 self-consistency, $\epsilon=2\sqrt\sigma l_p$, $S_{BH}=A/4l_p^2$ |

**Trailing chain.** 1036-1040: "Definition → universal $Q_{\rm fb}$ … → $S_{BH}=A/(4l_p^2)$" and
"Every link is either a proof or a calculation. No link requires quantum mechanics as input."

**Adjacent appendix**, which the status note does not name: "Key Mathematical Subtleties",
1044-1060, four numbered items. It is treated under §4 below.

***

## 2. Where the maintained corpus carries each element

### 2a. D-gauge walkthrough

**Papers carry it fully, and in a stricter form.**

| Explainer content | Maintained counterpart | Comparison |
|---|---|---|
| Problem statement (488) | `papers/GR.md:170` (§3.3 "Gauge-fixing and the dimensional obstruction", heading 168) | same question, stated more fully |
| Bohr-frequency completeness (490) | `GR.md:172` theorem, `GR.md:174` proof (Dedekind independence, positivity) | same content; GR states the hypotheses and gives the proof |
| Two-branch reconstruction (492) | `GR.md:178` theorem with H-BG stated explicitly (the μ map on {0,1,4,10,12,17}→{0,1,8,11,13,17}), `GR.md:180` conditional proof, `GR.md:182` scope paragraph (Bekir–Golomb comparison open; `BGIntegerClassification` false with the explicit rulers (0,1,4,10,12,17)/(0,4,6,9,16,17); kernel `twoBranch_of_BGClassification` not established; $C_4$ ring; homometric rulers) | same claims; GR gives the explicit counterexample rulers. The Explainer's "reflecting one of the homometric six-mark rulers" is the same fact: (0,4,6,9,16,17) is the reflection of (0,1,8,11,13,17) |
| Double-difference equation (494–496) | `papers/Main.md:234-238` (φ-notation, "gauge freedom … $\varphi_{ik}\to\varphi_{ik}+\alpha_i+\beta_k$"), `Main.md:224` (Lemma, $n\ge3$, H-BG, G1–G3), `Main.md:230` (six-mark correspondences) | same content in a different symbol (φ, not δ) |
| Dimensional obstruction (498) | `GR.md:176` (full paragraph: energy origin, antiunitary reflection, "mathematically obligatory entry point"), `GR.md:294-298` | same; GR is fuller |
| (not in Explainer) | `GR.md:184-186` Corollary (operational antiunitary invariance, kernel `OIBridge/AntiunitaryInvariance.lean`); `GR.md:300` remark on phase recovery under discrete sampling | maintained material the Explainer omits |
| $C_4$ ring, Prop. 20 | `papers/SM.md:631` | the counterexample exists as cited |

**The book carries it partly.**

- `book/ch03-structural-realism.md:70` = `FULL.md:944` (verbatim, diffed). This is Level G1,
  "D-gauge on the emergent Hamiltonian": $H\to DHD^\dagger$ invisible; energy shift and the
  antiunitary reflection; completeness conditional on H-BG ([GR §3.3]). Further mentions are at
  ch03:108/FULL:982 and ch03:148/FULL:1022.
- `book/appendix-b-derivations.md:426-430` = `FULL.md:6207-6211` (verbatim, diffed). This is
  Lemma B.7.5 (phase locking): $m\ge3$, H-BG, distinct gaps and overlaps for both Hamiltonians;
  gauge = shift + diagonal rephasing + $\hat H\to-\hat H^*$. The proof defers the classification
  to [GR §3.3].
- **Missing from the book.**
  - The Bohr-frequency completeness theorem. "Bohr" has 0 hits in `book/`.
  - The dimensional-obstruction argument. "dimensionful" and "obligatory" have no relevant hits.
  - The `BGIntegerClassification` refutation and the homometric rulers. "homometric" and
    "six-mark" have 0 hits.
  - The $C_4$-ring failure of the gap condition.
  - The double-difference display.

### 2b. Summary tables

Searches for the headers ("What it establishes", "What it uses", "Key equation"), the titles, the
chain sentence ("Every link is either…", "chain from definition") and the phrase "summary table"
found no counterpart in `book/` or `papers/`. **The tabular form is unique to the Explainer.**
Row content is carried as prose:

- **Table 1 and the §3 rows of Table 2.**
  - Book: Appendix B.7, "The lemma chain for emergent quantum mechanics"
    (`appendix-b-derivations.md:402-456`, mirrored in FULL), Lemmas B.7.1–B.7.5 and
    Theorem B.7.6.
  - Coin-and-die: `book/ch01-observation.md:133-153` and `papers/Main.md:178-198`.
  - Bell: `ch01-observation.md:167-171` and `Main.md:354-405`.
  - The status table closest to Table 2's §3 rows is `papers/Main.md:712-722` ("Status ledger
    (theorems and conditions)", Claim | Status | Site). It covers (ii)⇒(i), (ii)⇒(iii),
    (iii)⇒(ii), CP-indivisibility and the necessity of C1–C4. It is the authoritative status
    source for those rows.
- **§5.1–5.2 rows.**
  - Book: B.4 (`appendix-b-derivations.md:169-222`; Steps 1–4 at 175/197/199/205);
    `ch07-gravity.md:40-63`.
  - Papers: `GR.md` §3.1–3.2 (e.g. 132, 144, 160-164).
- **§5.3 row.** See 2a.
- **§6 row.** `ch07-gravity.md:288-290` (table rows for ħ, ε and $S_{BH}$, each "conditional on
  H-slope"); `GR.md:544-546`.
- **Existing book tables are not equivalents.** `ch07-gravity.md:286-301` and `GR.md:542-553` are
  *prediction* tables (observable / predicted / observed), not logical-flow tables.

***

## 3. Stale or contradicting content: what a migration must not bring back

### 3a. §5.3

No contradiction was found against GR §3.3 or Main §3.1. The minor differences:

- **Kernel-proved list.** 492 lists four independently established items, including "the
  real-to-integer realization transfer". `GR.md:182` lists three (it omits the transfer). The
  transfer is the adopted kernel lemma `real_to_integer_surrogate`
  (`verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean:536`; ROADMAP.md:1143), so the
  Explainer is not wrong. A migration should follow GR's wording, or GR should add the item.
- **Hypotheses not stated.** The Explainer does not give the Bohr-frequency hypotheses in §5.3;
  they appear only in subtlety 3 (1056). Its two-branch paragraph says "G1–G3", where GR says
  "distinct nonzero energy gaps and non-vanishing overlaps". These are equivalent for the
  purpose.
- **Omissions.** The operational antiunitary-invariance corollary (`GR.md:184-186`) and the
  discrete-sampling remark (`GR.md:300`) are absent. A migration should take them from GR.
- **Notation.** δ in the Explainer, φ in Main.

### 3b. Summary tables and chain

Five rows or sentences are stale or contradicted, and two internal-reference defects:

1. **Row 1027 "§4: Cosmological horizon … C1 ✓, C2 ✓, C3 ✓, C4 ✓".** This is contradicted by
   `GR.md:52` ("the present paper does not independently demonstrate" the C4 read-write cycle) and
   by `book/ch07-gravity.md:12` and `:30` (C4 "a named realization condition there, not presently
   discharged"). The Explainer's own §4.2 (`406-413`) verifies only C1–C3, and §4.3 (`416`)
   repeats "satisfying the definition and all conditions". Both 1027 and 416 overclaim.
2. **Chain sentence 1040, "Every link is either a proof or a calculation".** This is contradicted
   by the maintained conditionality:
   - ħ, ε and the 1/4 are each "conditional on H-slope" (`ch07-gravity.md:288-290`, `:303`;
     `GR.md:74`, `:643`);
   - phase-locking is conditional on H-BG (`GR.md:178`; the Explainer's own row 1021);
   - the C2 leg is conditional on mixing (`Main.md:720`).
3. **Rows 1032 and 1034 (thermal matching; ε, $S_{BH}$).** They give the results with no
   condition, where the maintained table rows carry "conditional on H-slope"
   (`ch07-gravity.md:288-290`). The Explainer's §5.2 Step 4 body (`464-478`) also never names
   H-slope. It is named only for the 1/4 factor at 526, and "H-balance" appears at 480.
4. **Row 1011 / body 196, $I\ge I_0(1-k\tau_S/\tau_B)$.** The body (`188-197`) presents this as an
   inequality, followed by "the hidden sector remembers everything". The book says the closed-form
   bound "holds only as a leading-order estimate", the CMI being "generally non-monotonic"
   (`appendix-b-derivations.md:424`, B.7.4 *Status*). The table row itself, with the readback
   bound $p_0\delta^2/\ln2$, matches `Main.md:717`.
5. **Rows that are consistent with Main's status ledger**, and so safe to use if re-derived:
   - 1013/1020 ($\le n^3$ external; universal $Q_{\rm fb}$; `Main.md:714-716`);
   - 1014/1023-1025 (necessity; `Main.md:719-722`);
   - 1022 (Bell; `Main.md:356-405`, `ch01:167-171`);
   - 1026 (characterization; both directions witnessed at `Main.md:715`/`717`, which satisfies
     §A.34);
   - 1028-1031.
6. **Section-number drift.** The tables mix numbering schemes. 1014 says "§3.3" next to
   "[Main §3.4]"; 1022 "§3.2 Bell" is Main §3.3; 1026 "§3.4 Characterization" does not match the
   Explainer's own heading "(§3.3)" at 351. The "§4/§5/§6" labels refer to an obsolete
   single-paper layout; the content now lives in GR §2–§5. Citations "[10,11]" (1013) and "[19]"
   (627) have no reference list in the Explainer.

### 3c. Body defect found incidentally

At `Explainer.md:120` a dark-energy paragraph ("**Not a distinctive prediction (removed from Tier
1).** The expansion below is correct but universal: … $B(H^2-H_0^2)^2$ …") is spliced into the
middle of the Liouville-measure sentence ("…invariant under Hamiltonian flow. [RVM paragraph] With
that said: any smooth initial distribution evolves toward it."). It was introduced by `3fe27778`
(2026-08-23, "Update files"). The paragraph's proper home is `GR.md:378` and
`ch07-gravity.md:205`. This is evidence that the file has drifted under mechanical propagation
edits.

***

## 4. Other Explainer content with no counterpart elsewhere

**Method.**

- Per-section 5-word-shingle overlap of the Explainer against all other `book/*.md` and
  `papers/*.md` (`tools/shingle.py`).
- Verbatim lookup of every one of the 42 `$$…$$` displays after whitespace normalization
  (`tools/eqs.py`). Each display not found verbatim was then checked by hand for a notational
  variant.
- Concept greps on names and terms for every section with low overlap.

Most sections have low verbatim overlap because the register is popular, but concept-level
counterparts exist. Every derivation display either has a counterpart or is a trivial variant:

- 188/192 ($e^{-\Delta\tau_S}$): the substance is in `ch01:121` and B.7.4;
- 364 (TV bound): `Main.md:433-447`;
- 374: `Main.md:490`;
- 452: `GR.md:132`;
- 261/267/728 ($\Lambda(2,1)$): `ch01:147-148`, `Main.md:188-190`;
- 494: `Main.md:234-238`;
- 524: `GR` §5, `ch07`.

**No unique derivation, worked example or mathematical table was found.** The unique content is
expository or philosophical:

| Lines | Content | Nearest counterpart | Assessment |
|---|---|---|---|
| 602-663 | Philosophical Lineage: "seven claims" list (606-618); the Claim-4 fault-line survey (644-655): Kant, Hegel, Nietzsche, Nāgārjuna, Daoism, Whitehead, Advaita; Falque's "wall of Paradise" (636); "What's genuinely new" (656-662) | Cusa and Spinoza at `book/ch03-structural-realism.md:194-204`, `ch00:71`. Hegel, Nietzsche, Nagarjuna, Whitehead, Advaita, Falque and Plotinus have **0 hits** outside the Explainer and the bibliography | unique; non-technical. The Explainer says it draws on "a systematic analysis" (997) |
| 764-780 | "Corroboration: The Rigidity Test", the seven-check enumeration (774) | SM §4.1 / `Substratum.md:48,104,144` | unique framing, **stale**: "No free parameters … The lattice spacing is fixed by the gap equation … nothing to tune" (776) contradicts ε/√σ = 2 l_p with σ undetermined (`Explainer.md:530-534` itself; `ch07:80`; `GR.md:160`) |
| 708-753 | "Decompression Algorithm", "Antimatter as algorithmic artifact", the JPEG/MP3 analogy | `ch03` (one mention); $\Lambda(2,1)$ in ch01 | unique interpretive prose; overclaims ("no other reconstruction is possible — this is the unique algorithm", 752; "resolves … is the wave function real", 746) that sit against the maintained antiunitary twofold ambiguity and the (T) scoping |
| 560-577, 664-707 | "What Quantum Weirdness Looks Like" (double slit, entanglement, measurement, cat); FAQ (10 Qs) | `ch01:288` (cat), `ch00`/`ch19`/`GR` (Bullet Cluster), Appendix C objections | mostly covered; register-specific |
| 817-870 | "Why These Particles?" | SM, book ch05–06 | covered. Not checked in depth: the "No empirical inputs" heading (859) may be stronger than the maintained H-χ′/H-link conditionality (`Complexity.md:109`; FULL:5538) |
| 1044-1060 | Key Mathematical Subtleties 1–4 | 1 → `GR.md:162`, `ch07:63`; 2 → `GR.md:164`, `SM.md:164`, `appendix-c-objections.md:261`; 3 → `Main.md:256`; 4 → `GR` §3.2, B.4.1 | covered. Item 1's "Type II running-vacuum form" check is also in GR:162 and ch07:63, which are in tension with GR:378 and ch07:205 ("not a distinctive prediction"); that is a corpus-wide issue, not an Explainer-only one |

Also unique, but as a *target*: `Main.md:66` cites "the companion Explainer draws via Noether's
theorem" the information↔energy link (`Explainer.md:807`). The same point is in
`Substratum.md:408` (§6.2), which Main could cite instead.

***

## 5. Files that a replacement of `papers/Explainer.md` would affect

**Live, gate-relevant.** These must be updated in the same change:

- **`verification/lean/edge_rigidity_probe.py`**: 58 references. It opens `papers/Explainer.md`
  and `papers/Explainer.tex` by path (e.g. 2870-2873, 2921, 2965, 2990-2992, … 9109) and asserts
  specific summary sentences in them; e.g. `_msum` at 2918-2923 must appear in
  `papers/Explainer.md`. It runs in CI (`.github/workflows/verify.yml:257`, `edge_rigidity`). A
  missing file raises an error; changed text fails the assertions.
- **`verification/lean-manuscript-census.json`**: `papers/Explainer.md` is in `manuscripts`
  (line 6). It is also an anchor file in seven families:
  - "completion classification…" (274)
  - CT2 (387)
  - minimal repertoire (421)
  - OI-N passive observation (778)
  - act 11 (956)
  - act 12 (982)
  - act 45 (1281)

  The anchors sit at `Explainer.md:382`, `386` and `388`. Every family keeps anchors in Main
  and/or GR, so none would be left without an anchor. "OI-N" has no book anchor; Main carries it.
  Under §A.35 the registry changes in the same commit. `tools/lean_manuscript_census.py:78` globs
  `papers/*.md`.
- **`verification/coverage/LEDGER.json`**: 46-98, four entries with `"paper":
  "papers/Explainer.md"`, each noted "a mirror under AGENTS.md §A.25". Read by
  `tools/coverage_check.py`.
- **Glob-based gate tools**, which pick up any new `papers/*.md` automatically and drop the
  Explainer on removal:
  - `tools/staleness_check.py:26-29` (.md↔.tex hash);
  - `tools/proof_census.py:82`;
  - `tools/voice_check.py:44` (§A.32/33 voice; an introductory paper will be scanned);
  - `tools/dependency_label_check.py:222`;
  - `papers/oi_lattice_code/citation_check.py:17`.
- **`build.sh`**: globs `papers/*.md` (84), and its comment at 12 says "12 papers". It appends
  the source hash to the `.tex` (60). `papers/Explainer.tex` and `.pdf` must be regenerated or
  removed with the source.

**Manuscript and landing references.**

- `papers/Main.md:66` (and `papers/Main.tex`): the Noether cross-reference above.
- `README.md:115`: "older overview, superseded by the book and retained for reference".
- `book/README.md:110`: "**Explainer** (superseded by this book as of 2026-07-26 and frozen)".
- `book/bibliography.md:9` = `FULL.md:6763` (mirror): "the companion documents Explainer,
  Complexity, …".
- `.zenodo.json:26`: the same list.
- `LICENSE:28`: names `Explainer.md`.

**Frozen or historical records.** Leave these as they are (§A.39, §A.42 item 4):

- `verification/README.md` (315, 345, 404, 1196-1246, 1341, 1953-1975, 2071-2176, 2345);
- `verification/audits/provenance-errata/errata.json` (965, 995, 1014, 1064 page count, 1212);
- round controls that hard-code the path: `round-cc-1`/`round-cc-2` `controls.py:27`;
  `act-45-fixed-basis-image/controls.py:27-37`;
- retirement ledgers `round-v3-12`/`v3-14`;
- certificates `A12P.json`;
- many propagation audits and preregistrations (full list:
  `git grep -c Explainer c91bf5dd`).

Frozen controls that read `papers/Explainer.md` would not re-run on a tree without it. That is
expected for frozen records, but it should be noted in the change.

***

## 6. Recommendation

**Must be migrated before replacement.**

1. **D-gauge walkthrough, into the book.** Nothing needs to be rescued from the Explainer:
   GR §3.3 (`GR.md:168-186`, `294-300`) is the authoritative and more complete source. To keep
   the book self-contained, extend Appendix B.7 with a short "B.7.5a Bohr-frequency completeness
   and the dimensional obstruction" next to Lemma B.7.5 (`appendix-b-derivations.md:426-430`).
   It should cover:
   - the GR theorem and proof;
   - the dimensional-obstruction paragraph (`GR.md:176`);
   - one sentence on the H-BG scope ending (`GR.md:182`): the open Bekir–Golomb comparison, the
     false `BGIntegerClassification`, and the $C_4$ ring.

   Optionally add a back-reference at `ch07-gravity.md` Step 4. Mirror the edit into FULL.md
   (§A.14). Write it from GR, not the Explainer. This is the only element the book truly lacks.
2. **Cross-reference repairs** in the same change:
   - repoint `Main.md:66` to `[Substratum §6.2]`, and rebuild Main.tex;
   - update `edge_rigidity_probe.py` and the census registry's `manuscripts` entry and seven
     anchors;
   - update `coverage/LEDGER.json`;
   - update README.md, book/README.md, bibliography.md + FULL.md, .zenodo.json and LICENSE;
   - check `build.sh`'s paper count.

   If the replacement keeps the filename `papers/Explainer.md`, the census anchors and the
   probe's `_msum` sentences must either be carried by the new paper or be removed from the
   registry and probe deliberately.

**Optional migration.** The summary tables are worth having in the book as a navigation aid,
for example as "B.1a Logical-flow summary" in Appendix B, or as a reader's-guide table. Rebuild
them from the maintained sources, not by copying:

- statuses from `Main.md:712-722` and `ch07-gravity.md:286-303`;
- C4 at the cosmological horizon recorded as named, not discharged;
- ħ/ε/$S_{BH}$ as conditional on H-slope;
- phase-locking as conditional on H-BG;
- section numbers as current [Main]/[GR] sections;
- no "every link is a proof or a calculation".

**Preserve as a frozen historical file, or drop.** If the owner wants provenance, the existing
Explainer can be kept under a new name with a standing "superseded and frozen" notice (§A.27
allows this). Strictly, though, the repository history already preserves it, and §A.28 argues
for dropping it. If it is kept, stop treating it as a §A.25 propagation mirror: take it out of
the census, the probe and LEDGER. Otherwise "frozen" stays false, as the 88 post-freeze commits
show.

**Drop, and do not carry into any introductory paper.**

- the Rigidity Test's "no free parameters / nothing to tune" (764-780);
- the decompression section's uniqueness and "wave function resolved" claims (708-753);
- the C4 ✓ row and the "all conditions" sentence (1027, 416);
- the unconditional chain (1040);
- the $I\ge I_0(1-k\tau_S/\tau_B)$ inequality presented as a bound (196);
- the spliced RVM paragraph (120).

The philosophical-lineage survey (602-663) is the one piece of unique, non-stale content. If the
owner values it, it belongs in `book/ch03-structural-realism.md` near 194-204, in essay register.
Otherwise it can go with the frozen file.

***

*Process note.* The audit was read-only, with one side effect. An early `git log -L` in the
scratch clone started git's automatic background repack
("Auto packing the repository…"). The clone is standalone: it has no `objects/info/alternates`
and no linked worktrees. A repack rewrites only pack files and does not change refs or objects.
Every later command passed `-c gc.auto=0`.
