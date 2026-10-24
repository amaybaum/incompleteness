# Equal heralds do not ensure equivalent joint records

Exploratory read-only handoff v1, 2026-10-22. This is a new diagnostic of the
emission-map proposal, not a C-SPH-1 rerun, acceptance experiment, or derivation
of a native clock or detector. No repository files or external records changed.

## 1. Review12 and its precise implication

I read the review and checker at
[`780ad5d2ef4e637dbaece1bc132e168c7ff618ca`](https://github.com/amaybaum/incompleteness/commit/780ad5d2ef4e637dbaece1bc132e168c7ff618ca),
under `mc-node9/design/owner-checks/report12/` within the reconstruction research
tree. Its attempt-count finding is correct. I independently recomputed the
original finite-source rates and the censored geometric distance exactly.

For per-trial rates p >= q > 0 and at most m attempts,

\[
 d_{TV}(G_{p,m},G_{q,m})
 =\max_{1\leq j\leq m}\{(1-q)^j-(1-p)^j\}.
\]

Here the record is the first successful attempt or all-fail. The likelihood
ratio of the success-at-j probabilities decreases with j, so the positive part
of their difference is a prefix. The all-fail mass has the opposite sign.
The maximum difference of prefix probabilities is therefore the full TV.
The checker compares this formula to the direct absolute-difference sum.

| n | Attempt-only TV, m=256 |
| --- | --- |
| 7 | 0.011829311867 |
| 15 | 0.005020820371 |
| 31 | 0.002380300466 |
| 63 | 0.001167252923 |
| 127 | 0.000577797726 |

These reproduce the review. I have not proved its suggested 1/n asymptotic.
The continuous-depth variant removes the arithmetic timing witness but leaves
these herald distances, as the review states.

Two scope distinctions: approximate equivalence permits a bounded rate error;
exact equivalence requires the appropriate record identities exactly. Moreover,
station-independent heralding is not a universal requirement of quantum theory:
a legitimate state-dependent herald can have a probability affine in the density
matrix. In the present centrally symmetric model p_w=p_-w, equality of the
antipodal I/2 preparations does require the rates to agree across the axes.

## 2. A countercontrol that removes both herald leaks

Before trying to implement a clock, I tested whether correcting the source's
orientation alone would suffice. Keep the previous independent bit sums
S=(S_x,S_y,S_z), with each component a sum of n fair +/-1 bits, n odd. Keep
D uniform on 1,...,M, where M is the smallest power of two at least 9n.

Change the supplied velocity interpretation: orient the same finite source
distribution with each station. For w in {X,Y,Z,R}, choose an orthogonal Q_w
with Q_w X=w and set V_w=5 Q_w S/n. In particular,

\[
 Q_R S=((4S_x-3S_y)/5,(3S_x+4S_y)/5,S_z),
 \qquad R=(4/5,3/5,0).
\]

For -w use the centrally inverted velocity. Because the source law is invariant
under coordinate sign changes, this also has a proper-rotation realization at
the level of distributions. The checker uses explicit signed frames for clarity.

The initial depth is D/n and the stipulated ballistic plane crossing now has

\[
 P_w=n\,w\cdot V_w=5S_x,\qquad
 \mathrm{success}\iff 1\leq D\leq 5S_x,\qquad T=D/(5S_x).
\]

Thus the entire herald law is IDENTICAL at all eight stations, exactly at every
finite n: successes, failed attempts, first-success index, and exact timestamps.
The old denominator event no longer distinguishes stations. The conditional
angular weak limit is still the projected-area law, since rotating the Gaussian
limit rotates its cosine-weighted hemisphere.

This is a diagnostic modification, not a native implementation. It changes the
source/plane alignment from the original common laboratory-frame distribution.
The native wave has not been shown to build these oriented carriers. In
particular, the R rotation is not a signed permutation symmetry of the spatial
cubic lattice. No claim is made that station rotation is free or dynamically
derived.

The favorable result requires a harder test. Every antipodal equal mixture still
gives a fair terminal sign read conditional on its entire herald record. Those
I/2 tests therefore all pass, including the joint clock/read record.

## 3. Another equivalent pair fails through clock/read correlations

Let P_w denote the preparation assigned the pure Bloch vector w. Compare

\[
 A=\tfrac{13}{16}P_R+\tfrac3{16}P_{-R},\qquad
 B=\tfrac12P_X+\tfrac38P_Y+
       \tfrac1{16}P_Z+\tfrac1{16}P_{-Z}.
\]

Both have the SAME quantum-reference Bloch vector
(1/2,3/8,0), hence density matrix (I+(1/2)sigma_x+(3/8)sigma_y)/2.
Each preparation coin can be drawn exactly from four independent fair bits:
A assigns 13 of the 16 values to R+, and B assigns 8,6,1,1 values to its four
stations. These coin bits are independent of all trial bits.
The preparation coin and station remain hidden, with a common schedule. Select
the station once, allow at most 256 independent trials at it, and on success
make a terminal X read. No reset or second instrument is involved. Keep all
failures in the record.

For a successful timestamp t, let h_t count (S_x,S_y,D) microstates with their
binomial multiplicities. Let k_t count those additionally satisfying
4S_x-3S_y>0. This is R's X-positive read. Then

\[
 \Pr_A(X+\mid t)=\tfrac3{16}+\tfrac58\frac{k_t}{h_t},
 \qquad \Pr_B(X+\mid t)=\tfrac34.
\]

The second identity holds because X+ reads positive with certainty, whereas
Y+ and both Z preparations have fair X reads conditional on the timestamp.
Let C=sum_t h_t, p=C/(M 4^n), and c=1-(1-p)^256. The exact COMPLETE-record TV is

\[
 d_{TV}(A,B)=\frac{c}{16C}\sum_t|10k_t-9h_t|.
\]

The all-fail masses agree. Each success-attempt factor is the same for A and B;
summing those factors gives c. Thus this is not a postselected distance.

| n | Joint attempt/time/read TV | TV with the crossing time omitted | Completion |
| --- | --- | --- | --- |
| 15 | 0.040614656430 | 0.000024720364 | 0.999657166211 |
| 31 | 0.046889907268 | 0.001212007354 | 0.996517868697 |
| 63 | 0.043770460871 | 0.000639824906 | 0.981776369544 |
| 127 | 0.041774027592 | 0.000304799578 | 0.941048489206 |

The rates and the entire herald distributions agree exactly. The residual
time-blind read error is small in these examples. Their joint record has a much
larger discrepancy. No limiting nonzero TV is asserted from this table.

A simple explicit event also witnesses the failure, without using the optimal
TV event: a success occurs by attempt 256, the reduced denominator of its
crossing time satisfies den(T)^2 > 25n, and the terminal X read is positive.
At n=63 its probability under A exceeds that under B by
0.017754798729564858... . The checker verifies the difference exceeds 1/64 in
exact rational arithmetic; it also verifies the full TV exceeds 7/160. These
are exploratory witness inequalities, not preregistered acceptance thresholds.

Mechanism: the clock carries information about the normal component S_x.
For R, that component affects the subsequent X read. For the X/Y/Z mixture it
does so differently. Equal herald marginals therefore do not remove the joint
correlation. An independent-clock countercontrol, with exactly the same herald
and read marginals, reduces the TV precisely to the time-blind column. That
countercontrol isolates the correlation; it does not supply a physical way to
erase or protect the original time information.

The exact rational clock remains an additional accessible observable of this
kinematic candidate. This witness is not an OI no-go theorem or a claim that
the native discrete wave supplies such a clock.

## 4. Four complete preparation identities for this menu

There is a sharper target than separately checking success rates, timing
marginals, and a few mixed states. Fix an allowed protocol and let K_w be its
probability MEASURE on the complete public record, starting from preparation w.
Classical randomization must mix these measures with the preparation weights.

For the eight preparations +/-X,+/-Y,+/-Z,+/-R, equivalence for every pair of
mixtures with the same Bloch vector holds if and only if these four signed
measure identities hold:

\[
\begin{aligned}
 K_X+K_{-X}&=K_Y+K_{-Y},\\
 K_X+K_{-X}&=K_Z+K_{-Z},\\
 K_X+K_{-X}&=K_R+K_{-R},\\
 5(K_R-K_{-R})&=4(K_X-K_{-X})+3(K_Y-K_{-Y}).
\end{aligned}
\]

These must hold on every measurable record event, not merely after forgetting
timestamps or failures. In a finite record space they hold at each record atom.

Proof: the 4-by-8 matrix with columns (1,w_x,w_y,w_z) has rank four. Differences
between equal-state mixing weights lie in its nullspace. The four displayed
relations give four independent null vectors, so they span it. Conversely, any
nonzero null vector has positive and negative parts with equal total mass;
normalizing those parts yields two equivalent mixtures. Thus equality of all
such mixtures is exactly annihilation of this nullspace. The checker verifies
both ranks and all products with exact fractions. This is ordinary affine
linear algebra applied to the whole record, not a new quantum reconstruction.

The first three relations are the antipodal I/2 tests. The rotated-source
candidate passes them and fails the fourth. This explains exactly why the
earlier unbiased-mixture tests miss the new witness.

This criterion concerns operational record probabilities. It does NOT require
equal microscopic hidden-state distributions for equivalent preparations and
does not assume ontological preparation noncontextuality. For context on that
distinct, stronger notion, see Spekkens, Phys. Rev. A 71, 052108 (2005),
[primary paper](https://doi.org/10.1103/PhysRevA.71.052108). No no-go theorem from
that paper is used here.

The criterion is complete for preparation equivalence within this finite menu
and one fixed protocol. It does not establish the Born rule, correct outgoing
instruments, all protocols, additional axes, or composites. Applying it to all
protocols requires either their record laws or a theorem covering the family.

## 5. A conditional joint-record convergence result for finite clocks

The failure of the exact-time interface does not rule out bounded approximation
with a physically justified finite clock. There is a direct bound that controls
the correlation, rather than only the clock marginal.

Let B equal-width bins partition (0,1]. For a positive integer normal speed P,
the number of depth labels in bin j is floor(jP/B)-floor((j-1)P/B). Write
r(P)=P mod B. There are r bins with floor(P/B)+1 labels, and B-r bins with
floor(P/B) labels. Let L denote the joint law of the accepted velocity and bin,
conditional on success. Let L_vel be its velocity marginal. Direct counting
gives

\[
 d_{TV}(L,L_{vel}\otimes U_B)
 =\frac{\mathbb E[1_{P>0}r(P)(B-r(P))/B]}{\mathbb E[P_+]}
 \leq\frac{B\Pr(P>0)}{4\mathbb E[P_+]}
 =\frac{B}{8\mathbb E[P_+]}.
\]

Here P=5S_x, and Pr(P>0)=1/2 for odd n. The equality compares two finite
velocity distributions, not an atomic law to a continuous angular law.
The derivation is the exact absolute-difference sum for the bin counts. The
checker independently assigns every depth to its bin and verifies the residue
formula and bound in twelve cases. A one-bin clock has exactly zero correlation.

Since E[P_+] is asymptotic to 5 sqrt(n/(2 pi)), the bound is O(B/sqrt(n)).
For fixed B, or B growing more slowly than sqrt(n), it vanishes. The absolute
moment asymptotic follows from the one-dimensional central limit theorem and
the uniformly bounded second moment of S_x/sqrt(n).

After applying a fixed sign read, TV can only decrease. Combining this bound
with the angular convergence on a fixed finite menu gives joint clock/read
convergence to a uniform bin independent of the Born read. In this rotated
candidate all stations already have exactly the same rate p_n. Adding the
first-success attempt and all-fail record multiplies the conditional error by
the completion probability, so any finite retry budget, including one that
grows with n, does not amplify this single-call bound. The comparison reference
uses that same p_n; fixed throughput is not claimed.

More explicitly, if delta_n is the largest time-blind single-read error on the
fixed preparation/read menus, any two equivalent mixtures A,B satisfy
d_TV(P_A,P_B) <= 2 c [delta_n + B/(8 E[P_+])] for this single-call protocol,
where c is their common completion probability. Both terms vanish under the
conditions just stated. This bound does not assume small exact-clock TV.

This is a conditional convergence theorem for the stipulated record interface,
not a native clock construction. It provides no privacy against a finer clock,
an impact probe, or later access to stored detector information. No asymptotic
claim for the exact-time witness follows from it.

## 6. Consequence for the native-emission target

The useful result is a stronger necessary test, not a completed physical map.
The investigation has now separated three obligations:

1. The source must supply the proposed angular statistics under the actual
   readiness and call conditions.
2. The physical clock/emission/detector interaction must produce the complete
   joint record law, including correlations of returned times with later reads.
3. The stated observation interface must be justified for all permitted probes
   over the claimed horizon; a reversible register that merely stores the fine
   time somewhere else does not establish its inaccessibility.

For the next native candidate, specify one autonomous reversible update for
the wave, clock, carrier and detector, its ready-state ensemble, and its public
registers. Derive the four record identities (or an explicit bounded-error
version) from that update. Include effects of detector coupling on the source;
the passive-source freshness lemma alone does not cover unspecified backreaction.
Do not accept station-independent heralds as a substitute for those identities.

Neither this diagnostic nor the earlier handoff derives that update. The
manuscript's finite operational realization theorem (Main §3.4) is an existence
construction using supplied instruments; it does not identify this physical
emitter. SM §§3 and 4.1 distinguish fixed linear dynamics from state-dependent
couplings and from observer-level projection. I checked those passages at the
review12 snapshot; no general impossibility claim about their broader class is
being made here. The immediate unresolved task remains a native interaction
and access argument, not further optimization of C-SPH-1.

## 7. Evidence

`joint_record_checks.py` uses only the Python standard library, integer counts,
and exact fractions. It has no randomness, file writes, network access or
repository imports, and uses explicit exceptions rather than removable asserts.

Independent paths: the old attempt law is checked by both prefix probabilities
and direct TV; at n=1,3, literal 3D bit/depth enumeration with explicit lab-frame
velocities reproduces the aggregated joint law and checks all eight herald
distributions; exact quantum menu effects satisfy all four identities, whereas
the candidate passes the first three and fails the fourth. The separate-clock
countercontrol preserves the marginals exactly. The finite-bin bound is checked
against separate direct depth assignments. The larger-n calculations are
exact combinatorial sums, not Monte Carlo or interval integration.

Normal and optimized Python runs from separate temporary directories reproduce
the included output byte for byte. The manifest covers the report, README,
checker, and expected output. PASS means these identities and scoped witnesses
were checked. It does not accept a physical apparatus.
