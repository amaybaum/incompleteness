# Pilot round PILOT-SB1 — the V3 lifecycle on a protected sandbox target: PREREGISTRATION

This is the preregistration of pilot round `PILOT-SB1`, which verifier round `V3-7` runs. The pilot
is published to the sandbox target branch `v3-sandbox/main` and never to `main`. Its execution
adds one file, `verification/infrastructure/v3/pilots/PILOT-SB1-execution.md`, and its record
directory's result note; it changes nothing else.

The round declaration:

```v3-round
round PILOT-SB1
kind non-sealing
record-directory verification/infrastructure/v3/pilots/round-pilot-sb1/
```

The governed paths:

```v3-governed-paths
record AM verification/infrastructure/v3/pilots/round-pilot-sb1/
record AM verification/receipts/PILOT-SB1.json
execution A verification/infrastructure/v3/pilots/PILOT-SB1-execution.md
```

The round is complete when its final receipt commit is published to `v3-sandbox/main` by a
non-force update. It has no guard clause, manifest record, seal record or certificate.
