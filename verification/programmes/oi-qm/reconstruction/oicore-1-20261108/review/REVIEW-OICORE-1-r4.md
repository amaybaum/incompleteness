# REVIEW-OICORE-1-r4: independent re-review of OICORE-1 r4

- **Reviewed file.** `OICORE-1.md` (r4), sha256 `e090309cfc87e761d643a8691533d20cabeb656536645d62dbec8e19f3b6267b`.
  I re-hashed it before the review. It has 725 lines.
- **Against r3.** `OICORE-1-r3.md` (`93156b28…`, re-hashed) was diffed line by line against r4. The writer's dispositions are in §9.2.
- **Snapshot.** `origin/main` = `2cd49dc0`. The review is read-only. No Lean was run and nothing was computed.
- **Owner ids.** All five were re-read from #1169:
  - c.6724620166 (amaybaum, 17:22:38Z);
  - c.6724668737 (17:27:00Z);
  - c.6724721208 (17:31:47Z);
  - c.6724832474 (17:42:02Z);
  - c.6723277401.

  Every quote in r4 is a verbatim substring, with the correct id and time. c.6724832474 is headed "Q-C2-2 (ARP-3) r3"; the quoted sentence
  is at its line 31.

## Verdict: **REVISE (minor, text-only)**

The science in r4 is right, and the R3 findings are fixed in substance. Two of the coordinator's explicit acceptance criteria still fail,
both on wording:

- the access exclusion is still labelled with the class that §0 defines as "proved unable" (R4-1);
- the horizon-limited route is presented as "consistent with OI" and as a route OI "exposes", rather than as "not excluded" (R4-2).

One new overstatement entered with the R3-n1 fix (R4-3). The remaining findings are nits. Each fix is a few words.

## R3 findings: status

| Item | Status | Evidence |
|---|---|---|
| R3-B1 | **fixed in substance; label residue (R4-1)** | ACC_op is restated precisely as "every available relabelling lies in ⟨σ, τ⟩" (l. 183). It carries three hypotheses, (iii) "consistency with `OICore`: open" in bold (l. 250). The dense form is NS (ll. 250, 337, 532). §5(b) moves ACC_op out of the "proved unable" bullet (ll. 330-332). §4 (l. 305) matches |
| R3-B2 | **fixed** | NI-W is defined (l. 84) and applied to EMB in §3.2 (l. 258) and §8.6 (l. 537). No NI-W row is counted as "proved unable": the only such list, §5(b) l. 330, names FIX_op and FIN_op. §8.4's capability table has no EMB "CX" |
| R3-B3 | **fixed** | Every dense-ceiling site names the carrier: K on the `Fin 2` system carrier, every ancilla level, with the carrier-general form as A (ll. 248, 267, 336, 378, 511, 533, 564, 658). l. 267 records that the kernel proof goes through the quarter phase (FrozenSourcing.lean:177) and that the mixing-specific form is A |
| R3-B4 | **fixed** | §5(f) now "supports this statement", followed by a neutral locating list (ll. 372-383). The exact result is flagged as not used against ε. Configuration level and effective level are separated, with c.6724668737 cited. The W/D exclusions are "conditional on those unverified records". "Beyond these, the question stands as the owner stated it." |
| R3-B5 | **fixed in structure; overstatement (R4-2)** | §8.7(e) is by route, and the gap table is split (ll. 609-611). "Not shown that every ε-route falls into one of these four" (l. 602) fixes the finite-to-universal step. "Under the existing theorems" is added (l. 586) |
| R3-B6 | **fixed, with two residues (R4-5)** | §7 lists Theorem C and F0 as open gaps. It cites owner ids, says "Coordinator messages are not cited as authority", and states no owner decision covers the Theorem C gap |
| R3-n1 | **fixed** | The spectral argument is given with its hypotheses (l. 565). The eigenvalue claim is right: `conjChannel(rot α ⊗ I)` has the nontrivial eigenvalues `e^{±2iα}`, and Niven's theorem makes 2α/π irrational |
| R3-n2–n8 | **fixed** | The `StateMixingCoupling.rot` citation; the CTRL exception (l. 342); FIN_op as A over K (l. 253); "not assessed" (l. 286); interpretation marks (ll. 501, 538) with §8.5 scoped (ll. 522-526); Lemma M names `Fin 2` (l. 212); RC-1 no longer cited |

## Findings

**R4-1. The access exclusion still carries the "proved unable" class label (blocking for criterion B1).** Lines 250 and 532.

- §0 defines **CX** as "*proved unable*: excluded within a stated class" (l. 82). ACC_op's cells read "**CX, exact**" in §3.2 (l. 250) and in
  §8.6 (l. 532: "**CX, exact**, possibly vacuous").
- The implication ACC_op ⇒ ¬control is proved, and it is definitional. But the class label asserts inability for a candidate that may be
  unrealizable together with the core. The coordinator's criterion is that nothing elsewhere calls it "proved"; the label does, through
  the legend.
- The same label residue appears in the §3.2 RET-s cell (l. 254): "CX in W/D scope". There CX, which means "proved unable", rests on
  W and D records. §8.6 l. 535 correctly says "excluded within those scopes, conditionally". Use that wording in the cell.
- *Fix.* Add a legend entry, for example **CX†** = "excluded *if* the candidate is consistent with the core; consistency open". Use it in
  both cells. §4 (l. 305) and §5(b) (ll. 331-332) already use the right words.

**R4-2. "Consistent with OI" overstates the horizon-limited route (blocking for criterion B5).** Lines 595, 599, 610, 629, 666, 716.

- *No model is exhibited.* r4 calls the route "consistent with OI" (ll. 599, 610, 629, 666, 716), says it assumes "nothing beyond OI's
  axioms" (l. 595), and says the distinction "exposes" it (l. 599). But no native rule, identification and read set realizing such a gate
  is exhibited. Consistency is therefore not shown; what is shown is that no result found excludes it.
- *The route is ENC-G's second disjunct.* §8.8 types ENC-G as an "ext (new hypothesis, not adopted)". "Assumes nothing beyond OI's axioms"
  is true only of the route's *target*. The existence of such a gate is the open conjecture, and positing it would be ENC-G.
- *Reviewer's note.* My R3-B5 fix text used the phrase "consistent with OI and not yet closed". On this pressure test that phrase was too
  strong, and the correction applies to it as well.
- *Fix.* At every site:
  - replace "consistent with OI" with "**not excluded** by any result found";
  - replace "Assumes: nothing beyond OI's axioms" with "no premise beyond OI's axioms *is needed to state it*; whether native dynamics
    supplies such a gate is open (ENC-G's second disjunct, OC)";
  - recast the headline at l. 599: "it leaves **one route not excluded**, the horizon-limited finite-order gate, which is open on two named
    counts; it is not a candidate mechanism".

**R4-3. "Exact infinite order requires an infinite world" overreaches (r4's own §8.7(c)).** Lines 593 and 629-630.

- *The overreach.* §8.7(e) row 2 and §8.8 (l. 629: "The first disjunct needs an infinite world or open supplies") treat an exact
  infinite-order gate as requiring an infinite world.
- *Why that is too strong.* §8.7(c) excludes such a gate in a closed finite world only under row 2's hypotheses: a linear identification,
  an `S`-invariant preparable span, and one fixed induced map. Row 5 lists "non-linear identifications" as **open**.
- *Fix.* State it conditionally: "in a closed finite world, excluded under §8.7(c) row 2's hypotheses; otherwise open (row 5), or an
  infinite world or open supplies, which is a new hypothesis".

**R4-4 (nit). A D1 level mix in §8.4's capability table.** Line 511.

- The cell reads "Dense on encoded carriers: … **open** beyond, including the horizon-limited route".
- Under the existing theorems, a finite-order gate gives no density (`denseUnitaryControl_of_fixedGate` needs α/π irrational). The
  horizon-limited route is an ε-route needing OICORE-F6, not a dense one.
- *Fix.* Move "horizon-limited" to an ε clause.

**R4-5 (nits). Residual off-`main` labelling under §A.42 item 8.**

- **Theorem C use sites.** The §7 row for Theorem C (l. 409) lists its use sites as §3.2, §5(f), §8.7(c) and §8.10. It also appears at:
  - §8.6 RET-s (l. 535);
  - §8.7(e) row 2 (l. 593);
  - §8.8 (l. 622);
  - §8.4 (l. 511).

  Each of these carries a [D] label, but the §7 list should be complete.
- **The F0 cell.** The §3.2 ACC-U cell (l. 252) still says "**OC, with one instance against sufficiency** [D]". §5(c) (ll. 350-351) uses
  the r4 wording ("*Draft-conditional* … If that draft stands …"). Use the same words in the cell.

**R4-6 (nit). Lemma M's carrier at §5(d).** Line 358. The sentence reads "Within `FiniteOperationalTheory`, no downward-closed predicate …
forces exact or dense control (Lemma M)". Lemma M is stated on `FiniteOperationalTheory (Fin 2)` (l. 212), and dense control exists only
there. Add "(Fin 2)".

## Answers to the coordinator's checks

- **B1.** The three hypotheses are kept, and the consistency hypothesis is prominent (bold, l. 250; l. 239; ll. 331-332). One residue
  remains: the CX label in two cells reads as "proved" through the legend (R4-1).
- **B2.** NI-W is applied consistently. No NI-W row is counted among the "proved unable" rows in any table or summary.
- **B3.** The carrier is named at every dense-ceiling site. The corollaries are marked as A.
- **B4.** §5(f) is neutral. No exact result is used against the ε question; l. 377 says so explicitly.
- **B5.**
  - The route-by-route structure is consistent across §8.7(e), the gap table, §8.8 and §8.10.
  - "Consistent with OI" is overstated; it should read "not excluded" (R4-2).
  - §8.8's "needs an infinite world" overreaches (R4-3).
  - The horizon-limited route is not presented as an *adopted* mechanism, but "exposes" in the headline leans that way (R4-2).
- **B6.** Every off-`main` reference has a classification, and draft-conditional uses are labelled. Two residues remain: the incomplete
  Theorem C use-site list, and the F0 cell wording (R4-5).
- **Summary against body.** §5(b), §5(f), §8.4, §8.6 and §8.10 agree, apart from R4-1, R4-2 and R4-4. No other new overstatement was found.
- **Owner-quote ids.** All correct.
