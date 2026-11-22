# Lean dependency audit for the A1 retirement (T1′)

**Kind.** Read-only audit. Nothing in the Lean sources, the census registry, the guards or the
retirement plan is changed by this record; every item below is a recommendation for a separate,
separately authorized change.

**Authorization.** Owner, #1169 comment 7075274142: "Lean dependency audit: read-only. Which Lean
statements, hypotheses or docstrings depend on A1 (`[Fintype]` and finite-carrier hypotheses, axiom
reports, the census registry), and whether retiring A1 at T1′ creates new proof obligations or
docstring corrections. Excluded: any Lean implementation, or any build beyond cheap local checks."

**Goal link (§A.47).** Serves the A1 retirement of #1169 (accountable Issue #1477): it decides
whether removing total finiteness as a global posit leaves any kernel statement, hypothesis,
docstring or registry entry that the retirement must change or re-prove.

**Objects audited.**

- Lean and registry: `main` at `53c6601a10419b6b333cc992474272501ab542af`, all of
  `verification/lean/*.lean`, `verification/lean-mathlib/OIBridge/*.lean` and
  `verification/lean-manuscript-census.json`. Every `file:line` below is at this commit.
- Retirement plan: branch `research/a1exit-deletion-20261121` at candidate head
  `607f7a6108318a309f93dd0b8dbd44b4c9310015`, directory
  `verification/audits/foundations/a1exit-deletion-20261121/` (`PREREG.md` through §31,
  `edits.json` with 391 records, `ledger.json`, `guards_check.py`). This head is not on `main`. It
  is the object under review; the findings about the plan hold for that head and no other
  (§A.42 item 8: the object audited, not support for any claim).

## 1. Summary

1. **No new proof obligation.** No Lean declaration takes the predicate `Substratum.A1` (or
   `A1Realized`) as a hypothesis. A1 occurs only as the conclusion of a theorem proved from explicit
   finite hypotheses, as the negated conclusion of a control, or as a definition. No Lean file
   declares an `axiom`; the axiom reports (`#print axioms`, checked by `tools/lean_axiom_check.py`
   against `propext`, `Classical.choice`, `Quot.sound`) carry no finiteness content. Every finiteness
   the kernel uses enters as an instance binder (`[Fintype _]`, `[Finite _]`, `[NeZero L]`,
   `[NeZero q]`) on the declaration that needs it. Retiring A1 as a global posit therefore removes
   nothing a kernel proof consumes.
2. **The plan's Lean edits are docstring-only.** Applying the 36 `lean-docstring` records of
   `edits.json` to the nine affected modules leaves every file identical outside comments, and
   every `old` string occurs exactly once at `main`. No theorem statement changes, so §A.35 asks for
   no supersession entry.
3. **The census passes after the retirement.** `tools/lean_manuscript_census.py` passes at `main`
   and on a copy of `papers/`, `book/`, `tools/`, the Lean trees and the registry with all
   applicable `edits.json` records applied by the plan's own `apply_edits`. Every family whose
   modules encode A1 is `kernel-only` with no manuscript anchor, so no anchor moves.
4. **Docstring corrections the plan does not yet make:** R-1 to R-3 and R-7 below, with R-4 a
   propagation note and R-8 a capitalization nit in plan record D319. R-1 to R-3 are headings or
   scope sentences that read as cardinality-free while the declaration carries finite hypotheses,
   or that state more finiteness than the declaration carries; under global A1 the first kind was
   implicitly finite, and after the retirement it is not. R-7 is a docstring that still states the
   retired posit as a fact about the manuscripts (`A6Instantiation.lean:508`), found by the
   independent review of this record (#1542 comment 7075467292).
5. **Identifier-migration candidates:** the thirteen kernel names and one registry family name of
   §5, matching the plan's §22.4 table. They are listed only; renaming is a §A.48 item 3 migration
   needing prior owner approval (Issue #1482).

## 2. Method

- `grep` over all `.lean` files for `A1` in identifiers and prose, for "total finiteness",
  "finite substratum", "ledger item", "every/any substratum", and for `[Fintype _]` / `[Finite _]`
  binders on configuration, carrier, site and alphabet types; reading of each hit's declaration.
- For each declaration that names `A1`: whether `A1` is a hypothesis, a conclusion or a definition
  (§1 item 1), and which binders carry its finiteness.
- For the theorems the task names as cardinality-free (§3 class (c)): reading of the statement and
  its binders.
- For the plan: extraction of every `edits.json` record whose file is a Lean module or the
  registry; for every manuscript record, whether the paragraph it edits carries a kernel citation
  (10 records do), and whether the new text states more or less than the cited kernel statement;
  in-memory application of the edits and a comment-stripped comparison of each edited Lean file
  with its base; the census run of §1 item 3.
- Classification layers are kept apart: kernel statements are read as stated; the paper proofs the
  retirement text relies on for cardinality-free claims are identified as paper derivations, not
  kernel results.
- Not run: `lake build`, the Mathlib build, `guards_check.py` (which needs `numpy`/`scipy` and
  several minutes) and the CI-run round controls (§A.40; excluded by the authorization).

## 3. Classified inventory

Classes: **(a)** finiteness is a genuine hypothesis of a finite-only theorem — keep, matching the
retirement's "finite as a local hypothesis"; **(b)** finiteness appears only as the global posit A1
(prose), needing a docstring correction or a restated hypothesis; **(c)** a theorem cited as
holding for any cardinality — statement checked; **(d)** an identifier whose name encodes A1 (§5);
**(u)** an unrelated label.

### 3.1 Declarations that name A1

| Site | Declaration | What it is | Class | Plan treatment |
|---|---|---|---|---|
| `SubstratumInterfaceAudit.lean:84` | `def A1 : Prop := Finite 𝒮.Conf` | the finiteness predicate on a `Substratum`; the structure itself (`:59`) has no finiteness field | (d); predicate, not a hypothesis | D277 docstring; name kept (#1482) |
| `SubstratumInterfaceAudit.lean:109` | `a1_of_finite [Finite 𝒮.ι] [Finite 𝒮.V] : 𝒮.A1` | finiteness concluded from finite sites and alphabet | (a), (d) | D278 |
| `SubstratumInterfaceAudit.lean:185` | `waveSubstratum_A1 [NeZero L] [NeZero q]` | the wave instance is finite for a nonzero torus size and a nonzero modulus | (a), (d) | D279; D276 module text, see R-2 |
| `SubstratumInterfaceAudit.lean:786` | `obs_a1` under `[Fintype 𝒮.ι] [Fintype 𝒮.V]` (`:766`) | finiteness of the observer theory's substratum | (a), (d) | D281 |
| `WaveSubstratumUnbounded.lean:70` | `waveZ_not_A1 (hd : 0 < d) [Nontrivial (ZMod q)]` | control: the instance on `ℤ^d` is not finite | (a) control, (d) | D323, D324 |
| `HexLatticeGas.lean:312` | `hexSubstratum_A1` under `[NeZero L]` (`:302`) | the hex gas on a finite torus is finite | (a), (d) | D321, D322; `:94` frozen H-B sentence kept (owner decision 4) |
| `A6Instantiation.lean:276` | `pk3a_A1 [NeZero L] [NeZero q]` | the packaged carrier is finite | (a), (d) | D314, D316 |
| `A6Instantiation.lean:512` | `cx3b_complex_not_A1` | control: the complex carrier is not finite | (a) control, (d) | D317–D320 |
| `ManuscriptAxioms.lean:76` | `A1Realized` | `Fintype.card Core = 8` and level cardinalities: true by the types of `FiniteOperationalTheory (Fin 2)`, independent of the theory | (d); finite by construction, not a posit | D262–D273 |
| `ManuscriptAxioms.lean:90, 94, 98, 107` | `A1A2Realized`, `a1_every_theory`, `substratumTheory_A1`, `substratumTheory_A1A2` | the image, its conjunction with A2's image, and their proofs | (d) | D265–D273 |

No theorem anywhere in `verification/lean-mathlib/` takes `𝒮.A1`, `A1Realized` or `A1A2Realized`
as a hypothesis; outside `ManuscriptAxioms.lean` no file uses the latter two at all.

### 3.2 Finite hypotheses on carriers (class (a), keep)

180 of the 252 Lean files (`verification/lean/*.lean`, `OIBridge/*.lean`, `OIBridge.lean`) match
`\[(Fintype|Finite)\b`, that is, carry `[Fintype _]` or `[Finite _]` binders. They type matrices,
finite sums, probability vectors and `FiniteOperationalTheory` carriers; none is stated as A1.
Those behind the finite-only results Main states were read in full at the signature level:

| Module | Finite binder | Manuscript scope after the retirement |
|---|---|---|
| `CausalReadback.lean:178` (`RootedRealization V H [Fintype H]`), `RecurrenceHorizon.lean:134`, `RootedClassification.lean:24, 135` | finite visible and hidden carriers | Main §2.3 theorems state finite `𝒞_V`, `𝒞_H`; D004 rewrites Main:129 to "the theorem takes the hidden space finite, as on a finite representative" — matches the kernel |
| `CanonicalMeasure.lean:54` (cited by `book/ch01` and FULL, not by Main or SM) | `[Fintype S]` (uniform law, injective ⇒ bijective) | Lemma 3 counting measure "on a finite representative" (D253, D389); Substratum:94 finite-set clause with (REV) otherwise (D374) — matches |
| `PhysicalC4Discharge.lean:576`, `PhysicalC4StorageReadback.lean` | `[Fintype 𝒮.ι] [Fintype 𝒮.V]`, finite `H` | routed readback, finite carriers; no plan edit to that paragraph |
| `SubstratumInterfaceAudit.lean:766`, `FrozenSourcing.lean:84, 277`, `StochasticInterface.lean:111, 182`, `LiftSource.lean:196, 296`, `ExecSource.lean` | `[Fintype 𝒮.ι] [Fintype 𝒮.V]` for `obsTheory 𝒮` | the observer theory is defined only for finite sites and alphabet; Main:598 and GR:257 keep "in its finite model" (D008, D043) — matches; headings see R-3 |
| `Finiteness.lean` | finite boundary modes ⇒ `Finite C_V` | Main Lemma 1, visible finiteness: not A1 and not touched |

### 3.3 Theorems the retirement can cite for any cardinality (class (c))

| Declaration | Statement checked | Verdict |
|---|---|---|
| `ObservableFactorRecurrence.changeEvent_eq_iUnion` (`:48`) | `X`, `V` arbitrary types, no instance | no finiteness at all |
| `ObservableFactorRecurrence.pIndivisible_of_visible_identity_return_nonperm` (`:68`) | `[Fintype V] [DecidableEq V]` on the visible alphabet only; no hidden carrier occurs in the statement; the measurable realization of `Γ` is not constructed (its docstring says so) | no hidden-carrier finiteness; finite visible alphabet kept |
| `WaveUnbounded.waveZ_A2`, `waveZ_A3`, `waveZ_A4Exact`, `waveZ_A4`, `waveZ_A5`, `waveZ_A4Exact_int` (`WaveSubstratumUnbounded.lean:45–65`) | `L = 0`, sites `Fin d → ℤ`; `q` arbitrary (`q = 0` gives alphabet `ℤ`); no instance binder; the upstream `waveSubstratum_A2`–`_A5` hold for every `L`, and the rule `waveF` sums over the `2d` neighbour directions, not over sites | no finiteness |
| `ObservableRigidity` (`:88–392`): `tv_revives_of_nearReturn` (`:88`), `rootedFamily_isRowStochastic` (`:170`), `exists_pIndivisibleWithin_of_nonPermutation`, `rootedFamily_productLaw` | microscopic carrier `S` any measurable space; `[Fintype V]` on the visible alphabet only; the existence theorem additionally assumes a compact-orbit hypothesis | no hidden-carrier finiteness |

None of these names is cited by a manuscript at `main` or in the plan's new text. The retirement's
cardinality-free claims — the near-return step on a measurable hidden carrier (D026, D229), the
measurable-carrier corollary of Main §3.2, and the classical factor "of any cardinality" of
Substratum Theorem 24(iii) (D363–D371) — rest on the paper proofs of Main §2.3, Main §3.2 and
Substratum §4, with no kernel citation. That is their current support layer and the plan does not
present them as kernel-checked. The matrix core of the near-return corollary
(`tv_revives_of_nearReturn`) and a measurable row-stochasticity lemma exist in
`ObservableRigidity`, a kernel-only research module of A1-RIGID-1; citing them from Main would need
the §Whole-framework upstream-independence check first. Recorded as an option (R-6), not an
obligation.

### 3.4 Prose naming A1 as the global posit (class (b))

Every such site at `main` but one is covered by a plan record: `ManuscriptAxioms.lean:4, 8, 17, 21–26, 72,
75, 89, 93, 97` (D262–D273); `SubstratumInterfaceAudit.lean:7, 13, 16, 83, 108, 184, 769, 785`
(D274–D281); `FrozenSourcing.lean:83` (D282); `HexLatticeGas.lean:37, 106, 311` (D283, D321,
D322); `HydroSourceAudit.lean:88` (D284); `RouteB.lean:108` (D285); `SubstratumSource.lean:48`
(D286); `A6Instantiation.lean:43, 74, 274, 498, 499, 509, 564` (D314–D320);
`WaveSubstratumUnbounded.lean:21, 67` (D323, D324). After the edits the only `A1` strings left in
these files are declaration names, the phrase "the finiteness predicate `A1`", and the frozen H-B
sentence at `HexLatticeGas.lean:94`.

The exception is `A6Instantiation.lean:508`, in the docstring of `cx3b_complex_not_A1`: "the
manuscripts' substratum is the finite object of `SM.md:306`". After the retirement the manuscripts
do not posit a finite substratum, so the clause states the retired posit as a fact; and `SM.md:306`
at `main` is the scope remark of SM Theorem 3, not a finiteness statement. No `edits.json` record
touches it (D319 edits the next sentence) and `PREREG.md` does not mention it. The A1-token grep of
§2 missed it because it contains no `A1` token. The same passage (`:506`) calls finiteness "the
first of the interface's axioms", which names the kernel predicate `A1` and is accurate for the
interface. The passage is labelled the round's frozen "bounded reading"; the plan already edits
inside it (D319), so it is treated as active docstring text, unless an owner decision freezes it as
for the H-B sentence. Class (b); recommendation R-7.

### 3.5 Unrelated labels (class (u), no change)

`OIBridge.lean:2` and `Averaging.lean:55` ("ROADMAP §A1", a section of the frozen roadmap);
`OI_Regulator_Symmetry.lean:27` (the same section); `OrbitGeometrySelector.lean:1641`
(`geo4_a1_l5_not_implies_geo`, cell `a1` of act 24) and its registry mention at line 1219;
`QuarterTurn.lean:408` (`chiA1`, the character of the irreducible representation A₁, and
`sum_chiA1_sq` at `:490`);
`OI_Structural_Core.lean:389` (variables `A0 A1 A2`); `ObservableRigidity.lean:8, 16` and registry
line 1725 (the programme label A1-RIGID-1, kept by the plan).

## 4. Cross-check against the retirement edits

**Kernel-citing manuscript paragraphs.** Eleven `edits.json` records were checked: D004, D008,
D009, D043, D224–D228, D253, D389. Nine of them (D008, D009, D043, D224–D228, D253) sit in a
paragraph with a kernel citation; D004 (`Main.md:129`) and D389 (`SM.md:252`) do not, and are scope
checks against the §3.2 modules. Each keeps or adds a finite scope ("finite model", "a finite
substratum", "on a finite representative", "takes the hidden space finite"). For D008, D009 and
D043 the cited kernel statements carry that finiteness as explicit binders (`obsTheory` under
`[Fintype 𝒮.ι] [Fintype 𝒮.V]`, `FiniteRootedRealizable` with a finite `H`). For D224–D228 and D253
the paragraph's kernel citation is `ruleDynamics`, for ledger item (viii) (a finite alphabet over
arbitrary sites), which the edits do not touch. No edited sentence states a kernel result more
strongly or more weakly than its statement.

**Census registry (§A.35).** No supersession entry is needed: no theorem statement changes. No
anchor changes: the families carrying A1 material — "route B: consequence closure", "manuscript
axioms A1-A6", "substratum interface: sourced observer theory", "LEAN-2 (i): wave substratum at
L = 0", rounds H-A and H-B, "A6 instantiation, round 2", "SUBSTATE-1 finite observable-factor
recurrence", "A1-RIGID-1 measured observable recurrence" — are all `kernel-only` with no manuscript
anchor. The plan's note edits D292–D294, D297–D299, D331–D339 cover every A1 string in the notes
other than declaration names, the frozen H-B quotation at line 993 and the labels of §3.5. One note
keeps an unscoped instance claim (R-2).

**Guard coverage.** `guards_check.py` runs, on the simulated tree, the R7 guard
(`edge_rigidity_probe.py`) and `bohr_frequency_probe.py` — the only probes under `verification/lean/`
that read the nine edited modules or the registry — and the census, mirror, citation and
dependency-label checks, with `edits_check.py --pins` scanning the literals of every tracked Python
check. Outside that list, CI runs self-tests that read the live registry:
`verification/infrastructure/ktoken_historical_selftest.py` (it compares the whole KTOKEN family;
the independent review ran it on the simulated tree: PASS), and the
`--self-test`/`exact` modes of the round controls of OI-FINITE-PROTOCOL-1, OI-PAIR-MAXCONE-1,
PRESERVE-INDUCT-1 and KTRANS-SEP-2. None names a family the plan edits, and the plan adds or
reorders no family, so none is expected to be affected; they are exercised by the plan's
exact-tree CI run (§25.2), not by `guards_check.py` (R-5). The CI core probe
`audit_census_probe.py` re-counts the vocabularies of `verification/audit-census.json` over
`papers/*.md` and `book/*.md` and fails on any changed count; it is not a literal pin, so
`--pins` does not see it, and it is not in the reader list. It passes on the simulated
post-retirement tree (§7). The round controls of
PC-1, F2-1, KINF-1/2, EFF-1, K1-BRIDGE-1, K2-GUARD-1, act 45, V3-14 and the intro-corpus unit-5
check name edited modules but compare blobs at their own frozen commits.

## 5. Identifier-migration candidates (list only; §A.48 item 3, Issue #1482)

`Substratum.A1` (`SubstratumInterfaceAudit.lean:84`), `Substratum.a1_of_finite` (`:109`),
`waveSubstratum_A1` (`:185`), `obs_a1` (`:786`), `WaveUnbounded.waveZ_not_A1`
(`WaveSubstratumUnbounded.lean:70`), `HexLatticeGas.hexSubstratum_A1` (`HexLatticeGas.lean:312`),
`A6Instantiation.pk3a_A1` (`A6Instantiation.lean:276`), `A6Instantiation.cx3b_complex_not_A1`
(`:512`), `ManuscriptAxioms.A1Realized` (`ManuscriptAxioms.lean:76`), `A1A2Realized` (`:90`),
`a1_every_theory` (`:94`), `substratumTheory_A1` (`:98`), `substratumTheory_A1A2` (`:107`), and the
registry family name "manuscript axioms A1-A6" (`lean-manuscript-census.json:488`). The module and
namespace name `ManuscriptAxioms` contains no `A1` but names the substratum conditions "axioms";
whether that is in scope is the owner's question. Each name denotes a true finite-only statement or
a control, so a rename is a clarity change, not a correction. Each is referenced by guards (R7,
pins P15 and the declaration-name pins of `guards_check.py`) and by frozen records, which a
migration leaves unchanged and indexes.

## 6. Recommendations (for a separate, authorized change)

| ID | Site | Class | Finding | Recommendation |
|---|---|---|---|---|
| R-1 | `SubstratumInterfaceAudit.lean:175–176` (`waveSubstratum` docstring) | (b), docstring | "the manuscripts' rule on a finite cubic torus with alphabet `ℤ/qℤ`": the definition holds for every `L` and `q`; at `L = 0` it is the instance on `ℤ^d` that `WaveSubstratumUnbounded` uses and `waveZ_not_A1` proves infinite. The docstring states a finiteness the declaration does not carry; no plan record touches it | Say "on the cubic torus `(ℤ/Lℤ)^d`, which at `L = 0` is `ℤ^d` (`WaveSubstratumUnbounded`), with alphabet `ℤ/qℤ`" |
| R-2 | Plan record D276 (`SubstratumInterfaceAudit.lean:16`) and D332 (registry line 525) | (b), scope | D276 reads "satisfies the finiteness predicate `A1` on a finite torus and A2–A5 as stated"; `waveSubstratum_A1` needs `[NeZero L] [NeZero q]`, and at a finite torus with `q = 0` the configuration space is infinite. D332's "an instance satisfying the finiteness predicate `A1` and A2-A5" carries no scope. Both state more than the kernel | Amend D276 to "for a finite torus and a finite alphabet" (the wording of `:184`), and D332 likewise, before execution |
| R-3 | `FrozenSourcing.lean:82` ("OBSERVER THEORY OF ANY SUBSTRATUM"); `StochasticInterface.lean:113` ("FOR EVERY SUBSTRATUM WITH A LINEAR RULE …") and `:173` ("For every substratum whose rule is linear"); `LiftSource.lean:36` and `ExecSource.lean:14` ("the observer theory of every substratum") | (b), docstring | Each declaration carries `[Fintype 𝒮.ι] [Fintype 𝒮.V]`; the heading reads as holding for a substratum of any cardinality. Under global A1 every substratum was finite; after the retirement the heading is stronger than the statement. D282 rewrites only the tail of the first | Insert "finite" ("any finite substratum", "every finite substratum …"), or state the binders, at the five sites |
| R-4 | `ManuscriptAxioms.lean:8–9` after D263 | (b), wording | D263 makes the module say the manuscripts' conditions are "finiteness of the configuration space (the scope of the reconstruction theorem) and A2–A6". Correct against Substratum Theorem 23's finite scope (PREREG H-7); the parenthesis is the only place in Lean that ties the reconstruction theorem's scope to finiteness, so it must follow any later change to that scope | No change now; add `ManuscriptAxioms.lean` to the propagation set of any future change to Theorem 23's scope |
| R-5 | `guards_check.py` reader list | coverage | The CI-run self-tests that read the live registry, and `audit_census_probe.py`, which counts manuscript vocabularies (§4), are outside the local list | Add `audit_census_probe.py` to the reader list (it runs in under a second); add the registry-reading self-tests or record that the exact-tree CI run alone covers them |
| R-6 | Main §2.3 Corollary (near-return); Main §3.2 Corollary (measurable hidden carrier); Substratum Theorem 24(iii) | layer | The retirement's cardinality-free statements rest on paper proofs. Kernel material for parts of them exists (`tv_revives_of_nearReturn`, `rootedFamily_isRowStochastic`, `rootedFamily_productLaw` in `ObservableRigidity`) | Optional, separate formalization Issue; before Main cites `ObservableRigidity`, check its proof dependencies for downstream content |
| R-7 | `A6Instantiation.lean:508` (docstring of `cx3b_complex_not_A1`) | (b), docstring | "the manuscripts' substratum is the finite object of `SM.md:306`" states the retired posit as a fact, and the pointer does not resolve to a finiteness statement at `main` (§3.4). No plan record touches it | Add a plan record rewriting the clause to a scoped statement, for example "the manuscripts' substratum on a finite representative", with a pointer that resolves; or, if the passage is to stay frozen, record the owner decision that freezes it, as for `HexLatticeGas.lean:94` |
| R-8 | Plan record D319 (`A6Instantiation.lean:509`) | nit, plan | The new text starts a sentence in lower case: "… Theorem 5 is conducted. **the finiteness predicate `A1` is not weakened**"; the other records that insert the phrase at a sentence start capitalize it | New text "**The finiteness predicate `A1` is not weakened**" |

**New proof obligations:** none (§1 item 1). **Census registry changes:** the plan's note edits,
plus R-2's D332 scope; no supersession entry, no anchor change. **Identifier migrations:** §5,
pending owner approval under §A.48 item 3.

**Disposition in the plan.** The owner approved the §31 corrections at #1169 comment 7075564570
(`amaybaum`, 2026-11-22T06:50:57Z): "R2, finite alphabet | Required fix. Keep the finite-alphabet
condition, including `[NeZero q]`, wherever the revised claims depend on it." and "R3, Lean
docstrings | Required fix. Scope all four ensemble claims explicitly to the finite cases actually
supported." That record numbers its findings as the §31 delta review does; its R2 and R3 cover this
audit's R-2 and R-3. Its "four ensemble claims" differs from the five headings of this audit's R-3;
reconciling the two is left to the §31 delta review. The owner then directed R-7 and R-8 into the
§31 corrections at #1169 comment 7075903147 (`amaybaum`, 2026-11-22T07:25:13Z): "R-7 and R-8 enter
the A1 plan's §31 corrections (#1477), as recommended by the Lean audit (#1542)", R-7 as required
and R-8 as approved. R-7 was found by the independent review of this record (#1542 comment
7075467292). None of R-2, R-3, R-7 or R-8 is present at the audited plan head `607f7a61`.

## 7. Checks run

| Check | Tree | Result |
|---|---|---|
| `python3 -I -B tools/lean_manuscript_census.py` | `main` at `53c6601a` | OK, 25 current families |
| the same, `--root` on a copy with the applicable `edits.json` records applied by `edits_check.apply_edits` (36 files changed; the 19 records whose files were not copied are in `verification/README.md`, three programme charters and READMEs, and AGENTS.md, none of which the census reads) | simulated post-retirement tree | OK, 25 current families |
| `python3 -I -B audit_census_probe.py` | `main`, and the simulated tree with `verification/audit-census.json` | ALL CHECKS PASS on both |
| every `old` of the Lean and registry records occurs exactly once at `main` | `main` | 0 failures |
| comment-stripped comparison of each edited Lean module with its base | simulated tree | 9 modules changed, 9 identical outside comments |
| `grep` for `axiom` declarations, `sorry`, and `.A1` / `A1Realized` in hypothesis position | `main` | none |

No Lean or Mathlib build was run; the kernel statements are read from source, not re-checked.

## 8. Not claimed

This audit does not certify the plan, its other 355 records, or the manuscript edits outside the
eleven records of §4's kernel-paragraph check; it does not re-check any kernel proof; and it changes no claim's
status.
