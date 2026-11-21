# REC-1 P0: the coset-space witness for OBL-SP (paper-only hand record)

**Standing.** WIP / UNVERIFIED. Hand reasoning only, unreviewed. No computation on any OI rule, no
script, no Lean, no manuscript or record edit, no premise adopted, no status or priority changed.
Every derivation step below is [W, P0] (a reading made in this record, unreviewed) unless it cites a
source. Under §A.46 item 7 nothing here may serve as a premise of an established claim before
independent review.

**Authority.**
- Owner authorization of REC-1 P0 as a supporting-priority, paper-only unit: #1169 c.6854241002
  (`amaybaum`, 2026-11-13), as relayed by the coordinator; the comment text was not re-fetched in
  this unit.
- Owner-confirmed safeguard (2026-11-13), as relayed by the coordinator: keep r7's mixed-case
  outcome; if some preparations fall outside the coset form while others are in form with
  unresolved checks, report both findings. Applied in §6.
- Limits: hand reasoning only; no computation on OI rules, no script, no Lean; no new premise; no
  repository edit, commit, push or post.

**Pins.**
- Preregistration: `REC-1-r7.md` (blob `f1ffac0e`), `verification/programmes/oi-qm/reconstruction/drafts/rec-1-20261113/`,
  branch `research/rec-1-1169-20261113` at `9f7d2612f39960a41188eae8f3753d9def8019e8` (draft PR
  #1268), cited `r7:n`. Off `main`.
- Sources on `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` (paths under
  `verification/programmes/oi-qm/reconstruction/` unless a paper):

  | Short | Path | Blob |
  |---|---|---|
  | Main | `papers/Main.md` | `0db17597` |
  | OA1 | `oa-1-20261112/OA-1-REPORT-r5.md` | `5a16b213` |
  | OA2 | `oa-2-20261112/OA-2-REPORT-r4.md` | `8f8ddf73` |
  | OA3 | `oa-3-20261112/OA-3-REPORT-r4.md` | `0a36fd05` |
  | S3 | `drafts/tune-1-20261111/TUNE-1-STEP2-SESSION3.md` | `a9cbc675` |

- Off `main`: `TUNE-1-STEP3A-r3.md` (blob `7bbec04d`), branch `research/tune1-step3a-1236-20261113`
  at `8228b3c24e17a17f324b6779b53b04ad296b4308`, cited `3A:n` [R-off].

**Labels.** [R] research record on `main`, not independently established; [R-off] research record
off `main`; [W, P0] hand reading in this record, unreviewed; [L] literature, from memory, context
only. OA-1 line numbers are those of `OA-1-REPORT-r5.md`; OA-3 and r7 cite OA-1 r4 lines, which
differ (for example N1-K is OA1:131 here).

***

## 1. The preregistered rule (r7 §4, verbatim)

P0 (r7:317–338):

> - P0. Cheapest decisive step: decide whether, for every instance in the class, the reachable laws
>   of `Z₀` are mixtures of uniform laws on the cosets of one subgroup, each coset reachable and
>   determined by the held record, so that the coset-space model is a simplex embedding. Record
>   which preparations, if any, fall outside that form, such as heralds that cannot be composed
>   under the fixed typing. Once the in-form preparations pass the operational witness, only those listed preparations
>   carry OBL-SP's open content. P0 is posed under H-xiv.
>   Implementation checks (not results): the coset-space simplex witness uses accessible indicator
>   effects in the C-PM class, excluding reads of preparation labels; that a coset is "determined by
>   the held record" is backed by a valid operational effect in that class and an operational
>   equivalence test; O-V and the controls of P4 (contextual, quantum and supra-quantum) are kept.
>   P0 has three outcomes.
>   - Pass, only when the entire operational simplex-embedding witness is validated for the whole
>     class: a common coset-mixture description of the reachable laws, every needed coset reachable,
>     each coset's identity operationally determined by held records, and the C-PM accessible
>     indicator and equivalence effects exhibited. The law form alone is not a pass. A pass may close
>     OBL-SP as O-C, subject to P4, including O-V.
>   - Out of form: preparations outside the coset form are exhibited. They are listed for the
>     residual investigation, and OBL-SP continues on them.
>   - Unresolved: the coset form holds, but a reachability, accessible-effect or equivalence check
>     fails or is unestablished. That failure is recorded separately, and the outcome is O-U unless an
>     independent classicality proof or a contextual counterexample is supplied. It is never reported
>     as O-C from the coset form alone, and never as a non-classical witness.

P4 (r7:349–357):

> - P4. Controls, with expected classifications preregistered as a rule: (i) instances that satisfy (SP)
>   are classified simplex-embeddable (preservation of E(b)); (ii) OA-2's N2.1 non-spanning
>   counterexample (OA2:296–315, :542–544) is classified non-simplex-embeddable by the same classifier;
>   (iii) the (V-ii-U) shift artefact (OA3:418–459) is excluded by the fixed herald typing; (iv) `𝔊_K`
>   (row 20), outside the class, is classified non-simplex-embeddable; (v) non-vacuity: at least one
>   instance of the class satisfying H-xiv, with records formed inside `S` and a nontrivial fragment, is exhibited, or
>   O-V is reported; (vi) P2's label is checked on a known quantum-realizable contextual fragment
>   (labelled O-Q) and on a fragment with no quantum model under P2 (labelled O-SQ), both fixed before
>   the attempt.

Ordering rule (r7:303–311):

> - Ordering rule, fixed in advance. If P0 passes for the whole class under the fixed typing (the
>   whole operational witness validated, P0), OBL-SP closes as O-C, subject to P4 (O-V if (v) fails), and the next
>   obligation is AW-OA2-1 with the same φ, `D_0`, (H3), record class, herald typing, C-PM, H-xiv and
>   (SP) and a non-additive read map; no premise is adopted, and H-xiv is carried as a hypothesis.
>   If P0 lists preparations outside the coset form and the in-form preparations pass the
>   operational witness, OBL-SP continues on the listed preparations alone; in-form preparations whose
>   checks fail or are unestablished are O-U as well (P0). If the coset
>   form holds but an operational check fails or is unestablished, the outcome is O-U (P0), and Q4 is
>   not handed to AW-OA2-1 on that basis. In none of these cases does Q4 stop at a premise; the herald typing (C7) is carried as a scope hypothesis.

The class is OBL-SP's statement (r7:251–264): φ in the gauge-derived affine class (ledger (vii);
R-lin with (xiii)) on a finite carrier; initial law in `D_0` (designated cells at known values, every
other cell uniform and independent); H-AR observers; (H3); records as in (H4) or in the (V-ii-H)
effect class; heralds typed as held at use with records formed inside `S`; the closure-defined
prepare–measure fragment under C-PM; H-xiv.

***

## 2. Fixed before the derivation

### 2.1 Instance and fragment

An instance is `(φ, V, D, r, T, t_p)`: a rule of the class, an H-AR observer `V ⊊ S` (a set of cells
read at full resolution, OA2:184–186; Main:42), a designated set `D` with values `r` (label and setting
cells are designated cells whose values vary with the procedure, OA1:111–113), a horizon `T`, and a
preparation–measurement split `t_p ≤ T`. Write `K = {ω : ω|_D = 0}` for the free subgroup; the initial
law is uniform on `r + K`.

The fragment (P1; OA2:100–125, :150–157):
- preparations: label values, coin mixtures (coins under C-PM, OA2:112–118), and heralds on held
  records of reads at ticks `≤ t_p`, each herald still held at use time (OA1:131), padded by waiting
  to end at `t_p`;
- measurements: setting values and post-processings of held records of reads at ticks in
  `(t_p, T]`, including heralded composites (herald at a measurement-stage tick, then read);
- C-PM: a preparation's own label cells, including its herald records (OA3:101–102), are not effects.

### 2.2 The classifier (derived from r7:317–338; used for the class and for every control)

Given a fragment whose effect responses are functions of one record variable `Z₀` (settings acting by
translation), find a subgroup `S` of the record group with:

- **C1 (law form).** Every reachable law of `Z₀` is a mixture of uniform laws on cosets of `S`.
- **C2 (reachability).** For every coset `t + S` meeting `U_Z` (the union of supports), the uniform
  law `u_{t+S}` is the law of some admitted preparation.
- **C3 (accessible indicators).** For every such coset, `1[Z₀ ∈ t + S]` is an available effect (or a
  sum of available effect statistics) in the C-PM class, reading no preparation label.
- **C4 (equivalence tests).** Preparations are operationally equivalent iff their coset-weight vectors
  agree; effects are operationally equivalent iff they agree on every `u_{t+S}`.

Output: PASS when some `S` meets C1–C4 for every instance; OUT-OF-FORM entries when admitted
preparations have no such description; O-U when C1 holds and C2, C3 or C4 fails or is
unestablished, unless an independent classicality proof or contextual counterexample is supplied.

### 2.3 Fixed control fragments for P4(vi)

- O-Q control: the qubit parity-oblivious multiplexing fragment: four states with Bloch vectors
  `((−1)^{b₀}, (−1)^{b₁})/√2` in the z–x plane, reads `σ_z`, `σ_x`.
- O-SQ control: the gbit square of `𝔊_K` (OA2:423–458): four point preparations `[ab]`, two sharp reads
  `X`, `Y`, and `½([00]+[11]) ∼ ½([01]+[10])`.

***

## 3. Inputs re-derived before use (P3)

- **R1 (Theorem E(a), OA2:525–527 [R]).** Under (H1) `Φ^τ` is affine; under H-AR a read is a
  coordinate projection; so each read is `Z_τ = H_σ^τ σ + H_c^τ c + H_α^τ α + k_τ` with homomorphisms
  independent of `c`. Settings act by translation. Re-derived. Feedback settings written by φ are
  coordinates of `Φ^τ ω₀` and are inside this affine form.
- **R2 (Lemma 0 and Lemma A-T (c), S3:50–54, :69–70 [R]).** The image of the uniform law on a coset
  `g + G′` under a homomorphism `h` is uniform on `h(g) + h(G′)` (fibres of `h|_{G′}` are cosets of
  `ker h ∩ G′`). Conditioning the uniform law on `g + G′` on an affine event `{Gω = y}` gives the
  uniform law on `(g + G′) ∩ G^{-1}(y)`, empty or a coset of `G′ ∩ ker G`. Re-derived.
- **R3 (S3 L5.4, S3:196–207 [R]).** With `S_m = H(K)` on (prefix, continuation) records, the
  continuation law given a complete prefix record is uniform on `t_r + S₀`,
  `S₀ = {t : (0, t) ∈ S_m}`. By R2, `S₀ = H_cont(K ∩ ker G_prefix)`: `(0, t) ∈ H(K)` iff some `k ∈ K` has
  `G_prefix k = 0` and `H_cont k = t`. Re-derived; it is the case `J = J*` of node N4 below.
- **R4 (retention under the fixed typing; OA3:410–416, :474–475, :491 [R]).** Under held-at-use
  typing, a heralded composite `[Z_{τ₁} = r]·f(Z_τ)` is one run's held outcome only if the event
  `{Z_{τ₁} = r}` is still held at `τ`, i.e. a function of `V(τ)` (OA1:131, :135). Its availability for
  every `r` and every `τ₁ < τ` makes every earlier read a function of `V(τ)`. Re-derived.
- **R5 (Proposition B(ii) (⇐), OA2:259–264 [R]).** If `W = ℝ^U`, two effects equal on `W` are equal on
  `U`. Re-derived (used in control (i) only).
- **R6 (N2.1 counterexample, OA2:296–315 [R]).** On `W = {w₀₀ + w₁₁ = w₀₁ + w₁₀}`,
  `w₀₀ = ½X0 + ½Y0 − ¼` holds at all four vertices (checked: `σ_{x0}`: ½ = ½ + ¼ − ¼; `σ_{y0}`: ½ = ¼ + ½ − ¼;
  `σ_{x1}`: 0 = 0 + ¼ − ¼; `σ_{y1}`: 0 = ¼ + 0 − ¼). The bounds `ξ_{E10} ≥ 0`, `ξ_{E11} ≥ 0` pin `ξ_{Y0} = ½`
  on the `x`-supports, and preparation noncontextuality puts the support of `μ_{y0}` there, against
  `Y0(σ_{y0}) = 1`. Re-derived (used in control (ii)).
- **R7 (Claim 2, OA2:443–458 [R]).** Four point preparations with pairwise disjoint supports and
  `½(μ₀₀+μ₁₁) = ½(μ₀₁+μ₁₀)` are incompatible. Re-derived (used in controls (iii), (iv)).

OA-2 Theorem E(b) steps 1–4 (OA2:528–534) are not used as premises: their content for this class is
re-derived in N1–N6. Proposition B(i) is not used.

***

## 4. Derivation (depth-first)

### N1. Form of the reachable laws [W, P0]

Fix an instance. By R1 every read, herald record and setting-free record is affine in `ω₀`.

1. A label value `p` gives the initial law uniform on `r_p + K`.
2. A herald on a set `J` of preparation-stage reads conditions on `G_J ω₀ = y` (affine). By R2 the
   result is uniform on a coset of `L_J := K ∩ ker G_J`. A herald on an event with several values
   gives a mixture of such laws; a coin mixture gives a mixture; a discard leaves `Z₀`'s law unchanged.
3. With `Z₀ = H ω₀ + k` (the measurement-stage record with `H_c c` removed, R1), R2 makes every
   reachable law of `Z₀` a mixture of uniform laws on cosets of `S_J := H(L_J)`.

Verdict: proved [W, P0], for every instance. It extends Lemma A-T (c) and L5.4 to arbitrary
herald sets.

### N2. The law form is vacuous on its own [W, P0]

C1 holds for `S = {0}` in every finite instance: every law is a mixture of point laws. So C1 carries
no content without C2 and C3, and with `S = {0}` C2 is (SP) itself (control (i)). The decisive
content of P0 is reachability (C2) and accessibility (C3). This is the reason r7:331 refuses a pass
on the law form.

### N3. Composability of heralds in the class [W, P0]

C2 needs a smallest `S_J`, i.e. an admitted herald set `J*` containing every admitted `J`.

- *(H4) instances.* The held record at the latest read determines every earlier available read
  (OA2:502); preparation-stage reads are available reads in "prepare, wait τ, read" (OA2:105–106). So
  every preparation-stage read is still held at use time, and the herald on all of them jointly is a
  function of held records at use: admitted.
- *(V-ii-H) instances.* (V-ii-H) makes every heralded composite available (OA3:120–123). Under the
  fixed typing, R4 turns this into: every earlier read is a function of the present `V` at every later
  read. So the same holds, with records formed inside `S` (MP-0b's outside-`V` history is excluded by
  r7:255).

Verdict: in every instance of the class, `J*` = the set of all preparation-stage reads is admitted.
This rests on the record hypothesis read with the fixed typing (OA3:474–475: under held-at-use typing
the (V-ii-H) class "is itself retention-type"); it does not follow from φ or `D_0`.

### N4. The finest subgroup and reachability (C2) [W, P0]

Let `L* = K ∩ ker G_{J*}` and `S* = H(L*)`.
- C1: `L* ⊆ L_J` for every admitted `J`, so each `S_J`-coset law is a uniform mixture of `S*`-coset
  laws.
- C2: the cosets of `L*` in `r_p + K` are the fibres of `G_{J*}`, each of positive probability under the
  uniform law. Heralding on `G_{J*} = y` with label `p` prepares, by R2, the uniform law on one
  `S*`-coset. `H(r_p + K)` is the union of these images, so every `S*`-coset in `U_Z` is reached.
- Preparations of several lengths are padded by waiting to `t_p`; their heralds are subsets of
  `J*`. So r7's case "heralds on prefixes of several lengths, whose cosets refine as the prefix grows"
  (r7:287–289) is inside the form: the refinement stops at `J*`.

Verdict: C1 and C2 hold with `S*` for every instance.

### N5. The effect set and accessible indicators (C3) [W, P0]

- Every preparation-stage read is a herald record of some admitted preparation (N3), hence a label
  under C-PM (OA3:101–102). A common effect set for the prepare–measure table therefore excludes all
  cells that hold preparation-stage records. What remains are reads of the prepared configuration,
  as OA2:114–115 requires ("No read of the prepared configuration is removed"). This is forced by
  C-PM together with N3, not chosen.
- By the record hypothesis (N3), the measurement-stage reads are jointly held at the latest read, in
  cells the effects may read. For (V-ii-H) the cone of joint indicators equals variant (i)'s
  (OA3:477–484), and singleton indicators are available as heralds at every tick followed by a final
  read (OA3:468–469).
- So `1[Z₀ − h(c₀) ∈ t + S*]`, for a fixed reference setting `c₀`, is an available C-PM effect, or a sum
  of available singleton statistics, and reads no preparation label.

Verdict: C3 holds. The witness does not depend on how label cells are delimited: for any fixed common
effect record `Z_e` (any homomorphic image of `ω₀` plus setting translation), N1–N4 run with `H`
replaced by `H_e`.

### N6. Equivalence tests and the simplex embedding (C4) [W, P0]

Ontic space `Λ` = the `S*`-cosets in `U_Z`. Preparation `s ↦ ι(s)(t+S*) = P_s(Z₀ ∈ t+S*)`. Effect
`(c, f) ↦ ξ(t+S*) = mean of f(z + h(c)) over z ∈ t+S*`, which equals the statistic of `(c, f)` on the
admitted preparation `u_{t+S*}`.

- Reproduces every statistic: `P_s = Σ_t ι(s)(t)·u_{t+S*}` (N4), and cosets are disjoint.
- Preparation noncontextual: `ι(s)` is a vector of statistics of C3's effects, so equivalent
  preparations have equal `ι`.
- Measurement noncontextual: equivalent effects agree on every admitted preparation, in particular on
  each vertex `u_{t+S*}`, so their `ξ` agree.
- Equivalence tests exhibited: preparations by the finitely many coset-indicator statistics; effects
  by their statistics on the finitely many vertex preparations.
- `ι` is affine on mixtures; `ξ ∈ [0, 1]`, summing to one over outcomes.

Verdict: the coset-space model is a noncontextual model of the prepare–measure fragment, hence a
simplex embedding (G3 read as OA2:157; [L: Schmid et al., PRX Quantum 2, 010331 (2021)]), for every
instance of the class, under H-xiv. Transformation noncontextuality is not claimed (as OA2:540–541).
With `J* = ∅` and no heralds, `S* = S_m` (Lemma A-T (c)); with `J*` a complete prefix, `S*` is S3's `S₀`
(R3), which re-derives S3:206–207's statement for the C-PM fragment of this class.

### N7. Preparations outside the form [W, P0]

Within the class, none. r7's two anticipated items:
- prefixes of several lengths: inside the form (N4);
- heralds that cannot be composed because an earlier herald has no record inside `S` (r7:289–290): an
  instance in which some earlier read is not held at a later read fails (H4), and fails (V-ii-H) under
  the fixed typing (R4). It is outside the class, not an out-of-form preparation of it.

### N8. Pressure test of the favourable branch (§A.31) [W, P0]

1. **Is the pass carried by a hypothesis rather than the dynamics?** Yes, in part. Composability
   (N3) comes from the record hypothesis under the typing. The class is the set of observers that
   physically retain, inside `S`, every read of the horizon. The pass says that for those observers
   the failure of raw (SP) is harmless; it says nothing about observers that do not retain.
2. **Does the excluded region hide a non-classical shape?** Hand sketch [W, P0; unreviewed; outside
   the class; not a result]. Take OA-3 N4.2's three-cell shift (OA3:420–425) and add, inside `V`, a
   recorder: a conveyor whose front cell receives `⊕=` the content of cell 0 each tick, with two
   designated blank cells at the front at ticks 1 and 2 and uniform cells everywhere else (a `D_0` law;
   each map is an additive bijection, so (H1) holds; it is not an R-lin rule). The blanks retain
   `V(1) = x` and `V(2) = y` inside `S`, so the heralds `[ab]`, `x+y = 0` and `x+y = 1` are held at use;
   later records are masked by uniform cells, so measurement-stage reads are held only at their own
   ticks. With the herald cells excluded under C-PM, the effects are N4.2's single-tick reads, and
   R7 makes the fragment preparation-contextual. The instance fails (H4) and fails (V-ii-H) under the
   typing, so it is outside the class. Consequence: the exclusion of N4.2's shape from the class rests
   on the record hypothesis, not on the herald typing alone (assumption-watch marker AW-P0-1, §7).
3. **Label delimitation.** C-PM is stated for label cells (OA2:112–115). N5's witness holds for every
   fixed common effect record, so the verdict does not depend on how cells carrying retained herald
   content are delimited. A per-preparation effect set would not define a prepare–measure table at
   all.
4. **Measurement timing.** Under inclusion a measurement is not started by an external clock; reads
   are absolute-tick records, and the split `t_p` is fixed per fragment (§2.1). Every `t_p ≤ T` is
   covered.
5. **H-xiv.** If measurement-setting cells influence a preparation-stage record, a herald correlates
   the prepared law with the setting. H-xiv excludes this by hypothesis; it is not derived from `D_0`
   or φ (r7:257–264).
6. **Exactness.** Herald probabilities may be small but are positive; the embedding is exact.

Classification under §A.31: N2 and N8.1–2 are NEW (the law form is vacuous; the class's
composability is supplied by the record hypothesis, and the excluded region contains a
convention-type contextual fragment realizable with records inside `S`); N1, N4–N6 are ELABORATING of
Lemma A-T (c), L5.4 and E(b).

***

## 5. Controls (P4)

| Control | Check performed | Result | Status |
|---|---|---|---|
| (i) (SP) instances simplex-embeddable | Under (SP), `span{u_{t+S*}} = ℝ^{U_Z}` forces `#cosets = |U_Z|`, so `S* = {0}`; the classifier's model is E(b)'s `Z₀` model; R5 gives measurement NC directly | classified simplex-embeddable, same as E(b) | green |
| (ii) N2.1 counterexample classified non-simplex-embeddable by the same classifier | C1 with `S = ⟨(0,1)⟩` fails on `σ_{y0}` and with `⟨(1,0)⟩` on `σ_{x0}`; only `S = {0}` remains; point laws are not reachable, so C2 fails and no pass is returned; R6 supplies the independent contextual counterexample | no pass; non-simplex-embeddable by R6 | green |
| (iii) (V-ii-U) shift artefact excluded by the fixed herald typing | N4.2's preparations need `V(1)`, `V(2)` held at `t_h` (OA3:410–413), which they are not; so they are not admitted. The recorder variant (N8.2) re-admits them with records inside `S` but fails the record hypothesis | cited instance excluded by the typing; variant excluded by the record class | green, with AW-P0-1 |
| (iv) `𝔊_K` classified non-simplex-embeddable | Outside the class (designed non-affine Φ, OA2:483). Classifier: point preparations reachable, so `S = {0}`; the joint `(x, y)` indicator is physically absent (OA2:466–467), so C3 fails and no pass is returned; R7 gives preparation contextuality | no pass; non-simplex-embeddable by R7 | green |
| (v) non-vacuity | Instances I and II below, each in the class, satisfying H-xiv, with records inside `S` and a nontrivial fragment | exhibited | green |
| (vi) P2 labels | O-Q: the §2.3 multiplexing fragment is contextual [L: Spekkens et al., PRL 102, 010401 (2009)] and is its own quantum model, with `½(ρ₀₀+ρ₁₁) = ½(ρ₀₁+ρ₁₀) = I/2` mapping the equivalence to equality. O-SQ: for the gbit square, `⟨E_X⟩ = 1` on `ρ₀₀, ρ₀₁` and `0` on `ρ₁₀, ρ₁₁` puts the first pair in the range of the eigenvalue-1 projector `P` of `E_X` and the second in `ker E_X ⊆ P^⊥`; then `P(ρ₀₀+ρ₁₁)P = ρ₀₀` and `P(ρ₀₁+ρ₁₀)P = ρ₀₁`, so the equivalence forces `ρ₀₀ = ρ₀₁`, against `Y` | O-Q and O-SQ labels assigned correctly | green |

The two operational checks are not vacuous: C2 fails on control (ii) and C3 fails on control (iv).

**Instance I (no herald).** R-lin `(y, x) ↦ (x, Ax − y)`, `A x_i = x_{i−1} + x_{i+1}`, ring of 4 sites
over `ℤ/q`. Designated: `x₀ = x₂ = 0`, `x₁ = c` (setting), `y₀ = p` (label), `y₂ = 0`; uniform: `x₃ = u`,
`y₁`, `y₃`. `V = {x₀, x₂}`, `T = 1`, `t_p = 0`. Then `V(0) = (0, 0)` and `V(1) = (u + c − p, u + c)`, so
`Z₀ = (u − p, u)` is uniform on `(−p, 0) + Δ` with `Δ` the diagonal. There are `q` cosets, each prepared
by one label; (SP) fails, since `dim W = q < q²`. The indicator is `z₀ − z₁`, a read of `V(1)` and not
of the label cell `y₀ ∈ H`. H-xiv holds: `c` is designated, and there is no herald or feedback.

**Instance II (one herald).** Same rule and ring. Designated: `y₀ = 0`, `x₁ = 0`, `y₁ = 0`,
`x₂ = c` (setting); uniform: `x₀ = w`, `x₃ = u`, `y₂`, `y₃`. `V = {y₀, x₀, x₁}`, `T = 1`, `t_p = 0`. Then
`V(0) = (0, w, 0)` and `V(1) = (w, u, w + c)`. A herald on `w` at tick 0 is held at use in `y₀(1)`, a
label cell. The effects read `(x₀(1), x₁(1)) = (u, w + c)`, so `Z₀ = (u, w)`. Unheralded, the law is
uniform; heralded on `w = a`, it is uniform on `(0, a) + (ℤ/q × {0})`. So `S* = ℤ/q × {0}`, every coset
is reached, the indicator is `z₁ − c₀`, and (SP) fails. H-xiv holds: `c` does not reach `V(0)`, so the
herald does not correlate with it.

***

## 6. Outcome

**PASS.** For every instance of the class (every rule of the gauge-derived affine class, every law in
`D_0`, every H-AR observer, every finite horizon and split), under (H3), the record class ((H4) or
(V-ii-H)) read with held-at-use herald typing and records formed inside `S`, C-PM, and H-xiv, the whole
operational witness is exhibited:
- a common coset-mixture description, with `S* = H(K ∩ ker G_{J*})` (N1, N4);
- every needed coset reached, by the joint herald `J*` (N3, N4);
- each coset's identity given by an available C-PM indicator effect that reads no preparation label
  (N5);
- the equivalence tests (N6).

Every P4 control is green (§5).

- Out-of-form preparations within the class: none (N7).
- In-form preparations with failed or unestablished checks: none.
- The mixed case of the safeguard does not arise. The partially retaining observers that r7
  anticipated as out of form are outside the class (N7, N8.2).

Under r7:328–332 and the instructed rule, the pass gives O-C for OBL-SP's fragment [W, P0;
unreviewed]: the prepare–measure fragment is simplex-embeddable for every instance of the class.

***

## 7. What the outcome does and does not imply

**For OBL-SP.**
- O-C holds at [W, P0], unreviewed. It is a one-direction statement (class ⇒ simplex-embeddable); no
  equivalence is claimed (§A.34).
- Its bearing is r7:362–366's, unchanged. Under (H3), the record class, held-at-use typing with
  records inside `S`, C-PM and H-xiv, no boundary condition of the `D_0` form gives a cell-aligned
  observer non-classical prepare–measure structure under the native rule.
- No content of OBL-SP remains open within its class.
- It does not reach:
  - non-additive observers (AW-OA2-1);
  - laws outside `D_0`, including μ-O and μ-R;
  - procedures for which H-xiv fails;
  - other herald typings (C7);
  - observers that do not retain every read inside `S` (C6);
  - non-affine rules (C2);
  - unbounded horizons (AW-OA2-2);
  - transformation noncontextuality.
- The pass does not derive composability from the dynamics. Composability is supplied by the
  record hypothesis under the typing (N3, N8.1).

**For the ordering rule (r7:303–311).**
- The case that applies is "P0 passes for the whole class": OBL-SP closes as O-C, subject to P4, all
  green. The next obligation named by the rule is AW-OA2-1 with the same φ, `D_0`, (H3), record class,
  herald typing, C-PM, H-xiv and (SP), and a non-additive read map.
- This record changes no priority or status. Under §A.46 item 7, the O-C may not serve as a premise
  until independently reviewed.

**Assumption-watch marker AW-P0-1.**
- Under held-at-use typing, `D_0`'s designated cells can serve as a herald register inside `S` while
  measurement-stage reads go unretained. The resulting fragment reproduces N4.2's
  preparation-contextual gbit, with records inside `S` (N8.2; a sketch, unreviewed).
- So any relaxation of (H4)/(V-ii-H) to "composites as far as the typing admits" re-admits a
  convention-type G3 pass. That pass is present for near-trivial dynamics and fails OA-2's Lemma 1
  (OA3:439–442, :445–449).
- The marker applies to AW-OA2-1, which carries the record class, and to any later treatment of C6.

***

## 8. §A.42 item 8: references to content off `main`

| Reference | Used where | Classification |
|---|---|---|
| `REC-1-r7.md` (blob `f1ffac0e`) at `9f7d2612`, branch `research/rec-1-1169-20261113`, draft PR #1268: P0, P4, the ordering rule, OBL-SP's class | §1, §2, §6, §7 | Support off `main` (the decision rule and class definition); a gap until landed. |
| `REC-1-REVIEW-r1.md` at `9f7d2612`: the reviewer's coset-space sketch | not used; N6 re-derives the construction | Provenance; credited as the earlier statement of the coset-space model. |
| `REC-1-RESPONSE-r1`…`-r6`, `REC-1-CONFIRM-r3`…`-r7` at `9f7d2612` | read for context | Provenance. |
| 3A:613–617 at `8228b3c2` (blob `7bbec04d`, PR #1267) | the remark naming the check | Provenance; no step rests on it. |
| 3A:595–612 at `8228b3c2` | read for context | Provenance. |
| OA1, OA2, OA3, S3, Main at `c3b5f37a` | R1–R7, N1–N8, controls | Support on `main`, as [R] (Main as manuscript); each input used is re-derived in §3. |
| #1169 c.6854241002 (authorization, as relayed) | header | Governance provenance; not re-fetched. |
| Owner-confirmed safeguard of 2026-11-13 (as relayed) | header, §6 | Governance provenance; not re-fetched. |
| [L] Spekkens et al. 2009; Schmid et al. 2021 | control (vi), N6 | External literature, context only. |
