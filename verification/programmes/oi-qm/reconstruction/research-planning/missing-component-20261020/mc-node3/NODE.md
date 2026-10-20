# Node 3: substratum enlargement, observer settings and the global antiunitary as sources at A1

Research only, consistency axis (§A.23). F2 stays A1 (exact finite operational QM on qubit-power registers). No
premise adopted, no status changed, nothing written to `main`.

**Base.** `main` = `809fa9d6`. Every [AT] name was confirmed by `git grep` of its declaration at `df9e601e`, and paper
lines (Main.md:n, GR.md:n, Substratum.md:n) are at `df9e601e`; `papers/` and `verification/lean-mathlib/` are identical
between `df9e601e` and `809fa9d6` (`git diff --quiet`). Lean paths are under `verification/lean-mathlib/OIBridge/`. N1 = `../oa-node1/NODE.md`, MC1 = `../mc-node1/NODE.md`
(with node 1b, §9), MC2 = `../mc-node2/NODE.md`, PLAN = `../PLAN.md`, all with their review outcomes. LG =
`f2-ledger-20261020/LEDGER.md`. H = `verification/programmes/oi-qm/reconstruction/f2-research-threads/H-extension-candidates.md`
at `804843f1`.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (two runs,
byte-identical); [UP] unsourced premise; [L] literature; [rec] recorded in the cited record, not re-derived.

**Productivity test (fixed before the node).** Gem iff the node yields a fact strictly stronger than "no OI source is
known for (a) the measurement continuum, (b) a deterministic phase, (c) O-B", and either constrains the form a source
must take or exposes a hidden assumption.

***

## 0. Choice of lead

| rank | lead | reason |
|---|---|---|
| 1 | (i) substratum enlargement | PLAN's form statement keeps "non-supervenient, or enlarges the substratum" as its first clause, from CR's premise P1 (N1 §2.1). It is the only alternative to non-supervenience that the records leave open, and OI's own text licenses it (N1 below). A decision on (i) also decides (ii): an observer setting is a context fed to a substratum process. |
| 2 | (ii) observer settings | subsumed by (i) once settings are treated as contexts of arbitrary cardinality and origin (§3) |
| 3 | (iii) reconstruction principles | MC2 §3 already ranks purification with uniqueness as the one principle covering (a)–(c), as a posit; checked here only for derivability (§6) |
| 4 | (iv) antiunitary | MC2 §3 already records it as discrete and ones-fixing [W]; exact checks only (§5) |

***

## 1. Node N1: does OI license an enlarged substratum?

**Check (citation).**
- Only finite visible resolution is a theorem; the bijective substratum is a representation choice and total
  finiteness a physical posit (Main.md:62; posit ledger item (ii), Main.md:708).
- The deep sector "may be finite of any size, or infinite": decoupled, without changing any transition probability
  (Substratum.md:92, Theorem 24(iii) at :256); coupled with slow dynamics, changing T at O(t/τ_B) (:256, scope).
- Continuous configuration and time are named as the continuum analogue (phase flow, Liouville measure: Main.md:46,
  :58).
- The corpus guard records finiteness as load-bearing for the recurrence route only
  (`papers/oi_lattice_code/architecture_check.py`:94–101).

**Verdict.** Licensed in the deep sector, at any cardinality, with continuous configuration and continuous time. E3 as
read in Substratum.md:92 bounds the visible sector and boundary layer, so a continuum there is not licensed [rec].

**Cost.** Main.md:123 (step 1) and :139 use finite order of φ. A measure-preserving bijection of a continuum need not
be periodic (an irrational rotation of the circle), and Poincaré recurrence is approximate only [L]. An enlarged
representative therefore loses exact recurrence, and the route of :139 with it. CR's premise P1 fails, so CR no longer
applies. The question is whether anything else does.

***

## 2. Node N2: the cone lemma for classical substrata of any cardinality

**Modelling premise (the pointwise model).** The lemma computes the visible map at each fixed hidden point and
integrates over the prior. This is a commutative (pointwise) model of the hidden sector, with κ1 in its mixed reading:
the prior is a classical mixture of hidden points, not a vector. For a continuum X, "Ad_U on descriptions" is not
standardly defined, so for infinite X the pointwise integral is the definition of the induced map, not a consequence of
κ3. The kernel takes the mixed reading at finite carriers: `uniformAttach` (OperationalAssembly.lean:492) attaches "a
maximally mixed ancilla, never a pure one". Measurability is also assumed: bimeasurable bijections and measurable
settings, so that the weights w_P below are defined.

**Statement [W from AT; EC instances].** Fix a finite visible carrier C (visible configurations with finitely many
attached configuration ancillas). Let the substratum be C × X for a measurable space X of any cardinality, in the
pointwise model, with:
- (κ1) hidden states given by probability measures on X, read as mixtures (the realization prior, Main.md:60);
- (κ2) processes given by bimeasurable bijections of C × X, with any time index (ℕ, ℤ or ℝ), any real couplings, and
  any setting value selecting the bijection, settings drawn from a set of any cardinality and any origin;
- (κ3) the G3 identification: a process acts on coherence-level descriptions by Ad_U, U its permutation operator;
- (κ4) readouts that are configuration readouts, with classical feed-forward, coarse-graining and discard.

Then every available outcome map of every finite protocol lies in the cone

  𝒞(C) = { Σ_P w_P Ad_P : w_P ≥ 0 },

P ranging over the 0/1 partial permutation matrices of C, a finite set.

**Proof.**
1. For a hidden point h and a bijection b, Ad_U(ρ ⊗ |h⟩⟨h|) followed by the trace over X keeps the coherence between v₁
   and v₂ exactly when b sends (v₁, h) and (v₂, h) to the same hidden point x′. So the outcome map for fixed h has Kraus
   operators K_{h,x′} = Σ_{v : x(v,h) = x′} |v′(v,h)⟩⟨v|. They are injective, because b is, and each is a 0/1 partial
   permutation of C.
2. Readout projectors restrict the domain, and feed-forward selects the next bijection from a visible outcome. A finite
   protocol is a composite of bijections of C × X, so step 1 applies to the whole tree.
3. Integrating over h against the prior gives Σ_P w_P Ad_P with w_P the prior measure of the set of h at which P occurs.
   Only finitely many P exist, so the sum is finite.

The map is then `Realized permClass` with a finite index set, and `preservesNonneg_of_realized`
(SubstratumInterfaceAudit.lean:536) applies verbatim. ∎

**Relation to the finite-substratum results [AT].** At finite carriers the observer theory is `permTheory`
(`obsTheory_eq_permTheory` SubstratumInterfaceAudit.lean:774) and lies inside the coherent-lift theory
(`obs_availExt_le_coherentLift` LiftSource.lean:200, the audit's T2). `stochasticChannel_kraus_monomial`
(LiftSource.lean:251) exhibits one monomial Kraus realization of a classical stochastic map, and the module header
disclaims that every Kraus realization of the stochastic channel is configuration-level (LiftSource.lean:41–43). The
cone lemma fills that gap for the realizations induced by classical hidden dynamics in the pointwise model, at any
hidden cardinality.

**Where the mixed reading is load-bearing (review K1–K3, C1).** Represent the uniform prior on a two-point hidden
sector as the vector √μ = |+⟩ (the Koopman–von Neumann reading). A v↔h swap then gives ρ ↦ |+⟩⟨+|·tr ρ (K1). That map
lies outside 𝒞(C), and corollary 6 fails. Entrywise nonnegativity and `OnesNormal` survive, because |+⟩ has
nonnegative amplitudes and overlaps 1 (K2). The same swap with the mixed prior gives I/2 (K3). Complex hidden
amplitudes give phases: a hidden |−⟩ with CNOT gives Ad Z (C1; §4). So 𝒞(C) needs κ1 in its mixed reading, while
`NonnegBounded` needs only nonnegative hidden amplitudes.

**Corollaries [W].**
1. `NonnegBounded` (FrozenSourcing.lean:65) holds for every classical enlargement. This extends
   `obsTheory_nonnegBounded` (:84), which is stated at finite carriers.
2. Every available effect K†K is diagonal, so no non-configuration test, sharp or unsharp, is available. (a) fails.
3. A one-outcome conj(V) in 𝒞(C) has a rank-one Choi matrix, so V ∝ P for a single partial permutation (the order
   argument of MC2 §2.1). At level one (`Fin 2 × Fin 1`) there are six nonzero rays. `hmem` of
   `countable_not_pairFlowSourced` (PairFlowEquivalence.lean:218) quantifies over every V with conj V available, so the
   theorem applies with a finite D, although CR's P1 fails (confirmed by the review).
4. With N = Σ_P w_P P†P = I, the decomposition gives Σ_P √w_P (√w_P P)†1 = 1, so 1 lies in the span of the Kraus
   images and the map is `OnesNormal` (InstrumentRealization.lean:172) after splitting (MC1 T2). No deterministic Ad Z,
   Ad S or |−⟩ is available. (b) fails.
5. 𝒞(C) is finitely generated, hence closed [L: finitely generated convex cones are closed; confirmed by the review]. Every channel-metric limit
   of available maps stays in it. Limit closure and almost-sure termination over a classical enlargement reach neither
   (a) nor (b). Under this lemma the obstruction does not depend on countability.
6. With configuration preparations, every reachable visible state is diagonal, because partial permutations preserve
   diagonality. (c) is not reached: the classical register family is the Σ0 countermodel of LG §4.2.

**Exact checks [EC] (`probe/enlarge.py`, A1–A7).**
- A1: all 720 bijections of {0,1} × {0,1,2} at every hidden point, on all four matrix units. Ad_U followed by the
  partial trace agrees with the predicted Kraus form. The two code paths share nothing but the bijection table.
- A2–A4: every induced Kraus operator is a 0/1 partial permutation, every effect is diagonal, and nonnegativity is
  preserved.
- A5: six distinct nonzero Kraus shapes occur, the six nonzero partial permutations of `Fin 2`.
- A6: two-step protocols with readout and feed-forward keep partial-permutation Kraus operators.
- A7: under a nonuniform prior the map is Σ_P w_P Ad_P over finitely many P and is trace preserving.

**The continuum is in the weights, not the extreme points.** An enlargement makes uncountably many maps available,
because the weights w_P range over a continuum (B1). Unitary channels are extreme points of the channel set. The
unitary channels in 𝒞(C) are the Ad_P with P a permutation, finitely many. The A1 requirement (a) is a continuum of
non-monomial extreme points (unitary conjugations). A classical enlargement supplies a continuum of convex weights over a
fixed finite set of extreme rays.

***

## 3. Node N3: continuous couplings, continuous time and observer settings

**B1, a real coupling [EC].** T_θ(v, h) = (v ⊕ [h < θ], h) with h uniform on [0, 1) gives (1 − θ) id + θ Ad X. Distinct θ
give distinct maps (B1c). The Choi rank is 2 for 0 < θ < 1 and 1 only at θ ∈ {0, 1} (B1b). H:52's "real coupling"
therefore supplies a continuum of mixtures and two unitary channels.

**B2, a continuous-time flow with a process at every time [EC].**
- Setup: S = [0, 2), the visible bit v = ⌊x⌋, the hidden coordinate h = x − v, φ_t(x) = x + t mod 2, prior density
  f(h) = (π/2) sin(πh) for both visible starts (B2a).
- The flip probability is exactly sin²(πt/2) on [0, 2] (B2b). That is the rooted flip probability of the layer flow
  Ad R_x(πt) (B2c).
- The final hidden point (h + t) mod 1 does not depend on v, so the Kraus operators are I and X. The realized map is
  Φ_t = (1 − p_t) id + p_t Ad X.
- It differs from Ad R_x(πt) off the diagonal: from |0⟩⟨0| the layer flow gives the coherence i sin(πt)/2 and Φ_t gives
  0 (B2d). Φ_{1/2} preserves nonnegativity on every matrix unit; Ad R_x(π/2) does not (B2e).
- The visible family is not a semigroup: Φ_{1/2}∘Φ_{1/2} ≠ Φ_1 (B2f), as indivisibility requires.

*Pressure test of the favourable reading.* Here every t has an implementing substratum process, which is the
ingredient N1's HA3 says continuous time lacks in the finite case. The flow reproduces the layer flow's rooted law at
every t, exactly and supervenient. The operation it realizes is still the mixture, not Ad R_x(πt). The coherence term
that separates the two is invisible to the native configuration tests, which is the representability/availability
split (PG §3.12 [rec]) in continuous time. Verdict: continuous time with processes at every time supplies the rooted
law, not the layer flow. A different product identification C × X in Lemma 2's decomposition changes which coherences
survive, but not the cone.

**B3, observer settings (lead (ii)) [EC + W].**
- A setting s, s₂ ∈ [0, 1] (a continuous apparatus variable, or a free parameter outside the substratum) with the
  outcome "v = 0 and h < s, or v = 1 and h < s₂" gives the effect diag(s, s₂).
- All such effects commute (B3a). The sharp ones are the four configuration projectors (B3b). The X-basis projector is
  not among them (B3c).
- In general (§2, κ2): a setting only selects among bijections. Its cardinality and its origin, supervenient or free,
  do not enter the Kraus form.

*Verdict on (ii).* The observer's choice of test supplies a continuum of unsharp configuration tests and nothing
non-configuration. It cannot source the basis continuum (a): what the setting selects among is fixed by κ2 and κ4,
not by the freedom of the choice. A free setting is a non-supervenient context, so under the pointwise model and
κ1–κ4, non-supervenience of a context does no work. CR's P2 allows an arbitrary assignment f(π, c); reading an
arbitrary f as a change of identification (κ3) rather than a context is [W].

***

## 4. Node N4: which premise carries the obstruction (drop-one, [EC])

| premise dropped | result | check | status of the escape |
|---|---|---|---|
| κ0 finiteness of S (CR's P1), discrete time | conclusion survives | §2, B1, B2 | not an escape |
| κ1 distribution priors | hidden prior \|−⟩ with CNOT v→h gives Ad Z exactly; nonnegativity broken | C1a, C1b; the distribution prior gives dephasing (C1c); \|+⟩ gives the identity (C1d) | a non-distribution hidden state is a coherent preparation, against Main.md:60's prior; with ⟨1\|ψ⟩ = 0 it is the non-`OnesNormal` preparation of MC1 §4 2(ii) [UP] |
| κ2 bijections of configurations | a non-permutation process (Hadamard) sends a matrix unit to a matrix with a negative entry | C2 | a non-classical process, against Lemma 3's form (Main.md:56) [UP] |
| κ3 the G3 identification | identification through a fixed basis change W = H makes native X act as Ad Z | C3 | barred by G3 (LG §2.4; Γ(Q3) control) |
| κ4 configuration readout | Y-basis Lüders branch has complex off-diagonal Kraus entries | C4; MC1 T1 | TU, the posited test continuum [UP] |

**Verdict.** For classical candidates (the pointwise model with κ1–κ4), the operation-side obstruction is carried by
κ1–κ4, not by the finiteness or countability of the substratum: no size, time model, coupling, context or limit leaves
𝒞(C). The table shows that each dropped κ leaves 𝒞(C), not that any reaches A1:
- dropping κ1 (a hidden |−⟩) gives (b) only;
- dropping κ4 gives (a) only, and only with a continuum of test bases (MC1 T1, T2);
- dropping κ3 is barred by G3; dropping κ2 by a fixed gate does not reach A1 either.

For non-classical candidates, CR's finiteness and supervenience premises stay load-bearing for (a): `fixedGateTheory`
drops κ2 and is still not QM (`fixedGateTheory_not_qm` DiscreteCompletion.lean:1948).

***

## 5. Node N5: the global antiunitary (lead (iv)) [EC D1–D6; W]

- D1: transposition on descriptions has Choi matrix SWAP, with eigenvalue −1. It is positive and not completely
  positive, so it is not an available operation. GR.md:204 uses it to relate completions, not as an operation within
  one.
- D2: τ∘Ad_P∘τ = Ad_P for all 24 pair permutations.
- D3: Σ conj(K)†1 = conj(Σ K†1) for a generic symbolic Kraus list. Time reversal maps `OnesNormal` families to
  `OnesNormal` families.
- D4: conj(U) fixes the all-ones ray whenever U does.
- D5: complex conjugation and the 24 pair permutations generate 48 antiunitary-or-unitary elements, and every unitary
  part is a permutation.
- D6: time reversal of the heralded phase gadget conjugates its `OnesNormal` sum.

**Verdict.** Composing the global antiunitary with native or TU operations yields no deterministic phase. (b) is not
sourced. This confirms MC2 §3's row with exact instances. The hidden predictive memory (Main.md:582) is classical
(MC1 row 11 [rec]) and falls under §2.

***

## 6. Node N6: reconstruction principles at the observer level (lead (iii)) [W, L]

| principle [L] | would supply | closest OI statement | derivable under κ1–κ4? |
|---|---|---|---|
| purification with uniqueness (Chiribella–D'Ariano–Perinotti 2011) | (a), (b), and a self-dual cone toward (c) | Main.md:600–602: substratum-level existence and the canonical predictive quotient | no. Under §2 corollary 6 every reachable state is diagonal; a pure diagonal joint state is a point mass with a pure marginal, so no mixed visible state has an operational purification. The operational form needs κ1 or κ4 |
| continuous reversibility (Hardy 2001; Masanes–Müller 2011) | (a); (b) once pure states form a connected set | none; layer flows only as representation (GR.md:272) | no: the pure states of a diagonal theory form a finite set, and continuous reversibility needs a connected set of pure states |
| local tomography + subspace axiom (Masanes–Müller) | with continuous reversibility, all of finite QM | H-CAR / LT (LG §2.2) | no: the subspace and reversibility clauses need non-diagonal states, so κ1 or κ4 |

**Verdict.** Purification is the closest to what OI states. None of the three is derivable under κ1–κ4. Each needs a
non-classical primitive kind, which confirms MC2 §3 ("classical theory has no purification").

***

## 7. The form of the missing component, as revised

PLAN's first clause, "it is non-supervenient, or it enlarges the substratum", is replaced by a conjunction of two
necessary conditions, neither claimed sufficient (§A.34):

> - It contains a primitive of non-classical kind (κ1 read as mixed priors, κ2, or κ4 dropped; κ3 is barred by G3),
>   and, for (a) at A1, it is non-supervenient or rests on an infinite substratum of non-classical kind (CR).
>   Enlarging a classical substratum's cardinality or time model adds nothing: in the pointwise hidden model, with
>   measurable dynamics, every available outcome map lies in the finitely generated cone of nonnegative combinations
>   of Ad_P, P a partial permutation (missing-component node `mc3`, §2).

The other clauses stand:
- a non-`OnesNormal` primitive for (b), which with κ1 dropped is a hidden or prepared |−⟩;
- an uncountable non-monomial family for (a);
- O-B through the G3 identification and multi-token clauses.

***

## 8. Controls and the independent prediction

No new candidate survives this node. The remaining class, primitives of non-classical kind, is the posit class of
MC1 §4 and MC2 §4. Controls fixed in advance for any candidate from that class:
1. `permTheory_not_qm` (SubstratumInterfaceAudit.lean:716) and `substratum_residual` (StructuralClosure.lean:383) hold
   with the addition removed. `NonnegBounded` holds for the native class (`obsTheory_nonnegBounded`), and by §2 for
   every classical enlargement.
2. K_B, K(Z_F) and Γ(Q3) are excluded through the G3 identification and multi-token clauses (LG §4).
3. The rooted law (`finiteRootedRealizable_iff_pper` RootedClassificationAllTime.lean:192) and M1 hold on retained
   protocols.
4. No E0 positing: the flow, gate or phase is not posited. Representability does not stand in for availability (B2 is
   the continuous-time must-fail instance).
5. `fixedGateTheory_not_qm` (DiscreteCompletion.lean:1948) stays non-QM under any completion rule (MC2 §2.2).
6. Must-fail: in the pointwise hidden model, no classical enlargement, setting, coupling, time model or limit reaches (a) or (b) (§2–§3).
7. The candidate names which of κ1–κ4 it gives up.

**Independent prediction (G6): none found.** §2 predicts nothing beyond the native theory, because it is a ceiling.
A source of non-classical kind has to bring its own prediction, and none is proposed.

***

## 9. Hidden-assumption watch

| # | assumption | where | finding |
|---|---|---|---|
| HA-E1 | enlarging the substratum is an escape from the operation-side obstruction | PLAN form clause 1; N1 §2.1 consequence; MC2 §4 item 5 | **exposed**: under κ1–κ4 an enlargement escapes CR and lands in 𝒞(C) (§2) |
| HA-E2 | the obstruction to exact QM is countability ("exact QM needs an added continuum, such as a real duration or a real coupling") | H:46–52; N1 §2.1 | **partly recorded, scoped**: H:40 already lists positivity (I1) as a separate invariant beside countability (I4). Added: for classical sources in the pointwise model, I1 already blocks at every cardinality, and a real duration or coupling in a classical substratum gives convex weights (B1, B2). For non-classical sources countability stays load-bearing (`fixedGateTheory_not_qm`) |
| HA-E3 | continuous time fails only for lack of an implementing process at non-integer times | N1 HA3 | **elaborated**: with a continuum substratum every time has a process, and the realized operation is still a mixture (B2) |
| HA-E4 | a free (non-supervenient) choice of test could supply a basis continuum | lead (ii) | **refuted**: settings of any cardinality and origin select among configuration tests (B3, κ2, κ4) |
| HA-E5 | the antiunitary orientation could supply a phase | lead (iv) | **confirming** (MC2 §3): not CP; preserves `OnesNormal` (D1–D6) |

Assumption-watch markers:
- **AW-MC3-1.** In the pointwise hidden model (κ1 mixed) with measurable dynamics and κ2–κ4, available outcome maps lie
  in the finitely generated cone 𝒞(C) at every substratum cardinality, time model, coupling and setting, and under
  limits. A claimed source names the κ it drops, or the modelling premise (a vector-valued hidden prior leaves 𝒞(C):
  review K1).
- **AW-MC3-2.** CR's P2 counts contexts. In the pointwise model, contexts of any cardinality or origin do not change
  the Kraus kind. That an arbitrary assignment f in P2 amounts to a change of identification is [W].
- **AW-MC3-3.** A rooted-law match at every time (B2) is not availability. Records citing continuous-time
  realizability should say which coherence terms the realization carries.

***

## 10. Not verified

- The cone lemma is [W], in the pointwise model, which is a definition for infinite X (§2). Measurability is assumed
  (bimeasurable bijections, measurable settings). The reduction to `Realized permClass` and
  `preservesNonneg_of_realized` is written, not compiled, and the kernel's `Substratum` has no infinite-carrier form.
- The exhaustive check A1–A7 covers |C| = 2 and |X| = 3 only. The continuum instances B1–B3 are single families.
- Closedness of 𝒞(C) is cited [L], not formalized. Approximate Poincaré recurrence and the irrational-rotation example
  are [L].
- The E3 reading that excludes a continuum in the boundary layer is taken from Substratum.md:92 [rec].
- §6 is [W]/[L]. The reconstruction theorems were not re-derived.
- [rec] rows (H, LG, MC1, MC2, PG) were taken as recorded.
- The first run of `enlarge.py` failed B2e. Its witness input was the all-ones matrix, which every R_x fixes. The check
  now uses the matrix units, which is what `PreservesNonneg` quantifies over. Both final runs are byte-identical.

***

## 11. Files (`probe/`)

| file | role |
|---|---|
| `enlarge.py` | blocks A (exhaustive finite core), B (continuum couplings, flow, settings), C (drop-one), D (antiunitary); 32 checks; SymPy 1.14.0, Python 3.13.16, `-I -B` |
| `enlarge.run1.out`, `enlarge.run2.out` | 32 PASS, 0 FAIL; byte-identical |
| `SHA256SUMS` | digests of the three files |
| `review/rev_mc3.py`, `review/rev_mc3.out`, `review/SHA256SUMS` | independent review, copied unchanged: 17 PASS, run once (A1–A7, K1–K3, B1–B3, C1–C3, D1) |

***

## 12. Productivity verdict

**Gem: yes, narrow.** Facts strictly stronger than "no OI source is known for (a)–(c)":
1. In the pointwise hidden model (κ1 mixed) with measurable dynamics and κ2–κ4, every classical substratum, at any
   cardinality and with continuous time, real couplings, settings of any cardinality or origin, and channel limits,
   makes available only maps in the finitely generated cone 𝒞(C). This constrains the form: the classical-enlargement
   escape in CR's conclusion is empty (§7).
2. For classical candidates the load-bearing premises are κ1–κ4, and each dropped κ leaves 𝒞(C) by an exact model;
   none reaches A1 alone. For non-classical candidates CR's premises stay load-bearing for (a)
   (`fixedGateTheory_not_qm`). This exposes HA-E1 and scopes HA-E2, which H:40 partly records.
3. A continuous-time substratum with a process at every time reproduces the layer flow's rooted law exactly and still
   realizes only the mixture (B2).
4. Leads (ii) and (iv) are closed with exact instances. Lead (iii) is not derivable under κ1–κ4.

**Classification: ELABORATING overall, with one NEW (narrow) item:** the classical-enlargement escape in CR's
conclusion is empty under κ1 (mixed) to κ4, the pointwise model and measurability. The cone reduction extends
`obsTheory_eq_permTheory`, `obs_availExt_le_coherentLift` and `preservesNonneg_of_realized` to arbitrary hidden
carriers and fills, for classical hidden dynamics, the disclaimer in the header of `stochasticChannel_kraus_monomial`
(LiftSource.lean:41–43, :251). B2 is ELABORATING (HA-E3). (iii) and (iv) are CONFIRMING (MC2 §3). G6: none. Sources
for (a), (b) and (c) remain open.

***

## Review outcome

Review: `probe/review/` (`rev_mc3.py`, 17 PASS, replayed byte-identical, with its output and `SHA256SUMS`, copied unchanged from the
reviewer's working copy). The corrections are applied in place above. The pre-review text is not kept here; its
sha256 is `4dc96831c0aa246a1428c9f16a59112fb0b38f06b62c3588c436c4b2c9a8a9f8`.

| item | verdict | applied as |
|---|---|---|
| cone lemma | CONFIRMED under the pointwise model | modelling premise and measurability stated (§2); for infinite X the pointwise integral is a definition, not a consequence of κ3; KvN counter-instance K1–K3 and complex amplitudes C1 added; the cone needs κ1 mixed, `NonnegBounded` only nonnegative amplitudes (F1) |
| exact checks A1–A7, B1–B3 | CONFIRMED | — |
| "6 rays" at level one; closedness of 𝒞(C) | CONFIRMED | cited as confirmed (§2 corollaries 3, 5) |
| drop-one | CONFIRMED that each dropped κ escapes; CORRECTED on what an escape means | each escape leaves 𝒞(C), none reaches A1 alone; κ1–κ4 carry the obstruction for classical candidates only; CR stays load-bearing for non-classical ones (`fixedGateTheory_not_qm`) (F6) |
| antiunitary | CONFIRMED | — |
| reconstruction principles | CONFIRMED [W, L] | — |
| PLAN revision | CORRECTED | conjunctive necessary form, pointwise model named; AW-MC3-1 restated; AW-MC3-2's identification reading marked [W] (F7) |
| classification | CORRECTED | ELABORATING overall with one NEW (narrow) item; finite-substratum kernel results and H:40 cited (F8) |
| base | CORRECTED | `main` = `809fa9d6`; kernel and papers identical to `df9e601e` |
