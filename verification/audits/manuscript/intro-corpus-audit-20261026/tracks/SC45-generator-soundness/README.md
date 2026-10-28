# SC-45 — exact fixed-interface relabelling counterexample

**Status:** DRAFT research finding, not an independently accepted or manuscript-propagated correction. Owner issue #979; draft PR #981.

## Reproducer

Run from repository root:

```bash
python3 -I verification/audits/manuscript/intro-corpus-audit-20261026/tracks/SC45-generator-soundness/verify_four_state.py
```

A separate private Python cross-check using the exact same four-state rule and rational arithmetic returned:

```
T(phi)       = [[1/2, 1/2], [1/2, 1/2]]
T(pi phi pi^-1) = [[1, 0], [0, 1]]
transferred observation interface: equal at t=0,1,2,3,4,5
one-step 24-transposition census: 16 preserving, 8 violating
```

The checked-in script asserts these counterexample and positive-control properties, with no floating point. `pi` swaps (0,0) and (1,0), while `phi(v,h)=(h,v)`; each input visible state uses an independently uniform hidden bit. The transformed dynamics are conjugate as full-state permutations but yield different one-step visible transition matrices **under the original, fixed partition and readout**.

A relabelling of *both* the dynamics and observer interface leaves the observations unchanged. That is an **isomorphism of presentations**, not the blanket assertion that arbitrary full-state relabelling preserves fixed-interface transition matrices.

## Theorem 24 implications

- Theorem 24(i) and its scope proof mix arbitrary full-state graph relabelling with the narrower requirement to preserve the visible transition law, emergent Hamiltonian and action scale. It cannot claim all `|S|!` relabellings are transformations of that fixed-interface observable structure.
- Theorem 24's introductory equivalence quantifies over all partitions in one structural class. A precise interpretation must specify how partitions are identified or transported. This counterexample by itself does not classify the all-partitions equivalence relation or show that the four families are incomplete.
- Generator (iv)'s quasi-isometry and statistical-isotropy claims are separate from equality of the complete time-resolved channel family. Check them explicitly before calling the exhibited family sound at the full-observable level.
- State the corrected definition **before** reclassifying which transformations count as gauge; preserve independently proved fixed-basis/hidden-only relabelling facts.

## Verification provenance and open gates

SC-45 initial PR head `681eefcaf59b700f1ec18d6102a3a4c4fef807ad` obtained all expected GitHub verification jobs green (run `40641002475`, including Lean and release gate). This does **not** certify the SC-45 custom script, because the existing workflow does not invoke it. The local exact arithmetic was checked separately, but an independent reader must run the checked-in script, inspect its argument and positive controls, and check the full theorem scope.

No corrections to Theorem 24 have been made in this unit yet. No merge is authorized. Its overlap with SC-44 #980 is a content dependency requiring reconciliation, not an instruction to combine the drafts prematurely.
