# TUNE-1, Step 2: amendment 1, final, addendum 1

**Governing text.** This addendum amends `TUNE-1-STEP2-AMENDMENT-1-final.md` (at `75dfb6d4`, left
unchanged) in one row only, C-POS-2 (final, B6.1 item 4). With the proposal at `e676c42a` (sha256
`2a081101…7499fd5`) and the final amendment, it is the governing text for the rerun of C-POS-2.
Paper-only; no computation is authorized.

## D1. The owner's decision

Recorded at PR #1237 comment 6822699905 (`amaybaum`, author association `OWNER`,
2026-11-12T11:45:23Z, posted through the `claude` GitHub app). Verbatim:

> **Owner decision (amaybaum, 2026-11-12).** The question: how should C-POS-2 be handled given
> decision 5? The answer: "(a) Accept b + δ_{K−2} (Recommended)". C-POS-2's δ is restated in the
> amendment and C-POS-2 alone is rerun. That rerun goes to independent review, then ChatGPT, before
> L5/M3.

## D2. C-POS-2's δ under decision 5

In final B6.1 item 4, the sentence "Q2, Q5′ and Q6′ hold at `ε ≥ b + δ`, as the row states" is
replaced by the following.

- **Definition.** `δ_{K−2}` is the larger of two quantities:
  - `g`, the largest gap between a requested angle and the nearest menu angle about `n̂`, unchanged;
  - the largest trace distance from a pure state to the nearest pure state `R_w n` prepared by a
    menu prefix of horizon at most `K − 2`. These are exactly the prefixes followed by at least two
    rounds (decision 5, final B3).
- **Preserved form.** Q6′ holds at every `ε ≥ b + δ_{K−2}`. It is posed for `K ≥ 3` (final B3).
- **Unchanged.** Q2 and Q5′ hold at `ε ≥ b + δ`, as the row states. The scope (separating menus)
  and the Q3′ floor `b + K g` are those of final B8.

## D3. The failure statement for C-POS-2's Q6′

The session-2 record (§2.3) claimed that Q6′ fails on the whole window
`[b + δ_K, b + δ_{K−2})`. The independent review of session 2 (F2) found two gaps:
- Q6′(i) bounds the *mean* credited state, so mixtures of prepared states count;
- the step "credited states cannot do better" was not made quantitative.

That claim is withdrawn and replaced by the following narrower statement, proved by hand [W]. It
uses the per-history bound of `finite-a2-v5/REPORT.md`:205–243 [R], which the review confirmed.

**Statement.** Let `C_{K−2}` be the convex hull of the ideal conditional states reachable by
admissible prefixes of horizon at most `K − 2`. These are the pure states `R_w v`, with `v` a
preparation direction or a read eigen-direction. Let

> `D_{K−2} = max over pure ψ of the Bloch distance from ψ to C_{K−2}`.

Then Q6′(i) fails for every `ε < (c₀ D_{K−2} − b − g)/(2c₀ + 1)`.

**Proof.**
1. Let `P` be an admissible Q6′ preparation (`ℓ ≤ K − 2`) with credited mean `σ̄`. All laws below
   are marginal over the prefix records and taken on `𝒯_2`, with Bloch vectors `r` and the sup-TV
   norm `‖·‖` over tests.
2. Credit gives `‖W_P − V(σ̄)‖ ≤ ε`, where `W_P` is the world's law and `V` the target's.
3. The per-history bound, with world weights, gives `‖W_P − M(ρ̄)‖ ≤ hκ ≤ b`. Here `M` is the
   menu-ideal quantum law, which is affine, and `ρ̄ = Σ_r w_r ρ_r^{ideal} ∈ C_{K−2}`. This includes
   heralded `P`, whose conditional ideal states are reachable ideal states.
4. A test in `𝒯_2` uses at most one gate. A menu gate is within diamond distance `g` of its target,
   and declared menu gates are exact, so `‖M(ρ) − V(ρ)‖ ≤ g`.
5. Hence `‖V(σ̄) − V(ρ̄)‖ ≤ ε + b + g`. By (ii), `‖Λ x‖ ≥ c₀|x|`, so
   `|r̄ − r̄_ρ| ≤ (ε + b + g)/c₀`.
6. Q6′(i) needs `|r̄ − ψ| ≤ 2ε`. So `dist(ψ, C_{K−2}) ≤ 2ε + (ε + b + g)/c₀`.
7. Taking `ψ` that attains `D_{K−2}`, Q6′(i) fails whenever
   `c₀ D_{K−2} > (2c₀ + 1) ε + b + g`. ∎

**Consequence for the old form.** For a menu with `δ_K` small and `D_{K−2}` large, the old entry
"Q6′ at `ε ≥ b + δ_K`" is false on `[b + δ_K, (c₀ D_{K−2} − b − g)/(2c₀ + 1))`. This interval is
non-empty for small `b`, `g` and `δ_K`. The red of session 2 stands with this window in place of the
withdrawn one. Section 3 of the C-POS-2 rerun record gives a concrete case.
