# QPHEN Phase 1 r4: independent full-text review

## Standing

- **Reviewer.** An independent, model-written review. It is read-only on the repository, git and GitHub. It writes
  only this file and the probe `review/probes/p8_r4rev_membership.py` with its output `p8_r4rev_membership.out`.
- **Files reviewed** (sha256 verified before reading):

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `f372cef7d3baad57…` |
  | `QX4-INCOMPATIBILITY-LG.md` | `2765e6f7cb06e4d6…` |
  | `QX6-BELL-CHSH.md` | `5c7ab0cb6efce8e3…` |
  | `SHARED-MECHANISM.md` | `23ec1ef19be8b2dd…` |
  | `DISPOSITIONS-r4.md` | `a886e40d0311849b…` |

  The r3 texts under `r3/` match the hashes in `REVIEW-PHASE1-r3.md` (`448614ea…`). `R4-REVIEW-ADDENDA.txt` is
  `7aa1b1ad…`, as DISPOSITIONS-r4 states.
- **Corpus.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (fetched 2026-11-09; no depth, gc or prune).
  `papers/Main.md` at that commit equals the session-local copy `main_fd.md` (`6144cd4a…`). Main:22, :44, :50, :56, :362,
  :364, :366-391, :403-414, :416, :418-421, :486 and :652 were read and are as quoted.
- **Owner records read** (read-only): #1210 c.6739286623 (amaybaum, 2026-11-09T11:47:25Z), c.6739311717
  (11:48:47Z) and c.6739250392 (11:45:26Z). The quotations in QX-3 §0 and the "Allowed: generic checks" answer match.
- **Method.** All four specifications and DISPOSITIONS-r4 were read in full, and `diff r3/ r4` was read for every
  file. `p7_r4_lg_order.py` (`6eb7f784…`) was re-run as a script with `python3 -I` from a separate directory (exit 0);
  its output equals `p7_r4_lg_order.out`. The new probe `p8_r4rev_membership.py` imports no earlier probe; it passes
  47 of 47 checks.

## Verdict: **REVISE (narrow)**

r4 fixes B1–B3 of r3 correctly, and the mathematics it adds is correct. Two blockers remain:
- **B1** concerns owner requirement 2: one disproved entry, Q4-D3, uses a counterexample outside the class in which the
  claim is naturally read, and that narrower claim is true.
- **B2** is a necessity statement introduced by r4's rewrite of QX-3 §7 item 5. It is stronger than A3.1(a)
  supports, and the item's own example contradicts it.

The owner's added check, that summary and dependency-table conclusions match their proofs in scope and status, finds
eight mismatches (§ "Summary-scope mismatches"). None is a false theorem. Several state a conditional or one-way
result without its condition. Under the owner's instruction these are must-fix.

Each item needs a one- or two-sentence edit. An r5 that applies B1, B2 and the must-fix nits N1–N8 needs only a check
of those sites.

***

## Blockers

### B1. Q4-D3: the counterexample is affine but not symplectic, and the narrower affine-symplectic claim is neither open nor stated

**The text.** SHARED Q4-D3: *Claim:* "A detector that interacts only when its cell is occupied is a controlled coupling
and lies outside the affine class." The counterexample is the copy coupling `m ← m + c`. The membership line says only
that the coupling acts only when `c = 1` and that `(c, x, m, m′) ↦ (c, x, m + c, m′)` is linear over `F_2`.

**Why it does not meet owner requirement 2.**
- In QX-4 "the affine class" also names A4.1's affine-*symplectic* class (A4.1's title, A4.1(c) "in the affine class").
  That is SA-1(a)'s class, the one the INM question concerns.
- The copy coupling is not symplectic for the pairs `(c, x)` and `(m, m′)`; p8 (6) checks this.
- Restricted to the affine-symplectic class, the claim holds:
  - **Exhaustive check.** Over all 720 × 16 affine-symplectic maps on `(c, x), (m, m′)`, none is the identity on the
    `c = 0` branch while changing a meter slot on the `c = 1` branch. Six affine non-symplectic maps do both
    (p8 (6), exhaustive).
  - **Argument.** A linear `M` that is the identity on `{c = 0}` is `M = I + d e_cᵀ`. Symplecticity requires
    `ω(d, e_j) = 0` for every `j ≠ c`. Then `d` lies in the span of `e_x`, so no meter slot changes.
  - **Agreement with the spec.** This is exactly the content of R4.9's sentence that the reciprocal coupling "acts on
    both branches".
- The membership line therefore shows membership only in "affine maps, not necessarily symplectic". It does not say
  so, and the narrower claim, the one about OI's native class, is not kept open as the owner's rule requires. Under
  the natural reading the entry marks a true statement as disproved. This is the same kind of ambiguity as r3's B3.

**Required fix.**
- Restate the claim as "… lies outside the class of affine maps of `F_2⁴` (not necessarily symplectic)".
- Add to the membership line: "the copy coupling is not symplectic".
- List the affine-symplectic form as open, or as proved [A, the three-line argument above; X: p8 (6), two modes,
  computation-supported]. As the owner's rule allows, "open" suffices unless the proof is adopted.

### B2. QX-3 §7 item 5 (rewritten in r4): "Intermediate values … therefore need non-uniform laws or mixtures"

**The text.** "Under N2 with affine functionals, `α ∈ {0, 1, 2}` (A3.1(a)). Intermediate values … therefore need
non-uniform laws or mixtures. Rationality of the probabilities is not the obstacle: the dyadic law … (cells
`9, 151, 71, 25` out of 256) gives `α = 9/50`."

**Why it is wrong.**
- A3.1(a) has two hypotheses: N2 laws uniform on a coset, and affine functionals. Leaving the case `α ∈ {0, 1, 2}`
  needs the failure of either one.
- The item lists only the failure of the first. A uniform N2 law on 256 configurations, with non-affine detector
  functionals whose cells are `9, 151, 71, 25`, gives `α = 9/50` with no non-uniform law and no mixture.
- The item's own example is therefore a counterexample to its necessity claim.
- This is a changed claim stronger than its evidence (necessary → sufficient type; Code Review Rules, claim/evidence
  boundary).

**Required fix.** Replace "therefore need non-uniform laws or mixtures" with "therefore need non-uniform laws, mixtures,
or non-affine detector functionals". Q3-P11's arithmetic is correct: p8 (8) checks it.

***

## Nits

**Must fix before freeze consideration** (N2–N8 are the summary-scope mismatches the owner asked for)

- **N1. The §8 membership rule reverses "narrower" and "wider".**
  - SHARED §8 says: "Where membership cannot be shown, the refuted claim is narrowed to a class the counterexample
    belongs to, and the wider claim is listed as open."
  - If the class were narrowed, that is made a subclass, and the counterexample belonged to it, it would also belong to
    the original class. So the rule as written is incoherent.
  - What r4 does is correct: Q4-D1 and Q4-D2 are restated over a larger class that contains the counterexample, which
    makes them stronger universal claims. The original claims, `A_4` (Q4-O6) and the INM form (Q4-O8), are the
    narrower ones, and they stay open, as the owner put it: "Keep the narrower claim open".
  - Fix the rule: "… the refuted claim is restated over a class the counterexample belongs to, and the original,
    narrower claim is listed as open".
  - Fix Q4-D1's header: "as narrowed" becomes "as restated". DISPOSITIONS-r4 N6 uses the same wording.
- **N2. QX-4 A4.1(c) and §7 item 2: "`K₃ ≤ 1` itself is established only at the scopes in (a) and (b)".**
  - This contradicts Q4-P3 and the preceding bullet of A4.1(c). Integrality, together with the Lüders bound, which is
    now proved [A], gives `K₃ ≤ 1` for Clifford `G` with pure stabilizer preparations, and for their mixtures, at any
    number of modes. The bullet says it "still holds" for mixtures.
  - p8 (7) gives numerical evidence: all 11,520 two-qubit Cliffords and all 60 two-qubit stabilizer states give
    integer correlators and a maximum `K₃` of 1.
  - Qualify both sites as "in the affine-symplectic class with A4.1's read model".
- **N3. "Not sufficient" without its condition.**
  - QX-6 A6.2's title is "… and not sufficient", and SHARED §2's cell M12 × QX-6 reads "r (…; not sufficient; A6.2)".
  - The supporting result, Q6-P10, holds only under A6.1's hypotheses, including the design assumptions (L′) and (R).
    SHARED §5 already states this; the title and the cell do not.
  - Add "(under A6.1's hypotheses, including the design assumptions (L′) and (R))" at both sites (owner requirement 1).
- **N4. SHARED §3 "Counting": "A construction serving all eight therefore needs, at minimum: M12; M19 with M20; M18;
  M14".**
  - This is a necessity conclusion with no §8 entry. Its supports are conditional:
    - M19's necessity rests on A6.1 [A], conditional on (MI) and the design assumptions (L′) and (R);
    - M12's necessity for QX-4 holds only with stabilizer preparations (A4.1(c));
    - for QX-1, QX-5 and QX-7 its support is D drafts.
  - State the conditions, and enter the statement in §8.4 (proved conditional, or open where the support is D).
- **N5. The class W2 excludes, as summarized.**
  - QX-3 §2's "Consequence", QX-3 §7 item 7 ("classical fields under square-law detection only") and SHARED §5's QX-3
    row ("W2's best case excludes classical fields only") are narrower than QX-3 §2's W2 row. That row excludes W1's
    class and "particle models with no wave-like phase variable"; `V > 0` excludes CP-3.
  - Make the summaries match the row.
- **N6. "Must keep an outcome-independent kick" (SHARED T2's last sentence; QX-4 A4.4, "Consequence", last bullet).**
  - A4.4 proves only that a construction matching the comparator protocol under INM, given (H1), (H2) and (H4), needs
    `K_null ≠ id` (Q4-P6).
  - An outcome-independent kick is one sufficient realization. A kick on the silent branch alone would also give
    `K_null ≠ id`.
  - Within the affine-symplectic class an unconditional kick is forced (B1's argument). For a non-affine routing map it
    is not shown.
  - Restate as "must act on its silent branch (`K_null ≠ id`), for example by keeping the reciprocal,
    outcome-independent kick". No §8 entry carries the stronger form.
- **N7. QX-4 §5, `A_4` arm: "`K₃ ≤ 1` is not expected".**
  - This is a residue of r3's B2. The sentence before it says that whether `A_4`'s admissible `G` contains the witness
    is construction-specific, and Q4-O6 lists `A_4`'s value as open.
  - Replace it with "`A_4`'s value is open (Q4-O6)".
- **N8. Probe layer labels in the spec bodies still read D.**
  - QX-4 A4.1(b) is labelled "[D: the reviewer's exhaustive finite scan, P3]". Under §8's rule ("A claim whose only
    support is a W record or a D draft is open") this conflicts with Q4-P2 [X; proved, computation-supported].
  - The same residue appears at:
    - QX-3 A3.1's heading ("probe P2 (D)");
    - QX-4 A4.1(c) ("P5-LG (D), exact");
    - QX-6 §2 ("P1 (D)", "P4(3) (D)", "P5-GHZ (D)");
    - QX-6 A6.1's checks ("P5-A61 (D)").
  - Relabel them X, with "computation-supported" where that applies. "Off `main` (D)" may stay in the reference tables
    as provenance.

**Precision**

- **N9.** All four §0 sections say "probes P1–P6", but QX-4 and SHARED cite P7. Write "P1–P7", or "P1–P8" if this
  review's probe is cited.
- **N10.** Q6-P10 and QX-6 ABL-BOT say "the rules `⊥ ↦ ±1` keep (R)". A6.1's (R) is defined with `⊥ ↦ +1`. Say
  instead: "(R) with `⊥ ↦ +1` replaced by any fixed local rule; the proof is unchanged, since steps 5–6 use only that
  each outcome is a function of its readout region".
- **N11.** QX-6 R6.4's type column carries (L′) but does not classify it as a design assumption of the Bell test, as
  R6.2's column does for (R) (owner requirement 1). Add the same words.
- **N12.** Q3-P6a's count (64 routers, none affine) and Q4-P7's environment and mixture values, which Q4-D1 relies on,
  rested on a single probe (`p6_r3rev_*`). The X rule needs a second probe. p8 (5) and (8) now reproduce them exactly,
  so cite p8 there.

**Optional**

- QX-4 §0 line 10 and QX-6 §0 line 8 are unwrapped.
- "Because that reading favours the framework" (QX-4 AW-QX4-1; QX-6 A6.4) and "stated first because the reading
  favours the framework" (SHARED §3) are §A.31 method notes. They are outside §A.32's `papers/` scope, so no change is
  required, but they are the only self-referential phrasing found.
- DISPOSITIONS-r4 line 24 records the summary-scope check as made against SHARED §5 only. N2–N8 lie outside §5.

***

## r3 blockers and nits

| r3 item | present in r4 | correct | notes |
| --- | --- | --- | --- |
| B1 (§9 (L′)/(R) column (ii)) | yes (SHARED:665; QX-6 A6.1 header and the paragraph after it) | yes | (ii) "no"; the Main:403-406 and :414 readings are correct; the Main:362 quote is removed from the row |
| B2 (Q4-D2 scope) | yes (Q4-D2, Q4-O6) | yes | witness symplectic, `K₃ = 2` (p8 (5)). Residue in the `A_4` arm prose: N7 |
| B3 (tensor order) | yes (A4.1(c), Q4-P4) | yes | p7 re-run equals its `.out`. p8 (1) reproduces it independently, in the Schrödinger picture with Lüders projectors and in the Heisenberg form, with equal results. The reading mediator ⊗ carrier gives `−cos β` (p8 (1e)) |
| N1 (Q6-P2 status) | yes | yes | "unreviewed" tags replaced; the not-on-`main` and not-kernel-checked note is present |
| N2 (standing on computation) | yes | yes | owner answer quoted correctly. "P1–P6" is stale: N9 |
| N3 (X layer) | yes | partly | rule and tags present. Residual D labels: N8. Single-probe entries: N12 |
| N4 (Lüders proof) | yes (QX-4 §2; Q4-P8 [A]) | yes | identity `P₊AP₊ − P₋AP₋ = ½{Q, A}` and `3 − 2K₃ ≥ 0` re-derived by hand |
| N5 (pure stabilizer) | yes | yes | creates the inconsistency N2 with the "only at (a) and (b)" sentence |
| N6 (Q4-D1) | yes | yes in substance | mixture `3/2`, NSIT at `t₂` in every branch (p8 (5)); INM form open (Q4-O8). Wording: N1 |
| N7 (Q4-D6) | yes | yes | comparator-protocol claim; OI value open (Q4-O2) |
| N8 (dyadic) | yes | yes, except item 5 | the writer correctly rejected r3's example: `5/8 + 5/8 − 9/128 = 151/128 > 1`. The replacement law is valid. Item 5's new necessity sentence: B2 |
| N9 (`I_ont`) | yes | yes | `(S − 2)² ≤ 32 ln 2 · I_ont` follows from Main:421; 0.0309 at `2√2` |
| N10 (TLM attribution) | yes (QX-6 §1, Q6-P7, §11) | yes | |
| N11 (SA-1(a), M15) | yes | yes | |
| N12 (matrix cells) | yes (M16, M20; §5 QX-4 and QX-6) | yes | M12 × QX-6 still unqualified: N3 |
| N13 (ledger completeness) | yes (Q4-P16–P18, Q3-P10, Q4-O4) | yes | Q4-P16 and Q4-P17 checked by hand |
| N14 (`NCONS_global` convention) | yes (A3.1(c), Q3-P6a) | yes | argument correct; counts 6, 48, 8 and 64, with 0 affine, reproduced (p8 (8)) |
| N15 (narration) | yes | yes | scan of the four specs: no narration. "no longer than" (QX-6:321) is mathematical |
| N16 (owner records) | yes | yes | author and times match the comments |
| N17 (line references) | yes | yes | DISPOSITIONS-r3 unchanged (`711bfda0…`) |

## Owner requirements (#1210 c.6739286623; c.6739311717)

| requirement | status | basis |
| --- | --- | --- |
| **Bell locality:** design assumptions, proof conditional | **met; two summary sites to qualify (N3), one type column (N11)** | (L′) and (R) are classed as design assumptions of the Bell test, not consequences of OI, in A6.1's header, R6.2, §9, Q6-P2, Q6-P10, §2's first row, `A_6`, §8 item 2 and SHARED §§3, 4, 5 and 8.4. The proof was re-read and is unchanged from r3; p8 (9) rebuilds a one-tick counterexample to the single-graph form. Remark: (R) is stated on `G_B`, which the dynamics fixes. It is therefore an assumption the design makes about the dynamics, not one the design can guarantee. The specs say this correctly, in that H-Bell is a failure of (R) |
| **Evidence ledger:** membership; narrower claim open | **not met (B1); rule wording (N1)** | 10 of the 11 membership lines are valid as stated (table below). Q4-D1 and Q4-D2 keep the narrower claims open (Q4-O8, Q4-O6). Q4-D3 shows membership only in affine maps, not necessarily symplectic. The narrower affine-symplectic claim holds and is not listed |
| **Leggett–Garg:** target mode, exact configuration | **met** | Target: carrier (`CNOT_{m→c}`); `H` on the mediator; order carrier ⊗ mediator. `(C₁₂, C₂₃, C₁₃) = (cos β, sin β, 0)`, `K₃ = cos β + sin β`, `√2` at `π/4` and `7/5` at `(4/5, 3/5)`, for `G1` and for `G2`. The other placement gives `−cos β` and `0`. `G1` and `G2` are unitary and Clifford. Checked by p7 (re-run) and by p8 (1), independently and in two pictures |
| **Re-read of the whole r4, including the 17 nits** | **done** | new errors from the r4 edits: B2 and N2. Earlier errors not caught in r3: B1 and N4–N7 |
| **Summary and dependency-table scope** | **not met (8 mismatches below)** | |

## Membership check of every disproved entry

| entry | refuted class (defining conditions) | counterexample satisfies each? | verdict |
| --- | --- | --- | --- |
| Q3-D1 | routing by an unknown bit into one of two cells; own-cell reads; number conserved on the ready support; "needs non-affine" | `L` is a bijection; the ready support maps to `(0,1,0)` and `(1,0,1)`; one field excitation in `c₁` or `c₂`; weight conserved under either weight convention; linear (p8 (8)) | **valid** |
| Q4-D1 (restated) | without (H2); reaching `K₃ = 3/2`; the claim is that a `t₂` read changing `Q₃`'s law is needed | ordinary kicking `t₁` read, so (H2) fails; (H1) and (H4) hold; mixture `K₃ = 3/2`; `P(z₃)` is the same with and without the `t₂` read in each branch and in the mixture; the `z`-row of `G` has no `x` term (p8 (5)) | **valid**. The INM form is open (Q4-O8). Header wording: N1 |
| Q4-D2 (restated) | affine-symplectic `G` with translations, two modes, sharp supplies admitted, A4.1 read model | invertible; symplectic for `(z, x)`, `(v, w)`; sharp mediator `(0, 0)`; carrier `X⁺`; `K₃ = 2` (p8 (5)) | **valid**. `A_4` open (Q4-O6) |
| Q4-D3 | "the affine class" | linear, but **not symplectic** (p8 (6)) | **valid only for affine maps, not necessarily symplectic. B1** |
| Q4-D4 | quantum Leggett–Garg protocols with dichotomic reads; "3/2 is the quantum maximum" | both instruments are trace-preserving; their effects are the `Z` projectors; `G = X` is unitary; `C_ij` from two-read runs; `K₃ = 6w − 3` (p8 (3)) | **valid** |
| Q4-D5 | affine and Clifford classes, any preparation; "correlators in `{0, ±1}`" | `CNOT` is Clifford; Lüders `Z`; `C₁₂ = cos 2θ` (p8 (2)) | **valid** |
| Q4-D6 | comparator protocol; more than one mode; preparations unrestricted; "`K₃ > 1` needs non-Clifford `G`" | Lüders reads of the carrier's `Z`; `G1` and `G2` Clifford and unitary; two modes; the non-stabilizer preparation is admitted; `K₃ = √2` and `7/5` (p7; p8 (1)) | **valid** |
| Q4-D7 | a preparation and a `t₂` read not commuting with the evolved `Q₃`; "NSIT fails" | maximally mixed state; Lüders `X`; `G = I`; `P(z₃ = +1) = 1/2` both ways (p8 (4)) | **valid** |
| Q6-D1 | (D); one graph `G` containing every tick's graph; (L); single-graph (R); (MI); "`|S| ≤ 2`" | independent rebuild with `op_B: b₂ += y`, `φ: a₂ += b₂`, `op_A: a₁ += x·a₂`. Bijective for every setting; (L) holds; `d_G(B, R_A) = 1 > 0`, `d_G(A, R_B) = ∞`; `λ` uniform; `S = 4`; (L′) fails (p8 (9)) | **valid** |
| Q6-D2 | `X/Z` reads only; "a GHZ-type contradiction needs `Y`" | triangle state: `+1, +1, +1, −1`; local maximum 2 (p8 (10)) | **valid** |
| Q6-D3 | GHZ-1's state; `X/Z` reads; "an `X/Z` contradiction exists" | the nonzero `X/Z` strings are exactly `XXX`, `ZZI`, `IZZ` and `ZIZ`, all `+1`; the assignment `+1` satisfies all of them (p8 (10)) | **valid** |

## Summary-scope mismatches

Every conclusion in each spec's summary-type sections was compared with its supporting entry: the witness tables, the
obstacle lists (§7 and §8), the ladder mappings, the derivation titles, the decision trees, SHARED §§1–5, the §2
matrix, the §4 tensions and controls, and the §8.4 headline lists.

| # | site | as stated | supporting result's scope and status | fix |
| --- | --- | --- | --- | --- |
| 1 | QX-3 §7 item 5 | intermediate `α` "need non-uniform laws or mixtures" | A3.1(a) needs uniform-coset laws **and** affine functionals | B2 |
| 2 | QX-4 A4.1(c); §7 item 2 | `K₃ ≤ 1` "established only at" (a) and (b) | Q4-P3 [A]: `K₃ ≤ 1` for Clifford `G` with pure stabilizer preparations, and for their mixtures, at any number of modes | N2 |
| 3 | QX-6 A6.2 title; SHARED §2 M12 × QX-6 | "not sufficient" | Q6-P10 [A], conditional on (L′) and (R) | N3 |
| 4 | SHARED §3 "Counting" | "needs, at minimum …", unconditional | conditional on A6.1 [A], (MI) and the design assumptions; stabilizer preparations; D drafts. No §8 entry | N4 |
| 5 | QX-3 §2 Consequence; §7 item 7; SHARED §5 QX-3 | W2 excludes "classical fields only" | the W2 row also excludes phaseless particle models | N5 |
| 6 | SHARED T2; QX-4 A4.4 Consequence | "must keep an outcome-independent kick" | Q4-P6: `K_null ≠ id` only | N6 |
| 7 | QX-4 §5 `A_4` | "`K₃ ≤ 1` is not expected" | `A_4`'s value is open (Q4-O6) | N7 |
| 8 | QX-4 A4.1(b) label | [D] | Q4-P2 [X, proved, computation-supported] | N8 |

Checked and consistent:
- SHARED §1 rows M2, M14, M15 and M16;
- the §2 cells M3, M12 and M13 × QX-4, M14, M16 and M20;
- §3 "Cross-wing dynamics" and "Epistemic restriction";
- §4 T6 and T9 and the controls list;
- §5 QX-4 and QX-6;
- §8.4;
- QX-4 §2's witness table, §7 items 3, 5 and 7, and §8;
- QX-6 §2's witness table, §3.2, §7, §8 items 2 and 6, and §9;
- QX-3 R3.6, §7 item 3 and §8.

## Register and authorization

- **§A.32 and §A.33.**
  - Caps scan: every all-caps token of four or more letters is an identifier (MECH-OPEN, NCONS, NSIT, OICORE, file
    names) or a quoted record status ("STOP").
  - History-phrase scan ("no longer", "now", "formerly", "withdrawn", "corrected", "unreviewed", "review N"): no
    narration. The hits are "unreviewed unless stated", a layer definition, and a mathematical "no longer than".
  - Reader-instruction phrases: none. §A.31 method notes: see the optional nit.
- **Authorization.** No text implies a D19–D23 decision, a freeze, a dispatch or construction. QX-3 §0 lists
  construction, computation on any OI mechanism, frozen criteria and execution as not authorized, and every rule is
  marked as an outline, not frozen. DISPOSITIONS-r4 line 9 keeps D19–D23 separate.

## Probes

| probe | sha256 | result |
| --- | --- | --- |
| `p7_r4_lg_order.py` (writer; re-run) | `6eb7f784164e178f…` | output identical to `p7_r4_lg_order.out`; exit 0 |
| `p8_r4rev_membership.py` (this review; imports no earlier probe; generic objects only) | `810131733cd34180…` | 47 of 47 pass. Exact (sympy or `Fraction`), except (7), which is numerical with an integrality tolerance and is evidence only. Output in `p8_r4rev_membership.out` (`a511a94c3a1ca4e1…`) |

p8's sections:
1. The LG target-mode configurations, both placements of `H` and the mediator ⊗ carrier reading, in two pictures.
2. Q4-D5.
3. Q4-D4's instruments.
4. Q4-D7.
5. The `F_2` witness: symplecticity, the sharp, environment and mixture values, and NSIT at `t₂`.
6. Q4-D3: the copy coupling is not symplectic; exhaustive over `Sp(4, F_2)` with translations and over all affine
   bijections.
7. Q4-P3 over 11,520 Cliffords × 60 stabilizer states.
8. QX-3's counts and Q3-P11.
9. The Q6-D1 rebuild.
10. GHZ-1 and GHZ-2.
