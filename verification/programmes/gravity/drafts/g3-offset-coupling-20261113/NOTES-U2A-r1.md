# NOTES-U2A-r1: working log for G3 unit 2(a), revision 1

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch.** `research/g3-offset-873-20261113`. The worktree was fast-forward pulled from `origin`. The
  pull reported "Already up to date" at `e81e4fb23f4a5abda910cc69e9f79f93e6ae1523`, and the working tree
  was clean. No file on the branch was edited.
- **Authority.**
  - #873 c.6863416405 (`amaybaum`, 2026-11-13T19:58:10Z): Q4 authorizes unit 2(a), paper-only, no new
    premise, no manuscript change, no Lean build, on #1275's branch. Q7: (ii-L) is not adopted as a
    §A.29 premise for now. Q8: the AW-loop wording gap is carried forward, and no manuscript change is
    authorized.
  - PR #1275 review 5896999577 (posted by `amaybaum`, 2026-11-13T19:41:56Z, on `e81e4fb2`): ACCEPT of
    unit 1 as a conditional, paper-only audit, with the "important limit" this unit tests.
  - The coordinator's instructions are session messages, not owner records.
- **Files written.** `G3-UNIT2A-r1.md` and this file, outside the repository. Nothing was committed,
  pushed or posted.

## 2. Reading log

Read at `c3b5f37a` unless stated otherwise.

| Source | What was used |
|---|---|
| GR:40 | the partition is the cosmological (event) horizon |
| GR:42 | ħ independent of the observer and of the horizon area; "Different observers have different horizon areas" |
| GR:58, GR:78 | H-count; the gap equation `ħ = τ_K/β_E`; "κ cancels" |
| GR:154 | "The non-circularity is structural" for the gap equation |
| GR:162, :334, :356 | Λ undetermined; its value an input |
| GR:332, :336 | `½ħω` per mode to the cutoff; `ρ_QFT` |
| GR:340–352 | §6.2: the geometry-first source; requirements (i)–(iii); laboratory scope; GR:352's two completions |
| GR:358, :374 | feedback "through state-level quantities"; "the emergent vacuum energy is a state-level quantity" |
| GR:362 | "the mode sum `k⁴/(16π²)` cut off at `1/ε`" |
| GR:364 | `N_modes = S_dS/σ` |
| GR:378 | `A = 4πc²/H²` |
| GR:388 | "The self-consistent emergent-QFT calculation" |
| GR:400 | Readings 1 and 2 |
| GR:569–581 | §8.3: relative and absolute levels; GR:579's open coupling of transition energies |
| book/ch07-gravity.md:181–187 | the book mirror of (i)–(iii); "not a stipulation but a structural consequence" |
| book/appendix-c-objections.md:250–259 | the gap equation "is therefore non-circular" |
| G3-UNIT1-r5.md, NOTES-r5.md, CONFIRM-r3.md, CONFIRM-r4.md | at `e81e4fb2` |

**Corpus search (§A.19).** `git grep` at `c3b5f37a` over `papers/`, `book/` and `verification/` (Lean
trees excluded) for "entry point", "non-circular", "self-consistent loop/fixed/solution/de Sitter" and
"fixed point"/"fixed-point". The relevant hits are GR:346 and its book mirrors (ch07:183, FULL:2049),
the gap-equation non-circularity statements (GR:154, appendix-b:216, appendix-c:259), and GR:388. No
corpus text states (ii-L) as a premise, or argues that a fixed point of the loop is excluded. The other
hits concern unrelated fixed points (RG, Lawvere, dyadic arithmetic).

## 3. Order of work

1. Read the authorization, the review, unit 1 r5, NOTES-r5, CONFIRM-r3, CONFIRM-r4 and GR §6.2, §7.1 and
   §8.3.
2. Wrote the decision rule, the admissible premise set and the controls (§1 of the record) before
   writing §2–§6. The sources had been read and the question scoped first, so the rule was not drafted
   blind to the likely direction. What was preregistered is the rule and the controls, not an outcome.
3. Formalized GR:346 (§2), built the model (§3), applied the argument (§4), ran the controls, then wrote
   the verdict from the rule.
4. Pressure-tested both branches (§5), then wrote the consequences (§6).

## 4. Decisions

1. **The premise set excludes conclusions and posits.** GR:342's "forced" and "not the reverse", and
   ch07:187, state the conclusion of (i)–(iii). GR:340 (P11) and GR:575 are posits of the geometry-first
   proposal. Using any of them would import the exclusion.
2. **Two orders.** "Order of explanation" is defined through specifications, explicit or implicit.
   "Order of determination" is defined through value dependence on a stated family. The implicit case
   separates the maps used in a condition from the element the condition selects.
3. **Witness conventions.** Z_I uses GR:362's mode sum with an IR limit read from `N_modes`. Z_II is unit
   1's literal `ρ_x = ħ e_x/v` with the total ground value. Z_0, GR:362 as written, is kept as the
   degenerate case and is not a witness (control C3).
4. **Positive weight.** The witness takes `n > 0`, following GR:332's `½ħω` per mode. A negative weight
   is recorded as a remark (non-uniqueness) and is not used.
5. **Scope.** Exact de Sitter only, under assumption M1 (`n`, `ε` independent of `R`). Observer-relativity
   and the teleology of the event horizon are recorded as AW-obs and AW-tel, not tested.
6. **Classification.** U2A-F2 is marked NEW as a candidate pending independent review, because it
   corrects a scope statement of unit 1 (B5) that the reviews of unit 1 did not raise. The others are
   ELABORATING.
7. **No magnitude claim.** The calibrated-constant identity of §3.4 is stated as an identity of the model,
   with no numerical value and no comparison with an observed value.

## 5. Checks

- No computation, script or build was run apart from the three permitted checks below.
- Algebra rechecked by hand: `G_μν = −3R⁻²g_μν` on de Sitter; `F_0 = 3/(q²ε²)` under both Z_I and Z_II;
  the Z_I quadratic and its positive root; the sign of `F′` under both conventions; the Z_II quintic and
  its Descartes count; the iteration slope `−2bx*/3`; `K = 2nGħ/(3v)`.
- A barred-string scan of both files (the repository paths and the scratch-directory word that the brief
  bars): no hit.
- The repository checks were run on the unchanged worktree at `e81e4fb2`. They do not scan drafts or
  files outside the repository. Results are in §7.

## 6. Owner questions

QU1 to QU5 are in §9 of the record: review routing; Q7 (whether (ii-L) stays open as a §A.29 candidate);
Q8 (scoping GR:346, GR:342 and ch07:183–187 to the order of explanation); whether unit 1 is revised or
corrected forward by this record; and the next unit.

## 7. Repository checks

| Check | Result |
|---|---|
| `tools/claims_check.py` | exit 0: "OK (no withdrawn result asserted unconditionally)" |
| `tools/staleness_check.py` | exit 0: "OK (13 matched, 0 unstamped)" |
| `tools/voice_check.py` | exit 0: "OK (no manuscript-voice history narration; 40 manuscript file(s) scanned)" |

The worktree stayed clean at `e81e4fb2` (`git status --short` empty).

## 8. Limits

- The derivations are by hand and are not machine-checked.
- The model is exact de Sitter only, under M1.
- The premise transcription of GR:346 is [P].
- The literature is recalled, and no verdict rests on it.
- The §A.31 fixed point is not reached.
