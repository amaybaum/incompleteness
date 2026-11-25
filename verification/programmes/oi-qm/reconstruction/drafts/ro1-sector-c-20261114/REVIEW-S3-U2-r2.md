# Confirmation review of S3-U2-r2 against REVIEW-S3-U2-r1 (independent, non-author)

**Objects.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U2-r2.md`
and `RESPONSE-S3-U2-r1.md`, at PR #1294 head `3fb9a6be09be623a8bac35fb056dfbb41b258e4f`. The r1 file
is unchanged at that head. Corpus at `origin/main` `75cc5100`. The new owner record cited by r2,
#1169 c.6891511297 (`amaybaum`, 2026-11-15T08:11:04Z), was read via the GitHub API, and r2's
quotations of it are accurate.

**Reviewer.** Claude, non-author of U2 and author of the r1 review. Read-only.

## Verdict: ACCEPT WITH CHANGES

All nine required findings and all four optional items of the r1 review are resolved. Two new
required changes are small and textual. One is a negative corpus claim about Substratum:481 that the
corpus does not support (N1). The other is a residual of R4 in two table columns (N2). Once both are
made (an r3, or a two-line erratum noted in the owner's acceptance), U2 is ready for owner
acceptance. Neither change moves a verdict.

## 1. Resolution of the r1 findings

| r1 # | Resolved? | Where checked in r2 |
|---|---|---|
| R1 | **Yes.** SPEC:468's reason fails at both levels. Its conclusion stands for the uncompleted tuple and at the derived level. SPEC:446 stays true. The enlargement can be a `μ`-level completion and is still needed. CP-1 is "available relative to `μ_PR`, an assumed initial law", with the `μ`-data listed and stated as non-producers (U1:201–202). F-1 is ELABORATING. F-2 is narrowed to the completed tuple, and §7 states that it does not hold for the uncompleted tuple or at the derived level | §1.2; §2.1 "Bearing on SPEC §7.2"; §7; §9 |
| R2 | **Yes.** The setting law is uniform on `{0,1}²`, which matches MP-0a (OA1:359–361). A non-uniform law is named as a different completion under ledger Q8 | §1.2 |
| R3 | **Yes.** Hypotheses (h1)–(h4) are explicit. The proof is unchanged and still correct under them. Seed-written settings, the cases without S5, the flagged realizations and the extension operations are named as not covered. Choosing restriction over repair is acceptable | §4.1 |
| R4 | **Mostly.** "Not in `Γ_exe`" is mapped onto *not available* at the tuple's scope, and a table gives each row's disproved input and ground. A residual remains in the M-PR(m) and SEL-EXCL-1-family columns (N2) | outcome vocabulary; §2.2; §3; §11.1 |
| R5 | **Yes.** Bob's `b = r` at `y = 0` is added. The CP-6 negative is restated as a read of `r` in a run that also uses `y = 1`. Each negative is attributed to `T`'s algebra and `S`, to AD-1(f), or to the declared `Obs`, and the last is named a declaration under K-1. U2's reading `φ = T` per tick is distinguished from SEL-EXCL-1's "once" per "clocked use" (l. 44) | §1.2; §2.2; §3 |
| R6 | **Yes.** Both halves carry (h1)–(h4), are conditional on L-1's review, and list the same open cases. §11.2 repeats this | §6.1; §6.2; §11.2 |
| R7 | **Yes**, applied alike to every model. The Substratum:481 sentence introduced with it has an error (N1) | §6.2; §11.2 |
| R8 | **Yes.** R-lin's blanks now rest on heralded visible blanks at the D3 cost (OA1:156–160, :328), whose herald retention is unsourced, and on MR★:642 [NP]. D2 is no longer cited for it. Every §11.1 cell is labelled. The SNR-1 counting note separates D5 [M-r] from U1's factor-set reading [A-inf] and from L-1 | §2.1 s2, s4; §2.3; §11.1 |
| R9 | **Yes.** L-1 is a "proposed lemma", [A-inf], routed to #914 O-INS and #1060, with dependent verdicts conditional on its review. The match with Main:404–412 is offered as context only, and the stop vocabulary now includes "a new derivation" | §4.1; §5; §8.3; §9 |
| O1 | **Yes.** `B₂ = B₀ ⊕ x₁y₁ ⊕ x₂y₂`. With `x₁ = x₂ = x`, `y: 0→1` and `B₀ = 0`, `B₂ = x` (re-derived). The blank and a budget of at least 2 are listed | §2.5; §5; §7; §9 |
| O2 | **Yes.** The flag is stated as vacuous. The (g)-reading coincidence is attributed to folding the retention into one tick | §8.1 |
| O3 | **Yes:** "may meet …; not constructed or checked" | §4.2 |
| O4 | **Yes.** The argument is grounded in S-A6 and SEL-DISC-1 l. 97, which I re-read and which matches | §2.6 |

## 2. Scope of the diff

The word-level diff from r1 to r2 shows three kinds of change: the R/O changes above, the citation
of c.6891511297, and extensive editorial restructuring of prose into lists. That restructuring
changes no claim I could find. Three small additions are not tied one-to-one to a finding, and I
checked each:
- §2.1 s4, R-lin: "`T` writes `x∧y` into `B`. The map is not affine, and every `φ^t` of an affine
  `φ` is affine." This is correct and harmless, a direct ground beside the D5 label.
- §2.2: a QR-1 row, "not available at the scope of M-PR5", on the ground that every record law of
  M-PR5 is a sub-read of CP-1. This is correct. Deterministic local relabellings of one PR use with
  no further local randomness give integer CHSH values, so never `2√2`. It restates r1's "coverage
  absent by model" in R4's vocabulary.
- The c.6891511297 record: r2 says no U2 verdict uses S-L3, CC4, CC5 or CC7. Confirmed. U2 cites MR★
  S-C4b (:638), :642 and S-C1(c) (:508–509), and none of those is among the four items.

The response's "Nothing else changes" is accurate in substance.

## 3. New findings

### Required

**N1. The status of the "no excess above `2√2`" datum is misstated.** §6.2 and §11.2 say that the
corpus carries this datum "only as a falsification condition (Substratum:481)". Substratum:481 is
indeed a Class A falsification condition (Substratum:475, "would falsify … if violated"), so that
part is accurate. But "only" is a negative corpus claim (§A.19), and it is false.
- The corpus also carries the datum as an empirical input. E1, at Substratum:76 [M]: "The observed
  physics is described, to the precision tested, by quantum mechanics … Born-rule outcome
  statistics."
- Quantum mechanics bounds every two-wing dichotomic CHSH value by `2√2`. So E1 entails that no
  excess above `2√2` has been observed within tested precision.
- E2's mirror in the book adds "refined in loophole-free tests since 2015" (`book/ch02-substratum.md`:58).

Change: state that the datum is carried by E1 (Substratum:76) as an empirical input, implied by it
through the quantum bound, and that Substratum:481 records the corresponding falsification
condition. The corpus states no measured CHSH value, and U2 still takes none from outside it. M-PR5's
raw-direct miss then stays conditional on `Θ`'s identification alone, given E1. This is a correction
of status wording and does not change the verdict.

**N2. A residual of R4: two columns still use states U1 does not define.** r2 says "r2 uses no other
state". But §11.1's M-PR(m) column has "excluded by declaration [OFF]" (CP-6) and "not in the
circuit [OFF]" (CP-7, CP-8), and the §3 SEL-EXCL-1-family column has the same. Map each one onto the
declared vocabulary:
- either *not available* at the scope of the specified circuit, by its declared grammar (SEL-EXCL-1
  ll. 91, 97, 150), with the K-1 caveat that this rests on a declaration;
- or *stop* where exhibiting the operation would need a construction (as §8.3 already lists for
  CP-6 and CP-7).

### Optional

- **P1.** §6.2: "That identification is S8 and `Θ` (a), and for the wing geometry it is also S5"
  merges two things. The wing geometry is `Θ` (a)/S8 material. S5, measurement independence, is a
  separate condition. Suggest: "… S8 and `Θ` (a), including the wing geometry; and S5."
- **P2.** §11.2, "What U3 can use": the CP-4 resource line ("one writer, plus one blank for the
  fresh-output variant") could add, as AW-U2-3 does, that the same-register witness also uses the
  blank `B₀` and a budget of at least 2.

## 4. Readiness for owner acceptance

U2 r2 meets PLAN:871's scope. It classifies only RO-1's own control programs, reads NAS without
classifying G_SM anew, and routes S-A1 to S-A7 and L-1 without classifying them. It reports AC-1 in
both amended halves on one model and one interface each. It treats C ⊆ Q as a finding, adopts no
premise, and keeps every off-`main` dependency labelled as a gap (§10; §A.42 item 8, §A.46 item 1).
It is ready for owner acceptance with N1 and N2 applied. Neither needs a further full review: a
diff check of the two edits is enough.

## Checked

- `git diff --stat ad83ee33..3fb9a6be`, and the word diff of r1 against r2.
- r2 §§1–11 read in full; `RESPONSE-S3-U2-r1.md` read in full.
- #1169 c.6891511297 via the GitHub API.
- Substratum:76, :123, :475–481; `book/ch02-substratum.md`:58; corpus grep for loophole-free,
  Tsirelson and observed-CHSH statements in `papers/` and `book/`.
- Re-derivations: O1's witness; L-1 under (h1)–(h4); integer CHSH for deterministic relabellings
  of one PR use.

## Not checked

- The other files added at this head (U4, VERIFY-SL3-CC r2 and their reviews), which are outside
  this confirmation.
- Line anchors that r2 carries over unchanged from r1, already spot-checked in the r1 review.
