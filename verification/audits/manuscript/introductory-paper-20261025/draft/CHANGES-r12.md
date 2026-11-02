# Introduction draft r12: changes from r11 (final scientific review)

## Inputs

- **Base:** r11, sha256 `a25e973c…f1d7`. r11 is unchanged.
- **Final scientific review of r11:** `review/scientific/FINAL-REVIEW-r11.md`. Verdict REVISE (minimal): two
  blocking findings (B1, B2) and eight nits (N1–N8).
- **Corpus:** `main` `c967d6a9` (after #937).
- **Method.** `draft/scripts/build_r12.py` applies 12 edits to r11, each an exact, uniquely matching replacement.
  Every sentence it does not touch is byte-identical to r11. r12 adds nothing beyond the findings and one page-budget
  trim.

## Findings and edits

| Finding | Where | r11 | r12 |
|---|---|---|---|
| **B1** | §3.2, setup of Theorem 4 | "Fix a nonempty finite system and an operational theory specifying which finite outcome families of linear maps are available on the system and at every ancilla level [GR §3.3]." | "… at every ancilla level. The theory contains the identity and is closed under coarse-graining of outcomes and, at every ancilla level, under outcome-conditioned composition; it has an available preparation of a uniformly mixed ancilla, which an available operation may follow, an available spectator-independent local readout of the ancilla, and ancilla discard: an available preparation followed by an available instrument, with the ancilla then discarded, is an available operation on the system [GR §3.3]." |
| **B2** | References, Corpus line | "(repository commit `17b830bc`," | "(repository commit `c967d6a9`," |
| **N1** | §2.4, capacity bound | "(machine-checked)" | "(machine-checked in the same form as Theorem 2)" |
| **N2** | §3.4 | "… the unboundedness is imported [Main §3.4, Proposition (…)]." | "… [Main §3.4, Proposition (…); HKLP24, Thm 4]." New bibliography entry [HKLP24] |
| **N3** | Code, data and formal verification | "… released under the MIT License (concept DOI 10.5281/zenodo.19060318), at these repository paths: … (probes); … (black-hole computations)." | "… released under the MIT License, at these repository paths at the corpus commit: `papers/oi_lattice_code/foundations/` (probes; also in the release archive, concept DOI 10.5281/zenodo.19060318); `verification/programmes/black-hole-information/` (black-hole computations; not part of the release archive)." |
| **N4** | Abstract | "Open are which of these a physical substratum supplies," | "Open are which of conditions (iii)–(v) a physical substratum supplies," |
| **N5** | §2.5, Theorem 3 | "*Let $\varphi$ be a bijection of a finite set.*" | "*Let $\varphi$ be a bijection of $\mathcal C_V\times\mathcal C_H$ with a fixed hidden prior.*" |
| **N6** | §6.2 item 4 | "the results of §5 concern finite toy models," | "the results of §5 reported from [BHa; BHb] concern finite toy models," |
| **N7** | §2.4, conditions paragraph | "In a faithful realization (C4) coincides with $M_t>0$, by the Corollary;" | "In a faithful realization (C4) coincides with $M_t>0$ by the vanishing criterion [CT06], and the Corollary places it in the hidden state;" |
| **N8** | Appendix B.3 | `<!-- Source of the decomposition below: ERRATUM-r4 (design record), …; not a corpus derivation. -->` | *(deleted)* |

## Checks behind the edits

### B1: the hypotheses checked against the kernel

`FiniteOperationalTheory` was read at `c967d6a9`, at `OperationalAssembly.lean:594` (the file is identical at
`17b830bc`). Each field maps to a clause of the new sentence:

| Field | Clause in r12 |
|---|---|
| `avail_id` | "contains the identity" |
| `avail_coarse` and `availExt_coarse` | "closed under coarse-graining of outcomes" (system and every ancilla level) |
| `availExt_bind` | "at every ancilla level, under outcome-conditioned composition" (the rule is stated on the extended carriers only, so the clause is scoped to them) |
| `prepAvail_uniform` | "an available preparation of a uniformly mixed ancilla" |
| `prepAvail_post` | "which an available operation may follow" |
| `readout_avail` and `readout_local` | "an available spectator-independent local readout of the ancilla" (the readout's form is derived, not postulated, by `readout_is_localLuders`) |
| `prepAvail_discard` | "ancilla discard: an available preparation followed by an available instrument, with the ancilla then discarded, is an available operation on the system" |

The sentence starts from GR:216's clause ("closed under coarse-graining and outcome-conditioned composition, with a
spectator-independent local readout of the ancilla") and adds the fields GR leaves implicit. Theorem 4's statement
and its §A.34 witnesses are unchanged: ⇒ is `physical_of_exactAll`, ⇐ is `exactAll_of_physical_general`. No
hypothesis is shortened.

### B2: corpus pointers at `c967d6a9`

**Identical files.** `git diff --stat 17b830bc c967d6a9` is empty for:
- `verification/lean` and `verification/lean-mathlib`;
- `tools`;
- `papers/Main.md`;
- `verification/programmes/black-hole-information`;
- `papers/oi_lattice_code`;
- `.gitattributes`.

The Lean pins (Conventions, Code section, Appendix A) therefore stay at `17b830bc`, and `papers/introduction_repro/`
holds unchanged. Every [Main §…] pointer and every [BHa]/[BHb] item resolves as before. Book ch01 (§1.11) is
unchanged.

**What #937 changed, and what the paper cites from it.** None of the cited content moved.

- **GR**:
  - §2.2 (C4, GR:52), §3.3 (GR:216/218) and App. A.1–A.9 are textually identical. App. A shifts by two lines
    (A.1 :717, A.7 :805, Thms A.7–A.9 :811/:817/:845, "Proper energy shells" :843).
  - §6.2 (GR:356) still carries the content §4 cites: the invariance under $\Omega_{\rm eff}\to\Omega_{\rm eff}+CI$,
    the two completions differing by $\rho_C g_{\mu\nu}$, and G3 open. Its changed final sentence now reads "that it
    does not enter the stress-energy tensor is the geometry-first proposal of this section, and establishing it is
    the coupling step that G3 leaves open". That agrees with the paper; at `17b830bc` the same sentence asserted
    the opposite (the review's B2).
  - The dependency ladder (GR:12) still makes G4, including the Page curve, conditional on G3, with the same
    target equation.
- **Book §7.6:** ch07:110 still reads "which the Page-curve derivation below addresses under its own conditions";
  only its "dissolution" phrase changed, to "conditional". The islands correspondence is still "conjectured".
- **Book §18.5:** ch18:146 still reads "the Page curve at the emergent level is a conditional result".

### N1

`card_hidden_ge_two_pow_Istar` (C3Necessity:117) is stated for `HiddenMemory.Realization`, a joint law of history,
present and hidden state. Its $I^*$ is a maximum over a finite nonempty family of slices sharing $H$. The form
Theorem 2 carries in the text (machine-checked for a joint law; the time-$t$ identification not machine-checked)
therefore applies. The review's shorter wording is used.

### N2

- **[HKLP24] was read first-hand.**
  - Source: arXiv:2308.07727v4 (PDF sha256 `194e5227…6868`); arXiv's API gives `journal_ref` "Phys. Rev. A 109,
    032627 (2024)" and DOI 10.1103/PhysRevA.109.032627.
  - Theorem 4, p. 4: "For all integers d, m ≥ 2 there is a communication matrix C such that dimQ(C) ≤ d while
    dimC(C) ≥ m" (proved for d = 2, a qubit, through Lemma 3, rank₊(Aₙ) = Ω(log n)).
  - This is the unboundedness Main:538 imports, from its ref. [55]. The bibliographic details agree with Main:884.
- **No VERIFY marker is needed.**
- **GH03 and Mon08 stay as illustrations.** Har04 stays only in the Montina sentence, the one place it is cited.

### N3

`.gitattributes` at `c967d6a9` (identical at `17b830bc`) excludes `verification/programmes`, `verification/audits` and
`verification/infrastructure/round-*` from release archives. `papers/` is not excluded, so the probes are in the
release archive and the black-hole computations are not. The repository's root `LICENSE` is MIT.

### N5

`pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148) takes a `RootedRealization`
(CausalReadback.lean): a reversible update `step : V × H ≃ V × H` and one fixed hidden prior shared by every root.

## Page budget

r11 with the findings applied ends the main text at p. 13 line 3 (12.06 pp). One trim, within the owner's rule, brings
it back.

| # | Where | Old | New | Why it is within the rule |
|---|---|---|---|---|
| P1 | §6.1, last sentence | "Two long-standing problems would then change form: vacuum energy becomes a question about how two levels of description couple to geometry, and black-hole information separates into conservation and accessible recovery." | *(deleted)* | **Repetition.** §4 states the first half ("its content lies in how the two levels couple to geometry"); §5 the second ("two questions separate"); the conclusion (§6.4) restates both, and so does the abstract. It is not a limitation, hypothesis or evidence qualification |

**Tried and not used:**
- **"The indivisibility of §2.5 is global …" (§3.1).** It borders on a limitation statement.
- **"The invariance is the familiar statement …" (§4).** Not needed: it ends a page that already breaks before a
  section heading, so it moves no page break.

## Build and checks

- **Build:** 17 pp; 0 overfull boxes; 0 missing glyphs; median 2,681 characters per page.
- **Main text:** abstract to §6.4 ends at **p. 12, line 43**, which is **11.90 pp** by the editorial measure. "Code,
  data and formal verification" starts at the top of p. 13.
- **Repository checks** on a fresh `git archive c967d6a9`, with r12 as `papers/Introduction.md`: `voice_check` (41
  files), `claims_check` and `duplicate_check` are OK.
- **identcheck** at `17b830bc` and at `c967d6a9`: the 28 Lean identifiers resolve, with 0 Appendix A line
  mismatches at either commit. The tool also lists the backticked commit hash `c967d6a9` of the Corpus line as an
  unresolved token. It is not a Lean identifier: the old pins began with a digit, so the tool skipped them.
- **Against `papers/introduction_repro/README.md`:** all 28 match. 27 match by script; the 28th,
  `finiteIsometryExtensionSF_discharged` at IsometryExtension:116, was checked by hand as before.
- **Bibliography:** 39 keys (HKLP24 added), none uncited.
- **§A.32/§A.33 scan of the added lines:** 0 phrase hits and no all-caps words.
- **Markers:** 0 OWNER and 4 VERIFY (CT06, Har04, Sha79, Weinberg). Weinberg remains an open landing gate.
