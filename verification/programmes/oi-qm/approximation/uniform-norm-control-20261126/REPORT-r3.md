# OI-QM-APPROX-1: uniform norm control in the converse — report, revision r3

Revision r3 applies the two nits of the delta review of r2 (`REPORT-r2.md`, commit
`1f49e6beda01526faf6b1a32204fdd225abfecb1`), posted on PR #1614, verdict ACCEPT WITH NITS. Apart
from this note, the title, the CC-p paragraph of §5, the CC-p row of §9 and the first sentence of
(U-a) in §3, it is identical to r2. The change map is `CHANGES-r3.md`.

Revision r2 applies findings 1–9 of the independent review of r1 (`REPORT.md`, commit
`1a6252f41ce71a029239a82f9bea667d056f8335`), posted verbatim on PR #1614, verdict ACCEPT WITH NITS,
no mathematical error found. r1 and `PLAN.md` are kept unchanged. The change map is
`CHANGES-r2.md`.

On when the derivation began (review observation 10): before the plan was committed, the writer
read the inputs and explored the question informally in the session, including the idea behind
Theorem G (using the coverage partner of the identity as a gauge). None of this was written down
before `PLAN.md` was committed, and the written derivation followed it. The plan therefore does
not certify that the derivation started afterwards, only that the decision rule was recorded
before the report. The rule N1–N4 is outcome-neutral.

Writer's report under `PLAN.md` (commit `de3447139fa13ce8ba1c84baa66d6302c03fa48f`), which fixes the
questions, the decision rule, the controls and the stopping conditions; they are not restated.
Pinned source: `main` = `a8d4ab969e274dc6ba25cbc6021da909d5aec814`.

Labels: [A] this investigation's paper argument, unreviewed; [U2] `../unit2/REPORT-r3.md`; [U3]
`../unit3/REPORT-r3.md` and `../unit3/PRESERVATION.md`; [L] standard mathematics. [U2] and [U3]
are reviewed paper derivations, not independently verified; they are used only for unchanged
steps, named where used. The rescaled theory T_s is unit 3's item D1 (`../unit3/PRESERVATION.md`
§7): it originated in a review, is recorded there as partially verified and is not part of unit 3's
report. It is labelled [D1] here, and only its definition and τ_min = s are used. No computation
was run. Nothing here is adopted, promoted or proposed for
the manuscripts.

## 0. Results

| ID | Result | Premises | Status |
| --- | --- | --- | --- |
| Lemma R, Lemma I | The coverage partner Φ := c′(id) of the identity is invertible, and its (K−1)-fold dual carries the test effects onto the projectors within 4ε | M_C < ε < 1/16, m, K ≥ 2 | proved [A] |
| Theorem G | Gauged uniform norm control: ‖Φ^{-1}∘F‖ ≤ C_G = 8(1+2ε)/(1−16ε) for every available F | same; no η-rule, no τ_min, no hypothesis on g | proved [A] |
| Corollary G1 | g ≤ sup_F ‖F‖ ≤ C_G‖c′(id)‖ < ∞, and ‖c′(id)‖ ≤ sup_F ‖F‖; g is finite whenever ε < 1/16 | same | proved [A] |
| Lemma 7G | Lemma 7 in the gauge of Φ: ‖Φ^{-1}F − c̃(F)‖ ≤ κ_snd and ‖Φ^{-1}c′(J) − J‖ ≤ κ_cov, with c̃(F) = c(Φ)^{K−2}∘c(F) a quantum instrument | same | proved [A] |
| Theorem U | Reduction of the converse to one number φ = ‖c′(id) − id‖: φ small for an admissible c′ ⇒ Lemma 7's map bounds for the pair (c̃, c′) and Theorem 8, with explicit constants (the bound for the original c is not claimed); Lemma 7's coverage bound for an admissible pair ⇒ φ ≤ κ | same; directions separate | proved [A], each direction |
| Prop S | On the system under rule (a): ‖Φ^{-1}‖ ≤ C_G/(1−η_a), and Φ^{-1} lies within δ_S of the quantum channel Q_I = c̃(I′); two one-directional perturbation bounds, each with its smallness condition | adds η_a < 1 | proved [A] |
| Prop X1 | Gauge-conjugate theories S∘Q∘S^{-1} (tr∘S = tr) with M_C < ε have all norms ≤ 32(1+2ε)/(1−16ε) | M_C < ε < 1/16, m, K ≥ 2 | proved [A] |
| Prop X2 | T_− = −Q (and T_ω = ωQ, ω^K = 1) has M_C = 0 at every m, with norms 1, and Lemma 7's conclusion fails | K even (resp. ω^K = 1); lies in class(η) only for η_a, η_c, η_d, η_e ≥ 2 | proved [A] |
| CC-s | T_s [D1] satisfies M_C < ε only if ((1+s)^K − 1)/2 < ε | — | proved [A] |
| CC-p | T_S with S^{-1} = C_p: every law is a probability vector (F1 holds exactly), the coverage term is at least p/4, and norms reach (1 + p(N−2)/N)/(1−p), unbounded as p → 1 | N ≥ 2 | proved [A] |

**Outcome against the decision rule (`PLAN.md` §3).**
- **U1: N2, relative bound.** A bound uniform over every theory with M_C < ε, independent of η,
  τ_min and g, is proved in the norm X ↦ ‖Φ^{-1}X‖₁, where Φ is the chosen correspondence's
  coverage partner of the identity (Theorem G). In the fixed trace norm the bound holds up to the
  factor ‖c′(id)‖ (Corollary G1). No bound on that factor, uniform over class(η) at fixed small η,
  is obtained.
- **U2: the single residual is φ = ‖c′(id) − id‖, named in both directions.** The converse under
  M_C reduces to φ for an admissible c′ (Theorem U): φ small gives Lemma 7's map bounds for the pair
  (c̃, c′), where c̃ = c(Φ)^{K−2}∘c, and Theorem 8; Lemma 7's coverage bound gives φ small. Each
  direction is proved separately. A bound on ‖F − c(F)‖ for the original c is not claimed. The
  norm ‖c′(id)‖ is the part of φ that unit 3's marker W4 isolates. The padding and its floor
  τ_min, which unit 3 identified as the obstruction, are not needed for the gauged statement.
- **PLAN §3's void clause.** A bound is void if its assumptions admit CC-L. Theorem G is a bound in
  the gauged norm, and Corollary G1 is relative to ‖c′(id)‖. A CC-L theory (large trace norm)
  would force ‖c′(id)‖ to be large, which both statements allow, so neither would be voided. No
  trace-norm bound of type N1, which CC-L would void, is claimed.
- **U3: open.** The natural operational candidate, an idle step at each level (an available
  single-outcome family near the identity), is analysed in §6. It is not shown to close φ; it is
  recorded as a candidate premise, not adopted (§A.29, §A.50 item 6).
- **CC-L: open, with two subclasses excluded and necessary conditions proved.** Gauge conjugates
  are excluded (Prop X1); T_s violates M_C < ε unless s < 2ε/K (CC-s). Any CC-L theory must have,
  for every admissible c′, φ(c′) ≥ τ_min and ‖c′(id)‖ ≥ g/C_G (§5).
  Prop X2 is a countercontrol of a different kind: bounded norms with the converse failing, at
  η = 2 only.

The stop is by bounded effort with the gap stated precisely (`PLAN.md` §5): §7, node UN-1.

***

## 1. Setting and notation

Fix a level (or the system), m ≥ 2, K ≥ 2, and correspondences c, c′ whose soundness and
coverage terms are at most ε, which exist when M_C(T, Q) < ε [U2]. P denotes the identity
channel, a single-outcome quantum instrument. For a projector E, M_E = {E, 1 − E} (Lüders),
G_E := c′(M_E), Γ_E := Γ_{G_E,1} and Γ′_E := Γ_{c(G_E),1} (N5 [U2]). Write

Φ := c′(P), an available single-outcome family; Ψ := c(Φ), a quantum channel;

and, for a linear map X on matrices, X† for its dual under the trace pairing,
tr(Y X(Z)) = tr(X†(Y) Z). Set

A_E := (Φ^{K−1})†(Γ_E), C_ρ := 4(1+2ε)/(1−16ε), C_G := 2C_ρ,
κ_cov := 16ε(1 + 2C_ρ), κ_snd := 32ε(1 + C_ρ).

As ε → 0: C_ρ → 4, κ_cov ≈ 144ε, κ_snd ≈ 160ε.

Two facts are used throughout:
- **(F1) Law boundedness.** If the soundness term is at most ε, every T-law of a protocol in the
  class lies within ℓ¹ distance 2ε of a probability vector, so the absolute values of its entries
  sum to at most 1 + 2ε. This is the definition of TV and of the soundness term [U2 §2].
- **(F2) N5 [U2].** If |tr(Zσ)| ≤ η for every density σ, then ‖Z‖_op ≤ 2η (η if Z is Hermitian);
  ‖Y‖₁ ≤ 4 max_E |tr(EY)| over projectors E (factor 2 if Y is Hermitian); a general X is a
  combination of four positive matrices of total trace at most 2‖X‖₁.

## 2. Gauged norm control

**Lemma R (tail effects) [A].** For every projector E, ‖A_E − E‖_op ≤ 4ε.

*Proof.* The quantum protocol (P^{K−1}, M_E) has law (tr Eρ, tr(1−E)ρ). Its coverage partner
(Φ^{K−1}, G_E) has first entry tr(Γ_E Φ^{K−1}ρ) = tr(A_E ρ). TV ≤ ε gives |tr((A_E − E)ρ)| ≤ 2ε
for every density, and F2 (A_E need not be Hermitian) gives 4ε. □

**Lemma I (invertibility) [A].** If ε < 1/16, Φ is invertible.

*Proof.* If Φ were singular, so would be (Φ^{K−1})†, whose range V would be a proper subspace.
Take Z ≠ 0 annihilating V under the trace pairing, with ‖Z‖₁ = 1. Since A_E ∈ V,
|tr(EZ)| = |tr((E − A_E)Z)| ≤ 4ε for every projector E, and F2 gives 1 = ‖Z‖₁ ≤ 16ε. □

**Theorem G (gauged uniform norm control) [A].** Let ε < 1/16. For every available family F with
at most m outcomes, Σ_a ‖Φ^{-1}F_aρ‖₁ ≤ C_ρ for every density ρ, and ‖Φ^{-1}∘F‖ ≤ C_G.

*Proof.*
1. Fix ρ and F, and let X_a := Φ^{-1}F_aρ. For each outcome a choose a projector E_a with
   |tr(E_aX_a)| ≥ ‖X_a‖₁/4 (F2); the choice depends only on (F, ρ).
2. The T-protocol "F; after outcome a, Φ for K − 2 steps; then G_{E_a}" has horizon K and outcome
   bound m. Its (a, 1) entry is tr(Γ_{E_a} Φ^{K−2} F_aρ) = tr(A_{E_a} X_a).
3. By F1, Σ_a |tr(A_{E_a}X_a)| ≤ 1 + 2ε. By Lemma R, Σ_a |tr(E_aX_a)| ≤ 1 + 2ε + 4εΣ_a‖X_a‖₁.
4. With step 1, Σ_a‖X_a‖₁ ≤ 4(1+2ε) + 16εΣ_a‖X_a‖₁. The sum is finite for the fixed (F, ρ), so it
   is at most C_ρ. The four-part split gives ‖Φ^{-1}∘F‖ ≤ 2C_ρ = C_G. □

The bound uses the soundness term only in step 3 and the coverage term only in Lemma R. It uses no
structure rule, no padding, no τ_min and no hypothesis on g, and it is uniform over every theory
with M_C < ε < 1/16 at m, K ≥ 2. Unlike the bootstrap of unit 3 §5.3, the self-consistent
inequality in step 4 is linear with coefficient 16ε < 1, so it has no excluded branch.

**Corollary G1 [A].** For every available F with at most m outcomes, ‖F‖ ≤ C_G‖Φ‖_{1→1}. Hence
g ≤ C_G‖c′(P)‖. Conversely, ‖c′(P)‖ is the norm of one available family.
- **g is finite.** For a single theory and an admissible pair, ‖c′(P)‖ is the norm of one linear
  map in finite dimension. So g < ∞ for every admissible pair whenever ε < 1/16, m ≥ 2 and K ≥ 2.
- **What the uniformity is over.** Take a class of theories, with an admissible c′ chosen for each
  at the given ε. Each direction is separate:
  - if ‖c′(P)‖ ≤ ν over the class, then every available family of every theory in it has norm at
    most C_Gν;
  - if the available families are bounded by B over the class, then ‖c′(P)‖ ≤ B.
- **Consequence for unit 3's O2-a (for routing only; unit 3's record is not edited).** Unit 3
  leaves open the branch g = ∞ (`../unit3/REPORT-r3.md` §5.2, "may be infinite"; §5.3, "excludes
  neither g = ∞"). Whenever ε < 1/16, that branch does not occur. The branch that remains is a
  finite g above unit 3's threshold (1/8 − 6ε)/ω′. Recording this against O2-a is a matter for a
  mutable record of unit 3 or for #1216.

**Lemma 7G (lifting in the gauge) [A].** Let ε < 1/16, and c̃(F) := Ψ^{K−2}∘c(F), a quantum
instrument with F's outcome set. Then:
- (coverage) ‖Φ^{-1}∘c′(J) − J‖ ≤ κ_cov for every quantum instrument J with at most m outcomes;
- (soundness) ‖Φ^{-1}∘F − c̃(F)‖ ≤ κ_snd for every available F with at most m outcomes.

*Proof.* (Coverage.) Fix ρ, let X_a := Φ^{-1}c′(J)_aρ and Y_a := X_a − J_aρ, and choose E_a for
Y_a as in F2. The quantum protocol (J, P^{K−2}, M_{E_a}) has (a, 1) entries tr(E_aJ_aρ). Its
coverage partner (c′(J), Φ^{K−2}, G_{E_a}) has (a, 1) entries tr(A_{E_a}X_a). TV ≤ ε, Lemma R and
Theorem G (applied to the available family c′(J)) give Σ_a|tr(E_aY_a)| ≤ 2ε + 4εC_ρ. F2 gives
Σ_a‖Y_a‖₁ ≤ 8ε(1 + 2C_ρ), and the four-part split gives κ_cov.

(Soundness.) Fix ρ and F, let X_a := Φ^{-1}F_aρ and Z_a := Ψ^{K−2}c(F)_aρ (positive, with
Σ_a tr Z_a = 1), and choose E_a for X_a − Z_a. The T-protocol of Theorem G's step 2 and its
soundness partner (c(F), Ψ^{K−2}, c(G_{E_a})) give Σ_a|tr(A_{E_a}X_a) − tr(Γ′_{E_a}Z_a)| ≤ 2ε.
Unit 2's step B [U2 §4.2, unchanged; it uses no T-side trace preservation, as unit 3 §5.1
records] gives ‖Γ′_E − E‖ ≤ 2ε. With Lemma R and Theorem G,
Σ_a|tr(E_a(X_a − Z_a))| ≤ 2ε + 4εC_ρ + 2ε, so Σ_a‖X_a − Z_a‖₁ ≤ 16ε(1 + C_ρ), and the four-part
split gives κ_snd. □

## 3. Reduction of the converse to one number

**Theorem U [A].** Let m, K ≥ 2 and ε < 1/16. Each direction is a separate statement (§A.34).
- **(U-a)** For an admissible pair (c, c′), with φ := ‖c′(P) − id‖_{1→1}:
  ‖F − c̃(F)‖ ≤ (1+φ)κ_snd + φ for every available F, and ‖c′(J) − J‖ ≤ (1+φ)κ_cov + φ for every
  quantum instrument J, all with at most m outcomes. This is Lemma 7's pair of map bounds for the
  pair (c̃, c′), with c̃ in place of c. No bound on ‖F − c(F)‖ for the original c is claimed; it
  would need c(Φ)^{K−2} to be near the identity, which is not shown. c̃ is not claimed to have
  soundness term at most ε.
- **(U-b)** If an admissible pair satisfies the coverage conclusion of Lemma 7 with constant κ,
  then φ(c′) ≤ κ.

*Proof.* (U-a): ‖F − c̃(F)‖ ≤ ‖Φ‖·‖Φ^{-1}F − c̃(F)‖ + ‖(Φ − id)∘c̃(F)‖ ≤ (1+φ)κ_snd + φ, using
‖c̃(F)‖ = 1 (N1 [U2]). The coverage bound is the same computation with Lemma 7G's coverage half.
(U-b): take J = P. □

**Theorem 8 under (U-a) [A, with U2].** Unit 2's proof of Theorem 8 uses Lemma 7 only through the
two map bounds and the fact that c(F) is a quantum instrument [U2 §4.2]. It does not use
c's soundness term. With c̃ in place of c,
(U-a) at each level of Λ gives C_{(N_Λ+1)κ′}[m, Λ], with κ′ := max over Λ of
(1+φ)·max(κ_snd, κ_cov) + φ, φ read at each level.

**Consequences.**
- The padding route of Lemma 7 (steps A and C), with its trace defect multiplying output norms
  (W4), is not intrinsic to the converse. In the gauge of Φ the lifting holds with no padding
  at all. The whole residual is how far the coverage partner of the identity is from the identity.
- **τ_min ≤ φ.** Φ = c′(P) is an available single-outcome family and id is a channel, so
  τ_min ≤ ‖Φ − id‖ = φ(c′) for every admissible c′, hence τ_min ≤ φ_min, where φ_min is the
  infimum of φ over admissible c′. A theory with M_C < ε and τ_min > 0 therefore has
  φ(c′) ≥ τ_min for every admissible c′. Unit 3's obstruction can bite only there.
- **Norm control: necessary; sufficiency open at small η.** Under (U-a),
  sup‖F‖ ≤ 1 + (1+φ)κ_snd + φ, so a small φ gives norm control. The converse does not hold without
  the structure rules at small η: Prop X2 has ‖c′(P)‖ = 1 and φ = 2, but it lies in class(η) only
  for η_a, η_c, η_d, η_e ≥ 2. In class(η) at small η, whether a bounded ‖c′(P)‖ gives φ → 0 is
  open (UN-1). The single residual is φ. Its norm part ‖c′(P)‖ is the part W4 isolates.

## 4. The system under rule (a)

**Prop S [A].** On the system, let I′ be an available single-outcome family with
‖I′ − id‖ ≤ η_a < 1 (rule (a) in class(η)). Then ‖Φ^{-1}‖ ≤ C_G/(1 − η_a), and
‖Φ^{-1} − c̃(I′)‖ ≤ δ_S := κ_snd + C_Gη_a/(1 − η_a), with c̃(I′) a quantum channel.

*Proof.* Theorem G gives ‖Φ^{-1}I′‖ ≤ C_G, and ‖I′^{-1}‖ ≤ 1/(1 − η_a) (Neumann series [L]).
Lemma 7G gives ‖Φ^{-1}I′ − c̃(I′)‖ ≤ κ_snd, and ‖Φ^{-1}(I′ − id)‖ ≤ ‖Φ^{-1}‖η_a. □

So on the system Φ^{-1} lies within δ_S of the quantum channel Q_I := c̃(I′). Write
R := Φ^{-1} − Q_I, so ‖R‖ ≤ δ_S. Two one-directional perturbation bounds follow from Neumann
series [L], each with its own condition:
- if Q_I is invertible and δ_S‖Q_I^{-1}‖ < 1, then ‖Φ‖ ≤ ‖Q_I^{-1}‖/(1 − δ_S‖Q_I^{-1}‖), since
  Φ^{-1} = Q_I(id + Q_I^{-1}R);
- if δ_S‖Φ‖ < 1, then Q_I is invertible and ‖Q_I^{-1}‖ ≤ ‖Φ‖/(1 − δ_S‖Φ‖), since
  Q_I = Φ^{-1}(id − ΦR).

δ_S ≈ κ_snd + 8η_a/(1 − η_a) is small only when η_a and ε are, so neither condition is supplied
by the hypotheses. A contracting Q_I (for instance, one close to a depolarizing channel) is not
excluded; that is node UN-1.
At levels there is no identity rule (unit 2 §3.2 records this), so even the bound on ‖Φ^{-1}‖ is
not obtained there.

## 5. Countercontrols

**CC-s (rescaled QM, unit 3's item D1, `../unit3/PRESERVATION.md` §7, partially verified) [A].** In T_s every available family is (1+s)J.
The single-outcome protocol of K copies of (1+s)·id has law (1+s)^K, while every quantum law of a
single-outcome protocol is 1. So the soundness term is at least ((1+s)^K − 1)/2 ≥ Ks/2, and T_s
satisfies M_C < ε only when s < 2ε/K. In that range τ_min = s is of order ε/K, and Theorem G and
Lemma 7η both apply. **T_s is not a CC-L candidate.** Unit 3's statement that class(η) contains
theories with τ_min > 0 stands. This result adds that T_s does not meet the converse's hypothesis
M_C < ε unless τ_min < 2ε/K.

**Prop X1 (gauge conjugates are excluded) [A].** Let S be an invertible linear map on the level's
matrices with tr∘S = tr, and T_S := {S∘J∘S^{-1} : J a quantum instrument}. If M_C(T_S, Q) < ε <
1/16 with m, K ≥ 2, then ‖S^{-1}‖ ≤ 8(1+2ε), ‖S‖ ≤ 4/(1−16ε), and every available family has
norm at most 32(1+2ε)/(1−16ε).

*Proof.* Since tr∘S = tr, every T_S-law is the quantum law of the corresponding quantum protocol
at input S^{-1}ρ.
1. The protocol (S M_E S^{-1}, id^{K−1}), with id = S P S^{-1}, has law
   (tr(ES^{-1}ρ), tr((1−E)S^{-1}ρ)). F1 gives |tr(ES^{-1}ρ)| ≤ 1 + 2ε for every E, so
   ‖S^{-1}ρ‖₁ ≤ 4(1+2ε) and, by the four-part split, ‖S^{-1}‖ ≤ 8(1+2ε).
2. The coverage partner of (M_E, P^{K−1}) is a T_S-protocol whose first entry is tr(Γ S^{-1}ρ)
   for a quantum effect 0 ≤ Γ ≤ 1. TV ≤ ε gives ‖(S^{-1})†Γ − E‖_op ≤ 4ε. For any X,
   |tr(EX)| ≤ ‖S^{-1}X‖₁ + 4ε‖X‖₁, and maximizing over E gives ‖S^{-1}X‖₁ ≥ ¼(1 − 16ε)‖X‖₁.
3. ‖S J S^{-1}‖ ≤ ‖S‖·‖S^{-1}‖. □

*Control of Prop X1.* Take S^{-1} = C_p, the depolarizing channel C_p(X) = (1−p)X + p tr(X)·1/N
(N ≥ 2). Step 2 at ρ = |0⟩⟨0| (with E = |0⟩⟨0|) and at ρ = |1⟩⟨1|, with Γ ≤ 1, forces
p·tr Γ/N ≤ 2ε and p·tr Γ/N ≥ p − 2ε, so p ≤ 4ε. Then
‖S‖ = ‖C_p^{-1}‖ ≤ (1+p)/(1−p) ≤ (1+4ε)/(1−4ε), within the proposition's bound. Coverage excludes
the large-norm gauge (p near 1); the bound's slack plays no part.

*Why the argument does not extend.* Step 2 bounds S^{-1} from below because the coverage
partner's effect Γ is a quantum effect, of operator norm at most 1. For a general T the
corresponding effect is that of a T-protocol, whose norm is the quantity sought. This is the
obstruction in its shortest form (marker W5, §8).

**CC-p (the coverage term is load-bearing) [A].** Take N ≥ 2 and S^{-1} = C_p, so
T_S = {C_p^{-1}∘J∘C_p}; class membership is not claimed. tr∘C_p^{-1} = tr, so every T_S-law is a
quantum law at the input C_pρ, which is a density. Every law is therefore a probability vector,
and F1's conclusion holds exactly, with nothing left over.
- *Norms.* For the replacement channel J(X) = tr(X)|0⟩⟨0|,
  C_p^{-1}JC_p(X) = tr(X)·C_p^{-1}(|0⟩⟨0|). The matrix C_p^{-1}(|0⟩⟨0|) has eigenvalues
  (1 − p/N)/(1−p) once and −p/(N(1−p)) N − 1 times. Its trace norm, and hence the family's norm,
  is (1 + p(N−2)/N)/(1−p) ≥ 1/(1−p), unbounded as p → 1.
- *Coverage.* The control of Prop X1, step 2, shows that coverage within ε of (M_E, P^{K−1}), with
  E = |0⟩⟨0|, forces p ≤ 4ε. So the coverage term is at least p/4.

F1 alone does not bound the norms; whether the soundness term alone does is not tested by CC-p.
Prop X1's norm conclusion fails for T_S at p near 1 while its step 1 premise holds, and the
coverage term (through Lemma R in Theorem G, and through step 2 in Prop X1) excludes T_S. CC-p is a countercontrol for Prop X1. It is not
claimed to violate Theorem G, which is stated in the gauge of a coverage partner and so presupposes
the coverage term.

**Prop X2 (bounded norms, converse fails) [A].** Let K be even, and T_− := {−J : J a quantum
instrument} at every level and on the system, with the completely positive, trace-preserving
preparations. Every T_−-law of horizon K equals the corresponding quantum law, so
M_C(T_−, Q) = 0 with c(−J) = J and c′(J) = −J, for every m. Every available family has norm 1.
For every quantum instrument J′, ‖−J − J′‖ ≥ |tr(−J(ρ) − J′(ρ))| = 2, so the conclusion of Lemma 7
fails for every pair of correspondences. The same holds for T_ω := ωQ with ω^K = 1, ω ≠ 1.

T_− satisfies rules (b) and (f) exactly (with these preparations), and rules (a), (c), (d) and (e)
only at η_r = 2: each exact object is at distance 2 from every available one. So T_− lies in
class(η) only when η_a, η_c, η_d, η_e(n) ≥ 2, which is the scale at which any two norm-one families
are within η. It is consistent with unit 3: τ_min(T_−) = 2, so (Hg) fails and Lemma 7η does not
apply. Its role here is to show that M_C < ε with m, K ≥ 2 does not by itself imply the converse,
even with bounded norms. The structure rules at small η carry the converse, and the residual is φ
(here φ = 2), not the norm alone. **Prop X2 is not CC-L**: its norms are not large.

**Necessary conditions for CC-L [A].** By Theorem U and Corollary G1, a CC-L theory (Lemma 7's
conclusion failing for every admissible pair, with g of order 1/τ_min) must have, for every
admissible c′: φ(c′) not small, ‖c′(P)‖ ≥ g/C_G, and φ(c′) ≥ τ_min. No
theory with these properties and small η was found. **CC-L: open.**

## 6. U3: an operational candidate for φ

The candidate is an **idle step**: at each level, an available single-outcome family within η_id
of the identity. Operationally it is the observer's option of applying no operation between two
records, and it refers only to the kinematics. On the system it is rule (a) of class(η); at levels
it is not among the six rules.

What it gives: Prop S at each level, that is, Φ^{-1} within δ_S of a quantum channel Q_I, with
‖Φ^{-1}‖ bounded; the two directions of Prop S's perturbation bounds keep their conditions. What it does not give: a bound on ‖Q_I^{-1}‖, hence on ‖Φ‖ or φ.

Two routes were tried.
- The first replaces c′(P) by the idle family I′ itself. Its coverage term would need the laws
  with I′ at the idle steps to stay close to those with Φ. The difference is paired with un-gauged
  tail effects, which are the quantity sought.
- The second inserts a measure-and-prepare instrument after Φ, so that its output no longer
  depends on Φ's gauge. It gives an estimate of the form u ≤ |t|^{-1}(1 + O(ε)·‖Φ^{-1}‖·u) for
  u = sup_ρ‖Φρ‖₁, with t fixed by the K-fold trace condition. Its error is linear in u with
  coefficient O(ε), not O(τ_min), but it enters through a K-th power. So it excludes only a window
  of u, not the large branch. This route is a sketch, not claimed.

The idle step is therefore recorded as a **candidate premise** whose sufficiency is open. It is
not adopted; adoption would be the owner's (§A.29, §A.50 item 6).

## 7. Open nodes

| ID | Node | Status |
| --- | --- | --- |
| UN-1 | Does M_C < ε (m, K ≥ 2) in class(η) at small η imply φ_min → 0, or a bound on ‖c′(id)‖? This is unit 3's O2-a in its reduced form (Theorem U) | open |
| UN-2 | Does an idle step at each level (§6) imply φ_min = O(ε + η_id)? | open; candidate premise, not adopted |
| UN-3 | CC-L: a theory with small η, M_C < ε, and φ(c′) bounded away from 0 for every admissible c′ | open; gauge conjugates and T_s excluded, Prop X2 only at η ≥ 2 |
| UN-4 | Does Theorem G hold at levels with a gauge chosen independently of c′ (an available near-identity, if any)? | open |
| UN-5 | Optimal constants in Theorem G and Lemma 7G | open; not needed for any status |

## 8. Classification (§A.31) and markers

- Theorem G, Lemma 7G and Theorem U: **NEW**. Under M_C, the converse needs no padding in the
  gauge of c′(id), and its whole residual is one family's distance from the identity. The padding
  obstruction of unit 3 §5.3 (W4) is a property of that route, not of the converse.
- Prop X2: **NEW**. M_C < ε at m, K ≥ 2 does not imply the converse without the structure rules
  at small η, even with norms bounded by 1 (T_− lies in class(η) only at η ≥ 2). Norm control is
  necessary (Theorem U). Whether it is sufficient in class(η) at small η is open (UN-1).
- Prop X1 and CC-s: **ELABORATING**. They exclude two candidate countercontrols.
- CC-p: **ELABORATING**. It shows that the coverage term is load-bearing for Prop X1.
- §6: **BORDERLINE**. It records a candidate premise and a sketch.

Outcome (`PLAN.md` §6): N2, a relative bound with the residual named in both directions, together
with a sharpened obstruction.

The favourable branch, Theorem G, was pressure-tested on four points:
1. The adaptive choice of E_a is made after (F, ρ) are fixed. The correspondences are fixed before
   the supremum over protocols, so each protocol may carry its own E_a.
2. Every protocol has horizon exactly K and at most m outcomes per step.
3. The soundness term is used only through F1, and the coverage term only in Lemma R and Lemma 7G.
4. C1 is respected: m ≥ 2 enters through M_E, K ≥ 2 through the tail, and nothing is stated across
   levels.

Theorem G is not read as norm control in the trace norm. Corollary G1 and Prop X2 state exactly
what it gives and what it does not.

**Assumption-watch marker W5 (gauge of the identity).** Under a correspondence metric the laws fix
the available families only up to the chosen correspondence's coverage partner of the identity,
which is not unique, so statements in the trace
norm need that partner to be near the identity. Wherever an argument bounds T-side effects by 1,
check whether the effect is a quantum effect (as in Prop X1) or a T-protocol's (where the bound is
the question). This refines W4 of unit 3.

## 9. Controls (`PLAN.md` §4)

| Control | Check | Status |
| --- | --- | --- |
| C0 | At T = Q with c = c′ = id: Φ = id, φ = 0, Ψ = id, c̃ = c. Theorem G gives ‖F‖ ≤ C_G, true since ‖F‖ = 1. Theorem U gives κ_snd → 160ε and κ_cov → 144ε as ε → 0, consistent asymptotically with unit 2's 160ε and 184ε; at ε = 1/48, C_ρ = 6.25 and κ_cov = 216ε exceeds 184ε, so the comparison is asymptotic only. Where τ_min = 0, Corollary 7c [U3] gives the coverage bound 184ε, so φ ≤ 184ε, consistent with Theorem U (U-b) | green |
| C1 | No statement drops m ≥ 2 or K ≥ 2, uses M_H, or crosses levels. Prop X2 and Theorem 5 [U2] are both failures of the converse without the structure rules, under different metrics | green |
| CC-s | T_s [D1] violates M_C < ε unless s < 2ε/K (§5) | checked |
| CC-p | T_S with S^{-1} = C_p, p near 1: F1 holds exactly, the coverage term is at least p/4, and norms are unbounded. F1 alone does not bound the norms; whether the soundness term alone does is not tested by CC-p (§5) | green |
| CC-L | Two subclasses excluded, necessary conditions proved, no realization (§5) | open |

All verdicts above are printed over the green controls C0 and C1.

## 10. Inputs and off-`main` references (§A.42 item 8)

| Input | Label | Use |
| --- | --- | --- |
| Unit 2: metrics and quantifier order of M_C, N1, N5, Lemma 7 step B, Theorem 8's proof, Theorem 5, Propositions 9 and 11 | [U2], on `main` | Setting, F2, Lemma 7G, Theorem U's Theorem 8, C1 |
| Unit 3: η-model, τ_min, Lemma 7η, (Hg), Corollary 7c, §5.1, §5.2, §5.3, W4 | [U3], on `main` | Question, C0, Corollary G1's routing note, consistency of Prop X2 |
| Unit 3 `PRESERVATION.md` §7, item D1 (T_s): review-originated, partially verified, not part of unit 3's report | [D1], on `main` | CC-s (definition and τ_min = s only) |
| PR #1614 review of r1 (verbatim on the PR) | provenance | Findings 1–9 applied here; no result uses its content as support |
| Neumann series, trace duality | [L] | Prop S, notation |
| #1169 comments 7200549806, 7199704501, 7191949320 | provenance | Authority and question; no result uses them |

Every support is on `main` at the pin. Support off `main`: none.
