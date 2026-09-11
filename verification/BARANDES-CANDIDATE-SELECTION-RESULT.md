# Track B act 3 — candidate selection and uniqueness: result

Frozen preregistration: commit `2fb894192bc9ae3bddc8bfa19301eeee1195a3fc`, blob
`64e07da7f20f362386da01087a260723a2213e68`, merged to `main` by PR #564.

Executed from `main` at `9ad37eb60c03d09fe44b18dc97ccd46e507e134f`, the merge of that freeze.
Kernel module: `verification/lean-mathlib/OIBridge/CandidateSelection.lean`.

## Outcome

**`CU1a` — the named rules are underdetermined.**

C1 and C2 both close. Two independently admissible extraction rules give **different** visible
candidate propagators on one lawful representation, with the representation held **fixed**. C4
closes on the non-unique side as a consequence, exactly as the freeze predicted it must: C1 makes
both named rules admissible, so the C2 witness instantiates `AdmissibleNonUnique` directly.

The prediction recorded before proving was **`CU1a` at roughly two-to-one against `CU2`, with
`CU1b` the fallback and `CU3` unlikely**. It **held**, on the ground it named: `initWeight` reads
`Q.init` while `uniformWeight` reads only the fibre's cardinality, and nothing in `IsLaw` or
`PositiveRootMass` ties those together.

## The four targets

**Seven named results.** Every one prints `[propext, Classical.choice, Quot.sound]` and nothing
else; the `#print axioms` lines are in the module and the build log carries the kernel's own answer.

| target | result | status |
|---|---|---|
| C1 | `initWeight_admissible` | closed |
| C1 | `uniformWeight_admissible` | closed |
| C1 | `candidateOf_isRowStochastic` | closed |
| C2 | `candidate_rules_disagree` | **closed** |
| C3 | `candidateOf_initWeight_eq_rooted` | closed |
| C3 | `candidateOf_uniformWeight_padData_eq` | closed |
| C4 | `admissible_nonUnique` | closed |

Definitions and **the signatures** exactly as frozen, binder for binder. All eight frozen
definitions are present; two of the frozen theorem statements are deliberately **absent**, and that
absence is the record of which outcomes were not reached — see below.

### C1 — both rules are admissible, and admissible rules give candidates

The sign clause of `Admissible` is load-bearing here, and the round would have been wrong without
it. Writing `R_b(j) = ∑_{b' ∈ fibre j} bornPow n b b'` for the visible row of a basis point,

    candidateOf Q μ n k j = ∑_{b ∈ fibre k} μ k b * R_b(j),

so support and normalization force the row **sums** on their own — which is what disguised the gap —
while leaving each **entry** an affine rather than convex combination of the fibre's visible rows. A
signed weight `(2, −1)` on two basis points with differing rows gives a row `[2, −1]`: normalized,
and negative.

`IsLaw`'s second conjunct supplies `∀ b, 0 ≤ Q.init b` and `PositiveRootMass` the denominator, so
`initWeight_admissible` discharges nonnegativity from hypotheses the target already carried.

### C2 — the decisive target, and it closed

The witness has visible carrier `Fin 2`, basis `Fin 3`, readout sending basis points `0` and `1` to
the visible value `0` and basis point `2` to `1`, evolution the transposition exchanging basis points
`1` and `2`, and initial law `(1/2, 1/4, 1/4)`. It is constructed **inside this theorem's proof**
rather than named at top level, because the freeze fixes that the round introduces exactly eight
definitions and a named witness datum would be a ninth.

Two requirements, both necessary. The fibre over `0` must carry two basis points **whose visible
rows differ** — the transposition fixes basis point `0` inside that fibre and moves basis point `1`
out of it — and the initial law must weight those two points **unequally**. The visible carrier must
also have at least two points: on `Fin 1` the single entry of `candidateOf` *is* the row sum, hence
`1` for every admissible weight whatever the basis is.

At one elapsed step the `(0,0)` entry reduces to the weight the rule assigns to basis point `0`
alone, so the two rules are read off directly: `2/3` for `initWeight`, `1/2` for `uniformWeight`.

**No appeal to representation freedom is made or needed.** That is what makes this target reachable
at all given the scoping pass, and it is why `CU1a`'s licence is about the bridge rather than about
padding.

### C3 — the padding mechanism, at exact scope

`candidateOf_initWeight_eq_rooted` is essentially definitional: the init-weighted candidate **is**
the rooted family, which is why an invariance round built on that extraction would have been vacuous.
It is stated so that the second theorem is seen not to be.

`candidateOf_uniformWeight_padData_eq` is the content. `padData` multiplies every visible fibre by
`Anc`, so the uniform weight really does change — and the candidate does not, because the ancilla
factor marginalizes to one at every horizon. The merged route it consumes is the general-horizon
one: **`padData_bornPow`** for the factorization at every horizon and **`sum_ancPow`** for the
ancilla marginal being one at every step. `padData_born` and `sum_ancBorn` are the one-step
ingredients those two are proved from, not the theorems applied here.

**This confirms the scoping pass's Finding 2 for the uniform rule**, which that pass recorded as
provisional and explicitly not a theorem. It is now a theorem, at that scope and no wider.

### C4 — the admissibility conditions do not force uniqueness

`AdmissibleNonUnique` is proved. Note what the frozen statement quantifies over: **arbitrary**
admissible weights, not the two named rules. C2 could have failed on the named pair while C4
succeeded on another; it went the other way.

It is proved **from C2 and C1**, with no second witness. The freeze says the C2 witness instantiates
C4's existential directly; this is that sentence as a derivation rather than as prose, and it needs
two side facts, both supplied by C2's own payload:

- the visible carrier is inhabited, because over an empty carrier every matrix equals every other
  and the two candidates could not then differ;
- every fibre is inhabited, because `rootMass` is a sum over that fibre and `PositiveRootMass` makes
  it positive.

The second is the fact that also made `CU3` unlikely, now doing work rather than being observed.

## What was not proved

Two frozen theorem statements do **not** appear in the executed module, and the two cases are not
alike — the distinction matters and is stated rather than blurred.

**`admissible_agree`** (the `CU2` side). Not proved, and it cannot be: it is the exact negation of
what C4 established over the same domain.

**`named_rule_inadmissible`** (the `CU3` side). Not proved — and here the honest statement is
stronger than "unreached". The frozen `NamedRuleInadmissible` carries `IsLaw`, `PositiveRootMass`,
`∀ k, ∃ b, Q.read b = k` and `Nonempty V` as its own hypotheses, and asks for one of the two named
rules to fail admissibility. Under exactly those hypotheses, `initWeight_admissible` gives the first
rule and `uniformWeight_admissible` the second, so **C1's two positive theorems independently
exclude that witness.** No counterexample exists to exhibit, and that is a fact about the
mathematics rather than about the search.

The general principle still holds and is not weakened by this case: **absence of a proof is not, by
itself, evidence against a proposition.** What licenses the stronger statement here is C1, not the
absence of `named_rule_inadmissible`. Where the two come apart — as they do for a proposition C1
does not bear on — the weaker reading is the one this round takes.

The freeze predicted `CU3` unlikely and gave its ground, which the proofs bore out: `PositiveRootMass`
forces every fibre nonempty — that is what `uniformWeight` needs in order to normalize, and positivity
of the same quantity is what `initWeight` needs for its denominator. `uniformWeight_admissible`'s
explicit hypothesis `∀ k, ∃ b, Q.read b = k` is therefore derivable from `PositiveRootMass`, which is
exactly how C4 discharges it below; the hypothesis is kept as frozen and costs nothing.

No named corollary `¬ NamedRuleInadmissible` is added. It would be a new target introduced after
seeing the results, which is what preregistration exists to prevent; the exclusion above is stated as
a two-line consequence of theorems the round already proves, checkable against their statements.

## What this licenses, and what it does not

`CU1a` was reached, so the strongest of the round's three reporting licences applies. It is stated
at exactly its scope.

**Permitted, and claimed:** *the merged OI → `QfbData` bridge does not select the candidate at this
interface.* A candidate-selection principle is **required** before "OI forces this interference
discrepancy" is a well-defined family-level question. That is a requirement, not a proposal: this
round proposes no such principle and adopts none.

**Not claimed, and not available from anything here:**

- that the external framework requires an additional physical principle. Act 1 established that the
  external diagnostic discussion uses a **particular** candidate whereas this programme's
  `PDivisible` quantifies existentially over all stochastic candidates. That external construction
  may well supply the selection canonically, from the relative unitary of its own dilation. If it
  does, the eventual task is to show that **our** representation instantiates **his** construction,
  not to add a principle to his framework. Act 1's determinations are the only citation for what
  that construction does or does not fix, and this round does not extend them;
- that no neutral admissibility criterion exists. The round quantifies over no space of criteria;
- anything about representation freedom. C2 holds the representation fixed;
- that OI does or does not force quantum structure.

Nothing here identifies `candidateOf` with any external object, and nothing here is a sourcing
claim: a statement about fibre weightings and marginals sources nothing.

## Where the chain now stands

The chain Track B needs is

    OI stochastic family  →  representation  →  candidate intermediate  →  discrepancy.

Arc D round 1 settled that the **first** arrow does not determine operator content. This round
settles that the **second** does not determine the candidate either: the missing ingredient sits
one level earlier than any interference round would have looked, which is what the scoping pass
suspected and could not establish.

So an interference round cannot be well posed on this route until a candidate is selected. Two ways
forward, neither taken here and neither adjudicated:

1. show that our representation instantiates the external dilation construction, which would supply
   the selection rather than add to it — this is the mapping obligation, and it is separate;
2. select the candidate on this side, from a stated principle, and say plainly that it is an
   addition to the merged bridge.

## What remains open

- Whether some admissibility criterion other than the frozen one admits both named rules. Not asked
  here; `Admissible` was frozen before proving and Control 4 forbids reshaping it.
- Whether padding is inert for extraction rules beyond the two named. C3 settles the uniform rule
  and `candidateOf_initWeight_eq_rooted` settles the init-weighted one by construction; the scoping
  pass's Finding 3 is used as a premise nowhere.
- The mapping obligation above, in either direction.
- The horizon gap recorded by act 2, untouched here.

## Controls

No `sorry`, no custom `axiom`, no `native_decide`. No primary source consulted. No manuscript edit.
§3.6 not reopened. `BD3`, `BR3` and `RT1` neither reopened, softened nor re-derived. Arc D's
`padData_rooted`, `padData_bornPow` and `sum_ancPow` are consumed, not re-proved. No deferred Arc D
resource adjudicated, and no fifth condition.
