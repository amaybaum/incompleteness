# OI-SM-QM-BRIDGE unit 1: dispositions of the r3 review (r4)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Paper-only. No git or
GitHub write, no Lean work, no manuscript change, no computation on an OI mechanism.

- **Object revised:** `BRIDGE-UNIT1.md`. r3 sha256
  `ee1c83c04366ea62c73b3d256e44e8e7415e3561b9a0a5a7576a278892038219`, kept unchanged as
  `r3/BRIDGE-UNIT1.md`; r4 revised in place. Line numbers below are r4 lines unless marked r3.
- **Review:** `review/REVIEW-UNIT1-r3.md`, sha256
  `7a6a7f1cd0f5ce290497171127fe15a02b44e29402e8fe3a8dd92d1da33ecc27`, verdict REVISE (B1–B5,
  n1–n11). Reviewer probes `review/probes/r3rev_checks.py` read; not imported.
- **Writer's notes adopted with corrections:** `NOTES-r3-parallel-gaps.md` (sha256
  `cb439009…16ce`), C1–C4.
- **Owner records read with `gh api`:** #1211 c.6738806776, c.6739843458, c.6740537555; #1169
  c.6740778880 (amaybaum, 2026-11-09T13:05:46Z).
- **Sources:** read by the writer with `git show fd539e15:<path>` after `git fetch origin main`
  (`fd539e150759a6ea51ab279aeeac80fc06050ade`). Lean statements read at their declarations;
  nothing built.
- **Checks:** `probes/r4_generic_checks.py` (sha256
  `97e57b3c722a9565ed8da22c2c7b4d578ca5a4d824b4d2acbac74b8931b643cb`), output
  `probes/r4_generic_checks.out` (sha256
  `696f5108d1b46cae8115d1e3722a4be58f4b6cf01f22be7c60bfde3432f030bf`, 22 PASS, ALL PASS), run with
  `python3 -I`. Exact arithmetic on generic objects (integers mod $p$, exact $2\times2$/$3\times3$
  complex matrices, $\mathbb F_2$ rules on $K_{2,4}$, rational two-qubit matrices) under #1211
  c.6739843458; imports no earlier script; no OI mechanism. A first run failed two D checks
  because sympy did not simplify a matrix exponential; the drive was rewritten in closed form
  ($X^3=X$ asserted) and the script re-run; the output file is from the second run.

## Owner-visible refinement (B2)

#1169 c.6740778880 calls phase, FI-1 and H-Bell "independent unresolved obligations". The sources
support that only in scoped senses, and r4 states them (§0 item 8; §5.1 (b)–(c); §5.3 *The
independence, scoped*; §11). **This refines the owner's wording; the owner should see it.**
- *Phase and layer flow (O1, O2):* independent, kernel-proved on `Fin 2`
  (`obligations_independent`, C5Discovery.lean:59).
- *Phase and FI-1, as predicates:* neither implies the other (substratum theory: phases, monomial
  class; ones-fixing theory: non-monomial at level one, no phase), by composition of kernel
  theorems not stated as one theorem.
- *Phase and state mixing, as obligations:* **not independent in every form.** GR:250–256 and
  Main:590: phase-free richness (one continuously driven transition and the exchanges, "No phase
  operation enters"), with implementation locality and embedded observation, is equivalent to
  exact finite endomorphic operational QM (`oiPlusMin_iff_qm`, MinimalRepertoire.lean:569), which
  gives the phases (`derivedOI_of_qm`, RouteB.lean:228); GR:258: "the quarter phase is
  dispensable at every level". The layer flow, by contrast, fixes the all-ones ray
  (`gateFlow_mulVec_ones`) and with the sourced closure does not give phase-free richness
  (`flow_endpoint_refuted_general`, FlowEndpoint.lean:157). So the phase is a separate obligation
  beside a mixing source of layer-flow form and not beside one of phase-free-richness form; under
  the latter the phase branch merges into the mixing branch.
- *H-Bell and the other two:* not derived from each other in the sources read; no independence
  theorem; posed on a different object.

## Blockers

| Finding | Verified (writer's reading at `fd539e15`) | Change in r4 |
|---|---|---|
| **B1** parallel presentation only partly met | Owner text of #1169 c.6740778880 read verbatim. r3 gave the phase's carrier/scope only in §6 and §5.1(b), H-Bell's nowhere, and stated none of the three distinctions as distinctions. | C1 adopted with the review's corrections: new **§5.3** (l.623–691): table with carrier, scope, "proved toward it, and constraints", open, for phase, state mixing (FI-1; O2) and H-Bell; *The independence, scoped* (l.638–659); *H-Bell's target* (l.661–671); *Three distinctions* (l.673–691). Corrections applied in C1: phase-row scope restated (`PhasesAvailable` is an all-level availability requirement, RouteB.lean:132, not an exactness predicate; exact QM implies it, `derivedOI_of_qm`); B2 in the opening, the table and the third distinction; B3 (site factorization not listed as FI-1's carrier input); n2 carriers; n6 source wording; n7 M-FIX under constraints; n9 attribution; n11. C2 adopted with n8's wording and B2 (§5.2 *earliest missing mechanism*, l.590–599). C3 adopted with B2's scope (§11 last bullet, l.1118–1125). C4 adopted (§0 item 8 heading, l.130). |
| **B2** phase independence overgeneralized | GR:250 (phase-free richness; "No phase operation enters"; `bracket_XX`), GR:256 (box), GR:258 ("the quarter phase is dispensable at every level"), Main:590 (primitive-source refinement "with no phase operation"): both hold. Kernel: `PhaseFreeRichness` (MinimalRepertoire.lean:423) uses `flow (transition a b) t` $=e^{-itX_{ab}}$ (ReachabilitySeam.lean:95); `oiPlusMin_iff_qm` (:569); `derivedOI_of_qm` (RouteB.lean:228); `onesTheory_not_phaseFree` and `flow_endpoint_refuted_general` (FlowEndpoint.lean:144, :157), which the review did not cite and which make the scoping kernel-backed on the layer-flow side; `gateFlow_mulVec_ones` (InstrumentRealization.lean:491). The driven transition at $t\notin\frac{\pi}{2}\mathbb Z$ on ≥3 states sends $\mathbf 1$ to $e^{-it}(e_a+e_b)+\sum_{c\ne a,b}e_c$ [A]; exact check D. | Scoped wherever stated: §0 item 8 (l.137–147); §5.1 *Position* (b) (l.517–536); §5.1 *Not established* (l.559–562); §5.2 *earliest missing mechanism* (l.596–598); §5.2 arrow 3 (l.612), its right-hand column restated as two conditionals; §5.2 summary (l.615–621); §5.3 table, scoped-independence bullets and third distinction; §10 FI-1 label (l.1035–1037); §11 last bullet. The phase-free-richness route is added as the mixing form under which the phase is not a separate input. Owner-visible refinement recorded above. |
| **B3** FI-1 placed on site factorization and second-order form | `ReadWriteFamily (a b : S)` on two states of any finite `S` (ReadWriteControl.lean:86–89); `permTheory` generic; `obsTheory_rule_independent` (SubstratumInterfaceAudit.lean:780) and its docstring ("configuration-level sourcing consumes nothing of A3–A6"); `exists_nonMonomial_of_layerFlowExecutable` (ExecSource.lean:52) and `layerFlowExecutable_of_control` (LiftAudit.lean:117) for any finite `S`; GR:270 "whether or not it is a gate of that factorization". P1–P3 are stated on cells of class N (QP:124–150). | §5.1 *Conditionality* rewritten (l.411–431): FI-1 posed on the stated read/write access on any finite configuration carrier with a bijection; site factorization and the second-order form placed upstream of the carrier's physical reading and layers, the cell-based P1–P3/E-iso/H-PREP, the spatial route and S13, and H-Bell's graph. §5.2 *earliest unproved assumption* rewritten (l.579–589). §5.2 row 1 gains one sentence (l.572). §0 item 8 (l.149–151, l.165–167) and §11 last bullet carry the same placement. |
| **B4** false $\mathbb Z_q$ scope guard | Refuted: $J_0^2=-I$ over every $\mathbb F_p$ (exact check J(a), $p\le13$). The reviewer's criterion is correct, and here proved by hand for odd prime $p$: a symplectic ($\det=1$) $J$ with $J^2=-I$ commuting with the non-scalar $f_a$ lies in $\mathbb F_p[f_a]\cong\mathbb F_p[x]/(x^2-ax+1)$ and is non-scalar; if $a^2-4$ is a non-square the algebra is $\mathbb F_{p^2}$ and a non-scalar root of $-1$ exists iff $-1$ is a non-square mod $p$; if $a^2-4$ is a nonzero square it is $\mathbb F_p\times\mathbb F_p$ and a non-scalar root $(i,-i)$ exists iff $-1$ is a square; if $a=\pm2$ it is $\mathbb F_p[\varepsilon]$ and every root of $-1$ is scalar. Together: existence iff $\big(\frac{4-a^2}{p}\big)=1$ [A]; exact check J(b) agrees on all 39 pairs, with the null-mode countercontrol. Corpus: no source states the guard. | Deleted from §5.2 row 5 (l.576) and from NQ1 (l.1073–1075), which keeps only the point it served (question posed on the real lift; a positive answer does not source a complex structure at the fundamental level, alphabet $\mathbb Z/q\mathbb Z$, SM:312). The correct criterion is not added to the text, because nothing there uses it (the review's §2 B4 says the same). |
| **B5** "excluded" for the lift formulations | `lift-source-audit.md`:250–270 (scope amendment: "no formulation that lands derives either target"; nonreversible L1 and other L2 realizations not classified); GR:270 ("whether every realization of those channels is configuration-level is not decided"). | §5.2 row 3 (l.574) and row 5 (l.576): "excluded under stated conditions" kept for the stated access only; the lift formulations get **not derived** ("derive neither target") with the undecided realizations in the same cell. "Not derived" added to the status terms (l.566–567). §5.1 and §0 "not supplied … by any stated lift formulation" kept, as the review advises. |

## Nits

| Finding | Verified | Change in r4 |
|---|---|---|
| **n1** H-Bell "does not wait on FI-1" | Sub:131 (preparation-indexed adjacency on $G(x)$); Main:566 is a single-system construction; Main:362 (unrestricted class, PR box); Sub:133 (iii). | §0 item 8 (l.144–147) and §5.1(c) (l.536–543): "not derived from FI-1 and does not derive it in the sources read", grounded first in H-Bell being posed within bijective dynamics, Main:566/584 second, with their limits; no independence theorem claimed. |
| **n2** carriers of witnesses | `obligations_independent` (C5Discovery.lean:59–63), `polarizedTheoryC_derivedOI`/`_not_qm`/`_phasesAvailable` (PolarizationClosure.lean:606, :620, :448), `uncountableNonMonomialRays_of_qm` (CoherentContinuumSource.lean:195): all on `Fin 2`. `polarizedTheoryC_not_layerFlowExecutable` (:389) is carrier-general. | "on the two-state carrier" added at §0 item 8, §5.1 *Scope of necessity*, *Source anchors*, *Position* (b), §5.2 arrow 3, §5.3. `genTheory 𝓘 arch S` named as the class in which the necessity is proved (l.434–436); the `Fin 2` scope of `uncountableNonMonomialRays_of_qm` and the unstated general-carrier composition added (l.450–452). *Partial refusal:* the review says `genTheory` "is what 'within the structural architecture' means". GR:266 uses "structural architecture" for the closure with the phase stated, which is narrower than an arbitrary architecture, so r4 says only that `genTheory` is the class in which the theorem is proved. |
| **n3** typed form | Main:590: "Its typed form removes the endomorphic qualifier", citing `typed_determined_iff`, `typed_determined_of_oiPlusMin`, in the primitive-/substratum-source passage, before the layer-flow sentence. | §5.2 arrow 4 (l.613): typed form attributed to the primitive-source equivalence; its statement for the layer-flow closure form recorded as not stated. |
| **n4** K1's c2 does not isolate linearity | r3 K1 c2 adds the same-colour read through an AND (r3 probe, `g_samecolour`). | New exact check L on $K_{2,4}$: linear opposite-colour control holds; linear rule with one same-colour read breaks the split. §10 citation extended (l.964–966). |
| **n5** "three formulations that name anything on the carrier" | `lift-source-audit.md`:95–102: L4 "no operation named (D1, D2)", tested by countermodel T4; verdicts :297–300. | §5.2 row 5: "the three formulations the lift-source audit tests (L1, L2, L4)". |
| **n6** "realizes the quantum Bell set" | Sub:129 (M1-B maps E2 to the ontically parameter-dependent Bell composite), Sub:131, Sub:133. | §6 Bell row (l.707) and §5.3 H-Bell scope use the source wording: ontic parameter dependence M1-B requires for the observed violation E2, with (i)–(iii). |
| **n7** M-FIX placement | MECH-2 DESIGN:543–567 ("a necessary condition derived from H-Bell, not an added requirement"); DESIGN:11 "promotes no claim". | §5.3 H-Bell row: under "Constraint on any H-Bell mechanism", with the record's standing. |
| **n8** "no single earliest" | — | §5.2: "The sources read establish no order among three missing mechanisms" (l.590). |
| **n9** attribution | #1169 c.6740778880: "state mixing remains a promising common research target"; "the shared-gap convergence remains provisional". | §5.3 opening (l.625–630) attributes both; §5.3 scoped bullets state when the target is shared with the phase. |
| **n10** §12 Q1–Q2 answered | #1211 c.6740537555, quoted verbatim; both take effect only on an ACCEPT. | §12 items 1–2 (l.1134–1146) record the answers, quotations and condition; F4 confirmation by the r1–r3 reviews noted. |
| **n11** H-Bell not outcome statistics alone | Sub:133 (iii). | §5.3 H-Bell scope: "Condition (iii) is geometric, so H-Bell is not an outcome-statistics condition alone"; §0 item 8 names the curvature-stability condition. |

## H-Bell exactness

Recorded in §5.3 (l.661–671): the sources state no exactness qualifier (grep of `H-Bell` in Sub,
Main, GR, SM at `fd539e15`; Sub:129–133, Main:414, Main:429 read); the finite-accuracy reading is
recorded as the r3 review's reading, adopted. The reviewer's rationality bound and the
CHSH $=344/125$ witness are included only as *reviewer-supplied, computation-supported, not
adopted as an established claim*; exact check B re-verifies the witness and the irrationality
independently.

## Refusals and refinements of the review

1. **n2, in part:** `genTheory` is not identified with "the structural architecture" (row n2).
2. **Review §6, "earliest unproved assumptions … the stated read/write access with the phase,
   which are what FI-1's negative uses":** refined. FI-1's negative does not use the phase: the
   observer theory lacks it (`obs_not_phasesAvailable`), and the substratum class, which contains
   it, is monomial as well (`substratumClass := IsMonomial`, StructuralClosure.lean:180). r4 says
   the phase enters FI-1's position as first, not its statement or negative (l.583–585, l.430–431).
3. **B4's criterion:** the review labels it computation-supported for $p\le13$; r4's
   dispositions give a hand proof for every odd prime (B4 row). It is still not placed in the
   text.

No finding is refused outright.

## Changes not traced to a review finding

1. Header standing line (l.3–5) names r4 and the r3 review; authorization bullet names the r4
   checks (l.18–19).
2. Header coverage: an "r4" reading line (l.60–70) listing what was read for B2–B5 and the nits.
3. §13: r4 checks entry (l.1197–1209) and the r4 declaration-reading sentence (l.1215–1216).
4. §12 item 3: "§5.2 and §5.3 list" (C4 cross-reference, l.1149–1150).
5. §5.1 *Statement* and the other unchanged parts of §5.1 are as in r3.

The diff r3 → r4 (`git diff --no-index -U0`) has 30 hunks; each falls under one of the rows
above.
