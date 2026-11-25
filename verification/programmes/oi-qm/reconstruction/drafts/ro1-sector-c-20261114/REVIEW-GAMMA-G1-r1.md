# Review of GAMMA-1 unit G1, r1 (definitions)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/GAMMA-G1-r1.md`
at PR #1294 head `1dcd7c686a66766d554b9f8d6fd43719ef5e665d`, blob
`46697d9c76892914cd2719f768373c836b952d17` (cited G1:N). The branch head moved during the review to
`213e3981` (a later commit adding U4 hand calculations r2); the G1 blob is identical there, and
nothing from that commit was used.

**Governing inputs, blobs checked at `1dcd7c68` against G1's input list:** GAMMA-PLAN-r1
`77f1fcd8` (PLAN-G:N), S3-U1-r5 `68983f86` (U1:N), S3-U2-r3 `2711c168`, LIT-ERASER-r3 `2b414173`
(LIT), S3-U4-r1 `e6d8101a` (U4) and REVIEW-S3-U4-r1 `63c95b30` (RU4). All match. Corpus at
`origin/main` `75cc5100`, read with `git show`: `papers/Main.md` blob `0db17597`; SUBSTATE-1
`observation-context-protocol.md` blob `6ca6f0ab` (OCP:N); MR★ blob `45af1678`; MR-1 preregistration
(PREREG:N); QB3-EVIDENCE (QB3:N). Owner records #1169 c.6891808569, c.6891710167 and c.6891338304
were read through the API; the quotations G1 gives from them are accurate.

**Reviewer.** Independent, non-author. Read-only; every check is by hand. No computation, Lean,
manuscript or Issue change.

## Verdict: REVISE

The frame is sound and well sourced: one observer family for all protocols, full-mass laws, κ fixed
in advance with no amplitude or Born input, the two directions kept apart, and every verdict reported
per instance. The NEW finding G1-F1 is correct against LIT and the two experiments read in full.
Four definitions are wrong as stated, though, and in a unit whose whole product is definitions they
need a re-checked r2:

- the coverage credit set, applied per phenomenon, makes (γ←) unsatisfiable even for quantum
  mechanics (finding 1);
- the operational path knowledge `K_P` does not reproduce Schwindt's `K = 2L − 1`, and can be 0 for
  a perfect marker (finding 2);
- the mass bookkeeping fails under the E-read and E-prep encodings (finding 3);
- NC-rep is identified with U4's time-indexed accessibility reading, contrary to G1's own §2.1
  (finding 4).

Findings 5 to 9 are required corrections of scope, conditionality or sourcing. None of them
overturns a stated outcome. The changes are local.

## Findings

### Required

**1. The per-phenomenon credit-set condition in (γ←) over-reads owner Q6, and no model can satisfy
it (G1:438–441 against G1:502–510).** (γ←) requires, for **every** listed `Φ`, that "`Φ` lies in the
coverage credit set of §7.2", which is the set of observables on which PC-wave does **not** agree.
G1 itself records that PC-wave passes the fringe statistics and "the fringe-build-up shape of X-1"
(G1:475). So X-1 can never enter the credit set, and (γ←) over a list that contains X-1 is false
for every model. The quantum benchmark fails it as well, since its X-1 agrees with PC-wave. The same
probably holds for X-4, because classical polarization optics reproduces a Schwindt-type `V`–`K`
trade-off (reviewer's inference, not checked in a source). Q6 says "compatibility with classical
waves alone does not establish quantum coverage" (c.6891808569). That is a condition on the coverage
result as a whole, which §7.2 already states correctly: where the credit set is empty, the result
"does not count toward the coverage half". It is not a membership condition on each phenomenon.
- *Required change.* Drop the per-`Φ` credit-set clause from (γ←). Keep §7.2's global rule: a
  coverage result counts toward AC-1 only if its credit set is nonempty. Add a satisfiability
  countercontrol for the definition: the OCP benchmark family, used only for the structure of the
  definition (NC-γ2), must be able to meet (γ←)'s definition. Otherwise the definition excludes
  quantum mechanics itself.
- *Also fix in §7.2.* An observable enters the credit set only when PC-wave's disagreement is
  established through the same κ, not when PC-wave's result is unknown. This matters for X-2 and
  X-3, whose PC-wave entries G1 leaves to G3 (G1:477–478). It should also be stated whether the
  classical eraser models (CC4, CC5 at VER2's scopes; G1:509–510) and C0 also remove an observable
  from the credit set. "Reported the same way" leaves that open.

**2. `K_P` as defined is not Schwindt's knowledge, and it breaks NC-copy (G1:176 against LIT 1.12,
1.8; G1:487–488).** G1 defines `K_P` as "the total-variation distance between the marker-record laws
of a2P and a3P, each normalized by its own incident mass". For a fixed partition with equal priors,
total-variation distance equals `2L − 1`. That part is correct. The incident-mass normalization is
not. Hand check with OCP's convention (closing an arm discards half the incident flux) and a perfect
marker:
- marker after the block: a2P has `(∅: 1/2, L: 1/2)` and a3P has `(∅: 1/2, R: 1/2)`, so `K_P = 1/2`;
- marker before the block: the blocked runs also carry their path mark, so both laws are
  `(L: 1/2, R: 1/2)` and `K_P = 0`.

Schwindt's `K` comes from detector counts with the path blocked and the analyzer in place, corrected
by the efficiency ratio 1.11 ± 0.01 (LIT 1.12). That is, it is a ratio within detected runs. Ma's
path probabilities are conditioned on Det 4 (LIT 1.8). So `K_P` as written is at most the detected
fraction and depends on where the block sits. NC-copy's required "`K_P = 1`" (G1:488) is then
unreachable, and NC-noise's separation "by `K_P`" (G1:496) reads a different statistic from the one
measured.
- *Required change.* Define `K_P` and `K_C` by the stated raw-count formula of §5.5 (G1:361):
  marker-outcome frequencies among runs with a screen detection in a2P and a3P, with the efficiency
  input as §5.4 has it. Compute this from the full-mass law, as a ratio of masses. That is a derived
  quantity under a stated formula, not a renormalized law, so NC-γ4 holds. Take the priors from the
  a2P and a3P detected masses at equal incident flux, not "equal priors" by assumption; Schwindt's
  `L` includes the a-priori predictability.
- *Also note (advisory).* `K_C = 0` (G1:177) is met by the trivial partition, which is not a
  read. It is necessary for "complementary", not sufficient.

**3. Masses and normalization are not defined for E-read and E-prep (G1:205–215, :319–324,
:531).**
- *E-read.* §3.2 defines `L_a` by restriction to `z(x) = a`, with total mass `μ(z = a)`, and asserts
  `L = Σ_a L_a`. Under E-read, a4, a5 and a6 are the **same runs**: one setting value `z*`, three
  readouts (§3.3). The laws `μ(z = a5)` and `μ(z = a6)` are then undefined or 0. `κ_norm`'s
  denominator `μ(z = a ∧ E)` (G1:319) is wrong for a5 and a6. And `Σ_a L_a` counts those runs three
  times, on three different record spaces (with `m` entered or not).
- *E-prep.* G1:209–210 restricts to the executed herald `E_a` and also keeps `¬E_a` "as an outcome".
  Inside the restriction `{E_a}`, `¬E_a` has no mass. The total mass of `L_a` and the denominator are
  not stated.
- *Consequence.* NC-γ4's checkpoint ("`L_a`'s total mass equals `μ(z = a)`", G1:531) is defined only
  for E-set.
- *Required change.* Give each encoding its incident event and total mass. For E-read, a4 to a6 share
  `z*` and `μ(z* ∧ E)`, and they enter the joint decomposition once. For E-prep, restrict to the
  preparation attempt for `a`, with the herald outcome as a record component. Restate NC-γ4's
  checkpoint per encoding.
- *Minor, same place.* §3.1 defines `L_a^full` as the law "with `m` retained" (G1:192–193), while
  §3.3 uses `L_{a4}^full` with `V_A`'s **full configuration** retained (G1:224–226). The sum rule for
  both `π_P` and `π_C` needs the latter, or a common refinement. Align the two.

With 3 fixed, the two claims of §3.3 check out by hand. Under E-read,
`L_{a5} = (id × π_P)_* L_{a4}^full`, and summing over `m` gives the `V_A` marginal of
`L_{a4}^full`, which is `L_{a4}` by definition. The same holds for `π_C`. So the screen marginals
are equal and the full-mass sum rule holds, `∅` included. These are identities of the pushforward,
as G1-F2 says (ELABORATING, bookkeeping). The raw-data caveat (marker efficiency, coincidence
window; RU4 finding 8) is correctly carried.

**4. NC-rep is not the time-indexed accessibility reading under G1's own conventions (G1:484–486;
U4 §6.3; RU4 finding 6).** U4 §6.3's reading predicts "fringes while the record is parked", that is,
while `V` does not hold it, and their loss when it returns. RU4 finding 6 fixes it as "whether `V`
holds the record at the recombination tick". G1 §2.1 places a stored, unread marker **in** `V_A`
("held by `V_A` and omitted from the compared record ... not moved into the hidden sector",
G1:115–116). Under G1's a4, then, the time-indexed reading predicts **no** fringes, which is the
opposite of NC-rep's a4. NC-rep would correspond to that reading only for a parked marker, and G1
defines no parked-record protocol (G1:160–163).
- *Further.* G1 then says this family "disagrees with the T-sing unread-marker data as read
  (Schwindt; LIT C1, C5)". That holds for NC-rep as a law family, since Schwindt's unconditional `V`
  is near zero at full marking with the analyzer removed. It does not carry over to the
  accessibility reading. LIT C5 states explicitly that whether these data disconfirm that reading
  "depends on how that reading classifies a marker that is unread but readable in principle".
- *Required change.* Delete the identification, or restrict it to a parked marker with that protocol
  named as undefined here (PROVISIONAL). Keep the disagreement with Schwindt for NC-rep itself. Note
  also that Schwindt's `V` is background-subtracted (LIT 1.12). Under G1's own §5.4 rule, the
  comparison is made with the stated background (100–400 s⁻¹) added back, or not made.

The rest of the NC-rep entry checks out. With `Δ ≠ 0`, E-read forces equal a4 and a5 screen
marginals, while NC-rep requires `c_{a1}` against `c_{a2} + c_{a3}`, which differ by `Δ`. So NC-rep
has no E-read realization, in any model and not only a bare one. The dilation realizes it with
per-family actions (Main:480–482), so representability tests nothing.

**5. The ready screen has a visible-herald route on record, and G1 omits it (G1:259, :269, :308–309;
U1:284–285, :300–304).** U1 records, at [M-r], that visible cells are prepared "Native, by a
visible herald, at the D3 cost" (OA1:328), with `P(E) ≤ q^{−M}` (OA1:156–160). The screen
`D ⊆ V_D` is visible. G1 gives the ready screen only "unsourced: same ready-region gap"
(MR★:642, an unconditioned counting-measure marginal). It also lists heralds as having "no executing
process on K1; listed with mass 0" (MR★:639 [NP]). Two problems follow.
- G1 does not reconcile MR★:639 [NP] with OA1:328 [M-r]. One concerns a heralding process inside
  `φ`; the other concerns conditioning on a held visible configuration.
- On the visible-herald route the first missing step moves. The herald is a component `e` of the
  compared record (G1:195), so it must be held at `t_c`, which is C-RET (unsourced; U1:300–304
  names exactly this case).
- *Consequence.* The bottom line "unsourced" survives. G1-F4's location "unsourced at C-PREP" is
  then not the first missing step for the screen; it is C-RET of the herald.
- *Required change.* Add the visible-herald row with its standing, reconcile it with MR★:639, and
  restate G1-F4's location.

**6. "No protocol reaches available" needs its `μ` scope and its conditions in the summary
(G1:273–276).**
- *(a) `μ` scope.* The unsourced verdicts for preparation, ready screen and retention rest on the
  counting measure (MR★:642, "under which every region's marginal is uniform"). `I` carries `μ` as a
  parameter (G1:89–91). Under a declared `μ` with ready cells or a register as `μ`-data, U1 admits
  *available relative to `μ`* for C-PREP, C-REC and C-RET (U1:275, :524–525, :576–577). The remaining
  blocker would then be R1 on K1, which is *undecided* (C-4, U1:532), not *unsourced*. The headline
  stays true, since nothing reaches *available*, but the stated reason is specific to μ-G.
- *(b) Conditions.* The a2/a3 and switch verdicts of *not available* are negatives under SNR-1 only
  once U1's factor-set reading is verified (U2 §11.1, "counts only once those are verified"). The
  table row says this (G1:261); the per-protocol summary drops it. The coupling-switch row also cites
  U4 §2.1 (PROVISIONAL). The summary should state whether that verdict rests on D5 alone or also on
  U4.
- *Required change.* Add the `μ` scope to the summary (μ-G; other declared `μ` giving undecided at
  C-4). Carry the factor-set condition and the PROVISIONAL tag where they apply. With these, the
  statement is correctly scoped. The scoped-reading paragraph (G1:278–283) is correctly reported as
  unsourced or not classified.

**7. The O11 conditional stop also covers a1 against a4, and the auxiliary protocols (G1:552–556,
:263–264, :174–178).** U4 §2.1 (PROVISIONAL): on K1 a region "records" whenever `Φ_{AΣ} ≠ 0`, "a
property of the declared region and the fixed graph". The marker-coupled comparison "has a K1
counterpart only as a comparison of declared regions, or through a setting's additive offset". G1
excludes the first (E-decl) and finds the E-set coupling switch not available. Its E-prep row changes
only the marker's prepared content, and the marker still records (S-L5). So E-prep does not realize
a1 "no marker" (OCP:19). It realizes a4 with a different marker preparation.
- *Consequence.* On K1, a1 as specified is available only in another geometry, the same standing as
  a2 and a3. The same holds for the Deletion control's "remove the marker" (G1:497–500) and for all
  four auxiliary protocols a2P, a3P, a2C and a3C, which block a path.
- *Required change.* Extend §9's O11 stop to a1 against a4 and to `𝒜_10 ∖ 𝒜_6` (PROVISIONAL where
  it rests on U4 §2.1). Say in owner question 1 that adopting `𝒜_10` adds protocols that, on K1,
  are comparable within `I` only through that stop.
- *Also state (minor).* Whether E-prep could represent blocking. Under C-9's wording (RU4 finding
  11), an offset correlated with the carrier under `μ` is not excluded by S-L5. List that case as
  excluded, with a ground, or as not classified.

**8. `κ_cmp` withholds counted misses on qualitative raw-direct features (G1:397–403).** A target
reported only qualitatively "cannot yield a counted miss", and (γ→) counts a miss only "on a
quantitative target". The amended target says "a raw-direct miss is a miss" (c.6891338304, §A.24).
Fringes plainly present or absent in plotted raw counts (Kim, Walborn; LIT 1.6, 1.7) are raw-direct.
- *Required change.* Either add a qualitative-feature miss (for example, fringes absent where the
  source shows them), counted at the qualitative level and reported separately, or state the ground
  for excluding it. Without that, κ shields the many unnumbered targets from falsification.
- *Advisory, same rule.* "Within the reported interval, at the confidence level the source states"
  usually means 1σ, which rejects a correct law about a third of the time. Fix the interval multiple
  in advance as part of the preregistered decision rule.

**9. κ-orb's weight, and κ-ens's hidden premise (G1:366–391; G1-F5).**
- *(a) Internal inconsistency.* G1:387–388 says the weight of κ-orb's report "is G4's question", then
  "G1 fixes only that the weight is the model's declared `μ`". Weighting the agreeing orbits by `μ`
  turns κ-orb into the ensemble probability of the event "`F_N` agrees". That moves the orbit reading
  toward κ-ens, against Q5's "neither is adopted".
- *Required change for (a).* Report the agreeing set without a measure (all, some or none of the
  orbits in the support) beside its `μ`-mass, and leave the weight to G4, as owner question 3 already
  asks.
- *(b) A premise of κ-ens.* "Each run is one evaluation of `g_a` from `μ`; no renewal is required"
  identifies sequential runs in one history with independent draws from `μ`. That identification is
  a premise of κ-ens, in effect exchangeability across runs, and it is where κ-ens's renewal
  requirement is hidden. G1-F5's "κ-orb needs C-REN and κ-ens does not" holds only because κ-ens does
  not represent the run sequence. It is favourable to κ-ens and was not pressure-tested.
- *Required change for (b).* Name the identification as a hypothesis of κ-ens (an H-4 marker) and
  restate G1-F5 accordingly.

With 9 fixed, both readings are carried and neither is adopted.

### Minor

**10. Hidden-assumption status of `κ_det` (brief item 2; G1:302–312).** The rule names no outcome
and does not presuppose agreement, so it does not beg (γ→) in that sense.
- *Ground.* It misattributes its clause. R1 (U1:514) says only "under `μ`, the law of the held value
  depends on the `P`-cell at `t₀`". "A detection is a departure from a ready value" is G1's [P], and
  its source is U1:519 ("The ready state the write needs is an input under C-PREP") and MR★ C-3. Cite
  those.
- *Effect.* It is still a choice with a verdict-level effect. A readout-partition rule with no ready
  reference also meets R1. Under μ-G, that rule lets a G2 outcome of "uniform law" become a
  comparison. Under `κ_det`, it becomes *unsourced*. Record `κ_det` as an assumption-watch marker,
  with that alternative stated and either carried or excluded on target-neutral grounds. Owner
  question 2 then has its object.
- *Partition.* On K1 the departure rule fires on any nonzero contribution, so detections are support
  events. The declared partition of `D_j`'s states therefore carries weight. List it explicitly under
  NC-γ1.
- *Tick.* `s` at `t_c` (G1:190) and "a detection at tick `t`" (G1:302) need to be tied together:
  held at `t_c`, or retained from the read tick.

**11. E-decl's ground (G1:134–137).** "Every record law is the same for every `a`" holds only with
the record map also fixed. If a declaration changes which cells are reported, the laws differ, but
they are post-processings of one configuration law, so that case is E-read. If it changes `Obs`, §2.1
and O11 apply. State the record map as fixed, or split the cases this way.

**12. PROVISIONAL tags missing.** "T0 not shown (U4 §3.2, confirmed in RU4)" in G1:258, and NC-noise
(G1:492–496, citing U4 §4.2 and PK-2's class). §8 lists NC-noise on K1 as U4-dependent, but §7.1
does not mark it. Every other U4-resting item checked is tagged (§2.3 eraser cases, marker-coupling
and E-prep rows, marker-as-record row, §5.8 phase scans, G1-F6, NC-rep, NC-copy).

**13. Screen-part versus full-law equalities.** C0's `L^{C0}_{a2} = p_L r_L` (G1:465) omits the loss
mass `p_R`, against NC-γ4. With loss included, `L_{a1} = L_{a2} + L_{a3}` holds only on the
detection part. NC-rep's `L^{rep}_{a5}(·, m = L) = L_{a2}` has the same issue. State both on the
screen part, per incident particle. `Δ` (G1:466–467) is correctly defined per incident particle and
gives OCP's `(+1/2, −1/2)`.

**14. Loss ledger without an observer.** §3.1 requires every component to be a function of an
observer's configuration at `t_c` (G1:199), but the ledgers `L` carrying `ℓ` are in no declared
observer (G1:109–111). Add one, or place `L` in `V_E`.

**15. "D itself … is not measured" (G1:170–171) overstates LIT §3.** LIT says `D = max{K}`, and that
the measured quantity is `K` for a chosen measurement, which can be below `D`. Schwindt used an
optimized basis, and Dürr's PRL abstract says "We have measured D and V independently" (ABSTRACT;
method NOT READ). Restate this as: `D` is defined as a maximum; the FULL-read sources report `K`.

**16. Citation.** OCP:45 (G1:155) concerns conditioning that changes the incident ensemble. A
partition chosen after seeing screen records is an outcome-based choice (K-2, NC-γ1). Cite that
instead, or both.

### Advisory

- **A1 (from G1-F1).** Without `𝒜_10`, `π_P` and `π_C` have no operational test (§2.3 defers it to
  §2.4). X-5's path-sorted and complementary comparisons on `𝒜_6` would then rest on declared
  labels. Add this to G1-F1's cross-propagation and to owner question 1.
- **A2.** Under E-read, every model holds one joint law of `(s, π_P(V_A), π_C(V_A))`, so a5 and a6 are
  always jointly representable reads. That is the classical-eraser class. A candidate gem for G5:
  check whether X-5 under E-read is bounded by the CC4/CC5 ceiling.
- **A3.** NC-γ1 and NC-γ5 should require a committed, hashed instance declaration that precedes
  every evaluation by commit order. Instances created after an evaluation should be counted and all
  reported, so that a search over `π_C` or `κ` variants is visible as a trial count.
- **A4.** In "every input derived or disproved" (G1:402, inherited from PLAN-G:136–138), "disproved"
  cannot occur with outcome *available*. Restate it as "every input derived".

## Brief items 1–10

1. **Definitions.** Noncircular and outcome-neutral: no amplitude, Born rule or Kraus map enters κ or
   a native law, and every partition and encoding is fixed in advance. Well-posedness fails at
   findings 2, 3 and 13, and needs the clarifications in 10, 11 and 14. NC-γ1–5 each have a
   checkpoint. NC-γ4's checkpoint is defined for E-set only (finding 3).
2. **`κ_det`.** It does not beg agreement. It is an unflagged choice whose consequence ("unsourced,
   not a miss") belongs to the choice, and its ground is misattributed (finding 10). The ready-screen
   location is wrong (finding 5).
3. **Typing.** Faithful to LIT 1.6–1.8, 1.11, 1.12, C2, C4 and C5: no unsorted singles in Kim,
   Walborn or Ma; Walborn Figs. 3 and 7 as unsorted coincidences; the time rescaling; Schwindt
   efficiency 1.11 ± 0.01; background treatment. One correction: Schwindt's `V` is background
   subtracted, which bears on the NC-rep comparison (finding 4).
4. **Sum rule and equal marginals.** Correct under E-read, as identities of the pushforward, once the
   E-read masses are defined (finding 3). The φ-effected caveat is correct.
5. **`Δ` and NC-rep.** `Δ` and C0 are correct; the screen part needs fixing (finding 13). "No E-read
   realization when `Δ ≠ 0`" is correct, in any model. The identification with the accessibility
   reading is wrong (finding 4).
6. **"No protocol reaches available."** True, and conditional. It needs its `μ` scope and the
   factor-set condition in the summary (finding 6).
7. **O11.** Correctly conditional and not resolved. Its scope is understated: a1 against a4, and
   `𝒜_10` (finding 7).
8. **NEW finding G1-F1.** Confirmed against LIT 1.12 ("from path-blocked counts with the analyzer in
   place") and LIT 1.8 ("Path probabilities measured by blocking one path"; counts conditioned on
   Det 4). No such protocol is among OCP:19–24, and no earlier RO-1 note characterizes the omission.
   NEW is justified. The defining statistic needs repair (finding 2), and the "D is not measured"
   wording (finding 15).
9. **U4 dependence.** Mostly tagged; two tags are missing (finding 12).
10. **Frequency readings.** Both are carried and neither is labelled adopted. κ-orb's `μ`-weight and
    κ-ens's hidden exchangeability lean toward the ensemble reading (finding 9). Classical waves are
    not counted as coverage. The per-phenomenon clause errs the other way: it excludes quantum
    mechanics too (finding 1).

## Checked and not checked

**Checked by hand.**
- Every G1 citation into U1 named in the brief, at the lines given, and U1 §§2–4.
- PLAN-G §§1, 3, 5 and 6.
- LIT in full.
- U4 §2.1 and §6.3, and RU4 findings 6, 8, 11 and 12.
- U2 §11.1's counting rule.
- OCP:1–100.
- MR★:455–520, :584–605 and :630–675.
- PREREG:177–187 and :228–238.
- QB3:54–62.
- Main:54, :480–482, :582, :588, :670 (isotropy as E4, in the line's last sentence) and :682.
- The three owner records.
- The algebra: total-variation distance equals `2L − 1`; the two `K_P` examples; `Δ` and the C0
  laws; the E-read pushforward identities; NC-rep's marginal conflict.

**Not checked.**
- The external papers themselves; LIT's read status is relied on.
- OA-1's own text, read only through U1's quotations, as G1 does.
- U4-CALC-r1 and r2, which G1 does not use.
- VER2.
- The SM:104–106 graph and SM §6.5 links.
- Whether classical optics reproduces X-4: finding 1's remark on X-4 is the reviewer's inference.
- The correctness of D5 and of U1's factor-set reading, which are taken at their stated standing.
