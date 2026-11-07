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

## 7. Explicit Barandes comparison

This section answers three separate questions about the candidate. Source [B1] defines
the finite stochastic tuple and proves its unistochastic embedding; source [B2] treats
the additional causal/composite structure used for the Bell bound. A representation of
the candidate is not an adoption of its physical assumptions.

### 7.1 Which stochastic assumptions hold?

At the full-world level, take \(\mathcal C=\Omega\), integer times
\(\mathcal T=\mathcal T_0=\mathbb Z\), and
\[
 \Gamma_{\omega'\omega}(t\leftarrow s)
       ={\bf1}_{\omega'=\Phi^{\,t-s}(\omega)},\qquad
 p(t)=\Gamma(t\leftarrow0)p(0).                                            \tag{12}
\]
Let the mathematical random-variable algebra contain all real functions on
\(\Omega\times\mathbb Z\). The source in §2 supplies \(p(0)\) for each controlled
program; its uncontrolled law remains the same across settings. Every column of
\(\Gamma\) is normalized, \(\Gamma(s\leftarrow s)=I\), and the composition rule
holds because \(\Phi\) is a permutation. These verify the finite tuple conditions
of [B1, §3.1] directly. The mathematical algebra does not make its functions physically
readable: the actual access remains the restricted record maps of §2.

The full-world process is Markovian and P-divisible. This is compatible with [B1]'s
broad class, whose definition includes Markovian special cases. Its term “indivisible
stochastic process” must not be read as requiring the particular failure of stochastic
factorization called P-indivisibility in Main.

A precise reduced map can nevertheless be P-indivisible. To see this without inferring
it just from the presence of memory, fix \(H=1\), initial clock zero and all four
settings zero. Use the raw pointer configuration
\(v=(a_1,b_1,a_2,b_2)\in\{0,1\}^4\), average the same independent source (2)
over \(R,C\), and define \(\Gamma_V(t\leftarrow0)\) for **every** initial \(v\),
at \(t=0,1,2\). These are normalized \(16\times16\) stochastic matrices with
\(\Gamma_V(0\leftarrow0)=I\). They use the already defined action of \(\Phi\)
outside its ready support, not a different gate or hidden law.

For roots \(v_\alpha=(\alpha,\alpha,0,0)\), \(\alpha=0,1\), the outputs are
\[
\begin{array}{c|c}
 t=1 & (\alpha\oplus R,\ \alpha\oplus R\oplus C,\ 0,\ 0)\\
 t=2 & (\alpha\oplus R,\ \alpha\oplus R\oplus C,\ R,\ R\oplus C).
\end{array}                                                               \tag{13}
\]
The time-one distributions for the two roots are identical: replace the fair bit \(R\)
by \(R\oplus1\). At time two they have disjoint support because \(a_1\oplus a_2=\alpha\).
Consequently no stochastic \(D\) can satisfy
\(\Gamma_V(2\leftarrow0)=D\Gamma_V(1\leftarrow0)\): equal input columns at time
one could not become unequal at time two. This is an explicit P-indivisibility witness
for this specified reduced family, for every \(\eta\).

**Scope:** the second root is not a supplied ready preparation in the experiment of §1.
The witness is a property of the formal root extension, not a claim that an observer
can prepare both roots, nor a classification of every possible observer projection.
The original experimental interface and its source remain unchanged. The point is
that P-indivisibility of an explicitly defined reduced map can coexist with the
candidate's observable reuse failure; it is not a certificate of operational QM.

### 7.2 Does a representation preserve the records and interventions?

For this particular candidate, a global representation is explicit, without invoking an
unspecified choice of dilation: on \(\mathbb C^\Omega\), set
\(U|\omega\rangle=|\Phi(\omega)\rangle\) and
\(\rho_0=\sum_\omega p(0)_\omega|\omega\rangle\langle\omega|\).
All register reads are diagonal projectors. The state remains diagonal, and sequential
conditioning on those reads has exactly the same effect as classical conditioning.
Thus this **one global permutation unitary**, with the declared controlled program slots,
preserves the complete laws (6)–(8), their failures and their recorded histories.
This construction is also the elementary permutation case discussed in [B1, §4.3].

What it preserves includes the nonlocal controlled gate and the signal in (10).
It is a quantum simulation of the complete specified apparatus with that interaction.
It is not a realization of the stipulated pair of separated local quantum instruments.
The availability of the native loader, clocks and detectors is still unproved.

For a reduced transition dictionary alone, higher-history preservation needs an additional
check: [B1, §3.1, discussion after Eq. (38)] explicitly distinguishes its stochastic tuple
from the more detailed higher-order laws of a realizer. Here those laws are fixed by
\(\Phi\) and (2); they may not be replaced by another realizer that merely shares
selected transition matrices.

### 7.3 Which Bell-bound assumptions are missing?

[B2, §3.3, Eqs. (22)–(24)] defines causal independence through marginal transition
laws conditioned on subsystem configurations. Its §4.2 proof uses a common bipartite
representation with setting-local operations
\((\mathcal{AB})_{xy}=\mathcal A_x\otimes\mathcal B_y\), immediately before
Eq. (30). The proof's local-operation structure is the relevant bridge to check;
fair outcome marginals alone do not verify it. This audit does not claim a new
derivation of that source's locality-to-factorization step.

| Requirement relevant to applying that route here | Candidate-specific assessment |
|---|---|
| Finite configurations and normalized time-directed dynamics | Supplied mathematically by (12), including Markovian special cases |
| Composite configuration space | The registers form a Cartesian product; this alone supplies no causal separation or local instrument dictionary for the two observers |
| One preparation independent of subsequent settings | Stipulated in (2), not physically sourced |
| Common representation of actual setting operations and records | The global permutation representation above works, including its nonlocal coupling |
| Causal locality for the intended separated-wing experiment | Not supplied: the \(x_i y_i\) interaction is explicitly cross-wing, with no spacetime/locality realization |
| A faithful local-instrument representation throughout reuse | Incompatible with (11) under the stated no-communication comparison, as shown below |
| Division/decoherence, apparatus records and subsequent resource policy | No physical division event or reset is derived; the retained source and finite record window are those of §§2–4 |

The last substantive incompatibility can be proved at the operational level, so it does
not depend on how one distributes \(R,C\) between hidden subsystems. Suppose one common,
setting-independent state \(\rho\) and local instruments faithfully represented the
two-round experiment, including all local records and failures. For fixed local setting
sequences \(\mathbf x,\mathbf y\), let \(\mathcal A_{\alpha|\mathbf x}\) and
\(\mathcal B_{\beta|\mathbf y}\) denote their complete-history branch maps.
Summing over all Alice histories gives a trace-preserving map. Therefore
\[
 \Pr(\beta\mid\mathbf x,\mathbf y)
 =\sum_\alpha\operatorname{tr}
       [(\mathcal A_{\alpha|\mathbf x}\otimes\mathcal B_{\beta|\mathbf y})(\rho)]
 =\operatorname{tr}
       [\rho(I\otimes\mathcal B_{\beta|\mathbf y}^{\dagger}(I))].             \tag{14}
\]
The right side does not depend on \(\mathbf x\). Fixed retained local ancillas and
resource registers may be included in the local maps and \(\rho\); this does not change
the argument. A prior herald independent of settings can be included in the preparation,
with its failure outcomes retained. A history-conditioned comparison is made only where
that history has positive probability.

But (11) depends on \(x_2=z\) in Bob's whole record, with nonzero unconditional difference
whenever \(h>0\). Hence **no such faithful local-instrument correspondence exists for
this candidate's full two-round interface**, even though its first-read probabilities
at \(\eta_*\) possess the familiar quantum realization (1). The source's Bell proof
concerns one round; extending the local instrument structure to the records and reuse
tested here is an explicit additional compatibility obligation, not a theorem attributed
to [B2].

This does not identify conditional correlations obtained by learning Alice's outcome with
signalling. Equation (14) sums over every Alice outcome. Equation (11) uses only Bob's own
records and the previously declared herald. Nor is this an assertion of physical
superluminal propagation by an implemented device: no such device or spacetime
realization has been supplied.

### 7.4 Does this route select the source law and safe reuse?

Applying a valid local quantum instrument correspondence would constrain both the
first-read CHSH value and the complete local-history marginals. It would therefore
exclude this candidate rather than repair its existing probabilities.

For the supplied one-parameter law (4), the necessary CHSH ceiling alone yields
\(\eta_*\le\eta\le1-\eta_*\). It does not pick \(\eta_*\), derive a preparation,
or prove that a whole process belongs to the quantum set. The calibrated endpoint
already fails (14). The basic stochastic correspondence also represents the same
global permutation for all \(\eta\), including the PR countercontrol, so representation
alone cannot supply the missing selection principle.

A successor exploring this route must give a noncircular physical source and a common
dictionary preserving the actual local preparations, interventions, records and resource
use, then verify its causal/composite conditions across the admitted protocols.
The source mechanism must determine the resulting probabilities; imposing the target
coefficient or admitting only laws that already match QM would leave that question
unanswered. The Barandes route remains open, with these candidate-specific compatibility
tests now explicit. No successor, new physical posit or strengthened equivalence claim
is adopted by this comparison.

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

- **B1.** J. A. Barandes, [The Stochastic-Quantum Theorem, arXiv:2309.03085v2](https://arxiv.org/html/2309.03085v2),
  §§3.1 and 4.1–4.3; finite tuple, higher-history scope and permutation example.
- **B2.** J. A. Barandes, M. Hasan and D. Kagan,
  [The CHSH Game, Tsirelson's Bound, and Causal Locality, arXiv:2512.18105v1](https://arxiv.org/html/2512.18105v1),
  §§3.3 and 4.1–4.2; causal independence and the factorized operations used in the proof.
  Both versioned sources were consulted on 2026-11-07. Their statements are distinguished
  from the candidate-specific derivations in §7; this is not an independent review of
  either external paper.
