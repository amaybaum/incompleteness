# NONDIO-M1: the non-DIO obstruction on uncountable configuration carriers (research record)

**WIP / UNVERIFIED. Paper-only research. It awaits an independent non-author review.** This
record walks the nodes of `PLAN.md`, which was committed before it at `24042c78`. It runs no
computation. It edits no manuscript, Lean module, reviewed record or Issue. It adopts no premise,
changes no status and strengthens no manuscript or kernel theorem. No merge is authorized. The pins,
formulations (F-at), (F-C\*) and (F-W\*), and assumptions are those of `PLAN.md` §1, §3 and §4.
Lemma, corollary and node names without a prefix are this record's. Those prefixed "NN" are
NATIVE-NONDIO's, at `ab830621` (`INVESTIGATION.md`).

Revision r2 answers the independent review of `24ac0874` (#1547 c.7077044631, verdict REVISE).
R1–R4 narrow §0 and the affected nodes to what is proved, and n1–n9 are applied as nits. The
headline changes in r2 are these:
- (F-at): the excluded set of maps is unchanged; it is described as a class of normal maps,
  since σ-D forces normality (Lemma NRM), and r1's "normal or not" covered no further map.
- Type-I diffuse W\*: withdrawn from the excluded class, since its reading SS-D is definitional;
  reported as DIO definitional and MIO untypable.
- R: restricted to NAT maps nonsingular for μ (singular case M1-c).
- (F-C\*): MIO stated in the proved direction only.

The delta check of `c39c5266` (c.7077116712, CONFIRMED WITH NITS) is answered in r2.1, which
moves this narration out of §0 and §3 and applies its nits m1, m2 and the n3
follow-up. `PLAN.md` is unchanged.

**Labels.**
- **ESTABLISHED**: proved on paper here (layer X), or cited at its source's standing: (L) a
  literature theorem, (R) a corpus record. "Established" means established within this record,
  not in the §A.46 sense.
- **ASSUMED**: a named premise.
- **MISSING**: a gap, stated with the node where the branch stopped.
- (N) native, (I) imported.

## 0. Outcome

**EXTENDS in (F-at), (F-C\*) and R, with the classes stated below. In the type-I diffuse W\*
formulation the question has no non-definitional typing** (DIO definitional, MIO untypable; NE
is the new content there). The countable proof does not transfer verbatim. This is a negative
result (an obstruction to native coherence), conditional throughout on TB, DEC, KIN-B (or KIN-𝒟),
LIN and NAT. NAT is a named premise that is not adopted (NN M4). Coherence is relative to the
configuration algebra 𝒟, and encoded carriers in the sense of T-SUB′ (iv) are outside every
statement (NN §0).

**The exact class excluded.** No NAT operation on a total configuration set of any cardinality
has a positive extension, satisfying TB, that is non-DIO-type, in each of the following
formulations; where MIO-type is typed, none is non-MIO-type either:

| Formulation | Algebras | Determinism hypothesis (configuration level) | Maps | States | DIO | MIO |
|---|---|---|---|---|---|---|
| (F-at) | B(ℓ²(X)) ⊇ ℓ^∞(X), X of any cardinality | each configuration input has an output configuration law that is zero or a point mass, σ-additively (σ-D); equivalently, NN point determinism of a normal map (NRM-D) | positive (σ-D forces normality, NRM) | all, normal or not | yes (DET-at) | yes (DET-at) |
| (F-C\*) | unital ℬ ⊇ C(X), X compact, with a faithful conditional expectation E; for example the quasi-local algebra of A^Λ | the configuration states ε_x = δ_x∘E have zero or point-mass output laws | positive | all (no normality notion) | yes (DET-C\*) | yes if every image point has unique extension (DET-C\* (iv)); this holds for the quasi-local diagonal (UE). If unique extension fails at some y, the constant action onto y has a DIO-type, non-MIO-type positive extension (CX-2) |
| (F-W\*), R | the trace closure R of the quasi-local algebra, ⊇ L^∞(A^Λ, μ_unif), with its trace-preserving E; NAT maps nonsingular for μ (singular case: M1-c) | the configuration law E(Φ\*(q)) of every output event q is an event (E-D) | positive; normal for MIO | all | yes (DET-R) | yes for normal maps on this pair (MIO-R) |

**Type-I diffuse W\* (not part of the excluded class).** In B(L²(X, μ)), μ diffuse, no
conditional expectation onto L^∞ is faithful or normal, and no normal state is diagonal (Lemma
NE). The only event reading available there, SS-D, is equivalent to Φ\* sending event
projections to event projections, the projection case of DIO-type (§3). So DIO-type is
definitional and MIO-type cannot be typed. NAT delivers SS-D only through the law-level reading,
which is itself definitional (§6).

- **Reductions and record laws.** Corollary RED-∞ (§5) shows that the visible reductions are
  DIO-type for every hidden state: in (F-C\*) for any visible carrier, and in (F-at) and R when
  the visible carrier is finite (FIN-V, `Main:46`). Corollary IDLE-∞ shows that native record
  laws depend only on the configuration law, for every state, in (F-at), (F-C\*) and R (in
  type-I diffuse W\* only under the definitional SS-D). This includes diffuse laws, such
  as Bernoulli and Gibbs measures on A^Λ, and coherent states with a diffuse configuration law.
  In (F-at) a configuration law is a finitely additive state of ℓ^∞(X), and a Bernoulli or Gibbs
  measure fixes the record law there when D_o and f_o are Borel, as they are for a CA.
- **The counterexamples.** They mark the boundary of the class; none is a native channel.
  - **CX-1′.** On any infinite carrier, countable or not, a non-normal positive map with
    Φ\*(1) = 1 can have every p(y | x) = 0 and p(Y | x) = 1, and still detect coherence. It
    fails σ-additivity and nothing else.
  - **CX-1.** A variant whose branch weight is ½ (it also fails finite-level determinism).
  - **CX-1b.** On an uncountable carrier, and using the axiom of choice, a non-normal positive
    map whose output law is deterministic on every Borel event is still non-DIO-type relative to
    ℓ^∞.
  - **CX-2.** Where unique extension fails, a DIO-type map can be non-MIO-type.

  CX-1′, CX-1 and CX-1b violate σ-additivity, which NAT's configuration-valued outputs deliver
  (§6).
- **What the countable proof used and this record replaces** (N1, §2).
  - Normality of the extension map entered NN DET exactly as σ-additivity of the output
    configuration laws on configuration inputs: for positive maps on atomic carriers the two are
    equivalent (Lemma NRM). This is assumption-watch marker AW-2.
  - Matrix entries ⟨x|·|x⟩ are replaced by a faithful conditional expectation.
  - Countability of X is not used anywhere.

**MISSING.**
- MIO in type-I diffuse W\* cannot be typed there. The creation question for diffuse laws is
  typed in (F-C\*) or in R instead.
- Uniqueness of extension at free ultrafilters, for non-normal maps with non-σ-additive
  deterministic laws on uncountable carriers. This is not needed for the native class.
- W\* formulations over a reference measure that a native dynamics renders singular (M1-c).
- M2 of NATIVE-NONDIO (a countably infinite visible carrier with a non-normal hidden state, in
  (F-at)) is **not settled** here (§5).
- NN M3 (nonlinear state assignments) and NN M4 (the nativeness criterion) are unchanged.

**Productivity (`PLAN.md` §5): gem.** The output class is ELABORATING, with one NEW
assumption-watch marker (AW-2) (§8).

## 1. Literature and sources

| Topic | Source | Use |
|---|---|---|
| Kadison's inequality | R. V. Kadison, Ann. of Math. 56, 494–503 (1952) | (L), used once (DET-C\*, general compact X): Ψ(a)² ≤ Ψ(a²) for a unital positive Ψ and self-adjoint a |
| Conditional expectations | J. Tomiyama, Proc. Japan Acad. 33, 608–612 (1957) | context: a norm-one projection onto a subalgebra is positive and bimodular. Here those properties are taken as the definition |
| Pure-state extension | R. V. Kadison, I. M. Singer, Amer. J. Math. 81, 383–400 (1959); A. Marcus, D. Spielman, N. Srivastava, Ann. of Math. 182, 327–350 (2015) | context only. Diffuse MASAs, and the free-ultrafilter remark of §4 (M1-b) |
| Cartan pairs, C\*-diagonals | J. Feldman, C. C. Moore, Trans. Amer. Math. Soc. 234 (1977); A. Kumjian, Canad. J. Math. 38 (1986); J. Renault, Irish Math. Soc. Bull. 61 (2008) | context: the setting of (F-C\*) and of R. No theorem is taken from them; UE and NE are proved here |
| Cellular automata | T. Ceccherini-Silberstein, M. Coornaert, *Cellular Automata and Groups* (2010); G. A. Hedlund, Math. Systems Theory 3, 320–375 (1969); D. Richardson, J. Comput. System Sci. 6 (1972) | (L), used in §6 only: the Curtis–Hedlund–Lyndon theorem on ℤ^d (a continuous shift-commuting map of A^{ℤ^d} is a CA), in the group form of Ceccherini-Silberstein–Coornaert. Hedlund (1969) is the one-dimensional case; Richardson (1972) treats injective d-dimensional CA. Context otherwise |
| Non-atomic measures | W. Sierpiński, Fund. Math. 3 (1922) | (L), used in NE: a non-atomic finite measure takes every intermediate value |
| Quasi-local algebras | O. Bratteli, D. W. Robinson, *Operator Algebras and Quantum Statistical Mechanics* 1 (1987) | context |

No source is claimed for Lemma P, Lemma NE, Lemma NRM, Lemma UE or the DET variants, all of which
are elementary. Lemma NRM (b) follows the proof given in the review (c.7077044631). Any novelty is relative to the corpus.

Corpus records read in full before the walk:
- NATIVE-NONDIO `PLAN.md` and `INVESTIGATION.md` at `ab830621`, and its three reviews (#1544
  c.7075473914, c.7075888975, c.7075922740);
- OPRES `NOTE.md` at `24702c1d` (Proposition D, Remark D′, Conjecture D″, U1′).

Manuscript sites read in context: `Main:42`–`60` (Definition; Lemmas 1–3; the status Remark,
including the adjoined deep factor), `Main:294` (§3.2, the reversible nearest-neighbour update),
`Main:328`–`338` (diagonal preservation; the measurable-hidden-carrier corollary), and the
`Main:131` scope sentence on the selected update on ℤ^d.

## 2. N1 (decisive): step audit of the countable proof

Each step of NN SHARP, DET, RED and IDLE is listed with what it uses. "Repl." names the argument
of this record that replaces the step.

| Step (NN) | Uses | (F-at), uncountable X | (F-C\*), (F-W\*) |
|---|---|---|---|
| S1 setting: trace-class maps on ℓ²(X), X countable | separability is never used; the predual is | holds for any cardinality: ℓ²(X) is non-separable and the trace class is unchanged | there is no predual containing configuration points; the Heisenberg form on ℬ is used (repl. §3) |
| S2 SHARP: 0 ≤ F_{o,y} ≤ Φ_o\*(1) ≤ 1 | positivity and TB | holds | holds for F = Φ_o\*(q), q an output event |
| S3 SHARP(D): Φ_o\*(M_g) = Σ_y g(y)F_{o,y}, σ-weakly | **normality of Φ_o\***, and singletons as events | holds for normal maps: a normal positive map is completely additive over index sets of any size. It **fails for non-normal maps** (CX-1′); normality is equivalent to σ-additivity on configuration inputs (NRM) | repl.: events (projections of 𝒟) and norm density of their span, with no normality (Lemma P, DET-C\*, DET-R) |
| S4 SHARP(D): the two-point entry argument | matrix entries | holds | repl.: a nonempty open set of points (SHARP-C\*) |
| S5 SHARP(M): Φ_o(Δρ) = Σ_x ρ_xx Φ_o(\|x⟩⟨x\|) | a trace-class input, so a countable diagonal support, and normality | holds for normal inputs. Diffuse laws are non-normal inputs, so MIO is shown in Heisenberg form (DET-at (ii)) | repl.: Heisenberg MIO, E_in Φ\* = E_in Φ\* E_out (DET-at, UE, MIO-R) |
| S6 DET (M) exclusion: Σ_y p ≤ 1 | TB on finite partial sums | holds for any positive map | holds |
| S7 DET: F\|x⟩ ∈ {0, \|x⟩} | 0 ≤ F ≤ 1 and diagonal entries in {0, 1} | holds (Lemma P, with Δ faithful) | repl.: Lemma P with a faithful E. In type-I diffuse W\* there is none (NE), and the sharp-support reading is definitional (§3) |
| S8 DET: Φ_o(\|x⟩⟨x\|) is rank one | normality | σ-D and Cauchy–Schwarz give the vector state (DET-at); σ-D forces normality of the map (NRM) | repl.: unique extension (UE) |
| S9 RED: the slice σ_ω on ℓ^∞(C_V × Z) | ω normal, or C_V finite | Z of any cardinality: normal ω for any C_V; any ω when C_V is finite (RED-∞) | (F-C\*): the minimal-tensor slice exists for any state and any visible carrier; (F-W\*): as in (F-at) |
| S10 RED MIO: \|v⟩⟨v\| ⊗ ω is a countable convex combination of configuration states | normality and countable support of ω | holds for normal diagonal ω. A diffuse (non-normal) diagonal ω is handled in Heisenberg form (RED-∞ (ii)) | the same |
| S11 RED: the Theorem C(b) bound | a CP extension; the visible system finite | holds: Φ^V is a CP map on M_{C_V} | holds |
| S12 IDLE | Φ_o\*(1) ∈ 𝒟 | holds for every state | holds for every state (IDLE-∞) |
| S13 protocols are compositions | the Heisenberg conclusion composes | holds | holds |
| NN N5: measurable carriers "Missing; branch stopped" | — | — | repl.: (F-C\*) gives point states and an extension class; E-D gives a non-definitional event reading in R; in type-I diffuse W\* NN N5's verdict stands, sharpened by NE (§3) |

**Verdict N1.** Countability of X is used nowhere. Normality is used in S3, S5, S8 and S10. In S3
and S8 it enters exactly as σ-additivity of the output configuration laws, which for positive
maps on atomic carriers is equivalent to normality of the map (NRM): AW-2 (§4, CX-1′). Matrix
entries are used in S4 and S7; a faithful conditional expectation replaces them where one exists.
The slice in S9 needs FIN-V, or normal ω, outside (F-C\*).

## 3. N2: what "deterministic action" means on each carrier

The circularity test (`PLAN.md` §6, N2) admits a definition only if it constrains Φ on states
whose configuration law is sharp, and does not already fix Φ on states whose law is not sharp.

In every formulation, (Φ_o)_{o∈O}, with O countable, is a family of positive linear Heisenberg
maps Φ_o\*: ℬ_out → ℬ_in satisfying TB: Σ_{o∈O′} Φ_o\*(1) ≤ 1 for every finite O′ ⊆ O. A
configuration-valued record is part of the output carrier (NAT: records are configurations), so
an uncountable record range needs no uncountable O.

- **(F-at).**
  - Point action: p(o, y | x) := ⟨x|Φ_o\*(|y⟩⟨y|)|x⟩, as in NN.
  - Event action: p(o, B | x) := ⟨x|Φ_o\*(P_B)|x⟩, for B ⊆ Y.
  - **σ-D**: for each o and x, B ↦ p(o, B | x) restricted to the Borel sets is a σ-additive
    measure that is 0 or a point mass δ_{f_o(x)}, where Y is standard Borel (A^Λ with Λ countable
    is compact metrizable).

  This hypothesis concerns configuration inputs |x⟩⟨x| only, so it passes the test. Given
  positivity and TB, σ-D is equivalent to NN point determinism together with normality of the
  map (NRM-D, §4).
- **(F-C\*).**
  - E: ℬ → 𝒟 = C(X) is a faithful conditional expectation: positive, unital, 𝒟-bimodular, the
    identity on 𝒟, and with E(b\*b) = 0 implying b = 0.
  - The configuration state is ε_x := δ_x∘E.
  - Point action: p_o(· | x) is the Radon measure of ε_x∘Φ_o\* on 𝒟_out. Deterministic means
    p_o(· | x) ∈ {0} ∪ {δ_y : y ∈ X_out}. This hypothesis concerns ε_x only, so it passes the test.
  - On the quasi-local algebra, ε_x is the **only** state extending δ_x (UE, §4), so the
    definition is forced there and is not a convention.
- **(F-W\*), R.**
  - **E-D**: for every projection q ∈ 𝒟_out, E_in(Φ_o\*(q)) is a projection of 𝒟_in.
  - Equivalently, for every normal diagonal state ρ = ρ∘E concentrated on the event P := E(Φ\*(q)),
    the output is in q surely, and for every one concentrated on 1 − P, never. This concerns
    sharp-event diagonal inputs only, so it passes the test.
- **(F-W\*), B(L²(μ)), μ diffuse.** There is no faithful conditional expectation (NE).
  - **SS-D**: for every output event q there is an input event P such that every normal state ρ
    with ρ(P) = 1 has ρ(Φ_o\*(q)) = 1, and every one with ρ(P) = 0 has ρ(Φ_o\*(q)) = 0.
  - SS-D is **definitional**. By Lemma P it gives Φ_o\*(q) = P; conversely Φ_o\*(q) = P, an event
    projection, gives SS-D at once. So SS-D says exactly that Φ_o\* sends event projections to
    event projections, the projection case of DIO-type. It constrains Φ\*(q) on all of ran P, and
    by NE every normal state concentrated on P is coherent.
  - What is proved about weaker readings is this: no formulation on normal
    diagonal states exists (NE), and no conditional expectation is faithful, so Corollary P1 is
    unavailable. Whether some other non-definitional event reading exists in this formulation
    is not settled here.
- **Law-level reading** (the output law of every state is the push-forward of its input law).
  This is DIO-type by inspection, so it is **definitional** (NN N5) and is not used.

**Verdict N2.** Three formulations have a non-definitional determinism hypothesis: σ-D in
(F-at), point determinism on ε_x in (F-C\*), and E-D in R. In type-I diffuse W\* the available
reading SS-D is definitional, and NN N5's verdict stands there, sharpened by NE. NN N5's
"Missing M1" stop was caused by the absence of point states in L^∞. It is removed by (F-C\*),
where points are states, and by E-D, where events replace points through a faithful expectation.

## 4. N3: rigidity

**Lemma P (compression rigidity; ESTABLISHED, X).** Let ℬ be a C\*-algebra, P a projection and
0 ≤ F ≤ 1 in ℬ. If P(1 − F)P = 0 and (1 − P)F(1 − P) = 0, then F = P.

*Proof.* ‖(1 − F)^{1/2}P‖² = ‖P(1 − F)P‖ = 0, so (1 − F)P = 0. Likewise F(1 − P) = 0. So
F = FP + F(1 − P) = P. ∎

*Corollary P1.* If E: ℬ → 𝒟 is a faithful conditional expectation, 0 ≤ F ≤ 1 (in the uses below
TB supplies this, since 0 ≤ Φ_o\*(q) ≤ Φ_o\*(1) ≤ 1), and E(F) = P is a projection in 𝒟, then
F = P. Indeed E(P(1 − F)P) = P(1 − P)P = 0, and E((1 − P)F(1 − P)) = 0. Both elements
are positive, and E is faithful.

Instances of a faithful E:
- the diagonal compression Δ on B(ℓ²(X)), for X of any cardinality (⟨x|b\*b|x⟩ = ‖b|x⟩‖²);
- the product expectation on the quasi-local algebra (τ∘E = τ, with τ the faithful trace);
- the trace-preserving expectation of R.

**Lemma NE (no faithful expectation on a diffuse type-I carrier; ESTABLISHED, X with Sierpiński
(L)).** Let μ be a diffuse probability on a standard Borel X, and let E: B(L²(X, μ)) →
L^∞(X, μ) be any positive, unital, L^∞-bimodular map that is the identity on L^∞. Then E
vanishes on every finite-rank operator. Hence E is neither faithful nor normal, and no normal
state ρ satisfies ρ = ρ∘E.

*Proof.* Let A = |ξ⟩⟨ξ| with ‖ξ‖ = 1. The measure |ξ|²μ is non-atomic, so for each N it splits
into N events P_1, …, P_N of mass 1/N (Sierpiński). Then:
- E(A)P_i = P_i E(A) P_i = E(P_i A P_i);
- P_i A P_i = |P_iξ⟩⟨P_iξ| ≤ (1/N) P_i;
- so E(A) = Σ_i E(A)P_i ≤ (1/N)·1.

Hence E(A) = 0. Polarization extends this to all finite-rank operators. A normal map that is zero
on the σ-weakly dense finite-rank operators is zero, which contradicts E(1) = 1. A normal state
vanishing on the finite-rank operators is zero. ∎

**Lemma NRM (σ-additivity on configuration inputs is normality; ESTABLISHED, X; (b) follows
review c.7077044631).** Let X and Y be sets of any cardinality, Φ\*: B(ℓ²(Y)) → B(ℓ²(X))
positive, and ψ_x := ⟨x|Φ\*(·)|x⟩.
- (a) ψ_x is normal if and only if Σ_{y∈Y} ψ_x(P_y) = ψ_x(1).
- (b) Φ\* is normal if and only if every ψ_x is normal.

*Proof.*
- (a) "Only if" is complete additivity of a normal functional. For "if", put
  Q_F := Σ_{y∈F} P_y for finite F ⊆ Y, so ψ_x(1 − Q_F) → 0 along F. Cauchy–Schwarz gives
  |ψ_x(a) − ψ_x(Q_F a Q_F)| ≤ 2‖a‖ ψ_x(1)^{1/2} ψ_x(1 − Q_F)^{1/2}. Each a ↦ ψ_x(Q_F a Q_F) is
  normal, since Q_F has finite rank. A norm limit of normal functionals is normal.
- (b) "Only if" is immediate. For "if":
  - Take a finitely supported ξ = Σ_{x∈G} c_x|x⟩ with |G| = n, and a ≥ 0. Since Φ\*(a) ≥ 0,
    Cauchy–Schwarz on its matrix entries gives ⟨ξ|Φ\*(a)|ξ⟩ ≤ n Σ_x |c_x|² ψ_x(a). So ω_ξ∘Φ\*
    is dominated by a normal positive functional, and is normal.
  - For general ξ, ω_ξ∘Φ\* is a norm limit of such functionals, because Φ\* is bounded.
  - A positive map whose vector-state compositions are all normal is normal. ∎

*Corollary NRM-D (ESTABLISHED, X).* For positive Φ_o\* with TB, σ-D holds if and only if NN's
point determinism (every p(o, y | x) ∈ {0, 1}) holds and Φ_o\* is normal.
- If σ-D holds, each ψ_x is 0 or the vector state at f_o(x) (DET-at's proof), so it is normal,
  and (b) makes Φ_o\* normal; point determinism is read off.
- If Φ_o\* is normal and point-deterministic, complete additivity gives
  p(o, B | x) = Σ_{y∈B} p(o, y | x). TB allows at most one y with value 1, so the law is 0 or a
  point mass, σ-additively.

**Theorem DET-at (ESTABLISHED, X; (I) on KIN-B, LIN, TB).** Let X be a set of any cardinality and
Y a standard Borel space (or any set, with all subsets as events). Let Φ_o\* be positive, satisfy
TB, and satisfy σ-D with maps f_o: D_o → Y. By NRM-D, Φ_o\* is then normal. Then:
- (i) Φ_o\*(P_C) = P_{f_o^{-1}(C)} for **every** C ⊆ Y. So Φ_o\*(ℓ^∞(Y)) ⊆ ℓ^∞(X), and every
  branch is DIO-type.
- (ii) Δ_in Φ_o\* = Δ_in Φ_o\* Δ_out: every branch is MIO-type in Heisenberg form, and so on
  every input state, normal or not.

*Proof.*
- For x ∈ D_o, the functional ψ_x := ⟨x|Φ_o\*(·)|x⟩ is positive, with ψ_x(1) = 1 = ψ_x(P_{f_o(x)}).
  Here P_Y = 1, and singletons are Borel.
- Cauchy–Schwarz gives ψ_x((1 − P_{f_o(x)})a) = 0 = ψ_x(a(1 − P_{f_o(x)})), so
  ψ_x(a) = ⟨f_o(x)|a|f_o(x)⟩.
- For x ∉ D_o, ψ_x(1) = 0, so ψ_x = 0.
- (i) Hence Δ(Φ_o\*(P_C)) = P_{f_o^{-1}C}, a projection. Corollary P1 with E = Δ gives
  (i) on projections. ℓ^∞(Y) is the norm closure of the span of its projections, and Φ_o\* is
  bounded.
- (ii) ψ_x(a) = ψ_x(Δa). ∎

DET-at is NN DET for any cardinality: by NRM-D, its hypothesis is NN's point determinism of a
normal map.

**Counterexample CX-1′ (σ-additivity alone is needed; ESTABLISHED, X; from review
c.7077044631, n1).** Let Y be any infinite set, countable allowed, and X = {0, 1}. Take two
distinct free ultrafilters u₁, u₂ on Y and a set C ∈ u₁ ∖ u₂. Each u_i is a character of ℓ^∞(Y);
extend it to a state ψ_i of B(ℓ²(Y)) (Hahn–Banach). Put Φ\*(a) := ψ₁(a)|+⟩⟨+| + ψ₂(a)|−⟩⟨−|.
Then:
- Φ\*(1) = 1, so TB holds, and p(Y | x) = 1 for both x;
- every p(y | x) = 0, since the u_i are free, so the point action is deterministic;
- Φ\*(P_C) = |+⟩⟨+| ∉ ℓ^∞(X), so the map is not DIO-type;
- Σ_y p(y | x) = 0 ≠ 1 = p(Y | x): complete additivity, and so normality (NRM), is what fails.

**Counterexample CX-1 (a variant; ESTABLISHED, X).** Let Y be any infinite set and
X = {0, 1}. Let ψ be a state of B(ℓ²(Y)) that vanishes on the finite-rank operators, for
instance a state of the quotient by the compact operators composed with the quotient map. Put
Φ\*(a) := ψ(a)|+⟩⟨+|. Then:
- Φ\* is positive, and Φ\*(1) = |+⟩⟨+| ≤ 1, so TB holds;
- every p(y | x) = 0, so the action is point-level deterministic in NN's sense;
- Φ\*(1) ∉ ℓ^∞(X), so the map is not DIO-type;
- in Schrödinger form, a normal input ρ goes to ⟨+|ρ|+⟩ψ: the branch weight reads an
  off-diagonal entry, and the output vanishes on every finite event;
- σ-D fails, since p(Y | x) = ½ while every singleton has weight 0.

CX-1's branch weight ½ also breaks finite-level determinism, so CX-1′ is the sharper witness.
Both exist for countable Y as well, and show that NN LIN's normality is load-bearing for NN's
point formulation on every infinite carrier.

**Counterexample CX-1b (Borel events are not enough without σ-additivity; ESTABLISHED, X, using
the axiom of choice).** Let Y be an uncountable standard Borel space.
- Let v be an ultrafilter of the Borel algebra that contains every co-countable Borel set; one
  exists by Zorn's lemma. Every member of v is uncountable.
- A Bernstein set C ⊂ Y (one that meets every uncountable Borel set, as does its complement)
  meets every member of v, and so does Y ∖ C.
- So v extends to ultrafilters u₁ ∋ C and u₂ ∋ Y ∖ C of all subsets. Each u_i is a character
  of ℓ^∞(Y), and Hahn–Banach extends it to a state ψ_i of B(ℓ²(Y)).
- Put Φ\*(a) := ψ₁(a)|+⟩⟨+| + ψ₂(a)|−⟩⟨−| on X = {0, 1}.

Then:
- Φ\*(1) = 1, so TB holds;
- for every Borel B, Φ\*(P_B) = v(B)·1, with v(B) ∈ {0, 1};
- yet Φ\*(P_C) = |+⟩⟨+| ∉ ℓ^∞(X).

The output law is {0, 1}-valued on Borel events but is not σ-additive, since v is free. So the
map is non-DIO-type relative to ℓ^∞(Y), although it is DIO-type relative to the Borel functions.
CX-1b is CX-1′ with the Borel structure kept, and shows that Borel events do not replace
σ-additivity.

**AW-2 (assumption-watch marker).** For a positive map on an atomic carrier, normality is
equivalent to complete additivity of the output configuration laws of configuration inputs
(Lemma NRM, both directions), and, under point determinism and TB, to σ-D (NRM-D, both
directions). NN DET uses normality exactly through this property. The non-normal maps of
(F-at) with point-deterministic action are exactly those whose output laws fail complete
additivity at some configuration (CX-1′, CX-1, CX-1b, M1-b), and none is a NAT operation (§6).
Records that use point determinism for maps that need not be normal should check complete
additivity.

**Lemma UE (unique extension on the quasi-local diagonal; ESTABLISHED, X).** Let ℬ be the
quasi-local algebra ⊗_{s∈Λ} M_A (Λ countable, A finite), let 𝒟 be its diagonal C(A^Λ), and let
E be the product expectation. Every state ψ of ℬ with ψ|_𝒟 = δ_y equals ε_y.

*Proof.* On a local algebra M_{A^F} (F finite), ψ restricts to a state whose diagonal is the point
mass at y|_F. Positivity kills every row of its density matrix with a zero diagonal entry, so
the restriction is |y|_F⟩⟨y|_F|, which is ε_y there. The local algebras are dense. ∎

**Theorem DET-C\* (ESTABLISHED, X; (I) on KIN-𝒟, LIN, TB; Kadison (L) for (iii)).** In (F-C\*),
let Φ_o\*: ℬ_out → ℬ_in be positive, satisfy TB, and have deterministic point action on the ε_x.
Then:
- (i) D_o := {x : p_o(X_out | x) = 1} is clopen, and f_o: D_o → X_out is continuous;
- (ii) if X_out is totally disconnected (A^Λ), then Φ_o\*(g) = 1_{D_o}·(g∘f_o) for every
  g ∈ C(X_out), so every branch is DIO-type;
- (iii) the same holds for any compact X_out;
- (iv) the branch is MIO-type, E_in Φ_o\* = E_in Φ_o\* E_out, provided every state of ℬ_out
  extending δ_{f_o(x)} is ε_{f_o(x)}. For the quasi-local diagonal this holds by UE.

*Proof.*
- E_in(Φ_o\*(g))(x) = ε_x(Φ_o\*(g)) = 1_{D_o}(x) g(f_o(x)).
- (i) With g = 1, E(Φ_o\*(1)) = 1_{D_o} is continuous and {0, 1}-valued, so D_o is clopen. On
  D_o, g∘f_o is continuous for every g ∈ C(X_out), so f_o is continuous.
- (ii) For a clopen event q_B, E(Φ_o\*(q_B)) = 1_{D_o ∩ f_o^{-1}B} is a projection. Corollary P1
  gives Φ_o\*(q_B) ∈ 𝒟_in, and locally constant functions are dense.
- (iii) P_o := Φ_o\*(1) = 1_{D_o}, by Corollary P1. From 0 ≤ Φ_o\*(a) ≤ ‖a‖P_o for a ≥ 0,
  Lemma P's argument gives Φ_o\*(a) = P_o Φ_o\*(a) P_o. So Ψ := Φ_o\* is unital and positive into
  the corner P_o ℬ_in P_o, which carries the faithful expectation P_o E(·) P_o.
  - For real g, put d := E(Ψ(g)) = (g∘f_o)P_o and h := Ψ(g) − d.
  - Bimodularity gives E(h²) = E(Ψ(g)²) − d².
  - Kadison's inequality gives E(Ψ(g)²) ≤ E(Ψ(g²)) = (g²∘f_o)P_o = d².
  - So E(h²) ≤ 0, and E(h²) ≥ 0. Faithfulness gives h = 0.
- (iv) ε_x∘Φ_o\* is a positive functional whose restriction to 𝒟_out is 0 or δ_{f_o(x)}. If it
  is 0, its value at 1 vanishes, so the functional is 0. Otherwise it is a state extending
  δ_{f_o(x)}, hence equal to ε_{f_o(x)}. So E_in Φ_o\*(b)(x) = E_out(b)(f_o(x)) =
  E_in Φ_o\*(E_out b)(x), the last step by the formula E_in Φ_o\*(g)(x) = 1_{D_o}(x) g(f_o(x))
  with g = E_out b. ∎

No normality, no countability and no reference measure are used. Every Radon law on X, including
a diffuse one, is the state μ∘E.

**SHARP-C\* (ESTABLISHED, X).** For X_out totally disconnected and any positive Φ_o\* with TB: if
the branch is non-DIO-type, there are a clopen B and a nonempty open set of x with
p_o(B | x) ∈ (0, 1). On A^Λ, which has no isolated points, that set is uncountable. This is the
contrapositive of the step in DET-C\* (ii), which uses no determinism beyond each
E(Φ_o\*(q_B)) being a projection.

**Counterexample CX-2 (unique extension is needed for MIO; ESTABLISHED, X).** Let X = [−1, 1],
with ℤ₂ acting by t ↦ −t, and let ℬ = C(X) ⋊ ℤ₂, with implementing unitary u, 𝒟 = C(X) and
E(f + gu) = f.
- 𝒟 is maximal abelian: f′ + g′u commutes with every h only if g′(t)(h(−t) − h(t)) = 0, so
  g′ = 0.
- E is faithful.
- Because 0 is fixed, f + gu ↦ f(0) + g(0) is a character ψ. It extends δ₀, and ψ(u) = 1 ≠ 0 =
  ε₀(u).

Put Φ\*(b) := ψ(b)·1. It is positive and unital, deterministic (every x goes to 0), and DIO-type
(Φ\*(g) = g(0)1). It is not MIO-type, since E Φ\*(u) = 1 while E Φ\*(E u) = 0.

The same construction gives: if unique extension fails at some y ∈ X_out, the constant action
onto y has a DIO-type, non-MIO-type positive extension, ψ(·)1. This is the only converse shown.
It does not show that a given action f with y ∈ f(D_o) has a non-MIO-type extension: replacing
ε_{f(x)} by ψ at one non-isolated x need not give an element of ℬ_in. So (F-C\*) states MIO in
one direction, DET-C\* (iv). The corpus-relevant pairs, the atomic one and the quasi-local
diagonal, have unique extension.

**Theorem DET-R (ESTABLISHED, X).** Let R be the trace closure of the quasi-local algebra, with
𝒟 = L^∞(A^Λ, μ) where μ is the uniform Bernoulli measure (the trace's restriction), and E
trace-preserving. If Φ_o\* is positive, satisfies TB and satisfies E-D, then
Φ_o\*(𝒟_out) ⊆ 𝒟_in (Corollary P1, together with norm density of the span of projections in an
abelian von Neumann algebra). The proof uses only a faithful E, and holds for any such pair.

**MIO-R (ESTABLISHED, X; for the quasi-local trace closure only).** If, in addition, Φ_o\* is
normal, then E_in Φ_o\* = E_in Φ_o\* E_out. The proof uses the atoms of 𝒟 ∩ M_{A^F}, so it is
stated for this pair and not for general Cartan pairs.

*Proof.* Let c be local, supported on F, with E(c) = 0, and split it into self-adjoint parts.
With p_i the atoms of 𝒟 ∩ M_{A^F}, p_i c p_i = 0, so c = Σ_{i≠j} p_i c p_j. Write
x_{ij} := p_i c p_j + p_j c p_i, which is self-adjoint.
- Block positivity gives ±x_{ij} ≤ ‖c‖(t p_i + t^{-1} p_j) for every t > 0.
- Applying Φ_o\* and E: q_k := Φ_o\*(p_k) are orthogonal projections of 𝒟_in (DET-R and TB),
  and ±E Φ_o\*(x_{ij}) ≤ ‖c‖(t q_i + t^{-1} q_j).
- This is a function inequality in the abelian 𝒟_in, so letting t → 0 and t → ∞ gives
  E Φ_o\*(x_{ij}) = 0.
- So E Φ_o\*(b) = E Φ_o\*(E b) on the local algebra.
- Both sides are normal, and the local algebra is σ-weakly dense. ∎

**Theorem DET-SS (ESTABLISHED, X; definitional).** In B(L²(X, μ)), μ diffuse, let Φ_o\* be
positive, satisfy TB and satisfy SS-D. Then Φ_o\*(L^∞_out) ⊆ L^∞_in. Since SS-D is equivalent to
the projection case of this conclusion (§3), DET-SS adds only norm density.

*Proof.* Testing vector states in ran P and in ran(1 − P) gives P(1 − F)P = 0 and
(1 − P)F(1 − P) = 0. Lemma P gives F = P. Then conclude by norm density. ∎

MIO cannot be typed here: there are no normal diagonal states (NE), and diffuse laws are
non-normal states.

**Verdict N3: YES** in (F-at), (F-C\*) and R, under their determinism hypotheses, for the stated
maps. In type-I diffuse W\* DET-SS holds but is definitional. The verdict is **NO** for the
following weaker hypotheses, each shown by a counterexample:
- point determinism without σ-additivity (CX-1′, CX-1);
- Borel-event determinism without σ-additivity (CX-1b);
- MIO without unique extension, for the constant action (CX-2).

## 5. N4: reductions and record laws

**Corollary RED-∞ (ESTABLISHED, X; (I) on KIN-B or KIN-𝒟, LIN, TB; (N) DEC, FIN-V where stated).**
The total carrier is C_V × Z, the hidden state is ω and the visible instrument is
Φ^V_o\*(a) := σ_ω(Φ_o\*(a ⊗ 1)).
- **(F-at).** Z is of any cardinality. Take ω any state of B(ℓ²(Z)) when C_V is finite (FIN-V),
  and ω normal for any C_V. Then:
  - (i) DIO-type: DET-at puts Φ_o\*(g ⊗ 1) in ℓ^∞(C_V × Z) = ⊕_v ℓ^∞(Z), and the entrywise slice
    gives (ω(f(v, ·)))_v. This is positive, since id_n ⊗ ω is CP.
  - (ii) MIO-type if ω = ω∘Δ_Z, normal or not: Δ_V σ_ω = σ_ω Δ, and DET-at (ii) applies at the
    total level.
- **(F-C\*).** ℬ_tot = ℬ_V ⊗_min ℬ_H with ω any state of ℬ_H. DET-C\* is applied to the total
  pair (ℬ_tot, 𝒟_V ⊗ 𝒟_H, E_V ⊗ E_H), which needs E_V ⊗ E_H to be faithful on ℬ_V ⊗_min ℬ_H. This
  is a hypothesis for general pairs; for the quasi-local pair it is immediate from the faithful
  trace. The slice id ⊗ ω exists for any state, maps 𝒟_V ⊗ 𝒟_H into 𝒟_V, and needs no
  restriction on the visible carrier. Branches are
  MIO-type if ω = ω∘E_H and the total pair has unique extension at the image points; for the
  quasi-local algebra the total pair is again quasi-local, so UE applies.
- **(F-W\*), R.** ω is normal, or ω is any state when C_V is finite. The pointwise slice of
  ⊕_v L^∞(H) is OPRES D′ step 3 with X = C_V.

In the total-carrier framing there is a single hidden state, on the whole hidden algebra. So
OPRES D′'s restriction to one non-normal state, appended while no diffuse factor is present,
does not arise: RED-∞ holds for every joint hidden state, including every extension of a product
of non-normal states. This concerns RED-∞'s class (positive extensions given on the total
carrier). It does not settle OPRES U1′, whose protocols append states step by step.

For CP extensions, the visible map is a CP DIO-type map on M_{C_V}, and OPRES Theorem C(b) gives
‖Φ^V − Ad_W‖_⋄ ≥ 2κ_row(W).

**Corollary IDLE-∞ (ESTABLISHED, X).** In (F-at), (F-C\*) and R, and in type-I diffuse W\* under
SS-D, which is definitional there (§3), for every state ρ of ℬ_in:
- the probability of outcome o is ρ(Φ_o\*(1)) with Φ_o\*(1) ∈ 𝒟_in;
- the joint law of outcome and output configuration is ρ∘Φ_o\*|_{𝒟_out}, and it depends only
  on ρ|_{𝒟_in}.

For example, on the quasi-local algebra over {0, 1}^Λ:
- the trace τ = μ_unif∘E and the pure product state ⊗_s |+⟩⟨+| have the same configuration law,
  the uniform Bernoulli measure;
- no NAT protocol distinguishes them.

Coherence carried by a state with a diffuse configuration law is idle at the record level.

**M2 kept separate.** M2 is (F-at) with C_V countably infinite and ω non-normal. On
ℓ^∞(C_V × Z) the pointwise slice f ↦ (ω(f(v, ·)))_v is canonical for every ω, so the DIO part on
𝒟 is not the obstruction. What RED-∞ does not supply is the visible instrument itself: defining
Φ^V_o\* on the non-diagonal elements of B(ℓ²(C_V)) when C_V is infinite and ω is non-normal, which
is NN M2 and OPRES U1′(ii). (F-C\*)'s minimal-tensor slice is a different formulation, and it
does not settle M2 as posed.

**Verdict N4: closed** at the stated scope.

## 6. N5: what NAT delivers on an uncountable carrier

- **The determinism hypotheses.** NAT makes outcomes and records functions of configurations and
  every transition a step of φ. Read on the total carrier, a native branch therefore sends each
  configuration x ∈ D_o to the configuration f_o(x).
  - So the output law of a configuration input is the point mass δ_{f_o(x)}: σ-D in (F-at), and
    point determinism on ε_x in (F-C\*).
  - Each output event pulls back to the event f_o^{-1}(B) ∩ D_o: E-D in R, where the pull-back is
    well defined on null classes when f_o is nonsingular (the singular case is M1-c).
  - SS-D is not delivered by NAT. NAT fixes configuration maps, not the action on coherent normal
    states, and in type-I diffuse W\* every normal state concentrated on an event is coherent
    (NE). SS-D follows from NAT only under the law-level reading, which is definitional (§3).
  - CX-1′, CX-1, CX-1b and CX-2's output functionals are not configurations (they are points at
    infinity, free ultrafilters, or a non-diagonal character), so they are not NAT outputs.
  - ESTABLISHED (P, reading of NAT); NAT itself is ASSUMED, (N), not adopted.
- **Non-vacuity (ESTABLISHED, X; Curtis–Hedlund–Lyndon (L)).** Positive extensions of native actions exist in
  each formulation:
  - **(F-at).** The permutation unitary U_f extends any bijection f; no measurability is needed.
  - **(F-C\*).** The selected update of §3.2 is a reversible nearest-neighbour update on ℤ^d
    (`Main:294`, `Main:131`), so it is a CA and a bijective homeomorphism of A^{ℤ^d}. Its inverse
    is continuous (compactness) and commutes with the shifts, so it is a CA by the
    Curtis–Hedlund–Lyndon theorem on ℤ^d (Ceccherini-Silberstein–Coornaert). Ad U_f then
    restricts to an automorphism of the quasi-local algebra that preserves 𝒟.
    - Represent ℬ on ℓ²(A^Λ) by π(|a⟩⟨b|_F)|x⟩ = [x_F = b]|x[F ← a]⟩. This is faithful, because
      ℬ is simple, and π(𝒟) consists of multiplication by continuous functions.
    - Then U_f† π(|a⟩⟨b|_F) U_f sends |x⟩ to [f(x)_F = b] |f^{-1}(f(x)[F ← a])⟩. Only sites
      within F − N′ change, with N′ the inverse neighbourhood, and the result depends on x
      through a finite window.
    - So the conjugate is a finite sum of local matrix units, and the same holds for U_f.
  - **(F-W\*), R.** The automorphism of the quasi-local algebra just constructed preserves its
    unique tracial state τ, so it extends to R. Since it preserves 𝒟 and τ|_𝒟 = μ_unif, the
    uniform Bernoulli measure is invariant under f, and the Koopman unitary exists on L²(μ_unif).
    No measure-invariance theorem for CA is needed.
- **The reference measure.** (F-at) and (F-C\*) need no reference measure. The nonsingularity
  hypothesis of OPRES Proposition D, and the open singular case D″, are therefore properties of
  the W\* formulation over a chosen μ. In (F-C\*) the detection half holds for every homeomorphic
  dynamics, and every Radon law, singular ones included, is a state. This does not prove D″,
  which concerns L²(H, ν) for a singular T.

**Coherence is relative to the formulation (observation; X).**
- In (F-at), B(ℓ²(A^Λ)) contains |x⟩⟨x′| for configurations differing at infinitely many sites.
- In (F-C\*), the quasi-local algebra contains coherences only between configurations that
  differ on finitely many sites (its matrix units are local).
- In R, coherence is relative to the diffuse Cartan algebra.

The verdicts DET, RED and IDLE are the same in all three, so the choice of formulation does not
change the obstruction. It does change what "coherence" refers to.

## 7. N6: drop-one

| Premise | Dropped | Effect |
|---|---|---|
| σ-D, (F-at) | point determinism only, non-normal map | **fails**: CX-1′ (and CX-1), on any infinite carrier |
| σ-D, (F-at) | Borel-event determinism only, non-normal map | **fails** relative to ℓ^∞(Y): CX-1b, uncountable Y, using choice |
| normality of the map, (F-at) | — | not a separate premise: σ-D implies it (NRM-D) |
| countability of X | — | **not used** (N1) |
| TB | the bound on configuration inputs only | **fails**: NN's Ψ(ρ) = 2⟨+\|ρ\|+⟩\|0⟩⟨0\| on a two-letter site of A^Λ, tensored with the identity elsewhere |
| DEC | a unitary deep factor coupled by configuration swaps | **fails**: Ad_H on the visible system (NN 4e), unchanged on any carrier |
| faithful E, (F-C\*) or R | an expectation that is not faithful | DET's route is unavailable. Type-I diffuse W\* has only such expectations (NE), and its reading SS-D is definitional |
| unique extension, (F-C\*) | a pair with a non-unique extension at some point y | MIO **fails** for the constant action onto y: CX-2. DIO is unaffected. For a general action the converse is not shown |
| normality of the map, R | — | needed for MIO-R's density step; DET-R does not use it |
| FIN-V | a countably infinite C_V with a non-normal ω, in (F-at) | not covered: this is M2 (§5) |
| total disconnectedness of X | compact X | **not used** (DET-C\* (iii)) |
| reference measure, nonsingularity | — | **not used** in (F-at) or (F-C\*); used by NAT's delivery of E-D in R (M1-c) |
| KIN-B / KIN-𝒟 | a rotated logical basis; encoded carriers | as in NN N6: relocated to the interface, or outside the statement |

## 8. Classification (§A.31) and productivity

| Item | Label | Layer | Class |
|---|---|---|---|
| Lemma P, Corollary P1 | — | X | ELABORATING: the operator core of NN DET, free of any basis |
| Lemma NE | Sierpiński (L) | X | ELABORATING: sharpens OPRES's "no normal Δ" to "no faithful or normal expectation; none fixes a normal state" |
| DET-at | (I): KIN-B, LIN, TB; σ-D | X | ELABORATING: NN DET for any cardinality |
| Lemma NRM, NRM-D | — | X | ELABORATING; (b) from the review |
| CX-1′, CX-1, CX-1b; AW-2 | — | X | **NEW** (assumption-watch): normality of the map is equivalent to complete additivity of the output configuration laws, and NN DET uses it exactly there |
| Lemma UE; DET-C\*; SHARP-C\*; CX-2 | (I): KIN-𝒟, LIN, TB; Kadison (L) | X | ELABORATING: decides M1 in (F-C\*) for all states and every Radon law |
| DET-R, MIO-R | (I): KIN-𝒟, LIN, TB; E-D; nonsingular NAT maps for the native reading | X | ELABORATING: decides M1 in R at the stated scope |
| DET-SS | (I): KIN-𝒟, LIN, TB; SS-D | X | CONFIRMING: definitional (§3) |
| RED-∞, IDLE-∞ | as above; DEC; FIN-V where stated | X | ELABORATING |
| §6 reference-measure observation | — | P | BORDERLINE: it locates D″ in the W\* formulation and does not settle it |
| §6 coherence-relative-to-formulation | — | X | CONFIRMING |

**Productivity test (`PLAN.md` §5).**
- *Stronger than the restatement:* NN N5 stopped at "both typable measurable readings make DIO
  definitional; a non-trivial reading needs non-normal point states, not defined". This record
  supplies:
  - three non-definitional determinism readings (σ-D, ε_x, E-D);
  - rigidity under each;
  - point states and an extension class, in (F-C\*);
  - a proof that a diffuse type-I carrier admits no faithful expectation.
- *(i) Constrains:* it decides NN M1 at the stated classes; it bears on READOUT-ALG items 11
  and 12 on measurable spaces through DET-R, under NAT and nonsingularity; OPRES U1′ is not
  settled.
- *(ii) Exposes a hidden assumption:* AW-2.
- **Gem under `PLAN.md` §5. Output class ELABORATING, with one NEW marker.**

*Skepticism on the favourable branch.* The result extends the obstruction, so the question is
whether the determinism hypotheses smuggle DIO in. Three checks bear on it:
- σ-D, ε_x and E-D pass the circularity test of N2; each constrains only diagonal data, and
  Corollary P1 does real work in each. SS-D does not pass it, and is recorded as definitional.
- In (F-at), CX-1′, CX-1 and CX-1b show that strictly weaker hypotheses fail. No such
  counterexample is given for (F-C\*) or R, where the hypotheses are already on diagonal inputs
  only.
- The hypotheses used are the ones NAT delivers (§6), with nonsingularity for E-D.

*Stop condition.* After the first full pass, which produced AW-2, two further passes over N1
were made:
- (F-C\*) with a non-totally-disconnected X, and outcome sets that are uncountable or recorded;
- the W\* formulations relative to the Borel functions instead of ℓ^∞.

Neither yielded a NEW finding. That is two passes, not the three consecutive passes of
`PLAN.md` §8's fixed-point condition, which is therefore not met, and the §A.31 fixed point is not
reached. Lemma NRM, which sharpens AW-2 and is classed ELABORATING, was found in review. This
record reads the bullets of `PLAN.md` §8 as alternative stop conditions, and stops under the one
that is met: the question is answered, or reported untypable with its missing ingredient, in
every formulation of `PLAN.md` §3.

## 9. ESTABLISHED, ASSUMED, MISSING

**ESTABLISHED** (this record, layer X, unreviewed; literature (L) at its source's standing):
- Lemma P, Corollary P1, Lemma NE, Lemma NRM, Corollary NRM-D and Lemma UE;
- DET-at, DET-C\*, SHARP-C\*, DET-R and MIO-R; DET-SS, which is definitional;
- CX-1′, CX-1, CX-1b (using choice) and CX-2;
- RED-∞ and IDLE-∞, each at its stated scope;
- the step audit (§2), the non-vacuity constructions (§6) and the drop-one table (§7).

**ASSUMED:**
- (I): KIN-B, KIN-𝒟, LIN and TB;
- (N): DEC, DEF, A2, LAW and FIN-V;
- NAT: (N), a reading of T-SUB′ (ii) and (iii), not adopted;
- UNC, as the scope hypothesis;
- the determinism readings σ-D, point determinism on ε_x and E-D. NAT delivers each (§6), E-D
  for nonsingular maps, and each is ASSUMED for any map that is not a NAT operation. SS-D is not
  delivered by NAT except through the definitional law-level reading.

**MISSING:**
- **M1-a.** MIO in a type-I diffuse W\* carrier. It cannot be typed there (NE). The creation
  question for diffuse laws is answered in (F-C\*) and R instead.
- **M1-b.** Atomic, non-normal maps whose deterministic laws are {0, 1}-valued but not
  σ-additive. MIO there needs unique extension of free-ultrafilter states of ℓ^∞(Y) to B(ℓ²(Y)).
  For countable Y this is the Kadison–Singer theorem (L), and it is not checked here for
  uncountable Y; the review suggests that paving with uniform constants and a compactness
  argument may give it, which stays MISSING until a source is checked. These maps are not NAT
  operations (§6).
- **M1-c.** W\* formulations over a reference measure that a native dynamics renders singular.
  The pull-back of events is then not defined on null classes, which is OPRES D″. The R row of §0
  is stated for nonsingular maps for this reason. It is not needed in (F-at) or (F-C\*).
- **M2** (NATIVE-NONDIO), unchanged and not settled (§5).
- **NN M3** (nonlinear state assignments) and **NN M4** (the nativeness criterion), unchanged.

No item here needs computation, and none was run.

## 10. What this record does not do

It edits no manuscript, Lean module, reviewed record, Issue or file of another track, and no
path in the A1 retirement ledger (`PLAN.md`, A1 ledger check). It adopts no premise and no
nativeness criterion. It treats the A1 retirement as not landed, and it says nothing about encoded
carriers.
