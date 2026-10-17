# Disposable storage: LOC-1 working material

This branch is storage, not development. It has no parent, shares no history with `main`, and is never merged.

It holds the LOC-1 drafting material that the control plane on PR #853 (head 026c00777d0fa09c72b82b7563b1238142b8fc29)
pins by sha256: the blinded preflight's scripts, inputs and outputs, the S16 completeness argument, the structured
expected result, and the six prior-disclosure files. Stage 1 of the round copies them byte for byte into the record
directory's `design/` and `prior/`, where K-design and K-prior check each against its pinned digest; this branch only
keeps them available until then.

- It is working material and provenance, not evidence (AGENTS §A.42): nothing may rest on this branch.
- The preflight evaluated no target object.
- `loc1-working-material/MANIFEST.json` lists every file with its size and sha256, and whether the preregistration at
  026c0077 pins it; the same content is the zip `loc1-working-material-20261017.zip`
  (sha256 b0f48176f62956ba8ec3acfcbabf23ee7d6725e9b8e35d0c5a42f7d9b2968269).
- Every file was scanned for token, key and private-key patterns before it was committed; there were no matches.
