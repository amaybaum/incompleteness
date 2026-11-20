# TUNE-1, Step 3A: the candidates Step 2 left open, their specification, and the tests they can face

**Standing: WIP / UNVERIFIED author report, r3 adds §2A (owner decision #1236 c.6847314661);
review edits E1–E7 applied, awaiting confirmation.** r3 is r2 (`TUNE-1-STEP3A-r2.md`, git blob
`17076ef7`, the version accepted after the recheck, unchanged) with §2A added, the reformulated
central question recorded in §1, a terminology pointer in §1, and change-map rows in §11. The focused
review of r3 ("Review of r3 (§2A)" in `REVIEW-STEP3A.md`, ACCEPT WITH CHANGES) required E1–E7 and nits
n1–n4, all applied in place; the pre-review text is `.r3-pre-review.md`. Nothing else differs. r1 (`TUNE-1-STEP3A.md`, sha256
prefix `914f2339b24d8a40`) is unchanged. The independent
review `REVIEW-STEP3A.md` (same model family, ACCEPT WITH CHANGES) required R1–R7 and minor edits
m1–m4, with R8 optional; §10 maps each item to its place here. Paper-only: reading and hand
derivations. No computation on any OI rule (no script, numerics or enumeration), no Lean execution,
no manuscript or Lean edit, no premise adopted, no claim promoted, nothing committed, pushed or
posted. A ChatGPT review follows before the owner. Step 3B is not authorized and nothing here
evaluates a candidate against the Born rule, Kochen–Specker contextuality or Bell correlations beyond
defining the tests.

**Writer.** This Claude session (owner record below).

**Pins.**
- `origin/main` = `080cd2be4b4d8220dd6527e2c0641f0b4f8bb47d` (2026-11-13). At r2, `origin/main` is
  `62bdc2cf`; `git diff --stat 080cd2be 62bdc2cf` is empty on the TUNE-1 directory and on
  `papers/Main.md`, so every citation below holds at both. The TUNE-1 records are
  on `main` under `verification/programmes/oi-qm/reconstruction/drafts/tune-1-20261111/`; the last
  commit touching them is `59557ee8`. Line numbers below are at `080cd2be`. Main lines are cited at
  `080cd2be`; Step 2 cites Main at the Step 1 pin `cac5d264`, where each cited line is two higher.
- The proposal file at `080cd2be` has sha256 prefix `2a081101efae469b`, the hash approved at M0
  (#1236 c.6816189419).
- OA-1 r5, OA-2 r4, OA-3 r4 and W1-1 r4: branch `research/oa1-w1-1-20261112` at
  `2d064a71d9a637c8b1d7983f91cdff2a6357a87b` (draft PR #1265). **Off `main`.** They are cited as
  provenance and context with their exact scope (§A.42 item 8, §A.46 item 7). No conclusion here
  uses them as established support; where a classification below rests on one, it says so and
  carries the OA result's hypotheses.

**Citation forms.** `P:n` = `TUNE-1-STEP2-PROPOSAL.md`; `AF:n` = `TUNE-1-STEP2-AMENDMENT-1-final.md`;
`AF1:n` = its addendum 1; `S3:n`, `S4:n` = `TUNE-1-STEP2-SESSION3.md`, `-SESSION4.md`; `T1:n` =
`TUNE-1-STEP1.md` (all in the TUNE-1 directory on `main`). `OA1:n`, `OA2:n`, `OA3:n`, `W11:n` = the
off-`main` reports `OA-1-REPORT-r5.md`, `OA-2-REPORT-r4.md`, `OA-3-REPORT-r4.md`,
`W1-1-REPORT-r4.md` at `2d064a71`. `Main:n` = `papers/Main.md`.

**Support labels.** [K] Lean statement (read, nothing built); [P] manuscript; [R] research record on
`main`, not independently established; [R-off] research record off `main`; [W] this writer's
derivation or reading, unreviewed; [L] literature from memory, context only, no verdict rests on it.
Every Step 2 result cited is a paper derivation [W] of Step 2's writer, reviewed under Step 2's
gates and not kernel-checked (#1236 c.6828822665).

***

## 0. Authorization and owner guidance

**Authorization.** Owner amaybaum, 2026-11-13, Issue #1236 comment 6846408321 (author association
`OWNER`), verbatim opening:

> **Owner decision (amaybaum, 2026-11-13): "Authorize Step 3A".**
>
> It was taken on ChatGPT's recommendation and replaces the "Step 3 is not authorized" line in
> c.6828822665 for **Step 3A only**. Step 3B is still not authorized and needs its own owner
> decision.

Its scope, verbatim in substance (the comment's own bullets): the question "Which candidates did
Step 2 not exclude? For each, which quantum tests can it meaningfully face, and which assumptions
are missing?"; the candidates "L5.4–L5.6 for families with unbounded control regions, NL-A and
NL-P"; "INCONCLUSIVE means not excluded. It does not mean shown to survive."; first test "An
approximate single qubit: preparation, transformations and Born readout"; "Kochen–Specker
contextuality and Bell correlations are separate obligations for larger systems. A single-qubit
test settles neither."; for each candidate its complete records, composition, control-resource
scaling, physically justified measurement access, and each assumption marked derived, imported or
unsourced, "Assumed quantum behaviour never counts as derived"; the stop condition "If no candidate
has fully specified dynamics, preparation and readout, Step 3A reports that gap. It does not report
it as a quantum failure."; no reopening of the parked Step 2 investigations and no repetition of
OA-1/OA-2/OA-3; "The work is paper-only. … No computation, Lean execution, new physical premise or
manuscript edit is authorized."

**Writer designation and owner guidance: the governing record.** Issue #1236 comment 6846442383
(`amaybaum`, author association `OWNER`, 2026-11-13T06:59:24Z), read through the GitHub API for r2.
Verbatim:

> **Step 3A has started.** The owner's choice (amaybaum, 2026-11-13) was "Start; this session
> writes (Recommended)", with this Claude session as the writer. The scope is the one in
> c.6846408321, plus the owner's guidance below.
>
> **Owner guidance (amaybaum, 2026-11-13):**
> - **Three tests for each candidate,** drawn from the accepted OA results on #1265 (cited as
>   off-main context, with their exact scope):
>   - **Preparation:** can the apparatus prepare the needed states without assuming an unexplained
>     resource or probability measure? (OA-1 gap 1)
>   - **Control:** does the native deterministic dynamics supply the required operations, rather
>     than having them inserted externally? (OA-1 gap 2: for the affine class, changing the measure
>     alone does not resolve control)
>   - **Persistent incompleteness:** does the observer stay unable to recover the hidden information
>     throughout the relevant experiment, including repeated measurements and retained records? The
>     incompleteness need not be permanent. What matters is that a restriction lasting a finite time
>     is not confused with a measurement menu imposed from outside. (OA-3: in G_SM, held-block
>     observers with kept history reconstruct the ring within about 2L ticks. That leaves other
>     observer models and shorter windows open.)
> - **Classification:** each candidate is classed as remains viable, classical-only under stated
>   assumptions, lacks a sourced apparatus, or underspecified.
> - **Central question:** can a deterministic substratum support an embedded apparatus whose
>   physically available operations show quantum interference, while keeping the observer from
>   accessing enough hidden information to reduce those operations to an ordinary classical
>   prepare–measure model?
> - **Step 3B** stays unauthorized until Step 3A identifies at least one concrete candidate testable
>   against that requirement.

This comment governs. Its wording differs from the coordinator's relay of the same guidance, which
r1 quoted and which is kept below as relay context only; where they differ, the GitHub wording
applies.

**First guidance message, as relayed by the coordinator (context; superseded in wording by
c.6846442383).** Recorded as a scope refinement that adds no authority. Quoted as relayed:

> 1. For each candidate, apply three explicit tests, in addition to the derived / imported /
>    unsourced marking:
>    - **Preparation.** Can the apparatus prepare the needed states without assuming an unexplained
>      resource or probability measure? See OA-1 gap 1, where μ-G is posited.
>    - **Control.** Does the native deterministic dynamics actually supply the required operations,
>      or are they inserted externally? See OA-1 gap 2: for the affine class, changing the measure
>      alone does not resolve control.
>    - **Persistent incompleteness.** Does the observer stay operationally unable to recover the
>      hidden information for the whole relevant experiment, including repeated measurements and
>      retained records? It need not be permanent. It must, though, distinguish a finite-time
>      operational restriction from an artificially imposed measurement menu. See OA-3 Lemma OBS and
>      Theorem S: in G_SM, held-block observers with kept history reconstruct the whole ring in about
>      2L ticks, so the fragment is a simplex under its hypotheses. Note what that does not exclude:
>      other observer models, and shorter operational windows.
> 2. Use the OA results to classify each candidate into one of four groups:
>    - remains viable;
>    - classical-only under stated assumptions;
>    - lacks a sourced apparatus;
>    - underspecified.
> 3. **Central question,** to state in the record and frame the verdict around: can a deterministic
>    substratum support an embedded apparatus whose physically available operations show quantum
>    interference, while preventing the observer from reaching enough hidden information to reduce
>    those operations to an ordinary classical prepare–measure model? The aim is a derived
>    quantum-capable interface, not just a restriction on what the observer may read.
> 4. **Step 3B** stays unauthorized until Step 3A names at least one concrete candidate that can be
>    tested against that requirement. Say explicitly whether any candidate qualifies.

**Second guidance message: relay only.** It is not on #1236 (eight comments read for r2) and
stands on the coordinator's relay alone. Quoted as relayed:

> Two more points of owner guidance for TUNE-1 Step 3A (amaybaum, 2026-11-13):
> 1. **Source of persistent incompleteness.** It must come from the physical dynamics and the
>    apparatus, not from forbidding the observer to make certain measurements. The information need
>    not stay inaccessible forever. It must stay inaccessible under the operating conditions the
>    proposed quantum behaviour needs, including composition and repeated measurements.
> 2. **Interference versus probability tables.** For each candidate, say explicitly whether it
>    genuinely supports quantum interference, meaning coherent transformations whose effects show up
>    in later statistics, or only reproduces selected probability tables. A candidate that only
>    matches tables does not meet the central question.

***

## 1. The central question, and the summary

**Central question (c.6846442383).** Can a deterministic substratum support an embedded apparatus
whose physically available operations show quantum interference, while keeping the observer from
accessing enough hidden information to reduce those operations to an ordinary classical
prepare–measure model? The relayed guidance adds: "The aim is a derived quantum-capable interface,
not just a restriction on what the observer may read."

**Reformulated central question (r3; recorded beside the above, not replacing it; §2A.7).** The
record is #1236 c.6847314661 (`amaybaum`, `OWNER`, 2026-11-13T07:51:30Z): "what observable
operational theories emerge from interactions among embedded observers and apparatus, and under what
intrinsic conditions quantum mechanics emerges rather than classical or supra-quantum behaviour."
The coordinator's relayed wording, kept as context: "Given a deterministic substratum in which
observers and apparatuses are themselves embedded dynamical structures, what observable operational
theories emerge from their interactions, and under what intrinsic conditions does quantum mechanics
emerge rather than classical or supraquantum behavior?" Where the two differ, the comment governs.

**Plain summary.**
1. Step 2 left four candidate classes neither excluded nor shown to work. All four are classes of
   apparatus families with an *unbounded* control region; every bounded-control family is excluded
   by Step 2's rule-free bound NL-C.
2. None of the four names a concrete apparatus. Step 2 fixed the rule (R-lin, or R-nl under a named
   hypothesis), the carrier and the interface *schema*. The readout *rule* is fixed completely by D4
   (the complete history of `O`, with outcome probabilities the pushforward of `μ`); what is missing
   is its instantiation `O_n` and the preparation prefixes. Every member's apparatus region, control
   region, ready configuration, timing, layout and label encoder is existentially quantified, and no
   member is exhibited. So no candidate has a fully specified preparation and readout. This is a
   specification gap, not a quantum failure.
3. Beyond the specification gap, every class carries unsourced ingredients in its apparatus: the
   ready configuration and program blocks (or, in exchange mode, a write access the rule does not
   supply), the run repetition that the record law presupposes, and the law of the unread world.
   The growth of the control region with precision is an admitted resource with no physical account.
4. For the linear-rule classes, an off-`main` result (OA-2 Theorem E(b)) bears on any member that
   meets its hypotheses. With the spanning hypothesis (SP), the prepare–measure fragment is
   simplex-embeddable; without (SP), the model is still preparation-noncontextual. Whether that alone
   excludes the single-qubit test at small `ε` is a Step 3B question at literature level, not derived
   here. Matching TUNE-1's interface to those hypotheses is a reading made here. Changing the law of
   the unread world (L5.6) does not change the translation-only action of the labels.
5. For the nonlinear-rule class, no Step 2 or OA result excludes or classicalizes it. That is an
   absence of results, not evidence for it.
6. **Stop condition: met.** No candidate qualifies for Step 3B. §5 states what a qualifying
   submission must contain. §4 defines T1, the single-qubit test, and proposes T2, a
   classical-reduction test that is an owner-decision proposal, not an authorized test.

**Summary table.** "Specified?" asks for dynamics, preparation and readout fully specified (§3.0).
The group is the owner's four-way classification (c.6846442383), primary group first. Every candidate
also carries the secondary group **lacks a sourced apparatus**, because its ready configuration and
program blocks are unsourced (§3.0), and H-write adds to this for B and for the exchange rows of C and
D. The conditional group says where a specified member would fall, with the hypotheses that carries.
"Lacks a sourced apparatus" is read as in §2A.6: the preparation, control or readout is not shown to be
derivable from the joint dynamics; it does not mean that a separate machine is missing. For
exchange-mode rows (B, and the exchange rows of C and D), the apparatus includes the write access
H-write, an operation not implemented by `Φ_F`; there the group also records that statement (i)
itself fails for the apparatus as specified (§2A.6). No entry of the table changes under that reading
(§2A.6).

| Candidate (Step 2 class, `sup_n |C_n| = ∞`) | Specified? | Missing ingredients | Applicable test (§4) | Status / group |
|---|---|---|---|---|
| **A. L5.4, init**: R-lin, coset-uniform law, initial-condition mode, Q6′ witnessed with heralds | Dynamics yes (ledger posit); readout rule fixed by D4; its instantiation `O_n` and the preparation prefixes missing; no member | concrete `O_n, C_n, r_O, τ`, layout, encoder; source of `r_O` and program blocks; physical account of `|C_n|` growth; source of run repetition; H-μ; the L4 escape audit (approximate form open) | T1 (single qubit, L4 audit included), once a member is specified; T2 proposed (owner decision) | INCONCLUSIVE in Step 2. **Underspecified**; secondary: **lacks a sourced apparatus**. Conditional on OA-2 Theorem E(b) [R-off; match W]: with (SP), **classical-only** (simplex-embeddable prepare–measure fragment); without (SP), still preparation-noncontextual, and whether that excludes T1 is open |
| **B. L5.4 + L5.5, exch**: R-lin, coset-uniform law, exchange mode under H-write, heralded or adaptive witnesses | As A | as A, and H-write (a classical write access `Φ_F` does not supply) | as A | INCONCLUSIVE. **Underspecified**; secondary: **lacks a sourced apparatus** (as A, and H-write). OA-2 Theorem E(b) not applicable as stated |
| **C. L5.6**: R-lin, law not uniform on a coset (level-set law on `𝓛_fin`, exch; non-uniform product law, both carriers and modes), any witness | As A | as A (and B in exch); the law itself is unsourced, and the non-uniform marginal is not fixed by any record | as A | INCONCLUSIVE. **Underspecified**; secondary: **lacks a sourced apparatus** (as A; H-write in exch). Conditional: init members as A (with (SP), **classical-only**; without, preparation-noncontextual); exch members as B |
| **D. NL-A / NL-P**: R-nl under H-nl, every law, both modes, both carriers | Dynamics specified under an unadopted hypothesis; readout rule as A; no member (NL-P is precisely the missing construction) | as A (and B in exch); the rule is not a ledger posit (H-nl; adopting it is a Layer-0 revision) | as A | INCONCLUSIVE. **Underspecified**; secondary: **lacks a sourced apparatus** (as A; H-write in exch); the rule is unsourced. No OA result places it classical-only. Not "remains viable" in any evidential sense (§3.4) |

No candidate is "remains viable" in the sense of c.6846442383's classification read with its Step 3B
gate: none is a concrete apparatus that is unexcluded, specified and sourced.

***

## 2. Productivity test and method (§A.31, §A.12)

**Productivity test, fixed before the per-candidate nodes.** The unit is a gem iff, for some
candidate, it yields a fact strictly stronger than the restatement "Step 2 left these classes
INCONCLUSIVE and no family is exhibited", and that fact either constrains what a concrete candidate
must contain or exposes a hidden assumption in the Step 2 interface. Otherwise it is recorded only.

**Method.** One candidate at a time, depth-first, each node closed by a check against a cited
statement; the decisive branch per candidate is "is there a concrete member to test?". Favourable
readings are pressed hardest (§6). No Step 2 gap is worked on: nothing below attempts to settle L5.4,
L5.5, L5.6, NL-A or NL-P.

**Marking.** Each ingredient is marked:
- **derived**: follows within Step 2's definitions from the fixed rule and the stated interface,
  with the derivation cited;
- **imported**: taken from a source as a premise: a ledger posit of Main:724, a convention of the
  corpus, or literature;
- **unsourced**: chosen by a family's specification, or an unadopted named hypothesis, with no
  physical source on `main`.

Assumed quantum behaviour is never marked derived.

***

## 2A. Embedded-observer framing

**Source: the governing record.** #1236 comment 6847314661 (`amaybaum`, author association `OWNER`,
2026-11-13T07:51:30Z), read through the GitHub API: "**Owner decision (amaybaum, 2026-11-13): "Add to
Step 3A as r3 (Recommended)".** This follows the owner's question: "Why would an observer living
inside the deterministic universe actually have access to those constructions? If the Substratum is
the most fundamental mathematical representation, then why wouldn't an embedded observer have access
to it, since the observer himself is constructed by it?"" The comment lists the seven items of this
section. The coordinator's brief for r3 relayed the same decision with a fuller statement of each
item; it is used below as context, and where it and the comment differ, the comment governs. This
section adds framing and makes no new result. Layer tags as in the header; [O] marks a question the
section leaves open.

### 2A.1 Three statements about the observer and the substratum

Write the substratum dynamics as `s_{t+1} = F(s_t)`.

- **(i) Ontological inclusion.** The observer, and every operation it performs, is implemented by
  `F`. This follows from OI's premise: an observation is a triple `(S, φ, V)` with the observer
  "`V ⊊ S` — a proper subsystem with finitely many distinguishable internal states, coupled to the
  complement `H = S ∖ V` through `φ`" (Main:42) [P].
- **(ii) Observational access.** The information the observer acquires through its interactions with
  the rest of `S`. Main derives that it is incomplete: "An observer embedded in a deterministic
  universe cannot access the complete state" (Main:26), with finite visible resolution the one
  theorem among the early commitments (Lemma 1, Main:60) [P].
- **(iii) Operational control.** The observer's arranging of transformations of other subsystems
  through its own degrees of freedom.

(i) does not imply (ii) or (iii): being built by `F` gives the observer neither the state of the rest
of `S` nor a choice of what `F` does to it. **(ii) and (iii) must be derived from the joint dynamics,
not supplied as a separate list of permitted operations** (c.6847314661: "observational access, which
must be derived from the joint dynamics; operational control, which must likewise be derived from the
joint dynamics"). This is the standard Step 2 applies in initial-condition mode (D2, D5; P:198–199,
"the strictly rule-only target") [R]. Exchange mode supplies (iii) as the named hypothesis H-write
(P:155–167, :237–239, :563–565) [R]. Step 1 records that `main`'s quantum-like constructions are
obtained where "someone chose by hand what the observer may prepare and read" (P:40–42, summarizing
Step 1) [R].

### 2A.2 Reachable versus definable

A configuration or operation that exists in the mathematical space is not thereby reachable under the
actual dynamics from the states the observer can be in (c.6847314661: "a configuration being
mathematically present in the substratum is not the same as being reachable under the actual
dynamics"). Instances in the corpus:
- TUNE-1's label menu is "every configuration of `C`" (P:147–148) [R]. That every such
  configuration is *placed* in `C` is not derived: in initial-condition mode it is an initial
  condition, in exchange mode the write access H-write, which `Φ_F` does not supply (P:155–167,
  :184–199) [R]. The menu is definable; its reachability by the observer's own dynamics is not shown.
- Main's ε-realizations exist as reversible maps, with "Quantum mechanics enters as the instrument
  data and as the state held in the hidden register", and the construction "uses no property of the
  substratum beyond finiteness and reversibility" (Main:580) [P]. Read from that [W]: the
  construction is definable for every target, and nothing makes it the world's dynamics.

**If rules are part of the state, what selects the operating rule?**
- In TUNE-1 the rule is fixed (D7, P:422–423) [R], so no selection question arises inside the
  question as posed.
- In SM's state-dependent-geometry principle, `s(t+1) = φ_{s(t)}(s(t))`, "where each `φ_s` is a
  bijection but `G_{φ_s}` varies with `s`" (SM:104) [P]; the operating rule at each step is selected
  by the state itself, so the global map `s ↦ φ_s(s)` is again one fixed map [W reading]. SM states
  it as a principle that general relativity's background independence would require, if space is the
  coupling graph (SM:104) [P], and its ring example is "not derived or selected by OI" (as OA-3
  quotes MECH-2, OA3:138–141) [R-off]. Which rule operates is then an initial-condition and principle
  question, which is open [O].

### 2A.3 Level A and Level B

- **Level A:** a mathematical representation theorem for a finite observational structure.
- **Level B:** embedded observers whose actual histories realize that structure.

**The nearest existing bridge on `main` is Main §3.4** (c.6847314661: "Main §3.4 is the nearest
existing bridge between the two") [P, with kernel names as Main cites them; no Lean was run here].
Exactly as stated there:
- At fixed observable horizon, `S ⇔ D ⇔ Q_fb` is exact: every finite stochastic law has a finite
  reversible realization and an exact fixed-basis unitary/Born representation (Main:28, :562). Main
  records that this is universal, "Markov and memory-bearing laws alike lie in `Q_fb`, so
  representability alone is not the framework's discriminating content" (Main:554).
- The operational-completion characterization (Main:562): "On any nonempty finite carrier, the
  operational theories whose available families on the system and on every positive ancilla level are
  exactly the normalized finite Kraus instruments are precisely those satisfying (i)–(v)": valid
  probabilities, trivial-ancilla consistency, inert spectators, full reversible control and iterated
  composition. Its hypotheses: a finite carrier; "the complex matrix kinematics the characterization
  takes as given … a kinematics whose derivation from operational premises is open"; the six rules
  (a)–(f) of a finite operational theory. Each condition is independent of the others "and of the
  C1–C4 process, witnessed on the qubit by theories realizing one fixed finite C1–C4 process"
  (`five_way_minimality`, `oi_alone_not_qm`), and none is supplied by bare finite OI (Main:66, :554).
  The kernel identifiers are `exactAll_iff_physical_general`, with necessity `physical_of_exactAll`
  and sufficiency `exactAll_of_physical_general` (Main:562).

What this does not give, read from those statements [W]: it characterizes an operational theory
(Level A) given the kinematics; it does not say which embedded processes (Level B) have operational
theories satisfying (i)–(v), and it names (iv), full reversible control, as not supplied under the
substratum's stated interventions (kernel `substratumGen_not_control`, on the two-state carrier, as
Main:80 and :582 cite it) [P].

**The open task** (owner brief) [O]: identify a class of embedded processes that necessarily has a
quantum operational representation, without defining that class in quantum terms. TUNE-1's
derived-family criterion D1–D7 (P:224–423), with D6 excluding quantum vocabulary and compilation
(P:281–289), is one attempt to state such a class for one qubit; the Q-conditions are the quantum
target the class is tested against (P:445–469; AF:80–197) [R].

### 2A.4 Preparation as derivation, not machine

Under the embedded framing, a preparation is not a separate machine. A distribution or a conditional
ensemble over the system may come from (c.6847314661: "deriving a distribution or ensemble from
initial or boundary conditions, typicality, or earlier dynamics, not building a separate machine"):
- initial or boundary conditions;
- typicality;
- correlations left by earlier dynamics.

Corpus anchors:
- Main already allows a structured preparation as an initial condition: "a realization in the sense of
  §3.4 carries its own fixed hidden prior `μ_H` as part of the realization datum, and the emergent law
  is a function of `(φ, partition, μ_H)`" (Main:58) [P]. That is a declared datum, not a derivation.
- OA-1's MP-0a (a ready-cell supply, "a past-hypothesis-type supply") and MP-0b (the visible history
  counts as held) are the two named premises that resolve OA-1's preparation gap classically
  (OA1:556–566) [R-off]. In this framing MP-0a is the boundary-condition route, and MP-0b is the
  retained-correlations route at the observer's own records [W].
- Step 3A's run-repetition finding F-3A-2 (§7) is the same question asked of TUNE-1: the record law is
  read as frequencies over runs, and which derivation (boundary conditions, typicality, or refresh by
  earlier dynamics, the role of Main's mixing hypothesis and (EM), Main:443–449, :742–758) makes
  successive runs reset and independent in one deterministic world is not stated.

So the preparation test of c.6846442383 becomes a derivation question: **is the preparation, and its
repetition, derived from the joint dynamics together with stated initial or boundary conditions, or
assumed?** [W restatement of the owner text].

### 2A.5 What remains even under the embedded framing

OI's assumptions as currently formulated admit classical countermodels and supra-quantum
constructions (c.6847314661: "OI's assumptions still admit classical and supra-quantum models").
Records, each checked at `origin/main` `62bdc2cf` (Main unchanged from `080cd2be`) or at the stated
off-`main` pin:
- **Supra-quantum.** "if the two wings are allowed to share globally coupled setting-dependent hidden
  dynamics, the same reversible response-table construction that realizes arbitrary finite stochastic
  laws also realizes PR-box behavior" (Main:360) [P]; "Removing the screened local-intervention
  restrictions admits the unrestricted OI behavior class, including the PR negative control"
  (Main:427) [P].
- **Observable laws: representability does not discriminate.** Every finite stochastic law, Markov
  laws included, has a finite OI realization (Main:431), and at that level representability does not
  discriminate (Main:554). The same reversible machinery realizes non-quantum finite instrument
  families (Main:582). The five conditions are independent of a fixed C1–C4 process, witnessed on the
  qubit by non-standard theories (`oi_alone_not_qm`, as Main:562 cites it) [P, kernel names cited].
- **Classical prepare–measure fragment, affine class.** Under OA-2 Theorem E(b)'s hypotheses the
  affine class has a simplex-embeddable prepare–measure fragment (OA2:550–556) [R-off].
- **Non-quantum (gbit) operational theory from a classical reversible substratum.** OA-2's `𝔊_K`: its
  observer sees a contextual gbit at every bounded horizon (OA2:381–490) [R-off]. Its rule is a
  "designed non-affine `φ` (posit)" (OA2:769) [R-off], admitted by Main's Definition (Main:42) but not
  by ledger item (vii) (Main:724).
- **Classical hidden-variable models reproduce one-qubit statistics under supplied access** (C-POS-1,
  C-POS-2; not constructions under OI's premises, P:675–676; AF:316–326) [R]. That shows quantum
  statistics do not by themselves certify a non-classical substratum.
- **Bell-local for the reference graph** (Main:414, Corollary, with all its hypotheses) [P]: if the
  Bell-relevant degrees of freedom are governed entirely by the nearest-neighbour cubic update used in
  SM, the setting interventions are applied at one step to disjoint wing regions, each reading and
  writing only its own, and each wing's ±1 outcome, recorded in every run, is read from a region whose
  graph distance from the other wing's setting region exceeds the number of updates from setting to
  readout, then every measurement-independent response-complete deterministic completion has
  `|S_CHSH| ≤ 2` (Main:364–381, :414).

Hence, read from these records [W]: **embeddedness plus incomplete observation does not by itself
select quantum mechanics.** The same premises admit classical, non-quantum and supra-quantum
behaviour, so any selection of quantum mechanics needs further conditions, which is what §3.4's
(i)–(v) name at Level A, within complex matrix kinematics taken as given (Main:562), and what TUNE-1
tries to source at Level B.

### 2A.6 Step 3A's own terms, re-read

- **"Lacks a sourced apparatus"** means: the preparation, control or readout is not shown to be
  derivable from the joint dynamics (with stated initial or boundary conditions) (c.6847314661: "will
  be read as "not shown derivable from the joint dynamics""). It does **not** mean that a separate
  machine is missing. Under (i) the apparatus is part of `S` by premise; what is missing is the
  derivation of (ii) and (iii) for it. For exchange-mode rows (B, and the exchange rows of C and D),
  the apparatus includes the write access H-write, an operation not implemented by `Φ_F`; there the
  group also records that statement (i) itself fails for the apparatus as specified. No
  classification changes.
- **The preparation test** becomes the derivation question of §2A.4.
- **Do any classifications, verdicts or the Step 3B answer change?** **No.** Checked candidate by
  candidate [W]:
  - A–D, primary group "underspecified": unchanged. The framing does not supply a member.
  - Secondary group "lacks a sourced apparatus": unchanged under the re-reading. For every candidate,
    no record derives `r_O`, the program blocks, run repetition or the growth of `|C_n|` from the joint
    dynamics with stated initial conditions (§3.0, F-3A-2). In exchange mode, H-write is a
    supplied write access, which is exactly what (iii) requires to be derived, and which (i) does not
    cover; B and the exchange rows of C and D therefore stay in the group for that additional reason.
  - Conditional groups (OA-2 Theorem E(b) for A and C; none for B and D): unchanged; the framing adds
    no hypothesis to E(b) and removes none.
  - The stop condition and "no candidate qualifies for Step 3B": unchanged.
- **Results that stay valid within their assumptions.** OA-3's Lemma OBS and Theorem S [R-off] and
  TUNE-1's bounded-control result NL-C [W, Step 2] hold within their stated hypotheses. NL-C applies to
  any control whose per-round gate setting is a configuration of a bounded set of cells, whether that
  set is designated or emergent (S4:423–462; it uses no rule, law or carrier, S4:457–458). What is
  open [O] is whether interfaces outside TUNE-1's schema, such as gates realized over several rounds
  (excluded by definition, S4:697) or settings not encoded as cell configurations, escape it. Whether
  OA-3's observer model captures other observers is open as OA-3 states (OA3:383–386).

### 2A.7 Reformulated central question

Recorded beside the central question of c.6846442383 (§1), which it does not replace.

The record, #1236 c.6847314661 (`amaybaum`, `OWNER`, 2026-11-13T07:51:30Z):

> "what observable operational theories emerge from interactions among embedded observers and
> apparatus, and under what intrinsic conditions quantum mechanics emerges rather than classical or
> supra-quantum behaviour."

The coordinator's relayed wording, kept as context:

> "Given a deterministic substratum in which observers and apparatuses are themselves embedded
> dynamical structures, what observable operational theories emerge from their interactions, and under
> what intrinsic conditions does quantum mechanics emerge rather than classical or supraquantum
> behavior?"

Where the two differ, the comment governs.

***

## 3. The candidates

### 3.0 What is common to all four

**The interface schema (Step 2).** An interface `I = (Λ, O, C, τ, r_O, μ)` with program blocks
`(P_j)` in initial-condition mode (P:137–222): finite observer region `O`, control cells `C ⊆ O`,
round length `τ`, ready configuration `r_O`, law `μ` of the unread world, independent of the observer
(H-μ). A family `{I_n}` comes from one generating rule `n ↦ I_n` (D1, P:232–236). Derived versus
supplied is D1–D7 (P:224–423). The operational target is Q0, Q1, Q2, Q4 (P:445–469) with Q1 changed
and Q3′, Q5′, Q6′ replacing Q3, Q5, Q6 (AF:80–197), conditional error and acceptance reporting
(AF:276–287), and Q4 proved directly (AF:406–420).

**What Step 2 proved for all four (rule-free).** NL-C (S4:423–462): under any rule, law, mode and
carrier, an interface with `|C| ≤ c` fails Q6′(i) at every `ε < sin(π/(q^{2c}+1))/8` and every
`K ≥ L + 1`, for every kind of witness. NL-C′ (S4:464–474): meeting Q6′ at `(ε, K)` with `ε < 1/8`
needs `|C| ≥ ½ log_q((1 − 4ε)/(4ε))`, and the resource `N` is at least `|C|` in exchange mode and
at least `(K + 1)|C|` in initial-condition mode. So every candidate below is a class of families
with `sup_n |C_n| = ∞` (S4:568–575, :668–674).

**What INCONCLUSIVE means here.** Not excluded, and not shown to survive (#1236 c.6846408321).
Each of the four is the complement, inside a family class, of a proved `FAIL-CLASS`; it is an open
existence question, not a candidate shown to work.

**Common specification ledger** (applies to A–D unless the candidate's section changes it).

| Ingredient | Status | Source |
|---|---|---|
| Carrier `𝓛_fin` (finite tori, side growing with `n`) | imported | Main:724 item (ii); P:123–125 |
| Carrier `𝓛_∞` | unsourced (H-∞, unadopted) | P:126–129 |
| Alphabet `q` fixed | imported | P:131–133 |
| Region `O_n`, control cells `C_n`, `τ`, layout, generating rule | unsourced: chosen by the family's specification; **none is given for any member** | P:137–150, :211–222; S3:213–229; S4:485–497 |
| Ready configuration `r_O` and, in init mode, the initial content of the program blocks | unsourced: a declared initial condition of designated cells, the type OA-1 names MP-0a, "a past-hypothesis-type supply of ready cells" [R-off] | P:184–199; OA1:556–562 |
| Repetition: the record law read as frequencies over runs, each run a fresh draw of `μ` with `O` reset to `r_O` | unsourced: used but not stated in TUNE-1's governing texts. B4's trial count `1/p_acc` and trial cost `R(ε, K)` presuppose independent repeated trials (AF:283–287), and the proposal speaks of runs a herald accepts (P:174–175). It is separate from H-μ, which is a time-zero law. The nearest corpus premises are MP-0a for the reset of `O` [R-off] and Main's mixing hypothesis or (EM) for refreshing the hidden sector between runs [P, conditional]; neither is applied to TUNE-1 interfaces (F-3A-2) | AF:283–287; P:174–175, :181–182, :242; OA1:556–562; Main:443–449, :498, :742–758 |
| Law `μ`, uniform | imported relative to a posit: the uniform reading of ledger item (iv) is [W] (P:266–268); OA-1 types the global counting measure μ-G as posited, not derived [R-off] | P:242–271; Main:724 (iv); OA1:96–105 |
| Independence of `μ` from everything the observer does | unsourced as a named hypothesis (H-μ); analogous to ledger (xiv), which Main posits for Bell | P:145; Main:724 (xiv) |
| Label *action* on the world | derived: only `Φ_F` acts after the label is in place | P:237–241 (D2) |
| Label *selection* | init: unsourced initial condition (as `r_O`); exch: unsourced write access H-write, which `obs_exchangesAvailable` does not discharge because the observer theory is rule-independent [K] | P:155–167, :184–199 |
| Label encoder (targets → labels) and its cost `G(ε, K)` | unsourced: computed off the lattice, or shown only to exist; D6(b) requires each component `parameter` or `selected` | P:147–153, :217–222, :357–401 |
| Access to `O` (passive, every tick, full resolution) | imported: `O` plays the visible sector of Main's partition (Main:42); D4/D5 forbid any declared restriction | P:272–280 |
| Complete records: the whole history of `O` held to the end | imported convention: the type OA-1 names MP-0b ("the visible history counts as held") [R-off]; matches OA-2's (H4) nested records | P:167–171, :272; OA1:563–566; OA2:502 |
| Outcome probabilities ("Born readout" in the operational sense) | derived given `μ`: the pushforward of `μ` through the dynamics; their match to Born weights is what T1 tests; why `μ` is what it is stays H-μ | P:272–277 (D4) |
| Heralds | derived (conditioning on records), with `p_acc` and trial cost `R(ε, K)` reported | AF:114–123, :276–287 |
| Composition | defined (Q4, model-free); L3 is not available under Q3′, so Q4 must be proved row by row; not proved for any candidate | P:460–469; AF:406–420 |
| Control-resource growth `|C_n| ≥ ½ log_q((1−4ε)/(4ε))` | the necessity is derived [W, Step 2]. The growth itself is an admitted resource with no physical account (owner requirement, c.6828822665: the growth "must itself be physically explained"): the question admits it by design through the generating rule and `n(ε, K)`, and no mechanism in the rule produces it | S4:464–474; P:123–125, :211–222 |
| Separation length `L` and constant `c₀` | family-declared constants, checked, not fitted | AF:168–197 |

**Reading of the three guidance tests against the common ledger** [W].
- *Preparation.* Every candidate's preparations are protocol prefixes run from a declared `r_O`
  (with declared program blocks in init mode, or H-write in exch mode), over a world drawn from `μ`
  under H-μ, repeated as an ensemble. Each of these is unsourced or posit-relative (table above).
  OA-1 gap 1 places the same resources (MP-0a, MP-0b) as classical resources that resolve the
  preparation gap only by being supplied (OA1:522, :556–566) [R-off]. **No candidate passes the
  preparation test as sourced.** This is common to all four and does not distinguish them, and it is
  why every candidate carries the secondary group **lacks a sourced apparatus** (§1).
- *Control.* The label's action is by `Φ_F` alone (derived). Its selection and placement are not
  (init: initial condition; exch: H-write). Whether the action supplies the *required* operations is
  the candidate-specific question (§§3.1–3.4).
- *Persistent incompleteness.* D5 admits every protocol and forbids every declared read restriction
  (P:278–280), so whatever incompleteness a member has comes from the boundary of `O_n`, the unread
  law and the dynamics, not from a forbidden measurement. That meets item 1 of the second guidance
  message in form. Whether it persists over the horizon `K` at `I_{n(ε,K)}`, through repeated reads
  and composition, is undecided for every candidate, and the region `O_n` that bounds it is itself a
  design choice (unsourced).

**A scope fact for every candidate** [W reading of P:211–222, :485–486]. The interface may depend on
`K` through `n(ε, K)`: a pass certifies one apparatus per `(ε, K)`, serving every label and protocol
of horizon `K`, not one apparatus for every horizon. Interference within each horizon is what Q3′
and Q4 test; a horizon-uniform apparatus is a stronger, separate requirement (§4.1, option T1-U).

### 3.1 Candidate A: L5.4 in initial-condition mode

**Node A.1: definition.** Gap L5.4 (S3:213–214): "For R-lin under a coset-uniform law, can a family
whose Q6′ witnesses are heralded meet Q3′, Q5′ and Q6′ together at every `ε`?" The class is
`(R-lin, uniform law on 𝓛_fin | uniform product law on 𝓛_∞ under H-∞, init)` (S3:335–336), narrowed
by the NL-C rows to families with `sup_n |C_n| = ∞` (S4:654–655, :668–674). R-lin is
`Φ_F(y, x) = (x, Ax − y)` with `A` the nearest-neighbour sum over `ℤ/q` (P:85–89; S3:58).

**Node A.2: what Step 2 proved and did not prove.**
- Proved [W]: Lemma A-T (S3:56–88): every complete record is `H_O r_O + H_P c + H_U u` with
  homomorphisms independent of the labels, the record law is uniform on a coset of a label-independent
  subgroup, and equal-length unheralded preparations followed by a common continuation are at total
  variation 0 or 1. FC-1 (S3:122–170; corrected by F-S3-1, S4:303–345): Q3′, Q5′, Q6′ fail together
  at `ε < 1/48`, `K ≥ L + 1` when Q6′ is witnessed by unheralded preparations. Lemma I (S4:262–282):
  under Q3′, Q5′, Q6′, any admissible witness pair, padded, is at total variation in
  `[¼ − 8ε, ¾ + 12ε]`, for every rule. NL-C excludes bounded `|C_n|`.
- Not proved: whether heralded witnesses can meet Q3′, Q5′, Q6′. A heralded preparation's
  continuation law is a mixture of pairwise equal-or-disjoint extreme laws (a simplex whose extreme
  points the labels translate), so Lemma I's intermediate distances are not excluded; one-axis
  rotations form an abelian group, which translations need not exclude (S3:198–211). The owner
  decided "Record and leave" (S4:12). No work on L5.4 is done here.
- Open and necessary for any pass: the **L4 escape audit**, "necessary conditions on any
  `PASS-DERIVED`" (P:842–849): (a) the map from preparation prefixes to qubit states is not an
  injective complete orthogonal frame with H-LIFT; (b) `N(ε, K)` is unbounded as `ε → 0`. Its exact
  form is proved for R-lin on `𝓛_fin` [W] (S3:276–282); its approximate, operational form is open (S3:283–289).
  A concrete member must meet it.

**Node A.3: specification.** Dynamics: imported (ledger posit, Main:724 items (vii), (xiii); P:85–89).
Readout: the rule is fixed completely by D4 (the complete history of `O`, with outcome probabilities
the pushforward of `μ`, P:272–277); its instantiation `O_n` is missing. Preparation: the protocol
prefixes from `r_O` (§3.0), not instantiated. No member is exhibited: no `O_n, C_n, r_O, τ`, layout
or encoder is given in any record read (S3:196–214; S4:668–674). **Verdict: not fully specified.**

**Node A.4: the three guidance tests.**
- *Preparation:* not sourced (§3.0).
- *Control:* the native dynamics supplies label actions that are **translations** of the record
  variable: Lemma A-T (a) is a statement about values and holds for every law (S3:62–64, :79–82); OA-2
  Theorem E(a) states the same measure-free form (OA2:525–527) [R-off]; OA-1 gap 2 names it the
  earliest failure that holds under every measure (OA1:523) [R-off]. Whether translations of a
  coset-structured law, conditioned by heralds, supply the target's gate family is exactly L5.4 and is
  open. **Verdict: control is native but translation-only; adequacy open.**
- *Persistent incompleteness:* undecided. OA-3's Lemma OBS does not transfer as stated: it is for a
  one-dimensional ring, under a rule permutive in its extreme left argument, with a held block of
  width `l + r` (OA3:223–268) [R-off]; no three-dimensional analogue is derived in any record read.
  D1 allows `O_n` to grow without bound, including into shapes a concrete family would have to check
  for reconstruction of the unread world within the horizon. More to the point for this class, OA-2
  Theorem E(b) (OA2:522–560) [R-off] gives a classical model of the affine prepare–measure fragment
  that does **not** need the observer to recover the hidden state: it is built from the translation
  structure alone. With (H1), H-AR, (H3), (H4), (xiv) and (SP), the fragment is simplex-embeddable;
  without (SP), the same model is still preparation-noncontextual (OA2:534, :542). So for R-lin,
  incompleteness that persists is not by itself enough for the central question.

**Node A.5: interference versus probability tables.** Not shown either way. No member is exhibited,
so the class neither reproduces tables nor shows coherent transformations. The test that would decide
it is defined: Q3′ credits each gate round with the rotation's effect on *later* identified rounds
(AF:161–167), Q4 tests composition model-free, and controls C-REBIT and C-NULL exclude the obvious
non-interfering cases (AF:357–379). Under R-lin the gate's effect on later statistics would have to
arise from label translations; Step 2 records no argument for or against (S3:206–209).

**Node A.6: relation to OA results.**
- OA-2 Theorem E(b) [R-off, WIP]: under (H1) affine bijection (R-lin included, OA2:499), H-AR
  (cell-aligned full-resolution reads, or their MP-0b history, OA2:182–186), (H3) no supplied control,
  (H4) nested records, (xiv) and (SP) spanning, the prepare–measure fragment is simplex-embeddable at
  every carrier size, and G3 fails (OA2:550–556). Transformation noncontextuality is not claimed
  (OA2:540–541). Reading of the match [W, unreviewed]: TUNE-1's init mode has (H1) (R-lin), H-AR
  (complete reads of the cells of `O`, D4), (H3) (no writes after time zero, D2), (H4) (the record is
  the complete history, D4) and an independence clause that plays (xiv) (H-μ). **(SP) is not decided**
  for TUNE-1 interfaces. Both halves matter:
  - with (SP), the prepare–measure fragment is simplex-embeddable (OA2:550–556);
  - without (SP), the model is still preparation-noncontextual (OA2:534, :542–544). Whether a
    preparation-noncontextual model can meet T1 at small `ε` is a Step 3B question at [L] level
    (a qubit's prepare–measure fragment is preparation-contextual: Spekkens, PRA 71, 052108 (2005);
    the parity-oblivious multiplexing bound 3/4 of §4.2), not derived here. Failing (SP) is at most a
    route past G3 or T2, through OA-2's "non-spanning reachable laws (N2.1's dual route)" (OA2:604),
    while T1 may stay blocked; the central question needs T1 and T2 together (§4.2), so a non-(SP)
    member is not shown to be an escape for it.
- Heralds and record class (m4). Heralded preparations lie inside OA-2's procedures ("It may include
  heralds (conditioning on held records) and discards", OA2:102–104). OA-3 N4.1 records herald typing
  as an open interface premise (OA3:124–127, :394–416); TUNE-1's D4 retains the complete history, the
  MP-0b convention, so held-at-use typing is met by convention [W reading]. OA-3 N4.3 shows (H4) can
  be replaced by the Lemma 1 effect class (OA3:460–475). The `𝓛_∞` rows of A rely on OA-2's reading
  of (H1) on "a finite-horizon window" of the lattice (OA2:499).
- Open item for Step 3B (the reviewer's remark, [W], unverified here and not used). Under a
  coset-uniform law, every reachable law of the label-free record is a mixture of uniform laws on
  cosets of a fixed subgroup (S3:198–204), so the raw (SP) of OA-2 fails whenever that subgroup is
  nontrivial, while a model on the coset space might restore measurement noncontextuality. "(SP) open"
  may therefore resolve cheaply, in either direction.
- OA-3 Theorem S [R-off, WIP]: a simplex prepare–measure fragment for `G_SM`, class N and SM:112's
  ring rule, with an observer holding three (class N: two) consecutive sites of a finite ring, MP-0b
  or (V-ii-H), a measurement stage of at least `2(L−2)` and (PT) (OA3:294–347). Its own scope note:
  horizons `T ≪ L` are not covered (OA3:383–386). It is about one-dimensional rings, not TUNE-1's
  cubic lattice; it does not apply to candidate A as stated, and is cited only as the kind of result
  the persistent-incompleteness test must rule in or out for a concrete member.
- OA-1 [R-off]: §4.2's single-qubit target (OA1:488–512) is the same target in OA-1's terms; R5
  records that TUNE-1's bounded-`|C_n|` FAIL-CLASS leaves open "5d with M-INACC on growing carriers"
  (OA1:437–446), which is where candidate A lies.

**Node A.7: group.** **Underspecified**; secondary group **lacks a sourced apparatus** (`r_O` and the
program blocks are unsourced, §3.0). Conditional on a member being specified and meeting OA-2
Theorem E(b)'s other hypotheses [R-off; the hypothesis match is W]: with (SP), **classical-only** in
its prepare–measure fragment; without (SP), still preparation-noncontextual, and whether that
excludes T1 at small `ε` is a Step 3B question [L], not derived.

### 3.2 Candidate B: L5.4 and L5.5 in exchange mode

**Node B.1: definition.** The class `(R-lin, uniform | uniform product, exch, H-write)`
(S3:337–338), with Q6′ witnessed by heralded preparations (L5.4) or by adaptive ones (gap L5.5,
S3:216–221: "as L5.4, for adaptive witnesses in exchange mode"), narrowed to `sup_n |C_n| = ∞`
(S4:656–657, :668–674). Exchange mode resets a label register and exchanges it with `C` each round
(P:155–171).

**Node B.2: proved / not proved.** Proved [W]: FC-2 (S3:191–194, corrected S4:342–343) for
non-adaptive unheralded witnesses; Lemma A-T (b) for non-adaptive protocols; NL-C. Not proved: the
heralded case (as A) and the adaptive case, where a prefix's joint law mixes record-dependent label
sequences and Lemma A-T (d) does not apply to its marginal (S3:218–219). Recorded and left by owner
decision (S4:12).

**Node B.3: specification.** As A, plus H-write: "a classical write access to `C` that `Φ_F` does
not supply" (P:157–167). **Verdict: not fully specified.**

**Node B.4: the three tests.** *Preparation:* not sourced (§3.0), and the per-round writes are an
additional unsourced resource. *Control:* the writes are inserted externally (H-write); their effect
on the world is by `Φ_F` and, for non-adaptive protocols, translation-only (Lemma A-T (b)). Adaptivity
chooses among translations by records; whether that supplies the target gates is L5.5, open.
*Persistent incompleteness:* as A; in exchange mode every round's record also contains its label
(S3:186–187).

**Node B.5: interference versus tables.** Not shown either way (as A).

**Node B.6: relation to OA results** [W reading]. OA-2's setup excludes writes outside `φ` (OA2:173,
item 1), and Theorem E(b) assumes (H3) no supplied control (OA2:501). Exchange mode under H-write is
outside both as stated, so Theorem E(b) does not classify B. OA-1's MP-0b/MP-0a remarks apply to the
register as to `r_O`.

**Node B.7: group.** **Underspecified**; secondary group **lacks a sourced apparatus**, for the same
reason as every candidate (§3.0) and additionally because H-write is a write access the rule does not
supply, so even a specified member is a result about the rule plus an external writer (P:563–565). No
OA result places it classical-only as stated.

### 3.3 Candidate C: L5.6, laws that are not uniform on a coset

**Node C.1: definition.** Gap L5.6 (S3:223–229): "as FC-1, under each of these laws": the level-set
law (the conditional, given `O = r_O`, of the uniform law on a level set `{E = e}` of SM:296's
conserved quantity, `𝓛_fin` and exchange mode only; P:249–258) and the translation- and
`O_h`-invariant product law with a non-uniform site marginal (P:253), in every carrier and mode where
defined (S3:339–344), narrowed to `sup_n |C_n| = ∞` (S4:658–663, :668–674). No witness restriction:
FC-1's route is unavailable under these laws.

**Node C.2: proved / not proved.** Proved: NL-C only. Not proved: anything about these laws'
record-law structure; Lemma A-T (c) needs a coset-uniform law (S3:225–226).

**Node C.3: specification.** As A (init) or B (exch), and in addition the law is unsourced. The
level-set law fixes a level value `e` in the specification (P:249–252). For the non-uniform product
law, **no record fixes the site marginal**: the list names a class of laws, not a law [W, from
P:253 and P:1154–1155]. A family that picks the marginal adds a free parameter to the apparatus, which
§A.29's hard-to-vary requirement would have to address before any result counted. The existing guard
against tuning it is D3's robustness clause: a result counts as derived only if it also holds under a
second law of the list with the same symmetries (P:268–271). **Verdict: not fully specified.**

**Node C.4: the three tests.** *Preparation:* not sourced (§3.0); the law is additionally unsourced.
*Control:* unchanged from A and B. Lemma A-T (a), (b) do not use the law (S3:62–68), so the labels
still act only by translation under every law of L5.6 [W, reading of S3:79–85]. This is the TUNE-1
instance of the owner's note that for the affine class "changing the measure alone does not resolve
control" (OA1:523, "a measure-free property of the map") [R-off]. *Persistent incompleteness:* as A.

**Node C.5: interference versus tables.** Not shown either way.

**Node C.6: relation to OA results** [W reading]. OA-2 Theorem E(b)'s proof uses the law only through
Proposition B(i) and B(ii) (⇐), which OA-2 states hold for every law (OA2:746) [R-off], and through
(xiv) and (SP); OA-2's measure table lists (xiv) as Theorem E(b)'s only law-dependent need (OA2:750),
and in TUNE-1 H-μ plays (xiv). So, under the same hypothesis match as A, an init-mode member of C would fall
under Theorem E(b) exactly as an init-mode member of A would, with (SP) open and both halves as in
A.6: with (SP), simplex-embeddable; without (SP), still preparation-noncontextual, with whether that
excludes T1 a Step 3B question [L]. Exchange-mode members are outside it as in B. The `𝓛_∞` rows rely
on OA-2's finite-horizon-window reading of (H1) (OA2:499).

**Node C.7: group.** **Underspecified**; secondary group **lacks a sourced apparatus** (as A, and
H-write for the exchange rows). Conditional: init members, with (SP), **classical-only** [R-off;
match W]; without (SP), preparation-noncontextual, T1 open at [L] level; exch members as B. The law is
unsourced in both.

### 3.4 Candidate D: NL-A and NL-P, the nonlinear rule

**Node D.1: definition.** R-nl is `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q` on representatives
(S4:30–36; SM:294), under H-nl, "the world's rule is R-nl", which replaces ledger item (vii) and is
not adopted (S4:37–39; P:90–112). The class is every R-nl family, under every law on the list, both
modes and both carriers (S4:577–588), with `sup_n |C_n| = ∞` (S4:572–575, :613–614). Two gaps are
stated on it:
- **NL-A** (S4:595–604): is there `δ ∈ [0, ¼)` such that every admissible padded witness pair of an
  interface meeting Q3′, Q5′, Q6′ has `TV ∉ (δ, 1 − δ)`? A yes would give a `FAIL-CLASS`.
- **NL-P** (S4:605–606): "Exhibit an R-nl family in `𝕀_D` with Q0–Q6 (amended) and D1–D7 proved,
  with explicit `N(ε, K)` and `G(ε, K)`."

**Node D.2: proved / not proved.** Proved [W]: R-nl is not affine (Lemma NA, S4:86–92); the
one-time-pad lemma for every second-order rule (Lemma M, S4:94–101); Lemma A-T's conclusions fail
for R-nl at `q = 3` in both modes and at `q = 2` in init mode, by witnesses W-nl-1 to W-nl-4
(S4:156–258); Lemma I (rule-free); NL-C. Not proved: NL-A (the restricted or approximate dichotomy;
the unrestricted form is refuted below stated constants, S4:385–397); NL-P (no family is exhibited;
"R-nl's record laws have no closed form", S4:485–497). Owner decision 4: "No further work on these
gaps is authorized" (S4:608–611).
- Open and necessary for any pass: the **L4 escape audit** (P:842–849), which NL.3 lists among the
  conditions any R-nl candidate must meet (S4:487–491). Lemma F and exact U2(ii) hold for R-nl on
  `𝓛_fin`, so L4(a) holds in exact form there [W] (S4:519–520); on `𝓛_∞` neither was re-derived, and
  the approximate form stays open (S4:522–523; S3:283–289).

**Node D.3: specification.** Dynamics: fully stated as a rule, but **unsourced as OI's rule**: R-nl
is a candidate realization introduced for numerical motivation (SM:294; Main:724 item (v)), it does
not meet ledger item (vii), and adopting it would be a Layer-0 revision needing preserved results and
an independent prediction (P:996–1004; §A.29). Preparation and readout: the common schema, with no
member. NL-P is by its statement the absence of a concrete family. **Verdict: not fully specified.**

**Node D.4: the three tests.** *Preparation:* not sourced (§3.0). *Control:* W-nl-2 to W-nl-4
(S4:168–253) [W] show that R-nl's record laws are not coset-structured for single rounds on one- or
two-cell regions: the exact total-variation dichotomy fails there (S4:385–397). That is a necessary
ingredient of MP-1-type control (OA1:556–566) [R-off], not shown to be setting-selective control;
Step 2 records the witnesses as single rounds that "say nothing about Q2–Q6" (S4:686–687), and they
do not show the target gates. *Persistent incompleteness:*
undecided. Lemma M gives fresh uniform masking of unread cells at each tick under the uniform law
(S4:94–101) [W]; that is a one-tick property and is not evidence of persistence over a horizon.

**Node D.5: interference versus tables.** Not shown either way; no family.

**Node D.6: relation to OA results.**
- OA-2 [R-off]: non-affine rules are OPEN (OA2:674, :765, :775–779). Its N2.3 constructs a designed
  reversible classical computer `𝔊_K` whose observer sees a contextual gbit at every bounded horizon
  (OA2:381–490): non-simplex-embeddability (G3) at bounded horizon does not separate classical from
  quantum (OA2:157). So non-affinity, or even G3 at bounded horizon, is not evidence of a
  quantum-capable interface.
- OA-2 Corollary E1 [R-off, W] (OA2:577–600) is the relevant necessary condition: within E3, keeping
  (H4), (SP) and (xiv), a G3 escape "requires settings that do **not** merely translate the joint
  held record", for any rule. For D this means a concrete member would have to show that R-nl's
  settings do more than translate the joint held record over the horizon; W-nl-2 to W-nl-4 do not
  show that (D.4).
- OA-3 [R-off]: Lemma OBS and Theorem S concern ring rules permutive at an edge; R-nl's rounded
  neighbour sum is not of that form as stated, and no transfer is derived [W reading]. OA-3 neither
  classicalizes nor excludes D.
- Step 2's own compiled-simulator boundary applies: if a proof of the Q-conditions for an R-nl family
  went through a capacity statement (R-nl reproduces some controller) whose controller has a D6 hit,
  the encoder is `content` and a hit (S4:493–497; P:302–321).

**Node D.7: group.** **Underspecified**, with an unsourced rule; secondary group **lacks a sourced
apparatus** (as A, and H-write for the exchange rows, S4:581–583, :587–588). No OA or Step 2 result places it
classical-only or excludes it for unbounded control regions. That is the absence of a result, and is
not "remains viable" in any evidential sense (§6).

***

## 4. Test definitions

These define the tests a concrete candidate would face. They are not applied to any candidate here
(no candidate is concrete, §5), and their application is Step 3B, which is not authorized.

### 4.1 T1: the approximate single qubit (preparation, transformations, Born readout)

**Object under test.** A family `{I_n}` in the schema of §3.0, with its generating rule, law, mode,
carrier, declared target `𝔔*` (axis `n̂`, gate labels `c(θ)`, Lüders reads `c_a, c_b` with
`a·b ∈ [−½, ½]`, optional further labels; AF:84–112), separation length `L ≥ 2`, separation constant
`c₀ > 0`, and a stated `n(ε, K)`.

**Conditions**, all at the interface `I_{n(ε,K)}`, for **every** `ε > 0` and every `K ≥ L + 1`
(Q6′ is not posed for smaller `K`, AF:262–274), with the governing Step 2 texts deciding every
definition:

| Part | Condition | Content | Source |
|---|---|---|---|
| Resources | Q0 | `N(I) ≤ N(ε, K)` explicit and finite; `G(ε, K)` and the trial cost `R(ε, K) = max 1/p_acc` reported beside it | P:447–449; AF:283–287 |
| Preparation | Q6′(i) | every pure `ψ` has an admissible preparation of length `≤ K − L`, credited at error `ε` on `𝒯_L`, with credited mean within trace distance `ε` of `ψ` | AF:168–170 |
| | Q6′(ii) | separation `c*_n ≥ c₀` for every `n` in the range of `n(ε, K)` | AF:171–197 |
| | Q1 | two preparations distinguished within `ε` by a common continuation, and no three pairwise; heralded witnesses admissible and credited on `𝒯_K` | P:450–453; AF:147–151 |
| Transformations | Q3′ | `F(ε; 𝒯_K)`: every admissible preparation of length `≤ K − 1` has an assignment credited at error `ε` on every identified test, gates included; each gate round's record has law `p(θ)` whatever was prepared, and its effect on later identified rounds is the rotation by `θ` about `n̂` | AF:125–140, :161–167 |
| | Q4 | composition, model-free: replacing gate rounds `c(θ₁), c(θ₂)` by `c(θ₁+θ₂), c(0)` changes the joint law of all other rounds by at most `ε`, with continuation labels not reading the gate rounds; proved directly | P:460–469; AF:406–420 |
| Born readout | Q5′ | `F(ε; 𝒯_R)`: sequential complete records of the two reads match Lüders instruments: repeated reads reproduce their class within `ε`, and `b` after `a` has class frequencies `Tr(P_b P_a·)` | AF:153–160 |
| | Q2 | one fixed qubit model `𝔔` with `d_K(I, 𝔔) ≤ ε` over complete multi-time records of every adaptive protocol (init mode: its non-adaptive protocols) | P:439–454 |
| Derivation status | D1–D7 | one interface per `n` for every target; only `Φ_F` acts; one law from the list with the robustness clause; complete reads; no access by declaration; no quantum input by vocabulary or compilation (choice 11(a)); rule class | P:232–423; AF:289–298 |
| Necessary condition | L4 escape audit | (a) the preparation-to-state map is not an injective complete orthogonal frame with H-LIFT (exact form proved on `𝓛_fin` only, for R-lin and for R-nl, S3:276–282, S4:519–520; approximate form open, S3:283–289, S4:522–523); (b) `N(ε, K)` unbounded as `ε → 0` | P:842–849; S4:487–491 |

**Tolerances.** One `ε` for every target `θ`, every protocol of horizon `K` and every condition, at
the one interface `I_{n(ε,K)}` (P:485–486). Heralded preparations at conditional error `ε`, with
`p_acc` reported (AF:276–287).

**What counts as passing.** The Step 2 token `PASS-DERIVED[R, 𝓛, λ, m | H]`, generated from the
condition and control tables by P:603–623 over green controls, with every hypothesis named. Partial
outcomes are reported with their `PARTIAL-x` tokens (P:570–574) and are not passes; in particular a
match at one `(ε, K)`, or at a finite menu, is not a pass.

**Reported beside the token, not part of it (Step 3A additions).**
- *Sourcing vector*: the derived / imported / unsourced status of each ingredient of §3.0 for the
  family, and the three guidance tests (preparation, control, persistent incompleteness).
- *Interference versus tables*: a family that passes T1 has, by Q3′ and Q4, gate rounds whose effect
  on later statistics is a composing one-parameter rotation family on credited states, which is the
  owner's sense of interference. A construction that matches the outcome statistics of a fixed list
  of experiments, without Q3′'s credit on every identified test and Q4, is classified as table
  matching and does not meet the central question. Main's ε-realizations (Main:564–596) are the
  reference case of table matching with supplied quantum data (control C-SUP-1, P:673).
- *Option T1-U* (owner decision, not adopted): the same conditions with `n` depending on `ε` alone,
  one apparatus for every horizon. The question whether a finite bijection can meet unbounded
  horizons is open in OA-2's terms (AW-OA2-2, OA2:157) [R-off]. Prior art: Main records that the
  characterization is stated per finite horizon and that "the per-horizon qualifier is load-bearing"
  (Main:496) [P]; a horizon-uniform requirement has to face that.

**What T1 assumes and does not establish.** It assumes H-μ (and H-∞, H-write, H-nl where used),
the declared ready configuration, the complete-history record and run repetition, which TUNE-1 uses
but does not state (F-3A-2). A pass
would not establish the selection of the Born rule (why `μ`), Kochen–Specker contextuality, Bell
correlations, composite systems, exact rotations, or any change in correctness (P:642–650; AF:252–257).
The Kochen–Specker sphere model reproduces one qubit with a classical hidden variable (control
C-POS-1, P:675), so a T1 pass does not by itself show the absence of a classical model.

### 4.2 T2: classical reduction under persistent incompleteness (for the central question)

**Status: a writer's proposal for owner decision, not an authorized test.** T2 makes the second half
of the central question testable on the same interface. It is proposed here because the owner frames
the verdict around that question; whether T2 is part of Step 3B is the owner's decision.
It is a single-system test of *generalized* (preparation and measurement) noncontextuality, distinct
from Kochen–Specker contextuality.

**Definition**, at each interface `I_{n(ε,K)}` that is evaluated for T1:
- **T2(a) Fragment.** The prepare–measure fragment: preparations are the admissible preparations of
  length `≤ K − L` (heralded ones included); effects are all post-processings of the complete records
  of every protocol continuation within the horizon, with OA-2's convention C-PM that a preparation's
  own label cells are not effects on what it prepared (OA2:103–117) [R-off; convention imported].
  No read admitted by D5 is removed.
- **T2(b) Classical reduction.** The fragment is *classical-reducible* at that interface if it is
  simplex-embeddable in the sense of OA-2's G3 (OA2:157; [L] Schmid et al., PRX Quantum 2, 010331
  (2021)). T2 passes at the interface if it is **not** classical-reducible.
- **T2(c) Robust witness.** Because T1 is approximate, the verdict of T2(b) must be carried by a
  noise-robust preparation-noncontextuality witness evaluated on the same records, with its
  operational-equivalence conditions checked within a stated tolerance and its classical bound
  stated before evaluation. An instance is the two-bit parity-oblivious multiplexing task
  ([L] Spekkens, Buzacott, Keehn, Toner, Pryde, PRL 102, 010401 (2009): preparation-noncontextual
  bound 3/4, qubit value `(2 + √2)/4`). The robust form and its tolerance are to be fixed in a Step 3B
  preregistration, from the literature read then; nothing here fixes numbers.
- **T2(d) Persistence and source.** The non-reducibility must hold with every read the definitions
  admit, including repeated reads, the retained complete history and composition within the horizon,
  so it cannot come from an omitted measurement. Its source is the boundary of `O_n`, the unread law
  and the dynamics, as D5 requires (owner guidance, second message, item 1, relay only).

**What T2 is not.** G3 alone does not separate classical from quantum at bounded horizons: OA-2's
`𝔊_K` passes it with a designed classical computer (OA2:381–490) [R-off]. T2 counts only together with
T1. Whether T1 at small enough `ε` already forces T2 (since no noncontextual model reproduces a qubit's
prepare–measure fragment, [L] Spekkens, PRA 71, 052108 (2005)) is an expectation from the literature,
not derived here; it is a Step 3B question.

**Controls for T2 (expected classifications, to be preregistered with the rule, not numbers).**
`𝔊_K`: not classical-reducible at bounded horizon, fails T1 (a gbit is not a qubit, OA2:476) [R-off].
C-POS-1, the Kochen–Specker sphere model: meets T1's Q-conditions at `ε = 0` on its protocol class;
supplied (it fails D-clauses, `OPERATIONAL-ONLY`, P:675), so not a T1 pass. Its operational
prepare–measure fragment is expected not classical-reducible [L expectation]; this concerns the
operational fragment, not the sphere model's ontic model, which is a classical hidden variable. A member of OA-3 Theorem S's class: classical-reducible
[R-off]. C-ISO-2's walker: classical-reducible [W expectation].

### 4.3 Obligations kept separate (larger systems)

- **Kochen–Specker contextuality.** Not posed by one qubit: the Kochen–Specker theorem needs a
  Hilbert space of dimension at least three [L], and the sphere model is a noncontextual model of one
  qubit in that sense (P:644–646). A test needs a larger system and is not defined here.
- **Bell correlations.** Need two apparatus regions. Any later test definition must first state
  whether the two wings' settings and readouts meet hypotheses (i)–(iv) of Main §3.3's theorem
  (Main:364–381) [P]; where they do, Main proves `|S_CHSH| ≤ 2`, so the test turns on which hypothesis
  the candidate gives up. The postdiction of P:1028–1030 (whether two disjoint regions compose as
  `ℂ² ⊗ ℂ²`) belongs here.
- Neither is settled by T1 or T2.

***

## 5. Stop-condition verdict and Step 3B

**Stop condition: met.** No candidate has fully specified dynamics, preparation and readout.
- Dynamics: specified for A–C (R-lin, a ledger posit) and, under the unadopted H-nl, for D.
- Readout: the rule is fixed completely by D4 (complete history of `O`; outcome probabilities the
  pushforward of `μ`); its instantiation `O_n` is not given.
- Preparation and the apparatus: specified only as Step 2's interface schema. For every candidate the
  apparatus region, control region, ready configuration, timing, layout, label encoder and generating
  rule are existential (P:1011–1016), and no member is exhibited in any record read (S3:196–229;
  S4:485–497, :595–614, :668–674).

This is a **specification gap**. It is not a quantum failure, and it is not a negative result about
any candidate class: every class stays INCONCLUSIVE, meaning not excluded and not shown to survive.

**Does any candidate qualify for Step 3B (the gate in c.6846442383)?** **No.** None names a concrete
apparatus that can be tested against the central question. Step 3B therefore has no candidate.

**What a qualifying candidate must contain** [W]. A submission names, for one rule, law, mode and
carrier:
1. the generating rule `n ↦ (O_n, C_n, τ_n, r_{O,n}, layout_n)` and `n(ε, K)`, explicitly;
2. the declared target `𝔔*` with `L` and `c₀`;
3. the label encoder, with each component's D6(b) class and the cost `G(ε, K)`;
4. the source of each unsourced ingredient of §3.0 it relies on, or the named hypothesis that carries
   it: in particular the ready configuration, the source of run repetition (F-3A-2), and a physical
   account of the growth of `|C_n|`, at least `½ log_q((1−4ε)/(4ε))`;
5. an argument, not a declaration, that the hidden information the target needs stays inaccessible
   over the horizon with complete reads (T2(d));
6. for R-lin, a statement of which OA-2 Theorem E(b) hypothesis it fails. If it meets all of them,
   with (SP), its prepare–measure fragment would be simplex-embeddable if that result holds; if it
   fails only (SP), the model is still preparation-noncontextual, which is at most a route past T2,
   and it must then say why T1 is not blocked (a Step 3B question at [L] level);
7. how it meets the L4 escape audit (P:842–849): its preparation-to-state map is not an injective
   complete orthogonal frame with H-LIFT, in the approximate, operational form that Step 2 left open
   (S3:283–289; S4:522–523), and `N(ε, K)` is unbounded.

For D this is the construction NL-P asks for, which the owner has not authorized (S4:608–611).

***

## 6. Pressure test of the favourable readings (§A.31)

- **"D remains viable because nothing excludes it."** Rejected as a classification. No R-nl family
  exists in any record. W-nl-2 to W-nl-4 show only that R-nl's single-round record laws on one- or
  two-cell regions are not coset-structured (D.4), a necessary ingredient of MP-1-type control, which a
  classical reversible computer also supplies (OA-1 gap 2, OA1:523; OA-2 N2.3) [R-off]. SM's chaos
  diagnostics are numerical and are not premises (P:108–111). Unexcluded and unconstructed is not
  evidence of a quantum-capable interface.
- **"Incompleteness in TUNE-1 is physically sourced, since D5 forbids declared restrictions."**
  Partly. The source is the boundary of `O_n` and the unread law, not a forbidden read, which meets
  the owner's requirement in form. But `O_n` and its growth are design choices with no physical
  account, and for R-lin OA-2 Theorem E(b) shows incompleteness is not sufficient: the classical model
  needs no recovery of the hidden state.
- **"L5.6 escapes the R-lin obstruction by changing the law."** It escapes FC-1's proof, which needs a
  coset-uniform law. It does not change the translation-only action of labels (Lemma A-T (a), (b) are
  law-free), and OA-2 Theorem E(b) does not need a uniform law. With (SP), the fragment is
  simplex-embeddable; without (SP), it is still preparation-noncontextual (OA2:534, :542). Failing
  (SP) is therefore at most a route past G3 or T2 (OA2:604), not an escape for the central question,
  which needs T1 as well; whether a preparation-noncontextual model can meet T1 at small `ε` is a
  Step 3B question at [L] level, not derived.
- **"The classification of A and C is a negative result."** It is not. It is conditional on an
  off-`main`, WIP result, on (SP) (open, with both halves as above), and on a hypothesis match made
  here without independent confirmation. It classifies; it does not exclude.

***

## 7. Findings and §A.31 classification

- **F-3A-1 (ELABORATING).** For R-lin, the L5.6 laws leave the label action translation-only, so the
  L5.4 and L5.6 init classes face the same route under OA-2 Theorem E(b) [W; R-off]. (SP) is not a
  single pivot: with (SP), the prepare–measure fragment is simplex-embeddable; without (SP), it is
  still preparation-noncontextual, and whether that alone excludes T1 at small `ε` is a Step 3B
  question at [L] level. Assumption-watch marker: a change of law does not change control for an
  affine rule.
- **F-3A-2 (ELABORATING).** Run repetition is used but not stated. TUNE-1's record law is read
  operationally as frequencies over runs, each a fresh draw of `μ` with the apparatus reset to `r_O`;
  B4's trial count `1/p_acc` and trial cost `R(ε, K)` presuppose independent repeated trials
  (AF:283–287), and the proposal speaks of runs a herald accepts (P:174–175). It is separate from
  H-μ, which is a time-zero law. Its antecedents in the corpus:
  - Step 1 lists "a native read and reset" as underived (T1:1625), counts "an unreset carrier" among
    the access countercontrols (T1:1696), and records the sphere model's fresh re-preparation as
    supplied (T1:249);
  - OA-1's MP-0a, "a past-hypothesis-type supply of ready cells" (OA1:556–562) [R-off], is the
    resource that resetting `O` to `r_O` consumes;
  - Main's mixing hypothesis, under which the hidden sector "looks" thermalized at every coupling
    event, with "an exact reset" as its `ε = 0` case (Main:443–449, :498), and (EM), "an additional
    conditional physical premise" (Main:742–758), are the corpus's named premises for refreshing the
    hidden sector [P, conditional]; Main also records that the exact Koopman operator of a finite
    permutation "cannot mix" (Main:758 (ii)).

  Neither MP-0a nor the mixing hypothesis or (EM) is applied to TUNE-1 interfaces. Assumption-watch
  marker: every pass carries run repetition, whose source a concrete candidate must name.
- **F-3A-3 (ELABORATING).** TUNE-1's D4 complete-history record is the type OA-1 names MP-0b and
  meets OA-2's (H4) [W; R-off]. It is an imported convention, which places TUNE-1 R-lin init members
  inside Theorem E(b)'s hypothesis set except for (SP), whose two halves are as in F-3A-1.
- **F-3A-4 (CONFIRMING).** Exchange-mode candidates lie outside OA-2's "no writes outside `φ`" and
  (H3); H-write is the unsourced apparatus there.
- **F-3A-5 (CONFIRMING).** The interface may depend on `K`; T1 certifies per horizon. This restates
  D1 (P:232–236) and the uniformity clause (P:485–486). A horizon-uniform variant is a separate owner
  option (T1-U), with Main:496 as prior art.
- **F-3A-6 (BORDERLINE).** The non-uniform product law of D3 names a class, not a law; a family that
  fixes the marginal adds a free parameter (§A.29). D3's robustness clause (P:268–271) is the existing
  guard against tuning it.

**Productivity verdict (§2): gem, BORDERLINE.** The surviving content constrains a concrete
candidate in two ways: it must name the source of run repetition (F-3A-2), and for R-lin it must
state which OA-2 Theorem E(b) hypothesis it fails, with the two halves of (SP) (F-3A-1, F-3A-3). Both
points are [W] and conditional on off-`main` work.

***

## 8. Hypothesis and premise ledger

| Item | Status | Where it enters |
|---|---|---|
| H-μ (law of the unread world at time zero, independent of the observer) | named, unadopted | every candidate |
| H-∞ | named, unadopted | `𝓛_∞` rows of A–D |
| H-write | named, unadopted | B; exch rows of C, D |
| H-nl | named, unadopted; adoption would be a Layer-0 revision | D |
| Run repetition (F-3A-2) | not stated in TUNE-1's governing texts though used by B4 (AF:283–287); separate from H-μ (a time-zero law); nearest corpus premises MP-0a [R-off] and Main's mixing hypothesis/(EM) [P, conditional], neither applied to TUNE-1 interfaces | every candidate |
| MP-0a-type ready supply (`r_O`, program blocks) | unsourced (OA-1 [R-off]) | every candidate |
| MP-0b-type complete history | imported convention | every candidate |
| Growth of `|C_n|` | admitted resource; no physical account (owner requirement, c.6828822665) | every candidate |
| L4 escape audit | necessary for any pass; exact form proved [W]; approximate form open | every candidate |
| OA-2 Theorem E(b) and its hypotheses (H1), H-AR, (H3), (H4), (xiv), (SP) | [R-off], WIP; (SP) open for TUNE-1, with both halves stated | conditional groups of A, C |
| OA-2 Corollary E1 | [R-off], WIP | D (necessary condition for a G3 escape) |
| OA-3 Lemma OBS, Theorem S, (PT), N4 | [R-off], WIP; Lemma OBS and Theorem S not applicable as stated | context for persistent incompleteness; herald typing |
| Step 2 results (Lemma A-T, FC-1, FC-2, Lemma I, NL-C, NL-C′, W-nl, Lemma F and exact U2(ii)) | [W], Step 2-reviewed, not kernel-checked | §3 |

No premise is adopted.

***

## 9. Reading inventory (§A.19) and disclosure

**Read, on `origin/main` at `080cd2be`** (unchanged at `62bdc2cf` on these paths).
- TUNE-1 directory: `TUNE-1-STEP2-PROPOSAL.md` (in full); `TUNE-1-STEP2-AMENDMENT-1-final.md` (in
  full); addenda 1 and 2 (in full); `TUNE-1-STEP2-SESSION3.md` (in full); `TUNE-1-STEP2-SESSION4.md`
  (in full); `TUNE-1-STEP1.md`, headings, :1–25, and for r2 :249, :1625, :1696. Not read: Sessions 1
  and 2, the C-POS-2 rerun, amendments r1–r3 (their content enters through the final amendment and
  Session 3's control statement, S3:21–22).
- `papers/Main.md`: §3.3 (:358–427); :58, :60, :556, :558, :564, :580, :594, :596; ledger :724 (by
  search for the items cited); for r2 :443–449, :496, :498, :742–758.
- Issue #1236: body and all eight comments, through the GitHub API (read-only), including
  c.6846442383 for r2.

**Read, off `main`, branch `research/oa1-w1-1-20261112` at `2d064a71`.**
- `OA-3-REPORT-r4.md`: :1–200, :220–400, and the lines located by search for Lemma OBS, Theorem S,
  (PT), scope and verdicts; for r2 :124–127, :394–416, :460–475.
- `OA-2-REPORT-r4.md`: :1–200, :236–300, :488–575, :735–780, and search hits for (CVX); for r2
  :102–104, :534, :542, :576–605.
- `OA-1-REPORT-r5.md`: :1–138, :423–462, :488–590.
- `W1-1-REPORT-r4.md`: :1–90 and search hits for verdicts. **No bearing found** on Step 3A: W1-1
  concerns the hidden-sector entropy slope for the ħ calibration; its real-energy premise does not
  touch the `ℤ/q` level-set law of L5.6. Not used.
- `DELTA-REVIEW-OA-3-r4.md`: extracted, not read beyond its existence; OA-3 r4's standing line
  states its verdict.
- For r2: `REVIEW-STEP3A.md` in this unit's directory, in full.

**Searches.** `grep` over the TUNE-1 files for `L5.4|L5.5|L5.6|NL-A|NL-P|NL-C`; over OA-2, OA-3 for
the statements cited; for r2, over Main for the mixing hypothesis, (EM) and the Koopman remark, and
over OA-2 for Proc's heralds and Corollary E1. No search for a concrete TUNE-1 family beyond the
Step 2 records was made; the claim "no member is exhibited" is scoped to the records read, which are
the records that define the classes, and Step 2's own statements (S3:206–211; S4:485–497).

**Not read.** The Lean modules (no statement here rests on one beyond Step 2's citations); SM beyond
the lines Step 2 cites; MECH-1, MECH-2, minacc-1, obsmu, apparatus-1 (entering only through Step 2
and the OA reports); the OA reviews other than as named.

**Commands.** r1: `git fetch`, `git show`, `git ls-tree`, `git log`, `git diff --stat`, `grep`,
`sed`, `head`, `wc`, `cut`, `sha256sum`, `mkdir`, `cat`; GitHub issue reads through the MCP tool.
r2: `git fetch`, `git rev-parse`, `git diff --stat`, `cp`, `cat`, `awk`, `sed`, `grep`, `wc`, `ls`,
`sha256sum`, `mv`, `rm`; GitHub issue reads through the MCP tool. Sources were copied for reading into
`tune1-3a/src/` inside this unit's working directory. No script was written and no computation on
any OI rule was made; the only arithmetic is restated from Step 2. **Disclosure:** while splicing text
into this file for r2, a shell command contained a stray `python3 -` with no script; it waited on
empty standard input, was stopped with the task-stop tool before doing anything, and ran no code and
computed nothing. The splice was redone with `awk`.

***

## 10. Review disposition: change map (REVIEW-STEP3A.md, ACCEPT WITH CHANGES)

Every item was checked against its cited source before it was applied. Line ranges below are in
this file.

| Item | Change | Where in r2 |
|---|---|---|
| R1 | F-3A-2 reclassified ELABORATING; restated as "repetition used but not stated; separate from H-μ; nearest premises MP-0a and (EM), neither applied to TUNE-1", with AF:283–287, P:174–175, T1:249, :1625, :1696, OA1:556–562, Main:443–449, :498, :742–758 (:744, :758 (ii)); ledger rows restated; productivity verdict "gem, BORDERLINE" | §3.0 Repetition row; §7 F-3A-2 and productivity verdict; §8 Run repetition row; §1 summary item 3 |
| R2 | (SP) no longer called a single pivot; both halves stated: with (SP), simplex-embeddable; without (SP), still preparation-noncontextual (OA2:534, :542); whether that excludes T1 at small `ε` is [L] and a Step 3B question; non-(SP) at most a G3/T2 route (OA2:604) | §1 summary item 4 and table (A, C); A.4 persistent incompleteness; A.6 first bullet; A.7; C.6; C.7; §5 item 6; §6 third and fourth bullets; §7 F-3A-1, F-3A-3 |
| R3 | Form 1 adopted: every candidate carries the secondary group "lacks a sourced apparatus" via §3.0, with H-write added for B and the exchange rows of C and D | §1 table preamble and every row; §3.0 preparation reading; A.7; B.7; C.7; D.7 |
| R4 | L4 escape audit added: exact form proved (S3:276–282; S4:519–520), approximate form open (S3:283–289; S4:522–523), necessary for `PASS-DERIVED` (P:842–849; S4:487–491) | A.2; D.2; T1 table (row "Necessary condition"); §5 item 7; §1 table; §8 |
| R5 | c.6846442383 cited and quoted as the governing record for the designation and the first guidance message; its wording governs; second message marked relay-only; eight comments | §0; §1 central question; §1 closing line; §5 gate question; §4.2 T2(d); §9 |
| R6 | T2 flagged as an owner-decision proposal in the summary and in §4.2; C-POS-1 row reworded: meets T1's Q-conditions at `ε = 0`, supplied, not a T1 pass; the [L] expectation scoped to the operational fragment, not the ontic model | §1 summary item 6 and table "Applicable test"; §4.2 status line and controls paragraph |
| R7 | D.4 control claim narrowed to "record laws not coset-structured for single rounds on one- or two-cell regions; a necessary ingredient of MP-1-type control, not shown to be setting-selective control (S4:686–687)"; OA-2 Corollary E1 cited in D.6 | D.4; D.6 (new bullet); §6 first bullet |
| m1 | F-3A-5 reclassified CONFIRMING; Main:496 cited for T1-U | §7 F-3A-5; §4.1 option T1-U |
| m2 | F-3A-6 cites D3's robustness clause, P:268–271 | §7 F-3A-6; C.3 |
| m3 | The readout rule is fixed completely by D4; only its instantiation `O_n` and the preparation prefixes are missing | §1 summary item 2 and table; A.3; §5 |
| m4 | Heralds inside OA-2's Proc; OA-3 N4.1's herald-typing premise met by D4/MP-0b by convention; N4.3 noted; `𝓛_∞` rows rely on OA2:499's window reading | A.6 second bullet; C.6 |
| R8 (optional) | Applied: growth of `|C_n|` marked "admitted resource; no physical account (owner requirement c.6828822665)" | §3.0 growth row; §1 summary item 3; §5 item 4; §8 |
| Reviewer remark on (SP) (not required) | Recorded as an open item for Step 3B, attributed to the reviewer, unverified and not used | A.6 third bullet |
| Reviewer remark on a 3D Lemma OBS (not required) | Not applied; A.4's "undecided" stands, as the review says | — |

**Disagreements.** None with any required or minor edit. Three citation details were adjusted while
applying them, without changing their content:
- the review cites Proc's heralds as OA2:96–97, which is OA-3's citation of OA-2 r3; in OA-2 r4 at
  `2d064a71` the sentence is at OA2:102–104, which r2 cites;
- Corollary E1 is cited as OA2:577–600 (its statement and open exits) rather than :578–590;
- Main's (EM) passage is cited as Main:742–758, since the hypothesis is stated at :744 and the
  Koopman remark appears at :744 and :758 (ii), slightly before the review's :746–758.

**Recheck nits (REVIEW-STEP3A.md, "Recheck of r2", ACCEPT; optional N1–N2, applied by the coordinator).**
- N1: the quoted words "cannot mix" are cited to Main:758 (ii) alone (§3.0 F-3A-2).
- N2: L4(a)'s exact form for R-lin is stated on `𝓛_fin` (A.2), and the T1 table's L4 row reads "exact form proved on `𝓛_fin` only", since Lemma F assumes a finite configuration set (S3:241).

***

## 11. r3 change map (owner decision #1236 c.6847314661, `amaybaum`, `OWNER`, 2026-11-13T07:51:30Z: "Add to Step 3A as r3 (Recommended)")

| Item (owner brief) | Change | Where in r3 |
|---|---|---|
| §2A, items 1–7 | New section "Embedded-observer framing", before the candidate sections: three statements (inclusion, access, control) with (ii) and (iii) to be derived from the joint dynamics; reachable versus definable, and what selects the operating rule; Level A versus Level B, with Main §3.4's characterization quoted with its hypotheses as the nearest bridge; preparation as derivation, linked to MP-0a, MP-0b and F-3A-2; what remains (classical countermodels and supra-quantum constructions, each cited); Step 3A's terms re-read; the reformulated central question | §2A.1–§2A.7 |
| Item 7, recorded beside the existing question | The reformulated central question added after the c.6846442383 central question, which is kept | §1 |
| Terminology: "lacks a sourced apparatus" | Read as "the preparation, control or readout is not shown to be derivable from the joint dynamics", not "a separate machine is missing"; pointer added to the summary-table preamble | §1 table preamble; §2A.6 |
| Terminology: preparation test | Read as a derivation question: is the preparation, and its repetition, derived from the joint dynamics with stated initial or boundary conditions, or assumed | §2A.4; §2A.6 |
| Classifications, verdicts, Step 3B answer | **None changes.** Checked candidate by candidate in §2A.6: primary groups, secondary group, conditional groups, the stop condition and "no candidate qualifies for Step 3B" are as in r2 | §2A.6 |
| Standing line | "r3 adds §2A (owner decision #1236 c.6847314661); review edits E1–E7 applied, awaiting confirmation" | header |

**Review of r3 (§2A), ACCEPT WITH CHANGES: disposition.** Each item was checked against its cited
source before it was applied; the review's wording is used where it gives any. Pre-review text:
`.r3-pre-review.md`.

| Item | Change | Where in r3 |
|---|---|---|
| E1 | #1236 c.6847314661 (`amaybaum`, `OWNER`, 2026-11-13T07:51:30Z) cited and quoted as the governing record; "not on #1236 … stands on the relay" deleted; the comment's wording of the reformulated question given as the record, the relayed wording kept as context, and the comment stated to govern where they differ | header; §1 reformulated question; §2A Source; §2A.7; §11 title and disclosure |
| E2 | The embedded standard is stated for initial-condition mode only (D2, D5; P:198–199, "the strictly rule-only target"); exchange mode supplies (iii) as H-write (P:155–167, :237–239, :563–565) | §2A.1 |
| E3 | For exchange-mode rows the apparatus includes H-write, not implemented by `Φ_F`, so statement (i) itself fails for the apparatus as specified; no classification changes | §1 table preamble; §2A.6 first and secondary-group bullets |
| E4 | NL-C applies to any control whose per-round gate setting is a configuration of a bounded set of cells, designated or emergent; open [O] only for interfaces outside TUNE-1's schema (gates over several rounds, excluded by definition, S4:697; settings not encoded as cell configurations); OA-3's observer-model scope as OA-3 states it (OA3:383–386) | §2A.6 last bullet |
| E5 | §2A.5's supports relabelled: C-POS-1/2 as classical hidden-variable models reproducing one-qubit statistics under supplied access, not constructions under OI's premises; `𝔊_K` as a non-quantum (gbit) theory from a classical reversible substratum with a posited non-affine rule (OA2:769), outside ledger item (vii); `oi_alone_not_qm` as non-standard theories, with Main:582 added; Main:414's Corollary carried with all its hypotheses; E(b)'s classical fragment kept as its own bullet | §2A.5 |
| E6 | D1–D7 with D6 is the class stated without quantum terms; the Q-conditions are the quantum target | §2A.3 open task |
| E7 | "on the two-state carrier" (kernel `substratumGen_not_control`, as Main:80 and :582 cite it) and "within complex matrix kinematics taken as given (Main:562)" added | §2A.3; §2A.5 closing paragraph |
| n1 | Standing line refers to §11, not §10 | header |
| n2 | "nothing makes it the world's dynamics" tagged [W], with Main:580's own clause "uses no property of the substratum beyond finiteness and reversibility" quoted | §2A.2 |
| n3 | The MP-0a/MP-0b route mapping tagged [W] | §2A.4 |
| n4 | AF range aligned to AF:316–326 in §2A.5 and in the disclosure | §2A.5; disclosure below |

**Citation details adjusted while applying the review (no change of content).**
- E2's "strictly rule-only target" is at P:198–199 (the sentence begins at :198), not P:197–198.
- E4's NL-C range is cited as S4:423–462 (statement through the relation to C-CARD (a)) and its "what
  it does not use" as S4:457–458, rather than S4:441–466 and :458–462.

**Disagreements.** None.

**r3 disclosure.** Read for r3, at `origin/main` `62bdc2cf` (`papers/Main.md` byte-identical to the
copy read at `080cd2be`; the TUNE-1 directory unchanged): Main:26, :28, :32, :40, :42, :58, :66, :80,
:360, :427, :429–442, :554, :562, :580, :582, :584 and search hits for "realization datum",
"typicality", "operational completion", "non-quantum" and `substratumGen_not_control`;
`papers/SM.md`:104 and :112; OA-3 r4 :138–141 and OA-2 r4 :769 at `2d064a71`; AF:316–326;
P:197–199, :237–239; S4:441–466, :697. #1236 c.6847314661 read through the GitHub API (read-only).
For the review edits: "Review of r3 (§2A)" in `REVIEW-STEP3A.md`. Commands: `git fetch`,
`git rev-parse`, `git diff --stat`, `git show`, `git hash-object`, `cp`, `cmp`, `cat`, `awk`, `sed`,
`grep`, `tail`, `rm`. No interpreter was run, no script was written and no computation on any OI rule
was made.
