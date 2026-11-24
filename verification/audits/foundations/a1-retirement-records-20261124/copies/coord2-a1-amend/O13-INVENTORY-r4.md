# O-13 inventory, r4: every scientific conclusion changed by D402–D412

**Status.** This inventory is paper-only and provisional, and it authorizes nothing. It is prepared for the owner's O-13
decision. The owner's request was quoted on 2026-11-24 (`amaybaum`, relayed in session): "prepare a prediction-by-prediction
inventory of every scientific conclusion changed by D402–D412 … Confirm that no scientific claim is strengthened
without supporting evidence." Also: "'no use of A1 found' must not become 'proved independent of A1.'"

Line citations are to `papers/SM.md` at H (`53c6601a`) unless another file is named. The verbatim old and new texts,
with their byte hashes, are in Appendix A.

**The five categories, as the owner listed them:**

| Code | Category |
|---|---|
| **E** | an explicitly stated existing dependency: a condition the manuscript already states in the derivation cited, now stated at the entry |
| **N** | a narrowed claim |
| **H** | a previously unstated hypothesis: a condition SM:1394 did not state for the entry |
| **A1** | a conclusion whose existing derivation requires A1 |
| **U** | an unresolved dependency |

A change may fall into several categories, or, where it changes no scientific conclusion, into none.

## 1. Inventory, prediction by prediction

| Prediction (SM:1394) | Edit(s) | Old at H → new (summary; verbatim in Appendix A) | Categories | Supporting lines at H | Strengthened? |
|---|---|---|---|---|---|
| Frame sentence, all entries | D402 | "they hold for every bijection satisfying the six structural properties." → they rest on §2.3's construction and cubic-group representation theory, each entry under the further conditions of the theorems cited for it; whether an entry requires finiteness of the substratum is not established where those theorems use Lemma 1c's or Proposition 4b's measure conditions or the d = 3 continuum conditions; 1/α₀ is computed from the lattice momentum integral of §6.1 over the whole Brillouin zone, and its finite-substratum counterpart and vertex normalization are not established | E, N, U | §2.3 dependency statement :60; Lemma 1c :252; Proposition 4b :334; Corollary :208–210; §6.1 :683–689 | **No.** The old sentence gave no referent for "the six structural properties" (independent reading: ambiguous). The new sentence asserts no common sufficient condition. Where it is not established whether an entry needs finiteness, it says so. It does not say any entry holds without A1. The equivalence class [(S, φ)]/G_sub and "do not depend on which specific φ" are unchanged. |
| SU(3) × SU(2) × U(1), multiplicities (3, 2, 1) | D412; D402 | "…(3, 2, 1)," → "…(3, 2, 1), whose reduction from the stabilizer U(3) × U(2) × U(1) of Theorem 5 carries the amplitude-scale-gauge and background-independence premises of §4.6, a specified charged matter action and the further physical input of Proposition 14a (§4.9)," | E, N, H, U | Theorem 5 :340, :344; Theorem 7 :374; Proposition 14a scope :585. U: H-cust's kinetic clause via Proposition 4b (:334, finite representative or H-blind); d = 3 continuum conditions :208–210 | **No.** It adds conditions only. No use of A1 was found in Theorem 7 (kernel-checked representation theory) or Theorem 5 (Schur). That is not a proof of independence from A1, and D402 keeps the open measure and continuum conditions visible. |
| Three generations, identical gauge quantum numbers | D410; D402 | "three generations (chirality conditional on H-χ', §4.8)" → "three generations (spin-1/2 sectors under H-spin', Theorems 9–10; chirality conditional on H-χ', §4.8; light-spectrum selection, Theorem 10)" | E, N, H, U | Theorem 9 :448; Theorem 10 :456, proof :460 ("flagged inputs (H-spin' …; H-χ' …; light-spectrum selection)"); Theorem 13 :543. U: d = 3 continuum conditions :208–210 | **No.** It adds conditions only. No use of A1 was found in Theorems 2, 8, 10 (ii) or 13; the reviewed Q1 record finds they hold on ℤ³ without A4's finite clause. That is not a proof of independence from A1. |
| One Higgs doublet | none (D402 frame only) | unchanged entry text | E | Theorem 11 :464–468 ("taken as phenomenological input") | **No.** The entry is unchanged and remains an input. |
| Unique hypercharges (Y_Q ≠ 0) | D411; D402 | "unique hypercharges from anomaly cancellation (apart from the exceptional branch $Y_Q=0$)" → "…, given the observed family pattern in the five representations per family, family-universal charges and chirality under H-χ' (Theorem 15; apart from the exceptional branch $Y_Q=0$)" | E, N, H | Theorem 15 :589; Theorem 10 proof :460 ("given … the observed family pattern"); :555 | **No.** It adds conditions only. No use of A1 was found in the anomaly algebra. That is not a proof of independence. |
| 1/α₀ = 23.25 | D402 (clause) | entry unchanged; D402 states that 1/α₀ is computed from the lattice momentum integral of §6.1 over the whole Brillouin zone, and that its counterpart for a finite substratum and the normalization of its vertex coupling are not established | E, N, U | §6.1 :681–689 (1/α₀ = 6 × Π_s(0) × 4π; ∫d⁴q and the lattice propagator over four directions, spatial vertex factors, :689) | **No.** The value is unchanged. The added clause marks two open points and asserts nothing new. |
| Action scale ħ = c³ε²/(4Gσ) | D403 | "hold for the same class as consistency relations conditional on H-slope ([GR §3.2, §4–§5])" → "…conditional on H-count, which includes finiteness of the total system and a conserved energy shell, and on H-slope on identified transitions, H-frame, the H-Hawking horizon and frame conditions, local boost structure and the symmetric detailed-balance rate ratio, with selection of the physical slope an additional condition ([GR §2.3, §3.2, §4–§5, §8.5])" | E, N, H, A1, U | `papers/GR.md` :58 (H-count: "Under A1, restrict the finite total system to a conserved energy shell"); :88 ("requires H-count, including A1 and the conserved energy shell (§2.3), H-slope on identified transitions, H-frame, the relevant H-Hawking horizon and frame conditions (§8.5), local boost structure and the symmetric detailed-balance rate ratio … Selection of the physical slope remains an additional condition") | **No.** It adds GR's own conditions, so it narrows the claim. The A1 dependence is now stated: finiteness of the total system. U: the selection of the physical slope stays an open additional condition. |
| Bekenstein-Hawking coefficient 1/4 | D403 | as for ħ: "…and the Bekenstein-Hawking coefficient it matches hold…" carries the same conditions | E, N, H, A1, U | GR :312–316 (the 1/4 is "recovered, under the conditions of the §3 calibration"); :88 | **No**, as for ħ |
| Book: ch09:137 and FULL:2552 (Tier 2 sentence) | D404, D405 | "the six structural properties developed in Chapter 5 (" → "the structural properties developed in Chapter 5 (" | none: no scientific conclusion changes | the list in the same sentence; ch09:36 | **No.** The set and its six members are unchanged; only the bare count word goes. |
| Book: ch19:198 and FULL:5268 (inflation remark) | D406, D407 | "(one of the framework's six structural properties of the bijection)" → "(one of the framework's structural properties of the bijection: isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count)" | none: no scientific conclusion changes. The set is named from ch09:36. | ch09:36 and :137 (the same six); isotropy is a member | **No.** Same set, named explicitly. |
| Book: ch19:212 and FULL:5282 ("further narrow it") | D408, D409 | "The framework's six structural properties of the bijection (developed across Chapters 5-7) further narrow it." → "…structural properties of the bijection (isotropy, …, generation count; developed across Chapters 5-7) further narrow it." | none: no scientific conclusion changes | ch09:36, :137; ch19:212 at H lists A1 apart from these properties | **No.** Same set, named explicitly. Owner decision: option A. |

**Not touched by D402–D412.** Every other sentence of SM and of the book; the 399 ledger splices D001–D401; and every
other scientific conclusion of the corpus.

## 2. Confirmations

- **No claim is strengthened without supporting evidence.**
  - Each edit either adds conditions that the cited derivation already uses (E/H, a narrowing), or names a set the same
    corpus already enumerates (the book edits), or marks open dependencies (U).
  - No edit removes a condition from an entry, enlarges a class or adds a prediction.
- **"No use of A1 found" is not "proved independent of A1".**
  - The new texts contain no statement that an entry holds without A1 or without finiteness. D402 says whether an
    entry requires finiteness "is not established" wherever an open condition enters.
  - §32.9 (r4) records the trace as "No use of A1 found in the cited derivation(s)". It adds: "No use of A1 found"
    records the result of reading the cited derivations; it is not a statement that an entry holds independently of
    A1.
  - The new texts, §32.9 and this inventory were checked for "independent of A1", "without finiteness" and "proved
    without". None occurs except in this negating sentence and in the owner's quotation.
- **Conclusions whose existing derivations require A1.** The action scale and the Bekenstein-Hawking 1/4, through
  H-count's finite total system (GR:58, GR:88). D403 states this at SM:1394.
- **Unresolved dependencies, all six stated in §32.9:**
  1. H-cust via Proposition 4b;
  2. Lemma 1c's measure, including the H-μ(φ,Θ) alternative on ℤ^d;
  3. the d = 3 continuum conditions;
  4. the finite-substratum counterpart of the lattice momentum integral of §6.1;
  5. the vertex normalization for 1/α₀;
  6. A6's role beyond the gauge entry.
## Appendix A. The edits, verbatim (old text at H, new text), with their splice hashes

Each `old_sha256` is the sha256 of the old bytes at H at the stated byte span. Each `new_sha256` is the sha256 of the new bytes. Both come from the r4 ledger.

### D402: `papers/SM.md`, site papers/SM.md:1394, part 1

- span at H: bytes 405504–405575
- old_sha256: `227117bc96e597894158fe4ba53ceb3b0c426e3a7f6ed5f414698db95e08d3c6`
- new_sha256: `c46d5981668cd855168395667e9ed51cf12fa62295e3addedc1a6d50b5a071d9`

Old:

> they hold for every bijection satisfying the six structural properties.

New:

> they rest on the local spatial/gauge construction of §2.3 and on cubic-group representation theory, each entry under the further conditions of the theorems cited for it; whether an entry requires finiteness of the substratum is not established where those theorems use the measure conditions of Lemma 1c or Proposition 4b or the continuum conditions of the $d = 3$ selection (§3.2), and $1/\alpha_0$ is computed from the lattice momentum integral of §6.1 over the whole Brillouin zone, whose counterpart for a finite substratum and whose normalization of the vertex coupling are not established.

### D403: `papers/SM.md`, site papers/SM.md:1394, part 2

- span at H: bytes 406304–406399
- old_sha256: `13d29b79536f017b85ed3a098ed71fa523cb869b86e71e16be06a68c6edd2d7c`
- new_sha256: `9b4e94b118f933c8f6bbfa5e0a3b24f7f83c9e0ebcd62a288a90dffde9b5f230`

Old:

> hold for the same class as consistency relations conditional on H-slope ([GR §3.2, §4–§5])

New:

> hold for the same class as consistency relations conditional on H-count, which includes finiteness of the total system and a conserved energy shell, and on H-slope on identified transitions, H-frame, the H-Hawking horizon and frame conditions, local boost structure and the symmetric detailed-balance rate ratio, with selection of the physical slope an additional condition ([GR §2.3, §3.2, §4–§5, §8.5])

### D404: `book/ch09-universality.md`, site book/ch09-universality.md:137, part 1

- span at H: bytes 26169–26223
- old_sha256: `8eb676bc135a4dcb4b48b654894ca36f5a0e24c1e09f5596c4f7267d37bd6284`
- new_sha256: `b88d10778c8dc87370c5109a846d07d232116e735db5432e4dd2490b49df88fe`

Old:

> the six structural properties developed in Chapter 5 (

New:

> the structural properties developed in Chapter 5 (

### D405: `book/The-Incompleteness-of-Observation-FULL.md`, site book/ch09-universality.md:137, part 1, mirror of book/ch09-universality.md:137

- span at H: bytes 621142–621196
- old_sha256: `8eb676bc135a4dcb4b48b654894ca36f5a0e24c1e09f5596c4f7267d37bd6284`
- new_sha256: `b88d10778c8dc87370c5109a846d07d232116e735db5432e4dd2490b49df88fe`

Old:

> the six structural properties developed in Chapter 5 (

New:

> the structural properties developed in Chapter 5 (

### D406: `book/ch19-open-problems.md`, site book/ch19-open-problems.md:198, part 1

- span at H: bytes 49287–49354
- old_sha256: `9890b8e5e5101e09af0a8f72f9575321c2892d16bbb8511b3707783dcaa19d68`
- new_sha256: `4ddee078457fb2cc5cfcef75b2b0a52036b7483fc0124a40c9e5b0aae4e1cc9b`

Old:

> (one of the framework's six structural properties of the bijection)

New:

> (one of the framework's structural properties of the bijection: isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count)

### D407: `book/The-Incompleteness-of-Observation-FULL.md`, site book/ch19-open-problems.md:198, part 1, mirror of book/ch19-open-problems.md:198

- span at H: bytes 1092427–1092494
- old_sha256: `9890b8e5e5101e09af0a8f72f9575321c2892d16bbb8511b3707783dcaa19d68`
- new_sha256: `4ddee078457fb2cc5cfcef75b2b0a52036b7483fc0124a40c9e5b0aae4e1cc9b`

Old:

> (one of the framework's six structural properties of the bijection)

New:

> (one of the framework's structural properties of the bijection: isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count)

### D408: `book/ch19-open-problems.md`, site book/ch19-open-problems.md:212, part 2

- span at H: bytes 51720–51829
- old_sha256: `085a5e05d6e02f7ce357fd0bef703c27fab50937c99b261c7c6269f8066a8c6d`
- new_sha256: `2ba6e306addc5776dbe65b83c8a98386134502ff8262d8b24c77bd9319c6980b`

Old:

> The framework's six structural properties of the bijection (developed across Chapters 5-7) further narrow it.

New:

> The framework's structural properties of the bijection (isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count; developed across Chapters 5-7) further narrow it.

### D409: `book/The-Incompleteness-of-Observation-FULL.md`, site book/ch19-open-problems.md:212, part 2, mirror of book/ch19-open-problems.md:212

- span at H: bytes 1094860–1094969
- old_sha256: `085a5e05d6e02f7ce357fd0bef703c27fab50937c99b261c7c6269f8066a8c6d`
- new_sha256: `2ba6e306addc5776dbe65b83c8a98386134502ff8262d8b24c77bd9319c6980b`

Old:

> The framework's six structural properties of the bijection (developed across Chapters 5-7) further narrow it.

New:

> The framework's structural properties of the bijection (isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count; developed across Chapters 5-7) further narrow it.

### D410: `papers/SM.md`, site papers/SM.md:1394, part 3

- span at H: bytes 405725–405782
- old_sha256: `61aee339b7b5fd2258bc76da5f5536f9b7767d50d8d495da76839a2ac39e1a14`
- new_sha256: `60165e7ced64da66c2da633a41acb475290fa7a6429712c762c1f3d350bc0582`

Old:

> three generations (chirality conditional on H-χ', §4.8)

New:

> three generations (spin-1/2 sectors under H-spin', Theorems 9–10; chirality conditional on H-χ', §4.8; light-spectrum selection, Theorem 10)

### D411: `papers/SM.md`, site papers/SM.md:1394, part 4

- span at H: bytes 405940–406029
- old_sha256: `d19aeb52bf949a18fd801ae3981493a6bc7cc29e2c4b8058230f1676f811dfea`
- new_sha256: `ec826227c78a97aa02321a0f6bb751cd7b2be4c2fce018c3802407ce837591f9`

Old:

> unique hypercharges from anomaly cancellation (apart from the exceptional branch $Y_Q=0$)

New:

> unique hypercharges from anomaly cancellation, given the observed family pattern in the five representations per family, family-universal charges and chirality under H-χ' (Theorem 15; apart from the exceptional branch $Y_Q=0$)

### D412: `papers/SM.md`, site papers/SM.md:1394, part 5

- span at H: bytes 405671–405724
- old_sha256: `84248f693bafe923251c44979e5382f7d0f1a5cc0361f2e34cb99c85cb1875bc`
- new_sha256: `758c165782d84541bf4e4c2612d50adb5d3710da0c4949bccc5669b8d8e82210`

Old:

> SU(3) × SU(2) × U(1) with multiplicities (3, 2, 1),

New:

> SU(3) × SU(2) × U(1) with multiplicities (3, 2, 1), whose reduction from the stabilizer U(3) × U(2) × U(1) of Theorem 5 carries the amplitude-scale-gauge and background-independence premises of §4.6, a specified charged matter action and the further physical input of Proposition 14a (§4.9),

