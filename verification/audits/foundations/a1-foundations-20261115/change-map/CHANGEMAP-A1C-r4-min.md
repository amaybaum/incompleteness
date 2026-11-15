# Change map A1C r4-min: the general A1 correction under the minimum-change policy

**Status.** Stage 1, paper-only, unreviewed. Derived from the confirmed r3 (kept unchanged) by applying the owner's minimum-change policy of 2026-11-15 (#1169, latest record comment: "Confirmed, proceed as suggested"). Nothing in the repository was edited, committed or pushed; no repository check, build or Lean run was made. Base: `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`; line numbers as in r3.

**How the policy is applied.**

| Policy item | Application in this map |
|---|---|
| 1. A1 kept as an open, unadopted hypothesis (revises Q4 (a), Q3 (a)) | Ledger item (ii) stays and is marked "an open hypothesis, not adopted" (N-M44); the label "A1", the range "A1–A6", the property "Finiteness" and every count that depends on them stay. Sites that present total finiteness as adopted ("posit", "commitment", "postulates", "axioms", "supported by E3") say instead that it is the open hypothesis A1. Sites that state a result "under the total-finiteness posit", or that name A1 as a hypothesis, are accurate and untouched. |
| 2. Change only sentences that present a finite-model conclusion as a fact about nature | Each Part A row names the claim it corrects and narrows that sentence only, usually by one clause ("under A1", "on a finite representative", "for a finite bijective model") or by deleting the word "finite" where the sentence is about nature or Main's substratum. Statements about OI's specific representative or reconstructed class (finite through A4 and through A1 as a hypothesis of Theorem 23), restrictive statements ("an observer embedded in a finite deterministic system …") and conditional statements are untouched. |
| 3. Theorem statements and proofs kept | No theorem or lemma statement is edited except where its wording asserts something about nature (none remains: Lemma 3, the Bell ceiling theorem, the non-permutation-witness lemma, Theorem 23, Lemma 23.0, Proposition 4b, Proposition 9.5, B.2.5 are all kept). The two named examples are narrowed: Main:449 (N-M31) and GR:342 (N-G12). |
| 4. A4 unchanged (OQ-6 (a)) | Sub:98 untouched; OI's specific representative is a finite model through A4. |
| 5. No unrelated cleanup | No formatting (OQ-5 (b): no `---` switch), no renaming (the Main:64 Remark keeps its title), no headings changed, no recounts. Required propagation kept: chapter ↔ FULL mirrors, companion restatements of each corrected sentence, and the registry entry of each changed census statement in the same commit (Q13 (a)). OQ-1 = (a): no headline deletion, no relocation. |
| OQ-2, decided by necessity | **(a)**: the calibration of $\hbar$, $\epsilon$ and the $1/4$ coefficient is applied to nature's horizon while its counting step (GR:58) uses a finite total system; the minimal correction is to name A1 among its conditions (one clause at GR:28, propagated to ch07:12 and appendix-a:117). Option (b) would restructure the calibration's support and is not needed now that A1 stays as a hypothesis. |
| OQ-3, decided by necessity | **No guard edit**: with the label kept, glossary:13 and every pinned phrase are untouched; R7-MAX, R7-RB1 and `_A6P_GLOS_ENTRY` need nothing. |
| Decisions not revised by the policy | Q5 (a) qualified, Q6 (a)+(e), Q7 (d), Q9 (c), Q10 (c), Q11 (a), Q14 (c) qualified, Q15 (b) stand and are applied minimally: the predictions withdrawn by Q9 (c) and Q10 (c) are deleted, not re-stated as conditionals (see OQ-A). |
| 6. Safeguard | Every corrective row of r3 is accounted for in the check table (Part H): either corrected here (row named) or shown not to be an unsupported assertion under the policy (reason given). |

**Counts.** r3 rows (Parts A–D, 368): kept 83, changed 9, split 12 (one sentence kept, the rest dropped; Part E), dropped 264 (Part F). Resulting rows in this map: 111 (98 kept, 13 changed), of which 109 manuscript rows and 2 registry rows; all are stage 2a in the r3 sense (no 2b row survives). Check table: 235 corrective rows of r3; 106 corrected here, 129 shown not to be unsupported assertions under the policy.

**Reason codes (DROP ledger, check table).** ACC accurate as worded or no change in r3 · RES restrictive or conditional statement (names the finite hypothesis, or says "under the posit", "on a finite representative") · MOD statement about OI's finite model, specific representative or reconstructed class (finite through A4 and A1 as a hypothesis) · THM theorem or proof kept (policy 3), accurate in its stated setting · SCP already scoped ("the substratum's stated interventions") · LBL only re-labels or retires A1, "A1–A6" or "Finiteness", or recounts because of it · 2B restructuring or relocation · CLN editorial.

**Status codes.** K kept (corrects an unsupported claim), C changed in form because A1 stays (the ledger entry and the sites that present A1 as adopted).

***

## Part A. Rows kept or changed

### A.1 `papers/Main.md`

| ID | Site | Unsupported claim corrected | Minimal change | From r3 | Status | Propagation |
|---|---|---|---|---|---|---|
| N-M04 | Main:20 | Exact causal cones stated for every spatial OI system, though at any cardinality Main:362 proves them only with finite reading sets | "For spatial OI systems, the coupling graph …" → "For spatial OI systems in which each site's update reads a finite set of sites, influence propagates at most one edge per update of the graph joining each site to the sites it reads, so the dynamics supplies exact causal cones." (wording reviewed in r2/r3) | M-04 | K | N-M57, N-U33, N-K01-16 |
| N-M05 | Main:20 | The Bell ceiling stated for every deterministic completion, though it is proved on a finite site set (§3.3) and, at any cardinality, only for the nearest-neighbour cubic update with finite regions (Main:414 (2)) | insert "for the nearest-neighbour cubic update on a site set of any cardinality," before "a deterministic completion", and "finite" before "wing region" and "readouts lie in finite regions" (r3 wording) | M-05 | K | N-M37, N-M54, Bell rows |
| N-M06 | Main:36 | Total finiteness presented as a posit of the framework | "and total finiteness of that representative is a posit (status Remark, §1.2; ledger §4.5)" → "and total finiteness of that representative is an open hypothesis, not adopted (status Remark, §1.2; ledger §4.5, item (ii))" | M-06 | C | N-M44 |
| N-M07 | Main:44 | "finiteness … is the load-bearing commitment", read as total finiteness | "finiteness, not the dynamics, is the load-bearing commitment" → "finiteness of the visible sector (Lemma 1), not the dynamics, is the load-bearing commitment" | M-07 | K | N-K01-28 |
| N-M09 | Main:58 | The physical realization (nature) said to use the maximal-entropy counting measure | delete "and the physical realization" ("…baseline transition matrices (§2.3) use it.") | M-09 | K | N-G01b |
| N-M10a | Main:60 | Total finiteness presented as an adopted posit | "carried as item (ii) of the posit ledger (§4.5), the total-finiteness posit;" → "carried as item (ii) of the posit ledger (§4.5), the total-finiteness hypothesis, which is open and not adopted;" | M-10 (2) | C | N-M44 |
| N-M10b | Main:60 | The fixed-realization obstructions said to bear on nature (Q9 (c)) | delete "; the obstructions stated in §3.4 for a fixed finite realization bear on nature through it" | M-10 (6) | K | — |
| N-M10c | Main:60 | "so $\varphi$ is a bijection" asserted of nature's dynamics from finiteness | "On a finite set, injectivity implies surjectivity, so $\varphi$ is a bijection." → "…so on a finite representative $\varphi$ is a bijection." | M-10 (7) | K | — |
| N-M10d | Main:60 | Uniqueness and selection of the measure stated for "the orbit of the actual microstate", which presupposes a finite carrier | "As for the measure: on the orbit of the actual microstate" → "As for the measure on a finite representative: on the orbit of the actual microstate" | M-10 (8) | K | N-M46 |
| N-M11 | Main:64 | Bijectivity of nature presented as an imported assumption the framework recovers (Q5 (a) qualified) | opening → "The bijectivity of the constructed realizations — equivalently, that they conserve information — mirrors the orthodox assumption of mainstream physics rather than an exotic commitment peculiar to this framework." ("imported here rather than invented" deleted); "The framework therefore assumes no more than standard physics already does." → "The framework's constructed realizations are bijective by construction; reversibility of nature's dynamics is not adopted as a postulate."; last sentence → "What is non-standard here is the recovery of part of it from the two-pronged argument of Lemma 3: injectivity on states that differ in registered content; injectivity of nature's dynamics on the hidden sector is open, and the emergence results of §3.4 do not use it." Title unchanged. | M-11 (r3 wording, title change dropped) | K | N-K01-41 |
| N-M19 | Main:216 | Corner occupancy of nature and its "prediction" (Q9 (c)) | delete the two sentences "What appears as a restriction … conditional on the total-finiteness posit (§1.2 Remark, §4.5 ledger)." and "This is explanatory unification … the corner-occupancy claim's falsifiable residue." | M-19 | K | — |
| N-M57 | Main:216 | Exact graph causal cones stated without finiteness of the site set or of reading sets | after "exact graph causal cones" insert ", with finitely many sites or with each site's update reading a finite set of sites (§3.3)" | M-57 | K | N-M04 |
| N-M26 | Main:356 | "The finite physical layer" — the physical layer presented as finite | "The finite physical layer supplies" → "The physical layer supplies" | M-26 | K | — |
| N-M31 | Main:449 | "The substratum dynamics is reversible" asserted of nature | "The substratum dynamics is reversible, so" → "For a finite reversible realization" (owner's named example) | M-31 | K | — |
| N-M33 | Main:592 | "the concrete OI substratum … its finite states and bijective dynamics" presents the substratum's finiteness as fact | after "the concrete OI substratum" insert ", in its finite model (ledger item (ii))," — census anchors and kernel identifiers untouched | M-33 | K | N-K01-165, N-K19-126, N-G10a |
| N-M35 | Main:630 | Recurrence-scale P-indivisibility of nature stated "unconditionally" | "unconditionally at the recurrence scale" → "on finite representatives at the recurrence scale" (guard phrase "non-permutation one-step witness" kept) | M-35 | K | — |
| N-M37 | Main:654 | Graph causal separation and Bell factorization stated without their scope | after "from the dependency graph" insert "with finitely many sites or with finite reading sets"; after "Bell adds a sharper restriction" insert "on a finite site set, and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality (§3.3)" | M-37 | K | N-M05 |
| N-M38 | Main:704 | Finiteness of the hidden sector "is posited" | "Finiteness of the hidden sector is posited in the forward construction, as item (ii) of the posit ledger (§4.5)" → "Finiteness of the hidden sector is the open hypothesis of the forward construction, item (ii) of the posit ledger (§4.5), not adopted"; "compatible with the finiteness assumed here" → "compatible with the finiteness hypothesized here" | M-38 | C | N-M44 |
| N-M39 | Main:710 | "the substratum is a finite configuration space" (Main's own substratum, whose cardinality §1.2 leaves open) | delete "finite" | M-39 | K | — |
| N-M40 | Main:714 | "a finite substratum", "a finite deterministic substratum" in the comparison with other programmes | delete "finite" at both | M-40 | K | — |
| N-M41 | Main:720 | Recurrence-scale P-indivisibility and a recurrence time stated of nature | first sentence after "**The theorem** requires …": "The P-indivisibility proof uses total finiteness (the total-finiteness posit, §1.2 Remark, §4.5 ledger) via the recurrence argument ($\varphi^N = \text{id}$)." → "The P-indivisibility proof uses total finiteness (ledger item (ii), an open hypothesis) via the recurrence argument ($\varphi^N = \text{id}$), so its recurrence-scale conclusions are statements about finite representatives." Rest unchanged. | M-41 (smaller) | K | — |
| N-M42 | Main:722 | The falsifiable structural claim includes finiteness "being the total-finiteness posit" | "— a finite set with a deterministic bijection, finiteness being the total-finiteness posit (§1.2 Remark, §4.5 ledger item (ii))" → "— a deterministic bijection on a set whose finiteness is the open hypothesis of §4.5 ledger item (ii)" | M-42 | C | — |
| N-M43 | Main:724 | "its deterministic finite ontology" | delete "finite" | M-43 | K | — |
| N-M44 | Main:728 item (ii) | Total finiteness listed as a posit in force | after "(ii) total finiteness of the bijective representative of the status Remark of §1.2" insert " — an open hypothesis, not adopted —"; the rest of the item (its scope, consumers, and the statement that §2.3's recurrence-scale conclusion concerns finite representatives) unchanged | M-44 | C | C-1; N-M06, N-M10a, N-M38, N-P03, book "posit A1" rows |
| N-M45 | Main:728 item (iii) | The hidden-sector margin of injectivity said to be closed, which uses a finite map (item (ii)) | after "close the hidden-sector margin" insert " on a finite representative (item (ii))" | M-45 (smaller) | K | N-M60 |
| N-M46 | Main:728 item (iv) | The maximal-entropy counting selection read as nature's measure (Q6 (a)+(e)); on an infinite carrier it is not normalizable | after "the measure selection" insert " for constructed realizations (§1.2 Remark)" | M-46 (smaller) | K | N-K01-85, N-P04 |
| N-M60 | Main:728 (after the ledger) | "the injectivity recovery closes its hidden-sector margin with an empirical input" (unscoped) | insert "on a finite representative" after "closes its hidden-sector margin" | M-60 (smaller) | K | N-M45 |
| N-M50 | Main:746 | §4.6 rule "replaces" the past hypothesis for nature (Q7 (d)) | delete "The rule replaces a postulate often imported from elsewhere — the "past hypothesis" of low initial entropy, in its role of selecting observer-compatible configurations — with a theorem" and begin "For such an $(S,\varphi)$ the rule is a theorem conditional on …" | M-50 | K | N-U06, N-U27 |
| N-M51 | Main:760 (end) | Same replacement claim in the observer-selection corollary | delete "The low-entropy initial condition commonly imported as a "past hypothesis" to select observer-compatible configurations is replaced here, within that description, by a structural selection rule:" and begin "Within that description, observers exist where …" | M-51 | K | D-2d |
| N-M54 | Main:774 | Causal-cone result and Bell locality without their scope | first sentence → "The spatial theory adds an exact causal-cone result, for finitely many sites or with finite reading sets (§3.3)."; after "Bell locality then follows" insert ", on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality," | M-54 | K | N-M05 |

### A.2 GR, SM, Substratum, Methodology, Complexity, Computation

| ID | Site | Unsupported claim corrected | Minimal change | From r3 | Status | Propagation |
|---|---|---|---|---|---|---|
| N-G01b | GR:20 (ii) | "which the physical realization uses" (mirror of Main:58) | delete ", which the physical realization uses" | G-01b | K | N-M09 |
| N-G03 | GR:28 | The $\hbar$, $\epsilon$ and $1/4$ calibrations, applied to nature's horizon, omit the finiteness of the total system that the counting step of §2 (GR:58) uses | in the list of named conditions insert "A1 (an open hypothesis) for the counting derivation of §2," after "together with H-count," (OQ-2 decided by necessity: (a), one clause) | G-03 | K | N-K07-12b, N-Kappa-117 |
| N-G10a | GR:256 | "The concrete OI substratum — finite states and bijective microscopic dynamics —" presents finiteness as fact | after "The concrete OI substratum" insert " under A1" (anchors and guard phrases untouched) | G-10a (smaller) | K | N-M33 |
| N-G12 | GR:342 | "irreducible starting commitments (… the structural assumptions A1–A6)" makes A1 a commitment (owner's named example) | "…and the structural assumptions A1–A6)" → "…and the structural assumptions A1–A6, A1 being an open hypothesis)" | G-12 | C | — |
| N-S20 | SM:36, :1520, :1546, :1588 | Reciprocal transition counts asserted of nature with no hidden prior, though Theorem 19 assumes the counting prior on a finite hidden space | insert "under the counting hidden prior of a finite model" after "reciprocal (visible) transition counts" at each | S-20 | K | N-U38, book reciprocity rows |
| N-S19 | SM:1592 | The synthesis "claim" that SM and GR are projections of "one finite deterministic construction" | delete "finite" | S-19 | K | N-U26 |
| N-U06 | Sub:56 | Observer selection replaces the past hypothesis, read of nature (Q7 (d)) | after "In that description," insert " for a finite bijective $(S,\varphi)$," | U-06 (smaller) | K | N-M50 |
| N-U22 | Sub:216 | "A1 (finiteness) is supported by E3", contradicting Sub:92 ("This bound alone does not establish finiteness of every underlying sector") | "is supported by E3" → "is motivated by E3, which does not establish it (A1 above)" | U-22 | K | N-K04-26 |
| N-U26 | Sub:367 | "quantum mechanics and general relativity are … projections of the same finite deterministic construction" asserted of physics | delete "finite" | U-26 | K | N-S19, N-K02-184, N-K03-196 |
| N-U27 | Sub:401, :407 | §4.6's selection content applied to nature's $(S,\varphi)$ | :401 "applied to the same underlying $(S, \varphi)$" → "applied to the same underlying $(S,\varphi)$ as a finite bijective model"; :407 after "via Main §4.6" insert " for a finite bijective $(S,\varphi)$" | U-27 (smaller) | K | N-M50 |
| N-U33 | Sub:14 | "Its spatial coupling graph supplies finite causal cones" without the reading-set condition | add " for finite-range couplings" | U-33 | K | N-M04 |
| N-U34 | Sub:48, :171, :467 | Bell ceiling restated without its scope; cone at :467 | insert the Bell scope of N-M37 at each Bell conclusion; :467 "gives an exact causal cone" → "…for finite-range couplings" | U-34 | K | N-M05 |
| N-U35 | Sub:131 | "reference graph" Bell-local without the finite-region condition of Main:414 (2) | after "graph cone" insert ", with finite setting and readout regions (a condition [Main §3.3] states separately)," | U-35 | K | N-Y11 |
| N-U38 | Sub:415 | Reciprocity of visible counts as a fact of the T-symmetric substratum | insert "under the counting hidden prior of a finite model" after "visible transition counts" | U-38 | K | N-S20 |
| N-Y05 | Meth:162, :283 | §4.6 selection presented as a rule on where observers exist in nature (Q7 (d)) | :162 after "can exist" insert " in a finite bijective model"; :283 after "admit embedded observers" insert " in a finite bijective model" | Y-05 | K | — |
| N-Y08 | Meth:357 | "the framework's finiteness" presented as adopted | "the framework's finiteness makes available" → "the framework's finiteness hypothesis A1 makes available" | Y-08 (smaller) | K | — |
| N-Y11 | Meth:339, :381, :385, :389, :391 | Bell restatements without scope | :339 add "with finite setting and readout regions" after "graph cone"; insert the Bell scope of N-M37 at the Bell conclusions of :381, :385, :389, :391 | Y-11 | K | N-M05 |
| N-X03 | Complexity:212 | Boltzmann-brain problem "dissolved" for nature by §4.6 (Q7 (d)) | "is also dissolved at the framework level" → "is also dissolved, for a finite bijective model, at the framework level" | X-03 (smaller) | K | N-M50 |
| N-X05 | Complexity:374 | "Genuine P-indivisibility is a property of the *closed substratum*" (recurrence-scale, of nature) | "Genuine P-indivisibility is" → "Genuine P-indivisibility is, under A1," | X-05 (smaller) | K | — |
| N-X06 | Complexity:434 | "the framework-distinctive prediction, that this memory is specifically P-indivisible" — its derivation rests on A1 | "the framework-distinctive prediction, that" → "the framework-distinctive prediction, conditional on A1, that" | X-06 (smaller) | K | — |
| N-P03 | Computation:118 | "The total-finiteness posit … takes $S$ finite" presented as adopted | "The total-finiteness posit ([Main] §1.2, §4.5), however, takes $S$ finite." → "The total-finiteness hypothesis ([Main] §1.2, §4.5, item (ii), open), however, would take $S$ finite." | P-03 | C | N-M44 |
| N-P04 | Computation:120 | "the substratum measure is the unique $\varphi$-invariant maximal-entropy measure" (nature's measure) | after "the substratum measure" insert " of a finite representative" | P-04 (smaller) | K | N-M46 |
| N-P06 | Computation:180 | "The framework's finiteness commitment — that the substratum has finitely many tokens at any moment —" | "finiteness commitment" → "finiteness hypothesis (A1)" | P-06 (smaller) | K | — |

### A.3 Book (each chapter line with its FULL mirror, byte-identical, §A.14; FULL line in parentheses)

| ID | Site (FULL) | Unsupported claim corrected | Minimal change | From r3 | Status |
|---|---|---|---|---|---|
| N-K01-28 | ch01:28 (363) | mirror of Main:44 | as N-M07 ("finiteness of the visible sector (Lemma 1), not the dynamics, is the load-bearing commitment") | K-ch01-28 | K |
| N-K01-41 | ch01:41 (376) | mirror of Main:64 (bijectivity of nature as assumed) | "the reversibility of $\varphi$ — equivalently, that the substratum conserves information — is not a peculiar demand of this framework but the standard assumption of mainstream physics" → "the reversibility of the constructed realizations — equivalently, that they conserve information — mirrors the standard assumption of mainstream physics rather than a peculiar demand of this framework"; "The framework assumes no more than standard physics already does; what is distinctive, developed below, is not the assumption but what emerges from it." → "The framework's realizations are bijective by construction, and reversibility of nature's dynamics is not adopted as a postulate; what is distinctive, developed below, is what emerges from them." | K-ch01-41 (smaller) | K |
| N-K01-85 | ch01:85 (420) | the counting selection read as nature's measure | after "The selection is a principle the framework adopts" insert " for constructed realizations" | K-ch01-85 | K |
| N-K01-93 | ch01:93 (428) | chapter's central result stated as P-indivisibility of nature's marginalized process | after "is that" insert ", on a finite reversible representative," | K-ch01-93a | K |
| N-K01-165 | ch01:165 (500) | mirror of Main:592 | as N-M33 (guard phrases kept) | K-ch01-165 | K |
| N-K01-181 | ch01:181 (516) | "Because the physical representative is finite and reversible, it also recurs" | "Because the physical representative is finite" → "Because the physical representative is, under A1, finite" | K-ch01-181 | K |
| N-K01-16 | ch01:16 (351), :183 (518) | cone and Bell without scope | :16 "gives exact causal cones" → "…for finite-range couplings"; Bell conclusions at :16, :183: insert the Bell scope of N-M37 | K-ch01-16/183 | K |
| N-K02-16 | ch02:16 (650) | "$S$ is a finite set (posit A1, §2.4)" presents A1 as adopted | "$S$ is a finite set (posit A1, §2.4)" → "$S$ is a set, finite under the open hypothesis A1 (§2.4)," | K-ch02-16 (smaller) | C |
| N-K02-76 | ch02:76 (710) | "the extension to all of $S$ is a posit, … supported by E3" | "is a posit" → "is an open hypothesis, not adopted"; "supported by E3" → "motivated by E3" | K-ch02-76 | C |
| N-K02-184 | ch02:184 (818) | "projections of the same finite deterministic construction" (physics) | delete "finite" | K-ch02-184 | K |
| N-K02-192 | ch02:192 (826) | §4.6 selection theorem applied to nature's horizon projection | after "The structural observer-selection theorem developed in Chapter 1's appendix material" insert " for a finite bijective model" | K-ch02-192–200 (smaller) | K |
| N-K03-22 | ch03:22 (887) | "what is derived from it: a finite deterministic substratum" — finiteness presented as derived | delete "finite" | K-ch03-22 | K |
| N-K03-58 | ch03:58 (923) | Boltzmann brains "structurally excluded" for nature | after "is dissolved at Level B" insert " for a finite bijective model" | K-ch03-58/62 (smaller) | K |
| N-K03-196 | ch03:196 (1061) | "projections of the same finite deterministic substratum" (physics) | delete "finite" | K-ch03-84/… split | K |
| N-K03-40 | ch03:40 (905), :162 (1027), :180 (1045), :186 (1051) | Bell restatements without scope | :40 add "with finite setting and readout regions"; :162, :180, :186 insert the Bell scope of N-M37 | K-ch03-40/162/180/186 | K |
| N-K04-26 | ch04:26 (1134) | "A1 is supported by the holographic entropy bound" | "A1 is supported by" → "A1 is motivated by" | K-ch04-10/22/26 split | K |
| N-K04-36 | ch04:36 (1144), :182 (1290) | observer selection by §4.6 read of nature | after "the structural observer-selection theorem of Chapter 1" (:36) and "the observer-selection theorem's restriction of observers to the non-equilibrium phase" (:182) insert " for a finite bijective model" | K-ch04-36/178/182 split | K |
| N-K04-116 | ch04:116 (1224), :166 (1274) | reciprocity without prior | as N-S20 | K-ch04-116/166 | K |
| N-K05-23 | ch05:23 (1341) | "a finite set $S$ (posit A1, Chapter 2 §2.4)" | "(posit A1, Chapter 2 §2.4)" → "(finite under the open hypothesis A1, Chapter 2 §2.4)", "a finite set" → "a set" | K-ch05-11/15/23 split | C |
| N-K05-194 | ch05:194 (1512) | reciprocity without prior | as N-S20 | K-ch05-194 | K |
| N-K06-10 | ch06:10 (1523) | reciprocity without prior | as N-S20 | K-ch06-10 | K |
| N-K07-12b | ch07:12 (1878) | $\hbar$ calibration conditions omit A1 (propagation of N-G03) | after "together with H-count" insert ", A1 (open) for the counting step" | NEW (propagation of OQ-2) | K |
| N-K07-12 | ch07:12 (1878), :110 (1976), :157 (2023), :159 (2025), :161 (2027) | "bijectivity being a premise" of the framework, read of nature (Q5 (a) qualified) | "bijectivity being a premise" / "bijectivity is a premise of the framework (Chapter 1)" / "rests on bijectivity (alone / as a premise)" → "… a premise of the framework's models" at each | K-ch07-12/… (ch07:118 dropped: model) | K |
| N-K09-36 | ch09:36 (2503) | "the framework's general structural axioms (finite substratum, …)" — finiteness as an axiom | "(finite substratum," → "(finite substratum under A1," | K-ch09-18/36 split | K |
| N-K09-129 | ch09:129 (2596) | "follows from the bijectivity premise" | "the bijectivity premise" → "the bijectivity premise of the framework's models" | K-ch09-129 | K |
| N-K09-184 | ch09:184 (2651) | "it postulates a finite configuration space" | "it postulates a finite configuration space" → "it takes, under the open hypothesis A1, a finite configuration space" | K-ch09-184/190/194 split | C |
| N-K14-90 | ch14:90 (3756), :268 (3934) | infinite-time computation "precluded" by the framework's finite substratum (structural exclusion of nature) | :90 "which the framework's finite substratum precludes (a structural exclusion)" → "which the framework's finite substratum precludes under A1 (a structural exclusion conditional on A1)"; :268 "The framework's finite substratum and bounded-coupling-degree commitments preclude" → "The framework's finite substratum (under A1) and bounded-coupling-degree commitments preclude" | K-ch14-90/268 (smaller) | K |
| N-K14-164 | ch14:164 (3830) | "the universe is a deterministic finite system at the substratum level" | "is a deterministic finite system" → "is, under A1, a deterministic finite system" | K-ch14-160/164 split | K |
| N-K18-20 | ch18:20 (4826), :28 (4834), :162 (4968) | cosmic recurrence as "a definite structural prediction" (Q10 (c)); "substratum commitments — finite information" | :20 after "Section 18.7 develops" insert ", under A1," and delete "— a definite structural prediction with real conceptual content, and without practical consequences at periods of astronomical size"; :28 delete "cosmic recurrence, at a period at most $g(\lvert S\rvert)$, and"; :162 "finite information" → "finite information under A1" | K-ch18-20/28/162 | K |
| N-K18-40 | ch18:40 (4846) | "the finite reversible substratum dynamics, which is recurrent" | "which is recurrent (§18.7)" → "which is recurrent under A1 (§18.7)" | K-ch18-40 | K |
| N-K18-166 | ch18:166 (4972) | "The framework's commitment to a finite substratum …"; "The universe is described by a finite configuration space"; "Finiteness is not a calculational convenience but a load-bearing commitment" | "The framework's commitment to a finite substratum" → "The hypothesis A1 of a finite substratum"; "The universe is described" → "Under A1 the universe is described"; "but a load-bearing commitment" → "but load-bearing under A1" | K-ch18-166 (smaller) | K |
| N-K18-172 | ch18:172 (4978) | "The framework's commitment to finite information" | → "The hypothesis of finite information (A1)" | K-ch18-170/172 split | K |
| N-K18-174 | ch18:174 (4980) | "The framework's substratum dynamics is therefore strictly periodic" (nature, Q10 (c)) | → "A bijection of a finite set is therefore strictly periodic"; the $\mathrm{lcm}$ and Landau bounds (:176–:184) unchanged as finite-model mathematics | K-ch18-174–184 (smaller) | K |
| N-K18-186 | ch18:186 (4992), :188 (4994), :190 (4996) | cosmic recurrence as a fact and a prediction (Q10 (c)) | :186 "the universe returns to its exact initial state" → "a finite model returns to its exact initial state"; delete the physical-units sentence and the "astronomical size … age of the universe" sentence; :188 delete the Falsifiability paragraph; :190 delete "The conceptual content is significant.", "The framework predicts that the universe is *cyclic at the substratum level* —" and "The framework's commitment to substratum cyclicity …" | K-ch18-186/188/190 | K |
| N-K18-192 | ch18:192 (4998), :194 (5000) | "(the framework's commitment to $\lvert S\rvert < \infty$)"; "The framework's commitment to finite information is therefore load-bearing" | :192 → "(the hypothesis A1, $\lvert S\rvert < \infty$)" (guard phrase "Recurrence together with C1" kept); :194 "The framework's commitment to finite information" → "The hypothesis of finite information (A1)" | K-ch18-192/194 (smaller) | K |
| N-K18-198 | ch18:198 (5004) | reciprocity without prior (:208 already names it) | as N-S20 at :198 | K-ch18-198/208 | K |
| N-K18-244 | ch18:244 (5050), :246 (5052), :262 (5068) | "the framework's substratum finiteness", "the framework's finiteness" presented as adopted | :244 "the framework's substratum finiteness (developed in §18.7)" → "substratum finiteness under A1 (§18.7)"; :246 "the framework's finiteness" → "A1" (both occurrences); :262 "(as one realization of the framework's finiteness)" → "(as one realization of A1)" | K-ch18-244/246/262 (smaller) | K |
| N-K18-290 | ch18:290 (5096) | "*The substratum is finite.* The framework's finite substratum constrains theories of consciousness" | "*The substratum is finite.*" → "*The substratum is finite under A1.*"; "The framework's finite substratum (§18.7) constrains" → "Under A1 the framework's finite substratum (§18.7) would constrain" | K-ch18-290 (smaller) | K |
| N-K18-328 | ch18:328 (5134) | "Finite information and exact finite recurrence (§18.7) are falsifiable only in the logical sense — …" (prediction, Q10 (c)) | delete the sentence | K-ch18-328 | K |
| N-K18-122 | ch18:122 (4928), :138 (4944) | "information is conserved by the bijectivity premise"; "Information is never lost from the substratum bijection $\varphi$ because $\varphi$ is bijective" | :122 → "…by the bijectivity premise of the framework's models"; :138 → "Information is never lost from a bijective model of the substratum;" | K-ch18-122/138 | K |
| N-K19-22 | ch19:22 (5169), :30 (5177), :72 (5219) | bijectivity "premise" of nature | "is a premise" / "by the bijectivity premise" → "… of the framework's models"; :72 "The substratum map $\varphi$ is bijective by premise (Chapter 1)" → "In the framework's models $\varphi$ is bijective by premise (Chapter 1)" | K-ch19-22/30/72 | K |
| N-K19-126 | ch19:126 (5273) | mirror of Main:592 | as N-M33 | K-ch19-126 | K |
| N-K19-212 | ch19:212 (5359) | "The framework's axioms — deterministic bijectivity, finiteness, …" — finiteness as an axiom | "finiteness," → "finiteness (the open hypothesis A1)," | K-ch19-212 (smaller) | K |
| N-K19-216 | ch19:216 (5363) | "(deterministic bijectivity on a finite set, no further commitments)" as the axioms | → "(deterministic bijectivity, on a finite set under A1, no further commitments)" | K-ch19-214/216 split | K |
| N-K19-80 | ch19:80 (5227) | reciprocity "holds exactly at every time scale" without prior | prefix "Under the counting hidden prior of a finite model, " | K-ch19-80 | K |
| N-K19-360 | ch19:360 (5507) | "the framework's commitment to finiteness" | → "the finiteness hypothesis A1" | K-ch19-360 | K |
| N-Kappa-48 | appendix-a:48 (5572) | "finite cardinality" listed as a Layer 0 prediction | delete "finite cardinality," | K-appa-48 (smaller) | K |
| N-Kappa-181 | appendix-a:181 (5705) | F8 cosmic recurrence as a forward prediction (Q10 (c)) | delete the row (F8 retired, not reused, no renumbering, no note) | K-appa-181 | K |
| N-Kappa-117 | appendix-a:117 (5641) | calibration conditions omit A1 (propagation of N-G03) | after "conditional on H-slope" insert ", A1 (open) for the counting step" | K-appa-111/117 split | K |
| N-Kappb-22 | appendix-b:22 (5776) | the characterization said to rely on the non-permutation-witness lemma, a finite-recurrence result (its proof does not use it) | after "P-indivisibility from a non-permutation witness" insert " (on finite reversible realizations)" | K-appb-12/22 split | K |
| N-Kappc-C6 | appendix-c:114 (6344), :122 (6352), :124 (6354), :128 (6358), :130 (6360), :132 (6362), :134 (6364) | §C.6 defends finiteness as a framework commitment and lists cosmic recurrence as its signature | :114 "the framework's commitment to finiteness — posit A1 (Chapter 2 §2.4) takes the substratum to be a finite set $S$" → "the framework's finiteness hypothesis — A1 (Chapter 2 §2.4), open and not adopted, takes the substratum to be a finite set $S$"; :122 "That extension is posited (A1 of Chapter 2 §2.4)" → "That extension is the open hypothesis A1 of Chapter 2 §2.4"; :124 "The framework's finiteness commitment agrees with … and extends beyond it by posit." → "A1 agrees with … and would extend beyond it; it is not adopted."; :128 "finite at the substratum level" → "finite at the substratum level under A1"; :130 "The framework's commitment to finiteness is therefore" → "A1 is therefore"; :132 delete the paragraph (cosmic recurrence, Q10 (c)); :134 → "A1 is therefore not just a mathematical convenience but a structurally consequential hypothesis: it is motivated by the Bekenstein bound and compatible with continuum QFT, and it is not adopted." Heading and :118–:120 unchanged ("Posit A1" names the entry). | K-appc-112–134 (smaller) | C |
| N-Kappc-154 | appendix-c:154 (6384) | "the framework's content is that $\varphi$ is a bijection on a finite set" | "on a finite set" → "on a finite set (under A1)" | K-appc-154 | K |
| N-Kappc-32 | appendix-c:32 (6262), :34 (6264) | Bell factorization without scope | insert the Bell scope of N-M37 | K-appc-32/34 | K |
| N-Kgl-11 | glossary:11 (6595) | "The posit that the substratum has finitely many degrees of freedom" | "The posit that" → "The open hypothesis, not adopted, that" | K-gl-11 | C |
| N-Kgl-19 | glossary:19 (6603) | Bell factorization without scope | insert the Bell scope of N-M37 before "gives Bell factorization" | K-gl-19 | K |
| N-Kbk-90 | book/README:90 | cosmic recurrence listed among predictions (Q10 (c)) | delete the list item | K-bk-90 | K |

### A.4 Registry

| ID | Entry | Action | From r3 | Status |
|---|---|---|---|---|
| N-D2d | `verification/coverage/LEDGER.json` `MAIN:C-observer-selection-rule-rate-condition` (GAP) | re-affirm the fingerprint moved by N-M51, same commit | D-2d | K |
| N-D2x | any other ledger entry whose fingerprint a kept row moves (Stage 2 `tools/coverage_check.py` run; at drafting none other is expected: the kept Main, GR and Substratum edits are outside census statement bodies) | re-affirm in the same commit | NEW | K |

***

## Part B. Placements

All kept finite-model mathematics stays where it is (OQ-1 (a); policy 3). No row moves text between sections or documents; r3's B-1 to B-20 need no edit and B-1r (relocation) is dropped. The Main-independence check is therefore trivially met: no Main row adds a citation, and the Main rows add no reference to a companion.

***

## Part C. Counts

| ID | Count | Before → after | Reason |
|---|---|---|---|
| C-1 | Posit ledger, Main:728: "Fourteen items, of unequal weight, and not fourteen independent physical assumptions" | **unchanged** (Fourteen). Entry (ii) stays, marked open and not adopted; the sentence counts entries ("items") and already says they are not independent assumptions, and the ledger is "the audited inventory of the explicit premises that the derivations of this paper consume", which still includes (ii) as the hypothesis of the finite-representative results. No numeral moves. | Changed form of (ii) only (N-M44) |
| C-2 | Sites that present item (ii)/A1 as adopted | changed at: Main:36, :60, :704, :722, :728 (ii); GR:342; Computation:118; ch02:16, :76; ch05:23; ch09:184; ch19:212, :216, :360; ch18:166, :172, :192, :194, :244, :246, :262, :290; appendix-c:114–:134; glossary:11 (rows marked C, and the K rows that replace "commitment"). Conditional uses ("under the total-finiteness posit", "the finiteness posit A1 for the hidden sector") unchanged. | Policy 1 |
| C-7 | Forward predictions, appendix-a | F8 row deleted (N-Kappa-181); IDs after: F1–F4, F6, F7, F9–F13; no total F count exists | Q10 (c) |
| — | "six structural properties" (ch09:104, :118), "six properties" / "six structural assumptions" (ch02:74, :120), "the sixth of … A1–A6" (glossary:13), "A1–A6" ranges, Structure §6 tally | **unchanged** | Label and property kept (policy 1) |
| — | Main:80 "three exact layers …", Main:604 "Four claims", Medicine:25 "three results", Substratum "three projections" | unchanged | — |

***

## Part D. Registry, records, guards and derived artifacts

- **Census (`verification/lean-manuscript-census.json`).** No action: no anchor phrase or identifier is changed (N-M33, N-G10a insert words beside the anchors), and the label A1 stays, so the notes of families 12, 13, 48, 49 stay. §A.35 is not triggered (no kernel theorem strengthened).
- **Coverage ledger (`verification/coverage/LEDGER.json`).** Re-affirm `MAIN:C-observer-selection-rule-rate-condition` (N-M51) in the same commit; run `tools/coverage_check.py` and re-affirm any other entry whose fingerprint a kept row moves (none expected). `MAIN:L-3` (K3), `MAIN:T-statement`, `MAIN:L-non-permutation-witness`, `SUBSTRATUM:T-23`, `SUBSTRATUM:L-23.0`, `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer`, `SM:P-4b-…` and `STRUCTURE:P-9.5` are untouched because their statements are kept.
- **Records (Q14 (c) qualified).** No record action: no manuscript line cites a record that premises A1 for a surviving claim (r3 D-3a to D-3e, confirmed by the review), and with A1 kept as an open hypothesis the records that name it describe a live hypothesis.
- **Guards.** No pinned phrase is changed (the kept rows avoid glossary:13, Main:80, Main:135–145, Main:338, Main:642 and keep "non-permutation one-step witness" at Main:630 and "Recurrence together with C1" at ch18:192); the V1 guard run in Stage 2 confirms.
- **Derived artifacts.** Rebuild `Main`, `GR`, `SM`, `Substratum`, `Methodology`, `Complexity`, `Computation` (`sh ./build.sh Main GR SM Substratum Methodology Complexity Computation`) and the book (`sh ./build.sh --book`). Introduction, Structure, Medicine, Bioinformatics and Juno are not touched.

***

## Part E. r3 rows split: one part kept, the rest dropped

| r3 row | Kept part (r4 row) | Dropped part |
|---|---|---|
| K-ch02-16 | N-K02-16 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-ch02-76 | N-K02-76 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-ch04-36/178/182 | N-K04-36 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-ch07-12/110/118/157/159/161 | N-K07-12 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-ch09-184/190/194 | N-K09-184 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-ch14-90/268 | N-K14-90 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-ch18-170/172 | N-K18-172 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-ch19-212 | N-K19-212 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-ch19-214/216 | N-K19-216 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-appa-111/117 | N-Kappa-117 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-appb-12/22 | N-Kappb-22 | the other sentences of the row: MOD/RES (model or conditional statements) |
| K-appc-112–134 | N-Kappc-C6 | the other sentences of the row: MOD/RES (model or conditional statements) |
***

## Part F. DROP ledger (r3 row → reason)

| r3 row | Reason |
|---|---|
| M-01 | RES: generic statement about an observer in a finite deterministic system; restrictive, not a claim that nature is finite |
| M-02a | ACC: no change in r3 |
| M-02b | 2B: headline deletion; OQ-1 = (a) |
| M-03a | ACC: no change in r3 |
| M-03b | 2B: headline deletion; OQ-1 = (a) |
| M-08 | THM: Lemma 3 speaks of the reversible representative of §1.2 (finite by definition) and Main:58 makes the measure a realization datum; statement and K3 entry kept |
| M-12a | ACC: no change in r3 |
| M-12b | 2B: headline deletion; OQ-1 = (a) |
| M-13a | ACC: no change in r3 |
| M-13b | 2B: headline deletion; OQ-1 = (a) |
| M-14 | SCP: scoped to "the substratum's stated interventions (its finite bijective read-write dynamics …)" |
| M-15 | RES: "under the total-finiteness posit" is conditional; the ledger entry is now marked open, not adopted (M-44) |
| M-16 | RES: "under the total-finiteness posit" is conditional; the ledger entry is now marked open, not adopted (M-44) |
| M-17 | RES: names the recurrence argument and its finiteness hypothesis |
| M-18 | RES: names the recurrence argument and its finiteness hypothesis |
| M-20 | RES: "under the total-finiteness posit" is conditional; the ledger entry is now marked open, not adopted (M-44) |
| M-21 | RES: "under the total-finiteness posit" is conditional; the ledger entry is now marked open, not adopted (M-44) |
| M-22 | RES: inside the §3.2 setup, which is conditional on the posit (Main:266) and concerns "the realization displayed above" (Main:324) |
| M-23 | RES: inside the §3.2 setup, which is conditional on the posit (Main:266) and concerns "the realization displayed above" (Main:324) |
| M-24 | ACC: no change in r3 |
| M-25 | ACC: states the role of P-indivisibility, not that it holds of nature |
| M-27 | ACC: no change in r3 |
| M-28 | THM: the theorem's setting is Main:362's finite site set ("with $V$ and each $S_i$ finite") |
| M-29 | ACC: no change in r3 |
| M-30 | THM: lemma in the finite-realization setting of §2.3/§3.2; statement and ledger entry kept |
| M-32 | ACC: no change in r3 |
| M-34 | ACC: no change in r3 |
| M-36 | ACC: open question about one fixed finite substratum; Q15 (b) wording unchanged |
| M-47 | LBL: the count of ledger entries is unchanged because entry (ii) stays (CHANGED, see C-1) |
| M-48 | LBL: the count of ledger entries is unchanged because entry (ii) stays (CHANGED, see C-1) |
| M-49 | ACC: status-table row about the representative's recurrence time |
| M-52 | ACC: no change in r3 |
| M-53 | ACC: no change in r3 |
| M-55 | SCP: scoped to "the substratum's stated interventions (its finite bijective read-write dynamics …)" |
| M-58 | THM: follows the theorem in its finite-site-set setting |
| M-59 | THM: proof of a lemma stated "under the canonical invariant measure"; conditional on the declared measure |
| M-56 | ACC: no change in r3 |
| I-01a | ACC: no change in r3 (Intro:34 scopes to finite models) |
| I-01b | 2B: OQ-1 = (a) |
| I-02 | ACC: no change in r3 (Intro:34 scopes to finite models) |
| I-03 | ACC: no change in r3 (Intro:34 scopes to finite models) |
| I-04 | ACC: no change in r3 (Intro:34 scopes to finite models) |
| I-05 | ACC: no change in r3 (Intro:34 scopes to finite models) |
| I-06 | ACC: no change in r3 (Intro:34 scopes to finite models) |
| I-07 | ACC: no change in r3 (Intro:34 scopes to finite models) |
| I-08 | ACC: no change in r3 (Intro:34 scopes to finite models) |
| I-09 | ACC: no change in r3 (Intro:34 scopes to finite models) |
| G-01 | RES: Main's result stated for a finite configuration space; restrictive |
| G-02 | RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-04 | RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-05 | ACC: no change in r3 |
| G-06 | RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-07 | ACC: no change in r3 |
| G-08 | ACC: no change in r3 |
| G-09 | SCP: scoped to "its stated interventions" |
| G-10b | 2B |
| G-11 | LBL: A1–A6 label kept |
| G-13 | RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-14 | ACC: no change in r3 |
| G-15 | RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-16 | ACC: no change in r3 |
| G-17 | LBL: A1–A6 label kept |
| G-18 | RES: "proposes" — a proposal, not an established claim |
| G-19 | ACC: no change in r3 |
| S-01 | MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-02 | MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-03 | RES: Main's result stated for a finite configuration space; restrictive |
| S-04 | ACC: no change in r3 |
| S-05 | ACC: no change in r3 |
| S-06 | ACC: no change in r3 |
| S-07 | ACC: no change in r3 |
| S-08 | ACC: no change in r3 |
| S-09 | MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-10 | MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-11 | ACC: no change in r3 |
| S-12 | MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-13 | ACC: no change in r3 |
| S-14 | MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-15 | MOD: Proposition 4b states the counting measure of SM's finite model; theorem statement kept |
| S-16 | ACC: no change in r3 |
| S-17 | ACC: no change in r3 |
| S-18 | MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| U-01 | MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-02 | MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-03 | MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-04 | MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-05 | ACC: no change in r3 |
| U-07 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-08 | RES: the structural prong is stated for "every map on a finite set" |
| U-09a | ACC: no change in r3 |
| U-09b | 2B / OQ-6 (a): A4 unchanged |
| U-10 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-11 | ACC: no change in r3 |
| U-12 | ACC: no change in r3 |
| U-13 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-14 | ACC: no change in r3 |
| U-15 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-16 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-17 | ACC: no change in r3 |
| U-18 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-19 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-20 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-21 | LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-23 | LBL: with A1 kept, "the interpretive premise of A1" states A1's motivation; Sub:92 already says the bound does not establish finiteness |
| U-24 | MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-25 | ACC: no change in r3 |
| U-28 | SCP: scoped to "the substratum's stated interventions" |
| U-29 | MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-30 | MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-31 | ACC: true of any bijection on a finite set |
| U-32 | ACC: no change in r3 |
| T-01 | MOD: OI's class or representative, finite through A4 and A1 |
| T-02 | RES: generic statement about an observer in a finite deterministic system |
| T-03 | LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-04 | LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-04b | LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-05 | MOD: OI's class or representative, finite through A4 and A1 |
| T-06 | LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-07 | LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-08 | LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-09 | ACC: no change in r3 |
| T-10 | MOD: OI's class or representative, finite through A4 and A1 |
| T-11 | LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-12 | ACC: no change in r3 |
| T-13 | MOD: OI's recurrence-scale theorem for its finite representative |
| T-14 | ACC: no change in r3 |
| T-15 | MOD: OI's class or representative, finite through A4 and A1 |
| T-16 | ACC: no change in r3 |
| T-17 | ACC: no change in r3 |
| Y-01 | LBL/RES: names A1 as what reversibility and rung 6 rest on; accurate with A1 kept as an open hypothesis |
| Y-02 | LBL/RES: names A1 as what reversibility and rung 6 rest on; accurate with A1 kept as an open hypothesis |
| Y-03 | LBL/RES: names A1 as what reversibility and rung 6 rest on; accurate with A1 kept as an open hypothesis |
| Y-04 | LBL/RES: names A1 as what reversibility and rung 6 rest on; accurate with A1 kept as an open hypothesis |
| Y-06 | MOD: the forward construction and its finite bijection |
| Y-07 | LBL |
| Y-09 | MOD: the forward construction and its finite bijection |
| Y-10 | ACC: no change in r3 |
| X-01 | MOD: the framework's finite model |
| X-02 | RES: restrictive restatement of Main's result |
| X-04 | MOD: the framework's finite model |
| X-07 | ACC: no change in r3 |
| P-01 | MOD: the framework's finite model |
| P-02 | LBL: "violating A1" accurate with A1 kept |
| P-05 | open: kept in F.2 (reading of $e^{S}$) |
| D-01 | RES: names finiteness as the hypothesis |
| D-02 | RES: already "on one fixed finite reversible representative" |
| D-03 | ACC |
| K-pref-3a | ACC: no change in r3, or accurate as worded |
| K-pref-3b | 2B: OQ-1 = (a) |
| K-rg-79 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch00-53a | ACC: no change in r3, or accurate as worded |
| K-ch00-53b | 2B: OQ-1 = (a) |
| K-ch00-59 | RES: generic "any observer embedded in a finite deterministic universe"; restrictive (ch05:23's "posit A1" is CHANGED as K-ch05-23) |
| K-ch00-69 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch00-95 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch00-39/51 | ACC: no change in r3, or accurate as worded |
| K-ch01-38 | THM: mirror of Lemma 3, kept as stated (as M-08) |
| K-ch01-93b | 2B: OQ-1 = (a) |
| K-ch01-111 | RES: proof step that names its finiteness hypothesis (A1) |
| K-ch01-119 | RES: proof step that names its finiteness hypothesis (A1) |
| K-ch01-121 | ACC: no change in r3, or accurate as worded |
| K-ch01-133 | RES: scoped to the recurrence proof, to "any finite reversible substratum", or to "where the dynamics is P-indivisible" |
| K-ch01-201 | RES: scoped to the recurrence proof, to "any finite reversible substratum", or to "where the dynamics is P-indivisible" |
| K-ch01-125/223 | ACC: no change in r3, or accurate as worded |
| K-ch01-235 | RES: generic "any observer embedded in a finite deterministic universe"; restrictive (ch05:23's "posit A1" is CHANGED as K-ch05-23) |
| K-ch02-8 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch02-32 | RES: "the exact OI model here has finite $S$" |
| K-ch02-74 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch02-78 | RES: mirror of Sub:94, whose structural prong is stated for a finite set |
| K-ch02-88/118/122 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch02-90 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch02-120 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch02-136/148/158/212 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch02-186 | ACC: no change in r3, or accurate as worded |
| K-ch03-34/44 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch03-36/102/114/240 | RES: scoped to the recurrence proof, to "any finite reversible substratum", or to "where the dynamics is P-indivisible" |
| K-ch03-84/88/196/230 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch04-10/22/26 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch04-94 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch04-210 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch05-11/15/23 | RES: generic "any observer embedded in a finite deterministic universe"; restrictive (ch05:23's "posit A1" is CHANGED as K-ch05-23) |
| K-ch05-19 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch05-25/77/83/89 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch05-41/95 | ACC: no change in r3, or accurate as worded |
| K-ch07-14 | MOD: finite deterministic systems / the class's bijection commitment |
| K-ch07-126/149 | ACC: no change in r3, or accurate as worded |
| K-ch09-14/42/61/84/118 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch09-18/36 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch09-104/106 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch09-108 | MOD: finite deterministic systems / the class's bijection commitment |
| K-ch09-298/300/314 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch11-164 | ACC: no change in r3, or accurate as worded |
| K-ch12-211/213 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch14-6/12/34/146 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch14-92 | ACC: no change in r3, or accurate as worded |
| K-ch14-100/105 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch14-160/164 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch15-114 | ACC: no change in r3, or accurate as worded |
| K-ch18-74 | ACC: no change in r3, or accurate as worded |
| K-ch18-164 | CLN: section heading names the topic |
| K-ch18-168 | RES: "under the finiteness posit A1 it is finite" is conditional |
| K-ch19-198 | ACC: no change in r3, or accurate as worded |
| K-ch19-261 | ACC: no change in r3, or accurate as worded |
| K-appb-32 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-appb-40 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-appb-92 | THM: theorem B.2.5 names "finiteness" among its premises |
| K-appb-194 | ACC: no change in r3, or accurate as worded |
| K-appb-413–421 | ACC: no change in r3, or accurate as worded |
| K-appb-451/454 | RES: scoped to the recurrence proof, to "any finite reversible substratum", or to "where the dynamics is P-indivisible" |
| K-appc-16 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-appc-224 | MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-appc-120 | ACC: no change in r3, or accurate as worded |
| K-gl-13 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-gl-105/107/117 | ACC: no change in r3, or accurate as worded |
| K-bk-82 | ACC: no change in r3, or accurate as worded |
| K-bk-100 | LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| R-01 | ACC |
| R-02 | ACC |
| R-03 | LBL: MAIN:L-3 unchanged (M-08 dropped); its assumption "finiteness of S (total-finiteness posit)" is accurate |
| B-1 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-1r | 2B: OQ-1 = (a) |
| B-2 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-3 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-4 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-5 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-6 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-7 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-8 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-9 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-10 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-11 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-12 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-13 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-14 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-15 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-16 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-17 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-18 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-19 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| B-20 | ACC: in place, no edit (OQ-1 = (a)); see Part B |
| C-3 | LBL: no recount (label, property and entries kept) |
| C-4 | LBL: no recount (label, property and entries kept) |
| C-5 | LBL: no recount (label, property and entries kept) |
| C-6 | LBL: no recount (label, property and entries kept) |
| C-8 | LBL: no recount (label, property and entries kept) |
| C-9 | LBL: no recount (label, property and entries kept) |
| C-10 | ACC |
| C-11 | ACC |
| D-1a | LBL/ACC: no census note or anchor changes (A1 label kept; anchors kept verbatim) |
| D-1a′ | LBL/ACC: no census note or anchor changes (A1 label kept; anchors kept verbatim) |
| D-1b | LBL/ACC: no census note or anchor changes (A1 label kept; anchors kept verbatim) |
| D-1c | LBL/ACC: no census note or anchor changes (A1 label kept; anchors kept verbatim) |
| D-1d | LBL/ACC: no census note or anchor changes (A1 label kept; anchors kept verbatim) |
| D-1e | LBL/ACC: no census note or anchor changes (A1 label kept; anchors kept verbatim) |
| D-2a | THM: the statement it tracked is no longer edited |
| D-2b | THM: the statement it tracked is no longer edited |
| D-2c | THM: the statement it tracked is no longer edited |
| D-2e | THM: the statement it tracked is no longer edited |
| D-2f | THM: the statement it tracked is no longer edited |
| D-3a | ACC: no record action needed |
| D-3b | ACC: no record action needed |
| D-3c | ACC: no record action needed |
| D-3d | ACC: no record action needed |
| D-3e | ACC: no record action needed |
***

## Part G. Remaining owner questions, separate units, and Stage 2 checks

**Owner questions (genuine only).**

- **OQ-A. Do the policy's open-hypothesis A1 and the earlier removals Q9 (c) and Q10 (c) interact?** With A1 kept as an open hypothesis, the corner-occupancy prediction (Main:216), the fixed-carrier bearing on nature (Main:60) and cosmic recurrence (§18.7, F8, book README:90, appendix-c:132) could be re-stated as explicit conditionals on A1 (the Q9 (a) and Q10 (b) forms) instead of being deleted. Options: (a) keep Q9 (c) and Q10 (c) as decided: delete the predictions, keep the period bound as finite-model mathematics (this map); (b) re-state them as conditionals on A1. **Recommendation: (a)**: the policy revises Q4 (a) and Q3 (a) only, and the reason for Q9 (c) and Q10 (c) (no accessible test, so the conditional fits any outcome) is unchanged.
- **P-05 (reading, not a decision).** Whether $e^{S}$ at Computation:142 is the accessible-sector budget (then accurate) or the whole lattice (then "under A1" is inserted). Stage 2 reading, then reviewer.

OQ-1 (a), OQ-2 (a) by necessity, OQ-3 (no guard edit) by necessity, OQ-5 (b) and OQ-6 (a) are settled by the policy; OQ-4 was withdrawn in r2.

**Separate units** (unchanged from r3 F.1, Q12 (b)): U-P1, U-P4, U-P5a/b, U-P6, U-P7, U-P9, U-P10, U-P11, U-P13, U-P12, U-P15, U-P16. Dropped: U-RL and U-264 (2b, not pursued under OQ-1 (a) and policy 5).

**Stage 2 checks.** Re-grep, before and after, for: `posit A1`, `finiteness posit`, `total-finiteness posit`, `commitment to finit`, `finiteness commitment`, `framework.s finiteness`, `postulates a finite`, `finite substrat`, `finite deterministic (system|substratum|construction|universe)`, `universe (is|returns)`, `cosmic recurrence`, `\bF8\b`, `unconditionally at`, `reciprocal (visible )?transition counts`, `bijectivity premise`, `by premise`, `CHSH`, `causal cone`, `past hypothesis`, `Boltzmann`; each hit read in context against Parts A and F. Mirrors byte-identical (SC-42 parity). Tools: `tools/coverage_check.py`, `tools/lean_manuscript_census.py`, `verification/lean/edge_rigidity_probe.py`, `tools/legacy_records_check.py`, `tools/v3_verifier.py --receipts HEAD`, `claims_check`, `staleness_check`, `voice_check` (added lines), `build.sh` with page-count checks.

***

## Part H. Check table: every corrective row of r3

Each r3 row that corrected something (class other than NC, stage 2a) is listed with its disposition here: corrected (r4 row named), or not an unsupported assertion under the policy (reason).

| r3 row | r3 site | r4 disposition |
|---|---|---|
| M-01 | Main:14 | not an unsupported assertion under the policy — RES: generic statement about an observer in a finite deterministic system; restrictive, not a claim that nature is finite |
| M-04 | Main:20 | corrected: N-M04 |
| M-05 | Main:20 | corrected: N-M05 |
| M-06 | Main:36 | corrected: N-M06 |
| M-07 | Main:44 | corrected: N-M07 |
| M-08 | Main:54 | not an unsupported assertion under the policy — THM: Lemma 3 speaks of the reversible representative of §1.2 (finite by definition) and Main:58 makes the measure a realization datum; statement and K3 entry kept |
| M-09 | Main:58 | corrected: N-M09 |
| M-10 | Main:60 | corrected: N-M10a, N-M10b, N-M10c, N-M10d |
| M-11 | Main:64 | corrected: N-M11 |
| M-14 | Main:80 item (4) | not an unsupported assertion under the policy — SCP: scoped to "the substratum's stated interventions (its finite bijective read-write dynamics …)" |
| M-15 | Main:111 | not an unsupported assertion under the policy — RES: "under the total-finiteness posit" is conditional; the ledger entry is now marked open, not adopted (M-44) |
| M-16 | Main:129 | not an unsupported assertion under the policy — RES: "under the total-finiteness posit" is conditional; the ledger entry is now marked open, not adopted (M-44) |
| M-17 | Main:157 | not an unsupported assertion under the policy — RES: names the recurrence argument and its finiteness hypothesis |
| M-18 | Main:178 | not an unsupported assertion under the policy — RES: names the recurrence argument and its finiteness hypothesis |
| M-19 | Main:216 | corrected: N-M19 |
| M-20 | Main:222 | not an unsupported assertion under the policy — RES: "under the total-finiteness posit" is conditional; the ledger entry is now marked open, not adopted (M-44) |
| M-21 | Main:266 | not an unsupported assertion under the policy — RES: "under the total-finiteness posit" is conditional; the ledger entry is now marked open, not adopted (M-44) |
| M-22 | Main:280 | not an unsupported assertion under the policy — RES: inside the §3.2 setup, which is conditional on the posit (Main:266) and concerns "the realization displayed above" (Main:324) |
| M-23 | Main:292 | not an unsupported assertion under the policy — RES: inside the §3.2 setup, which is conditional on the posit (Main:266) and concerns "the realization displayed above" (Main:324) |
| M-25 | Main:354 | not an unsupported assertion under the policy — ACC: states the role of P-indivisibility, not that it holds of nature |
| M-26 | Main:356 | corrected: N-M26 |
| M-28 | Main:366 (theorem header at :364) | not an unsupported assertion under the policy — THM: the theorem's setting is Main:362's finite site set ("with $V$ and each $S_i$ finite") |
| M-30 | Main:439–441 | not an unsupported assertion under the policy — THM: lemma in the finite-realization setting of §2.3/§3.2; statement and ledger entry kept |
| M-31 | Main:449 | corrected: N-M31 |
| M-33 | Main:592 | corrected: N-M33 |
| M-35 | Main:630 | corrected: N-M35 |
| M-36 | Main:642 | not an unsupported assertion under the policy — ACC: open question about one fixed finite substratum; Q15 (b) wording unchanged |
| M-37 | Main:654 | corrected: N-M37 |
| M-38 | Main:704 | corrected: N-M38 |
| M-39 | Main:710 | corrected: N-M39 |
| M-40 | Main:714 | corrected: N-M40 |
| M-41 | Main:720 | corrected: N-M41 |
| M-42 | Main:722 | corrected: N-M42 |
| M-43 | Main:724 | corrected: N-M43 |
| M-44 | Main:728 (ledger) | corrected: N-M44 |
| M-45 | Main:728 (ledger) | corrected: N-M45 |
| M-46 | Main:728 (ledger) | corrected: N-M46 |
| M-47 | Main:728 (ledger) | not an unsupported assertion under the policy — LBL: the count of ledger entries is unchanged because entry (ii) stays (CHANGED, see C-1) |
| M-48 | Main:728 (ledger) | not an unsupported assertion under the policy — LBL: the count of ledger entries is unchanged because entry (ii) stays (CHANGED, see C-1) |
| M-49 | Main:735, :737 (status table) | not an unsupported assertion under the policy — ACC: status-table row about the representative's recurrence time |
| M-50 | Main:746 | corrected: N-M50 |
| M-51 | Main:760 (end) | corrected: N-M51 |
| M-54 | Main:774 | corrected: N-M54 |
| M-55 | Main:778 | not an unsupported assertion under the policy — SCP: scoped to "the substratum's stated interventions (its finite bijective read-write dynamics …)" |
| M-57 | Main:216 | corrected: N-M57 |
| M-58 | Main:393, :402 | not an unsupported assertion under the policy — THM: follows the theorem in its finite-site-set setting |
| M-59 | Main:86, :103 | not an unsupported assertion under the policy — THM: proof of a lemma stated "under the canonical invariant measure"; conditional on the declared measure |
| M-60 | Main:728 (after the ledger) | corrected: N-M60 |
| G-01 | GR:20 | corrected: N-G01b |
| G-01b | GR:20 clause (ii) | corrected: N-G01b |
| G-02 | GR:22 | not an unsupported assertion under the policy — RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-03 | GR:28 | corrected: N-G03 |
| G-04 | GR:58 | not an unsupported assertion under the policy — RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-06 | GR:90 | not an unsupported assertion under the policy — RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-09 | GR:224 | not an unsupported assertion under the policy — SCP: scoped to "its stated interventions" |
| G-10a | GR:256–274 | corrected: N-G10a |
| G-11 | GR:260 | not an unsupported assertion under the policy — LBL: A1–A6 label kept |
| G-12 | GR:342 | corrected: N-G12 |
| G-13 | GR:585 | not an unsupported assertion under the policy — RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-15 | GR:605 | not an unsupported assertion under the policy — RES: names the finite representative or the finite model of its setting (Tier 1 "finite deterministic system"; Appendix A setup) |
| G-17 | GR:669 | not an unsupported assertion under the policy — LBL: A1–A6 label kept |
| G-18 | GR:705 | not an unsupported assertion under the policy — RES: "proposes" — a proposal, not an established claim |
| S-01 | SM:14 | not an unsupported assertion under the policy — MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-02 | SM:20 | not an unsupported assertion under the policy — MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-03 | SM:22 | not an unsupported assertion under the policy — RES: Main's result stated for a finite configuration space; restrictive |
| S-09 | SM:222 | not an unsupported assertion under the policy — MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-10 | SM:232 | not an unsupported assertion under the policy — MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-12 | SM:250 | not an unsupported assertion under the policy — MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-14 | SM:316 | not an unsupported assertion under the policy — MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-15 | SM:334 | not an unsupported assertion under the policy — MOD: Proposition 4b states the counting measure of SM's finite model; theorem statement kept |
| S-18 | SM:1588 | not an unsupported assertion under the policy — MOD: OI's specific representative, finite through A4 (OQ-6 (a)); no claim that nature's total system is finite |
| S-19 | SM:1592 | corrected: N-S19 |
| S-20 | SM:36, :1520, :1546, :1588 | corrected: N-S20 |
| U-01 | Sub:14 | not an unsupported assertion under the policy — MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-02 | Sub:16 | not an unsupported assertion under the policy — MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-03 | Sub:22 | not an unsupported assertion under the policy — MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-04 | Sub:44 | not an unsupported assertion under the policy — MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-06 | Sub:56 | corrected: N-U06 |
| U-07 | Sub:92 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-08 | Sub:94 | not an unsupported assertion under the policy — RES: the structural prong is stated for "every map on a finite set" |
| U-09b | Sub:98, :157 | not an unsupported assertion under the policy — 2B / OQ-6 (a): A4 unchanged |
| U-10 | Sub:104 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-13 | Sub:123 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-15 | Sub:129 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-16 | Sub:133 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-18 | Sub:189 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-19 | Sub:193 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-20 | Sub:199 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-21 | Sub:205, :207, :212, :223, :233 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; theorem hypotheses that name A1 are accurate |
| U-22 | Sub:216 | corrected: N-U22 |
| U-23 | Sub:268 | not an unsupported assertion under the policy — LBL: with A1 kept, "the interpretive premise of A1" states A1's motivation; Sub:92 already says the bound does not establish finiteness |
| U-24 | Sub:288 | not an unsupported assertion under the policy — MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-26 | Sub:367 | corrected: N-U26 |
| U-27 | Sub:371, :377, :401, :407, :413 | corrected: N-U27 |
| U-28 | Sub:373 | not an unsupported assertion under the policy — SCP: scoped to "the substratum's stated interventions" |
| U-29 | Sub:389 | not an unsupported assertion under the policy — MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-30 | Sub:429 | not an unsupported assertion under the policy — MOD: the reconstruction's object, finite through A4 and A1 as hypotheses of Theorem 23 |
| U-31 | Sub:465 | not an unsupported assertion under the policy — ACC: true of any bijection on a finite set |
| U-33 | Sub:14 | corrected: N-U33 |
| U-34 | Sub:48, :171, :467 | corrected: N-U34 |
| U-35 | Sub:131 | corrected: N-U35 |
| U-38 | Sub:415 | corrected: N-U38 |
| T-01 | Struct:21 | not an unsupported assertion under the policy — MOD: OI's class or representative, finite through A4 and A1 |
| T-02 | Struct:45 | not an unsupported assertion under the policy — RES: generic statement about an observer in a finite deterministic system |
| T-03 | Struct:47 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-04 | Struct:80, :86, :196, :206, :331, :339 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-04b | Struct:1032, :1034, :1036, :1038 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-05 | Struct:108 | not an unsupported assertion under the policy — MOD: OI's class or representative, finite through A4 and A1 |
| T-06 | Struct:134–140 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-07 | Struct:224, :230, :256–:327 (§6, incl. | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-08 | Struct:646 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-10 | Struct:741 | not an unsupported assertion under the policy — MOD: OI's class or representative, finite through A4 and A1 |
| T-11 | Struct:767 | not an unsupported assertion under the policy — LBL: A1 and A1–A6 kept; class membership and Theorem 23 hypotheses accurate |
| T-13 | Struct:1174, :1211, :1248 | not an unsupported assertion under the policy — MOD: OI's recurrence-scale theorem for its finite representative |
| T-15 | Struct:377, :528 | not an unsupported assertion under the policy — MOD: OI's class or representative, finite through A4 and A1 |
| Y-01 | Meth:148 | not an unsupported assertion under the policy — LBL/RES: names A1 as what reversibility and rung 6 rest on; accurate with A1 kept as an open hypothesis |
| Y-02 | Meth:156 | not an unsupported assertion under the policy — LBL/RES: names A1 as what reversibility and rung 6 rest on; accurate with A1 kept as an open hypothesis |
| Y-03 | Meth:158 | not an unsupported assertion under the policy — LBL/RES: names A1 as what reversibility and rung 6 rest on; accurate with A1 kept as an open hypothesis |
| Y-04 | Meth:166, :253, :261 | not an unsupported assertion under the policy — LBL/RES: names A1 as what reversibility and rung 6 rest on; accurate with A1 kept as an open hypothesis |
| Y-05 | Meth:162, :283 | corrected: N-Y05 |
| Y-06 | Meth:337 | not an unsupported assertion under the policy — MOD: the forward construction and its finite bijection |
| Y-07 | Meth:339, :345, :367, :369 | not an unsupported assertion under the policy — LBL |
| Y-08 | Meth:357 | corrected: N-Y08 |
| Y-09 | Meth:409, :517, :529 | not an unsupported assertion under the policy — MOD: the forward construction and its finite bijection |
| Y-11 | Meth:339, :381, :385, :389, :391 | corrected: N-Y11 |
| X-01 | Complexity:21 | not an unsupported assertion under the policy — MOD: the framework's finite model |
| X-02 | Complexity:27 | not an unsupported assertion under the policy — RES: restrictive restatement of Main's result |
| X-03 | Complexity:212 | corrected: N-X03 |
| X-04 | Complexity:314 | not an unsupported assertion under the policy — MOD: the framework's finite model |
| X-05 | Complexity:374 | corrected: N-X05 |
| X-06 | Complexity:434 | corrected: N-X06 |
| P-01 | Computation:21 | not an unsupported assertion under the policy — MOD: the framework's finite model |
| P-02 | Computation:100 | not an unsupported assertion under the policy — LBL: "violating A1" accurate with A1 kept |
| P-03 | Computation:118 | corrected: N-P03 |
| P-04 | Computation:120 | corrected: N-P04 |
| P-06 | Computation:180 | corrected: N-P06 |
| K-rg-79 | readers-guide:79 (169) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch00-59 | ch00:59 (286) | not an unsupported assertion under the policy — RES: generic "any observer embedded in a finite deterministic universe"; restrictive (ch05:23's "posit A1" is CHANGED as K-ch05-23) |
| K-ch00-69 | ch00:69 (296) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch00-95 | ch00:95 (322) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch01-28 | ch01:28 (363) | corrected: N-K01-28 |
| K-ch01-38 | ch01:38 (373) | not an unsupported assertion under the policy — THM: mirror of Lemma 3, kept as stated (as M-08) |
| K-ch01-41 | ch01:41 (376) | corrected: N-K01-41 |
| K-ch01-85 | ch01:85 (420) | corrected: N-K01-85 |
| K-ch01-93a | ch01:93 (428) | corrected: N-K01-93 |
| K-ch01-111 | ch01:111 (446) | not an unsupported assertion under the policy — RES: proof step that names its finiteness hypothesis (A1) |
| K-ch01-119 | ch01:119 (454) | not an unsupported assertion under the policy — RES: proof step that names its finiteness hypothesis (A1) |
| K-ch01-133 | ch01:133 (468) | not an unsupported assertion under the policy — RES: scoped to the recurrence proof, to "any finite reversible substratum", or to "where the dynamics is P-indivisible" |
| K-ch01-165 | ch01:165 (500) | corrected: N-K01-165 |
| K-ch01-181 | ch01:181 (516) | corrected: N-K01-181 |
| K-ch01-201 | ch01:201 (536) | not an unsupported assertion under the policy — RES: scoped to the recurrence proof, to "any finite reversible substratum", or to "where the dynamics is P-indivisible" |
| K-ch01-235 | ch01:235 (570) | not an unsupported assertion under the policy — RES: generic "any observer embedded in a finite deterministic universe"; restrictive (ch05:23's "posit A1" is CHANGED as K-ch05-23) |
| K-ch01-16/183 | ch01:16 (351), :183 (518) | corrected: N-K01-165, N-K01-16 |
| K-ch02-8 | ch02:8 (642) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch02-16 | ch02:16 (650) | corrected: N-K02-16 |
| K-ch02-32 | ch02:32 (666) | not an unsupported assertion under the policy — RES: "the exact OI model here has finite $S$" |
| K-ch02-74 | ch02:74 (708) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch02-76 | ch02:76 (710) | corrected: N-K02-76 |
| K-ch02-78 | ch02:78 (712) | not an unsupported assertion under the policy — RES: mirror of Sub:94, whose structural prong is stated for a finite set |
| K-ch02-88/118/122 | ch02:88 (722), :118 (752), :122 (756) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch02-90 | ch02:90 (724) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch02-120 | ch02:120 (754) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch02-136/148/158/212 | ch02:136 (770), :148 (782), :158 (792) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch02-184 | ch02:184 (818) | corrected: N-K02-184 |
| K-ch02-192–200 | ch02:192–200 (826–834) | corrected: N-K02-192 |
| K-ch03-22 | ch03:22 (887) | corrected: N-K03-22 |
| K-ch03-34/44 | ch03:34 (899), :44 (909) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch03-58/62 | ch03:58 (923), :62 (927) | corrected: N-K03-58 |
| K-ch03-36/102/114/240 | ch03:36 (901), :102 (967), :114 (979), | not an unsupported assertion under the policy — RES: scoped to the recurrence proof, to "any finite reversible substratum", or to "where the dynamics is P-indivisible" |
| K-ch03-84/88/196/230 | ch03:84 (949), :88 (953), :196 (1061), | corrected: N-K03-196 |
| K-ch03-40/162/180/186 | ch03:40 (905), :162 (1027), :180 (1045 | corrected: N-K03-40 |
| K-ch04-10/22/26 | ch04:10 (1118), :22 (1130), :26 (1134) | corrected: N-K04-26 |
| K-ch04-36/178/182 | ch04:36 (1144), :178 (1286), :182 (129 | corrected: N-K04-36 |
| K-ch04-94 | ch04:94 (1202) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch04-210 | ch04:210 (1318) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch04-116/166 | ch04:116 (1224), :166 (1274) | corrected: N-K04-116 |
| K-ch05-11/15/23 | ch05:11 (1329), :15 (1333), :23 (1341) | corrected: N-K05-23 |
| K-ch05-19 | ch05:19 (1337) | corrected: N-K05-194 |
| K-ch05-25/77/83/89 | ch05:25 (1343), :77, :83, :89 | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch05-41/95 | ch05:41 (1359), :95 (1413) | not an unsupported assertion under the policy — ACC: no change in r3, or accurate as worded |
| K-ch05-194 | ch05:194 (1512) | corrected: N-K05-194 |
| K-ch06-10 | ch06:10 (1523) | corrected: N-K06-10 |
| K-ch07-12/110/118/157/159/161 | ch07:12 (1878), :110 (1976), :118 (198 | corrected: N-K07-12 |
| K-ch09-129 | ch09:129 (2596) | corrected: N-K09-129 |
| K-ch18-122/138 | ch18:122 (4928), :138 (4944) | corrected: N-K18-122 |
| K-ch19-22/30/72 | ch19:22 (5169), :30 (5177), :72 (5219) | corrected: N-K19-22 |
| K-ch09-14/42/61/84/118 | ch09:14 (2481), :42 (2509), :61 (2528) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch09-18/36 | ch09:18 (2485), :36 (2503) | corrected: N-K09-36, N-K09-184 |
| K-ch09-104/106 | ch09:104 (2571), :106 (2573) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-ch09-108 | ch09:108 (2575) | not an unsupported assertion under the policy — MOD: finite deterministic systems / the class's bijection commitment |
| K-ch09-184/190/194 | ch09:184 (2651), :190 (2657), :194 (26 | corrected: N-K09-184 |
| K-ch09-298/300/314 | ch09:298 (2765), :300 (2767), :314 (27 | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch12-211/213 | ch12:211 (3451), :213 (3453) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch14-6/12/34/146 | ch14:6 (3672), :12 (3678), :34 (3700), | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch14-90/268 | ch14:90 (3756), :268 (3934) | corrected: N-K14-90 |
| K-ch14-100/105 | ch14:100 (3766), :105 (3771) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-ch14-160/164 | ch14:160 (3826), :164 (3830) | corrected: N-K14-164 |
| K-ch18-20/28/162 | ch18:20 (4826), :28 (4834), :162 (4968 | corrected: N-K18-20 |
| K-ch18-40 | ch18:40 (4846) | corrected: N-K18-40 |
| K-ch18-164 | ch18:164 (4970) | not an unsupported assertion under the policy — CLN: section heading names the topic |
| K-ch18-166 | ch18:166 (4972) | corrected: N-K18-166 |
| K-ch18-168 | ch18:168 (4974) | not an unsupported assertion under the policy — RES: "under the finiteness posit A1 it is finite" is conditional |
| K-ch18-170/172 | ch18:170 (4976), :172 (4978) | corrected: N-K18-172 |
| K-ch18-174–184 | ch18:174–184 (4980–4990) | corrected: N-K18-174 |
| K-ch18-186/188/190 | ch18:186 (4992), :188 (4994), :190 (49 | corrected: N-K18-186 |
| K-ch18-192/194 | ch18:192 (4998), :194 (5000) | corrected: N-K18-192 |
| K-ch18-198/208 | ch18:198 (5004), :208 (5014) | corrected: N-K18-198 |
| K-ch18-244/246/262 | ch18:244 (5050), :246 (5052), :262 (50 | corrected: N-K18-244 |
| K-ch18-290 | ch18:290 (5096) | corrected: N-K18-290 |
| K-ch18-328 | ch18:328 (5134) | corrected: N-K18-328 |
| K-ch19-126 | ch19:126 (5273) | corrected: N-K19-126 |
| K-ch19-212 | ch19:212 (5359) | corrected: N-K19-212 |
| K-ch19-214/216 | ch19:214 (5361), :216 (5363) | corrected: N-K19-216 |
| K-ch19-80 | ch19:80 (5227) | corrected: N-K19-80 |
| K-ch19-360 | ch19:360 (5507) | corrected: N-K19-360 |
| K-appa-48 | appendix-a:48 (5572) | corrected: N-Kappa-48 |
| K-appa-181 | appendix-a:181 (5705) | corrected: N-Kappa-181 |
| K-appb-12/22 | appendix-b:12 (5766), :22 (5776) | corrected: N-Kappb-22 |
| K-appb-32 | appendix-b:32 (5786) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-appb-40 | appendix-b:40 (5794) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-appb-92 | appendix-b:92 (5846) | not an unsupported assertion under the policy — THM: theorem B.2.5 names "finiteness" among its premises |
| K-appb-451/454 | appendix-b:451 (6205), :454 (6208) | not an unsupported assertion under the policy — RES: scoped to the recurrence proof, to "any finite reversible substratum", or to "where the dynamics is P-indivisible" |
| K-appc-16 | appendix-c:16 (6246) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-appc-112–134 | appendix-c:112–134 (6342–6364) | corrected: N-Kappc-C6 |
| K-appc-154 | appendix-c:154 (6384) | corrected: N-Kappc-154 |
| K-appc-224 | appendix-c:224 (6454) | not an unsupported assertion under the policy — MOD: the framework's finite model or class (split rows: any sentence about the universe or nature is kept in Part A) |
| K-appc-120 | appendix-c:120 (6350) | not an unsupported assertion under the policy — ACC: no change in r3, or accurate as worded |
| K-gl-11 | glossary:11 (6595) | corrected: N-Kgl-11 |
| K-gl-13 | glossary:13 (6597) | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| K-appc-32/34 | appendix-c:32 (6262), :34 (6264) | corrected: N-Kappc-32 |
| K-gl-19 | glossary:19 (6603) | corrected: N-Kgl-19 |
| K-bk-90 | book/README:90 | corrected: N-Kbk-90 |
| K-bk-100 | book/README:100 | not an unsupported assertion under the policy — LBL: label, property or count retirement (A1 and "Finiteness" kept) |
| R-01 | README.md:6 | not an unsupported assertion under the policy — ACC |
| R-03 | `verification/coverage/LEDGER.json` en | not an unsupported assertion under the policy — LBL: MAIN:L-3 unchanged (M-08 dropped); its assumption "finiteness of S (total-finiteness posit)" is accurate |