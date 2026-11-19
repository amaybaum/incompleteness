# (γ): the substratum-to-detection correspondence at Main:682 — plan, r1

**Plan only; unreviewed; authorizes nothing.** This document plans paper-only work on the open
correspondence (γ). It derives nothing, evaluates no candidate, adopts no premise, runs no
computation, simulation, enumeration or Lean, edits no manuscript, and changes no Issue, writer,
tier or authorization. Every [A-inf] below is an author-side reading offered for a later unit to
check; none is a finding. Nothing in it starts until the owner authorizes a unit (§7).

**Authorization.** Owner decision record, #1169 c.6891511297 (`amaybaum`, 2026-11-15T08:11:04Z),
item (2c): "A plan only, with no derivation, for the open substratum-to-detection correspondence
(γ) at Main:682." The same record keeps "All S3 safeguards (c.6890079967, c.6891338304)" and
authorizes none of: "new physical premises, MR-1 stage 2, simulation, or merges. Physical source
remains NOT PASSED."

**Binding target** (#1169 c.6891338304, `amaybaum`, 2026-11-15T07:54:33Z). Hypothesis:
observational incompleteness explains our perception of quantum mechanics. **Q** (quantum zone) is
a descriptive label, defined by outcome. **C** (physical sector) is defined by the limits of
embedded observation, with no reference to quantum outcomes (noncircular). Required: coverage of
perceived quantum phenomena, and agreement with every performed experiment (§A.24, raw-direct).
The relation of C to Q is a finding, not a requirement.

**Writer:** Claude (paper-only writer for item 2c). **Review:** none yet.

**Inputs, at exact objects.**
- Corpus at `origin/main` `75cc51009aebcfb17c1bbf76d149760c540aac3b`, read with `git show`:
  - `papers/Main.md` (blob `0db17597`, cited Main:N); `papers/Substratum.md` (blob `da64dc35`,
    Substratum:N); `papers/Methodology.md` (blob `b1bbe2a2`, Meth:N); `papers/GR.md` (GR:N);
    `book/ch19-open-problems.md` (ch19:N);
  - SUBSTATE-1: `verification/programmes/substratum/continuous-substates/observation-context-protocol.md`
    (blob `6ca6f0ab`, cited OCP:N) and `README.md` in the same directory;
  - MR-1: `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md`
    (blob `c36fb14b`, PREREG:N) and `amendments/MR-star.md` (blob `45af1678`, MR★:N);
  - BORN-SEL (b): `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`
    (blob `9dac27fe`, QB3:N);
  - K1-RDY: `verification/programmes/oi-qm/reconstruction/round-k1-rdy-1/preregistration.md`
    (blob `c7505385`, K1R:N) and `result.md` (blob `e494a32b`, K1R-res:N);
  - `verification/programmes/oi-qm/reconstruction/drafts/unified-ledger-20261114/LEDGER-r9.md` (LEDGER:N);
    `verification/ROADMAP.md` (frozen; RM:N); `verification/audits/operational/census-oi-compatible-theories.md`.
- RO-1 drafts in `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, branch
  `research/ro1-sector-c-1169-20261114`, PR #1294 head `e681f62429994165ac8f11f39758813336ac2513`
  (the four blobs below are identical at `25207fae`):
  - `S3-PLAN-r9.md`, blob `46ebc72d` (PLAN), accepted by #1169 c.6890079967;
  - `S3-U1-r5.md`, blob `68983f86` (U1), accepted by #1169 c.6891241282;
  - `S3-U4-r1.md`, blob `e6d8101a` (U4), **unreviewed**;
  - `U4-SOURCES-r1.md`, blob `2e75b886` (INV), read-only inventory;
  - `S3-U2-r1.md`, blob `08afa36b` (U2), reviewed ACCEPT WITH CHANGES, not yet revised;
  - `VERIFY-SL3-CC-r2.md`, blob `9f81ad0e` (VER2), accepted by #1169 c.6891511297 item 1 at its
    stated narrower scopes.
- Issues read through the GitHub REST API on 2026-11-15: #1169, #866, #1007, #914 (body), and
  comments c.6891511297 and c.6891338304.

**Labels** (as U1 and U4): **[M]** on `main` at its own layer; **[M-r]** research or verification
record on `main`, with the standing its own status line gives; **[NP]** named premise (§A.46 item 7);
**[OFF]** off `main`; **[EXT]** external literature, to verify first-hand (none was read first-hand
for this plan); **[P]** proposed definition or plan decision; **[A-inf]** author-side inference, not
verification.

***

## 1. The precise statement of (γ)

### 1.1 What the corpus records

- [M] Main:682: "a finite set of apparatus settings — both slits open, one slit closed, a which-path
  record coupled — with the detection statistics over finitely many outcomes under each setting
  defines a finite-horizon action-labelled family"; "By the intervention dilation (§3.4), every
  such family has a finite reversible realization with one fixed prior"; "The detection statistics
  are an input of that construction, and a derivation of the two-slit interference pattern from the
  substratum dynamics is open."
- [M] Substratum:463: "In the double-slit experiment, the substratum occupies a single
  configuration at every step, and a derivation of the interference pattern from its dynamics is
  open."
- [M-r] LEDGER:394, row B-P4-MEAS-5: "Derivation of the double-slit interference pattern from the
  dynamics; full operational protocols; Frauchiger–Renner premises", classification UO
  ("unresolved obligation: no derivation at source", LEDGER:117).
- [M] Meth:401 uses the same passage: "compare the double-slit case of Main §4.1, where coupling a
  which-path record is an intervention that changes the visible transition law".
- [OFF] PLAN §8.4 check 1 (γ): "The additive-field interference of S-L1 corresponds to the observed
  detection statistics." U4 §3.3 stops there: "D-1 outcome: undecided at (γ)."

So the corpus has the **input direction** only: given detection statistics, a realization exists.
That realization is a per-law construction (response table, ledgers, product prior), which is
*representable*, not *available* (U1 §2.3; PLAN K-4, Main:582: "the same reversible machinery can
realize non-quantum finite instrument families"). (γ) asks for the other direction.

### 1.2 The objects (proposed definitions, for unit G1 to fix)

[P] **Substratum side.** One fixed model `M = (S, φ, μ, Obs, Γ, R, Res)` (U1 §2.1), with:
- one rule, named per reading (α) of P-vii (K1 under the global reading; a σ12 rule, MR★:667, only
  where (α) or a later decision places the apparatus there); the reading itself stays under #1234;
- one `μ`, fixed before any setting (U1 G3), reported at U1's levels: *derived* only with the
  counting measure of Main Lemma 3 (Main:54), otherwise *available relative to the declared μ*;
- one access instance AD-1 (U1 §3), carried in both slice forms A-reg and A-cur where K1 is used;
- one **double-slit program family** `{g_a : a ∈ 𝒜}`, each a program in U1's sense (§2.1): declared
  regions (source, two path regions, an optional marker region, a screen of finitely many readout
  cells, ledgers), one budget, one read schedule, one comparison tick `t_c`, the same for every
  setting value. `𝒜` is SUBSTATE-1's six protocols (OCP:19–24): both open, left only, right only,
  marker stored and unread, marker read in the path basis, marker read in a complementary basis.

[P] **Detection statistics for an embedded observer, under U1's criterion.** For protocol `a`, the
**complete record law** `L_a`: the joint law, at `t_c`, of every record held (G4) by the declared
observers — screen cell, marker record, setting record, herald, loss and attempt marks — with
unnormalized masses (G5), computed from `μ`, or from `μ` conditioned on an *executed* herald with
the complementary mass kept (U1 §2.1, "Execution"). It is a law over the ensemble `μ`, not over the
analyst's sequence of projected configurations (R-seq is a representation, U1 G4). Its level is the
weakest level of the actions `g_a` uses (C-PREP, C-SET, C-INT, C-REC, C-RET, C-REN; U1 §4).

[P] **Target side.** For each `a`, the raw-direct observables (§A.24) of performed experiments:
counts per screen cell per incident particle, losses included (subnormalized, OCP:26–28); marker-
conditional counts with full branch masses (PREREG T4, :490); and, for coverage beyond fringes, the
single-detection observables listed in §5.3. All are [EXT].

[P] **The correspondence.** A map `κ` from `{L_a}` to the target observables, fixed before any `L_a`
is evaluated: which region is the screen, which held value counts as a detection at which cell, how
incident flux is normalized, and how a probability under `μ` is compared with a relative frequency
over runs (§3, H-4). `κ` may not refer to amplitudes, `|·|²`, a Kraus menu, assigned marker overlaps
or quantum statistics (K-2, G7; OCP:41; PREREG:233–237).

### 1.3 What would close it: two directions, kept apart (§A.34)

- **(γ→), derivation and agreement.** For the fixed `M` and `κ`, each `L_a` is derived from `(φ, μ)`
  at a stated level, and `κ(L_a)` agrees with the raw-direct data for every performed protocol in
  `𝒜`. This is "substratum dynamics → detection statistics".
- **(γ←), coverage.** Every perceived double-slit phenomenon in `𝒜` (and in the extended list of
  §5.3, if the owner adopts it) is realized by a program in `Γ_exe(M)` of the **same** `M`, the same
  `μ` and the same AD-1 instance (U1 G6; AC-1, one interface).

Neither direction gives the other. (γ←) can hold with a program whose law disagrees with a
performed apparatus elsewhere; (γ→) for one geometry says nothing about the other five protocols.
The intervention dilation (Main:480–482) supplies (γ←) only at the representable level, with a
constructed `S`, `φ` and `{𝓘_a}` per family; it does not count toward either direction (K-4).

**Outcomes, per direction and per protocol** (U1 §2.3 and PLAN SNR-1, unchanged):
- *closed at level X*: derived, or available relative to the declared `μ`, with the level stated;
- *unsourced* or *requires assumed apparatus*: not a negative;
- *counted miss*: an available `L_a` with every input derived or disproved, whose `κ`-image
  disagrees with a raw-direct datum. It falsifies the identification `(M, κ)` at that scope. It does
  not falsify every observer-level extension (Code Review Rules, bridge and no-go scope);
- *undecided*: otherwise.

**What (γ) is not.** It is not the derivation of the Born exponent (#914 row 1e; #1059), nor Born
statistics across settings (#914 row 17c), nor the full operational completion (#914 row 21). It is
the double-slit instance of row 17c's question, at the record-law layer, under U1's criterion. A
closure of (γ) on K1 that reproduces only what a classical coherent wave reproduces is reported as
such (§5.1, PC-wave) and is not coverage of perceived quantum phenomena.

### 1.4 Where (γ) blocks

- **D-1** (PLAN §8.4 check 1): its miss and match branches need (γ); U4 §3.3 stops there.
- **AC-1, coverage half** (as amended, c.6891338304): U2 §11.2 records "Coverage half: shown on no
  model" ([OFF], U2:523). For which-path complementarity, coverage on a fixed model is (γ←) for the
  marker protocols of `𝒜`.

## 2. Existing evidence and prior attempts (homes, not duplicated)

| Item | Status | Bearing on (γ) | Home |
|---|---|---|---|
| Main:682; Substratum:463 | [M] open | (γ) itself; input direction only | — (no accountable Issue located; owner question 3) |
| LEDGER:394, B-P4-MEAS-5 | [M-r] UO | classification of the obligation | #914 (ledger) |
| Intervention dilation, Main:480–482; gluing remark Main:582 | [M] proved; kernel-checked equivalence (`finite_horizon_equivalence`) | representable-only realization of any action-labelled family, quantum or not; negative control K-4 | — |
| Diagonal preservation, Main:326–328; `permTheory_phase_ceiling` (#914 row 8) | [M] paper proof; kernel | under the stated access, no available operation creates coherence from a basis state | #914 rows 8, 9 |
| Census cell {D}: "the absence of interference fringes in any experiment prepared and read in the computational basis" | [M-r] | the coherent-preparation layer is where operational fringes would enter | — |
| Born form exhibited, exponent not selected (Main:18, :224); μ-form/μ-number (QB3:49–75): "the recovered table is the same for `\|U\|^p` at every `p > 0`" (a reading of the proof, QB3:54); μ-number "invariance fails on the tested class; selection open" | [M]; [M-r] reviewed (QB3-EVIDENCE-REVIEW.md) | the representation dictionary cannot serve as evidence for (γ); detection numbers depend on `μ` | #1059 (BORN-SEL); #914 rows 1e, 14 |
| Posit (iv), Main:724: measure selection "a standard but substantive epistemic postulate, not derived" | [M] | `μ` enters every `L_a` | #1059; #866 O-OBSMU |
| SUBSTATE-1 observation-context protocol (OCP) | [M-r] preregistered research protocol; exact reference benchmark; **no native microdynamics** (OCP:56) | supplies `𝒜`, C0, C1, C2, the no-upgrade rule (OCP:44–46) and the native test gate (OCP:88–97) | #1007, PR #1009 |
| MR-1 preregistration: complementarity benchmark (PREREG:228–238), T0 (:471), T3 (:485), T4 (:490), W1 (:519) | [M-r] stage 0; stage 2 not authorized | the which-path tests and their physical-justification clause | #866 (O-REC, MR-1) |
| MR★ S-L1 (:491), S-C1 (:498), S-L5 (:584), S-L7 (:603); μ leg (:642): "every region's marginal is uniform, so there is no ready region" | [M-r] stage 1; S-L5, S-L7 [NP]; S-L3 verified at VER2's scope (c.6891511297 item 1) | on K1: additive interference; no conditional dynamics; marking does not destroy interference; no ready region under the counting measure | #866 |
| K1-RDY-1 | [M-r] halted (`S12`), K1R-res:3; P0 evaluated, P1 not | readiness under a conditioned law (K1R:18) is the preparation that a K1 detection law needs (§3, H-1) | #1031 |
| NATIVE-PREP-SRC-1, NATIVE-INT-SRC-2, CP-PREP-1 | [OFF]/[M-r] per #866 table; physical source NOT PASSED | native preparation and observer–apparatus interaction; both inputs of every `g_a` | #866 |
| PLAN §8; U4 §§2–6 | [OFF] PLAN accepted; U4 unreviewed | D-1's conditions (α)–(δ); U4-F1 (masking coset); U4 §2.1 "Marker coupling is not a setting on K1" | #1169 (RO-1/S3) |
| U2 §11.2 | [OFF] reviewed ACCEPT WITH CHANGES | AC-1 coverage half shown on no model | #1169 |
| ROADMAP:1608–1613, "Named double-slit / Born-interference benchmark" | [M] frozen record, set aside "with a reason" | an earlier adjudication that the packaging was not a dependency gap; the amended AC-1 now makes coverage a requirement | — |
| #914 rows 12 (lift, L3 underdetermined), 16, 17c (O), 20 (O, research) | [M-r] planning record | (γ) is an instance of 17c; routes C and D (§4) wait on rows 12 and 20 | #914 |

[P] **Not duplicated.** This plan defines (γ) and orders units that would use these records. It does
not re-plan MR-1 stage 2 (#866), K1-RDY's P1 (#1031), BORN-SEL's selection question (#1059), the
SUBSTATE-1 native test gate (#1007/#1009), or the σ12 recording screen routed by U4 §10 to #866.

## 3. Hidden assumptions to watch (§A.31, gem-finding form)

Productivity test, fixed now for the units that follow: a check is a gem if it yields a fact
strictly stronger than the obvious restatement and either constrains (γ) or exposes an assumption
in a corpus statement about it. Each marker below is a question for a unit, not an answer.

- **H-1. A pattern needs a non-uniform ensemble.** [A-inf, to check in G2] Under the counting
  measure, every region's marginal is uniform (MR★:642), and `μ` is `φ`-invariant. On K1, by S-L1,
  the screen's content conditioned on a setting value `z` is `Φ_{DZ} z` plus a sum of independent
  uniform contributions, hence uniform on a coset of the subgroup those contributions span — the
  structure U4 §3.2 found for the marker. If that subgroup is the whole screen group, the
  setting-conditioned detection law is uniform and does not depend on `z`: no fringe and no
  which-path effect, for any geometry. Fringes would then need a proper subgroup (a geometric
  property of the K1 propagator), a sourced non-uniform preparation (C-PREP; NATIVE-PREP-SRC-1), or a
  conditioned law on an executed herald (the K1-RDY question, K1R:18). If confirmed, (γ) on K1 under
  the counting measure reduces to preparation sourcing and carries no separate content.
- **H-2. No intensity on the value group.** The K1 value group is `ℤ/q`, `ℤ_p` or `ℝ/ℤ` (MR★:464).
  None carries a modulus-square, and S-C1 (MR★:498) excludes conditional dynamics, so no threshold
  detector is native on K1. A K1 detection event can only be a held readout value; its probability
  can only come from `μ`. Any `κ` that converts a field value into a click rate is a supplied
  detector model and fails G1 unless sourced.
- **H-3. Settings versus geometry.** Main:682 and Meth:401 treat "slit closed" and "record coupled"
  as settings of one apparatus. On K1 the graph is fixed and a per-design graph is excluded
  (MR★:471–473); U4 §2.1 [OFF]: a marker "records" whenever `Φ_{AΣ} ≠ 0`, a property of the declared
  region. So the six protocols may be programs of different models, and comparing them would breach
  G6. Whether a native blocking operation or marker-coupling setting exists is a C-SET/C-INT
  question; on K1 a setting enters only additively.
- **H-4. Probability versus frequency.** Performed data are relative frequencies over sequential
  runs in one history. In OI one history is one orbit of `φ`; its time averages are taken under the
  uniform law on that orbit, not under the counting measure on `S`, and QB3 shows that one-step
  matrices differ between such laws on CE-8 (QB3:60–61). Sequential runs also need renewal (C-REN;
  H-RR; #913 O-REUSE). `κ` must state which identification it uses, before evaluation, on grounds
  that do not refer to the outcome (K-2).
- **H-5. Exponent blindness.** The fixed-basis Born form does not select the exponent (Main:18), and
  the permutation-unitary table is the same for every `p > 0` (QB3:54). Agreement of `L_a` with
  `|ψ|²` at the `Q_fb` layer is definitional; citing it for (γ) is circular.
- **H-6. Classical-field interference is not quantum interference.** S-L1's additive superposition
  is the interference a classical coherent wave also shows (OCP:37–39). PLAN §8.4 keeps three
  objects apart: classical-field interference, quantum interference (W1, PREREG:519) and the ability
  to create or erase which-path information. A K1 closure that matches fringe intensities is at most
  "interference compatible with classical coherent waves; no quantum completion" (OCP:45).
- **H-7. Visibility loss without a record.** By S-L5 [NP], on K1 a marker cannot remove interference;
  any loss is an additive offset of carrier-independent content (U4 §4.2). Complementarity on K1, if
  present, would come from `μ`-noise, not from the record. A `κ` that reads such a loss as which-path
  decoherence would need the D–V relation to hold as executed quantities (PREREG:233–237).
- **H-8. Conditioning as preparation.** A fringe that appears only after conditioning on a herald or
  marker value is a selection effect unless the herald is executed and the complementary mass kept
  (U1 G5; OCP:46; PLAN K-6).
- **H-9. Scale and isotropy.** Agreement with performed fringe spacings needs an emergent dispersion
  relation and spatial isotropy. Isotropy is empirical input E4 (Main:670), and the observer-level
  wave operator is unresolved (Main:588; #914 row 12). A quantitative (γ→) on a lattice geometry
  inherits both.
- **H-10. The input direction may be the only well-posed one at the law layer.** Main:682's family is
  realizable for any detection table, quantum or not (Main:582). A (γ) statement phrased only at the
  `Q_fb` layer cannot discriminate; the discriminating content, if any, lies in which tables are
  *available* on a fixed `M`.

[P] **Cross-propagation.** H-1, H-4 and H-5 apply to every OI claim that compares a law under `μ`
with laboratory frequencies, not only to (γ); they are recorded as assumption-watch markers for D-1,
AC-1's coverage half, and #914 row 17c.

## 4. Candidate routes

Each route: what it would establish, its first missing step, required inputs, and the cheapest
decisive test. "First missing step" is the next link with no producer; the ultimate goal is (γ→)
and (γ←) on one model.

| Route | Would establish | First missing step | Required inputs | Cheapest decisive test |
|---|---|---|---|---|
| **A. K1, global reading of P-vii, counting measure** | (γ→) for K1 protocols at the *derived* level, or a counted miss | a setting-dependent detection law at all (H-1); then a sourced carrier preparation (C-PREP; T0, PREREG:471) | S-L1, S-C1, MR★:642; U1 AD-1 (both slice forms); `κ` from G1 | **G2**: exact hand algebra on S-L1 — is the subgroup spanned at the screen by the non-carrier regions the whole screen group, for a declared two-path geometry? Same computation type as (2b)'s masking question (U4-F1) |
| **B. Fixed-basis representation** | nothing toward (γ); serves as target language and negative control | — (representable only) | Main:480–482, :582; `finite_horizon_equivalence` | none needed: classified representable-only by K-4; used as control NC-rep (§5) |
| **C. Non-additive rules (σ12: native-Y, G_SM, SM:104–106, SM §6.5)** | native threshold detection and record-tied visibility, where S-L5 does not hold | a recording screen of σ12 under U1 (U4 §4.5; routed to #866) | (α) placing the apparatus there; NATIVE-INT-SRC-2 (STOPPED / UNSOURCED) | paper screen of one rule: does a held record conditioned on carrier content exist under G1–G7? Owned by #866, not here |
| **D. Observer-level lift / continuum wave (L3)** | an emergent wave with an intensity-type readout | the site-space wave-operator formulation (Main:588; #914 row 12, "L3 … underdetermined") | lift sources; E4 | whether a lift yields a quadratic readout functional without inserting it; even then PC-wave applies (H-6) |
| **E. SUBSTATE-1 continuous substates (C2)** | the preregistered native double-slit test on a continuous-state model | OCP's realization dossier: "a pinned microscopic d=3 update and prior" (OCP:58), and its native test gate (OCP:88–97) | #1007/#1009 scope and writer | the gate itself: are a which-path marker and a complementary read both selectable on one incident preparation? Owned by #1007/#1009 |
| **F. Measure and frequency** | the identification inside `κ`: ensemble `μ` versus orbit frequency (H-4) | a target-neutral statement of which law the laboratory frequency estimates | QB3 §1; posit (iv); C-REN | **G4**: a definitional note stating both identifications and where they differ on records already on `main` (CE-8); no selection |

[A-inf] Route A is the only route whose first test is reachable by hand algebra on records already on
`main`; routes C–E wait on obligations owned elsewhere. Route F is definitional and must precede any
evaluation of `L_a` under route A.

## 5. Controls and countercontrols

Fixed before G1 and applied to every unit. They add to PLAN K-1–K-6 and AC-1, which apply unchanged.

### 5.1 Positive and negative controls

| # | Control | Required result | Source |
|---|---|---|---|
| C0 | Fixed-path classical stochastic model: two-open = sum of subnormalized one-open patterns | must **fail** the two-open benchmark; a native law that C0 also reproduces gains nothing | OCP:34–36 |
| PC-wave | Classical coherent wave through both paths with a linear recombiner | must **pass** the fringe statistics; a native result reproducing only what PC-wave reproduces is labelled "interference compatible with classical coherent waves; no quantum completion" and does not count toward AC-1's coverage half | OCP:37–39, :45 |
| NC-rep | The intervention dilation realizing an anti-complementary family (fringes kept with full which-path information) | must be realizable: it shows that representability tests nothing (K-4) | Main:480–482, :582 |
| NC-copy | A non-invasive classical copy of the path, which leaves the fringe intact | separates record formation from visibility loss; D–V relation need not hold classically | PREREG:237–238 (CC1) |
| NC-noise | Visibility loss by carrier-independent additive noise with no record | must be distinguished from record-tied loss | U4 §4.2; CC7 (VER2 scope) |
| Deletion | Remove the second path's transfer, the marker, the setting, the herald in turn | the attributed effect must vanish | PREREG T8 |

### 5.2 Noncircularity countercontrols

- **NC-γ1.** `κ`, the screen region, the run and renewal convention, `μ`, AD-1 and the program family
  are declared before any `L_a` is evaluated. A `κ` justified only by matching Born statistics is
  rejected (K-2, G7). The correspondence may not be chosen to reproduce Born statistics.
- **NC-γ2.** No amplitude, wavefunction, Kraus map, Born probability or assigned marker overlap
  enters (OCP:41; PREREG:233–237). The `Q_fb` Born form is not evidence (H-5).
- **NC-γ3.** One `M`, one `μ`, one AD-1 instance for all of `𝒜` (G3, G6). Verdicts under different
  slice forms or rules are reported separately and never combined.
- **NC-γ4.** Complete masses: every attempt, loss and herald kept unnormalized (G5); no
  postselection (K-6; H-8).
- **NC-γ5.** No `C` adjusted after results are known (U4 authorization record, owner refinement);
  agreement with performed experiments tests `C`, it does not define it (U4 §0).

### 5.3 Agreement with performed experiments (raw-direct, §A.24; all [EXT])

Each to be read first-hand before use. Eraser and complementarity sources are inside authorized unit
(2a); the others would need the owner's extension of (2a) or a sibling unit (owner question 4).

| # | Observable | Distinguishes | Sources (to verify) |
|---|---|---|---|
| X-1 | Single-particle fringe build-up: discrete detections whose cell frequencies approach the pattern | C0 (fails) from PC-wave and QM | Tonomura et al. 1989; Arndt et al. 1999 |
| X-2 | Single-quantum anticorrelation behind a beam splitter (anticorrelation parameter below the classical bound) | PC-wave (fails) from QM | Grangier–Roger–Aspect 1986 |
| X-3 | Third-order interference `I_3 = 0` in three-slit experiments | a quadratic probability rule; classical square-law waves also satisfy it, so it tests the exponent, not nonclassicality | Sorkin 1994; Sinha et al. 2010 |
| X-4 | Which-path complementarity `D² + V² ≤ 1`, with a stored unread marker | record-tied visibility loss versus NC-copy | Englert 1996; Dürr–Nonn–Rempe 1998 (INV 5.3, 5.5) |
| X-5 | Delayed-choice erasure: unsorted pattern without fringes; sorted conditional fringes summing to it | the accessibility reading U4 §6.3 found disagreeing with data | INV 5.9–5.13 |

[P] Coverage of perceived phenomena in the sense of c.6891338304 needs at least X-1, X-2 and X-4 on
one model; X-3 bears on the exponent (#1059); X-5 is the parked-record check U4 already applies.

### 5.4 Same-interface report (AC-1 as amended)

Every unit reports, on the same `Γ_exe`, (i) coverage of `𝒜` and §5.3, (ii) agreement with
performed data, and (iii) as a finding, whether the same model also yields stronger-than-quantum
behaviour in unperformed settings (C/Q relation). No unit proposes a restriction to win (iii).

## 6. Bounded units, in dependency order

All paper-only. None runs a simulation, enumeration or Lean, adopts a premise or edits a manuscript.

| Unit | Content | Depends on | Could establish | Stops when |
|---|---|---|---|---|
| **G1. Definition** | Fix §1.2's objects: `𝒜`, the program family per rule and slice form, `L_a`, `κ` (with both H-4 identifications carried), the target list. For each `g_a`, list the U1 actions it needs and their outcome from existing records (U1 §4, U2, U4) | this plan accepted | definitions; per-protocol "unsourced at X" or "requires assumed apparatus" from records already classified. No derivation | an action has no classification on record (named stop); or a definition would need an outcome-based choice (K-2) |
| **G2. K1 detection law** (route A, H-1) | Exact hand algebra on S-L1 for one declared two-path geometry, shared with (2b)'s masking computation if the owner so decides: whether the screen-side subgroup is the whole group; the resulting setting-conditioned law | G1; derivation authorization (outside 2c) | either "on K1 under the counting measure, the setting-conditioned detection law is uniform for this geometry" (scoped negative: route A reduces to preparation sourcing), or a proper subgroup and the law it gives, checked against C0 and PC-wave | the question needs enumeration or simulation (halt, as K1-RDY did); or `κ` is not fixed |
| **G3. Literature** | First-hand reads of X-1 to X-3 (X-4, X-5 are in (2a)): raw counts, conditions, losses | none | the agreement targets with verified values | a source is unavailable first-hand (recorded) |
| **G4. Measure and frequency** (route F, H-4) | State the ensemble and orbit-frequency identifications, their difference on QB3's CE-8, and their dependence on C-REN; select neither | G1 | an exposed assumption inside `κ`, with both readings carried as AD-1 carries both slice forms | a selection would be needed (owner question 5) |
| **G5. Synthesis** | Per route and protocol: (γ→), (γ←), outcome level; D-1's (γ) condition; AC-1 coverage half; C/Q finding | G1–G4; routes C–E as their owners report | a precise status for (γ) per route; no closure is expected | — |

[P] Routes C, D and E have no unit here: they wait on #866 (σ12 recording screen; NATIVE-INT-SRC-2),
#914 row 12, and #1007/#1009. G5 reads their records as they land.

**What the sequence can and cannot reach.** [A-inf] On the record, G1–G5 can at most: define (γ);
report it unsourced per protocol; decide route A's H-1 question for declared geometries; and expose
the frequency assumption. (γ→) on K1 at the derived level would also need a sourced preparation,
which no record supplies (MR★:642; K1-RDY halted; NATIVE-PREP-SRC-1 NOT PASSED). No unit here can
close (γ) or reach a counted miss beyond the scope of what it derives.

## 7. Owner questions

1. **Authorization.** Is G1 (definition, paper-only) authorized? G2 is a derivation and lies outside
   (2c): should it be authorized, and merged with (2b)'s masking computation since both decide a
   subgroup of the K1 propagator's image?
2. **Writer and reviewer.** Claude as writer with a separate non-author Claude reviewer, ChatGPT
   review optional, as for (2a)–(2c)?
3. **Home Issue.** No accountable Issue for B-P4-MEAS-5 was located (§A.45 rule 6). Should #1169
   carry (γ) as an obligation row, or should a dedicated Issue be opened, cross-linked to #866,
   #1059, #1031, #1007 and #914 rows 17c and 20?
4. **Literature scope.** Should (2a) extend to X-1 to X-3, or should G3 be a separate unit?
5. **Frequency identification.** Should G4 carry both identifications (ensemble `μ`, orbit frequency)
   without selecting, as AD-1 carries both slice forms, or is a selection an owner decision?
6. **Classical-wave ceiling.** Is a K1 result that reaches only "compatible with classical coherent
   waves" (PC-wave) to be reported as not counting toward AC-1's coverage half, as OCP:45 implies?
7. **Reading (α).** Confirmed that (γ) is reported per reading of P-vii, with C-1 and OB-b0 left
   under #1234?

## 8. Off-`main` references traced (§A.42 item 8)

| Reference | Claim it is attached to here | Classification |
|---|---|---|
| PLAN, U1 on PR #1294 at `e681f624` | the frame, the criterion, D-1 and AC-1 | support off `main` (gap); accepted by owner records c.6890079967 and c.6891241282 |
| U4 at `e681f624` | U4 §2.1 (settings on K1), §3.2 (coset), §3.3 (stop), §6.3 (accessibility reading) | support off `main`, unreviewed; used as context for H-1, H-3, H-7 and X-5 only |
| U2 at `e681f624` | AC-1 coverage half "shown on no model" | support off `main`; reviewed, not yet revised |
| VER2 at `e681f624` | S-L3 and CC7 scopes | support off `main`; accepted by c.6891511297 item 1 at its scopes |
| INV at `e681f624` | external-source item numbers | provenance |
| #1169, #866, #1007, #914 bodies and comments | authorization, planning homes, row numbers | provenance and governance |

[P] This plan is itself off `main` and unreviewed. Every statement resting on an [OFF] or [NP] row
carries that gap.
