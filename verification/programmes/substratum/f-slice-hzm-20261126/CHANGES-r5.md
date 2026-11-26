# F-SLICE-HZM: changes from REPORT-r4.md (r4) to REPORT-r5.md (r5)

r4 is `REPORT-r4.md` at `21ba94c3ac19139885b7de4891e7234c7d4c84d1`, kept unchanged with r1–r3. The review is the independent delta review of r4, posted verbatim on PR #1611, comment 7201689426 (posted from the account amaybaum, created 2026-11-26T19:31:52Z), verdict ACCEPT WITH NITS, with one nit. The coordinator's instruction directed applying it after a hand check. The change is textual: no derivation, witness, classification or outcome changes.

| Finding | Change in r5 |
| --- | --- |
| Nit: the O_h example in §3.4 gives a zero quadratic form | The example i(P_{k_0} − P_{−k_0}) is replaced by i(P_{k_0} − P_{−k_0}) J_F, after a hand check. K = i(P_{k_0} − P_{−k_0}) is real, antisymmetric, inversion-odd, and commutes with the translations, F, Ω and J_F, so it is g-antisymmetric. J_F is g-antisymmetric because it is tamed and ω-compatible. Their product is g-self-adjoint, real, inversion-odd, and commutes with F and the translations. §3.4 states this, and states that K alone gives a zero quadratic form |

Consequential edits:
- the header, the revision note and the r4 pin;
- §1's pass count;
- §9's Pass 8 (textual; no classification change);
- §10 N-7;
- §12's provenance rows: comment 7201689426 and commit `21ba94c3`.
