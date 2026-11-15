# Focused confirmation of S3-U3-r2 (independent, non-author)

**Objects.** In `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, at
`93e83475d`:
- `S3-U3-r2.md`, blob `34ffe552`;
- `RESPONSE-S3-U3-r1.md`.

r1 is unchanged at that commit (blob `3da2be22`). The retained `REVIEW-S3-U3-r1.md` is
byte-identical to the r1 review (blob `4155bc8d`).

**Reviewer.** The non-author Claude reviewer of r1. Read-only. Hand checking only: no computation,
commit, push or GitHub post.

**Verdict: ACCEPT.** R1–R4 and M1–M10 are all resolved. L-3 holds as stated. Every conclusion that
rests on L-2 or L-3 is marked as conditional. L-1 supports nothing. Three nonblocking nits remain
(N1–N3). N3 bears on the continuous-source claim.

***

## 1. Dispositions (r2 line numbers)

| Item | Status | Where |
|---|---|---|
| R1 | RESOLVED | §2.2 ll. 224–241 (three exhaustive cases (U), (S), (N)); §3 ll. 367–377; §4.1 ll. 479–481; §5.1 ll. 661–665; U3-1 l. 854; §10.1 l. 904; §10.2 l. 934; §10.5 l. 985. Residual wording: N1 |
| R2 | RESOLVED | §3 ll. 378–399; §5.2 ll. 678–752 (L-3); U3-2 l. 855; §10.1 l. 904; §10.3 l. 950. The inference is credited to the review |
| R3 | RESOLVED | §6 ll. 754–831; (a) ll. 807–819 and §10.7 ll. 1032–1050; (b) ll. 791–805 and l. 955; (c) ll. 756–760 and 796–798; (d) ll. 765–767; (e) l. 345 and U3-4 l. 857; (f) ll. 781–785; (g) l. 830 |
| R4 | RESOLVED | §10.3 ll. 943–951; owner question 4, ll. 1057–1062. "Demanded by" E1 is gone |
| M1 | RESOLVED | ll. 617–621, 649–655 |
| M2 | RESOLVED | ll. 186–204. With `Δ_k` as the set of non-inherited inputs, both directions hold by definition |
| M3 | RESOLVED | ll. 514–530. Residual: N3 |
| M4 | RESOLVED | l. 854 |
| M5 | RESOLVED | ll. 913–918 |
| M6 | RESOLVED | ll. 315–320; U3-5 l. 858 |
| M7 | RESOLVED | l. 970 |
| M8 | RESOLVED | ll. 47–48; l. 1015 |
| M9 | RESOLVED | ll. 229–232; §7 l. 839 |
| M10 | RESOLVED | ll. 166–176. Main:652 was checked at `75cc5100` and is quoted accurately |

## 2. Diff r1 → r2

Every hunk of the line diff maps to an item of the response, or to its "Other changes" list (the L-1
scope context and the §9 rows). Three added passages are not named one by one in the response:
- §4.1 ll. 475–476 and 484–486 (L-3's bearing on RR-1; the escape is (S) for the quantum law and (N)
  for PR's fresh cells);
- §4.4 ll. 589–592 (a pressure test of that favourable reading);
- §6 l. 784 (the alternating-axis example).

Each is a necessary consequence of R2 or R3(f), and each is marked as conditional or pressure-tested.
I checked the alternating example by hand: on one wing, each Lüders read along a Bloch-orthogonal
axis is fair and independent of the earlier outcomes. No unlisted substantive change was found.

The new citations I checked are all correct:
- SPEC:277 (J1), :404–405 (ledger Q1), :620–621;
- PLAN:416 (K-3);
- TSI:293 ("demonstrably fails (9)");
- Main:652;
- PR #1294 review 5909913170 (`amaybaum`, 2026-11-15T08:50:28Z).

## 3. L-3, re-derived by hand

**Derivation.**
- Fix Alice's policy `(x, x)` and Bob's second setting `y₂`, and vary Bob's first setting `y₁`.
- (9) gives `a₂ = a₁` almost surely at a repeated setting, for every `y₁` and `y₂`: Alice's factor in
  (9) depends only on her own settings.
- Under the hypothesis `κ_A = G(λ, ν, x₁)`, this reads `A₁(x, y₁, λ) = F(λ, ν)`, with
  `F = A₂(x, y₂, G(·, ·, x))`. Here `F` does not depend on `y₁`.
- By (k4′), the law of `(λ, ν)` is the same under `y₁ = 0` and `y₁ = 1`. The two full-measure sets
  therefore lie in one probability space, and `A₁(x, 0, λ) = A₁(x, 1, λ)` almost surely.
- In case (U), the single pair with Bob `(0, 1)` gives this directly.

**Conclusions (a)–(c).**
- (a) is the contrapositive of the statement. (U), (N), a tick-indexed `A₂` and dependence on the
  wing's own first setting alone are all forms of `G(λ, ν, x₁)`, so all are excluded on a wing whose
  first response depends on the remote setting.
- (b) follows from the elementary step together with (1): `|CHSH| = 2√2`.
- (c) holds: if `κ_A` were a function of `(x₁, y₁, a₁, b₁)`, then `a₂` would be fixed by the records,
  against (9)'s fairness at a changed setting.

**Instances.** Both check out:
- TSI case (U), Bob `(1,1)`, Alice `(0,1)`: `b₁ = R⊕C` and `b₂ = R⊕C⊕1`.
- Bob's wing under fresh replacement: `Pr(b₂ = b₁) = 1/2`.

**Scope.** As stated (ll. 745–752):
- no no-signalling premise, and no use of L-1 or L-2;
- deterministic realizations of (1)×(9) under `Θ` (S8), with S5 for `λ` and `ν`;
- both uses' records held at `t_c`;
- a herald only if it is a function of the source.

The scope claim "no atomic source law needed" is correct, subject to measurability (N2).

**Marking.** Every use of L-3 is marked as conditional:
- §3 ll. 378, 389, 399;
- §4.1 ll. 475–476, 484–485;
- §4.2 l. 534;
- §4.4 l. 588;
- §7 l. 839;
- U3-2 ("conditional on the review of L-3");
- §10.1 l. 904; §10.2 l. 935; §10.3 l. 950.

No verdict rests on L-3 unconditionally. It is stated as needed for coverage, not as executed
(l. 752).

## 4. L-1 and the continuous case

- **L-1 supports nothing.** L-1 appears only as context: ll. 17–21, 522–523, 659, 671–676, 883, 1007
  and 1051–1054. U3-3, U3-6, §2.4, §4.4 and the §10.3 probe row now rest on the elementary step.
- **The elementary step holds for any source law.** If both response differences vanish almost surely,
  integrating the pointwise bound gives `|CHSH| ≤ 2`. A violation therefore gives a set of positive
  measure (not a single value of positive mass) on which `a` depends on `y` or `b` depends on `x`.
- **It is not touched by the review's counterexample.** In the review's continuous example
  `b = x ∧ y`, and the dependence set is the whole space. The counterexample targets U1's
  positive-mass-at-a-value I-sel predicate, which the step does not use.
- **Postselection.** The review's setting-dependent acceptance example is excluded by the requirement
  that a herald be a setting-independent function of `λ` (l. 521). Correct.

## 5. K-3 frame report and E1

- **§6** is now a report on the frame:
  - it is "not a native fact about OI models", disproves no input, and is not a *not available*
    outcome under SNR-1;
  - it separates the two coverage targets;
  - it gives the grounds correctly (per-observer finiteness from Main:42; family finiteness from
    AD-1(a); fixedness from reading (a));
  - it gives three readings tied to ledger Q1.

  The words "no execution in U1's sense" (l. 776) describe a program, not a verdict counted under
  SNR-1. Acceptable.
- **E1** is described as an explicit empirical input and is not used as raw-direct data. The agreement
  half is conditional on a named experiment class (owner question 4). Correct under §A.24, and
  soundness is no longer brought in through E1.

## 6. Nonblocking nits

- **N1 (§2.2 ll. 238–240).** The outputs `a₁, b₁` are functions of `(x₁, y₁, λ)`, so the
  representation `G(λ, ν, x₁, y₁, a₁, b₁)` is not unique. Under a Bell-local `a₁ = λ₀`,
  `κ = (λ, a₁)` can be written either way. Suggested reading: (U) and (N) are the cases where `κ` is
  almost surely a function of `(λ, ν)`, and (S) is the case where `κ` depends on `(x₁, y₁)` given
  `(λ, ν)`. L-3's statement is already in this "there exists a `G`" form. Its (a), "depends on the
  first use's outputs or on the remote first setting", then means "depends on the remote first setting
  given `(λ, ν, x₁)`".
- **N2.** For non-atomic laws, L-2, L-3 and the elementary step presuppose measurable response and
  update maps. This is automatic on finite configurations. Stating it once would make "needs no
  atomic source law" exact.
- **N3 (l. 527).** "Learns that setting … when it reads the whole `λ`". For a non-atomic `λ`, a finite
  observer (AD-1(a)) cannot hold the whole `λ`. The claim survives with a finite read: take `D_y`, the
  set where `b(0,y,λ) ≠ b(1,y,λ)`. Holding the two bits `1_{D_y}(λ)` and `b(0,y,λ)` before the use
  gives `x = b ⊕ b(0,y,λ)` on `D_y`, for any source law. Whether `φ` executes such a read is not
  shown, as before. Suggest replacing "the whole `λ`" with this two-bit read.

## 7. Checked / not checked

**Checked:**
- all R and M dispositions against r2;
- the line diff from r1 to r2;
- L-3's proof, conclusions, instances, scope and marking;
- the elementary step for non-atomic laws, against review 5909913170;
- the L-1 references;
- §6 and §10.3;
- the new citations.

**Not checked:**
- any literature on L-2 or L-3;
- performed sequential experiments;
- L-1's repair;
- parts of r2 unchanged from r1 beyond the r1 review.
