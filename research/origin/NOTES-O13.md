# NOTES-O13 — is the Kochen–Specker sphere tower's re-preparation law realizable by an `InstAvail` protocol?

Thread `research/origin`, round 4, node O13. Base L = `9f9f8257`; kernel paths under
`verification/lean-mathlib/OIBridge/` at L. Evidence levels as in NOTES-O1. Script: `experiments/o13_ks.py`. No design
module: the round's three dispatches are used (O11, O12 and O12's repair), so O13 is written ([W]) with exact checks
([X]) and the kernel lines it cites ([K]).

Kernel objects. `InstAvail` (ImplementationLocality.lean:268) and `Realized` (:250: a finite sum of conjugations by
members of the class at the carrier); `realized_of_instAvail` (:530: every branch of every `InstAvail` family of an
architecture is realized, the discard taking contractive blocks); the native readout `readout_is_localLuders`
(OperationalAssembly.lean:658: the theory's readout at level n is exactly the rank-one Lüders selector on the ancilla,
identity on the system); `pureSeedPrep_available_of_swap` (:675: read the uniform ancilla, correct by the exchanges,
forget the outcome — a re-preparation of a configuration state); `mixR_countable_upToScalar` (StateMixingCoupling.lean:662).

**The law, in the kernel's vocabulary.** On the token's carrier (the qubit, Fin 2; with ancillas, any carrier whose
token-level family is obtained by discard), the Kochen–Specker sphere tower's readout along a unit vector n ∈ S² with
its cosine re-preparation is, on the completed body (the Bloch ball, O6-I, O10-T1), the instrument
F^n_± (ρ) = tr(Π^n_± ρ) Π^n_±, Π^n_± = (1 ± n·σ)/2: outcome probability (1 ± ψ·n)/2 and post-state the pure state ±n,
whatever the input. "Realizable by an `InstAvail` protocol with ancillas" is read as: some `InstAvail` family of the
theory's class at the token's carrier equals (F^n_+, F^n_−). Only the operational law is at issue; the hidden-variable
re-preparation on the continuous sphere is not a kernel object.

**Productivity test, fixed before starting (§A.31).** A finding counts only if it is strictly stronger than O10-T1's
label ("CONDITIONAL on the cosine re-preparation law; outside the stated access; O8: false there") and either (i) decides,
for the stated access and for the fixed-gate theories, along which axes the law is realizable, by an argument covering
every `InstAvail` protocol with ancillas, or (ii) names exactly what a class must contain for the law to be realizable
along every axis, with a construction showing sufficiency. A restatement of "outside the stated access" is a non-gem.

**The suspected hidden assumption, recorded before any computation.** That a re-preparing readout is an observation
law — something a theory could have in addition to its operations. In the kernel every branch of every available family
is a sum of conjugations by class members (`realized_of_instAvail`), and a branch that re-prepares a pure state whatever
the input has, in every Kraus form, only multiples of one rank-one projector. So the law along n is an operation datum:
it needs a member ∝ Π^n_+ in the class. Suspected: on the stated access only the configuration axis passes; a class
countable up to scalar passes countably many axes; the full sphere needs an uncountable family of coherent members.

## S0 — predictions, written before the first run of `o13_ks.py` (2026-10-11T04:50:02Z)

Written argument, predicted to hold:

- **W1 (Kraus form).** If F(ρ) = tr(Π ρ) Π for every ρ, with Π a rank-one projector, then every finite family K_i with
  F = Σ_i conj(K_i) has K_i = c_i Π, Σ|c_i|² = 1 (the Choi matrix of F has rank one).
- **W2 (the no-go form).** If (F^n_+, F^n_−) is an `InstAvail` family of an architecture 𝓘 at the token's carrier, then
  𝓘 contains a nonzero multiple of Π^n_+ and of Π^n_− there (`realized_of_instAvail` with W1).
- **W3 (the stated access).** Π^n_± is submonomial exactly when n = ±z; so on every configuration-level class (the
  stated access) the law is realizable along the configuration axis only, at every carrier and with every ancilla; along
  that axis it is realized by the native readout after the exchange (`readout_is_localLuders`).
- **W4 (fixed gates).** For a class countable up to scalar at the carrier (the fixed-gate theories at every angle,
  `mixR_countable_upToScalar`) the law is realizable along at most countably many axes, so the sphere tower's law —
  every n ∈ S² — is not realizable, even where unitary control is dense (irrational angles).
- **W5 (sufficiency).** If 𝓘 contains a unitary U at the carrier with U|0⟩ ∝ |n+⟩ (and the configuration projectors),
  the law along n is realized by: the step U†, the configuration readout, the step U, coarse-grained to two outcomes.
  In the full class, along every n.

Exact script (sympy, exact radicals):

- **K1.** Over the test axes z, −z, x, y, (4/5, 0, 3/5), (3/5, 4/5, 0), (2/3, 1/3, 2/3), (0, 3/5, 4/5): Π^n_+ is
  submonomial exactly for z and −z.
- **K2.** For each test axis the Choi matrix of F^n_+ has rank 1 and is proportional to vec(Π^n_+) vec(Π^n_+)†; the
  Choi matrix of the summed channel F^n_+ + F^n_− has rank 2.
- **K3.** For each test axis, with U_n the explicit SU(2) matrix taking |0⟩ to |n+⟩, the composite
  conj(U_n) ∘ conj(P_±) ∘ conj(U_n†) equals F^n_± on all four matrix units.
- **K4.** The rank-one Lüders selectors on the configuration basis equal F^z_± (the native readout is the law along z).
- **K5.** At the Clifford angle π/4 the axes U Z U† over the 24 level-one classes are exactly the six octahedral axes
  ±x, ±y, ±z; at π/8 the orbit of z under the level-one group has more than 1000 axes within the first 3000 classes
  (infinite: O12), all with coordinates in ℤ[ζ₁₆][1/2].
- **Positive controls (expected True).** PC1 Π^z_+ is submonomial; PC2 K3 at n = x.
- **Countercontrols (each expected False).** CC1 the submonomial test accepts Π^x_+; CC2 the construction with U_n
  replaced by U_n† reproduces the law along an axis with n_y ≠ 0; CC3 the Choi rank of F^n_+ + F^n_− is 1; CC4 the axis
  (4/5, 0, 3/5) is among the π/4 axes.

Decision rule (fixed in the script's header before run 1): `VERDICT O13-KS-LAW-NEEDS-A-COHERENT-MEMBER-PER-AXIS` if
K1–K5 hold, PC1–PC2 are True and CC1–CC4 are False; `VOID` if a control fails; `UNDECIDED` otherwise.

**S0 addendum (2026-10-11T04:53:08Z, before the script exists and before run 1).** Two corrections to the S0 above,
made on reflection before any computation. (a) K5 is an illustration about *unitary conjugation only*: the axes U z for
U in the level-one group. It is not a realizability claim for the law, because a class member ∝ Π^n_+ need not be a
unitary conjugate of a configuration projector — it may be a block of a member at a higher level (a dilation). So W4's
countable bound stands, but which axes a fixed-gate class passes is not decided here, and CC4 is read as "the axis
(4/5, 0, 3/5) is a unitary conjugate of z at π/4" (expected False). (b) At π/8 the stabilizer of the z-axis in the
level-one group, taken modulo scalars, has order 8 (rotations about z by multiples of π/4), so 3000 classes give about
375 axes, not more than 1000; K5 at π/8 is revised to "more than 100 distinct axes U z within the first 3000 classes".
The decision rule is unchanged.

Run 1 of `o13_ks.py` (2026-10-11T04:55:02Z, 3 s): `VERDICT O13-KS-LAW-NEEDS-A-COHERENT-MEMBER-PER-AXIS` — K1–K5 True,
PC1–PC2 True, CC1–CC4 False; replay byte-identical. One pre-run edit before any run: `U_of` converted the axis's third
coordinate with `sp.Integer`, which would have truncated 3/5 to 0; changed to `sp.sympify`. Every S0 prediction met except
one estimate of the addendum: at π/8 the first 3000 classes give 774 distinct axes, not "about 375" (the coset count
holds for complete cosets only; a BFS ball holds many partial ones); the decision quantity "more than 100" is met.

## 0. Verdict

Every statement below is an **availability** statement (what an `InstAvail` protocol of a class can do), never a
cone-invariance one. The law along every axis is cone-preserving — each F^n is a valid quantum instrument on the ball —
and is available on the stated access along one axis only: an instance of addendum 3's distinction.

1. **W1, the Kraus form** [W; X K2]. If F(X) = tr(Π X) Π for every X, with Π a rank-one projector, every Kraus family of F
   consists of multiples of Π: the Choi matrix of F is Πᵀ ⊗ Π, of rank one, so every Kraus operator is a multiple of one
   operator K, and F = |c|² conj(K) forces K ∝ Π. The summed channel F^n_+ + F^n_− has Choi rank two [X K2].
2. **W2, the no-go form** [K ImplementationLocality.lean:250, :530; W]. If (F^n_+, F^n_−) is an `InstAvail` family of an
   architecture 𝓘 at the token's carrier — every protocol allowed: steps, readouts, coarse-graining, feed-forward, and
   ancillas attached uniformly and discarded — each branch is `Realized` (`realized_of_instAvail`): a finite sum of
   conjugations by members of 𝓘 at the carrier, ancilla blocks included. By W1 each such member is a multiple of
   Π^n_±, and one of them is nonzero. So **the law along n is available only if 𝓘 contains a nonzero multiple of Π^n_+
   (and of Π^n_−) at the token's carrier**: a re-preparing readout is an operation datum, not an observation law.
3. **The stated access: the configuration axis only** [D + K + X + W]. Π^n_+ is submonomial exactly when n = ±z [X K1:
   its off-diagonal entry is (n_x − i n_y)/2 and its diagonal entries (1 ± n_z)/2]. Every member of a configuration-level
   class is submonomial (I4.242; the substratum class, `substratumClass_configurationLevel` [K ManuscriptAxioms.lean:129]),
   so on the stated access the law is available along ±z and along no other axis — at every carrier, with every ancilla.
   Along z it is available, and it is the native readout: the rank-one Lüders selectors on the configuration basis are
   F^z_± [X K4], and the theory's native readout is exactly the rank-one Lüders selector on the ancilla
   (`readout_is_localLuders` [K OperationalAssembly.lean:658]), reached on the token through the exchange. The same
   conclusion follows from O11-T1's `reach_diag_of_submonomial` [D run 38108620996]: the law's branch on a configuration
   state outputs the coherent state Π^n_± with positive weight when n ≠ ±z.
4. **Fixed gates: countably many axes; the sphere tower's law is not available, even with dense control**
   [K StateMixingCoupling.lean:662; W]. For a class countable up to scalar at the carrier — `MixR D` with D countable,
   so `fixedGateTheory α` at every angle — the multiples of the Π^n_+ in the class form countably many rays, so the law
   is available along at most countably many axes; the sphere tower's law, along every n ∈ S², is not available in any
   such theory — at an irrational angle too, where `DenseUnitaryControl` holds (`fixedGateTheory_denseUnitaryControl`
   [K DiscreteCompletion.lean:1942]). Illustration, unitary conjugation only [X K5]: at π/4 the axes U z over the level-one
   group are exactly the six octahedral axes; at π/8 the first 3000 classes give 774 axes, and the orbit is infinite (O12).
   Which axes a fixed-gate class passes through non-unitary members (blocks of higher-level members, i.e. dilations) is not
   decided here.
5. **Sufficiency** [W; X K3]. If 𝓘 contains at the carrier a unitary U with U|0⟩ ∝ |n+⟩ together with U†, the law along
   n is available: the step U†, the configuration readout, the step U, coarse-grained to two outcomes, gives
   X ↦ U P_s U† X U P_s U† = F^n_s(X) [X K3: exact at all eight test axes, including (4/5, 0, 3/5) and (2/3, 1/3, 2/3)].
   In the full class (`fullClass`, every matrix admissible) the law is available along every axis.
6. **Answer to O13.** The Kochen–Specker sphere tower's re-preparation law is realizable by an `InstAvail` protocol with
   ancillas exactly so far as the class supplies, at the token's carrier, a coherent rank-one member Π^n_+ for each axis n
   of the law: on the stated access, along the configuration axis only (no-go off that axis, in O8's style: the native
   readout is the local Lüders selector, and nothing else in the protocols can re-prepare a coherent state); with any
   fixed gate, along countably many axes, never along all of S²; in the full class, along all. The sphere tower's law
   presupposes an uncountable family of coherent members — the coherence of SRC and the continuum at once.

## 1. Hypotheses, by kind (the coordinator's rule)

| statement | hypotheses | kind | form |
|---|---|---|---|
| W1 | none (a statement about completely positive maps) | — | mathematical |
| W2 | an architecture (I4.32), `InstAvail` (I4.26), `Realized` and its theorem (I4.25) | (i) | OI ⇒ (the law along n available ⇒ a member ∝ Π^n_+) |
| item 3 | the substratum class (I4.44), its generated theory (I4.240), configuration level (I4.242, discharged [K ManuscriptAxioms.lean:129]) | (i) | OI ⇒ the law is not available off the configuration axis on the stated access |
| item 4 | the gate at α (`MixR {α}`, I4.175) | the gate: introduced, not an OI premise (I4.239) | OI + {the gate at α} ⇒ at most countably many axes |
| item 5 | a class containing U and U† at the carrier | introduced (a coherent unitary), not an OI premise | OI + {U, U†} ⇒ the law along n |
| the law itself (the cosine re-preparation law) | — | introduced, not an OI premise (addendum 1's list) | the object tested, never a premise |

## 2. Disguise test of the law as a candidate source

- *Letter:* fails. Off the configuration axis the law's branch is conjugation by Π^n_±, a non-monomial operator and a
  coherent state of the matrix carrier; the law names coherence in the form of its re-prepared states.
- *Kernel carrier:* failed as an independent source: by W2 it is available only where the class already holds a coherent
  member per axis, i.e. it presupposes the coherence (SRC's content, O11-T5) and, for the sphere, a continuum of it. On
  the sphere tower it then supplies J and R_z(θ₀) (O10-T1), but only by assuming them in this form.

## 3. Alternatives defeated (the coordinator's rule for O12–O13, in those words)

- The re-preparation law, unavailable off the configuration axis on the stated access, defeats *"the Kochen–Specker
  re-preparation law is available on the stated access, so the sphere tower's token pair (J and R_z(θ₀)) is sourced
  there"*.
- Its unavailability along all of S² with any fixed gate defeats *"a fixed gate with dense unitary control realizes the
  sphere tower's re-preparation law"*.
- Its availability exactly per coherent member defeats *"a re-preparing readout is an observation law a theory can have
  besides its operations"*.

## 4. Classification (§A.31)

The productivity test is met: (i) the stated access and the fixed-gate theories are decided by an argument covering
every `InstAvail` protocol with ancillas; (ii) what a class must contain is named (a nonzero multiple of Π^n_+ per axis;
with U and U†, sufficient), with an exact construction.

- **NEW, O13-N1.** In the kernel a re-preparing readout is an operation datum: the law along n is available only through a
  class member ∝ Π^n_+ at the token's carrier. O10-T1's condition ("CONDITIONAL on the cosine re-preparation law") is
  thereby a condition on the class, not on observation.
- **NEW, O13-N2 (assumption-watch marker).** Dense unitary control does not give exact re-preparation: no class countable
  up to scalar realizes the sphere tower's law, although `DenseUnitaryControl` holds at irrational angles. An exact law
  along a continuum of axes needs a continuum of members.
- **CONFIRMING.** O8 (the native readout is the local Lüders selector); O11-T1 (the reachable states of the stated access
  are configuration-diagonal); O10-T1's label (outside the stated access), now with its reason.

## 5. Open

- Which axes a fixed-gate class passes through dilations (non-unitary members from higher levels) is not decided; the
  countable bound is all that is claimed.
- W1, W2, W5 are written; their kernel forms (the Choi rank and `realized_of_instAvail` composed) are not checked — no
  dispatch was left this round.
