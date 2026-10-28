# First-hand citation check of Introduction-r7

**Object.** `Introduction-r7.md`, sha256 `3ef2725b3f23f8ad08cb37913c94034480bd3b87fec22be905e0c572b3af7cfd`. The copy in
the clone under `verification/audits/manuscript/introductory-paper-20261025/draft/` has the same digest.

**Scope.** The nine VERIFY-marked entries, each cited by text r7 keeps, plus the Weinberg owner gate (line 146). Mon08
was also read, because r7's Har04 sentence attributes its claim to Montina's report.

**Records.** Page numbers are pages of the arXiv PDF read. The source PDFs and their extracted text are third-party
and not committed; they are in `S/refs/<key>/`. Written by the coordinator from the reader's report, because the
reader's tool refused report files.

## Verdict counts

| Verdict | Count | Keys |
|---|---|---|
| SUPPORTED | 6 | BBS24, Cal26, EvEMU11, KP14, tH14, Vol06 |
| SUPPORTED, read through Mon08 | Har04 sentence | Montina's report of Hardy's result |
| UNREACHABLE | 4 | CT06, Har04 (Hardy's own paper), Sha79, Weinberg 1989 |
| SUPPORTED-WEAKER | 0 | — |
| NOT SUPPORTED | 0 | — |

## Per citation

| key | draft line | claimed content | verdict | passage (page / §) | replacement wording | source digest (sha256) |
|---|---|---|---|---|---|---|
| BBS24 | 272 (bib 300) | a two-step process has classical memory when the second map can be written as an instrument realizing the first map, followed by channels conditioned on its outcome | SUPPORTED | arXiv:2310.01205v2, Def. 1, pp. 1–2: "The dynamics D = (E1, E2) can be realized with classical memory, iff there is at least one Kraus decomposition {Mi} of E1[ρS] = Σi Mi ρS Mi† and suitable CPT maps Φi such that E2[ρS] = Σi Φi[Mi ρS Mi†]." p. 2: "The Kraus decomposition {Mi} can be seen as a local measurement on S which on average realizes the first map E1. The second step with CPT map Φi is conditioned on that outcome i". | None required. BBS state it with a Kraus decomposition, one operator per outcome; a general instrument gives the same class, since each outcome can be split into its Kraus operators. Optional exact form: "…when, for some Kraus decomposition $\{M_i\}$ of the first map and channels $\Phi_i$ conditioned on the outcome $i$, the second map is $\rho\mapsto\sum_i\Phi_i(M_i\rho M_i^\dagger)$ [BBS24, Def. 1]." The bibliography entry may add arXiv:2310.01205v2; its DOI matches PRL 132, 060402. | a410003530514ed679f2dd041f65a652cba307856deff644537aa3c63d8515b1 |
| Cal26 | 114 (bib 310) | Calvo states a proof of the six axioms of textbook quantum mechanics from the single axiom that every physical system evolves according to a generally indivisible stochastic law | SUPPORTED | arXiv:2601.18720v2. Abstract, p. 1: "we prove the six axioms of textbook quantum mechanics from a single axiom: every physical system evolves according to a, generally indivisible, stochastic law." §2, p. 4: "Stochastic Axiom: The evolution of every physical system is governed by a generalised stochastic process"; "Theorem 1. (The Stochastic-Quantum Correspondence). The six traditional, textbook quantum mechanics axioms can be derived from the Stochastic Axiom." | None | 0519d97d57604c32a943b3fc622cce3aa20f65c7c64c1c973ba6418ea78b81a4 |
| CT06 | 86, 88, 90, 227 (bib 314) | the conditional-mutual-information vanishing criterion (88, 227); Pinsker's inequality (90); a general reference for Theorem 2 (86) | UNREACHABLE | — | Keep the VERIFY. It is a commercial Wiley textbook with no lawful open copy. | — |
| EvEMU11 | 157 (bib 322) | trace-free Einstein equations aim to remove matter's vacuum energy as a source of curvature and "leave the observed value of Λ unexplained" | SUPPORTED | arXiv:1008.1196v2. Abstract, p. 1: "While this does not solve the fundamental issue of why the cosmological constant has the value that is observed cosmologically, it is indeed a viable theory that resolves the problem of the discrepancy…". §2, p. 2: "If these trace-free equations are adopted, the vacuum energy has no gravitational effect. This does not determine a unique value for the effective cosmological constant". §6, pp. 9–10: "this proposal does not solve the issue of why the cosmological constant has the value it has today". | None | 9e0f85dfc406ce0267616916efdb5f6d5e32b90fe5d0903db5e5072d6dd29669 |
| Har04 | 136 (bib 326) | "Montina reports Hardy's result that the number of ontic states cannot be finite [Mon08; Har04]" | Sentence SUPPORTED through Mon08; Har04 itself UNREACHABLE | Mon08 (arXiv:0711.4770v2), §I, p. 2: "similar questions were discussed by L. Hardy [10]. He proved that the number of ontic states can not be finite". p. 9: "As previous proven by Hardy [10], this mapping … does not work, since the number of ontic states has to be infinite." Montina's ref. [10] is SHPMP 35, 267 (2004), the same paper as r7's entry. | None; the sentence only states what Montina reports, which is confirmed first-hand. Keep the VERIFY on Har04: closed-access Elsevier, with no arXiv version found. | Mon08: 3cb60e2fb5c8cf01650a380d60040e8a55297e469708acbd8ade359acfa9255b |
| KP14 | 157 (bib 330) | sequestering removes matter's vacuum energy as a source of curvature and "also renders contributions from phase transitions small" | SUPPORTED | arXiv:1309.6562v2. Abstract, p. 1: "completely sequesters from gravity all of the vacuum energy from a matter sector … and renders all contributions from phase transitions automatically small … prevents any of its vacuum energy … from sourcing the curvature of the universe." p. 6: phase-transition contributions "become automatically small at times after the transition in a large and old universe … far smaller than the current critical density". | None required. Optional: "…small at late times in a large, old universe [KP14]". | be61a4bfbf2d9cffc99e96c49b4f4524f9aa6281bdda96a6e0417fad9c7572b9 |
| Sha79 | 170 (bib 352) | "its linear case is the secret-sharing threshold [BHa; Sha79]" | UNREACHABLE | — | Keep the VERIFY. Two lawful copies exist: the ACM DL bronze open-access PDF (doi 10.1145/359168.359176) and MIT DSpace MIT-LCS-TM-134 (hdl 1721.1/148961). Both sit behind bot challenges from this egress, which the reader did not try to get past. | — |
| tH14 | 195 (bib 354) | "deterministic systems analysed with quantum methods have been studied before, for example in [tH14]" | SUPPORTED | arXiv:1405.1548v3. Abstract, p. 1: "Examples are displayed of models that are classical in essence, but can be analysed by the use of quantum techniques". Ch. 2, §2.1, p. 21: ontological states "form a basis for a Hilbert space that we may herewith define … all ontological states form an orthonormal set". | None | 6df7d330378d76f0fd08ff6b6b73bb888e7776ae50e56cb342db839e5424b24e |
| Vol06 | 157 (bib 356) | "Volovik argues from the thermodynamics of quantum many-body ground states that the ultraviolet zero-point sum does not set the vacuum energy" | SUPPORTED | arXiv:gr-qc/0604062v4. Abstract, p. 1: the myths, including "the dominating contribution of zero point energy of quantum fields to the vacuum energy", "appear to be wrong when one considers the thermodynamics of the ground state of the quantum many-body system … in spite of the ultraviolet divergence of the zero-point energy, the natural value of the vacuum energy is comparable with the observed dark energy". §5.2, pp. 9–10: "The higher-energy (trans-Planckian, microscopic) degrees of freedom … perfectly cancel the huge positive contribution of the zero-point fluctuations". | None. The PDF header says IJMP A, but arXiv's journal_ref and the DOI give IJMP D 15, 1987 (2006), as r7 has it. | 4d91039faf2d2a9efea3f801fb1c04e62eaaf161e78d8883c7c9f93b57e6b8bb |
| Weinberg 1989 (owner gate, line 146) | 147 | "Summing zero-point energies … up to a Planck-scale cutoff gives a vacuum energy density some 120 orders of magnitude above the observed one …, the exact power depending on the cutoff convention" | UNREACHABLE | — | Not citable as written: it could not be read first-hand, so the gate stays open. | — |

## Weinberg 1989 (Rev. Mod. Phys. 61, 1; UTTG-12-88)

**Nothing was cited from memory, so nothing is said first-hand about Weinberg's figure, his cutoff, or the section it
is in.** No first-hand copy was reachable:
- **Publisher.** The APS PDF links return 403; the article is paywalled.
- **Green open-access copy.** The only one found is the submitted version at Texas ScholarWorks, UT Austin (hdl
  2152/61094, per OpenAlex). Its CloudFront WAF returns 403 "Request blocked" to this egress. Its TLS chain roots in a CA
  outside the proxy bundle; it was verified with the Mozilla roots rather than by disabling verification. The reader did
  not try to get past the bot check.
- **Other routes.** INSPIRE has no eprint, OSTI 6538767 is metadata only, ADS has no scan, and CERN CDS shows a bot
  challenge.

**What r7 actually says:** "some 120 orders of magnitude". The figure 10¹²² does not appear in r7.

**Second-hand context, not a substitute for the gate.** EvEMU11 (read first-hand), §2, p. 3, eqs. (11)–(12): "With a
suitable high-energy cut-off, the vacuum energy density is estimated by Weinberg [20] to be of the order
⟨ρvac⟩ ≃ 2×10⁷¹ GeV⁴", against "⟨ρobs⟩ ≃ 10⁻⁴⁷ GeV⁴". That is a ratio of about 10¹¹⁸. Its abstract says "incorrect by
between 60 to 120 orders of magnitude". EvEMU11 does not name the cutoff as Planck-scale.

**Ways to close the gate:**
1. The owner fetches the UT ScholarWorks copy in a browser and places it in `S/refs/Wei89/`; the check and the
   citation text then follow.
2. As a stopgap, cite the EvEMU11 passage as a report of Weinberg's estimate. That does not meet the gate's "read
   first-hand" condition.

## Still UNREACHABLE (keep VERIFY)

- **CT06:** commercial textbook with no lawful open copy.
- **Har04:** closed Elsevier with no arXiv version. The r7 sentence itself is confirmed through Mon08.
- **Sha79:** open copies at ACM and MIT DSpace sit behind bot challenges from this egress.
- **Weinberg 1989:** paywalled at APS, and the UT green copy is blocked by its WAF. The owner gate stays open.
