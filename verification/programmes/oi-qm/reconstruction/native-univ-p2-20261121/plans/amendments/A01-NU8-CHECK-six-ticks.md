# A01 to NU8-CHECK: six ticks per PCA step (amendment before any run)

**Standing.** Recorded amendment to `plans/NU8-CHECK-PREREG.md`, written before any run. The check
has not been run and stays gated. It answers review
[#1499 c.7064953331](https://github.com/amaybaum/incompleteness/pull/1499#issuecomment-7064953331)
item R1. The preregistration file itself is unchanged.

**Error.** The preregistration states the relation as `Φ³ ∘ E = E ∘ F_P`, with "10 PCA steps, that
is, 30 second-order steps" and a comparison "at step `3n`". One tick of the second-order rule is one
half-step of a staggered component (NU1(b)), and NU8 has six phases. So one PCA step is six ticks,
and the stated rule would fail on a correct implementation.

**Replacements** (all else unchanged):
- **Question:** does `Ψ⁶ ∘ E = E ∘ F_P` hold, where `Ψ` is one tick of the second-order rule?
- **Length:** 10 PCA steps, that is, 60 second-order ticks.
- **Pass:** for every instance and every PCA step `n ≤ 10`, the second-order run started at `E(c)`
  equals `E(F_P^n(c))` bitwise at tick `6n`.
- **Controls K2 and K3:** they compare at tick `6n`.
