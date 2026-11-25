# A1-EXIT regression comparison (#1468): preregistration of the before/after comparison

**Status.** Writer's preregistration, WIP / UNVERIFIED. It is frozen before any after-state exists:
the A1 deletion has not been executed. Nothing here has been run against a deletion head. The only runs
were the baseline against itself, the Step-2 records replayed against their own merges, and synthetic
edits of the pinned corpus (§7). Independent non-author review is required before use.

**Authorization.** Owner `amaybaum`, #1169 comment 7058783437, 2026-11-21T06:42:54Z: "**Regression
comparison: approved for preparation now.** The before/after comparison against the preserved baseline
is conditionally authorized once the deletion has been executed and independently reviewed. Its verdict
requires separate scientific evaluation." The same record: "Removing the global finiteness assumption
must not be presented as proof that the theory works for every infinite system. Each result keeps its
own mathematical conditions." The design decision, #1169 comment 7057297534 (2026-11-21T04:30:15Z),
adds "a regression check against new global infinity assumptions". #1169 comment 7059136165
(2026-11-21T07:15:31Z), decision 6: the decision on executing the deletion comes after "an
independently recorded review of #1483".

This record authorizes nothing further. Running §2 requires the condition quoted above: the deletion
executed and independently reviewed.

**Goal link (§A.47).** A1-exit objective (#1169), owner requirement 6 (#1169 c.7048255658): "A final
regression audit shows that removing A1 has not weakened, strengthened or changed any physical
prediction without explicit justification." This preregistration fixes the procedure and the decision
rules that will decide that. It does not decide the outcome.

**Baseline.** The read-only before-baseline of #1471, landed on `main` (merge `0adc410c`) in
`verification/audits/foundations/a1exit-regression-20261121/`, pinned at
`1c7eedc402eafd2bac654484fa790874a33f444d`. Drafting base for this record: `main` at
`7f28886f4cc96fbfa7407af1fdc37de2f0e562e5` (`PIN_S2`), where all five Step-2 units have landed; no
manuscript changed on `main` between it and `97070c98`.

## 1. Frozen tools and inputs

| File | SHA-256 |
|---|---|
| `baseline.py` | `e0749fb926ce9da0ee52bad0ea9e0e80e4fa9f4edeb22c8009a303bf1af23ad9` |
| `snapshot.json` | `2db7832d7cb95b0ba77b42afad965696390d4ad67a6835b2c45f045bd04f88c8` |
| `compare/verdict.py` | `eb3f4fbf76bce9f67ad334cc457ed43495ede0a329f60c3f19d9f032a26b9219` |
| `compare/inputs/edits-s2.json` | `f43086e43663ea5becabee3b0439d338dca78da3170f6a1d951a5ec713583a4c` |
| `compare/inputs/finiteness-cases.json` (test fixture for T13e) | `9a516d196c2927e9872d6f60111bdd8bd23330c96ae3cd30d0dd7e2604909699` |
| the ledger's `rows.json`, read from the Git object at `PIN_S2` | `39e51d0cfd8d6855f17ef3d7253a43d372fae608a9dcae083fbeb52471b512a0` |

`FROZEN.json` records the same six digests. **C0** reads `FROZEN.json` and this file from the Git
objects at the frozen ref, never from the working tree. It passes only if:
- the frozen ref is the *pinned commit*: the commit on the first-parent chain of `main` (`origin/main`
  where it resolves, else `main`) that last changed `FROZEN.json`, which is this record's merge
  commit or the merge of its latest amendment. Any other commit, a PR head included, fails;
- every digest of the files in use equals `FROZEN.json` at that ref, and so does every frozen file's
  blob at that ref;
- this file at that ref states each digest in full.

A *preparation run* (`collect --prep`) is allowed only with the pin as head. Its frozen ref is the
checkout HEAD instead of the pinned commit, and its verdict text says that it is a preparation run and
not a regression verdict. J9 reads `rows.json` from
the Git object at `PIN_S2` whose digest C0 checks. The term lists of J9 and J10 are constants of
`verdict.py`, frozen with it.

None of these files changes after this record's review except by an amendment in `compare/amendments/`
made before the comparison is run. Amendment A2 (`amendments/A2-integration.md`) records the
integration of the concurrent revision `43122ff6` and the dispositions of its review: what is adopted
and what is superseded. If the deletion reconciles the ledger, an amendment states before the run
which ledger state J9 reads.

## 2. Procedure

**H.** The execution head is the commit the owner designates as the executed A1 deletion, after its
independent review. **Deletion commit.** The commit that lands the deletion's `edits.json`; it must be
an ancestor of H (C6).

**Checkout.** The tools are run from a checkout of `main` that contains this record. The deletion
branch is not used as the checkout. `DIR` is a working directory outside the repository.

1. **Collect.**

   ```
   python3 -I -B verification/audits/foundations/a1exit-regression-20261121/compare/verdict.py collect --head <H> --out <DIR> --frozen-ref <merge of this record> --del-commit <deletion commit>
   ```

   - `collect` refuses a non-empty `DIR`. It resolves H with `git rev-parse --verify H^{commit}` and
     records the full commit id; a head that does not resolve fails.
   - It runs C0, C4, C1, C2 and C3, the comparison `baseline.py --compare <H> --json DIR/compare.json`,
     and C5 (§5).
   - The comparison step passes only if `compare.json` was written by this run, has schema
     `a1exit-regression-compare/1`, `pin` equal to the baseline pin and `other` equal to the resolved H,
     and the exit status is 1 exactly when `any_change` is true. A crashed comparison, which also exits
     1, writes no `compare.json` into the fresh `DIR` and so fails.
   - It compiles the deletion unit's edits from the `edits.json` landed at the deletion commit into
     `DIR/edits-del.json` (§4), JSON to JSON, with no hand step, and records the SHA-256 of the landed
     `edits.json` blob.
   - It writes `DIR/controls.json` (schema `a1exit-compare-controls/2`) with the SHA-256 of every file it
     wrote. Exit 0 when every control passes, 4 otherwise.
2. **Classify.** Every reported item of `compare.json` (§3) is entered in `DIR/classify.json` (schema
   `a1exit-compare-classify/2`) as J or R, with its cited edit keys and ledger row, or is left out, in
   which case it is U. The file names its `head` (the resolved H), its author (`classifier`, a GitHub
   login) and the result PR (`result_pr`). The cited edits are keys of the frozen lists only; there is
   no hand-compiled edit list.
3. **Verdict.**

   ```
   python3 -I -B verification/audits/foundations/a1exit-regression-20261121/compare/verdict.py verdict --dir <DIR> --classify <DIR>/classify.json
   ```

   - It refuses to run (exit 2, no `verdict.json`) if `verdict.json` exists, if any file listed in
     `controls.json` differs from the digest recorded there, if `controls.json`'s `head`,
     `compare.json`'s `other` and `classify.json`'s `head` are not all the resolved H, or if any entry
     of `controls.json` has a `pass` that contradicts its `exit`.
   - No stored pass flag is trusted (§A.44). `verdict` re-runs C1, C2, C3 and C4
     itself, re-runs C0 and C6, and re-derives the comparison and C5's injected comparison from the
     frozen inputs, requiring each stored file to equal its re-derivation as canonical JSON (`other`
     aside for the injected tree); a file rewritten after `collect`, with its digest updated, fails
     (T20d). A control passes only if its
     re-run or re-check passes and its recorded `exit` is the expected one; every control `collect`
     must record is required.
   - If any control fails, `verdict` classifies nothing and writes `verdict.json` with verdict VOID
     and no item classes (review c.7059580868, finding 3). Otherwise it runs C7, C8 and C9 and the
     classification of C5's injected run, checks every J and R claim against §3, and writes
     `DIR/verdict.json` (schema `a1exit-compare-verdict/2`) with the SHA-256 of every input. The item
     classes are left out when a countercontrol fails.
   - Exit status: 0 PASS, 5 FAIL, 3 PENDING, 4 VOID. Status 2 is a refusal and any other status (1 is
     an uncaught exception) is no verdict. The verdict is read from `verdict.json` together with the
     exit status, never from printed text (§A.44); if the two disagree there is no verdict.
4. **Record.** `compare.json`, `controls.json`, `edits-del.json`, `classify.json` and `verdict.json` land
   in this directory under a result note. `--compare-tree` reports are not committed, because they name
   only a temporary tree.

## 3. Decision rule for each reported change

**Two separate checks** (review c.7066078604, N11; owner #1169 c.7061485446, item 1). Item 1 requires
an exact, character-for-character comparison against the frozen approved transformation, with no
whitespace exemption, and a correction needs a reviewed amendment. Under it, a head byte that differs
from the replay of the approved edits is an unapproved change, which no review can approve. The
comparison therefore runs two checks that never mix.

- **1. The byte gate.** The *replayed state* is the baseline at the pin with every landed approved
  edit applied: the frozen Step-2 list, then the deletion list as pinned (§4). In every manuscript file
  in scope, H must equal the replayed state byte for byte. Each differing hunk of raw lines yields U.
  - A hunk is counted through the reported items whose own lines make it up. These are the H lines of
    reported items, and the replayed lines that are a reported deleted or removed line or a
    replay-missing item. A deletion is therefore counted once.
  - Every other hunk is an item `BX:<file>:<line>`. This includes any blank-line or whitespace
    difference, and any line not reported as an item.
  - An item any of whose lines lies in a differing hunk is **U by the byte gate**. No J, no R, no
    resolution and no binding can change that.
  - **Scope.** The byte gate covers the manuscript files `papers/*.md` and `book/*.md` only, and the
    gate is not widened beyond them. Everything else the A1 retirement edits rests on #1477's own checks
    (`edits_check`, `preserve_check` and its TeX/PDF comparison), not on this gate. In #1477's plan at
    `55544cc3`, that is 90 of its 373 edits: `AGENTS.md`, verification records, and Lean and Python
    files. The generated `.tex` and `.pdf` files are also outside the gate. The verdict text states this
    scope.
- **2. The scientific classification** (J, R, J9, J10) applies only to items that pass the byte gate.
  Such an item's H text equals the replayed text of the approved edits, so the classification
  concerns the approved text itself, and an R resolution concerns approved text only. Because the byte
  gate already guarantees that H equals the replay, an R resolution can never cover a head byte that
  differs from it.
- **3. The bytes, recorded.** For every U and every R item, `verdict.json` records the exact bytes
  involved, H's lines and the replayed region. Each character outside printable ASCII is rendered
  visibly as `<U+XXXX>`, and a tab or CR as `\t` or `\r`, so that a reviewer sees, for example, a
  zero-width space, a CR or a line separator.

Everything below about J, R, J9, J10 and resolutions applies within check 2. The file-level items and
the resolution binding described below are superseded by the byte gate where the two differ.

**Reported items.** Every entry whose status is not `unchanged`; every relocated entry; every
`unaccounted` line; every `deleted` line. An entry moved within one file and otherwise unchanged is not
reported (baseline amendment A1, R4).

**Replay-missing items** (amendment A2). The comparison with the baseline cannot see a reviewed change
that H lacks or reverts, because the line then equals the baseline. The *landed edits* are the frozen
edits of every unit whose merge is an ancestor of H, then the deletion edits. They are applied in order
to the baseline, giving the replayed state. Each of the following is also an item:
- a line of the replayed state that carries reviewed new text (it is not a baseline line of its file),
  where H lacks it and H's aligned lines there are all baseline lines, or there are none;
- a landed edit that does not apply.

These items are U unless marked R and resolved; they are never J. A difference whose H side is itself
a change is already a reported item and is not counted twice (T21); that item is held to the replay
state by the completeness condition below.

**File-level exactness items** (review c.7062140466, N5; root-cause rule after N7 and N8, reviews
c.7063250049 and c.7064135477). The baseline comparison does not report blank lines. So every manuscript
file of H is also compared with the replayed state, line by line on the raw bytes, with whitespace,
blank lines and a final newline kept and no normalization at this level. A differing hunk is accounted
for by reported items only under the following rule. In every other case it is an item
`RX:<file>:<line>`: U unless marked R and resolved, never J, always flagged, and attributed in its notes
to the nearest reported item within three lines.
- **The root rule.** Every line of the hunk that is not itself a reported item's own H line must be
  byte-identical to its corresponding replayed line, blank lines included.
- **Where both sides have the same number of lines,** line k of H corresponds to line k of the
  replayed state.
- **Where the line counts differ,** the hunk is never accounted for: it is an RX item (review
  c.7065119625, N10). The earlier clause that let reported items account for an unequal hunk is
  removed. A deleted line, even a reported one, is therefore also an RX item.
- **What follows.** A blank replayed line is never accounted for by an adjacent item. So any byte
  difference on a line that is not a reported item's own line is an RX item. That includes a space,
  tab, CR, NBSP or other whitespace standing in for a blank line. A line-boundary change (a join, a
  split, an insertion, a removal or a reorder) changes the line sequence, so it cannot be byte-identical
  and is an RX item too.
- **What it subsumes.** This rule contains the clause proposed in review c.7064135477, "each blank H
  line identical, character for character, to its replayed counterpart", and the structure condition
  of the previous amendment.
- **No double counting** holds for equal-count hunks. A value change on a reported line is accounted for
  by its item, so C5 still counts its injection once (T13f). A hunk whose line count changes is always
  its own RX item.

An inserted blank line, joined paragraphs, a removed blank line and a changed trailing newline are each
an RX item (T13f). A head that is exactly the approved plan has none (T21).

**Classes.**
- **J, justified by a landed Step-2 unit or by the deletion edit.** Accepted only when the replay rule
  holds and neither J9 nor J10 sends the item to R.
- **R, needs scientific review.** The writer may mark any item R. An item whose replay holds but which
  fails J9, hits J10, or is relocated out of Main is R automatically.
- **U, unjustified.** Every item that is not J or R. In particular, an item that is not classified, or
  whose cited edits do not reproduce its after text and that the writer did not mark R, is U.

**Replay rule (J1–J8).** The cited edits are applied to the baseline file of the item, in the frozen
replay order (§4), each as an exact `old`→`new` replacement whose `old` occurs exactly once in the
current text; an edit applies to a file only if the file is in its `files`. An edit whose `old` is empty
or equals its `new` covers nothing. The *region* is the replayed text spanned by the item's baseline
line together with every replacement that touches it, extended to whole lines (for an unaccounted
line: a replacement's new text, extended to whole lines). Lines are compared whitespace-normalized.
- **Entry (text, value or label changed).** At least one cited edit touches the baseline line, and the
  replayed region equals the lines of the after file that contain the item's after line.
- **Removed entry, deleted line.** At least one cited edit touches the baseline line, and the replayed
  region occurs in the after file.
- **Unaccounted line.** The line lies in the region of a cited edit's new text, and that region equals
  the after file's lines around it.
- **Relocated.** Both of the above: the source region is replayed in the source file, and the
  destination line is reproduced in the destination file. A relocation out of Main is never plain J,
  because Main must stay independent of downstream papers (AGENTS.md, Code Review Rules).

**Completeness** (review c.7059976436, finding 2; the comparison with the replayed state of `43122ff6`,
kept as a J precondition). The cited edits are all landed edits. Every landed edit that touches the
item's region (for an unaccounted line, that produces its line) is cited. The region replayed from the
cited edits equals the same region of the replayed state. A reviewed change that H reverts on a line
that keeps another reviewed change therefore makes that item U (T21b: ch02:144, ch02:192).

Any residual difference in the region makes the item U, or R if the writer so marks it. Partial
coverage, a substring citation, a unit or a swapped value outside the reproduced text, and a no-op edit
therefore cannot produce J (self-test T4–T6, T12).

**J9 (label or text changed).** For an item whose kinds include `label changed` or `text changed`,
comparing the before region with the after region:
- no open, conditional or hypothesis term is lost (count not decreased), and no term of J10's lists is
  gained;
- if the entry has its own `ledger_rows` in `snapshot.json`: the cited ledger row is one of them and is
  listed on a cited edit that touches the region; for an F row a finite-scope term is present after the
  change and not lost by it; for an O row an open, conditional or hypothesis term is present after the
  change and not lost by it; a J row needs only the first condition;
- if the entry has no ledger row: a label change is R; a text change needs no finite-scope term lost.

Otherwise R.

**J10, the regression check against new global infinity assumptions.** J10 has two layers, computed
for every item. Neither depends on recognizing a wording.

*Normalization.* Every text J10 reads is first normalized:
- HTML entities are decoded;
- `ℕ`, `ℤ`, `ℝ` and `ℵ` are spelled out;
- NFKC is applied;
- soft hyphens (U+00AD), zero-width characters and LaTeX discretionary hyphens (`\-`) are removed;
- Cyrillic and Greek letters that render as ASCII letters are folded to them;
- each footnote reference `[^id]` is expanded inline with its definition from the same file.

Parenthetical content is already inline.

*The exact allowlist.* Two sentences are removed before anything is compared, and only where each
stands as a whole sentence, at the start or after a sentence or heading boundary and followed by
whitespace or the end:
- the owner's configuration-space sentence, verbatim (#1169 c.7058446475): "The substratum has a
  configuration space $\mathcal S$. No restriction is imposed on its cardinality; $\mathcal S$ may be
  finite or infinite.";
- its rendering with $S$ in #1477's plan: "The substratum has a configuration space $S$. No restriction
  is imposed on its cardinality; $S$ may be finite or infinite."

No other text is exempt. The earlier exemption of the clause "may be finite or infinite" is withdrawn.

*Layer 1, the exact expected text (structural, no vocabulary).* The *expected text* of an item's region
is what replaying its cited approved edits onto the baseline at the pin produces. It is derived only
from independently frozen inputs: the pinned corpus, `inputs/edits-s2.json` (C0, C6 (a)–(c)) and the
deletion edits compiled from the landed `edits.json`, accepted only when that blob has the approved,
pinned digest (§4, C6 (d)). It is never derived from H, from
`compare.json`'s texts, or from an earlier verdict. Both texts are normalized as above, and whitespace is
kept character for character.
- **Exactness (non-J).** A covered item is never J unless H's region equals its expected text
  character for character. Any difference, whitespace included, makes it R if marked or covered, U
  otherwise, and it is flagged. A covered item is also never J if H's region carries a token that
  neither the before region nor the new text of a cited edit carries.
- **Change flag.** An item whose normalized after region differs from its normalized before region,
  whitespace included and allowlisted whole sentences removed, is flagged `scientific_evaluation`,
  whatever its class.
- **Diagnostics.** The token sequence (ASCII words and every other non-space character, in order) and
  the finite-scope terms do not decide anything. They explain a flag in the item's notes: "token
  sequence" or "whitespace only", and any finite-scope term lost.

The allowlisted sentence followed by any further words changes the text, and is flagged.

*Layer 2, the vocabulary (on the approved edits' texts).* For a covered item, the frozen vocabularies
are counted, after normalization, in the before and after regions and in the old and new text of each
cited edit. A rise in the count of any term, or a fall in the count of the finite-scope terms, makes
the item never J: it is R if marked or covered, U otherwise, and it is flagged. An unclassified item is
counted the same way, so that its notes say what it gains. Every landed edit whose own new text gains a
term against its old text is listed in `verdict.json` (`flagged_edits`) and counted in the open
scientific evaluation. The terms, matched case-insensitively:
- `PROMOTION_TERMS`: `unconditional(ly)`, `proved`, `proven`, `proof(s)`, `theorem`, `established`,
  `derived`, `shown`, `demonstrated`, `in general`, `general`, `generally`, `generality`,
  `universal(ly)`, `always`, `without exception`;
- `INFINITY_TERMS`, quantifier and cardinality vocabulary:
  - any word beginning `infinit`; `\infty`, `∞`, `\aleph`; `countabl*`, `uncountabl*`; `cardinal*`;
    `arbitrar*`;
  - `finiteness`; `finite or not`; `not (necessarily) finite`; `non-finite`; `need not be finite`;
    `unrestricted`; `irrespective`; `independent of`; `uniform(ly)`; `large or small`;
    `no assumption`; `beyond the finite`; `transfinite`; `continuum`; `whatsoever`;
  - `\omega`, `ω`, `\mathbb{N}`, `|S|`, `\kappa`, `κ`, `\to \infty`;
  - `for` or `over` followed by `all`, `every`, `any` or `each`; `of any` or `for any` followed by
    `size`, `order` or `number`; `any number of`; `regardless`; `whatever`; `in either case`,
    `in both cases`, `in all cases` and the like;
  - `unbounded*`; `unlimited`; `without` (optionally `any` or `a`) followed by a word beginning
    `finit`, `bound` or `limit`, or by `restriction`; `no restriction`, `no bound`, `no limit`;
  - `all sizes`, `every cardinality`; `every`, `all`, `any` or `each` followed by a math
    expression (`$`).
- the finite-scope terms (stems and forms; review c.7061319560, N3), whose loss is a hit: any word
  beginning `finit` (finite, finitely, finiteness, finitary), `< \infty` in any form (`N < \infty`,
  `|S| < \infty`, `\lt \infty`, `< ∞`), `bounded`, `compact`. J9 uses the same terms.

*What J10 guarantees, exactly.*
- **Exactness.** No item is J unless H's region equals, character for character after normalization,
  the expected text that replaying its cited approved edits onto the baseline produces. Every other
  difference is non-J and flagged. This includes added, deleted or reordered wording, operators,
  punctuation and whitespace.
- **Change flag.** Every item whose region differs from its baseline is flagged, so every change
  reaches the scientific evaluation, J or not.
- **Vocabulary.** No item whose cited edits gain a vocabulary term, or lose a finite-scope term, is J.

These are statements of conformance to the frozen approved plan. **The mechanical comparison
establishes that H is the approved plan applied to the baseline. It does not establish that the plan
is scientifically correct.** That is the separate scientific evaluation's task, and the flags route
every change to it.

The standing batteries check this:
- T13 flags the 16 paraphrases of review c.7059976436, the 28 wordings of review c.7060670839, the
  allowlisted sentence followed by an unlisted claim, and a gain-only case.
- T13c flags the 11 deletion, reordering, operator and punctuation cases of review c.7061319560.
- T13d checks that a whitespace-only difference from the expected text is not J and is flagged.

The mutants must fail: layer 1 disabled fails T13 (T13b), and the earlier set comparison fails T13c.

Some results do hold for arbitrary S. J10 does not treat such a statement as false: it sends it to
review, and the item clears only through a resolution whose review cites the proof that covers that
generality (below).

A justification that is not mechanically checkable, such as a reviewer's argument with no covering
edit, is R, never J.

**R resolution.** An R item is resolved only by a review recorded on the result PR. The resolution is
`{"outcome": "justified"|"unjustified", "review": <URL>, "reviewer": <login>, "proof": <citation>,
"binding": <binding>}`:
- `review` is the URL of a comment or review on the result PR (`result_pr`);
- `reviewer` is not `classifier`, compared case-insensitively;
- for an item with a J10 hit, a justified outcome also needs `proof`, the citation of the proof that
  covers the generality the after text states;
- **`binding` names the exact bytes the review assessed** (review c.7065119625, N9; owner
  c.7061485446, item 1):
  - for each H line the item covers, in order, its file, its line number and the SHA-256 of its raw
    bytes;
  - the SHA-256 of the replayed (approved) text of the item's region, or of its baseline text where no
    cited edit covers it.

  `verdict.py` computes this binding for every item and lists it in `verdict.json`, so that the review
  copies it. A resolution applies only when the item's binding at the run equals the recorded one
  exactly: the same files, lines, order, line count and digests. With any other byte, line, order or
  count difference, the resolution covers nothing, and the item is U.

So a resolution can never approve bytes that differ from the approved transformation unless it names
those exact bytes. A CR, a zero-width character, a line separator, an NBSP or a second edit on an
R-resolved line makes the item U. So does a swap or a join of R-resolved lines (T13i).

A resolution that fails any of these leaves the item unresolved. An unjustified outcome counts as U.
`verdict.json` lists every resolution with its URL. `verdict.py` checks the form offline; that the
URL's author is the named reviewer, and not the classifier, is checked against the host by the review
of the result PR.

**Scientific evaluation flag.** An item is flagged when any of the following holds:
- it carries any of the categories C-TAB, C-PROSE, C-FINL, C-CDO, C-CAL, C-OBS or C-OPEN;
- it carries a `value changed` kind, or a J10 hit (including a lost finite-scope term);
- its normalized after region differs from its before region, whitespace included (J10, layer 1);
- it is an unaccounted or deleted line flagged `numbers` or `marker`;
- its before or after region contains a decimal, a number with a unit, a power of ten or a comparison
  marker.

No category is exempt. The flag is set whatever the class.

## 4. Justification sources (frozen inputs)

**Step-2 units.** `compare/inputs/edits-s2.json` (schema `a1exit-compare-edits/2`) holds every edit of
S2-A to S2-E, 139 in all, amendments composed. It is generated by `verdict.py compile-s2` from the Git
objects at `PIN_S2` and frozen by C0. Each edit carries its key (`<unit>:<id>`), PR, `files` (with the
FULL mirror where the record names one), `old`, `new`, ledger `rows`, its replay order `seq`, and
`components`: the source record file and the JSON index or the 1-based line span of each Old and New
block it was compiled from. The unit table carries each unit's merge commit and the blob id of every
allowlisted source at `PIN_S2`.

| Unit | PR (merge) | Allowlisted sources (in composition order) | Edits |
|---|---|---|---|
| S2-A | #1470 (`0cd5d5bf`) | `checks/s2a_edits.json` | 17 |
| S2-B | #1473 (`a1f38284`) | `PREREG.md`, `amendments/A1-round1.md`, `A2-return-form.md`, `A3-cptp-register.md` | 29 |
| S2-C | #1474 (`0ba358cc`) | `PREREG.md` §5, `amendments/A1.md`, `RESULT.md` §9.1 | 28 |
| S2-D | #1472 (`4de2eabd`) | `PREREG.md`, `amendments/A1.md` | 20 |
| S2-E | #1475 (`7f28886f`) | `checks/s2e_edits.json`, `checks/s2e_amend1.json` | 45 |

Record directories: `verification/audits/manuscript/a1exit-s2{a,b,c,d,e}-20261121/`.

**Compilation rules.**
- JSON sources: each object, with `mirror` or `full_mirror` giving the FULL file.
- Markdown sources: paired `Old ...:` / `New:` fenced text blocks under a `### <ID> —` heading, with the
  sites from the heading or its `Sites:` line and the ledger rows from the heading; S2-D's "identical to
  <ID>" FULL entries copy that edit's strings; S2-C §5 and S2-B A3 are tables (`\|` unescaped); S2-C A1
  is `- old:` / `- new:` bullets, wrapped lines joined by one space, applied in the order the amendment
  states, with A1-1 checked against the 15 sites the amendment names.
- Composition: an amendment with an `amends` field composes into that edit; any other amendment composes
  into every edit of its unit, in its files, whose new string contains its old string exactly once;
  with no such edit it stands alone.
- S2-C's catch-up resolution of C4 (RESULT §9 and §9.1: the only splice resolved by hand) is the edit
  `S2-C:C4-resolved`: old the line Main:224 at the merge's first parent, new the resolved line quoted in
  §9.1. It replaces C4.

**Replay validation.** Applying the five units in landing order, from the pin, reproduces every
manuscript file at each unit's merge byte for byte (C6 (c)). The frozen list is therefore each unit's
whole manuscript change and nothing more.

**Deletion unit.** `DEL` edits are taken only from the deletion's `edits.json` as landed
(`verification/audits/foundations/a1exit-deletion-20261121/edits.json`), by `verdict.py compile-del
--commit <deletion commit>`, JSON to JSON, keeping the `papers/` and `book/` Markdown edits in list
order. They replay after the Step-2 edits. A record whose `old` equals its `new` (a site recorded as
retained unchanged) is not an edit: it covers nothing, is left out of the list, and its ID is listed
under `retained_unchanged`.

**Approved deletion list, pinned** (review c.7062140466, N6). The deletion edits are read from the history
of the head under test, so they are independent only if their source is pinned.
- `verdict.py` carries `DEL_APPROVED_SHA256`, the SHA-256 of the *approved* `edits.json`: the blob named
  by #1477's independent acceptance and by the owner's decision to execute the A1 retirement. It is
  frozen with `verdict.py` by C0.
- It is a required field, unset in this record, because #1477 is still being amended. A reviewed
  amendment made after #1477 is accepted, and before the comparison is run, fills it in.
- C6 (d) passes only if the landed `edits.json` blob has exactly that digest. If the pin is unset, or
  the blob differs from it, the run is VOID (T15b).

**What is not a source.**
- #1476 changed CI only, and #1471 is the baseline itself.
- Any manuscript change that reaches H from a PR not listed here has no source, so its items are U
  unless reviewed as R.

## 5. Controls

All must pass, or the verdict is VOID.

| Control | What | Pass condition |
|---|---|---|
| C0 | Frozen tools, inputs and ledger (§1), at `collect` and again at `verdict` | the frozen ref is the pinned commit on the first-parent chain of `main` (in a preparation run at the pin: the checkout HEAD); every digest and every frozen blob at that ref equals `FROZEN.json` there; this file at that ref states each digest |
| C1 | `baseline.py check` | exit 0 (snapshot regenerates byte for byte from the pin) |
| C2 | `baseline.py self-test` | exit 0 |
| C3 | Baseline against itself: `baseline.py --compare 1c7eedc4…` | exit 0, a fresh `self-compare.json` with no change |
| C4 | `verdict.py self-test` (T1–T22, with T13b–T13i, T15b and T20d) | exit 0 |
| C5 | Countercontrol for the comparator: H's corpus copied to a temporary directory, one unjustified value change injected (the first unchanged entry of a prediction table, the last digit of its first decimal token), compared with `--compare-tree`, classified with the same `classify.json` | a fresh `injected-compare.json` with `any_change` true reporting the entry `value changed`; the entry is U and the U count is the main U count plus one |
| C6 | Edit inputs (§4) | (a) `compile-s2` from the records reproduces `edits-s2.json` exactly; (b) every edit is non-empty and not a no-op, of a listed unit with that unit's PR, every component from that unit's allowlisted sources; (c) the replay validation of §4 holds; (d) the landed `edits.json` blob has the approved, pinned digest `DEL_APPROVED_SHA256` (unset or different: VOID), `compile-del` reproduces `edits-del.json` exactly, the deletion commit is an ancestor of H, and the deletion edits applied to its first parent reproduce its manuscript files byte for byte. (d) is not applicable only when H is the pin |
| C7 | Bad-citation countercontrol: in a copy of H's corpus, the first J item with an after line has one number token outside its cited edits' new strings changed (or, with none, " 0" appended), and the copy is compared and reclassified with the same edits and `classify.json` | that item becomes U, and the U count is the main U count plus one |
| C8 | J10 countercontrol: the sentence " The same identity extends to every infinite system." is appended to a J item's line, with a synthetic edit carrying exactly that change and listing the item's ledger row, so that the replay holds. **Precondition:** the copy is J with J10 disabled, so that only J10 can stop J; the first J item that meets it is used (up to five tried), else C9 (b)'s item | the precondition holds, and with J10 the item is R, with a J10 hit, and flagged |
| C9 | Decisive control on the pinned corpus, each case cited J to an edit that reproduces it and lists the row: (a) ch01:179's "Without A1, the near-return condition" rewritten as "For every infinite system, the near-return condition" (row X-26); (b) GR:134 (row X-52, disposition J) gains the allowlisted configuration-space sentence; (c) GR:134 gains ", for arbitrary $S$"; (d) GR:134 gains ", and this is proved"; (e) the first J-row prose entry with one open, conditional or hypothesis term loses it; (f) appB:42 (row X-15, disposition J) loses "finite" from "on a finite configuration space"; (g) appB:194 (row X-52, disposition J) loses "finitely many" | (a) is R, flagged, J10-hit, and stays R under a review that cites no proof; (b) is J; (c), (d), (f) and (g) are R, flagged and J10-hit; (e) is R |

If the main run has no J item with an after line, C7 runs on T3's synthetic item and C8 on C9 (b)'s
item, and `verdict.json` records that they did.

**Mutants (self-test).** Each of C6–C9 fails when the rule it guards is broken: C6 catches a fabricated
S2-B edit (`old` "conditional", `new` "finite"), an empty edit, an S2-E edit sourced to the S2-C record
and one altered frozen edit (T15); C7 fails when the replay rule is replaced by the earlier containment
rule J1 (T17); C8 fails with J10 disabled and with `INFINITY_TERMS` empty (T17); C9 fails under each of:
J10 disabled, `PROMOTION_TERMS` empty, `INFINITY_TERMS` empty, the finite-loss test removed, the
allowlist removed, and J9 always passing (T18). A `controls.json` whose `pass` contradicts its `exit`
is refused (T20b); C0 rejects a commit that is not the pinned one (T20c).

## 5a. Invariants and checkpoints (§A.41)

| Invariant | Checkpoint |
|---|---|
| Tools, inputs and ledger are as frozen | C0 at `collect` and at `verdict`, against `FROZEN.json` at the frozen ref |
| The frozen Step-2 list is what the records state and what the units landed | C6 (a), (c) |
| Every edit is a non-empty, non-trivial edit of its own unit's allowlisted sources | C6 (b); T15 |
| The deletion edits are the landed list and the deletion's whole manuscript change | C6 (d) |
| Outputs are this run's, for H | fresh-`DIR` refusal; `other`, `pin` and schema checks; recorded digests and head checks at `verdict`; T20 |
| A crashed step is not a pass | file-written and exit-status checks; T20 |
| The comparator detects an unjustified value change | C5 |
| The classifier rejects a citation that does not reproduce the change | replay rule; C7; T4–T6, T12 |
| Every change in an item's region, whitespace included, is flagged | J10 layer 1 (change flag on exact normalized text); T13, T13c, T13d; T13b and the set-comparison mutant |
| No item is J unless H's region equals its expected text character for character | J10 layer 1 (exactness); T13c, T13d |
| The expected text depends only on frozen inputs | the replay reads the pinned corpus, `edits-s2.json` and the compiled deletion list only; C0, C6 |
| No item whose cited edits gain a vocabulary term is J | J10 layer 2; C8; C9 (a), (c), (d); T13 |
| A result does not lose its finiteness condition as J | J10 finite-loss test on the widened finite-scope terms; C9 (f), (g); T13c, T13e |
| A lost open term on a J row is not J | J9; C9 (e) |
| The owner's cardinality-neutral sentence, row-supported, is not blocked | exact allowlist; C9 (b) |
| A generality claim clears only by an independent review citing its proof | resolution rule; C9 (a); T18b |
| R is resolved only by a non-classifier review on the result PR, bound to the exact bytes it assessed | resolution rule with `binding`; T7, T13i |
| The verdict is given only over green controls, and nothing is classified over failed ones | `verdict_of`; VOID without classification; T11 |
| No stored pass flag is trusted, and no stored comparison | `verdict` re-runs every control and re-derives both comparison files; T20b, T20d |
| Only the pinned frozen commit is accepted | C0; T20c |
| Every reported item is classified | `items_of` coverage, unlisted means U; T2, T10 |
| A landed reviewed change absent from H, or reverted in it, is not passed | replay-missing items; completeness; T21, T21b |
| H equals the replay of the approved edits byte for byte, and no review can approve a difference | byte gate (U, unresolvable); T13i, T22 |
| No difference from the replayed state anywhere in a file goes unreported, newlines included, and none is absorbed into an adjacent item | file-level exactness items (RX), root byte-identity rule; T13f, T13g, T13h; T21 |
| The deletion edits are the approved list, independent of the head under test | `DEL_APPROVED_SHA256` in C6 (d); T15b |
| A PASS does not settle requirement 6 | `requirement6_settled: false` and the verdict text (§6) |

## 6. Verdict rule (owner requirement 6)

| Verdict | Condition |
|---|---|
| **VOID** | any control or countercontrol fails |
| **FAIL** | there is at least one U item |
| **PENDING** | there is no U, and at least one R item is unresolved |
| **PASS** | there is no U item, and every R item is resolved as justified by an independent review |

The verdict text is generated by `verdict.py` from the counts:
`VERDICT <v>: <n> reported changes; J <a>, R resolved as justified <b>, R unresolved <c>, U <d>;
<k> flagged for scientific evaluation; controls <pass|FAIL>; countercontrols <pass|FAIL>.` It always
ends: "Owner requirement 6 is settled only by the separate scientific evaluation; scientific evaluation
is open for k items and m landed edits.", with m the landed edits listed in `flagged_edits`. A
preparation run's text begins "PREPARATION RUN at the pin, not a regression verdict." `verdict.json`
carries `requirement6_settled: false` in every case.

**What PASS does not settle.** Only the separate scientific evaluation, recorded on the result PR,
settles requirement 6. Every flagged item, J or not, goes to it. A PASS is not presented as showing that
any result holds for infinite systems; each result keeps its own conditions.

## 7. Preparation runs

All runs were made on the pin, on the Step-2 records and on synthetic data only, from the tree of this
record's head. The pin self-run is a preparation run (`collect --prep`), whose frozen ref is the
checkout HEAD; a non-preparation C0 at this PR's head fails, as it must (T20c).
- `verdict.py self-test`: T1–T21b PASS. These include:
  - the standing J10 battery, with all 47 cases flagged (T13);
  - the sequence battery: the 11 deletion, reordering, operator and punctuation cases are all flagged,
    and the set-comparison mutant fails it (T13c);
  - a whitespace-only difference from the expected text is not J and is flagged (T13d);
  - the nine planned deletion records that remove only the word "finiteness" (D001, D061, D180, D181,
    D184, D185, D190, D191, D227) each lose a finite-scope term, while the earlier narrow list misses
    seven of them (T13e);
  - an inserted blank line, joined paragraphs, a removed blank line and a trailing newline are each
    an RX item, U and flagged, and the unchanged corpus has none (T13f);
  - the same structural changes next to a line whose H text differs from the replay, including the
    review's example (GR:134 with a doubled space and an adjacent paragraph join), are each an RX item
    (T13g);
  - a space, tab, CR, NBSP, em space or ideographic space in place of the blank line before or after
    such a line, and a swap of two adjacent lines, are each an RX item (T13h);
  - on a line produced by an approved edit, a CR, ZWSP, U+2028, NBSP or a second edit; a swap and a
    join of two such lines; and a `$$` deleted next to one, each with R resolutions whose bindings are
    copied from H, give U by the byte gate and a verdict that is not PASS (T13i);
  - the 139 approved Step-2 edits replayed together onto the pin, each item citing its landed edits,
    give no U (T22);
  - an unapproved deletion of a reported line is counted once (T13f);
  - the approved-list pin: unset or altered gives VOID, approved passes (T15b);
  - the gain-rule mutant, which fails the battery on the bare footnote marker and the gain-only case
    (T13b);
  - the mutants of C6–C9 (T15, T17, T18);
  - the forged `controls.json` (T20b) and C0 at a non-pinned ref (T20c);
  - a rewritten `compare.json`, which fails its re-derivation (T20d);
  - the same-line reverts at ch02:144 and ch02:192 (T21b).
- `verdict.py check-edits`: PASS. The frozen Step-2 list equals its compilation from the records, and
  replaying the five units from the pin reproduces every manuscript file at each unit's merge byte for
  byte; the deletion list is not applicable at the pin.
- `collect --prep --head 1c7eedc4`, the baseline against itself, into a fresh directory: C0 (preparation)
  to C5 pass; C5 injected FULL:1642 `0.3183` → `0.3184`.
- `verdict` on that directory with an empty classification: the controls were re-run, both comparison
  files were re-derived,
  and the text began "PREPARATION RUN at the pin, not a regression verdict. VERDICT PASS: 0 reported
  changes; …; controls pass; countercontrols pass." Exit 0, `requirement6_settled: false`. C7 ran on
  T3's synthetic item and C8 on C9 (b)'s item. C9 gave (a) R, staying R without a proof; (b) J; (c), (d),
  (e), (f) and (g) R.
- A second `verdict` into the same directory was refused (exit 2).
- `compile-del` on #1477's plan, as a format check only: 264 manuscript edits; D032 and D039, recorded
  there as retained unchanged, are set aside.

No deletion head was compared.

**Pre-execution gate: finiteness-term removals** (owner, #1169 c.7061485446, item 2). The vocabulary
layer, run over the approved edit texts, finds 65 edits that remove a finite-scope term: 12 in the
frozen S2 list (S2-B:E4, E6a, E6b, E12a, E12b, E12d, E13a, E14, E15a, E15b, E16; S2-E:E12) and 53 in the
#1477 D-records at `e924e583`. Before execution, each is classified scientifically on the predicted
retirement text, with the original claim, the resulting claim, the hypotheses the result requires and
the mathematical justification:
- removing finiteness as a global foundational premise is intentional;
- removing it from a theorem that requires it is prohibited;
- replacing global finiteness by a weaker sufficient local hypothesis is acceptable only when justified
  mathematically.

The other flagged edits receive a scope review. This record does not carry that classification. The
list is regenerated by applying `j10_hits(old, new)` to each edit of `inputs/edits-s2.json` and of
`compile-del`'s output.

## 8. Limits

- The replay rule shows that cited reviewed edits produced the change. It does not show that an edit is
  scientifically right; that is the job of the flag and of the separate evaluation.
- J9 and J10's second layer are lexical, and a lexical list is not complete. J10's guarantee is the
  one stated in §3. No item is J unless H's region is its expected text exactly, and every change is
  flagged. A change made by an approved edit and worded outside the vocabulary can be J; it is
  flagged, and it reaches the scientific evaluation through the flag. Every J item whose region changes
  goes to the scientific evaluation; the flag does not block a PASS.
- The comparison establishes conformance to the approved plan, not the plan's scientific correctness.
- **No whitespace exemption** (owner, #1169 c.7061485446, item 1). The comparison stays exact, character
  for character, against the frozen approved transformation. Whitespace differences are flagged and
  non-J: doubled spaces, newlines, indentation and changes inside mathematical expressions. A reviewer
  may classify a flagged difference as formatting-only. That never makes it an approved change: a
  correction needs an explicitly reviewed amendment.
- The principle is zero unauthorized differences and zero unsupported strengthening of mathematical
  claims, not zero flagged changes (same record, item 3). Inserting the allowlisted sentence itself is a
  change and is flagged; it is exempt only from J10's vocabulary.
- J10's vocabularies are deliberately wide: many reviewed changes will be R and will need a review, and
  a generality claim needs one that cites its proof.
- The author of a resolution's review is checked against the host by the result PR's review, not by
  `verdict.py`, which compares logins case-insensitively. The content of `proof` is checked by that
  review.
- The compilation rules of §4 are fitted to the five records as they stand; C6 (a) and (c) show that
  they reproduce those records and their merges exactly, and a changed record fails C6.
- The comparison inherits the baseline's limits (baseline RESULT §4). A prediction stated without a
  marker or number form is not an entry, but a change to it is still reported as an `unaccounted` or
  `deleted` line.

## 9. Off-`main` references (§A.42 item 8)

| Reference | Claim | Classification |
|---|---|---|
| #1169 c.7058783437, c.7057297534, c.7059136165, c.7048255658 | Authorization, safeguard, infinity-regression check, requirement 6 | provenance, quoted with author and time |
| #1477 and its branch | The deletion plan whose landed `edits.json` becomes a source | provenance now. Its edit list is used only as landed with the executed deletion; until then it is not a source |
| #1477's `--static` infinity scan | Checks the deletion's own edit strings | provenance; not a substitute for J10, which reads the integrated after-state |
| The preparation runs (§7) | The tool works on the pin, on the Step-2 records and on synthetic data | provenance; the claim rests on `verdict.py self-test` and `check-edits`, reproducible from `main` once this record lands |
| PR records #1470–#1475 | Justification sources | support on `main` (merges and blobs in `edits-s2.json`) |
| `43122ff6` and its blobs `505d0329` (`A1-replay.md`), `3d242ed2` (`edits/S2.json`), `ef9b7970` (`verdict.py`); the ref `preserve/w1483-09673477` | The superseded concurrent design, dispositioned in A2; the writer's commits before integration | provenance; reachable from `main` only if this PR lands by merge commit |
| `inputs/finiteness-cases.json`: nine records copied from #1477's plan at `e924e583` (blob recorded in the file) | Test fixture for T13e only | provenance; not a justification source. The deletion edits are taken only from the landed `edits.json` (§4) |
| #1483 c.7059580868 | Review of `43122ff6` | provenance; its findings are dispositioned in A2 |
| #1483 c.7059099956, c.7059220314, c.7059976436 | Review rounds of this record | provenance; their findings are addressed in this record and A2 |
| #1169 c.7058446475, c.7059632884 | The owner's configuration-space sentence (the J10 allowlist); the writer designation | provenance, quoted |

## 10. Verification status (§A.46 item 4)

- **Evidence level:** a preregistration with a tested tool. There is no result yet.
- **Missing:** independent review of this preregistration, of `verdict.py` and of the compiled
  `edits-s2.json`.
- No CI workflow runs `baseline.py` or `verdict.py`; their evidence is the local self-test, `check-edits`
  and the pin self-run, reproducible from `main` once this record lands.
- **Accountable Issue:** #1468.
- **Remaining gate:** the comparison runs only after the A1 deletion is executed and independently
  reviewed (owner record above). The verdict's flagged items need a separate scientific evaluation.
