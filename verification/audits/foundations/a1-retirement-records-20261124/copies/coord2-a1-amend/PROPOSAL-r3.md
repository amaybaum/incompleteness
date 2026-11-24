# A1 plan amendment proposal, revision 3

## 0. Status

**Paper-only.** This revision is paper-only and provisional, and it authorizes nothing. Everything in PROPOSAL-r2 §0
still applies: the inputs, the owner instructions of 2026-11-24, the dependency on tool design v6.0e, and the
boundaries. No repository file was changed. Every check ran on sandbox copies and scratch exports, read through
`git show` and `git archive`.

**What r3 answers.** It answers review r2 (`review-r2/review.md`, sha256
`901787327ba80afaee661c0f12e6f66854a163dae3859820ac8db1caa547c522`). That review rejected D402 and the SM:1394 entries
only (R2-B1). It accepted everything else, with nits. `CHANGES-r2-to-r3.md` maps each change. The r1 and r2 files are
unchanged.

**Independent review.** Still pending for r3. The science of D402, D403 and D410–D412 needs it most.

**The owner decision required at adoption.** The edits D402–D412 change manuscript statements by narrowing them. The
owner's 2026-11-24 instruction authorizes their preparation only. Adoption needs an owner decision that adopts
D402–D412. That decision must expressly supersede, for these edits, the clause of c.7093128173 that authorizes "No
change to the ledger base H …, the 399 ledgered splices or any scientific conclusion". §32.9 carries the placeholder
for that quotation.

## 1. What changes from r2

| Item | r3 |
|---|---|
| D402 (SM:1394, part 1) | It no longer asserts one common sufficient condition. In the sentence itself it states where it is not established whether an entry requires finiteness of the substratum. |
| D410, D411, D412 (new; SM:1394, parts 3–5) | Each entry now names the conditions its theorems use. Generations: H-spin′ and light-spectrum selection. Hypercharges: the family pattern, family-universal charges and H-χ′. Gauge group: the premises and inputs of the Standard-Model reduction. |
| D403 | adds H-Hawking and "selection of the physical slope" (GR:88) |
| §32.9 | Corrects the false sentence. The open-dependency list is now the same here and in §32.9. The generation row drops Lemma 1c. The ℤ^d alternative and the H-blind route are added. |
| Item 7 row | One clause: the FULL mirrors are false positives by the ledger's mirror convention (LEDGER.md:304) |
| §32.7 | Caveat: the side-change records pin today's `main` blobs |
| Authorization | The adoption decision must supersede c.7093128173's clause (§0) |
| Configuration | `adapters.ledger` and its `edits` companion pin the new `ledger.json` and `edits.json`. The writer found this: r2 left P's digests there. |
| Counts and pins | 412 edit records; 410 splices in 44 files. `edits.json` `1adaadb93769005bf8eb27ff82a8941359f82f20f395eeb61101a73f240f1778`; `ledger.json` `afbd4d00ce21c663bf34ef25841b1e5374372de2f70a82a835f6131693123fbd` |

These are unchanged from r2:

- item 7, kept exactly as frozen;
- D404–D409;
- ESC-1 to ESC-4, with v2 carrying W2-a and W2-b;
- B2, O-9, and arrangements A and C′;
- the side-change records;
- P1–P5 and P8;
- every other configuration field.

## 2. The SM:1394 edits (final texts)

Each old string is unique in `papers/SM.md` at H: build uniqueness was checked for 412 edits with 0 failures. The five
splices lie in one line and do not overlap.

| Id | Old (H) | New |
|---|---|---|
| D402 | "they hold for every bijection satisfying the six structural properties." | "they rest on the local spatial/gauge construction of §2.3 and on cubic-group representation theory, each entry under the further conditions of the theorems cited for it; whether an entry requires finiteness of the substratum is not established where those theorems use the measure conditions of Lemma 1c or Proposition 4b or the continuum conditions of the $d = 3$ selection (§3.2), and $1/\alpha_0$ is the Brillouin-zone integral over $\mathbb{Z}^3$ of §6.1, whose counterpart for a finite substratum and whose normalization of the vertex coupling are not established." |
| D403 | "hold for the same class as consistency relations conditional on H-slope ([GR §3.2, §4–§5])" | "hold for the same class as consistency relations conditional on H-count, which includes finiteness of the total system and a conserved energy shell, and on H-slope, H-frame, the H-Hawking horizon and frame conditions, local boost structure and the symmetric detailed-balance rate ratio, with selection of the physical slope an additional condition ([GR §2.3, §3.2, §4–§5, §8.5])" |
| D410 | "three generations (chirality conditional on H-χ', §4.8)" | "three generations (spin-1/2 sectors under H-spin', Theorems 9–10; chirality conditional on H-χ', §4.8; light-spectrum selection, Theorem 10)" |
| D411 | "unique hypercharges from anomaly cancellation (apart from the exceptional branch $Y_Q=0$)" | "unique hypercharges from anomaly cancellation, given the observed family pattern in the five representations per family, family-universal charges and chirality under H-χ' (Theorem 15; apart from the exceptional branch $Y_Q=0$)" |
| D412 | "SU(3) × SU(2) × U(1) with multiplicities (3, 2, 1)," | "SU(3) × SU(2) × U(1) with multiplicities (3, 2, 1), whose reduction from the stabilizer U(3) × U(2) × U(1) of Theorem 5 carries the amplitude-scale-gauge and background-independence premises of §4.6, a specified charged matter action and the further physical input of Proposition 14a (§4.9)," |

**The reviewer's proposed D402, quoted.** "they rest on the local spatial/gauge construction of §2.3 and on cubic-group
representation theory, each entry under the further conditions of the theorem cited for it; whether an entry requires
finiteness of the substratum is not established where that theorem uses the measure conditions of Lemma 1c or
Proposition 4b, the continuum conditions of the d = 3 selection (§3.2) or, for $1/\alpha_0$, the infinite-lattice
Brillouin-zone integral of §6.1."

**Adjustments to that text, each for accuracy:**

- "the theorem cited for it" becomes "the theorems cited for it", because an entry rests on several theorems.
- For 1/α₀, the open point is the converse: the stated value is the integral over ℤ³, and its finite-substratum
  counterpart is not computed. The normalization of the vertex coupling is also open, as the trace found. The
  sentence states both.
- "the infinite-lattice" is avoided. "infinite lattice" is a pattern of P's infinity scan, and "over $\mathbb{Z}^3$"
  says the same without it. `--static` gives 0 infinity hits.

**Whether D412 is necessary.** It is. The entry claims SU(3) × SU(2) × U(1). Theorem 5 yields U(3) × U(2) × U(1).
SM:344 and SM:374 state that the reduction to the Standard-Model group "carries the amplitude-scale-gauge and
background-independence premises … and a specified charged matter action". SM:585 states that the other circle and
the charged action "remain additional physical input". These are necessary conditions of the entry as stated. The
background-independence premise is A6, so this also settles A6's role for the gauge entry.

**Why D410 includes light-spectrum selection.** Theorem 10's proof (SM:460) lists it among "the flagged inputs" for
reading the three sectors as SM generations.

**The per-prediction dependencies.** The table, the A1 determination and the open-dependency list are in PREREG §32.9
(`diffs-r3/PREREG-append-s32-r3.diff`). PROPOSAL-r2 §3.3 is superseded where it differs. In summary:

- Gauge group, generations, Higgs, hypercharges, 1/α₀: no use of A1 found in their derivations, subject to the open
  dependencies below.
- The action scale and the 1/4: A1 is **used**, through H-count's finite total system.

**Open dependencies** (identical in §32.9):

1. H-cust's kinetic clause via Proposition 4b: the counting measure on a finite representative, or the H-blind
   extension.
2. Lemma 1c's measure: the finite-representative counting measure, a structured prior, or H-μ(φ,Θ) on ℤ^d. It enters
   only where a theorem used by an entry relies on Lemma 1c. The generation count does not.
3. The d = 3 continuum conditions.
4. The finite-substratum counterpart of 1/α₀'s integral over ℤ³.
5. The normalization of 1/α₀'s vertex coupling.
6. The role of A6, beyond the gauge entry, which D412 now covers, and §2.3's statement for the construction.

**Non-strengthening.**

- D410–D412 add conditions only.
- D403 adds conditions taken from GR:88.
- D402 removes the count, names no sufficient set, and states the open points in the sentence itself.
- No entry loses a condition or gains a class.

## 3. Checks (re-run for r3)

The sandbox and scripts are in `work-r3/` (`run_all.sh`, `gate_tools.sh`).

| Check | Result |
|---|---|
| `preserve_check --build-ledger` | 410 splices in 44 files. The 399 P splices are byte-equal. The 401 P edit records are unchanged. |
| `edits_check --static` | PASS (infinity, register, capitals and identifier 0; mirror parity 0; sitemap 194/194) |
| `--commit H --simulate` | PASS: 412 unique; residual 5 (all allowed); criterion-5 0; identifier and count 0 |
| `--pins` | PASS |
| `--repo-scan --simulate --final` | PASS, 0 unexplained |
| `edits_check --self-test`; `preserve_check --self-test` | PASS; PASS |
| `preserve_check --verify-ledger`; `--verify-pins` with the r3 PREREG | re-derived identically; pin findings 0, PASS |
| Item 7 as frozen, on H plus the r3 ledger | count grep 0 lines; pointer grep only the 4 false positives; **PASS** |
| Negative controls: "six structural assumptions", "Fourteen items, …", the SM:1394 phrase | each **FAIL** |
| `duplicate_check` on the 4 edited sources and on the r3 PREREG | OK; OK |
| Gate tools (coverage, claims, voice, citation_roles, dependency_label, baseline_label) on H and on H with only D402–D412 | identical output and exit status. coverage_check: 132 statements; the export includes `.github` |
| `staleness_check` | STALE for SM and the book with the edits, as expected until the TeX is regenerated |
| TeX rebuilt with P's recipe (the base control reproduces H) | SM.tex sha256 `0c7506337d2248297e47ee96373c76d6a79cb72f8c93017e27802c6abbc60107`; FULL.tex unchanged from r2 (`5d37cafc…`). Each differs from T1′ only in the edited paragraphs and the source stamp (`diffs-r3/*.tex.t1p-to-proposed.diff`). |
| PREREG r3 | a pure append; the last of 13 `Record pins` headings is §32.10, and both parsers read 6 rows |

**Not run:**

- `guards_check --predict` and `--mutants`, and the SC-42 regeneration. These are gate items.
- PDFs and CI.

## 4. Open questions for the owner

These are as in r2, with two changes.

- **O-12 is resolved.** H-spin′ is included as D410, under requirements 2, 5 and 7, as review r2 recommends. The owner
  confirms it in the adoption decision.
- **New O-13:** the adoption decision described in §0.
