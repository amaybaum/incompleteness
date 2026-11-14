# QPHEN Phase 1 r6: dispositions of `review/REVIEW-PHASE1-r5.md` (`fa7fd9fe…`)

## Scope and standing

- Paper only and model-written. There are no repository, git or GitHub writes. Owner comments on #1210 were read
  (read-only) to verify the quotations used.
- No computation is run on any OI mechanism. The one new check, `review/probes/p11_r6_checks.py`, is an exact check of
  paper claims on generic objects ("Allowed: generic checks", #1210 c.6739250392, owner, 2026-11-09). It imports no
  earlier probe.
- Q-C2-1's D19–D23 remain separate. No freeze, dispatch, construction or implementation approval follows from this
  revision.
- **Inputs.**
  - The r5 review, sha256 `fa7fd9fe7726b1b9f50d5c5280c9700588fea857dbaf40bcbe258992985dedfe` (verified before
    reading), verdict REVISE (narrow), and its probe `p10_r5rev_checks.py` (`ca3607952c244aa7…`). p10 was re-run with
    `python3 -I` from a separate directory: exit 0, output byte-identical to `p10_r5rev_checks.out` (`7ec5713f…`).
  - The owner's added check, relayed by the coordinator (amaybaum, session chat, 2026-11-09): "preserve the
    distinction between necessary physical conditions and assumptions built into the design". It is not a GitHub
    record, so it is cited here and not in the specifications; the specification changes it prompted (N14–N20) stand
    on their own sources.
  - The owner rules still in force (last section).
- **Corpus check.** `git fetch origin main` (no depth, gc or prune): `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`.
  `git show fd539e15:papers/Main.md` equals `main_fd.md` (`6144cd4a…`). Every finding was checked against that text
  before it was applied: Main:56, :406-412, :421, :652, :726 (items (iv)–(xiii)); Substratum:48, :98, :100,
  :270-272, :481; SM:240; AP1 `DESIGN.md`:280-362. The owner records c.6739311717 (amaybaum, 2026-11-09T11:48:47Z),
  c.6739286623 (11:47:25Z) and c.6738866690 (11:25:06Z) were read and match the review's quotations.
- **The r5 texts** are copied unchanged into `r5/`:

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `e231a795508769cec7645f05931b1ce04e418bbd69acd8802f794a0bec8add71` |
  | `QX4-INCOMPATIBILITY-LG.md` | `7f4cd21d02a0dbf7946c4d481c6140f7e3c6df053a5096b8fd589de123a7b5a5` |
  | `QX6-BELL-CHSH.md` | `9e9c0d02c48dfc748baa7fade7a271c938e8ae817457ec635a3076cec774e4ea` |
  | `SHARED-MECHANISM.md` | `a72067015789371a087517d92f71a5fcc654770d1d3f105e217eda6fcba2cc4d` |
  | `DISPOSITIONS-r5.md` | `01ef37655352c0d8dc0cdaf4512fee1df74ec5183267dd1982177addacbaa28c` |

  These match the hashes the r5 review lists. `DISPOSITIONS-r5.md` is a record and is not edited.

## The new check

`p11_r6_checks.py` (pure Python, exact integer and `Fraction` arithmetic; run with `python3 -I` from a separate
directory; exit 0; 11 of 11 checks pass; output `p11_r6_checks.out`):
1. **Q4-P19 (ii), N3.** `Sp(4, F_2)` is rebuilt by brute force over all 65,536 matrices (720 found), independently of
   the Gram-test and transvection constructions in p9 and p10. Of the 384 location-preserving affine-symplectic maps,
   288 have a meter write that depends on `c`, and every one changes `x` on some state with `c = 0`. Under the weak
   reading, maps that never change `x` on `c = 0` exist, the translation `m ← m + 1` among them. Statement (i)'s
   0 / 11,520 count is re-confirmed. This reproduces p10 (7) independently, so (ii) is X at its scope.
2. **B1, the SA-1(a) row.** The phase-space step `(a, b) ↦ (b, F b − a)` is symplectic iff `F = Fᵀ`, exhaustively
   for `(q, n) ∈ {(2, 2), (2, 3), (3, 2), (5, 2)}`. The symplectic counts, 8, 64, 27 and 125, equal the numbers of
   symmetric matrices, so the non-symmetric cases are present and fail (the control is not vacuous). A translation
   has identity linear part.
3. **N2.** Over all 256 deterministic `±1` response tables with two settings per wing, every table without
   remote-setting dependence has `|CHSH| ≤ 2`, and every table with `|CHSH| > 2` has remote-setting dependence.
4. **N15.** A point-mass preparation is no-signalling iff its table is local (256 tables). Countercontrol: the equal
   mixture of two signalling point masses (`A = w`, `B = w ⊕ xy`) is no-signalling with `S = 4`, so the point-mass
   restriction has content.

Checks 3 and 4 are by the writer only and are not independently reproduced, so Q6-P12 is entered as [A] with those
checks named, not as X.

## Blocker

| finding | verified against | change made (r6) |
| --- | --- | --- |
| **B1** (SHARED §9 column (ii) stronger than Main's posit ledger) | Main:726 (iv) "a standard but substantive epistemic postulate, not derived"; (v) "one conditional wearing three hats"; (vi) isotropy, E4; (vii) the affine part from first-difference gauge; (xiii) "the second-order form of the update, a posit of the selected lattice model, not derived", "stated relative to" (viii); Substratum:48 (uniqueness among "second-order reversible nearest-neighbor" rules given "center independence, isotropy, and linearity"); Substratum:270-272 ("an operational input …, not a theorem"); SM:240. The symmetry ⇔ symplecticity step: by hand (`MᵀJM = [[0, I], [−I, F − Fᵀ]]`) and p11 (2) | **N2 row**: column (ii) "no: a posit in Main", quoting Lemma 3 and posit (iv) "not derived", with (v)'s shared conditional; H-PREP clause kept. Standing "posit in Main (iv); application conditional on H-PREP". **MI row**: column (ii) adds that its motivation is the same open question as (v)'s mixing hypothesis and N2's typicality selection, "one conditional wearing three hats" (Main:726 (v)). **SA-1(a) row**: column (ii) "conditional on Main's posits for the selected lattice step": (xiii) on the site factorization (viii); (A4)/(xi); coefficient symmetry from isotropy (E4; (vi)); the affine part of (A5) in its first-difference form, an operational input, open. On these the coefficients are symmetric and the step symplectic (AP1; p11 (2)); the nearest-neighbour form rests also on (x); linearity beyond affine is not used. Standing "native element of the selected lattice model, conditional on those posits". **Propagation (§A.25)**: QX-3 R3.2's type "CS (close to native for `H` …)" becomes "CS (Main's posit (iv) for `H`, not derived; …)". The M15 row inherits the condition, as the review says. SHARED §7's `main`-references row adds Substratum:48, :98, :100, :270-272, Main:652, :726 and SM:240, which §9 now cites |

The two additions beyond the review's suggested wording, (viii) and (x), are in B1's scope: Main:726 states (xiii) "relative to" (viii), and the review itself names the nearest-neighbour premise as an input to Substratum:48's uniqueness. (x) is stated as what the nearest-neighbour form rests on, not as a condition of symplecticity, which p11 (2) shows does not need it.

## Must-fix nits

| finding | verified | change made (r6) |
| --- | --- | --- |
| **N1** ((D), (MI) omitted at A6.1 citations) | yes. Q6-P10's first bullet is false without (MI): Main:421 allows `S = 4` under measurement dependence | **SHARED Q6-P10** header "conditional on (D), (MI), and the design assumptions (L′) and (R)", and its first bullet "Under A6.1's hypotheses ((D), (MI), and the design assumptions (L′) and (R)), own-wing operations do not exceed 2". The same parenthesis at **QX-6 §8 item 2**, **QX-6 `A_6`**, **SHARED §4** controls (third item) and **SHARED §3** "Cross-wing dynamics" (first bullet). A grep for "(L′) and (R)" finds no other site citing A6.1 without "A6.1's hypotheses" or all four conditions |
| **N2** ("insufficient separation" equals every failure of (R)) | yes: as defined it is `d_{G_B}(B, R_A) ≤ T_A − t_B`, which is the failure of (R) | Both of the review's routes. **QX-6 §3.2**: insufficient separation is defined in the designed reference graph `G_ref` (the union over the ticks after `t_B` of the dependency graphs the design specifies; for OI the bounded-range reference graph of Main:414 without preparation-indexed edges); the third case is `d_{G_B} ≤ T_A − t_B < d_{G_ref}`, a path with an edge outside `G_ref`. **New SHARED Q6-P12** [A] derives M19's necessity directly: under (D), (MI) and the `⊥` rule, `|S| > 2` needs an outcome that depends on the remote setting at some `Ω` (A6.1 step 6 in contrapositive; p11 (3)); with (L′) and separation in `G_ref`, A6.1 then forces a `G_B`-path with an edge outside `G_ref`. **SHARED §3 "Counting"** (M19 item) and **§8.4**'s proved entry cite Q6-P12 in place of the old route |
| **N3** (Q4-P19's "records" too weak) | yes: the review's proof re-derived by hand (rows `c`, `x` vanish on the meter columns; the meter block is invertible since `ω(Me_m, Me_m′) = 1`; `(γ, β)B = 0`); p10 (7) re-run; p11 (1) reproduces 288 / 384 independently | **SHARED Q4-P19** restated in two parts: (i) the identity-on-`c = 0` statement and proof, unchanged in content; (ii) "a location-preserving map records occupation when its meter write depends on `c`; every location-preserving affine-symplectic map that records occupation changes `x` on some state with `c = 0`", with the review's proof, the 288 / 384 count, and the note that the weak reading does not give (ii). Evidence line adds the r5 review, p10 (7) and p11 (1). **QX-4 R4.9** cites (ii) in its strong wording, "on `F_2⁴`". T2 and A4.4 already use "acts on its silent branch" as `K_null ≠ id`, which (ii) now supports; unchanged |
| **N4** (Q4-P19 not propagated to M16) | yes: O1 (c.6738866690) prescribes "none identified (open)" only "wherever no QM-independent justification has been found" | **SHARED §1 M16**, **§2 M16 × QX-4** and **§9's null-result row**: in the affine-symplectic class every location-preserving coupling that records occupation is null-result invasive (Q4-P19 (ii), at its scope), so a detector coupling that is an SA-1(a) step has it on the SA-1(a) row's condition; none identified for non-affine couplings (open). §9 standing "a hypothesis under test (O1); **QM-only** for non-affine couplings". The §A.31 cautions are carried in the cell: conditional on SA-1(a)'s posits, only for couplings that are SA-1(a) steps, at Q4-P19's scope, and "this gives no QM-matching value by itself (A4.4)" |
| **N5** (M15 status wider than its support) | yes | **SHARED §1 M15**: "holds for location detectors in the affine-symplectic class (Q4-P19); for encoded meters AP1 §3.2 [W] (Q3-O5)". **Propagation**: §9's M15 row splits its column (ii) the same way |
| **N6** (QX-6 §7: "if any is missing") | yes, against QX-6 §9 | **QX-6 §7** first block states each consequence: R6.5 or R6.7 missing → `A_6` / `B_6-loc` (under their hypotheses) plus benchmarks; R6.8 missing → no Level-2 credit; R6.10 missing → no Level-3 credit, Level 2 not requiring it. R6.5 is labelled "presupposed by the protocol" (N17) |
| **N7** (QX-4 §7 item 3) | yes, against A4.4's Consequence | "under (H1), (H2) and (H4), to match the comparator protocol, it needs null-result invasiveness (A4.4)" |
| **N14** ("Every column needs") | yes: the support is `DESIGN-DS.md` §2 [D] only | **SHARED §3** "Every column uses, by the design of construction B:" |
| **N15** (restricted preparation class rests on a W record) | yes. The review's recovery argument re-derived and extended to the exact affine-hull form: no-signalling is linear in the preparation law, and under a point mass at `Ω` a deterministic outcome with a remote-setting-independent law has a remote-setting-independent value; p11 (4) checks it and its countercontrol | Recorded as **SHARED Q6-P12** (third bullet) [A]. **QX-6 §3.2**: "For Level 2 (§9), any such dependence must also be invisible …; under (D) and (MI), `|S| > 2` with complete-history no-signalling needs an admitted preparation class whose affine hull excludes the point mass at some `Ω` in the support (SHARED Q6-P12 [A]; prepared-pair-source §5 (W) …)". **QX-6 A6.4**: the same statement first, the W balance-map statements marked "open, SHARED Q6-O8"; "R6.9 must be some state restriction" becomes conditional on supplying R6.7 and meeting Level 2's no-signalling target. **QX-6 §8 item 4**: "For Level 2, under (D) and (MI), …" with the W statement marked open |
| **N16** ("must exclude PR-type sources") | yes: R6.10 is a Level-3 condition and a hypothesis under test | **QX-6 §8 item 4**: "For Level 3, the admitted class must also exclude PR-type sources (R6.10, a hypothesis under test)". **SHARED §3** H-SDC obstacle 4: "For Level 3, the rule must exclude PR-type responses (M20's Tsirelson half, a hypothesis under test; §9)" |
| **N17** (Bell prerequisites without their basis) | yes | **QX-6 §8 item 2**: "Under (D) and (MI), a Bell excess needs a cross-wing response; given the design assumptions it needs one through an edge outside the designed reference graph, which is R6.7 (H-Bell), open (SHARED Q6-P12)". **QX-6 A6.2 "For #1210"** and **SHARED §5 QX-6**: each prerequisite with its basis: R6.5 / M18 presupposed by the protocol (§1); R6.7 / M19 necessary for `|S| > 2` under (D) and (MI), and in H-Bell's form given the design assumptions; R6.8 / M20 a condition of Level-2 credit (§9). The review placed R6.7's necessity under (D), (MI), (L′) and (R)-separation; with N2's direct route, a cross-wing response is necessary under (D) and (MI) alone, and the design assumptions are needed only for its H-Bell form. Both layers are stated |
| **N18** (Obligation C "needed" without A6.2's premises) | yes, against A6.2's body | **QX-6 §8 item 6**, **SHARED §5 QX-6** first bullet and **SHARED §3 "Counting"** (M12): "when settings are identified as local read directions, since Clifford-class local operations then give `|S| ≤ 2` in QM itself (A6.2)". **Propagation**: §8.4's proved entry adds "with settings identified as local read directions" |

## Precision nits

| finding | verified | change made (r6) |
| --- | --- | --- |
| **N8** (Tsirelson: "none identified" omits conditional routes) | yes: Substratum:481 first sentence; Main:652 "one common tensor-product instrument category" not established. Boxworld (generalized no-signalling theory) is locally tomographic and contains PR boxes (L) | **SHARED §9 Tsirelson row**, column (ii): "open. Two conditional routes are on record, each on a premise with quantum structure: …"; boxworld; the Substratum:481 quotation kept. Standing unchanged (**QM-only**). **Propagation**: SHARED §1 M20 and QX-6 R6.10 read "no identified support other than agreement with QM or a premise with quantum structure" |
| **N9** (c.6739311717 missing from owner records) | yes; the comment was read (amaybaum, 2026-11-09T11:48:47Z) | Added, with its content, to **QX-3 §0**, and to the owner rows of **QX-3 §10** and **SHARED §7** |
| **N10** (§8 rule: "unless separately established") | yes, c.6739286623 | **SHARED §8 rules**: "… listed as open unless separately established" |
| **N11** (QX-4 §10 lacks R4.9's SHARED citations) | yes | **QX-4 §10** row: SHARED Q4-P15 and Q4-P19; the r4 review with p8; p9; the r5 review with p10; p11 |
| **N12** (`A_6`, `B_6-loc` expectations in no ledger list) | yes | **SHARED Q6-P10** adds "`A_6` and `B_6-loc`: `|S| ≤ 2`, for one-step settings under Main §3.3's hypotheses (Q6-P1), and for multi-tick settings under A6.1's hypotheses (Q6-P2)"; its evidence line adds Q6-P1 |
| **N13** (name the affine input in first-difference form) | yes; p10 (6) re-run; consistent with Substratum:272 and SM:240 | In B1's SA-1(a) cell: "the affine part of (A5), which amplitude-scale gauge yields in its first-difference form" |
| **N19** (`K₃ ≤ 1` control without the read model) | yes | **SHARED §4** controls: "`K₃ ≤ 1` with A4.1's read model, at one mode, …" |
| **N20** ("`G` must be C's …") | yes | **QX-4 §4**: "By the programme rule of one shared mechanism (#1210 requirement 1; SHARED §0), `G` is C's, QX-1's or QX-7's operation …" |

## Optional nits

- **ABL-G** (QX-4 §5): applied. "`≤ 1` with A4.1's read model at one mode, and at two modes under SA-1(c) or
  environment supplies", since A4.1(b) also contains `K₃ = 2`.
- **§A.31 method notes**: no change, as the review allows.

## Changes not traced to a finding

1. Housekeeping from the instruction to revise in place as r6 and keep r5 under `r5/`: titles "(draft r6)";
   "§0 (r6)" and "specifications (r6)"; §0 "Revisions" pointers name `r5/` and `DISPOSITIONS-r6.md`; the §0 probe
   ranges become "P1–P11" (QX-4, SHARED) and "P1–P6 and P11" (QX-6), since those files now cite p10 or p11; QX-3
   keeps "P1–P6".
2. §A.42 item 8 rows for the new citations: SHARED §7 rows for the r5 review with p10 and for p11; QX-6 §11 row for
   SHARED Q6-P12 with p11. SHARED §8's X rule names P10 (reviewer) and P11 (writer).
3. **QX-4 §4, "Shared with QX-3"** (own pass under the owner's necessary-against-designed check). "One routing map has
   to give QX-3's exclusivity and QX-4's INM with null-result invasiveness, and has to keep QX-0's complementarity"
   rests on the programme rule and on the comparator target, and "has to" was outside the review's grep of "needs",
   "must", "required" and "necessary". It now reads "Under the same programme rule, one routing map gives … with
   null-result invasiveness if INM is to match the comparator protocol (R4.10), and keeps QX-0's complementarity as
   A3.2's control". A grep for "has to" and "have to" finds no other site.
4. The propagation edits listed in the tables above (QX-3 R3.2; §9's M15 row; M20 and R6.10; §8.4's M12 entry).

Every added line was re-scanned for necessity words ("needs", "must", "required", "requires", "necessary"): each is
proved under stated hypotheses, or is labelled as a protocol presupposition, a Level-2 or Level-3 target, or a
programme rule.

## Checked and left unchanged

- The EN type on M1, R3.1, R4.3 and R4.4 is the owner's category for elements native to the selected lattice model,
  which matches B1's standing "native element of the selected lattice model, conditional on those posits".
- QX-6 R6.2 states (R) on `G_B`. As the r4 review remarked, that is an assumption the design makes about the
  dynamics, and H-Bell is a failure of it; the new `G_ref` definition in §3.2 concerns only what the design itself
  guarantees.
- T2 and A4.4 (see N3); QX-6 A6.2's title and the M12 × QX-6 cell (they carry A6.1's hypotheses, and A6.2's body
  states the identification).

## Register

A scan of every added line (§A.32, §A.33) finds four-letter capitals only in identifiers (`NCONS`, `MECH-OPEN`,
`H-PREP`, `CHSH`, file names) and no history phrase, reader instruction or self-assessment. No revision narration was
added to the specification bodies.

## The owner rules still in force

| rule | status in r6 |
| --- | --- |
| The three-column restrictions table; column (iii) never supports column (ii) | B1 brings column (ii) into line with Main's posit ledger for N2, MI and SA-1(a). N4's and N8's column (ii) entries cite Q4-P19 and the corpus routes, never column (iii) |
| A6.1 conditional on its hypotheses; (L′) and (R) design assumptions; (D) and (MI) carried at every citation | N1; Q6-P12 states its own hypotheses |
| Disproved entries carry membership lines; narrower claims stay open unless separately established | all 11 unchanged; N10 adds the owner's qualifier |
| Summary and dependency-table conclusions match the scope and status of their proofs | N1–N7, N12, and the propagation edits |
| Necessary physical conditions kept distinct from design assumptions | N14–N20 and own-pass item 3 |
| Exact generic checks labelled; probe-only results computation-supported; no computation on an OI mechanism | p11 acts on generic `F_2`, `Z_q` matrices and response tables only. Q4-P19 (ii) has a paper proof and two independent probes (X); Q6-P12 has a paper proof and one writer probe, entered as A with the checks named |
| Configuration vs encoded carriers; mathematically available vs derived from OI; coherent mixing vs full probability and composition rules | M15 and M16 now separate location detectors from encoded meters (N4, N5); B1 separates Main's posits from derived content |
| No implied D19–D23 decisions, freeze, dispatch or construction | none added; all rules remain outlines |

## Refusals and deviations

- **None refused.**
- **N2.** Both of the review's routes are applied: the `G_ref` definition makes QX-6 §3.2's case list a partition, and
  the direct route (Q6-P12) carries the necessity statement without depending on it.
- **N15.** The conclusion is stated in the exact form the argument gives: the affine hull of the admitted class
  excludes the point mass at some `Ω` in the support.
- **N17.** R6.7's basis is stated in two layers (see the N17 row), which is more precise than the review's single
  condition list.

## r6 file hashes (sha256)

| file | sha256 |
| --- | --- |
| `QX3-ANTIBUNCHING.md` | `01f8a44d64334d01923ee6c499dd4f59df9be341c0035148573e35bcd6e421da` |
| `QX4-INCOMPATIBILITY-LG.md` | `df4def7192b7d8226eb339330fc764a91a2ec062d42aa58748e24afae6647e0e` |
| `QX6-BELL-CHSH.md` | `1243cea4e052a48730969f9a6f2f161ea67754a502088af396fa2ac78a9d2874` |
| `SHARED-MECHANISM.md` | `67b3f5b54f25fdba3f65dedb9346c892d8833223711b8edb03f8352c2ea66327` |
| `review/probes/p11_r6_checks.py` | `d8026111baa43581ee77762b34508ee2d875b83cdb954f9950bf8665d80569f3` |
| `review/probes/p11_r6_checks.out` | `bc9bc1e4e86cbddadad409c9d2ce6c4fb70d972a17b7386d43056c19fbc0c7f8` |
