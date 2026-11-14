# Independent non-author review: Bell-scope unit 1, r2 (PR #1231)

- **Object.** Branch `research/bell-scope-868-20261111`, head `e1534b08fa3f361e05416b3cc0c1dcd2f3b23918`,
  directory `verification/programmes/oi-qm/reconstruction/drafts/bell-scope-868-20261111/`:
  `BELL-SCOPE-UNIT1.md` (blob `5814e479`, 472 lines), `DISPOSITIONS-r2.md` (`dd8cbc8c`),
  `probes/generic_bell_checks.py` (`e47f3179`, SHA-256 `83cecb18…b6d0`, equal to BS:300),
  `probes/generic_bell_checks.out` (`0798db76`). "BS:n" is line n of `BELL-SCOPE-UNIT1.md`.
- **Authority.** #868 comment 6874036684 (owner, 2026-11-14, OQ-2: "BS r2 (#1231) and the SB-L3 extract
  each get a separate independent non-author review"; "No probe replay, computation, integration or merge
  is authorized"), read first-hand, with #868 comment 6873193841 (landing plan, option (1)).
- **Reviewer.** Not the author of BS, its dispositions, its probe, the landing plan or the ladder. Hand
  reasoning only. No computation on any OI rule; the probe was read as source and **not executed**; no
  replay. Nothing was written to the repository.
- **Context read.** `papers/Main.md` at `cac5d264` (BS's pin) and at main `c3b5f37a`; `papers/SM.md`,
  `papers/Substratum.md`, `book/ch18-beyond.md` at both; the four `oi-qm/reconstruction` records BS cites;
  #1210 QX-6 r7c at `4c7f3f86`; `STATUS-BS.md` and `LANDING-PLAN.md` at `3859c3ef`; Bell ladder r3 at
  `d8e4f80e`; #1283 at `f57e576a` (§A.46 item 8); PR #1231 reviews 5857227567 and 5857981727; #1169
  comment 6791556736.
- **Line convention.** "Main:n" below is BS's numbering at `cac5d264`; at `c3b5f37a` it is Main:(n−2) for
  n ≥ 6 (checked: Main lost exactly lines 4–5, every other hunk is line-count neutral), as `STATUS-BS.md`
  states.

***

## Verdict: ACCEPT WITH CHANGES

Theorem N, Theorem N′, Lemma G (one direction), the §4.1 bound with its optimality and abstract
attainment, the §4.2 contraction and the §4.3 corollary are correct at their stated scope; I re-derived
each by hand. The verdicts (C) for OI, (A) restricted to 𝒞_sep, (B) not established, are stated at the
right level and nothing in the record is a native OI result or an OI-wide no-go. Three statements outside
the proved core need correction before landing (findings 1–3): the O1 analysis omits ledger item (vii),
which already at the pin closes O1 inside NBA's own domain; one summary sentence turns a necessary
condition for (B) into a sufficient one; and the Level-A disjunction of §5 is incomplete. None changes a
proved result or the verdicts. Each can be carried either as an r3 of the record or, if r2 is landed
byte-for-byte, in `STATUS-BS.md`'s "Superseded lines" (with finding 1 reclassified from source drift to a
correction).

## What the record establishes, and at what layer

| Result | Layer | Conditional on | Reviewer check |
|---|---|---|---|
| Theorem N (BS:159–178) | mathematical derivation on paper, on Main's cone lemma (paper proof on `main`) | (D), (F) (ledger (ii), (viii), posited); (Gen), (Rec) incl. the ⊥-rule, (Sep), (GI) (protocol properties, posited per protocol); (MI) for Ω (posited; ledger (xiv) on current `main`) | re-derived; correct |
| Theorem N′ (BS:185–196) | as above | as above without (GI); (MI\*) for λ\* (posited, chart-relative) | re-derived; correct (finding 6) |
| Lemma G (BS:198–228) | paper derivation | (M) (ledger (iv), Lemma 3 scope; uses bijectivity), (CF) open | re-derived both directions' status; correct as one implication |
| §4.1 bound, optimality, attainment in abstract 𝒞_sep | elementary paper derivation | Bell locality with MI; attainment: the six-site toy under (M), (CF) | re-derived; toy checked by hand |
| §4.2, §4.3 | paper derivation; §4.3 on Main's boxed bound | one product extractor; response-complete Ω | re-derived, including Main's Pinsker–Jensen bound |
| Verdicts (C)/(A)/(B); NBA | classification; NBA open | — | correct, with findings 1–2 |
| §5 | conditional consequences | 𝒞_sep membership; C9 (research record on `main`) | correct after finding 3 |
| §6 | exploratory scoring; none adopted | — | P-a row needs finding 1 |

All of it sits on the consistency axis (§A.23): it confirms what follows from stated premises and confronts
no new data. No result is kernel-checked; the [X] checks are provenance only (Check 4). Architecturally every
load-bearing element is substratum-level (the cone lemma on `(S, φ)` and protocol properties); no emergent
input enters.

***

## Check 1. Theorem N and Theorem N′

**Hypotheses (exact).** (D) one deterministic `φ: S → S` for every run and setting value (bijectivity
unused). (F) `S = ∏_{i∈V} S_i`, all finite; `G_φ` the symmetrized one-step dependence graph of the actual `φ`
(Main:364). (Gen) disjoint `G_A, G_B`; `a = g_A(x_{t_s}|_{G_A})`, `b = g_B(x_{t_s}|_{G_B})`; `W = V∖(G_A∪G_B)`,
`Ω = x_{t_s}|_W`. (Rec) `h_A = H_A((x_t|_{R_A^t})_{t_s≤t≤T_A})`, `o_A = π_A(h_A) ∈ {±1}` with a fixed local ⊥-rule.
(Sep) `d_{G_φ}(G_B, R_A^t) > t − t_s` for all t in the window, symmetrically. (GI) `h_A` depends on `x|_{G_A}` only
through `a`. (MI) `p(Ω|a,b) = p(Ω)` for every jointly admissible pair; a finite menu, every pair admissible.

**Re-derivation.**
1. `x_t = φ^{t−t_s}(x_{t_s})`; by the cone lemma each `x_t|_{R_A^t}` is a function of `x_{t_s}` on
   `B_{G_φ}(R_A^t, t−t_s)`, which (Sep) makes disjoint from `G_B`. A finite union of such balls still misses
   `G_B`, so `h_A = F_A(x|_{G_A}, x|_W)`. Correct. It needs the regions, `T_A` and `H_A` fixed in advance;
   that is the natural reading of (Rec), but it is not written (finding 5).
2. (GI) makes `F_A(g, w) = F_A(g′, w)` whenever `g_A(g) = g_A(g′)`, so `F_A = Ĥ_A(Ω, a)`. Because `S` is a full
   product and `φ` is defined on all of it, `Ĥ_A(Ω, a)` is defined for every Ω and every menu value `a`, which
   is what a response function for the whole menu needs. Correct.
3. Conditional on `(Ω, a, b)` both records are point masses; (MI) gives one μ = p(Ω) for every pair. Correct,
   for the whole menu at once.
4. `q_0(r_0+r_1) + q_1(r_0−r_1)`: one bracket is 0 and the other ±2, so the value is ±2; averaging gives
   `|S_CHSH| ≤ 2` for every CHSH variant. Correct.

**Theorem N′.** Step 1 alone gives `h_A = F_A(x|_{G_A}, Ω) = Ĥ*_A(λ*, a)` through the injective chart. With
(MI\*), the mixture formula holds with λ\*. Correct, with two unstated points (finding 6): (MI\*) depends on
the chosen charts (with the trivial chart `ρ_A = x|_{G_A}` it fails whenever two settings occur), and the
response `Ĥ*_A(λ*, x)` is defined for every menu value `x` only because (MI\*) forces every λ\* in the support to
co-occur with every setting (if `p(λ*) > 0` and `(x′, ρ_A)` were outside the chart image, `p(λ*|x′,y) = 0 ≠
p(λ*)`). The remark at BS:193 that (MI\*) implies (MI) for Ω is correct (marginalize over the residues).

**Scope.** The conclusions are stated at the proved scope: one fixed map, the class's protocol properties,
complete local histories inside the window, every-run outputs, no postselection. Pre-`t_s` heralds are
handled loosely in §2 (finding 8) but not in the theorem.

**Narrowings required by the earlier reviews.** All five of review 5857227567 are present in r2: CF
sufficient only (BS:215–219, :286–287, C4); the O2 window (BS:56–60, :254–260); NBA's complete antecedent with
Theorem N′ (BS:185–196, :232–244); tightness split into optimality over Bell-local tables and abstract
attainment (BS:329–341); the rationality aside under (M) (BS:371–373). Review 5857981727's nonblocking note
on the symmetrized (Sep) postdates r2 and is not in the record text; `STATUS-BS.md` carries it under
Limitations (finding 7 gives text for the record).

## Check 2. The §4 bound (BS:317–330)

- `P_Q(a,b|x,y) = (1 + ab·c_xy/√2)/4` sums to 1 (Σ ab = 0) and has entries `(1 ± 1/√2)/4 > 0`.
  `E_xy = c_xy/√2`; `S_Q = 3/√2 + 1/√2 = 2√2`. Correct.
- `|E^L − E^Q| = |Σ ab(P_L − P_Q)| ≤ Σ|P_L − P_Q| = 2ε_xy`; `2√2 − S_L ≤ Σ 2ε_xy`; `S_L ≤ 2` gives
  `Σ ε_xy ≥ √2 − 1`, mean `≥ (√2−1)/4 ≈ 0.10355`, and max ≥ mean. Correct. "Equivalently" at BS:323 should be
  "in particular" for the worst setting (finding 9).
- **Optimality.** The eight deterministic tables with S = +2: if `r_0 = r_1`, then `q_0 = r_0` with `q_1` free
  (4 tables); if `r_0 = −r_1`, then `q_1 = r_0` with `q_0` free (4 tables). Their uniform mixture has zero
  marginals and correlators `(½, ½, ½, −½)`, so `P_L = (1 + ab·c_xy/2)/4`. Per context
  `TV = ½·4·|1/2 − 1/√2|/4 = (√2−1)/4`, in every context. The witness is Bell-local, so the constant is optimal
  for the mean and for the worst setting over all MI Bell-local tables. Correct. It is the isotropic mixture
  at `v = 1/√2`, as stated.
- **Attainment in abstract 𝒞_sep (BS:332–341).** Eight bits, 256 states; `r_A ← r_A ⊕ w_A[g_A]` is an involution
  in `r_A`, so a bijection. Symmetrized `G_φ` has two components, `{g_A, w_A, r_A}` and `{g_B, w_B, r_B}`, so
  (Sep) holds for any window; (GI) is trivial (the generator is its setting). The event "(w_A, w_B) in the
  eight tables, r_A = r_B = 0" is `S_G × E_W`, so (CF), hence (MI), with all four pairs admissible; the record law
  is the witness. Correct. The update is not linear over GF(2) (`g_A·w_A1` term), so the toy lies outside
  ledger (vii); BS does not claim otherwise, and correctly leaves attainment by the native rule open.
- **General target** `ε ≥ (S_Q − 2)/8` for the mean, given the same CHSH functional. Correct.
- **§4.2.** `TV(f_#P, f_#Q) = sup_U |P(f⁻¹U) − Q(f⁻¹U)| ≤ TV(P, Q)`. Correct; the last sentence of BS:354–355 is
  informal but harmless.
- **§4.3.** I re-derived Main's boxed bound: `S − 2 ≤ Σ_z 2·TV(p(Ω|z), p(Ω)) ≤ Σ_z √(2 D_z) ≤ 4√(2 I_nats)`
  (Pinsker, then Jensen with Z uniform) `= 4√(2 ln2 · I_bits)`. Then mean `ε ≥ (2√2 − 2 − 4√(2 ln2 I))/8`, positive
  iff `I < (3 − 2√2)/(8 ln 2) ≈ 0.0309` bits, matching Main. Correct.

## Check 3. The extra content landing with the record (OQ-5)

- **Lemma G (BS:198–228).** Status: paper derivation, one implication (M)+(CF) ⇒ (MI); with block products
  and setting–residue independence, ⇒ (MI\*). Proof correct (uniform law on a product set is a product law;
  for (MI\*) the joint law factorizes as `p(Ω)p(a)p(ρ_A)p(b)p(ρ_B)`). The converse counterexample `r = w` is
  correct: `{r = w}` is not of the form `E_G × E_W`, and `(a, b)` is uniform and independent of `w`; (MI\*) also
  holds there. Hypotheses: (M) is posited and its transport clause uses bijectivity of `φ` (finding 10); (CF)
  is open and unsourced. Stated at proved scope; the closing paragraph (BS:221–228) is correctly hedged.
- **NBA (BS:232–244).** Status: open lemma; the implication NBA ⇒ (A) on its domain, by Theorem N or N′ then
  §4, is correct and one-directional. Limit: the domain is "Main's ledger posits (i)–(xiii)", which includes
  (vii), linearity. Under a linear (or affine) update `(φ(s′))_i − (φ(s))_i` depends only on `s′ − s`, so a
  dependence present at one state is present at every state and `G_φ` is the reference graph; with (x) on
  either reading it is simple-cubic. Inside NBA's own domain no preparation-indexed long edge exists and O1 is
  closed; O1 is open only for Main's adopted branch (a), which lies outside (vii) (Main at `c3b5f37a`, lines
  362 and 414, now says so). BS states O1 as open on the reference-class reading and lists it among NBA's open
  parts (BS:49–54, :73–74, :246–253). This is an omission at the pin, not source drift (finding 1). NBA stays
  open through O2, O3 and the existence of generator and record regions; the verdict (C) is unaffected.
  Separately, BS:73 overstates what a failure of NBA yields (finding 2).
- **§5 (BS:377–402).** Status: conditional consequences. Level B items 1–3 are correct at their stated
  conditions (C9's antecedent and conclusion match `prepared-pair-source.md` §5, which also assumes each law is
  common across settings). The Level-A paragraph's disjunction is incomplete (finding 3). The #1169 paragraph
  omits the measurement-dependence route (finding 13). Consistent with #1169 comment 6791556736 ("do not
  promote Level B without Bell coverage").
- **§6 (BS:406–415).** Status: exploratory; nothing adopted; the §A.29 checks are reasonable. P-a's
  disposition rests on F1's reading of (x); under (vii) P-a's content is already entailed by the ledger, and
  the tension is between (vii) and Main's adopted branch (finding 1).
- **#1210 A6.1 [D] (BS:183).** Status: provenance only, off `main` (`QX6-BELL-CHSH.md`, blob `2b525318`, at
  `4c7f3f86` on `research/qphen-phase1-frozen-20261109`; located). Its hypotheses are per-tick maps independent of
  the remote setting outside each wing (L′) and graph distances in `G_A`, `G_B` (R). Theorem N's proof uses only
  C1; it does not use A6.1, as BS says. Limit worth noting: A6.1's time-dependent maps are not a subclass of
  Theorem N's single fixed map with symmetrized (Sep) (a clock site read by both wings breaks symmetrized
  (Sep)), and BS only calls A6.1 "parallel". Stated at the right scope.

## Check 4. Evidence tags

- Legend (BS:21–24) is accurate for r2 except "A … unreviewed" (BS:23), now reviewed; `STATUS-BS.md` notes it.
- Row tags C1–C13 are accurate. C2 "P (+ exhaustive check 11)" and C13 "P" match Main. C9 "W" matches the
  research record on `main`. C10 "P (construction)" is if anything conservative (the S ⇒ D direction is
  kernel-checked, ladder stage 0). C8 is correctly "bound not re-proved here".
- [D]: one item (A6.1), correctly provenance. [L]: Wharton–Argaman, Barrett–Collins–Hardy–Kent–Popescu
  (2002, memory loophole: the two-sided case affects finite-sample estimators, not the per-run law), Hall–
  Branciard (via Main), de Broglie–Bohm non-equilibrium signalling. Attributions are correct as recalled;
  BS says none was read first-hand.
- **[X] checks (OQ-8 open; provenance only).** I read the probe and did not run it. If the owner ratifies the
  run and a replay from `main` matches the recorded output, each would support:
  - G1 — exhaustive finite check of the pointwise CHSH identity (16 tables × 8 functionals); also immediate by
    hand (Check 1 step 4).
  - G2a–b — exact symbolic CHSH = 2√2 and normalization of the target; positivity (G2b) uses a floating
    `evalf` comparison, trivially true but not exact.
  - G3a–e — exact certification of the optimality witness (count 8, correlators, per-context TV, isotropic
    form). Exhaustive on a finite object.
  - G4 — a sample on a rational grid (the second law is subsampled, `laws[::7]`) of `|ΔE| ≤ 2 TV`; a control,
    not a proof; the inequality's proof is the one-line hand argument.
  - G5 — 400 seeded pseudo-random rational cases of TV contraction; a control only.
  - G6a–b — one product-event example and one coupling-event countercontrol; illustrations of Lemma G, not
    a proof of it.
  - G6c — exhaustive check of the converse counterexample `r = w` (a complete check of that finite object).
  - G7a–d — exhaustive certification of the six-site toy: bijectivity, dependence graph (no cross-wing edge),
    setting independence under the conditioned law, record law = witness.
  So G3, G6c and G7 would add exhaustive-finite-computation support to optimality, the converse
  counterexample and attainment; G1, G2 to the constants; G4, G5, G6a–b are controls. Until ratification all
  rest on the hand arguments, which I find complete. BS:14–16 presents the probe as within the unit's scope
  without recording the "no runs" option text (finding 14).

## Check 5. Dependencies and citations

Every cited file:line was opened at `cac5d264` and compared with `c3b5f37a`.

| BS cites | Says what BS says? |
|---|---|
| Main:22 (Level A envelope) | yes |
| Main:362 (PR via globally coupled hidden dynamics) | yes |
| Main:364 (cone lemma, "for some state", symmetrized) | yes; at `c3b5f37a` Main:362 adds `G_φ^K` and the (vii) consequence |
| Main:366–393 (exogenous theorem; check 11) | yes (theorem through □ at 366–391) |
| Main:406–407, :406–410 (MI retained as posit; fails for the full microstate) | yes |
| Main:416 (Corollary; cone reach 1 to 1/√3; wave speed 1/√3; c "not derived"; wings inside the graph cone fall outside) | yes; the O2 window is BS's own derivation at the pin and is now in Main:414 |
| Main:418–425 (boxed bound; 0.0309 bits; Hall–Branciard 0.080) | yes |
| Main:427 (response-completeness), :429 (NS; PR control), :698 (spatial-composite branch) | yes |
| Main:654, :726 (F2: chaotic-mixing citation of §3.3; no such passage in Main:360–430) | yes at the pin; corrected on `main` (ledger (v), (xiv)) |
| Main:726 ledger (x) unscoped | yes at the pin; scoped to `G_φ^ref` on `main` |
| SM:108 (reference-class local graph-dependence), SM:110 (prepared long edges) | yes, unchanged; SM:104 changed on `main` |
| Substratum:131–133 (H-Bell (i)–(iii)) | yes, unchanged |
| Substratum:171, :467 | exist and are Bell passages, but no BS statement cites them (finding 12) |
| `book/ch18-beyond.md`:104 ("candidate realization, not an established Bell mechanism") | yes, unchanged |
| `composition-source-map.md` @ `017ae88e` (blob `98470461`) vs `main` (`c4eeb467`) | yes: commit not an ancestor of `main`; only line 5's author label differs; §5.2 PR CHSH 4 |
| `prepared-pair-source.md` §§4–5 (C9) | yes; §5 also requires each law common across settings (finding 11) |
| `two-system-interface.md` ("not a compiled extension"; cross-wing controlled interaction; reuse signalling) | yes |
| `NO-SIGNALLING.md` | exists; attached to "§2 (NS source stop)", which does not cite it (finding 12) |
| h-bell preregistration (`b27851ea`) | located, untouched; provenance |
| #1169 comment 6791556736 | yes |

Blob prefixes in BS §7 for Substratum (`e5c6f217`), SM (`7d805ac8`), ch18 (`ace0bad4`) and the preregistration
(`b27851ea`) match `cac5d264`. `STATUS-BS.md`'s Main line map and its record of changed cited lines are correct.

## Check 6. Register and claims

No statement presents a native OI result or an OI-wide no-go. §0 says "This is an interface-scoped result, not
a no-go for OI" (BS:45); §3.5 item 1 says Theorem N is "native in form … but not in coverage"; §4.4 routes OI
only through NBA; §5 tags its consequences conditional. The word "native" in the title, in "closed native
screened class" and in "Theorem N (closed native screened ceiling)" invites the misreading the contract warns
against when quoted out of context (the ladder already quotes "closed native form"); finding 14 gives a gloss.
The record is a verification record, so §A.32's paper register does not apply.

## Check 7. Fitness as an item-8 record (#1283 at `f57e576a`)

- **Substantive, nonredundant result.** Met, modestly. Theorem N/N′ instantiate the standard Bell
  factorization argument on Main's cone lemma for a closed system (generators inside the state, complete local
  histories, the whole menu, generator residues). `main` carries only the exogenous theorem; the closed form,
  N′, Lemma G, the §4 bound with its mean, full-history and attainment forms, and NBA's statement are not on
  `main`, and ladder r3 uses Theorem N/N′ (stage 5), §4.1 (stage 5), §4.2 and §3.5 item 5 (stage 6). Parts of the
  record are now redundant with or superseded by `main` (the O2 window, F1, F2). The status note should
  describe the substance as an instantiation of a standard argument, not new mathematics.
- **Scope and limits documented.** Met for the proved core; met for the whole record once findings 1–3 are
  carried.
- **Independent non-author review.** This review supplies it for r2 at `e1534b08`.
- **Accountable Issue, status, remediation.** #868; `STATUS-BS.md` supplies them; its "Known-invalid: none in
  r2" needs the corrections of findings 1–2 recorded.

***

## Findings

**1. should-fix — O1 omits ledger (vii); O1 is closed inside NBA's domain (BS:49–54, :73–74, :246–253,
:410, :453–456).** Under (vii), which is in NBA's stated domain ("ledger posits (i)–(xiii)", BS:232) and was
ledger (vii) at `cac5d264`, a dependence present at one state is present at every state, so `G_φ = G_φ^ref` and,
with (x) on either reading, `G_φ` is simple-cubic. The dichotomy "read globally / read as reference-class
constraint" therefore collapses; H-Bell (i) and Main's adopted branch (a) require an update outside (vii).
This held at the pin; `STATUS-BS.md` lists it under source drift and should instead record it as a correction.
Replacement text:
- BS:49–54: "**O1 — the actual coupling graph.** Main defines `G_φ` by one-step dependence "for some state"
  (Main:364). Under ledger (vii) (linearity, Main:726) a dependence occurring at one state occurs at every
  state, so `G_φ` is the same on every state class and, with ledger (x) on either reading, is the simple-cubic
  graph: no preparation-indexed long edge exists and graph-separated protocols meet (Sep). Main's adopted Bell
  branch (Main §3.3(a)) and H-Bell (Substratum:131–133) need preparation-indexed long edges, so they need an
  update outside (vii). O1 is open only for that branch."
- BS:73–74: "Within its domain, which includes ledger (vii), NBA requires O2 to be resolved and O3 to be
  sourced or posited explicitly; O1 bears on NBA only if the domain drops (vii) (§3.4)."
- BS:252–253, replace the last two sentences of the O1 bullet: "Under (vii) neither reading of (x) admits a
  long edge: a state-dependent edge contradicts (vii), and a state-independent one is an edge of the reference
  graph, contradicting (x). Within NBA's domain O1 is therefore closed and (Sep) reduces to graph separation on
  the simple-cubic graph; H-Bell (i) is open only for an update outside (vii)."
- BS:410 (P-a disposition): "entailed by ledger (vii) with (x) on either reading; the conflict is between (vii)
  and Main §3.3(a)'s adopted branch, not a reading of (x)".
- BS:453–456 (F1), append: "Ledger (vii) already excludes preparation-indexed edges whatever the reading of
  (x), so the adopted branch requires relaxing (vii)." (On `main` at `c3b5f37a`, Main:362, :414 and :724 state
  the scoped (x) and the (vii) consequence.)

**2. should-fix — §0 turns a necessary condition for (B) into a sufficient one (BS:72–73).** "its failure
through a sourced native coupling with complete-history no-signalling would give (B)" omits CHSH > 2.
Counterexample (hand): let `G_B`'s content be a setting bit and a residue bit `ρ_B`, and add an edge from `ρ_B`
into `R_A`. (Sep) fails, yet `h_A` is a function of `(λ*, a)`; under (MI\*) the record law is Bell-local and
complete-history no-signalling holds. §3.4 (BS:267–272) states the (B) lemma correctly. Replacement for
BS:72–74: "NBA would give (A) for OI by Theorem N or N′. A failure of NBA does not by itself give (B); (B) needs
a sourced native coupling that gives CHSH > 2 under (MI) with every-run outputs, together with complete-history
no-signalling for a sourced preparation family (§3.4)."

**3. should-fix — the Level-A disjunction is incomplete (BS:381–385).** Being outside 𝒞_sep and N′'s class can
also mean failing (D), (F), (Gen) or (Rec) (Main's Level-A construction is a global response table, not a
site-factorized protocol with wing regions), and the escape list omits measurement dependence. Replacement:
"By §4, any construction within ε < (√2−1)/4 of the Tsirelson box on a two-wing CHSH experiment lies outside
𝒞_sep and outside Theorem N′'s class: either it is not one site-factorized deterministic map with generator and
fixed record regions in the sense of (D), (F), (Gen), (Rec); or it has a `G_φ` path from a generator region to a
remote record region inside the window; or it fails measurement independence for its response-complete variable
((MI) for Ω under (GI), (MI\*) for λ\* otherwise); or it fails every-run accounting. This is consistent with Main
(C10). Such a Level-A realization is a native spatial realization of separated wings only if O2 is resolved
positively, an update outside ledger (vii) supplies a long edge (O1), or measurement independence is given up
(Main option (b), recorded, not adopted)."

**4. nit — header and pin lines are stale (BS:3–5, :17–19, :23, :421–422, :471–472).** Covered by
`STATUS-BS.md` ("Superseded lines", "Source drift"); its line map is correct. No change needed beyond findings
1–2 being moved from drift to corrections there.

**5. nit — (Rec) should fix regions, window and maps in advance (BS:146–149).** Replacement for the first
sentence: "Wing A's complete record is `h_A = H_A((x_t|_{R_A^t})_{t_s ≤ t ≤ T_A})` for regions `R_A^t`, a window end
`T_A` and maps `H_A`, `π_A` fixed in advance, independent of the state and of the settings." (Ladder r3's (AL4) states
this.)

**6. nit — Theorem N′ is chart-relative and its menu-wide responses come from (MI\*) (BS:185–188, :239–240).**
Add after BS:188: "(MI\*) is relative to the charts; the theorem holds for any charts for which it holds. (MI\*)
also makes every λ\* in its support occur with every menu setting, so `Ĥ*_A(λ*, x)` is defined for the whole
menu." At BS:240: "or (MI\*) for λ\* = (Ω, ρ_A, ρ_B) for some injective charts."

**7. nit — state that (Sep) is the symmetrized, sufficient form (BS:150).** Append: "Here `d_{G_φ}` is the
distance in the symmetrized graph (Main:364), which makes (Sep) sufficient and not necessary for step 1 of
Theorem N: no directed `G_φ` path from `G_B` to `R_A^t` of length at most `t − t_s` suffices." (Review 5857981727's
note; `STATUS-BS.md` carries it under Limitations.)

**8. nit — pre-setting heralds (BS:126).** Replace "Heralds before `t_s` are part of Ω" with: "A herald
recorded before `t_s` enters either as content of W at `t_s`, and so as part of Ω, or as an event the run law is
conditioned on, where it bears on (MI); heralds after `t_s` are local records." (Under bijectivity a past herald
is a function of all of `x_{t_s}`, generator content included, not of Ω alone.)

**9. nit — "Equivalently" (BS:323–324).** Replace with: "In particular `2√2 − 2 ≤ 8ε` for the mean ε, and hence
for the worst-setting ε."

**10. nit — Lemma G uses bijectivity (BS:200–202; compare BS:139).** Insert after "without changing the
counting measure": "(this transport uses bijectivity of `φ`, Lemma 3 and ledger (iii); Theorem N does not)".

**11. nit — C9's hypotheses omit the common law (BS:106).** Hypotheses cell: "(S) full span (unsourced); each
law common across setting interventions (MI); every-run binary first outputs".

**12. nit — two §7 rows attach references no statement uses (BS:427, :433).** Either cite Substratum:171,
:467 in O1 and `NO-SIGNALLING.md` in the §2 no-signalling row, or reclassify those references as provenance
(§A.42 item 8: the claim does not use them).

**13. nit — §5 wording (BS:388–390, :400–401).** BS:389: "Level B fails at every target accuracy below
(√2−1)/4 for any class containing …". BS:400–401: "… needs C11 — a native escape with complete-history
no-signalling and measurement independence kept — or a failure of measurement independence (Main option (b),
not adopted), neither of which is established."

**14. nit — "native" naming and the probe's authority (BS:1, :34, :159, :14–16).** Add to §3.1 after
BS:157: "'Native' in 𝒞_sep and in Theorem N's name means closed (setting generators inside the state, no
exogenous map); it is not a claim that any OI protocol belongs to the class (§3.5 item 1)." At BS:14–16 add: "The
probe was run under a writer assignment whose option text reads "no runs" (#868 comment 6791606126); its
ratification is open, and until then its checks are provenance." (`STATUS-BS.md` carries the second point.)

***

## Not done

- No computation on any OI rule; the probe was not run and no replay was made. G3, G6c and G7's finite objects
  were checked by hand.
- Main's cone lemma and check 11 were read, not re-run; Main's boxed bound was re-derived by hand.
- No primary literature was read first-hand; [L] attributions were checked from recall.
- SB L3, the ladder's Proposition AL and the landing plan were read only for how they use BS; they are not
  reviewed here.
