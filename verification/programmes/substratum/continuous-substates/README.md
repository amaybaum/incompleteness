# SUBSTATE-1: internal sub-states and visible recurrence

**Status: research-only, work in progress.** Tracking issue #1007. Base: `main` at
`f6989a27815c4d715223eebf2859422c1231e3f8`. This note changes no manuscript claim, status
or premise.

## Question

Main Lemma 1 proves that the visible sector is finite. Finiteness of the whole substratum
is a posit (Main §1.2 Remark, §4.5). This programme asks what happens if each finite
site state carries infinitely many internal sub-states below the resolution ε.

The first question concerns the recurrence route to P-indivisibility (Main §2.3). It
uses `Γ_L = I`: at one common time, the visible state returns for every hidden state.
A bijection of a finite set guarantees this. Does the property survive when the
sub-states are infinite?

## Setting of the probe

- **Dynamics:** the 1-D lattice wave map on a ring of `L` sites,
  `u_{t+1}(n) = u_t(n+1) + u_t(n−1) − u_{t−1}(n)`. Its integer matrix `F` reduces
  mod `q` to the substratum wave map (SM Theorem A.1).
- **Two sub-state continua:**
  - **real-type:** each site value in `R/Z`, with `F` acting on the torus `(R/Z)^{2L}`;
  - **`p`-adic-type:** each site value in `Z_p`, whose quotients `Z/p^k` are finite alphabets.
- **Hidden prior:** Haar measure.
- **Visible observable:** an integer linear form `v`, read through a two-cell partition.

`wave_torus_probe.py` uses exact integer and rational arithmetic only and runs in
about two seconds. `expected-result.json` is its byte-exact output; the run is
deterministic. Verdict text is generated from the measurements and printed only when
every control passes. The controls are:

1. `F mod q` has order `qL` for prime `q ∤ L` (SM Theorem A.1).
2. `M = F^L − I` is nonzero with `M² = 0` over `Z` (SM Theorem A.2, over `Z`).
3. Exact counts on the finite subgroup `(Z/8)^6` (`L = 3`). These check facts (H) and
   (R) below independently of their proofs.

Two facts are used:

- **(H)** If `v` and `w` are integer forms of rank 2, then `(v·x, w·x) mod 1` is
  Haar-distributed on `T²` when `x` is Haar-distributed on the torus. So
  `Γ_t = [[½, ½], [½, ½]]` whenever `v F^t` is not proportional to `v`.
- **(R)** If `vM = 0`, then `v F^{mL} = v`, so the visible cell returns exactly at
  every `t = mL`.

## Findings (`L = 3, …, 10`)

1. **Pointwise recurrence does not give `Γ_L = I`.**
   - With real-type sub-states, the single-site observable `u(0)` has `v F^t` never
     proportional to `v` for any `t ≥ 1`. So `Γ_t` is uniform for every `t ≥ 1`.
   - This family is P-divisible: `Γ_t = Γ_s Π` with `Π` uniform.
   - Every trajectory still recurs pointwise (Poincaré), and the visible space has two
     cells. Main's "Continuous-time extension" paragraph states the same obstruction for
     mixing flows.
2. **Observables blind to the non-recurring modes recur exactly.**
   - The non-recurring part of `F` is its unipotent part (`M ≠ 0`, `M² = 0`). Its image
     comes from the parabolic modes: the uniform shift of every site, and for even `L`
     the alternating mode.
   - The difference `u(0) − u(1)` (odd `L`) and `u(0) − u(2)` (every `L`) satisfy
     `vM = 0`. They return exactly at every `t = mL`, with `Γ_1` uniform.
   - By the stochastic-inverse lemma (Main §2.3), these rooted families are
     P-indivisible on `{0, …, L}`.
   - The uniform shift is the amplitude-shift symmetry of SM §2.7.
   - Countercontrol: `u(0) − u(1)` at even `L` has `vM ≠ 0` and does not return.
3. **The finite alphabet as a grid, and the direction of carries.** `(Z/N)^{2L}` is a
   finite `F`-invariant subgroup of the torus, and its uniform measure is the finite
   substratum with alphabet `Z/NZ`.
   - **Most significant digit:** for `L = 3` the single-site observable recurs only at
     `ord(F mod N) = 3N` (6, 12, 24, 48 for `N = 2, 4, 8, 16`), which grows with the
     alphabet. This is finding 1 seen through finite alphabets.
   - **Least significant digit:** the same observable returns exactly at
     `ord(F mod 2) = 6` on `(Z/8)^6`, with `Γ_1` uniform.
   - The reason is the direction of carries:
     - In `R/Z` the coarse digit is the most significant, and carries from finer digits
       reach it. The sub-states influence the visible cell.
     - In `Z_p` the coarse digit is the least significant, and carries only move upward.
       Under any `Z_p`-linear dynamics the sub-states never influence the visible cell,
       so `Γ_{ord(F mod p)} = I` holds exactly for every sub-state.

## Reading

Finding 2 suggests the condition that replaces total finiteness: *the part of the hidden
dynamics that does not recur has no influence on the visible statistics*. Total
finiteness is one way to satisfy it.

The two continua sit at opposite ends of this condition:

- **`p`-adic sub-states** preserve the finite recurrence theorem verbatim. Under linear
  dynamics they are inert: they are a deep sector that no dynamics couples to the
  boundary, so they are gauge (GR:142). They cannot supply what #1007 asks of them,
  namely a continuous gauge group or the operational completion of Main's finite-carrier
  obstruction.
- **Real sub-states** influence the visible state. They can do that work, but recurrence
  then holds only for observables blind to the non-recurring modes, and only for
  dynamics with that structure. A mixing interaction removes it.

Influence on the visible state and preservation of the recurrence route therefore pull
against each other. Any sub-state proposal has to be placed on that axis explicitly.

## Scope and limits

- Free linear dynamics in `d = 1` only, for `L = 3, …, 10`. The general-`L` pattern
  follows from the structure of SM Theorem A.2. A proof for every `L` is not written out.
- **The `d = 3` map.** It uses `α = 1/3`, which is not an endomorphism of `R/Z`. The
  real-type lift of the `d = 3` map is therefore not defined on the torus; it needs `R`
  or another carrier. In `Z_p` with `p ≠ 3`, `1/3` exists, which matches SM's condition
  `3 ∤ q`.
- **What is established:** P-indivisibility of the rooted family `Γ_t` only. Multi-time
  memory and the readback route are not examined.
- **The prior:** the hidden prior is Haar measure; other invariant measures are not
  examined.

## Next steps

1. Prove finding 2 for every `L` from the parabolic-mode structure of `M`.
2. Choose a carrier for the `d = 3` map, real-type or `p`-adic, and repeat the analysis.
3. Test an interacting map, the gauge-coupled update, for which observables, if any,
   keep exact or near-total common-time return.
4. Literature check, as listed in #1007, before any construction is promoted.
