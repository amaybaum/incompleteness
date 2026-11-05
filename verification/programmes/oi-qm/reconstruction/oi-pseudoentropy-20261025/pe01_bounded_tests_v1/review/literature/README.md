# PE-01 literature tags (amendment A3)

Literature tags for PE-01's two in-scope results, assigned under `../../amendments/A3-literature-tags.md`, whose
rule was fixed before any of this literature was read. Tags bear on no verdict. The verdicts, measurements and the
A2 mechanical tags are unchanged, and nothing in `../../results/` was re-run or edited.

## Files

- `TAGS-r2.md`: the annex. The tags in force.
- `TAGS-r1.md`: r1, the object of the first independent review, byte-identical to what it read
  (sha256 `ac3cdffed97efe2b7fa1b7b1279cfdaee76ba311df66ed767843bf325a93eb2e`).
- `REVIEW.md`: independent review of r1. Verdict: ACCEPT WITH CHANGES.
- `RECHECK-r2.md`: independent re-check of r2. Verdict: ACCEPT WITH NITS. It read r2 at sha256
  `95b644bc075c1a5a…`; `TAGS-r2.md` as committed adds its nits RN1 (the linear-prediction argument for the plin K0
  rows) and RN4 (the status line), and nothing else.
- `check/linear_rows.py`: the annex author's check of the linear-statistic rows, from PLAN definitions only, with no
  repository imports. `check/out_n3_6.txt` and `check/out_n3_7.txt` are its outputs for `n ≤ 6` and `n ≤ 7`
  (`python3 -I check/linear_rows.py 6` and `… 7`). The reviewer reproduced the `n ≤ 6` output byte for byte.
- `review-probes/`: the reviewer's independent checks cited in `REVIEW.md` and `RECHECK-r2.md` (`aghp_check.py`,
  `b3w_check.py`, `plin_bf.py`, `qcheck.py`, `pages.py`). `plin_bf.py` imports `aghp_check.py` from this directory.

## Summary of the tags

- **The COUNTEREXAMPLE cell** (`G_clk`, n = 5, `emb_m2_all`, K = 7) is covered in kind, not in its parameters, by
  Gomułkiewicz–Kutyłowski–Wlaź 2006 (a clock-control fault attack on the shrinking generator: separately clocked,
  rerun from the same state, state recovery rather than prediction; an unimplemented outline).
- **Passive horizons of linear statistics** on `G_lin`, `G_lin_sib` and 𝔉_lin are covered in kind by AGHP 1992's
  mechanism. Their values are not stated there, so none is COVERED-literature.
- **No candidate-NEW tag** is assignable while the works listed as unread remain unread.

## Not retained

- The downloaded papers and their text extractions (third-party documents). Each is identified in `TAGS-r2.md` by
  URL and the sha256 of the file read, with the page of every passage relied on.
- The working locations the records cite (`pe01lit/`, `pe01lit_check/`, `revlit/`) are the annex author's and the
  reviewer's scratch directories: `pe01lit_check/` is `check/` here, and `revlit/probe/` is `review-probes/`.
