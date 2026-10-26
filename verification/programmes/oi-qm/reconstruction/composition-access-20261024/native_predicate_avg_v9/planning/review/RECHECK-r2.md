# Re-check of draft r2 (NP-AVG-1, Issue #929)

Objects:
- `draft/PLAN-r2.md` (670 lines) and `draft/CHANGES-r2.md`, against `review/REVIEW.md` (SHA-256
  `4d77c7c2…`, matching r2's pin);
- the pinned inputs. All 22 SHA-256 pins in PLAN-r2:519-582 were recomputed and match.

Read-only. Nothing was computed on the question. The only new execution is
`review/toy/cones.py`, which checks the reference-pair cone radii on random 3D instances of v8's
rule: forward depth k reaches the later slice of the pair at distance k, and the earlier slice at
distance k−1. The argument in §1 depends on this off-by-one. The analysis in §1 is the reviewer's
written argument. It needs to be written up and checked by the drafter, as the plan's lemmas are.

## Verdict: BLOCK for freeze

The owner's gating requirement is not met: the question as preregistered is predominantly
redundant (§1). The mechanical revision is good:
- R1–R13 are applied, with five residual defects (§2–§3);
- two of the drafter's three non-adoptions improve on the review (§4).

A short path to an acceptable plan is given in §5.

## 1. Nonredundancy finding

### 1.1 Masking makes convention A trivially negative, not positive

A positive needs the record to carry flag information about Φ. Masking removes information, so
L2 and L3 cannot make A "trivially positive". Under A they make almost every record
*uninformative*, and an uninformative record fails the law: given (p, V), J is uniform, because
three of the seven Φ triples are fresh. K2 passes only because its flag A is supplied in clear by
a gate the class forbids. So the A-part is not vacuous as a screen, but its outcome is largely
forced, as follows.

### 1.2 The collapse argument under A

In reference coordinates (the pair n+1, n+2) every quantity has one of two types:
- **F** (slice t ≥ n+2): its cone is slice n+2 within t−(n+2) and slice n+1 within t−(n+3); its L3
  tips are in slice n+2 at distance t−(n+2);
- **B** (slice s ≤ n+1): its cone is slice n+1 within (n+1)−s and slice n+2 within n−s; its tips
  are in slice n+1 at distance (n+1)−s.

Φ consists of six B-type triples (s = n+1) and one F-type triple (V, t = n+2); none is ever
eliminated.

Fix an axis direction e. Define the reach of an F quantity as y_e + t − (n+2), and of a B
quantity as y_e + (n+1) − s. Let M_F and M_B be the maxima over the retained quantities. Then:
- an F-extreme's tip lies in some B cone only if M_B − 1 ≥ M_F;
- a B-extreme's tip lies in some F cone only if M_F − 1 ≥ M_B.

Both cannot hold. So in every direction the extremes of at least one type have tips outside every
cone of the other type. A same-type cone covers such a tip only if the two quantities share that
tip triple, which means they are light-like aligned on that axis line. The only other cover is a
Φ triple. This is the transport audit's cyclic structure (`main:…/transport_audit_v1/REPORT.md:188-203`).

Hence the L3 closure of a record keeps nothing beyond Φ, p and the Φ triples the record reads in
clear, unless, in all six directions, the extreme quantities are tied. With at most two items,
the port and the Φ sites, ties need distinct sites on common axis lines at matching slice
offsets. Such configurations are possible but special.

**Collapsed records fail Law_A.** For every record whose closure collapses, the retained public
part is (p, V, and at most two of the six slice-(n+1) Φ triples read in clear). There are three
cases:
- q8 is read: Y is known, but t1 and t0 both put mass on both values of y, so the law fails;
- q10 is read: R and Z are known, and the law fails in the same way;
- at most two of {m, o1, o2, o3} are read: at least two remain fresh, so (q8, q10) is uniform given
  the record, J is uniform, and neither target holds.

So **Law_A fails for every collapsed record, by L1–L3 and this argument alone**.

### 1.3 The collapse argument under G

In initial coordinates every quantity is F-type. A tip that is a seed is free unless it is tied.
So a collapsed record's closure keeps only quantities whose tips all lie in the frame. On a check
of the octahedral geometry, their cones then lie in the frame; this step is a sketch. Each
quantity is then a function of (frame, G).

Law_G(Π_R) on a frame is therefore Law_P of the truncated record on that frame. v8 found no R
whatever in C(4, 16) to be admissible, family by family, on exactly these sixteen frames and the
zero background (`native_predicate_v8/REPORT.md:19-21, 37`). So **every G failure of a collapsed
record restates v8**.

### 1.4 The only possibly nonredundant content

The only possibly nonredundant content is the **tie residue**: records whose L3 closure retains
quantities beyond Φ, p and Φ-in-clear, in A, or seed-tied quantities, in G. Whether the residue is
empty, and whether it connects to Φ, is an exact integer-geometry question over the 5,163,225
records. It involves no laws, and it was not computed here.

### 1.5 Which outcome classes are informative

| class | status as preregistered |
| --- | --- |
| NEG_BOTH | **Forced** for every collapsed record. Informative only through the tie residue. If the residue is empty, the sweep's verdict is a consequence of L1–L3, §1.2 and v8: a consistency re-derivation, not new information. |
| PADS_NOT_FRESH | Reachable only within the residue, since Law_A must hold. Any `F1b[frame]` failure on a retained part inside the frame is v8's pointwise negative, restated. Only the existence of a Law_A record would be new. |
| POS_A, POS_A_SAMPLED_FRAMES (+ `_PENDING_REVIEW`) | Reachable only through tie configurations whose G residual keeps seeds. Genuinely informative if reached; a priori very unlikely. |
| NOT_DECIDED | Likely to be an *artifact* wherever F2 with 𝓛_R item (iii) must be computed (§3.3). Uninformative. |
| VOID | Control-only. |

### 1.6 What known results settle

- **One-time pad.** L3 is the one-time-pad-by-bijection argument: a bijection of a fresh uniform
  variable is uniform and independent. Together with L2 it gives total masking; secret-sharing
  reasoning adds nothing beyond §1.2.
- **v8** settles every G-side failure of collapsed records.
- **The composition contract** (`REPORT.md:57-69, 151-157`) settles none of it. It states the
  admissibility condition, not the native outcome.

**The question as preregistered could tell us something not already known only through the tie
residue.** The 5.16 M-record law sweep, with F checks in both conventions, IM1 and IM2 in CI and
the mutant campaign, is unjustified for everything outside it.

### 1.7 The nonredundant version of the target

Two candidates:
- **(a) The collapse theorem.** For C_avg(4, 16, 2) under π_bg, every record is masked, reads Φ in
  clear, or belongs to an explicitly enumerated tie set. It would come with the two corollaries
  above, and would close v8's open averaging branch (v8 `REPORT.md:58-65`) by proof rather than
  enumeration. This is a modest consistency-axis result, but it is new.
- **(b) The tie residue**, if it is nonempty and connected to Φ: the only place where averaging
  could matter at k ≤ 2.

A larger, plausibly nonredundant question sits behind (b). In the union context of §3.3, a block
of consecutive slices over a neighbourhood is self-supporting under L3: the dynamics itself
constrains it, through x_{t+2} ⊕ x_t = H(Σ x_{t+1}). So averaging can matter only for records
large or aligned enough to defeat masking. The informative quantity is the smallest native record
whose closure retains carrier information. k = 2 may be below it.

## 2. R1–R13 as applied

| item | status | note |
| --- | --- | --- |
| R1 | applied | F1a, F1b and F2 are required in A and in G on every frame (PLAN-r2:118-131), with reason codes (260-266). |
| R2 | applied | `POS_A_SAMPLED_FRAMES` with the frame text (238-240). PADS_NOT_FRESH names the seed declaration (241-247). The seed declaration has its own paragraph (102-112). |
| R3 | applied | Codes and counts; NEG_BOTH reports counts by mechanism (248-251). |
| R4 | applied | Stream items, at distinct sites, with 3,225 and 5,160,000 records; F2 forward only (33-43, 73-78, 196-197). |
| R5 | applied | K6's w2 fixed; K3 and K3c append in the clear; the herald is in Π_R; K3d added (306-338). All four can fail. |
| R6 | applied, with gaps | GB, Z0, L2c, K4 (c alone, an exact product) and protocol 3 restated (340-366, 434-441). Z0's third bullet ("differs … *wherever* the A engine uses L2") must name the instance or instances on which the difference is required; otherwise it can pass vacuously. L2c's "a 2D instance" needs its size. |
| R7 | applied, with a gap | IM1 (371-375) runs "through T_h". v8's evaluator stops at slice n+17, on ball(ρ+n+17−t). Reaching slice 46 needs an evolution on a ball of radius about 50, with v8's families zero beyond radius 27. Specify it. IM2 (376-381) is fine. |
| R8 | applied | L1c measures dependence by perturbation, with a non-vacuity condition (352-360). |
| R9 | applied | Shard schema, coverage and disjointness, NOT_DECIDED on a missing shard (209-224). |
| R10 | applied, one defect | IC2 (272-273) is my own C2 suggestion, mis-stated by me. Agreement of the per-frame maps is implied only *given Law_A(Π_R)*: a mixture of a t1/20 and a t0/44 posterior is neither target. Without Law_A, disagreeing maps are a legitimate F1b failure. Because Law_G is reported for every decided R (456-457), IC2 as written can VOID a correct run. Add the premise "and Law_A(Π_R)". IC1 and IC3–IC6 are valid and can fail. Protocol 1's not-applicable branch is right (428-429). |
| R11 | applied, one gap | I1–I4 on a fixed set M (405-418). I1's expected outcome needs the injected item's *other* stream samples to be uninformative. v8's m9 chose "a native cell whose earlier samples are constant" (v8 PLAN:150-153). State that condition for I1 and I2: earlier samples constant given the frame, and a continuation that is L3-masked. Otherwise I1 can fail for reasons unrelated to its target. |
| R12 | applied | Table (463-492), scope (494-514), full SHA-256 pins (all verified), base containing `fc452ea8` (8-9, 612-614). |
| R13 | applied | Native-only sweep; constants transcribed (198-199, 302-303). |

## 3. New engines, controls and the O4 method

### 3.1 Can the new checks fail?

| check | result |
| --- | --- |
| GB | yes |
| Z0 | yes, after the R6 fix |
| IM1 | yes |
| IM2 | yes. Its bijection check uses four fixed values per elimination, which is evidence beside the written proof and is labelled as such. |
| FR | yes, but only through the frame computation: by the light-cone definition, a correct frame cannot fail it. It is an implementation check, which is all the table claims (478). |
| W1 | yes |
| ST | yes |

### 3.2 State the cone radii

State the asymmetric cone radii of §1.2 in L3's setting (PLAN-r2:156-173):
- forward from the pair: t−(n+2) and t−(n+3);
- backward: (n+1)−s and n−s.

Symmetric radii would be sound but would over-retain, turning eliminable records into not-decided
ones.

### 3.3 The O4 union-elimination argument (PLAN-r2:184-190) is sound but ineffective

**Soundness.** The L3 closure of a context is its largest self-supporting subset, and a union of
self-supporting sets is self-supporting. So C′ ⊆ C implies ret(C′) ⊆ ret(C) ∩ C′; elimination is
monotone. Eliminated quantities are mutually independent and independent of the retained ones:
by induction, each was a bijection of a tip that no later-remaining quantity reads. Restricting a
member to Ω_R is therefore exact.

**Effectiveness.** Item (iii) makes the union *all* in-region samples after t_R through T_h. Such a
block contains genuine dynamical constraints (x_{t+2} ⊕ x_t = H(Σ x_{t+1})), so it cannot be fully
eliminated, and Ω_R will be large. A two-segment member restricted to Ω_R then exceeds S_max,
even where its own context (Π_R ∪ Φ ∪ S, at most four sites) would collapse by §1.2. The result:
F2 with (iii) is effectively always not decided, which is a sound method producing an
uninformative NOT_DECIDED.

Use the union only as a pre-filter. Decide members by their own closures, classified
geometrically by configuration type rather than enumerated: there are about 10⁹ members per R.
Otherwise take O4's alternative and state that F2 is near-vacuous.

## 4. The drafter's non-adoptions

- **O3: accept r2's version.** My mechanical L3 certificate covered only the averaged variables.
  The retained part also needs an all-frame argument, and r2's (a)+(b) is correct (PLAN-r2:643-651).
  By §1.3, for collapsed records (b) is exactly v8's per-frame negative, so (b) is needed only for
  residue records.
- **C5: accept report-only.** Under the declared seeds, P(U | H, frame, Φ) = ν holds by
  construction. FR measures the construction, and F1a-G and F2-G carry the joint content.
- **A2: the correction is right.** q8 at (0, 0, −1) has six neighbours at n+2: q9 (V) and five
  outside Φ. My "four" was wrong; the conclusion is unchanged.

## 5. Required before any freeze (owner's gate first)

1. **Nonredundancy, the owner's gate.** Rewrite the plan in two stages.
   - **Stage 0, preregistered and local:**
     - write out the collapse argument (§1.2–1.3) with the cone radii;
     - write out the Φ-in-clear lemma and the G-truncation-to-v8 lemma, including a proof of the
       in-frame cone step;
     - run an exact integer-geometry enumeration of the L3 closure of all 5,163,225 records under
       A and under G. It computes no laws, and its decision rule is fixed in advance.
     - If the closure collapses for every record, the result is NEG for C_avg(4, 16, 2) by proof,
       and no law sweep runs.
   - **Stage 1** runs the existing law machinery, controls and protocol on the residue records
     only. The scope text records that everything else was settled at Stage 0.
2. Add the Law_A premise to IC2 (§2, R10).
3. State I1's and I2's injection-site condition (§2, R11).
4. Name Z0's required-difference instance; give L2c's 2D size and IM1's evolution ball (§2, R6 and
   R7).
5. Replace the F2 union-only method (§3.3), or adopt O4's alternative.
6. State the cone radii in L3 (§3.2).

## 6. Owner decisions

- **Gate.** Recommend keeping NP-AVG-1 in planning and approving only a Stage-0 plan. The
  nonredundant target is the collapse theorem plus the tie residue. If the residue is empty, the
  thread closes with a written negative, and the frontier moves, as #929 itself says for NEG_BOTH,
  to gates and compilation. It could also be re-scoped to the minimal self-supporting record size
  (§1.7).
- **O4** (later reads). If Stage 1 runs, take (iii) only with per-member closures.
- **O1–O3, O5–O9:** no change from REVIEW.md. r2's O3 is better than the review's.
