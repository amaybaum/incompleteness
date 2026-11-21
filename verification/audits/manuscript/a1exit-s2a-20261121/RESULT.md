# A1-EXIT Step 2, unit S2-A (lattice qualifications): result

**Status.** Writer's manuscript-correction record. The edits of `PREREG.md` (pushed at `940dde6c1`
before any manuscript edit) are applied verbatim in `e414d1c24`; amendment 1 (`66bae3100`, appended
before its edit) is applied in `083e13db2` (deviation D1, §5); amendment 2 (`47812024a`, appended
before its edits, answering the round-1 review) is applied in `8b77e78f5` (deviations D2, D3). No Lean, registry, ledger or Q1 record
edit; no merge; no workflow dispatch. Round-1 independent review: REVISE (§7).

**Authorization.** Owner `amaybaum`, #1169 comment 7056875845 (2026-11-21), unit S2-A. Q1's E5 is
skipped by the same decision. A1 and Main ledger item (ii) are untouched.

**Goal link (§A.47).** The A1-exit objective (#1169). Outcome for this unit's sites: A4's lattice
clause and the Q1 consumers are stated on ℤ^d as the standard construction, and each finite periodic
quotient is a qualified case with Q1's wrapping conditions. No site needed A1 for its truth; no site
became an open statement.

**Base.** `main` at `1c7eedc40`. No drift from Q1's pin `9db51884` at any site: `git diff 9db51884
1c7eedc40` in the affected files is only Q2's SM:242/250 edit, and `q1_census.py` and
`q1_census_supp.py` reproduced Q1's committed JSON byte for byte at the base. Line numbers are
unchanged by the edits (each is an in-line replacement), so every site keeps its base line number.

## 1. Edits as applied

The exact old and new strings are in `PREREG.md` and `checks/s2a_edits.json`. `checks/s2a_check.py`
exits 0 in default mode at `8b77e78f5` (15 base entries, 3 amending entries; amended texts checked): every new string occurs exactly once in its file and in its
mirror, and no old string survives outside its own new string.

| Id | Site (line after edit) | Ledger row | Source |
|---|---|---|---|
| E1 (+ E1-am2) | SM:222 | X-42, X-43 | Q1 §7 E1 (covers SM:134/136, SM:549, SM:1237–1257, SM:1554); "one and the same axis" (D3) |
| E2a, E2b | SM:539 | X-42 | Q1 §7 E2 |
| E3a, E3c | SM:1506, SM:1536 | X-42 | Q1 §7 E3 |
| E3b (+ E3b-am2) | SM:1532 | X-42, X-43 | Q1 §7 E3, amended per Q1 §3 row C13 to "period vectors lie in $2\mathbb Z^3$" (D2) |
| E4 | ch06:24 = FULL:1535 | X-42, X-43 | Q1 §7 E4 (covers ch06:22, :30, FULL:1533, :1541) |
| E6 (+ E6-am2) | ch05:91 = FULL:1406 | X-42, X-43 | Q1 §7 E6, "one and the same axis" (D3) (covers ch05:154, :156, :162, :166, :172, ch06:20 and FULL mirrors) |
| A4-Sub98 | Sub:98 | X-40 | owner A4 decision (#1169 c.7048255658) |
| A4-ch02-82 | ch02:82 = FULL:712 | X-40 | as above (book mirror) |
| A4-SM202 | SM:202 | X-40 | as above (SM restatement) |
| A4-ch05-65 | ch05:65 = FULL:1380 | X-40 | as above (book mirror) |
| A4-Sub157 | Sub:157 | X-41 via X-40 | X-40's A4 restatements (Q1 §6); X-41 "covered by X-40's A4 restatement" |
| A4-ch02-96 | ch02:96 = FULL:726 | X-41 via X-40 | as above (book) |
| A4-ch19-198 | ch19:198 = FULL:5268 | X-40 | X-40 site column; PREREG amendment 1 (D1) |

15 edits at 21 locations (6 book edits mirrored into FULL). A4 restatement: ℤ^d is printed as "the
discrete lattice … as the standard construction, distinct from a continuous space"; the finite
periodic quotient ℤ^d/P is "admitted as a qualified case, under the conditions on P stated with each
result that uses it" (Sub cites [SM §4.1], where E1 states them). No edited sentence calls a finite
lattice an approximation or a representative of ℤ^d. Only the lattice clause of A4 changed; its
second sense, the side-≥3 independence example (a finite example, true as stated) and A1 are
untouched. One edited sentence states a consequence of Theorem 13: SM:1532 ('t Hooft anomaly matching
from Theorems 13 and 15 under H-χ'). Its quotient qualification carries C13's period condition
`P ⊂ 2ℤ^3` (D2). X-43's further C13 condition (bounded invertibility of an off-diagonal hidden block
on ℓ²) is printed neither there nor at Theorem 13 (SM:543); see §3.

**Ledger sites changed (for the post-Step-2 reconciliation).** X-40: Sub:98, ch02:82, FULL:712,
SM:202, ch05:65, FULL:1380, ch19:198, FULL:5268. X-41 (lattice clause only): Sub:157, ch02:96, FULL:726. X-42: SM:539,
SM:1506, SM:1532, SM:1536, ch06:24, FULL:1535, ch05:91, FULL:1406, SM:222. X-43: SM:222 (E1), E4
and E6 sites. All at their base line numbers. Not changed: X-41's SM:122 and SM:252 (unit S2-C); X-43's SM:446 (E5, skipped).

## 2. Propagation and re-grep

| Phrase | Hits after edit (papers/ + book/) | Disposition |
|---|---|---|
| "finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice" | 0 | all six instances restated |
| "finite periodic lattice" | 1 (ch18:242 and FULL mirror) | A1 sentence: "a compact identification can give a finite periodic lattice … one way to realize A1 in a model"; true as a qualified case; A1 is out of scope |
| "finite periodic quotient" | 14 lines (6 files) | all are this unit's new texts and their FULL mirrors |
| "finite-index sublattice" | Sub:98, SM:202, ch02:82, ch05:65 and mirrors | new A4 texts |
| "periodic-lattice class" | 24 lines (10 files) | true for ℤ^d and its quotients alike; unchanged |
| "periodic lattice" (other) | SM:210, ch05:73 (Corollary: "a $d$-dimensional periodic lattice") | true on ℤ^d and quotients; unchanged |
| "torus"/"tori" with lattice sense | SM:294, :296 (finite-torus probes, explicitly finite), SM:539 (odd torus, a qualified case), ch01:284 (finite torus "before wraparound") | stated as finite cases; no approximation claim |
| "approximat" with lattice/finite context | none calls a finite lattice an approximation of ℤ^d | see §3 |
| A4 phrasings with finite/periodic/quotient | Complexity:13, :37; Computation:13; GR:446; SM:30, :36, :56, :60, :172, :208, :210, :1257; ch02:70, :94; ch05:15, :51, :63, :71, :77; ch10:26, :28 | all "periodic-lattice class" or "rank of the translation lattice"; consistent with the restatement |

Q1 census re-run (`q1_census.py`, `q1_census_supp.py`, output to scratch, Q1's committed JSON
untouched): 216 → 218 census lines. The changes are exactly the E-text lines: SM:222 gains G1, G2 and
L-labels (E1's checkerboard, corner and Theorem 2 clauses); ch05:91 and FULL:1406 enter the census
(G4, G2: E6's "finite periodic quotient", "staggered phases"); ch06:24 and FULL:1535 gain G4 and G2
(E4). Supplementary census: 235 lines, ch05:91 and FULL:1406 gain G6/G7. The A4 lines stay in G4 with
unchanged family sets. E2 and E3 sites were already in G1 and their family sets are unchanged; their
text is confirmed by `s2a_check.py`.

## 3. Findings outside scope (not fixed)

- **ch18:226 = FULL:4957 and ch18:22 = FULL:4753.** "whether the lattice extends globally as
  $\mathbb{R}^3$, identifies as a 3-torus, has a Klein-bottle quotient" and "whether the universe is
  topologically trivial $\mathbb{R}^3$, a 3-torus …" put the discrete lattice's global form beside the
  continuous space ℝ^3. Under the owner's A4 decision the infinite discrete lattice (ℤ^3) and the
  continuous space are kept distinct; the lattice counterpart of ℝ^3 is ℤ^3. Not in this unit's sites:
  the coordinating session classifies them as Q3 sites and routes them to unit S2-E as a finding.
- **Q1 record, E3 against C13.** Q1 §7 E3's text for SM:1532 ("quotients whose period vectors have
  even coordinate sum") contradicts Q1's own §3 row C13 (Theorem 13 on a quotient iff `P ⊂ 2ℤ^3`;
  the skew even-sum quotient is a countermodel). Applied here in the C13 form (D2); the Q1 record is
  unchanged and the coordinating session routes the discrepancy separately.
- **SM:1532 and SM:543, C13's invertibility condition.** SM:1532 uses Theorem 13 under H-χ', whose
  hidden block can carry an off-diagonal term. Q1 C13 and ledger X-43 state that on ℤ^3 the Schur
  complement then needs that block boundedly invertible on ℓ² of the odd sublattice. Neither SM:1532
  nor Theorem 13's statement prints this condition. Adding it is outside the round-1 instruction and
  this unit's edit list; reported to the coordinator.
- **"Finite representative"** (Main, GR, Sub, ch01–ch03, ch09, ch14, glossary, appendices) refers to
  A1's finite configuration space, not to a finite lattice representing ℤ^d. It is A1 vocabulary
  (ledger X-02, X-45) and out of scope; no site uses it for the lattice.
- No site in papers/ or book/ calls a finite lattice an approximation of ℤ^d. The "approximation"
  sites with lattice context (Sub:225, :227, :552; SM:547; GR:292; Structure:226) concern the lattice
  against a continuum theory, not a finite lattice against ℤ^d.

## 4. Build and checks

| Check | Result |
|---|---|
| `sh ./build.sh SM Substratum` | OK; SM 148 pages (base 148), Substratum 54 (base 53); no dropped glyphs (SM rebuilt after amendment 2, same figures) |
| `sh ./build.sh --book` | OK; 489 pages (base 489); no dropped glyphs (also after amendments 1 and 2) |
| median characters per page (pdftotext -layout) | SM 3130 (base 3153), Substratum 3189 (3240), FULL 2997 (2998); unchanged after amendments 1 and 2 |
| `python3 tools/coverage_check.py` | OK (132 canonical statements); no fingerprint moved, LEDGER.json unchanged |
| `python3 tools/lean_manuscript_census.py` | OK |
| `python3 tools/artifact_placement_check.py` | OK |
| `python3 tools/legacy_records_check.py <head>` | UNDECIDABLE locally (shallow repository); no legacy record touched; CI decides |
| added-line register scan (§A.32, §A.33) | no history phrase, reader instruction or caps emphasis |
| `checks/s2a_check.py` (default) | PASS |
| `checks/s2a_check.py --apply` on the base files (`1c7eedc40`) | reproduces the head's seven manuscript files byte for byte |

## 5. Deviations from PREREG

- **D1 (amendment 1): ch19:198 = FULL:5268 added.** The PREREG listed it as outside the unit's
  authorized sites. The coordinating session ruled (2026-11-21) that it is in scope: it is in X-40's
  site column ("stated as a qualified case"), and the owner authorized S2-A to make X-40's A4
  restatement (#1169 c.7056875845). The amendment was appended to PREREG and pushed (`66bae3100`)
  before the edit, which is applied in `083e13db2`. Old: "On a finite lattice, the notion". New: "On a
  finite periodic quotient of $\mathbb{Z}^3$, a qualified case of A4 (Chapter 2), the notion". One
  qualified-case clause, no approximation wording.

- **D2 (amendment 2, review B1): SM:1532 departs from Q1 §7 E3.** E3's "(on $\Lambda$ and on
  quotients whose period vectors have even coordinate sum)" is replaced at SM:1532 by "(on $\Lambda$
  and on quotients whose period vectors lie in $2\mathbb Z^3$)". The sentence states 't Hooft anomaly
  matching from Theorems 13 and 15, and Q1 §3 row C13 classifies Theorem 13 on a quotient as holding
  iff `P ⊂ 2ℤ^3`, with the skew even-sum quotient as countermodel. SM:1506 and SM:1536 assert only the
  checkerboard and keep E3's text. The PREREG rules line on Theorem 13 is corrected in amendment 2.
- **D3 (amendment 2, review N1): "one and the same axis".** At SM:222 (E1) and ch05:91 = FULL:1406
  (E6), Q1's "even off one axis" becomes "even off one and the same axis", as Q1 Lemma 1(c) requires
  (a single axis common to all period vectors). An accuracy departure from Q1's verbatim text.

Every other edit was applied as preregistered, at the preregistered line.

## 6. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 c.7056875845 | Authorization | Provenance |
| Round-1 review of `88b70e0f` on #1470 | D2, D3 | Provenance; the support used (Q1 §3 row C13, Lemma 1(c)) is on `main` |
| Coordinating-session ruling on ch19:198 (2026-11-21, session message) | D1 scope | Provenance; the authority it applies is #1169 c.7056875845 and ledger X-40 on `main` |
| #1169 c.7048255658 | A4 wording rule | Provenance; the decision is quoted with author and time in Q1 RESULT §7 on `main` |
| Guiding PR (#1470) | Tracking | Provenance |

Support used by the edits (Q1 RESULT §2–§7 and checks, A1-EXIT ledger rows X-40–X-43) is on `main`
at the base and is cited as it stands there.

## 7. Verification status and remediation (§A.46 item 4)

- **Evidence level.** Manuscript text corrections taken verbatim from Q1 §7 (independently reviewed
  and owner-accepted, Q1 §11) and from the owner's A4 decision, with mechanical checks (§4). The
  mathematical content (Q1's per-consumer conditions) is Q1's, at Q1's evidence level; nothing here
  adds or strengthens a result.
- **Review.** Round 1 at `88b70e0f`: REVISE (B1, N1), recorded on #1470 and answered by amendment 2. **Missing.** A delta review of amendment 2.
- **Accountable Issue.** #1169 (A1-exit). **Resolution.** A review recorded on the guiding PR, then a
  separate owner merge decision.
