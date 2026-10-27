# SM Theorem 3: restricted converse and the boundary of the claim

Status: author-derived mathematical proof with bounded exact computational checks; independent review pending. No manuscript, coverage status, Lean module or CI configuration is changed. The earlier proposed one-way replacement is superseded by the two precise statements below; its history remains in the preceding commits.

## Source pins and evidence boundary

Sources inspected at audit parent `ccdbab630baba6d25474b241d783f750c3c87b60`:

- `papers/SM.md`, section 4.3: the displayed equivalence refers to the lattice dynamics, while the adjoining remark distinguishes a Laplacian self-term from a Dirac mass term.
- `verification/lean/OI_Structural_Core.lean`, `Chiral.center_anticommutator` and `Chiral.mass_square`. The former proves an identity in the custom class `Rng`; it does not conclude a biconditional or coefficient uniqueness. Source inspection is not a fresh kernel run.
- `verification/lean/ROADMAP.md`, generator-relations layer, and `verification/lean/structural_chain_probe.py`, C2/C3: their narrower object is the staggered Dirac operator. C2 constructs B=2D from signed symmetric differences; C3 checks mass/offset deformations.

The new results here are elementary algebra, not a new physical prediction or a claim of novelty. They resolve the logical gap for a specified operator family. They do not supply the microscopic-to-observer map.

## 1. General commuting-perturbation theorem

Let A be a unital associative algebra over a field of characteristic different from two (in particular the real or complex numbers). Let epsilon, D, C belong to A and assume

    epsilon^2 = I,
    D epsilon + epsilon D = 0,
    C epsilon = epsilon C.

Then

    {D+C, epsilon} = 0  if and only if  C = 0.

**Proof.** Expanding gives

    {D+C, epsilon}
      = {D,epsilon} + C epsilon + epsilon C
      = 2 C epsilon.

If the left-hand side vanishes, multiply on the right by epsilon to get 2C=0, and divide by two. The reverse implication follows immediately from the assumed anticommutation of D. This proves both directions.

More generally, in the custom ring setting it is enough that x+x=0 implies x=0 for every x. Merely saying that an arbitrary ring has characteristic other than two is not enough: it need not exclude additive two-torsion. No assumption that both parity eigenspaces are populated is needed to infer C=0.

**Application to a fixed staggered branch.** Take epsilon to be site parity times the identity on each site's internal space. Any on-site operator C then commutes with epsilon, even when it mixes internal components. If the fixed off-site staggered operator D anticommutes with epsilon, exact anticommutation of D+C is equivalent to the absence of that on-site operator. This is the precise operator-level sense in which a center-free/chirality equivalence can be retained.

This is not an equivalence for arbitrary center-free lattice updates. A zero diagonal alone does not make an arbitrary matrix chiral: with epsilon=diag(1,1,-1), a nonzero matrix entry between the first two sites has zero diagonal but anticommutator equal to twice that entry. The fixed opposite-parity hopping structure is load-bearing.

## 2. Scalar coefficient-identification corollary

In a nonzero vector space over the same field, suppose epsilon has both a nonzero +1 eigenspace and a nonzero -1 eigenspace. For scalar coefficients m and p, set

    C = m epsilon + p I.

Then

    {D+m epsilon+p I, epsilon} = 0
      if and only if m=0 and p=0.

**Proof.** Section 1 reduces the question to C=0. Applied to a nonzero vector in each parity sector, this gives respectively m+p=0 and -m+p=0. Addition and subtraction give p=m=0. The reverse direction is immediate.

Equivalently, the existing Lean identity specializes to

    {D+m epsilon+p I,epsilon} = 2m I + 2p epsilon.

The extra eigenspace hypothesis is needed for unique scalar coefficients, not for section 1. If epsilon=I, then m=1 and p=-1 give C=0 with neither parameter zero. Nor does the generic Lean identity force operator-valued m,p to vanish separately: take M=I and P=-epsilon. They commute with epsilon and are nonzero, but M epsilon+P=0 even with both parity sectors present.

On a nonempty ordinary periodic hypercubic lattice with every extent even and at least two, both site parities occur. Nearest-neighbor hopping changes parity, including across boundaries. Odd periodic extents do not support that argument. These are explicit lattice assumptions, not consequences of observational incompleteness.

## 3. Why a second-order self-term is a different object

With the repository's convention

    B = 2D = sum_mu eta_mu (T_mu - T_mu^{-1}),

the standard staggered factorization on the tested even periodic lattices is

    B^2 = sum_mu (T_mu^2 + T_mu^{-2} - 2I).

For extent four, the shifted terms have no diagonal entries, so diag(B^2)=-2d I while diag(B)=0 and {B,epsilon}=0. Thus a nonzero central term in the squared operator coexists with exact first-order chirality. This is a concrete counterexample to identifying every second-order self-term with a chirality-breaking first-order mass/offset.

The exact checker independently constructs the signed nearest-neighbor operator and the second-difference operator, compares their matrices, and checks chirality and the diagonal. It does not use the desired square identity as its operator constructor. Tested dimensions d=1,2,3,4 at extent four have 4,16,64,256 sites and squared diagonals -2,-4,-6,-8.

This construction does not identify a particular time-discretized update coefficient with the SM remark's C=2(1-d), and does not establish a general observer projection or an interacting continuum chiral theory. The distinction suffices without those stronger claims.

## 4. Bounded exact checks and countercontrols

`restricted_converse_probe.py` uses only standard-library rational arithmetic and raises explicit exceptions, so checks are not disabled by `python -O`.

The finite check specification was written locally before execution: 81 two-by-two scalar cases over {-1,0,1}, two rational cases, 243 three-by-three commuting-block cases, four even periodic lattices, and ten countercontrols. This is an exploratory smoke check, not an owner-designated frozen round or a CI attestation.

Results in `RESULTS.json`:

- 83 scalar cases and 243 general commuting-block cases pass; the latter include non-diagonal even-parity blocks.
- Four explicit lattice square/chirality checks pass.
- Ten countercontrols pass: dropping commutation, baseline anticommutation, or grading invertibility; characteristic two; a single parity sector; operator-coefficient cancellation; and four odd-periodic boundaries with d=1,2 and extent 3,5.
- Normal and optimized execution produce byte-identical JSON. Python compilation succeeds.

Reproduction:

    python restricted_converse_probe.py > actual.json
    python -O restricted_converse_probe.py > optimized.json
    cmp actual.json optimized.json
    cmp actual.json RESULTS.json

Script SHA-256: `0ddc0d9dd905d9aa59f8e5dabc5e837b6c04497325279bdef60a9bb275481d60`.
Result SHA-256: `e9031340988e11ed0db9d1433fcaaae4f4b1e122a90edbe0ec52c386baec77c7`.

The universal support is the proof in sections 1-2, not the finite count. No Lean compiler or lake is installed in the execution environment. No new kernel certificate, successful full repository gate, or independent review is claimed.

## 5. Proposed manuscript replacement, not applied

> **Theorem 3 (on-site terms and staggered chiral symmetry).** On the stated staggered branch, let the fixed hopping operator D satisfy {D,epsilon}=0 with epsilon^2=I. Over the real or complex numbers, an on-site perturbation C commuting with site parity preserves this anticommutation exactly when C=0. For C=m epsilon+p I with scalar m,p and both parity sectors nonzero, this is equivalent to m=p=0.
>
> **Proof.** The anticommutator is 2C epsilon, so multiplication by epsilon and division by two recover C. In the scalar family, restriction to the two parity sectors identifies both coefficients.
>
> This is a statement about the first-order staggered operator. Its square may have a nonzero Laplacian diagonal without breaking the symmetry. No converse relating an arbitrary microscopic update's center dependence to the projected observer dynamics follows from this result.

A manuscript correction must preserve the valid restricted equivalence and carry these hypotheses. It must not silently substitute this elementary identity for a missing physical derivation, or declare all chirally symmetric interacting theories massless.

## 6. Review and propagation boundary

Before accepting a manuscript/status patch, independently check the algebra, exact probe, definition of on-site/center-free, lattice boundary hypotheses, and the correspondence to the precise SM branch. Inspect the theorem's dependents in SM, Main, book chapters and FULL, Explainer or its legacy location, the roadmap, probe descriptions, and the coverage ledger. These are targets, not a claim that a full propagation audit has already been completed.

Formalization should keep two separate conclusions: C=0 under additive two-torsion-freeness; and scalar coefficient uniqueness under both parity sectors. Existing identities are not relabelled as certificates of these new statements. A fresh exact-head CI/axiom record is still required for any later formal-status upgrade.

## 7. External source check

Simon Catterall, *Chiral lattice fermions from staggered fields*, Physical Review D 104, 014503 (2021), section II, equations (1)-(7), supplies the conventional staggered phases, symmetric difference and parity projectors used for comparison. DOI: 10.1103/PhysRevD.104.014503. Those equations were read in the parsed primary-source PDF; the screenshot fetch failed. No visual/table evidence is relied on, and this is not a claim to have read the whole paper. The converse here is proved directly, not attributed as a new result.
