# Introduction draft r6: changes from r5

## Inputs

Both reviews concern r5 (sha256 `c538d9e1…5c24`), which is unchanged:
- the scientific review `S/paper/sci-review/REVIEW-r5.md` (ACCEPT WITH CHANGES; C1, C2, N1–N3);
- the editorial review `S/paper/ed-review/REVIEW-r5.md` (ACCEPT WITH CHANGES; RC1–RC5, recommended flow items,
  trims T, layout variant L1, nits).

**Rule for conflicts:** where the two reviews touch the same sentence, the science wording governs content and the
editorial wording governs presentation.

**Method.** `S/paper/draft/scripts5/build_r6.py` applies each edit to r5 as an exact, uniquely matching replacement,
so every unchanged sentence stays byte-identical to r5. "l." means r5's line number.

## Required

| Item | Where | Applied as |
|---|---|---|
| **sci C1** | l.169, N-LIT2 | Verbatim: "…and of vacuum-energy sequestering, which also renders contributions from phase transitions small [KP14]" |
| **sci C2** / **ed RC5** | §6.2 item 8 | Verbatim sci C2: "What the paper states are the cited theorems and their scopes." **Resolution:** both reviews target the same sentence, and science governs the content. Ed RC5's "The paper's content is the cited theorems and their scopes" is not used |
| **ed RC1** / **sci N2** | l.30, N-INT1 | Verbatim ed RC1: "The paper develops one idea, OI: its foundation and quantum-emergence results (§§2–3), and two of its consequences, for the cosmological constant (§4) and for black-hole information (§5)." **Resolution:** sci N2 and ed RC1 agree on the structure "one idea, OI: its foundation … and …". RC1's "two of its consequences" is taken, because it matches the abstract, Contributions and §6 (presentation). Sci N2's "two applications" carries the same claim, so no content conflict arises |
| **ed RC2** / **sci N3** | abstract | Verbatim: "Each class contains the Markov laws, so representability does not distinguish a law with memory from one without, and the Born exponent is not selected." It replaces r5's "The Born exponent is not selected." |
| **ed RC3** | §4 | (i) "the mismatch" is named at its source (l.159: "(the mismatch)"). (ii) The proposal is stated before "its content" (l.161: "OI's proposal is that the mismatch requires no cancellation, and its content lies in …"). (iii) Symbols defined (see the note below this table). (iv) The Hubble rate is renamed $H_{\rm Hub}$, its only occurrence, so it does not clash with the hidden sector $H$ |
| **ed RC4** | §5 | (i) $t_{\rm evap}$ is "the evaporation time" and $\tau_B^D$ is "the $D$-sector timescale [GR App. A.5]" (Departures 1). (ii) "accessible advantage" is glossed at first use (l.182: "that is, no gain in success probability over a blind guess"), and the later gloss in l.184 is removed (this also settles ed nit "line 184"). (iii) H-scramble is glossed at first use ("equidistribution of the orbit over pure states on an energy shell", r4/GR wording), and the separate defining sentence is removed |

**RC3 (iii), the symbols defined.** Each is glossed in one clause at first use:
- $\mathcal G_{\mu\nu}$, the Einstein tensor;
- $T^{\rm cl}_{\mu\nu}$, the classical stress-energy of the substratum;
- $\rho_C$, the energy density of the offset;
- $E_{\mu\nu}[g,\mathrm{OI}]$, the gravitational side still to be derived;
- $\mathcal F[g,T]$, a scalar functional of the metric and the stress-energy.

GR displays $E_{\mu\nu}[g,\mathrm{OI}]$ and $\mathcal F[g,T]$ only at GR:12 (abstract, the G3 target form), and
$\mathcal G_{\mu\nu}$, $T^{\rm cl}_{\mu\nu}$ and $\rho_C$ only in the two completions at GR:356. It defines none of them in words
(checked by grep at `687e885b`). Each gloss names the role the symbol plays in those displays and adds no claim:
- the offset is GR:356's $C$ (the invariance $\Omega_{\rm eff}\to\Omega_{\rm eff}+CI$);
- "the Einstein tensor" is the standard reading of $\mathcal G_{\mu\nu}$.

## Recommended (flow): applied where no claim changes

| Item | Applied as |
|---|---|
| Bridge into §4 | "In OI (§1.1) the zero-point sum of the emergent quantum description (§§2–3) and …" |
| Bridge into §5 | "Because the dynamics of OI is a bijection observed through a partition (§1.1), two questions separate: …" (replaces "Under OI two questions separate:") |
| Calvo moved | out of §2.2, to the end of §3.1, after the representation-result sentence |
| 't Hooft sentence deleted (l.74) | [tH14] stays cited in §6.2 item 8 |
| Connective at l.110 | "With this lemma, on a fixed finite reversible substratum history readback forces …" |
| Memory in the conclusion | as a clause: "…; because the representation is universal, the discriminating content lies in memory, which every deterministic completion carries in its hidden state." The clause shortens r4:249 s2 to fit the length target |
| Bell sentence split (l.152) | split after "must give up one of the two." F7's "with measurement independence kept" (§6.1) is untouched |
| "no experiment yet" | Applied in a content-preserving form (Departures 2) |
| Ed nit F3 | "The written proof is in [Main §3.4, Theorem (unavoidable hidden predictive memory)]; see also [CT06]." |
| sci N1 (optional) | **Not applied:** dropped for length. It is optional, and the sentence is correct as it stands (sci REVIEW §2) |

## Length

| Item | Applied as |
|---|---|
| Trim T, l.150 | "The origin of the quadratic Born exponent, which the correspondence does not select (§2.3), is open [Main §3.4; Bar26, Thm 3.1]." |
| Trim T, §6.2 item 4 | "No resolution of the black-hole information problem: the Page curve of [GR App. A] is not established (§5), and the results of §5 concern finite toy models, each proved on paper or checked exhaustively at small size or by exact arithmetic. No claim is made that information reaches $D$, …" Two things carried only here are kept: the verification-layer clause, and the three "No claim is made …" disclaimers (information reaching $D$; [GR, Thm A.7] within scope; other decoupling arguments). The removed conditions for the Page curve are stated in §5 (r6 l.176): H-scramble, the closure, the full-shell scope and the cycle average. So are the islands and generalized-second-law clauses (r6 l.178) |
| L1 | The six `***` rules from the abstract through §6 are dropped. The rule under the title block is kept, as in the editorial variant |
| F1 reverted | The r5 sentence "Exact operational quantum mechanics is reached only under conditions that OI alone does not imply (§3.2)." is removed from §1.2. N-INT1 now replaces it, as OUTLINE-r7 specified. The qualification is unchanged in the abstract, §3.2, §6.2 items 1–2 and the conclusion |
| l.142 → Appendix A | **Not taken**, as instructed |

## Departures from a reviewer's exact text

1. **RC4 (i), the τ_B^D citation.** The editorial suggestion reads "the time scale of the $B$–$D$ coupling [GR App.
   A.7]". r6 uses GR's own definition instead: "the $D$-sector timescale [GR App. A.5]". GR:761, in App. A.5, reads
   "Let $\tau_B^D$ be the $D$-sector timescale". GR's wording is the source.
2. **"No experiment yet."** Dropping "yet" alone would leave "no experiment distinguishes OI from standard quantum
   theory", which reads as a claim that none can, stronger than Main:704 ("No ontology-level memory falsifier is
   established"). r6 reads "no experiment distinguishing OI from standard quantum theory, and no memory-witness
   constraint, is established [Main §4.5]". It is time-neutral, as the nit asks, and stays at the source's strength.
3. **Memory in the conclusion.** It is a clause, not the full r4 sentence, so the text stays near 11.7 pp.
4. **sci N1** is not applied (optional; length).

## Build and checks

- **Build:** 17 pp; 0 overfull boxes; 0 missing glyphs; median 2,574 characters per page.
- **Main text:** abstract–§6.4 ends on p. 12, line 33 of 45, **11.73 pp** by the editorial reviewer's `measure.py`
  (r5: 11.89). The code section and Appendix A start on p. 12.
- **Repository checks,** on a fresh `git archive` of `687e885b` with r6 at `papers/Introduction.md`:
  `voice_check`, `claims_check` and `duplicate_check` are OK.
- **Identifier check:** `identcheck.py` finds 28 Lean identifiers, 0 unresolved and 0 Appendix A line mismatches.
- **Bibliography:** 38 keys, none uncited, none undefined.
- **§A.32/§A.33 scan of the 21 changed lines:** 0 hits; caps CHSH only.
- **Markers:** 9 OWNER and 9 VERIFY, as in r5. The two approved raw lines are unchanged.
