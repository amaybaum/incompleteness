# Introduction draft r11: changes from r10

## Inputs

- **Base:** r10 (`74330267`), sha256 `b87ef6f9…9830`. r10 is unchanged.
- **Re-check of r10:** `review/scientific/RECHECK-r10.md`, ACCEPT WITH NITS.
- **Retained Lean evidence:** `papers/introduction_repro/` at `ed3ca911` (`README.md` and
  `results-121598983127.json`).
- **Method.** `draft/scripts/build_r11.py` applies 9 edits, each an exact, uniquely matching replacement. Every
  sentence it does not touch is byte-identical to r10. r11 adds no sections, applications or claims.

## Changes

| # | Where | r10 | r11 | Reason |
|---|---|---|---|---|
| 1 | §2.2, Realization | "[Main §3.4; EGGH26, Prop. 13]" | "[Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]" | **T3 reverted** (RECHECK-r10 finding 1). It saves no space, and [Main §3.4] holds about a dozen results |
| 2 | §4, Weinberg VERIFY marker | "it is cited for that sentence only once the source is read and checked." | "it is cited for that sentence only after the source is read and checked." | Unambiguous wording (RECHECK-r10 finding 3) |
| 2a | §4, Weinberg VERIFY marker, opening | "<!-- VERIFY: Weinberg 1989 (Rev. Mod. Phys. 61, 1) is not read first-hand …" | "<!-- VERIFY: Landing gate (owner, 2026-10-26): the paper does not land until this source is read first-hand and checked. Weinberg 1989 (Rev. Mod. Phys. 61, 1) is not read first-hand …" | **Owner decision of 2026-10-26: "Keep as landing gate".** The marker states that it gates landing, and still states that the source is not read first-hand and not verified. **Weinberg 1989 is an open landing gate** |
| 3 | §1.2, Conventions | "at commit `687e885b`" | "at commit `17b830bc`" | The retained evidence holds at main `17b830bc`. Its Lean trees (`verification/lean`, `verification/lean-mathlib`) are identical to `687e885b` |
| 4 | §1.2, after Conventions | OWNER marker "decision 2 / retention §A.42" | *(removed)* | The evidence it asked for is retained at `papers/introduction_repro/` |
| 5 | Code, data and formal verification | OWNER marker "retention §A.42", with the "[expected-result file path]" placeholder | *(removed)* | As for 4 |
| 6 | Code, data and formal verification | "The declarations in Appendix A were checked in Lean 4/Mathlib at commit 687e885b1cfd24d6f17eee439101afc8acf07015 by the recipe `python3 tools/lean_axiom_check.py --require-lake`, which builds the Lean project and requires every `#print axioms` report to lie within `propext`, `Classical.choice` and `Quot.sound`; the expected result is in [expected-result file path]." | "The declarations in Appendix A were checked in Lean 4.33.0 with Mathlib v4.33.0 at commit 17b830bcd0ecc36e10eff5b9eeca03bdd7198d86, by building the Lean project in `verification/lean-mathlib` (`lake exe cache get`, `lake --rehash build`) and running `python3 tools/release_gate.py`, whose `lean-axioms` step requires every `#print axioms` report to lie within `propext`, `Classical.choice` and `Quot.sound`. Each declaration in Appendix A reports exactly these three; the expected result and the comparison recipe are in `papers/introduction_repro/`." | States what the retained evidence shows (detail in the next paragraph). The project path comes before the command list, which avoids a 0.5 pt overfull line |
| 7 | Appendix A, lead line | "line numbers at commit `687e885b`" | "line numbers at commit `17b830bc`" | One commit throughout. The Lean trees are identical at the two commits, so every line number is unchanged; identcheck confirms all 28 at `17b830bc` |
| 8 | References, Corpus line | "(repository commit `687e885b`," | "(repository commit `17b830bc`," | One commit throughout. The r8 black-hole section cites #936's GR and book text, which exists only from `17b830bc`. Every corpus pointer was checked at `17b830bc` first (next section) |

**Change 6, checked against `papers/introduction_repro/README.md`:**
- **Commit:** `17b830bcd0ecc36e10eff5b9eeca03bdd7198d86`.
- **Toolchain:** `leanprover/lean4:v4.33.0`. Mathlib is required at `rev = "v4.33.0"`.
- **Build step:** `lake exe cache get` and `lake --rehash build`, in `verification/lean-mathlib`.
- **Gate:** `python3 tools/release_gate.py`. Its `lean-axioms` step runs `lean_axiom_check.py --require-lake`, which
  fails on any axiom outside `propext`, `Classical.choice` and `Quot.sound`.
- **Reports:** all 28 Appendix A declarations report exactly `[propext, Classical.choice, Quot.sound]`.
- **Comparison recipe:** the README's "Reproducing it".

## T4 is kept, and this is its record

- **What T4 undid.** T4 (r10) removed "Theorem (operational-completion characterization)" from inside Theorem 4's
  citation. That undoes the r2 editorial fix (`review/editorial/REVIEW.md:173`, applied in r2 as F10), which had
  added the explicit "Theorem (…)" pointer.
- **Why the theorem stays findable.**
  - The label's name, "operational-completion characterization", stands immediately before "[GR §3.3]".
  - It matches GR's own heading verbatim: GR:216, "**The operational-completion characterization.**", and
    GR:218, "**Theorem (operational-completion characterization).**".
- **Page budget.** T4 is needed: without it, four lines of §6.4 spill onto p. 13 (RECHECK-r10 §2).
- **§A.34 is unaffected.** Each direction keeps its own named witness:
  - ⇒ `physical_of_exactAll`;
  - ⇐ `exactAll_of_physical_general`.

## Corpus pointers at `17b830bc`

Every [GR …], [Main …], [Book …] and [BHa]/[BHb] pointer in r11 was checked at `17b830bc` before the Corpus commit
was changed. **None moved.**
- **Unchanged files** (`git diff --stat 687e885b 17b830bc` is empty for each): `papers/Main.md`, book ch01 (§1.11),
  `verification/programmes/black-hole-information/` (the [BHa]/[BHb] items C1, C6(a)–(d) and F), the Lean trees
  and `papers/oi_lattice_code/foundations/`. Every [Main §…] pointer, with its Theorem, Remark and Proposition
  names, and [Book §1.11] and the [BHa]/[BHb] items therefore resolve exactly as at `687e885b`.
- **`papers/GR.md` changed only in the #936 hunks:** the summary lines 605 and 611, the App. A introduction (717) and
  App. A.6–A.7 (805–879). The other cited sections are untouched:
  - §2.2, with (C4) at GR:52;
  - §3.3, with Theorem (operational-completion characterization) at GR:218;
  - §6.2, from GR:342, with the two completions at GR:356;
  - App. A.1 (GR:719, $\mathcal C_V\times\mathcal C_B\times\mathcal C_D$).
- **Already checked against `17b830bc` in r8:**
  - App. A.6 (the generalized second law is open);
  - App. A.7 (H-decouple, Thms A.7–A.9, "Proper energy shells", the single-trajectory paragraph);
  - Book §7.6 (ch07:110) and §18.5 (ch18:146).
- **No `687e885b` remains in r11.**

## Markers

0 OWNER and 4 VERIFY (CT06, Har04, Sha79, Weinberg). The Weinberg marker is an **open landing gate** (owner,
2026-10-26). The other three record sources that cannot be reached from this environment.

## Build and checks

- **Build:** 17 pp; 0 overfull boxes; 0 missing glyphs; median 2,666 characters per page.
- **Main text:** abstract to §6.4 ends at **p. 12, line 40**, which is **11.82 pp** by the editorial measure. "Code,
  data and formal verification" starts at the top of p. 13, so the main text is unchanged from r10.
- **Repository checks** on a fresh `git archive 17b830bc`, with r11 as `papers/Introduction.md`: `voice_check` (41
  files), `claims_check` and `duplicate_check` are OK.
- **Identifiers at `17b830bc`:** `identcheck.py` runs on a fresh archive of `17b830bc`, the commit Appendix A now names. It finds 28 identifiers, 0 unresolved and 0 line mismatches.
- **Against `papers/introduction_repro/README.md`:** all 28 declarations match by name, module and declaration line.
  `scripts5/repro_names.py` (scratch) matches 27 automatically. The 28th,
  `finiteIsometryExtensionSF_discharged` at IsometryExtension:116, sits inside a parenthesis the parser does not
  read and was checked by hand. No Appendix A name is missing from the README.
- **§A.32/§A.33 scan of the 6 added lines:** 0 phrase hits. The only all-caps words are VERIFY and FINDINGS,
  inside the VERIFY comment.

## Basis of the Code-section edits

- **The rewrite of the Code-section sentence and the removal of the two §A.42 markers** carry out the owner's
  instruction of 2026-10-26: "Lean axiom evidence: Retain the exact command, output, source SHA, and toolchain
  version on main." The markers asked for that evidence, and it is in `papers/introduction_repro/`. Holding the Code
  section unchanged in r10 was a coordinator instruction, pending that package; it was not an owner decision.
- **The "decision 2" marker** asked the owner to choose between "machine-checked" and "checked in Lean 4/Mathlib at
  commit X by recipe Y". r11 keeps "machine-checked", defined in the Conventions paragraph as checked in Lean
  4/Mathlib at commit `17b830bc` by the stated recipe. It is put to the owner for confirmation.

