# QPHEN Phase 1 r2: dispositions of `review/REVIEW-PHASE1.md` (`8d704712…`)

**Scope and standing.**
- Paper only and model-written. The r1 files are kept under `r1/`.
- Every substantive edit in r2 maps to one row below. Nothing else was changed beyond the revision headers and the
  reference tables these rows require.
- Owner decision cited: D18(a), conditional (#1169 c.6735014875, amaybaum, 2026-11-09T07:52:50Z), as directed by the
  coordinator.

## Blockers

### B1. Main §3.3's reach

**Where applied.** QX6 §1, §3, §3.2, A6.1, §6 (`A_6`, `B_6-loc`, ABL-BOT), §8 item 2, §10 Q6-4; SHARED §3, §4 controls,
§6.

**Disposition.**
- Main's literal hypotheses are quoted: a one-step setting and iterates of one fixed `φ`.
- A6.1 is restated as this file's own derivation [A, unreviewed], with hypotheses (D), (L), (R) and (MI) and a proof
  sketch. It covers time-dependent maps whose dependency graphs lie in one graph `G`, multi-tick own-wing settings,
  and P3 arming inside a wing.
- A declared local `⊥ ↦ +1` rule is added. Coincidence-only statistics are named as the detection loophole.
- The conclusion is narrowed to access restrictions, state restrictions on a setting-independent ensemble, own-wing
  operations and local registration rules, under A6.1's hypotheses. R6.7 is named as a candidate OI principle that
  A6.1 does not cover.

### B2. QX-3: routing not shown to need non-affinity

**Where applied.**
- QX3: §1 (`NCONS_ready` and `NCONS_global`), R3.6, A3.1(b)–(d), §5 (ABL-ROUTE restated, ABL-NCONS added), §6, §7
  item 3, §8, Q3-2.
- QX4: R4.9, A4.4's consequence.
- SHARED: M14, §3 counting, H-SDC (statement and obstacle 6), T4, §5's QX-3 and QX-4 rows.

**Disposition.**
- The false step ("complementary values mean clicking on absence") is withdrawn.
- The map `L(s, c₁, c₂) = (s, s + c₁, s + c₂)` (P2) is stated: `α = 0`, own-cell reads, weight conserved on the ready
  support, equal to Fredkin on the single-excitation sector.
- A3.1(c) proves that globally weight-preserving affine bijections are coordinate permutations. Non-affinity is
  therefore forced only under `NCONS_global`.
- The domain is an owner decision (Q3-2).
- Whether OI's step admits either map is stated as MECH-OPEN and is not evaluated.
- The count of non-affine rules is corrected to two, with routing a third only under `NCONS_global`.

### B3. QX-6 GHZ row

**Where applied.** QX6 §2 (GHZ row), §5; SHARED M11 (QX-6 cell), M18.

**Disposition.**
- "Needs `Y` reads" is withdrawn.
- The triangle graph state contradiction with `X/Z` reads (P1) is stated, and `Y` is attributed only to Mermin's
  standard presentation.
- The prerequisites are restated as a three-party source and a cross-wing response, and the native affine class is
  noted to be local.
- Coecke–Edwards–Spekkens is no longer cited for this claim.

### B4. QX-4 A4.4: missing protocol hypothesis

**Where applied.** QX4 §1 (INM control), §2 (INM row), A4.4 (H1)–(H4), ABL-NULL, ABL-T1 (new), §7 item 3, Q4-2;
SHARED M16, T2.

**Disposition.** The hypotheses are stated:
- `Q₁` by preparation from a setting-independent supply, or an INM read at `t₁`;
- `K_null = id` for both placements;
- placement independent of the ontic state;
- `Q` a configuration functional (IR).

The consequence is now conditional on them. ABL-T1 controls against taking credit from a `t₁` kick.

### B5. QX-4 A4.1's scope

**Where applied.** QX4 A4.1(a)–(c), AW-QX4-1, §2 (Budroni–Emary), §5 (`A_4`, `B_4-nat`, ABL-SA1c, ABL-G), §6, §7 item
2, §8 Level 2 (values above `3/2` reported, not credited), Q4-4; SHARED M3 row, §3, T9, §4 controls, §5.

**Disposition.**
- The one-mode scope is stated for (a).
- The reviewer's two-mode scan is (b): maximum 1 under SA-1(c) or environment supplies, 2 with a sharp mediator; its
  witness is quoted.
- The integer-valued form (c) carries the ladder-relevant claim that QX-4c's QM-matching value depends on Obligation C.
- `A_4`'s expectation is corrected.
- ABL-SA1c predicts that `K₃ = 2` is reachable.
- AW-QX4-1 is recorded as an assumption-watch marker, not a result, with §A.31 skepticism and a request for an `m`-mode
  proof.

## Nits

| # | where | disposition |
| --- | --- | --- |
| N1 | QX6 §2; A6.2 | Fine's theorem (joint measurability) is given as the commuting-case reason, covering multi-qubit wings. A6.2's "necessary" is qualified "with a stabilizer pair state", noting that a non-stabilizer pair state with Pauli settings reaches `2√2` |
| N2 | QX6 §1; §8 item 10 | TLM is stated as exact for the correlator projection. For full behaviours with biased marginals, the absence of an exact closed-form test is stated as a limitation |
| N3 | QX6 §3; R6.10; §6 PR-6 | PR behaviour is attributed to an enlarged source class as a separate conditional countercontrol; the fixed baseline source does not reach it |
| N4 | QX6 A6.4; §3.2; ABL-SA1c/N2 | Restated: signalling holds iff the supply leaves the kernel of the balance map, so ABL-SA1c/N2 is not predicted. N2 and SA-1(c) are "the only state restrictions in the present toolkit; neither is shown to mask". The corollary reading is recorded as a hypothesis, with §A.31 skepticism |
| N5 | QX6 §3, §8 item 2, §11; SHARED H-SDC obstacle 5 | Cited as `verification/ROADMAP.md`:974-979 at `fd539e15` (checked), quoted in HB-1 under 764-769 |
| N6 | QX3 §0 | The file is named `oicore/OICORE-1.md` (`9b82ecc2…`), with its one-cell difference from `OICORE-1-r6.md` (`ec7966c9…`) noted |
| N7 | QX3 §10; QX4 §10; QX6 §11; SHARED §7 | Issue comments are traced: #1210 c.6736966265 and c.6734406842; #1169 c.6734304025, c.6734374076 and c.6735014875; #1060. c.6734406842 item 2 is reclassified as provenance, with its support `DESIGN-DS.md` finding 6 [D]. OICORE-1 is added to QX4 and QX6. `DECISIONS.md` and NR-13, NR-14 and NR-16 are added to QX3. The review file and probes are traced where they support r2 statements |
| N8 | QX3 §0; SHARED M9 | Per the coordinator's direction: D18 was decided by the owner as (a), conditional (c.6735014875, quoted with author and time). Its scope is path, port, calibration and U′. L-CLICK is outside it and is put to the owner (Q3-3) |
| N9 | QX3 §3; QX4 §3; QX6 §4; SHARED §1 | Type and dependency are separate columns. Types are EN, CS, IQ, IR and untyped. Dependencies are MC, MECH-OPEN and — |
| N10 | QX3 A3.2; SHARED T1 | The hazard is identified as the existing copy-only hazard (`DESIGN-DS.md` finding 9 / ABL-RECIP). Routing matters only because a non-affine rule need not be reciprocal (`G_SM`) |
| N11 | SHARED T8; QX4 §1, §7 item 1 | "OI" is replaced by "construction B, given SA-1(c) (CS) and the IR premise that the read quantity is a configuration functional" |
| N12 | SHARED §4 controls; QX4 and QX6 §§6–7 trees | C's ABL and W-CL are marked conditional on Theorem C [D] and Lemma P (conditional on Theorem C(ii), L1–L3). Lemma M's applicability (a core-realizer satisfying the restriction; not used for ACC_op) is stated |
| N13 | QX6 §3.2 | Region overlap and insufficient separation are added as escape routes, excluded by the design (R6.2) and not by the theorem |
| N14 | QX4 §3 corpus search | Main:358 ("Leggett-Garg violations included, §3.4") is added |

## Kept as the reviewer advised

- The Main and Substratum anchors.
- The rational comparators: `S = 5/2`; `K₃ = 3/2`, `4/3`, `37/25`.
- The separation of ontic from operational no-signalling, and the `access_only` discipline.
- QX-3's classical-field ceiling, and QX-4's point that Main:486 reaches `K₃ = 3/2` classically.
- H-SDC as named only.
