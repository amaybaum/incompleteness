# Setting-conditioned later access: result

Research-only execution of `later-access-preregistration.md` as frozen at
`b532472a5979d1f27d14d972c52357bad9f7a463` on draft PR #1009. The
preregistration is unchanged. `native_later_access_probe.py` implements its
decision rule, preconditions, controls and mutant table. Its structured output
is `later-access-result.json`. This note changes no manuscript, status label,
prior, access rule, benchmark or earlier verdict.

## Outcome

The JSON gives:

| Field | Value |
| --- | --- |
| `token` | `LA-EQUAL` |
| `hidden_only` | `false` |
| `informativeness` | `EMPTY` |
| `TV_win(k0)`, `TV_acc(k0)` | `0` for every incoming-packet value and for k0=⊥ |
| `search` | trigger none, \|S\| none, derivation not run, outcome not triggered |

The token is conditional on H-prior, H-inventory, H-access, H-rule and
H-torus. The 22 control checkpoints in the JSON passed before the token was
computed, as CP-GATE records. CP-PIN and CP-REPLAY also pass, and every
precondition P1-P6b holds. The zero TV values are what the written
chronological-triangular proof gives once P1-P6b hold. They are not an
enumeration of the history law, which is astronomical.

`EMPTY` comes from the same proof. For every value of D' and eta, the tail
word over the 8(H*-L-5) frontier triples has conditional mass
8^-(8(H*-L-5)), so Tail is independent of (eta, K0, K1, K2) given D'. The
sourced later read therefore carries no packet or key information at all, and
its equality across the two settings has the same cause as its emptiness.

## Measured preconditions

All minima are exact integers over the window L+6 <= t <= 2L, evaluated at the
endpoints and at every absolute-value breakpoint. They were recomputed
independently of the `history_v11` checker.

| Precondition | Measurement | Holds |
| --- | --- | --- |
| P1 | own paths axial with length t; min over j != i of dist(f_i(t), p_j) - t = 0, attained only by the edges 2->5 and 3->5 | yes |
| P2 | min dist(f_i(t), cell) - time = 1 over 80 record and label entries (port 0 against deltaW2 at L+6) | yes |
| P3 | 0 intersections with 42 eta cells, 1479 sources and 17 exceptions; min ball distance minus radius = 6 (port 7) | yes |
| P4 | equal-time cross-edges exactly {2->5, 3->5} | yes |
| P5 | 2H* < side, and every coordinate span < side/2 | yes |
| P6a | H takes 8 distinct values | yes |
| P6b | 12672 diagonal-permutation checks in 162 dense worlds with setting- and key-dependent backgrounds, including same-tick co-arrival | yes |

No precondition failed, so there is no first failing (cell, tick).

## Controls

| Control | Measured |
| --- | --- |
| CP-PIN, CP-RULE | five input digests equal; h equals the pinned rule on all 8 codes |
| CP-POS | TV_acc 1/8; bounded search returns a witness (\|S\|=1) |
| CP-ACCESS | TV 0 with LA alone, 1/8 with an extra read of the own bank triple |
| CP-PRIOR | TV_win 1/8 with b5 equal to a tail bank triple and fair marginals; 0 for another eta key |
| CP-MARG | joint TV 1/2, per-coordinate marginal TV 0 |
| CP-LEAK | TV 1 with R.B/D retained, 0 without |
| CP-NULL | TV 0 on identical laws; search returns no witness |
| CP-SEARCH-COUNTER | no witness on Y = c XOR d; S with d omitted rejected as incomplete |
| CP-SEARCH | trigger, \|S\|, derivation and outcome recorded for every search |
| CP-SUPPORT | support 4096, 512 after pinning, in two backgrounds |
| CP-HIDDEN | TV_win 1/8, TV_acc 0, hidden_only true |
| CP-INFO | EMPTY fixture EMPTY; INFO-COUNTER INFORMATIVE with TV 0 |
| CP-GEO-COUNTER | cone ray minimum exactly 0 fails P2; eta-cell ray fails P3; q9 ray fails P2 at the q9 and V records |
| CP-BREAKPOINT | breakpoint minimum -2 at t=37; endpoint and grid sampling gives 1 |
| CP-ORDER-COUNTER, CP-PERM-COUNTER | reversed order fails P4; H' fails P6a and P6b |
| CP-READSET | declared reads are the LA set plus pre-cut records; an extra q10 read is flagged |
| CP-STOP, CP-STOP-COUNTER | 25 stop rules on A(X)-prefixes give pushforwards with TV <= 1/8; a rule reading R.A is rejected before evaluation |
| CP-PRECUT | pre-cut factor TV 0 on both fixtures; b5 to K0 slices exceeds tau by 1 |
| CP-BRANCH | 64 contexts, 16 at k0=⊥; masses 63/256 and 193/256 equal the fixture's assigned context masses |
| CP-EXACT, CP-GATE, CP-REPLAY | no float; token computed after the controls; normal and `-O` outputs byte-identical to the JSON |

The mutation suite applies the 14 code mutants of the preregistered table.
Row 4 runs in both variants, `>=` for `>` and record cells skipped, so the
suite makes 15 runs. Each run exits 2 with VOID and names its preregistered
catching checkpoint, in both normal and `-O` mode.

## Scope

`LA-EQUAL` closes only the LA interface: the passive read of the eight public
ports at every tick L+6..2L, in the window through H*=2L, for this setting,
carrier and record dictionary, under the five hypotheses. It does not show that
the outgoing environment G is setting-independent. It is not a no-go for G or
for an active later coupling. It says nothing about horizons beyond 2L, an
exposed private field, a correlated prior, adaptive operations or other
constructions. Because the flag is `EMPTY`, it also does not show that any
informative later read is setting-blind.

The procedure is asymmetric. LA-EQUAL is certified by a proof over the whole
window. LA-DIFFERENT would need a local exact witness whose backward cone
holds at most six triples. At actual scale a tail port's backward cone is
large, so that bound can be met only for a local P1 failure. No outcome
changes an earlier verdict, the 42-bit benchmark, any #866 quotient, a
manuscript claim or a status label.

The probe also makes five implementation choices.

- The P2 record set adds the eight port streams through L+3. P1 already
  implies these, and they make P2 stricter.
- The flag and timing cells are the source-phase cells q0..q9 at R+k, as in
  the parent unit; they match the parent's old-core cells and the ready-ball
  centres. A different cell set could change P2. The measured P2 margin is at
  least 1 over all 80 entries.
- P3 also checks that the beta rays are pairwise disjoint.
- The q9 counter-ray must fail at a record cell, so that a P2 test that skips
  record cells is caught.
- The BRANCH context masses (2i+1)/4096 are bookkeeping masses, not native
  failure probabilities.

The small worlds test the mechanism and the comparator. They do not measure
the astronomical preparation.

## Replay

From the repository root:

    python3 -I -B verification/programmes/substratum/continuous-substates/native_later_access_probe.py
    python3 -I -O -B verification/programmes/substratum/continuous-substates/native_later_access_probe.py | cmp - verification/programmes/substratum/continuous-substates/later-access-result.json
    python3 -I -B verification/programmes/substratum/continuous-substates/native_later_access_probe.py --mutation-suite

Exit 0 with a token, 2 VOID, 3 for a mismatch with, or absence of, the
committed JSON (`--write-expected` writes it on a first execution). The
suite exits 0 only if every mutant is caught in both modes. A run takes about
5 s and the suite about 45 s. The result is exact algebra plus a conditional
paper proof. It is not Lean certification, an operational QM result or a
native instrument.
