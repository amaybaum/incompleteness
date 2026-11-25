# Review of SIGMA12-SCREEN r1

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/SIGMA12-SCREEN-r1.md`,
blob `c32d54c8b8e36602149ab52d2d76200a46392e1b`, read at `95c7e0661e5d5c73528163745bd97415c91abed2`.
The branch head moved to `ea1c1b5d` during the review (a commit adding another unit's review); the
object's blob is the same there.
**Reviewer.** Independent, non-author, read-only. Paper only: every algebraic step and every
counterexample was redone by hand. Git was used only to read files and blob ids. No computation, no
Lean, no edit, no commit, no GitHub action. Issue #866 and the relayed owner comments were not
re-fetched.
**Sources read directly.** MR★ (`.../measurement-record-formation/amendments/MR-star.md`, blob
`45af1678`) at :485–618, :636–681, :853–866; `stage1-log.json`:706; `papers/SM.md` (blob `a5202371`)
at :100–112 and :797–813; native-Y `shared_v12/INTERFACE-CONTRACT.md` (blob `03857785`) at :25–60 and
`native-y-continuation-20261024/CURRENT-HANDOFF.md` (blob `bfcfb83f`) at :36–60; NIS2 SOURCE-SCREEN
§§3, 5; OA-1 and OA-3 STATUS; PC-1 README; VER r2; U4-CALC r1 and r2 with REVIEW-U4-CALC-r2;
S3-U1-r5 §§2.3, 4.3, C-REN; S3-PLAN-r9 §§8.4, 8.6; S3-U4-r1 §4.5.

## Verdict: ACCEPT WITH CHANGES

All five counterexamples and every lemma marked [proved here] check by hand, and the conclusion
"partly done; no negative on recording for route M" stands. The required changes narrow three
generality statements to what the proofs give, add one negative that the SNR-1 accounting leaves out,
remove one unsourced premise, and complete the (c′) blocker list. None of them changes the verdict
or adds anything that would count under SNR-1.

***

## 1. Identification of σ12 (task 1)

- **Three members, correctly read.** MR★:667 names three: native-Y's rule; SM:104–106's coupling graph that varies
  with the state [paraphrase]; "SM §6.5, dynamical links". `stage1-log.json`:706 lists the same
  three. The screen's bracketed paraphrase of the middle item is marked as one. Correct.
- **Y.** INTERFACE-CONTRACT:33–36 gives the rule verbatim as quoted; :59 gives "all six neighbors";
  the torus side `256L+64T+1` with `L = P+262` is at :32–33. Correct.
- **G.** SM:104 states the principle `s(t+1) = φ_{s(t)}(s(t))`; SM:106 the second-order form; SM:112
  the explicit ring, exactly as transcribed (`R(i,x) = i+2` if `x_{i+1} = 0`, else `i+1`; `L(i) = i−1`;
  `L ≥ 4`, `ℤ/q`). Over `ℤ/2`, `x_{R(i,x)} = x_{i+1} ∨ x_{i+2}`, which agrees with NIS2
  SOURCE-SCREEN:42–43. The identification check holds.
- **L.** SM:803 says the link variable "is determined by the matter field … (§3.1)"; SM:809 says the
  map is "under-determined at several enumerable joints"; SM:811 gives the exponential map "as a
  candidate". No update rule for links is stated anywhere in §6.5. "No stated rule" is correct for an
  update rule. See O3: SM:811 does state an explicit candidate *map*, under which the links are a
  function of the matter state.

## 2. Re-derivation (task 2)

| Item | Hand check | Result |
|---|---|---|
| G-1 (L3a) | `φ^{−1}(a,b) = (F(a) − b, a)`; `σφσ(a,b) = (F(a) − b, a)` | holds, any rule (2.1) |
| G-1 (L3b) | first component of `φ²` is `F(y) − x`; `= x` for all `x, y` forces `F ≡ 0`. `H` inverse `(p,q,r) ↦ (r ⊕ pq, p, q)` checked; G-ring `F(δ_{i−1})_i = 1` uses `L ≥ 4` | holds for `F ≢ 0`; see R2 for Y's side |
| G-1 (L3d), G-3 | `φ^{−1} = φ^{N−1}`; `n + m ∈ [m, m+T] ⊂ [1, N−1]` | holds, every bijection |
| G-2 | `(τs)_X = 0`, so the previous slice of `φτs` vanishes on `X`, while that of `τφs` is `F(rδ_j)|_X`; for Y with `i ∼ j`, `H(r) ≠ 0`; for G-ring with `j = i−1`, `F = r` | holds for Y and G-ring; **not** for every rule (2.1) (R1) |
| G-4 | for fixed `s_{A^c}`, `(x_A, y_A) ↦ (y_A, F(y)|_A − x_A)` is a bijection, and its current part has fibres of equal size | holds, every rule (2.1) |
| G-5 | product of uniforms is uniform for any partition of `Σ^c` | holds. It is the partition-independence clause of CALC Prop. 2.8(i), not its "first clause" (O4) |
| G-6, Y | influence of `y_p` at tick `s` lies in the torus ℓ1-ball of radius `s`; the other neighbours of `p_{s+1}` and `u_{s−1}(p_{s+1})` lie outside it when `ℓ > 2s + 2`; `H` bijective gives induction | holds for `t < ℓ/2` |
| G-6, G-ring | reach at tick `s` is `[p − 2s, p + s]`; `u_s(j+1)`, `u_s(j+2)` outside iff `3s + 3 < L`; `u_{s−1}(j)` outside a fortiori; coefficient of `u_s(j−1)` is `1` | holds for `t < L/3` |
| G-7 | counting measure invariant under every bijection; agrees with MR★:642 | holds |
| C-1 | `z = 0`: `P1 ↦ (0,0)`, `P2 ↦ (0, (0,1,0) ⊕ H(0,0,1)) = (0,0)`. `z = (0,1,0)`: `P1 ↦ (0, (1,0,0))`, `P2 ↦ (0, (0,1,0) ⊕ (1,1,1)) = (0, (1,0,1))` | holds; operational I-sel in U1 §4.3's sense |
| C-2 | `u_1(i) = c` at `z = 0`, `= z` otherwise | holds; I-sel |
| C-3, Y | marker effect `H(c ⊕ m) ⊕ H(c)` at `m = (0,1,0)`: `(1,0,0)` at `c = 0`, `(1,0,1)` at `c = (0,0,1)` | holds (clarity, O2) |
| C-3, G-ring | `u_1(i) = m + (c − m)[m = 0]`; `u_1(i+1) = c − x_{i+1}` | holds (wording, O2) |
| C-4 | `φ(0, y) = (y, F(y))`; graph is a coset iff `F` affine. Y: `H(0,1,1) = (1,1,1) ≠ (1,1,0)`. G-ring: `F(a)_i = F(b)_i = F(a+b)_i = 1`, and `1 ≠ 2` in every `ℤ/q` | holds |
| C-5 | All sixteen table entries recomputed from `u_1`, `u_2`; direct substitution agrees. Law given L: `(0,1,1)` 2/8, `(0,1,0)` 1/8, `(0,0,1)` 1/8, `(1,0,1)` 3/8, `(1,1,0)` 1/8. Given R: `(0,1,1)` 2/8, `(0,1,0)` 1/8, `(0,0,0)` 1/8, `(1,1,1)` 2/8, `(1,0,0)` 1/8, `(1,1,0)` 1/8. Overlap carries mass 1/2 under both with equal pointwise masses, so `H(W | Y) = 1/2` | holds: `I = 1/2` bit |
| VER Sup-3 row | Y: `pr_v φ = (y_v, x_v ⊕ H(0)) = σ_X`; G-ring: `(y_i, −x_i)` | holds |

## 3. Scope (task 3)

Each clause failure in §3 is stated per rule, for Y and G-ring only, and the CALC rows are correctly
called "does not apply" or "undetermined" where additivity is used. Three places generalize beyond the
proofs (R1, R2), and several finding summaries drop the rule names (O1). The U1 statements
"unsourced, not disproved" are correct for the marker, given U1 §2.3 and MR★'s GAP caveat on ready
supply, with two exceptions: the J-return form of an undo is excluded at G-6's scope (R3), and one
premise used for the uncomputation is unsourced (R4).

## 4. SNR-1 and blockers (task 4)

Nothing is counted under SNR-1, and the screen says so twice. The global-reversal "not available" is
correctly held back until review, and it rests only on criterion clauses (G1, AD-1(f)), not on
capabilities. The accounting is incomplete in one respect (R3), and the blocker list for (c′) misses
items (R5).

## 5. Repo-text rules (task 5)

None of the repository's banned words, machine-local paths or closing keywords appear in the object. The MR★ quotation avoids the barred word through the marked
paraphrase. Passes.

***

## Required findings

**R1. G-2 is not a statement about every rule (2.1) with `F ≢ 0`.** SG-1 ("(a)–(c) hold for every
rule of form (2.1) with `F ≢ 0`"), §3's [A-inf] ("use only bijectivity, the second-order form (2.1),
finite speed and μ-G's invariance"), AW-σ1 ("Statements that use bijectivity, finite speed or μ-G
(G-1 to G-7) transfer") and blocker 2 ("G-1 to G-5 and G-7 apply to every rule of form (2.1)") all
overstate it. G-2's proof needs a coupling condition: for every proper nonempty `X`, some `i ∈ X`,
`j ∉ X` and `r` with `F(rδ_j)_i ≠ 0`. *Countercontrol:* over `ℤ/2`, take `F` that vanishes on `X` and
is nonzero on a separate component `X^c`. Then `φ = σ_X ⊕ φ|_{X^c}` is itself a block swap and a time
shift (`k = 1`). G-6 also uses more than finite speed: `H` bijective on Y, and the unit coefficient of
the left-neighbour read on G-ring. Fix: state (a) and (c) for every rule (2.1) with `F ≢ 0` ((c) for
every bijection), and (b) under G-2's coupling condition, verified for Y and G-ring. Name the extra
hypotheses of G-6.

**R2. Y "any torus side" (§1 table; G-1, G-2).** If every side is 2 and `⊕_{w∼v}` runs over the six
offsets, each neighbour occurs twice, the XOR cancels, `F ≡ H(0) = 0` and `φ = σ`. So `σ` *is* a time
shift. This is the same boundary case VER r2 §1.2 records for K1 under the multiset reading. Fix:
"every torus with some side `≥ 3`, or with `w ∼ v` read as a set relation". Native-Y's own side is odd
and large, so nothing about native-Y changes.

**R3. A second negative is proved here and is not accounted for.** §4's closing [A-inf] says "The one
negative proved here, no global reversal within budget", and §5 says "The only negative it has". G-6
is also a proved negative: there is no carrier–marker joint-law return before the crossing time for a
carrier whose current marginal is not uniform. On native-Y it covers every tick of the programme
horizon (as the screen notes). It must be listed and classified under SNR-1. It rests on an assumed
carrier preparation (U1 C-PREP), so it concerns an assumed apparatus and does not count. It also
concerns transport and return rather than recording, which is the analogue of CALC-F5. The Y and
G-ring cells for "subsystem uncomputation" should then say this explicitly: in its J-return form an
undo is excluded at G-6's scope, conditional on the assumed preparation. "Unsourced, not disproved"
applies to weaker forms, for example a marker decorrelated while the carrier is transported.

**R4. "It would need blank cells" (§4, subsystem uncomputation, Y) is an unsourced premise stated as
fact.** U1 does not state it. A reversible conditional gate can uncompute a conditional marking without
an ancilla, so a blank supply is not evidently necessary. The sentence sits next to Lemma R [NP] and
G-7, which leave no blanks under μ-G, so read as fact it would push the outcome toward "not
available". Fix: label it [A-inf] and write "may need", or source it.

**R5. The (c′) blocker list is incomplete.** Add:
- C-PREP, a sourced carrier preparation: C-5's point paths and G-6's non-uniform carrier both use it;
- R4 (amplification), beside R3 and R5;
- R1 on G-ring beyond C-5's single instance (`L = 4`, `q = 2`, one path pair, one tick);
- SUBSTATE-1's four scoped σ12 results (MR★:674–678, at `8af2d904`, which is reachable from `main`).

The screen cites MR★:670–681 but leaves SUBSTATE-1 out of "Prior screens". Those results ("a clean
single-register pair violates the preparation"; "a native random setting fails the distinct-interaction
test"; "supplies no selectable setting operation") bear on the C-PREP and C-INT rows of §4. Cite them
with their scope and their provenance standing in MR★, or say why they are not used.

## Optional findings

- **O1. Name the rules in the summaries.** SG-3 "does not transfer to σ12" should read "to Y and
  G-ring". AW-σ1 "is K1-only" should read "not shown beyond K1, and fails on Y and G-ring". SG-4 "on
  a non-additive rule" should read "on G-ring (one instance)". SG-5 "does not depend on additivity"
  should read "holds on Y and G-ring as on K1". In §5, "A negative closure of route M on K1 … does not
  extend" should read "the K1 obstructions used toward a negative closure do not extend to Y and
  G-ring".
- **O2. C-3 wording.** "Records" here means S-L5's structural hypothesis `Φ_{AΣ}s_Σ ≠ 0`. The
  marker's content masks it at `t = 1` (G-4), so no informational record is claimed. Say so. In the Y
  case, state `Σ = {v, w}` and `D = v ⊂ Σ` (S-L5's first bullet, the carrier's later state). Note
  that `w₂` records `y_v` while the effect on `D` depends on `y_w`. In the G-ring case,
  `m + (c − m)[m = 0]` is `u_1(i)` itself; the effect relative to `m = 0` is `(m − c)[m ≠ 0]`. And
  `u_1(i+1) = c − x_{i+1}` holds for every `c`, so the qualifier "for `c ≠ 0`" is not needed.
- **O3. Member L.** SM:811 states an explicit candidate map, under which links are a function of the
  matter state. No dynamics in which links act back on the matter is stated. Blocker 1 could name
  exactly that as what is missing, or offer a screen conditional on SM:811's candidate.
- **O4.** G-5 is Prop. 2.8(i)'s partition-independence clause, not its first clause.
- **O5.** OA-3 Lemma OBS concerns "an additive observer" (OA-3 STATUS:51–52); add the word.
- **O6.** §4, G-ring marker cell: say that C-5's `1/2` bit uses point-prepared carriers ([assumed],
  C-PREP), as CALC §3 does for its instances.
- **O7.** "Its K1 exclusion rested on S-C1(a)" should read "at VER's narrower scope". VER r2 §1.5 notes
  that MR★'s "no subsystem undo" wording goes beyond what is verified on K1.
- **O8.** Blocker 2, "The counterexamples and G-6 are about G-ring only", should read "within the SM
  class, about G-ring only".

## Nits

- **N1.** "CURRENT-HANDOFF.md in the same directory" is wrong. The file is in
  `native-y-continuation-20261024/`, not `shared_v12/`. The blob `bfcfb83f` is right.
- **N2.** CALC is cited as r1 and "unreviewed". r2 (`U4-CALC-r2.md`, blob `bef634e2`) is reviewed
  ACCEPT in `REVIEW-U4-CALC-r2.md`, and r1 itself was reviewed ACCEPT WITH CHANGES. The statements
  compared (Theorem 1(a)–(d), Theorem 2(a)–(d), Props. 1.4, 2.6, 2.8) are unchanged in r2, apart from
  Theorem 2(c) now carrying S-L2 [NP], which the screen does not use. Update the citation and the
  "Label dependence" paragraph.
