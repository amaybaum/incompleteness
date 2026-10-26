# Conditional native post-Y phase preparation: combined law

Research checkpoint based on the reviewed native controller at
bf1bc9fb067e38417d8968e26a691debf7d3eb5f and synchronized remote-source
construction at 25220128c3c7991e4c22c917af56b68c02ab8051. The actual selected
physical fields now have the calibrated post-Y distribution jointly with
the old public record and new herald, under the supplied initialization and
access assumptions. No nonlinear initial seed function is used.

This is a post-Y **two-slice phase-preparation candidate** on the retained
native family. Y occupies a previous-slice field and X/R share a current raw
port. General native menu readout, next-stage closure and an arbitrary late-q8 socket
remain open. This report does not designate a reusable instrument or alter
the observer's access class.

## One physical initial preparation and one deadline

Keep T=185, P=12*840^185, S=T+P, R=S+68 and L=R+9. All existing old sources,
readiness and the seven-port independent frontier bank through L are retained.
The local current/previous ready balls are those about q9=(0,S,77), with
radii L and L-1. Preserve W=111, Q,C,G and the three boundary exceptions:

| Initial source | Position | Payload |
| --- | --- | --- |
| J | (0,S,S+154) | (u XOR b,a,u XOR a) |
| Kplus | (1,S,S+153) | (a XOR b,0,a XOR b) |
| Kminus | (-1,S,S+153) | (a XOR b,a XOR b,a XOR b) |

The new independent fair seed bank is (a,b,k0,k1,k2,z), six bits, independent
of old variables under the stipulated initial preparation. Every source
field is affine in those seeds and existing u. The remote compiler shares
a,b with these local sources; it does not redraw them. The old used seed u
is not treated as fresh.

At c_G=(48L,0,0) use the original-time affine compiler hemisphere in
herald_v10/REPORT.md. Its exact word is the retained 2684-step Y predicate,
followed by (P-2424)/6 identity words of length six and two final H steps.
Its complete raw prefix is blank and terminal triple is (0,G,0) at L.
The predicate accepts K=k0+2k1+4k2 below 5,0,3,2 for (a,b)=00,01,10,11.
This is the original 5/16 benchmark, not the separately considered 5/32
fair-J alternative. That alternative was parked before computation.

At c_Z=(-48L,0,0), a pure-A z source at c_Z-L e_y gives (0,0,z) at L,
with a blank prefix. The local/remote source families coexist: old sources
and banks have |x|<=13R; the new remote cones have |x|>=47L. The remote
program and z source cannot affect the local outputs, old records or each
other by L. J,Kplus,Kminus cannot affect the earlier Y read or any old
public port by L. None pins an old frontier coordinate. Use the explicit
enlarged no-wrap side 256L+64T+1. Enlarging this finite resource does not
change P or any of the earlier local causal calculations.

The independent native reviews establish the separate physical mechanisms.
The present calculation checks their actual joint seed variables and output
law; its inputs are their retained source data, not an invented reset map.

## Fixed phase code and actual success law

Write y=x XOR u for the native Y value. On every retained x,u,mY,mR and
accepted mask 00,10,11, the unchanged native dynamics gives

    U_(L-1)(q8)=(0,y,0),
    U_L(q9)=(0,y XOR a,y XOR b),
    U_L(c_Z)=(0,0,z),
    U_L(c_G)=(0,1,0).

Define one fixed selected-phase encoding for j=(X,Y,R,Z):

    E_phase(j) = (previous q8=(0,Y,0),
                  current q9=(0,X,R), current c_Z=(0,0,Z)).

Its inverse reads X=q9.B, Y=previous q8.B, R=q9.D and Z=c_Z.D. This map is
independent of old x,u,pads and history. It is a coordinate comparison, not
a newly available physical observer operation. The complete physical phase
also retains other apparatus information; no erasure or independence of the
whole neighborhood is claimed.

For each fixed old row, direct combination of the actual controller table
and native herald program yields 20 successful and 44 failed worlds among
64 equally likely new seed assignments. Conditional on success,

    j=(y XOR a,y,y XOR b,z),
    Pr((a,b)=00,10,11 | G=1)=5/10,3/10,2/10,
    Pr(z=0 | a,b,G=1)=Pr(z=1 | a,b,G=1)=1/2.

Thus the entire selected raw success-phase distribution is the same at a
fixed y for all old rows, not merely its decoded one-sign marginals. The
carrier is the supplied calibrated mu_Y,y. Its probabilities are not derived
as parameter-free predictions.

## Complete old record, new herald and failures

Let D be the inherited informative record, including the earlier flags and
an allowed whole q8 Y read (0,y,0) at L-1. Keep every earlier flag combination
in the record and offer no new carrier if the predecessor already terminated.
For branches on which the retained native-family incoming assumptions hold,
let N be the entire seven-port post-deadline noise word through L. Its bit
count is B=6P+18d+189. The independently reviewed chronological proof gives
N uniform conditional on the initial bank complement. The combined source
geometry keeps that bank free and all selected success-phase fields, D and
G are functions of the complement.

Consequently, on each nonzero-probability valid incoming history,

    Pr(N=n,G=1,E_phase(j) | D) = 2^(-B) (5/16) mu_Y,y(j),
    Pr(N=n,G=0,offered=none | D) = 2^(-B) (11/16).

The new herald's whole predeadline record is zero and its final whole cell
is (0,G,0), so it has no unaccounted K metadata. Neither masking nor heralding
changes the probability of an informative old record. At a predecessor
failure the native fields and new flag still evolve, but no offered quantum
state is inferred. The prior conditional reference is not extended to a new
successful measurement after such a terminal failure.

The physical G=0 fields are retained separately. The rejected K counts for
00,01,10,11 are 3,8,5,6. For rejected runs with masks 00,10,11 the same local
formula (0,y XOR a,y XOR b) still holds. Pattern01 instead gives

    U_L(q9)=(u,y,x(1 XOR u)).

The four (x,u) raw values are 000,110,011,100, in lexicographic order.
They are not replaced by a chosen qubit failure state. z is still jointly
fair with every rejected mask, and previous q8 retains y. The exact full
physical failure distribution is checked, in addition to the terminal
no-offered-carrier convention. Exposing those private fields or q9's private
prefix would change the access contract and require another record proof.

## Restricted terminal X and R record checks

Under the candidate's permitted whole-q9 terminal read at L, no raw field
is suppressed. On a successful post-Y branch its (X,R) pairs are
(y,y),(1 XOR y,y),(1 XOR y,1 XOR y), with probabilities 1/2,3/10,1/5.
For designated X the quantum outcome is fair. The additional R field has
conditional weight 1 when X=y, or weights 3/5,2/5 when X differs from y.
For designated R the quantum probabilities are 4/5,1/5. The extra X field
has weights 5/8,3/8 when R=y, or weight 1 when R differs from y. These
refinements depend only on the earlier public y, setting and outcome, not
the original preparation conditional on that record.

This gives a bounded terminal X-to-Y-to-X or X-to-Y-to-R record comparison
on the post-Y family, inheriting the predecessor's native-family/record law
and the candidate's declared terminal-access and clock convention. It does
not derive that access rule, a direction selector, or menu reads on arbitrary
inputs. If the terminal port is also exposed on G=0, its actual raw failure
law above must be retained as failure metadata; no successful reference
measurement or offered carrier is asserted there.

After any nonzero whole-port record the unchanged phase has sharp old Y
and sharp X. Its fixed Bloch decoder determinant is -1/4. The terminal
record comparison therefore permits stopping after the read; it supplies
no valid post-read quantum output or reusable instrument. New native
back-action/reset remains necessary, as #912's controls require.

## Readout and reuse boundary

The second-order native state at L is the pair (U_(L-1),U_L), so the selected
phase code contains simultaneous state information in the Markov description.
It does not give three publicly readable current-slice cells. In particular:

- Y is in the previous slice. A native operation delivering it at a later
  permitted read remains unconstructed. Retaining a past public Y record
  is not silently used to replace this physical operation.
- The whole current q9 port contains X and R together. A claimed terminal
  menu read must retain both raw fields, or construct a native separation.
  Reading only the chosen component is not an allowed shortcut.
- The forced-q8 diagnostic still fails: changing q8.B alone with its actual
  surrounding past retained does not make q9 follow that arbitrary input.
  This is an exact native-family construction, not a reusable q8 socket.
- The rest of the two-slice neighborhood can contain old history and used
  frontier variables. The next native instrument must accept that boundary
  and prove its branch law. A standalone cold apparatus cannot be spliced in.

Thus preparation, menu access and compositional closure have distinct
outstanding obligations. The current phase candidate has the correct
conditional calibrated success law; no full OI-QM equivalence follows.

## Exact validation

checks.py reads the pinned actual symmetric-controller table and evaluates
the retained 2684-step predicate word on all 32 seed assignments, including
its final H phase. It enumerates all 1024 old-row/new-seed worlds, verifies
32 success/failure branch measures, 208 nonzero raw phase cells and 96
whole-port terminal-refinement branches, and
checks the complete physical rejected distribution. Normal and optimized
execution are byte-identical to result.json. Failed controls raise before
a pass verdict is emitted.

Independent countercontrols give full-law TV1/10 for swapping 5:3:2 to5:2:3,
TV1/2 for shared z despite its fair marginal, and TV1/2 in the required X
marginal if old u is reused as the fresh mask (even with the correct total
herald mass). Discarding the failure runs is rejected by normalization.
The combined source/deadline/remote-envelope inequalities are checked at
actual giant parameters. The enormous noise factor rests on its written
bijection proof, not a finite enumeration of all noise words.

Replay from this directory in the retained tree:

    python3 checks.py
    python3 -O checks.py

Both must match result.json; SHA256SUMS pins the files. Source commits and
input hashes are in PROVENANCE.json. No new kernel certificate, exact-head
attestation, premise, access rule, F/E designation, dispatch or merge is
asserted. Separate integration review is required before synthesis adoption.
