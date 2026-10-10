# Level 3A — result note (SEALED 2026-10-03 16:36 UTC; artifact hashes in SEAL-3A.md)

Base `0f2687b7`. Read-only, off-repo (scratchpad/level3); no act, freeze or repository implication. Preregistration
PREREG-3A.md `9fe88a1a` (owner-amended before execution). Code seal and amendments: SEAL-3A.md.

## 0. Chronology (provenance; kept visible)

| Step | Artifact | sha256 | Time (UTC, 2026-10-03) |
|---|---|---|---|
| preregistration, with §8 prediction | PREREG-3A.md (candidate) | `ffb58069` | 09:46 |
| owner amendments (one letter c + word-metric scope; Stage C (4,5); R4-CLOSED needs a structural proof about the true orbit) | PREREG-3A.md (frozen) | `9fe88a1a` | 09:50 |
| code freeze (+ amendment 1 before any result run: free-leap letter bug found by validation) | SEAL-3A.md | — | 09:54 / 09:56 |
| validations: letters 121 words/0 (|⟨f,s,c⟩| = 24, |⟨f,s⟩| = 8) · brute force 120/0 · fast = reference 67,478 + 2,124 / 0 | unit_letters.log, validate3_brute.log, validate3_fast.log | — | 09:54–10:06 |
| **pre-output lemma** (masking argument, infinite-horizon ceiling) | LEMMA-3A.md | `272bee1b` | 10:05 |
| **Stage A result** | fast3_stageA_linear.json | `9b88a7cc` | 10:12 |
| **post-output proof refinement** (fresh-coordinate lemma; explicit sandwich) | LEMMA-3A.md (amendment 1) | `6206f1aa` | 10:17 |
| Stage-A reference replay 10/10 MATCH | replay3_A.log | — | 11:05 |
| G identities 143/143 | layers3_linear.json | `fee05255` | 12:03 |
| harness stop of the non-resumable Stage-B run (no output); driver3.py added (orchestration only) | SEAL-3A.md amendment 2 | — | 12:13 / 12:16 |
| **Stage B result** | fast3_stageB_linear.json | `48296b18` | 13:47 |
| **Stage C result** | fast3_stageC_linear.json | `ceb33dc9` | 14:54 |
| Stage-B reference replay MATCH | replay3_B.log | — | 16:35 |
| countercontrol census | cc3_census.json | `729bdd5b` | 15:38 |
| byte-identical Stage-A rerun | rerun3_stageA.log | `9b88a7cc` (= first run) | 15:21 |

R4-CLOSED (§2 below) is a **post-result mathematical theorem**, not a preregistered verdict criterion: its proof
was sharpened after Stage-A output existed. The preregistered verdict is §1.

## 1. Track 1 — the frozen experimental verdict (PREREG-3A §§4–5)

**Stage A** (143 κ, L_p = L_e = 3): 76 ADVANCE with dims [2, 3, 4] and certified rank 4; 64 NOT-INVASIVE, rank 1;
3 NOT-INVASIVE, rank 4. Certified 143/143; WELLDEF 143/143; no rank above 4. The invasive set is exactly the
linear rule's Level-2 invasive set.

**Stage B** (the 76 advancing κ, L_p = L_e = 4; 781 preparation protocols → 1,523 or 1,538 positive-weight
preparations; 2,801 effects): **76/76 AT-RANK** — certified table rank 4, dims C = [2, 3, 4, 4] (C₃ = C₂), WELLDEF
holds, invasive, for every κ. No OVER-RANK, no UNDER-RANK, no INCONCLUSIVE.

**Stage C** (depth probe, L_p = 4, L_e = 5; the first three AT-RANK κ in frozen order — ((0,1),(0,1)), ((0,1),(0,2)),
((0,1),(0,3)) — no UNDER-RANK κ exists): **3/3 C-CONSISTENT**, dims C = [2, 3, 4, 4, 4], certified table rank 4
against 19,608 effects on the Stage-B preparation set (1,523 / 1,538 / 1,538 preparations), WELLDEF, invasive.
No OVER-RANK.

**Level 3A label: EXPOSED** (76 κ AT-RANK, 0 κ OVER-RANK at every stage) — final.

**Validation gates.** Stage-A reference replay: 10 jobs (nine fixed positions + the class-completion pick), 10/10
field-by-field MATCH, covering all three Stage-A outcome patterns. Stage-B reference replay (κ ((0,1),(0,1)),
reference table computed in 507 resumable chunks on the reference simulator, then the unchanged `analyze`):
AT-RANK, rank 4, dims [2, 3, 4, 4], field-by-field MATCH with the fast-evaluator record. G identities (G2 forgetful sum, G3 normalization,
G3 trailing-idle): 143/143 — faithfulness checks of the extended simulator, not evidence about nature (L-G).
Countercontrol census (m with the branch maps exchanged, all 143 κ): G2 fails on 71/143 — on 68 of the 76 invasive
κ and 3 of the 67 non-invasive; of the 8 invasive κ not caught, 4 have κ₀ = κ₁ (the mutation is the identity) and
4 are operationally null; G3 identities unaffected (143/143). This is the same pattern as RECORD's Level-2 census
(71/143), so the G2 check discriminates under I₃. Byte-identical Stage-A rerun after Stages B and C: `9b88a7cc`
both times.

## 2. Track 2 — the structural conclusion (LEMMA-3A, post-result)

**Theorem (pair-marginal reduction; LEMMA-3A §3 with the fresh-coordinate lemma of its amendment 1).** Under the
linear leap and the product initial measure, for OBS-R and any interface built from pair permutations,
record-writing pair maps κ_b and leaps, every protocol probability is a function of the four-state pair marginal
of the prepared state: after every leap one pair coordinate is a cone-edge initial variable that is fresh
(edge-permutivity) and independent of everything observable (product measure). Hence the infinite-horizon
effect space, as functionals on all preparations, has dimension ≤ 4, and so has C(r; G₃).

**Sandwich.** For every κ with a certified finite table of rank 4 and certified dim(C_k|_X) = 4:
4 = dim(C_k|_X) ≤ dim C(r; G₃) ≤ 4, so dim C(r; G₃) = 4; C(r; G₃) contains 1 and r and is G₃-invariant by
construction. **R4(r; G₃) holds with E = C(r; G₃): R4-CLOSED.** Finite equality C₃ = C₂ and Stage C play no role
in this conclusion.

**Taxonomy of the 143 κ.**

| Count | Status | Basis |
|---|---|---|
| **79** | R4-CLOSED(r; G₃) | Stage A certifies dim(C₂\|_X) = 4 (lower bound); the theorem supplies the ceiling |
| 76 of the 79 | additionally operationally invasive → count toward the preregistered capacity question (EXPOSED) | G-INV per κ |
| 3 of the 79 | passive-type (v-image = b on both branches): R4-CLOSED mathematically, **excluded from the capacity verdict** by G-invasiveness; not failed R4 cases | G-INV per κ |
| 64 | rank 1 at every horizon (nothing learnable), non-invasive | Stage A; the theorem's mechanism (both branch images v-distinct) |

**Status of the proof.** Lemmas 1–2 and the Theorem are written and short; independent review is the remaining
verification step. The computation is their control: no certified rank exceeded 4 anywhere (Stages A, B, C).

## 3. Descriptive diagnostic (post-freeze, not a criterion; geometry3.py)

For κ ((0,1),(0,1)) and ((1,0),(0,2)) at L_p = 4, in the fiducial coordinates (P(v = 1), P(u = 1),
P(u ⊕ v = 1)) predicted by the theorem: all 1,523 / 1,538 positive-weight preparations map to exactly **7 distinct
points** — the centre (½, ½, ½) and the six vertices of the octahedron |x−½| + |y−½| + |z−½| ≤ ½ — and no other
point. Every reachable state is therefore either "one register function known, the rest fair" or "nothing known";
the convex hull of these seven points is the octahedron; the computation shows only the seven points, with no
intermediate mixtures, and does not by itself make the octahedron the state space. At L_p = 3 one vertex of ((0,1),(0,1)) is not yet reached
(it needs the word `osfs`): a horizon artifact, gone at L_p = 4. This is a finite-horizon description of two κ; the
exact reachable set for all preparations is not certified here.

## 4. What this result is, and is not

- **It is an interface-capacity result:** I₃ = IC × {f, s, c} can expose a 4-dimensional observer-relevant sector
  for the linear rule — 76 invasive κ at AT-RANK under the frozen criteria, and R4-CLOSED by the theorem. It removes
  one specific way the R4 bridge could have failed for this rule: hidden dimensions appearing with the horizon.
- **It is not evidence on A5 versus A4-S.** Only the linear rule ran. The theorem's inputs are edge-permutivity and
  the product measure, not linearity; 3B varies exactly those two levers (edge coordinate survives the rule;
  hidden law preserves its independence).
- **It is not a QM result, and it sharpens the Q gap.** The exposed sector is the pair-marginal space; its
  protocols reach only seven discrete states (§3, two κ, finite horizon), whose convex hull is a polytope — the
  knowledge-balance structure — not a ball; convex mixing is not itself part of the adopted structure here. A finite substrate with this
  interface yields a classical-epistemic 4-dimensional sector (OI-STAGE NG1 made concrete); whatever selects a ball
  over this polytope is a Q-layer premise the substrate and interface do not supply.
- **Scope:** OBS-R only (no transfer to OBS-M, OBS-C); H₀ only; r fixed; the word metric of {f, s, c}
  (PREREG-3A §3).

## 5. Artifacts

PREREG-3A.md `9fe88a1a` · PREREG-3B-DRAFT.md `4ef4c775` · LEMMA-3A.md `6206f1aa` (pre-output `272bee1b`) ·
SEAL-3A.md · fast3_stageA_linear.json `9b88a7cc` · fast3_stageB_linear.json `48296b18` · fast3_stageC_linear.json
`ceb33dc9` · layers3_linear.json `fee05255` · cc3_census.json `729bdd5b` · replay3_A.log · replay3_B.log (MATCH) ·
rerun3_stageA.log · select/ (SELECT research note, separate thread) ·
geometry3_L3.log, geometry3_L4.log · validate3_brute.log · validate3_fast.log · unit_letters.log · ckpt/ (per-κ
checkpoints and reference-table chunks).
