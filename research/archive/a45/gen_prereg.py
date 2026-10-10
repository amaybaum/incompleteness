import json, subprocess, sys
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/a45/'
fr = json.load(open(S + 'frozen.json')); tx = json.load(open(S + 'texts.json'))
edits = {p: r for p, r in json.load(open(S + 'edits.json'))}
def blob(p): return subprocess.run(['git', 'hash-object', p], capture_output=True, text=True).stdout.strip()
PROBE_BLOB, REF_BLOB, CTRL_BLOB = blob(S + 'fixed_basis_ancilla_probe.py'), blob(S + 'TrackBQfbBridge.lean'), blob(S + 'controls.py')
PRED = sys.argv[1] if len(sys.argv) > 1 else None   # the predicted-tree run row, once measured
CLAUSE, SENT = tx['CLAUSE'], tx['SENTENCES']
P, U = 'A45-BRIDGE-PROVED', 'A45-UNDECIDED'
defs = '\n\n'.join(fr['defs'].values())
stmts = '\n\n'.join(v + ' …' for v in fr['statements'].values())
def ins_block(path, k=0):
    return '```text\n' + edits[path][k][1] + '\n```'
ROAD = edits['verification/ROADMAP.md'][0][1]

pre_rows = """| 36595682134 | `fa26d6a3` on `claude/a45-bridge-dev` | the first design module, 19 theorems | red: two rewrites of `born` across the dependent field `Bas` failed; every other theorem compiled |
| 36596287670 | `68cf4596` | the repaired module, 19 theorems | `Mathlib bridge` build green; `lean-axioms` at 5270 named results, no sorry, every theorem of the module within `[propext, Classical.choice, Quot.sound]`; the gate red only at `lean-manuscript` (module unclassified) |
| 36598896118 | `a77a7dfd` | adds the converse: `realData_bornPow_one`, `realData_rooted_one`, `slice_eq_of_rooted_eq`, `rooted_eq_iff_slice_eq` | build green; `lean-axioms` 5274, no sorry; red only at `lean-manuscript` |
| 36599732472 | `8863c9c9` | adds `rootTraj_congr`, `bridge_traj`, `realData_traj_stochastic` | build green; `lean-axioms` 5277, no sorry, 26 theorems within the three axioms; red only at `lean-manuscript` |
| 36609040917 | `d7f33158` on `claude/a45-manuscript-draft` | the manuscript rehearsal: the frozen insertions below, the census family and the `P0` sentence, on the 26-theorem module; `.tex`/`.pdf` not rebuilt | 20 of 21 gate steps green, `lean-manuscript`, `voice`, `claims`, `mirror`, `citation` among them; red only at `staleness` |"""
pred_row = PRED or ("| 36612901341 | `ad64b60319e1ff2d40a5a5eed8e3aa4bfcf30b0e` on `claude/a45-predicted`, tree `12a695df15fcfc0634f6b0d7953c03482d980101` | "
 "**the predicted execution tree less the result note**: the reference implementation `9d6086bbe3af28e576adf2fb51784b02a5d66e5f`, the probe `8419549b598131a4bdef36e8c9ce82690cdaac6c`, "
 "`controls.py` `95ee78b284b4aec3ec487effd6018feb76c6e986`, the workflow `876f2e6d15ea30a435c868cc29ed4d0dacf98ae3` (`D`'s with the frozen edit), `OIBridge.lean` `0c400130d920b0b8bad9c70d6dab5cdf2f156ad3`, "
 "the census `bd4258a761ec0a533fb7fb6b9d25bae588d6811c`, `ROADMAP.md` `4e53a3b266d2b63ab1f1aa7728de329298e9fcf9`, `Main.md` `536e5f59c958cf1ea9790f89a592a2a448e5993d`, `Explainer.md` `83f99188c7e0cad114cb26fd959bed9bb2d29756`, "
 "`ch01-observation.md` `bffa69f3f2a3cb9cecc76d6a362b728a7ac369a5`, `ch19-open-problems.md` `f7bf7a7cfd7cd02ebe6e2e06128b16ecfd226175`, `FULL.md` `75c8e4c32e263bb243b476e4fe209c11b6a301c4`, "
 "`Main`, `Explainer` and the book rebuilt by `build.sh` (87, 67 and 540 pages), and this file's draft `2c0054744b887561d04130bb7ea82287d881b139`, before this row was filled | "
 "all thirteen jobs green: the `Mathlib bridge` (job 109558562718, 3 minutes 23 seconds) with the release gate passing all 21 steps — `staleness` (13 matched, 0 unstamped), `lean-manuscript`, `voice`, `claims`, `mirror` and `citation` among them — "
 "`lean-axioms` at 5278 named results and no sorry, each of the module's 27 axiom lines `[propext, Classical.choice, Quot.sound]`, seventeen receipts holding and the 303 legacy records intact; "
 "`Numerical probes / A45 ancilla` (job 109558562779, 11 seconds) with 16 `PASS`, no `FAIL` and the probe's `OK` line; the aggregate `Numerical probes` (job 109565848934) green; the kernel check and every other probe shard green |")

doc = f"""# Track B act 45 — the fixed-basis image of a single-time lift: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> {CLAUSE}

## The declarations

```v3-round
round A45
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/
record AM verification/receipts/A45.json
execution A verification/lean-mathlib/OIBridge/TrackBQfbBridge.lean
execution A verification/lean/fixed_basis_ancilla_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
execution M verification/ROADMAP.md
execution M papers/Main.md
execution M papers/Main.tex
execution M papers/Main.pdf
execution M papers/Explainer.md
execution M papers/Explainer.tex
execution M papers/Explainer.pdf
execution M book/ch01-observation.md
execution M book/ch19-open-problems.md
execution M book/The-Incompleteness-of-Observation-FULL.md
execution M book/The-Incompleteness-of-Observation-FULL.tex
execution M book/The-Incompleteness-of-Observation-FULL.pdf
```

The record directory holds three files: this preregistration, the round's frozen controls `controls.py`, and the
result note. The receipt path is `verification/receipts/A45.json`. Every other path the round changes is an execution
path listed above. The manuscripts, their built artifacts and `ROADMAP.md` change only on `{P}`.

The workflow changes by one frozen edit in five places: the round's probe runs in a shard of its own, `probes_a45`,
`Numerical probes / A45 ancilla`, inserted before the foundations shard, and the aggregate `Numerical probes` job lists
it in its `needs`, reads its result into its environment, echoes it and tests it for `success`. `controls.py` checks
that the workflow at `E` is `D`'s with exactly that edit.

## The objects

- **`D`** = `fa6ddf77703a8ce7f9eaf573ef48355194d72541`: the head of `main` after act 41's landing,
  `A41-CENSUS-CORRECTED`, receipt `verification/receipts/A41.json`; its parents are act 41's base `78ea3c39` and act
  41's receipt commit `f3eff7d3`. It is certified by push run 36573013258: twelve jobs green, the release gate passing
  21 of 21 steps with seventeen receipts holding and the 303 legacy records intact, `lean-axioms` at 5251 named results
  and no sorry. Every measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only `verification/receipts/A45.json`.

No other round runs beside A45 at this freeze. Should one land first, its movement of `main` enters A45 only by
reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — two layers, never merged.** The kernel proves the statements frozen below, at evidence level 2. The round's
probe computes, in exact arithmetic replayed in CI and not in the kernel, the ancilla boundary: an ancilla carried
between steps as hidden basis states separates two dilations of one slice at two steps, and a tensor-factor ancilla does
not. No kernel statement concerns a nontrivial ancilla, and nothing in the result note or the manuscripts says one does.
The corpus's own tensor-factor theorem, `padData_rooted` (`OperationalSourcing.lean`), is a landed kernel result the
manuscripts cite beside the probe; this round does not re-prove it.

**Hazard 2 — one instantiation, frozen.** The fixed-basis datum of a realization is `realData U`: evolution `U`, the
uniform initial law and the identity readout — the initial law and readout of the landed witness `hadData`. No landed
theorem names a map from Track-B realizations to `Q_fb`; this definition is the round's, frozen as text, and every
conclusion is about it. The generalization to arbitrary shared initial laws and readouts is not frozen and not claimed.

**Hazard 3 — directions (§A.34).** `rooted_eq_iff_slice_eq` is an equivalence with a witness for each direction:
forward, equal rooted families force equal slices (`slice_eq_of_rooted_eq`, through `realData_rooted_one`); backward,
equal slices give equal rooted families (`visible_congr`). The relation it identifies is equality of the visible slice.
No statement here derives a realization's class — two-sided, Diţă, or A41's factorization class — from its data, and
the round's own design evidence (act 45's research note, Q3) exhibits two realizations of one slice, a Diţă point and
the support-40 line, whose data agree and whose A41 classes differ.

**Hazard 4 — scope.** Trivial-ancilla admissible dilations only; interventions in `permClass`, the corpus's stated
access (`IsScaledPartialPerm`); the representational equivalence `S ⇔ D ⇔ Q_fb` is consumed as landed
(`finite_horizon_equivalence`), not re-proved. Excluded, as statements, dependencies and readings: interventions outside
`permClass`; any relation finer than equality of the slice adopted as the physical one; `P0`'s cross-time parts; any
selection principle.

**Hazard 5 — manuscripts.** The round writes six frozen insertions into five manuscript files and one sentence into
`ROADMAP.md`, rebuilt with `sh ./build.sh Main Explainer` and `sh ./build.sh --book`. The toolchain was measured at `D`
before this freeze: rebuilding `Main`, `Explainer` and the book from `D`'s sources reproduces `D`'s three `.tex` byte for
byte and their page counts (86, 67 and 539), the PDFs differing only in embedded timestamps.

**Hazard 6 — history.** Act 41 recorded `A41-CENSUS-CORRECTED`, act 40 `A40-LOCUS-CLASSIFIED`, act 39
`A39-REALIZABLE-PROVED`, act 38 `A38-NON-DITA-WITNESS-PROVED`, and earlier rounds their verdicts. All stand as recorded.
The pre-`D` research threads named A42 to A44 are not evidence here; act 45's research thread, from `D`, is design
evidence only.

***

## Provenance

Consumed as frozen declarations and theorems, never re-proved and never paraphrased:

- `QuantumRepresentation.lean` — `QfbData` and its `IsLaw`, `born`, `bornPow`, `rootMass`, `jointMass`, `rooted`,
  `rootTraj`, `chainW`, `PositiveRootMass`, `QStar`; `qfbRealizable_rootTraj`;
- `Equivalence.lean` — `QfbRealizable`, `Stochastic`, `Qfb_imp_S`;
- `DilationChoice.lean` — `AdmissibleDilationAt`;
- `SubstratumInterfaceAudit.lean` — `IsScaledPartialPerm`, `permClass`; `StructuralClosure.lean` — `IsSubmonomial`;
- `DitaHull.lean` — `a35_shared_pad_unitary`;
- `FiniteEntropy.lean` — `marg`;
- Mathlib — matrix, unitary-group, norm, sum and field lemmas of `ℂ` and `ℝ`, among them `Matrix.mem_unitaryGroup_iff`,
  `Matrix.star_eq_conjTranspose`, `Matrix.conjTranspose_smul`, `Matrix.smul_mul`, `Matrix.mul_smul`,
  `Matrix.mul_apply`, `Finset.sum_eq_single`, `Finset.sum_congr`, `Fintype.sum_prod_type`, `Fin.sum_univ_one`,
  `star_inv₀`, `star_ofNat`, `norm_mul`, `norm_inv`, `Complex.norm_ofNat`, `mul_pow`, `mul_one_div_cancel`,
  `one_div_ne_zero`, `div_self`, `Fintype.card_pos_iff`, `Fintype.card_ne_zero`, and the tactics `simp`, `rw`,
  `norm_num`, `positivity`, `induction`, `unfold`, `dsimp`, `ext`, `subst`.

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| `qfbRealizable_rootTraj` | `verification/lean-mathlib/OIBridge/QuantumRepresentation.lean` | 228 |
| `Qfb_imp_S`, `finite_horizon_equivalence` | `verification/lean-mathlib/OIBridge/Equivalence.lean` | 245, 459 |
| `AdmissibleDilationAt` | `verification/lean-mathlib/OIBridge/DilationChoice.lean` | 134 |
| `IsScaledPartialPerm`, `permClass` | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean` | 231, 236 |
| `IsSubmonomial` | `verification/lean-mathlib/OIBridge/StructuralClosure.lean` | 98 |
| `a35_shared_pad_unitary` | `verification/lean-mathlib/OIBridge/DitaHull.lean` | 122 |
| `padData_rooted` | `verification/lean-mathlib/OIBridge/OperationalSourcing.lean` | 476 |

| file at `D` | blob |
| --- | --- |
| `QuantumRepresentation.lean` | `e1338f54af1df896d5e3c237ec00ed6e3d69dbf2` |
| `Equivalence.lean` | `08b9c358feb378bb4cce300ad548594cd3c5040f` |
| `DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `SubstratumInterfaceAudit.lean` | `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| `StructuralClosure.lean` | `d6999cd1bd13013851aa7833c0ae062e60a4b35b` |
| `DitaHull.lean` | `5404decfe03ddced08aa4143a549601766fc9785` |
| `OperationalSourcing.lean` | `2ab6113754874ff6a83956ef8f2227578d089547` |
| `verification/lean-mathlib/OIBridge.lean` | `d605af03ab1211bbfe7b0c5d9843aeb86ebc29e1` |
| `verification/lean-manuscript-census.json` | `d36a579f91ee4ab7d641a05986d142fe5e5cc26f` |
| `verification/ROADMAP.md` | `0a2e0ec9d2c5ce82f9d2db0f20be0c0d841b2e18` |
| `.github/workflows/verify.yml` | `d9e372f1dc4ba5b45031d5b7f5d87dc78fd6d854` |
| `papers/Main.md` | `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` |
| `papers/Explainer.md` | `b0926875346305ef053995fc10695353df64de68` |
| `book/ch01-observation.md` | `355d1c58dc09c4b6128fde2de55475aa673e4315` |
| `book/ch19-open-problems.md` | `7fda22cde84655d1d1de718b162d816f015e6f30` |
| `book/The-Incompleteness-of-Observation-FULL.md` | `9674614cbb55b58b7492f1e4b65a4f09e82e91b5` |

The names this round introduces return nothing from `git grep -l` at `D`: `TrackBQfbBridge`, `act-45`, `A45-`, `a45_`,
`fixed_basis_ancilla`, `realData_traj`, `bridge_traj` and `rooted_eq_iff_slice_eq`.

***

## Why this round exists

`S ⇔ D ⇔ Q_fb` (`finite_horizon_equivalence`) is the landed finite observable-law correspondence, and acts 11 to 41
classified the lift freedom a visible law leaves: at one time, the off-diagonal fibre-Gram data modulo phases, with
Diţă and factorization strata inside it. What was missing is a kernel construction taking a single-time lift into
`Q_fb` and a statement of what the instantiated data see. Act 45's research thread, from `D`, found that the adopted
operational data are visible-level (its Q1), that monomial access preserves visible equivalence while a row-non-monomial
intervention separates it (its Q2), and built the bridge in the kernel on disposable branches; its Q3 suite and ancilla
probe matched every preregistered cell. This round freezes that bridge, its manuscript propagation, and the probe.

***

## The frozen definitions and statements — the exact Lean text

The module is `verification/lean-mathlib/OIBridge/TrackBQfbBridge.lean`. Its header, up to `namespace OIBridge`, is
frozen byte for byte:

```lean
{fr['header']}```

**The definitions, FROZEN — the round's definition budget is exactly these four:**

```lean
{defs}
```

**The statements, FROZEN** — each theorem's text from `theorem` to the `:=` that opens its proof, byte for byte, shown
here with its proof elided:

```lean
{stmts}
```

### The theorems, FROZEN by name and role

| role | theorem |
| --- | --- |
| verdict `P_R`, `{P}` | `a45_bridge_kernel` |
| the bridge at trajectory laws | `bridge_traj`, `rootTraj_congr`, `bridge` |
| the converse at rooted families (§A.34, one witness per direction) | `rooted_eq_iff_slice_eq`; forward `slice_eq_of_rooted_eq`, backward `visible_congr` |
| the chain into `S` | `realData_traj_stochastic` |
| the flat 16 × 16 instance | `UH_unitary`, `UH_norm`, `UH_born_eq_slice`, `UH_admissible`, `flat_bridge` |
| the constructor | `realData_born`, `realData_isLaw`, `realData_rootMass`, `realData_positiveRootMass`, `realData_qstar` |
| supporting | `bornPow_congr`, `rooted_congr`, `slice_of_admissible`, `realData_bornPow_one`, `realData_rooted_one`, `exists_row_single`, `exists_col_single`, `mul_mul_apply_single`, `normSq_mul_mul_congr` |

Every theorem is followed by its `#print axioms` line. A proof-only repair may add theorems named `a45_shared_…`.

### The reference implementation

**Frozen**, and checked by `controls.py` at `E`: the header, the four definitions, the twenty-seven statement texts,
the theorem names, one `#print axioms` line per theorem, the forbidden tokens (`sorry`, `admit`, `native_decide`,
`axiom`, `unsafe`, `opaque`, `implemented_by`, `extern`), and no `set_option` but `linter.unusedSectionVars false`.

**Not frozen: the proofs.** The reference implementation is blob **`{REF_BLOB}`**: 27 theorems and the four
definitions. It is the module built green on the design branch at `8863c9c9` (26 theorems) with the round's docstring
and the verdict `a45_bridge_kernel` added. A proof-only repair — a change that leaves every frozen surface unchanged — is
permitted as a later linear commit before `E`; the result note names the reference blob and the module's blob at `E`,
and, if they differ, states the departure from the reference implementation and justifies it, which `controls.py`
checks.

### Pre-freeze evidence — design evidence, not attestation

Each run is a `workflow_dispatch` run whose `head_sha` is the commit named, on disposable branches never landed. None
is a `check-run` attestation, and no predicate of the round reads them.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
{pre_rows}
{pred_row}

The run 36612901341 is evidence for the blobs it names and nothing else: it did not test this file's final text, which
differs from the draft it carried only by the row above and this paragraph. The same tree was re-committed as two
linear commits from `D` on the disposable branch `claude/a45-predicted-b` — the first `D` plus this file's draft alone,
the second the execution, tree `12a695df` — after a first split was rejected by `controls.py` (`freeze:delta`: the
first commit had carried seven further files). On that branch, with a temporary result note carrying the `{P}`
sentence, the clause, the probe's line and the two blobs, `controls.py check HEAD --freeze` printed
`controls: check OK`; the note was not kept.

***

## The exact-computation layer — the frozen probe

`verification/lean/fixed_basis_ancilla_probe.py`, blob **`{PROBE_BLOB}`**, is written before `F` and added by the
execution at stage 1 with exactly this blob, and the workflow runs it in its own shard at every execution commit from
stage 1 on. It uses Python integers and fractions for every value it asserts, no floating point, and exits 1 on any
mismatch. Its statements are exact arithmetic replayed; they are not kernel-certified, and the result note names them as
this layer's. Sixteen checks:

1. **Trivial ancilla, replayed at points** (the kernel's objects; this does not stand in for the kernel): six flat
   16 × 16 realizations of `J/16` — `SIG`, a two-sided gauge `D₁ SIG D₂`, a relabelling, the Diţă point
   `H3(1, v₂, v₃)`, the support-40 line `SIG ∘ v^E40` and `i·SIG` — are flat unitaries (1a) with equal Born weights
   (1b), equal rooted families for `t ≤ 3` (1c), the one-step family `J/16` (1d), and equal rooted families after three
   pairs of monomial interventions (1e, 1f).
2. **Countercontrols**: an off-slice unitary gives a different rooted family (2a); a row-non-monomial `K = F4(i) ⊗ I4`
   separates **14** of the 15 pairs (2b).
3. **The ancilla boundary**: five dilations of `G = J/4` with a two-state ancilla, unitary and admissible (3a); the
   carried one-step family equals `G` on all five (3b); `D1` and `D2` share every `(·, a₀)` column and differ in a
   completion column (3c); at two steps `D1`'s row 0 is uniform and `D2`'s is **(17187, 6371, 23271, 20771)/67600**
   (3d); `D3` and `D4` (constant angle) agree (3e).
4. **The tensor-factor ancilla**: `(F/2) ⊗ W` with a rational rotation `W` is unitary and admissible (4a) and its carried
   rooted family equals `Gᵗ` for `t ≤ 3` (4b), as does the trivial-ancilla embedding (4c).

It ends with the line `fixed_basis_ancilla_probe: OK -- 16 checks: …` on success, which the result note carries
verbatim, and `fixed_basis_ancilla_probe: FAILED …` otherwise. It runs in about four seconds.

***

## The question, FROZEN — one target

### `A45` — the fixed-basis image of a single-time lift

**For a trivial-ancilla admissible dilation `pad U` of a visible slice `G`, and the fixed-basis datum `realData U`: are
its trajectory laws determined by `G`, also after `permClass` interventions on either side; do its rooted families
agree with a second such datum's exactly when the slices agree; and is each law `Q_fb`-realizable and stochastic? The
frozen answer is yes, as the package `P_R` = `a45_bridge_kernel` states.**

| direction or part | statement | witness | layer |
| --- | --- | --- | --- |
| slice ⇒ laws, with interventions | equal slices give equal trajectory laws after `permClass` interventions | `bridge_traj` | kernel, level 2 |
| slice ⇒ rooted | equal slices give equal rooted families | `visible_congr` | kernel, level 2 |
| rooted ⇒ slice | equal rooted families give equal slices | `slice_eq_of_rooted_eq` | kernel, level 2 |
| into `S` | each law `QfbRealizable` and `Stochastic` | `realData_traj_stochastic` | kernel, level 2 |
| flat instance | `U_H = H/4` unitary with Born weights `1/16` | `UH_unitary`, `UH_born_eq_slice` | kernel, level 2 |
| ancilla boundary | carried separates at two steps; tensor factor does not | the probe, sections 3 and 4 | exact computation, replayed in CI |

The answer is reported as one of two labels: `{P}`, the theorem `P_R` in the kernel with the probe green at
`E`; `{U}`. The probe is not a label: green at `E`, it certifies its layer; red at `E`, the round halts as a freeze
failure.

## The controls

| role | object | what it is for |
| --- | --- | --- |
| realizations of one slice agree | the probe's section 1 | the kernel's objects replayed at six exact points |
| an off-slice realization differs | the probe's 2a | the congruence is not vacuous |
| a non-licensed intervention separates | the probe's 2b | the `permClass` hypothesis is load-bearing |
| the carried ancilla separates | the probe's 3c, 3d | the trivial-ancilla hypothesis is load-bearing |
| the tensor-factor ancilla does not | the probe's 4a to 4c | the boundary is the carried non-product case, as `padData_rooted` states in the kernel |
| the manuscripts absorb the result | `lean-manuscript`, `voice`, `claims`, `mirror`, `staleness` in the release gate at `E` | propagation is checked, not asserted |
| the frozen surfaces | `controls.py check E` | the statements, definitions, surfaces, note and paths |

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A45` | `{P}` | **very high** | the 26 non-verdict theorems were built green on the design branch within the three axioms; the verdict is their conjunction; the probe was run green at the predicted tree; the manuscript rehearsal passed every gate step it could |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `{P}`

> {SENT[P]}

### `{U}`

> {SENT[U]}

### The outcome table

The result note carries exactly one line `**Outcome:** \\`LABEL\\`` for its label, the label's sentence, the clause at
its mention `**THE CLAUSE, carried at this mention — the result.**`, and the probe's summary line from the run at `E`.

| row | outcome |
| --- | --- |
| 1 | `{P}` |
| 2 | `{U}` |

***

## The manuscript propagation, FROZEN — on `{P}` only

Each insertion is placed immediately after its anchor, the text at `D` that precedes it; `controls.py` embeds each
anchor and insertion and checks that the file at `E` is `D`'s with exactly these insertions.

**`papers/Main.md`**, §3.4, the remark on the scope of representability, after *"… on a single visible law two lifts can
lie in different two-sided classes and differ in their relating evolution."*:

{ins_block('papers/Main.md')}

**`papers/Explainer.md`**, after *"… that residue is not inert, since two lifts of one visible law can differ in it and
differ in relating evolution."*:

{ins_block('papers/Explainer.md')}

**`book/ch01-observation.md`**, and its mirror in `book/The-Incompleteness-of-Observation-FULL.md`, after the same
sentence:

{ins_block('book/ch01-observation.md')}

**`book/ch19-open-problems.md`**, and its mirror in `book/The-Incompleteness-of-Observation-FULL.md`, after *"… the
off-diagonal fibre-Gram data modulo phases."*:

{ins_block('book/ch19-open-problems.md')}

**`verification/ROADMAP.md`** — appended to the `P0` status cell, after its standing clause *"… and nothing here names,
endorses or excludes a selection principle."*:

{'```text' + chr(10) + ROAD + chr(10) + '```'}

**The census.** `verification/lean-manuscript-census.json` gains one family, appended last, for `TrackBQfbBridge`,
`current`, with anchors `bridge_traj`, `rooted_eq_iff_slice_eq` and `realData_traj_stochastic` in `papers/Main.md`, the
first sentence of the Explainer and ch01 insertion in `papers/Explainer.md` and `book/ch01-observation.md`, and the
first sentence of the ch19 insertion in `book/ch19-open-problems.md`; and the family of `OperationalSourcing` moves from
`kernel-only` to `current` with the anchor `padData_rooted` in `papers/Main.md` (§A.35), since `Main` carries that
module's conclusion. On `{U}` the new family is appended `kernel-only` with no anchor, and nothing else changes.

**The build.** `sh ./build.sh Main Explainer` and `sh ./build.sh --book`; the release gate's `staleness` step at `E`
checks every `.tex` stamp against its source, and `controls.py` checks the three stamps and that the three PDFs changed.

***

## What no outcome licenses

- **No outcome revises any earlier verdict.**
- **No outcome says the kernel proves anything about a nontrivial ancilla**; the carried and tensor-factor computations
  are the probe's, and the tensor-factor kernel statement is the landed `padData_rooted`.
- **No outcome recovers a realization's class from its data** — two-sided, Diţă, or A41's factorization class.
- **No outcome adopts `realData`, visible equality, `permClass` or any carrier as the physical relation or access**, and
  none closes `P0`, which stays `OPEN`.
- **No outcome generalizes to arbitrary initial laws or readouts**, nor to interventions outside `permClass`.

## Non-doings

This round does not do any of the following:
- define anything beyond the four frozen definitions;
- edit any closed round's record;
- edit any manuscript beyond the six frozen insertions, or any built artifact except by `build.sh`;
- change the workflow beyond the frozen edit that adds the probe's shard;
- import into the module anything beyond the four frozen imports.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Four**: `realData`, `pad`, `IsFlatHadamard`, `UH`, frozen as text above; `controls.py` checks that the module carries
no other `def`, `abbrev`, `instance`, `structure`, `class` or `inductive`.

## Evidence level

**2** for the kernel layer — Lean theorems, kernel-checked, every named result printing its axioms, each within
`propext`, `Classical.choice` and `Quot.sound`. The probe's statements are exact arithmetic replayed in CI, a separate
layer named as such wherever they are cited.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/controls.py`, blob **`{CTRL_BLOB}`**, is written before
`F` and added by the execution with exactly this blob. It imports nothing from the repository and changes nothing; it
reads `D` and the commit under check through `git`; it embeds every frozen text it compares against.

`controls.py check <commit> [--freeze F]` fails unless all of the following hold:
- **the module**: the frozen header and four definitions, no other definition, no forbidden token or option, every
  theorem named in the frozen list or `a45_shared_…` with one `#print axioms` line, each frozen statement byte for byte,
  and the verdict present exactly under `{P}`;
- **the result note**: the outcome line once; the label's sentence once and no other label's; the clause after its
  mention; the probe's summary line; the reference blob and the module's blob at `E` in backticks, and, if they differ,
  the words *departure from the reference implementation*;
- **the probe** has its frozen blob; **the workflow** is `D`'s with the frozen edit; **`OIBridge.lean`** is `D`'s with
  `import OIBridge.TrackBQfbBridge` directly after `import OIBridge.DitaTorusLocus`; **the census** is `D`'s with the
  frozen transform for the label;
- **the manuscripts and `ROADMAP.md`** are `D`'s with the frozen insertions under `{P}`, and `D`'s under `{U}`;
  the three `.tex` stamps match their sources and, under `{P}`, the three PDFs changed;
- **the paths** changed from `D` are exactly the governed ones for the label; with `--freeze F`, `F` is `D` plus this
  file alone and this file is unchanged at the commit.

`controls.py --self-test` checks its constants against this file (the sentences, the clause, every frozen statement and
definition, every insertion and both blobs); builds a synthetic execution for each of the two rows and requires both to
hold; and applies thirty mutation controls, each of which must fail with its named code. Run at `D` beside this file,
it prints:

```text
controls: the frozen constants match the preregistration beside this file
controls: 2 rows hold as frozen
controls: 30 mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear commits from `F`, each
with one parent:

1. **Stage 1 — the controls, the probe and the module without its verdict.** `controls.py` with its frozen blob; the
   probe with its frozen blob and the frozen workflow edit; the module, the reference implementation without
   `a45_bridge_kernel` and its `#print axioms` line; the import line. The gate is red at `lean-manuscript` until stage 3
   classifies the module.
2. **Stage 2 — the verdict.** `a45_bridge_kernel`, making the module the reference implementation; or, if it cannot be
   obtained, no verdict.
3. **Stage 3 — the surfaces.** The census transform for the label. On `{P}` only: the six manuscript insertions,
   the rebuild of `Main`, `Explainer` and the book by `build.sh`, and the `P0` sentence.
4. **The result note** `result.md`, whose commit is `E`; it carries the probe's summary line from the run at `E`'s
   predecessor and is confirmed by the run at `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40), and so is the probe as a CI job. A stage whose build fails is followed by
a fixing commit, never rewritten, and a fix may touch proofs only.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the probe is the frozen one and runs green in its own shard | `C3`: the probe's blob at stage 1 and at `E`; `Numerical probes / A45 ancilla` green at every execution commit and at `E` with the probe's `OK` line; the aggregate `Numerical probes` job green |
| every frozen statement is kernel-checked within the three axioms | `C8`: the dispatch run at `E`, the `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the manuscripts absorb the result without stale artifacts | `C8`: the release gate at `E` — `lean-manuscript`, `staleness`, `voice`, `claims`, `mirror`, `citation` — all green |
| the frozen surfaces, the note and the paths | `C9`: `controls.py check E --freeze F` prints `controls: check OK` |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen surfaces unchanged** is repaired by later linear commits before `E`,
  and reported in the result note as a departure from the reference implementation.
- **A verdict that cannot be obtained** is reported `{U}`, with the step named; the manuscripts and `ROADMAP.md` are
  not touched.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target or any frozen
  surface: a frozen statement ill-typed or false as frozen; the probe red at `E` with the frozen blob; a frozen
  manuscript insertion that the release gate rejects. The round then halts under the specification's `S12`, with the
  result note naming the failure.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
"""
open(S + 'preregistration.md', 'w').write(doc)
print('written', len(doc))
