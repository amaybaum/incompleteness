# Independent recheck of EF-1 r5 (final)

**Reviewer:** non-author. I wrote none of r1–r5 and none of the reviews of r1–r4. Paper-only and
read-only: no repository edit, commit, push, GitHub write, computation or Lean build.
**Target:** `EF-1-r5.md`, sha256
`3cf761f0313e57eb6718f82bf3d6dc54dbbe710a85736c3a5858c84ae0beb16d` (verified before and after
reading). **Inputs read:** `EF-1-r4.md` (sha256 `b429d3af…d1b1`, verified), `REVIEW-EF-1-r4.md`,
`AGENTS.md` on `main` (§A.29, §A.31, §A.34, §A.47, Code Review Rules). **Citations** read at `main`
`bf89ba133ee9f2926a317e8af067ccaa862ce2db` with `git show origin/main:<path>`. **Owner comments** on
#1169 read through the GitHub tool: the fourteen comments from c.6894553525 to c.6897946443, which
include every id that r5 quotes; c.6897946443 is the latest comment on the issue. The review of r4
was treated as an unverified input: its three new statements were re-derived here from the
definitions, not relied on. Marking **[R2]** = an argument of this recheck, written out here and
checked by nobody else.

**Goal link (§A.47).** Item served: priority item 2, A1 dependence of the main equivalence and of
the results built on it. This recheck decides whether the three statements r5 lists as still
unchecked are sound as written, and whether r5 states the owner's distinctions exactly. It decides
no status, adopts no premise and gives no class recovery credit.

## Verdict: CONFIRMED WITH NITS

The mathematics that was still unchecked is sound as written in r5. All eleven findings of the
review of r4 are applied; two of them are applied in the body and only partly in the plain-language
summary (nit 1). The owner items O15–O19 are met; four sentences drop the owner's word
"automatically" (nit 3) and two summaries of Lemma C drop its measure (nit 2). No nit touches a
proof, and none gives any class recovery credit.

**Fit to present to the owner:** yes, after nits 1–3 are applied. Nits 4–8 are precision and can
be applied in the same pass; none of them changes a conclusion.

| Statement (r5 location) | Result of this check |
|---|---|
| Lemma C: a measure-preserving bijection of the patch data that reproduces the window exists iff the window law is shift-stationary (§P.4 (b2)) | **CHECKED-SOUND**, both directions separately |
| Corollary C1: invariance of the uniform product measure for the full system gives the condition of Lemma C at every horizon (§P.4 (b2)) | **CHECKED-SOUND** (one direction, and r5 claims only that direction) |
| Lemma C′: for second-order rules, the selected model included, every fixed-boundary closure is such a bijection (§P.4 (b3)) | **CHECKED-SOUND** |
| The necessity refinement: under one law that charges every cylinder, a finite influence set is necessary (N2.1) | **CHECKED-SOUND** |

These four have now had one independent check by a reviewer who did not state them. They remain
paper proofs, not kernel-checked. Whether that moves them out of the owner's tier "Still
unchecked" is a status statement for the coordinator to report and the owner to accept; r5's
tiers should not be changed silently (nit 8).

## 1. The unchecked mathematics, re-derived

### 1.1 Definitions checked first

- *Patch and record.* `U_n` is the syntactic backward set of the finite visible region `V`, with
  `U_{m+1} = V ∪ ⋃_{i∈U_m} N(i)` (N1.1). `G_n : C_{U_n} → (C_V)^{n+1}` is the record map of Lemma
  PM (a), and `X_k(d)` is its `k`th entry. `X_0(d)` is the readout of `d|_V`.
- *Reproducing the window.* A self-map `f` of `C_{U_n}` with `X_0(f^k d) = X_k(d)` for every patch
  datum `d` and every `k ≤ n` (§P.4 (b)). It is r4's definition with the readout made explicit.
- *Which measure.* The uniform probability on the finite set `C_{U_n}` (needs (P-fin) on `U_n`).
  On a finite set a self-map preserves it exactly when it is a bijection. It is the description's
  probability only under a uniform product starting law (D2); r5 says so at "Scope of Lemma C"
  (1) and at condition C4 of §4.0.
- *Which shift.* (C-ii): `|A_v| = |B_v|` for every `v ∈ (C_V)^n`, with
  `A_v = {d : X_{1:n}(d) = v}` and `B_v = {d : X_{0:n−1}(d) = v}`. Divided by `|C_{U_n}|` this is:
  under the uniform patch measure the block of steps `1..n` has the law of the block of steps
  `0..n−1`. That is one-step shift-stationarity of the window law, and "shift-stationary" names it
  correctly.
- *Boundary handling.* The fixed-boundary closure is `f_b(d) = φ(d ⊔ b)|_{U_n}` for a datum `b`
  on the sites outside `U_n`, the same `b` at every step (§P.4 (b1)).

### 1.2 Lemma C — CHECKED-SOUND

Hypotheses: (P-dep), (P-V), autonomous, (P-fin) on `U_n`, `n ≥ 1`. Each of `(A_v)_v` and
`(B_v)_v` partitions `C_{U_n}` (possibly with empty parts), since every datum has exactly one
value of each block.

*(C-ii) ⟹ (C-i).* Choose bijections `f_v : A_v → B_v` and let `f` be their union. It is total
(the `A_v` cover), injective (each `f_v` is, and the targets `B_v` are disjoint) and onto (the
`B_v` cover). By construction `X_j(f d) = X_{j+1}(d)` for `0 ≤ j ≤ n − 1`. Claim
`X_j(f^k d) = X_{j+k}(d)` whenever `j + k ≤ n`: true for `k = 0`; if true for `k` and
`j + k + 1 ≤ n`, then `j ≤ n − 1`, so `X_j(f^{k+1} d) = X_{j+1}(f^k d)`, and the hypothesis at
index `j + 1` (allowed, since `(j + 1) + k ≤ n`) gives `X_{j+1+k}(d)`. With `j = 0` this is (C-i).
The index bounds are right at each use.

*(C-i) ⟹ (C-ii).* For `0 ≤ j ≤ n − 1`: `X_j(f d) = X_0(f^j(f d)) = X_0(f^{j+1} d) = X_{j+1}(d)`;
the first equality is the hypothesis at the datum `f d` with `k = j ≤ n`, the last at `d` with
`k = j + 1 ≤ n`. So `f(A_v) ⊆ B_v`. `f` is injective, so `|A_v| ≤ |B_v|` for every `v`; both
families partition the same finite set, so the sums agree and every inequality is an equality.
Only injectivity is used.

§A.34: the two directions are proved separately in r5, each with its own argument, and both hold.

*Attempts to break it [R2].* (i) The shift on `Q^ℤ`, `V = {0}`: `|A_v| = |B_v| = |Q|`; the
rotation is a witness. (ii) `φ = id`: both parts are singletons for constant `v` and empty
otherwise; `f = id`. (iii) B1, `n = 1`: `X_1 = s_0 s_1`, so `|A_0| = 3`, `|B_0| = 2`; no
injective `f` can send three data into two, as the lemma says. (iv) A constant map
`φ(s) = 0`: `X_1 ≡ 0`, not stationary, and a closure would need `X_0(f d) = 0` for every `d`,
so no bijection: consistent. (v) The one-sided shift on `Q^ℕ`, which is not injective: the
window law is stationary and the rotation is a bijective closure, so the lemma does not need
`φ` to be a bijection, as stated. (vi) A readout that is a non-injective function of `s|_V`:
the proof never uses the form of the readout. (vii) `n = 0` is excluded by the hypothesis and
would be trivial. No counterexample found.

*One scope remark [R2], not a correction.* r5's "Scope of Lemma C" (1) says that for another
patch probability `p` stationarity is necessary and that sufficiency "is not proved here". The
necessity line is right (`f_# p = p` and `X_{0:n−1} ∘ f = X_{1:n}`). Sufficiency fails in
general: a bijection that preserves `p` on a finite set must send each datum to one of equal
mass, and stationarity determines only the total mass of each `A_v`. Example: sites 0 (visible,
`Z_2`) and 1 (hidden, `Z_3`), `φ(s)_0 = 1 − s_0` with declared reading set `{0, 1}`, `n = 1`,
`p(0, ·) = (0.3, 0.1, 0.1)`, `p(1, ·) = (0.2, 0.2, 0.1)`. Then `X_1` and `X_0` are both uniform,
so the window law is stationary under `p`, while a closure must exchange `{s_0 = 0}` and
`{s_0 = 1}`, whose mass lists differ. So the characterization belongs to the uniform patch
measure, which is what r5 states. The example uses a declared reading site with no actual
influence; it is offered as a caution only.

### 1.3 Corollary C1 — CHECKED-SOUND

Hypotheses: every alphabet finite; (L1), so `φ` is measurable; `μ(φ^{−1}E) = μ(E)`. Since
`X_k(s) = X_0(φ^k s)`, `{s : X_{1:n}(s) = v} = φ^{−1}{s : X_{0:n−1}(s) = v}`, and the two events
have equal `μ`-measure. The first is `{s : s|_{U_n} ∈ A_v}` and the second
`{s : s|_{U_n} ∈ B_v}` (Lemma PM (a), with `U_{n−1} ⊆ U_n`), and the marginal of `μ` on `U_n` is
uniform, so `|A_v| = |B_v|`. The proof uses invariance in the pre-image form only and no
bijectivity. r5 claims this direction only ("hence whenever"); it does not claim the converse,
and none is needed.

The existence of the bijection is a fact about `φ` and `μ`. A uniform product starting law is
needed only for the uniform patch measure to be the description's probability. r5 keeps the two
apart in §4.0 (C2 versus C4); the phrase "which holds given D2 with D3" in the claim table is a
sufficient condition and loses nothing.

### 1.4 Lemma C′ — CHECKED-SOUND

Form checked against `main`: ledger item (xiii), Main:724, "each site of (viii) carries a
previous and a current value in a finite abelian group", phase-space form
"$(x(t-1), x(t)) \mapsto (x(t), F(x(t)) - x(t-1))$", "each $F_i$ reading the current values at
finitely many sites". r5's `φ(p, c) = (c, F(c) − p)` is that form, on any site set.

(i) *Reproduces the window.* This is (b1), re-derived: for `i ∈ U_{n−k−1}`,
`N(i) ⊆ U_{n−k} ⊆ U_n`, so `f_b(f_b^k d)_i` reads only patch values, which equal those of
`φ^k s` on `U_{n−k}` by the induction hypothesis; hence `(f_b^k d)|_{U_{n−k}} = (φ^k s)|_{U_{n−k}}`
for `k ≤ n` and every `s` extending `d`, and `V ⊆ U_{n−k}`.
(ii) *Bijection.* For `i ∈ U_n`, `f_b(p, c)_i = (c_i, F_i(c ⊔ b^c) − p_i)`, because the previous
value read is the site's own. With `F^b(c) := F(c ⊔ b^c)|_{U_n}`, `f_b(p, c) = (c, F^b(c) − p)`
and `g(p′, c′) = (F^b(p′) − c′, p′)` satisfies `f_b ∘ g = id` and `g ∘ f_b = id`; both
compositions were recomputed. So `f_b` is a bijection of the finite set `C_{U_n}` and preserves
its uniform measure, for every `b` and every `F`, linear or not.
(iii) *Form.* `f_b` is of second-order form with force `F^b`, which reads `N_F(i) ∩ U_n`.

No counterexample is possible in this class: for a fixed current part `c` the map
`p ↦ F^b(c) − p` is a bijection, and `c` is carried along. Consistency with Lemma C: N3.2 gives
invariance of `μ` for every local second-order rule, so the window law is stationary, as Lemma C
requires of any rule with a bijective closure. The shift, a first-order rule, is correctly placed
outside: its fixed-boundary closure drops `d_0`.

### 1.5 The necessity refinement — CHECKED-SOUND

Statement: autonomous substratum setting, (P-dep), (P-V), no controller, the measurability
condition of Lemma PM (b); `ω` gives positive probability to every nonempty cylinder; a finite
autonomous deterministic model `(W, f, λ)` with some initial law reproduces the observation law
under `ω` at every horizon. Then `Im R` is finite, hence `J_∞` is finite.

Steps re-derived. (1) The model has at most `|W|` records; call the set `F_W`. Agreement at
every horizon is agreement on every cylinder of `(C_V)^ℕ`, hence on the product σ-algebra
(π–λ); a single record is a countable intersection of cylinders, so `F_W` is measurable and
`ω(R^{−1}F_W) = 1`. `R` is measurable because each `X_t` is. (2) Each `X_t` depends on the
finitely many coordinates in `U_t`, so it is locally constant and `R` is continuous for the
product topologies of discrete alphabets; no finiteness of alphabets enters. A finite set of
records is closed. So `O = R^{−1}(F_W^c)` is open, with `ω(O) = 0`. (3) A nonempty open set
contains a nonempty cylinder, which has positive probability; so `O = ∅` and `Im R ⊆ F_W`.
(4) (N2) ⟹ (N1) is Proposition N's step (two distinct records of a finite set differ by a time
`T`; then `J_∞ ⊆ U_T`), which uses no alphabet condition.

The writer's added observation is right: this direction uses no compactness and no alphabet
condition. With finite alphabets at every site the uniform product measure charges every
cylinder. §A.34: N2.8 carries the two directions as two rows with separate witnesses (the
refinement; Proposition N's (N1) ⟹ (N2) ⟹ (N3′) with finite alphabets on `J_∞`), and the
combined equivalence is stated with both hypotheses.

*Attempts to break it [R2].* The shift under a law charging every cylinder: the record law
charges every cylinder of records, so it is not carried by a finite set; consistent. The
counter example of N2.1 (alphabet `ℕ` at a hidden site): infinitely many records each of
positive probability; consistent. A law charging every cylinder whose record law is carried by
finitely many records while `Im R` is infinite would need an exceptional set of configurations
that is nonempty, open and null, which the hypothesis excludes. No counterexample found.

### 1.6 Two further checks made on the way

- *The two-site example of §P.4 ("Consequence for result classes").* Over `Z_2`, record
  `(d_0, d_0 + d_1)`: both displayed maps are bijections of the patch data and satisfy
  `X_0(f d) = X_1(d)`; under the first the hidden outputs from the two roots always coincide,
  under the second never. Correct.
- *A sharper form of r5's open question [R2].* r5 leaves open whether the fixed-boundary
  closures agree with the stage form of N1.7 for the full system. For a general rule they need
  not, and the reason is spatial: the off-diagonal action of the full system's reduced channel
  depends on the sites that *read* `V`, which the backward patch need not contain. Example:
  sites 0 (visible) and 1 (hidden) over `Z_2`, `φ(s) = (s_0, s_0 + s_1)`, a bijection. Then
  `U_n = {0}` for every `n`, the description determines its own self-map (the restriction, the
  identity on `Z_2`), and that map's channel is the identity; the full system's one-step channel
  with a uniform hidden state sends `|0⟩⟨1|` to 0, complete dephasing. The populations agree.
  This supports r5's sentence that a statement about off-diagonal action proved on a closure is a
  statement about that closure, and it bears on the rows whose content is off-diagonal (nit 5).
  It says nothing about the selected model, where coupling is symmetric and the question stays
  open.

## 2. The eleven findings of the review of r4

| # | Finding | Applied? | Note |
|---|---|---|---|
| 1 | (M-desc) existential; two statements wrong as written | **Yes** | Split into (M-desc-own) and (M-desc-some); Lemma C, C1, C′ stated and marked unchecked; both statements withdrawn; §4.2 cells restated as the requirement itself; "no class cites (M-full), Lemma C or Lemma C′". Two summaries drop the measure (nit 2) |
| 2 | Four sentences contradict Lemma K | **Yes in the body; partly in the summary** | Verdict 2, N1.5 ("can fail if"), F7, §4.1, EF-G18, §10 item 1 and question 9 (c) are right. The summary no longer says that finite reads on only the runs considered are not enough (nit 1) |
| 3 | Necessity under one fixed law | **Yes** | Verdict 3, N2.1, two rows in N2.8, §4.1, EF-G19, §10 item 3 |
| 4 | §3.4 obstructions have no row | **Yes** | Row in both tables of §4.2; bullet in N3.10; quotations and lines verified (Main:60, :480–486, :556–562) |
| 5 | Readback and one-step coherence rows miss requirements | **Yes** | Main:135, :137, :280–282, :310, :324 verified |
| 6 | F5 flag; "finite alphabets at every site"; D3 | **Yes** | All three |
| 7 | Corner occupancy, form cell | **Yes** | |
| 8 | "The locality class of `main`" | **Yes** | Paragraph in §P.3 |
| 9 | Summary, three points | **Partly** | The inexact sentences are gone, but so is the statement that two conditions are not separate premises on `main`, which the finding asked to be named, not removed (nit 1) |
| 10 | E3; "the same comment continues"; AW-EF15 | **Yes** | E3's added example re-derived |
| 11 | Standing of the proofs | **Yes** | Tier table; marks replaced. Two stale marks elsewhere (nit 7) |

The r4 response tables are kept as r4's record with r4's marks, and r5 says so before them. That
is acceptable.

## 3. Owner items

- **O15** (c.6897859755): "Failure of automatic inheritance does not imply that no suitable finite
  closed model exists. Any wording suggesting the latter should be withdrawn." Searched the whole
  text for "does not transfer", "fails for", "cannot", "no … closed model", "no invariant
  measure", "not defined", "not supplied", "not carried", "has no" and kindred wording. Every
  remaining negative statement is about one of: the description as given (it has no self-map of
  its own); one particular closure (the shift's fixed-boundary closure); bijections of the patch
  data under the uniform patch measure (B1, with the sentence that B1 has finite closed models on
  other carriers); or what a window-valid model can establish about nature ("closure cannot supply
  it", defined that way before the second table of §4.2). The withdrawn sentences survive only as
  quotations of what was withdrawn. **No residual wording found.**
- **O16**: three tiers with the owner's contents, quoted exactly; each of the four checked items
  carries "under its stated hypotheses" in the tier table, §9 and the summary. r5's own additions
  to the unchecked tier are labelled as r5's. **Met.** The phrase is missing at a few brief
  mentions outside the table (nit 4).
- **O17**: "no recovery credit yet" and "does not automatically disqualify" both stated at Verdict
  6 and §P.4; §4.2 has the per-class column "requirements confined to the window?" for every
  class. **Met**, except that four sentences drop "automatically" (nit 3).
- **O18**: "finite reads on every run, under the lemma's other hypotheses" is used wherever
  Lemma K is stated in brief (status tables, Verdict 2, N1.5, F7, §4.1, EF-G18, §10, summary,
  question 9). **Met.**
- **O19**: the six-row claim-to-conditions table is in the owner's order with the owner's row
  texts quoted exactly; §4.0 is organized by the same six claims; "Scope conceded" quotes the
  owner and concedes scope without deciding status; every direct-proof target is marked
  "[IR; no proof given; not a recovery]"; the two barred shortcuts are quoted exactly and the file
  is checked against both. Checked here: no target removes a condition of an existing proof; no
  assumption is proposed for adoption (D2, FS-all, a finite complete state and H-mem are named as
  unadopted); every conditional statement read carries its condition. **Met**, with one target
  whose stated conclusion omits the rule it is proved for (nit 5) and one favourable aside that
  should carry its caveat (nit 6).

## 4. Standing rules, quotations, summary, questions, disagreements

- No finiteness claim about the substratum as a whole, under any label: none found. The owner's
  question in c.6896070253 is quoted to its first clause only.
- F-each and F-one kept apart; settings the same or the same policy with its information (claim 1,
  Verdict 2, F6, PM-I); no recovery credit in any row; "currently establish no justified
  constraint on observations" used, the other phrase only inside the owner's quotation.
- **Quotations.** Every quoted owner passage in r5 was matched as an exact substring of the
  comment it is attributed to (c.6894872312 through c.6897946443). All exact, ids right. The
  quoted passages of `main` added in r5 were matched against `papers/Main.md` at the lines given.
- **Summary.** Plain. Accurate as far as it goes; it now omits the settings condition and the
  status of two premises (nit 1).
- **Questions.** Self-contained except 9 (b) and 10, which use "fixed-boundary closure",
  "second-order rules" and "shift-stationary" without a gloss (nit 2).
- **Remaining disagreements.** Complete against the review of r4's section 7. One deviation is
  not recorded there: the summary was rewritten where findings 2 and 9 asked for amendments. Nit 1
  removes the deviation; otherwise it should be listed.
- **Banned content.** None found in r5.

## 5. Nits, with exact remedies

1. **Summary: restore the settings condition, the per-run sentence and the two premises
   (owner-facing; apply before presenting).** In "Plain-language summary for the owner", after the
   sentence ending "a starting law only adds probabilities." insert:
   "With settings or a policy, the runs compared must have the same settings, or the same policy
   with the information it uses. One patch for every branch then needs the sites that could be
   read or acted on to be finite over every branch, or finite reads on every run, under the
   lemma's other hypotheses; finite reads on only the runs considered are not enough. Without A1,
   a finite visible region and finite supports over every branch are not stated as separate
   premises on `main`."
2. **Lemma C in brief: keep its measure; gloss question 9 (b) and question 10 (owner-facing; apply
   before presenting).**
   - "Detail by piece", row for §P.4: replace "Lemma C (a measure-preserving bijection" by
     "Lemma C (under the uniform patch measure, a measure-preserving bijection".
   - Question 9 (b): replace the clause from "(b) the finite description" to "closure is one;" by
     "(b) the finite description does not automatically inherit a measure-preserving map; on the
     patch data, with all patch data taken as equally likely, a one-to-one map that matches the
     observations up to the horizon can be chosen exactly when, under that measure, the statistics
     of steps 1 to `n` equal those of steps 0 to `n − 1`; and for updates of the second-order form
     (ledger item (xiii), Main:724) the map obtained by holding the sites outside the patch at any
     fixed values is always one;".
   - Question 10: after "so that a chosen closure" insert "(a self-map of the patch data, added
     by choice, that matches the observations up to the horizon)".
3. **"Automatically" (owner-facing; apply before presenting).** Owner: "does not automatically
   disqualify it either".
   - "Detail by piece", row for §P.4: "does not disqualify it either" → "does not automatically
     disqualify it either".
   - EF-G17 and §10 item 2 (same words in both): "it earns no recovery credit yet and is not
     disqualified for a theorem whose requirements are confined to the window" → "it earns no
     recovery credit yet, and being chosen and window-valid does not automatically disqualify it:
     it could suffice for a theorem whose requirements are entirely confined to the window".
   - Summary: "does not disqualify it either" → "does not automatically disqualify it either".
   - "r5 changes", row O17: "and not disqualified" → "and not automatically disqualified".
4. **"Under its stated hypotheses" at brief mentions.**
   - Header, definition of the mark "[checked by the review of r4]": after "found sound" insert
     ", as the statement with its stated hypotheses".
   - Verdict 11: "checked, the four proofs of the table "Proof status"" → append
     ", each under its stated hypotheses".
   - §10, last paragraph: "invariance is checked for the full system" → "invariance is checked
     for the full system, under its stated hypotheses".
   - "Detail by piece", rows for N2.1 and for (M-full): after "checked sound by the review of
     r4" insert ", under its stated hypotheses".
5. **One-step coherence row, second table of §4.2.**
   - Target: replace "Conclusion: the one-step reduced channel of a region is not
     entanglement-breaking exactly when `w < κ`" by "Conclusion: for one step of the displayed
     update over `F_2` (Corollary 1, Main:316; stated for `q = 2`, Main:324), the reduced channel
     of a region is not entanglement-breaking exactly when `w < κ`".
   - Window cell: after "Closure could suffice; to be determined; no credit yet" append
     ". Open within that, as for the row above: the result concerns the action on off-diagonal
     inputs, which depends on the closure (§P.4)".
   - Optional, marked as this recheck's and unchecked: add the example of section 1.6 to §P.4
     after "is not derived here", as a case where the closure the description determines differs
     from the full system's channel off the diagonal.
6. **Lemma 3 row, second table of §4.2.** The aside that the counting measure is the
   maximal-entropy invariant measure of every bijective closure is true and favourable (§A.31).
   Append: "It could not serve as an independent justification of a uniform starting law: that a
   bijective closure exists is itself a statement made under the uniform patch measure
   (Lemma C)."
7. **Two stale marks.** N3.5 ("[IR, proof in N2.10, unreviewed]") and EF-G10
   ("(N2.10, unreviewed)"): N2.10's heading and EF-G15 say "checked by the review of r3". Replace
   "unreviewed" by "checked by the review of r3" at both.
8. **Standing after this recheck.** r5 may add one line under the tier table: "Lemma C,
   Corollary C1, Lemma C′ and the one-law refinement were re-derived by the recheck of r5 and
   found sound (one independent check; paper proofs; not kernel-checked). They stay in the tier
   'Still unchecked' until the owner accepts that check." No tier, class or row changes on it.

Optional, no remedy required: "Scope of Lemma C" (1) may replace "is not proved here" by "does
not hold in general (an example is in the recheck of r5, unchecked)"; question 9's letters run
(a), (c), (d), (b), (e) and could be put in reading order if the references to them in "r5
changes" are updated together.

## 6. Remaining disagreements with r5

None on the mathematics. On wording: nits 1–3. On scope, one addition offered and not required:
the off-diagonal action of a closure can differ from the full system's even where the description
determines the closure (section 1.6).

## 7. What can be relied on after this recheck

- Lemma C, Corollary C1, Lemma C′ and the one-law necessity refinement, each under the hypotheses
  r5 states, with one independent check each. Paper proofs.
- That r5 withdraws every statement suggesting that no suitable finite closed model exists, and
  claims no recovery for any class.
- Nothing about recovery. Whether a closure preserves everything a particular audited result
  requires is unproved for every class; this recheck proves none of it. The [R2] remarks of
  sections 1.2 and 1.6 are unchecked and support no classification.
