# Native-Y continuation: reversible interface and a boundary-control obstruction

24 October 2026. Research continuation of OI Research Work. Repository read-only;
no commits, pushes, comments, dispatches, premise adoptions, or certification claims.
The transport-proof review remains open. These are author results, not an
independent review or Lean certificate.

## Result

The accepted incoming code is `(A,B,D)=(y,y,1 XOR xy)`, where x is the earlier
public X outcome and y the actual arriving Y operand. There is a particularly
simple total reversible four-bit normalization. Moreover, the auxiliary bit
need not accumulate garbage if x and y are retained as accessible controls.
This resolves the logical information accounting, not native implementation.

A separate exact calculation rules out a concrete attempted native shortcut:
adding initially prepared B-field pulses on two specified sections of the
receiver's first-arrival boundary. Even with all twenty relevant slice entries
freely controllable, the full output cannot depend on y alone. On y=1 it obeys
`B XOR D=x` for every setting. A larger routing stage or a different collision
geometry is required to obtain the requested clean socket through this route.

## 1. Total reversible interfaces

With an initially clean auxiliary bit E, define

    F(A,B,D,E) = (E, A XOR B, A, 1 XOR D).

This is a permutation on all sixteen inputs, with inverse

    F^-1(a,b,d,e) = (d, b XOR d, 1 XOR e, a).

On the native domain:

| x | y | Incoming triple | Clean triple | Retained E |
|---|---|---|---|---|
| 0 | 0 | 001 | 000 | 0 |
| 0 | 1 | 111 | 001 | 0 |
| 1 | 0 | 001 | 000 | 0 |
| 1 | 1 | 110 | 001 | 1 |

Thus the retained bit is exactly x AND y. The two x histories with y=0 were
already indistinguishable in this three-bit input; F makes no claim to recover x.
The construction is affine: one XOR, one NOT and a wire permutation suffice as
abstract circuit operations. No claim is made that these are freely available
operations of the native lattice.

If the earlier public x is available as a retained physical control, no new
clean bit is logically required. Define instead

    G(x,A,B,D) = (x, B XOR A, D XOR 1 XOR xA, A).
    G^-1(x,a,b,d) = (x, d, a XOR d, b XOR 1 XOR xd).

Then `G(x,y,y,1 XOR xy)=(x,0,0,y)`. G is also a total permutation. Equivalently,
after F one can uncompute E by `E <- E XOR xy`, while preserving x and y.
That operation is reversible on the full domain and returns E to zero on
native inputs. There is no necessary growing garbage register for this logical
normalization alone. The actual stochastic reset has its own retained-state
and fresh-resource obligations; this does not eliminate those.

Crucially, an earlier public record is not automatically a native control
available at the required site and time. We have not constructed persistence
or transport of x, a lattice implementation of G, or a new permission to
preload the unknown x into the apparatus. The original clean-ancilla counting
obstruction remains correct when x is unavailable and no other state is retained.

## 2. The attempted native boundary repair

Keep the actual parameters and update unchanged:

    T=185, P=12*840^185, S=T+P, d=68, R=S+d,
    U_(t+1)(v)=U_(t-1)(v) XOR H(XOR of six neighbours),
    H(A,B,D)=(B,D,A XOR BD).

Coordinates in this section are relative to qY. The receiver is q2=(0,0,2)
at tick R+2. Consider extra initial B-field sources at `(a,b,z)` with z=1 or 2
and `|a|+|b|+|z-2|=R+2`. No other initial sources or slices are changed in the
local model. Their distance to qY is R+2z>R and to the original upper pulse
at `(0,0,R)` is 2R. They cannot affect the original qY endpoint at R, or
interact with that pulse before R. All lower first-arrival fields have the
same rotating field phase, so their contributions before the collision are
linear path-parity sums.

In the shrinking backward cone used by the retained proof, these sources
cannot alter the R-2 slice: its radius is two, while four steps of radial
progress would be needed. On the R-1 slice their only possible changes are
B-field entries at:

- z=1, |a|+|b|=2: eight entries;
- z=2, |a|+|b|=3: twelve entries.

The analysis allows all twenty changes independently. This is a relaxation:
it proves a negative result even before imposing full-apparatus compatibility.
The retained source witnesses also realize each entry individually in this
local cone by exact no-carry parity, but no successful apparatus modification
or global readiness/prior compatibility is claimed or adopted.

Let k be the XOR of the four axial changes at `(0,+/-2,1)` and `(+/-2,0,1)`.
Let l be the XOR of all twelve changes on z=2. The other four diagonal z=1
changes cancel. Three ordinary native updates give exactly

    A = y,
    B = y XOR uk XOR l,
    D = 1 XOR xy XOR u(1 XOR x)k XOR yl,
    y = x XOR u.

The old selector masks cancel for every assignment. Thus the twenty controls
reduce to two effective parities for this endpoint. On y=1, u=1 XOR x, and

    A=1,  B XOR D=x.

The x=0 and x=1 outputs therefore have disjoint full-cell codes for every
setting. This excludes every Y-only full-triple encoding in this family,
including `(0,0,y)` and `(1,y,1)`. The invariant even survives history-dependent
choices of k and l; treating those as implementable is not needed for the
negative result. Randomizing these controls does not create a clean full triple.

This is not a general no-go for the lattice, ancillas, extra time, other source
fields or positions, native history-controlled routing, or the complete Y
instrument. Nor is retaining x itself a privacy failure: x is already public.
The obstruction concerns the requested clean interface, not excess secret
information at the terminal read.

## 3. Verification and provenance

The source handoff was read in full for the native-Y result and its synthesis;
the relevant earlier localized-reset and Y-adapter reports were also read.
All ten retained handoff checkers replayed normally and with Python -O, with
byte-identical recorded outputs. This does not close the wider transport-proof
review or rerun every earlier baseline test.

New checks:

- Both interface maps and their inverses on all sixteen states, all four native
  histories, and the conditional auxiliary-bit recycling identity.
- Twenty explicit source witnesses and their exact first-arrival parity, the
  complete relaxed shell support, separation from the upper pulse, and
  inability to affect qY at R.
- 16,777,216 bit-parallel native input/control cases, including every old
  selector-mask assignment, agree with the displayed full-triple formula.
- 33,554,432 diagnostic cases replace the incoming qY D operand by p and retain
  A=p. These replacements are tests only, never native operations.
- A separate Boolean-polynomial implementation of the three updates derives
  the same formula and the invariant symbolically. It shares the previously
  reviewed upper-pulse recurrence, so is not an independent transport proof.
- Wrong finite-phase extrapolation, discarded-garbage and missing-history-AND
  controls are rejected. All new checks remain active with Python -O.

The copied `core.py` is byte-for-byte from the accepted native-Y handoff. Hashes
are in PROVENANCE.json and SHA256SUMS. `patterns.json` records the actual
large-integer source witnesses; no large-torus tick simulation is claimed.
The boundary family and its reduced formula were found exploratorily, not
under an externally frozen preregistration. No subagents or independent
reviewers were used in this continuation.

## 4. Remaining construction

The next native obligation is to implement a history-controlled or larger
routing stage, using initially specified resources, without silently cleaning
neighbouring fields. G is a precise logical target if native x persistence and
transport can be supplied. F is the alternative with one clean bit and explicit
retained public information. A fixed reversible circuit alone does not satisfy
that obligation.

The native 5:3:2 Y reset, fresh conditional resources, enlarged joint observation
window, complete outgoing-carrier law, X→Y→X and X→Y→R diagnostics, and all failure
branches remain open. The early prefix `(1,u,0)` remains informative and still
requires the existing supplied delayed-access convention. No native clock,
shutter or access closure has been constructed. Exact reconstruction and the
separate finite-precision OI programme retain their distinct status.

## Replay

From the extracted bundle root:

    python3 continuation/checks.py
    python3 -O continuation/checks.py
    python3 continuation/symbolic.py
    python3 -O continuation/symbolic.py

The symbolic script writes its derived polynomial JSON in the extracted folder.
All computation uses the Python standard library and no network. Compare the
printed output with the retained .out files. The original handoff is identified
by hash but need not be downloaded to replay these new local checks.
