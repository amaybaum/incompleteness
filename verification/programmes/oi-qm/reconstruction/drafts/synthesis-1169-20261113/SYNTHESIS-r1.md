# #1169 synthesis (r1): prioritized missing-mechanism list from the four Bell-first paper units

**Standing.** WIP / UNVERIFIED author record. Paper-only: source reading and hand reasoning, no
computation on any OI rule, no script, no Lean build, no manuscript or record edit. It adopts no
premise, promotes no claim and changes no Issue priority or status. The order in §1 is the ranking
this deliverable asks for; it is not a planning-record change (§A.45). Every unit result used here
is a research record, model-reviewed, and not established (§A.46 item 7). The next steps are an
independent non-author review and the ChatGPT exact-head review.

**Authority.** #1169 c.6860584645 (`amaybaum`, 2026-11-13T17:47:40Z), owner answer "Start now
(Recommended)". Scope, verbatim: "It produces a prioritized list of missing mechanisms. Each entry is
labelled either **shown necessary**, with a cited proof, its assumptions and the observer class it
applies to, or **proposed route**. An obstruction found for one interface stays tied to that
interface, and #1060 is used only as supporting context." Not covered: "It merges nothing, starts
no new research or computation, adopts no premise and changes no priority."

***

## 0. Inputs, pins and labels

**Unit records (off `main`).** Paths under `verification/programmes/oi-qm/reconstruction/`; every
branch was fetched by name and its remote head equals the pinned commit.

| Short | Unit, PR | Head | File (blob) |
|---|---|---|---|
| TS | TUNE-1 sourcing, #1272 | `c539a60c` | `drafts/tune-1-sourcing-20261113/TUNE-1-SOURCING-r2.md` (`35c5c116`); `CONFIRM-r2.md` (`558ddc77`) |
| P0 | REC-1 P0, #1268 | `cd38655c` | `drafts/rec-1-20261113/REC-1-P0-r3.md` (`611a4d9a`); `REC-1-P0-CONFIRM-r3.md` (`8b440f2d`) |
| R7 | REC-1 r7 (context), #1268 | `cd38655c` | `drafts/rec-1-20261113/REC-1-r7.md` (`f1ffac0e`, unchanged since `9f7d2612`) |
| BL | Bell ladder, #1273 | `d8e4f80e` | `drafts/bell-ladder-20261113/BELL-LADDER-r3.md` (`0298088d`); `NOTES-r3.md` (`963d7352`); `CONFIRM-r3.md` (`c968776a`) |
| OC | Option-(c) package, #1274 | `d015131d` | `intervene-substate-results-20261113/NEW-RESULTS.md` (`1859e8c5`); `DEPENDENCIES.md` (`6c127b0a`) |

**ChatGPT exact-head reviews (host records, provenance; model review is not verification).**
5892912253 (#1272, ACCEPT, bounded); 5892912758 (#1268, ACCEPT of P0's O-U, r7 reconciliation
required); 5892919040 (#1273, ACCEPT as a conditional paper result, two safeguards); 5895564670
(#1274, ACCEPT as a scoped evidence package, integration gated). Their scope limits are carried in
§2 and §5.

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
(`0db17597`); OB = `verification/lean-mathlib/OIBridge/` (statements read, nothing built).

**Support layers.** [K] kernel statement on `main`; [P] manuscript proof on `main`; [A] paper
argument, hand-checked, not kernel-checked (on `main`: a research record, not established; off
`main`: a draft); [X] exact generic check (a script in a draft), not run here; [L] external
literature; conjecture. "[A, here]" marks a reading made in this file, unreviewed.

**Entry labels.** *Shown necessary*: a cited proof shows that, for the stated observer class or
interface and under the stated assumptions, the target fails without the ingredient. Necessity is
never sufficiency. *Proposed route*: no such proof; its status and its test are stated.

***

## 1. The list in priority order

| Rank | ID | Missing ingredient | Label | Tied to | Layer, location | Found by |
|---|---|---|---|---|---|---|
| 1 | MM-1 | Ready resource: a native producer of known-value cells, renewed per run | shown necessary (3 scoped forms); producer: proposed route | TUNE-1's initial-condition schema; μ-G; μ-G with held = present `V` | [A] off and on `main` | TS (first stop); OA-1; R7 §3.2 |
| 2 | MM-2 | A sourced embedded record and effect class: retention, herald typing, label delimitation, history region | shown necessary as a decision input; content: proposed route | affine class with `D_0` or coset laws; H-AR; two-wing every-run protocols | [A] off `main`; [A] on `main` | P0; BL; OA-3; TS (e) |
| 3 | MM-3 | An observer operation beyond the configuration-level ceiling (gap 3), with its interface-specific necessary conditions | shown necessary per sub-row; the operation itself: proposed route | per sub-row 3a–3e | [K], [P], [A] on `main`; [A] off `main` (3e) | OA-1, OA-2, OA-3; OC (E2, G1) |
| 4 | MM-4 | Setting-selective coupling: an update outside ledger (vii) | shown necessary for classical setting selection and for route B; one of four exits in AL's class; not sufficient for MM-3 | every observer under inclusion (4a); affine updates on products of abelian groups (4b); AL's class (4c) | [A] on `main`; [A] off `main`; [P] | OA-1; TS (N1.5); BL (AL); OC (L4) |
| 5 | MM-5 | The run law that posit (iv) selects for an observer with records, and whether it is coset-uniform | proposed route; load-bearing role shown in AL | affine class | [A] off `main` | BL; R7 (C8–C10); TS (N3.3) |
| 6 | MM-6 | A native source of setting independence (H-xiv, MI\*, H-μ) | proposed route; load-bearing role in every ceiling shown | Bell analysis; every admitted procedure | [A] off `main`; [P] | BL; R7 (C12); OC (S7); TS (c) |
| 7 | MM-7 | A sourced, restricted preparation family with complete-history no-signalling (masking) | shown necessary | parameter-dependence branch with MI kept, finite `Λ` | [A] on `main` | BL (stage 6, §5); OC (N3) |
| 8 | MM-8 | A selector of the quantum Bell set (CHSH in `(2, 2√2]` and not more) | shown necessary relative to the unrestricted class | the unrestricted OI behaviour class | [P]; [X] off `main` | BL (stage 7); OC (N4) |
| 9 | MM-9 | A non-site-fibred hidden factor written by one wing and read by the other (route A) | proposed route (open obligation SLL) | route A only | [A] off `main` | OC (N1, N2, SLL) |

Unranked items (open mathematics, not physical ingredients, and the W1 track) are in §4.

***

## 2. The entries

### MM-1. Ready resource

- **Missing ingredient.** A process inside the joint dynamics `φ`, from a stated initial or boundary
  law, that places cells at known values in an apparatus's ready configuration and its designated
  program or setting content at use time, renewed for every run. For TUNE-1's target the amount grows
  with precision. In the corpus this is the open obligation O-RDY (#1147; OBS:100, :121).
- **Label: shown necessary, in three scoped forms.** None is an OI-wide statement.
  - **(1a) TUNE-1's initial-condition schema.** At precision `ε` a run needs at least
    `2(K+1)|C_n| ≥ (K+1) log_q((1−4ε)/(4ε))` known `q`-ary cells; with a fixed supply `D` per run,
    `ε ≥ 1/(4(1 + q^{D/(K+1)}))`; a gate needs at least `log_q((1−4ε)/(4ε))` `q`-ary cells of
    setting content. Proof: F-S2 and F-S1 (TS:321–345), arithmetic on NL-C′ (S4:464–474 on `main`)
    and on the schema's designated sites (P:143, :184–199). Assumptions: finite alphabet `q`; blocks
    are translates of `C`; `r_O` fixed on all of `O`; NL-C′'s hypotheses hold at every interface
    (TS:185–224). Observer class: any embedded observer in that schema, any rule and law. Necessity
    only: that a supply yields the larger control region is not shown (TS:340–342).
  - **(1b) Global counting measure μ-G.** For a finite abelian `S`, an automorphism `φ` and the
    uniform law, every region is uniform at every time (Lemma P-1, OBS:529–545); point-preparing `M`
    `q`-ary cells by a herald costs `P(E) ≤ q^{−M}` (OA-1 D3, OA1:157–160). So no ready region
    exists at any time under μ-G and no bijection produces one (TS:239–246). Observer class: every
    observer; measure μ-G only.
  - **(1c) μ-G with "held = a function of the present `V`" (C5).** A selected hidden carrier cannot
    be held together with its choice record (OA-1 gap 1, D2 applied to N1-S, OA1:145–155, :522);
    and any held one-time statistic of fixed functions is the same for every `φ`, so a
    `φ`-dependent held statistic needs a law other than μ-G or a typing other than C5 (R7:185–206,
    marked unreviewed in its own text; the r7 record as a whole was independently reviewed and
    ChatGPT-reviewed). Observer class: held-at-use observers under μ-G.
- **Not shown.** That a producer is excluded under μ-O's conditional route, under μ-R, or under a
  structured `μ_H` (TS:247–255; OA1:522). For any invariant law, OA-1 D1 (OA1:141–143) gives an
  unconditional law that is the same at every time, so every time-specific preparation is
  conditional on a record event; whether such conditioning counts as a producer is an owner scope
  question (§7, Q2).
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
- **Interface.** As in (1a)–(1c), separately.
- **Support.** (1a) [A] off `main` on [A] on `main`; (1b) [A] on `main`; (1c) [A] on `main` (OA-1)
  and [A] off `main` (R7 §3.2).
- **Found by.** TS (first stop, TS:282–287; F-S3 records the same stop in NPS1 and NIS2 for the
  selected binary ring); OA-1 gap 1; R7 §3.2 (AW-REC-1). BL's AL2 and P0's `D_0` quantify over the
  MP-0a family without sourcing it.
- **§A.31 check.** The favourable readings "Main:58 admits MP-0a, so the supply is sourced" and
  "conditioning on the observer's configuration prepares the apparatus" are both rejected in TS
  (TS:301–309), and the rejection is kept here.
- **Smallest next check.** Paper-only: decide whether O-RDY, under every invariant law, reduces to
  the selection question on `μ_H` (C11), using OA-1 D1 and the answer to §7 Q2. Not authorized.

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
- **Label: shown necessary as a decision input.** Within the affine class the classical verdict
  changes with these items, by paired results:
  - **P0.** Under (LF) the coset-space model is a simplex embedding of the C-PM prepare–measure
    fragment (N5–N6, P0:250–293). Without (LF), an additive bijection meeting every OBL-SP hypothesis
    except R-lin with (xiii) gives a preparation-contextual gbit (N8.2(b), P0:318–352). Observer
    class: H-AR, (H3), the r7 record class, held-at-use typing with records inside `S`, C-PM, H-xiv,
    `D_0`.
  - **BL.** Inside (vii) with a coset law and MI\*: no-signalling on the complete fixed-region
    histories forces a Bell-local law (Proposition AL, BL:187–229); no-signalling imposed only on a
    setting-selected read admits the PR box (BL:249–253). Observer class: two-wing every-run
    protocols with cell-valued settings, every pair admissible, no postselection.
  - **OA-3 N4 (on `main`).** Under (V-ii-U) a 3-cell shift gives a gbit; with (V-ii-H) Theorem
    E(b) holds without (H4) (OA3:392–497).

  What is shown is the dependence, not which convention is physical.
- **§A.31 check.** Every non-classical pattern found in or next to the affine class (P0 N8.2(b),
  BL's selected read, OA-3's (V-ii-U) shift) appears at a record-convention boundary, and OA-3 N4
  classes one of them as a memory or herald artefact. A convention that is chosen rather than
  derived from the Definition therefore cannot carry a non-classical result. P0's N8.2(b) gbit is
  outside R-lin with (xiii) (P0:350–352; ChatGPT review 5892912758: "not a contextual witness inside
  the target rule class"), and a gbit at bounded horizon does not separate classical from quantum
  (OA-2 N2.3, R7 row 20).
- **Interface.** This entry is the interface. Its parts are fixed separately where the owner has
  decided: the literal L reading for r7's class (c.6860582570); the full-history convention for AL
  only, with the setting-selected case separate (c.6860580909).
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
| 3a | Change what an observer operation acts on | Configuration identification `obsTheory = permTheory Conf`, every rule: no phases, not `DerivedOI` on any carrier, no dense control on `Fin 2`; rule-derived configuration interfaces stay inside (D6) | `obsTheory_rule_independent` OB/SubstratumInterfaceAudit.lean:780; `phase_ceiling_rule_independent`, `nonnegBounded_verdict` OB/FrozenSourcing.lean:302, :327; OA1:418–421 | [K] on `main` |
| 3b | Carriers that grow with the demanded exactness or precision | (i) Exact infinite-order reversible trace-preserving emergent control: at fixed finite `S` these operations form a finite group, every rule, μ and interface (OA-2 Theorem C). (ii) Exact full qubit prepare–measure theory: no fixed finite realization, under the preparation → finite ontic system → measurement factorization (Main:558). (iii) TUNE-1's target at precision `ε`: control region `|C| ≥ ½ log_q((1−4ε)/(4ε))` (NL-C′) | OA2:332–376; Main:558; S4:464–474 | [A] on `main`; [P] with [L]; [A] on `main` |
| 3c | Preparation or effect equivalences coarser than ontic equality, used non-trivially | The configuration model is always preparation-noncontextual (Prop. B(i)), and measurement-noncontextual when the restriction map is injective (B(ii)(⇐)); the converse (⇒) needs (CVX) and is not used here | OA2:242–300; N2.6 row N-b, OA2:682 | [A] on `main` |
| 3d | Settings that do more than translate the joint held record | Any rule, under (H4), (SP) and (xiv), G3 on the prepare–measure fragment (Corollary E1); exits named at OA2:599–604 | OA2:577–605 | [A] on `main` |
| 3e | On route E_f, a pair of incompatible sharp native measurements, which requires leaving E2's class | One linear encoding `L` defined on every density matrix and shared by all procedures, P-CONF∞, H4, H-IND: any two native procedures are jointly measurable and projective ones commute (E2). Outside: context-dependent encodings `L_c`, non-linear or history-dependent realizations (E_r, C-dyn), encodings positive only on a restricted preparation set, or failure of H-IND | OC:333–392 (scope OC:376–384) | [A] off `main` |

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
    non-import test (OA-1 key test, OA1:534–552). G1 (OC:263–331) shows that on non-spanning frames a
    nonnegative frame matrix does not separate classical from non-classical transformations, so an
    E_f verdict must state whether its frame spans.
- **Interface.** Per sub-row; no sub-row is generalized beyond its stated class.
- **Found by.** OA-1, OA-2, OA-3 (on `main`); OC (E2, G1); TS (3b(iii), through NL-C′); R7 rows 9,
  18–23.
- **Smallest next check.** OA-3's open regime (an H-AR observer without three consecutive held sites,
  short horizons; OA3:568–581) is where the preregistered `G_SM` computation is decisive; it needs
  owner authorization together with OA-3's proposed design amendments. No paper-only check of
  comparable size is identified.

### MM-4. Setting-selective coupling: an update outside ledger (vii)

- **Missing ingredient.** A coupling whose non-translational part depends on a stored setting
  (OA-1 MP-1, OA1:565–584; MECH-1 M1, M1D:125–128, :940–; TUNE-1 H-nl; R7 C2), that is, an update
  outside ledger (vii).
- **Label: shown necessary, for three separate targets.**
  - **(4a) Classical setting-selective control.** Under one affine `φ` acting on every cell, a stored
    setting acts on a carrier only by translation, for every measure (OA-1 D5, D7, OA1:176–195,
    :523; re-derived in S3 and M1D). Dropping A5 linearity alone, keeping the affine form, does not
    restore control. Observer class: every embedded observer, given inclusion (settings are cell
    content, no write outside `φ`). TS N1.5 applies it to setting-dependent durations (TS:214–219).
  - **(4b) Preparation-indexed long edges (Bell route B).** For an affine update on a product of
    abelian groups, the dependency relation is the same on every non-empty state class (L4,
    OC:427–465; for finite `S_i`, Main:362 [P]). So route B needs a non-additive update
    (OC:450–453; Main:414).
  - **(4c) A Bell violation with complete-history no-signalling in AL's class.** Proposition AL
    (BL:187–263) leaves four exits: an update outside (vii), a run law that is not coset-uniform,
    settings that are not cell values, or postselection (BL:78–83). Here (vii) is one disjunct, not
    a necessary condition on its own.
- **Not sufficient for MM-3.** Non-affine rules at the configuration level stay inside the kernel
  ceiling (OA-1 D6, row 5b; OA1:524, :539–544). The repair is classical only.
- **Proposed route status.** Each candidate (`G_SM`, `G_σ`, R-nl, MP-1, M1) is a Layer-0 revision
  under §A.29, "Hard to vary? No in bare form" (OA1:570). BL:280–284 lists what such a revision
  would have to preserve and predict. Owner Q1 (#1273 c.6860580909): (vii) is a conditional ledger
  posit.
- **Support.** (4a) [A] on `main`; (4b) [A] off `main` with [P] for finite `S_i`; (4c) [A] off
  `main`.
- **Found by.** OA-1 (gap 2); MECH-1 (M1); TS (N0.2, N1.5); BL (AL); OC (L4).
- **Smallest next check.** Paper-only, before any evaluation: a §A.29 statement for one candidate
  (`G_SM`) of the results it must preserve (dispersion, area law, Main:362's reference graph) and one
  independent prediction. Not authorized.

### MM-5. The run law posit (iv) selects for an observer with records

- **Missing ingredient.** A derivation of the law that posit (iv) selects for an observer with
  records (μ-R, under-specified, R7:220) and of whether it is coset-uniform or of the `D_0` form.
  Lemma A-T (c), Theorem E(b) with heralds, Proposition AL (AL2) and P0 (`D_0`) all assume such laws.
- **Label: proposed route (open).** Its load-bearing role is shown in BL: AL does not cover laws
  that satisfy no-signalling only as a mixture (BL:243–245), and a setting-dependent non-coset law
  with an affine readout gives the PR box (NOTES-r3:67–69). μ-O is derived (Main:54) but not shown
  coset-uniform; OA-1 D2 is "Not established under μ-O or μ-R" (OA1:154).
- **Interface.** The affine class, every observer whose verdict rests on a coset-uniform law.
- **§A.31 check.** "The negative results do not cover μ-O or μ-R" is a scope limit of those
  results, not evidence of non-classical structure under those laws.
- **Support.** [A] off `main` (BL); the measure split is on `main` (OA1:522; OA2:745–752).
- **Found by.** BL (§5 "Run law under (iv)", BL:275; NOTES-r3:76–78 assumption-watch); R7 (C8–C10);
  TS (N3.2–N3.3).
- **Smallest next check.** Read-only audit of which affine-class classicality results read (iv) as
  selecting a coset-uniform law (the NOTES-r3:76–78 marker), and whether the uniform law on an
  R-lin orbit is coset-uniform. Not authorized.

### MM-6. Native setting independence

- **Missing ingredient.** An account, inside `φ` and a stated law, of how an embedded observer's
  setting cells come to satisfy the independence that the classical-ceiling results assume: (xiv)
  for the Bell analysis (Main:724), H-xiv for every admitted setting and herald procedure (R7:223,
  :257–264), MI\* over generator residues (BL:53–62), and TUNE-1's time-zero H-μ (P:145).
- **Label: proposed route (open).** These are carried as hypotheses, never derived. Their
  load-bearing role in the ceilings is shown: holding `φ_0` and access fixed, the initial law alone
  switches CHSH from 0 to 4 with complete-history no-signalling (BL:177); invariance of an
  unconditional marginal does not give operational no-signalling when settings correlate with the
  hidden state (S7, OC:584–595). H-xiv is not a consequence of `D_0` or `φ` (R7:223).
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
  `𝒫` of restricted affine span. Observer class: two-wing protocols, finite `Λ`, laws common across
  settings, complete records.
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
  So a route exceeding 2 in that class reaches the quantum set only with a selector.
- **Interface.** The unrestricted OI behaviour class (Main:427); stage 3 relaxed (BL:104). Inside
  AL's class quantum Bell tables are unreachable, so the selector is not the missing item there.
- **Context.** #1060 (Tsirelson selection open), supporting context only. QH's encoded `U′` composite
  reaches a non-quantum table that is Bell-local over Pauli-axis tests (BL:104; QH off `main`).
- **Support.** [P] on `main`; [X] off `main`.
- **Found by.** BL (stage 7); OC (N4).
- **Smallest next check.** None at paper level is identified that does not presuppose MM-3 or MM-4.

### MM-9. A non-site-fibred hidden factor (route A)

- **Missing ingredient.** A hidden factor `M` that is not site-fibred, adjacent to both wings (N1),
  with a directed path remote generator → `M` → near record inside the window (N2) (OC:490–493).
- **Label: proposed route (open obligation SLL).** SLL "is neither necessary nor sufficient for a
  Bell escape in OI: routes B and C do not pass through it" (OC:514–516). N1 conflicts with ledger
  (viii) as stated unless `M` is counted as a site (OC:492). N2's necessity rests on L3, carried
  conditionally (`DEPENDENCIES.md` row D2).
- **Interface.** Route A only.
- **Support.** [A] off `main`.
- **Found by.** OC (§5, SLL); BL takes SLL as an input.
- **Smallest next check.** The owner question recorded in SLL: whether ledger (viii) binds a deep
  hidden sector (OC:532–535).

***

## 3. Priority order and its reason

The order ranks entries by how many downstream results each blocks.

1. **MM-1 blocks every embedded protocol.** Preparation comes first in operation order. MM-1 is
   TUNE-1's first stop and blocks its parts (b)–(f) (TS:380–382). It is OA-1's gap 1 under μ-G,
   and O-RDY is a listed prerequisite of #1143. Under μ-G with C5 it also blocks every
   `φ`-dependent held statistic (MM-1c).
2. **MM-2 decides the scope of every classification in the affine class.** That covers OBL-SP,
   AL, Theorem S, E(b) and OA-1 D4. It also decides TUNE-1's part (e) and whether MM-7 and MM-8 arise
   inside (vii).
   - *Coupling with MM-1.* Under μ-G, complete in-`V` records cost blank memory (OA-1 D4(c),
     OA1:171–173). So in-`V` retention needs MM-1, and MP-0b places the records outside the
     observer (TS:143).
   - #1147, in turn, lists native retention (O-RET, #1032) as a prerequisite of O-RDY. The two
     are coupled both ways (§6, T3).
3. **MM-3 is the only entry whose closure would discriminate quantum from classical.** MM-1, MM-4
   and, under a fixed convention, MM-2 can be met by a classical reversible computer: `𝔖_F` with
   MP-0a passes N1–N4 and still fails the qubit tier under the configuration interface
   (OA1:534–552). MM-3 is independent of MM-4: the gap-2 repair does not close gap 3 (OA1:524).
   It ranks below MM-1 and MM-2 because every MM-3 route still needs a prepared apparatus and a
   fixed record class.
4. **MM-4 blocks three targets.** These are in-world classical setting selection under every
   measure, Bell route B, and one of AL's four exits. It opens no MM-3 route by itself.
5. **MM-5 conditions the reach of the negative results.** Every affine-class negative result
   extends beyond coset laws only through MM-5. It also decides MM-1 under μ-R.
6. **MM-6 is a hypothesis of every ceiling** (OA-2 E(b), OBL-SP, Bell stage 5). It is ranked
   below MM-5 because its open part is a derivation of a posit already carried, not a mechanism
   whose absence blocks a construction.
7. **MM-7, MM-8 and MM-9 are Bell-specific.**
   - MM-7 and MM-8 matter only outside AL's class, after one of AL's exits (MM-4, MM-5, non-cell
     settings or postselection).
   - MM-9 concerns route A alone.

**Dependencies, stated once.**
- MM-1 ⇄ MM-2 under μ-G (in-`V` retention).
- MM-2 → MM-3 (sub-rows 3c, 3d and G3 targets) and MM-2 → MM-7 (the record region of no-signalling).
- MM-5 → MM-1 (μ-R) and MM-5 → the scope of every MM-2 result.
- MM-4 ↛ MM-3.
- MM-7 and MM-8 arise only outside AL's class.
- MM-6 is carried by the ceilings and is not consumed by any construction.

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
  class and assumptions only (TUNE-1's schema, μ-G, the configuration identification, AL's class, a
  finite `Λ`, and so on).
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
- **No status or priority change.** The ranking is this deliverable's order, not an Issue tier. No
  unit result becomes established by appearing here (§A.46 item 7). The "[A, here]" readings are
  unreviewed.

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
- **A4. The affine class is classical when the observer has full, label-free or fixed-region access
  to a coset-uniform record.**
  - P0 under (LF): P0:417–422.
  - AL under (AL4): BL:207–213.
  - E(b) under (H4) and (SP): OA2:522–576.
  - In each, the open case is a restricted record region.
  - No formal map between (LF), (AL4) and (SP) is given, and none is asserted here (Code Review
    Rules, "Bridge and no-go scope").
- **A5. TC-A's prepare–measure fragment would inherit P0's outcome.** TS N4 defers the (SP)
  question to P0 (TS:296–297). P0 is O-U, so TC-A gets no classical pass from E(b).
- **A6. r8 does not reach the other units.** The three r7 passages that r8 will correct are
  R7:287–290, :299–300 and :320–321. None of them is cited by TS (which cites R7:215, 217, 220,
  222, 223), by BL (C9, C10, H-xiv, `D_0`, Q2 levels) or by OC (vocabulary R7:94–104).

**Tensions and disagreements** (each is a finding to propagate when its record is next revised,
not a correction made here).
- **T1. Route C.** OC (copying S:183) says route C "is available with neither a new factor nor a new
  edge" and is "not assessed" (OC:480, :482–488). BL's AL closes route C for the affine class under
  (AL2)–(AL4): a remote-setting dependence of a complete history is absorbed into a local model or
  makes two remote settings perfectly distinguishable (BL:255–259). The two are compatible once
  scoped, since "available" means not excluded by L1. OC carries no cross-reference to AL, which
  postdates it.
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
  H-PREP-type identification and not a producer (§7, Q2).
- **T5. AW-P0-2, on `main`.**
  - P0 records that OA-2 E(b) step 4 (OA2:534) and OA-3 N4.3 step 4 (OA3:468–469) take singleton
    indicators to be available under C-PM, which presumes label-free retention (P0:488–492).
  - P0 says this does not refute E(b), since N8.2(b) fails (SP).
  - The records on `main` do not state the presumption as a hypothesis.

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
- **Ledger (vii) exits.** These are the same lever under different names: MP-1 (OA-1), M1
  (MECH-1), H-nl / R-nl (TUNE-1), C2 (R7), "an update outside (vii)" (BL, OC route B), and
  `G_SM` / `G_σ` as instances.

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
  - "C1–C18" are R7's candidate restrictions; "C1–C4" are P0's classifier checks.
  - "N1–N4" are OA-1's operation tiers in one source and OC's Bell requirements in another.
  - "Q1–Q4" are R7's questions in one source and BL's owner questions in another.
  - "L" is r7's literal reading in one source and OC's lemmas L1–L4 in another.

***

## 7. Owner questions (for decision; none is decided here)

1. **MM-1 and MM-2 under μ-G.** Should the ready resource and in-`V` retention be one obligation
   under μ-G (T3)? This is planning only.
2. **Scope of "not a producer".** Does the scope statement quoted at TS:306–308 (#866 c.6765161496,
   "An inverse image, conditioned event, imposed blank field or statistical weight is not a
   producer") apply to O-RDY generally?
   - If yes, OA-1 D1 excludes an unconditioned producer under every invariant law (μ-G, μ-O). MM-1's
     open part then becomes a selection question on `μ_H` (C11), and the H-PREP identification
     stays a separate question.
3. **MM-2's home and the C3 check.**
   - Should MM-2 have one accountable home, or should its parts stay with their units (C5–C7 with
     REC-1, AL4 with #868, herald typing with OA-3)?
   - Is the paper-only C3 check for R-lin with (xiii) authorized? It is currently proposed and not
     authorized.
4. **AW-P0-2 (T5).** Should there be a read-only check of whether OA-2 E(b) step 4 and OA-3 N4.3 step
   4 need a label-free-retention hypothesis stated in the records on `main`?
5. **Labels and names (T2 and the collisions).** Should future records use the owner's "conditional
   ledger posit" label for (vii), and avoid reusing H-μ and "route C" for different objects? This
   would be forward only (§A.42 item 6).
6. **Route C wording (T1).** At any integration of #1274, should the package's route C row
   cross-reference AL's scoped closure, with AL's off-`main` status kept?
7. **W1.** Should W1 stay out of this list (§4) and remain on #1245?
8. **The ranking.** Is the §1 order to be proposed as a planning change? That would be a separate
   decision (§A.45).

***

## 8. §A.42 item 8: references to content off `main`

| Reference | Used where | Classification |
|---|---|---|
| TS at `c539a60c` (F-S1, F-S2, N1, N3, N5, (b)–(f) rows) | MM-1a, MM-1 producer routes, MM-2, MM-3b(iii), MM-4a, A1, A3, A5, T4 | support off `main` (gap until landed) for F-S1, F-S2 and the stop verdict; the underlying NL-C′, Lemma P-1, OA-1 D1–D4 and MP-0a statements are on `main` |
| P0 at `cd38655c` (N5, N6, N8.2(b), AW-P0-2, §6) | MM-2, A4, T5 | support off `main` (gap) |
| R7 at `cd38655c` (§3.2, C-rows, rows 1–3, 9, 13, 18–23, 30, 33, OBL-SP) | MM-1c, MM-2, MM-4, MM-5, MM-6, §4, A6 | support off `main` (gap) for §3.2 and the C-row statuses; vocabulary otherwise; the rows' underlying records are on `main` |
| BL at `d8e4f80e` (Proposition AL, controls, §5, NOTES-r3) | MM-2, MM-4c, MM-5, MM-6, MM-7, MM-8, A4, T1 | support off `main` (gap); Main:362–427 and PPS are on `main` |
| OC at `d015131d` (E2, G1, L4, §5, S7) | MM-3e, MM-4b, MM-6, MM-8, MM-9, T1 | support off `main` (gap); L4 for finite `S_i` is Main:362 on `main` |
| QH (#1269), BS (#1231), SB (#1232), 3A (#1267), OICORE-1 (#1214), APPROX (#1221) | through the units only | provenance here; each unit's own §A.42 table classifies its use |
| ChatGPT reviews 5892912253, 5892912758, 5892919040, 5895564670; independent reviews in each unit | §0, §2 | host and review records; provenance; model review is not verification |
| #1169 c.6860584645, c.6854774010; #1273 c.6860580909; #1268 c.6860582570; #866 c.6765161496 (as quoted in TS) | authority, §2, §7 | governance provenance |
| #1147, #1060 bodies | MM-1, MM-8 | planning provenance; #1060 supporting context only |

Records on `main` used (support on `main`, as research records not established, or [P] and [K]): OA1,
OA2, OA3, W11, OBS, M1D, M2D, PPS, `minacc-1-20261108/RESULT.md`, Main, and the OB statements
cited in MM-3a and MM-8.

This record cites no off-`main` content as the sole support of an "on `main`" label. Before any
landing, each "support off `main`" row is closed by landing its source or the entry is narrowed
(§A.42 items 2, 8).
