# PE-01 amendment A3: literature tags extended to relevant prior work

The verdict-bearing run (40271434371, head `54964146`) is complete, and its results are retained in `../results/`.
This amendment extends the literature that productivity tags (`../PLAN.md` §6 item 5) may cite. It is made after
the results exist, so it is restricted to the tags.

- **Decided by:** the owner (amaybaum), 2026-10-26: "Literature extension: Extend tagging to relevant prior work,
  without changing PE-01's frozen verdict."

## What does not change

- The verdict (`../results/verdict.txt`, `verdict.json`), the measurements, conditions (a)–(f), the window, the
  thresholds, the controls, the classification and the stopping rules, as reviewed and as amended by A1 and A2.
- The governing classification (condition (d) read as `abs`, COUNTEREXAMPLE) and the sensitivity classification
  (`signed`, COUNTEREXAMPLE), each reported separately.
- The mechanical tags of A2 item 4 (L1–L4, `../pe01/pending.py`), which stay as computed. Tags bear on no verdict
  (§6 item 5).
- No code is re-run and no output in `../results/` is regenerated or edited.

## What is extended

§6 item 5 admits, besides the closed forms, only results listed in §9 under "before any candidate-NEW tag". That list
treats passive observers (oblivious read-once branching programs and small-bias inputs). The extension adds prior work
on generators whose clocking depends on their own output or on an external input, and on prediction or reconstruction
of such generators:

- R. A. Rueppel, "When shift registers clock themselves", EUROCRYPT '87, LNCS 304 (self-decimated sequences);
- D. Gollmann, W. G. Chambers, "Clock-controlled shift registers: a review", IEEE JSAC 7(4):525–533 (1989), already
  cited in §9 as design rationale;
- any further peer-reviewed or archived prior result found while reading these, under the rule below.

## The tagging rule, fixed before any of this literature is read

1. **Scope.** The extended tags are assigned to two results only: the COUNTEREXAMPLE cell (`G_clk`, n = 5,
   `emb_m2_all`, K = 7) and the passive horizons listed as PROVED (exhaustive finite) in `../results/verdict.txt`.
2. **COVERED-literature (extended).** A result is tagged COVERED-literature only when a cited work, read first-hand in
   full or in its relevant section, states or directly implies it: the same kind of generator (or a class containing
   it) and the same kind of observer (for the counterexample, one whose inputs affect the generator's clocking or
   state; for passive horizons, an observer that only reads). The tag quotes the passage, gives its page or section,
   and says which of the result's parameters it covers. Coverage of the phenomenon in kind without the parameters is
   recorded as such ("covered in kind"), not as COVERED-literature.
3. **Not verified.** A work read only through an abstract, a survey or a citing paper supports no tag. It is listed as
   unread with the reason.
4. **candidate-NEW.** Not assigned unless every listed work has been read first-hand and none covers the result, and
   then only as a candidate until independent review. If any listed work is unread, the result stays untagged with
   "candidate-NEW not assignable: <works> unread".
5. **Independent review.** The tag annex is reviewed independently before it is relied on anywhere.

The tag annex goes in `../review/literature/` beside this amendment's record.
