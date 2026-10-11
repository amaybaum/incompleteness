# NOTES-B17 — HO-24's explicit cone along B10-5's locally finite tower

Node B17 of `research/bridge` (round 4; last in priority, taken while dispatch 2 ran). Base L = `9f9f8257`. Evidence
levels as in NOTES-B14. Reading (the coordinator's third addendum): every statement here is an invariance statement —
whether a given cone is preserved by a given group — and none is about operational availability.

## 0. Question

The round-4 directive: is HO-24's explicit exotic cone invariant under B10-5's groups
`G_n = ⟨CNOT, 1 ⊗ diag(1, e^{2πi/2ⁿ}), 1 ⊗ X⟩` for `n ≥ 3`, and what is the first failing `n`; exact arithmetic. The
cone (HO-24 item 4, CONDITIONAL): `K = (Q3 ∩ Z*) + cone Z`, `Z` the `G₃₈₄`-orbit of the defect `d* = I − c*P_{h*}`,
`h* = (10, 2 − 2i, −1 − 3i, 3 − i)/√128`, `c* = 401/400`, `G₃₈₄ = ⟨CNOT, I ⊗ diag(1, i), I ⊗ U_J⟩` (item 1, its
Gaussian-rational lift; re-derived here before use, as the receipt of HO-24 says). The second addendum: name the weaker
alternative a failure defeats.

## S0. Design, productivity test and predictions (written 2026-10-11T05:39:54Z, before any run)

**Design.**
- **Invariance without Theorem S′.** `K` is defined from the orbit `Z` and `Q3`; `Q3` is preserved by every unitary
  conjugation and `Z` by `G₃₈₄`, so `K` is `G₃₈₄`-invariant by construction, and invariant under every `G_n ⊆ G₃₈₄`.
  No self-duality is used.
- **A non-invariance certificate without Theorem S′.** For a defect `d_j = I − c*P_{h_j} ∈ Z` and a unitary `V`, put
  `h′ = V h_j`. If `|⟨h_k|h′⟩|² ≤ 1/c*` for every orbit ray `h_k`, then `P_{h′}` pairs nonnegatively with every
  defect and (being positive) with `Q3 ∩ Z*`, so `P_{h′} ∈ K*`; and `⟨P_{h′}, V d_j V*⟩ = 1 − c* < 0`, so
  `V d_j V* ∉ K`. Only the definition of the dual is used.
- **Exact arithmetic.** Rays as Gaussian-rational vectors; the eighth root of unity enters only through
  `|A + ωB|² = |A|² + |B|² + √2·Re(Ā B (1 + i))` (`ω = (1 + i)/√2`), compared with `1/c*` by integer arithmetic on
  `p + q√2`.
- **Membership of the stages.** `G_n ⊆ G₃₈₄` modulo phases is decided by enumerating `G₃₈₄` (order 384 modulo
  `{±1, ±i}`) on Gaussian-rational matrices.

**Decision rules (fixed now).** `n` passes iff `G_n ⊆ G₃₈₄` modulo phases (then invariance holds by construction);
`n` fails iff an exact certificate as above exists for a generator of `G_n` and some defect; neither — UNDECIDED. The
first failing `n` is reported only if every `m < n` passes. Controls: (K1) the re-derived `G₃₈₄` has order 384 modulo
phases and the orbit of `h*` has 192 rays (HO-24 items 1, 4); (K2) positive control: at `n = 2` the certificate search
finds nothing (every image ray is an orbit ray, overlap 1 with itself); (K3) countercontrol: the certificate test
rejects `V = 1` (it must not certify the identity).

**Productivity test (§A.31), fixed now.** Gem iff the result constrains a bridge beyond "finite stages do not force
`Q3`" (known: HO-24 item 6, B7-4) — e.g. if the explicit cones of the finite stages turned out nested along the tower.
Expected: CONFIRMING (the first non-Clifford stage breaks the explicit Clifford cone).

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | (K1): the lift generates 384 elements modulo phases; the orbit of `h*` has 192 rays | `b17_tower.py` |
| S0-2 | `G_1, G_2 ⊆ G₃₈₄` modulo phases: `K` is invariant under them | `b17_tower.py` |
| S0-3 | `G_3 ⊄ G₃₈₄`; an exact certificate exists for `V = 1 ⊗ diag(1, e^{iπ/4})`: some defect and a projector in `K*` with pairing `1 − c* = −1/400` | `b17_tower.py` |
| S0-4 | First failing `n` = 3; every `n ≥ 3` fails (`G_3 ⊆ G_n`) | `b17_tower.py` |
| S0-5 | Controls K2, K3 green | `b17_tower.py` |
| S0-6 | Defeated alternative: "a finite stage" — each finite stage has an explicit exotic invariant cone (HO-24 item 6, [W]), so no finite stage forces `Q3`; and the explicit cones are not nested along the tower | §2 |
| S0-7 | Gem: CONFIRMING | §3 |

## 1. Outcome of S0 (written 2026-10-11T06:42Z)

**The run.** `experiments/b17_tower.py`, run 1 at 05:41:17Z, all six checks green; replay at 05:41:28Z byte-identical.
No Lean module (exact arithmetic only).

| id | outcome |
|---|---|
| S0-1 | confirmed [X] K1: the Gaussian-rational lift generates 384 elements modulo `{±1, ±i}`; the orbit of `h*` has 192 rays; its pairwise squared overlaps lie in `[25/2048, 13/16]` over 18336 pairs (K1b, HO-24 item 4's window) |
| S0-2 | confirmed [X]: `CNOT`, `1 ⊗ Z`, `1 ⊗ S`, `1 ⊗ X` lie in `G₃₈₄` modulo phases, so `G_1, G_2 ⊆ G₃₈₄` and `K` is invariant under both (by construction, §S0) |
| S0-3 | confirmed [X], more strongly than predicted: under `V = 1 ⊗ diag(1, e^{iπ/4})` every one of the 192 orbit defects is certified out of `K` — for each, `P_{V h_j}` lies in `K*` (all 192 squared overlaps at most `1/c* = 400/401`) and pairs to `1 − c* = −1/400` with `V d_j V*` |
| S0-4 | confirmed: the first failing stage is `n = 3`, and every `n ≥ 3` fails (`G_3 ⊆ G_n`) |
| S0-5 | confirmed [X]: K2 (no certificate at `n = 2`), K3 (none for `V = 1`) |
| S0-6 | confirmed (§2) |
| S0-7 | CONFIRMING (§3) |

## 2. The statement and the defeated alternative

All statements are invariance statements. HO-24's explicit exotic cone `K = (Q3 ∩ Z*) + cone Z` is invariant under
B10-5's stages `G_1` and `G_2` and under no `G_n` with `n ≥ 3` [X]; the first failing stage is `n = 3`, the first
non-Clifford one. Label: CONJECTURE (exact computation with controls, not kernel-checked; no named premise for the
tower facts; the exoticness of `K` is HO-24 item 4's, CONDITIONAL there).

**Defeated alternative: "a finite stage."** Each finite stage has an explicit exotic invariant cone (HO-24 item 6
[W]), so no finite stage forces `Q3`; and the explicit Clifford cone does not persist along the tower — `K` fails at
every stage from `n = 3` on — so the stages' explicit cones are not one cone carried up the tower. The tower as a whole
does not force `Q3` either, but through a different cone: the closure of the union (B10-5) is the closed group of
B10-4, generated by the gate, the NOT and the phase circle on one token, whose identity component is a 2-torus, and it
leaves an exotic cone invariant under every `G_n` at once (B10-4, CONDITIONAL on claim (D) through B7-2; dimension two
is beyond B16's count). Reading: invariance.

## 3. Gem classification (§A.31)

CONFIRMING, as predicted: the productivity test's alternative — the explicit cones of the finite stages nested along
the tower — did not occur.

## 4. Manuscript obligations

None.
