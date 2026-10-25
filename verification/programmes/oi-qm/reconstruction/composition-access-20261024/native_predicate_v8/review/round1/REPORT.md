VERDICT: ACCEPT WITH NITS — 375a29e4aa824183e71c0b60abd9cd321617081d (native_predicate_v8, plan 631bec0ca55eacbf6a7cf7e72d72c673dfe430da, on afc7bced6720ee6b3ce27207423d1f56f5851779)

Independent read-only review of PR #912's passive-native-readout test. I wrote and ran nothing in the clone.
Reviewer files are under `indep/`. Replay outputs are in `run1/`, `run2/`, `runmut/` and `runmut2/`, and my
mutant workspace is `mymut/`. Package files exported from git are in `pkg/`.

The scientific result holds within its stated scope. I re-derived the scaled native fields, histograms and
law tests in four backgrounds with independent numpy code, and they match exactly. The 20/44 argument is
exact. Every control can fail, and the decisive law statistic is live. One retained-evidence recipe is
broken: the mutant replay command as documented does not work (F1). It must be fixed before landing. It
does not affect the verdict.

## Ranked findings

**F1 (must fix before landing; replay defect). The documented mutant recipe fails from an empty directory.**
The REPORT replay is `mkdir mut && python3 -I -B "$D/mutants/run_mutants.py" "$D/checks.py" mut`.
`run_mutants.py` writes each mutant to `os.path.join(work, name)` and then runs that relative path with
`cwd=work`, so the interpreter looks for `mut/mut/<name>.py`. Run exactly as documented (`runmut/`), every
mutant is `UNPARSED` ("can't open file …/mut/mut/m1_scalar_H_or.py") and the output has
`all_caught: false`. The script still exits **0**. With an absolute work directory (`runmut2/`) the output
is byte-identical to `mutants/mutants.out` (5 min 26 s).
Fix: `work = os.path.abspath(sys.argv[2])`, and `sys.exit(1)` unless `all_caught`. Then regenerate
SHA256SUMS. `mutants.out` itself does not change, because it contains no paths. `PROVENANCE.json`'s
`mutant_command` uses the same relative form and should be checked once the script is fixed.

**F2 (nit; control gap). The scope parameters are not pinned inside the checker.** My mutant R1
(`REGION = ball(RHO-1)`, 1,575 site-times) and R8 (`TEND` reduced by 8, reads to L+9, 2,193 site-times)
both exit 0 with `NEGATIVE_FOR_CONSTRUCTION`. The hard-coded scope string still says C(4,16). Comparing the
output with `result.json` would catch either, because `scaled_parameters` would differ, but the checker
does not. Fix: add `need(len(REGION) == 129 and len(SITE_TIMES) == 3225 and TEND - NS == 17, ...)`, or
generate the scope string from the parameters.

**F3 (nit; mutant coverage). m4b never reaches x4.** By itself this leaves x4's reduction-side test (the law
statistic) without a mutant that reaches it, since m4a breaks only the direct `proportional` side. I
checked the gap. My R7 makes `law_of` accept any split with block sizes 20/44 regardless of the J counts.
It is caught at `x4_planted_negatives_rejected_and_encodings_accepted`, through the permuted-threshold
plant, whose blocks are also 20/44. So x4's reduction side is live. Recommend adding R7 to
`run_mutants.py` as m4c, so the package itself shows this.

**F4 (nit; wording, REPORT "Result and scope").** "Per family, 2,224 to 2,226 site-times are constant given
C0" is off by one. The histogram bin `1` counts cells that are trivial *given V*. Exactly one of them in
each family I checked is the V cell itself, (0,0,0) at slice n+2, which is not constant given C0. In
seed 3, 2,223 cells are globally constant plus V (`indep/trivial_nonconst.py`). Suggested wording: "carry
no information beyond V given C0".

**F5 (nit; scope wording).** The REPORT title line and the commit subject say "not an admissible acceptance
flag in C(4,16)" without "scaled". "This test settles that form for the class above" should read "…for the
class above, in the scaled control". The body's scope list is correct. Only these two headline phrases
drop the scale qualifier.

**F6 (nit; scope clarity).** Conditioning on the whole dirty background C0 is exactly what stops background
bits from acting as v6-style fair pads. So the two listed exclusions ("mixture over private backgrounds"
and "fresh initially-fair pads") are one open branch, not two. A one-sentence link would stop a reader
from treating the C0-conditional negative as closing the pad route. The REPORT already lists both, so
nothing is overclaimed.

**F7 (propagation note).** `CURRENT-HANDOFF.md` still lists "a cheaper native predicate" as the next gate
and does not mention v8. That matches the precedent (v7's handoff line came after its review). The v8
result should go into the handoff, in its scoped form, when the review lands (§A.25/§A.27).

**F8 (informational).** The x7 "scaled G arrival = actual − (L−n)" check holds by construction: the
offsets are identical and the region lies in the linear regime of |x₀+n+1|. It confirms the transcription
of the source offsets, not dynamical faithfulness. The REPORT does not claim more.

## Evidence per check

### 1. Preregistration — PASS
- `631bec0c` adds only PLAN.md (180 lines), committed 03:56. `375a29e4` adds the computation at 04:18, and
  the plan's parent is `afc7bced`.
- The verdict follows PLAN.md's decision rule: HOLDS needs a common, stream-closed, tail-free R with a
  consistent accept map; NEGATIVE otherwise with controls green; VOID on a failed control or an undecided
  search. The checker implements exactly that, and the caps (10^5 per family, 24 common) were never hit.
- Post-plan items are disclosed in PROVENANCE.json, and REPORT names the cell list. None of them weakens a
  control:
  - the two-block cell list is reported only;
  - the trivial-cell omission cannot change a decision, because an all-trivial cell never equals a
    nontrivial pick in the cover test, so the decision is unchanged;
  - the injection argument is inert unless set, and x1 excludes only the injected key;
  - m4a was added after m4b was found to be caught by the cap, with both kept.
- The m4b target was widened to `search_decided_family|x4`. That is disclosed, and F3 shows x4 is live
  anyway.

### 2. The reduction — PASS (exact)
- `indep/arith_geom.py`:
  - For s=0,1, t1 = (5,5,0,0,4,4,1,1) and its s-swap, and t0 = 8−t1. Both contain coprime entries (1;
    3 and 4), so any class whose counts are proportional to a target is an integer multiple ≥1 of it.
  - The only nonnegative integer solution of 20a+44b=64 is (1,1). So for each V value there is exactly
    one accepted class with counts exactly t1 and one rejected class with counts exactly t0, and the
    cell-wise consequences in PLAN step 3 follow.
- **"For some predicate" is fully captured.**
  - The public record is (old q9, V, w_R, ports). Given C0, old q9 is fixed.
  - The port streams through H ≤ 2L enter only through v7's factorization. They are bank-padded and
    uniform given (C0, G), and tail-free w_R does not touch the bank, so they cannot help a predicate.
  - The carrier is private. The record must leave J independent of w_R given (V, A'), which is exactly
    the per-(V,w_R)-class posterior condition.
  - The per-family search also lets the predicate (and R) depend on the background. That is more
    permissive than a public predicate, and it still finds 0.
- **C0-conditioning.**
  - C0-conditional is the form in which v6 and v7 state their *positive* laws ("conditioning on eta is
    stronger"). For a *negative* it is the weaker exclusion.
  - A mixture can succeed where every C0-conditional law fails. Example: a cell (A, Y⊕c, ·) with c a fair
    background bit leaks Y given C0 but not on average.
  - The REPORT excludes this case explicitly, and the PLAN fixed it in advance. That is acceptable as
    scoped (see F6).
- **Independent re-derivation** (`indep/rederive.py`: numpy periodic cube with every read cone inside,
  own H table, own J map; imports nothing from checks.py):
  - In seeds 3, 14, 37 and the zero background, the max-blocks-given-V histograms equal `result.json`
    exactly. In each of the four, 0 cells have a law-good two-block split and 0 cells are heralded, for
    every V value (`indep/rederive.out`).
  - The two-block cells split every V value 24/40, 32/32 or 16/48, never 20/44
    (`indep/rederive_allv.out`). So the negative does not depend on the carrier-coordinate map at all.
  - The family seed scan reproduces the chosen seeds 3,6,…,37 exactly (`indep/seedscan.py`).
- **Reviewer probe beyond the class** (`indep/coarse_probe.py`, seeds 3 and 14): no single G-dependent cell
  (1,002 and 1,000 of them) has *any* coarsening, i.e. any V-dependent union of its classes, with counts
  exactly t1 for even one V value. No fixed linear bit of a cell works either. So the failure is not an
  artefact of whole-triple reading. This supports the REPORT's "what the cells carry" explanation at
  single-cell level. It is POSITIVE for the explanation, not a new claim.

### 3. Faithfulness — PASS (scaled, as stated)
- The rule H = (0,2,4,7,1,3,5,6) and the two-slice XOR-of-six-neighbours update match v7 `checks.py`.
  Source offsets (−(n+1),0,∓1), (−(n+2),0,0) and the xorshift background generator match v7's scaled
  control.
- The phase map matches v6's bit layout: V, Q8, Q10, M, C0–C2 in A/B/D order, with Y=4 (Q8.B), R=8
  (Q10.D), Z=7 (Q10.B), K=(3,5,6) (Q8.A, Q8.D, Q10.A), and s-inputs (1,5,8,11,14,17,20).
- The dirty radius 27 = ρ+n+1+τ covers every read cone.
- Uniform dirty backgrounds are legitimate counterexamples only as members of a generic scaled family. They
  say nothing about the actual-L background, which the REPORT states.
- Geometry, independently recomputed:
  - over 129 offsets, the first tail arrival is L+74 to L+82;
  - every read through L+17 is tail-free (window to L+73);
  - G first reaches the region at L−2, and the scaled−actual mapping holds at all 129 offsets (F8);
  - v7's carrier table (q8, m, q9+x, q9+y: 77; q9: 78; q10, q9−y: 79) is reproduced.
- Time parity: the dependence graph preserves (t − dist) mod 2, and every source has the same parity. The
  site-times that can depend on G by cone and parity number exactly 1,002. All of them depend on G in seed
  3; in seed 14, 1,000 do.
- "Operands are delivered": x2 holds in all families in the scaled control (bijective pool at n+1,
  seven-site inverse, phase sign, V uniform). At actual L, delivery is inherited from Native A. The REPORT
  sentence sits inside the scaled "here" context, which is acceptable.

### 4. Controls and mutants — PASS (with F1, F3)
- With an absolute work directory, all 11 author mutants are caught as targeted, byte-identical to
  `mutants.out`.
- m9 (injected (0,A,0) at (4,0,0), slice 12) turns the verdict to HOLDS. So stream closure, the common
  search and the accept-map step can return a positive on native cells.
- My mutants (`indep/my_mutants.py`, `indep/my_mutants.out`):

| mutant | change | outcome |
| --- | --- | --- |
| R2 | Y := Q8.A consistently in A and J | VOID x3 |
| R3 | target sign flipped | VOID x3 |
| R4 | `law_of` one block orientation only | VOID x3 |
| R5 | native injection of permuted-threshold A (20/44 split, wrong law) | NEGATIVE (correctly rejected) |
| R6 | native injection of (0, A⊕V.B, 0) | HOLDS (V-dependent predicate found natively) |
| R7 | law accepts any 20/44 split | VOID x4 (F3) |
| R1, R8 | search domain shrunk | uncaught, still NEGATIVE (F2) |

### 5. Scope and wording — PASS (with F5, F6)
- The REPORT limits the negative to C(4,16), passive whole-triple readout, the scaled n=6 dirty families,
  and the C0-conditional law.
- It lists the following as not excluded: pads, prepared sources, other source families, gates and
  compilation, larger regions or later reads up to L+73, mixtures, and an actual-L predicate.
- It states that the carrier remains v6's supplied logical storage, and it adopts no access rule, native
  storage, clock or A1/A2 claim. `result.json` carries the matching false flags.
- The dismissal of option (a) is argued, not overclaimed:
  - The fixed-site failure is v6's scaled one-tick delay control, cited as such.
  - "Re-encoded by the exact native inverse … equals v7's law by identity" is correct as stated: if the
    decoded variable is the same random variable, the joint law is unchanged. It leaves decoder
    availability (compilation) open.
  - It is presented as "not decisive as a computation", not as a no-go.

### 6. Replay and hygiene — PASS except F1
- `python3 -I -B checks.py` and `python3 -I -B -O checks.py` from an empty directory exit 0, and both
  outputs are byte-identical to `result.json`. A run took 118 s under parallel load.
- `sha256sum -c SHA256SUMS`: all 7 files OK.
- The REPORT verdict (`NEGATIVE_FOR_CONSTRUCTION`) and every quoted count match `result.json`:
  - histogram ranges 2,224–2,226 (see F4), 921–925, and 2–6;
  - x5: 2,046 subsets, 28 passing;
  - zero-background cells (−2,0,0)@6 and (2,0,0)@10.
- Hygiene of the package:
  - No absolute paths, emails, IPs or tokens in the package files.
  - No `__pycache__` in the tree.
  - The diff `afc7bced..375a29e4` touches only `native_predicate_v8/`.
  - The checker reads no repository file and imports only the standard library.
- Repository tools, run from the clone root:
  - `tools/duplicate_check.py`: OK, on the whole repo and on the package.
  - `tools/voice_check.py`: OK (40 manuscript files).
  - `tools/artifact_placement_check.py`: OK (self-test passed).
- Afterwards: `git status --porcelain --ignored` is empty, and HEAD is still `375a29e4`.
- The documented mutant command fails (F1).
