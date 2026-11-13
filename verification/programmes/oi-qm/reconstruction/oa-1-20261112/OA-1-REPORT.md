# OA-1: can one fixed deterministic substratum supply preparation, control, measurement and complete records?

**Standing.** WIP / UNVERIFIED author report for unit OA-1 under #1169. Authorization: owner
amaybaum, 2026-11-12, recorded in #1169 comment 6829742537 ("A: observer–apparatus (#1169)"),
paper-only, together with the owner-approved scope addition relayed by the coordinator ("Fold into
OA-1 (Recommended)"). This file adopts no premise, promotes no claim, edits no manuscript or Lean
file and runs no computation on any OI rule. It is not independently reviewed. The unit ends with
an independent review and an owner decision checkpoint (owner's limits). TUNE-1 Step 3 stays
paused.

**Snapshots.** `main` = `fb733b4a58558ef64bd7c3585712c76e9f2dfb42` (cited `Main:n`, `OB/File:n`
for `verification/lean-mathlib/OIBridge/`, and record paths relative to
`verification/programmes/oi-qm/reconstruction/`). TUNE-1 records are read from branch
`research/tune-1-20261111` at `d47a6377f2d8753f88ddc4d3ab0c03ead64393dd` (cited `T1/<file>:n`).
They are off `main`, reviewed only as their headers state, and are used as cited research
results, never as established premises (§A.46 item 7).

**Support labels.** **[K]** Lean statement on `main`; I read the statement text and, where noted,
the proof text; I built nothing. **[P]** manuscript statement on `main`. **[R]** research record
(on `main` or the TUNE-1 branch) that states it is not independently established. **[W]** my own
derivation in this file, unreviewed and not kernel-checked. **[O]** open.

**Disclosure.** Commands run: `git` (fetch, show, ls-tree, grep, log, rev-parse, status, diff
--stat), `grep`, `sed`, `wc`, `ls`, `mkdir`, `cat -n`, one `curl` of the GitHub API for comment
6829596317, and one `python3 -I` JSON parse of that response's author, date and length. GitHub MCP
reads of #1169 and its last comments. No interpreter or probe touched an OI rule. Nothing was
committed, pushed or posted. The output directory already held files dated 2026-10-20
(`EXCERPTS.md`, `H-extension-candidates.md`, `I-f2-sufficiency-target.md`, `NODE1*.md`,
`probe/`) that this session did not write. They were not opened, used, changed or removed. The
repository working tree is clean.

***

## 0. Plain-language summary

1. The exact theorem S⇔D⇔Q_fb never fails, but it chooses the world after the target. It shows
   that some world fits, not that a given world supplies the operations.
2. With one world fixed in advance (the corpus's linear lattice rule), I followed four operations
   in order: prepare, control, measure, record.
3. Preparation fails first, but for a reason classical computers share. Under OI's own
   maximum-entropy measure, nothing the observer physically holds now says anything about the
   hidden world now. Preparing a hidden carrier therefore needs either a low-entropy starting
   supply or a memory of history the observer does not physically keep.
4. Grant that resource. Control then fails: under the linear rule a setting stored in the world
   can only shift values. It cannot choose which operation runs or which quantity is read. An
   ordinary classical reversible computer can do this, so the first real gap is classical.
5. Grant control as well, even full classical write access. The kernel then caps the current
   observer interface: no phases and no dense control. No change of rule can lift that cap.
6. Only a change in what an "observer operation" acts on could escape. None of the candidates on
   `main` does so without supplying the answer by hand.
7. One new tension (unreviewed): an observer that keeps complete records in its own
   configuration sees, under OI's canonical measure, only a memoryless chain. OI's signature
   hidden readback is then invisible to it.

***

## 1. Definitions in OI's own terms

**Data of one physical setup.** `𝔖 = (S, φ, (V, H), μ, A)`:

- `S` is finite (Main:60, ledger item (ii) at Main:724), and `φ` is a bijection fixed **before**
  any target is named;
- `V ⊊ S` is the observer's registered configuration and `H` the hidden sector (Main:42, :48);
- `μ` is the canonical counting measure of Lemma 3 (Main:54), or a structured prior declared as a
  realization datum (Main:58). The latter is a named premise wherever used.
- `A` is the apparatus layout: which cells play carrier, setting, meter and record. It is chosen
  once for every setting.

There is no write access outside `φ`. Settings are configurations of designated cells, set as an
initial condition or written by `φ` from the observer's own records.

**Native / premise / not supplied.**

- An operation is **native** if `(φ, partition, μ_canonical, A)` supplies it, with every
  probability computed from `φ` and `μ`.
- It is **supplied under a named premise** if it needs one extra named statement and that
  statement carries no target data.
- It is **not supplied** if neither holds.

**Non-import test (hard-to-vary form, §A.29).** A construction imports its target if its supplied
elements can be re-tuned, with `φ` and the partition unchanged, to realize a non-quantum target
with equal ease. Example targets: a gbit, Born exponent `p ≠ 2`, or an arbitrary finite instrument
table.

**The four operations.** Each has an infrastructure tier (target-neutral) and a qubit tier (§4.2).

| | Operation | Infrastructure tier (what counts as supplying it) |
|---|---|---|
| N1 | Preparation | A record event `E` with `P(E) > 0` reported, and its complement recorded as failure. A designated carrier `Σ` (possibly hidden) whose conditional law at the preparation time `ν_E` differs from its unconditional law. `E` is held by the observer when `Σ` is next used, and `ν_E` does not depend on later settings. |
| N2 | Controllable interaction | Setting cells `s` and a duration `τ` such that `φ^τ` acts on `Σ` by a map whose **non-translational part** depends on the content of `s`, for at least two operationally distinct values. `s`'s initial law is independent of `Σ`'s (ledger item (xiv), Main:724). |
| N3 | Measurement | A meter whose later recorded value is correlated with a functional of `Σ`. **Selectable**: which functional is read is fixed by a setting (N2). The residual `Σ` is handed on. |
| N4 | Complete records | Every outcome, herald and failure of a protocol is physically held in `V` at the end, together with the observer's knowledge of the residual carrier. Records are not lost to `H`. |

***

## 2. Facts derived here (paper, [W] unless cited)

**D1 (stationarity; any bijection, any φ-invariant μ).** `μ∘φ⁻¹ = μ`, so the unconditional law of
the full state is the same at every time. No dynamical step prepares anything unconditionally.
Every time-specific preparation, and every new same-time correlation between record and carrier,
is a property **conditional on a record event**. ∎

**D2 (equal-time blindness, every bijection, counting measure).** Under the counting measure the
law at time `t` is uniform on `S`. For disjoint `X, Y ⊂` cells, `X_t` and `Y_t` are therefore
independent and uniform. In particular `V_t ⊥ H_t` for every `t`, and every function of `V_t`
(any physically held record, memory included) is independent of the present hidden state. This
generalizes Lemma P-1 and Lemma Q-b1 of `observer-interface-obsmu-20261104/ANALYSIS.md:529–545,
:907–912` [R], stated there for automorphisms, to every bijection. The proof is the same: the
pushforward of a uniform law under a bijection is uniform. ∎

**D3 (herald bound).** For any event `E` and carrier `Σ`,
`P(Σ_t = σ | E) ≤ μ(Σ_t = σ)/P(E)`, which under counting measure is `1/(|Σ| P(E))`.
- A preparation whose most likely value has probability `p_max` succeeds with
  `P(E) ≤ 1/(|Σ| p_max)`.
- Point-preparing `M` distinct `q`-ary cells at one time costs `P(E) ≤ q^{−M}`, with equality for
  the herald "those cells read the target values".
- Ready meters, blank ledger slots and heralds are therefore exponentially rare resources under
  the canonical measure. ∎

**D4 (records versus readback; new candidate, see §7).**
- (a) For any law, `M_t = I(X_{<t}; X_{t+1} | X_t) ≤ H(X_{<t} | X_t)`. If the observer's present
  configuration determines its whole visible history (complete records in `V`), then `M_t = 0`
  and (C4) fails at `t` for that configuration.
- (b) In a bijective realization under counting measure with complete in-`V` records,
  `P(V_{t+1} = v' | V_{≤t}) = P(V_{t+1} = v' | V_t)`, because the history is a function of
  `V_t`. That equals `T(V_t, v') = |{h : π_V φ(V_t, h) = v'}| / |C_H|`, since `H_t ⊥ V_t` and
  `H_t` is uniform (D2). The observer's own process is therefore the homogeneous Markov chain of
  the uniform-prior one-step kernel `T`, which is doubly stochastic (Main:60). The hidden sector
  acts on it as fresh memoryless noise at every step.
- (c) This agrees with Main:97: in a bijective realization `I(X_{<t}; H_t | X_t) = H(X_{<t} | X_t)`.
  The hidden predictive memory is exactly the part of the history that `X_t` does not hold. ∎

**D5 (Lemma A, re-derived).** Let `Φ` be additive on the configuration group, as under R-lin
(`Φ_F(y, x) = (x, Ax − y)`, item (xiii) at Main:724). Take the initial state `(c, x, u)`: setting,
carrier, rest. Then `Φ^τ(c, x, u) = L_c c + L_x x + L_u u` with `L_•` independent of `c`.
- The carrier's map is `x ↦ (L_x x + L_u u)|_Σ + (L_c c)|_Σ`. Its non-translational part does not
  depend on `c`.
- Every record is `H_O r_O + H_P c + H_U u`. The functional each record reads (`H_U`, `H_O`) is
  independent of `c`, and the record law is uniform on a coset of a `c`-independent subgroup.
- An affine exchange that writes `c` into cells changes nothing above, because its linear part
  `I − Π_C` does not involve `c`.

This reproduces MECH-1 Lemma A (`mechanism-1-20261107/DESIGN.md:95–98`, :402–437 [R]) and
TUNE-1 Lemma A-T (`T1/TUNE-1-STEP2-SESSION3.md:32–98` [W], ACCEPT WITH SCOPE QUALIFICATIONS
review recorded in `T1/TUNE-1-STEP2-SESSION4.md:13–16`). ∎

**D6 (the ceiling is monotone; point 3).**
- `NonnegBounded T` quantifies over `T`'s available one-outcome composite operations
  (`OB/FrozenSourcing.lean:65`). Hence any `T′` whose such operations are among `T`'s inherits it.
- More directly, any theory generated from configuration bijections by the closure rules of
  `FiniteOperationalTheory` (`OB/OperationalAssembly.lean:594`ff.) preserves entrywise
  nonnegativity: coarse-graining (sums), feed-forward composition, attaching a uniformly mixed
  ancilla (`prepAvail_uniform`, the only preparation assumed), Lüders ancilla readout `P_k·P_k`
  with 0/1 diagonal `P_k`, and partial trace. This is the kernel's
  `nonnegBounded_of_bijectionLevel` (:74) for any bijection-level architecture.
- So restricting availability to what a given rule `φ` generates can only shrink a theory inside
  the ceiling. ∎

**D7 (post-hoc and timing "selection" do not supply N2).**
- If no setting changes `φ`'s action, the joint law of every record is setting-independent.
  "Choosing a read" then means choosing which already-made record to consult, so every selectable
  read is a coarse-graining of one joint record and is jointly measurable with the others. The
  read order on a given preparation is fixed by the rule.
- Selecting by preparation timing (prepare at even tick, then the rule reads `z`; at odd tick, it
  reads `x`; `apparatus-1-20261107/DESIGN.md:379–390`) turns the setting into a different
  preparation procedure. Each procedure then has only one read available. Operational equivalence
  of the two procedures, which needs both reads on one procedure, cannot be certified, and the
  setting is a function of the preparation record, against setting independence. ∎

***

## 3. The debugging ladder

The stronger target is held fixed: one physical `𝔖` across all settings, with source-derived
preparation, control, readout, failures and residual state. "Holds" refers to the rung's theorem;
"target" refers to that fixed target.

### R0. `finite_horizon_equivalence` (S⇔D⇔Q_fb)

- **Holds [K].** `OB/Equivalence.lean:462–469` assembles `S_imp_D` (:422), `D_imp_Qfb` (:294) and
  `Qfb_imp_S` (:245) [P, Main:546–552].
- **What it uses.** `RevReal` (:157) allows any `Hid`, step and initial law. `S_imp_D` builds a
  clock-and-trajectory carrier and sets `init := marg P ι`, so the target law is in the prior.
  `D_imp_Qfb` uses a permutation unitary.
- **Target.** None of N1–N4 is addressed. There are no settings. The "records" are a complete
  trajectory held in `H`, not in `V`, and the readout is fixed-basis by definition. The world is
  chosen after the law, so the rung cannot fail. This confirms the trace's rung 0.

### R1. + embedded readback (C1–C4)

- **Holds [P/K].** Main:68–80 and Main:602–612, with the kernel's `pushforward_identity` and
  `distinguishability_floor` (cited at Main:97). C4 forces readout-relevant hidden predictive
  memory in every faithful completion. Representation is untouched.
- **Target.** Unchanged: C1–C4 supply no setting, preparation or record mechanism. The C2
  persistence that reversibility supplies is global (Main:74) and does not retain records in `V`.
- **New tension (D4).** C4's discriminating memory is exactly the history `X_t` does not hold
  (Main:97). Complete in-`V` records make the observer's own process Markov with kernel `T` under
  counting measure. "Complete records" (N4) and "visible C4 readback" therefore compete for the
  same history.

### R2. + one common realization for a fixed finite experiment

- **Holds [P; certified by probes, no kernel].**
  - Comb theorem: Main:480–482. Settings enter as externally indexed bijections `𝓘_a`. The hidden
    variable `u_c ~ P(·|c)` carries the target table.
  - Gluing theorem: Main:564–578. The hidden "density register" and "pre-loaded seeds" carry the
    quantum state and instruments.
  - Single controlled dynamics: Main:580, verbatim "Quantum mechanics enters as the instrument
    data and as the state held in the hidden register". The program is "paid for as an initial
    condition".
  - Uniform continuum realization: Main:596.
- **Target.** All four operations are realized, but supplied as data. The construction fails the
  non-import test by its own statement: "the same reversible machinery can realize non-quantum
  finite instrument families" (Main:582). Records are complete because ledgers are initialized by
  a structured prior (Main:522), which D3 shows is not free under the canonical measure.
- **Classical control.** This rung passes any finite target, classical included. Its criteria
  cannot discriminate. This confirms the trace's rung 2 ("existence for supplied data").

### R3. + sourcing from the actual substratum and observer access (the depth-first chain)

Fixed rule: **R-lin**, the second-order linear nearest-neighbour rule, the only rule the corpus
posits (items (vii) and (xiii), Main:724). The bijection class in general and the nonlinear
candidates are treated as scope remarks at each node.

**Node N1 — preparation.**
- **N1.1 Strict reading** (records are what `V` physically holds; `μ` canonical).
  - By D2, conditioning on anything in `V_t` leaves `H_t` uniform. No hidden carrier is prepared
    by a record the observer holds at the preparation time. This is
    `observer-interface-obsmu-20261104/ANALYSIS.md:911–912` [R], generalized to every bijection [W].
  - Verdict: **not supplied natively, for every φ.** The cause is target-neutral: the classical
    control fails here too (§4.1).
- **N1.2 Under a named premise.** Either of two premises supplies conditioning-based preparation:
  - **H-MEM:** the observer conditions on its visible history, which `V_t` does not contain. This
    is the convention behind Main's trajectory laws (Main:97). It is not a physical record.
  - **H-LOW:** a structured, lower-entropy prior with ready cells, declared as a realization datum
    (Main:58). Apparatus-1's P2 is an instance (`apparatus-1-20261107/DESIGN.md:298–303`, :418).
  - Reading the conditional as a laboratory preparation is the open hypothesis H-PREP
    (`observer-interface-obsmu-20261104/ANALYSIS.md:892–900`; owner D-OB8, not adopted).
- **N1.3 Content under R-lin.**
  - Every conditional law of a set of functionals given records is uniform on a coset
    (`T1/TUNE-1-STEP2-SESSION3.md:48–79` [W]; obsmu Proposition C, :546–575 [R]). Heralds give
    mixtures of these.
  - Infrastructure tier: supplied under H-MEM or H-LOW, plus H-PREP, at cost D3.
  - Qubit tier: only stabilizer-type states.
    - At odd `q` there is no non-stabilizer and no Wigner-negative state
      (`mechanism-1-20261107/DESIGN.md:93–94`, Proposition C [R]).
    - At `q = 2` with heralds: open (`T1/TUNE-1-STEP2-SESSION3.md:196–215`, L5.4).
- **N1.4 Pressure test (favourable branch).** "Supplied under a premise" is not native supply.
  H-MEM is a modelling convention, not a mechanism. H-LOW is the corpus's own past-hypothesis
  datum. Main §4.6 replaces that datum only "in its role of selecting observer-compatible
  configurations" (Main:742; obsmu :233–236). It does not supply ready cells, so the supply role
  stays a premise.

**Node N2 — controllable interaction (granting N1 under H-MEM or H-LOW).**
- **N2.1** D5: under any additive rule, a setting held in the world enters every carrier map and
  every record only as a translation. Which non-translational map runs, and which functional is
  read, are setting-independent. D7 closes the post-hoc and timing loopholes.
- **Verdict: not supplied natively under R-lin.** This is proved on paper three times: MECH-1
  Lemma A [R], TUNE-1 Lemma A-T [W, reviewed], and D5 here.
- **N2.2 Scope.**
  - A generic bijection can contain a classical controlled permutation `(s, x) ↦ (s, g_s(x))`, and
    a classical reversible computer has one natively (§4.1). The gap is therefore classical: R-lin
    is weaker than the classical control at N2.
  - Apparatus-1 obtains setting selection only through P3, per-tick and per-edge arming loaded by
    a classical controller, with E-iso (`apparatus-1-20261107/DESIGN.md:288–293`, :420).
  - MECH-1 shows that an in-world setting must be non-affine, and names M1 / CTRL-MON with
    residual supplied elements (a)–(e) (`mechanism-1-20261107/DESIGN.md:797–893`, :938–1050 [R]).
  - Nonlinear candidates:
    - R-nl (under H-nl): open (`T1/TUNE-1-STEP2-SESSION4.md:553–628`).
    - G_SM (SM §3.1, a stated hypothesis): switches natively, but is non-reciprocal, breaks A5,
      and its instruments are not CP (`mechanism-2-20261108/DESIGN.md:35–131` [R]).
    - The Fredkin switch is not identified with the selected ring
      (`controller-preparation-1-20261108/SELECTION.md:105–121` [R]).
- **This is the earliest operation with no native supply that survives the resource premises.**

**Node N3 — measurement (granting N1 and N2 by premise).**
- A fixed, unselectable read stream is native: `O`'s cells carry fixed linear functionals of the
  carrier, which rotate `z, −x, −z, x` for an isolated cell
  (`mechanism-1-20261107/DESIGN.md:815–823`).
- Backaction is native given half-known meters, from symplectic reciprocity
  (`apparatus-1-20261107/DESIGN.md:311–325`).
- A selectable read is not supplied (D5(ii), D7). Repeatability needs P1 and E-iso.
- Under the configuration interface a passive internal observer can only read an existing record
  (`OB/InternalObserver.lean:92`, :272, :290 [K]; Main:590).
- Verdict: **fixed read native; selectable read not supplied** (it inherits N2).

**Node N4 — complete records, failures, residual state.**
- Under R-lin no cell is inert: every cell is coupled at every tick, so values in `O` are
  overwritten and disperse.
- Retention in `V` needs P1 and E-iso (posits) or a ledger with blank slots. Blank slots cost D3
  or need H-LOW. O-RET, O-REC and O-ACC are open
  (`observer-interface-obsmu-20261104/ANALYSIS.md:913–925`).
- The residual hidden carrier is independent of every physically held record under the canonical
  measure (D2). Knowledge of it rests on H-MEM or H-LOW.
- Complete in-`V` records make C4 invisible to the observer (D4).
- Verdict: **not supplied natively.** Supplied under P1, E-iso and H-LOW. H-MEM supplies only the
  convention, not the records.

### R4. The current observer interface `obsTheory 𝒮 := permTheory 𝒮.Conf`

- **Holds [K].**
  - `OB/SubstratumInterfaceAudit.lean:770` (definition), :775 (`rfl`), :780
    (`obsTheory_rule_independent`, `rfl`).
  - :790 `obs_dynamics_avail`: the rule's own update is available.
  - :816 `obs_exchangesAvailable`: every exchange is available.
  - `OB/FrozenSourcing.lean:84` `obsTheory_nonnegBounded`; :277 `obs_dynamics_preservesNonneg`;
    :295 `sourcing_rule_independent`; :302 `phase_ceiling_rule_independent`.
  - :318 `frozen_sourcing_verdict` and :327 `nonnegBounded_verdict`: no phases, no dense unitary
    control (stated on `Fin 2`), not `DerivedOI`.
  - `OB/StructuralClosure.lean:348` `substratumGen_not_control`; `OB/SubstratumInterfaceAudit.lean:708`
    `permTheory_not_control`.
- **Relation to R3.**
  - On N2 the interface over-supplies relative to one fixed `φ`. It grants every configuration
    permutation, i.e. classical write access, which is H-write in TUNE-1's terms
    (`T1/TUNE-1-STEP2-PROPOSAL.md:155–167`).
  - On N1 it assumes only a uniformly mixed ancilla (`prepAvail_uniform`), with pure seeds
    reached by readout. This matches D1–D3.
  - Granting more classical control than R3 has, it still fails the qubit tier, at kernel level.
- **Point 3 (coordinator): confirmed, with three precisions.**
  1. Rule-independence holds by `rfl`, because the definition never mentions `R`. The substantive
     reason is maximality: `permClass` contains every permutation matrix
     (`OB/SubstratumInterfaceAudit.lean:406`), and the rule's update is one of them (:790; also
     `OB/FrozenSourcing.lean:277`).
  2. Any rule-derived interface **on the configuration carrier**, generated from the rule's
     bijections by the closure rules, is inside `NonnegBounded` (D6, via `:74`). It need not be a
     literal sub-theory. `nonnegBounded_verdict` then excludes phases, dense control (on `Fin 2`)
     and `DerivedOI`; the phase exclusion holds on every carrier (:99).
  3. "Use the rule to decide availability" therefore only shrinks availability under the ceiling.
     An escape must change what an observer operation acts on: its carrier, level or
     identification.
- **What the trace (#1169 c.6829596317) misses.**
  - It treats rule-blindness as the defect and proposes rule-sensitivity (its §C, D3) as the test.
    By D6, rule-sensitivity at the configuration level cannot help. Its §C allows the source map to
    be "replaced", but does not say this is forced.
  - It also does not note that the interface already over-supplies control (write access), so its
    first proved loss sits after a classical gap (R3/N2) that it does not record.

### R5. Candidate replacement interfaces

| Candidate | Escapes the R4 ceiling? | Source of escape: native or imported | Existing no-go theorems | Classical control | Single-qubit target |
|---|---|---|---|---|---|
| **5a.** Rule-derived availability on configurations | No (D6) | — | `nonnegBounded_verdict` [K] | Classical | Fails T-C |
| **5b.** Nonlinear or state-dependent rule (R-nl, G_SM), configuration level | No (D6). Fixes R3/N2 for G_SM only, as a proposal | Rule change; G_SM is an SM hypothesis | As 5a; at encoded level, MECH-2 Lemma F, Theorem U2 and Theorem NC [R] | Fredkin-type switching is classical | G_SM: non-CP instruments, no non-Clifford unitary (U2) |
| **5c.** Visible quotient: encoded carrier through a fixed linear frame (R1, Gross R-W, 8-point model) | Partly: encoded Clifford, e.g. a Hadamard from a hidden permutation (`states-dynamics-audit-20261024/operational-quotient-v3/REPORT.md:11–23` [R]) | The identification, a representation choice. The frame is chosen for the comparator's covariance (`mechanism-1-20261107/DESIGN.md` SC-1). Partly imported | Capped: finite encoded group (U2(ii)); nonnegative frame branches (Lemma F); noncontextual under injectivity, H-LIFT and spanning reads (Theorem NC); no exact `rot` on any finite carrier (`apparatus-1-20261107/DESIGN.md:955–1023` [R]; Main:558 [P, half imported]); error floor 1/15 for one non-Clifford rotation (op-quotient :218–230) | Passes only as a classical epistricted (Spekkens) model, so it does not discriminate | Stabilizer and Clifford only. Fails T-P (non-stabilizer state) and T-C |
| **5d.** Record level: operations are maps on record laws; states are classes of heralded preparations under the available reads | Not shown. Possible only if (i) the access restriction is derived from `φ` (M-INACC) and (ii) the carrier is unbounded (Main:558 for exact; bounded `\|C\|` excluded at fixed ε, `T1/TUNE-1-STEP2-SESSION4.md:556–563`) | Target-neutral if achieved. The escape would come from derived inaccessibility | Theorem NC applies unless injectivity or H-LIFT fails, which is M-INACC's content. M-INACC is not supplied by G_SM (MECH-2 §6.2) or by `G_σ` (`minacc-1-20261108/RESULT.md:37–60` [R]). TUNE-1 R-lin and R-nl give FAIL-CLASS on bounded subclasses and INCONCLUSIVE otherwise | Full access: commutative, so complete passive observation is possible (`OB/CentralObservation.lean:620` [K]). Supplied restriction (KS sphere): flagged by the non-import test | Exact needs an infinite carrier; approximate needs growing `\|C_n\|` and derived access. Open |
| **5e.** Emergent amplitude space (Main §3.4 lifts, wave-operator lift) | Only by adding real amplitudes, an isolated pair and a loaded coefficient (E-real, E-pair, E-control; `oi-qm-ext-1/two-mode-drive.md:25–40` [R]) | Imported. `U_φ` is a permutation unitary (Main:552); every reversible coherent lift of a permutation is monomial (`OB/LiftSource.lean:164` [K]); lifts are not unique (Main:644); layer flows are not executable from observer access (`OB/ExecSource.lean:129` [K]); the wave-operator formulation is unresolved (Main:588) | With the native sign read, the amplitude dictionary does not factor through a density matrix (`oi-qm-ext-1/whole-model-bridge.md:14`, :242 [R]) | A plainly classical real harmonic lattice has the same unitary normal-mode representation (Koopman–von Neumann type) [W]. It would pass, so this is an import | T-C reached only with supplied E-real, E-pair and E-control. T-M not reached |
| **5f.** Infinite substratum, quasilocal (H-∞) | No by itself: a one-site phase is induced by no reversible finite-range dynamics (`OB/QuasilocalCharacterization.lean:792` [K]) | — | Necessary for exactness (Main:558), not sufficient | — | Must be combined with 5d |

**Smallest non-importing change.** The candidates on `main` give no construction.
- The smallest change the no-go theorems leave open is 5d with M-INACC and an unbounded carrier:
  the observer's operations act on record-equivalence classes, and the inaccessible functional is
  derived from `φ`.
- No construction of it exists on `main`. Every partial instance either supplies the restriction
  (KS sphere, Apparatus-1 P1/P2/P3) or fails it (G_SM, `G_σ`, R-lin bounded subclasses).

***

## 4. Controls

### 4.1 Classical control

Take `𝔖_F`: a classical reversible computer built from Fredkin controlled exchanges
`(s, a, b) ↦ (s, s ? b : a, s ? a : b)` with a clock register, under the counting measure, then
under H-LOW.

| Criterion | Result for `𝔖_F` | Is the criterion too weak? |
|---|---|---|
| N1 strict | Fails (D2 holds for every bijection) | No. The failure is target-neutral and correctly shared |
| N1–N4 under H-LOW | Passes: heralded preparation, setting-selected routing, ready-meter copies, ledgers | Infrastructure is meant to be target-neutral. It is not used as a quantumness test |
| Qubit tier, configuration identification | Fails. `permClass`, so no phases and no dense control (`OB/FrozenSourcing.lean:327` [K]). Reads are compatible: complete passive observation of a commutative algebra (`OB/CentralObservation.lean:620` [K]) | No |
| Qubit tier, restricted-access classical models (KS sphere: `states-dynamics-audit-20261024/history-architecture-v5/REPORT.md:1–60` [R]; Spekkens toy; Main's gluing) | Passes T-P to T-R (exactly or within ε) | Caught by the non-import test: the response function, preparation cone and instrument data can be re-tuned to non-quantum targets |

So the criteria do not pass a plainly classical system trivially. They also expose that R-lin is
**weaker than the classical control at N2**.

**Limit of any single-qubit test.** One qubit has classical hidden-variable models (Bell 1966;
Kochen–Specker 1967). The qubit tier can therefore test *sourcing*, not quantumness. Any finite
OI model that met it would itself be a preparation-contextual hidden-variable model.

### 4.2 Single-qubit target, at accuracy ε and horizon K

- **T-P.** Heralded preparations with reported `p_acc` whose conditional read statistics lie within
  ε of `(1 + r·n)/2`, for `r` in an ε-net of the Bloch ball. The net includes a non-stabilizer
  pure state, e.g. `r = (3/5, 4/5, 0)`, and two preparations with equal Z law and different X law.
- **T-C.** A setting-selected reversible family about two non-parallel axes at a non-Clifford
  angle (`cos θ = 3/5`). After `j ≤ K` applications the read statistics are within ε of
  `cos²(jθ/2)`-type laws, and compositions are consistent.
- **T-M.** At least two selectable sharp reads, Z and X (Y for spanning certification), each
  chosen after the preparation and independently of it. Lüders update: repeatable, and Z then X
  gives a uniform X.
- **T-R.** Every outcome, herald and failure is recorded with no renormalization of rejected runs.
  The residual carrier handed to round `j+1` matches the Lüders post-state.
- **D.** One fixed `𝔖` for all of the above, chosen before the target; no write outside `φ`; the
  non-import test passes.

| Claimed supply | T-P | T-C | T-M | T-R | D |
|---|---|---|---|---|---|
| Main gluing and single controlled dynamics (Main:564–582) | ε-pass | ε-pass | ε-pass | pass | **Fails**: quantum data in the hidden register; realizes non-quantum families too |
| Comb theorem (Main:480) | per menu | no continuum (Main:486) | per menu | pass | **Fails**: `u_c ~ P(·|c)` holds the target |
| Apparatus-1, R-lin `q = 2` with P1, P2, P3, E-iso, H-PREP | stabilizer only | no encoded S, no `rot` (Lemma 5) | Z/X Lüders exact, all four settings | heralded failures pass | **Fails** at P3 (setting), P1, P2, E-iso |
| MECH-1, odd `q` | stabilizer, Wigner ≥ 0 | Clifford only, needs NNB (M2) | stabilizer instruments | under posits | **Fails** native setting selection (Theorem T) |
| MECH-2, G_SM at `q = 2` | P★ non-stabilizer, but in a non-CP instrument | no non-Clifford (U2) | Z/X only | — | G_SM is a hypothesis; fails C-CP |
| B1 two-mode drive | point preparations | every angle | the native sign read is not quantum (E-AR) | — | **Fails**: E-real, E-pair, E-control supplied |
| KS sphere model | exact | exact | exact (projective) | exact | **Fails**: everything supplied |
| Operational quotient v3 | stabilizer region | 24 Clifford actions; error ≥ 1/15 non-Clifford | — | — | supplied region and seeds |
| TUNE-1 R-lin and R-nl | FAIL-CLASS for subclasses; else INCONCLUSIVE | same | same | same | H-μ, H-write (exchange mode) carried |
| `obsTheory` (R4) | readout conditioning only | **fails [K]** | passive record reads only | idealized | over-supplies write access |

***

## 5. Earliest unsupplied operation and the missing premises

The answer depends on what is granted. The order is the owner's ladder and the N1–N4 order.

**MP-0 (first, at N1; target-neutral resource).**
- *Statement:* the observer holds, at the time of use, records correlated with the present state
  of a hidden carrier. Either H-LOW (a declared lower-entropy prior with ready cells) or H-MEM
  (the observer's visible history counts as its record) supplies this.
- *Physical content:* a past-hypothesis-type supply of known or blank degrees of freedom, or an
  observer memory outside `V`.
- *Why it is not supplied:* D2 for every bijection under the canonical measure. Lemma 3 selects
  the maximum-entropy measure, which is the opposite. Main §4.6 does not supply ready cells.
- *Hard to vary?* No. Any supply pattern works, and its known consequence (record asymmetry) is a
  retrodiction. It carries no quantum content, and classical computing needs it equally.

**MP-1 (earliest gap that survives MP-0, at N2; classical).** **M-CTRL**: the fixed rule contains
a setting-selective interaction.
- *Statement:* cells `s`, carrier `Σ` and a duration `τ` exist such that the non-translational part
  of `φ^τ|_Σ` depends on the content of `s`. The content of `s` is preserved or recorded, its
  initial law is independent of `Σ` (ledger item (xiv)), and the timing is sourced (a clock in
  the state).
- *Physical content:* the micro-dynamics contains conditional (switch-like, necessarily non-affine)
  couplings.
- *Why it is not supplied:* the posited rule is additive (items (vii) and (xiii)), so D5 applies.
  The only corpus candidate that switches natively, G_SM, is a stated SM hypothesis that is
  non-reciprocal, breaks A5 and is non-CP. The selected ring sources no Fredkin switch.
- *Hard to vary?* No in its bare form. Any nonlinear rule of many kinds supplies it, and no
  independent prediction has been identified (as MECH-1 found for CTRL-REC,
  `mechanism-1-20261107/DESIGN.md:960–973`). It is necessary for any apparatus and carries no
  quantum content. This is MECH-1's M1 restated at the infrastructure tier.

**MP-2 (the structure to replace, at R4 and R5).**
- *The structure:* the identification of observer operations with configuration-basis matrices,
  `obsTheory 𝒮 := permTheory 𝒮.Conf`. No rule change can lift it (D6).
- *Smallest non-importing replacement:* candidate 5d with **M-INACC** (MECH-2 §6.2): per encoded
  system, an ontic functional that the fixed rule uses and that no permitted preparation, read,
  reuse or recombination can access, with a reason not chosen to reach the target. It needs an
  unbounded carrier.
- *Why it is not supplied:* no rule on `main` has been shown to supply M-INACC. G_SM fails it,
  `G_σ` fails it, and Lemma Q's protection holds only under P1 and P2.
- *Hard to vary?* No in its bare form. It becomes hard to vary only if the specific inaccessible
  functional is fixed by `φ` and yields a prediction beyond the qubit fit.
- **If MP-0, MP-1 and MP-2 all held, sufficiency for the qubit target is still not shown [O].**

**Earliest rung at which the target fails.** R0–R2 do not refute the target; they meet it only
with supplied data. The first rung that tries to source it is R3, which fails at N1 (strict
reading, every φ) and at N2 for R-lin (granting MP-0, on paper). The first kernel-proved failure
is R4, granting even full classical write access.

***

## 6. Status table

| Item | Status | Support |
|---|---|---|
| S⇔D⇔Q_fb | proved | [K] `OB/Equivalence.lean:462` |
| Hidden predictive memory = unstored history, `H(X_{<t}|X_t)` | proved in part, partly not formalized | [P/K] Main:97 |
| Comb, gluing, uniform continuum: realizations with supplied data | proved on paper with probes | [P] Main:480, :564, :596 |
| No fixed finite carrier reproduces the full qubit | proved, half imported | [P] Main:558 |
| Configuration-interface ceiling: no phases, no dense control (`Fin 2`), not DerivedOI, rule-independent | proved | [K] `OB/FrozenSourcing.lean:295–327` |
| Monomial class has no composite control; supplied phases | proved | [K] `OB/StructuralClosure.lean:348`, :336 |
| Substratum plus elementary drives gives QM | proved, conditional on `DrivesElementary` | [K] `OB/StructuralClosure.lean:414` |
| D1–D3 (stationarity, equal-time blindness for every bijection, herald bound) | derived here; D2 extends Q-b1/P-1 | [W] (+[R]) |
| D4 (complete in-`V` records give a Markov kernel `T`; C4 invisible) | derived here, new candidate | [W] |
| D5 (Lemma A) | derived on paper three times | [R] + [W] |
| D6 (ceiling monotone, point 3) | derived here from kernel statements | [W] on [K] |
| D7 (post-hoc and timing selection fail N2) | derived here | [W] |
| R-lin N2 not supplied | proved on paper, conditional on the rule being R-lin | [R]/[W] |
| N1 under H-MEM or H-LOW; N3 fixed read; N4 under P1, E-iso, H-LOW | conditional on named premises | [R]/[W] |
| R-nl N2; heralded `q = 2` preparations (L5.4); 5d with M-INACC | open | [O] |
| MP-0, MP-1, MP-2 jointly sufficient for the qubit target | open | [O] |

***

## 7. §A.31 classification, assumption-watch markers, pressure tests

- **D4 — NEW (candidate, unreviewed).**
  - *Productivity test:* it is stronger than restating "C4 needs memory", because it fixes the
    observer's own process exactly as Markov with the uniform-prior kernel `T`. It also exposes a
    hidden assumption (H-MEM).
  - *Pressure test:* part of it is definitional (any process is Markov in its full-history state).
    The non-trivial part is that the kernel is `T`, fixed by `φ` alone, with the hidden sector
    acting as memoryless noise. That rests on D2 and holds only under counting measure.
  - It does not hold under a structured prior or a per-cycle uniform measure. On one cycle the
    law is stationary but need not be a product (Main:54), so D2 can fail there.
  - **Marker AW-OA1-1:** a statement that conditions on `X_{<t}` assumes an observer memory that
    `V_t` does not contain. Check H-MEM wherever C4 content is called observer-accessible.
- **D2 and the N1 strict verdict — CONFIRMING.** Q-b1 is already on `main`; the extension to every
  bijection is routine.
  - **Marker AW-OA1-2:** the "supply" role of the past hypothesis is not replaced by Main §4.6.
    This is not a manuscript defect: §4.6 claims only the selection role. It applies wherever a
    construction uses ready cells under the canonical measure.
- **D5 / N2 — CONFIRMING** MECH-1 and TUNE-1.
  - **Marker AW-OA1-3:** the first native gap under R-lin is classical. A claim that R-lin lacks
    quantum control should not be read as R-lin having classical control.
- **D6 / point 3 — ELABORATING.** It strengthens the trace's "interface blindness" to maximality
  plus monotonicity.
- **R5-5e Koopman–von Neumann control — ELABORATING [W].**
- **Pressure tests on favourable branches.**
  - N1 "supplied": downgraded to "under a premise" (N1.4).
  - Apparatus-1's exact Z/X Lüders match: it reproduces a quantum formula, which is not success.
    It is the Spekkens countercontrol CC4 with supplied access (`apparatus-1-20261107/DESIGN.md:56–60`).
  - 5c's encoded Hadamard: inside the finite Clifford group and noncontextual, so it does not
    escape the qubit-tier cap.
  - 5e's every-angle drive: imported, and a classical wave would pass it too.
- **Fixed point.** This is one pass. The run gives two CONFIRMING findings, two ELABORATING and one
  NEW candidate. The 3–4-pass no-NEW fixed point is not reached.

***

## 8. Check of the FH→SOURCE-1 trace (#1169 c.6829596317), claim by claim

| Trace claim | Verdict |
|---|---|
| Equivalence.lean line numbers (462–469, 157–185, 422–453, 294–359); per-`P` clock and record carrier; permutation unitary | Confirmed |
| Rung 1: Q_fb is retained, with no gate entailed | Confirmed; D4 adds the records-versus-readback tension |
| Rung 2: existence for supplied data; quantum matrices, seeds and records imported | Confirmed (Main:580, :582) |
| Rung 3: `obsTheory := permTheory` and rule-independence by `rfl` | Confirmed (`OB/SubstratumInterfaceAudit.lean:770`, :780). Qualified: the cause is maximality (D6); "first exact" ignores R3/N2 and the over-supplied write access |
| Rung 4: FrozenSourcing ceilings; `substratumGen_not_control`; `rot_not_monomial` | Confirmed (`OB/FrozenSourcing.lean:295`, :318; `OB/StructuralClosure.lean:348`; `OB/SubstratumInterface.lean:155`) |
| "The monomial class allows diagonal phases by stipulation" | Confirmed (`OB/StructuralClosure.lean:333`, `phaseOperator_supplied`) |
| Rung 5: `DrivesElementary` (77), `QuantumArchitecture` (86), `substratum_plus_control_qm` (~414) | Confirmed (`OB/SubstratumSource.lean:77`, :86; `OB/StructuralClosure.lean:414`). It is conditional sufficiency, and `DrivesElementary` includes continuous flows and phases, so it imports |
| §D3: "rule-sensitive source map (B)" as the ablation | **Refuted as a route at the configuration level** (D6). Still meaningful only for a non-configuration carrier |
| Verdict: the first proved loss is at the interface and its phase/control ceiling | Qualified: the first kernel-proved loss, yes. The first paper-proved loss for the posited rule comes earlier, at R3/N2, and is classical |

***

## 9. Reading inventory

**Read** (`main@fb733b4a` unless stated):
- `papers/Main.md`:
  - :1–110: abstract, §§1.1–1.5, §2.1–2.2;
  - :429–612: §3.4 through the unavoidable-memory theorem, including the gluing theorem, OI⁺,
    passive observation, and the uncertainty paragraph;
  - :644 and :740–760 (§4.6);
  - ledger items at :724 by extract;
  - the theorem and remark outline of the whole file.
- Lean, statements, with proof text where shown:
  - `Equivalence.lean:155–190`, :455–470;
  - `SubstratumInterfaceAudit.lean:1–40`, :740–830, and the declaration list;
  - `FrozenSourcing.lean:1–125`, :160–360;
  - `StructuralClosure.lean:330–430`;
  - `SubstratumSource.lean:60–100`;
  - `SubstratumInterface.lean:150–160`;
  - `LiftSource.lean:1–60`, :158–164;
  - `InternalObserver.lean` (the three theorems);
  - `OperationalAssembly.lean:594–640`;
  - declaration lines of `ExecSource`, `CentralObservation`, `GeneralCarrier` and
    `QuasilocalCharacterization`.
- Research records:
  - `apparatus-1-20261107/DESIGN.md:1–120`, :275–430;
  - `mechanism-1-20261107/DESIGN.md:1–137`, :797–900, :938–1060;
  - `mechanism-2-20261108/DESIGN.md:1–140`;
  - `controller-preparation-1-20261108/SELECTION.md` (in full);
  - `physical-controller-20261107/LEAD.md:1–50`;
  - `minacc-1-20261108/RESULT.md:1–70`;
  - `observer-interface-obsmu-20261104/ANALYSIS.md:1–40`, :228–240, :520–575, :885–960;
  - `states-dynamics-audit-20261024/history-architecture-v5/REPORT.md:1–60`;
  - `operational-quotient-v3/REPORT.md` and `oi-qm-ext-1/whole-model-bridge.md` (by grep);
  - `oi-qm-ext-1/two-mode-drive.md:1–40`;
  - `oi-pseudoentropy-20261025/review/REVIEW.md:455–475`.
- TUNE-1, on the branch:
  - `STEP1.md:1–80`, :148–315;
  - `STEP2-PROPOSAL.md:1–230`;
  - `STEP2-SESSION3.md:1–100`, :314–400;
  - `STEP2-SESSION4.md:1–82`, :553–630.
- GitHub: the #1169 body and comments 6791574087 through 6829742537 (the last seven); the
  coordinator's message.

**Not read:**
- #1169 comments before 6791574087;
- #866, #914, #1143, #1236 and PR #1237 threads;
- the other TUNE-1 files (Step 2 amendments and addenda, sessions 1, 2 and the C-POS-2 rerun);
- `papers/SM.md`, `Substratum.md`, `GR.md` and `Structure.md` (cited only through records);
- Main §2.3–§3.3 bodies;
- Q-A `DESIGN.md` and `PROOF-RECOVERY.md`, the feedback `RESULT.md`, record-control, `mathcon1`;
- `state-mixing-coupling`, `polarization-closure` and `dense-instrument-bridge` audits (extracted,
  not read);
- the KS model's later sections;
- the Lean proof bodies beyond those listed.

Negative claims here are therefore limited to the sources read, as §A.19 requires.

***

## 10. Limits

- Every [W] item is unreviewed and not kernel-checked. D4 in particular needs independent review
  before any use.
- Verdicts at R3 are for R-lin. For general bijections, N2 is possible in principle (classical
  switches); R-nl is open.
- D2 and D4 assume the global counting measure. Under per-cycle or structured measures they can
  fail. That failure is exactly what H-LOW supplies.
- The single-qubit tier tests sourcing, not quantumness (§4.1). Composite, Bell and Born-exponent
  questions are untouched.
- No candidate was constructed. 5d with M-INACC is named, not shown possible.
- Nothing here changes a manuscript claim. AW-OA1-2 is a reading note, not a finding against
  Main §4.6.
