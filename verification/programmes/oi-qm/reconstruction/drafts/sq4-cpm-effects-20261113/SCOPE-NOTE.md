# Scope of OA-2 E(b) and E1 in records on `main`: citing note for Finding CX-1

**Standing.** A citing note for eight records on `main` that state OA-2 Theorem E(b), Corollary E1
or OA-3 N4.3/N4.4. None of the eight is edited: each is pinned by blob or SHA-256 in another
record. The note states the scope at which their statements are supported. Authority: owner
amaybaum, #1169 comment 6894115930 (2026-11-15T12:11:24Z), "Confirmed, proceed as suggested", for
the scope correction; and #1277 comment 6894228476 (2026-11-15T12:21:00Z), "Confirmed, proceed as
suggested", for one citing note on `main` naming CX-1 and stating the narrower scope. The
statements below are hand derivations [W] and await independent review.

SQ4 is a proof-dependency audit. It is not a refutation of OA-2 or OA-3 at the scope stated here,
and not a physical no-go. No manuscript or book text cites E(b), E1, C-PM or OA-2, so no manuscript
is affected.

## Finding CX-1 and the supported scope

**CX-1** (`AUDIT.md` §2.1, this directory). The rule `M(x, w, ℓ, r) = (x, x + r, ℓ, w + ℓ)` over
`F₂`, with `x, w ∈ H`, `ℓ, r ∈ V`, `ℓ` the preparation's setting cell and horizon `T = 2`, meets
(H1), H-AR, (H3), (H4) as written at OA2:502, (xiv), (SP) and C-PM. Under held-at-use herald typing
(OA1:127, :131) or the single-tick effect class (OA2:107–108), its prepare–measure fragment has no
preparation-noncontextual model: the earlier record value is held at the latest read only in the
label cell `ℓ`, which C-PM excludes from effects. It is classical under ensemble-conditioned heralds,
under MP-0b retention of the non-label record, under C-PM′ and under role-typed labels. Its gbit is
imposed by the cell-typed label convention; it is not a nonclassicality witness. Literal (H4) is
also met with no label routing, through static held label cells alone (`AUDIT.md` §2.1, Bearing):
when held label cells determine the initial configuration, literal (H4) holds at every horizon, and
the same gbit arises under cell-typed and role-typed labels alike. Role-typed labels therefore do
not restore literal (H4) in general.

**Supported scope** (`AUDIT.md` §2.2). Write `Z^{lf}` for the held records restricted to cells outside one
fixed label-cell set for the whole fragment, the union of the label cells of its admitted
preparations (as OA2:451–454), and `Z₀ := Z^{lf} − H_c^{lf} c`; `Z^{lf}`, the effect class and `ι`
then do not depend on the preparation.

- **(H4′).** Within the horizon, the C-PM-available part of the held record at the latest read
  determines every earlier available read. MP-0b retention of the non-label record realizes it;
  retention held only in label cells does not.
- **Held-at-use or single-tick typing.** E(b) holds under (H1), H-AR, (H3), (H4′), (xiv), C-PM and
  (SP), with `Z₀` label-free.
- **Ensemble-conditioned heralds.** E(b) holds under (H1), H-AR, (H3), (xiv), C-PM and (SP), with
  `Z₀` label-free and (H4) redundant (OA-3 N4.3's route).
- **(SP)** for the label-free record follows from (SP) for the full record, by pushforward along a
  coordinate projection.
- **E1.** Its generalized form and contrapositive hold with (H4′) for (H4) and `Z₀` label-free. Literal
  (H4) without (H4′), under held-at-use or single-tick typing, is an exit within (H1) ∧ (H3).
- **Status.** (H4′) is a named hypothesis, not derived from OI's rules. Which herald typing E3 uses is
  open (OA3:124–128), so neither form is established as the theorem. The statements below are used as
  premises only at the scope stated here (§A.46 item 7).

## The eight records

Paths are relative to `verification/programmes/oi-qm/reconstruction/`, on `main` at
`7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac`. Each statement is quoted as written; "Scope" gives the
reading at which it is supported.

1. **`oa-2-20261112/OA-2-REPORT-r4.md`**, blob `8f8ddf73366deb1a2caa13d8c826744d1ba87607`.
   - :534, E(b) step 4: "It is preparation-noncontextual, because singleton indicators are
     available."
   - :552–553, Verdict N2.4: "Under (H1), H-AR, (H3), (H4), (xiv) and (SP), the emergent
     prepare–measure fragment is simplex-embeddable (fails G3), at every carrier size."
   - :585–586, E1: "So for **any rule, affine or not**, and any observer: if settings translate the
     joint held record, and (H4), (SP) and (xiv) hold, then the prepare–measure fragment is
     simplex-embeddable."
   - The same conditions are restated at :79–82, :720, :764, :872, :874 and :886–888.
   - Scope: step 4 holds for the label-free `Z₀` under (H4′) or ensemble-conditioned heralds. N2.4,
     E1 and the restatements hold with (H4′) for (H4) under held-at-use or single-tick typing.
2. **`oa-2-20261112/STATUS.md`**, blob `7945ac8acaaae40fca6ec754498456153da9f280`.
   - :62–64: "Under (H1), H-AR (additive, cell-aligned observers), (H3) no supplied control, (H4)
     nested records, (SP) spanning and ledger item (xiv), the prepare–measure fragment is
     simplex-embeddable."
   - :71–73, the claim supported by the record, carries the same conditions.
   - Scope: "nested records" is read as (H4′), or the heralds as ensemble-conditioned, with `Z₀`
     label-free.
3. **`oa-3-20261112/OA-3-REPORT-r4.md`**, blob `0a36fd05ba6931705ecdbb1de9962d58a307c1cb`.
   - :468–469, N4.3 step 4: "Singleton indicators `[Z = λ + h(c)]` are available, as heralds at every
     tick followed by a final read."
   - :479, N4.4: "the effect cone is the cone generated by the joint indicators `[Z = z]`".
   - :488–489, Verdict N4: "E(b) holds with (H4) replaced by that effect class, under (H1), H-AR, (H3),
     (xiv) and (SP)."
   - Scope: the indicators and cone are those of `Z^{lf}`, not of `Z` with label coordinates. Under
     ensemble typing, N4.3 and N4.4 hold as stated for `Z^{lf}`. Under held-at-use typing, the
     retention the class needs is (H4′), for example MP-0b retention of the non-label record; with
     retention held only in label cells, the cones of :477–484 differ (CX-1).
4. **`oa-3-20261112/STATUS.md`**, blob `9b1f6f5aee806d3f97c38b241f5467169e7bb779`.
   - :61–63: "For the affine class under (H1), H-AR, (H3), (xiv) and (SP), Theorem E(b) holds with
     (H4) replaced by the heralded-composite effect class (V-ii-H)."
   - :76, the claim supported by the record: "Theorem E(b) holds with nested records replaced by the
     heralded-composite effect class".
   - Scope: as for record 3.
5. **`drafts/unified-ledger-20261114/LEDGER-r9.md`**, blob `7c69662ad04430a2554d07614dea0e3412b69b73`.
   - :614: "Theorem E(b): for the affine class, under (H1), H-AR (additive, cell-aligned observers),
     (H3) no supplied control, (H4) nested records, (SP) spanning and ledger item (xiv), the
     prepare–measure fragment is simplex-embeddable."
   - :615: "N4 there: Theorem E(b) holds with (H4) replaced by the heralded-composite effect class."
   - :616: "By contraposition (inferred): within these records' hypotheses, a prepare–measure
     fragment that is not simplex-embeddable needs a rule outside the affine class or the failure of
     one listed hypothesis".
   - Scope: :614–615 as for records 2 and 4. :616 holds with (H4′) among the listed hypotheses.
     Under literal (H4) with held-at-use or single-tick typing, CX-1 is affine, meets every listed
     hypothesis and is not simplex-embeddable.
6. **`selection-discriminator-20261113/support/synthesis/SYNTHESIS-r3.md`**, blob
   `e68295098577f4ec28cdc52726e83395deee915f`.
   - :93: "T5, a non-simplex-embeddable (G3) prepare–measure fragment (OBL-SP; OA-2 Corollary E1);"
   - :610: "P0 says this does not refute E(b), since N8.2(b) fails (SP)."
   - Scope: E1 as in record 1. :610 holds of N8.2(b). CX-1 meets (SP) and bears on E(b) under
     literal (H4) with held-at-use or single-tick typing. It answers T5's presumption (:608–609):
     step 4 needs label-free `Z₀` and, under held-at-use typing, (H4′).
7. **`native-apparatus-source-20261113/support/tune-published/TUNE-1-SOURCING-r2.md`**, blob
   `35c5c116c017ed03a2eacfbeccfed457bae4649b`.
   - :295–296: "Context, not used for the verdict: if a member were specified and met OA-2 Theorem
     E(b)'s hypotheses with (SP), its prepare–measure fragment would be simplex-embeddable".
   - Scope: E(b)'s hypotheses read with (H4′) and label-free `Z₀`, or with ensemble-conditioned
     heralds. The record's verdict does not use the sentence.
8. **`native-apparatus-source-20261113/support/tune-confirmed/TUNE-1-SOURCING-r2.md`**, blob
   `20ee9b04844fa548a7845c7da655a7fd4a723196`.
   - :295–296: the same sentence as record 7.
   - Scope: as for record 7.

## Pins that keep these records unedited

| Record | Pinned by |
|---|---|
| 1 | `native-apparatus-source-20261113/EVIDENCE.md` and `source-objects.json`; `oa-2-20261112/OBJECTS.md`; `oa-2-20261112/STATUS.md` |
| 2 | `native-apparatus-source-20261113/EVIDENCE.md` and `source-objects.json` |
| 3 | `native-apparatus-source-20261113/EVIDENCE.md` and `source-objects.json`; `oa-3-20261112/OBJECTS.md`; `oa-3-20261112/STATUS.md` |
| 4 | `native-apparatus-source-20261113/EVIDENCE.md` and `source-objects.json` |
| 5 | `drafts/unified-ledger-20261114/README.md` (SHA-256) |
| 6 | `selection-discriminator-20261113/ARTIFACTS.sha256`, `RETENTION.json`, `SOURCES.md` |
| 7, 8 | `native-apparatus-source-20261113/ARTIFACTS.sha256`, `RETENTION.json`, `EVIDENCE.md` |
