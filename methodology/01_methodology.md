<!-- methodology/01 — Preamble + §A methodology. Part of the repo methodology set (01–03). §A.x/§B.x labels preserved; §B.2.x markers cite the project's session journal, maintained off-repo. -->

# OI Framework — Master Reference

The audit findings from per-session work (SM Sessions 1-7, GR Sessions 1-4,
Substratum Sessions 1-2, Main, Juno, Complexity, Medicine) are summarized
inline in §A.11 (lessons from completed audits) and §B.3 (prediction status
table).

---

## §0 Orientation — how to use this document

The master reference has three sections at three temporal scales. This repo carries §A (this file) and the current §B state (`02_operational_state.md`, `03_reference_docs.md`); §C and the §B.2 session journal are maintained in the project's private working records, off-repo:

- **§A Methodology** — *stable*. Audit procedure, classification scheme,
 accumulated antipattern lessons. Updates only when methodology learns
 something new (currently 7 manifestations of the QM-emergence-interface
 antipattern documented).

- **§B Operational state** — *current, updates each session that changes
 prediction status*. Per-cluster confidence, prediction status table,
 active research directions, prioritized work plan, applied
 changes.

- **§C Handoff** — *latest session*. Rewritten each major session.
 What just happened, current document versions, recommended next session,
 honest limitations, cold-pickup orientation. Maintained off-repo with the
 session journal.

**Update protocol:**

| Section | Updates when | Last updated |
|---------|--------------|--------------|
| §A | Methodology lesson learned (~rare) | June 4, 2026 (see §A.16–A.17) |
| §B | Prediction status changes, work plan shifts | May 24, 2026 (see §B.2.186–187 (journal, off-repo)) |
| §C | Each major session | May 24, 2026 (maintained off-repo) |

**For cold pickup:** read §C (off-repo) first, then §B.4 (active research directions),
then §B.5 (work plan). §A is reference material — consulted as needed,
not read top-to-bottom.

**For deep work on a specific prediction:** read §B.3 (prediction status
table) for the entry; the audit lessons in §A.11 give context for why
each classification was assigned.

---

# §A METHODOLOGY (stable reference)

## §A.1 Purpose and standard

A reusable procedure for auditing derivation chains in OI framework
documents. Applies to SM.md, Main.md, GR.md, Substratum.md, and any
document making S-class structural prediction claims.

**Standard.** Every prediction labeled S (strictly parameter-free
structural) — and every load-bearing theorem in foundational sections —
must have a derivation chain that walks end-to-end without sketch-grade
links. Predictions that fail this standard get reclassified honestly into
one of: C (conditional structural — depends on a stated open assumption),
L (layered conditional, see §A.2), R (retrodiction — fitted to observation),
P (phenomenological input), M (mass/parameter chain with one input), or E
(uses explicit empirical input).

**Outcome.** A framework whose claims are precisely calibrated to what
has actually been derived versus assumed. The deliverable is *not* "every
gap closed" but "every gap explicitly identified and classified."

## §A.2 Classification scheme

### S/C/L/R/P/M/E — the primary classifications

- **S** — Strictly parameter-free structural prediction. No fitted
 parameters; chain walks end-to-end with all links Solid.
- **C** — Conditional structural. Chain walks modulo a stated open
 assumption (e.g., "conditional on Cond 2"). Empirical match
 unaffected.
- **L** — Layered conditional. Chain walks given Layer 2 inputs;
 closure path is a specific active research direction (e.g., "S → L
 pending Direction 10").
- **R** — Retrodiction. Fitted to observation by construction; cannot
 falsify in the precision-upgrade sense. The structural content lives
 in *what's predicted given the fit* (universality, structure of
 remaining quantities), not in the fitted value.
- **P** — Phenomenological input. A specific quantity is taken from
 experiment because the framework doesn't yet derive it.
- **M** — Mass-chain inheritance. Empirical match given a single
 upstream empirical input (e.g., $m_e, m_\mu$ given $m_\tau$).
- **E** — Explicit empirical input. Some specific input enters the
 chain from experiment (acknowledged honestly).

### The four-layer framing

A separate axis from S/C/L/R/P/M/E. Captures *where in the substratum-
to-emergent stack* a prediction's derivation lives:

- **Layer 0** — Gauge structure (what gauge groups exist, what
 representations, structural constraints from C1-C3).
- **Layer 1** — Structural form (Cabibbo's $1/(\pi\sqrt{2})$, Wolfenstein
 $\sqrt{2/3}$ — pure substratum geometry/representation theory).
- **Layer 2(a)** — Operator-relation structural (e.g., the structural
 form of Cond 2 *given* that the relevant operators exist).
- **Layer 2(b)** — Solution-specific (mixing-angle values within a fixed
 operator structure).
- **Layer 3** — Mass-scale and bijection-specific (the specific values
 of $m_s$, $\mu_c$, $\mu_w$, etc., that pick out which $\varphi$).

Predictions span layers. The §7.6-style table needs both a
classification (S/C/L/...) and a layer assignment for each entry.

### Substratum / emergent / mixed (architectural classification)

Used in Step 5 (architectural review). Every load-bearing element of
a calculation lives in one of three architectural layers:

- **Substratum** — Bijection $(S, \varphi)$ on cubic lattice with
 coupling matrix $M(\mathbf{n}, \hat e_j)$. Predictions: pure
 structural ratios from geometry/representation theory.
- **Emergent** — Unitary QFT after trace-out: induced gauge couplings,
 RG running, Coleman-Weinberg potentials, $Z$-factors. Predictions:
 PT/RG outputs.
- **Mixed** — QFT machinery in derivation, but specific substratum-level
 inputs constrain the output (the most typical case for §7's
 quantitative predictions).

Framework's stated rule: *"group structural, couplings emergent."*

## §A.3 Per-prediction audit procedure (Steps 1-7)

### Step 1 — Identify the derivation chain

Document the chain explicitly as an ordered list of links. Each link is
one of: theorem, definition/convention, computation, identification,
assumption (explicitly flagged), or empirical input.

### Step 2 — Classify each link

- **Solid (✓)** — proved theorem, unambiguous computation, standard
 textbook result, or framework-consistent definition.
- **Documented gap (◯)** — explicitly flagged in the document as an
 open task. No audit action; downstream classifications must reflect.
- **Sketch-grade (⚠)** — presented as derivation but on inspection is:
 a consistency check rather than derivation; an empirical exclusion
 of natural alternatives masquerading as structural selection; a
 "convention" doing load-bearing work; multiple triangulating
 arguments that suggest but don't prove; or an identification
 $X = Y$ without rigorous justification.
- **Hidden gap (✗)** — link requires an input or assumption not flagged.
 Most serious.

### Step 3 — Triage the chain

Chain status = weakest link.

- All Solid or Documented → S classification justified.
- Has Documented gaps → downgrade to C with assumption stated.
- Has Sketch-grade links → at risk; deeper probing required (Step 4-6).
- Has Hidden gaps → classification is wrong; close, document, or
 reclassify.

### Step 4 — Literature search before closure attempts

Before deriving a sketch-grade factor from scratch, **search published
literature** for established derivations in adjacent frameworks.

OI operates in domains (cosmological-horizon entropy displacement,
lattice QFT, etc.) where many results have analogues in published work
by Verlinde, Padmanabhan, Jacobson, Susskind, Panagopoulos, etc.

**Why this matters.** The audit's job is to find honest status, not
reconstruct everything. If a result is established, the honest move is:
1. Cite the established derivation
2. Note what OI adds beyond it (typically: structural grounding for
 assumptions the cited work postulates)
3. Acknowledge published consistency objections to the cited work

**Validated examples:**
- **D12** (1/6 in $a_0 = cH/6$): Verlinde 2016 eq. 1.7 establishes
 $(d-3)/[(d-2)(d-1)] = 1/6$ in $d = 4$. OI adds structural grounding
 via condition C2. Closed via literature.
- **D8** (Cabibbo $1/|q|$ chirality): Mason et al. (HPQCD,
 hep-lat/0209152) "Taste-Changing in Staggered Quarks" establishes
 taste-changing transitions have spinor structure $\gamma_\mu$ +
 $\gamma_{5\mu}$ — both chirality-preserving. Closed via literature.

**When to skip Step 4:** if the gap is genuinely OI-specific (e.g.,
K=1/2 depends on OI's specific taste decomposition), literature
search yields only loose analogues. Proceed to Step 5.

### Step 5 — Framework-architecture review (the QM-emergence-interface antipattern)

**The lesson.** When a residual gap appears in a derivation, the
natural reflex is to look for a structural ratio (representation-
theoretic dimension ratio, group-invariant Casimir, geometric
projection magnitude) parallel to OI's other clean structural
predictions (Koide's $C_2/d^2 = 2/9$, Cabibbo's $1/(\pi\sqrt{2})$,
Wolfenstein's $\sqrt{2/3}$).

**This reflex is sometimes right and sometimes wrong.** The framework
has an architectural classification that determines which residual
gaps should be expected to close to clean structural ratios, and
which shouldn't. Skipping the architectural review costs sessions of
work attempting closures that the framework's own architecture
forbids.

**Why this matters especially for OI.** OI is at the *QM-emergence
interface* — derives QM from a deterministic substratum via
marginalization, rather than presupposing QM as fundamental. Standard-
QFT scaffolding imported into OI calculations carries hidden
assumptions that *presuppose* what OI is trying to derive. The
architectural review catches this.

**Common scaffolding imports and their hidden assumptions:**

- *"Action vs operator" distinction.* Presupposes a path-integral
 measure with that decomposition. In OI, $M_\text{taste}$ is a
 structural feature of $\varphi$'s coupling graph (substratum-level),
 not a path-integral choice.

- *LSZ subtraction.* Presupposes asymptotic states in a Hilbert space
 that's emergent from C1-C3. Whether LSZ factors cleanly through the
 substratum/emergent matching condition is a question, not a default.

- *"Loop kinematic coefficient" (independent of substratum structure).*
 Presupposes coefficient is independent of structure generating the
 loop. In OI, loops live in emergent theory but inherit measure and
 vertex structure from the substratum; the "coefficient" may carry
 substratum dependence invisible from standard-staggered perspective.

- *Renormalization scheme as free choice.* In OI, the matching scale
 $\Sigma$ is a structural feature of chiral condensate formation on
 the substratum lattice, not a renormalization-scheme convenience.

- *Diagrammatic decomposition (e.g., $K = K_T + K_S$).* Presupposes
 individual diagrams are well-defined as separate objects with
 separately-meaningful coefficients. In OI, the substratum/emergent
 layering may force certain decompositions to be only meaningful in
 combination.

- *Chirally-symmetric vacuum for perturbation theory.* Presupposes
 bare-mass perturbative one-loop calculations capture the relevant
 physics. In OI's matching condition $\Pi_{taste}(m_{match}) = \Sigma$,
 the $\Sigma$ enters as a non-perturbative input from chirally-broken
 vacuum (where dynamical mass generation gives $\Sigma \neq 0$ even
 at zero bare mass). Required machinery: staggered chiral
 perturbation theory (SχPT, Aubin-Bernard hep-lat/0308036), not
 standard one-loop lattice PT.

- *Surface-representation-theoretic appearance of derivations.*
 Presupposes that a derivation chain whose visible elements are
 group-theoretic (Casimirs, dimensions, Clebsch-Gordan) is pure-
 substratum. Surface-classification can hide emergent-layer
 ingredients (e.g., EWSB) only visible after explicit identification
 of the perturbation $V$.

- *External-structure-implies-internal-structure for diagrams.*
 Presupposes two diagrams sharing external state structure also share
 internal loop structure. In SχPT, internal structure is constrained
 separately by what the $M_\text{taste}$ insertion selects in the
 loop.

- *Same loop order for parallel contributions.* Presupposes
 contributions appearing at the "same level" in prose share the same
 perturbative order. By Panagopoulos-Spanoudes 2017, the singlet-vs-
 nonsinglet difference in chirally-symmetric staggered first appears
 at *two loops* — meaning $K_T$ is one-loop while $K_S$ is two-loop
 even though they appear together in §7.5 prose.

These are reasonable defaults in standard QFT where QM is fundamental.
They are *hypotheses requiring verification* in OI.

### §A.4 The seven manifestations of the antipattern (case studies)

Each instance refines the methodology by adding a recognizable pattern
for future audits. Documented across May 2026 D10 sessions.

**Manifestation 1 (scaffolding import).** D10 first pass opened by
importing standard staggered PT scaffolding — action vs operator
distinction, LSZ subtraction, $K = K_T + K_S$ as separately-meaningful
coefficients. The "convention ambiguity" appeared real but was an
artifact of the imported scaffolding. Diagnosis: $M_\text{taste}$ in
OI is substratum-level structural feature, not a path-integral choice.

**Manifestation 2 (structural-ratio reflex).** After scaffolding was
diagnosed, hypothesis tested: $K = \dim(\hat h)/\dim(E) = 1/2$ as a
pure substratum ratio, by analogy to §7.1 Wolfenstein A. Architectural
review: §7.5 is *mixed-layer* (Coleman-Weinberg + $Z_S$ running),
while §7.1 is *pure substratum*. The structural closure analogue
was wrong; right closure is explicit lattice PT with substratum
inputs.

**Manifestation 3 (chirally-symmetric vs broken vacuum).** Session 2
attempt: explicit one-loop staggered BZ integral. Numerical result
gave $I_A \sim m^2$ at small $m$, meaning $m \cdot I_A \to 0$
cubically — the $\Sigma/m$ IR-divergent structure of §7.5's matching
condition was *not present* in the perturbative calculation.
Diagnosis: §7.5's matching works in chirally-broken vacuum (where
$\Sigma \neq 0$ from dynamical mass generation), while Session 2 was
in chirally-symmetric vacuum. Required machinery: SχPT, not standard
one-loop lattice PT.

**Manifestation 4 (surface-classification trap).** D11 Session 1:
initial Step 5 review classified as "presumptively pure substratum"
because §7.2's derivation chain *looks* representation-theoretic —
Koide angle from $C_2/d^2$, square-root scaling from QM amplitude-vs-
eigenvalue. Closer inspection: the actual asymmetry between $m_u$
and $m_d$ comes from electroweak symmetry breaking — the Higgs VEV
$\langle\Phi\rangle = (0, v/\sqrt{2})$ selects a preferred direction
in $E$. EWSB is *emergent-layer machinery*. D11 reclassified as
mixed-layer, structurally analogous to D10.

**Manifestation 5 (external-vs-internal structure conflation).** D10
Specification Session B: hypothesis that $K_S/K_T$ might be a pure
cubic-group ratio if both calculations share the same pion-loop
integrand. Verification: walking through the SχPT diagrams revealed
$K_T$'s tadpole loop sums over all pion taste channels (no internal
selection), while $K_S$'s self-energy loop is restricted to $T_2$
taste channels (selected by $M_\text{taste}$ insertion). Different
internal structure even with same external structure.

**Manifestation 6 (single-named-gate vs multi-parameter gating chain).**
After spec sessions named D10's closure gate as the pion decay
constant $f$, a follow-up session extracted $f$ online (quenched
$L=8$, GMOR, ~10 minutes compute) giving $f = 0.30 \pm 0.01$. The
$K_S$ calculation then ran with measured $f$ as input — and gave
$K_S = 5\times 10^{-4}$ disagreeing with empirical $7\times 10^{-3}$
by factor ~14. The "named gate" framing was incomplete; actual
gating chain has multiple parameters: (1) $f$ extracted ✓; (2) SχPT-to-
staggered measure factor $\mathcal{N}$ (guessed, off by ~14×); (3)
cubic-group structural coefficient $c_S$; (4) production-grade $f$
vs test-bed quenched $f$; (5) higher-order SχPT corrections.

**Manifestation 7 (implicit loop-order assumption — the deepest layer).**
After decomposing the factor-14 disagreement into 6.5 (calibration) ×
2.2 (structural ratio), literature search revealed
**Panagopoulos-Spanoudes 2017 (1709.10447):** the difference between
$Z_S^\text{singlet}$ and $Z_S^\text{nonsinglet}$ in chirally-symmetric
lattice regularizations (including staggered) **first appears at two
loops, not one**. At one loop, $Z_S^\text{singlet} =
Z_S^\text{nonsinglet}$ identically. So $K_S$ is fundamentally a
two-loop effect. The factor-14 disagreement was the wrong loop order
entirely. Closure path: 10+ hours of careful diagrammatic work with
symbolic algebra (Mathematica/FORM), beyond chat-session scope.

**Manifestation 8 (group-theoretic surface masking bijection-specific
operator alignment).** Cond 2 Step 5 review: the relation
$b_{23} = (4/3)(b_{12}+b_{13})$ has the surface form of a Layer 2(a)
group-theoretic relation — the geometric reading $4/3 = 2A^2$ uses
$A = \sqrt{2/3}$ (a verified Layer 1 substratum quantity from cubic-
lattice Brillouin geometry, §7.1) and decomposes as "partner-count ×
per-partner projection." Surface-classification suggests Layer 2(a):
forced by cubic-group representation theory.

Step-5-style architectural review with explicit operator counting on
$\Lambda^2(T_1) \otimes \Lambda^2(T_1) \to T_2$ (the channel feeding
the off-diagonal $A_2$ corrections) showed: the off-diagonals
$(m_{12}^{(2)}, m_{13}^{(2)}, m_{23}^{(2)})$ form a single $T_2$ irrep
of $O$, but the $T_2$ direction is determined by the substrate's
*specific Yukawa structure*, not by $O$-invariance alone. The natural
Higgs-democratic spurion direction $\xi_h \propto (1,1,1)$ does *not*
satisfy the relation — it produces $b_{12}^\text{sub}: b_{13}^\text{sub}:
b_{23}^\text{sub}$ ratios incompatible with the observed values.

So Cond 2 is **not forced by representation theory + Higgs democratic
direction**. The empirical match indicates the cubic-lattice substrate
has additional structure that picks out a specific $T_2$ direction,
but identifying that structure requires explicit cubic-lattice
Yukawa analysis — bijection-dependent, not pure rep theory.

The antipattern: **a clean rational ratio decomposed in terms of a
known structural quantity ($4/3 = 2A^2$) looks Layer 2(a), but the
load-bearing claim is the operator alignment / factorization, which
is bijection-specific.** Distinct from Manifestation 4 (surface-form
trap on a discrete count) in that the ratio here is not even
discrete-count — it's a numerical coincidence between two real
quantities ($4/3$ from the relation, $2A^2$ from projection geometry)
that happen to match. Distinct from Manifestation 5 (external-vs-
internal conflation) in that the relevant external scaffold is
"natural EFT operator counting" which is in fact internal to the
substrate analysis.

Closure path: Cond 2 cannot be promoted to Layer 2(a) by rep-theory
arguments alone; explicit cubic-lattice Yukawa structure analysis
required. Pre-registered work targeting Layer 2(a) closure should
expect the demote outcome and budget accordingly.

**The cumulative lesson.** Each instance refines the methodology. The
antipattern's root cause: importing QM-as-fundamental defaults into a
QM-emergent framework without checking architectural mapping. Catching
any one early helps catch others. Default to OI-internal vocabulary
(substratum, emergent, trace-out, marginalization, $M_\text{taste}$
as coupling structure) before reaching for standard-QFT vocabulary.

Manifestation 8 adds: when a structural-looking ratio decomposes
neatly in terms of a verified Layer 1 quantity, check whether the
decomposition is forced by representation theory or relies on an
operator-alignment assumption. If the latter, it is bijection-specific
(Layer 2(b)) until explicitly derived from substrate structure.

**Manifestation 8 instances confirmed:**
- Cond 2 (PMNS sum rule, §B.2.2): same-bijection-alignment hypothesis
 on $T_2$ direction. Demoted to Layer 2(b).
- D11 ($m_u/m_d = \sqrt{\theta_0}$, §B.2.3): same-perturbation
 hypothesis on amplitude-vs-eigenvalue PT scaling. Demoted to Layer
 2(b). Operator counting showed four independent Wilson coefficients
 controlling the ratio.

**Manifestation 8 systematic scan completed (§B.2.4):** All S- and
L-class predictions in §B.3 checked against the four-feature
signature. Zero new instances confirmed. One initially flagged
($\sin^2\theta_{13}$) subsequently cleared via the structural
identity $A^2 = C_2/d$ for vector reps. One borderline item
($\theta_0$ bandwidth-squared scaling) has Manifestation 4
character (not 8); empirical match (0.02%) supports retention as
Layer 1 pending first-principles derivation. Conclusion: the two
confirmed instances are isolated, not part of a broader pattern
affecting many predictions.

The pattern: clean ratio + verified Layer 1 decomposition + same-X
hypothesis + bijection-specific alignment. When all four are present,
default expectation should be Layer 2(b), not Layer 2(a). Layer 2(a)
promotion requires explicit substrate-level derivation showing the
alignment is forced.

**Diagnostic tool from the scan: $A^2 = C_2/d$ structural identity.**
For the vector rep of any rotation group, $C_2 = d-1$, hence
$C_2/d = (d-1)/d = 1 - 1/d = A^2$ (off-democratic projection
squared). Ratios of the form $C_2/d$, $C_2/d^2$, $\sqrt{C_2}/d$ in
single-amplitude contexts are structural; ratios that relate
independent operators or transfer between sectors are bijection-
specific until proven otherwise. Use this identity when scanning
future predictions for Manifestation 8 character.

**Two-layer conflation diagnostic (§B.2.6).**
When a derivation invokes "the same X" applied across different
layers (spatial/internal, structural/effective, etc.), check whether
X is well-defined at both layers. Example: D11's "same Casimir
$C_2 = 2$ in different channels" invokes $C_2(T_1)$ at *spatial*
layer (well-defined via $T_1 \subset SO(3)$ with $C_2 = l(l+1) = 2$)
and at *internal* layer (where $E$ rep doesn't lift to SO(3) and
$C_2$ doesn't have the same meaning). This conflation is a
sub-pattern of Manifestation 8.

**Hidden-gem prioritization (user directive, May 6, 2026).**
When investigating unknowns, frame as "what does this reveal?" not
"does this close?" Closure attempts that produce structural
understanding without binary closure are positive outcomes; the
methodology refinement is value. See §B.2.7 for full diagnostic
checklist. Sub-classifications of Layer 2(b) by mechanism:
*single-parameter direction selection* (D11), *multi-parameter
operator alignment* (Cond 2), *cross-layer transfer* (any
spatial↔internal). Algebraic re-expression of predictions in
Layer 1 constants is necessary but not sufficient for promotion;
verify constants enter via their structural mechanisms.

**Rigor-level methodology (§B.2.10).**
Closure investigations should produce their proof rigor level
explicitly. Three levels: Level 1 (verified at explicit equation
chain, referee-ready), Level 2 (verified up to standard moves of
the field, acceptable from established researchers), Level 3
(sketch identifying right approach, *not closure*). When claiming
closure on a multi-part theorem, state rigor level for each part —
they may differ. Default to honesty: assertion at Level 3 should
not be labeled "closed."

**Algebraic-identification verification rule.** When claiming
operator $X$ in one structure corresponds to operator $Y$ in
another, verify the algebra explicitly (commutators/anti-
commutators distinguishing $Y$ from similar operators) AND verify
matrix structure (diagonal vs off-diagonal action patterns).
"$X$ and $Y$ both square to 1 and anticommute with $Z$" is
necessary but not sufficient. Origin of the rule: §B.2.9 initial
claim mis-identified $\gamma_0$ where $\gamma_5$ is correct;
both satisfy anticommutator with $\gamma_i$ and square to 1, but
matrix structure (diagonal-with-opposite-signs vs off-diagonal)
distinguishes them.

**Scope-overstatement diagnostic (added §B.2.12).** *"Not
chat-tractable" framings are themselves overstatements that hide
closeable components.* Apply rigor-level decomposition before
declaring scope. Origin: §B.2.8 framed gap (i) as "not chat-
tractable, requires explicit substratum measure analysis." §B.2.12
revealed that gap (i) parts (a)-(d) are Level 2 closeable via
pseudofermion correspondence; only the cycle-ergodicity component
(part e) is genuinely Level 3. The "not chat-tractable" framing
caused gap (i) to be deferred indefinitely when most of it could
have been addressed earlier.

**Pattern across the audit sessions.** Methodology caught
five overstatements: §B.2.9 Gem E (algebraic misidentification),
§B.2.8 Gem B (closure-completeness overstatement), §B.2.11
(application of Gem B correction), §B.2.12 ("not chat-tractable"
scope overstatement), §B.2.14 (cycle-ergodicity "typical chaotic
dynamics" framing for strictly-linear substratum). All five
corrections strengthened the framework's claims by being honest
about rigor levels and scope. Apply rigor-level decomposition +
scope-overstatement diagnostic to *every* closure claim before
treating it as final.

**Layer 2(b) sub-classification refinement (added §B.2.14, May 6,
2026).** Layer 2(b) coefficient values are *discretization-
determined*, not Wilson-coefficient-style free. The bijection space
is parametrized by discretization-scheme choices (field
quantization, lattice size, timestep, boundary conditions, rounding
rule), not by abstract permutation freedom. Once discretization is
fixed within the framework's constrained class (linear dynamics +
T-invariance + P-indivisibility), the bijection is almost unique.
**Implication:** different Layer 2(b) coefficients (Cond 2
alignment, D11 mechanism, D10 K-value, $\delta_0$) are functions of
the *same* discretization choices, not independent. Cross-prediction
consistency tests are therefore possible — fitting one Layer 2(b)
value constrains the others. This sharpens Layer 2(b) interpretation
beyond the prior §B.2.6/§B.2.7 mechanism sub-classification (single-
parameter direction selection / multi-parameter operator alignment /
cross-layer transfer).

**Cross-prediction consistency tests (§B.2.15).**
The discretization-determined nature of Layer 2(b) values
(§B.2.14 Gem K) implies cross-prediction consistency. Investigation
shows this holds *within structural clusters* but not *across
clusters*: predictions sharing the same representation-theoretic
content (e.g., all derived from cubic-group $T_1$-Casimir $C_2 = 2$)
are mutually constrained, while predictions in distinct sectors
(e.g., U(1) threshold $\delta_0$ vs cubic-group $T_2$ direction
Cond 2) are not directly constrained by each other.

**Gem L:** the framework's cubic-group $T_1$-Casimir structure has
already passed a non-trivial five-prediction cross-consistency test:
Wolfenstein $A$, $\sin^2\theta_{13}$, Koide $\theta_0$, $m_u/m_d$,
and PMNS sum rule (Cond 2's $4/3$ factor) all derive from $A^2 =
C_2/d = (d-1)/d$ on $d = 3$ lattice. All five match observation at
sub-percent or sub-σ level simultaneously. Probability of accident
is small under any reasonable correlation assumption. This is
*one* successful test of cubic-group structure with five observables,
not five independent successes — a methodologically sharper framing
of the framework's empirical track record.

**Gem M (extension):** $|V_{cb}| = A\lambda^2$ extends the cluster
from 5 to 6 simultaneous matches (0.4σ). Cluster-coherence one
observable broader than §B.2.15 articulated.

**Gem N (refinement):** The framework's empirical case rests on *two*
independent Layer 1 structural ingredients passing simultaneous tests:
(1) Cabibbo $\lambda = 1/(\pi\sqrt 2)$ from BZ geometry — tested via
$\lambda$ direct, $|V_{cb}|$, $\sin^2\theta_{13}$, $m_d/m_s$;
(2) Cubic-group $T_1$-Casimir $C_2/d = 2/3$ — tested via 6 cluster
members per Gem M. Cleaner articulation than "many predictions, all
match" — it's two structural tests, each with multiple observables,
all simultaneously matching.

**D10 $K = 1/2$:** Mixed Manifestation 4 + 8 character; offline
closure path retained. Two-loop SχPT computation can produce useful
data either way (Layer 2(a) verification or Layer 2(b) calibration);
the Manifestation 8 risk is communicated to the collaborator via the
Part B specification.

**Session-fatigue / diminishing-returns conflation diagnostic (added
May 7, 2026).** Saturation conclusions formed at the close of long
investigation arcs may reflect either genuine diminishing returns in
the line of work or fatigue degrading the assessing voice's
calibration; the two look identical at session-close and should not
be conflated. By the end of a long arc, working context is loaded
with the arc's cumulative refinements — new findings get
pattern-matched against the bar set by earlier wins in the same arc
rather than judged on absolute structural value. This degrades
calibration in two ways: (1) the overall arc gets logged as
saturating when it may not be; (2) individual findings get logged at
lower severity than their absolute structural impact warrants. The
§B.2.17 conclusion ("diminishing-novelty pattern continues") was the
originating instance, and §B.2.15's Gem L (cubic-group six-prediction
simultaneous-match consistency test) was the under-rated finding
within it — load-bearing in absolute terms, logged "modest" because
Gem K from §B.2.14 had reset the recent-novelty bar.

*Continuity is the default; fresh context is the surgical tool.*
Loaded context is itself substantive value — the arc's working
state, named gems, derivation threads, and current framings are
difficult to reconstruct from documents alone. Routinely discarding
context to "refresh" trades fatigue cost for reconstruction cost,
and the latter is typically larger. The diagnostic targets
*calibration claims specifically*, not all session work. Continue
in the same session for technical derivations, structural
decompositions, calculations, and content-additive work — these
benefit from loaded context and are not the failure mode the
diagnostic addresses. Pause for fresh context when the load-bearing
output is a saturation/novelty/severity *assessment* —
arc-saturation claims, individual-finding tier ratings, work-plan
pivots that hinge on "this line is exhausted." Those are the
calibration outputs the diagnostic protects.

*Operational rule:* treat saturation framings produced at
session-close as provisional pending fresh-context confirmation;
re-read "modest"-tier findings on fresh context before treating
their assessment as final; propagate calibration upgrades to
downstream artifacts (§B.3 entries, framework-document edits, §C
handoff narrative). Genuine diminishing returns survive the
fresh-context re-read; fatigue artifacts do not. The diagnostic
does not forbid saturation conclusions — it requires that they be
confirmed rather than asserted, and it does not force session
interruption when calibration is not the load-bearing concern.

**Within-line vs across-line generalization .**
Saturation in one investigation line is weak evidence about other
lines that work different machinery. §B.2.14–§B.2.17 worked the
bijection-characterization neighborhood (§B.8.1 + §B.8.7 share
substrate-class machinery); apparent saturation there is essentially
mute on §B.8.2 (holography), §B.8.3 (Lorentz emergence), §B.8.4
(cosmology beyond MOND), §B.8.5 (specific predictions framework
could make but doesn't), §B.8.6 (positioning), and §B.8.8 (math
characterization). When pivoting between §B.8 items, or between any
structurally-distinct investigation lines, treat each line's
saturation status as independent. The "diminishing returns across
§B.8" inference would require investigating multiple §B.8 items with
different machinery and seeing low novelty on each — not the same
neighborhood across two adjacent sessions. *Heuristic:* before
generalizing a saturation conclusion, identify the specific machinery
the recent investigations shared and check whether the next candidate
line shares it.

**Convergence-vs-saturation diagnostic .** A
§B.8 (or similar) investigation line *converges* when its original
question targets have been answered at honestly-stated rigor levels
and remaining gaps are explicitly classified — not when the
assessing voice judges that "no more is coming." Convergence and
saturation are different stopping criteria and should not be
conflated; the saturation diagnostic guards against premature stops
mid-flight, while the convergence diagnostic guards against
terminating without producing the deliverables the line was opened
for.

*Convergence checklist:*

1. The §B.8 entry's listed open questions have explicit answers
 with rigor levels per §B.2.10 (Level 1 / 2 / 3 stated; "we
 addressed it" without a level is *failed convergence*).
2. Every open thread surfaced during the investigation is either
 resolved, named as a follow-up task with a specific closure path
 (added to §B.4 if material, otherwise documented in the §B.2.x
 entry), or explicitly flagged as out-of-chat-scope.
3. Findings carry provisional severity ratings flagged for
 fresh-context confirmation per §A.4 mis-ranking diagnostic.
4. The §B.2.x entry states what was investigated, what was found,
 what remains, and whether the line is closed-for-now vs paused-
 pending-other-work.

*Origin (§B.2.18).* §B.8.3 (Lorentz emergence and
corrections) opened with five listed questions; investigation
produced F1 (mechanism), F2 (operator structure), F3 (UHECR
phenomenology) plus two F3-internal resolution closures (Maccione
exception via constituent-quark inheritance dominance; traceless
anisotropy protecting the GZK-cutoff shift at leading order).
Convergence reached when all five §B.8.3 questions had explicit
answers, F3 had three resolution paths classified (two closed at
Level 1-2, one out-of-chat-scope and named in §B.4), and candidate
gems R, S were flagged for fresh-context severity confirmation.

*Distinction from §B.2.17.* The saturation framing in §B.2.17
*failed convergence* — open questions remained (selection problem
"reframed" without a derivation path; cycle ergodicity flagged but
its rigor level not stated) but the line stopped on a vibes-based
"diminishing returns" judgment. The convergence diagnostic would
have caught the gap. The §B.2.17 reassessment now appropriately
flags both calibration failures (saturation) and procedural
failures (convergence) as session-close artifacts.

*Relationship to saturation diagnostic.* Saturation says "this
line is producing diminishing returns, pivot." Convergence says
"this line has produced its deliverables, document and close."
The two are independent and both should be checked: a line can
saturate before converging (premature stop, gap-leaving — the
§B.2.17 failure mode) or converge without saturating (more findings
possible, but the original target is met — appropriate to document
and pivot anyway). Session-fatigue affects saturation judgments
specifically; convergence is more procedural and less calibration-
dependent — the checklist either passes or it doesn't.

*Pattern observed, one instance.* §B.8.3 followed the sequence:
open question → initial findings of mixed rigor → external
phenomenological cross-check produced apparent tension → resolution
paths identified and ranked by tractability → in-scope paths
pursued sequentially to convergence. The tension-then-structural-
resolution character (F3's Maccione exception and traceless-
anisotropy protections both being structural rather than
coincidental) is consistent with the framework being mostly right
and apparent tensions arising from naive coefficient estimates
rather than genuine problems. **One instance is weak evidence —
flag the pattern but do not generalize until §B.8.2, §B.8.4, or
similar lines have been run and either confirm or break it.**

### Step 5 summary protocol

When approaching a residual gap:

1. *Scaffolding audit first.* Identify external scaffolding being
 imported (action/operator, LSZ, diagrammatic decompositions, scheme
 conventions). For each: does it presuppose QM-as-fundamental? If yes,
 classify as hypothesis to verify.

2. *Architectural classification.* Substratum, emergent, or mixed?
 Examine the derivation chain for QFT machinery (loops, RG,
 condensates, fermion determinants).

3. *If substratum:* structural-closure attempts well-motivated.

4. *If emergent or mixed:* structural-closure attempts low-probability.
 Right path is explicit calculation respecting the architecture, with
 substratum data feeding emergent machinery. Analogues from
 substratum-level predictions (Koide, Cabibbo, Wolfenstein) should
 not be expected to transfer.

5. *Track loop order explicitly.* "At what loop order does this
 contribution first appear?" — distinct from architectural layer and
 from EFT framework choice.

6. *Steps 4 and 5 are both prerequisites to closure attempts.*
 Literature search asks "is the answer already published?";
 architecture review asks "what kind of answer should we be looking
 for, and what scaffolding is being silently assumed?"

### Step 6 — Probe sketch-grade links

For each sketch-grade link, attempt:

(a) *Promote to Solid.* Provide rigorous derivation. If literature
 search (Step 4) found established derivation, straightforward.

(b) *Demote to Documented.* Acknowledge gap explicitly. Downstream
 prediction becomes C-class.

(c) *Demote to Hidden-gap.* Neither (a) nor (b) possible — link is
 broken. Classification must change.

The choice depends on actual content, not preference. The audit's job
is honest answer, not preserving desired classification.

### "Park with named gap" — the precise demote

Demote-to-Documented outcomes vary substantially in epistemic
precision. *Vague demote* ("requires explicit OI computation") differs
qualitatively from *precise demote* ("requires extension of MC code to
extract pion decay constant $f$, which is a standard chiral PT
observable not currently measured in OI MC infrastructure"). Both are
technically Documented gaps but precise demote is genuine framework
progress: identifies which specific framework input/measurement is the
gate to closure, gives clear handoff target, provides actionable
extension path.

The diagnostic typically sharpens in layered fashion:

| Layer | Diagnostic state | Example (D10) |
|-------|------------------|---------------|
| Empirical only | "X residual ≲ Y" | "$K_S \lesssim 0.01$" |
| Architectural | "X at substratum/emergent interface" | "$K_S$ at the interface" |
| Framework | "X requires EFT extension Z" | "Requires SχPT" |
| Specific input | "X requires LEC W not currently extracted" | "Requires pion $f$" |
| **Running pipeline** | **"X computed; disagrees by factor F"** | **"$K_S^\text{pred} = 5\times 10^{-4}$ vs $7\times 10^{-3}$ empirical; factor ~14 missing"** |
| **Loop order** | **"X is loop order $n$, not order $m$"** | **"$K_S$ is two-loop (PS 2017)"** |

Each layer is cumulatively sharper. "Running pipeline" and "loop order"
are qualitatively distinct: the disagreement itself becomes diagnostic.

### The offline-C closure track (for mixed-layer/emergent gaps)

When Step 5 classifies a link as mixed-layer or emergent, (a)-promotion
may exceed chat-session scope. Closure path:

1. *Algorithm specification in chat session(s).* Complete bounded spec
 of what the C code needs to compute — data structures, integration
 scheme, BZ discretization, mass-insertion structure, output
 extraction, cross-checks.

2. *C code generation in chat session.* Self-contained C ready to
 compile and run.

3. *Offline (or online-batched) execution.* User compiles, runs.

4. *Result interpretation in chat session.* Analyze C output, extract
 coefficient with error bars, cross-check, propagate to documents.

**Online compute scope is wider than first estimates suggest.** Each
$(L, m, N_\text{configs})$ measurement is independent and decomposable.
Per-session compute budget can typically accommodate 5-30 batches at
$L=8-24$. The offline package is genuinely required only for $L=32+$
production runs at small mass.

**Adaptive batching benefit.** Online path can stop measuring as soon
as the diagnostic stabilizes. Offline path runs every measurement
specified in advance. Adaptive saves both compute and chat-session
time.

### Step 7 — Update prediction's classification

Based on chain's audit outcome:

- All Solid → keep S
- One or more Documented gaps → C, state assumption
- Promoted sketch-grade links → keep S, document promotion
- Unresolved sketch-grade or Hidden gaps → C/L/R/P/E as appropriate

## §A.5 Document-level audit procedure

### Catalog → Triage → Cross-cutting → Closure → Document

1. **Catalog all S-class claims.** Build flat list = audit worklist.

2. **Triage by expected difficulty.**
 - *Quick (~30 min):* Simple chains, well-known results.
 - *Medium (~1-2 hrs):* Multi-step chains requiring careful reading.
 - *Deep (~session+):* Non-trivial computation or likely sketch-grade.

3. **Cross-cutting analysis.**
 - *Shared inputs:* multiple predictions deriving from same claim.
 - *Shared methodology:* same derivation template (e.g., "structural
 identification + Coleman-Weinberg matching + empirical exclusion").
 - *Layer assignment:* apply four-layer framing consistently.

4. **Closure decisions.**
 - *Close it now:* provide missing derivation. 1-N sessions.
 - *Reclassify and document:* update classification + text. <1 session.
 - *Defer with explicit acknowledgment:* add to open-tasks list with
 provenance. <0.5 session.

5. **Document the audit.** Machine-readable record format (YAML in
 per-session audit document):

```yaml
prediction:
 name: sin²θ_12
 document: SM.md
 section: §7.3
 formula: 1/3 - 1/(4π²)
 value: 0.30798
 observation: 0.3085 ± 0.0073 (post-JUNO global fit)
 match: 0.07σ
original_classification: S
derivation_chain:
 - link_1: { claim, type, source, status }
 -...
audit_outcome: Conditional on link_4
revised_classification: C
closure_decision: Defer — Direction 6 / Direction 1 are closure paths
action_items: [...]
```

## §A.6 Cross-document considerations

### Dependency graph (current understanding)

```
 Main.md ──── (uses area-law lemma from SM §3.1)
 │
 ▼
 SM.md ──┬──→ Substratum.md (reconstruction theorem takes SM as input)
 │
 ├──→ GR.md (independent of SM derivation chain)
 │
 └──→ Juno.md (heavy dependency on §4.7, §7.1, §7.3)

 Complexity.pdf ←── SM (A·B derivation)
 Explainer / Medicine / README ←── all (derivative)
```

### Audit ordering (final, per scope-check)

Juno → Main → **SM → GR → Substratum** → derivatives.

The "SM before Substratum" ordering reflects: Substratum's
reconstruction theorem takes SM's results as input; the area-law lemma
is housed in SM §3.1 (resolves the Main → Substratum dependency
identified in the Main audit).

**Dependency structure is itself an audit finding**, not a precondition.
Each audit refines the dependency graph.

### Cross-document coherence check

After all primary documents are audited:

- Every claim in derivative document is supported by an audited claim
 in a primary document, with consistent classification.
- §7.6-style summary tables across documents use the same S/C/L/R/P/M/E
 consistently.
- Four-layer framing applied consistently.
- Open tasks listed in one canonical place (this document §B.4 / §B.5).
- **A status/claim edit is not complete until it is propagated corpus-wide.** Any change to a claim,
 its classification (status/layer/tier; "theorem/derived/forced/open/hypothesis/conditional"), or a
 numeric value must be grepped across *every* document (all papers `.md/.tex`, book chapters, `FULL.md`,
 and derivatives) and mirrored everywhere it recurs — abstracts, bodies, §9-style conclusions, summary
 tables, and the book mirror. See the procedure in **§A.25**.

## §A.7 Standards for promotion

A sketch-grade link is promoted to Solid when the audit produces:

- A *self-contained derivation* of the link's claim, written in the
 document with full notation
- Derivation is *uniquely determined* by structural inputs (no hidden
 choices that could have gone the other way)
- Independent *consistency checks* ruling out alternative conclusions
- Optionally: *external corroboration*

**Empirical exclusion of natural alternatives** (e.g., "$K = 1/2$ is
the only fraction in $\{1/4, 1/2, 1, 2\}$ compatible with observation")
is *not* promotion. It's evidence in favor but not derivation.

**Conventions doing load-bearing work:** if a "convention" is doing
load-bearing work, the link is sketch-grade regardless of how natural
the convention seems.

## §A.8 Honest assessment of audit scope

### What the audit achieves
- Precise classification of every claim
- Explicit list of open tasks with provenance
- Framework whose stated confidence matches actual derivation status
- Robust foundation for external scrutiny

### What the audit does not achieve
- Does not close gaps requiring new research (identifies, classifies,
 worklist)
- Does not eliminate need for ongoing scrutiny
- Does not change empirical status (a 0.07σ-matching C-class prediction
 is still empirically successful)

### Calibration of expectations

A comprehensive audit of OI's scope is expected to find:
- ~10-20% of S-class predictions audit to S unchanged
- ~30-50% audit to S after promotion of sketch-grade links
- ~20-30% downgrade to C/L (conditional/layered, with explicit open
 assumptions)
- ~5-15% downgrade to R/P (retrodiction or phenomenological)
- ~5-10% require substantive paper modifications

These numbers are rough priors. An audit ending with "everything
audits to S unchanged" is implausible for a framework of this scope —
and an audit ending with "most things downgrade" doesn't mean the
framework is wrong, only that its claims were over-stated.

## §A.9 Versioning and re-audit cadence

- Every framework version increment (1.9.1 → 1.9.5 → 2.0.0) includes
 audit-status update.
- Each new quantitative claim audited at introduction, not after-the-fact.
- Open tasks reviewed periodically (every 6 months) for independent
 closure.

## §A.10 Terminal vs instrumental value
The audit produces two distinct value functions:

### Terminal value
Audit closes (or honestly demotes) a specific prediction. Output: the
prediction's updated classification.

### Instrumental value
Audit reveals hidden assumptions in the framework's derivation
apparatus. Hidden assumptions typically affect multiple predictions.
Output: methodology refinement (new Step 5/Step 6 entries) plus
"watch for X in other predictions" markers.

**The May 2026 D10 sessions exemplified this.** Across 13 distinct
gem-finding sessions, D10 itself was never closed. But the same
sessions produced 7 antipattern manifestations, 3 coherent themes
(3D↔4D bridges, hybrid PT structure, gauge measure consistency), and
6 substantive structural findings affecting potentially all 21 SM
mass-cluster predictions. Terminal-value output was zero; instrumental-
value output was substantial.

### Identifying high-instrumental-yield predictions

A prediction has high instrumental yield if:

1. **Mixed-layer character** (substratum + emergent + EFT, etc.). More
 layers → more architectural tensions visible.
2. **Load-bearing assumptions in derivation chain.** Each is a
 potential hidden-assumption site.
3. **Empirically validated but structurally open.** Empirical
 validation removes pressure to "make the structure work"
 (which biases against finding hidden assumptions); openness motivates
 investigation.
4. **Standard-EFT analogue exists.** Disagreements with the analogue
 are candidate hidden assumptions.

D10 satisfies all four. D11 also (substantially). Cond 2 satisfies
1-3 but not 4 cleanly — paradoxically lower instrumental yield than
D10 even with higher terminal value.

### Two distinct investigation modes

**Closure mode** (Steps 1-7): structured around closing the
prediction. Architectural review, literature search, probe. Goal: the
classification update.

**Gem-finding mode** (Part VII): structured around exposing hidden
assumptions. Different question per session ("what assumption am I
implicitly making in step X?"). Different success criterion ("did
such findings reveal a structural blind spot, regardless of whether
it helped close the prediction?").

The two modes are not mutually exclusive but prioritized differently:
- Closure mode prioritizes high probability of classification change.
- Gem-finding mode prioritizes high probability of finding hidden
 assumptions, regardless of classification change.

When closure mode appears to yield diminishing returns (D10 after
several parking states), gem-finding mode may still have high yield.

### Triggers for invoking gem-finding mode

1. **Prediction repeatedly fails to close** despite multiple sessions.
 Diagnostic refines without closure.
2. **Methodology output accumulating faster than classification
 changes.** Make gem-finding explicit.
3. **Prediction recognized as high-instrumental-yield** (per criteria
 above). Even before investigation, gem-finding may be right initial
 framing.

### Operational difference

*Closure mode session:* identify residual gap → hypothesize derivation
that fills it → test → update classification.

*Gem-finding mode session:* identify load-bearing step → ask "what
assumption am I making here that could be wrong?" → investigate (lit,
dim analysis, re-derivation) → update methodology (and prediction
status if real issue found).

The gem-finding question is *what could go wrong*, not *how do I make
this work*. Bias toward skepticism, not extension.

### Classification scheme for gem-finding outputs

- **NEW:** Identifies structural blind spot not previously characterized.
- **POSITIVE:** Validates an inheritance or assumption (also valuable).
- **ELABORATING:** Adds detail or mechanism for previously-identified finding.
- **CONFIRMING:** Re-validates previously-identified theme.
- **BORDERLINE:** Identifies related question connecting to existing themes.

### Fixed-point criterion for convergence

Continue gem-finding until ~3-4 consecutive sessions produce only
ELABORATING / CONFIRMING / BORDERLINE outcomes (no NEW findings).

**Empirical baseline (D10):** Productive phase 6 NEW findings + 1
positive validation in 9 sessions (~50% NEW yield). Convergence phase
0 NEW findings in 4 consecutive sessions. Total: 6 substantive findings
+ 1 positive validation in 13 sessions.

### Cross-prediction propagation

A hidden assumption found in one prediction's audit often applies to
others. The Step 5 antipattern instances from D10 sessions have direct
implications for D11, Cond 2, and other SχPT-style or mixed-layer
predictions.

**This is a strong reason to do gem-finding investigation on a
high-instrumental-yield prediction *before* moving to lower-yield
predictions:** methodology refinement and assumption-watch markers
help lower-yield investigations catch their own issues earlier.

## §A.11 Lessons from completed audits
Across 17+ audit sessions covering all five primary documents (Main,
SM, GR, Substratum, Juno) plus two application papers (Complexity,
Medicine), the audit produced **0 fatal gaps** and **16 substantive
reclassifications**. The methodology lessons summarized here were
extracted from those sessions and integrated into §A.4 (the seven
manifestations) and the procedural sections.

### Per-document headline outcomes

**Main (foundational paper, C1-C3 → emergent QM theorem).**
- 6 sketch-grade findings, all editorial-level.
- 1 explicit conditionality: C2 necessity proof conditional on ETH
 (eigenstate thermalization hypothesis), honestly flagged in §3.4.
 ETH is well-supported but not theorem; framework's conditional
 framing appropriate.
- The "phase-locking lemma" upgrade and "spatial Markov property"
 invocation are sketch-grade but closeable (the area-law lemma
 exists in SM §3.1 — the Main → SM logical loop is closeable by
 Main-side restatement; this is Session 7-A pending work).
- Two independent emergence routes (§3.1, §3.2) provide genuine
 redundancy — *positive* finding.
- C1, C3 necessity theorems walk end-to-end without conditional flags.

**SM (most quantitatively dense, primary audit target).**
- 7 substantive sessions (triage + 6 substantive + assembly).
- 6 reclassifications: items 5 (Cabibbo, then re-promoted via D8),
 14 ($m_b$ via $Q_\text{down}$), 15 ($m_u/m_d$ via D11), 16
 ($\sin^2\theta_{12}$ via Cond 2), 18 ($\sin^2\theta_{23}$ via
 Cond 2), 21 ($m_b/m_\tau$ via D10).
- 3 active research directions identified (D8 closed, D10 pending,
 D11 pending).
- §7.5 flagged as the densest cluster of "structural identification
 + matching" links in the framework — most likely site for
 reclassifications.
- §7.6 / §8.3 internal tension on "mixing angles" classification
 resolved via four-layer framing (Layer 0/1/2(a)/2(b)/3) in §A.2.
- 17 text changes across §7.1, §7.2, §7.3, §7.5,
 §7.6, §8.3, plus §1/§7.7 coherence updates.

**GR (cosmological-horizon construction).**
- 4 sessions (triage + Tier 1 + Tier 2 + Tier 3 assembly).
- 1 reclassification: 1/6 factor in $a_0 = cH/6$ initially S → L,
 then closed via Verlinde 2016 literature search (D12).
- 1 new direction (D12, closed).
- Tier 3 self-classifications (transition steepness, greybody factor)
 confirmed honestly classified — explicitly flagged as
 solution-specific. *Positive* audit outcome.
- Appendix A theorems (Generalized Second Law, Page curve) properly
 proved using strong subadditivity, CPTP monotonicity, and
 Popescu-Short-Winter typicality.
- 5 text changes (~0.5 session of editing) —
 much smaller than SM's. Reflects GR's superior internal
 classification.

**Substratum (reconstruction theorem, gauge group).**
- 2 sessions (audit + assembly).
- §6.4 Class B paragraph restructured into four-stratum classification:
 - **B-S** (4 unconditional structural): Wolfenstein A, $m_d/m_s$,
 Koide $\theta_0$, Bekenstein-Hawking 1/4.
 - **B-L** (6 layered conditional, pending active research): Cabibbo
 $\lambda$ (D8 — now closed, moves to B-S), $m_u/m_d$ (D11), $m_b/m_\tau$
 (D10), $\sin^2\theta_{12}$ + $\sin^2\theta_{23}$ (Cond 2), MOND
 $a_0$ (D12 — now closed, moves to B-S).
 - **B-M** (2 mass-chain): $m_e, m_\mu$ via $m_\tau$; $m_H$ via $m_t$.
 - **B-R** (2 retrodictions): SU(2), SU(3) gauge couplings at $M_Z$.
- 0 fatal gaps in 8 prior-theorem dependencies (audit-verified).
- Theorem 23 (Reconstruction) and Theorem 24 (Substratum Gauge Group)
 unchanged.

**Juno (PMNS sin²θ_12, JUNO-relevant).**
- 1 session.
- 3 sketch findings: §3.4 "geometric interpretation 4/3 = 2A²"
 pattern-matched §A.4 Manifestation; §7.1 chirality argument for
 $1/|q|$ propagator (later closed via Mason et al. = D8); §7.3
 $\sin\theta_{13} = A^2\lambda$ projection geometry presented as
 derivation but actually motivating-target.
- Established that Juno's deepest dependencies route through SM
 (cubic-lattice substrate, Cond 2), not Main. This corrected the
 audit ordering: Juno → Main → SM (rather than Juno → Main → Substratum
 → SM).

**Complexity (chemistry/biology applications).**
- 1 session.
- 5 sketch-grade findings, all editorial: spin-statistics chain,
 mass hierarchy claim, independence assumption, implicit prior on
 parameter space, PVED magnitude argument.
- 2 minor: §2.7 thermal window circularity, §8.11 H ≈ 0.79 framing.
- *1 substantive observation:* §8.11 reports universal Hurst
 exponent H ≈ 0.79 ± 0.03 across single-molecule enzymes and a
 superconducting qubit. If holds up, constitutes quantitative
 empirical support for C1-C3 universality. New research direction
 (H(C3)) targets deriving this value from hidden-sector dimension.
- §§5-8 honestly classified as application content (statistical-
 structural, philosophy of existence, quantum biology, engineering)
 with explicit "Status: structural / parametric / contingent"
 classifications throughout. *Positive* audit outcome.

**Medicine (therapeutic applications).**
- Lightweight scope-classification check rather than full audit.
- §10.1 scope acknowledgment exemplary: explicitly states pure
 loss-of-function genetic disorders are NOT memory diseases. *The
 kind of scope discipline other framework documents also display.*
- 5 minor editorial findings.
- 0 fatal classification problems.

### Cross-cutting patterns (recurring sketch-grade templates)

These templates appear across multiple documents and merit uniform
treatment:

**Template 1: "Structural identification + matching".**
The most common sketch-grade pattern. Form: "[structural lattice
quantity] → identified with → [physical observable]." When forced by
a theorem, it's Solid. When relying on naturalness arguments +
consistency checks + empirical exclusion of alternatives, it's
sketch-grade. Examples: Cabibbo via $1/|q|$, Wolfenstein A via
"perpendicular component," Koide angle via $C_2/d^2$ vs alternatives,
$m_u/m_d$ via $\sqrt{\theta_0}$, matching scale + K = 1/2.

**Template 2: "Geometric interpretation".**
A numerical relation given a "geometric interpretation" ($4/3 = 2A^2$;
$\theta_0 = 2/9$ from $C_2/d^2$; etc.) without explicit uniqueness.
The interpretation may be correct but is not itself a derivation. The
audit should distinguish "geometric interpretation" (suggestive) from
"geometric derivation" (forced).

**Template 3: "$O(1)$ coefficient absorbed into the lattice convention".**
Used in §7.5's matching-scale derivation and §7.2's mass
parametrization. Natural in lattice physics but it *is* a convention
freedom doing load-bearing work. The audit determines whether the
convention is forced by other framework constraints (Solid) or
genuinely free (sketch-grade).

**Template 4: "Empirical exclusion of natural fractions".**
"$K = 1/2$ is the only fraction in $\{1/4, 1/2, 1, 2\}$ compatible
with observation" — *evidence in favor* of a particular value but
*not a derivation*. The audit's standard for promotion (§A.7)
explicitly excludes empirical exclusion as a promotion mechanism.

### Closure validations (what made D8 and D12 close cleanly)

Two of six active research directions closed via Step 4 literature
search alone, without OI-internal computation:

**D12 (1/6 factor in $a_0 = cH/6$).** Initial audit identified the
factor as sketch-grade, attributed loosely to "volume-to-surface
ratio of spherical redistribution in de Sitter" (which isn't quite
right — V/A for a sphere is r/3, not r/6). Literature search
revealed Verlinde (2016, eq. 1.7) establishes the factor explicitly
as $(d-3)/[(d-2)(d-1)] = 1/6$ in $d = 4$. Closure proceeds by citing
Verlinde + noting OI's structural grounding of his postulated
elasticity (via condition C2) + addressing the published consistency
objection (Dai & Stojkovic 2017) by pointing to OI's derivable
structure.

**D8 (Cabibbo $1/|q|$ chirality).** Mason et al. (HPQCD,
hep-lat/0209152) "Taste-Changing in Staggered Quarks" establishes
directly that taste-changing transitions in staggered quarks have
spinor structure given by $\gamma_\mu$ + $\gamma_{5\mu}$ — both
chirality-preserving (vector and axial currents). Combined with
unbroken $U(1)_\epsilon$ chiral symmetry, this establishes the OI
claim. Closure took ~30 minutes of literature search rather than
from-scratch derivation.

**Lessons from the closures:**
1. Literature search before from-scratch derivation can save weeks
 of effort.
2. The honest move is "cite + note OI-specific contribution," not
 "reconstruct."
3. The OI framework's distinctive contribution becomes *clearer* when
 stated as extension of established work rather than replacement.
4. Published consistency objections to the cited work can be
 addressed directly in OI text, sharpening OI's contribution.

### Self-disclosure quality assessment

Some framework documents are more self-disclosing than others. Worth
preserving as templates:

**Exemplary self-disclosure:**
- SM §7.5 *Residual gap* subsection — explicitly identifies what's
 deferred for K = 1/2 verification.
- SM §6.2 *Empirical determination via the U(1) row* — explicitly
 flags $\delta_0$ as fitted, marked **E** in §7.6.
- SM §7.2 — $Q_\text{down}$ marked **P** (phenomenological input)
 with §7.6 footnote.
- GR §7.3 Step 4 — transition steepness explicitly Tier 3
 (solution-specific rather than structural).
- Medicine §10.1 — explicitly states genetic disorders not in scope.

**Foregrounding could improve:**
- SM §7.5 lines 946 and 970 (empirical-fitting acknowledgments
 embedded in primarily structural arguments — easy to miss on
 casual reading; amendment text foregrounds them).
- §7.6 / §8.3 tension on "mixing angles" before the four-layer framing
 (Layer 0/1/2(a)/2(b)/3 in §A.2) was developed and applied.
- Substratum §6.4 Class B's undifferentiated "13 parameter-free
 retrodictions" (restructures to four-stratum B-S/B-L/B-M/B-R).

**Patterns that cause foregrounding gaps:**
- Empirical-fitting acknowledgments embedded in structural arguments
 rather than at section opening.
- Conditional dependencies not stated when they enter the chain (only
 noted later as "open task").
- Honest-but-implicit classifications (where the document gets it
 right in spirit but misses the explicit status table update).

The audit's role for already-self-disclosing sections is foregrounding
+ propagating to summary tables, not finding new content gaps.

### Overall summary

After 17+ sessions across all primary documents:
- **0 fatal gaps** across the entire framework.
- **16 substantive reclassifications**, all status refinements (S → C/L
 acknowledging conditional or layered structure) rather than content
 corrections.
- **4 active research directions** identified (D8 closed, D10/D11
 open, D12 closed, Cond 2 next, H(C3) longer-horizon).
- **Empirical performance unchanged across audit:** every prediction
 within ~1% or ~1σ. Audit refines classification precision; predictions
 stand.
- **Framework characterization (post-audit):** *structurally correct
 but under-documented* on bridges between substratum (3+1D Lorentzian,
 real scalar bijection, Z/qZ measure) and operational lattice-PT
 machinery (3D Euclidean, Berezin pseudofermion, Haar gauge measure).
 Closing those bridges would upgrade many predictions from S‡ to S.

This is a healthy outcome: the framework's strong claims are mostly
sustained, with explicit conditional flags on the 4-6 predictions where
the derivation chain genuinely depends on stated open assumptions.

## §A.12 Investigation strategy — DFS preferred over BFS
**Decision recorded.** When pursuing gem-finding investigations or other multi-avenue research questions, the default investigation strategy is **depth-first** (DFS): drive a single avenue toward higher closure levels until it is exhausted or genuinely walled, before pivoting to alternative avenues.

This contrasts with breadth-first (BFS): scoping multiple avenues in parallel, achieving partial results in each, and reporting the best overall. BFS produces broader-but-shallower results; DFS produces narrower-but-deeper results.

**Rationale.**

1. **Closure-level asymmetry.** A single avenue closed to Layer 1 is more valuable than three avenues closed to "partial Layer 2(b) sharpening." Closure-level value is highly nonlinear: full Layer 1 is qualitatively different from partial Layer 2 (definitive vs. provisional).

2. **DFS exposes deeper structure.** Avenue 4 of gem-hunt 1.1 illustrates this: pushed shallowly, avenue 4 produced "partial Layer 2(b) sharpening" (MFV-like reformulation). Pushed deeper, the same avenue produced explicit derivation of Δ_23 = b_23 λ², the Cond 2 ⟺ sum-rule-preservation equivalence, and Layer 1 closure of A_1's structural role — three substantively different results, none visible at the shallow level.

3. **Pivoting to a new avenue resets the work.** Each avenue has its own setup cost (state-loading, calculation infrastructure, conventions). Pivoting incurs this cost repeatedly. DFS amortizes the setup cost across deeper progress in the same avenue.

4. **DFS produces immediately-actionable paper updates.** Deep results within a single avenue are typically self-contained and can be propagated to the paper text directly. Shallow results across multiple avenues require synthesis before they become paper-ready.

5. **DFS aligns with how genuine progress actually happens.** Most novel mathematical insights emerge from sustained engagement with one specific question, not from juggling several. The framework's prior closures (D8, D12, multiple bridge-gap closures) all came from extended single-thread investigation.

**When BFS is appropriate.**

- *Pure scoping phase.* Before committing investigation effort, BFS is appropriate to map which avenues exist (this is what gem-hunt 1.1's initial scoping into avenues 1-4 was). The pivot from BFS to DFS happens once the avenue space is mapped.
- *When DFS hits a hard wall.* If an avenue genuinely cannot proceed (e.g., requires offline lattice-PT computation; requires data we don't have), then pivoting to a different avenue is correct.
- *When DFS would require capabilities outside chat scope.* E.g., Cond 2 closure requires explicit numerical lattice computation; further DFS into avenue 4's substrate-mechanism question would require running a one-loop staggered code, which is offline territory. At that boundary, recording the open task and pivoting is correct.

**Operational implications.**

- Sessions should default to DFS within an investigation. Pivots to alternative avenues happen only when (a) DFS hits a genuine wall, (b) user explicitly requests pivot, or (c) DFS produces a result that subsumes other avenues.
- "Partial closure" results should not be the default reporting form. If an avenue gives only partial closure, push deeper before reporting.
- When recording results, include the DFS-progression: what was the prior state, what intermediate states were passed, what was the final state, what walled the further progression. This makes the closure level claim auditable.

**Methodology amendment recorded.** This applies to all subsequent gem-finding investigations and multi-avenue research questions in the framework.

## §A.13 Offline tasks excluded from chat-track ranking
**Decision recorded.** Tasks that are external to the chat environment or beyond chat-session feasibility are excluded from chat-track recommendations, prioritization, and confidence-impact assessments. Chat-track output is ranked on its own terms — what chat sessions can produce — without competing against tasks that don't belong on the same ranking axis.

**What "offline" means (refined definition).** "Offline" is defined by feasibility, not by task category. Three classes of tasks are excluded:

1. *External / administrative.* Tasks requiring systems Claude cannot access — Zenodo deposits, journal submission portals, ORCID/email fills, verification of what is currently published at a DOI, internal-section-number checks against external deposits. These are never chat-track candidates regardless of session length.

2. *Beyond chat-session feasibility.* Computations whose scale or duration exceeds chat-session timescales — multi-day Monte Carlo studies with thermalization plus many independent samples, FORM/Mathematica-scale symbolic computations (10+ hours typical), large-$N$ extrapolations requiring many runs in sequence. These are offline by computational scale.

3. *Capability-blocked.* Tasks requiring capabilities Claude does not currently have (image generation specific to the framework, real-time external data feeds beyond what `web_search` provides, etc.).

**What "online" includes (the corrected scope).** Computations within chat-session feasibility are *online and chat-trackable*, even when they involve numerical or lattice work that earlier framing might have called "offline":

- Sympy verification of structural identities (algebraic checks, RG-irrelevance arguments, group-theory expansions)
- Small-to-medium-$N$ lattice perturbation theory — up to roughly the $N = 40$ scale of the existing `oi_lattice_code/AB_derivation/` (~40 minutes single-core per run, manageable in a chat session)
- Targeted HMC simulations at small lattice (compile + run the existing C codes for specific cross-checks)
- Numerical evaluation of paper-text claims against PDG values
- Monte Carlo sanity checks at small statistics (where full closure would need many more samples but a first-pass is informative)

These participate in chat-track ranking like any other chat-tractable investigation.

**Earlier formulation correction.** The initial §A.13 entry listed "lattice-PT computations" in the offline-example bullet alongside Zenodo deposits and ORCID fills. That formulation was over-broad: it conflated administrative/external tasks (genuinely off-axis) with computational tasks (which range from chat-tractable to chat-prohibitive based on scale). The corrected framing distinguishes by feasibility rather than by category. The methodology rule's *purpose* — preventing administrative items from dominating chat-track ranking — is unchanged; the refinement is just to specify what counts as administrative vs. computational vs. chat-trackable.

**Rationale (unchanged from initial entry).** Offline and chat-track tasks are not commensurable on a single ranking axis. Including offline items in chat-track rankings produces two failure modes:

1. *Offline items always dominate.* "Submit Juno to PLB" has higher real-world publishability impact than any internal structural sharpening, so any ranking that includes it will recommend it. This collapses chat-track recommendations to "remind the user to do their offline work" — useful exactly once, then noise.

2. *The comparison itself is malformed.* "Re-deposit to Zenodo" and "investigate Cond 2 substrate alignment" are not the same kind of task; ranking them against each other produces apples-to-oranges output.

**Operational implications.**

- §C.3 "Recommended next session" subsection ranks chat-track candidates only — including in-chat numerical work where feasible. Offline tasks (the three classes above) live in §C.3 "Offline tasks user retains" and in §C.4 honest limitations.
- Chat-track confidence-impact analyses (expected pp-movement on framework-overall confidence) compute over the chat-track candidate set only — but the candidate set now includes in-chat numerical tasks at the appropriate feasibility level.
- The user is presumed to be tracking external/administrative tasks independently. Repetitive surfacing of those in chat-track output is to be avoided.
- Exception: if a chat-track recommendation is *prerequisite-blocked* by an offline task (e.g., a chat investigation cannot proceed without a particular external result), that prerequisite is stated once and the chat-track item is deferred or scoped accordingly.
- Sanity-check / first-pass / small-scale numerical work *promoted from offline*: when a previous classification said "offline lattice-PT computation," ask whether a small-$N$ or first-pass version is feasible in chat. If yes, the chat-track candidate is the small-$N$ first pass, with the full $N \to \infty$ extrapolation remaining offline. This produces a graduated rather than binary online/offline classification.

**Second refinement : online-by-default presumption.** Tasks are presumed online (chat-trackable) unless explicitly identified as one of the three offline classes above. The default-classification direction was reversed by this refinement, addressing a recurring pattern in which structural derivations were being classified offline by default — and only re-promoted to online after explicit user prompting (instances: §B.2.38 promoted lattice-PT first passes; this refinement promotes structural derivations).

*Operational test.* Before classifying a candidate task as offline, ask: "does this require Mathematica/FORM-scale symbolic computation, multi-day Monte Carlo with full thermalization plus many independent samples, or external system access Claude does not have?" If no to all three, the task is online.

*Examples reclassified by this refinement.*

- Structural derivations (e.g., "derive the boundary-mode dispersion from substratum mode counting + QFT-recovery requirement"): online, even if non-trivial. They require reasoning, not heavy compute.
- Sympy-aided algebraic verification: online (already in scope per first refinement).
- Small-to-medium-$N$ lattice PT (up to ~$N = 40$): online (already in scope per first refinement).
- Targeted small-lattice HMC: online (already in scope per first refinement).
- Multi-day MC studies, FORM-scale symbolic, large-$N$ extrapolations needing many runs: offline (computational scale gates).
- Zenodo deposits, journal submissions, ORCID fills, DOI verification: offline (external/administrative gates).

*Pattern this refinement addresses.* Default-offline classification of derivations leads to under-using chat scope: a structural derivation gets parked as offline when it would close in 1-2 sessions of focused DFS. Default-online classification matches §A.12's DFS-preferred posture and avoids the recurring offline/online recategorization back-and-forth.

**Third refinement : three-phase computational pipeline framing.** The first two refinements established that "online" includes more than initially classified — small-to-medium-$N$ lattice PT, sympy verification, structural derivations, targeted small-lattice HMC. This refinement extends the framing to computational tasks that exceed chat-session feasibility *for execution* but do not exceed chat-session feasibility *for preparation or analysis*. These are split into a three-phase pipeline:

- *Phase 1 — online prep (chat-track).* Write the source code, Mathematica/FORM notebook, or lattice driver. Specify diagrams, regularization scheme, parameter scan, expected outputs, runtime envelope, and environment requirements. Pre-register what each result would mean for prediction classification — including both confirmation criteria (e.g., "$K_S = 0.0072 \pm 0.001$ → D10 L → S") and falsification criteria (e.g., "$K_S < 0.005$ → reopen mechanism specificity"). Pre-registration before execution prevents post-hoc rationalization of unexpected outputs.

- *Phase 2 — offline execute (user-side).* User runs the prepared code on local hardware. Mechanical only: no research decisions, no scope changes, no scope additions. The phase is gated by hardware availability and runtime; once those are met, the work is determinate.

- *Phase 3 — online analyze (chat-track).* User pastes outputs from Phase 2; chat-track validates against the Phase 1 pre-registered criteria, identifies discrepancies, runs follow-up analysis where Phase 1 left analytic flexibility, and propagates results into framework documents and §B.3 classifications.

*Pattern this refinement addresses.* The previous offline-bucket framing collapsed three distinct activities into one: research design (Phase 1), mechanical execution (Phase 2), and result interpretation (Phase 3). Phases 1 and 3 are core chat-track work — they involve reasoning, framework integration, and pre-registration discipline that are substantively chat-tractable. Only Phase 2 actually requires offline resources. Treating the whole pipeline as offline made the work plan look static even when the design and analysis components were chat-trackable; treating only Phase 2 as offline restores accurate accounting and converts the offline-computation items into staged work with the user as the named executor for Phase 2.

*Pre-registration discipline.* Each pipeline requires pre-registered *failure modes* alongside closure criteria, not just confirmation criteria. The pattern: "if [output] then [classification movement]; if [other output] then [framework update]." Pre-registration before execution prevents the post-hoc rationalization failure mode the §A.4 antipattern catalog warns against — getting an unexpected number and reverse-engineering an explanation. The Phase 1 deliverable is therefore *code + pre-registered closure-and-falsification specification*, not code alone.

*Operational implications.*

- §B.5's computational items are reshaped as pipelines with current-phase status. Each item carries: which phase is current, what was completed in prior phases, what Phase 2 resources are needed, and what Phase 3 closure + falsification criteria have been pre-registered.
- "Offline" in §B.5 now refers narrowly to: external/administrative tasks (Class 1), Phase 2 execution of pipelines whose Phase 1 has completed (Class 2 narrowed), and capability-blocked tasks (Class 3). Computational items as a whole are no longer offline; only their *execution* phase is.
- Cold-pickup orientation: the Phase 1 candidate at the head of the queue is the natural next chat-track item.
- Pre-registration criteria become part of the documented framework state. Phase 1 outputs include both code and a pre-registered closure-criteria specification to be referenced in Phase 3.
- The methodology update is independent of §A.10's instrumental-value framing: a pipeline's Phase 1 + Phase 3 still count as terminal-value work toward the prediction it targets; the new framing only refines how chat-track work is staged across the offline boundary.

*Examples reclassified by this refinement.*

- D10 K_S two-loop SχPT (offline, ~10+ hours Mathematica/FORM): now a pipeline. Phase 1 (write code + pre-register criteria) is chat-track. Phase 2 (execute) is offline. Phase 3 (analyze + propagate) is chat-track.
- Cond 2 4A² channel enhancement at full $N \to \infty$: now a pipeline. Phase 1 spec ready (Layer 2(a) reduction per §B.2.29-§B.2.31). Phase 2 (offline staggered substrate one-loop with $N$-extrapolation harness). Phase 3 propagates to entries 12, 14, 19.
- AB-separation 3-loop integrand decomposition: now a pipeline. §B.2.34 partial Phase 1 already done at chat scope $(A,B) = (2^d, 2d)$ confirmation; full 3-loop Phase 1 requires extending existing `oi_lattice_code/AB_derivation/` infrastructure.
- A2 δ_0 3-loop staggered VP: now a pipeline. Phase 1 ready; shares machinery with D10 K_S, so amortization across pipelines is available.

**Methodology amendment recorded.** Applies to all §B.5 work plan formulation, §C handoff orientation, and computational-item classification going forward.

**Fourth refinement : pipeline framing applies to research-stage exploration, not just preparation of established pipelines.** §A.13's third refinement framed three-phase pipelines for tasks where Phase 1 is *known to be feasible* and Phase 2 is *known to require specific external resources* (Mathematica/FORM hours, named compute hardware). This refinement extends the framing to **research-stage exploratory calculations** that might be feasible at small scale in chat without yet knowing whether they'll succeed.

*Pattern this refinement addresses.* In §B.2.107-§B.2.108 the composite-Higgs cluster's Option (a) — derive the trace-out fractional-power mechanism (GEMs 53-54) — was labeled "offline-heavy" without checking against §A.13's established framework. Re-examination revealed that the calculation decomposes naturally into the three-phase pipeline: Phase 1 = small-lattice exact computation specification (chat-tractable), Phase 2 = larger-$L$ stochastic execution (chat-tractable to offline depending on scale), Phase 3 = scaling analysis and framework propagation (chat-tractable). Default-offline classification of exploratory research-stage calculations leads to the same under-using-chat-scope failure that prompted the second refinement, but with a different mechanism: the offline label is being assigned not because the work has been shown to require offline resources, but because the work has not been *scoped* yet and offline is the default for unscoped computational tasks.

*Operational test (revised).* Before classifying a research-stage exploratory calculation as offline, ask: "**Has Phase 1 scoping been done?**" If no, Phase 1 scoping itself is chat-tractable and should be the first step. The Phase 1 output (precise model specification, resource estimate, decomposition into tractable pieces) determines whether Phases 2-3 are chat-tractable, offline, or genuinely infeasible. Skipping Phase 1 to assign an offline label is a methodology error — Phase 1 *is* the determination of whether the rest is offline.

*Examples reclassified by this refinement.*

- Trace-out fractional-power derivation (GEMs 53-54): no longer offline-by-default. Phase 1 scoping is chat-tractable. Whether Phases 2-3 are chat-tractable depends on the Phase 1 output (specifically: what lattice sizes are required for clean scaling extraction, and whether the trace-out admits enumeration / stochastic sampling / transfer matrix at those sizes).
- Other "speculative" structural derivations: same treatment. Default presumption is that Phase 1 scoping is chat-tractable; the resource-requirements determination follows from Phase 1 rather than preceding it.

*Pattern observation.* The first three §A.13 refinements progressively expanded the chat-track scope by reclassifying specific task categories from offline to online. This fourth refinement is methodological rather than categorical: it adds the procedural step of *scoping before classifying*. The risk this addresses is that exploratory-research calculations have no fixed category — they could be cheap or expensive depending on the structure of the calculation, which isn't known until Phase 1 is done.

*Relationship to §A.12's DFS-preferred posture.* Phase 1 scoping is DFS into the calculation: pin down the smallest version that would still produce informative output. The DFS-vs-BFS distinction now extends to computational planning: BFS surveys all parameter choices before computing; DFS picks one and computes, learning whether the choice was viable. For exploratory calculations, DFS is the right posture — pick the smallest tractable version, compute, learn, then decide whether to scale.

*Methodology amendment recorded.* Applies to all exploratory-calculation classification going forward.

**Fifth refinement (validated by §B.2.111 + §B.2.113): Phase 1 deliverables include explicit measurement-procedure pre-registration.** §A.13's third and fourth refinements established the three-phase pipeline for exploratory calculations and specified that Phase 1 scoping is the prerequisite for offline/online classification. This refinement adds a specific Phase 1 deliverable: **the measurement procedure that connects the calculation's output to the hypothesis must be pre-registered, not deferred.**

*Pattern this refinement addresses.* In §B.2.111 the v1 Phase 1 spec for trace-out fractional-power was nominally complete (lattice size scoped, sampling strategy specified, resource estimates verified) but the v1 *execution* revealed three errors: (1) operators were defined on visible sites only, giving identically zero hidden-state variance by construction; (2) the test was time-evolution of uniform-random states, trivially flat for linear-mod-q dynamics; (3) the measurement strategy conflated dynamical correlation decay with static coupling renormalization. None of these errors were detectable from the v1 spec alone — they only became visible when the code ran and produced uninformative output. The v2 spec written in §B.2.113 explicitly pre-registered: (a) what quantity is computed, (b) what the hypothesis predicts for that quantity, (c) how the prediction translates to numerical outcomes, (d) what classifications (Outcome A/B/C/D) the numerical outcomes map to. The v2 execution then produced cleanly-interpretable results — including refutation of the hypothesis — that the v1 procedure could not have produced.

*Operational test (revised Phase 1 deliverables).* A Phase 1 scoping document must address all four:

1. **Computational scoping** (third refinement): lattice size, sampling strategy, resource estimates.
2. **Decomposition** (fourth refinement): what the smallest informative version of the calculation is.
3. **Measurement procedure** (this refinement): the precise quantity computed and how it connects to the hypothesis being tested.
4. **Outcome pre-registration** (this refinement): what numerical outcomes count as confirmation, refutation, or ambiguous, *before* the calculation runs.

If any of (1)-(4) is missing, the Phase 1 spec is incomplete and the calculation may produce uninterpretable results — as occurred in §B.2.111 v1.

*Examples this refinement clarifies.*

- §B.2.111 trace-out v1: Phase 1 deliverables (1)-(2) complete, (3)-(4) absent. Execution produced output but the output couldn't be interpreted because the connection between "operator variance under sampling" and "fractional-power suppression hypothesis" wasn't pre-registered.
- §B.2.113 trace-out v2: Phase 1 deliverables (1)-(4) complete. Execution produced output that mapped cleanly to pre-registered outcome categories. Result was Outcome C (refutation at basic-substratum level) — interpretable.
- Future exploratory calculations: Phase 1 spec must include (3) and (4) before classifying as offline/online or proceeding to execution.

*Relationship to scientific methodology.* This refinement is the framework-internal version of pre-registration in empirical research — specifying analysis procedures and predicted outcomes before the data is collected, to prevent the "results uninterpretable because the question wasn't precise enough" failure mode. For internal exploratory calculations the same discipline applies: pre-register the measurement and the outcome map, so that the calculation either confirms, refutes, or returns an ambiguous result *that the spec recognizes as ambiguous*.

*Empirical validation.* This refinement is being committed *after* its application to §B.2.113 produced cleanly-interpretable results (specifically: clean refutation of GEMs 53-54 at the basic-substratum level, with the cycle-length structure as a separately-interpretable positive finding). The methodology rule is therefore empirically supported, not just speculative.

*Methodology amendment recorded.* Applies to all exploratory-calculation Phase 1 specs going forward.

## §A.14 Propagation-audit pattern across parallel manuscript sources
**Context.** The framework's book is maintained in two parallel forms: `book/The-Incompleteness-of-Observation-FULL.md` (consolidated complete manuscript) and individual chapter files `book/ch*.md`. These are *parallel sources*, not derived from each other — FULL.md is larger than the sum of chapter files (it includes title page, frontmatter, appendices, etc.) and chapter files are not concatenated to produce it. The same content appears in both whenever a chapter is treated as a standalone artifact.

**Implication for propagation.** When sharpening or modifying content that appears in multiple manuscript locations, edits must be applied to every parallel location independently. The audit pattern that catches all parallels is:

```
grep -rn "<distinctive phrase from the sharpened content>" papers/ book/
```

Critically: this must search BOTH `papers/` AND `book/` (including all `book/ch*.md` files AND `book/The-Incompleteness-of-Observation-FULL.md`). Searching only `papers/` and `FULL.md` (the failure mode that occurred this session) misses parallel passages in individual chapter files.

**Consistency check after propagation.** For each newly-introduced distinctive phrase, verify the count matches expected locations:

```
grep -c "<distinctive phrase>" papers/*.md book/*.md
```

If a sharpening was meant to apply to N locations but only N-1 files show the new phrase, a parallel passage has been missed. Cross-check by also counting the *old* phrase being replaced:

```
grep -c "<old phrase being sharpened>" papers/*.md book/*.md
```

If the old phrase still appears anywhere it shouldn't, that file needs updating.

**Empirical validation.** This refinement is being committed *after* its application to the §17 math-physics-gauge sharpening propagation produced a user-caught miss: `book/ch02-substratum.md` line 32 retained the unsharpened substrate-objection passage even though `book/The-Incompleteness-of-Observation-FULL.md` had been sharpened. The miss occurred because my initial propagation audit searched `papers/*.md book/The-Incompleteness-of-Observation-FULL.md` but not `book/ch*.md`. Applying the §A.14 pattern from the start would have caught this.

*Methodology rule recorded.* Applies to all propagation passes affecting content that appears in multiple manuscript sources.

---

## §A.15 Repository scope — manuscript files only
**Rule.** The public repository (`incompleteness-main`) contains **manuscript files only**: the papers (`papers/`), the book (`book/`), the supporting lattice/numerical code that the papers depend on (`papers/oi_lattice_code/`), and standard repo infrastructure (README, LICENSE, .gitignore), and — since 2026-07-25 — the methodology set (`methodology/01–03`: §A, §B operational state, §B.9 reference docs), kept self-contained. Nothing else belongs in the repo.

**What this EXCLUDES (and where each lives instead):**
- **The session journal, TODO queue, and handoff (§B.2 / §C)** — the private working record across sessions, not a framework artifact; maintained off-repo. (The stable §A/§B layers moved into the repo as `methodology/` on 2026-07-25; the session-scale layers deliberately did not.)
- **Working-session findings** — venture screening, geometry-vs-contents analysis, Bell-gate reasoning, realism/epistemics discussions, etc. (§B.2.193–195). These are journal content (off-repo), not repo content.
- **Exploratory / applied-track documents** — e.g. TEMPO_VENTURES.md, the benefit-if-true pipeline. Decoupled applied tracks (§B.2.194) live in their own files outside the repo; per the prior precedent (§C era, May 24) exploratory work belongs in a companion location, not the framework repo.
- **Audit / verification scaffolding** — e.g. load_bearing_joints_audit_map.md. Internal tools for structuring verification. NOT committed to the repo unless and until (a) their content is corrected and verified against the papers, and (b) a deliberate decision is made to publish them — and even then as a clearly-marked separate document, not mixed into the manuscript. (As of this entry, the audit map is NOT repo-ready: the Joint-1 first-principles pass found it over-states a status the source qualifies; the correction has not yet been applied to the map file itself.)

**Rationale.** The repo is the framework's public, citable face — what a referee, reader, or arXiv submission points to. Mixing in working notes, applied-track exploration, or unverified self-audit scaffolding would (a) dilute the manuscript with non-manuscript material, (b) risk publishing status claims (e.g. an "audit map" label) that the author already knows need correction, and (c) blur the clean separation between *the framework* (repo) and *the work of developing and checking it* (the off-repo working records + companion docs). Keeping the repo manuscript-only keeps the public artifact exactly as authoritative as the papers themselves, no more and no less.

**Consequence for "is the repo updated?" checks.** Most session work is NOT repo-bound by construction — it updates the off-repo working records. A repo update is warranted only when a manuscript file (paper, book, or its code) actually changes. Confirming "the repo is updated" therefore means checking that manuscript edits propagated (per §A.14), NOT that session findings appear in the repo — they should not.

## §A.16 Understanding is the aim — run cheap probes that might serve it; judge significance after, not before
**Decision recorded.** Understanding of the underlying truth is the terminal aim; computation is instrumental to it (complements §A.10). The operational consequence: **when a computation might increase understanding, the default is to run it and see, not to rule it out in advance.** A pre-emptive judgment that "this can't bear on the question" is itself an unverified theoretical claim — and you frequently do not know a computation's true significance until the result is in hand. Ruling it out beforehand is how genuine surprises get missed.

**Why pre-judging significance is the trap.** The significance of a result is a property of the result, not of the plan. Predicting "all outcomes will be uninformative" assumes you already understand the structure well enough to know what the computation would reveal — which, for a genuinely open question, is exactly what you do not yet have. The history of the framework's own progress (and of physics generally) is full of computations expected to be routine that exposed unanticipated structure. So a *predicted*-null result is not the same as a *checked*-null result, and the gap between them is where understanding sometimes lives.

**Cost is the governor (not relevance-prediction).** This is not "run everything." It is "do not let an unverifiable relevance-prediction veto a cheap probe with any genuine chance of teaching you something."
- **Cheap probe, possible upside → just run it.** The cheapest way to learn a computation's significance is usually to run it. piece11 cost seconds.
- **Expensive campaign → the relevance case must justify the cost.** A multi-day two-species HMC is not run on a whim; here the burden of arguing it bears on the question is real, because the cost is real. The discipline scales with cost, not with a blanket pre-filter.

**The piece11 episode, correctly read (§B.2.232).** Running piece11 was *right*, not a mistake: it was cheap, fully gated (rotational R = machine zero, hypercubic B_phys ≈ zero at both loop orders), and its two-loop trend could in principle have bent sharply toward the sign-flip — which would have been a real signal worth having. The actual error was downstream, in the *interpretation*: framing an uninformative outcome as "removes perturbative comfort for the candidate" inflated a null result into apparent significance. An honest post-hoc reading converts it to its true value: a *checked* fact (the perturbative series shows no trend toward the flip, now verified rather than assumed) that does not settle the non-perturbative question. That is a modest but real gain — and it is the correct way to bank a null.

**Where the discipline actually lives: honest interpretation, after the run.** The gate discipline ("trust the gated computations over the narrative") ensures a result is *correct*. §A.16 governs how its *significance* is reported once it is in hand: state plainly what the result does and does not bear on, and resist inflating a null or off-target result into a verdict (the converse of the declare-victory antipattern). A checked null is logged as a checked null — neither discarded as worthless nor dressed up as progress.

**Relation to §A.12 (DFS) and the no-shopping guardrails.** Depth-first still means deeper *toward understanding*; but when uncertain whether a cheap next step bears on the question, the resolution is to run it and find out, not to debate it into a veto. The "resist mechanism-shopping / declare-victory" guardrails are unaffected: they govern proliferation and over-interpretation, not the decision to execute a cheap, possibly-informative probe.

**Operational implications.**
- Default to running cheap probes that might increase understanding; reserve relevance-justification for genuinely expensive work, where it is a cost decision, not an epistemic veto.
- Do not rule a computation out on a predicted-insignificance basis you cannot verify without running it. A predicted null is not a checked null.
- Put the discipline on the *interpretation*: report exactly what a result bears on; bank checked nulls honestly (neither inflated nor discarded).

**Methodology amendment recorded.** Applies to all subsequent computational and analytic work in the framework. Supersedes the earlier same-day draft of this section, which framed the lesson as a pre-registration relevance *filter* ("if all outcomes leave the question where it was, do not run it") — that over-rotated toward avoidance and would have wrongly vetoed cheap probes like piece11 whose significance was not actually knowable in advance. The corrected principle: lean toward running; judge significance after; scale caution to cost. Earned from the piece11 episode (§B.2.232).

## §A.17 Peer review is the verification stage — proceed with development; the only pre-review limitation is on self-assessment (the bands are a proxy until then)
**Decision recorded.** Independent verification is the job of *peer review* — the designated external stage that comes after the work exists. Its absence is therefore the NORMAL condition of in-progress, pre-submission work, NOT a constraint on current development. Development proceeds now; you cannot peer-review work that has not yet been done, and waiting for verification before producing internal results inverts the normal scientific order. The lack of independent verification does not limit or gate development.

**The one thing it does limit: self-assessment.** The single quantity the pre-review verification gap genuinely constrains is the confidence bands (consistency 89–93%, correctness 33–47%). Until peer review is possible, the bands are a self-generated *proxy* — a self-consistent internal *ordering* of confidence — not externally calibrated probabilities. They are self-referential: they score internal coherence as judged by the same process that produced the content, and only their relative *moves* (the 0pp bookkeeping) have been tracked with care, never the absolute *level*. Peer review is precisely what converts this proxy into an externally anchored assessment. So: treat the bands as provisional-pending-review, and label them that way in any external-facing artifact — this is honest status-marking, not a brake on the work.

**Exposure is a spectrum — and it matters FOR review, not as a development brake.** Different result-types will be weighted differently by a reviewer, so it is worth recording where each sits — not to slow development, but so nothing is *presented* as more settled than it is:
- **Low — machine-checkable.** Computations with falsifiable numerical gates (hypercubic ⇒ 0, rotational ⇒ 0, machine-precision self-tests; pieces 6–12). A gate is a quasi-independent check even though self-authored — a fact that holds or fails, not a judgment — and is robust to review.
- **Medium — structural proofs.** Checkable in principle but subject to the author's blind spots.
- **High — impossibility / negative claims.** "I could not find X, therefore X does not exist" (the false-impossibility trap, §B.2.228 B). The claim type most discounted at review until independently reproduced.
- **Highest — the bands.** Self-assessment, self-referential, the most reviewer-discounted of all (see above).

**The actual discipline (a presentation rule, not a development limit).** Develop freely, but do not *lean a conclusion on a high-exposure result as if it were already verified*. The boost no-go is the live example: developing the candidate, the gates, and the characterization is good current work and should continue; asserting "no protecting symmetry exists" as established would be the misstep — not because a specialist is needed first, but because a self-certified impossibility claim is exactly what does not survive review. Likewise, stating the bands as calibrated probabilities (rather than a provisional internal ordering) would overstate them. The limitation is on what one *claims as settled*, not on what one *works on*.

**Operational implications.**
- Proceed with development without waiting for verification; peer review is the verification stage, and its absence pre-submission is normal.
- Treat self-assessment (the bands) as a provisional proxy pending review; in external-facing artifacts state them as an internal ordering of confidence, not calibrated probabilities.
- Do not present any high-exposure result (impossibility claims especially, and the band levels) as already-verified; that is the only thing the verification gap actually constrains, and it is a presentation discipline.

**Methodology amendment recorded.** Applies framework-wide. Supersedes the initial same-day draft of this section, which over-rotated — it correctly recorded the calibration caveat but wrongly converted it into a *development* brake ("rank getting verified above producing internal results"), inverting the normal order in which development precedes peer review. Corrected position: peer review is the verification stage, so develop now; the only pre-review limitation is on self-assessment, which is a proxy until review makes external calibration possible. Complements §A.16 (self-generated *understanding*) by bounding self-generated *assessment*.

---

## §A.18 Guard against the program-scale recency ratchet — rebuild the assessment from the oldest claims, not the latest
The session-scale rhythm (log an entry, fold it, update the marker, resume from the marker) has a structural side effect at the *program* scale: the newest thread is always the one in working memory, named, given a confidence line and follow-up targets, while older results settle into unexamined "background." Each marker points the next session back at the most recent thread, deepening it further. The result is a ratchet — recent work accretes elaboration; old load-bearing claims go un-re-audited — that from the inside is indistinguishable from genuine prioritization.

**The fingerprint is already in this document.** The correctness band has wobbled 25-40% → 32-46% → 33-47% → 34-48% → 33-47% in ±1pp steps that each track whichever audit was most recent; the consistency band has been pinned at 89-93% across the entire history. §A.17 already conceded the deeper fact: *only the relative moves were ever tracked with care, never the absolute level.* A number that never moves across dozens of intensive sessions is ambiguous between calibrated and anchored, and the ratchet predicts anchored.

**The discipline (symmetric — this is NOT a license to deflate).** The ratchet distorts in both directions: a recent skeptical arc over-weights deflationary readings; a recent pleasant surprise (e.g. a joint-forcing result like §B.2.236's SC→gauge+Cabibbo+generations) over-weights it as the headline. The corrective is not "be more skeptical" — that would itself be recency capture by the latest (skeptical) turn. It is:
1. **Reference class is the recency-invariant anchor.** "Foundational derive-everything programs; decades each; none yet established" does not depend on which sub-result was worked on last, and is not generated by the program's own activity. When the internal narrative (momentum, engines built, results found) and the external reference class point different ways, the reference class is the less-contaminated reading.
2. **Volume is not progress.** A history that *feels* like momentum is exactly what the ratchet produces. The core epistemic situation — unverified retrodictions, the open boost sector, no external review, one currently-adverse falsifier (DESI) — is the state to compare against, and it is roughly unchanged across many sessions, regardless of how much intricate work has accrued.
3. **Periodically rebuild from the oldest claims.** On the §A.9 re-audit cadence, re-examine the *least-recently-audited* load-bearing claims without reference to recency — they are where a quiet error survives longest. Currently overdue: SM §6 (the A·B "numerical coincidence (8,6)" hedge), the GR ℏ gap-equation circularity rebuttal, Substratum.md, Main.md. NEXT_STEPS item 4 is the operational instance of this rule — now methodologically motivated, not mere completeness.
4. **Do not move the bands on a meta-insight.** This entry does not move them. Bands move only on band-moving *evidence* (a run, a referee, a closed integral) or a deliberate from-scratch rebuild — never on a reinterpretation, in either direction. Complements §A.17 (bands as proxy) and §A.9 (re-audit cadence).

---

## §A.19 Read the whole framework before concluding — the answer is often already elsewhere in it
The framework is large (cross-referenced companion papers — Main, SM, GR, Substratum, Structure, plus the book and applied papers) and its answers are DISTRIBUTED: a question raised in one paper is frequently resolved in another, or in a later remark of the same paper. Before concluding — and ALWAYS before any NEGATIVE or GAP claim ("the framework is silent on / omits / never addresses / contradicts X") — search the full corpus for X and read what it says. A gap found by partial reading is PROVISIONAL until the whole corpus is checked.

**Motivating instance (§B.2.253).** While reading the GR prediction sections, claimed the framework was "silent" on Lorentz violation. It is not: SM.md §3.1 treats it in depth — linear LV forbidden by cubic symmetry (no $O(k^3)$ term), the $-2/15$ quadratic coefficient pre-registered, and the radiative-stability problem flagged honestly and tied to the coarse-graining map. The "silence" was an artifact of not yet having read the right paper; the negative claim was simply wrong and would have mis-stated the assessment.

**Operational form.** "Read the entire framework" is not literally re-reading 1.25 MB before every sentence. It is: (i) for any conclusion the framework plausibly bears on, and unconditionally for a gap/omission/contradiction claim, grep the full manuscript corpus (all companion papers, not just the one in hand) for the relevant terms first; (ii) treat the conclusion as provisional until that search returns; (iii) follow the cross-references — answers routinely live one paper over (LV is in SM, not GR; the coarse-graining map spans SM §3.1 / §4.7.1.1 / §4.7.1.2; the gauge measure spans §6.5 / §7.5 / §4.2).

**Symmetric, and not a rubber stamp.** This cuts both ways: do not over-claim a gap (the LV error), and do not assume the framework has addressed something without finding where. It is NOT a license to assume the framework is always complete or correct — a real gap is still real after a full read (θ₀'s missing taste vertex and the gauge-measure map both survived the corpus check). The rule forbids only concluding BEFORE the check. Complements "trust the filesystem over summaries," §A.16/§A.17 (build freely, let gates verify), §A.18 (recency ratchet), and §A.9 (re-audit cadence).

---

## §A.20 Do not fear multi-session challenges — decompose and plan them methodically, while holding that a plan is not progress
The size or duration of a problem is not a reason to avoid it, shrink it to fit one session, or treat "the next step is offline/external" as "stop." The framework's hardest open problems — the UV-smearing characterization of the coarse-graining map (§B.2.254), the boost-sector emergent-Lorentz campaign, the Phase-1 confinement run — are genuinely multi-session and partly external. That is a reason to STRUCTURE them, not to defer them indefinitely.

**Methodical decomposition.** Plan a multi-session challenge by: (i) decomposing into PHASES with explicit success/failure GATES — no phase is trusted until its gate passes (§A.16/§A.17); (ii) labelling each phase by where it must run — in-session, offline-batch (§A.13), or external — and not pretending an offline/external phase can be completed in-session; (iii) persisting the plan, the resumable state, and the handoff artifacts (NEXT_STEPS, campaign docs, the off-repo journal's resume marker) so any future session resumes cleanly without re-deriving context; (iv) building freely toward each gate (engines, calibrations, scaffolds) so the offline/external steps are TEED UP, not blocked on missing infrastructure.

**The line that holds simultaneously (with §A.18).** A methodical multi-session plan is NOT itself progress. Decomposing, scaffolding, and persisting a plan are 0pp; the binding constraint moves only when a GATE actually passes (a run completes, a derivation closes, a referee weighs in). Boldness about SCOPE must not become inflation about STATUS. This is the inverse failure mode to §A.18's: §A.18 warns against mistaking volume for progress; §A.20 warns against mistaking a problem's difficulty or scale for a reason to stop. Both errors end in the same place — the binding constraint unmoved — and the correct posture splits the difference: take on the big problem, structure it across sessions, report its status honestly at each gate.

**"Stopping point" = handoff, not abandonment.** A correctly-identified stopping point means the next gate lives offline or externally, the in-session phase is complete and persisted, and the right move is to run/route it — not to generate another in-session lap. Plan the campaign so that handoff is clean and the offline/external phases are unambiguous and resumable. Complements §A.13 (offline runs), §A.16/§A.17 (build freely, gates verify), §A.18 (volume ≠ progress), §A.19 (read the whole corpus first).

---

## §A.21 A numerical probe's SIGN can be an artifact — require an exactness/symmetry control before trusting a probe's direction
A toy/numerical probe can return a confident but WRONG-SIGNED verdict if it rests on an unfaithful approximation, and the error can survive several turns of interpretation. Before trusting the DIRECTION of a probe's result (sign, presence/absence of an effect — not just its magnitude), run an exactness or symmetry CONTROL that checks whether the modeled operation preserves what it provably must.

**Motivating instance (§B.2.259→261).** Probe B (§B.2.259) used a STATIC spatial Schur kernel paired with a separate plain time kernel and concluded that the spatial trace-out radiatively induces boost-sector Lorentz violation (η≠0); this drove an adverse lean across two turns (§B.2.259/260). The first-principles check (§B.2.261) showed it was an ARTIFACT: integrating out the hidden sublattice is an EXACT change of variables, so the faithful (worldline) trace-out must preserve the dispersion (c=1) — confirmed analytically and numerically (c²: faithful ≈ 1.0 vs the static approximation's spurious ≈ 2.0). The probe's normalization had hidden a factor-2 distortion, leaving its residue as a fake signal.

**The control that would have caught it.** "Does this operation preserve the quantity it provably must?" A faithful trace-out (exact partial path integral) cannot create LV, so integrating out a sublattice of a known-Lorentz-invariant lattice must return c=1. Had Probe B run that control, the static setup's c²=2 would have flagged it as unfaithful before its η was ever interpreted.

**Operational form.** For any numerical probe whose VERDICT will be trusted: (i) identify an exact invariant or symmetry the modeled operation must respect; (ii) construct a control input whose answer is fixed by that invariant; (iii) confirm the probe returns the known answer on the control BEFORE trusting it on the real input. Magnitude-only robustness (varying N, fit window, mass — as §B.2.259 did) checks numerical CONVERGENCE, not FAITHFULNESS; an unfaithful-but-converged probe converges to the wrong answer. Complements §A.16/§A.17 (build freely, let gates verify): the gate for a probe's SIGN is an exactness/symmetry control, not just convergence. Kin to §A.19 (read before concluding) — both guard against confident conclusions from incomplete checks.

---

## §A.22 A conclusion that shifts a result's VALENCE needs a NEW result behind it — re-narration is not evidence, in either direction
The recurring failure mode across this audit is not a bias toward optimism or toward pessimism specifically; it is a willingness to MOVE A RESULT'S VALENCE — toward "stronger / vindicated / resolved" or toward "more exposed / falsified / over-claimed" — by RE-NARRATING a fact already in hand, with no new computation, representation-theory result, or external input behind the move. The two directions are the same error in different clothes. Documented instances: the four optimism-toward-good-news episodes of the May arc; the §B.2.442dj k_F "more exposed / ~10^15 tuning / near-falsification" reversion (a worst-case coefficient asserted as settled when it was precisely the uncomputed quantity); and §B.2.477es, where re-examining the arrow/Boltzmann sector produced a fresh "§397 mildly over-claims" finding that dissolved on contact with the already-recorded analysis (the deceptive small Boltzmann brains are structurally excluded by C2; the surviving large fluctuations are veridical observers, hence not the Boltzmann-brain problem at all).

**The tell.** A valence-shifting conclusion whose entire support is a paraphrase of something already known — "this really means the framework is more/less exposed than stated" — with no result dated to the current turn. If the only thing that changed is the framing, the valence must not change.

**Operational form.** Before recording any conclusion that moves a result toward favorable or unfavorable: (i) name the NEW result it rests on (a computation, an exact/symmetry control per §A.21, a checkable rep-theory fact, an external review); (ii) if there is none, hold the valence fixed and record only the structural observation; (iii) apply the SAME scrutiny to a framework-favorable conclusion as to an unfavorable one — favorable results get held to the bad-news standard (as in §B.2.449dq), unfavorable ones to the good-news standard; (iv) keep the COST axis (does a signature carry a live empirical price — typically the open, arbiter-gated question) distinct from the STRUCTURAL status (what the fact is — often already settled), and never let a cost claim stand in for a status claim or vice versa.

**Why it binds here.** Internal work cannot raise Correctness and can lower it only via genuine falsification (§A.1, the bands discipline). A re-narrated valence shift therefore either fakes a Correctness gain (favorable direction) or manufactures a falsification the evidence does not support (unfavorable direction); both corrupt the one thing the audit exists to produce — a precisely calibrated map of what is actually derived versus assumed. This is the third member of a set: §A.18 is volume ≠ progress, §A.20 is difficulty ≠ reason to stop, and §A.22 is valence ≠ evidence. Kin to §A.19 (read before concluding) and §A.21 (control a probe's sign before trusting its direction).

---


### §A.23 Correctness vs consistency: the mechanism, refined
Refinement of the blunt rule "only external review moves correctness". Precise version:
- A result sits on the CORRECTNESS axis iff it is a NOVEL EMPIRICAL CONFRONTATION: a framework
  output (not fit to the data) compared to an INDEPENDENT measurement. On the CONSISTENCY axis iff
  it confirms the framework's claims follow from its premises / are internally coherent.
- EXTERNAL REPLICATION/REVIEW *banks* a result on whichever axis it already sits; it does NOT
  convert consistency into correctness. Reviewing a derivation-confirmation banks consistency;
  reviewing a novel empirical confrontation banks correctness.
- Therefore correctness gains are possible from ANY layer that yields a novel empirical confrontation
  (A2 gauge MC; substratum loop-level LV vs experimental bounds; cosmological nu vs DESI), not only
  from peer review of the manuscript. Re-derivation / re-narration / tooling / pre-registration still
  move NO band. Confirmation is provisional until replicated; falsification banks more readily.
- CEILING on all of them: empirical support raises "consistent with observation", never proves
  existence/uniqueness of the substratum. Bands UNCHANGED by logging this (it is methodology, not a result).

### §A.23.1 Guard: the mechanism generalizes, the PROPERTY is per-item
A.23 ("correctness = novel empirical confrontation, any layer; replication banks the axis a result
already sits on") must NOT be misread as "every replicated simulation moves correctness." The
discriminator is whether a NOVEL EMPIRICAL CONFRONTATION is in the loop, not whether it is a
simulation or whether it is reviewable.
- HAS a correctness route (novel output vs independent measurement): production A2; loop-level
  emergent-LV vs experimental bounds; (weakly) trace-out -> Born-rule emergence.
- CONSISTENCY even when fully replicated (no measurement in the loop): code-vs-code cross-checks;
  classical-automaton emergence; exact-algebra batteries. Replication certifies "the math/code is
  right", not "the world is this way".
- ENABLING (infrastructure feeding a confrontation): framework ports, reviewer packaging.
- RETRODICTION wrinkle: derived value vs KNOWN observed value = weak/discounted correctness
  (already in the band), not consistency.
- COMPOUNDING (the true core of "more than consistency"): a large body of externally-replicated
  CONSISTENCY results does not convert to correctness, but it raises the framework's prior
  plausibility and the seriousness/credibility the genuine correctness tests receive. Consistency
  work is a FORCE MULTIPLIER on the correctness tests, not a direct band-mover.
Bands UNCHANGED by logging this (methodology, not a result).

### §A.24 OI-aware external comparison (raw vs inferred; checkable, never immunizing)
When comparing OI to external theoretical/experimental data, account for OI's QM-emergence
(measurements = trace-out projections, not collapses) and observational incompleteness (embedded
observer's partial access; the dark/invisible sector is a DESCRIPTION ARTIFACT, not new substance).
PROCEDURE:
1. CLASSIFY the datum.
   (a) RAW/DIRECT (baryonic gas/stellar mass, lensing deflection, decay rates, spectral-line and
       CMB-peak POSITIONS) -> OI must reproduce as-is.
   (b) FRAMEWORK-DEPENDENT INFERENCE (dark-matter mass; Sigma m_nu under LambdaCDM; w(z) under a DE
       ansatz; CDM peak-HEIGHT interpretation; anything via standard QM measurement axioms)
       -> RE-DERIVE under OI's assumptions BEFORE declaring a tension.
2. The OI-corrected prediction must be SPECIFIC and CHECKABLE (move a number derivably).
3. ABUSE-GUARD (load-bearing): a blanket "observational incompleteness explains it" is NOT a defense
   and is disallowed -- it would make OI unfalsifiable, which yields an UNDEFINED correctness, not a
   high one. If the OI-corrected prediction cannot be computed, status = "open/uncomputed", NEVER
   "consistent". UNCOMPUTED RECOVERY IS NEVER SCORED AS A MATCH, and never re-inflates a band.
4. SYMMETRIC: applies both directions -- can DISSOLVE tensions that are artifacts of non-OI inference
   AND REVEAL tensions where OI predicts a deviation in a raw quantity the standard analysis averages out.
Bands unchanged by logging this (methodology, not a result).

### §A.25 Whole-corpus propagation & consistency check (before any status/claim edit lands)
TRIGGER: any edit that changes a CLAIM, its CLASSIFICATION (status/layer/tier; "theorem / derived /
forced / open / hypothesis / conditional / retrodiction"), or a NUMERIC value.
MOTIVATION (cross-artifact audit, batches 1-9): the dark-energy "theorem-level" overclaim recurred in
7+ places across GR / Substratum / book / FULL / Explainer -- each reader agent saw only its own range,
so the first fix (papers) left the book asserting the stronger claim for weeks; and the REVERSE also
occurred -- the book (ch08) was AHEAD of the papers on the Cabibbo c_λ closure. Single-location edits
silently desynchronize the corpus in either direction.
PROCEDURE:
1. GREP THE WHOLE CORPUS, not the file at hand. Before assuming an occurrence count, grep every
   papers/*.{md,tex}, book/*.md, book/FULL.md, and the derivatives (Explainer, README/journal,
   appendix status tables) for the flagged phrase AND its paraphrases/symbols. A shared claim recurs in
   abstracts, section bodies, §9-style conclusions, summary tables (§7.6 / appendix-a G-rows),
   cross-reference remarks, and the book mirror.
2. IDENTIFY THE AUTHORITATIVE ANCHOR, then propagate FROM it. The maintained / most-careful statement
   (usually the body, or a referee-grade "Status" note) governs; `git log -1 --format=%ci -- <path>`
   settles vintage when unclear. Propagation runs BOTH directions -- the book can lag OR lead the
   papers; check, do not assume.
3. MIRROR EVERY MIRROR. FULL.md duplicates each chapter -- a chapter edit MUST be mirrored into FULL.md
   (and vice-versa). Companion papers that restate a shared claim (SM ↔ GR ↔ Substratum ↔ Structure)
   must agree. Every summary / abstract / conclusion restatement must match the body's graded status.
4. PRESERVE, DON'T BLANKET-REPLACE. A flagged phrase can have legitimate non-target uses (e.g.
   "theorem level" is correct for the characterization theorem and the Brandner 2025 theorems; only the
   dark-energy magnitude was the overclaim). Verify each hit's context before editing it.
5. REGENERATE OR FLAG DERIVED ARTIFACTS. .tex/.pdf are generated from .md; after a content edit either
   regenerate them (pandoc + xelatex; see the build recipe / unicode-fix.tex) or explicitly flag them
   stale in the SAME commit. Never leave a distributed PDF silently inconsistent with its source.
6. VERIFY POST-EDIT. Re-grep to confirm zero stale occurrences remain AND that the legitimate uses
   survive; state the surviving count.
ABUSE-GUARD (load-bearing): "I only edited the one place I was looking at" is precisely the failure this
rule exists to prevent. An edit to a shared claim is NOT complete until the whole-corpus grep is clean.
Bands unchanged by logging this (methodology, not a result).
