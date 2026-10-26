# Corpus consistency audit: horizon entropy, cosmological constant, prediction counts, Cabibbo, echoes

The owner directed this audit on 2026-10-26, as a dedicated corpus-consistency change separate from the black-hole
correction (#936) and the Introduction paper (#918). The rules:
- each flagged claim is independently verified before any edit;
- original wording is preserved in this record, with citations and a rationale for each correction;
- incorrect claims are distinguished from statements that only need a qualification.

`AUDIT.md` verifies, item by item at `main` `687e885b`, the overclaims first flagged by the Introduction's
applications audit (#918, `design/applications-audit/AUDIT.md` §9). For each item it gives:
- the source and original wording;
- the support behind it;
- the defect class: INCORRECT, OVERSTATED, NEEDS-QUALIFICATION or CONSISTENT;
- the status class, in the owner's six-class scheme (Derived, Conditional, Consistency, Postdiction, Forward test,
  Open), with the corpus's S/C/L/R/P/M/E class where relevant;
- the minimal replacement and its rationale;
- every mirror and paraphrase.

Lines that #936 edits are listed as owned by #936 and are not proposed for edit here.

`scripts/` holds the auditor's independent checks:
- `quarter_indep.py`: the Bekenstein–Hawking 1/4 as the ratio of two normalizations, with non-vacuity controls;
- `cc_indep.py`: the 10¹²² ratio against the de Sitter entropy as a dimensional identity;
- `cabibbo_cmp.py`: 1/(π√2) against the PDG 2025 values;
- `mirror.sh`: a book-to-FULL mirror lookup helper.

Paths written `S/…` refer to the session's scratch directory, which is not part of the repository. The PDG review
read for the comparison is identified in `AUDIT.md` by its digest and is not committed.

Status: verification audit, under independent review. No manuscript text is changed yet.
