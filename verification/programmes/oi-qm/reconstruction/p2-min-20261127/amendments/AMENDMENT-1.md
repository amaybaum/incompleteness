# P2-MIN plan, Amendment 1: single-principle, multi-gap question (owner steer)

**Status.** Committed after `PLAN.md` (`a86d6bea`) and before `REPORT.md`. `PLAN.md` is unchanged.

**Owner steer**, relayed by the coordinating session (2026-11-27): "Prioritize constructive
mechanisms over further classification. In particular, investigate whether one independently
justified physical principle could address multiple outstanding gaps simultaneously, rather than
introducing a separate assumption for each gap." The relay adds: at least one question on whether a
single candidate principle resolves two or more gaps non-circularly, and ranking by the number of
gaps resolved non-circularly, not by rows classified.

**Chronology disclosure.** Between the plan commit and this amendment the writer had read three
sources:
- MECH-1's Proposition AS;
- the C-ENV screen's Node 10 and D1;
- lane 2's Theorem 1 (`complex-carrier-20261126/REPORT-r2.md`).

The writer had also formed, without writing them, provisional readings of the cells of PLAN §3. No
verdict was written before this amendment. Two additions below come from that reading:
- the CS entry rests on lane 2's Theorem 1;
- candidate x6 was considered because of it.

## 1. Gaps added

PLAN §3's gap list (NC, SET, O-RET) is extended. SET is read as "in-world settings **or meter
supply**" (SET/M); meter supply is the supply of fresh, readable ancilla states for monitoring.

| Gap | Statement |
|---|---|
| CS | a complex structure on the observer-level description, determined by native structure rather than posited. The H-PF bridge (SM's φ is the J-linear positive-frequency field of Theorem 5) is SMD-adjacent and outside scope |
| OBS | observer emergence: a rule-fixed criterion selecting a persistent, coupled, access-restricted partition (OBS-EMERGE (E0)–(E3)) |

## 2. Candidates added

| ID | Candidate principle | Source |
|---|---|---|
| x6 | **KVP (Kähler-vacuum principle):** the observer's maximal-knowledge background is the F-stationary Gaussian law, on the observer-level real lift, with covariance proportional to g_J⁻¹ = ω(·, J_F ·)⁻¹, where J_F is lane 2's canonical complex structure. It is one principle that would bear on CS, SET/M and O-RET at once | proposed here as the strongest single-principle candidate found in the corpus |
| x7 | a posited invariant law of intermediate entropy density | C-ENV D1 option (a) |
| x8 | an added structure supplying a root of t² − Xt + 1 (a substratum-level frequency split) | C-ENV D1 option (b) |

D1 option (c), sublattice translation invariance, was not examined by C-ENV. It stays outside the
covered class and is named as uncovered; it is not a cell.

## 3. Preregistered N/A cells (reasons fixed now)

- (x4, CS), (x4, O-RET), (x4, OBS): x4 changes only what is read.
- (x5, CS), (x7, CS): a background law fixes no complex structure.
- (x5, OBS), (x6, OBS), (x7, OBS), (x8, OBS): no in-scope candidate proposes a partition-selection
  criterion. OBS-EMERGE G4 places the only known route in localized nonlinear structures, which is
  C-NL territory.

## 4. The multi-gap question and the ranking

- **Q-MULTI.** Does any single candidate x ∈ {x4, …, x8} receive RESOLVES on two or more gaps
  among CS, NC, SET/M, O-RET and OBS?
- **Ranking.** Candidates are ranked by the number of RESOLVES cells. Ties are broken by the
  number of OPEN cells, which counts gaps still possibly resolvable. Rows classified do not count.
- **CS inside 𝒞.** A CS verdict for "inside 𝒞 + LIFT" is reported. It also serves as a further
  RESOLVES-capable control:

| ID | Input | Required output |
|---|---|---|
| K7 | inside 𝒞 with the real lift (LIFT, carried as an open bridge, SM:232), gap CS | RESOLVES, conditional on LIFT (lane 2 Theorem 1: tamed F-commuting J exists iff E positive definite, then unique, J_F) |

The decision rule, Q0, the outcomes and the stopping bounds of PLAN §4–§7 are unchanged and apply
to the added cells.
