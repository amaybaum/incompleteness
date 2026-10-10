"""Assemble the A38 preregistration from the single proposition source (props38.json, texts38.json, witness38.json).
Placeholders @@RUNS@@, @@CONTROLS_BLOB@@, @@PROBE_BLOB@@, @@NMUTS@@, @@NPASS@@, @@PROBE_MIN@@, @@ROAD_PV@@,
@@ROAD_FL@@ are filled by fill_prereg38.py once the runs, controls.py and the probe are final. Line numbers of the
locating table are read from the D worktree at generation time."""
import json, os, pickle, re, subprocess
S = os.path.dirname(os.path.abspath(__file__))
WT = os.path.join(S, '..', 'wt-d38')
P = json.load(open(os.path.join(S, 'props38.json')))
T = json.load(open(os.path.join(S, 'texts38.json')))
WIT = json.load(open(os.path.join(S, 'witness38.json')))
E_CAND = pickle.load(open(os.path.join(S, 'deep_wit.pkl'), 'rb'))['E_all']
PR, CO = P['PROPS'], P['COMPONENTS']
def lean(key):
    return '```lean\n' + PR[key] + '\n```\n'
def q(t):
    return '\n'.join('> ' + l for l in t.split('\n'))
def line_of(path, pat):
    src = open(os.path.join(WT, path), encoding='utf-8').read().split('\n')
    for n, l in enumerate(src, 1):
        if re.match(pat, l): return n
    raise SystemExit('not found: %s in %s' % (pat, path))
def lines(path, names):
    return ', '.join(str(line_of(path, r'^(?:theorem|def|noncomputable def|abbrev)\s+' + re.escape(n) + r'\b')) for n in names)
def blob(path):
    return subprocess.run(['git', 'rev-parse', 'HEAD:' + path], capture_output=True, text=True, cwd=WT).stdout.strip()
DAE = 'verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean'
DHI = 'verification/lean-mathlib/OIBridge/DitaHierarchy.lean'
DH = 'verification/lean-mathlib/OIBridge/DitaHull.lean'
PS = 'verification/lean-mathlib/OIBridge/ProductStratum.lean'
OGR = 'verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean'
OGI = 'verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean'
TSG = 'verification/lean-mathlib/OIBridge/TwoSidedGauge.lean'
CLS = [('k1', '4 × 4', '(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15)', '(0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15)', 'the Kronecker split: blocks by `c`, classes by `b`'),
       ('k2', '4 × 4', '(0, 2, 8, 10), (1, 3, 9, 11), (4, 6, 12, 14), (5, 7, 13, 15)', 'the same four sets', 'the parity regrouping'),
       ('k3', '4 × 4', '(0, 2, 9, 11), (1, 3, 8, 10), (4, 6, 13, 15), (5, 7, 12, 14)', '(0, 6, 8, 14), (1, 7, 9, 15), (2, 4, 10, 12), (3, 5, 11, 13)', 'the mixed regrouping'),
       ('k4', '4 × 4', '(0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15)', '(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15)', 'the swapped Kronecker split: blocks by `d`, classes by `a`'),
       ('e1', '8 × 2', '(0, 2), (1, 3), (4, 6), (5, 7), (8, 10), (9, 11), (12, 14), (13, 15)', '(0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)', 'blocks by `(c, d div 2)`, classes by the parity of `b`'),
       ('e2', '8 × 2', '(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)', '(0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15)', 'blocks by `(c mod 2, d)`, classes by the parity of `a`'),
       ('t1', '2 × 8', '(0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15)', '(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)', "act 36's frozen class, `dita28` at `r28`, `c28`: blocks by the parity of `c`, classes by `(a mod 2, b)`"),
       ('t2', '2 × 8', '(0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)', '(0, 2), (1, 3), (4, 6), (5, 7), (8, 10), (9, 11), (12, 14), (13, 15)', 'blocks by the parity of `d`, classes by `(a, b div 2)`'),
       ('t3', '2 × 8', '(0, 2, 5, 7, 8, 10, 13, 15), (1, 3, 4, 6, 9, 11, 12, 14)', '(0, 10), (1, 11), (2, 8), (3, 9), (4, 14), (5, 15), (6, 12), (7, 13)', 'blocks by `(c + d) mod 2` … the twisted parity split')]
NONID = [56, 54, 26, 28, 52, 72, 48, 58, 44, 31, 34, 24, 16, 23, 16, 39, 52, 16]
def witrow(nm, form):
    w = WIT[nm + ('_col' if form == 'column' else '_row')]; p = w['p']
    pos = ', '.join('`((%d,%d),(%d,%d))`' % (i // 4, i % 4, j // 4, j % 4) for i, j in p)
    const = '`±1/16`, rational' if w['rational'] else '`z/16`'
    coef = '`%d`' % w['coef'] if w['rational'] else 'the factor `z/16` cancelled: `z · (u − 1) = 0` by `linear_combination (16 : ℂ) * key`, then `z ≠ 0`'
    return '| `%s` | %s | %s | %s | `%d`, `%d` | %s | %s |' % (nm, form, 'proportionality' if w['kind'] == 'prop' else 'rectangle (rank-one)', pos, w['e'][0], w['e'][1], const, coef)

doc = r'''# Track B act 38 — a genuine non-Diţă local escape at the product-embedded stratum point: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
''' + q(T['CLAUSE']) + r'''

## The declarations

```v3-round
round A38
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-38-local-escape/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-38-local-escape/
record AM verification/receipts/A38.json
execution A verification/lean-mathlib/OIBridge/DitaLocalEscape.lean
execution A verification/lean/dita_local_escape_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
execution M verification/ROADMAP.md
```

The record directory holds three files: this preregistration, the round's frozen controls
`controls.py`, and the result note. The receipt path is `verification/receipts/A38.json`. Every
other path the round changes is an execution path listed above. The guard,
`verification/lean/edge_rigidity_probe.py`, is not governed and is not changed: at `E` it is byte
for byte `D`'s, and `controls.py` checks that it is. The workflow changes by one shard: the round's
probe runs in its own job `probes_a38`, named `Numerical probes / A38 escape`, inserted before the
foundations shard and required by the aggregate `Numerical probes` job — its `needs` entry, its
result variable, its echo and its test line — so that the required check fails unless the probe
is green; `controls.py` checks that the workflow at `E` is `D`'s with exactly those five frozen
edits applied. The probe takes about six minutes in exact arithmetic; a shard of its own keeps the
workflow's wall time at the slowest job rather than the sum.

`ROADMAP.md` changes only on a decided outcome, and only as this file freezes: by the `P0` sentence
for the case, appended to the cell. The roadmap's section *The residual deformation space at the
product stratum*, landed before `D`, is not edited by this round.

## The objects

- **`D`** = `5949740297034d0ddc522aff9577bd1fa36fe42f`: the head of `main` after the landing of
  act 37's pull request #764, `A37-EXCLUSIVITY-PROVED`. It is certified by push run 36387732790:
  all seven jobs green, the release gate passing with thirteen receipts holding, the `Mathlib
  bridge` build green with `lean-axioms` at 4829 named results and no sorry, the guard `ALL CHECKS
  PASS`, act 36's probe reporting its `OK` line and act 37's its own. Every measurement here was
  taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A38.json`.

No other round runs beside A38 at this freeze. Should one land first, its movement of `main`
enters A38 only by reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — the exclusion is two-layered, and the layers are never merged.** The kernel proves,
for the explicit arc `Hu u = SIG ∘ u^E`, that `Hu u` is a flat unitary at every unit `u`, and, for
each of the nine factorization classes of the stratum point, that a Diţă form of `Hu u` at that
class's index maps, in either orientation, forces `u = 1`; and, as the corollary, that every
neighbourhood of `SIG` contains a realizable matrix admitting none of the eighteen forms. Those are
statements about eighteen named index maps. That **no index maps whatever** admit a Diţă form of
`Hu u` at a unit `u ∉ {1, −1}`, in either orientation, strictly or up to diagonal equivalence, is
the exact-computation layer's statement, established by the frozen probe and not by the kernel; it
is never written as a theorem of the module, and the result note, the census family and the `P0`
sentence name its layer wherever it is cited. The frozen main statement — *for every unit
`u ∉ {1, −1}`, `Hu u` admits no Diţă structure of any admissible shape, index map or orientation,
including up to the allowed diagonal equivalences* — is therefore earned by the two layers
together, and the result note says which layer earns which clause.

**Hazard 2 — the exceptional set is determined by the algebra before the freeze, and the freeze
records what it found.** The set is `{1, −1}`. The kernel statements force `u = 1` for the eighteen
structures because the obstruction each carries is a monomial `u^{±1} = 1`, found by the pre-freeze
measurement and replayed by the probe; the probe computes the candidate set of every unit at which
any structure could appear, forty points named exactly, in both orientations, and decides each by
the exhaustive search, finding a structure at `u = 1` (the eighteen) and at `u = −1` (one `2 × 8`
structure per orientation, at index maps outside the census) and nowhere else. At `u = −1` the two
structures are **certified**, not merely observed: the probe reconstructs `Hu (−1)` and its transpose
exactly from flat unitary factors and unit twists at those index maps, and the numeric search with
factor unitarity finds exactly them. The value `{1, −1}` is the design run's, asserted by the probe
at every execution commit. A different value at `E` is not a reinterpretation of the theorem: it is
the probe red with the frozen blob, a freeze failure, and the round halts. The point `u = −1` is at
distance 2 from the base point; nothing in the local statement depends on it, and the corollary's
units lie within any prescribed distance of `1`.

**Hazard 3 — the monomial calculus and its canonical names.** Every entry of
`SIG = F₄(z) ⊗ F₄(w)` is `i^p z^q w^r`, so every entry of `Hu u = SIG ∘ u^E` is `i^p z^q w^r u^k`
with `k = E(i, j) ∈ {0, 1}`. A Diţă structure — column blocks and row classes — is admitted at `u`
if and only if finitely many **monomial equations** hold: the proportionality of every two rows of
a class on every block, and the rank-one condition on the block ratios; the flat unitarity of the
factors follows from that of `Hu u`, which this round proves in the kernel for every unit `u`, and
is not a further condition. Each equation `u^k = i^p z^q w^r` with `k ≠ 0` has exactly `|k|` unit
solutions `u = ζ · z^{−q/k} · w^{−r/k}`, `ζ` a root of unity; and because `z = (2+i)/(2−i)` and
`w = (3+2i)/(3−2i)` are quotients of distinct Gaussian primes by their conjugates, they are
multiplicatively independent modulo roots of unity, so the triple `(ζ, s, t)` with `u = ζ z^s w^t`
is a canonical exact name for a point, and monomials at a point are compared exactly as such
triples. The probe uses this and nothing else for its symbolic searches; twenty of the forty
candidate points are Gaussian rational and there the numeric search of act 36's probe, with factor
unitarity, is run as a control in both orientations and must agree.

**Hazard 4 — why the candidate set is exhaustive, in both orientations, recorded as the freeze's
reading.** A Diţă form of `Hu u` at any index maps is a column form of `Hu u` or a column form of
`(Hu u)ᵀ`; the arc is not symmetric, so both are searched, the second as the column search on the
transposed exponent matrix. At a generic `u` **no** block of any of the three shapes, in either
orientation, splits the rows into proportionality classes of the right size: the generic candidate
set is empty. So a structure admitted at any unit lies at a point where some pair of rows becomes
proportional on some block without being so generically — the candidate set, computed over every
`n`-subset of columns, `n ∈ {4, 2, 8}`, every pair of rows and both orientations — and at the
candidate points the exhaustive search decides. No structure is admitted identically, none at
infinitely many units, and no index maps outside the census appear anywhere on the circle off the
forty points; at the forty points the search finds the census at `u = 1`, the two certified
structures at `u = −1`, and nothing elsewhere. This subsumes the local statement: a factorization
appearing at units arbitrarily near `1` would appear at `u = 1` itself, hence be one of the census,
each of which the kernel excludes at every unit `u ≠ 1`. The probe executes each step of this
reading; the reading itself is this file's.

**Hazard 5 — the diagonal equivalences.** Two matrices related by a permutation of rows, a
permutation of columns and unit diagonal rescalings on both sides are equivalent complex Hadamard
matrices. The permutations are the quantifier over all admissible index maps. The diagonal
rescalings are the **relaxed** form: a Diţă form of `D₁ · Hu u · D₂` at some index maps exists
exactly when the rows of every class are proportional on every block — a condition invariant under
diagonal rescaling — and the block ratios satisfy the rank-one condition up to a row-dependent
factor, `λ(a,b,c) / λ(a,0,c)` independent of `c`; the strict form is the case of a trivial factor.
At `SIG` the relaxed census equals the strict one, eighteen structures; along the arc the probe
tests the relaxed condition on every proportionality candidate at every candidate point and finds
it satisfied at `u = 1` and `u = −1` only, by the same structures. Complex conjugation carries
`SIG` to a stabilizer image of itself and a Diţă form to a Diţă form, so it adds nothing to the
quantifier; transposition is the second orientation. That is what *including up to the allowed
diagonal equivalences* means in the frozen statement, and it is the exact-computation layer's
clause.

**Hazard 6 — what this freeze does not claim.** The witness `E = A + B + C` was found by a search
over exponent matrices with entries in `{0, 1}` and a zero first row; that search was not finished
at the freeze and is not part of the round: **no count** of such lines, **no minimality** of the
support 48, and **no classification** of orbits is claimed or depended on. The decomposition
`E = A + B + C`, each piece and each pairwise sum a straight line lying identically in some census
class while the triple lies in none, is recorded by the probe as a **control** of the classifier
and as interpretation, and is not a theorem of this round; the three-parameter family
`SIG ∘ u₁^A u₂^B u₃^C` is not frozen, since its realizability would need its own multivariate
identity. Each may become a round of its own.

**Hazard 7 — the tangent space, recorded as interpretation.** The probe computes, in exact integer
arithmetic, the tangent space of unitary deformations at `SIG`: dimension 80 with the 31 gauge
directions, defect 49; the subspace along which each of the eighteen structures is admitted to
first order, of dimension 36, 46, 36, 36, 44, 44, 57, 57 or 49 by class; and that the eighteen
subspaces together span the whole tangent space. The witness is tangent and lies in none of them.
So the escape is a **nonlinear compatibility** obstruction, not a missing tangent direction: three
Diţă directions that integrate exactly to a straight line whose sum is Diţă-linear for no
structure. This is interpretation, probe-checked and kernel-free, and it licenses nothing beyond
the frozen statements.

**Hazard 8 — history.** Act 37 recorded `A37-EXCLUSIVITY-PROVED` with the exhaustion of the
hierarchy open, act 36 `A36-HIERARCHY`, act 35 `A35-DITA-STRATIFIED`, act 34 `A34-STRATIFIED`, act
33 `A33-CLASSIFIED`, act 32 `A32-NOT-RIGID`, act 29 to act 31 their product-configuration verdicts.
All stand as recorded. A decided outcome here answers the question acts 36 and 37 recorded open — it
is stated as a fact about the arc and the classes of the stratum point and is never a revision of
an earlier round's verdict: act 37's arc lies in its `2 × 8` hull, as recorded, and this round's
arc lies in none.

**Hazard 9 — vocabulary.** A class is a pair of index maps, a hull is a family of classes, a
factorization is a way of writing a matrix, a realizable matrix is a flat unitary on the carrier,
an isometry is not a symmetry, the group acting is not a symmetry group of anything physical,
covariance under it is a hypothesis this round does not assert of any law, and none is written as
the other.

***

## Provenance

The following are consumed as frozen declarations and frozen theorems, never re-proved and never
paraphrased:

- **act 12 and act 17** — `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `AdmissibleDilationAt`,
  `sh1_necessity`, `fibreGram_apply`;
- **act 23**, `OrbitLawGaps.lean` — `hadamard_z_admissible`;
- **act 24**, `OrbitGeometrySelector.lean` — `mixedTriple`;
- **act 25**, `OrbitGeometryIsometries.lean` — `transpose_unitary`;
- **act 26**, `OrbitGeometryRigidity.lean` — `featureVec` and `normalizedSet`;
- **act 33**, `OrbitIsometryGroup.lean` — the whole module as landed at `D`;
- **act 34**, `ProductStratum.lean` — the whole module as landed at `D`;
- **act 35**, `DitaHull.lean` — the whole module as landed at `D`, in particular
  `a35_shared_f4_flat`, `a35_shared_half`, `a35_shared_norm_of_unit`, `a35_shared_unit_of_norm`
  and `a35_shared_gram_realizable`;
- **act 36**, `DitaHierarchy.lean` — the whole module as landed at `D`, in particular
  `a36_shared_z_unit`, `a36_shared_w_unit` and `a36_shared_one_core`;
- **act 37**, `DitaArcExclusivity.lean` — the whole module as landed at `D`: its head, the lookup
  tables of the eight classes and the census of the stratum point's Diţă structures in nine
  classes, which this round carries verbatim; no theorem of it is consumed by a proof;
- **Mathlib** — `Matrix.of`, `Matrix.of_apply`, `Matrix.transpose`, `Matrix.transpose_apply`,
  `Matrix.unitaryGroup`, `Matrix.mem_unitaryGroup_iff`, `Matrix.mul_apply`, `Matrix.one_apply`,
  `Matrix.star_apply`, `Fintype.sum_prod_type`, `Fin.sum_univ_four`, `Fin`, `Fin.divNat`,
  `Fin.modNat`, `finProdFinEquiv`, `Fintype.card`, the vector literal `![…]` and its evaluation
  lemmas, the star, norm and field lemmas of `ℂ` (`Complex.star_def`, `Complex.ext_iff`,
  `Complex.conj_ofReal`, `Complex.conj_I`, `Complex.norm_real`, `norm_mul`, `norm_div`,
  `norm_pow`, `norm_add_le`, `eq_inv_of_mul_eq_one_left`, `mul_eq_zero`, `div_eq_iff`,
  `div_le_iff`, `map_div₀`, `map_ofNat` and their kin), and the tactics `fin_cases`, `simp`,
  `decide`, `ring`, `field_simp`, `norm_num`, `linarith`, `nlinarith`, `linear_combination`,
  `split_ifs`, `induction` and `calc`.

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| `a37_shared_base_core`, `a37_exclusivity`, `a37_c_exclusive` | `''' + DAE + r'''` | ''' + lines(DAE, ['a37_shared_base_core', 'a37_exclusivity', 'a37_c_exclusive']) + r''' |
| `a36_shared_pow_unit`, `a36_shared_z_unit`, `a36_shared_w_unit`, `a36_shared_one_core` | `''' + DHI + r'''` | ''' + lines(DHI, ['a36_shared_pow_unit', 'a36_shared_z_unit', 'a36_shared_w_unit', 'a36_shared_one_core']) + r''' |
| `a36_shared_line_core`, `a36_hierarchy`, `a36_c_exclusive` | `the same file` | ''' + lines(DHI, ['a36_shared_line_core', 'a36_hierarchy', 'a36_c_exclusive']) + r''' |
| `a35_shared_f4_flat`, `a35_shared_half`, `a35_shared_norm_of_unit`, `a35_shared_unit_of_norm`, `a35_shared_gram_realizable` | `''' + DH + r'''` | ''' + lines(DH, ['a35_shared_f4_flat', 'a35_shared_half', 'a35_shared_norm_of_unit', 'a35_shared_unit_of_norm', 'a35_shared_gram_realizable']) + r''' |
| `a34_shared_product_core`, `a34_stratified` | `''' + PS + r'''` | ''' + lines(PS, ['a34_shared_product_core', 'a34_stratified']) + r''' |
| `featureVec`, `normalizedSet` | `''' + OGR + r'''` | ''' + lines(OGR, ['featureVec', 'normalizedSet']) + r''' |
| `transpose_unitary` | `''' + OGI + r'''` | ''' + lines(OGI, ['transpose_unitary']) + r''' |
| `FibreGram`, `RealizableGram`, `fibreGram_apply`, `sh1_necessity` | `''' + TSG + r'''` | ''' + lines(TSG, ['FibreGram', 'RealizableGram', 'fibreGram_apply', 'sh1_necessity']) + r''' |

| file at `D` | blob |
| --- | --- |
| `DitaArcExclusivity.lean` | `''' + blob(DAE) + r'''` |
| `DitaHierarchy.lean` | `''' + blob(DHI) + r'''` |
| `DitaHull.lean` | `''' + blob(DH) + r'''` |
| `ProductStratum.lean` | `''' + blob(PS) + r'''` |
| `OrbitGeometryRigidity.lean` | `''' + blob(OGR) + r'''` |
| `OrbitGeometryIsometries.lean` | `''' + blob(OGI) + r'''` |
| `TwoSidedGauge.lean` | `''' + blob(TSG) + r'''` |
| `verification/lean-mathlib/OIBridge.lean` | `''' + blob('verification/lean-mathlib/OIBridge.lean') + r'''` |
| `verification/lean-manuscript-census.json` | `''' + blob('verification/lean-manuscript-census.json') + r'''` |
| `verification/ROADMAP.md` | `''' + blob('verification/ROADMAP.md') + r'''` |
| `verification/lean/edge_rigidity_probe.py` | `''' + blob('verification/lean/edge_rigidity_probe.py') + r'''` |
| `verification/lean/dita_hierarchy_probe.py` | `''' + blob('verification/lean/dita_hierarchy_probe.py') + r'''` |
| `verification/lean/dita_arc_exclusivity_probe.py` | `''' + blob('verification/lean/dita_arc_exclusivity_probe.py') + r'''` |
| `.github/workflows/verify.yml` | `''' + blob('.github/workflows/verify.yml') + r'''` |

The names this round introduces return nothing from `git grep -l` at `D`: `DitaLocalEscape`,
`act-38`, `A38-`, `a38_` and `dita_local_escape`.

***

## Why this round exists

Acts 36 and 37 ran an exact one-parameter family `Pu u = SIG ∘ u^W` of realizable classes through
the certified rational stratum point and proved it exclusive to its frozen `2 × 8` Diţă class: an
arc that escapes no hull. Both recorded open whether every realizable class near the stratum lies
in some Diţă hull of some factorization of the sixteen-point carrier. The read-only discovery at
`D` searched, in exact arithmetic, for exponent matrices `E` with `SIG ∘ u^E` unitary at every unit
`u` — the straight lines through `SIG` — and classified them against the eighteen census
structures by linear algebra, since a structure holds identically along a straight line exactly
when `E` satisfies the structure's linear conditions. It found lines in no census subspace; the
smallest found, `E = A + B + C`, is the witness of this round. Its arc is realizable at every unit
`u`, admits no Diţă structure of any shape, index map or orientation at any unit outside `{1, −1}`,
strictly or up to diagonal equivalence, and so carries realizable non-Diţă points arbitrarily close
to `SIG`. This round freezes that: the realizability, the eighteen exclusions and the local-escape
corollary in the kernel, and the exhaustive complement, the exceptional set and its sharpness in
the exact-computation layer.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Every quantity below was computed at `D` from act 37's frozen probe objects, in exact arithmetic
throughout; the scripts are kept off the repository except the frozen probe.

- **The witness.** On the entry `((a,b),(c,d))`, rows `i = 4a+b` and columns `j = 4c+d`,
  `E = A + B + C` with `A = [a odd][b = 3][c odd]`, `B = [a = 2][d = 1]` and
  `C = [a+b odd][(c,d) ∈ {(0,2),(2,0)}]`; the three pieces are disjoint, each of support 16, so
  `E ∈ {0, 1}` with support 48. `E` is not a row-and-column shift: the arc is not a diagonal
  rephasing of `SIG`.
- **Realizability.** `H(u) H(u)^* = 16 I` as a Laurent-polynomial identity in `u`: every level set
  of every row-pair difference, 248 level sets over the 120 pairs with differences in `{−1, 0, 1}`,
  has vanishing pair sum, exactly; and every such sum vanishes monomial by monomial in `z` and `w`,
  so the identity holds with `z` and `w` symbolic units — which is how the kernel proves it. The
  naive per-monomial balance criterion is **false** in general at this point (the relation
  `z + w = 2(1 + zw)` produces vanishing subsets that are not balanced), so the search used exact
  subset-sum tables; for the witness the balanced form happens to hold and the kernel uses it.
- **The census and the exclusions.** Act 37's census is replayed: the nine column-form structures
  of `SIG`, the same nine index sets in the row form. Along the arc each of the eighteen imposes,
  beyond the identities, between 16 and 72 non-identity conditions, every one of the form
  `u^k = 1` with `k ∈ {−2, −1, 1, 2}` and trivial constant part, and each is admitted at `u = 1`
  alone. The arc is not symmetric, so the column and row forms are separate statements.
- **The generic point.** At a free symbol `u`, in both orientations and all three shapes, the
  proportionality test passes for **no** block structure at all: `(0, 0)` throughout.
- **The candidate set and the exceptional set.** Over every `n`-subset, `n ∈ {4, 2, 8}`, every pair
  of rows and both orientations, the units at which the pair becomes proportional on the subset
  without being so generically are forty points, `u = ζ z^s w^t` with
  `s, t ∈ {0, ±1/2, ±1}`, twenty Gaussian rational and twenty square roots outside `Q(i)`. The
  exhaustive search at each finds: at `u = 1` the eighteen, as `(5, 4)`, `(3, 2)`, `(3, 3)` per
  orientation; at `u = −1` exactly one `2 × 8` structure per orientation, `(1, 0)`, `(1, 0)`,
  `(1, 1)`, at index maps outside the census — column form blocks `(0, 2, 4, 6, 8, 10, 12, 14)`,
  `(1, 3, 5, 7, 9, 11, 13, 15)` and classes `(0, 2), (1, 3), (4, 6), (5, 15), (7, 13), (8, 10), (9, 11), (12, 14)`,
  row form blocks `(0, 1, 2, 3, 8, 9, 10, 11)`, `(4, 5, 6, 7, 12, 13, 14, 15)` and classes
  `(0, 2), (1, 9), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 10)`; at every other candidate
  point nothing. The relaxed condition, tested on every proportionality candidate at every point,
  holds at the same two units by the same structures. **The exact exceptional set is `{1, −1}`**,
  strictly and up to diagonal equivalence.
- **Sharpness.** `Hu (−1)` and its transpose are reconstructed exactly from flat unitary factors and
  unit twists at the two index maps, and the numeric search with factor unitarity finds exactly
  them and nothing of the other shapes; `Hu 1 = SIG` is reconstructed at every one of the nine
  census structures.
- **Controls.** The numeric search agrees with the symbolic one at all twenty Gaussian-rational
  candidates in both orientations; a genuine deformation inside each of the nine classes — one
  twist phase moved to `u₅` — is unitary, off `SIG`, and found by the search in its own class; the
  exponent matrix transported by three stabilizer elements, one of each kind, is straight, admits
  nothing at a generic `u` and exactly two structures at `u = −1`; a perturbed exponent matrix, one
  entry cleared, is not straight; the pieces `A`, `B`, `C` and their pairwise sums are straight
  lines lying identically in named census structures while the triple lies in none; act 37's `W`
  lies identically in `t1` alone.
- **The tangent space** (Hazard 7): rank 176 of the first-moment equations, dimension 80, defect
  49; the eighteen first-order subspaces of dimensions 36, 46, 36, 36, 44, 44, 57, 57, 49 by class,
  column and row forms agreeing, spanning all of it.
- **The kernel witnesses.** For each of the eighteen structures, four entry positions
  `p₁, p₂, p₃, p₄` with `H p₁ · H p₂ = H p₃ · H p₄` forced by the structure's Diţă form and
  `u`-exponent sums differing by one; for seventeen the four entries of `SIG` are in `{+1, −1}`,
  so that the identity reads `±u/16 = ±1/16` and gives `u = 1` by one `linear_combination`; for the
  column form of `t2` no such rational witness exists and the identity reads `(z/16) u = z/16`,
  which gives `z (u − 1) = 0` and `u = 1` since `z ≠ 0`.

None of this is a finding of the round. The route below is the freeze's reading of how the frozen
theorems are reached; the theorems and the probe decide.

***

## The configuration, FROZEN — act 29's product configuration over act 26's single carrier

- Act 37's frozen head, verbatim: act 36's head — act 35's head, then `dg`, `dgT`, `flg`, `r28`,
  `c28`, `dita28`, `r82`, `c82`, `dita82`, `z`, `w`, `SIG`, `Wt`, `Pu`, `u₆₀`, `P` — followed by act
  37's row map `r…`, column map `c…` and Diţă form `dita…` for each of the eight classes other than
  the frozen one.
- This round's objects, `let`-bound after it:

```lean
''' + CO['HEAD38'].rstrip('\n') + r'''
```

`Ew` is `E = A + B + C` in closed form on the product index; `Hu u = SIG ∘ u^{Ew}` is the arc. The
nine classes and their forms:

| class | shape | column blocks | row classes | reading |
| --- | --- | --- | --- | --- |
''' + '\n'.join('| `%s` | `%s` | %s | %s | %s |' % c for c in CLS) + r'''

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

The module `verification/lean-mathlib/OIBridge/DitaLocalEscape.lean` opens with exactly
`import OIBridge.DitaArcExclusivity`, its docstring, `namespace OIBridge`,
`namespace DitaLocalEscape`, and the one `open`:

```lean
''' + P['OPEN'] + r'''
```

It carries no definition of any kind, no `variable`, no second `open` and no second `import`; every
theorem is followed by its `#print axioms` line. Each statement below is declared
`theorem NAME :` with no binder before the colon, and statements are compared after collapsing
whitespace. The `let`-bound tables inside a statement are part of the statement. Every statement's
head is act 37's frozen head followed by this round's objects, and `controls.py` checks the head
against act 37's text byte for byte.

### `P_R` — the package

The conjunction, over one head, of `REAL` and the nine exclusions `EXCL_k1`, `EXCL_k2`, `EXCL_k3`,
`EXCL_k4`, `EXCL_e1`, `EXCL_e2`, `EXCL_t1`, `EXCL_t2`, `EXCL_t3`:

''' + lean('P_R') + r'''
### `P_N` — its negation

''' + lean('P_N') + r'''
`P_N` is `P_R`'s negation pushed through the outer conjunction. `controls.py` rebuilds both from the
shared components and rejects any drift.

### `A38-1` — the arc is realizable, required under `A38-NON-DITA-WITNESS-PROVED`

`REAL`, `a38_shared_realizable` — for every unit `u`, `Hu u` is unitary with every entry of norm
`1/4`, its Gram family is a realizable Gram over the product carrier, and its feature vector lies in
the product normalized set:

''' + lean('REAL') + r'''
### `A38-2` — each class is admitted only at the base point, required under `A38-NON-DITA-WITNESS-PROVED`

For each of the nine classes, `EXCL_…`, `a38_shared_excl_…` — for every unit `u`, a Diţă form of
`Hu u` at the class's index maps with flat unitary factors and unit twists forces `u = 1`, and so
does the transpose of one:

''' + ''.join('`EXCL_%s`, `a38_shared_excl_%s`, the class `%s`:\n\n' % (nm, nm, nm) + lean('EXCL_' + nm) for nm, *_ in CLS) + r'''
### `A38-3` — the local escape, required under `A38-NON-DITA-WITNESS-PROVED`

`ESCAPE`, `a38_c_local_escape` — for every `ε > 0` there is a unit `u ≠ 1` within `ε` of `1`, with
`Hu u` within `ε` of `SIG` entrywise, such that `Hu u` is realizable and admits none of the eighteen
Diţă forms:

''' + lean('ESCAPE') + r'''
### The control, required under both decided labels

`BASE`, `a38_control_base` — the arc at `u = 1` is the stratum point, the Fourier factors are flat
unitaries, and the stratum point carries the Kronecker `4 × 4` factorization, class `k1`, with
those factors and the trivial twist, so that the exclusion of `k1` is sharp at `u = 1`:

''' + lean('BASE') + r'''
### The theorems, FROZEN by name and statement form

| role | theorem | statement |
| --- | --- | --- |
| `A38-NON-DITA-WITNESS-PROVED` | `a38_witness` | `P_R` |
| `A38-WITNESS-FAILS` | `a38_not_witness` | `P_N` |
| corollary, required in every case | `a38_c_exclusive` | `(P_N) → ¬ (P_R)` |
| `A38-1`, required under `A38-NON-DITA-WITNESS-PROVED` | `a38_shared_realizable` | `REAL` |
''' + '\n'.join('| `A38-2`, required under `A38-NON-DITA-WITNESS-PROVED` | `a38_shared_excl_%s` | `EXCL_%s` |' % (nm, nm) for nm, *_ in CLS) + r'''
| `A38-3`, required under `A38-NON-DITA-WITNESS-PROVED` | `a38_c_local_escape` | `ESCAPE` |
| control, required under both decided labels | `a38_control_base` | `BASE` |

A module with neither verdict theorem reports `A38-UNDECIDED`, and a module with both is a failure
of the round. Every other theorem is named `a38_shared_…`, and every theorem is followed by its
`#print axioms` line.

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze, on disposable branches from `D` that are never landed.
Each is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design
evidence** recorded here: none is a `check-run` attestation, and no predicate of the round reads
them.

The design file is `verification/lean-mathlib/OIBridge/DitaLocalEscape.lean` on those branches;
the branches also carry a disposable census family for the module and, on the probe's design head,
the frozen probe wired into the workflow, none of which is part of the freeze except the probe and
its wiring.

@@RUNS@@

***

## The exact-computation layer — the frozen probe

`verification/lean/dita_local_escape_probe.py`, blob **`@@PROBE_BLOB@@`**, is written before `F`
and added by the execution at stage 1 with exactly this blob, and `.github/workflows/verify.yml` at
`E` is `D`'s with the shard `probes_a38` inserted before the foundations shard and required by the
aggregate job, the five frozen edits `controls.py` embeds, so that the shard runs the probe at every
execution commit from stage 1 on, and so at `E`. `F` carries this file alone and no probe; the runs
at `F` exercise the workflow at `D`. The probe's design run before `F` is recorded in the runs table
above. Its first part is act 37's probe head verbatim — act 36's exact Gaussian rationals, exhaustive
structure search and stabilizer, and act 37's monomial calculus — and it uses Python integers and
fractions for every value it asserts, no floating point anywhere, and exits 1 on any mismatch with
the values frozen here. Its statements are exact arithmetic replayed; they are not kernel-certified,
and the result note names them as this layer's.

**0. Act 36's stabilizer, replayed**: the factor stabilizer products 256 for each of the four
operations without factor exchange and 0 with it; the order **1024**.

**1. Realizability.** The symbolic entries `i^p z^q w^r` equal the numeric entries of `SIG`;
`E = A + B + C` equals its frozen table, with entries in `{0, 1}` and disjoint pieces; the supports
are **16, 16, 16, 48**; `E`'s gauge normal form is not zero; every level set of every row-pair
difference has vanishing pair sum — **248** level sets, differences in `{−1, 0, 1}` — and vanishes
monomial by monomial; `H(1) = SIG`, and `H(u)` is unitary at `u₅`, `u₆₀`, `−1` and `i`; `H(u₅)`
differs from `SIG` in exactly the 48 support entries.

**2. Class exclusions.** Act 37's census replayed, nine column-form structures at the frozen index
sets, the same nine in the row form; each of the eighteen structures imposes non-identity
conditions, all `u^k = 1` with trivial constant part and `k ∈ {−2, −1, 1, 2}`, in the counts
**''' + ', '.join(str(x) for x in NONID) + r'''** for `k1, k2, k3, k4, e1, e2, t1, t2, t3`, column
then row form; each is admitted at `u = 1` alone; the kernel witness identity of every structure
is forced by its Diţă form with the frozen exponent sums differing by one, rational for seventeen;
the one non-rational, `t2` in the column form, reads `(z/16) u = z/16`:

| class | form | kind | positions `p₁, p₂, p₃, p₄` | exponent sums | constant | `linear_combination` |
| --- | --- | --- | --- | --- | --- | --- |
''' + '\n'.join(witrow(nm, f) for nm, *_ in CLS for f in ('column', 'row')) + r'''

**3. All-index exhaustion.** At a generic `u`, `(0, 0)` for every orientation and shape: no block
structure passes the proportionality test.

**4. The exceptional set.** The candidate exceptional set is exactly, in the probe's order,
`''' + '`, `'.join(E_CAND) + r'''`; twenty are Gaussian rational. At `u = 1`: `(5, 4)`, `(3, 2)`,
`(3, 3)` per orientation; at `u = −1`: `(1, 0)`, `(1, 0)`, `(1, 1)` per orientation, the two
structures at the index maps named above, outside the census; **the exact exceptional set is
`{1, −1}`**, and the relaxed exceptional set is the same, with the relaxed structures at the two
units the strict ones.

**5. Sharpness.** `H(−1)` and its transpose reconstructed exactly at the two index maps; the numeric
search at `u = −1` finds exactly them; `SIG` reconstructed at all nine census structures and
`H(1) = SIG`; the two structures of `u = −1` are admitted at `u = −1` alone, neither at a generic
`u` nor at `u = 1`.

**6. Generic non-Diţă.** The units at which `H(u)` admits any structure, strictly or relaxed, are
exactly `{1, −1}`; the generic candidate set is empty.

**7. Controls.** Numeric agreement at the twenty Gaussian-rational candidates in both
orientations; a genuine deformation in each of the nine classes found in its class; three
stabilizer transports of `E` straight, `(0, 0)` generically and two structures at `u = −1`; the
perturbed matrix not straight; the pieces and pairwise sums straight with their identical
structures as measured, the triple in none; act 37's `W` in `t1` alone.

**8. The tangent space.** Rank **176**, dimension **80**, defect **49**; the first-order subspaces
of dimensions **36, 46, 36, 36, 44, 44, 57, 57, 49** by class, column and row forms agreeing; `E`
tangent, in none of the eighteen, and the eighteen spanning all 80 dimensions.

The probe reports @@NPASS@@ `PASS` and no `FAIL`, runs in about @@PROBE_MIN@@ minutes, and ends
with the line `dita_local_escape_probe: OK …` on success, which the result note carries verbatim,
and `dita_local_escape_probe: FAILED …` with the failing checks otherwise.

***

## The question, FROZEN — one target

### `A38` — a genuine non-Diţă local escape

**For the explicit exponent matrix `E = A + B + C` and the arc `Hu u = SIG ∘ u^E` through the
certified rational stratum point: is `Hu u` a complex Hadamard matrix — a flat unitary, realizable
— at every unit `u`; for each of the nine factorization classes of the stratum point, does a Diţă
form of `Hu u` at that class's index maps, in either orientation, force `u = 1`; and does every
neighbourhood of `SIG` therefore contain a realizable matrix admitting none of the eighteen forms —
while, under every decided label, the base point `Hu 1 = SIG` carries the Kronecker `4 × 4`
factorization with flat unitary factors?**

The answer is reported as one of three labels:
- `A38-NON-DITA-WITNESS-PROVED`, the theorem `P_R`;
- `A38-WITNESS-FAILS`, the theorem `P_N`;
- `A38-UNDECIDED`.

Beside the label, the exact-computation layer's statement stands or falls with the probe: green,
it establishes that at every unit `u ∉ {1, −1}` no index maps whatever admit a Diţă form of `Hu u`
in either orientation, strictly or up to diagonal equivalence, and that at `u = −1` exactly one
`2 × 8` structure per orientation does; red at `E`, the round halts. Together the two layers earn
the frozen main statement: *`Hu u` is a complex Hadamard matrix for every unit `u`, and for every
unit `u ∉ {1, −1}` it admits no Diţă structure of any admissible shape, index map or orientation,
including up to the allowed diagonal equivalences.*

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| the base point | `a38_control_base` | `Hu 1 = SIG` carries class `k1` with flat unitary factors, so the exclusion of `k1` is sharp at `u = 1`, required whichever label is earned |
| the exceptional point | the probe's reconstruction at `u = −1` | the failure of every exclusion at `u = −1` is certified as a Diţă structure, not merely observed |
| the census is not vacuous | the probe's `(5, 4)`, `(3, 2)`, `(3, 3)` at `u = 1` in both orientations | the same search finds the eighteen structures of the stratum point |
| the symbolic search is the numeric one | the probe's agreement at the twenty Gaussian-rational candidates | the monomial calculus, without factor unitarity, returns what act 36's search returns with it |
| each class is reachable | the probe's genuine deformations, one per class | a point of each class's hull off `SIG` is found by the search in its class, so a class the search fails to find at an arc point is absent, not invisible |
| equivalence invariance | the probe's three stabilizer transports | the classifier gives the same answer under the allowed row and column operations |
| a wrong matrix fails | the probe's perturbed exponent matrix | one entry cleared, the Laurent identity fails and `H(u₅)` is not unitary |
| the classifier sees Diţă lines | the probe's pieces and act 37's `W` | straight lines that do lie in census classes are found there, so a line found in none is absent, not invisible |
| the witnesses are forced | the probe's witness check | each kernel identity is a consequence of its structure's Diţă form with the frozen constants and exponent sums |
| duality | `a38_c_exclusive` and `controls.py` | the two verdicts cannot both be earned |

***

## The route, recorded as the freeze's reading and not as a finding

1. **`REAL`.** With `z`, `w`, `u` symbolic units, `star x = x⁻¹` for each; for each of the sixteen
   rows `(a, b)` the entry `((a,b), j)` of `Hu · (Hu)^*` is a sum of sixteen monomials in `z`, `w`,
   `u` and their inverses with rational coefficients, and equals `[ (a,b) = j ]`: by `fin_cases` on
   `j`, `simp` with the sum expansions and the star rewrites, `field_simp` and `ring` — sixteen
   row lemmas, one per `(a, b)` (`a38_shared_row_core_ab`), assembled into the unitarity by `ext`
   and `fin_cases` on the row (`a38_shared_unitary_core`); flatness from `a35_shared_half` twice and
   `‖u‖ = 1` (`a38_shared_flat_core`); the realizable Gram and the feature vector from act 35's
   `a35_shared_gram_realizable` (`a38_shared_real_core`), instantiated at `z`, `w` by act 36's unit
   lemmas.
2. **`EXCL_…`.** From a Diţă form `Hu u = dita… X Y D`, or `= (dita… X Y D)ᵀ`, the four entries
   at the witness positions of the table factor as `X a c · D c b · Y c b d`, and the product of
   the first two equals the product of the last two identically (`ring`), because they pair the
   same factors: for a proportionality witness the two rows are in one class and the two columns in
   one block, for a rectangle witness the rows `(a,b), (a',b')` against `(a,b'), (a',b)` sit in one
   column, and in the row form the roles of rows and columns are exchanged. The same four entries of
   `Hu u` are `±(1/4)·u^k` with exponent sums differing by one, so the identity reads
   `±u/16 = ±1/16` and `linear_combination` with the coefficient of the table gives `u = 1`; for the
   column form of `t2` it reads `(z/16) u = z/16`, so `z (u − 1) = 0` and, `z ≠ 0` by `norm_num` on
   real and imaginary parts, `u = 1`.
3. **`ESCAPE`.** For `t > 0` the Cayley point `u = (1 + t i)/(1 − t i)` is a unit, is not `1`, and
   `‖u − 1‖ ≤ 2t` since `‖1 − t i‖ ≥ 1` (`a38_shared_cayley_core`); with `t = ε/8`,
   `‖u − 1‖ ≤ ε/4 < ε`. Entrywise, `Hu u − SIG = SIG ∘ (u^E − 1)`, `‖SIG i j‖ = 1/4`, and
   `‖u^n − 1‖ ≤ n ‖u − 1‖` for a unit `u` by induction (`a38_shared_pow_sub_one`) with
   `E i j ≤ 3` by `split_ifs` (`a38_shared_ew_le`), so every entry differs by at most `3ε/16 < ε`.
   Realizability is `REAL` at `u`; each of the eighteen negations is the corresponding exclusion
   at `u` against `u ≠ 1` (`a38_shared_escape_core`).
4. **`BASE`.** `Hu 1 = SIG` entrywise by `one_pow` and `mul_one`; the flatness of `F4 z`, `F4 w` by
   act 35's `a35_shared_f4_flat` and `a35_shared_half`; the Kronecker identity entrywise, the two
   lookup tables of `k1` returning `i.1` and `i.2` by `fin_cases`, then `mul_one`.
5. **`a38_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

No route to `A38-WITNESS-FAILS` is expected. The freeze's reading is that `P_R` holds.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| every `a38_shared_…` and every `a38_c_…` other than `a38_c_exclusive` | either verdict theorem; `a38_c_exclusive` |
| every `a38_control_…` | either verdict theorem; `a38_c_exclusive` |
| `a38_not_witness` | `a38_shared_realizable`, every `a38_shared_excl_…`, `a38_c_local_escape` |
| `a38_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A38` | `A38-NON-DITA-WITNESS-PROVED` | **very high** | the realizability is a finite polynomial identity verified in exact arithmetic monomial by monomial before the freeze; each exclusion is one forced product identity with a nonzero constant, verified in exact arithmetic; the escape is elementary from those; and every frozen statement was proved on a disposable branch before the freeze, with every named result within the three axioms |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A38-NON-DITA-WITNESS-PROVED`

> ''' + T['SENTENCES']['A38-NON-DITA-WITNESS-PROVED'] + r'''

### `A38-WITNESS-FAILS`

> ''' + T['SENTENCES']['A38-WITNESS-FAILS'] + r'''

### `A38-UNDECIDED`

> ''' + T['SENTENCES']['A38-UNDECIDED'] + r'''

### The corollary, REQUIRED

`a38_c_exclusive : (P_N) → ¬ (P_R)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label, and the probe's
summary line `dita_local_escape_probe: OK …` from the run at `E`.

| row | outcome |
| --- | --- |
| 1 | `A38-NON-DITA-WITNESS-PROVED` |
| 2 | `A38-WITNESS-FAILS` |
| 3 | `A38-UNDECIDED` |

***

## The `P0` row, per case

At `D`, the `P0` cell of `verification/ROADMAP.md` ends with act 37's sentence and its standing
clause:

> ''' + T['P0_END_D'] + r'''

**On a decided outcome**, this round's sentence for the case is appended once after that standing
clause, followed by its own standing clause:
- **`A38-NON-DITA-WITNESS-PROVED`:**

  > ''' + T['P0_CASE']['A38-NON-DITA-WITNESS-PROVED'] + ' ' + T['P0_STANDING_38'] + r'''

- **`A38-WITNESS-FAILS`:**

  > ''' + T['P0_CASE']['A38-WITNESS-FAILS'] + ' ' + T['P0_STANDING_38'] + r'''

**On `A38-UNDECIDED`** the cell is not touched.

The expected `ROADMAP.md` at `E` is `D`'s with that sentence appended, or `D`'s unchanged, byte for
byte. Rehearsed at `D`, the two decided cells give these blobs:
- `@@ROAD_PV@@` (`A38-NON-DITA-WITNESS-PROVED`);
- `@@ROAD_FL@@` (`A38-WITNESS-FAILS`).

The guard run locally at `D` against each rehearsed cell reports `ALL CHECKS PASS`, the tags in
`D`'s order; the guard is not changed by this round.

***

## What no outcome licenses

- **No outcome revises act 37's `A37-EXCLUSIVITY-PROVED`, act 36's `A36-HIERARCHY`, act 35's
  `A35-DITA-STRATIFIED`, act 34's `A34-STRATIFIED`, act 33's `A33-CLASSIFIED`, act 32's
  `A32-NOT-RIGID` or any verdict of acts 28 to 31.** Those are the verdicts those rounds recorded,
  and they stand; act 37's arc lies in its `2 × 8` hull as recorded.
- **No outcome counts, classifies or minimizes.** Nothing is claimed about how many straight lines
  through `SIG` exist, about the minimality of the witness's support, about the orbits of witnesses,
  about the three-parameter family `SIG ∘ u₁^A u₂^B u₃^C`, or about the decomposition `E = A + B + C`
  beyond its use as a control; each is a possible round of its own.
- **No outcome says anything about Diţă's construction beyond the frozen statements**: what is
  established is that one explicit realizable arc admits no Diţă structure of the sixteen-point
  carrier at any unit outside `{1, −1}`, by the kernel for the eighteen census forms and by the
  probe for every other index map, and that realizable non-Diţă points lie arbitrarily close to
  `SIG`. Whether some larger construction, or a finer notion of hull, captures those points is not
  asked.
- **No outcome classifies the classes of the product normalized set or its isometries.**
- **No outcome reports anything about transition families or dynamics.** Nothing here establishes
  that any admissible law is covariant under any isometry or reaches any class, and none closes
  `P0`, which stays `OPEN`.
- **No hull, family, factorization, class, isometry, group or covariance is called canonical,
  physical or fundamental.**

## Non-doings

This round does not do any of the following:
- define anything, or restate any rung or declaration;
- read any configuration but the one frozen;
- edit any closed round's record;
- edit the guard, or the roadmap's section on the residual deformation space;
- write any manuscript file;
- change the workflow beyond the one shard and the four lines that require it;
- import any Mathlib module into the frozen module beyond what `DitaArcExclusivity` imports;
- search for, name or freeze any arc other than the one explicit `E`, or any family containing it.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks; act 37's head and
this round's `Ew` and `Hu` are `let`-bound inside each statement that uses them.

## Evidence level

**2** for the module — Lean theorems, kernel-checked, every named result printing its axioms, each
within `propext`, `Classical.choice` and `Quot.sound`. The probe's statements are exact arithmetic
replayed in CI, a separate layer named as such wherever they are cited.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-38-local-escape/controls.py`, blob
**`@@CONTROLS_BLOB@@`**, is written before `F` and added by the execution with exactly this blob.
- It imports nothing from the repository and changes nothing.
- It reads `D` and the commit under check through `git`.
- It embeds every frozen text it compares against.

`controls.py check <commit>` fails unless all of the following hold:

- **The duality and the single source.**
  - The frozen `P_R` is the conjunction, over the frozen head, of the ten package texts, and
    `P_N` the disjunction of their negations, rebuilt from the shared components.
  - Every other statement carries the one head verbatim; the head is act 37's frozen head, byte
    for byte, followed by this round's objects.
- **The module**:
  - begins with the frozen import and carries the one frozen `open`;
  - has no forbidden command or token;
  - has a `#print axioms` line for every theorem;
  - uses only the frozen names or `a38_shared_…`;
  - gives each frozen theorem its frozen statement, the statement ending at the `:=` that opens
    its proof and not at a `let` inside it;
  - has at most one verdict theorem, and `a38_c_exclusive`;
  - carries the statements the earned label requires.
- **The result note** carries:
  - the outcome line once;
  - the earned label's frozen sentence once, and no other label's;
  - THE CLAUSE's mention once, with the complete clause following it;
  - by name, the statements the label requires;
  - the probe's summary line.
- **`ROADMAP.md`** is byte-identical to `D`'s with the frozen sentence for the case appended, or to
  `D`'s.
- **The guard** is byte-identical to `D`'s.
- **The probe** has its frozen blob, and **the workflow** is `D`'s with the five frozen edits.
- **The census** is `D`'s with exactly one family appended, last, for `DitaLocalEscape`:
  `kernel-only`, no manuscript anchor, and its note naming the label and no other.
- **`OIBridge.lean`** is `D`'s with `import OIBridge.DitaLocalEscape` inserted directly after
  `import OIBridge.DitaArcExclusivity`.
- **The paths** changed from `D` are exactly these:
  - added: the three record files, the module and the probe;
  - modified: `OIBridge.lean`, the census and the workflow;
  - modified on a decided outcome only: `ROADMAP.md`.

`controls.py --self-test` also does four things:
- it checks the constants against this preregistration, beside it;
- it checks the duality and single source of the frozen texts, together with 9 duality
  mutations, each of which must be rejected;
- it builds a synthetic execution for each of the three rows and requires every one to hold;
- it applies @@NMUTS@@ mutation controls, each of which must fail with its named code.

Run at `D` beside this file, it prints:

```text
controls: the two verdict propositions are duals and every shared text has one source; 9 duality mutations fail as required
controls: 3 rows hold as frozen, @@NMUTS@@ mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear
commits from `F`, each with one parent:

1. **Stage 1 — the module, the controls and the probe.**
   - `controls.py` with its frozen blob.
   - The probe with its frozen blob, and the workflow shard that runs it.
   - The module with the frozen header and its shared lemmas. On the route to
     `A38-NON-DITA-WITNESS-PROVED` these include `A38-1`, the nine `A38-2`, `A38-3` and the control.
   - The import line.

   No verdict theorem and no corollary `a38_c_exclusive`.
2. **Stage 2 — the verdict.** `a38_witness` or `a38_not_witness`, or neither, and
   `a38_c_exclusive`.
3. **Stage 3 — the surfaces.** The census family, `kernel-only`, appended last. On a decided
   outcome only, the `P0` sentence for the case.
4. **The result note** `result.md`, whose commit is `E`; it carries the probe's summary line from
   the run at `E`'s predecessor and is confirmed by the run at `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40), and so is the probe as a CI job. A stage whose build
fails is followed by a fixing commit, never rewritten. The label is read from the module at `E`.
Proofs may be developed first on a disposable branch from `F`, never landed; such runs are design
evidence and the result note names them.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the probe is the frozen one and runs green | `C3`: the probe's blob at stage 1 and at `E`; the `Numerical probes / A38 escape` shard green at every execution commit and at `E` with the probe's `OK` line in its log |
| the frozen propositions elaborate as frozen | before `F`: the elaboration run above; at `E`: `C8`, every frozen theorem compiled under its statement |
| every verdict and control is kernel-checked, within the three axioms | `C8`: the dispatch run at `E`, the `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the statements, duality, corollary, controls and outcome grammar hold | `C9`: `controls.py check E` prints `controls: check OK` |
| the surfaces are exactly the frozen ones for the case, and the guard is untouched | `C9` |
| the guard stays green | `C8`: `ALL CHECKS PASS`, the tags in `D`'s order |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen propositions unchanged** is repaired by later
  linear commits before `E`.
- **A verdict that cannot be obtained** is reported `A38-UNDECIDED`, with the step named. In that
  case `ROADMAP.md` is not touched.
- **A decided label whose required statements are not all proved** is not reported; it is
  `A38-UNDECIDED` with the missing statement named. A verdict prints only over green controls,
  the probe among them.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target.
  It is any of these:
  - a frozen proposition that is ill-typed or cannot be stated as frozen;
  - a required statement or control that is false as frozen when the route through it is taken —
    in particular `BASE` false as frozen, which no label absorbs;
  - the probe red at `E` with the frozen blob — in particular an exact exceptional set other than
    `{1, −1}`, or a structure at `u = −1` that fails to reconstruct (Hazard 2).

  The round then halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
'''
open(os.path.join(S, 'preregistration.draft.md'), 'w', encoding='utf-8').write(doc)
print('draft lines', doc.count('\n'))
