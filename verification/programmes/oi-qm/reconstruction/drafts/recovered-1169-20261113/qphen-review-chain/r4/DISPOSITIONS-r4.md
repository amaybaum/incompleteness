# QPHEN Phase 1 r4: dispositions of `review/REVIEW-PHASE1-r3.md` (`448614ea…`) and of the owner's r4 requirements

## Scope and standing

- Paper only and model-written. There are no repository, git or GitHub writes; Issue comments were read only.
- No computation is run on any OI mechanism. The one new check, `review/probes/p7_r4_lg_order.py`, is an exact check
  of a paper claim on generic objects ("Allowed: generic checks", #1210 c.6739250392, owner, 2026-11-09). It imports
  no earlier probe.
- Q-C2-1's D19–D23 remain separate. No freeze, dispatch or implementation approval follows from this revision.
- **Inputs.**
  - The r3 review, sha256 `448614ea403a6d41517aacd155bb6b973e4fc2c7a342b65324bf6226a4c3e5ba`, and its probes
    `p6_r3rev_*.py`.
  - Owner records, read at their source:
    - #1210 c.6738145827 (amaybaum, 2026-11-09T10:48:39Z);
    - c.6738337450 (10:58:24Z);
    - c.6738866690 (11:25:06Z);
    - c.6739250392 (11:45:26Z);
    - the authorization c.6736966265 (09:45:12Z).
  - The owner's three r4 requirements (Bell locality, membership of counterexamples, Leggett–Garg target mode),
    recorded at #1210 c.6739286623 (amaybaum, 2026-11-09T11:47:25Z) and quoted in QX-3 §0.
  - `R4-REVIEW-ADDENDA.txt` (sha256 `7aa1b1ad…`, 11:48). This is the coordinator's note for the r4 reviewer prompt.
    It was not written by this writer, is treated as data and is left untouched. Its owner point is that every
    conclusion in a summary or dependency table has the same scope and status as its supporting proof. That point
    was checked against SHARED §5's QX-3, QX-4 and QX-6 rows, which carry the stabilizer and (L′)/(R) qualifiers.
- **The r3 texts** are copied unchanged into `r3/`:

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `4ea39322…` |
  | `QX4-INCOMPATIBILITY-LG.md` | `866a6f2a…` |
  | `QX6-BELL-CHSH.md` | `04882cc2…` |
  | `SHARED-MECHANISM.md` | `6537031a…` |
  | `DISPOSITIONS-r3.md` | `711bfda0…` |

  These match the hashes the r3 review lists. `DISPOSITIONS-r3.md` is a record and is not edited.

## The new check

`p7_r4_lg_order.py` (exact, sympy). The configuration is:
- tensor order carrier ⊗ mediator, basis `|c m⟩`;
- `G1 = (I ⊗ H)·CNOT_{m→c}`, in which the `CNOT` has the mediator as control and the carrier as target, and `H` then
  acts on the mediator;
- `G2 = (I ⊗ H)·SWAP·CNOT_{m→c}`;
- Lüders reads of `Z` on the carrier.

Results:
- `G1` and `G2` are unitary and Clifford.
- (a) `G1`, carrier `|+⟩`, mediator `(sin β, 0, cos β)`: `(C₁₂, C₂₃, C₁₃) = (cos β, sin β, 0)`, so
  `K₃ = cos β + sin β`, which is `√2` at `π/4` and `7/5` at `(4/5, 3/5)`.
- (b) `G2`, carrier `(sin β, 0, cos β)`, mediator `|0⟩`: the same.
- (c) With `H` on the carrier:
  - `(H ⊗ I)·CNOT_{m→c}` gives `(0, 0, cos β)` and `K₃ = −cos β`;
  - `(H ⊗ I)·SWAP·CNOT_{m→c}` gives `K₃ = 0`.

  This agrees with `p6_r3rev_lg.py` (1).

## Blockers

| finding | change made (r4) |
| --- | --- |
| **B1** (§9 "(L′) and (R)", column (ii)) | **SHARED §9.** Column (ii) now reads "no. These are design assumptions of the Bell test: own-wing settings and separation. They are not consequences of OI. OI's chosen branch (a) gives up Main's (ii) and (iii), of which (L′) and (R) are the generalizations (Main:403-406, :414), and H-Bell's preparation-indexed long edges are a failure of (R) (QX-6 §3.2)". The standing column reads "design assumptions (protocol). A6.1 is proved conditional on them". The Main:362 quotation is removed from this row |
| **B2** (Q4-D2's scope) | **SHARED §8 Q4-D2** is restated as "Every affine-symplectic `G` with translations on two modes, with sharp supplies admitted, under A4.1's read model, gives `K₃ ≤ 1`", with the witness and a membership line. `A_4`'s own value is listed as open (Q4-O6) |
| **B3** (tensor order) | **QX-4 A4.1(c)** and **SHARED §8 Q4-P4** state the configuration: tensor order carrier ⊗ mediator, `CNOT` control mediator and target carrier, `H` on the mediator, and the same for the SWAP variant. They give the other placement's values, `K₃ = −cos β` and `K₃ = 0`. The probe `p7_r4_lg_order.py` is cited |

## Nits

| finding | change made (r4) |
| --- | --- |
| **N1** (Q6-P2's status) | **SHARED §8 Q6-P2** now reads "[A: complete paper proof …; independently reviewed in `review/REVIEW-PHASE1-r3.md` (`448614ea…`); exact checks P5-A61 and `p6_r3rev_a61.py`]", conditional on (D), (L′), (R) and (MI). The conditional sentence about the review is removed, and a note is added that the lemma is a paper derivation, not on `main` and not kernel-checked. **The "unreviewed" tags are replaced** in QX-6 A6.1's header and in SHARED §3. The A-layer definition reads "unreviewed unless stated" (QX-3 §0; SHARED §8 rules) |
| **N2** (standing: computation) | **The four specs' §0** now say: "no computation on any proposed OI mechanism". They also say that exact checks of paper claims on generic mathematical objects are allowed when labelled as such ("Allowed: generic checks", #1210 c.6739250392, owner, 2026-11-09), that the cited probes P1–P6 are of that kind, and that results supported only by such a check are marked computation-supported. In QX-3 §0, the not-authorized list keeps mechanism construction, frozen criteria and execution, and reads "computation on any proposed OI mechanism" |
| **N3** (X layer) | **SHARED §8 rules.** An X computation is a re-runnable generic probe off `main`, counted as X at its scope when independently reproduced. An entry whose only support is such a computation is marked **computation-supported**. The tag is added to Q3-P4, the Q3-P6 and Q3-P6a counts, Q4-P2, Q4-P4, Q4-P7, Q4-P9, Q4-P15 and Q6-P6. Each X entry names the reproducing probe. QX-3 §0 gains the X layer, and D no longer lists the probes. QX-4 §0 lists X |
| **N4** (Lüders bound proof) | **QX-4 §2.** The two-line proof is added: the identity `P₊AP₊ − P₋AP₋ = ½{Q, A}`, so `C_ij = ½⟨{Q_i, Q_j}⟩`; then `0 ≤ ⟨(Q₁ − Q₂ + Q₃)²⟩ = 3 − 2K₃`. The proof is cited to `p6_r3rev_lg.py` (3), with Budroni–Emary kept as L. **SHARED Q4-P8** is now [A] |
| **N5** (pure stabilizer) | **QX-4 A4.1(c)** reads "pure stabilizer preparations", and adds, as a separate bullet after the consequence, that for convex mixtures the correlators need not be integers but `K₃ ≤ 1` still holds by linearity. **SHARED Q4-P3** gets the same |
| **N6** (Q4-D1) | **SHARED Q4-D1.** The refuted claim is narrowed to the class the counterexample belongs to: without (H2), reaching the comparator value `3/2` needs a `t₂` read that changes the law of `Q₃`. The counterexample is the review's mixture, weight `3/4` on the sharp mediator, with `K₃ = 3/2` and the `t₂` kick never entering `z₃` (`p6_r3rev_lg.py` (6)). The membership line is given. The INM-detector form, `K_null = id`, is not shown to contain the counterexample, because INM is not posable in the encoded setting, so it is open (new Q4-O8). **Q4-P7** gives the environment value 0 and the mixture |
| **N7** (Q4-D6) | **SHARED Q4-D6** is restated as a claim about the comparator protocol, with the OI-value statement open (Q4-O2). **QX-4 A4.2** now reads "the comparator protocol exceeds 1 with a Clifford `G` … The OI value under C-NONSTABILIZER is not predicted" |
| **N8** (dyadic) | **"Rational (dyadic at `q = 2` without conditioning)"** is used in QX-3 R3.2, SHARED M2, T6, QX-6 A6.3, SHARED Q6-P9, §8.4 and the §9 N2 row. **QX-3 §7 item 5** gets the correct reason: A3.1(a) gives `α ∈ {0, 1, 2}`. The review's example `P_A = P_B = 5/8`, `P_AB = 9/128` is not a valid law, since `P(a = 1 or b = 1) = 151/128 > 1`. The example used is the valid dyadic law with cells `9, 151, 71, 25` out of 256 (`P_A = 5/8`, `P_B = 5/16`, `P_AB = 9/256`), which gives `α = 9/50`, checked exactly. It is ledger entry Q3-P11 |
| **N9** (`I_ont`) | **QX-6 §2** now reads "`I_ont ≥ (S − 2)²/(32 ln 2)` bits for the observed `S` (Main:418-421), which is `0.0309` bits at `S = 2√2`". **SHARED Q6-P8** adds the equivalent form |
| **N10** (TLM attribution) | **QX-6 §1** gives necessity as Landau 1987, and sufficiency as Landau, Found. Phys. 18, 449 (1988), and Masanes (2003), all L, not read first-hand. **QX-6 §11 and SHARED Q6-P7** are updated to match |
| **N11** (SA-1(a), M15) | **§9 SA-1(a), column (ii)**: "yes, conditional on Substratum (A4)–(A5), with (A5)'s restriction to linear 'imposed' and (A5) 'partly derived' (Substratum:98, :100)". **The M15 row** reads "conditional … on the same condition as the SA-1(a) row; the support is a W record" |
| **N12** (matrix cells) | **SHARED §2.** M16 × QX-4 now reads "? (tested in the INM variant under H1, H2, H4; QM-only, §9)". M20 × QX-6 now reads "R (no-signalling); ? (Tsirelson half: tested; QM-only, §9)". **SHARED §5's QX-4 row** is matched: the INM variant needs M14, and M16 only for matching the comparator protocol, as a hypothesis under test. **SHARED §5's QX-6 row** gives "not sufficient" for constructions satisfying A6.1's hypotheses, including (L′) and (R), under the owner's Bell requirement |
| **N13** (ledger completeness) | **New ledger entries:** Q4-P16 (classical mixing, `η_Z + η_X ≤ 1`, A); Q4-P17 (classical wave, `V² + D² = 1`, A, elementary); Q4-P18 (A4.5, two applications of `G`, A), with its C-SIZE-DEPENDENT statement in Q4-O4 (D-sourced); Q3-P10 (W1 and W2 need only stabilizer or classical-reversible operations, A) |
| **N14** (`NCONS_global` convention) | **QX-3 A3.1(c)** states that weight counts every coordinate, `s` included, and adds the field-only case. An affine field map that preserves field weight for both values of `s` is the identity or the swap, independent of `s`. The 64 field-weight-preserving routing bijections are all non-affine (`p6_r3rev_qx3.py` (c); computation-supported). This is ledger entry Q3-P6a |
| **N15** (revision narration) | **Removed:** QX-6 §11's "it is no longer cited for the GHZ claim", together with the Coecke–Edwards–Spekkens entry, which nothing cites; QX-3 §0's "(review N9)"; and Q6-P2's conditional sentence (N1). The specs' §0 "Revisions" lines are reduced to a pointer, "Earlier texts are kept under `r1/`, `r2/` and `r3/`. The revision record is `DISPOSITIONS-r4.md`". A scan of the four specs for "no longer", "now", "formerly", "withdrawn", "corrected", "unreviewed" and "review N" finds no narration left. Remaining hits are identifiers, or "no longer than" used mathematically |
| **N16** (owner records) | **QX-3 §0** quotes the four records with author and time: c.6738145827, c.6738337450, c.6738866690 and c.6739250392. SHARED §0 points there. **SHARED §9** cites decision O1. **QX-6 §11** quotes decision O2 for Q6-5. Reference rows are added to QX-3 §10 and SHARED §7. DISPOSITIONS-r3's O3 is resolved (below) |
| **N17** (stale line references) | `DISPOSITIONS-r3.md` is a record and is left unchanged. This file cites sections and entry identifiers, not line numbers |

## The owner's r4 requirements (#1210 c.6739286623)

| requirement | change made (r4) |
| --- | --- |
| **Bell locality.** Locality conditions are design assumptions, and the proof is conditional on them | **QX-6 A6.1's header** reads "Proved conditional on (D), (L′), (R) and (MI)", followed by a paragraph classing (L′) and (R) as design assumptions of the Bell test, not consequences of OI (Main:403-406, :414; §3.2). **QX-6 R6.2's type** is "design assumption of the Bell test (A6.1 (R)), not a consequence of OI". **Where A6.1 is cited as proved, the condition is stated:** QX-6 §2's first witness row, `A_6`, §8 item 2, SHARED §3, SHARED §4 controls, SHARED §8 Q6-P2, Q6-P10 and §8.4, and §9 (B1) |
| **Evidence ledger.** Show that each counterexample belongs to the class it refutes; keep narrower claims open | **SHARED §8 rules** require a membership line, or narrowing. **All 11 disproved entries** carry one: Q3-D1, Q4-D1 to Q4-D7, and Q6-D1 to Q6-D3. **Narrowed:** Q4-D1, to ordinary reads without (H2), with the INM form open as Q4-O8 (N6); and Q4-D2, to the generic two-mode class, with `A_4` open as Q4-O6 (B2). Q4-D6's claim is stated for the comparator protocol, with OI's value open as Q4-O2 (N7) |
| **Leggett–Garg.** Specify the gate's target mode, verify the exact configuration, and report the other order separately | B3 above. The gate's target mode is the carrier (`CNOT_{m→c}`), and `H` acts on the mediator. `p7_r4_lg_order.py` verifies `K₃ = cos β + sin β` exactly for that configuration and reports the other placement of `H` separately (`−cos β`; `0` for the SWAP variant). Under the owner's r3 Leggett–Garg criterion (c.6738145827, "Qualify every comparison by the applicable measurement protocol"), QX-4 §2 defines "QM-matching" as a value in the comparator protocol's range `(1, 3/2]`, and R4.10 now names the comparator protocol in place of "QM" |
| **N2 answer** (c.6739250392) | Applied as in N2 and N3 above |

## Owner questions from DISPOSITIONS-r3: resolved

- **O1.** Resolved: approved, #1210 c.6738866690 (amaybaum, 2026-11-09T11:25:06Z), confirmed at c.6739250392 ("Yes
  to both"). SA-1(c), null-result invasiveness and Tsirelson soundness are carried as hypotheses under test. SHARED
  §9 cites the decision.
- **O2.** Resolved: approved, same records. Q6-5 is the identifier of the `⊥`-rule question. QX-6 §11 quotes the
  decision.
- **O3.** Resolved: the r3 requirements are recorded at #1210 c.6738145827 and c.6738337450, quoted with author and
  time in QX-3 §0.

## Changes not traced to a review finding

Each change below is traced to the instruction to write r4 in place or to an owner requirement. None is restyling,
and nothing new beyond the findings is added.
1. Titles change from "(draft r3)" to "(draft r4)", and the cross-references "§0 (r3)" and "(r3) specifications"
   change to r4.
2. The §0 "Revisions" pointers name `r3/` and `DISPOSITIONS-r4.md` (N15).
3. New reference-table rows: the r3 review and its probes (QX-3 §10, QX-4 §10, QX-6 §11, SHARED §7); `p7` (QX-4 §10,
   SHARED §7); the owner records (QX-3 §10, QX-6 §11, SHARED §7). These follow §A.42 item 8 tracing of new citations.
4. Q4-O1 records the review's `m = 3` random sample (`p6_r3rev_aw3.py`) as not a proof, so that the X/sample
   distinction of N3 is kept.

## Refusals and deviations

- **None refused.**
- **N8.** The review's example is replaced by a valid one, for the reason given.
- **N6 and owner requirement 2.** Q4-D1's INM-detector form could not be shown to contain the counterexample. It is
  narrowed, and the INM form is open (Q4-O8).

## r4 file hashes (sha256)

| file | sha256 |
| --- | --- |
| `QX3-ANTIBUNCHING.md` | `f372cef7d3baad57cb4cddd72a710bb1077a1235299fd34283fb5ca29b6c5282` |
| `QX4-INCOMPATIBILITY-LG.md` | `2765e6f7cb06e4d6bbd60645616abd70588ca8b739235181845fed3cde6f97c4` |
| `QX6-BELL-CHSH.md` | `5c7ab0cb6efce8e33b23daad29fd20076e6cceeb1fe83d54e11b68c6d6ef774a` |
| `SHARED-MECHANISM.md` | `23ec1ef19be8b2dd4aa77d59926853fd00a125ee552746db14d83203b366fd11` |
| `review/probes/p7_r4_lg_order.py` | `6eb7f784164e178f9a29a4b9dc010c0def009f642afa7aae3425fcf89f596d9a` |
