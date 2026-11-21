# A1-EXIT ledger — preregistration: schema, sources, completeness check, deletion criterion

**Status.** Writer's paper-only preregistration. It is committed and pushed before any ledger row is
populated, and the ledger (`LEDGER.md`, with its machine-readable rows and site map) follows in
later commits. Existing records only: no proof, measure construction, physical premise, manuscript,
Lean or registry edit, and no classification is re-derived. A1 (Main posit ledger item (ii)) remains
open and unadopted. Independent non-author review is required before any use.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7047514209](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7047514209),
2026-11-20T18:31:48Z, Step 1 table, row **A1-EXIT**: "A ledger mapping every remaining A1 dependency
to its disposition, its exit route, and the exact corrections required" — "A complete ledger" —
"Paper-only". The objective, quoted: "Every result that depends on A1 must end in one of three
states: independently justified; explicitly finite-only; marked open." The four safeguards are
quoted in §4 and applied as columns and checks.

**Goal link (§A.47), from the authorization.** "Make OI's foundational formulation independent of the
assumption that the whole universe is finite, while keeping honest limitations on the results that
still require finiteness." This unit decides, for each A1 dependency, which of the three end states
applies, what correction reaches it, and which unit owns that correction. It does not decide any
outcome of Q1, Q2, R6 or the Step-2 units.

**Source pin.** `main` at `9db518844` (merge of #1460). Site notation `File:n` is line `n` at the pin
(`M` Main, `SM`, `GR`, `Sub` Substratum, `Str` Structure, `Meth` Methodology, `Comp` Computation,
`Cx` Complexity, `Intro` Introduction, `Med` Medicine, `chNN`, `appA/B/C`, `gloss`, `FULL`).

## 1. Sources (cited, not redone)

All under `verification/audits/foundations/` on `main` at the pin.

| Short name | Path | Contribution to the ledger |
|---|---|---|
| REMAINDER | `a1-remainder-20261119/REMAINDER.md` | Rows M1–M21, C1–C14; residues R1–R6; lemmas L1–L10, O-A4, O-INFLOW |
| P0 | `a1-scope-phase0-20261120/sites.json`, `PREREG.md` | 566 classified lexical and structural sites; pattern set; classes DECL, R1–R6, B, INFLOW, FREE, FP |
| P1 | `a1-scope-phase0-20261120/phase1_ledger.json` | Main and Phase-1 book splices (applied, #1443) |
| P2 | `a1-scope-phase2-20261120/PREREG.md`, `dispositions.json`, `phase2_ledger.json` | Companion and mirror dispositions (applied, #1450); the 77 Phase-3 sites (§2) |
| FCLASS | `a1-finiteness-classes-20261117/CLASSIFICATION.md` | F1–F4/A1 row classes |
| A1-09 | `a1-09-dependency-census/CENSUS.md` | Declaration and site traces (through P0's row keys) |
| NEC | `a1-necessity-20261117/ASSESSMENT.md` | Five-family reconciliation |
| O-A4 | `o-a4-20261120/RESULT.md` | Step table; §6 finite-model-only steps; §7 period-lattice failures; §9a |
| NR-1 | `nr1-near-return-20261116/NR-1.md` | (NR) failure under β_A for the selected update |
| R1-INF | `r1-inf-20261119/RESULT.md` | Infinite-volume law facts (P-ED, μ-O/μ-R collapse, m_H) |
| STAGE0 | `r1-l8-stage0-20261120/AUDIT.md` | 22 law-dependence rows (a)/(b)/(c) |
| STAGE1i | `r1-l8-stage1i-20261120/AUDIT.md` | Horizon-entropy normalization provenance |
| STAGE1ii | `r1-l8-stage1ii-20261120/AUDIT.md` | 49 rows; the 12 NOT FOLLOWING global-phase rows; G1–G3; O1 |
| POSIT-MIN | `posit-min-20261120/items.json`, `AUDIT.md` | Item (ii) verdict WEAKEN; items (iii), (iv), (xi) |
| LEAN-2(i) | `o-a4-20261120/RESULT.md` §8, §13 (amendment) | A2–A5 kernel predicates on ℤ^d |

Owner records used for dispositions: #1169 comment 7047514209 (this unit, Q1, Q2, R6, Main:764,
Step 2); #1169 comment 7041456852 item 3 ("(iii) Orbit and record laws (μ-O, μ-R) as finite-only
statements … Adopted as a scope restriction for existing results"); #1169 comment 7035888700
(Phase 2 Q1–Q5); #1454 (P2-Q1, P2-Q2, P2-Q3).

## 2. Units of the ledger

- **Dependency row (`X-nn`).** One result, or one separately worded part of a result, whose stated
  support uses A1 (total finiteness of `S`, of the bijective representative, of the substratum or
  of the total carrier), directly or through A4's finite periodic lattice (`a1_of_finite`), or one
  pointer to the posit itself. Rows are seeded from REMAINDER M1–M21 and C1–C14 and split where a
  later record (STAGE0, STAGE1ii, O-A4, owner decisions) separates parts with different end states.
- **Site (`File:n`).** A manuscript line carrying a dependency row's claim, its declaration or a
  pointer to it, in `papers/*.md`, `book/*.md` (chapters, appendices, glossary) and FULL. The site
  map is P0's 566 sites relocated to the pin, plus every line at the pin that matches P0's pattern
  set (`core_patterns`, `paraphrase_patterns`) and has no P0 counterpart.

## 3. Row schema

| Column | Content |
|---|---|
| Id | `X-nn` |
| Dependency | The result and its home `File:n` at the pin |
| Source rows | REMAINDER / STAGE0 / STAGE1ii / O-A4 / FCLASS / P0 keys |
| How A1 enters | The step that uses finiteness, as the source records it |
| Disposition | Exactly one of **J** (independently justified under a named weaker condition, proved on `main`), **F** (explicitly finite-only: a statement about finite systems or finite representatives, with no physical reading that the universe is finite), **O** (open: no proof without A1 and no finite-only reading that keeps the claim) |
| Weaker condition | For J: the condition, where proved, layer |
| Disguised A1? (S1) | For J: does the condition imply total finiteness, or restate A1 or a uniform-on-finite law under another name? `No` / `Yes` / `Relabel` (logically weaker but as unobservable as A1, REMAINDER §3) with the reason. A `Yes` forbids J |
| Exit route | What makes the end state hold (already on `main`; owning unit's outcome; scope narrowing; deletion edit) |
| Correction | Exact `File:n` and proposed wording, or `none` |
| Mirrors (S3) | Every site carrying the claim; `visible` / `not visible` / `n/a` for the qualification at each |
| Owner | Q1, Q2, R6, Main:764, Q3 propagation, R1/R2 scoping, Step-2 phase, final deletion, or none |
| Status | `done` (on `main`), `in progress` (open PR), `authorized`, `queued` (Step 2, not authorized), `open` (no unit) |

Each site in the site map carries: `File:n` at the pin, quote, P0 id (or `new`), P0 class and rows,
ledger row, correction code (`none`, `ptr` — a pointer to A1 or item (ii) rewritten at deletion,
`unit` — corrected by the owning unit), owner, status.

## 4. Safeguards as checks (owner, quoted)

1. "**No disguised A1.** A weaker hypothesis must not imply total finiteness indirectly, or reproduce
   A1 under another name." → column S1 on every J row; a J row whose condition is `Yes` is
   reclassified F or O. `Relabel` is reported, not forbidden.
2. "**No forced proof.** Q1 and R6 may end with negative results or finite-only restrictions." → rows
   owned by Q1 and R6 carry their current disposition as F or O, with the possible outcomes listed;
   no row is classified J on the expectation of a proof.
3. "**No silent promotion.** Statements that are finite-only or conditional stay clearly qualified in
   Main, the companion papers, the book and all mirrors. R1's physical justification and C1
   (coupled shell law) remain open." → column S3 on every F and O row; R1's physical justification
   and C1 coupled are O rows.
4. "**No premature deletion.** Main ledger item (ii) may be deleted only after three things are
   complete: the A1-EXIT ledger, all required propagation, and an independent review showing that no
   result silently relies on A1." → the deletion criterion (§6).

## 5. Completeness check (run by `ledger_check.py`; all must pass)

| Id | Check |
|---|---|
| CK1 | Every REMAINDER row M1–M21, C1–C14 and residue R1–R6 maps to at least one ledger row |
| CK2 | Every STAGE0 row of class (b), (c) or undetermined, every STAGE1ii row NOT FOLLOWING or RETAINED-WITH-(LE), and every O-A4 step of class (b) or (c) maps to a ledger row |
| CK3 | Every P0 site of class other than FP and FREE is relocated to a line at the pin (same text, or the P1/P2 splice that changed it), or recorded as removed, and maps to a ledger row |
| CK4 | Every line at the pin matching P0's pattern set is in the site map; a line with no P0 counterpart is classified by hand, with the class vocabulary of P0 |
| CK5 | Each ledger row has exactly one disposition in {J, F, O}; each J row has S1 ∈ {No, Relabel}; each F and O row lists its mirror sites with S3 |
| CK6 | Every site that names A1, total finiteness as a posit, or item (ii) (P0 patterns core P1, P2, P5) has correction code `ptr` or `unit`, unless its row's correction is recorded as `none` with a reason |
| CK7 | The 77 Phase-3 sites (P2 §2) are each listed, with owner Q3 propagation |
| CK8 | Lean: every kernel declaration that the manuscripts cite for an A1-dependent row, and `SubstratumInterfaceAudit.a1_of_finite`, is listed with its finite or infinite carrier |

Countercontrols: a synthetic site with no row, a J row with S1 = `Yes`, and a dropped Phase-3 site
must each make the check fail (self-test).

## 6. Deletion criterion for item (ii) (stated in advance)

Item (ii), and with it A1 as a posit of the framework, may be deleted only when all of the following
hold at one exact head, and an owner decision authorizes it (owner safeguard 4, Step 2):

1. **Ledger complete.** CK1–CK8 pass at that head.
2. **Every row closed.** Every row's status is `done`: its correction is on `main` or recorded as
   `none`. Rows that stay F or O are closed when their qualification is visible at every mirror (S3)
   — an open row need not be solved, only stated as open where it is claimed.
3. **No disguised A1.** No J row carries S1 = `Yes`, and every `Relabel` is stated as such in the
   manuscript where the condition is introduced.
4. **Pointers rewritten.** Every site with code `ptr` is rewritten in the deletion edit itself: a
   pointer to A1 for an F row becomes the finite-only scope ("for a finite substratum", "on a finite
   representative"); for a J row, the weaker condition; for an O row, the open statement. No
   pointer to item (ii) or to A1 as a hypothesis of the framework survives.
5. **Independent review.** A non-author review of that exact head records that no result silently
   relies on A1: a fresh pattern scan (P0 set) finds no unqualified site.

What may remain after deletion: F rows (finite-only theorems, stated as such) and O rows (open
claims, stated as open). What may not remain: any claim whose support is A1 presented as a
property of nature or of the framework without its finite-only or open qualification.

## 7. Decision rule for dispositions (fixed in advance)

- A row is **J** iff a source on `main` proves its conclusion, as stated, under a condition that does
  not include total finiteness, and S1 ≠ `Yes`. Where only part of the conclusion is covered, the row
  is split.
- A row is **F** iff its conclusion is a true statement about finite systems or representatives
  (proved there), no A1-free proof covers its physical reading, and an owner decision or a printed
  scope already restricts it, or the owning unit's authorized outcome includes the restriction.
- Otherwise **O**. A row whose owning unit is in progress (Q1, Q2, R6) carries its disposition at the
  pin and the outcomes the unit may reach; it is not marked J in advance (safeguard 2).

## 8. Limits

Paper-only. The site map reuses P0's lexical census; a dependency carried by a sentence that
matches no pattern and is not a P0 structural site is outside CK4, and the review checks for such
sentences (§9 of `LEDGER.md`). No Main, companion, book, Lean or registry file is edited by this
unit.
