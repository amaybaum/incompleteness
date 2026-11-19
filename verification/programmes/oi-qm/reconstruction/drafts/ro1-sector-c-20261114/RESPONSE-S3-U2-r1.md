# Response to the review of S3-U2-r1

**Review.** `REVIEW-S3-U2-r1.md`, on PR #1294 at `e681f624` (blob `3a6c599c`): ACCEPT WITH CHANGES.
It has nine required findings, R1–R9, and four optional items, O1–O4.

**Revision.** `S3-U2-r2.md` applies every required finding and every optional item. r1 (`S3-U2-r1.md`,
blob `08afa36b0f0af60ef27c09f055e890fd1a14cdc0`) is left unchanged. No verdict moves between
*available* and *not available*.

**Owner records read at the same time.**
- #1169 c.6891338304, the amended AC-1. It is unchanged and still applied.
- #1169 c.6891511297, which records S-L3 and CC4, CC5 and CC7 as verified at narrower scopes. No U2
  verdict uses those items, so r2 cites the record and changes nothing for it.

Each finding was checked at its source before it was applied.

| # | Finding | Disposition | Where in r2 |
|---|---|---|---|
| R1 | F-1 overstated: `μ_PR`'s setting law is U2's own completion; SPEC:468's conclusion holds for the stated tuple and at the derived level; the enlargement can be a completion of `μ` alone and is still needed; NEW is not justified | **Accepted.** Checked against SEL-EXCL-1 ll. 17 and 44: "freely chosen" labels, and no setting law. U1:390–391 makes the settings derived under μ-G. F-1 now states four things: the reason fails at both levels; the conclusion stands for the uncompleted tuple and at the derived level; SPEC:446 stays true; the enlargement can be a `μ`-level completion, and it is still needed. CP-1 is "available relative to `μ_PR`, an assumed initial law". F-1 is reclassified as ELABORATING. F-2 is narrowed to the completed tuple | header; §1.2; §2.1 "Bearing on SPEC §7.2"; §7; §9 F-1, F-2; §11.2 |
| R2 | `μ_PR` is MP-0a only if the setting law is uniform | **Accepted.** The setting law is fixed as uniform on `{0,1}²`. That meets U1:308–309, and the MP-0a claim then holds at OA1:359–361 [M-r]. A non-uniform law is named as a different completion, with its own admissibility question (ledger Q8) | §1.2 |
| R3 | L-1's clause "or written from such a factor" is not covered by the proof | **Accepted; restricted, not repaired.** Re-derived: for a non-binary seed, the trivial-or-discrete step fails, and seeds in `λ` break (h3). L-1 now carries (h1)–(h4), with settings as binary factors of the initial configuration, unchanged up to the use or copied there injectively. The seed-written case is named as not covered, along with the cases without S5, the flagged realizations and the extension operations. The repair the review sketches would need an S5-type condition on the seeds. It is not added, because it would extend a new derivation further (R9) | §4.1 |
| R4 | "Not in `Γ_exe`" is an outcome state U1 does not define, yet it is counted under SNR-1 | **Accepted.** The state is mapped onto U1's *not available* at the tuple's scope. A table names each row's disproved input and its ground, and every cell carries its standing [A-inf on OFF]. The outcome vocabulary now says r2 uses no other state | outcome vocabulary; §2.2; §3; §11.1 |
| R5 | (a) Bob holds `b = r` at `y = 0`, so the CP-6 sentence is false; (b) "None of them is a declaration" overstates | **Accepted.** (a) Bob's `b = r` at `y = 0` is added to the available sub-reads. The negative is restated as Bob reading `r` in a run that also uses `y = 1`, which is not available by the declared `Obs` (`r` hidden, and Bob has one register). (b) Each negative is attributed to `T`'s algebra or the tuple's `S`, to AD-1(f) applied to the native order 2, or to the declared `Obs`. SEL-EXCL-1 calls the last "assumed rather than OI-derived" (l. 150). The attribution is made under reading (i) of O11. r2 also states that `φ = T` at every tick is U2's reading, while SEL-EXCL-1 applies `T` "once" per clocked use (l. 44) | §1.2; §2.2; §3 CP-6; §11.1 |
| R6 | The AC-1 verdicts on removing setting–setting I-sel need the same scope in both halves | **Accepted.** Both halves now read: fails under (h1)–(h4), conditionally on L-1's review; open for seed-written settings, for realizations without S5 (Main:416–423), for flagged realizations, and for extension operations typed into `φ` or `Γ`. §11.2 repeats the scope | §6.1; §6.2; §11.2 |
| R7 | The `Θ` condition is applied to M-PR5 but not to R-lin | **Accepted, applied alike rather than justified as an asymmetry.** R-lin's conflict with E2 now holds only if `Θ` identifies the performed tests' separated wings with programs whose wings lie outside each other's cone, and S5 holds. The optional datum note is added: M-PR5's miss also needs "no observed excess above `2√2`", which the corpus carries only as a falsification condition (Substratum:481) | §6.2; §11.2 |
| R8 | The MP-0a claim, the D2 citation and the labels in §11.1 | **Accepted.** MP-0a: see R2. R-lin's blanks now cite heralded visible blanks at the D3 cost (OA1:328, :156–160), whose herald must be retained to `t_c` and is unsourced, and on K1, MR★:642 [NP]. D2 is no longer cited for "no ready region". Every cell of §11.1 is labelled. The negatives on QR-1, CP-1, CP-7 and CP-8 on R-lin are marked as D5 [M-r] read through U1's factor-set extension [A-inf] (U1:435–440). The SNR-1 counting note now says that such negatives, and those resting on L-1, count only once verified | §2.1 s2, s4; §3; §4.2; §11.1 |
| R9 | L-1 is a new derivation and falls under PLAN:871's stop | **Accepted; routed.** L-1 is labelled a proposed lemma, [A-inf], and routed to #914 O-INS ("Composites and Bell structure") and #1060. Every verdict that rests on it is marked conditional on its review. The text explains why it is stated at all: U1's AW-3 is an AC-1 question that U2's report must address. The match with Main:404–412 is given as context, not as a reason to treat L-1 as established | §4.1; §5; §8.3; §9 L-1 |
| O1 | AW-U2-3 also uses the blank `B₀ = 0` and a budget of at least 2; Bob's setting change alone suffices | **Applied.** Re-derived: with `x₁ = x₂ = x`, `y: 0 → 1` and `B₀ = 0`, `B₂ = x` | §2.5; §5; §7; §9 AW-U2-3 |
| O2 | The retention flag is vacuous | **Applied.** The flag is stated as vacuous because no coverage result is positive. r2 also notes that for CP-3 in reading (g) the two criteria coincide only because that reading folds the retention between uses into one tick | §8.1; §11.2 |
| O3 | "would meet" for the response-table tuple | **Applied.** It now reads "may meet …; not constructed or checked" | §4.2 |
| O4 | Ground CP-5's "not absorbable" argument in S-A6 and SEL-DISC-1 l. 97 | **Applied** | §2.6 |

**Checks made for r2.**
- The text rules were applied by grep: no forbidden word or local path.
- Line anchors added in r2 were re-read at their objects: SEL-EXCL-1 ll. 17, 44 and 150; SEL-DISC-1
  l. 97; OA1:156–160, :328 and :359–361; MR★:642; U1:390–391 and :435–440; Substratum:123 and :481.
- Nothing is computed, committed or pushed.
