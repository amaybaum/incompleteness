# F29 follow-ups: corpus search

**Corpus.** `papers/*.md`, `book/*.md`, and `book/The-Incompleteness-of-Observation-FULL.md`,
at `c967d6a9`.

**Patterns.** The searches were case-insensitive, extended regex.

1. Horizon quantifiers:
   - `every finite (accessible )?horizon`
   - `every (accessible )?horizon`
   - `each finite (accessible )?horizon`
   - `per (finite )?accessible horizon`
   - `per[- ]horizon`
   - `for all \$?K`
   - `histories of length`
   - `history of length`
2. Slogans:
   - `C1, C3,? (and )?C4`
   - `C1/C3/C4`
   - `⟺ ?C1`
   - `\iff ?C1`
   - `embedded observation under`
   - `C1[–-]C4 realization`
   - `(C1)–(C4) realization`
   - `on each (finite )?(accessible )?horizon`
   - `on accessible horizons`
   - `each accessible horizon`
   - `every accessible window`
   - `witness order`
3. Quantifiers over `K`, the history-length convention, and the endpoint wording:
   - `for (every|all|each) \$?K`
   - `every \$?K ?(\geq|≥)`
   - `all (finite )?horizons`
   - `every finite \$?K`
   - `arbitrarily long accessible horizons`
   - `each horizon`
   - `every horizon`
   - `common (endpoint|present)`

**Result.** 84 distinct `file:line` locations.

**Classes:**
- **O**: outdated, corrected by this change.
- **C**: correct as stated, with its hypotheses named.
- **U**: unrelated to the quantifier or the history length.

## O: outdated, corrected (8 lines; 5 sites, one of them mirrored)

| Location | Claim | Correction |
|---|---|---|
| `papers/Explainer.md:353` | theorem statement "⟺ embedded observation under C1, C3, C4 (per finite accessible horizon)" | anchor at an order $k$, every $K \geq k+1$, readback at $k$ (review finding 2) |
| `papers/Explainer.md:373` | non-Markovian ⟺ realization "on each finite accessible horizon" | anchor at an order $k$, every $K \geq k+1$, readback at $k$ |
| `book/appendix-b-derivations.md:454` | equivalence "on each finite accessible horizon" | as above |
| `book/appendix-b-derivations.md:455` | display "… C1, C3, C4, per finite accessible horizon" | display $\exists k\,\forall K \geq k+1$, readback at $k$ |
| `FULL.md:6221` | mirror of appendix-b:454 | mirrored byte for byte |
| `FULL.md:6222` | mirror of appendix-b:455 | mirrored byte for byte |
| `papers/Main.md:167` | readback lemma: "histories … of length $k$ with a common endpoint" | values of $X_{<k}$, length $k$, followed by common present $X_k = c$; $p_0$ bounds $\Pr[X_{<k}=p, X_k=c]$ |
| `papers/Main.md:170` | proof: "common endpoint $c$", unnamed $w_a$ | "common present state $c$", $w_a = \Pr[X_{<k}=a \mid X_k=c]$ |

## C: correct as stated (49)

### Already witness-anchored by #932 (4)

| Location | Content |
|---|---|
| `papers/Main.md:522` | (iii): for some accessible order $k$ and every $K \geq k+1$ |
| `papers/GR.md:20` | the same anchoring |
| `book/glossary.md:39` and `FULL.md:6639` | "for some accessible order, every finite accessible horizon extending at least one step beyond it" |

### Main's own per-horizon and existential statements (12)

| Location | Content |
|---|---|
| `papers/Main.md:476` | "stated per finite horizon": the realization is per horizon |
| `papers/Main.md:496` | dilation for one given $K$, "for all $k \leq K$" |
| `papers/Main.md:514` | "(ii) ⇒ (iii) ⇒ fixed-$\hat H$ form … per horizon" |
| `papers/Main.md:597` | bare form displayed and declared false in the text (`:598`) |
| `papers/Main.md:608` | "per accessible horizon containing the witness order $k$" |
| `papers/Main.md:610` | names the unrestricted every-horizon form as false, and states the per-witness form |
| `papers/Main.md:614` | "some per-horizon (C1)–(C4) realization exists", existential |
| `papers/Main.md:616` | "admits a per-horizon C1–C4 realization", existential |
| `papers/Main.md:618` | per-horizon equivalence; the all-time form is negative |
| `papers/Main.md:715` | "(ii) ⇒ (iii) … per accessible horizon" |
| `papers/Main.md:80`, `:172` | the coin has zero backflow "on arbitrarily long horizons" and "at every horizon time": a property of the coin, true |

### Representation equivalence on every horizon, and a section pointer (6)

These are true on every horizon, Markov laws included.

| Location | Content |
|---|---|
| `papers/Main.md:82` | $S \iff D \iff Q_{\rm fb}$ "on every finite accessible horizon" |
| `book/preface.md:3` and `FULL.md:74` | "the equivalence … exact on every finite horizon": the representation equivalence |
| `papers/Main.md:510` | fixed-$\hat H$ form "at every horizon time", for a realized process |
| `book/ch01-observation.md:73` and `FULL.md:417` | "the characterization theorem in its current per-horizon form", a section pointer; see the note under U |

### Slogans: "⟺ C1/C3/C4 per (finite) accessible horizon" (11)

This re-checks the earlier review's claim that these sites are unaffected.

None of these sites quantifies over horizons with "each" or "every". "Per accessible horizon"
names the type of the realization: a per-horizon realization, with the hidden space growing with
the horizon. That is Main's own wording in its existential statements (`:614`, `:616`). Read
as Main reads it, the slogan is the theorem: (ii) holds iff a per-horizon C1/C3/C4 realization
exists, which by `:610`, `:614` and the corrected (iii) is anchored at a witness order.

The phrase "per-horizon biconditional" (appendix-c:106) also has a true horizon-local reading:
for each $K$, the $K$-law has memory iff it has a C1/C3/C4 realization.

**Verdict:** correct as stated, unaffected. The earlier review's claim is confirmed.

| Location |
|---|
| `papers/Explainer.md:1021` |
| `papers/Substratum.md:111` |
| `papers/Substratum.md:126` |
| `book/appendix-b-derivations.md:22` and `FULL.md:5789` |
| `book/appendix-b-derivations.md:406` and `FULL.md:6173` |
| `book/appendix-c-objections.md:106` and `FULL.md:6352` |
| `book/ch02-substratum.md:90` and `FULL.md:733` (existential: "arises … for some partition") |

**Borderline.** The slogans are compressed, and a reader could take "per accessible horizon" to
mean "on every horizon". Changing them was not in the owner's scope, and the reading above makes
them correct. They are listed here for the reviewer.

### Necessity, per condition and universal over realizations (12)

These state no horizon quantifier, and they are correct as stated.

| Location |
|---|
| `papers/Explainer.md:348` |
| `papers/Explainer.md:352` |
| `papers/Explainer.md:1009` |
| `papers/GR.md:565` |
| `book/appendix-b-derivations.md:459` and `FULL.md:6226` |
| `book/appendix-c-objections.md:98` and `FULL.md:6344` |
| `book/appendix-c-objections.md:110` and `FULL.md:6356` |
| `book/ch04-methodology.md:182` and `FULL.md:1301`: the identification slogan, no horizon quantifier |

### Other characterization summaries without a horizon quantifier (4)

| Location | Content |
|---|---|
| `papers/Explainer.md:351` | P-indivisibility is not implied by C1/C3/C4 alone |
| `book/ch00-introduction.md:95` and `FULL.md:331` | sufficiency direction: under C1–C4 the description is non-Markovian |
| `papers/Main.md:76` | "the characterization's equivalence runs over those three" |

## U: unrelated (27)

| Location | Subject |
|---|---|
| `papers/GR.md:198` | "for all $k$" over an operator family |
| `papers/GR.md:607`, `FULL.md:1969`, `book/ch07-gravity.md:90` | "each horizon": Bekenstein–Hawking entropy |
| `papers/Main.md:508`, `book/glossary.md:15` and `FULL.md:6615` | "per-horizon transition family" in (T) |
| `book/glossary.md:25,27,29,31` and `FULL.md:6625,6627,6629,6631` | definitions of C1–C4 ("three structural conditions") |
| `book/glossary.md:99,105` and `FULL.md:6699,6705` | "non-Markovian on accessible horizons" in the Markov / non-Markov entries |
| `papers/Main.md:636`, `:690` | C1/C3/C4 necessity theorems listed as internal; the mechanism of C1–C4 |
| `papers/SM.md:14`, `:507`, `papers/Substratum.md:54`, `:128` | C1/C3/C4 diagnosing the memory-bearing sector |
| `book/ch02-substratum.md:212` and `FULL.md:855` | C1/C3/C4 diagnosing the memory sector |

**Note.** `ch01:73` / `FULL:417` ("in its current per-horizon form") is a section pointer. It
carries the history phrase "in its current form", but §A.33 governs `papers/`, and the book's
chapters keep their own register. It is pre-existing, outside this change's scope, and recorded
for the owner.

## Counts

| Class | Lines |
|---|---|
| O, outdated and corrected | 8 |
| C, correct as stated | 49 |
| U, unrelated | 27 |
| **Total distinct locations** | **84** |

The count lists each mirror line separately.

## History length

- "histories of length" and "history of length" occur only at `papers/Main.md:167`.
- "length-$k$ histories" occurs only at `:170`.
- "common endpoint" occurs only at `:167` and `:170`.
- No paper or book file paraphrases the lemma's hypothesis. GR:20 cites the lemma by name.
