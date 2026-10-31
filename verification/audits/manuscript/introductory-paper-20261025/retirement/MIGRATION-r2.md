# Explainer content-migration audit, revision 2

Revision 2 applies the independent review `S/paper/retire-review/REVIEW.md` (ACCEPT WITH CHANGES):
RC6, RC7 and nits F3/F4. It also records the owner decisions of 2026-10-26. `MIGRATION.md`
(revision 1) is kept unchanged as the reviewed object; `CHANGES-r2.md` lists every change.

**Owner decisions recorded (2026-10-26).**
- The retirement strategy is approved, conditional on independent review and acceptance of the
  Introduction.
- The move to `papers/legacy/` is approved, to happen after acceptance.
- A superseded notice is required.
- `Main.md:66` → `[Substratum §6.2]` is approved.
- The shape is one PR with two commits.
- Safeguards: (S1) historical reproducibility; (S2) a minimal redirect at `papers/Explainer.md`.
  Both are carried in RETIREMENT-r2.md.

Planning document. No repository file is changed. All `file:line` references are at `main`
`687e885b1cfd24d6f17eee439101afc8acf07015` (the worktree `S/paper/mainwt`) unless marked otherwise.
`papers/Explainer.md` has 1059 lines, sha256 `e1167acd…ce9d83` (matching the stamp in
`papers/Explainer.tex`).

**Inputs used.**
- The whole Explainer, read section by section (every heading from :1 to :1059), not only the
  REVIEW list.
- `S/paper/explainer/REVIEW.md` (re-verification of `EXPLAINER-AUDIT.md` at `687e885b`; verdict HOLDS
  WITH CORRECTIONS). Its stale list is cited below as **R3.n** (REVIEW §3 item n).
- The outline. **The governing revision is OUTLINE-r4** (`S/paper/design/OUTLINE-r4.md`). This
  audit was drafted against r2 (`OUTLINE-r2.md`, `CONTRIBUTION-r2.md`, `SOURCES-r2.md`), and the
  claim IDs (`§3-a` etc.) are r2's. r4 keeps them stable: "The section numbering of the claim
  register is kept, so that claim IDs stay stable" (OUTLINE-r4.md:72–73). r4's "What the paper must
  not inherit" list equals REVIEW §3. Where r3/r4 change something relevant, it is noted in §4.
- Novelty classes from `novelty-v5/AUDIT.md` (AUDIT r4; read at the audit branch head `1e9c05c7`,
  not on `main`; the applied text was not itself re-checked, per OUTLINE-r2 "Inputs"). Cited
  `AUDIT:NNN`. AUDIT:129–130 already records: "The Explainer is superseded, and it is not a drafting
  source for the introductory paper."

**Classes.**
- **(a)** already carried in the maintained corpus → no action (counterpart cited).
- **(b)** unique and essential → migrate (destination, justification, source lines).
- **(c)** unique-but-not-essential, or redundant → not migrated (§A.28).
- **(d)** stale or unsupported → must not be carried anywhere (contradicting authoritative source
  cited).

A section can be (a) in substance and still contain (d) sentences; both are listed.

***

## 1. Result

1. **Nothing migrates into the Introduction from the Explainer.** Class (b) is empty for the
   Introduction. Every Introduction claim in OUTLINE-r2 is sourced from Main, GR, the BH packages or
   the kernel (SOURCES-r2), and the Explainer adds no statement the outline needs. This agrees with
   AUDIT:129–130 and SOURCES-r2 "Decision 7".
2. **Nothing migrates into Main.** The one Main change is a dependent repair, not content:
   `Main.md:66` (and `Main.tex:545`) cites "the companion Explainer" for the Noether
   information↔energy link. The same point is at `Substratum.md:408` (§6.2, heading :406). Repoint to
   `[Substratum §6.2]`, Main's own citation style (cf. `[Substratum §3.3]`). This lands in the
   retirement commit (RETIREMENT.md step 2).
3. **Nothing is required in the book.** The D-gauge walkthrough is already in book B.7
   (`appendix-b-derivations.md:432–452` = `FULL.md:6221–6241`, from #921). Three *optional* book items
   exist, all owner choices and none needed for retirement:
   - the explicit double-difference display, taken from **Main** (`Main.md:232–238`), not from the
     Explainer, into B.7.5c (`appendix-b:444–446` + FULL mirror). This is Main content, so it is not
     an Explainer migration;
   - a navigation table (§3 below: **not recommended**);
   - a philosophical fault-line paragraph in ch03 §3.8 (§2, row 22: **not recommended as written**);
   - a holography objection in Appendix C (§2, row 23a: owner option; default (c)).
4. **Unique content, on its merits.** The REVIEW's four Explainer-only items are:
   - the appendix summary tables (form only);
   - the philosophical-lineage survey;
   - the decompression section;
   - the Rigidity Test.

   Walking the whole file adds a fifth: the holography/Ryu–Takayanagi FAQ answer (row 23a), (c) by
   default with an owner option for book Appendix C.

   Their dispositions: the tables are superseded, conditionally (§3). The lineage survey is (c), with a stale thesis
   at its centre. The decompression section and the Rigidity Test are (d).
5. **The (d) list is longer than REVIEW §3.** Walking the whole file adds further stale or unsupported
   statements, marked **NEW** in eighteen rows of §2, beyond REVIEW's eleven. None may enter the Introduction,
   Main or the book from this source. Several of them already have correct statements in the
   maintained corpus. The rest sit only in the Explainer, and leave the active corpus when it is
   retired.

***

## 2. Section-by-section classification

"AUDIT class" is the class a claim would carry if any maintained document restated it; it matters
for the "known results not presented as novel" rule. The Explainer presents several AUDIT-KNOWN
results as "the paper's" own proofs (rows 7, 11, 14). No migration may carry that framing.

| # | Explainer lines | Section / element | Class | Counterpart, destination or reason | AUDIT class / notes |
|---|---|---|---|---|---|
| 1 | 1–10 | Title, status note (:3), subtitle "Why Physics' Biggest Contradiction…", byline "March 2026" | (c) | Replaced by the standing notice in RETIREMENT.md §3. Title and subtitle not reused | Introduction title is owner item R1 (OUTLINE-r2 "Positioning") |
| 2 | 12–24 | "The Worst Prediction in Physics": 10¹²² as "strongest piece of existing evidence" that QM is emergent (:22) | (a) substance; (d) framing | CC problem and compression ratio: `GR.md:358–370`, `:366`; `ch07-gravity.md:191`. **(d) NEW:** the superlative at :22, "strongest piece of existing evidence" that QM is emergent. `GR.md:358` lists the CC dissolution as one item of "cumulative evidence for the ordering", and `GR.md:360` says "The framework does not explain *why* ρ ∼ H²/G; this is set by initial conditions". Under §A.23 a match to an already-known value is a retrodiction, not a correctness confrontation. The (d) rests on the superlative; the dissolution itself is (a) at GR:358 | Not in Introduction scope (OUTLINE-r3 "Gap in coverage, accepted by design") |
| 3 | 28–66 | Starting point: definition (:38), two/three-axiom note (:42), Lemmas 1–3 (:44–56), layered summary (:58), C1–C3 (:60–64) | (a) | Definition and Lemmas: `Main.md:44–62`. Two axioms: `Main.md:34–38`, `Methodology.md:31`. Layered summary: `Main.md:16–22`, `:534`, `:542`. C1–C3 incl. the fast conserving bath: `Main.md:72–80`. :42's "it is under review" is process narration and is not carried | Definitions, n/a. Introduction §2-a, §2-b source Main directly |
| 4 | 70–88 | "The Observer's Blind Spot": horizon, trace-out, coupled/slow/vast (:82–86), "it is the feedback (C4) that does the work" (:88) | (a) | `GR.md:36–52` (§2.1–2.2), `Main.md:103–109`. :88 agrees with `Main.md:722` (C4 load-bearing) | — |
| 5 | 92–115 | Partition-relativity (formula :100, proof :113, Liouville/measure :115) | (a) | `Main.md:84–93`, measure remarks `:56–60`; `invariance_does_not_select` (CanonicalMeasure:242) per OUTLINE-r2 §2-c | (e) per AUDIT:331 (#919) |
| 6 | 119–129 | Emergent stochasticity, slow bath | (a); (d) one sentence | `Main.md:103–109`; ch01. **(d) NEW:** :129 "It's the key ingredient that separates quantum mechanics from classical stochastic processes" against `Main.md:534` / OUTLINE-r2 §3-f (the representation is universal and includes Markov laws) | — |
| 7 | 133–169 | P-indivisibility theorem, Steps 1–3, BLP backflow (:143) | (a) theorem; (d) three sentences | Theorem and proof: `Main.md:111–141` (hypothesis "If T is not a permutation matrix", :119). **(d) NEW:** :135 (genuine coupling ⟹ P-indivisibility), :169 ("the proof uses … that the coupling is non-trivial (C1)") and :272 ("needs only coupling (C1) and finiteness"). All three contradict the theorem's own non-permutation hypothesis, which :161 itself states, and `Main.md:719` (C1 row: "a non-permutation one-step T is the sufficient first-step witness, not an equivalence") | **C8 KNOWN** (RHP 2014 Thm 2.4 "only if"; BD Prop. 1; AUDIT:821–905). "QED" as the paper's own result must not be carried |
| 8 | 173–195 | Accessible-timescale lemma: $I\ge I_0(1-k\tau_S/\tau_B)$ (:191), "remembers everything" (:193) | (d) | **R3.5.** Against `appendix-b-derivations.md:424` (leading-order estimate; CMI generally non-monotonic). The maintained readback lemma is `Main.md:167–170` ($I\ge p_0\delta^2/\ln2$), Introduction §4-d | C9 REFRAMING, PROVISIONAL (AUDIT:1114–1124) applies to Main's form only |
| 9 | 199–268 | Coin-and-die model, $\Lambda(2,1)$, mechanism (:266) | (a) | `Main.md:178–196`; `ch01-observation.md:135–155`. Introduction §5-b sources Main and must state the $x_0$ law (OUTLINE-r2 §5-b). :227 "C2 … τ_S/τ_B = 1/2 ✓" is a loose gloss; not carried | Not classified (illustration) |
| 10 | 270–274 | "Why C2 and C3 matter physically" | (a); (d) one sentence | `Main.md:72–80`, `:172` (zero-backflow coin), `:722`. :272 is **(d)** (row 7) | §4-f source is Main:172 |
| 11 | 278–300 | Stochastic-quantum correspondence; Born form; Schrödinger; ħ; Bell bullet | (a) core; (d) three items | Correspondence: `Main.md:202–256`, Stinespring `:258–352`. Born dictionary and exponent non-selection (:296): `Main.md:534`, outline §3-g. Bell (:300): `Main.md:354–405`. **(d):** (i) "dimension ≤ n³" (:282, :1015) is F13, unresolved and excluded (CONTRIBUTION-r2 (c)8; AUDIT:1872–1918). (ii) **NEW:** :294 claims "the framework's realized processes supply exactly such a group … (the fixed-Ĥ lemma)" and calls this "the answer that wasn't available in 1963". This is the F3 remark (Main:532 "fixed autonomous generator"), which the outline excludes as open/contentless (OUTLINE-r2 §3-d; AUDIT:1551 F3). (iii) **NEW:** :286 "This is the Born rule … a mathematical identity", presented as a derivation, against `Main.md:534` (the quadratic readout is part of the definition of $Q_{\mathrm{fb}}$) | **C2 KNOWN** (Barandes B25/B23/B26; AUDIT:572–586); §3-g KNOWN (B26 Thm 3.1) |
| 12 | 304–330 | Phase-locking lemma | (a) | `Main.md:224–238` (display :232–238); `GR.md:168–186`; B.7.5 `appendix-b:426–452` | Outside the Introduction's scope (OUTLINE-r3 part 2: "phase-locking is outside this paper's scope"). Not classified in AUDIT r4 |
| 13 | 334–342 | Bell inequality violations (incl. H-Bell curvature paragraph :340, Hall–Branciard, Tsirelson layer) | (a); (c) caps | `Main.md:354–405` (0.0309409 bits at :403; ontic parameter dependence :392); hop-metric/curvature: `SM.md` §3.2, `Substratum.md:132`. ":340 FAILS" is caps emphasis (§A.33), not carried | Introduction §8-h sources Main:360–377, :392–394 |
| 14 | 346–385 | Characterization theorem block | mixed | See 14a–14i | — |
| 14a | 348–353 | Logical chain, combined biconditional (:353) | (d) as displayed | **R3.1** (slogan form) and C12: (ii)⟺(iii) is prose in both directions with no kernel witness (`Main.md:608`), so it cannot be displayed (§A.34; OUTLINE-r2 "Not to be displayed"). :352 "necessity, unconditional" is consistent with `Main.md:719–722` for C1/C3/C4 | **C12 REFRAMING, near-definitional** (AUDIT:1191–1207) |
| 14b | 355–371 | Necessity of C1, C2 (conditional), C3 (DPI chain :369) | (a) | `Main.md:719–722`; C3 kernel `c3_necessity` (outline §4-c); C2 conditional `Main.md:720` | C11 REFRAMING, PROVISIONAL (AUDIT:1182–1188) |
| 14c | 373 | "Complete characterization": every-horizon form; "Both directions are the foundational paper's own theorems"; "The old three-way biconditional is retired" | (d) | **R3.1**: against `Main.md:522` (bound: some accessible order k, every finite horizon K ≥ k+1) and `Main.md:610` ("the unrestricted every-horizon form of (iii) is false"). F5/F26 open at this site (AUDIT:1226–1230, :1552, :1569). "is retired" is self-narration (§A.30) | Issue #931 |
| 14d | 375 | What "unitarily evolving QM" means (layer statement) | (a) | `Main.md:534`, `:542`, `:562`; GR §3.3 | — |
| 14e | 377 | Relating evolution not fixed; two-sided gauge; fibre-Gram residue; `bridge_traj` | (a) | `Main.md:624` (census families act 11/12/45 anchor Main and ch01) | Introduction §6-b carries only the kernel-scoped parts. The fibre-Gram classification and ancilla remark are excluded (UNTRACED-1) |
| 14f | 379 | Three statuses | (a) | `Main.md:624` closing; GR, Methodology, ch19 (probe E16) | Introduction §6-c |
| 14g | 381 | "Proved versus imported"; OI⁺, primitive-source, substratum-source, typed, Level III quasilocal completion, layer-flow, sourcing | (a) | `GR.md` §3.3 (168–300) and `Main.md` §3.4 summaries; ch01, ch19, FULL. These are the census-anchored summary sentences (RETIREMENT.md step 2) | Alt-X only (E4); not in the recommended scope |
| 14h | 383 | Passive observation, kept apart (OI-N) | (a) | `Main.md:570` | Not classified |
| 14i | 385 | Uncertainty relations | (a) | `Main.md:572` | Introduction §1-d |
| 15 | 389–411 | Cosmological application (partition, ħ universality :399, C1–C3 verification, "all conditions" :411) | (a); (d) one sentence | `GR.md:36–60`. **(d):** **R3.2**, :411 "satisfying the definition and all conditions" against `GR.md:52` (C4 not independently demonstrated) and `ch07-gravity.md:12`, `:30` | — |
| 16 | 415–477 | ħ: classical temperature, four steps, non-circularity, "predictive content" (:477) | (a); (d) three items | `GR.md:94–166`; `appendix-b:169–222` (B.4); `ch07-gravity.md:40–63`. **(d):** **R3.3/R3.4**, Step 4 states no H-slope condition (against `GR.md:12`, `ch07:294–296`). **NEW:** :465 "Since the quantum description is derived from the classical one (Part I)", against `Main.md:616` (representation, not explanation) and `:624`. **R3.11:** :477 lists the "Type II RVM dark-energy form" as a check, in tension with `GR.md:378` / `ch07:211` (not a distinctive prediction) | Not in Introduction scope |
| 17 | 481–493 | D-gauge walkthrough (§5.3): problem, Bohr-frequency completeness, two-branch reconstruction under H-BG, C₄ ring, double-difference display (:489–491), dimensional obstruction (:493) | (a) | REVIEW §2: statement by statement. Problem → `GR.md:170`. Bohr completeness → `GR.md:172–174`, B.7.5a `appendix-b:434–436`. Two-branch, H-BG, `BGIntegerClassification` refutation, rulers, C₄ ring → `GR.md:178–182`, B.7.5c `appendix-b:444–448`. Display → `Main.md:232–238` (book: one clause at `appendix-b:446`). Dimensional obstruction → `GR.md:176`, `appendix-b:438`. **Nothing Explainer-only.** The C₄-ring sentence at :487 is the corrected one (REVIEW §5.1) | Not an Introduction item. Before any later use of Bohr completeness or the two-branch theorem in a paper, it needs an AUDIT class (none assigned: AUDIT:329, "not an intro-paper candidate") |
| 18 | 497–527 | Discreteness scale; S_BH and the 1/4; "what self-consistency does not bound" | (a); (d) one sentence | `GR.md:304–324`, `:160`; `ch07-gravity.md:80`. **NEW (d), mild:** :523 "The 1/4 factor has been a mystery for 50 years … Most frameworks either assume it…" is an unsourced literature characterization (self-assessment, §A.32 in a paper). The maintained statement is `GR.md:12` | — |
| 19 | 531–551 | "The Two Levels": locality inheritance, Level 1/2, three ordering requirements, 10¹²² as compression ratio, "track record" | (a); (d) two items | `GR.md:326–370` (§6); `Substratum.md:330–338` (§5.2); `ch07:191`. **(d) NEW:** :551 "one ordering … predicts the observed value" and :549's "the framework explains why", against `GR.md:360` ("does not explain *why* ρ ∼ H²/G; this is set by initial conditions"). :549's "sits exactly at the classical geometric scale" is close to `GR.md:358` ("sits at ρ ∼ H²/G, the classical baseline, without fine-tuning") and is not itself (d) | — |
| 20 | 555–569 | "What Quantum Weirdness Looks Like From Here": double slit, entanglement, measurement, Schrödinger's cat, Feynman quotes | (a) concept; (c) register; (d) framing | Double slit, Wigner's friend: `Main.md:662–676` (§4.1; Wigner :670–676). Cat: `ch01-observation.md:290–294` (§1.11). Entanglement/Bell: `Main.md:354–405`. **(d) NEW:** :559 and :561 ("the mystery dissolves … into a derivation") and :569 ("the rules … have to be derived") against `Main.md:616`, `:624` and CONTRIBUTION-r2 (c)1 | Interpretation, (e) not classified (AUDIT:1455). Owner-part 3 candidate: see §4 |
| 21 | 573–593 | Predictions (dark energy, dark sector, high-z, clusters/Bullet, neutrinos, gauge couplings, Brandner/Mehl/Gröblacher/Kim, closing claim) | (a) substance; (d) five items | Dark energy `GR.md:376–416`; dark sector `:418–464` (LZ :458); MOND/clusters/Bullet `:466–536`; neutrinos `papers/Juno.md`, `SM.md` §7, `appendix-a-prediction-status.md` A.4.3; couplings `SM.md:1259–1261`; Brandner/Mehl/Gröblacher `Main.md:214`, `:808–810`. **(d) NEW:** (i) :585 says the cluster residual is "attributable to undetected warm-hot intergalactic medium (WHIM)", against `GR.md:528` ("the residual is **not** closable by undetected cluster baryons"). (ii) :589 says "reproduces all three SM gauge couplings … < 0.1%" without noting that $1/\alpha_1$ is an input (class **E**, "fixes δ₀"), against `SM.md:1259`. (iii) :591 says the "central technical move … which under the Barandes correspondence becomes quantum mechanics — is now established at theorem level". It attaches "QM" to Brandner's theorem, against `Main.md:624` (representability, not derivation). (iv) :581 "independent corroboration" and :593 "No competing framework produces all of these" are self-assessment and consistency-as-correctness (§A.23). (v) :587 "every directly comparable measurement matches" / "exactly the structural mismatch that the OI dark energy resolves" is unsupported by `GR.md:376–416` | Not in Introduction scope |
| 22 | 597–657 | Philosophical Lineage (seven claims :601–613; Gödel :615–625; Cusa :627–631; Spinoza :633–637; Claim-4 fault line :639–649; "What's genuinely new" :651–655) | (a) partly; (c) remainder; (d) the thesis | Already in the book: Cusa, Spinoza, Worrall, Hofstadter, Gödel/Turing/Wolpert, observer programmes at `ch03-structural-realism.md:190–231` (§3.8); T. Breuer at `GR.md:366`, `ch07:195`; Wolpert at `Main.md:40`, `ch03:214`. Unique remainder: the seven-claims list, the Kant/Hegel/Nietzsche/Wittgenstein/Nāgārjuna/Daoism/Whitehead/Advaita survey, Falque's "wall of Paradise", "What's genuinely new". **(d) NEW:** the survey is organised around Claim 4, "The underlying reality is **local** and definite" (:608). That contradicts the adopted Bell branch, `Main.md:392` ("at the microstate level, one wing's response depends on the remote setting"; also `Substratum.md:122` M1-B). :655's "Gödel → Wolpert → causal partition chain" contradicts :621 ("not a derivation in which each implies the next") and `ch03-structural-realism.md:214` ("the logical results corroborate the framework's derivation but do not supply it"). :619 cites "[19]" with no reference list (R3.10). The survey's source, "a systematic analysis" (:992), is not in the repository, and its attributions (Bennett's "barrier doctrine", Falque's reading) are unverified in-repo | Not physics; book register (§A.32 forbids it in a paper). **Not migrated by default** (§A.28: no claim depends on it). Owner option: a ch03 §3.8 paragraph rewritten around "definite, with ontic parameter dependence", from primary sources. Git history keeps the original |
| 23 | 659–702 | FAQ (10 questions) | (a) answers; (d) four items | Bell `Main.md:354–405`; randomness `Main.md:103–109`; dark matter/Bullet `GR.md:466–536`; observer programmes `Main.md:692–694`, `ch03:216`; string theory `papers/Structure.md`; classical vacuum `GR.md:342–370`; **holography (:694–699): (c) by default, see row 23a.** **(d) NEW:** (i) :662 says the framework "*derives* the quantum formalism … and proves the derivation is the only possible one", against `Main.md:616`, `:624`, `GR.md:220–222` (bare OI ⇏ QM) and CONTRIBUTION-r2 (c)1–2. (ii) :692 "Claim 4 is a theorem, not an assumption" is against `Main.md:62` (the bijective substratum is a reconstruction choice; total finiteness a posit) and `Main.md:704` (no ontology-level falsifier). (iii) :684 says "the SM gauge group is forced uniquely from cubic-group representation theory", against `glossary.md:75` (conditional on H-link). (iv) :679 "twenty-two classified quantitative predictions … a comparable empirical record is not currently produced by the alternatives" is self-assessment; the counts live in `SM.md:1298` | Owner-part 6 candidate: see §4 |
| 23a | 694–699 | FAQ: "Doesn't holographic physics show that spacetime comes from entanglement?" (Ryu–Takayanagi read geometry-first; van Raamsdonk; different breakdown places for the two orderings) | **(c)** by default; :699 list is (d) | **Unique.** The corpus covers only ER=EPR (`Substratum.md:236–242`). Ryu–Takayanagi and van Raamsdonk occur in no maintained `.md`, and book Appendix C (`appendix-c-objections.md`, C.2–C.12) has no such objection. Not essential to the Introduction (outside its scope, OUTLINE-r3 "Gap in coverage"). **Owner option:** a new Appendix C objection section, written from primary sources (Ryu–Takayanagi 2006, Van Raamsdonk 2010), in essay register. **Must not be carried even then:** :699's list of "consequences matching observation". "Produces the observed vacuum energy" conflicts with `GR.md:360`. "The SM gauge group with its coupling strengths" is unconditional, against `glossary.md:75` (H-link) and `SM.md:1259` (1/α₁ an input, class E). Also not carried: the "ten consequences … seven mutually independent" framing outside GR:358's own dependency statement | The one substantive objection-response that leaves the corpus with the Explainer (review F1) |
| 24 | 703–745 | The Decompression Algorithm; antimatter as artifact; "Nothing in QM explains a fundamental phenomenon"; JPEG/MP3 | (d) | **R3.7:** :745 says "no other reconstruction is possible — this is the unique algorithm", against `Main.md:624`, `GR.md:178–186` (antiunitary twofold ambiguity) and `ch03-structural-realism.md:10` ("the quantum decompression — a representation, explicitly non-unique"). :739 claims to resolve "is the wave function real?", against the same sources. **NEW:** :719–727 makes the $\Lambda(2,1)$ negative entries "the minimal-model ancestors of antimatter". No maintained source supports this ("antimatter" appears only in Complexity/ch10/ch19, in other senses). :707 "exactly the quantum algorithm" overstates `Main.md:534` | Not migrated. The interpretive core ("QM as the observer's compression") is already in ch03 at the non-unique strength |
| 25 | 749–755 | "What This Means" | (c); (d) one sentence | Covered by `GR.md:326–370`, `Substratum.md:330–338`. **NEW (d):** :753 "All three are mandatory consequences … and all three match what we observe", against `GR.md:52` (C4 not discharged) and `GR.md:12` (conditional on H-slope) | — |
| 26 | 759–773 | Corroboration: The Rigidity Test | (d) | **R3.6:** :771 "No free parameters … nothing to tune", against σ undetermined (`Explainer.md:525–527` itself; `ch07:80`; `GR.md:160`). **NEW:** :769/:773 "seven independent checks … Seven passed checks with no free parameters" as "Corroboration": these are internal consistency checks (§A.23), and item (7) "all inputs to Jacobson's derivation" is stated without GR's conditions (H-slope, frame conditions; `GR.md:12`). Pieces are in the maintained corpus at their proper scope: dynamics selection `Substratum.md:158` (within nearest-neighbour, under A4/E4/A5), `:48`, `SM.md` §4.1; LIV coefficient `Substratum.md:433` | Not migrated |
| 27 | 777–808 | "What Is the Lattice?": minimal structure, coupling graph, alphabet size, causal sets, hierarchy (:793–804), "What remains" | (a); (d) two items | `Substratum.md:42–64`, `:406–408` (hierarchy, incl. Noether, which Main:66 now cites); `SM.md` §2.4, §2.7; causal sets `Structure.md:366–376`, `SM.md:1664`, `ch03`. **(d) NEW:** :779 "The rigidity test proves that the wave equation on a lattice produces both QM and GR" (row 26). :806/:808 "The partition V, the dimension, and the laws of physics are all derived" contradicts the Explainer's own :783/:854 and `Substratum.md:84–88`, `:156` (d = 3 from empirical inputs E5–E7) and the README scope note ("derived relative to the named premises") | — |
| 28 | 812–862 | "Why These Particles?" (fermions/tastes, Higgs, gauge from M, K = 6 under H-link, chirality H-χ′, strong CP, hypercharge, matter reps, predictions) | (a); (d) three items | `SM.md` (§§2–8), `ch05-gauge-structure.md`, `ch06-matter-content.md`, `appendix-b` B.5–B.6c. **(d):** **R3.8**, the heading "No empirical inputs" (:854; `glossary.md:75` H-link; H-χ′). **NEW:** :862 "[SM §7]'s twenty-two zero-parameter quantitative predictions" contradicts :858 and `SM.md:1298` (7 of 22 are parameter-free structural). **NEW:** :856 says the observer genericity theorem with the universal representation "supplies every such observer's self-consistent quantum description"; that is the full-operational reading `Main.md:542` keeps separate | Not in Introduction scope |
| 29 | 866–882 | "The Full Picture" table; "From physics to life"; closing | (c); (d) | **(d) NEW:** the table row "General relativity: Emerges from lattice dynamics passing 7 checks" (row 26). The Complexity paragraph (:880: "no fitted parameters", "RNA world a structural prediction", "fine-tuning and the anthropic principle dissolve") is against `README.md` §3 (conjectural extensions "carry no evidential weight for the core framework"). :882 "Everything else … is emergent" overstates, as row 27 | — |
| 30 | 886–988 | "What Is (S, φ)?": storage, Turing, arrow of time, incompleteness family, mathematics/physics, reconstruction converse | (a) concepts; (d) five items | Storage/Turing `Substratum.md:42–56`, `ch02-substratum.md:34`; arrow of time `Main.md:724–744` (§4.6), `Substratum.md:56`, `:348–364`; incompleteness family `ch01`, `ch02`, `ch03:214`; mathematics `Substratum.md:62`, `:234`, `Methodology.md:439–441`, `ch02:72`; reconstruction `Substratum.md:66–245` (§3–4). **(d) NEW:** (i) :892 "the accessible-timescale backflow lemma (Main, §2.3) establishes P-indivisibility without recurrence", against `Main.md:141` (C4 does not force P-indivisibility on short windows; XOR). (ii) :930 "the 'past hypothesis' … gets replaced by a theorem … No additional axiom required", against `Main.md:726` (a theorem *conditional on (EM)*; "without (EM) it is a conjectural application") and `:740` (rate condition). (iii) :942/:944 "The structural consequence is quantum mechanics … (unitary QM with the Schrödinger equation, Born rule, and Bell violations)", against `GR.md:220–222` and `Main.md:542`. (iv) :974 says "If you observe QM with Bell violations … the characterization theorem forces you into some (S, φ, V)". That omits the reconstruction's premises M1-T/M1-B and H-Bell (`Substratum.md:122`, `:132`). (v) :902 says the reality/description question is "a question the framework proves to be gauge"; that is stronger than `Substratum.md` §6.1 (`:380`) at the stated scope | REVIEW §2 found no unique substance; overlap 0.08–0.18 |
| 31 | 992 | Companion-papers note ("five core papers"; lineage "draws on a systematic analysis") | (c) | Stale list (core set is now seven: `README.md:45`). Not carried | — |
| 32 | 996–1035 | Appendix: Mathematical Summary Tables (Table 1 :1000–1009; Table 2 :1013–1029; chain :1031–1035) | (c) form; (d) rows | See §3. **(d):** R3.2 (:1022 C4 ✓), R3.3 (:1035 "Every link is either a proof or a calculation"), R3.4 (:1027, :1029 unconditioned), R3.9 (:1021 bare "universal hidden-memory theorem"; `Main.md:580`, `:588`), R3.10 (:1008, :1009, :1017, :1021 section drift; "[10,11]"), F13 "≤ n³" (:1015) | — |
| 33 | 1039–1055 | Key Mathematical Subtleties 1–4 | (a); (d) one item | 1 → `GR.md:162`; 2 → `GR.md:164`, `SM.md:164`, `appendix-c-objections.md:261`; 3 → `GR.md:178` (H-BG statement verbatim in substance), `Main.md:256`; 4 → `GR.md:128–134` (§3.2), B.4.1. **(d):** **R3.11**, item 1's "Type II running-vacuum form" check, against `GR.md:378` / `ch07:211`. That tension also exists at `GR.md:162`, so it is a corpus issue, not an Explainer-only one | — |
| 34 | 1059 | AI-assistance acknowledgment | (c) | The Introduction carries its own, on Main's pattern (`Main.md:768–770`) | — |

**Counts.** 34 numbered rows, plus sub-rows 14a–14i and 23a (23a added in revision 2). REVIEW §3 lists 11 stale items, all re-confirmed at
`687e885b`. Walking the whole file adds the items marked NEW. Counting each distinct claim once:
rows 2, 6, 7 (three sites, one claim), 11 (ii, iii), 16 (:465), 18, 19, 20, 21 (i–v), 22, 23 (i–iv; 23a's :699 list),
24 (antimatter), 25, 26 (seven checks), 27, 28 (two), 29, 30 (i–v). That is eighteen rows. The number of distinct
statements depends on grouping, so no count of them should be quoted anywhere.

***

## 3. The summary tables (Explainer:996–1035)

**Decision: superseded, conditionally, by the accepted Introduction's kernel map for the rows within
the paper's scope. No book navigation table by default.**

- **The condition.** Appendix A is still an outline item (`OUTLINE-r4.md:325–336`, default about 15
  kernel-backed rows). Under Alt-L it is folded into §3 as a kernel table (`OUTLINE-r4.md:342`).
  The supersession holds only if the **accepted** Introduction text carries that kernel map, as
  Appendix A or as the Alt-L §3 table, with unformalized links listed. This is checked at
  RETIREMENT-r2 P1/P6.
- **Current draft.** The coordinator reports that the draft at #918, `8fcc6443`, has a 16-row
  Appendix A. That object is not in the local store, so this audit has not verified it. It is the
  row set P1 must check in the accepted text, not in the draft.
- **If the accepted text has no kernel map.** The Explainer's QM-side rows (Table 1; Table 2
  §3.1–§3.4) fall back to their prose carriers: Main's status ledger `Main.md:710–722` and B.7
  `appendix-b:402–478`. The no-table recommendation for the book is unchanged, because those
  carriers already exist.

- **What the Explainer tables are.** A logical-flow table of the *whole* programme: 8 rows on Main
  §1–2, 15 rows from the stochastic-quantum correspondence through ħ, ε and S_BH, and a chain sentence.
  No maintained file has a tabular counterpart (REVIEW §1 row 2b). Every row's content exists in prose,
  and five rows plus the chain are stale (row 32 above).
- **What the Introduction's Appendix A is (as planned).** OUTLINE-r2/r4 "Appendix A. Kernel map": about 15
  kernel-backed rows (claim ID, declaration at module:line on the drafting commit, unformalized links,
  recipe `lake build` + `tools/lean_axiom_check.py`), built from Main's status ledger
  (`Main.md:710–722`). It supersedes the Explainer's Table 1 and the QM rows of Table 2 (§3.1–§3.4)
  for the paper's purpose, and does better on three counts:
  - it is built on kernel declarations;
  - it lists unformalized links, which replaces the chain's "Every link is either a proof or a
    calculation";
  - it carries status from Main's ledger rather than prose.

  It deliberately has no counterpart for the ħ/ε/S_BH rows (Table 2 §4–§6): the Introduction's scope
  excludes them (OUTLINE-r3 "Gap in coverage, accepted by design").
- **Why no book navigation table.** The ħ-chain rows are already in the book in status-bearing form:
  - the prediction table `ch07-gravity.md:292–307`, which marks rows conditional on H-slope (:294–296;
    tier note :309);
  - the B.4 derivation (`appendix-b:169–222`);
  - the B.1 overview (`appendix-b:6–24`) and the "full mathematical content" list
    (`appendix-b:465–476`);
  - `appendix-a-prediction-status.md` and `readers-guide.md:71–80` serve navigation.

  A further table would restate these (§A.28) and would add one more status surface to keep in sync
  (§A.25).
- **If the owner wants one anyway.** The home is Appendix B §B.1 (+ FULL mirror). It is rebuilt from
  Main:710–722 and ch07:292–309, never copied, with these constraints (REVIEW §4 "Book items"):
  - Main:522's witness binding;
  - C4 at the horizon "named, not discharged" (`GR.md:52`);
  - H-slope on the ħ/ε/S_BH rows, H-BG on phase-locking, mixing on C2;
  - current [Main]/[GR] section numbers;
  - no "every link" sentence;
  - no "≤ n³".

  **Precondition:** the #931 correction first. B.7.6 itself still displays the per-horizon slogan
  (`appendix-b:454–455` = `FULL:6243–6244`), so a table built on it would inherit the defect.

***

## 4. Revision-3/4 candidates (OUTLINE-r3 "Mapping onto the owner's six-part structure")

OUTLINE-r3/r4 (on disk, written after r2) add an "absorb from the Explainer (candidates only)" column
and leave the decision to this audit. Verdicts:

| r3 candidate | Verdict | Reason |
|---|---|---|
| Part 1: the motivating register of the Explainer's introductory sections, rewritten from Main:28–30 | **No Explainer source.** Write from `Main.md:28–30` | Rows 2–4: :22 is (d), and the register is the Explainer's popular one (§A.32) |
| Part 2: the summary-table *form*, rebuilt as Appendix A from Main:710–722 | **Adopt as stated; supersession conditional on the accepted text (§3)** | §3. Only the idea of a table is shared; no row text is reused. The Appendix A rows take AUDIT r4 classes, not the Explainer's framing |
| Part 3: a technical-register short version of the quantum-weirdness walkthrough | **Source Main, not the Explainer; at most one sentence, labelled interpretation** | Row 20. The supported content is `Main.md:666` (double slit) and `:668–676` (observer covariance, Wigner's friend at :670–676). Both are interpretation ((e), AUDIT:1455), not derived results: Main:666 gives no model of interference. The Explainer's "dissolves … into a derivation" (:561) and its cat paragraph are not carried. The corrected card-table version of the cat is §5-h from ch01 §1.11 (`ch01:265–294`) |
| Part 6: an FAQ-style "what the correspondence does not say" list | **Build from CONTRIBUTION-r2 (c) 1–11 and OUTLINE §6/§8; nothing from Explainer:659–702** | Row 23: the Explainer FAQ asserts the opposite of non-claims (c)1–2 at :662 |
| Part 4 (examples); part 5 (black hole) | None (as r3 says) | Coin-and-die and minimal model come from `Main.md:178–196` |

**What r3/r4 change for this audit.** They name the owner decision (replace; publication order
Introduction → Main → Book) and the planned filename `papers/Introduction.md` (audit README.md:112).
RETIREMENT.md depends on that filename. The list of things the paper must not inherit (r3's 11
items) equals REVIEW §3. This audit adds the NEW items of §2. The outline's R24 (the paper read as
covering the whole programme) is unaffected.

***

## 5. Overclaim and novelty check on every candidate migration

| Candidate | Inherits an unsupported claim? | Presents a known result as novel? | Result |
|---|---|---|---|
| Main:66 repoint to [Substratum §6.2] | No: Substratum:408 states the same identification at the same strength | No: it is an interpretation, and Main:66 already says "the literature independently records" it | Proceed (retirement commit) |
| Double-difference display into B.7.5c (optional, from Main:232–238) | No: B.7.5c keeps "conditional on H-BG" (`appendix-b:444–446`) | Unclassified in AUDIT r4. In the book appendix it is a derivation step, not a claim of priority | Optional |
| Navigation table (optional, not recommended) | Only if built from Explainer rows. The constraints in §3 prevent it | Rows would need AUDIT classes for C2/C8 (KNOWN) if they carry any "framework result" wording | Not recommended |
| Holography objection in Appendix C (owner option, row 23a) | Yes if :699's list is carried; excluded | n/a (response to an objection; RT and Van Raamsdonk cited as the literature they are) | Only if rewritten from primary sources, without :699 |
| Lineage paragraph in ch03 (optional, not recommended) | Yes as written (Claim 4 "local"; Gödel→Wolpert "chain") | n/a (philosophy) | Only if rewritten from primary sources around "definite, with ontic parameter dependence" |
| Introduction Appendix A (r3 part 2), if present in the accepted text | No: built from Main's ledger, with unformalized links listed | Classes from AUDIT r4: C4 PARTLY KNOWN, C2 KNOWN, C8 KNOWN, C10/C11/C9/C12 REFRAMING. No priority sentence (CONTRIBUTION-r2 (c)7) | Adopt |

*Process.* Read-only. Only `git -c gc.auto=0 -c maintenance.auto=false grep`/`show`/`log` were run
against the shared store.
