- **`da295a1be51e7d7e2013307b85b0c5f44a9c897a`** (`claude/relc-select-predicted`, a single-parent child of `D`) is the
  execution tree less the result note. Its files and blobs:
  - this preregistration in its drafting revision, blob `a87695ae16f9ad7be0f21f6cb131f9fb1c3f95e0`, which differs from
    the revision at `F` only in this section;
  - `controls.py`, blob `8cafc140b519495d1687a5507846d320c3c3295f`;
  - the four modules, the reference blobs above;
  - `OIBridge.lean`, blob `f3b6b201cec58a6210b12a63aba7955c704f532e`;
  - the census, blob `1bc4d1f1c0037123bef545077125dc635ef0c3d8`.
- `delta(D, da295a1b)` is exactly those eight paths: the record directory's two files and the six execution paths. The
  modules differ from the amendment's (`f062fcff`) only in comments: `controls.py check f062fcff` fails exactly P, S8
  and C — that commit has no record directory, its module headers are the design headers and its census family the
  design family — and passes every other check, N1 to N3 among them.
- At that commit `controls.py check da295a1b`, run from the tree's own frozen `controls.py`, passes all 29 checks, and
  `controls.py verdict da295a1b` prints exactly `RELC-PARITY-PROVED`, `CTRL-SELECTOR-PROVED`,
  `POSITIVITY-SEPARATION-PROVED` and `RELT-NOT-DIMENSION-SELECTING-PROVED`.
@@RUN@@
- An earlier assembly, `5a8fd461`, differed from this tree only in the drafting revision of this file; its run
  37721238035 was cancelled before the Mathlib bridge finished and is not evidence.

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and these runs are design evidence, not
attestations.
