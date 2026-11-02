# Re-check: introductory-paper design, revision 3

- **Objects:** `S/paper/design/OUTLINE-r3.md`, `CONTRIBUTION-r3.md`, `SOURCES-r3.md`,
  `CHANGES-r3.md` and `probe/cards.py`, against `RECHECK-r2.md`, `S/paper/explainer/REVIEW.md`
  and `main` `687e885b` (worktree `S/paper/mainwt`).
- **Read-only.** No repository file changed. Git ran with `-c gc.auto=0 -c maintenance.auto=false`.
- **Own check:** `S/paper/review/r3/mycards.py`. It is written independently of `probe/cards.py`
  and run with `python3 -I`.

## Verdict: BLOCK (wording only), one required change

- RC-1, RC-2, RC-3, n1 and n2 are applied correctly.
- The six-part mapping, the absorption candidates, the mapping of the eleven stale items, the
  budget shift, R23, R24, contribution items 7 and 8, and non-claim 12 introduce no overclaim.
- I confirm the designer's new card-table finding independently, exactly, and with one further
  rule.

The block is for §5-h's scope sentence and for non-claim 13, which repeats it.
- They call the card game classical, with an entanglement-breaking one-step channel and "classical"
  indivisibility. They cite Main:286 and Main:702.
- They omit what Main:702 and Main:326 say about this same map: under the permutation-unitary
  embedding, its two-step map is the identity channel, its indivisibility is also
  CP-indivisibility, and the swap realization admits no classical-memory decomposition.
- So, unqualified, "its indivisibility is classical" is in tension with two Main statements the
  row itself cites or depends on.
- The fix is one sentence (RC-A).

***

## 1. RECHECK-r2 items

| Item | Result |
|---|---|
| RC-1, option (b) | **Applied.** The variant is renamed "BH-01-conflict-free" and says it is not free of conflict (OUTLINE-r3:344). ch07:126 s1 / FULL:2003 and GR:869 are in R11 (SOURCES-r3:347), in decision 1(a) for every scope carrying §7-h (:220–236), and in the §7 paragraph (OUTLINE-r3:267–279). Option (ii) is offered and its cost stated: the H-scramble finding is lost |
| RC-2 | **Applied.** CONTRIBUTION-r3:46–61 gives the replacement sentence per scope, and §10 (OUTLINE-r3:320–323) matches. The variant's sentence is faithful to §7-b, §7-h and §7-i |
| RC-3 | **Applied.** Decision 2 (SOURCES-r3:247–259), CONTRIBUTION-r3:69–81, R6 (:342) and UNTRACED-4 (:195) all require retention whatever the wording |
| n1 | **Applied.** R12 adds ch18:148 / FULL:4968 at the "conditions" level |
| n2 | **Applied.** OUTLINE-r3:267–279 |

**CHANGES-r3's observation on ch07:126 sentence 2** ("exponentially small corrections", which
contradicts BH-02 C5): this is not an R11 site for the paper, because the paper does not carry C5.
Recording it only for the owner's correction list is correct.

## 2. The card table (§5-h)

### Own exact check

ch01:273 describes:
- the hole card h as the visible bit and the burn card b as the hidden bit, both uniform and
  independent;
- the shuffle as the swap (h, b) → (b, h);
- 16 cases (h₀, b₀ and two fresh cards).

The matching odds P(hole at showdown = h₀):

| Protocol | Odds |
|---|---|
| one shuffle | 1/2 |
| two shuffles | 1 |
| chained one-street odds (Γ₁ = ½J computed from the swap, then Γ₁²) | 1/2 |
| peek, passive (no replacement) | **1** |
| peek, burn card overwritten by a fresh card | 1/2 |
| peek, only the revealed hole card replaced, burn kept | **1** |
| peek, both replaced | 1/2 |
| peek, the revealed card moved to the burn slot, fresh hole card (a literal reading of "a revealed card is burned and replaced", ch01:271) | 1/2 |

**The finding is confirmed.** The peek line's 1/2 needs the stored record, the burn card's h₀, to
be overwritten. If the burn card is left, the odds are 1. A passive look also gives 1, so the 1/2
comes from the intervention, not from observing.

`probe/cards.py` gives the same values for its rules A, B and C (its A is my last row, its C is my
"burn overwritten" row). Its chained value is hard-coded as ½J and not computed, so my check
computes it.

### The indivisibility claim holds

- Γ₁ = ½J and Γ₂ = I.
- Γ₂ = Γ₁Λ has no stochastic solution, since Γ₁Λ = ½J for every stochastic Λ.
- φ has order 2, so §5-c applies. The readback of (C4) holds (x₂ = x₀), so §5-e applies too.

### RC-A — §5-h's scope sentence is incomplete in a way that conflicts with Main (required)

OUTLINE-r3:227 has "Stated scope: a classical toy whose one-step channel is entanglement-breaking
(Main:286); the indivisibility is classical; no Bell violation". CONTRIBUTION-r3 non-claim 13 says
"Its indivisibility is classical, its one-step channel is entanglement-breaking …" and item 8 says
"its classical scope".

My check embeds the swap as a permutation unitary with a uniform hidden qubit:
- Φ₁(|+⟩⟨+|) = I/2, the constant channel of Main:286, which is entanglement-breaking;
- Φ₂(|+⟩⟨+|) = |+⟩⟨+|, so Φ₂ is the identity channel, which is not entanglement-breaking.

Main says the corresponding things about this map:
- **Main:326** (theorem, framework scope): for the permutation-dilation family, P-indivisibility
  implies CP-indivisibility. Here no CPTP Λ gives id = Λ∘Φ₁, because Φ₁ is constant.
- **Main:702** (the same swap φ(x,h) = (h,x), with an initialized slot): its two-step maps are
  ρ ↦ |0⟩⟨0| and ρ ↦ ρ, and "this swap realization admits no classical-memory decomposition".

The card game is classical on configuration (card) inputs. Its memory is not classical in the
open-system sense once the map is embedded as §3-d does. Without that qualifier, the row and
non-claim 13 read as "the swap's memory and indivisibility are classical", against Main:326 and
Main:702.

**Exact fix.** In OUTLINE-r3 §5-h, replace "Stated scope: a classical toy whose one-step channel is
entanglement-breaking (Main:286); the indivisibility is classical; no Bell violation (ch01:286;
Main §3.3)" with:

> "Stated scope: on configuration (card) inputs the game is a classical stochastic process, and its
> P-indivisibility is the population notion (2) of Main:334. Under the permutation-unitary
> embedding (§3-d) the one-step channel is the constant, entanglement-breaking channel (Main:286),
> but the two-step map is the identity channel; the family is CP-indivisible (Main:326) and this
> swap realization admits no classical-memory decomposition (Main:702). A card arrangement violates
> no Bell inequality (ch01:286; Main §3.3)."

Then:
- in CONTRIBUTION-r3 non-claim 13, replace "Its indivisibility is classical, its one-step channel
  is entanglement-breaking" with "On card inputs its statistics are classical stochastic ones; its
  one-step channel is entanglement-breaking, though its two-step map under the unitary embedding
  is not (Main:286, :702)";
- in item 8, replace "its classical scope" with "its scope".

### The rest of §5-h is accepted

- The list of what is not carried is right, and each reason checks against the source:
  - the C1–C4 "card form": ch01:271's three modifications are bijectivity, burn cards for C1–C3,
    and an intervention rule, so C4 is not among them;
  - "quantum, not classical, statistics" (ch01:269);
  - "interference term" (ch01:282) and "phase … where the information resides" (ch01:284);
  - the cat paragraphs;
  - the unistochasticity sentence (ch01:286). The tension with Main:270 (every rational doubly
    stochastic one-step matrix is a uniform-prior bijection marginal) and with Main:204 (the
    framework's own marginals fail unistochasticity at n_V = 3) is real.
- Calling the ch01 sites "a book matter" (R23) is right.
- **Nit n-A.** "with a uniform burn card" should read "with a burn card uniform and independent of
  the hole card". With a two-card deck (b₀ = 1 − h₀), Γ₁ is a permutation and the game is
  divisible.

## 3. Replacing the Explainer

- **The six-part mapping** (OUTLINE-r3:97–120) is coherent.
  - Every outline section has a part. §6 is split between parts 3 and 6 for a stated reason, and
    §9, §10 and the references are explained as outside the parts.
  - Part 6 answers "why full quantum equivalence is not established" with E2 plus bare OI ⇏ QM,
    §6-b, §6-e and §8-a. That is the right answer, at the right scope (qubit for independence).
- **The stale-item mapping** (OUTLINE-r3:82–93) matches the eleven items of REVIEW.md §3 one for
  one. Item 1 uses Main:522's binding, item 7 is contradicted by §6-b, and item 9 carries the
  formalization status.
- **The absorption candidates** are correctly limited to candidates. The D-gauge display is
  rightly excluded as Main §3.1 content (Main:232–238), and the lineage survey and the
  decompression section are rightly excluded.
  - **Nit n-B.** The quantum-weirdness candidate cites "Main:666, double slit" as "Main-supported
    content". Main:666 is interpretive prose with no proof, and it says "The Everettian measure
    problem dissolves". If the candidate is used, it should be carried as interpretation, class (e)
    as in §1-a and §6-a, not as a result.
- **R24, item 7 and non-claim 12** state the replacement scope without overclaim. The deliberate
  gap (ħ, cosmology, SM) is stated and pointed to Main and the Book.
- **No known result is presented as novel.** Every originality entry is still AUDIT r4's or a
  package's own, and no new class was introduced for §5-h ("not classified (illustration)").

## 4. Budget

- The sum is 0.25 + 1.25 + 0.75 + 1.75 + 1.25 + 2.25 + 1.75 + 1.75 + 1.0 + 0.5 + 0.25 + 0.5 =
  13.25 pp of body, plus 1.0 pp of references, for 14.25 pp. That is correct.
- §5 at 2.25 pp (about 1,240 words) for eight items, including the card table with its rule and
  scope, is plausible.
- §9 at 0.5 pp (about 275 words) is tight for the descriptions AUDIT §7 requires. Those include
  the F14–F17 rewrites, DO3 as concurrent work, and Milz and Strasberg as studies of Kolmogorov
  consistency. Flag it as the next section to give way.

## Nits

- **n-A** and **n-B** are above.
- **n-C.** OUTLINE-r3:1 still reads "revision 2". Several cross-references still point to r2
  files: OUTLINE-r3:141, :149 and :236; SOURCES-r3:168 and :204 (decision 1's heading); and
  CONTRIBUTION-r3:4–5.
- **n-D.** Decision 1's recommended mathematics list (SOURCES-r3 under "Decision 1") reads "§5-c to
  §5-g". Make it "§5-b to §5-h".
- **n-E.** Appendix A's alternative (OUTLINE-r3:332) suggests "§9 to 0.5 pp" as a cut, but §9 is
  already 0.5 pp in r3. Name a different cut.
- **n-F.** Option (ii) is called "conflict-free" (SOURCES-r3 decision 1(a)). It is free of
  contradiction, but ch18:148 / FULL:4968 remains a conditions-level site against §7-i (R12).
  Say so in the same line.
