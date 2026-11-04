# PR-AUDIT-1 — LA-EQUAL and MR-1 N5: consolidated read-only proof review

**Date:** 2026-11-04. **Object:** the `LA-EQUAL` token, informativeness `EMPTY`, of #1009's
setting-conditioned later-access unit
(`verification/programmes/substratum/continuous-substates/later-access-preregistration.md`,
`later-access-result.md`, `later-access-result.json`, `native_later_access_probe.py`), and its use as
item N5 of MR-1's frozen preregistration (`preregistration.md:109–111` in this directory).

**Reviews.** Three read-only reviews of the same object were made separately on 2026-11-04;
reviews 1 and 2 are recorded below in full:

- **Review 1:** ChatGPT (GPT-6), at the owner's request.
- **Review 2:** a read-only review agent coordinated by the Claude Code session that drafted the
  2026-11-04 status notes. It read `main` at `449b8fa8e732995798b7cbca473cf38b57a037fa`.
- **Review 3:** a separate read-only agent, coordinated by the same session, that re-reviewed this
  consolidation and review 2's new claims and checked whether an existing result closes the gap.
  Its findings are incorporated in the consolidated assessment below.

All three are model-authored. None is an authenticated human or external review, and together they
do not discharge AGENTS.md §A.46 item 7. None ran a probe, numerical experiment or Lean build (review 3 ran only the repository's
`legacy_records_check.py` and `duplicate_check.py`),
and no frozen record is changed. Recorded check results are taken from `later-access-result.json`
without re-running them. An earlier confirmation of the token posted on #1009 was not relied on.

## Consolidated assessment

### 1. Proof validity: partially verified

- **Established, conditionally.** Under H-prior, H-access, H-rule and H-torus, with the recorded
  exact checks P1–P5 and P6a (H-inventory enters for consistency of the prior with the preparation):
  the passive read of the eight public ports over `L+6 … 2L` adds no setting dependence. The tail is
  uniform and independent of the earlier keys, so `EMPTY` holds, and for every `k0`, including `⊥`,
  `TV_win(k0)` and `TV_acc(k0)` of the window equal those of its pre-tail part. Reviews 1 and 2 accept
  this triangular argument (review 1, §A; review 2, §1.2, steps S1–S6). The argument is not written
  out in the LA files; the probe inserts the zero TV values once P1–P6b hold
  (`native_later_access_probe.py:1186–1193`; `later-access-result.md:25–27`).
- **Not established: `LA-EQUAL` itself.** Equality of the full window laws across the two setting
  values also needs the pre-tail (pre-cut) law to be the same for both values. Reviews 1 and 2 locate
  the gap here (review 1, §A, "Missing bridge"; review 2, §1.3); review 3 concurs.
  - Review 2 identifies the mechanism. The setting bit re-enters port 5's accessible record two ticks
    after `R`: the A-component of `U_{S+6}(p5)` is `R.A ⊕ Σ.B`. It is masked if the pre-cut
    port-5 frontier triples `f_5(t)`, `S+4 < t ≤ L+3`, are uniform and independent; no weaker
    condition is examined. Review 3 confirmed this channel by hand. H-prior as
    displayed (`later-access-preregistration.md:151`) constrains `(η, β)` given `D′` and not those
    triples, which lie in `D′`. The CP-PRECUT control does not cover this channel
    (`native_later_access_probe.py:1136–1153`).
  - The 42-key law, the parent's forward kernel and the tail argument do not by themselves give the
    pre-tail equality: the 42-key law is conditional on the other variables
    (`native-random-setting-test.md:88`) and leaves their law free; for fixed `D` the pre-cut history
    is a function of `r` (`:122–123`); the kernel is conditional on the public past
    (`:109–110`), and the tail argument covers `β` only (review 3).
  - Review 3 identifies an existing route. H-prior's sourcing sentence
    (`later-access-preregistration.md:153–154`) names the source of those triples, the history_v11
    bank (`native-y-continuation-20261024/history_v11/REPORT.md:23–25`, `:41`). Under that law the
    whole port word through `L+3`, `R` included, is uniform given the bank complement (`:110–112`),
    which, by review 3's hand argument, gives the pre-cut equality. That argument is not recorded as a
    check. The history_v11 result is itself a written paper theorem ("written conditional
    finite-horizon theorem", `history_v11/REPORT.md:4–5`) with a separate-agent internal review
    (`history_v11/review/REPORT.md`), not an independent review on `main`. The LA files state neither that law as a hypothesis nor this step.
  - The equality also rests on the parent unit's forward-kernel result
    (`native-random-setting-test.md:95–112`), a paper proof that "awaits its own independent review"
    (`:3–5`); its acceptance on #1009 (`later-access-preregistration.md:5`) is author-reported
    (`continuous-substates/README.md:12–17`). That unit conditions on the whole public past, which
    contains `R` (`native-random-setting-test.md:118–127`), and the
    LA preregistration bars using equality after a fixed history in place of equality of the
    history masses (`later-access-preregistration.md:139–140`).
  - Review 2 sketches a closure: with H-prior strengthened to include those frontier triples jointly
    with `η` and `β`, and the parent kernel accepted, the reconstructed proof gives `LA-EQUAL`. That
    closure is hand arithmetic in review 2, not a recorded check, and is not verified here.
- The finding is a missing proof, not a counterexample. Whether the pre-cut law actually depends on
  the setting for some admissible law of `D′` is not determined.

### 2. Hypothesis sourcing: none derived for native OI

- **H-prior** is a stipulated joint uniform prior, supplied as a resource extension
  (`native-y-continuation-20261024/history_v11/REPORT.md:23–27`), and is load-bearing: a correlated
  prior gives `TV_win = 1/8` (CP-PRIOR, `later-access-result.md:60`).
- **H-inventory** is a declared completeness condition of the construction, not a derived fact.
- **H-access** is the retained eight-port passive, non-writing read convention; it is not adopted
  as a physical OI access law (`later-access-preregistration.md:68–75`).
- **H-rule** is the native-Y model rule `H(A,B,D) = (B, D, A ⊕ BD)`. It is bijective, but it is not
  the corpus's selected substratum dynamics: center independence, isotropy and linearity select the
  linear wave rule (`papers/SM.md:224`), and `H` is nonlinear.
- **H-torus** is a construction parameter, measured exactly on the recorded geometry by P5.
- **The pre-cut port-5 bank law** named in §1 is used by the closure route identified and is not
  among the five hypotheses as displayed. H-prior's sourcing sentence names its source, the
  history_v11 bank, which is stipulated in the same way ("supplied assumptions rather than derived
  physical laws", `history_v11/REPORT.md:23–27`).

A valid conditional proof does not establish its hypotheses.

### 3. Support for MR-1 N5: partial

- `EMPTY` is supported as N5 states it.
- `LA-EQUAL` is not established under the five hypotheses N5 lists: its written route uses, in addition, the
  pre-cut port-5 bank law and the parent unit's forward-kernel result.
- N5 is not wider than the established result on ports, horizon or read. It is incomplete on its
  hypothesis list.
- N5's own text omits that it concerns the native-Y rule; MR★ supplies that qualifier
  (`amendments/MR-star.md:668`). The LA licence also excludes other settings, carriers and
  dictionaries and adaptive operations (`later-access-preregistration.md:266–272`).
- MR-1 does not use N5 more strongly than it states it, and no MR-1 outcome depends on it (review 2,
  §3). Under §A.46 item 7, N5 is not usable as a premise of an established claim.

**Overall: partially verified.** The tail independence and `EMPTY` are conditionally supported. The
full `LA-EQUAL` equality is not established from the stated hypotheses.

### Where the reviews differ

Their overall verdicts and the location of the gap agree. Review 2 adds three points that this
consolidated assessment adopts:

- the specific re-entry channel and the bank law its closure uses;
- the dependence on the parent unit's unreviewed forward-kernel proof;
- that H-rule is not the corpus's selected linear rule.

Review 1, §C, reads N5 as accurately reporting #1009's scoped output. The consolidated reading is
that N5 is accurate on ports, horizon and read but incomplete on its hypothesis list.

Review 3 confirms review 2's channel and closure inequalities by hand, and identifies the existing
history_v11 noise-word result as a closure route under the bank law H-prior's sourcing already
names. Review 1 (§A) noted that "a complete proof may be possible from the full chronological
bank construction plus the 42-key factorization". The three verdicts are unchanged: the gap is a missing written composition
under a named but undisplayed stipulation, together with the unreviewed parent kernel.

### Ownership

The proof gap belongs to SUBSTATE-1 (#1007), and its consequence for MR-1 N5 to #866. Both remain
scientifically open.

## Review 1 (ChatGPT, GPT-6)

Recorded as written. Paths are relative to the repository root.

**Disposition: GAP for independently establishing the full LA-EQUAL claim.**
The conditional tail-independence step has a coherent triangular argument, but
the reviewed sources do not establish one additional equality needed to conclude
equality of the **complete** joint history under both setting values. This finding
is a missing-proof finding, **not a counterexample** and not a finding that the
reported LA-EQUAL token is false.

### Sources read (paths relative to repository root)

- `verification/programmes/substratum/continuous-substates/later-access-preregistration.md`,
  especially lines 61–75, 117–168, 170–207 and 348–379.
- `verification/programmes/substratum/continuous-substates/later-access-result.md`,
  especially lines 10–33 and 83–99.
- `verification/programmes/substratum/continuous-substates/native_later_access_probe.py`,
  especially lines 1136–1153 and 1182–1204 (decision rule).
- `verification/programmes/substratum/continuous-substates/native-random-setting-test.md`,
  especially lines 67–116 and 118–150.
- `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/history_v11/REPORT.md`,
  especially lines 91–129 (chronological inversion under supplied independent bank).
- Frozen `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md`,
  especially N5 at lines 109–111. The frozen file has not been changed.

### A. Proof validity — PARTIALLY VERIFIED; full claim has a GAP

Let `c=R.A`, `Y` denote all pre-tail coordinates of the comparison window,
including the complete pre-cut public history with `R.A` removed, the incoming
packet, the two subsequent packet slices, and the two recorded increments.
Let `T=Tail`. The comparison keeps unnormalized masses for each `K0=k0`
(including `k0=⊥`).

Under H-prior and the exclusion/order/permutation properties P1–P6b,
the first-arrival triangular mechanism implies that for each fixed original
complement and the earlier 42 keys, the complete tail-output word is a
bijective image of fresh uniform tail-bank triples. Its conditional law is
therefore uniform and does not depend on earlier key, setting or packet
labels. This step has a recognizable argument using the explicit
`v ↦ α XOR H(v XOR β)` permutation and chronological ordering
(`history_v11/REPORT.md:91–108`; `later-access-preregistration.md:178–198`).
It supports the conditional `EMPTY` reading, given the supplied joint prior
and the declared access. The local P6b control is not itself a universal-scale
proof, and no Lean certification is claimed.

**Missing bridge:** the complete-history result `μ_0^k0=μ_1^k0` needs
equality of the *pre-tail* law as well. Tail freshness alone gives, for
each compatible `y,t,c`,

    Pr(Y=y, T=t | R.A=c) = Pr(Y=y | R.A=c) / 8^m

where `m=8(H*−L−5)`. Equality across `c` thus additionally requires

    Pr(Y=y | R.A=0) = Pr(Y=y | R.A=1)

with the same incoming-packet and terminal-branch mass conventions.
This equality is not an automatic consequence of tail-bank freshness.

The earlier port-5 note establishes a setting-independent **future
record/carrier kernel conditional on the full public history**
(`native-random-setting-test.md:109–114`); it does not by itself
establish equality of the full **pre-cut public-history distribution**
after omitting `R.A`. That note explicitly retains and conditions on
`Wτ`, which contains `R` (`:118–127`). The LA probe's
`CP-PRECUT` checks a *small fixture* plus geometric exclusions
(`native_later_access_probe.py:1136–1153`); it does not calculate or
prove this joint equality for the astronomical original preparation.

A complete proof may be possible from the full chronological bank
construction plus the 42-key factorization, but the missing composition
and conditioning step must be supplied and checked. The existing
`LA-EQUAL` token is generated from passing P1–P6b and controls, with
full-TV zero inserted as proof-derived, not enumerated
(`native_later_access_probe.py:1182–1193`).
Therefore its green controls cannot close this paper-proof gap.

### B. Assumption sourcing — PARTIAL; not derived from OI alone

| Hypothesis | Standing in the reviewed sources |
| --- | --- |
| H-prior | Explicit **joint** conditional product/uniform law of the original 42 keys and tail bank. Stipulated; separate marginal source laws do not imply it (`later-access-preregistration.md:147–157`). |
| H-inventory | Completeness of original sources/readiness/bank inventory is declared, not a proof that no further physical interaction or source exists (`:159–163`, `:79–98`). |
| H-access | Retained candidate eight-port passive/read-stop convention, with non-writing read stipulated, **not adopted as a physical OI access law** (`:61–75`). |
| H-rule | The chosen native reversible rule `H(A,B,D)=(B,D,A XOR BD)`, checked for the pinned interface; it is a declared dynamics input (`:164`). |
| H-torus | No-wrap and coordinate-span inequalities checked for this finite window; this is conditional geometry, not a sourced experimental horizon (`:165–168`, P5). |

The theorem cannot be read as deriving preparation, access, inventory
completeness or native measurement control from OI alone.

### C. Frozen MR-1 N5 — PARTIALLY SUPPORTED, NOT ESTABLISHED

N5 accurately **reports** #1009's scoped output:
`LA-EQUAL`, `EMPTY`, the passive read of eight public ports through
`H*=2L`, under all five named hypotheses
(`measurement-record-formation/preregistration.md:109–111`).
Its limitations on active coupling and outgoing environment are proper.

However the full joint-law equality underlying the token has the
unclosed proof bridge in section A, and the hypotheses are not all sourced
as available physical OI operations. N5 is therefore **not verified as an
established scientific result** by this review. It remains a accurately
scoped historical research result with an explicit proof gap. No frozen
MR-1 text, negative-result classification, or manuscript conclusion is
changed.

**Disposition and ownership:** This finishes the *read-only review task*
within administrative #1088. The underlying scientific proof gap belongs
to the pre-existing SUBSTATE-1 scientific owner #1007, and the impact on
MR-1 N5 belongs to #866. They remain scientifically open; closing #1088
must not imply that the gap was proven away. Do not adopt the premise,
or certify complete operational QM, on this record.

## Review 2 (read-only review agent)

Recorded with headings demoted one level and some lists reflowed as prose; its findings are unchanged. All references are to `main` at
`449b8fa8e732995798b7cbca473cf38b57a037fa`. `CS/` = `verification/programmes/substratum/continuous-substates/`,
`NY/` = `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`,
`MR/` = `verification/programmes/oi-qm/reconstruction/measurement-record-formation/`.

### Scope and sources

The review was read-only; no probe, script, Lean build or new computation was run. Object identity
was checked with `git rev-parse` on blobs: `CS/later-access-preregistration.md` has blob `41ac4d05…`
at `b532472a`, at `8af2d904` and on `main`; `later-access-result.md`, `later-access-result.json` and
`native_later_access_probe.py` have the same blobs at `8af2d904` and on `main`. The recorded JSON's
fields were read with a JSON reader and not regenerated. Every other step below is hand algebra or
arithmetic on recorded coordinates.

Files read: the preregistration, the result note and JSON, and the probe; the parent unit
`CS/native-random-setting-test.md` and its probe; `NY/history_v11/REPORT.md` and its review;
`NY/native_vread_v15/REPORT.md` and `checks.py` (the `PORTS` list and constants);
`NY/shared_v12/INTERFACE-CONTRACT.md`, `NY/CURRENT-HANDOFF.md` and `NY/junction_v4/review/REPORT.md`;
`CS/README.md`; MR-1's preregistration, README and amendments; and, for §A.19 sourcing,
`papers/SM.md`, `papers/Substratum.md` and `papers/Explainer.md`.

### 1 Proof validity

#### 1.1 Where the proof is

The decision rule says LA-EQUAL "is decided by a written chronological-triangular proof"
(`CS/later-access-preregistration.md:172–174`); under the hypotheses "the written proof then gives
mu_0^k0 = mu_1^k0 exactly for every k0" (`:205–207`); and EMPTY "is computed from the same
triangular proof" (`:253–254`). `CS/README.md:25–26` locates the proof at
`later-access-preregistration.md:173`.

Neither the preregistration nor the result note writes out the proof's steps. The probe hard-codes
the zero TV values and `EMPTY` once P1–P6b hold (`CS/native_later_access_probe.py:1186–1193`), as
the result note says (`CS/later-access-result.md:25–27`). The only stated pieces are the EMPTY sketch
at `later-access-result.md:29–31`, a code comment at `native_later_access_probe.py:1189–1190`, and the
JSON basis strings (`:1310–1311`, `:1320`). The template the proof follows is written elsewhere:
`NY/history_v11/REPORT.md:91–124` (bank-to-noise triangular inversion) and
`CS/native-random-setting-test.md:79–84`, `:95–112` (the 42-key triangular law). The argument was
therefore reconstructed and checked step by step.

#### 1.2 Reconstruction

Notation: β is the tail bank, `f_i(t)` for `L+6 ≤ t ≤ 2L`, with `8(L−5)` triples; η is the 42 keys;
D′ is every other original variable (`:147–151`); W is the pre-tail window object
`(R.B, R.D, W_τ∖R, K0, K1, K2, ΔW1, ΔW2)`, so that `X = (W, Tail)` (`:117–119`); `c = R.A`.

- **S1. Diagonal permutation.** Under the rule `U_{t+1}(v) = U_{t−1}(v) ⊕ H(⊕_{w∼v} U_t(w))`, with H
  bijective, suppose `f_i(t)` lies at axial distance exactly t from `p_i` on the unwrapped lattice.
  Then `U_t(p_i)`, for fixed values of all other initial variables, is a bijection of `f_i(t)`: along
  the axial path only the preceding vertex can depend on `f_i(t)` at each first-arrival step, and the
  step is `v ↦ α ⊕ H(v ⊕ β)`. This is the argument of `NY/history_v11/REPORT.md:98–108`. Its inputs
  are H-rule, P6a (H bijective), the axial own path (P1) and no wrap (P5). P6b (`:194–198`) is a
  sampled mechanism check and is not needed for this paper step.
- **S2. Chronological triangularity.** Tail coordinate `(t, i)` depends only on initial cells within
  distance t of `p_i`. For `f_j(t′)` with `j ≠ i`, P1 gives `dist(f_j(t′), p_i) ≥ t′`. A tail bank
  triple that influences `(t, i)` therefore has `t′ < t`, or `t′ = t` with an equal-time edge `j→i`;
  P4 restricts such edges to 2→5 and 3→5, which the `(t, i)` order places earlier. So `β ↦ Tail` is
  triangular with S1's bijections on the diagonal. Valid from P1 and P4.
- **S3. Tail uniform.** P3 makes the `8(L−5)` tail bank cells distinct and disjoint from η, the
  sources and the balls, so `|Tail| = |β|`. For fixed `(D′, η)`, `β ↦ Tail` is then a bijection of
  `8^{|β|}` words, and H-prior gives `Pr(Tail = y | D′, η) = 8^{−8(L−5)}`. Valid.
- **S4. W does not depend on β.** P2 states `dist(f_i(t), cell) > time` for every pre-cut record and
  every K0/K1/K2/ΔW label (`:181–186`). So W, and `c = R.A`, are functions of `(D′, η)`. Valid.
- **S5. Factorization.** From S3 and S4, for every k0 including ⊥,
  `μ_c^{k0}(w, y) = Pr(W = w, K0 = k0 | c) · 8^{−8(L−5)}`. The TV values of X therefore equal those of
  W: `TV_win(k0) = TV(ν_0^{k0}, ν_1^{k0})`, and likewise for `TV_acc`, where `ν_c^{k0}` is W's
  unnormalized law at k0. The tail adds no setting dependence. A stop rule on `A(X)`-prefixes is a
  function of `A(X)`, so TV cannot increase. Valid.
- **S6. EMPTY.** By S3, Tail is independent of `(D′, η)`, hence of `(η, K0, K1, K2)` given D′, since
  the K labels are functions of `(D′, η)` by S4. This matches the definition at `:252` and
  `later-access-result.md:29–31`. Valid under H-prior, H-rule and H-torus, with P1–P5 and P6a. It
  does not use the parent unit.
- **S7. Setting-equality of W.** LA-EQUAL needs `ν_0^{k0} = ν_1^{k0}`. The LA documents do not
  derive this; they take it from the parent unit (`:14–16`). It splits into two parts:
  - **(a) The forward kernel.** The parent claims
    `Pr(K1, K2, ΔW1, ΔW2 | K0, W_τ, R) = 8^{−28} S(k0,k1) S(k1,k2)`, the same for every r
    (`CS/native-random-setting-test.md:95–112`). Its structure (28 future keys, triangular, with
    bijective diagonals) is consistent with the parent probe's geometry checks
    (`CS/native_random_setting_probe.py:71–82`, `:96–100`). The parent's written proof "awaits its
    own independent review" (`native-random-setting-test.md:3–5`; `CS/README.md:22–28`).
  - **(b) Pre-cut masses.** It must also hold that `Pr(R.B, R.D, W_τ∖R, K0 | c)` does not depend on
    c. The parent establishes `R ⫫ K0` (`:47–52`). It does not establish that `W_τ∖R` is independent
    of R: it states that "For fixed D the pre-cut history is a function of r" (`:122–123`) and
    compares kernels "at the same incoming packet" conditional on `W_τ` (`:23–25`, `:109`). The LA
    preregistration explicitly bars that substitution: "equality after a fixed history is not used in
    place of equality of the history masses" (`:139–140`).

#### 1.3 The gap at S7(b)

`W_τ` is the whole public past (`native-random-setting-test.md:20`; LA access `:33–35`). The probe
treats the port streams through `L+3` as pre-cut records (`native_later_access_probe.py:224`;
`later-access-result.md:103–104`).

The setting source is `b5 = f_5(S+4) = (0, 2S+4, 0)` (`native-random-setting-test.md:40`), at
distance `S+4` from `p5 = (0, S, 0)`. From the coordinates in `NY/native_vread_v15/checks.py:377–380`
and `NY/history_v11/REPORT.md:34–43`, a hand calculation shows that b5's cone reaches no other port,
the herald, the q9/V cells or the flags before `L+3`. It does reach port 5's own stream after `S+4`.

By the parity of the second-order rule, `U_t(p)` depends on `U_0(x)` only if `dist(x, p) ≡ t (mod 2)`,
as the parent probe also uses (`:105–111`). The affected ticks are therefore `t = S+6, S+8, …, L+3`,
38 ticks. At the first of them, exactly from the rule (`native_later_access_probe.py:438–440`):

    U_{S+6}(p5) = U_{S+4}(p5) ⊕ H(Σ),  Σ = ⊕_{w∼p5} U_{S+5}(w),
    so its A-component = R.A ⊕ Σ.B     (H(A,B,D) = (B, D, A⊕BD)).

The setting bit therefore re-enters the accessible record two ticks after R. It is masked when Σ is
uniform and independent of R. That holds if the bank triple `f_5(S+6) = (0, 2S+6, 0)` is uniform and
independent of the other variables, because it arrives at `p5+e_y` at `S+5` as a first-front
permutation. `f_5(S+6)` is in neither η nor β, so it belongs to D′. H-prior as displayed (`:151`)
constrains only the conditional law of `(η, β)` given D′ and places no constraint on D′'s law; a
point-mass D′, for example, is consistent with it.

Under the five hypotheses as written, then, the c-independence of the pre-cut masses is not derived.
Its proof requires the uniform independence of the pre-cut port-5 frontier triples `f_5(t)`,
`S+4 < t ≤ L+3`. These are history_v11 bank triples (`NY/history_v11/REPORT.md:41`, `:45`, `:23–25`).
H-prior's sourcing sentence names that bank (`:153–154`), but its displayed equation does not include
it. No computation was run to settle whether a dependence actually arises for a particular D′ law.

The control named for this step does not cover it. The CP-PRECUT row claims "use-cut independence
re-measured, not assumed" (`:375`). At actual scale the probe measures only three exclusions: b5 from
the K0 slices (margin 1), the incoming keys from R, and b5 from q9/V
(`native_later_access_probe.py:1144–1150`; JSON `CP-PRECUT`). On the toy fixture it inspects R.B,
R.D, K0, Wq@2 and Wp@3 (`:1141`). By the same parity argument, Wp@3 sits at distance 2 from the toy
setting source s and so cannot depend on s; the analogous re-entry would first appear at tick 4,
which the fixture does not include (`:517–521`). The toy also assigns its D′ analogue g a uniform mass
(`:551–557`, `:562`). This part of the control therefore cannot fail on the channel above.

**Closure.** Suppose H-prior is strengthened to H-prior⁺: `(η, β, f_5(t) for S+4 < t ≤ L+3)` jointly
uniform given the remainder, or equivalently the history_v11 bank law posited jointly with η and β.
Order the variables as b5, then `f_5(t)` chronologically, then the remaining keys, then β. By hand
from the recorded coordinates:

- `dist(f_5(t), K0 footprint) = t+77 > L+3`;
- `dist(f_5(t), q9) = t+77 > L+2`;
- `dist(f_5(t), flag cell (0,S,68+k)) = t+68+k > R+k`;
- `dist(f_5(t), p_j) > L+3` for `j ≠ 5`.

Each port-5 coordinate after `S+4` is then a first-front permutation of its own triple given earlier
variables, so `W_τ∖R` is independent of R given K0 and the rest, and S7(b) holds. Combined with S7(a)
and S5, this gives `μ_0^{k0} = μ_1^{k0}` for every k0 including ⊥. These closure computations are the
reviewer's; they are not among the recorded checks.

#### 1.4 What the written argument establishes

- **Established, conditional.** Under H-prior, H-rule, H-torus and H-access (which fixes A and the
  passive, no-write read), with P1–P5 and P6a as recorded: (i) EMPTY, and (ii) the factorization of
  S5. The passive read through `2L` contributes nothing setting-dependent, and `TV_win` and `TV_acc`
  of X equal those of the pre-tail window W. H-inventory makes H-prior consistent with the preparation
  (with P3, the tail cells are not prepared cells); it is not a step of the argument.
- **Not established as stated.** `TV_win = TV_acc = 0`, that is, LA-EQUAL, from the five hypotheses
  with H-prior as displayed. It additionally needs (b) the pre-cut port-5 bank law, an unstated
  hypothesis, and (a) the parent's forward-kernel result, a paper proof not independently reviewed on
  `main`, whose structure was reconstructed here only in outline.
- With H-prior⁺ in place of H-prior, and the parent kernel accepted, the reconstructed proof gives
  LA-EQUAL.
- There is no quantifier slip over k0: the factorization holds for each k0 and for ⊥ (BRANCH,
  `:344–346`). `TV_by_k0` in the JSON aggregates "every incoming-packet value" under one key because
  the values are proof outputs, not per-k0 measurements.
- `:257–259` and `later-access-result.md:32–33` say the equality across settings "has the same cause
  as its emptiness". That is accurate for the tail factor only; the equality of the pre-tail factor
  has a different cause, S7.

#### 1.5 How P1–P6b are established, and faithfulness of the code

P1–P5 and P6a are exact finite computations on very large integers, recorded in
`CS/later-access-result.json` and not re-run here (`later-access-result.md:37–49`). P6b is a sampled
check on 162 small worlds. Read-only comparison of the code with the preregistration:

- **P1** (`probe:245–272`). Own path: the code checks that the direction is a unit axial vector and
  that the ray starts at the port; its length check at `:252–254` holds automatically for an axial
  ray, and uniqueness of the straight path follows from axiality plus P5. "No other-port arrival
  before t": the code takes the exact minimum of `dist − t` over the endpoints and the absolute-value
  breakpoints (`:157–168`), which is correct because the function is convex and piecewise affine. The
  recorded minimum is 0, at edges 2→5 and 3→5. Faithful.
- **P2** (`:275–295`): strict `>`. The labels are both slices of K0–K2 and ΔW1, ΔW2 (`:225–231`); the
  records are R, q9 at L, V at L+2, the herald, flags q0..q9 at R+k, and all eight ports at L+3
  (`:221–224`). Faithful. The flag/timing dictionary is an implementation choice, disclosed at
  `later-access-result.md:105–108`.
- **P3** (`:307–339`): exact on-ray tests against the 42 η cells, 1479 sources and 17 exceptions;
  strict distance > radius for the 25 balls; pairwise disjointness of the rays. Faithful.
- **P4** (`:359–374`): faithful.
- **P5** (`:377–394`): faithful; the point set includes the ray endpoints, which suffices for straight
  segments.
- **P6a** (`:397–399`): faithful.
- **P6b** (`:478–512`): faithful as a mechanism sample, with same-tick co-arrival included.

Partial internal corroboration of the tail-ray geometry (P1, P4, ray distinctness and ready-ball
exclusion through 2L) comes from `NY/history_v11/review/REPORT.md:11–25`, a separate-agent internal
review.

#### 1.6 Support layer of each link

| Link | Support |
|---|---|
| H bijective, the rule | exact finite computation (P6a, CP-RULE), recorded, not re-run; H-rule assumed |
| P1–P5 geometry | exact finite computation, recorded, not re-run; code checked against text |
| S1 diagonal permutation | paper proof (template `history_v11:98–108`); P6b sampled mechanism only |
| S2–S6 (triangularity, tail uniformity, factorization, EMPTY) | paper proof, reconstructed here; not written in the LA files |
| S7(a) forward kernel | parent's paper proof plus recorded geometry; not independently reviewed on `main` |
| S7(b) pre-cut masses | not derived; needs an unstated hypothesis; CP-PRECUT does not cover it |
| H-prior, H-inventory, H-access, H-rule, H-torus | assumptions (§2) |

### 2 Assumption sourcing

- **H-prior** (`:147–157`): joint uniformity of `(η, β)` given D′. Stipulated: history_v11 supplies its
  bank "independently and uniformly … an explicit resource extension … supplied assumptions rather
  than derived physical laws" (`NY/history_v11/REPORT.md:23–27`); the complement prior is "explicitly
  chosen" (`NY/junction_v4/review/REPORT.md:78–81`); the 42-key prior is "a precise prior hypothesis"
  that the native_route_v13 contract "alone does not supply" (`CS/native-random-setting-test.md:86–93`;
  `NY/native_vread_v15/REPORT.md:51–53`). It is load-bearing: a correlated prior gives
  `TV_win = 1/8` (CP-PRIOR, `later-access-result.md:60`). It is not derived for native OI. Tension:
  MR-1 requires μ to be fixed by a selection principle or by invariance over an admissible class
  (`MR/preregistration.md:137–140`); H-prior is a single chosen prior. As shown in §1.3, H-prior as
  displayed is too weak for LA-EQUAL; the needed H-prior⁺ is likewise stipulated, from the same source.
- **H-inventory** (`:161–162`): the source, readiness and bank inventory is complete. A stated
  condition of the construction, carried in the same form in `NY/native_vread_v15/REPORT.md:43–47`; not
  checkable beyond the declared lists, and some source lists are not materialized
  (`NY/history_v11/REPORT.md:79–81`). In effect a definition of the construction, not a derived fact.
- **H-access** (`:163`, `:68–75`): the retained eight-port convention, with port reads passive and
  writing nothing. Not adopted (`NY/CURRENT-HANDOFF.md:6–7`; `NY/native_vread_v15/REPORT.md:62–70`),
  and the no-write clause is "not stated explicitly" in the sources (`:72–74`). Stipulated.
- **H-rule** (`:164`): `U_{t+1} = U_{t−1} ⊕ H(Σ)` with `H(A,B,D) = (B, D, A⊕BD)`, the fixed model rule
  of the native-Y programme (`NY/shared_v12/INTERFACE-CONTRACT.md:32–36`;
  `NY/history_v9/REPORT.md:27–32`). Admissible as a bijection, since every second-order rule is
  bijective (`papers/SM.md:106`). It is not the corpus's selected substratum dynamics: center
  independence, isotropy and linearity select the linear wave rule (`papers/SM.md:224`;
  `papers/Substratum.md:48`; `papers/Explainer.md:767`), and H's BD product is nonlinear. Stipulated;
  N5 applies to the native-Y model only, which MR-1 records (`MR/amendments/MR-star.md:667–668`).
- **H-torus** (`:165–168`): no wrap, with `2H* < side` and spans `< side/2`, `side = 256L+64T+1`. A
  construction parameter (`NY/history_v11/REPORT.md:31–32`), measured exactly by P5 on the recorded
  geometry. Finiteness of the substratum is a posit (`CS/README.md:36–37`). A convention plus a
  measured fact.
- **Hidden sixth hypothesis.** The uniform independent pre-cut port-5 frontier triples, needed at
  S7(b) (§1.3). Unstated, with the same stipulated source as H-prior.

A valid conditional proof does not establish its hypotheses. None of the five is derived for the
native OI system.

### 3 Support for MR-1 N5

**N5 as frozen** (`MR/preregistration.md:109–111`): "`LA-EQUAL`, informativeness `EMPTY`, for the
passive read of the eight public ports through `H* = 2L`, under H-prior, H-inventory, H-access, H-rule
and H-torus. Not a no-go for the outgoing environment or an active coupling." It is cited as off-`main`
provenance at `8af2d904` (`:77–80`, `:86`); the same bytes are now on `main` (`CS/README.md:7–8`).

- **Support.** `EMPTY` is supported as stated. `LA-EQUAL` is supported only with one hypothesis beyond
  the five, the pre-cut port-5 bank law (or H-prior⁺), and with the parent's forward-kernel premise. On
  its hypothesis list, N5 is therefore wider than what is established. On ports, horizon and passive
  read it is not wider.
- **Scope wording.** The LA licence (`:266–272`; `later-access-result.md:85–92`) also excludes other
  settings, carriers and dictionaries (this one is `c = R.A` of `U_{S+4}(port5)` with this K0),
  adaptive operations and other constructions, and, with EMPTY, any claim that informative later reads
  are setting-blind; N5 does not state these. "Not a no-go for the outgoing environment or an active
  coupling" is correct but incomplete. `MR/amendments/MR-star.md:668` adds the qualifier "N5 concerns
  the native-Y rule", which is correct and material.
- **Uses in MR-1.** The statement itself (`preregistration.md:109–111`); a control set that a proposed
  primitive must keep (§7.3, `:690–691`); source screen σ13, "Respected at their scopes and not
  reopened" (`MR-star.md:668`); and selection criterion (s3) (`MR-star.md:734`), which decides no
  source, since every σ fails on (s1), (s2), (s4) or availability (`:741–749`). The SUBSTATE-1 bullets
  at `MR-star.md:674–678` come from other units (`native-random-setting-test.md:9–13`,
  `native-setting-source-feasibility.md:7–8`), not from N5. `MR/README.md` did not mention N5 at the
  reviewed commit. MR-1 does not use N5 more strongly than it states it, and no MR-1 outcome depends on
  it. Under §A.46 item 7, N5 is not yet usable as a premise of an established claim.

### Overall verdict

**Partially verified.**

- **The mathematically valid conditional result.** Under H-prior, H-access, H-rule and H-torus, with
  H-inventory for consistency and the recorded exact P1–P5 and P6a: `EMPTY` holds, and the passive read
  of the eight public ports over `L+6..2L` adds no setting dependence; `TV_win(k0)` and `TV_acc(k0)` of
  X equal those of the pre-tail window, for every k0 including ⊥.
- **What is missing for LA-EQUAL / N5 as stated.** (1) The pre-cut masses' setting-independence
  (S7(b)), which needs the uniform independent pre-cut port-5 frontier triples `f_5(t)`,
  `S+4 < t ≤ L+3`, posited jointly with η and β; this is a hypothesis outside H-prior's displayed form,
  and CP-PRECUT does not measure it. (2) The parent's forward-kernel result, a paper proof not
  independently reviewed on `main`. With (1) added as H-prior⁺ and (2) accepted, the reconstructed proof
  gives LA-EQUAL/EMPTY on N5's stated ports, horizon and read.
- **Hypotheses justified in native OI.** None. All five, and the sixth, are stipulations or
  construction conventions of the native-Y model; H-rule is not the corpus's selected linear lattice
  dynamics.

### Limits of this review

- This is an agent review, run read-only by an agent coordinated by the same Claude Code session that
  drafted the status notes. It is not an independent human or external review and does not discharge
  §A.46 item 7.
- No computation was run. P1–P6b and all control results are taken from the recorded JSON. The closure
  distances in §1.3 are hand arithmetic, and whether S7(b) actually fails for some D′ law is not
  determined.
- The parent's packet-level inputs (π, Q, S, and the 13 incoming keys) and its 42×42 graph were not
  audited beyond their structure.
- The earlier confirmation posted on #1009 was not relied on.
