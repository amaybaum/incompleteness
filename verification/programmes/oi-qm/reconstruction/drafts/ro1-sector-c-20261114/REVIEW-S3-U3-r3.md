# Focused check of S3-U3-r3 against the L-2/L-3 review (independent, non-author)

**Objects.** In `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, at
`dbb1c154` on `research/ro1-sector-c-1169-20261114`:
- `S3-U3-r3.md`;
- `RESPONSE-U3-L2-L3-REVIEW.md`;
- `README.md` (two added rows).

**Integrity of the inputs.**
- r2 is unchanged at `dbb1c154`: blob `34ffe552`.
- The cited review, `REVIEW-U3-L2-L3.md` at `8a48c795`, has blob `3a81d18d`. It is byte-identical to
  the reviewer's file.

**Reviewer.** The non-author reviewer of L-2 and L-3. Read-only, hand checking only.

**Verdict: ACCEPT.**
- R1–R3 are RESOLVED.
- The r2 → r3 diff holds only those corrections, the recorded scope notes, O2, O4, O5 and O6, and
  their necessary consequences.
- The citations are exact.
- L-2 and L-3 stay labelled proposed, and every use stays marked conditional.
- Two nonblocking nits remain (N1, N2).

***

## 1. Required items

| Item | Status | Where in r3 |
|---|---|---|
| R1, hypotheses at "every … realization" sites | RESOLVED | RQ-REU (ll. 384–389), RQ-UPD-1 (ll. 395–400), §4.1 (ll. 499–508), §4.4 (ll. 622–624), U3-1 (l. 902), §10.2 RR-1 (l. 982), §10.3 two rows (ll. 998–999), CQ-2 (ll. 1019–1022) |
| R2, prior art of L-2 | RESOLVED | §1 (ll. 187–193); §5.1 Prior art (ll. 640–645); U3-1 reclassed ELABORATING; §10.6 (l. 1073) |
| R3, wing-local readback; designed realizations | RESOLVED | §5.2 Scope (ll. 791–800); RQ-UPD-2 (i) and its closing sentence (ll. 418–420, 430–432); U3-2 (l. 903); §10.1 RQ-UPD row (l. 952); §10.6 (ll. 1068–1069) |

**R1.** Each site now names (k1)–(k5) and singles out (k3) and (k4).
- RQ-UPD-1 lists (k1), (k3), (k4) and (k5) and omits (k2). That is correct: (k2)'s failure is the
  conclusion.
- RQ-REU states that `Δ₄` alone supplies neither (k3) nor (k4), and that M-PR5 lies outside (k3).
- The (k4) exposure is stated as U3 §1 requires (S5 not assumed; Main:416–423).

**R2.** The Valentini paragraph matches what Valentini's text supports: the transition-set proof; a
signal "in general"; theories reproducing quantum theory in equilibrium. It also states the three
sharpenings correctly.

**R3.**
- The construction is transcribed exactly, and its claim (record law (1) times (9); both histories
  blind to the remote settings) is what I verified.
- The sentence "it does not require a cross-wing or hidden-sector update. It does not show that any
  model executes such an update" stays inside what L-3 gives.

## 2. Diff r2 → r3

The hunks fall exactly at the writer's listed lines: 1, 3–11, 23–28, 91–92, 187–193, 384–425,
499–508, 622–653, 720–800, 902–903, 952, 982, 998–999, 1019–1022 and 1068–1073. Each maps to one of
the following:
- an R item;
- a recorded scope note (measurability in (k1); L-3 needs no (k1) by dilation; (b) needs only
  `|CHSH| > 2`);
- O2 ("or" to "and"), O4 ((k3′) named at RQ-UPD-2 and U3-2), O5 or O6 (U3-2 to ELABORATING);
- the status lines that record the review's verdicts.

No unlisted substantive change was found. O1 and the widening part of O3 are declined with reasons,
which is acceptable for optional items.

## 3. Citations

- **Valentini.** A. Valentini, "Signal-locality in hidden-variables theories", Phys. Lett. A **297**,
  273–278 (2002), doi:10.1016/S0375-9601(02)00438-3, arXiv quant-ph/0106098. Exact.
- **Kleinmann et al.** M. Kleinmann et al., "Memory cost of quantum contextuality", NJP **13**, 113011
  (2011), arXiv 1007.3650, App. A. Exact. The relation is stated as an analogue, not as the source of
  L-3.
- **Popescu.** S. Popescu (1995) is recorded as not accessible. Correct.
- **Line 92.** The note says the literature was read first-hand by its reviewer, not by the writer.
  Accurate.

## 4. The narrowing, and Main:480–482

- **Line 952.** "No executed or native source-update process on record" is correct at U1's levels.
- **The comb.** Main:480 states the intervention-dilation theorem for a finite action alphabet and a
  finite-horizon action-labelled family. Main:482 is its construction, which reads context-indexed
  hidden coordinates `u_c` with `c = (x_{≤k}, a_{≤k})`, so its responses are history-indexed. r3
  cites it as "represents any finite action-labelled law with history-indexed responses, at K-4
  standing: representable only (U1:819)". U1:819 lists "the comb (Main:482)" under K-4. Correct.
- **Line 1068.** "An executed or native deterministic realization … (a designed one is elementary)"
  is correct.

## 5. Labels

- **Header (ll. 23–28) and §§5.1–5.2.** Both record "PROVED AS STATED" and keep "proposed" until the
  owner decides.
- **Uses.** Every use keeps "conditional on L-2" or "conditional on L-3".
- **No promotion.** No conclusion is moved to established.

## 6. Nonblocking nits

- **N1.** Owner question 2 (ll. 1101–1102) still asks whether to route L-2 and L-3 for review and to
  authorize a literature check, and both have now been done (#1169 c.6892563291). The response keeps
  r2's wording on purpose. A one-line note that the question has been answered would avoid a stale
  question. §10.5's "(proposed lemmas, for review)" (l. 1035) remains accurate while the owner's
  decision is pending.
- **N2.** Line 952 could add that Main's comb is a single-process (centralized) realization, not a
  wing-separated one. Its K-4 standing already prevents any overreading.

## 7. Checked, and not checked

**Checked:**
- the full line diff from r2 to r3;
- the response's dispositions;
- the README rows;
- the r2 and review blobs;
- the bibliographic data against the reviewer's first-hand reading;
- Main:480–482 and U1:819.

**Not checked:** parts of r3 that are unchanged from r2.
