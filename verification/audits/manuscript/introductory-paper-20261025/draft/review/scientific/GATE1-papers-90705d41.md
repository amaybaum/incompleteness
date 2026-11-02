# Gate 1 (scientific accuracy): focused confirmation of PR #918 r26 at `90705d41`

**Verdict: ACCEPT.** The card example now states the causal order correctly, every other edit is accurate, and nothing is weakened. I have no findings, required or optional.

I compared `d831fb83` (whose paper is r25 `366da4bb`) with `90705d41`, read-only, using a detached worktree that is now removed. Line numbers are at `90705d41`.

## Main check: the causal safeguard in the card example (L130–L134)
The three things are kept distinct and in the right causal order:
- **(i) The world's recurrence at L = 3.** The text says "the whole world, which returns to its starting configuration only at its recurrence time, step 3".
- **(ii) The forecasts' earlier return at step 2.** The text says "Both forecasts return to certainty at step 2, earlier than the whole world".
- **(iii) The failure of chaining.** The text says "The failure of chaining comes from the step-1 overlap together with this step-2 return, not from the step-3 recurrence: no step-by-step forecast can carry the overlapping forecasts of step 1 to the two certainties of step 2". This is Theorem 3 with s = 1 and n = 2.

I recomputed the example's bijection (visible {R, B}, hidden {0, 1, 2}, shared prior uniform on {0, 1}):
- after one step, the red row is a point mass on R and the black row is (½, ½), so the two rows overlap at R;
- after two steps, Γ = I;
- φ has order 3.

The other items in this passage:
- **Merged fixed-rule sentence (L130)** is accurate: "The comparison is about one fixed rule, the same hidden preparation tried from every visible start the world could have, not about the starts a sample happens to contain, and it means something only because the face-down card is dealt the same way whichever card is face up". A per-root deal appears only as the excluded contrast ("two different deals, not one rule started in two ways").
- **"Why keep a start that never occurs?" (L132)** is accurate. The observed record ("red at every step") is still separated from the hypothetical forecast from black ("part of the mathematical comparison, not something this observer measures").
- **Gloss of "overlap" (L132)** is accurate: "After the first shuffle both forecasts give red a positive chance, an overlap that comes only from the start that is never dealt [Main §2.3]". It matches Theorem 3 ("both positive in a common column") and Main's "possibly only through a row of a root of visible probability zero".
- **Gloss of "rooted family" (L132)** is accurate: "the table of forecasts from every start", matching the definition at L136.
- **"Return horizon"** first appears at its definition (L144). It is used again only at L160 and in Appendix A (L338).

## Inaccessible memory (L150): meets all three owner requirements
The case-2 sentence reads: "an observer confined to accessible windows sees neither the late conditional memory nor the failure of chaining it implies across the cycle: both remain established in the dynamics under the theorem's hypotheses, but neither appears in any accessible record."
- It names both properties.
- The established-in-the-dynamics clause sits right beside "neither appears".
- Nothing suggests either property is absent from the underlying dynamics.
- "the failure of chaining it implies" is correct: a memory witness of order k < L gives a non-permutation Γ_s, and hence failure on {0, …, L} (Main §2.3, Theorem).

(C4) is still stated correctly after the clause was dropped from case 2:
- L122 gives (C4) as "history readback, a memory witness at some accessible order".
- L156 says "what an observer can discriminate is memory at an accessible order, which (C4) asserts [Main §2.3, Scope]".

## Other edits: accurate
- **L138.** The removed clause ("a preparation that depended on the start would give rows for different setups, as in the card comparison above") duplicated L130's contrast. Nothing is lost.
- **L212.** "That is, the experimenter can always leave the system alone, combine operations, lump outcomes together, prepare an evenly mixed helper and act after preparing it, read the helper without disturbing the system, and discard it" now maps one to one onto GR §3.3 and `FiniteOperationalTheory`:

  | Plain clause | Structure field |
  |---|---|
  | leave the system alone | identity |
  | combine operations | outcome-conditioned composition |
  | lump outcomes together | coarse-graining |
  | prepare an evenly mixed helper | uniform-ancilla preparation |
  | act after preparing it | `prepAvail_post` |
  | read the helper without disturbing the system | spectator-independent readout |
  | discard it | ancilla discard |

- **L306 (R2, trimmed).** "Given determinism and an outcome in every run, quantum Bell correlations require giving up ontic parameter independence or measurement independence; with measurement independence retained, they require ontic parameter dependence, whose realization on the substratum without usable signalling and with the gravitational continuum limit is the open hypothesis H-Bell". Both alternatives remain, and the H-Bell scope is intact (Main §3.3).

## Unchanged material: confirmed
- **Exact statements** are word for word as in r25. I checked Theorems 1–4, both corollaries, the Γ_t definition, the Theorem 3 reading (L142), the recurrence lead-in (L144), the labelled paragraphs of §§4–6 and the Bell paragraphs.
- **The §2.4 Corollary** is byte-identical.
- **The ledger** changed only in `line` fields, so no ID is retired. `coverage_check` reports OK (134 statements).
- **The "Precisely" scope (L154)** is still explicit: "for the rooted family, with a hidden prior shared by every root and drawn independently of it and with a full-support visible prior, failure of P-divisibility on {0, …, L} is equivalent to M_k > 0 at some order k < L".
- **Nothing is weakened.**

## The owner's two final questions
- **Is every substantive claim supported by its evidence and assumptions?** Yes.
- **Does the paper communicate the strongest results without unnecessary weakening?** Yes. Every established result is stated at proved strength. The card example states the causal mechanism of Theorem 3 exactly: the overlap at step 1 plus the return at step 2, not the step-3 recurrence.