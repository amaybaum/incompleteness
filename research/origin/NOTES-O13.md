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
