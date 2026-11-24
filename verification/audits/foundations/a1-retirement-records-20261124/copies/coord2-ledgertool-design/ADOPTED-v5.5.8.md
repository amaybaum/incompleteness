# Design v5.5.8 adopted (owner decision, 2026-11-24)

Authoritative design: DESIGN-v5.5.8.md, sha256 f531948147b3638c5ad567f5ccf0eedfd04650a30be9fd0a9f2084aa13a77ad2.
Frozen base, kept unchanged: DESIGN-v5.5.3.md, sha256 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379.
Basis: review-v5.5.8/review.md (5cd26d441c9302333861790f024f2b433d0e2749bbcdd90e3992452d3f1b21e9), ACCEPT;
earlier reviews review-v5.5.4 .. review-v5.5.7.

Conditions (owner): DI-1 and DI-2 exactly as in v5.5.8, no further rule changes; Z9h duplication accepted
as a known non-blocking historical issue, not modified; adoption of the design is not acceptance of the
implementation. Authorized next: implement v5.5.8 (DI-1, DI-2, one review verdict per added ledger event,
TR54-TR70 and LN1-LN12 as executable tests), full rerun, fresh independent review at the final commit
covering the whole approval and acceptance chain with real mutation tests. Not authorized: trial dispatch,
freeze change, merge to main, push.
