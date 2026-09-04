# CT3-R2B-Q2: exact period and cycle spectrum of the binary wave rule

`verification/lean/wave_period_probe.py` — checks W1–W10, exact integer arithmetic throughout.

The first-moment obstruction of CT3-R2B reduces, after the divisor-indexed simplification, to a
statement about the cycle spectrum of the update permutation. With `m = ord(P)`,
`ω = e^{2πi/m}`, and `s = ord(ω^r) = m/gcd(m,r)`, the block dimension `d_r` depends on `r` only
through `s` and equals

> `D_s` = the number of `P`-cycles whose length is divisible by `s`,

so the whole test is: **the width-2 obstruction fires iff some `s | m` with `s > 2` has
`(s/gcd(s,2)) ∤ D_s`.** Deciding that at every `L` needs the exact cycle spectrum. This note supplies
it in closed form for `q = 2`, without enumerating `4^L` states.

## The setup, and the one factorization everything comes from

On a ring of `L` sites over `𝔽₂`,

> `x(n,t+1) = x(n−1,t) + x(n+1,t) + x(n,t−1)`,  `F = [[0,I],[I,A]]`,  `A = S + S⁻¹`,

`S` the spatial shift; over `𝔽₂` the sign in `[[0,I],[−I,A]]` is immaterial. The temporal polynomial
factors,

> `x² + (S + S⁻¹)x + 1 = (x + S)(x + S⁻¹)`,

which is the algebraic form of the two traveling-wave directions. Every result below is a
consequence of it, in the equivalent shape given by Lemma 1.

## 1. Fixed points

**Lemma 1 (d'Alembert over `𝔽₂`).** *A function `x : ℤ² → 𝔽₂` satisfies*
`x(n,t+1) + x(n+1,t) + x(n−1,t) + x(n,t−1) = 0` *for all `(n,t)` iff*

> `x(n,t) = f(n−t) + g(n+t)`  *for some* `f, g : ℤ → 𝔽₂`.

*Two pairs give the same `x` exactly when they differ by `(c,c)` with `c` in the two-dimensional
space spanned by the constant `1` and the parity function `π(u) = u mod 2`.*

*Proof.* For `x(n,t) = f(n−t)`, the four terms are `f(n−t−1), f(n−t−1), f(n−t+1), f(n−t+1)` and
cancel in pairs; likewise for `g(n+t)`. Conversely, a solution is determined by `x(·,0)` and
`x(·,1)`, so it suffices to hit arbitrary initial data: `g = x(·,0) + f` and then
`f(n+1) = f(n−1) + x(n+1,0) + x(n,1)`, a recursion solvable from any choice of `f(0), f(1)`. For the
kernel, `f(u) + g(v) = 0` for all `u ≡ v (mod 2)` — and `u = n−t`, `v = n+t` realize exactly the
equal-parity pairs — forces `f` and `g` to be equal and constant on each parity class, i.e.
`f = g ∈ span{1, π}`. ∎

**Theorem 1 (fixed-point dimension).** *For all `L ≥ 1`, `k ≥ 1`,*

> `dim_{𝔽₂} ker(F_L^k − I) = 2·gcd(k,L) − 1_{L odd and k odd}`,

*hence* `|Fix(F_L^k)| = 2^{2gcd(k,L) − 1_{L,k odd}}` *with no state enumeration.*

*Proof.* A state fixed by `F^k` is exactly a solution on `ℤ²` that is `L`-periodic in `n` and
`k`-periodic in `t`. Write `x = f(n−t) + g(n+t)` by Lemma 1 and set `ε(u) = u mod 2`. Periodicity in
`n` says `f(u+L) + f(u) = g(v+L) + g(v)` whenever `u ≡ v (2)`; both sides are therefore constant on
each parity class, with common values `α₀, α₁`. Periodicity in `t` gives the same for the shift by
`k`, with values `β₀, β₁`:

> `f(u+L) = f(u) + α_{ε(u)}`,  `f(u−k) = f(u) + β_{ε(u)}`,
> `g(v+L) = g(v) + α_{ε(v)}`,  `g(v+k) = g(v) + β_{ε(v)}`.

Since `L` and `k` generate `dℤ` with `d = gcd(L,k)`, these relations determine `f` from its values on
`{0,…,d−1}` and `g` likewise — freely, and with no other constraint, once the relations are
consistent. Consistency is one condition: going `j = k/d` steps by `L` and then `j' = L/d` steps by
`−k` returns the argument to itself, so the accumulated increment must vanish, for `f` and for `g`.
Three parity cases, using that `j` and `j'` are never both even:

* `L, k` **both even** — every shift preserves parity, the increments are `jα_u` and `j'β_u`, and the
  condition is `jα_u + j'β_u = 0` for `u = 0,1`: one condition per parity class, so `(α,β)` has
  **two** free bits. The `g` condition is the same.
* **exactly one even**, say `L` even and `k` odd (`d` odd, `j` odd, `j'` even) — the `α`-sum is
  `α_u`, the `β`-sum alternates over an even number of terms and is `(j'/2)(β₀+β₁)`, so
  `α₀ = α₁ = (j'/2)(β₀+β₁)` with `β₀, β₁` free: **two** free bits, and again `g` gives the same.
* `L, k` **both odd** (`j, j'` odd) — the `f` condition is
  `((j−1)/2)(α₀+α₁) + α_u + ((j'−1)/2)(β₀+β₁) + β_{u+1} = 0` and the `g` condition is the same with
  `β_v` in place of `β_{u+1}`. Subtracting gives `β₀ = β₁`, hence `α₀ = α₁` and finally `α = β`:
  **one** free bit.

So the space of admissible `(f, g)` has dimension `2d + 2` in the first two cases and `2d + 1` in the
third; quotienting by the 2-dimensional kernel of Lemma 1 — which is admissible in all three cases,
`π` contributing `α_u = L mod 2` and `β_u = k mod 2` — gives `2d` and `2d − 1` respectively. ∎

Check W3 verifies the formula against the matrix for every `L = 1..14` and every `k = 1..3L`.

**Corollary (period).** `m_L = ord(F_L over 𝔽₂) = L` for even `L` and `2L` for odd `L`.

*Proof.* `F^k = I` iff the fixed-point dimension is `2L`, which needs `gcd(k,L) = L`, i.e. `L | k`,
and for odd `L` needs `k` even as well; the least such `k` is `L`, resp. `2L`. ∎ (Check W2, to
`L = 24`.)

## 2. The cycle spectrum in closed form

Write `M(n) = (1/n)·Σ_{d|n} μ(n/d)·4^d` for the number of aperiodic necklaces of length `n` on four
letters, and `C_ℓ` for the number of `P`-cycles of length exactly `ℓ`.

**Theorem 2 (cycle spectrum).** *For even `L`, the cycle lengths divide `L` and* `C_ℓ = M(ℓ)`.
*For odd `L`, the cycle lengths are the `e` and `2e` with `e | L`, and*

> `C_e = M(e)/2`,  `C_{2e} = M(e)/4`.

*Proof.* Möbius inversion of `|Fix(k)| = Σ_{ℓ|k} ℓ·C_ℓ` gives `C_ℓ = (1/ℓ)Σ_{d|ℓ} μ(ℓ/d)|Fix(d)|`.
For even `L` and `d | ℓ | L`, Theorem 1 gives `|Fix(d)| = 4^d`, which is `M(ℓ)` on the nose. For odd
`L`, `|Fix(e)| = 2^{2e−1}` and `|Fix(2e)| = 2^{2e}` for `e | L`; the odd-length sum is
`(1/e)Σ_{f|e} μ(e/f)2^{2f−1} = M(e)/2`, and splitting the divisors of `2e` into `f` and `2f` with
`μ(2e/2f) = μ(e/f)` and `μ(2e/f) = −μ(e/f)` collapses the even-length sum to
`(1/2e)Σ_{f|e} μ(e/f)(4^f − 2^{2f−1}) = M(e)/4`. Both are integers: every term of `Σ μ(e/d)4^d` is
divisible by 4 and `e` is odd. ∎

The two forms account for every state — `Σ_ℓ ℓ C_ℓ = 4^L` — and agree with brute-force enumeration
of all `4^L` states for `L ≤ 8` (checks W4, W5).

**Corollary (`D_s`).** With `W(t) = Σ_{t | e | L} M(e)`: for even `L`, `D_s = W(s)`; for odd `L`,
`D_s = 3W(s)/4` at odd `s` and `D_{2t} = W(t)/4`. (Check W6, to `L = 41`.)

## 3. What the first-moment test does

**Theorem 3 (powers of two are silent).** *For `L = 2^a` the test is silent at every `s`.*

*Proof.* Every cycle length is `2^i` and `C_{2^i} = M(2^i) = 2^{2^i}(2^{2^i} − 1)/2^i`, so
`v₂(C_{2^i}) = 2^i − i`, which increases in `i`. Hence `v₂(D_{2^j}) = v₂(Σ_{i ≥ j} C_{2^i}) ≥ 2^j − j`,
and `2^j − j ≥ j − 1` for every `j ≥ 1`; the test asks exactly for `2^{j−1} | D_{2^j}`. ∎

**Theorem 4 (the conjecture "silent iff `L` is a power of two" is false).** *For an odd prime
`L = p > 3` the test is silent iff `p² | 2^{p−1} − 1`, i.e. iff `p` is a Wieferich prime base 2. In
particular `L = 1093` and `L = 3511` are silent and are not powers of two.*

*Proof.* `m = 2p`, so the only `s > 2` are `p` and `2p`, and by the Corollary
`D_p = 3(4^{p−1} − 1)/p` and `D_{2p} = (4^{p−1} − 1)/p`. Both tests ask for divisibility by `p`, so
for `p > 3` both are silent iff `p² | 4^{p−1} − 1`. That is equivalent to Wieferich: `ord_{p²}(2)`
divides `2(p−1)` and equals either `ord_p(2)` or `p·ord_p(2)`, the latter impossible since `p ∤ 2(p−1)`
for odd `p`; so `ord_{p²}(2) | p−1`, i.e. `p² | 2^{p−1} − 1`. ∎

Checked exactly at `p = 1093` and `p = 3511` and at the eighteen odd primes `5 ≤ p ≤ 71`, where the
test fires and the Wieferich condition fails (check W8).

So the answer to the round's sharp question is **no**: the silence set is not the powers of two. The
power-of-two direction is a theorem; the converse fails, and it fails at a set no finite search can
delimit, since a further counterexample of this shape is a further Wieferich prime. Silence over
`L ≤ 64` coinciding with the powers of two (check W6) is a small-`L` coincidence, not the law.

## 4. The corpus correction

**Appendix B.3.1 / SM Appendix A, Theorem A.1** stated, for `q` prime with `gcd(L,q) = 1`,
`ord(F mod q) = qL` for odd `q` and `L` for `q = 2`, on the ground that "for `q = 2` the nilpotent
part is automatically killed". The value at `q = 2` is `2L`, not `L`. The unipotent factor at the
parabolic mode `λ = 0` is `[[0,1],[1,0]]` over `𝔽₂`, of order exactly 2, and `gcd(L,2) = 1` forces
`L` odd, so that factor is not absorbed into `L`. The uniform statement

> `ord(F mod q) = qL` at every prime `q` with `gcd(L,q) = 1`, `q = 2` included,

is what holds. Theorem B.3.2 of the same appendix is consistent with it without giving it on its
own: `F = F_ss·F_u` has commuting factors whose orders *divide* `L` and `q`, and the exact values
need in addition that the semisimple sector carries a primitive `L`-th-root mode and that `N ≠ 0`.
The parabolic bookkeeping is likewise a case split: the block at `α = −1`, of order `2q`, exists
only for even `L`, where the extra factor 2 already divides `L`; at odd `L` only the `α = +1`
block occurs, of order `q`. Either way `lcm(L,q) = qL`. Check W1 verifies the
corrected value over `q ∈ {2,3,5,7,11,13}` and `L ≤ 12`, and records that the superseded value holds
at no admissible `L`. The three corpus locations — `papers/SM.md`, `book/appendix-b-derivations.md`,
`book/The-Incompleteness-of-Observation-FULL.md` — carry the corrected statement.

The same audit found a second defect in the same appendix. **Theorem B.3.2(i)** states
`rank(N) = 2` for `N = (F^L − I)/L` with no parity hypothesis, while its own proof appeals to
`(−1)^L = 1 for even L`. There are two parabolic modes, `ζ = ±1`, only when `L` is even; for odd `L`
there is one, and `rank(N) = 1`. Check W9 verifies both values over `q ∈ {2,3,5,7}` and `L = 3..11`
with `gcd(L,q) = 1`, together with `N² = 0` throughout. **Theorem B.3.3**'s conductor is
`𝔣_ss(L) + rank(N)`, which is `𝔣_ss(L) + 2` at the even `L` of its table and `𝔣_ss(L) + 1` at odd `L`;
the table is unaffected. Nothing downstream of the appendix uses either value: the corpus sweep for
`ord(F`, `qL` and the conductor found no other dependent statement.

## What this round does not claim

That a firing test is a width-`w` obstruction for any `w ≥ 3`. The symmetric-sector palindromicity is
structural, but the antisymmetric-sector trace vanishing is the computed **width-2** ingredient of
CT3-R2B step one, and nothing here extends it.

That any of this transports to the infinite lattice. The periodization obligation recorded in CT3-R1
stands unused here as well.

That silence of the test — at `L = 4, 8, 1093, 3511` — exhibits a static local generator. The test is
an obstruction; its silence is the absence of one obstruction, and R2-A's control makes the general
form of that warning explicit.

That anything here covers `q = 3`. The period and the spectrum there are governed by different
formulas; the `q = 3` data of CT3-R2B step one is untouched.

That CT3 is settled in either direction.
