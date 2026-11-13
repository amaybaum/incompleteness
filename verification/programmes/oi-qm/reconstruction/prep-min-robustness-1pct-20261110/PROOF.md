# PREP-MIN-ROB-1 — 1% complete-history preparation robustness

**Paper-only author WIP; complete hand proof; independent exact-checkpoint review pending.**
Writer/coordinator: Codex, 2026-11-10. Accountable [#1216](https://github.com/amaybaum/incompleteness/issues/1216),
coordination [#1169](https://github.com/amaybaum/incompleteness/issues/1169).
[Owner decision](https://github.com/amaybaum/incompleteness/issues/1216#issuecomment-6772851768):
“Authorize the bounded 1% paper proof.” This adopts the fixed initial contract of the
[earlier scoping proposal](https://github.com/amaybaum/incompleteness/issues/1216#issuecomment-6769621038).
Only hand mathematics, source reading, ordinary PR validation and separate non-author paper review
are authorized. No scientific program, physical-source work, new premise or merge is authorized.

## 1. Fixed source and target

Source snapshot D: `cac5d26441dd33e9348151487e4df7b547195481`.

| Main source | Git blob | Content used |
| --- | --- | --- |
| [SM section 3.1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/SM.md) | `7d805ac879cfd9561c0ede14507ad0c5b8e7b238` | Selected binary ring rule. |
| [preparation-loading sections 3–6](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md) | `1802ea3c335eb7457739fa5af13b3aefd0c603af` | Original precursor, uniform reference, supplied eta and apparatus limits. |
| [physical-interface sections 4–5](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md) | `3229ef3cd234e613a4b0cb63bab548e0fec666a9` | Original raw observer and target histories. |

All indices are modulo L>=9. Addition of bits means XOR over F_2; OR is written `∨`.
At precursor time -1, `(X,Y)=(u_-1,u_-2)`. Keep

    f_i(u)=u_(i-1)+(u_(i+1) ∨ u_(i+2)),
    F(u,v)=(f(u)+v,u),   F^-1(a,b)=(b,a+f(b)).

The fixed visible root is X_0=X_1=Y_0=0, Y_1=c, c=0 or 1. Omega is the same
free-coordinate space for both settings, omitting these four fixed coordinates.
N=2L-4, |Omega|=2^N and U is uniform on Omega. U_c injects this law at the corresponding
root. A common nu on Omega changes only the visible Y_1 when the setting changes.

The raw observer is

    O_t=(u_t(0),u_(t-1)(0),u_t(1),u_(t-1)(1)).

Let Phi_c map Omega to the entire raw joint history (O_-1,O_0,O_1,O_2). The target
T_c gives probability 1/2 to each of the following two histories H_c(z), z=0,1,
and probability zero to every other raw history:

| Cut | Raw tuple in H_c(z) |
| --- | --- |
| -1 | (0,0,0,c) |
| 0 | (0,0,c,0) |
| 1 | (c ∨ z,0,z,c) |
| 2 | ((1+c)z,c ∨ z,c,z) |

This is the original eta benchmark, where the source event has
X_-1=X_2=X_3=0,
Y_-2=X_-3, Y_-1=X_-2,
Y_3=X_4 ∨ X_5, Y_4=X_5 ∨ X_6,
Y_5=X_4+(X_6 ∨ X_7).
The loading update is -1 to 0. All four coordinates at every declared cut are retained;
this is a passive mathematical projection, not a sourced preparation/logger apparatus.

Class A allows every normalized common nu on Omega. Class B allows U(.|E) for one
nonempty common event E subset Omega. The only error and cost are

    Delta_L(nu)=max_(c=0,1) TV((Phi_c)_*nu,T_c),
    TV(P,Q)=(1/2) sum_h abs(P(h)-Q(h)),
    Delta_L(nu)<=beta=1/100,
    D_2(nu||U)=sum_omega nu log_2(nu/U)=N-H_2(nu).

Set alpha=1/2-beta=49/100. Zero-mass KL terms are zero. The four precursor root
coordinates are given, not charged again. Cost is relative entropy in bits, not physical
memory, energy, source availability or total classical computational resources. Initial
conditioning in class B is a mathematical law, not a physical herald or output filter.

[The exact endpoint](https://github.com/amaybaum/incompleteness/pull/1227#pullrequestreview-5843234635)
at `076b8e6f951ab20de2ead780099b8a448485cb2e` is accepted off main (15/2 and 8 bits),
not a premise for inheriting positive-error support. The derivation below starts anew.

## 2. Positive-error source classification

For each setting define G_(c,j)={omega:Phi_c(omega)=H_c(j)}. These are source events,
not new accessible operations. A point in any G_(c,j) must give the target loaded root.
Writing (A,B)=F(X,Y),

    A_0=X_-1+X_2,  A_1=c+(X_2 ∨ X_3), B_0=B_1=0.

Hence it must belong to R={X_-1=X_2=X_3=0}, independent of c. **No constraint forces
an approximate candidate nu itself to be supported on R**; outside-R mass is bad in
both settings and is retained in the analysis.

On R introduce masked bits, here q is an auxiliary bit rather than the alphabet size:

    p=Y_-1+X_-2=A_-1,   a=Y_-2+X_-3=A_-2,
    z=Y_2+X_4=A_2,      q=Y_3+(X_4 ∨ X_5)=A_3,
    r=Y_4+(X_5 ∨ X_6)=A_4,
    s=Y_5+X_4+(X_6 ∨ X_7)=A_5.

Conditional on all X, the six named Y coordinates are distinct free bits translated
by fixed masks. Thus (p,a,z,q,r,s) is uniform on 64 possibilities conditional on R,
independent of all X values. U(R)=1/8. Each masked assignment on R has mass 1/512
and cardinality M=2^(N-9)=2^(2L-13).

At L=9 these Y labels (-2,-1,2,3,4,5) are (7,8,2,3,4,5), and the three extra X pins
are (8,2,3). At L=10 the labels are (8,9,2,3,4,5) and (9,2,3). None touches its own
field's root labels 0,1. For L>=11 the same labels remain distinct. Coincident X
masks, such as X_-3=X_6 at L=9, do not duplicate a Y translation. M is a positive
integer for every allowed L, including M=32 at L=9 and M=128 at L=10.

Put d=z ∨ q, h=q ∨ r, j=r ∨ s. Direct updating on R gives

    u_1(0)=p+(c ∨ z), u_1(1)=d,
    u_1(-1)=a+c, u_1(2)=c+h, u_1(3)=z+j.

A target branch must have label d, determined by raw u_1(1) independently of c.
Its cut-1 match requires p=d+z at c=0 and p=0 at c=1. In either setting the
cut-2 receiver equation requires a=h(1-d). The other current-field equation is

    c=0: h ∨ (z+j)=d,
    c=1: (1+h) ∨ (z+j)=1.

These conditions, and the fixed earlier/previous-slice coordinates, are necessary
and sufficient for G_(c,d). Their hand case split is:

| z,q | d | c=0: p,a and allowed (r,s) | c=1: p,a and allowed (r,s) | Common good count |
| --- | --- | --- | --- | --- |
| 0,0 | 0 | p=0,a=r; (0,0) | p=0,a=r; all four | 1 |
| 0,1 | 1 | p=1,a=0; all four | p=0,a=0; all except (0,0) | 0 |
| 1,0 | 1 | p=0,a=0; (0,0),(1,0),(1,1) | p=0,a=0; (0,0),(0,1) | 1 |
| 1,1 | 1 | p=0,a=0; all four | p=0,a=0; (0,0) | 1 |

In particular G_(0,0) is exactly the all-zero masked assignment on R and is a subset
of G_(1,0). Cross-branch good/good events are empty because d is common on R.
This gives six disjoint source atoms partitioning ALL Omega:

| Atom | Target histories matched | Reference mass | Cardinality |
| --- | --- | --- | --- |
| C_0 | Both settings, branch 0 | 1/512 | M |
| C_1 | Both settings, branch 1 | 2/512 | 2M |
| U_0 | Only c=1, branch 0 | 3/512 | 3M |
| V_1 | Only c=0, branch 1 | 9/512 | 9M |
| W_1 | Only c=1, branch 1 | 4/512 | 4M |
| Z | Neither setting matches either target history | 493/512 | 493M |

C_0=G_(0,0); C_1=G_(0,1) intersect G_(1,1). The three one-setting atoms are the
remaining parts of their named G events, and Z is the complement of the other five.
The table follows from counts 1 and 11 for c=0's two branches, 4 and 6 for c=1,
and common counts 1 and 2. The bad-both atom includes all outside-R states and
45 masked assignments on R. No bad histories have been discarded or conditioned away.

## 3. Exact error constraints, without changing the raw-history metric

Write the source masses on (C_0,C_1,U_0,V_1,W_1,Z) as (x,y,u,v,w,t), with
nonnegative entries summing to one. The entire raw-history laws have these target
and outside-target masses:

| Setting | Mass of H_c(0) | Mass of H_c(1) | All other raw histories |
| --- | --- | --- | --- |
| c=0 | x | y+v | u+w+t |
| c=1 | x+u | y+w | v+t |

This table does not discard other histories. Since T_c gives each of them zero
probability, their total contribution to the exact TV sum is their full combined
mass, regardless of how it is distributed among distinct bad raw histories.

For any distribution with masses p_0,p_1 on two target histories and p_bad elsewhere,

    TV(P,(delta_0+delta_1)/2)
      = (abs(p_0-1/2)+abs(p_1-1/2)+p_bad)/2
      = max{p_bad,1/2-p_0,1/2-p_1}.                    (3.1)

If both p_j<=1/2 the value is p_bad; if one exceeds 1/2 it is the deficit of the
other. These cases prove the identity. Therefore the approved 1% constraint is
exactly the following six inequalities, together with normalization/nonnegativity:

    x>=alpha,          y+v>=alpha,     u+w+t<=beta,
    x+u>=alpha,        y+w>=alpha,     v+t<=beta,        (3.2)

where alpha=49/100 and beta=1/100. The x+u inequality follows from x>=alpha,
but is displayed to retain both settings explicitly. No exact-support restriction,
exact loaded root, output conditioning, per-cut tolerance, or setting average was
introduced in (3.1)–(3.2).

## 4. The exact class-A minimum and an explicit common law

Let tau be the unique number in (0,beta) satisfying

    (alpha+tau)tau = (986/63)(beta-tau)^2.               (4.1)

It exists uniquely: the ratio (alpha+tau)tau/(beta-tau)^2 is continuous, strictly
increasing from zero to infinity on this interval. Equivalently, tau is the smaller
root in that interval of

    4615000 tau^2 - 252950 tau + 493 = 0.               (4.2)

This is an exact algebraic definition, not a numerical root search. Put v_star=beta-tau
and assign the following atom masses:

| Atom | Optimal mass pi | Density pi/U(atom) |
| --- | --- | --- |
| C_0 | alpha | 512 alpha |
| C_1 | alpha+tau | 256(alpha+tau) |
| U_0 | 3v_star/7 | 512v_star/7 |
| V_1 | v_star | 512v_star/9 |
| W_1 | 4v_star/7 | 512v_star/7 |
| Z | tau | 512tau/493 |

Every entry is positive. The sum is
2alpha+2tau+2(beta-tau)=2alpha+2beta=1. Define the complete law on Omega by

    nu_A_star = sum_I pi_I U(.|I),                    (4.3)

where I runs over the six explicitly defined source atoms. This gives the probability
of every source state, including every exterior coordinate and all bad-history states.
Atom membership is a function of common hidden coordinates; the same law is used
for both c. Nothing in (4.3) samples a new physical seed or implements a preparer.

Its error is exactly beta in both settings. In c=0, the two target masses are
alpha and (alpha+tau)+v_star=1/2, with bad mass beta. In c=1 they are

    alpha+3v_star/7,       1/2-3v_star/7,

each at most 1/2, and their sum is 1-beta. Equation (3.1) consequently gives beta.
Thus the law is feasible for the actual full-history problem, not just a relaxation.

The exact minimum, independent of L on this fixed family, is

    C_A = alpha log_2(512alpha)
        + (alpha+tau) log_2(256(alpha+tau))
        + v_star log_2(512v_star/7)
        + v_star log_2(512v_star/9)
        + tau log_2(512tau/493).                       (4.4)

### 4.1 A finite variational certificate over all admissible laws

For finite probability laws P,Q with Q positive on its finite domain,
D_2(P||Q)>=0 by Jensen applied to t log_2 t (0 log 0=0), with equality only at P=Q.
Partitioning Omega into the six atoms gives, for any nu with atom masses p_I,

    D_2(nu||U)=D_2(p||q)+sum_I p_I D_2(nu(.|I)||U(.|I)),  (4.5)

where q=(1,2,3,9,4,493)/512. Terms with p_I=0 are omitted. This identity is a finite
sum expansion and supplies the within-atom lower bound without assuming a source
factorization for nu.

Temporarily retain only the three necessary constraints

    x>=alpha,      u+w+t<=beta,       v+t<=beta.        (4.6)

The other good-history constraints in (3.2) are dropped for a lower bound. Define

    gamma=log_2(256(alpha+tau)),
    eta=log_2(2alpha/(alpha+tau)),
    lambda=log_2(7(alpha+tau)/(2v_star)),
    mu=log_2(9(alpha+tau)/(2v_star)).

Eta, lambda and mu are strictly positive: alpha+tau<1/2<2alpha and v_star<beta,
while 7alpha>2beta and 9alpha>2beta. The logs of the six optimal densities in the
table are, in order,

    gamma+eta, gamma, gamma-lambda, gamma-mu,
    gamma-lambda, gamma-lambda-mu.                    (4.7)

For the final equality, (4.1) says precisely that the Z density is the product
of the U_0 and V_1 densities divided by the C_1 density. For any normalized p,
expanding its KL sum relative to the positive vector pi now yields

    D_2(p||q)-D_2(pi||q)
      = D_2(p||pi) + eta(x-alpha)
        + lambda(beta-u-w-t) + mu(beta-v-t).           (4.8)

Gamma cancels by normalization; pi saturates the three constraints. Every term on
the right is nonnegative for (4.6). Combined with (4.5), this proves (4.4) is a
lower bound on every feasible law in the original class A. Equation (4.3) is feasible
for all of (3.2) and attains it. Equality requires p=pi and uniform reference
conditionals inside each atom; hence (4.3) is the unique class-A minimizer.
No optimizer, finite-state enumeration or assumption about exact-support confinement
is used in this certificate.

## 5. The exact class-B minimum, including finite-cardinality rounding

Let nu=U(.|E), with K=|E|>0. TV<=beta in setting c=0 forces

    nu(G_(0,0))>=1/2-beta=alpha.

Section 2 proves G_(0,0)=C_0, with cardinality M, even when E contains arbitrary
states outside the old exact support. Consequently

    alpha <= |E intersect C_0|/K <= M/K,
    K <= K_star=floor(M/alpha)=floor(100M/49).         (5.1)

Its entropy cost is N-log_2 K. Thus every feasible class-B event has cost at least

    C_B(L)=log_2(512M/K_star),  M=2^(2L-13).           (5.2)

An actual common event attains that bound. Include all M states in C_0 and exactly
K_star-M states from C_1. To specify the latter subset explicitly, parametrize C_1
by the unfixed X coordinates in increasing residue order, then q, then the remaining
unmasked free Y coordinates in increasing residue order. There are

    (L-5)+1+(L-8)=N-8

such bits. Their inverse is given by the masked formulas in section 2 with
p=a=r=s=0,z=1 and q free. Hence their binary rank ranges over 0,...,2M-1 bijectively.
Let C_1_prefix contain precisely the states with rank <K_star-M, and set

    E_star=C_0 union C_1_prefix.                      (5.3)

The order is fixed on common hidden labels, not by c. Since M>=32,
K_star=2M+floor(2M/49)>2M and K_star<3M, so this prefix exists. Under U(.|E_star),
each setting's only histories are H_c(0) and H_c(1), with probabilities
M/K_star and 1-M/K_star. Both settings therefore have

    Delta_L = 1/2-M/K_star <= 1/100.                  (5.4)

The law is normalized and attains (5.2); no off-target record is hidden. Uniform
input conditioning is the given mathematical class, not a claimed physical acceptance
or success process. The finite rounding is essential:

| L | N | M | K_star | Exact class-B minimum | Attainer's TV error |
| --- | --- | --- | --- | --- | --- |
| 9 | 14 | 32 | 65 | log_2(16384/65) | 1/130 |
| 10 | 16 | 128 | 261 | log_2(65536/261) | 5/522 |
| >=9 | 2L-4 | 2^(2L-13) | floor(100M/49) | log_2(512M/K_star) | 1/2-M/K_star |

This proves the exact infimum and its attainment for the entire allowed family,
without replacing the finite event problem by continuous weights. Other optimal
events may exist; (5.3) is an explicit one.

## 6. What the 1% relaxation changes, with exact bounds only

For calibration, the same source partition recovers the already reviewed zero-error
endpoint without using its off-main proof as a premise. Zero bad-history mass in
both settings forces u=v=w=t=0 and x=y=1/2. The finite KL identity gives
(8+7)/2=15/2 bits in class A. Uniform conditioning requires equal cell cardinalities,
so K<=2M, attained by C_0 and the q=0 half of C_1, at cost 8 bits in class B.
This is the original E_8 event. No new result at other positive tolerances is claimed.

### 6.1 Class A: a strict reduction and a robust positive cost

The exact value is (4.4), an algebraic/logarithmic expression. No decimal root or
floating-point cost has been used. Two simple analytic bounds clarify its scale.

For an upper bound, the common law

    nu_simple=alpha U(.|C_0)+(1/2)U(.|C_1)+beta U(.|Z)

has full-history TV exactly beta for both settings. Its cost is

    alpha log_2(512alpha)+7/2+beta log_2(512beta/493).

Here 512alpha<2^8 and 512beta/493<2^-6, so

    C_A <= D_2(nu_simple||U) < 8alpha+7/2-6beta
                              =184/25 bits.          (6.1)

For a lower bound, every feasible law has mass at least 1-2beta=49/50 in the
common-good event C_0 union C_1, whose reference mass is 3/512. The two-event KL
partition bound gives

    C_A >= d_2(49/50 || 3/512),                        (6.2)

where d_2 is binary relative entropy. The binary divergence is increasing in its
first argument above 3/512; this follows by differentiating its finite expression.
For completeness it is strictly greater than seven bits. Indeed
log_2(512/3)>59/8 because (4/3)^8>8. Also
h_2(1/50)<3/20: its first term is less than 6/50, and its second is less than 3/100,
using -(1-z)ln(1-z)<=z and ln 2>2/3. Dropping a positive cross-entropy term in (6.2)
therefore gives

    C_A > (49/50)(59/8)-3/20=2831/400>7.              (6.3)

The elementary ln 2>2/3 follows, for example, from strict convexity of 1/t on [1,2]
and its integral. Equations (6.1)–(6.3) imply a saving greater than 7/50 bit from
15/2, while retaining a cost above seven bits for this fixed mathematical benchmark.
They are broad certified bounds; (4.4), not a rounded decimal, is the exact optimum.

### 6.2 Class B: a smaller bounded reduction

Because 2M<K_star<=100M/49,

    0 < 8-C_B(L) <= log_2(50/49) < 1/32 bit.           (6.4)

For the final strict bound, ln(1+1/49)<1/49 and ln 2>2/3 imply
log_2(50/49)<3/98<1/32. Formula (5.2) retains the exact L dependence and granularity.
The bounds quantify reductions in conditional relative entropy. They do not measure
physical memory, source hardware, energy, gate complexity or an apparatus success rate.

## 7. Interpretation, assumptions and scope

| Ingredient | Mathematical standing and physical boundary |
| --- | --- |
| Selected F, original observer and all four cuts | Fixed by the owner contract and main source definitions. No different native rule, apparatus, readout or history recoding was selected to improve the result. |
| Given precursor root and uniform U_c | Conditional reference law; the visible root/request and its physical production are not priced or constructed by D_2. |
| Common law across c | Every witness is a single law/event on Omega. Joint atom definitions compare two deterministic maps on common hidden labels; they assume no physical simultaneous measurement of both settings. |
| Positive error | All raw bad-history mass is included in TV. Partitioning for analysis is exact because target probability is zero on every other history; it grants no coarser observer or output postselection. |
| Class A | All normalized laws were allowed. The optimum uses target-fitted algebraic real weights on all six atoms, including positive mass outside the old exact support. No finite-bit sampler, physical randomness source or precision-cost theorem is supplied. |
| Class B | Uniform source conditioning is allowed, with any common hidden event. The explicit prefix event is target-fitted mathematics, not a readable physical herald or source producer. |
| Fixed 1% tolerance | The theorem solves only the approved beta=1/100 problem. Neither a full error-cost curve nor arbitrary-precision quantum approximation follows. |
| L>=9 | Atom masses and the A law are uniform on this family; B's exact finite-cardinality term depends on L. This is a local finite-history result, not a uniform physical quantum compiler or resource bound. |
| Apparatus, availability and resources | No producer, selectable native controller, logger, clock, failure/retry process, renewal or composite instrument is constructed. INT-AVAIL, #866 sourcing and #1220 total resources remain separate. |

In class A the permitted error can be spent on genuinely wrong histories, not just
on reweighting the original pair. In the attaining class-B event, it is spent only
on the imbalance of the two target-history probabilities. Neither construction is
an independently motivated OI selection rule. An actually sourced implementation
would have to include its preparation/controller/record/failed-attempt/residual laws;
the four-cut passive projection is not their complete operational history.

Thus this is a robust preparation-cost statement for one classical native benchmark.
It supplies no Born derivation, coherent quantum operation, Bell/no-signalling theorem,
coverage/soundness of all quantum protocols, or OI-derived Level B. The physical-source
gate remains **NOT PASSED**; no positive physical mechanism or general OI obstruction
is inferred from a relative-entropy lower bound.

## 8. Verification, evidence retention and independent review

All Boolean case splits, cell counts, TV identities, the variational certificate,
cardinality argument, algebraic-root definition and witnesses were derived by hand.
Static tools check only source/document bytes, hashes, paths and publication diffs.
No numerical/scientific/Lean program, optimizer, simulation, code enumeration,
workflow dispatch/rerun or physical-source investigation was executed. Ordinary
automatic PR CI is repository validation, not mathematical or physical certification.

The mathematical proof is contained here. The three pinned main sources provide
the actual model/target definitions; the target raw tuples follow directly from
their E_8 law and F and are explicitly fixed above. The owner authorization supplies
governance and the selected contract, not an entropy theorem or physical premise.
The scoping proposal is provenance of the adopted test. The #1227 exact proof and
its model review are off-main historical calibration; the comparison values needed
here were re-established in section 6. No #1228 selection claim, missing historical
H input, author-posted acceptance or off-main physical theorem is a premise.

This new proof and its required fresh non-author full paper/algebra review are
currently off main. Before any enduring established claim uses them, retain all
claim-relevant proof, source/authority and review evidence under A.42/A.46 and obtain
the separate integration decision. A linked branch, comment, digest or CI result
alone does not close those duties. Existing #1226/#1227 and ChatGPT's #1228 ownership
and scientific gates are unchanged.

The independent reviewer must verify the entire positive-error source classification,
small-ring aliases, exact TV reduction, every sign/equality in the class-A certificate,
algebraic-root existence, normalization and both error values, class-B integer bound
and explicit prefix witness, and the interpretation/retention limits. Material errors
require correction and exact-checkpoint re-review. Author completion is not acceptance.
