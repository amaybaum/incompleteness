# Changes r13 → r14

r14 clears the Weinberg 1989 landing gate (owner, 2026-10-26). The owner supplied a third-party hosted copy; the
Introduction's final scientific referee read it first-hand and checked the title, publication details, completeness
and the relevant passages (`review/references/WEI89.md`). The verdict is SUPPORTED in substance by §I and §III, with
two qualifications, both handled in the wording below. The copy is not committed.

r14 is generated from r13 by `draft/scripts/build_r14.py`: two exact, uniquely matching replacements. Every other
sentence is byte-identical to r13.

| # | Change | Old | New |
|---|---|---|---|
| G1 | The VERIFY marker before §4's first sentence is removed, and the sentence is cited to what Weinberg states. "Observational value" covers Weinberg's 1989 upper bound and the present measurement, which are of the same order. The cutoff-convention clause is the paper's own and stays uncited. | "…some 120 orders of magnitude above the observed one (the mismatch), the exact power depending on the cutoff convention; if that density sources curvature, it must be cancelled to that accuracy." | "…some 120 orders of magnitude above the observational value [Wei89, §I; §III, Eqs. (3.4)–(3.6)] (the mismatch), the exact power depending on the cutoff convention; if that density sources curvature, it must be cancelled to that accuracy [Wei89, §III]." |
| G2 | Bibliography entry, after [Vol06], with a first-hand provenance comment in the [Vol06] style. | — | "[Wei89] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989)." |

## Build and checks

Built as `papers/Introduction.md` on a fresh `git archive b64919cd` with `sh ./build.sh Introduction`:
- 17 pp; build OK, with no dropped glyphs. "Code, data and formal verification" starts on p. 13, so the main text
  stays within 12 pp.
- `voice_check`, `claims_check` and `duplicate_check` are OK.
- No Lean identifier changes. One citation key and one bibliography entry are added. 0 OWNER and 3 VERIFY markers
  (CT06, Har04, Sha79; none gates landing).
