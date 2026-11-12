# Independent review of OA-1 (`OA-1-REPORT.md`)

**Reviewer standing.** Independent reviewer, same model family, read-only and paper-only. No computation on any OI
rule, no commits, pushes or GitHub writes. Authorization: owner amaybaum, #1169 c.6829742537 and c.6829898892.
Sources: `main` = `fb733b4a58558ef64bd7c3585712c76e9f2dfb42` (read by `git show`), TUNE-1 at
`d47a6377f2d8753f88ddc4d3ab0c03ead64393dd`, trace #1169 c.6829596317 (fetched by API). Citation forms follow the
report (`Main:n`, `OB/File:n`, record paths relative to `verification/programmes/oi-qm/reconstruction/`).

## Verdict: ACCEPT WITH CHANGES

The central derivation D2 is correct and does not confuse a marginal with a conditional. The control result D5 and
the R4 kernel readings are correct. The report is broadly well labelled. Changes are still required before the
report is used. The claimed earliest failure (R3/N1) holds only under one of the three measures Main states. Two of
MP-0's branches have different types. D4, the one NEW candidate, rests on a premise that forces a trivial case, so
it is not NEW. Several statements need their kernel/paper scope or their search scope stated.

***

## 0. Coordinator check: the scratchpad-root `Main.md` and `GR.md`

- The report cites neither root file. `grep` finds no reference to the scratchpad root, and `GR.md` appears only in
  the "Not read" list (`OA-1-REPORT.md:583`). Every `Main:n` citation is to `papers/Main.md` at `fb733b4a`
  (`OA-1-REPORT.md:11`, :540).
- OA-1 made its own copy at `oa1/src/main/Main.md` (mtime 16:42:04, after the root overwrite at 16:41:57). It is
  byte-identical to `git show fb733b4a:papers/Main.md` (`cmp`). The root `Main.md` and `GR.md` are now also identical
  to `fb733b4a`.
- I checked every cited Main line against `fb733b4a`: :42, :48, :54, :58, :60, :68–80, :74, :97, :480–486, :522,
  :546–552, :558, :564–582, :588, :590, :596, :602–612, :644, :724 (items ii, vii, xiii, xiv), :742. Each has the
  content the report attributes to it. The quotations at :580 and :582 are verbatim.
- OA-1's copies of MECH-1, MECH-2, minacc RESULT, apparatus-1 and TUNE-1 Step 1, the proposal and Session 3 match
  their pinned blobs. Every Lean line I checked holds the declaration cited: `Equivalence` :157, :245, :294, :422,
  :462; `SubstratumInterfaceAudit` :406, :708, :770, :775, :780, :790, :816; `FrozenSourcing` :65, :74, :84, :99, :277,
  :295, :302, :318, :327; `StructuralClosure` :333, :336, :348, :414; `InternalObserver` :92, :272, :290;
  `CentralObservation` :620; `QuasilocalCharacterization` :792; `LiftSource` :164; `ExecSource` :129;
  `SubstratumInterface` :155; `SubstratumSource` :77, :86.
- **Answer.** No reliance on the root files was found, and the citations hold at `fb733b4a`. The tool history of the
  OA-1 session is not available to me, so I cannot rule out that it opened a root file. That would not matter,
  because every citation checks out at the pin.

***

## 1. Check 1 — R3/N1 preparation failure, D2 (pressure-tested)

**The derivation is correct.** Main fixes the canonical measure on the bijective carrier `C_V × C_H` as uniform,
"with the uniform conditional law on `C_H` in each visible fibre" (Main:58). It is φ-invariant (Main:54), so the law
at every time `t` is uniform on the product. Hence `H_t` is uniform and independent of every function of `V_t`.

The worry that a record, being a function of the configuration, could still be correlated with `H_t` does not apply
to records the observer holds at `t`. Those are functions of `V_t`, and the product form settles them.

Correlations do arise when one conditions on an event that is **not** a function of `V_t`. My check: cells `a, r`
visible, `b` hidden, `φ(a, r, b) = (b, r⊕a, a)` (a bijection). Conditioned on the past herald `r_t = 0`, we get
`r_{t+1} = b_{t+1} = a_t`, a perfect correlation between `V_{t+1}` and `H_{t+1}`. But `r_t = r_{t+1} ⊕ b_{t+1}` is not
a function of `V_{t+1}`, so the observer no longer holds the herald. This is exactly the report's H-MEM split
(N1.2). The strict reading "`E` held when `Σ` is used" (N1 row, `OA-1-REPORT.md:89`) carries the weight, and it holds
up. **No marginal/conditional confusion.**

**Required changes.**

- **C1-a (measure scope; substantive).** D2 holds for the *global* counting measure. Main states two other measure
  selections, and on either one D2 is not established:
  - the uniform measure on the orbit of the actual microstate, unique and derived (Main:54, Main:60);
  - the posited selection "maximal entropy compatible with the observer's records" (Main:60; ledger item (iv),
    Main:724).

  The law selected that way is uniform on a union of compatible orbits. That law is invariant but in general not a
  product, so `V_t` and `H_t` can be correlated. The report mentions the per-cycle case only in §7 and §10, and §10
  wrongly says "That failure is exactly what H-LOW supplies" (`OA-1-REPORT.md:601–602`). Neither a per-orbit law nor
  a record-compatible law is a lower-entropy prior with ready cells. Fixes:
  - Qualify "for every φ" in N1.1 (:230), §0 item 3 (:40–43), MP-0's "why not supplied" (:421–422) and §5's
    earliest rung (:456–457) as "under the global counting measure (Lemma 3; Main:58)".
  - Add the per-orbit and record-compatible selections as a distinct branch, status open. The record-compatible
    selection is orbit-level conditioning on records, so state whether it is read as native (ledger (iv)) or as H-MEM.
- **C1-b (carrier scope).** N1's definition allows a "possibly hidden" carrier (:89). A visible carrier is prepared
  natively, by heralding on `V`, at the D3 cost. Write the verdict as "no **hidden** carrier is prepared natively". The
  bullet at :228 says this; the verdict line at :230 does not.
- **C1-c (novelty).** Q-b1 (`observer-interface-obsmu-20261104/ANALYSIS.md:907–912`, in §4.6.2) is stated for the
  counting measure on `C_V × C_H` at a time slice, with no automorphism hypothesis. Only Lemma P-1 (:529–545) assumes
  an automorphism. D2 is Main:58 plus invariance; it does not extend Q-b1 "to every bijection". Correct :107–109,
  :229 and the status row at :473.
  - What D2 does add: obsmu treats in-`V` retention as the open route to preparation (:913–917, O-RET/O-REC/O-ACC).
    Under the global counting measure, D2 applied at `t_0` closes that route, because a retained record is a
    function of `V_{t_0}`. Say this explicitly (ELABORATING of obsmu). It is the point the report makes only in N4
    (:293–294).

***

## 2. Check 2 — MP-0 (H-LOW / H-MEM)

- **H-LOW** is correctly typed as a resource with no quantum content, but only if its form is fixed:
  - fixed known values on designated cells, independent of the setting and of the carrier, and uniform elsewhere.

  A general "structured prior" is the channel through which R2 supplies its target: `u_c ~ P(·|c)` (Main:482), the
  initialized ledgers (Main:522), and the program and quantum state in the hidden register (Main:580). **Required
  (C2-a):** state the admissible form, which is what makes N1.2 pass the report's own non-import test (:80–83).
- **H-MEM is not a resource.** It redefines what the observer holds: records outside `V`. That conflicts with N4's
  "physically held in `V`" (:92), and over growing horizons with an observer that has finitely many states (Main:42).
  It is an interface premise, the same type as MP-2.
  - The kernel interface of R4 already assumes it: `FiniteOperationalTheory` keeps instrument outcome labels outside
    the carrier (`OB/OperationalAssembly.lean:594–643`).
  - **Required (C2-b):** split MP-0 into MP-0a (H-LOW, resource) and MP-0b (H-MEM, interface convention). Note that R4
    grants MP-0b. The report's own wording "not a physical record" (:234) already points this way.
- **Main:58 for H-LOW.** The citation fits the claim that a declared structured prior is admissible as a realization
  datum, which keeps it a premise. Two limits:
  - Main:58 speaks of a *hidden* prior `μ_H`. Ready visible or apparatus cells need the joint initial law on
    `C_V × C_H` (Main:97, Main:602).
  - Main:58 places such priors inside §3.4 realizations, that is, as supplied data.

  **Required (C2-c):** cite Main:97/:602 alongside Main:58 and keep the "datum, not supply" reading. N1.4's reading of
  Main §4.6 (Main:742, "in its role of selecting observer-compatible configurations") is correct.

***

## 3. Check 3 — control failure, D5, MP-1, G_SM

- **D5 is correct and matches its sources.** MECH-1 Lemma A (`mechanism-1-20261107/DESIGN.md:404–430`) is stated for
  any affine bijection with a setting law independent of the rest. TUNE-1 Lemma A-T (`T1/TUNE-1-STEP2-SESSION3.md:41–98`)
  re-derives it for `Φ_F(y, x) = (x, Ax − y)` over `ℤ/q`, in both modes and with record laws. The "shift values only"
  claim is right: the non-translational part and the functional read do not depend on `c`. D7 is sound.
- **Precisions required (C3).**
  - (a) **Affine, not only linear.** Lemma A covers affine rules. Ledger (vii) states that amplitude-scale gauge
    invariance yields the affine form (Main:724). So the N2 failure holds for the gauge-derived affine class, not only
    under the linearity posit. MP-1 (M-CTRL) is "necessarily non-affine" (:432), so it gives up a derived
    restriction: a Layer-0 revision under §A.29. Say so in MP-1's "Hard to vary?".
  - (b) **Measure-independent.** Lemma A(i)–(ii) need only setting independence, not the uniform law. So N2's failure
    holds under every measure, unlike N1's (C1-a). This bears on the ordering (§9 below).
  - (c) "Proved on paper three times" (:258, :475) is one paper proof re-derived twice, at the same layer (§A.22: no
    added weight). The "reviewed" tag on Lemma A-T (:144, :259) refers to the ChatGPT review recorded in
    `T1/TUNE-1-STEP2-SESSION4.md:13–16`, not to an independent review on `main`. Reword both.
- **G_SM characterization.** The summary at :270–271 and :435–436 needs three precisions
  (`mechanism-2-20261108/DESIGN.md`):
  - G_SM is non-reciprocal "for `L ≥ 5`" (:44–45).
  - A5 fails (:44) ✓; it is an SM stated-hypothesis example, not physically sourced (:45–48) ✓.
  - "Not CP" is relative to the R1 frame. Joint-CP failure under R1 "holds for every coupling rule and does not
    single out `G_SM`", including the linear class N (:59–61, :95–96). P★'s instrument fails C-CP (:82–90) ✓.

  Required: add "for `L ≥ 5`" and the R1/not-specific qualifier. Minor: the timing-selection citation in D7
  (`apparatus-1-20261107/DESIGN.md:379–390`) should point to :510 ("the setting is the parity of the armed tick,
  which is available only through P3").

***

## 4. Check 4 — R4 ceiling and point 3

- **Kernel statements verified.**
  - `obsTheory 𝒮 := permTheory 𝒮.Conf` (`OB/SubstratumInterfaceAudit.lean:770`), `rfl` at :775 and :780.
  - `permClass_permMatrix` (:406).
  - `obsTheory_nonnegBounded` (`OB/FrozenSourcing.lean:84`), `nonnegBounded_not_phasesAvailable` (:99, any carrier),
    `nonnegBounded_not_derivedOI` (:111, any carrier).
  - `frozen_sourcing_verdict` and `nonnegBounded_verdict` (:318, :327), both on `Fin 2`.
- **Point 3 is confirmed.** Required precisions (C4):
  - (a) **Sub-theory.** A theory generated from φ's configuration bijections by the closure rules is, in
    availability, a sub-theory of `permTheory 𝒮.Conf`. That theory contains every permutation conjugation and is
    closed under the same rules. `NonnegBounded` (:65) is monotone under availability inclusion, so the result
    follows from :84 directly.
    - Remove or explain "It need not be a literal sub-theory" (:325).
    - `nonnegBounded_of_bijectionLevel` (:74) applies only to a `genTheory` of a `BijectionLevel` class carrying an
      `Architecture` (`OB/ImplementationLocality.lean:506–516`: unit, products, scalings, projections, blocks). No
      kernel theorem states "the generated sub-theory is `NonnegBounded`", so D6 is [W] on [K], as the status table
      says. Keep D6's text consistent with that label.
  - (b) **Fin 2 scope.** `DenseUnitaryControl` is defined only for theories on `Fin 2`
    (`OB/DiscreteCompletion.lean:45`). For `obsTheory` on `Conf`, the kernel states only no phases and not
    `DerivedOI`. Add the `Fin 2` qualifier, or the label [W on K], at §0 item 5 (:47), the `obsTheory` row "T-C fails
    [K]" (:407) and the qubit-tier control row (:370).
  - (c) **R4 is not "R3 + one structure".** R4 grants write access (H-write; `T1/TUNE-1-STEP2-PROPOSAL.md:155–167`)
    and external outcome labels (MP-0b). It also restricts the identification to the configuration basis. R3's
    encoded-frame qubit tier (5c) lies outside R4's kernel cap. Present R3 and R4 as two branches, not a chain (see
    §9 below).
- The trace audit in §8 is accurate. The only change is to soften "Refuted as a route" (:532) to "settled by D6 for
  configuration-level, bijection-generated source maps". The trace's own §C allows a source map that is "changed or
  replaced", and the coordinator note had already reached this.

***

## 5. Check 5 — MP-2 and the proposed replacement

- **Credit.** The replacement is MECH-2's named missing premise M-INACC (`mechanism-2-20261108/DESIGN.md:108–117`,
  "needs a change in the identification and access, not in the dynamics alone"). It is also
  `mathcon1-polc-20261108/DESIGN.md:585`, "Shape 1, non-injective protected-functional access rule … M-INACC". OA-1
  did not read mathcon1 (:585 of the report). **Required (C5-a):** credit both. MP-2 is then CONFIRMING, not a new
  proposal.
- **"Smallest".** No argument shows it is smallest. What is shown is that it is the option the cited no-go results
  leave open within their hypotheses: U2 (R1), Lemma F, Theorem NC, Main:558, and TUNE-1 FAIL-CLASS on bounded
  `|C_n|` (`T1/TUNE-1-STEP2-SESSION4.md:567–575`). Other routes stay open:
  - NC needs spanning-read certification, which at `q = 2` needs a `Y` read that is not native; over native `Z`/`X`
    reads, NC does not apply (`mechanism-2-20261108/DESIGN.md:69–71`);
  - mathcon1 Shapes 2–3.

  **Required (C5-b):** say "the escape left open by …", not "smallest".
- **"Non-importing".** This holds only by definition: M-INACC's clause requires "a reason not chosen to reach the
  target". Whether any φ realizes it is open. The report says "target-neutral if achieved" (:345), which is right.
  The MP-2 text should use the same conditional form.
- **§A.19 search.** I grepped `M-INACC` across `main` and searched for record-level and operational-equivalence
  constructions. Hits beyond those cited:
  - mathcon1 (a candidate shape, not a construction);
  - `round-arp1-marc-20261108/result.md`. Token `ARP1-MARC-SURVIVAL`: in a finite ring model (`L ∈ {7, 9}`, `q = 2`,
    `T = 4`), protection of `Q* = 1` functionals survives removal of the coupling isolation. It stays conditional on
    supplied registration, P2 and H-PREP, and the round does not adopt Lemma Q as an instance of M-INACC (:36–38).
    This refines the report's "Lemma Q's protection holds only under P1 and P2" (:450). Isolation is measured not to
    carry the protection there, while P2 and access do. Cite it.
  - `q3-a6-offsets` (authorization context only);
  - `oi-pseudoentropy-20261025/README.md:150` ("up to record-equivalence", not a construction).

  None constructs 5d. **The claim "No construction of it exists on main" survives**, but its scope must be stated
  (C5-c). As written, §0 item 6, :353 and :449 are unscoped, while §9 limits negatives to sources read.
- **"Sufficiency open" (:453, :481)** is stated correctly as [O].

***

## 6. Check 6 — R5 candidate verdicts

- **5c (encoded carrier).** The ceilings are cited correctly, but the qubit column "Stabilizer and Clifford only"
  (:344) is too broad. Required (C6-a): replace it with "CP-reachable: stabilizer/Clifford only, frame-relative", and
  name where each part comes from:
  - U2 under R1, whose covariance is `A_4 ≀ S_n` (`mechanism-2-20261108/DESIGN.md:52–61`);
  - Proposition C at odd `q`;
  - the 24 Clifford actions under the eight-sign map (`operational-quotient-v3/REPORT.md:11–23`);
  - MECH-2's P★, a non-stabilizer state that appears only in a non-CP instrument (:76–86).

  Also: NC does not apply over native `Z`/`X` reads alone. "Noncontextual" is conditional on spanning reads. The
  op-quotient v3 is itself an operational quotient with a supplied private-access contract. List it under 5d's
  "supplies the restriction" as well.
- **5e (emergent amplitude space).** The Koopman–von Neumann remark shows that passing T-C does not discriminate: a
  classical linear oscillator lattice evolves complex normal-mode amplitudes unitarily. It does not show that the
  amplitude space is imported. Import rests on two other facts: E-real, E-pair and E-control are supplied
  (`oi-qm-ext-1/two-mode-drive.md:25–40`), and the kernel facts (`OB/LiftSource.lean:164`; `OB/ExecSource.lean:129`;
  Main:644, :588). **Required (C6-b):** reword the classical-control cell ("would pass, so this is an import").
  Keep the KvN item [W]. Note that it concerns a real continuous lattice, not R-lin over `ℤ/q`.
- **5f (infinite lattice).** Correct. `phaseQ_ne_heisQ` (`OB/QuasilocalCharacterization.lean:792`) [K] supports "not
  sufficient" for the phase automorphism. "Necessary" rests on Main:558, correctly tagged [P, half imported] in §6.

***

## 7. Check 7 — D4, the NEW candidate

- **The implication is true but its premise is degenerate.** Under the counting measure, `V_t` and `V_{t−1}` are both
  uniform on `C_V`.
  - If `V_t` determines `V_{t−1} = g(V_t)`, then `g` pushes the uniform law to itself, so `g` is a bijection. (A map
    of a finite set that is not injective leaves some point without a preimage, and that point would get mass 0.)
  - Then `T(v, v′) = 1` exactly when `v = g(v′)`, so `T` is a permutation matrix. `T` does not depend on `t`, so one
    complete step anywhere forces this.
  - By Main:147, `T` is a permutation matrix iff `φ(x, h) = (φ_V(x), σ_x(h))`: the visible dynamics does not depend
    on `h` at all.

  So complete in-`V` records force the hidden sector to have **no** influence on `V`. (C1) fails at every step
  (Main:72), not only (C4).
  - D4(b)'s description, "a homogeneous Markov chain of the uniform-prior one-step kernel `T`" with the hidden sector
    as "fresh memoryless noise at every step" (:127–129), is literally true but misleading: the chain is a
    deterministic permutation and the noise is trivial.
  - The same argument works for any stationary law (the pushforward of `ν` to `ν` forces a bijection on the support).
- **Classification.** The tension is not "records versus readback". It is between keeping complete records in an
  equilibrium state and **any** hidden influence: the blank-memory (Landauer) cost of D3, i.e. MP-0a again.
  **Required (C7):**
  - reclassify D4 from NEW to ELABORATING, a corollary of D2, stationarity and Main:147;
  - correct D4(b) and its echoes at §0 item 7 (:51–53), R1 (:196–199), N4 (:295), §7 (:487–497) and the status table
    (:474);
  - state the scope: the global counting measure, or any stationary law, for full-history records. D4 does not cover
    partial records (records of functionals of the past) and dissolves under H-LOW.
- **AW-OA1-1** (:496–497) is valid. It restates Main:97 ("in a bijective realization run from time 0 the visible past
  is a function of `(X_t, H_t)`") and obsmu (:915–917), so classify it CONFIRMING. The fixed-point tally (:516–517)
  becomes: no NEW findings in this pass.

***

## 8. Check 8 — negative-result scope and layers

- Verification layers are mostly kept apart ([K]/[P]/[R]/[W]/[O]), and R2's verdict is quoted from Main's own text
  (Main:580, :582). Remaining scope defects, all listed above:
  - "for every φ" without the measure qualifier (C1-a);
  - "no dense control" for `obsTheory` without `Fin 2` (C4-b);
  - an unscoped "nothing on main" (C5-c);
  - "three times" (C3-c);
  - "Refuted as a route" (§4 above);
  - D4's mis-description (C7).
- No statement turns failure of R-lin or of the configuration interface into impossibility for every
  observer-level extension. The report's §10 and its final trace row explicitly keep R-nl, other identifications and
  OI generally open. ✓
- §A.32/§A.33 do not apply: this is a research record, not paper prose.

***

## 9. What OA-1 establishes, and at which layer

At kernel level, OA-1 adds nothing new. It reads correctly that R0 (`finite_horizon_equivalence`) cannot fail and
that the current configuration interface `obsTheory = permTheory Conf` is rule-blind by `rfl`, has no phases and is
not `DerivedOI` on any carrier, and has no dense control on `Fin 2`. Its own paper results [W] are:

- **D2/D3.** Under the global counting measure no physically held record is correlated with the present hidden
  state, and point preparations and blank cells cost `q^{−M}`. These are correct and essentially Main:58 plus
  invariance; they close obsmu's in-`V` retention route under that measure.
- **D5/D7.** Under any affine rule, hence under R-lin and the gauge-derived affine class, a setting held in the world
  acts only as a translation. This is correct and measure-independent; it re-derives MECH-1 Lemma A.
- **D6.** Rule-derived, bijection-generated configuration-level interfaces stay inside the `NonnegBounded` ceiling.
  Correct, [W] on [K].
- **D4.** Correct but degenerate (§7 above).

OA-1's replacement candidate (5d with M-INACC) is MECH-2's and mathcon1's. Its non-import status and its sufficiency
are open.

**The "earliest failure" ordering survives only in qualified form.** R0–R2 never fail; they meet the target only
with supplied data. At R3, for the posited rule:

1. The N1 strict failure comes first in operation order, but it holds only under the global counting measure. It is
   target-neutral, and a classical computer shares it. Main's per-orbit and record-compatible measures (Main:54, :60,
   ledger (iv)) leave it open.
2. The **earliest measure-robust failure is N2**: no native setting selection under any affine rule. It is
   paper-level and classical.
3. The **first kernel-proved failure** is the configuration-identification ceiling. It is reached on a parallel
   branch (R4) that grants more control (write access, external records) and less identification freedom; it is not
   a later rung of R3. R3's encoded-frame qubit tier is capped only by paper results (U2, NC, Proposition C), and those
   caps are frame-relative.

With these changes, the report's answer to the owner's question stands: the structure to replace is the
identification of observer operations with configuration-basis matrices. The escape the existing no-go results leave
open is a derived inaccessibility (M-INACC) on growing carriers. It is not constructed anywhere on `main`, and whether
it suffices is open.
