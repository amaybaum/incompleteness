# A1-EXIT final regression audit (#1468): report

**Status.** Writer's paper-only record, WIP / UNVERIFIED: no independent review yet. It follows `PLAN.md` (`0fa90db1`), committed before this report. No manuscript, Lean module, registry, ledger or plan file is edited.

**Authorization.** Owner `amaybaum`, #1169 comment 7214186738, 2026-11-27T09:01:16Z: "Authorize the #1468 regression audit with a designated writer. Reuse existing accepted evidence and limit the audit to its necessary scope."

**Goal link (§A.47).** A1 retirement (#1477, #1169), through #1468: decides whether the integrated A1-exit changes weaken, strengthen or alter any physical prediction or empirical comparison without explicit justification (owner requirement 6, #1169 comment 7048255658).

**Verdict.** No physical prediction or empirical comparison is weakened, strengthened or altered by the integrated A1-exit changes. Every number token or status label that changes in a prediction, empirical or status row has a cited justification. No changed-without-justification item was found (§3). The verdict holds for the edit list at `4c79be64` applied at H = `53c6601a`. At current `main` `d7794dc9` it holds for the 291 edits that apply; the remaining 10 must be re-checked in their re-cut form at the final H (§8).

## 1. Inputs

| Input | Identity |
|---|---|
| Before-baseline (accepted, #1471) | `../a1exit-regression-20261121/`, pin `1c7eedc402eafd2bac654484fa790874a33f444d`; `baseline.py check` PASS at this branch's base (sha256 `2db7832d…88c8`) |
| Layer S (Step 2, landed) | `1c7eedc4..53c6601a10419b6b333cc992474272501ab542af` on `papers/*.md`, `book/*.md`: the merges #1470 (S2-A), #1473 (S2-B), #1474 (S2-C), #1472 (S2-D), #1475 (S2-E) and #1494, and no other manuscript commit |
| Layer R (retirement, planned) | `a1exit-deletion-20261121/edits.json` at PR #1477 head `4c79be642ca631573f06b444903be75ec4f5e2b6`, blob `ec384fdfbc12937b860e2f226355e8c5d94820a5`: 401 edits, of which 301 are manuscript edits; applied by the plan's `edits_check.py` (blob `1153e039`) rule |
| Current `main` | `d7794dc9e43a0c66328747354787a707ed2dae88` |
| A1-EXIT ledger | `../a1exit-ledger-20261120/LEDGER.md`, rows X-11, X-47, X-48, X-71 and §6.1 |

`main` moved after H by 21 commits touching `papers/` or `book/` (16 `.md` files): #979, #924, #1558/#1560 and #1588. None is an A1-exit change, so they are outside the audit. Their per-file number tokens: none lost.

## 2. Recipe and results (§A.42 item 1)

From a clone holding the commits of §1, with the plan directory at `PLAN_DIR` (on `main` once #1477's record lands: `verification/audits/foundations/a1exit-deletion-20261121`):

```
B=verification/audits/foundations/a1exit-regression-20261121/baseline.py
D=verification/audits/foundations/a1exit-regression-20261127/delta.py
python3 -I -B $B --compare 53c6601a10419b6b333cc992474272501ab542af --json s.json        # Layer S
python3 -I -B $D --rev 53c6601a10419b6b333cc992474272501ab542af --plan-dir $PLAN_DIR --tree-out T   # Layer R
python3 -I -B $B --compare-tree T --json i.json                                           # integrated
python3 -I -B $D --rev d7794dc9e43a0c66328747354787a707ed2dae88 --plan-dir $PLAN_DIR       # Layer R at main
```

Expected (Python 3; deterministic):
- **Layer S:** `summary: {"deleted": 19, "deleted_flagged": 15, "label changed": 93, "moved": 90, "relocated": 0, "relocated_from_main": 0, "removed": 4, "text changed": 12, "unaccounted": 25, "unaccounted_flagged": 25, "unchanged": 2984, "value changed+label changed": 12}`.
- **Layer R at H:** `301 manuscript edits, 301 applied, 0 not applicable`; tokens lost: `Substratum.md {'4': 1}`, `glossary.md {'10^122': 1}`, `FULL.md {'10^122': 1}`, `tokens lost in total: 3`; ten `edit` lines (D022, D026, D068, D120, D121, D232, D235, D236, D363, D364); `edits touching a prediction or status table row: 0`.
- **Integrated:** `summary: {"deleted": 34, "deleted_flagged": 30, "label changed": 244, "moved": 1043, "relocated": 0, "relocated_from_main": 0, "removed": 16, "text changed": 52, "unaccounted": 55, "unaccounted_flagged": 53, "unchanged": 2777, "value changed+label changed": 16}`.
- **Layer R at `main`:** as at H, except `291 applied, 10 not applicable: D184 D185 D255 D256 D366 D369 D375 D376 D385 D386`.

The compare reports are working files and are not committed (as `../a1exit-regression-20261121/RESULT.md` §2 provides).

**Reading of the integrated report.**
- **Tables.** Of 709 table rows, 3 change: M:742 (status), Str:320 and Str:1224 (class "other"). No row of a prediction-class table changes, including appendix-a A.4–A.5, SM §7.6, GR §7.4 and the book status tables.
- **Number tokens.** Over every changed or removed entry and every deleted line, the net loss is the 3 tokens of Layer R. Layer S loses none. The gains are lattice dimensions and indices (ℤ³, `2\mathbb Z^d`, `\ell^2`, A2).
- **Removed entries.** Of the 16 removed entries, Sub:92 is the only comparison line (C-PROSE). The other 15 are the A1 entries, their motivation paragraphs (appC §C.6, ch02 §2.4, glossary) and three Step-2 rewrites paired below threshold (M:459, Sub:262, ch18:242 with FULL mirror).

## 3. Findings

### 3.1 Prediction and empirical rows

| Item | Layer | Change | Class | Justification |
|---|---|---|---|---|
| All prediction-table rows (appA, SM §7.6, GR §7.4, ch06–ch09, ch19, companions) | S, R | none | unchanged | — |
| M:742, CP-indivisibility row of Main §4.5 (status table) | S | "framework's diagonal-preserving (permutation-dilation) channels" → "hidden-prior (diagonal-preserving) channel family on finite or measurable hidden carriers, given P-indivisible populations" | changed, justified | R6 T6/T7, applied by S2-B (#1473); R6 accepted (owner, #1169 c.7049542030). A theorem's carrier class with its added hypothesis, not a prediction |
| Str:1224, OI row of Structure §14.10 | S | adds "on a finite representative" | changed, justified | S2-C (#1474), ledger X-46 finite scope |
| Str:320, Structure §6.7 tally | R | "A1 (finiteness)" → "Finiteness" | changed, justified | D068, ledger X-46 |
| Prose comparison lines (C-PROSE, 1674 entries) | S, R | label changes only (scope words); no number, unit or uncertainty changes except the lattice notation above | changed, justified | each edit's `row`/`reason` (Layer R); the S2 PR's ledger row (Layer S) |
| Theorem conditions in "value changed" entries: SM:543 (Theorem 13 gains a hypothesis: nonzero diagonal entries for a site-diagonal hidden block, or bounded invertibility of the hidden block on $\ell^2$) and Sub:266 (the proof of Theorem 24(iii) extended to classical factors) | S | a theorem's condition or proof | changed, justified | S2-A amendment 4 (SM:543); S2-B / R6 (Sub:266). Not predictions; every SM §7.6 row is unchanged. The other "value changed" entries are the lattice notation (ℤ³, $2\mathbb Z^3$, $\mathbb Z^3/P$) |
| E3 bound $e^{A/4}$ (Sub:92, deleted with the (A1) entry) | R | removed there | changed, justified | D232 (X-02); the bound survives at Sub:268 (i), "$\le e^{S_\partial}$, with $S_\partial=A/4$" |
| $S_{\rm dS}\sim10^{122}$ (gloss:11, FULL:6502) | R | removed with the A1 glossary entry | changed, justified | D235/D236 (X-01). A motivation of A1, not a prediction; $N_H\sim10^{122}$ survives at ch07 C3 and FULL:1895, the discrepancy at FULL:314, :2058 |
| Theorem 23 hypotheses (D022, D120, D121; Sub:216 bullet D026) | R | "A1–A6" → finite substratum with A4's finite periodic case under Stage 2's wrapping conditions, A2–A6 | changed, justified | X-45, X-42; plan §31 (#1477 c.7074137435; owner #1169 c.7074687817). A theorem's scope, not a prediction |
| Theorem 24(iii) (D363, D364) | R | the factor family narrowed to bijective factors of any cardinality; the channel identity kept for the wider class | changed, justified | X-53; #1477 c.7061693815; owner #1169 c.7062144714 |
| Observer selection, global phase (X-63: M:748, M:764, Sub:56, :401, :407, :542, Str:718, :734, ch02:192, ch04:178, FULL mirrors) | S (+ D244) | "non-equilibrium phase of $(S,\varphi)$" → "regions whose effective channel mixes fast"; Sub:407 "is the premise" → "Whether … is open" | changed, justified | S2-D (#1472), ledger X-63. No number or comparison changes; the Boltzmann-brain exclusion is an explanatory claim and has no empirical row |
| Calibration chain (X-70–X-72: GR:58, GR:88, ch07:42, FULL:1907, Sub:157) | R (+ S at Sub:157) | "Under A1" → "For a finite total system"; "(A1)" dropped from H-count, which already states "the total system is finite" | changed, justified (renaming of a carried condition) | D040–D042, D164, D165 (X-70, X-72). The condition is the one A1 named, so the scope is unchanged; GR §7.4 "Each formula uses the conditions of its derivation" |

**Unjustified changes: none.**

### 3.2 Why the renamings change no prediction

At the pin, A1 was already "an open hypothesis, not adopted, and one sufficient condition among those each result names" (Main ledger item (ii); M:36, M:60, M:732). Layer R deletes the name and the ledger item, and writes at each use the condition A1 named: "for a finite substratum", "for a finite total system", "on a finite representative". The hypotheses that each result consumes are therefore unchanged, except where an edit's recorded reason changes them (Theorems 23 and 24(iii), above). Those are theorem scopes, not predictions. The per-file token comparison (§2) mechanically confirms that no number moved, beyond the three tokens accounted for above.

## 4. Classical-dimension family (X-48)

**Sites.** M:362, :568, :570, :572, :592, :610, :654, :784; Sub:533; ch04:146 = FULL:1250; Intro:135 (lines at `main`). Neither layer edits any of these lines. The C-CDO entries are all `unchanged` in the integrated report.

**The theorem.** The Proposition (M:568) concerns one realization with $N<\infty$ ontic configurations: no such realization reproduces the exact prepare-and-measure theory of a qubit (factorization half proved; the unboundedness of the nonnegative rank imported from [55]). It holds for every finite carrier, independently of A1.

**With A1.** OI's substratum was a fixed finite carrier. The obstruction then applied to the substratum itself: OI could not have a literal continuum-QM endpoint, and the exact continuum theory was an idealization.

**Without A1.** The obstruction applies to a substratum only if that substratum is finite (carrier-size dependence). On an infinite carrier it does not apply. Whether the exact continuum operational theory is realized is then open. It is neither excluded by this theorem nor established.

**The sites at `main`.**
- Every framework-reading site scopes the obstruction to a fixed finite carrier or realization:
  - M:362: "beyond any fixed finite carrier";
  - M:572: "What no fixed finite carrier can do";
  - M:592: "no fixed finite realization";
  - M:610: "at any fixed stage";
  - Sub:533 and ch04:146: "at any fixed finite carrier";
  - M:784: "A single fixed finite carrier".
- Intro:135–137 is conditional on "A fixed finite world" and states that the broader construction is left open.
- The ledger's X-48 correction ("state 'for a fixed finite carrier' … do not convert the obstruction into a claim about an unspecified-size substratum") is therefore met by the existing text, and the audit requires no edit. For the two ledger-named sites: M:362 (M:358 at the pin) scopes the obstruction to "beyond one fixed finite carrier", which is what the theorem establishes; its "closure/limit" wording is accurate only if a realization on an infinite carrier counts as the closure of its finite regions (see the observation below). M:784 (M:780 at the pin) describes the finite-resolution description, and its "does not require an ontically infinite carrier" is cardinality-neutral.

**Observation (not a finding).** Two unchanged clauses read most naturally with finite stages in view:
- M:362, "into a compatible closure/limit". On an infinite carrier an exact endpoint need not be a limit.
- M:784, "the continuum is the mathematical idealization of its finite-resolution physical description".

Neither states a prediction or comparison. Neither uses the obstruction to describe a substratum of unspecified size. M:784's "does not require an ontically infinite carrier" is cardinality-neutral. They are recorded here because their reading shifts once A1 is gone. Under the standing policy, the audit adds no requirement for them.

## 5. Finite-lattice numerics (X-47)

**Ledger reading.** Except SM:645 = ch06:62, these lattices regulate the emergent gauge theory (Haar and staggered HMC, SM:813). They are not A4's substratum lattice. The owner's rule applies by analogy: a numerical L → ∞ value is numerical evidence, not a convergence result.

**What changed.** Neither layer changes any value or comparison at an X-47 site. The C-FINL entries that change carry scope words only: FULL:4901/ch18:170, FULL:4975/ch18:244, FULL:5268/ch19:198, M:732, ch09:192, appC:112. The probe "finite lattice called an approximation of ℤ^d" returns no line in either after-tree.

**Values whose reading depends on L → ∞, or on a finite-size extrapolation.** Each is stated at `main` with its lattice sizes and with its extrapolation labelled.

| Value | Where | Finite-L basis | Dependence |
|---|---|---|---|
| $m_b/m_\tau = 2.361$, 0.4 % (0.5σ) | appA:85 (row 16, class L), SM:1267, ch06:208, ch19:152 | $Z_S(0.122)=1.813\pm0.001$ at $L=32$, cubic interpolation | The match is quoted at $L=32$. The "$\sim0.7\sigma$" figure, $Z_S\approx1.83$ and $m_b/m_\tau\approx2.34$ are L → ∞ extrapolations; "finite-volume systematics are not exhaustively quantified" |
| $Z_S$ volume behaviour | SM:1140, SM:1656 | $L=16, 32, 64$ | "converges from 1.70 … to 1.94 ($L{=}64$)" and "volume-converged region ($mL\gtrsim3$)" describe three finite-L values. This is numerical; no convergence theorem is cited |
| Regulator difference, about 2 % at $L=32$ | SM:1138 | corner modes excluded from a free-field sum | "converges to it at $L\to\infty$" concerns an explicit free-field momentum sum, not the interacting theory |
| $A\cdot B\approx48$–$62$ (against fitted 46.4) | SM:713, :742–759, :783, :817, :1300; ch04:48; ch06:94; appC:273; appA:30, :217 | $N\le$ the computed sizes; largest computed value 41.7 | Wholly an N → ∞ extrapolation. Labelled model-conditional and inconclusive (C class, appA:30) |
| $c_{F^3}$ sensitivity 8.4 | SM:756 | $N=8$–$20$, $1/N^2$ extrapolation | extrapolation |
| Vertex-correction channel "approaches zero at continuum limit" | SM:765 | $N=6$–$12$, values falling as $1/N^{\sim5}$ | extrapolation, stated with its data |
| Confinement of the purely induced theory | SM:801 | $L=2$–$8$ | A phase statement is an infinite-volume statement. The data are finite-L; the closing sentence generalizes beyond them |
| $\Sigma\approx0.20$; $m_{\rm match}^{\rm MC}=0.1234\pm0.0002$ (1.4 % from $\lambda g_0^2$) | SM:813, :1144, :1261, :1302 | $L=32$ | finite-L values; no L → ∞ claim |
| T-violation exactly zero | SM:645 = ch06:62 | substratum rings $L=4,6$, $q=2,3,5$ | an exact finite check of a finite-carrier counting lemma (X-16, F). It is evidence for the finite case only and is stated with its sizes |

None of these readings is changed by the A1-exit changes. Their dependence on finite-size extrapolation is pre-existing and stated where they appear. SM:1140's "converges" and SM:801's closing sentence are the two places where the wording goes beyond the finite data. They are recorded here; they are not A1-exit regressions.

## 6. R1 and C1 (X-11, X-71)

**R1 (physical justification of the selected law).** Missing premises, as named after both layers:
- the measure selection, "a maximal-entropy principle … on a finite representative — a standard but substantive epistemic postulate, not derived" (Main posit ledger (iv), M:738 at `main`);
- the induced-measure identification, "a conjecture about the correct map, not a derived property" (SM:809);
- the stationary-law hypothesis of SM §4.2, "which is open" (SM:811).

Selection over laws on a carrier of unspecified cardinality has no stated form (ledger X-11). The MC verdicts that sample the induced measure are stated as "conditional on the measure identification" (SM:809). No unconditional claim.

**C1 (coupled shell law).** GR:58 is stated "For a finite total system" with the boundary interaction negligible at the shell scale, under H-count ("that the total system is finite and that …"). No claim is printed for coupled bijections, for which no normalized invariant shell law is established (ledger X-71). GR §7.4 states that "Each formula uses the conditions of its derivation", and its calibration paragraph reads "The conditional horizon calibration". No unconditional claim.

## 7. Recorded for the owner

- **No material correctness defect** in the sense of #1169 comment 7214186738 was found.
- **Two clauses whose reading shifts once A1 is gone** (§4, observation, not a finding): M:362 "into a compatible closure/limit" and M:784 "the continuum is the mathematical idealization of its finite-resolution physical description". Neither is a prediction or comparison, and neither layer introduced them; they are listed here so the owner sees them before the A1 posit is deleted.
- **The 10 edits that do not apply at `main`** are D184/D185 (ch19:212 and mirror), D255/D256 (ch09:104 and mirror), D366 (Sub:201), D369 (Str:154), D375/D376 (ch02:134 and mirror) and D385/D386 (ch04:172 and mirror). #1588 and #979 rewrote these sentences after H. At H each one changes no number. Each lies outside every prediction and status table, and carries the justification its `reason` records. Their re-cut forms are the plan's reconciliation (#1477 PREREG §9). At current `main` the #979 changes already drop "finite" at the four X-53 sites, and #1588 already replaces "six structural properties" at ch09:104.

## 8. Re-check at the final H (a delta, not a redo)

The H-drift mitigation (owner, #1169 c.7214186738) suspends merges to `papers/`, `book/` and ledgered paths until retirement lands. At the final H:
1. `git diff --stat d7794dc9e43a0c66328747354787a707ed2dae88 <H> -- 'papers/*.md' 'book/*.md'`. If it is empty, this report's `main` results are the final-H results for every unchanged edit. Otherwise, read the number tokens of the changed lines (`delta.py` reports them per file only for edited files; a changed file with no edit is read directly).
2. `delta.py --rev <H> --plan-dir <plan dir at the final plan head> --prev-edits <edits.json at 4c79be64>`. Its change key is `(file, old, new, old_step2, new_step2)`, the fields `edits_check.variant` reads at `4c79be64`; if the final plan's `variant` reads any further field (for example, a re-cut field for the ten edits), the key must be extended to cover it before this step is relied on.
   - **Edit list.** Only the edits it lists as added or changed are read, together with the not-applicable list, which must be empty at the final H.
   - **Tokens.** The token loss must still be exactly the three tokens of §2, unless an added or changed edit explains a difference.
   - **Tables.** "edits touching a prediction or status table row" must be 0, or each listed row is classified by §3's rule.
3. For each added or changed edit, classify it by PLAN §3 and add a row to §3.1 in a short delta note. The integrated `--compare-tree` run (§2) need not be repeated unless step 2 reports a changed table row or a lost token.

Everything in §§3.2, 4, 5 and 6 is H-independent while step 1 is empty and step 2 lists no added or changed edit at an X-47, X-48, X-11 or X-71 site.

## 9. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| `edits.json` (blob `ec384fdf`) and `edits_check.py` (blob `1153e039`) at PR #1477 head `4c79be64` | §§2, 3, 7: what Layer R changes; the application rule | **support off `main`: a gap.** It closes when #1477's record lands on `main`. This record does not land before that record, and lands with it or after it |
| `53c6601a` (H), `d7794dc9` (`main` at drafting), `1c7eedc4` (pin) | §§1–3 | support on `main` (ancestors of `main`) |
| `f10195d4` (r6 Amendment 8, branch `design/a1-minimum-path-20261127`) | PLAN goal link: the audit is listed as necessary | provenance; the necessity also rests on owner requirement 6 and DP-1, quoted |
| #1169 comments 7048255658, 7049542030, 7062144714, 7074687817, 7213780573, 7214186738 | requirement 6, R6 acceptance, edit justifications, authorization, policy | provenance; quoted or cited as the owner's recorded decisions |
| #1477 comments 7061693815, 7074137435 | justifications recorded in the edits' `reason` fields | provenance; the edits' reasons are carried in `edits.json` |
| PRs #1470, #1472–#1475, #1494 | attribution of Layer S changes | provenance; the changes are on `main` |
| PRs #979, #924, #1558, #1560, #1588 | changes after H, outside the audit | provenance |

## 10. Verification status (§A.46 item 4)

| Claim | Evidence level | Missing | Accountable Issue | What would resolve it |
|---|---|---|---|---|
| No prediction or status table row changes; net number-token loss is exactly 3, each accounted for (§§2, 3) | Deterministic computation with the accepted extractor, reproducible from §2 | Independent review; the plan record on `main` (§9) | #1468 | A non-author review of this record; #1477's record landing |
| Every changed label or number on a prediction or empirical line has a cited justification (§3.1) | Writer's reading of the word diffs and of each edit's `reason` | Independent review | #1468 | A non-author review |
| X-48 reading (§4); X-47 dependence table (§5); R1/C1 premises (§6) | Writer's reading of the sites at `main` and in the after-tree | Independent review | #1468 | A non-author review |
| Results at the final H | Not yet available (H not chosen) | The delta of §8 | #1468 | §8 run at the final H |
