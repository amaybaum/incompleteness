# SUBSTATE-1: smallest shared native gauge/observation sourcing gate

**Status:** research-only; compare the conditional non-Abelian exponential-link candidate in SM §6.5 and its still-unproved physical/measure premises.
Tracking #1007, draft PR #1009 and #1003. This note distinguishes (i) a
rigorous rejection of one simple link extraction from the *actual* cubic
wave rule; (ii) a successful **invented** gauge-pointer extension toy;
(iii) the still-open physical sourcing of either a YM action or an
operational quantum measurement. No manuscript change or status upgrade.

## Actual OI reference input

The retained finite cubic wave update in
\`papers/oi_lattice_code/trace_out_fractional/wave_eqn.c\` has, at a site,
\[
(f_{t+1})_x=\left(\sum_{y\sim x}(f_t)_y-(f_{t-1})_x\right)
\bmod q.
\]
On the full current/previous-slice configuration its inverse is
\((f_{t+1},f_t)\mapsto(f_t,\sum_{y\sim x}f_t(y)-f_{t+1}(x))\).
This is a **genuine two-slice reversible microscopic update** (for the
stated model), but it has neither a sourced link variable nor a pointer
readout in the formula. SM §4.1 distinguishes it from the normalized
\(\alpha=1/3\) observer-level wave operator.

**Existing conditional link candidate, not a verified native gauge interaction.**
SM §6.5 proposes \(M_{xy}=\exp[(2\pi i/q)\,\mathrm{Lie}(\phi_y-\phi_x)]\)
under separately stated scalar energy-shell and gauge-principle hypotheses.
The abelian restriction is a flat coboundary; non-Abelian commutators
can give second-order curvature. Neither local covariance under the
actual wave update nor the physical link measure and nontrivial
holonomy has been independently verified for this candidate.

## Decisive native countercontrol: scalar site differences are pure gauge

Consider the simple candidate link assignment
\[
U_{x\to y}(f)=\exp\!\left(\frac{2\pi i}{q}
                    [f_y-f_x]\right).
\]
It transforms in the expected way under a *re-description*
\(f_x\mapsto f_x+g_x\):
\[
U_{x\to y}\mapsto e^{(2\pi i/q)(g_y-g_x)}U_{x\to y}.
\]
But along **every** oriented closed path
\(x_0\to x_1\to\cdots\to x_n=x_0\), the exponent is
\(\sum_j(f_{x_{j+1}}-f_{x_j})=0\bmod q\).
Thus \(U(C)=1\) identically for every microscopic state and at every
time. All such links are pure gradients. Their Wilson plaquette
functional vanishes identically, so this candidate cannot yield a
nontrivial gauge-field distribution, Wilson-loop correlation or Yang–Mills
action, whatever the recurrence of the underlying scalar wave.

The implied local site-shift transformations do **not all**
commute with the native evolution. If a shift \(g\) is
applied to both current and previous slices, the difference between
"evolve shifted" and "shift evolved" in the new current slice
is \(Ag-2g\), where \(Ag(x)=\sum_{y\sim x}g(y)\).
For the periodic cubic \(L=3\), \(q=5\), start from zero
current/previous fields and shift \(g=\delta_0\) at one site.
At that site \(Ag=0\), so the shifted state's native next
field is \(-1=4\bmod5\), whereas the claimed transformed
unshifted next field is \(1\bmod5\). This supplies an
exact covariance counterexample for this *naive shift action*.
The commuting shifts satisfy \((A-2I)g=0\), a proper subgroup
at \(L=3,q=5\); the nonconstant tensor-product example
\(g_{xyz}=h_xh_yh_z\), \(h=(2,4,4)\), does commute.
A physical gauge transformation acting differently on link-carrier
variables is not excluded.

The companion \`native_wave_gradient_check.py\` checks the
inverse map and six scoped exact controls on four fixed fields
(including nonconstant fields and 3-D evolution), all positive.
The *universal flatness* statement is the algebraic telescope
above, not an extrapolation from those finite samples.
This calculation excludes only the abelian scalar gradient source;
it does **not** refute the conditional non-Abelian exponential map
or H-link/H-cust carrier of SM §6.5, whose covariance and dynamics
remain independently unverified.

## Fully specified but non-native link/pointer model

\`shared-gauge-pointer-candidate.md\` constructs a **new** U(1)
link and pointer microstate and two gauge-covariant reversible
read-and-kick maps. Its exact finite-grid control
\`gauge_pointer_toy_probe.py\` tests 8,192 states, 30
controls, full pointer/loop records, local gauge covariance,
inverse dynamics and back-action.

Its two controlled operations do not commute as **classical
permutations**; when the link kick is disabled they commute.
This illustrates why contextual readback, real back-action and even
noncommuting classical control are still insufficient to derive
quantum operational noncommutativity, entanglement, phase
interference or the Wilson action. The added link and apparatus
rules are unsourced physical resources relative to current OI.

## Minimal actual-native sourcing test (candidate must pass all)

1. **Link carrier:** provide a source-level map from the actual
   two-slice OI state to oriented links with at least one nontrivial
   closed-loop holonomy, **and** an explicit local gauge action
   commuting with microscopic dynamics. A pure site gradient
   fails the nontrivial-loop and update-covariance controls above.
2. **Pointer and settings:** specify finite public apparatus state,
   incoming preparation and two physically selectable
   setting-dependent update rules on the same ontology. The
   native-Y retained q10 sign is currently inaccessible and
   the q9 one-tick read has unseen-key obstructions; decoding
   after the fact is not a native measurement.
3. **Full record:** compute raw pointer, marker, herald-failure,
   initial/output loop and later carrier states; do not drop
   rejected attempts or replenish fresh pointer bits for free.
   Compare active link back-action with an explicitly decoupled
   pointer control, plus a passive observation-only control.
4. **Operational distinction:** show the *public* controlled
   operations are beyond stochastic classical reversible
   control or classical coherent-wave analogues. Mere
   noncommutation of microscopic permutations is **not**
   quantum evidence. Test composition, inert spectators and
   the independent OI F2 conditions without supplying
   complex Kraus or unitary availability as an input.
5. **Yang–Mills source:** derive an invariant link dynamics or
   effective action; discriminate #1003's \(S_1=\sum w\)
   from \(S_2=\sum w^2\), including an unconditioned Wilson
   loop and connected correlator, and test complete records
   against the equal-herald-rate selection countercontrol
   of \`yangmills-substate-bridge.md\`.

**Disposition at this head:** the naive site-gradient source
is REJECTED by an exact all-state flatness proof and an
explicit local-shift covariance counterexample. The added
link-pointer toy is ACCEPTED only as a mathematical
consistency control. A **shared physically established native** OI link/pointer interaction
remains **BLOCKED**: SM §6.5 gives a *conditional* non-Abelian link
candidate, not a verified covariant dynamical source with nontrivial
holonomy, action selection and a permitted public measurement interface.
A bounded negative result is useful; no manuscript
or full-equivalence promotion is authorized.
