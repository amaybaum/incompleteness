# SC-22 fix: the 𝒩-regime vocabulary in the book (#942 / #946)

Base: `main` at `0d917665`. Provenance: the SC-22 audit report and its rewrite list (`REPORT.md` and `proposals.py`
on `audit/intro-corpus-20261026`, head `42bbd33c`, written at `1a60e06b`). The rewrite list was checked against
`0d917665` before editing, and each of its old strings still occurred once in its chapter and once in FULL. The
exact probes this record relies on are landed beside the audit track (see Checks). Every edit removes or narrows a claim, or relabels. No new physical assumption is
introduced, and no papers are touched: the 𝒩-regime vocabulary occurs only in the book.

## Owner decisions

| Decision | Applied as |
|---|---|
| (i) 𝒩 is the peak, not the cumulative quantity | The report's D3, stated at ch18 §18.3 (anchor) and in the glossary. On a window W = {0, …, K}, 𝒩 = max over pairs of preparations and s < t in W of [d_t − d_s]⁺, with d the total variation of the visible population laws, equivalently the trace distance of the diagonal states, so that 𝒩 has one value. "Peak" here means the largest single revival, d_t − d_s on one interval. It is not the maximum of d_t, and not the sum of increases, and it lies in [0, 1]. The cumulative quantity (the Breuer–Laine–Piilo sum of every increase) is named separately, "cumulative backflow", at the anchor only. It is not used elsewhere. The anchor gives the reason it is unbounded on a finite reversible system: Γ_{t+L} = Γ_t (Main §2.3), so a revival recurs in every period. |
| (ii) relabel "partially-quantum" | "restricted quantum-statistical regime" at every site except the two excluded below. Section heads ch13 §13.7, ch15 §15.7 and ch18 §18.3 are renamed. The glossary entry is renamed and moved to its alphabetical place. The anchor defines the name as partial revival, 0 < 𝒩 < 1. It also says what the name refers to: the representation at the transition-statistics layer, with the operational layer not supplied. That restriction holds at every 𝒩, so the regime is fixed by its revival range, and the name marks neither a partial nor a complete quantum theory. ch18 :76 "partially quantum in that precise sense" becomes "the quantum description is restricted in that precise sense … not a complete operational quantum theory". |
| (iii) remove the ch18 table | The table is removed. The prose keeps only these conclusions. A fast, uniformly erasing bath drives the readback gap to zero and (C4) fails (Main §2.3, fast-bath lemma). A slow or static bath gives neither memory nor revival by itself (Main §2.3, static-bath coin). The candidate systems (protein conformational dynamics, single-enzyme kinetics) are stated as the proposal's conjecture. Dropped: every 𝒩 placement by τS/τB (not derived), the "maximal" and "weak" labels (undefined for the peak measure), and the "memoryless at τS/τB ∼ 1" row (the lemma needs τB ≪ τS). The matching clause at ch18 :94 ("in regimes where τS/τB is intermediate") is removed. |

## Sites

Line numbers are at `0d917665`. Every chapter edit is mirrored in FULL. The mirror check compares the multiset of
lines added to and removed from FULL with the same multisets over the chapters. Both are equal: 78 lines added and 86
removed. The 8 extra removals are the table's 7 rows and the blank line before them.

| Site | Was | Anchor | Now |
|---|---|---|---|
| ch18 :74 (R1) | "P-indivisibility measure 𝒩", interpolating to "maximal backflow (𝒩 at its maximum value, fully P-indivisible)"; "partially quantum" | Main §2.3: P-divisible ⇒ d non-increasing; the converse fails; XOR is P-divisible on a window carrying its memory (`regime_exact.py` B: gap at order 1, R = 0 on {0..2}) | Peak revival measure defined; cumulative backflow named apart; 𝒩 > 0 ⇒ P-indivisible; memory does not fix 𝒩; three ranges; label defined as above |
| ch18 :60, :76 (R2–R4), :78 (R5, R6) | "structurally distinct" third memory regime; "degree of indivisibility"; RHP as a backflow measure | Main §2.3, §3.4 | Regime lies strictly between no and complete revival; 𝒩 is the largest revival, not a distance from divisibility; RHP measures CP-divisibility departures |
| ch18 :72 (R12) | marginal-capacity regime "is" the partially-quantum regime | Main §3.4 (c), capacity floor | Capacity floor stated; revival at marginal capacity stated as the proposal's hypothesis |
| ch18 :80–:88 (R7, R8), :94 | table; "specifies where … expected to occur"; τS/τB-intermediate clause; "A density-matrix description requires specific algebraic constraints" | decision (iii); Main §3.4 (every finite law is representable); the form already at ch13 :144 | Conjecture; table removed; τS/τB conclusions as above, with "does not by itself place"; "A memoryless (divisible) density-matrix description requires …" (coordinator decision) |
| ch18 :90, :92, :96 (R9, R10, R13) | "specific predictions"; one test for both memory and revival; "not a hypothetical prediction" | Main §2.3 | Proved distinction plus labelled conjecture; memory test and revival test separated; "testable conjecture" |
| ch18 :16, :28, :325, :335 (R11, R14) | label; "partially-quantum regimes" as content standard physics lacks | ch18 :78 (partial revival is standard phenomenology) | Relabelled; :335 names the capacity-controlled origin instead |
| ch13 :20, :22, :24, :40, :68, :80 (B1–B5) | intermediate 𝒩 as prediction; test of "density-matrix descriptions"; F(r) cross-reference to ch18 §18.3 | Main §2.3, §3.4; ch15 §15.7 | Labelled proposal; memory and revival tests separated; cross-reference to ch15 §15.7 |
| ch13 :84, :128, :130, :132, :142, :146, :170 | label | — | Relabelled; attribution to the mechanism proposal where the sentence names the framework |
| ch13 :128 (B6), :134 (B7), :136 (B8), :138 (B9), :140 (B10, B11), :144 (B12) | diagnostic that "distinguishes" from classical memory; maximal-backflow system; biology "spans the regime where C3 is marginally satisfied" | Main §2.3, §3.4; capacities ≥ 10³⁰ at :138 | Memory test alone does not separate; 𝒩 measures revival, not memory; biology's placement a conjecture the capacity ratio does not fix |
| ch13 :172 (added) | diagnostic "testing for density-matrix structure" | Main §3.4 (every law is representable); B1/B3 | Revival measurements, with multi-time correlations testing memory |
| ch15 :10, :20, :140, :142 (E1–E3) | label; C2/C3 conflation; maximal-backflow regime | — | Relabelled; revival at marginal hidden capacity |
| ch15 :144 (E4) | overwhelming C3 margin ⇒ maximal backflow; regime at N_H/N_V ∼ 1 to 10 | Main §3.4 (c); XOR plus an idle register (visible law unchanged, `regime_exact.py` C) | Capacity bounds memory without fixing revival. The hypothesis range is narrowed to N_H/N_V ∼ 1, the proposal's own F(r) < 1 range, which also matches :160 and :246 |
| ch15 :146 (E5), :148, :150 (E6) | memory-backflow spectrum; Markov failure as "the regime's operational signature" | Main §3.4 | Revival scale; Markov failure is the memory signature; regime's signature is partial revival |
| ch15 :152 (E7) | backflow saturation, "specific saturation patterns as r approaches unity from above" (F = 1 there) | Main §3.4 (c); F(r) at :154 | Memory capped by capacity; revival below its saturated value at r < 1; no further pattern specified |
| ch15 :154 (E8), :168 (E9) | "non-monotonic" 𝒩(r); F → 1 called maximal backflow | `regime_exact.py`: 2r − r² strictly increasing on [0, 1], F(1) = 1; §15.8 relation 𝒩 = 𝒩_max·F·(1 − τS/τB) with 𝒩_max measured | "increasing on that range"; F → 1 is "saturated revival, 𝒩 = 𝒩_max at small τS/τB", not complete revival (𝒩 = 1); observable defined as the peak revival of the total-variation distance of the visible population laws |
| ch15 :158, :160, :164, :166, :176, :182, :184, :190 (E10, E11, E14–E17) | non-Markovianity; label; "fully-quantum regime"; "memory factor is small" | — | Revival; relabelled; "τS/τB is small". At :184, F = 1 is saturated revival (𝒩 = 𝒩_max), and the short region is the proposal's sub-saturated case 0 < F < 1. Since 𝒩_max ≤ 1, that case lies in the regime 0 < 𝒩 < 1 whenever τS/τB < 1, and a saturated 𝒩_max < 1 is itself partial revival. |
| ch15 :197, :198, :208, :210 (added) | "for P-indivisible dynamics" revivals in G²; trace distance D(t); "non-Markovianity … 75%"; monotone G² = "Markovian" | Main §2.3 (indivisibility without revival; monotonicity necessary, not sufficient); review counterexample (a P-divisible kernel, d_t = (4/5)^t, with non-monotone G²) | G² non-monotonicity is the proposal's prediction and does not by itself establish 𝒩 > 0 or P-indivisibility; step 5 uses the total-variation distance of the visible population laws; revival measure 75% of 𝒩_max |
| ch15 :144, :146, :220 (added) | "C3 marginality"; "a capacity margin does not produce revival" | report finding 2 (r = N_H/N_V is not Main's C3 quantity) | "hidden capacity" / "marginal hidden capacity"; "does not by itself produce revival" |
| ch15 :204, :206, :216, :222, :226, :228, :246, :248, :258 (E12, E13, E18–E22) | attribution; non-Markovianity; label | — | Proposal; revival; relabelled |
| glossary :29 (G2), :115 → :125 (G1) | label; "fully representable"; entry "Partially-quantum regime" | ch18 §18.3 | Relabelled; entry renamed, re-sorted, and carrying the definition (d the total variation of the visible population laws) |
| ch18 :72, ch13 :134 (added) | "the the"; "quantified by the Breuer–Laine–Piilo measure" | — | Typo fixed; "quantified in the literature by" |
| ch09 :283 (added), :285, :287 (X1, X2) | "C3 … marginally satisfied" for biological partitions; "when N_H/N_V is finite" partial revival, with "fully Markovian and fully P-indivisible"; label | ch13 :138 (B9); ch15 :144, :154 (F → 1 for r ≫ 1) | Marginal hidden capacity; C3 "can be satisfied" with finite capacity, and biology is not placed at marginal capacity; partial revival predicted at marginal capacity (N_H/N_V ∼ 1); proposal attribution; relabelled |
| ch01 :263 (X3 and added) | label; "probe of C3 marginality"; "biological systems approaching marginal C3" | ch13 :138 (B9) | Relabelled; marginal hidden capacity; "the proposal's conjecture for biological systems" |
| appendix-a :170, :213 (X4 and added) | "no analog in standard QM"; "Capacity-controlled non-Markovianity" | ch18 :78 | Origin and form are the proposal's own; "Capacity-controlled revival" |
| appendix-c :277 (added) | "marginal C3 capacity" | finding 2 | "marginal hidden capacity" |
| readers-guide :53, ch19 :356 | label | — | Relabelled |

## Left unchanged

- **Excluded to other units, as instructed:** ch15 :103, :112, :114; glossary :91, :105; Main :334; ch01 :225 and
  appendix-c :62. The last two still read "partially-quantum regime", and appendix-c :62 also reads
  "capacity-controlled non-Markovianity" and "C3 is marginally satisfied". Report X5 (appendix-c :62) is therefore
  not applied.
- **Not assigned to SC-22 by the report:** the "specific algebraic predictions" at ch13 :142, :146 and :170. The
  label is relabelled there, and the claim is unchanged. The same family also appears at ch13 :136 (the "positivity
  and completeness conditions" signature), which is unchanged. At ch18 :94 only the subject is narrowed, to "a
  memoryless (divisible) density-matrix description"; the algebraic-constraint claim itself is unchanged.
- The SM taste-loop symbol 𝒩 = 1/9 (SM §7.2, ch06 :179) still collides with the revival measure. This is not
  renamed.
- ch15 :156 (F(r) motivation, "not packaged") and the L ≈ 5 overlap between ch15 :112 and :164 are unchanged.

## Re-grep (`papers/*.md`, `book/*.md`, chapters / FULL / papers)

| Pattern | Count |
|---|---|
| `partial(ly)?[- ]quantum` | 2 / 2 / 0, the excluded ch01 :225 and appendix-c :62 |
| `restricted quantum-statistical` | 57 / 57 / 0 |
| `intermediate[- ]backflow`, `maximal[- ]backflow`, `weak backflow`, `P-indivisibility measure`, `non-Markovianity measure`, `fully[- ]quantum regime`, `memory-backflow`, `backflow strength`, `depends non-monotonically` | 0 / 0 / 0 |
| `capacity-controlled non-Markovianity` | 1 / 1 / 0, the excluded appendix-c :62 |
| `C3 marginality`, `marginal C3`, `marginally satisfied` (𝒩 sense) | 1 / 1 / 0, the excluded appendix-c :62 |
| `revival measure` | 15 / 15 / 0 |

## Checks

- The probes are landed at `verification/audits/manuscript/intro-corpus-audit-20261026/tracks/SC22-N-regime/`,
  byte-identical to their blobs at `42bbd33c` (`git hash-object`):
  - `regime_exact.py` `f65a9286e82e2ecb50a583c820012d02544057af`, `.out` `9674f0a296a7e6ef90e8a36b8f406e6501cdf600`;
  - `blp_unbounded.py` `418a96ed8616476d9a88c5d74a8136ce7e8c8f1a`, `.out` `cbed77dbe1078d68b5443258c61b1c6026dc6a18`;
  - `enum_window.py` `53581d5088845c7c179b93ba68d7f204e19580ce`, `.out` `eb2d93d08e319eb7284bfab2c9a2833b2a0cda80`.
- Regenerate them from that directory with `python3 -I -B regime_exact.py`, `python3 -I -B blp_unbounded.py .` and
  `python3 -I -B enum_window.py .`. Each prints its `.out` exactly; this was confirmed from a scratch copy.
- `enum_window.py` gives the exhaustive counts behind "C1–C4 give memory without fixing 𝒩". Among models with a gap
  inside the window, R_W = 0 in 8 of 12 at (2,2), in 540 of 576 at (2,3) and in 192 of 616 at (3,2). R_W > 0 never
  occurs without a gap.
- Controls are green. K1: the Markov powers are P-divisible with R = 0. K2: (I, J/2, I) is P-indivisible with R = 1.
  K3: the tape-and-ledger coin has no gap.
- The outputs used in the prose:
  - Rows B and C: XOR, alone and with an idle register (M = 2, 8), has a gap at order 1 and R = 0 on {0..2}.
  - Row E: the static bath has R = 0 on {0..2}.
  - F(r) is strictly increasing on [0, 1], with F(1) = 1.
  - The minimal model's cumulative sum is 2/3, 4/3, 10/3 and 20/3 at K = 2, 4, 10, 20, while the peak stays 2/3.
    This supports the stated periodicity argument; the numbers are not quoted in the prose.
- `sh ./build.sh --book`: OK, 558 pages, the same count as before.
- Release gate: every step passes except `lean-axioms`, which fails because there is no lake toolchain locally.
  `edge_rigidity_probe.py` passes.
- Scans of the added lines found no hits for the §A.32/§A.33 phrase family. The only new capitalized token is
  `FULL`, in this record. The scan for tokens, keys, URLs, IP addresses and e-mail addresses also found nothing.
