# Round 6 — transfer sourcing and the O14 channel bridge

Research work authorized by the owner in this session (“Ok let's proceed as suggested”).
Started 2026-10-11 13:01:52 UTC. This is an isolated cross-thread research record for B22, E23 and B23;
it does not open S6 or designate a native V3 freeze or execution head.

## Baseline and scope

Certified base L: `9f9f8257a980a1819fbbc1dc0019917cf8678626`.
Overview: `1325160c35ddb5b7a9f6f608cced0225a40401f1`.
Bridge: `5ba9218eb17608015118131be4a3ddc14d8095cf`.
Equivalence: `3a46b81103717c55510ea5b57ea7d520858cb478`.
Origin: `44c06d461ea7b6519c61efdd23534d48bf2f345b`.
Countermodels: `c9ac75bd51f2c7be201f21083be866e92269dfa3`.
Inventory: `research/archive` at `4dc0321ca2aac6f6aca6f55efc90b7f51330334a`.

Order: B22 (unitary and channel transfer sourcing), E23 (H2, H3, A_miss),
then B23 (assemble O14 against the pair-cone theorem). Read-only source reconnaissance
precedes this S0; no new decisive computation or Lean development run has occurred.

## Questions and prospective decision rules

1. **B22-SOURCE.** Does an existing inventory item, at its recorded status, connect the
   implementation-generated matrix state space to an arbitrary P-level pair cone K through
   the dictionary, and yield unitary or channel transfer?
   Record DERIVED only with a complete chain and every side hypothesis sourced.
   A proof conditional on an identification or added compatibility clause is CONDITIONAL.
   Absence of a theorem or import path records OPEN; it never establishes full-framework
   independence. Identifying K with Q3 is a target-level argument, not a source of reconstruction.
2. **E23-SOURCE.** For H2, H3 and A_miss, name inventory ids, exact declarations and remaining
   identification or operation-datum hypotheses. Statuses are kept distinct: definitions,
   assumed hypotheses, open obligations and proved instances. An assumed inventory item is
   not upgraded to an observer-native consequence. H3 means K = dualW K, not closedness.
3. **B23-ASSEMBLY.** State channel transfer using actual InstAvail one-outcome protocols and
   the kernel's spectator extension. Combine O14's finite-round protocol with a closed K
   to prove drive invariance, combine the J datum to obtain the generator clause, and name
   the remaining density and pair-cone assumptions. Exact availability of the limit is
   never inferred. The protocol assembly remains [W]+[X] until its InstAvail witness is built.
4. **S6-SURFACE.** Give a concrete dependency choice for cnotMat/dict_cnot and retain the
   conditional theorem and its non-inference rule. No governed round starts in this work.

## Check plan, fixed before run 1

The exact checker independently rebuilds the O14 circuit, its readout/reset and correction,
the two-qubit Pauli dictionary and the spectator channel. It checks every matrix unit for
one round and several finite retry depths; checks trace preservation, the dictionary action,
the exact residual coefficient (3/8)^k and J; and includes expected-false controls for omitted
correction and an incorrect success gate. It also checks a closed cone invariant under the
24 one-token Clifford unitaries but moved by the first retry channel, and an explicit
nonclosed cone where finite-channel invariance fails to pass to the drive limit.
These are scope controls for the transfer and closedness lemmas, not full OI countermodels.
A proper closed unitary-invariant cone larger than Q3 checks that closedness cannot replace H3.

Verdict R6-CHANNEL-CHECK-PASS is printed iff all named exact checks pass and all
expected-false controls are false. Finite computation never substitutes for the
written induction, topological limit proof or InstAvail witness. First failures,
outputs, errors and subsequent repairs are retained. A replay must be byte-identical.

## Evidence and governance

[K] means certified kernel at L; [D] requires a recorded successful design build;
[X] exact arithmetic; [W] written proof; [A] previously audited records; [U] unsourced.
New Lean source without a build is explicitly UNBUILT. Four transfer claims are recorded
separately: existing-framework derivation, conditional derivation, necessity for this
construction, necessity for every reconstruction. LOG.md is append-only.

The working branch is research/round6-transfer-sourcing, based on the overview checkpoint.
Existing thread branches, main, manuscripts and governed records remain under their
existing authority. Remaining round-six nodes are not completed by this focused record.

## S0-b — pre-run-1 revision after the coordinator's review

Written 2026-10-11 15:30:41 UTC, before any run, any dispatch and any node work. No computation of this record has
been run. The text above is unchanged; the clauses named below supersede it. Scope was narrowed by the owner
(through the coordinator, during this revision): STEP 0, B22 (priority) and a short E23 table are done in this batch;
B23 is the Lean fixes and at most one design build of the existing module; the items marked DEFERRED go to round 7,
recorded as deferred, not done.

1. **B22 decides both forms separately** (supersedes question 1). (T)_𝓘: every admissible one-token unitary of
   `𝓘` maps `K` into itself through `transferMap U` (`TransferClause`). (T^ch)_𝓘: every one-token channel
   instrument-realized by `𝓘` (`InstAvail 𝓘 (Fin 2) Unit`) maps `K` into itself through
   `coordOf ∘ (1 ⊗ Φ) ∘ dict` (`ChannelTransferClause`), stated with `K` closed. For each form the owner's four
   claims are recorded apart: (i) derivable from the existing OI assumptions at their recorded status; (ii)
   derivable with an additional assumption, named; (iii) necessary for this particular construction; (iv) necessary
   for any derivation of quantum equivalence. (iv) is never concluded from (iii). The mandatory countercontrol (the
   full class with `K(Z_F)`) filters every DERIVED chain in both forms. Absence of a derivation records OPEN.
2. **B23's placement question** (supersedes question 3's scope): whether the bridge's cones are required to be
   invariant under every available channel of the class (the scope of HO-45's (B) placement), with outcome
   "design statement" or "obstruction". DEFERRED to round 7 beyond what B22's channel-form verdict states.
3. **E23 states the reading** (invariance or availability) of every source it names for H2, H3 and A_miss
   (supplements question 2). This batch: a source table only; no new computation.
4. **The exact-check plan** (supersedes "Check plan, fixed before run 1"): DEFERRED to round 7 with B23's controls.
   No exact checker runs in this batch, so no `R6-CHANNEL-CHECK-PASS` verdict can print. When it is taken up, the plan
   is enumerated before its run 1 — every check by name with its expected truth value, fixed retry depths, every cone
   by an explicit construction — and a control that does not behave as expected voids the verdict, the run is kept,
   and a substitute needs a logged amendment before a new run. Design notes for round 7, not results (no run):
   (a) KC is likely unsuitable as the "moved by `Φ_1`" control — with `c − 1 = 10⁻⁵` and `Φ_1`'s identity weight
   `3/8`, a negative pairing needs an orbit ray `g` with `p₀p₁ < 5.33·10⁻⁵` (`pᵢ` its target weights), so KC is
   expected invariant under `Φ_1`; a cone such as `{ω : ω b ∈ L for the six octahedral vectors b = (1, ±eᵢ)}` (closed,
   H1, invariant under the 24 Clifford target actions; the table `tens(e₀, (1,1,1,1))` is mapped outside) is the
   candidate; (b) the open-disc-plus-one-point cone in `V = span{e₀₀, e₀₁, e₀₂}`, scoped to the sequence `Φ_k`;
   (c) the block-positive cone (also fails H2) and, isolating H3, `{A ⪰ 0, D ⪰ 0, ‖B‖₁ ≤ κ (tr A tr D)^{1/2}}`, `κ > 1`.
5. **`channelTransfer_of_identified_stateSpace`** (BridgeChannelTransfer.lean:61 at `5d4b9833`): its `hValid` ranges
   over channels available on the single token and asserts that their spectator extensions preserve the pair set;
   reading that as validity on the pair silently uses the kernel's spectator rule `instAvail_spectator`
   (ImplementationLocality.lean:789 at L; hypotheses `ContextStable`, I4.29, and `LabelInvariant`, I4.30). It is
   restated over pair-available channels with I4.29 and I4.30 as explicit hypotheses, and the token case derived
   through `instAvail_spectator` (a small edit, in the one Lean-fix commit). At the kernel's own pair state space (the
   positive semidefinite cone) the identification `hId` is `K = Q3` — the target, excluded as a source (line 29).
6. **Provenance.** The dev commit `5d4b9833` (base `16e75fbe`; files `OIBridge.lean`, `BridgeChannelTransfer.lean`,
   `EqvK2Block.lean`, `EqvOneDictionary.lean`, `EqvK2Generation.lean`) is UNBUILT and was made before B22/E23,
   contrary to this S0's stated order — a deviation, logged. Baselines added: `dev-bridge/r5-bridge2` @ `16e75fbe`
   (run 38124442150, green) and `dev-equivalence/r5-design` @ `f0c36cf9` (the three E19 modules, byte-identical
   blobs, built green in run 38134245361). `BridgeChannelTransfer.lean` receives the standard design-module header.
7. **Receipts.** One LOG line per inbox handoff (version; whether and how relied on); README states that this
   cross-thread record does not discharge the four threads' own round-6 receipts; HO-44 is reference-only.
8. **Lean fixes** on the dev branch, one commit before the first dispatch: line 1 `/-!` → `/-` (a module doc before
   `import` ends the import header); "Closedness is needed for the limit" → "used"; the unused
   `import OIBridge.EqvK2Generation` dropped; item 5's restatement. No new theorem. Predictions for the one dispatch
   (Build, every `#print axioms` line, `lean-axioms`) are written in NOTES-B23.md before the dispatch.

S6-SURFACE: DEFERRED to round 7.
