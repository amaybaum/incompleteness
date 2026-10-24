# The sidecar junction meets an unprepared causal boundary

Status: author-checked research result; independent review pending.
24 October 2026. Continuation of draft PR #910, initial checkpoint
`3fcaa271e689209dd74272c14a924c8f7fe44998`.

## Decision and scope

The unchanged site `s=qY+(0,-1,2)` at tick `N=R+3` is not a deterministic
raw-Y transfer or clean Y code for all allowed initial complements. An
unconstrained initial triple reaches it along a unique axial first-arrival
path. Conditional on every other initial coordinate, its map to the whole
terminal triple is a permutation of all eight values.

This is a result about the proposed untouched junction. It neither excludes
a redesigned apparatus with additional compatible initial preparation nor
establishes a joint record law. No physical premise or acceptance rule changes.
The productivity test is whether the calculation constrains the actual
junction beyond the known warning that some neighbors were uncomputed.
The explicit free coordinate and the incompatible blanket preparation meet
that test: NEW for this junction, using the inherited first-arrival principle.

## 1. A free coordinate in the actual apparatus

Use the existing parameters `T=185`, `P=12*840^T`, `S=T+P`, `d=68`,
`R=S+d`. Coordinates in this section are absolute. Then

    s = (0,S-1,d+2),       N=R+3,
    f = s-N e_y = (0,-d-4,d+2) = (0,-72,70).

Let `M=U_0(f)`. The distance from f to s is exactly N, with a single
shortest path, along +y. The initial triple M is outside every prepared
current ball in the retained apparatus, even if the optional q3 extension
is included. The previous balls are smaller and add no current constraint.

| Initial current ready region | Distance minus its radius |
| --- | --- |
| Original X,Y,R receivers, radius T | 142 |
| Relocated original Z, radius T | 3T+142 |
| Relocated original herald, radius T | 7T+142 |
| Transported X,Y,R receivers, radius S | 142 |
| Transported Z, radius S | 3T+142 |
| qY collision, radius R | 6 |
| qR collision, radius R | 142 |
| q2 extension, radius R+2 | 2 |
| Optional q3 extension, radius R+3 | 2 |
| Remote herald and Z, radius R | 11R+142 |

The original five centers are `(0,T,0)`, `(T,0,0)`, `(-T,0,0)`,
`(4T,0,0)`, `(0,0,-8T)`. The first four are also translated by P e_y
for transport. The collision centers are `(0,S,+/-d)`, the optional
outward centers are `(0,S,d+2)` and `(0,S,d+3)`, and the remote centers
are `(+/-12R,0,0)`. This inventory is the retained native-X/selector/outward
construction; no optional mirror-memory correlations are added.

The exact 1,479-entry source table contains no entry at f. Neither the
selector controls nor the reset pulses occupy f. Remote herald sources
have x>=12R, and the remote Z source has x=-12R. Thus M is an ordinary
unpinned complement coordinate, not an affine seed copy. Under the
inherited independent-uniform-complement prior it is a uniform triple,
independent of the input and apparatus seeds.

Moreover, `dist(f,qY)=R+6`, `dist(f,q2)=R+4`, and `dist(f,q3)=R+5`.
Varying M changes neither the established Y operand nor q2 through R+2,
nor the optional q3 result through R+3. It also cannot change the sidecar
through R+2. The original large-torus no-wrap condition is retained.

## 2. The complete update, with every background term retained

Write `v_k=f+k e_y` and `V_k=U_k(v_k)` along the unique ray. For k>=1,
the full six-neighbor, second-order native rule is exactly

    V_0=M,
    V_k = a_k XOR H(V_(k-1) XOR b_k),
    a_k = U_(k-2)(v_k),
    b_k = XOR of U_(k-1) on the five neighbors other than v_(k-1).

The old term a_k cannot depend on M: its site is at distance k and its
time is k-2. Each of the other five neighbors is at distance k+1 and
time k-1. Thus every a_k and b_k is fixed when the other initial
coordinates are fixed. They include *all* lower-source behind-front
contributions, unknown old-input terms, and other free complement fields
where those can arrive. None is set to zero or approximated by a
first-arrival-only lower formula.

For any fixed triples a,b, `z -> a XOR H(z XOR b)` is a permutation,
since `H(A,B,D)=(B,D,A XOR BD)` has inverse
`H^-1(A,B,D)=(D XOR AB,A,B)`. Composition gives an exact permutation
`Pi_C` depending on the fixed complement C, such that

    U_N(s)=Pi_C(M).

This proves the dependence and the law without evaluating an astronomical
background-dependent permutation or simulating N ticks. It is not an
explicit polynomial table for the five other neighbors.

At the final update, put `(a,b,c)=XOR_{w~s} U_(R+2)(w)`. The accepted
old slice is `U_(R+1)(s)=(0,1 XOR y,x)`, so the exact terminal identity is

    U_(R+3)(s) = (b, 1 XOR y XOR c, x XOR a XOR b*c).

Only the -y neighbor can contain M at this time: its distance from f is
N-1; the other five distances are N+1. Hence that last neighbor XOR,
and then the final triple, range over all eight values. In particular no
raw field, its complement, or nonconstant local decoder can be guaranteed
to equal y or a separately inserted diagnostic p across all complements.
The diagnostic intervention at qY is itself outside M's causal influence,
so it does not invalidate this argument.

## 3. Probability and history boundary

Under the specified independent uniform M, for each fixed assignment C,

    Pr(U_N(s)=w | C)=1/8  for every raw triple w.

This marginal remains uniform when conditioning on the initial input,
seeds, earlier Y outcome, and remote herald, since those are independent
of M. Retaining all M values therefore gives four zeros and four ones
for every raw output field at fixed actual operand. Discarding the
unwanted values would introduce a new event whose full law needs proof.

This does **not** prove uniformity conditional on the complete public
history: M may reach an old public port earlier. For example its distance
to the original X port is T+142, less than R. Distance permits that
dependence; it does not establish an actual leak or a joint masking law.
A history-aware decoder or later native processing is not ruled out.

## 4. Why a blanket cold extension is incompatible

One might add current `B_(R+3)(s)` and previous `B_(R+2)(s)` as blank
regions. Their interiors or boundaries contain:

| Coordinate | Role | Distance to s |
| --- | --- | --- |
| Current (0,-1,0) | old independent frontier M1 | R+2 |
| Current (0,-2,0) | old independent frontier M2 | R+3 |
| Previous (0,0,0) | unknown old input triple | R+1 |

These coordinates cannot be set to zero while claiming the same initial
resources. This obstruction applies to a blanket-zero prescription, not
every possible extension. It also does not say every captured variable
actually affects this particular endpoint.

Inside the unwrapped causal cone there are two decoupled spacetime parities:
`sum(v)+t mod 2` is
the same for the old local term and all six contributing neighbors.
The inherited torus has odd side length, so this is a local no-wrap
argument, not a global bipartition of the periodic lattice.
The target parity is even. Current M1 and the previous unknown input
are in the odd sector; a preparation restricted to the active sector
need not touch them. Current M2 is even and remains a protected exception.
All current M_j with j>=3 are outside this target cone.

### A compatible initial prescription, with an uncomputed law

The initial geometry admits the following conditional extension. In the
current ball B_N(s), pin newly unprepared even-parity coordinates to zero,
preserving the existing sources and M2. In the previous ball B_(N-1)(s),
pin newly unprepared odd-parity coordinates to zero. Leave the opposite
sector unchanged. This is a new *initial* apparatus prescription, not a
late modification or a statement about the original unextended apparatus.

The protected frontier families have exact distance slacks relative to N:

| Initial current family, positive index | Distance to s minus N |
| --- | --- |
| M_j=(0,-j,0) | j-2 |
| N_j=(0,0,-9T-j) | 9T+j-2 |
| F_(X,k), F_(Y,k), F_(R,k)=Q_i+(S+k)e_y | k |
| F_(Z,k)=Q_Z+(S+k)e_y | 3T+k |

Thus M1 is in the untouched sector, M2 is an explicit untouched exception,
and the rest lie outside. The remote banks are outside by their inherited
x separation. All 1,479 old source coordinates are checked; only the origin
lies inside. The Z selector and opposite reset pulse are also outside.
The unknown previous origin remains in the untouched sector. No input-
dependent pin or new seed is required for this geometric prescription.

The exact active-sector computation consequently reduces to **six current
sources**, with a zero previous active sector:

| Absolute coordinate | Preserved initial triple |
| --- | --- |
| (0,0,0) | (0,x,0) |
| (0,2S,0) | (0,mY XOR mR,0) |
| (T,P+S,0) | (0,mY,0) |
| (-T,P+S,0) | (0,mR,0) |
| (0,S,S+2d) | (u,0,1) |
| (0,-2,0) | M2, an independent uniform triple |

This is a finite-speed reduction of the proposed prepared cone, not an
evaluation of its output. The origin is two steps behind its first-arrival
front at the target; M2 and the three selector controls are on the boundary.
Interactions therefore cannot be replaced by a sum of isolated pulses.

In particular M2's *isolated* first-arrival contribution cancels: the
displacement is `(0,S+1,70)` and `(S+1)&70=2`, so the shortest-path count
is even. That does not prove cancellation in the populated nonlinear cone.
Keeping this as a countercontrol prevents treating causal inclusion alone
as proof of influence, just as it prevents deleting M2 without calculation.

The next focused task is the exact six-source native output and the
diagnostic operand test under this initial prescription. Any favorable
result must also prove the joint old-record/carrier law: preserving the
frontier variables alone does not preserve their independence from a new
carrier that may use M2. Pinning only f does not implement this extension;
the whole newly specified active portion of the cone is part of its cost.

## Checks

Run `python3 junction_v4/checks.py` from this checkpoint root (or use an
absolute script path), and repeat with `-O`. The script uses no inherited
dynamics module and checks:

* actual giant-integer geometry, all 15 ready balls and the 1,479 sources;
* all 64 fixed-offset maps on all eight triples;
* 144 independent full 3-D causal-recursion cases with dense current and
  previous backgrounds, all eight pivot values, six directions, lengths
  1..8 and three backgrounds;
* a countercontrol distinguishing the full equation from H^N(M), and
  a two-path cancellation showing distance alone is insufficient;
* the terminal sidecar identity, captured-resource/parity inventory, complete
  reserved-bank inequalities, and isolated-M2 cancellation countercontrol.

Normal and optimized output is byte-identical. These finite controls
exercise the analytic unique-path argument; they do not replace its
all-N proof. No joint-history certification, native reset, Lean proof,
or general obstruction to OI is claimed.
