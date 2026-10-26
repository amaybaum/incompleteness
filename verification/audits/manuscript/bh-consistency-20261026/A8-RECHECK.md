# Verbatim check of the A.8 review fixes (PR #936, head ca159cc9)

This check covers the single commit `ca159cc9` on top of `2d13792d`. It was done read-only. The tool runs used a
detached worktree at `bhfix/review4/rv`, which was removed afterwards with `git worktree remove`; no gc was run.

**Verdict: ACCEPT.**

## 1. The fixes are applied verbatim

I extracted each replacement block from A8-REVIEW §4 and searched for it as a fixed string at `ca159cc9`. Every
block occurs exactly once where it belongs.

| Fix | Where found |
|---|---|
| A1 (A.8 proof) | GR |
| A2a (proper-shells paragraph, including the black-hole sentence) | GR |
| A2b | ch07 and FULL |
| A3, the ch09:127 cell | ch09 and FULL |
| A3, the README:64 sentence | book/README.md (it has no mirror) |
| Nit: "cycle typicality on the configuration space" | ch18, ch19 and FULL ×2 |
| Nit: the diagonal-shell qualifier | GR |

**Re-grep of the superseded text:**
- "the wave equation is Hamiltonian), so": 0 hits.
- "cycle typicality on the energy shell": 0 hits.
- Every hit of "conditional on … H-scramble and … H-decouple" now carries the full-space scope in the same
  sentence or cell:
  - GR:605;
  - ch07:116;
  - ch09:127 / FULL;
  - README:64, where the scope precedes the condition.

## 2. The owner's three questions: all now YES

1. **Mathematical validity: yes.** This is unchanged from A8-REVIEW. A.8's statement equals what its proof
   supports. The proof's first sentence now derives the bijection of Σ_E from the hypothesis that the energy is
   constant on C_B × C_R, not from the wave equation.
2. **Physical interpretation: yes.** It is now explicit.
   - GR's proof says energy conservation "places no constraint on the orbit".
   - The GR proper-shells paragraph says three things:
     - the hypothesis "requires the energy to be constant on C_B × C_R";
     - it "does not follow from the conservation of a Hamiltonian that takes more than one value there";
     - "an evaporating black hole whose radiation carries away its energy is in that proper-shell case", which is
       stated as open.
   - ch07:126 / FULL says the same in book register.
   - Nothing implies that energy conservation is established for the whole-space case.
3. **Consistency: yes.** No site silently extends A.8 or A.9 to smaller shells.
   - The two quiet extensions (ch09:127 and README:64) are fixed.
   - The ambiguous mechanism names at ch18:148 and ch19:72 now read "configuration space".
   - The remaining "energy shell" mentions are of two kinds. Some are the horizon-temperature results, which are
     unrelated. The others are the conjectured cycles-to-replica-wormholes correspondence (ch07:147, GR:877),
     which asserts no Page value.

## 3. Mirrors, scope and checks

**Mirrors.** All 4 changed chapter lines (ch07, ch09, ch18, ch19) occur exactly once in FULL, and FULL's diff
adds exactly those 4 lines.

**Nothing else changed.** The GR.md diff is exactly the 2 edited lines. Apart from the manuscript files, the commit
touches only:
- the regenerated `.tex`/`.pdf`: 4 GR.tex hunks, with `source-sha256` matching the new GR.md (b8b63d37…) and
  FULL.md (bfe7e4ed…);
- the record directory: A8-REVIEW.md, byte-identical to mine; a README line accurately describing it; and
  CHANGE-NOTE §8.

**LEDGER.** It is unchanged, as expected: A1 and A2a lie outside A.8's statement, and coverage_check passes
without any fingerprint change.

**Checks at `ca159cc9`, all OK:** coverage_check, voice_check, claims_check, duplicate_check,
dependency_label_check --strict, artifact_placement_check, mirror_check (0 absent), and legacy_records_check (303
records intact).
