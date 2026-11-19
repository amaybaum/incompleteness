# Review of S3-U2-r4 (bounded L-1 correction) and RESPONSE-L1-REVIEW-5909913170

**Reviewer.** Independent, read-only, paper-only. Not the author of the object. Hand checks only; no
computation, no Lean, no edits.

**Object.** Worktree at `022ed5ab`. `S3-U2-r4.md` (938 lines) against the accepted `S3-U2-r3.md`
(822 lines), and `RESPONSE-L1-REVIEW-5909913170.md`. Checked against PR #1294 review 5909913170
(`amaybaum`, 2026-11-15T08:50:28Z, at `b547c9f2`), read in full; the owner decision #1169
c.6892224647 (`amaybaum`, 2026-11-15T09:17:55Z), read in full; U1 r5 §4.3(i) (I-sel, positive-mass
fixed-rest values) and G5 (complete masses).

**Verdict: ACCEPT WITH CHANGES.** The corrected L-1 is proved by hand at the stated scope. One
required change: the open-case enumerations downstream do not match the complements of (h5) and (h7).
Optional items O1–O6.

## 1. Diff r3 → r4

`diff S3-U2-r3.md S3-U2-r4.md` has 29 hunks. Each matches a row of the response's diff table, and
the table has no row without a hunk. "No other line changes" holds. Every hunk is the correction or a
necessary consequence:

- title, status (lines 1, 3–5), revision block (15–42), authorization and input entries (113–115,
  125–126): bookkeeping for the correction;
- §4.1 (527–660): the corrected lemma, hypotheses, test, proof, consequence, limits of scope;
- §§4.2, 5, 6.1, 6.2, 7, 8.2, 8.3, 9, 10, 11.1, 11.2: "(h1)–(h4)" → "(h1)–(h7)", "contains" →
  "exhibits", the two added open cases, the review row in §10.

Changes beyond the review's and the owner's lists, all narrowing or explanatory, none broadening:
- (h1) now states "`φ` is a fixed bijection". The proof does not use bijectivity (O1).
- (h3) gains the product formula; (h4) gains "in that wing's observer (AD-1(a))". Both are what the
  application of U1's test needs (`Y` readable under AD-1).
- The CHSH sign convention (560–561). Correct: relabelling a setting value moves the minus sign and
  leaves the mixed differences and (h2), (h3), (h6) unchanged.
- §4.1 heading "Cases L-1 does not cover" → "Cases outside L-1's hypotheses"; seed clause (a)
  re-anchored because "trivial or discrete" no longer appears.
- §6.1 restriction row gains "under U1's criterion at every tick" and "A restriction stated on a
  particular primitive operation is not reached by L-1". This is the composition point of the review
  and the owner's "no inference to a particular primitive operation".

The literal "(h1)–(h4)" survives at lines 36 and 616 only, both legitimate. No residual "contains"
tied to L-1 (the remaining hits are "`φ` contains `T`", unrelated).

## 2. The corrected proof, re-derived

**Test application (563–577).** U1 §4.3(i): selector values of positive mass; readable `Y`; tick `t`;
the rest fixed at a value of positive mass; the partition of the carrier's content induced by
`s_carrier ↦ pr_Y φ^t` differs. For Bob: selector `{x}`, carrier `{y}`, rest `λ`, `Y = B`,
`t = t_c`. A two-element carrier has two partitions, one class (`Δ_y b(x,λ) = 0`) or two classes
(`= 1`). They differ between `x = 0, 1` iff `Δ_y b(0,λ) ⊕ Δ_y b(1,λ) = D b(λ) = 1`. Correct;
Alice's wing likewise.

**Admissibility.** (h6) gives `μ(x = z) > 0` for both selector values. (h3) and (h6) give
`μ(x,y,λ) = μ(x,y)μ(λ) > 0` whenever `μ(λ) > 0`. So a positive-mass `λ` with `D b(λ) = 1` is an
admitted U1 comparison under a joint reading of the rest, a configuration-wide reading, and also a
factor-by-factor reading (each marginal of a positive-mass joint value is positive; O4). Hence: the
predicate as defined (`D = 1` at some `λ ∈ Λ⁺`) is sufficient for U1 I-sel of `φ^{t_c}` for that
pair. The proof needs exactly this direction (not-exhibited ⇒ `D = 0` on `Λ⁺`). **Confirmed.**

**Steps.**
1. `Λ` finite ⇒ `μ(Λ∖Λ⁺) = 0`. Correct. (h5) is used only here; admissibility uses atoms but not
   finiteness.
2. `D b(λ) = 0` ⇒ `Δ_y b(0,λ) = Δ_y b(1,λ) = k_B(λ)` ⇒ `b(x,y,λ) = b(x,0,λ) ⊕ y·k_B(λ)`. Check: at
   `y = 1`, `b(x,0) ⊕ k_B = b(x,0) ⊕ Δ_y b(x) = b(x,1)`. Likewise `a(x,y,λ) = a(0,y,λ) ⊕ x·k_A(λ)`.
   Correct.
3. `a ⊕ b = [b(x,0,λ) ⊕ x·k_A] ⊕ [a(0,y,λ) ⊕ y·k_B] = α(x,λ) ⊕ β(y,λ)`. Correct. (`α` carries a
   term of Bob's output; harmless, since CHSH reads only the parity; O2.)
4. (h7) defines `E(x,y)` as the full-attempt mean given the setting pair; (h6) makes it defined;
   (h3) makes `μ(λ | x,y) = μ(λ)`; step 1 restricts to `Λ⁺`, where step 3 holds. So
   `E(x,y) = Σ_{Λ⁺} μ(λ) A_x(λ) B_y(λ)` with the **same** weights at every setting pair. This is the
   common-`λ` averaging, and it rests on unconditional full-attempt statistics plus S5. **Confirmed.**
5. `A_0(B_0 + B_1) + A_1(B_0 − B_1) = E00 + E01 + E10 − E11` integrand; one bracket is 0, the other
   `±2`; value `±2`; `|S_CHSH| ≤ 2`. Correct.

**"On at least one wing."** The contrapositive needs `D a = 0` and `D b = 0` on all of `Λ⁺`; a
violation therefore needs one nonzero mixed difference on one wing. It cannot be strengthened to both
wings: the PR table `a = 0`, `b = x∧y` has `D a = 0`, `D b = 1`, `|S| = 4`. **Correct.**

**Consequence (600–607).** U1's I-sel is existential in the tick, so exhibition at `t_c` makes `φ`
I-sel in U1's sense; no tick, primitive gate, native resource, apparatus mechanism or sourced
operation is identified. Matches the owner's wording and the review's composition point.

## 3. The two recorded limits

Both are introduced as "limits of the statement's scope. They are not claims about OI, and neither is
a model of OI's premise list" (609–610). **Confirmed as scope limits.**

- *Non-atomic.* Checked: `φ` an involution; `a = 0`, `b = x∧y`; `E11 = −1`, others `+1`,
  `S = 4`; every exact `λ = (A₀, B₀, u)` has mass 0, so the fixed-`λ` comparison is never admitted;
  with carrier `{y, u}` and rest `A = B = 0` (mass 1) the partitions differ (one class at `x = 0`,
  two at `x = 1`). Correct. "The statement fails at this scope" means L-1's conclusion without (h5);
  wording could be sharper (O3). Option (b) recorded as not made. Correct.
- *Postselection.* Checked: full-attempt `E = 3/4 − 1/4 = 1/2` at each pair, `S = 1`; conditioned on
  both flags, `i = x`, `j = y`, `b = x∧y`, `S = 4`. No output (outcomes or flags) depends on the remote
  setting, so no setting–setting I-sel for any carrier. The example meets (h1)–(h7) and the bound
  holds on its full-attempt table. Correct. The flag-writing part of `φ` is not written out (O5).

## 4. Downstream consistency (§§4.2, 6, 8.3, 11.2)

All L-1-dependent statements carry "(h1)–(h7)" and "exhibits"; every verdict stays conditional on
L-1's confirmation; outcome states of r3 are unchanged; nothing is broadened. §4.2's R-lin note
("real-valued with a non-atomic law, (h5) fails and this route is open") is correct as a sufficient
case. §8.3 lists the forms not attempted and the U1 revision not made. §10 classifies the review
reference correctly under §A.42 item 8: support off `main` for the report of its finding,
provenance for the examples and proof re-checked here.

**Required R1. Open-case lists do not match the complements of (h5) and (h7).**
- (h7) excludes *every* conditioning ("No conditioning on a herald, success flag or other event
  enters"; 557–558). The open lists of §6.1 (702), §6.2 (741) and §11.2 (900–903), and the revision
  note (37–38), name only "statistics conditioned on a setting-dependent event". Statistics
  conditioned on a setting-independent herald (an event-ready design; the case U3 r2 treats with its
  own step) are outside L-1 but listed nowhere, so a reader can take them as covered. §8.3 already
  says "conditioned on a herald", generally.
- (h5) requires a finite `Λ`. The same lists, and §8.3 (825), name only "non-atomic hidden states".
  Countably infinite atomic laws and mixed laws are outside (h5) and are neither non-atomic nor listed.
- Fix (wording only, no claim change): in those places write "hidden states that are not
  finite-valued (non-atomic laws included)" and "statistics conditioned on any event (a herald or
  success flag, setting-dependent or not)", or state that the list is the complement of (h1)–(h7).
  Mirror the response's disposition bullets. Do not extend L-1 to these cases, even where its
  proof would go through (the owner's no-broadening scope).

## 5. Claim/evidence boundary; text rules

- No witness → theorem, finite → universal, or conditional → unconditional move: L-1 stays a proposed
  lemma at the scope of (h1)–(h7), pending focused confirmation; the review is reported as finding the
  core sound at finite or atomic scope, which matches its text.
- The implication and its contrapositive are stated; no equivalence is displayed (§A.34 not engaged).
- Owner quotes match c.6892224647 verbatim. The response's line anchors (r4:527–660, 563–577,
  572–574, 584–598, 600–607, 609–624, 623–624) are correct, and its U3 r2 quotations check.
- Added lines: no machine-local paths, no closing keywords, no new caps emphasis (only acronyms and
  file stems), no history-narration or reader-instruction phrases. The revision block follows the
  form already used in r2 and r3 of this draft.

## Optional

- **O1.** (h1)'s "fixed bijection" is not used by the proof. Keep it (OI's `φ` is a bijection) or
  note that the proof uses only that outputs are functions of the initial configuration.
- **O2.** In step 3, `α(x,λ)` contains `b(x,0,λ)` and is written `A_x`. A clause saying that
  `α`, `β` decompose the parity and are not the wings' own response functions would prevent a misread.
- **O3.** Line 620: "The statement fails at this scope" → "L-1's conclusion fails without (h5)".
- **O4.** Admissibility (572–574): add the factor-by-factor reading of U1's qualifier, also met.
- **O5.** Postselection example: write the flag factors as XOR-written by `φ` so that "meets
  (h1)–(h7)" can be checked line by line.
- **O6.** §6.2 (741): (h7) is a condition on the statistic, not the program; "realized by programs
  meeting (h1)–(h6) and scored on full-attempt statistics" is more exact.

## Confirmation (fix commit `85bfd162`)

Checked `git diff 75dd0600..85bfd162`. In that range `73f843a4` (GAMMA-G1-r3 review and its README
rows) is a separate unit, not part of this fix. `85bfd162` touches only `S3-U2-r4.md`, the U2 row of
`README.md` (digest `9b800abd…` matches the file at `85bfd162`) and an appended section of
`RESPONSE-L1-REVIEW-5909913170.md`.

- **R1 resolved.** The revision note (38–39), §6.1 (705), §6.2 (744), §8.3 (828–829) and §11.2
  (906–907) now name "hidden states that are not finite-valued (non-atomic, countably infinite or
  mixed laws)" and "statistics conditioned on any event (a herald or success flag, setting-dependent
  or not)". Together with the other listed exclusions, these are the complements of (h5) and (h7).
  L-1 is not extended to them.
- **Optional edits correct.** O1 (546–547): the proof does use only the functional dependence. O2
  (594): accurate. O3 (623): accurate. O4 (576–577): accurate, since a joint positive-mass value has
  positive marginals. O6 (744): "(h1)–(h6) and scored on full-attempt statistics (h7)" is exact.
  O5 is not applied, and the reason given is acceptable.
- **Nothing else changed** in `S3-U2-r4.md`: nine hunks, exactly the ranges listed. The anchor
  r4:528–663 for L-1 checks. Added lines have no local paths and no closing keywords.
- Cosmetic, optional: lines 38 and 828 now run past the file's usual wrap width.

**Verdict on the fix: R1 resolved; ACCEPT.**
