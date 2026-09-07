import OIBridge.FrozenSourcing
import OIBridge.CanonicalMeasure

/-!
# The stochastic observer-interface determination audit — does the architecture fix a map and an ensemble?

The preregistered pass of `STOCHASTIC-OBSERVER-INTERFACE-AUDIT.md`, read under its scope amendment.
Stage 1 asks whether the stated architecture determines the observation map and the initial
ensemble; the induced process and the divisibility predicates of stage 2 are defined only if it
does. No correspondence theorem is stated, cited as a premise, or used, and no predicate for one is
defined here. Nothing is named "C5"; nothing is added to the substratum and nothing added anywhere
is reported as sourced; the census core's visible map is not carried to the configuration space;
neither the map nor the ensemble is selected for the answer it would yield.
-/

namespace OIBridge
namespace StochasticInterface

open Complex Matrix CoherentLift OperationalAssembly InterventionLocality MonoidalCompletion
open RouteB SubstratumInterface SubstratumInterfaceAudit SecondOrderLayer SecondOrderCircuit
open ReadWriteControl CanonicalMeasure FrozenSourcing

/-! ### Section A — what "the ensemble is determined" would mean -/

section Determination

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- **THE ENSEMBLE IS DETERMINED BY INVARIANCE**: exactly one probability law on the state space is
invariant under the dynamics. This is the only ensemble constraint the architecture states, so it
is the predicate the census must test; it is not a new principle and nothing here selects a law. -/
def EnsembleDetermined (φ : Equiv.Perm S) : Prop :=
  ∃! p : S → ℝ, IsProb p ∧ Invariant φ p

/-- **A TRANSITIVE DYNAMICS DETERMINES ITS ENSEMBLE**, by the kernel's single-orbit uniqueness:
when one orbit exhausts the state space, the invariant law is the uniform law on it and there is no
other. This is the positive route the scope amendment records, and it is derived, not chosen. -/
theorem ensembleDetermined_of_transitive (φ : Equiv.Perm S) (s : S)
    (htr : ∀ t : S, t ∈ orbit φ s) : EnsembleDetermined φ := by
  refine ⟨unif (orbit φ s), ⟨unif_isProb _ (orbit_nonempty φ s), ?_⟩, ?_⟩
  · exact unif_invariant φ (orbit_mapsTo φ s)
  · rintro q ⟨hprob, hinv⟩
    exact orbit_invariant_unique φ s q hinv hprob (fun t ht => absurd (htr t) ht)

/-- **TWO DISJOINT INVARIANT SETS LEAVE THE ENSEMBLE UNDETERMINED**, the kernel's guard read as a
statement about determination. -/
theorem not_ensembleDetermined_of_disjoint (φ : Equiv.Perm S) {A B : Finset S}
    (hA : A.Nonempty) (hB : B.Nonempty) (hAm : ∀ x ∈ A, φ x ∈ A) (hBm : ∀ x ∈ B, φ x ∈ B)
    (hdisj : Disjoint A B) : ¬ EnsembleDetermined φ := by
  rintro ⟨r, -, huniq⟩
  obtain ⟨p, q, hpi, hqi, hpp, hqp, hpq⟩ :=
    invariance_does_not_select φ hA hB hAm hBm hdisj
  exact hpq ((huniq p ⟨hpp, hpi⟩).trans (huniq q ⟨hqp, hqi⟩).symm)

/-- **A FIXED POINT BESIDE ANY OTHER STATE LEAVES THE ENSEMBLE UNDETERMINED**: the fixed point and
the orbit of any other state are disjoint nonempty invariant sets. -/
theorem not_ensembleDetermined_of_fixedPoint (φ : Equiv.Perm S) {x y : S} (hx : φ x = x)
    (hxy : y ≠ x) : ¬ EnsembleDetermined φ := by
  refine not_ensembleDetermined_of_disjoint φ (A := {x}) (B := orbit φ y)
    (Finset.singleton_nonempty x) (orbit_nonempty φ y) ?_ (orbit_mapsTo φ y) ?_
  · intro z hz
    rw [Finset.mem_singleton] at hz
    rw [hz, hx]
    exact Finset.mem_singleton_self x
  · refine Finset.disjoint_left.mpr fun z hz hzo => ?_
    rw [Finset.mem_singleton] at hz
    obtain ⟨n, hn⟩ := (mem_orbit φ y z).1 hzo
    -- the fixed point is not on the orbit of any other state, since `φ` is a bijection
    refine hxy ?_
    have hpow : ∀ m : ℕ, (φ ^ m) x = x := by
      intro m
      induction m with
      | zero => rfl
      | succ k ih => rw [pow_succ', Equiv.Perm.mul_apply, ih, hx]
    have hyx : (φ ^ n) y = (φ ^ n) x := by rw [hn, hz, hpow n]
    exact (Equiv.injective (φ ^ n)) hyx

end Determination

/-! ### Section B — the substratum's dynamics has a fixed point under A5 -/

section FixedPoint

variable (𝒮 : Substratum)

/-- **AN ADDITIVE RULE FIXES THE ZERO CONFIGURATION.** Additivity gives `F 0 = 0`, and the
phase-space step `(p, c) ↦ (c, F c − p)` then fixes the all-zero configuration. A5 is one of the
architecture's own stated axiom predicates, not an addition. -/
theorem phi_fixes_zero (h5 : 𝒮.A5) : 𝒮.φ 0 = 0 := by
  have hF0 : 𝒮.R.F 0 = 0 := by
    have h := h5 0 0
    rw [add_zero] at h
    simpa using h.symm
  funext i
  show ((0 : 𝒮.Conf) i |>.2, 𝒮.R.F (curOf (0 : 𝒮.Conf)) i - ((0 : 𝒮.Conf) i).1) = (0 : 𝒮.V × 𝒮.V)
  have hcur : curOf (0 : 𝒮.Conf) = 0 := rfl
  rw [hcur, hF0]
  simp

/-- **THE WAVE RULE FIXES THE ZERO CONFIGURATION**, since it satisfies A5. -/
theorem waveSubstratum_phi_fixes_zero (d L q : ℕ) [NeZero L] [NeZero q] (α : ZMod q) :
    (waveSubstratum d L q α).φ 0 = 0 :=
  phi_fixes_zero _ (waveSubstratum_A5 d L q α)

end FixedPoint

/-! ### Section C — T3: the ensemble leg -/

section EnsembleLeg

variable (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V]

/-- **THE ENSEMBLE LEG FAILS FOR EVERY SUBSTRATUM WITH A LINEAR RULE AND MORE THAN ONE
CONFIGURATION.** The zero configuration is fixed, so it and the orbit of any other configuration
are disjoint nonempty invariant sets, and invariance leaves the law undetermined. The architecture
states A5 and states no ensemble beyond invariance, so nothing here selects a law and nothing is
added. -/
theorem ensemble_underdetermined (h5 : 𝒮.A5) {y : 𝒮.Conf} (hy : y ≠ 0) :
    ¬ EnsembleDetermined 𝒮.φ :=
  not_ensembleDetermined_of_fixedPoint 𝒮.φ (phi_fixes_zero 𝒮 h5) hy

/-- **THE MANUSCRIPTS' WAVE SUBSTRATUM LEAVES ITS ENSEMBLE UNDETERMINED**, on every torus whose
alphabet has more than one letter. The witness for the second orbit is the constant configuration
carrying the alphabet's unit in the past coordinate; no configuration is chosen for the verdict it
would yield, and any configuration other than zero serves equally. -/
theorem waveSubstratum_ensemble_underdetermined (d L q : ℕ) [NeZero L] [NeZero q]
    [Fact (1 < q)] (α : ZMod q) :
    ¬ EnsembleDetermined (waveSubstratum d L q α).φ := by
  set y : (Fin d → ZMod L) → ZMod q × ZMod q := fun _ => ((1 : ZMod q), (0 : ZMod q)) with hydef
  have hy : y ≠ (0 : (waveSubstratum d L q α).Conf) := by
    intro h
    have h1 : ((1 : ZMod q), (0 : ZMod q)) = ((0 : ZMod q), (0 : ZMod q)) :=
      congrFun h (fun _ => 0)
    exact one_ne_zero (congrArg Prod.fst h1)
  exact ensemble_underdetermined _ (waveSubstratum_A5 d L q α) hy

/-- **THE SINGLE-ORBIT ROUTE AND THE FIXED POINT ARE EXCLUSIVE**: a dynamics with a fixed point and
another state is not transitive, so the positive route of the scope amendment cannot be taken here.
Stated so that the closure of that route is a theorem and not a remark. -/
theorem not_transitive_of_fixedPoint {S : Type*} [Fintype S] [DecidableEq S] (φ : Equiv.Perm S)
    {x y : S} (hx : φ x = x) (hxy : y ≠ x) : ¬ ∃ s : S, ∀ t : S, t ∈ orbit φ s := by
  rintro ⟨s, hs⟩
  exact not_ensembleDetermined_of_fixedPoint φ hx hxy (ensembleDetermined_of_transitive φ s hs)

end EnsembleLeg

/-! ### Section D — T2: the observation-map leg -/

section ObservationLeg

variable {S : Type}

/-- **THE READ-WRITE STRUCTURE PRIVILEGES NO LOCUS**: a read-write family exists at every pair of
states, so the structure singles out no pair to serve as the observer's readout. The witness is the
constant reference coupling, which the structure's own axioms already admit. -/
theorem readWriteFamily_exists (a b : S) : Nonempty (ReadWriteFamily a b) :=
  ⟨{ couple := fun _ => 1
     reference := rfl
     local_support := fun _ _ _ _ => rfl }⟩

/-- **AND IT PRIVILEGES NO PAIR EVEN AMONG DISTINCT PAIRS**: on a carrier with at least three
states there are two pairs sharing no locus, each carrying a family, so no pair is distinguished by
the existence of a family. -/
theorem readWriteFamily_exists_two {a b c d : S} :
    Nonempty (ReadWriteFamily a b) ∧ Nonempty (ReadWriteFamily c d) :=
  ⟨readWriteFamily_exists a b, readWriteFamily_exists c d⟩

end ObservationLeg

/-! ### Section E — T8: the verdict -/

section Verdict

/-- **OUTCOME A, THE INTERFACE GAP, ON THE ENSEMBLE LEG.** For every substratum whose rule is
linear and whose configuration space carries more than the zero configuration, the only ensemble
constraint the architecture states — invariance — leaves the law undetermined, and the single-orbit
route that would have derived one is closed by the same fixed point. Stage 1 therefore does not
deliver a sourced pair, and the round stops: the induced process of stage 2 is not defined and the
divisibility predicates are not introduced.

Nothing here says the architecture is refuted, that no extension could supply an ensemble, or that
the observation-map leg fares better or worse; the observation-map leg is recorded separately. -/
theorem stochastic_interface_gap (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V]
    (h5 : 𝒮.A5) {y : 𝒮.Conf} (hy : y ≠ 0) :
    ¬ EnsembleDetermined 𝒮.φ ∧ ¬ ∃ s : 𝒮.Conf, ∀ t : 𝒮.Conf, t ∈ orbit 𝒮.φ s :=
  ⟨ensemble_underdetermined 𝒮 h5 hy,
    not_transitive_of_fixedPoint 𝒮.φ (phi_fixes_zero 𝒮 h5) hy⟩

/-- **THE SAME VERDICT FOR THE MANUSCRIPTS' OWN SUBSTRATUM**, on every torus whose alphabet has
more than one letter. The wave rule satisfies A5, so both legs of the gap hold of it and the
single-orbit route of the scope amendment is closed for it too. -/
theorem waveSubstratum_stochastic_interface_gap (d L q : ℕ) [NeZero L] [NeZero q] [Fact (1 < q)]
    (α : ZMod q) :
    ¬ EnsembleDetermined (waveSubstratum d L q α).φ ∧
      ¬ ∃ s : (waveSubstratum d L q α).Conf,
        ∀ t : (waveSubstratum d L q α).Conf, t ∈ orbit (waveSubstratum d L q α).φ s := by
  refine ⟨waveSubstratum_ensemble_underdetermined d L q α, ?_⟩
  rintro ⟨s, hs⟩
  exact waveSubstratum_ensemble_underdetermined d L q α
    (ensembleDetermined_of_transitive _ s hs)

end Verdict

end StochasticInterface
end OIBridge

#print axioms OIBridge.StochasticInterface.ensembleDetermined_of_transitive
#print axioms OIBridge.StochasticInterface.not_ensembleDetermined_of_disjoint
#print axioms OIBridge.StochasticInterface.not_ensembleDetermined_of_fixedPoint
#print axioms OIBridge.StochasticInterface.phi_fixes_zero
#print axioms OIBridge.StochasticInterface.waveSubstratum_phi_fixes_zero
#print axioms OIBridge.StochasticInterface.ensemble_underdetermined
#print axioms OIBridge.StochasticInterface.waveSubstratum_ensemble_underdetermined
#print axioms OIBridge.StochasticInterface.not_transitive_of_fixedPoint
#print axioms OIBridge.StochasticInterface.readWriteFamily_exists
#print axioms OIBridge.StochasticInterface.readWriteFamily_exists_two
#print axioms OIBridge.StochasticInterface.stochastic_interface_gap
#print axioms OIBridge.StochasticInterface.waveSubstratum_stochastic_interface_gap
