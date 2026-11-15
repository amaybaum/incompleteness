# Focused confirmation review: VERIFY-SL3-CC-r2 against the review of r1

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/VERIFY-SL3-CC-r2.md`
and `RESPONSE-VERIFY-SL3-CC-r1.md` at PR #1294 head `3a08a4463b64bde2fa1cd09e2c415b7a65972180`. r2 was
added in `d195a29f`. The other commits since the r1 review are `c2da5530` (it retains the review),
`ad83ee33` (U2 r1) and `3a08a446` (U4 r1). U2 and U4 were not reviewed here.

**Sources.** The same as for the review of r1: MR★, PREREG, LOG and PC★ at
`origin/main` = `75cc5100`. Read-only; hand checking only. This reviewer wrote the review of r1 and none of
the records under review.

**Verdict: ACCEPT.** F1–F7 are resolved. The F5 departure is correct. The diff makes no change beyond the
findings and what they require. All four items stay named premises until acceptance. Three optional nits
follow; none blocks acceptance.

***

## 1. Each finding

- **F1, resolved.**
  - §1.2's (L3c) now checks only MR★'s stated support, with the corrected sentence ("the map on `s_X` is
    `Φ^t_{XX}`, fixed by `(t, X)` and selectable by no region").
  - The block-swap argument is now Sup-1, "global block-form reading", in §1.3. It is credited to the record,
    and "unconditional" is gone.
  - The marginal reading and the `ℤ/2` one-site case are Sup-3. They are stated correctly: `Φ^1_{XX} = σ_X`;
    the cross term vanishes under a zero-current-slice neighbourhood; the case contradicts no S-L3 bullet and
    gives no erasure; and regions with internal edges and `n ≥ 2` are left undecided. I re-checked the algebra.
- **F2, resolved.**
  - §1.5 has two rows: S-L3 as stated is VERIFIED; the gloss "erasure unavailable on K1" is VERIFIED AT
    NARROWER SCOPE, with the scope stated.
  - §6 credits Sup-1 and Sup-2 to the record, not to S-L3.
  - The narrowing is applied to MR★'s own uses (MR★:648, 856, 1396, 1485), and MR★ is left uncorrected
    because it is frozen.
  - The list "what is not verified under the gloss" covers T3-sense return (PREREG:485–487), transport (as
    relocation, with marker-local reading only) and Sup-3.
- **F3, resolved.**
  - "Side 2 in every axis" and "`𝐑 = ℤ/2`" are both stated.
  - "Outside the native lattice" is removed.
  - The native scope is unaffected for the correct reason: frozen K1 uses the relation sum (MR★:358–359;
    PC★:102–106).
  - The `A ≠ 0` remark is restricted to the multiset reading.
- **F4, resolved.** CC5's T7 separation is split into the law level (as written; same protocol, PREREG:552)
  and the verdict level (conditional on PC-Q's W1 and MR★:1145–1147), in §4.2 and §4.4. CC7's T7 carries the
  same condition, and the record notes that CC7's named test is §3.5.
- **F5, resolved.** The record now uses the signed `V = 1 − 2q`:
  - `V = 0` needs `q = ½`;
  - (ii) and the dephasing classification need `0 < q < 1`;
  - the §3.5 separation is moved to conditional, and only the `D` part stays as written.
- **F6, resolved.** §2 states both facts: PREREG:552's "from PC-Q's law", and Row 0 (MR★:1243–1248) against
  frozen 0(i) (PREREG:592–593). §3.2 and §3.4 say CC4's T7 separation cannot be computed under the law
  reading, and hold only under a reading that does not compare laws. §6's repair list adds the rule for
  `separated` and the Row 0 clause. The repair list was a recommendation of mine, so its addition is in
  scope.
- **F7, resolved.**
  - `DP`'s validity for CC4 needs uniform `f`.
  - G-CC4-1 names the strength map, `B₀`/`B₁`, and `z_s`/`x_s`.
  - CC5's T5 `p₀ = ½` needs uniform `e`, while the frozen T5 records hold for any law of `e`.
  - LIT-1-C7 is cited at LOG:433–435 and LIT-1-C4 at LOG:67–70.
  - CC4's three T2 laws are shown and match B-T2; I re-derived them.
- **Optional §0 note, applied.** The off-`main` references are classified: the S3 drafts as provenance;
  PR #1023 c.6554399670 as support on `main` through MR★ §K★.F; the relayed `fc68d333` review as provenance
  only.

## 2. The F5 departure (the T8 row needs only `q > 0`)

The departure is correct. §M.9's check (b) requires that "the capability recorded for the element in the full
interface vanishes in the deleted one". CC7's row records that capability as "`V(π/2) < V(0)`" (MR★:1172),
and `V` is signed (MR★:972).
- In the full interface, `V(π/2) = 1 − 2q < 1 = V(0)` exactly when `q > 0`. With `q = 1`, `V(π/2) = −1`.
- Under `MK₁(0)`, `V(π/2) = V(0) = 1`, so the capability vanishes.
- So the T8 row passes for every `q > 0`.

My r1 bound `0 < q < 1` belongs to (ii), which concerns contrast. The record now keeps the two conditions
apart, which is correct.

*Nit (optional).* At `q = 1`, `MK₁` is a deterministic phase flip. It passes this T8 row with no loss of
contrast. So the row's signed capability is a weaker test than (ii), and CC7's reference value `V = 0` is
what catches a degenerate `f`. This could go in the §6 repair list as a specification note.

## 3. Nothing else changed

- `VERIFY-SL3-CC-r1.md` is byte-identical between `d58bd082` and the head. The only other change in the
  directory that touches it is the README row for r1, now marked "reviewed (ACCEPT WITH CHANGES), so all four
  stay named premises".
- I compared r2 with r1 section by section. Every substantive change maps to F1–F7 or to the optional note.
  The remaining edits are consequential:
  - the `fc68d333` disclaimer moved into §0's classification;
  - B-T2 and B-T4 were added to the PC-Q comparison values, for F7's T2;
  - the §1.4 row on the "subsystem form" was removed, because that content moved to Sup-1;
  - §7's checked and not-checked lists were updated.
- No verdict became stronger than in r1 except where a finding required it. Every scope is narrower or more
  explicitly conditioned.

## 4. Standing

- §0 keeps all four items as named premises "until this record is itself reviewed and accepted", and §6's
  consequences apply "once this record is accepted". Both match #1169 c.6891189024 and c.6891241282.
- The record claims paper verification only. No conditional claim is presented as established, and the
  supplements are not credited to S-L3.

## 5. Optional nits

1. §7 still cites the LIT-1 reader record as "LOG:55–80". The LIT-1 entry begins at LOG:21, and LOG:55–80
   holds caveats C2 to C5. Citing it as "LOG:21–80 and LOG:433–435" would be exact.
2. §1.2's (L3c) paragraph could point to Sup-3 for the case `Φ^t_{XX} = σ_X`, so that the sentence "no
   region's content can make `σ` the map applied to `X`" is not read as "`σ` is never applied".
3. The F5 nit in §2 above.

## What I checked and did not check

**Checked:**
- every F1–F7 site in r2 against the sources at `75cc5100`;
- the Sup-1 and Sup-3 algebra, the F5 sign analysis, and CC4's T2 laws;
- that r1 is unchanged, and the README rows for r1 and r2;
- the response table against r2.

**Not checked:** S3-U2-r1, S3-U4-r1 and U4-SOURCES-r1 (outside this object), and anything my review of r1
listed as not checked.
