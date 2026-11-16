# CHANGEMAP-A1C-r6-min — Addendum 1: exact edit pairs for the seven unapplied entries

Base: `main` at `e4c6ba7f`. The worktree `wt-2a` holds the 126 applied r6-min edits, uncommitted; none of the lines below is changed there. This addendum adds no site and changes no entry's purpose: it turns each of the seven entries left unapplied in IMPLEMENT-2a-r1 into exact old/new pairs. **Not applied.**

## Conventions

- Each pair is a single replacement on the named line. The old string occurs exactly once on that line at `e4c6ba7f` (checked), and the line is the same in `wt-2a`.
- An empty new string deletes the old string; its leading space is part of the old string, so no double space is left.
- `<LINE>` deletes the whole line, together with the blank line after it.
- A book chapter pair is applied byte-identically to the FULL line named (§A.14). FULL line numbers are given at `e4c6ba7f` and, where they differ, in `wt-2a`. The N-K18-186 (c) deletion moves later FULL lines up by two, so apply by string or bottom-up.
- Bell scope phrase, the N-M54 wording of Main §3.3's Corollary, parts (1) and (2):

  > on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality

  Where a sentence already concerns the nearest-neighbour or reference cubic graph (Sub:48, Sub:171, ch03:40), only part (2)'s finite-region condition is added, as in N-U35. The cone scope is "for finite-range couplings", as in the map.
- **Proposed drops.** Three listed Bell sites (ch01:183, ch03:186, glossary:19) assume ontic parameter independence directly; they do not derive it from the graph cone. Main §3.3 itself separates the two steps: "(ii) and (iii), which with the cone lemma secure ontic parameter independence" (Main:404). Only the cone step needs a finite site set or finite reading sets. Determinism, parameter independence and measurement independence give factorization and $|S_{\rm CHSH}|\le2$ on any hidden-variable probability space, so these sentences make no claim that rests on A1, and adding the scope would understate a result that holds unconditionally. Each drop carries a fallback (`-alt`) pair in case the owner keeps the edit.

## N-U34

Summary: Bell finite-region scope added at Sub:48 and Sub:171 (Sub:171 does state a Bell no-go, so it is kept, not dropped); Sub:467 cone scoped to finite-range couplings and the N-M54 Bell scope inserted.

### N-U34 (a)

Location: `papers/Substratum.md:48` (Sub:48)

Old:

```text
together with interventions each reading and writing only its own wing and readouts outside the remote setting's graph cone
```

New:

```text
together with interventions each reading and writing only its own finite wing region and readouts in finite regions outside the remote setting's graph cone
```

Note: The sentence concerns the nearest-neighbour update, so the any-cardinality case is part (2) of the Main §3.3 Corollary, which needs finite regions.

### N-U34 (b)

Location: `papers/Substratum.md:171` (Sub:171)

Old:

```text
in a Bell protocol with one-step own-wing read/write setting interventions, a $\pm1$ outcome at each wing in every run, and readout regions outside the other wing's graph cone over its duration
```

New:

```text
in a Bell protocol with one-step own-wing read/write setting interventions on finite regions, a $\pm1$ outcome at each wing in every run, and finite readout regions outside the other wing's graph cone over its duration
```

Note: Sub:171 does carry a Bell conclusion, stated as a no-go: the nearest-neighbour reference cone "cannot itself realize M1-B" under measurement independence. It is the Corollary's statement, so it takes the Corollary's finite regions. The sub-edit is kept, not dropped.

### N-U34 (c)

Location: `papers/Substratum.md:467` (Sub:467)

Old:

```text
The dependency graph gives an exact causal cone.
```

New:

```text
The dependency graph gives an exact causal cone for finite-range couplings.
```

Note: As in the map.

### N-U34 (d)

Location: `papers/Substratum.md:467` (Sub:467)

Old:

```text
For a response-complete deterministic completion with one-step
```

New:

```text
For a response-complete deterministic completion, on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, with one-step
```

Note: The N-M54 scope wording.

## N-Y11

Summary: Meth:339 gets "with finite setting and readout regions"; the N-M54 Bell scope is inserted at the Bell conclusions of :381, :385, :389, :391; the cone sentences of :389 and :391 are already scoped and are left as they are.

### N-Y11 (a)

Location: `papers/Methodology.md:339` (Meth:339)

Old:

```text
for wings separated by more than its graph cone;
```

New:

```text
for wings separated by more than its graph cone, with finite setting and readout regions;
```

Note: As in the map.

### N-Y11 (b)

Location: `papers/Methodology.md:381` (Meth:381)

Old:

```text
satisfying the setting and readout hypotheses of Main §3.3 nevertheless obeys
```

New:

```text
satisfying the setting and readout hypotheses of Main §3.3, on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, nevertheless obeys
```

### N-Y11 (c)

Location: `papers/Methodology.md:385` (Meth:385)

Old:

```text
Bell is sharper: for a response-complete deterministic completion, one-step
```

New:

```text
Bell is sharper: for a response-complete deterministic completion on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, one-step
```

### N-Y11 (d)

Location: `papers/Methodology.md:389` (Meth:389)

Old:

```text
But when the completion is response-complete and deterministic, one-step
```

New:

```text
But when the completion is response-complete and deterministic, on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, one-step
```

Note: The first sentence of :389, "…for finite-range substrata", is already scoped and is not edited.

### N-Y11 (e)

Location: `papers/Methodology.md:391` (Meth:391)

Old:

```text
through that graph. If the setting interventions are applied at one step,
```

New:

```text
through that graph. On a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, if the setting interventions are applied at one step,
```

Note: The cone sentence of :391 ("for any substratum whose Bell-relevant couplings are finite-range") is already scoped and is not edited.

## N-K01-16

Summary: ch01:16 cone scoped to finite-range couplings and the Bell scope inserted; ch01:183 proposed DROP (parameter independence is assumed, so the sentence is Bell's theorem itself and does not rest on A1); fallback wording given.

### N-K01-16 (a)

Location: `book/ch01-observation.md:16` (ch01:16); FULL `book/The-Incompleteness-of-Observation-FULL.md:351`

Old:

```text
The coupling graph of the underlying dynamics gives exact causal cones.
```

New:

```text
The coupling graph of the underlying dynamics gives exact causal cones for finite-range couplings.
```

Note: As in the map.

### N-K01-16 (b)

Location: `book/ch01-observation.md:16` (ch01:16); FULL `book/The-Incompleteness-of-Observation-FULL.md:351`

Old:

```text
At the response-complete deterministic level, setting interventions,
```

New:

```text
At the response-complete deterministic level, on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, setting interventions,
```

### N-K01-16 (c)

Location: `book/ch01-observation.md:183` (ch01:183); FULL `book/The-Incompleteness-of-Observation-FULL.md:518`

**No edit.** Proposed DROP. ch01:183 assumes parameter independence directly ("measurement independence plus parameter independence would imply $|S_{\rm CHSH}|\le2$"). That is Bell's theorem itself, which needs neither the graph cone nor a finite site set, so the sentence makes no claim that rests on A1. Its cone sentence already reads "for finite-range substrata".

### N-K01-16-alt (c) — fallback, only if the drop is declined

Location: `book/ch01-observation.md:183` (ch01:183); FULL `book/The-Incompleteness-of-Observation-FULL.md:518`

Old:

```text
that records a $\pm1$ outcome in every run, measurement independence
```

New:

```text
that records a $\pm1$ outcome in every run, on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, measurement independence
```

Note: Only if the owner declines the drop of N-K01-16 (c).

## N-K03-40

Summary: ch03:40 gets finite setting and readout regions; the Bell scope is inserted at :162 and :180; ch03:186 proposed DROP (parameter independence assumed); fallback wording given.

### N-K03-40 (a)

Location: `book/ch03-structural-realism.md:40` (ch03:40); FULL `book/The-Incompleteness-of-Observation-FULL.md:905`

Old:

```text
With one-step own-wing setting interventions, readouts outside the other wing's graph cone
```

New:

```text
With one-step own-wing setting interventions on finite regions, readouts in finite regions outside the other wing's graph cone
```

Note: The sentence concerns the reference cubic graph, so the finite-region condition of part (2) is the whole scope needed.

### N-K03-40 (b)

Location: `book/ch03-structural-realism.md:162` (ch03:162); FULL `book/The-Incompleteness-of-Observation-FULL.md:1027`

Old:

```text
If the setting interventions, applied at one step,
```

New:

```text
On a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, if the setting interventions, applied at one step,
```

Note: The sentence derives factorization from the coupling range not connecting the wings (the cone), so it takes the theorem's scope.

### N-K03-40 (c)

Location: `book/ch03-structural-realism.md:180` (ch03:180); FULL `book/The-Incompleteness-of-Observation-FULL.md:1045`

Old:

```text
If the setting interventions, applied at one step,
```

New:

```text
On a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, if the setting interventions, applied at one step,
```

Note: As :162.

### N-K03-40 (d)

Location: `book/ch03-structural-realism.md:186` (ch03:186); FULL `book/The-Incompleteness-of-Observation-FULL.md:1051`

**No edit.** Proposed DROP. ch03:186 states the conclusion for "a completion that keeps ontic parameter independence and measurement independence", that is, with parameter independence assumed rather than derived from the cone. That is Bell's theorem itself, which uses no finite site set; nothing to correct.

### N-K03-40-alt (d) — fallback, only if the drop is declined

Location: `book/ch03-structural-realism.md:186` (ch03:186); FULL `book/The-Incompleteness-of-Observation-FULL.md:1051`

Old:

```text
a completion that keeps ontic parameter independence
```

New:

```text
a completion on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality that keeps ontic parameter independence
```

Note: Only if the owner declines the drop of N-K03-40 (d).

## N-Kappc-32

Summary: The Bell scope is inserted at appendix-c:32 and :34.

### N-Kappc-32 (a)

Location: `book/appendix-c-objections.md:32` (appendix-c:32); FULL `book/The-Incompleteness-of-Observation-FULL.md:6262` (`wt-2a`: 6261)

Old:

```text
If the Bell-relevant coupling range is finite at the wings' separation, the setting interventions,
```

New:

```text
On a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, if the Bell-relevant coupling range is finite at the wings' separation, the setting interventions,
```

### N-Kappc-32 (b)

Location: `book/appendix-c-objections.md:34` (appendix-c:34); FULL `book/The-Incompleteness-of-Observation-FULL.md:6264` (`wt-2a`: 6263)

Old:

```text
By the Bell ceiling theorem (Main §3.3), a response-complete deterministic completion
```

New:

```text
By the Bell ceiling theorem (Main §3.3), on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality, a response-complete deterministic completion
```

## N-Kgl-19

Summary: Proposed DROP (glossary:19 assumes parameter independence, so it is Bell's theorem itself); fallback inserts the Bell scope with the book-correct reference "(Main §3.3)", not "(§3.3)".

### N-Kgl-19 (a)

Location: `book/glossary.md:19` (glossary:19); FULL `book/The-Incompleteness-of-Observation-FULL.md:6603` (`wt-2a`: 6600)

**No edit.** Proposed DROP, for the same reason as ch01:183 and ch03:186. glossary:19 assumes "measurement independence plus ontic parameter independence" directly, which is Bell's theorem with no cone and no finite site set. If the owner keeps the edit anyway, the book-correct form is given as N-Kgl-19-alt.

### N-Kgl-19-alt (a) — fallback, only if the drop is declined

Location: `book/glossary.md:19` (glossary:19); FULL `book/The-Incompleteness-of-Observation-FULL.md:6603` (`wt-2a`: 6600)

Old:

```text
with a $\pm1$ outcome in every run, gives Bell factorization
```

New:

```text
with a $\pm1$ outcome in every run, on a finite site set and for the nearest-neighbour cubic update with finite wing and readout regions on a site set of any cardinality (Main §3.3), gives Bell factorization
```

Note: Only if the owner declines the drop. The book cites Main by name, as in "(Chapter 1 §1.7; Main §3.3)" at appendix-c:32, so the reference is "(Main §3.3)", not "(§3.3)".

## N-K18-186

Summary: ch18:186 return stated for a finite model, with the physical-units and astronomical-period sentences deleted; :188 Falsifiability paragraph deleted with its blank line; :190 opens "A finite model is periodic with period $N$, …" and the cyclicity-commitment sentence is deleted. No fragment is left and the period bounds stay.

### N-K18-186 (a)

Location: `book/ch18-beyond.md:186` (ch18:186); FULL `book/The-Incompleteness-of-Observation-FULL.md:4992`

Old:

```text
The return itself is definite: the universe returns to its exact initial state after $N$ substratum time steps,
```

New:

```text
The return itself is definite: a finite model returns to its exact initial state after $N$ substratum time steps,
```

Note: Q10 (c): the return is stated for a finite model.

### N-K18-186 (b)

Location: `book/ch18-beyond.md:186` (ch18:186); FULL `book/The-Incompleteness-of-Observation-FULL.md:4992`

Old:

```text
 Translating to physical units with the substratum time step $\tau_{\text{sub}} \sim t_{\text{Pl}} \sim 10^{-43}$ seconds multiplies the recurrence time by $\tau_{\text{sub}}$, which changes its logarithm by about $10^2$, negligible at these magnitudes. A period of astronomical size is vastly longer than the age of the universe, vastly longer than the lifetime of the proton, vastly longer than any timescale physics conventionally treats, and at such a period the recurrence has no practical empirical consequences.
```

New: empty (delete the old string)

Note: Deletes the two sentences that apply the period to the universe. The bound sentences ("It is at most $g(|S|)$ … no lower bound on $N$.") stay.

### N-K18-186 (c)

Location: `book/ch18-beyond.md:188` (ch18:188); FULL `book/The-Incompleteness-of-Observation-FULL.md:4994`

Old: `<LINE>`, the whole of line 188, which begins

```text
**Falsifiability.** The recurrence prediction is falsifiable only in the logical sense.
```

and ends

```text
with a period at most $g(|S|)$ that divides $\mathrm{lcm}(1, \ldots, |S|)$, and below $|S|$ for the exactly linear rule.
```

New: nothing (delete line 188 and the blank line 189 after it)

Note: Deletes the Falsifiability paragraph (the prediction, Q10 (c)), together with the following blank line, so no doubled blank remains.

### N-K18-186 (d)

Location: `book/ch18-beyond.md:190` (ch18:190); FULL `book/The-Incompleteness-of-Observation-FULL.md:4996`

Old:

```text
The conceptual content is significant. The framework predicts that the universe is *cyclic at the substratum level* — periodic with period $N$, the least common multiple of the bijection's cycle lengths.
```

New:

```text
A finite model is periodic with period $N$, the least common multiple of the bijection's cycle lengths.
```

Note: No fragment is left. The cycle-structure mathematics that follows is kept.

### N-K18-186 (e)

Location: `book/ch18-beyond.md:190` (ch18:190); FULL `book/The-Incompleteness-of-Observation-FULL.md:4996`

Old:

```text
 The framework's commitment to substratum cyclicity is one of the structural commitments that distinguishes it from frameworks treating the universe as either fundamentally non-cyclic (most cosmological models) or fundamentally infinite (most quantum gravity programs).
```

New: empty (delete the old string)

Note: Deletes the cyclicity-commitment sentence about the universe.

## Result check (dry run on copies of the base files, primary pairs only)

- All old strings found exactly once on their lines; every chapter line equals its FULL line at `e4c6ba7f`.
- ch18:186–190 after the pairs read: "The return itself is definite: a finite model returns to its exact initial state after $N$ substratum time steps, … and it supplies no lower bound on $N$." followed by "A finite model is periodic with period $N$, the least common multiple of the bijection's cycle lengths. … and at the substratum level the dynamics has no preferred direction." No fragment remains, and the period bounds ($N\le g(|S|)$; $N<|S|$ for the exactly linear rule) are kept as statements about finite models.
- Counts: 7 entries; 21 primary pairs (N-U34 4, N-Y11 5, N-K01-16 2, N-K03-40 3, N-Kappc-32 2, N-Kgl-19 0, N-K18-186 5); 3 proposed drops (ch01:183, ch03:186, glossary:19), each with 1 fallback pair.
