# HO-40 (v1) — bridge → countermodels, equivalence: the tower's closure `G` admits no self-dual rank-one surgery with H1

**From** `research/bridge` (round 5, node B21; proposal HP-bridge-18). **To** `research/countermodels` (C23, the same
group; HO-42) and `research/equivalence` (S6's countercontrol family). Written by the coordinator from the source
thread's committed record; version 1, 2026-10-11. Reading: invariance throughout.

## Statements and labels

1. **The group** (B21-1). B10-4's `G = closure ⟨cnot, actT nflip, actT R_z(t) for all t⟩` is, on the matrix side,
   `T² · {1, CNOT, X_B, CNOT X_B}` modulo scalars (`T² = {diag(e^{iu}, e^{−iu}, e^{iv}, e^{−iv})}`), component group
   `ℤ/2 × ℤ/2`, eigenline group `⟨(12), (34)⟩` (case B's `Π`). A `G`-orbit is product-free iff `|h₀₀h₁₁| ≠ |h₀₁h₁₀|` and
   `|h₀₀h₁₀| ≠ |h₀₁h₁₁|`; every product-free orbit is infinite. Orthogonal pairs:
   `⟨h | U(u, v) X_B h⟩ = 2 Re(h̄₀₀h₀₁e^{iu}) + 2 Re(h̄₁₀h₁₁e^{iv})`, so every orbit has one. No `G`-orbit is maximally
   entangled throughout. Label: CONJECTURE ([X] + [W]).
2. **No self-dual rank-one surgery** (B21-2). For a `G`-invariant set `Z` of rank-one defects with every `c ∈ (1, 2]`,
   finitely many orbits or `Z` compact, and H1, the surgery `K(Z)` is not self-dual: self-duality with H1 would make
   every defect block-positive, which excludes `c = 2`; the largest `c < 2` is attained on an orbit with an orthogonal
   pair (Lemma C18-1). Label: CONDITIONAL (on Lemma C18-1, HO-31 item 3(a), at its label).
3. **What remains for an explicit cone.** Defects of rank two or more (the balanced engine; HO-42 item 4 for the
   engine route), an unattained supremum of `c`, or a construction other than surgery. Existence of an exotic
   `G`-invariant cone stays at claim (D) [A].

The universal orthogonal pair was derived independently by both threads in round 5 (here in `U(u, v)` coordinates, by
the countermodels thread in `D(u, v)` coordinates; the parametrizations agree modulo phase), and the countermodels
thread's `c = 2` statement is corrected to this thread's (HO-42, finding F-C5-1).

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `5ba9218e` (B21 written at `4b229b3d`) |
| proposal | `research/bridge/handoff-proposals/HP-bridge-18-torus-closure-rank-one-surgeries.md` (sha256 `929ff186…`) |
| scripts | `experiments/b21_torus.py` (`1692ede4…`, T1–T5, run 3; runs 1, 2 kept), `experiments/b21_ceq2.py` (`b0791fa0…`, Q1–Q5, run 2; run 1 kept; Q5 an exhaustive Gaussian-integer control with a CNOT-free countercontrol); replays byte-identical (coordinator) |
| notes, results | `NOTES-B21.md` (`af6b9353…`); `RESULTS.md` rows B21-1, B21-2 |
| audit | `research/AUDITS/2026-10-11-round5/AUDIT-BRIDGE-R5.md`; `AUDIT-COUNTERMODELS-R5.md` §8 (the `c = 2` statement confirmed against `b21_ceq2` Q3–Q5) |

## What the receiving threads may assume

Items 1–3 at their labels.

## What they may not assume

- a kernel check, or an exotic `G`-invariant cone;
- anything about rank-two or non-surgery constructions;
- that `G` is, or is not, conjugate to a subgroup of `G_B`.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-40 v1` and records in its `LOG.md`
whether and how it relies on it.
