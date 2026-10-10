"""Write rec/result.md for A39-REALIZABLE-PROVED. Reads runs39.txt (the stage runs table) and the probe log."""
import importlib.util, os, re, hashlib
S = os.path.dirname(os.path.abspath(__file__)) + '/'
spec = importlib.util.spec_from_file_location('c39', S + 'rec/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
L = C.PROVED
def blob_of(path):
    b = open(path, 'rb').read(); return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
log = open(S + 'probe39.log', encoding='utf-8').read()
probeline = [l for l in log.split('\n') if l.startswith('dita_torus_probe: OK')][0]
npass = len(re.findall(r'(?m)^\s+PASS\s', log))
RUNS = open(S + 'runs39.txt', encoding='utf-8').read().strip()
bad, rows, dmuts, muts = C.self_test()
assert bad == [], bad
CL = '> **' + C.MENTION + ' — the result note.**\n' + '\n'.join('> ' + l for l in C.CLAUSE.split('\n'))
road = blob_of(S + 'roadmap-%s.md' % L)
note = r'''# Track B act 39 — the three-parameter realizable family through the product-embedded stratum point: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #767. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A39.json`, and on the pull request.

- **`D`** — `08a7707dfe282f85c14e598f93cc27113ad00157`, the head of `main` after the landing of #766.
- **`F`** — `7deb404e9c772ce3f7ae65c89509d9dd3965f16e`, the child of `D` that adds the
  preregistration alone, blob `''' + blob_of(S + 'rec/preregistration.md') + r'''`. `F`'s `check-run`
  attestation is run 36415055421; the owner's designation is comment 5869013084 on #767.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A39-REALIZABLE-PROVED`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A39` | `A39-REALIZABLE-PROVED`, theorem `a39_realizable` | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a39_c_exclusive` and the three statements required under this label:
`A39-1`, `a39_shared_realizable`; and the controls `a39_control_base` and `a39_control_diagonal`.

***

## The frozen post-round sentence

> ''' + C.SENTENCES[L] + r'''

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `H3 u₁ u₂ u₃ = SIG ∘ u₁^{Ea} u₂^{Eb} u₃^{Ec}` is
the family, `Ea`, `Eb`, `Ec` act 38's pieces `A`, `B`, `C` in closed form on the product index, and
`SIG = F₄(z) ⊗ F₄(w)` the certified rational stratum point, act 38's head carried verbatim inside
every statement.

**`A39-1`, `a39_shared_realizable`.** With `z`, `w`, `u₁`, `u₂` and `u₃` symbolic units,
`star x = x⁻¹` for each (`a39_shared_inv_of_unit`) and `x ≠ 0` (`a39_shared_ne_zero_of_unit`). For
each row `(a, b)` and each column block `c`, the four entries `((a,b), (c,d))` of `H3 · H3^*` are
sums of sixteen monomials in the five units and their inverses with rational coefficients, and equal
`[ (a,b) = (c,d) ]`: a four-case split on `d`, `simp` with the product-sum expansion, the star
rewrites and the conjugates of `1/2` and `2`, then `field_simp` and `ring`
(`a39_shared_row_core_00_0` to `a39_shared_row_core_33_3`, sixty-four lemmas). They assemble into the
sixteen rows (`a39_shared_row_core_00` to `a39_shared_row_core_33`), the four row blocks
(`a39_shared_rowblock_core_0` to `a39_shared_rowblock_core_3`) and all rows
(`a39_shared_rows_core`), and the unitarity follows by `ext` (`a39_shared_unitary_core`). Flatness is
act 35's `a35_shared_half` twice with `‖uₖ‖ = 1` for each `k` (`a39_shared_flat_core`); the
realizable Gram and the feature vector are act 35's `a35_shared_gram_realizable`
(`a39_shared_real_core`), instantiated at `z`, `w` by act 36's unit lemmas. The identity holds with
`z` and `w` symbolic because every joint level set cancels monomial by monomial, as the probe checks.

**The controls.** `a39_control_base`: `H3 1 1 1 = SIG` entrywise by `one_pow` and `mul_one`
(`a39_shared_base_core`). `a39_control_diagonal`: `H3 u u u = Hu u` entrywise, `u^(Ea + Eb + Ec)`
split by `pow_add` twice and closed by `ring` (`a39_shared_diag_core`).

**`a39_realizable`** is `a39_shared_real_core` over the frozen head; **`a39_c_exclusive`**: `P_N` is
the negation of `P_R`.

**Zero definitions.** The module carries one hundred and one theorems, each followed by its
`#print axioms` line, each within `propext`, `Classical.choice` and `Quot.sound`.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a39_shared_…` or `a39_control_…` consumes a verdict theorem or
`a39_c_exclusive`, and `a39_c_exclusive` consumes neither verdict theorem. Beside Mathlib and this
round's own shared lemmas, the module consumes only `a35_shared_half`, `a35_shared_norm_of_unit`,
`a35_shared_gram_realizable`, `a36_shared_z_unit` and `a36_shared_w_unit`, all listed under
Provenance. No deviation.

***

## The exact-computation layer

The frozen probe `verification/lean/dita_torus_probe.py`, blob `''' + C.PROBE_BLOB + r'''`, is added at
stage 1 and run in act 38's shard `Numerical probes / A38 escape`, directly after act 38's probe.
Its run at the stage commits reports ''' + str(npass) + r''' `PASS` and no `FAIL` and ends with the line

```text
''' + probeline + r'''
```

These are exact arithmetic replayed, not kernel-certified: act 36's stabilizer replayed, order 1024;
the pieces `A`, `B`, `C` disjoint with sum `E`, their rows, columns and supports, and the nine joint
difference triples; **the 552 joint level sets of the 256 ordered row pairs, none failing**, in
exact Gaussian rationals and monomial by monomial in `z` and `w`; and the controls — `H3(1, 1, 1) =
SIG`, the diagonal equal to act 38's arc at `u₅`, `u₆₀`, `−1` and `i`, exact unitarity at four
Gaussian-rational points off the diagonal, non-unitarity at `u₁ = 2`, the eight single- and
two-variable subfamilies with 512, 312, 352, 384, 424, 440, 480 and 536 level sets and none failing,
the countercontrol with one entry of `C` cleared failing on 60 level sets and not unitary at
`(u₅, w, u₁₇)`, and the 16 merged diagonal level sets, of two columns each, each cancelling on its
own. The probe's count is the certificate of the identity the kernel proves.

**Not claimed**, recorded as such: which points of the three-torus admit a Diţă structure; any
transfer of act 38's exclusion off `{1, −1}` from the diagonal to the generic point of the family,
to any other point off the diagonal, or to any subfamily; the exponent matrices with entries in
`{0, 1}`; and the minimality of support 48.

***

## The `P0` cell and the guard

On `A39-REALIZABLE-PROVED` this round's sentence and its standing clause are appended once after act
38's standing clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E` is
`''' + road + r'''`, the blob rehearsed for this case in the preregistration.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The workflow at `E` is `D`'s with the two frozen lines
that run the probe in act 38's shard.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `''' + blob_of(S + 'rec/preregistration.md') + r'''`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `''' + blob_of(S + 'rec/controls.py') + r'''` at stage 1, as frozen.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 12 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, ''' + str(muts) + r''' mutation controls fail as required` and
    `controls: self-test OK`.
  - At stage 1 `controls.py`'s module checks report only the corollary that stage 2 adds; from
    stage 2 on, none.
- **`C3`:** the probe has blob `''' + C.PROBE_BLOB + r'''` at stage 1; its run is green at the stage
  commits with the line above.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on fourteen receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A39-REALIZABLE-PROVED`, less this note:
  - added: the preregistration, `controls.py`, the module and the probe;
  - modified: `OIBridge.lean`, the census, the workflow and `ROADMAP.md`.

The guard, run locally at stage 3, reports `ALL CHECKS PASS` in `D`'s order. That run is evidence
for the executor and not an attestation.

''' + RUNS + r'''

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

None.

''' + CL + '\n'
open(S + 'rec/result.md', 'w', encoding='utf-8').write(note)
print('note_ok:', C.note_ok(note, L)); print('bytes', len(note.encode()))
