# Independent review: Q-C2-1 r13 (ARP-2-QC21), the implementer's nineteen items

**Reviewer.** The same independent model reviewer, 2026-11-09. Read-only. Work done:
- the writer's two r13 probes run (paper-sized; QM and synthetic data only);
- both self-tests run in `wt-impl`;
- one text-only check of Appendix D against the r5, r6 and r7 drafts (`review/probes-r13/appd_check.py`).

No decisive builder was run, and no B-P or B-C table was built.

## Verdict: **REVISE**

- **Not freeze-ready by design.** D19 to D23 are `PENDING` owner decisions, and freeze readiness requires none.
- **Two blockers on the text:**
  - **R13-B1.** One IMPL item (#3, second half) is IMPL only under D21(a). Under D21(b) it silently weakens a control,
    so D21(b)'s stated consequences are incomplete.
  - **R13-B2.** D19's options omit two readings that could decide the **unnarrowed** B-P within the caps, and a third
    with a one-sided outcome. Under the owner's rule ("do not narrow it silently"), the owner should see them before
    choosing a narrowing.
- **Implementation finding.** The implementer's scripts at `aa9cd82e` / `b1d4bea4` predate several r13 resolutions and
  must be brought into line before the pins are taken at `F`.
- **Otherwise sound.** The other IMPL items preserve the approved definitions, controls and outcome rules. The SCI
  items are correctly separated and neutrally posed. The VOID-by-construction finding and its arithmetic are correct.
  Appendix D is faithful.

## Inputs verified

| file | sha256 / blob |
| --- | --- |
| preregistration r13 | `d0795c002ce7286a0f7b4361b2845e436d2cb70e23847a71284598af13fced92` |
| PLAN r13 | `fe1515332745328da611c3070d062b47367030c5f7d3173f6ea74316ae692735` |
| DESIGN-DS r13 | `fbfbd9faccce2ff617669ef120a1b4d17497bb0f7d93ff40647427b5dca99b57` |
| `probes-r13/s4f.py`, `qmp_marker.py` | `d1e56566…`, `efd583bd…` (as cited) |
| `wt-impl` `qc21_check.py`, `controls.py` | git blobs `aa9cd82e…`, `b1d4bea4…` (as cited); HEAD `d87547a4a` (local, unpushed) |
| r5, r6, r7 drafts (Appendix D's provenance) | `d82af33c…`, `0120357a…`, `e75f0bc6…` (as cited) |

**Self-tests, run from the work-tree root:**
- `qc21_check.py --self-test`: 137 checks, 0 failed, exit 0, 2.5 s;
- `controls.py --self-test`: 160 checks, 0 failed, exit 0, 7.4 s.

***

## 1. The IMPL items

| # | verdict | note |
| --- | --- | --- |
| 2 | IMPL ✓ | SF-1 is defined at B-P's shape; its size follows D19 |
| **3** | **replay part IMPL ✓; verdict part IMPL only under D21(a): R13-B1** | Removing `parameters.dispatch_sha` is necessary, since S1's and `E`'s dispatch shas differ. "Not-applicable" at S1 is correct, because B6 runs at S1 and must be `success`. Dropping the S1-artifact condition: see R13-B1 |
| 4 | IMPL ✓ | pure-Python SHA-256; C-INDEP excludes it from `v_*` |
| 5, 6, 7 | IMPL ✓ | one `s_refusal`; the entry function; four builders; `t_builder_refuses` under the real environment |
| **8** | **IMPL ✓** | Reading A3b's step conclusion in place of the artifact's content keeps the rule. The evidence moves to a structured signal (§A.44). Both forms are self-reports of the run under test, so for a modified workflow neither is stronger. Rule (d) applies only at recorded-branch commits, whose `verify.yml` control W fixes, so A3b there is the frozen step |
| 9, 14, 18, 19 | IMPL ✓ | |
| **11** | **IMPL ✓** | Appendix D is faithful; see §4 |
| 12 (slot naming) | IMPL ✓ | `Acc` is symmetric in the slots |
| **13** | **IMPL ✓**, apart from D23 (SCI, posed) | See below |
| **15** | **IMPL ✓** | B-S4F is a genuine new test of step 4's feasible branch. `d = 3`, `r_S = 4` (so steps 2 and 3 are inapplicable), `m = 4`, `T = 3`. The writer's probe reproduces the triangle model exactly. By hand: the unit square lies in the triangle `(−½, −½), (5/2, −½), (−½, 5/2)`, with `(1, 1)` on its edge; the responses `5/8 − ω/4` lie in `[0, 1]` at its vertices |
| 16 (gating path) | IMPL ✓ | CC-NAT red gives C-VOID. The round-level effect is D21 |
| certificates | IMPL ✓ | A9 reads them in its own process, checked against their pins, and the result is A9's conclusion. The 652 KB file lands on `main` as needed evidence (§A.42 item 1) |

**#13's readings, checked.**
- **L-PATH (β)**, one free tick prepended. At odd ticks the encoded frame is `(v, u)`, so the phase now acts on `z`,
  the marker reads `x`, and the screen reads `z`. This is the conjugate assignment, path = `x`, and with it the source
  names exchange ("coherent" = `Z±`). That is correct, and it is a symmetry.
- **L-PORT (β)**: after a free tick the screen bit sits in `v_s`. Correct.
- **ABL-RECIP**: eleven arms. Its copy-only map `(u_a, v_a) ↦ (u_c + v_a, u_a)`, with the carrier on a free tick,
  matches the probes. Correct.
- **ABL-ENV-u and ABL-ENV-v**: as a set, each class is `Adm_B` without the hidden cell, and the two differ only in
  `decompose-p`'s SH-K role. Correct.
- **QM-P's `D`** as a trace distance is right for a QM control. The owner's no-trace-distance point concerns OI's
  validation layer.
- **`decide-b`'s range** (B-P and the built B-C fragments; construction A of B reported) is consistent with A's role
  as an A/B report. Whether A's `out_of_scope` makes B VOID is correctly D19(ii).

### R13-B1 (blocker): #3's verdict change is IMPL only under D21(a)

`verdict` no longer compares S1's artifact with the committed measurements. The reason is real: the artifacts API's
`digest` is the zip's sha256, and no frozen template or `zipfile` reads the content. The committed file is now bound
only to `E`'s recomputation, through B6 at `E`. Under deterministic replay this preserves "the committed record is the
frozen code's output under an approved dispatch", but it binds the record to `E`'s run, not to S1's.

**Under D21(a)** a red control or an `out_of_scope` makes B4 exit 3. S1's step conclusions then fail `verdict`, and
nothing is lost.

**Under D21(b)** a test-level VOID exits 0, so S1's output is never compared with anything. An S1 whose token differed
from `E`'s, for example from nondeterminism, would go undetected. `-I` leaves string-hash randomization on, so set
order can differ between interpreter runs. That is a "first computation, selected later" gap.

**Fix:**
- Add to D21(b)'s required edits: restore the S1 binding, either through a frozen `GET actions/artifacts/{id}/zip`
  template with `zipfile` in control B's import list (the S1 artifact's content compared with the committed file,
  excluding `dispatch_sha`; ARP-1's verdict did this), or through an equivalent S1-versus-`E` comparison.
- State in *The objects* and the note that the committed measurements are bound by B6 at `E`.

***

## 2. The SCI items (D19 to D23)

**The arithmetic is correct:**
- B-P: 32 preparations; 51 effects (2 + 8 + 8 + 32 outcomes, plus the unit); `d ≤ 18`.
- `C(32, 4) = 35,960`; `C(32, 5) = 201,376`; `C(32, 17) = 565,722,720`.
- `C(16, d − 1) ≤ C(16, 8) = 12,870`.
- B-C: up to 7 × 13 = 91 preparations; `C(85, 3) = 98,770`; `C(86, 3) = 102,340`.
- Construction A of B: 2⁸ = 256 outcomes against 200.
- Up to 4 × 150 = 600 instances can be flagged.
- D20: 8 × 23 × 150 × 151 ≈ 4.17 × 10⁶ propagations at depth 2, against 27,600 at depth 1.

**VOID by construction is correct.** Under D19(0)(b), (i)(c) and (ii)(a) with D21(a), B-P is over the generator cap,
so it is `out_of_scope`; the checker exits 3; and the round is VOID. Even under (0)(a), `d` can reach 18 and exceed
`d ≤ 16`, unless the number of distinct generators is at most 16.

**Neutrality.** D19 to D23 recommend nothing and state their Level, VOID and A/B consequences. D21 lists its required
edits. D22's options are accurate to the writer's QM probe, which I re-ran. A hand check of the on arm, slot 0 against
`X`, matches.

### R13-B2 (blocker): D19 is missing options

These options do not narrow B-P, and the owner should see them before choosing a narrowing:
- **(0)(c) Count generators as the extreme rays of `cone{a_p}`.**
  - The facets of `cone{a_p}`, which are all that steps 2–4 and the verifier use, depend only on its extreme rays.
  - Removing non-extreme rows, with each removal certified by an exact nonnegative combination that the verifier
    checks, changes no decision. It can bring the unnarrowed B-P within `n ≤ 16`.
  - `n_extreme ≤ n_distinct ≤ 32`, and its value is unknown before `F`, as with (0)(a).
- **(i)(d) A sufficient covering by sub-fragments.**
  - B-P is declared B-CONTEXTUAL if some frozen sub-fragment of at most 16 preparations, with the same `Acc`, is
    infeasible with a verified certificate. A noncontextual model of the whole restricts to every sub-fragment, so this
    is sound.
  - If every sub-fragment is feasible, B-P is "not decided", not imitable.
  - It is one-sided, and that must be stated with it.
- **(i)(e) A different exact facet enumeration** (for example, a double-description method) in the solver and the
  verifier, under the timeout test.
  - It is a method change under D10, so it needs its own review.

Also state, with (0)(a) and (0)(c), that `d ≤ 16` can still fail, because `d ≤ 18`.

***

## 3. Implementation fidelity (static reading and self-tests only)

**Implemented as r13 states:**
- #3's replay core: `replay_compare` pops `dispatch_sha` on both sides and compares canonical JSON. S1 with no committed
  file gives exit 0.
- #5 `s_refusal`. `os` occurs at exactly two `os.environ` sites.
- #7: `DECISIVE_BUILDERS = ("s_build_p", "s_build_repinv", "s_build_b", "s_build_c")`.
- #9: `"workflow_dispatch"` occurs only in `run_class_dispatch`.
- STAB-FALSE in `controls.py` with the pinned certificates. Its self-tests pass.
- `verdict_mode` already omits the S1-artifact condition (R13-B1).

**Not yet as r13 states** (to be fixed before the pins are taken at `F`):

| C.8 item | r13 text | scripts |
| --- | --- | --- |
| 3 | prints `{"replay":"not-applicable"}`; exits 3 on mismatch | plain text; exit 1 |
| 4 | `h_sha256` in namespace `h_*`; three FIPS vectors | `sha256_hex`; two vectors (`abc`, empty) |
| 5 | `s_entry(argv, environ)`; `s_refusal()` with no argument | `run_entry`; `s_refusal(name)` |
| 7 (#8) | A3b `fixture-mode-check`; rule (d) reads A3b's conclusion | no `fixture-mode-check`; rule (d) still reads `fixtures_mode` (`controls.py:1656`) |
| 9 (#18) | `evidence/approvals.json`, schema v1 | absent |
| 10 (#19) | `--fixture-output` is not a flag | still a flag (`qc21_check.py:12, 3696`) |
| B-S4F (#15) | a fixture-mode control | absent |
| 8 (#9) | `SPLICE_*` constants hold the splice | absent (permitted, not required) |

The scripts are references and the pins are frozen at `F`, so this is not a text blocker. But precondition 5's review
must see scripts that match r13.

***

## 4. C.8 and Appendix D

- **C.8.** Items 1–13 are consistent with PLAN §20 and with the body's references. Item 12's placement of STAB-FALSE
  (A9, outside B4's process, so outside C-STATELESS's comparison) is argued correctly.
- **Appendix D.** Every unit marked *verbatim* is in the cited draft:
  - D.1's input rows;
  - D.2's method and the fixture-law rows;
  - D.3 and D.4's model and quantities;
  - D.5's C-NONSTABILIZER, C-SURVIVAL and C-VOID quotes;
  - D.6's rows carried from r6 and C-EMB's r5 row;
  - D.8's r5 renaming table (8 of 8 rows);
  - the r6 "Which direction is the obstruction" passage, which differs only by a line-break hyphen ("Schmid–
    Spekkens");
  - the r7 NR-15 line, apart from one comma.
- The units the text check flags are labels, declared adaptations, or this file's own additions. D.7's three phrases
  added in r8 fall under "and this file".
- **The orbit adaptations of Appendix B (D.6) are sound:**
  - CC-DYAD on orbits holds by dyadic descent: unconditioned rounds keep dyadic laws, `Λ_{y,b}` is dyadic, and an
    orthogonal dyadic `β` is a signed permutation.
  - C-FRAME under rule 0 with `k = 1` fits the transposition.
  - C-XB on `O_11` and C-SCOPE are correct.
  - Each is a decisive-mode control.
- D.5's C-EXPOSURE prints the "orders 3 or 6" sentence only when `STAB(K)` is true, which is faithful to the cone
  review.

## 5. Regressions

None found. The diff against r12a is confined to the nineteen items, the certificates, Appendix D, the r12a nits and
the edit-log rows 45–71. The stop rule is restated consistently with D21.

## What remains before `F`

1. **R13-B1.** Add the S1-binding requirement to D21(b)'s required edits, and state the `E`-binding in *The objects*
   and the note.
2. **R13-B2.** Add D19 (0)(c), (i)(d) and (i)(e), with their consequences, and the `d ≤ 18` caveat.
3. **The owner's decisions D19 to D23**, recorded with author and time. Freeze readiness requires that no ambiguity
   remains.
4. **The scripts brought to r13** (§3's table), then re-run of the self-tests and the design run.
5. **Everything listed at r12:**
   - the `PENDING` fields;
   - D9(a)'s landings;
   - the confirmation run and C.7's gate tests;
   - the owner's freeze commitments;
   - the round PR with the fields filled, and precondition 5's review of the filled plane and the scripts' blobs;
   - the `F` dispatch and the designation request.
