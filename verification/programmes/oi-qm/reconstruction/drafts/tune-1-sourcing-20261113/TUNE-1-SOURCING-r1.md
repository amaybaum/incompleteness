# TUNE-1 sourcing unit: one candidate for embedded-observer tunable mixing, sourced part by part

**Standing.** WIP / UNVERIFIED author record. Paper and source reading with hand reasoning only:
no computation on any OI rule, no script, no Lean, no manuscript or record edit, no premise
adopted, no claim promoted. Independent non-author review, then ChatGPT review at the exact head,
are the next steps (authority below). Step 3B is not authorized and nothing here evaluates a
candidate against Born statistics, Kochen–Specker contextuality or Bell correlations.

**Verdict (stated in full in §5).** **STOP AT MISSING INGREDIENT.** The candidate is the most
hypothesis-sparing member of TUNE-1's surviving classes (R-lin, initial-condition mode, finite
tori, a designated-cell initial law, heralded witnesses, unbounded control region). Its first
part that OI's stated premises do not supply is the **ready resource**: a native producer of
known-value cells for the apparatus's ready configuration and designated program content, renewed
for every run, in an amount that grows with the demanded precision (the open obligation O-RDY,
Issue #1147). It blocks (b) first; (e) and the physical account of growth in (f) rest on the same
ingredient. The bounded-control result NL-C is accepted, not escaped.

***

## 0. Authority, safeguard and input pins

**Authorization.** Issue #1169 comment 6854241002 (`amaybaum`, author association `OWNER`,
2026-11-13T13:24:47Z), item 1, verbatim:

> 1. **TUNE-1 sourcing unit** (#1236, #866).
>    - **Deliverable:** one concrete candidate for embedded-observer mixing. It states the dynamics, preparation, actual control interface, readout, memory and resource scaling. Each part is marked either as following from OI's stated premises or as unsourced.
>    - The unit must respect the proved scope of the NL-C bounded-control result.
>    - **Stop rule:** if no complete candidate can be identified, it stops at the first precise missing physical ingredient.
>    - Step 3B is not authorized.

and, from the same comment: "**Not authorized:** computation on OI rules, new premises, Step 3B,
priority changes and merges."

**Safeguards carried.**
- #1169 c.6848268369 (ChatGPT scope review, posted by `amaybaum`, 2026-11-13T08:44:28Z): "TUNE-1's
  NL-C remains rule-independent within its per-round bounded-cell label-menu form, including
  emergent controls of that form"; "Separate a mathematically definable construction, an operation
  reachable under one fixed dynamics from stated initial/boundary conditions, and a physically
  derived embedded access/control family."
- Owner-confirmed safeguard for this unit, as relayed by the coordinator (2026-11-13; relay only,
  not located on GitHub in the comments read): the NL-C obstruction "applies to its specified
  per-round bounded label-menu form, including emergent controls of that form. A candidate must
  genuinely escape those hypotheses — state exactly which NL-C hypothesis fails for it, with the
  source showing it fails — not merely call its control region emergent or 'growing'. If it
  cannot, accept the bound and report it." Addressed in node N1.
- #1236 c.6817129920 (`amaybaum`, `OWNER`, 2026-11-12): "**Not in TUNE-1's scope:** continuous-valued
  cells." Applied in node N0.1.
- Prior results kept at their proved scope: TUNE-1 NL-C and NL-C′ (Step 2 Session 4); REC-1 r7's
  separation of definable / reachable-under-fixed-dynamics / physically derived, with measurement
  independence carried as the named hypothesis H-xiv and never derived, μ-G as the
  no-record-constraint case, and OA-3's results finite-ring only; TUNE-1 Step 3A r3 (candidates
  underspecified; §2A embedded-observer framing).

**Input pins.** On `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` (2026-11-13). Paths are under
`verification/programmes/oi-qm/reconstruction/` unless stated; blobs by their first eight
characters.

| Short name | Path | Blob |
|---|---|---|
| Main | `papers/Main.md` | `0db17597` |
| P | `drafts/tune-1-20261111/TUNE-1-STEP2-PROPOSAL.md` | `84f71030` |
| AF | `drafts/tune-1-20261111/TUNE-1-STEP2-AMENDMENT-1-final.md` | `ee8582b2` |
| S3 | `drafts/tune-1-20261111/TUNE-1-STEP2-SESSION3.md` | `a9cbc675` |
| S4 | `drafts/tune-1-20261111/TUNE-1-STEP2-SESSION4.md` | `17ca08f8` |
| T1 | `drafts/tune-1-20261111/TUNE-1-STEP1.md` | `84491c8d` |
| OA1 | `oa-1-20261112/OA-1-REPORT-r5.md` (accepted r5) | `5a16b213` |
| OA2 | `oa-2-20261112/OA-2-REPORT-r4.md` (accepted r4) | `8f8ddf73` |
| OBS | `observer-interface-obsmu-20261104/ANALYSIS.md` | `e657732b` |
| NPS1 | `native-preparation-source-1-20261110/PREPARATION-SCREEN.md` | `8f1edce3` |
| NIS2 | `native-interaction-source-2-20261110/SOURCE-SCREEN.md` | `1daf3861` |
| SUB | `verification/programmes/substratum/continuous-substates/README.md` | `9e84cb4f` |

Off `main` (scoped context; §7 classifies each use):

| Short name | Source | Commit | Blob |
|---|---|---|---|
| REC | `drafts/rec-1-20261113/REC-1-r7.md`, branch `research/rec-1-1169-20261113` (draft PR #1268) | `9f7d2612f39960a41188eae8f3753d9def8019e8` | `f1ffac0e` |
| 3A | `drafts/tune-1-20261111/TUNE-1-STEP3A-r3.md`, branch `research/tune1-step3a-1236-20261113` (draft PR #1267) | `8228b3c24e17a17f324b6779b53b04ad296b4308` | `7bbec04d` |

Neither branch head is an ancestor of `c3b5f37a` (checked with `git merge-base --is-ancestor`).

**Support labels.** [P] manuscript on `main`; [R] research record on `main`, not independently
established (§A.46 item 7), used with its hypotheses; [R-off] research record off `main`, context
only; [W] a paper derivation in the cited record; [W, here] a reading or derivation made in this
file, unreviewed; [L] literature, context only.

**Marking of each part.** *premise*: follows from OI's stated premises (the Definition, Main:42,
and the posit ledger, Main:724), with the derivation cited; *named hypothesis*: follows under an
existing named hypothesis, stated with its status; *unsourced*: neither.

***

## 1. The candidate

**TC-A: designated-program translation gate on the reference rule.** Step 3A's candidate A
(3A:212, :531–632 [R-off]) with every free choice fixed to the option that adds the fewest
unadopted hypotheses, and with the initial law fixed to the form OI's manuscripts already admit as
realization data:

- rule R-lin, `Φ_F(y, x) = (x, Ax − y)`, `A` the nearest-neighbour sum over `ℤ/q`, `q` fixed
  (P:85–89, :131–133);
- carrier `𝓛_fin`, the tori `(ℤ/Lℤ)^3` (P:123–125); no H-∞;
- initial-condition mode: no write outside `Φ_F`, labels are the time-zero content of program
  blocks outside `O` (P:184–199); no H-write;
- initial law of the `D_0` form: designated cells (`O_n` in `r_{O,n}`, every program block in its
  label) at known values, every other cell uniform and independent, which is the statement of MP-0a
  (OA1:556–558) and a law Main:58 admits as realization data; Lemma A-T's coset-uniform hypothesis
  holds for it (S3:58–60);
- heralded Q6′ witnesses (the L5.4 class, S3:196–214);
- a family `{I_n}` with `sup_n |C_n| = ∞` (the part of the class NL-C leaves open, S4:668–674).

**Mechanism.** The observer's choice of a gate angle `θ` is the designated content `c(θ)` of a
program block. That content reaches the control cells only through `Φ_F` and enters every complete
record as the translation `H_P c` (Lemma A-T (a), S3:62–64; OA-1 D5, OA1:176–195); the readout is
the complete history of `O_n` (D4, P:167–171). Tunability in TUNE-1's sense is the target of Q3′
(a gate label for every `θ`, its effect on later identified rounds the rotation by `θ`, AF:161–167)
together with Q4, Q5′, Q6′ (3A:794–805 [R-off] collects them).

**Why this candidate and not another** (node N0 records the checks). Every other surviving class
adds an unadopted hypothesis before the apparatus is reached: H-nl at (a), H-write at (c), H-∞ at
(a), or continuous-valued cells, which are outside TUNE-1's scope. TC-A's dynamics is the ledger
rule, its law is of the admitted realization-datum form, and every operation after time zero is
`Φ_F`, so statement (i) of the embedded framing holds for it (3A:263–266 [R-off]; Main:42).

***

## 2. The six parts and their sourcing

Line references are at `c3b5f37a` unless marked [R-off].

| Part | Content for TC-A | Marking | Sources |
|---|---|---|---|
| **(a) Dynamics** | `φ = Φ_F` (R-lin) on `(ℤ/Lℤ)^3`, alphabet `ℤ/q` fixed; one fixed rule, no coupling fitted | **premise** (ledger posits, not derived): items (ii) total finiteness, (vii) linearity, (viii) site factorization, (x) nearest-neighbour range, (xiii) second-order form. The alphabet is fixed per verdict (imported convention). Each precision uses a different torus side `L` (a different finite world, P:123–125); one world for every `ε` would need H-∞ (named, unadopted) | Main:724; P:85–89, :123–125, :131–133; S3:58 |
| **(b) Preparation** | The ready configuration `r_{O,n}`, the designated content of every program block, the heralded preparation prefixes credited at conditional error `ε`, and run repetition | **First stop: the ready resource is missing.** OI's stated premises do not supply known-value cells: under posit (iv) read as μ-G no region holds a fixed pattern except with probability `|S_X|⁻¹`, at every time (Lemma P-1). The only existing names are MP-0a (named in OA-1, not adopted; "Hard to vary? No"; a new §A.29 premise once a concrete law is selected) and the open identification H-PREP; a native producer is the open obligation O-RDY (#1147, not authorized). Heralding cannot replace the supply: the program blocks are outside `O` and not read (P:192), so the observer cannot condition on their content; an event fixing every designated cell would in any case have probability `≤ (4ε/(1−4ε))^{K+1}` per run under μ-G (F-S2), and a herald on `r_O` must be held at use, which is (e). Run repetition from spatial copies is derived given a supply per copy (N3.6) | OBS:529–545 (Lemma P-1), :100, :121, :893–901 (H-PREP); OA1:145–160 (D2, D3), :556–562 (MP-0a); Main:54, :58, :724 item (iv); REC:222 (C11) [R-off] |
| **(c) Control interface** | What the observer varies: the designated content `c(θ)` of its program blocks, one block per gate round; how: `Φ_F` carries it to `C_n` and it acts on the record by translation `H_P c` | Mechanism: **premise** (derived, law-free: Lemma A-T (a); D5). The content's source: as (b) (blocked there). Independence of the unread world from the labels: **named hypothesis** H-μ (unadopted), contained in MP-0a's clause "independent of setting and carrier"; the labels are designated constants and protocols are non-adaptive, so the feedback and herald-conditioning cases of H-xiv do not arise (H-xiv itself is not derived here). Label encoder `θ ↦ c(θ)`, layout, `O_n`, `C_n`, `τ`: **unsourced** (chosen by the family's specification; no member exhibited). Whether translations supply the one-axis rotation family with Q3′, Q4, Q5′, Q6′: **open mathematical question L5.4**, not a physical ingredient. NL-C: accepted at every interface (N1) | S3:56–98, :196–214; OA1:111–114, :176–195, :556–558; P:145, :147–153, :184–199, :211–222; REC:223 (C12) [R-off]; S4:423–474 |
| **(d) Readout** | The complete history of `O_n` at every tick (D4), Lüders reads as labels `c_a, c_b`; outcome probabilities the pushforward of the `D_0` law through `Φ_F` | The read rule: **imported** from the Definition (`O` plays the visible sector, Main:42; D4/D5 forbid declared restrictions). Outcome probabilities: derived given the law. That the outcome is *held* at use time: as (e) | P:167–171, :272–280; AF:153–160 |
| **(e) Memory** | The whole history of `O_n` over `K` rounds (`Kτ` configurations of `O_n`), every herald and acceptance record, held to the end | **named hypothesis** MP-0b only: "The visible history counts as held, outside `V`" (interface convention; status undetermined). It places the records outside the observer, which statement (i) does not provide. An in-`V` complete history under μ-G is subject to D4(b): it excludes hidden influence on `V`; D4(c) names the cost as blank memory, MP-0a. So (e) rests on the same ingredient as (b) or on a convention | OA1:162–175 (D4), :563–564 (MP-0b); 3A:501 [R-off]; REC:217 (C6) [R-off]; Main:42 |
| **(f) Resource scaling** | Control cells `|C_n| ≥ ½ log_q((1−4ε)/(4ε))`; sites `N ≥ (K+1)|C_n|`; known `q`-ary cells per run `≥ (K+1) log_q((1−4ε)/(4ε))`; under μ-G, probability `≤ (4ε/(1−4ε))^{K+1}` per run of any event fixing every designated site; with a fixed supply of `D` known cells per run, `ε ≥ 1/(4(1 + q^{D/(K+1)}))` | The necessity of growth: **premise**-level consequence of NL-C′ ([W], Step 2) and of the schema; the known-cell, acceptance and floor bounds: [W, here] (F-S2). The physical account of the growth: **unsourced**. MP-0a declares a larger designated region at each `n`; no mechanism in `Φ_F` produces it, and on `𝓛_fin` each `n` is another world | S4:464–474; P:143, :184–199, :211–222; OA1:156–160 (D3) |

**Status of the candidate as a whole.** Parts (a) and the mechanism of (c) follow from the stated
premises. Part (b) does not, and it is the first such part in the order (a)–(f). Parts (c)'s
content, (d)'s held outcomes and (e) depend on the same ingredient. The specification gap of Step 3A
(no member exhibited) and the mathematical gap L5.4 remain and are not physical ingredients.

***

## 3. Depth-first branch log

**Productivity test, fixed before node N0 (§A.31).** The unit is a gem iff it yields, for the
selected candidate, a fact strictly stronger than the restatement "Step 3A candidate A lacks a
sourced apparatus and is underspecified" (3A:212, :628–632 [R-off]) that either constrains what any
embedded-tunability candidate must contain or exposes a hidden assumption. Otherwise it is
recorded only.

### N0. Candidate selection (decisive branch: which class adds fewest unadopted hypotheses)

- **N0.1 Continuous-valued cells** (SUBSTATE-1's real-type sub-states; Step 1's two-mode drive).
  Check: #1236 c.6817129920, "Not in TUNE-1's scope: continuous-valued cells"; P:114–118 excludes
  real-valued sites, an isolated pair, a loaded coefficient and per-site continua from the rule
  class because Step 1 shows each unsourced. **Closed** (out of scope; not evaluated).
- **N0.2 A non-affine rule** (R-nl; the native-Y rule `H(A,B,D) = (B, D, A ⊕ BD)` of the native
  apparatus records). Check: R-nl enters only under H-nl, which replaces ledger item (vii) and is a
  Layer-0 revision (P:90–112); the native-Y rule is "a declared dynamics input"
  (`measurement-record-formation/LA-EQUAL-REVIEW.md`:241). Part (a) would be unsourced at once.
  **Not selected.**
- **N0.3 Exchange mode.** Check: per-round writes are H-write, "a classical write access to `C`
  that `Φ_F` does not supply" (P:155–167); statement (i) fails for that apparatus (3A:413–420
  [R-off]). Part (c) would be supplied. **Not selected.**
- **N0.4 `𝓛_∞`.** Check: H-∞, named and unadopted (P:126–129). **Not selected**; its one relevance,
  a single world for every `ε`, is recorded in (a) and (f).
- **N0.5 Selected:** R-lin, initial-condition mode, `𝓛_fin`, `D_0`-form law, heralded witnesses,
  unbounded `|C_n|` (TC-A, §1).

### N1. The NL-C safeguard: does TC-A escape a hypothesis of NL-C?

NL-C's hypotheses (S4:451–458; restated for R-lin at S4:645–650): a declared target with a gate
label for every `θ` and Lüders reads `a, b` with `a·b ∈ [−½, ½]`; Q6′(i) with its credit on `𝒯_L`;
the finite menu `(V × V)^C` with `|C| ≤ c`; identified tests whose labels do not depend on the
preparation's records; `K ≥ L + 1`. It uses no rule, law or carrier (S4:457–458).

- **N1.1 Per-interface hypotheses.** Check against §1: each gate is one round with one label (the
  content of one block, P:184–199); labels are configurations of `C_n`; TC-A declares the full
  target; its identified tests' labels are designated constants and so do not depend on any record.
  **Every per-interface hypothesis holds. NL-C applies to every interface of TC-A. Accepted:** at
  precision `ε`, `|C_n| ≥ ½ log_q((1−4ε)/(4ε))` (NL-C′, S4:464–474).
- **N1.2 The family-level condition.** The `FAIL-CLASS` rows assume `sup_n |C_n| ≤ c`
  (S4:642–643). TC-A violates it by construction. This is compliance with NL-C′, not an escape
  from NL-C; the growth it requires is part (f), and its source is the question of (b).
- **N1.3 Gates over several rounds** (outside TUNE-1's schema, S4:697–698). [W, here] NL-C's
  proof (S4:428–450) uses the gate's setting only through steps 1–2 (a finite menu, pigeonhole on
  `M + 1` angles) and step 6 (equal settings give equal world laws, since the identified test's
  labels do not depend on the preparation's records). Read with "gate setting" for "label", the
  same steps apply to a gate occupying `m` rounds, whose setting is a sequence in
  `((V × V)^C)^m`, provided `𝒯_L` admits the `m`-round test. For fixed-length gates
  `M = q^{2m|C|}` and the bound becomes `m|C| ≥ ½ log_q((1−4ε)/(4ε))`; variable lengths up to `m`
  at most double `M`. Splitting a gate over rounds moves the growth from space to time; it does not
  remove it. Unreviewed reading.
- **N1.4 Settings not encoded as cell configurations.** Check: "A setting is a configuration of
  designated cells" (OA1:111), from the Definition (Main:42) and the absence of writes outside `φ`
  (OA1:111–114; REC:215, C4 [R-off]). For an embedded observer there is no other encoding. Closed.
- **N1.5 A setting-dependent duration** (tuning `θ` by how long a coupling acts). Check: under an
  affine rule "the non-translational part of the carrier's map does not depend on `c`" (D5 (i),
  OA1:176–183), so stored content cannot change which linear map acts or for how long; "Selecting
  by timing turns the setting into a different preparation procedure", and without a change of
  `φ`'s action every "selectable" read is a coarse-graining of one joint record (D7,
  OA1:202–208). Closed for R-lin.
- **Verdict N1.** TC-A does not escape NL-C; it accepts the bound and grows. No NL-C hypothesis is
  claimed to fail except the family-level `sup_n |C_n| ≤ c`.

### N2. Part (a)

Check: R-lin is "the instance of Main §3.2 at `q = 2` … and the exact rule of SM:296 with `α = 1` at
general `q`", linear (item (vii)), translation-invariant, range one, site-factorized (P:85–89); each
is a ledger item (Main:724). **Premise** (posit-relative). Noted: on `𝓛_fin` the side grows with
`n`, so "one fixed substratum for every precision" is not met without H-∞ (P:123–129).

### N3. Part (b): where do the designated known cells come from? (decisive branch)

The candidate's schema requires a fixed ready configuration `r_O ∈ (V × V)^O` (P:143) and, in
initial-condition mode, program blocks whose content is the label sequence; the blocks lie outside
`O` and are not read (P:184–199), so their content must be fixed in advance rather than recorded.

- **N3.1 Posit (iv) as μ-G.** Check: Lemma P-1 (OBS:529–545 [R]): for a finite abelian `S`, an
  automorphism `φ` and the uniform law, every region is uniform at every time, disjoint regions are
  independent, and a fixed pattern on `X` has probability `|S_X|⁻¹`. OA-1 D3: point-preparing `M`
  `q`-ary cells costs `P(E) ≤ q^{−M}`; "Ready cells under μ-G cost exactly this" (OA1:156–160).
  **No ready region exists under μ-G at any time; a bijection cannot produce one.** Heralding is the only
  route under μ-G, and it is not available for the program blocks, which lie outside `O` and are
  not read (P:192); for `r_O` it costs F-S2's bound and the herald must be held at use (N5, part (e)).
- **N3.2 μ-O (derived, Main:54).** [W, here] μ-O is uniform on the actual orbit; a cell is
  known under it only if its value is the same at every point of the orbit, i.e. constant on the
  actual trajectory. Such a cell is never written, so it is not a consumable ready supply. A
  time-specific conditional law needs a held record event (D1, OA1:141–143). No ready supply.
- **N3.3 μ-R (posit (iv) as stated, Main:724).** Known values are the observer's records; the law
  "presupposes 'the observer's records', whose formation is the question" (REC:220, C9 [R-off]);
  "using a ready record to supply readiness may be circular" (NPS1:85, citing OBS §4.6.2–4.6.3).
  Undecided; no source.
- **N3.4 A structured prior as realization datum (MP-0a).** Check: Main:58 admits "its own fixed
  hidden prior `μ_H` as part of the realization datum"; OA-1 states MP-0a as "fixed known values on
  designated cells, independent of setting and carrier, uniform elsewhere", physical content "a
  past-hypothesis-type supply of ready cells", not supplied because "μ-G is not that law", and
  "Hard to vary? No" (OA1:556–562). H-PREP, identifying a laboratory preparation with an
  in-realization conditional, is an explicit open hypothesis (OBS:893–901). A concrete candidate
  must select its designated values; selecting is a new §A.29 premise (REC:222, C11 [R-off], which
  rests on OA1:556–562 and Main:58). **Covers (b) only as an unadopted named hypothesis.**
- **N3.5 A native producer on `main`.** Searches (§6) for ready/blank supplies, erasure, cooling
  and low-entropy sources. Findings: O-RDY is an open obligation, "a ready resource", with "H-μ has
  no ready region" (OBS:100, :121); the two native source screens on `main` that tested a producer
  stopped there, for another rule (the selected binary ring): "no producer of this ordered bank,
  its common incoming law and selectable request is identified" (NPS1:14), and "Renewal, retry/reset
  or fresh ordered bank: Unsourced. Mathematical invertibility grants no selectable inverse or free
  blank supply" (NIS2:132). A cosmological low-entropy boundary "does not specify which local
  fields are blank" (NPS1:88). No record on `main` supplies a producer for R-lin.
- **N3.6 Run repetition, given a supply.** [W, here] Place apparatus copies on one torus at mutual
  graph distance greater than twice (radius of `O_n ∪ P` plus `Kτ`). Under a `D_0` law the unread
  cells of distinct copies' dependence cones are disjoint and independent (product law; range one,
  ledger (ix), (x)), so the copies' records are independent and identically distributed. This
  derives F-3A-2's repetition (3A:969–986 [R-off]) from the product form, given one designated
  region per copy; reuse of one apparatus would need a reset, which NIS2:132 records as unsourced.
- **Verdict N3. STOP.** The first missing physical ingredient is the ready resource: a native
  producer of known-value cells for `r_{O,n}` and the program blocks, renewed per run. It is not
  supplied by the stated premises (N3.1–N3.3), is covered only by the unadopted MP-0a or the open
  H-PREP (N3.4), and its general form is the open, unauthorized obligation O-RDY (#1147; N3.5).

### N4. Statuses past the stop (read from existing records; no derivation attempted)

The rows (c)–(f) of §2 are read from existing records so that the deliverable states every part;
nothing after N3 is derived beyond F-S2's arithmetic. Two items there are not physical ingredients
and are not the stop: the member specification (encoder, layout, `O_n`, `C_n`, `τ`), which Step 3A
records as existentially quantified (3A:896–905 [R-off]), and L5.4, which the owner left open
("Record and leave", S4:12). Context, not used for the verdict: if a member were specified and met
OA-2 Theorem E(b)'s hypotheses with (SP), its prepare–measure fragment would be simplex-embeddable
(OA2:522–576 [R]); the (SP) question is REC-1's separately authorized P0.

### N5. Pressure test of the favourable readings (§A.31)

- **"MP-0a is admitted by Main:58, so (b) is sourced."** Rejected. Main:58 admits structured priors
  as data; it does not derive one. OA-1 states why μ-G is not that law and that MP-0a carries no
  quantum content and is not hard to vary (OA1:556–562). Adopting it is outside this unit.
- **"The observer is in some configuration anyway; conditioning on it prepares the apparatus."**
  Conditioning on the present visible value gives `δ_r ⊗ unif(C_H)` (OBS Lemma Q-b1, :906–910) and
  prepares nothing outside the cut; the owner's scope for the native preparation screen states that
  "An inverse image, conditioned event, imposed blank field or statistical weight is not a
  producer" (#866 c.6765161496). Self-heralding also needs the herald held at the end of the run,
  which is part (e). Rejected as a source; its cost is F-S2.
- **"Growth is explained: a finer apparatus is a larger designated region."** Rejected as a physical
  account. On `𝓛_fin` each `n` is a different world (P:123–125); within one world the designated
  supply `D` is fixed, which gives the floor of F-S2.
- **"The control is native."** Partly. The action is native and law-free (translation). The choice
  is an initial condition, as P:194 states ("Every observer choice is then an initial condition"),
  so what the observer varies is supplied with the ready resource.

***

## 4. Findings and classification (§A.31)

- **F-S1 (ELABORATING).** [W, here; N1.3–N1.5] NL-C's counting step does not depend on a gate
  occupying one round: for `m`-round gates the bound reads `m|C| ≥ ½ log_q((1−4ε)/(4ε))`. Settings
  are cell content for an embedded observer (OA1:111), and under R-lin a setting cannot change a
  coupling's duration (D5, D7). So the two routes Step 3A left open as possibly escaping NL-C
  (3A:436–439 [R-off]: gates over several rounds; settings not encoded as cell configurations) do
  not escape its counting bound. Assumption-watch marker AW-SRC-1: an embedded control at precision
  `ε` needs at least `½ log_q((1−4ε)/(4ε))` cells of setting content per gate, spread over space or
  time.
- **F-S2 (ELABORATING).** [W, here; arithmetic on NL-C′, the schema and D3] Under initial-condition
  mode the designated sites per run number at least `|O_n| + K_n|C_n| ≥ (K + 1)|C_n|`, each with two
  `q`-ary components, so the known `q`-ary cells per run number at least
  `2(K + 1)|C_n| ≥ (K + 1) log_q((1−4ε)/(4ε))`. Consequences:
  - under μ-G, any event that fixes every designated site of a run (a herald, were the program
    blocks readable; P:192 places them outside `O`) has probability at most
    `q^{−2(K+1)|C_n|} ≤ (4ε/(1 − 4ε))^{K+1}`;
  - with a supply of `D` known `q`-ary cells per run, `ε ≥ 1/(4(1 + q^{D/(K+1)}))`.
  The growth of the control interface that the owner asked to be physically explained
  (c.6828822665) is therefore a growth of the ready resource at this rate: the two unsourced items
  Step 3A lists separately (the ready configuration and the growth of `|C_n|`, 3A:493, :505
  [R-off]) are one resource. Assumption-watch marker AW-SRC-2: any candidate with a declared ready
  configuration and designated settings inherits O-RDY at least at this rate.
- **F-S3 (CONFIRMING).** The first stop coincides with OA-1 gap 1 (OA1:522), with O-RDY (OBS:100,
  :121; #1147), and with the first stops of NPS1 and NIS2 for a different rule. The same
  ingredient blocks embedded preparation under the reference rule and under the selected binary
  ring.
- **F-S4 (BORDERLINE).** [W, here; N3.2] Under μ-O the only known cells are orbit-constant cells,
  which are never written.
- **F-S5 (CONFIRMING).** Spatial copies under a `D_0` law give independent runs (N3.6), reducing
  F-3A-2's repetition to one designated region per copy.

**Productivity verdict: gem (ELABORATING).** F-S1 and F-S2 are strictly stronger than the fixed
restatement and constrain every embedded-tunability candidate: no candidate escapes NL-C's counting
by splitting gates or re-encoding settings, and the growth NL-C′ forces is a growth of the ready
resource at a stated rate. Both are unreviewed [W, here]. Correctness bands unchanged; this is
consistency-axis work.

***

## 5. Verdict

**STOP AT MISSING INGREDIENT.**

- **Candidate.** TC-A (§1): R-lin on finite tori, initial-condition mode, `D_0`-form initial law,
  heralded witnesses, unbounded control region; gate angles chosen as designated program content
  that acts by translation.
- **NL-C.** Accepted, not escaped: every per-interface hypothesis holds; only the family-level
  `sup_n |C_n| ≤ c` fails, by the growth NL-C′ requires (N1).
- **Missing physical ingredient.** The **ready resource**: a native producer, inside the joint
  dynamics, of known-value cells for the apparatus's ready configuration and designated program
  content, renewed for every run, numbering at least `(K + 1) log_q((1−4ε)/(4ε))` `q`-ary cells per
  run (F-S2). OI's stated premises do not supply it (N3.1–N3.3); the corpus names it only as the
  unadopted MP-0a, the open H-PREP, and the open obligation O-RDY (#1147).
- **Parts blocked.** (b) first. (e) rests on the same ingredient, or on the convention MP-0b, which
  holds records outside the observer. The physical account of growth in (f) is the same ingredient.
  (c)'s content and (d)'s held outcomes inherit it.
- **Not physical ingredients, and still open.** The member specification (encoder, layout, `O_n`,
  `C_n`, `τ`) and L5.4. Neither is the stop.
- **Step 3B.** Not eligible: the candidate is not sourcing-complete. Nothing here proposes a
  premise.

***

## 6. Reading inventory and method (§A.19)

**Read at `c3b5f37a`.** P in part (:80–222, the interface schema); S3 :52–100 and :194–232;
S4 :405–480 and :560–767; T1 :148–314 and search hits for tunability; OA1 :1–12, :90–300,
:515–600; OA1 `STATUS.md`; OBS :1–30, :100, :121, :456, :525–546, :888–912; NPS1 and NIS2 by search
for their stop lines and source tables; SUB in full; `continuous-substates/native-coordinated-affine-apparatus.md`
in full and the heads of six other `native-*.md` units; Main :42, :48, :54, :58, :582, :724, and
search hits for tunability and mixing. OA2 by search for Theorem E. Issues #1236 (body and all 11
comments), #866 (body; 69 comments scanned by search for tunability, ready, blank, low-entropy,
O-RDY), #1147 (body), #1169 c.6854241002 and c.6848268369, through the GitHub API, read-only.

**Read off `main`.** REC in full; 3A in full.

**Searches** (`git grep` at `c3b5f37a` over `papers`, `book`, `verification`): `ready
(cell|region|supply|resource)` (93 files), `blank (memory|cell|bank|supply)` (9),
`erasure|cooling|Landauer` (36), `low-entropy` (24), `H-PREP`, `A XOR BD`. Hits bearing on a
producer of known cells were read at their source scope; the "no producer for R-lin" statement of
N3.5 is scoped to these searches and the records read.

**Not read.** MECH-1, MECH-2 and apparatus-1 beyond Step 1's and REC's citations; OA-3; the
native-Y package; Issue #914's O-RDY row; the book's Chapter 18 (cited through NPS1:86–88).

**Commands.** `git rev-parse`, `git show`, `git ls-tree`, `git grep`, `git merge-base
--is-ancestor`, `git ls-remote`, `git archive` (failed extraction, then `git show` per file),
`curl` reads of the GitHub API, `python3 -I` used only to print JSON fields of the issue reads and for two literal text substitutions in this file,
`sed`, `grep`, `wc`, `cut`, `cat`. No computation on any OI rule; the arithmetic of F-S2 is by hand.

***

## 7. §A.42 item 8: references to content off `main`

| Reference | Used where | Classification |
|---|---|---|
| REC (`REC-1-r7.md`, blob `f1ffac0e`, at `9f7d2612`, draft PR #1268): the three-way separation and constraints | §0 safeguards | Governance and scope provenance; the separation is the owner's (#1169 c.6848268369). |
| REC:215 (C4) | N1.4 | Support on `main` for the statement used: OA1:111–114 and Main:42; REC cited as agreeing. |
| REC:217 (C6) | (e) | Support off `main` for the status word "undetermined"; the content used (MP-0b is an interface convention) is OA1:563–564 on `main`. |
| REC:220 (C9) | N3.3 | Support off `main` for the under-specification reading; N3.3 reaches no verdict on μ-R. |
| REC:222 (C11) | (b), N3.4 | Support on `main` for MP-0a's content and status (OA1:556–562; Main:58); REC cited for the phrase "new §A.29 premise if selected". |
| REC:223 (C12) and H-xiv | (c) | Provenance for the name H-xiv; the hypothesis used is H-μ (P:145, on `main`) and (xiv) (Main:724). |
| 3A (`TUNE-1-STEP3A-r3.md`, blob `7bbec04d`, at `8228b3c2`, draft PR #1267): candidate A, §2A statement (i), the T1 conditions | §1; §2; N0.3; N1.3; N4 | Support on `main` for each property used: R-lin, the schema and the classes (P:85–222; S3:196–214; S4:568–674); statement (i) from Main:42. 3A is the source of the candidate's name and of the formulation of statement (i): support off `main`, a gap until landed. |
| 3A:493, :505, :969–986 (F-3A-2) | F-S2; N3.6 | Provenance: the restatement F-S2 and N3.6 improve on; their content is derived here from on-`main` sources. |
| 3A:436–439 (NL-C's open routes) | F-S1 | Provenance: the question; F-S1 rests on S4:423–474 and OA1:111, :176–208 on `main`. |
| 3A:896–905 | N4 | Support off `main` for "no member is exhibited"; on `main` S3:196–214 and S4:485–497, :668–674 state the same for the classes. |
| Issues #1169 c.6854241002, c.6848268369; #1236 c.6817129920, c.6828822665 | §0; F-S2 | Governance provenance, quoted. |
| Coordinator relay of the owner safeguard (2026-11-13) | §0; N1 | Governance provenance, relay only. |
| #866 c.6765161496 | N5 | Governance provenance (an owner scope statement), quoted. |
| #1147 body | (b); §5 | Planning provenance for the obligation's name and status; the content used is OBS:100, :121 and Lemma P-1 on `main`. |
| `measurement-record-formation/LA-EQUAL-REVIEW.md`:241 | N0.2 | Support on `main`. |

This record cites no off-`main` content as the sole support of its verdict. Before any landing,
each row marked "support off `main`" is closed by landing its source or narrowed (§A.42 items 2, 8).
