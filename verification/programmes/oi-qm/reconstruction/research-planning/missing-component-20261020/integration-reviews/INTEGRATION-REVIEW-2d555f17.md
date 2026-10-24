# Review of 0be12721..2d555f17 (PR #885, INTEGRATION.md, answering INTEGRATION-REVIEW-0be12721)

Verdict: ACCEPT. No blocking findings.

## 1. Obligation 2 (B1')
- E(x,y,r,z) = ((x,1,y)@q_Y, (x,1,r)@q_R, (0,0,z)@q_Z) is now the Y stage's *starting* carrier. This matches
  START-HERE.md l.82-86 ("The current outgoing X encoding is E(...)", followed by "the first outward Y step").
- Reset target (X,Y,R,Z) = (y⊕a, y, y⊕b, z), (a,b) = 00:10:11 = 5:3:2, z fresh and fair: verbatim match with
  composition/REPORT.md §4 (l.~90-96, "let a,b be the new X and R signs relative to y ... (y XOR a, y, y XOR b, z)"),
  START-HERE.md l.77 ("(newX XOR y, newR XOR y)=00,10,11" at 5:3:2) and calibration/README.md l.33 (Y row:
  (X XOR y, R XOR y), 00:5, 10:3, 11:2, 01:0). So a = X_new⊕y and b = R_new⊕y, consistent with all three.
- No conflict with obligation 3. Obligation 2 fixes only the decoded law and leaves the outgoing encoding open;
  obligation 3 separately asks for an encoding the next instrument accepts natively, without a history-reading decoder.
  B1' is resolved.

## 2. Other edited phrases
- Read-reset row: "input-independent random permutations (XOR masks among them) reach 7/30, also when validity is
  required, and a non-reversible discard-and-resample reaches 0". This matches READ-RESET-REVIEW E1-E3 (l.60-65):
  Birkhoff doubly stochastic maps, XOR masks a subset, 7/30 over the hidden inputs, with X+ validity and against the
  menu, and discard-and-resample reaching 0 trivially. Accurate.
- "readout of the selected sign for a setting programmed into the initial apparatus": this matches the
  NATIVE-SELECTOR-REVIEW title and l.213 text and closes the NB-5 remainder. Accurate.
- "an abstract staged-disclosure contract, whose recorder and reset are supplied abstractions": this matches the native-Y
  SYNTHESIS l.35 ("Recorder and reset are supplied abstractions, not native implementations") and l.81 ("proves an
  abstract alternative contract"). Accurate.
- NI README: "PREREG.md was first committed together with the code". PREREG.md, PREREG.sha256 and
  instrument_checks.py were all added in 455eb092, so the sentence is true and resolves the NB-1 nit.

## 3. Checksums and scope
- `sha256sum -c` was run on an archive of 2d555f17. integration-reviews/SHA256SUMS: 5/5 OK, including the new
  INTEGRATION-REVIEW-0be12721.md. mc-node9/design/native-instrument/SHA256SUMS: 6/6 OK, including the new README digest.
- The diff touches exactly 5 paths: INTEGRATION.md (M), INTEGRATION-REVIEW-0be12721.md (A, the review being answered),
  two SHA256SUMS files (M) and the NI README (M). Nothing else changed.

Non-blocking: none needed.
