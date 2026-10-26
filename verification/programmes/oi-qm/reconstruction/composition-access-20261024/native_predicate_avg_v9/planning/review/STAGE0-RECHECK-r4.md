# Re-check: NP-AVG-1 Stage 0 r4 (the r3→r4 diff, under owner decision O-a)

**Reviewed.**
- `stage0/r4/STAGE0-PLAN-r4.md` (SHA-256 `1a9a2812…0a12`) and `STAGE0-CHANGES-r4.md`
  (`5dbf5adf…aeae`), on PR #935 at `2b54c8bd`.
- Diffed against r3 and `review/STAGE0-RECHECK-r3.md`.
- `stage0/code-r4/`: the diff against `code-r3/` read in full, and `s0mutants.py` read whole.
- `stage0/design-r4/`: the manifest and `runs/`. The code hashes and every retained stdout hash
  equal the manifest.

**Read-only.** Nothing was edited, committed or pushed. I ran no closure on v8's class; v8
contexts were constructed only. My re-runs are in `S/npavg/review-r4/rerun/` and my probes in
`S/npavg/review-r4/probe/`. The probes run on a copy of the r4 code, with the reviewer mutants
added.

## Verdict: ACCEPT WITH CHANGES

r4 applies RC1–RC10 and N1–N9 substantively.
- **The new required C11 parts work.** Every owner-named family is detected, and every
  decision-level mutant is caught, including mine from r3.
- **Everything replays.** All controls and the QUICK campaign replay byte for byte.

Seven required changes remain (R4-1 to R4-7). Each is a bounded text edit, a one-line planted-set
fix, or a keying fix. None changes the masking law, the domain or the decision labels.

**Freeze.** Layer 1 is not ready to freeze until these are applied. A diff-only re-check should
then suffice.

## 1. Reproduction

| step | my result | against `runs/` |
| --- | --- | --- |
| `s0controls.py` (full), normal and `-O` | exit 0, `failed: []`; 52 counts; refusal 13/13 | byte-identical (`a556e324…`); `-O` identical |
| `s0s6.py`, `s0symcheck.py`, normal and `-O` | exit 0 | byte-identical; `-O` identical |
| `rerun.py`, `planted.py`, `radius_mutants.py`, `exact_small.py`, normal and `-O` | exit 0 | byte-identical; `-O` identical |
| `s0mutants.py` (QUICK) | exit 0 | byte-identical (`8971d628…`) |
| full campaign | not run (§A.40, CI) | absent from `runs/`, as the plan says |

**QUICK campaign, from my re-run.**
- The frozen suite is clean, and mutants run only after that.
- All 16 mutants are killed at their named cases.
- The two demonstrations fail C11 only: blind −y fails parts i–iii, and ignore-fixed −y fails
  parts i and iii. Their reported counts equal the frozen rule's.
- The equivalent mutants: parity-dropped fails nothing, and symmetric-blind fails C1 only.
- Every bracketed "observed failures" cell in §6's mutant table matches the run.
- The demonstration context matches §9: 0 toy survivors under A and G, and 30 of the 52
  counts are identically 0.

## 2. The owner's five explicit checks

### 2.1 Planted-case families

**B type: detected.** `blind_B_minus_y` gives P_A-dir violations on the B planted sets (C11 ii),
and also fails C11 i and iii.

**G: detected.** `blind_G_minus_y` gives P_G-dir violations on the G sets (C11 ii).

**Φ-adjacent: detected.** `ignore_fixed_minus_y` eliminates the Φ-adjacent families (C11 iii).
My `rv_decide_ignore_fixed_y` eliminates 8 of them.

**G frame-adjacent family (departure 2): does not test what it is said to.** The family keeps
its own in-frame −x tip quantity. That quantity is non-fixed and covers the tip, so the fixed
quantities are never the tip's only cover.

The departure's premise is also wrong. Under G, every in-frame cell lies in the G cone of a fixed
quantity or a port sample, and neither is ever eliminated. So "ineligible" coincides with
"covered by the frame's own quantities". The true G analogue of the Φ-adjacent family is the
frame-adjacent family *minus* its in-frame tip quantity. Probe (`probe/frame_adjacent*.{py,out}`,
toy G only):

| mutant (depths 1–4) | r4's family | the family minus its in-frame tip |
| --- | --- | --- |
| frozen | 8/8, 13/13 | 7/7, 12/12 (retained) |
| −x tips ignore frame and fixed cover (decision-level) | 8/8, 13/13: **not detected** | 0/7, 0/12: **detected** |

That mutant is still caught elsewhere on toy records:
- C11 (i)'s decision check, 1,427 cases;
- C7;
- C18;
- C8 (`probe/G_ignore_fixed_mx.json`).

So no escape results, but C11 (iii)'s G family is decorative as built. **R4-1** fixes it.

### 2.2 Decision-level mutants: caught

| mutant | caught by |
| --- | --- |
| my `rv_decide_ignore_fixed_y`, re-implemented against r4 | C11 (i), 8 decision–table inconsistencies; C11 (iii), 8 adjacent families eliminated |
| my `rv_decide_blind_y` | C11 (i), (ii) and (iii) |
| r4's `decide_*` mutants | killed at their named C11 (i) case |

My third mutant does not matter: a G decision mutant that treats an uncovered ineligible −x tip as
free, keeping the fixed covers, is *equivalent*, since ineligible implies frame-covered. It fails
nothing (`probe/probe_quick.json`).

### 2.3 Configuration-keyed refusal: bypassable (R4-2)

Probe: `probe/guard_probe.{py,out}`. Contexts and record indices only; no closure.

| attempt | result |
| --- | --- |
| V8 object; a fresh identical `Setup`; sources reordered; flag flipped; `ref_context` under A and G | **refused** |
| port given as a list | TypeError, not a bypass |
| fresh `Setup` with the sources changed or empty | **not refused** |
| fresh `Setup` with ρ = 5 or t_last = 24, a superset of v8's records | **not refused** (`num_records`, `record_at`) |
| rebinding `G.V8_PARAMS` or `REF.V8_REF` in process | **not refused**; this is deliberate tampering and is noted only |

The sources enter only G-linkage and the (b) source cells, never the closure. So under A, and for
survivor status under G, a setup that differs from v8's only in its sources computes exactly
v8's closures. The same holds for a superset region or slice range on every v8 record it
contains.

The refusal therefore keys on parameters the class does not depend on. `s0ref` already keys
correctly, on (dim, n, port).

### 2.4 Completeness of the proof-dependent statements

PO3, PO5 and PO8 are complete and correct. I checked each:
- **PO3:** opposite-type cover needs reach r + 1, and same-type cover means a shared tip.
- **PO5:** p's cone is the six slice-7 cells plus V's cell. An aligned-tip norm of |c|₁ + d = 0
  or 1 forces V, a Φ cell or p, within the even class.
- **PO8:** t1 and t0 put mass on both y and both r; one unread fresh triple already makes
  (q8, q10) uniform; t1 has a zero entry, and t0 is not uniform.

**PO6 (A) is correct.** If no cone of S_A contains a pair cell of Φ, then S_A is a function of
pair variables disjoint from Φ under π. p is a function of Φ's cells. With PO4, the law reduces
to the collapsed case.

**Three defects (R4-3):**
- **PO6 (G) is a non-sequitur as written.** "S_G is a function of the frame and the seeds only,
  hence independent of G given the frame." G's source cells (−7, 0, ±1) and (−8, 0, 0) at slice
  0 lie *in* the frame (|c| = 8, even, so in B8). Being a function of the frame therefore does
  not give independence of G. The argument needs two things:
  - S_G is a function of the **non-source** frame cells and the seeds;
  - "given the frame" means given the frame's non-source cells, which is v8's frame or
    background, with G and the seeds random.

  With that wording the statement holds. The seeds are independent of G and of the in-frame
  quantities, and with PO4 (G) and PO7, Law_G reduces to Law_P of the truncated record. Since
  RESIDUE_UNLINKED's G clause rests on PO6 (O-c), this must be exact.
- **PO7's "a quantity has a seed tip iff |c| + t > 8" is false at slice −1.** A slice −1
  quantity (B, depth 0) has itself as its tip. It is a seed iff |c| > 7, that is |c| ≥ 9, which
  is |c| + t ≥ 8, not > 8. P_G's "|c| + t > 8" inherits the error. No item of the class is
  affected, since |c| ≤ 4 at slice −1 and the global bound lies in the same domain. But the
  frozen statement is false as written.
- **PO4 is missing from the citations.** C_A, C_G and PO6 (A and G) each need PO4 (the
  eliminated set is uniform and independent) to pass from "collapsed" to a law statement. None
  cites it.

### 2.5 Disclosure of the earlier demonstration's limits

§9 and the CHANGES file disclose accurately:
- 0 toy survivors;
- 30 of 52 counts identically zero, and their composition: survivor-conditioned 25,
  L3/L3′ 2, port-site 2, G source-cell 1;
- the vacuous port-site count (N7);
- r3's narrowness, including the 24 zero counts of 44 and the escape of
  `rv_decide_ignore_fixed_y`.

**One sentence is false.** "The other 22 … so no over-eliminating mutant can change them on this
class." My G over-elimination mutant (−x tips ignore frame and fixed cover) changes
`G:observer_classes` and `G:observer_classes_collapsed` from 173 to 24. The statement holds only
for over-elimination that respects the frame or eligibility (R4-4).

## 3. Other checks

**Rule T (O-b).**
- **Outcome-neutral: yes.** Its only inputs are the objective S1a counts L_A and L_G. It does not
  read the label, whether survivors exist, or the sign of any result, and a nonzero count *widens*
  the search.
- **Logic of the L_A = L_G = 0 branch: correct.** Every record over the S1a item domain has a
  context inside the union context, so its retained set lies in the global bound (PO4). The
  seed-tip property is intrinsic. So L_A = L_G = 0 excludes a linked survivor for every such
  record. PO6 is not needed for that.
- **Gaps (R4-5):**
  - **Invalid S1a.** No action is stated for an S1a run that is VOID, MISMATCH or INCOMPLETE.
  - **Undefined consequence.** "The k-independent consequence" is not defined. If it is read as
    law failure for every k, it over-claims: C_A rests on PO8, which is proved only for at most
    two Φ triples in clear. At k ≥ 4, for example, all of m, o1, o2 and o3 can be read in clear.
    The consequence must be the geometric statement alone.
  - **No checkpoint.** Nothing records L_A, L_G and the outcome of rule T as structured output
    (§A.41).

**The closed list of 52 counts.** It matches the code exactly: 10 per-convention counts, 7 under
A, 1 under G, 32 degeneracy counts and 2 global counts.
- **It is not closed against §3.** The G-linked and G-unlinked survivor counts are missing.
  RESIDUE_UNLINKED depends on them, and §3 defines them. They are source-dependent, so they
  belong on the list as computed per record, exempt from orbit reduction (R4-6).

**RC1–RC10.**
- **Applied:** RC1, RC3, RC4, RC5, RC6 (implemented: `c11_dir_tables` checks the decision
  against both tables), RC8 and RC9 (b), (c) and (d).
- **RC2:** applied, with the R4-3 defects.
- **RC7:** applied. Departure 1, placing retention in C11 (iii) with failure VOID, is sound.
  Departure 2 is not (R4-1).
- **RC9 (a):** applied as written, but keyed too narrowly (R4-2).
- **RC10:** applied, minus G-linkage (R4-6).

**N1–N9.**
- **Applied:** N1, N3, N4, N5, N6, N7 and N8. The aggregate checker now matches P_A.
- **N2:** bare "R5" (header line 45 and §12) and "R8" (§12, S10) remain.
- **N9:** applied. But the `blind_B_minus_y` and `blind_G_minus_y` predicates test only
  "pa_dir_violations > 0". They do not test that a violation lies on a B or G set, as their
  named cases say.

**The nine departures.**
- **Departures 1 and 3–9: accepted.** Departure 8 is acceptable because `s0native` takes no
  configuration.
- **Departure 2: rejected** (R4-1).

**§A.41.**
- **Covered:** the new invariants (C11 i–iii, the refusal, the closed counts, the
  demonstrations) each have a row.
- **Missing:** rule T has no row (R4-5).
- **Self-referential:** the row "every proof-dependent rule rests on a complete statement" is a
  document property checked only by review. That is acceptable, but it should say so.

**Minor.** §4's "asymmetry" bullet still lists the over-elimination guards as C2, C3, C6, C7, C15
and the campaign. C11 (i) and (iii) are now the direction-specific ones.

## Required changes

**R4-1. The G frame-adjacent family.** In §6 C11 (ii), and in `_planted_sets`, replace "Under G
the analogue is a frame-adjacent family, whose near tip in one direction is in the frame and so
ineligible" with:
> Under G the analogue is a frame-adjacent family *without its in-frame near-tip quantity*: that
> tip is in the frame, so it is covered only by the frame's own (fixed and port) quantities, and
> the frozen rule must retain the rest.

Correct CHANGES departure 2's rationale to:
> under G every in-frame cell is covered by a fixed or port quantity, so ineligibility coincides
> with frame cover

Add the reviewer's mutant to the campaign, named at C11 (iii): "−x tips ignore frame and fixed
cover (decision-level)".

**R4-2. Refusal keyed on what the closure depends on.**
- In §6 Refusal and §5b item 6, replace "Any setup whose (dim, n, ρ, t_last, port, sources)
  equal v8's" with:
  > Any setup whose (dim, n, port) equal v8's, whatever its region, slice range or sources
- Add to the refusal check: sources changed, sources empty, ρ = 5, and t_last = 24.

**R4-3. PO6 (G), PO7 and PO4 citations.**
- PO6 (G): replace "then S_G is a function of the frame and the seeds only, hence independent of
  G given the frame" with:
  > then S_G is a function of the frame's non-source cells and the seeds. Given the frame (its
  > non-source cells, v8's frame), the seeds are independent of G and of every in-frame quantity,
  > so S_G is independent of (G, V, the truncated record), and with PO4 (G)
- PO7's last sentence becomes:
  > A quantity at t ≥ 0 has a seed tip iff |c| + t > 8; a quantity at slice −1 iff |c| > 7. No
  > item of the class at slice −1 has |c| > 4.
- Restrict P_G's "|c| + t > 8" to t ≥ 0 in the same way.
- Add PO4 to the citations of C_A, C_G and PO6.

**R4-4. §9 disclosure.** Replace "so no over-eliminating mutant can change them on this class"
with:
> so an over-eliminating mutant that respects the frame cannot change them on this class; one
> that eliminates in-frame quantities can (the r4 re-check's G mutant changes the G observer-class
> counts)

**R4-5. Rule T.**
- Define the consequence:
  > **L_A = 0 and L_G = 0.** No record whose items lie in Reg × {−1, …, 23}, of any size, has a
  > linked survivor (PO4). The report states this geometric fact only; law failure beyond k ≤ 2
  > is not claimed, since PO8 covers at most two Φ triples in clear.
- Add:
  > If S1a is VOID, MISMATCH or INCOMPLETE, rule T is not evaluated and S1b and S1c are not
  > proposed.
- Add a §7 row:
  > rule T is applied as preregistered | `result.json` records L_A, L_G and rule T's outcome
  > (structured, §A.44)

**R4-6. G-linkage in the closed list.** Add to the §6 C8 list:
> under G: survivors G-linked and G-unlinked, computed per record and exempt from orbit
> reduction (source-dependent)

Update the total from 52, and update the design evidence to match.

**R4-7. The `blind_B` and `blind_G` predicates.** Make them require a violation on a set whose
name starts `A_B` (or `adjPhi_A_B`) and `G_F` (or `adjFrame_G_F`) respectively, matching their
named cases (§A.40).

## Nits

- **Status labels.** Label the bare "R5" and "R8" as "review R5" and "review R8" (N2).
- **Over-elimination guards.** Add C11 (i) and (iii) to §4's over-elimination guard list.
- **`s0symcheck` docstring.** It still says "control C0 (layer 1)". Prefer "design evidence for
  C0".
- **§7 review-only row.** Mark "every proof-dependent rule rests on a complete statement" as
  checked by independent review.

## Owner decisions

- **O-a (unchanged).** Apply R4-1 to R4-7, with a diff-only re-check, then freeze Layer 1.
- **Rule T's consequence.** Confirm that the L = 0 branch reports the geometric statement only,
  as R4-5 proposes. A law statement for k > 2 would need a new proof obligation generalising PO8.
- **Unchanged:** v8 is not authorized, and the full campaign runs in CI only on your dispatch
  approval.
