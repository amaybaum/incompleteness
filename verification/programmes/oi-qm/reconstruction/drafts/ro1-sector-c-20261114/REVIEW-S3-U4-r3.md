# Focused confirmation of S3-U4 r3 against the review of r2

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U4-r3.md`
(blob `54ee9629`) and `RESPONSE-S3-U4-r2.md` (blob `055349c1`), at PR #1294 head `41d4d8ce`.

**Baseline.** `REVIEW-S3-U4-r2.md` (blob `e377aa5e` at `e3245893`), which has six required findings
(R1–R6) and nine optional ones (O1–O9).

**Reviewer.** The same independent, non-author reviewer. Read-only and paper-only. Git and the API were
used only to read files and comments.

**Integrity.** r2 is unchanged at `41d4d8ce` (blob `d8cced4c`). The blob pins r3 cites for
`REVIEW-S3-U4-r2` (`e377aa5e`) and `REVIEW-U4-CALC-r2` (`70eddf2d`) match `e3245893`.

## Verdict: ACCEPT WITH CHANGES

r3 is ready, and nothing in r3 itself needs to change. One sentence of the response misdescribes r3
and makes a technical claim that does not hold, so the response needs a one-line correction (C1).
Every r2 finding is resolved in r3. D-1 stays undecided at (γ), and nothing counts under SNR-1.

## 1. The r2 required findings

| # | Finding | r3 location | Status |
|---|---|---|---|
| R1 | The PK-2 conflict needs its fixed-geometry condition | §6.3 (r3:661–681); U4-F8 (r3:777); routing (r3:861–862); AV-t scope (r3:709, :846) | **RESOLVED.** PK-2 is stated at fixed geometry, tick and background, and is said not to predict fringes in any one configuration (that is `K^D_t`). The data are identified as comparisons of settings (LIT C8; Walborn Fig. 2 against Fig. 3). A conflict needs (γ) to map the runs to the same `Φ_{DΣ}` and background at `D`, differing only in which region is declared a marker. Otherwise PK-2 is silent. The native-marker part is tied to §4.1's unreachable branch |
| R2 | Prop. 2.8(i) holds under H-μ only | §2.1 (r3:188–201); PK-2 (r3:537–546); U4-F3 (r3:772) | **RESOLVED.** See §3 for the new [A-inf] |
| R3 | QM-4's "It excludes only …" | QM-4 (r3:625–628) | **RESOLVED.** It now excludes every pair with `V > √(1 − D_whole²)`, and every pair off the circle under the equality. The exclusion is total only at the extremes. This matches LIT §3 |
| R4 | PK-6 caveat dropped | PK-6 (r3:581–583) | **RESOLVED.** Both r1 sentences are restored verbatim in substance |
| R5 | The Case Pk typing is unconditional | §5.4 (r3:478–490); U4-F6 (r3:775); owner question 2 (r3:877–880) | **RESOLVED.** The text uses LIT's word "unread". The typing is conditional on G4 classifying an unread in-flight photon as unheld or inaccessible, and one owner question now governs both this typing and AV-t |
| R6 | The response's change list is incomplete | §6 definition (r3:509–518); response R6 list | **RESOLVED**, with one inaccurate item (C1). The U1 r5 §4.5 parked-record clause (U1 r5:571–574) is now quoted verbatim, and AW-1 is kept separate in owner question 1 |

The optional items O1–O9 are all applied as the response states. Spot checks:
- **O1.** The CALC status and its blob match.
- **O2.** r3:288–289 reads correctly.
- **O8.** P-L3 is PLAN r9:533's premise (Main:54).
- **O6.** The [A-inf] labels are added at r3:247–249, r3:258, r3:407 and U4-F10.

## 2. r2 → r3 diff

Every hunk of `diff r2 r3` falls into one of these groups:
- the revision paragraph;
- the restored decision-A and "not authorized" quotations. The decision-A text matches c.6890079967;
  the not-authorized list matches U1 r5:68–69;
- an R1–R6 disposition;
- an O1–O9 disposition;
- one of the restorations the response lists: §3.1's scoped-reading clause, M-8's §A.29 clause, and
  Main:153's backflow sentence. The last is checked: Main:153 cites [4, 5] for information backflow.

The two AV-t scope additions ("at fixed geometry", r3:709 and r3:846) are not itemized in the response,
but they are direct consequences of R1. No unaccounted change was found.

## 3. The new author-side extension in §2.1 ("Beyond H-μ"), re-derived

**Claim.** Fix a non-carrier law `ν` on `S_{Σ^c}`, independent of the carrier. Then `D`'s law is
unchanged by how `Σ^c` is partitioned into declared regions. A change of the marker's preparation
changes `ν`, and is not covered.

**Hand derivation.** Let `D ⊆ Σ^c` be readable.
- By additivity (S-L1; the exact algebra of VER §1.2), `π_D pr_D φ^t(s) = M^D_t s_Σ + N^D_t`, with
  `N^D_t = π_D pr_D φ^t ι_{Σ^c} s_{Σ^c}`, one fixed homomorphism of `s_{Σ^c}`.
- By independence, given `s_Σ = x`, `D`'s readable content has law `ν^D_t(· − M^D_t x)`, where `ν^D_t` is
  the pushforward of `ν`.
- A partition of `Σ^c` into regions changes neither `ν` (a law on `S_{Σ^c}` as a whole) nor that
  homomorphism. So `D`'s conditional law is the same under every declaration.
- This is Theorem 1′'s conditional-law step applied at `D`. It needs neither bijectivity nor
  uniformity. Under H-μ it reduces to Prop. 2.8(i).

**Verdict: correct.**

**Scope.** The scope is stated correctly:
- `ν` must be fixed as a joint law, so a preparation assigned region by region is a change of `ν`,
  which is the stated exclusion;
- a `μ` that correlates non-carrier content with the carrier is excluded (C-9);
- the claim holds at fixed geometry and tick.

The content is a relabelling observation, close to definitional. It is labelled [A-inf] and claimed as
nothing more.

**Citation, optional.** It rests on S-L1 alone. Citing S-L5 [NP] as well is conservative, not wrong.

**SNR-1.** The extension carries only the quiet-marker branch of the potential conflict. That branch is
an assumed apparatus (PLAN §8.4; U1 C-PREP), and r3:675–678 states that it does not count. No negative,
and no count toward (a′)–(e′), rests on the extension. **Nothing counts because of it.**

## 4. The PK-2 conflict

It stays potential (r3:675). It is conditional on (γ) *and* on (γ) mapping the compared runs to the
same carrier transfer and background at `D`. It rests on an assumed carrier preparation and, for the
quiet branch, an assumed marker. It does not count under SNR-1, and it is routed to the γ plan with the
mapping question attached (r3:861–862). Its native-marker part is §4.1's branch, which is not reachable.
**Confirmed.**

## 5. Repository text rules

Both files were grepped for the banned words, machine-local paths and closing keywords. There were no
hits.

## 6. Findings

### Required (response only; r3 unchanged)

**C1. Correct item 5, first bullet, of the response's R6 list.** The bullet says PK-1 "now states" that
the parked value, outside Sup-3's zero-neighbour condition, "returns mixed, which is scrambled in
C-RET's sense".
- r3's PK-1 (r3:528–536) is unchanged from r2 and contains no such sentence.
- The claim is also not right in general. C-RET's "scrambled" means readable only with content still
  held in `H`. The r1 review's finding 1 showed that under A-cur `V` can recover the parked value from
  its own reads of the neighbours, so a mixed return need not be scrambled.

*Required change:* state that the r1 sentence is dropped, without replacement, for that reason. Do not
add the sentence to PK-1.

### Optional

- **O-a.** In §2.1's "Beyond H-μ", "resting on S-L1" would be exact; S-L5 [NP] is not needed.
- **O-b.** The response could name the two AV-t "at fixed geometry" additions under R1.

## 7. Checked and not checked

**Checked:**
- the full r2 → r3 diff;
- each R1–R6 against the text, and O1–O9 by spot check;
- the restored quotations, against c.6890079967, U1 r5:68–69 and :571–574, and Main:153;
- the hand derivation of the §2.1 extension;
- SNR-1;
- the blob pins and r2's immutability;
- the text-rule grep.

**Not checked:**
- anything outside r3 and its response;
- the other units added in `95c7e066..41d4d8ce`.
