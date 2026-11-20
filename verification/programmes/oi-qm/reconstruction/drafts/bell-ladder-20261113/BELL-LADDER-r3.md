# Bell debugging ladder (#868): where Bell-local behaviour is first forced

**WIP / UNVERIFIED. Paper-only writer draft r3, after the independent non-author review of r1 (ACCEPT WITH
CHANGES; required changes C1–C14, dispositions in `RESPONSE-r1.md`) and its focused confirmation of r2 (ACCEPT WITH
CHANGES; R1–R3 and N1–N4, dispositions in `RESPONSE-r2.md`), pending ChatGPT review at the exact head.
Authorizes nothing; adopts no premise; edits no manuscript or frozen record.**

- **Accountable home:** #868. Coordination #1169.
- **Authority.** Owner decision recorded at #868 c.6854708572 (account `amaybaum`, 2026-11-13T13:44:26Z):
  "Full ladder as relayed". The record states: "This is a paper-only unit under #868. The writer is the
  coordinating Claude Code session. The unit gets an independent non-author review, then ChatGPT review at the
  exact head." It lists as not authorized: "computation on OI rules, new premises, adoption of a state-dependent
  graph or a new rule class, changes to manuscripts or frozen records, merges, and priority changes." It also states:
  "Escape is not quantum mechanics."
- **What was done.** Source reading and hand derivations only. No script, no probe, no Lean build, no computation on
  any OI rule. The toy maps of §2 are generic finite bijections checked by hand; none is an OI rule.
- **Pins.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153` (2026-11-13 10:53 +0200). `Main:n` is line n of
  `papers/Main.md` at that commit (blob `0db17597…`). Inputs off `main`, read at their stated heads:

  | Label | Record | Head | Blob |
  |---|---|---|---|
  | BS | Bell-scope r2, `…/drafts/bell-scope-868-20261111/BELL-SCOPE-UNIT1.md` (PR #1231) | `e1534b08` | `5814e479…` |
  | SB | SUBSTATE-BRIDGE-1 r2, `…/drafts/substate-bridge-1-20261111/SUBSTATE-BRIDGE-UNIT1.md` (PR #1232) | `86a413c8` | `9ff0f077…` |
  | QH | Q-868-H unit 1 r3, `…/drafts/q868h-20261109/Q868H-UNIT1.md` (PR #1269) | `ffc9cda4` | `ebf5215b…` |
  | RC | REC-1 r7, `…/drafts/rec-1-20261113/REC-1-r7.md` (PR #1268) | `9f7d2612` | `f1ffac0e…` |

  `…` is `verification/programmes/oi-qm/reconstruction`. Records on `main` used: OA1 =
  `…/oa-1-20261112/OA-1-REPORT-r5.md` (`5a16b213…`), OA2 = `…/oa-2-20261112/OA-2-REPORT-r4.md` (`8f8ddf73…`),
  T1 = `…/drafts/tune-1-20261111/TUNE-1-STEP2-SESSION3.md` (`a9cbc675…`), PPS =
  `…/oi-qm-ext-1/prepared-pair-source.md`; Lean `verification/lean-mathlib/OIBridge/Equivalence.lean`
  (`9513665b…`).
- **BS and SB are pinned at `cac5d264`, which is stale against `main`.** Since PR #1233, Main:362 defines
  `G_φ^K` and states that a linear update has the same graph on every state class; ledger (x) is scoped to
  `G_φ^ref`; and ledger (xiv) is measurement independence (Main:724). BS's findings F1 and F2 and its O1/O3 framing
  are read against those lines; where BS or SB differ from `main`, `main` is used.

**Evidence tags.** **K** kernel theorem on `main`; **P** paper proof in a manuscript on `main`; **W** research
record on `main`, model-reviewed (not verification, §A.46 item 7); **D** draft off `main`; **A** hand derivation in
this file, unreviewed.

***

## 0. Answer

**Decisive comparison.** For a general fixed deterministic dynamics, the CHSH obstruction does **not** arise when
a fixed local coupling graph is required. Separation in the actual coupling graph (stage 3) gives pointwise
parameter independence and nothing more: a measurement-dependent initial law on a separated, generator-isolated
carrier realizes the PR box with complete-history no-signalling (§2, toy `φ_0` with `μ_MD`). The obstruction arises
when measurement independence for the response-complete pre-setting variable is added (stage 5) to that
separation. Generator isolation (stage 4) is not needed: BS Theorem N′ replaces it by the stronger MI* for
`λ* = (Ω, ρ_A, ρ_B)`.

**Controlling condition, general class (stage 5).** Bell-local behaviour, for the whole finite menu and complete
local histories, is forced by the conjunction

> (D) one deterministic map; (F) `S = ∏_{i∈V} S_i` finite (ledger (ii), (viii)); (Gen) settings are functions of
> the content of disjoint generator regions at the setting slice; (Rec) complete local record windows; (Sep) no directed `G_φ` path
> from either generator region to the other wing's record region within the record window (BS states (Sep) with the
> symmetrized distance, which is sufficient; the directed form is SB L3); (MI\*) the
> response-complete pre-setting variable is independent of the setting pair (or (GI) with MI for Ω); a finite menu
> with every pair jointly admissible; every-run outputs with failures mapped by a fixed local rule; no
> postselection.

Source: BS Theorem N/N′ [D, on Main's cone lemma, P]; Main's exogenous theorem (Main:364–389) [P]. The two
controls of §3 isolate the two levers: with the initial law and observer access held fixed, the coupling condition
alone switches CHSH from 2 to 4 (NS kept); with the map and access held fixed, the initial law alone switches it
from 0 to 4 (NS kept).
In the toy of §2, observer-access changes alone (generator residues, enlarged record regions) produce either no
change or signalling; no general access-only theorem is claimed (§3).

**Ledger rule class (vii) (§4, Proposition AL [A]).** Within the affine update class of ledger (vii), with a run
law uniform on a coset (the counting measure conditioned on values of affine functionals) and settings given by
cell values, complete-history no-signalling over fixed record regions alone forces a Bell-local record law, with no
separation, generator isolation or measurement-independence hypothesis; a failure of no-signalling then makes two
remote settings perfectly distinguishable from one wing's complete history at a fixed own setting. In that class the coupling graph does not control Bell locality, and route C of SB (within-cone
propagation in the window between graph cone and wave cone) yields either signalling or no Bell violation.

**For OI under the ledger (conditional).** Under the full ledger (i)–(xiv) with coset run laws and cell-valued
settings, every every-run protocol with complete-history no-signalling over fixed record regions is Bell-local
(Proposition AL [A]; for graph-separated wings also Theorem N [D] with (GI) and (xiv), or Theorem N′ if (xiv) is
read as MI\*). A Bell violation with complete-history no-signalling over fixed record regions then needs one of: an update outside (vii) (Main:414 already places the adopted preparation-indexed branch there), a run
law that is not coset-uniform, settings that are not cell values, or postselection. Each is open or excluded; none
is adopted here. Quantum selection (stage 7) remains undetermined.

***

## 1. The ladder

The same carrier and the same family of maps and laws (§2) are restricted stage by stage. "Not forced
(designed witness)" means a member of the stage's admissible class with complete local records, every-run outputs
and complete-history no-signalling checked by hand. It is a designed map, not the ledger rule, so it is not an
escape demonstrated in the authorization's sense (a native construction). For OI's native rule the stage is
undetermined unless stated.

| Stage | Structure added | Classification | Proof / citation (path:line @ commit) | Assumptions carried |
|---|---|---|---|---|
| 0 | Finite-horizon equivalence `S ⇔ D ⇔ Q_fb`, each direction separately | NOT FORCED (designed witness; law level; the PR law is no-signalling by definition) | S⇒D: `S_imp_D`, `Equivalence.lean:422` [K]; D⇒Q_fb: `D_imp_Qfb`, `:294` [K]; Q_fb⇒S: `Qfb_imp_S`, `:245` [K]; assembled `finite_horizon_equivalence`, `:462` [K], each converse a composite of the three (`:466–468`); Main:546–552, :97 (pointers) [P]. PR realizable: Main:360, :427 [P]; response-table form with prior independent of the visible initial state: Main:518 [P, not formalized] | finite visible alphabet, finite horizon; a joint law over (settings, outputs) is a trajectory law. No spatial structure, no NS notion beyond the law |
| 1 | One fixed deterministic map for all four settings | NOT FORCED (designed witness) | One fixed realization serves every action sequence: Main:480–482 [P]; one fixed `φ_×` with settings as initial content, PR with complete-history NS (§2) [A] | finite menu (Main:486's no-uniform-realization applies to the continuum instrument space, not to a finite menu) |
| 2 | Lattice positions and site factorization | NOT FORCED (designed witness) | `φ_×` is site-factorized; `G_φ` contains the edge `g_A → r_B` (§2) [A]; Main:360 "globally coupled setting-dependent hidden dynamics" [P] | (viii) without (x)/(vii): factorization does not bound `G_φ` |
| 3 | Actual coupling graph: (Sep) required in `G_φ` | NOT FORCED (designed witness, via measurement dependence) | Cone lemma: Main:362 [P] gives pointwise parameter independence; directed form SB L3 (SB:167–171) [D]. `φ_0` with `μ_MD`: separated, PR, complete-history NS (§2) [A] | (Sep) in the actual `G_φ`, not in a reference graph. Under (vii), `G_φ^K = G_φ` for every K (Main:362) and `G_φ` is simple-cubic with (x) (Main:724) |
| 4 | Observer preparation and access: (Gen), (Rec), (GI) | NOT FORCED (designed witness, via measurement dependence) | `φ_0` with `μ_MD` satisfies (Gen), (Rec), (GI) (§2) [A]. Whether native embedded observers generate settings with the required independence is not derived: settings are configuration content (Main:42; OA1:111–112 [W]); QH's settings enter through the supplied controller P3 (QH:213–214) [D] | (Gen), (Rec), (GI) are protocol properties (BS:156) |
| 5 | Measurement independence for the response-complete variable | **OBSTRUCTION** | BS Theorem N (BS:159–178), N′ (BS:185–196) [D on Main:362, P]; exogenous form Main:364–389 [P]; ledger (xiv) (Main:724) posits MI for the response-relevant variable; CHSH ≤ 2 and `ε ≥ (√2−1)/4` to the Tsirelson box (BS:317–330) [D] | the conjunction of §0; MI\* (or (GI)+MI); every-run; no postselection |
| 6 | Complete operational statistics: NS, failures, composition | **OBSTRUCTION** (inherited; extended in class (vii)) | Bell-local ⇒ NS (standard). ⊥-rule and full-history contraction BS:345–355 [D]; composition per run with fresh generators BS:292–294 [D]. Class (vii): Proposition AL (§4) [A] removes (Sep), (GI), (MI) given coset law, cell-valued settings and complete fixed-region NS | for the branch with stage 3 relaxed and each law common across settings (MI kept): NS for a full-span preparation family forces pointwise locality (PPS:134–145) [W]; `φ_×` signals under reuse of its pad and under a deterministic pad (§2) |
| 7 | Quantum selection (why quantum, not PR) | UNDETERMINED | Under stages 0–6 quantum Bell tables are unreachable (stage 5). In the relaxed class PR (CHSH 4) is reachable (Main:360) and no selector is supplied (SB N4, SB:190) [D]. The native encoded U′ composite reaches the non-quantum table SWAP/2 (QH:68–97) [D], which is Bell-local over Pauli-axis product tests [A] | escape is not quantum mechanics |

### Directions of `S ⇔ D ⇔ Q_fb` and what each carries into the ladder (§A.34)

- **S ⇒ D** (`S_imp_D`). Every finite trajectory law, PR and Tsirelson tables encoded as `x_0 = (x, y)`,
  `x_1 = (x, y, a, b)` included, is the visible marginal of a finite bijection. The Lean class (D) allows an initial
  law that correlates hidden and visible coordinates (`Equivalence.lean:150–156`); the realization records the whole
  trajectory in the hidden register, so in Bell terms it is measurement-dependent. A realization with a hidden prior
  independent of the visible initial state is the response-table construction, Main:516–518 [P], not formalized.
- **D ⇒ Q_fb** (`D_imp_Qfb`). The law of any toy of §2, PR included, has a fixed-basis unitary representation.
  Membership in `Q_fb` therefore carries no local-subsystem structure (Main:360).
- **Q_fb ⇒ S** (`Qfb_imp_S`). A fixed-basis Born record is a stochastic law; it carries no Bell constraint.

None of the three directions carries spatial structure, generator regions or a measure condition. Stage 0 cannot
obstruct, in either direction.

***

## 2. One carrier, the maps and laws it is restricted through [A]

Sites (one bit each unless stated): `g_A`, `g_B` (generators; setting = content, so (GI) holds); `λ_A = (λ_A0,
λ_A1)` in wing A, `λ_B = (λ_B0, λ_B1)` in wing B (two bits each); records `r_A`, `r_B`. One update; record windows
`R_A = {g_A, λ_A, r_A}`, `R_B = {g_B, λ_B, r_B}` over the tick (each wing may read all of its own wing's content);
outputs `a = r_A`, `b = r_B` after the tick. Every map below XORs into a record site a function of sites it does not
write, so it is an involution, hence a bijection.

| Map | Update | Directed edges into records |
|---|---|---|
| `φ_0` | `r_A ⊕= λ_A[g_A]`, `r_B ⊕= λ_B[g_B]` | `g_A, λ_A → r_A`; `g_B, λ_B → r_B` |
| `φ_0′` | `φ_0`, and `r_B ⊕= λ_A0` | adds `λ_A0 → r_B` (shared cause; no setting writes `λ_A0`) |
| `φ_×` | `φ_0′`, and `r_B ⊕= g_A ∧ g_B` | adds `g_A → r_B` |
| `ψ_0` (affine) | `r_A ⊕= λ_A0`, `r_B ⊕= λ_A0` | `λ_A0 → r_A, r_B` |
| `ψ_×` (affine) | `ψ_0`, and `r_B ⊕= g_A` | adds `g_A → r_B` |

| Law | Content |
|---|---|
| `μ_0` | `x, y, ρ` independent uniform; `λ_A = (ρ, ρ)`; `λ_B = (0, 0)`; `r_A = r_B = 0`. Uniform on a coset; generators independent of every other site, so MI\* holds |
| `μ_MD` | `x, y` independent uniform; given `(x, y)`: `ρ` uniform, `λ_A[x] = ρ`, `λ_A[1−x] = 0`, `λ_B[y] = ρ ⊕ xy`, `λ_B[1−y] = 0`, `r = 0`. MI fails |

Hand checks (every entry follows by substitution):

1. **`φ_× , μ_0`** (stages 1–2). `a = ρ`, `b = ρ ⊕ xy`: the PR box, CHSH 4. A's complete history `(x, (ρ, ρ), ρ)`:
   law independent of `y`. B's complete history `(y, (0, 0), ρ ⊕ xy)`: `ρ` is never in B's wing, so `r_B` is uniform
   for every `(x, y)`; law independent of `x`. Complete-history NS holds for this law. It fails for a deterministic
   pad (`ρ = 0` gives `b = xy`) and under reuse of `ρ` in a second run (B's two records differ by `x_1y_1 ⊕ x_2y_2`):
   the witness needs a restricted preparation family and single-use pads, as PPS:134–145 [W] and SB N3 require.
2. **`φ_0 , μ_MD`** (stages 3–4). (Sep) holds: no directed path from `g_B` to `R_A` or from `g_A` to `R_B`. (GI)
   holds. `a = ρ`, `b = ρ ⊕ xy`: PR. A's complete history `(x, λ_A, ρ)` has `λ_A[x] = ρ` uniform and `λ_A[1−x] = 0`:
   independent of `y`; symmetrically for B. Complete-history NS holds; MI fails (`I_ont` far above the
   `0.0309`-bit floor of Main:416–423).
3. **`φ_0 , μ_0`** (stage 5). `a = ρ`, `b = 0`; Bell-local (Theorem N′ hypotheses all hold).
4. **`φ_0′ , μ_0`**. `a = b = ρ`: CHSH 2, Bell-local. The edge `λ_A0 → r_B` leaves both forms of (Sep) intact at the
   one-tick window (symmetrized `d(g_A, R_B) = 3`, `d(g_B, R_A) = 2`); `λ_A0` is a common cause (SB L3).
5. **`ψ_× , μ_0`** (class (vii)). `a = ρ`, `b = ρ ⊕ x`: B's record depends pointwise on the remote setting, yet
   `a ⊕ b = x` and the law is Bell-local (with `λ′ = ρ ⊕ x`, uniform and independent of the settings:
   `a = λ′ ⊕ x`, `b = λ′`; §4).
   `|CHSH| ≤ 2` for every pair of local extractors, by Proposition AL.

`μ_MD` is not coset-uniform and `φ_0`, `φ_×` are not affine, so none of checks 1–2 lies in Proposition AL's class.

***

## 3. Controls at the decisive boundary

Each row changes one condition; everything else, including the initial law unless the row says otherwise, is held.

| Lever | Held fixed | Changed | Result | Reading |
|---|---|---|---|---|
| Coupling, general class | `μ_0` (MI\*), access, extractors | `φ_0′ → φ_×`: one directed edge `g_A → r_B` | CHSH 2 → 4; complete-history NS holds for `μ_0` | the coupling condition controls, given MI |
| Coupling, class (vii) | `μ_0`, access, extractors | `ψ_0 → ψ_×`: one additive edge `g_A → r_B` | CHSH 2 → 2; pointwise parameter dependence present, law Bell-local | in the affine coset class the coupling condition does not control (§4) |
| Access: generator residue | `φ_0′`, `μ_0` | add a residue cell `ρ′_A` to `G_A`, uniform and independent, read by A's extractor | no change: MI\* holds, Theorem N′ applies | (GI) does not control |
| Access: record region to remote generator | `φ_0′`, `μ_0` | `R_A ∋ g_B`; A outputs `r_A ⊕ (x ∧ y)` | CHSH 4 with A's history depending on `y` | signalling, not an admissible escape |
| Access: record region to remote record | `φ_0′`, `μ_0` | `R_A ∋ r_B` (`= ρ`) | no change | (Sep) fails in `G_φ` (edge `g_B → r_B` through `λ_B[g_B]`); the dependence is null on the support of `μ_0` (`λ_B = 0`), and `r_B = ρ` is a common cause |
| Initial law (third lever; the initial law changes) | `φ_0`, access, extractors | `μ_0 → μ_MD` | CHSH 0 → 4; complete-history NS holds | measurement independence controls, given (Sep) |

**Reading of the controls.** In the general class, two hypotheses each switch the obstruction off by themselves:
(Sep) in the actual `G_φ` and MI\*. Observer access alone does not: within (Sep) every access pattern is covered by
Theorem N′, and an access pattern that breaks (Sep) in the toy either changes nothing or signals. That last
statement is shown for the toy only; a general access-only theorem is not proved here. Stage 3 alone is not
sufficient (control 6); stage 5 alone is not sufficient (control 1); their conjunction is (Theorem N′).

***

## 4. Proposition AL: affine dynamics, coset law, no-signalling ⇒ Bell-local [A]

*Hypotheses.*
- (AL1) `S = ∏_{i∈V} S_i` with each `S_i` a finite abelian group, and `φ` affine (ledger (ii), (vii), (viii); the
  second-order form (xiii) is affine on phase space). Bijectivity is not used.
- (AL2) The law of `x_{t_s}` is uniform on a coset `C = c + H` of a subgroup `H ≤ S`. This is the counting measure
  conditioned on the values of affine functionals at earlier ticks, transported by the affine bijection; it covers
  the MP-0a family (designated cells at known values, uniform elsewhere; OA1:556–558 [W], RC's `D_0`) and μ-G
  (OA1:103–105 [W]).
- (AL3) The settings are the values of affine maps `P_A`, `P_B` of `x_{t_s}` (generator cell values); a finite
  menu with every pair of positive probability.
- (AL4) The complete histories `h_A = (x_t|_{R_A^t})_{t_s ≤ t ≤ T_A}`, `h_B` likewise, for any fixed regions
  `R_A^t`, `R_B^t`, independent of the state and the settings (overlap and in-cone regions allowed), complete in the
  sense of BS (Rec): every record the wing holds or can obtain in the window; outputs are arbitrary local functions of `h_A`, `h_B` (own setting, failures and a
  fixed ⊥-rule included).
- (NS) For every `x`, the law of `h_A` given `(x, y)` does not depend on `y`; for every `y`, the law of `h_B` given
  `(x, y)` does not depend on `x`.

No separation, generator isolation or measurement-independence hypothesis is made.

*Conclusion.* There are a subgroup `M` and maps with `(h_A, h_B) = (F_A(λ, x), F_B(λ, y))` in joint law, for every
menu pair, with `λ` uniform on `M` and independent of the settings. So every local function of the complete
histories is Bell-local for the whole menu, `|CHSH| ≤ 2`, and `ε ≥ (√2−1)/4` to the Tsirelson box (BS §4.1 bound,
which needs only Bell locality). If (NS) fails for wing A, there are `x`, `y`, `y′` for which the laws of `h_A` given `(x, y)`
and `(x, y′)` are uniform on two distinct cosets of `π_A M`, hence disjoint: at that own setting A's complete history
distinguishes `y` from `y′` with certainty, total variation 1 (the 0-or-1 dichotomy of
T1 Lemma A-T (d), T1:73–76, applied to the two-wing record).

*Proof.*
1. `φ^k` is affine, so `(h_A, h_B) = L x_{t_s} + ℓ` with `L` a homomorphism (OA1 D5, OA1:176–195 [W]).
2. Write `P = (P_A, P_B) = P̄ + p`. Given `(x, y)`, `x_{t_s}` is uniform on `C_{xy} = C ∩ P^{-1}(x, y)`, a coset of
   `K = H ∩ ker P̄`. Fix an admissible `(x_0, y_0)` and `c_0 ∈ C_{x_0 y_0}`. For each `x` pick `z ∈ C_{x y_0}` and set
   `e_x = z − c_0 ∈ H`, so `P̄ e_x = (x − x_0, 0)`; for each `y` pick `f_y ∈ H` with `P̄ f_y = (0, y − y_0)` likewise;
   take `e_{x_0} = f_{y_0} = 0`.
   Then `c_0 + e_x + f_y ∈ C` has `P = (x, y)`, so `C_{xy} = c_0 + e_x + f_y + K`.
3. Hence `(h_A, h_B)` given `(x, y)` is uniform on `b + α(x) + β(y) + M`, with `b = L c_0 + ℓ`, `α(x) = L e_x`,
   `β(y) = L f_y`, `M = L K`. Write `α = (α_A, α_B)`, `β = (β_A, β_B)`, `π_A`, `π_B` the projections.
4. A's history law is uniform on `b_A + α_A(x) + β_A(y) + π_A M`. Uniform laws on cosets of one subgroup are equal
   iff the cosets are equal, so (NS) gives `β_A(y) ∈ π_A M` (`β_A(y_0) = 0`). Pick `m_y ∈ M` with
   `π_A m_y = β_A(y)`. Likewise `α_B(x) ∈ π_B M`; pick `n_x ∈ M` with `π_B n_x = α_B(x)`.
5. Subtracting `m_y + n_x ∈ M` does not change the coset: the joint law is uniform on
   `b + (α_A(x) − π_A n_x, β_B(y) − π_B m_y) + M`. With `λ` uniform on `M`,
   `F_A(λ, x) = b_A + α_A(x) − π_A n_x + λ_A`, `F_B(λ, y) = b_B + β_B(y) − π_B m_y + λ_B`. ∎

*Converse.* A Bell-local law with setting-independent `λ` satisfies (NS) (standard). The two directions rest on
different arguments and are stated separately; no equivalence is displayed.

*Relation to sources.* ELABORATING. It sits alongside OA2 Corollary E2 (OA2:606–613 [W]: affine bijection (H1),
H-AR, `q = 2`, parity outcomes, (xiv), CHSH ≤ 2 without spatial separation); neither contains the other. AL covers
every finite abelian group and every local extractor of the complete histories, but needs (NS) and a coset-uniform
law (AL2). E2 covers every law satisfying (xiv), coset-uniform or not, and needs no (NS), but only for `q = 2` parity
outcomes under H-AR. OA2's `Z_4` counterexample (CHSH 4, OA2:612–613) signals, as AL requires. The
single-wing coset structure is T1 Lemma A-T (T1:56–98 [W]) and OA1 D5. The obstruction-favourable reading is
pressure-tested in NOTES.

*Scope limits.*
- **Laws.** Only coset-uniform laws. A setting-independent mixture of coset laws, each satisfying (NS), is
  Bell-local. A law that satisfies (NS) only as a mixture (conditioning on a non-affine event: a coarse-grained herald,
  a nonlinear record predicate; μ-O; a non-uniform structured prior) is not covered. `μ_MD` is such a law.
- **Settings.** Cell values, or affine images of them. A coarse-grained setting is covered when the generator
  values of the two wings range over a product set; otherwise it is not.
- **Postselection** on post-setting events is outside AL, as it is outside Theorem N.
- **Histories.** (NS) is imposed on the complete fixed-region histories. If it is imposed only on a
  setting-selected part, the PR box is reachable inside (vii) with `μ_0`: with `λ_B0 ⊕= λ_A0`,
  `λ_B1 ⊕= λ_A0 ⊕ g_A` (an involution; after the tick `λ_B = (ρ, ρ ⊕ x)`), `a = λ_A0` and `b = λ_B[y]`, the selected
  history `(y, λ_B[y])` is no-signalling, while B's fixed-region history `(ρ, ρ ⊕ x)` signals. So "complete" and
  "fixed region" in (AL4) are load-bearing hypotheses [A; witness from the independent review of r1].

*Consequences.* (i) Ontic parameter dependence (Main's option (a), Main:412) that is statistically no-signalling is
Bell-inert in this class: `ψ_× , μ_0` is an instance. (ii) Route C of SB (SB:181) is closed for the affine class
under (AL2)–(AL4): in the window `Δt/√3 < d ≤ Δt/‖n̂‖₁` (Main:414) a remote-setting dependence of a complete
history either is absorbed into a local model or makes two remote settings perfectly distinguishable. This is a stated
expectation for the separately authorized mixed-path computation (#868 c.6794392080), not a substitute for it.
(iii) With (vii), Main:362 already excludes preparation-indexed edges; AL adds that no in-cone path helps.
A Bell violation with complete-history no-signalling under the ledger therefore requires leaving (vii), (AL2), (AL3)
or every-run accounting; no-signalling imposed on less than the complete fixed-region history is a weaker
admissibility criterion (scope limit **Histories**), not an escape in this ladder's sense.

***

## 5. Open premises, and what would settle them

| Item | Status | What would settle it |
|---|---|---|
| Stage 7: a selector for the quantum Bell set | UNDETERMINED | an OI-sourced principle, independent of the target table, that bounds CHSH by `2√2` and reaches it (SB N4); for composites, which of the operational-completion conditions (i)–(v) (Main:562; `exactAll_iff_physical_general` [K]) an embedded process supplies |
| NBA for non-affine branches (BS:232–244) | open | for the H-Bell branch outside (vii): a sourced preparation family with complete-history NS and its reason (N3; PPS:134–145 forbids full span), H-Bell (i)–(iii) (`papers/Substratum.md`:131–133) |
| Proposition AL | [A]; one independent non-author review (ACCEPT WITH CHANGES, applied in r2); ChatGPT review pending | ChatGPT review at the exact head; extension to mixtures that satisfy (NS) only jointly, and to coarse-grained settings with correlated generators |
| Record convention for (AL4) | open | whether an embedded observer's complete history is the full fixed record region or may be a setting-selected read (NOTES Q4); AL's obstruction needs the former, and the selected-read witness of §4 gives PR for the latter |
| Run law under (iv) | open | whether the law an observer's actual records select is coset-uniform (RC C9, C10; OA1:176–195 notes (xiv) may fail on the actual orbit) |
| MI\* versus (xiv) | reading | whether (xiv)'s "response-relevant pre-setting variable" includes generator residues that reach a record (then (xiv) is MI\*) |
| Embedded setting generation | open | a native account of settings as configuration content with the independence (xiv) posits; QH uses the supplied controller P3 |
| Physical *c* (Main:414) | open | which cone is physical; under AL it decides only whether a window dependence is superluminal signalling, not whether it yields a Bell escape |

**What a Bell escape would require (stated, not adopted).** An update outside (vii) is a Layer-0 revision under
§A.29: it would have to state in advance the results it preserves (the dispersion and area-law results that rest on
(vii) and (x), Main:362's reference graph), deliver a prediction beyond the Bell table (for example the resolution at
which masking fails, SB:220), supply complete-history no-signalling for a sourced, restricted preparation family,
and supply a selector. None is supplied.

***

## 6. §A.42 item 8 reference table

| Reference | Attached to | Classification |
|---|---|---|
| `papers/Main.md` @ `c3b5f37a` (Main:14–18, :42, :97, :360–427, :480–486, :516–518, :546–552, :562, :724) | §0, stages 0–7, §4 consequences | support on `main` |
| `Equivalence.lean` @ `c3b5f37a` (:150–156, :245, :294, :422, :462, :466–468) | stage 0, directions | support on `main` [K] |
| OA1 (`5a16b213…`) :176–195; :103–105, :111–112, :556–558 | §4 step 1; (AL2) law family; stage 4 settings as configuration content | support on `main` [W] |
| OA2 (`8f8ddf73…`) :606–613, :875 | §4 relation | provenance for priority; AL does not use E2 |
| T1 (`a9cbc675…`) :56–98 | §4 dichotomy | support on `main` [W] for the single-wing coset fact; AL restates the step it uses |
| PPS :134–145 | stage 6, §2 check 1, §5 | support on `main` [W] |
| BS @ `e1534b08` (Theorem N, N′, Lemma G, §4 bound, NBA) | stages 5–6, §0 controlling condition | **support off `main`: gap** if this record lands; the exogenous form (Main:364–389) is on `main`, the closed native form is not |
| SB @ `86a413c8` (L3, routes A/B/C, N3, N4) | stage 3 (directed Sep), §4 route C, stage 7 | **support off `main`: gap** for L3 and N4 if this record lands; L4 is not cited; its content for the linear update of (vii) is Main:362 (support on `main`) |
| QH @ `ffc9cda4` ((V), (C), QC) | stages 4 and 7 remarks | **provenance** for stage 4; **support off `main`: gap** for the stage-7 illustration, on which no verdict rests |
| RC @ `9f7d2612` (Q2-A/F/P levels, C9, C10, H-xiv, `D_0`) | classification vocabulary, §5, the name `D_0` | provenance; the facts used are cited on `main` (OA1, Main:42); no verdict rests on RC |
| `papers/Substratum.md`:131–133 @ `c3b5f37a` | §5 (H-Bell) | support on `main` |
| #868 c.6854708572; c.6794392080 | authority; mixed-path unit | planning records; provenance |
| PR #1231 reviews 5857227567 (REVISE, `7abf59d7`), 5857981727 (ACCEPT WITH NONBLOCKING NITS, `e1534b08`); PR #1232 reviews 5858000929 (REVISE, `b94b283a`), 5859960068 (ACCEPT WITH NITS, `86a413c8`); PR #1269 review 5891666660 (ACCEPT WITH DOCUMENTATION NITS, `acf28d3a`; QH's head `ffc9cda4` adds two record-nit commits); PR #1268 review 5891524305 (ACCEPT, `9f7d2612`) | input status | host records; provenance. Model acceptance is not verification (§A.46 item 7) |
