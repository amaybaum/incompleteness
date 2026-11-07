# Forward paper recovery for Q-A

**WIP / independent review pending.** Author: root, 7 November 2026.
Accountable home #1169; [bounded forward scope](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6713553987).
This repairs the written proof/scope findings in
[the additional review of merged #1184](https://github.com/amaybaum/incompleteness/pull/1184#issuecomment-6713513478).
It preserves the original construction. These are paper derivations, not new
kernel results or physical mechanisms. No scientific program was run.

## 1. Exact scope of the R1 complete-positivity recovery

Fix a finite non-adaptive protocol in N on a bipartite graph, with the same
single carrier cell as input/output and the fixed R1 frame. Condition on its
externally supplied settings, constants and heralds. They do not depend on
the input state. Every other initially unknown variable, including each
ready cell's unknown slot, has the independent uniform product law used by
N2/P2; known ancillary slots have their supplied values. The input carrier
law may vary independently of those auxiliary variables.

These are the product-ready instrument inputs, applied through the open
H-PREP identification. They are explicit assumptions, not a preparation
theorem. For an infinite sector the finite cone needs the stated normalized
product marginal, H-INF-mu. This proof does not apply to an additional
correlated or preparation-dependent hidden background by declaration.

Write the initial carrier coordinates z,x. Relabel the two G1 sectors so z
is in E and x in O. Let I be the span of initially known ancillary slots,
and pull every final functional back to the initial variables. I is
isotropic and disjoint from the input coordinates. The global linear part
is symplectic and graded; translations only change constants. Let R be the
span of the registered terminal record functionals. Its members commute
with one another and with all active output functionals. These are the
same terminality and symplectic facts used in apparatus-1 Lemma 3.

We keep the **entire joint record**, including records individually masked
by uniform unknowns. Only after proving each branch CP may it be
coarse-grained. No conclusion is inferred from a single marginal record.

## 2. Two elementary lemmas about the recorded information

**No sharp input effect.** The joint record cannot determine both initial
z and initial x. If it did, full support on the remaining unknowns gives

    z = kappa_1 + rho_1,   x = kappa_2 + rho_2,
    kappa_j in I, rho_j in R, up to known constants.

Since the input and I have disjoint support and I is isotropic,
omega(rho_1,rho_2)=omega(z+kappa_1,x+kappa_2)=1.
But R is isotropic. Contradiction.

**Information recorded about z forbids unrandomized retention of x.**
Suppose the record determines z and an active output functional g retains
initial x with only a record-dependent known offset. Then

    z = kappa + rho,
    g = x + kappa' + rho',       kappa,kappa' in I; rho,rho' in R.

Terminal-active commutation gives omega(rho,g)=0. Expansion instead gives

    omega(rho,g)
       = omega(z+kappa, x+kappa'+rho')
       = 1 + omega(rho,rho') = 1.

This is impossible. The analogous statement exchanges z and x.
It is stronger than just saying that an active cell cannot be sharp:
it excludes retaining a conjugate **initial input** value alongside a
terminal record even if the current output cell has been randomized.

The representations used here follow from linear elimination: a functional
constant on the affine subspace cut out by I and the full record belongs
to the span of their linear parts. No finite table or probability bound
is needed.

## 3. Conditional normal form and CP of every R1 branch

Grading and the independent product-ready source make the full instrument
kernel factor by sectors, before any record is discarded:

    K_r(z',x' | z,x) = A_(r_E)(z'|z) B_(r_O)(x'|x).

A sector's record has the form r_E = a z + B eta + c, with eta uniform.
For a fixed nonzero branch, its likelihood as a function of the one input
bit is either constant or a constant times one input-bit indicator.
Indeed a lies in image(B), when both bits have equally many solutions, or
it does not, when at most one bit is compatible.

If the likelihood is constant, solve the conditioned affine equations as
eta = eta_0 + h z + N xi. The free coordinates xi are uniform and independent
of z. A scalar output is therefore either:

- the input bit plus a fixed offset;
- a fixed known bit;
- a fresh fair bit independent of the input.

A nonzero free linear form is fair; its input-dependent shift can be
absorbed into that fresh variable. This changes the **effective** input
coefficient. It need not preserve the raw coefficient displayed before
conditioning. Elimination is performed separately in E and O, so their
residual variables stay independent.

**Case U: the entire joint record is input-independent.**
The two scalar kernels have the three forms above.

- Two retained bits give an encoded Pauli.
- One retained bit and a fair replacement give a Pauli composed with
  dephasing in the retained axis.
- No retained bits give a constant preparation; the permissible outputs
  are an X or Z eigenstate, or the maximally mixed state.
- A known replacement with the other input bit unrandomized is excluded:
  apply it to the corresponding X or Z eigenstate input, which is a
  permitted half-known initial cell. The active output would be sharp,
  contradicting Lemma 3. Two known replacements are excluded likewise.

This exhausts the two-sector scalar normal forms. The listed maps are
CP: Paulis are unitary conjugations, dephasing has its two Pauli
projectors as Kraus operators, and constant preparation of a valid state
is CP. Scale the branch by its constant probability.

**Case I: the record is informative.**
By the likelihood normal form and the no-sharp-effect lemma it determines
one initial coordinate, say z=a, and not x. The opposite output kernel
cannot retain x unrandomized, by the second lemma. It therefore replaces
x by a known bit or a fresh fair bit; it is independent of the remaining
input. The E output is also input-independent since z=a is fixed.
The output is a fixed law sigma_r. Lemma 3, tested with the compatible
half-known input, excludes a sharp law; hence sigma_r is a valid R1
X/Z eigenstate or maximally mixed state.

The encoded branch has the explicit form

    rho -> gamma_r Tr(P_(Z,a) rho) sigma_r,

or its X analogue. This is CP: if sigma_r=sum_j lambda_j |psi_j><psi_j|,
use Kraus operators sqrt(gamma_r lambda_j) |psi_j><Z_a|.
Both cases include zero branches harmlessly. Summing or coarse-graining
the CP branches, and mixing fixed herald/program cases with their
input-independent weights, preserves CP.

**Recovered result.** Under R1 and the stated non-adaptive product-ready
instrument inputs, C-CP holds. This is not a proof for adaptive protocols
or arbitrary initially correlated background sources.

### A masked-record check on the written normal form

For carrier A(z,x), neighbour B(w,0), w fair, one even native coupling
gives A(z,x+w), B(w,z). A later native X read records r=x+w and leaves
A(z+k,x+w), k independently fair. The record is input-independent but,
given r, the raw offset w=r+x is not. Conditional elimination gives a
constant X_r preparation with branch probability 1/2. This is Case U,
not a Pauli mixture with the original raw coefficients alpha=beta=1.
It explains why the unreduced noise-independence inference was invalid.

## 4. An explicit available Hadamard word

Use node 8's C12 and its reverse C21, both realized by the returned
mediator construction of node 1. The graded word
W=C12 o C21 o C12 swaps the two cells. Let Na be the NNB shear on x,
and Nb the other-parity NNB shear on z. Direct substitution gives

    Na o Nb o Na: (z1,x1,z2,x2) -> (x2,z2,x1,z1),
    R=W o Na o Nb o Na: (z1,x1,z2,x2) -> (x1,z1,x2,z2).

The word uses the available parities and free scheduling. Translate z2
by 1 after R (P2 through H-PREP). The result H obeys

    f_z o H=f_x,  f_x o H=f_z,  f_y o H=f_y+1,  p o H=p+1.

Thus its action is the encoded Hadamard needed in A3. This is an explicit
word, not an inference from the uncommitted group check.

## 5. Fixed affine offsets and availability

Within the stated N resource class, every constant translation is supplied.
For a fixed affine coupling G=t_a o L, the available t_(-a) cancels its
offset, giving L. Consequently fixed offsets alone cannot weld a linear
part to its translation while those translations remain independently
available. A weaker class that restricts translations is a different
hypothesis and needs its own source and proof. No 256-case result is used
as a premise.

An affine output map does not imply that the implementing protocol is
non-adaptive. Node 9's separate-availability statement retains its
explicit non-adaptive-realization hypothesis.

## 6. Scope of the hidden-sector conclusion

Reciprocal access to individual slots does not imply access to their sum.
On an extra native cell h, Q*(u_h+v_h)=1; Lemma Q protects that functional
under P1/P2 even though either individual slot can be read. This does not
construct the required third complementary read or quarter phase.

G2 excludes non-adaptive S under its hypotheses. The displayed shared-cell
arrangement signals. Those facts do not prove that every adaptive or
distributed hidden-sector route is impossible. The forward DESIGN wording
preserves the valid constraints and keeps the uncovered questions open.

The separate [feedback/control result](../quarter-phase-feedback-20261107/RESULT.md)
addresses the combined S+C-CP target under its own explicit linear encoding,
common-lift and translation hypotheses. It does not use the R1 CP recovery.

## 7. Verification and retained limits

This is a hand paper recovery of three bounded written gaps. Root read the
actual native step, R1 frame and Lemma 3 at the source snapshot; the proof
uses their stated conditional scopes. No prior probe count, uncommitted
Choi check, kernel-vacuous predicate or off-main result is a premise.
The symplectic identities and word substitutions are shown above.
No simulation, enumeration, implementation, Lean build, freeze, dispatch,
physical-premise adoption, merge or manuscript change occurred.
Independent review of the exact pushed forward patch is required.
