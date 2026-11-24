# Independent review, round 4: A1 amendment proposal r4, the O-13 inventory and the draft decision

Reviewer: non-author, 2026-11-24. This is a paper-only review. Nothing was written in the repository. P's checkers and
the repository tools ran only on copies under `review-r4/`.

**Inputs.** `MANIFEST.sha256` passes. The files reviewed, with their sha256:

| File | sha256 |
|---|---|
| PROPOSAL-r4 | `676810f6…4e74` |
| CHANGE-INVENTORY-r4 | `6b875c29…117c` |
| CHANGES-r3-to-r4 | `4399ff01…fe9d` |
| O13-INVENTORY-r4 | `497950bd…2458` |
| O13-DECISION-DRAFT-r4 | `eb282795…05ef` |
| review-r3 | `ab30b1a7…3ff9` |

## Verdict: ACCEPT-WITH-NITS

There is no blocking finding. R3-B1 is resolved exactly. All seven of the owner's acceptance requirements pass. The
draft O-13 decision correctly adopts exactly D402–D412 and limits the supersession to them. Before the owner approves
it, I recommend four precise wording additions (§4 below). Each closes a gap that a strict reader could otherwise
open. None of them changes the proposal's substance.

## 1. R3-B1 and D403

**D402 now reads** "… and $1/\alpha_0$ is computed from the lattice momentum integral of §6.1 over the whole Brillouin
zone, whose counterpart for a finite substratum and whose normalization of the vertex coupling are not established."
This is my r3 wording verbatim.

**The same correction is applied in three other places:**
- the §32.9 1/α₀ row, which now cites Π_s(0), ∫d⁴q over four directions (:689) and 1/α₀ = 6 × Π_s(0) × 4π (:683–685);
- open-dependency item 4;
- the PROPOSAL.

**No stale phrasing remains.** A grep of PROPOSAL-r4, the r4 PREREG, both O13 files, CHANGE-INVENTORY-r4 and the edit
records finds no "over ℤ³", "is the Brillouin" or "is the integral". The only "over $\mathbb{Z}^3$" left is the quoted
r3 text in PROPOSAL-r4's change table, as history. The regenerated SM.tex diff carries "over the whole Brillouin
zone".

**D403's "H-slope on identified transitions"** appears verbatim in GR:88, at H and at T1′.

## 2. The owner's seven acceptance requirements

| # | Requirement | Result | Evidence |
|---|---|---|---|
| 1 | The blocking finding is resolved | **Pass** | §1 |
| 2 | Every scientific change in D402–D412 is explicitly justified | **Pass** | Each edit record carries a reason. O13-INVENTORY-r4 gives the supporting lines at H for every changed conclusion. I checked each citation: SM :60, :252, :334, :340–344, :374, :448–460, :464–468, :543, :555, :585, :589, :681–689; GR :58, :88, :312–316; ch09:36, :137; ch19:212. |
| 3 | No unsupported claim of independence from A1 is introduced | **Pass** (nit N1) | The new texts contain no independence statement. The only "independen" hit is "background-independence" in D412. §32.9 states that "No use of A1 found" is not independence. N1 concerns a possible implicature only. |
| 4 | The six unresolved dependencies remain explicitly unresolved | **Pass** (nit N2) | All six are in §32.9 and the inventory. Items 1–5 are also named in SM:1394 itself through D402. Item 6, A6's role beyond the gauge entry, is stated only in §32.9. |
| 5 | Item 7 remains unchanged and passes | **Pass** | The PREREG is a pure append; row 7 reads "as frozen". My item-7 implementation on H plus the r4 ledger gives PASS: pointer 4 lines, all "(A1)" false positives; count 0. NC1–NC5 each FAIL. |
| 6 | The original 399 ledger edits and the trial evidence remain unchanged | **Pass** (correction C1) | P's 399 splices are byte-identical in the r4 ledger, and D001–D401 are unchanged (edits.json rebuilt from P plus the new records). §32.1 keeps T0′ `02172b20…` and T1′ `14ac71b4…` and their runs as evidence of what they tested. The draft decision does not mention trial evidence; see C1. |
| 7 | O-13 supersedes the scientific-preservation clause only for the exact reviewed edits | **Pass** (C2–C4 recommended) | Item 2 of the draft limits the supersession to the eleven edits, each identified by file and by the hashes of its old and new bytes, plus the two digests. |

**N1.** D402 says "whether an entry requires finiteness of the substratum is not established where those theorems use
…". A strict reader could infer the converse: that where those conditions are not used, independence is established.
- The text does not say that.
- Almost every entry rests on the d = 3 selection, so the converse would cover only the trivially conditional Higgs
  input and the algebraic step of Theorem 15.
- Optional tightening, which removes the implicature entirely without weakening any established statement: "it is not
  established whether the entries require finiteness of the substratum; this turns in particular on the measure
  conditions of Lemma 1c or Proposition 4b, the continuum conditions of the $d = 3$ selection (§3.2), and, for
  $1/\alpha_0$, …".
- This is the owner's choice. The current text is acceptable.

**N2.** Open dependency 6 (A6) is visible in SM:1394 only for the gauge entry, through D412. This is consistent with
§2.3, which lists A5–A6 for the whole construction, so it is acceptable as stated in §32.9.

## 3. O13-INVENTORY-r4

**Every changed conclusion is present.** There are 11 edits across 11 rows:
- 6 SM predictions plus the frame sentence;
- 3 book sites, each with its FULL mirror.

The Higgs entry is listed as unchanged.

**Appendix A is verbatim and its hashes are correct.** I recomputed each edit (`inventory_check.out`):
- each span equals the ledger;
- each old_sha256 and new_sha256 equals the ledger's and my own recomputation;
- each old text equals the bytes at H;
- each new text equals the record.

**The classifications are correct against the cited lines.** Specifically:
- D403's A1 category: GR:58 at H reads "Under A1, restrict the finite total system to a conserved energy shell", and
  GR:88 reads "including A1 and the conserved energy shell".
- H, the previously unstated hypotheses: H-spin′ and light-spectrum selection (D410); family pattern, representations
  and H-χ′ (D411); the reduction premises and Proposition 14a (D412); GR's conditions (D403).
- U: matches the six open dependencies.

**Nit N3.** The Higgs row lists category "E", but no text of that entry changes. "none (unchanged)" is more accurate.

**The "strengthened?" column is correct.** Each change does one of the following:
- adds conditions that the cited derivations already state (a narrowing);
- marks open points;
- names a set the corpus already enumerates (ch09:36).

None establishes a new result. D402's "rest on the local spatial/gauge construction of §2.3" restates SM's own
dependency statement (:60). It corrects scope and is not a new result, which is the owner's distinction.

## 4. O13-DECISION-DRAFT-r4

**What it gets right:**
- It adopts exactly D402–D412. I checked all 11 (file, old_sha256, new_sha256) rows against the ledger; all match. It
  also names edits.json `19eb79bd…6b4b` and ledger.json `d20495f0…0976`, both reproduced.
- It supersedes only "or any scientific conclusion", only for those edits.
- It protects H and the 399 splices.
- It protects every other conclusion "as written".
- It requires a new decision for any byte change or further edit.
- It authorizes nothing else (item 5).

**It is not quite complete enough to approve as is.** I recommend four exact additions.

**C1 (requirement 6).** Add to item 2:
> - The frozen plan `4c79be642ca631573f06b444903be75ec4f5e2b6` and the trials T0′ and T1′ of that plan, with their
>   runs 45077568347, 45080985924 and 45083256017, remain unchanged as evidence of what they tested.

**C2 (the 399-splice clause).** c.7093128173 also forbids any "change to … the 399 ledgered splices". Adding splices
changes `ledger.json`. Add to item 2:
> - Adding the splices of D402–D412 to the ledger leaves each of the 399 ledgered splices byte for byte unchanged and
>   is not a change to them; the words "the ledger base H" and "the 399 ledgered splices" of c.7093128173 are not
>   superseded.

**C3 (the owner's scope/result distinction).** Replace the first line of item 3 with:
> The edits correct the stated scope and dependencies of existing conclusions; they establish no new scientific
> result, and none of them may be cited as one. None strengthens a claim.

**C4 (binding the reviewed text).** Item 1 identifies the edits by their hashes alone. Add:
> The adopted texts are those of `O13-INVENTORY-r4.md` Appendix A (sha256 `497950bd…2458`), reviewed by
> <reviewer, review file and sha256, verdict>; if any later revision changes a hash above, this decision does not
> apply to it.

**Placeholder.** "Independent review: <…>" should be filled with this review's file and sha256 and the verdict
ACCEPT-WITH-NITS, or with that of any later round.

With C1–C4 and the placeholder filled, the wording is unambiguous and complete.

## 5. Mechanics, all reproduced independently in `review-r4/sb`

**edits.json.** P's edits.json round-trips exactly. Adding `diffs-r4/new-edit-records-D402-D412.json` gives 412
records, sha256 `19eb79bd478275110b4ff1cd3ae2271c37574e849d45be272f53b8e75e726b4b`. This matches the claim. Between r3
and r4 only D402 and D403 changed, in their `new` and `reason` fields.

**ledger.json.** `preserve_check --build-ledger` gives 410 splices in 44 files, sha256
`d20495f0084f29ac5c58c5a0480be5f0ed342334381e6680e9cca58952940976`. This matches.
- P's 399 splices are identical.
- The 11 new splices equal the writer's.
- Each new old string is unique at H.
- No splices overlap.

**P's checkers**, all exit 0 / PASS:
- `--static`, `--simulate`;
- `--pins`: 412 unique;
- `--repo-scan --simulate --final`: 0 unexplained;
- `--verify-ledger`: re-derived identically;
- `--verify-pins`: pin findings 0;
- both self-tests.

**PREREG.** It is a pure append. Both parsers read 6 equal rows from §32.10, and §32.10 carries the r4 digests.
`duplicate_check` reports OK.

**Configuration.** It pins `d20495f0…` (ledger) and `19eb79bd…` (edits), replacing the r3 digests. The w1-w2 v2 file is unchanged since r2.

**Item 7.** The tree is PASS, and NC1–NC5 each FAIL (`item7.out`).

**Gate tools on H plus D402–D412.**
- Same output as at H: coverage, claims, voice, citation_roles (exit 2 at H as well), dependency_label and
  baseline_label.
- staleness reports SM and book as STALE, which is expected before the TeX is regenerated.

**TeX.** The diffs are confined to the edited paragraphs. The source stamps equal my rebuilt sources: SM `1259d56b…`
and FULL `9f419aae…`.

**Not run:** guards_check and SC-42. These are gate items.

## Files (`review-r4/`)

- review.md
- item7.py and item7.out
- ledger_cmp.out and inventory_check.out
- the checker outputs, rc.out and pins_check.out
- gate_tools.out and *_tree.out
- sb/ and work/

tree/ and tmp/ are scratch and are not in the manifest.
