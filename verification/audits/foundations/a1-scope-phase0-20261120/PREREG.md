# A1-SCOPE Phase 0 — site map, target statements, controls and decision rule

**Status.** This is the writer's paper-only preregistration. It was revised after the independent
non-author review of `7e679831`
([#1442 comment 7031480016](https://github.com/amaybaum/incompleteness/pull/1442#issuecomment-7031480016),
REVISE), and a fresh review of the revised head is required.

- **Not done here:** no manuscript edit, no Lean, no new premise, no proof beyond the elementary
  checks named in §3 and §6, and no merge request.
- **Status of A1 and sourcing:** A1 (Main posit ledger item (ii)) remains open and unadopted.
  Physical measurement sourcing remains not passed.
- **Phase 1 is not authorized.** This record fixes what Phase 1 may change and how the change is
  checked. Phase 1 needs a separate manuscript-edit decision.

**Authorization.** Owner `amaybaum`,
[#1055 comment 7030993647](https://github.com/amaybaum/incompleteness/issues/1055#issuecomment-7030993647),
2026-11-20T05:06:11Z, "Owner decision: A1-SCOPE framing, O-A4 and Phase 0". Three of its decisions
bear on this record:

- **Decision 3** authorizes this phase: "Phase 0: authorized now. It is the complete corpus-wide
  census and preregistration of A1, finite-carrier and posit-(ii) dependencies."
- **Decision 1** fixes the framing: "A1 or the explicitly stated sufficient conditions … H-μ must
  supply the *specific* measure properties each theorem uses".
- **Decision 2** assigns the finite-periodic-lattice question to O-A4 (#1441). This record does not
  do O-A4's work.

The scope is the proposal at
[#1055 comment 7030887534](https://github.com/amaybaum/incompleteness/issues/1055#issuecomment-7030887534)
(2026-11-20T04:59:16Z).

**Scope correction.** The coordinating session relayed an owner question: the existing audits are
authoritative inputs, their rows and classifications are cited rather than re-derived, and Phase 0
supplies only the delta they lack. Accordingly:

- No row of A1-REMAINDER, A1-FCLASS, A1-MAIN-ROOTS, A1-NECESSITY or the A1-09 census is reclassified.
- The class of a site is that of the existing row it is keyed to (§2.2).
- Disagreements between audits are recorded as findings (§1.2).

**Goal link (§A.47).**

- **Item served:** #1055, the A1 programme, which serves #1169.
- **What the work decides:** before any edit, exactly which manuscript sentences carry total
  finiteness and which weaker or alternative condition each consumer can state.
- **What it fixes:** the exact text and the mechanical tests that a Phase 1 edit must pass.
- **The aim:** Main stops requiring a finite universe without importing an equally unsupported
  premise and without implying a derived law.

**Source pin.** `main` at `d5735bedb3958394e3e095a4513d9fb5996d079d`.

- **Line notation:** `M:n` is line `n` of `papers/Main.md` at the pin. Other files are named by
  basename.
- **Unchanged since:** the reviewer confirmed that nothing under `papers/` or `book/` changed between
  the pin and `main` at `d6aa6361`.
- **Agreement with the REMAINDER pin:** Main's line numbers at the pin agree with the REMAINDER pin
  `21e16c61` for every cited line. The only Main change between the two pins edits line 540 in
  place.

## 1. Inputs and findings

### 1.1 Inputs (all on `main` at the pin)

| Short name | Path under `verification/` | Used for |
|---|---|---|
| REMAINDER | `audits/foundations/a1-remainder-20261119/REMAINDER.md` | consumer rows M1–M21, C1–C14; residues R1–R6; repairs; hypotheses H-* (§3) |
| FCLASS | `audits/foundations/a1-finiteness-classes-20261117/CLASSIFICATION.md` | F1–F4; rows 01–27, U1–U2 |
| ROOTS | `audits/foundations/a1-main-roots-20261118/AUDIT.md` | Main roots R0–R8 |
| NEC | `audits/foundations/a1-necessity-20261117/ASSESSMENT.md` | five-family table |
| CENSUS | `audits/foundations/a1-09-dependency-census/CENSUS.md` | §7, §17, §18, §23.2 |
| LADDER | `audits/foundations/a1-10-recurrence-premises/PREMISE-LADDER.md` | F11, §3.4 |
| REC-1 | `audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md` | (V)(M)(I)(P)(RET)(RIG)(FS); Props 3.4, 3.6′, 5.1, 6.1, 6.2; U1–U16 |
| RIGID | `audits/foundations/a1-rigid-visible-recurrence-20261119/A1-RIGID-1.md`; `lean-mathlib/OIBridge/ObservableRigidity.lean` | compact-orbit theorem; rotation × Bernoulli |
| R1-INF | `audits/foundations/r1-inf-20261119/RESULT.md` | P-ED (Prop. 3); Lemma 8; Prop. 9; §6–§7 |
| P8 (A1-05) | `audits/foundations/a1-05-p8-observer-selection/SOURCE-MATRIX.md` | P8-M |
| P7B | `audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` | H1–H14 |
| PREP | `programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md` | 1.5(d) (companion and programme scope only; see §3.1 "Inflow") |
| Registry | `lean-manuscript-census.json` | family dispositions |

### 1.2 Findings on the inputs (recorded, not resolved here)

| Id | Finding | Evidence at the pin | Consequence |
|---|---|---|---|
| F1 | REMAINDER row M14 places "t ≪ t_R" at M:540. Line 540 contains no `t_R` at REMAINDER's own pin `21e16c61`: MAIN-TR-1 (`a8119d20`), an ancestor of that pin, removed it. | `t_R` occurs only at M:155, :449, :453 and :644 | Live `t_R` sites are keyed to REC-1 U4, U11 and M10 |
| F2 | REMAINDER M4 attaches "a bimeasurable bijection T preserving a normalized μ and positive cell masses" to ladder F11. LADDER §3.4 and NEC state F11 for row-stochastic rooted laws only. | LADDER lines 93–105; NEC §2 row 1 | The M4 target under (NR) needs only one normalized shared prior and a measurable update (review: holds) |
| F3 | The Status headers of REMAINDER and R1-INF still ask for a delta review, but their PRs record confirmed delta reviews: #1421 at 2026-11-19T21:37:05Z and #1431 at 2026-11-19T23:44:30Z. | the headers; the PR comments | Main carries its own proof of everything it uses (§6) |
| F4 | REMAINDER M3 lists L3 as unproved. R1-INF Lemma 8 proves it for any measurable `V × H` and any invariant `ν ⊗ ρ` with uniform `ν`. | R1-INF lines 268–279 | E9 carries the one-line proof |
| F5 | The header of `OIBridge/Finiteness.lean` quotes a Lemma 1 text that differs from M:46. | `Finiteness.lean` lines 1–8 | Outside A1 (it concerns visible finiteness); recorded for the owner |
| F6 | There are two false positives: appendix-b:235 and :246, where "(A1)" labels an anomaly equation. An earlier unanchored pattern also matched "definite substratum" in four places; the anchored patterns exclude those. | §2.1 | Recorded so the counts reproduce |
| F7 | Review finding for O-A4: SM:539's bipartite claim fails on odd tori. | review 7031480016 | Keyed to O-A4 (#1441); not addressed here |

## 2. Site map (delta 1)

### 2.1 Method

Every line of `papers/*.md` and `book/*.md` was scanned with Python `re` for two pattern sets. The
book scan covers the chapters, appendices a/b/c, glossary, preface, README and FULL. A matching line
is one site. Each site carries:

- the quote of the sentence that contains its first match;
- the existing row or rows it is keyed to;
- its class and its phase;
- an `action`: `E*` and `B*` are units of the Phase 1 edit ledger; `N` means Phase 1 scope with no
  edit; `K` means preserved; `P2`, `OA4` and `FP` mean Phase 2, the O-A4 unit and false positive.

FULL sites carry `mirror_of`, which points to the chapter line they copy.

Lexical sites are supplemented by **structural** sites. These are the REMAINDER locators, in Main
and the companions, that use finiteness without a listed word, plus O-A4's SM:240 and SM:539. The
map is [`sites.json`](sites.json) (schema `a1-scope-phase0 site map v1`). It stores every pattern
verbatim.

Core set:

| Id | Target | Pattern (abridged; exact in `sites.json`) |
|---|---|---|
| P1 | A1 | `\bA1\b` |
| P2 | total finiteness | `[Tt]otal[- ]finiteness`, `totally finite`, `finite total (system\|configuration\|state)` |
| P3 | "finite S" | `finite $S$`, `$S$ finite`, `$S$ is finite`, `$S$ is a finite`, `$S$ be finite`, `finite set $S$`, `\|S\|`, `\lvert S\rvert` |
| P4 | finite configuration space | `finite configuration space`, `finitely many configurations`, `finite (state\|configuration\|phase) space` |
| P5 | posit (ii) | `posit (ii)`, `ledger item (ii)`, `item (ii) of the posit`, `ledger (ii)` |
| P6 | uniform or counting measure | `counting measure`, `counting probability`, `uniform (hidden )?prior`, `uniform … on S / configuration / \mathcal{C}`, `maximal-entropy invariant` |
| P7 | recurrence time | `t_R`, `t_{R}`, `t_{\rm R}`, `Poincaré recurrence`, `recurrence time` |
| P8 | finite universe | `finite universe`, `universe is finite`, `finite (substratum\|bijection\|reversible substratum\|representative)` |

Every "finite" pattern is anchored with `(?<![A-Za-z])`, so "infinite" and "definite" do not match.

The paraphrase set covers:

- `periodic lattice`;
- `eventual image` and the injective/surjective step;
- recurrence-scale, recurrence-cycle, exact return, `\Gamma_L = I`, orbit of period and `\log_2 p`;
- canonical typicality;
- maximal-entropy measure or selection;
- finite hidden space, finite carrier, finitely many states, finite cardinality and finite information;
- uniform measure, uniform counting and uniform law(s);
- finite bijective;
- finiteness of `S`, and `\mathcal{C}_H` finite;
- total carrier, finite recurrence, and bijection, permutation or map on (or of) a finite set.

FULL lines were matched to chapter lines by exact equality (CENSUS §7). The extended P3 and the
paraphrase additions were added after review. They catch every site the review named (SM:44,
Substratum:52, SM:210, SM:242, ch18:174, Substratum:288, ch02:158) and further sites (28 new lexical sites in all, FULL mirrors included).

### 2.2 Coverage, keying and limits

**Covered.**
- All 12 papers and all 30 book Markdown files at the pin.
- Lean header and docstring text containing A1 or posit-(ii) wording (§2.6).
- Structural sites from REMAINDER's locators for Main and for C1–C14.
- All 143 FULL sites, each byte-identical to a chapter line.

**Keying rule.**
- A site is keyed to the existing row whose claim it states, restates or mirrors.
- Its class is DECL when the sentence states or points to posit (ii) itself, whatever its other
  rows. Otherwise its class is that of its first row.
- No new row is created.

**Not covered.**
- `.tex`/PDF (generated from stamped sources; `tools/staleness_check.py` reports 13 matched).
- Lean proof bodies.
- Registry notes and other verification records.
- The claim chains of FCLASS U1/U2.
- Implicit uses phrased without any listed word and without a REMAINDER locator.

A1-C01 remains incomplete. This map does not certify the absence of other consumers.

### 2.3 Counts

There are 566 sites: 384 core, 143 paraphrase-only and 39 structural. Of these, 423 lie outside
FULL and 143 inside it.

Class legend:

| Class | Meaning |
|---|---|
| DECL | states or points to posit (ii) |
| R1–R6 | A1-REMAINDER residues |
| B | A1-REMAINDER class (b): A1-free under a named hypothesis |
| INFLOW | finiteness excludes PREP 1.5(d)'s incoming stream |
| FREE | A1-free already, or an explicit finite-model statement already labelled |
| FP | false positive |

| File | DECL | R1 | R2 | R3 | R4 | R5 | R6 | B | INFLOW | FREE | FP | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `papers/Main.md` | 10 | 6 | 11 | 0 | 0 | 2 | 4 | 19 | 0 | 34 | 0 | 86 |
| `papers/GR.md` | 3 | 7 | 2 | 0 | 0 | 0 | 2 | 11 | 0 | 17 | 0 | 42 |
| `papers/Substratum.md` | 3 | 0 | 0 | 1 | 18 | 0 | 4 | 3 | 1 | 14 | 0 | 44 |
| `papers/SM.md` | 1 | 8 | 0 | 0 | 11 | 0 | 0 | 6 | 0 | 1 | 0 | 27 |
| `papers/Structure.md` | 0 | 0 | 0 | 0 | 1 | 0 | 41 | 9 | 0 | 3 | 0 | 54 |
| `papers/Methodology.md` | 3 | 0 | 0 | 3 | 0 | 0 | 5 | 2 | 0 | 2 | 0 | 15 |
| `papers/Computation.md` | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 5 |
| `papers/Complexity.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 |
| `papers/Introduction.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 4 |
| `papers/Medicine.md` | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| `book/ch00-introduction.md` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 |
| `book/ch01-observation.md` | 2 | 3 | 1 | 1 | 0 | 0 | 0 | 6 | 0 | 2 | 0 | 15 |
| `book/ch02-substratum.md` | 4 | 0 | 1 | 1 | 6 | 0 | 4 | 1 | 0 | 2 | 0 | 19 |
| `book/ch03-structural-realism.md` | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 0 | 2 | 0 | 10 |
| `book/ch04-methodology.md` | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 2 | 0 | 5 |
| `book/ch05-gauge-structure.md` | 1 | 0 | 0 | 0 | 7 | 0 | 0 | 1 | 0 | 0 | 0 | 9 |
| `book/ch07-gravity.md` | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| `book/ch09-universality.md` | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 3 | 0 | 9 |
| `book/ch11-origin-of-life.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| `book/ch14-quantum-computing.md` | 3 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 5 |
| `book/ch18-beyond.md` | 4 | 1 | 17 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 23 |
| `book/ch19-open-problems.md` | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| `book/appendix-b-derivations.md` | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 5 | 0 | 6 | 2 | 17 |
| `book/appendix-c-objections.md` | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| `book/glossary.md` | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 2 | 0 | 7 |
| `book/preface.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 2 |
| `book/…-FULL.md` (mirrors) | 35 | 9 | 21 | 2 | 16 | 0 | 13 | 21 | 1 | 23 | 2 | 143 |
| **Total** | 91 | 40 | 56 | 8 | 62 | 2 | 84 | 94 | 4 | 121 | 4 | 566 |

Actions:

| Action | Outside FULL | In FULL |
|---|---|---|
| Phase 1 edit | 19 | 7 |
| Phase 1, no edit (N) | 58 | 31 |
| Preserved (K) | 127 | 29 |
| Phase 2 | 171 | 58 |
| O-A4 | 46 | 16 |
| False positive | 2 | 2 |

Main has 86 sites: 12 edited, 27 N and 47 K.

### 2.4 Main, sentence level

Quotes are the opening of the sentence containing the first match; `sites.json` holds the full
sentence. Structural sites (marked s) carry no lexical match.

| Site | Quote | Rows | Class | Action |
|---|---|---|---|---|
| M:18 | "On a fixed finite reversible representative … at some order $k$ below the recurrence time …" | M7 | R2 | N |
| M:36 | "Total finiteness remains an open physical posit (status Remark, §1.2 and ledger §4.5, item (ii))." | REM-s3 | DECL | E1 |
| M:44 | "… and the map acts on a finite $S$ under the total-finiteness posit (§1.2 Remark, §4.5 ledger) …" | REM-s3 | DECL | E2 |
| M:54 | Lemma 3: "… the counting measure is selected among invariant measures as the maximal-entropy one …" | M1, M11 | R1 | K |
| M:58 | "… the counting probability on the eventual image … belongs to a different representative choice …" | M1, M3 | R1 | N |
| M:60 | "Total finiteness of that representative is a premise of the results that use it, carried as item (ii) …" | REM-s3, M1, M2, M3, M11, M13, M21 | DECL | E3 |
| M:72 | "One-way influence can suffice for recurrence-cycle indivisibility …" | M4 | B | N |
| M:76, 616, 620, 622 | exhaustive probes at stated $(n_V,\|\mathcal C_H\|)$ | CEN17 Main 508/608 | FREE | K |
| M:80 | "… indivisibility somewhere in the recurrence cycle of a fixed finite reversible representative …" | M7 | R2 | N |
| M:111 | "… under the total-finiteness posit (§1.2 Remark, §4.5 ledger) the hidden sector is also finite …" | REM-s3 | DECL | N |
| M:113, 121 s | one-step theorem; "Step 1 (Recurrence). $\varphi$ bijective on a finite set ⇒ …" | M4 | B | K |
| M:129 | "… the hidden space is finite under the total-finiteness posit (§1.2, §4.5)." | M4 | B | E5 (insertion after) |
| M:135, 137 | history-readback theorem "of order $L$" and its proof | M5 | R2 | K |
| M:139 | "Under a full-support prior, the gap it is equivalent to may lie at any order below the recurrence time …" | M7 | R2 | E6 |
| M:141, 143 s | overlap and return, and its proof | M6 | FREE | K |
| M:145 s | routed readback "for some n" | M8 | B | N |
| M:147, 151 s | genericity count over bijections of a finite set | M13 | R2 | N |
| M:155 | "If the flow then returns near-totally at a common time — some $t_R>t_1$ …" | REC-1 U4 | FREE | K |
| M:163 s | fast bath erases readback (uniform erosion) | M20 | B | K |
| M:178 | "… P-indivisibility from a non-permutation one-step witness and finiteness alone, at the recurrence time …" | M4 | B | E7 |
| M:180 | "… from a non-permutation rooted map and finite order alone …" | M4 | B | N |
| M:208 | "Marginalizing a bijection under the uniform hidden prior yields a doubly stochastic one-step matrix …" | M3 | R1 | N |
| M:214, 437, 484, 528, 540, 660 | finite visible configuration spaces; constructed finite sets | CEN17 Main 484/550 | FREE | K |
| M:216, 352, 558, 566, 588, 604, 648, 658, 778, 780 | "on a finite carrier with complex matrix kinematics taken as given …" | FCLASS 26, C5 | FREE | K |
| M:222 | "… with the total-finiteness posit (§1.2 Remark, §4.5) where a result also needs the hidden sector finite." | REM-s3 | DECL | N |
| M:266 | "**Setup.** … $\mathcal C_H$ under the total-finiteness posit, §1.2, §4.5 …" | M12, REM-s3 | DECL | N |
| M:274, 276 | reverse lemma and proof (uniform prior) | M3 | R1 | K |
| M:278 | "*Remark.* This is the correspondence for a single step with a uniform hidden prior …" | M3 | R1 | E9 |
| M:324, 356, 486, 490, 534, 696 | statements about a displayed or every fixed finite realization | CEN17 Main 298/484/534 | FREE | K |
| M:330, 334 s | CP-indivisibility, framework scope | M9 | R6 | K |
| M:338 | "… which on one fixed finite reversible representative is what the recurrence-scale theorem delivers …" | M4 | B | N |
| M:362, 414, 416 s | causal cone; Bell ceiling | M17 | FREE | K |
| M:439, 441 | non-permutation witness lemma for the finite bijective model | M4, REC-1 U6 | B | K |
| M:449, 453 | "For a finite reversible realization … Poincaré recurrence at $t_R$ …"; "$t\ll t_R$" | REC-1 U11, M16 | R2 | N |
| M:457, 471 s | physical-memory theorem; "the uniform hidden prior of the model above" | M16 | R6 | N / K |
| M:508, 516 s | C3 necessity; per-process capacity | M15 | FREE | K |
| M:592 | "… the concrete OI substratum, in its finite model (ledger item (ii)) …" | C5, REM-s3 | DECL | N |
| M:632 | "… on finite representatives at the recurrence scale …" | M4 | B | N |
| M:644 | "*Remark (consolidation).* … a bijection on a finite set has finite order $L$ … windows $t\ll t_R$ …" | M10 | R2 | N |
| M:662 | "… canonical typicality [31], which the structural observer-selection theorem of §4.6 uses." | M19 | R5 | N |
| M:706 | "Finiteness of the hidden sector is … item (ii) of the posit ledger (§4.5), an open hypothesis, not adopted …" | REM-s3 | DECL | E10 |
| M:722 | "Recurrence-scale P-indivisibility uses finite order of the specified bijective representative …" | M4 | B | E11 |
| M:724 | "**Falsifiability.** … a deterministic bijection on a set whose finiteness is the total-finiteness posit …" | REM-s3 | DECL | E12 |
| M:730 | posit ledger items (ii), (iii) and its closing sentence | REM-s3, M11, M1, M2, C14 | DECL | E13 |
| M:739 | status ledger: "… at the recurrence time $L$" | M7 | R2 | N |
| M:748, 750 s, 756, 758, 760 s | §4.6 setting, Setup ("exact recurrence"), theorem, corollary | M18, M20 | B | N |
| M:762 | "For $(S,\varphi)$ in its equilibrium macrostate, canonical typicality [31] implies …" | M19 | R5 | N |
| M:764 | "**Scope.** The theorem uses bounded coupling, finiteness of $S$, the canonical-typicality result [31] …" | M18, M20 | B | E14 |

### 2.5 Book Phase 1 sites, companions and Lean

Phase 1 book sites (FULL line in brackets; each `B*` unit is applied to the chapter and to FULL):

| Site [FULL] | Rows | Class | Action |
|---|---|---|---|
| ch00:95 [320] | REM-s3, C6 | DECL | B1 |
| ch01:28 [361] | REM-s3 | DECL | B2 (mirror of E2) |
| ch01:38, 81, 85 [371, 414, 418] | M1 | R1 | N |
| ch01:41 [374] | M11 | R3 | N |
| ch01:93, 95, 97, 121 [426, 428, 430, 454] | M4 | B | N |
| ch01:111 [444], appendix-b:417 [6093] | M4, M5 | B | K (mirrors of frozen proofs) |
| ch01:119 [452] | M4 | B | B3 (corollary inserted after; mirror of E5) |
| ch01:161 [494], ch19:126 [5195] | REM-s3, C5 | DECL | N |
| ch01:177 [510] | M10 | R2 | B4 |
| ch19:212, 214, 216, 360 [5281, 5283, 5285, 5429] | REM-s3 | DECL | N |
| appendix-b:42, 44 [5718, 5720] | M3 | R1 | K |
| appendix-b:46 [5722] | M3 | R1 | B6 (mirror of E9) |
| appendix-b:419, 453, 456 [6095, 6129, 6132] | M5, M4, M7 | R2/B | N |
| appendix-c:16, 96–116, 136 [6170, 6250–6270, 6290] | REM-s3 | DECL | B7 at :104; N elsewhere |
| glossary:11 [6501] | REM-s3 | DECL | B8 |
| glossary:105, 117, 137 [6595, 6607, 6627] | M4, M7, REM-s3 | B/R2/DECL | N |
| preface:3 [62] | M4 | B | N |

Companion and remaining book sites, by row. The site lists are in `sites.json`; "K" means preserved.

| Phase | Class | Rows | Sites |
|---|---|---|---|
| P2 | R1 | C1, C2, C4 | GR:58, 88, 112 s, 122 s, 124, 126 s, 128 s; ch07:42 |
| P2 | R1 | M1 consumers | Computation:122; ch14:272; ch18:36; SM:292, 334, 336, 1225, 1227 |
| P2 | R1 | R1-INF §6 note | SM:803, 809, 811 |
| P2 | R2 | M5/M7/M13 restatements | ch02:32; ch18:20, 162–192; Medicine:25 |
| P2 | R2 | REC-1 U15 | GR:589, 591 |
| P2 | R3 | M11 | Substratum:94; ch02:78; Methodology:106, 146, 148 |
| P2 | R6 | C11 | Structure (41 sites); ch03:34, 44; ch09:18–193; Methodology:339–369 |
| P2 | R6 | C8, C9, C12, GR App. A | Substratum:44, 52, 262, 268; ch02:14–18, 144; Computation:178, 182; ch14:262; GR:609, 719 |
| P2 | B | M4, C3, C10 | SM:24, 44, 112, 236, 252, 308; Structure:718, 1116–1189; Substratum:137, 401, 407; GR:138; Introduction:12, 93; Methodology:283, 441; ch02:192; ch03:36, 58, 102, 114, 240; ch04:36; ch05:95 |
| P2 | DECL | C5, C6, C9, C12, REM-s3 | GR:20, 257, 261; SM:22; Substratum:92, 288, 389; Computation:120; Methodology:156, 158, 517; ch02:76, 136, 158, 212; ch03:84; ch05:23; ch07:118; ch14:160, 164, 184; ch18:242, 244, 260, 288 |
| P2 | INFLOW | C10 | Substratum:56; Complexity:212; ch18:40 |
| OA4 | R4 | C6, C7, CEN17 SM 210/224–278/641 | Substratum:98, 104, 121 s–133, 157, 189 s–195 s, 193, 205–233; SM:20, 158, 202, 210, 222, 232, 240 s, 242, 316, 539 s, 641; Structure:768; ch02:82–122; ch04:10, 26; ch05:19, 25, 65–89; glossary:13 |
| K | FREE / B | C3, C5, C8, M21, CEN17/18 rows | GR:132 s, 134, 136 s, 174, 190–328, 673, 817, 871–905; Substratum:14, 247 s–272 s, 344, 348, 359, 373, 459, 465, 533; SM:1648; Structure:1096, 1233, 1251; Computation:144; Complexity:292; Introduction:34, 129; Methodology:409, 529; book mirrors |

Lean header and docstring sites with A1 wording. No phase of A1-SCOPE edits Lean, and registry
dispositions are given at the pin:

| Module (disposition) | Lines | Content | Row |
|---|---|---|---|
| `CanonicalMeasure` (current) | 1–40 | quotes Lemma 3; "the lemma's formal obligation is entirely finite" | M1; stays true while Lemma 3 is frozen (CTL-4) |
| `Finiteness` (current) | 1–30 | quotes a Lemma 1 text differing from M:46 | F5 |
| `SubstratumInterfaceAudit` (kernel-only) | 7–16, 83–84, 108–109, 184–185, 769, 785–786 | `A1 : Prop := Finite 𝒮.Conf`; `a1_of_finite` | C6/C7 (O-A4) |
| `ManuscriptAxioms` (kernel-only) | 4–97 | realized-core images of A1, A2 | C6 |
| `ObservableRigidity` (kernel-only) | 8–16 | A1-RIGID-1 theorem | M4 |
| `SubstratumSource` (current) | 48 | "does not derive a quantum architecture from A1-A6" | C5 |
| `HexLatticeGas`, `A6Instantiation`, `HydroSourceAudit`, `FrozenSourcing`, `RouteB`, `RecursiveFiniteFactor` (kernel-only) | as grepped | A1 for specific finite models | C6 / FREE |

## 3. Per-consumer target statements (delta 2)

**Marks.** Each replacement carries one of four marks:

| Mark | Meaning |
|---|---|
| **equivalent** | Any hypothesis that makes the statement true as stated is equivalent to A1 for it. |
| **weaker** | Implied by A1 (with the structure the finite theorem already uses) and strictly weaker; the separating example is named. |
| **alternative (incomparable)** | A sufficient condition that A1 does not imply and that does not imply A1. |
| **finite-model only** | No traced replacement; the statement is kept as a statement about finite representatives. |

**Labels proposed for Main.**

| Label | Condition |
|---|---|
| (NR) | later common near-return |
| (IP) | invariant product law with uniform visible marginal |
| (IL) | normalized invariant law, for §4.6 |
| (FS) | full-support visible prior |
| (REV) | reversibility |

- **Status:** each is "assumed as a hypothesis of that result and not adopted".
- **Collisions:** `grep -F` at the pin finds none of these labels in papers or book.
- **Not in Main:** (ED) and the inflow condition do not enter Main (§3.1).

### 3.1 Main consumers

| Row | Under A1 | Sufficient condition stated in Phase 1 | Measure properties used | Mark | Source |
|---|---|---|---|---|---|
| M1 Lemma 3 selection | counting probability on the finite representative | finite representative (unchanged). Not carried into Main: (ED), the entropy-density selection on $A^{\mathbb Z^d}$ under rule and translation invariance | (ED): normalization; rule invariance; translation invariance; entropy density | counting form: **equivalent**. (ED): **alternative (incomparable)**. A1 does not give a full $A^{\mathbb Z^d}$ with translations, and R1-INF says P-ED "relocates the uniform posit rather than deriving it" | R1-INF Prop. 3, §7 |
| M2 μ-G, μ-O, μ-R, posit (iv) | uniform on carrier / orbit / record-compatible union | finite representative (unchanged) | PREP 1.1–1.3 use normalization and invariance only | μ-O and the static budgets: **finite-model only** (L2). μ-G, μ-R under (ED): **alternative (incomparable)**, not carried | REMAINDER M2; R1-INF Prop. 7 |
| M3 baseline matrices | $T_{ij}$ counts a finite hidden set | already allowed at M:135, M:141: rooted maps of one normalized prior shared by roots | normalization of $\rho$ | **weaker**; separating: the RIGID example | REMAINDER M3 |
| M3 doubly stochastic corner | uniform prior on finite $\mathcal C_V\times\mathcal C_H$ | (IP): $\varphi$ preserves $\nu\otimes\rho$ with $\nu$ uniform (E9) | normalization; invariance; product $\nu\otimes\rho$; uniform $\nu$. No ergodicity, no uniform $\rho$ | **weaker**. Separating: the RIGID rotation × Bernoulli pulls back to $\mathrm{Unif}\otimes\rho$ (review: holds). Countercontrol: $\mathrm{Unif}(V)\otimes\delta_0$ | R1-INF Lemma 8 |
| M4 one-step theorem | $\Gamma_N=I$ (M:121) | (NR) for an overlapping pair $a\ne b$ at the non-permutation time $s$: some $n>s$ with $(1-\Gamma_n(a,a))+(1-\Gamma_n(b,b))<m$ (E5) | normalization of the shared prior; measurable update. A1 with bijectivity supplies (NR) at every multiple of $N$ exceeding $s$. (RIG) supplies it under (V)(M)(I)(P); RIGID compactness supplies it as well | **weaker**. Separating: RIGID rotation × Bernoulli ($s=1$, $n=4$, review); REC-1 golden rotation. Lost: the specific $N$ | LADDER §3.4 (F2) |
| M5 readback + recurrence | order $L$ | first half (non-permutation $\Gamma_s$, $s\le k$) without return | measurable $F$; normalized shared $\rho$; roots independent of $\rho$ | first half: **weaker**. $s\le L-1$ and the endpoint $\{0,\ldots,L\}$: **finite-model only** in Phase 1 ((RET) not carried) | REC-1 Props 6.1, 3.6′ |
| M6 overlap and return | — | — | — | preserved | |
| M7(i) index-free equivalence | finite order | E6, one direction at a time: (a)⇒(b) Prop. 6.1; (b)⇒(c) by the corollary under (NR) for an overlapping pair at the $s$ found; (c)⇒(a) by the direct divisor $\Gamma_t=\Gamma_s(Q_s\cdots Q_{t-1})$ of the Markov law, using (FS) | (FS) full-support visible prior independent of $\rho$; normalized $\rho$; (NR) | **weaker**; separating: RIGID rotation × Bernoulli | REC-1 Prop. 6.2 |
| M7(ii) L-indexed form | exact return at $L$ | none in Main | — | **finite-model only** | REC-1 U2 |
| M8 routed readback "for some n" | `rootedMap_periodic` | storage-time overlap, then (NR) (the corollary covers it; no edit) | as M4; the write clause needs an atom or a positive-measure seed set | "for some n": **weaker**. Write/store/read: **finite-model only** | REC-1 U14 |
| M9 CP-indivisibility | finite $H$ | none (L6) | — | **finite-model only** | |
| M10 all-time classification | finite order | theorem unchanged; no A1-free physical reading | — | theorem preserved; reading **finite-model only** | |
| M11 bijectivity | eventual image; injective ⇒ surjective on a finite set | (REV): $\varphi$ a bimeasurable bijection of a measurable carrier (label added to the alternative already printed in item (iii)); prong 1 under (IP) | prong 1 as the M3 corner | (REV): **alternative (incomparable)**. A1 does not give bijectivity without the eventual-image restriction, and (REV) assumes the conclusion the A1 route recovers. Eventual-image prong: **finite-model only** | REMAINDER M11 |
| M12, M15, M17 | — | — | — | preserved | |
| M13 orbit capacity, $P_{\rm perm}$ | finite orbit and count | none | — | **finite-model only** | |
| M14 `t_R` | see F1 | none; the accessibility scale is stated apart from recurrence (REC-1 U11) | — | M:155 preserved; M:449, 453, 644 **finite-model only** (already scoped) | F1 |
| M16 physical memory | uniform-prior finite model | none (L7) | reference prior $\pi_H$ | **finite-model only** | |
| M18 §4.6 decay estimate | counting inner product; finite $S$ | (IL), narrowed (E14): normalized $\varphi$-invariant $\mu$; $P$ the $\mu$-conditional expectation onto the declared local observables of a finite readout support with a locally finite dependence cone; (EM) on $\mu$-centred $L^2(\mu)$ | normalization; invariance (so $U$ is an isometry); $L^2(\mu)$; $P$; (EM). No product form, uniformity or separate ergodicity | decay estimate: **weaker**; separating: the Bernoulli shift. The $O(\varepsilon)$ corrections, the canonical-typicality clause and the Setup's exact recurrence: **finite-model only** | P8 P8-M; review |
| M19 typicality | finite-dimensional shell | none (L8) | — | **finite-model only** | |
| M20 anti-Boltzmann-brain | inherits M18 | inherits E14 at the decay step | as M18 | decay step **weaker**; the rest are A1-independent gaps | |
| M21 deep sector | finite decoupled factor | none in Main. GR Appendix B's (D1)–(D5) is a companion result, and Main does not cite it | (D5): $u_{B_n}\otimes\nu$ | finite windows: **weaker** (companion). All-time: **finite-model only** | REMAINDER M21 |
| Inflow | A1 excludes PREP 1.5(d)'s inflow law | **none in Main**. PREP 1.5(d) is a downstream programme record, and no Main result uses an inflow condition (Main-independence rule). Main contains no inflow site (§2.5). The obligation stays O-INFLOW (#866 under #1169) and the companion INFLOW sites (Phase 2) | — | — | REMAINDER §5 |

### 3.2 Companion consumers (Phase 2; listed so that Phase 1 contradicts none of them)

| Row | Sufficient condition | Measure properties | Mark |
|---|---|---|---|
| C1 H-count | decoupled: P7B H1–H14 | H4: normalized shell counting ⊗ one deep law $\nu$; decoupled dynamics | counting form: **equivalent**; P7B: **weaker**; coupled case: **finite-model only** |
| C2 | inherits C1 | as C1 | as C1 |
| C3 | GR Appendix B (D1)–(D5) | as M21 | preserved |
| C4 H-BD | none (L10) | — | **finite-model only** |
| C5, C13 | — | — | preserved |
| C6, C7 | O-A4 | — | **finite-model only** until O-A4 reports |
| C8 | finite identities; windows as C3; infinite L9 | as M21 | identities preserved; infinite transfer **finite-model only** |
| C9, C11, C14 | none | — | **finite-model only** |
| C12 | counts $\|S\|$ | — | **equivalent** |
| C10 | inherits M18–M20 | as M18 | as M18. Each INFLOW site must name the inflow question as open, with its own support |

## 4. Preserved statements (must not change)

| Statement | Exact assumptions as printed | Where |
|---|---|---|
| Definition; Lemma 1 (observer-relative finiteness) | finite-capacity clause ⇒ $\mathcal C_V$ finite; "only finite visible resolution is a theorem" | M:42, M:46, M:60 |
| Lemma 3 statement | bijective representative; uniform invariant law on each finite cycle; counting measure selected as maximal-entropy | M:54 (`CanonicalMeasure`) |
| Process dilation, extension, proof | finite $\mathcal C_V$, finite horizon; constructed finite hidden space | M:520–524 |
| S ⇔ D ⇔ Q_fb | finite visible alphabet, finite horizon $K$ | M:550–556 |
| Characterization theorem | time-homogeneous process on finite $\mathcal C_V$; (T) for (i) | M:540–546 |
| One-step theorem, Step 1, history-readback theorem, proofs | finite $\mathcal C_V,\mathcal C_H$; bijection; order $L$ | M:113–127, 135–137 |
| Overlap and return; C4r route | $\Gamma_n=I$ supplied | M:141–143 (`pIndivisible_of_identity_return_of_overlap`) |
| Reverse lemma; non-permutation witness lemma | finite bijective model, uniform prior | M:274–276, 439–441 |
| CP-indivisibility; no-uniform-finite-realization; C3; physical memory; cone and Bell ceiling | as printed | M:330, 490, 508–516, 457–475, 362, 414–416 |
| §4.6 theorem statement | as printed; only the Scope paragraph gains E14 | M:748–758 |
| Companion A1-free results | GR App. B; GR §3.3; Theorem 24 identities; forward gauge algebra | C3, C5, C8, C13 |

## 5. Regression controls (§A.41 invariant → checkpoint table)

Everything is implemented in [`phase0_controls.py`](phase0_controls.py), which uses the standard
library only.

- **Base and head.** The base is read with `git show`. The head is the working tree; under
  `--dry-run` it is the base with [`phase1_ledger.json`](phase1_ledger.json) applied in memory.
- **Exit status (§A.44).** 0 iff no control FAILs.
- **Self-test.** `--self-test` drives every control through violating and compliant edits,
  including all of the review's adversarial edits.

Results of the runs on the revised head:

| Run | Result |
|---|---|
| Self-test | PASS |
| Base, working tree | CTL-1–13 PASS; decision rule unmet (no edit yet) |
| `--dry-run` | CTL-1–8, 10, 12, 13 PASS; CTL-9 and CTL-11 N/A in memory; DR-1–3 all met |
| Ledger written to a working copy | CTL-1–8 and CTL-10–13 PASS; CTL-9 FAIL until a rebuild |
| Same, plus one unlisted line in `glossary.md` | CTL-11 and CTL-13 FAIL |

The working copy was reverted after each run.

| Id | Invariant asserted of Phase 1 | Checkpoint (mechanical) |
|---|---|---|
| CTL-1 | S ⇔ D ⇔ Q_fb unchanged | the theorem, the (S)/(D)/(Q_fb) paragraph and the proof occur once each and equal the base |
| CTL-2 | finite-horizon equivalence unchanged | same test for the process dilation, its extension and proof, the Characterization theorem and items (i)–(iii) |
| CTL-3 | C4r route unchanged | same test for the overlap-and-return theorem and proof; `pIndivisible_of_identity_return_of_overlap` still cited |
| CTL-4 | finite-carrier theorems unchanged as finite-model statements | same test for Lemma 3, the one-step theorem and Step 1, the history-readback theorem and proof, the reverse and witness lemmas, the CP theorem, the no-uniform-finite-realization proposition, C3, physical memory and the cone |
| CTL-5 | observer-relative finiteness reading unchanged | Definition and Lemma 1 equal the base; "only finite visible resolution is a theorem" present |
| CTL-6 | Lean census disposition unchanged | no change under `verification/lean*` or to the registry; no backticked identifier new to Main; registry statuses equal the base; `tools/lean_manuscript_census.py` exits 0 |
| CTL-7 | no edit implies a derived law, typicality, physical recurrence or inflow | over sentences added to `papers/` and `book/`, two rules apply. First, "holds in nature", "in nature", "is/are derived", "derived from" and "follows from the dynamics" fail unless negated. Second, a derive/force/select/determine/imply/yield/entail/follow/fix/establish/ensure verb near law, measure, typicality, recurrence, inflow or universe fails unless negated or conditional (if, whenever, unless, assumed). In addition, every added sentence using a new label carries a status word ("not adopted", assumed, hypothesis, condition, sufficient, postulate, alternative, open, full support) |
| CTL-8 | paper register (§A.32, §A.33) | added sentences in `papers/` contain no history phrase, no meta phrase and no four-letter capitals outside the whitelist, code and math |
| CTL-9 | generated artifacts current | `tools/staleness_check.py` exits 0 |
| CTL-10 | ledger inventory unchanged | each of the fourteen exact item openings ("(i) Axiom 2" … "(xiv) measurement independence") and "Fourteen items" occurs exactly once in the ledger |
| CTL-11 | the edit is exactly the preregistered text | each `papers/*.md` and `book/*.md` at the head equals the base with exactly the `phase1_ledger.json` splices applied. Each splice's old string occurs once in the base and matches its SHA-256. Any other change fails |
| CTL-12 | status wording not weakened | in Main and each Phase 1 book file, none of these counts decreases: "not adopted"; the word "open"; sentences pairing A1, item (ii) or total finiteness with "posit" or "hypothesis" |
| CTL-13 | FULL parity | every non-blank chapter line occurs in FULL, and FULL's non-chapter lines equal the base's (CENSUS §7 recipe) |

**Revision to the edit plan forced by the controls.** The first revised ledger contained three
pointer edits: at M:111, M:222 and M:266, "under the total-finiteness posit" would have become "on
a finite representative". CTL-12 failed on them, because they removed the word "posit" from four
sentences. These pointers are accurate as printed under the framing, so they were dropped (§6).

**Not mechanized; for the reviewer:**
- correctness and self-containment of each added proof (Main independence);
- placement and meaning of each label beyond its tokens.

## 6. Phase 1 edit plan (exact text in `phase1_ledger.json`; not applied)

The ledger is authoritative. It holds 29 splices: 15 in Main and 7 book units, each applied to its
chapter and to FULL. Every splice records its file, its exact old string and that string's SHA-256,
its new text and that text's SHA-256, its rows and the finding it answers. Any later change is
appended as a new reviewed entry.

| Unit | Site | Change (summary; exact text in the ledger) |
|---|---|---|
| E1 | M:36 | "open physical posit" gains ", not adopted, and one sufficient condition among those each result names" |
| E2 | M:44 | "the map acts on a finite $S$ under the total-finiteness posit" → "on the finite representative of the total-finiteness posit … the map acts on a finite $S$" |
| E3a | M:60 | "is a premise of the results that use it" → "is one sufficient condition for the results that use it", adding that each result names its hypotheses and that a weaker sufficient condition, where its sufficiency is proved, is stated with the result (§2.3, §3.2, §4.6) |
| E3b | M:60 | the use list adds: (NR) is an alternative sufficient condition for the P-indivisibility conclusion; the exact return and its index $L$ are statements about the finite representative |
| E5 | after M:129 | new paragraph *Corollary (near-return)*. Hypotheses: finite $\mathcal C_V$; one probability $\rho$ on a measurable $H$ shared by every root; measurable $F$. If $\Gamma_s$ is not a permutation, some rows overlap (one-line reason: disjoint supports would partition the $\|\mathcal C_V\|$ columns into singletons). (NR) is assumed for such a pair, as a hypothesis of this result and not adopted. Conclusion: not P-divisible on $\{0,\ldots,n\}$. *Proof.* Total variation against the contraction stated at the start of the proof above (M:119), ending in $\square$. On a finite representative Step 1 supplies (NR) at every multiple of $N$ exceeding $s$ |
| E6 | M:139 | index-free form under full support (FS), one direction at a time. (a)⇒(b): the first half of the proof with $\min(k,L-1)$ replaced by $k$, which uses no return. (b)⇒(c): the corollary under (NR) for an overlapping pair of rows of that $\Gamma_s$. (c)⇒(a): with no gap below $n$ the law is Markov with one-step matrices $Q_j$, and under (FS) each row of $\Gamma_t$ is a conditional law, so $\Gamma_t=\Gamma_s(Q_s\cdots Q_{t-1})$. The bound below $L$ and the horizon $\{0,\ldots,L\}$ stay finite-representative statements |
| E7 | M:178 | adds "or from a non-permutation rooted map and the near-return condition (NR) of §2.3 without finiteness" |
| E9 | M:278 | (IP), assumed as a hypothesis of this remark and not adopted: $\varphi$ preserves $\nu\otimes\rho$ with $\nu$ uniform. Rows sum to one; columns sum to one by invariance |
| E10 | M:706 | adds ", and one sufficient condition among those stated at each use" |
| E11 | M:722 | adds ", or the near-return condition (NR) assumed in its place" |
| E12 | M:724 | "whose finiteness is the total-finiteness posit" → "finite under the total-finiteness posit"; "not adopted" kept, adding "and one sufficient condition among those stated at each use" |
| E13a | M:730 item (ii) | text in §6.1 |
| E13b | M:730 item (iii) | adds the label "(REV), $\varphi$ a bimeasurable bijection of a measurable carrier" to the reversibility alternative already printed |
| E13c | M:730 closing | "conditional on the full list" gains ", item (ii) entering only as one of the sufficient conditions named at each use" |
| E14 | M:764 | the decay estimate holds with finiteness of $S$ replaced by (IL), assumed as a hypothesis of this estimate and not adopted: normalized $\varphi$-invariant $\mu$; $P$ the $\mu$-conditional expectation onto the declared local observables of a finite readout support with a locally finite dependence cone; (EM) on $\mu$-centred $L^2(\mu)$. The $O(\varepsilon)$ typical-set and finite-size corrections, the canonical-typicality clause and the exact recurrence of the Koopman operator of a finite permutation (Setup) are statements about the finite representative |
| B1 | ch00:95 | "remains open as a physical posit" gains ", not adopted, and is one sufficient condition among those the results name" |
| B2 | ch01:28 | mirror of E2 |
| B3 | after ch01:119 | the corollary (mirror of E5), referring to Step 1 of the chapter's proof |
| B4 | ch01:177 | "Because the physical representative is, under A1, finite and reversible, it also recurs:" → "On a finite representative, which A1 supplies, … also recurs; without A1, the near-return condition of the corollary in §1.5 is the stated sufficient condition for the indivisibility conclusion:" |
| B6 | appendix-b:46 | mirror of E9 |
| B7 | appendix-c:104 | A1 is "one sufficient condition rather than a premise of the framework", and the route's conclusion also follows from the near-return condition of §1.5, "assumed in its place and not adopted" |
| B8 | glossary:11 | "It is one sufficient condition for the results that use it, each of which names the hypotheses it consumes." |

**Dropped from the reviewed draft:**
- E4 and E8 (pointers at M:111, M:222, M:266): they failed CTL-12 and are accurate as printed.
- B5 (ch19): the sentences are accurate as printed.
- (ED) in item (iv) and the inflow sentence (review items 4–5).

No unit cites an audit record or a new kernel identifier.

### 6.1 What Main's posit ledger would say (E13a, verbatim from the ledger)

> (ii) total finiteness of the bijective representative of the status Remark of §1.2 (an open
> hypothesis, not adopted), carried as one sufficient condition and not as a premise of the
> framework: each result that uses it names the hypotheses it consumes, and a weaker sufficient
> condition, where its sufficiency is proved, is stated with the result — the near-return condition
> (NR) for the P-indivisibility conclusion of §2.3, the invariant-product condition (IP) for the
> doubly stochastic marginal of §3.2 and the invariant-law condition (IL) for the decay estimate of
> §4.6, each assumed as a hypothesis of that result and not adopted, and reversibility (REV), item
> (iii), an alternative sufficient condition for bijectivity — while the counting-measure selection
> of Lemma 3, the exact return and its index $L$, the orbit capacity, the CP-indivisibility theorem
> of §3.2, the physical-memory theorem of §3.4 and the canonical-typicality step of §4.6 are
> statements about finite representatives — Lemma 1 delivers finiteness of the observer's
> distinguishable states … [the existing text of item (ii) continues unchanged]

The closing sentence becomes "… conditional on the full list, item (ii) entering only as one of the
sufficient conditions named at each use." Item labels and "Fourteen items" are unchanged (CTL-10).

### 6.2 Propagation and rebuild

After the edit:

1. Apply the ledger.
2. Run `phase0_controls.py` (all CTL, including CTL-11 and CTL-13).
3. Re-grep with the §2.1 patterns and confirm that every site with an `E*` or `B*` action changed
   and no other site changed. State the surviving counts.
4. Rebuild with `sh ./build.sh Main` and `sh ./build.sh --book`.
5. Check the page count and characters per page.
6. Run CTL-9.

Companion papers are Phase 2.

## 7. Decision rule (fixed in advance)

Phase 1 succeeds if and only if, on its final head, all of the following hold:

1. **DR-1, DR-2, DR-2b.**
   - Ledger item (ii) contains "sufficient".
   - The ledger's closing sentence with "conditional on the full list" is present and contains
     "(ii)" and "sufficient".
   - The status Remark of §1.2 contains "sufficient".
2. **DR-3, diff-based.** For each change row, every token occurs in sentences of the named section
   that are absent from the base:
   - M4: (NR) and "not adopted" in §2.3.
   - M7(i): "index-free", "(FS)" and "Q_s \cdots Q_{t-1}" in §2.3.
   - M5/M7(ii): "finite representative" and "$L$" in §2.3.
   - M3: (IP) and the column-sum identity in §3.2.
   - M11: (REV) in §4.5.
   - M18/M20: (IL), "L^2(\mu)" and "canonical-typicality clause" in §4.6.

   The corollary paragraph must contain "*Proof.*" and "$\square$". The standing rows (M1/M2, M9,
   M13, M16, M19) must keep their finite-representative scope phrases, present at the base, at the
   head.
3. **All controls hold.** CTL-1 to CTL-13 PASS; CTL-11 makes the text the ledger's exactly.
4. **Review.** An independent non-author review confirms the proofs and Main's independence.

Any failure means Phase 1 does not land as preregistered. The predicates, token lists and ledger
are not adjusted after Phase 1's text exists, except by an appended, reviewed ledger entry made
before the edit.

## 8. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1055 comments 7030993647, 7030887534 | authorization and scope | provenance; quoted with author and time |
| #1442 comment 7031480016 | the review answered by this revision | provenance |
| #1421, #1431 review comments (F3) | review status of the inputs | provenance; the results used are on `main` |
| commit `a8119d20` (F1) | F1 | support on `main` |
| #1055, #1334, #1169, #866, #1441 | accountability; O-INFLOW; O-A4 | provenance |

## 9. What an independent reviewer must check

1. That the revision answers review items 1–8 and the nits. The checkpoint maps each item.
2. The added sites (§2.1, last paragraph) and the structural sites against the files, and that their
   keys are existing rows.
3. E5 and E6 in the ledger, one direction at a time (§A.34), including (FS) and the direct divisor
   of (c)⇒(a); and E9.
4. E14: that the decay estimate uses only the listed properties, and that the listed parts stay
   finite.
5. The marks of §3.1, especially the two **alternative (incomparable)** marks and the separating
   examples.
6. That no unit adopts a premise or presents a law, typicality, recurrence or inflow as derived, and
   that the ledger's wording is "assumed as a hypothesis … not adopted" throughout.
7. That `phase0_controls.py` implements §5 and §7 as stated; that the self-test, the base run and
   the dry run reproduce; and that the review's adversarial edits fail.
