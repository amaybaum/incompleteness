# Review of OI-SM-QM-BRIDGE unit 1, revision r5 (BRIDGE-UNIT1.md)

**Reviewer.** A fresh, independent reviewer (Claude Code subagent, 2026-11-09). This is a
paper-only, full-text review. The reviewer made no git write, GitHub write or Lean action, and no
manuscript change. It authorizes nothing. Under #1211 c.6738806776, an ACCEPT authorizes no
freeze, implementation, manuscript change or merge.

**Objects.** Hashes were verified before reading.
- `BRIDGE-UNIT1.md` (r5): `78f1098ee4310b0a190e211add27094025f95d3d1fa7d9b0fd77eaf260cf91a4`.
  Read in full, all 1288 lines.
- `DISPOSITIONS-UNIT1-r5.md`: `d27c50e779e00c2794559046ef2beafc930e53ccd5b14ab78e4359bda79fdd13`.
  Read in full.
- `r4/BRIDGE-UNIT1.md`: `4e97610d…85e2`. Diffed against r5 with `git diff --no-index -U0`:
  19 hunks.
- `review/REVIEW-UNIT1-r4.md`: `e489fc19…c2bc7`, verdict REVISE (R4-B1, R4-B2, n1–n6).
- `probes/r5_generic_checks.py`: `db07e9fe…9933`. Its output is `df300469…86a7`.

**Owner records.** Read with `gh api`:
- #1211 c.6738806776 (11:22:08Z), c.6739843458 (12:17:04Z), c.6740537555 (12:53:23Z);
- #1169 c.6740778880 (13:05:46Z) and c.6741291498 (13:30:54Z).

**Sources.** Read with `git show fd539e15:<path>` after `git fetch origin main`.
- *Papers:* GR:248–272, with the anchors at GR:250 "No phase operation enters", GR:258
  "dispensable at every level", GR:260 "is not shown sufficient", GR:266 and GR:270 "the smaller
  one". Main:218 and Main:590. SM:809. Sub:131 and Sub:133.
- *Audits:* `phase-source-audit.md`:205–235 and :280–292 (the owner quote is at :212–221, "by
  itself" at :229, and :287); `frozen-sourcing-audit.md`:282–293.
- *Lean statements, read at their declarations:* `gateFlow`, `signFun`, `phaseFun`,
  `gateFlow_isolation` and `avail_conj_mul` (LiftAudit.lean:47, :582, :586, :660, :770); `unit` and
  `unit_mul_unit` (SecondOrderCircuit.lean:356, :392); `flow` (ReachabilitySeam.lean:95);
  `transition` (LieRankSource.lean:199); `PhaseFreeRichness` and `control_at_level`
  (MinimalRepertoire.lean:423, :452); `phaseGate_mul_self`, `gateFlow_isolation_flip`,
  `phaseFree_of_derivedOI_layerFlowExecutable` and `qm_of_derivedOI_layerFlowExecutable`
  (DerivedQ3.lean:66, :81, :207, :214); `onesTheory_no_quarter_flow`,
  `onesTheory_not_phaseFree(_general)`, `flow_endpoint_refuted(_general)`,
  `onesTheory_not_phasesAvailable` and `onesTheory_not_qm` (FlowEndpoint.lean:121–208); `rot` and
  `mixImage` (StateMixingCoupling.lean:44–51); `mixImage_not_preservesNonneg`
  (FrozenSourcing.lean:199); `obligations_independent` (C5Discovery.lean:59); `PhasesAvailable`
  and `derivedOI_of_qm` (RouteB.lean:132, :228); `exists_nonMonomial_of_layerFlowExecutable`
  (ExecSource.lean:52).
- Nothing was built and no working copy was kept.

**Verdict: ACCEPT WITH NITS.** No blocking issue was found.
- R4-B1 and R4-B2 are fixed correctly against their sources.
- Every r4 nit is applied, and each one is correct.
- The three narrower wordings the writer chose are correct in the text.
- One supporting argument in the dispositions is wrong for odd carriers (nit r5-n1). The text
  does not use it.
- The corrected phase/mixing relation is stated the same way at every site.
- The full re-read found no new error in a claim. The four nits are confined to the
  dispositions, the header and the coverage limits, or are optional.

***

## 1. R4-B1, R4-B2 and the r4 nits

| Item | Where in r5 | Verified |
|---|---|---|
| **R4-B1** | §0 item 8 (l.152–155); §5.1 (b) (l.537–566); §5.2 earliest mechanism (l.629–632), arrow 3 (l.646), summary (l.653–654); §5.3 phase row, state-mixing row, scoped bullet, third distinction (l.669–670, 685–698, 729–732); §6 (l.748, 753); §10 (l.1081–1085); §11 (l.1169–1170); DISPOSITIONS refinement | Correct. "With no phase input" is replaced by "with no phase operation in its repertoire (GR:250…)", which is GR:250's own statement about the listed repertoire. The text adds that the drive carries the phase, with the isolation form, the quarter-turn identity and the real-rotation countercontrol. Each of these is verified in §2. The merge is now "folded into", "carried inside" or "moved inside", "and is not removed", at every site (§3). |
| **R4-B2** | §5.3 phase row, *Open* (l.669) | Correct. The text now reads: "a mixing resource of the phase-free-richness form (the complex driven transition); moving the all-ones ray is necessary, not sufficient (GR:260; `phase-source-audit.md`:212–221)". GR:260 says "is not shown sufficient". :212–221 is the owner's quoted amendment, and the line numbers match. §6's *Complex phases* row carries the same wording (l.748). |
| r4-n1 | §5.1 (b) l.537–540; §5.3 third distinction l.729–730 | Correct. `flow_endpoint_refuted_general` is `SourcedOI ∧ LayerFlowExecutable ∧ ¬PhaseFreeRichness` for `onesTheory A` with `card A ≥ 2`. `onesTheory_not_phaseFree` and `onesTheory_not_qm` are on `Fin 2`. `phaseFree_of_derivedOI_layerFlowExecutable` uses only the phases and the exchanges of `DerivedOI` (its docstring), so "with the phase it does" is correct within the closure. |
| r4-n2 | §6 l.748, l.753 | Correct. The configuration-level source O1 is named, with the ray condition stated as necessary only. *Interference* now distinguishes "the layer flow together with a separate phase" from "a complex driven transition, which carries the phase". |
| r4-n3 | §5.3 l.706–714; §13 r4 entry | Correct. Both parts are exact algebra: the rationality argument under B3, and the closed form. Check V5 confirms CHSH $=3\cos\alpha-\cos3\alpha=6\cos\alpha-4\cos^3\alpha$. At $\cos\alpha=4/5$ all sixteen probabilities are rational and satisfy no-signalling, and CHSH $=344/125$. $P(a{=}b)=(2+\sqrt2)/4$ is irrational. The bound is still marked "not adopted here as an established claim". The §13 label is propagated. |
| r4-n4 | DISPOSITIONS nit table | Correct. A non-scalar $2\times2$ matrix is cyclic, so its centralizer is $\mathbb F_p[f_a]$, and the determinant is the algebra norm. In the field case $\det J=J\bar J=-J^2=1$. In the split case $\det(i,-i)=1$. In the dual case there is no non-scalar root. Check V6 enumerates every $J$ for all 158 pairs with odd $p\le31$ (a separate enumeration from R1 of the r4 review). The centralizer has $p^2$ elements. Every non-scalar root of $-1$ has determinant 1. Scalar roots have determinant $-1$. The existence criterion holds. |
| r4-n5 | DISPOSITIONS refinement opening | Correct. The refinement opens with *Where the owner's word holds as stated*. |
| r4-n6 | §5.1 (b) l.541–545, l.556–557; §5.3 l.670 | Correct. The pair block is $\begin{pmatrix}\cos t&-i\sin t\\-i\sin t&\cos t\end{pmatrix}$, which is monomial iff $\sin t\cos t=0$. The ratio of entry $a$ to entry $c$ in the image of $\mathbf 1$ is $e^{-it}$, so the drive moves the ray iff $t\notin2\pi\mathbb Z$. |

Changes not traced to a finding: header standing and coverage lines, §13 r5 entry, §10 label.
Each maps to an item in the dispositions' last table. All 19 hunks are accounted for.

***

## 2. Independent verification of the adopted algebra

All checks are in `review/probes/r5rev_checks.py`.
- *Hashes:* script `3c31465ee67927ca033e782fb611a14f6da13b60b3e75255be3c330bddc4d507`; output
  `r5rev_checks.out` `70d30ea64e2e2e3d6d765701e330296754d08ba3eb631a7c6bf6e93333bf1f30`.
- *Result:* 37 PASS, 0 FAIL. Two runs gave byte-identical output.
- *Method:* exact sympy, integers mod $p$, and exponent vectors mod 4. The probe imports no earlier
  script and runs no OI mechanism (#1211 c.6739843458).
- *Independence from the writer's probe:* the exponential is built from spectral projectors and
  cross-checked against sympy's `Matrix.exp`. Lie closures are computed in a real $2n\times2n$
  representation. The monomial-group question is settled by breadth-first search.

**Isolation form [A] (V1).** The claim is
$e^{-i\theta X_{ab}}=e^{-i\theta}\,G_{(ab)}(2\theta/\pi)\,\mathrm{diag}(1,1,e^{i\theta})$ for every
$\theta$. The diagonal factor commutes with $G_{(ab)}$, so the order of the factors does not
matter. Dropping the relative phase breaks the identity.

The derivation from the kernel was checked as follows.
- `gateFlow_isolation` states
  $\mathrm{diag}(\mathrm{phaseFun})\,G(t)\,(\mathrm{diag}(\mathrm{sign})\,G(t)\,\mathrm{diag}(\mathrm{sign}))=\mathrm{flow}(X_{a,\tau a})(\pi t)$,
  where `flow H t` $=\exp(-itH)$.
- V1 checks the general identity on a two-orbit involution $(0\,1)(2\,3)$ of five states, where
  `signFun` is non-trivial. It fails when the sign is dropped, which is a countercontrol on the
  reading of the theorem.
- For a single transposition, `signFun` is identically 1 (its condition needs a moved point
  outside the pair).
- `unit_mul_unit` gives $G(t)G(t)=G(2t)$.
- The three-state form follows with $\theta=\pi t$.

Labelling the result [A, from K `gateFlow_isolation` with `unit_mul_unit`] is correct. The kernel
does not state the three-state form, so K would be an overclaim.

**Quarter-turn identity (V2).** For $n=3,4,5$,
$e^{-i\frac\pi2X_{ab}}\,\mathrm{swap}(a\,b)=-i\,\mathrm{diag}(1,1,i,\dots,i)$.
- At $n=3$ its channel is the quarter phase on the third state.
- Transport by an exchange moves it to every state.
- On two states the product is the scalar $-i$.
- `avail_conj_mul` (LiftAudit.lean:770) holds for any `FiniteOperationalTheory`, so availability
  is closed under the composition.

**Real-rotation countercontrol (V4).** With permutation transport, the rotation generators close
on $\mathfrak{so}(n)$ and $iX$ closes on $\mathfrak{su}(n)$:

| $n$ | rotations | driven transition |
|---|---|---|
| 3 | 3 | 8 |
| 4 | 6 | 15 |

The conjugation channel of any real word sends the real matrix $E_{ac}+E_{ca}$ to a real matrix.
The quarter-phase channel on $c$ does not, so no real word acts as the quarter phase (the hand
argument is [A]). The text identifies its real rotation with the "pair rotation at a quarter
turn, which carries no phase at all" of `frozen-sourcing-audit.md`:289. That identification is
correct: the object there is `mixImage`/`rot θ`, the real matrix
$\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$
(StateMixingCoupling.lean:44–51; FrozenSourcing.lean:192–199).

**H-Bell closed form (V5)** and **determinant step (V6):** see §1, r4-n3 and r4-n4.

**Writer's probe.** `python3 -I probes/r5_generic_checks.py` was re-run. Its output is
byte-identical to `probes/r5_generic_checks.out` (copy at `review/probes/r5_generic_checks.rerun.out`,
`df300469…86a7`): 40 PASS, ALL PASS. Notes on it:
- It imports only `itertools` and `sympy`.
- The closed-form exponential is certified by its initial value and its ODE.
- Countercontrols are present for I, Q and the zero test.
- Monomiality in Y(b) is sampled, and its docstring says so. The text rests the
  monomiality statement on the hand argument [A], which is correct.
- R(c) checks one real word; the general statement is the hand argument.

None of the text's statements rests on the probe alone.

***

## 3. The writer's three narrower wordings

**(i) [A], not K, for the isolation form.** Correct, for the reasons in §2.

**(ii) Three-state scope, the mod-4 parity argument, and `derivedOI_of_qm`.**
- *The text is correct.* It claims the quarter phase from the quarter-turn identity only "on every
  state of a three-state level". For larger levels it says "the phases follow through the
  equivalence (K `derivedOI_of_qm`)", with implementation locality and embedded observation named
  in the same paragraph. That route is valid.
- *The supporting argument in the dispositions is wrong for odd $n\ge5$.* *Refinements of the
  review* item 2 says: on $n\ge4$ states the quarter-turn channels and the permutations "cannot
  isolate one state", because each generator has even coordinate sum mod 4. A global constant
  changes the sum by $nc$, so the invariant holds only for even $n$. Check V3 settles it by
  breadth-first search over the whole monomial group generated by all exchanges and quarter-turn
  drives:
  - $n=3$ (order 192): a single-state quarter phase is reachable.
  - $n=4$ (order 3072): not reachable.
  - $n=5$ (order 61440): reachable.
  - On the exponent lattice, $n=6$ is not reachable and $n=7$ is.

  An explicit word for $n=5$:
  $(e^{-i\frac\pi2X_{01}}\mathrm{swap}_{01})(e^{-i\frac\pi2X_{23}}\mathrm{swap}_{23})=-i\,\mathrm{diag}(1,1,1,1,i)$,
  whose channel is the quarter phase on the fifth state. This is nit r5-n1. It does not affect
  the text.
- *A more direct kernel route exists.* `control_at_level` (MinimalRepertoire.lean:452) takes
  `PhaseFreeRichness T` and gives every unitary conjugation channel at every level with three or
  more states. That includes the quarter phase on every state, with no use of implementation
  locality or embedded observation. Those two principles are needed only for levels with two or
  fewer states (`descend`, `control_of_phaseFree`). So the parity obstruction concerns quarter-turn
  products only and does not limit what the drive supplies. This strengthens R4-B1's conclusion
  that the drive carries the phase. The text's route through `derivedOI_of_qm` is correct but uses
  more hypotheses than it needs (optional nit r5-n2).

**(iii) Agreement with `phase-source-audit.md`:286–287.** Correct.
- The scope amendment (:227–229) concerns a quarter-turn transition flow that is "admissible in
  `onesClass`'s branch-wise closure". It says that moving the ray "does not by itself furnish a
  quarter phase".
- The flow-endpoint witness `onesTheory` does not even have the quarter-turn flow as an available
  channel (`onesTheory_no_quarter_flow`, FlowEndpoint.lean:121). So the witness concerns branch
  admissibility, not channel availability together with the exchanges.
- r5's identity needs channel availability, the exchange and a third state. On two states the
  product is a scalar (V2 control), so "by itself" holds.
- r5 cites only the owner's quote (:212–221), and nothing in r5 contradicts the branch reading.
- Read literally as a statement about an *available* quarter-turn flow with the exchanges on three
  or more states, :287's sentence (which lacks "by itself") would be false (V2; `control_at_level`).
  A dependency matrix that cites it should keep the branch reading, as the r4 review's aside said.

***

## 4. The corrected phase/mixing relation, everywhere

**What r5 states.**
- Beside the layer flow, which fixes the all-ones ray, the phase is a separate obligation
  (K `obligations_independent`).
- Under phase-free richness no separate phase *operation* is needed, because the complex driven
  transition carries the phase. The phase obligation moves inside the mixing obligation, as the
  requirement that the source be that transition and not a real rotation. It is not removed.

**Where it is stated, in the same terms:** l.152–155, 546–566, 629–632, 646, 653–654, 669, 670,
685–698, 729–732, 748, 753, 1081–1085 and 1169–1170, and the DISPOSITIONS refinement and its
plain-words section.

**Grep** of r5 and the dispositions for "phase-free in content", "no phase input",
"merge(s)", "discharg", "removes the obligation", "not a separate obligation/input" and "one
obligation fewer":
- r5 has no hit except "merge" in the authorization text (l.14, l.22).
- The dispositions' hits are the corrected framing ("it is not one obligation fewer"; "the merge
  is the phase obligation folded into the mixing obligation") and the R4-B1 row quoting the old
  wording.
- "Dispensable" occurs only as GR:258's quotation (l.151–152), immediately followed by the
  corrected relation.

**Owner record.** c.6741291498 item 1 ("If it is confirmed, the 'complex phases' candidate merges
with native mixing outside the layer flow"; "gives exact QM without a phase") is the owner-visible
wording that this correction refines. r5 does not cite that comment, and the dispositions do not
list it. The DISPOSITIONS refinement already gives the reading the matrix should record ("folded
into the mixing obligation … not one obligation fewer"). The coordinating session may want to
point the matrix to it explicitly (§6).

The scoped bullet's conclusion (l.695–698) is supported: the common target is shared with the
phase only if the mixing source moves the all-ones ray, and it is shared when the source is the
complex driven transition. V2 shows this at three states, and `control_at_level` at every level
with three or more states.

***

## 5. Full re-read

- **Unchanged passages.** §§1–4, §5 (S1–S29), §5.1's *Conditionality*, *Scope of necessity*,
  *Closest derived objects* and *Status*, §5.2 rows 1–5, §7–§9, §10's Q6 analysis, §12 and §13 are
  unchanged from r4 except as the dispositions record. A sample of their anchors was re-read at
  `fd539e15` and is correct: `obligations_independent` (statement as quoted), `PhasesAvailable`,
  `derivedOI_of_qm`, `exists_nonMonomial_of_layerFlowExecutable` (for any `genTheory 𝓘 arch S`,
  carrier `S × Fin 1`), Main:218, Main:590, SM:809, Sub:131 and Sub:133. No error in a claim was
  found outside the changed passages.
- **Claim/evidence boundary.** Each check is checked separately below.
  - *Negatives are stated for the class ruled out.* "A real rotation … with the permutations
    supplies no phase" applies to real rotations together with permutations. The phase-free
    negatives are tied to `onesTheory` with the sourced closure. FI-1's negative concerns the
    stated access on the configuration carrier.
  - *Necessity is not promoted to sufficiency:* R4-B2 is fixed, and "FI-1 not sufficient (`PolC`)"
    is kept.
  - *Conditionals keep their conditions:* phase-free richness is cited with locality and embedded
    observation at every QM conclusion.
  - *Witnesses are not promoted to theorems:* the [A] and K labels are correct (§2–§3).
- **Three-column separation.** It holds. Column (iii) is not counted as support anywhere, and r5
  adds no column-(iii) support.
- **§A.31 labels.** These are correct.
  - FI-1 is CONFIRMING.
  - The relation of the phase-free form to the phase is ELABORATING. Its parts are in
    `gateFlow_isolation`, GR:270 and `frozen-sourcing-audit.md`:289, and the added content is
    elementary algebra on them.
  - Nothing is labelled NEW. The `control_at_level` reading in §3(ii) would also be ELABORATING
    (GR:250 states it).
- **The three gaps in parallel.** §5.3 lists the phase (O1), state mixing (FI-1, with O2 as the
  layer-flow form) and H-Bell, each with its carrier, its scope, what is proved toward it, and what
  is open. The independence is stated in scoped senses:
  - phase and layer flow: K;
  - phase and FI-1 as predicates: a composition of K results;
  - phase and the mixing obligation: folded under the phase-free-richness form;
  - H-Bell: not derived, in the sources read.
- **The owner's three distinctions** (c.6740778880) are kept apart as distinctions (l.716–735):
  - configuration versus encoded carriers;
  - mathematically available versus derived;
  - generating coherent mixing versus the full probability and composition rules.
- **Authorization.** Nothing implies any:
  - the header quotes c.6738806776 and c.6739843458;
  - §12 records the c.6740537555 answers as taking effect only on a review ACCEPT;
  - unit 2 is not selected;
  - the r5 checks are generic and labelled, run under c.6739843458.
- **Small inconsistencies (nit r5-n4).**
  - The header's r5 line cites `frozen-sourcing-audit.md`:287–291, and the dispositions cite
    :284–291. Both cover :289.
  - §13 *Limits* (l.1281–1282) still bounds GR reading at "§3.3's opening and GR:260, GR:270",
    but r4 and r5 read GR:248–258 and GR:266 (header l.61, l.72). The search-scope statement is
    narrower than what was read, so it is not an overclaim.

***

## 6. Nits

- **r5-n1 (dispositions only; not in the text).** *Refinements of the review* item 2. The
  claim that quarter-turn channels with permutations cannot isolate one state on $n\ge4$ holds
  for even $n$ only. For odd $n\ge5$ they can (V3; the explicit $n=5$ word in §3(ii)). Correct the
  record to "even $n$" if the dispositions are carried into the matrix. The text is unaffected.
- **r5-n2 (optional; l.557–558, and the §5.3 phase row *Conditional*).** `control_at_level`
  (MinimalRepertoire.lean:452) gives the quarter phase on every state at every level with three or
  more states from phase-free richness alone. Locality and embedded observation are needed only
  for levels with two or fewer states. Citing it would replace "follow through the equivalence"
  with the direct kernel route, and would sharpen *Conditional* to say which hypotheses are used
  where. This is optional: the present wording is correct and only routes through more
  hypotheses.
- **r5-n3 (dispositions, plain-words section, last sentence).** "Beside the layer flow, which
  carries no phase" is loose. On the pair the gate flow at time $t$ is
  $e^{i\pi t/2}\,e^{-i(\pi t/2)X_{ab}}$, so at intermediate times it has complex entries. What
  holds is that it fixes the all-ones ray, and that with the sourced closure it supplies no quarter
  phase (`onesTheory_not_phasesAvailable`; `obligations_independent`). Suggested wording: "Beside
  the layer flow, which fixes the all-ones ray and with the sourced closure supplies no quarter
  phase, …". The text's own sentence (l.565–566) is correct.
- **r5-n4 (cosmetic).** The two coverage inconsistencies in §5.

***

## 7. Acceptance readiness

**No blocking issue.** The verdict is **ACCEPT WITH NITS**. None of the nits requires another
review round.
- r5-n1 and r5-n3 are corrections to the dispositions record.
- r5-n2 is optional.
- r5-n4 is cosmetic.

The owner can use this verdict to select unit 2 and to build the dependency matrix
(c.6740778880, c.6741291498). Under c.6740537555 it is the review ACCEPT on which two decisions
take effect:
- tracking the complex structure as its own item (F4);
- the separate correction unit.

This review confirms F4's premise: Theorem 5 asserts a stabilizer in $\mathrm U(6)$ with no
complex structure among its stated premises, and SM:809 names "the real-to-complex step" as open.
Under c.6738806776, an ACCEPT authorizes no computation, Lean work, freeze, manuscript change, PR
or merge.

**For the dependency matrix**, as the sources at `fd539e15` support it. Each entry gives a status,
its carrier and its assumptions.

| Pair | Status | Carrier | Basis |
|---|---|---|---|
| Phase (O1) and layer flow (O2) | Independent, proved (K) | Two-state carrier | `obligations_independent` |
| Phase and FI-1, as predicates | Neither implies the other, proved | `Fin 2` and general carriers | Composition of K results |
| Phase and the state-mixing obligation | Not independent in every form | See the next rows | See the next rows |
| — beside a layer-flow-form source | Phase is a separate input | — | Within the closure |
| — under the phase-free-richness form | Drive carries the phase; folded into the mixing obligation, not removed | Three-state level: quarter-turn identity [A]. Every level with ≥3 states: `control_at_level` [K]. Every level: with locality and embedded observation, through exact QM [K] | V2; `control_at_level`; `derivedOI_of_qm` |
| — a real-rotation source | Moves the ray, supplies no phase | — | [A] |
| H-Bell and the other two | Not derived from them and does not derive them, in the sources read; no independence theorem | Different object: a preparation-indexed rule on the SM/GR graph | Sources read |
