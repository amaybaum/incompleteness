# QPHEN Phase 1 r3: dispositions of `review/REVIEW-PHASE1-r2.md` (`47af406f…`) and of the owner's r3 requirements

## Scope and standing

- Paper only and model-written. No mechanism is built and no criterion is frozen. Nothing here touches the repository,
  git or GitHub.
- The computations are small exact probes of paper claims, `review/probes/p5_r3_*.py`. None imports P1–P4.
- Q-C2-1's D19–D23 decisions are separate and are not addressed or implied here. No freeze, dispatch or
  implementation approval follows from this revision.
- **Inputs.**
  - The r2 review, sha256 `47af406f4541df13ea3707c632898676005e44552ee5916d89488fc7afd18b97`.
  - The owner's r3 requirements, the acceptance criteria and the three-questions addition. These were given in chat on
    2026-11-09 and relayed verbatim by the coordinator. They are not on a recorded Issue comment (see owner question
    O3 below).
  - The D-sheet quote "Passing a consistency check must not be presented as a new derivation" (#1169 c.6735014875,
    amaybaum, 2026-11-09T07:52:50Z), as verified by the r2 reviewer.
- **The r2 texts** are copied unchanged into `r2/`:

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `26ba2167…` |
  | `QX4-INCOMPATIBILITY-LG.md` | `47fb4202…` |
  | `QX6-BELL-CHSH.md` | `9d68526c…` |
  | `SHARED-MECHANISM.md` | `7d10092a…` |
  | `DISPOSITIONS-r2.md` | `064df364…` |

  These match the hashes the r2 review lists.

## Writer's probes (exact unless stated)

| probe | sha256 | result |
| --- | --- | --- |
| `p5_r3_a61.py` | `801f1a55729600bf…` | (1) the one-tick composite fails (L′) and gives `S = 4`; with the single-graph (R) of r2, `d_G = 1 > 0`. (2) The split over three ticks satisfies (L′) and fails (R) (`d_{G_B} = 2 = T_A − t_B`), with `S = 4`. (3) Random constructions satisfying (D) and (L′): 2,734 wing-cases with (R), 0 with remote dependence; 2,524 without (R), 642 with dependence. (4) Main's one-step form satisfies (L′) at every tick. (5) `d_φ = ∞`, single-graph `d = 2 ≤ k = 2`, and the readout is `b`-independent |
| `p5_r3_lg.py` | `72d6a4e5c189357c…` | (1) copy and reciprocal couplings affine; occupation-conditional kick not. (2) `C₁₂ = cos 2θ`. (3) `G = (I⊗H)·SWAP·CNOT_{m→c}`: `K₃ = cos β + sin β`, so `√2` and `7/5`. (3′) `G = (I⊗H)·CNOT_{m→c}`, carrier `|+⟩`, non-stabilizer mediator: `K₃ = cos β + sin β`. Enumeration of all 11,520 two-qubit Cliffords: with product stabilizer preparations every correlator lies in `{0, ±1}` and the maximum `K₃` is 1. With a stabilizer carrier and a 7×6 ancilla grid, the grid maximum is `(1 + √3)/2`. (4) The flip instrument with `G = X` gives `K₃ = 3`; the mixture gives `K₃ = 6w − 3`, so `2` at `w = 5/6`. (5) Numerical evidence only: the Lüders maximum found is `1.49999` at dimension 2 and `1.4951` at dimension 4 |
| `p5_r3_ghz.py` | `a7ca4df2ceef881e…` | GHZ-1: `+1, −1, −1, −1`, Mermin 4, local maximum 2. The nonzero `X/Z` strings are `ZZI`, `IZZ`, `ZIZ` and `XXX`, all satisfied by `x_i = z_i = +1`. GHZ-2: `+1, +1, +1, −1`, sum 4, local maximum 2. There are 32 local-Clifford maps; one is `SH ⊗ SH ⊗ SHS`, up to the phase `e^{iπ/4}` |
| `p5_r3_qx3.py` | `66fc94735be10ea6…` | `L` equals Fredkin on `c₁ + c₂ = 1`, with `α = 0`. Counts: 6 globally weight-preserving affine bijections, all permutations; 48 affine ready-support routers. Fredkin is weight-preserving and not affine. All 8 globally weight-preserving routers on `F_2³` are non-affine |

Full hashes are in the final table at the end of this file.

## Blockers

| finding | change made (r3) |
| --- | --- |
| **R2-B1** (A6.1 false as worded) | **QX6 A6.1** is rewritten as a complete proof under the hypotheses below. The proof's steps: one-tick locality from Main:364's dependency definition, with finite `V`; `Δ_t = ∅` before `t_B`; `Δ_{t_B} ⊆ B` by (L′); induction `Δ_t ⊆ N^{G_B}_{t−t_B}(B)`; readout disjoint by (R); response functions of `Ω` by (MI); the pointwise CHSH bound. The writer's probe P5-A61 adds three checks. A table checks every hypothesis against Main:364-389, quoted, and finds Main's one-step form satisfies all of them. **The P4 counterexample is kept** as SHARED §8 Q6-D1, with the r2 hypothesis set stated. **Propagation:** QX6 §1 validation layer, §3.2 escape list, R6.4, the consequence paragraph, §8 items 2 and 7, §11; SHARED §3 and §4 controls; SHARED §8 Q6-P2, Q6-P3, Q6-D1 |
| **R2-B2** (Leggett–Garg protocol class) | **QX4.** The §2 heading becomes "Lüders instruments unless another instrument is named". Line 76 is replaced: `3/2` is the Lüders bound (Budroni–Emary, L, not read first-hand, with numerical evidence from P5-LG), measure-and-reprepare gives `K₃ = 3` and `2` (P5-LG, exact), and the von Neumann degenerate case is cited (L, not read first-hand). The comparator protocol is declared. The INM sentence names the Lüders update. **The five sites:** A4.1(b) (line 129) says "exceeds the Lüders bound … does not exceed what QM reaches with other instruments"; ABL-SA1c (line 251) says "above the comparator protocol's Lüders bound"; §7 item 2 (line 301) gives the same; §8 (line 322) says "lies above the comparator protocol's Lüders bound … reported, not credited". A4.4, ABL-NULL and the Consequence name the comparator protocol. **SHARED:** T9 is restated, and T2 names the protocol. QX6's Tsirelson row is reworded to drop "supra-quantum" and name the strategy class (owner criterion 3). "supra-quantum" and "QM-incompatible" remain only inside SHARED §8 Q4-D4, as the quoted refuted claim |
| **R2-B3** (agreement with QM supporting SA-1(c)) | **SHARED T9** keeps the fact only, and adds: "This is not a justification of SA-1(c), whose status remains posited, not derived (AP1:344-350; §9)". AW-QX4-1 is dropped from T9's source column. **SHARED M3 × QX-4** now reads "R (backaction)". **QX4 AW-QX4-1** adds that agreement is a consistency result (§A.23), not a justification. It counts as a §A.29 consequence only if SA-1(c) is shown not to have been fitted to it, and SA-1(c) has no reason independent of QM on record. **QX4 Q4-4** adds: "A proof would establish a property of SA-1(c). It would not justify SA-1(c)." **QX6 R6.9 and A6.4** add that a class fixed only by the balance equations is fitted to no-signalling, and is creditable only if fixed in advance by an independent principle with a consequence of its own (§A.29) |
| **R2-B4** (GHZ protocols) | **QX6 §2.** The GHZ table row now points to a new block naming two protocols. GHZ-1 gives the state `(|000⟩+|111⟩)/√2`, per-qubit `X/Y` bases, `XXX`, `XYY`, `YXY`, `YYX` with `+1, −1, −1, −1`, Mermin 4 against local maximum 2, and the `X/Z` scope note. GHZ-2 gives `CZ₁₂CZ₁₃CZ₂₃|+++⟩`, per-qubit `X/Z` bases, `XZZ`, `ZXZ`, `ZZX`, `XXX` with `+1, +1, +1, −1`, sum 4 against local maximum 2, and the optional local-Clifford map (P5-GHZ). The block states that an `X/Z`-only access class can pose only GHZ-2. **SHARED M11 × QX-6** gains "on the triangle graph state, protocol GHZ-2" |
| **R2-B5** (ledger) | **SHARED §8**, new: a claim-status ledger with per-spec sections, each with separate proved, disproved and open lists, the §A.34 directions separate, and rules stating how W/D-only, expectation and decision-tree claims are classified. A "Claim status" pointer is added to each spec's §0 |
| **R2-B6** (R4.9's false sentence) | **QX4 R4.9.** The sentence is replaced: the copy coupling `m ← m + c` and the reciprocal coupling (unconditional kick `x ← x + m′`) are affine; the kick acts on both branches, so the coupling is null-result invasive (A4.4); the occupation-conditional kick `x ← x + c·m′` is not affine. No non-affinity requirement is added. The refuted sentence is SHARED §8 Q4-D3 |

## Nits

| finding | change made (r3) |
| --- | --- |
| **R2-N1** (A4.1(c) hypotheses) | **QX4 A4.1(c)** states the hypotheses: N2 uniform-coset laws in the affine class, and stabilizer preparations of every mode, ancillas and mediators included, with Lüders `Z` reads in the Clifford class. It gives the `cos 2θ` counterexample (P5-LG, exact). **The review's open question, whether a QM-matching violation then needs a non-Clifford `G`, is resolved by an exact probe: no.** The two-qubit Clifford `G = (I⊗H)·CNOT_{m→c}`, with carrier `|+⟩` and mediator Bloch vector `(sin β, 0, cos β)`, gives `K₃ = cos β + sin β`, which is `√2` and `7/5`. A carrier-side variant gives the same. **Necessary propagation**, since these statements relied on the unscoped A4.1(c): A4.2 (now scoped to one mode), ABL-G, the §6 C-NONSTABILIZER branch and §7 item 2 in QX4; the SHARED M12 × QX-4 cell and §5's QX-4 row; SHARED §8 Q4-P3, Q4-P4, Q4-D5, Q4-D6 and Q4-O2. **This is new content, and the reviewer should check it** |
| **R2-N2** (`h > 0`) | **QX6 §3.** The sentence now reads "at every `η` and every herald rate `h > 0` (eq. (11) and the text below it)", checked against the record at `fd539e15` |
| **R2-N3** (injective identification) | **QX6 §3, Theorem NC.** The sentence now reads "Under an injective identification (R1^⊗n, or R-W at odd `q`) with spanning reads". The citation lines are corrected to M2D:65-71 for the quoted sentence, Theorem NC at :483-497 and Corollary NC-B at :509-516, checked at `fd539e15` |
| **R2-N4** (renumbering) | **Undone.** Q6-4 is again HB-1's question. The `⊥`-rule question takes the new identifier Q6-5, and QX6 §11's #1060 row cites Q6-4 again |
| **R2-N5** (r2 understated its diff) | `DISPOSITIONS-r2.md` is a record and is left unchanged. The r2 changes it did not list were the R4.9 sentence, the dropped `h > 0` and "injective identification" hypotheses, the Q6-4 → Q6-5 renumbering, and widespread restyling of prose into bullets. The first three are corrected above (R2-B6, R2-N2, R2-N3, R2-N4). The restyling is not reverted: the reviewer found no content change in it, and reverting it would be a further unrelated change. r3 adds no restyling. Every r3 edit is listed in this file |
| **R2-N6** (Q4-4 caveat) | Done under R2-B3 (QX4 Q4-4 and AW-QX4-1) |
| **R2-N7** (`t_B`) | **QX6 A6.1 (L′).** `t_B` is defined as the earliest tick at which any value of `b` acts, and `t_A` likewise |

## Owner requirements 1–4 (chat, 2026-11-09)

| requirement | change made (r3) |
| --- | --- |
| 1. GHZ state and measurement bases | R2-B4 above. Both forms are named with state, bases, operators and values. An `X/Z`-only access class can pose GHZ-2 only. SHARED M11 is qualified "on the triangle graph state" |
| 2a. Antibunching: nonlinear dynamics not established as necessary | **QX3 A3.1(d)** adds: non-affine dynamics is not established as necessary for antibunching; a router must be non-affine under `NCONS_global` and need not be under `NCONS_ready`. Which additional physical constraints, if any, make non-affinity necessary is open, and no OI principle with a reason independent of QM is identified that requires `NCONS_global` (SHARED §9). The framing is a question (Q3-2; SHARED §8 Q3-O2), not a conclusion |
| 2b. Leggett–Garg: `3/2` is the Lüders bound | R2-B2 above. Every comparison names the comparator protocol. Measure-and-reprepare values `K₃ = 3` and `2` are stated, with exact examples. Budroni–Emary is marked "L, not read first-hand" |
| 3. Proved / disproved / open; explicit counterexamples | SHARED §8 (R2-B5). Every one of the six required disproved items is linked to its counterexample: Q3-D1 (map `L`), Q6-D2 (triangle graph state), Q4-D1 (sharp-mediator witness without (H2)), Q4-D2 (`A_4: K₃ ≤ 1`; the same witness), Q6-D1 (A6.1 under the r2 hypothesis set; P4(1)) and Q4-D3 (R4.9's r2 sentence; P4(2)). The ledger also lists Q4-D4 to Q4-D7 and Q6-D3 |
| 4. No restrictions chosen to force agreement with QM | R2-B3 above, plus SHARED §9 (next table) |

## Owner acceptance criteria and the three-questions addition (chat, 2026-11-09)

| criterion | change made (r3) |
| --- | --- |
| Bell locality: tighter condition, proved lemma, Main checked, counterexample kept | R2-B1 above. The proof is complete. (R) is measured in `G_B = ⋃_{t > t_B} G_t`, so that Main's (iii) is exactly an instance, a choice P5-A61(5) motivates. **Status rule:** SHARED §8 Q6-P2 lists A6.1 as proved [A, complete proof, Main checked, unreviewed]. The entry moves to open, with the gap stated, if the r3 review finds a gap in the proof or the Main check |
| GHZ: both formulations with exact states and predictions | R2-B4 above |
| Leggett–Garg: every comparison qualified; no "supra-quantum" for exceeding `1.5` | R2-B2 above |
| Evidence ledger: every substantive claim classified; six disproved items linked | SHARED §8. A whole-text pass for the ledger found two carried-over sentences in QX4 that overstate their direction. They are corrected: (a) §1: "`P_succ > 3/4` with parity-obliviousness is equivalent to preparation contextuality" now states the proved direction only (§A.34; SHARED §8 Q4-P13, Q4-O7); (b) §2: "NSIT fails whenever the `t₂` read does not commute with the evolved `Q₃`" now says "for some preparation" (SHARED §8 Q4-P11; the unqualified reading is Q4-D7, counterexample: the maximally mixed preparation) |
| Independent physical justification; three separate questions | **SHARED §9**, new. A table of 22 restrictions, with columns (i) well-defined, (ii) follows from independently justified OI principles, and (iii) reproduces the relevant QM predictions (comparator), and a rule that (iii) is never cited for (ii). Sources are AP1:282-349 and :415-421, Main:44, :50, :56, :362-414, Substratum:48, :98, :100, :467, :481, and `DECISIONS.md` D15. No justification is supplied where the corpus has none. **SA-1(c)**, null-result invasiveness (M16, R4.10) and Tsirelson soundness (R6.10, M20) are marked **QM-only**: hypotheses under test, not requirements. Their type cells in SHARED §1 (M16, M20) and QX6 R6.10 say so |

## Changes not traced to a review finding

Each change below is traced to the coordinator's instructions or to an owner requirement. None is restyling.
1. **Titles and version labels.** "(draft r2)" becomes "(draft r3)", and "`QX3-ANTIBUNCHING.md` §0 (r2)" and "(r2)
   specifications" become "(r3)". Traced to the instruction to revise in place as r3.
2. **Spec §0 "Revisions" bullets.** These are reduced to "Earlier texts are kept under `r1/` and `r2/`. The revision
   record is `DISPOSITIONS-r3.md`", with the two review files named in QX3. Traced to the coordinator's instruction
   that revision history lives only in this file.
3. **Spec §0 "Claim status" pointers** to SHARED §8 and §9 (owner requirement 3; acceptance criteria 4 and 5).
4. **Reference-table rows** for the r2 review, P4 and the P5 probes, M2D's lines and §9's sources (§A.42 item 8
   tracing of the new citations).

Optional items not taken:
- The review's strengthening of A3.1(c) to field-cell weight. It was optional, and nothing depends on it.

## Findings refused or unresolved

- **None refused.**
- **Unresolved, and stated as open in SHARED §8:**
  - AW-QX4-1 beyond two modes (Q4-O1);
  - construction B's value under C-NONSTABILIZER (Q4-O2);
  - every MECH-OPEN row;
  - H-Bell (Q6-O1);
  - R6.9's masking (Q6-O4);
  - W3's classical status (Q3-O3);
  - L-CLICK's typing (Q3-O4).

## New points for the reviewer and the owner

- **A4.1(c) and A4.2 (new, exact).** With one further mode, a two-qubit Clifford `G` and one non-stabilizer
  preparation give `K₃ = √2` under the comparator protocol. So "C-NONSTABILIZER gives no QM-matching value" holds at
  one mode only, and QX-4c's dependence on Obligation C holds only with stabilizer preparations.
- **SA-1(c) has no reason independent of QM in the corpus.** AP1:347-349 names closure and the E-AR obstruction.
  Closure is a consistency property, and E-AR is an agreement-with-QM reason. In §9, SA-1(c) is therefore QM-only.
- **The G_B choice.** With one graph containing the setting tick's edges, A6.1 would not contain Main's theorem in
  every case (P5-A61(5)). The per-tick union after `t_B` fixes this.

## Owner questions (new)

- **O1.** Should the QM-only restrictions in SHARED §9 (SA-1(c), M16, R6.10) be carried into #1210's dependency table
  as hypotheses under test? Options: (a) yes; (b) record in the specifications only.
- **O2.** Does the new identifier Q6-5 for the `⊥`-rule question stand? Q6-4 is restored to HB-1.
- **O3.** The r3 requirements were given in chat. Should they be recorded on #1210, so that the specifications can
  quote them with author and time (§A.42 item 7)? At present they are cited only in this file, as relayed by the
  coordinator.

## r3 file hashes (sha256)

| file | sha256 |
| --- | --- |
| `QX3-ANTIBUNCHING.md` | `4ea39322ec363331653ae79d9623ac5be5548d8a11147e0be0545535109718de` |
| `QX4-INCOMPATIBILITY-LG.md` | `866a6f2aeae4e3946b61a2ded9bf043689c0843c709b86e6099e8cc6e70badd6` |
| `QX6-BELL-CHSH.md` | `04882cc25af134768257aa4fa6c83412ecd79868010d3be938f50f1c9cb07c69` |
| `SHARED-MECHANISM.md` | `6537031aa829965218bbd1424d5342917674d64683defafa97c74b64845280fd` |
| `review/probes/p5_r3_a61.py` | `801f1a55729600bff06c73de82049976fe4eaa99e100cf4e458fe04f616af392` |
| `review/probes/p5_r3_lg.py` | `72d6a4e5c189357c0a7b71533189868ffbb4530207e055b45c87df4c35006397` |
| `review/probes/p5_r3_ghz.py` | `a7ca4df2ceef881e55a5029a4e40a177baf530959c975e65a47bc4d568607799` |
| `review/probes/p5_r3_qx3.py` | `66fc94735be10ea6e4a63a98ffa687eb30feedcb0f6ed7ef5edee362c0e7ee32` |
