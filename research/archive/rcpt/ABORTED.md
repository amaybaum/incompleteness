# CI-RECEIPTS-1: aborted on owner direction before F (2026-10-01)

PR #779 closed unmerged (closing comment 5937761910). main unchanged at 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a.

Branch heads at deletion:
- claude/network-tool-access-8jtdhm (PR head, draft preregistration only): 863402cead41ce07488bdc2d3765978afae673cb
- claude/ci-receipts-1-dev (disposable design branch): b6a39780a454cd97c9e4cf53654c46ad98926e6e
- local-only, never pushed: 5b413fdb (aggregate echo edit for the unrun reuse control)

Design runs (evidence only):
- 36900689313 decision job red (self-test committed bytecode; fixed)
- 36900831018 closure measurement: outside a42/, the probe reads dita_arc_exclusivity_probe.py (13 shards),
  dita_index_map_probe.py, dita_index_map_independent.py, act-41 measurements.json (paths only)
- 36903494687 live negative: push run as source rejected at check 1, mode compute; cancelled after the decision
- 36903422265 cancelled (superseded tool)
- 36903830057 computing source run at b6a39780: success, 15 receipts, closure audit clean; reuse never run

Local copies of the draft prereg, tool, controls and workflow edits remain in this directory.
