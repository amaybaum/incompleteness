# Selection — the route (ii) program

**Status: program document, working draft (b183; corrected b184 per review —
S5 withdrawn and replaced by the embeddability separation S5′; the S1
identification tightened to the ambient simplex; S2 restated on the actual
operational polytope; the memory-regime identification retracted to the
negative-determinant regime pending a computed $M_t$. Not in the canonical
build set. The selection question itself remains OPEN.**

The target, as fixed in [Main §3.4]'s program Remark: derive from observation
incompleteness, rather than postulate, the hypotheses of an operational
reconstruction theorem — continuous reversible transitivity, local
tomography, and purification with uniqueness up to reversible relabeling of
the purifier — so that the reconstruction theorems (Hardy 2001; Masanes and
Müller 2011; Chiribella, D'Ariano and Perinotti 2011, as cited in [Main
§3.4]) select the quantum operational theory among the representations the
framework proves universal. [Main §3.4] already supplies: finite
dimensionality; reversible dilation; the canonical predictive quotient
theorem (certified: `purification_probes.py`) as a purification-uniqueness
INGREDIENT; and the inventory of what is not yet established.

What this document proves (phase 1, corrected): the operational theory a
finite law generates embeds in the canonical predictive simplex, with
cylinder tests supplying single-system finite tomographic injectivity
unconditionally, the preparation quotient identified, and tail-vertex
reachability characterized (Theorem S1); the operational state space is a
finite polytope whose affine automorphism group is finite, admitting no
nontrivial continuous one-parameter subgroup — so no nontrivial Hardy-type
continuous reversible transitivity between DISTINCT pure states can occur
at an individual finite-law layer, and a selector capable of producing the
quantum pure-state geometry necessarily lives at a
continuum/closure/emergent-limit layer (Lemma S2); a decidable spectral
obstruction excludes classical homogeneous continuous-time Markov-semigroup
embedding and stochastic roots of the law's one-step map (Lemma S3); the
fixed-basis quantum carrier realizes the same map at $t = 1$ of a continuous
one-parameter unitary group with valid marginals at every $t$ (Proposition
S4); together, a classical–quantum embeddability separation under a
symmetric carrier-level requirement (Proposition S5′). What this document
does NOT prove, stated plainly: operational selection in any form. The
b183 Theorem S5 claimed classical exclusion from a bare continuity
requirement; that inference was FALSE — the convex path
$C(t) = (1-t)I + tA$ is a perfectly valid continuous stochastic
interpolation of any stochastic $A$ — and S5 is withdrawn (§6, with the
counter-control now certified in the suite). The selector is not mere
continuity; it is O2's transitive reversible structure, fully open.

All finite claims are certified: `selection_probes.py` (suite 29 of the
foundation battery), including the negative controls.

## 1. The operational theory of a finite law

Fix a finite-horizon visible law $P$ on trajectories $x_{1:K}$ over a finite
alphabet, as in [Main §3.4]'s canonical-quotient theorem, with its tail
object $T(P)$: stage-$t$ states the positive-probability future tails
$\tau \in \mathrm{tails}_t(P)$, dynamics the shift.

**Definition (operational data).** A *preparation* at stage $t$ is a
positive-probability visible prefix $h = x_{1:t}$ (stage 0: the empty
prefix). A *test* is a finite future event; it suffices to take the
*cylinder tests* $E_\tau = \{\text{future} = \tau\}$,
$\tau \in \mathrm{tails}_t(P)$, and their unions. The *statistic* of a
preparation is the conditional law $P(\cdot \mid h)$ on
$\mathrm{tails}_t(P)$. Two preparations are *operationally equivalent* iff
they have the same statistic on all tests. The *operational state space at
stage $t$* is
$$\mathcal{S}_t(P) \;=\; \mathrm{conv}\{\, P(\cdot \mid h) : h \text{ a
positive-probability stage-} t \text{ prefix} \,\},$$
the convex hull of finitely many points of $\Delta(\mathrm{tails}_t)$ —
a finite polytope. A *reversible operational transformation* at stage $t$
is an affine bijection of $\mathcal{S}_t(P)$ onto itself commuting with the
assignment of outcome probabilities and the shift update.

## 2. Theorem S1 (operational translation of the canonical predictive quotient)

**Theorem S1.** *For every finite law $P$ and stage $t$:*

*(i) (ambient identification) $\mathcal{S}_t(P) \hookrightarrow
\Delta(\mathrm{tails}_t)$, every preparation represented by its conditional
future law; the extreme points of the AMBIENT simplex
$\Delta(\mathrm{tails}_t)$ are exactly the point masses on tails — the
states of [Main §3.4]'s canonical predictive quotient $T(P)$ at stage $t$;
and a tail vertex belongs to $\mathcal{S}_t(P)$ iff some
positive-probability prefix makes the future deterministic.*

*(ii) (finite tomographic injectivity, unconditional) the cylinder tests
separate: distinct points of $\Delta(\mathrm{tails}_t)$ — in particular
distinct operational states — assign different probabilities to some
$E_\tau$; the state-to-statistics map is injective, with the separating test
constructive.*

*(iii) (no-redundancy quotient) the quotient of preparations by operational
equivalence is exactly the quotient by equality of conditional laws, and it
embeds injectively in $\Delta(\mathrm{tails}_t)$ by (ii).*

*Proof.* (i) A preparation's statistic is by definition a probability
assignment to the tails, i.e., a point of $\Delta(\mathrm{tails}_t)$;
convexification stays inside the simplex. The extreme points of a finite
simplex are its vertices, here the point masses on individual tails, which
are precisely $T(P)$'s stage-$t$ states. A point mass arises from a prefix
$h$ iff $P(\cdot \mid h)$ is deterministic. (ii) For $m \neq m'$ pick
$\tau$ with $m(\tau) \neq m'(\tau)$; then $E_\tau$ separates, the
probability of $E_\tau$ in state $m$ being $m(\tau)$ itself. (iii)
Operational equivalence is equality of statistics, which by (ii) is
equality in $\Delta(\mathrm{tails}_t)$. $\square$

**What S1 does NOT assert.** In general
$\mathrm{Ext}\,\mathcal{S}_t(P) \neq \mathrm{Ext}\,\Delta(\mathrm{tails}_t)
\cap \mathcal{S}_t(P)$: an extreme point of the reachable operational
polytope can be a MIXED distribution over tails. The immediate example is
already stage 0: with a single (empty) preparation and two equiprobable
tails, $\mathcal{S}_0(P) = \{(\tfrac12, \tfrac12)\}$ — its sole element is
extreme, hence pure in the operational/GPT sense, and its future is not
deterministic. The identification "quotient tails = pure states of the
operational theory" is therefore not claimed; what is proved is the
ambient embedding plus the reachability criterion for tail VERTICES. The
distinction matters exactly where O1/O2 meet reconstruction machinery,
whose axioms (e.g. purification with uniqueness, CDP) are statements about
the operational theory's own pure states. Certified: the suite exhibits
instances with mixed extreme points (`selection_probes.py`, Ext control).

*Remark.* S1 is the operational translation [Main §3.4]'s purification
Remark names as the first remainder, at the single-system level; composites
and LOCAL tomography are obligation O3 — injectivity here is single-system,
full-test.

## 3. Lemma S2 (finite reversibility of the operational polytope)

**Lemma S2.** *For every finite law $P$ and stage $t$, the affine
automorphism group of the operational state polytope $\mathcal{S}_t(P)$ is
finite — an affine bijection of a polytope permutes its finitely many
extreme points and is determined on the polytope's affine hull by that
permutation together with the hull's structure — and therefore admits no
nontrivial continuous one-parameter subgroup: a continuous homomorphism
from $(\mathbb{R}, +)$ to a finite group is constant.*

*Proof.* $\mathcal{S}_t(P)$ is the convex hull of finitely many points,
hence a polytope with finite extreme set $E$. An affine bijection of the
polytope onto itself preserves extremality in both directions, so restricts
to a permutation of $E$; two affine maps agreeing on $E$ agree on
$\mathrm{conv}(E) = \mathcal{S}_t(P)$, and on its affine hull. So
$\mathrm{Aut}_{\mathrm{aff}}(\mathcal{S}_t(P)) \hookrightarrow
\mathrm{Sym}(E)$, a finite group; local constancy of continuous maps into a
discrete group finishes. $\square$

*Remark (where O2 must live).* The consequence is structural, with its
exact qualifier: no NONTRIVIAL Hardy-type continuous reversible transitivity
between DISTINCT pure states can occur at an individual finite-law layer,
because the finite-law operational polytope's reversible group is finite —
while a singleton polytope (the stage-0 example of §2) satisfies continuity
VACUOUSLY, there being no two distinct pure states to connect; the selector
that produces the quantum pure-state geometry is the nontrivial case. So O2, if it holds at
all, is a statement about a continuum/closure/emergent-limit layer of the
operational theory, not about any single finite law — which is exactly
where [Main §3.4]'s finite-test-density architecture already places the
continuum theory: approached by finite realizations, reached by none.

## 4. Lemma S3 (classical homogeneous-Markov embeddability obstruction)

**Lemma S3.** *Let $A$ be a real square matrix. (a) If $\det A < 0$, then
$A$ has no real square root ($\det R^2 = (\det R)^2 \geq 0$); a fortiori a
row-stochastic $A$ with $\det A < 0$ has no stochastic square root and is
not embeddable as $A = e^{Q}$ for any real $Q$ ($\det e^{Q} =
e^{\operatorname{tr} Q} > 0$) — no classical homogeneous continuous-time
Markov-semigroup embedding. (b) The same conclusions hold if $A$ has a
negative real eigenvalue of odd algebraic multiplicity: in the real Jordan
form of a real $R$ or $e^{Q}$, negative real eigenvalues of the square or
exponential arise from conjugate non-real pairs and so carry even
multiplicity. (c) For the two-outcome exemplar class
$A_a = \begin{pmatrix} a & 1-a \\ 1-a & a \end{pmatrix}$ one has
$\det A_a = 2a - 1 < 0$ exactly for $a < \tfrac12$ — the
NEGATIVE-DETERMINANT (flip-dominant) regime.*

*Proof.* As stated in (a) and (b); (c) is direct. $\square$

**Scope, stated exactly.** S3 is an EMBEDDABILITY obstruction: it forbids
semigroup/root structure. It does NOT forbid continuous stochastic paths:

**Counter-control.** For any row-stochastic $A$, the convex path
$C(t) = (1-t)\,I + t\,A$ is a continuous family of valid stochastic
matrices with $C(0) = I$ and $C(1) = A$ — including for every
negative-determinant $A_a$, where $\det C(t)$ crosses zero along the way.
Any argument that would exclude classical carriers from a bare
path-continuity requirement is refuted by this control, which the suite
certifies (`selection_probes.py`). The b183 Theorem S5 made exactly that
inference and is withdrawn (§6).

**On "memory".** No identification of $a < \tfrac12$ with the framework's
memory witness $M_t = I(X_{<t}; X_{t+1} \mid X_t)$ is claimed: a
first-order chain with transition matrix $A_a$ has $M_t = 0$ for every
$a$. Connecting the obstruction regime to a genuinely memory-bearing
multi-time family — a $P_a$ with computed $M_t$ — is future work, listed
under the obligations.

## 5. Proposition S4 (the quantum carrier's continuous interpolation)

**Proposition S4.** *Let $A$ be row-stochastic, realized at the fixed basis
by a unitary: in the unistochastic case $A_{ij} = |\langle j | U | i
\rangle|^2$; in the general case via [Main §3.4]'s ancilla dilation, with
the intermediate marginal written explicitly as*
$$M_{ij}(t) \;=\; \sum_{\alpha} \bigl|\langle j, \alpha \,|\, e^{itH} \,|\,
i, 0 \rangle\bigr|^2, \qquad U = e^{iH} \text{ on system} \otimes
\text{ancilla}.$$
*Then $M(t)$ is a valid row-stochastic matrix for EVERY real $t$, with
$M(1) = A$ and $M(0) = I$: the quantum carrier supplies a continuous
one-parameter GROUP of dynamics at the carrier level whose fixed-basis
marginals are valid at every intermediate time. For the exemplar class,
$U_a = e^{i\theta Y}$ with $\cos^2\theta = a$ exhibits this with no
ancilla. The marginal path is NOT a semigroup — $M(\tfrac12)^2 \neq M(1)$
in general, exhibited in the suite — and is not claimed to be: the
one-parameter-group structure lives at the unitary carrier, the validity
statement at the marginals.*

*Proof.* Unitarity of $e^{itH}$ makes each row of $M(t)$ the squared moduli
of a unit vector's components in the product basis, summed over the ancilla
index: nonnegative, summing to 1. $M(1) = A$ by hypothesis; $M(0) = I$
with the ancilla read in its reference state. The exemplar: direct. $\square$

## 6. Proposition S5′ (classical–quantum embeddability separation) — and the withdrawal of S5

**The b183 Theorem S5 is withdrawn.** Its hypothesis [A2] demanded only "a
continuous family of valid operational evolutions interpolating the
one-step law," which the classical convex path $C(t)$ satisfies for every
stochastic $A$; its proof sentence "a stochastic continuous interpolation
of the one-step map (none exists under the obstruction)" was false; its
conclusion does not follow. The comparison it drew was asymmetric —
semigroup structure demanded classically, path structure accepted
quantumly. What survives, under a SYMMETRIC carrier-level requirement, is:

**Proposition S5′ (embeddability separation).** *Let $A$ be row-stochastic
and satisfy Lemma S3's obstruction (decidable: $\det A < 0$, or an
odd-multiplicity negative real eigenvalue). Consider the DIRECT classical carrier — the
visible simplex itself, canonical preparation and readout, the carrier's
time-one map equal to $A$ — and require a continuous one-parameter GROUP
(reversible) or SEMIGROUP of carrier dynamics with that time-one map. Then
no such classical realization exists — $A = e^{Q}$ is impossible (S3), and
stochastic roots do not exist — while the unitary quantum carrier realizing
the same observable endpoint qualifies, $e^{itH}$ being a
one-parameter group with valid marginals at every $t$ and $M(1) = A$
(S4).*

*Proof.* Immediate from S3 and S4. $\square$

**What S5′ is and is not.** It is a true DIRECT-CARRIER separation: for
obstruction-class laws, direct visible-space classical Markov
embeddability fails while quantum unitary availability holds. Hidden or
enlarged classical carriers — realizations $A = R\,T_1\,E$ with nontrivial
encoding/readout, where $T_1 \neq A$ and $T_{1/2}^2 = T_1$ would not give
$A$ a stochastic root — are a SEPARATE question, not addressed and not
excluded here. It is NOT operational
selection: it does not exclude non-classical non-quantum carriers, does not
supply transitivity, does not touch composites, and the carrier-level
requirement it imposes is itself a modeling choice, not yet derived from
observation incompleteness. The selector remains O2's transitive reversible
structure on the operational theory's pure states — Hardy's axiom, whose
continuity clause is what excludes classical probability theory in the
reconstructions — and O2 is fully open, located by Lemma S2's Remark at
the continuum/limit layer.

## 7. The obligations ledger (all OPEN)

- **O1 (purification role).** Whether quotient-level uniqueness — the
  canonical predictive quotient theorem, [Main §3.4], certified — can play
  the purification axiom's reconstruction role given the certified fiber
  freedom; noting that CDP's axiom concerns the operational theory's own
  pure states, where §2's Ext distinction bites. Status: open.
- **O2 (transitivity — the selector).** Derive, from observation
  incompleteness at the continuum/closure layer (per Lemma S2's Remark,
  the only layer where it can live), a TRANSITIVE continuous reversible
  action on the pure states of the operational theory. Not mere
  continuity — the counter-control — and not one one-parameter family.
  Status: open; hardest, and the one carrying Hardy's selection force.
- **O3 (tomographic locality).** A composite structure for framework
  observers (disjoint visible regions; coupling-graph locality supplies an
  ingredient, [Main §3.1]) under which local statistics determine global
  states. Status: open — S1's injectivity is single-system, full-test.
- **O4 (reconstruction import).** With O1–O3, check the hypothesis set of a
  reconstruction theorem (Hardy; Masanes–Müller; CDP — [Main §3.4]) against
  the operational theory the framework generates, importing the theorem as
  external mathematics with its hypotheses verified, in the manner of the
  arc's Lemma-24.1 discipline. Status: open.
- **O5 (Born exponent).** Downstream of O4 via Gleason-type constraints, as
  [Main §3.4] already notes. Status: open, inherited.
- **O6 (memory linkage, added b184).** Exhibit a multi-time family $P_a$
  with computed memory witness $M_t(P_a) > 0$ whose one-step operational
  maps satisfy S3's obstruction, so that the obstruction regime and a
  certified memory regime are connected by computation rather than by
  name. Status: open.

Nothing above upgrades the corpus's "operational selection remains open"
status; the phase-1 results are the translation (S1), the finite-layer
obstruction with its structural consequence for O2's location (S2), and
the embeddability separation (S3 + S4 = S5′), each labeled at exactly its
strength.

## 8. Certification

`selection_probes.py` (foundation battery, suite 29) certifies, exactly
where exactness is available: (1) S1(i,iii) exhaustively at
$(n_V, |\mathcal{C}_H|) = (2,2), (2,3)$, both priors — 1,488 instances —
support, tail-vertex reachability iff deterministic prefix, and the
no-redundancy quotient; (2) S1(ii) constructively — a separating cylinder
for every distinct pair; (3) the Ext control — exact extreme-point
computation of $\mathcal{S}_t(P)$ (Carathéodory in dimension $\leq 2$)
exhibiting instances whose operational polytope has MIXED extreme points,
certifying §2's non-identification; (4) the STAGED-PROCESS automorphism census — recursively label-preserving,
group-closure verified, orders reported (the b183 census accepted
label-breaking induced maps and is corrected); a structural observation:
this does NOT compute $\mathrm{Aut}_{\mathrm{aff}}(\mathcal{S}_t(P))$,
whose finiteness Lemma S2 establishes by proof, not computation; (5) S3 — determinant and double-negative-spectrum
certificates plus numeric root-search corroboration; (6) the
COUNTER-CONTROL — $C(t)$ verified a valid continuous stochastic path to a
negative-determinant $A$, with the determinant sign change exhibited: S3
forbids roots and semigroups, not paths; (7) S4 — the unitary
interpolation's marginals row-stochastic on a fine $t$-grid, $M(1) = A$,
$M(0) = I$, and $M(\tfrac12)^2 \neq M(1)$ exhibited.
