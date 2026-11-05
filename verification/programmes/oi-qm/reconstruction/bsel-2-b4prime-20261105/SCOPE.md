# BSEL-2 unit B4′: single-unit scope (r3, draft for independent review)

**Status:** draft scope r3, revised after review of r1 (REVISE) and delta review of r2 (ACCEPT WITH CHANGES). r1 and r2
are kept as `SCOPE-B4prime-r1.md` and `SCOPE-B4prime-r2.md`.
Paper-only (#914 c.6567372732, H.2; #1033 "Gate and outcome"). Grants nothing.
**Authority:** owner choice of B4′, #1033 c.6652148478; activation c.6652730356; owner rulings on this scope
c.6652903587. Writer: the dedicated BSEL-2 writer.
**Drafting snapshot `D`:** `origin/main` `4f016afd943f5a3939493eab752664949e90dbbb`. Every [K] line below was re-read
at `D`.
**Accepted sources:** `BSEL2-B3-B5.md` at `88c175c3` ("F", by line; branch-only, off `main`) and sources on `main`.
#1033/#914 comments are provenance only. No off-repo record is quoted (F ll. 33–38: PL-BSEL2, RV-BSEL2, Thread E).

## 0. Provenance ruling
amaybaum, Claude Code session chat, 2026-11-05, recorded at #1033 c.6652903587 (posted 2026-11-05T08:02:12Z):
> 1. B4′ evidence: GitHub comments on #1033 may be cited as provenance, but not as proof. Any result that depends on
> those comments must be independently re-derived from accepted sources or explicitly marked unresolved.

So every cell of the B4′ note c.6567713723 ("B4N") or of its review c.6567723333 that the unit uses is handled one of
two ways. Either it is re-derived in the unit's own record from F, `main` and written-out algebra, or it is labelled
UNRESOLVED (rests on c.<id>). B4N is a cross-check only. Rulings 2 and 3 also govern the unit (§5, §6).

## 1. The exact question
`G(U,U′)` is `TwoSidedRelated a₀ U U′` [K TSG:84]: `U′_t = L_tU_tK_t` with `L_t ∈ LeftFibreGroup` [TSG:78] and
`K_t ∈ WeakAnchorStabilizer a₀` [CLG:114], both time-dependent. For candidate `C` (§3), `O_C(U,U′)` is equality of
the complete-record laws `Λ_C`: every branch mass and every failure record `⊥`, unnormalized and unconditioned.
For every candidate, the two directions the owner asks about (ruling 2) are posed separately:
- **G⇒O**, written `R[C]`;
- **O⇒G**, written `Q[C]`.

**W0 (first work item): derive `Λ_C`** for C0, C1, C1′ and for C2 under each of Rst-auto, Rst-ch and Rst-sel.
- Under Rst-auto and Rst-ch, the expected form is the factorization: the root factor `Γ_{t₁}(v₁, j)` times the
  `𝒪₂(t_{m+1}, t_m)` factors.
- Under Rst-sel, the expected form is the ok-chain, with anchored-to-anchored moduli, and the `⊥` masses
  `‖(1 − |a₀⟩⟨a₀|)P_v·‖²`.
- Each form is derived from H-comp, Rd and Rst-x as frozen in §3. B4N D1, D2, D2′ and D4 serve only as cross-checks.

**`R_C` (this scope's own definitions, frozen):**
- `R_C0`: `Γ_t` equal for all `t`.
- `R_C1`: `FibreGram a₀ U_t` equal for all `t`.
- `R_C1′`: `U′_te_j ∈ U(1)·U_te_j` for all `t, j`.
- `R_C2-auto`, `R_C2-ch`: `R_C0` and `𝒪₂(t,s)` [CF:123] equal for all `s < t`.
- `R_C2-sel`: `R_C2-ch` plus equal moduli `|⟨e_w,U_te_v⟩|²` and `|⟨e_w,U_tU_sᴴe_v⟩|²`.

**E[C]⊇** (`R_C ⇒ O_C`) and **E[C]⊆** (`O_C ⇒ R_C`) are decided separately, from W0. A failed direction is reported.
Any alternative `R_C` is out of scope for this unit and is recorded as a proposal only.

**Q2A.** `Q[C2-ch]` and `Q[C2-sel]` at `|A| ≥ 2`.

**S1′.** `Sub[C1′]`, both inclusions, reported outside the owner-direction cells.

**Cmp (gauge respect on every candidate).** One row per candidate × `|V|` (split wherever a result depends on it, e.g.
C0 at `|V| = 2` against `|V| ≥ 3`) × `|A|` × `Rst` × class (all unitary families, or `PPer`). Each row has two cells:
G⇒O and O⇒G. Each cell names its support. A failed `R[C]` voids every gauge-class reading of `C`, and the raw
comparisons stand. No cell, and no combination of cells, is a global gauge classification.

**Src′ (reported separately: composition physically sourced).** Assume H-comp with `Rst-x` is the physical composition
rule. The unit states:
- (a) the subgroup `𝒢_C2-x` of symmetries of C2's laws, re-derived;
- (b) **Own[C2-x]**: whether `O_C2-x ⇒ ∼_C2-x`;
- (c) what does or does not follow about `G`.

`∼_C` is labelled "relative to `𝒢_C`, not OI's gauge" and never fills a G⇒O or O⇒G cell. Form:
CONDITIONAL[H-comp, Acc₂, Rst-x, P-conf]. Physical supply is a SOURCING-GAP.

**Order:** W0 → E[C] → Q2A → S1′ → Cmp → Src′.

## 2. Starting points
**Support classes:**
- K: kernel on `main`.
- M: prose on `main`.
- F: F's own derivation from [K] or elementary algebra; off `main`.
- F←c: an F step that inherits a comment-only premise.
- c: comment only, which is provenance.
- O: owner decision.

| Fact | Where | Class | Use in this unit |
|---|---|---|---|
| Objects `𝒜, C, P_w, 𝒢_L, 𝒲, Γ`; H-fac interface (proposed, not adopted); GR(I) under ∀U; NI | F ll. 53–67 | F | definitions |
| FI, FI_c; FI ⇒ FI_c | F ll. 81–91 | F, O (Q1) | FI is a convention only |
| Q1⇐ under FI; CE-3 | F ll. 175–185 | F ([K] TSG:217, CLG:273) | usable |
| Lemma HS | F l. 188 | c (c.6567694252 §2 Step 2) | re-derive, or UNRESOLVED |
| Q1⇒; Q1c(⇒); DC's step "R[C] ⇒ O_C ⊇ Fib" | F ll. 197–210, 219, 242 | F←c (inherit HS) | as HS |
| Lemma CM; Q1c(⇐); CE-1, CE-2 | F ll. 191–195, 219–239 | F ([L] Schur) | usable |
| DC witnesses: TG3; `F₃`/`F̄₃` at `\|V\|≥3`, any `\|A\|`; `Fib = G` at `\|V\|=2, \|A\|=1` | F ll. 243–261 | F ([K] TSG:263, :752, :839, :870, :907) | usable |
| K3: B4′'s C1 fails GR | F l. 273 | F←c (B4N HC-A) | re-derive by hand |
| Content rests on ∀U and H-fac; restricted `U` UNDECIDED | F ll. 279–287 | F | scope |
| Q5a `Γ^alt ∈ PPer`; Q5b lifts not `G`-related | F ll. 137–144, 351–362 | F ([K] RCAT:162, TSG:84, :907) | usable |
| Q5c C2 cells (`R` and `Q` fail at `Γ^alt`) | F ll. 366–376, 394 | F←c (B4N D4) | re-derive after W0 |
| Undecided list; owner questions; §7 not authorized | F ll. 425–457 | F | open |
| B4N table, `Cov`, `Sub[C2]`, `Src`; review | c.6567713723, c.6567723333 | c | provenance only |
| Lift freedom two-sided; one-time residue; fibre-Gram data a coordinate | Main:646 | M | context |
| "The fibre-Gram data is a coordinate on the lift space, not a physical quantity" | TSG:49–50 (docstring prose) | M | context |
| Fixed-basis layer acts on visible equality, trivial ancilla (`Fin 1`) only | `rooted_eq_iff_slice_eq` TrackBQfbBridge:180 | K | context, `\|A\|=1` |
| CT1 | `ct1_relative_iff_constRight` CTI:305 | K | usable, both directions |
| `twoSidedRelated_iff`; TG3 slices and lifts; `weak_mul` | TSG:839, :907, :966, :252 | K | usable |

F's standing as an accepted source rests on the owner's decisions c.6624264992 and c.6652148478; the #1084 review
c.6622656252 (ACCEPT at `88c175c3`) is provenance. F's header (ll. 3–4) predates that review. The exact machine
checks of B4N and its review (HC-A, HC-B, RC1–RC3) are provenance. No result of this unit rests on them.

## 3. Definitions frozen before work
- **Carrier:** `V × A`, fixed `a₀`, `e_v = e_{(v,a₀)}`, `|V| ≥ 2` (F ll. 53–61). The gauge `𝒢` is the set of families
  `g = (L_t, K_t)`, acting by `gU = (L_tU_tK_t)`.
  - **𝒢 is a group, re-derived in the record:** products of weak elements are weak (`weak_mul` TSG:252). Inverses
    (`Kᴴe_v = c̄e_v` for unitary weak `K`) and the closure of `LeftFibreGroup` are elementary.
- **NI** (F l. 67) and **AR** (the apparatus record, B1(c) note c.6567694252 §1.1, as provenance): recorded; not used.
- **FI** (F l. 82): an explicit mathematical convention [O c.6624264992 Q1]. **Q1c** (F ll. 214–220) [O Q3].
  **H-fac** (F ll. 62–65).
- **∀U:** the owner's Q2 fixes ∀U for the one-time equivalence only. Extending it to two-time families (lifts range over
  all unitary families `ℕ → U(V×A)`) is adopted here as this scope's own frozen definition. B4N used the same
  convention.
- **H-comp:** from the root to the first read at `s`, the state evolves by `U_s`. Between reads at `s < t`, it evolves
  by `T_{t,s}(U) = U_tU_sᴴ`.
- **Acc:** Acc₁ is one read at one time. Acc₂ is any finite increasing read list, with all records kept jointly.
- **Preparations:** P-conf is `|j,a₀⟩` at the root, each `j` separately, with laws indexed by `j`. P-coh is
  `ρ ⊗ |a₀⟩⟨a₀|` for every density matrix `ρ` on `V`. `prior` only mixes the per-`j` laws and is labelled where used.
- **Reads:** Rd is a Lüders read `P_v = |v⟩⟨v| ⊗ 1_A` with record `v`.
- **Resets:** Rst-auto (`|A| = 1`) leaves `|v,a₀⟩` up to a phase. Rst-ch replaces the ancilla by `|a₀⟩`. Rst-sel is an
  `|a₀⟩⟨a₀|` test; `⊥` is kept with its mass and is not continued.
- **Candidates (closed list):**
  - C0 = (P-conf, Acc₁, Rd);
  - C1 = (P-coh, Acc₁, Rd);
  - C1′ = (P-conf, Acc₁, H-fac, all devices);
  - C2-x = (P-conf, Acc₂, Rd, H-comp, Rst-x), for x ∈ {auto, ch, sel}.

  X (global reversibility) is a control, never an `Acc`.
- **Statements:**
  - `R[C]`: `∀U ∀g ∈ 𝒢: Λ_C(gU) = Λ_C(U)`.
  - `Q[C]`: `∀U,U′: O_C(U,U′) ⇒ G(U,U′)`.
  - `Sub[C]`: `𝒢_C = {g : ∀U, Λ_C(gU) = Λ_C(U)}`; `∼_C` is relatedness by `𝒢_C`.
  - `Cov`: the `g` with `T(gU)_{t,s} ∈ U(1)·L_tT(U)_{t,s}L_sᴴ` for all `t, s`.
  - `Src`: whether, if H-comp with `Rst-x` is the physical composition rule, `g ∉ 𝒢_C2-x` (in particular `K_tK_sᴴ`
    non-scalar) is a symmetry of C2's laws.
  - Plus `R_C`, `E[C]` and Own[C2-x] (§1).
- **Class:** `PPer` [RootedClassification:32] requires `Γ_0 = 1`, `IsRowStochastic` at every `t`, and a period. The
  readback is column-stochastic (`readback` DilationChoice:86; `readback_isColStochastic`, R-1, :93). Every `PPer` claim
  states the orientation and checks it (W9).

## 4. Deliverable
One paper record in F's form. Each result carries one label per direction and scope. Three blocks stay visibly
separate:
- (i) proved and disproved mathematics;
- (ii) conditional readings, listing every §3 hypothesis used;
- (iii) unresolved physical sourcing.

It ends with the Cmp table, the §9 matrix filled in, and a "does NOT establish" column.

**Premise ledger (§A.42 item 8).** Each off-`main` reference is classified one at a time, by reading the claim it is
attached to:
- **provenance:** the claim does not use the referenced content;
- **support on `main`:** the content is on `main` and supports the claim as it stands;
- **support off `main`:** a gap.

F itself is off `main`: every F fact used is support off `main` until F lands. A comment can only be provenance.

## 5. Decision rule (preregistered, §A.29)
**Labels**, mapped to the owner's vocabulary:
- **MATHEMATICAL → proved:** a complete paper proof under the stated quantifiers. Each step is [K] at `D` (identifier
  and line), an F line of class F, or written-out elementary algebra.
- **COUNTEREXAMPLE[scope] → disproved:** an explicit instance with every entry written, checked by hand in exact
  arithmetic, refuting a universal direction and nothing more. The bracket names the candidate, `|V|`, `|A|`, `Rst`,
  same-`Γ` or not, and class.
- **CONDITIONAL[...] → conditional:** required beside every proved result read about OI lifts or physics.
- **SOURCING-GAP:** physical supply of any hypothesis, and which candidate is native.
- **UNDECIDED, VOID, or UNRESOLVED (rests on c.<id>) → unresolved.**
  - UNDECIDED names the unproved step; a deciding computation is written as a proposal and not run.
  - VOID: a control fails, a definition cannot be fixed from accepted sources, or a [K] line does not resolve at `D`.
  - UNRESOLVED (rests on c.<id>): a cell whose only support is a comment.

**"Equivalent"** is written only when both directions are proved at the same scope: the same `|V|`, `|A|`, `Rst` and
class. A one-direction result is reported as that direction (ruling 2). Verdicts print only over green controls, with
text generated from the derivation.

**Controls**
- **K-A (cross-check against B4N):** where a re-derived cell disagrees with B4N, that item halts and the disagreement
  is reported as a finding. It is settled only by a hand check written in the record; neither side is presumed right.
- **K-B (positive):** `R_C` is invariant under every `g ∈ 𝒢_C`.
- **K-C (non-vacuity):** the identity family against `H(1)` is separated by every `R_C`.
- **K-D (same-Γ):** every pair offered as evidence about gauge freedom has equal `Γ_t` for all `t`.
- **K-E (accessibility):** every witness states three things:
  - (a) whether it is explicit or existence-only; existence is not a COUNTEREXAMPLE;
  - (b) its class: whether it is in `PPer`, with the orientation checked (W9);
  - (c) that the separating procedure is one of `C`'s frozen procedures, not X.

  Nothing transfers into `PPer` without its own witness there.
- **K-F (directions, §A.34):** each direction has its own proof or witness. Uniqueness, extension or characterization
  relative to fixed data is not a converse. Each use of `twoSidedRelated_iff` names `mp` or `mpr`.
- **K-G (masses):** under Rst-sel, `⊥` masses are kept unnormalized; each witness's masses sum to 1 per `j`; every
  conditioned statement is labelled.
- **K-H (ℕ coverage):** a witness claimed on ℕ is eventually constant or periodic, and its argument covers every
  finite read list, not a horizon.
- **K-I (identical procedure):** only `U ↦ gU` or `U ↦ U′` changes. Preparation, read times, `Rst` and reads stay
  fixed. Two-time candidates use time-dependent `g`.

**Hidden-assumption watch (§A.31).** The productivity test: a finding counts if it is strictly stronger than
restating F, and it either constrains a candidate or exposes an assumption.
- **W1:** ∀U carries much of the content (F ll. 279–287). A result that needs ∀U is not about OI-realizable lifts.
- **W2:** ∀U is not "sufficient reversible control". That bare OI does not supply that condition is clause (iii) of
  `main_result` (GeneralCarrier:188); `oi_alone_not_qm` (:160) proves only that OI alone is not QM.
- **W3:** the `a₀` reset frame of Rst-ch and Rst-sel is not `𝒢_L`-invariant. A `|A| ≥ 2` result that rests on it is a
  property of the reset hypothesis, not of `G`.
- **W4:** `a₀` is fixed; re-anchoring is out of scope.
- **W5:** per-`j` laws are a setting choice. Under `prior`, `O_C` only coarsens.
- **W6:** the `mpr` of `twoSided_slice_iff` gives some `(L, K)`. Membership of that `K` in `𝒢_C2-x` (Own[C2-x]) is a
  separate claim.
- **W7:** a `|A| = 1` witness embedded at `|A| ≥ 2` (Q2A) is re-checked for non-relatedness under the larger left group
  and for zero `⊥` mass.
- **W8:** a branch favourable to native gauge fixing (Src′) is pressure-tested. Its fixing comes from H-comp, which is
  a hypothesis.
- **W9:** the readback is column-stochastic, while `PPer` requires row-stochastic slices. Every `PPer` claim states
  which orientation it uses and checks it.

## 6. Non-goals
- No physical gauge equivalence, and no native observer inferred from a quotient [O c.6624264992; #1033 Gate].
- No assumption, relation or class introduced solely to obtain an equivalence (c.6652903587 rulings 2–3). No new
  premise, candidate, reset or `Acc` beyond §3.
- No computation, enumeration, simulation, script or Lean.
- No promotion, propagation, #914 matrix edit or manuscript change.
- No use of B6 (blocked on O-REC, O-SET), Q3/Q3c, Q5d, restricted-`U` classes or two-time H-fac devices.
- No literature claim on Barandes' gauge discussion (D-42–D-44).
- No branch, PR or post, and no mutation of #1009, #1023, #1011, #1003 or #918, before this scope is reviewed.

## 7. Size and stopping
One unit, one writer. The record is estimated at 250–350 lines, since W0 re-derives B4N's laws. The nontrivial block
of each witness has `|V| ≤ 4`, `|A| ≤ 2`; a ⊕1 extension on further configurations, as in F ll. 245–247, is allowed.
Witnesses are checked by hand.

Stop and report a wall (§A.12) when:
- a step needs more than exact hand arithmetic (UNDECIDED, with a proposal);
- a definition needs PL-BSEL2 or Thread E (VOID; stop, and do not quote them);
- a control fails, or a [K] line drifts;
- K-A disagrees with B4N (that item halts; the rest continue).

A cell that rests only on a comment and cannot be re-derived by exact hand arithmetic is reported UNRESOLVED (rests on
c.<id>), and the unit continues. The unit does not widen to rescue a result.

## 8. Owner questions and recorded findings
- **D-38 (B5's lane), D-39 (B5's Lean work):** not touched. Q5a and Q5b stand on F's own support; Q5c's C2 cells need
  W0. No lane is chosen and there is no Lean work.
- **Q6 (quoting PL-BSEL2 and Thread E):** not touched; nothing from them is quoted. Where a definition traces to
  PL-BSEL2 (B4N's [plan] tags; F l. 62), §3 restates it and records the trace as provenance.
- **F §6 q. 7:** not touched; F's standing as an accepted source rests on the owner's decisions c.6624264992 and
  c.6652148478; the #1084 review c.6622656252 is provenance. D-36 and F §6's undecided items are not touched.
- **Branch name:** closed by c.6652903587 (decision 4). The branch is `research/bsel2-b3-b5-20261104` at `88c175c3`.
  The record directory `bsel-2-b3-b5-20261104/` is correct.
- **Recorded findings, not changed (c.6652903587, to be assessed):**
  - #1033's "accessible redundancy" gloss differs from the frozen AR definition, the apparatus record.
  - #1033's Readiness line omits B4′, although B4N exists.
- **Recorded findings, not resolved:**
  - #1033's Readiness line still says "B3/B5, not started", though F covers both.
  - A designated writer is now recorded at #1033 c.6653013695.

## 9. Preregistered outcome matrix (draft)
Labels: proved, disproved, conditional; "re-derive" (pending W0 and its items); **open** (a question this unit poses that
has no F or B4N witness); unresolved is the terminal label for a re-derive or open cell that cannot be decided.
★ marks a cell F fixes on its own support (class F). The provenance column records where B4N and F stood, not
expected outcomes (§A.29); it is not support.

| Candidate | `\|V\|` | `\|A\|` | Class | G⇒O | O⇒G | Provenance position (not support) |
|---|---|---|---|---|---|---|
| C0 | any | any | all | proved★ (F l. 178: TSG:217, CLG:273) | see rows below | — |
| C0 | 2 | 1 | all | proved★ | proved★ (F ll. 254–261) | — |
| C0 | ≥3 | 1 | all (witness outside `PPer`) | proved★ | disproved★ (TG3 at 4, `F₃` at ≥3; F ll. 244–249) | — |
| C0 | 4 | 1 | `PPer` | proved★ | disproved★ (`Γ^alt` pair; F Q5a, Q5b) | — |
| C0 | 3 | 1 | `PPer` | proved | open | Candidate: the alternating `1, F₃` against `1, F̄₃` on the anchored lines with `1` on `C`, giving invariant `ω/9` against `ω̄/9` |
| C0 | ≥5 | 1 | `PPer` | proved | open | Candidate: `Γ^alt ⊕ 1` on the further configurations, per F ll. 245–247. `Γ₀ = 1`, the slices are symmetric, period 2, so it lies in `PPer`. The `∼_D` invariant `G⁽⁰⁾₁₀G⁽¹⁾₀₁` is `1/16` against `i/16` (TSG:870, :263) |
| C0 | ≥3 | ≥2 | all (witness outside `PPer`) | proved★ | disproved★ (`F₃` placed on anchored lines; F ll. 245–249) | — |
| C0 | ≥3 | ≥2 | `PPer` | proved | open | Candidate: the alternating `1, F₃` against `1, F̄₃` on the anchored lines with `1` on `C`, giving invariant `ω/9` against `ω̄/9` |
| C0 | 2 | ≥2 | any | proved | not addressed: F §6 undecided (F l. 430); untouched (§8) | — |
| C1 | ≥2 | 1 | all; `PPer` | re-derive | re-derive | G⇒O: B4N D2's explicit witness (`U = H(1)`, `K = diag(1,−1,1,1)`, `ρ = \|+⟩⟨+\|`), disproved; `PPer` if placed at t = 1 with `U₀ = 1` (W9). O⇒G: B4N D2, proved (equal Grams, then `mpr` of TSG:839) |
| C1 | ≥2 | ≥2 | all | open | re-derive | G⇒O: no witness (B4N's is at `\|A\| = 1`; embedding per W7). O⇒G: B4N D2, "every `\|A\|`" |
| C1′ | ≥2 | 1 | all; `PPer` | re-derive | re-derive | G⇒O: RHC2 as restated in B4N D2′ (`W = H(1)`; `H(1)` against `diag(1,i,1,1)H(1)`), disproved. O⇒G: B4N D2′, proved |
| C1′ | ≥2 | ≥2 | all | open | re-derive | O⇒G: B4N D2′ (no `\|A\|` restriction) |
| C2-auto | ≥2 (witness 4) | 1 | all | re-derive | re-derive | G⇒O: RHC6. O⇒G: RHC6 images of TG3. Both outside `PPer` |
| C2-auto | 4 | 1 | `PPer` | re-derive after W0 | re-derive after W0 | F Q5c (F←c through the factorization only): disproved in both directions |
| C2-ch | ≥2 (witness 2) | ≥2 | all; `PPer` | re-derive | open (Q2A) | G⇒O: B4N `1⊗H₂` (`U = (1, swap((0,1),(1,1)))`, read (0,1), `j = 0`: (1,0) against (½,½), no `⊥`). Γ ≡ 1, so in `PPer` subject to W9. O⇒G: B4N undecided; candidate is the embedded Γ^alt pair (W7) |
| C2-sel | ≥2 (witness 2) | ≥2 | all; `PPer` | re-derive | open (Q2A) | G⇒O: the same `1⊗H₂`; root (ok, `⊥`) = (1,0) against (½,½). O⇒G: as C2-ch |

**Conditional block (separate; never fills a cell above).** Src′ (a) `𝒢_C2-x` and (b) Own[C2-x], for each `x`, are
re-derive or unresolved. Each is CONDITIONAL[H-comp, Acc₂, Rst-x, P-conf] and stated relative to `𝒢_C`, not OI's
gauge. Physical supply is a SOURCING-GAP.

The non-C0 rows record B4N's and F's positions as provenance.
