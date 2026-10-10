"""Assemble the A39 preregistration from the single proposition source (props39.json, texts39.json).
Placeholders @@RUNS@@, @@CONTROLS_BLOB@@, @@PROBE_BLOB@@, @@NMUTS@@, @@NPASS@@, @@ROAD_PV@@, @@ROAD_FL@@ are filled by
fill_prereg39.py once the runs, controls.py and the probe are final. Line numbers of the locating table are read from the D
worktree at generation time."""
import json, os, re, subprocess
S = os.path.dirname(os.path.abspath(__file__))
WT = os.path.join(S, '..', 'wt-d39')
P = json.load(open(os.path.join(S, 'props39.json')))
T = json.load(open(os.path.join(S, 'texts39.json')))
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
DLE = 'verification/lean-mathlib/OIBridge/DitaLocalEscape.lean'
DAE = 'verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean'
DHI = 'verification/lean-mathlib/OIBridge/DitaHierarchy.lean'
DH = 'verification/lean-mathlib/OIBridge/DitaHull.lean'
OGR = 'verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean'
TSG = 'verification/lean-mathlib/OIBridge/TwoSidedGauge.lean'
PV, FL, UN = 'A39-REALIZABLE-PROVED', 'A39-REALIZABLE-FAILS', 'A39-UNDECIDED'

doc = r'''# Track B act 39 — the three-parameter realizable family through the product-embedded stratum point: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
''' + q(T['CLAUSE']) + r'''

## The declarations

```v3-round
round A39
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-39-realizable-torus/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-39-realizable-torus/
record AM verification/receipts/A39.json
execution A verification/lean-mathlib/OIBridge/DitaTorus.lean
execution A verification/lean/dita_torus_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
execution M verification/ROADMAP.md
```

The record directory holds three files: this preregistration, the round's frozen controls
`controls.py`, and the result note. The receipt path is `verification/receipts/A39.json`. Every
other path the round changes is an execution path listed above. The guard,
`verification/lean/edge_rigidity_probe.py`, is not governed and is not changed: at `E` it is byte
for byte `D`'s, and `controls.py` checks that it is. The workflow changes by two lines: the round's
probe runs in act 38's shard `probes_a38`, `Numerical probes / A38 escape`, directly after act 38's
probe, so that the shard, which the aggregate `Numerical probes` job already requires, fails unless
both probes are green; `controls.py` checks that the workflow at `E` is `D`'s with exactly that
frozen edit. The probe takes a few seconds; no shard of its own is needed.

`ROADMAP.md` changes only on a decided outcome, and only as this file freezes: by the `P0` sentence
for the case, appended to the cell. The three entries the roadmap records at `D` as separate future
directions — the census of exponent matrices with entries in `{0, 1}`, the minimality of support
48, and the stronger multi-parameter geometry — are not edited by this round.

## The objects

- **`D`** = `08a7707dfe282f85c14e598f93cc27113ad00157`: the head of `main` after the landing of pull
  request #766, which recorded those three directions in the roadmap and changed no mathematical
  claim; its first parent is act 38's landing `6e8ce41d`, `A38-NON-DITA-WITNESS-PROVED`. It is
  certified by push run 36412115126: all eight jobs green, the release gate passing with fourteen
  receipts holding, the `Mathlib bridge` build green with `lean-axioms` at 4951 named results and
  no sorry, the guard `ALL CHECKS PASS`, and act 38's probe reporting its `OK` line. Every
  measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A39.json`.

No other round runs beside A39 at this freeze. Should one land first, its movement of `main`
enters A39 only by reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — realizability only.** This round asks one question: is
`H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` a complex Hadamard matrix, with realizable Gram family and
feature vector in the product normalized set, at every point `(u₁, u₂, u₃)` of the three-torus? It
freezes nothing else as a conclusion. Four things are **excluded** from the round, as statements,
as dependencies and as readings of its outcome:
- **the `{0, 1}` census** — no count, enumeration or classification of exponent matrices with
  entries in `{0, 1}` is claimed or used;
- **support-48 minimality** — nothing is claimed about whether a realizable non-Diţă line through
  `SIG` with smaller support exists;
- **the Diţă locus in the three-torus** — which points `(u₁, u₂, u₃)` admit a Diţă structure, of any
  shape, index map or orientation, is not classified, not bounded and not sampled by this round;
- **the generic three-parameter behaviour** — act 38 proved that its arc, the diagonal
  `u₁ = u₂ = u₃`, admits no Diţă structure off `{1, −1}`; nothing here claims that this describes
  the generic point of the three-parameter family, or any point off the diagonal.

A read-only, exact measurement of the Diţă locus runs separately from this round. Its result is
neither consumed nor asserted here, and it seeds a later round rather than this one.

**Hazard 2 — the two layers, never merged.** The kernel proves the realizability: for each of the
256 entries of `H3 · H3^*`, a sum of sixteen monomials in `z`, `w`, `u₁`, `u₂`, `u₃` and their
inverses, the identity `(H3 · H3^*) i j = [i = j]` with `z`, `w`, `u₁`, `u₂`, `u₃` symbolic units.
The exact-computation probe certifies the same identity in its structural form: for every ordered
pair of rows `(r, s)`, the columns grouped by their **joint** exponent-difference triple
`(A_rj − A_sj, B_rj − B_sj, C_rj − C_sj)` have pair sums `Σ SIG_rj · conj(SIG_sj)` equal to
`16 · [r = s]` on the zero triple and `0` on every other triple — **552 joint level sets, none
failing**, both in exact Gaussian rationals and monomial by monomial in `z` and `w`. The probe's
count is the exact-computation certificate; the kernel's theorem is the proof; the result note
names each as its own layer.

**Hazard 3 — the controls are controls.** The family passes through the stratum point,
`H3 1 1 1 = SIG`, and its diagonal is act 38's arc, `H3 u u u = Hu u`; both are required kernel
statements, frozen as **controls** and not as conclusions. The single-variable and two-variable
subfamilies — `E` in one variable, `A`, `B`, `C` alone, `(A, B)`, `(A, C)`, `(B, C)` and
`(A + B, C)` — are checked by the probe as controls of the joint test, with their own level-set
counts; none is an additional conclusion of the round.

**Hazard 4 — the joint test is strictly stronger than the line tests.** On the diagonal the joint
triples `(1, −1, 0)` and `(−1, 1, 0)` project to the same integer as the zero triple, so act 38's
one-variable identity alone does not see their separate cancellation. The probe computes those
merged level sets directly — 16 of them, each of two columns — and checks that each cancels on its
own. A countercontrol clears one entry of `C`, at row `1`, column `2`: the joint identity then fails
on 60 level sets and `H3` is not unitary at the Gaussian-rational point `(u₅, w, u₁₇)`.

**Hazard 5 — history.** Act 38 recorded `A38-NON-DITA-WITNESS-PROVED`, act 37
`A37-EXCLUSIVITY-PROVED`, act 36 `A36-HIERARCHY`, act 35 `A35-DITA-STRATIFIED`, act 34
`A34-STRATIFIED`, act 33 `A33-CLASSIFIED`, act 32 `A32-NOT-RIGID`, acts 29 to 31 their
product-configuration verdicts. All stand as recorded. A decided outcome here extends act 38's arc
to a family containing it, and is never a revision of an earlier round's verdict.

**Hazard 6 — vocabulary.** A class is a pair of index maps, a family is a map from a torus to
matrices, a realizable matrix is a flat unitary on the carrier, an isometry is not a symmetry, the
group acting is not a symmetry group of anything physical, and none is written as the other.

***

## Provenance

The following are consumed as frozen declarations and frozen theorems, never re-proved and never
paraphrased:

- **act 12 and act 17** — `FibreGram`, `RealizableGram`, `fibreGram_apply`, `sh1_necessity`;
- **act 26**, `OrbitGeometryRigidity.lean` — `featureVec` and `normalizedSet`;
- **act 35**, `DitaHull.lean` — `a35_shared_half`, `a35_shared_norm_of_unit` and
  `a35_shared_gram_realizable`;
- **act 36**, `DitaHierarchy.lean` — `a36_shared_z_unit` and `a36_shared_w_unit`;
- **act 38**, `DitaLocalEscape.lean` — its head, carrying act 36's head and act 37's tables, and
  its objects `Ew` and `Hu`, which this round carries verbatim; no theorem of it is consumed by a
  proof;
- **Mathlib** — `Matrix.of`, `Matrix.of_apply`, `Matrix.unitaryGroup`,
  `Matrix.mem_unitaryGroup_iff`, `Matrix.mul_apply`, `Matrix.one_apply`, `Matrix.star_apply`,
  `Fintype.sum_prod_type`, `Fin.sum_univ_four`, `Fin`, the star, norm and field lemmas of `ℂ`
  (`Complex.star_def`, `Complex.ext_iff`, `norm_mul`, `norm_pow`, `one_pow`, `mul_one`, `pow_add`,
  `eq_inv_of_mul_eq_one_left`, `mul_zero`, `zero_ne_one`, `map_ofNat` and their kin), and the
  tactics `fin_cases`, `simp`, `decide`, `ring`, `field_simp`, `norm_num` and `ext`.

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| `a38_shared_realizable`, `a38_c_local_escape`, `a38_control_base`, `a38_witness`, `a38_c_exclusive` | `''' + DLE + r'''` | ''' + lines(DLE, ['a38_shared_realizable', 'a38_c_local_escape', 'a38_control_base', 'a38_witness', 'a38_c_exclusive']) + r''' |
| `a36_shared_z_unit`, `a36_shared_w_unit` | `''' + DHI + r'''` | ''' + lines(DHI, ['a36_shared_z_unit', 'a36_shared_w_unit']) + r''' |
| `a35_shared_half`, `a35_shared_norm_of_unit`, `a35_shared_gram_realizable` | `''' + DH + r'''` | ''' + lines(DH, ['a35_shared_half', 'a35_shared_norm_of_unit', 'a35_shared_gram_realizable']) + r''' |
| `featureVec`, `normalizedSet` | `''' + OGR + r'''` | ''' + lines(OGR, ['featureVec', 'normalizedSet']) + r''' |
| `FibreGram`, `RealizableGram`, `fibreGram_apply`, `sh1_necessity` | `''' + TSG + r'''` | ''' + lines(TSG, ['FibreGram', 'RealizableGram', 'fibreGram_apply', 'sh1_necessity']) + r''' |

| file at `D` | blob |
| --- | --- |
| `DitaLocalEscape.lean` | `''' + blob(DLE) + r'''` |
| `DitaArcExclusivity.lean` | `''' + blob(DAE) + r'''` |
| `DitaHierarchy.lean` | `''' + blob(DHI) + r'''` |
| `DitaHull.lean` | `''' + blob(DH) + r'''` |
| `OrbitGeometryRigidity.lean` | `''' + blob(OGR) + r'''` |
| `TwoSidedGauge.lean` | `''' + blob(TSG) + r'''` |
| `verification/lean-mathlib/OIBridge.lean` | `''' + blob('verification/lean-mathlib/OIBridge.lean') + r'''` |
| `verification/lean-manuscript-census.json` | `''' + blob('verification/lean-manuscript-census.json') + r'''` |
| `verification/ROADMAP.md` | `''' + blob('verification/ROADMAP.md') + r'''` |
| `verification/lean/edge_rigidity_probe.py` | `''' + blob('verification/lean/edge_rigidity_probe.py') + r'''` |
| `verification/lean/dita_local_escape_probe.py` | `''' + blob('verification/lean/dita_local_escape_probe.py') + r'''` |
| `.github/workflows/verify.yml` | `''' + blob('.github/workflows/verify.yml') + r'''` |

The names this round introduces return nothing from `git grep -l` at `D`: `DitaTorus`, `act-39`,
`A39-`, `a39_` and `dita_torus`.

***

## Why this round exists

Act 38 wrote its witness exponent matrix as `E = A + B + C`, three disjoint pieces with entries in
`{0, 1}`, each of support 16, and proved the arc `SIG ∘ u^E` realizable at every unit `u`. It
recorded that the three-parameter family `SIG ∘ u₁^A u₂^B u₃^C` was not frozen, since its
realizability needs its own multivariate identity: the one-variable identity cancels level sets of
the summed exponent difference, and a joint level set is finer. This round freezes that identity.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Every quantity below was computed at `D` from act 38's frozen probe objects, in exact arithmetic;
the scripts are kept off the repository except the frozen probe.

- **The pieces.** On the entry `((a,b),(c,d))`, rows `i = 4a+b` and columns `j = 4c+d`:
  `A = [a odd][b = 3][c odd]` on rows `7, 15` and columns `4, 5, 6, 7, 12, 13, 14, 15`;
  `B = [a = 2][d = 1]` on rows `8, 9, 10, 11` and columns `1, 5, 9, 13`;
  `C = [a+b odd][(c,d) ∈ {(0,2),(2,0)}]` on rows `1, 3, 4, 6, 9, 11, 12, 14` and columns `2, 8`.
  They are disjoint, each of support 16, and `A + B + C = E`.
- **The joint difference triples.** Over all ordered row pairs the triples that occur are the zero
  triple, `±(1, 0, 0)`, `±(0, 1, 0)`, `±(0, 0, 1)` and `±(1, −1, 0)`; the last, the only mixed one,
  arises where `A` and `B` meet, at columns 5 and 13.
- **The gate.** For every ordered row pair, including `r = s`, and every joint triple, the pair sum
  is `16 · [r = s]` on the zero triple and `0` otherwise: **552** joint level sets, **0** failures,
  in exact Gaussian rationals and monomial by monomial in `z` and `w`.
- **The subfamilies**, each in its own variables, level sets and failures: `E` in one variable
  512 and 0; `A` 312 and 0; `B` 352 and 0; `C` 384 and 0; `(A, B)` 424 and 0; `(A, C)` 440 and 0;
  `(B, C)` 480 and 0; `(A + B, C)` 536 and 0.
- **The merged triples** under the diagonal projection: `(1, −1, 0)` and `(−1, 1, 0)`, 16 level sets
  of two columns each, every one cancelling on its own.
- **The countercontrol**: `C` with its entry at row 1, column 2 cleared fails on 60 level sets.

None of this is a finding of the round. The route below is the freeze's reading of how the frozen
theorems are reached; the theorems and the probe decide.

***

## The configuration, FROZEN — act 29's product configuration over act 26's single carrier

- Act 38's frozen head, verbatim: act 36's head — act 35's head, then `dg`, `dgT`, `flg`, `r28`,
  `c28`, `dita28`, `r82`, `c82`, `dita82`, `z`, `w`, `SIG`, `Wt`, `Pu`, `u₆₀`, `P` — act 37's row
  map, column map and Diţă form for each of the eight classes other than the frozen one, and act
  38's `Ew` and `Hu`.
- This round's objects, `let`-bound after it:

```lean
''' + CO['HEAD39'].rstrip('\n') + r'''
```

`Ea`, `Eb`, `Ec` are `A`, `B`, `C` in closed form on the product index, and `Ew` is textually
`Ea + Eb + Ec` entry by entry; `H3 u₁ u₂ u₃ = SIG ∘ u₁^{Ea} u₂^{Eb} u₃^{Ec}` is the family.

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

The module `verification/lean-mathlib/OIBridge/DitaTorus.lean` opens with exactly
`import OIBridge.DitaLocalEscape`, its docstring, `namespace OIBridge`, `namespace DitaTorus`, and
the one `open`:

```lean
''' + P['OPEN'] + r'''
```

It carries no definition of any kind, no `variable`, no second `open` and no second `import`; every
theorem is followed by its `#print axioms` line. Each statement below is declared
`theorem NAME :` with no binder before the colon, and statements are compared after collapsing
whitespace. The `let`-bound tables inside a statement are part of the statement. Every statement's
head is act 38's frozen head followed by this round's objects, and `controls.py` checks the head
against act 38's text byte for byte.

### `P_R` — the package

`REAL` over the head:

''' + lean('P_R') + r'''
### `P_N` — its negation

''' + lean('P_N') + r'''
`P_N` is `P_R`'s negation. `controls.py` rebuilds both from the shared components and rejects any
drift.

### `A39-1` — the family is realizable, required under `A39-REALIZABLE-PROVED`

`REAL`, `a39_shared_realizable` — for all units `u₁`, `u₂`, `u₃`, `H3 u₁ u₂ u₃` is unitary with
every entry of norm `1/4`, its Gram family is a realizable Gram over the product carrier, and its
feature vector lies in the product normalized set:

''' + lean('REAL') + r'''
### The controls, required under both decided labels

`BASE`, `a39_control_base` — the family passes through the stratum point:

''' + lean('BASE') + r'''
`DIAG`, `a39_control_diagonal` — its diagonal is act 38's arc:

''' + lean('DIAG') + r'''
### The theorems, FROZEN by name and statement form

| role | theorem | statement |
| --- | --- | --- |
| `A39-REALIZABLE-PROVED` | `a39_realizable` | `P_R` |
| `A39-REALIZABLE-FAILS` | `a39_not_realizable` | `P_N` |
| corollary, required in every case | `a39_c_exclusive` | `(P_N) → ¬ (P_R)` |
| `A39-1`, required under `A39-REALIZABLE-PROVED` | `a39_shared_realizable` | `REAL` |
| control, required under both decided labels | `a39_control_base` | `BASE` |
| control, required under both decided labels | `a39_control_diagonal` | `DIAG` |

A module with neither verdict theorem reports `A39-UNDECIDED`, and a module with both is a failure
of the round. Every other theorem is named `a39_shared_…`, and every theorem is followed by its
`#print axioms` line.

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze, on disposable branches from `D` that are never landed.
Each is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design
evidence** recorded here: none is a `check-run` attestation, and no predicate of the round reads
them.

The design file is `verification/lean-mathlib/OIBridge/DitaTorus.lean` on those branches; the
branches also carry a disposable census family for the module and, on the probe's design head, the
frozen probe wired into the workflow, none of which is part of the freeze except the probe and its
wiring.

@@RUNS@@

***

## The exact-computation layer — the frozen probe

`verification/lean/dita_torus_probe.py`, blob **`@@PROBE_BLOB@@`**, is written before `F` and added
by the execution at stage 1 with exactly this blob, and `.github/workflows/verify.yml` at `E` is
`D`'s with the two lines that run it in act 38's shard, directly after act 38's probe, the frozen
edit `controls.py` embeds, so that the shard runs the probe at every execution commit from stage 1
on, and so at `E`. `F` carries this file alone and no probe; the runs at `F` exercise the workflow
at `D`. Its first part is act 38's probe head verbatim — act 36's exact Gaussian rationals and
structure search, act 37's monomial calculus and act 38's pieces and arc — and it uses Python
integers and fractions for every value it asserts, no floating point anywhere, and exits 1 on any
mismatch with the values frozen here. Its statements are exact arithmetic replayed; they are not
kernel-certified, and the result note names them as this layer's.

**0. Act 36's stabilizer, replayed** as in act 38's head: the factor stabilizer products 256 for
each of the four operations without factor exchange and 0 with it; the order **1024**.

**1. The pieces.** `A + B + C = E`, entries in `{0, 1}`, disjoint; rows, columns and support of each
as above; the joint difference triples, exactly the nine named.

**2. Realizability on the three-torus.** The joint level-set identity in exact Gaussian rationals:
**552** level sets, **0** failures; and monomial by monomial in `z` and `w`, the form of the kernel
proof: **552** and **0**.

**3. Controls.** `H3(1, 1, 1) = SIG`; `H3(u, u, u) = SIG ∘ u^E` at `u₅`, `u₆₀`, `−1` and `i`; `H3`
exactly unitary at four Gaussian-rational points off the diagonal; not unitary at `u₁ = 2`; the
eight subfamilies with the counts above and no failure; the countercontrol, 60 failures and not
unitary at `(u₅, w, u₁₇)`; the merged triples `(−1, 1, 0)` and `(1, −1, 0)`, 16 level sets of two
columns, each cancelling.

The probe reports @@NPASS@@ `PASS` and no `FAIL`, runs in seconds, and ends with the line
`dita_torus_probe: OK …` on success, which the result note carries verbatim, and
`dita_torus_probe: FAILED …` with the failing checks otherwise.

***

## The question, FROZEN — one target

### `A39` — the three-parameter family is realizable on the whole torus

**For act 38's three exponent pieces `A`, `B`, `C` and the family
`H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point: is
`H3 u₁ u₂ u₃` a complex Hadamard matrix — a flat unitary, whose Gram family is realizable and whose
feature vector lies in the product normalized set — at every point `(u₁, u₂, u₃)` of the
three-torus, while, under every decided label, the family passes through `SIG` at `(1, 1, 1)` and
its diagonal is act 38's arc?**

The answer is reported as one of three labels:
- `A39-REALIZABLE-PROVED`, the theorem `P_R`;
- `A39-REALIZABLE-FAILS`, the theorem `P_N`;
- `A39-UNDECIDED`.

Beside the label, the exact-computation certificate stands or falls with the probe: green, it
establishes the 552 joint level-set cancellations of Hazard 2; red at `E`, the round halts.

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| the base point | `a39_control_base` | the family passes through the stratum point, required whichever label is earned |
| the diagonal | `a39_control_diagonal` | the family contains act 38's arc on its diagonal, required whichever label is earned |
| the exact values | the probe's unitarity at four Gaussian-rational points off the diagonal | the theorem's content is checked at points it quantifies over, independently of the level-set count |
| the unit hypothesis is used | the probe's non-unitarity at `u₁ = 2` | the statement is not true off the torus, so the hypothesis carries weight |
| the joint test is finer than the line test | the probe's merged triples | the level sets the diagonal merges cancel separately |
| a wrong matrix fails | the probe's countercontrol | one entry of `C` cleared, 60 level sets fail and `H3` is not unitary at a named point |
| the subfamilies | the probe's eight subfamily counts | each single-variable and two-variable restriction passes its own joint test; none is a conclusion |
| duality | `a39_c_exclusive` and `controls.py` | the two verdicts cannot both be earned |

***

## The route, recorded as the freeze's reading and not as a finding

1. **`REAL`.** With `z`, `w`, `u₁`, `u₂`, `u₃` symbolic units, `star x = x⁻¹` for each
   (`a39_shared_inv_of_unit`) and `x ≠ 0` (`a39_shared_ne_zero_of_unit`); for each row `(a, b)` and
   each column block `c`, the entries `((a,b), (c,d))` of `H3 · H3^*` over the four `d` are sums of
   sixteen monomials in the five units and their inverses with rational coefficients, and equal
   `[ (a,b) = (c,d) ]`: by `fin_cases` on `d`, `simp` with the sum expansions and the star
   rewrites, `field_simp` and `ring` — sixty-four lemmas `a39_shared_row_core_ab_c`, assembled into
   sixteen row lemmas, four row-block lemmas and the rows (`a39_shared_rows_core`), then the
   unitarity by `ext` (`a39_shared_unitary_core`); flatness from `a35_shared_half` twice and
   `‖uₖ‖ = 1` for each `k` (`a39_shared_flat_core`); the realizable Gram and the feature vector from
   act 35's `a35_shared_gram_realizable` (`a39_shared_real_core`), instantiated at `z`, `w` by act
   36's unit lemmas.
2. **`BASE`.** Entrywise by `one_pow` and `mul_one`.
3. **`DIAG`.** Entrywise, `u^(Ea + Eb + Ec) = u^Ea · u^Eb · u^Ec` by `pow_add` twice, then `ring`.
4. **`a39_c_exclusive`**: `P_N` is the negation of `P_R`.

No route to `A39-REALIZABLE-FAILS` is expected. The freeze's reading is that `P_R` holds.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| every `a39_shared_…` | either verdict theorem; `a39_c_exclusive` |
| every `a39_control_…` | either verdict theorem; `a39_c_exclusive` |
| `a39_not_realizable` | `a39_shared_realizable` |
| `a39_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A39` | `A39-REALIZABLE-PROVED` | **very high** | the realizability is a finite polynomial identity in five symbolic units, verified in exact arithmetic level set by level set and monomial by monomial before the freeze, and every frozen statement was proved on a disposable branch before the freeze, with every named result within the three axioms |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A39-REALIZABLE-PROVED`

> ''' + T['SENTENCES'][PV] + r'''

### `A39-REALIZABLE-FAILS`

> ''' + T['SENTENCES'][FL] + r'''

### `A39-UNDECIDED`

> ''' + T['SENTENCES'][UN] + r'''

### The corollary, REQUIRED

`a39_c_exclusive : (P_N) → ¬ (P_R)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label, and the probe's
summary line `dita_torus_probe: OK …` from the run at `E`.

| row | outcome |
| --- | --- |
| 1 | `A39-REALIZABLE-PROVED` |
| 2 | `A39-REALIZABLE-FAILS` |
| 3 | `A39-UNDECIDED` |

***

## The `P0` row, per case

At `D`, the `P0` cell of `verification/ROADMAP.md` ends with act 38's sentence and its standing
clause:

> ''' + T['P0_END_D'] + r'''

**On a decided outcome**, this round's sentence for the case is appended once after that standing
clause, followed by its own standing clause:
- **`A39-REALIZABLE-PROVED`:**

  > ''' + T['P0_CASE'][PV] + ' ' + T['P0_STANDING_39'] + r'''

- **`A39-REALIZABLE-FAILS`:**

  > ''' + T['P0_CASE'][FL] + ' ' + T['P0_STANDING_39'] + r'''

**On `A39-UNDECIDED`** the cell is not touched.

The expected `ROADMAP.md` at `E` is `D`'s with that sentence appended, or `D`'s unchanged, byte for
byte. Rehearsed at `D`, the two decided cells give these blobs:
- `@@ROAD_PV@@` (`A39-REALIZABLE-PROVED`);
- `@@ROAD_FL@@` (`A39-REALIZABLE-FAILS`).

The guard run locally at `D` against each rehearsed cell reports `ALL CHECKS PASS`, the tags in
`D`'s order; the guard is not changed by this round.

***

## What no outcome licenses

- **No outcome revises act 38's `A38-NON-DITA-WITNESS-PROVED` or any earlier verdict.**
- **No outcome says which points of the three-torus admit a Diţă structure.** In particular, no
  outcome carries act 38's exclusion off `{1, −1}` from the diagonal to the generic point of the
  family, to any other point off the diagonal, or to any subfamily.
- **No outcome counts, classifies or minimizes.** Nothing is claimed about the exponent matrices
  with entries in `{0, 1}`, about the minimality of support 48, or about the orbits of such
  matrices; each stays the separate direction the roadmap records.
- **No outcome classifies the classes of the product normalized set or its isometries.**
- **No outcome reports anything about transition families or dynamics.** Nothing here establishes
  that any admissible law is covariant under any isometry or reaches any class, and none closes
  `P0`, which stays `OPEN`.
- **No family, factorization, class, isometry, group or covariance is called canonical, physical or
  fundamental.**

## Non-doings

This round does not do any of the following:
- define anything, or restate any rung or declaration;
- read any configuration but the one frozen;
- edit any closed round's record;
- edit the guard, or the roadmap's recorded directions;
- write any manuscript file;
- change the workflow beyond the two lines that run the probe;
- import any Mathlib module into the frozen module beyond what `DitaLocalEscape` imports;
- measure, freeze or cite the Diţă locus of the family.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks; act 38's head and
this round's `Ea`, `Eb`, `Ec` and `H3` are `let`-bound inside each statement that uses them.

## Evidence level

**2** for the module — Lean theorems, kernel-checked, every named result printing its axioms, each
within `propext`, `Classical.choice` and `Quot.sound`. The probe's statements are exact arithmetic
replayed in CI, a separate layer named as such wherever they are cited.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-39-realizable-torus/controls.py`, blob
**`@@CONTROLS_BLOB@@`**, is written before `F` and added by the execution with exactly this blob.
- It imports nothing from the repository and changes nothing.
- It reads `D` and the commit under check through `git`.
- It embeds every frozen text it compares against.

`controls.py check <commit>` fails unless all of the following hold:

- **The duality and the single source.**
  - The frozen `P_R` is the package `REAL` over the frozen head, and `P_N` its negation, rebuilt
    from the shared components.
  - Every other statement carries the one head verbatim; the head is act 38's frozen head, byte for
    byte, followed by this round's objects.
- **The module**:
  - begins with the frozen import and carries the one frozen `open`;
  - has no forbidden command or token;
  - has a `#print axioms` line for every theorem;
  - uses only the frozen names or `a39_shared_…`;
  - gives each frozen theorem its frozen statement, the statement ending at the `:=` that opens
    its proof and not at a `let` inside it;
  - has at most one verdict theorem, and `a39_c_exclusive`;
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
- **The probe** has its frozen blob, and **the workflow** is `D`'s with the frozen edit.
- **The census** is `D`'s with exactly one family appended, last, for `DitaTorus`: `kernel-only`, no
  manuscript anchor, and its note naming the label and no other.
- **`OIBridge.lean`** is `D`'s with `import OIBridge.DitaTorus` inserted directly after
  `import OIBridge.DitaLocalEscape`.
- **The paths** changed from `D` are exactly these:
  - added: the three record files, the module and the probe;
  - modified: `OIBridge.lean`, the census and the workflow;
  - modified on a decided outcome only: `ROADMAP.md`.

`controls.py --self-test` also does four things:
- it checks the constants against this preregistration, beside it;
- it checks the duality and single source of the frozen texts, together with 12 duality
  mutations, each of which must be rejected;
- it builds a synthetic execution for each of the three rows and requires every one to hold;
- it applies @@NMUTS@@ mutation controls, each of which must fail with its named code.

Run at `D` beside this file, it prints:

```text
controls: the two verdict propositions are duals and every shared text has one source; 12 duality mutations fail as required
controls: 3 rows hold as frozen, @@NMUTS@@ mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear
commits from `F`, each with one parent:

1. **Stage 1 — the module, the controls and the probe.**
   - `controls.py` with its frozen blob.
   - The probe with its frozen blob, and the two workflow lines that run it.
   - The module with the frozen header and its shared lemmas. On the route to
     `A39-REALIZABLE-PROVED` these include `A39-1` and the two controls.
   - The import line.

   No verdict theorem and no corollary `a39_c_exclusive`.
2. **Stage 2 — the verdict.** `a39_realizable` or `a39_not_realizable`, or neither, and
   `a39_c_exclusive`.
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
- **A verdict that cannot be obtained** is reported `A39-UNDECIDED`, with the step named. In that
  case `ROADMAP.md` is not touched.
- **A decided label whose required statements are not all proved** is not reported; it is
  `A39-UNDECIDED` with the missing statement named. A verdict prints only over green controls,
  the probe among them.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target.
  It is any of these:
  - a frozen proposition that is ill-typed or cannot be stated as frozen;
  - a required statement or control that is false as frozen when the route through it is taken —
    in particular `BASE` or `DIAG` false as frozen, which no label absorbs;
  - the probe red at `E` with the frozen blob — in particular a joint level-set count other than
    552 or any failing level set (Hazard 2).

  The round then halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
'''
open(os.path.join(S, 'preregistration.draft.md'), 'w', encoding='utf-8').write(doc)
print('draft lines', doc.count('\n'))
