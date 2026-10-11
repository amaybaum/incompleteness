# HP-round6-transfer-1 — to bridge, origin, equivalence, countermodels: the transfer clause's source is OPEN in both forms, located at I3.165's clause; the countercontrol extends to the channel construction

**From** `research/round6-transfer` (round 6, nodes B22, E23; narrowed batch). Proposal for the coordinator to issue.
Reading: availability in, invariance out, throughout.

## Statements and labels

1. **Where OI's operational semantics lives** (B22-2). I4.66 `CompositeOperationalValidity` (assumed, do not assume;
   derived from implementation locality by I4.38 [K]) says available families map PSD matrices of every matrix carrier
   to PSD matrices. A P-level pair cone `K ⊆ W 3` is not the state space of any carrier in that vocabulary; I4.66
   reaches `K` only through an identification `hId : C = dict '' K`, which at the kernel's own pair state space (PSD) is
   `K = Q3`, the target. Label: OPEN for (i) in the channel form ([A] + [K]).
2. **The gap, located** (B22-1, B22-2). The inventory's only items whose content contains the transfer are I3.165's
   clause "local actions compatible with the composite cone" (open, ROADMAP.md:1001; do not assume) and the (b)-forms
   I3.150–I3.153 (PT-record open; do not assume). The landed M/O → P results (K2-GUARD-1, K1-BRIDGE-1,
   K1-SHARP-TESTS-1, EFF-1, I3.42) transfer the availability of tests and give only `K ⊆ maxCone`; none transfers an
   operation. (T)_𝓘 and (T^ch)_𝓘: (i) OPEN, not independence (the full-model question is B24's).
3. **Countercontrol, both forms** (B22-3). (full class, `K(Z_F)`) meets every hypothesis of `bridge_derived_half`
   except (T) and every hypothesis of `bridge_channel_half` except (T^ch) (closedness from self-duality; the witness by
   the constant sequence `conjChannel zPh`; `J` by `InstAvail.op`); both conclusions fail. So (T^ch) cannot be omitted
   from the channel construction, and every DERIVED chain in either form must use one of Table A2's 13 FAILS rows or a
   bridge absent at L. Label: CONJECTURE ([K] + [D] + [X] + [A]).
4. **The identified-state-space route** (B22-4): validity of pair-available channels on `C`, `hId`, I4.29 and I4.30 ⇒
   (T^ch)_𝓘 (`channelTransfer_of_identified_stateSpace`). CONDITIONAL. Assumption-watch marker (B22-AW): validity or
   transfer "on the pair" quantified over token-available channels carries I4.29 and I4.30.
5. **Sources of H2, H3, A_miss** (E23-1 … E23-3): none stronger than its recorded status; H2's operation is available in
   the stated access as a permutation [W], so its open content is a two-token transfer clause; H3's nearest source
   (CSD2) is a states/effects duality with UNRESOLVED observer-native source; A_miss's availability routes all pass
   through an introduced transfer clause. Label: OPEN.

## The owner's four claims, per form

| claim | (T)_𝓘 | (T^ch)_𝓘, `K` closed |
|---|---|---|
| (i) from the existing OI assumptions | OPEN | OPEN |
| (ii) with an additional assumption | CONDITIONAL on (T)_𝓘, or (b_S4) (`actT` form), or `K = Q3` (excluded) | CONDITIONAL on (T^ch)_𝓘, or validity on an introduced pair state space with `hId`, I4.29, I4.30 |
| (iii) necessary for this construction | yes (`bridge_derived_half`) | yes (`bridge_channel_half`) |
| (iv) necessary for any derivation of QE | not shown | not shown |

## Evidence

`research/round6-transfer`: NOTES-B22.md, NOTES-E23.md, RESULTS.md (rows B22-1 … B22-4, B22-AW, E23-1 … E23-3);
module `OIBridge/BridgeChannelTransfer.lean` at dev `fd364020`: run 38151796092 Build FAILED on
`channelTransfer_Q3` (missing `open scoped ComplexOrder`; RESULTS row B23-1), so its statements are [W], not [D].

## What the receiving threads may assume

Items 1–5 at their labels.

## What they may not assume

- that (T) or (T^ch) is independent of the inventory (OPEN, not independence);
- that (T) or (T^ch) is necessary for quantum mechanics (claim (iv) not shown);
- certification, or a census disposition; anything of the deferred items (HP-round6-transfer-2).
