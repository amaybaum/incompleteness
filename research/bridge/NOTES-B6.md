# NOTES-B6 — Theorem B1.1 as a Lean design module

Node B6 of `research/bridge` (round 2). Base L = `9f9f8257`. The module is
`verification/lean-mathlib/OIBridge/BridgeLemma.lean` on the disposable branch `dev-bridge/b11-lemma`; its verbatim
copy is `research/bridge/lean/BridgeLemma.lean`. It is a design module, [D] at best: CONJECTURE until a governed round
lands it. The CI record is in §4.

**Success criterion (round-2 directive).** Formalize the H→P bridge lemma at the `W 3` table level. The hypotheses
are RESPECT, availability in context (A), product behaviour (P) and local tomography; the conclusion is (b_H) for the
token operation. If the full lemma is out of reach, formalize the largest exact sub-lemma and record the gap.

## 1. What the module states

| declaration | content |
|---|---|
| `actCLin`, `actTLin` | the kernel's `actC N`, `actT N` as linear maps of `W d` |
| `actC_prodState` | `actC N (prodState x y) = prodState (N x) y`; the target law is K2Guard's `actT_prodState` |
| `lawSub`, `intertwine_of_respect` | **the linear-algebra core**. For linear `R : V → W 3`, `P : V → V`, `T : W 3 → W 3`, a submodule `D` and a spanning `G ⊆ W 3`: if `R ν = 0 → R(Pν) = 0` on `D`, and every `g ∈ G` is realized in `D` with `R(Pμ) = T g`, then `R ∘ P = T ∘ R` on `D` |
| `prodSetOf`, `tens_mem_span_prodSetOf`, `span_prodSetOf` | **local tomography of the carrier, proved.** If the homogenized points of `X` span `HVec 3`, the products over `X` span `W 3` |
| `span_hom_of_frame`, `span_productSet` | the points `0, e_x, e_y, e_z` suffice; the products of the ball span `W 3` |
| `hpush`, `hiddenCone`, `hiddenCone_mapsTo` | pushforward along a hidden bijection; the hidden composite cone (rays through `R 𝒫`); invariance from intertwining plus (A) |
| `bH_respect`, `bH_respect_target`, `bH_perm` | **Theorem B1.1, readout-kernel form.** RESPECT on all hidden vectors, (P) on a spanning set of products, (A): `R ∘ P = actC O ∘ R` (resp. `actT`), and the hidden cone is invariant. `bH_perm` is the form for a hidden bijection |
| `ray_add`, `diffSub`, `mem_diffSub`, `respect_diff` | differences of rays through a convex `𝒫` form a submodule; RESPECT on `𝒫` with normalized readout gives the kernel form on it |
| `bH_convex` | **Theorem B1.1 exactly as stated in NOTES-B1 §2**: convex `𝒫`, normalized readout (`R μ 0 0 = 1`, i.e. joint states), RESPECT on `𝒫`, H1 on the ball, (P), (A) |
| `tok`, `tokPerm`, `cyc_tok`, `ctlR`, `ctlPerm`, `ctl_intertwine`, `ctlR_single`, `hidSimplex`, `hpush_hidSimplex` | the control model: product registers `Fin 4 × Fin 4`, token points `0, e_x, e_y, e_z`, local readout, hidden bijection `tokPerm × id` realizing the linear part `cycEquiv` of the kernel's `cyc3` |
| `ctl_bH` | **positive control.** The control model satisfies every hypothesis of `bH_perm` with `𝒫` the probability simplex. The hypotheses are jointly satisfiable and the theorem is not vacuous |
| `ctl_counter` | **countercontrol.** With `𝒫` a point mass, RESPECT and (P) hold and (A) fails, and `actC cycEquiv` moves the hidden cone. (A) is not redundant |

**Mapping to NOTES-B1 §2.**
- (W) is `hW`: kernel form in `bH_respect`, on `𝒫` in `bH_convex`.
- (A) is `hA`.
- (P) is `hP`.
- H1 is `hH1` (in the kernel form it is folded into `hP`'s existence clause).
- Local tomography is not a hypothesis but a theorem of the carrier (`span_prodSetOf`). The carrier `W 3` encodes it
  (CompositeDimension.lean:96); the module proves the spanning statement used in step 3 of the written proof.
- Steps 1–4 of the written proof are, respectively: `lawSub`'s well-definedness (by RESPECT); linearity (the
  submodule); agreement on products with spanning (`intertwine_of_respect`); and (A) (`hiddenCone_mapsTo`).

## 2. What is not formalized, and why

- **The convex-set form is complete.** No gap remains between `bH_convex` and the written B1.1. The written proof's
  affine-extension step is replaced by an exact submodule argument (`diffSub`): normalization makes the positive and
  negative weights equal.
- **L-REG's computation** (B1 §2: under product registers, RESPECT of `π` gives (W) and (P)) appears only as the
  control instance `ctl_intertwine`, not as a general lemma.
- **The membership facts at the pair level** (`phiW` in every candidate cone, B1-0) are not touched.
- **Nothing sources (A)**, which is the point of B1.1: it relocates the local-action clause to the hidden premise (A).

## 3. Reading

- **B1.1 [D].** The first H→P declaration about the pair carrier, as a design module (run 38092042844 green on
  Build and `lean-axioms`). It discharges no
  obligation: (b_H) for `O` holds exactly when (A) holds for `O`'s hidden realization (given RESPECT and (P)).
- **The controls make the hypothesis set honest.**
  - Satisfiable: `ctl_bH`, in an L-REG model. Such models are Bell-local by B1.2, consistent with local readout.
  - (A) load-bearing: `ctl_counter`.
- **Gem classification.** ELABORATING. The round-1 [W] proof is now a kernel-checkable design statement. The convex
  form needed no further hypothesis beyond normalization, which B1 §1 already had (`R(𝒫)` consists of joint states).

## 4. CI record

Dispatches: `workflow_dispatch` of `verify.yml` on `dev-bridge/b11-lemma`, 2 of 3 used for this module. As noted in
the round-1 CI record, the gate's `claims`, `duplicate` and `lean-manuscript` steps are red by construction on
research branches; the meaningful signals are the Build step, the module's `#print axioms` lines and the
`lean-axioms` gate step.

| run | dev commit | Build | module `#print axioms` | `lean-axioms` | notes |
|---|---|---|---|---|---|
| 38090784384 | 00d43da4 | **failure** (22:28:43–22:30:37Z) | 7 built on [propext, Classical.choice, Quot.sound]: `actCLin`, `actTLin`, `intertwine_of_respect`, `span_prodSetOf`, `span_hom_of_frame`, `span_productSet`, `ctl_intertwine` | not run (gate skipped) | `𝒫` is reserved Mathlib notation (`Set.powerset`), so nine declarations failed to parse and their dependents followed; remaining probe jobs cancelled after the bridge job completed |
| 38092042844 (job 114330283929) | f1c5f0fb | **success**, 22:59:12–23:01:10Z ("Build completed successfully (3644 jobs)"; `Built OIBridge.BridgeLemma`, warnings only) | all 14 `#print axioms` lines on [propext, Classical.choice, Quot.sound]: `actCLin`, `actTLin`, `intertwine_of_respect`, `span_prodSetOf`, `span_hom_of_frame`, `span_productSet`, `bH_respect`, `bH_respect_target`, `bH_perm`, `respect_diff`, `bH_convex`, `ctl_intertwine`, `ctl_bH`, `ctl_counter` | **PASS** ("OK (5874 named result(s) reported, no sorr…") | gate red only on `claims`, `duplicate`, `lean-manuscript` (1 problem: no census disposition for the design module), by construction; `𝒫` renamed `Pd`; unexecuted fallbacks removed; `mem_diffSub`; explicit countercontrol evaluation |
