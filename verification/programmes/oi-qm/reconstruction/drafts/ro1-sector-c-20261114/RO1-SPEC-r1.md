# RO-1: paper-only specification of sector C, r1

**UNREVIEWED.** This is the writer's first draft of the RO-1 specification. It is a specification and
not a proof. It establishes no result, adopts no premise, extension E or sector condition C, and
changes no Issue's scope, tier, readiness, authorization or writer.

**Authority.** Owner decision on #914, c.6883249235 (`amaybaum`, 2026-11-14T19:48:13Z), item 1,
quoted verbatim: "I authorize Claude to proceed with the previously scoped paper-only sector-C
specification. The specification must preserve required coverage and soundness, with necessity
optional. It must not silently resolve an open scientific question or introduce a premise merely to
reproduce quantum predictions." The split it adopts is that of `RO1-OVERLAP-r3.md`: "RO-1 (#1169)
owns sector-C membership, physical confinement grounds (S-J), closure under permitted operations and
compositions (S-A), and non-circularity" (same item). Item 3 governs off-`main` citations and item 4
governs IC₂ (§§6, 9).

**Writer:** Claude Code. **Reviewer:** ChatGPT (#914 c.6883249235, writers table).

**Base.** `origin/main` `dfeec843bec08443b25cffe34d33dc8401c3b604`; the ledger branch
`origin/records/unified-ledger-914-20261114` at `9ff3b8d913abfe720273ff162f6340054cb69437` (LEDGER =
`LEDGER-r8.md` in `verification/programmes/oi-qm/reconstruction/drafts/unified-ledger-20261114/`).
Off-`main` sources at the exact reviewed commits of §9. **Method:** reading only. No computation on OI
rules, no Lean, no edit, no post.

**Labels.** Every statement of substance carries one:
- **[R]** existing result, with its evidence state: *main* (on `main`), *reviewed, not merged* (draft
  PR at an exact reviewed commit), or *author-side* (unreviewed).
- **[P]** proposed obligation or definition. It binds nothing until reviewed and decided.
- **[A]** unproved assumption. **[A-inf]** marks an inference drawn in this note from cited results.
  It is unreviewed and is treated as unproved until reviewed.
- **[STOP]** a point where going further would decide an open question. The question is listed in
  §10 and is not resolved.

Owner decisions and planning rows are cited as records. They are not results.

**Outcome in one paragraph.** [P] §§2–5 state C as a conjunction of clauses on #1143's tuple, with a
closure contract and a decision rule. [A-inf] Applied under that rule, the clauses that the corpus
can support today admit the reversible PR countercontrol (§7), so they cannot yet be sound. Every
candidate for the missing clause either loses the quantum Bell target, or is IC₂, which item 4 bars
until its conditions are met, or depends on Q7. The specification therefore stops at that clause
(§7.3), and also at the choice of the model-identity relation (§2.3). §10 lists every stop for the
owner.

***

## 1. Requirements the specification must meet

These are records, quoted. Each is a requirement on this text, not a result.

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
  predictions" (#1060 body, BELL-QSET).
- **No fitting per experiment.** "The two directions must use a compatible model and operational
  interface, not unrelated constructions selected separately for each experiment" (#914
  c.6875046763). "A single witness theory must match all operations and histories in scope,
  coherently" (#1143 body).
- **Carrier.** "the target cannot assume one fixed finite total carrier" (#914 c.6875046763).

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
(#1281 at `445b17f7`, ASSESSMENT.md l. 34).

[P] Two components are renamed here only, and no #1143 record is renamed. The tuple's `C` becomes
`Res`, by the O12 convention (`RO1-OVERLAP-r3.md` §3). The tuple's `E` becomes `Obs`, because `E` also
names the target's extension (OI + E, #914 c.6875046763). [R, main] The second collision is new: r3
§3 lists only the letter C. A third collision is noted for readers. The observer conditions (C1)–(C4)
of `papers/Main.md` are not clauses of C. The clauses below are named `K-…` to keep them apart.

[P] A model is a realization of OI + E for some extension E that is fixed with the model. [R, record]
No extension E is adopted (LEDGER:506; #914 c.6875548603). [P] So C is stated for every candidate E.
Choosing E is not part of RO-1.

### 2.2 Reading of "a model in C"

[P] C is read as a **class of models**: a condition on the tuple that each model satisfies or fails.
The experiment families of C are the complete-record laws of the programs in `Γ` of the models in C.
This reading follows the records' own wording: "what puts a model in C" (#914 c.6880010243, item 3),
"Models outside C" (#1169 c.6876591512, answer 2), and "C applies to the underlying model" (answer 1).

[A] An alternative reading takes C as a sector inside one model, picking out some of its subsystems
and programs. Answer 3's "subsystems realizing every quantum carrier" is compatible with both. The
two readings differ on soundness. Under the class reading, every performable experiment of a model in
C must be quantum. Under the sector reading, only those in the sector must be. Both coverage and
soundness are stated for the class reading in §6, with the sector variant noted. The choice is
listed for the owner (§10, S6). It is a reading of the target's wording, not a scientific question.

### 2.3 The model-identity relation (O11): left open

[P] Membership is stated relative to an identity relation `≈` on models: when are two tuples the same
model? Its choice is left open (`RO1-OVERLAP-r3.md` §4.6; #914 c.6883249235, item 1: "The shared
model-identity and typing questions remain open"). The candidates are:

- (i) equality of tuples, the finest relation;
- (ii) the two-sided gauge relation `G` of B4′;
- (iii) equality of complete-record laws over `Γ`;
- (iv) another relation, stated with its reason.

[R, main] (ii) and (iii) differ. `O_C ⇒ G` is disproved for record classes C0, C2-ch and C2-sel in the
all-unitary class and in `PPer` at `|V|=2`, `|A|≥2`
(`verification/programmes/oi-qm/reconstruction/bsel-2-b4prime-20261105/B4PRIME.md`:19; Q2A and M-1
RESULT.md). These are model-reviewed hand derivations, not kernel-checked.

[P] Whatever `≈` is chosen, C must be `≈`-invariant: two `≈`-related models are both in C or both
outside it.

[P] `≈` must not identify two models whose executable menus `Γ` give different sets of performable
experiments. [A-inf] The reason is access closure. If `≈` identified a restricted-menu model, which
passes soundness, with a full-menu model that fails it, then a `≈`-invariant C would have to admit or
reject both. Admitting both lets the full-menu model qualify through the restricted model's selected
experiments, which answer 4 forbids.

[A-inf] Under (iii), clauses on `φ` or `S` are well defined on classes only if complete-record laws
determine them. [R, main] In general they do not: "the response-table construction realizes
arbitrary finite stochastic behavior" (`papers/Main.md`:598), so one record law has many
realizations. [A-inf] So the choice of `≈` changes which clauses of §3 are admissible.

**[STOP S1]** §3 states the clauses on tuples, as under (i). This fixes nothing. Under (ii) or (iii),
each clause must be re-checked for `≈`-invariance, and K-dyn and K-obs may fail it. The choice is the
owner's (§10).

## 3. Statement of C: the clauses

[P] **Definition (frame).** `M ∈ C` iff `M` satisfies K-dyn, K-obs, K-src, K-acc, K-rec, K-res and
the clause K-X of §7.3. K-X is not yet stated.

| Clause | Constrains | Content | Status and source |
|---|---|---|---|
| **K-dyn** | `S`, `φ` | `φ` is one fixed deterministic bijection of `S`, the same for every program. It includes whatever E adds, fixed in advance. `S` need not be one fixed finite set | [R, main] Bare-OI premise: observation is a triple `(S, φ, V)` (`papers/Main.md`:42); bijectivity is part-empirical and the measure is posited (LEDGER §2.2). Record: no fixed finite total carrier (#914 c.6875046763). [R, main] exact inclusion on one fixed finite carrier is obstructed (`papers/Main.md`:558; LEDGER §2.1), so EXACT and the carrier inventory bear on `S` (#1169 EXACT; #1055 RO-3) |
| **K-obs** | `Obs` | Each observer is a proper subsystem with finitely many distinguishable internal states, coupled to the rest only through `φ`. Its records are read only through its own readout maps | [R, main] premise (`papers/Main.md`:42). [STOP S4] whether `Obs` is one interface or a stated family of nested partitions is ledger Q1 (LEDGER:931), not decided here |
| **K-src** | `μ` | One common source law, fixed with the model before any setting is chosen. It is not refitted per experiment or per setting | [P] from the records of §1 ("No fitting per experiment"). Measurement independence (ledger (xiv)) is **not** included. [R, main] it is posited (LEDGER §3.3), and a measurement-dependent Bell alternative is recorded and not adopted (`papers/Main.md`:416–423). Including (xiv) would choose between Bell routes, which is part of Q7 (§7.3). [STOP S5] whether (xiv) and the hidden prior are admissible as posits is ledger Q8 (LEDGER:938) |
| **K-acc** | `Γ`, with `φ` and `Obs` | `Γ` is the set of programs that `M`'s own dynamics executes through `Obs`, closed under the contract of §5. It is not a menu stipulated beside the dynamics: nothing `M` can execute is removed by declaration, and nothing it cannot execute is added | [P], new (judged under §A.29 at J7, §4). It implements access closure (answer 4). It follows SEL-ACCESS-1's requirement to "source a nonpassive context switch in a single realization" (§4 item 2 at `1b966a03`) [R, reviewed, not merged] |
| **K-rec** | `R` | Records are complete accessible histories: raw calibrated outcomes, retained settings and controller data, readable workspaces, heralds, failures, clocks and stopping status. No subensemble is renormalized and no record is discarded before comparison | [P], reusing [R, reviewed, not merged] SEL-DISC-1 §2 l. 38 and §5.1 l. 91, and SEL-ACCESS-1 §1 item 2 |
| **K-res** | `Res` | Every source cell, renewal, reset, channel and reservoir a program uses is part of `M` and is counted | [P], reusing [R, reviewed, not merged] SEL-DISC-1 P5 (l. 53): a target-neutral accounting requirement, "Scarcity alone is not a separator" |
| **K-X** | not yet fixed | the clause that excludes stronger-than-quantum behaviour while keeping the quantum Bell target | **[STOP S2]**, §7.3 |

[P] **Consequences for experiment families** (answer 1). An experiment of `M` is a program `g ∈ Γ`
run with the source law `μ`, and its outcome is the law of complete records `R` that `g` produces.
The experiment family of `M` is the set of these laws, one per program, with the program labels kept.
The experiment family of C is the union over `M ∈ C`, keeping track of which model each law comes
from.

[P] No clause mentions a Hilbert space, a density operator, the Born or trace rule, a Tsirelson value,
or a quantum correlation set (§6.1).

## 4. Confinement grounds (S-J)

"What physically confines observation to C" is read as follows [P]. It is the physical reason why
the observers of the world are embedded as K-obs says, and why the programs they can execute are only
those of K-acc. The table lists every candidate ground found in the corpus, and one new definitional
item (J7). No ground is derived here.

| # | Ground | Source | Status | Controls | Accountable Issue |
|---|---|---|---|---|---|
| J1 | Embedded finite observer: a proper subsystem with finite momentary capacity | `papers/Main.md`:42; Lemma 1, stipulated finite capacity (LEDGER §2.2) | [R, main] premise of bare OI | [R, reviewed, not merged] the weak package with an embedded cut admits PR (SEL-EXCL-1, #1228 at `0ecfddeb`, §0 l. 22); "the observer is finite" does not yield IC₂ (SEL-DISC-1 §7, ll. 155–157); C0 classical countermodel (SEL-ACCESS-1 §3) | #1169 (S-J); tests: #1143 |
| J2 | Observer admission (C1)–(C4): the memory-bearing sector | `book/ch18-beyond.md`:64, 72; `papers/Main.md`:18, 97 | [R, main] the diagnostics are kernel or paper results. Identifying the quantum–classical boundary with the (C1)–(C4) sector is a proposed explanation at source (LEDGER B-P4-QCB-1, l. 380) | [R, main] representability is universal and "does not distinguish the memory-bearing sector from an ordinary Markov process" (`papers/Main.md`:18). No result says whether (C1)–(C4) excludes PR | #1169 |
| J3 | Observers confined to the non-equilibrium phase | `papers/Main.md`:742–758; LEDGER B-P4-AOT-2, l. 360 | [R, main] derived on paper, conditional on (EM), `τ_mix ≪ τ_S`, the one-step-channel description and bounded diameter of `V` | It confines where observers exist, not which experiments they can execute. No link to a quantum sector is stated | #1169 for any use as an S-J ground; LEDGER names no Issue for the result |
| J4 | Causal locality of the coupling graph | `papers/Main.md`:360 ("The selector in a Bell experiment is therefore causal locality, not representability"), 362 (causal cone), 364–389 (Bell ceiling), 414 | [R, main] the cone is derived on paper; the ceiling CHSH ≤ 2 for a screened local completion is a paper proof under (viii) and (xiv) | [R, main] as a clause it excludes PR and also the quantum Bell value (LEDGER §3.1); [R, reviewed, not merged] SEL-DISC-1 D4 and P4. Keeping the quantum Bell target needs H-Bell, which is open | #1060 (H-Bell) |
| J5 | Common source independent of settings (measurement independence) | ledger (xiv), LEDGER §3.3; `papers/Main.md`:416–423 | [R, main] posited | [R, reviewed, not merged] the fresh-cell PR model satisfies it (SEL-EXCL-1 §2, l. 67), so it is insufficient for soundness | #1060 for the Bell route; ledger Q8 under #914 |
| J6 | An information or access principle, for example IC₂ | SEL-DISC-1 §5 | **open, home #1143.** Not derived here. [R, reviewed, not merged] "Not supplied" (D8) | Owner's four conditions (#914 c.6883249235, item 4; §6.2) | #1143 |
| J7 | K-acc: the executable menu is what the dynamics executes through the observer | this note; SEL-ACCESS-1 §4 item 2; #1143 c.6777830496 ("The program menu must be **derived from the apparatus/whole-world dynamics**", author-side) | [P] newly proposed, as a definition. **§A.29 judgement:** it preserves every existing control listed in §8 and adds no quantum element. It delivers no independent prediction beyond the problem, so it does not qualify as a Layer-0 revision or as a confinement ground on its own. It is kept as a definition that access closure requires | Must not delete executable programs (SEL-MENU, SEL-ACCESS-1 §2 at `1b966a03`) | #1169 (S-A); availability: #866, #913 |
| J8 | A concrete observer-interface lift | #914 body, O-IF-SELECT row | [R, record] "blocked: no qualifying candidate in the bounded checked record" | — | #914 |
| J9 | Finite entropy or reservoir budget | SEL-DISC-1 §4 l. 79; P5 l. 53 | [R, reviewed, not merged] not a separator: fresh PR, fair classical records and deterministic realizations of independent fair quantum records need comparable entropy | — | #1143; renewal: #913 |

[R, reviewed, not merged] SEL-MENU applies to any ground that depends only on passive-law data, under
its hypotheses: the class contains a full/restricted-menu pair with the same passive data, and a
required operation has no alternative implementation in the restricted menu (SEL-ACCESS-1 §2, ll.
41–51 at `1b966a03`). [A] Whether the actual OI class meets those hypotheses is open (#1143;
`RO1-OVERLAP-r3.md` §4.6). [P] No ground in the table is excluded for being passive-law only. SEL-MENU
is recorded as a control on J1–J3.

## 5. Closure contract (S-A)

[P] `Γ` is closed under the following, each to the extent that `M`'s dynamics executes it (K-acc):

- **S-A1, sequence.** Run programs one after another, retaining all records.
- **S-A2, adaptivity.** Later settings may depend on the observer's own retained records and on
  private seeds.
- **S-A3, parallel composition.** Run programs on several observers or wings over a common source.
- **S-A4, reuse.** Use a carrier again after it has been read. Where the dynamics allows the
  continuation, it is in `Γ` and is not removed by declaration.
- **S-A5, renewal.** Fresh source cells come only from an executed renewal or preparation process in
  `M`, counted in `Res`.
- **S-A6, classical communication.** Send a classical message between observers with a stated
  alphabet, budget and schedule, if a channel is executable. Arrival times, flags and side channels
  count toward the budget.
- **S-A7, later joint readout.** Bring the records of several observers together after the run.
  Joined correlations are not local signalling (SEL-DISC-1 §2, l. 38).

### 5.1 The #1143 countercontrol continuations

| Continuation | Inside C? | What the contract presupposes | Home of the availability question |
|---|---|---|---|
| **Fresh-cell use**: a fresh independent source cell and blank outputs for each use, on a fixed finite schedule (SEL-EXCL-1 §3) | [P] Inside iff the cell bank and its renewal are part of `M` and executed (S-A5, K-res) | A physical source or renewal process for independent cells, counted in `Res`. [R, reviewed, not merged] the bank grows with the chosen finite horizon (SEL-DISC-1 P5, l. 53) | #913 (O-REUSE, renewal), #866 (preparation) |
| **Same-seed reuse**: a second setting and use on the same hidden cell, with the first output retained (SEL-EXCL-1 §7) | [P] Inside whenever the continuation is executable (S-A4). It cannot be excluded by declaration | Record retention, a second setting actuation and a clock on the same carrier | #913 (O-REUSE), #866 (record, clock, controller) |
| **One-bit message**: two independent input bits, one device use, one fixed-schedule classical bit (SEL-DISC-1 §5.1) | [P] Inside iff a classical channel with that budget and the input sources are executable (S-A6) | A channel apparatus, independent input sources and a clock. [R, reviewed, not merged] "The appended channel is a mathematical operational extension, to be source-certified if tested physically" (SEL-DISC-1 l. 95) | #866 (apparatus, inputs, clock) |

[R, reviewed, not merged] In the PR model, same-seed reuse signals in complete local histories
(SEL-EXCL-1 §7; SEL-DISC-1 D3). The one-bit protocol gives `J = 2` (SEL-DISC-1 D5).

[A-inf] So any model in C that contains the PR gate and can execute either continuation fails
soundness through that continuation (§8). If neither continuation is executable, the contract yields
no conclusion.

[A] Whether these operations are executable in any OI model is unsourced. "Physical source remains
NOT PASSED" (#914 c.6883249235). The contract states what membership presupposes. It does not supply
availability.

## 6. Non-circularity, coverage and soundness

### 6.1 Non-circularity

[P] The clauses of §3 refer only to `S`, `φ`, `μ`, `Obs`, `Γ`, `R` and `Res`. None refers to quantum
statistics (§3, last paragraph). K-X must meet the same test.

[P] A clause is rejected if its only stated justification is the outcome of a control in §8.

[R, reviewed, not merged] "Admit precisely quantum/Tsirelson-compatible tables" is "Circular as an OI
derivation" (SEL-DISC-1 P7, l. 55).

### 6.2 IC₂

[P] IC₂ is not a clause of C. Under the owner's decision, "IC₂ may enter the physical definition of C
only if its justification is independently motivated by OI's dynamics, observer interface or
another physically defensible principle". It requires: "A source-first explanation, not selected
because IC₂ excludes PR correlations"; "An executable native protocol with explicit preparations,
inputs, controls, communication budget and accessible records"; "A stated prediction or consequence
beyond matching quantum statistics"; "Independent review and the applicable §A.29 controls". "Until
these conditions are met, IC₂ remains a conditional discriminator, not an established physical
selection law" (#914 c.6883249235, item 4).

[R, reviewed, not merged] None of the four is met. The native principle is "Not supplied" (SEL-DISC-1
D8), and the protocol's availability is an added hypothesis (l. 95).

[P] Here IC₂ appears only in the decision rule, as one control (§8).

### 6.3 What coverage and soundness would require on one common model

These are stated for the class reading of §2.2.

[P] **Coverage.** There is one model `M* ∈ C`, with one `φ`, one extension E, one `μ` and one stated
`Obs`, with the following property. For every finite quantum experiment family `Q` in the agreed
scope there is a program `g ∈ Γ(M*)`, with a stated encoding and resource budget, whose complete-record
law equals `Q`'s law. The agreed scope includes arbitrarily large finite carriers (answer 3). The
program correspondence `Q ↦ g` is one map for the whole scope. It is not chosen per experiment, and it
respects sequence, adaptivity and composition (S-A1 to S-A3). Exact equality is the ultimate target;
an approximation with stated error is a separate milestone (#914 c.6875046763, decision 2).

[P] **Soundness.** For every `M ∈ C` and every program `g ∈ Γ(M)`, the complete-record law of `g`
equals that of some finite quantum experiment, under one program correspondence for the whole of
`Γ(M)`. Access closure applies: `Γ(M)` is the full executable menu of K-acc, not a selected part. Under
the sector reading of §2.2, the quantifier "every `g ∈ Γ(M)`" is replaced by "every `g` in the sector
of `M`", and `M*`'s sector must contain the programs of coverage.

[P] **Necessity** would say that every OI model whose experiments are quantum lies in C. It is an
optional future theorem (#1169 c.6876591512, answer 2; #914 c.6878200172). This specification does not
assert it and does not depend on it.

[R, main] Neither coverage nor soundness is proved for any C (LEDGER:139, A-QM, UO). Related results
on `main`:
- an extension characterization, OI⁺ ⟺ exact finite endomorphic operational QM, which is not a
  sector result (LEDGER:155; `papers/Main.md`:584–588);
- approximate inclusion to accuracy ε by one finite reversible realization (`papers/Main.md`:596–598);
- exact inclusion on one fixed finite carrier is obstructed (`papers/Main.md`:558).

[A-inf] These bear on coverage through K-dyn's carrier. They do not bear on soundness.

## 7. Applying the frame to the existing controls, and the stop

### 7.1 Classical and quantum references

[A-inf] Nothing in K-dyn to K-res forbids a model whose `Γ` contains ordinary repeatable classical
measurements. This is what the classical-preservation control asks (SEL-ACCESS-1 §4 item 3; SEL-DISC-1
D6, §6.3).

[A-inf] No clause of the frame forbids quantum Bell behaviour by its content.

[R, main] No OI model realizing the quantum Bell value with a sourced mechanism is known: "No
mechanism is stated in the corpus" (LEDGER §3.3).

### 7.2 PR countercontrol

[A-inf] The SEL-EXCL-1 model satisfies every clause from K-dyn to K-res:
- K-dyn: it is a fixed reversible map (`T² = id`, SEL-DISC-1 §4 l. 65);
- K-obs: each wing has finite local registers and no access to `r` or the remote registers (SEL-EXCL-1
  §1, l. 44);
- K-src: one common fair source, the same for every setting (SEL-EXCL-1 §2, l. 67);
- K-rec: complete local histories, with an always-success flag;
- K-res: a finite bank for each declared horizon.

[A-inf] Under K-acc its programs are executed by `T` itself, so `Γ` contains the single-use Bell test,
whose CHSH value is 4 [R, reviewed, not merged, SEL-EXCL-1 §2]. [R, main] "the same reversible
response-table construction that realizes arbitrary finite stochastic laws also realizes PR-box
behavior" (`papers/Main.md`:360).

[A-inf] Under the decision rule of §8, the frame without K-X is therefore REFUTED as a sound C. It
admits a model with a supraquantum performable experiment. This holds whatever the continuations of
§5.1 are, because the single-use test needs none of them.

### 7.3 The missing clause K-X, and the stop

[P] K-X must:
- exclude the PR countercontrol (or exclude its membership in C);
- keep the quantum Bell target and the classical contexts;
- meet §6.1.

[R] Every candidate in the corpus falls into one of five kinds:

| Candidate for K-X | Effect | Status |
|---|---|---|
| Bell-local response factorization with measurement independence (J4 without H-Bell; SEL-DISC-1 P4); full span of preparable latent laws (P3) | Excludes PR, and also the quantum Bell value | [R, main] `papers/Main.md`:364–389; [R, reviewed, not merged] SEL-DISC-1 D4. Rejected: it fails coverage |
| IC₂ or another information principle (J6) | Excludes the fresh one-use PR if the one-bit protocol is executable (SEL-DISC-1 §5.2, l. 107) | Barred until the four conditions of item 4 are met. Open, home #1143 (O4) |
| Preparation-indexed adjacency with H-Bell (J4 with H-Bell) | Would keep the quantum value with setting-independent remote marginals | [R, main] H-Bell is open (LEDGER §3.1; `papers/Substratum.md`:131–133); #1060 |
| The measurement-dependent alternative | CHSH ≤ min{4, 2 + 4√(2 ln 2 · I_ont)} | [R, main] recorded, not adopted (`papers/Main.md`:416–423) |
| A supraquantum exclusion stated on C directly | — | No non-circular statement exists. Which of this row and the H-Bell row is the route is ledger Q7 (LEDGER:937) |

**[STOP S2]** Fixing K-X would decide Q7, between the H-Bell route and an exclusion stated on C
directly (`RO1-OVERLAP-r3.md` §4.6, Q7 row; #1060). If IC₂ were chosen, it would also decide O4 (#1143).
The specification stops here. K-X is left unstated, and C is incomplete.

## 8. Decision rule (proposed)

[P] **Proposed.** Preregistered as a rule, not as expected outcomes (§A.29). It applies to any
complete statement of C, which needs K-X and a choice of `≈`.

1. **Freeze first.** Record C's clauses, the choice of `≈`, the reading of §2.2, the closure contract
   and each clause's justification, before any control is applied. A later change to C is a new
   revision and repeats step 1.
2. **Membership of each control model.** For each control model, decide clause by clause whether it
   is in C. For each control program, decide by §5 whether it is in `Γ`. If a control program's
   executability depends on an unsourced availability question, record that control as UNSOURCED, not
   as passed.
3. **Classical control.** C must admit a model whose `Γ` contains a nontrivial repeatable classical
   measurement fragment, with valid complete records. If it does not, C is REJECTED (classical
   preservation).
4. **Quantum references.** If a clause of C, by its content, excludes every model realizing a quantum
   reference in scope, C FAILS COVERAGE. This holds for the CHSH value 2√2 with independent settings,
   and for an ordinary shared classical bit (SEL-DISC-1 §6.3). Matching a reference does not establish
   coverage.
5. **PR countercontrol.** If the PR model is in C, C FAILS SOUNDNESS at that scope. If it is excluded,
   name the clause that excludes it and check its step-1 justification. A clause justified only by
   excluding PR fails §6.1 and is rejected.
6. **Reuse menus.** If same-seed reuse is in `Γ` of a model in C containing the PR gate, its
   complete-history signalling is a soundness failure. If only fresh-cell use is in `Γ`, step 5
   decides.
7. **IC₂ as a test.** If the one-bit protocol is in `Γ` of a model in C, compare its `J` with the
   quantum comparator's bound `J ≤ 1`. That bound holds under the comparator's premises of SEL-DISC-1
   §6.2, which are quantum premises used only for the comparison. `J > 1` is a soundness failure. This
   uses IC₂'s inequality as a falsifier derived from the quantum comparator, not as a law of C (§6.2).
8. **Verdicts.** One of SUPPORTED, REFUTED, INCONCLUSIVE or UNSOURCED, at the tested scope (#1143
   body). The verdict text is generated from steps 2–7. Passing all controls is SUPPORTED for those
   controls only. It does not establish soundness or coverage, which are universal statements (§6.3).
   No control result moves C's classification by re-narration (§A.22).

[A-inf] §7.2 applies steps 2 and 5 to the frame without K-X.

## 9. Off-`main` citations

Each source below is a reviewed result on a draft pull request that is not merged. Under #914
c.6883249235 item 3, each is cited at its exact reviewed commit, with "its proven scope". "The §A.42
support-off-main gap remains until the relevant content is integrated through its own gates. Citing
these results does not establish physical availability or authorize their adoption as premises."

| Source | Exact reviewed commit and file | Review | Scope cited here |
|---|---|---|---|
| SEL-ACCESS-1, #1224 | `1b966a0383e1dabe867d41816ee9743e99502938`, `verification/programmes/oi-qm/reconstruction/oiqmsel-access-20261110/SELECTION-ACCESS-1.md`, blob `5c125be576fd9552acabe891ff851fa19046fc3a` | Full review ACCEPT WITH NITS at `ea8827ff`; focused ACCEPT at `1b966a03` (#1224 reviews 5840425454, 5840851253; #1143 c.6765757859). **Reviewed, not merged.** The file's own status line at this commit still reads "FOCUSED DIFF CHECK PENDING" (l. 5); SEL-DISC-1 l. 26 records that such headings are stale at accepted commits | SEL-MENU as a conditional obstruction (§2); the classical-preservation control; §4's minimum obligations |
| SEL-EXCL-1, #1228 | `0ecfddeb89540aedf1e2dc3ae7c377516641066c`, `verification/programmes/oi-qm/reconstruction/oiqmsel-exclusion-20261110/SEL-EXCL-1.md`, blob `1e8892ff94a8f0dcf306e3f43cd57e951a446ca7` | Full review ACCEPT WITH NITS at `4813bc0b`; focused ACCEPT at `0ecfddeb` (#1228 reviews 5845436861, 5848321039). **Reviewed, not merged** | The reversible PR model with CHSH 4; fresh-cell no-signalling within its declared grammar; same-seed reuse signalling in the enlarged grammar. Its in-file status lines are likewise stale at this commit |
| SEL-DISC-1, #1281 | `445b17f7f808c0b8b5ff82da34fb3a0f474ceaaa`, `verification/programmes/oi-qm/reconstruction/selection-discriminator-20261113/ASSESSMENT.md`, blob `ccf2d46d889a640f37fdeaec1e92164d7e026d3f` (unchanged at publication child `37e19f3d`) | Non-author ACCEPT (5897727347) and ChatGPT ACCEPT (5898055055) at `445b17f7`; publication ACCEPT at `37e19f3d` (5898298958, 5901719219). **Reviewed, not merged.** The later documentary child `3c445e6c` changes only l. 3 and awaits focused review (#1281 c.6875713759); line numbers here are the same at all three commits | The tuple; P0–P7; D1–D8; IC₂ as a conditional discriminator; the classical and quantum references |

[P] The §A.42 item 8 gap: every statement of this note marked "reviewed, not merged" is supported
off `main`. No such statement is established (§A.46 item 1). Any statement built on one, including
every [A-inf] in §§5, 7 and 8 that uses them, carries the same gap until that content lands.

## 10. Stops and owner questions

Each stop is a point where the specification would otherwise decide an open question. None is
resolved here.

| Stop | Question | Why stating C meets it | Issue that keeps it open |
|---|---|---|---|
| **S1** | Which relation `≈` identifies models for membership (O11)? | The choice of `≈` decides which clauses are admissible (§2.3) | Shared interface; #1143 supplies the relations, #1169 the choice for C |
| **S2** | Q7: is supraquantum exclusion met through H-Bell, or stated on C directly? And, if IC₂, is it native (O4)? | K-X cannot be stated without it (§7.3) | #1060 (Q7, H-Bell); #1143 (O4); ledger Q7 under #914 |
| **S3** | Are the operations of §5.1 executable in any OI model (O10)? | Membership of the control programs, and so step 2 of §8, depends on it | #866, #913 |
| **S4** | Ledger Q1: one observer interface, or a stated family of nested partitions? | K-obs depends on it | #914 (ledger Q1) |
| **S5** | Ledger Q8: are measurement independence (xiv) and the hidden prior admissible as posits? | J5, and whether K-src may include (xiv) | #914 (ledger Q8); #1060 for the Bell route |
| **S6** | Class reading or sector reading of "a model in C" (§2.2)? | Soundness has a different quantifier under each | Owner; a reading of the target, not a scientific question |

Not met by this draft, and kept open where r3 placed them:
- Whether passive-law grounds can ever suffice (#1143). Recorded only as a control in §4.
- Whether coverage or soundness holds for any C (#914, A-QM).

[P] **Next step, proposed.** After review, the owner's answers to S1, S2 and S6 are the minimum
needed to state K-X and a complete C. Without them, r1 stands as the frame, the closure contract and
the decision rule, with C incomplete.
