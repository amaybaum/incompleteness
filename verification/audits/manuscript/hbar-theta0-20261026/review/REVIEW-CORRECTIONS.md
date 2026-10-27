# Review of the #939 corrections (4ed4c6e6..2cb44824)

This is an independent, read-only review at exactly `2cb44824`.
- **How I read the tree:** checks ran on a `git archive` snapshot (`S/hbar-theta/rc/head`) and on `git show` extracts. No worktree was created and nothing was committed. Git ran with `-c gc.auto=0 -c maintenance.auto=false`; Python with `python3 -I`.
- **Where this file lives:** it is written to scratch rather than into a worktree, because I was not given a writable worktree for the branch.

## Verdict: REVISE

Of the six items checked, five pass in full. One is a required fix: the two Substratum Stage-3 sites the coordinator flagged, plus the proof line between them, need the O1-A consistency fix and one ledger re-affirmation (F1 below). The fix is a small mechanical edit; with it applied verbatim, the verdict is **ACCEPT**.

***

## 1. The diff matches DECISIONS — PASS

- **Method.** I applied the DECISIONS set mechanically to the `b64919cd` sources: every no-decision edit plus O1-A, O2-a, O3-b, O4-a, O5-a, O6-A and O7-a (`S/hbar-theta/dec/sim`, from `gen/entries.py`). I then compared the result with `2cb44824` file by file.
  - `4ed4c6e6` equals `b64919cd` in `papers/` and `book/`, so the comparison is valid.
- **Result.** Every `papers/*.md` and `book/*.md` is byte-identical to the simulation except four files: FULL.md, ch06, ch07 and SM. Their differences are exactly the following, and nothing else:
  - the O4 qualification at SM:940 and at ch06:179 [FULL:1705];
  - the O6 qualification at ch06:192 [FULL:1718];
  - R1 at ch06:179 [FULL:1705];
  - R2 at ch07:8 [FULL:1887].
- **FULL mirror.** Lines added and removed in FULL equal the union of the chapter diffs as multisets: 61 added and 61 removed. `mirror_check` reports 0 lines absent.
- **Outside `papers/` and `book/`.** The only other changes are the regenerated `.tex`/`.pdf`, the record files and `LEDGER.json` (one fingerprint).

## 2. The qualification adjustments — PASS

**O4, SM:940.**
- The new text opens "In this linear-response model, with $\kappa \approx -35$ and $\lambda_E/\lambda_{A_1} = 0.22$–$0.24$, …".
- It states the interval and "…the interval is conditional on that response model, its sensitivity coefficient and the range of $\lambda_E/\lambda_{A_1}$, and is not a model-independent exclusion."
- It ends: "A second-order lepton-Yukawa loop, of order $10^{-6}$, is compatible with the interval for either sign, by a factor of about two; the comparison is not decisive, and the loop estimate is not a confirmed prediction."
- Each of the owner's three points is met exactly. Nothing is overstated, and the interval and margin are kept, so nothing is understated.

**O4, ch06:179 [FULL:1705].**
- The new text reads "…at 95% confidence, conditional on the linear response of $\theta_0$ to the dressing (sensitivity coefficient $\kappa \approx -35$, with $\lambda_E/\lambda_{A_1}$ in the range above) rather than as a model-independent exclusion; a lepton-Yukawa loop of order $10^{-6}$ is compatible with that interval for either sign, by a factor of about two, but is not a confirmed prediction (SM §7.2)."
- It meets the owner's words.
- Nit N1: "constrains it to … rather than as a model-independent exclusion" is slightly ungrammatical. A suggested wording is in §8.

**O6, ch06:192 [FULL:1718].**
- The new text reads "— one possible explanation of the pattern is electroweak-scale renormalization-group running …, in which the larger $m_\tau$ Yukawa would receive proportionally smaller logarithmic corrections …; the agreement of the mass ratios does not by itself establish that running."
- It frames the running as a possible explanation, not a demonstrated mechanism, and says the agreement does not independently establish it, as the owner asked. "By itself" is equivalent to the owner's "independently".

## 3. Residue sites — PASS

**R1, ch06:179: "the empirical match at 0.02 %" → "0.001 %".** This is θ₀'s normalization match, so the correct figure is 0.001 % (SM:903; recomputed 0.00114 %). Correct.

**R2, ch07:8: "0.02 % to 1.2 %" → "0.0003 % to 1.2 %".** I checked it against the SM §7.6 table at `2cb44824` (SM:1259–1280).
- **Tightest entry.** The percent-quoted measured comparisons are:

  | Entry | Figure |
  |---|---|
  | Koide Q | 0.0003 % |
  | θ₀ | 0.001 % |
  | m_μ | 0.002 % |
  | m_e | 0.003 % |
  | λ | 0.04 % |
  | Q_down | 0.15 % |
  | m_b | 0.9 % |
  | m_t | 0.9 % |

  The couplings' "< 0.1 %" are fits and are excluded by "measured comparisons". Koide Q is therefore the tightest.
- **The figure for Q.** From the PDG 2024 masses, Q = 0.6666645 ± 0.0000051, and (2/3 − Q)/(2/3) = 3.3×10⁻⁶ = 0.00033 %, so "0.0003 %" is right.
- Nit N2: a reader using the displayed six-digit value 0.666664 gets 4.0×10⁻⁶, i.e. 0.0004 %. Optionally display "0.6666645" at SM:1267, ch06:302 and the O7 sites.

## 4. Substratum Stage-3 sites — REQUIRED FIX (F1)

**Why they fall within O1-A.**
- **Substratum:188 (Lemma 23.0)** concludes "…and the same Stage-3 value of $\hbar$." Its hypotheses (E1–E7, A1–A6, M1, mixing, Lemma 24.1) do not include H-slope, which Stage 3 now requires (Substratum:180/184). Its wording also contradicts the adjacent Stage-3 output, which now reads "it fixes only $\epsilon/\sqrt{\sigma}$, not the value of $\hbar$" (Substratum:178).
- **Substratum:190 (Lemma 23.0's proof)** says "Stage 3 fixes the same gap-equation value $\hbar=c^3\epsilon^2/(4G\sigma)$".
- **Substratum:194 (Theorem 23's proof)** says "Stage 3 uniquely fixes $\hbar$". That is stronger than the theorem statement, which O1-A has already made conditional.

All three state more than their hypotheses support. They fall within O1-A: Lemma 23.0 is the uniqueness lemma Theorem 23 rests on, and the proofs restate Stage 3.

**Exact replacements** (papers/Substratum.md; not mirrored in FULL):

```text
Substratum:188
OLD: and the same Stage-3 value of $\hbar$.*
NEW: and, conditional on H-slope with the horizon and frame conditions of [GR §3.2], the same Stage-3 action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$.*

Substratum:190
OLD: Stage 3 fixes the same gap-equation value $\hbar=c^3\epsilon^2/(4G\sigma)$;
NEW: Under H-slope, Stage 3 fixes the same gap-equation relation $\hbar=c^3\epsilon^2/(4G\sigma)$;

Substratum:194
OLD: Stage 3 uniquely fixes $\hbar$.
NEW: Stage 3, conditional on H-slope, fixes the relation $\hbar=c^3\epsilon^2/(4G\sigma)$.
```

Each OLD string occurs exactly once in its line at `2cb44824`.

**Ledger.** I applied the three edits to a copy of `2cb44824` and ran `coverage_check`. It reports exactly one stale entry, `SUBSTRATUM:L-23.0`: `"fingerprint": "11c8a93fc88cf91b"` → `"fingerprint": "fd8439a8bd3f7ee1"`. Re-affirm that entry in the same commit; its kernel "GAP", delta "not formalized" and assumptions "see the statement" still hold. The proof edits move no fingerprint, so T-23 stays at `e6bf53b0d2ae0955`. Rebuild Substratum.tex/.pdf.

**book/README:98** reads "gap equation deriving $\hbar = c^3 \epsilon^2/(4G\sigma)$". It states the relation, not the value, so it is acceptable as written, as it was CONTEXT-OK in the audit. No change is needed.

Other "Stage 3" mentions need nothing:
- ch02:110 now carries the condition, and ch02:114 refers to it;
- Substratum:140 and :172 "Status: Theorem" concern Stages 1 and 2, not the ħ step.

## 5. Ledger — PASS

`SUBSTRATUM:T-23` changes only its fingerprint, `b69a16c2e08bd93f` → `e6bf53b0d2ae0955`, and `coverage_check` at `2cb44824` is OK (128 statements).
- **Mapping:** still Theorem 23 at Substratum:192.
- **Level:** still kernel "GAP", because the statement gained a hypothesis and the formalization status is unchanged.
- **Delta:** still "not formalized".
- **Assumptions:** "see the statement" now correctly includes H-slope.

## 6. Re-grep, Category A count, PDFs — PASS

**Stale figures.** Across `papers/*.md` and `book/*.md`, excluding FULL, there are 0 hits for:
- `0.2227`, `0.222220`, `1776.86`, `105.652`, `0.51096`, `0.666661`;
- "seven independent relations", "theorem *within*", "deriving $\hbar$" without the relation;
- θ₀ or Koide angle with 0.02 %.

The survivors are all intended:
- `105.74` at ch06:190 is kept under O6-A with its structural-closure label.
- "the sharpest empirical agreement" at ch06:12 now carries "in relative precision" (O5-a).
- `8 \times 10^{-5}` at ch06:157 is the Jarlskog value, which is unrelated.
- "value of ħ" survives at Substratum:178, appendix-b:173 and ch07:36 as "not the value of ħ" or "not an independent determination …". At ch02:134, ch03:80, ch07:22 and ch07:124 it means gauge invariance ("the same value"), which is CONTEXT-OK.
- The exception is Substratum:188, which is F1.

**Category A, recounted independently.** ch06:320 lists λ, A, |V_cb|, m_d/m_s, sin²θ₁₃, Q, θ₀ and λ(M_Pl) = 0: **8**. The text says "These eight relations", and ch06:332 says "eight Category A rows, one for each relation". The §6.8 table has 8 rows tagged **A**. All consistent.

**PDFs** (`pdftotext`):
- **SM.pdf (146 pp.):** contains "In this linear-response model, with 𝜅 ≈ −35 and 𝜆𝐸/𝜆𝐴1 = 0.22–0.24 …" and the §7.6 row "Koide 𝑄 2/3 0.66667 0.666664 0.0003% C".
- **FULL.pdf (556 pp.):** contains "one possible explanation of the pattern …", "eight Category A rows, one for each relation" and "0.0003% to 1.2%".
- **Substratum.pdf (52 pp.):** contains "Status: Conditional on H-slope …".
- No "??" or unresolved references in any of the three. Every `.tex` source-sha256 stamp matches its `.md`.
- `claims_check`, `voice_check`, `duplicate_check` and `lean_manuscript_census` all pass at `2cb44824`.

***

## 7. Required change

- **F1.** Apply the three Substratum edits in §4 (lines 188, 190 and 194), re-affirm `SUBSTRATUM:L-23.0` as `fd8439a8bd3f7ee1`, and rebuild Substratum.

## 8. Nits (optional)

- **N1** (ch06:179 [FULL:1705]): replace "…at 95% confidence, conditional on the linear response of $\theta_0$ to the dressing (sensitivity coefficient $\kappa \approx -35$, with $\lambda_E/\lambda_{A_1}$ in the range above) rather than as a model-independent exclusion;" with "…at 95% confidence, conditionally on the linear response of $\theta_0$ to the dressing (sensitivity coefficient $\kappa \approx -35$, with $\lambda_E/\lambda_{A_1}$ in the range above), not as a model-independent exclusion;".
- **N2:** optionally display Q as 0.6666645 at SM:1267, ch06:302, ch00:77 and glossary:97, so the quoted 0.0003 % is reproducible from the displayed value.
