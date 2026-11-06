# Whole-model bridge for the amplitude/readout extension

**Standing.** Paper-only candidate assessment for #1169, on guiding draft #1173.
The [owner scope](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6693973889)
authorizes one proposed extension, its correspondence and first bridge limitation,
with independent review. Review status is recorded on that PR.
The exact endpoint is `endpoints.md`; it is not narrowed here.
Source snapshot for the retained main corpus:
`f49b768709d262a05471895cec703b31aff19b57`.

**Result.** The first state/readout bridge fails for the candidate specified below.
Its exact point preparations, continuous drive family and public sign sensor give
arbitrarily large finite sets of pairwise perfectly distinguishable preparations.
They have no realization by density states and preparation-independent effects
on any one fixed finite-dimensional quantum carrier. The state encoding may be
nonlinear and need not be the original rank-one dictionary.
This is a hand proof about one added-access extension. It is not a no-go for bare
OI, other preparation/access principles, or finite-menu representations with
growing dimension. B3's restricted conditional instrument result remains valid.

## 1. Candidate extension E-AR

E-AR is the proposed operational closure of the current amplitude-control,
public sign-readout and detector-controlled exchange architecture.
Its admission conditions are the following primitive data and access rules,
specified without reference to equality with quantum probabilities.

| Clause | Independently specified candidate input | Status |
| --- | --- | --- |
| AR-1: carrier | Nonzero real mode pairs `(x,y) in R^2 x R^2`; write `z=x+i y` as coordinates | Added real-carrier idealization, not derived from finite native OI |
| AR-2: drive | `T_k(x,y)=(k X x-y,x)`, `X=[[0,1],[1,0]]`, with exactly loadable `k in [-1,1]`; B1's fixed 24-step words U(theta) are available | The word identities are derived in B1; real coefficients, isolation and control availability are unsourced |
| AR-3: preparation/composition | Prepare `z=e1`, execute a drive as preparation, then execute an independently selected drive on that same carrier | Explicit composition condition under assessment; not inferred from the single-program B1 example |
| AR-4: public sign | Copy `1[x1>0]` reversibly into a fresh zero bit and read that bit after the complete copy | B1's declared sensor, now retained in the common interface; physical source open |
| AR-5: exchange detector | B3's sensor `1[q<abs(z1)^2/norm(z)^2]`, record-controlled exchange with a ready reference, and public record after that coupled operation | Added sensor/coupling/resource conditions; no access to an intermediate copy-only factor is inferred |
| AR-6: resources/access | Keep every physically available record in the correspondence; prepare ready references and independent seeds as stated; provide a common causal reversible controller | The finite witness below is explicit; a compatible realization for all Gate A protocols is not established |

For the B3 benchmark, the two seeds are independent uniform variables in `(0,1)`,
and each reference bank is `(e2,e1)`. The quadratic response and uniform law
are explicit inputs, not a derivation of Born selection. The sign result does
not use either seed or the exchange detector.

The full proposed programme would require extensions of these data to all
objects and protocols in `J_exact(A)`. E-AR does not declare admission by
successful quantum reproduction. Its finite-window instances exist (§2);
nonemptiness of the complete Gate A model class is not claimed. A vacuous
soundness statement over an empty full class would not meet the objective.

## 2. One common finite-window world

Let the signal be z, the references `A_(j,b)` for `j=1,2`, `b=0,1`,
the seeds `q_j`, and record bits `r_j`. Use the same domain of nonzero
carriers as B3. Add 48 real program coefficients, two immutable opcode flags
`c1 in {idle,D1}`, `c2 in {idle,S,D2}`, and a clock in `Z_128`.
Thus one common world is

    (R^4 minus {0})^5 x (0,1)^2 x {0,1}^2
      x [-1,1]^48 x {idle,D1} x {idle,S,D2} x Z_128.

At clocks 0–23 apply the first 24-step drive; at clock 24 apply c1;
at clocks 25–48 apply the second drive; at clock 49 apply c2;
at clocks 50–127 keep these data idle. Every step advances the clock.
S copies `1[Re z1>0]` into r2 by XOR. D1 and D2 are exactly the coupled
maps in `measurement-exchange.md`: XOR the sensor into r_j and exchange
z with `A_(j,r'_j)`, controlled by the output bit. The flags and coefficients
are unchanged. This is one fixed interpreter, not dynamics fitted per history.

Each opcode is bijective on its full stated domain. The inverse of T is
`T_k^{-1}(u,v)=(v,k X v-u)`; S is an involution. For D_j undo the
exchange using its unchanged output bit, then undo the XOR using the restored
old signal. Given the new clock, recover the old clock and opcode and apply
its inverse. This proves global reversibility of the common world map.

The prepared law has point signal e1, references `A_(j,0)=e2`,
`A_(j,1)=e1`, zero records and clock, and fixed independent seed laws.
Only declared program/flag fields change between experiments.
The second drive fields are not consulted before clock 25. Changing its
setting therefore leaves the preparation and all earlier uncontrolled data
and records unchanged. The same operation label uses the same word and sensor.

This world contains B3's two-drive/two-detector protocol in its first 50 steps,
with the same conditional behavior. It also contains the sign subinterface:
take c1=idle and c2=S. The first word is a preparation U(theta); the second
is a test drive U(phi). At the cut just after the idle step at clock 24,
the carrier is prepared independently of phi. At step 50 the sign bit is public
and it persists through the remainder of that first cycle.
No reset or perpetual retention in later cycles is asserted.

The composition and switchable opcode availability are proposed added physical
conditions. The explicit interpreter establishes their mathematical consistency
on this finite window, not availability of this apparatus in native OI.

## 3. Proposed correspondence and necessary bridge

The starting dictionary is `rho(z)=z z*/||z||^2`; a prepared ensemble would
map to its average. This is a proposed mathematical representation.
It supplies no preparation availability or native probability law.

| Native data/procedure | Proposed quantum interpretation | Current extent |
| --- | --- | --- |
| Prepared nonzero z | `rho(z)` | A map, not a proved full operational quotient |
| B1 drive U(theta) | Conjugation by `exp(i theta X)` | Endpoint identity derived in B1; one control family, not all-carrier unitary availability |
| B3 coupled detector under its stated law/resources | Binary basis instrument `rho -> P_b rho P_b` | Conditional one/two-read agreement already assessed; does not settle other accessible sensors |
| Public sign sensor | A preparation-independent quantum effect for each test setting | Fails even if the state encoding is replaced, as below |
| Ancilla joins, arbitrary instruments and adaptive resource family | The full typed operations of Gate A | Not constructed by this finite apparatus |

For the sign subinterface, allow the most general alternative state assignment
on one fixed finite-dimensional carrier. The necessary bridge statement is:

**BR-0(d).** There exist density operators `sigma_theta` on `C^d` and effects
`0 <= F_phi <= I_d`, with one fixed d, such that

    Tr(sigma_theta F_phi) = P_native(r2=1 | prepare theta, test phi)

for every admitted theta and phi. F_phi is independent of the preparation label.
No continuity, affine dependence on theta, rank-one form, injectivity assumption
or unitary representation of the drives is imposed on sigma or F.

This is a necessary test of a fixed typed prepare-and-measure correspondence.
It must represent all preparation-dependent information accessible to this
test in the prepared object. A setting may select the same effect for two
different preparations; the effect cannot consult an extra classical copy of
the preparation label or underlying real coordinates outside that object.
Such an extra input is a different interface, not a realization of BR-0(d).

An independent apparatus state, even one chosen by phi and of larger finite
dimension, does not evade this test: its fixed preparation and quantum
processing pull the final binary outcome back to an effect on the prepared
`C^d` object. Preparation-correlated accessible memory must instead be
included in that object's encoding and dimension. These are type/access
requirements of the bridge, not physical exclusions established for E-AR.

## 4. Native probabilities and the dimension obstruction

B1 derives a fixed 24-step forward word for every real angle:

    U(theta) = exp(i theta X) = cos(theta) I + i sin(theta) X.

All required coefficients lie in `[-1,1]`: reduce theta modulo `2pi`
to `theta_bar in [-pi,pi]`, set `a=-tan(theta_bar/4)`, and use twice
the compensated word with `b=-2a/(1+a^2)`.
This reuses the explicit synthesis in `two-mode-drive.md` §4.
No quantum instrument is assigned to the individual microscopic T steps.

After the preparation, `z_theta=cos(theta)e1+i sin(theta)e2`.
After the test drive, `z=U(phi)U(theta)e1=U(theta+phi)e1`.
The ready bit therefore has the deterministic law

    P_native(r2=1 | theta,phi) = 1[cos(theta+phi)>0].       (1)

This follows from the real-coordinate sensor and fixed point preparation.
There is no Born rule, detector-seed law or preparation-dependent test map
in this calculation.

**Lemma 1 (native separating tests).** For any distinct theta_i < theta_j
in `(-pi/4,pi/4)`, put `delta=theta_j-theta_i` and
`phi_ij=pi/2-(theta_i+theta_j)/2`. Then

    cos(theta_i+phi_ij) =  sin(delta/2) > 0,
    cos(theta_j+phi_ij) = -sin(delta/2) < 0.

The same test phi_ij gives bit 1 certainly for preparation i and bit 0
certainly for preparation j. No threshold tie is involved. The experimenter
may choose a different test for each declared pair, but that test is the same
in the two compared runs; it is not fitted to which member was prepared.
Every such angle has an allowed fixed-duration drive word.

**Lemma 2 (quantum dimension bound).** If density operators rho and sigma
obey `Tr(F rho)=1` and `Tr(F sigma)=0` for an effect `0<=F<=I`,
their supports are orthogonal.
To see this, diagonalize rho on its support. The nonnegative terms in
`Tr((I-F)rho)=0` imply that F acts as identity on every positive-eigenvalue
eigenvector of rho. Similarly `Tr(F sigma)=0` implies that F vanishes
on the support of sigma. The 1 and 0 eigenspaces of the Hermitian F are
orthogonal. Consequently a finite set of N nonzero density operators that
are pairwise perfectly distinguished, even by different binary effects,
has N mutually orthogonal nonzero support subspaces and requires `d>=N`.

**Proposition (BR-0(d) fails for every finite d).**
Choose `N=d+1` distinct angles in `(-pi/4,pi/4)`, for example

    theta_i = -pi/4 + (i+1)pi/(2(N+1)),   i=0,...,N-1.

If BR-0(d) held, Lemma 1 and (1) would supply a perfectly distinguishing
effect for every pair of their encoded states. Lemma 2 would give
`d>=d+1`, a contradiction. No particular state dictionary was used.

For the qubit target the finite three-preparation witness
`theta in {-pi/6,0,pi/6}` already suffices. The corresponding three pair
tests are `7pi/12`, `pi/2` and `5pi/12`; the smallest absolute
tested real coordinate is `sin(pi/12)>0`. This finite strict-sign witness
avoids ambiguity about ties. It is not a claimed noise-tolerance theorem.

The dimension argument is elementary quantum mathematics, not a new general
distinguishability theorem. The application here identifies a stronger
candidate boundary than B1's failure of the specific rank-one dictionary.
Its extra premises are the declared preparation/test composition and complete
sign access in E-AR.

## 5. Controls, scope and attempts to repair the dictionary

- **Original dictionary control:** theta and theta+pi have the same
  rank-one density but can give opposite sign records. B1's I/-I check is
  recovered. The new proof does not assume that these are encoded identically.
- **Finite-menu positive control:** for any finite list of N prepared angles,
  use orthogonal basis states `|i><i|` in `C^N` and the diagonal effects
  `F_phi=diag(1[cos(theta_i+phi)>0])`. They reproduce every sign-test
  probability on that list. Thus the claim is about one fixed finite carrier
  covering the entire admitted preparation family. This control is a table
  representation, not a physical reconstruction or a full dynamic extension.
- **B3 control:** the same common world still gives B3's conditional fixed
  instrument statistics when its detector flags are selected. A successful
  subinterface coexists with the failed full sign interface.
- **Existing positive architecture:** the retained history-architecture-v5
  model has hemisphere responses with restricted cosine-distributed
  preparations and a specified private/non-returning reservoir. It does
  not admit the exact point-preparation orbit of Lemma 1. The present
  obstruction does not refute that conditional positive control.
- **Larger finite encoding:** already covered by arbitrary d. Adding
  preparation-independent helpers does not remove Lemma 2.
- **Changed preparation or access:** finite resolution, noise, restricted
  preparations, loss of sign access, or a different carrier/reference model
  changes a premise of this assessment. Such a physical restriction must
  be sourced independently; this paper neither assumes it nor selects
  a replacement candidate.

Nothing here refutes native OI generally, all possible encodings/target types,
or Main's finite observable-law representation results. Those results can
use a different finite representation for a specified finite experiment
family; Lemma 2 makes the dimension dependence explicit here.
An unrestricted infinite-dimensional or additional classical-label interface
is outside the fixed finite-carrier comparison proved impossible above.

## 6. Both whole-model directions and the existing theorem

A candidate matching the full native interface must first supply a consistent
state/effect correspondence. BR-0 is a weaker necessary fragment of it.
For the candidate retaining this point-preparation/sign subinterface, that
fragment is refuted. There is therefore no complete full-interface witness
with a fixed finite-dimensional prepared object and preparation-independent
test labels. No choice of a larger fixed d repairs this candidate.

The first bridge is thus **refuted under E-AR**, not merely an unproved lemma.
The finite-window world demonstrates a nonvacuous conditional instance of
the primitive/access assumptions. It does not prove that a model already
realizing every preparation and protocol of `J_exact(A)` exists.
If no such full model exists, a universal statement over that empty class
would provide no reconstruction. If a proposed completion retains this
subinterface at a fixed typed object, the same obstruction still applies.

The remaining programme obligations are separate:

| Obligation | What a successful bridge must prove | Status for this candidate |
| --- | --- | --- |
| Forward model correspondence | Every admitted native model's complete observable histories have one compatible quantum interpretation | Blocked already by BR-0 for the retained sign subinterface |
| Matrix/instrument interpretation | Native preparations and branch maps supply the complex-linear interface, valid probabilities and its complete composite scope | Not derived; a coordinate z or an amplitude mixer does not supply these fields |
| Five completion conditions | Composite validity, inert spectators, all-composite unitary control, iterated ancilla closure and system-to-level-one consistency | The existing theorem is available once its interface/premises are established; this candidate has not established them |
| Reverse model correspondence | For every target quantum theory, construct one admissible native model and fixed label interpretation for all target preparations, instruments, composites and histories | No such full construction is provided; the restricted B3 witness is insufficient |
| Common histories/resources | Preparation/setting independence, prefix compatibility, retained records and compatible resource embeddings for arbitrary finite adaptive protocols | The short common interpreter is proved; the unrestricted resource family is open |
| Native physical interpretation | Derive the assumed real carrier, control, preparation, readout and resource rules from independently stated physical principles | UNSOURCED; no assumption is adopted |

`GeneralCarrier.exactAll_iff_physical_general` supplies the existing internal
characterization on `FiniteOperationalTheory`. That structure already has
complex-linear matrix operations, availability, preparation and readout data.
`OperationalAssembly.readout_is_localLuders` derives its readout form from
the stated interface and spectator-independence hypotheses; this paper
does not relabel that derived formal result as a postulate.
Neither internal theorem constructs the native model and both all-history
correspondences requested by Gate A. Reproving them would not remove BR-0.

## 7. Exactness, resources and the next missing physical lemma

The witness uses finitely many real coordinates and bounded clock/record
resources, but its state/program domain is infinite. Exact real loading
is an explicit added condition. It is not a derivation from a single fixed
finite configuration space or a finite controller alphabet.
For each finite d the contradiction has a finite experimental menu;
requiring one interpretation for all admitted preparations is what excludes
a single finite-dimensional bridge. No simulation or limit approximation is
being substituted for the accepted exact endpoint.

The finite interpreter supplies only its declared first-cycle history.
Arbitrary finite adaptive trees, unbounded positive ancilla levels and
compatible resources require a common construction with proved embeddings
and prefix laws. A family chosen independently per experiment is not that
construction. A finite-menu/precision approximation remains a separately
named target, not a replacement for `J_exact(A)`.

The next missing physical statement is an **observer/access quotient lemma**:
derive, from independent physical premises, which preparations and coupled
readouts are available, and why their complete operational state can pass
the required finite-dimensional state/effect test. A quotient must remain
valid under every allowed control and read, including public record and
reservoir procedures. It cannot simply identify states that an available
sensor distinguishes. This is a desired conclusion, not a new admission
axiom stating that the model reproduces quantum probabilities.
For E-AR as currently specified, such a finite-dimensional quotient is
impossible by §4; a future positive route must justify which premise changes.

The accountable dependency is #1169 for the correspondence and candidate
restriction, with #866 for physically sourced observer/coupling/public access.
#1059 retains measure selection, #1147 ready supply, #1032 retention and its
separate cross-read-coherence obligation, and #1143 the distinguishing test.
The sign obstruction uses no detector seed, so selecting a different seed
law alone would not repair it while its point preparations and sign interface
remain available. Better classical retention alone also would not repair it.
No new work on those branches or replacement candidate is commissioned here.

## 8. Evidence and source roles

The new mathematical result is the hand derivation in §§2–4.
The following references state exactly what is reused.

| Source | Role and scope |
| --- | --- |
| `endpoints.md`, §§2–4 | Support in this PR: fixed target, typed labels, same-model/all-history and resource requirements |
| `two-mode-drive.md`, §§2–6 | Support in this PR: T inverse, compensated fixed-duration U(theta), point preparation and sign sensor; composition closure is explicitly added here |
| `measurement-exchange.md`, §§1, 4–8 | Support in this PR: D_j and inverse, finite resources and conditional B3 benchmark; no general native availability inferred |
| `../../../../lean-mathlib/OIBridge/OperationalAssembly.lean`, FiniteOperationalTheory and readout_is_localLuders | Support on main: actual formal interface and the derived readout statement |
| `../../../../lean-mathlib/OIBridge/GeneralCarrier.lean`, exactAll_iff_physical_general | Support on main: existing characterization and its scope |
| `../states-dynamics-audit-20261024/history-architecture-v5/REPORT.md`, fixed preparation cone and public/private contract | Support on main for the retained positive comparison's assumptions; no replay or fresh certification claimed |
| `../../../../../papers/Main.md`, §3.4 | Support on main for the finite-law/full-operational distinction |
| #1169 c.6693973889 | Owner scope provenance, not scientific evidence |

The sibling endpoint/B1/B3 content is not yet on main. It must land with any
authorized landing of a claim that relies on it; keeping a branch or naming a
SHA alone is insufficient under AGENTS.md §A.42. No such landing is authorized
by this paper. The construction and dimension proof are stated here so that
their assumptions and conclusions can be independently checked.

No scientific code, CAS, enumeration, simulation, Lean build, physical experiment,
governed execution or manuscript change is part of this assessment. Ordinary
automatic PR CI is a separate repository check. Neither a physical premise,
a full OI–QM equivalence nor a publication claim is adopted.
