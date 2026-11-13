## EOI gate (Emergence and Embedded-Observer Integrity): draft acceptance criterion for #1169 (r4)

**Standing.** WIP / UNVERIFIED planning draft for #1169. Model-written; r4 answers the re-review of r3
(`7fdef7a9…93ce929`, ACCEPT WITH CHANGES, R3-B1, R3-B2, R3-N1 to R3-N3); earlier dispositions are referenced in §8. It proposes a planning and
acceptance criterion only. It changes no scientific status (§A.45 rule 1), adopts no premise, edits no record, and
grants no authorization. A gate label is a planning attribute; what a construction establishes stays in its records on
`main` (§A.46). Frozen and accepted records are not edited: the retrospective classification in §3 lives only in this
mutable planning comment (§A.42 item 6). Every original mathematical finding keeps its proved scope; the gate changes
scope statements and interpretation only (owner integration requirement R-I1).

**Sources** (every `X:n` is line `n` at the pinned commit):

| Abbr. | Record | Pinned at |
|---|---|---|
| MC1 | `verification/programmes/oi-qm/reconstruction/mathcon1-polc-20261108/DESIGN.md` (branch `research/mathcon1-prereg-20261108`, #1206; not on `main` at `5ce4f98e`) | `41a42cb97e5e044f5a9e906e33fbf6f22de52dc4` |
| M1D, M2D | `…/mechanism-1-20261107/DESIGN.md`, `…/mechanism-2-20261108/DESIGN.md` | `main@5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732` |
| MID, MIR | `…/minacc-1-20261108/DESIGN.md`, `…/RESULT.md` | `main@5ce4f98e` |
| A45 | `verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/result.md`; `Main` = `papers/Main.md` | `main@5ce4f98e` |
| PCD | `…/fhesel1-p-control-20261108/DESIGN.md` (draft PR #1203) | `cc4537746301b672e2f871f930c7e63e82d5c2e5` |
| PMD | `…/fhesel1-p-mix-20261108/DESIGN.md` (draft PR #1204) | `7d707bb512fe474591aa7900d068fd9852a51e35` |
| POD | `…/fhesel1-p-obs-20261108/DESIGN.md` (draft PR #1205) | `83eca7cdcf77258bf5c013116796113939425993` |
| S1B | MATH-CON-1-S1B-1 preregistration, draft r5 (pre-`F`; not pushed in this form) | sha256 `36cc740a…23c3eb` |

**Owner direction** (amaybaum, chat, 2026-11-08, verbatim as relayed by the coordinating session; to be quoted from
its #1169 record with author and time before posting): "The main risk is not that embedded observers are secretly
reading hidden information. It is that some proofs restrict hidden memory or import quantum behavior, and their
conclusions are subsequently presented as general properties of OI." "What is proved only under particular hidden
priors or observer interfaces? Clearly label these as conditional. Test alternatives where the dependence affects a
major conclusion." "What genuinely emerges from OI alone? Reserve this classification for behavior obtained without
inserting the quantum target into the physical assumptions." R-I4: "Separate representation from mechanism. A unitary
lift, Born-rule marginal or Lüders instrument imported mathematically must never be credited as an OI physical
derivation."

***

### 1. Gate text

**Scope and claimed items.** The gate applies to any construction whose record is offered as bearing on "QM from OI".
Its preregistration fixes the *claimed items* (each operation, law, rule or structure the construction is to yield)
and excludes from them every item met through a shared reference interface. The class attaches to each claimed item;
a construction's class is the list. Applied to a preregistration, the gate yields only the reachable set of classes.

**Principle 1 (outcome, not input).** Quantum structure may enter as a target or comparator. A quantum operation,
probability rule, measurement rule or Hilbert-space structure that enters as a physical ingredient is not counted as
derived (R-I4).

**Principle 2 (embedded observer).** Every observer or controller decision (preparation, setting, feedback, stopping,
conditioning, registration) depends only on physically available records, known preparation information and
executable controls, as available at the decision. No decision reads the full microstate, unregistered hidden values
or later events. Hidden information becomes available only through a protocol of the stated class under the stated
dynamics. Operationally: known preparation information is the declared laws, including supplied known values
(information axis); executable controls are the stated class's operations (execution axis). The *embedded class* is
the protocols whose decisions meet Principle 2 and are executed by the stated rule, under the same world assumptions.

**Role test (G1).** An item is an *ingredient* iff removing or replacing it changes the dynamics, the records or an
observer decision. It is *test-only* iff it enters only the map from record statistics to the compared quantity. An
ingredient supported only by a consequence of the target (CC-RECON, M1D:357; PCD §3.2, PCD:442) counts as a [Q]
ingredient. Under this test A-2's readout and discard rules (MC1:170) are ingredients. Items in neither role (a motivation, the
claimed-item list) are not ledgered.

**Audits.** Each audit reads a table the record supplies. "Disclosed" means listed with any status the record uses
(derived and cited, posit, hypothesis, modelling condition, supplied, imported). A conclusion carries its labels
directly or by reference to a named scope section that lists them.

| Audit | Evidence the record supplies | Pass | Disclosed departure (caps at EOI-C) | Fail |
|---|---|---|---|---|
| **G1 Quantum import** | Clause ledger: every ingredient and comparator with class [N]/[R]/[Q]/[P] and role (role test); for operator-level rules, the CT verdict with its class column (MC1:409) | No [Q] ingredient | [Q] ingredients only inside a disclosed shared reference interface, none of whose items is claimed | Per claimed item: the role test, applied to that item's records, finds a [Q] ingredient outside such an interface, or a clause names or supplies the item (including a [Q] uniform law CT does not mark, MC1:449) → EOI-I for that item |
| **G2 Embedded access** | Access table: each decision, what it reads (*information axis*) and what executes it (*execution axis*) | Reads only records, known preparation information and the schedule; executed by the stated rule | Executed by a supplied agent or source (M1D:900; MID:417, 607; POD:438) | Reads unregistered hidden values, the microstate or later events; or an exposure asserted without an exhibited protocol |
| **G3 Hidden memory and prior** | Environment ledger: every independence, product-source, freshness, decoupled-store, common-lift (H-LIFT type), carried-versus-tensor-factor ancilla (A45:5, 38–39), finite-cone and recurrence assumption; the hidden prior `μ_H` each conclusion uses (Main:60) | Each is derived from, or is itself, a framework posit other than a hidden prior, cited; a posit Main states for every realization, such as (iv), is a framework posit, not a hidden prior (Main:406–410); a hidden-prior assumption only if the item is shown for every `μ_H` in a prior class fixed in the preregistration that contains the counting measure and, for each restriction on `μ_H` that the proof uses at a named step (G0's dependency trace), a law violating that restriction inside the protocol's dependency cone; the item's scope names the class | A particular `μ_H` (a realization datum, Main:60; the counting measure is a selection principle, Main:56) and every assumption that only restricts it (uniform unknown slots, H-PS, fresh fixed-law cells); any other assumption, disclosed. If a conclusion is known to change under a correlated or non-uniform hidden law, its scope names that dependence (R-I3; Main:60); where this bears on a major conclusion, an alternative-prior check is a planning item | An undisclosed assumption; a known prior dependence not named in the scope |
| **G4 Physical record** | Record table: for each record a conclusion conditions on, the carrier that holds it, its retention, reset and timing; whether the conditioning set is the retained record or the analyst's transcript | Retention, reset, fresh ancillas and timing produced by the stated dynamics | Perfect retention, free reset, fresh ancillas or a supplied schedule disclosed (P1; POD:433–447) | A conclusion conditions on information no stated record holds, undisclosed |
| **G5 Emergence vs matching** | Agreement claim on joint laws of whole accessible record sequences, branch by branch, under the class's adaptive protocols (feedback, repeats, changed settings, composition), and the imitation countercontrol in the fixed class below | Equality for all finite sequences, by exact homomorphism or induction over a closed family (M1D:372); and either the item is claimed only as the imitable fragment, or the imitation fails or none exists in the fixed class (proof) | — | Agreement only for hidden-averaged, single-step or one-setting statistics; the countercontrol not reported; or an item claimed beyond the fragment while an imitation reproduces every compared law or the question is undecided |

**Imitation rule (G5).** The imitation class is fixed: ontological models that are preparation-, transformation- and
measurement-noncontextual on the compared fragment (A6, M2D:250; Theorem NC's notion, M2D:485–498; CC-IMIT′, M1D:356);
operational equivalences are statistical equivalences over the construction's accessible preparations,
transformations and reads. Where the accessible reads do not span the configuration-level read space (M2D:488–490,
521–527), a failed imitation counts toward G5 only with a proof that the missing reads are physically absent in the
stated class and dynamics (M2D:528–529); otherwise the question is undecided. A comparator frame used to state
spanning is test-only. A measure-and-prepare imitation is not this class. The construction's own configuration model
counts only if it is noncontextual on those equivalences. If an imitation in this class reproduces every compared joint law, the
claimed item is the classically imitable fragment and is not counted as quantum beyond it.

**Operator-level rule.** A construction stated on a shared operator interface (A-2) supplies, in place of the G2–G4
tables, the interface's attach, readout and discard rules, each a disclosed departure; and in place of G5, availability
of the claimed operation at every finite depth of repeated composition (MC1:201). Its claimed items are operator
availability statements. The imitation rule is not evaluated, and the class is at most EOI-C, which credits
availability on A-2 only and no physical derivation of the imported unitary or Lüders items (R-I4).

**Negative-result audit (G0).** A failure, obstruction, LIMIT or no-go record states: the class it is proved for;
whether that class contains the embedded observer's class; whether it is universal ("no protocol in Π achieves X")
or existential ("some protocol in Π breaks X"); a census or definition-level result says so instead. Labels:
- *within its stated class*: every negative;
- *restricted*: the proof uses a G2–G4 restriction on hidden correlations, memory, prior or access, at a named step.
  Owner (chat, 2026-11-08, as relayed): "A proof that excludes such memory is valid only within that restricted
  model; it cannot automatically establish a limitation of OI generally."
- *idealization-dependent*: an existential negative, or a universal one over a class not containing the embedded
  class, whose proof uses a supplied observer capability (records, preparations, executor) at a named step.
A claim that relaxing the restriction, or removing the capability, removes the failure needs its own proof or
exhibited construction. A negative is stated beyond its class only with a proof that uses none of these, or a proof
that the restriction is without loss of generality.

**Classes** (first matching row; each claimed item gets exactly one):

| Class | Condition |
|---|---|
| **reachable set only** | No result record exists (design or preregistration) |
| **EOI-NEG, negative** | The result for the item is a failure, obstruction, LIMIT or null; carries its G0 labels |
| **EOI-I, imported QM** | A positive result for the item, and G1 fails for it |
| **EOI-N, native emergence** | A positive result; G1–G5 pass with no departure; criterion preregistered (pending owner decision §6 (b)) |
| **EOI-C, conditional reconstruction** | A positive result; G1–G5 pass or carry only disclosed departures; every departure and label carried into the conclusion |
| **EOI-0, not classified** | The remainder: an undisclosed G2–G5 failure, or an inconclusive or void result |

Only EOI-N counts as deriving QM from OI. The prefix `EOI-` avoids collision with MATH-CON-1's (P)/(C)/(N)/(I).

***

### 2. Mapping onto MATH-CON-1's circularity test (CT)

| MATH-CON-1 outcome (MC1:499–503) | CT verdict and class disclosure | EOI class |
|---|---|---|
| (P) or (C-T1) | `generated`; every rule clause [N]/[R] | EOI-C by the operator-level rule: A-2 is a disclosed shared interface, and T3, met through it (MC1:200), is not a claimed item |
| (P) or (C-T1) | `generated`; some rule clause [Q] (a G-u law, as CC-0's) | EOI-I. CT returns `generated` here by the writer's choice not ruled by the owner (MC1:431–434, 449–452) |
| (C-inst) | `installed` or `mixed` | EOI-I for `K*`; for `mixed` the record states the other clauses' part |
| (N) | — | EOI-NEG; (N)'s row already excludes "a failed route alone" (MC1:502) |
| (I), or void at order 0 | — | EOI-0 |

On the object the reachable labels are (C-inst), (N), (I) (MC1:548–560), hence the reachable set {EOI-I, EOI-NEG,
EOI-0}. No CT outcome reaches EOI-N: CT is scoped to A-2 (MC1:413), A-2's readout and discard rules are [Q]
ingredients by the role test, and the operator-level rule caps at EOI-C.

**What the gate needs that CT lacks.** (1) A class consequence of the [Q] disclosure (MC1:409, 449): G1's fail column.
(2) G2–G5 and G0: CT has no observer, record, environment or sequence model; the operator-level rule supplies the
reduction. (3) A preregistered certifier for EOI-N (§6 (b)). CT's naming test and its controls CC-0 to CC-4 are
reused as G1's operator-level check and countercontrols.

***

### 3. Retrospective (planning classification only; the records are not edited)

| Unit | Already addresses | Assumptions under G2 / G3 / G4 (cited) | G0 / class |
|---|---|---|---|
| MATH-CON-1 (design) | G1: CT, class column, three statuses (MC1:337–452, 639–647) | G2/G4: A-2's readout (local Lüders, imported) and discard rules (MC1:170, 200). G3: "discard after uniform attach" (MC1:170) | No result. Reachable set {EOI-I, EOI-NEG, EOI-0} (§2) |
| P-CONTROL | G1: G-1, G-2 (PCD:99–103); L-7 imported (PCD:414); A-car supported only by L-7 (PCD:442) | G2: H-INT, embedded access via the operational interface, open (PCD:423). G4: records are rule (e), local Lüders (PCD:401). G3: hidden set `H` finite and preparation independence (posit), in the imitation class only (PCD:604, 618–620) | Null relative to base (b) (PCD:134–137, 326–333). Against the access model (a), K-10 and K-13, "control mediated by hidden memory", would be generative (PCD:134–137, 302): an interface-relative negative. Census null, not a protocol-class negative. EOI-NEG, within its class |
| P-MIX | G1: target-import grep (PMD:873–879). G5: S-CLASSICAL, a standing classical model (PMD:489) | G2: setting independence (PMD:336); coefficient loading supplied (PMD:364). G3: isolated pair, omitted modes spectators (PMD:365). G4: fresh record cell `ρ_0 = 0`, supplied (PMD:367); passive read after copy (PMD:330) | "Redundant at H1, inconclusive at H2" is the owner's Stage 1A recording decision (PMD:109, 236), not a Stage 1B result. Reachable set only |
| P-OBS | G2: LB-W, LB-S, sink content reaches a register only through the rule (POD:351–375). G4: record store separated from the physical register (POD:384–386). G5: branch by branch (POD:622) | G2: declared blank law, information axis (POD:356–361). G3: H-PS (POD:602); LB-F (POD:359); EXHAUST (POD:442). G4: RECORD-STORE, BLANK-SRC, SWAP-EXEC, TIMING supplied (POD:433–447) | LIMIT of the property definition, whose justification assumes terminal registration, which the construction removes by design (POD:116–124). Definition-level, not a protocol-class negative. EOI-NEG, within its class |
| M-INACC-1 | G1: C-IMPORT green (MIR:491–503). G2: knowledge `K` and access (MID:132, 398–404). G5: owner addendum and branch-by-branch rule (MID:25–29, 141–144) | G2: feedback executor supplied (MID:417, 607). G3: H-PS, correlated backgrounds outside both classes (MID:309, 605); fresh P2 refills (MID:361). G4: P1 archive (MID:357–360); complete joint record kept (MID:369) | Within its stated class (`G_σ`, `Π_A`, `Π_B`, P1, P2; MIR:91–96); existential; attributed to the gate of `G_σ` together with `Π_A`'s supplied resources (MIR:84–85), hence idealization-dependent on those; containment of the embedded class not stated by the record. H-PS in scope (MID:309–311); behaviour under correlated backgrounds not established. EOI-NEG |
| MECH-1 | G1: SC-1, CC-RECON (M1D:357, 378–381, 899). G2: SC-2 present and disclosed (M1D:900); O1 "supplied" (M1D:313–316, 929). G5: C-COMP K1–K6 (M1D:364–372) | G3: fresh cells with fixed laws (M1D:146); T′ converse uses `v_c` uniform and independent (M1D:107); hidden backgrounds outside R-W states not covered (M1D:508). G4: P1 (M1D:302); meter supply and terminality under CC-RECON (M1D:131), in the missing premise M1 only | Theorem W in R-W, a frame singled out by the comparator's covariance (M1D:899). The record's noncontextual model reproduces the record statistics (M1D:88–90, 901); claimed only as that imitable stabilizer fragment, with equality by C-COMP, G5 passes, and G2–G4 carry disclosed departures (P2, P3, H-PREP, uniform prior): EOI-C for that fragment. The CC-RECON items enter only the unadopted M1 |
| MECH-2 | G1: SC-1 (M2D:761). G2: SC-2, preparation supplied (M2D:762). G5: A5, A6, C-LEAK, Theorem NC (M2D:249–250, 261) | G3: H-LIFT (M2D:319–322), satisfiable by enlarging the carrier (M2D:346–347), its failure route analysed (M2D:728–733); hidden uniform cells supplied (M2D:207). G4: P1 not implemented; record keeps evolving (M2D:692–694) | U2 and NC: universal, within Lemma F's operation set and H-LIFT (M2D:50–52, 109–111); restricted by H-LIFT; containment of the embedded class not stated by the record. M2D:728 states "every nonclassical route at `q = 2`" without those qualifiers in the sentence; for the retrospective audit, not decided here. EOI-NEG |

Every unit discloses its G2–G4 assumptions as posits, hypotheses or supplied items, subject to the open M2D:728 item.
None reaches EOI-N, and none claims to. **Act 45** (R-I2), for G3's memory items: the kernel verdict holds for
trivial-ancilla dilations under the uniform initial law (A45:5). At the exact-arithmetic probe layer, replayed in CI and
not a kernel statement or part of the verdict, an ancilla carried between steps as hidden basis states separates two
dilations of one slice that agree on every column entering the slice, at two steps, while a tensor-factor ancilla does
not (A45:5, 38–39). Slice-determination therefore does not extend to a carried ancilla.

***

### 4. The outside analysis checked against the sources

| Claim (as relayed) | Finding |
|---|---|
| Principle 1 | Confirmed as a restatement of existing rules: CC-RECON (M1D:357), SC-1 (M1D:378), MC1's status "derived from native OI" (MC1:645). New content: G1's class consequence (§2 (1)) |
| Principle 2 | Confirmed in substance for M-INACC and P-OBS (MID:132, 398–404; POD:371). The "no later events" clause is new in wording; `K` "at a time" (MID:132) implies it there |
| Audit 1 (quantum import) | Largely existing: CT, SC-1, CC-RECON, C-IMPORT, G-1/G-2 |
| Audit 2 (embedded access) | Partly existing (SC-2, FB-EX, MID §3.6); no uniform decision table. H-INT is open (PCD:423). Consistent with the owner's statement that hidden reading is not the main risk: no reviewed unit has an undisclosed G2 failure |
| Audit 3 (hidden memory) | Not a labelling gap: the assumptions found are labelled (H-PS "Hypothesis", MID:605; H-LIFT a stated hypothesis, M2D:319). H-LIFT is not a memoryless-environment assumption (M2D:346–347, 728–733). The gap is prior dependence in scope sentences (R-I3) |
| Audit 4 (physical record) | Existing in P-OBS (POD:384–386, 433–447); elsewhere a labelled posit (P1) |
| Audit 5 (emergence vs matching) | Duplicates the owner addendum c.6714136234 (MID:25–29) and C-COMP (M1D:364–372); the imitation rule is the addition |
| Restricted-failure rule; three classes | Consistent with "State negative results only for the construction or class actually ruled out", one-sided as proposed (§5 K4); the classes are not a partition, completed in §1 |

***

### 5. Critical findings

- **K1. Partition.** The proposal's three classes leave negatives and no-result records unclassified; see §1.
- **K2. Reachability of EOI-N.** Closed on A-2 by G1 and the operator-level rule. Open in principle at configuration
  level, for a construction on a finite carrier under a fixed rule whose every preparation, registration, retention,
  reset and timing is executed by the rule; whose G3 inputs are framework posits other than a hidden prior, with any
  prior dependence shown for a preregistered prior class as in G3; and whose claimed item passes G5 against the fixed imitation
  class. No reviewed unit meets it, because each relies on supplied items: the named open inputs BLANK-SRC, SWAP-EXEC,
  RECORD-STORE and TIMING (POD:433–447), H-PREP (POD:603), and each unit's own supplied executors and P1/P2 (M1D:900;
  M2D:762; MID:417, 607). MC1 is capped by A-2 (MC1:170); P-CONTROL's L-3 to L-6 and P-MIX's coefficient loading,
  record cell and schedule are supplied (PCD:410–413; PMD:363–367). That is a finding about the present record. Comparator frames: R-W is comparator-chosen
  (M1D:899); R1 is AP1's fixed representation (M2D:761); §6 (d).
- **K3. Supplied executors.** Treating a supplied executor as a G2 fail would fail every unit (M1D:900; MID:607;
  POD:438); the execution axis makes it a disclosed departure.
- **K4. Direction of G0.** The proposal covers failures caused by restricting hidden resources, not failures produced
  by supplied observer capabilities, and not universal negatives over a class that contains the embedded class, which
  transfer a fortiori. M-INACC's exposure (MIR:84–85) is existential and uses supplied refills.
- **K5. Dependency trace for "restricted".** Without it any negative can be relabelled by citing some idealization.
  The owner direction requires a proof for a rescue claim; M-INACC shows a blocking premise can be vacuous: P-GK
  empties `Π_A` of nontrivial protocols (MIR:97–103).
- **K6. Labels by reference.** Ledger labels pass G3 when the conclusion cites the scope section that lists them
  (MIR:91–92 states `G_σ`, the classes, P1, P2; H-PS sits in MID:605).
- **K7. Derivation bars.** Requiring perfect retention or fresh ancillas to be derived would block every reviewed unit;
  none sources a retention mechanism (RECORD-STORE, POD:440–441). Disclosure suffices for EOI-C.
- **K8. Unbounded sequences.** "Whole accessible record sequences" uses M1D:372's finite-sequence standard.

***

### 6. Open questions for the owner

- **(a) MATH-CON-1-S1B-1.** Recommendation: option (i), no change to the round text. Frozen text 2 already states
  that "Hadamard is supplied by the polarization map, not derived" and that the round does not claim OI independently
  generates the quantum operation; a sentence carrying a gate label would put a planning attribute into a verification
  record (§1 Standing). By MC1:173–175 (A-5, A-7), the witness would fall under EOI-I; that reading, if the gate is
  adopted, is recorded in this planning record.
- **(b) Certifying EOI-N.** Proposal: scored only against a criterion frozen in the construction's preregistration
  before any result (the G1–G5 tables, the no-departure condition, and the §A.29 items: preserved results as
  controls, one independent prediction or postdiction, rejected variants); certified by an independent review of the
  result record against it, then a recorded owner decision. Otherwise at most EOI-C. A planning attribute only.
- **(c) Countercontrol for G0 labels.** Proposal: *restricted* and *idealization-dependent* need only the dependency
  trace at a named step, checked by the reviewer. The stronger claim that relaxing the restriction or removing the
  capability removes the failure needs a countercontrol: an exhibited construction without the failure, or a proof.
  Otherwise the record says "relaxation open".
- **(d) Comparator frames.** R-I4 settles A-2's imported Lüders and unitary items as never credited. Whether R-W or R1
  enters only the comparison map is a reviewer check per record. Open: is a claim stated in a comparator-chosen frame
  reported as relative to that frame?
- **(e) Placement.** Adopt as a planning criterion on #1169 only, or also require the G0–G5 tables in future OI↔QM
  preregistrations.

***

### 7. References off `main` (§A.42 item 8)

This comment lands nowhere on `main`. Each reference below whose content §2–§3 use is support off `main`: a gap,
acceptable for a planning comment and to be closed before any record on `main` relies on it.

| Reference | Use | Classification |
|---|---|---|
| MC1 at `41a42cb9` (#1206, open) | §2; §3 row | Support off `main` (gap) until #1206 lands |
| PCD, PMD, POD at the pinned heads (#1203–#1205, draft) | §3 rows | Support off `main` (gap) |
| S1B draft r5 (scratchpad, pre-`F`), its frozen texts | §6 (a) | Support off `main` (gap); may change before `F` |
| #1206, #1203, #1204, #1205 as identifiers | Locating the branches | Provenance |
| #1169 c.6714136234 (owner addendum) | §4 row 7 | Support on `main` (MID:25–29, paraphrase) |
| #1169 c.6721662886 (quoted in S1B frozen text 3) | §6 (a) context | Provenance; §6 (a) rests on frozen text 2, not on it |
| Owner chat direction 2026-11-08 (R-I1 to R-I4, "main risk", the three questions) | Standing; §1; §5 K5 | Provenance; verbatim as relayed; quoted with author and time from its #1169 record before posting |

***

### 8. Dispositions

Earlier reviews: §8 of `GATE-DRAFT-r2.md` and `GATE-DRAFT-r3.md`, with their own line numbers. The re-review of r3:

| Finding | Change in r4 (line numbers of this file) |
|---|---|
| R3-B1 | G3 pass clause replaced by the review's text verbatim (L69); K2 "shown for a preregistered prior class as in G3" (L180) |
| R3-B2 | Certification clause replaced by the review's text verbatim (L75–79); "on those equivalences" (L80) |
| R3-N1, R3-N2, R3-N2a, R3-N3 | K2 covers MC1, P-CONTROL and P-MIX (L183–184); (iv) distinguished from a hidden prior (L69); owner statement BRIEF-P2:51 cited at G0's *restricted* label (L94–95); G2 pass restores "the schedule" (L68) |
