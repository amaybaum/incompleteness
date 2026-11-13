# OA-3 (r3): native gbit or dual-gbit shapes in `G_SM`, and Theorem E(b) without (H4)

**Standing.** WIP / UNVERIFIED author report for unit OA-3 under #1169, revision r3. r2 applied the
independent review `REVIEW-OA-3.md` (ACCEPT WITH CHANGES, F1–F7). r3 applies the focused recheck
`RECHECK-OA-3-r2.md` (ACCEPT WITH CHANGES: E1, E2 required; m1–m3 optional, all applied), which
re-derived and accepted (PT), (PT-a) and (PT-b) and conceded D1. r3's edits were then given an exact-text
delta review `DELTA-REVIEW-OA-3-r3.md` (ACCEPT WITH CHANGES: R1–R4 required, O1–O5 optional), whose
required edits and optional O1–O3 and O5 are applied here; those edits are unreviewed.

- **Scope.** Paper-only: reading and hand derivations. No computation on any OI rule (no script,
  numerics, enumeration or LP), no Lean change, no manuscript edit, no premise adopted, no claim
  promoted. Recorded on the research branch of draft PR #1265 (not for merge); not landed on `main`.
- **Authorization.** Owner amaybaum, 2026-11-12, #1169 comment c.6833027576: a paper-only OA-3
  (as relayed by the coordinator; not re-fetched in this unit). Unit OA-3: one bounded paper-only
  investigation (OA-2 r3 "next step 1").
- **Commands used (r1 and r2).** `git fetch`, `git show`, `git ls-tree`, `git grep`, `git diff`,
  `git rev-parse`, `grep`, `sed`, `cut`, `tr`, `diff`, `head`, `fold`, `wc`, `cat -n`, `ls`, `mkdir`.
  No script was written or run on any rule or source; `python3` was used only for inline text
  replacements in this report file. No source copy was written anywhere.

**Snapshots.**

- `main` = `615cc1190ec1bda69093be1eac49c839744008a5` (read with `git show`). `origin/main` is now
  `911a5cb6`. `git diff 615cc119 911a5cb6` touches, under `papers/` and
  `verification/programmes/oi-qm/`, only `papers/Main.md` (lines 36, 60, 90, 151, 700, 724; one line each) and
  `papers/SM.md` (lines 196, 605). Main:58 and the ledger's item (xiv) at Main:724 are unchanged;
  Main:60 adds the source of visible finiteness ("from the finite-capacity clause of the
  Definition") without changing that `S`'s visible part is finite; SM §3.1 (SM:100–169) is
  untouched; nothing under `verification/programmes/oi-qm/` changed; line numbers are unchanged. The pin is current for every
  citation below.
- Research branch `research/oa1-w1-1-20261112` = `815d6a8ee110ec713b54549ba70c501eb8f1db59`
  (OA-1 r4, OA-2 r3 and their reviews).

**Citation forms.** `OA2:n` = `.../oa-2-20261112/OA-2-REPORT-r3.md` at `815d6a8e`; `Rv2:n` =
`REVIEW-OA-2.md` there; `Rv2b:n` = `REVIEW-OA-2-r2.md` there; `OA1:n` =
`.../oa-1-20261112/OA-1-REPORT-r4.md` at `815d6a8e`; `SM:n` = `papers/SM.md`; `Main:n` =
`papers/Main.md`; `M2:n` = `mechanism-2-20261108/DESIGN.md`; `MA:n` / `MAR:n` =
`minacc-1-20261108/DESIGN.md` / `RESULT.md`; `AP1:n` = `apparatus-1-20261107/DESIGN.md`;
`M1:n` = `mechanism-1-20261107/DESIGN.md`; `obsmu:n` = `observer-interface-obsmu-20261104/ANALYSIS.md`;
`L3b` = `verification/programmes/oi-qm/interface/round-l3b-orthogonal-rule-controls/`; all of `M2`,
`MA`, `MAR`, `AP1`, `M1`, `obsmu` under `verification/programmes/oi-qm/reconstruction/` at
`main@615cc119`. `Rv3:n` = line `n` of `REVIEW-OA-3.md` in this directory; `r1:n` = line `n`
of `OA-3-REPORT.md` in this directory.

**Support labels** as in OA2:43–51: [K] Lean statement read, [P] manuscript, [R] research record,
[W] hand derivation here (unreviewed), [RW] re-derived by hand by the OA-3 reviewer, [L] literature
from memory (context only), [O] open.

***

## 0. Plain-language summary

1. minacc-1's gate cancellation transfers to `G_SM` (on the right-hand side only). Under P1, P2 and
   H-PREP's known-1 supply it defeats Lemma Q's protection, which settles at [W] level the item M2
   records as open (M2:857–859). It *adds* access; it is a refuter of read restriction, not a source
   of it (N1).
2. In OA-2's E3 setting the observer's own cells are held, so a held reader exerts no unknown
   "kick". Lemma Q's reader-kick mechanism needs readers with an unknown slot (P2, with P1). Whether
   hidden-cell noise yields a native restriction for observers below Lemma OBS's block size is open
   (N1.3, N5).
3. `G_SM`'s left edge is fixed and enters linearly. From that alone, three consecutive observer
   sites with retained history determine the entire configuration of a finite ring of `L` sites
   within `2(L−3)` ticks, whatever the settings (Lemma OBS, N2). The proof is measure-free. It is the
   permutive-CA argument (Hedlund 1969, [L]); within the corpus its content is that an ungated
   permutive edge is a native return path.
4. Hence, as a corollary, for such observers on a finite ring, with MP-0b history or heralded
   composites (V-ii-H), heralds, a measurement stage of at least `2(L−2)`, and every configuration
   in the preparations' supports reachable by a preparation of stage at least `2(L−3)` (true under
   initial laws with `F`-invariant support, e.g. μ-G and μ-O, whenever the horizon is at least `4L − 10`, and under any initial law when every preparation
   has that stage), `G_SM`'s prepare–measure fragment is a simplex: neither the gbit shape nor the
   dual shape occurs (Theorem S, N3). The same holds for class N and for SM's rule at every `q`.
5. Non-nested reads (AW-OA2-4), for the affine class under (H1), H-AR, (H3), (xiv) and (SP): OA-2
   r3's gap paragraph assumed an effect class under which OA-2's own Lemma 1 is false. Under the
   class Lemma 1 presupposes (heralded composites are effects, V-ii-H), the effect cones coincide
   with variant (i)'s, and Theorem E(b) holds with (H4) replaced by that class (N4). If heralds are
   typed as held at use time, that class is itself retention-type.
6. Under the narrower class (V-ii-U: multi-tick heralds for preparations, single-tick reads for
   effects), a 3-cell shift with a one-cell observer already shows an exact gbit, and Lemma 1 fails.
   That "success" is a memory artefact of the convention, present already for trivial dynamics (a
   shift), and does not count (N4.2).
7. **Verdict: OPEN, narrowed.** Still open: the union of small observers (no three consecutive held
   sites), horizons below Theorem S's bounds, infinite windows, the (V-ii-U) record class, and
   initial laws with short preparations outside (PT). The preregistered computation (OA2:776–833) is
   decisive for its own instance, with three design amendments (§4).

***

## 1. Definitions (kept from OA-2; nothing redefined)

- **Setup.** `𝔖 = (S, φ, (V, H), μ, A)` (OA2:83–92; OA1:90–105). Procedures `Proc(𝔖)`: waiting under
  `φ`, settings as cell contents (initial, or written by `φ` from records), heralds and discards
  (OA2:95–101). "Held" = a function of present `V` (OA1:107–110). MP-0b retains history (OA1:554–555).
- **Label conventions.** C-PM: a preparation's own label cells (setting, coin, herald records) are
  not effects; effects are post-processings of held records other than those (OA2:103–111). C-PM′:
  the labels are physically out of reach (OA2:112–117).
- **E3 operational class** `[p]`; `W = span(reachable laws)`, `U = ⋃ supp` (OA2:127–132).
  Induced maps; heralded branches subnormalized then renormalized (OA2:136–141). **Lemma 1**
  (closure): every `π ∈ Proc` induces a well-defined `π_E` because `e∘π` is available for every
  available `e` (OA2:224–227).
- **Criteria G0–G3** (OA2:143–152). G3 here is always the prepare–measure criterion (OA2:521–523).
- **H-AR** additive (cell-aligned, full-resolution) observer (OA2:175–186). **(H4)** nested records
  (OA2:486). **(SP)** spanning of reachable record laws (OA2:519–521). **(xiv)** measurement
  independence (Main:724). **Proposition B** (i)–(iv) (OA2:237–278); (iv) needs (i)–(iii)
  (OA2:248–249). **Corollary B′**: G3 needs preparation or effect equivalences coarser than ontic
  equality (OA2:301–312).
- **Measures** μ-O (derived), μ-G and μ-R (posited, ledger (iv)) (OA1:96–105, :236–270). MP-0a
  declared ready cells (OA2:783). Each result below states which initial law it uses.
- **The two shapes.** (a) gbit: two switch-selected reads `f₀, f₁` of one carrier, four reachable
  preparations fixing `(f₀, f₁)`, joint read unavailable under every protocol (OA2:767–770;
  𝔊_K, OA2:365–475; AP1 Lemma 4′, AP1:698–712; M2:521–529). (b) dual: complete reads, reachable laws
  confined to `W ⊊ ℝ^U` (OA2:280–299, :771–773).
- **Variant (ii) effect class (made explicit here; N4).** (V-ii-U): effects are post-processings of
  the final present `V` only (the literal reading of OA2:107–108 with "held = present `V`"), used
  here as a contrast class. (V-ii-H): in addition, heralded composites `e∘π` (herald at earlier
  ticks, then read) are available subnormalized effects, as Lemma 1's proof uses (OA2:226).
- **Herald typing (open interface premise; N4.1).** OA-1 types a herald event as "still held at use
  time" (N1-K, OA1:127) and complete records as every outcome, herald and failure held in `V` at the
  end (N4, OA1:131). OA-2 conditions on the value of a stated `V` cell at a stated tick (OA2:800–801);
  "ensemble conditioning" is this report's reading of that wording, not OA-2's term. Which typing E3
  uses is not fixed by either source.

### 1.1 `G_SM`: definition and standing

- **Definition [P].** Ring of `L ≥ 4` sites, alphabet `ℤ/q`; `R(i, x) = i+2` if `x_{i+1} = 0`, else
  `i+1`; `L(i) = i−1` fixed; `x_i(t+1) = x_{L(i)}(t) + x_{R(i,x(t))}(t) − x_i(t−1) mod q` (SM:112).
  Bijective by explicit inverse (SM:106, :112).
- **At `q = 2` [R, hand-checked here].** `f_i(u) = u_{i−1} ⊕ (u_{i+1} ∨ u_{i+2})`, `F(u, v) = (f(u) ⊕ v, u)`
  (M2:157–164). Check: if `u_{i+1} = 1` the selected value is that 1, else `u_{i+2}`; this is
  `u_{i+1} ∨ u_{i+2}`. At `q = 2` the memory sign is immaterial (M2:167–168).
- **Status.** The state-dependent-geometry principle `s(t+1) = φ_{s(t)}(s(t))` is a stated
  hypothesis/principle, distinct from A6 (SM:104). The ring is SM's example of it, "not derived or
  selected by OI" (M2:199–209); its standing is an independently motivated proposal (M2:43–46). Any
  use as OI's rule is a Layer-0 revision under §A.29 (OA2:660–661).
- **Axioms (M2:184–193) [R].** A2, A3 (reach 2), A4 (center-free, translation) kept. **A5 broken**
  by the term `u_{i+1}u_{i+2}`. **Non-reciprocal for `L ≥ 5`**: `i` can read `i+2`, while `i+2`
  reads `i+1` and `i+3` or `i+4`; at `L = 4`, `i + 4 = i` (M2:191). Lemma Q's argument does not
  apply.
- **CP status relative to R1 [R].** Joint-CP failure under R1 holds for every coupling rule
  (covariance group `A_4 ≀ S_n`, not Clifford) and does not single out `G_SM` (M2:455–471, :761).
  P★'s C-CP failure is R1-relative. OA-2 treats these as G4-type: they count for nothing either way
  in E3 (OA2:671–672). Nothing below uses R1.
- **The feature used below.** For every state, `f_i` contains `u_{i−1}` with coefficient 1, ungated:
  `G_SM` is permutive in its extreme left argument (for the property's name in the corpus: L3b
  `preregistration.md`:65–66, :99–109; `result.md`:51–53). SM:112's own remark ("the update adds the
  hidden value `x_{L−1}(t)`") is the same edge seen from the visible side.

***

## 2. Depth-first chain

### N1. minacc-1's gate cancellation in `G_SM` (first item: rule in or out)

**N1.1 Source [R].** Under `G_σ = OR(u_{i−1}, u_{i−2}) ⊕ OR(u_{i+1}, u_{i+2})` (MAR:36–40), a reader
whose own `u` is unknown has no backaction when the far cell of the gated pair is 1, because
`OR(α, 1) = 1`; protocol `E_A` determines `u + v` (`Q* = 1`) of an active cell in every branch
(MAR:201–256). Resources: P2 half-known ready cells, one known-1 cell (H-PREP), P1 registration with
archive-swap refills (MAR:297–318; MA:294–326, "No cell with both slots known is supplied").

**N1.2 Transfer to `G_SM` [W; RW].** In `G_SM` only the right side is gated, so the mirror image
works with the reader on the right. Sites are relative to target 0, with `(u_0, v_0) = (x, y)`:

- t = 0 (Π_A-type supplies): cell −1 known `u = 0` (P2); reader cell 1 known `v = 0`, unknown
  `u = α` (P2); gate cell 2 known `u = 1` (H-PREP); cell 3 arbitrary.
- Tick 1: `u_1(1) = v_1 ⊕ u_0 ⊕ OR(u_2, u_3) = x ⊕ 1`, so register `r_1 = x ⊕ 1`.
  `u_0(1) = v_0 ⊕ u_{−1} ⊕ OR(u_1, u_2) = y ⊕ OR(α, 1) = y ⊕ 1`, and `v_0(1) = x`. The reader's unknown
  `α` does not reach cell 0.
- Refill cells −1, 1, 2 to the `t = 0` specification (fresh `α₂`).
- Tick 2: `u_1(2) = 0 ⊕ (y ⊕ 1) ⊕ OR(1, ·) = y`, so register `r_2 = y`.
  `u_0(2) = x ⊕ 0 ⊕ OR(α₂, 1) = x ⊕ 1`, and `v_0(2) = y ⊕ 1`.
- **Exposure.** Cell 0 is active, unregistered and sharp at `t = 2`, `(u, v) = (r_1, r_2 ⊕ 1)`. Its
  `u + v` (`Q* = 1`) is determined in every branch. This is minacc-1's (B-D), now for `G_SM`. The
  schedule needs only `L ≥ 4`: at `L = 4` site 3 is site −1, and `OR(1, ·)` still absorbs it
  (Rv3:52–54).
- **Bearing on M2's open item.** M2:857–859 records for `G_SM`: "Whether the protection fails under
  P1 and P2 is open." `E_A^SM` answers it at [W] level: the protection fails, under P1, P2 and
  H-PREP's known-1 supply.
- **Mechanism-off control (hand).** With `R ≡ i+1` (class N; M2:195–197) the same schedule gives
  `u_0(1) = y ⊕ α`, masked: protection returns, as required.
- **Observation (the `R ≡ i+2` limit) [W; RW].** In the other linear limit, `f_i = u_{i−1} ⊕ u_{i+2}`
  (non-symmetric). Cell 1 does not enter `f_0`, so there is no kick, and this limit does not restore
  protection. The supply changes: the reader's update is `f_1 = u_0 ⊕ u_3`, so with cell 3 arbitrary
  the register is `x ⊕ u_3`, not `x ⊕ 1`. Exposure needs cell 3 supplied known (a P2 cell). With
  cell 2 known `u = c` and cell 3 known `u = 0`, both refilled:
  - tick 1: `r_1 = u_1(1) = x`; `u_0(1) = y ⊕ c`, `v_0(1) = x`;
  - tick 2: `r_2 = u_1(2) = y ⊕ c`; `u_0(2) = x ⊕ c`, `v_0(2) = y ⊕ c`;
  - so cell 0 is sharp at `t = 2`, `(u, v) = (r_1 ⊕ c, r_2)`.

  What removes the backaction is a coupling that is one-way at that tick. Gate cancellation is one
  way to get it; the non-reciprocity of M2:191 is another. This agrees with "a gate whose influence
  is one-way" (MAR:93–95).

**N1.3 What this means in E3 [W].** OA-2's E3 observer holds its own cells, so their contents are
held records, known to every effect. Hence:

- A `V`-cell reader has no unknown slot. Its kick is a known translation, and no gate cancellation
  is needed for it.
- OA-2 lists the premises of the class-N single-cell result as "Lemma Q(iii) under P1–P2"
  (OA2:632–633). Lemma Q's reader-kick mechanism needs readers with an unknown slot (P2, with P1). A
  held E3 reader has none.
- Whether hidden-cell noise yields a native restriction for observers below Lemma OBS's block size
  is open (N5). In E3 an unknown disturbance can still come from hidden cells that neighbour the
  carrier, under the stated μ. For a one-cell class-N observer, (★) below yields only
  `x_{a−1} + x_{a+1}`.

**Verdict N1.**

- Gate cancellation is **ruled in as a refuter**: it transfers to `G_SM` and defeats Lemma Q's
  protection under P1, P2 and H-PREP's known-1 supply, which settles the item M2:857–859 records as
  open. It is **ruled out as a source** of shape (a): it supplies access, not restriction.
- Measure-free: determination is a support statement for any full-support prior on the unknown
  slots (MAR:254–255).
- Classification: N1.2 **ELABORATING** (a direct transfer of minacc-1's `E_A` that settles a recorded
  open item); N1.3 **CONFIRMING** of OA2:632–633.

### N2. Lemma OBS: a three-site held block observes the whole ring

**Lemma OBS [W; RW].** Take SM's rule (SM:112) at any `q ≥ 2` and either memory sign, on a ring of
`L ≥ 4` sites. Let `V ⊇ {a, a+1, a+2}` with H-AR. Then:

- **(i)** The history of the three `u`-slots over `[0, T]`, together with `v_a(0)`, determines the
  full configuration at time `L − 3` whenever `T ≥ 2(L−3)`. By bijectivity it therefore determines
  the full configuration at every time.
- **(ii)** Without `v_a(0)`, the `u`-history over `[1, T_M]` determines the configuration at time 0
  whenever `T_M ≥ 2(L−2)`.
- **(iii)** Both hold for every setting (every content of `V`) and pointwise in the configuration, so
  they are measure-free.

*Proof.* Write `x_j(t)` for the `u`-slot; then `v_j(t) = x_j(t−1)`. The update at site `j`,

  `x_j(t+1) = x_{j−1}(t) + x_{R(j, x(t))}(t) ∓ x_j(t−1)`,

is solved for the left neighbour:

  `x_{j−1}(t) = x_j(t+1) − x_{R(j, x(t))}(t) ± x_j(t−1)`.   (★)

`R(j, x(t))` and `x_R(t)` need only `x_{j+1}(t)` and `x_{j+2}(t)`. For `j = a`, all three of
`x_{a+1}, x_{a+2}` and the history of `x_a` are held. Let `D_k` be the set of times at which
`x_{a−k}` is determined, with `D_0 = D_{−1} = D_{−2} = [0, T]`. For `t = 0`, (★) at `j = a` uses
`v_a(0)`.

- `k = 1`: `D_1 = [0, T−1]`.
- `k ≥ 2`: (★) at `j = a−k+1` needs `x_{a−k+1}` at `t ± 1` and `x_{a−k+2}`, `x_{a−k+3}` at `t`. Those were
  determined at depths `k−1`, `k−2`, `k−3`, or are held. By induction `D_k ⊇ [k−1, T−k]`.
- Site `a−k`'s pair `(x(t*), x(t*−1))` is determined at `t* ∈ [k, T−k]`.
- The hidden sites are `a−1, …, a−(L−3)` (going round the ring to `a+3`). They are all determined
  at the common time `t* = L−3` when `T ≥ 2(L−3)`. The held sites are known at `t*` directly.

For (ii), start (★) at `t ≥ 2`: `D_k = [k+1, T_M−k]`, pairs are known on `[k+2, T_M−k]`, and the
common time exists when `T_M ≥ 2(L−2)`.

No step uses a gate value, a setting, a known ready cell or a measure. Each step is the
left-edge permutivity of (★). ∎

- **Generality (corrected per Rv3:105–111).** The argument needs the update to be permutive in its
  **extreme** left argument: with left reach `l` and right reach `r`, (★) at `j` is solved for
  `x_{j−l}` given `x_{j−l+1}, …, x_{j+r}` and the history of `x_j`, so the held block must have width
  `l + r`. With `l = 1` this is `r + 1`. The mirror statement holds for a permutive extreme right
  argument. `G_SM` (`l = 1`, `r = 2`) needs a 3-block; class N (`l = r = 1`) a 2-block. `G_σ` is
  permutive in no argument (MAR:36–40) and is **not** covered.
- **Hand checks.** `L = 4`: the hidden site is `a+3 = a−1`; (★) at `j = a` gives `x_{a−1}(t)` for
  `t ∈ [0, T−1]`, so its pair is known at `t* = 1` once `T ≥ 2 = 2(L−3)` ✓. `L = 5`: common time 2 at
  `T = 4` ✓ (Rv3:99).
- **Prior art [L].** For permutive cellular automata, a vertical strip of width equal to the radius
  determines the space-time diagram on the permutive side (Hedlund 1969, *Math. Systems Theory* 3;
  and the expansive-CA literature). Lemma OBS is that argument for SM's second-order ring rule.
- **Prior art in the corpus.** For class N (affine), the conclusion is an instance of obsmu
  Proposition C's coset structure (obsmu:546–578): the history homomorphism determines the
  configuration exactly when its kernel is trivial. obsmu does not compute that kernel for the ring.
  No statement of the lemma was found in SM:112's visible-sector remark, L3b, obsmu, PI, MECH-1,
  minacc-1 or the TUNE-1 drafts (§6).
- **Bearing on shape (a).** For any carrier, every functional pair is jointly read by the single
  procedure "wait `2(L−2)`, read the history" (under MP-0b); under V-ii-H the joint statistics are
  available, since the joint indicators lie in the effect cone generated by the heralded composites
  over that history. The gbit's "joint read unavailable under every protocol" (§1; OA2:767–770)
  therefore fails under MP-0b. Under V-ii-H the gbit's restriction fails at the level of joint
  statistics, which is what it concerns at the GPT level (N4.4); a single-run joint effect may still
  be absent.
- **Bearing on N-a.** `G_SM`'s setting-gated reads at the right end of `V` (OA2:665: N-a met) are
  real but irrelevant here: completeness comes from the ungated edge, whatever the settings.

**Verdict N2: NO for shape (a)**, for `G_SM`, class N and SM's rule at every `q`. Class: H-AR observer
with three (class N: two) consecutive held sites; MP-0b history, or heralded composites (V-ii-H);
horizon at least `2(L−2)` after handoff; finite ring. Measure-free. **NEW** at corpus level (§5),
with the [L] prior art above.

### N3. Theorem S: the dual shape is closed for the same observers

**Theorem S [W; proof step RW under μ-G].** Assume:

- Lemma OBS's observer: H-AR, three consecutive held sites, finite ring of `L ≥ 4` sites;
- **MP-0b or (V-ii-H)**, for both the preparation herald and the effect below; under held-at-use
  herald typing (§1), (V-ii-H) is itself retention-type (N4.1);
- heralds (OA2:96–97, :800–801) and C-PM;
- a measurement stage of at least `2(L−2)` after every handoff;
- **(PT)**: every configuration in `U` lies in the support, at handoff, of some preparation whose
  stage is at least `2(L−3)`.

(PT) holds in two cases. (PT-a) Under any initial law (μ-G, μ-O, μ-R, MP-0a declared cells, initial
settings) when every preparation of the fragment has stage at least `2(L−3)`. (PT-b) For preparations
of any stage, for initial laws with `F`-invariant support (e.g. μ-G, support `S`, and μ-O, support an
orbit, OA1:97–98), when a preparation of stage at least `2(L−3)` from them fits the horizon, i.e.
horizon at least `4L − 10`.

Then the prepare–measure fragment of `G_SM` (likewise class N with a held 2-block, where the stage
bounds become `2(L−2)` and `2(L−1)`, total `4L − 6`; and SM's rule at any `q`) is simplex-embeddable,
and `E` is a simplex. G1 and G3 fail.

*Proof.*

1. **Point preparations of every configuration in `U`.** Let `ω ∈ U`. By (PT), `ω` lies in the support
   of the law at handoff `t_h ≥ 2(L−3)` of some preparation `π`. Compose `π` with a herald on the
   full held history over `[0, t_h]`, including `V(0)` (Proc is closed under composition, OA2:98).
   - By Lemma OBS(i) and bijectivity, the herald value determines `ω(t_h)`, pointwise and for every
     setting.
   - The value belonging to `ω` has subnormalized weight `ν(F^{−t_h} ω)`, times any external C-PM coin
     weight, `> 0` (after renormalizing on `π`'s herald, divided by `P(π's herald)`), for `ν` the initial
     law (`S` finite). Only positivity is used. Under μ-G, `ν(F^{−t_h} ω) = |S|^{−1} = q^{−2L}`, which is OA-1 D3
     with equality (OA1:152–156).
   - So every `δ_ω`, `ω ∈ U`, is a reachable preparation, and `W = ℝ^U`.
2. **Complete effects.** By Lemma OBS(ii), the post-handoff `u`-history over
   `[t_h+1, t_h+2(L−2)]` determines `ω(t_h)`. It uses no label cell: no `V(t_h)` entry and no
   `v`-slot copy of it. Under MP-0b every function on `S` is an available effect. Under (V-ii-H) the
   singleton indicators `[ω(t_h) = ω]` are available (heralds at each post-handoff tick, then a final
   read), so the span of the available effects, as functions on `U`, is `ℝ^U`.
   - The read also reveals the label. C-PM′ therefore fails physically, which only refines the
     equivalences.
3. **The model.** Take the ontic state to be the configuration at handoff, each preparation to its
   law, and each effect to its response. Responses depend on `ω(t_h)` only, since `F` is
   deterministic and autonomous.
   - Prepare–measure statistics are reproduced.
   - Proposition B(i): `R` is injective on `W` (step 2), so the model is preparation-noncontextual.
   - Proposition B(ii) (⇐): `W = ℝ^U` (step 1) makes `ρ` injective, so the model is
     measurement-noncontextual.
   - These two give a simplex embedding of the prepare–measure fragment, as in Theorem E(b) step 5
     (OA2:519–525). Proposition B(iv) is not used: it needs (iii) (OA2:248–249), and transformation
     noncontextuality is not claimed.
   - `E = R(Δ(U))` with `R` injective is a simplex.
   - Shorter measurement procedures are responses on `U` and are covered. Shorter preparations are
     covered exactly when (PT) holds. ∎

- **Measure (corrected per Rv3:159–170; §A.31 check below).** The proof uses the initial law only
  through the supports at handoff, in step 1. It uses no invariance and no (xiv): Theorem S has no
  measurement setting cells, and every response is a function of the configuration at handoff.
  Proposition B holds for every law (OA2:730). r1's reasons for excluding μ-O, μ-R and MP-0a ("full
  support", "(xiv) may fail", "not invariant") are not used by the proof and are deleted.
- **§A.31 check of the generalization (favourable to the negative, so pressed).**
  - *Node 1: does step 1 need full support?* No. It needs `δ_ω` for every `ω ∈ U`, and full support is
    one way to get it. ✓
  - *Node 2: does heralding on the history give `δ_ω` for every `ω` in a preparation's support?*
    Yes, for that preparation's handoff, when its stage is at least `2(L−3)`. ✓
  - *Node 3: is `U` the union of those supports only?* No. `U` collects the supports of **all**
    reachable laws, including preparations shorter than `2(L−3)`. Under μ-G each such support lies
    in `S`, which long preparations cover. Under a non-invariant initial law (MP-0a declared cells,
    or μ-R where its support is not invariant), a short preparation's support `F^t(supp ν)` need not
    be covered. This is the condition (PT), which the review's derivation (Rv3:164–165) leaves
    implicit (Disagreements, D1).
  - *Node 4: what fails without (PT)?* With complete effects, `ρ` is injective iff `W = ℝ^U`. If
    `W ⊊ ℝ^U`, Proposition B(ii) (⇒) (OA2:257–275) makes the configuration model
    measurement-contextual, so this proof route fails. Embeddability then rests on another model, and
    is not decided here (OA2:276–278). Whether `W ⊊ ℝ^U` actually occurs for a given initial law with
    short preparations is not decided.
  - *Verdict:* generalized to every initial law under (PT); μ-G and μ-O satisfy (PT) for preparations
    of any stage.
- **Relation to M2 Theorem NC (ELABORATING).** NC needed spanning certification, and at `q = 2` a
  `Y` read not exhibited natively (M2:485–537). In E3 with a held 3-block, spanning on the
  configuration space is supplied natively, by observability plus heralds. This is a different
  object (configuration E3, not R1-encoded cells under P1/P2). It does not decide M2's A6 at the
  native `Z`/`X` level.
- **Classical control.** 𝔊_K passes G3 because its conveyors keep labels and old contents out of
  reach for the horizon, with no return path (OA2:404–426). In `G_SM`, the ungated left edge is a
  native return path of exactly the kind 𝔊_K is designed to lack. The negative is consistent with
  the control.
- **Scope, skeptically.** The horizon `≈ 4L` is of the order of the ring size. Physically relevant
  horizons `T ≪ L` are **not** covered. On a line, or for `T < 2(L−2)`, hidden sites at depth in
  `(T/2, T]` still feed the records through the left chain but are not determined, and the right-hand
  hidden region is read only through OR terms. The question stays open there.

**Verdict N3: NO for shape (b) (and (a))** within Theorem S's class. Scoped to that class; not an
impossibility for `G_SM`. **ELABORATING**: a corollary of Lemma OBS with OA-1 D3 and Proposition B;
the content is Lemma OBS.

### N4. Theorem E(b) without (H4): the variant-(ii) effect class decides AW-OA2-4

**N4.1 Where the defect is.** OA-2's own text does not exclude heralded composites:

- Proc contains heralds (OA2:96–97);
- Proc is closed under composition (OA2:98);
- OA2:522–523 folds every procedure into a measurement "procedure, then read";
- Lemma 1 (OA2:224–227) uses `e∘π`.

The statement inconsistent with these is the gap paragraph, "only the marginals are available
statistics" (OA2:548–551), taken from Rv2:115–122 and accepted in Rv2b:105–107. (V-ii-U) is the
literal reading of OA2:107–108 and is used here as a contrast class.

- **Finding.** OA-2 r3's gap paragraph, and both OA-2 reviews, assumed an effect class under which
  OA-2's own Lemma 1 is false (N4.2). Under the class Lemma 1 presupposes, (H4) is redundant for E(b)
  (N4.3).
- **Nearest prior art.** Rv2:134–137 flagged a closure-versus-timing tension: if durations are part
  of Proc, reading at different times is native, and otherwise Lemma 1 loses its closure.
- **Herald typing (the open premise).**
  - If E3 heralds carry OA-1's typing (held at use time, OA1:127, :131), then under "held = present
    `V`" a multi-tick herald needs an MP-0b-type retention convention (OA1:554–555). This applies
    equally to N4.2's *preparations* (`V(1)`, `V(2)` are not held at `t_h`), to N4.3's *effects* and to
    Theorem S's herald and effect.
  - If heralds are ensemble conditionings (this report's reading of OA2:800–801; §1), no retention is
    needed and (V-ii-H) is the class OA-2's Lemma 1 uses (OA2:226).

**N4.2 Under (V-ii-U): an exact gbit for a shift [W; RW].**

- **Setup.**
  - `Φ` = cyclic shift on 3 cells, `ω(t+1)_i = ω(t)_{i−1}`. It is linear, an additive bijection,
    so (H1) holds as stated in OA2:483.
  - `V` = cell 0 (H-AR). μ-G. No settings, so (xiv) holds trivially; (H3) holds.
  - At `t = 0`: cell 0 holds `p`, cell 2 holds `x`, cell 1 holds `y`. `V` holds `x` at `t ≡ 1`,
    `y` at `t ≡ 2` and `p` at `t ≡ 0 (mod 3)`.
- **Preparations.** Herald `V(1) = a` and `V(2) = b`, with handoff at `t_h = 3`. The configuration
  returns to its initial form, with `(x, y) = (a, b)` sharp. These are four point preparations
  `[ab]`, each with probability ¼. Coin mixtures are taken under C-PM for the coin (as OA2:435–438).
  The herald cells are past `V` contents, so C-PM is met. Under held-at-use herald typing these
  preparations already need retention (N4.1).
- **Effects.** Under (V-ii-U), an effect is a function of `V(t_h + τ′) ∈ {p, x, y}`: one variable at a
  time.
  - `A = ½([00]+[11])` and `B = ½([01]+[10])` have equal `p` and uniform `x`- and `y`-marginals. So
    `A ∼ B`.
  - `X` (`τ′ = 1`) and `Y` (`τ′ = 2`) are sharp on `[ab]`.
- **Contradiction.** OA-2 Claim 2's argument applies verbatim (OA2:427–442): the four supports are
  disjoint, and `½(μ₀₀+μ₁₁) = ½(μ₀₁+μ₁₀)` is impossible. So the fragment is
  preparation-contextual, and G3 passes.
- **Lemma 1 fails here.**
  - Let `π` = herald `V(t_h+1) = 0`.
  - Then `π(A) = [00]` and `π(B) = [01]`, and reading `V(t_h+2)` gives 0 against 1.
  - So `A ∼ B` but `π(A) ≁ π(B)`.
- **Formal statement of the exit.** The exit is the asymmetric class: multi-tick heralds for
  preparations, but not for effects.
- **Pressure test (favourable branch, maximum skepticism).**
  - Nothing in `Φ` supplies the restriction. It comes from a one-cell memory and from heralds that
    condition at several ticks while effects cannot.
  - The artefact needs dynamics that cycle distinct contents through a one-cell `V`; identity
    dynamics on a static `V` do not produce it. It is present already for trivial dynamics (a shift).
  - So the access restriction is **imposed by convention, not native**. G3 here does not
    discriminate even trivial dynamics, which fails the classical control more severely than 𝔊_K.
    Non-import is trivially met.
  - **Would establish:** that the asymmetric variant-(ii) class makes G3 non-discriminating.
  - **Would not establish:** anything about any OI rule, admissibility (§A.29), non-import's bearing
    on OI, unbounded horizons, or a qubit-type fragment.
  - **Prior art:** OA-1 D8(c)'s cyclic permutation `(y, r, h) ↦ (h, y, r)` (OA1:216–223), and the
    ingredient anticipated at Rv2:124–132. The missing piece there ("a counterexample that also
    meets C-PM", OA2:555–556; Rv2:131–132) is supplied here, *for the asymmetric class only*.

**N4.3 Under (V-ii-H): Theorem E(b) with (H4) replaced by the Lemma 1 effect class [W; RW].** Assume
(H1), H-AR, (H3), (xiv), C-PM and **(SP)**, where (SP) is read for the formal joint record
`Z = (Z_τ)_{τ ≤ T}`, which is never held at once.

1. **Records.** By Theorem E(a) (OA2:509–511), `Z_τ = Z₀^τ(ω) + h_τ(c)`, measure-free.
2. **Effects.** Each available effect is either a single-tick read `f(Z_τ)` or a heralded composite
   `Π_i [Z_{τ_i} = r_i] · f(Z_τ)`. Both are functions of `λ = Z₀` after translation by `h(c)`.
3. **Model.** `ι(s)` = law of `Z₀` under `s`; responses as in step 2. It reproduces every statistic.
4. **Preparation NC.** Singleton indicators `[Z = λ + h(c)]` are available, as heralds at every tick
   followed by a final read. So two equivalent preparations have equal laws of `Z₀`.
5. **Measurement NC.** By Proposition B(ii) (⇐) on the `Z₀` model with (SP) (OA2:519–521).
6. **Conclusion.** The model is a simplex embedding of the prepare–measure fragment. Transformation
   noncontextuality is not claimed (as OA2:524–525). ∎

(H4) is replaced by the effect class Lemma 1 presupposes. Under held-at-use herald typing that class
is itself retention-type, so "without (H4)" does not mean "without any retention convention".

**N4.4 Corollary (the cones coincide) [W; RW].** Under (V-ii-H):

- the effect cone is the cone generated by the joint indicators `[Z = z]`, which is variant (i)'s
  cone. The effect *sets* differ: a cross-tick parity indicator such as `[00]+[11]` is in the cone
  but is not one run's outcome without memory;
- preparations heralded on a history are the same as sequential single-tick heralds;
- simplex-embeddability is a condition on the cones and the unit (OA-2's G3 definition, OA2:150
  [L: Schmid et al. 2021]), so variants (i) and (ii) give the same verdict.

**Verdict N4.**

- Under (V-ii-H), which Lemma 1 requires, **AW-OA2-4 is not an exit for the affine class**:
  E(b) holds with (H4) replaced by that effect class, under (H1), H-AR, (H3), (xiv) and (SP). The
  measure row is as OA2:733: (xiv) holds for disjoint cells under μ-G and may fail under μ-O and μ-R.
  With heralds typed as held at use time, the class is retention-type (N4.1).
- Under (V-ii-U), an exit exists, but it is convention-imposed, present already for trivial dynamics
  (a shift), and OA-2's Lemma 1 fails there. It does not count.
- The affine class at E3 without (SP) stays open (OA2:762).
- **NEW**: a hidden assumption in OA-2 r3's gap paragraph and both OA-2 reviews (§5), with Rv2:134–137
  as nearest prior art.

### N5. What remains for `G_SM`: small observers and short horizons

**Candidate mechanism (not decided) [W].** With `|V| ≤ 2`, (★) leaves residuals. For
`V = {a, a+1}` at `q = 2`, site `a+1`'s update gives `o(t) = OR(u_{a+2}(t), u_{a+3}(t))`. Site `a`'s
update then determines `u_{a−1}(t)` in three cases out of four:

- when `u_{a+1}(t) = 1`;
- when `u_{a+1}(t) = 0` and `o(t) = 0`;
- in the remaining case (`u_{a+1}(t) = 0`, `o(t) = 1`) only `u_{a−1}(t) ⊕ u_{a+2}(t)` is
  determined.

These residuals are data-dependent and gated by held contents. Separately, the left-end setting
`u_a` gates the hidden–hidden edge `{a−2 ← a−1}`, since `OR(u_{a−1}, u_a)` enters `f_{a−2}`. That is
a genuinely non-translational setting action on `H`.

**What a native gbit would need.** In E3 every influence of `V` on `H` is a function of held data,
so it is a known translation. An unknown disturbance on a carrier can come only from hidden cells
(μ-dependent). A gbit would therefore need held settings to route hidden noise into a hidden carrier
selectively, against the residuals above.

**Verdict N5.** Not derivable by hand without enumerating protocols, which is outside this unit's
authorization. **OPEN.**

***

## 3. Candidates and controls

| Candidate | Passes G3 (prepare–measure)? | Access restriction native? | Classical control (𝔊_K) | Non-import | Verdict |
|---|---|---|---|---|---|
| C1. Lemma-Q / P2 read restriction transplanted into `G_SM` as gbit source | No: class N's native `Z`/`X` fragment is NC (OA2:627–656); in `G_SM`, gate cancellation defeats it (N1.2) | Lemma Q's reader-kick mechanism needs P2 (MA:297–300); a held E3 reader has no unknown slot | — | met | Ruled out |
| C2. Gate-cancellation reads (minacc-1 mechanism, mirrored) | No: it adds access | Native (rule), but access, not restriction | — | met | Refuter, ruled in |
| C3. One-site or any carrier, observer ⊇ 3 consecutive held sites, MP-0b or (V-ii-H) | No (N2, N3) | Rule supplies the opposite: an ungated return path | Consistent: 𝔊_K lacks a return path | met | NO in class of Theorem S |
| C4. Dual shape via restricted preparations, same observer | No: heralds reach every `δ_ω`, `ω ∈ U`, under (PT) (N3) | — | — | met | NO in class of Theorem S |
| C5. Small observers (`|V| ≤ 2`), setting-gated OR reads; short horizons | Not decided | Possible (non-translational gating, N5) | Not run | met by construction (no quantum structure in the definitions) | OPEN |
| C6. Memory gbit under (V-ii-U) (3-cell shift) | **Yes** | **No**: imposed by the asymmetric herald/effect convention; present already for trivial dynamics (a shift) | Fails to discriminate (trivial dynamics pass) | met | Does not count |
| C7. Affine class, non-nested reads, (V-ii-H) | No, under (SP), (xiv) (N4.3) | — | — | met | NO; AW-OA2-4 closed as an exit (retention-type under held-at-use herald typing) |

**Controls applied in the derivations.**

- *CC-OFF for N1.2.* `R ≡ i+1` must mask: it does (`y ⊕ α`). `R ≡ i+2` does not restore protection,
  with cell 3 supplied known (a P2 cell), as reported.
- *Must-break for Lemma OBS.* `G_σ` has no permutive argument. (★) cannot be solved at `j = a`, since
  `OR(u_{a−1}, u_{a−2})` is not invertible in `u_{a−1}`. So the lemma correctly does not cover it.
  MAR's exposure under `G_σ` uses refills and P2, not observability.
- *Positive control for N4.2.* OA-2's 𝔊_K Claim 2 argument (OA2:427–442) is used verbatim. The shift
  example is checked tick by tick above.
- *Non-vacuity of N4.2.* Two operationally distinct classes exist (`[00]` vs `[11]`), and two
  non-equivalent effects (`X`, `Y`). This is the guard of OA2:809–811.
- *Target-neutrality.* Every object uses only laws on `S`, `[0, 1]` responses and convex structure.
  R1, CP and Hilbert space enter nowhere.

***

## 4. Conclusion

**OPEN, narrowed**, with the following established by hand at [W] level (re-derived by the reviewer
[RW] where marked; r2's changes rechecked in `RECHECK-OA-3-r2.md`, r3's E1, E2 and m1–m3 delta-reviewed in `DELTA-REVIEW-OA-3-r3.md`, its R1–R4/O edits unreviewed):

1. **Shape (a), gbit:** NO for `G_SM` with H-AR observers holding three consecutive sites, MP-0b
   history or heralded composites (V-ii-H), horizon at least `2(L−2)`, finite ring. Measure-free
   (N2).
2. **Shape (b), dual:** NO for the same class, with a measurement stage of at least `2(L−2)` and
   (PT): for initial laws with `F`-invariant support (e.g. μ-G, μ-O) with horizon at least `4L − 10`,
   or under any initial law when every preparation has stage at least `2(L−3)` (N3).
3. **Gate cancellation:** transfers to `G_SM`, is a refuter of read restriction, and settles M2's
   open item (M2:857–859) under P1, P2 and H-PREP (N1).
4. **Theorem E(b) for the affine class:** (H4) is replaceable by the effect class Lemma 1 presupposes
   (V-ii-H), under (H1), H-AR, (H3), (xiv) and (SP); that class is retention-type under held-at-use
   herald typing. Under (V-ii-U) the gbit pattern appears for a 3-cell shift and does not count (N4).

**Precise remaining question.** The open regime is the complement of Theorem S's class, a union. For
`G_SM`, under C-PM, is the closure-defined prepare–measure fragment simplex-embeddable in any of:

- an H-AR observer with no three consecutive held sites (for example `V = {0, 1}`), at any horizon;
- a three-block observer with `T < 4L − 10`; in particular, for `2(L−2) ≤ T < 4L − 10` shape (a) is
  excluded and shape (b) is open;
- `T ≪ L` with any observer, and infinite windows;
- the (V-ii-U) record class, where Theorem S does not apply as proved;
- an initial law with short preparations outside (PT);
- non-additive observers (AW-OA2-1) and unbounded horizons (AW-OA2-2)?

**Is the preregistered computation still decisive?** It is decisive for that instance (`Z_5`,
`V = {0, 1}`, `T ≤ 4`, OA2:797, :832–833), which lies outside Lemma OBS (`|V| = 2`; `T < 10`). Three
design amendments are proposed for the future preregistration. Each needs owner authorization before
anything runs.

1. **Variant (ii) effect class and herald typing.** State the effect class, and fix the herald
   typing (held at use time, or ensemble conditioning; N4.1). If heralded composites are effects
   (Lemma 1), variant (ii)'s effect cone equals variant (i)'s (N4.4), so drop it or keep it only as a
   pipeline cross-check. If the asymmetric class is kept, add the 3-cell shift with a one-cell `V`
   (or OA-1 D8(c)'s permutation) as a memory-artefact control that must return non-embeddable. A
   non-embeddable variant-(ii) verdict for `N₁` or `G_SM` then carries no rule-specific information
   without a preregistered discriminating criterion. This replaces the "measurement without a
   prediction" reading of OA2:818–819.
2. **Predicted-embeddable `G_SM` control (proof: Theorem S).** `G_SM` on `Z_4` (one hidden site) with
   `V` three consecutive sites, heralds, horizon at least `4L − 10 = 6`. It must return embeddable.
   A class-N analogue with a 2-block has horizon at least `4L − 6`.
   - **Record variant.** (i) MP-0b, or (V-ii-H) if that is implemented; never (V-ii-U), under which
     Theorem S does not apply.
   - **Initial law.** μ-G; MP-0a ready cells as in OA2:797 are also admissible when the
     preregistered preparation list satisfies (PT), for example every preparation of stage at least
     `2(L−3) = 2`.
   - **Handoff.** Every handoff is at `t_h ≤ T − 2(L−2)`, which is `t_h ≤ 2` at horizon `6`, so every
     measurement stage is at least `2(L−2)`. Under MP-0a with (PT-a), every preparation then has stage
     exactly `2`.
   - **Guards.** It carries the non-vacuity guard (OA2:809–811).
   - **Degenerate instance.** At `L = 4` `G_SM`'s edges are reciprocal (M2:191: "At `L = 4`,
     `i + 4 = i`"), so `Z_4` tests the pipeline, not the non-reciprocal regime.
   - **Independence.** It counts as an independent control only once Theorem S has passed review.
     The OA-3 review accepted its proof step under μ-G, subject to F4, and the focused recheck
     accepted the (PT) form; r3's last edits (R1–R4, O1–O3, O5) are unreviewed.
3. **Keep** 𝔊_K (positive), the variant-(ii) single-cell control (OA2:814–817), and the non-vacuity
   guards. The `G_SM` test object stays as preregistered.

***

## 5. Status table

| Item | Status | Support | Initial law |
|---|---|---|---|
| `G_SM` definition, bijectivity, `q = 2` OR form | manuscript / research record, re-checked by hand | [P] SM:112, :106; [R] M2:157–164 | — |
| `G_SM` standing: state-dependent-geometry principle stated as a hypothesis; ring an example | as recorded | [P] SM:104; [R] M2:43–46, :199–209 | — |
| A5 broken; non-reciprocal for `L ≥ 5` (reciprocal at `L = 4`); CP verdicts relative to R1 only | as recorded | [R] M2:184–193, :455–471 | — |
| N1.2 gate-cancellation exposure `E_A^SM` (Π_A-type supplies); settles M2:857–859 under P1, P2, H-PREP | derived here, ELABORATING | [W] + [RW] on [R] MAR:201–256 | any full-support prior (support statement) |
| N1.2 `R ≡ i+2` limit does not restore protection (cell 3 supplied known) | derived here | [W] + [RW] | measure-free |
| N1.3 held E3 readers carry no kick; native restriction below the block size open | CONFIRMING of OA2:632–633; open part [O] | [W] | — |
| Lemma OBS (extreme-left permutivity; block width `l + r`; any `q`, either sign) | derived here; NEW at corpus level | [W] + [RW]; [L] Hedlund 1969; class N an instance of obsmu Proposition C | measure-free |
| Shape (a) excluded for ≥3-block held observers (MP-0b or V-ii-H) | derived here | [W] + [RW] | measure-free |
| Theorem S (simplex fragment; shapes (a), (b) excluded) | derived here; ELABORATING (corollary of Lemma OBS, D3, Proposition B) | [W] + [RW] (μ-G proof step) + OA-2 Proposition B [W/RW] | any, under (PT); μ-G and μ-O satisfy (PT) for every stage; (PT) form accepted in the focused recheck |
| N4.1 OA-2 r3's gap paragraph inconsistent with Lemma 1 | derived here; NEW (hidden-assumption finding) | [W] + [RW]; nearest prior art Rv2:134–137 | — |
| Herald typing (held at use time vs ensemble conditioning) | open interface premise | [O]; OA1:127, :131; OA2:800–801 | — |
| N4.2 memory gbit under (V-ii-U); Lemma 1 fails there | derived here; does not count | [W] + [RW]; prior art OA1:216–223, Rv2:124–132 | μ-G (any full-support law on `(x, y)`) |
| N4.3 Theorem E(b) with (H4) replaced by the V-ii-H effect class | derived here | [W] + [RW] on OA-2 Theorem E(a) [R/W] | as OA2:733 |
| N4.4 effect cones of variants (i) and (ii) coincide under (V-ii-H) | derived here | [W] + [RW]; [L] Schmid et al. 2021 for the cone formulation | as N4.3 |
| `G_SM`, the union in §4 (small observers, short horizons, infinite windows, V-ii-U, initial laws outside (PT)) | open | [O] | — |
| Affine class without (SP) | open | [O] (OA2:762) | — |

**§A.31 classification (one pass; fixed point not reached).** The productivity test is OA-2's
(OA2:866–867).

- **Lemma OBS: NEW**, at corpus level, with the [L] caveat. The argument is the standard
  permutive-CA one (Hedlund 1969); within the corpus it exposes that an ungated permutive edge is a
  native return path, which the OA-2 design and the M-INACC framing did not register. It constrains
  where non-embeddability can occur.
- **N4: NEW.** A hidden assumption in OA-2 r3's gap paragraph and both OA-2 reviews: they assumed an
  effect class under which OA-2's own Lemma 1 is false. Nearest prior art Rv2:134–137. No source
  searched (the OA-1 and OA-2 reports and all five reviews; §6) notes that heralded composites supply
  the joint statistics.
- **Theorem S: ELABORATING**, a corollary of Lemma OBS with OA-1 D3 and Proposition B; scoped
  negative.
- **N1.2: ELABORATING** (settles M2:857–859). **N1.3: CONFIRMING** of OA2:632–633.
- **Tally:** 2 NEW, both [W] with the proof steps [RW]; r2's changes rechecked; r3's E1, E2 and m1–m3 delta-reviewed; its R1–R4/O edits unreviewed.

**Assumption-watch markers.**

- **AW-OA3-1 (permutive extreme edge).** A rule permutive in its extreme left (or right) argument,
  with left reach `l` and right reach `r`, is fully observable from a held block of width `l + r` on
  a finite ring (Lemma OBS's class: H-AR observer holding the block, MP-0b history or V-ii-H effects,
  horizons of about `2L` or more). For observers in that class, on a finite ring at horizons of order
  `L`, M-INACC (M2:832–871) needs no permutive extreme edge on either side. Growing carriers
  (OA1:573–574) and short horizons are untouched. Cross-propagates to M2 §6.2's "what would derive
  it" and to any symmetrized `G(x)` proposal (M1:1023–1028).
- **AW-OA3-2 (heralded composites and herald typing).** Any record-level claim that uses present-`V`
  reads together with heralds must state whether heralded composites are effects, and whether heralds
  are typed as held at use time (OA1:127, :131) or as ensemble conditionings (this report's reading of
  OA2:800–801). Under the
  first typing, multi-tick heralds for preparations and effects alike need MP-0b-type retention. This
  applies to OA-2 Lemma 1 and variant (ii), to "only the marginals are available" (OA2:550–551), to
  Theorem S and to N4.2–N4.3. OA-1 D2 (OA1:141–150) is a single-time statement and is unaffected as
  stated. Its reading as a retention no-go should be checked against this marker.

***

## 6. Reading inventory and §A.19 basis

**At `main` `615cc119`** (cited lines unchanged at `911a5cb6`; Snapshots).

- `papers/SM.md`: heading index; :56; :100–169 (§3.1 whole; :104 principle, :106 bijectivity, :112 the
  explicit construction and its visible-sector remark), read via `sed`/`fold`.
- `papers/Main.md`: :42, :54, :58, :60 (spot reads); :724 item (xiv); grep for `G_SM` and
  "state-dependent".
- `mechanism-2-20261108/DESIGN.md`: :1–330, :360–560, :560–760, :760–880 (r2 re-read :184–210,
  :850–872).
- `minacc-1-20261108/RESULT.md`: :1–420 (r2 re-read :30–64, :86–96, :240–320). `DESIGN.md`: :294–330
  and a grep. Amendments: line counts only, not read.
- `apparatus-1-20261107/DESIGN.md`: :694–730.
- L3b round: grep of `result.md` and `preregistration.md` for permutivity; r2 read
  `preregistration.md`:64–67, :99–110 and `result.md`:50–54.
- `observer-interface-obsmu-20261104/ANALYSIS.md`: :546–580 (Proposition C), read in r2.
- `mechanism-1-20261107/DESIGN.md`: :877–891, :1023–1028, read in r2.
- `git grep` over `verification/programmes/oi-qm/`, `papers/SM.md` and `papers/Main.md` for prior art
  on observability and heralded effects. No prior statement of Lemma OBS or N4 was found; L3b frames
  edge-permutivity as the axis of the masking argument.
- **Checked by the OA-3 reviewer, not re-read by the author** (Rv3:115–118): PI
  (`oi-qm-ext-1/physical-interface.md`) and the TUNE-1 drafts (`drafts/tune-1-20261111/`), for a
  statement of Lemma OBS; none found there.

**At research branch `815d6a8e`.**

- `OA-2-REPORT-r3.md`: whole (r2 re-read :80–160, :220–320, :478–560, :625–680, :725–740, :755–880).
- `REVIEW-OA-2.md`: :60–140 and grep. `REVIEW-OA-2-r2.md`: grep; :88–110 read in r2.
- `OA-1-REPORT-r4.md`: :85–275, :540–575.
- r2: grep of `REVIEW-OA-1.md`, `REVIEW-OA-1-r2.md`, `REVIEW-OA-1-r3.md`, `REVIEW-OA-2.md`,
  `REVIEW-OA-2-r2.md`, `OA-1-REPORT-r4.md` and `OA-2-REPORT-r3.md` for heralded composites, `e∘π` and
  joint statistics. The only hits are OA2:226–227 (Lemma 1), OA2:550 and Rv2:116 (marginals only),
  and Rv2b:94 (native reads closed under `e∘π`), none of which notes that heralded composites supply
  the joint statistics.

**This directory.** `OA-3-REPORT.md` (r1), `REVIEW-OA-3.md` (the review) and `RECHECK-OA-3-r2.md` (the focused recheck of r2).

**Not read.**

- OA-2 r1 and r2; REVIEW-OA-1* beyond the grep above.
- minacc-1 amendments (A1–A3) and DESIGN outside :294–330.
- QA, FB, mathcon1; PI and TUNE-1 (reviewer-checked only); MECH-1 and obsmu outside the lines above.
- AP1 outside :694–730.
- SM outside the lines above.
- The literature [L], including Hedlund 1969.
- #1169 comment c.6833027576 itself (authorization as relayed).

Negative claims are limited to these sources. "No prior statement found" rests on the greps above
and the reviewer's checks.

***

## 7. Limits

- Every [W] item is a hand derivation; the r1 proof steps were re-derived by the reviewer [RW]. None
  is kernel-checked or computed. r2's changes, including (PT), passed the focused recheck; r3's E1, E2 and m1–m3 were
  delta-reviewed; its R1–R4 and O1–O3, O5 edits are unreviewed.
- Theorem S needs:
  - a finite ring;
  - three consecutive held sites, H-AR;
  - MP-0b history, or heralded composites (V-ii-H);
  - (PT): for initial laws with `F`-invariant support (e.g. μ-G, μ-O), a horizon of at least
    `4L − 10`; under any initial law, every preparation of stage at least `2(L−3)`;
  - a measurement stage of at least `2(L−2)`.

  It says nothing about `T ≪ L`, lattice windows, initial laws with short preparations outside (PT),
  (V-ii-U), non-additive observers (AW-OA2-1) or unbounded horizons (AW-OA2-2).
- N4.3 needs (SP) for the formal joint record. N4.2's example satisfies (H1) as OA-2 states it,
  but it is not a gauge-derived OI rule. Its role is to show the convention, not OI physics.
- The herald typing is an open interface premise; under held-at-use typing, N4.2's preparations,
  N4.3's effects and Theorem S all rest on MP-0b-type retention.
- C-PM's treatment of labels that return to `V` in a fixed layout is used as OA-2 uses it. In
  Theorem S the labels are physically readable, which only refines equivalences.
- No manuscript claim is affected. No premise is adopted. Theorem S is not an impossibility result
  for `G_SM`, and N4 does not promote any OI claim. Consistency axis only (§A.23).

***

## Disagreements

- **D1 (F4.3, partial: the generalization is adopted with an explicit extra hypothesis).** Rv3:164–165
  derives `W = ℝ^U` under any μ from "heralding on the full history gives `δ_ω` for every `ω` in the
  support of the law at `T₁`". That covers the supports of preparations of stage at least `2(L−3)`
  only. `U` is the union of the supports of **all** reachable laws (OA2:131–132), and r1's Theorem S
  includes shorter preparations (r1:227–228). Under μ-G (or μ-O) every such support lies in a set
  that long preparations cover, but under a non-invariant initial law, such as MP-0a declared cells,
  a short preparation's support `F^t(supp ν)` need not be covered. If `W ⊊ ℝ^U` then results,
  Proposition B(ii) (⇒) (OA2:257–275) makes the configuration model measurement-contextual, so the
  proof route fails. r2 therefore states the generalization under (PT) (N3) rather than "for every
  μ" unqualified, and conditions amendment 2's MP-0a admissibility on (PT). No other required change
  is disputed.

***

## Change map (review item → where applied in r2)

| Review item | Applied in r2 |
|---|---|
| F1.1 M2:857–859 open item; N1.2 ELABORATING | §0 item 1; N1.2 "Bearing on M2's open item"; Verdict N1; §4 item 3; §5 table row and §A.31 list |
| F1.2 `R ≡ i+2` supply change (cell 3 known; exposure redone) | N1.2 "Observation"; §3 CC-OFF control; §5 row |
| F1 (`L ≥ 4` schedule note) | N1.2 "Exposure" |
| F2 narrowing of "exists only under P2" / "not a property of the rule"; N1.3 CONFIRMING of OA2:632–633 | §0 item 2; N1.3; Verdict N1; §3 row C1; §5 rows and §A.31 list |
| F3.1 extreme-left permutivity, block width `l + r` | §1.1 "feature used"; N2 "Generality"; §3 must-break control; AW-OA3-1 |
| F3.2 Hedlund 1969 under [L]; obsmu Proposition C note; NEW as corpus-level finding | §0 item 3; N2 "Prior art [L]", "Prior art in the corpus"; Verdict N2; §5 row and §A.31 list |
| F3.3 AW-OA3-1 M-INACC sentence scoped | AW-OA3-1 |
| F4.1 "MP-0b or (V-ii-H)" in Theorem S statement, §0 item 4 with finite ring | Theorem S hypotheses; §0 item 4; §4 item 2; §7; proof step 2 adapted to V-ii-H (singleton indicators span `ℝ^U`) |
| F4.2 cite B(i) and B(ii) (⇐) as in OA2:519–525, not B(iv) | Theorem S proof step 3 |
| F4.3 measure scope: checked by hand; generalized under (PT); r1's unused reasons deleted | Theorem S statement (PT, PT-a, PT-b); "Measure" and "§A.31 check" bullets; §0 item 4; §4 item 2; §5 row; §7; Disagreements D1 |
| F4.4 Theorem S → ELABORATING corollary; scope statements kept | Verdict N3; §5 row and §A.31 list; "Scope, skeptically" and §7 kept |
| F5 (cones, not variants, coincide) | N4.4 title and first bullet; §0 item 5; §4 amendment 1; §5 row |
| F5.1 defect located in OA2:548–551 (Rv2:115–122, Rv2b:105–107); (V-ii-U) as contrast class; Rv2:134–137 credit; NEW justified | N4.1; §1 variant (ii) definitions; Verdict N4; §0 item 5; §5 rows and §A.31 list |
| F5.2 herald typing (OA1:127, :131); MP-0b-type retention caveat; asymmetric class as formal statement of N4.2's exit; "without (H4)" not "without retention"; AW-OA3-2 extended | §1 "Herald typing"; N4.1; N4.2 "Preparations" and "Formal statement of the exit"; N4.3 closing paragraph; Verdict N4; Theorem S hypotheses; §0 items 5–6; §3 row C7; §4 amendment 1; AW-OA3-2; §7 |
| F5.3 "present already for trivial dynamics (a shift)" | §0 item 6; N4.2 pressure test; Verdict N4; §3 row C6 |
| F5.4 §0 item 5 conditions and affine-class scope | §0 item 5 |
| F6.1 open regime as a union | §0 item 7; §4 "Precise remaining question"; §5 row |
| F6.2 "decisive for that instance" | §0 item 7; §4 |
| F6.3 amendment 1 tied to herald typing | §4 amendment 1 |
| F6.4 amendment 2: record variant (i) or V-ii-H; non-vacuity guard; `Z_4` reciprocal-edge degeneracy; independence only after review; MP-0a if F4.3 adopted | §4 amendment 2 (MP-0a conditioned on (PT), D1) |
| F6.5 amendment 3 | §4 amendment 3 (unchanged) |
| F7 tally 2 NEW | §5 §A.31 list |
| F7 authorization comment id | Standing block |
| F7 §A.19 basis: obsmu, MECH-1, TUNE-1, PI, L3b, and the review's other checks | §6 |
| Snapshot currency (Rv3:6–9) | Snapshots (re-checked against `911a5cb6`) |

***

## Change map r3 (focused recheck → where applied)

| Recheck item | Applied in r3 |
|---|---|
| E1 herald weight in Theorem S step 1 | N3 proof step 1: subnormalized weight `ν(F^{−t_h} ω)`, renormalized form stated, positivity only |
| E2 handoff bound in amendment 2 | §4 amendment 2, new "Handoff" bullet (`t_h ≤ T − 2(L−2)`, `t_h ≤ 2` at horizon 6) |
| m1 "ensemble conditioning" is this report's reading | §1 herald-typing bullet; N4.1 |
| m2 (PT-b) phrasing; μ-O in §0 item 4 | §0 item 4; (PT) paragraph in N3; §7 |
| m3 joint statistics available under V-ii-H | Lemma OBS "Bearing on shape (a)" |
| Recheck acceptance of D1 and (PT) | Standing note; amendment 2 "Independence" bullet |
| Status phrases and citation forms | Standing note; §4 lead-in; amendment 2; §5 Theorem S row and tally; §7; citation forms and §6 (sibling files in this directory) |

## Change map r3, delta-review edits (`DELTA-REVIEW-OA-3-r3.md` → where applied)

| Delta-review item | Applied |
|---|---|
| R1 C-PM coin weight in E1 | N3 proof step 1 |
| R2 second m1 site | N4.1 herald-typing bullet, second sub-bullet |
| R3 §7 (PT) wording | §7 Theorem S needs |
| R4 gbit quotation and single-run caveat | Lemma OBS "Bearing on shape (a)" |
| O1 §4 item 2 (PT-b) wording | §4 item 2 |
| O2 AW-OA3-2 reading tag | §5 AW-OA3-2 |
| O3 change-map row for status and citation edits | Change map r3 |
| O5 redundant "for the unheralded π" | N3 proof step 1 |
| O4 rewrapping | not applied (layout only) |
| Scope line (outside the gate) | Standing note "Scope" |
| Recheck D1 (μ-G weight after R1 + O5) | N3 proof step 1 |
