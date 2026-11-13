# REC-1 (r7): embedded-operations reconciliation of the OI→QM results (paper-only draft)

**Revision.** r2 applies the required changes RC-1 to RC-16 of the independent review of r1
(draft PR #1268, r1 at `d7f7aac1`), with the dispositions in `REC-1-RESPONSE-r1.md`. Each cited source line was
re-read before the change was made. r3 applies the required changes RC-r2-1 to RC-r2-5 and two
optional suggestions of the re-check of r2 (r2 at `b39e40ff`), with the dispositions in
`REC-1-RESPONSE-r2.md`. r4 applies the ChatGPT review of r3 (#1268 review 5890763675, r3 at
`1fd0c241`) by the repair the owner chose, an explicit hypothesis, with the dispositions in
`REC-1-RESPONSE-r3.md`. r5 applies the required changes RC-r4-1 and RC-r4-2 and the optional
suggestion of the confirmation of r4 (r4 at `c73e855f`), with the dispositions in
`REC-1-RESPONSE-r4.md`. r6 applies the ChatGPT review of r5 (#1268 review 5890968976, r5 at
`6de32c95`) under the owner's decision "Proceed with all (Recommended)", with the disposition in
`REC-1-RESPONSE-r5.md`. r7 applies the required changes RC-r6-1 and RC-r6-2 of the confirmation of r6
(r6 at `1ab6371b`), with the dispositions in `REC-1-RESPONSE-r6.md`.

## 1. Header

**Purpose.** A dependency map of the existing OI→QM results under the embedded-observer framing of
#1236 c.6847314661 and TUNE-1 Step 3A r3 §2A. Each input result is classified by its layer of support,
its scope and conditions, and by whether its premises are consequences of the substratum dynamics or
describe one observer interface (Q1), or whether it derives an operation reachable by an embedded
observer or only a mathematical representation (Q2). Q3 lists candidate restrictions on the
observer–substratum interaction class with the component each filters and its premise status. Q4
names one open obligation, or the missing premise. Section 5 lists Issue-priority proposals for the
owner. Nothing here is a new theory, a new computation, an adopted premise or a change of status.

**Authority.**
- Owner decision, #1169 c.6850732002 (`amaybaum`, 2026-11-13T10:51:17Z): "Authorize, start now
  (Recommended)". "It authorizes REC-1 as scoped in c.6848080209." Still unauthorized there: "Step
  3B, the G_SM computation, G-C, G-D and G-E, any priority change, and any merge."
- Scope, #1169 c.6848080209 (`amaybaum`, 2026-11-13T08:34:02Z): questions Q1–Q4, the inputs, the
  output, and the constraints "Paper-only: no computation on OI rules, no Lean, and no new premise
  adopted"; "Accepted results keep their scope. Nothing is reclassified upward."
- Safeguards, #1169 c.6848268369 (posted by `amaybaum`, 2026-11-13T08:44:28Z, the ChatGPT scope
  review): "TUNE-1's NL-C remains rule-independent within its per-round bounded-cell label-menu form,
  including emergent controls of that form. OA-3's reconstruction/simplex result concerns its
  finite-ring observers and named hypotheses, not arbitrary cubic-lattice observers"; "Separate a
  mathematically definable construction, an operation reachable under one fixed dynamics from stated
  initial/boundary conditions, and a physically derived embedded access/control family"; "Name the
  smallest useful open obligation … only if it can be justified without adopting a new physical
  premise. Otherwise report that missing premise and stop. Do not define the obligation by assuming
  quantum target behavior." (Emphasis removed.)

**Method.** Reading and hand reasoning only. No script computing on any OI rule, no Lean build, no
manuscript or record edit. Commands used: `git fetch` by branch name, `git show`, `git rev-parse`,
`git log`, `git merge-base`, `grep`, `sed`, `awk`, `curl` reads of the GitHub API.

**Inputs.** On `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`, blobs by
their first 8 characters:

| Short name | Path (under `verification/programmes/` unless a paper) | Blob |
|---|---|---|
| Main | `papers/Main.md` | `0db17597` |
| OA1 | `oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md` (accepted r5) | `5a16b213` |
| OA2 | `oi-qm/reconstruction/oa-2-20261112/OA-2-REPORT-r4.md` (accepted r4) | `8f8ddf73` |
| OA3 | `oi-qm/reconstruction/oa-3-20261112/OA-3-REPORT-r4.md` (accepted r4) | `0a36fd05` |
| W11 | `physical-realization/w1-1-20261112/W1-1-REPORT-r4.md` (accepted r4) | `8bf64629` |
| S3, S4 | `oi-qm/reconstruction/drafts/tune-1-20261111/TUNE-1-STEP2-SESSION3.md`, `-SESSION4.md` | `a9cbc675`, `17ca08f8` |
| M1D | `oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md` (MECH-1, PR #1191) | `7f8a142b` |
| M2D | `oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md` (MECH-2, PR #1195) | `9352d9da` |
| B4P | `oi-qm/reconstruction/bsel-2-b4prime-20261105/B4PRIME.md` | `aff62906` |
| Q2A | `oi-qm/reconstruction/bsel-2-q2a-ce-20261105/RESULT.md` (the #1139 record) | `7fd5aeda` |
| MR1 | `oi-qm/reconstruction/oiqmsel-m1-alt-w-20261105/RESULT.md` (M-1) | `321bc874` |
| Lean | `verification/lean-mathlib/OIBridge/` (statements read, nothing built) | — |

Off `main` (scoped context, not support on `main`):

| Short name | Source | Commit | Blob |
|---|---|---|---|
| 3A | `TUNE-1-STEP3A-r3.md`, branch `research/tune1-step3a-1236-20261113` (PR #1267) | `8228b3c24e17a17f324b6779b53b04ad296b4308` | `7bbec04d` |
| OC1 | `oi-qm/reconstruction/oicore-1-20261108/OICORE-1.md`, branch `research/oicore1-record-20261109` (PR #1214) | `7722612883f5fc694f3e4dafae84f00f4407073d` | `83188952` |

Framing only, not evidence: #1143 body including the section "Embedded-observer selection: classical
and quantum contexts (owner reformulation, 2026-11-09)"; #1236 c.6847314661; #1169 comments of
2026-11-12 and 2026-11-13.

Pin facts checked here: `2d064a71` (the commit at which 3A cites the OA reports), `62bdc2cf` and
`080cd2be` are ancestors of `c3b5f37a`; `papers/Main.md` and the TUNE-1 directory are unchanged from
`080cd2be` to `c3b5f37a`; between `2d064a71` and `c3b5f37a` the OA report bytes differ only in
OA2 lines 65 and 958, which no citation below uses. So 3A's line citations of Main, S3, S4 and the OA
reports hold on `main` at `c3b5f37a`.

**Status markers.**
- [K] Lean statement on `main`, read, not rebuilt.
- [E] exact algebra by hand, in the cited record.
- [W] paper derivation: in a manuscript on `main` (`Main:n`) or in a record (with the record cited);
  "[W, REC-1]" marks a reading made in this file, unreviewed.
- [R] research record on `main`, not independently established (§A.46 item 7); any use carries the
  record's hypotheses.
- [R-off] research record off `main`; scoped context only.
- [L] imported external result.

**Terms used in Q1/Q2 (from 3A:259–344 [R-off]; the distinction itself is the owner's, c.6848268369).**
- Q1-D: the result's premises are properties of the substratum dynamics or of stated substratum posits
  (finiteness, the rule class), and hold for every observer interface.
- Q1-I: a premise describes one observer interface (state-space identification, access, record class,
  effect class, control schema); the premise is named.
- Q1-μ: a premise is a property of the initial law.
- Q2-A: a mathematically definable construction or representation (Level A).
- Q2-F: an operation reachable under one fixed dynamics from stated initial or boundary conditions.
  The row states the dynamics' standing: ledger class, proposal rule, or a map designed from the
  target.
- Q2-P: a physically derived embedded access or control family (dynamics and conditions both
  sourced in OI).

***

## 2. Classification table

Locations are `path:line` at `c3b5f37a` unless marked [R-off] (then at the commit in §1). Each row keeps
the result's proved scope; no row strengthens it.

| # | Result | Layer | Scope and conditions | Location | Class | Justification (premise named) |
|---|---|---|---|---|---|---|
| 1 | S ⇒ D: every finite-horizon law has a finite reversible realization | [K] | per law and horizon; the carrier and the initial law (which may correlate V and H) are built from the law | Lean `Equivalence.lean:422` (`S_imp_D`); Main:546–552 | Q2-A | The realization is chosen after the target; OA1:285–289 records that this rung "cannot fail". |
| 2 | D ⇒ Q_fb: the visible law of a given reversible realization has a fixed-basis unitary/Born representation | [K] | one fixed φ and initial law; fixed-basis reads only | `Equivalence.lean:294` (`D_imp_Qfb`); Main:552 | Q2-A | A representation of a given process's visible law; it adds no coherent instrument and is universal (Main:554: "representability alone is not the framework's discriminating content"). |
| 3 | Q_fb ⇒ S: fixed-basis Born records are finite stochastic laws | [K] | finite dimension, fixed basis | `Equivalence.lean:245` (`Qfb_imp_S`); assembly `finite_horizon_equivalence` `Equivalence.lean:462` | Q2-A | Born rule applied to records. The three implications of the cycle S⇒D⇒Q_fb⇒S are separately witnessed; rows 1–3 are kept apart (§A.34). |
| 4 | No fixed representation hosts generic action-labelled combs as the horizon grows | [W] | generic combs; per-horizon representation exists (Main:556) | Main:496, :556 | Q1-I | Premise: the intervention family is generic (arbitrary action-labelled combs); Main:496 names a "quantum-compatible subclass" as an open alternative. |
| 5 | Finite-substratum obstruction: no fixed finite realization reproduces the full prepare–measure theory of one qubit exactly | [W] + [L] (unboundedness, Main ref. [55]) | one fixed finite realization; exact; ε-level statistics unaffected | Main:558 | Q1-D + Q1-I + Q1-μ | Dynamics: total finiteness (ledger (ii), Main:724). Interface: the ordinary preparation → finite ontic system → measurement factorization, which Main:558 names as assumed. μ: the ontic law of a preparation is independent of the measurement choice, a (xiv)-type condition (C12) that inclusion does not supply. Main:558 extends the obstruction to finite shared coordination ([55]); whether that covers every embedded correlation is not checked here. |
| 6 | ε-gluing and the single controlled dynamics: one reversible map realizes a finite quantum instrument family to grid accuracy, protocols entering as an initial program register | [W] | finite family, finite K, grid G; designed map; "Quantum mechanics enters as the instrument data and as the state held in the hidden register" | Main:564, :580, :582 | Q2-F | Designed map. Reachable under one fixed map from stated initial conditions, but the map and the initial register are chosen from the target, and "the same reversible machinery can realize non-quantum finite instrument families" (Main:582). Not Q2-P. 3A:295–297 [R-off] reads it as definable only (Q2-A). |
| 7 | Operational-completion characterization: exact finite operational QM on a carrier and its composites ⇔ conditions (i)–(v) | [K] (necessity and sufficiency separately) | finite carrier; complex matrix kinematics taken as given; rules (a)–(f) | Main:562; `GeneralCarrier.lean:100` (`exactAll_iff_physical_general`), `PhysicalCharacterization.lean:301` (`physical_of_exactAll`), `GeneralCarrier.lean:93` (`exactAll_of_physical_general`) | Q2-A | Characterizes operational theories; it does not say which embedded processes satisfy (i)–(v) (3A:334–338 [R-off]; Main:66). |
| 8 | Conditions (i)–(v) independent of each other and of a fixed C1–C4 process; not supplied by bare finite OI | [K] | qubit witnesses | `GeneralCarrier.lean:160` (`oi_alone_not_qm`); `RankGapTheory.lean:702` (`five_way_minimality`); Main:562 | Q2-A | Witness theories (definable), used as non-supply results. |
| 9 | Configuration-level ceiling: the observer theory `obsTheory = permTheory Conf` has no phases, is not `DerivedOI` on any carrier, has no dense control on `Fin 2`; the substratum's stated interventions do not supply full reversible control | [K] | rule-independent (by `rfl`); `substratumGen_not_control` on the two-state carrier | OA1:408–422 (kernel lines listed there); `StructuralClosure.lean:348`; Main:80, :582, :588 | Q1-I | Premise: the configuration identification, i.e. observer operations act on configuration-indexed matrices. OA1:420–421: "An escape must change what an observer operation acts on." Rule changes stay inside (OA1 D6, :196–200). |
| 10 | Bell ceiling for a screened local completion; Corollary for the reference graph: `|S_CHSH| ≤ 2` | [W] | (i)–(iv) of the theorem; reference nearest-neighbour cubic update; wing-local setting interventions at one step; readout regions beyond the graph cone; (xiv) | Main:364–381, :414 | Q1-D + Q1-I + Q1-μ | Dynamics: ledger (x) reference graph. Interface: wing-local interventions and separated readout regions. μ: (xiv) measurement independence, "a posit about the initial condition" (Main:724). |
| 11 | PR-box behaviour is realizable when the wings share globally coupled setting-dependent hidden dynamics | [W] | unrestricted OI behaviour class | Main:360, :427 | Q2-A | A definable construction; under row 10's hypotheses it is excluded. Main:427: "Removing the screened local-intervention restrictions admits the unrestricted OI behavior class, including the PR negative control." |
| 12 | Embedded incompleteness: the observer cannot access the complete state | [W] (Definition; Lemma 2) | per moment: `V ⊊ S`, product decomposition | Main:26, :42, :48 | Q1-D (embedding) | Per-moment inaccessibility follows from the Definition. Persistence over a horizon of influential hidden content is not derived from the Definition alone (Main:26's permanence concerns degrees of freedom beyond causal reach, C14). For one rule family, on a finite ring, a held three-site block with retained history reconstructs the ring within `2(L−3)` ticks (row 27, with its hypotheses; OA-3 is not extended beyond those observers). #1143 (2026-11-09, question 1) draws the same distinction. |
| 13 | OA-1 gap 2 (D5, Lemma A): under one affine φ a stored setting acts on a carrier only by translation | [R] + [W] (one proof, re-derived twice) | gauge-derived affine class; every measure; every observer | OA1:176–195, :523; M1D:404–438; S3:56–98 | Q1-D | Property of the map (ledger (vii)), given inclusion (settings are cell content, no write outside φ, OA1:111–114). Not interface-specific. Fredkin bijections supply control, so the restriction is specific to the affine class (OA1:523). |
| 14 | OA-1 gap 1 (D2 applied to N1-S): a selected hidden carrier cannot be held with its choice record | [R] / [W] | μ-G, "held = function of present V", hidden carriers, every bijection | OA1:145–155, :522 | Q1-μ + Q1-I | Premises: μ-G (posit (iv), global case) and the held-at-use convention. Resolved classically by MP-0a (μ) or MP-0b (interface), OA1:556–564. |
| 15 | OA-1 D4: complete in-V records exclude hidden influence on V | [R] / [W] | (a) any stationary law: deterministic on support; (b) μ-G: no hidden influence | OA1:162–175 | Q1-μ + Q1-I | Premises: complete in-V records (interface) and μ-G. D4(c): "the blank-memory cost of D3 (MP-0a)". |
| 16 | OA-1 D8 (candidate, unreviewed): inert partial records show no memory at the orders held | [R] (candidate) | μ-G only | OA1:210–238 | Q1-μ + Q1-I | As row 15, for partial windows; marked unreviewed in OA1 §6. |
| 17 | `𝔖_F`: a reversible Fredkin computer with MP-0a passes N1–N4 and fails the qubit tier under the configuration interface | [W] on [K] | configuration-level interface only | OA1:546–550 | Q2-F | Designed map. One fixed designed bijection from a stated initial law (MP-0a). The failure is Q1-I (row 9's identification); not shown for every observer-relative representation (OA1:548–550). |
| 18 | OA-2 N0, Lemma 0, Proposition A: on laws over configurations a bijection acts stochastically; reversible actions are permutations | [R] / [W] | E1/E2 with a fixed lift (or strong lumpability); every φ, μ | OA2:199–223 | Q1-I | Premise: the emergent state space is a law over configurations or record classes with a fixed lift (state-space choice). |
| 19 | OA-2 Theorem C: at a fixed finite carrier, reversible trace-preserving emergent operations form a finite group | [R] / [W] | every rule, μ, interface; finite S | OA2:332–376 | Q1-D | Premise: finiteness of the carrier (ledger (ii)). |
| 20 | OA-2 N2.3, `𝔊_K`: an exact preparation-contextual gbit at each bounded horizon | [R] / [W] | designed non-affine φ (posit); MP-0a ready cells; μ-G bath; conveyors longer than the horizon; C-PM′/C-PM | OA2:379–490, :766–773 | Q2-F | Designed map. Reachable under one fixed designed bijection from a stated initial law. Not Q2-P: φ is outside ledger (vii), "a control, not an OI result" (OA2:483–484). Shows G0, G1, G3 do not separate classical from quantum at bounded horizon. |
| 21 | OA-2 Theorem E(b): the prepare–measure fragment is simplex-embeddable | [R] / [W] on [R] | (H1) affine; H-AR; (H3) no supplied control; (H4) nested records; (xiv); (SP) | OA2:522–576 | Q1-D + Q1-I + Q1-μ | (H1): dynamics. (H3): follows from inclusion. H-AR: an observer restriction (OA2:182–196) not implied by the Definition. (H4): record convention (MP-0b type). (xiv) and (SP): conditions on the initial law and its reachable record laws. Without (SP), only preparation noncontextuality (OA2:542). |
| 22 | OA-2 Corollary E1: under (H4), (SP), (xiv), a G3 escape needs settings that do not merely translate the joint held record, for any rule | [R] / [W] + [RW] | E3, prepare–measure G3 | OA2:577–605; label [W] + [RW] at OA2:874 | Q1-I + Q1-μ | Necessity statement; premises (H4), (SP), (xiv). Open exits listed at OA2:599–604: non-additive observers, non-nested reads, non-spanning reachable laws. |
| 23 | OA-2 Proposition B(ii)(⇒) under (CVX) | [R] / [W] + [RW] (reviewer-supplied steps) | available effects closed under mixing | OA2:244–300, :747 | Q2-A | A mathematical lemma about models; (CVX) is a closure hypothesis on effects. |
| 24 | OA-2 class N, one cell, native Z/X reads: preparation- and measurement-noncontextual | [R] / [W] + [RW] on [R] | premises at q = 2 only; P1, P2; H-LIFT | OA2:645–673 | Q1-I | Premises: native Z/X read set, P1 terminal registration, P2 half-known ready cells, H-LIFT. |
| 25 | OA-2 N2.6: G3 for admissible non-affine rules | open | `G_SM`, `G_σ`; each a Layer-0 revision | OA2:674–694, :775–779 | — | Open; not classified. |
| 26 | OA-3 N1: minacc-1's gate cancellation transfers to `G_SM` and defeats Lemma Q's protection | [R] / [W] | P1, P2, H-PREP's known-1 supply | OA3:159–222 | Q1-I | Premises P1, P2, H-PREP (interface posits). Result: it supplies access, not restriction (OA3:213–219). |
| 27 | OA-3 Lemma OBS: three consecutive held sites with retained history determine a finite ring of L sites within `2(L−3)` ticks (with `v_a(0)`; `2(L−2)` without it, OA3:228–232) | [R] / [W] + [RW] | SM's ring rule (SM:112) at any q, class N, permutive edge; H-AR; retained history; finite ring; measure-free | OA3:223–293 | Q1-D + Q1-I | Dynamics: a ring rule permutive in its extreme left argument (`G_SM` is a proposal, not OI's rule). Interface: held block, retained history. Scoped to its finite-ring observers; no extension to cubic-lattice observers (c.6848268369). |
| 28 | OA-3 Theorem S: for those observers, the prepare–measure fragment of `G_SM` is a simplex | [R] / [W] + [RW] | row 27 plus MP-0b or (V-ii-H), heralds, C-PM, stage ≥ `2(L−2)`, (PT) | OA3:294–391 | Q1-D + Q1-I + Q1-μ | (PT) is a condition on the initial law's support. Not an impossibility result for `G_SM` (OA3:388–391); horizons `T ≪ L` not covered (OA3:383–386). |
| 29 | OA-3 N4: E(b) holds with (H4) replaced by (V-ii-H); under (V-ii-U) a 3-cell shift shows a gbit | [R] / [W] + [RW] | affine class, (H1), H-AR, (H3), (xiv), (SP) | OA3:392–497 | Q1-I | Premise: the effect class. The (V-ii-U) gbit is a convention artefact present for trivial dynamics (Q2-A, does not count). Herald typing is an open interface premise (OA3:124–127, :410–416, :660–667). |
| 30 | W1-1: W1 is an additional physical assumption, not a derived result | [R] / [W] | candidate mechanisms tested, list not proven exhaustive; consistency axis | W11:29, :56; W1-1 `STATUS.md`:48–59 | Q1-D | Premises concern the hidden-sector entropy–energy slope; no observer-interface premise. No bearing on Q3 or Q4 (as 3A:1047–1049 [R-off] also finds). |
| 31 | TUNE-1 Lemma A-T: R-lin record laws are coset-uniform; labels act by translation | [R] / [W] | (a), (b) law-free; (c), (d) need a coset-uniform law | S3:56–98 | Q1-D (+ Q1-μ for (c), (d)) | (a), (b): property of R-lin; (c): uniform law. |
| 32 | TUNE-1 FC-1, FC-2 | [R] / [W] | R-lin, coset-uniform law, unheralded (FC-1) or non-adaptive (FC-2) witnesses | S3:122–194; corrected S4:303–345 | Q1-D + Q1-μ + Q1-I | Interface premise: the witness class (unheralded, non-adaptive). |
| 33 | TUNE-1 NL-C, NL-C′: an interface with `|C| ≤ c` fails Q6′(i) at every `ε < sin(π/(q^{2c}+1))/8`; meeting Q6′ needs `|C| ≥ ½ log_q((1−4ε)/(4ε))` | [R] / [W] | any rule, law, mode, carrier; heralded and adaptive witnesses included | S4:423–475 | Q1-I | Premises: one gate is one round with one label (S4:697–698), labels are configurations of a cell set `C` (the menu `(V × V)^C`, S4:432–434), the declared target's gate family over every θ with Lüders reads (S4:452–453), the target's separation length `L` with `K ≥ L + 1` and Q6′(i) with its credit on `𝒯_L` (S4:425–427, :454), and that an identified test's labels do not depend on the preparation's records (final B1.1, S4:456). It uses no rule, law or carrier (S4:457–458). The interactions of that form: every interface whose per-round gate setting ranges over configurations of a cell set bounded uniformly in ε, whether the set is designated or emergent. Outside it: gates over several rounds, settings not encoded as cell configurations, control regions growing with 1/ε (3A:433–439 [R-off] reads the same). |
| 34 | TUNE-1 W-nl, Lemma M (one-time pad); NL-A, NL-P open | [R] / [W] | R-nl under H-nl (unadopted) | S4:86–258, :403, :497 | Q1-D | Dynamics under an unadopted rule; NL-P is the absence of a construction. |
| 35 | TUNE-1 L4 escape audit, exact form | [R] / [W] | R-lin and R-nl on `𝓛_fin`; approximate form open | S3:276–289; S4:519–523 | Q1-I | Premise: an injective complete orthogonal frame with H-LIFT (identification). |
| 36 | TUNE-1 Step 3A: no candidate (A–D) is specified; A and C conditionally classical-only via E(b) with (SP), preparation-noncontextual without | [R-off] / [W] | 3A's schema and readings | 3A:210–218, :896–931 | Q2: none | No member exhibited, so no construction at any level; the specification gap is not a quantum failure (3A:907–908). |
| 37 | TUNE-1 Step 3A F-3A-2: run repetition is used but not stated | [R-off] / [W] | every candidate | 3A:969–986 | Q1-μ | An unstated condition on the initial and refresh law (separate from the time-zero law H-μ). |
| 38 | MECH-1 Theorem W, Proposition C: at odd q, in frame R-W, every protocol of the native class acts as a stabilizer instrument; no quarter phase; an epistricted noncontextual model reproduces the reachable fragment | [R] / [W] | odd prime q; native class N (+ NNB, P3-armed) | M1D:465–513, :751–796 | Q1-D + Q1-I | Dynamics: native affine symplectic class. Interface: the frame R-W, a representation chosen once (M1D:252–292). |
| 39 | MECH-1 Theorem T, Proposition T′; missing premise M1 | [R] / [W] | odd q, R-W | M1D:797–894, :938–1051 | Q1-D + Q1-I | CP in the frame forces affine, so in-world setting selection fails; M1 is named, not adopted. |
| 40 | MECH-2 Lemma F, Theorem U2: every encoded unitary channel of a fixed bijection under R1^⊗n lies in `A_4 ≀ S_n` | [R] / [W] | q = 2; H-LIFT; frame R1 | M2D:325–347, :404–482 | Q1-I | Premise: the frame identification R1 with H-LIFT; holds for every coupling rule. |
| 41 | MECH-2 Theorem NC: an injective identification with spanning reads gives a noncontextual model, whatever the dynamics | [R] / [W] | Lemma F's hypotheses; spanning certification | M2D:485–541 | Q1-I | Premise: injective identification and spanning-read certification (CERT). Missing premise named: M-INACC (M2D:114–117, :832–). |
| 42 | MECH-2 P★: a non-stabilizer encoded state heralded under `G_SM` in a C-CP-failing instrument | [R] / [W] | q = 2; R1-relative | M2D:80–92 | Q2-F | Proposal rule (`G_SM`). Reachable under one fixed (proposal) rule from stated laws; frame-relative; the instrument fails C-CP. |
| 43 | BSEL-2 B4′: gauge relatedness G against complete-record operational equivalence O_C, per access tuple C0–C2 | [R] / [W] (hand) | stated lifts; ∀U; fixed `a₀`; access tuples | B4P:541–620 | Q2-A (Q1-I for the O⇒G failures) | Statements about mathematical lifts; every access tuple is a SOURCING-GAP (B4P:610–620). The O⇒G failures are identifiability limits under posited interfaces. |
| 44 | #1139 Q2A: O⇒G fails for C0, C2-ch, C2-sel at `|V| = 2`, `|A| ≥ 2`, constant lifts (outside PPer) | [R] / [E] | as stated | Q2A:274–296 | Q2-A (Q1-I) | As row 43; "a native separation" is not established (Q2A:366–370). |
| 45 | M-1: the same failure in PPer, alternating-W lifts | [R] / [E] | `|V| = 2`, `|A| ≥ 2`; PPer | MR1:316–343, :370–375 | Q2-A (Q1-I) | Physical availability of P-conf, Acc₂, Rd, H-comp, Rst-ch, Rst-sel and the coherent preparation are SOURCING-GAPs (MR1:371–372). |
| 46 | OICORE-1 Lemma M: a downward-closed predicate satisfied by a core-realizer forces neither exact nor dense control on `Fin 2` | [R-off] (its own label: A over K) | `FiniteOperationalTheory (Fin 2)` | OC1:218–246 | Q1-I | Premise: the restriction class (downward-closed predicates on the operational theory). |
| 47 | OICORE-1 §5: no quantum-selecting property follows from any candidate other than CTRL; open routes ACC-U, ACC-R4/M-INACC, selection on `(φ, μ_H)` | [R-off] | twelve candidate rows | OC1:322–391 | Q1-I (negative part) | Its candidates are restrictions on T; CTRL is the target's own resource (OC1:347–351). The open routes are Q3 inputs. |

Rows: 47 (two of them, 25 and 36, record the absence of a result).

***

## 3. Q3: the interaction class

### 3.1 What OI's stated premises fix

- **φ.** Ledger items (vii) affine/linear update, (xiii) second-order form, (x) nearest-neighbour range,
  with (viii)–(xi) for spatial structure (Main:724). The settings of such a rule act on the configuration by translation, for every measure (row
  13); held records are translated only for additive (H-AR) observers (OA2:601–602).
- **μ.** Ledger item (iv): the maximal-entropy measure "compatible with the observer's records",
  whose global case is μ-G (OA1:100–109; Main:54). The per-orbit measure μ-O is derived (Main:54, :60).
  A realization may carry a structured prior `μ_H` "as part of the realization datum"; "the counting
  measure is the default, not a constraint on representations" (Main:58).
- **Embedding.** The Definition: `V ⊊ S`, finitely many distinguishable states, coupled through φ
  (Main:42); the product decomposition (Main:48).
- **Interface.** Statement (i), ontological inclusion, follows from the Definition (3A:263–266 [R-off]):
  every operation is implemented by φ, so there is no write access outside φ (OA1:111–114). What the
  observer holds at a time is a function of its present configuration (OA1:112–114). Heralds held at
  use time are an open typing choice against ensemble conditioning (OA3:410–416, :660–667).

### 3.2 A reading of OA-1 D2 under held-at-use typing [W, REC-1; unreviewed; ELABORATING of OA-1 D2, D4]

1. Under μ-G the law at every time is uniform on `C_V × C_H` (OA1:145–150; Main:58). The same holds for
   any subsystem `W` (a set of sites, ledger (viii)) of the product carrier: `W_t` is uniform on `C_W` at every t.
2. Hence, for any fixed functions `f, g` of `W`'s present configuration, the joint law of
   `(f(W_t), g(W_t))` is the uniform pushforward, the same for every bijection φ and every t.
3. The dynamics therefore enters the statistics an embedded observer holds at one time only through
   which present functions are records of earlier events. Under μ-G such records carry OA-1's cost:
   complete records exclude hidden influence on the recording subsystem (D4(b), OA1:162–175, applied
   to `W = V ∪ R`, with `R` record cells in the sense of OA-1 D8, OA1:211), partial inert records show no held-order memory (D8, a candidate), and D4(c) names
   the cost as blank memory, MP-0a (OA1:171–173).
4. So, under μ-G with held-at-use typing, no held one-time statistic of fixed functions depends on
   φ. A φ-dependent held statistic needs either an initial or boundary law other than μ-G (MP-0a,
   OA1:556–558, is the form the corpus names; any structured realization law, Main:58, :97, also
   qualifies) or a typing other than held-at-use (the retention convention MP-0b, or heralds read
   as ensemble conditionings, C7). Read as what an embedded observer holds at time `K` under μ-G
   with held-at-use typing, the finite-horizon law `P(x_0, …, x_K)` of Main:546 presupposes one of
   these.

Scope: μ-G only. Under μ-O and μ-R, D2 is not established (OA1:258, :262), and nothing here applies.
Assumption-watch marker AW-REC-1: a statement about what an embedded observer records under μ-G names
its retention source, MP-0a or MP-0b. This is a reading of [R] statements, not a result.

### 3.3 Candidate restrictions

| # | Restriction | Filters | Premise status | Reason |
|---|---|---|---|---|
| C1 | Ledger rule class (affine/linear, second-order, nearest-neighbour) | φ | follows from stated premises | Ledger (vii), (x), (xiii), Main:724. Consequence: settings act on the configuration by translation only (row 13). |
| C2 | Non-affine rule (MP-1, `G_SM`, `G_σ`, R-nl under H-nl) | φ | new §A.29 premise | A Layer-0 revision of (vii) and A5 (OA1:565–584; OA2:674–676). |
| C3 | One law for all operations (FIX) | φ | follows from stated premises | Main:44 (composition of the evolution); for interventions an interpretation (OC1:187 [R-off]), which OC1:310, :319 calls the smallest faithful strengthening. |
| C4 | No write access outside φ; settings are configuration content | interface | follows from stated premises | Statement (i) from the Definition (Main:42); exchange-mode H-write is the alternative and is a new premise (3A:279–282, :413–420 [R-off]). |
| C5 | Held = a function of the present configuration of V | interface | convention (OA1:112–113); the Definition (Main:42) is consistent with it [W, REC-1] but does not fix it, and MP-0b is the alternative (C6) | Under μ-G its consequence is §3.2. |
| C6 | Retained visible history (MP-0b; (H4) nested records) | interface | undetermined | OA-1 lists it as a missing interface convention (OA1:563–564); 3A:501 [R-off] treats it as imported. Under μ-G and statement (i), §3.2 ties it to MP-0a. |
| C7 | Herald typing: held at use time vs ensemble conditioning | interface | undetermined | Open interface premise (OA3:124–127, :628). Ensemble conditioning is an analyst's conditioning, not a held record. |
| C8 | μ-G (global counting measure) | μ | the global special case of posit (iv), with no record constraint; not the unique law (iv) selects for an observer with records (μ-R, C9) | OA1:103–105. With C5, held statistics of fixed functions are φ-independent (§3.2). |
| C9 | μ-R (record-compatible maximal entropy) | μ | follows from stated premises (posit (iv)), under-specified | It presupposes "the observer's records", whose formation is the question (§3.2). |
| C10 | μ-O (uniform on the actual orbit) | μ | follows (derived) | Main:54, :60. (xiv) may fail on the orbit (OA1:264). |
| C11 | Boundary condition with designated known (blank or ready) cells, uniform elsewhere (MP-0a) | μ | new §A.29 premise if selected; admitted as a realization datum if only quantified over | OA1:556–562 ("Hard to vary? No. It carries no quantum content"); Main:58 admits structured priors; selection on `(φ, μ_H)` is open (OC1:359–363 [R-off]). |
| C12 | (xiv) measurement independence | μ | a ledger posit for the Bell analysis (Main:724: "a posit about the initial condition, not derived"); its time-zero extension is the unadopted H-μ; its extension to every admitted procedure, feedback and herald conditioning included, is carried in §4 as the explicit hypothesis H-xiv | Main:724 ("(xiv) enters only the Bell analysis"); H-μ is stated at P:145 (`TUNE-1-STEP2-PROPOSAL.md` on `main`). It is not a consequence of C11 or of φ: the procedure class admits settings written by φ from earlier records and heralded branches (OA2:102–104); a deterministic update can make a later setting depend on an earlier record of the response-relevant variable, and conditioning can create correlation (#1268 review 5890763675). |
| C13 | Additive, cell-aligned observers (H-AR) | embedding | undetermined | A restriction of the observer class not implied by the Definition (OA2:182–196). Using it as a scope adopts nothing. |
| C14 | Persistent inaccessibility from the causal cone | embedding + φ | follows from stated premises (the causal cone of Main §3.3, under (viii) and (ix), Main:724) | [W, REC-1] What lies outside the cone over the horizon also cannot influence the observer's records within it, so the cone alone gives no persistent inaccessibility of influential information; Lemma M (one-time pad, S4:94–101) gives masking for one tick, given previous components uniform and independent of the rest. |
| C15 | M-INACC: an ontic functional the rule uses that no permitted procedure accesses, for a reason not chosen to reach the target | interface + embedding | new §A.29 premise | M2D:114–117, :832; OC1:190, :314 [R-off] ("under-specified as a schema"). |
| C16 | ACC-U: accessible but uncertifiable functionals (removal of spanning certification) | interface | removal of an imported assumption, not a premise; open | OC1:191, :315, :355–358 [R-off]; draft-conditionally, one instance (ARP-3 F0) has an exact noncontextual model (OC1:258 [R-off]). |
| C17 | Terminal registration below recurrence (RET-s, P1) | interface | new premise | OC1:194, :313 [R-off] ("the smallest crisp new hypothesis"). |
| C18 | Bounded per-round control menu (the NL-C form) | interface | not a restriction to adopt; its consequence is known | Any class containing only interfaces of that form fails Q6′(i) for TUNE-1's declared one-qubit target at every `ε < ε_C(c)`, for a menu bound `c` uniform over the class (row 33). |

**Answer to Q3.** A class can be stated from OI's premises without naming target statistics:
φ from C1, μ from C8 or C10, embedding from the Definition, interface from C4 and the convention C5. It names no
quantum object. Under C8 with C5 and held-at-use typing, its held statistics of fixed functions do not
depend on φ (§3.2); a dynamics-dependent operational theory needs a law other than C8 (C11 is the form named in
the corpus; C9, C10 or another structured μ_H also qualifies) or a typing other than C5 (C6, or C7's
ensemble reading) [W, REC-1; unreviewed], and neither is selected by the stated premises. Under C10 and C9 its classification is open. Every
candidate that is a new premise (C2, C11 as selected, C15, C17) is a §A.29 matter (§A.45 rule 5).

***

## 4. Q4: the next obligation

The obligation below quantifies over boundary conditions of the C11 form instead of selecting one,
so it adopts no premise. Its classical outcome bears on OI, under the hypothesis H-xiv, for every boundary condition of that form;
its non-classical outcomes would give operations reachable under the fixed native dynamics from a
stated boundary condition (Q2-F), whose physical bearing needs the selection named at the end of this
section.

**OBL-SP (non-spanning case of OA-2 Theorem E(b) for the native rule class).**

*Statement.* Let φ be a rule of the gauge-derived affine class (ledger (vii); R-lin with (xiii)) on a
finite carrier. Let the initial law range over the family `D_0`: designated cells at known values,
every other cell uniform and independent (the form of OA-1 MP-0a, OA1:556–558; `D_0` contains μ-G as
the case with no designated cell). Take observers satisfying H-AR, no write outside φ ((H3)),
records as in (H4) or in the (V-ii-H) effect class (OA3:460–476), heralds typed as held at use with
records formed inside `S`, and the closure-defined prepare–measure fragment under C-PM (OA2:88–125).
Assume the hypothesis H-xiv: (xiv)'s condition, the response-relevant pre-setting variable
uncorrelated with the settings (Main:724), holds for every admitted setting and herald procedure,
including settings written by φ from earlier records (feedback) and postselected herald branches
(OA2:102–104). H-xiv is ledger (xiv) extended in scope from the Bell analysis to every admitted
procedure. It is related to the unadopted H-μ (C12; P:145), a time-zero independence that does not by itself
cover settings generated by feedback or correlations created by herald conditioning; it is a
hypothesis of the question, not a consequence of `D_0` or
of φ. When (SP) fails, is that fragment simplex-embeddable?

*Why open.* OA-2 proves preparation noncontextuality without (SP) and states the
affine-class question at OA2:779 ("is the affine class itself classical at E3 without (H4) or
(SP)?"); OA-3 N4 removes (H4) under (V-ii-H) and states "The affine class at E3 without (SP) stays open" (OA3:494). For unheralded preparations under a law of `D_0`, each label sequence's record law is uniform on
one coset of a label-independent subgroup `S_m` (Lemma A-T (c), S3:56–98, with `r_O` the
designated values; S3:107). For heralds on a complete prefix, the continuation law is a mixture
of uniform laws on cosets of one fixed subgroup `S₀` (S3:198–201), and S3:206–207 states that "The
restricted record theory is a classical simplex theory whose extreme points the labels translate"
[R]. Raw (SP) therefore fails whenever the relevant subgroup is nontrivial. A model on the coset
space may still restore measurement noncontextuality, so that "(SP) open" may resolve cheaply in
either direction (3A:613–617 [R-off], an unverified reviewer remark). OBL-SP's first step is that
check (P0 below). If the coset model is a simplex embedding for the whole class, OBL-SP closes
as O-C, and Q4 is re-run on the remaining items.

*What P0 may settle, and why smallest.*
- A P0 pass, which needs the whole operational witness of P0 and not the law form alone, may close
  OBL-SP as O-C for the fragment of unheralded preparations and of heralds on prefixes of one length: S3:206–207 [R] states that the record theory of continuation laws under R-lin with a
  coset-uniform law, in initial-condition mode, after heralds on a complete prefix, is a classical
  simplex theory (it is not stated for the E3 prepare–measure fragment under C-PM), and the r1
  review sketches a coset-space simplex embedding (unreviewed; not used here as a
  result). This record does not carry out P0. If the coset form holds there but a reachability,
  accessible-effect or equivalence check fails or is unestablished, that fragment is O-U (P0).
- If P0 passes on that fragment, OBL-SP's open content is the set of preparations that P0 lists as
  outside the coset form: heralds on prefixes of several lengths, whose cosets refine as the prefix
  grows, and heralds that cannot be composed because, under held-at-use typing, an earlier herald is
  available only if a record of it is formed inside `S` (C6, C7; OA3:410–416, :474–475). This
  residual is the preparation-side route of OA-2 N2.1 (restricted preparations, OA2:75, :313–315)
  inside the native class. Its answer still separates O-C from the non-classical outcomes. Its
  bearing is conditional on the herald typing, which the stated premises do not fix (C7).
- Comparison with AW-OA2-1, non-additive observers (OA2:601–602, :626). It needs no new physical
  premise either: H-AR is a restriction the Definition does not impose (OA2:182–196), so dropping it
  removes a restriction and adds none. It is the read-side route of N2.1 (OA2:75) [W, REC-1]. The two classes
  are incomparable: OBL-SP drops (SP) and keeps H-AR; AW-OA2-1 drops H-AR and keeps (SP). OBL-SP is
  placed first because it has a cheapest decisive step (P0) whose inputs are [R] statements on
  `main` (S3:56–98, :196–207; OA2:522–576), and because a P0 pass narrows it to the herald-retention
  residual, a subset of OBL-SP's own preparations. The ordering is by cost, not by the size of the
  two classes, which are not nested. It is not placed first
  for an expected non-classical answer: S3:206–207 points to O-C on the main fragment.
- Ordering rule, fixed in advance. If P0 passes for the whole class under the fixed typing (the
  whole operational witness validated, P0), OBL-SP closes as O-C, subject to P4 (O-V if (v) fails), and the next
  obligation is AW-OA2-1 with the same φ, `D_0`, (H3), record class, herald typing, C-PM, H-xiv and
  (SP) and a non-additive read map; no premise is adopted, and H-xiv is carried as a hypothesis.
  If P0 lists preparations outside the coset form and the in-form preparations pass the
  operational witness, OBL-SP continues on the listed preparations alone; in-form preparations whose
  checks fail or are unestablished are O-U as well (P0). If the coset
  form holds but an operational check fails or is unestablished, the outcome is O-U (P0), and Q4 is
  not handed to AW-OA2-1 on that basis. In none of these cases does Q4 stop at a premise; the herald typing (C7) is carried as a scope hypothesis.
- The remaining open items are larger or need a premise: unbounded horizons (AW-OA2-2) enlarge the
  protocol class; non-affine rules (OA2:775–778) need C2; TUNE-1's T1 needs a specified family and
  Step 3B; selection on `(φ, μ_H)` needs a selection principle.

*Prerequisites (fixed before any attempt).*
- P0. Cheapest decisive step: decide whether, for every instance in the class, the reachable laws
  of `Z₀` are mixtures of uniform laws on the cosets of one subgroup, each coset reachable and
  determined by the held record, so that the coset-space model is a simplex embedding. Record
  which preparations, if any, fall outside that form, such as heralds that cannot be composed
  under the fixed typing. Once the in-form preparations pass the operational witness, only those listed preparations
  carry OBL-SP's open content. P0 is posed under H-xiv.
  Implementation checks (not results): the coset-space simplex witness uses accessible indicator
  effects in the C-PM class, excluding reads of preparation labels; that a coset is "determined by
  the held record" is backed by a valid operational effect in that class and an operational
  equivalence test; O-V and the controls of P4 (contextual, quantum and supra-quantum) are kept.
  P0 has three outcomes.
  - Pass, only when the entire operational simplex-embedding witness is validated for the whole
    class: a common coset-mixture description of the reachable laws, every needed coset reachable,
    each coset's identity operationally determined by held records, and the C-PM accessible
    indicator and equivalence effects exhibited. The law form alone is not a pass. A pass may close
    OBL-SP as O-C, subject to P4, including O-V.
  - Out of form: preparations outside the coset form are exhibited. They are listed for the
    residual investigation, and OBL-SP continues on them.
  - Unresolved: the coset form holds, but a reachability, accessible-effect or equivalence check
    fails or is unestablished. That failure is recorded separately, and the outcome is O-U unless an
    independent classicality proof or a contextual counterexample is supplied. It is never reported
    as O-C from the coset form alone, and never as a non-classical witness.
- P1. Definitions of the fragment and of simplex-embeddability: OA-2 §1.0–1.4 and G3 (OA2:150–170),
  with every procedure folded into a preparation or a measurement.
- P2. The quantum-model criterion for a non-classical outcome: a finite-dimensional set of density
  operators and effects reproducing all statistics of the fragment, with every operational
  equivalence of preparations mapped to equality of density operators and every operational
  equivalence of effects mapped to equality of effect operators. Stated before the attempt, used only to label outcomes.
- P3. Inputs, each with its hypotheses carried, each re-derived or independently validated in
  the unit before it is used as a premise (§A.46 item 7): OA-2 Theorem E(a), E(b) steps 1–4 and Proposition B(i),
  B(ii)(⇐) (OA2:244–300, :522–576) [R]; OA-3 N4.3 [R]; Lemma A-T (c) and Node L5.4 (S3:56–98,
  :196–207) [R].
- P4. Controls, with expected classifications preregistered as a rule: (i) instances that satisfy (SP)
  are classified simplex-embeddable (preservation of E(b)); (ii) OA-2's N2.1 non-spanning
  counterexample (OA2:296–315, :542–544) is classified non-simplex-embeddable by the same classifier;
  (iii) the (V-ii-U) shift artefact (OA3:418–459) is excluded by the fixed herald typing; (iv) `𝔊_K`
  (row 20), outside the class, is classified non-simplex-embeddable; (v) non-vacuity: at least one
  instance of the class satisfying H-xiv, with records formed inside `S` and a nontrivial fragment, is exhibited, or
  O-V is reported; (vi) P2's label is checked on a known quantum-realizable contextual fragment
  (labelled O-Q) and on a fragment with no quantum model under P2 (labelled O-SQ), both fixed before
  the attempt.
- P5. Owner authorization of a paper-only unit; none exists.

*Rival outcomes (fixed in advance).*
- O-C (classical): simplex-embeddable for every rule of the class, every law in `D_0`, every H-AR
  observer and every finite horizon. Bearing: under (H3), the record class ((H4) or (V-ii-H)),
  held-at-use herald typing with records formed inside `S`, C-PM and H-xiv, no boundary condition of the
  `D_0` form gives a cell-aligned observer non-classical prepare–measure structure under the native
  rule; the remaining routes are named: non-additive observers (AW-OA2-1), laws outside `D_0`,
  procedures for which H-xiv fails, other herald typings and record classes (C6, C7), and C2.
- O-Q (non-classical, quantum-realizable): some instance is not simplex-embeddable and has a quantum
  model in the sense of P2.
- O-SQ (non-classical, not quantum-realizable): some instance is not simplex-embeddable and has no
  quantum model in the sense of P2 (a candidate shape is the dual gbit of OA-2 N2.1, OA2:313–315,
  whose lack of a quantum model in the sense of P2 is not established here).
- O-Q and O-SQ are not exclusive; both are reported if both occur.
- O-V (vacuous): no instance of the class satisfies H-xiv and has a nontrivial prepare–measure fragment with records
  formed inside `S` (P4(v)). Reported as such and not as O-C.
- O-U: undecided at the attempted scope; reported as such and not as any of the above.

*Why no new physical premise.* φ is fixed by ledger posits. The initial law is quantified over `D_0`,
which Main:58 admits as realization data; nothing in `D_0` is selected. H-AR, (H4) or (V-ii-H), and the
herald typing are hypotheses of the question, carried into its conclusion as scope. (H3) follows from
statement (i). (xiv) is a ledger posit, "a posit about the initial condition, not derived" (Main:724),
stated for the Bell analysis; OBL-SP carries its extension to every admitted setting and herald
procedure as the hypothesis H-xiv (related to, and not reduced to, the unadopted H-μ, C12). "No new physical premise" holds only in
this sense: nothing is adopted, and H-xiv is carried into every conclusion as a hypothesis, not
derived from `D_0` or from φ.

*Why not defined by the quantum target.* Membership in the class is fixed by φ, `D_0`, the observer
class and the record class. The criterion is simplex-embeddability, which is target-neutral. Quantum
realizability enters only as P2's label on a non-classical outcome.

*What an O-Q or O-SQ outcome would still need before it bears physically on OI.* A selection of the
boundary condition from `D_0` (MP-0a type), which is OICORE-1's open existence route, "a selection
principle on the realization data `(φ, μ_H)` native to OI" (OC1:359–363 [R-off]). That premise is
named here and not adopted; OBL-SP does not need it.

***

## 5. Proposed Issue-priority changes (proposals for the owner; none applied)

Priority changes are unauthorized (c.6850732002). Each item below is a proposal only.

1. **OBL-SP.** Record it as an obligation with its own accountable Issue (or as a row of #1169's
   block), proposed tier: supporting (its outcome decides, for H-AR observers, `D_0` laws, the
   record class and herald typing stated in §4, whether the native rule class can host
   non-classical prepare–measure structure; P0 may settle it cheaply (§4), and S3:206–207 points to
   O-C on its main fragment, so "high" is not proposed); readiness: ready for a paper-only unit;
   authorization: not authorized.
2. **#1236 (TUNE-1).** Proposed prerequisite edge: Step 3B's candidates A and C after OBL-SP, since
   their conditional classification rests on (SP) (3A:212–214 [R-off]). Step 3B stays unauthorized.
3. **AW-OA2-1 (non-additive observers).** Proposed as the next item after OBL-SP's P0 (the ordering
   rule of §4), tier: supporting; prerequisite: P0.
4. **Selection on `(φ, μ_H)` / MP-0a.** Proposed as a tracked premise question, tier: exploratory,
   readiness: blocked on OBL-SP (only an O-Q or O-SQ outcome makes it decisive).
5. **#1143.** Proposed note against question 2 of the 2026-11-09 reformulation: the filters are
   tabulated in §3.3; against question 1: per-moment inaccessibility is not persistence (rows 12, 27;
   §3.2).
6. **#1214 and #1267.** Proposed owner decision on landing their records, since rows 36, 37, 46, 47
   and the [R-off] citations of §3 rest on them (§6 below). This is an integration question, not a
   priority change.
7. **#1245 (W1-1).** No change proposed; no bearing found.

***

## 6. §A.42 item 8: references to content off `main`

| Reference | Used where | Classification |
|---|---|---|
| 3A (`TUNE-1-STEP3A-r3.md`, blob `7bbec04d`, at `8228b3c2`, PR #1267): the Q1/Q2 terms (§1) | §1 | Support off `main` (a gap until landed). |
| 3A, rows 36 and 37 | rows 36, 37 | Support off `main` (a gap until landed). |
| 3A:263–266, statement (i) | §3.1 | Support off `main` for the formulation of statement (i); the Definition it reads is Main:42 on `main`. |
| 3A:501, the record convention typed as imported | C6 | Support off `main` for C6's "undetermined" status, which rests on OA1:563–564 on `main` against 3A:501. |
| 3A:279–282, :413–420 (H-write) | C4 | Support on `main` for C4 itself (Main:42; OA1:111–114); 3A is cited for the exchange-mode alternative, which rests on TUNE-1's proposal on `main` (P:155–167, as 3A cites). |
| 3A:334–338, :433–439, :1047–1049 | rows 7, 33, 30 | Support on `main` (Main:562, :66; S4:423–475; W11); 3A is cited as agreeing. |
| 3A:295–297 (row 6 read as definable only) | row 6 | Provenance: a contrary reading recorded; row 6's classification does not rest on it. |
| 3A:212–214 | §5 item 2 | Provenance: a proposal's rationale, not a claim. |
| 3A:613–617 (reviewer's (SP) remark) | §4 | Provenance: the (SP) point rests on S3:56–98, :196–207 on `main`; P0 is the check the remark names, and no conclusion rests on the remark. |
| `TUNE-1-STEP3A-REVIEW.md` (blob `49a5d52a`, at `8228b3c2`) | not used | Provenance. |
| S3:196–207 (TUNE-1 Node L5.4) | §4 | Support on `main`, as [R]. |
| P:145 (`TUNE-1-STEP2-PROPOSAL.md`, H-μ) | C12 | Support on `main`, as [R]. |
| OC1 (`OICORE-1.md`, blob `83188952`, at `77226128`, PR #1214): rows 46, 47 | rows 46, 47 | Support off `main` (a gap until landed). |
| OC1:187, :310, :319 | C3 | Support off `main` for the attribution "smallest faithful strengthening"; C3's status rests on Main:44 on `main`. |
| OC1:191, :258, :315, :355–358 | C16 | Support off `main` (a gap until landed). |
| OC1:194, :313 | C17 | Support off `main` (a gap until landed). |
| OC1:190, :314 | C15 | Support on `main` for C15's status (M2D:114–117, :832); OC1 is cited as agreeing. |
| OC1:359–363 | C11; §4 last paragraph | Provenance: the premise is named and not used; OBL-SP does not rest on it. C11's status rests on OA1:556–562 and Main:58 on `main`. |
| Commits `2d064a71`, `62bdc2cf`, `080cd2be` | pin checks (§1) | Support on `main`: ancestors of `c3b5f37a`. |
| PRs #1265, #1237, #1191, #1195, #1139, #1151 | input identification | Support on `main`: merged (merge commits `c3b5f37a`, `c03a5764`, `1287748d`, `9facdf03`, `c987b890`, `f810f5ee`). |
| #1169 c.6850732002, c.6848080209, c.6848268369 | authority (§1) | Governance provenance, quoted. |
| #1236 c.6847314661 | framing (§1) | Provenance. |
| #1143 body (2026-11-09 reformulation) | framing; row 12; §5 item 5 | Provenance. |
| #1169 comments of 2026-11-12 (c.6834439001 to c.6835700002) | read for status of the OA records | Provenance; the status used is the one in each `STATUS.md` on `main`. |
| Draft PR #1268, r1 at `d7f7aac1`, and its r1 review | revision line (header) | Provenance. |

This record does not land on `main` while any support off `main` remains; before landing, each such
row is closed by landing its source or narrowed (§A.42 items 2, 8).
