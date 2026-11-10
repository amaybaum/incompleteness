# PREP-MIN — exact declared-history preparation cost through t=2

**Paper-only WIP; author checkpoint, proof incomplete and independent review pending.**
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

## 3. Remaining proof work at this checkpoint

The full proof must independently derive the common support cells, rule out alternative
allowed histories, handle L=9/10 aliases, establish class-A variational and class-B support
bounds, and give attaining common laws/events. The provisional comparison is A: 3,9/2,15/2
bits and B: 3,5,8 bits through cuts 0,1,2; no result is accepted at this checkpoint.

The complete microscopic outgoing-law comparison is different: bijectivity would fix
nu=eta if that stronger target were required. It is not the operational optimization.
All physical sourcing and executing availability remain separate; the source gate is
NOT PASSED. Exact-checkpoint independent paper/algebra review and ordinary CI remain gates.
