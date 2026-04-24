# Π_s convention audit

**Scope.** Audit of the 2-loop staggered VP computation in `two_loop_vp.py` against the $\Pi_s$ convention used in the paper text (SM.md §6.2).

**Finding.** The scalar used as the induced-propagator denominator in `two_loop_vp.py` is not the $\Pi_s$ defined in SM §6.1. The resulting ratio exhibits factor-7× IR-regulator dependence across $m \in [0.01, 0.20]$ — characteristic of a scheme-locked quantity rather than a physical $\delta(1/\alpha)$ shift. The `δ_0^{(2L)} = 8.0 ± 2` result produced by this script is therefore held in reserve pending a rebuilt calculation.

**Scope of impact.** No numerical prediction in the paper changes. $\delta_0 = 10.02$ is determined empirically from the U(1) row (SM §6.2). $1/\alpha_0 = 23.25$ and $A \cdot B = 48.0 \pm 1.5$ use $\Pi_s$ from `paper_pi_s.py` under the TEXT formula and are unaffected.

---

## 1. The two formulas

**TEXT** (SM §6.1):

$$\Pi_s(0) = \int d^4q\,\Big[\tfrac{\cos^2(q_\mu)}{D(q)} - \tfrac{\cos^2(q_\mu)\,\sin^2(q_\mu)}{D(q)^2}\Big], \quad D(q) = \sum_\nu \sin^2(q_\nu) + m^2$$

spatially averaged over $\mu = 1, 2, 3$. Gives $\Pi_s \to 0.3084$ in the plateau $m \in [0.001, 0.05]$. Satisfies $1/\alpha_0 = 6 \cdot \Pi_s \cdot 4\pi = 23.25$. This is the form used by `paper_pi_s.py` and the A·B derivation code.

**CODE** (`oi_lattice_code/gauge/two_loop_vp.py`, scalar labelled `Pi_1`):

```python
V2_q = (cos²(q_1) + cos²(q_2) + cos²(q_3)) / 3.0
Pi_1 = Σ V2_q / D_q² · vol
```

Equivalent to $\text{Pi}_1 = (1/3) \sum_{\mu} \int \cos^2(q_\mu)/D(q)^2\, d^4q$. This is the second term of the TEXT formula **without the $\sin^2(q_\mu)$ factor in the numerator and without the first** $\cos^2(q_\mu)/D(q)$ **term**.

## 2. Numerical behavior of the two quantities

Across $(N, m)$:

| N  | m    | Pi_1_code | Pi_s_text | 6·Pi_1_code·4π | 6·Pi_s_text·4π |
|----|------|-----------|-----------|----------------|----------------|
| 8  | 0.05 | 625       | 1.853     | 47,000         | 139.7          |
| 16 | 0.05 | 39.5      | 0.401     | 2,980          | 30.2           |
| 24 | 0.05 | 8.22      | 0.326     | 619            | 24.5           |
| 24 | 0.10 | 0.951     | 0.309     | 71.7           | 23.3           |
| 24 | 0.20 | 0.419     | 0.297     | 31.6           | 22.4           |

- `Pi_1_code` has a $1/m^4$ IR divergence (factor 48,000× increase from $m=0.20$ to $m=0.01$ at $N=16$, consistent with $1/m^4$ scaling).
- `Pi_s_text` is IR-finite and converges to 0.3084 in the plateau.
- $6 \cdot \text{Pi}_1\text{\_code} \cdot 4\pi$ never equals 23.25 at any $(N, m)$ tested — the closest it comes is 31.6 at $(N=24, m=0.20)$, still 36% off.
- $6 \cdot \text{Pi}_s\text{\_text} \cdot 4\pi$ converges cleanly to 23.25.

**Conclusion 1.** The $1/\alpha_0 = 23.25$ identification holds only with the TEXT formula for $\Pi_s$.

## 3. The 2-loop VP formula requires Pi_1 = Π_s

From `two_loop_vp.py`:
```python
D_gauge = 1.0 / (p² · Pi_1)              # induced gauge propagator
Sigma_q = ∫ V²_se / D_qp · D_gauge       # self-energy insertion
Pi_2_SE = ∫ V²_q / D_q³ · Sigma_q        # 2-loop VP
ratio_SE = Pi_2_SE / Pi_1
δ_0 = 23.25 · 3 · ratio_SE               # converted via 1/α_0
```

Since `Sigma_q` has one factor of $1/\text{Pi}_1$ from `D_gauge`, `Pi_2_SE` also has one factor of $1/\text{Pi}_1$. Therefore:
$$\text{ratio}_\text{SE} = \text{Pi}_2\text{\_SE} / \text{Pi}_1 = \Omega / \text{Pi}_1^2$$
where $\Omega$ is an integral with no $\text{Pi}_1$ dependence. So $\delta_0 = 23.25 \cdot 3 \cdot \Omega / \text{Pi}_1^2$ scales as $1/\text{Pi}_1^2$.

The formula $\delta_0 = 23.25 \cdot \text{ratio}$ can only be physically correct if $\text{Pi}_1$ is the same $\Pi_s$ that satisfies $1/\alpha_0 = 6 \cdot \text{Pi}_1 \cdot 4\pi = 23.25$. Otherwise the conversion factor 23.25 and the scalar in `D_gauge` are inconsistent.

**Conclusion 2.** The code's formula is convention-locked: it requires $\text{Pi}_1$ to equal $\Pi_s\text{\_text}$ for the "23.25·ratio" conversion to yield a physical $\delta(1/\alpha)$ shift. The code uses $\text{Pi}_1\text{\_code}$ instead, which breaks this.

## 4. Direct numerical test

At $(N=8, m=0.01)$, computing `compute_fast()` with two choices of the scalar used in `D_gauge`:

| choice                | pi_1     | Pi_2_SE   | ratio_tot | δ_0 naive |
|-----------------------|----------|-----------|-----------|-----------|
| `pi_1 = V²/D²` (code) | 3.91×10⁵ | 3.01×10⁴  | 0.231     | **5.37**  |
| `pi_1 = Π_s_text`     | 39.35    | 2.99×10⁸  | 2.28×10⁷  | 5.3×10⁸   |

Using $\Pi_s\text{\_text}$ in `D_gauge` (as the paper TEXT says the induced propagator uses) makes the self-energy insertion ~10⁷× larger (because `D_gauge` is 10⁴× larger). The resulting $\delta_0$ is astronomical, not the ~10 the paper claims.

**Conclusion 3.** There is no simple convention substitution that makes the code produce a physical $\delta_0 \approx 10$ while using $\Pi_s\text{\_text}$ consistently. The ≈ 5–8 number emerges specifically from using $\text{Pi}_1\text{\_code}$ (the non-physical scalar) throughout and then multiplying by 23.25 at the end.

## 5. IR-regulator dependence of the code's ratio

A physical 2-loop correction to $1/\alpha$ should be IR-regulator-independent (stable as $m \to 0$ in the continuum, with weak $m$-dependence at finite $m$ within the plateau $m \in [0.001, 0.05]$). The code's ratio does not behave this way:

| N | m=0.01 | m=0.05 | m=0.10 | m=0.20 |
|---|--------|--------|--------|--------|
| 6 | 0.0760 | 0.0867 | 0.1195 | 0.2346 |
| 8 | 0.0771 | 0.1136 | 0.2237 | 0.5405 |

At $N=8$, varying $m$ from 0.01 to 0.20 changes the ratio by a factor of 7×, and the resulting "$\delta_0 = 23.25 \cdot \text{ratio}$" ranges from 5.4 to 37.7.

The stability at $m=0.01$ specifically (0.0760 at $N=6$, 0.0771 at $N=8$) is a numerical artifact, not a physical plateau: at $m=0.01$ both $\text{Pi}_1\text{\_code}$ and $\text{Pi}_2\text{\_SE}$ are dominated by the shared $1/m^n$ IR divergence near $q=0$, so their ratio becomes the ratio of divergent coefficients — a finite scheme-defined quantity. At larger $m$ where the divergences don't dominate, the ratio is sensitive to the integrands' finite parts, which differ between the code's scheme and the TEXT-formula scheme.

**This is the signature of a scheme-locked quantity, not a physical $\delta(1/\alpha)$.** A physical $\delta_0$ would not change by a factor of 7 when the IR regulator moves by a factor of 20 within the paper's claimed $m$-plateau. The apparent "stability" of the code's result at $m=0.01$ is a coincidence of that specific choice of regulator, not a feature of the calculation's physical content.

The paper's §6.2 claim of "a robust plateau $m \in [0.001, 0.05]$" is correct for $\Pi_s\text{\_text}$ (the 1-loop VP), which varies by <10% across that range and converges to 0.3084. It is NOT correct for the code's 2-loop ratio, which depends strongly on $m$ in that same range.

A derivation yielding a physical $\delta(1/\alpha)$ from the code's ratio would require the ratio to be $m$-stable (at least within the plateau); it isn't. The code computes a specific regulator-locked ratio, not a physical 2-loop correction. The rebuild in `two_loop_rebuild/` starts from the TEXT formula rather than attempting to justify the code's scheme.

## 6. Structure of a TEXT-consistent 2-loop VP calculation

The components a correct calculation requires:

### 6.1 Physical relationship between 2-loop VP and δ(1/α)

Starting from $1/\alpha_0 = 6 \cdot \Pi_s(0) \cdot 4\pi = 23.25$ (requires $\Pi_s = \Pi_s\text{\_text}$), 2-loop corrections yield $\Pi_s^{(2L)}(0) = \Pi_s^{(1L)}(0) \cdot (1 + \delta)$, giving a shifted coupling $1/\alpha_\text{ren} = (1/\alpha_0) \cdot (1 + \delta)$ and therefore $\delta_0 \equiv 1/\alpha_\text{ren} - 1/\alpha_0 = 23.25 \cdot \delta$.

The $\delta$ in "$\delta_0 = 23.25 \cdot \delta$" must be $(\delta\Pi_s\text{\_text})/(\Pi_s\text{\_text})$, where $\delta\Pi_s\text{\_text}$ is the 2-loop correction to $\Pi_s\text{\_text}$ specifically — not a ratio of two quantities in a different scheme. The code's `Pi_2/Pi_1` is not this ratio.

### 6.2 Diagrams contributing to δΠ_s_text

The 1-loop integrand of $\Pi_s\text{\_text}$ is
$$I_1(q) = \cos^2(q_\mu) \cdot [1/D(q) - \sin^2(q_\mu)/D(q)^2]$$
averaged over $\mu = 1, 2, 3$. At 2-loop, insertions modify this integrand:

**(a) Fermion SE insertion** on one of the two fermion lines in the bubble. The propagator $S(q) \to S(q) + S(q) \cdot \Sigma(q) \cdot S(q)$, where $\Sigma(q)$ is the fermion self-energy from gauge exchange with $D_\text{gauge} = 1/(p^2 \cdot \Pi_s\text{\_text})$. This modifies the $1/D^2$ factor as $1/D^2 \to 1/D^2 + 2 \Sigma(q)/D^3$, and similarly for the $1/D$ factor. Contribution:
$$\delta I_1^{(\text{SE})} = \cos^2(q_\mu) \cdot [\Sigma(q)/D^2 - 2 \sin^2(q_\mu) \cdot \Sigma(q)/D^3] + \text{(other leg)}$$

**(b) Vertex correction** to the OI vertex $\cos(q_\mu)$. By Ward identity at $p=0$, this contributes equal to the SE insertion (up to sign conventions).

**(c) Momentum-dependent Π_s(p).** The gauge propagator $D_\text{gauge}(p) = 1/(p^2 \cdot \Pi_s)$ uses $\Pi_s$ at $p=0$. At finite internal momentum $p$, $\Pi_s(p) = \Pi_s(0) \cdot (1 + c p^2 + \ldots)$, and the correction propagates into the integrand.

**(d) Sails (crossed) diagram.** Gauge line connecting the two fermion propagators of the VP bubble, rather than attaching to one line. Topologically distinct; must be computed directly.

For each, the integrand has the TEXT-style structure $\cos^2 \cdot [1/D^n - \sin^2 \cdot (\ldots)/D^{n+1}]$ rather than the code's $V^2/D^2 \cdot (\ldots)$. The integrands share the IR structure of $\Pi_s\text{\_text}$, ensuring the $m \to 0$ limit is well-defined.

## 7. Summary of impact

**Unaffected:**
- $1/\alpha_0 = 23.25$ — a 1-loop result using the TEXT formula via `paper_pi_s.py`.
- $A \cdot B = 48.0 \pm 1.5$ from SM §6.2.1 — `reproduce_AB.py` uses $D_\text{ind}(k) = 1/(\hat{k}^2 \cdot \Pi_s\text{\_text})$ with `paper_pi_s.py`'s TEXT formula. Independent of `two_loop_vp.py`.
- $\delta_0 = 10.02$ as empirically determined from the U(1) row.

**Affected:**
- The prior claim "$\delta_0^{(2L)} = 8.0 \pm 2$ from 2-loop lattice PT" — the code computes a scheme-locked ratio, not a physical 2-loop $\delta(1/\alpha)$ shift. The "8" is specifically tied to $m=0.01$; at $N=8$ the same code's naive $\delta_0$ output varies 5.4 → 7.9 → 15.6 → 37.7 across $m = 0.01, 0.05, 0.10, 0.20$ — a factor of 7× span, much larger than the claimed ±2 uncertainty.

`two_loop_vp.py` is retained in-tree for reference; its output is held in reserve pending the rebuilt calculation in `two_loop_rebuild/`. The paper's primary source of $\delta_0$ is the empirical U(1)-row determination.
