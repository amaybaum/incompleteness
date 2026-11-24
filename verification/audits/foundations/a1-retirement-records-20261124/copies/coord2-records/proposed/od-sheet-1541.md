**Record, 2026-11-24: decision sheet for the owner decisions OD1–OD12 of RECON-INF P2-C Node 2**

Posted by the coordinating session for the owner's review. Goal link: #1169 → RECON-INF (#1531) → P2-C Node 2. The sheet decides and authorizes nothing; its recommendations are the sheet's, not owner decisions. All twelve decisions are open and are to be resolved as one authorization (#1169 c.7075903147). Node 2 stays held.

***

# RECON-INF P2-C Node 2: decision sheet on OD1–OD12 (for the owner)

Prepared 2026-11-24, read-only. It decides nothing, authorizes nothing and changes no repository
file, Issue or pull request. Recommendations are this sheet's; they are not owner decisions.

## 0. Sources and citation keys

| Key | Object |
|---|---|
| `PKT:n` | `verification/audits/foundations/recon-inf-p2c-20261121/NODE-2-PACKET.md` at `29ad41811d54b43dd1eef5601484ea4aaa02648c` (blob `20a32718`), branch `research/recon-inf-p2c-n2-packet-20261122`, PR #1541 |
| `N1:n` | `…/NODE-1.md` at `29ad4181` (blob `cab51faf`, identical to its blob at `08626aa2`) |
| `DES:n` | `…/DESIGN.md` at `29ad4181` (blob `654b758f`, identical to its blob at `d1f39ce8` and `08626aa2`) |
| `Sub:n`, `SM:n`, `Main:n` | `papers/Substratum.md`, `papers/SM.md`, `papers/Main.md`. `git diff df6da1c6 53c6601a -- papers` and `git diff df6da1c6 8e9b8334 -- papers` are both empty (checked 2026-11-24; `8e9b8334` was `origin/main` at the time of the check), so these lines read the same at the packet's pin `df6da1c6`, at H `53c6601a` and at that `main` |
| `LEDGER` | `verification/audits/foundations/a1exit-deletion-20261121/edits.json` at `4c79be642ca631573f06b444903be75ec4f5e2b6` (`drafting_base` = `53c6601a`; 401 entries) |
| `AG:n` | `AGENTS.md` at `origin/main` `8e9b8334` |
| `c.N` | a GitHub comment id. #1169 comments are on Issue #1169; c.7075391312, c.7075409014, c.7075458483, c.7075476406, c.7075490748 and c.7075498029 are on PR #1541 |
| `STATUS` | the coordinating session’s research sweep (snapshot 2026-11-23 ~12:28Z; not on `main`) |

Review chain of the packet (all on #1541): review of `14465231`, REVISE (c.7075391312) and its
addendum (c.7075409014); writer's disposition, head `2e264b33` (c.7075458483); delta review,
CONFIRMED WITH NITS at `2e264b33` (c.7075476406); writer's disposition, head `29ad4181`
(c.7075490748); confirmation check, **CONFIRMED at `29ad4181`** (c.7075498029).

***

## 1. The twelve owner decisions

### Recorded status of all twelve (applies to every row below)

- **Open. None of OD1–OD12 is decided.** The packet settles none (PKT:421–426); the confirmation
  check states "No OD settled" (c.7075498029).
- The owner's *preliminary* recommendations on OD1, OD3, OD4, OD6 and OD9 are recorded as "not yet
  adopted" (#1169 c.7075394811), and restated as "unchanged" (c.7075564570 item 3).
- OD2, OD5, OD7, OD8, OD10, OD11 and OD12 "are to be evaluated against the reviewed packet (#1541 at
  `29ad4181`), not inferred from their numbers" (c.7075564570 item 3).
- "OD1–OD12 are to be resolved as a separate, coherent authorization, not mixed into the A1
  retirement corrections" (c.7075903147 item 3).
- Node 2 execution and the reference-set freeze are unauthorized and held: c.7075000289,
  c.7075394811, c.7075564570 item 3, c.7075665868 ("pending evaluation of the full OD1–OD12 packet at
  `29ad4181`"), c.7075869738, c.7077598984 (table row "P2-C Node 2 | Held | Requires the OD1–OD12
  decisions"). No later #1169 comment (through c.7099655517, 2026-11-23T11:26:50Z, the last of 603)
  mentions P2-C Node 2, #1541 or an OD.

### OD1. "No Stage 2 content" (PKT:428–437; criterion text PKT:157)

- **Question as stated.** The membership clause "carrying no Stage 2 content" (design, quoted at
  PKT:61–62) needs an operational reading.
- **Options.** (a) Default: the rule fails at least one of linearity A5 (Sub:100), cubic isotropy E4
  (SM:224, proof SM:228) or the nearest-neighbour premise; the failed premises are recorded per rule
  and genericity is reported per failed premise (PKT:157, PKT:166–170). (b) Alternative: the rule fails
  all three, all four outside the second-order form (PKT:157, PKT:433).
- **Dependencies.** OD2: within the second-order form with unit minus-past coefficient, (a) reduces to
  "outside the `Φ_{q,α}` family" by SM:224, so the exclusion of near-copies of `Φ` rests on OD2's
  `𝒯`, not on OD1 (PKT:157, PKT:430–432; c.7075391312 F3). OD8: outside the second-order form, posit
  (xiii) (Main:736) counts as a fourth failed premise and listing waits for D3 (PKT:157, PKT:432–433).
  OD3: under (b) T-lin, which fails E4 only, is not admissible (PKT:225–226), and a T-nl must also be
  anisotropic and non-nearest-neighbour.
- **Commitments.** (a): T-lin is admissible; a Nodes 4–5 positive reproduced by T-lin is recorded as
  generic over isotropy only; "generic over all three" needs one rule failing all three or one rule
  per premise (PKT:166–170). More comparison rules make a "specific" credit harder to earn
  (c.7075391312, views on OD1). (b): a smaller reference set of non-linear, anisotropic,
  non-nearest-neighbour rules; "specific" becomes easier to earn and T-lin is excluded (c.7075391312).
- **Recommendation: (a), decided together with OD2.** Reason: it is the conservative direction for a
  specificity test, keeps the linear control, and reports genericity at the resolution of the premise
  actually failed. Owner preliminary: (a) with exact failed premises recorded (c.7075394811). Reviewer:
  concurs, with the SM:224 reduction, `𝒯` and the non-second-order case stated (PKT:436–437;
  c.7075409014 §2), all three of which are now in the packet (c.7075476406, F3/C3).

### OD2. The transformation set `𝒯` (PKT:438–444; criterion row PKT:156)

- **Question as stated.** Which transformations of `Φ_{q,α}` define "outside the `Φ_{q,α}` family".
- **Options.** (a) Default: `𝒯` = (i) static site-wise gauge (Sub:98), (ii) addition of a particular
  solution, which includes the affine shift `x(t+1) = αSx(t) − x(t−1) + b`, `b ≠ 0`, (iii) site-uniform
  time-dependent relabelling, and composites; images of `Φ_{q,α}` under `𝒯` are excluded with a
  `𝒯`-invariant witness (PKT:156, PKT:439–442). (b) A smaller set, e.g. (i) only. Any transformation
  left out is "recorded as admitted" (PKT:361).
- **Dependencies.** Prerequisite of OD1 (see OD1). Bears on the A4 reading of PKT:153: Sub:98 states
  translation commutation "up to gauge", while PKT:153 reads the first sense of A4 as exact
  commutation and lists a gauge-only rule "only with OD2 decided". The Curtis–Hedlund–Lyndon
  citation for D5 covers exact translation-commuting rules only (PKT:342–344).
- **Commitments.** (a): near-copies of `Φ` (gauge conjugates, the affine shift, time-dependent
  relabellings) cannot enter the reference set; the read-set witness (a read set other than the six
  nearest neighbours, nonempty) is the paper certificate (PKT:156); the affine shift, which by SM:240
  no time-independent relabelling linearizes, is excluded by (ii) (PKT:156). (b): the affine shift
  (fails A5 only) would be admissible under OD1(a) and would record positives as generic over A5 "for a
  reason unrelated to linearity" (c.7075409014 §2, OD1).
- **Recommendation: (a).** Reason: without (ii) the OD1(a) reading admits the affine shift, which
  shares `Φ`'s solutions up to a uniform particular solution (c.7075391312 F3). The delta review found
  `𝒯` "small, fixed in advance" and excluding no legitimate comparator (c.7075476406). Additionally
  recommended for the decision text: state that no rule commuting with translations only up to a
  non-trivial gauge is listed in the first freeze, so that PKT:153's gate and the D5 citation's scope
  (PKT:342–344) agree. Owner: no preliminary recommendation (PKT:443). Reviewer: agrees (PKT:444).

### OD3. A non-linear tape (PKT:445–451; text PKT:187–245)

- **Question as stated.** "Whether the always-listed tape must be non-linear, as the design's example
  is, or may be T-lin" (PKT:238–239).
- **Options.** (a) Default: T-nl over the grid alphabets alongside T-lin as linear control; T-tw
  recorded as exploratory at `q ≥ 4` (PKT:446–447). (b) T-lin alone as the always-listed tape.
- **Dependencies.** OD1 (T-lin admissible under OD1(a) only, PKT:225–226). OD4 and OD12: on
  `q ∈ {2, 3}` every permutation of `ℤ_q` is affine, so the twisted family is affine there and T-nl
  needs another mechanism (PKT:214–216, PKT:228–230). The property (R) (PKT:193–218) is scoped to one
  update form and bounds no tape (PKT:210–211; c.7075409014 §1).
- **Commitments.** (a): if no T-nl over `q ∈ {2, 3}` meeting §4.1 is constructed, Node 2 records that
  and stops under S-N2a; no freeze is made and Node 4 cannot open (PKT:243–245, PKT:375–379). (b): a
  freeze with only a linear J1 member, which "does not test the distinction between the linear Stage 2
  rule and a non-linear one" (PKT:240–241).
- **Recommendation: (a).** Reason: the design's own example is non-linear (DES:306 ff., quoted at
  PKT:51–54), and a linear comparator alone cannot show that a positive is specific to linearity. The
  stop under S-N2a is the honest outcome if no T-nl exists on the grid. Owner preliminary: (a)
  (c.7075394811). Reviewer: concurs (PKT:450–451).

### OD4. The grid `𝒢` and the (R-nl) list form (PKT:452–461; text PKT:270–302)

- **Question as stated.** The finite grid of `(q, W)` on which every readout-map list is frozen, and
  the form of the (R-nl) lists.
- **Options.** (a) Default: `q ∈ {2, 3}`; `W` one site or two adjacent sites; each reference rule's
  lists on every image of `W` under the 48-element cubic group (PKT:279–288); (R-nl) all partitions of
  `G_W` for `q^{2w} ≤ 9`, a named finite subfamily above (PKT:296). (b) A wider grid (see OD12(b)).
- **Dependencies.** OD3/OD12 (alphabet). OD10 (correspondence uses the same window images). The
  (F)-setting torus reading cites SM:222, which states the finite periodic quotient "under A1 and A4"
  and is a ledgered site (LEDGER D036); see §4.
- **Commitments.** A Node 4–5 run outside `𝒢` has no frozen counterpart and cannot be credited as
  specific (PKT:273–275, PKT:454–456). At `w = 2`, `q^{2w}` is 16 or 81, above 9, so the (R-nl) list
  there is the named subfamily, whose content the packet leaves to the amendment (PKT:296); a positive
  using an (R-nl) map outside it cannot be credited as specific. `α`, `m_max`, torus side and targets
  stay with the Node 4–5 amendments (PKT:276–277).
- **Recommendation: (a), with one added requirement.** The decision should require that the
  amendment state the (R-nl) subfamily for two-site windows by a selection criterion fixed in the
  amendment and reviewed at its exact head before acceptance (it is then frozen with the rest under
  OD6). Reason: the grid is bounded and the window-orientation clause removes the bias toward
  "specific" found in review (c.7075391312 F2); leaving the subfamily unnamed until the amendment is
  admissible only if its choice is visibly outcome-blind. Owner preliminary: provisionally (a), "claims
  outside this range stay exploratory unless separately preregistered" (c.7075394811). Reviewer:
  concurs provisionally (PKT:459–461).

### OD5. (Π-β) events (PKT:462–466; text PKT:319–327)

- **Question as stated.** The time set of the cylinder events defining the (Π-β) preparation class in
  the frozen lists.
- **Options.** (a) Default: a finite list of event specifications with `T_E ⊂ {0}`, identical for
  every rule (PKT:321–323). (b) A wider time set, which needs D1 (N1:461–465) decided first (PKT:323–324).
- **Dependencies.** D1 (first needed by Node 3, N1:465). The law `β` is the counting law on (F) and
  Bernoulli on (Z) (N1:75–76), cited from Main:54, a ledgered site (LEDGER D260); see §4.
- **Commitments.** (a): permanent; a (Π-β) positive of Nodes 4–5 whose event uses a time other than 0
  never has a frozen counterpart, even after D1 is decided (PKT:324–327, PKT:463–464). (b): D1 must be
  decided before Node 2's freeze, i.e. earlier than the design needs it.
- **Recommendation: (a).** Reason: the event is then a cylinder of the initial configuration and the
  same set of laws for every rule, so the comparison is rule-independent; the cost (no specificity
  credit for in-run apparatus records) is conservative and is stated. Owner: no preliminary
  recommendation (PKT:465). Reviewer: agrees (PKT:466).

### OD6. Freeze timing (PKT:467–475; procedure PKT:99–137)

- **Question as stated.** Whether the freeze precedes Node 2's class-level verdicts or only every
  per-target outcome.
- **Options.** (a) Default: literature → rule construction and membership → freeze (exact-head review,
  owner acceptance) → class-level verdicts; a universal construction found after the freeze is
  recorded and routed (S-N2f) (PKT:99–133, PKT:468–471, PKT:389–391). (b) Freeze after the class-level
  verdicts and before every per-target outcome, admitting a construction proved universal before the
  freeze (PKT:471–472).
- **Dependencies.** None on other ODs; it fixes the order in which OD1–OD5, OD8 and OD10 take effect.
  Interacts with the design's "Node 2's universal construction is included wherever Node 2 finds one"
  (PKT:64), resolved by writing candidates before the freeze (PKT:249–254; c.7075409014 §2, OD6).
- **Commitments.** (a): no vacuity verdict can influence list selection; a universal construction
  first found after the freeze is excluded from the frozen set (S-N2f). (b): the reference set can
  include a proved-universal rule, at the price of selecting lists after class-level verdicts are known.
- **Recommendation: (a).** Reason: it is the stricter reading of "before any outcome is evaluated"
  (DES:681, I5) and the cost is bounded by S-N2f's routing. Owner preliminary: (a) (c.7075394811).
  Reviewer: concurs (PKT:475).

### OD7. D5, finite range of `F^{-1}` (PKT:476–480; text PKT:329–349)

- **Question as stated.** D5 (N1:478–480): whether `F^{-1}` must have finite range in J1⁰.
- **Options.** (a) Default: working reading "`F^{-1}` of finite range (on (F) uniform in the torus
  size)", each verdict stated for both readings, routed to the owner under S2 only if a verdict
  differs (PKT:347–349). (b) Fix either reading now.
- **Dependencies.** OD2 (the `d`-dimensional Curtis–Hedlund–Lyndon citation covers exact
  translation-commuting rules only, PKT:339–344). No other OD.
- **Commitments.** (a): no effect on the freeze; every proposed rule has a finite-range inverse by
  explicit formula (PKT:333–336). A negative or obstruction is stated under the reading it was proved
  for (PKT:337–338).
- **Recommendation: (a).** Reason: D5 does not bite on any listed rule, and the routing clause keeps
  the choice from being made after an outcome. Owner: no preliminary recommendation (PKT:479).
  Reviewer: agrees (PKT:480).

### OD8. D3 for a construction outside the second-order form (PKT:481–483)

- **Question as stated.** Whether a universal construction outside the second-order form can be
  listed as J1 before the no-self-input reading (D3, N1:469–470; N1:342–349) is fixed for its form.
- **Options.** (a) Default: not listed as J1 until the owner fixes D3 for its form (PKT:482). (b)
  Fix a general D3 reading now.
- **Dependencies.** OD1 (fourth premise outside the second-order form), OD6 (a candidate needing D3
  must have it decided before the freeze, otherwise it cannot be in the frozen set), OD10 (such
  constructions often use another site alphabet, PKT:255–258). A4's no-self-input clause is Sub:98.
- **Commitments.** (a): a block- or partitioned-form universal construction (PKT:254–257) found in
  step 2 stops at S-N2b and is routed to the owner before the freeze; if not decided by then it is
  outside the frozen set. (b): a reading fixed before any candidate is seen; outcome-blind, but made
  without the construction it is meant to govern.
- **Recommendation: (a), with the routing made explicit:** a candidate needing D3 that is found before
  the freeze is routed under S-N2b and the freeze waits for the owner's D3 decision. Reason: keeps D3
  a stated choice for a known form, decided before any verdict. Owner: no preliminary recommendation.
  Reviewer: agrees (PKT:483).

### OD9. Computation (PKT:484–488; text PKT:393–403)

- **Question as stated.** Whether Node 2 runs any computation.
- **Options.** (a) Default: none; any need recorded as "Missing (needs computation)" (S-N2c,
  PKT:382–383). (b) A bounded computation authorized now.
- **Dependencies.** None. Any later computation must evaluate no target law (PKT:400–401).
- **Commitments.** (a): Node 2 is reading, literature (L1, L6, L7) and paper derivation; a needed
  computation becomes a separate packet with a §A.40 cost class (PKT:399–403). (b): an exhaustive check
  on a side-3 torus in `d = 3` is not bounded (`|Ω| = q^{54}`, PKT:401–403).
- **Recommendation: (a).** Reason: every membership property follows from the rule's form
  (PKT:395–397). Owner preliminary: (a) (c.7075394811). Reviewer: concurs (PKT:488).

### OD10. Site alphabet and correspondence (PKT:489–493; text PKT:160–164, PKT:304–311)

- **Question as stated.** The domain correspondence of readout maps and preparations between
  `Φ_{q,α}` and each reference rule.
- **Options.** (a) Default: tape-kind members over `ℤ_q` with the identity correspondence on each
  cubic image of `W`; a rule on another alphabet takes every map of the same class and value count on
  every cubic image (PKT:490–492, PKT:306–309). (b) A single named map per `Φ` map (PKT:310–311).
- **Dependencies.** OD4 (window images), OD8 (alphabet of a universal construction).
- **Commitments.** (a): the reference rule gets at least the freedom "free within the lists" requires;
  a "generic" record is no harder and a "specific" credit no easier (PKT:308–310). (b): a choice of map
  per `Φ` map, which narrows the reference rule's freedom.
- **Recommendation: (a).** Reason: it is fixed before any outcome and does not bias toward "specific".
  Owner: no preliminary recommendation. Reviewer: agrees, with the window clause (PKT:493).

### OD11. Branch base (PKT:494–498; record location PKT:517–521)

- **Question as stated.** The base of Node 2's branch.
- **Options.** (a) Default: the accepted head of the packet branch (`29ad4181`), which descends from
  `08626aa2` and contains `DESIGN.md`, `NODE-1.md` and the packet, none on `main` (PKT:495–497). (b) Any
  other base, which would lack those files.
- **Dependencies.** None on other ODs. It requires the owner to accept the packet head first (the
  packet is confirmed by review, c.7075498029; no owner acceptance of `29ad4181` is recorded in the
  #1169 comments read).
- **Commitments.** (a): Node 2's record carries the design, Node 1 and the packet in its history;
  landing any of them on `main` later needs its own decision and §A.42 item 8 tracing.
- **Recommendation: (a), naming `29ad41811d54b43dd1eef5601484ea4aaa02648c` exactly.** The branch named
  at PKT:517, `research/recon-inf-p2c-n2-20261122`, does not exist on the remote (checked
  2026-11-24); its date suffix may be changed by the decision. Owner: no preliminary recommendation.
  Reviewer: agrees (PKT:498).

### OD12. The OD3–OD4 interaction (PKT:499–509)

- **Question as stated.** If Node 2 cannot construct a non-linear tape over `q ∈ {2, 3}` meeting
  §4.1, which alternative applies (PKT:500–503).
- **Options** (PKT:503–506). (a) Keep the grid; record the non-linear requirement as unmet; no freeze
  (S-N2a); "a freeze with T-lin as the only J1 member does not satisfy OD3". (b) Widen the grid before
  the freeze to a `q ≥ 4` (e.g. `q = 4` for T-tw), with every list frozen there. (c) Keep the grid and
  preregister T-tw separately as exploratory.
- **Dependencies.** OD3 (only arises under OD3(a)), OD4 (grid), OD1 (T-tw's admissibility and its
  `𝒯`-relation to a linear rule are for Node 2 to check, PKT:233–236).
- **Commitments.** (a): a possible halt of P2-C before Node 4, routed to the owner. (b): every list at
  `q = 4` as well; at `w = 1`, `|G_W| = 16 > 9`, so the (R-nl) list there is a named subfamily
  (PKT:296); must be decided before any verdict (c.7075476406). (c): T-tw carries no specificity credit.
- **Recommendation: (a) as the default, together with (c) for T-tw.** Choose (b) only if the owner
  wants the non-linear comparison executed on the frozen range, and then decide it before the freeze.
  This is the reviewer's recommendation (c.7075476406, "View on OD12"); the owner has not addressed it
  (PKT:508).

***

## 2. Dependency order for deciding

1. **OD2** (`𝒯`), then **OD1** in the same decision: OD1(a) is fair only with `𝒯` fixed
   (PKT:430–432; c.7075391312 F3).
2. **OD8** (D3 gating): it completes OD1 outside the second-order form.
3. **OD6** (freeze timing): fixes when 1–2 and the lists take effect; independent of the others.
4. **OD4** (grid, window images, (R-nl) form), then **OD3** (non-linear tape), then **OD12** (what
   happens if 3 and 4 cannot both be met).
5. **OD10** (correspondence): needs OD4's window images and OD8's alphabet outcome.
6. **OD5** (`T_E ⊂ {0}`): independent of the others; must precede the freeze.
7. **OD7** (D5) and **OD9** (no computation): independent; may be decided at any point before
   authorization.
8. **OD11** (branch base): last, after the owner accepts the packet head it names.

All twelve, together with the Node 2 authorization, writer and reviewer, form one decision record
(c.7075903147 item 3). None is a prerequisite of the A1 retirement, and the A1 retirement is not a
prerequisite of the decisions themselves; §4 states what the retirement changes for their sources.

***

## 3. Draft research brief for Node 2 (conditional on the decisions of §1)

**Not authorized.** This brief has effect only if the owner records OD1–OD12 and an execution
authorization naming writer and reviewer.

- **Question (bounded).** For the frozen reference rule set: (a) is J1⁰ (N1:323–340) realizable for
  every target of each class of design §2.3 by the range-0 rules R0 and R0-ti, and (b) is J1
  (N1:342–349) so realizable by any frozen J1 member inside A2–A4 (Sub:94–98)? Verdicts are
  class-level paper results; no individual target of the Nodes 4–5 families is evaluated (PKT:135–137).
  Design Node 2 is quoted at PKT:46–88 (verbatim from DES:306 ff., c.7075498029).
- **Inputs.** Design `DESIGN.md` at `d1f39ce886c69c0d5bf3dd566f30c55285d0a4c6` (accepted, #1169
  c.7069340219); Node 1 `NODE-1.md` at `08626aa270da27df0f369dece9bb09560aa1c17f` (accepted
  c.7074721954, M1–M8 and D1–D5 open, PKT:30); packet `NODE-2-PACKET.md` at
  `29ad41811d54b43dd1eef5601484ea4aaa02648c` (CONFIRMED, c.7075498029); corpus `main` at
  `df6da1c6101e811acdc7952d5748aff57028e8ed` (PKT:31), papers identical at H `53c6601a` and at
  `8e9b8334`; the owner decision record on OD1–OD12.
- **Procedure.** PKT:99–133 under OD6: L1, L6, L7 literature → rule construction and membership with
  the §7 controls (PKT:356–369) → freezing amendment as one commit, exact-head review, owner acceptance
  → case (a) → case (b) → verdicts per premise set with the countercontrol (DES:688, I12).
- **Scope.** Paper-only; no computation (OD9); no change to `DESIGN.md`, `NODE-1.md` or the packet
  (PKT:409); files only `verification/audits/foundations/recon-inf-p2c-20261121/NODE-2.md` and
  `…/amendments/NODE-2-REFERENCE-SET.md` (PKT:519–521), on a new branch from `29ad4181` (OD11); one
  draft PR linked to #1531, #1535 and #1538 (PKT:521) and to the accountable Issue of §5; no file of
  the A1 retirement ledger is touched (c.7076731666, as STATUS §1 records it); no manuscript or Lean
  change, no merge (PKT:529–531).
- **Roles.** Writer: one fresh agent, not the packet's writer (PKT:513). Reviewer: independent
  exact-head review in a separate session, never the writer, of the amendment before the owner accepts
  it and of the record before acceptance (PKT:514–516; c.7075274142 conditions). The freeze counts
  only at the SHA the owner accepts (PKT:516).
- **Stop conditions.** The node ends at the first of:
  - *proof*: a class-level realization verdict for a premise set, recorded as uninformative for Q at
    that class, Q then carried by the next stronger relation (PKT:56–58, PKT:129–131);
  - *counterexample or obstruction*: none of the frozen rules realizes the class inside A2–A4; J1
    carried as Missing with the obstruction at its scope (PKT:57–58, PKT:125–127);
  - *identified missing premise*: a definitional choice not decided (S-N2b → design S2, PKT:380–381),
    a needed computation (S-N2c, PKT:382–383), no J1 member or no non-linear tape (S-N2a,
    PKT:375–379), an outcome before the freeze (S-N2d, PKT:384–386), a membership failure (S-N2e) or a
    rule found after the freeze (S-N2f) (PKT:387–391); design S3 (control failure), S4 (cost) and S6
    (provenance) apply (PKT:373; DES:641–651). S1 does not apply (PKT:95).
- **Goal link (§A.47, AG:1458–1463).** RECON-INF (#1531) → P2-C (#1535 design). Node 2 decides whether
  lattice realization without the Stage 2 constraints is vacuous, and freezes the comparison set that
  decides which positive outcomes of Nodes 4–5 can be credited as specific to the Stage 2 dynamics; it
  decides no part of Q (J2) or Q⁺ (J3) (PKT:11–14). It serves #1169's foundational question of whether
  the observational construction connects to the native lattice (owner's reason for P2-C first,
  c.7069340219).

***

## 4. Dependence on `papers/Substratum.md` at H and on the A1 retirement

**Statement.** Every conclusion of Node 2, of its freezing amendment, and of the decisions OD1–OD12
that rests on `papers/Substratum.md` as it stands at H = `53c6601a10419b6b333cc992474272501ab542af`
(identical to its text at the pin `df6da1c6`) rests on a ledgered path of the A1 retirement
(`papers/Substratum.md` has 31 LEDGER entries; `SM.md` 10, `Main.md` 25). Such a conclusion must be re-pinned after the A1
retirement lands: each cited `Sub:n` re-read at the post-retirement `main`, its line number and text
compared, and any change recorded and assessed before the conclusion is used. The same applies to
`papers/SM.md` and `papers/Main.md`, which are also ledgered. The retirement is not complete:
execution is suspended and the route is being replaced (c.7093128173), and LEDGER is the frozen plan
at `4c79be64`, whose splices may be amended under that route. The line lists below are therefore
against LEDGER at `4c79be64` and must themselves be re-checked against the ledger that lands.

**Ledgered sites cited by the P2-C records** (exact `file:line` match between a citation and a
LEDGER `site`):

| Site | LEDGER id | Cited at |
|---|---|---|
| Sub:94 (A1/A2 neighbourhood) | D374 (needs scientific review) | N1:21; DES:36 |
| Sub:123 | D019 | N1:19, N1:310; DES:56, DES:294 |
| Sub:129 | D020 | N1:19; DES:294, DES:594 |
| Sub:133 | D021 | N1:19; DES:80, DES:294 |
| Sub:137 | D245 | N1:19, N1:91; DES:88, DES:91, DES:294, DES:595 |
| SM:222 ("under A1 and A4 … finite periodic quotient") | D036 | PKT:287; N1:19, N1:41; DES:114–115, DES:294 |
| SM:232 | D037 | N1:19; DES:294 |
| Main:54 (counting-measure selection; `β`) | D260 | N1:21, N1:76; DES:120 |
| Main:646 | D009 | N1:19; DES:294 |

The packet itself cites Substratum at Sub:98 (A4: translation commutation up to gauge, no
self-input, side ≥ 3, the self-input example; PKT:52, PKT:156, PKT:360) and Sub:100 (A5; PKT:157).
Neither line is a LEDGER site, but LEDGER edits earlier lines of the same file (Sub:42–56: D013,
D014, D015, D244, D261, D367; Sub:92, the A1 statement itself: D232; Sub:94: D374), so their line
numbers and the surrounding premise list can change.

**Nodes and ODs that depend on Substratum.md at H.**

- **Node 1** (accepted record): its readout classes, J1⁰/J1 statements and D3 rest on Sub:94, :98,
  :121–173 (N1:19–21, N1:342–349).
- **Design**: pin and premise citations Sub:94, :98, :123, :129, :133, :137 (DES:33–37, table above).
- **Node 2 (as proposed)** through:
  - **OD1**: A5 (Sub:100); the no-self-input clause (Sub:98).
  - **OD2**: the site-wise gauge and the read-set witness (Sub:98, quoted at PKT:156).
  - **OD3** and **OD12**: tape admissibility inside A2–A4 (Sub:94–98) and the side-≥3 condition
    (Sub:98).
  - **OD8**: D3 is a reading of Sub:98's no-self-input clause (N1:342–349).
  - **OD4** and **OD10**: torus conditions (Sub:98) and the (F) setting via SM:222 (LEDGER D036).
  - **OD5**: not through Substratum; through `β` at Main:54 (LEDGER D260).
  - **OD6, OD7, OD9, OD11**: procedural; no Substratum citation. OD7's citation is external
    (Curtis–Hedlund–Lyndon, PKT:339–342).
- **Membership controls** (PKT:360–362): the self-input detector quotes Sub:98's rule.

A1-specific point for the owner: SM:222 places the (F) setting "under A1 and A4", and Node 1's `β` on
(F) cites Main:54; both are LEDGER sites. Whether setting (F) and the counting law keep their present
role after the retirement is a question for the re-pin, not decided here.

***

## 5. Draft planning-status block (§A.45 rule 4, AG:1265–1289; §A.47, AG:1458–1463)

**Where it would go.** #1541 is a pull request, not an Issue; under §A.45 rule 6 "A pull request is
never an accountable home" (AG:1290). The chain has no Issue for P2-C: #1535 and #1538 are pull
requests; #1531 is the only Issue, scoped to Phase 1, with no planning-status block, no labels, and
"Phases 2 and 3 are not authorized" (#1531 body). The owner chooses between a new accountable Issue
for P2-C Node 2 and a row in a block on #1531. Draft:

> **Planning status — RECON-INF P2-C Node 2** (draft for the owner; not in force until recorded)
>
> | Attribute | Entry |
> |---|---|
> | Tier | Foundational (provisional): proposed from the parent #1169's tier (label `tier: foundational`). The owner ranking "P1 \| RECON-INF P2-C" (#1169 c.7069936226) and "P2-C first" (c.7069340219) are recorded; they are not §A.45 tiers. |
> | Prerequisites | P2-C design accepted (`d1f39ce8`, c.7069340219); Node 1 accepted (`08626aa2`, c.7074721954); Node 2 packet confirmed at `29ad4181` (c.7075498029); owner decisions OD1–OD12 (open); owner acceptance of the packet head as branch base (OD11); a designated writer and an independent reviewer. |
> | Readiness | blocked: owner questions (OD1–OD12; Node 2 held, c.7075665868, c.7077598984) |
> | Authorization | not authorized |
> | Designated writer | none |
> | Status source | `verification/audits/foundations/recon-inf-p2c-20261121/NODE-2-PACKET.md` at `29ad4181` (#1541); `NODE-1.md` at `08626aa2` (#1538); `DESIGN.md` at `d1f39ce8` (#1535). None is on `main`. |
> | Goal link (§A.47) | #1169 → RECON-INF (#1531) → P2-C. Node 2 would decide whether lattice realization without the Stage 2 constraints (J1⁰, J1) is vacuous, and freeze the comparison set that decides which Nodes 4–5 positives can be credited as specific to the Stage 2 dynamics. It decides no part of Q (J2) or Q⁺ (J3). |
> | Notes | Conclusions resting on `papers/Substratum.md`, `SM.md` or `Main.md` at H `53c6601a` are re-pinned after the A1 retirement (decision sheet §4). OD1–OD12 are resolved as one authorization, separate from the A1 corrections (c.7075903147). |

Labels that would summarize it: `tier: foundational`, `tier: provisional`, `readiness: blocked`.

***

## 6. Discrepancies between the packet and the record

1. **OD count in the PR body.** #1541's description says "eleven points needing an owner decision
   (OD1–OD11)"; the packet at its head has OD1–OD12 (PKT:499–509), OD12 added at `2e264b33`
   (c.7075458483). The body predates the revision.
2. **No accountable Issue** for Node 2 (§5): #1541, #1535, #1538 are pull requests; #1531 has no
   planning-status block (also STATUS §4 item 3). The packet's goal link names #1535 (a PR) as P2-C's
   home (PKT:11).
3. **Which comment confirms the head.** c.7075476406 is CONFIRMED WITH NITS at `2e264b33`; the
   confirmation at `29ad4181` is c.7075498029.
4. **"Current main" in the packet.** PKT:34 calls `53c6601a` current `main`; `main` has since moved
   (`8e9b8334` at the check). The papers diff is still empty; the writer repeats the check at start
   (PKT:41–42).
5. **Design's statement about the retirement plan.** DES:35–37 says the retirement plan P* "leaves
   `Sub:94` onward, SM, GR and Structure unchanged". That describes the plan then current; LEDGER at
   `4c79be64` edits Sub:94, :123, :129, :133, :137 and SM:22–641 (§4). The design cites B1 only and
   assumes no edit has landed (DES:36–37), so its pins are unaffected; the re-pin of §4 is needed.
6. **STATUS §3.1** says "the design pins `papers/` at `53c6601a`"; the design pins `df6da1c6`
   (DES:33), with `papers/` identical at `53c6601a` (PKT:34–36).
7. **A4 reading (not a defect, flagged for OD2).** Sub:98 states translation commutation "up to
   gauge"; PKT:153 reads it as exact commutation and defers gauge-only rules to OD2.
8. **Concurrency limit.** c.7077598984 records "At most two scientific successor workstreams run
   concurrently"; whether that limit still applies to a Node 2 start is not stated in the comments
   read and would need the owner's statement in the authorization.

---
_Generated by [Claude Code](https://claude.ai/code)_