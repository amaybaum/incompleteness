ACCEPT WITH NITS — 2c43d615a440c2b837dc19f410759d01a47e5362 (native_vread_v15, plan ead2c38842222786c68551484b708c19f29c83ab, base bef79f6f3daec0b734a7d9c6a9423ed634852818)

Independent, read-only review. Package: `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/native_vread_v15/`.
All Python ran with `python3 -I -B` from an empty directory on files exported with `git show`. Reviewer
material in this directory: `indep/verify.py` (own re-derivation, imports nothing from the author),
`indep/verify_out.json`, `indep/rev_mutants.py`, `indep/rev_mutants_out.txt`, `indep/mutwork/` (mutant
sources), `tree/` (export of the native-y-continuation directory at 2c43d615), `replay/` (recipe clone).

## 1. Preregistration — PASS (with one wording nit)

- ead2c388 adds only `PLAN.md` and its line in the directory `SHA256SUMS`; 2c43d615 adds only the
  other seven package files and their seven manifest lines. `PLAN.md` is byte-identical between the
  two commits; its SHA-256 `e24c1632…` matches PROVENANCE.json and both manifests.
- Outcome against the rule: rule 2 needs at least one non-q10 key that is FREE and passes the receiver
  check. Two do (−x, +y; nearest receiver L+79), so NEGATIVE_FOR_CONSTRUCTION is the rule's outcome.
  The text is generated from the measurements, and every control runs before any verdict code.
- Post-plan changes:
  - **Parity in K2.** This corrects the code, not the rule. The plan's own proof sketch
    (|c−q9| = L+2) already uses parity. I checked the parity form against the rule's own dependency
    propagation over both initial slices for n = 1..6: 0 mismatches in 9225 cell tests. It weakens
    nothing.
  - **SHA-256 family and the relaxed countercontrol ("at least one SHA-256 world").** The plan says
    the effect "must be observed", without saying how often. Whether one off-axis cell actually
    changes two neighbours depends on the background under the nonlinear H. My random backgrounds
    show it in 19 of 20 worlds, and the author's SHA-256 family in 11 of 12. A per-world reading
    would therefore VOID under any family, while one observation is enough to show that the check
    can discriminate.
    - The relaxed rule would also pass with the polynomial family alone (my mutant
      `STRENGTHEN_counter_polynomial_only`). So the added family is not what makes it pass.
    - A stronger rule, at least one SHA-256 world for every n, also passes
      (`STRENGTHEN_counter_every_n`).
    - The positive K3 checks still have to hold in all 144 worlds, so the relaxation does not touch
      the parts the verdict rests on.
    - That both changes came before the verdict is the author's own statement. Git cannot confirm it,
      because execution is one commit. It does not matter here: the verdict is the same under every
      variant.
  - **Extra anchors and the replaced (equivalent) mutant.** These only add strength.

## 2. Central claim — PASS (verified independently, exact integers and Fractions)

- **Axial-key lemma.** I propagated dependency sets from the native second-order rule, not from the
  formula, for n = 1..6:
  - The current-slice keys of V at n+1 are exactly the six cells (n+1)e.
  - The previous-slice keys are exactly the six cells n·e.
  - K2's countercontrol count of 772 equals Σ_{r=3..8}(4r²−4), the number of non-axial cells on
    those L1 spheres.
- **Classification at actual scale** (`indep/verify_out.json`, C_keys):

  | Key | Cell | My classification |
  | --- | --- | --- |
  | +x | (L+2,S,77) | pinned; port-4 ball, margin −399 |
  | −x | (−(L+2),S,77) | free; nearest ready ball at margin 2 (the q9 L-ball and B_(L+1)(q10)); nearest local source at distance 2 (F8, F10); inherited sources ≈ S away; on no bank ray |
  | +y | (0,S+L+2,77) | free; ready margin 2; nearest source selector_y at 156 |
  | −y | (0,−79,77) | free; ready margin 2; E at distance 2; inherited source at 156; reaches port 0 at 341 |
  | +z | (0,S,S+156) | this is N, inside B_(L+1)(q10) |
  | −z | (0,S,−S−2) | pinned; ball ((0,S,−68),R) |

  - Receiver distances: −x and +y are at L+79, −y at 341. Torus distance (side 256L+64T+1) equals L1
    distance for every receiver.
- **Is the inventory complete?** The 24-ball list is the same as in native_route_v13 `geometry()`,
  native_seed_v12 and history_v11.
  - branch_v10's lists, and history_v11's "selected" list ((0,S,76),L−1), ((0,S,77),L),
    (±48L,0,0),L), are all contained in it. Checked as extra balls, they pin no further key.
  - The herald source family (near 49L) and the remote program sources (inside the ±12R and ±48L
    balls) are not in v15's list. They are at least 46L away, which is harmless.
  - Grepping for B_(L+2), "blank shell" and "readiness extension" finds no declared region at L+2
    about q9. native_x_v12 explicitly declines a blank shell.
  - I found no missing region. Completeness is still an input assumption that no control can detect
    (finding 4).
- **The native_v11 unique-axial-path argument at actual scale.** It is an induction that holds for any
  length and any background. At step j the old term (time j−2, distance j) and the five other
  predecessors (distance j+1, time j−1) cannot depend on the key, so each step is
  XOR∘H∘XOR, a bijection. This holds for the −x and +y paths of length L+1.
  - p (distance L+2 at time L), q10 at L+1 (distance L+3) and the other four neighbours (L+3) do not
    depend on the key, so V is a permutation of it.
  - My random-background native worlds (n = 1..5, 4 seeds, 6 keys, 120 worlds) confirm: V and the key's
    own neighbour are permutations, and q9 at n−1 and the other five neighbours are constant.
- **One-time pad, exact.**
  - For every (p, c, rest), m ↦ p⊕H(c⊕m⊕rest) is a bijection (all 512 cases).
  - I put arbitrary non-uniform rational weights on all other variables (p, q10 code, residual). With a
    uniform key, Pr(V, others) = Pr(V)·Pr(others) exactly and V is uniform.
  - Countercontrols: a key skewed by ±1/16, or a fixed key, gives exact dependence.
  - On the retained table (fewest-seed law [1,5,1,4,1,5]): 48 accepted rows; old q9 = (0,s,s⊕a⊕b) on
    48; q10.A = s on 48; q10.A⊕p.D = a⊕b on 48; 4/4 distinct q10 codes; 384 uniform cases. v14 records
    1456 laws for readout 240.

## 3. Scope and framing — PASS with nits

- **The hybrid test case.** PLAN and REPORT say plainly that using Native A's read with the route_v13
  geometry is a test case and that neither contract is adopted. Native A's harmlessness argument came
  from a fair F9. Here the same cell is an unrestricted complement cell, and REPORT says so.
- **The −y key** is left as "not computed" and is not implied harmless. Correct (but see finding 2).
- **Privacy is conditional on a uniform key** in the verdict, in not_established and in Scope.
  - Exception: the REPORT "Result" summary paragraph states the one-time pad and harmlessness without
    the condition (finding 1).
- **The negative is stated for this construction only**, with no OI-wide no-go. The untested items are
  listed: multi-tick route to port 5 (78 ticks; checked: dist(q10, port 5) = 78, ports 2 and 3 at 448),
  other reads and layouts, readiness extensions, previous-slice keys, Native A's geometry and pool,
  acceptance predicate, carrier law, A1/A2, and OI generally.
- **Diagnostics.** No section called "Accounting for B and D" exists in REPORT.md or anywhere in the
  native-y-continuation directory. I checked the nearest diagnostics instead:
  - The read-algebra formulas hold on all 64 (p, Σ).
  - "q10.A ⊕ p.D = a⊕b on 48 rows" and "4 distinct codes per s" are reproduced.
  - The bank shell is reproduced: 8 coordinates, 4 active at L+2.

    | Bank coordinate | q9 neighbours reached at L+1 |
    | --- | --- |
    | port 0, deadline+2 | −y, −z |
    | port 2, deadline+2 | +x, +y, −z |
    | port 3, deadline+2 | −x, +y, −z |
    | port 5, deadline+2 | +y, −z |

    This matches native_x_v12 ("M1/M2 and the first two post-deadline coordinates of rays 2, 3, 5").

## 4. Controls — PASS

- The author's 21 mutants reproduce `mutants/OUTPUT.txt` byte for byte.
- I wrote 25 more mutants (`indep/rev_mutants_out.txt`). Every control-violating mutant VOIDs on its
  own label:
  - K1: v14 pin, truncated table, source count.
  - K2: cone shifted to previous-slice semantics; cone widened; countercontrol threshold.
  - K3: H made non-bijective in *both* evaluators (so they still agree); key planted in the previous
    slice in both evaluators; countercontrol cell moved out of the cone; off-axis keys.
  - K4: non-uniform (7-value) key law; operand outside the cone.
  - K5: q9 ball inflated by 2 (caught by the F8-free anchor); q10 extension radius.
  - K6: q9 payload codes; shell parity; s = x⊕u; E/N avoidance.
  - G: a non-bijective map in the table check.
- **Survivor: `K5_E_moved`.** Moving E in the classifier's source list leaves exit 0 and the same
  verdict. E, N, F10 and the q10-axial cell all lie in B_(L+1)(q10), so these anchors pass through the
  ready ball whatever the source list says (finding 3). Requiring the (status, reason) tuple catches it:
  `K5_strict_anchor_with_E_moved` VOIDs.
- **Verdict-change mutants.** These are not controls. They show the outcome responds to the inventory:
  - a zero-radius ready region at the −x and +y keys → NOT_DECIDED_BY_THIS_PLAN;
  - at −x only → NEGATIVE with +y alone;
  - a receiver near +y → NEGATIVE with −x alone.
- **The countercontrols do not reproduce the claim.**
  - K2's counts the cells that reach two or more neighbours.
  - K3's off-axis cell must change two or more neighbours, the opposite of the key property.
  - K4's pinned-key positive (total variation 1) is the complement of the null.

## 5. Replay — PASS

- Normal and `-O` runs are byte-identical to `result.json` (0.8 s).
- The package `SHA256SUMS` (7 entries) and the directory `SHA256SUMS` (389 entries; the set equals all
  files except itself) both verify.
- The REPORT recipe works in a fresh clone (`replay/`, a shallow clone of the branch, checkout of
  2c43d615): checker normal and `-O`, mutant run, and `sha256sum -c` all pass.
- No `__pycache__` was produced, and `git status --ignored` is clean.

## 6. Hygiene — PASS

- The new files contain no absolute paths, secrets, e-mail addresses or IP addresses.
- The diff from bef79f6f contains only the 8 new package files and the directory `SHA256SUMS`.
- Run from the clone root:
  - `tools/duplicate_check.py`: OK, for the whole tree and for the package.
  - `tools/voice_check.py`: OK.
  - `tools/artifact_placement_check.py`: OK; the self-test passes.
- The worktree and HEAD are unchanged afterwards.
- REPORT.md's quoted verdict, unwrapped, equals `result.json` `verdict.statement` exactly
  (1262 characters). The heredoc kept `$D` and the backticks literally, and the numeric claims match
  result.json.

## Findings (ranked), with fixes

1. **(Nit, claim/evidence boundary.)** The REPORT "Result" summary says the whole-V read "is a
   one-time-pad ciphertext … keyed by complement cells" under the route_v13 contract, and that "Its
   harmlessness and its emptiness have the same cause". Both are stated without a condition. Under the
   contract the key law is unrestricted. Without a uniform key, only (i) is established: V is a keyed
   permutation and no fixed readout works for every complement value.
   *Fix:* write "under a uniform free key, the read is a one-time pad …; its harmlessness then has the
   same cause as its emptiness".
2. **(Nit, generated verdict text.)** The verdict names two unseen keys, then says "needs at least these
   3 free key cells known".
   - For the −y key, the list "pinning … or reading their q9 neighbours" is not exhaustive: port 0's
     permitted record depends on it and might determine it. This is not computed.
   - "their joint law is not computed" applies only when no unseen key is uniform. Under (ii), V is
     independent of port 0's record.
   - The plural is wrong when there is one extra key: "1 further such keys".

   *Fix:* "needs the 2 unseen free keys known (pinning, or reading their q9 neighbours at L+1); the −y
   key must also be determined, by pinning, by reading, or from port 0's record (not computed)". Fix
   the plural.
3. **(Nit, vacuous anchors.)** The K5 anchors for E, N, F10 and the q10-axial cell test only that the
   status is PINNED. All four lie in B_(L+1)(q10), so these anchors do not test the local source list
   (mutant `K5_E_moved` survives). The outcome is unaffected, because only N coincides with a key.
   *Fix:* compare the full (status, reason) tuple, as is already done for `q10_ready_interior`.
4. **(Nit, inventory provenance.)** The ready-ball list is retyped, not tied to
   `native_route_v13/checks.py`. No control can detect a missing region, and the verdict-change
   mutants show one would flip the outcome. I compared the lists by hand and found none missing.
   *Fix:* pin `native_route_v13/checks.py` by hash and assert that the retyped list equals the one
   parsed from its `geometry()` lines. Also record the margin-2 position of the −x and +y keys
   relative to the q9 L-ball and the q10 (L+1)-ball.
5. **(Nit, countercontrol strength.)** Strengthen K3's countercontrol to "at least one SHA-256 world
   for every n". It passes. Also say in PROVENANCE that the relaxed rule would pass with the
   polynomial family alone.
6. **(Nit, wording vs plan.)** K3 compares the scalar and bit-parallel evaluators on 3 of 8 key values
   (432 = 144×3). The plan says the two "must agree". *Fix:* compare all 8 lanes, which is cheap.
7. **(Nit.)** K2 brute-forces the lemma against the cone formula, not the dynamics. *Fix:* compute the
   cones by propagating dependency sets through the rule. My version confirms the formula for n ≤ 6.
8. **(Nit, cheap closure.)** "Previous-slice key cells (not classified)" can be closed in a few lines.
   My classification: the q9+(L+1)e cells in the previous slice are free for −x, +y and −y
   (ready margin 1); +x and −z are pinned; +z is inside the q10 cone. The outcome is unchanged.
9. **(Cosmetic.)**
   - In verdict (i), "nonconstant" is redundant: constant readouts also fail.
   - The verdict lists "q10 at L+1" among the "permitted records", but q10 is private.
   - The recipe's `<commit>` placeholder should be filled in once the commit is published.
