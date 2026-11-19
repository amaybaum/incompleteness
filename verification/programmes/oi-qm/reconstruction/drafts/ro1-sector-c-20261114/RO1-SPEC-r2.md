# RO-1: paper-only specification of sector C, r2

**UNREVIEWED.** This is the second draft of the RO-1 specification. It is a specification and not a
proof. It establishes no result, adopts no premise, extension E or sector condition C, and changes no
Issue's scope, tier, readiness, authorization or writer.

**Revision.** r2 applies the independent review of r1 (`REVIEW-SPEC-r1.md`, REVISE at `7156d761`:
three blocking, seven major and twelve minor findings) and two additions relayed by the coordinator
from ChatGPT:
- test the PR countermodel clause by clause and name the exact missing restriction;
- no repair of C by quantum-set membership.

It also adds a statement, under O11, of whether physically equivalent descriptions can get different
membership decisions. Each finding was checked at source; the dispositions are in
`RESPONSE-SPEC-r1.md`. r1 (`RO1-SPEC-r1.md`, SHA-256
`d7f4380d2c2786a30f68b2d1776f5212ca11750192778e2fed3e2bde7e6a4341`) is left unchanged.

**Authority.** Owner decision on #914, c.6883249235 (`amaybaum`, 2026-11-14T19:48:13Z), item 1,
quoted verbatim: "I authorize Claude to proceed with the previously scoped paper-only sector-C
specification. The specification must preserve required coverage and soundness, with necessity
optional. It must not silently resolve an open scientific question or introduce a premise merely to
reproduce quantum predictions." The same item: "RO-1 (#1169) owns sector-C membership, physical
confinement grounds (S-J), closure under permitted operations and compositions (S-A), and
non-circularity"; "The shared model-identity and typing questions remain open." Item 3 governs
off-`main` citations and item 4 governs IC₂ (§§6.2, 9).

**Writer:** Claude Code. **Reviewer:** ChatGPT (#914 c.6883249235, writers table).

**Base.** `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`. Off-`main` sources at the exact
commits of §9. **Method:** reading only. No computation on OI rules, no Lean, no edit, no post.

**Labels.**
- **[R]** existing result, with its evidence state:
  - *main*: on `main`;
  - *reviewed, not merged*: draft PR at an exact reviewed commit;
  - *off-main record*: a planning or ledger draft on a branch, with its review state;
  - *outside the repository*: support held off GitHub;
  - *author-side*: unreviewed.
- **[P]** proposed obligation or definition. It binds nothing until reviewed and decided.
- **[A]** unproved assumption. **[A-inf]** marks an inference drawn in this note from cited results.
  It is unreviewed and treated as unproved.
- **[STOP Sn]** a point where going further would need an owner decision or would decide an open
  question. It is listed in §10 and is not resolved.

Owner decisions and planning rows are cited as records, not results.

**Outcome.** [P] §§2–5 state a frame for C: six clauses on #1143's tuple, a seventh clause K-X not yet
stated, a closure contract, and a decision rule (§8).

[A-inf] §7 checks the PR countermodel against the frame clause by clause. It meets five clauses as
stated. Whether it meets the sixth, K-acc, is an open availability question: its setting, use and
record programs are "specified, not derived" (SEL-EXCL-1 l. 46). So the control is **UNSOURCED**,
not a refutation.

[A-inf] If those programs are executable, the PR model meets all six clauses and fails soundness
under the proposed correspondence of §6.3. The missing restriction is then named exactly in §7.3.

[A-inf] The candidates for it found in a stated search are classified in §7.4. None is both
justified and shown to exclude PR while keeping the quantum Bell target.

The specification stops there (S2) and at seven other points (§10).

***

## 1. Requirements the specification must meet

Records, quoted. Each is a requirement on this text, not a result.

- **What C is.** "C applies to the underlying model. It should be a physically stated condition, with
  its consequences for experiment families defined explicitly" (#1169 c.6876591512, answer 1).
- **Coverage and soundness, not necessity.** "Require coverage and soundness. Necessity remains an
  optional future theorem. Models outside C may also reproduce quantum statistics. Membership in C
  need not characterize every possible quantum realization" (answer 2).
- **One model.** "One fixed model, with one common extension E, must support subsystems realizing
  every quantum carrier in the agreed scope … The ultimate model must accommodate arbitrarily large
  finite carriers, with the permitted encodings and resource requirements stated explicitly" (answer
  3); "one model that satisfies the necessary premises simultaneously" (#914 c.6877420015, item 4).
- **Access closure.** "Require quantum behaviour for every physically performable experiment within
  C. This includes accessible preparations, interventions, compositions and complete records under
  the retained contract. Access closure must prevent a model from qualifying through selected quantum
  experiments while also permitting stronger-than-quantum experiments" (answer 4).
- **Confinement and Bell.** The target "adds the obligation to state the sector condition C and
  justify it physically, including why observation is confined to that sector; for Bell this includes
  excluding stronger-than-quantum correlations in the physical sector, not in all of OI" (#914
  c.6875548603).
- **Non-circularity.** "Specify C independently of matching quantum statistics" (#914 c.6880010243,
  item 3). C "may not be chosen by testing whether the resulting correlations match quantum
  predictions" (#1060 body, BELL-QSET). The specification must not "introduce a premise merely to
  reproduce quantum predictions" (#914 c.6883249235, item 1).
- **No fitting per experiment.** "The two directions must use a compatible model and operational
  interface, not unrelated constructions selected separately for each experiment" (#914
  c.6875046763). "A single witness theory must match all operations and histories in scope,
  coherently" (#1143 body).
- **Carrier.** "the target cannot assume one fixed finite total carrier" (#914 c.6875046763).
- **Complex matrices.** "Allowed as a conditional mathematical input, not a physical explanation"
  (#914 c.6875046763, decision 4).

## 2. The object C is stated on

### 2.1 The tuple

[P] A **model** is a tuple `M = (S, φ, μ, Obs, Γ, R, Res)`:

| Component | Meaning | #1143 name |
|---|---|---|
| `S` | microscopic state space | `S` |
| `φ` | fixed dynamics on `S` | `φ` |
| `μ` | common initialization and source law | `μ` |
| `Obs` | embedded observer and readout maps | `E` |
| `Γ` | executable preparation, setting, intervention and continuation programs | `Γ` |
| `R` | typed complete records | `R` |
| `Res` | resource and renewal contract | `C` |

[R, reviewed, not merged] This is SEL-DISC-1's typing: "Write a candidate realization as
`(S, φ, μ, E, Γ, R, C)` … A mathematical response map is not a physical availability certificate"
(#1281 at `445b17f7`, ASSESSMENT.md l. 34). SEL-DISC-1 P6 (l. 54) writes the same `E` in `(φ, μ, E)`.

[P] Two components are renamed in this note only. No #1143 record is renamed.
- `C` becomes `Res`. This goes beyond the O12 convention of `RO1-OVERLAP-r3.md`, which is to name the
  other objects in full. The renaming serves the same purpose.
- `E` becomes `Obs`, because `E` also names the target's extension, OI + E (#914 c.6875046763).
  [A-inf] This second collision is not among those r3 lists; r3 §3 lists only the letter C.

[P] Notation only: the clauses below are named `K-…` so that they cannot be confused with the
observer conditions (C1)–(C4) of `papers/Main.md`. Whether (C1)–(C4) enter C as a clause is not
decided by this naming. They are a candidate ground (J2, §4) and a candidate for K-X (§7.4).

[P] A model realizes OI + E for some extension E fixed with the model. [R, main] No extension E is
adopted: "This is a characterization of a quantum-complete extension of OI, not a claim that bare OI
entails the added principles" (`papers/Main.md`:588). Record: no E is adopted (#914 c.6875548603).
[P] C is stated for every candidate E.

**[STOP S7, typing]** Two typing choices are left open, as owner item 1 requires: "The shared
model-identity and typing questions remain open".
- *Where E's additions live.* An extension may change `φ`. It may also add an operation, as the
  "empirical controllability resource" of `papers/Main.md`:588 does, or add access rules. These
  belong to `Γ` or `Obs`.
- *Whether `Γ` is a component or derived.* K-acc (§3) derives `Γ` from `(φ, Obs)`. The tuple of
  SEL-DISC-1 lists `Γ` as a component.

This draft states each clause so that it reads under either answer. Where it cannot, the clause
says so.

### 2.2 Reading of "a model in C"

[P] *Class reading.* C is a class of models: a condition on the tuple that each model satisfies or
fails. The experiment families of C are the complete-record laws of the programs in `Γ` of the models
in C. The records use this wording: "what puts a model in C" (#914 c.6880010243, item 3), "Models
outside C" (#1169 c.6876591512, answer 2), and "C applies to the underlying model" (answer 1).

[P] *Sector reading, the alternative.* C picks out a sector inside one model: some of its observers,
subsystems and programs. Answer 3's "subsystems realizing every quantum carrier" is compatible with
both readings.

The two readings differ on soundness (§6.3) and on what confinement must explain (§4). **[STOP S6]**
The choice is the owner's. Both are carried below.

### 2.3 The model-identity relation (O11): left open

[P] Membership is stated relative to an identity relation `≈` on models: when are two tuples the same
model? Its choice is left open (owner item 1; `RO1-OVERLAP-r3.md` §4.6). The candidates are:
- (i) equality of tuples, the finest relation;
- (ii) the two-sided gauge relation `G` of B4′;
- (iii) equality of complete-record laws over `Γ`;
- (iv) another relation, stated with its reason.

[R, main] (ii) and (iii) differ at B4′'s scope. `O_C ⇒ G` is disproved for the record classes C0,
C2-ch and C2-sel in the all-unitary class and in `PPer` at `|V|=2`, `|A|≥2`. G ⇒ O also fails for C2-ch
and C2-sel in the all-unitary class
(`verification/programmes/oi-qm/reconstruction/bsel-2-b4prime-20261105/B4PRIME.md`:19; Q2A and M-1
RESULT.md; #1143 body). These are model-reviewed hand derivations, not kernel-checked.

[P] Whatever `≈` is chosen, C must be `≈`-invariant: two `≈`-related models are both in C or both
outside it.

**Can physically equivalent descriptions get different membership decisions?** No relation of
physical equivalence is fixed in the records. [R, main] The corpus treats as equivalent, for its
finite-representative conclusions, the representatives "reached from it by relabelling the hidden
states, by such a finite decoupled enlargement" and, under the alphabet-size hypothesis, "by a change
of alphabet". This is stated where they are "expressible through the transition probabilities"
(`papers/Main.md`:724, item (ii)). Taking those as the physically equivalent descriptions [P]:

- **Under (i), yes.** A relabelling or a decoupled enlargement gives a different tuple, so the two
  descriptions get separate membership decisions. [A-inf] For relabelling, the clauses of §3 should
  give the same decision, because each is stated invariantly under bijections of `S`. A decoupled
  deep-sector enlargement changes `S` and `φ`, and K-dyn allows either. So agreement is expected,
  but it is not proved, and it is unchecked for K-acc and K-X.
- **Under (ii), yes in general.** [R, main] Lifts with equal complete-record laws need not be
  gauge-related (M-1, Q2A). So two descriptions that agree on every record of the given class can be
  different models under (ii), and can get different decisions if a clause reads more than records.
  Conversely, for C2-ch and C2-sel, gauge-related lifts can differ in record laws. A `G`-invariant C
  then cannot depend on those records. [A] Whether relabelling and decoupled enlargement fall
  under `G` is not stated in the sources read.
- **Under (iii), no for record-equivalent descriptions,** by construction. But a clause on `φ` or `S`
  is then well defined only if the record laws determine it. [R, main] "the response-table
  construction realizes arbitrary finite stochastic behavior" (`papers/Main.md`:598). [A-inf] So one
  record law has realizations that differ in `φ`, and K-dyn need not be `≈`-invariant under (iii).
- **Under (iv),** it depends on the relation stated.

**[STOP S1]** The choice of `≈` is the owner's. §3 states the clauses on tuples, which reads them
under (i) and fixes nothing. Under (ii) or (iii) each clause must be re-checked for invariance.

[P] *A proposed constraint for the owner, under S1:* `≈` should not identify two models whose
executable menus give different sets of performable experiments.
- [A-inf] *Reason:* access closure (answer 4). If `≈` identified a restricted-menu model, which passes
  soundness, with a full-menu model that fails it, then a `≈`-invariant C would admit both or neither.
  Admitting both lets the full-menu model qualify through selected experiments.
- *Effect:* this constraint narrows the open choice, excluding any relation coarser than equality of
  menus. It is proposed, not applied.

## 3. Statement of C: the clauses

[P] **Definition (frame).** `M ∈ C` iff `M` satisfies K-dyn, K-obs, K-src, K-acc, K-rec, K-res and
the clause K-X of §7.3. K-X is not yet stated.

| Clause | Constrains | Content | Status and source |
|---|---|---|---|
| **K-dyn** | `S`, `φ` | `φ` is one fixed deterministic bijection of `S`, the same for every program, fixed with the model. `S` need not be one fixed finite set | [P] It adopts posits. [R, main] `papers/Main.md`:42 gives `φ: S → S` with an observer `V ⊊ S`, not a bijection. Bijectivity is posit (iii) of the posit ledger, "part-empirical rather than a pure lemma" (`papers/Main.md`:724). Allowing a non-finite `S` departs from posit (ii), total finiteness of the representative (A1; `papers/Main.md`:724), as the target requires (#914 c.6875046763). [R, main] exact inclusion on one fixed finite carrier is obstructed (`papers/Main.md`:558). EXACT and the carrier inventory therefore bear on `S` (#1169 EXACT; #1055 RO-3). Where E's changes to `φ` sit is S7 |
| **K-obs** | `Obs` | Each observer is a proper subsystem with finitely many distinguishable internal states, coupled to the rest only through `φ`. Its records are read only through its own readout maps | [R, main] premise of the Definition (`papers/Main.md`:42). The clause quantifies over each observer, so it holds whether `Obs` is one interface or a family. Ledger Q1 bears on coverage (§6.3), not on this clause |
| **K-src** | `μ` | One common source law, fixed with the model before any setting is chosen. It is not refitted per experiment or per setting | [P] from the records of §1 ("No fitting per experiment"). Measurement independence (posit (xiv)) is not included. [R, main] measurement dependence is recorded as an alternative and not adopted (`papers/Main.md`:416–423). **[STOP S5]** Whether (xiv) and the hidden prior are admissible as posits is ledger Q8 (§9, ledger record) |
| **K-acc** | `Γ`, with `φ` and `Obs` | `Γ` is the set of programs that `M`'s own dynamics executes through `Obs`, closed under the contract of §5. Nothing `M` can execute is removed by declaration, and nothing it cannot execute is added | [P], new. It implements access closure (answer 4), following [R, reviewed, not merged] SEL-ACCESS-1's requirement to "source a nonpassive context switch in a single realization" (§4 item 2, at `1b966a03`). [A] "Executes through `Obs`" has no criterion until the availability questions are answered (S3), so the clause cannot yet be applied to a model. It is a typing choice (S7). §A.29 judgement: J7, §4 |
| **K-rec** | `R` | Records are complete accessible histories: raw calibrated outcomes, retained settings and controller data, readable workspaces, heralds, failures, clocks and stopping status. No subensemble is renormalized and no record is discarded before comparison | [P], reusing [R, reviewed, not merged] SEL-DISC-1 §2 l. 38 and §5.1 l. 91, and SEL-ACCESS-1 §1 item 2 |
| **K-res** | `Res` | Every source cell, renewal, reset, channel and reservoir a program uses is part of `M` and is counted, whether it is prepared in `μ` at the start or produced later | [P], reusing [R, reviewed, not merged] SEL-DISC-1 P5 (l. 53): a target-neutral accounting requirement, and "Scarcity alone is not a separator" |
| **K-X** | to be stated with its justification | a physically justified clause, stated first with its ground. The exclusion of PR, the 2√2 reference and the classical fragment are then tests it must pass under §8. They do not define it | **[STOP S2]**, §§7.3–7.4 |

[P] **Consequences for experiment families** (answer 1). An experiment of `M` is a program `g ∈ Γ`
run with the source law `μ`. Its outcome is the law of complete records `R` that `g` produces. The
experiment family of `M` is the set of these laws, one per program, with the program labels and
their structure kept: which observer runs which part, in what order, and with which messages. The
experiment family of C is the union over `M ∈ C`, keeping track of which model each law comes from.

[P] No clause of the frame refers to quantum statistics. Quantum-set membership is not, and may not
become, a clause or an assumption of C (§6.1). **[STOP S9]** Whether a clause may use quantum
kinematics (complex matrices, or the OI⁺ principles stated "within the same complex matrix
kinematics", `papers/Main.md`:584) as a conditional input is an owner question. Decision 4 allows
complex matrices "as a conditional mathematical input, not a physical explanation"
(#914 c.6875046763). r1's ban on such clauses is withdrawn as an unrecorded choice.

## 4. Confinement grounds (S-J)

[P] "What physically confines observation to C" has two parts, tied to S6.
- **Class reading.** Why the actual world is a model in C. That is: why its observers are embedded as
  K-obs says, why its menu is what K-acc says, and why K-X holds.
- **Sector reading.** Why observers cannot run programs outside the sector of their model.
- **Under both,** the Bell part is the ground of K-X: "for Bell this includes excluding
  stronger-than-quantum correlations in the physical sector" (#914 c.6875548603).

[A-inf] K-acc holds by definition, so it explains nothing about confinement. The physical content lies
in K-obs, in the availability facts behind K-acc (S3), and in K-X.

The table lists the candidate grounds found in the corpus and one new definitional item, J7. No
ground is derived here.

| # | Ground | Source | Status | Controls | Accountable Issue |
|---|---|---|---|---|---|
| J1 | Embedded finite observer: a proper subsystem with finite momentary capacity | `papers/Main.md`:42; Lemma 1, the stipulated finite-capacity clause (`papers/Main.md`:724, item (ii)) | [R, main] premise of bare OI | [R, reviewed, not merged] the weak package with an embedded cut admits a CHSH-4 model *under an assumed interface* (SEL-EXCL-1 §0 l. 22; l. 46); "the observer is finite" does not yield IC₂ (SEL-DISC-1 §7, ll. 155–157); the swap and visible-flip classical-access control (SEL-ACCESS-1 §2, ll. 53–69). The C0 countermodel is not cited: its proof is held outside the repository (SEL-ACCESS-1 ll. 26, 123; SEL-DISC-1 l. 30) | #1169 (S-J); tests: #1143 |
| J2 | Observer admission (C1)–(C4): the memory-bearing sector | `book/ch18-beyond.md`:64, 72; `papers/Main.md`:18, 78, 97 | [R, main] the diagnostics are kernel or paper results. Identifying the quantum–classical boundary with the (C1)–(C4) sector is "the framework's identification" at source (`book/ch18-beyond.md`:72) | [R, main] representability is universal and "does not distinguish the memory-bearing sector from an ordinary Markov process" (`papers/Main.md`:18). (C4) is met by "a pre-sampled hidden variable revealed by the history … (the response-table construction, §3.4)" (`papers/Main.md`:78). [A-inf] This suggests (C4) does not exclude response-table models, but no result tests (C1)–(C4) against PR | #1169 |
| J3 | Observers confined to the non-equilibrium phase | `papers/Main.md`:742–758 | [R, main] derived on paper, conditional on (EM) and `τ_mix ≪ τ_S`, using bounded coupling, finiteness of `S`, canonical typicality [31] and bounded coupling-graph diameter of `V` (`papers/Main.md`:742, 758) | It confines where observers exist, not which experiments they execute. No link to a quantum sector is stated. [A-inf] Its finiteness hypothesis conflicts with K-dyn's non-finite `S`, so a transfer is needed | #1169 for any use as an S-J ground; no Issue named for the result |
| J4 | Causal locality of the coupling graph | `papers/Main.md`:360 ("The selector in a Bell experiment is therefore causal locality, not representability"), 362, 364–389, 414 | [R, main] the cone is derived on paper for `S = ∏ S_i` with `V` and each `S_i` finite (:362). The ceiling CHSH ≤ 2 is a paper proof for a screened local completion under its hypotheses (i)–(iv): deterministic dynamics, product setting operations on disjoint regions, readouts outside the remote cone, and a common pre-setting ensemble (:366–376) | [R, main] as a clause it excludes PR and also the quantum Bell value under those hypotheses (:364–389). [R, reviewed, not merged] SEL-DISC-1 D4, P4 | #1060 (H-Bell, which would keep the target) |
| J5 | Common source independent of settings (measurement independence) | posit (xiv) (`papers/Main.md`:724); :416–423 | [R, main] posited | [R, reviewed, not merged] the fresh-cell PR model satisfies it (SEL-EXCL-1 §2, l. 67), so it is not sufficient for soundness | #1060 for the Bell route; ledger Q8 (S5) |
| J6 | An information or access principle, for example IC₂ | SEL-DISC-1 §5 | **open, home #1143.** Not derived here. [R, reviewed, not merged] "Not supplied" (D8) | Owner's four conditions (#914 c.6883249235, item 4; §6.2) | #1143 |
| J7 | K-acc: the executable menu is what the dynamics executes through the observer | this note; SEL-ACCESS-1 §4 item 2; #1143 c.6777830496 ("The program menu must be **derived from the apparatus/whole-world dynamics**", author-side) | [P] newly proposed, as a definition. **§A.29 judgement: not met.** (a) It is claimed to preserve the existing controls, but applying it to SEL-EXCL-1 is the open point of §7.2, so preservation is not shown. (b) It gives no independent prediction. (c) Until "executes through `Obs`" has a criterion (S3), it can be read to fit any outcome. So it is not a confinement ground and not a Layer-0 revision. It is kept only as the form access closure takes, pending S3 and S7 | Must not delete executable programs (SEL-MENU, SEL-ACCESS-1 §2 at `1b966a03`) | #1169 (S-A); availability: #866, #913 |
| J8 | A concrete observer-interface lift | #914 body, O-IF-SELECT row | [R, record] "blocked: no qualifying candidate in the bounded checked record" | — | #914 |
| J9 | Finite entropy or reservoir budget | SEL-DISC-1 §4 l. 79; P5 l. 53 | [R, reviewed, not merged] not a separator: fresh PR, fair classical records and deterministic realizations of independent fair quantum records need comparable entropy | — | #1143; renewal: #913 |

[R, reviewed, not merged] SEL-MENU applies to grounds that depend only on passive-law data, under its
hypotheses: the class contains a full/restricted-menu pair with the same passive data, and a required
operation has no alternative implementation in the restricted menu (SEL-ACCESS-1 §2, ll. 41–51 at
`1b966a03`). [A] Whether the actual OI class meets those hypotheses is open (#1143). [P] No ground is
excluded for being passive-law only. SEL-MENU is recorded as a control on J1–J3.

## 5. Closure contract (S-A) (proposed)

[P] `Γ` is closed under the following, each to the extent that `M`'s dynamics executes it (K-acc,
pending S3 and S7):

- **S-A1, sequence.** Run programs one after another, retaining all records.
- **S-A2, adaptivity.** Later settings may depend on the observer's own retained records and on
  private seeds.
- **S-A3, parallel composition.** Run programs on several observers or wings over a common source.
- **S-A4, reuse.** Use a carrier again after it has been read. Where the dynamics allows the
  continuation, it is in `Γ` and is not removed by declaration.
- **S-A5, renewal.** Fresh source cells come from preparation in `μ` at the start or from a renewal
  process executed later. Either way they are counted in `Res`.
- **S-A6, classical communication.** Send a classical message between observers with a stated
  alphabet, budget and schedule, if a channel is executable. Arrival times, flags and side channels
  count toward the budget.
- **S-A7, later joint readout.** Bring the records of several observers together after the run.
  Joined correlations are not local signalling (SEL-DISC-1 §2, l. 38).

### 5.1 Programs named by #1143 controls

The question for each program is "In `Γ`?". Programs are members of `Γ`, not of C.

| Program | In `Γ`? | What it presupposes | Home of the availability question |
|---|---|---|---|
| **Single-use test**: setting actuation on each wing, one use of the gate, raw readout | [P] In `Γ` iff `M` executes the setting writes, with setting sources independent of the unused source, a clock and the readout | Setting actuation and sources, clock, readout. [R, reviewed, not merged] "This interface is **specified, not derived from the native OI/SM dynamics**" (SEL-EXCL-1 l. 46); the interface is "UNSOURCED" (l. 129) | #866 |
| **Fresh-cell use**: a fresh independent cell and blank outputs for each use, on a fixed finite schedule (SEL-EXCL-1 §3) | [P] In `Γ` iff the cells are prepared or renewed within `M` and counted (S-A5, K-res) | Preparation or renewal of independent cells. [R, reviewed, not merged] the bank grows with the chosen finite horizon (SEL-DISC-1 P5, l. 53) | #913 (O-REUSE), #866 |
| **Same-seed reuse**: a second setting and use on the same cell, the first output retained (SEL-EXCL-1 §7) | [P] In `Γ` whenever executable (S-A4). It cannot be excluded by declaration | Record retention, a second setting actuation and a clock on the same carrier | #913, #866 |
| **One-bit message**: two independent input bits, one use, one fixed-schedule classical bit (SEL-DISC-1 §5.1) | [P] In `Γ` iff a channel with that budget and the input sources are executable (S-A6) | Channel apparatus, input sources, clock. [R, reviewed, not merged] "The appended channel is a mathematical operational extension" (SEL-DISC-1 l. 95) | #866 |
| **Probe of a source cell** (`r` or an unused cell) | [P] In `Γ` whenever executable. The fresh-cell lemma does not cover it (SEL-EXCL-1 l. 97; SEL-DISC-1 l. 71) | Read access to the source register | #866 |
| **Arbitrary choice of source index** | [P] As above (SEL-EXCL-1 l. 91; SEL-DISC-1 l. 71) | Addressable source bank | #866, #913 |
| **Unilateral stop or ready request that changes the remote clock or success field** | [P] As above (SEL-EXCL-1 l. 91; SEL-DISC-1 l. 71) | Cross-wing control fields | #866 |

[A] Whether any of these is executable in any OI model is unsourced: "Physical source remains NOT
PASSED" (#914 c.6883249235). **[STOP S3]** The contract states what membership presupposes. It does
not supply availability.

## 6. Non-circularity, coverage and soundness

### 6.1 Non-circularity and no repair by quantum-set membership

[P] The frame's clauses refer only to `S`, `φ`, `μ`, `Obs`, `Γ`, `R` and `Res`. None refers to quantum
statistics. K-X must meet the same test.

[P] A clause is rejected if its only stated justification is the outcome of a control in §8.

[P] C is not repaired by adding quantum-set membership, or any equivalent condition, as a clause or an
assumption. [R, reviewed, not merged] "Admit precisely quantum/Tsirelson-compatible tables" is
"Circular as an OI derivation" (SEL-DISC-1 P7, l. 55).

[P] Any new restriction needs an independent physical justification under §A.29, stated before any
control is applied. It must preserve the existing controls of §8, deliver at least one independent
prediction beyond the problem, and not be open to adjustment to fit any outcome. Until it meets
these, it is recorded as a stop.

### 6.2 IC₂

[P] IC₂ is not a clause of C. Under the owner's decision, "IC₂ may enter the physical definition of C
only if its justification is independently motivated by OI's dynamics, observer interface or another
physically defensible principle". It requires: "A source-first explanation, not selected because IC₂
excludes PR correlations"; "An executable native protocol with explicit preparations, inputs,
controls, communication budget and accessible records"; "A stated prediction or consequence beyond
matching quantum statistics"; "Independent review and the applicable §A.29 controls". "Until these
conditions are met, IC₂ remains a conditional discriminator, not an established physical selection
law" (#914 c.6883249235, item 4).

[R, reviewed, not merged] None of the four is met: the native principle is "Not supplied" (SEL-DISC-1
D8), and the protocol's availability is an added hypothesis (l. 95). [P] IC₂ appears here only in §8,
as a test.

### 6.3 What coverage and soundness would require on one common model

[P] **The correspondence `Θ`.** Coverage and soundness compare a model's experiments with finite
quantum experiments through one map `Θ`, fixed for the whole model. `Θ` must preserve structure:
- (a) each observer, or wing, maps to its own quantum subsystem, and that observer's local programs
  map to local instruments on that subsystem;
- (b) parallel composition (S-A3) maps to the composite system, and the common source maps to one
  initial state, independent of the settings;
- (c) sequence and adaptivity (S-A1, S-A2) map to composition of instruments conditioned on retained
  records;
- (d) a classical message (S-A6) maps to a classical channel with the same alphabet, budget and
  schedule;
- (e) complete records, failures included, map to complete outcome records;
- (f) exogenous settings map to exogenous settings.

[R, reviewed, not merged] The sources' comparisons assume such a map. SEL-EXCL-1 l. 81 speaks of "the
corresponding bipartite dichotomic Bell scenario". SEL-DISC-1 D7 rests on local quantum instruments,
an input-independent shared state and one classical bit (ll. 129, 190). SEL-ACCESS-1 §1 item 4 speaks
of "a predeclared family of finite-dimensional preparations, instruments, compositions and complete
histories".

[A-inf] Without `Θ`, any finite conditional table, PR's included, is the law of some finite quantum
experiment, for example one device that takes `(x, y)` jointly. So soundness would exclude nothing.

[P] `Θ` constrains the quantum comparison class. It is not a clause of C and refers to no OI-side
quantum statistics, so §6.1 is unaffected. **[STOP S8]** Adopting `Θ` as the meaning of "quantum" in
answers 2 and 4 is an owner decision about the target's comparison class.

[P] **Coverage.** There is one model `M* ∈ C`, with one `φ`, one extension E, one `μ` and one stated
`Obs`, and one `Θ`, such that every experiment of every finite quantum experiment family in the agreed
scope is the `Θ`-image of a program `g ∈ Γ(M*)` with the same complete-record law. The agreed scope
includes arbitrarily large finite carriers (answer 3). Each program has a stated encoding and
resource budget. `Θ` is one map for the whole scope, not chosen per experiment. Exact equality is the
ultimate target; an approximation with stated error is a separate milestone (#914 c.6875046763,
decision 2).
- Ledger Q1 (one observer interface, or a stated family of nested partitions) bears on "one stated
  `Obs`" here (§9, ledger record). It is a coverage dependency, not a clause.

[P] **Soundness.**
- *Class reading.* For every `M ∈ C` and every `g ∈ Γ(M)`, the complete-record law of `g` equals that
  of a finite quantum experiment `Θ(g)`, with one `Θ` for all of `Γ(M)`. Access closure applies:
  `Γ(M)` is the full executable menu, not a selected part.
- *Sector reading.* Replace "every `g ∈ Γ(M)`" by "every `g` in the sector of `M`". Then `M*`'s sector
  must contain the programs used for coverage.

[P] **Necessity** would say that every OI model whose experiments are quantum lies in C. It is an
optional future theorem (#1169 c.6876591512, answer 2; #914 c.6878200172). This specification does not
assert it and does not depend on it.

[R, main] Related results on `main`:
- an extension characterization, "OI⁺ ⟺ exact finite endomorphic operational QM" on every nonempty
  finite carrier, kernel-checked (`papers/Main.md`:584–588);
- approximate inclusion to accuracy ε by one finite reversible realization (`papers/Main.md`:596–598);
- exact inclusion on one fixed finite carrier is obstructed (`papers/Main.md`:558).

[R, off-main record] The ledger records coverage and soundness for a C as an unresolved obligation
(LEDGER:139, A-QM, "UO"). [A-inf] No result read here proves either for any stated C.

## 7. The PR countermodel against the frame

### 7.1 Status of the check

[P] This section is a conditional check, not a verdict under §8. §8 applies only to a complete C,
frozen with K-X and a choice of `≈` (step 1). Neither exists. The check assumes the class reading (S6)
and reads the clauses on tuples (S1, reading (i)).

### 7.2 Clause by clause

[A-inf] The model is SEL-EXCL-1's: `T(x,y,r,A,B) = (x,y,r, A⊕r, B⊕r⊕(x∧y))`, one fair source cell per
use, a declared local access grammar (SEL-EXCL-1 §1, ll. 28–46; SEL-DISC-1 §4, ll. 61–69). The
closure rules of §5 are applied with it.

| Clause | Does the PR model meet it? | Basis |
|---|---|---|
| K-dyn | **Yes.** `T` is a fixed reversible map, with `T² = id` on all configurations | SEL-DISC-1 l. 65 |
| K-obs | **Yes.** Each wing holds finite local registers; neither reads `r` or the remote registers | SEL-EXCL-1 l. 44 |
| K-src | **Yes.** One common fair source, "the **same** for every setting" | SEL-EXCL-1 l. 67 |
| K-acc | **Open.** `T` leaves `x, y` unchanged and executes no setting program. The setting writes, setting sources, clock and readout are "specified, not derived", and the access restriction is "**assumed** rather than OI-derived" | SEL-EXCL-1 ll. 46, 129, 150. Whether they are in `Γ` is S3 |
| K-rec | **Yes, conditionally.** Complete local histories with an always-success flag, if the programs are in `Γ` | SEL-EXCL-1 ll. 67, 91 |
| K-res | **Yes, conditionally.** A finite cell bank for each declared horizon, prepared in `μ` and counted (S-A5) | SEL-EXCL-1 l. 87; SEL-DISC-1 P5 |

The closure rules give the following, with every program under K-acc open.
- **Single-use test.** [R, reviewed, not merged] If it is in `Γ`, its CHSH value is 4 (SEL-EXCL-1 §2).
  [A-inf] Under `Θ` (a)–(b), its two wings map to two quantum subsystems with local instruments on a
  setting-independent state. The table then lies outside the quantum correlation set. [R, reviewed,
  not merged] It "exceeds the quantum Tsirelson maximum 2√2 for the corresponding bipartite
  dichotomic Bell scenario" (SEL-EXCL-1 l. 81).
- **Same-seed reuse.** [R, reviewed, not merged] If it is in `Γ`, Bob's complete local history depends
  on Alice's second setting (SEL-EXCL-1 §7; SEL-DISC-1 D3). [A-inf] Under `Θ` (a), (c) and (e), local
  instruments with no message give complete local-history no-signalling. This is the quantum
  reference of SEL-DISC-1 §6.3 (l. 149), so the history has no `Θ`-image.
- **One-bit message.** [R, reviewed, not merged] If it is in `Γ`, `J = 2` (SEL-DISC-1 D5). Under `Θ`
  (a), (b) and (d), the quantum comparator gives `J ≤ 1` (D7). [A-inf] So the history has no
  `Θ`-image.

**Verdict of the check, conditional.** [A-inf] The PR model meets K-dyn, K-obs and K-src. It meets
K-rec and K-res given its programs. K-acc is UNSOURCED (§8 step 2), so the control is UNSOURCED.

*If* its single-use test is in `Γ`, then:
- it meets all six clauses;
- the frame without K-X admits a model that fails soundness under `Θ`, under the class reading.

Under the sector reading, the conclusion holds only if the sector of a model containing the PR gate
must contain the single-use test (S6).

### 7.3 The missing restriction, named

[P] *If* the single-use test is in `Γ`, the frame is incomplete at the following restriction `R*`. It
is the condition K-X must state.

`R*` is a condition on `(φ, μ, Obs, Γ)`, stated without quantum statistics and justified under
§A.29, such that:
- (a) the PR model's tuple fails `R*`;
- (b) some model whose `Γ` contains a two-wing test with the reference value CHSH = 2√2 and an ordinary
  repeatable classical fragment satisfies `R*`, with fair marginals and a setting-independent common
  source (SEL-DISC-1 §6.3);
- (c) `R*` meets §6.1.

[A-inf] Pointwise parameter independence together with K-src's common source and determinism gives
local response functions. [R, main] Then CHSH ≤ 2 (`papers/Main.md`:364–389; SEL-ACCESS-1 §3, ll.
96–102). [A-inf] So `R*` cannot be pointwise parameter independence. A deterministic model meeting (b)
must keep some dependence of a wing's response on the remote setting, or on a source that depends on
it. `R*` must therefore limit the form or extent of that dependence, not forbid it.

**[STOP S2]** This draft does not state `R*`. Choosing a route to it is the owner's (see §7.4).
- *Q7* asks whether supraquantum exclusion is met through H-Bell or stated on C directly (LEDGER:937,
  off-main record; #1060).
- If an information principle such as IC₂ is proposed, whether it is native is the scientific question
  O4, homed at #1143. It is not an owner decision.
- [P] Following r3 owner question 6, the next revision can present conditional variants of C, one per
  route, each with its consequences, without choosing.

### 7.4 Candidates for K-X, over a stated search

**Search.** `papers/Main.md` §§3.3–3.4 (ll. 18, 78, 97, 360–427) and ll. 584–598; `papers/Substratum.md`
ll. 131–133; SEL-ACCESS-1 §3; SEL-DISC-1 §3; LEDGER §§1–3 (off-main record).

[A-inf] The classification below is over this search only. It is not a claim about the whole corpus.

| Candidate | Excludes PR? | Keeps the 2√2 target and a classical fragment? | Status |
|---|---|---|---|
| Bell-local response factorization with measurement independence (J4 without H-Bell; SEL-DISC-1 P4). Full span of preparable latent laws (P3) | Yes | No | [R, main] `papers/Main.md`:364–389; [R, reviewed, not merged] SEL-DISC-1 D4. Fails coverage |
| (C1)–(C4) (J2) | Untested. [R, main] (C4) is met by a pre-sampled hidden variable in the response-table construction (`papers/Main.md`:78) | Untested | No result |
| OI⁺ principles: observational independence, reversible richness, observer recursion. Their primitive-source form: implementation locality, phase-free richness, embedded observation. Their substratum-source form | Not stated as a test against PR. [A-inf] An exact characterization of operational QM on a finite carrier excludes PR tables on that carrier, if the PR model's operations satisfy the principles' hypotheses | [R, main] equivalent to exact finite operational QM on every nonempty finite carrier, kernel-checked (`papers/Main.md`:584–588) | Stated "within the same complex matrix kinematics" (:584). In the substratum-source form, the continuously tunable state-mixing operation is "an empirical controllability resource" and the phases are "a stated intervention principle rather than a consequence" (:588). Their admissibility as a clause of C is S9. Physical sourcing is NOT PASSED |
| Candidate E: an operationally pure joint preparation with a mixed local marginal (SEL-ACCESS-1 §3, l. 81) | Untested on PR | [R, outside the repository] the restricted affine C1 model satisfies E, keeps classical contexts and fails CHSH > 2 under its stated locality premises (SEL-ACCESS-1 l. 81) | The support is held outside the repository (SEL-ACCESS-1 ll. 26, 123) |
| IC₂ (J6) | Yes, for the fresh one-use PR, if the one-bit protocol is in `Γ` (SEL-DISC-1 §5.2, l. 107) | [R, reviewed, not merged] the classical-local and quantum-local references satisfy it (D6, D7) | Barred as a clause until the four conditions of item 4 are met. Open, home #1143 (O4) |
| Preparation-indexed adjacency with H-Bell (J4 with H-Bell) | **No, as stated.** Its clauses are (i) parameter dependence, (ii) operational no-signalling and (iii) a metric/Ollivier–Ricci stability condition (`papers/Substratum.md`:133). The PR model has (i) and (ii). (iii) is a continuum-geometry condition, and no result applies it to PR | It is a route to keeping the target with a Bell-local reference graph (:131) | [R, main] open (#1060). It is not a PR-excluding candidate |
| The measurement-dependent alternative | **No.** CHSH ≤ min{4, 2 + 4√(2 ln 2 · I_ont)} allows 4 | — | [R, main] recorded, not adopted (`papers/Main.md`:416–423). It bears on ledger Q8 (S5), not on Q7 |

[A-inf] Within the search, no candidate is both physically justified as a clause of C and shown to
exclude PR while keeping the 2√2 target and a classical fragment.
- The OI⁺ principles come nearest. Their use as a clause depends on S9, and on physical sourcing of
  their posited inputs.
- (C1)–(C4) and E are untested.

## 8. Decision rule (proposed)

[P] **Proposed.** It is preregistered as a rule, not as expected outcomes (§A.29). It applies only to a
complete statement of C: K-X stated with its justification, `≈` chosen, the reading of §2.2 fixed and
`Θ` adopted.

1. **Freeze first.** Record C's clauses, `≈`, the reading, `Θ`, the closure contract and each clause's
   justification before any control is applied. A later change to C is a new revision and repeats
   step 1.
2. **Membership and availability.** For each control model, decide clause by clause whether it is in
   C. For each control program, decide by §5 whether it is in `Γ`. If that depends on an unsourced
   availability question, record the control as UNSOURCED, not as passed or failed.
3. **Classical control.** Exhibit a model in C whose `Γ` contains a nontrivial repeatable classical
   measurement fragment with valid complete records. The control is green only when such a model is
   exhibited with its programs in `Γ`. If no model in C can have one, C is REJECTED (classical
   preservation). If availability is open, the control is UNSOURCED, and no verdict is printed over
   it (§A.29).
4. **Quantum references.** If a clause, by its content, excludes every model realizing a quantum
   reference in scope through `Θ`, C FAILS COVERAGE. This covers CHSH 2√2 with independent settings, and
   an ordinary shared classical bit (SEL-DISC-1 §6.3). Passing does not establish coverage.
5. **PR countercontrol.** If the PR model is in C with its single-use test in `Γ`, C FAILS SOUNDNESS
   under `Θ` (§7.2). If it is excluded, name the excluding clause and check its step-1 justification.
   A clause justified only by excluding PR fails §6.1 and is rejected.
6. **Reuse menus.** If same-seed reuse is in `Γ` of a model in C containing the PR gate, its complete
   local history has no `Θ`-image, and C FAILS SOUNDNESS. If only fresh-cell use is in `Γ`, step 5
   decides.
7. **IC₂ as a test.** If the one-bit protocol is in `Γ` of a model in C, compare its `J` with the bound
   `J ≤ 1`. That bound holds for `Θ`-images under the comparator premises of SEL-DISC-1 §6.2, which are
   quantum premises used only for the comparison. `J > 1` is a soundness failure. IC₂ is used here as a
   falsifier, not as a law of C (§6.2).
8. **Verdicts.** One of SUPPORTED, REFUTED, INCONCLUSIVE or UNSOURCED, at the tested scope (#1143 body).
   The verdict text is generated from steps 2–7. A verdict over a control that is not green is void.
   Passing all controls is SUPPORTED for those controls only. It does not establish soundness or
   coverage, which are universal statements (§6.3). No classification moves by re-narration (§A.22).

[P] §7 is not an application of this rule: C is not complete.

## 9. Off-`main` citations

Under #914 c.6883249235 item 3, each source below is cited at its exact reviewed commit, with "its
proven scope". "The §A.42 support-off-main gap remains until the relevant content is integrated
through its own gates. Citing these results does not establish physical availability or authorize
their adoption as premises."

| Source | Exact commit and file | Review | Scope cited here |
|---|---|---|---|
| SEL-ACCESS-1, #1224 | `1b966a0383e1dabe867d41816ee9743e99502938`, `verification/programmes/oi-qm/reconstruction/oiqmsel-access-20261110/SELECTION-ACCESS-1.md`, blob `5c125be576fd9552acabe891ff851fa19046fc3a` | Full review ACCEPT WITH NITS at `ea8827ff`; focused ACCEPT at `1b966a03` (#1224 reviews 5840425454, 5840851253). **Reviewed, not merged.** The file's status line at this commit still reads "FOCUSED DIFF CHECK PENDING" (l. 5); SEL-DISC-1 l. 26 records such headings as stale | SEL-MENU (§2); the swap and visible-flip classical control (§2); §4's minimum obligations; candidate E as stated in §3, whose support is held outside the repository (ll. 26, 123) |
| SEL-EXCL-1, #1228 | `0ecfddeb89540aedf1e2dc3ae7c377516641066c`, `verification/programmes/oi-qm/reconstruction/oiqmsel-exclusion-20261110/SEL-EXCL-1.md`, blob `1e8892ff94a8f0dcf306e3f43cd57e951a446ca7` | Full review ACCEPT WITH NITS at `4813bc0b`; focused ACCEPT at `0ecfddeb` (#1228 reviews 5845436861, 5848321039). **Reviewed, not merged.** In-file status lines are stale (ll. 7, 132, 192) | The reversible PR model with CHSH 4 under its specified interface; fresh-cell no-signalling within its declared grammar; same-seed reuse signalling in the enlarged grammar |
| SEL-DISC-1, #1281 | `445b17f7f808c0b8b5ff82da34fb3a0f474ceaaa`, `verification/programmes/oi-qm/reconstruction/selection-discriminator-20261113/ASSESSMENT.md`, blob `ccf2d46d889a640f37fdeaec1e92164d7e026d3f` (unchanged at `37e19f3d`) | Non-author ACCEPT 5897727347 and ChatGPT ACCEPT 5898055055 at `445b17f7`; publication ACCEPT at `37e19f3d` (5898298958, 5901719219). **Reviewed, not merged.** The documentary child `3c445e6c` changes only l. 3 and awaits focused review; line numbers are the same at all three commits | The tuple; P0–P7; D1–D8; IC₂ as a conditional discriminator; the classical and quantum references |

**Other off-`main` records cited.** These are planning or ledger drafts, cited as records and not as
results. Owner item 3 does not cover them.
- **LEDGER.** `LEDGER-r8.md` on `origin/records/unified-ledger-914-20261114` at
  `9ff3b8d913abfe720273ff162f6340054cb69437`
  (`verification/programmes/oi-qm/reconstruction/drafts/unified-ledger-20261114/`). Its header reads
  "UNREVIEWED" (l. 3), while `REVIEW-r8.md` records ACCEPT. The branch README reads "UNREVIEWED — NOT
  AUTHORITATIVE". Cited for A-QM (l. 139), Q1 (l. 931), Q7 (l. 937) and Q8 (l. 938).
- **The overlap note.** `RO1-OVERLAP-r3.md` on PR #1294, accepted by ChatGPT (PR #1294 review
  5906337770) and adopted as the split by #914 c.6883249235.

**Outside the repository.** The C0/C1 constructions and candidate E's supporting proof are held on
pages outside the repository (SEL-ACCESS-1 ll. 26, 123). SEL-DISC-1 l. 30 records that "Their complete
original independent review artifacts were not recovered".

[P] **The §A.42 item 8 gap.** Every statement here marked *reviewed, not merged*, *off-main record* or
*outside the repository* is supported off `main`. No such statement is established (§A.46 item 1).
Any statement built on one carries the same gap until that content lands. This includes every
[A-inf] in §§6.3, 7 and 8 that uses one.

## 10. Stops and owner questions

None of these is resolved here.

| Stop | Question | Why stating C meets it | Issue that keeps it open |
|---|---|---|---|
| **S1** | Which relation `≈` identifies models for membership (O11)? Should the proposed constraint of §2.3 (do not identify models whose menus differ) be adopted? | The choice decides which clauses are admissible. Physically equivalent descriptions can get different decisions under (i) and (ii) (§2.3) | Shared interface: #1143 supplies the relations; the choice for C is the owner's |
| **S2** | Which route states `R*` / K-X? Q7: through H-Bell, or stated on C directly? An information principle (IC₂)? The OI⁺ principles (with S9)? (C1)–(C4)? Present conditional variants instead? | K-X cannot be stated without it (§§7.3–7.4) | #1060 (Q7, H-Bell); #1143 (O4, scientific); ledger Q7 under #914 |
| **S3** | Are the programs of §5.1, the single-use test included, executable in any OI model (O10)? What criterion gives "executes through `Obs`"? | K-acc cannot be applied without it; the PR check (§7.2) is UNSOURCED | #866, #913 |
| **S5** | Ledger Q8: are measurement independence (xiv) and the hidden prior admissible as posits? | Whether K-src may include (xiv); J5 | #914 (ledger Q8); #1060 for the Bell route |
| **S6** | Class reading or sector reading of "a model in C"? | Soundness, confinement and the PR check change with it (§§2.2, 4, 6.3, 7.2) | Owner; a reading of the target |
| **S7** | Typing: where E's additions live (`φ`, `Γ` or `Obs`), and whether `Γ` is a component or derived from `(φ, Obs)` | K-dyn and K-acc depend on it (§2.1) | Shared interface, per owner item 1 |
| **S8** | Adopt the structure-preserving correspondence `Θ` as the meaning of "quantum" in coverage and soundness? | Without it, soundness excludes nothing (§6.3) | #914 (A-QM) |
| **S9** | May a clause of C use quantum kinematics, such as complex matrices or the OI⁺ principles, as a conditional input (decision 4)? | It decides whether the OI⁺ route can supply K-X (§§3, 7.4) | Owner; #914 |

S4 of r1 (ledger Q1) is withdrawn as a stop. K-obs holds under either answer. Q1 bears on coverage
(§6.3) and stays with #914.

Kept open where r3 placed them, and not met by any stop:
- whether passive-law grounds can ever suffice (#1143), recorded only as a control (§4);
- whether coverage or soundness holds for any C (#914, A-QM).

[P] **Next step, proposed.** After review, the owner's answers to S1, S2 and S6–S9 are needed to state
K-X and a complete C. S3 is needed before any control can be green. Without them, r2 stands as the
frame, the closure contract, the correspondence `Θ` and the decision rule, with C incomplete.
