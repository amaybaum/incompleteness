# Independent review: PR #864 third-pass correction (MEV / OV-LU)

**Object.** `a147aa3ab94ea064cbdeb5432f3febd06f7967c0` (tree `eec67e2d…`, parent `6df43b2c`), branch
`staging/premise-memo-864-20261018`, fetched from GitHub into a read-only sparse partial clone `/home/user/work/r864`
(blob:none, cone = the premise-memo directory, 7.9 MB). No pushes or GitHub writes; one GET of review comment
6254962113. Author: `Claude <noreply@anthropic.com>` for both author and committer, with the required trailers.

**Verdict: ACCEPT-WITH-NITS.** The correction is mathematically right. It removes the equivalence at every site
and changes no class or label. Two wording nits (N1, N2) are worth fixing. Neither is a blocker.

## 1. Witness, recomputed independently

Script: `$S/w1019/864/review/rv_mev.py`. It uses exact SymPy, is written from the memo's definitions, and does not
read `verify_mev.py` or `dc_premise.py`. Output `review/rv_mev.out`: 17 PASS, 0 FAIL, rc 0, byte-identical over two
runs. sha256 py `d264de65…3261c`, out `1bfd506f…2913`.

| quantity | author | mine | |
|---|---|---|---|
| min over all ME projectors of Tr(P_ψ X_c) | 15/136 | 15/136 | agree |
| product test (e_v⊗P_0) after CN: Tr[(e_v⊗P_0) CN X_c CN] | ½ − 53/100 = −3/100 | −3/100 | agree |
| CN(e_v⊗P_0)CN = P_v | yes | yes (exact matrix identity) | agree |
| min over product vectors (block positivity) | 1/850 | 1/850 (Schmidt² = {16/17, 1/17}) | agree |
| min eig X_c; even block of X_c | −3/100 | −3/100; −3/100 (fails UPD) | agree |
| B = CN(\|+⟩⟨+\|⊗P_0)CN = \|Φ+⟩⟨Φ+\| | yes | yes | agree |

- **How ME-validity was checked.** ψ = (I⊗W)Φ+ runs over all ME vectors, with W ∈ SU(2) (the phase drops out). I
  checked symbolically that the coefficient matrix of ψ is Wᵀ/√2. Exactly, ⟨ψ|P_v|ψ⟩ = (25a₁² + 9a₂²)/34 ≤ 25/34, with
  a remainder of 16a₂² ≥ 0 and equality at W = I. The minimum is therefore 15/136 > 0. A float countercheck over 20 000
  random W is evidence only, and is consistent.
- **OV-LU ⇒ MEV holds as stated.** For symbolic X and symbolic unitary W I checked the identity
  Tr(P_{(I⊗W)Φ+} X) = Tr[(|+⟩⟨+|⊗P_0) CN (I⊗W)† X (I⊗W) CN]. So each ME projector is one product test after a local
  unitary and the coupling. The converse fails on K = cone(SEP ∪ {X_c}): this cone is a domain cone (X_c is
  block-positive) and satisfies MEV, but fails OVc and hence OV-LU, since the identity is a local unitary.
- **The new operational form is an exact equivalence.** MEV ⟺ "the fixed test |+⟩⟨+|⊗P_0 is valid after *every*
  local unitary and the coupling". The forward direction holds because local unitaries map ME vectors to ME vectors;
  the converse is the identity above. See N1 for the quantifier.
- **Controls.** The countercontrol (a PSD state passes the same product test) and the mutation (c = ½ gives 0, no
  violation) both behave as expected.
- **Consistency.** MEV ⇏ OVc already follows from rows the memo had before this pass: "UPD vs MEV incomparable" (the
  X_c cone) together with "OVc ⇒ UPD". The new row agrees with them. The CORRECTIONS reason column states that the old
  equivalence would have forced MEV ⇒ K ⊆ Q3, and that reasoning is right.

## 2. The equivalence is gone

- **Search.** I ran `git grep -E 'OV-LU|ME-valid'` over all 52 files of `x-screen-20261018/` at a147aa3a, and read
  the full memo for "=", "⟺", "iff" and "equivalent" near MEV.
- **Memo, current hits.** OV-LU now appears only in implications that are true: PREMISE-MEMO.md:137 ("OV-LU …
  implies MEV. MEV implies neither OV-LU nor OVc"), :244 and :409.
- **Original memo.** The hits in `PREMISE-MEMO.original.md` (:127, :315) are in the frozen original and are correct
  to keep.
- **Rest of the directory.** No file outside the premise-memo directory mentions OV-LU.
- **Downstream sites read.** None asserts or relies on MEV ⇒ OVc, MEV ⇒ OV-LU or MEV ⇒ K ⊆ Q3:
  - §3.3 L-row, the §3.4 rows and the X_c note;
  - the §4 MEV row and the PSD list;
  - the headlines, the G1/G4/G5 cells, §6 item 2, U4;
  - CORRECTIONS :63–66.
- **Assert-then-qualify (§A.30).** None found. The old assertion is deleted, not qualified.
- **Not run.** A repo-wide grep. The disk was too low to fetch blobs (see the end), and the code-search API is not
  available to this session. OV-LU is coined in this memo and appears nowhere else in its directory, so the risk is
  low, but the corpus-wide check (§A.25) is not certified here.

## 3. Status is unchanged

**Cell-by-cell table diff.** I parsed every table row at 6df43b2c and at a147aa3a: 110 rows before, 111 after.
- One row is added: §3.4 "OV-LU ⇒ MEV; MEV ⇏ OVc, hence MEV ⇏ OV-LU".
- Exactly four cells change:
  - §2 MEV premise text;
  - §2 UPD basis;
  - §5 UPD G5, where only the tag is split and "FAIL standalone…" is kept;
  - §5 MEV G1, where BORDERLINE is kept.
- Every class cell is identical, including MEV (i), UPD (iii) and OVr unresolved.
- The §4 MEV row and every other §4 and §5 label cell are byte-identical.

**The author's three judgment calls.**
- **(a) New operational form of MEV (:137).** This is within the authorization. It is an exact restatement of MEV,
  which I verified (§1), so it carries no new scientific content. It rests on B = CN(|+⟩⟨+|⊗P_0)CN, which is
  `dc.out` line 4 [EC, dc], and on the textbook local-unitary orbit of Φ+. Tagging that orbit fact [W] rather than
  [W, new] is reasonable. The quantifier needs tightening (N1).
- **(b) n133 rewording (UPD basis cell, plus "D3, as in row CPK" in class (iii)).** This is within the authorization
  (review item 3). It states why D3 is not a G2 ground, which the second pass had already established and the third
  review accepted: UPD evaluates PSD of compressions but posits no PSD or CP order on K. It coheres with §4, where UPD
  fails the no-PSD-import criterion. That is a criterion, not a class ground. Class and status are unchanged.
- **(c) Dropping "unless stated as OV-LU" from MEV's G1 cell (:369).** This is within the authorization and
  required by it. The clause offered a route to G1 PASS through the false equivalence, and OV-LU is a different,
  strictly stronger premise. The label stays BORDERLINE. OV-LU is not an inventoried premise, so no row's status
  moves.

## 4. Frozen files are byte-identical

Blob ids are the same at 6df43b2c and at a147aa3a:
- `PREMISE-MEMO.original.md` `8637edfb0dcb6b83130a6fe97e0994112554983c`
- `dc_premise.py` `ef35cb837a1b1f4932a59d09048d8321472599f5`
- `dc.out` `f4f1e9e57312f0908523e67e4e0583ed0c3a1c54`

The diff touches only `PREMISE-MEMO.md` (`1c410ae5 → 7a8e5813`) and `CORRECTIONS.md` (`90351ef2 → 6c5bd86d`). I
did not replay `dc_premise.py`.

## 5. The CORRECTIONS.md entry

**Present and in the file's own format.** It has a provenance bullet (:13–15), a third-pass section with a
fix / lines / what / reason table, and a checks paragraph.

**Line references.** I checked them against `git diff -U0` hunks. All are exact (t33, t103–106, t133, t137, t168–174,
t244, t246–249, t270–271, t366, t369, t405–410, t412–413), except the one in N2. The prior-file references
(second-pass :56–60, :14–16) and the corrected second-pass ranges (n169–173, n420–421) also match the 11562ace→6df43b2c
hunks.

**Content.** The checks paragraph discloses honestly that the scratch computation is not retained, and its numbers
agree with mine.

**Edits in place to the second-pass section.** The consistency paragraph, rows 4 and 6 and the scope paragraph were
edited in place. These edits are owner-authorized ("CORRECTIONS.md") and each is recorded in third-pass rows 1 and 6,
so provenance is kept. The corrected consistency sentence is right: MEV's state-side form is membership in the dual of
the ME projectors.

**Memo voice.** The memo carries no self-narration. The added "(comment 6254962113)" citations follow the tag idiom
already used for review-sourced checks.

## 6. Register

I scanned the diff's added lines for:
- the §A.32 family (meta-commentary, reader instruction, self-assessment);
- the §A.33 history family ("no longer", "is now", "corrected form", "formerly", …);
- mid-line [A-Z]{4,} capitals.

There are 0 phrase hits. The capitals are only the gate labels PASS / FAIL / OPEN / BORDERLINE and the filename
`PREMISE-MEMO`. CORRECTIONS.md's "was false" is change-note text, which is exempt. Strictly, §A.32/§A.33 govern
`papers/` only.

## Findings

- **N1 (nit, recommended): the quantifier.** "the product test |+⟩⟨+|⊗P_0 after a local unitary and the coupling"
  can be read as a single unitary. That is validity of one ME projector, which is strictly weaker than MEV. This is
  exactly the distinction the pass corrects.
  - Sites:
    - PREMISE-MEMO.md:137 ("after a local unitary and the coupling is valid");
    - :369 (G1: "one product test after a local unitary and the coupling");
    - :408 ("one product test after a non-native local unitary and the coupling");
    - CORRECTIONS.md:84 ("Its operational form is the product test … after a local unitary and the coupling").
  - Fix: write "the fixed product test |+⟩⟨+|⊗P_0 after every local unitary and the coupling". At :408, write "one
    fixed product test after every (non-native) local unitary and the coupling".
- **N2 (nit): one line range.** CORRECTIONS.md:89 says "n108–109 → t109–110". The hunk is `-109,2 +109,2`, and line
  108 is unchanged. Fix: "n109–110 → t109–110".
- **O1 (optional): spell out the "hence".** The "hence" in PREMISE-MEMO.md:244 uses OV-LU ⇒ OVc, which is true
  (take the identity unitary) but not written. Fix: "…MEV ⇏ OVc, hence MEV ⇏ OV-LU (OV-LU ⇒ OVc, identity
  unitary)".
- **O2 (no action): the [EC, dc] tag on the value.** At :137 and :247–248, "Tr(P_v X_c) = ½ − 53/100" carries
  [EC, dc]. `dc.out` checks the sign ("Tr(P_v X) < 0 with P_v in G") and the generic CN(a⊗P_0)CN form, and the value
  itself is one line of algebra. The tag is adequate.

**Not done by this review.**
- A repo-wide grep, which disk limits prevented.
- A replay of `dc_premise.py`.
- fsck, signature verification, CI and the release gate.

**Disk.** `df -h /` read 549 MB at the start and fell to 440 MB during the review from other writers. My own writes
were the 7.9 MB clone and under 20 KB in `$S/w1019/864/review/` and this file. The clone `/home/user/work/r864` is my
own and can be deleted.
