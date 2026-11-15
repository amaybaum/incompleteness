# Review of change map A1C r1 (the general A1 correction, site by site)

**Reviewer.** Independent, non-author. Paper-only: no repository file was edited, nothing was committed or pushed, nothing was posted, no Lean or build was run. Read-only text searches and small read-only scripts were run against the read-only worktree of `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`; `tools/proof_census.py --json` was run read-only to map edited lines to ledger statements.

**Standard.** `AGENTS.md` at the base (§A.25, §A.14, §A.27, §A.30, §A.32–§A.35, the Main-independence and Main-root rules, the claim/evidence boundary); the owner decisions as recorded in `DECISIONS.md`, with every qualification read as a binding condition; the owner's 2026-11-15 split into Stage 2a (retire A1 as an assumption about nature: label, "Finiteness" property, ledger entry; remove unsupported physical readings; withdraw cosmic recurrence while keeping the period bound in place; correct counts and references, with the registry actions those require) and Stage 2b (relocation between documents, restructuring, new foundational interpretations); finiteness of the substratum is open, and no text may assert or imply infiniteness. Audit r9, owner briefs 15Q-r1 and REMAINING-r1, the held map A1W r2 and the #1312 PR body r2 were used as the map's sources.

## Verdict

**REVISE.**

The map is careful and mostly faithful: every quoted fragment I tested exists at its stated line (one locator is off by two lines), the decisions are applied in the large, no row asserts or implies that the substratum is infinite, the Main rewording of the cone and Bell scope claims no more than #1312 proved, and the Part E reconciliation of the 137 held sites is arithmetically right. It cannot go to the owner as Stage 2a as it stands. Three rows would put new or false content into the manuscripts (F1–F3). Several classes of A1-dependent sites are missing, the largest being the Bell and cone restatements in the companion papers and the book (F5). Two registry actions conflict with a guard or a K3 certification (F2, F9). Two owner questions rest on premises that are wrong at the base (F12, F13). Several 2a tags cover headline restructuring that the 2026-11-15 split places in 2b (F11).

Findings: **3 blocking, 17 required, 11 recommended** (31 in all).

***

## Findings

### Blocking

**F1 (blocking). M-31, Main:449: the proposed text states something false about finite reversible realizations.**
*Evidence.* Main:449 is inside the ETH "physical motivation" paragraph about a hidden Hamiltonian $H_H$ ("finite-dimensional Hamiltonian flow has purely imaginary spectrum and Poincaré recurrence at $t_R$ exponentially large in the system size"). M-31 transfers both clauses to "a finite reversible realization": "its dynamics has purely imaginary spectrum and recurrence at a time $t_R$ exponentially large in the system size". A finite reversible realization is a permutation. Its spectrum lies on the unit circle; "purely imaginary" applies to a Hamiltonian generator, not to the map. Its period can be any order up to Landau's $g(n)$, as small as 1. Book §18.7 states that the framework supplies no lower bound on the period (ch18:186). The row therefore introduces a false general statement in place of a typical-size estimate made for Hamiltonian flows.
*Fix.* Change only the subject of the first clause and keep the Hamiltonian clause as it stands: "In a finite reversible realization there is no relaxation in the strict sense — finite-dimensional Hamiltonian flow has purely imaginary spectrum and Poincaré recurrence at $t_R$ exponentially large in the system size." Alternatively, replace only "The substratum dynamics is reversible, so" with "For a finite reversible realization". Main:453 stays NC as proposed.

**F2 (blocking). M-08 and K-ch01-38 (Lemma 3), with R-03 and D.2: the rows add a clause to a K3-certified lemma statement, and the registry action would re-certify it falsely.**
*Evidence.* M-08 inserts into the statement of Lemma 3 "it is injective on states that differ in registered content (record preservation, §1.2 Remark)". `verification/coverage/LEDGER.json` entry `MAIN:L-3` is **K3** ("the exact manuscript statement is proved in Lean") with an empty `delta`. Its note reads: "REVERSIBILITY IS NOT DERIVED … phi is a hypothesis (Equiv.Perm S) everywhere and no theorem concludes that the substratum is bijective". The Lean theorem `determinism_reversibility_selected_measure` proves no record-preservation injectivity. R-03 proposes "fingerprint re-affirmed", which would keep K3 over a statement that is no longer exactly proved in Lean (coverage_check rule 6: a recorded gap is the definition of not-K3). Moving an argued claim of the status Remark into a lemma statement also promotes its status. It reinterprets Lemma 3 (a 2b kind of change), and it sits badly with Q5 (a)'s qualification ("Assert record preservation about nature only to the extent independently supported").
*Fix.* Drop the inserted clause from M-08 and from the K-ch01-38 mirror. Keep the narrowing: "*$\varphi$ is a function with a unique successor for every state (determinism) and, on a finite reversible realization (the representative of §1.2), a bijection …; on each finite cycle of such a realization … the realization's default prior …*". Record preservation stays where it already is (Main:36, the status Remark). In R-03, re-affirm K3 only after checking the new statement against the Lean statement (`[Fintype S]`, `Equiv.Perm S`); otherwise lower the level or record the delta in the same commit.

**F3 (blocking). G-12, GR:342: the proposed text makes finiteness one of the framework's "irreducible starting commitments".**
*Evidence.* GR:342 lists "the framework's irreducible starting commitments (the fact that observation occurs, the empirical inputs E1–E7, and the structural assumptions A1–A6)". G-12 replaces the last item with "the structural assumptions A2–A6 and the finiteness hypothesis of [Substratum] Theorem 23". That re-posits finiteness as a commitment of the framework, contrary to Q4 (a) and Q3 (a) ("retire A1 as a posit about nature").
*Fix.* "…given the framework's irreducible starting commitments (the fact that observation occurs, the empirical inputs E1–E7, and the structural assumptions A2–A6), in the reconstruction theorem's finite setting." Alternatively, keep the list as A2–A6 and add after "under the reconstruction theorem" the words "which takes $S$ finite". F10 shows that A2–A6 still contain finiteness through A4 while A4 is unchanged, so this site is also affected by the owner question raised there.

### Required

**F4 (required). M-41, Main:720: the new sentence adds a claim about nature and omits its probability hypothesis.**
*Evidence.* The proposed sentence reads: "for nature's visible process P-indivisibility is certified by a measured revival or identity return within an accessible window (§2.3)". (a) It reads as an established certification route for nature. (b) Rooted families need a hidden prior shared by every root (Main:135, :141), so a statement about nature's rooted family carries a probability law for nature, which Q6 (a)+(e) requires to be a named hypothesis where it enters. (c) It adds a claim where only a removal was triggered.
*Fix.* Delete the A1 sentence and the recurrence phrase. Keep "**The theorem** requires …" and "The readback lemma (§2.3) provides the quantitative route to accessible non-Markovianity, establishing observable conditional memory on the timescales accessible to laboratory experiments." If a pointer is wanted, use the model-neutral form: "on an accessible window a rooted family is certified P-indivisible by a revival within it (§2.3)".

**F5 (required). Bell and cone scope: the Main rows are consistent with #1312, but the restatements elsewhere are not mapped (§A.25).**
*Evidence.* M-28 narrows the Bell ceiling theorem to a finite site set. M-05, M-37 and M-54 state the any-cardinality case only for the nearest-neighbour cubic update with finite wing and readout regions (Main:414 (2)). M-04 and M-10 (6) state the cone at any cardinality only with finite reading sets. The following restatements remain without either condition and become stronger than what Main proves once A1 is retired:
- the dependency-graph cone stated without finiteness of $V$: Main:216 ("For a spatial OI constitution the coupling graph is defined by one-step dependence, so its iterates give exact graph causal cones"), Main:654 first sentences ("inherit an exact dynamical causal separation from the dependency graph"), and Main:774 first two sentences (M-54 edits only the Bell clause);
- the dichotomy "a completion reproducing quantum Bell correlations gives up at least one of two remaining hypotheses: (ii) and (iii) … or measurement independence" (Main:401–404), and the bold sentence at Main:391–393;
- companion papers: Substratum:14 ("Its spatial coupling graph supplies finite causal cones"), :48, :131 ("makes that reference graph Bell-local and caps CHSH at 2"), :171, :467; Methodology:339 ("The reference nearest-neighbor graph is Bell-local under measurement independence…"), :381, :385, :389, :391;
- book: ch01:16 and :183, ch03:40, :162, :180, :186, appendix-c:32, :34, glossary:19 (each with its FULL line).

Sites that say "for finite-range couplings" (Substratum:22, :373) already carry the reading-set condition. Introduction:143 is covered by Introduction:34's finite-model scope.
*Fix.* Add rows. For the Bell restatements, insert the scope M-37 uses ("on a finite site set, and for the nearest-neighbour cubic update with finite setting and readout regions on a site set of any cardinality"). For the "reference graph is Bell-local" sentences, add the finite-region condition, labelled as Main:414 (2) labels it. For Main:216, :654 and :774, add "with finitely many sites, or with each site's update reading a finite set of sites (§3.3)". For Main:401–404, either scope the dichotomy the same way or add an NC row giving the reason. All are 2a: they narrow and add nothing.

**F6 (required). Other missed sites.**
- **Structure:1032, :1034, :1036, :1038.** "A1 (finiteness) **fails** …", "A1 and A2 fail", "A2, A5, A1 fail", and at :1038 "as that class is delimited by A1–A6". T-04 covers :1030 and :1040 only. *Fix:* W4c for the items ("finiteness (the hypothesis of Theorem 23)") and W4b ("A2–A6") at :1038. Each programme still fails A2 or A5, so the conclusion survives.
- **ch02:120 (FULL:754).** "together with six structural assumptions and the nearest-neighbor restriction". This is a count (§A.30) that C-4 misses. *Fix:* "together with the structural assumptions A2–A6, a finite configuration space and the nearest-neighbor restriction".
- **ch03:58 (FULL:923) and ch03:62.** "The Boltzmann brain problem … is dissolved at Level B …; Boltzmann brains … are structurally excluded from the observer-admitting subset". This is in audit AM-8's downstream list and Q7 (d) applies, but the map has no row. *Fix:* mirror U-27 and X-03 (the exclusion is the §4.6 result for a finite bijective model, in its coarse-grained description).
- **ch18:190 (FULL:4996).** K-ch18-186/188/190 deletes only the "predicts … cyclic" clause. Still asserted: "The conceptual content is significant." and "The framework's commitment to substratum cyclicity is one of the structural commitments that distinguishes it from frameworks treating the universe as either fundamentally non-cyclic … or fundamentally infinite". *Fix:* delete both under Q10 (c).
- **ch14:92 (FULL:3758).** "The infinite-resource routes are closed by the framework's structural commitments" follows ch14:90's infinite-time exclusion (AM-23.2). *Fix:* "The arbitrary-precision route is closed by the lattice's finite site resolution". See F15.
- **GR:20, clause (ii).** "under the canonical measure of [Main] Lemma 3 — the invariant measure selected by maximal entropy, which the physical realization uses —". This is the GR mirror of the Main:58 phrase that M-09 removes (Q6 (a)). G-01 edits only clause (i). No guard pins clause (ii). *Fix:* "under the default measure of [Main] Lemma 3 for a finite realization — the invariant measure selected by maximal entropy —".
- **Main:84–90 and Main:103.** Lemma (partition-relativity under the canonical invariant measure), with proof "By Lemma 3, the observer uses the Liouville measure μ — the maximal-entropy invariant measure"; and Main:103, "marginalizing over the Liouville measure (§1.4)". After M-08 and M-09 Lemma 3 selects the default prior of a finite realization. The "observer uses" reading is a claim about nature's prior (Q6 (a)+(e)). The census label of the lemma (`MAIN:L-partition-relativity-under-canonical-invariant`) is an identifier and should not be renamed. *Fix:* add a row. Either NC, giving the reason that this is the continuum analogue under a declared prior, or replace "the observer uses" with "the canonical choice is" and keep the label.
- **Main:728, after the ledger.** "…and agree on the substance, including that the injectivity recovery closes its hidden-sector margin with an empirical input". This contradicts M-45's new item (iii) ("the hidden-sector margin … is open"). *Fix:* "…including that the injectivity recovery is a lemma for registered content and leaves the hidden-sector margin open for nature".
- **ch05:95 (item 7).** "Main's readback lemma supplies that memory, and its recurrence-cycle theorem the P-indivisibility". *Fix:* W2 ("and, on finite reversible realizations, its recurrence-cycle theorem the P-indivisibility").

**F7 (required). OQ-4 is already decided by Q5 (a) qualified, and its scope is wider than book Chapter 7. K-ch02-16 keeps "reversible" for nature's dynamics.**
*Evidence.* The map's own option (b) is Q5 (b), which the owner did not choose. Q5 (a)'s option text reads: "Bijectivity is kept for constructed realizations … Injectivity on the hidden sector, and surjectivity, are stated as open for nature." The same "bijectivity premise / information is never lost" reading appears beyond ch07:
- ch09:129;
- ch18:122 and :138;
- ch19:22, :30 and :72 ("The substratum map $\varphi$ is bijective by premise (Chapter 1), so information is never lost from it");
- Main:64's opening ("The bijectivity of $\varphi$ — equivalently, that the substratum conserves information — is … imported here … The framework therefore assumes no more than standard physics already does"), which M-11 leaves standing above its rewritten last sentence, and its book mirror ch01:41.

K-ch02-16's proposed text gives "$\varphi: S \to S$ is the dynamics, a bijection on the finite realizations of Chapter 1 — a deterministic, reversible transition rule that maps each state to its unique successor". That still asserts reversibility of nature's $\varphi$, and the clause is garbled ($\varphi$ on $S$ is not "a bijection on the finite realizations").
*Fix.* Remove OQ-4 as an owner question. Apply Q5 (a) at every site listed above, all as 2a. Rewrite K-ch02-16 as: "$\varphi: S \to S$ is the dynamics — a deterministic transition rule that maps each state to its unique successor, injective on states that differ in registered content (Chapter 1, Lemma 3) and a bijection in the finite realizations of Chapter 1." For Main:64, keep the historical comparison and replace "The framework therefore assumes no more than standard physics already does." with a statement that the framework's constructed realizations are bijective by construction and that it does not adopt reversibility of nature as a postulate (the M-45 wording).

**F8 (required). D.2 does not list all the coverage-ledger entries whose fingerprints the map moves.**
*Evidence.* Census statements (lines beginning with a bold `**Theorem`/`**Lemma`/`**Corollary`…) whose fingerprinted body the map edits:
- `MAIN:L-3` (M-08; K3);
- `MAIN:T-statement` (Main:80, edited by M-12, M-13, M-14; level SUM; its note quotes "the substratum's stated interventions", which M-14 rewrites);
- `MAIN:L-non-permutation-witness` (M-30; assumptions "T not a permutation");
- `MAIN:C-observer-selection-rule-rate-condition` (Main:760, edited by M-51);
- `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer` (Sub:268, edited by U-23);
- `SUBSTRATUM:L-23.0`, `SUBSTRATUM:T-23`, `STRUCTURE:P-9.5`, `SM:P-4b-…` (all GAP, assumptions "see the statement").

D.2 names only the first and the last group ("if gated entries exist"). The Bell ceiling theorem (Main:364) has no ledger entry, because its header is mid-line and the census does not see it; D.2's conditional should say so.
*Fix.* List every entry above in D.2, with its action: re-affirm the fingerprint; rewrite `MAIN:L-non-permutation-witness` assumptions to "T not a permutation; a finite reversible realization"; update the `MAIN:T-statement` note to the M-14 wording; check K3 for `MAIN:L-3` (F2).

**F9 (required). D-1a conflicts with guard R7-MAX, and the D.4 guard-pin scan missed pins outside the manuscripts. OQ-3 is narrower than the conflicts it has to cover.**
*Evidence.* D-1a rewrites "A1-A6" to "A2-A6 (with the finiteness hypothesis of Theorem 23)" in the notes of census families 12, 13, 48 and 49 (zero-based numbering; confirmed). R7-MAX (`edge_rigidity_probe.py` ~3466–3479) requires family 13's note to contain "asserts nothing about whether the witness satisfies any of A1-A6 in the manuscript sense", and the README (`_rd1`) to contain "no manuscript-level A1–A6 conjunct is presently a faithful predicate of the bare theory". R7-RB1 (~3344, ~3355) pins "whose A1–A6 are not `DerivedOI`". Family 13's note describes what a closed audit tested, namely the six manuscript axioms quoted at that audit's base. Rewriting it to A2–A6 would misdescribe that audit. Families 48 and 49 use "A1-A4, not-A5 class" and "A1-A6 unchanged" partly about kernel predicates.
*Fix.* Re-scope D-1a. Family 13: no change, because the note describes the audit's object; if anything is added, say "the six axioms as stated at the audit's base". Families 48 and 49: change only clauses that assert current manuscript content. Family 12: change the clause quoting the manuscripts' current statement, after checking the guard. Add R7-MAX and R7-RB1 to OQ-3, or to D.4 as NC with that reason. Add `verification/README.md` (~:317, :917–:954, :1006–:1010) as NC with that reason (see F29). Run the Stage 2 guard check against the census JSON and `verification/README.md`, not only against manuscript lines.

**F10 (required). A4's finite quotient lattice (U-09a/U-09b): finiteness stays inside A2–A6, and Q3 (a) as decided includes restating A4.**
*Evidence.* Sub:98 (A4): "the coupling graph is a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice". With $\mathbb Z_q$ alphabets (Sub:98, A5), A2–A6 entail $|S|<\infty$. The Q3 option text the owner adopted reads: "(a) Retire the identifier A1 … A4's parenthesis, 'a finite periodic lattice' (Sub:98), is restated, with the sentence of Stage 2 (a) that uses it (Sub:157); the census notes of families 12, 13, 48 and 49 are updated." The owner's qualification reads: "Preserve finite periodic lattices where explicitly used as model conditions." The map keeps A4 unchanged in 2a (U-09a NC) and defers the restatement to 2b (U-A4). This may be the right reading of the 2026-11-15 split, but it is a choice between two owner texts. Its consequences are not stated:
- every 2a sentence naming "A2–A6" (T-01, T-04, T-15, G-11, U-21 and others) describes a class of finite models;
- W4's "finiteness of $S$ and A2–A6" is redundant while A4 stands;
- any sentence presenting A2–A6 as commitments about nature (G-12, F3) keeps finiteness through A4.

Methodology:345 supports the model reading ("restrictions on the class of constructions the reconstruction considers").
*Fix.* Add this as an owner question (OQ-6): (a) A4 unchanged in 2a, with a one-line map rule that A2–A6 sentences are statements about a class of finite models and no sentence presents A2–A6 as posited of nature; or (b) the minimal A4 restatement in 2a. Recommendation: (a), under the qualification. Note the redundancy in W4.

**F11 (required). The headline deletions of valid finite-model results are restructuring, not removal of physical readings. They interact with the Main-root rule (OQ-1).**
*Evidence.*
- M-02 deletes Main:18's three sentences ("On one fixed finite reversible representative …"). They are explicitly model-scoped once M-01 removes "finite" from Main:14.
- M-12 deletes the recurrence clause of the Theorem statement (Main:80 item (2)).
- I-01 deletes Introduction:12's sentence, which Introduction:12 and :34 already scope to finite models.
- K-pref-3 and K-ch00-53 delete the corresponding book sentences.
- K-ch01-93 rewrites ch01's "central technical result" sentence and names other results as central.

These apply the audit's headline rule H1, which the owner never adopted as a rule. Under the split, changing what Main and the book declare as their headline results is restructuring (2b). It also changes Main's set of roots: once the results leave the abstract and the Theorem statement, the Main-root rule asks whether they may stay in Main, which is OQ-1. Tagging them 2a while deferring OQ-1 leaves Main exposed to the root rule between 2a and 2b.
*Fix.* Either tag these rows 2b and decide them together with OQ-1, keeping in 2a only the W2 scoping ("on a finite reversible realization", K-ch01-93: "the central technical result of the chapter is that, on a finite reversible realization, …"), or keep them in 2a and present OQ-1 for decision in the same approval. State which in Part F.

**F12 (required). OQ-2: the recommended option keeps total finiteness as a named hypothesis of a physical calibration. K-ch09-118 contradicts both options.**
*Evidence.* OQ-2 (a) adds "finiteness of the total system, a model condition not posited of nature" to the named conditions of $\hbar = c^3\epsilon^2/(4G\sigma)$, $\epsilon$ and the $1/4$ coefficient. These are calibrations applied to nature's horizon. Making them conditional on a finite total system keeps A1 as a hypothesis of physical claims. That is the form the owner declined in Q9 (c) and Q10 (c) (both rejected the "keep as labelled conditional on A1" options), and audit AM-22 §5 says that without P7 the calibration "become[s] conditional on a premise the owner's condition excludes". Option (b) has an existing route: GR:669 already treats "the symmetric detailed-balance rate ratio" as "an additional condition" for general dynamics, so the counting link can be replaced by naming that ratio (and the shell counting) as a condition. Separately, K-ch09-118 changes "six" to "five" but leaves "The framework's universality-class results — the classical horizon temperature of the boundary count, … the Bekenstein-Hawking $1/4$ and the action-scale relation for $\hbar$ … — follow from these … commitments". That asserts the counting results without finiteness, which neither option supports.
*Fix.* Keep OQ-2 as a genuine owner question. Label option (a) as "total finiteness kept as a named hypothesis of the physical calibration". Recommend (b): name the shell-counting rate ratio as a condition at GR:28, GR:669, ch07, ch09 and appendix-a:117, using GR:669's wording. Do not pre-apply G-03's default. Hold G-03, G-16, K-ch07-14, K-ch09-14/61/84 and K-ch09-118 until the answer. In K-ch09-118, scope the "follow from" sentence to the finite members of the class, or to the named condition, according to the answer.

**F13 (required). OQ-5 rests on a wrong premise.**
*Evidence.* At `e4c6ba7f`, `papers/Main.md`, `papers/SM.md` and every `book/*.md` contain no bare `---` rule (AGENTS' counts are stale). The files this unit touches that do contain them are Methodology (13), Computation (12), Medicine (16) and Bioinformatics (13).
*Fix.* Restate OQ-5 with the correct files and counts. The recommendation, a separate commit in the same PR recorded as build hygiene, remains reasonable.

**F14 (required). S-07 (SM:60) should be NC (item 7 result).**
*Evidence.* SM:60 describes "this construction", the local spatial/gauge construction, which assumes "the bounded-degree and periodic-lattice structure of A3–A4" (A4: a finite quotient lattice) and site alphabets. SM:66 defines $S = S_1 \times \dots \times S_N$ as a finite product of finite sets. Finiteness of $S$ follows from the construction's own model conditions, not from A1.
*Fix.* S-07 → NC, which is the map's own fallback. Apply the same reasoning to S-05 (SM:30, "The spatial construction uses a finite set …"): NC, or "a finite set (A4's finite periodic lattice)".

**F15 (required). K-ch14-90/268 (item 7 result): the first alternative adds content, and the text proposed for :268 misattributes an exclusion.**
*Evidence.* The first alternative for :90 adds "infinite-time computation is not excluded by a finiteness commitment" (narration about a retired commitment) and "the restricted statement … is open (Chapter 14 §14.4)". That pointer is unsupported: the restricted statement is P16, which is not on `main` (audit AM-23.2). The text proposed for :268 opens "excluded by the model in its oracle and arbitrary-precision forms", but ch14:90 makes the arbitrary-precision exclusion structural (the lattice), not the model's.
*Fix.* :90: delete "infinite-time computation requires actual infinity, which the framework's finite substratum precludes (a structural exclusion);" and in the last sentence change "excluded structurally in its infinite-resource forms" to "excluded structurally in its arbitrary-precision form". Remove "infinite-time computation" from the list only if the definition sentence must follow; it can stay as a definition. :268 heading: "excluded — structurally in its arbitrary-precision form, by the model in its oracle form". :268 body: "The lattice's finite site resolution precludes arbitrary-precision continuous computation; oracle access is excluded by the operational-closure hypothesis, not derived from the framework." :92: as in F6.

**F16 (required). SM Theorem 19 (item 7 result): the positive reciprocity readings carry no probability-law hypothesis.**
*Evidence.* Theorem 19 assumes "the hidden prior be the counting measure". Of its uses, the negative ones are unaffected: "reciprocity … does not fix $\bar\theta$" and Theorem 21 hold a fortiori. These sites assert reciprocity of nature's visible counts from substratum T-invariance with no prior named:
- SM:36, :1520, :1546, :1588;
- Substratum:415;
- ch04:116, :166; ch05:194; ch06:10; ch18:198, :208; ch19:80 ("Reciprocity of the visible transition counts … holds exactly at every time scale").

Q6 (a)+(e) requires the law to be carried where it enters.
*Fix.* Add rows (2a, RR) inserting "with the counting hidden prior" (or "under the counting prior of a finite model") at each positive use, with FULL mirrors. Remove G-9 from the Stage 2 reading tasks.

**F17 (required). M-10 (6) and (7): the list of finiteness uses omits a theorem, and (7) deletes valid content.**
*Evidence.* (6) enumerates the results that use finiteness of the whole realization, but omits the Bell ceiling theorem, which M-28 now scopes to a finite site set. (7) replaces the span "Either horn delivers a bijective substratum … so $\varphi$ is a bijection", which also deletes "the two prongs use different inputs — the first empirical (the observed statistics, in the uniform-prior doubly stochastic scope), the second structural (finiteness, …)". That attribution is valid, and M-45's item (iii) still relies on it.
*Fix.* (6): add "the Bell ceiling theorem of §3.3 (whose any-cardinality case is part (2) of the Bell–lattice Corollary, with finite regions)". (7): keep the prong-input clause, scoped "on a finite realization".

**F18 (required). I-06 (Introduction:129): the row quotes two non-adjacent sentences as one span.**
*Evidence.* In the file, "Quantum theory can turn one state partly into another … (a factor $i$)." stands between "A finite reversible world does not supply condition 4 on its own." and "A reversible rule on finitely many states can only permute whole states; it cannot blend them." Applied as written, the replacement would delete the intervening sentence.
*Fix.* Give two separate edits: "world" → "model" in the first sentence, and the new sentence "Whether nature's available operations supply it is open." at a stated position. Under F21 the whole row may be unnecessary.

**F19 (required). The map's own row counts are wrong (§A.30 hygiene for the record).**
*Evidence.* Part A has 284 table rows (282 tagged 2a, 2 tagged 2b), not 280 (278/2). Per section: A.1 56, A.2 9, A.3 20, A.4 19, A.5 33, A.6 17, A.7 10, A.8 16, A.9 101, A.10 3. The total over Parts A–D is 325, not 321.
*Fix.* Correct the header and Stage paragraph.

**F20 (required). Part E.2 / item 4: the #1312 consistency claim needs one qualification.**
*Evidence.* E.2 states that M-04 and M-10 (6) remove the inconsistency left at the base. Main:216, :654 and :774 still state the dependency-graph cone without the finite site set or the reading-set condition (F5), so the inconsistency moves rather than disappears.
*Fix.* Extend E.2 to the F5 sites once their rows are added.

### Recommended

**F21 (recommended). Introduction rows I-02 to I-05, I-07 and I-08 are not needed (minimum-change rule).** Introduction:34 already reads "The results about hidden worlds in sections 3 and 4 are proved for *finite models*, called *substrata* … Finiteness of the whole is an assumption of these models". Introduction:36 adds "A finite reversible world is the model under investigation". "World" and "substratum" are therefore defined as finite models. Mark these rows NC, giving that reason. Keep I-06's open-status sentence only if M-14's parallel is wanted.

**F22 (recommended). Disclaimer phrasing in paper prose.** Several additions state what the paper does not assert rather than stating the content and its status: "Finiteness of the hidden sector is not posited" (M-38), "that finiteness is not posited" (Y-02), "the rule is not asserted of nature" (U-06), "the theorem is not asserted of nature" (X-03), "it does not identify nature with a finite reversible substratum" (M-10 (3)), "a model condition not posited of nature" (G-03), "nothing is posited of nature's initial law" (M-46). They border on §A.30's "is not listed" family and on §A.32 meta-commentary. Prefer positive status ("The cardinality of the hidden sector is open: it is not derived from Lemma 1 …"), or remove the reading and keep the theorem with its finite-model hypothesis. The book essay chapters may keep "the framework does not posit …" in appendix C, where the objection asks for the position.

**F23 (recommended). M-36 (b): "on windows shorter than its recurrence time" is ambiguous** between the target and the realization. Use "by one fixed finite realization, on windows shorter than that realization's recurrence time".

**F24 (recommended). Locator fixes.** M-28's "(i) the dynamics is deterministic" is at Main:366 (the theorem header is on Main:364). K-appb-451/454: the second quoted fragment is on :454 only.

**F25 (recommended). Y-04 says "same wording in each", but the wording does not fit Methodology:253's grammar** ("bijectivity of $\varphi$ rests further on an empirical input and on A1 …"). Give per-site text.

**F26 (recommended). M-42 (Main:722):** "the hidden sector is a classical substratum — a deterministic system of undetermined cardinality, every finite-horizon visible law of which …" attributes visible laws to the hidden sector. Write "… a deterministic system of undetermined cardinality; every finite-horizon visible law it produces has finite reversible realizations (§3.4)".

**F27 (recommended). appendix-b:22 (FULL:5776; item 7 result).** "The framework's characterization theorem … relies on a chain of intermediate lemmas: partition-relativity, emergent stochasticity, P-indivisibility from a non-permutation witness, …". Main:632's proof uses the readback lemma, the process dilation and data processing, not the witness lemma. The sentence overstates the headline's dependence on a finite-recurrence result and bears on OQ-1's trace. Scope it ("the lemmas stated with it") or apply W2 to the witness lemma.

**F28 (recommended). P-05 (Computation:142): give the NC reason precisely.** "Hypercomputation through spacetime structure is closed as well: … unavailable on a finite lattice with $e^{S}$ states" is a claim about nature. It is A1-free only if $e^{S}$ is the patch budget of §4.5 (a named hypothesis); then say "under the patch-budget hypothesis". If it is the total lattice, it is A1-dependent and needs RR.

**F29 (recommended). `verification/README.md` (mutable; ~:317, :920, :926–:954, :1006–:1010)** speaks in the present tense of "the manuscripts' own structural assumptions A1–A6 of the Substratum paper, each quoted verbatim". After U-07 this describes a closed audit's quotation. No current claim relies on it, and R7-MAX and R7-RB1 pin the text, so NC is right. List it in D.3 with that reason, so that the Stage 2 propagation grep does not flag it.

**F30 (recommended). M-19 (Main:216):** the kept clause "its emergent dynamics lies in the near-unitary corner …, displaced … only by the residual dissipation $\mathcal D$ …, whose bath-motion term is $\mathcal O((\tau_S/\tau_B)^2)$" keeps the original's generality. The estimate is a slow-bath one (Main:340). Add "in the slow-bath regime" to avoid stating it for every finite reversible realization.

**F31 (recommended). Survivors to list in C-9 and G.1.** Lemma 1's own label "(Finiteness)" (Main:46, ch01:30) and Introduction:34's model statement survive legitimately. C-9 should name them, so that the "Finiteness" re-grep does not read them as missed.

***

## Item 4: #1312 consistency (summary)

- **M-04** matches Main:362's any-cardinality form: a finite reading set $N_i$, distance in a graph joining each site to the sites it reads. It claims no more.
- **M-05, M-37, M-54** match Main:414 part (2): nearest-neighbour cubic update, finite setting and readout regions, and condition (iv). A setting-independent pre-setting ensemble implies (iv) for the response table, as Main:416 states. They also match part (1) on a finite site set. M-05 states only part (2) in the abstract, which is narrower than Main and acceptable.
- **M-28** is consistent with part (1). The theorem's proof uses the cone lemma and a sum over $\Omega$, and its setting is the finite-$V$ setup of Main:362. Making the finite site set explicit narrows the statement to what is proved, and the theorem-recovery requirement is met by audit r9 AM-7 §3 (P4 candidate, gap stated).
- **G-13** keeps GR:585's deep-sector sentence ("only $\mathcal C_V$ and $\mathcal C_{B_n}$, a finite set of sites, need be finite, while the deep sector may be infinite given the normalized prior and dynamics stated there"). That agrees with (D1)–(D5) of GR:132 and does not assert infiniteness.
- **No row** cites Main:414 (2) as anything other than its own statement, and no recovery credit enters the text.
- **Gaps:** the restatements outside these rows (F5, F20).

## Item 5: counts

- **Correct:** C-1 (fourteen → thirteen at Main:728 only; no other site restates the ledger count); C-7 (F8 row only; F5 already absent; no F total anywhere); C-8 (55 lines with A1–A6 in papers and chapters, 65 with FULL, as audit r9 says).
- **Missed:** ch02:120 "six structural assumptions" (F6).
- **Incomplete:** ch09:118 carries "six commitments" twice; C-3 should name both occurrences, and ch09:118's FULL mirror is FULL:2585, which also has both.
- **Map-internal totals:** wrong (F19).

## Item 6: registry and records

- **Census (§A.35).** No kernel theorem is strengthened, so no supersession entry is needed (agreed). D-1a must be re-scoped (F9). D-1b and D-1c are agreed. For D-1d, the anchors on touched lines are kept verbatim in every row I sampled.
- **Coverage ledger.** D.2 is incomplete (F8), and K3 for MAIN:L-3 is at risk (F2). At the base, MAIN:L-3 is the only ledger entry whose fields name the posit (confirmed; the other "A1" hits are the irrep $A_1$).
- **Q14.** I agree that no manuscript-cited record premises A1. Substratum:346 and :361 cite audits that do not use it. Introduction:212 and :214 cite bh01 and bh02: the bh01 key `zero_advantage_bijections_satisfying_A1` belongs to the record's own claim labelling, and "A1" in bh02 is an amendment label. The records of AM-18, AM-26 and AM-35 are cited by no manuscript line. So no note is required under Q14 (c) qualified.
- **Glossary:13 pin.** Confirmed: `_A6P_GLOS_ENTRY` pins the whole entry, including "The sixth of the framework's structural assumptions A1–A6". OQ-3 must also cover R7-MAX and R7-RB1 (F9).

***

## Item 7: the writer's open reading tasks

| Task | Result |
|---|---|
| appendix-a:111 (G11 row) | NC. The row names "Nested trace-out, H-scramble (fails from configurations), H-decouple; full product space", Open; no cycle average and no A1 reading. |
| appendix-a:117 | It names the horizon calibration as a consistency relation "conditional on H-slope and the further conditions of [GR §8.5(b)]"; no finiteness. NC under OQ-2 (b); under (a) it would take the added condition. Follows OQ-2. |
| ch05:41 | NC. "Several results hold for every $q \geq 2$ … the P-indivisibility theorem …" is a statement about the model's $q$-independence. |
| ch05:95 | Needs W2 (F6). |
| appendix-b:12 | NC. A1-free ("constructed from a deterministic substratum bijection …"). |
| appendix-b:22 | Overstates the characterization's dependence on the witness lemma (F27). |
| ch14:90, :268 | Exact fixes in F15; ch14:92 also needs a row (F6). |
| SM Theorem 19, 13 SM uses | The negative uses (SM:649, :651, :655, :659, :667, :671, :1318) need nothing. The positive readings at SM:36, :1520, :1546, :1588, plus Sub:415 and the book mentions, need the counting prior named (F16). |
| SM:60 | Finiteness of $S$ follows from the construction's own A4 and site alphabets (SM:66): S-07 → NC (F14). |
| LEDGER: Bell ceiling theorem | No entry (header mid-line, not a census statement). |
| LEDGER: Main:439 lemma | `MAIN:L-non-permutation-witness` exists (level P); fingerprint moves under M-30; assumptions text to be rewritten (F8). |
| LEDGER: SM Proposition 4b | `SM:P-4b-…` exists (GAP); fingerprint moves under S-15. |
| LEDGER: Theorem 23 and Lemma 23.0 | `SUBSTRATUM:T-23` and `SUBSTRATUM:L-23.0` exist (GAP); fingerprints move under U-19 and U-18. |
| LEDGER: Structure Proposition 9.5 | `STRUCTURE:P-9.5` exists (GAP); fingerprint moves under T-08. |
| LEDGER: further entries the map did not name | `MAIN:T-statement`, `MAIN:C-observer-selection-rule-rate-condition`, `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer` (F8). |

## Item 8: owner questions

**OQ-1 (Main-root rule for the recurrence group).** Genuine. The options are right. I agree with recommendation (a) for 2a, with two corrections to the trace and one condition.

*Independent root trace.*
1. No headline proof uses the recurrence-cycle P-indivisibility theorems (Main:113–129, :135–139, :439), the routed-readback forcing sentence (Main:145) or the CP-indivisibility theorem (Main:326–332). The characterization theorem's proof (Main:632) uses the readback lemma, the process dilation and data processing. The equivalence theorem's proof (Main:556) uses the response-table construction and the permutation unitary. On these, the map's trace is right.
2. The **recurrence step** itself (a bijection of a finite set has finite order; rooted maps are periodic, `rootedMap_periodic`) is used by root-scoping results that B-5 keeps in Main. These are the consolidation (Main:642, "a bijection on a finite set has finite order $L$ …", kernel `pper_of_finiteRootedRealizable`) and the $t_R$ qualifier of the characterization theorem (Main:540, :544). M-10 (6) itself lists "the all-time periodicity of a fixed realization in §3.4" among the results resting on the recurrence step. So the group cannot move whole: Step 1 has to stay.
3. The characterization theorem's statement contains the clause "P-indivisibility determining not whether the representation exists but whether its dynamics is nontrivially indivisible (Remark below)". It points to Main:630, whose content is the recurrence-scale theorem. Under (b), that clause and Main:630 must be rewritten in the same change. Book appendix-b:22 claims the characterization "relies on" the witness lemma (F27).

*Condition.* Decide OQ-1 together with the headline deletions of F11, because those deletions create the root question.

**OQ-2 (counting link of the GR horizon calibration).** Genuine. Option (a) should be labelled as keeping total finiteness as a named hypothesis of a physical calibration. I disagree with the recommendation and recommend (b), using GR:669's existing "additional condition" wording; (c) is correctly marked inadmissible (F12).

**OQ-3 (guard pins).** Genuine to the extent that a guard edit lies outside the manuscripts. The options are right and I agree with (a). The scope must add R7-MAX and R7-RB1 (census family 13 note, `verification/README.md`), and the recommended action there is NC rather than an edit (F9).

**OQ-4 (book Chapter 7's bijectivity premise).** Not a genuine open question: Q5 (a) qualified decides it, as the map's own option (b) concedes. Remove it from Part F and apply Q5 (a) at the wider set of sites in F7.

**OQ-5 (bare `---` rules).** A genuine conflict between two AGENTS rules, but the premise is wrong: Main, SM and the book have none at the base. Restate with Methodology, Computation, Medicine and Bioinformatics (F13). Recommendation (a), a separate commit, is acceptable.

**Proposed addition: OQ-6.** A4's finite quotient lattice in 2a (F10).

***

## 2a/2b tagging (item 2)

- **U-09a/U-09b.** The split follows the 2026-11-15 rule, but Q3 (a)'s adopted text includes the A4 restatement, so the owner should confirm (F10).
- **G-10a/G-10b.** Agreed. G-10a restates the sentence as a statement about the monomial class, which is audit AM-27's treatment. G-10b reframes theory-general results and is 2b.
- **B-1/B-1r.** Agreed in form, but B-1's 2a tag depends on how F11 is resolved.
- **Mis-tagged 2a rows:**
  - the headline deletions and K-ch01-93 (F11);
  - M-08's added lemma clause, a reinterpretation of Lemma 3 (F2);
  - G-03's default under an undecided OQ-2 (F12).
- **All other sampled rows** are within 2a: removals, narrowings, count and reference corrections, and registry actions.

## Rows checked

- **All rows, automated.** Every quoted "Current" fragment in Parts A–D (274 fragments) was tested against the stated file and line. 26 did not match literally; on inspection, 25 are formatting differences (`\lvert`/`|`, `$\implies$`/`⟹`) or paraphrased locators, and one is the M-28 locator (F24).
- **Read in full against the text** (all Main, Introduction and GR rows): M-01 to M-56; I-01 to I-09; G-01 to G-19, G-10a and G-10b.
- **Sample of the other rows** (81 of 236, about 34%):
  - SM: S-01, S-02, S-05, S-07, S-09, S-12, S-15, S-16, S-17;
  - Substratum: U-01, U-04, U-06, U-07, U-08, U-09a, U-09b, U-10, U-13, U-18, U-19, U-21, U-22, U-23, U-31;
  - Structure: T-01, T-04, T-06, T-07, T-08, T-10, T-13;
  - Methodology: Y-01, Y-02, Y-03, Y-04, Y-07;
  - other papers: X-03, X-06, P-02, P-03, P-05, D-01;
  - book: K-pref-3, K-ch00-53, K-ch01-28, K-ch01-38, K-ch01-89/93, K-ch02-16, K-ch02-74, K-ch02-76, K-ch05-41/95, K-ch07-12…161, K-ch09-104/106, K-ch09-108, K-ch09-118, K-ch14-90/268, K-ch18-164, K-ch18-166, K-ch18-168, K-ch18-170/172, K-ch18-174–184, K-ch18-186/188/190, K-ch18-290, K-ch18-328, K-appa-111/117, K-appa-181, K-appb-12/22, K-appb-32, K-appc-112–134, K-gl-11, K-gl-13, K-ch19-212, K-bk-90;
  - records: R-03.

  All of Parts B, C and D were also checked.
- **Mirrors.** Every chapter-to-FULL offset in A.9 was verified by line matching (no mismatch except ch05's first heading lines, which carry no hit). No FULL-only hit exists for the search patterns.
- **Corpus search.** Run independently over `papers/*.md`, `book/*.md` (FULL by mirror), `README.md`, `book/README.md`, `verification/README.md`, the coverage ledger, the census JSON and string literals in `verification/lean/*.py` and `tools/*.py`, with the patterns of G.1 plus "six structural assumptions", "bijectivity premise", "information is never lost", "reciproc", "Malament", "infinite-resource", "CHSH" and "causal cone".

## What I could not check

- The guard and census tools were not run. The pin conflicts in F9 come from reading the guard source, not from a run.
- I did not read in full every line of the 101 book rows; the unsampled book rows were checked only by the quote test and the mirror test.
- Whether $e^{S}$ at Computation:142 denotes the patch budget or the whole lattice (F28) was not settled by reading.
- The audit's EF-1 drafts (off `main`) were not consulted.
