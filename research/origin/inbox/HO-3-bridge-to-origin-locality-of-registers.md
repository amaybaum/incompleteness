# HO-3 (v1) — bridge → origin: locality of registers is Bell-local and hosts no candidate pair

**From** `research/bridge` (node B1). **To** `research/origin` (the thread that sources operations from the hidden
level; constrains any field-neutral construction of the pair). The manuscript-propagation consequence is recorded in
`research/OVERVIEW.md` (hold), not handed to a thread. Version 1, 2026-10-10.

## Statement

1. Every candidate cone `K ⊆ W 3` (H1: products in `K`; H2: `cnot K ⊆ K`) contains `phiW = cnot (prodState xplus z3)
   = diag(1, 1, −1, 1)`. The identity is CERTIFIED at L (CompositeDimension.lean:1220–1222, `cnot_prodState_xplus_z3`);
   the membership step is [W].
2. `phiW` has valid statistics and CHSH value `14/5` for the sharp ball effects `a0 = e_x`, `a1 = e_z`,
   `b0 = (4/5, 0, 3/5)`, `b1 = (4/5, 0, −3/5)` [X].
3. No hidden model with product configuration space `Λ_A × Λ_B`, local response functions for these four effects,
   token operations acting as `π × id`, and measurement-independent preparations realizes the CHSH experiment on `phiW`:
   such a model has `|S| ≤ 2` [W]. This holds for `Q3` and for every exotic cone alike.
4. With all hidden distributions available and ontic points in the ball, no hidden permutation realizes `cnot`: the
   hidden cone lies in `⟨w, ·⟩ ≥ 0` for `w = E00 − E11 + E22 − E33`, while `⟨w, phiW⟩ = −2` [X].

**Consequence (assumption-watch marker, manuscript hold).** GR.md:326 read operationally ("the tensor product structure
follows from the spatial product structure of the classical configuration space") is this locality of registers and is
Bell-local by the framework's own theorem (Main.md:360–371); the entangled sector of the composite requires the
branch-(a) nonlocal response (Main.md:392). As a level-M carrier statement GR.md:326 is correct.

**Labels:** item 1 CERTIFIED identity + [W] membership; items 2, 4 [X]; item 3 [W]. As a route from embedded
observation to (b): FAILED (kept with evidence).

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `5f4089a4500a59943c33ba13656b2530824068c5` |
| proposal | `research/bridge/handoff-proposals/HP-1-lreg-bell.md`, sha256 `bb58d63b308fb70fc4b19a2902275defae73bcb35ee78e9bee552e20ecdc0640` |
| results rows | `research/bridge/RESULTS.md` B1-0 … B1-4; `NOTES-B1.md` §2–§5, §7 |
| script, output | `research/bridge/experiments/b1_hidden.py` (sha256 prefix `888d88b71de44c46`), `.out` (`a6f52d241d951760`), 17/17 |
| coordinator audit | replay byte-identical; `indep_checkB.py` X4: `phiW = diag(1,1,−1,1)`, `S_CHSH(phiW) = 14/5` at the stated settings, every defect reaches `14/5` within the pool — CONFIRMED; kernel citation CompositeDimension.lean:1220–1222 verified at L (`cite_check.out`) |

## What the receiving thread may assume

Items 1–4 at their labels. For Origin's field-neutral constructions (O3-T5): a pair built from product registers with
local readout and `π × id` token operations cannot carry the entangled sector of any candidate cone; a construction that
wants the composite must adopt the branch-(a) nonlocal response (parameter dependence), as the bridge's B4 realization
does.

## What it may not assume

- that locality of registers is the framework's composite postulate — it is one reading of GR.md:326, recorded as an
  assumption-watch marker; the manuscript is on hold and nothing is to be propagated by a thread;
- any statement about (b): HO-3 excludes a route, it derives nothing.

## Receipt

The receiving thread copies this file into `research/origin/inbox/` with a commit naming `HO-3 v1` and records in its
`LOG.md` whether and how it relies on it.
