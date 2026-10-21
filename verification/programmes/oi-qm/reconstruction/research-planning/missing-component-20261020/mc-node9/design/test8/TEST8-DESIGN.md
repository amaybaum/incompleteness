# Node 9, test 8: can an access condition force the polarization map? Design and gem-finding pass

> **DRAFT — NOT FROZEN.** Design note for the owner and the coordinator. It preregisters nothing, and nothing in it
> is adopted. No manuscript, kernel file or record outside this directory is changed.

Base: branch `research/missing-component-20261020`, head `9be40875`. Scripts run with `python3 -I`, use Fractions and
Gaussian integers only, run in under 3 CPU-seconds, and replay byte for byte (`SHA256SUMS`).

Tags:
- [corpus file:line] cites the corpus.
- [kernel `name`] cites a statement under `verification/lean-mathlib/OIBridge/`, read from source; no `lake` build was run.
- [exact, script] is a check in this directory.
- [exact, algebra] is a proof given here in a few lines and not kernel-checked.
- [arg] is an argument, not reviewed.
- [lit] is literature, with the check that was made.
- [open] is undecided.

## 1. The target, stated exactly

**Objects.** A site configuration is x = (p, c) ∈ V × V: p is the previous value and c is the current value
[kernel `Substratum.Conf`, `curOf`, SubstratumInterfaceAudit.lean:78]. The two layers are:
- the shear τ(p, c) = (F(c) − p, c);
- the swap σ(p, c) = (c, p).

Both are involutions of the configurations [kernel `shear_shear`, `swapLayer_swapLayer`, SecondOrderCircuit.lean:89,
:96]. On V = F₂:
- the C5 audit's map sends τ to the quarter phase S = diag(1, i) and σ to H, on the carrier `Fin 2 × Fin n`
  [kernel `siteShearImage`, `siteSwapImage`, C5Discovery.lean:192, :196];
- that carrier is the position alphabet times an ancilla. It is not V × V.

An **encoding** is a map E from a set P of admitted preparations to density operators on ℂ^V ⊗ K, where K is an
untouched spectator. For a layer F acting on P and a unitary U, write

- Cov(F, U): E(F p) = (U ⊗ 1) E(p) (U ⊗ 1)† for every p ∈ P.

Three further clauses can be imposed on E:
- **NT (nontriviality).** E is not constant. The coordinator's formulation lacks this clause, and the constant map
  I/2 satisfies every Cov(F, U).
- **PR (reads the position half).** The Z-statistics of the site factor of E(p) are a non-constant function of p's
  current-value marginal.
- **AI (affine injectivity).** E is affine on distributions and injective on the affine span of P.

**Three statements kept apart.**
- (a) **A representation exists.** Matrices H and S are posited on the position carrier, as in `PolGen` and `PolC`.
  This is already known. By the audit's own rule it fails test 8, because reading a representation as an
  availability is not a sourcing map [corpus c5-discovery-audit.md:108–110].
- (b) **A forces the map.** An access condition A, whose definition avoids the test-7 vocabulary
  [corpus c5-discovery-audit.md:67–70], *implies* that every E satisfying A (with NT and PR) satisfies
  Cov(σ, H) and Cov(τ, S), up to a stated equivalence. A must also be satisfiable.
- (c) **A is consistent with the map.** A ∧ Cov ∧ NT is satisfiable.

**Which direction test 8 asks for.** Test 8 asks that the map be *supplied*: stated by the corpus, or by a
condition, before any experiment [corpus c5-discovery-audit.md:71–74, :249].
- The obligation is therefore the sufficiency direction (b): A ⟹ map.
- The converse (map ⟹ A) is not the obligation.
- (c) is necessary for (b) and not sufficient for it.

## 2. Productivity test, fixed before the pass

The pass is a **gem** iff it yields a fact strictly stronger than T6's record ("the corpus does not supply the map")
and that fact either constrains which encodings E can satisfy the test-8 intertwining or exposes a hidden assumption
of candidate 2. Otherwise it is a non-gem, recorded only.

**Verdict: gem.** N1, N2 and N3 each constrain E or expose an assumption (see §5).

## 3. Depth-first pass

The nodes are ordered by decisiveness. Each closes with a check and a verdict.

### N1. Do the two images admit any common covariant encoding?

**Check [exact, algebra].** Let P be any set closed under τ and σ, and E any function on P, not necessarily affine.
From Cov(τ, U_τ) and τ² = id:
- E(p) = E(τ²p) = Ad_{U_τ²}(E(p)), so every E(p) commutes with U_τ² ⊗ 1.
- For U_τ = S or S†, which are the two Weil lifts that fix the position basis, U_τ² = Z.
- So [E(p), Z ⊗ 1] = 0 for every p ∈ P.
- Applying this to σp and using Cov(σ, H) gives [E(p), X ⊗ 1] = 0.
- The commutant of {Z ⊗ 1, X ⊗ 1} is 1 ⊗ B(K) [exact, script: real dimension 8 for K = ℂ²].
- Hence E(p) = I/2 ⊗ ρ_K(p) for every p. The site carries no information, whatever the spectator and whatever P.

**Check [exact, script].** The script repeats the test for every Pauli-coset lift, shear ↦ S·P and swap ↦ H·Q.
- No pair admits a PR encoding at one site.
- The only non-constant solutions use the lifts S·X and S·Y. These are involutive, but they move the position basis
  (Ad: Z ↦ −Z), so they are not phase images of the shear, which fixes c [kernel `curOf_shear`].
- A position-fixing lift of the self-coupled shear has projective order 4 [exact, script: S² = Z]. The layer has
  order 2.
- So the map is a homomorphism only of the ℤ/4 lift of the layer, the Clifford group over ℤ/4. It is not a
  homomorphism of the group the layers generate on configurations. This is where the quarter phase comes from.

**Verdict.** The full polarization map admits no NT ∧ PR encoding at all, at one site, with or without a spectator.
- No access condition can force it, because the only encodings it allows are the trivial ones.
- **NEW** (hidden assumption: the ℤ/4 lift).
- Pressure test: the finding bears on test 8 only. It changes nothing in the audit's kernel results, which concern
  the class `PolGen`/`PolC` and posit no E.

### N2. Does the corpus's rule produce the quarter phase at all?

**Corpus.**
- The displayed update is u'_x = Σ_{z∼x} u_z + v_x [corpus Main.md:290]. It is centre-free: the update at a site
  contains no copy of that site's present value [corpus SM.md:224, :228, :236].
- Over F₂ the shear is (p, c) ↦ (p + Lc, c), with L the adjacency matrix, whose diagonal is zero. Reading z ∼ x as
  excluding x is my reading of the notation [arg].

**Check [exact, algebra].**
- A diagonal Weil lift D = diag(d_c) satisfies d_{c+a} = d_c d_a (−1)^{(La)·c}.
- Putting c = a gives d_a² = d_0² (−1)^{Σ_x L_xx a_x}.
- So d_a/d_0 = ±i exactly when Σ_x L_xx a_x is odd.
- [exact, script, brute force over all candidate lifts] at n = 1, 2, 3, for paths and triangles with and without
  centre terms: 2ⁿ lifts in each case, and the criterion holds everywhere.

**Consequences.**
- For L with zero diagonal, every Clifford lift of the shear is real up to phase: a CZ network times a Pauli.
- H is real, and so are the scaled partial permutations [kernel `IsScaledPartialPerm`].
- Every constructor of `PolGen` and `PolC` preserves the set ℂ·Mat(ℝ) [arg].
- By the bridge [kernel `exists_scaled_mem_of_instAvail_unitary`, MicroscopicReversibility.lean:251], availability
  of `phaseGate` would place c·diag(1, …, i, …, 1) in ℂ·Mat(ℝ), which is impossible.
- So the class sourced from the corpus rule's Weil images has no O1 [arg].

**Verdict.** The site quarter phase of candidate 2 needs a centre term, F(c) ∋ c, which the corpus's centre-free
branch excludes.
- So the dilemma holds both ways:
  - with a centre term, N1 kills every encoding;
  - without one, the images are real and give no phase.
- **NEW**; an assumption-watch marker on candidate 2 [corpus c5-discovery-audit.md:91–106].

### N3. The swap half alone: what structure does Cov(σ, U) force? (favourable branch, pressure-tested)

**Sign obstruction [exact, algebra].** Suppose E is AI on Δ(C) with |C| = d², and Cov(π, U) holds for a permutation
π of C.
- The linear part intertwines π on sum-zero vectors, whose determinant is sgn π, with Ad_U on traceless Hermitian
  matrices, whose determinant is +1.
- So sgn π = +1.
- σ and the self-coupled τ are transpositions of the four site configurations [exact, script: signs −1, −1]. The
  self-coupled one-step map is a 3-cycle (+1).
- So at one site, no AI encoding is swap-covariant for any unitary. All 24 single-qubit Clifford rotations have
  determinant +1 [exact, script].
- Controls [exact, script]:
  - the one-step map with U = HS or SH (positive control) admits rank-3, injective solutions;
  - the antiunitary H·K (det −1, countercontrol) admits rank 3;
  - every unitary lift admits rank at most 2.
- [lit] matches Spekkens's toy bit. Its permutations of four ontic states act as the tetrahedral group: even
  permutations act as rotations, and odd ones as reflections, the analogues of antiunitaries
  (quant-ph/0401052; search summary, not re-derived here).

**U = H with PR [exact, script].** Every solution has the same three features:
- x(p, c) = g(p) and z(p, c) = g(c). The previous value is read in the X basis with the same response function as
  the current value.
- The swap-fixed configurations (v, v) go to g(v)·(1, 0, 1).
- So |g| ≤ 1/√2. The position readout is unsharp with bias at most 1/√2. A rational witness exists (g = ±1/2).

**Pressure test.** The favourable reading is that a non-constant swap-covariant PR encoding exists. It does, but
with four limits:
- (i) It is not AI: rank at most 2, and a σ-symmetric direction is lost.
- (ii) It cannot be sharp.
- (iii) It reads the previous value as strongly as the current one, in a conjugate basis, which is the opposite of
  "reads the position half".
- (iv) The class it would source is ⟨H, permutations⟩: real, so no O1 by N2's argument, and countable, so no O2
  [kernel `polC_countable_upToScalar`].

**Verdict.** The swap-only target is strictly weaker than "the polarization map", and a positive answer to it yields
neither O1 nor O2. **ELABORATING**, with the sign obstruction **NEW** for this target.

### N4. Does the corpus place the previous value outside the observer's read? (§A.19)

**Corpus.** Two statements bear on this.
- **Discrete realization.** The visible sector is the sites of R with s = dim V = 2|R| [corpus Main.md:292, :316],
  so both slices of a visible site are read. Lemma 2's Weyl operators act on ℂ^{F₂^{2|R|}} [corpus Main.md:300–306].
- **Continuum §3.1.** "T_ij are projections of the full phase-space flow onto the configuration sector of Γ_V, with
  momenta … absorbed into the Liouville marginalization" [corpus Main.md:216].
  - This is an access statement of the requested logical type: it places the momentum half outside the read.
  - T6's record ("Γ_V × Γ_H splits sites") is accurate for the discrete realization, but it does not mention this
    sentence.

**Check [exact, algebra; exact, script].** Formalize Main.md:216's reading as E(p, c) = e(c), so that the encoding
ignores the previous value.
- Cov(σ, U) then gives e(p) = U e(c) U† for every p and c.
- So e is constant, for every U (H, H·Y, X, and the antiunitary H·K were checked).

**Verdict.** The one corpus access statement of the right type excludes the target rather than forcing it. The
classical reading (distributions over positions, momenta marginalized) is that statement.
- The two corpus surfaces differ: §3.1 marginalizes the momenta, while §3.2 reads both slices.
- This is recorded for the coordinator and not edited.
- **NEW** (a corpus statement the audit did not cite), **CONFIRMING** outcome C.

### N5. Can any C1–C4-type condition exclude the classical reading?

**Kernel.**
- The permutation theory realizes the sealed OI core, which is C1–C4, with no phase
  [kernel `permTheory_twoState`, `permTheory_realizesSealedOICore`, SubstratumInterfaceAudit.lean:740, :753].
- The observer theory is rule-independent [kernel `obsTheory_rule_independent`].
- "Bare finite OI therefore does not select quantum mechanics" [corpus Main.md:352].

**[arg]** A condition on the rule, the partition or the prior leaves the observer theory at `permTheory` under the
stated sourcing. Only a condition that changes the encoding can change it. By N3, any surviving encoding must specify
a conjugate-basis readout of the previous value. That is new structure: Main.md:262's identification is diagonal and
Main.md:216 marginalizes the momenta.

**Verdict.** Such a condition is necessarily new physical structure, which is outcome C again, now with the missing
structure named exactly. **CONFIRMING**.

### A1 (coordinator addendum 1). Is there one encoding under which H, S and the relabellings all act?

**Definitions.**
- `PolGen` and `PolC` place every generator on one carrier and one basis [kernel `PolGen` C5Discovery.lean:221,
  `polGen_arch` :234, `PolC` PolarizationClosure.lean:150]:
  - `perm` is a scaled partial permutation at any carrier;
  - `shear` and `swap` act on `Fin 2 × Fin n`;
  - `relabel` reindexes along any carrier bijection.
- Inside the kernel class, the Toffoli, the CNOT and the relabellings are therefore basis permutations in the same
  position-amplitude basis in which H and S act. The card report's encoding mismatch does not arise inside `PolC`.
- That common basis is stipulated in two ways:
  - the observer's sourced relabellings, including the shear and swap layers themselves, are permutation matrices on
    `Conf × Fin n` with Conf = V × V [kernel `obs_shear_avail`, `obs_swap_avail`, `obs_exchangesAvailable`,
    SubstratumInterfaceAudit.lean:799–816];
  - `PolC`'s `perm` constructor instead permutes the *position* carrier.

**Exact.** Under the Weil encoding of a site's (p, c) onto position amplitudes:
- a position permutation is the image of a phase-space map only if it is affine;
- of the 40,320 permutations of 8 positions, 1,344 are Clifford, exactly the affine ones;
- the Toffoli is neither affine nor Clifford [exact, script];
- the shear fixes c, so read as a configuration relabelling on the position carrier it is the identity, while its
  Weil image is diag(1, ±i) [exact, script].

So `PolC` combines two rules on one carrier:
- Weil images for the two layers;
- "carrier permutation = sourced relabelling" for the access.

They assign different images to the same layer, and the Toffoli is not the image of any substratum relabelling
under the first rule. The card witness recomputes as stated: at most 1 for products of X/Z vertices, and 2 for the
graph state [exact, script].

**Verdict.** `PolC` is one encoding only by stipulation. No encoding of substratum preparations carries even H and S
together (N1). **NEW** (the double assignment of the shear).

### A2 (coordinator addendum 2). Does `PolC` give dense finite QM? (favourable branch, maximum skepticism)

**Kernel.**
- `fixedGateTheory_denseFiniteQM` is a theorem about `mixTheoryR {α}` [kernel DenseInstrumentBridge.lean:521]. It
  is not a hypothesis schema.
- The general route is `krausDense_of_fixedGate` (DerivedOI, α/π irrational, `FixedGateSourced α`), or
  `denseFiniteQM_of_denseControl` (DerivedOI, `DenseUnitaryControl`, `KrausSoundExt`)
  [kernel DenseInstrumentBridge.lean:496, :502].
- For `polarizedTheoryC (Fin 2)`, DerivedOI holds [kernel `polarizedTheoryC_derivedOI`].
- KrausSoundExt follows by the same one-line route as for `fixedGateTheory` [arg; kernel
  `krausSoundExt_of_implementationGenerated`, ImplementationLocality.lean:963].

**Missing.** `FixedGateSourced α`, that is, the exact availability of the real rotation `mixImage n α` with α/π
irrational at every level, or `DenseUnitaryControl` at every level n ≥ 1. Neither is a kernel theorem. Known
constraints:
- **Ring constraint [arg].** Every `PolC` element is a scalar of modulus at most 1 times a contraction over
  ℤ[1/√2, i]. A unitary element is therefore a unit scalar times a unitary over that ring. Entry squared moduli then
  lie in ℤ[1/√2], and the rational ones in ℤ[1/2].
  - This excludes, as exact unitaries, the level-three reflection's rotation (cos² = 4/5), report 3's R
    (cos² = 9/25) and the 1-radian gate [exact, script].
  - It does not exclude every irrational angle (cos² = 5/8 passes).
- **Level one.** The unitaries generated there without blocks form the 24-element Clifford group [exact, script].
  The only non-Clifford level-one element known is contractive, and its unitary direction is not claimed
  [corpus polarization-closure-audit.md:200–214, T6 row].
- **Literature.** The density facts, Clifford plus any non-Clifford gate on qubits [lit: Nebe–Rains–Sloane 2001;
  Boykin et al. 1999; not re-checked here], concern group closure on qubit tensor powers. `DenseUnitaryControl` asks
  for available approximants at every carrier `Fin 2 × Fin n`, including n = 1 and dimensions that are not powers of
  two. No bridge is stated [open].

**Pressure test.** Suppose density held. It would still be a property of a representation:
- N1 shows that S has no covariant source with a centre term;
- N2 shows that without one, the sourced images are real, and ℂ·Mat(ℝ) stays a positive distance from S, so it is
  not dense.

The report's PR countercontrol stands, and exclusion and soundness remain a separate obligation.

**Verdict.** The claim that test 8 plus exclusion is the whole remaining gap is not established. Test 8's shear half
is unsatisfiable (N1), and density of `PolC` is [open]. **BORDERLINE**: the favourable branch does not survive.

### Fixed point

Two further passes found nothing new:
- the spectator, by N1's commutant;
- multi-site swap layers, through the site marginal [arg]: if the spectator's configuration does not change the site
  marginal, the marginal map inherits Cov(σ, U) and N3 applies.

## 4. Decision rule for a future probe (rule, not expected numbers)

**Input.** A candidate access condition A, given as definition text, together with its formalization: P, E's
regularity, the equivalence ~ and the spectator clause.

**Verdict, generated from the measurements.**

| verdict | rule |
|---|---|
| VOID | any control in the table below fails |
| DEAD-VOCAB | A's definition uses test-7 vocabulary |
| EXCLUDES | A ∧ Cov(σ, H) ∧ NT ∧ PR has no solution at one site (with and without a spectator, m = 2) |
| CONSISTENT-ONLY (c) | a solution exists, but some E satisfying A ∧ NT ∧ PR violates Cov(σ, H) modulo ~ |
| FORCES-SWAP (b, swap half) | every E satisfying A ∧ NT ∧ PR satisfies Cov(σ, H) modulo ~, and one exists |
| FORCES-MAP | FORCES-SWAP, and the same holds for Cov(τ, U_τ) with U_τ a position-fixing lift; N1 predicts this verdict is unreachable |

A FORCES-* verdict is a test-8 candidate only. It establishes nothing about O1, O2 or QM:
- the countermodel `PolC` has the map and is not QM [kernel `polarizedTheoryC_not_qm`];
- swap-half survivors source a real, countable class (N2, N3).

**Invariant → checkpoint table (§A.41).**

| invariant | checkpoint |
|---|---|
| arithmetic exact | no `float(` call and no decimal literal in the scripts (the one hit for "float" is a comment); Fractions and Gaussian integers only |
| layers as in the kernel | the script asserts τ² = σ² = id and the signs (−1, −1, +1) before any solve |
| the solver is not vacuous | positive control: the one-step map with HS has a rank-3 solution |
| the obstruction is the sign, not the solver | countercontrol: antiunitary H·K has a rank-3 solution |
| NT is enforced | constant E is reported separately and never counts as a solution |
| classical reading rejected | E(p, c) = \|c⟩⟨c\| is fed to the probe and must be EXCLUDES |
| configuration-level negatives | the diamond (\|x\| + \|z\| ≤ 1), diagonal-range E (the basis-permutation dilation, 12/25) and the `permTheory`/`substratumTheory`/`onesTheory` readings must each fail FORCES-* |
| calibration not a witness | report 3's interpreter (identity E on quantum states) is run as calibration and never as a FORCES-* witness |
| replay | outputs replay byte for byte against `SHA256SUMS` |
| resources | each run under one CPU-minute (§A.40) |

**Independent prediction (§A.29).** Any FORCES-SWAP survivor inherits the N3 consequence: unsharp readout of the
current value, bias at most 1/√2 on configurations with p = c, and the previous value readable in the conjugate
basis.
- This follows from the target, not independently from A.
- It is a risky consequence, since it conflicts with the sharp visible records the corpus uses (Main.md Lemma 3; the
  passive readout).
- No prediction independent of the target is identified.

## 5. Output classification and next step

**Pass classification: NEW.**
- N1: the full map admits no non-trivial covariant encoding; the ℤ/4-lift order.
- N2: the quarter phase needs a centre term that the corpus rule lacks.
- N3: sign obstruction, rank at most 2, unsharpness.
- N4: Main.md:216 is a corpus access statement, and it excludes the target.
- A1: `PolC` assigns two images to one layer.
- CONFIRMING: N5 (outcome C).
- BORDERLINE: A2 (density open, and irrelevant without sourcing).

**Where the coordinator's framing needs correcting.**
1. "Equivalently … the swap layer with U = H" is not equivalent: the swap-only target is strictly weaker, and the
   full map is unsatisfiable (N1).
2. The target needs NT. The constant map satisfies it as stated.
3. "The corpus does not supply this map: Γ splits sites" omits Main.md:216, which supplies the access half in
   classical form, and that half excludes the map.
4. "H … is the gate the polarization map produces" holds, but S is produced only with a centre term (N2).
5. Addendum 2: "test 8 + exclusion is the whole remaining gap" is not established (A2).

**Recommended next step for node 9.**
- (i) Record N1 and N2 as assumption-watch markers on candidate 2. Test 8 cannot source O1 through the polarization
  map on the corpus rule.
- (ii) If test 8 is kept, restate it as the swap-half target with NT, and accept that a positive answer gives the
  real countable class: no O1, no O2.
- (iii) Pursue the only per-layer-free option, the full one-step map, which is even and admits injective
  encodings, only after an owner decision. On the centre-free rule its Weil image is real Clifford, so it does not
  reopen O1.
- (iv) No probe is worth dispatching until a candidate A is written down. The rule above is ready for one.

## Files

`TEST8-DESIGN.md`, `t8_encoding_checks.py`/`.out`, `t8_weil_relabel_checks.py`/`.out`, `SHA256SUMS`.
