# Review of OI-SM-QM-BRIDGE unit 1, revision r2 (BRIDGE-UNIT1.md)

**Reviewer.** A fresh, independent reviewer (Claude Code subagent, 2026-11-09). The review is
paper-only and full-text. It made no git, GitHub or Lean action and no manuscript change. This
review authorizes nothing: a review ACCEPT does not authorize a freeze, an implementation, a
manuscript change or a merge (#1211 c.6738806776).

**Objects.** Hashes were verified before reading.
- `BRIDGE-UNIT1.md` (r2): `3905569bd8d47e3d3797e66f5d3c68b2fbf054e8859191b7cf3777db0412103a`, read in
  full (839 lines).
- `DISPOSITIONS-UNIT1-r2.md`: `5b30fdfdac7dc3e4e0948475dad294873b1024205853cc9ad07ea55d12ae1d95`.
- `r1/BRIDGE-UNIT1.md`: `00cd6fad…`.
- `review/REVIEW-UNIT1.md`: `e242a794…`.
- `probes/r2_generic_checks.py`: `579533e3…`. Its output: `fba1e561…`.
- `issue1211.md`: `49fc9572…`.

I also read the owner records c.6738806776 and c.6739843458 with `gh api`. Sources were read
with `git show fd539e15:<path>` after `git fetch origin main`; working copies are in
`review/src2/`.

**Verdict: REVISE.** All of the r1 blockers B1–B5 and nits N1–N15 are fixed, and every fix
checks against its source (§3). The changes made from the r1 text are sound except in one
place, the new central claim FI-1 (§0 item 8, §5.1, the FI-1 line of §10, and §11's
"The first unsupported step is FI-1"). There are three blockers there:
- **RB1.** The ordering ("earliest", "weakest … therefore") is contradicted by records on `main`
  that the unit did not read.
- **RB2.** The necessity claim drops the qualifier "exact finite endomorphic" and leaves the
  carrier ambiguous.
- **RB3.** The status line cites the wrong direction of support and mis-scopes the adaptive
  case.

There are ten nits. A delta review of the FI-1 passages, the coverage list and the nits is
enough, provided nothing else changes.

***

## 1. Blockers

### RB1. FI-1's "earliest" and "weakest" are contradicted by kernel and audit records on `main` (§A.19, §A.31, §A.34)

The document claims the following:
- §5.1: "FI-1 is therefore the weakest coherent requirement on the chain's path to operational
  QM, and the first that fails to be supplied".
- §5.1(b) places the phase after FI-1, because "it is adjoined as a stated intervention
  principle and is itself monomial, so it does not reach coherent content without FI-1".
- §10 labels FI-1 CONFIRMING with "added: its position as the first unsupported step of the
  forward chain".

Records under `verification/audits/foundations/` at `fd539e15` were not read. They already
state the frontier, and they state it differently:

- **Two independent obligations, kernel-proved.** The C5 discovery audit (`c5-discovery-audit.md`,
  T0) and `obligations_independent` (`OIBridge/C5Discovery.lean:59`) separate two obligations:
  O1 is the phase (`PhasesAvailable`) and O2 is the flow (`LayerFlowExecutable`). Each holds
  without the other.
  - The substratum theory has the phase and no flow.
  - The ones-fixing theory executes every flow and has no phase. It is not QM
    (`onesTheory_layerFlowExecutable`, `onesTheory_not_qm` in `FlowEndpoint.lean`).

  So a non-monomial resource without the phase does not reach QM either. The argument of
  §5.1(b) is symmetric. FI-1 comes first only once the phase is granted, which is how Main:590
  and GR:268 state their equivalence ("with the phase intervention stated"). It does not come
  first in any logical order of the forward chain.
- **The audit that sources the claim.** `exec-source-audit.md` (the round that proves
  `exists_nonMonomial_of_layerFlowExecutable`, which FI-1 rests on) states the outcome as "two
  named assumptions, neither derived from the stated access": the phase and the flow. It names
  "a non-monomial admissible operator at level one" as the flow's necessary condition. That is
  FI-1's content. The audit does not rank FI-1 before the phase.
- **A strictly stronger necessary condition is proved.**
  - `uncountableNonMonomialRays_of_layerFlowExecutable` (`CoherentContinuumSource.lean`) and
    `uncountable_of_layerFlowExecutable` (`PolarizationClosure.lean`) show that executability
    forces uncountably many pairwise non-proportional non-monomial rays at level one.
  - `coherent-continuum-source-audit.md` concludes that no stated mechanism sources this.
  - `polarization-closure-audit.md` constructs `PolC`. It has the phases, non-monomial
    operators and the whole closure `DerivedOI`, and it executes no layer flow and is not QM
    (`polarizedTheoryC_derivedOI`, `polarizedTheoryC_not_qm`).

  So FI-1 is shown insufficient. The corpus's sharpened requirement is stronger than FI-1, so
  calling FI-1 "the" requirement understates what is known.
- **Bell is independent of FI-1 as well.** Quantum Bell statistics are realized to finite
  accuracy by fixed bijections (Main:566, Main:584), which are monomial on configurations, once
  ontic parameter dependence is given (Main:403–406). So H-Bell (S9) is a separate unsupported
  implication. It does not come after FI-1. §5.1 does not address it.
- **Reviewer check G2** (generic, exact). This illustrates the independence at the operator
  level, which `obligations_independent` proves at the level of theories.
  - $G=\tfrac23\mathbf 1\mathbf 1^{T}-I_3$ is orthogonal, non-monomial, and fixes the all-ones
    vector.
  - $\mathrm{diag}(1,i)$ is monomial and moves the all-ones ray.

*What is supported.* FI-1 is a necessary condition, proved in one direction only, for layer-flow
executability. It is not supplied by the stated access, and it is open where §5.1 says. With the
phase taken as stated (Main:590, GR:268), it is the first unsupported step on the route to
exact finite endomorphic operational QM. The phase obligation O1 and H-Bell are logically
independent unsupported implications beside it.

*Required.*
- Restate "earliest" relative to the stated phase, and name O1 and H-Bell as parallel,
  independent gaps, citing `obligations_independent`.
- Delete "weakest coherent requirement … therefore". Cite instead the strengthened necessary
  condition, and `PolC` as the countermodel to sufficiency.
- Correct §5.1(b), §0 item 8 and §11's last bullet to match.
- In §10, keep FI-1 at CONFIRMING. Cite `exec-source-audit.md`, `c5-discovery-audit.md` and
  `coherent-continuum-source-audit.md` as its basis, and drop "added: its position as the first
  unsupported step", which is contradicted.

### RB2. FI-1's necessity drops the qualifier "exact finite endomorphic", and its carrier is ambiguous (Code Review Rules, "class actually ruled out"; the r1 B4 pattern)

**The qualifier.** Main:590, GR:262 and GR:268 state the equivalence for "exact finite
endomorphic operational quantum mechanics … within the structural architecture". §0 item 8
says only "equivalent to operational QM", and §5.1 says "the chain's path to operational QM".
That target is weaker, and FI-1 is not necessary for it:
- Main:566 and Main:584 give "finite reversible deterministic embedded" realizations, by fixed
  bijections (monomial on the configuration carrier), of arbitrary finite quantum experiments,
  including "incompatible measurements, adaptive interventions, preparation and instrument
  statistics", to any finite accuracy.
- Main:600 gives two-sided ε-density.

These are QM → OI results and correctly do not count toward the forward bridge (§2). They do,
however, bound FI-1's necessity. FI-1 is necessary for exact operational QM on the
configuration carrier within the interface. It is not necessary for reproducing operational
quantum statistics at finite accuracy.

**The carrier.** FI-1 says "on the observer's carrier". The kernel statement
(`exists_nonMonomial_of_layerFlowExecutable`) is at level one of the configuration carrier
($S\times\mathrm{Fin}\,1$). On an encoded carrier, non-monomial encoded maps exist without any
non-monomial configuration-level operator:
- **QP.** NNB gives encoded $S$ and $H$ at single-qubit stabilizer scope (QP:79–98). By QP's
  §4.1 containment (QP:846–877), every operation of N with or without NNB, adaptive included,
  still lies in `permTheory`.
- **MECH-2.** Theorem U2 places the encoded unitaries that fixed bijections induce in
  $A_4\wr S_n$ (tetrahedral rotations, which include rotations of order 3). Theorem NC gives a
  noncontextual configuration-level model of the whole encoded theory.
- **Reviewer check G3** (a generic 4-state toy model with an epistemic restriction; not an OI
  mechanism). The permutation (2 3 4) is a permutation matrix. It maps $Z_\pm\to X_\pm\to
  Y_\pm\to Z_\pm$, and the encoded qubit unitary realizing that rotation is non-monomial in the
  encoded $Z$ basis.

*Required.*
- State FI-1 on the configuration carrier at level one, as GR:270 does ("a non-monomial
  admissible operator at level one").
- Restore "exact finite endomorphic … within the structural architecture, with the phase
  stated" wherever FI-1's necessity is stated: §0 item 8, §5.1, and §11's last bullet.
- Add one sentence noting that encoded-level non-monomial maps (QP NNB, MECH-2) and
  finite-accuracy realizations (Main:566) do not meet FI-1 and are not counterexamples to
  "not supplied".

### RB3. FI-1's status line cites the wrong direction of support, mis-scopes the adaptive case, and contradicts itself on "only"

- **Direction (§A.34).** "Not supplied for the stated substratum dynamics with the observer's
  read/write access" cites `substratumTheory_not_layerFlowExecutable` and
  `obs_not_layerFlowExecutable`. Both prove $\neg$executability. FI-1 is only *necessary* for
  executability, so neither establishes $\neg$FI-1. Main:590 likewise says only that the
  read/write access does "not source that executability". Its "neither a non-monomial
  admissible operator nor the layer flow" refers to the lift alone.

  The correct support is on `main`:
  - `obs_availExt_le_substratum` (`SubstratumInterfaceAudit.lean:837`, with
    `obsTheory 𝒮 = permTheory (Conf 𝒮)`, :20);
  - `substratumClass := IsMonomial` (`StructuralClosure.lean:180`);
  - `exec-source-audit.md`'s scope amendment: "every operation supplied by the stated observer
    access is configuration-level, in `obsTheory 𝒮` permutation-valued";
  - GR:260's `bijectiveOperator_monomial`, with `readWriteOperator_monomial`.

  For the lift, `coherentLiftClass_eq_substratumClass` is correctly cited.
- **The adaptive case.** "Open … for adaptive or extended mechanisms" is wrong for the
  configuration-level statement:
  - every `FiniteOperationalTheory` carries `availExt_bind`, the feed-forward step
    (`OperationalAssembly.lean:617`);
  - `obsTheory` is `permTheory`;
  - QP:851–863 maps adaptive processes of N, with or without NNB, into `permTheory` by a paper
    argument.

  The open adaptive item in the corpus is the *encoded* quarter phase $S$ (QP:897–915;
  `quarter-phase-feedback-20261107/RESULT.md`). That is a different object, and by RB2 it
  does not need FI-1. Keep "extended mechanisms" open, and remove "adaptive".
- **"Only".** §5.1(e) calls S13 "FI-1's only unresolved candidate source". This contradicts
  the status bullet of the same section, which keeps open "whether every realization of the
  lift's channels is configuration-level (GR:270)". It also omits the corpus's stated
  candidate sourcing map: the C5 discovery audit's candidate 2. That candidate is a
  polarization of the per-site phase space $V\times V$, with the Weil representation sending
  the swap layer to the Hadamard matrix (non-monomial). Its verdict is C, underdetermined,
  because the corpus does not supply the map (test 8).

  That candidate is a phase-space polarization of the kind NQ1 studies (the positive-frequency
  $J$ on the real lift's phase space). §5.1 and NQ1 should cross-reference it as an
  assumption-watch link (§A.31, cross-propagation).

*Required.* Re-cite the read/write negative as above, remove "adaptive" from the open list,
replace "only" with the list of open candidates, and cite the C5 candidate 2.

***

## 2. Nits

- **n1 (FI-1 wording).** "non-monomial (state-mixing)" equates two predicates that differ for a
  general Kraus operator. In reviewer check G1, $K=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ is
  non-monomial, yet $X\mapsto KXK^\dagger$ preserves diagonal states. Both predicates coincide
  for unitaries. Necessity holds for both: the stronger "an available operation that is not
  diagonal-preserving" comes from `gateFlow_half_not_preservesDiag`. Use GR:270's term,
  "admissible *operator*", or state the two separately.
- **n2 (§5.1(c)).** "On monomial operations $|U|^p$ gives the same table for every $p>0$"
  should read "on permutation unitaries" (Main:556: "entries are 0 or 1"). Weighted monomial
  Kraus families, such as QP:855's $2^{-k/2}P_\sigma$, are normalized under $|K|^p$ only at
  $p=2$ (reviewer check G4).
- **n3 (§6 Born row; carried from r1).** "An independently justified selection of the
  quadratic functional …; equivalently a source of non-monomial admissible operators" is not an
  equivalence. The second is a precondition for the first to have content. It also cites a
  layer-flow negative for a non-monomial claim (see RB3). Replace "equivalently" with "which
  presupposes".
- **n4 (§0 item 8, §5.1).** "the site-space wave-operator formulation …, which is the unproved
  map $\varphi\to L_{\rm obs}\to\Delta_g$" merges two gaps:
  - the map itself (SM:232);
  - the missing operational map from that formulation to the configuration carrier (GR:270).

  State both.
- **n5 (§5.1).** Name the closest derived objects:
  - the layer flows (one-parameter groups of $*$-automorphisms from `SecondOrderLayer` and
    `SwapLayer`), whose intermediate-time points are non-monomial;
  - `driveQ_isContinuousPath`, which §3.1 and B26 already cite.

  These are derived but are not available operations (coherent-continuum audit, row S5). This
  shows that "supplies" in FI-1 means "makes available".
- **n6 (§9 scope sentence, touched in r2).** "SM §§1–6 … Main §§1–3.4" disagrees with the
  header's coverage. The header covers SM §§1–5, with SM §6.1 only at SM:677–690, and of Main
  §3.4 only the cited statements and remarks. §13 agrees with the header. Align §9 with them.
- **n7 (F8).** The ellipsis in the ch06:28 / FULL:1541 quotation drops "— with the physical
  spin identification riding H-spin' (SM §4.7) —". State the book's qualifier. Then say why the
  finding stands despite it: H-spin' gives spin, not statistics, and the fermionic measure is
  open.
- **n8 (§4 counts).** B9's column (ii) also carries a D clause ("quadratic isotropy at observer
  level is then D given cubic symmetry"). Either count it under "D for one prong or a stated
  restricted class" (4, not 3) or say why it is excluded. The other counts are correct; see §5.
- **n9 (header coverage).** After RB1–RB3, add the records read to the coverage list:
  - `verification/audits/foundations/` `exec-source-audit.md`, `lift-source-audit.md`,
    `c5-discovery-audit.md`, `polarization-closure-audit.md`,
    `coherent-continuum-source-audit.md`, `state-mixing-coupling-audit.md`;
  - the Lean identifiers cited from them.
- **n10 (§5.1(d)).** "Its SM-specific bridges (H-link, H-cust, …) are downstream of FI-1 for
  their quantum content" should be confined to bridges whose content is operational or
  field-theoretic: H-spin', H-χ' and the fermionic measure. The carrier's complex structure,
  NQ1, is posed on the real lift and is not downstream of FI-1. C5 candidate 2 tests a
  structure of that kind on its own terms.

***

## 3. The r1 findings: fixes confirmed against their sources

| Item | Present in r2 | Correct against source | Notes |
|---|---|---|---|
| B1 | §0 item 6; §10 "Connection" and consequences; §11 NQ2(c); label ELABORATING | Yes. Read: QP:298–305 (the "Relation to SM" bullet); SM:306; QP:805–806; SM:539; SM:569 ($\Gamma A\Gamma=-A$, "for *any* site partition"); QP:954–956. The C3 countercontrol re-derived by hand: the $T^{\pm4}$ coefficient of $-4D'^2$ is $-2\mu$, with no $\mu^2$ contamination at that distance. | "Whether the identity or the identification themselves fail on the armed region is not derived here" is correctly scoped. |
| B2 | §10 third consequence; NQ2; B25; §9 NNB row; header | Yes. MECH-1:877–893 read verbatim, including "These are consequences of the paper argument". MECH-2 §0 items 1–3 read. M-INACC-1 standing as stated. | Citation "as the record, not as established premises" is correct under §A.46 item 7. |
| B3 | F4; §0 item 4; §3.2 row; B13; §6 phases row; §11; NQ1; label | Yes. SM:505, SM:809 and SM:130 quoted exactly. Hand check: the commutant of $f\otimes I_6$ in $\mathfrak{sp}(12)$ is $\{I\otimes A+J\otimes B: A^T=-A,\,B^T=B\}=\mathfrak u(6)$ (dimension 36), and the stationary stabilizer is $\{A,B\ \text{commuting with}\ \Sigma\}$, dimension 14. Null modes $a=\pm2$: $(f\mp I)^2=0$. | C2(d) is labelled computation-supported. The hand argument above also supports it, so the label is conservative. |
| B4 | §0 item 4; S7; §6 Interference and tally; B23; §11 | Yes. Main:590 and GR:270 qualifiers restored verbatim. | The same pattern recurs in the new FI-1 text (RB2). |
| B5 | Header; §13 | Yes. c.6738806776 is quoted with its six exclusions; c.6739843458 is quoted ("Allow generic checks (as #1210)"); the r1 script is recorded as run before the permission. | — |
| N1 | F9 | Yes. #1188 body: owner decision "Do not use it as scientific evidence"; the site list matches. `MonoidalCompletion.lean:360` is stated to be a definition. | — |
| N2 | F11 | Yes. Hand check: the undirected neighbours are $\{i\pm1\}\cup\{i+2: x_{i+1}=0\}\cup\{i-2: x_{i-1}=0\}$, giving degree 2, 3 or 4 for $L\ge5$. | — |
| N3 | F8 | Yes, apart from n7. ch06:28 = FULL:1541; ch10:36. | — |
| N4 | F7 | Yes. ch05:91 = FULL:1409 ("exact change of variables"). | — |
| N5 | F4 and F5 site lists | Yes. Sub:393–395 (Level 2); SM:511 ("At the bijection level … the commutant"). | — |
| N6 | §4 counts | Yes. Recount: Op 6, E 7, St 10, QS 1, C 1, "none identified" 14. D-partial is 3 or 4 (n8). | — |
| N7 | B6, B7, B20, F2, §9 | Yes. SM:1424; Main:403–407; Sub:98. | — |
| N8 | §3.2, F6 | Yes (SM:176). | — |
| N9 | §6 phases row | Yes. GR:260, "exhibited at level one, with no claim … at each composite level"; the identifiers exist in `PhaseSource.lean`. | — |
| N10 | §3.1, B26, §6 | Yes (Main:274, Main:590; `SecondOrderDrive.lean`'s docstring: "Not claimed: a group law"). | — |
| N11 | §3.1, B20, F2, §9 | Yes (Main:22, $I_{\rm ont}\ge0.0309$ bits). | — |
| N12 | F3 | Yes (Main:66); labelled CONFIRMING. | — |
| N13 | §3.3 | Yes. | — |
| N14 | F10 | Yes. | — |
| N15 | B8, §9 | Yes. `A5-LINEAR-AFFINE.md`:543, R5, with its standing. | — |

The r1 review's other items (QP:954–956; MonoidalCompletion:360) are applied. The two
deviations the dispositions record, the N6 counts and B2's standing, are correct.

***

## 4. The changes not traced to a finding

- **§0 item 8 and §5.1 (FI-1).** See RB1–RB3 and n1–n5, n10.
- **Removed question 5.** Correctly removed: c.6738806776 designates "a fresh, independent
  reviewer". §12 is renumbered without loss. Its closing line also records F9 as decided by
  #1188.
- **Header standing line.** Correct, and adds no claim.
- **Scope wording in §9 and §13.** §13 agrees with the header. §9's pre-existing "SM §§1–6 …
  Main §§1–3.4" does not (n6).
- **Check C2(d).** Correct and not vacuous. It runs an independent count with the o(6)
  comparison; my hand derivation agrees (§3, row B3).
- **S12 in §5.1.** SM:276 is read correctly: "the descent of CI through the
  substratum-to-observer map remains open". S12 is open, not refuted. SM:236 refutes only the
  stronger inference "CI ⟹ no information".
- **QP:954–956.** These are the right lines (the assumption-watch bullet on bipartiteness).

***

## 5. Exact checks

**The writer's probe.** `python3 -I probes/r2_generic_checks.py` was re-run. Its output is
byte-identical to `probes/r2_generic_checks.out` (copy at
`review/probes/r2_generic_checks.rerun.out`): 20 PASS, ALL PASS. The controls are not vacuous:
- C2(c) has a countercontrol: real $J$ exists at $a=1$, with 2 solutions.
- C3 has a control ($\{D_0+h,\varepsilon\}\ne0$), and its $-2\mu$ is symbolic in $\mu$, so
  $\mu=0$ is the null case.
- C2(d) compares against diagonal o(6), which has a different count (4), so it does not merely
  reproduce the claimed 14.
- C1 and C2(a)–(b) are single-instance witnesses ($\omega=\pi/3$; one rational $\Sigma$) of
  statements that the text also proves by hand (Schur's lemma; $f^2=af-1$). That is
  acceptable.

**Reviewer probe** `review/probes/r2rev_fi1_checks.py`.
- Output: `r2rev_fi1_checks.out`, ALL PASS (20 checks).
- Method: exact sympy on generic objects only. It imports no earlier script and runs no OI
  mechanism, under c.6739843458.
- File hashes: script `3f8d0f45…`, output `9ddf0156…`.
- Results:
  - **G1:** non-monomial ≠ state-mixing for Kraus operators; they coincide for unitaries (n1).
  - **G2:** non-monomial and ray-moving are independent at the operator level (RB1).
  - **G3:** an encoded non-monomial rotation from a configuration permutation in a 4-state toy
    model, with an identity control (RB2).
  - **G4:** the exponent is inert on permutation unitaries and normalizes only at $p=2$ for a
    weighted monomial Kraus family (n2).
- **Integrity note.** The first run failed G1(b) because I wrote the expected sign of the
  off-diagonal entry as $cs(b-a)$; the correct value is $cs(a-b)$. I corrected the expected
  expression, which does not change the claim (zero iff $cs=0$), and re-ran. The recorded
  output is from the corrected script.

***

## 6. FI-1 assessment, by the brief's questions

- **Earliest?**
  - **Inputs, not implications.** Site factorization (B4), the access posits P1–P3 and E-iso,
    and the second-order form are stipulated inputs; FI-1 is conditional on them, which §5.1(e)
    says for B4–B8. The kernel `obsTheory 𝒮` presupposes a site-factorized `Substratum`, so
    FI-1 is conditional on B4. State this, and state the same for P1–P3, explicitly.
  - **H-PREP** concerns preparations, and FI-1 does not use it.
  - **Not earlier than the phase or H-Bell.** As an unconditional ordering, "earliest" fails.
    The phase obligation O1 and H-Bell are logically independent unsupported implications, not
    later ones (RB1).
- **Necessary, one direction only?** Yes. GR:270 and `exists_nonMonomial_of_layerFlowExecutable`
  give executability ⟹ a non-monomial admissible operator at level one. The text claims no
  converse. `PolC` shows the converse fails, and the text should cite it (RB1). The scope must
  be exact, finite and endomorphic, on the configuration carrier (RB2).
- **The Main:548 citation.** Correct. Main:99 names `S_imp_D` (⊆), and `D_imp_Qfb` with
  `Qfb_imp_S` (⊇), assembled in `finite_horizon_equivalence`. All exist in
  `OIBridge/Equivalence.lean`. Every direction of the three-way coincidence is witnessed.
  "Whose operations on the configuration carrier are monomial" is not part of Main:548. It is
  correctly sourced to Main:270, GR:260 and GR:270 in §5.1.
- **Scope of "not supplied".** The §A.19 search covered:
  - MECH-1 and MECH-2: their encoded maps lie in `permTheory` (RB2);
  - `driveQ` and the layer flows: derived, not available (n5);
  - adaptive feedback: inside `permTheory` at configuration level (RB3);
  - the quarter-phase feedback results: encoded $S$ only;
  - QP NNB: encoded $H$ and $S$, inside `permTheory`;
  - the C5 polarization candidate: non-monomial, with the map not supplied (verdict C);
  - `PolC`: a constructed candidate, not sourced;
  - `StateMixingCoupling`: a postulate ("Nothing here derives the datum");
  - the read-write family: permutation-valued.

  No record on `main` supplies a non-monomial admissible operator on the configuration carrier
  from the stated substratum dynamics and access. So the claim "not supplied" survives, but
  under the citations of RB3. The open part must list the site-space formulation, the
  undecided realizations of the lift's channels, C5 candidate 2's unsupplied map, and extended
  mechanisms. It must not list adaptive processes.
- **Ordering in §5.1.**
  - Born exponent after FI-1: holds, scoped to permutation unitaries (n2).
  - Phases after FI-1: does not hold. The ordering is by stipulation, and the obligations are
    independent (RB1).
  - SM bridges after FI-1: holds for H-spin', H-χ' and the fermionic measure. It does not hold
    for the carrier's complex structure (n10).
  - H-Bell is not addressed, and it is independent (RB1).

***

## 7. The other checks in the brief

- **Three-question columns.** These stay separate in every ledger row (B1–B27), in §6 and in
  §9. Column (iii) is never used for column (ii). Selection by an observed quantity is
  labelled E (B2, B6, B7, B9, B18–B20); QS is kept for premise I only (B25); consistency is
  labelled C (B17).
- **§A.31 labels.**
  - Q6, F1, F4, F5 and F8 as ELABORATING are confirmed against their bases. I checked
    `phase-source-audit.md`:74 and `dimension-dependency-reconciliation-20261029/README.md`:8.
  - F2, F3, F6, F7, F9, F10 and F11 as CONFIRMING are confirmed.
  - FI-1 as CONFIRMING is right, but its stated basis and its "added" clause need correcting
    (RB1).
  - "No finding is NEW" is correct.
- **Counts.** These are correct except for n8.
- **Authorization.** Nothing implies that a manuscript change, a computation on an OI
  mechanism, a new assumption, a freeze or a dispatch has been authorized:
  - the header and §13 quote both owner records;
  - every manuscript-level finding is "recorded only";
  - §12 asks rather than acts;
  - NQ1 and NQ2 are paper questions;
  - the r2 checks run on generic objects;
  - F9 defers to #1188's owner decision.

***

## 8. What a revision needs for ACCEPT

1. Fix RB1–RB3 in §0 item 8, §5.1, §10's FI-1 line and §11's last bullet.
2. Apply n1–n10. Of these, n1, n2, n3 and n6 are factual; the others are scope or wording
   fixes.
3. Add the foundations audits to the coverage list (n9).

A delta review of those passages is sufficient if nothing else changes.
