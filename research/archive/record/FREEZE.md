# RECORD — frozen interface class, search rule and verdict criteria (written before any computation)

Base `0f2687b7b87925b53c6e3d8c6d1a233f36624dea`. Read-only; off-repo; no act, freeze or repository implication.
The same class, search rule and criteria apply to all three rules (linear, nonlinear, majority) with no
per-rule adjustment.

## Substratum and system

The leap rule on ℤ: v^{t+1}_i = F(v^t)_i + v^{t−1}_i mod 2, state (u_i, v_i) = (v^{t−1}_i, v^t_i), F one of
linear v_{i−1}+v_{i+1}, nonlinear v_{i−1}v_{i+1}+v_i, majority maj(v_{i−1},v_i,v_{i+1}). Initial state: the
uniform product measure (invariant under every leap). The *system* is the lattice. The observer's visible site
is 0; its *pair* is p = (u_0, v_0) ∈ {0,1}², encoded p = u + 2v.

## The interface class IC (finite, exhaustive)

An observation O_κ is a record-writing invasive measurement, given by κ = (κ_0, κ_1):
1. read b = v_0 (the outcome);
2. append b to the external record (never acted on by the system dynamics; never read except as an outcome);
3. disturb the pair: (u_0, b) ↦ κ_b(u_0), where κ_b is an injection of the two branch inputs
   {(0,b), (1,b)} into the four pair states (12 choices per branch);
4. one leap.

The joint map on system × record is injective for every κ (the record holds b; κ_b is injective). The
non-selective map f_κ(ω) = κ_{v_0(ω)}(ω) on the system alone may be non-injective: then information leaves the
system for the record. |IC| = 12 × 12 = 144; the one passive member (κ_b = identity on its branch for both b) is
excluded, leaving **143 interfaces**, all run for every rule.

## Effects, preparations, generators

- Selective observation letter `o` (records b), free time step `i` (one leap), non-selective observation `m`
  (= O_κ with the record forgotten). Level 2 adds the local actions `f` (flip v_0) and `s` (swap u_0, v_0).
- **Preparations:** protocols over {o, i} (Level 2: {o, i, f, s}) of length ≤ L_p, conditioned on their
  record, positive weight.
- **System effects:** protocols over {o, i, m} (Level 2: {o, i, m, f, s}) of length ≤ L_e with a singleton
  record event. Record degrees of freedom are never counted as system effects: an effect is a functional on the
  system state, its value the probability of a record outcome of a later protocol.
- **Non-selective generators** (invariance is tested for these only): G = {W = i, M = m} (Level 2:
  {i, m, f, s}). Selective branches are **not** required to preserve anything.
- **Seed:** r = (o, outcome 1), "measure now, get 1". The space must contain the unit and r.

## Criteria (per rule, per interface)

All linear algebra exact over ℚ on integer count tables; rank certified by the rank-basis method of QUOTIENT
(full table built, greedy columns, exact independence and spanning); every generator's dual map checked
well defined on the detected relations; byte-identical replay for every reported witness.

- **(Q1) Existence / admissibility:** κ ∈ IC (injective record writing, by construction) and **invasive**:
  some domain effect e has (m·e)(x) ≠ (i·e)(x) for some preparation x (the non-selective observation differs
  from idling on the completed state). Non-invasive members of IC are reported and excluded.
- **(Q2) Finite effect closure:** C = span(unit, w·r : words w over G) computed by word length k. PASS iff
  C stabilizes (C_k = C_{k−1} at the largest k reached), dim C = **exactly 4**, and C is G-invariant (every
  generator maps each basis effect of C into C, certified). dim C < 4 or > 4, or no stabilization, is FAIL for
  that κ. (No time-dependent basis, no history-dependent readout, no enlargement by adding orbit directions
  beyond the cyclic span of unit and r.)
- **(Q3) Discrimination:** per rule, PASS iff some admissible κ passes Q2.

## Stages (fixed in advance)

- **Stage A (all 143 κ × 3 rules), Level 1:** L_p = 3, L_e = 3 (words ≤ 2). Advance κ iff dim C_2 ≤ 4,
  C_2 = C_1, and C invariant.
- **Stage B (every advancing κ, any rule):** L_p = 4, L_e = 4 (words ≤ 3); the Q2 test proper.
- **Level 2** (actions f, s added; same 143 κ × 3 rules, same stages, L_p = L_e = 3 for Stage A) runs **only
  if Level 1 ends ALL FAIL**, for all rules alike.

## Terminal labels

- **SEPARATES:** linear passes, nonlinear and majority both fail.
- **ALL FAIL:** no rule passes (evidence that IC is too weak).
- **NEGATIVE LEAK:** nonlinear or majority passes (recorded as is; the criterion is not changed).
- **INCONCLUSIVE:** a certification or well-definedness guard fails where a verdict depends on it.

A pass is reported with its witness: κ, branch maps, record update, non-selective map, the four effect
generators of C, and the exact invariance matrices. A fail is reported with its obstruction (dim C or the
first non-closing generator image).
