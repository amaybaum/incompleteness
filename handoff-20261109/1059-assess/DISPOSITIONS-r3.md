# ASSESS-1059 r3: dispositions of REVIEW-1059-r2

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Maps each finding of
`review/REVIEW-1059-r2.md` (sha256 `a262ad4fa246753747d7d5c14b16af61ad499166e486154e8b215258f8269710`,
REVISE, bounded) to its change in `ASSESS-1059.md` r3, from r2 = `r2/ASSESS-1059.md`
(`f99a4c3b2196bd035295b4bbff341459abb0f0c23a802621e4b26ba10b8120d2`, copied unchanged). Every
finding was checked against its source at `fd539e15` (`git show fd539e15:<path>` after
`git fetch origin main`) or against the cited draft before it was applied. No finding was refused.
Two source citations in the review were corrected while applying them (B1: QP:855 → QP:856–857;
nit 3: the glossary line was edited between `02009693` and `fd539e15`, its two relevant
sentences were not). This unit made no git or GitHub write; the only GitHub access was a read
of #1169 c.6740778880.

## Blockers

| Finding | Verified against | Disposition | Change in r3 |
|---|---|---|---|
| B1 (the 2 in R3-C is H-LIN's posited unitarity, not H-RF$_p$; U1's Kraus reason applies to unitaries; QP's √-insertion) | Reviewer D1, D2, D4 re-run (byte-identical); own check r3 E1 (column exponent = normalisation exponent: $\ell^2$→2, $\ell^1$→1, $\ell^3$→3, doubly stochastic → 1) and E3 ($\{w^{1/q}P_\sigma\}$ admissible only at $p=q$, complete only at $q=2$); QP:853–857 at `fd539e15` ("A uniform unknown supplied by a ready cell enters as coarse-grained Kraus operators `2^{−k/2} P_σ`"; the sentence is at QP:856–857, not :855); BORN-SRC-1 review 9(ii) (√T insertion, `src/914-bornsrc.txt`:333–334); Main:218 | Accepted, all three parts | (i) §3 column lemma restated for any column with ≥2 entries of modulus in $(0,1)$: the forced exponent is the column's own normalisation exponent, with the $\ell^2/\ell^1/\ell^3$ cases; the 2 is attributed to H-LIN's posited unitarity. R3-C column (ii) rewritten ("consistency condition between two posits"); §0 item 2 *for the exponent* bullet; §1 H-LIN (unitarity is the posited quadratic invariant) and H-RF$_p$ ("a power family with no preferred exponent"); §3 *Answer to Q1* first bullet and closing sentence; §4.4 (a-pow) bullet and §A.34 bullet; §4.5 (a-pow) row. (ii) R3-N last column: the Kraus family is R3-C's column lemma on its Stinespring dilation (its 2 being the posited completeness), and at QP:856–857 its amplitudes are square roots of counting weights, so its $p=2$ is the √-insertion circularity of BORN-SRC-1 review 9(ii), with N2's numbers. The r2 reason ("puts the exponent in by hand") is removed. (iii) §3 new paragraph *If the antecedent were supplied*, §5 NQ-1059 statement and *Yes* branch, §0 item 5: the positive branch bears on the exponent beyond R3-C only if the operation's quadratic invariant is derived rather than posited; stated as a condition, no premise added |
| B2 (necessity stated outside its hypotheses; H-LIN, H-RF$_p$ listed as necessary; R3-N column (ii) "stated interventions" not all unitary) | GR:260 ("monomial observable operators, a permutation of a diagonal", `bijectiveOperator_monomial`, `phaseOperator_monomial`); kernel `IsMonomial` (SubstratumInterface.lean:75: `permMatrix σ * diagonal d`, zeros allowed); QP:853–857 (scaled partial permutations, Kraus $2^{-k/2}P_\sigma$, registrations as 0/1 diagonals); r2 K2, reviewer D2 | Accepted | Form "Under H-LIN ∧ H-RF$_p$, a non-monomial admissible unitary in the read basis is necessary for any record to discriminate $p$ (R3-N)" used in §0 item 2, R3-N last column, §4.4 (a-pow) bullet, §4.5 (a-pow) row, §0 item 5, §5 *Yes* branch, OQ-1. H-LIN and H-RF$_p$ stated as the hypotheses of the necessity, not conditions it shows necessary (§4.4, R3-N). §0 item 2 and R3-N add that a selection of $p$ need not be record-based and that outside H-LIN weighted monomial Kraus families discriminate $p$. §5 *No* branch: "under H-LIN ∧ H-RF$_p$ no record of the stated access discriminates $p$ … not a no-go for a selection of $p$ that is not record-based, or for operations outside H-LIN" (replaces "(a-pow) lacks a necessary condition"). R3-N column (ii): antecedent holds for the unitary members of the stated access; registrations and the weighted Kraus operators are monomial, not unitary, outside H-LIN, and not covered by R3-N. §4.5 (a-pow) *Change* cell: "A conditional necessary condition for record discrimination located" |
| B3 (FI-1 extended beyond the configuration carrier; unscoped existence negative) | BRIDGE r4 §5.1 (FI-1 posed on $S\times{\rm Fin}\,1$; encoded maps without FI-1, QP:79–98, QP:846–877; MECH-2 $A_4\wr S_n$) [D]; §8 search scope | Accepted, reviewer's wording | R4 column (ii): "No native dense family is recorded on `main` (§8): on the configuration carrier one would need FI-1, which the stated access does not supply; on encoded carriers the operations in the records read form finite groups (stabilizer scope, QP:79–98; MECH-2's $A_4\wr S_n$, cited through BRIDGE §5.1 [D])". §4.5 (a-gen): "(on the configuration carrier, which needs FI-1)". §8's negatives list now reads "no native dense family recorded" |

## Nits

| Nit | Verified against | Disposition | Change in r3 |
|---|---|---|---|
| 1 (BRIDGE hash and status; SHM path) | sha256 of `bridge/r3/BRIDGE-UNIT1.md` = `ee1c83c0…8219`; current `bridge/BRIDGE-UNIT1.md` = r4 `4e97610d…85e2`; REVIEW-UNIT1-r3 `7a6a7f1c…cc27` (REVISE); REVIEW-UNIT1-r4 `e489fc19…2bc7` (REVISE); `qphen/r5/SHARED-MECHANISM.md` = `a7206701…cc4d`, `qphen/SHARED-MECHANISM.md` = `67b3f5b5…` (later) | Accepted; cites r4 as the coordinator directed | Header drafts list: BRIDGE = r4 `4e97610d…85e2`, reviewed REVISE in REVIEW-UNIT1-r4, every BRIDGE citation checked against r4; r3 `ee1c83c0…8219` with its REVISE review. SHM path → `qphen/r5/`. §6 F-b: `a5d7aad1…` replaced by r3 `ee1c83c0…8219` and r4 `4e97610d…85e2`; the r4 §6 "Born statistics" row reads the same (line 706). §4.1 gap 1: FI-1 "not supplied by the stated access and … open for the candidate sources BRIDGE lists (§5.1 Status [D])", matching r4's status |
| 2 (R3-C's unitary scope sufficient, not necessary; K1's $K$ not a contraction) | Reviewer D3 re-run; own r3 E2: exhaustive over 1034 support patterns ($n,m\le3$) that a non-monomial Kraus operator of a complete family gives a dilation column with ≥2 nonzero entries; instruments $\{|0\rangle\langle+|,|1\rangle\langle-|\}$, $\{|0\rangle\langle+|,|0\rangle\langle-|\}$ admissible only at $p=2$; unscaled $K$ has $K^\dagger K$ eigenvalue 2 | Accepted, extended (U1) | R3-C last column: unitary scope sufficient, not necessary; outside H-LIN a visited 2-normalised column or dilation column with ≥2 nonzero entries forces $p=2$. §3 *FI-1 and R3* bullet rewritten ("FI-1 entails R3-C's antecedent only for a unitary operator"; dilation case; $K$ "lies in no complete family … shows only that the predicates differ"). §0 item 2 FI-1 sentence. §4.4 §A.34 bullet and §6 F-b drop r2 K1 as a sufficiency counterexample |
| 3 (F-e locus; FULL mirror; CONFIRMING) | `git show fd539e15:book/glossary.md` l.21 and `…FULL.md` l.6604 (identical); Main:556 ("not an open choice at all"; "an operational question, not the exponent question of §3.1, and the two should not be conflated"); ch18:34; `git diff 02009693 fd539e15 -- book/glossary.md` (the line changed, both sentences unchanged); BORN-SRC-1 review finding 4 (`src/914-bornsrc.txt`:302–304) | Accepted; the review's "unchanged" corrected to "line edited, sentences unchanged" | §6 F-e rewritten: first sentence agrees with Main:556 at the fixed-basis layer; the inconsistency is "What remains is operational", which omits the exponent-origin frontier item of Main:20, :226, :556 and ch18:34; FULL:6604 mirror added; labelled CONFIRMING (BORN-SRC-1 F3 as sharpened by review finding 4). §8 lists the reads |
| 4 (unscoped negatives) | Kernel at `fd539e15`: `gateFlow_not_monomial` (CoherentContinuumSource.lean:74), `hadamard_not_monomial` (C5Discovery.lean:162), StateMixingCoupling.lean header ("the datum is a postulate, and nothing here derives it") | Accepted, extended to three nearby sites (U5) | §0 item 3 first bullet: "No record read derives it as an operation the observer executes". §4.1 *Effect*: "Every other probability-outputting non-monomial route found (§8)", with the three non-probability-outputting objects named. Same scoping applied to §0 item 4 ("the two probability-outputting non-monomial routes found (§8)"); §8 negatives list updated |
| 5 ("exact" Bell weights) | Main:566, Main:584 | Accepted | §0 item 3 second bullet: "The exact quantum Bell values … (finite-accuracy realizations exist, Main:566, Main:584)" |
| 6 (H-Bell "independent" of FI-1) | BRIDGE r4 §0 item 8 and §5.1 *Position* (c) ("not derived from FI-1 and not deriving it in the sources read … No independence theorem between H-Bell and FI-1 or the phase is stated") [D]; Main:362; Substratum:133 | Accepted, reviewer's wording | §0 item 2: three unsupported implications, none derived from another; "No independence theorem between H-Bell and FI-1 or the phase is stated". §4.2 *Relation to FI-1*: "beside FI-1, not after it; neither is derived from the other in the sources read", support one-directional, with BRIDGE r4's caveat that the finite-accuracy realizations have no spatial graph while H-Bell's clause (iii) is a curvature condition |
| 7 (Main:580 role; quotation accuracy) | Main:580 at `fd539e15` (computes $q_o={\rm Tr}\,\mathcal I_o(\tilde\rho)$); BORN-SRC-1 B10 (`src/914-bornsrc.txt`:114) and review 9(i) (:331–333); Main:218 ("takes the complex matrix kinematics as given, … and deriving that kinematics is open") | Accepted | §1 H-RF$_p$: Main:580 kept as the operational-route instance (trace rule an input of the realization, BORN-SRC-1 B10); 9(i) quoted as "OI supplies it rather than sourcing it (B10; Main:580). The hypothesis is open, not weaker than what is open". Main:218 quoted verbatim in §1 H-LIN and R6 |
| 8 (two admissibility notions) | BRIDGE r4 §5.1 ("'Supplies' in FI-1 means 'makes available as an admissible operator'") [D] | Accepted | §3 *FI-1 and R3*: new paragraph separating R3's admissibility (H-LIN class, $p$-normalised readout) from FI-1's (made available by the stated access); the entailment reads R3's class as the operations the stated access makes available; §0 item 2 carries the same qualifier |

## Coordinator and owner-direction changes

| Source | Change in r3 |
|---|---|
| Coordinator: cite current #1211 bridge r4 (`4e97610d…85e2`), r3 at `bridge/r3/` | Header drafts list; §6 F-b; §8 reads (nit 1 row) |
| Coordinator: under r4, phase independent of mixing only in the layer-flow form; scope phase/FI-1 independence | §0 item 2: kernel independence of the phase is from the *layer flow*, on the two-state carrier (`obligations_independent`); §3 last *FI-1 and R3* bullet: FI-1 is first only once the phase is taken as stated (Main:590, GR:268; BRIDGE §5.1 *Position* (b)) |
| Coordinator correction (REVIEW-UNIT1-r4 `e489fc19…2bc7`, R4-B1, R4-B2): the complex drive carries the phase; ray-moving necessary, not sufficient; do not say the phase is supplied with QM | §0 item 2 rewritten: in the driven-transition form the complex drive carries the phase ($e^{-i\theta X_{ab}}$ = layer flow × relative phase up to a global phase; quarter turn with the exchange = $-i\,{\rm diag}(1,1,i)$), K `gateFlow_isolation` (LiftAudit.lean:660, read at `fd539e15`: a diagonal phase times gate flows equals the transition flow); GR:250's "No phase operation enters" concerns the repertoire; the form folds the phase obligation into the mixing obligation, to be met by the complex drive and not a real rotation (only $\mathfrak{so}(3)$); moving the all-ones ray necessary, not sufficient (GR:260). The reviewer-supplied identities were checked independently (r3 E4). The interim r3 wording "the phase is supplied together with QM" never reached a recorded version. Header records REVIEW-UNIT1-r4 |
| Owner direction #1169 c.6740778880 (read via `gh api`, author amaybaum, 2026-11-09T13:05:46Z) | Header: the coordinator-relayed paraphrase replaced by the comment id and verbatim quotes (three distinctions; "would not by itself prove the Born exponent, H-Bell or full OI–QM equivalence"); §1 cites the comment. OQ-3 added (U3) |

## Untraced changes (not from a review finding)

- **U1. Dilation lemma (r3 E2).** Extends nit 2: within complete Kraus families, FI-1's operator,
  if non-monomial, yields a non-monomial dilation column, so outside H-LIN the forcing at $p=2$
  holds with the 2 again from the quadratic completeness. Needed so that "FI-1 does not entail
  R3-C's antecedent" is not left resting on $K$, which nit 2 showed is not admissible. §1 H-RF$_p$
  gains one sentence defining the readout on a Kraus family's outcome table, which B1, B2 and this
  lemma use.
- **U2. Probe `probes/r3_exponent_source.py`** (E1–E4); see below.
- **U3. OQ-3.** Asks whether the planned dependency matrix should record the scoped relations
  among the phase, FI-1 and H-Bell rather than the unqualified "independent" of the owner
  direction. Prompted by the coordinator's phase correction.
- **U4. NQ-1059 clause.** The next question now also asks whether an exhibited operation's
  unitarity is derived or posited (§5 statement, §0 item 5). This is B1(iii) carried into the
  question itself.
- **U5. Further scoping of negatives**, in nit 4's sense: §4.1 "first record found (§8)"; "In the
  records read, none is an available operation of the stated access"; R5 column (ii) "No
  frame-function predicate is found in the kernel (§8)"; §0 item 4.
- **U6. QP read first-hand at QP:846–877** (r2 cited QP only through BRIDGE); §8 "Not done"
  updated. BRIDGE r4 §5.1 *Position* (d) cites "QP:855's" for the same operators; the line is
  QP:856–857.
- **U7. Header and §8** updated for r3: revision line, r2 kept at `r2/`, drafts list, checks line,
  reads, kernel identifiers read, probe entry, re-runs of every earlier probe and of both reviewer
  scripts (all byte-identical), §4.4 ELABORATING sentence.

## Probe added

`probes/r3_exponent_source.py` (sha256
`34db77f279374af11aef8c47b8dd4748de78c343736c6d1a2d83ceed5d74e758`), output
`probes/r3_exponent_source.out`
(`3b54c129ba01469ab80dfb1efe96e033cd930a80ba646e4b8a4f85fb6e52c8a0`), exit 0 under
`python3 -I`, run from `/tmp`. Label X: exact sympy computation on generic matrices and columns;
imports no earlier script; computes nothing on an OI mechanism. E1 column exponent; E2 dilation
lemma (exhaustive support patterns) with instrument instances and the non-contraction control; E3
root insertion returns the inserted exponent, completeness only at the square root; E4 the complex
drive's phase content, the quarter-turn identity, and the real-rotation control ($\dim=3$ against
8). Mutation-tested: six single-line mutants each turn the affected check to FAIL. The E4
identities were first supplied by REVIEW-UNIT1-r4 and are checked here independently.
