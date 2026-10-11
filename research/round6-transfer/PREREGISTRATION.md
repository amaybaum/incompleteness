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
