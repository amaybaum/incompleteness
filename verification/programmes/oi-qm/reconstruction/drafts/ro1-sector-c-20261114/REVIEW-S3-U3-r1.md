# Review of S3-U3-r1 (independent, non-author)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U3-r1.md`
at PR #1294 head `395d7bf1ec507e99b762379353d4143e987c8c0b`, blob `3da2be22`.

**Reviewer.** A separate non-author Claude reviewer (#1169 c.6890079967, C1; c.6891710167). Read-only.
Hand checking only: no computation, Lean, enumeration, repository edit, commit, push or Issue
change.

**Provenance note.** During the review the branch head moved from `395d7bf1` to `b547c9f21` (a
commit retaining a U4 review). The U3 blob is byte-identical at both commits (`3da2be22`), and every
read of U3 and its governing files was made at `395d7bf1` with `git show`. No anomaly bears on U3.

**Verdict: ACCEPT WITH CHANGES.** No claim is asserted beyond its stated conditions in a way that
decides a verdict. H-RR is not asserted, SNR-1 is applied, and routing changes no status. L-2 is
correct under its hypotheses (one small gap in (k3)). Four changes are required (R1–R4). They
narrow or re-scope statements. They do not overturn any reported status. The rest are minor (M1–M10).

***

## 1. Check (1): L-2 re-derived by hand

**Setup.** Deterministic responses `a(x,y,λ)`, `b(x,y,λ)`; `λ` unchanged between the uses; the same
response functions at both uses; binary settings and outcomes.

**Re-derivation.** Fix Alice's policy `(x,x)`. Under Bob's `(0,0)` her fresh-output history is
`(a(x,0,λ), a(x,0,λ))`, with equal entries with probability 1. Under Bob's `(0,1)` it is
`(a(x,0,λ), a(x,1,λ))`. With (k4), the two laws are laws of functions of one `λ`-law. Equal laws give
`P[a(x,0,λ)=a(x,1,λ)] = 1`. The same-register form gives the same conclusion through the XOR. Exchange
the wings. Then `a = α(x,λ)` and `b = β(y,λ)` almost surely, and with (k4) `|CHSH| ≤ 2` by the
sixteen-table bound (Main:389, [M]; an elementary bound). **The proof is correct.**

**Exact hypotheses under which it holds.** These are (k1), (k2), (k4) and (k5) as stated, plus the
following on (k3):
- the proof needs the *product* policy pairs to be jointly executable in one program on one `M` and
  one AD-1 instance: Alice `(x,x)` with Bob `(0,0)` and with Bob `(0,1)`, for `x = 0,1`, and the mirror
  pairs. (k3) states policies per wing only (M1);
- the proof does not use (k3)'s clause "the change is `φ`-effected". The TSI instance does not meet
  that clause: its settings sit in preloaded per-use slots `x₁, x₂, y₁, y₂` (TSI:57, :87–94), and no
  change is written between the uses. TSI is an instance of the proof, not of (k3) as worded (M1);
- binary settings are implicit in "for all `x`, `y`".

**Counterexample search.** None was found within the hypotheses. Heralded failure (TSI `h < 1`) is
setting-independent and does not affect the argument. Stochastic responses with per-use noise, a
tick-indexed response, and a source changed between uses all fail (k2) and fall outside L-2. That
last case is the basis of R1.

**Instance checks.**
- `T` (SEL-EXCL-1 l. 33): Bob `(1,1)`, Alice `(0,0)` against `(0,1)` gives `(r,r)` against `(r,r⊕1)`.
  Verified, and consistent with l. 179 up to `y₁`.
- TSI: `a = R` and `b = R⊕xy⊕C` (TSI (3), §3). U3 cites (10). In (10) Bob's policy is `(0,1)` and Alice
  varies `x₂`. That is not L-2's comparison. Under L-2's own comparison (Bob `(1,1)`, Alice `(0,0)`
  against `(0,1)`), Bob's pair is `(R⊕C, R⊕C)` against `(R⊕C, R⊕C⊕1)`. I verified this. "As L-2
  requires" should cite this comparison, or say that (10) is a different witness (M1).

**Labelling.** L-2 is called proposed or unverified at the header (l. 13), in §5 Status, in §4.1, in
§4.4 ("counts only once L-2 is verified"), in §8 U3-1 ("conditional on review"), §10.2, §10.3, CQ-2,
§10.5 and §10.6. **No verdict rests on it unconditionally**, with one wording exception: RQ-UPD-2's
closing sentence and U3-2 (§8) carry no conditional marker, although the text cites L-2. R2 removes
the dependence instead.

**R1 (required). RQ-UPD-1 overstates what L-2 forces.** L-2's escape is "(k2) fails". §2.2 defines
only two cases:
- unchanged source: the same `λ`, the same responses;
- source update: the content read changes *as a function of the first use's settings or outputs*.

These are not exhaustive. A third case is a change of the content read that does not depend on
settings or outputs. Examples: the second use reads a different preloaded cell (RR-2's fresh cells),
or `λ` is scrambled by a setting-independent bijection. That case escapes L-2, and the fresh-cell
lemma shows that it can be no-signalling. So L-2 does not imply "a use must update its source" in
§2.2's sense. L-2 implies only that the source content or the responses change between the uses.
Required: state the third case in §2.2, and restate RQ-UPD-1 as "(k2) fails: a source update or a
setting-independent renewal of the content read". Propagate the change to:
- §3 (RQ-REU's last bullet);
- §4.1 ("Its content is the requirement RQ-UPD-1");
- §8 U3-1;
- §10.1 (RQ-UPD row);
- §10.2 (RR-1);
- §10.5.

The quantum-reuse case does force an output-dependent update, but on a different ground (R2).

## 2. Check (2): the 2√2 candidate's status at source

TSI is on `main` at `75cc5100` (blob `65db5a7c`). Its header says "Independent exact-head review
verdicts are recorded on [#1173]" (a PR). §6 says "Author result, pending independent review"
(TSI:311). No review file is on `main`. **[NP] is correct** under U1's label (U1:110–111), and it is
the conservative reading of a source that is itself inconsistent on this point. "Quantum-calibrated"
is accurate: "(5) was selected from the comparator", "an exact **calibration**, not a derivation"
(TSI §3). The candidate also gives up graph-cone isolation explicitly (TSI:82–83). U3 does not need
that fact, but it bears on "deterministic realization" readings, and it could be noted.

## 3. Check (3): quantum reuse law and capacity bound

**R2 (required). RQ-UPD-2 and U3-2: (i) is stated on the wrong ground, and a stronger route exists.**
- As worded, (i) ("the first outcome written into what the next use reads", from repeatability) fails
  for a Bell-local wing. An unchanged `λ = (λ₀, λ₁)` with `a(x,λ) = λ_x` meets (9)'s single-wing law:
  `a₂ = a₁` at a repeated setting, and fair and independent at a changed one.
- [A-inf, reviewer] (9) also requires `a₂ = a₁` when `x₁ = x₂` *for every* `y₁, y₂`. Under
  unchanged-source reuse that gives `a(x,y₁,λ) = a(x,y₂,λ)` almost surely. With (k4) this means
  `|CHSH| ≤ 2`, which contradicts (1). So the quantum two-use law excludes unchanged-source
  realizations of the `2√2` table **directly, without L-2 or any no-signalling premise**, under
  (k1), (k3), (k4) and (k5) with (9) in place of no-signalling. TSI already states this for its
  candidate: the continuation "demonstrably fails (9)" (TSI §5 ledger); "a different post-measurement
  state cannot be chosen to rescue (7)" (TSI:239).
- Correct form of (i): the content read at use 2 determines `a₁` (and `b₁`). It must depend on the
  first use's settings or outputs at positive mass on at least one wing, namely the wing whose
  first-use response depends on the remote setting. It need not do so on both wings.
- (ii): "content the first use did not read" is too strong. The requirement is content *not determined
  by the first use's records*. It may be preloaded in `λ` (booked in `μ`), as U3's "booked in `μ` or
  renewed" already allows.

Required: restate (i) and (ii) accordingly. Base the exclusion of unchanged-source reuse in RQ-UPD-2
on (9) with its hypotheses listed, and state the remaining dependence (none on L-2). Carry the result
to U3-2 and to §10.3's RQ-UPD row. The writer must check this; it is a reviewer [A-inf], not a result.

**Capacity bound (§6).** The counting is correct. Records held at one tick are functions of the joint
present configuration of the declared family, so they take at most `∏_k |C_{V_k}|` values. A program
whose complete-record law needs a larger support cannot have it at `t_c` (G4, U1:183). Θ(e) requires
equality of complete-record laws, so the record map cannot be many-to-one. The bound is target-neutral.

**R3 (required). Scope and classification of the bound.**
- (a) **Ledger Q1.** SPEC already carries this question open: coverage has "one stated `Obs`", and
  "Ledger Q1 (one observer interface, or a stated family of nested partitions) bears on 'one stated
  `Obs`'" (SPEC:397–402). Owner question 1 should be put as bearing on Q1, not raised as a new
  question. The "family of nested partitions" option is a reading §6 omits.
- (b) **Two coverage targets.** Two different coverage targets are run together:
  - Gate A answer 3, "arbitrarily large finite carriers" (#1169 c.6876591512; SPEC:400);
  - amended AC-1's coverage half, "what perceived quantum phenomena need" (c.6891338304).

  Perceived phenomena are finite, so under reading (a) the bound defeats the second only for a model
  whose family is too small. §10.3's RQ-CAP coverage cell reports only the first. It should report both.
- (c) **"Fails on every model" is a consequence of the frame.** It follows from U1's own [P] choices
  (G4's joint-hold clause, U1 §5.2; AD-1(a)'s finite family) together with answer 3. It is not a native
  fact about OI models. It should be reported as a frame-level incompatibility for owner decision under
  K-3: the frame does not keep the unbounded scope under reading (a). It should not be stated as a
  negative about OI, or as "not available" in SNR-1's counting sense.
- (d) **Ground.** Main:42 gives the finiteness of *each* observer. The finiteness and fixedness of the
  *family* come from AD-1(a) and reading (a), not from the Definition. Correct §6's "whose finiteness
  is the Definition's premise".
- (e) **Missing condition.** RQ-SEQ's "Bound: … fails at the held capacity of one model" (§3) and
  U3-4's first sentence should carry "under reading (a)".
- (f) **Count.** "At least `2^{2m}` values" holds for randomized setting policies. A fixed policy
  needs at least `2^m`.
- (g) **Class.** The bound is the immediate consequence of J1, "a proper subsystem with finite
  momentary capacity" (SPEC J1; Main:724 (ii)), under G4. It is a held-capacity analogue of SEL-DISC-1
  l. 79. ELABORATING fits better than NEW.

**K-1/K-2.** Under reading (a) the bound makes SPEC's unbounded coverage impossible *by the frame's
definitions*, for PR and the quantum references alike. That is not a K-1 breach: PR is not singled
out, and the ground is observer finiteness, a genuine premise. It is not a K-2 breach either: nothing
in it is chosen for quantum outcomes. It is a K-3 matter, which R3(c) addresses.

## 4. Check (4): H-RR and SNR-1

- H-RR is never asserted. §4 assesses it as a hypothesis, and §10.2 reads "a hypothesis,
  undetermined. No joint restriction is claimed".
- PLAN's support, refutation and undetermined conditions are applied unchanged.
- RR-2's supplied bank is `μ`-assumed, and nothing resting on it counts as a refutation (PLAN:380–382,
  :796–797). Correct.
- §4.4's sub-form refutation "counts only once L-2 is verified". Correct. After R1 the sub-form should
  read "unchanged-source realizations" (it already does).
- §4.4's "can be met only by …" is a necessity claim built from [A-inf] links conditional on L-1 and
  L-2. It is labelled [A-inf] and conditional, which is acceptable.

## 5. Check (5): routing

- The O-REUSE row text matches #913's body: "Foundational | O-INS (#914) | blocked: O-INS | not
  authorized".
- The status source on `main` matches #913 c.6891515006 (REPORT blob `2f77fe2f`; `86cd47e53` is an
  ancestor of `75cc5100`).
- The O-INS row text matches #914's body.
- The gate names match #913's body, and the accountability at O-INS matches #913 c.6628909432 item 46.
- "Routed as requirements … unchanged" holds. **No status, readiness or authorization changes**, as
  C5 requires.

## 6. Check (6): definitions

- The definitions of reuse, source, freshness relative to `Γ_exe`, unread versus unreadable, held
  channels, granularity and comparison-tick holding are stated on factor sets, `φ`, `μ` and AD-1.
  None refers to a record law or to quantum statistics, so they are noncircular and meet G7 and K-2.
- The operational counting of side channels is a [P] choice. Its grounds are SEL-DISC-1 l. 97 and
  l. 38, plus an argument from the PR test's usability. That last argument is not its only ground, so
  SPEC §6.1's rule is not breached. Owner question 3 is the right route. The choice is also
  target-neutral: conditional on L-1, the ontic reading would exhaust the budget for deterministic
  realizations of QR-1 as well. Stating this would strengthen the K-2 case (optional).
- §2.2's definitions are not exhaustive (R1).

## 7. Check (7): citations spot-checked (all at the stated objects)

The following match: blob ids for U1, U2, PLAN, DEPS, SPEC and VERIFY at `0f416af5` and at
`395d7bf1`; SEL-EXCL-1 `1e8892ff`, SEL-DISC-1 `ccf2d46d`, NAS `a6661de9`, TSI `65db5a7c` and MR★
`45af1678`. Quotations and lines checked:
- **TSI:** :202, :228–239 ((9), with "orthogonal"), :277–282, :311–314, :323–325, (3) and (10).
- **SEL-EXCL-1:** l. 33, l. 36 (`T² = id`), ll. 87–101 (including "no admitted operation reads or
  couples to them earlier", l. 101), ll. 165–181.
- **SEL-DISC-1:** l. 38, l. 50 ("**not** a quantum-reference assumption"), l. 53, l. 79, l. 97, l. 149.
- **NAS:** l. 77, l. 84.
- **REPORT:** :29–31, :59–67.
- **PREREG:** :177–187 (Lemma R, invariance).
- **OA1:** D2 :145–154, D3 :156–160, D4 :162–174, :328, :359–361.
- **MR★:** :638, :1344–1345.
- **Main:** :42, :74, :389, :416–423.
- **Substratum:** :76 (E1).
- **SPEC:** :239–242, :307–308, :373–374, :397–400.
- **U1:** :157–167, :183, :193–197, :227 (quoted as a prefix; the cell continues "and bounded diameter,
  each a factor …"), :570–574, :603–616, :650–677, :691, :892 (F-2), :895–900.
- **U2:** :127–131, :203–205, :379–391, :400–408, :418–435, :487–488, :528–530, :728 (F-3), :733,
  :766, :804–809.
- **PLAN:** :209, :348–384, :396–398, :561, :784–799, :872, :894–898.
- **DEPS:** :389–404.
- **Other on-`main` files:** `apparatus-1-20261107/DESIGN.md`:225, `composition-source-map.md`:88,
  `oa-1-20261112/STATUS.md`:65.
- **#913:** gate "do not infer privacy from an unread field".
- **#1169:** the five owner comments, quoted correctly.

## 8. Check (8): premises, conditionals, soundness

- **No new physical premise** is adopted. L-2 is proposed, the operational counting is [P] and
  routed, and reading (a) is not chosen.
- **Soundness is not treated as required in the definitions.** RQ-UPD is stated as conditional on
  no-signalling.

**R4 (required). E1 used as performed-experiment data.**
- §10.3 says "that is a raw-direct miss, given E1 (Substratum:76)" and "Agrees with E1; demanded by
  it". E1 ("described, to the precision tested, by quantum mechanics") is an explicit empirical input.
  It summarizes QM's success and is not a raw-direct record of a performed sequential experiment on
  one entangled source (§A.24).
- Used this way, E1 reintroduces soundness as a requirement for sequential experiments, which the
  amended target makes open (c.6891338304).
- Required: state the agreement half as conditional on a performed experiment whose raw complete
  local-history records show setting-independence. Whether such an experiment exists and was read
  first-hand is owner question 4. Remove "demanded by" E1.

## 9. Minor findings

- **M1.** L-2's (k3):
  - require joint executability of the product policy pairs on one `M` and one AD-1 instance (G6);
  - drop or explain the unused "`φ`-effected" clause, and note that TSI's preloaded per-use slots
    meet the proof, not (k3) as worded;
  - in the TSI check, cite L-2's own comparison (§1 above) rather than (10) as "what L-2 requires".
- **M2.** §2.1's "exactly when" (§A.34). The ⇒ direction holds by U1:676–677. The ⇐ direction needs
  the components' inputs re-certified in the composite context, for example freshness of a stage-2
  cell relative to stage 1, which §2.3 itself requires. `Δ_k`, defined as "inputs … that no component
  needs", omits this. Fix: include re-certified component inputs in `Δ_k`, or state the result as
  one direction only.
- **M3.** §4.2. Conditional on L-1, a Bell violation gives positive mass where `a(x,·,λ)` depends on
  `y` *or* `b(·,y,λ)` depends on `x`. It does not necessarily give dependence of `b` on `x`. The probe
  is then on whichever wing applies.
- **M4.** U3-1's "exposes an assumption in DEPS §5.1". DEPS's "Exact scope" already limits the
  discriminator to "the **same-seed** PR implementation … not shown against any other non-quantum
  model" (DEPS:397–401), and TSI (on `main`) already gives the quantum-calibrated instance. What L-2
  adds is the general form: the label "discriminator", read as PR against QM, is unsupported. Restate
  the finding as that, with NEW for L-2's general statement only.
- **M5.** §10.1 question 1. "Disproved for programs needing full in-`V` histories" should read: under
  μ-G and D4's premise, a native *hidden* fresh cell cannot influence such records. Visible heralded
  cells (D3) are not excluded, and D4 "dissolves under MP-0a" (OA1:174). RQ-REN-F already states this
  correctly.
- **M6.** §2.5 GR-2. RR-1 at the next tick also needs a `φ`-effected setting change inside `φ_m`
  (RQ-REU). The absorbed circuit's re-application alone does not supply one.
- **M7.** CQ-2 should name S8 (adoption of `Θ`) as a condition, as §10.3 does.
- **M8.** The authorization block omits C1's "followed by ChatGPT exact-head review". §10.6 says the
  constructions are "routed to #1143", while §10.5 says #1143 is "not routed by C5". Use "noted for
  #1143" in §10.6.
- **M9.** §2.2 grounds the persistence of a source update in C-RET's parked-record clause
  (U1:570–574). That clause governs records returning to a readable region. C2-structural (Main:74),
  which U3 also cites, is the fitting ground; drop the C-RET citation or explain it.
- **M10.** §1: "No general statement of L-2 was found in the corpus searched" is a bounded negative
  with a stated search. Acceptable. The literature caveat stands (owner question 2).

## 10. Checked / not checked

**Checked.**
- L-2's proof and hypotheses, and its two instances.
- The quantum two-use law (9) against RQ-UPD-2.
- §6's counting, and its readings against U1 AD-1(a), G4 and G6 and SPEC's coverage, K-obs, K-dyn,
  J1 and ledger Q1.
- C-RET against the R2 table.
- H-RR and SNR-1.
- Routing text against #913 and #914.
- The definitions for circularity.
- The §A.42 item 8 table.
- The citations of §7.
- The owner comments c.6890079967, c.6891241282, c.6891338304, c.6891511297, c.6891710167,
  c.6876591512, and #913 c.6628909432 and c.6891515006.

**Not checked.**
- The literature on L-2.
- Whether performed sequential Bell experiments test complete local-history no-signalling.
- L-1's proof (U2's).
- D5, D2, D3 and D4 beyond their statements.
- MR★ items other than the cited lines.
- U2's per-program verdicts.
- §7's C-RET/R2 rows beyond plausibility.
- Any Lean module or probe script (Main:389's check script was not run).
