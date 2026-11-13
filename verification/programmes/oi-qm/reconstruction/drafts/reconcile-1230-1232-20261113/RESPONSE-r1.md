# #1230 / #1232 reconcile: response to the independent review (r1 → r2)

**Objects.**
- r1 is `RECONCILE.md`, sha256 `05ad46b2977055069678f7a911d87bcd59f85408e10786ebcdd57d86cf91a71f`. This matches the object the review names.
- r2 is `RECONCILE-r2.md`.
- The review is `REVIEW.md` (ACCEPT WITH CHANGES, 20 replacements).

**Method.** Read-only. Before applying each replacement, I checked it against its source (below). The edits were then applied mechanically, and each old string was asserted to occur exactly once. r1 is unchanged. No change outside the 20 items was made, except the owner-guidance paragraph recorded below. There was no computation on any OI rule, and nothing was committed, pushed or posted.

**Sources re-read for this response:**
- the kernel at `c3b5f37a`: `realized_of_instAvail` (ImplementationLocality:530, the same induction as INTERVENE T7(b)); `configurationLevel_falsifierUnavailable` (ManuscriptAxioms:155); `configurationLevel_not_layerFlowExecutable` (LiftAudit:183); `SystemToLevelOne` (LevelOneSeam:115–117, with its docstring at :115–116 and the `def` at :117);
- APPROX r4a on `research/approx-unit1-r4a-1216-20261109` @ `e41cf613`, `APPROX-UNIT1.md`:453–485;
- #1216 c.6793397036, full body;
- OA-2 r4 on `main`: N2.1 at :300–318, Corollary B′ at :319–323, and 𝔊_K Claim 2 and its scope at :440–467;
- INTERVENE-UNIT1.md at `ea12fde1`, lines :108, :123 and :222;
- `research/q868h-868-20261113` @ `ffc9cda4`, compared with `acf28d3a` (two commits; header status, the probe-repeat note and hashes only);
- Bell-scope `e1534b08`, which has no citation of INTERVENE or #1230.

| # | Finding | Check against source | Disposition |
|---|---|---|---|
| 1 | A, B: T7(b) is not new. The system-branch FI-1 also follows under `LabelInvariant`. | Confirmed. `realized_of_instAvail` has the op/readout/coarse/bind/discard induction verbatim on `main`. APPROX r4a :455–467 uses it, together with `discardWith_uniform_conjChannel`, and states "Under one of those named hypotheses [`LabelInvariant` transport or `SystemToLevelOne`], system-NX-1 ⇒ exact FI-1". | Applied exactly. |
| 2 | A: drop T7(b) from the list of additional items. | Follows from 1. | Applied exactly. |
| 3 | A: drop T7(b) from option (c). | Follows from 1. | Applied exactly. |
| 4 | C: the governance statement was false. The rule to cite is §A.45 rule 3. | Confirmed. #1216 c.6793397036 (`amaybaum`, 2026-11-11T10:28:21Z) item 3 reads "Related draft: INTERVENE-1 (PR #1230, WIP, under review)" and says "it authorizes nothing". §A.42 item 7 is the native-round clause; §A.45 rule 3 governs authorization entries. | Applied exactly (both strings). |
| 5 | D: 𝔊_K is the M-INACC case, not a non-spanning one. The link to OBL-SP is an analogy only. | Confirmed. OA2:442–446: the point preparations [ab] are reachable through PREP(a, b). OA2:466–467: "a designed classical, per-horizon instance of M-INACC". Corollary B′ (:319–323) names both routes. | Applied exactly (all three strings; the appended sentence follows "set up to examine."). |
| 6 | E: the T3 boundary flag is incomplete and imprecise. | Confirmed. INTERVENE:222 drops "spanning". INTERVENE:123 defines the E_f class by "an entrywise nonnegative frame matrix", which is not unique without spanning. | Applied exactly. |
| 7 | E: §5 conflict 1. | As 6. | Applied exactly. |
| 8 | F, G: the Q1 labels in row T2, and its mixed-scope "Dup". | Confirmed. REC-1 r7 rows 9 and 18 carry Q1-I only. REC-1 has no row for H-IND. OA-1 row 9 and Main:588 are results specific to the read/write access. | Applied exactly (both strings). |
| 9 | F: H-IND "plays the role of" a fixed lift. | Confirmed. INTERVENE §1.1 H11 and §6 leave the relation of H-IND to H-LIFT unaudited. | Applied exactly. |
| 10 | I: the Q2 scope of "no Q2-F operation", and the class of the saturation register. | Confirmed. REC-1 rows 6, 17 and 20 class designed maps as Q2-F with designed-map standing. | Applied exactly. |
| 11 | I: §5 "None supplies…". | As 10. | Applied exactly. |
| 12 | H: "establishes" conflicts with §A.46 item 1. | Confirmed. The drafts are off `main` and were reviewed only by a model. | Applied exactly. |
| 13 | J: the L1/L4 summary could be read as excluding the O2 window. | Confirmed. SUBSTATE leaves the window untested (§3.1, §3.3 route C). | Applied exactly. |
| 14 | J: the writer-pass list omitted nit 2. | Confirmed. INTERVENE:108 says "Then the output is not a function of μ (X7)", while X7 is a two-point existence countercontrol. | Applied exactly. |
| 15 | J: the landing order was stated as forced. | Confirmed. Bell-scope `e1534b08` does not cite INTERVENE or #1230. | Applied exactly (both strings). |
| 16 | J: the Lean citations did not drift. | Confirmed. `SystemToLevelOne` sits at :115–117 at both pins, with the `def` at :117, and :116 is a docstring line. Under OIBridge only `OIRealization.lean` changed between `cac5d264` and `c3b5f37a`. | Applied exactly. |
| 17 | J: the [L] facts are external inputs, not §A.42 item 8 references. | Agreed. | Applied exactly. |
| 18 | J: the Q-868-H pin, and the premises of (V). | Confirmed. The branch head is `ffc9cda4`, and the commits after `acf28d3a` touch only the header status, the probe-repeat note and hashes. Q868H-UNIT1:47–54 lists SA-1(a), P3 with (iv), E-iso, WL and NNB. | Applied exactly (both strings). |
| 19 | J: what T5 adds. | Confirmed. APPROX r4a :471–483 has CM as an Architecture, the FI-1 witness and "CM's isometries are exactly the monomial ones". It does not have `InstAvail CM ↔ InstAvail substratumClass` or the theory equality. | Applied exactly. |
| 20 | Process: the record needs a pushed head for the ChatGPT review. | Agreed on substance (§A.43 item 2; c.6854241002). | **Applied in modified form.** The review's new text keeps the word for a local session directory, which the coordinator's instruction bars from r2. r2 reads "It is a working record, not yet on any branch; …". The rest of the sentence matches the review's text exactly. |

**Owner-guidance item (relayed by the coordinator after the review; not one of the 20 replacements).** The guidance asked for three things:
- state the final conclusion at exactly this strength: neither draft establishes an operation physically reachable under the currently demonstrated OI premises (REC-1 Q2-F/Q2-P). That is stronger than "documentation incomplete", and it is not a claim of impossibility;
- keep mathematical existence (for example `realized_of_instAvail`, proved and conditional) separate from physical reachability;
- keep 𝔊_K (M-INACC) and N2.1 (non-spanning) as distinct obstructions.

Disposition: **applied.** r2 adds one paragraph, "Conclusion, at its exact strength", directly after §5's "None supplies an operation outside 𝒦 …". It is consistent with the review: the distinction between 𝔊_K and N2.1 is change 5, and `realized_of_instAvail` is change 1. This paragraph is the only text in r2 that is not one of the review's 20 replacements.

**Not changed.**
- The nit that the Main:414 "Wings separated by less than the graph cone …" sentence predates #1233 (it was at Main:416 at the pin) carried no replacement string, so r2 does not change it.
- The review states that none of the changes alters the central conclusion or the disposition options (a)–(e), and r2 keeps them. Option (c) no longer lists T7(b). The owner has since adopted option (c) (#1169 c.6854728636). That decision is not recorded in r2, because recording it was not among the 20 changes.
