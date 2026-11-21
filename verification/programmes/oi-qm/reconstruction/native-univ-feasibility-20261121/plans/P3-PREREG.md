# P3: does every excursion of a finite configuration of Q grow without bound? (paper preregistration)

**Standing.** Design and preregistration of a paper investigation, authorized by owner decision
[#1169 c.7064226074](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064226074)
item 3.4. The proof attempt itself is research work under that authorization. It runs no
computation, and the small exact checks named in §4 run only once separately authorized. Object:
Q = `R_{2^16}` on `ℤ³` at uniform backgrounds `c` (decision 3.2). Notation as in `P2-PREREG.md`.

## 1. Question

**Conjecture S(c).** Let `1 ≤ c ≤ q − 2`, and let a two-slice configuration differ from `(c, c)` on
a finite set. If the orbit has an excursion at some tick (P2 §1), its support over `t ≥ 0` is unbounded.

By NU2 this is equivalent to: no periodic finite orbit on the background `c` has an excursion.
The two directions: a periodic orbit visits finitely many states, so its support is bounded,
which gives S ⇒ "no periodic orbit with an excursion"; conversely, an orbit with an excursion
and bounded support over `t ≥ 0` is periodic by NU2, which gives the converse.

**Staged targets, in order (§A.12):**
- **S1:** single-site seeds `(a, b)` with `max(|a − c|, |b − c|) ≥ 2`, at `c = 2^15`.
- **S2:** seeds supported in one closed set of at most 3 sites, at `c = 2^15`.
- **S(c):** for every `c` in `[1, q − 2]`.

Each stage is stated, and proved or refuted, before the next begins.

## 2. Decision rule (fixed now)

- **Proof.** A written proof that uses only the lemmas of §3 at their stated standing. It counts as
  established at [W] once written, and as reviewed only after an independent non-author review.
  Until then it is reported as a writer's derivation.
- **Refutation.** One explicit finite configuration with an exact periodicity certificate (both
  slices bitwise equal after `P` ticks) and an exhibited excursion tick. A refutation found by P2
  counts once P2's controls are green.
- **Neither.** The stage is reported as open, with the step at which the attempt stopped. A partial
  argument is not reported as a proof of a weaker statement unless that statement is written out
  and proved in full.

## 3. Lemmas allowed, with their standing

- MQ1 (one-step confinement, sharp) and MQ2(a) (windowed confinement): MEAS-Q `RESULT.md` §2,
  [R], at that record's review standing.
- U1 Lemma 2.1 (the mid-alphabet embedding, one direction): [R].
- NU2 (`NOTE.md` §3.2): [W].
- The light cone of a radius-1 second-order rule: elementary.

Any further lemma is stated and proved in the P3 record before it is used.

## 4. Controls and countercontrols (for a paper argument)

| Id | Kind | Requirement on the argument |
|---|---|---|
| P3-K1 | countercontrol: a rule where S fails | `F ≡ 2c` (so `x(t+1) = 2c − x(t−1)`, every site independent, every orbit periodic) has periodic orbits with excursions. A proof of S must use a property of `G(s) = ⌊(s+1)/3⌋` that this rule lacks, and must name the step where it does |
| P3-K2 | countercontrol: the vacuum | at `c = 0` the residue of `−1` is outside `[c−1, c+1]` (MQ, scope note). Any statement for `c = 0` is made separately |
| P3-K3 | consistency with known orbits | the ternary singletons (period 4, no excursion) must not be excluded by the argument |
| P3-K4 | exact sanity checks, if authorized | the base cases the argument asserts (e.g. the first ticks of the S1 seeds) are checked by exact runs before the proof is called complete |
| P3-K5 | pressure test (§A.31) | a refutation is favourable to the framework, since it supplies an ingredient for the missing block, so it gets maximum skepticism: exact certificate, an independent re-run, and a check that the excursion is real, i.e. that the out-of-range value sits on the boundary layer of the instantaneous closed hull |

## 5. Invariant → checkpoint (§A.41)

| Invariant asserted | Checkpoint that measures it |
|---|---|
| The statement precedes the attempt | this file's commit is an ancestor of the first P3 derivation commit, which changes nothing in `plans/` |
| The scope is as stated (`q = 2^16`, `d = 3`, uniform `c`, finite perturbations) | the P3 record restates the scope on every theorem; the reviewer checks it |
| Only the lemmas of §3 are imported | each step cites its lemma; the reviewer checks the list |
| The countercontrol is met | the record names the step that fails for `F ≡ 2c` (P3-K1) |
| No computation is run without authorization | P3-K4 runs only after a recorded authorization |

## 6. Cost class (§A.40)

Local and paper only. The exact base-case checks of P3-K4, if authorized, are bounded local checks.

## 7. What P3 would and would not establish

- **Would:**
  - *If S holds at a stage:* on uniform backgrounds no finite gadget of that stage has a
    non-spreading excursion. Combined with MQ2, a controlled transfer on a uniform background would
    then need infinite components, such as lines, whose junction boundary never breaches. That
    sharpens U1's missing block for this class.
  - *If S fails:* an explicit non-spreading excursion, a candidate ingredient for step 2.
- **Would not:**
  - non-universality of Q, since non-uniform backgrounds, infinite configurations and signals on
    lines remain;
  - any statement about other `q` unless the proof is uniform in `q`;
  - any statement about other rules sharing the update form.

## 8. Literature used

- Vivaldi and co-workers on rounded rotations `x_{t+1} = ⌊λ x_t⌋ − x_{t−1}` [abstract level]: the
  zero-dimensional analogue of the rounding. Periodicity of all orbits for `|λ| < 2` is conjectured
  and proved only for a few `λ`. Background for why bounded orbits of rounded maps are hard to
  classify; it is not a lemma here.
- Damage spreading in cellular automata [from memory, background only]: no result is imported.
