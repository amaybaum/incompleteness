# Note: Π_s convention — paper text vs code

This note flags a **potential discrepancy** between SM.md's text definition
of `Π_s` and the formula used in `oi_lattice_code/gauge/two_loop_vp.py`.

## The two formulas

**Text** (SM.md line 564):
```
Π_s(0) = ∫ d⁴q [cos²(q_μ)/D(q) − cos²(q_μ)·sin²(q_μ)/D(q)²]
D(q) = Σ_ν sin²(q_ν) + m²
spatial average over μ = 1, 2, 3
```

**Code** (`two_loop_vp.py`):
```python
D_q = sin²(q_0) + sin²(q_1) + sin²(q_2) + sin²(q_3) + m²
V2_q = (cos²(q_1) + cos²(q_2) + cos²(q_3)) / 3
Pi_1 = sum(V2_q / D_q²) * vol
```

## Numerical comparison at m=0.05

| N  | `Π_s(0)` via text formula | `Pi_1` via code formula |
|----|---------------------------|--------------------------|
| 12 | 0.607                     | 123.8                    |
| 16 | 0.401                     | 39.5                     |
| 20 | 0.345                     | 16.5                     |
| N→∞ target | **0.3084** (matches 1/α_0 = 23.25) | ??? |

The text formula converges to the value consistent with `1/α_0 = 6·Π_s·4π = 23.25`,
matching the paper's claimed 1/α_0.

The code formula does not converge to 0.308. It gives much larger numbers
(decreasing with N but still well above 0.3 at N=20), and is sensitive to
small m via a 1/m⁴ pole at q=0.

## Algebraic identity

The two formulas are NOT algebraically equivalent:
```
(text) = cos²·(1/D − sin²/D²) = cos²·(D − sin²)/D² = cos²·(Σ_{ν≠μ} sin²_ν + m²)/D²
(code) = cos²(q_μ)/D²                              [only the cos², no "(Σ_{ν≠μ} sin² + m²)" factor]
```

These are different integrands. The text formula comes from the "cos²" (vertex²)
minus a seagull-like subtraction that removes the IR-divergent `q=0` contribution.
The code formula has only the bubble-like `cos²/D²` without subtraction, giving
a 1/m⁴ pole at `q=0`.

## Where this matters

The paper's code uses `Pi_1` (code formula) as the denominator of the induced
gauge propagator:
```python
D_gauge = 1.0 / (p2_lat * Pi_1)
```

If the text's `Π_s` is the physically correct induced 1-loop VP, then the code
is using a different (smaller by factor ~100) D_gauge. This would affect the
numerical values of `δ_0 = 8.0 ± 2` reported from the 2-loop VP calculation.

However — the reported `δ_0` result may still be internally consistent if the
CODE uses Pi_1_code everywhere uniformly (as long as the 1/α_0 calibration is
done separately, which the code does not show).

## My calculation's choice

`reproduce_AB.py` and the supporting files use the **text formula** throughout:
- `paper_pi_s.py` implements `Π_s = [cos²/D − cos²·sin²/D²]` exactly
- `bubble_at_finite_p.py`, `ghost_self_energy.py`, `p_extrapolation.py` use
  `D_ind = 1/(k̂²·Π_s)` with `Π_s` from `paper_pi_s.py`

My result `A·B = 48` is in the convention where:
- `Π_s = 0.308` (text formula)
- `1/α_0 = 6·Π_s·4π = 23.25`
- `g_0² = 1/(6·Π_s) = 0.541`
- `A·B · g_0²` per C_2 = `46.4 · 0.541 = 25.1` (paper's target)

This is internally consistent. My first-principles derivation recovers paper's
fitted 46.4 to within 4%.

## Suggested action for paper authors

Either:
1. **Update the code** to use the text's two-term formula for Π_s, and verify
   the `δ_0 = 8.0` result is unchanged (if it was computed self-consistently
   with Pi_1_code throughout, this just re-normalizes).
2. **Update the text** to reflect what the code actually computes, with
   clarification of what Pi_1_code represents.

Either way, the `1/α_0 = 23.25` identification with `6·Π_s·4π` requires
`Π_s = 0.308`, which only the text formula produces.
