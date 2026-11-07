# Minimal two-system interface: shared-parity candidate and reuse screen

Author analysis; independent review pending. This paper tests one common finite reversible
candidate against a deliberately restricted two-system target. It does not assert a native
physical realization, adopt an extension, or change the full endpoint in [Gate A](endpoints.md).

## 1. Question and fixed comparison

Can a shared hidden parity resource give the embedded observers quantum Bell statistics,
usable records, and a second measurement under the same rules? A hidden variable need not
be directly decoded to matter operationally. Determinism is permitted. The tests concern
the observers' complete accessible histories.

The smallest comparison used here has two qubits initially in
\[
 |\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2,
 \qquad A_0=Z,\quad A_1=X,\quad
 B_0=(Z+X)/\sqrt2,\quad B_1=(Z-X)/\sqrt2 .
\]
Outcome bits \(a,b\) denote eigenvalues \((-1)^a,(-1)^b\). At each measurement the
comparator uses the **local projective Lüders instruments** for these observables.
Every pair \(x,y\in\{0,1\}\) is available. Its first-read law is
\[
 Q(a,b\mid x,y)=\frac{1+(-1)^{a\oplus b\oplus xy}/\sqrt2}{4}.                 \tag{1}
\]
This is a specified QM comparator, not a proposed native probability rule. Direct evaluation
uses \(\langle ZZ\rangle=\langle XX\rangle=1\), vanishing mixed \(ZX,XZ\)
expectations, and zero local means in \(\Phi^+\). The same Bell comparison appears in
the existing MR-star amendment, §M.5, B-T6 [S3]; no new Bell benchmark is claimed.

The restricted experiment family consists of:

- one preparation, followed by one or two measurement rounds;
- all four first-round setting pairs and all sixteen fixed two-round setting sequences;
- each wing retaining and rereading its own setting, outcome and preparation-status records;
- a preparation status \(H\), recorded before settings interact: \(H=1\) means the declared
  ready preparation, and \(H=0\) means failure with recorded outcome \(\bot\) at both rounds.

For accounting, let \(\Pr(H=1)=h>0\), independent of the chosen protocol. On failure,
all outcomes are \(\bot\); the run remains in the probability law. The ideal comparison has
\(h=1\). Allowing \(0<h<1\) is an explicitly supplied, setting-independent heralded
preparation channel, not a derived detector-efficiency model. No conditioning on a later
successful detection or setting-dependent selection is admitted.

This family is strictly smaller than \(J_{\rm exact}\): it does not contain arbitrary
preparations, instruments, adaptive trees or ancillas. Failure here excludes this candidate
from a correspondence that includes this family. Success here would not establish the full
equivalence.

## 2. One reversible candidate, one source law

All additions below are explicit abstract apparatus assumptions. The candidate is motivated
by the minimal reversible use of a hidden relation at two ports. It is **not** a compiled
extension of the finite-wave paper, Native A, or B3.

Use bits \(R,C\), isolated setting slots \(x_1,y_1,x_2,y_2\), two outcome slots
\((a_i,b_i)\), the herald \(H\), and a three-state clock \(k\in\mathbb Z/3\).
These form one finite product space \(\Omega\). On the source's ready support, \(k=0\)
and all four outcome bits are zero. Conditional on \(H=1\),
\[
 \Pr(R=r,C=c\mid H=1)=\tfrac12 w_\eta(c),\qquad
 w_\eta(0)=1-\eta,\quad w_\eta(1)=\eta,\quad 0\le\eta\le1.                   \tag{2}
\]
Thus \(R\) is fair and independent of \(C\); the entire uncontrolled source is independent
of settings. For definiteness the failure source has \(R=C=0\) and zero outcome slots.
The particular source used for the target comparison below fixes one value of \(\eta\).
Changing \(\eta\) later is not an admitted baseline measurement choice.

At clock value \(k=i-1\), for \(i=1,2\), apply
\[
 a_i\longmapsto a_i\oplus HR,\qquad
 b_i\longmapsto b_i\oplus H(R\oplus x_i y_i\oplus C).                       \tag{3}
\]
At \(k=2\) apply no bit gate. Then advance \(k\) by one modulo three. All other
registers are unchanged. This defines a single autonomous permutation \(\Phi\) on
**every** configuration, not just the zero-pointer support: decrement the clock and apply
the corresponding XOR gate to invert it. No setting-specific change of \(\Phi\) occurs.

The \(x_i y_i\) term requires a cross-wing controlled interaction. It explicitly gives up
the remote-setting graph-cone isolation of Main §3.3 [S1]. A Boolean reversible specification
does not supply a physical interaction, preparation-induced edge, clock or controller.
There is no claim that the original nearest-neighbor wave rule realizes (3).

For the fixed protocols in this screen, the program slots may be loaded initially. Future
slots do not enter either first-round gate. Changing \(x_2,y_2\) therefore preserves the
first-round uncontrolled state and all first-round records. This proves an algebraic
prefix property of the specified circuit. Physical loading and fresh/adaptive setting
selection remain source obligations; no arbitrary adaptive-controller construction is
claimed.

After round \(i\), wing A observes its \(x_i,a_i,H\), and wing B observes its
\(y_i,b_i,H\). For \(H=0\) both outcome maps return \(\bot\). Each wing may retain
its own complete record and compare successive outcomes. Neither can initially read \(R\),
\(C\), or the other wing's setting slot. This access restriction is supplied, not derived.

The second gate leaves first-round slots unchanged. The two-round observation window ends
at \(k=2\), before clock wrap can cause a later overwrite. The record map is nondestructive
as a mathematical projection during this window. A physical repeated-read detector,
longer retention, stopping controller, reset, and resources for arbitrary depth are not
provided by this definition.

## 3. First-read calculation and source dependence

On \(H=1\), the first output is
\[
 a=R,\qquad b=R\oplus xy\oplus C .
\]
Consequently
\[
 P_\eta(a,b\mid x,y,H=1)=\tfrac12 w_\eta(a\oplus b\oplus xy),\qquad
 E_{xy}=(-1)^{xy}(1-2\eta),\qquad S=4(1-2\eta).                            \tag{4}
\]
Both one-round marginals are fair for every \(x,y,\eta\). At
\[
 \eta_*=\frac{1-1/\sqrt2}{2},                                               \tag{5}
\]
(4) equals (1) at all four settings, with \(S=2\sqrt2\). This is an exact
**calibration**, not a derivation of the quantum coefficient: (5) was selected from
the comparator. Neither a natural source for (2) nor a principle selecting (5) is supplied.

The complete first-round law includes
\[
 \Pr(H=1,a,b\mid x,y)=\frac h2 w_\eta(a\oplus b\oplus xy),\qquad
 \Pr(H=0,\bot,\bot\mid x,y)=1-h.                                          \tag{6}
\]
These masses sum to one. No discarded failure mass is renormalized into a Bell claim.
A truthful, settings-independent herald and its rate \(h\) are assumptions of this
candidate, not evidence that a physical preparation or failure monitor exists.

Useful source countercontrols follow immediately:

| Countercontrol | Exact consequence | Scope |
|---|---|---|
| \(\eta=1/2\), fair \(R\) | \(S=0\), uniform first-read joint law | Same gate, different hypothetical source |
| \(\eta=0\), fair \(R\) | \(a\oplus b=xy\), \(S=4\), fair marginals: PR behavior | Not asserted physically preparable |
| \(\eta<\eta_*\) or \(\eta>1-\eta_*\), fair \(R\) | \(|S|>2\sqrt2\) | A source class admitting these values fails quantum soundness |
| \(\Pr(R=1)=p\), independent of \(C\) | For \(y=1\), changing \(x\) changes Bob's zero-outcome probability by magnitude \(|(1-2p)(1-2\eta)|\) | Shows the dependence of one-round masking on source balance |

The quantum ceiling in the third row is the standard CHSH operator bound for local
binary observables. For \(\mathcal B=A_0\otimes(B_0+B_1)+A_1\otimes(B_0-B_1)\)
with \(A_i^2=B_j^2=I\),
\(\mathcal B^2=4I-[A_0,A_1]\otimes[B_0,B_1]\) and
\(\|\mathcal B\|\le2\sqrt2\). This is an imported QM comparison, not an OI axiom.

Restricting the candidate to the single source \(\eta_*\) avoids these particular
one-round countercontrols by stipulation. It does not physically justify that restriction,
exclude other accessible source manipulations, or solve the reuse failure below.

## 4. Complete continuation under the same rules

There is no reset of \(R,C\), no replacement preparation and no fresh hidden mask between
measurements. For any of the sixteen setting sequences and \(H=1\), the full history law is
\[
\begin{split}
 &P_\eta(a_1,b_1,a_2,b_2\mid x_1,y_1,x_2,y_2,H=1)\\
 &\quad=\tfrac12w_\eta(a_1\oplus b_1\oplus x_1y_1)\,
       {\bf1}_{a_2=a_1}\,
       {\bf1}_{b_2=b_1\oplus x_1y_1\oplus x_2y_2}.                         \tag{7}
\end{split}
\]
Multiply (7) by \(h\) for the unconditional successful-history mass and add the one
all-\(\bot\) failure history of mass \(1-h\). Equation (7) accounts for every history
and is normalized: summing over \(a_2,b_2\) leaves (4).

The remaining-state law is also explicit. Conditional on a positive-mass first history,
\[
 R=a_1,\qquad C=a_1\oplus b_1\oplus x_1y_1 .                               \tag{8}
\]
All other registers are those in §2: first outcomes are retained, second outcome slots
remain zero until the second gate, the program slots are unchanged, and the clock is one.
Applying \(\Phi\) gives precisely (7) and clock two. Before conditioning, the complete
outgoing state is the mixture of these four deterministic register configurations with
weights \(\frac12 w_\eta(C)\). The failure branch remains its specified deterministic
state with null observable outcomes. No hidden reservoir or outgoing state has been
dropped from the calculation.

For the **same** local Lüders instruments in §1, the quantum conditional continuation is
\[
\begin{split}
 &Q(a_2,b_2\mid a_1,b_1,x_1,y_1,x_2,y_2)\\
 &\quad=\frac{1+(-1)^{a_1\oplus a_2}\delta_{x_1x_2}}2\,
         \frac{1+(-1)^{b_1\oplus b_2}\delta_{y_1y_2}}2.                    \tag{9}
\end{split}
\]
Here \(\delta\) is the equality indicator. The first local rank-one projective
measurements leave their outcome-conditioned product eigenstate. The two axes on either
wing are orthogonal, giving (9). Multiplying (9) by (1) defines the full quantum
two-round law; a different post-measurement state cannot be chosen to rescue (7).

### A usable signal from local records

Choose \(y_1=0\), \(y_2=1\), and fix any \(x_1\). Let Alice's isolated second
setting encode a freely selected bit \(z=x_2\). Bob's own record gives
\[
 b_1=R\oplus C,\qquad b_2=R\oplus C\oplus z,\qquad
                         b_1\oplus b_2=z.                                \tag{10}
\]
The first-round state and records do not depend on \(z\); the uncontrolled source law
is the same for both messages. Bob learns \(z\) after the second interaction without
receiving Alice's outcome or reading either hidden variable separately. For every
\(\eta\), including \(\eta_*\), the successful-run local-history distribution is
\[
 \Pr(b_1=u,b_2=v\mid H=1,z)=\tfrac12{\bf1}_{v=u\oplus z}.                 \tag{11}
\]
Its supports for \(z=0\) and \(z=1\) are disjoint. The unconditional distributions share
only the failure branch and have total-variation distance \(h\). This is a usable
signalling channel whenever \(h>0\), not a postselected detection loophole. At \(h=1\)
it transmits the chosen bit perfectly.

In the quantum comparator Bob instead has
\(Q(b_1=u,b_2=v\mid H=1,z)=1/4\), independent of Alice's settings: the local
\(B_0\) and \(B_1\) axes are orthogonal and Alice's uncommunicated local instruments
cannot alter Bob's marginal history. Thus the failure is already an observable
two-round discrepancy, not an interpretation of the ontic state.

This is operational signalling across the stipulated two-wing interface. No physical
speed, laboratory separation or native implementation is established, so it is not a
claim that an actual OI device sends faster-than-light messages. The abstract coupling
was explicitly nonlocal; the failed obligation is masking its influence from the
embedded observers throughout the admitted protocol.

### Why a silent fresh-source replacement is not a repair

Giving each measurement an independent new \(R,C\) would define a different process.
It would remove the shared-mask cancellation in (10), but even at unchanged \(x,y\)
it would give \(\Pr(a_2=a_1)=1/2\). The repeated Lüders measurement in (9) requires
\(\Pr(a_2=a_1)=1\). A labelled re-preparation of a new Bell pair is a different
experiment from reusing the measured pair. A physical state-update mechanism remains
necessary; replacing the consumed state silently is not a correspondence.

## 5. Source and access ledger

| Ingredient | Supplied mathematical fact | Physical obligation |
|---|---|---|
| One common reversible evolution | The permutation and inverse in (3) | Source a native cross-wing coupling, clock and executing controller; not derived from the wave rule |
| Preparation | Ready support and source (2) | Produce the correlated apparatus state, balanced mask and calibrated law without fitting future settings |
| Choices | Program independence and prefix isolation for the fixed protocols | Physically load/select settings while preserving preparation and records |
| Failures | Complete law (6) and its two-round extension | A truthful herald, actual preparation rate and a treatment of all real error modes; none derived here |
| Accessible records | Local projections, retained first slots through the second gate | A physical read mechanism, read access and retention; no privacy inferred merely from an unread register |
| Continuation | Complete remaining-state law (8) | It demonstrably fails (9) and operational no-signalling; longer resource supply cannot erase that failure |
| Composite selection | Four calibrated first-read correlations | Independently constrain the full admitted source/operation class; a chosen quantum coefficient or no-signalling alone is insufficient |

The response-table existence result in Main [S1] and the CC8 control in MR-star [S3]
already permit supplied finite quantum laws. This paper does not offer that existing
representability as a new reconstruction. Its specific screen concerns the explicitly
retained shared-parity state, not every response-table implementation. An implementation
that stores a different response for each history is not this candidate.

The recent finite-wave correlation-recovery paper [S4] motivates testing indirect access
and supplies its own scoped positive result. It is not used as a premise that (2), (3),
the detector, or this composite exists natively. Its previous review and CI do not
validate this new model. Main's conditional Bell ceiling and its proposed
parameter-dependent branch remain unchanged. Substratum's additional H-Bell
curvature/geometry obligations [S2] are not addressed by a two-port circuit.

## 6. Result and next physical requirement

**Author result, pending independent review:** this common-model candidate fails the
requested operational standard. A supplied source can match all four first-read quantum
correlations and give fair one-read marginals. Reusing its unchanged hidden resource
produces the explicit local-history signal (10), even at that exact calibration.
Its physical source/access obligations were already unsupplied. An enlarged source
class can also admit PR behavior by (4), but that is a separate conditional countercontrol,
not a claim that the fixed baseline source admits a PR preparation.

The failure is neither a no-go for deterministic OI nor a requirement to decode hidden
memory directly. The very indirect recovery allowed by the operational criterion exposes
why this particular no-signalling argument is insufficient.

A successor must supply an interaction-derived post-measurement state and record/resource
policy whose **whole local histories** remain independent of remote choices, while
retaining the comparator's repeatability and other conditional transitions. Its
allowed preparation and control class must be physically justified and checked for
nonquantum behavior. Merely replacing the noise coefficient or appending fresh randomness
does not discharge those obligations. No successor mechanism is selected here.

Accountable routes: #1169 owns this comparison; #866 owns physical interaction/access,
#868 joint-test/composition sourcing, #1032 retention, and #913 O-REUSE. #914 retains
the dependency map. The full \(J_{\rm exact}\) equivalence and all broader source
questions remain open.

## Sources

- **S1.** [Main, §§3.3–3.4](https://github.com/amaybaum/incompleteness/blob/4b14b9d4e1d984fd22674e5abb1f611c36325ed0/papers/Main.md):
  screened local Bell ceiling, nonlocal response-table scope, and finite-horizon
  representation. The two-round calculation above is self-contained.
- **S2.** [Substratum, §3.2](https://github.com/amaybaum/incompleteness/blob/4b14b9d4e1d984fd22674e5abb1f611c36325ed0/papers/Substratum.md):
  H-Bell's physical and geometric obligations, distinct from a finite circuit.
- **S3.** [MR-star, §§M.5–M.6](https://github.com/amaybaum/incompleteness/blob/4b14b9d4e1d984fd22674e5abb1f611c36325ed0/verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md):
  existing B-T6 comparator and CC8 supplied response-table control; read-only provenance,
  not a claim of native availability or approval of that programme's execution.
- **S4.** [Finite-wave recombination paper at its reviewed head](https://github.com/amaybaum/incompleteness/blob/9d24914c5006d775315189dadf56769e1e9cc847/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md):
  conditional indirect parity recovery and its preparation/access gaps; branch evidence
  used as motivation only.
