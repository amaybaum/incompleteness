# HP-round6-transfer-2 — to the coordinator (round 7; for bridge and countermodels): the deferred channel-route controls

**From** `research/round6-transfer` (S0-b item 4, deferred by the owner's narrowing). Design notes only: nothing here
was computed or run, and nothing here is a result. Reading: invariance of cones under transferred maps.

## What round 7 would check (proposal)

The exact checker of the original S0 (rebuild of O14's circuit with readout, reset and `Z` correction; the channel
`Φ_k = (1 − (3/8)^k) conj(zPh) + (3/8)^k id` on every matrix unit at fixed depths; trace preservation; the dictionary
action; `J`), with expected-false controls (omitted correction; a wrong success outcome), and three cone controls,
each by an explicit construction, enumerated with expected truth values before its run 1:

- **(a) closed, invariant under the 24 Clifford target actions, moved by `Φ_1`.** KC is likely unsuitable: with
  `c − 1 = 10⁻⁵` and `Φ_1`'s identity weight `3/8`, every pairing of a generator's image with a generator is
  nonnegative unless some orbit ray `g` has target weights with `p₀p₁ < (16/3)(c − 1)/c² ≈ 5.33·10⁻⁵` [W]. Candidate:
  `{ω ∈ W 3 : ω b ∈ L for b ∈ {(1, ±e₁), (1, ±e₂), (1, ±e₃)}}` (`L` the Lorentz cone): closed, contains the products,
  invariant under every signed-permutation rotation; `tens(e₀, (1, 1, 1, 1))` lies in it and its `Φ_1`-image
  `tens(e₀, (1, 1/4, 5/4, 1))` does not (`b = (1, 0, −1, 0)` gives `−1/4`). With O9-L1 and O14-T9 at their labels it
  separates (T) from (T^ch) for `MixR {π/4}`.
- **(b) closedness is used.** In `V = span{e₀₀, e₀₁, e₀₂}` the cone over the open unit disc plus the point `(1, 0)`:
  convex, not closed, invariant under every `Φ_k` (`|M_k v|² = (1 − (4/5)p(1 − p))|v|²`, `p = (3/8)^k`), not under
  `conj(zPh)`. Scope: invariance under the sequence `Φ_k`, not under every available channel of the class.
- **(c) closedness cannot replace H3.** The block-positive cone (closed, `⊋ Q3`, H1, every local positive map,
  not self-dual; it also fails H2: `CNOT F CNOT` pairs to `−1` with `|−⟩|1⟩`) and, isolating H3,
  `{X = [[A, B], [B†, D]] : A ⪰ 0, D ⪰ 0, ‖B‖₁ ≤ κ (tr A · tr D)^{1/2}}` for `κ > 1` in the control's block form:
  closed, convex, H1, H2, every target unitary (so A_miss), every local CPTP target channel (trace-norm contraction
  [L]), `⊋ Q3`, not self-dual.

## What the receiving threads may assume

Nothing as a result. The constructions are proposals to be checked exactly in round 7 or labelled [W]/[L].
