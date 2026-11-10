# PREP-MIN-ROB-1 — 1% complete-history preparation robustness

**Paper-only author WIP; lower-bound/attainment proof in progress; independent review pending.**
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

## 3. Remaining proof at this checkpoint

The next author pass will derive the exact TV inequalities on the six atom masses,
then prove the class-A variational minimum and class-B finite-support minimum and
supply explicit common attainers. The source partition is an analytical device, not
permission to coarsen or relabel the raw observation metric. Independent full paper
review at a complete immutable checkpoint remains required. Physical source NOT PASSED;
INT-AVAIL, Level B, Bell/composition, execution and integration remain separate.
