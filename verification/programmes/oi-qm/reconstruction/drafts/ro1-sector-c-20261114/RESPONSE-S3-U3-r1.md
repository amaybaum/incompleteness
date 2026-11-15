# Response to the review of S3-U3-r1

**Object reviewed.** `S3-U3-r1.md`, blob `3da2be223f61e5d7c99d0c8553f0ba5f065ede4c`.
**Review.** `REVIEW-S3-U3-r1.md`, blob `4155bc8de64d60162f7605ceba3b459dd706b114`, at
`ea1c1b5dc98a0fe86939990dfb544ae33e090eef` on branch `research/ro1-sector-c-1169-20261114`
(verdict ACCEPT WITH CHANGES; required R1–R4, minor M1–M10).
**Revision.** `S3-U3-r2.md`. r1 is left unchanged.

**Writer:** Claude Code. Paper-only: reading and hand reasoning, no computation, no Lean, no
manuscript or record edit. Every [A-inf] in r2 is an author-side hand check and is not verification.

One disposition per finding: **applied**, **partly applied** or **not applied**, with the reason
and the place in r2.

***

## Required

**R1. RQ-UPD-1 overstates what L-2 forces. Applied.**
- §2.2 now writes the second-use content as `κ` and states three exhaustive cases: (U) unchanged
  source, (S) source update (`κ` depends on the first use's settings or outputs at positive mass),
  and (N) setting-independent renewal (a different preloaded cell, a setting-independent bijection
  of `λ`, fresh noise, or a tick-indexed response). The fresh-cell lemma is cited for (N) being able
  to give no-signalling for PR (SEL-EXCL-1 §3, l. 181).
- RQ-UPD-1 now reads: with no-signalling under reuse, (k2) fails, by (S) or (N); conditional on L-2.
- Propagated to §3 (RQ-REU's last bullet and RQ-UPD-1), §4.1 (content of RR-1), §5.1 (what L-2
  does not cover), §8 U3-1, §10.1 (RQ-UPD row), §10.2 (RR-1 and RR-2 rows) and §10.5 (routing of
  the three cases).

**R2. RQ-UPD-2 stated on the wrong ground; a stronger route exists. Applied, after an independent
hand check.**
- *Check of the reviewer's inference.* Re-derived by hand in §5.2 as the proposed lemma L-3.
  **It holds.** Scope: deterministic responses with binary settings and outcomes (k1); the product
  policy pairs (Alice `(x, x)`, Bob `(0, y₂)` and `(1, y₂)`) and their mirrors jointly executable
  on one `M` and one AD-1 instance, and in the unchanged-source case one pair per `x` with Bob
  `(0, 1)` suffices (k3′); S5 at policy level for all content read (k4′); both uses' records held at
  `t_c` and `Θ` (S8) identifying the program with the two-use Lüders experiment (k5′); no failure
  branch, or a setting-independent herald that is a function of the source. No no-signalling
  premise, no L-2 and no L-1 are used, and no atomic source law is needed. TSI (9) was re-checked
  by hand as the Lüders update on `|Φ⁺⟩` with Bloch-orthogonal axes on each wing.
- *What the check adds beyond the reviewer's form.* The same argument excludes setting-independent
  renewal (N) and dependence on the wing's own first setting alone, not only unchanged-source reuse
  (U). The exclusion is per wing: it applies to each wing whose first-use response depends on the
  remote setting at positive mass, and at least one wing is of that kind because (1) violates
  CHSH. A Bell-local wing needs no update (the reviewer's `a = λ_x` example, kept in §3 and §5.2).
- *Restated (i) and (ii)* (§3, RQ-UPD-2). (i): at a repeated setting the wing's second-use content
  determines the first outcome, and on each remote-dependent wing it must depend on the first use's
  outputs or the remote first setting, a source update (S). (ii): at a changed setting each wing's
  second-use content must carry information that `(x₁, y₁, a₁, b₁)` do not determine; it may be
  preloaded in `λ` (booked in `μ`) or renewed.
- *Dependence.* RQ-UPD-2 rests on L-3 (proposed), TSI (9) [NP] with the hand re-check, S5 and `Θ`.
  Nothing in it rests on L-2. Carried to U3-2 (§8), §10.1's RQ-UPD row and §10.3's RQ-UPD row. The
  inference is credited to the review in §5.2 and in U3-2's check column.
- L-2 remains labelled a proposed lemma throughout, and every conclusion resting on it carries
  "conditional on L-2" where it is stated (§§3, 4.1, 4.4, 5.1, 8, 10.1–10.4).

**R3. Scope and classification of the capacity bound. Applied.**
- (a) Owner question 1 is put as bearing on ledger Q1 (SPEC:404–405; "stays with #914",
  SPEC:620–621), and the nested-partitions option is stated as reading (c) (§6, §10.7).
- (b) The two coverage targets are reported separately in §6, U3-4 and §10.3's RQ-CAP row:
  answer 3's arbitrarily large finite carriers, which no model of the frame meets under reading (a);
  and the amended AC-1's perceived phenomena, which have finite records and are excluded only on a
  model whose family is too small (not checked).
- (c) §6 now opens as a K-3 report on the frame. It states that the bound follows from G4's
  joint-hold clause (U1's [P]), AD-1(a)'s finite family read as fixed per model, and answer 3; that
  it is not a native fact about OI models, disproves no input and is not a *not available* outcome
  under SNR-1. r1's "Its outcome is *not available*" and "fails on every model" are removed; the
  program is described as having no execution in U1's sense on that model. §6 also notes that U1
  §5.3's coverage-neutral cell for G4 holds per program and, at answer 3's scope, only up to `N_held`.
- (d) Ground corrected: Main:42 gives the finiteness of each observer; the family's finiteness is
  AD-1(a)'s wording and its fixedness is reading (a).
- (e) RQ-SEQ's bound (§3), U3-4 (§8) and §10.1's RQ-CAP row carry "under reading (a)".
- (f) Count corrected: at most `2^{2m}` per wing; `2^{2m}` for a randomized policy with full-support
  settings and outcomes; `2^m` for a fixed policy with full-support outcomes.
- (g) Class changed to ELABORATING (J1 under G4; held-capacity analogue of SEL-DISC-1 l. 79).
- The reviewer's K-1/K-2 assessment is recorded in §6.

**R4. E1 used as performed-experiment data. Applied.**
- §10.3 now states that E1 is an explicit empirical input summarizing QM's success, not a raw-direct
  record of a performed sequential experiment on one entangled source, and is not used as one.
- The RQ-UPD row's agreement half is conditional on a performed experiment that measures one
  entangled source twice per wing with a setting change between uses and whose raw complete
  local-history records show setting-independence (and, for the L-3 ground, repeatability). Whether
  such an experiment exists and has been read first-hand is owner question 4.
- "Demanded by" E1 is removed from the candidate-restriction row, which now reads as conditional on
  the same experiment and not checked.

## Minor

**M1. L-2's (k3). Applied.** (k3) now requires the product policy pairs to be each executed on one
`M` and one AD-1 instance (G6), and states that the proof does not use how the second setting
reaches the use, a `φ`-effected write or a preloaded per-use slot (TSI:57, :87–94). The unused
"`φ`-effected" clause is dropped from (k3). Binary settings and outcomes are explicit in (k1). The
TSI check now uses L-2's own comparison (Bob `(1, 1)`, Alice `(0, 0)` against `(0, 1)`, giving
`(R⊕C, R⊕C)` against `(R⊕C, R⊕C⊕1)`) and names TSI (10) as a different witness (§5.1).

**M2. §2.1's "exactly when". Applied.** `Δ_k` now includes component inputs re-certified in the
composite context (for example freshness of a stage-2 cell relative to stage 1), so both directions
hold by U1's definitions; the reasoning is stated (§2.1; §10.1 RQ-CL row).

**M3. §4.2's dependence direction. Applied, by a different route.** The probe point now uses an
elementary step (§4.2): with S5 and deterministic binary responses, a Bell violation gives a
positive-mass set on which `a` depends on `y` or `b` depends on `x`. The probe is on whichever wing
applies. This step is the last step of L-2's proof read in reverse, holds for non-atomic source laws
and does not use L-1, so the probe point no longer carries L-1's open scope question (PR #1294
review 5909913170). Carried to §4.4, U3-3, U3-6 and §§10.2–10.3. The same step supports the
optional K-2 strengthening of §6 of the review, now stated in §2.4.

**M4. U3-1's "exposes an assumption in DEPS §5.1". Applied.** U3-1 now records that DEPS already
limits the discriminator to the same-seed PR implementation (DEPS:397–401) and that TSI gives the
quantum-calibrated instance. The finding is that the label "discriminator", read as PR against QM,
is unsupported for unchanged-source reuse; NEW is kept for L-2's general statement only, and the
bearing on DEPS and PLAN is ELABORATING (§8).

**M5. §10.1 question 1. Applied.** Restated: under μ-G and D4's premise, a native hidden fresh cell
cannot influence the records of a program needing full in-`V` histories (OA1:162–175); visible
heralded cells (D3) are not excluded, and D4 "dissolves under MP-0a" (OA1:174).

**M6. GR-2 and RR-1 at the next tick. Applied.** §2.5 now states that the re-application reuses each
cell at its first setting, that RR-1 also needs a `φ`-effected setting change between the ticks,
and that RR-1's question becomes native only where such a change is effected and the budget allows
it. U3-5 is narrowed to match.

**M7. CQ-2 and S8. Applied.** CQ-2 is conditional on L-2 and on the adoption of `Θ` (S8) (§10.4).

**M8. Authorization block and §10.6. Applied.** C1 is quoted with "followed by ChatGPT exact-head
review". §10.6 reads "noted for #1143".

**M9. Ground for the persistence of a source update. Applied.** The C-RET parked-record citation is
dropped; the persistence of a hidden source update is grounded on C2-structural (Main:74) alone
(§2.2; §7's RQ-UPD-2 row).

**M10. Bounded negative on L-2's novelty. Applied.** The review required no change. The
statement is kept with its stated search and extended to L-3 with a further stated search, which
found Main:652 (the Lüders rule as Bayesian updating for the diagonal sector; noncommuting updates
belong to the instrument algebra). L-3 is recorded as consistent with it (§1). The literature caveat
stands (owner question 2).

## Other changes made as necessary consequences

- L-1 is no longer used for any conclusion. It is mentioned only as context, at finite or atomic
  source laws with unconditioned full-attempt statistics, citing PR #1294 review 5909913170, whose
  repair is not decided (header; §§4.2, 5.1, 9; owner question 2).
- §9 adds rows for r1 and the review (provenance) and for PR #1294 review 5909913170 (support off
  `main` for the L-1 scope statement only).
- Owner questions updated (§10.7): question 1 states three readings of AD-1(a) and asks which
  coverage target RO-1 checks closure against; question 2 covers L-2 and L-3; question 4 states that
  E1 supplies no raw-direct reuse data and names the experiment class to be read first-hand.

No H-RR status, routing target, readiness or authorization changes.
