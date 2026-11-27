# FSLICE-PS-1: preservation record (draft for a consolidated owner decision)

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it.

- **Evidence layer of every result:** mathematical derivation on paper, with source reading at the
  pin [P] `13c05b4fe666c2e128eed1213874be9b8208982d`. The report labels its steps [A] (exact hand
  algebra) and [W] (reasoning).
- **Input records.** The F-slice record [FS], lane 2 [L2], unit A [A-rec], unit C [C3] and
  SMD-SRC-1 are model-reviewed paper derivations. They are used as named conditional inputs
  (§A.46 item 7).
- **Computation.** None was run, and no Lean was built.

## 1. The record preserved

- **Current report:** `REPORT-r2.md`, revision r2 with the in-place r3 edits. Commits:
  - `f4bd7b2f4d16aa362737a72378fdb0e7b88e01c6` (r2);
  - `2706ae17f9d0881ac461a3c8331da67933505ce0` (r3: nits D1–D4, text only).
- **r1 record:** `REPORT.md` (r1, commit `b3500e3194e4db04372c6ed2bf9b4ab4962c3dc8`), kept
  unchanged.
- **Change map:** `CHANGES-r2.md` maps each r1-to-r2 change to its review finding, and its r3
  section maps D1–D4.
- **Plan:** `PLAN.md` (commit `158f4155c9b80f220bb6543b11e04497c3ec0328`), committed alone before
  r1. It is recorded, not frozen, and is not superseded. It states that the writer is the author of
  the F-slice record and had read the inputs before writing it. The report labels its per-carrier
  application of the rule as a refinement of PLAN §4.
- **Status in the header.** The header of `REPORT-r2.md` records the report's status before
  acceptance ("WIP / UNVERIFIED"). The reviews are recorded here.
- **Accountable Issue:** #1217 (programme #1169). Guiding pull request: #1624.
- **Owner decisions** (#1169 comments posted from the account `amaybaum`, quoting the owner):
  - **Comment 7199704501** (created 2026-11-26T17:49:03Z): activation of work package WP-2,
    "Proceed as suggested".
  - **Comment 7208939261** (created 2026-11-27T03:22:49Z; decision received 2026-11-27): "Proceed
    as suggested". This authorizes, under WP-2, the paper-only investigation "F-slice premise
    sourcing (#1217)": "Whether N-2 (label independence), N-8 (the centred field reading) and N-9
    (SMD on the full state) can be derived from native OI dynamics, or whether at least one remains
    an independent premise."
  - **Comment 7209325168** (created 2026-11-27T03:51:22Z), quoting the owner: "Prepare #1623
    together with UN-1 and F-slice for a consolidated preservation decision." and "Preserve the
    negative results and their exact limitations. No new premise is adopted, and no merge is
    authorized yet."
  - **Owner decision on preservation: pending.** It is to be a consolidated decision for #1622
    (UN-1), #1623 (SMD-CL-1) and #1624 (this record). No preservation, merge or premise adoption is
    authorized by this file.
- **Independent non-author reviews.** These are model reviews by reviewer agents, each recorded on
  PR #1624 as reviewer text posted verbatim. They are evidence of review, not independent
  mathematical verification.
  - **Comment 7209242260**, review of r1 at `b3500e31`: REVISE (minor to moderate), findings 1–11,
    no class changes. It found §2.2's conditioning, Lemma PF, witness ρ_P and route R9.3 correct by
    hand. It found R2.2 false as stated, the reflection route R9.6 missing, and the carrier ranges
    overstated.
  - **Comment 7209316524**, delta review of r2 at `f4bd7b2f`: ACCEPT WITH NITS. Findings 1–11
    resolved; nits D1–D4. It checked the new and widened items by hand.
  - **Comment 7209338201**, confirmation of r3 at `2706ae17` (nits D1–D4): ACCEPT.
  - **Reviewer identity:** the records do not state whether the reviews were written by one
    reviewer agent or by several.

## 2. Substantive result and its precise scope

**Scope.**
- Carrier T = (Z/L)^3 at the massless point (αμ = 1/d, M = μI_6), b_A1 = 0, on the linear lift,
  for SM Theorem 5's consumers only.
- Every result is conditional on the carried conditions C*: LIN (posited); LIFT and the SM:232
  bridge (open); lane 2's Theorem 1 (proved on paper, conditional on LIN and LIFT); and H-link,
  H-cust, H5, H-PF, L-SDS, TPC, and SMD on the fluctuation law (open).
- The stabilizer statements are under N-1's extension reading, a candidate reading under the
  owner's ruling (#1169 comment 7202075726, item 4, quoted on `main` in the F-slice
  PRESERVATION.md §1).
- Not addressed: carrier Z, the nonlinear lift, consumers outside Theorem 5, and the Z/q level.
- Each independence claim is relative to the stated premises of Main and SM, C*, N-1, and the
  premises listed in the report's §4.2 table. It is not a claim that no extension of OI could
  supply the premise.

**The nonredundant result (report §0, §2–§4).**
- **No class D.** None of N-2, N-8 or N-9 is derived from native OI dynamics: Main's and SM's
  substratum and observer interface together with C*.
- **N-2 (label-independent J): class R only under owner reading O-1a.**
  - Under O-1a, N-2 follows from H-PF with its positive-frequency clause referred to the update F
    on V_rest. H-PF names J_F = D(−D²)^(−1/2), which is one operator independent of the label.
    Any J that is a function of the slice-preserving group is not tamed (§2.2).
  - Without the clause, N-2 is class I. That is a weakening of H-PF, not a reading of it, and it
    is witnessed by [FS] Proposition P's family. If O-equivariance of J is required, this class I
    rests on a [W] transport step and holds only for L ≥ 7.
- **N-8 (centred field reading): class R only under owner reading O-1b.**
  - Lemma PF [A], both directions: given φ = Φ_n on V_rest and real-linearity, N-8 is equivalent
    to H-PF's positive-frequency clause extended to the trajectories of the stationary support.
    That extension is not in H-PF as stated.
  - Under the formula-only reading N-8 is class I (witness ρ_W of [FS]).
- **N-9 (SMD on the full law): independent, per carrier.** The rule is applied per carrier, as a
  labelled refinement of PLAN §4:

  | Carrier | Without the label-sector reading | Under the label-sector reading |
  | --- | --- | --- |
  | even L ≥ 2 | I (ρ_P; also ρ_T for L ≥ 8), unless R_π-invariance is required (for L ≤ 6) | I (ρ_P), unless the state is required to be R_π-invariant, in which case R |
  | odd L ≥ 7 | I (ρ_T) | R (reduces to SMD on the sector's fluctuation law) |
  | odd L ∈ {3, 5} | O (no witness found) | R |

  - **The R_π caveat.** R_π = 1 − 2P_π commutes with F. Invariance of the state under it is not
    stated. If it were required, N-9 would reduce to SMD on the fluctuation law on even L under the
    label-sector reading (route R9.6). R_0-invariance does not rescue N-9 (witness ρ_T′, L ≥ 7).
  - **The witnesses.**
    - ρ_P (new, [A]) is a single label sector on every even L ≥ 2. Its stabilizer test uses
      w_φ ∈ SU(6), φ = 2π/3.
    - ρ_T comes from the F-slice record, here extended to odd L ≥ 7.
  - **The closed and conditional routes.**
    - Measure selection is vacuous for Theorem 5 ([A-rec] Proposition C).
    - Extremality excludes the conclusion ([A-rec] Proposition B).
    - Joint Gaussianity would give N-9, but it is open and stronger than SMD.
    - Label–fluctuation independence is sufficient, and open.
- **NAT-C (recorded, not adopted).** Naturality of the complex structure under the whole linear
  commutant of F (through R_π) would force N-2. No stated premise requires it, so under stopping
  condition 3 it is recorded as a new premise and not adopted (§A.29, §A.50 item 6).

**The owner questions this record leaves open.**
- **O-1a.** Does H-PF's positive-frequency clause refer to the update F on V_rest? (This decides
  N-2: R or I.)
- **O-1b.** Is that clause extended to the stationary support in the trajectory form? (This decides
  N-8: R or I.)
- **O-2.** Is Theorem 5's state a label sector fixed by the observer's records? (This decides the
  N-9 column; the R_π caveat applies.)

**What it would change.** If O-1a and O-1b were both accepted, the candidate-premise set of the
F-slice outcome R2 would shrink from {N-2, N-8, N-9} to {N-9}, with N-1 and H-PF remaining. This
record adopts nothing and changes no status.

**Productivity (report §6): gem.**
- NEW: Lemma PF with the N-8 equivalence; ρ_P for every even L ≥ 2.
- POSITIVE: H-PF implies N-2 under O-1a; joint Gaussianity implies N-9; the reduction for a = 0
  sectors.
- ELABORATING: R2.2 with NAT-C; R9.3; R9.6 with ρ_T′; ρ_T on odd L ≥ 7.
- CONFIRMING: ρ_T.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Every result is a paper derivation, checked only by the model reviews of §1. "Partially verified"
means checked by a model review. "Exploratory" means not yet reviewed beyond the delta review's
scope. The remediation plan below authorizes no work (§A.45 rule 3).

| Claim class | Where (REPORT-r2.md) | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| H-PF implies N-2 (§2.2 steps 1–3, step 3 over all of 𝒢_+) | §2.2 | partially verified (r1 review checked step 3 for F²; delta review accepted r2) | independent non-model review | #1217 | a recorded independent review |
| Identification of H6-M's structure with H-PF's J (§2.2 step 4) | §2.2 | partially verified (delta review) | independent review | #1217 | a recorded independent review |
| R2.2(a), the stated symmetries do not force LI; the O-equivariant transport | §2.1 | exploratory; the transport is [W], under the χ-orbit condition | a written transport argument; review | #1217 | a written derivation and a recorded review |
| R2.2(b) and NAT-C | §2.1 | partially verified (delta review checked R_π) | independent review | #1217 | a recorded independent review; any adoption of NAT-C is an owner decision (§A.50 item 6) |
| Lemma PF, both directions, and §3.3 | §3.2–§3.3 | partially verified (r1 review checked (⇒); delta review checked r2) | independent non-model review | #1217 | a recorded independent review |
| R8.2, the amplitude-scale gauge | §3.1 | exploratory; conditional on an open warrant | review | #1217 | a recorded review |
| R9.1, relying on [A-rec] Proposition C | §4.1 | partially verified (Proposition C model-reviewed in unit A) | independent non-model review | #1217 | a recorded independent review |
| R9.2, R9.3, R9.4 | §4.1 | partially verified (r1 review) | independent non-model review | #1217 | a recorded independent review |
| R9.6 and ρ_T′ | §4.1 | partially verified (delta review; ρ_T′ specified in r3, pending the r3 confirmation) | the r3 confirmation; independent review | #1217 | a recorded review |
| ρ_T, even L ≥ 8 | §4.2 | partially verified ([FS] §3.4) | independent non-model review | #1217 | a recorded independent review |
| ρ_T extended to odd L ≥ 7 | §4.2 | partially verified (r1 review) | independent non-model review | #1217 | a recorded independent review |
| ρ_P, every even L ≥ 2 | §4.2 | partially verified (r1 review checked large L; the delta review checked the extension) | independent review; an exact finite control on L = 2 or 4 | #1217 | a recorded review; an exact control run under authorization |
| Odd L ∈ {3, 5} without the label-sector reading | §4.3 | open: class O, no witness found | a witness or a derivation | #1217 | a construction or a proof |
| Owner readings O-1a, O-1b, O-2 | §8 | open | owner decisions | #1217 | recorded owner decisions |
| Preregistration order (PLAN before r1) | §1 here | established from commit order: `158f4155` (03:30:31Z) precedes `b3500e31` | none beyond the commit order | #1217 | none; it stands as stated |

## 4. Off-`main` references (§A.42 item 8)

Every reference the record makes to content not on `main` has been traced to the claim it is
attached to:

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7199704501, 7208939261, 7209325168 (owner decisions) | report header; §1 here | provenance: authority records quoted with author and time; no result uses them |
| #1169 comment 7202075726, item 4 (owner ruling on N-1, N-2, N-8, N-9) | report §1; §2 here | support on `main`: quoted with author and time in `verification/programmes/substratum/f-slice-hzm-20261126/PRESERVATION.md` §1 |
| PR #1624 comments 7209242260, 7209316524 and the r3 confirmation | report header; §1 here | provenance: evidence of review; no result uses them |
| Issues #1217, #1169, #1049, #1216, #1622, #1623 | PLAN; §1 here | provenance: accountability, scope boundary, consolidated decision |
| commits `158f4155` (PLAN), `b3500e31` (r1), `f4bd7b2f` (r2), `2706ae17` (r3) and the commit adding this file | report header; §1, §3 here | support on `main` once the merge of §5 lands: the record's own content and preregistration order; not before |
| [FS], [L2], [A-rec], [C3], SMD-SRC-1 records and their PRESERVATION.md files | report §2–§4 | support on `main` at [P] |

Support off `main`: none, once the record lands as §5 requires.

## 5. Landing condition

The record is preserved only through a merge commit that keeps `158f4155`, `b3500e31`, `f4bd7b2f`,
`2706ae17` and the commit adding this file reachable from `main`. The order of the plan's commit
before the report commits is part of the record's provenance. Merging needs the owner's separate
approval (§A.50 item 1), which this file does not record.

## 6. Preservation rationale

The record answers the authorized question for each of N-2, N-8 and N-9 separately, with checked
witnesses and stated limits. It contains negative results that narrow the search:
- none of the three candidate premises is derived from native dynamics;
- N-9 remains independent on every even L and on odd L ≥ 7, by witnesses that meet every stated and
  carried premise;
- the natural routes to N-9 (measure selection, extremality, conditioning on records) are closed or
  only conditional, with the conditions stated.

It also isolates exactly what would reduce the candidate-premise set:
- two owner readings of the already-carried premise H-PF (O-1a, O-1b);
- one unstated invariance (R_π);
- one unstated naturality principle (NAT-C).

Each of these is recorded and none is adopted. The owner asked that these negative results be
preserved with their exact limitations (#1169 comment 7209325168). The result is nonredundant with
the F-slice record: that record named N-2, N-8 and N-9 as candidate premises, and this record
classifies each. The new results are Lemma PF and ρ_P.
