# Companion: autonomous reversible sequential release

Research-only companion to the immutable mathematical candidate `bdcbd32`.
The earlier entropy-profile proof and controls are unchanged.

Fix n≥1. Let X and Y each be n binary coordinates, interpreted as interior and
radiation registers. Let a clock t belong to Z/(n+1). Define a single finite
configuration permutation P by first swapping X_(t+1) with Y_(t+1) when 0≤t<n
(and doing nothing to the data when t=n), then incrementing the clock modulo n+1.
The inverse decrements the clock and undoes that previous stage's swap. Over a
full clock period each pair swaps once, so P^(n+1) swaps X and Y and
P^(2(n+1)) is the identity on every configuration.

Prepare |0>_clock |V>_X |0^n>_Y, where one coherent subspace V has already been
chosen as in the original candidate. The clock is in a **definite configuration**.
For 0≤r≤n, P^r maps each basis vector (0,x,0) to (r,x_tail,x_prefix), where the
first r coordinates of X are zero, the first r coordinates of Y carry the
original first r coordinates of x, and the remaining Y coordinates are zero.
The clock remains a definite product factor because its update is independent
of the data. Consequently, up to tensoring fixed zero coordinates,

rho_Y(r) = Tr_{r+1,...,n} |V><V|,

and its entropy in bits is exactly the nested-cut value S_r already proved.
The same sampled V is used throughout the entire release window, so the exact
mean/purity formulas and shared-state simultaneous bound apply to this actual
toy trajectory. For a uniform GL(2m,2) preparation with k=m, the mean is within
two bits of min(r,2m−r); for mirror Bell-pair preparation the trajectory is the
exact tent. This conclusion uses an explicit release rule rather than inferring
movement of radiation from a change of names for tensor factors.

The release window ends at r=n: the radiation register contains |V> and is pure,
while X is zero. Later the clock resets and the same reversible map transfers the
state back. Already released radiation slots are untouched for the rest of the
first window, but they are **not** permanently decoupled over complete cycles.
There is no irreversible evaporation, energy conservation model, gravitational
geometry, Hawking emission, local scrambling rate or derived coherent preparation.
The uniform GL ensemble is a stipulated preparation measure, not a theorem about
orbits of that ensemble's matrices. This does not restore the vacuous
configuration-state GR A.8–A.9 or their physical applications.

Countercontrols: configuration input and unmixed coherent product input have
zero radiation entanglement throughout the release window; k=0 and k=n are also
zero. A coherent clock need not preserve the claimed data purity. For n=1,
clock |+>, X |+>, Y |0>, the first step gives reduced-Y purity3/4 rather than1.
Thus even the elementary clocked toy requires its definite-clock premise.
The exact inverse, full reversible period, window formula, extreme ranks and
clock counterexample are tested by `sequential_release_controls.py`.
