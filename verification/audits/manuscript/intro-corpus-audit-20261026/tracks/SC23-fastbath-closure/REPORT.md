# SC-23 investigation: fast-bath bound vs exact zero; one-step thermalization vs window-wide Markovianity (WIP, unreviewed)

Read-only investigation at `main` `1a60e06b`, owner-prioritized (2026-10-27). Run every script from this directory with
`python3 -I -B`. The preregistrations were frozen before computation: `PREREG.txt` (sha256 d82f4d53…, with Amendment A1
appended before any code ran) and `PREREG2.txt` (sha256 fd869745…, a new F1 round). `f1.py` is **void**: its positive
control CF1-b failed on the frozen model E, which never writes x_0, and it exits 1. The F1 verdict therefore rests on
`f1b.py`. `f1c_check.py` and `f2x_explore.py` are confirmatory or exploratory and were not preregistered. The coordinator
replayed `f1b.py` and `f2.py`, and both reproduced their committed outputs byte for byte.

No formal theorem is involved. Nothing in `verification/lean-mathlib/OIBridge/` (238 files) states either lemma; the search
covered Fannes/Pinsker, mixing, erasure, fast bath, ETH, T^k and Markov.

## F1: an exponential bound is not an exact zero
- **Claim** (Main :159–161, a paper statement with no proof). Assuming τ_B ≪ τ_S and uniform erosion e^{-τS/τB} per step,
  δ_k ≤ δ_0 e^{-(k-1)τS/τB} for k ≥ 2, and therefore (C4) "fails". δ_0 is undefined.
- **Definitions.** (C4) (Main :80) requires only a nonzero gap at an accessible order. No precision threshold exists
  (:141, :167, :538, :624).
- **The conclusion fails for three reasons:**
  - the right-hand side is positive for every finite τS/τB;
  - order k = 1 is not covered;
  - with δ_k read as the largest gap at order k, the inequality itself is false, because erosion counts a record's age,
    not the gap's order.
- **Counterexample, model G** (`f1b.py`, all controls green). G is a register whose erosion events wipe every cell.
  - d = 2, r = 1/1000: δ_3 > r², refuting the inequality for every δ_0 ≤ 1.
  - d = 2, r = 1/2: δ_k = 1/4, 3/10, 4/13, 21/68, 55/178, 72/233, increasing in k.
  - r = 10⁻¹²: δ_k ≈ 10⁻²⁴ > 0 at every k, and M_k ≈ 7.2 × 10⁻⁴⁹ bits > 0.
  - The inequality is refuted in 21 cells; exact vanishing is unsupported in every tested (d, r).
- **Strongest correct form** (paper derivation from the physical-memory theorem, Main :463–467). Suppose that at each
  coupling the readout-relevant hidden conditional given the visible record is within ε ≤ ε_0 e^{-τS/τB} of π_H. Then:
  - δ_k ≤ 2ε at every k ≥ 1, uniformly in k (attained in all 72 E′/G cells);
  - M_k ≤ 2[ε log₂(n_V−1) + h(ε)] ≤ (2/ln 2) ε_0 e^{-x}(x + 1 + ln((n_V−1)/ε_0)), with x = τS/τB;
  - this is exponentially small and not zero; at x ≥ 10⁶ it is about 10⁻⁴³⁴²⁸⁸ bits.
- **Sites stating exact vanishing:**
  - Main :161, :165, :742, :754, :756;
  - Complexity :204;
  - Explainer :926, :928, :930, :932;
  - Substratum :56, :351, :492;
  - ch03 :58, ch04 :178 and :182, ch01 :227, glossary :27, ch02 :194, each with its FULL mirror.
- **Proposed lemma text** (unreviewed draft): "**Lemma (fast bath suppresses readback).** *Suppose that at each coupling the
  conditional law of the readout-relevant hidden variable given the visible record to date lies within ε of π_H in total
  variation, with ε ≤ ε_0 e^{-τ_S/τ_B} … Then for every k ≥ 1, δ_k ≤ 2ε, and for ε ≤ 1−1/n_V,
  M_k ≤ 2[ε log₂(n_V−1)+h(ε)] ≤ (2/ln 2) ε_0 e^{-τ_S/τ_B}(τ_S/τ_B + 1 + ln((n_V−1)/ε_0)).*" Not recommended: adding a gap
  threshold to (C4), which would change a Layer-0 definition.

## F2: one-step thermalization does not give window-wide Markovianity
- **Claim** (Main :439, :445; Explainer :357–361). The hidden sector dephases between couplings, so T^(k) = T^k on
  accessible timescales and the dynamics is P-divisible. The display at :443 conditions only on the previous visible state.
  Composing T^(k) = T^k needs the hidden law at each coupling, given the root and the intermediate visible states, to be the
  equilibrium law of the readout-relevant compression.
- **Paper proof.** Under the invariant (uniform) measure, P(H_t | X_t) = π_H for every bijection and every t, so one-step
  thermalization holds exactly and cannot imply T^(k) = T^k.
- **Counterexamples** (`f2.py`, all controls green). One-step thermalization holds exactly, with ε = 0, in every model;
  D_k = ‖T^(k) − T^k‖.

  | Model | D_k for k = 1..6 |
  |---|---|
  | M1, Main §2.4's σ | 0, 4/9, 4/27, 40/81, 40/243, 364/729 |
  | M2, φ(x,h) = (x⊕h, x) | 0, 0, 1/2, 0, 0, 1/2 |
  | M3, a rotation bath | D_2 = 2/9 |
  | M4, a random bijection | D_2 = 1/32 |

  - Exhaustive: 24/24 bijections of Z2×Z2 and 720/720 of Z2×Z3 satisfy one-step thermalization, and 16 and 648 of them
    respectively have T^(k) ≠ T^k.
  - Countercontrols N1 (fresh-symbol tape) and N2 (hidden reset) give D_k = 0.
  - Main's (k−1)ε theorem holds on every model.
- **Explainer :357–361** claims e^{-Δτ} convergence for the fine-grained flow. That cannot hold: a bijection preserves the
  total-variation distance to its invariant measure.
- **Exploratory** (`f2x_explore.py`, not preregistered): with ε = 1/2·10⁻⁶, 192 of 432 invertible-T bijections of Z3×Z2
  are P-indivisible. So Main :447's contrapositive "observable P-indivisibility requires τ_S ≲ τ_B" is unsupported. The
  supported contrapositives are ε ≥ δ/(k−1) and ε ≥ ε_min(I*, n_V).
- **Exact identity** (CF2-d): in a bijective realization, TV(P(H_t | X_0..X_t), π_H) = 1 − P(X_1..X_t | X_0). The
  fine-grained ε is near 1, so Main :494's "drives ε small" needs a compression, which is what (EM) supplies.
- **Dependent sites:**
  - Main :439, :445, :447, :494;
  - Explainer :357–361;
  - Substratum :129 ("divisibility deficit", which contradicts Main :461);
  - ch01 :51, :225, :227 and glossary :27, each with its FULL mirror.
- **Proposed text for Main :445** (unreviewed draft): "If, at every coupling, the readout-relevant hidden conditional
  given the root and the intermediate visible record equals one effective equilibrium distribution, each step is computed
  against it and T^{(k)} = T^k on accessible timescales; with ε-closeness the quantitative theorem below gives
  ‖T^{(k)}−T^k‖ ≤ (k−1)ε and the physical-memory bound. Thermalization conditioned on the current visible state alone does
  not suffice: under the invariant measure it holds exactly for every bijection, including §2.4's model, where
  T^{(2)} = I ≠ T²."

## Assumption-watch markers
- Reading an upper bound as vanishing; check other "≪ ⇒ absent" exclusions.
- An erosion exponent counts record age, not gap order.
- The conditioning set matters: a hidden conditional given only the current state is automatically π_H under the
  invariant measure.
- Closure must hold on the readout-relevant compression, not on the fine-grained state.
- T^(k) ≈ T^k does not imply P-divisibility.

## Expected output
- `f1b.py`: "W1: PRINT … {2: 3, 3: 4}", "W2: PRINT", "ALL CONTROLS GREEN", exit 0.
- `f2.py`: "V2-1/V2-2/V2-3: PRINT", "ALL CONTROLS GREEN", exit 0.
- `f1.py`: exit 1 (void).
- `f1c_check.py f1.py f1b.py`: "72/72 cells".
