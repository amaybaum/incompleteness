# ASSESS-868 r3: dispositions of REVIEW-868-r2

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Maps each finding of
`review/REVIEW-868-r2.md` (sha256 `d37cb1b1385a58287f6319273acef8dea86f828c56b573710149d3af84128f11`, REVISE
(narrow)) to its change in `ASSESS-868.md` r3, from r2 = `r2/ASSESS-868.md`
(`f4873a4494193b521d33b642156c2f611773e90947211849e50bcb3142ff34ae`, byte-identical copy of the reviewed file). Each
finding was checked against its source at `fd539e15` (`git fetch origin main` → `fd539e150759a6ea51ab279aeeac80fc06050ade`;
reads by `git show fd539e15:<path>`; no `--depth`, `gc` or `prune`; no git or GitHub write) or against the cited draft
before it was applied. No finding was refused. Independent r3 checks: `probes/r3_scope_checks.py` (exact, generic;
imports no earlier probe; no OI mechanism). The reviewer's `rv2_868_checks.py` and the writer's
`g868_generic_checks.py` were re-run with `python3 -I`: exit 0, byte-identical outputs (`rerun-r3/`).

| Finding | Verified against (fd539e15 unless stated) | Disposition | Change in r3 |
|---|---|---|---|
| **B1** "J3 needs the phase (O1)" overclaims; the argument proves only that J3 needs a non-real operation | R6d/r2 V5 (real-preserving operations keep ⟨Y⟩ = 0); `PhasesAvailable` RouteB.lean:132; `LayerFlowExecutable` LiftAudit.lean:112, `gateFlow` :47, `unit` SecondOrderCircuit.lean:356; `obligations_independent` C5Discovery.lean:59-67 (O1 vs O2 on `Fin 2`); `PhaseFreeRichness` MinimalRepertoire.lean:423 with `flow` = `exp(−itH)` ReachabilitySeam.lean:95 and `transition` LieRankSource.lean:199; GR:250 ("No phase operation enters"), GR:258 ("the quarter phase is dispensable at every level"), GR:260 (ray-moving necessary, not shown sufficient); Main:590 ("as a stated intervention principle", "added as an empirical controllability resource"); reviewer D1, D2 re-run; r3 W6–W8 | Accepted | J3's second necessity restated as **a non-real operation** (one that takes some state real in the configuration basis to a non-real one), with O1 as one source and the layer flow and the driven transition as others, none derived from OI; independence stated only as O1 versus O2. Sites: §0 Q1 *Missing*; §0 Q2 first and second bullets; J3 row (column (ii) and status); §4.4 first bullet group (rewritten: definition, three sources, countercontrol, scoped independence); §5 *Missing* J3; §6 FI-1 row (all three columns) and verdict; §8 J3 item ("a non-monomial operation and a non-real operation: CONFIRMING", sources extended); §10 Q1 and Q2; probe V5 docstring (below) |
| B1, coordinator correction (bridge r4 review R4-B1/R4-B2, `REVIEW-UNIT1-r4.md` `e489fc19…`, REVISE) | `gateFlow_isolation` LiftAudit.lean:655-662 (the transition flow as a product of gate flows and a phase diagonal); R4-B1/R4-B2 text in `bridge/review/REVIEW-UNIT1-r4.md`; r3 W10 (three-state identity `e^{−iθX_ab} = e^{−iθ} G_(ab)(2θ/π) diag(1,1,e^{iθ})`, quarter-turn identity, real-rotation countercontrol; a sign mutation of the identity fails) | Accepted | §4.4: GR:250's "No phase operation enters" read as a statement about the repertoire; the drive is complex and carries the phase (layer flow times a relative phase; quarter phase at a quarter turn with the exchange), so the phase content is carried, not dispensed with; countercontrol: a real rotation moves the all-ones ray and is real. §0 Q1 calls the layer flow and the drive complex; §6 FI-1 row says the driven transition carries the phase. No site calls the drive phase-free in content; "no separate phase gate/operation" is used for the preparations (§4.4, §11, r3 W7/W8 labels) |
| **N1** (§0 Q2) "H-Bell is a third, independent gap" | BRIDGE r3 §5.1(c) ("no source read derives either from the other"); BRIDGE r4 §0 item 8 and §5.1(c) ("No independence theorem between H-Bell and FI-1 or the phase is stated") | Accepted | §0 Q2 first bullet: "a further gap: in the sources read it is not derived from FI-1 or the phase and derives neither, and no independence theorem is stated (BRIDGE r4 §5.1(c))"; §6 FI-1 row column 1 likewise |
| **N2** (§2) BRIDGE r3 hash and status stale | `sha256sum`: `bridge/r3/BRIDGE-UNIT1.md` = `ee1c83c0…8219`; `bridge/BRIDGE-UNIT1.md` = `4e97610df18a8f6a9e8a89486ea3633cc3609bcbd6a2c9686f3ad780af2885e2` (r4, header "Revision r4"); `REVIEW-UNIT1-r3.md` (`7a6a7f1c…`) verdict REVISE; `REVIEW-UNIT1-r4.md` (`e489fc19…`) verdict REVISE. The r2 hash `a5d7aad1…78c1` matches no file found | Accepted | §2: cites r4 (`4e97610d…85e2`) as the current working file under review, with REVIEW-UNIT1-r4 REVISE and its R4-B1/R4-B2 used in §4.4; r3 at `ee1c83c0…8219` (archived `bridge/r3/`) with REVIEW-UNIT1-r3 REVISE; the earlier chain kept. Body citations "BRIDGE r3 §5.1" changed to "BRIDGE r4 §5.1" after checking that r4 states the same content (FI-1 necessary, one direction, configuration carrier: r4 §0 item 8; encoded stabilizer-scope maps without FI-1: r4 §5.1 :458); §11 read list adds r4 and both reviews |
| **N3** (§8, §4.1 (⇐)) the `block-positiv` hit; label (⇐) CONFIRMING; orientation | `bridge-compatibility-audit/source-assessment.md:17-19` ("For block-positive X and a unit local vector a, the conditional matrix sigma_a … is PSD: its quadratic form at b is the nonnegative product pairing at a tensor b"); `git grep block-positiv` (also `kt4_prem1_indep_check.py:825, :898`); `toOp ω = Matrix.toLin' (Matrix.of ω)` and `lor_toOp_of_maxCone` CompositeDimension.lean:1049; r3 W5 | Accepted | §4.1 (⇒): `h_a` orientation by transposition [A; r3 W5]; §4.1 (⇐): operator-form identity (r3 W5), standard fact (L), the W record states the (⇒) direction; §0 Q1 second bullet; §5 *Conditional* Lemma H entry; §8 search paragraph reports the hit; §8 labels: (⇒) CONFIRMING in the wing-exchanged orientation, (⇐) CONFIRMING. Native form stays ELABORATING |
| **N4** (§0 Q1, §4.1) K2-route hypotheses list omits closure; they are hypotheses on `K` | `EqvK2MaxCone.lean:153-160, :174-183, :204-213` (`hH1`, `hadd`, `hsmul`, `hmax`/`hvalid`+`hsharp`, `hH2`, `hA`, all on `K`; conclusion `K = Q3`) | Accepted | §0 Q1 *Validity is not quantumness*: six hypotheses, all on `K`, listed; §4.1 closing paragraph likewise. The "selects Q3 only with `cnot` invariance and the drive" sentence is replaced |
| **N5** (§0 Q1 vs §5) T2 §6 [W] under "Established" | §1 layer rule (K/P established; W model-reviewed record); §5 lists T2 under *Conditional (W/D/A)* | Accepted | §0 Q1: T2 §6 moved to a separate *Conditional (W)* bullet |
| **N6** (§11, dispositions) "Python integer division (floats)" | Python 3 semantics: `/` on ints is true division (float), `//` is integer division; sympy 1.14 `Rational(1,2) == 0.5` is `False` (r3 W9; reviewer E1) | Accepted | §11 r2-probe run-1 bullet: cause stated as Python numbers with the float `1/2` and sympy's strict Rational–float `==`; adds that the run-1 source was not retained and that the reviewer's reconstruction is consistent. DISPOSITIONS-r2.md is a record of r2 and is left unchanged; this entry supersedes its wording |
| **N7** (probe) V1 and V3 do not test their full claims; V5 docstring carries B1 | `r2_validity_scope.py` V1 (one vertex, one outside point), V3 (comment only for `a₁² + a₃² ≤ 1`), V5 docstring "(phase needed)" | Accepted (strengthen) | r3 W1: dual of the six Pauli effects = cube cone, both inclusions, via `λ_s = Π_i (t + s_i v_i)/(8t²)` reconstructing `(t, v)` with each factor one of the dual's inequalities, plus outside control; r3 W3: herald identity, `1 − a₁² − a₃² = (1 − |a|²) + a₂²`, and the certificate `2(1 + a₁b₁ + a₃b₃) = (1 − a₁² − a₃²) + (1 − b₁² − b₃²) + (a₁ + b₁)² + (a₃ + b₃)²` for every full-ball product value, singlet eigenvector; W4 swap with explicit real and imaginary parts. §11 cites V1 and V3 as illustrations and W1, W3 as the full checks. V5 docstring rewritten (below) |

## Probe changes

- **`probes/r2_validity_scope.py`**: only the V5 docstring line changed, from "(phase needed)" to "(a non-real operation
  is needed; the quarter phase S is one, not the only one: see r3_scope_checks.py W7-W8)". sha256 `60095dc0…0ea2` →
  `cedf61129150dcac287675a1107f8cefbb68e94e3256a472faeb2060023a7101`. The recorded original is kept byte-identical at
  `r2/probes/r2_validity_scope.py` (`60095dc01a21c62735f81f29ac85f11986a58ff535cc72f6112a3350fa5e0ea2`) with its output.
  Re-run after the change: exit 0, output byte-identical to `r2_validity_scope.out` (`d86e03c1…f020`).
- **`probes/r3_scope_checks.py`** (new): sha256 `e6afb063d08802f45c59e258b2f6f4933c9adc7041e71ac8d2ab7568ba299575`,
  output `probes/r3_scope_checks.out` (`394b6fd8e033f49ca784457c1bbee09a2c1757e1b93b47d826471dbb3be58ed9`), exit 0,
  27 checks, 0 failures. Exact generic checks only; imports no earlier probe; re-types two kernel definitions as
  generic matrices; computes nothing on an OI mechanism.
  - Run 1 (`probes/r3_scope_checks.run1.out`, `ec76650ab8c46b7e6c13adf364e945247cbafcf3a353cdcb4c0dad06aec07223`;
    24 checks) failed the W8 control "closed form of `exp(−itX_ab)` equals the matrix exponential": sympy's
    `simplify` left `(-1)**(1/4)` forms unreduced, while `expand_complex` shows the two matrices equal entrywise. The
    comparison was given `expand_complex`; no expected value changed.
  - After run 1, W10 (3 checks) was added on the coordinator's relay of the bridge r4 review's R4-B1/R4-B2, and the
    W7/W8 docstring and labels were reworded to "no separate phase gate" (the flow and the drive are complex) without
    changing any check. The intermediate passing outputs were overwritten and are not retained.
  - Mutation spot-check (not recorded in the probe): replacing `diag(1,1,e^{iθ})` by `diag(1,1,e^{−iθ})` in W10's
    identity leaves the residual `1 − e^{−2iθ}`, so the check is not vacuous.

## Owner-direction changes (#1169 c.6740778880)

| Distinction | Change in r3 |
|---|---|
| Product-test validity vs quantum joint-state behaviour | Unchanged in substance; N4 sharpens it: the K2 conclusion is about a cone `K` under six hypotheses on `K`, and product tests do not decide whether a table is a quantum state (§0 Q1, §4.1) |
| Configuration vs encoded carriers | B1's non-real necessity is stated for configuration-basis reality on the configuration carrier (§4.4, §0 Q1); encoded-carrier sentence kept with the r4 citation |
| Mathematically available vs derived from OI | §4.4 lists each source of a non-real operation with its status: O1 "a stated intervention principle" (Main:590); the layer flow available by stipulation (`onesTheory`); the drive "added as an empirical controllability resource" (Main:590); none derived |
| Coherent mixing vs the full probability and composition rules | Unchanged; §4.4's mixing bullet and §0 Q2 kept. B1's correction keeps "mixing" and "a non-real operation" apart without merging the phase obligation into mixing: the drive carries the phase, a real rotation mixes and carries none |

## Untraced changes (not from a review finding)

- **U1.** Header: revision line r3, review cited, r2 archived path and hash, "three probes".
- **U2.** Owner-direction citation in the header gives the comment id (#1169 c.6740778880) in place of "chat direction".
- **U3.** §11: rv2 and g868 re-runs recorded; r3 reads added (kernel declarations listed in the B1 row, GR:246–260,
  `EqvK2MaxCone.lean:150-215`, BRIDGE r4 and both bridge reviews, REVIEW-868-r2).
- **U4.** §4.3 item 1 cites r3 W3 beside r2 V3 (follows N7).
- **U5.** Line rewrapping in edited paragraphs; no wording change beyond the entries above.

## Not changed

- K2 analysis, Lemma H's native form, the J5/J7/J9–J14 rows, §4.3 item 2, §7 (Q-868-H) and §9: the review states that
  neither the K2 analysis nor Q-868-H depends on B1, and no other finding touches them.
