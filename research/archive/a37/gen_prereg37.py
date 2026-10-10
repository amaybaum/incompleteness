"""Assemble the A37 preregistration from the single proposition source (props37.json, texts37.json).
Placeholders @@RUNS@@, @@CONTROLS_BLOB@@, @@PROBE_BLOB@@, @@NMUTS@@, @@NPASS@@, @@PROBE_MIN@@, @@ROAD_PV@@,
@@ROAD_FL@@ are filled by fill_prereg37.py once the runs, controls.py and the probe are final. Line numbers of the
locating table are read from the D worktree at generation time."""
import json, os, re, subprocess
S = os.path.dirname(os.path.abspath(__file__))
WT = os.path.join(S, '..', 'wt-d37')
P = json.load(open(os.path.join(S, 'props37.json')))
T = json.load(open(os.path.join(S, 'texts37.json')))
WIT = json.load(open(os.path.join(S, 'witness37.json')))
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
       ('t2', '2 × 8', '(0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)', '(0, 2), (1, 3), (4, 6), (5, 7), (8, 10), (9, 11), (12, 14), (13, 15)', 'blocks by the parity of `d`, classes by `(a, b div 2)`'),
       ('t3', '2 × 8', '(0, 2, 5, 7, 8, 10, 13, 15), (1, 3, 4, 6, 9, 11, 12, 14)', '(0, 10), (1, 11), (2, 8), (3, 9), (4, 14), (5, 15), (6, 12), (7, 13)', 'blocks by `(c + d) mod 2` … the twisted parity split')]
def witrow(nm):
    w = WIT[nm]; p = w['p']
    pos = ', '.join('`((%d,%d),(%d,%d))`' % (i // 4, i % 4, j // 4, j % 4) for i, j in p)
    return '| `%s` | %s | %s | `%d`, `%d` | `%d` |' % (nm, 'proportionality' if w['kind'] == 'prop' else 'rank-one', pos, w['e'][0], w['e'][1], w['coef'])
E_CAND = json.load(open(os.path.join(S, 'e_cand37.json')))

doc = r'''# Track B act 37 — the exclusivity of the `2 × 8` arc through the product-embedded stratum point: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
''' + q(T['CLAUSE']) + r'''

## The declarations

```v3-round
round A37
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-37-arc-exclusivity/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-37-arc-exclusivity/
record AM verification/receipts/A37.json
execution A verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean
execution A verification/lean/dita_arc_exclusivity_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
execution M verification/ROADMAP.md
```

The record directory holds three files: this preregistration, the round's frozen controls
`controls.py`, and the result note. The receipt path is `verification/receipts/A37.json`. Every
other path the round changes is an execution path listed above. The guard,
`verification/lean/edge_rigidity_probe.py`, is not governed and is not changed: at `E` it is byte
for byte `D`'s, and `controls.py` checks that it is. The workflow changes by two lines: the round's
probe is appended, as its own `echo` and `python3` lines, after act 36's probe in the
`Numerical probes / A36 hierarchy` shard, and `controls.py` checks that the workflow at `E` is `D`'s
with exactly those two lines inserted.

`ROADMAP.md` changes only on a decided outcome, and only as this file freezes: by the `P0` sentence
for the case, appended to the cell. The roadmap's section *The residual deformation space at the
product stratum*, landed before `D`, is not edited by this round.

## The objects

- **`D`** = `d014bafef404b991b4544e6d2041edcfab1ac765`: the head of `main` after the landing of
  pull request #763, the last of four continuous-integration pull requests that followed act 36's
  landing `2abd7816…` and changed no mathematics: they accelerated act 36's and act 35's probes
  under an exact old-versus-new replay control and split the core probe shard. It is certified by
  push run 36373806246: all seven jobs green in 3 minutes, the release gate passing with twelve
  receipts holding, the `Mathlib bridge` build green with `lean-axioms` at 4829 named results and no
  sorry, the guard 91 PASS and 0 FAIL, act 36's probe reporting its `OK` line in 50 seconds and act
  35's in 45. Every measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A37.json`.

No other round runs beside A37 at this freeze. Should one land first, its movement of `main`
enters A37 only by reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — the exclusion is two-layered, and the layers are never merged.** The kernel proves,
for each of the eight factorization classes of the stratum point other than the frozen one, that a
Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`. That is a
statement about eight named index maps. That **no index maps whatever** admit a Diţă form of `Pu u`
at a unit `u ≠ 1` except the frozen class's is the exact-computation layer's statement, established
by the frozen probe and not by the kernel; it is never written as a theorem of the module, and the
result note, the census family and the `P0` sentence name its layer wherever it is cited.

**Hazard 2 — the exceptional set is determined by the algebra before the freeze, and the freeze
records what it found.** The frozen theorem's set is `{1}`: the kernel statements force `u = 1` for
the eight classes because the obstruction each class carries is a monomial `u^{±1} = 1`, found by
the pre-freeze measurement and replayed by the probe; and the probe computes the candidate set of
every unit at which any other structure could appear, twenty points named exactly, and decides
each by the exhaustive search, finding only the frozen class away from `u = 1`. The value `{1}` is
the design run's, asserted by the probe at every execution commit. A different value at `E` is not
a reinterpretation of the theorem: it is the probe red with the frozen blob, a freeze failure, and
the round halts.

**Hazard 3 — the monomial calculus and its canonical names.** Every entry of
`SIG = F₄(z) ⊗ F₄(w)` is `i^p z^q w^r`, so every entry of `Pu u = SIG ∘ u^W` is `i^p z^q w^r u^k`
with `k = W(i, j) ∈ {0, 1, 2}`. A Diţă structure — column blocks and row classes — is admitted at
`u` if and only if finitely many **monomial equations** hold: the proportionality of every two rows
of a class on every block, and the rank-one condition on the block ratios; the flat unitarity of
the factors follows from the unitarity of `Pu u`, which act 36 proved for every unit `u`, and is not
a further condition (Hazard 4). Each equation `u^k = i^p z^q w^r` with `k ≠ 0` has exactly `|k|` unit
solutions `u = ζ · z^{−q/k} · w^{−r/k}`, `ζ` a root of unity; and because `z = (2+i)/(2−i)` and
`w = (3+2i)/(3−2i)` are quotients of distinct Gaussian primes by their conjugates, they are
multiplicatively independent modulo roots of unity, so the triple `(ζ, s, t)` with `u = ζ z^s w^t`
is a canonical exact name for a point, and monomials at a point are compared exactly as such
triples. The probe uses this and nothing else for its symbolic searches; twelve of the twenty
candidate points are Gaussian rational and there the numeric search of act 36's probe, with factor
unitarity, is run as a control and must agree.

**Hazard 4 — why the candidate set is exhaustive, recorded as the freeze's reading.** Outside the
candidate set, no monomial condition other than an identity holds: the proportionality partition of
every block is its generic one, so the candidate structures are exactly the generic candidates —
one `4 × 4`, one `8 × 2` and one `2 × 8` — and of these only the frozen `2 × 8` class satisfies the
rank-one condition identically; the other two satisfy it at `u = 1` alone, which is itself a
candidate point. At the candidate points the exhaustive search decides. So a structure admitted at
any unit off the candidate set is the frozen class, a structure admitted at infinitely many units
is admitted identically and so at `u = 1`, hence is one of the eighteen of the census, and no index
maps outside the census appear anywhere on the circle off the twenty points. This subsumes the
local reduction: a factorization appearing arbitrarily near `SIG` specializes at `u = 1` to one of
the census. The probe executes each step of this reading; the reading itself is this file's.

**Hazard 5 — the census is complete because act 36's search is.** The eighteen structures of the
stratum point are the exact factorizations of act 36's exhaustive block-structure search at
`SIG`, which enumerates every block structure a factorization must induce (act 36, Hazard 4). The
nine classes are its orbits under the certified stabilizer of `SIG` in `G_ext`, of order 1024,
which contains transposition since `SIG` is symmetric; each orbit is a structure paired with its
transpose and nothing else, because the factor exchange is not a symmetry (`z ≠ w`). The frozen
quantifier ranges over all admissible index maps by Hazard 4, and the kernel's eight statements
range over the eight other classes, one representative each in the column form, the row form being
the same statement by the symmetry of the arc.

**Hazard 6 — the hierarchy is not exhausted.** That the arc is exclusive to its `2 × 8` class is a
statement about the arc. Whether every realizable class near the stratum lies in some Diţă hull of
some factorization of the sixteen-point carrier is **open**; the round records it and does not
decide it, and an `EXCLUSIVITY-PROVED` verdict is not evidence that the hierarchy exhausts anything
or that the arc escapes every hull: it lies in the frozen `2 × 8` hull, by act 36's theorem, at
every unit `u`.

**Hazard 7 — history.** Act 36 recorded `A36-HIERARCHY` with the exhaustion of the hierarchy open,
act 35 `A35-DITA-STRATIFIED`, act 34 `A34-STRATIFIED`, act 33 `A33-CLASSIFIED`, act 32
`A32-NOT-RIGID`, act 29 to act 31 their product-configuration verdicts. All stand as recorded. A
decided outcome here is stated as a fact about the arc and the classes of the stratum point; it is
never a revision of an earlier round's verdict.

**Hazard 8 — vocabulary.** A class is a pair of index maps, a hull is a family of classes, a
factorization is a way of writing a matrix, an isometry is not a symmetry, the group acting is not
a symmetry group of anything physical, covariance under it is a hypothesis this round does not
assert of any law, and none is written as the other.

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
- **act 36**, `DitaHierarchy.lean` — the whole module as landed at `D`: `a36_hierarchy`,
  `a36_c_exclusive`, every `a36_control_…` and every `a36_shared_…` theorem. In particular
  `a36_shared_z_unit`, `a36_shared_w_unit`, `a36_shared_u60_unit`, `a36_shared_pow_unit`,
  `a36_shared_hull28_core`, `a36_shared_line_core`, `a36_shared_one_core`, `a36_shared_line` and
  `a36_shared_point`;
- **Mathlib** — `Matrix.of`, `Matrix.of_apply`, `Matrix.transpose`, `Matrix.transpose_apply`,
  `Matrix.transpose_transpose`, `Matrix.unitaryGroup`, `Fin`, `Fin.divNat`, `Fin.modNat`,
  `finProdFinEquiv`, `Fintype.card`, the vector literal `![…]` and its evaluation lemmas, the
  tactics `fin_cases`, `simp`, `decide`, `ring`, `norm_num` and `linear_combination`, and the algebra
  of `ℂ`.

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| `a36_shared_pow_unit`, `a36_shared_z_unit`, `a36_shared_w_unit`, `a36_shared_u60_unit` | `''' + DHI + r'''` | ''' + lines(DHI, ['a36_shared_pow_unit', 'a36_shared_z_unit', 'a36_shared_w_unit', 'a36_shared_u60_unit']) + r''' |
| `a36_shared_hull28_core`, `a36_shared_line_core`, `a36_shared_one_core` | `the same file` | ''' + lines(DHI, ['a36_shared_hull28_core', 'a36_shared_line_core', 'a36_shared_one_core']) + r''' |
| `a36_shared_line`, `a36_shared_point`, `a36_hierarchy`, `a36_c_exclusive` | `the same file` | ''' + lines(DHI, ['a36_shared_line', 'a36_shared_point', 'a36_hierarchy', 'a36_c_exclusive']) + r''' |
| `a35_shared_f4_flat`, `a35_shared_half`, `a35_shared_norm_of_unit`, `a35_shared_unit_of_norm`, `a35_shared_gram_realizable` | `''' + DH + r'''` | ''' + lines(DH, ['a35_shared_f4_flat', 'a35_shared_half', 'a35_shared_norm_of_unit', 'a35_shared_unit_of_norm', 'a35_shared_gram_realizable']) + r''' |
| `a34_shared_product_core`, `a34_stratified` | `''' + PS + r'''` | ''' + lines(PS, ['a34_shared_product_core', 'a34_stratified']) + r''' |
| `featureVec`, `normalizedSet` | `''' + OGR + r'''` | ''' + lines(OGR, ['featureVec', 'normalizedSet']) + r''' |
| `transpose_unitary` | `''' + OGI + r'''` | ''' + lines(OGI, ['transpose_unitary']) + r''' |
| `FibreGram`, `RealizableGram`, `fibreGram_apply`, `sh1_necessity` | `''' + TSG + r'''` | ''' + lines(TSG, ['FibreGram', 'RealizableGram', 'fibreGram_apply', 'sh1_necessity']) + r''' |

| file at `D` | blob |
| --- | --- |
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
| `verification/lean/dita_defect_probe.py` | `''' + blob('verification/lean/dita_defect_probe.py') + r'''` |
| `.github/workflows/verify.yml` | `''' + blob('.github/workflows/verify.yml') + r'''` |

The names this round introduces return nothing from `git grep -l` at `D`: `DitaArcExclusivity`,
`act-37`, `A37-`, `a37_` and `dita_arc_exclusivity`.

***

## Why this round exists

Act 36 ran an exact one-parameter family `Pu u = SIG ∘ u^W` of realizable classes through the
certified rational stratum point, every member a `2 × 8` column Diţă matrix at the frozen index
maps, and found by its probe that the named point `P = Pu u₆₀` admits no factorization but that
one; it recorded open whether every realizable class near the stratum lies in some Diţă hull of
some factorization. The natural extension of act 36's evidence is not that the arc escapes every
hull — it lies in the frozen `2 × 8` hull by act 36's own theorem — but that the arc is
**exclusive** to it: that at every unit parameter other than the base point the arc point is a
Diţă matrix for the frozen class and its transpose orientation and for no other index maps at
all. The pre-freeze work at `D` took a census of every Diţă structure of the stratum point,
deduplicated it modulo the certified stabilizer, and found, by an exact monomial calculus, that
each of the eight other classes is excluded along the arc by a single monomial condition
`u^{±1} = 1`, that every unit at which any other structure could appear lies in an explicit set of
twenty points, and that at each of them the exhaustive search finds only the frozen class away
from `u = 1`. This round freezes that: eight kernel exclusions, the symmetry and the persistence of
the arc in the kernel, and the exhaustive complement in the exact-computation layer; and it
records the exhaustion of the hierarchy as open, unchanged.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Every quantity below was computed at `D` from act 36's frozen probe objects, in exact arithmetic
throughout; the scripts are kept off the repository except the frozen probe.

- **The census.** Act 36's exhaustive search at `SIG` finds 18 exact Diţă structures: 4 of shape
  `4 × 4`, 2 of `8 × 2` and 3 of `2 × 8` in the column form, and the same 9 index sets in the row
  form, since `SIG` is symmetric; every one reconstructs `SIG` exactly from its factors with the
  trivial twist. Under the certified stabilizer of `SIG` in `G_ext`, of order 1024 and containing
  transposition, they form 9 orbits, each a structure paired with its own transpose. The frozen
  `2 × 8` class is one orbit, and the named point `P` lies in it and in no other.
- **The monomial calculus.** With `SIG`'s entries written as `i^p z^q w^r`, symbolically matching the
  numeric entries, and the arc's as `i^p z^q w^r u^k`: at a generic `u`, one `4 × 4` and one `8 × 2`
  block structure pass the proportionality test and fail the rank-one condition, and exactly one
  `2 × 8` structure, the frozen class, passes both. Each of the eight other census classes imposes,
  beyond the identities, between 4 and 40 non-identity conditions, every one of the form
  `u^k = 1` with `k ∈ {−1, 1}` and trivial constant part; the frozen class imposes none.
- **The candidate set.** Over every `n`-subset of columns, `n ∈ {4, 2, 8}`, and every pair of rows,
  the units at which the pair becomes proportional on the subset without being so generically,
  together with the units at which the two generic candidates satisfy the rank-one condition
  (`u = 1` alone), are twenty points: `u = ζ z^s w^t` with `ζ ∈ {1, i, −1, −i}`,
  `s ∈ {0, −1/2, −1}`, `t ∈ {0, ±1/2, ±1}`, twelve of them Gaussian rational and eight square roots
  outside `Q(i)`.
- **The exhaustive search at each candidate point**, symbolic: at `u = 1` the eighteen structures,
  as `(5, 4)`, `(3, 2)`, `(3, 3)`; at `u = −1` the same candidates as at `u = 1` but only the frozen
  class exact, `(5, 0)`, `(3, 0)`, `(3, 1)`; at every other candidate point `(1, 0)`, `(1, 0)`,
  `(1, 1)` with the frozen class the one exact structure. **The exact exceptional set is `{1}`.**
- **Controls.** The numeric search of act 36's probe, with factor unitarity, agrees with the symbolic
  one at all twelve Gaussian-rational candidate points; a genuine deformation inside each of the
  eight other classes — one twist phase moved to `u₅` — is unitary, off `SIG`, and found by the
  search in its own class; the search on `P^T = P` returns the column-form result; the classifier
  commutes with stabilizer elements; a perturbed index map, the frozen blocks with two columns
  exchanged between them, is admitted neither at generic `u` nor at `P`.
- **The kernel witnesses.** For each of the eight other classes, four entry positions
  `p₁, p₂, p₃, p₄` with `H p₁ · H p₂ = H p₃ · H p₄` forced by the class's Diţă form, all four
  entries of `SIG` in `{+1, −1}` so that the identity has rational constants, and `u`-exponent sums
  `{0, 1}`, so that the identity reads `±u/16 = ±1/16` and gives `u = 1` by one
  `linear_combination`.

None of this is a finding of the round. The route below is the freeze's reading of how the frozen
theorems are reached; the theorems and the probe decide.

***

## The configuration, FROZEN — act 29's product configuration over act 26's single carrier

- Act 36's frozen head, verbatim: act 35's head — act 34's tables and objects, then `Γ`, `N`,
  `gram`, `fl`, `dita`, `ditaT`, `Δc`, `Δr`, `F4` — followed by act 36's objects `dg`, `dgT`, `flg`,
  `r28`, `c28`, `dita28`, `r82`, `c82`, `dita82`, `z`, `w`, `SIG`, `Wt`, `Pu`, `u₆₀` and `P`.
- This round's objects, `let`-bound after it: for each of the eight other classes, the row map
  `r…` and the column map `c…` of the product carrier onto `Fin m × Fin n`, written as `4 × 4`
  lookup tables over the two coordinates of the index — a row `i = (i.1, i.2)` to its position
  and class `(a, b)`, a column `j` to its block and position `(c, d)` — and the class's Diţă form
  `dita… X Y D = Matrix.of fun i j => dg X Y D (r… i) (c… j)`:

| class | shape | column blocks | row classes | reading |
| --- | --- | --- | --- | --- |
''' + '\n'.join('| `%s` | `%s` | %s | %s | %s |' % c for c in CLS) + r'''

The frozen class itself, `2 × 8` with blocks `(0, 1, 2, 3, 8, 9, 10, 11)`, `(4, 5, 6, 7, 12, 13, 14, 15)`
and classes `(0, 8), …, (7, 15)`, is act 36's `dita28` at `r28`, `c28`.

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

The module `verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean` opens with exactly
`import OIBridge.DitaHierarchy`, its docstring, `namespace OIBridge`,
`namespace DitaArcExclusivity`, and the one `open`:

```lean
''' + P['OPEN'] + r'''
```

It carries no definition of any kind, no `variable`, no second `open` and no second `import`; every
theorem is followed by its `#print axioms` line. Each statement below is declared
`theorem NAME :` with no binder before the colon, and statements are compared after collapsing
whitespace. The `let`-bound tables inside a statement are part of the statement. Every statement's
head is act 36's frozen head followed by this round's objects, and `controls.py` checks the head
against act 36's text byte for byte.

### `P_R` — the package

The conjunction, over one head, of `SYM`, `PERSIST` and the eight exclusions `EXCL_k1`, `EXCL_k2`,
`EXCL_k3`, `EXCL_k4`, `EXCL_e1`, `EXCL_e2`, `EXCL_t2`, `EXCL_t3`:

''' + lean('P_R') + r'''
### `P_N` — its negation

''' + lean('P_N') + r'''
`P_N` is `P_R`'s negation pushed through the outer conjunction. `controls.py` rebuilds both from the
shared components and rejects any drift.

### `A37-1` — the arc is symmetric, required under `A37-EXCLUSIVITY-PROVED`

`SYM`, `a37_shared_symmetric` — for every `u`, `Pu u` equals its transpose, so that a row Diţă
form of `Pu u` at any index maps is a column Diţă form at the same maps:

''' + lean('SYM') + r'''
### `A37-2` — the frozen class persists in both orientations, required under `A37-EXCLUSIVITY-PROVED`

`PERSIST`, `a37_shared_persistence` — for every unit `u`, `Pu u` is a `2 × 8` column Diţă matrix at
the frozen index maps with flat unitary factors and unit twists, and the transpose of one:

''' + lean('PERSIST') + r'''
### `A37-3` — each other class is admitted only at the base point, required under `A37-EXCLUSIVITY-PROVED`

For each of the eight classes, `EXCL_…`, `a37_shared_excl_…` — for every unit `u`, a Diţă form of
`Pu u` at the class's index maps with flat unitary factors and unit twists forces `u = 1`, and so
does the transpose of one:

''' + ''.join('`EXCL_%s`, `a37_shared_excl_%s`, the class `%s`:\n\n' % (nm, nm, nm) + lean('EXCL_' + nm) for nm, *_ in CLS) + r'''
### The control, required under both decided labels

`BASE`, `a37_control_base` — the family at `u = 1` is the stratum point, the Fourier factors are
flat unitaries, and the stratum point carries the Kronecker `4 × 4` factorization, class `k1`,
with those factors and the trivial twist, so that the exclusion of `k1` is sharp at `u = 1`:

''' + lean('BASE') + r'''
### The theorems, FROZEN by name and statement form

| role | theorem | statement |
| --- | --- | --- |
| `A37-EXCLUSIVITY-PROVED` | `a37_exclusivity` | `P_R` |
| `A37-EXCLUSIVITY-FAILS` | `a37_not_exclusivity` | `P_N` |
| corollary, required in every case | `a37_c_exclusive` | `(P_N) → ¬ (P_R)` |
| `A37-1`, required under `A37-EXCLUSIVITY-PROVED` | `a37_shared_symmetric` | `SYM` |
| `A37-2`, required under `A37-EXCLUSIVITY-PROVED` | `a37_shared_persistence` | `PERSIST` |
''' + '\n'.join('| `A37-3`, required under `A37-EXCLUSIVITY-PROVED` | `a37_shared_excl_%s` | `EXCL_%s` |' % (nm, nm) for nm, *_ in CLS) + r'''
| control, required under both decided labels | `a37_control_base` | `BASE` |

A module with neither verdict theorem reports `A37-UNDECIDED`, and a module with both is a failure
of the round. Every other theorem is named `a37_shared_…`, and every theorem is followed by its
`#print axioms` line.

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze, on disposable branches from `D` that are never landed.
Each is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design
evidence** recorded here: none is a `check-run` attestation, and no predicate of the round reads
them.

The design file is `verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean` on those branches;
the branches also carry a disposable census family for the module and, on the probe's design head,
the frozen probe wired into the workflow, none of which is part of the freeze except the probe and
its wiring.

@@RUNS@@

***

## The exact-computation layer — the frozen probe

`verification/lean/dita_arc_exclusivity_probe.py`, blob **`@@PROBE_BLOB@@`**, is written before
`F` and added by the execution at stage 1 with exactly this blob, and `.github/workflows/verify.yml`
at `E` is `D`'s with the two lines `echo "=== dita_arc_exclusivity_probe.py ==="` and
`python3 dita_arc_exclusivity_probe.py` inserted after act 36's probe in the
`Numerical probes / A36 hierarchy` shard, so that the shard runs it at every execution commit from
stage 1 on, and so at `E`. `F` carries this file alone and no probe; the runs at `F` exercise the
shard at `D`'s list. The probe's design run before `F` is recorded in the runs table above. Its
first part is act 36's probe head verbatim — the exact Gaussian rationals, act 36's exhaustive
structure search and its stabilizer construction — and it uses Python integers and fractions for
every value it asserts, no floating point anywhere, and exits 1 on any mismatch with the values
frozen here. Its statements are exact arithmetic replayed; they are not kernel-certified, and the
result note names them as this layer's.

**0. Act 36's stabilizer, replayed**: the factor stabilizer products 256 for each of the four
operations without factor exchange and 0 with it; the order **1024**.

**1. The census.** The symbolic entries `i^p z^q w^r` equal the numeric entries of `SIG`; `SIG`
and `W` are symmetric; the exact structures by shape and form are **4, 4, 2, 2, 3, 3**; every one
reconstructs `SIG` exactly with trivial twist; the column- and row-form index sets coincide; the
stabilizer permutes the eighteen with **9** orbits of size 2, each a structure and its transpose;
the frozen class is one orbit; the other classes are four `4 × 4`, two `8 × 2`, two `2 × 8`.

**2. The arc.** `Pu 1 = SIG`, `P = Pu u₆₀`, `P` and `Pu u₅` unitary and symmetric; `P` and `Pu u₅`
admit exactly the frozen class.

**3. The generic point and the obstructions.** At a generic `u`: `(1, 0)`, `(1, 0)`, `(1, 1)`, the
one exact structure the frozen class; each other class imposes non-identity conditions all of the
form `u^k = 1`, `k ∈ {−1, 1}`, in the counts **20, 4, 36, 24, 40, 8, 20, 20** for `k1`, `k2`, `k3`,
`k4`, `e1`, `e2`, `t2`, `t3`; the frozen class imposes none; and the kernel witness identity of each
class is forced by its Diţă form, has rational entries and exponent sums `{0, 1}`:

| class | kind | positions `p₁, p₂, p₃, p₄` | exponent sums | `linear_combination` coefficient |
| --- | --- | --- | --- | --- |
''' + '\n'.join(witrow(nm) for nm, *_ in CLS) + r'''

**4. The candidate set.** The generic `4 × 4` and `8 × 2` candidates satisfy the rank-one condition
at `u = 1` only; the candidate exceptional set is exactly, in the probe's order,
`''' + '`, `'.join(E_CAND) + r'''`; twelve are Gaussian rational.

**5. The exact exceptional set.** At `u = 1`: `(5, 4)`, `(3, 2)`, `(3, 3)`; at `u = −1`: `(5, 0)`,
`(3, 0)`, `(3, 1)` with the frozen class the one exact structure; at every candidate point other
than `u = 1` exactly the frozen class is admitted; **the exact exceptional set is `{1}`**.

**6. Controls.** The numeric search agrees with the symbolic one at all twelve Gaussian-rational
candidates; a genuine deformation inside each other class is unitary, off `SIG` and found in its
class; the search on `P^T` returns `P`'s result; the classifier commutes with three stabilizer
elements, one of each kind; the perturbed index map is admitted neither at generic `u` nor at `P`;
the frozen maps are admitted at generic `u`.

The probe reports @@NPASS@@ `PASS` and no `FAIL`, runs in about @@PROBE_MIN@@ minutes, and ends
with the line `dita_arc_exclusivity_probe: OK …` on success, which the result note carries
verbatim, and `dita_arc_exclusivity_probe: FAILED …` with the failing checks otherwise.

***

## The question, FROZEN — one target

### `A37` — the exclusivity of the `2 × 8` arc

**Along act 36's arc `Pu u = SIG ∘ u^W` through the certified rational stratum point: is the arc
symmetric; does the frozen `2 × 8` factorization persist at every unit `u` in both orientations;
and, for each of the eight other factorization classes of the stratum point, does a Diţă form of
`Pu u` at that class's index maps, in either orientation, force `u = 1` — while, under every
decided label, the base point `Pu 1 = SIG` carries the Kronecker `4 × 4` factorization with flat
unitary factors?**

The answer is reported as one of three labels:
- `A37-EXCLUSIVITY-PROVED`, the theorem `P_R`;
- `A37-EXCLUSIVITY-FAILS`, the theorem `P_N`;
- `A37-UNDECIDED`.

Beside the label, the exact-computation layer's statement stands or falls with the probe: green,
it establishes that the exceptional set of the arc is exactly `{1}` and that at every unit `u ≠ 1`
no index maps whatever admit a Diţă form of `Pu u` but the frozen class's; red at `E`, the round
halts.

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| the base point | `a37_control_base` | `Pu 1 = SIG` carries class `k1` with flat unitary factors, so the exclusion of `k1` is sharp at `u = 1`, required whichever label is earned |
| the named point | act 36's `a36_shared_point`, and the probe's counts at `P` and `Pu u₅` | two points of the arc off the base, each admitting exactly the frozen class |
| the census is not vacuous | the probe's `(5, 4)`, `(3, 2)`, `(3, 3)` at `u = 1` | the same search finds the eighteen structures of the stratum point |
| the symbolic search is the numeric one | the probe's agreement at the twelve Gaussian-rational candidates | the monomial calculus, without factor unitarity, returns what act 36's search returns with it |
| each other class is reachable | the probe's genuine deformations, one per class | a point of each class's hull off `SIG` is found by the search in its class, so a class the search fails to find at an arc point is absent, not invisible |
| transpose and equivalence invariance | the probe's checks on `P^T` and on three stabilizer transports | the classifier gives the same answer under the allowed row and column operations |
| a wrong map fails | the probe's perturbed index map | the frozen blocks with two columns exchanged are admitted nowhere |
| the witnesses are forced | the probe's witness check | each kernel identity is a consequence of its class's Diţă form with rational constants and exponent sums `{0, 1}` |
| duality | `a37_c_exclusive` and `controls.py` | the two verdicts cannot both be earned |

***

## The route, recorded as the freeze's reading and not as a finding

1. **`SYM`.** `Pu u` is `F4 z i.1 j.1 · F4 w i.2 j.2 · u^{Wt i j}`; `F4 t` is symmetric for every `t`,
   by `fin_cases` on its two indices, and `Wt i j = Wt j i` since its condition and its value are
   symmetric in `i` and `j`; the transpose entry is the entry.
2. **`PERSIST`.** The column form is the first component of act 36's `a36_shared_line_core` at
   `z`, `w`, `u`; the row form is the same witnesses under `SYM`: `Pu u = (Pu u)^T = (dita28 X Y D)^T`.
3. **`EXCL_…`.** From a Diţă form `Pu u = dita… X Y D` at the class's maps, the four entries at the
   witness positions of the table above factor as `X a c · D c b · Y c b d`, and the product of the
   first two equals the product of the last two identically (`ring`), because they pair the same
   factors: for a proportionality witness the two rows are in one class and the two columns in one
   block, for a rank-one witness the four rows `(a,b), (0,0), (a,0), (0,b)` sit in one column. The
   same four entries of `Pu u` are `±(1/4)·u^k` with the exponent sums `{0, 1}`, so the identity reads
   `±u/16 = ±1/16` and `linear_combination` with the coefficient of the table gives `u = 1`. The
   transpose orientation reduces to the column one by `SYM` and `Matrix.transpose_transpose`.
4. **`BASE`.** `Pu 1 = SIG` by act 36's `a36_shared_one_core`; the flatness of `F4 z`, `F4 w` by act
   35's `a35_shared_f4_flat` and `a35_shared_half`; the Kronecker identity entrywise, the two lookup
   tables of `k1` returning `i.1` and `i.2` by `fin_cases`, then `mul_one`.
5. **`a37_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

No route to `A37-EXCLUSIVITY-FAILS` is expected. The freeze's reading is that `P_R` holds.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| every `a37_shared_…` and every `a37_c_…` other than `a37_c_exclusive` | either verdict theorem; `a37_c_exclusive` |
| every `a37_control_…` | either verdict theorem; `a37_c_exclusive` |
| `a37_not_exclusivity` | `a37_shared_symmetric`, `a37_shared_persistence`, every `a37_shared_excl_…` |
| `a37_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A37` | `A37-EXCLUSIVITY-PROVED` | **very high** | the symmetry is a finite check; the persistence is act 36's theorem with the symmetry; each exclusion is one forced product identity with rational constants, verified in exact arithmetic before the freeze, and every frozen statement was proved on a disposable branch before the freeze, with every named result within the three axioms |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A37-EXCLUSIVITY-PROVED`

> ''' + T['SENTENCES']['A37-EXCLUSIVITY-PROVED'] + r'''

### `A37-EXCLUSIVITY-FAILS`

> ''' + T['SENTENCES']['A37-EXCLUSIVITY-FAILS'] + r'''

### `A37-UNDECIDED`

> ''' + T['SENTENCES']['A37-UNDECIDED'] + r'''

### The corollary, REQUIRED

`a37_c_exclusive : (P_N) → ¬ (P_R)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label, and the probe's
summary line `dita_arc_exclusivity_probe: OK …` from the run at `E`.

| row | outcome |
| --- | --- |
| 1 | `A37-EXCLUSIVITY-PROVED` |
| 2 | `A37-EXCLUSIVITY-FAILS` |
| 3 | `A37-UNDECIDED` |

***

## The `P0` row, per case

At `D`, the `P0` cell of `verification/ROADMAP.md` ends with act 36's sentence and its standing
clause:

> ''' + T['P0_END_D'] + r'''

**On a decided outcome**, this round's sentence for the case is appended once after that standing
clause, followed by its own standing clause:
- **`A37-EXCLUSIVITY-PROVED`:**

  > ''' + T['P0_CASE']['A37-EXCLUSIVITY-PROVED'] + ' ' + T['P0_STANDING_37'] + r'''

- **`A37-EXCLUSIVITY-FAILS`:**

  > ''' + T['P0_CASE']['A37-EXCLUSIVITY-FAILS'] + ' ' + T['P0_STANDING_37'] + r'''

**On `A37-UNDECIDED`** the cell is not touched.

The expected `ROADMAP.md` at `E` is `D`'s with that sentence appended, or `D`'s unchanged, byte for
byte. Rehearsed at `D`, the two decided cells give these blobs:
- `@@ROAD_PV@@` (`A37-EXCLUSIVITY-PROVED`);
- `@@ROAD_FL@@` (`A37-EXCLUSIVITY-FAILS`).

The guard run locally at `D` against each rehearsed cell reports 91 PASS and 0 FAIL, the tags in
`D`'s order; the guard is not changed by this round.

***

## What no outcome licenses

- **No outcome revises act 36's `A36-HIERARCHY`, act 35's `A35-DITA-STRATIFIED`, act 34's
  `A34-STRATIFIED`, act 33's `A33-CLASSIFIED`, act 32's `A32-NOT-RIGID` or any verdict of acts 28 to
  31.** Those are the verdicts those rounds recorded, and they stand.
- **No outcome decides whether the hierarchy exhausts the realizable classes near the stratum.**
  Whether every realizable class near the stratum lies in some Diţă hull of some factorization is
  recorded open; the arc lies in the frozen `2 × 8` hull and escapes no hull.
- **No outcome says anything about Diţă's construction beyond the frozen statements**: what is
  established is that the arc is exclusive to its `2 × 8` class, by the kernel for the eight other
  classes of the stratum point and by the probe for every other index map.
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
- change the workflow beyond the two lines that wire the probe;
- import any Mathlib module into the frozen module beyond what `DitaHierarchy` imports;
- search for, name or freeze any arc other than act 36's.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks; act 36's head and
this round's maps and forms for the eight classes are `let`-bound inside each statement that uses
them.

## Evidence level

**2** for the module — Lean theorems, kernel-checked, every named result printing its axioms, each
within `propext`, `Classical.choice` and `Quot.sound`. The probe's statements are exact arithmetic
replayed in CI, a separate layer named as such wherever they are cited.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-37-arc-exclusivity/controls.py`, blob
**`@@CONTROLS_BLOB@@`**, is written before `F` and added by the execution with exactly this blob.
- It imports nothing from the repository and changes nothing.
- It reads `D` and the commit under check through `git`.
- It embeds every frozen text it compares against.

`controls.py check <commit>` fails unless all of the following hold:

- **The duality and the single source.**
  - The frozen `P_R` is the conjunction, over the frozen head, of the ten package texts, and
    `P_N` the disjunction of their negations, rebuilt from the shared components.
  - Every other statement carries the one head verbatim; the head is act 36's frozen head, byte
    for byte, followed by this round's objects.
- **The module**:
  - begins with the frozen import and carries the one frozen `open`;
  - has no forbidden command or token;
  - has a `#print axioms` line for every theorem;
  - uses only the frozen names or `a37_shared_…`;
  - gives each frozen theorem its frozen statement, the statement ending at the `:=` that opens
    its proof and not at a `let` inside it;
  - has at most one verdict theorem, and `a37_c_exclusive`;
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
- **The probe** has its frozen blob, and **the workflow** is `D`'s with the two lines inserted.
- **The census** is `D`'s with exactly one family appended, last, for `DitaArcExclusivity`:
  `kernel-only`, no manuscript anchor, and its note naming the label and no other.
- **`OIBridge.lean`** is `D`'s with `import OIBridge.DitaArcExclusivity` inserted directly after
  `import OIBridge.DitaHierarchy`.
- **The paths** changed from `D` are exactly these:
  - added: the three record files, the module and the probe;
  - modified: `OIBridge.lean`, the census and the workflow;
  - modified on a decided outcome only: `ROADMAP.md`.

`controls.py --self-test` also does four things:
- it checks the constants against this preregistration, beside it;
- it checks the duality and single source of the frozen texts, together with 8 duality
  mutations, each of which must be rejected;
- it builds a synthetic execution for each of the three rows and requires every one to hold;
- it applies @@NMUTS@@ mutation controls, each of which must fail with its named code.

Run at `D` beside this file, it prints:

```text
controls: the two verdict propositions are duals and every shared text has one source; 8 duality mutations fail as required
controls: 3 rows hold as frozen, @@NMUTS@@ mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear
commits from `F`, each with one parent:

1. **Stage 1 — the module, the controls and the probe.**
   - `controls.py` with its frozen blob.
   - The probe with its frozen blob, and the two workflow lines that wire it.
   - The module with the frozen header and its shared lemmas. On the route to
     `A37-EXCLUSIVITY-PROVED` these include `A37-1`, `A37-2`, the eight `A37-3` and the control.
   - The import line.

   No verdict theorem and no corollary `a37_c_exclusive`.
2. **Stage 2 — the verdict.** `a37_exclusivity` or `a37_not_exclusivity`, or neither, and
   `a37_c_exclusive`.
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
| the probe is the frozen one and runs green | `C3`: the probe's blob at stage 1 and at `E`; the `Numerical probes / A36 hierarchy` shard green at every execution commit and at `E` with the probe's `OK` line in its log |
| the frozen propositions elaborate as frozen | before `F`: the elaboration run above; at `E`: `C8`, every frozen theorem compiled under its statement |
| every verdict and control is kernel-checked, within the three axioms | `C8`: the dispatch run at `E`, the `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the statements, duality, corollary, controls and outcome grammar hold | `C9`: `controls.py check E` prints `controls: check OK` |
| the surfaces are exactly the frozen ones for the case, and the guard is untouched | `C9` |
| the guard stays green | `C8`: 91 checks, all `PASS`, in `D`'s order |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen propositions unchanged** is repaired by later
  linear commits before `E`.
- **A verdict that cannot be obtained** is reported `A37-UNDECIDED`, with the step named. In that
  case `ROADMAP.md` is not touched.
- **A decided label whose required statements are not all proved** is not reported; it is
  `A37-UNDECIDED` with the missing statement named. A verdict prints only over green controls,
  the probe among them.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target.
  It is any of these:
  - a frozen proposition that is ill-typed or cannot be stated as frozen;
  - a required statement or control that is false as frozen when the route through it is taken —
    in particular `BASE` false as frozen, which no label absorbs;
  - the probe red at `E` with the frozen blob — in particular an exact exceptional set other than
    `{1}` (Hazard 2).

  The round then halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
'''
open(os.path.join(S, 'preregistration.draft.md'), 'w', encoding='utf-8').write(doc)
print('draft lines', doc.count('\n'))
