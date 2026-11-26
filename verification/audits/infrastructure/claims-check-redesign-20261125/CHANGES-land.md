# Landing correction: design example sentences moved to a control file (Issue #1565, PR #1567)

At `1a489caf`, the release gate step `claims` (`tools/claims_check.py`) reported six matches in
`DESIGN-r2.md` and `DESIGN-r3.md`. Each was an example sentence or phrase that the design text
quotes to illustrate a detection rule. Following the owner's decision (`amaybaum`,
2026-11-26T03:43:11Z; #1169 comment 7181966825): "Prefer moving the six example sentences into
dedicated control files rather than quoting them in code blocks. The purpose is to keep the
examples as explicit test data, separate from normative governance text, rather than relying on
Markdown formatting to distinguish them. Preserve all six examples and their intended test
coverage, independently review the correction, and rerun CI at the new exact head."

## Changes

- New file `work/design-example-sentences.json`. It holds the six examples EX-1 to EX-6 verbatim.
  Each entry records its id, source file, section and line at `1a489caf`, the rule it exercises,
  the outcome its source states, and the existing controls that carry the same content.
- `DESIGN-r2.md` §3.3 (EX-1) and §3.11 operations (iii) and (iv) (EX-2, EX-3), and `DESIGN-r3.md`
  §3.3 (EX-4), §6.1 (EX-5) and §7 (EX-6): each quoted example is replaced by a reference to its
  control id. No other text changed. Every other file in this directory is unchanged, byte for byte.
- `tools/claims_check.py` is unchanged and no exemption was added. The checker reads only `.md`
  files, so the JSON control file is not scanned.

## Checks

- `tools/claims_check.py` on `1a489caf` with these files substituted: OK, exit 0.
  `artifact_placement_check.py`, `duplicate_check.py` and `dependency_label_check.py --strict`
  also pass.
- Each example text occurs exactly once in its source document at `1a489caf`.
- `proto.r4.py --self-test`, `proto.r4.py --controls work/reviewer-heldout-W.json`,
  `run_r4.py compare` and `run_r4.py exitcodes <git dir> 4c3ad079…` give output byte-identical to
  `results-r4/`.

## Coverage

No runner reads the new file. The examples were never runner inputs. They were illustrations in
the design text, and the inputs that test the same behaviour are existing controls, all
unchanged:

- EX-1: `reviewer-heldout.json` X-P-05 (the same sentence ending "sets the detector calibration")
  and `controls_r2.json` R2-P-04.
- EX-2: `controls.json` P-KDEG-4 and `reviewer-heldout.json` X-P-10. No control contains the
  gerund form.
- EX-3: `controls.json` P-TQ-1 and P-TQ-6, `controls_r2.json` R2-P-04 and `reviewer-heldout.json`
  X-P-07. No control contains the forms "identical in every state", "unchanged in every state" or "insensitive
  to the state".
- EX-4: `controls.json` P-EPS-1, with N-EPS-1 as countercontrol.
- EX-5: `controls.json` P-KDEG-3, whose text begins with the quoted opening.
- EX-6: `r3-author-diagnostics.json` D-03 (byte-identical text), with `controls.json` A-TQ-1 and
  `reviewer-heldout-Y.json` Y-A-02.

This correction still needs independent review and a CI run at the new exact head.
