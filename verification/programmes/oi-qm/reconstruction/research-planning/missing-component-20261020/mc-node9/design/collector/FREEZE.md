# Freeze designation: C-SPH-1 complete-record checker

**Designation (owner, 2026-10-22, relayed in the coordinating session):**

> Review accepted. Freeze the preregistration unchanged at commit 27cbc2d7837a93800f7ff88da044382fdfec91ce.
> […] Proceed with checker implementation under this specification. Record the freeze designation separately,
> preserving the approved preregistration bytes.
> […] This approves the experimental specification; it does not certify the eventual result.

**What is frozen.** `CHECKER-PREREG.md` as it stands at `27cbc2d7`:
- sha256 `98418851b0bc5012e6cc9f13738921b7300ebf808143ccb644bae4052108b117`;
- its reference, `REFERENCE.md`, sha256 `1a961de9d0270836febcd7a82566a92d247b87eed7902c6ac243667a0c056dd5`.

Both match the checksum entries of that commit. Neither file is edited after this designation. The banner "draft for
owner review" inside the preregistration is part of the approved bytes; this file records its frozen standing.

**Frozen coverage (owner count).** 444 protocols:
- 340 sequence-and-terminal-read protocols;
- 72 probe protocols;
- 32 read-then-probe protocols.

Across the six relations this gives 2,664 preparation-pair/protocol cases.

**Reporting required.**
- the controls;
- independently computed TV brackets;
- completion probabilities;
- the coupling diagnostic D1.

The fixed work limits apply, and any UNDECIDED result is retained.

**After the checkpoint.** Numerical refinement of C-SPH-1 stops, and work returns to which assumptions OI actually
supplies.
