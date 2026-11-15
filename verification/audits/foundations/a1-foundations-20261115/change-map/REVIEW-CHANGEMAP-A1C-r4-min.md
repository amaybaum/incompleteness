# Review of change map A1C r4-min: the minimum-change policy

**Reviewer.** The independent reviewer of r1–r3. Paper-only: no repository file was edited, nothing was committed, pushed or posted, and no Lean, build, guard or census run was made. One exception: `tools/proof_census.py --json` was run read-only, to map edited lines to census statements.

**How I checked.** I compared r4 against r3 and against the manuscript text in the worktree of `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. I did not rely on the writer's reason codes. For every r3 corrective row that r4 reclassifies as "not an unsupported assertion", I opened the site and judged it in context, asking how an ordinary reader would read it. I treat Q5 (a) qualified, Q6 (a)+(e), Q7 (d), Q9 (c), Q10 (c), Q11 (a) and Q14 (c) as still standing; the map says the same.

## Verdict

**REVISE.**

r4 applies the owner's minimum-change policy carefully in most places:
- A4 is unchanged.
- No theorem statement or proof is altered, except where its wording asserted something about nature.
- The registry action is limited to the one census statement that changes.
- The 13 rows that change form because A1 stays use consistent "open hypothesis, not adopted" wording.
- Main:449 and the Bell and cone scope rows are correct.

The owner's safeguard is not met, however. Some unsupported assertions that r3 corrected are left in place:
- **15 of the 129 "not unsupported" reclassifications are wrong.** Read in context, those sites present total finiteness, or a finite-model conclusion, as a fact about nature.
- **Three dropped halves of split rows are wrong.** They drop sentences that make the same claim as the half that was kept.
- **Five kept rows leave a contradiction or an adoption claim in the same sentence or paragraph.**

OQ-2 (a) is consistent with the policy, but the map propagates it to 3 sites, when roughly 40 statements enumerate the calibration's conditions.

**Findings:** 2 blocking, 12 required, 9 recommended (23 in all).
**Reclassifications:** 114 of 129 agreed (seven of them with a consistency note); 15 disagreed.

***

## Findings

### Blocking

**F1 (blocking). Safeguard: 15 of r4's "not unsupported" reclassifications are wrong.**

Each site below, read in context, presents total finiteness of nature's substratum, or a finite-model conclusion, as a fact. Each needs a one-clause narrowing.

| r3 row | Site | Text at the base | Why the reason code fails | Minimal fix |
|---|---|---|---|---|
| S-01 | SM:14 (abstract) | "The Standard Model arises as a distinguished low-freedom representation of a finite bijection on a $d = 3$ simple-cubic lattice" | A claim about nature's Standard Model. r4 corrects the same synthesis claim at SM:1592 (N-S19) and Sub:367 (N-U26), so MOD is applied inconsistently. | delete "finite" (as N-S19) |
| S-18 | SM:1588 | "This paper has shown that the Standard Model's gauge group, matter content, and discrete symmetries are determined by a finite bijection on a $d = 3$ cubic lattice" | Says it has *shown* a fact about physics; same kind as SM:1592. | delete "finite" |
| U-01 | Sub:14 (abstract) | "The underlying object is the bijection $(S,\varphi)$ on a finite configuration space." | States nature's underlying object as finite. (The first sentence, "develops the alternative …", is a proposal and may stay, as GR:705 does.) | "…on a configuration space, finite under A1." or delete "finite" |
| U-02 | Sub:16 | "The synthesis claim is therefore structural …: the same finite deterministic object supports the visible …, the boundary-thermodynamic … and the lattice gauge projection" | The same synthesis claim r4 corrects at Sub:367. | delete "finite" (as N-U26) |
| U-03 | Sub:22 | "The underlying object is a finite deterministic bijection $(S, \varphi)$ on a configuration space partitioned into a visible sector accessible to an embedded observer …" | Nature's underlying object, which contains us as observers. | delete "finite" |
| U-04 | Sub:44 | "S is the set of all distinguishable states: *finite capacity*. … Together, $(S,\varphi)$ is a finite lossless memory." | A flat claim that nature's state set has finite capacity. Sub:44 is framing text, not inside Theorem 23. | "*finite capacity* (under A1)" |
| U-29 | Sub:389 | "The fundamental object is $(S, \varphi)$ — a finite set with a deterministic bijection —" | An ontological claim about nature's fundamental object. | "— a set (finite under A1) with a deterministic bijection —" |
| U-30 | Sub:429 | "The ontological hierarchy distinguishes the finite substratum from derived spatial, temporal and matter descriptions." | Ontology of nature. | delete "finite" |
| K-ch02-136/212 | ch02:136 (770), :212 (846) | ":136 There is no Lagrangian at the substratum level; the substratum is a finite set with a bijection on it"; ":212 The fundamental object is $(S, \varphi)$ — a finite set with a deterministic bijection on it —" | Book mirrors of the Sub:389 ontology. | as U-29 at :212; ":136 … the substratum is a set (finite under A1) with a bijection on it" |
| K-ch12-213 | ch12:213 (3453) | "The framework's substratum is a finite deterministic system; embedded observers within the substratum are themselves substructures of the substratum" | Nature's substratum, the one we observers live in. r4 corrects the parallel ch14:164 (N-K14-164). | "is, under A1, a finite deterministic system" |
| K-ch09-104/106 | ch09:104 (2571), :106 (2573) | ":104 The framework's universality-class commitments … are six structural properties of the substratum"; ":106 *Finiteness.* The substratum $S$ has finite cardinality." | Lists A1 as a "commitment" and states it flatly. This is exactly the adoption language that policy item 1 changes elsewhere. The label "LBL" does not apply: the sentence is not a label. | ":106 *Finiteness.* The substratum $S$ has finite cardinality — the open hypothesis A1, not adopted." (count and label unchanged) |
| K-ch05-41/95 | ch05:95 (1413) | "Main's readback lemma supplies that memory, and its recurrence-cycle theorem the P-indivisibility" (for the memory-bearing phenomenology) | Recurrence-scale P-indivisibility of the physical sector. r4 corrects the analogous ch01:93 (N-K01-93). | "…and, on finite reversible representatives, its recurrence-cycle theorem the P-indivisibility" |
| M-22 | Main:280 | "The observer's ignorance of the hidden sector (Lemma 3) corresponds to $\rho_H = I_m/m$." | Reads the maximal-entropy counting prior as nature's observer's epistemic state, which Q6 (a)+(e) still bars. N-M46 scopes ledger item (iv) "for constructed realizations", so this line now contradicts it. The RES reason cites Main:324, but Main:324 scopes the Main:292 realization, not Main:280. | "The default hidden prior of a constructed realization (Lemma 3) corresponds to $\rho_H = I_m/m$." |
| M-36 | Main:642 (b) | "(b) the physically operative form: quantitative approximation of the target on windows $t \ll t_R$ by one fixed substratum before its recurrence" | "Physically operative" presupposes that nature's substratum recurs, which is A1 adopted. No guard pins (b): R7-RCL pins (a). | "(b) the physically operative form under A1: …" |
| G-04 | GR:58 | "Restrict the finite total system to a conserved energy shell" | The definite "the finite total system" states the total system of the physical horizon as finite. The RES reason ("Tier 1 'finite deterministic system'; Appendix A setup") does not describe §2.3. | "Under A1, restrict the finite total system …" (this also anchors F12) |

**F2 (blocking). Safeguard: three dropped halves of split rows make the same claim as the half that was kept.**
- **ch07:118 (FULL:1984)**, dropped as "model". The text: "The framework's substratum is a deterministic bijection $\varphi$ acting on a finite configuration space $S$. Information is never lost from $\varphi$ — bijectivity is the framework's structural commitment to unitarity at the substratum level." This is the claim N-K07-12 corrects at ch07:110 (Q5 (a) qualified), plus finiteness stated as fact. *Fix:* "…acting on a configuration space $S$, finite under A1. Information is never lost from $\varphi$ in the framework's bijective models — bijectivity is the framework's structural commitment to unitarity in those models."
- **ch14:160 (FULL:3826).** The text: "Under the framework's reading, physical reality is *deterministic and classical* at the substratum level (the bijection $\varphi$ acts on a finite state space …)". This is the same claim N-K14-164 corrects two sentences later. *Fix:* "acts on a state space, finite under A1, …".
- **ch04:178 (FULL:1286).** The text: "the structural observer-selection theorem developed at Main §4.6 restricts observers to the non-equilibrium phase of the substratum's dynamics". This is the same Q7 (d) reading N-K04-36 corrects at :36 and :182. *Fix:* insert "for a finite bijective model" after "Main §4.6".

### Required

**F3 (required). Main:60, N-M10a: renaming the term leaves later uses without a definition.**
N-M10a renames the term at its defining site ("the total-finiteness posit" → "the total-finiteness hypothesis, which is open and not adopted"). Main:44, :111, :129, :222, :266 and :720 (unchanged, or N-M41), GR:585 ("posit (ii)") and the MAIN:L-3 ledger assumptions still say "the total-finiteness posit". They then name a term Main no longer defines.
*Fix (smaller and consistent):* keep the name and mark its status: "…item (ii) of the posit ledger (§4.5), the total-finiteness posit, an open hypothesis that is not adopted;". The conditional uses ("under the total-finiteness posit") then stay accurate with no further edits.

**F4 (required). ch01:41: the earlier narrowing is lost, and N-K01-41 contradicts itself.**
r4 keeps "The bijection requirement is structural: non-injective dynamics would merge distinct total states, erasing the observer's records". In the same paragraph, N-K01-41 adds "reversibility of nature's dynamics is not adopted as a postulate". The argument supports only injectivity on states that differ in registered content (Main:36, :60), as my r3 confirmation found.
*Fix:* restore r3's sentence: "The injectivity requirement is structural: dynamics that merged states differing in registered content would erase the observer's records of past outcomes — contrary to what observation is." This is the minimal correction of an unsupported claim about nature.

**F5 (required). GR:342 (N-G12) and ch19:212 (N-K19-212): an open hypothesis is listed as a commitment or an axiom.**
- GR:342 would read "…irreducible starting commitments (…, and the structural assumptions A1–A6, A1 being an open hypothesis)". That asserts a commitment and disclaims it in the same breath (§A.30).
- ch19:212 would read "The framework's axioms — deterministic bijectivity, finiteness (the open hypothesis A1), …".

*Fix:*
- GR:342: "…and the structural assumptions A1–A6, of which A1 enters as an open hypothesis rather than a commitment)".
- ch19:212: "The framework's axioms — deterministic bijectivity, causal partition, classical probability — together with the open hypothesis A1 of finiteness constrain the class."
- Apply the same to N-K09-36, "general structural axioms (finite substratum under A1, …)": "…axioms (deterministic bijection, classical probability, causal partition) with the open hypothesis A1 (finite substratum)".

**F6 (required). appendix-c:124 still says "which is posited".**
N-Kappc-C6 changes only the last sentence of :124. The earlier clause, "…does not establish finiteness of the whole of $S$, which is posited", stays, while the new last sentence says "it is not adopted".
*Fix:* "which is the open hypothesis A1". (Optional: :118 and :120 "Posit A1" → "A1"; see F15.)

**F7 (required). ch09:18: A1 is presented as a commitment.**
"The framework's specific commitments to a finite deterministic bijection are not equivalent to string theory's commitments" is commitment language (policy item 1). It was dropped as MOD within the K-ch09-18/36 split.
*Fix:* "…specific commitments to a deterministic bijection (finite under A1) are not equivalent…".

**F8 (required). Main:720 (N-M41): the kept clause presupposes that nature recurs.**
The unchanged tail reads "— physically indistinguishable from a timeless identity for all experiments well below the recurrence time". It speaks of physical experiments measured against a recurrence time, which presupposes A1 for nature. The inserted scope sentence covers "recurrence-scale conclusions", not this physical comparison.
*Fix:* "…well below the recurrence time of a finite representative", or delete the clause, as r3 did.

**F9 (required). Main:20 (N-M05): the edit instruction does not match the text.**
r4 says to insert "finite" before "wing region" and to write "readouts lie in finite regions". Main:20 reads "each read and write only their own wing" and "whose readouts lie outside the other wing's cone". There is no "wing region".
*Fix:* give the exact r3 replacement: "…each read and write only their own finite wing region, whose readouts lie in finite regions outside the other wing's cone…".

**F10 (required). OQ-2 (a) reaches 3 of about 40 condition lists.**
The calibration's condition list ("H-slope together with H-count, the horizon and frame conditions …") is restated in about 40 places:
- GR:12 (abstract), :24, :88, :316, :318, :611, :669, :701;
- SM:30, :1592; Structure:56; Substratum:191;
- ch00:21, :81, :97; ch01:87; ch02:190; ch03:120;
- ch07:14, :32, :52, :104, :106, :260, :262, :288, :307, :309, :313;
- ch08:272; ch09:14, :16, :48, :118, :226; ch19:116; appendix-b:196, :210.

r4 adds A1 at GR:28, ch07:12 and appendix-a:117 only. Under policy item 2, every companion restatement has to agree. A list that omits a condition a result uses is misleading under the safeguard.
*Fix (minimal):* attach A1 where H-count is stated, since every list names H-count:
- GR:58: "Under A1, restrict the finite total system …", per F1 / G-04;
- the H-count definition on the same line: "…the whole hidden sector at the shell scale, of a finite total system (A1), is the boundary count …";
- its book mirror at ch07:52;
- keep GR:28, ch07:12 and appendix-a:117 as drafted.

The lists that name H-count then inherit A1 without one edit each. If the owner prefers explicit lists instead, every site above changes.

**F11 (required). OQ-1 (a) leaves Struct:1293 mirroring the phrase N-M26 removes.**
Structure:1293 reads "[Main §3.2] states the mapping of their hypotheses to what the finite physical layer supplies". It quotes Main:356's phrase, which N-M26 changes to "The physical layer supplies".
*Fix:* "…what the physical layer supplies" (companion restatement, required propagation).

**F12 (required). The reason codes do not match the text in several rows.**
- M-22 cites Main:324 for Main:280 (F1).
- G-04 cites "Tier 1 … Appendix A setup" for GR:58 (F1).
- K-appc-16 and K-bk-100 are coded LBL, but the issue there is "posit" adoption language, not a label (F15).
- K-ch09-104/106 is coded LBL, but its text is a commitment claim (F1).
- K-ch14-92 is coded "ACC: no change in r3": correct.

*Fix:* correct the reason column wherever a finding above changes the disposition. Under the owner's request, reason codes must match the text.

**F13 (required). The Main:728 ledger's closing sentence now overstates.**
The ledger ends "this ledger states what is *assumed*, and the framework's claims are conditional on the full list". With (ii) marked "not adopted", "what is assumed" asserts and disclaims at once.
*Fix:* "…this ledger states what is assumed or, for item (ii), hypothesized, and the framework's claims are conditional on the full list".

**F14 (required). ch18:174: the period-bound paragraph still says "the substratum returns".**
r4 changes only the last sentence of :174. "After $N$ time steps, the substratum returns to its exact initial state" stays, contrary to Q10 (c), which r4 applies at :186. It is inside a conditional paragraph ("A bijection $\varphi$ acting on a finite set $S$ …"), but "the substratum" names nature's.
*Fix:* "After $N$ time steps, it returns to its exact initial state."

### Recommended

**F15.** Residual "posit" wording that presents A1 as adopted: appendix-c:16 ("whether the framework's posit A1 is too strong"), the :112 heading, :118 and :120 ("Posit A1 …"), readers-guide:79 ("the finiteness posit") and book README:100 ("finiteness posit defense"). Either keep "posit" as the name of ledger item (ii) and accept these sites (consistent with F3), or change each to "hypothesis A1". State which.

**F16.** Parallel sentences are handled differently. N-M40 corrects Main:714's comparison with other programmes ("derives this content from a finite deterministic substratum"). Its book analogues, ch09:300 and :314 ("operates with/uses a finite deterministic substratum"), and Structure:108 are kept as MOD. The distinction (Main has no A4; the book and companions do) is defensible but stated nowhere. State it in Part F, or treat the analogues alike.

**F17.** ch01:235 ("there is no 'outside' in a finite deterministic universe") and ch19:214 ("the existence of *some* finite deterministic bijection structure") read naturally of our universe. "under A1" would be a one-word safeguard.

**F18.** N-K07-12 gives one wording for five sites ("… a premise of the framework's models" at each). It does not fit :157 ("rests on bijectivity alone"). Give per-site text.

**F19.** The Main:64 title, "(reversibility as the conservative assumption)", sits above text that now says reversibility of nature "is not adopted as a postulate". r3 changed the title (no pin). Keeping it is minimal, but it reads as an adoption claim. Owner's call; note it.

**F20.** "(a condition [Main §3.3] states separately)" (N-U35) is meta-commentary in paper prose (§A.32). Use "(Main §3.3, Corollary, part (2))".

**F21.** Use one form for the status phrase. r4 uses "an open hypothesis, not adopted", "which is open and not adopted", "open" and "(an open hypothesis)". These are fine as status labels, but should be one form (§A.30: "if every other cell is two words …").

**F22.** OQ-A wording: say that option (b) would be the *smaller* edit at several sites (a conditional clause rather than deletion), so the owner sees the trade-off (see §6).

**F23.** The MAIN:L-3 ledger assumptions say "total-finiteness posit". Align them with F3's choice; if the name is kept, nothing changes.

***

## 1. The 129 reclassifications

**Agreed: 114.** Read in context, these sites are restrictive or conditional, are model statements, are theorems kept as stated, are already scoped, or are label sites.
- **M rows:** M-01, M-08, M-14, M-15, M-16, M-17, M-18, M-20, M-21, M-23, M-25, M-28, M-30, M-47, M-48, M-49, M-55, M-58, M-59.
- **G rows:** G-02, G-06, G-09, G-11, G-13, G-15, G-17, G-18.
- **S rows:** S-02, S-03, S-09, S-10, S-12, S-14, S-15.
- **U rows:** U-07, U-08, U-09b, U-10, U-13, U-15, U-16, U-18, U-19, U-20, U-21, U-23, U-24, U-28, U-31.
- **T rows:** T-01 to T-04b, T-05, T-06, T-07, T-08, T-10, T-11, T-13, T-15.
- **Y rows:** Y-01 to Y-04, Y-06, Y-07, Y-09.
- **X and P rows:** X-01, X-02, X-04, P-01, P-02.
- **Book rows:** K-rg-79, K-ch00-59, K-ch00-69, K-ch00-95, K-ch01-38, K-ch01-111, K-ch01-119, K-ch01-133, K-ch01-201, K-ch01-235, K-ch02-8, K-ch02-32, K-ch02-74, K-ch02-78, K-ch02-88/118/122, K-ch02-90, K-ch02-120, the :148 and :158 parts of K-ch02-136/148/158/212, K-ch03-34/44, K-ch03-36/102/114/240, K-ch04-94, K-ch04-210, K-ch05-25/77/83/89, the :41 part of K-ch05-41/95, K-ch09-14/42/61/84/118, K-ch09-108, K-ch09-298/300/314, K-ch14-6/12/34/146, K-ch14-100/105, K-ch18-164, K-ch18-168, K-appb-32, K-appb-40, K-appb-92, K-appb-451/454, K-appc-16, K-appc-224, K-appc-120, K-gl-13, K-bk-100.
- **Records:** R-01, R-03.

Seven of these carry a consistency note (F15–F17): K-rg-79, K-appc-16, K-bk-100, K-ch01-235, K-ch09-298/300/314, T-05 and G-18.

**Disagreed: 15.** S-01, S-18, U-01, U-02, U-03, U-04, U-29, U-30, K-ch02-136/212 (the :136 and :212 parts), K-ch12-211/213, K-ch09-104/106, K-ch05-41/95 (the :95 part), M-22, M-36, G-04. Each is in F1.

## 2. A1 open and unadopted

- **Consistent:** across the 13 "C" rows and N-M06, N-M38, N-M42, N-M44, N-U22, N-K02-16, N-K02-76, N-K05-23, N-K09-184 and N-Kgl-11.
- **Not yet consistent:**
  - adoption language in kept text: ch09:18, ch09:104/106, appendix-c:124, and the GR:342 and ch19:212 lists (F1, F5–F7);
  - the dangling term (F3).
- **Never disproved:** no row describes A1 as false or the substratum as infinite.

## 3. A4 and finite-model mathematics

- **A4 (Sub:98, :157):** unchanged.
- **Finite-model mathematics:** the period bounds (ch18:176–184), the recurrence theorems, Lemma 3, Theorem 23 and Lemma 23.0, Proposition 4b, Proposition 9.5, B.2.5, the cone and Bell theorems: all unchanged. N-K18-174 rewords only the "framework's substratum" sentence.

## 4. Theorems, lemmas and registry entries

- **Census statements touched:** the read-only census map of every line r4 edits finds one census statement in an edited body: `MAIN:C-observer-selection-rule-rate-condition` (Main:760, N-M51). N-D2d re-affirms it.
- **N-M51** deletes only the "past hypothesis … replaced" clause. The corollary's conclusion ("observers exist where (C1)–(C4) … are satisfiable …") is kept.
- **Main:449 (N-M31)** is in the ETH "physical motivation" paragraph, not a theorem, and its Hamiltonian clause is kept.
- **GR:342** is not a theorem.
- **No theorem's assumptions, conclusions or dependencies change.**
- **Census anchors and guard pins:** all are kept.

## 5. The 264 dropped rows

By reason code:
- the 2B rows are correct under OQ-1 (a);
- the ACC rows were no-change rows in r3;
- the LBL rows are correct only where the site is a label, range or count (not K-ch09-104/106);
- the registry and record rows are correct (their statements are not edited).

Every drop whose r3 row was corrective is among the 129 above or among the split halves in F2, and I opened each. The splits in Part E are coded generically ("MOD/RES"); the three in F2 are wrong.

## 6. OQ-2 and OQ-A

**OQ-2 (a).** Consistent with the policy: naming A1 among a result's conditions narrows the result and keeps A1 open. It is also consistent with Q9 (c) and Q10 (c). Those decisions removed conditionals that have no accessible content once $|S|$ is free; the calibration's content ($\epsilon/\sqrt\sigma = 2\,l_p$) does not depend on $|S|$. Applied at three sites, though, it is incomplete (F10). With F10's anchoring in H-count it becomes a complete minimal change.

**OQ-A.** Genuine. Keeping A1 as an open hypothesis reopens the Q9 (a) and Q10 (b) forms, and the policy's "narrow that sentence" favours the smaller edit. The options are right, and recommendation (a) is sound, because the owner has not revised Q9 (c) or Q10 (c) and their reason (no accessible test) still holds. The question should state the trade-off (F22).

## 7. Mirrors and registry

- **Mirrors:** every book row names its FULL line, and the offsets match the line-matching check of r1. No FULL-only site exists. The companion restatement Structure:1293 is missing (F11).
- **Registry:** N-D2d is needed and sufficient. N-D2x is a correct placeholder for the Stage 2 coverage run.

## 8. Register

- The new paper wording has no §A.33 caps or history phrases.
- §A.30 is breached where an adoption claim and its disclaimer sit together (F5, F6, F13).
- One meta parenthetical (F20).
- The status phrase varies in form (F21).

## What I could not check

- No guard, census, coverage or build run was made. Pin and anchor statements come from reading the sources.
- F10's list of calibration restatements comes from a search for "H-count". Lists that name the calibration's conditions without that word may exist.
- I did not read every one of the 98 kept rows' replacement texts in full context; Main, GR and the F-findings sites were read.
