# Response to the focused review of S3-PLAN-r2

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-S3-PLAN-r2.md` (ACCEPT WITH CHANGES at
`413af128`) and of three owner-confirmed additions. The changes are in `S3-PLAN-r3.md`.
`S3-PLAN-r2.md` is left unchanged (SHA-256
`5be454bf2555b8c3269716ebd78685be024e85334021ddc0b12a61610e09e474`).

The owner confirmed the additions (`amaybaum`, 2026-11-14): "Yes. Add both points to S3-PLAN-r2. They
are important scientific requirements, and neither introduces a new premise or authorizes new
execution."

Each finding was checked at source before it was applied. No finding was found to be wrong.

Unchanged:
- the F2 and F3 boundaries: no model construction, no MR-1 stage 2, no duplication of #866 or #913;
- S5 stays separate from setting availability;
- the plan is paper-only, with no new premise;
- C-1 stays under #1234, and X1–X5 stay open;
- requirements A, B1–B3 and C still apply.

## Required changes

| Finding | Check at source | Disposition | Where in r3 |
|---|---|---|---|
| **R1(a).** The marker's preparation is missing | **Confirmed.** S-L5: the marker "affects any later test of the carrier only through the offset `Φ_{DA} s_A`, which comes from its own initial content"; loss "can arise only by additive injection from regions whose content does not depend on the carrier" (`MR-star.md`:584–594). The μ leg: "every region's marginal is uniform, so there is no ready region" (`MR-star.md`:642) | **Applied.** Condition (δ) is added: a quiet marker (assumed, unsourced) or a native marker (uniform, noisy), plus the geometry `Φ_{DA}`. Sourced preparations are those produced from `μ` by native steps, which on the record is only the noisy native marker. The miss branch is split by (δ). With a native marker it is a raw-direct miss only if the noise-induced drop fails to track path distinguishability and to return under erasure (MR-1 §3.5; T4). With a quiet marker the conflict concerns an assumed apparatus and is reported as such | §8.4, check 1 |
| **R1(b).** (γ) is an open derivation | **Confirmed.** Main:682 and Substratum:463: "a derivation of the … interference pattern from the substratum dynamics is open" | **Applied.** "Undecided at (γ)" is the first of three outcomes, marked the likeliest on the record. U4 stops there and does not derive. The U4 row's stop condition now includes reaching (γ) | §8.4, check 1; §8.6 (a′); §9 |
| **R1(c).** (α) is C-1 | **Confirmed.** C-1 stays under #1234 | **Applied.** (α) is the conditioning reading, and D-1 is reported per reading. Under the scoped reading, D-1 does not apply off the reference class. "U4 can settle (a′)" is replaced by "U4 can decide (β) and (δ) on paper, conditional on (α), and stops at (γ)" | §8.4, check 1; §8.6 |
| **R2.** U2 still classifies S-A1 to S-A7 | **Confirmed.** #913's gates are accountable at #914 O-INS (#913 c.6628909432) | **Applied.** U2 no longer classifies the closure rules. Their definitions stay in U1 and U3. U2 only reads existing records on them and routes any bearing to #913/#914 | §9, U2 row |

## Owner additions

| Addition | Disposition | Where in r3 |
|---|---|---|
| **1. Recording and renewal tested together** | **Applied** as hypothesis H-RR, not a claim. The three cases are kept separate: RR-1, same-seed reuse with retained records; RR-2, supplied fresh-cell renewal; RR-3, physically sourced renewal. The section states what would support H-RR: a structural, class-(i) result on one interface meeting AC-1. It cannot be a resource count, since "Scarcity alone is not a separator". It states what would refute H-RR: sourced renewal running fresh PR; every exclusion also excluding the Bell reference; or equal renewal costs. It states what leaves H-RR undetermined: the present record. U3 and U4 assess it within the F3 boundaries; nothing is constructed | §4.1; §8.3 Point 3; §9 (U3, U4) |
| **2. Coverage on the same interface as a hard criterion** | **Applied** as AC-1 in §6, a condition of acceptance for every unit, and stated again above the §9 order. A restriction that excludes PR by disabling operations that coherent measurements or allowed Bell correlations need fails. Point 3 now points to AC-1 | §§6, 8.3, 9 |
| **3. The which-path route stays open** | **Applied.** Check 1 keeps classical-field interference, quantum interference (beyond generalized-noncontextual models, W1) and the ability to create or erase which-path information distinct. S-L5 is examined, not assumed: its premises and its scope (linear rule only) are restated and checked against MR★'s review record. The σ12 rules and the observer-level wave-operator route stay open. The test is stated as nontrivial: its outcome turns on (β), (δ), and on whether a noise-induced drop tracks distinguishability and returns under erasure, none of which follows from reversibility alone | §8.4, check 1; §8.6 |

The plan still does not resolve the mechanism. Per the coordinator's note, what it shows is that each
unit can discriminate between the possibilities (§9).
