# Review of LIT-REUSE r1 (first-hand reading of performed experiments that use one source twice)

**Reviewer:** Claude, independent, non-author. **Date:** 2026-11-15. **Scope:** paper-only. Primary texts
were opened first-hand (arXiv PDFs converted to text and read; Crossref and OpenAlex records for
bibliography). No computation, no repository edits, no posts.

**Object:** `LIT-REUSE-r1.md` on branch `research/ro1-sector-c-1169-20261114`, directory
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, read against
`S3-U3-r2.md` §§2.2, 4.1, 4.4, 5.1–5.2, 10.3, 10.7 and `RR1-REGISTER-BRIEF-r1.md` §§1, 4. The
authorizing owner text was checked in #1169 c.6892563291 (`amaybaum`, 2026-11-15T09:49:19Z): "Q4: yes,
the performed experiments that use one source twice are read first-hand." The note quotes it
correctly.

## Verdict: ACCEPT WITH CHANGES

The central conclusion (R-6) holds on the papers read and is correctly scoped to them ("On the papers
read … is not met by any single experiment"); it is not stated as a general absence, and Choi et al.
2020 is correctly excluded as not read in full. Most attributed facts check out verbatim. Six
corrections are required: one finding (R-5) is false as stated, one mapping (Zhu, G3) claims more
than the paper supports, and the reading grid misstates L-2's (k3) policy pattern. None of them
reverses R-6; two of them change the reasons given for it.

## 1. Per-paper check (task 1)

Versions opened: arXiv 2102.02550v2, 1504.02707v2, 1611.02430v1, 1609.01863v3, 2212.03815v1,
2202.04840v1, 1706.07370v2, 0904.1655v2 (full checks); 1906.07412v2, 2309.12286v2, 1912.02979v2,
2101.12074v2, 1112.3664v3 (quoted passages and key numbers only). DOIs checked on Crossref.

| Paper | Citation/DOI | What was done; wings reused | First-use record | Instrument | Conditioning | Raw data | Result |
|---|---|---|---|---|---|---|---|
| Zhu 2022 | correct (PRA 105, 032211; arXiv DOI field agrees) | correct; both wings twice | correct ("only middle path out of BD2 is retained"; −1 by HWP) | correct (weak A1, B1; projective A2, B2) | correct | correct (none stated) | **G3 mapping overreaches** (C2); otherwise correct, numbers verbatim |
| White 2016 | correct | correct; both Bell qubits twice, one fixed configuration a=0, b=π/4, a′=π/2, b′=3π/4 | correct ("encoded on a distinct qubit"; "all four qubits are read out") | **"unsharp" is wrong as a blanket** (C4) | correct (calibration rescaling; locality "cannot be ruled out") | correct (none in main text) | 27 s.d., ≈2.5, 600,000 iterations, ±10σ verbatim |
| Schiavon 2017 | correct | correct; Bob1 then Bob2 | correct ("one single output port at a time … tilting the glass plate") | correct | correct ("we did not subtracted accidental coincidences") | correct | all four CHSH values verbatim; 16 acquisitions, 30 s, 700 counts/s |
| Hu 2018 | correct | correct | correct ("outcomes of Bob1 are actually obtained by Bob2"; HWP1/HWP4 selection) | correct | correct | correct (on request) | 2.20 ± 0.02, 2.17 ± 0.02, 64 trials, ≈10 s.d. verbatim |
| Xiao 2022 | arXiv correct; NJP record correct (authors, title, 26, 053019) | correct; one wing | correct (linear polarizers) | correct (projective) | correct | correct | case-1 settings and all four numbers verbatim; "λ unrecorded" is an inference (O1) |
| Mao 2022 | **published venue missed** (C5) | correct; one wing per branch | correct, verbatim ("exactly one of the four outcome combinations"; time-tagged) | correct | correct (six-fold, 5 ns, 0.7 s⁻¹, 80 MHz) | correct | all numbers verbatim; "settings fixed per acquisition" not stated (O1) |
| Leupold 2018 | correct | correct (53 million measurements, 13 observables, QRNG, < 50 µs) | correct | correct | not stated in the note | **wrong: raw data are published** (C1) | R_u > 99.6 % (lowest R_h1 = 0.9967(2)); backward/forward signalling statement correct |
| Kirchmair 2009 | correct | correct | correct | correct | — | correct (none stated) | **⟨X_DHV⟩ belongs to a different state** (C6) |

Spot checks, all verbatim: Foletto 2020 ("not made in real time", "fair-sampling", "cannot be
physically excluded", "One exit of each is blocked"); Foletto 2021 ("only expectation values, hence
this is not a true Bell experiment"); Padovan 2024 ("did not include the random inputs",
"effectively using different states", data on request, Table I/II values); Feng 2020 (808 nm BBO,
four CHSH values); Higgins 2015 ("does not constitute a Bell test", accidental subtraction).

**NOT CHECKED:** Liu et al. arXiv:2102.12166; Cheng, Liu, Baker, Hall arXiv:2109.03472; remaining
fields of Feng 2020, Foletto 2020/2021, Padovan 2024, Higgins 2015; White 2016 supplement; Leupold's
public dataset itself (the repository was not opened). Choi et al. 2020: the abstract sentence the
note quotes was confirmed verbatim from OpenAlex; the Optica full text was not reachable here either
(the host returns a bot-protection page), so the note's NOT READ is correct.

## 2. Required changes

**C1. Leupold 2018 publishes its raw data; R-5 is false as stated.** arXiv:1706.07370v2 §VIII, "Data
repository": "The complete raw dataset is publicly available from an open repository on
http://www.tiqi.ethz.ch/publications-and-awards/public-datasets.html." The same section states that
the dataset "does not include the data purged in real time by the computer system due to long
sequences of dark measurements", and that of 54.5 million measurements about 1 million were ignored
because of a thresholding error, leaving "almost 53.5 million" evaluated. Correct the §2 table cell
(Leupold, "Raw data published") and R-5 ("No paper read publishes raw event data"). The purge and the
discarded million bear on completeness (brief §4, K-6) and belong in the record.

**C2. Zhu 2022's steering configurations cannot give the G3 comparison.** The steering quantity is
S_n = (1/n) Σ_m |C(x_m, y_m)| (their Eq. (7)): Alice1 and Bob1 share setting index k and Alice2 and
Bob2 share index l (Eqs. (9)–(10), "the measurement directions of Alice and Bob are chosen to be
opposite"). With one wing's policy (k, l) fixed, the remote wing's policy is fixed with it, so no
remote policy is varied. The Bell part (Supplement §B, Fig. S1) uses x₀ = Z, x₁ = X and two Bob
settings, but the paper does not state which setting combinations were acquired. Replace "The
configurations scanned would determine each wing's two-use joint law per remote policy" (1.9) and
"Zhu et al.'s scanned configurations would determine it" (R-2) with this: the steering data match
the two wings' settings and do not vary the remote policy, and the Bell-test configurations are not
stated.

**C3. The reading grid misstates (k3).** G1 asks for "a setting change between the uses on each
wing". L-2's (k3) (U3 §5.1) compares Alice's history at a *repeated* own setting `(x, x)` under Bob's
`(0, 0)` and `(0, 1)`, and the mirror pairs. The compared wing holds its setting, and the remote wing
either repeats its setting or changes it. L-3's (k3′) varies the remote *first* setting at a repeated
own setting. Restate G1/G3 (and G4) by these policy patterns, keeping §10.3's wording as the
headline. Then re-map: White 2016 changes the setting on both wings and varies nothing, so it has
neither a repeated own setting nor a remote variation. Zhu's steering data contain same-index
configurations (k = l) but no remote variation (C2). R-6 stands and its reasons get sharper.

**C4. White 2016's first use is tunable up to projective.** The strength φ is scanned from 0 to π/2
(Fig. 2, Fig. 3), and the text reports data "For projective angles φ ≈ π/2". G4 fails because the
settings change between the uses (a → a′, b → b′), not because the first use is unsharp. Correct the
1.10 bearing row and R-6 ("The two-sided experiments read … use unsharp first uses").

**C5. Mao 2022: Crossref holds a published record.** doi:10.1103/PhysRevResearch.5.013104,
"Recycling nonlocality in quantum star networks", *Phys. Rev. Research* 5, 013104 (2023), with the
same nine authors as arXiv:2202.04840. Record it as the Xiao entry does: a candidate published form,
whose identity with the arXiv text is not established here. As written, "Crossref returned only a
Research Square preprint" conflicts with the method's statement that bibliography was checked
against Crossref.

**C6. Kirchmair 2009: name the state for ⟨X_DHV⟩.** ⟨X_KS⟩ = 5.46(4) is the singlet value.
⟨X_DHV⟩ = 2.23(5) was measured on a different state, Ψ ∝ |↑↑⟩ + iγ|↓↑⟩ + γ|↑↓⟩ + i|↓↓⟩ with
γ = √2 − 1, using the Mermin–Peres square with σ_y and σ_z exchanged, where ⟨X_KS⟩ = 5.22(10). The
cell currently juxtaposes the two values as if they came from one state.

## 3. Optional changes

- **O1. Label inferences as such.** Mao: the version read does not say how settings were changed
  between acquisitions (they are set by wave-plate QHQ boxes; random choice appears only in the
  protocol). Xiao: that λ is not recorded per event follows from the unbalanced interferometer and
  the measurement of p by blocking paths, but it is not stated. Zhu: "fixed per configuration" is
  inferred from the HWP-selected outcome. Mark each as the writer's reading.
- **O2.** Give the owner decision's author and time (`amaybaum`, 2026-11-15T09:49:19Z), as the brief
  does (§A.42 item 7).
- **O3.** Give the Cheng et al. arXiv:2109.03472 entry a status label from the note's own set
  ("abstract and first page" is not one of them). The search below also located two theory items
  that could be listed in 1.13: Cabello, arXiv:2103.11844, a proposal for two Alices and two Bobs;
  and Cheng, Liu, Baker, Hall, *Phys. Rev. A* 104, L060201 (arXiv:2102.11574), which proposes a test.
  This reviewer saw them only at search-result level.
- **O4.** Xiao: the NJP abstract on Crossref matches the arXiv content ("stochastically combining no
  more than two different projective measurement strategies", "11 standard deviations"). That
  supports the candidate identification without establishing it.
- **O5.** For papers that do not discuss locality, "none … excludes the locality loophole" could read
  "none reports space-like separation".

## 4. Scope and missed papers (task 2)

The searches covered photonic two-sided sequential Bell and steering tests, two Alices with two
Bobs, projective sequential repeats on entangled pairs, and trapped-ion, superconducting and
cloud-processor sequential CHSH. They found no performed two-sided experiment beyond Zhu 2022 and
White 2016, and no performed test of same-axis repeatability on a wing of an entangled pair. This was
a brief search, not exhaustive, and it supports the note's scoping without widening it into a
general absence. Choi 2020 stays the one located experiment that was not read.

## 5. No claim beyond the papers; NOT READ items (task 3)

Apart from C1–C6 and the inferences listed in O1, every attributed quote and number sampled is in
the primary text. Choi 2020 is described only by the abstract sentence it quotes, which matches
OpenAlex. Nothing in the note reads as summarized from memory. The mapping rows are labelled as the
writer's, as the method says.

## Confirmation (r2)

**Objects:** `LIT-REUSE-r2.md` and `RESPONSE-LIT-REUSE-r1.md` (same directory and branch as above),
read against `LIT-REUSE-r1.md` by a full line diff. Primary sources were re-opened wherever a
correction depends on them. **Verdict on r2: ACCEPT.** Every required change is resolved. One small
unlisted edit is noted below. It is accurate and needs no change.

| Item | Status | Check made |
|---|---|---|
| C1 | RESOLVED | arXiv:1706.07370v2 §VIII: "The complete raw dataset is publicly available"; purged real-time data excluded; 54.5 million measured, about 1 million ignored, "almost 53.5 million" evaluated. Main text: "between two and five subsequences containing more than 55 dark measurements in a row" per million, attributed to "off-resonant leakage" into long-lived dark states, purged and restarted "from the same v0". The table row, R-5 and the §2 table agree with it. The outcome-triggered purge is labelled as the writer's reading |
| C2 | RESOLVED | Zhu Eqs. (7), (9)–(10) and the "chosen to be opposite" quote re-read. The overreaching sentence is removed, R-2 is restated, and the Bell-test combinations are said to be not stated. The k = l reading of Eq. (10) assumes one direction set for both pairs, and it is labelled as the writer's reading |
| C3 | RESOLVED | G3 and G4 match `S3-U3-r3.md` (k3) (ll. 652–656) and (k3′) (ll. 737–739) verbatim in content. The §10.3 headline fragment is unchanged in r3. Moving the citation from U3 r2 to r3 is a consequence of this item, and the response records it. Zhu, White and Xiao are re-mapped consistently |
| C4 | RESOLVED | arXiv:1504.02707v2: at φ = π/2 the operation "becomes a control-NOT gate and implements a projective measurement", and the text reports data "For projective angles φ ≈ π/2". The uses row, bearing row, §2 cell and R-6 are corrected |
| C5 | RESOLVED | Crossref doi:10.1103/PhysRevResearch.5.013104: title, volume, article number and the nine authors in order, as stated. The OpenAlex abstract contains the quoted added sentence. It also differs from the arXiv abstract in small wording ("realize … three-branch", "Einstein-Podolsky-Rosen"), so "repeats … with one added sentence" is close but not exact (optional: "with one added sentence and minor rewording"). Identity is not claimed |
| C6 | RESOLVED | arXiv:0904.1655v2: the state, the σ_y/σ_z exchange and ⟨X_KS⟩ = 5.22(10) are as stated. R-3 now says "non-singlet two-ion state" |
| O1 | RESOLVED | The *[writer's reading]* label is defined and applied to Mao, Xiao, Zhu and Leupold |
| O2 | RESOLVED | Author, time and quote match #1169 c.6892563291 |
| O3 | RESOLVED | ABSTRACT and LOCATED labels are applied. Crossref PRA 104, L060201: title and authors Cheng, Liu, Baker, Hall confirmed. The LOCATED items are described only at search-result level, attributed to this review |
| O4 | RESOLVED | Both quoted phrases are in the NJP abstract on Crossref |
| O5 | RESOLVED | Restated as "reports space-like separation"; White's "cannot be ruled out here" is quoted correctly |

**Diff scope.** Every hunk of the r1→r2 diff maps to C1–C6 or O1–O5 or to a necessary consequence: the
header and review line, the method lines on abstract sources, G5's completeness clause, the Xiao and
Mao bearing rows, the §4 source list and the U3 citation. One hunk is not listed in the response: R-4
replaces Padovan's short quote with the fuller sentence "since we are scanning the measurements one
by one, we are effectively using different states for each measurement". It is verbatim in
arXiv:2309.12286v2 apart from the case of its first letter, it changes no finding, and listing it in
the response is optional.

**Central conclusion.** R-6 is stated at the papers-read scope ("On the papers read …"; "This is a
finding about the papers read, not about the literature as a whole"), and Choi et al. 2020 is still
excluded as not read in full. Its reasons now rest on C2–C4: neither two-sided experiment realizes
the (k3) or (k3′) pattern, and the only raw dataset and the repeatability data are single-system.
