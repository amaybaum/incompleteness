# FIXED-SCALE-1 — one reversible hierarchy, indefinitely deep access, classical memory

**Research author result; written infinite-model proof and exact finite enumerations, pending independent mathematical review.** Related to SUBSTATE-2 issue #1010 and draft PR #1011. The test conditions were committed first in `PREREGISTRATION.md`. No native OI source, QM instrument, YM action or physical scale prediction is claimed.

## Mathematical result

One single compact-state dynamical law was fixed *before* the exact tests:
\[
X=\mathbb F_2\times\mathbb F_2\times\{0,1\}^{\mathbb Z},
\quad
T(a,r,c)=(a\oplus r\oplus c_0,\;r,\;Sc),
\quad
(Sc)_i=c_{i+1}.
\]
The prior is product-fair Haar and the finite observer alphabet contains four possible records:
\(\pi(a,r,c)=(a,c_0)\).
In particular r is a persistent hidden bit, not a fresh seed chosen at each time.

**Proposition (fixed-law classical memory with P-divisible rooted maps).**
The map T is a continuous, invertible, product-measure-preserving homeomorphism of the compact Cantor-like state space. For all \(t\ge1\),
\[
\Gamma_t=\tfrac14 J_4,\qquad
I(O_{t-1};O_{t+1}\mid O_t)=1\text{ bit},
\]
where the \(\Gamma_t\) are rooted conditional two-time maps and
\(O_t=\pi(T^t x)\). There is **no common exact observable identity return at any positive time**, even though every finite horizon uses only finitely many initial coordinates. In fact,
\[
P(O_t=O_0)=\tfrac14 \quad (t\ge1).
\]
The entire rooted family is P-divisible. The visible multi-time process is not first-order Markov.

**Proof (T and prior).** The tape shift is a homeomorphism with inverse the right shift and preserves independent fair bits. For a fixed tape and r, the operation \(a\mapsto a\oplus r\oplus c_0\) permutes the a-bit, and the skew-product preserves the fair a-bit, uniform r and tape product measure. Inversion first recovers the tape via \(S^{-1}\), then
\(a=a'\oplus r\oplus c_0\).
Thus no fresh randomness has been inserted by the dynamics.

**Proof (two-time rooted statistics).**
Induction gives
\[
a_t=a_0\oplus(t\bmod2)r
          \oplus\bigoplus_{j=0}^{t-1}c_j,\qquad
O_t=(a_t,c_t).
\]
For \(t=1\), the hidden r-bit makes \(a_1\) fair conditional on \(O_0\), while \(c_1\) is independent fair. For odd \(t\ge3\), r again supplies a fresh fair conditional parity; for even \(t\ge2\), at least one of \(c_1,\ldots,c_{t-1}\) does so. The independent \(c_t\) is fair in every case. Therefore every rooted conditional row is \((1/4,1/4,1/4,1/4)\). Divisibility is witnessed by the identity stochastic matrix at \(s=0\) and the uniform transition \(J_4/4\) for any \(s\ge1,t>s\), since
\((J_4/4)^2=J_4/4\).
The probability of matching the initial full two-bit record at \(t>0\) is exactly \(1/4\); hence no positive \(t\) yields \(\Gamma_t=I_4\).

**Proof (multi-time memory).** For every \(t\ge1\),
\[
r=a_{t-1}\oplus a_t\oplus c_{t-1}.
\]
Thus after observing \(O_{t-1},O_t\), the next a-bit is **completely determined** as \(a_{t+1}=a_t\oplus r\oplus c_t\). Without \(O_{t-1}\), the hidden r-bit is still uniformly fair conditional on \(O_t\), so the next a-bit is fair. The future tape bit \(c_{t+1}\) is independent fair under both conditionings. Consequently
\[
H(O_{t+1}\mid O_t)=2,\qquad
H(O_{t+1}\mid O_{t-1},O_t)=1
\]
and the conditional mutual information equals exactly **one bit**, for every \(t\ge1\).
This is a concrete demonstration that **rooted stochastic P-divisibility and finite-history conditional memory are distinct**. It says nothing about quantum CP-divisibility.

## Parameter-free triple-record identity (a classical diagnostic)

The same unaltered update rule yields, for every \(t\ge1\),
\[
a_{t-1}\oplus a_{t+1}=c_{t-1}\oplus c_t.
\]
Both sides follow by XORing the two adjacent updates, cancelling the same hidden r.
The two-time rooted distributions are completely uniform, yet this full-record parity check holds with probability **one**. That observation distinguishes the model from an iid four-outcome process sharing all its two-time rooted matrices.

**Classical countercontrol:** if the r term is removed, the single-step relation
\(a_{t+1}=a_t\oplus c_t\) holds, so the visible process is Markov and CMI is zero. The three-time parity relation then still holds; it **does not uniquely identify persistent hidden memory on its own**. Use the parity diagnostic **together with** the one-step uncertainty and the complete three-time law. This additional parity prediction was deduced from the preregistered fixed rule; it is a mathematical follow-up, not an independent preregistered physical forecast.

## Matched-classical reference: identical rooted maps, different full records

A stronger follow-up negative control uses a **separate reversible iid
four-symbol shift**, rather than only disabling r within the same
skew model. Let its hidden tape have independent uniform symbols
\(d_i\in\{0,1,2,3\}\), shifted invertibly on a bi-infinite
index set, and let the visible record at time t be \(d_t\).
For every \(t\ge1\), this iid model has **exactly the same
rooted matrix \(\Gamma_t=J_4/4\)** as the fixed-skew model,
but the full three-time distributions differ:

| Quantity | Fixed skew T | Matched iid shift |
|---|---:|---:|
| \(\Gamma_t(i,j)\), all \(i,j\), all \(t>0\) | 1/4 | 1/4 |
| Three-record support | 32 of 64 | 64 of 64 |
| Probability per supported triple | 1/32 | 1/64 |
| \(I(O_0;O_2\mid O_1)\) | 1 bit | 0 bits |

The **exact total-variation distance** between their three-time
joint laws is \(1/2\), because the fixed-skew law has 32
events of probability \(1/32\), while the iid reference has
all 64 at \(1/64\). No model parameters were adjusted to match
the two-time channels: they agree *identically* by the analytic
rules. This isolates the missing information in a purely
two-time experimental description.

A separate [matched classical control](matched_control.py)
exhaustively checks cyclic four-symbol tapes of lengths 3–7
(up to **16,384** tape configurations), all earlier rooted
two-time maps, all 64 triple probabilities, and the rational
three-time total variation \(1/2\). Both normal and optimized
Python gave byte-identical [MATCHED.json](MATCHED.json);
the [joint replay driver](replay.py) pins the script and
structured evidence hashes. This follow-up comparison was
added **after** the initial FIXED-SCALE-1 preregistration;
it is a stronger classical negative control, not an
original preregistered or physically predicted quantum effect.

## Exact finite approximation and boundary effects

For each \(n=3,\ldots,9\), replace the bi-infinite tape by a cyclic n-bit tape, leaving the update rule, the a/r variables, and the observer unchanged. The full state has \(2^{n+2}\) configurations; the largest test exhausts **2,048**.

The committed exact rational `fixed_scale_probe.py` verifies for every n:

- Both skew and no-r variants are bijections with explicit two-way inverse.
- Under uniform counting measure, all **32 supported three-time words** have exact probability \(1/32\), and the CMI ratio is exactly one bit (versus zero without r).
- At every \(1\le t<n\), every rooted transition row is \((1/4,1/4,1/4,1/4)\). No asymptotic statistics or floating-point tolerances are used.
- At \(t=n\), the tape wraps and the rooted map is **not** uniform. At \(2n\), the whole microscopic permutation is the identity, providing an exact visible return. **Do not infer this size-dependent return in the infinite model.**
- A tape bit initially at any predeclared depth \(1\le m<n\) first changes the visible tape bit at time m, and changes the a-bit at time \(m+1\), with exactly the same rule at every level.
- The no-feedback variant has a deterministic one-step visible a update and no three-time conditional memory.

The source `fixed_scale_probe.py` has **no Python assert statements**: each check uses an explicit error-raising function and remains active with optimization. Both `python3 -I -B` and `python3 -I -B -O` were executed locally and produced byte-identical `RESULTS.json`. The immutable source and expected-results SHA-256 are pinned by `replay.py`.

Command from repository root:

```sh
python3 -I -B verification/programmes/substratum/recursive-substates/fixed-scale-skew/replay.py
```

This is an exact finite computation, **not** Lean certification of the infinite probabilistic theorem.

## Scientific boundary and next source gate

This is a genuine **one-law**, no horizon-dependent-parameter, *classical* example of indefinitely deep initial-state access, positive predictive memory and **no** common exact visible return. It improves on B1 (which chose depth m in the rule separately for every m) and explains how a recursive state topology can matter dynamically.

But it does **not** select a unique physical self-similar scaling ratio, a log-periodic spectrum, a finite physical boundary entropy, a gauge action or the five operational QM conditions. Its tape coordinate is a mathematically convenient hierarchy; no derivation ties that hierarchy to the actual OI cubic microscopic lattice, native observer interface or Yang–Mills link variables. A stationary fair Bernoulli shift is also a familiar purely classical construction.

**Decision:** ACCEPT as a bounded mathematical fixed-law control, with independent review pending; PARK any claim of physical emergence. The next honest test must source the same level coupling and accessible apparatus from an actual OI microscopic system, constrain the hidden prior without calibration to the target, and then attempt a genuinely nonclassical or gauge-action-selecting prediction. Do not claim physical quantum equivalence from an exact classical memory witness.
