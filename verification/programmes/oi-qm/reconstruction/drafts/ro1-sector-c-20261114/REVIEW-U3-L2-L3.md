# Independent review of the proposed lemmas L-2 and L-3 (S3-U3-r2)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U3-r2.md`
at `11734ce3`, blob `34ffe552` (the blob confirmed by `REVIEW-S3-U3-r2.md`). Lemmas: L-2 (§5.1,
ll. 602–676) and L-3 (§5.2, ll. 678–752). Context read: `REVIEW-S3-U3-r1.md`, `REVIEW-S3-U3-r2.md`,
`S3-U1-r5.md`, `S3-U2-r4.md` (L-1, for scope comparison only), TSI
(`oi-qm-ext-1/two-system-interface.md` at `75cc5100`, §§1–6), Main at `75cc5100` (ll. 385–389,
414–424, 480–484, 652).

**Remit.** #1169 c.6892563291, U3 Q2: an independent review of L-2 and L-3, with a literature check.

**Reviewer.** A non-author Claude reviewer. Paper-only: hand derivations and first-hand reading of
primary sources (arXiv texts; bibliographic data from Crossref). No computation, Lean, repository
edit, commit or GitHub post.

**Verdicts.**
- **L-2: PROVED AS STATED.** Measurable response maps are presupposed (automatic on finite
  configurations; `REVIEW-S3-U3-r2.md` N2). In substance it is a sharpened special case of a known
  result (Valentini 2002, §3 below).
- **L-3: PROVED AS STATED.** (k1) can be dropped. (b) needs only `|CHSH| > 2`. Its content is weaker
  than the words "source update" suggest: the dependence it forces can be supplied by a wing reading
  back its own first record (finding R3).

Required findings: R1–R3. Optional: O1–O6.

***

## 1. Re-derivations

### 1.1 L-2

**Setup.** `a = a(x,y,λ)` and `b = b(x,y,λ)` at both uses, with the same `λ` and the same maps. The
law of `λ` does not depend on the policy `((x₁,x₂),(y₁,y₂))`.

**Alice's wing.**
- Take Alice's policy `(x,x)`. Under Bob `(0,0)` her output pair is `(a(x,0,λ), a(x,0,λ))`. Under Bob
  `(0,1)` it is `(a(x,0,λ), a(x,1,λ))`.
- Both pairs are functions of one `λ` with one law. The event "entries equal" has probability 1 under
  the first. Equal laws give `P[a(x,0,λ) = a(x,1,λ)] = 1`.
- The same-register form reads the XOR: `0` against `a(x,0,λ) ⊕ a(x,1,λ)`, with the same conclusion.

**Bob's wing.** The mirror pairs give `b(0,y,λ) = b(1,y,λ)` a.s.

**Conclusion.** Intersect four full-measure sets. Then `a = α(x,λ)` and `b = β(y,λ)` a.s., and by
the pointwise bound (Main:385–389) `|CHSH| ≤ 2` after integration against the policy-independent
law. **Correct.**

**Equivalent reading.** Conditioning on `a(x,0,λ) = +1` selects a subensemble that contains no
`−1 → +1` transitions. Any transition set of positive measure therefore shifts Alice's second-output
ratio. This is Valentini's transition-set argument, with the subensemble prepared by the first use
(§3).

### 1.2 L-3

**First step.**
- Take Alice's policy `(x,x)` and Bob's policy `(y₁, y₂)` with `y₂` held constant.
- Repeatability in (9) gives `A₁(x,y₁,λ) = A₂(x,y₂,G(λ,ν,x))` a.s. for `y₁ = 0` and for `y₁ = 1`.
  Under (k4′) both statements hold on one probability space.
- The right side does not depend on `y₁`. So `A₁(x,0,λ) = A₁(x,1,λ)` a.s. **Correct.**

**Conclusions (a)–(c).**
- (a) is the contrapositive.
- (b) uses Bell's theorem (Main:389) against `|CHSH| > 2`.
- (c) uses the fairness in (9) at `x₂ ≠ x₁`: if `κ_A` were a function of `(x₁,y₁,a₁,b₁)`, then `a₂`
  would be determined by the records and the settings.

All three are **correct**.

**Instances.**
- TSI, case (U), Bob `(1,1)` with Alice `(0,1)`: `b₁ = R⊕C` and `b₂ = R⊕C⊕1`. Verified against
  TSI (3) and (7).
- Fresh replacement on Bob's wing: `P(b₂ = b₁) = 1/2`. Verified.
- The Bell-local wing `a = λ_x`. Verified.

**What (a) amounts to.** `a₁` and `b₁` are functions of `(x₁,y₁,λ)`. So "depends on the first
outputs or the remote first setting, given `(λ,ν)` and the own setting" reduces to dependence on the
remote first setting (N1 of `REVIEW-S3-U3-r2.md`). On a remote-dependent wing, the wing's *own* first
output already carries that dependence (`b₁` depends on `x₁`). Reading it back therefore meets (a).
R3 turns this into a construction.

## 2. Necessity of each hypothesis (hand countermodels)

"Necessary" means that dropping the hypothesis alone admits a model in which the other hypotheses and
the premise hold and the conclusion fails.

### 2.1 L-2

| Hyp. | Dropped | Countermodel or reason | Status |
|---|---|---|---|
| (k1) deterministic | stochastic responses with per-use **joint** noise | Trivial `λ`; `a_i = ε_i`, `b_i = ε_i ⊕ x_i y_i`, with `ε_i` fresh and fair. Every two-use history law is setting-blind, and CHSH = 4. After dilation this is fresh noise consumed, case (N) of §2.2 | necessary. With wing-local noise only, L-2 extends (O1) |
| (k1) binary | larger alphabets | The equal-law step is alphabet-free; only the CHSH form uses binary outputs | sufficient only |
| (k2) unchanged source | fresh cell per use | SEL-EXCL-1 §3: `a_i = r_i`, `b_i = r_i ⊕ x_i y_i`, with `r_i` independent. No signalling and CHSH = 4 | necessary |
| (k3) policy pairs executable | no two-use program (M-PR5, budget 1) | The premise is vacuous and `T` gives CHSH = 4 | necessary |
| (k3) mirror half | Alice-side pairs only | `T` (`a = r`, `b = r ⊕ xy`). Two-use set: every Alice policy with Bob `(0,0)`, and Alice `(0,0)` with every Bob policy. Bob's history is `(r,r)` whenever Alice varies, and Alice's history is always `(r,r)`, so the premise holds. Yet `b` depends on `x` at `y = 1` | necessary |
| (k4) S5 at policy level | policy-dependent law | `λ = (α₀,α₁,β₀,β₁)`, `a = α_x`, `b = β_y`, unchanged. Given `(x₁,y₁)`: `α_{x₁}` fair, `β_{y₁} = α_{x₁} ⊕ x₁y₁`, the other two independent and fair. Both two-use histories are setting-blind (checked case by case), and CHSH = 4. The locality clause holds; the CHSH clause fails | necessary for the CHSH clause |
| (k5) histories held jointly | per-use marginals only | `T` unchanged: every single output is fair whatever the remote policy, and CHSH = 4 | necessary |

The (k3) list is sufficient, not minimal. For each `x` it suffices to have Alice `(x,x)` with one Bob
policy that repeats a setting and one that shares a coordinate with it and changes the other: `(y,y)`
with `(y,y′)` or with `(y′,y)`. A pair `(0,1)` against `(1,0)` does not suffice: `a₀ = λ` and
`a₁ = 1 − λ`, with `λ` fair, gives equal laws.

### 2.2 L-3

| Hyp. | Dropped | Countermodel or reason | Status |
|---|---|---|---|
| (k1) deterministic | stochastic, with policy-independent noise | Dilate: write each kernel as a function of `(x, y, λ, ε)` with `ε` uniform, and put all noise into `(λ,ν)`. (k4′) survives, and the proof applies to the dilation. A `κ_A` that reads first-use noise is a function of the dilated `λ`, so it is excluded as well | **not needed**: L-3 holds without it (O1) |
| (k3′) both `y₁` at a common `y₂` | only repeated-setting policies `(x,x)`, `(y,y)` executable | TSI's candidate, unchanged (U): `a₂ = R = a₁` and `b₂ = R ⊕ x₂y₂ ⊕ C = b₁` when `(x₂,y₂) = (x₁,y₁)` (TSI (7)). (1)×(9), restricted to those policies, holds exactly. The remote-dependent wing reuses an unchanged source, because `B₂`'s dependence on `x₂ = x₁` mimics dependence on `x₁` | necessary |
| (k4′) S5 | policy-dependent law | The (k4) model of §2.1 with `P(α_{x₁} ⊕ β_{y₁} = x₁y₁) = cos²(π/8)`. Then (1)×(9) holds **exactly**, both wings are Bell-local, and the source is unchanged (U). (b) fails | necessary |
| (k5′) / `Θ`: `a₁, a₂` held jointly | per-tick marginals | Repeatability is a joint statement. Fresh replacement (N) has every per-tick single-wing marginal fair, as (1)×(9) does | necessary |
| herald clause | setting-dependent acceptance | `λ` uniform on the 16 local tables, unchanged (U). Accept with probability 1 if `α_x ⊕ β_y = xy` at the first settings, else with probability `(1−c)/c`, where `c = cos²(π/8)`. The success branch is (1)×(9), with repeatability automatic | necessary |
| (1) at `2√2` | any `|CHSH| > 2` | (b) uses only `|CHSH| > 2` | sufficient only (O3) |
| full (9) | repeatability on one wing, at the (k3′) pairs | (a) uses only this. (c) uses only fairness at a changed setting | sufficient only (O3) |

## 3. Literature check (first-hand, arXiv texts)

| Source | What it states (read first-hand) | Bearing |
|---|---|---|
| A. Valentini, "Signal-locality in hidden-variables theories", Phys. Lett. A **297**, 273–278 (2002), doi:10.1016/S0375-9601(02)00438-3; arXiv quant-ph/0106098 | "all deterministic hidden-variables theories, that reproduce quantum theory for a 'quantum equilibrium' distribution of hidden variables, predict the existence of instantaneous signals at the statistical level for hypothetical 'nonequilibrium ensembles'". The proof uses transition sets `T_A(+,−)` and `T_A(−,+)` and gives a signal "in general". "Bell's theorem guarantees that at least one of the pairs … has non-zero equilibrium measure" | **L-2 is a sharpened special case.** Reuse prepares the nonequilibrium subensemble `{a(x,0,λ) = ±1}` operationally. On that subensemble the signal is guaranteed, not generic, and no quantum equilibrium law is assumed. §4.2's elementary step is the quoted remark (Bell 1964). No conflict |
| R. Silva, N. Gisin, Y. Guryanova, S. Popescu, PRL **114**, 250401 (2015); arXiv 1408.2272 | Quantum sequential Bobs. `I⁽²⁾_CHSH = 2(1+F)`, so a strong first measurement (`F = 0`) leaves Bob₂ at 2. Monogamy results "assume no-signalling between all parties, while in our scenario Bob1 implicitly signals to Bob2" | Quantum, not hidden-variable. Consistent with (9). Neither lemma appears in it. No conflict |
| F. J. Curchod et al., PRA **95**, 020102 (2017); arXiv 1510.03394 | "if B1 performs a projective measurement on the shared entangled state, the resulting post-measurement state … is separable". Outcome `bᵢ` "can depend only on variables produced in its past" | Consistent with (9). Non-projective sequences lie outside L-3 (L-3 Scope, l. 748) |
| P. J. Brown, R. Colbeck, PRL **125**, 090401 (2020); arXiv 2003.12105 | Arbitrarily many independent Bobs with unsharp measurements can each have an expected CHSH violation | Outside L-3: non-repeatable instruments. These laws are further coverage targets that RQ-UPD-2 does not address. No conflict |
| R. Gallego et al., "Nonlocality in sequential correlation scenarios", NJP **16**, 033037 (2014); arXiv 1308.0477 | Time-ordered local models: "The response of one party for its i-th measurement should depend only on the given hidden variable λ, the first i measurement settings and the first i − 1 measurement outcomes of that party" | That causal structure is the wing-local readback of R3. L-3 forces own-history dependence only on a remote-dependent wing. Compatible |
| M. Kleinmann et al., "Memory cost of quantum contextuality", NJP **13**, 113011 (2011); arXiv 1007.3650, App. A | A set of repeated measurements `Q_repeat`: "the constraints from Qrepeat require that γ has the same values in S1 and S2"; "a two-state automaton cannot obey both, Qrc and Qrepeat" | Same type of argument: repeatability forces an internal-state change. L-3 is its Bell-wing analogue. No conflict |
| S. Teufel et al., PRA **56**, 1217 (1997); arXiv quant-ph/9609005 (abstract and §1 read) | Local causal hidden-variable models for sequences of measurements (LCHV_N) | Context only |
| T. Fritz, NJP **12**, 083055 (2010); C. Budroni, G. Fagundes, M. Kleinmann, NJP **21**, 093018 (2019) (abstracts read) | Temporal CHSH; memory cost of temporal correlations | Context only |

**Novelty.**
- L-2: not new in substance. It is Valentini's signal-locality mechanism with the subensemble
  selected by the first outcome, which removes "in general" and the quantum-equilibrium premise.
- L-3: not found stated in this form in the sources read. It is an elementary combination of Bell's
  theorem with the repeatability-forces-memory argument.
- No source read conflicts with either lemma.

**Limits.**
- Read: arXiv versions only. Journal references from Crossref.
- Not read: Popescu, PRL **74**, 2619 (1995), which is not accessible here.
- The search was not exhaustive.

## 4. Marking of uses, and claim/evidence boundary

Every use of L-2 and L-3 carries "conditional on L-2" or "conditional on L-3" (the marking audit of
`REVIEW-S3-U3-r2.md` §3 was re-checked at blob `34ffe552`). L-1 supports nothing. No verdict rests on
either lemma unconditionally. L-3's necessity/sufficiency boundary is stated (l. 752). Three defects
remain.

**R1 (required): "every … realization" outruns L-2's hypotheses.** These sites state L-2's
conclusion for every Bell-violating unchanged-source realization, or whenever `Δ₄` is available.
L-2 needs (k3), (k4) and (k5), and U3 itself records that M-PR5 lies outside (k3) (l. 667). Read
literally, M-PR5 is a counterexample.
- RQ-REU, ll. 367–368 ("whenever `Δ₄` is available"; `Δ₄` does not supply the (k3) pairs or (k4));
- RQ-UPD-1, ll. 373–376;
- §4.1, ll. 479–480;
- U3-1, l. 854;
- §10.2, RR-1 row, l. 934;
- CQ-2, ll. 969–972 (it names `Θ` but not (k3) or (k4)).

Safe path: write "conditional on L-2, for realizations meeting (k1)–(k5)", or name (k3) and (k4)
explicitly. Under §1 (S5 not assumed) the (k4) exposure must be visible at each site.

**R2 (required): the prior-art status of L-2.**
- U3-1 classes L-2's general statement as NEW (l. 854).
- §1 ll. 174–176, §5.1 l. 607 and §10.6 ll. 1022–1023 say the literature was not searched.

Safe path: cite Valentini 2002 at §5.1, state L-2 as a sharpened special case, and reclass U3-1's L-2
part (ELABORATING against the literature; new only relative to the corpus). The lemma's proof and its
uses are unaffected.

**R3 (required): the update L-3 forces can be wing-local readback, and designed realizations
exist.**

*The construction* [reviewer, hand].
- `λ = (R, C, f_A, f_B)`, policy-independent: `R`, `f_A`, `f_B` fair; `C ~ w_{η*}` (TSI (2), (5));
  all four independent.
- First use, as in TSI: `a₁ = R`, `b₁ = R ⊕ x₁y₁ ⊕ C`.
- Second use: `a₂ = a₁` if `x₂ = x₁`, else `f_A`; `b₂ = b₁` if `y₂ = y₁`, else `f_B`.

*Check against (1)×(9).*
- The first use reproduces (1).
- At a repeated setting, `a₂ = a₁` and `b₂ = b₁`.
- At a changed setting, `f_A` and `f_B` are fair and independent of the first outputs and of each
  other.
- So the record law is (1)×(9) exactly. Both complete local histories are blind to the remote
  settings.

*What it shows.* Each wing reads only its own first record (`x₁, a₁` or `y₁, b₁`) and a preloaded bit.
- Bob's content depends on `b₁`, so the wing meets L-3 (a).
- `f_A` and `f_B` meet (c), booked in `μ`.
- So L-3 shows that the remote-dependent wing must consult its own first record, or equivalent
  information. It does not show that a cross-wing or hidden-sector update is required.
- Main's comb, the intervention-dilation theorem (Main:480–482 [M]), also realizes any finite
  action-labelled law with history-indexed responses. It is centralized, and U1 K-4 classes it as
  representable only (U1:819).

*Required at three sites.*
- In §5.2 Scope and RQ-UPD-2 (i), state that (a) can be met by readback of the wing's own first
  record.
- In §10.1's RQ-UPD row, narrow "no source-update process on record for any realization" to
  executed or native processes, and cite Main:480–482 at its K-4 standing.
- In §10.6, read "a deterministic realization of QR-1 meeting RQ-UPD-2" as a native or executed one;
  a designed one is elementary.

§2.2's "where that content is hidden" (ll. 230–232) is already conditional and needs no change.

**Optional.**
- **O1.** L-3 holds without (k1), by dilation (§2.2). L-2 needs (k1) against joint per-use noise. It
  extends to wing-local per-use noise if Bob `(1,1)` against `(1,0)` is added to (k3): equal laws give
  `E[p₀²] = E[p₀p₁] = E[p₁²]`, hence `p₀ = p₁` a.s.
- **O2.** (k3)'s mirror clause "(Alice `(0,0)` or `(0,1)`, Bob `(y,y)`)" means both pairs; say
  "and". A weaker sufficient list is given in §2.1.
- **O3.** (b) needs only `|CHSH| > 2`, and (a) needs only repeatability on that wing at the (k3′)
  pairs. Stating this widens L-3 to every Bell-violating table with repeatable reads.
- **O4.** Name (k3′) at RQ-UPD-2 (ll. 382–384) and in U3-2. "`Θ` identifies with that two-use
  experiment" implies (k3′) only if `Θ` covers all sixteen sequences, and §2.2's countermodel shows
  that it matters.
- **O5.** State measurability once (carried over from `REVIEW-S3-U3-r2.md` N2).
- **O6.** U3-2 (NEW): L-3 is new relative to the corpus. Against the literature it is the Bell-wing
  form of a known repeatability argument (Kleinmann et al., App. A). After R3, consider ELABORATING.

**Other boundary checks, all passed.**
- Witness → theorem: both lemmas have general proofs, and the TSI and `T` cases are labelled as
  instances.
- Finite → universal: none.
- Necessary → sufficient: L-3, l. 752, is explicit.
- Conditional → unconditional: R1 only.
- Ambient → native: none. The elementary step uses Main's own Bell theorem at [M].

## 5. Checked, and not checked

**Checked:**
- both proofs, line by line;
- the instances against TSI (3), (7), (9), (10) and `T`;
- one countermodel per hypothesis (§2);
- the marking sites of both lemmas;
- Main:385–389, :480–482 and :652, and U1:819;
- the eight sources in §3, first-hand.

**Not checked:**
- L-1's repair;
- performed sequential experiments (owner question 4);
- journal versions of the papers;
- Popescu 1995;
- parts of U3 that do not use L-2 or L-3.
