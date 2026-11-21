import OIBridge.SubstratumInterfaceAudit

/-!
# The wave substratum at `L = 0`: sites `ℤ^d`

`SubstratumInterfaceAudit` states `waveSubstratum_A2`, `waveSubstratum_A3`,
`waveSubstratum_A4Exact` and `waveSubstratum_A5` for every `L : ℕ`, with no `[NeZero L]`
hypothesis, and `waveSubstratum_A1` under `[NeZero L] [NeZero q]`. In Mathlib `ZMod 0` is `ℤ`
by definition. This file elaborates the four theorems at `L = 0`, which makes them statements
about the wave rule on the unbounded lattice `ℤ^d`, and adds a control showing that the instance
is infinite.

* `waveZ_sites` : the site type at `L = 0` is `Fin d → ℤ`, by `rfl`.
* `waveZ_waveF` : at `L = 0` the rule is `α` times the sum over the `2d` neighbours `i ± e_k`,
  computed in `ℤ^d` with the additive structure of `ℤ`, by `rfl`.
* `waveZ_A2`, `waveZ_A3`, `waveZ_A4Exact`, `waveZ_A4`, `waveZ_A5` : the specializations of the
  existing theorems at `L = 0`; `waveZ_A4` is A4 with trivial gauge, through
  `Substratum.a4_of_exact`.
* `waveZ_A4Exact_int` : the exact form of A4 restated over `ℤ^d`, with the translation `shiftBy`
  taken in the additive group of `Fin d → ℤ`.
* `waveZ_not_A1` (control) : for `d ≥ 1` and a nontrivial alphabet, the finiteness predicate `A1` fails at `L = 0`; the
  configuration space is infinite, so the instance above is not a finite model.

The scope is the wave rule of `[SM §4.1]` on `ℤ^d` with alphabet `ZMod q`, and the predicates
`Substratum.A2`–`A5` as `SubstratumInterfaceAudit` defines them. Nothing here concerns A6, the
observer theory, or any other step of the reconstruction chain.
-/

namespace OIBridge
namespace SubstratumInterfaceAudit
namespace WaveUnbounded

variable (d q : ℕ) (α : ZMod q)

/-- At `L = 0` the sites of the wave substratum are `Fin d → ℤ`. -/
theorem waveZ_sites : (waveSubstratum d 0 q α).ι = (Fin d → ℤ) := rfl

/-- At `L = 0` the wave rule is `α` times the sum over the axis neighbours `i ± e_k` of `ℤ^d`. -/
theorem waveZ_waveF (c : (Fin d → ℤ) → ZMod q) (i : Fin d → ℤ) :
    waveF d 0 q α c i =
      α * ∑ p : Fin d × Bool,
        c (i + (if p.2 then Pi.single p.1 (1 : ℤ) else -Pi.single p.1 (1 : ℤ))) := rfl

/-- A2 at `L = 0`. -/
theorem waveZ_A2 : (waveSubstratum d 0 q α).A2 := waveSubstratum_A2 d 0 q α

/-- A3 at `L = 0`, with degree `2d`. -/
theorem waveZ_A3 : (waveSubstratum d 0 q α).A3 (2 * d) := waveSubstratum_A3 d 0 q α

/-- The exact form of A4 at `L = 0`. -/
theorem waveZ_A4Exact : (waveSubstratum d 0 q α).A4Exact := waveSubstratum_A4Exact d 0 q α

/-- A4 with trivial gauge at `L = 0`. -/
theorem waveZ_A4 : (waveSubstratum d 0 q α).A4 ⊥ :=
  Substratum.a4_of_exact (waveSubstratum d 0 q α) (waveZ_A4Exact d q α)

/-- A5 at `L = 0`. -/
theorem waveZ_A5 : (waveSubstratum d 0 q α).A5 := waveSubstratum_A5 d 0 q α

/-- The exact form of A4 over `ℤ^d`: the wave rule commutes with every translation of `ℤ^d`,
the translation taken in the additive group of `Fin d → ℤ`. -/
theorem waveZ_A4Exact_int (v : Fin d → ℤ) (c : (Fin d → ℤ) → ZMod q) :
    waveF d 0 q α (shiftBy (ι := Fin d → ℤ) v c) =
      shiftBy (ι := Fin d → ℤ) v (waveF d 0 q α c) :=
  waveSubstratum_A4Exact d 0 q α v c

/-- Control: for `d ≥ 1` and a nontrivial alphabet, the finiteness predicate `A1` fails at `L = 0`. The configurations
`δ_n`, equal to `(1, 0)` at the constant site `(n, …, n)` and `(0, 0)` elsewhere, are pairwise
distinct for `n : ℤ`. -/
theorem waveZ_not_A1 (hd : 0 < d) [Nontrivial (ZMod q)] : ¬ (waveSubstratum d 0 q α).A1 := by
  intro h
  have hfin : Finite ((Fin d → ℤ) → ZMod q × ZMod q) := h
  have hinj : Function.Injective (fun (n : ℤ) (i : Fin d → ℤ) =>
      ((if i = (fun _ => n) then (1 : ZMod q) else 0), (0 : ZMod q))) := by
    intro n m hnm
    by_cases hs : (fun _ : Fin d => n) = (fun _ => m)
    · exact congrFun hs ⟨0, hd⟩
    · exfalso
      have h1 : (if (fun _ : Fin d => n) = (fun _ => n) then (1 : ZMod q) else 0) =
          (if (fun _ : Fin d => n) = (fun _ => m) then (1 : ZMod q) else 0) := by
        have h0 := congrArg (fun y => (y (fun _ => n)).1) hnm
        exact h0
      rw [if_pos rfl, if_neg hs] at h1
      exact one_ne_zero h1
  exact not_finite_iff_infinite.mpr (Infinite.of_injective _ hinj) hfin

end WaveUnbounded
end SubstratumInterfaceAudit
end OIBridge

#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_sites
#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_waveF
#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_A2
#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_A3
#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_A4Exact
#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_A4
#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_A5
#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_A4Exact_int
#print axioms OIBridge.SubstratumInterfaceAudit.WaveUnbounded.waveZ_not_A1
