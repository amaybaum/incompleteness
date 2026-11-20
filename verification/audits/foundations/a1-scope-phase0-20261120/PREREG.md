# A1-SCOPE Phase 0 — site map, target statements, controls and decision rule

**Status.** Writer's paper-only preregistration for independent non-author review. No manuscript
edit, no Lean, no new premise, no proof attempted beyond the elementary checks named in §3, and no
merge requested. A1 (Main posit ledger item (ii)) remains open and unadopted; physical measurement
sourcing remains not passed. This record fixes what Phase 1 may change and how the change is
checked; it does not authorize Phase 1, which needs a separate manuscript-edit decision.

**Authorization.** Owner `amaybaum`,
[#1055 comment 7030993647](https://github.com/amaybaum/incompleteness/issues/1055#issuecomment-7030993647),
2026-11-20T05:06:11Z, "Owner decision: A1-SCOPE framing, O-A4 and Phase 0", decision 3: "Phase 0:
authorized now. It is the complete corpus-wide census and preregistration of A1, finite-carrier and
posit-(ii) dependencies." Decision 1 fixes the framing: "A1 or the explicitly stated sufficient
conditions … H-μ must supply the *specific* measure properties each theorem uses". Decision 2 assigns
the finite-periodic-lattice question to O-A4, which this record does not do. The scope is the
proposal at [#1055 comment 7030887534](https://github.com/amaybaum/incompleteness/issues/1055#issuecomment-7030887534)
(2026-11-20T04:59:16Z).

**Scope correction received during drafting.** The coordinating session relayed an owner question:
the existing audits are authoritative inputs, their rows and classifications are cited and not
re-derived, and Phase 0 supplies only the delta they lack — the sentence-level site map keyed to
existing rows, the per-consumer measure properties with their equivalent / weaker / finite-model
marks, and the preserved list, controls, edit plan and decision rule. Disagreements between audits,
or between an audit and current `main`, are recorded as findings (§1.2) and not silently
reclassified. Accordingly no row of A1-REMAINDER, A1-FCLASS, A1-MAIN-ROOTS, A1-NECESSITY or the
A1-09 census is reclassified here; the class column of the site map is the class of the existing row
the site is keyed to.

**Goal link (§A.47).** Item: #1055 (A1 programme; serves #1169). The work decides, before any edit,
exactly which manuscript sentences carry total finiteness, which weaker condition each consumer can
state instead, and the mechanical test that a Phase 1 edit must pass, so that Main can stop requiring
a finite universe without importing an equally unsupported premise or implying a derived law.

**Source pin.** `main` at `d5735bedb3958394e3e095a4513d9fb5996d079d`. `M:n` is line `n` of
`papers/Main.md` at the pin; other papers and book files are named by basename. Main's line numbers
at the pin agree with the A1-REMAINDER pin `21e16c61` for every line cited below (the only Main
change between the pins edits line 540 in place).

## 1. Inputs and findings

### 1.1 Inputs (all on `main` at the pin; cited by short name)

| Short name | Path under `verification/` | Used for |
|---|---|---|
| REMAINDER | `audits/foundations/a1-remainder-20261119/REMAINDER.md` | consumer rows M1–M21, C1–C14; residues R1–R6; repairs P-μ, L1–L10, O-A4, O-INFLOW; hypotheses H-* (§3) |
| FCLASS | `audits/foundations/a1-finiteness-classes-20261117/CLASSIFICATION.md` | F1–F4 definitions; rows 01–27, U1–U2 |
| ROOTS | `audits/foundations/a1-main-roots-20261118/AUDIT.md` | Main roots R0–R8 |
| NEC | `audits/foundations/a1-necessity-20261117/ASSESSMENT.md` | five-family table |
| CENSUS | `audits/foundations/a1-09-dependency-census/CENSUS.md` | §7 (book/FULL parity), §17 (canonical statements), §18, §23.2 |
| LADDER | `audits/foundations/a1-10-recurrence-premises/PREMISE-LADDER.md` | F11, §3.4 |
| REC-1 | `audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md` | contract (V)(M)(I)(P)(RET)(RIG)(FS); Props 3.4, 3.6′, 5.1, 6.1, 6.2; verdict rows U1–U16 |
| RIGID | `audits/foundations/a1-rigid-visible-recurrence-20261119/A1-RIGID-1.md`; `lean-mathlib/OIBridge/ObservableRigidity.lean` | compact-orbit theorem; rotation × Bernoulli example |
| R1-INF | `audits/foundations/r1-inf-20261119/RESULT.md` | P-ED (Prop. 3, (G1)–(G4)); Lemma 8 (L3); Prop. 9; §6 consumer table |
| P8 (A1-05) | `audits/foundations/a1-05-p8-observer-selection/SOURCE-MATRIX.md` | P8-M operator inputs |
| P7B | `audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` | H1–H14 |
| PREP | `programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md` | 1.1–1.3, 1.5(d) inflow endpoint |
| Registry | `lean-manuscript-census.json` | family dispositions |

### 1.2 Findings on the inputs (recorded, not resolved here)

| Id | Finding | Evidence at the pin | Consequence for Phase 1 |
|---|---|---|---|
| F1 | REMAINDER row M14 describes "Characterization theorem window t ≪ t_R (M:540)", but M:540 at REMAINDER's own pin `21e16c61` contains no `t_R`; MAIN-TR-1 (`a8119d20`) removed it and is an ancestor of that pin (`git log 21e16c61 -- papers/Main.md`). REC-1 U11 also names M:540, :544 (older pin). | `grep -n 't_R' papers/Main.md` at the pin: M:155, M:449, M:453, M:644 only | The live `t_R` sites are M:155 (REC-1 U4), M:449/453 (REC-1 U11) and M:644 (M10). Phase 1 keys them to those rows, not to M14 |
| F2 | REMAINDER M4 lists ladder F11 among hypotheses "each with a bimeasurable bijection T preserving a normalized μ and positive cell masses". LADDER §3.4 and NEC's recurrence row state F11 for row-stochastic rooted laws only: "independent of cardinality of the hidden carrier", using "no hidden carrier, prior or reversibility". | LADDER §3.4 (lines 93–105); NEC §2 row 1 | The target for M4 under (NR) (§3) takes LADDER's weaker form: a normalized hidden prior shared by roots and a measurable update. The invariant-law contract enters only when (NR) is to be derived from (RIG) or compactness. Reviewer to confirm (§9 item 3) |
| F3 | The "Status" headers of REMAINDER and R1-INF still say "a delta review of the revised head is required", while their PRs record a confirmed delta review: #1421 comment at 2026-11-19T21:37:05Z ("Independent delta confirmation … CONFIRMED"), #1431 comment at 2026-11-19T23:44:30Z (same). | the two record headers; PR comments | Phase 1 relies on R1-INF Lemma 8 and Prop. 3 only as reviewed paper-level results (§A.46 item 7: a model's acceptance is evidence of review, not independent mathematical verification). Main must carry its own proof of anything it uses (§6.1) |
| F4 | REMAINDER M3 names L3 (double stochasticity under an invariant product law with uniform visible marginal) as not proved. R1-INF Lemma 8, landed after REMAINDER, proves it for any measurable `V × H` and any `F`-invariant `ν ⊗ ρ` with `ν` uniform; its restriction to window readouts concerns only when `β_A` has that product form. | R1-INF lines 268–279 | L3 is available; the Phase 1 sentence carries its one-line proof (§6.1 E9) |
| F5 | `OIBridge/Finiteness.lean`'s header quotes a Lemma 1 text ("with a discreteness scale ε providing a finite minimal cell volume … holographic entropy bounds") that differs from Lemma 1 at M:46. The module's registry disposition is `current`. | `Finiteness.lean` lines 1–8; M:46 | Outside A1 (it concerns F3, visible finiteness). Recorded for the owner; Phase 1 does not edit Lean |
| F6 | Four lexical hits of an earlier pattern set were not A1 sites: "definite substratum" (appendix-c:54, ch19:64, Methodology:397, :401) matched an unanchored "finite substratum". The patterns in §2.1 are anchored; two genuine false positives remain (appendix-b:235, :246, where "(A1)" labels an anomaly equation). | §2.1 patterns | Recorded so that the counts in §2.3 can be reproduced |

## 2. Site map (delta 1)

### 2.1 Method

Every non-blank line of `papers/*.md` and `book/*.md` (chapters, appendices a/b/c, glossary,
preface, README and FULL) was scanned line by line with Python `re` for two pattern sets. A line is
one site; a site may match several patterns. Each site carries the quote of the sentence containing
its first match, the existing audit row(s) it belongs to, the residue class of that row, and the
Phase it falls in. The machine-readable map is [`sites.json`](sites.json) (schema
`a1-scope-phase0 site map v1`), which stores both pattern sets verbatim.

Core set (the terms the authorization names):

| Id | Pattern (Python `re`) | Target |
|---|---|---|
| P1 | `\bA1\b` | A1 |
| P2 | `[Tt]otal[- ]finiteness\|totally finite\|(?<![A-Za-z])finite total (system\|configuration\|state)` | total finiteness |
| P3 | `(?<![A-Za-z])finite \$?\\?(mathcal\{)?S\}?\$?([^a-zA-Z]\|$)\|\$S\$ (is )?finite\|\$\|S\|\$\|\\lvert S\\rvert\|\|S\|` | "finite S", `|S|` |
| P4 | `(?<![A-Za-z])finite configuration space\|finitely many (complete )?configurations\|(?<![A-Za-z])finite (state\|configuration\|phase) space` | finite configuration space |
| P5 | `posit \(ii\)\|ledger item \(ii\)\|item \(ii\) of the posit\|ledger \(ii\)\|posit-\(ii\)` | posit (ii) |
| P6 | `counting measure\|counting probability\|uniform (hidden )?prior\|uniform (probability\|measure\|distribution) (on\|over) (the )?(\$?S\|configuration\|\\mathcal\{C\})\|maximal[- ]entropy invariant` | uniform or counting measure |
| P7 | `t_R\|t_\{R\}\|t_\{\\rm R\}\|[Pp]oincar[ée] recurrence\|recurrence time` | recurrence time |
| P8 | `(?<![A-Za-z])finite universe\|universe (is\|be) finite\|(?<![A-Za-z])finite (substratum\|bijection\|reversible substratum\|representative)` | finite universe / representative |

Paraphrase set (sites matching no core pattern): finite periodic lattice; eventual image and
injectivity-to-surjectivity; recurrence-scale / recurrence-cycle / exact return / `\Gamma_L = I` /
orbit of period / `\log_2 p`; canonical typicality; maximal-entropy measure or selection; finite
hidden space, finite carrier, finitely many states, finite cardinality, finite information; uniform
measure, counting or law; finite bijective; finiteness of `S`; `\mathcal{C}_H` finite. The exact
regular expressions are in `sites.json` (`paraphrase_patterns`).

Reproduction: the scan is the loop described above over `sorted(glob('papers/*.md')) +
sorted(glob('book/*.md'))` at the pin, one record per matching line; FULL lines were matched to
chapter lines by exact string equality (CENSUS §7's recipe).

### 2.2 Coverage and its limits

- **Covered.** All 12 papers, all 30 book Markdown files including FULL, glossary, preface and
  appendices a/b/c, at the pin. All 135 FULL sites are exact copies of chapter lines (re-checked here;
  CENSUS §7 established parity at an earlier pin), so FULL carries no site absent from the chapters.
  Lean: header and docstring text of the modules whose comments contain A1, total finiteness or
  posit (ii) wording (§2.6).
- **Structural sites.** A consumer can use finiteness without any listed word. The REMAINDER rows
  whose cited step has no lexical hit are listed in §2.5 from REMAINDER's own locators.
- **Not covered.** `.tex` and PDF artifacts (generated from stamped sources; `tools/staleness_check.py`
  reports 13 matched at the pin); Lean proof bodies; registry notes; verification records; FCLASS U1
  and U2 claim chains (book ch18 cosmology, biology and medicine chapters are mapped at site level
  only); implicit uses phrased without any listed word or REMAINDER locator. A1-C01 remains
  incomplete, and this map does not certify the absence of other A1 consumers.
- **Keying.** A site is keyed to the existing row whose claim it states, restates or mirrors. Where
  several rows apply, all are listed; the class column is the class of the first. Sites that state
  the posit itself are keyed to REMAINDER §3 (`REM-s3`, class DECL). No new row is created.

### 2.3 Counts

499 sites: 377 core, 122 paraphrase-only; 364 outside FULL and 135 in FULL. Classes: DECL states or
points to posit (ii); R1–R6 are REMAINDER residues; B is REMAINDER class (b), A1-free under a named
hypothesis; INFLOW marks sites where finiteness excludes PREP 1.5(d)'s incoming stream; FREE is A1-free
already or an explicit finite-model statement already labelled; FP is a false positive.

| File | DECL | R1 | R2 | R3 | R4 | R5 | R6 | B | INFLOW | FREE | FP | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `papers/Main.md` | 10 | 6 | 8 | 0 | 0 | 2 | 1 | 14 | 0 | 27 | 0 | 68 |
| `papers/GR.md` | 3 | 3 | 2 | 0 | 0 | 0 | 2 | 4 | 0 | 15 | 0 | 29 |
| `papers/Substratum.md` | 2 | 0 | 0 | 1 | 14 | 0 | 3 | 3 | 1 | 9 | 0 | 33 |
| `papers/SM.md` | 1 | 8 | 0 | 0 | 7 | 0 | 0 | 5 | 0 | 1 | 0 | 22 |
| `papers/Structure.md` | 0 | 0 | 0 | 0 | 1 | 0 | 41 | 8 | 0 | 3 | 0 | 53 |
| `papers/Methodology.md` | 2 | 0 | 0 | 3 | 0 | 0 | 5 | 2 | 0 | 2 | 0 | 14 |
| `papers/Computation.md` | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 5 |
| `papers/Complexity.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 |
| `papers/Introduction.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |
| `papers/Medicine.md` | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| `book/ch00-introduction.md` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 |
| `book/ch01-observation.md` | 2 | 3 | 1 | 1 | 0 | 0 | 0 | 5 | 0 | 2 | 0 | 14 |
| `book/ch02-substratum.md` | 3 | 0 | 1 | 1 | 6 | 0 | 4 | 1 | 0 | 2 | 0 | 18 |
| `book/ch03-structural-realism.md` | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 2 | 0 | 8 |
| `book/ch04-methodology.md` | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 2 | 0 | 5 |
| `book/ch05-gauge-structure.md` | 1 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | 0 | 0 | 0 | 8 |
| `book/ch07-gravity.md` | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| `book/ch09-universality.md` | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 3 | 0 | 9 |
| `book/ch11-origin-of-life.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| `book/ch14-quantum-computing.md` | 3 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 5 |
| `book/ch18-beyond.md` | 4 | 1 | 15 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 21 |
| `book/ch19-open-problems.md` | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| `book/appendix-b-derivations.md` | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 6 | 2 | 16 |
| `book/appendix-c-objections.md` | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| `book/glossary.md` | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 2 | 0 | 7 |
| `book/preface.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 2 |
| `book/…-FULL.md` (mirrors) | 34 | 9 | 19 | 2 | 15 | 0 | 13 | 17 | 1 | 23 | 2 | 135 |
| **Total** | 87 | 36 | 49 | 8 | 52 | 2 | 80 | 70 | 4 | 107 | 4 | 499 |

By phase, outside FULL: Phase 1 (Main and its book mirrors) 81, Phase 2 (companions and their
mirrors) 155, O-A4 37, preserved without edit 89, false positive 2. In FULL: 40, 53, 15, 25, 2.

### 2.4 Main, sentence level (Phase 1 scope)

Quotes are the opening of the sentence containing the first match; `sites.json` holds the full
sentence. "Action" is the Phase 1 proposal of §6: E*n* an edit unit, N no edit (the sentence is
already scoped to a finite representative or model), K preserved (§4).

| Site | Quote | Rows | Class | Action |
|---|---|---|---|---|
| M:18 | "On a fixed finite reversible representative … equivalent to a memory obstruction, $M_k>0$ at some order $k$ below the recurrence time …" | M7 | R2 | N |
| M:36 | "Total finiteness remains an open physical posit (status Remark, §1.2 and ledger §4.5, item (ii))." | REM-s3 | DECL | E1 |
| M:44 | "… and the map acts on a finite $S$ under the total-finiteness posit (§1.2 Remark, §4.5 ledger) …" | REM-s3 | DECL | E2 |
| M:54 | "… globally, the counting measure is selected among invariant measures as the maximal-entropy one …" (Lemma 3) | M1, M11 | R1 | K |
| M:58 | "… the counting probability on the eventual image of a non-bijective description … belongs to a different representative choice …" | M1, M3 | R1 | N |
| M:60 | "Total finiteness of that representative is a premise of the results that use it, carried as item (ii) of the posit ledger …" | REM-s3, M1, M2, M3, M11, M13, M21 | DECL | E3 |
| M:72 | "One-way influence can suffice for recurrence-cycle indivisibility (§3.4, non-permutation witness)." | M4 | B | N |
| M:76 | "Exhaustive enumeration over the realizations … at $(n_V,\|\mathcal C_H\|)=(2,2),(2,3),(2,4),(3,2)$ …" | CEN17 Main 508/608 | FREE | K |
| M:80 | "… indivisibility somewhere in the recurrence cycle of a fixed finite reversible representative …" | M7 | R2 | N |
| M:111 | "By Lemma 1 the visible sector is finite; under the total-finiteness posit (§1.2 Remark, §4.5 ledger) the hidden sector is also finite …" | REM-s3 | DECL | E4 |
| M:113 | "**Theorem.** *Let $\mathcal C_V$ and $\mathcal C_H$ be finite sets …*" | M4 | B | K |
| M:129 | "Lemma 1 gives the finite visible space; the hidden space is finite under the total-finiteness posit (§1.2, §4.5)." | M4 | B | E5 |
| M:137 | "*Proof.* Because $\varphi$ is a permutation of a finite set, it has finite order $L$, so $\Gamma_L=I$ …" | M5 | R2 | K |
| M:139 | "Under a full-support prior, the gap it is equivalent to may lie at any order below the recurrence time …" | M7 | R2 | E6 |
| M:141 | "**Theorem (overlap and return).** *Let $\mathcal C_V$ and $\mathcal C_H$ be finite sets …*" | M6 | FREE | K |
| M:155 | "If the flow then returns near-totally at a common time — some $t_R>t_1$ …" | REC-1 U4 | FREE | K |
| M:178 | "… the former establishes P-indivisibility from a non-permutation one-step witness and finiteness alone, at the recurrence time …" | M4 | B | E7 |
| M:180 | "The recurrence theorem uses no form of (C2), deriving recurrence-cycle P-indivisibility from a non-permutation rooted map and finite order alone …" | M4 | B | N |
| M:208 | "Marginalizing a bijection under the uniform hidden prior yields a doubly stochastic one-step matrix (§3.2) …" | M3 | R1 | N |
| M:214 | "… the source's membership conditions are the tuple's own — a finite configuration space …" | CEN17 Main 484/550 | FREE | K |
| M:216 | "… whether the available interventions on a finite carrier and its composites are exactly the quantum instruments …" | FCLASS 26, C5 | FREE | K |
| M:222 | "… runs on finite configuration spaces: Lemma 1 for the visible sector, with the total-finiteness posit (§1.2 Remark, §4.5) where a result also needs the hidden sector finite." | REM-s3 | DECL | E8 |
| M:266 | "**Setup.** The finite configuration spaces … ($\mathcal C_H$ under the total-finiteness posit, §1.2, §4.5) …" | M12, REM-s3 | DECL | E8 |
| M:274 | "**Lemma (Reverse direction, scoped).** *Any single one-step doubly stochastic matrix on a finite configuration space …*" | M3 | R1 | K |
| M:276 | "*Proof.* Any marginal of a bijection with uniform prior is a doubly stochastic matrix …" | M3 | R1 | K |
| M:278 | "*Remark.* This is the correspondence for a single step with a uniform hidden prior …" | M3 | R1 | E9 |
| M:324 | "All of this concerns the realization displayed above and is not a property of arbitrary finite bijections." | CEN17 Main 298/326 | FREE | K |
| M:338 | "(2) **Stochastic P-indivisibility** … which on one fixed finite reversible representative is what the recurrence-scale theorem delivers …" | M4 | B | N |
| M:352 | "*Level three (characterized conditionally):* … on a finite carrier …" | FCLASS 26, C5 | FREE | K |
| M:356 | "… every fixed finite representative has finite predictive dimension …" | CEN17 Main 298/534 | FREE | K |
| M:437 | "**Dilation existence.** Any single one-step doubly stochastic matrix on a finite configuration space …" | CEN17 Main 484/550 | FREE | K |
| M:439 | "**Lemma (non-permutation witness).** *For the finite bijective model of §3.2 with its common uniform hidden prior …*" | M4, REC-1 U6 | B | K |
| M:441 | "*Proof.* The common uniform prior makes $T$ doubly stochastic …" | M4, REC-1 U6 | B | K |
| M:449 | "For a finite reversible realization there is no relaxation in the strict sense — … Poincaré recurrence at $t_R$ …" | REC-1 U11, M16 | R2 | N |
| M:453 | "… holds on accessible timescales $t\ll t_R$ …" | REC-1 U11, M16 | R2 | N |
| M:457 | "… with $\pi_H$ the *reference prior defining $T$* — the uniform hidden prior of the model above …" | M16 | R6 | N |
| M:486 | "… both instruments and $\varphi$ verified bijections on $\|S\|=124{,}416$ …" | CEN17 Main 484 | FREE | K |
| M:490 | "*Proposition (no uniform finite realization).* A fixed finite $S$ with a fixed prior and a fixed bijection …" | CEN17 Main 484 | FREE | K |
| M:528 | "**Definition (unitarily evolving QM).** A stochastic process $\mathcal S$ on a finite configuration space …" | CEN17 Main 528 | FREE | K |
| M:534 | "… for the uniform hidden prior, $T^{(k)}_{ij}=\frac1{\|\mathcal C_H\|}\sum_{h,l}\ldots$ exactly …" | CEN17 Main 534 | FREE | K |
| M:540 | "**Characterization theorem.** *Let $\mathcal S$ be a time-homogeneous stochastic process on a finite configuration space $\mathcal C_V$ …*" | CEN17 Main 550 | FREE | K |
| M:558, 566, 588, 604, 648, 658, 778, 780 | finite operational carrier statements ("on a finite carrier with complex matrix kinematics taken as given …") | FCLASS 26, C5 | FREE | K |
| M:592 | "… the concrete OI substratum, in its finite model (ledger item (ii)), supplies the structural architecture …" | C5, REM-s3 | DECL | N |
| M:616, 620, 622 | exhaustive probes "under the uniform prior" at stated $(n_V,\|\mathcal C_H\|)$ | CEN17 Main 608/626 | FREE | K |
| M:632 | "… on finite representatives at the recurrence scale from a non-permutation one-step witness (§2.3) …" | M4 | B | N |
| M:644 | "*Remark (consolidation).* … a bijection on a finite set has finite order $L$ … windows $t\ll t_R$ by one fixed substratum before its recurrence …" | M10 | R2 | N |
| M:660 | "… renewal processes, semi-Markov processes on finite state spaces …" | CEN17 Main 484/550 | FREE | K |
| M:662 | "… and canonical typicality [31], which the structural observer-selection theorem of §4.6 uses." | M19 | R5 | N |
| M:696 | "**Joint description.** For the finite hidden sector with the uniform conditional law on $H$ …" | CEN17 Main 298 | FREE | K |
| M:706 | "Finiteness of the hidden sector is, in the forward construction, item (ii) of the posit ledger (§4.5), an open hypothesis, not adopted …" | REM-s3 | DECL | E10 |
| M:722 | "Recurrence-scale P-indivisibility uses finite order of the specified bijective representative and a non-permutation rooted map …" | M4 | B | E11 |
| M:724 | "**Falsifiability.** … a deterministic bijection on a set whose finiteness is the total-finiteness posit (§1.2 Remark, §4.5 ledger item (ii)) …" | REM-s3 | DECL | E12 |
| M:730 | posit ledger, items (ii), (iii), (iv) and the closing sentence | REM-s3, M11, M1, M2, C14 | DECL | E13 |
| M:739 | status ledger: "bare-recurrence form from a non-permutation rooted map at the recurrence time $L$" | M7 | R2 | N |
| M:748 | "An immediate corollary of (C1)–(C4) is a structural selection rule on where in a finite bijective $(S,\varphi)$ observers can exist." | M18, M20 | B | N |
| M:756, 758 | "… local equilibrium macrostate in the sense of canonical typicality [31] …" | M18 | B | N |
| M:762 | "For $(S,\varphi)$ in its equilibrium macrostate, canonical typicality [31] implies every local subsystem is also in its local equilibrium." | M19 | R5 | N |
| M:764 | "**Scope.** The theorem uses bounded coupling, finiteness of $S$, the canonical-typicality result [31], and the effective-mixing hypothesis (EM) …" | M18, M20 | B | E14 |

### 2.5 Structural sites in Main without a lexical hit

From REMAINDER's locators: M:113–127 (M4; finite order at Step 1, M:121); M:135 (M5 statement,
"of order $L$"); M:143 (M6 proof); M:145 (M8, routed readback "for some n"); M:147–151 (M13,
$P_{\rm perm}$ counts bijections of a finite set); M:163 (uniform erosion, consumed by M20); M:330–334
(M9); M:362 (M17); M:414–416 (M17); M:471–475 (M16); M:508–518 (M15); M:750 (M18: "the exact Koopman
operator of $\varphi$ … has … exact recurrence"); M:760 (M20). Each is either preserved (§4) or
covered by the paragraph edit named for its row in §6.1; none needs its own edit unit.

### 2.6 Book mirrors of the Phase 1 sites, and the rest of the corpus

Phase 1 book sites (FULL line in brackets):

| Site [FULL] | Rows | Class | Action |
|---|---|---|---|
| ch00:95 [320] | REM-s3, C6 | DECL | B1 |
| ch01:28 [361] | REM-s3 | DECL | B2 (mirror E2) |
| ch01:38 [371], :81 [414], :85 [418] | M1 | R1 | N |
| ch01:41 [374] | M11 | R3 | N (stated "on a finite set") |
| ch01:93 [426], :95 [428], :97 [430], :119 [452], :121 [454] | M4 | B | B3 (mirror E5) |
| ch01:161 [494] | REM-s3 | DECL | N (mirror of M:592) |
| ch01:177 [510] | M10 | R2 | B4 |
| ch19:126 [5195] | REM-s3, C5 | DECL | N |
| ch19:212 [5281], :214 [5283], :216 [5285], :360 [5429] | REM-s3 | DECL | B5 |
| appendix-b:42 [5718], :44 [5720] | M3 | R1 | K (mirror of the frozen reverse lemma) |
| appendix-b:46 [5722] | M3 | R1 | B6 (mirror E9) |
| appendix-b:419 [6095], :453 [6129], :456 [6132] | M5, M4, M7 | R2/B | N |
| appendix-c:16, 96–116, 136 [6170, 6250–6270, 6290] | REM-s3 | DECL | B7 (C.6 response) |
| glossary:11 [6501], :137 [6627] | REM-s3 | DECL | B8 |
| glossary:105 [6595], :117 [6607] | M4, M7 | B/R2 | N |
| preface:3 [62] | M4 | B | N ("In the finite reversible model …") |

Companion and remaining book sites, by row (Phase 2 or O-A4 unless marked K; site lists in
`sites.json`):

| Phase | Class | Rows | Sites |
|---|---|---|---|
| P2 | R1 | C1, C2, C4 | GR:58, :88, :124; ch07:42 |
| P2 | R1 | M1 (selection consumers) | Computation:122; ch14:272; ch18:36; SM:252 (B: "or a stated structured prior"); SM:292, 334, 336, 1225, 1227 |
| P2 | R1 | R1-INF §6 note (A1-independent tension) | SM:803, 809, 811 |
| P2 | R2 | M5/M7/M13 restatements | ch02:32; ch18:20, 162–192 (15 sites); Medicine:25 |
| P2 | R2 | REC-1 U15 | GR:589, 591 |
| P2 | R3 | M11 | Substratum:94; ch02:78; Methodology:106, 146, 148 |
| P2 | R6 | C11 (OI class A1–A6) | Structure (41 sites, :80–:1305); ch03:34, 44; ch09:18, 36, 106, 183, 189, 193; Methodology:339–369 |
| P2 | R6 | C8, C9, C12, GR App. A | Substratum:44, 262, 268; ch02:14–18, 144; Computation:178, 182; ch14:262; GR:609, 719 |
| P2 | B | M4, C3, C10 | SM:24, 112, 236, 308; Structure:718, 1116–1189; Substratum:137, 401, 407; GR:138; Methodology:283, 441; ch02:192; ch03:58, 102, 240; ch04:36; ch05:95 |
| P2 | DECL | C5, C6, C9, C12, REM-s3 | GR:20, 257, 261; SM:22; Substratum:92, 389; Computation:120; Methodology:156, 158; ch02:76, 136, 212; ch03:84; ch05:23; ch07:118; ch14:160, 164, 184; ch18:242, 244, 260, 288 |
| P2 | INFLOW | C10 | Substratum:56; Complexity:212; ch18:40 |
| OA4 | R4 | C6, C7, CEN17 SM 210/641 | Substratum:98, 104, 123–133, 157, 193, 205–233; SM:20, 158, 202, 222, 232, 316, 641; Structure:768; ch02:82–122; ch04:10, 26; ch05:19, 25, 65–89; glossary:13 |
| K | FREE / B | C3, C5, C8, CEN17/18 rows | GR:134, 174, 190–328, 673, 817, 875, 885; Substratum:14, 253, 266, 344, 348, 359, 373, 459, 533; SM:1648; Structure:1096, 1233, 1251; Computation:144; Complexity:292; Introduction:34, 129; Methodology:409, 529; book mirrors |

Lean header and docstring sites with A1 wording (no Lean edit in any phase of A1-SCOPE; registry
dispositions at the pin):

| Module (disposition) | Lines | Content | Row |
|---|---|---|---|
| `CanonicalMeasure` (current) | 1–40 | quotes Lemma 3; "the lemma's formal obligation is entirely finite" | M1 — stays true while Lemma 3's statement is frozen (CTL-4) |
| `Finiteness` (current) | 1–30 | quotes a Lemma 1 text differing from M:46 | F5 |
| `SubstratumInterfaceAudit` (kernel-only) | 7–16, 83–84, 108–109, 184–185, 769, 785–786 | `A1 : Prop := Finite 𝒮.Conf`; `a1_of_finite` | C6/C7 (O-A4) |
| `ManuscriptAxioms` (kernel-only) | 4–97 | realized-core images of A1, A2 | C6 |
| `ObservableRigidity` (kernel-only) | 8–16 | A1-RIGID-1 theorem | M4 |
| `SubstratumSource` (current) | 48 | "does not derive a quantum architecture from A1-A6" | C5 |
| `HexLatticeGas`, `A6Instantiation`, `HydroSourceAudit`, `FrozenSourcing`, `RouteB`, `RecursiveFiniteFactor` (kernel-only) | as grepped | A1 for specific finite models; "nothing here changes A1–A6" | C6 / FREE |

## 3. Per-consumer target statements (delta 2)

Each row gives what the theorem consumes under A1, the stated sufficient condition that replaces it
where one exists, the exact measure properties that condition uses (for H-μ), and the mark:
**equivalent** (any hypothesis that makes the statement true as stated is equivalent to A1 for it),
**weaker** (strictly weaker, with the separating example), or **finite-model only** (no traced
replacement; the statement is kept as a statement about finite representatives). Hypothesis labels
proposed for Main: (NR) later common near-return; (IL) invariant law with the listed properties;
(REV) reversibility; (ED) entropy-density selection; (IN) inflow condition, open. No label collides
with an existing Main label (checked by `grep -F` at the pin).

### 3.1 Main consumers

| Row | Under A1 | Stated sufficient condition (status) | Measure properties used | Mark | Source |
|---|---|---|---|---|---|
| M1 Lemma 3 selection | counting probability on the finite representative, maximal Shannon entropy among invariant laws | finite representative; or (ED), posited: carrier a full site product $A^{\mathbb Z^d}$, $A$ finite; injective local rule; admissible laws invariant under the rule **and** every lattice translation; selection by entropy per site | normalization; invariance under the rule; translation invariance; entropy density. Selected law: uniform product $\beta_A$ | counting form: **equivalent** (a uniform probability exists iff the carrier is finite). (ED): **weaker**, separating example $\beta_A$ on $A^{\mathbb Z^d}$ (R1-INF Prop. 3); not observationally distinguishable (R1-INF §7; REMAINDER §3). Without translation invariance the selection fails for $d\ge2$ (R1-INF Prop. 9(b)) | R1-INF Prop. 3, Lemma 2, Prop. 9 |
| M2 μ-G, μ-O, μ-R, posit (iv) | uniform on the carrier / on the actual orbit / on the record-compatible orbit union | μ-G as M1; μ-R collapses to μ-G under (ED) (R1-INF Prop. 7.2); μ-O: none | μ-G as M1. Stationarity and no production (PREP 1.1–1.3) use normalization and invariance only | μ-O and the static budgets $\log_2(\|S\|/\ell)$: **finite-model only** (L2 open). μ-G: as M1. μ-R: **weaker** under (ED), with the record clause vacuous | REMAINDER M2; R1-INF Props 7.1–7.2 |
| M3 baseline matrices | $T_{ij}$ counts a finite hidden set | rooted maps $\Gamma_t(a,b)=\rho\{h:\pi_V F^t(a,h)=b\}$ for one normalized hidden prior $\rho$ shared by roots (already allowed at M:135, M:141) | normalization of $\rho$ only | **weaker**, separating: any infinite measurable hidden space (RIGID example) | REMAINDER M3; RIGID "common hidden-prior convention" |
| M3 doubly stochastic corner | uniform prior on finite $\mathcal C_V\times\mathcal C_H$ | (IL), posited: $F$ preserves a probability $\mu=\nu\otimes\rho$ with $\nu$ uniform on $V$ | normalization; $F$-invariance; product form $\nu\otimes\rho$; uniform visible marginal. Not used: ergodicity, uniform $\rho$ | **weaker**, separating: RIGID rotation × Bernoulli pulls back to $\mathrm{Unif}(\{0,1\})\otimes\rho$; $\beta_A$ with a window readout (R1-INF Lemma 8). Countercontrol: non-invariant $\mathrm{Unif}(V)\otimes\delta_0$ fails (R1-INF §9 C) | R1-INF Lemma 8 (F4) |
| M4 one-step theorem | finite order: $\Gamma_N=I$ (M:121) | (NR), posited: roots $a\ne b$, value $x$ with $m=\min(\Gamma_s(a,x),\Gamma_s(b,x))>0$, and some $n>s$ with $(1-\Gamma_n(a,a))+(1-\Gamma_n(b,b))<m$. Conclusion: not P-divisible on $\{0,\ldots,n\}$ | normalization of the shared prior $\rho$ (row-stochasticity); measurable update. Not used: invariance, product form, bijectivity, hidden cardinality. (NR) itself is supplied by: A1 + bijectivity ($n=N$); (RET); (RIG) under (V)(M)(I)(P) [bimeasurable bijection, invariant $\nu\otimes\rho$, $\nu(a)>0$]; RIGID compactness [same + compact closure of the indicator orbit] | **weaker**, separating: RIGID rotation × Bernoulli; REC-1 golden rotation (indivisible on $\{0,1,2,3\}$). Lost: the specific $N$ | LADDER §3.4; REC-1 Prop. 3.4; RIGID Thm (F2) |
| M5 readback + recurrence | order $L$ gives $\Gamma_L=I$, $\Gamma_{t+L}=\Gamma_t$ and $s\le\min(k,L-1)$ | non-permutation $\Gamma_s$ with $1\le s\le k$: no recurrence, no invariant law (REC-1 Prop. 6.1); P-indivisibility then under (NR) at that $s$ | Prop. 6.1: measurable $F$, normalized $\rho$ shared by roots, roots drawn independently of $\rho$. (NR) as M4 | first half: **weaker** (holds with no finiteness). $s\le L-1$ and endpoint $\{0,\ldots,L\}$: **finite-model only** in Phase 1; (RET) at $L$ with (M)(I)(P) would be **weaker** (separating: rules with $F^N=\mathrm{id}$ on an infinite lattice, R1-INF countermodel C4(i)) but its proof (REC-1 Prop. 3.6′) is not carried into Main | REC-1 Props 6.1, 3.6′, U2 |
| M6 overlap and return | finiteness only in the setup | — (A1-free) | none beyond a probability $\mu_H$ | preserved (§4) | REMAINDER M6 |
| M7(i) index-free equivalence | finite order | (a)⇒(b): Prop. 6.1; (b)⇒(c): (NR) after the non-permutation time; (c)⇒(a): Markov argument. Each direction separately (§A.34) | (FS) full-support visible prior independent of $\rho$; normalized $\rho$; (NR). REC-1 Prop. 6.2 obtains (NR) from (RIG) under (V)(M)(I)(P) | **weaker**, separating: RIGID rotation × Bernoulli | REC-1 Prop. 6.2 |
| M7(ii) L-indexed form | exact return at $L$ | none carried into Main | — | **finite-model only** | REC-1 U2 |
| M8 routed readback "for some n" | `rootedMap_periodic` | storage-time overlap, then (NR) | as M4; the write clause's seed $\mu_H(h)>0$ needs an atom or a positive-measure seed set | "for some n": **weaker**; write/store/read formalization: **finite-model only** (finite-carrier Lean modules) | REMAINDER M8; REC-1 U14 |
| M9 CP-indivisibility | permutation unitary on finite $H$ | none (L6 open). The implication from a supplied P witness is carrier-independent | — | **finite-model only** | REMAINDER M9 |
| M10 all-time classification | finite order | none needed for the theorem; no A1-free physical reading (GLUE, RIGID give aperiodic exact families) | — | theorem preserved as a finite-realization statement; physical reading **finite-model only** | REMAINDER M10 |
| M11 bijectivity | eventual image; injective ⇒ surjective on a finite set; prong 1 uses uniform-prior double stochasticity | (REV), posited: $T$ a bimeasurable bijection of a measurable carrier (the alternative already printed at M:730 (iii)); prong 1 under (IL) with $\nu$ uniform | prong 1: as M3 corner | (REV): **weaker** in cardinality (separating: GLUE carrier; RIGID example) but assumes the conclusion the A1 route recovers; eventual-image prong: **finite-model only** | REMAINDER M11, R3 |
| M12 §3.2 representation | finite $H$ constructed per law | — | — | preserved | REMAINDER M12 |
| M13 orbit capacity, $P_{\rm perm}$ | finite orbit, uniform count over bijections | none | — | **finite-model only** (non-root, ROOTS R0, R8) | REMAINDER M13 |
| M14 `t_R` | see F1 | REC-1 U11: no common $t_R$ without a return condition; accessibility scale stated independently of recurrence | — | live sites M:155 preserved (already conditional on a common near-return); M:449/453/644 inside finite-realization statements, **finite-model only** | F1; REC-1 U4, U11 |
| M15 C3 capacity bound | counts hidden states of a realization | — | — | preserved | REMAINDER M15 |
| M16 physical-memory theorem | uniform-prior finite coupling model | none (L7 open) | reference prior $\pi_H$ | **finite-model only** | REMAINDER M16 |
| M17 causal cone, Bell ceiling | finite-site presentation | arbitrary-site form already in Main (M:362, M:414–416) | — | preserved | REMAINDER M17 |
| M18 §4.6 operator step | counting inner product; finite $S$ | (IL) for §4.6, posited: a normalized $\varphi$-invariant $\mu$; $P$ the $\mu$-conditional expectation onto the declared local observables; finite readout support with a locally finite dependence cone; (EM) as $\|K^n\|\le Ce^{-n\Delta t/\tau_{\rm mix}}$ on $\mu$-centred observables | normalization; invariance; the $L^2(\mu)$ structure. Not used: product form, uniformity, separate ergodicity | operator step: **weaker**, separating: Bernoulli shift (mixing on an infinite carrier, REC-1 U10). Transfer to $\tau_B$ and to $PU^nP$: A1-independent source gap, not claimed | P8 P8-M; REMAINDER M18 |
| M19 global typicality | canonical typicality on a finite-dimensional energy shell | none (L8 open); narrowing to a supplied local-equilibrium state | — | **finite-model only** | REMAINDER M19, R5 |
| M20 anti-Boltzmann-brain | inherits M18 | as M18 at the operator step | as M18 | operator step **weaker**; remaining steps A1-independent gaps | REMAINDER M20 |
| M21 deep sector | finite decoupled factor | finite windows: GR Appendix B (D1)–(D5), any cardinality | (D5) $\mu_H=u_{B_n}\otimes\nu$: product; uniform on the finite boundary layer; $\nu$ normalized, otherwise arbitrary | finite windows: **weaker** (separating: infinite deep sector with any $\nu$). All-time infinite factor: **finite-model only** (L9) | REMAINDER M21 |
| Inflow | A1 excludes PREP 1.5(d)'s invariant inflow law | (IN): a stated condition on incoming boundary supply — **open**, not a premise of any result | PREP 1.5(d): the inflow law is shift-invariant and singular to the product-uniform law, so (IL) does not exclude it | — | REMAINDER §5; PREP 1.5(d) |

### 3.2 Companion consumers (Phase 2; listed so Phase 1 introduces nothing that contradicts them)

| Row | Stated sufficient condition | Measure properties | Mark |
|---|---|---|---|
| C1 H-count (GR:58) | decoupled: P7B H1–H14 | H4: normalized shell counting on finite boundary modes ⊗ one deep law $\nu$ of any cardinality, no energy reweighting; decoupled product dynamics | counting on a finite total shell: **equivalent**; decoupled P7B form: **weaker**; coupled case: **finite-model only** (P7B node 6.3) |
| C2 calibration | inherits C1 | as C1 | as C1; (U1)–(U3) preserved |
| C3 deep sector without H-BD | GR Appendix B (D1)–(D5) | as M21 | preserved |
| C4 H-BD | none (L10) | — | **finite-model only** |
| C5 operational completion | — | — | preserved |
| C6, C7 Theorem 23, $d=3$ | O-A4 | — | **finite-model only** until O-A4 reports; the reconstruction states its finite periodic lattice |
| C8 Theorem 24 | finite identities; finite windows as C3; infinite factor L9 | as M21 | identities preserved; infinite transfer **finite-model only** |
| C9, C11, C12, C14 | none | — | **finite-model only** (labels); C12 counts $\|S\|$: **equivalent** |
| C10 equilibrium scope | inherits M18–M20; inflow sites carry (IN) open | as M18 | as M18; INFLOW sites Substratum:56, Complexity:212, ch18:40 |
| C13 forward gauge algebra | — | — | preserved |

## 4. Preserved statements (must not change)

| Statement | Exact assumptions as printed | Where |
|---|---|---|
| Lemma 1 and the Definition (observer-relative finiteness) | finite-capacity clause of the Definition ⇒ $\mathcal C_V$ finite; "only finite visible resolution is a theorem" | M:42, M:46, M:60 |
| Lemma 3 statement | bijective representative; uniform invariant law on each finite cycle; counting measure selected as maximal-entropy (a selection principle) | M:54 (kernel `CanonicalMeasure`) |
| Finite-horizon process dilation and extension | finite $\mathcal C_V$, finite horizon, kernels of the stated class; constructed finite hidden space | M:520–524 |
| S ⇔ D ⇔ Q_fb | finite visible alphabet, finite accessible horizon $K$ | M:550–556 (`finite_horizon_equivalence`, `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S`) |
| Characterization theorem | time-homogeneous process on finite $\mathcal C_V$, $\|\mathcal C_V\|\ge2$; (T) for (i) | M:540–546 |
| One-step theorem, history-readback theorem, their proofs | finite $\mathcal C_V,\mathcal C_H$, bijection; order $L$ | M:113–127, M:135–137 |
| Overlap and return; C4r route | finite carrier in the setup; $\Gamma_n=I$ supplied; row-stochastic $\Gamma_s$ | M:141–143 (`pIndivisible_of_identity_return_of_overlap`) |
| Reverse lemma; non-permutation witness lemma | finite bijective model, uniform prior | M:274–276, M:439–441 |
| CP-indivisibility theorem | permutation-dilation family | M:330 |
| No-uniform-finite-realization proposition | fixed finite $S$, prior, bijection | M:490 |
| C3 necessity and capacity | $m=\|\mathcal C_H\|$ of a realization | M:508–516 |
| Physical-memory theorem | coupling-step model, reference prior $\pi_H$ | M:457–475 |
| Coupling-graph cone; Bell ceiling | finite-site and arbitrary-site forms | M:362, M:414–416 |
| §4.6 theorem statement | as printed; only its Scope paragraph is edited (E14) | M:748–758 |
| Companion A1-free results | GR Appendix B (D1)–(D5); GR §3.3 operational completion on finite carriers; Theorem 24 finite identities; forward gauge algebra | C3, C5, C8, C13 |

## 5. Regression controls (§A.41 invariant → checkpoint table)

All controls are implemented in [`phase0_controls.py`](phase0_controls.py) (standard library; reads
the base with `git show`; writes a JSON record; exit status 0 iff every CTL passes, §A.44). Its
`--self-test` drives each check through a violating and a compliant edit. Run at the pin (head =
base): self-test PASS; CTL-1 … CTL-10 PASS; DR-1, DR-2, DR-2b and six DR-3 rows unmet (expected:
no edit yet). Mutation checks on the real Main (reverted afterwards): editing the Characterization
theorem's first words fails CTL-2; renaming "Step 1 (Recurrence)" fails CTL-4; appending "The
invariant law is derived from the dynamics alone. This is now settled." fails CTL-7 and CTL-8; any
Main edit without a rebuild fails CTL-9. A dry run that applied abbreviated forms of E3, E5, E6, E9
and E13 (§6) to a working copy of Main, then reverted, met DR-1 … DR-3 and passed CTL-1 … CTL-8 and
CTL-10, with CTL-9 failing until a rebuild: the decision rule is attainable by the planned edit
without touching a frozen paragraph. The same run shows the limit of the token predicates: an
abbreviated ledger that named (REV) inside item (ii) rather than item (iii) still met DR-3, so the
placement and content are the reviewer's check (§9 item 8).

| Id | Invariant asserted of Phase 1 | Checkpoint (mechanical) | When |
|---|---|---|---|
| CTL-1 | S ⇔ D ⇔ Q_fb unchanged | the paragraphs of Main opening "**Theorem (finite-horizon stochastic–reversible–unitary equivalence).**", "*(S) the finite stochastic laws;*" (which carries (D) and (Q_fb)) and "*Proof.* (S ⇒ D)" each occur once and equal the base byte for byte | every Phase 1 commit |
| CTL-2 | finite-horizon equivalence unchanged | same test for the process-dilation theorem, its extension and proof, the Characterization theorem and items (i)–(iii) | every commit |
| CTL-3 | C4r → P-indivisibility route unchanged | same test for "**Theorem (overlap and return).**" and its proof; Main still cites `pIndivisible_of_identity_return_of_overlap` | every commit |
| CTL-4 | every finite-carrier theorem unchanged as a finite-model statement | same test for Lemma 3, the one-step theorem and Step 1, the history-readback theorem and proof, the reverse lemma, the non-permutation witness lemma, the CP-indivisibility theorem, the no-uniform-finite-realization proposition, C3 necessity, the physical-memory theorem, the coupling-graph cone | every commit |
| CTL-5 | observer-relative finiteness reading unchanged | same test for the Definition and Lemma 1; Main contains "only finite visible resolution is a theorem" | every commit |
| CTL-6 | Lean census disposition unchanged | no path under `verification/lean-mathlib/`, `verification/lean/` or the registry changes; Main cites no backticked identifier absent at the base; every registry family's status equals the base; `tools/lean_manuscript_census.py` exits 0 | every commit |
| CTL-7 | no edit implies a derived probability law, typicality, physical recurrence or inflow | over sentences added to `papers/` and `book/`: a sentence matching the derivation patterns (verb … law/typicality/recurrence/return/inflow, or law … "is derived/forced/selected/…") must carry a scope or status token (finite representative, A1, a new label, hypothesis, posit, supplied, declared, conditional, open, if, given); every sentence using (NR), (IL), (ED), (IN), (RET) or (REV) carries a status token; every sentence with (IN) says "open" | every commit |
| CTL-8 | paper register (§A.32, §A.33) | sentences added to `papers/` contain no history phrase ("no longer", "is now", "formerly", …), no meta-commentary phrase, and no four-letter capitals outside a whitelist, code or math | every commit |
| CTL-9 | generated artifacts current | `tools/staleness_check.py` exits 0 | final commit |
| CTL-10 | ledger inventory unchanged | ledger paragraph keeps items (i)–(xiv) and "Fourteen items" (IDs not renumbered; §A.30) | every commit |

Not mechanized, for the reviewer: that each added proof is correct and self-contained in Main (Main
independence); that FULL mirrors each chapter edit (CENSUS §7 recipe: every chapter line occurs in
FULL); the §A.25 re-grep (§6.4).

## 6. Phase 1 edit plan (proposal, not applied)

Phase 1 edits Main and its book/FULL mirrors only. It adds two short results with inline proofs
(E5, E9), rewrites the posit's statement and pointers, and edits one Scope paragraph. It adds no
reference to an audit record, cites no new kernel identifier, and changes no theorem statement in §4.

### 6.1 Main edit units

| Unit | Site | Proposed change |
|---|---|---|
| E1 | M:36 | "Total finiteness remains an open physical posit (…)" → "Total finiteness is an open physical hypothesis, not adopted, and one sufficient condition among those each result names (…)". |
| E2 | M:44 | "and the map acts on a finite $S$ under the total-finiteness posit (§1.2 Remark, §4.5 ledger)" → "and on the finite representative of the total-finiteness hypothesis (§1.2 Remark, §4.5 ledger) the map acts on a finite $S$". |
| E3 | M:60 | "Total finiteness of that representative is a premise of the results that use it, carried as item (ii) …" → "Total finiteness of that representative is one sufficient condition for the results that use it, carried as item (ii) …; each such result names the hypotheses it consumes, and where a weaker sufficient condition is proved it is stated with the result (§2.3, §3.2)". In the use list, after "the recurrence step of §2.3": "(the later near-return (NR) of §2.3 is the alternative sufficient condition for its P-indivisibility conclusion; the exact return and its index $L$ remain statements about the finite representative)". |
| E4 | M:111 | "under the total-finiteness posit (§1.2 Remark, §4.5 ledger) the hidden sector is also finite" → "on a finite representative (§1.2 Remark, §4.5 ledger item (ii)) the hidden sector is also finite". |
| E5 | M:129, new paragraph after it | M:129: "the hidden space is finite under the total-finiteness posit (§1.2, §4.5)" → "the hidden space is finite on a finite representative (§1.2, §4.5 item (ii)); the corollary below uses neither". New paragraph: "*Corollary (near-return).* *Let $V$ be finite with $\|V\|\ge2$, $\rho$ a probability on a measurable space $H$ shared by every root, $F$ a measurable map of $V\times H$, and $\Gamma_t(a,b)=\rho\{h:\pi_V F^t(a,h)=b\}$. Suppose $\Gamma_s$ is not a permutation matrix, so that roots $a\ne b$ and a value $x$ have $m=\min(\Gamma_s(a,x),\Gamma_s(b,x))>0$, and suppose the condition (NR), posited where it is used: some $n>s$ has $(1-\Gamma_n(a,a))+(1-\Gamma_n(b,b))<m$. Then the rooted family is not P-divisible on $\{0,\ldots,n\}$.* *Proof.* $d(\Gamma_s(a),\Gamma_s(b))\le1-m$; testing $\{a\}$ gives $d(\Gamma_n(a),\Gamma_n(b))\ge\Gamma_n(a,a)-\Gamma_n(b,a)\ge1-(1-\Gamma_n(a,a))-(1-\Gamma_n(b,b))>1-m$, and a stochastic divisor would not increase total variation (Step 3). $\square$ On a finite representative Step 1 supplies the condition (NR) with $n=N$. The condition (NR) needs no finite carrier, invariant law or bijection, and it fixes neither $N$ nor $n$." |
| E6 | M:139 | Append to *Scope*: "The index-free form — a readback gap at some finite order; some $\Gamma_s$, $s\ge1$, not a permutation; the family not P-divisible on some $\{0,\ldots,n\}$ — holds without a finite representative when the condition (NR) holds after the non-permutation time: the first implication by the first half of the proof above with $\min(k,L-1)$ replaced by $k$, which uses no return; the second by the corollary (near-return); the third by the Markov argument above. The bound below $L$ and the horizon $\{0,\ldots,L\}$ are statements about the finite representative." |
| E7 | M:178 | "from a non-permutation one-step witness and finiteness alone, at the recurrence time" → "… and finiteness alone, at the recurrence time, or from the near-return condition (NR) (§2.3)". |
| E8 | M:222, M:266 | M:222: "with the total-finiteness posit (§1.2 Remark, §4.5) where a result also needs the hidden sector finite" → "with a finite representative (§1.2 Remark, §4.5 item (ii)) where a result is stated with a finite hidden sector". M:266: "$\mathcal C_H$ under the total-finiteness posit, §1.2, §4.5" → "$\mathcal C_H$ finite on the representative of §1.2 (§4.5 item (ii)) or constructed per law (§3.4)". |
| E9 | M:278 | Append: "On a measurable carrier the conclusion holds at every step under the condition (IL), posited where it is used: $\varphi$ preserves a probability $\nu\otimes\rho$ on $\mathcal C_V\times H$ with $\nu$ uniform; then $\sum_a\Gamma_t(a,b)=\|\mathcal C_V\|\,(\nu\otimes\rho)(\pi_V\circ\varphi^t=b)=\|\mathcal C_V\|\,\nu(b)=1$ by invariance, and the rows sum to one because $\rho$ is a probability." |
| E10 | M:706 | after "an open hypothesis, not adopted": ", and one sufficient condition among those stated at each use". |
| E11 | M:722 | "Recurrence-scale P-indivisibility uses finite order of the specified bijective representative and a non-permutation rooted map under a common hidden preparation (§2.3)" → "… uses finite order of the specified bijective representative, or the posited near-return condition (NR), and a non-permutation rooted map …". |
| E12 | M:724 | "a deterministic bijection on a set whose finiteness is the total-finiteness posit (§1.2 Remark, §4.5 ledger item (ii)), an open hypothesis, not adopted" → "a deterministic bijection on a set, finite under the total-finiteness hypothesis (§1.2 Remark, §4.5 ledger item (ii)), an open hypothesis, not adopted and one sufficient condition among those stated at each use". |
| E13 | M:730 | See §6.2. |
| E14 | M:764 | "The theorem uses bounded coupling, finiteness of $S$, the canonical-typicality result [31], …" → unchanged, plus one sentence only if the reviewer confirms that §4.6's operator step uses no property of the counting measure beyond normalization and invariance (§9 item 6): "The operator step alone holds with the condition (IL), posited where it is used, in place of finiteness of $S$: a normalized $\varphi$-invariant $\mu$, $P$ the $\mu$-conditional expectation onto the declared local observables and (EM) stated on $L^2(\mu)$; the canonical-typicality step is a statement about the finite representative." If not confirmed, E14 is dropped and M18/M20 stay finite-model statements (DR-3 accepts either). |

Not edited (N in §2.4): the sentence is already scoped to a finite representative, a finite model or
a finite realization, which under the framing names A1 as its sufficient condition.

### 6.2 What Main's posit ledger would say (E13)

Item (ii), from its opening to the end of its existing deep-sector clause, becomes:

> (ii) total finiteness of the bijective representative of the status Remark of §1.2 (an open
> hypothesis, not adopted), carried as one sufficient condition and not as a premise of the
> framework: each result that uses it names the hypotheses it consumes, and a weaker sufficient
> condition, where one is proved, is stated with the result — the near-return condition (NR) for the
> P-indivisibility conclusion of §2.3, the invariant-law condition (IL) for the doubly stochastic
> marginal of §3.2, and reversibility (REV), item (iii), for bijectivity — while the counting-measure
> selection of Lemma 3, the exact return and its index $L$, the orbit capacity, the CP-indivisibility
> theorem of §3.2, the physical-memory theorem of §3.4 and the canonical-typicality step of §4.6 are
> statements about finite representatives. Lemma 1 delivers finiteness of the observer's
> distinguishable states … [existing text through "(deep-sector enlargement, developed there)"
> unchanged] … consumed here by the recurrence step of §2.3 and by §4.6, whose conclusions hold on
> the finite representative … [existing transfer clause unchanged]. Without (ii), invariant laws that
> supply records from an incoming low-entropy boundary stream are not excluded; the condition on
> such supply, (IN), is open and no result here uses it;

Item (iii)'s parenthesis "(a reader who declines the recovery may instead adopt reversibility as the
standard information-conservation postulate …" gains the label: "… adopt reversibility (REV) — $\varphi$
a bimeasurable bijection of a measurable carrier, posited — as the standard …". Item (iv) gains, after
"not derived": "; on a finite representative the selected law is the counting measure, and on an
infinite site product with an injective local rule the posited entropy-density form (ED) — among
laws invariant under the rule and every lattice translation, maximal entropy per site — selects the
uniform product law" with two standard citations added to the reference list (preservation of the
uniform product measure by surjective cellular automata; uniqueness of the measure of maximal entropy
of the full shift), which the reviewer checks before E13 lands. The closing sentence "the framework's
claims are conditional on the full list" becomes "… conditional on the full list, item (ii) entering
only as one of the sufficient conditions named at each use." The item count, "Fourteen items", and
all item labels are unchanged.

### 6.3 Book and FULL mirrors (§A.14)

| Unit | Sites [FULL] | Mirror of |
|---|---|---|
| B1 | ch00:95 [320] | E1/E13: "under A1, which remains open as a physical posit" → "… open as a physical hypothesis and one sufficient condition among those the results name" |
| B2 | ch01:28 [361] | E2 |
| B3 | ch01:93–121 [426–454] | E5: the near-return corollary and its scope sentence after the P-indivisibility theorem; "the recurrence time $N$" sentence of the accessible-timescale lemma unchanged |
| B4 | ch01:177 [510] | E6/E13: "Because the physical representative is, under A1, finite and reversible, it also recurs" → "On a finite representative (A1) the representative also recurs; without A1 the near-return condition of §1.x is the stated sufficient condition" |
| B5 | ch19:212–216, 360 [5281–5285, 5429] | E13 wording for "the open hypothesis A1" where it is described as constraining the class |
| B6 | appendix-b:46 [5722] | E9 |
| B7 | appendix-c:98–116 [6252–6270] | E13: the C.6 response states A1 as one sufficient condition and lists the consumers that name a weaker one |
| B8 | glossary:11, 137 [6501, 6627] | E13: A1 entry and substratum entry |

Each chapter edit is applied to the identical FULL line, and the result re-checked with CENSUS §7's
parity recipe.

### 6.4 Propagation and rebuild

After the edit: re-grep with the §2.1 patterns and confirm that every Phase 1 site in `sites.json`
either shows its planned change or is N/K, and that no other site changed class; state the surviving
counts. Rebuild with `sh ./build.sh Main` and `sh ./build.sh --book` (papers/Main.tex, Main.pdf,
book FULL .tex/.pdf); check page count and characters per page; run `tools/staleness_check.py`
(CTL-9). Companion papers are Phase 2 and are not rebuilt in Phase 1.

## 7. Decision rule (fixed in advance)

Phase 1 succeeds if and only if, on its final head:

1. **DR-1, DR-2, DR-2b.** Main's posit ledger item (ii) states total finiteness as a sufficient
   condition ("sufficient" inside item (ii)); the ledger's closing sentence, if it keeps "conditional
   on the full list", qualifies item (ii) with "(ii)" and "sufficient"; the status Remark of §1.2
   states sufficiency.
2. **DR-3.** Every Main consumer row has an explicit sufficient condition in its section: (NR) with
   the corollary (M4) and the index-free form (M7(i)) in §2.3; the finite-representative scope of the
   index $L$ (M5, M7(ii)) in §2.3; (IL) with "doubly stochastic" in §3.2 (M3); (REV) in §4.5 (M11);
   (ED) or item (iv) with "finite representative" in §4.5 (M1, M2); (IL) or "finiteness of $S$" in
   §4.6 (M18, M20); "finiteness of $S$" and "canonical-typicality" in §4.6 (M19); (IN) with "open" in
   §4.5. The rows of §3.1 marked finite-model only satisfy DR-3 by their finite-representative scope.
3. **All controls hold.** CTL-1 … CTL-10 PASS (`phase0_controls.py` exit 0).
4. **Review.** An independent non-author review confirms the semantics the predicates cannot check
   (§9) and Main's independence of the added proofs.

Any failure means Phase 1 does not land as preregistered. Failure is recorded; the predicates and
token lists are not adjusted after Phase 1's text exists.

## 8. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1055 comments 7030993647 and 7030887534 | authorization and scope | provenance; quoted with author and time |
| #1421 and #1431 review comments (F3) | review status of REMAINDER and R1-INF | provenance; the results used are on `main` in those records |
| commit `a8119d20` (F1) | finding F1 | support on `main` (an ancestor of the pin) |
| #1055, #1334, #1169, #866 | accountability; O-INFLOW | provenance |

## 9. What an independent reviewer must check

1. A sample of `sites.json` against the files at the pin, including every Main row of §2.4, and that
   each site's row key is the row whose claim it states (no reclassification).
2. Findings F1–F6 against their evidence.
3. F2: that ladder F11 needs only row-stochastic rooted laws from one normalized shared prior, so
   the M4 target in §3.1 is not weaker than its source.
4. Each "weaker" mark and its separating example; each "equivalent" mark (M1 counting form, C1
   counting form, C12).
5. The proofs proposed for Main in E5, E6 and E9: correct, self-contained, and using no downstream
   result; E6's three directions checked one at a time (§A.34).
6. Whether §4.6's operator step uses only normalization and invariance of the counting measure; this
   decides whether E14 is included.
7. The two standard citations proposed for (ED) in E13.
8. That `phase0_controls.py` fixes the controls of §5 as stated, that its self-test and the baseline
   run reproduce, and that the predicates cannot be met by an edit that only adds the tokens without
   the content (the semantic part of this is the reviewer's, not the script's).
9. That nothing here adopts a premise, edits a manuscript or presents (NR), (IL), (ED), (REV) or (IN)
   as more than a stated condition.
