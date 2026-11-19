# RESPONSE-r2: disposition of REVIEW-r2 for G3 unit 1

**Review.** `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/REVIEW-r2.md`, on
branch `research/g3-offset-873-20261113` at `25257ae5`. It reviews r2 at `1aaf87a2`. Verdict: REVISE,
with one blocking finding (R2-1), five should-fix findings (R2-2 to R2-6) and three nits (R2-7 to
R2-9).

**Files.** New: `G3-UNIT1-r3.md`, `NOTES-r3.md` and this file. The r1 and r2 files are unchanged.

**Line references.**

- "r3:n" is a line of G3-UNIT1-r3.md.
- "N3:n" is a line of NOTES-r3.md.
- "r2:n", "N2:n" and "RESP:n" refer to the r2 files, as in the review.
- Corpus lines refer to `main` at `c3b5f37a`.

## Summary

| Finding | Disposition | r3 location |
|---|---|---|
| R2-1 | Applied, with two precisions of wording (below) | §0 r3:34–79; §2 r3:211–222; §3.1 r3:278–346; §3.2 r3:357, :361–365, :373–374; B1 r3:404–406; B5 r3:445–496; §4 r3:506, :517; §5 r3:525–543, :590–599, :606–608; F1 r3:619; F8 r3:626; AW-loop r3:644–648; N3 §4 and §5 |
| R2-2 | Applied (the review's text) | r3:333–336; N3 §4 |
| R2-3 | Applied | r3:327–331 |
| R2-4 | Applied (the review's text) | F5 r3:623 |
| R2-5 | Applied at all three places | r3:280–282, r3:387–389, F2 r3:620 |
| R2-6 | Applied (the review's text) | r3:605–608 |
| R2-7 | Applied | r3:182–183 |
| R2-8 | Applied | r3:576–577 |
| R2-9 | Applied | r3:484–486 ("directly") |

No finding is rejected. R2-1 is accepted in substance, and its central charge is correct. In r2, the
step "on shell, metric → origin" held only because `Λ₁` was defined from `ρ(r₀)`. That made the
"selection" a read-back of a free coordinate, and the r2 completion world-equivalent to K_dec. The
completion with physical content, which GR:352 contrasts, fixes the offset by convention from
post-partition data. For that completion, GR:346's loop closes.

## R2-1, in detail

**Applied as the review proposes:**

- The two cases K_cpl^free and K_cpl^conv (r3:338–346, and the λ-families at r3:297–305).
- The replacement B5 bullet (r3:469–471).
- The replacement node verdict (r3:488–493).
- The two-part verdict in §0 and §5 (r3:36–49, r3:525–531).
- R0 redefined as "GR:346 as argued (no self-consistent loop through post-partition data)", called
  (ii-L) (r3:463–464, r3:535–543).
- F1 (r3:619), F8 (r3:626), the AW-loop marker (r3:62–63, r3:644–648), O0 (r3:590–599), and Q7/Q8 in
  N3 §5.
- N2:71, N2:76–78 and RESP:49–55 are corrected in N3 §4 and in this file. The r2 files themselves stay
  unchanged.

**Precision 1: (DZ) in place of "(SI) for the convention-fixed offset".**

- K_cpl^conv's offset `e_Z` is a function of the operational class `[r]`. Relabelling `σ_C` at fixed
  `κ` leaves `[r]` unchanged, so K_cpl^conv **satisfies** (SI) and (SI′) as §2 defines them [A]
  (r3:323–325).
- Part (2) of the verdict therefore needs its own target. That target is (DZ), zero-point decoupling:
  the source is constant in `e_Z` (defined at r3:211–218, together with the zero-point convention `Z`).
- The review's phrase "(SI) for the convention-fixed offset" is rendered "(DZ) for the convention-fixed
  offset". Once (DZ) is defined, this is equivalent to the review's meaning.
- Without the new target, part (2) would assert a violation of (SI) that K_cpl^conv does not commit.

**Precision 2: "fixed independently of the metric".**

- The review's text reads "ρ(r₀) is fixed independently of the metric".
- r3 writes "`ρ_Z(r₀)` is fixed by the emergent class and not read back from the field equation"
  (r3:343–344).
- The reason: `e_Z` depends on the class, the class on the partition, and the partition on the metric
  (GR:346). "Independently of the metric" would then contradict the loop that the B5 bullet identifies
  next.
- The intended contrast, a convention fix rather than a field-equation read-back, is unchanged.

**Additions consistent with R2-1.**

- B5 now names three readings: strong (ii-S), loop (ii-L, which is GR:346 as argued), and weak (ii-W)
  (r3:458–468). The review's R0 is (ii-L).
- B5 states which coupled completion each reading excludes.
- The corpus-use bullet adds GR:374, which the review cites (r3:475).
- B1 is amended so that K_cpl^free's on-shell "selection" is called a relabelling, and K_cpl^conv's
  origin is attributed to the convention `Z`, which (TL) does not supply (r3:404–406).
- The §3.2 "What differs" passage and the ordering row are split by completion (r3:357, r3:361–365).

**Class of F8.** NEW candidate (the GR:346 / GR:400 tension), flagged for review, as the review allows.

## R2-2 to R2-9

- **R2-2.** The review's replacement text is used verbatim, apart from list formatting (r3:333–336).
  N2:73 and RESP:102–103 overstated the claim, and N3 §4 corrects them. Scoping "differ only" to the
  oriented branch is kept, as the review allows.
- **R2-3.** "(under K9's hypotheses, §1.1)" is inserted (r3:328–329). K9's hypotheses are listed in
  the K9 row of §1.1.
- **R2-4.** F5 now reads: "`E_s` carries no energy-origin constant; it inherits the additive constant
  of `s_H` (GR:58), set to zero in `S_dS = σA/ε²` (GR:422)" (r3:623).
- **R2-5.** The qualifier is appended at r3:280–282 (§3.1 data), r3:387–389 (§3.3, item 2) and F2
  (r3:620).
- **R2-6.** The O1 bullet is replaced (r3:605–608). It now says the λ-families are compatible with
  every OI premise for K_cpl^free, and only conditionally on the corpus's reading of (ii) for
  K_cpl^conv.
- **R2-7.** `κ⁻` now excludes the metric and the partition (r3:182–183). K_cpl^free's violation of
  (SI′) at r3:320–321 keeps its reason, which is the differing de Sitter radii. That reason now applies
  as stated.
- **R2-8.** The finite-4-volume qualifier is added to the spacetime average (r3:576–577).
- **R2-9.** "cheaply" is replaced by "directly" (r3:485).

## Passages changed from r2 (delta list)

The line ranges come from `diff G3-UNIT1-r2.md G3-UNIT1-r3.md`. Each entry gives r2 → r3.

| r2 | r3 | Change |
|---|---|---|
| 1 | 1 | Title r2 → r3 |
| 8–9 | 8–10 | Header lists both reviews and both responses |
| 35–65 | 36–72 | §0: two-part verdict, results list, AW-loop, solution-level bullets (R2-1) |
| 175 | 182–183 | κ⁻ (R2-7) |
| after 202 | 211–218 | Zero-point convention and (DZ) (R2-1, precision 1) |
| 205 | 221–222 | Question includes (DZ) and the §A.34 note |
| 264 | 281–282 | Data bullet, R2-5 qualifier |
| 267–284 | 285–308 | Two offset functionals, their properties, the two λ-families (R2-1) |
| 289–290 | 313–314 | Coincidence at r₀ for every x |
| 296–298 | 320–325 | Response to the shift, by completion (R2-1) |
| 301–317 | 328–346 | "Only" scope (R2-3); reflection (R2-2); the two on-shell cases (R2-1) |
| 328 | 357 | §3.2 ordering row |
| 332 | 361–365 | "What differs", by completion |
| 340 | 373–374 | Shared-list scope sentence |
| 354 | 388–389 | §3.3 item 2, R2-5 qualifier |
| 369–370 | 404–406 | B1 |
| 415–450 | 451–493 | B5: (i), (iii), three readings, where the loop closes, corpus use (adds GR:374), skepticism (R2-9), node verdict, AW-loop |
| 452 | 495–496 | NEW-count sentence |
| 462 | 506 | §4 ordering row |
| 473 | 517 | §4 closing list |
| 481–489 | 525–543 | §5 verdict and R0 |
| 508 | 562 | ρ_x in R2a |
| 522 | 576–577 | R2-8 |
| 535–542 | 590–599 | O0 |
| 549 | 606–608 | O1 (R2-6) |
| 560–561 | 619–620 | F1, F2 |
| 564 | 623 | F5 (R2-4) |
| 567 | 626 | F8 |
| after 584 | 644–648 | AW-loop marker |

Every other line of r3 is identical to r2.

## Checks

- No computation, build or script was run.
- The review records `claims_check`, `staleness_check`, `voice_check`, `artifact_placement_check` and
  `legacy_records_check` passing at `1aaf87a2`. None of them scans the drafts.
- All three new files were scanned by hand for the barred path strings and words, and for
  history-voice phrases.
- Every citation that is new or changed in r3 was re-read at `c3b5f37a`: GR:332, :346, :358, :374,
  :400, :422 and :58. They are listed in N3 §3.
