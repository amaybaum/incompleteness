## Re-review of PR #957 at `806b57dc` (three commits since `b25dcfc4`): ACCEPT WITH CHANGES

The foliation premise is resolved correctly, the second case under the owner's rule applies, and I agree with leaving GR unchanged. My earlier findings 1–3 and 5–8 are applied correctly, and the writer's four departures are acceptable. Three new required items remain:
- the new corollary turns SM's "only if" for the condensate into "when";
- SM :1418 states the now-conditional selection as "the fact";
- Main :668 restates "with no boosts" without the hypothesis.

Setup: 23 GB free. I worked in a fresh detached worktree at `806b57dc` and removed it afterwards. Line numbers below refer to `806b57dc`.

### (c) Foliation premise and GR
**1. No definition or theorem gives foliation preservation, so the second case holds.** I searched Main, GR, SM and Substratum for foliation, simultaneity, H-frame, preferred frame, frame transformation, O(3,1) and Lorentz group.
- **Main:**
  - :660 is the only place the foliation is introduced.
  - Main never defines an O(3,1) action on T, so "Λ leaves T invariant" has no definition from which preservation could follow.
  - :72 says the horizon realization "is nowhere consumed by a proof here".
- **GR:**
  - S1 (:665) is only "a partition V at a causal horizon".
  - H-frame (:88, :470) concerns *which* foliation the substrate's preferred foliation is (the comoving one), not T's invariances, and it is itself open ("S1–S4 do not supply and [SM] states is not derived").
  - H-Hawking (i) (:653) presupposes a preferred microscopic frame and does not establish the lemma's hypothesis.
- **SM:** :130 (ii) gives the *lattice dynamics* a preferred frame. That is about φ, not about T's invariance group.

The hypothesis is therefore needed, and it is now explicit: "let T determine this foliation, so that any Λ leaving T invariant maps the foliation to itself". The boost exclusion now reads "Consequently, under this hypothesis, boosts…". This makes explicit a step the proof already used; it is not a new physical assumption added to rescue anything. The ledger's `assumptions` field records it.

Optional: since no action is defined, the hypothesis is only as precise as the unstated action of O(3,1) on T. One clause naming the intended action would close this, for example action on the spacetime increments of the step laws, as in the kernel.

**2. The GR pushback is correct: no GR conclusion depends on the boost exclusion.**
- GR :641, :653, ch07 :57 and appendix-b :209 need the opposite property: *emergent local boost invariance* at the horizon for the KMS and Euclidean-regularity step.
  - :641 cites [Main §3.5] only to name "the framework's Lorentz-sector item in the boost channel".
  - :653 cites it only to identify the velocity-splitting core with "the open Lorentz-sector boost item".
- The preferred frame GR uses comes from the lattice (SM :130 (ii); H-Hawking (i)), not from the lemma.
- If the hypothesis failed and T were boost-invariant, none of GR's conditionals would gain or lose a premise. GR needs no qualification.

**On the tension:** Main's boost exclusion (the map selects a frame) and GR's need for emergent infrared local boost invariance do not contradict each other.
- A frame selected by the map, or by the lattice, is compatible with dynamics that become boost-invariant in the infrared.
- The corpus already names this as the open boost-sector item: SM :130 (ii) ("boost invariance can hold only as an emergent infrared property"), GR :641 ("inherited, not established"), and Main :664 (boost-sector violation "exposed to … the local-boost-invariance prerequisite").
- So the tension is acknowledged, not hidden. No sentence states the reconciliation outright; an optional clause in the corollary could.

### Findings
**1. Main.md:664, new corollary text (required).**
- **Current:** "…and the effective operator is $O_h$-invariant when the condensate is $O_h$-equivariant ([SM §3.1])."
- **Problem:** This turns a necessary condition into a sufficient one, and it uses the wrong group.
  - SM :136 says "The effective operator is octahedral-invariant **only if** the condensate Σ is".
  - What SM gives in the other direction is only that "an equivariant condensate leaves the $E_g$ channel exactly null".
  - SM's condensate condition is $O$-equivariance (Theorem 5, :338), not $O_h$.
- **Proposed:** "…and, since the condensate breaks a symmetry of the dynamics, the effective operator is octahedral-invariant only if the condensate is $O$-equivariant, an alignment the block–link identification secures and which leaves the $E_g$ channel exactly null ([SM §3.1])."
- The all-orders clause before it matches SM :136 exactly.

**2. SM.md:1418 (required, §A.25 dependent).**
- **Current:** "…via the fact that the observation map selects a timelike direction but no spatial one."
- **Problem:** That the map carries n is now the lemma's hypothesis, so "fact" states as unconditional something that is now conditional.
- **Proposed:** "…via its result that, when the observation map determines the horizon foliation, the map selects a timelike direction but no spatial one."

**3. Main.md:668 (required, small).**
- **Current:** "what it leaves invariant (its symmetry: contained in the transformations preserving the line $\mathbb{R}n$, with no boosts)".
- **Problem:** This restates the boost exclusion without the hypothesis, while :670 is qualified.
- **Proposed:** "(its symmetry, under the lemma's hypothesis: contained in … with no boosts)".

**4. ch19:246 and FULL:5406 (recommended).**
- **Current:** "The rest-frame-selection lemma (the map selects a timelike direction, no spatial one)".
- **Problem:** This is the same unconditional reading. :240 of the same section is qualified.
- **Proposed:** "(given that the map determines the horizon foliation, it selects a timelike direction, no spatial one)". Mirror the change in FULL.

**5. Main.md:664, corollary premise (optional).** "the emergent theory inherits from the partition a physical rest frame" relies on T carrying n, which is the new hypothesis. A corollary inherits its lemma's hypotheses, and the ledger records it so, but an opening "Under the lemma's hypothesis," would make this visible.

**6. Two phrasings of the premise (optional).**
- Main :256, SM :136 and ch19 :248 use "a partition defined on the slices of the (horizon / a fixed simultaneity) foliation".
- Main :660, :670, Substratum :329 and ch19 :240 use "T determines the foliation".
- Both are right in their contexts: factorization-breaking is about the partition, invariance is about T. But :256 and SM :136 cite §3.5 for a condition §3.5 does not state in that form. Suggest "(the condition under which the §3.5 lemma excludes boosts)" or similar.

### Earlier findings and the writer's departures (task 4)
- **F1 (:666):** applied exactly.
- **F2 (ch19 :240/:242 and FULL mirrors):** applied.
- **F3 (:660 and the corollary):** applied ("not fixed by $n$; it depends on the substratum dynamics and on the lattice geometry of the partition").
- **F5 (Substratum):** "compatible with it" is accurate. Dropping my gloss loses nothing.
- **F6:** applied, but with the error in Finding 1.
- **F7:** applied, including "selects $n$", "nonzero" and the "combined with the lemma…" strengthening.
- **F7, dropped "its converse fails":** acceptable, since the cubic-kernel sentence that follows supplies the witness.
- **F8:** the heading, "honest" and "tempting" are gone. The C2 "same feature" identification was removed, and nothing else in the corpus depended on it.
- **Substratum "the partition's rest-frame data":** matches my proposal.
- **ch19 :246 left unchanged:** this is now Finding 4.

### Mirrors, ledger, artifacts, gate (task 5)
- **Mirrors:** ch19 :240/:242/:246/:248 and FULL :5400/:5402/:5406/:5408 are byte-identical.
- **Ledger:** the fingerprints match the census. `MAIN:L-rest-frame-selection` is `990927d001224c55` at :660, with assumptions extended by "T determines the horizon's simultaneity foliation". `MAIN:C-boost-rotation-inequivalence` is `177c3af33db4c623` at :664.
- **.tex:** regenerated with the build.sh recipe (with the source-sha256 footer), Main, SM, Substratum and FULL `.tex` are byte-identical to the committed files.
- **PDFs:** they contain the new text. Page counts are 96, 146, 53 and 557.
- **Gate:** every step passes except `lean-axioms`, which fails because lake is missing locally, as expected.
- **Voice:** the §A.32/§A.33 scan of all words added since the base finds no hits.

### Owner questions
**(a) Is every claim supported?** Yes, apart from Findings 1–3: one necessary→sufficient inversion with the wrong group, and two sites that state the conditional selection or boost exclusion unconditionally.

**(b) Is any result unnecessarily weakened?** No. The boost exclusion is conditional only because no definition supplies the premise (item 1 under (c)). The ± form remains justified (Substratum §5.4 :359; GR :68–70). The corollary now states the SM §3.1 all-orders result instead of "only at tree level".

**(c) Is the foliation premise correctly resolved, and is GR correctly handled?** Yes on both counts. The second case holds: no existing definition gives preservation, and GR does not establish the hypothesis, since H-frame is a different and open condition. GR needs no qualification because none of its conclusions uses the boost exclusion. The map-versus-emergent-boost tension is already named as the open boost-sector item.
