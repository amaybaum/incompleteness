# Independent review, round 3: A1 amendment proposal r3

**Reviewer and scope.** Non-author reviewer, 2026-11-24. The review is paper-only.

- Nothing was written in the repository. GitHub was not read in this round; only local git objects were used.
- P's checkers and the repository tools ran only on copies under `review-r3/`.

**Inputs verified.**

- `MANIFEST.sha256` passes.
- PROPOSAL-r3 is `64157a76…b773`, CHANGE-INVENTORY-r3 is `f355e2e9…cae5`, CHANGES-r2-to-r3 is `5d06e1e9…6c42`.
- review-r2 is `90178732…c522`.

## Verdict: REJECT, on one clause of D402

The clause is "$1/\alpha_0$ is the Brillouin-zone integral over $\mathbb{Z}^3$". Everything else in r3 is accepted:

- R2-B1's structure is fixed.
- D403 and D410–D412 are correct.
- The §32.9 corrections are in place.
- O-13 is stated.
- The mechanics, the configuration digests and every check reproduce.

The fix is one clause, applied in three places. It changes only the 1/α₀ wording of D402, §32.9 and the proposal.

## Blocking finding

### R3-B1. D402 misdescribes the 1/α₀ computation: the integral is not "over ℤ³"

r3 replaced the r2 wording "the infinite-lattice Brillouin-zone integral" with "$1/\alpha_0$ is the Brillouin-zone
integral over $\mathbb{Z}^3$ of §6.1". This is wrong in two ways, both stated facts in SM §6.1 at H and T1′:

- **The integral is four-dimensional.** SM:689 says the loop integration $\int d^4q$ and the lattice propagator
  $D(q)=\sum_\nu \sin^2(q_\nu)+m^2$ "run over four directions (consistent with the substratum's 3+1D Lorentzian
  structure)". Only the vertex factors are spatial. The integral is a hybrid over the four-direction lattice Brillouin
  zone, not over ℤ³.
- **1/α₀ is not the integral.** It is computed from it: $1/\alpha_0 = 6\times\Pi_s(0)\times 4\pi$ (SM:685), where
  $\Pi_s(0)$ is the lattice momentum integral (SM:683).

The r2 wording was accurate and also passes P's infinity scan. I ran P's `INF` regex. "infinite-lattice", with the
hyphen, does not match; only "infinite lattice", with a space, does. So the stated reason for the change is mistaken.

**Smallest fix.** Use the replacement clause below. I checked it against P's `INF` pattern, and it does not match.

> … and $1/\alpha_0$ is computed from the lattice momentum integral of §6.1 over the whole Brillouin zone, whose
> counterpart for a finite substratum and whose normalization of the vertex coupling are not established.

Apply the same correction in §32.9's 1/α₀ table row and open-dependency item 4, and in PROPOSAL-r3 §2. Rebuild the
ledger, the pins, the configuration digests and SM.tex.

## Focus 1: R2-B1. Resolved apart from R3-B1

The new SM:1394, rebuilt from H and the r3 ledger, is in `work/SM-proposed.md`, line 1394.

- **No single common sufficient condition.** "they rest on … each entry under the further conditions of the theorems
  cited for it" states dependencies, not sufficiency.
- **The open dependencies are visible in SM:1394 itself:**
  - the measure conditions of Lemma 1c and Proposition 4b;
  - the continuum conditions of the d = 3 selection;
  - for 1/α₀, the finite-substratum counterpart and the normalization of the vertex coupling.
- **No independence from A1 is implied where a dependency is open.** "whether an entry requires finiteness of the
  substratum is not established where …" leaves every open case open. For the entries whose cited proofs use none of
  these conditions, my r2 trace found no use of finiteness at the proof steps:
  - Theorem 7 is character theory (kernel-checked).
  - Theorem 8 is corner combinatorics (kernel-checked).
  - Theorem 15 is anomaly algebra.
  - Theorem 11 takes the Higgs doublet as input.
- **Most entries remain qualified anyway.** The d = 3 continuum clause applies to every entry that rests on the cubic
  d = 3 lattice, which is nearly all of them. The sentence therefore stays weak rather than strong.

**The writer's three adjustments to my wording.**

- "theorems" in place of "theorem": correct.
- Adding the vertex-coupling normalization to the 1/α₀ clause: correct and an improvement.
- "over ℤ³": incorrect (R3-B1).

## Focus 2: D410, D411, D412. Each is correct, complete and meaning-preserving

I checked each against the cited lines at H and T1′.

**D410.** It adds "spin-1/2 sectors under H-spin', Theorems 9–10; … light-spectrum selection, Theorem 10".

- Theorem 10 (:456) reads the three sectors as spin-1/2 SM generations "under H-spin'".
- Its proof (:460) names the flagged inputs: H-spin′, H-χ′ and light-spectrum selection. :458 repeats this.
- O-12 is resolved. Nothing is overstated.

**D411.** It adds "given the observed family pattern in the five representations per family, family-universal charges
and chirality under H-χ' (Theorem 15; …)".

- Theorem 15 (:589) assumes SU(3)×SU(2)×U(1), the five representations and family-universal charges.
- :460 and :555 add the observed family pattern and H-χ′.
- The uniqueness qualifiers of Theorem 15 (overall normalization, Y_u ↔ Y_d fixed by Q_em) were not in the entry at H
  either. Leaving them out changes nothing.

**D412.** It adds "whose reduction from the stabilizer U(3) × U(2) × U(1) of Theorem 5 carries the
amplitude-scale-gauge and background-independence premises of §4.6, a specified charged matter action and the further
physical input of Proposition 14a (§4.9)".

- Theorem 5 (:340) gives U(3)×U(2)×U(1).
- :344 says the reduction "carries the separate amplitude-scale-gauge/background-independence premises discussed in
  §4.6 and a specified charged matter action". :374 says the same.
- Proposition 14a is in §4.9 (:573, :579), and :585 says "the other circle and the charged action remain additional
  physical input".
- D412 is necessary, since the entry claims the Standard-Model group. It is accurate and overstates nothing.
- "background-independence premises" is SM's own term for A6's role here.

**Nothing missing that I could find.** The H-link, H-cust and Tier-2 framing is unchanged.

## Focus 3: D403. Correct per GR

GR:88 at T1′ lists:

- H-count, including finiteness of the total system and the conserved energy shell (§2.3);
- H-slope on identified transitions;
- H-frame;
- the relevant H-Hawking horizon and frame conditions (§8.5);
- local boost structure;
- the symmetric detailed-balance rate ratio;
- "Selection of the physical slope remains an additional condition."

D403 now carries all of them. Optional nit: "on identified transitions" after H-slope. The text does not match P's
`PTR` pattern.

## Focus 4: §32.9

- **The false sentence is removed.** "The wording" now says that D402 replaces the count by a reference, states no
  condition sufficient for every entry, and gives the open points in the sentence.
- **The six open dependencies agree in content** with PROPOSAL-r3 §2. The wording differs slightly; "identical" is
  true of the content.
- **Each item is correct:**
  1. Proposition 4b: finite representative or H-blind (:334).
  2. Lemma 1c: three alternatives including H-μ(φ,Θ) on ℤ^d (:252), and not used by the generation count.
  3. The d = 3 continuum conditions.
  4. The finite counterpart of the integral. This item carries R3-B1's "over ℤ³" and must change with it.
  5. The vertex normalization.
  6. A6. This one is weakly phrased but correct.
- **The O-13 placeholder is stated correctly.** It quotes the adopting decision and says expressly that it supersedes
  c.7093128173's clause, for these edits. The preamble is reworded to match, and §32.8 lists the decision as missing.

## Focus 5: mechanics, all reproduced independently in `review-r3/sb`

**Rebuild.**

- `edits.json`: P's edits round-trip exactly, plus `diffs-r3/new-edit-records-D402-D412.json`. 412 records, sha256
  `1adaadb9…1778`, equal to the writer's.
- `preserve_check --build-ledger`: 410 splices in 44 files, sha256 `afbd4d00…3fbd`, equal to the writer's.

**Ledger comparison.**

- P's 399 splices are byte-identical.
- The 11 new splices equal the writer's `LEDGER-new-splices`.
- Each new old-string occurs exactly once at H.
- No two splices overlap in any file. D412 ends at 405724 and D410 starts at 405725.
- The `files` entries change only for SM, ch09, ch19 and FULL.

**P's checkers.** Exit 0 or PASS on each:

- `--static`;
- `--simulate` (residual 5, all allowed);
- `--pins` (412 unique);
- `--repo-scan --simulate --final` (0 unexplained);
- both `--self-test` runs;
- `--verify-ledger` (re-derived identically; pin findings 0 with §32.10).

**PREREG.** It is a pure append. Both pin parsers read 6 equal rows from §32.10, the last of 13 `Record pins`
headings. `duplicate_check` reports OK.

**Configuration.** `adapters.ledger` and the `edits` companion now pin `afbd4d00…` and `1adaadb9…`, so the r2 defect is
fixed. The file parses as JSON. `w1-w2-allow-v2` is unchanged from r2.

**Item 7 as frozen** (`item7.py`, my own implementation, on H plus the r3 ledger):

- The pointer grep finds the 4 "(A1)" false-positive lines.
- The count grep finds 0 lines.
- Result: **PASS**.
- Negative controls NC1–NC5 (the SM:1394 phrase, ch09:137's count, "Fourteen items", a bare A1 pointer, "sixth of")
  each **FAIL** as required.
- The script's tree label still says "407 splices" from r2; it actually ran on the 410-splice ledger.

**Gate tools on H plus D402–D412.**

- `coverage_check`, `claims_check`, `voice_check`, `citation_roles_check`, `dependency_label_check` and
  `baseline_label_check` give the same output as at H. `citation_roles_check` exits 2 at H as well.
- `staleness_check` reports STALE for SM and book. This is expected until the TeX is regenerated.

**TeX.** The diffs against T1′ are confined to the SM:1394 paragraph and the FULL paragraphs, plus the stamps. The
stamps equal the rebuilt sources: SM `d7a9e552…` and FULL `9f419aae…`.

## Focus 6: r2 nits

All are applied:

- the FULL-mirror clause in row 7;
- the caveat on `main` blobs in §32.7;
- H-Hawking and the slope selection;
- Lemma 1c's ℤ^d alternative and Proposition 4b's H-blind route;
- Theorem 8b removed from the generations row;
- the authorization placeholder;
- the coverage and gate tools run.

**New item:** only R3-B1. No scope creep: D410–D412 lie inside the SM:1394 sentence that option (c) covers.

## What I re-ran

Every hash, ledger and checker result in Focus 5 was reproduced by computation. I also reproduced the item-7 controls,
the gate tools and the TeX stamps, and tested the proposed wordings against P's infinity scan.

The science of D410–D412 and D403 was verified by reading the cited lines (SM :340–344, :374, :456–460, :555,
:573–589, :683–689; GR:88). guards_check and SC-42 were not run; they are gate items.

## Files (`review-r3/`)

- `review.md`
- `item7.py` and `item7.out`
- `ledger_cmp.out`
- `build-ledger.out`, `static.out`, `simulate.out`, `pins.out`, `reposcan.out`, `verify-ledger.out`, `selftest-*.out`
  and `rc.out`
- `pins_check.out`
- `gate_tools.out` and `*_tree.out`
- `sb/` and `work/`

`tree/` and `tmp/` are scratch and are not in the manifest.
