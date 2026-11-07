# One existing record at a native receiving gate

**Paper-only source assessment; awaiting independent review.** Accountable
issue: #866; parent objective: #1169; guiding draft: #1173.
[Owner scope](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6700487063)
authorizes one record-to-control candidate under its retained preparation and
access rules. Source snapshot:
`f49b768709d262a05471895cec703b31aff19b57`; starting research head:
`813b7263523c3975f9c6585f67e8c9d794fb99fa`.

**Decision:** the existing record-bearing field enters the neighboring
interaction without an added write. This candidate stops at conversion of
that masked interaction into a usable controlled operation and output.
The receiving q10 field is private; the stipulated next whole-V read does
not supply the private decoder or an acceptance flag. No reusable
measurement boundary is constructed. This is a source-specific stop, not
an impossibility result for native feedback or OI.

The contribution is the explicit record/input/output account in §§1–4 and
its gate decision. The native source-to-pool/ciphertext permutation and
seven-site inverse are existing results, reused with their assumptions,
not new research claims or computations. In particular, the existing
port-5 transport and record/key studies are not repeated.

## 1. One candidate, with one source contract

Use **Native A** in the shared v12 contract and native_x_v12 report. It
already includes the stipulated whole-q9 record at L and the candidate
single whole-q9/V read at L+2. These are the retained protocol conventions;
their physical observer, clock and access realization is not derived here.

The rule on three-bit triples is

    U_(t+1)(v) = U_(t-1)(v) XOR H(XOR_(w~v) U_t(w)),
    H(A,B,D) = (B,D,A XOR B*D).

All arithmetic within triples is over F2. H is bijective:
H^-1(a,b,d)=(d XOR a*b,a,b). Keep the source constants
T=185, P=12*840^185, S=P+185, R=S+68, L=R+9 and the inherited
torus side 256L+64T+1. Keep every existing ready region, source exception,
public bank, old flag and terminal rule.

Choose q9=(0,S,77), q10=(0,S,78), q8=(0,S,76).
On an old successful prepared branch, the current physical field at L is

    p = U_L(q9) = (0,s,r_old).

The whole p, including r_old, is in the stipulated old record. The source
for the next interaction is this physical field itself, not an assumed
copy from an observer's memory. The neighbor stencil already connects q9
to q10. No read-triggered write or history-dependent source preparation
is introduced.

The candidate schedule is fixed in advance:

| Event | Physical state or admitted record | Limitation |
| --- | --- | --- |
| L | Old whole-q9 record p; the same p remains a physical current field | Retain all old flags and raw record fields |
| L+1 | q10 receives q9 in its six-neighbor sum; previous q9 still stores p | q10 is private, not a new public output |
| L+2 | Old p enters the q9 update; one whole V read is stipulated on continuing branches | No private-neighbor read, acceptance flag or reuse is added |

The q10-ready/E–N route-v13/v14 variant has a different preparation. Its
selected q10.A=s law cannot be combined with Native A's fair pool.
The earlier scalar finite-q receiver and B3's real-valued exchange are
also different models; none supplies operands, readiness or controls here.

## 2. Actual delivery into the neighboring input

Let J=U_(L-1)(q10) and let eta be the XOR of the five current neighbors
of q10 at L other than q9. The complete current output is

    Q10 = J XOR H(eta XOR p).

For p=(0,s,r_old), this means

    Q10.A = J.A XOR eta.B XOR s,
    Q10.B = J.B XOR eta.D XOR r_old,
    Q10.D = J.D XOR eta.A
              XOR (eta.B XOR s)*(eta.D XOR r_old).

This is an actual native update on every prepared successful trajectory.
The record-bearing s is present in the physical gate input. The term
s*(eta.D XOR r_old) is part of that same update; the other terms and all
three output fields remain physical. Nothing has cleared them.

For a *formal local-coordinate comparison* at fixed J, eta and r_old,
let Q0 be the expression with s set to zero. Then

    Q_s XOR Q0 = (s,0,s*(eta.D XOR r_old)).

This identity does not exhibit two independently available settings on one
fixed incoming carrier. Under the original source law, changing s can
also change J, eta, r_old and other fields. One must not hold them fixed
by fiat, treat the identity as an allowed private XOR write, or read Q10
because it appears in an equation. The output's previous slice and all
other evolving sites also remain part of the state.

Thus physical neighbor delivery is present, while a separately usable
record-conditioned operation on a specified operational carrier has not
been supplied. This preserves the positive native coupling result without
claiming a clean gate or an actual-world comparison from a symbolic one.

## 3. The next read, with the original random sources retained

Native A supplies three independent original-time current triples:

    F8 at (-(L+1),S,76),
    F10 at (-(L+1),S,78),
    F9 at (-(L+2),S,77).

Let C be every other original variable, with all its inherited correlations.
The source assumption is explicitly

    Pr(F8=a,F10=b,F9=c | C) = 1/512.

F9 was an added candidate resource in native_x_v12; it is already part of
the Native A contract selected here. This unit adds none. Fairness and
independence are supplied initial conditions, not a derived OI measure or
fresh randomness generated at the late gate. A fixed-zero or correlated
complement would require a different conditional analysis.

For each fixed C, the original unique axial first-arrival proof gives:
Q8 is a permutation of F8, Q10 a permutation of F10, and
M=U_(L+1)(-1,S,77) a permutation of F9 conditional on F8,F10.
Each axial step is an XOR translation, H, and another XOR translation.
Off-path and old-local terms are too early to depend on that source.
The cross-target distances minus L are respectively (1,3,1), (3,1,1),
(3,3,1), with target order q8,q10,M. Sequential inversion therefore
makes (F8,F10,F9) -> (Q8,Q10,M) a bijection.

Let B be the XOR of the other three current q9 neighbors at L+1.
The source cones exclude p and B, so both are functions of C. At L+2,

    V = p XOR H(Q8 XOR Q10 XOR M XOR B).

This equation holds for every old raw p, including nonzero-A triples on
old failure branches; only §2's displayed component expansion specializes
to prepared successes. For fixed C,Q8,Q10, the map M -> V is another
permutation. Hence

    Pr(Q8=a,Q10=b,V=v | C) = 1/512.                 (1)

This rederives the retained paper argument; it does not rerun its finite
controls. M can depend on F8 and F10 before the triangular change of
variables. No independence of arbitrary neighboring fields is assumed.

The actual two-slice phase still encodes p:

    p = V XOR H(XOR_(six q9 neighbors) U_(L+1)(neighbor)),
    s = V.B XOR XOR_(six q9 neighbors) U_(L+1)(neighbor).D.

This seven-site identity is not a permitted private read or an implemented
native decoder. Continuous q9 access is not implied by the single V
convention. Neither the observer's old knowledge of s nor its mathematical
recoverability physically places a clean operand at another gate.

## 4. Complete records, remaining state and terminal branches

Let W collect the permitted history through L+2 other than the proposed V
read, using no-read symbols after termination. It includes old p where
admitted, every earlier raw field, timing and old success/failure flags.
The source/public-cone exclusions in native_x_v12 give W=w(C):
minimum old-port arrivals are L+77, L+79, L+79 for F8,F10,F9.
No additional earlier read or private-source access is included.

Let D(W) indicate that the original protocol permits attempting this
single V read. It is decided before V, without a new postselection rule.
Write V_obs=V when D=1 and bottom when D=0.
For each positive-mass w, let mu_w be the conditional law of C given W=w.
Old branch masses Pr(W=w) are inherited; this paper neither counts them
from contexts nor replaces them by a chosen quantum failure law.

On an enabled branch, (1) gives

    Pr(Q8=a,Q10=b,V_obs=v | W=w) = 1/512,
    Pr(V_obs=v | W=w) = 1/8,
    Law(C | W=w,V_obs=v) = mu_w.

This is a statement about the complete raw triple, not just one bit.
It does not imply independence from the remaining physical world. To
retain that world, let G2(C,F8,F10,F9) be the complete global two-slice
state at L+2, and let Psi_C(a,b,v) be the unique source triple tuple
obtained by inverting the triangular map above. Conditional on an enabled
(w,v), the full outgoing-state law is exactly the mixture

    sum_(a,b) (1/64) * integral
        delta_[G2(c,Psi_c(a,b,v))] d mu_w(c).        (2)

Equation (2) is a conditional pushforward, not an evaluated operational
instrument. It keeps all carrier fields, sources, bank remnants and
apparatus correlations. It chooses no quotient to hide a failed test.
The reversible native update retains the initial information in the
global state; that fact does not make its inverse publicly accessible.

On a terminal branch D(w)=0, the only new protocol symbol is bottom.
The mathematical field continuation, if used diagnostically, has law

    sum_(a,b,c) (1/512) * integral
        delta_[G2(x,a,b,c)] d mu_w(x),

but no read is attempted and no carrier is offered. Native evolution is
not a restart authorization. These formulas apply only to positive-mass
histories; no zero-mass branch is normalized.

Later records could disclose masks or correlate with the outgoing carrier.
Nothing above certifies a longer read prefix or reusable measurement.
The existing port-5 fibre analysis explicitly preserves this distinction;
its later horizon is not added to this candidate.

## 5. Resource account and stopping gate

The complete inherited preparation remains an assumption: ready regions,
named source values, public bank law, original correlations and read/clock
conventions. The nine conditional fair source bits are used in the
specified two-tick analysis. They are not erased or refreshed; their
information remains in the outgoing state. No cost-free repeated
independence, late blank processor, reset or unbounded reservoir follows.
This is not a minimal resource count for an apparatus.

The first unresolved operational gate is **physical conversion of the
encoded dependence into a usable control/output interface**. For the
selected q10 receiver, direct read access is absent. The permitted single
V convention gives an output symbol but does not supply the private
seven-site decoding operation, a native acceptance predicate or a successor
accepting the complete outgoing carrier. The input delivery alone does not
discharge these requirements.

Uniform V is not itself an instrument impossibility proof: (2) may contain
useful outcome/carrier correlations. Nor would recovering s from the whole
public transcript be progress: the old q9 record already contains s. The
needed object is a physically implemented operation on the retained
carrier, with its record and next usable boundary, not a relabelled old bit.

The shared contract's 5:4:1 post-X target and 5/16 reference acceptance use
an abstract predicate of decoded s and pool bits. This paper does not turn
that predicate into a physical flag or equate it with D. The same concern
blocks applying B3's fixed qubit-instrument comparison to this candidate;
matching a permitted marginal would not establish its state change.

Stop this bounded candidate here. No extra write, private decoder read,
source pin, new carrier quotient, longer port schedule or replacement
candidate is adopted. #866 retains the control/access obligation; physical
ready-source justification belongs with #1147 and retained readable storage
with #1032. This unit supplies no new design or authorization for either.
#1169's two whole-model directions, composites and native sourcing stay open.

## 6. Evidence scope and review anchors

All native-package paths below are relative to
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`
at the source snapshot above.

| Source | Role here |
| --- | --- |
| shared_v12/INTERFACE-CONTRACT.md | Native A, source/read conventions, full records and target; no physical premise adoption |
| native_v11/REPORT.md | Q8/Q10 unique-path argument and complement dependence |
| native_x_v12/REPORT.md §§1–5 | Three-source geometry, conditional law, phase inverse and terminal guard |
| native_x_v12/review/REPORT.md | Separate retained review of that geometry and proof, including source-prior and access limits |
| native_vread_v15/REPORT.md | Distinct q10-ready route/read study; its law is not substituted for Native A |

The corpus search also checked the maintained continuous-substates
actuation, causal-interface, setting-source, randomized-setting, port-5
cone and record/carrier-fibre records, alongside the previous #866 source
assessment. They explain why a private coordinate, a passive record label
or an existing transport lemma is not an available controller. Their
pending computational verdicts are not premises of §§2–4. The decisive
algebra is written here; the source geometry and supplied prior are stated
explicitly and traced to native_x_v12 and its retained separate review.
No conclusion is inferred merely from a file being on main or an Issue's
planning status.

Independent review must check the actual native input, unchanged source
variant, conditional permutation argument, absence of arbitrary-neighbor
independence, full-state mixture, terminal guard and the narrow stop.
No new scientific script, enumeration, simulation, Lean proof or physical
test is part of this paper unit. Ordinary repository CI checks integration
hygiene; it does not certify the physical sourcing conclusion.
