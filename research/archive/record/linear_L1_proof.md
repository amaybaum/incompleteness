# Linear rule, Level 1: every interface yields i.i.d. fair records (written proof)

Setting: linear leap v^{t+1}_i = v^t_{i−1} + v^t_{i+1} + v^{t−1}_i (mod 2), initial state uniform product measure on
(u^0_i, v^0_i). Level-1 letters o, m, i each end in exactly one leap; an `o` reads v_0 *before* its disturbance, so
the k-th reading in time is taken at a time t (number of leaps already done), and distinct readings are at
distinct times. Disturbances are arbitrary (non-affine allowed) maps of the site-0 pair at the time they act.

**Claim.** For every κ ∈ IC and every Level-1 protocol, the joint law of the record bits is i.i.d. Bernoulli(1/2).

**Proof.** Write the state after t leaps as a function of the initial data X = (u^0, v^0) and of the disturbances
δ_s (s < t), each δ_s a change of the site-0 pair at time s. The leap is affine over GF(2), so
v^t_0 = (free propagation of X)_0 + Σ_{s<t} (propagation of δ_s from (0, s))_0.
(i) Free propagation: the coefficient of v^0_{±t} in v^t_0 is 1 (Pascal-edge of the permutive rule; the rule
depends on v_{i±1} with coefficient 1 and the cone grows by exactly one site per leap), and every other initial
variable entering v^t_0 lies within radius t−1 (u^0 enters only from the second leap on, one site inside the
edge).
(ii) δ_s is a function of the site-0 pair at time s, hence of X restricted to radius ≤ s ≤ t−1 (cone), and its
propagation to (0, t) mixes only further radius ≤ t−1 data.
So v^t_0 = v^0_t + v^0_{−t} + h_t(X|_{radius ≤ t−1}). The variable v^0_t is uniform and independent of
X|_{radius ≤ t−1} (and v^0_{−t} too), while every earlier reading and every earlier disturbance is a function of
X|_{radius ≤ t−1}. Hence the reading at time t is a fair bit independent of all earlier readings. Induction on t.
The reading at t = 0 is v^0_0, fair. ∎

**Consequences.** All Level-1 effect rows are proportional to the unit, the protocol table has rank 1, the
non-selective observation m and idling i give the same row on every effect (operationally non-invasive although
f_κ ≠ id on the state for every κ ≠ passive), and C = span(unit) has dim 1 for all 143 interfaces. The `s` letter
of Level 2 breaks step (ii)'s premise that readings are of v^t_0 at the current time (s exposes u_0 = an older v_0),
which is why Level 2 is the first place the linear rule can do anything.
