# OI-SM-QM-BRIDGE unit 1: dispositions of the r4 review (r5)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Paper-only. No git or
GitHub write, no Lean work, no manuscript change, no computation on an OI mechanism.

- **Object revised:** `BRIDGE-UNIT1.md`. r4 sha256
  `4e97610df18a8f6a9e8a89486ea3633cc3609bcbd6a2c9686f3ad780af2885e2`, kept unchanged as
  `r4/BRIDGE-UNIT1.md`; r5 revised in place, sha256
  `78f1098ee4310b0a190e211add27094025f95d3d1fa7d9b0fd77eaf260cf91a4` (1288 lines). Line numbers
  below are r5 lines unless marked r4.
- **Review:** `review/REVIEW-UNIT1-r4.md`, sha256
  `e489fc19f29240d5f57a6d80c543f4f390dedd61b251875bc4fa7ce63b0c2bc7`, verdict REVISE (R4-B1,
  R4-B2, r4-n1–r4-n6). Reviewer probe `review/probes/r4rev_checks.py` read; not imported.
- **Sources:** read by the writer with `git show fd539e15:<path>` after `git fetch origin main`
  (`fd539e150759a6ea51ab279aeeac80fc06050ade`): GR:248–272 (line map checked: 250 phase-free
  richness, 256 box, 258 "the quarter phase is dispensable at every level", 260 substratum-source
  form, 266–270 layer-flow form); Main:590 ("with no phase operation"); `phase-source-audit.md`:
  207–232 and 283–290; `frozen-sourcing-audit.md`:284–291. Lean, at their declarations, nothing
  built: `gateFlow` (OB/LiftAudit.lean:47), `unit` and `unit_mul_unit`
  (OB/SecondOrderCircuit.lean:356, :392), `signFun`, `phaseFun` and `gateFlow_isolation`
  (OB/LiftAudit.lean:582, :586, :660), `avail_conj_mul` (:770), `phaseFree_of_layerFlowExecutable`
  (:780 ff., where `gateFlow_isolation` and `avail_conj_mul` are used together), `transition`
  (OB/LieRankSource.lean:199), `flow` (OB/ReachabilitySeam.lean:95), `PhaseFreeRichness`
  (OB/MinimalRepertoire.lean:423), `phaseGate_mul_self`, `gateFlow_isolation_flip` and
  `phaseFree_of_derivedOI_layerFlowExecutable` (OB/DerivedQ3.lean:66, :81, :207),
  `onesTheory_no_quarter_flow`, `onesTheory_not_phaseFree(_general)`,
  `flow_endpoint_refuted_general`, `onesTheory_not_phasesAvailable`, `onesTheory_not_qm`
  (OB/FlowEndpoint.lean:121, :130/:144, :157, :180, :208).
- **Checks:** `probes/r5_generic_checks.py` (sha256
  `db07e9fe1deab56890e67d6b1d4f2afb1c0d8ae991f5771c49b98d48d5ea9933`), output
  `probes/r5_generic_checks.out` (sha256
  `df300469555e79a73ddc0ec621793fc1a57734db2761edda3e7713af267186a7`; 40 PASS, 0 FAIL, ALL PASS),
  run twice with `python3 -I`, outputs byte-identical. Exact sympy with a symbolic real angle on
  generic objects (hand-built $2\times2$–$4\times4$ complex matrices; two-qubit matrices) under
  #1211 c.6739843458; imports no earlier script; no OI mechanism; no kernel object imported or
  run. The closed-form drive is certified as the exponential by $U(0)=I$ and
  $U'=-iXU$. Countercontrols: the isolation identity fails without the relative phase; the
  exchange alone does not act as the quarter phase; on two states the quarter-turn drive times
  the exchange is a scalar; a nonzero matrix is rejected by the zero test.

## Owner-visible refinement (B2, as corrected for R4-B1 and r4-n5)

#1169 c.6740778880 calls phase, FI-1 and H-Bell "independent unresolved obligations".

**Where the owner's word holds as stated.** For the phase and FI-1 *as predicates* the owner's
"independent" holds without qualification: neither implies the other (below). It also holds,
kernel-proved, for the phase and the *layer flow*. The refinement narrows nothing there. It
concerns only the phase and the state-mixing *obligation*, which is stronger than FI-1, and H-Bell,
for which the sources give non-derivation, not an independence theorem. **The owner should see
it.**
- *Phase and layer flow (O1, O2):* independent, kernel-proved on `Fin 2`
  (`obligations_independent`, C5Discovery.lean:59).
- *Phase and FI-1, as predicates:* neither implies the other (substratum theory: phases, monomial
  class; ones-fixing theory: non-monomial at level one, no phase), by composition of kernel
  theorems not stated as one theorem.
- *Phase and state mixing, as obligations:* **the phase obligation is folded into the mixing
  obligation under one form of mixing; it is not one obligation fewer.** GR:250–256 and Main:590:
  phase-free richness (one continuously driven transition and the exchanges; "No phase operation
  enters", a statement about the listed repertoire), with implementation locality and embedded
  observation, is equivalent to exact finite endomorphic operational QM (`oiPlusMin_iff_qm`),
  which gives the phases (`derivedOI_of_qm`). The drive $e^{-i\theta X_{ab}}$ is complex and
  carries the phase: on three states it equals
  $e^{-i\theta}\,G_{(ab)}(2\theta/\pi)\,\mathrm{diag}(1,1,e^{i\theta})$, the transposition's
  layer flow times a continuous relative phase (the single-transposition case of
  `gateFlow_isolation` with `unit_mul_unit`), and at a quarter turn, composed with the exchange,
  it is $-i\,\mathrm{diag}(1,1,i)$, the quarter phase on the third state as a channel. A real
  rotation moves the all-ones ray and mixes states, but with the permutations generates only
  $\mathfrak{so}(3)$ and no phase. So: beside a mixing source of layer-flow form (which fixes the
  all-ones ray; with the sourced closure and without the phase it does not give phase-free
  richness, `flow_endpoint_refuted_general`) the phase is a separate obligation; under the
  phase-free-richness form no *separate phase operation* is needed, because the complex driven
  transition contains the phase, and the phase obligation becomes the requirement that the mixing
  source be that complex transition, not a real rotation. It is moved, not removed. For the
  owner's matrix: the merge is the phase obligation folded into the mixing obligation.
- *H-Bell and the other two:* not derived from each other in the sources read; no independence
  theorem; posed on a different object.

## Blockers

| Finding | Verified (writer's reading at `fd539e15`) | Change in r5 |
|---|---|---|
| **R4-B1** "no phase input" and the merge framing overstate GR:250 | GR:250 "No phase operation enters" and Main:590 "with no phase operation" list the repertoire. `PhaseFreeRichness` (MinimalRepertoire.lean:423) requires `flow (transition a b) t` $=\exp(-itX_{ab})$ with `transition a b` $=E_{ab}+E_{ba}$ (LieRankSource.lean:199; ReachabilitySeam.lean:95). `gateFlow σ t = unit (permMat σ) t` $=1+(e^{i\pi t}-1)\frac{1-P}{2}$ (LiftAudit.lean:47; SecondOrderCircuit.lean:356). `gateFlow_isolation` (LiftAudit.lean:660) is $\mathrm{diag}(\mathrm{phaseFun})\,G(t)\,(\mathrm{diag}(\mathrm{sign})\,G(t)\,\mathrm{diag}(\mathrm{sign}))=\exp(-i\pi t X_{a,\tau a})$, with `phaseFun` $=e^{-i\pi t}$ on moved and 1 on fixed configurations (:586) and `signFun` $\equiv1$ when $\tau$ is one transposition (:582). With `unit_mul_unit` ($G(t)G(s)=G(t+s)$, :392) and $\theta=\pi t$ this is $e^{-i\theta X_{ab}}=e^{-i\theta}G_{(ab)}(2\theta/\pi)\,\mathrm{diag}(1,1,e^{i\theta})$ on three states. So the identity is a *consequence* of the kernel theorem with the group law, which r5 labels [A], not K. Hand check: on the pair, $e^{-i\theta X}=e^{-i\theta}\frac{1+X}{2}+e^{i\theta}\frac{1-X}{2}=e^{-i\theta}G(2\theta/\pi)$; on $c$, $1=e^{-i\theta}\cdot1\cdot e^{i\theta}$. Quarter turn: $-iX\cdot X=-i$ on the pair, $1$ on $c$. Real rotation: real orthogonal; with permutation conjugates, Lie closure dimension 3. Exact checks I, Q, R. `avail_conj_mul` (:770) closes availability under the composition. GR:270 states the relation from the layer-flow side ("the resource named here is the smaller one"); `gateFlow_isolation_flip` (DerivedQ3.lean:81) is the converse with the sign flip, "No continuous phase enters". `frozen-sourcing-audit.md`:289: "the pair rotation at a quarter turn, which carries no phase at all". | Every site restated so that the drive carries the phase and the phase obligation moves into the mixing obligation: §0 item 8 (l.152–155); §5.1 (b) (l.537–565), with the isolation form, the quarter-turn identity, the real-rotation countercontrol and the sentence "no separate phase operation is needed because the complex driven transition contains the phase: the phase obligation moves inside the mixing obligation … and is not removed"; §5.2 earliest-mechanism bullet (l.629–632); §5.2 arrow 3 (l.646), "with no phase input" → "with no phase operation in its repertoire (GR:250–258 …), the complex drive carrying the phase", and the left column and last clause qualified; §5.2 summary (l.653–654), "merges into" → "is carried inside … and is not removed"; §5.3 phase row *Conditional* (l.669); §5.3 state-mixing row *Two forms* (l.670), "with no phase input" replaced; §5.3 scoped bullet (l.685–698), with the review's sentence; §5.3 third distinction (l.729–732); §6 *Interference* (l.753, also r4-n2); §10 FI-1 label (l.1081–1085); §11 (l.1169–1171). Re-grep: zero hits for "no phase input", "merges", "not a separate obligation", "not a separate input", "discharge the phase". |
| **R4-B2** ray-moving condition stated as sufficient | GR:260: "necessary to any access that supplies the phases, and is not shown sufficient". `phase-source-audit.md`:212–221 (owner, quoted): "Do not describe the ray-moving condition alone as *the* missing access sufficient to source the conjunct"; :286–287. Exact check R: the real rotation moves the ray, generates $\mathfrak{so}(3)$ with the permutations, and its channels send a real matrix to a real matrix, unlike the quarter phase. | §5.3 phase row *Open* (l.669): "… of the configuration-level phase or of a mixing resource of the phase-free-richness form (the complex driven transition); moving the all-ones ray is necessary, not sufficient (GR:260; `phase-source-audit.md`:212–221): a real rotation moves it and, with the permutations, supplies no phase (§5.1 (b))". |

## Nits

| Finding | Verified | Change in r5 |
|---|---|---|
| **r4-n1** scope of the flow-endpoint negatives | `flow_endpoint_refuted_general` (FlowEndpoint.lean:157) is `SourcedOI ∧ LayerFlowExecutable ∧ ¬PhaseFreeRichness` for `onesTheory A`; `onesTheory_not_phaseFree` and `onesTheory_not_qm` are on `Fin 2` (:144, :208); `phaseFree_of_derivedOI_layerFlowExecutable` (DerivedQ3.lean:207) gives phase-free richness with the phase. | §5.1 (b) (l.537–540): "with the sourced closure and without the phase, does not give phase-free richness (K `onesTheory_not_phaseFree`, on the two-state carrier, and `flow_endpoint_refuted_general`); with the phase it does (K `phaseFree_of_derivedOI_layerFlowExecutable`)". §5.3 third distinction (l.729–730): "not from the layer flow with the sourced closure and without the phase, on the two-state carrier (K `onesTheory_not_qm`)". |
| **r4-n2** §6 propagation | §5.3 *Open* names the configuration-level source; the *Interference* row's "together with a native phase" fits the layer-flow form only. | *Complex phases*, last column (l.748): configuration-carrier source (O1) or the complex driven transition, ray condition necessary not sufficient (§5.3), then the encoded carrier; "for the carrier" → "For the six-link carrier", needed once the configuration carrier is named in the same cell. *Interference*, last column (l.753): "the layer flow (beam-splitter) together with a separate phase, or a complex driven transition, which carries the phase (§5.1 (b))". |
| **r4-n3** H-Bell bound is [A] (optional; applied) | Hand check: for $\lvert\Phi^+\rangle$ and observables in the x-z plane, $E(x,y)=\cos(x-y)$; with angles $0,2\alpha$ and $\alpha,-\alpha$, CHSH $=3\cos\alpha-\cos3\alpha=6\cos\alpha-4\cos^3\alpha$, $=344/125$ at $\cos\alpha=4/5$. Exact check H (all $\alpha$). The rationality argument is a written argument given B3. | §5.3 (l.706–712): label "*Reviewer-supplied bound, not adopted here as an established claim*; both its parts are exact algebra [A]", closed form added. §13 r4 entry (l.1257–1258): "computation-supported" and the "except the reviewer-supplied bound" clause removed, since that bound no longer rests on the check alone (§A.25 propagation of the label). |
| **r4-n4** determinant step of B4's hand proof (dispositions only) | A non-scalar $2\times2$ matrix is cyclic, so $\mathbb F_p^2$ is a free rank-one module over $\mathbb F_p[f_a]$ and $\det$ of an element of that algebra is its algebra norm. *Field case* ($a^2-4$ a non-square): a non-scalar root $J$ of $x^2+1$ has conjugate $\bar J=-J$, the other root, so $\det J=J\bar J=-J^2=1$. *Split case* ($a^2-4$ a nonzero square): $J=(i,-i)$, $\det J=i\cdot(-i)=1$. *Dual case* ($a=\pm2$): no non-scalar root. The scalar roots $\pm i$ have $\det=-1$ and are excluded. So every non-scalar root is symplectic, and the existence direction holds. | None in the text (the criterion is not used there). |
| **r4-n5** open the refinement with what holds as stated | — | Refinement above opens with *Where the owner's word holds as stated*: for the phase and FI-1 as predicates, and for the phase and the layer flow. |
| **r4-n6** $t\notin\frac{\pi}{2}\mathbb Z$ is for non-monomiality only (optional; applied) | Pair block $\begin{pmatrix}\cos t&-i\sin t\\-i\sin t&\cos t\end{pmatrix}$: monomial iff $\sin t\cos t=0$. Image of $\mathbf 1$: entry $a$ over entry $c$ is $e^{-it}$, so on the ray iff $t\in2\pi\mathbb Z$. Exact check Y. | §5.1 (b) (l.541–545): moves the ray "at every $t\notin2\pi\mathbb Z$; it is non-monomial at $t\notin\tfrac{\pi}{2}\mathbb Z$, a restriction needed for non-monomiality only"; §5.3 *Two forms* (l.670): "at intermediate times" → "at every $t\notin2\pi\mathbb Z$"; §5.1 (b) l.557: at the quarter turn "the drive is monomial and still moves the all-ones ray". |

## Refinements of the review

1. **Kernel status of the isolation form.** The task brief and the review say the three-state
   identity holds "by the kernel's `gateFlow_isolation`". The kernel theorem is the general
   three-factor product for any involution; the three-state form is its single-transposition case
   combined with `unit_mul_unit`. r5 labels it [A] and cites both theorems, rather than K.
2. **Scope of the quarter-turn identity.** It gives the quarter phase on every state of a
   *three-state* level (review §2 says the same). On $n\ge4$ states the same product is
   $-i\,\mathrm{diag}(1,1,i,\dots,i)$, the quarter phase on the complement of the pair, and the
   diagonal products of such channels with permutations cannot isolate one state: in quarter-turn
   exponents mod 4, modulo a global constant, each generator has even coordinate sum and a single
   state has odd sum [A, hand argument]. r5 therefore says "of a three-state level" and adds "On
   larger levels the phases follow through the equivalence (K `derivedOI_of_qm`)" (l.557–558).
   The phases at every level still follow from phase-free richness, through exact QM.
3. **Consistency with `phase-source-audit.md`:227–229, :286–287.** "Moving the ray by such an
   operator does not by itself furnish a quarter phase" concerns the flow alone, in `onesClass`'s
   closure. r5's identity needs the exchange and a third state; on two states the product is a
   scalar (exact check Q, countercontrol). r5 does not cite that sentence; the branch reading of
   the review's §2 aside is not contradicted.

No finding is refused.

## Changes not traced to a review finding

1. Header standing line (l.3–6) names r5 and the r4 review; authorization bullet names the r5
   checks (l.19).
2. Header coverage: an "r5" reading line (l.72–78) listing what was read for R4-B1, R4-B2 and the
   nits.
3. §13: r5 checks entry (l.1259–1272); the declaration-reading sentence names r5 (l.1279–1280).
4. §10 FI-1 bullet (l.1081–1085): the §A.31 label for the adopted content, ELABORATING, with its
   parts in `gateFlow_isolation`, GR:270 and `frozen-sourcing-audit.md`:289 (review §2 gives the
   same classification). Nothing is labelled NEW.

The diff r4 → r5 (`git diff --no-index -U0`) has 19 hunks; each falls under one of the rows
above.

## Corrected relation between phase and mixing, in plain words

Under phase-free richness there is no separate phase *operation*, because the one driven
transition is complex: it is the layer flow with a continuous relative phase attached, and at a
quarter turn, with an exchange, it is the quarter phase. The phase has not gone away. It has moved
inside the mixing requirement, which now says the mixing source must be that complex transition.
A real rotation would also mix states and move the all-ones ray, but it gives no phase. Beside the
layer flow, which carries no phase, the phase remains a separate obligation.
