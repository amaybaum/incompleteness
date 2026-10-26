# Explainer audit, re-verified at `main` `687e885b`

**Status: independent re-verification of `../EXPLAINER-AUDIT.md`.** Verdict: HOLDS WITH CORRECTIONS.

- `REVIEW.md`: the re-verification. The audit's measurements reproduce at its own commit `c91bf5dd`. At `687e885b`
  its two headline findings are fixed (the Explainer's status note; the D-gauge material, now in book Appendix B.7),
  its stale-content list stands at shifted lines, and it has three errors (the C₄-ring claim it carried forward, a
  §A.34 overclaim, and a missed every-horizon statement at Explainer:373, recorded on #931). It lists the
  Explainer-only content and every file a replacement must change in the same commit.
- `tools/`: the reviewer's helper scripts (`shingle.py`, `shingle_range.py`, `eqs.py`, `mapline.py`, `c4ring.py`);
  each takes a directory holding `Explainer.md`, `book/*.md` and `papers/*.md` from one commit.
- `outputs/`: their outputs at both commits (`*-c91.txt`, `*-687.txt`).

The corpus copies the scripts were run on are not retained; they are `git archive` extractions of the two commits.
