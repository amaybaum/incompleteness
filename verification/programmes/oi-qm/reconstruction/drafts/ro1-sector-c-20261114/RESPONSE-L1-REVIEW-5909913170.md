# Response to the independent mathematical review of L-1 (PR #1294 review 5909913170)

**Review.** PR #1294 review 5909913170 (`amaybaum`, 2026-11-15T08:50:28Z), at exact head
`b547c9f21c72ee29a2a3e07f9f14dd93bfc07107`, on `S3-U2-r3.md` §4.1 (lines 492–550, blob
`2711c168a65c0ae4397195593528fcf0ee6a4cba`). Verdict: counterexample to L-1 as stated under
(h1)–(h4) alone; the core binary argument proved for finite or atomic hidden laws with unconditioned
CHSH.

**Scope of the correction.** Owner decision #1169 c.6892224647 (`amaybaum`, 2026-11-15T09:17:55Z):
- "L-1 is restricted to finite-valued hidden states, with all four setting pairs represented and
  measurement independence preserved."
- "The CHSH bound applies to the complete, unconditional outcome statistics of all attempted runs.
  No setting-dependent postselection."
- "Contains setting–setting selection" is replaced by "the executed output map exhibits
  setting–setting selection under U1's criterion". "No inference to a particular primitive
  operation."
- "The existing exclusions stay: seed-written settings, missing S5, flagged readouts, observer-level
  extensions."
- "This is not adoption of a premise, a merge, or a change to U2's accepted status."

**Revision.** `S3-U2-r4.md` differs from r3 only by this correction and its necessary consequences.
r3 is left unchanged. The corrected L-1 is at r4:527–660; it is proposed, pending a focused
independent confirmation. Nothing is computed, and no premise is adopted.

## Dispositions

### §1. Core algebra — valid

**Accepted.** The review's mixed-difference reading is the one r4 uses. For binary carrier and binary
output, equality of the two induced partitions of the carrier is the vanishing of the mixed
difference `D b(λ) = b(0,0,λ) ⊕ b(0,1,λ) ⊕ b(1,0,λ) ⊕ b(1,1,λ)` (and `D a(λ)` for Alice). Its
vanishing on every positive-mass `λ` gives `a ⊕ b = α(x, λ) ⊕ β(y, λ)`, and a common
setting-independent law of `λ` gives `|S_CHSH| ≤ 2`. r4 writes this out in five steps (r4:584–598)
and states the predicate "exhibits setting–setting I-sel under U1's criterion" as "the mixed
difference is 1 at some `λ` of positive mass" (r4:563–577). r4 also checks that the comparison meets
U1's positivity qualifier under either reading, on the rest or on the whole configuration, using (h3)
and (h6) (r4:572–574).

### §2. Counterexample to the literal U1 predicate (blocking)

**Accepted; repair (a) applied.**
- *Check by hand* [A-inf]. `φ(x, y, A, B, u) = (x, y, A, B ⊕ (x∧y), u)` is an involution, so a
  bijection. With `x, y` fair and independent, `A = B = 0`, and `u` uniform on `[0,1]` and
  independent of the settings, the table is `a = 0`, `b = x∧y`, so `S_CHSH = 4`. Every exact value of
  `λ = (A₀, B₀, u)` has mass 0, so U1's fixed-`λ` comparison with selector `{x}` and carrier `{y}`
  is never admitted, although `D b = 1` everywhere. The review's further point also checks: with
  carrier `{y, u}` and rest `A = B = 0` (a value of mass 1), the partitions differ for `x = 0` and
  `x = 1`, so a different I-sel comparison holds. r4 records that L-1 says nothing about that
  comparison.
- *Repair.* (h5) restricts L-1 to finite-valued hidden states, and (h6) requires all four setting
  pairs to have positive mass. Under (h5), `μ(Λ⁺) = 1` (proof step 1, the only use of (h5)). Repair
  (b), a revision of U1's test for non-atomic laws, is not adopted and is listed as not made
  (r4:623–624; §8.3).
- *Recorded limit.* The example is stated in r4 §4.1 as a limit of scope, not as a claim about OI
  (r4:609–624).
- *Necessary consequences.*
  - "Non-atomic hidden states" joins the open cases of §§6.1, 6.2 and 11.2.
  - §4.2's R-lin cell notes that where the hidden factors are real-valued with a non-atomic law,
    (h5) fails and the L-1 route is open; the [M] bound outside the cone with S5 is unchanged.

### §3. Other boundary conditions

| Bullet | Disposition | Where in r4 |
|---|---|---|
| **Postselection** | **Accepted.** (h7) takes CHSH on the complete, unconditional statistics of all attempted runs, conditioned on the setting pair alone, with herald and failure masses retained (U1 G5). The review's example is checked by hand [A-inf]: full-attempt `E(x, y) = 1/2` for every pair and `S_CHSH = 1`; conditioned on both success flags, `i = x`, `j = y` and `S_CHSH = 4`. No outcome map or flag exhibits setting–setting selection, since each flag depends only on the local setting and `λ`. The example meets (h1)–(h7), and L-1's bound holds for its full-attempt table. It is recorded as a limit of scope. A statement for herald-conditioned statistics would need a separately proved setting-independent conditional law and is not made | §4.1 (h7), proof step 4, limits of scope; §§6.1, 6.2, 8.3, 11.2 |
| **Seed-written settings** | **Accepted; exclusion kept.** The case stays outside (h2)–(h3), and r4 makes no claim that seed-written realizations evade the bound. Clause (a) is re-anchored to the mixed-difference reduction, since r4's proof no longer uses the words "trivial or discrete" | §4.1, cases outside the hypotheses |
| **No S5** | **Accepted; exclusion kept.** Proof step 4 is where the common law of `λ` enters | §4.1 |
| **Flagged and coarse readouts** | **Accepted.** One sentence is added: a binary output factor written by `φ^{t_c}` falls under L-1 whenever (h1)–(h7) hold. The flagged case remains the one where an outcome is a non-injective function of a larger region, outside (h4) | §4.1 |
| **Extensions** | **Accepted, within the kept exclusion.** Observer-level operations stay at S7(a). r3's "L-1 does not reach operations typed into `φ` or `Γ`" is replaced by: L-1 concerns models that meet (h1)–(h7); an operation typed into `Γ` as supplied apparatus fails (h1); an extension folded into `φ` gives a different model, and whether it meets (h1)–(h7) is not decided. The "open for extension operations" entries of §§6 and 11.2 are unchanged | §4.1 |
| **Composition** | **Accepted.** "Contains setting–setting I-sel" becomes "the executed output map exhibits setting–setting I-sel under U1's criterion" in §§4.1, 4.2, 5, 6.1, 7 and 9. r4 states that U1's test quantifies over ticks, so `φ` is then I-sel in U1's sense, and that no tick, primitive gate, native resource, apparatus mechanism or sourced operation is identified. §6.1's restriction row now reads "under U1's criterion at every tick" and adds that a restriction stated on a particular primitive operation is not reached by L-1 | §4.1 consequence; §§4.2, 5, 6.1, 7, 9 |

### Disposition

**Accepted.**
- L-1 is not marked proved. It is a proposed lemma at the scope of (h1)–(h7), pending a focused
  independent confirmation, and every verdict resting on it is conditional on that confirmation.
- Existing programme-level stops are kept, and §8.3 adds the forms not attempted (non-atomic,
  herald-conditioned) and the U1 revision not made.
- The downstream statements are reconciled in §§4.2, 5, 6.1, 6.2, 7, 8.2, 8.3, 9, 10, 11.1 and 11.2.
- Nothing in r4 closes the C/Q relation, Bell sourcing or AC-1's coverage obligation. U2's accepted
  status is unchanged. No outcome state of r3 changes; the verdicts that rest on L-1 are narrowed.

## Consistency with `S3-U3-r2.md`

U3 r2 uses its own elementary step (U3 r2 §4.2) and states that no conclusion of U3 rests on L-1.
Checked:
- U3's elementary step is stated on response functions almost surely, not on U1's fixed-rest
  predicate, so it holds for non-atomic laws. That agrees with the non-atomic example, where
  `D b = 1` at every `λ`. U3 allows a herald that is a setting-independent function of `λ`;
  conditioning on such a herald keeps the law of `λ` independent of the settings. This is U3's own
  statement. L-1 at r4's scope does not make it.
- Two wording differences, for U3's next revision; no U3 verdict depends on them:
  - U3 r2 describes L-1's scope as "finite or atomic source laws" (U3 r2 lines 17–18, 522–523). r4's
    scope is finite-valued hidden states.
  - U3 r2 §5.1, "Relation to L-1", states L-1 under "(h1)–(h4)" with "requires setting–setting I-sel".
    r4 has "(h1)–(h7)" and "exhibits".
- U3 r2's line anchors `U2:492–550` and `U2:528–530` refer to r3 and stay valid for r3. In r4, L-1
  is at r4:527–660, and its consequence paragraph is at r4:600–607.

## Diff r3 → r4

`diff S3-U2-r3.md S3-U2-r4.md`; r3 line ranges, then r4 line ranges. r4 is 938 lines; r3 is 822.

| r3 | r4 | Change |
|---|---|---|
| 1 | 1 | title: r3 → r4 |
| 3 | 3–5 | status: r4 differs from the accepted r3 only by the L-1 correction; L-1 pending confirmation |
| after 12 | 15–42 | new Revision r4 block: review and decision, quoted scope, change list |
| after 82 | 113–115 | Authorization: c.6892224647 added |
| after 91 | 125–126 | Inputs: review 5909913170 added |
| 492 | 527 | §4.1 heading |
| 494 | 529–530 | §4.1 status: pending focused confirmation |
| 497 | 533–538 | §4.1 status: conditional on confirmation; what the review finds; scope by owner decision |
| 502–503 | 543–545 | hypotheses heading; (h1) stated in full |
| 507–530 | 549–635 | (h3) formula; (h4) observer; new (h5)–(h7); CHSH sign convention; selection test applied; statement; proof; consequence; the two limits of scope |
| 532 | 637 | "Cases L-1 does not cover" → "Cases outside L-1's hypotheses" |
| 536 | 641–642 | seed-written clause (a) re-anchored |
| 542–546 | 648–655 | flagged sentence added; extensions bullet restated |
| 549–550 | 658–660 | standing: finite-valued hidden states; confirmation; (h1)–(h7) |
| 556 | 666 | §4.2 QR-1 row: (h1)–(h7), "exhibits"; non-atomic R-lin note |
| 580 | 690 | §5 routing row |
| 592–593 | 702–703 | §6.1 restriction row and R-lin row |
| 601 | 711 | §6.1 coverage on R-lin |
| 631 | 741 | §6.2 I-sel restriction row |
| 665–666 | 775–776 | §7 H-RR pointer |
| 697–698 | 807–808 | §8.2 L-1 bullet: (h6) |
| 714 | 824–826 | §8.3 stop: scope, confirmation, forms not attempted, U1 revision not made |
| 730 | 842 | §9 L-1 row |
| 740 | 852–853 | §9 pressure test |
| 751 | 864–865 | §10: review row added; c.6892224647 added to governance row |
| 771 | 885 | §11.1 QR-1 row: (h1)–(h7) |
| 786–787 | 900–902 | §11.2 coverage bullet |
| 790 | 905 | §11.2 R-lin bullet |
| 812 | 927–928 | §11.2 "What U3 can use": L-1 at (h1)–(h7) |

No other line changes. The literal "(h1)–(h4)" survives twice in r4: in the revision note naming the
replacement, and in the non-atomic example, where (h1)–(h4) hold and (h5) fails.

**Checks.** r4 is built from r3 by exact-string replacements, each occurring once. The new §4.1 block
replaces r3:492–550 whole. The forbidden words, local paths and closing keywords were checked with
grep in both files, with no match.

## Response to the focused review of r4 (`REVIEW-S3-U2-r4.md`)

**Review.** `REVIEW-S3-U2-r4.md`, on the r4 object at `022ed5ab`: ACCEPT WITH CHANGES, with one
required change, R1, and optional items O1–O6. The edits are made in place in `S3-U2-r4.md`, and
nothing else changes. Line numbers below are those of r4 after these edits (943 lines). The anchors
given earlier in this file refer to r4 before them; L-1 is now at r4:528–663.

| # | Finding | Disposition | Where in r4 |
|---|---|---|---|
| R1 | The open-case lists do not match the complements of (h5) and (h7) | **Accepted; wording only.** "Non-atomic hidden states" becomes "hidden states that are not finite-valued (non-atomic, countably infinite or mixed laws)". "Statistics conditioned on a setting-dependent event" becomes "statistics conditioned on any event (a herald or success flag, setting-dependent or not)". §8.3's forms not attempted get the same two phrases. L-1 is not extended to these cases. This also extends the list wording of §2 ("Necessary consequences") and of the §3 postselection row above | 38–39 (revision note); 705 (§6.1); 744 (§6.2); 828–829 (§8.3); 906–907 (§11.2) |
| O1 | (h1)'s bijectivity is not used | **Applied.** (h1) states that the proof uses only the functional dependence, not bijectivity | 546–547 |
| O2 | `α`, `β` could be read as the wings' response functions | **Applied.** One sentence: they decompose the parity and are not the wings' response functions | 594 |
| O3 | "The statement fails at this scope" | **Applied.** It now reads "L-1's conclusion fails without (h5)" | 623 |
| O4 | Factor-by-factor reading of U1's positivity qualifier | **Applied.** "on the rest alone, factor by factor, or on the whole configuration" | 576–577 |
| O5 | Write the flag factors as XOR-written by `φ` | **Not applied.** This is more than a one-line precision fix. The example's outcome and flag functions are stated, and the review checked them as stated | — |
| O6 | (h7) is a condition on the statistic | **Applied.** §6.2's row reads "realized by programs meeting (h1)–(h6) and scored on full-attempt statistics (h7)" | 744 |

**Changed line ranges** (`diff` of r4 before and after these edits; before → after): 38 → 38–39;
545 → 546–547; 574 → 576–577; 591 → 594; 620 → 623; 702 → 705; 741 → 744; 825 → 828–829;
902 → 906–907.
