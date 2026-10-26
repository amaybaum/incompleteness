# Diff-only confirmation: PR #938, `2b660c93..28c7b2bf`

**Verdict: ACCEPT WITH NITS.** Findings 1 and 2 of my review are fixed correctly, and the ledger re-affirmation is sound. The only nits are stale counts in the audit record `SEARCH.md` and the PR description. No manuscript text is affected.

Everything was read-only. I fetched the branch from `S/cc2/wt`; `origin/fix/f29-followups-20261026` points to `28c7b2bf`, and its single parent is `2b660c93`. I took an archive snapshot in `S/f29b/snap2` and extracted the audit directory with `git show`.

## Checks

1. **Explainer:373 — the new sentence is correct.** It reads: "No two of representability, memory and P-indivisibility are equivalent." All three pairs fail:
   - **Representability vs memory.** Every finite law is representable (S⟺D⟺Q_fb), and Markov laws exist. A diagonal Hamiltonian is one example.
   - **Memory vs P-indivisibility.** The XOR family has 1 bit of conditional memory and its matrix family factors through Λ = I.
   - **Representability vs P-indivisibility.** A diagonal Hamiltonian is representable with T(t) = I, so it is P-divisible.

   The sentence is now consistent with the S⟺D⟺Q_fb biconditional asserted earlier in the same paragraph.
2. **Explainer:353 — now matches Main's (iii).** The parenthetical reads "(for some accessible order $k$, on each finite accessible horizon $K \geq k+1$, with the readback at $k$)". That is ∃k ∀K≥k+1 with C1, C3 and C4 and readback at k, with C2 outside, as at Main:522. It is neither stronger nor weaker.
3. **Ledger re-affirmation — sound.**
   - **The fingerprint change was required and is the right value.** At `2b660c93`, `coverage_check` fails with exactly one error: "STALE … MAIN:L-accessible-backflow-from-readback (1bf64869e7938d80 -> afbdefe369fdd5a0)". At `28c7b2bf` it passes: "OK (128 canonical statements, 19 unattached checkers)". The base `c967d6a9` also passes, so the failure came from this PR.
   - **The ledger diff is that one fingerprint line.** The line number (167), the assumptions, the check, the level P and the delta "no Lean statement" are unchanged.
   - **The probe mapping still holds.** `c4_backflow_probes.py` indexes the past as `(x0,)` = X_{<1} and the present as c = X_k. It takes p0 = min of the joint weights Pr[X_{<k}=a, X_k=c], which is the corrected convention. It passes.
   - **The lemma is still not in the kernel.** There are no Pinsker or readback-lemma hits under `verification/lean*`, and `verification/lean*` has a zero-line diff.
4. **Mechanics — all pass.**
   - These report OK: `coverage_check`, `claims_check`, `voice_check`, `staleness_check` (13 matched), `duplicate_check` and `artifact_placement_check`.
   - `mirror_check` reports 0 lines absent. `architecture_check` reports 259 invariants and 0 violations.
   - **Explainer `.tex`.** Regenerating it with pandoc gives a file identical to the committed one, apart from the build stamp. The stamp equals the sha256 of `Explainer.md` (`759f3291…`).
   - **Explainer `.pdf`.** It has 69 pages, unchanged, and contains both new sentences.
   - The §A.32/§A.33 scan of the 2 added manuscript lines found 0 hits.
   - The drafter's probe passes 12/12, and my retained probe passes.
5. **Nothing else changed.** The diff touches eight files, and each one is accounted for:
   - Explainer `.md`, `.tex` and `.pdf`;
   - CHANGE-NOTE and SEARCH;
   - `review/REVIEW.md`, byte-identical to my review;
   - `review/probe/review_probe.py`, byte-identical to my probe;
   - one line of `LEDGER.json`.

   No other manuscript file, mirror, or Lean file changed.

## Nits (record only, no manuscript change)

1. **Stale counts in `SEARCH.md`.** `:353` was removed from the C/slogans table and noted only in an appended paragraph. These counts were not updated:
   - the slogans header "(12)" should be 11;
   - "## C: correct as stated (50)" and the counts table should say 49;
   - "## O: outdated, corrected (7 lines; …)" and the counts table should say 8;
   - the total of 84 stays the same.

   Ideally the `:353` row also moves into the O table. The PR description's "7 are outdated and corrected, 50 are correct" is stale in the same way. (§A.30: after an inventory change, grep the totals.)
2. **Math notation in the Explainer.** `:353` writes `$k$` and `$K \geq k+1$` in math mode, while `:373` uses plain "k" and "K ≥ k+1". This is cosmetic, and no change is needed.
3. **A gap in my own first review.** It did not run `coverage_check`, which was failing at `2b660c93`. CI caught it, and the fix here is correct.
