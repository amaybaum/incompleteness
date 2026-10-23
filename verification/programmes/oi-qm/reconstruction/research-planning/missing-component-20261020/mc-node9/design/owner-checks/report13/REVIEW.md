# Coordinator review: joint-record handoff v1

> **DRAFT — research record.** The owner's read-only session produced this exploratory diagnostic. It is recorded
> here with the coordinator's verification and independent checks. It is not a native apparatus or an acceptance test.

## Verification

- **Archive.** The archive's sha256 is `e864a676cc742c94b358ef476a642002479da2c8c67c1137b1a4326c5b67f070`, as
  stated. The files in `handoff/` are its contents, unchanged. Their `SHA256SUMS` verifies.
- **Code review before running.** `joint_record_checks.py` uses only the standard library and writes no files.
- **Replay.** Run from a separate directory, normally and with `-O`, the output is byte-identical to
  `joint_record_checks.out`.

## Independent checks (`coordinator_joint_checks.py`; separate code)

**Setup.** Each station uses its own orthonormal frame with rational entries. Read ties are excluded and asserted.
Per-station (timestamp, read) laws are mixed directly, without the aggregated h_t/k_t formula.

| Check | Result |
|---|---|
| J1 | A against B at n = 63, m = 256, with an X read. **Handoff frames:** exact-time TV 0.04377046, time-blind TV 0.00063982, matching the handoff; with a 16-bin clock, 0.00790809. **R's transverse frame rotated by (3/5, 4/5) about R:** 0.04424444, 0.00060662 and 0.00891793 respectively. The witness does not depend on that free frame choice |
| J2 | n = 15, alternative frames, atom by atom on (timestamp, read), reported per read axis. The three antipodal identities hold on every axis. The fourth fails on the X, Y and R reads (245 of 245 positive-read atoms each) and holds exactly on the Z read (0 of 245): for a Z read the X, Y and R emissions have a symmetric transverse Z projection given the timestamp |
| J3 | The (1, w) columns have rank 4. The four relations lie in the null space with rank 4, so they span it |
| J4 | Clock/velocity TV at n = 127, from exact depth counting: 0.0597 for B = 16, under the bound 0.0888; 0.2370 for B = 64, under the bound 0.3552 |
| J5 | The single-call joint-record inequality with a 16-bin clock: TV(A, B) ≤ 2c[δ_n + B/(8E[P₊])], with δ_n the largest single-read error on 8 stations × 4 reads. At n = 63: TV 0.0079 ≤ 0.2495 (δ = 0.00123). At n = 127: TV 0.0046 ≤ 0.1683 (δ = 0.00061) |

## Findings

1. **The handoff's results hold.**
   - With equal heralds, the fourth identity already fails without timestamps (time-blind TV 0.00064). The clock
     amplifies the failure to 0.0438.
   - The completeness criterion for preparation equivalence on this menu is correct.
   - The finite-clock bound holds.
2. **The witness is robust to the station frame.**
   - Rotating R's transverse frame changes the exact-time TV only from 0.0438 to 0.0442.
   - The mechanism is as stated: the clock carries S_x, and S_x enters R's X read with weight X·R = 4/5, whatever
     the transverse frame.
3. **The finite-clock bound is valid but conservative (POSITIVE, quantified).**
   - The measured 16-bin joint TV falls from 0.0079 at n = 63 to 0.0046 at n = 127. That is a factor of 1.7 for a
     doubling of n, consistent with the O(B/√n) bound.
   - The bound itself is 30 to 37 times larger. It is dominated by B/(8E[P₊]).
4. **Scope is unchanged.**
   - The station-rotated source is a diagnostic modification. The native wave has not been shown to build oriented
     carriers.
   - The finite clock is a stipulated interface, not a derived one.
   - The four identities hold for one fixed protocol and this menu; they cover neither all protocols, the Born rule
     nor composites.
   - Two tested transverse frames show robustness to those two choices, not a theorem for every frame. The owner's
     follow-up (report14) proves a nonzero exact-clock witness for every frame.

## Relevance to the next target

The four record identities, or an explicit bounded-error version of them, are the test a native
clock/carrier/detector update must pass. Station-independent heralds and correct herald marginals are not enough.
