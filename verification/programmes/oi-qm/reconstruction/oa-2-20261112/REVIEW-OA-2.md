# Independent review of OA-2 (`OA-2-REPORT.md`)

**Reviewer standing.** Independent reviewer, read-only and paper-only. No computation, no script,
no commit, push or GitHub write. Sources read with `git show` at `main` `fb733b4a` (the report's pin)
and at OA-1 `066be3b1`. `origin/main` is now `ec257bee`; `git diff fb733b4a ec257bee` touches no
file under `papers/Main.md`, `verification/programmes/oi-qm/` or `verification/lean-mathlib/`, so the
pin is current for everything cited. The authorization was re-fetched read-only: #1169
c.6831588323 (account amaybaum, 2026-11-12T17:55Z) records the owner's question verbatim and
"Authorize paper-only unit … no computation, no Lean or manuscript changes, and no premise
adoption". OA-2 stays inside that scope. During the review I wrote a temporary byte copy of
`Main.md` inside `scratchpad/oa2/` to grep it; it has been deleted.

Citation form: `R:n` = line `n` of `OA-2-REPORT.md`; `OA1:n` = `OA-1-REPORT-r4.md` at `066be3b1`;
`MECH-2:n` = `mechanism-2-20261108/DESIGN.md`; `MECH-1:n` = `mechanism-1-20261107/DESIGN.md`;
`AP1:n` = `apparatus-1-20261107/DESIGN.md`; `obsmu:n` = `observer-interface-obsmu-20261104/ANALYSIS.md`.
Reviewer derivations are labelled [RW] (by hand, unreviewed).

## Verdict: **REVISE**

Much of the report checks out. Lemma 0, Proposition A, Lemma 1, Theorem C (after a one-line repair),
Theorem E(a) and (c), Corollary E2 and the logic of Claim 2 are correct. Three findings change
stated verdicts, though.

- **F1.** Proposition B's measurement-noncontextuality clause is false as stated, and so is
  Corollary B′ ("G3 requires non-injectivity … for every rule").
- **F2.** Theorem E(b), which is the report's only NEW item and the basis of its headline "NO for
  OI's own rule class", covers one joint record at one readout time. Proc's own closure supplies
  reads at every duration, and in the default convention those reads are not nested.
- **F3.** The verdict "fails G3" is carried beyond the spanning condition under which (b) proves it.

F4 also matters: the 𝔊_K equivalence (Claim 1) does not hold under the report's own definition of
effects unless a prepare-measure convention is stated.

The open verdict on `G_SM` stands. The next steps need the corrections below.

***

## Findings

### F1 (major): Proposition B's second clause and Corollary B′ are false as stated

**Claim (R:184–198).** If `R` is injective on `W = span(reachable)` and the effects restricted to
`W` span `W*`, then the model is measurement-noncontextual and `E` is simplex-embedded by `R⁻¹`.
Hence (B′) G3 requires two reachable laws with the same emergent state, "now necessary in E3 for
every rule". The proof is "Theorem NC's proof with the frame replaced by `R`" (R:192).

**Why the proof does not transfer.** Theorem NC obtains measurement noncontextuality from the
*states* spanning: "ξ is determined by E, because frame coordinates of states span" (MECH-2:506), and
its equivalences are certified "once the reachable preparations span the operator space"
(MECH-2:489). Proposition B drops that hypothesis. Its replacement, effects spanning `W*`, is
tomographic completeness for the states. It does not make two effects that agree on `W` agree as
ontic response functions.

**Counterexample [RW].**
- *Ontic space.* Take `(x, y) ∈ F₂²`.
- *Reachable laws.* All laws with `P(x = y) = ½`. Then `W = {w : w₀₀ + w₁₁ = w₀₁ + w₁₀}` has
  dimension 3, and `Δ ∩ W` is the square with vertices `σ_{x0} = ½[00]+½[01]`, `σ_{x1}`, `σ_{y0}`
  and `σ_{y1}`.
- *Effects.* All classical reads of `(x, y)`. `R` is injective on `W`, and the effects span `W*`.
- *Equivalences on `W`.* `w₀₀ = ½X0 + ½Y0 − ¼` and `w₀₁ = ½X0 − ½Y0 + ¼`. These were checked on
  all four vertices.
- *Contradiction.* With measurement noncontextuality and convex-linearity:
  1. On `supp μ_{x0}` we have `ξ_{X0} = 1`. Positivity of `ξ_{E10}` and `ξ_{E11}` then forces
     `ξ_{Y0} = ½`.
  2. On `supp μ_{x1}`, positivity of `ξ_{E00}` and `ξ_{E01}` forces `ξ_{Y0} = ½`.
  3. Preparation noncontextuality gives `μ_{y0} + μ_{y1} = μ_{x0} + μ_{x1}`. So `ξ_{Y0} = ½`
     holds `μ_{y0}`-a.e., which contradicts `Y0(σ_{y0}) = 1`.
- *Conclusion.* The fragment is measurement-contextual, so G3 holds, with `R` injective. This is
  the dual of the gbit: preparations are restricted while reads are complete.

**Whether Proc's closure excludes this is not shown.** Heralding on a non-disturbing joint read would
leave `W`. A designed read that re-randomizes the parity after recording `(x, y)` keeps the
reachable laws inside `W`, in the same way that 𝔊_K's MEAS re-randomizes `y`. So the report's
general claim ("for every rule", R:196) has no proof.

**Correct statements [RW].**
- *(B, corrected).* Suppose `R` is injective on `W`. Then the substratum model is
  preparation-noncontextual.
- It is also measurement-noncontextual **iff** the restriction map from the span of the available
  effects, taken as functions on the union of supports `U`, to `W*` is injective. A sufficient
  condition is `W = ℝ^U`, which is NC's actual hypothesis.
- Transformation noncontextuality of the substratum model likewise needs `π` to be fixed on
  `ℝ^U`, not only on `W`. As written, "π|_W is fixed by π_E" (R:187) does not give it.
- *(B′, corrected).* G3 requires that the substratum model's preparation equivalences **or** its
  effect equivalences be coarser than ontic equality. MECH-2 already states this
  frame-independently in M-INACC's "Why it is needed": "a contextual observer-level theory needs
  operational equivalences coarser than ontic equalities" (MECH-2:842).

**Knock-on effects.**
- §0 item 3 ("escape is possible exactly through non-injectivity", R:40–41) and N-b (R:427) are
  wrong as stated.
- Next step 1 (R:508–515) tests only the gbit shape and must add the dual shape: reads that are
  complete but preparation span that is restricted.
- The class-N single-cell result (R:408–416) rests on the false clause. **Its conclusion
  survives on a corrected reason [RW].** Let `f(z) + g(x)` vanish on every `z`-pair and `x`-pair
  law. Then `f(a) + mean(g) = 0` for all `a`, and `mean(f) + g(b) = 0` for all `b`. So
  `f(z) + g(x) ≡ 0` as an ontic function, for every `q`. The restriction is therefore injective,
  and the configuration model is noncontextual.

**Required.**
1. Restate Proposition B as corrected above.
2. Replace Corollary B′ with the two-route necessary condition, credited to MECH-2:842 and
   MECH-2:523–529.
3. Re-derive the class-N result through the injectivity check.
4. Correct §0 item 3, N-b, next step 1, the status table (R:536) and §6 (R:561–562).

### F2 (major): Theorem E(b) covers one joint record; Proc supplies reads at every duration

**What (b) proves.** For one readout `Z` with a fixed schedule, every effect is `λ ↦ f(λ + H_c c)`
on `Λ = values of Z₀` (R:341–349). That is correct for one `Z` [RW].

**What the framework supplies.**
- Proc is "closed under sequential composition" (R:69). So "prepare, wait `τ`, read" is available
  for every `τ`, and the held record `Z_τ` changes with `τ`.
- Under the default convention "held = a function of the present configuration `V_t`"
  (OA1:107–110), `Z_τ` and `Z_τ′` are not jointly held. Their joint law is not an available
  statistic.
- Retention is itself open on `main` ("That is retention: O-RET, O-REC and O-ACC, all open",
  obsmu:917).
- A single `Λ = values of Z₀` then does not carry all effects. Preparation noncontextuality
  needs the class to fix the *joint* law of `(Z₀^{(τ)})_τ`, and only the marginals are
  fixed.

**Why this is the gbit's ingredient.** The setup is two sharp reads whose joint is unavailable,
plus preparations that fix their parity through an earlier read. MECH-2:523 states it: "a law on two
bits read only one bit at a time generates the square state space, a gbit". In an affine world the
same per-horizon asymmetry as 𝔊_K's (AW-OA2-2) is not excluded by (H1)–(H3):
- pre-reference heralds read `ℓ₁ + ℓ₂`;
- post-reference reads within the horizon read `ℓ₁` and `ℓ₂` separately and never their sum.

I have not constructed a full counterexample that also meets the label and record conventions of F4.
I flag it as a gap, not a refutation.

**Internal inconsistency.** (H3) excludes "supplied timing selection" (R:333). Pressure test 2
handles only MP-0b ("MP-0b's whole history is still one `Z`", R:386–387). If protocol durations
are part of Proc, then reading at different times is native. If they are not, Lemma 1 and
Theorem C lose the closure they use (R:171, R:208).

**Required.** Do one of the following.
- (a) Add an explicit (H4), nested records: within the horizon, the held record at the latest read
  determines every earlier available read, as under MP-0b with the history retained. Restate
  Theorem E, Corollary E1 and the headline under (H4).
- (b) Prove (b) for non-nested multi-time families.
- (c) Exhibit the counterexample.

Pressure test 2 must be rewritten either way.

### F3 (major): "fails G3" outruns (b)'s own spanning condition

**The gap.** (b) gives simplex-embeddability only "if the reachable laws of `Z₀` span the functions
on their support" (R:348–349). Without that condition only preparation noncontextuality is shown.
The Limits note this (R:622–623). Yet the following all state G3 failure or "classical"
unconditionally:
- Verdict N2.4 (R:356–357), "fails G3";
- §0 item 6 (R:46–48), "the emergent theory is classical … for every measure";
- the conclusion table (R:498);
- the status table (R:539), "classical E3";
- §3.1 (R:468).

**Why spanning matters.** F1's counterexample is exactly a single-`Z` affine readout with every
singleton indicator available and non-spanning reachable laws. It is measurement-contextual. §3.1's
own row "G1 can pass (restricted reachable laws)" (R:465) is the regime in which spanning can fail.

**Measure.** §0's "for every measure" holds only for (a). (b) needs (xiv), which OA-1 records as
possibly failing on the actual orbit under μ-O and μ-R (OA1 §2A, the row "N2, operational
reading via (xiv)").

**Required.** Carry "spanning" and "(xiv)" into every place that states the N2.4 verdict, or prove
spanning for the affine class.

### F4 (moderate): 𝔊_K's exact equivalence needs a stated prepare-measure convention

**The conflict.** E3's effects are "**all** post-processings of held records: none is removed by
fiat" (R:70). In 𝔊_K the A/B label is held: "The observer therefore holds only the label A or B"
(R:265). PREP(p_x, p_y) leaves `p_x` and `p_y` in held setting cells (R:253–254). So:
- reading the label distinguishes PREP(A) from PREP(B);
- reading the `p` cells distinguishes the explicit mixture `½[00] + ½[11]`, which is selected by
  a coin through PREP(a, a), from PREP(A).

Claim 1 (R:268–279) and step 4 of Claim 2 (R:288–292) therefore fail under the report's own
definition.

**The usual repair.** Effects on the system do not read the preparation procedure's records. This is
Spekkens' convention, or equivalently a PREP that moves its setting and coin cells out of reach under
the same horizon argument. With that repair, Claim 1 holds per horizon. I re-derived the MEAS step:
after MEAS(0), the joint law of the record, the carrier and the cells in reach is `(b, b_fresh)`
under both A and B. FLIP and SWAP map `{P_A, P_B}` to itself. Claim 2's support-disjointness
argument is then correct.

**Smaller gaps.**
- PREP(A/B)'s bath bit "rotates out of reach" (R:265), but no gadget rotates the bath except MEAS
  (R:257–258). If the next MEAS uses the same bath cell, `y` is not re-randomized under A, and two
  MEAS steps reveal the parity.
- The horizon count `M > K` must include rotations caused by PREP.

**Required.**
1. State the convention in §1.1–1.2 and reconcile it with "none removed by fiat".
2. Apply it uniformly to Theorem E.
3. Specify PREP(A/B)'s rotation.
4. Recount `M`.

### F5 (moderate): Theorem E is not NEW against the corpus, and §A.19 was not met

**Prior parts of Theorem E.**
- (a) and (c) are MECH-1 Lemma A (i)–(iii) (MECH-1:404–418) and OA-1 D5 (OA1:172–190).
- The key step of (b) is already on record:
  - MECH-1 Corollary A′: "Choosing afterwards which record to consult does not escape Lemma A.
    The physical joint law of all records does not depend on the setting" (MECH-1:424–425);
  - OA-1 D7: "every 'selectable' read is a coarse-graining of one joint record" (OA1:198–199).
- From "one setting-independent joint record, with settings acting by translation", the classical
  model is a standard one-step consequence.
- obsmu Proposition C (obsmu:546–580) already gives the coset structure of homomorphic-readout
  record laws.

**Reading inventory.** The report lists MECH-1 and TUNE-1 as "Not read" (R:613). It labels Theorem E
NEW (R:553) without reading the record whose Corollary A′ states its core premise.

**Required.**
- Reclassify Theorem E as **ELABORATING**: the E3-level, GPT-form corollary of MECH-1 Lemma A,
  Corollary A′ and OA-1 D7, conditional on (H1)–(H4), (xiv) and spanning.
- Credit those three and obsmu Proposition C.
- Change the tally to "no NEW findings" (R:578).

### F6 (moderate): Corollary E1's "gap-2 repair is necessary for gap 3" is conditional

**What OA-1 said.** OA-1's "Independent of the gap-2 repair" (OA1:515; gap-2 row, "does not by
itself bear on gap 3") is a statement about **sufficiency**: dropping A5 does not close gap 3, and at
configuration level D6 shows this. OA-2's necessity is a different direction. The two do not
contradict each other once they are stated precisely.

**What OA-2's necessity needs.** It holds only:
- for gap 3 read as G3 in E3. OA-1's gap 3 is "a sourced operation beyond the configuration-level
  ceiling", which is broader;
- under H-AR, (H4) of F2, spanning (F3) and (xiv).

**Escapes without non-translational setting dependence that remain open:**
- non-additive partitions (AW-OA2-1, R:392–397);
- non-nested multi-time reads (F2);
- non-spanning reachable laws (F3).

**Wording.** "Gap-2 repair" in OA-1 means MP-1. E1's necessary condition is met by MP-1 **or** by
supplied P3/E-iso, so the condition is "non-translational setting dependence of read functionals",
not the repair itself.

**Required.**
1. Restate E1 and §0 item 7 as: within E3 and for G3, under (H1)–(H4), H-AR, spanning and (xiv),
   a G3 escape needs a non-translational setting dependence of the read functionals (MP-1 or
   supplied P3/E-iso).
2. Add "compatible with OA-1's insufficiency statement".
3. Drop the claim that E1 shows the repair is necessary for gap 3 outright (R:555).
4. "Closes OA-1 row 5d for the native affine class" (R:554) becomes "closes 5d for the affine class
   under H-AR, nested records, spanning and (xiv)".

### F7 (moderate): H-AR is a restriction on observers, and its support citation is weak

**The claim.** Pressure test 5 says H-AR holds because "Main's partition is the projection `π_V`
(Main:82–92), which is cell-aligned in the lattice model" (R:396–397).

**What Main supports.** Main:82–92 is the partition-relativity lemma. It says nothing about cell
alignment. Site-region observers are suggested at Main:260 and :650, but Main also uses observation
maps with an induced coarse-graining (Main:664). Main's Definition requires only "finitely many
distinguishable internal states" (Main:42).

**Why it matters.** A thresholded or coarse-grained readout, as in a detector click, is not
additive. So H-AR is a substantive restriction on the class of observers, not a technicality.

**Required.**
- Cite Main:260 and :650 for site regions.
- State H-AR as a named restriction in §0 item 6 and in the conclusion row.
- Keep AW-OA2-1 open as written.

### F8 (minor): Theorem C, step 3, and prior art

**Proof.** The proof is correct apart from one step [RW]. `E` need not be convex, and it may be
finite. So "π_E(E) = E forces |det| = 1" (R:212) should be argued on `K = cl conv(E)`, which is a
convex body in `aff(E)` with `π_E(K) = K`.

The other steps hold:
- `π(W) ⊆ W` follows from the closure of the reachable set.
- `P_W` is a polytope, being the linear image of `Δ ∩ W`.
- Equal volume plus inclusion gives equality.
- Polytope automorphisms are a finite group.
- Inverses are powers of the map and are therefore induced.

The example is also correct. `cos θ = 3/5` gives `e^{iθ} = (3+4i)/5`, whose minimal polynomial is
`5x² − 6x + 5`. It is not an algebraic integer, so its order is infinite.

**Prior art (§A.19).**
- AP1 §5.3 (AP1:955–979) already derives "no finite carrier induces `rot` with exact statistics"
  in-corpus, with no import. It uses Perron–Frobenius and Niven, for any stochastic matrix on a
  finite ontic set.
- So "a self-contained derivation … that OA-1 R7 took half-imported from Main:558" (R:223–224) is
  inaccurate.
- Main:558 also concerns prepare-measure behaviours (nonnegative rank), not operations, so
  Theorem C is an operations analogue, not a replacement for it.
- The finiteness of reversible transformations of polytopic state spaces is standard in the GPT
  literature [context, cited from memory: e.g. Gross–Müller–Colbeck–Dahlsten, PRL 104, 080402
  (2010)].

**Required.**
1. Patch step 3.
2. Credit AP1 §5.3.
3. Restate the Main:558 relation.
4. Keep ELABORATING.

### F9 (minor)

- **Lemma 0, "exactly when" (R:151–152).** A fixed lift is sufficient. It is not necessary:
  strong lumpability (`M(i|s)` constant within classes) also makes the coarse map well defined.
  Write "when" (§A.34).
- **Heralds (R:231–233; G2 row, R:107).**
  - Bayesian filters at fixed `S` generate a countable family from finitely many likelihood
    vectors per protocol, not "a continuous group".
  - Reversibility on `E` also needs the inverse heralds to be available.
  - Restate as: infinite-order injective heralded maps exist at fixed `S`, and they are reversible
    on `E` when the inverse likelihoods are reachable.
- **Theorem E(c) (R:350–352).** "One fixed … stochastic map (the pushforward averaged over α)"
  needs a fixed conditional law of `α` given `σ`, that is H-LIFT (cf. R:165). State it.
- **§3.1 (R:468).** `OB/CentralObservation.lean:620` concerns passive instruments on matrix
  algebras. It is context for the full-access row, not support for an E3 classification. Label it
  as context.
- **Corollary E2 (R:372–379).**
  - Correct [RW]: `E(a, b) = K s(a) t(b)` with `s, t = ±1`, so `|CHSH| ≤ 2|K| ≤ 2`.
  - The `Z₄` example checks: `w = 0` and `g(0) = g(1) = 0`, `g(2) = 1` give `B = ab` and
    CHSH = 4, and it signals.
  - Relative to Main:414 it trades the graph-cone locality hypothesis for parity outcomes and the
    affine class. Say "complements", not "extends … in this one direction".
- **§0 item 4 and §3.1 "Reading" (R:42–44, R:472–475).** Scope "non-discriminating" to bounded
  horizons. 𝔊_K is exact only per horizon (R:305–308), and whether any G3 success survives
  unbounded protocols on a finite bijection is AW-OA2-2, which is open.
- **Credits for 𝔊_K's role (R:313–316).** Cite MECH-2:523–529 (gbit from one-at-a-time reads;
  "not a nonclassicality witness unless the missing reads are absent for a physical reason") as
  in-corpus prior art. 𝔊_K is then a designed classical, per-horizon instance of M-INACC (a)–(c),
  which strengthens AW-OA2-3.

***

## Item-by-item answers to the brief

1. **Definitions.**
   - E1–E3 and G0–G3 are target-neutral: laws, `[0,1]` responses, convex structure.
   - G4 and G5 are correctly kept out of the verdicts.
   - The measure is stated per result. But §0 says "for every measure" where (b) needs (xiv) (F3).
     There is no per-result measure table of OA-1 §2A's kind; it is advisable, not required.
   - The effect convention needs fixing (F4). "Common preparation and readout", (d)1–4, is
     adequate and matches OA-1's non-import test (OA1:119–120).
2. **𝔊_K.**
   - The contextuality proof is correct given F4's convention.
   - Exactness holds per horizon `K < M`, not under every procedure: the report states this at
     R:305–308 but not at R:322 or R:495.
   - It passes G0, G1 and G3, fails G2 at fixed `S`, and fails G4 and G5.
   - The criteria are non-discriminating at bounded horizon, which MECH-2:523–529 already
     anticipates.
3. **N0 "NO".** Correct, and correctly scoped to E1/E2 with a fixed lift (Lemma 0, Proposition A).
   Only the "exactly when" wording needs repair (F9).
4. **Theorem C.**
   - Correct after the step-3 patch. The hypotheses are complete: finite `S`, linear effects,
     closure of the reachable set, trace-preserving. It is restricted to trace-preserving maps.
   - Independence from Main:558 is right, but Main:558 is about a different object.
   - Corpus prior art is AP1 §5.3. Literature: polytope automorphisms (F8).
5. **Theorem E.**
   - (a) and (c) are correct and already in MECH-1 Lemma A and OA-1 D5.
   - (b) is correct only for one nested record (F2), and G3 failure needs spanning (F3).
   - "Additive readout" is a real restriction on observers (F7).
   - It is not NEW (F5).
   - It closes row 5d only under the added conditions.
   - "Necessary" reconciles with OA-1's "independent" as necessity against sufficiency, but only
     conditionally (F6).
6. **CHSH ≤ 2.** Correct for the affine class at `q = 2` with parity outcomes and (xiv). The scope is
   stated, and the relation to Main:414 needs rewording (F9).
7. **Proposition B / B′.**
   - The preparation-only form is false (F1).
   - The correct two-route form is MECH-2's M-INACC "why needed" (MECH-2:842) made
     frame-independent: preparation **or** effect equivalences coarser than ontic equality.
   - Corollary B′ is therefore CONFIRMING of MECH-2. It is not "now necessary in E3 for every
     rule" in the form stated.
8. **G_SM OPEN, and the next steps.**
   - OPEN is sound, and the skeptical reading of P★ and minacc-1 is apt.
   - Step 1 must add the dual shape (F1).
   - Step 2 is correctly framed as needing separate authorization. But its preregistered control
     "the affine ring `N₁` must return embeddable (Theorem E)" is valid only if the enumeration
     uses (H4) nested records (MP-0b), H-AR and a spanning check. Otherwise Theorem E does not
     predict the outcome (F2, F3).
   - The computation's spec must also fix μ, the partition, the horizon, and the label convention
     of F4.
   - The exact-rational LP requirement is right under the exactness rule.
9. **Overreach.**
   - §0 items 3, 6 and 7, Verdict N2.4, the conclusion row "OI's native rule class: NO", and the
     status table entries for B′ and E.
   - The NEW label on E.
   - "For every rule" on B′.
   - "Continuous group" for heralds.
   - Layer labels are not misused ("Layer-0 revision" for `G_SM` is correct, Main:724 (vii)).

## Required changes (summary)

1. Correct Proposition B and Corollary B′ to the two-route form, with credit to MECH-2. Re-derive
   the class-N result. Fix §0.3, N-b, next step 1 and the tables (F1).
2. Add (H4) nested records to Theorem E, or prove or refute the multi-time case. Rewrite pressure
   test 2 (F2).
3. Carry spanning and (xiv) into every G3 or "classical" verdict for the affine class (F3).
4. State the prepare-measure label convention. Fix PREP(A/B)'s rotation and the `M` count (F4).
5. Reclassify Theorem E as ELABORATING, credit MECH-1 Lemma A, Corollary A′, OA-1 D7 and obsmu
   Proposition C, and make the tally zero NEW (F5).
6. Restate E1 and §0.7 conditionally, and reconcile them with OA-1:515 as necessity against
   sufficiency (F6).
7. Name H-AR as an observer restriction wherever the NO is stated, and fix the Main citation (F7).
8. Theorem C: repair step 3, credit AP1 §5.3, restate the Main:558 relation (F8).
9. Apply the minor fixes in F9.

## What OA-2 establishes, and at which layer

All of what follows is paper-level [W]/[RW]: unreviewed hand derivations, none kernel-checked,
nothing adopted.

**Conceded by the report and confirmed here**
- On laws over configurations or record classes with a fixed lift, every induced operation is
  stochastic, and the reversible ones are permutations.
- On the closure-defined operational class E3, induced operations are well defined and linear.
- At any fixed finite carrier, the reversible trace-preserving emergent operations form a finite
  group, for every rule, measure and interface. This is an operations analogue of AP1 §5.3 and
  Main:558.
- A designed reversible classical computer has, at bounded horizon, an exactly gbit-shaped,
  preparation-contextual emergent theory, under a stated prepare-measure convention. Target-neutral
  single-system criteria G0–G3 therefore do not by themselves separate classical from quantum
  dynamics. The decisive question remains sourcing, items (d)3–4.

**For the gauge-derived affine class**
- Settings act by translation after one fixed noise map, measure-free. This was already MECH-1
  Lemma A and OA-1 D5.
- At `q = 2` with parity outcomes and (xiv), CHSH ≤ 2.
- The emergent theory is classical only under additional hypotheses: H-AR, nested held records,
  (xiv) and spanning. Without them its classicality at the E3 level is not established. The
  question "is OI's native affine class classical at the record level?" is narrowed, not closed.

**Open (Layer-0 revision ground)**
- Whether an admissible non-affine rule such as `G_SM` supplies G3, by either the preparation or
  the measurement route, and then a qubit-type fragment that passes non-import.

**No manuscript claim is affected.**
