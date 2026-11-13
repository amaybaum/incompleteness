# PREP-MIN — exact declared-history preparation cost through t=2

**Paper-only WIP; complete author proof, independent exact-checkpoint review pending.**
Writer/coordinator: Codex, 2026-11-10. Accountable issue: [#1169](https://github.com/amaybaum/incompleteness/issues/1169).
The [owner authorization](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6768774955)
fixes the target, two mathematical preparation classes and relative-entropy cost. The
[preliminary calculation](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6767228389)
is a hypothesis to audit, not a premise or independent acceptance. Completed draft #1226 is outside
this unit's write scope. No scientific program, source screen, new premise or merge is authorized.

## 1. Source, carrier and cost definitions

Source snapshot D: `cac5d26441dd33e9348151487e4df7b547195481`.

| Main source | Immutable blob | Content used |
| --- | --- | --- |
| [SM section 3.1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/SM.md) | `7d805ac879cfd9561c0ede14507ad0c5b8e7b238` | The selected reversible ring rule; its binary specialization gives the Boolean rule below. |
| [preparation-loading sections 3–6](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md) | `1802ea3c335eb7457739fa5af13b3aefd0c603af` | Canonical precursor, common eta, eight constraints and source/record limits. |
| [physical-interface sections 4–5](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md) | `3229ef3cd234e613a4b0cb63bab548e0fec666a9` | Original two-site/two-slice observer and reference history. |

All sites are modulo L>=9; all fields are bits. Write XOR as `+` over F_2 and keep
Boolean OR as `∨`. At precursor time -1, `(X,Y)=(u_-1,u_-2)`. The unchanged rule is

    f_i(u) = u_(i-1) + (u_(i+1) ∨ u_(i+2)),
    F(u,v) = (f(u)+v,u),
    F^-1(a,b) = (b,a+f(b)).

The visible precursor root is X_0=X_1=Y_0=0, Y_1=c, for c in {0,1}.
Let Omega be the same labelled free-coordinate space for both c, omitting those four
fixed coordinates. Its dimension is N=2L-4 and its size is 2^N. Let U be uniform on
Omega; U_c is its injection into the full precursor with that visible root.

A candidate nu is one normalized distribution on Omega, used unchanged for both c.
Class A contains all such distributions. Class B contains U(.|E), for one common
nonempty event E subset Omega. No extra seed outside Omega, per-setting source,
postselection of output records or physical herald is granted.

The sole cost is

    D_2(nu||U) = sum_omega nu(omega) log_2(nu(omega)/U(omega))
               = N-H_2(nu),

with 0 log 0=0. This equals D_2(nu_c||U_c) for either setting. The four visible root
coordinates are given by the reference and are not charged again. This cost is not
physical memory, energy, total preparation complexity or the cost of operating a device.
For class B it is exactly -log_2 U(E).

## 2. The fixed target and observer

Put `(A,B)=F(X,Y)` at time 0. Define the original event E_8 on Omega by

    X_-1=X_2=X_3=0,
    Y_-2=X_-3,  Y_-1=X_-2,
    Y_3=X_4 ∨ X_5,
    Y_4=X_5 ∨ X_6,
    Y_5=X_4+(X_6 ∨ X_7).

Let eta=U(.|E_8), common across c. This is the original supplied comparator law,
not a physical producer. Loading gives A_1=c, A_2=z=Y_2+X_4,
A_i=0 for i in {-2,-1,0,3,4,5}, and B_i=0 for i in {-1,0,1,2,3}.

The raw observer at each declared cut is

    O_t=((u_t(0),u_(t-1)(0)),(u_t(1),u_(t-1)(1))).

Its complete declared projection history is (O_-1,...,O_k), k=0,1,2. Under eta
it has the following values, with one fair z shared throughout each history:

| Cut | Raw tuple (u_t(0),u_(t-1)(0),u_t(1),u_(t-1)(1)) |
| --- | --- |
| -1 | (0,0,0,c) |
| 0 | (0,0,c,0) |
| 1 | (c ∨ z,0,z,c) |
| 2 | ((1+c)z,c ∨ z,c,z) |

The primary target T_(c,2) is the law of this full table for c=0 and c=1 separately,
with mass 1/2 on each z history and zero on every other history. T_(c,0) is a single
history because the first two cuts do not depend on z. The same table truncated at
cut 1 defines T_(c,1). Cuts 0 and 1 are internal checks, not substitute targets.
A candidate matches if its history pushforward equals T_(c,k) for each setting.
These are declared mathematical projections, not records of an available physical logger
or a preparation apparatus. No raw coordinate or failed history may be discarded.
The loading update is -1 to 0; the primary window includes three forward updates from
the precursor and two after the loaded cut. Its earlier cuts are retained, not skipped.

## 3. Statement and precise matching constraint

Let Phi_(c,k):Omega -> Hist_k be the deterministic map retaining all four raw coordinates
at every cut -1,...,k. Here Hist_k is the raw product alphabet, including histories that
the dynamics cannot realize. The feasible laws satisfy

    (Phi_(c,k))_*nu = T_(c,k) for each c=0,1.             (3.1)

Equality includes all history probabilities; any history outside the target support has
probability zero. There is no conditioning on a favorable observed output. The two maps
are compared on the same Omega because the source law is common. No experiment that
reads both settings in one run, or extra target law for counterfactual joint outcomes,
is assumed.

**Theorem (fixed mathematical contract).** For every L>=9, the minimum of D_2 in (3.1)
over class A, and separately over class B, is

| Last cut k | Class A | Class B | Role |
| --- | --- | --- | --- |
| 0 | 3 bits | 3 bits | Internal root/history check |
| 1 | 9/2 bits | 5 bits | Internal one-post-load-update check |
| 2 | 15/2 bits | 8 bits | Primary declared-history target |

All minima are attained by explicit common laws/events below. Thus 7.5 and 8 are exact
entropy values, not floating-point estimates. The theorem concerns the supplied reference,
selected rule and finite declared observer, not a physically sourceable preparation class.
The following sections give the complete hand proof.

## 4. Boolean reduction and reference cell sizes

### 4.1 The loaded-root event

At the fixed precursor root, the unchanged rule gives

    A_0 = X_-1+X_2,
    A_1 = c+(X_2 ∨ X_3),  B_0=B_1=0.

The required A_1=c forces X_2=X_3=0, after which A_0=0 forces X_-1=0.
Conversely those three equations give the complete cut-0 tuple. Therefore, for either
setting, exact target support through cut 0 is precisely

    R = {X_-1=X_2=X_3=0},       U(R)=2^-3.              (4.1)

The precursor tuple is already fixed by the reference. No additional unobserved
ready-state condition has been imposed to obtain (4.1).

### 4.2 Six masked free coordinates

Define the following functions on Omega; the displayed A-field identifications hold on R:

    p = Y_-1+X_-2                 = A_-1,
    a = Y_-2+X_-3                 = A_-2,
    z = Y_2+X_4                   = A_2,
    q = Y_3+(X_4 ∨ X_5)           = A_3,
    r = Y_4+(X_5 ∨ X_6)           = A_4,
    s = Y_5+X_4+(X_6 ∨ X_7)       = A_5.               (4.2)

Here q is an auxiliary bit; the alphabet remains F_2. These identities follow by
substitution into f(X)+Y, using X_0=X_1=0 and (4.1). They do not require any Y constraint.
In these coordinates the original comparator event is exactly

    E_8 = R intersect {p=a=q=r=s=0}.                    (4.3)

For fixed all-X data, each of the six functions in (4.2) is one different free Y bit
XOR a fixed mask. Consequently their joint conditional law under U is uniform on
{0,1}^6, independent of the X assignment. The same remains true conditional on R.
In particular each additional specified bit in (4.2) costs a factor 1/2 in reference
mass, regardless of any coincidences among the X masks. This also proves U(E_8)=2^-8
and that z is fair under eta, as used in section 2.

### 4.3 Small-ring boundaries

The relevant Y labels and three extra X pins are distinct from their own fixed root
coordinates for every allowed L. The two boundary cases are explicit:

| L | Y labels (-2,-1,2,3,4,5) modulo L | X pins (-1,2,3) modulo L |
| --- | --- | --- |
| 9 | (7,8,2,3,4,5) | (8,2,3) |
| 10 | (8,9,2,3,4,5) | (9,2,3) |
| >=11 | (L-2,L-1,2,3,4,5) | (L-1,2,3) |

All six Y labels avoid 0,1, and all three X labels avoid 0,1. A Y label may equal an
X label: they are different fields. X_-3=X_6 at L=9, X_-2=X_7 at L=9, and X_-3=X_7
at L=10 are allowed mask aliases, not duplicate Y constraints. Conditional on all X,
the six Y translations are still separate bijections. All other modular coincidences
among X masks are harmless for the same reason. No argument below assumes independent
values for two names of the same X coordinate. N>=14, so all displayed cell sizes are
positive integers, including the smallest boundary ring.

## 5. Necessary and sufficient common history cells

The reference target has only the histories in section 2. For a feasible common nu,
each setting's forbidden-history set must have nu-mass zero. The union of those two
forbidden sets therefore has mass zero. Thus nu is supported on their intersection
of allowed pointwise histories. We now determine that intersection, rather than
assume that a hidden signal label is necessarily the observed target label.

### 5.1 Through cut 1

On R, let w=z ∨ q. Directly from F at the next update,

    u_1(0)=p+(c ∨ z),       u_1(1)=w.                 (5.1)

The other two raw coordinates in O_1 are A_0=0,A_1=c. The target branch label at this
cut is determined by the raw coordinate u_1(1), so it must be w in both settings.
At c=1, (5.1) must equal 1 in its first entry, forcing p=0. At c=0 the same source
point must then obey z=w. Equivalently, q=0 if z=0; q is free if z=1. Conversely
these conditions give exactly the two target raw tuples in both settings.

The disjoint common cells, their reference masses and sizes are therefore

| Cell | Definition | U-mass | Cardinality |
| --- | --- | --- | --- |
| S_0^(1) | R, p=0, z=0, q=0 | 2^-6 | 2^(N-6) |
| S_1^(1) | R, p=0, z=1; q free | 2^-5 | 2^(N-5) |

Every point of S_z^(1) yields precisely the target history with that same z for each c.
These two histories are distinct for either c because the raw controller entry is z.
Accordingly (3.1) through cut 1 is equivalent to

    nu(S_0^(1))=nu(S_1^(1))=1/2,  nu(outside)=0.       (5.2)

The common branch assignment has been derived from (5.1), not added as a constraint.
Reference masses use (4.1)–(4.2); no point outside these cells can be hidden by a
different z label, a receiver-only marginal or relabelling the raw record.

### 5.2 Through cut 2

The prefix already forces (5.2). On those cells, another direct substitution gives

    u_1(-1)=a+c,
    u_1(2)=c+(q ∨ r),
    u_1(3)=z+(r ∨ s),
    u_2(0)=a+c+[z ∨ (c+(q ∨ r))],
    u_2(1)=(c ∨ z)+[(c+(q ∨ r)) ∨ (z+(r ∨ s))]+c.    (5.3)

All old-local terms are included. In O_2 the other two raw coordinates are the
already fixed u_1(0)=c ∨ z and u_1(1)=z. Hence the remaining target equations are
u_2(0)=(1+c)z and u_2(1)=c, for both c.

If z=0, the cut-1 condition sets q=0. The first equation in (5.3) then reads
u_2(0)=a+r; matching its zero target forces a=r. The second simplifies to
u_2(1)=c ∨ r ∨ s. Its c=0 target forces r=s=0, and therefore a=0.

If z=1, the first target equation in (5.3) forces a=0. Put h=q ∨ r and j=r ∨ s.
The second target equation requires

    (c+h) ∨ (1+j)=1   for c=0 and c=1.                (5.4)

Taking c=h, one of the two declared settings, forces 1+j=1, hence j=0 and r=s=0.
No restriction on q follows. Conversely a=r=s=0, with the earlier q condition,
makes (5.3) equal the target for both c: at z=1 the OR in (5.4) is always 1.

Thus the complete common cells through cut 2 are exactly

| Cell | Definition | U-mass | Cardinality |
| --- | --- | --- | --- |
| S_0^(2) | R, p=a=r=s=q=z=0 | 2^-9 | 2^(N-9) |
| S_1^(2) | R, p=a=r=s=0, z=1; q free | 2^-8 | 2^(N-8) |

Every one of the four raw coordinates at all four cuts is now accounted for. Prefix
matching rules out every other possible allowed history; the cut-2 calculation is
both necessary and sufficient. The exact constraint is

    nu(S_0^(2))=nu(S_1^(2))=1/2,  nu(outside)=0.       (5.5)

These cells are subsets of the corresponding cut-1 cells and are independent of c.
The statement covers both boundary rings by section 4.3. Requiring only one setting
would not justify the simultaneous-setting steps in (5.1) and (5.4).

## 6. Variational lower bounds and explicit class-A minimizers

For any normalized finite reference law Q with full support and normalized P,
D_2(P||Q)>=0. One proof is
Jensen's inequality for the strictly convex function t log_2 t, with its continuous
value 0 at t=0: sum Q (P/Q) log_2(P/Q)>=1 log_2 1=0. Equality requires P=Q.
No numerical optimization or asymptotic limit is involved.

For disjoint cells S_z with u_z=U(S_z)>0 and required masses m_z=1/2, write
nu_z=nu(.|S_z) and U_z=U(.|S_z). Splitting the finite KL sum cell by cell gives

    D_2(nu||U)
      = sum_z m_z log_2(m_z/u_z)
        + sum_z m_z D_2(nu_z||U_z).                    (6.1)

There is zero nu-mass outside, whose KL contribution is 0. Nonnegativity gives a
lower bound, attained exactly when the law inside each cell is its reference
conditional. Consequently the unique class-A minimizer for k=1,2 is the explicit
normalized common law

    nu_A,k = (1/2)U(.|S_0^(k))+(1/2)U(.|S_1^(k)).     (6.2)

Both cells are independent of c, so this is one law on Omega. Normalization follows
from disjointness and weights 1/2; the target follows from (5.2)/(5.5). In particular,

| k | Density nu_A,k/U on S_0^(k) | Density on S_1^(k) | Exact minimum |
| --- | --- | --- | --- |
| 1 | 2^5 | 2^4 | (5+4)/2=9/2 bits |
| 2 | 2^8 | 2^7 | (8+7)/2=15/2 bits |

The density is zero elsewhere. This specifies the probability of every state of Omega,
including unobserved free coordinates, and supplies an explicit attainability witness.
For k=0, the same single-cell identity gives

    D_2(nu||U)=3+D_2(nu||U(.|R))>=3,

with unique minimizer U(.|R). Here no fairness condition on z is required by the
target; it is simply present in that entropy-maximizing conditional.

An equivalent coordinate description makes (6.2) concrete. Choose X uniformly subject
to its fixed root and R. Choose z fair; choose q=0 when z=0 and choose q fair when z=1.
For k=2 set p=a=r=s=0; for k=1 set p=0 and take a,r,s independently fair. Set

    Y_-1=p+X_-2,  Y_-2=a+X_-3,  Y_2=z+X_4,
    Y_3=q+(X_4 ∨ X_5),  Y_4=r+(X_5 ∨ X_6),
    Y_5=s+X_4+(X_6 ∨ X_7),                             (6.3)

and take all unmentioned free Y coordinates independently fair. Each fair coordinate
here is independent of the other listed free choices except the stated q dependence
on z. Conditional on each cell, (4.2)'s invertible masks show this is exactly uniform,
so (6.3) describes (6.2), including for L=9/10. It is a description of a law on Omega,
not a physical sampler, additional external seed, field-writing operation or producer.

## 7. Support lower bounds and explicit class-B minimizers

Let nu=U(.|E) with E nonempty and common across settings. Exact matching implies
E is a subset of the allowed common support: U assigns positive mass to every point,
so a point outside would have positive forbidden-history mass. For k=1,2, fairness
of the target and uniformity imply

    |E intersect S_0^(k)|=|E intersect S_1^(k)|=|E|/2.

Since S_0^(k) is the smaller cell, this yields

    |E| <= 2|S_0^(k)|,
    U(E) <= 2u_0,
    D_2(U(.|E)||U)=-log_2 U(E) >= -log_2(2u_0).        (7.1)

No fractional inclusion of a state is available in this class. The bound is attained
by the following actual common hidden-coordinate events:

| k | Event | U-mass | Cost |
| --- | --- | --- | --- |
| 0 | R | 2^-3 | 3 bits |
| 1 | E_5=R intersect {p=q=0} | 2^-5 | 5 bits |
| 2 | E_8=R intersect {p=a=q=r=s=0} | 2^-8 | 8 bits |

For E_5, z is fair by (4.2); its z=0 half is all S_0^(1), and its z=1 half is
the q=0 half of S_1^(1), of equal cardinality. For E_8 the same statement holds
with S_0^(2) and the q=0 half of S_1^(2). Equation (4.3) identifies E_8 with the
original source event, not a new fitted replacement for its microscopic law.
Thus both witnesses give every target history its required probability for both c.
Their support sizes are integers for every L>=9. Through cut 0, E subset R gives
the bound 3, attained by R. This completes the class-B proof and the theorem.

The class-B minimizer is not unique: for k=1,2 one may take all S_0^(k) together
with any subset of S_1^(k) of the same cardinality. E_5/E_8 give explicit choices.
This is uniform source conditioning in the mathematical contract, not an available
herald or a demonstrated physical success rate.

## 8. Why half a bit is saved, and the stronger target

For the primary target, both classes fix the three X fields and p,a,r,s: seven
independent reference bits in the masked coordinates. The observable constraint on
q is only q=0 when z=0. Class A keeps z fair and retains a fair q when z=1;
the joint entropy of (z,q) is 1+(1/2) instead of the reference 2. Its additional
deficit is therefore 1/2 bit. Class B must balance the two target-cell cardinalities;
E_8 fixes q in both branches and pays one additional bit. This interpretation is
consistent with, and not a replacement for, the variational and support proofs.
An entropy value of half a bit is not half of a physical binary register.

Matching the entire post-load world-state law F_*eta_c is a different constraint.
The displayed inverse of F gives nu_c=eta_c, hence nu=eta and cost 8 in both classes.
That observation supplies neither (5.5) nor the operational lower bound: the
declared-history optimum in class A is a different, nonuniform law. No claim of
equality of its full microscopic output, or of any later observer history, is made.

## 9. Assumptions, fitting and physical limits

| Ingredient | Status and exact role |
| --- | --- |
| Selected binary F and L>=9 | Fixed mathematical specialization and ring family from the main sources, not a claim that all OI realizations use this rule. |
| Fixed root and uniform U_c | Stipulated comparator; its visible blanks and request are given, not produced or charged by this conditional hidden-order metric. |
| One common source on Omega | Required by the owner contract; only Y_1=c changes. No per-setting fitted preparation or extra initial variable is allowed. |
| Original eta and fair z | Benchmark law from the main sources. Fairness is supplied target data, not a derived Born rule or physical randomness source. |
| Raw histories through t=2 | Every declared two-site/two-slice coordinate and all bad-history mass are included. The projection is not a constructed clock, logger, durable memory or preparer record. |
| Classes A/B | Mathematical admissibility only. Class A's optimal weights and conditional q law are fitted to this target; class B's support restrictions are selected to meet it. Neither is independently motivated OI selection. |
| Cost | Exact relative entropy in bits on the fixed finite source. It is not a fixed-pin count for arbitrary correlated/nonuniform laws, thermodynamic work, physical apparatus memory or #1220 total resource complexity. |
| Physical source and execution | No producer, selectable write, herald, reset, trial/failure process, persistent record or reusable/composite device is constructed. Sourceability and executable availability remain open; INT-AVAIL is not discharged. |

No output history was discarded to reach the theorem. Class B is an admitted
conditional input law, not postselection on a measured output. If a future device
implements it by rejection, its failed attempts, flags, clock and residual state
must be included in that larger physical problem; U(E) here is not its success rate.

The uniformity of the exact cost in L concerns this fixed local finite-history
benchmark. It establishes no arbitrary quantum experiment, intervention repertoire,
Bell/composition result, native Level B correspondence or efficient classical simulator.
Physical-source gate: **NOT PASSED**. The result is a mathematical minimum in the
two stipulated classes and is conditional on this entire target/source contract.

## 10. Verification, provenance and review gate

The displayed Boolean identities, boundary-label argument, finite KL decomposition,
support bounds and witnesses were derived by hand from the pinned main rule and
observer. The preliminary 3/4.5/7.5 and 3/5/8 numbers are thereby independently
rederived by the writer, not inherited as accepted facts. A separate non-author
exact-checkpoint full paper/algebra review is still required.

Only static document/source/digest/diff checks accompany this author pass. No numerical
or scientific program, enumeration, optimizer, simulation, Lean build or workflow
dispatch/rerun was executed. Ordinary automatic draft-PR CI is repository validation,
not a scientific experiment or a kernel proof of this theorem.

The three main sources in section 1 supply the actual rule/target definitions and
source limitations at D. The proof content needed for the new minimum is supplied
here; it does not depend on unpublished #1049/QPHEN drafts or a report of acceptance.
The owner authorization and preliminary issue brief are governance/revision provenance;
the latter's mathematical assertions were checked anew in sections 4–7, not used as
an unverified premise. This branch and its future model-review record are off main;
an enduring established claim still requires the applicable A.42/A.46 evidence and
review retention plus separate integration approval. No exception is granted here.

The reviewer must check all raw cuts, common-setting support equivalence, both small
rings, every cell mass, normalization and attainment, the two lower-bound arguments
and the physical/target-fitting limits. Any material defect requires correction and
new exact-checkpoint review. Author completion is not independent acceptance.
