# #1169 synthesis (r2): prioritized missing-mechanism list from the four Bell-first paper units

**Standing.** WIP / UNVERIFIED author record. Paper-only: source reading and hand reasoning, no
computation on any OI rule, no script, no Lean build, no manuscript or record edit. It adopts no
premise, promotes no claim and changes no Issue priority or status. The order in §1 is the ranking
this deliverable asks for; it is not a planning-record change (§A.45). Every unit result used here
is a research record, model-reviewed, and not established (§A.46 item 7). The next steps are a
focused confirmation of r2 and the ChatGPT exact-head review.

**Revision.** r2 applies findings F1–F21 of the independent review of r1 (`REVIEW-r1.md`, ACCEPT
WITH CHANGES; r1 at `4940e8d6`), with one disposition per finding and an r1→r2 delta table in
`RESPONSE-r1.md`.

**Authority.** #1169 c.6860584645 (`amaybaum`, 2026-11-13T17:47:40Z), owner answer "Start now
(Recommended)". Scope, verbatim: "It produces a prioritized list of missing mechanisms. Each entry is
labelled either **shown necessary**, with a cited proof, its assumptions and the observer class it
applies to, or **proposed route**. An obstruction found for one interface stays tied to that
interface, and #1060 is used only as supporting context." Not covered: "It merges nothing, starts
no new research or computation, adopts no premise and changes no priority."

***

## 0. Inputs, pins and labels

**Unit records (off `main`).** Paths under `verification/programmes/oi-qm/reconstruction/`. Every
branch was fetched by name. Its remote head equals the pinned commit, except #1268, whose head is
`2a9f10ba`: it adds REC-1-r8 (the owner's forward fix of three r7 passages, at `4b81298f`) and its
independent review (ACCEPT); the ChatGPT review of r8 is pending. `REC-1-P0-r3.md` and `REC-1-r7.md`
are byte-unchanged at `2a9f10ba`.

| Short | Unit, PR | Head | File (blob) |
|---|---|---|---|
| TS | TUNE-1 sourcing, #1272 | `c539a60c` | `drafts/tune-1-sourcing-20261113/TUNE-1-SOURCING-r2.md` (`35c5c116`); `CONFIRM-r2.md` (`558ddc77`) |
| P0 | REC-1 P0, #1268 | `cd38655c` (unchanged at `2a9f10ba`) | `drafts/rec-1-20261113/REC-1-P0-r3.md` (`611a4d9a`); `REC-1-P0-CONFIRM-r3.md` (`8b440f2d`) |
| R7 | REC-1 r7 (context; support for MM-1c and MM-2, see §8), #1268 | `cd38655c` (unchanged at `2a9f10ba`) | `drafts/rec-1-20261113/REC-1-r7.md` (`f1ffac0e`, unchanged from `9f7d2612` to `2a9f10ba`) |
| R8 | REC-1 r8, #1268 | `2a9f10ba` | `drafts/rec-1-20261113/REC-1-r8.md` (`615b7de8`); `REC-1-REVIEW-r8.md` |
| BL | Bell ladder, #1273 | `d8e4f80e` | `drafts/bell-ladder-20261113/BELL-LADDER-r3.md` (`0298088d`); `NOTES-r3.md` (`963d7352`); `CONFIRM-r3.md` (`c968776a`) |
| OC | Option-(c) package, #1274 | `d015131d` | `intervene-substate-results-20261113/NEW-RESULTS.md` (`1859e8c5`); `DEPENDENCIES.md` (`6c127b0a`) |

R7 line numbers are r7's at `cd38655c`. r8 shifts them by +4 for r7:15–288 and differs from r7 only
in its header and the three passages r7:289–290, :299–300 and :320–321.

**ChatGPT exact-head reviews (host records, provenance; model review is not verification).**
5892912253 (#1272, ACCEPT, bounded); 5892912758 (#1268, ACCEPT of P0's O-U, r7 reconciliation
required); 5892919040 (#1273, ACCEPT as a conditional paper result, two safeguards); 5895564670
(#1274, ACCEPT as a scoped evidence package, integration gated); 5891524305 (#1268, ACCEPT of r7 at
`9f7d2612`). Their scope limits are carried in §2 and §5.

**Owner decisions carried.** #1273 c.6860580909 (Bell Q1–Q4: ledger (vii) a conditional ledger
posit; MI\* a distinct hypothesis; AL's expectation not written into the mixed-path test; the
full-history convention for AL only). #1268 c.6860582570 (literal L reading of r7's class; an r8
correction of three r7 passages; P0 stays O-U; the C3 check proposed and not authorized; AW-OA2-1
stopped). #1169 c.6854774010 (NL-C safeguard; P0 mixed case).

**Records on `main` at `c3b5f37a`** (blob prefix): OA1 = `oa-1-20261112/OA-1-REPORT-r5.md`
(`5a16b213`); OA2 = `oa-2-20261112/OA-2-REPORT-r4.md` (`8f8ddf73`); OA3 =
`oa-3-20261112/OA-3-REPORT-r4.md` (`0a36fd05`); W11 =
`verification/programmes/physical-realization/w1-1-20261112/W1-1-REPORT-r4.md` (`8bf64629`); OBS =
`observer-interface-obsmu-20261104/ANALYSIS.md` (`e657732b`); M1D =
`mechanism-1-20261107/DESIGN.md` (`7f8a142b`); M2D = `mechanism-2-20261108/DESIGN.md`
(`9352d9da`); PPS = `oi-qm-ext-1/prepared-pair-source.md` (`9123157c`); Main = `papers/Main.md`
(`0db17597`); OB = `verification/lean-mathlib/OIBridge/` (statements read, nothing built). TUNE-1
records, under `drafts/tune-1-20261111/`: P = `TUNE-1-STEP2-PROPOSAL.md` (`84f71030`); AF =
`TUNE-1-STEP2-AMENDMENT-1-final.md` (`ee8582b2`); S3 = `TUNE-1-STEP2-SESSION3.md` (`a9cbc675`); S4 =
`TUNE-1-STEP2-SESSION4.md` (`17ca08f8`). Source screens: NPS1 =
`native-preparation-source-1-20261110/PREPARATION-SCREEN.md` (`8f1edce3`); NIS2 =
`native-interaction-source-2-20261110/SOURCE-SCREEN.md` (`1daf3861`).

**Support layers.** [K] kernel statement on `main`; [P] manuscript proof on `main`; [A] paper
argument, hand-checked, not kernel-checked (on `main`: a research record, not established; off
`main`: a draft); [X] exact generic check (a script in a draft), not run here; [L] external
literature; conjecture. "[A, here]" marks a reading made in this file, unreviewed.

**Entry labels.** *Shown necessary*: a cited proof shows that, for the stated observer class or
interface and under the stated assumptions, the target fails without the ingredient. Necessity is
never sufficiency. *Proposed route*: no such proof; its status and its test are stated. These are
the only two labels. The qualifier "load-bearing role shown" on a proposed route records that paired
results show a verdict depends on the item; it is not a third label. Two other findings are recorded
as such and never labelled shown necessary: that an ingredient is *absent* under a stated law, and
that it is *one member of a disjunction* the target needs.

***

## 1. The list in priority order

**Construction targets.** The units name eight targets an ingredient can block:
- T1, embedded preparation of a selected state (OA-1 N1-S; TS (b); O-RDY);
- T2, embedded held records over a run (TS (e); OA-1 gap 1);
- T3, in-world classical setting selection (OA-1 gap 2);
- T4, TUNE-1's embedded tunable mixing at precision `ε`;
- T5, a non-simplex-embeddable (G3) prepare–measure fragment (OBL-SP; OA-2 Corollary E1);
- T6, OA-1's qubit tier: phases and dense control on a qubit;
- T7, a Bell violation with complete-history no-signalling and MI kept;
- T8, the quantum Bell set.

**Ranking metric.** "Blocks" means that the entry is a premise of a construction target. Entries are
ranked lexicographically by three counts over T1–T8: (i) targets for which the entry is shown
necessary on its own, within some stated interface; (ii) targets for which it is a shown member of
a disjunction; (iii) targets for which its load-bearing role is shown. Ties are broken by target
dependency (an entry whose target presupposes another entry's target ranks after it). A premise of
an obstruction (MM-6) blocks no construction and is listed last, by its role in the ceilings. The
counts and two alternative metrics are in §3. Entry IDs are identifiers and keep their r1 values;
§2 gives the entries in ID order.

| Rank | ID | Missing ingredient | Label | Tied to | Layer, location | Found by |
|---|---|---|---|---|---|---|
| 1 | MM-3 | An observer operation beyond the configuration-level ceiling (gap 3), with its interface-specific necessary conditions | shown necessary per sub-row; the operation itself: proposed route | per sub-row 3a–3e | [K], [P], [A] on `main`; [A] off `main` (3e) | OA-1, OA-2, OA-3; OC (E2, G1) |
| 2 | MM-1 | Ready resource: a native producer of known-value cells, renewed per run | shown necessary in TUNE-1's schema (1a) and for writing a selected value under R-lin and μ-G (1b′); producer: proposed route | TUNE-1's initial-condition schema; N1-S of hidden carriers under R-lin and μ-G | [A] off and on `main` | TS (first stop); OA-1; R7 §3.2 |
| 3 | MM-4 | Setting-selective coupling: a non-affine update (outside the affine class that amplitude-scale gauge invariance yields; a fortiori outside (vii)) | shown necessary for classical setting selection and for route B; one member of a disjunction in AL's class and in Corollary E1; not sufficient for MM-3 | every observer under inclusion (4a); affine updates on products of abelian groups (4b); AL's class (4c) | [A] on `main`; [A] off `main`; [P] | OA-1; TS (N1.5); BL (AL); OC (L4) |
| 4 | MM-7 | A restricted preparation family with complete-history no-signalling (masking) | shown necessary | parameter-dependence branch with MI kept, finite `Λ` | [A] on `main` | BL (stage 6, §5); OC (N3) |
| 5 | MM-8 | A selector of the quantum Bell set (CHSH in `(2, 2√2]` and not more) | shown necessary relative to the unrestricted class | the unrestricted OI behaviour class | [P]; [X] off `main` | BL (stage 7); OC (N4) |
| 6 | MM-2 | A sourced embedded record and effect class: retention, herald typing, label delimitation, history region | proposed route; load-bearing role shown | affine class with `D_0` or coset laws; H-AR; two-wing every-run protocols | [A] off `main`; [A] on `main` | P0; BL; OA-3; TS (e) |
| 7 | MM-5 | The run law that posit (iv) selects for an observer with records, and whether it is coset-uniform | proposed route; load-bearing role shown in AL | AL and P0 | [A] off `main` | BL; R7 (C8–C10); TS (N3.3) |
| 8 | MM-9 | A non-site-fibred hidden factor written by one wing and read by the other (route A) | proposed route (open obligation SLL) | route A only | [A] off `main` | OC (N1, N2, SLL) |
| 9 | MM-6 | A native source of setting independence (H-xiv, MI\*, H-μ) | proposed route; load-bearing role shown for E(b), OBL-SP and the Bell stage-5 ceiling; not a hypothesis of AL or Theorem S | Bell analysis; every admitted procedure | [A] off `main`; [P] | BL; R7 (C12); OC (S7); TS (c) |

Unranked items (open mathematics, not physical ingredients, and the W1 track) are in §4.

***

## 2. The entries

### MM-1. Ready resource

- **Missing ingredient.** A process inside the joint dynamics `φ`, from a stated initial or boundary
  law, that places cells at known values in an apparatus's ready configuration and its designated
  program or setting content at use time, renewed for every run. For TUNE-1's target the amount grows
  with precision. In the corpus this is the open obligation O-RDY (#1147; OBS:100, :121).
- **Label: shown necessary in two scoped forms, (1a) and (1b′); the producer is a proposed route.**
  (1b) records the absence of the ingredient under μ-G, and (1c) a disjunction of which it is one
  member; neither is a necessity label. None is an OI-wide statement.
  - **(1a) TUNE-1's initial-condition schema.** At precision `ε` a run needs at least
    `2(K+1)|C_n| ≥ (K+1) log_q((1−4ε)/(4ε))` known `q`-ary cells; with a fixed supply `D` per run,
    `ε ≥ 1/(4(1 + q^{D/(K+1)}))`; a gate needs at least `log_q((1−4ε)/(4ε))` `q`-ary cells of
    setting content. Proof: F-S2 and F-S1 (TS:321–345), arithmetic on NL-C′ (S4:464–474 on `main`)
    and on the schema's designated sites (P:143, :184–199). Assumptions: finite alphabet `q`;
    `ε < 1/8` and `K ≥ L + 1` (S4:465); blocks are translates of `C`; `r_O` fixed on all of `O`;
    NL-C′'s hypotheses hold at every interface (TS:185–224). The schema's candidate TC-A is defined
    in TS from Step 3A's candidate A (TS:100–101, off `main`, see §8). Observer class: any embedded
    observer in that schema, any rule and law. Necessity only: that a supply yields the larger
    control region is not shown (TS:340–342).
  - **(1b′) Writing a selected value under R-lin and μ-G.** For a hidden carrier, unmasking the
    previous slot needs a ready cell (MP-0a), with the neighbours known or isolated (OA1:522).
    Observer class: selectable preparation (N1-S) of hidden carriers under R-lin and μ-G.
  - **(1b) Not supplied under μ-G.** For a finite abelian `S`, an automorphism `φ` and the uniform
    law, every region is uniform at every time (Lemma P-1, OBS:529–545); point-preparing `M` `q`-ary
    cells by a herald costs `P(E) ≤ q^{−M}` (OA-1 D3, OA1:157–160). So no *unconditionally* ready
    region exists at any time under μ-G, no bijection produces one (TS:239–246), and a heralded
    substitute costs `P(E) ≤ q^{−M}`. This is the absence of the ingredient, not its necessity.
  - **(1c) One disjunct under μ-G with C5 ("held = a function of the present `V`").** A selected
    hidden carrier cannot be held together with its choice record (OA-1 gap 1, D2 applied to N1-S,
    OA1:145–155, :522). Any held one-time statistic of fixed functions is the same for every `φ`, so
    a `φ`-dependent held statistic needs a law other than μ-G (the ready-resource form, MP-0a, or any
    structured realization law) **or** a typing other than C5 (MP-0b or C7, which are MM-2)
    (R7:196–200). OA-1 gap 1 is likewise "resolved classically by MP-0a or MP-0b" (OA1:522). Here the
    ready resource is one disjunct, not a necessary condition on its own. The R7 reading is marked
    unreviewed in its own text (R7:185, :206); r7 as a whole was independently reviewed and
    ChatGPT-reviewed (5891524305). Observer class: held-at-use observers under μ-G.
- **Not shown.** That a producer is excluded under μ-O's conditional route, under μ-R, or under a
  structured `μ_H` (TS:247–255; OA1:522). For any invariant law, OA-1 D1 (OA1:141–143) gives an
  unconditional law that is the same at every time, so every time-specific preparation is
  conditional on a record event; whether such conditioning counts as a producer is an owner scope
  question (§7, SQ2).
- **Proposed routes for the producer** (none tested):
  - selecting a designated-cell boundary law (MP-0a, OA1:556–562; C11, R7:222): a new §A.29
    premise once selected, "Hard to vary? No";
  - H-PREP, an in-realization conditional read as a laboratory preparation (OBS:893–901): an open
    hypothesis, not adopted;
  - μ-O with held-record conditioning (OA1:522 "N1-S is open"): open; the owner classed conditioning
    as a construction step (D-OB7, OBS:888–892), and the native preparation screen's scope states
    "An inverse image, conditioned event, imposed blank field or statistical weight is not a
    producer" (#866 c.6765161496, quoted at TS:306–308);
  - μ-R (posit (iv) as stated): undecided, since it presupposes the records whose formation is the
    question (R7:220; TS:252–255);
  - a cosmological low-entropy boundary: it "does not specify which local fields are blank"
    (NPS1:88, quoted at TS:271–272).
- **Interface.** As in (1a), (1b′), (1b) and (1c), separately.
- **Support.** (1a) [A] off `main` on [A] on `main`; (1b′) and (1b) [A] on `main`; (1c) [A] on
  `main` (OA-1) and [A] off `main` (R7 §3.2).
- **Found by.** TS (first stop, TS:282–287; F-S3 records the same stop in NPS1 and NIS2 for the
  selected binary ring); OA-1 gap 1; R7 §3.2 (AW-REC-1). BL's AL2 and P0's `D_0` quantify over the
  MP-0a family without sourcing it.
- **§A.31 check.** The favourable readings "Main:58 admits MP-0a, so the supply is sourced" and
  "conditioning on the observer's configuration prepares the apparatus" are both rejected in TS
  (TS:301–309), and the rejection is kept here.
- **Smallest next check.** Paper-only: decide whether O-RDY, under every invariant law, reduces to
  the selection question on `μ_H` (C11), using OA-1 D1 and the answer to §7 SQ2. Not authorized.

### MM-2. Embedded record and effect class

- **Missing ingredient.** A derivation, from the Definition (Main:42) and inclusion (C4, R7:215),
  of four interface items that the stated premises do not fix:
  1. what an embedded observer holds over time: present `V` (C5), retained visible history (C6,
     MP-0b, (H4)), or complete records in the window it "can hold or obtain" (BL (Rec), AL4);
  2. herald typing: held at use time or ensemble conditioning (C7; AW-OA3-2, OA3:660–668);
  3. which held cells are preparation labels and which are effects under C-PM, i.e. whether the
     measurement-stage reads are jointly held in label-free cells ((LF), P0:259–261);
  4. on which history no-signalling is imposed: the complete fixed region or a setting-selected
     read (BL:249–253; owner Q4).
- **Label: proposed route (a derivation of the four interface items from the Definition and
  inclusion); load-bearing role shown by paired results.** Within the affine class the classical
  verdict changes with these items:
  - **P0.** Under (LF) the coset-space model is a simplex embedding of the C-PM prepare–measure
    fragment (N5–N6, P0:250–293). Without (LF), an additive bijection meeting every OBL-SP hypothesis
    except R-lin with (xiii) gives a preparation-contextual gbit (N8.2(b), P0:318–352). Observer
    class: H-AR, (H3), the r7 record class, held-at-use typing with records inside `S`, C-PM, H-xiv,
    `D_0`.
  - **BL.** In the affine class with a coset law (AL has no MI hypothesis, BL:205): no-signalling on
    the complete fixed-region histories forces a Bell-local law (Proposition AL, BL:187–229). Inside
    (vii), with a coset law under which MI\* holds, no-signalling imposed only on a setting-selected
    read admits the PR box (BL:249–253). Observer class: two-wing every-run protocols with
    cell-valued settings, every pair admissible, no postselection.
  - **OA-3 N4 (on `main`).** Under (V-ii-U) a 3-cell shift gives a gbit; with (V-ii-H) Theorem
    E(b) holds without (H4) (OA3:392–497).

  What is shown is the dependence, not which convention is physical.
- **§A.31 check.** Three of the non-classical patterns found in or next to the affine class sit at
  record-convention boundaries: P0 N8.2(b), BL's selected read and OA-3's (V-ii-U) shift, the last
  of which OA-3 N4 classes as a convention artefact. Others sit at other boundaries: non-spanning
  reachable laws (N2.1, OA2:296–315, :604), non-coset laws (NOTES-r3:67–69) and non-H-AR
  coarse-grainings (OA2:612–613). The classical verdicts also rest on conventions not fixed by the
  Definition ((LF), (AL4), (H4)). Neither side's convention is derived, so neither verdict is a
  result about the Definition alone. P0's N8.2(b) gbit is outside R-lin with (xiii) (P0:350–352;
  ChatGPT review 5892912758: "not a contextual witness inside the target rule class"), and a gbit at
  bounded horizon does not separate classical from quantum (OA-2 N2.3, R7 row 20).
- **Interface.** This entry is the interface. Its parts are fixed separately where the owner has
  decided: the literal L reading for r7's class (c.6860582570; stated in r8 at R8:297–303); the
  full-history convention for AL only, with the setting-selected case separate (c.6860580909).
- **Support.** [A] off `main` (P0, BL); [A] on `main` (OA-3 N4).
- **Found by.** P0 (C3, (LF), AW-P0-1, AW-P0-2); BL (AL4, Histories; NOTES-r3:55–58, :102–103);
  OA-3 (AW-OA3-2); TS part (e) (TS:143); R7 C5–C7 (R7:216–218).
- **Smallest next check.** The paper-only C3 check for R-lin with (xiii): exhibit retention carried
  only through label cells with lost common effects, or prove it cannot occur, keeping H-xiv, `D_0`,
  H-AR, C-PM and the herald and timing conventions (P0:477–478; ChatGPT review 5892912758). Proposed,
  not authorized (#1268 c.6860582570).

### MM-3. An observer operation beyond the configuration-level ceiling (gap 3)

- **Missing ingredient.** A sourced observer operation that is not a configuration permutation or a
  nonnegative stochastic map, obtained without importing quantum structure (OA-1 gap 3, OA1:524).
  The corpus has no construction; it has necessary conditions, each tied to its interface.
- **Label: shown necessary per sub-row; the operation itself is a proposed route.**

| Sub | Necessary condition | Interface and assumptions | Proof | Layer |
|---|---|---|---|---|
| 3a | Change what an observer operation acts on | Configuration identification `obsTheory 𝒮 = permTheory 𝒮.Conf` (`Substratum` with finite abelian sites and alphabet), every rule: no phases, not `DerivedOI`. Every NonnegBounded theory on `Fin 2` has no dense control. Rule-derived configuration interfaces stay inside (D6) | `obsTheory_rule_independent` OB/SubstratumInterfaceAudit.lean:780; `obsTheory_nonnegBounded` OB/FrozenSourcing.lean:84; `nonnegBounded_not_derivedOI` :111; `phase_ceiling_rule_independent` :302; `nonnegBounded_verdict` :327; D6 at OA1:196–200; OA1:418–421 | [K] on `main` (identifiers); D6 [A] on `main` on [K] |
| 3b | Carriers that grow with the demanded exactness or precision | (i) Exact infinite-order reversible trace-preserving emergent control: at fixed finite `S` these operations form a finite group, every rule, μ and interface (OA-2 Theorem C). (ii) Exact full qubit prepare–measure theory: no fixed finite realization, under the preparation → finite ontic system → measurement factorization (Main:558). (iii) TUNE-1's target at precision `ε < 1/8`, `K ≥ L + 1`: control region `|C| ≥ ½ log_q((1−4ε)/(4ε))` (NL-C′) | OA2:332–376; Main:558; S4:464–474 | [A] on `main`; [P] with [L]; [A] on `main` |
| 3c | Preparation or effect equivalences coarser than ontic equality, used non-trivially | For `R` injective on `W`, the configuration model is preparation-noncontextual (B(i)), and measurement-noncontextual when the restriction map is injective (B(ii)(⇐)). Target: G3 on the prepare–measure fragment. The converse (⇒) needs (CVX) and is not used here | OA2:242–300; N2.6 row N-b, OA2:682 | [A] on `main` |
| 3d | Settings that do more than translate the joint held record | Any rule, under (H4), (SP) and (xiv), G3 on the prepare–measure fragment (Corollary E1); exits named at OA2:599–604 | OA2:577–605 | [A] on `main` |
| 3e | On route E_f, a pair of incompatible sharp native measurements with their update rule, which requires leaving E2's class | One linear encoding `L` defined on every density matrix and shared by all procedures, P-CONF∞, H4, H-IND: any two native procedures are jointly measurable and projective ones commute (E2). Outside: context-dependent encodings `L_c`, non-linear or history-dependent realizations (E_r, C-dyn), encodings positive only on a restricted preparation set, or failure of H-IND. The E_f classical class is defined in APPROX r4a, off `main` (OC `DEPENDENCIES.md` row A2) | OC:333–392 (scope OC:376–384) | [A] off `main` |

- **Proposed routes** (none constructed):
  - record-level operations on record-equivalence classes on growing carriers, with M-INACC (OA-1
    MP-2, OA1:585–586): "possible ingredients only, and sufficiency is open";
  - M-INACC (M2D:114–117, :832): a new §A.29 premise; its protection fails on `G_σ`
    (`minacc-1-20261108/RESULT.md`:36–53), and `G_SM` does not supply it;
  - admissible non-affine rules: open (OA-2 N2.6, OA2:674–694); for `G_SM` both the gbit and the dual
    shape are excluded within Theorem S's finite-ring class (OA3:294–391), and the complement is
    open (OA3:568–577).
- **§A.31 check.** A designed reversible classical computer passes G0–G3 at bounded horizon (`𝔊_K`,
    OA-2 N2.3), so a G3 success alone is not a quantum signature; every route must also pass the
    non-import test (OA-1 key test, OA1:534–552). Sub-rows 3b–3d are each met by classical systems
    ("G2 tests carrier growth, not quantumness", OA2:372–374; `𝔊_K` for 3c and 3d). G1
    (OC:263–331) shows that on non-spanning frames a nonnegative frame matrix does not separate
    classical from non-classical transformations, so an E_f verdict must state whether its frame
    spans (the E_f classical class is defined off `main`, OC `DEPENDENCIES.md` row A2).
- **Interface.** Per sub-row; no sub-row is generalized beyond its stated class.
- **Found by.** OA-1, OA-2, OA-3 (on `main`); OC (E2, G1); TS (3b(iii), through NL-C′); R7 rows 9,
  18–23.
- **Smallest next check.** OA-3's open regime (an H-AR observer without three consecutive held sites,
  short horizons; OA3:568–581) is where the preregistered `G_SM` computation is decisive; it needs
  owner authorization together with OA-3's proposed design amendments. No paper-only check of
  comparable size is identified.

### MM-4. Setting-selective coupling: a non-affine update

- **Missing ingredient.** A coupling whose non-translational part depends on a stored setting
  (OA-1 MP-1, OA1:565–584; MECH-1 M1, M1D:125–128, :940–; TUNE-1 H-nl; R7 C2), that is, a
  non-affine update: outside the affine class that amplitude-scale gauge invariance yields, and a
  fortiori outside ledger (vii). Leaving (vii) alone does not suffice (OA1:523), and leaving the
  affine form modifies the gauge-invariance step (OA1:583–584; Main:724).
- **Label: shown necessary, for two separate targets; one member of a disjunction for two others.**
  - **(4a) Classical setting-selective control.** Under one affine `φ` acting on every cell, a stored
    setting acts on a carrier only by translation, for every measure (OA-1 D5, D7, OA1:176–195,
    :523; re-derived in S3 and M1D). Dropping A5 linearity alone, keeping the affine form, does not
    restore control. Observer class: every embedded observer, given inclusion (settings are cell
    content, no write outside `φ`). TS N1.5 applies it to setting-dependent durations (TS:214–219).
  - **(4b) Preparation-indexed long edges (Bell route B).** For an affine update on a product of
    abelian groups, the dependency relation is the same on every non-empty state class (L4,
    OC:427–465; "L4 needs only the affine form", OC:441–444; for finite `S_i`, Main:362 [P]). So
    route B needs a non-additive update (OC:450–453; Main:414).
  - **(4c) A Bell violation with complete-history no-signalling in AL's class.** Proposition AL
    (BL:187–263; AL1: every affine update, BL:190) leaves four exits: a non-affine update (named "an
    update outside (vii)" at BL:78–83, see T6), a run law that is not coset-uniform, settings that
    are not cell values, or postselection. Here the non-affine update is one disjunct, not a
    necessary condition on its own.
  - **(4d) A G3 escape within Corollary E1's scope.** With (H4), (SP), (xiv), H-AR, (H1) and (H3), a
    G3 escape needs leaving (H1) ∧ (H3): MP-1 (a non-affine rule) or supplied P3/E-iso (OA2:587–592).
    The other exits are non-additive observers, non-nested reads and non-spanning laws
    (OA2:600–604). The non-affine update is one disjunct.
- **Not sufficient for MM-3.** Non-affine rules at the configuration level stay inside the kernel
  ceiling (OA-1 D6, row 5b; OA1:524, :539–544). The repair is classical only, and "does not by itself
  bear on gap 3" (OA1:524, :573–574). OA-2 states that E1 does not make the gap-2 repair necessary
  for gap 3 outright (OA2:596–599).
- **Proposed route status.** MP-1 is "Hard to vary? No in bare form" (OA1:570). Every candidate
  (`G_SM`, `G_σ`, R-nl, MP-1, M1) is a Layer-0 revision under §A.29 and would have to state the
  preserved results in advance, give an independent prediction, and not be adjustable to fit any
  outcome (OC:502–504; BL:280–284). Owner Q1 (#1273 c.6860580909): (vii) is a conditional ledger
  posit. That label applies to (vii), not to the gauge-derived affine form.
- **Support.** (4a) [A] on `main`; (4b) [A] off `main` with [P] for finite `S_i`; (4c) [A] off
  `main`; (4d) [A] on `main`.
- **Found by.** OA-1 (gap 2); MECH-1 (M1); TS (N0.2, N1.5); BL (AL); OC (L4); OA-2 (E1).
- **Smallest next check.** Paper-only, before any evaluation: a §A.29 statement for one candidate
  (`G_SM`) of the results it must preserve (dispersion, area law, Main:362's reference graph) and one
  independent prediction. Not authorized.

### MM-5. The run law posit (iv) selects for an observer with records

- **Missing ingredient.** A derivation of the law that posit (iv) selects for an observer with
  records (μ-R, under-specified, R7:220) and of whether it is coset-uniform or of the `D_0` form.
  Lemma A-T (c), Proposition AL (AL2), P0 (`D_0`, through R2's coset conditioning, P0:163–166) and
  the coset form of heralded preparations assume such laws. E(b) and OA-2 Corollary E2 need (xiv)
  instead, not a coset law (OA2:528–537, :752; BL:236–238).
- **Label: proposed route; load-bearing role shown in AL.** AL does not cover laws that satisfy
  no-signalling only as a mixture (BL:243–245), and a setting-dependent non-coset law with an affine
  readout gives the PR box (NOTES-r3:67–69). μ-O is derived (Main:54) but not shown coset-uniform;
  OA-1 D2 is "Not established under μ-O or μ-R" (OA1:154).
- **Interface.** The coset-dependent results: Lemma A-T (c), AL and P0.
- **§A.31 check.** "The negative results do not cover μ-O or μ-R" is a scope limit of those
  results, not evidence of non-classical structure under those laws.
- **Support.** [A] off `main` (BL); the measure split is on `main` (OA1:522; OA2:745–752).
- **Found by.** BL (§5 "Run law under (iv)", BL:275; NOTES-r3:76–78 assumption-watch); R7 (C8–C10);
  TS (N3.2–N3.3).
- **Smallest next check.** Read-only audit of which affine-class classicality results read (iv) as
  selecting a coset-uniform law (the NOTES-r3:76–78 marker, with T7), and whether the uniform law on
  an R-lin orbit is coset-uniform. Not authorized.

### MM-6. Native setting independence

- **Missing ingredient.** An account, inside `φ` and a stated law, of how an embedded observer's
  setting cells come to satisfy the independence that E(b), OBL-SP and the Bell stage-5 ceiling
  assume: (xiv) for the Bell analysis (Main:724), H-xiv for every admitted setting and herald
  procedure (R7:223, :257–264), MI\* over generator residues (BL:53–62), and TUNE-1's time-zero H-μ
  (P:145).
- **Label: proposed route; load-bearing role shown for E(b), OBL-SP and the Bell stage-5 ceiling.**
  These are carried as hypotheses, never derived (OA2:528; R7:257; BL:102, which rests on BS Theorem
  N/N′, off `main`). They are not hypotheses of Proposition AL (BL:205) or of OA-3 Theorem S
  (OA3:349–351); in AL the coset law (MM-5) plays their role (NOTES-r3:69). Their load-bearing role
  in these ceilings is shown: holding `φ_0` and access fixed, the initial law alone switches CHSH
  from 0 to 4 with complete-history no-signalling (BL:177); invariance of an unconditional marginal
  does not give operational no-signalling when settings correlate with the hidden state (S7,
  OC:584–595). H-xiv is not a consequence of `D_0` or `φ` (R7:223).
- **Reading [A, here].** Under μ-G, (xiv) holds for disjoint setting cells (OA2:750), but those
  values are uniform and are not selected by the observer in OA-1's N1-S sense (MM-1c). Under a `D_0`
  law, selection is supplied and independence is a clause of the posit ("independent of setting and
  carrier", OA1:556–558; TS:141). No law in the corpus is shown to supply both natively.
- **Interface.** Bell analysis (xiv); every admitted procedure (H-xiv); generator residues (MI\*).
  Owner Q2 (#1273 c.6860580909): MI\* stays a distinct hypothesis unless (xiv)'s variable is shown
  to contain every residue reaching the response or the full record.
- **Support.** [A] off `main` (BL, OC, R7); [P] for the posit (Main:724) and the cost of option (b)
  (Main:416).
- **Found by.** BL (stage 4 row, BL:101; §5 BL:277); R7 (C12); OC (S7); TS ((c), TS:141).
- **Smallest next check.** The owner reading of whether (xiv)'s response-relevant variable includes
  generator residues (BL §5, BL:276), which decides whether (xiv) is MI\*.

### MM-7. A restricted preparation family with complete-history no-signalling (masking)

- **Missing ingredient.** A physically preparable family `𝒫` whose restriction has a reason
  independent of the target table, for which complete-history no-signalling holds on a route that
  uses parameter dependence with MI kept.
- **Label: shown necessary.** Preparation-span diagnostic (PPS:134–145): for a finite `Λ` and laws
  common across setting interventions, if both wings obey complete-history no-signalling for every
  law in `𝒫` and `aff(𝒫) = aff(Δ(Λ))`, each wing's complete record is pointwise independent of the
  distant policy. So any parameter-dependence route (Main:412, option (a); OC routes A, B, C) needs
  `𝒫` of restricted affine span. That the restriction be physically sourced, for a reason
  independent of the target table, is a §A.29 and non-import requirement (OC:494), not part of the
  diagnostic. Observer class: two-wing protocols, finite `Λ`, laws common across settings, complete
  records.
- **Scope.** In AL's class every coset-uniform law with complete fixed-region no-signalling is
  Bell-local (BL:207–213), so the restriction question arises only outside that class.
- **Support.** [A] on `main` (PPS).
- **Found by.** BL (stage 6, BL:103; NBA row, BL:272); OC (N3, OC:494).
- **Smallest next check.** The separately authorized mixed-path computation under #868 (c.6794392080)
  for route C. AL's expectation is not written into it (owner Q3).

### MM-8. A selector of the quantum Bell set

- **Missing ingredient.** An OI-sourced principle, independent of the target table, that bounds CHSH
  by `2√2` and reaches it; for composites, which of the operational-completion conditions (i)–(v)
  (Main:562; `exactAll_iff_physical_general` [K]) an embedded process supplies (BL:271).
- **Label: shown necessary relative to the unrestricted class.** That class realizes the PR box
  (Main:360, :427 [P]); a channel with a pad alone gives the PR box (OC:497–500, [X S4] hand-checked).
  So a route exceeding 2 in that class reaches the quantum set only with a selector. This necessity
  follows from the definition of a selector. The PR control (OC:497–500) is generic, not sourced by
  OI.
- **Interface.** The unrestricted OI behaviour class (Main:427); stage 3 relaxed (BL:104). Inside
  AL's class quantum Bell tables are unreachable, so the selector is not the missing item there.
- **Context.** #1060 (Tsirelson selection open), supporting context only.
- **Support.** [P] on `main`; [X] off `main`.
- **Found by.** BL (stage 7); OC (N4).
- **Smallest next check.** None at paper level is identified that does not presuppose MM-3 or MM-4.

### MM-9. A non-site-fibred hidden factor (route A)

- **Missing ingredient.** A hidden factor `M` that is not site-fibred, adjacent to both wings (N1),
  with a directed path remote generator → `M` → near record inside the window (N2) (OC:490–493).
- **Label: proposed route (open obligation SLL).** SLL "is neither necessary nor sufficient for a
  Bell escape in OI: routes B and C do not pass through it" (OC:514–516). N1 conflicts with ledger
  (viii) as stated unless `M` is counted as a site (OC:492). N2's necessity rests on SB's L3 (off
  `main`), carried conditionally (`DEPENDENCIES.md` row D2).
- **Interface.** Route A only.
- **Support.** [A] off `main`.
- **Found by.** OC (§5, SLL); BL takes SLL as an input.
- **Smallest next check.** The owner question recorded in SLL: whether ledger (viii) binds a deep
  hidden sector (OC:532–535).

***

## 3. Priority order and its reason

**Counts under the metric of §1.** Each cell names the targets of §1; the interface of each claim is
in the entry.

| ID | (i) shown necessary on its own | (ii) one member of a disjunction | (iii) load-bearing role shown | Key | Rank |
|---|---|---|---|---|---|
| MM-3 | T4 (3b(iii)), T5 (3c, 3d), T6 (3a, 3b(ii), 3e) | — | — | (3, 0, 0) | 1 |
| MM-1 | T1 (1b′), T4 (1a) | T2 (1c) | — | (2, 1, 0) | 2 |
| MM-4 | T3 (4a) | T5 (4d), T7 (4c) | — | (1, 2, 0) | 3 |
| MM-7 | T7 | — | — | (1, 0, 0) | 4 |
| MM-8 | T8 | — | — | (1, 0, 0) | 5 |
| MM-2 | — | T1 (gap 1, "resolved classically by MP-0a or MP-0b", OA1:522), T2 (1c), T4 (TS (e), TS:143) | T5 (P0; OA-3 N4), T7 (AL4 against the selected read) | (0, 3, 2) | 6 |
| MM-5 | — | T7 (AL's non-coset exit) | — | (0, 1, 0) | 7 |
| MM-9 | — | — | — | (0, 0, 0) | 8 |
| MM-6 | blocks no construction; a hypothesis of E(b), OBL-SP and the Bell stage-5 ceiling | | | — | 9 |

MM-7 ranks before MM-8 by the tie rule: T8 presupposes a violation (T7). MM-4's route-B necessity
(4b) is not counted separately because route B is a route to T7, not a target.

**Reasons, entry by entry.**
1. **MM-3** has the most targets for which a sub-condition is shown necessary on its own. Its count
   comes from five sub-rows bundled under one ingredient.
2. **MM-1 blocks every protocol of TUNE-1's initial-condition schema (1a) and, under R-lin and μ-G,
   selectable preparation of hidden carriers (1b′; OA1:522, :526–529).** It is TUNE-1's first stop
   and blocks part (b); parts (c) content, (d) held outcomes and (f) inherit it, and (e) rests on it
   or on MP-0b (TS:380–382). Under μ-O and μ-R it is not shown to block (N1-K can be native; N1-S
   open, OA1:522). O-RDY is a listed prerequisite of #1143.
   - *Coupling with MM-2.* Under μ-G, complete in-`V` records cost blank memory (OA-1 D4(c),
     OA1:171–173). So in-`V` retention needs MM-1, and MP-0b places the records outside the
     observer (TS:143). #1147, in turn, lists native retention (O-RET, #1032) as a prerequisite of
     O-RDY. The two are coupled both ways (§6, T3).
3. **MM-4** is shown necessary for in-world classical setting selection under every measure (4a),
   and is one member of the disjunctions of AL's class (4c) and of Corollary E1 (4d). It is not
   sufficient for MM-3 (OA1:524).
4. **MM-7 and MM-8** are each shown necessary for one Bell target; both matter only outside AL's
   class, after one of AL's exits (MM-4, MM-5, non-cell settings or postselection).
5. **MM-2 decides the scope of every classification in the affine class (OBL-SP, AL, E(b), OA-1
   D4), and of Theorem S for `G_SM` through its record and herald conventions (AW-OA3-2).** It is a
   member of the disjunctions for T1 (holding the choice record, OA1:522), T2 and TUNE-1's part (e),
   and load-bearing for T5 and T7, but no target is shown to fail without a particular derivation of
   it.
6. **MM-5** conditions the reach of the coset-dependent results: Lemma A-T (c), AL and P0 extend
   beyond coset laws only through MM-5. E(b) and Corollary E2 need (xiv) instead (OA2:528, :752;
   BL:236–238). It also decides MM-1 under μ-R.
7. **MM-9** concerns route A alone, and SLL is neither necessary nor sufficient for T7.
8. **MM-6** is a hypothesis of E(b), OBL-SP and the Bell stage-5 ceiling (OA2:528; R7:257; BL:102).
   AL and Theorem S do not use it (BL:205; OA3:349–351); in AL the coset law (MM-5) plays its role
   (NOTES-r3:69). It blocks no construction.

**Sensitivity of the order to the metric.**
- *MM-3 unbundled.* Counted sub-row by sub-row, 3b has key (2, 0, 0) (T4, T6) and each of 3a, 3c,
  3d, 3e has (1, 0, 0). MM-1 (2, 1, 0) then ranks first, 3b second and MM-4 third.
- *Any role counted once.* Counting the targets for which an entry has any of the three roles gives
  MM-2 5 (T1, T2, T4, T5, T7); MM-1, MM-3 and MM-4 3 each; MM-5, MM-7 and MM-8 1 each. MM-2 then
  ranks first.
- The primary metric is the one fixed in §1. Choosing between the three is an owner question
  (§7, SQ8).

**What the targets separate.** MM-3 is the only entry whose target separates quantum from
classical. That is its definition, the qubit tier beyond the configuration ceiling (OA1:524). Its
necessary conditions 3b–3d are each met by classical systems (OA2:372–374; `𝔊_K`). MM-1, MM-4
and, under a fixed convention, MM-2 are met by a classical reversible computer (`𝔖_F` with MP-0a,
OA1:534–552). The targets of MM-5 to MM-9 are met by designed classical bijections when locality is
not imposed (BL §2; BL:108–109; Main:360).

**Dependencies, stated once.**
- MM-1 ⇄ MM-2 under μ-G (in-`V` retention; the disjunction of 1c).
- MM-2 → the scope of P0 (OBL-SP), AL, E(b) and OA-1 D4, and of Theorem S for `G_SM` through
  AW-OA3-2; MM-2 → MM-7 (the record region of no-signalling).
- MM-3d (with (H4), (SP), (xiv), H-AR) → MM-4 ∨ supplied control ∨ the OA2:600–604 exits.
- MM-4 is not sufficient for MM-3 (OA1:524).
- MM-5 → MM-1 (μ-R) and MM-5 → the scope of AL and P0.
- MM-7 and MM-8 arise only outside AL's class.
- MM-6 is carried by E(b), OBL-SP and the Bell stage-5 ceiling and is not consumed by any
  construction.

***

## 4. Unranked items

- **Open mathematics, not physical ingredients.**
  - TUNE-1 L5.4: whether translations supply the one-axis rotation family (TS:141).
  - The member specification of TUNE-1's candidate classes (TS:383–384).
  - NL-C for gates of `m ≥ L` rounds (TS:207–209).
  - OBL-SP itself (R7:249–264), and AW-OA2-1, which stays stopped.
  - AW-OA2-2 (unbounded horizons).
  - AL's extension to mixtures that satisfy no-signalling only jointly (BL:273).
  - A general access-only theorem for the Bell toys (NOTES-r3:81–84).
- **W1 (GR track, #1245).** W1 is an additional physical assumption of the ħ calibration, not a
  derived result (W11:288–300). It is not ranked here: it bears on no OI→QM operational target, and
  R7 row 30 (R7:144) finds no bearing on Q3 or Q4. It is not shown necessary; its gap route C6(a)
  is open for the finite substratum and fails in the real lift.

***

## 5. What is not claimed

- **No OI-wide no-go.** Each shown-necessary statement holds for its stated interface, observer
  class and assumptions only (TUNE-1's schema, R-lin with μ-G, the configuration identification,
  the affine class, a finite `Λ`, and so on). Absence results (MM-1b) and disjunctions (MM-1c,
  MM-4c, MM-4d) are not necessity claims.
- **No native Bell escape.** The PR witnesses of BL stages 0–4 are designed maps. The
  setting-selected-read witness is a different admissibility class (BL:262–263). Routes A, B and C
  are classifications and open obligations (OC §5).
- **No OI↔QM equivalence.** `S ⇔ D ⇔ Q_fb` is a finite-horizon representation theorem whose three
  directions are separately witnessed. No direction supplies an operation, locality or quantum
  selection (BL:106–118; R7 rows 1–3). Every one-direction result above (P0's scoped embedding, AL,
  E2, PAD ⇒ NS_A) is stated one way only.
- **No adopted premise.** MP-0a, MP-0b, H-PREP, M-INACC, M1/MP-1, H-xiv, H-μ, MI\*, (LF) and every
  Layer-0 candidate remain unadopted. The owner's "conditional ledger posit" label for (vii) adopts
  nothing new.
- **No sufficiency.** "Shown necessary" never means that supplying the ingredient yields the target.
- **No status or priority change.** The ranking is this deliverable's order under the metric of §1,
  not an Issue tier. No unit result becomes established by appearing here (§A.46 item 7). The
  "[A, here]" readings are unreviewed.

***

## 6. Cross-unit consistency check

**Agreements.**
- **A1. The first missing physical ingredient under μ-G is the ready resource.**
  - TS (first stop), OA-1 (gap 1) and R7 (C11, §3.2) agree.
  - NPS1 and NIS2 stop at the same ingredient for another rule (TS F-S3, TS:346–349).
  - BL and P0 quantify over the MP-0a / `D_0` family and do not source it.
  - TC-A fixes one `D_0`-form law as an admitted datum, not a derived one (TS:110–114).
- **A2. Affine translation (D5) is used the same way throughout.** See TS (c); P0 R1
  (P0:159–162); BL AL step 1 (BL:216); R7 row 13.
- **A3. NL-C is respected.** TS shows that no hypothesis fails for TC-A (TS:220–224), in line with
  R7 row 33 and the owner safeguard.
- **A4. Three affine-class classicality results, each under its own full hypothesis set.**
  - P0, the scoped pass under (LF): (H3), the r7 record class, held-at-use typing, C-PM, H-xiv,
    `D_0` (P0:454–459).
  - AL: (AL1)–(AL4) and (NS) (BL:189–203).
  - E(b): (H1), H-AR, (H3), (H4), (xiv), (SP) (OA2:528–537).

  Each has a record-access clause ((LF), (AL4), (H4)), and for each, dropping that clause leaves the
  case open. Each also has other open exits: for E(b), non-additive observers and non-spanning
  reachable laws (OA2:600–604); for AL, non-coset laws, non-cell settings and postselection
  (BL:242–248). No formal map between (LF), (AL4) and (SP) is given, and none is asserted here (Code
  Review Rules, "Bridge and no-go scope").
- **A5. TC-A and P0.** If a TC-A member were specified and fell in P0's class (H-AR, held-at-use
  records inside `S`, (H4) or (V-ii-H)), its prepare–measure fragment would carry P0's O-U. TC-A's
  (e) rests on MP-0b, which places records outside `V`, so membership is not shown, and TC-A has no
  classical pass from E(b) either (TS:296–297).
- **A6. r8 does not reach the other units.** The three r7 passages that r8 (`4b81298f`; review at
  `2a9f10ba`) corrects are R7:287–290, :299–300 and :320–321. None of them is cited by TS (which
  cites R7:215, 217, 220, 222, 223), by BL (C9, C10, H-xiv, `D_0`, Q2 levels) or by OC (vocabulary
  R7:94–104).

**Tensions and disagreements** (each is a finding to propagate when its record is next revised,
not a correction made here). T5 is carried as P0's record-only marker; any propagation waits on the
read-only check of §7 SQ4.
- **T1. Route C.** OC (copying S:183) says route C "is available with neither a new factor nor a new
  edge" and is "not assessed" (OC:480, :482–488). BL's AL closes route C for the affine class under
  (AL2)–(AL4): a remote-setting dependence of a complete history is absorbed into a local model or
  makes two remote settings perfectly distinguishable (BL:255–259). The two are compatible once
  scoped, since "available" means not excluded by L1. OC copies route C from the draft S at
  `86a413c8`, which predates AL, and carries no cross-reference to AL. AL's closure is [A], off
  `main`, and a stated expectation, not a substitute for the mixed-path computation (BL:258–259;
  owner Q3).
- **T2. The status word for ledger (vii).** OA-1 r5 says "The affine form is **derived** (ledger
  (vii))" (OA1:569), referring to the amplitude-scale gauge step (OA1:583–584). TS says "ledger
  posits, not derived" (TS:139). R7 C1 says "follows from stated premises" (R7:212). The owner's Q1
  says "a conditional ledger posit". The four agree that linearity is posited, but the labels
  differ.
- **T3. Ready resource and retention are coupled both ways.**
  - #1147 lists O-RET (#1032) as a prerequisite of O-RDY.
  - Under μ-G, in-`V` retention consumes ready cells (OA-1 D4(c); TS:143).
  - The planning edge and the units' finding therefore form a cycle under μ-G.
- **T4. The μ-O route.** TS leaves "conditional preparation through held records" open under μ-O
  (TS:140, :247–251). OA-1 D1 (OA1:141–143) makes every time-specific preparation under an invariant
  law conditional on a record event. The owner scope quoted in TS N5 says a conditioned event is
  not a producer (TS:306–308). If that scope applies to O-RDY generally, the μ-O route is an
  H-PREP-type identification and not a producer (§7, SQ2).
- **T5. AW-P0-2, on `main`.**
  - P0 records that OA-2 E(b) step 4 (OA2:534) and OA-3 N4.3 step 4 (OA3:468–469) take singleton
    indicators to be available under C-PM, which presumes label-free retention (P0:488–492).
  - P0 says this does not refute E(b), since N8.2(b) fails (SP).
  - The records on `main` do not state the presumption as a hypothesis.
- **T6. "Outside (vii)" versus "non-affine".** BL:81, :261 and OC route B (OC:479) name the exit
  "an update outside (vii)". AL (AL1), L4 and D5 hold for every affine update, so the exit each
  proves is a non-affine update.
- **T7. Coset premise.** NOTES-r3:76–78 lists E(b) and E2 among results that rest on a coset-uniform
  run law. BL:236–238 and OA2:528 state that E2 and E(b) need (xiv), not a coset law.

**Different names for one ingredient.**
- **Ready resource.**
  - "ready resource" (TS); O-RDY (#1147, OBS:100); "blank memory" (OA-1 D3, D4(c)); P2
    half-known ready cells (MECH-1; OA-1 SA-1(c)).
  - MP-0a / H-LOW (OA-1) and C11 (R7) name the boundary-law route to it.
  - `D_0` names the family that P0 and AL2 quantify over.
  - These are not one object. MP-0a is a law form, a premise once selected; O-RDY is the producer
    obligation; H-PREP is an identification hypothesis; `D_0` is a quantified family.
- **Retention.**
  - MP-0b / H-MEM (OA-1), C6 (R7), (H4) nested records (OA-2), (V-ii-H) (OA-3; retention-type under
    held-at-use typing), "complete local record windows" (BL (Rec)), and complete fixed-region
    histories (AL4).
  - These differ: BL's "every record the wing holds or can obtain" is broader than C5's "held = a
    function of present `V`", and MP-0b holds records outside `V`.
  - Owner Q4 fixes the BL notion for AL only.
- **Label-free access.** (LF) occurs only in P0. It is distinct from BL's setting-selected read and
  from G1's spanning frames. G1 relates to (SP) by analogy only (OC:323–326).
- **Measurement independence.**
  - (xiv): MI for the response-relevant pre-setting variable, Bell analysis only (Main:724).
  - MI\*: for `λ* = (Ω, ρ_A, ρ_B)`, generator residues included; kept distinct by owner Q2.
  - H-xiv: (xiv) extended to every admitted procedure (R7:257–264).
  - H-μ (P:145): time-zero independence of the unread world from labels; related to H-xiv, not
    reduced to it (R7:261–263).
  - (GI): generator isolation (BL).
  - H-IND (OC:67) is not a measurement-independence condition. It fixes a procedure kernel
    independent of the input law, analogous to H-LIFT, with the exact relation not audited.
- **Non-affine-update proposals.** MP-1 (OA-1), M1 (MECH-1), H-nl / R-nl (TUNE-1), C2 (R7), and
  `G_SM` / `G_σ` as instances share one necessary ingredient, a non-affine update (MM-4). They are
  not one object: MP-1 adds setting control, independence and sourced timing, and M1 adds diagonal
  confinement.

**Distinct objects kept distinct.**
- **Six gbit and PR witnesses, never pooled.**
  - `𝔊_K`: a designed non-affine reversible computer; a read-restriction gbit at bounded horizon
    (OA-2 N2.3; P0 control (iv); P0's O-SQ control).
  - N2.1: the non-spanning, preparation-restriction counterexample (OA2:296–315; P0 control (ii)).
  - P0 N8.2(b): a recorder gbit for an additive bijection outside R-lin with (xiii).
  - OA-3 N4.2: the (V-ii-U) shift artefact.
  - BL's setting-selected-read PR box, inside (vii).
  - BL's designed toys `φ_×` and `φ_0` with `μ_MD`.
- **Name collisions.**
  - H-μ means the uniform law μ-G in OBS (OBS:69–73) and time-zero label independence in TUNE-1
    (P:145) (TS:266–267).
  - "Route C" is INTERVENE's commutant route in one source and within-cone propagation in another
    (OC:123–125).
  - "C1–C18" are R7's candidate restrictions; "C1–C4" are P0's classifier checks. "C3" also names
    R7's FIX (R7:214) and OA-3's table row (OA3:529–530).
  - "N1–N4" are OA-1's operation tiers in one source and OC's Bell requirements in another; P0's
    nodes N1–N8, TS's nodes N0–N5 and OA-3's N1–N5 are further uses.
  - "Q1–Q4" are R7's questions in one source and BL's owner questions in another. This record's own
    questions are SQ1–SQ9.
  - "L" is r7's literal reading in one source and OC's lemmas L1–L4 in another. "B" is r7's broad
    reading (P0:442) and OC's route B.
  - "H3" is OC's "laws, no amplitudes" (OC:64) and OA-2/P0's "no supplied control". "H4" is OC's
    "records are coordinates" (OC:65) and OA-2's nested records.
  - "E1" and "E2" are OA-2's Corollaries (OA2:577, :606) and OC's Lemmas E1 and E2.
  - "G1" is OC's frame-relativity finding and criterion G1 of OA-2's G0–G3.
  - "D4" and "D5" are OA-1's facts and P's interface clauses D4/D5 (TS:121, :142).

***

## 7. Owner questions (for decision; none is decided here)

1. **SQ1. MM-1 and MM-2 under μ-G.** Should the ready resource and in-`V` retention be one
   obligation under μ-G (T3)? This is planning only.
2. **SQ2. Scope of "not a producer".** Does the scope statement quoted at TS:306–308 (#866
   c.6765161496, "An inverse image, conditioned event, imposed blank field or statistical weight is
   not a producer") apply to O-RDY generally?
   - If yes, OA-1 D1 excludes an unconditioned producer under every invariant law (μ-G, μ-O). MM-1's
     open part then becomes a selection question on `μ_H` (C11), and the H-PREP identification
     stays a separate question.
3. **SQ3. MM-2's home and the C3 check.**
   - Should MM-2 have one accountable home, or should its parts stay with their units (C5–C7 with
     REC-1, AL4 with #868, herald typing with OA-3)?
   - Is the paper-only C3 check for R-lin with (xiii) authorized? It is currently proposed and not
     authorized.
4. **SQ4. AW-P0-2 (T5).** Should there be a read-only check of whether OA-2 E(b) step 4 and OA-3
   N4.3 step 4 need a label-free-retention hypothesis stated in the records on `main`?
5. **SQ5. Labels and names (T2, T6 and the collisions).** Should future records use the owner's
   "conditional ledger posit" label for (vii), name the Bell and route-B exit "a non-affine update"
   rather than "an update outside (vii)", and avoid reusing H-μ and "route C" for different objects?
   This would be forward only (§A.42 item 6).
6. **SQ6. Route C wording (T1).** At any integration of #1274, should the package's route C row
   cross-reference AL's scoped closure, with AL's off-`main` status kept?
7. **SQ7. W1.** Should W1 stay out of this list (§4) and remain on #1245?
8. **SQ8. The ranking.** Which metric should order the list: the §1 metric (MM-3 first), MM-3
   unbundled (MM-1 first), or any role counted once (MM-2 first)? Is the chosen order to be proposed
   as a planning change? That would be a separate decision (§A.45).
9. **SQ9. Coset premise (T7).** Should the NOTES-r3:76–78 marker be narrowed to the coset-dependent
   results at the next revision of the Bell ladder?

***

## 8. §A.42 item 8: references

Each reference is classified on its own, by the claim it is attached to.

**Off `main`.**

| Reference | Used where | Classification |
|---|---|---|
| TS r2 (`35c5c116`) at `c539a60c` | MM-1a (F-S1, F-S2), MM-1 stop and producer routes, MM-2 (part (e)), MM-3b(iii), MM-4a (N1.5), A1, A3, A5, T4 | support off `main` (gap until landed) for F-S1, F-S2 and the stop verdict; the underlying NL-C′, Lemma P-1, OA-1 D1–D4 and MP-0a statements are on `main` |
| TS CONFIRM-r2 (`558ddc77`) at `c539a60c` | §0 | provenance (review status) |
| P0 r3 (`611a4d9a`) at `cd38655c` | MM-2, MM-5 (P0:163–166), A4, A5, T5 | support off `main` (gap) |
| P0 CONFIRM-r3 (`8b440f2d`) at `cd38655c` | §0 | provenance (review status) |
| R7 (`f1ffac0e`) at `cd38655c` | MM-1c (§3.2), MM-2 (C4–C7), MM-4 (C2), MM-5 (C8–C10), MM-6 (C12, H-xiv), §4, T2, A6 | support off `main` (gap) for §3.2 and the C-row statuses; the rows' underlying records are on `main` |
| R8 (`615b7de8`) at `2a9f10ba` | MM-2 interface (R8:297–303), A6 | support off `main` (gap) for the statement of the L reading; the decision itself is the owner record #1268 c.6860582570 |
| REC-1-REVIEW-r8 at `2a9f10ba` | §0 | provenance (review status) |
| BL r3 (`0298088d`) at `d8e4f80e` | MM-2, MM-4c, MM-5, MM-6, MM-7, MM-8, A4, T1, T6 | support off `main` (gap); Main:362–427 and PPS are on `main` |
| BL NOTES-r3 (`963d7352`) at `d8e4f80e` | MM-2 (:55–58), MM-5 (:67–69), MM-6 (:69), T7 (:76–78), §4 | support off `main` (gap) |
| BL CONFIRM-r3 (`c968776a`) at `d8e4f80e` | §0 | provenance (review status) |
| OC `NEW-RESULTS.md` (`1859e8c5`) at `d015131d` | MM-3e (E2), MM-3 §A.31 check (G1), MM-4b (L4), MM-6 (S7), MM-7 (N3), MM-8 (N4), MM-9 (SLL), T1, T6 | support off `main` (gap); L4 for finite `S_i` is Main:362 on `main` |
| OC `DEPENDENCIES.md` (`6c127b0a`) at `d015131d` | MM-3e (row A2), MM-9 (row D2) | provenance: used to classify the two gaps below |
| BS Theorem N/N′ (#1231 at `e1534b08`) | MM-6 and §3 item 8 ("Bell stage-5 ceiling", BL:102) | support off `main` (gap), as BL:298 classes it; the exogenous form, Main:364–389, is on `main` |
| SB L3 (#1232 at `86a413c8`) | MM-9 (N2's necessity) | support off `main` (gap), as OC row D2 |
| SB draft S at `86a413c8` (route C, S:183) | T1 | provenance: the dating of OC's copied text |
| APPROX r4a (#1221 at `e41cf613`) | MM-3e and the MM-3 §A.31 check (definition of the E_f classical class) | support off `main` (gap), as OC row A2 |
| TUNE-1 Step 3A (#1267 at `8228b3c2`) | MM-1a, through TC-A (TS:100–101) | support off `main` through TS (gap), as TS's own §7 classes it |
| QH (#1269) | not used in r2 | — |
| OICORE-1 (#1214) | not used | — |
| `REVIEW-r1.md` on `research/synthesis-1169-20261113` at `71253fd4` | Revision line | provenance |
| ChatGPT review 5892912253 (#1272) | §0; MM-1 scope | provenance (review status and scope limits) |
| ChatGPT review 5892912758 (#1268) | §0; MM-2 (§A.31 check, smallest next check) | provenance (review status and scope limits) |
| ChatGPT review 5892919040 (#1273) | §0 | provenance (review status and scope limits) |
| ChatGPT review 5895564670 (#1274) | §0; MM-8 | provenance (review status and scope limits) |
| ChatGPT review 5891524305 (#1268, r7 at `9f7d2612`) | §0; MM-1c | provenance (review status of R7) |
| #1169 c.6860584645 | authority | governance provenance |
| #1169 c.6854774010 | §0 | governance provenance |
| #1273 c.6860580909 | §0; MM-2, MM-4, MM-6, MM-7 | governance provenance (owner decisions Q1–Q4) |
| #1268 c.6860582570 | §0; MM-2 | governance provenance (owner decision on the L reading) |
| #866 c.6765161496, as quoted at TS:306–308 | MM-1 producer routes; T4; SQ2 | governance provenance; no result here rests on it; its reach is SQ2 |
| #868 c.6794392080 | MM-7 | governance provenance (mixed-path authorization) |
| #1147 body | MM-1; T3 | planning record; T3's planning statement rests on it; no scientific claim does |
| #1060 body | MM-8 | supporting context only |

**On `main` at `c3b5f37a`** (support on `main`; research records are not established, §A.46 item 7).

| Reference | Used where | Classification |
|---|---|---|
| OA1 (`5a16b213`) | MM-1, MM-3, MM-4, MM-5, MM-6, §3, T2, T4 | support on `main` [A] |
| OA2 (`8f8ddf73`) | MM-2, MM-3, MM-4d, MM-5, MM-6, A4, T5, T7 | support on `main` [A] |
| OA3 (`0a36fd05`) | MM-2, MM-3, MM-6, T5 | support on `main` [A] |
| W11 (`8bf64629`) | §4 | support on `main` [A] |
| OBS (`e657732b`) | MM-1 | support on `main` [A] |
| M1D (`7f8a142b`) | MM-4 | support on `main` [A] |
| M2D (`9352d9da`) | MM-3 | support on `main` [A] |
| PPS (`9123157c`) | MM-7 | support on `main` [A] |
| `minacc-1-20261108/RESULT.md` | MM-3 | support on `main` [A] |
| P (`84f71030`) | MM-1a; MM-6 (H-μ) | support on `main` [A] |
| AF (`ee8582b2`) | defined in §0; cited through TS | support on `main` [A] |
| S3 (`a9cbc675`) | MM-4a | support on `main` [A] |
| S4 (`17ca08f8`) | MM-1a; MM-3b(iii) | support on `main` [A] |
| NPS1 (`8f1edce3`) | MM-1 producer routes; A1 | support on `main` [A] |
| NIS2 (`1daf3861`) | A1 | support on `main` [A] |
| Main (`0db17597`) | throughout | support on `main` [P] |
| OB statements in MM-3a and MM-8 | MM-3a; MM-8 | support on `main` [K] |

This record cites no off-`main` content as the sole support of an "on `main`" label. Before any
landing, each "support off `main`" row is closed by landing its source or the entry is narrowed
(§A.42 items 2, 8).
