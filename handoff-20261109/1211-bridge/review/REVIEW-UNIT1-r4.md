# Review of OI-SM-QM-BRIDGE unit 1, revision r4 (BRIDGE-UNIT1.md)

**Reviewer.** A fresh, independent reviewer (Claude Code subagent, 2026-11-09). The review is
paper-only and full-text. It made no git write, GitHub write or Lean action, and no manuscript
change. It authorizes nothing. A review ACCEPT would not authorize a freeze, an implementation, a
manuscript change or a merge (#1211 c.6738806776). The two owner decisions of c.6740537555 that take
effect on an ACCEPT are not triggered, because the verdict is REVISE.

**Objects.** Hashes were verified before reading.
- `BRIDGE-UNIT1.md` (r4): `4e97610df18a8f6a9e8a89486ea3633cc3609bcbd6a2c9686f3ad780af2885e2`,
  read in full (1224 lines).
- `DISPOSITIONS-UNIT1-r4.md`: `9dcf139060ce962b421cf1e44860111d658f5fc35c6f0c8a18d5329b298a5a34`.
- `r3/BRIDGE-UNIT1.md`: `ee1c83c0…8219`.
- `review/REVIEW-UNIT1-r3.md`: `7a6a7f1c…3ecc27`; the earlier reviews `3cdf7dc2…`, `e242a794…`.
- `NOTES-r3-parallel-gaps.md`: `cb439009…16ce`.
- `probes/r4_generic_checks.py`: `97e57b3c…43cb`; output `696f5108…30bf`.

**Owner records**, read with `gh api`: #1211 c.6738806776, c.6739843458, c.6740537555; #1169
c.6740778880 (13:05:46Z) and c.6741291498 (13:30:54Z). r4's dispositions do not list c.6741291498,
which postdates them; nothing in it requires a change to r4 beyond what §2 below says.

**Sources.** Read with `git show fd539e15:<path>` after `git fetch origin main`
(`fd539e150759a6ea51ab279aeeac80fc06050ade`): GR:248–272; Main:362, 403–416, 429, 590; Sub:127–133;
SM:340–344, SM:809; `lift-source-audit.md`:93–103, 248–302; `phase-source-audit.md`:205–315;
`frozen-sourcing-audit.md`:280–296; MECH-2 DESIGN head and :540–568; and, at their declarations,
`flow`, `transition`, `PhaseFreeRichness`, `OIPlusMin`, `oiPlusMin_iff_qm`, `PhasesAvailable`,
`DerivedOI`, `derivedOI_of_qm`, `SourcedOI`, `sourcedOI_qm_iff_phaseFree`, `obsTheory`,
`obsTheory_rule_independent`, `obs_availExt_le_substratum`, `ReadWriteFamily`, `substratumClass`,
`gateFlow`, `unit`, `LayerFlowExecutable`, `layerFlowExecutable_of_control`, `avail_conj_mul`,
`gateFlow_isolation`, `gateFlow_mulVec_ones`, `onesTheory`, `onesTheory_no_quarter_flow`,
`onesTheory_not_phaseFree(_general)`, `flow_endpoint_refuted(_general)`,
`onesTheory_not_phasesAvailable`, `onesTheory_not_qm`, `onesFixing_not_phasesAvailable`,
`obligations_independent`, `exists_nonMonomial_of_layerFlowExecutable`,
`phaseFree_of_derivedOI_layerFlowExecutable`, `qm_of_derivedOI_layerFlowExecutable`,
`derivedOI_qm_iff_layerFlowExecutable'`. Every file:line in r4's header r4-reading line was checked
and is correct. No working copy was kept; nothing was built.

**Verdict: REVISE.** Every r3 finding is fixed, and fixed correctly against its source (§1). The
writer's two refinements of the r3 review are correct (§3). The §5.3 table is accurate cell by
cell except one cell (§4). Two blockers remain, both in the phase/mixing passage that B2 rewrote:
- **R4-B1.** "With no phase input" (§5.2 arrow 3; §5.3 state-mixing row) and the merge framing
  carried to the owner (§5.3, DISPOSITIONS *Owner-visible refinement*) omit that the driven
  transition of phase-free richness *carries* the phase. It is the layer flow of the transposition
  times a continuous relative phase, and at a quarter turn, composed with the exchange, it is the
  quarter phase on a third state. "No phase operation enters" (GR:250) is a statement about the
  repertoire, not about the drive's content.
- **R4-B2.** The phase row's *Open* cell lists "a mixing resource that moves the all-ones ray" as
  what would close the phase gap. Moving the ray is necessary and not sufficient (GR:260; the
  owner's scope amendment in `phase-source-audit.md`:212–221). A real rotation moves the ray and
  generates no phase.

There are six nits. A delta review of the passages named in §7 is enough if nothing else changes.

***

## 1. The r3 findings

| Item | Fixed in r4 | Correct against source |
|---|---|---|
| B1 | New §5.3: table, *The independence, scoped*, *H-Bell's target*, *Three distinctions*; §0 item 8 cross-reference; §5.2 *earliest missing mechanism*; §11 | Yes. Each gap has its carrier and scope. The three distinctions are stated as distinctions. Cell check: §4. |
| B2 | §0 item 8; §5.1(b); §5.1 *Not established*; §5.2 earliest-mechanism bullet, arrow 3, summary; §5.3; §10 FI-1 label; §11 | Yes in scope, with R4-B1 and R4-B2 remaining. `PhaseFreeRichness` (MinimalRepertoire.lean:423) drives `flow (transition a b) t` $=e^{-itX_{ab}}$ (ReachabilitySeam.lean:95, LieRankSource.lean:199), with no phase operation listed; `oiPlusMin_iff_qm` (:569); `derivedOI_of_qm` (RouteB.lean:228); GR:258 "the quarter phase is dispensable at every level"; Main:590 "with no phase operation". `flow_endpoint_refuted_general` (FlowEndpoint.lean:157) is `SourcedOI (onesTheory A) ∧ LayerFlowExecutable (onesTheory A) σ ∧ ¬ PhaseFreeRichness (onesTheory A)`, for every carrier with ≥2 states and every involution. It is correctly cited as "with the sourced closure" in DISPOSITIONS and §5.3, but not in §5.1(b) (nit r4-n1). The formula $e^{-it}(e_a+e_b)+\sum_{c}e_c$ is right for all $t$ (R2(a)). Every "independent" sentence (grep: l.137–147, 520–533, 561, 612, 618, 638–659, 1036, 1120) is scoped to the layer flow, to FI-1 as a predicate, or to non-derivation for H-Bell. |
| B3 | §5.1 *Conditionality*; §5.2 earliest-assumption bullet; §5.2 row 1; §0 item 8; §11 | Yes. `ReadWriteFamily (a b : S)` is defined on two states of any finite `S` (ReadWriteControl.lean:86–89). `obsTheory 𝒮 := permTheory 𝒮.Conf` and `obsTheory_rule_independent` (docstring: "Configuration-level sourcing consumes nothing of A3–A6"). `obs_availExt_le_substratum` comes from the carrier-generic `permTheory_availExt_le_substratum`. `exists_nonMonomial_of_layerFlowExecutable` holds for any `genTheory 𝓘 arch S`. The upstream placement is right: the shear/swap instance (`derivedOI_qm_iff_layerFlowExecutable_swap'`, DerivedQ3.lean:253), the class-N cell posits (QP:124–176), S13 and H-Bell's graph use the factorization; FI-1's statement, necessity and negative do not. |
| B4 | §5.2 row 5; NQ1 scope guard | Yes. The guard is gone; NQ1 keeps only the point it served (SM:312). The writer's hand proof of the criterion is correct for every odd prime (§3.3). |
| B5 | §5.2 rows 3 and 5; status terms | Yes. The wording matches `lift-source-audit.md`'s scope amendment (:250–264: "no formulation that lands derives either target"; nonreversible L1 and other L2 realizations not classified) and GR:270. "Excluded under stated conditions" is kept for the stated access only. |
| n1 | §0 item 8; §5.1(c) | Yes (Sub:131; Main:566/584 with Main:362; Sub:133 (iii)); no independence theorem claimed. |
| n2 | Carriers at every cited witness; `genTheory` named | Yes. The partial refusal is assessed in §3.1. |
| n3 | §5.2 arrow 4 | Yes (Main:590 states the typed form for the primitive-source equivalence only). |
| n4 | Exact check L; §10 | Yes. Reviewer check R3 repeats it on a six-cycle, a third graph. |
| n5 | §5.2 row 5 | Yes (`lift-source-audit.md`:97–101). |
| n6 | §6 Bell row; §5.3 | Yes (Sub:129, 131, 133). |
| n7 | §5.3 H-Bell row | Yes. MECH-2 DESIGN:543–567 calls M-FIX "a necessary condition derived from H-Bell, not an added requirement", and the head says the file "promotes no claim". |
| n8 | §5.2 | Yes. |
| n9 | §5.3 opening | Yes. The owner's words are quoted and attributed. |
| n10 | §12 items 1–2 | Yes. The answers are quoted from c.6740537555 and conditioned on an ACCEPT. |
| n11 | §5.3 H-Bell scope; §0 | Yes. |

***

## 2. The owner-visible refinement (B2) in plain words

The refinement says the owner's "independent unresolved obligations" holds only in scoped senses.

**Accurate.** Each of its four bullets checks against the sources:
- the phase and the layer flow are kernel-independent on `Fin 2`;
- the phase and FI-1, as predicates, imply neither each other, by a composition of kernel results;
- the phase and state mixing are not independent in every form;
- H-Bell is only not derived from, and does not derive, the other two in the sources read.

**Fair, with one omission.** It keeps the owner's word where the sources support it, and in
particular for FI-1 as stated. It narrows the word only for the mixing *obligation*, which is
stronger than FI-1. It flags itself as a refinement for the owner.

What it omits bears directly on c.6741291498's "the 'complex phases' candidate merges with native
mixing outside the layer flow". The drive that phase-free richness consumes is not phase-free in
content:
- *Isolation form.* $e^{-i\theta X_{ab}} = e^{-i\theta}\,G_{(ab)}(2\theta/\pi)\,\mathrm{diag}(1,1,e^{i\theta})$
  on three states, where $G$ is the layer flow of the transposition $(a\,b)$ [A; check R2(b)].
  The kernel's isolation identity (`gateFlow_isolation`, LiftAudit.lean:660) and GR:270 ("the layer
  flow reaches the driven elementary transitions … through the closure … the resource named here is
  the smaller one") state the same relation from the other side. So the driven transition is the
  layer flow plus a continuous relative phase on the configurations it fixes.
- *Quarter turn.* $e^{-i\frac{\pi}{2}X_{ab}}\cdot\mathrm{swap}(a\,b) = -i\,\mathrm{diag}(1,1,i)$. As a
  conjugation channel this is the quarter phase on the third state. With permutation transport it
  gives the quarter phase on every state of a three-state level [A; checks R2(c)]. Availability is
  closed under this composition (`avail_conj_mul`, LiftAudit.lean:770).
- *Monomial there.* At $\theta=\pi/2$ the drive is monomial, a signed permutation with entry $-i$,
  and it still moves the all-ones ray (R2(d)). The phase content sits exactly where FI-1 says
  nothing.
- *Countercontrol.* The real rotation $e^{\theta(E_{ab}-E_{ba})}$ is non-monomial, does not preserve
  diagonal states and moves the all-ones ray. With permutation transport it generates
  $\mathfrak{so}(3)$ (dimension 3), against $\mathfrak{su}(3)$ (dimension 8) for the $X$ drive. No
  word in real matrices conjugates as the quarter phase does (R2(e)). This is the corpus's "pair
  rotation at a quarter turn, which carries no phase at all" (`verification/programmes/substratum/frozen-sourcing-audit.md`:289) and
  GR:258's real-antisymmetric obstruction.

*In plain words.* Under phase-free richness the phase is not a separate input because it is
already inside the drive. The merge relocates the phase obligation into the mixing obligation,
where it becomes the requirement that the mixing source be the complex driven transition and not
a real rotation. It does not discharge the phase. The refinement is correct as far as it goes. As
worded, "the phase branch merges into the mixing branch" and "with no phase input" read as one
fewer thing to source. That reading is favourable to the framework, and §A.31 asks for maximum
skepticism on favourable branches. This is R4-B1.

*Classification (§A.31).* ELABORATING. `gateFlow_isolation`, GR:270, GR:258
(`not_hControl_evenCycle`) and `verification/programmes/substratum/frozen-sourcing-audit.md`:289 contain the parts; what is added is
the exact quarter-turn identity and its consequence for the merge.

*Aside, recorded only.* `phase-source-audit.md`:286–287 says "the quarter-turn transition flow moves
it and furnishes no quarter phase (the flow-endpoint witness)". Its own scope amendment (:227–229)
reads this as an admissible *branch* in `onesClass`'s closure. As a channel, the flow is unavailable
in `onesTheory` (`onesTheory_no_quarter_flow`). In a theory where it *is* available as a channel,
together with the exchanges, R2(c) shows it furnishes the quarter phase at a three-state level.
r4 does not cite that sentence. A dependency matrix that does should keep the branch reading.

***

## 3. The writer's refinements and refusals

### 3.1 n2: `genTheory` not identified with "the structural architecture". Correct.

GR:266 uses "structural architecture" for the substratum's closure with the phase intervention
stated: closed under the adjoint, with embedded observation, the exchanges, the quarter phases and
the read-write operators. `exists_nonMonomial_of_layerFlowExecutable` holds for every
`genTheory 𝓘 arch S`, which is a wider class. The r3 review's identification was too loose. r4
states the necessity "within the structural architecture", which is narrower than the theorem and
so is not an overclaim, and it names the class in which the theorem is proved. Optionally, r4
could say "for any theory generated by an architecture, in particular within the structural
architecture".

### 3.2 FI-1's negative does not use the phase. Correct.

The negative is `obs_availExt_le_substratum` with `substratumClass := IsMonomial`
(StructuralClosure.lean:180). The phase gate is monomial (`phase_monomial`), so the class stays
monomial with or without it, and the observer theory lacks it anyway (`obs_not_phasesAvailable`).
The phase enters only FI-1's position as "first", through `derivedOI_qm_iff_layerFlowExecutable'`,
which assumes `DerivedOI`. The r3 review's §6 wording was wrong on this point.

### 3.3 B4's hand proof. Correct for every odd prime, with one step left implicit.

The argument runs as follows.
- The centralizer of the non-scalar $f_a$ is $\mathbb F_p[f_a]\cong\mathbb F_p[x]/(x^2-ax+1)$.
- A scalar root of $-1$ has determinant $-1$, so it is excluded.
- In the three cases ($\mathbb F_{p^2}$, $\mathbb F_p\times\mathbb F_p$, $\mathbb F_p[\varepsilon]$),
  a non-scalar root exists iff $(-1/p)=-1$, iff $(-1/p)=1$, and never, respectively.
- With $\big(\frac{4-a^2}{p}\big)=\big(\frac{-1}{p}\big)\big(\frac{a^2-4}{p}\big)$, the three cases
  combine to "iff $4-a^2$ is a nonzero square".

The existence direction also needs the non-scalar roots to have determinant 1. That holds:
- in the field case the norm of $J$ is $J\bar J=-J^2=1$;
- in the split case $\det(i,-i)=1$.

The dispositions do not state this step. Check R1 confirms the whole criterion on all 158 pairs
with odd $p\le31$, the centralizer, the scalar exclusion and the determinant step. Its
countercontrol (drop $\det=1$; at $p=5$, $a=1$ the roots $2I,3I$ exist) shows the determinant
condition is load-bearing. The criterion is correctly kept out of the text (nit r4-n4,
dispositions only).

***

## 4. The §5.3 table, cell by cell

| Gap | Carrier | Scope | Proved / constraints | Open |
|---|---|---|---|---|
| Phase (O1) | Correct. `PhasesAvailable` is RouteB.lean:132: quarter phase on any state at every level. Encoded $S$ is flagged as a separate object. | Correct. It is an availability requirement, not an exactness predicate; `derivedOI_of_qm` gives it from exact QM. | Correct, with R4-B1 for the *Conditional* entry. `obs_not_phasesAvailable` fails at level 2 (docstring). The ones-fixing failure is at level one with no composite-level claim (PhaseSource.lean:51–55; GR:260). `phase_monomial` is available by stipulation. `polarizedTheoryC_phasesAvailable` (:448) is on `Fin 2`. The encoded entries match §10, QP and MECH-2. | **R4-B2.** "Or of a mixing resource that moves the all-ones ray" states a necessary condition as sufficient. |
| State mixing (FI-1; O2) | Correct. $S\times\mathrm{Fin}\,1$ on any finite configuration set (B3 verified). | Correct (`genTheory`; Main:566, 584, 600). | Correct. The "Two forms" entry has R4-B1 ("with no phase input"). `flow_endpoint_refuted_general` is cited correctly as "without it [the phase]", since `SourcedOI` is `DerivedOI` without `PhasesAvailable` by definition (SubstratumInterfaceAudit.lean:619–630). | Correct. These are the four candidates of §5.1. |
| H-Bell | Correct (Sub:131; Main:414). | Correct. (i)–(iii) match Sub:133, with (i) glossed through M1-B (Sub:129). "No exactness qualifier" was confirmed by grep in the r3 review and is consistent with the lines read. | Correct (Main:416, 362, 429, 566/584, 403–406; MECH-2 DESIGN:543–567 under "constraint", with its standing). | Correct. |

**H-Bell exactness paragraph.** The paragraph labels the bound "reviewer-supplied,
computation-supported, not adopted here as an established claim", as the r3 review asked, and the
finite-accuracy reading is attributed. Check R4 gives the witness in closed form:
CHSH $=6\cos\alpha-4\cos^3\alpha$ for every $\alpha$, which is $344/125$ at $\cos\alpha=4/5$. So
the witness is [A], like the rationality argument. The r3 review labelled the rationality argument
[A] and the witness computation-supported. r4 labels both computation-supported, which is weaker
than the evidence and so not an overclaim (nit r4-n3, optional).

**The three distinctions** are correct. The third carries B2. On "not from the layer flow alone
(K `onesTheory_not_qm`)", see nit r4-n1.

***

## 5. Blockers

### R4-B1. The phase-free-richness drive carries the phase; "no phase input" overstates GR:250

*Where.*
- §5.2 arrow 3, right column (l.612): "gives the same QM with no phase input".
- §5.3 state-mixing row (l.635): "gives QM with no phase input".
- The merge framing at §0 item 8 (l.140–143), §5.1(b) (l.526–533), §5.2 earliest-mechanism bullet
  (l.596–598), §5.2 summary (l.619), §5.3 scoped bullet (l.650–656), §10 (l.1036–1037), §11
  (l.1120–1121), and DISPOSITIONS *Owner-visible refinement*.

*Source.* GR:250 says "No phase operation enters", and Main:590 says "with no phase operation".
Both are statements about the listed repertoire. The drive is $e^{-itX_{ab}}$ with $X_{ab}$ the
real transition, and its content is complex. It equals the layer flow times a continuous relative
phase (`gateFlow_isolation`; GR:270, where the layer flow is "the smaller" resource), and at a
quarter turn, composed with the exchange, it is the quarter phase on a third state as a channel
(§2; R2(b)–(e)).

*Rule.* Claim/evidence boundary (available → derived). §A.31: maximum skepticism on the branch
favourable to the framework.

*Required.*
- Replace "with no phase input" by "with no phase operation in its repertoire (GR:250)".
- In §5.1(b) and the §5.3 scoped bullet, add one sentence: the driven transition is the
  transposition's layer flow times a continuous relative phase on the configurations it fixes
  (`gateFlow_isolation`; GR:270), and at a quarter turn with the exchange it is the quarter phase
  on a third state [A]. So under phase-free richness the phase is carried by the drive, not
  dispensed with. A real rotation moves the all-ones ray and mixes states but, with the exchanges,
  generates only real orthogonal operators.
- Carry the qualifier into the other merge sites, keeping them short.
- Add it to the DISPOSITIONS refinement, so that the owner's matrix records the merge as the phase
  obligation folded into the mixing obligation and not as one obligation fewer.

The exact identities are reviewer-supplied. If r5 adopts them, it should run its own check of them.

### R4-B2. The phase row's *Open* cell states the ray-moving condition as sufficient

*Where.* §5.3, phase row, *Open*: "A source … of the configuration-level phase or of a mixing
resource that moves the all-ones ray."

*Source.* GR:260 says the condition is "necessary … and is not shown sufficient". The owner's
scope amendment (`phase-source-audit.md`:212–221) reads: "Do not describe the ray-moving condition
alone as *the* missing access sufficient to source the conjunct". r4's own scoped bullet
(l.654–655) says "not shown sufficient". Countercontrol R2(e): a real rotation moves the ray and
supplies no phase.

*Rule.* Necessary → sufficient.

*Required.* Write "… or of a mixing resource of the phase-free-richness form (the complex driven
transition); moving the all-ones ray is necessary, not sufficient (GR:260)".

***

## 6. Nits

- **r4-n1 (scope of the flow-endpoint negatives).**
  - §5.1(b) (l.526–527): "The layer flow fixes the all-ones ray and does not give phase-free
    richness". Add "with the sourced closure and without the phase". With the phase it does
    (`phaseFree_of_derivedOI_layerFlowExecutable`, DerivedQ3.lean:207).
  - §5.3, third distinction (l.687): "not from the layer flow alone (K `onesTheory_not_qm`)". Add
    "with the sourced closure, on the two-state carrier".
- **r4-n2 (§6 propagation, §A.25).**
  - The *Complex phases* row's last column names only the encoded $S$. After §5.3 it should also
    name the configuration-level source (O1), as §5.3's *Open* cell does.
  - The *Interference* row's "together with a native phase" holds for the layer-flow form. Under
    phase-free richness the drive carries the phase (R4-B1).
- **r4-n3 (H-Bell paragraph, optional).** The rationality argument and the witness are [A] (R4's
  closed form), not only computation-supported.
- **r4-n4 (dispositions only).** B4's hand proof leaves implicit that the non-scalar roots of $-1$
  have determinant 1 (§3.3). The text is unaffected.
- **r4-n5 (dispositions).** The refinement could open by saying that the owner's "independent"
  holds as stated for the phase and FI-1 as predicates, so that it is not read as narrowing that
  part.
- **r4-n6 (§5.1(b), §5.3, optional).** The restriction $t\notin\tfrac{\pi}{2}\mathbb Z$ is needed
  for non-monomiality only. The drive moves the ray for every $t\notin2\pi\mathbb Z$, including at
  the monomial quarter turn where the phase sits (R2(a), R2(d)). Saying so supports R4-B1.

***

## 7. Full re-read: other checks

- **New errors elsewhere.** None beyond the above. §§1–4, §6 (apart from r4-n2), §7–§9, §10 (apart
  from the L citation, verified), §12 and §13 are unchanged from r3 or change only as the
  dispositions record. The 30 r3→r4 hunks each map to a disposition row.
- **F4 condition (for §12 item 1).** This review also confirms it: Theorem 5 (SM:340) asserts a
  stabilizer "in $\mathrm U(6)$" under H-link, H-cust and $O$-equivariant $\Sigma$, with no complex
  structure among the stated premises, and SM:809 names "the real-to-complex step" as an open
  joint.
- **Three-column separation.** It holds. §5.3 adds no column (iii) content as support. §4 and §9
  are unchanged.
- **§A.31 labels.** Correct. The FI-1 label (CONFIRMING) now mentions GR:250–258. Nothing is
  labelled NEW. R4-B1's content is ELABORATING (§2).
- **Authorization.** Nothing implies any:
  - the header quotes c.6738806776 and c.6739843458;
  - §12 records the c.6740537555 answers as taking effect only on an ACCEPT;
  - unit 2 is not selected;
  - the checks are generic and labelled.
  c.6741291498 grants nothing new, and r4 claims nothing from it.
- **Passages for r5.** §5.1(b); §5.2 arrow 3 and the earliest-mechanism bullet; §5.3 (phase row
  *Open* and *Conditional*, state-mixing row *Two forms*, scoped bullets, third distinction); §6
  *Complex phases* and *Interference* rows; §0 item 8, §10 FI-1 label and §11 last bullet, for the
  qualifier; the DISPOSITIONS refinement.

***

## 8. Exact checks

**The writer's probe.** `python3 -I probes/r4_generic_checks.py` was re-run. Its output is
byte-identical to `probes/r4_generic_checks.out` (`696f5108…30bf`; copy at
`review/probes/r4_generic_checks.rerun.out`). All 22 checks pass.
- The controls are non-vacuous: J has a null-mode countercontrol, D a two-state control and a
  gate-flow control, L a linear opposite-colour control.
- D(a) tests one time ($\pi/4$). It is a witness, and the text labels it [A].

**Reviewer probe** `review/probes/r4rev_checks.py`.
- Hashes: script `310432163fd357247f5b39aac75e1ff0b89b50c19571e1ea2c4c4561720a7ee4`; output
  `r4rev_checks.out` `077d62774a6324337eade2b3cafadd530605dad79c1914b83dbf4cfe050f99a4`. All 24
  checks pass.
- Method: exact arithmetic only (integers mod $p$; sympy with a symbolic angle; $\mathbb F_2$ on
  $C_6$; rational two-qubit algebra). It imports no earlier script and runs no OI mechanism, under
  c.6739843458.
- Results:
  - **R1:** B4's criterion and proof steps, odd $p\le31$, with a determinant countercontrol (§3.3).
  - **R2:** the drive's ray image for all $\theta$ on 3 and 4 states; the isolation form; the
    quarter-turn identity and the quarter phase on every state of a three-state level; monomiality
    at $\pi/2$; the real-rotation countercontrol with Lie dimensions 3 against 8 (R4-B1, R4-B2).
  - **R3:** read pattern versus linearity on $C_6$ (n4).
  - **R4:** CHSH $=6c-4c^3$ for all $\alpha$; $344/125$; below the irrational $2\sqrt2$.

These are witnesses and controls for algebra stated here. No verdict rests on them alone. R2's
identities are also hand-checked in §2.

***

## 9. What r5 needs for ACCEPT

1. R4-B1: replace "no phase input"; add the drive-carries-the-phase sentence (isolation form,
   quarter-turn identity, real-rotation countercontrol) at §5.1(b) and §5.3, the short qualifier at
   the other merge sites, and the same in the DISPOSITIONS refinement.
2. R4-B2: correct the phase row's *Open* cell.
3. r4-n1, r4-n2 and r4-n5; r4-n3, r4-n4 and r4-n6 are optional.

A delta review of the passages listed in §7 is enough if nothing else changes.
