# Composition and observer access: finite-depth instrument contract

Research draft, 24 October 2026. Consistency axis only. This report proves a
conditional composition statement; it does not claim that the native lattice
meets its hypotheses. No premise, certification, or manuscript status is adopted.

## Result: what one reusable interface must establish

Let X_i be the complete physical boundary state at stage i: both time slices
needed by the native rule, the carrier, residual memory, future apparatus banks,
and anything that can affect an allowed later observation. A boundary law mu is
an unnormalized nonnegative measure; its total mass is its branch probability.
For each available setting a and complete public record increment r, let
K_i(a,r) map input measures to output measures. These are the actual physical
transition kernels; summing over r preserves mass. Failures, heralds, timing,
and accessible intermediate ticks belong to r. Stopping can be padded with an
absorbing state and a distinguished no-new-record symbol.

Let C_i be a cone of admissible boundary measures containing the initial law
and closed under every allowed K_i(a,r). A fixed linear decoder D_i on the span
of C_i maps its elements to positive semidefinite quantum operators, with
Tr D_i(mu)=mass(mu). It is fixed by the interface, not chosen after reading a
history. Positivity is required on C_i, not silently on every ontic point mass.
Let I_i(a,r) be the reference quantum instrument, including its declared record
refinement and failure outcomes. The local composition obligation is

    D_(i+1)(K_i(a,r) mu) = I_i(a,r)(D_i(mu))                 (1)

for every admissible mu, allowed a, and complete record r. Native boundaries
must also physically fit: the output of stage i is an allowed input of stage
i+1, including its neighboring state and resource correlations. D_i is a
mathematical comparison map; it is not an additional physical decoder or gate.

**Conditional theorem.** If (1), initialization D_0(mu_0)=rho_0, and the stated
physical/access closure hold, then every finite adaptive protocol over this
menu has the same full record law as its reference instrument protocol. Each
record branch has the reference outgoing decoded operator. Any allowed
terminal carrier test has the reference joint law if its effect is also
intertwined by D. The theorem does not identify latent physical states.

**Proof.** For a history h=(r_1,...,r_i), let mu_h be its unnormalized physical
branch measure and sigma_h its quantum branch operator. Initially the claimed
identity is initialization. If D_i(mu_h)=sigma_h, the controller selects the
same a(h) from the same public history in both models. Equation (1) gives
D_(i+1)(mu_(h,r))=I_i(a(h),r)(sigma_h)=sigma_(h,r). Induction proves the branch
identity. Taking traces proves every history probability, including zero-mass
and failure branches without division or postselection. Applying any matched
terminal effect proves the joint terminal law. Randomized controllers follow
by the same common controller kernel and linearity. This is a sufficient
contract, not a claim that every operationally equivalent implementation must
admit this particular decoder. QED.

## Fresh resources: a sufficient route to the contract

At the actual use boundary, a seed U may be averaged with its advertised law
nu only after establishing P(U | H=h, X_relevant=x)=nu on every reachable
positive-probability pair. Here X_relevant includes all variables used by the
stage, not merely the visible carrier. Conditional independence given the
public history alone need not suffice if the seed remains correlated with a
hidden input. An independent initial seed bank supplies this condition only
when earlier dynamics and access have not used it or conditioned on it in a
way that changes the relevant joint law. Alternatively retain the seed inside
the complete boundary and verify (1) directly; statistical freshness is a
sufficient construction method, not necessary for every possible instrument.

## Consequence for the native-Y construction

The clean code (0,0,y) at R+7 on #910 supplies a candidate operand on its native
family. It does not supply K for a later reset or the closed boundary cone C.
The earlier informative prefix (u,u,1), the two time slices, neighboring
fields, and old-record resource banks must be included in an application of
(1). An inaccessible prefix may remain private under a stated access policy;
it cannot be erased from the physical boundary if it can affect later outputs.
The calibrated post-Y 5:3:2 law is a reference requirement, not a consequence
of this theorem. The theorem does not derive readiness, settings, clocks,
calibration, or the access policy.

## Composite systems and the scope of equivalence

A serial theorem for one menu does not prove tensor-product composition,
entangled preparations, independently selectable local settings, or Bell
statistics. Those require a composite boundary and reference map with matched
local operations and complete accessible joint records. Treating both wings
as one unrestricted controller does not establish physical subsystem locality.
Conversely, under measurement independence and Bell-local factorization,
the CHSH ceiling applies; a candidate must identify the actual causal premise
it changes, not merely call its description emergent. These are application
obligations, not a general impossibility claim about OI.

The contract gives one direction: specified native protocols reproduce the
specified reference protocols. Full operational equivalence also requires
coverage of the target protocols and an audit that every permitted native
protocol is represented on the reference side. Enlarging access changes that
second condition. An unbounded-depth theorem further needs one compatible
family of realizations/resources and interfaces, rather than a new unrelated
finite construction for each depth.

## Sources and status

- Programme acceptance rule and open obligations: #885, commit
  `2d555f17c23bea31d32b3f5eb4c49d245b413a76`,
  `verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/INTEGRATION.md`.
- R0/R1/R2 and composite-system limitation: the same commit, `mc-node6/NODE.md`,
  sections 0 and 1, relative to that programme directory. Its cited results are
  inherited context, not independently re-proved here.
- Native clean Y and resource boundary: #910, commit
  `5f6786d6f02605f8e8821a536b678495e19015da`,
  `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/CURRENT-HANDOFF.md`.
- Literature check before the proof: Chiribella, D'Ariano, Perinotti,
  *Theoretical framework for quantum networks*, Physical Review A 80, 022339
  (2009), DOI https://doi.org/10.1103/PhysRevA.80.022339,
  https://arxiv.org/abs/0904.4483. Its network/memory-channel framework is
  relevant background; the elementary induction above is self-contained and
  does not import a claim of native realizability from that paper.

The theorem is a written proof, not Lean certification. This initial checkpoint
precedes the exact countercontrol suite and independent review. It is a scoped
active research result, not a completed native application or full equivalence.
