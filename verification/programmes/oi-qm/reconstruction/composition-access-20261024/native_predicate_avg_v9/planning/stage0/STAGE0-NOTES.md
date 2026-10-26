# Notes on the NP-AVG-1 Stage 0 plan

## Inputs read
- `review/RECHECK-r2.md`, SHA-256 `676ecc08…a7`. Its §1 is the collapse
  argument; §3.2 gives the cone radii; §3.3 covers the union method.
- `review/toy/cones.py`, the reviewer's cone-radius check.
- `draft/PLAN-r2.md`, SHA-256 `c9d8dbf8…c2`.
- v8 `REPORT.md:19-21, 37`, the per-family "every R" negative and the
  zero-background diagnostic, cited by C_G.

## What was run (owner-approved design controls; nothing on v8's class)

Directory `npavg/stage0-design/`. Python 3.13.16, `python3 -I -B`, standard
library, exact integers.

| file | SHA-256 |
| --- | --- |
| `sym_check.py` | 2c818b4360bf38bf7486b088aab5d999811ee28ce3ecfe5874e924419aa8c35a |
| `sym_check.out` | 76779524835103d032eda1d2170a6c1a4e57d5fb9cdb342835f5c03056c2d8b5 |
| `toy_closure.py` | 5e7a3b75f23ef71de4a14673054d4a588900c6e4c667c1a0d48394fbef4ed87a |
| `toy_closure.out` | 053c672291ce4382fd1618b76f1bbc6f38002956d21d09a04124664493f64e6e |
| `toy_block.py` | 2d251c61907e94ec79c2b945c30338101e094524c9647678bc2a276667bdeb3c |
| `toy_block.out` | bcacf1e1b3dfbcc1cdf8ee0c7a2d9a38875b24725f6a4c3feb9acaf771fb92a9 |
| `toy_fartip.py` | d737ad9e3597f9a7068926729a996d323b90e76a3769a975767833fd1fa4fa45 |
| `toy_fartip.out` | 401fe8bede723017c4781bb1cc07523334c2da887790d0849248b42beedb3db6 |

**`sym_check.py`** (20 s) checks configuration combinatorics only:
- group orders: O_h 48; masking geometry 48 without the port and 8 with it;
  labelled roles 8;
- ℓ¹-ball counts equal A001845 for r ≤ 11;
- 3,225 items; 5,160,000 pairs;
- orbits 875 and 815,175, equal by direct canonicalization and by Burnside.

No closure or law was computed.

**`toy_closure.py`** (7 s) runs on toy geometry only: pair (2, 3), regions
ball(1)–ball(2), no streams, no port. Results:
- the hand instance collapses;
- 0 self-supporting sets of size 1–3 in a 75-quantity pool;
- a 14-quantity block retains 8;
- symmetric radii retain strictly more in 160 of 400 random sets, and never
  less;
- the off-axis mutant differs in 0 of 400 random sets, so random tests are
  insufficient (see `toy_fartip.py`);
- in the native toy, the influence radius is (d − 1, d) at depths 1–4, and
  axis-tip bijection failures are 0 of 300;
- 2.65 ms per closure with 30 quantities plus 8 fixed.

**`toy_block.py`** shows the 8-quantity core:
- the core is the dynamical-constraint block: (0, L+1), its six slice-L
  neighbours, and the slice-E centre;
- it is a fixed point;
- removing the centre leaves 7 under the near-only rule; removing anything
  else collapses it.

**`toy_fartip.py`**, on toys:
- the far-slice axis extreme at distance d − 1 is bijective in 200 of 200
  cases; an off-axis far cell fails in 87 of 100;
- block minus its centre: L3 retains 7, L3′ retains 0;
- the depth-2 planted set is retained 13 of 13 by L3′ and 0 by the off-axis
  mutant;
- L3′ ⊆ L3 in all 300 random sets.

## Hand-checked toy instances (C6)

Pair (E, L); F depth d = t − L. Near cone: radius d on slice L. Far cone:
radius d − 1 on slice E.

1. **q1 = ((0,0,0), L+2) and q2 = ((1,0,0), L+1).** Both have the +x tip
   (2,0,0) on slice L. q1's tip (−2,0,0) is at distance 3 from q2, outside q2's
   radius-1 cone, so it is free and q1 goes. Then every tip of q2 is
   uncovered, and q2 goes. Closure: ∅. The code agrees.
2. **The constraint block** {top = (0, L+1); the six (±e, L); centre (0, E)}.
   - Every near tip of top is one of the six, each of which is retained.
   - top's far tip is the centre, which is retained.
   - Each of the six (depth 0) has its tip in top's near cone.
   - The centre (B, depth 0) lies in top's far cone, of radius 0.
   - All 8 are retained.

   Without the centre:
   - under L3′, top's far tip is free, so top goes, and then the six go;
     closure ∅;
   - under L3, top's near tips are still covered, so 7 remain.

   That L3′ is right is the physical fact x_{L+1}(0) = x_E(0) ⊕ H(Σ six):
   with x_E(0) fresh, top is independent of the six. The code agrees.

## Interpretations and additions

1. **Far-slice tips (L3′).** This addition is mine; neither the review nor
   the re-check contains it. A depth-d site-time is also a bijection of its
   far-slice axis extremes at distance d − 1, because x_E(u) enters the
   dynamics only via x_{L+1}(u) = x_E(u) ⊕ H(…). It is checked natively on toys
   and is sound. Adding tips can only strengthen elimination, so the re-check's
   necessary conditions remain necessary. The plan freezes L3′ for the labels
   and reports near-only L3 beside it (S2). The reasons:
   - the re-check's argument is stated for L3;
   - comparing the two exposes the records that only the far tips mask.
2. **P_A and P_G** restate the re-check's argument in a cleaner form: the
   ρ-maximal element's aligned near tip must be shared. The facts that make
   this work:
   - an opposite-type cover needs reach greater by at least 1, so a ρ-maximal
     element cannot have one;
   - fixed quantities cover only Φ site-times;
   - the aligned tip of a non-fixed quantity is never a Φ site-time;
   - under G, an element with a seed tip has |c| + t > 8, so its aligned tip
     is a seed.

   These are proof obligations PO3–PO7 for the report.
3. **Fixed versus eliminable quantities.** Φ and p are fixed. The port samples
   are eliminable under A, and in-frame (hence retained) under G. Making the
   port fixed would break P_A, since the port's B-cones are large.
4. **Global closure bound (S1a).** It follows from monotonicity (PO4): the
   closure of the union of all items' samples bounds every record's retained
   set, for any k. It is proposed as the k-independent answer to "the smallest
   record that masking does not wipe out" before any search (S1b).
5. **S6 (exact check of PO8)** is a law computation, so it is listed for the
   owner in a stage that is otherwise geometry-only.
6. **Timing** comes from toy prototypes, not from v8's class. The real cost is
   measured only after launch.
7. **The literature list (§8)** names candidates from memory. The references
   were not consulted, and the report must check them before citing.
