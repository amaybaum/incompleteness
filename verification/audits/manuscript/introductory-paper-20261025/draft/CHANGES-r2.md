# Introduction draft, revision 2: changes

**Applies:**
- the scientific review `S/paper/sci-review/REVIEW.md` (sha256 `061c3d2b…e8c1`);
- the editorial review `S/paper/ed-review/REVIEW.md` (sha256 `91d3bc0b…4f79`).

Both reviews concern `Introduction.md` (r1, sha256 `03c1154b…4b25`), which is kept unchanged.

**Output:** `Introduction-r2.md` (sha256 `98d35eec…`; see DRAFT-NOTES-r2 for the full hash).

**Rule for conflicts:** where the two reviews conflict, the scientific review governs content and the editorial review governs presentation. Every conflict is listed below.

## Scientific review

| Item | Applied as |
|---|---|
| RC-1 (false $\Gamma_1\Lambda=\tfrac12J$) | Replaced verbatim (§4.3) |
| RC-2 (card-table quantum sentence) | Applied with the exact content: the uniform diagonal burn card under the permutation-unitary embedding [Main §3.2]; the constant channel $\operatorname{tr}(\rho)I/2$, entanglement-breaking; the two-step identity; CP-indivisible; the definition of classical memory following [BBS24]; no decomposition for the initialized slot [Main §4.5]; the Pauli instrument for the uniform burn card. "Record which Pauli was applied" is removed. The text is split into three sentences (editorial presentation). [BBS24] is added. The optional D1 sentence is not included and is marked `OWNER: D1` |
| RC-3 (§5.2 H-scramble/PSW) | Replaced verbatim. C6(c) is included. [PSW] is deleted |
| RC-4 (R11 markers) | §5.1 marker extended verbatim; it also names ch18:146, ch18:158 and ch18:130. §5.2 marker extended verbatim (ch18:146, ch19:334). New markers: the abstract, §6.5 item 4 (r1 item 5), and the conclusion's second paragraph. The decoupling sentence, now in §5.4, keeps its GR:811 marker. R12 (ch18:148 / FULL:4968) has its own non-blocking marker at §5.3 |
| RC-5 (§6.2 quotient) | Replaced verbatim, with `bridge_traj` forward, `rooted_eq_iff_slice_eq` forward and `realData_traj_stochastic`. No "exactly when" remains |
| RC-6 (attribution up front) | Abstract sentence inserted, ending at "as one theorem" as RC-6 requires until the §A.42 retention is met. §1.2 "Contributions" carries the citations |
| RC-7 (non-claims) | The card-game item is added, with the corrected wording. Item 2 gains "which of (iii)–(v) a physical substratum supplies is open". Item 4's last clause is now "finite toy models whose reviews are internal, not external validation". The list is compacted (see conflict C13) |
| M1 (`isDiag_Phi`) | The non-disturbance step now rests on the Born weights being indicators, as `D_imp_Qfb` proves. The added sentence on product states and `isDiag_Phi` was cut for length; the appendix keeps `permMatrix_mem_unitaryGroup` only. **Partly adopted** |
| M2 | Applied: "no stochastic intermediate transition map exists (where the candidate $\Gamma_s^{-1}\Gamma_t$ exists, it has negative entries)". "Usually associated with quantum theory" became "The stochastic–quantum correspondence relates these features to quantum theory [Bar23; Bar25]" |
| M3 (HKLP/Hardy04) | §6.3 now rests on [GH03] and [Mon08], with Hardy's result "as reported" [Mon08; Har04]. [HKLP] is dropped. Reading the sources is owner decision D3 |
| M4 (SCH) | [Sch21, Thm 2] is added beside [Bar26, Thm 3.3], as "coincides with". Placed in §2.2, because §7 related work is cut (C14) |
| M5 (checking scope) | "Checked exhaustively at small size … Page-time fraction by exact algebra" (§5 intro). Item F is "by exact interval arithmetic" (§5.4). The review mention moved to §6.5 item 4 (see conflict F3b) |
| M6 (characterization hypotheses) | Not applicable: the characterization paragraph is cut (C4). The memory corollary carries the content |
| Bibliography table | VERIFY removed for BB, Bell64, CHSH69, GH, Hawking, Lean4 (LNCS volume omitted), Mathlib, Milz, MO, Penington and SGD. EG initials fixed; Hardy title added; LPW authors fixed; journal references added for GH, MO and Pen. [PSW] and [HKLP] deleted. [BBS24] and [Sch21] added |
| Nits | "characterized exactly by five completion conditions"; "distinguishes a law with memory from one without"; "Three statuses are kept apart" removed; "lattice" dropped; "(C4) coincides with $M_t>0$, by the Corollary"; "exact enumeration of the equally likely cases"; "The indivisibility of §3.1 is global" |

## Editorial review

| Item | Applied as |
|---|---|
| RC1 / F1 (blank lines before lists) | Every list is preceded by a blank line, checked by script. Short fragment lists are written as prose (F tables) |
| RC2 / F2 (Appendix A as a list) | List, one entry per result. Main-ledger pointers and "none" rows are dropped; the Theorem 2 rows are merged |
| RC3 / F3a | The packaging/comb sentence is dropped altogether: the comb literature is unread, so RC3's fallback applies |
| RC4 / F3b | The review sentence is removed from §5's opening. **Conflict with science M5:** the internal-review status is kept as a non-claim (§6.5 item 4), not in §5's description |
| RC5 / F3c | "The bound is the remnant-capacity form of a known fact, and its linear case is the secret-sharing threshold [BHa; Sha79]". [Sha79] is added and marked VERIFY (from memory) |
| RC6 / F3d–e | Decoupling moved to §5.4 as declarative text with the full-interval statement and its limits; the post-plan narration is gone; r1 line 367 ("is reversed") deleted. R11 marker kept |
| RC7 / F6 (abstract) | The replacement structure is adopted. **Conflict with science RC-6:** the three "(machine-checked)" parentheticals are omitted, because a Lean-check claim in the abstract needs the §A.42 retention first. The status distinction kept is "one step proved on paper only". The card-game sentence was later cut for length |
| RC8 | Corollary (proved on paper), verbatim in substance |
| RC9 | Applied, shortened (C7) |
| RC10 | Theorem 4 stated as a sentence; the two direction witnesses are named beside it (§A.34) |
| RC11 | Probability table with protocol rows and a separate Markov row; "probability", not "odds"; "a street is one shuffle step" |
| RC12 (conventions) | Added. "Kernel" no longer appears in the body; $\pi_V$ and $J$ are defined. **Conflict with the coordinator's default Lean wording** ("checked in Lean 4/Mathlib at commit X by recipe Y"): the conventions define "machine-checked" as exactly that wording, and an `OWNER: decision 2` marker records that the word is the owner's choice |
| RC13 | Lead sentences for §2, §3 and §4. §3 retitled "Physical interpretation: indivisibility from recurrence". The §1.2 pointer to [Main] adopted |
| RC14 | Applied ("presently", "This is the content…", and the "form … is false" sentence removed) |
| F7 (terms) | Conditions (i)–(v) are defined in one line each. Also defined or glossed: access class, accessible advantage, street/hole/burn, the sector $D$, P-divisible on $\{0,\dots,n\}$, "fixed finite observation process satisfying (C1)–(C4)" and ontic parameter dependence. "Posit ledger" and "inert ledger bits" are gone |
| F8 (notation) | Classes renamed $\mathsf S_K,\mathsf D_K,\mathsf Q_K$ with "=", and the paper notes Main's $S\iff D\iff Q_{\mathrm{fb}}$. The §5.1 set is $\mathcal U$ and the messages are $\mathcal M$. "Conjugation by the Hadamard gate". The product form is used in §1.1, and "(C1)–(C4)" throughout. **Owner item:** the notation now differs from Main's |
| F10 | §6.1 retitled "Operational completion". Theorem 4 is cited as "[GR §3.3, Theorem (operational-completion characterization)]". On the GR:228 witness question: GR:218 names `exactAll_iff_physical_general` for Theorem 4 itself, while GR:228's `main_result` / `oi_compatible_classification` belong to the separate box with the OI conjunct, which the paper does not cite (design decision 5). No misalignment |
| F11 | Main remark titles are now verbatim. GR theorem citations use "[GR, Thm A.n]" |
| F13 | "Contributions" paragraph added at the end of §1.2 |
| F14 | Applied. Main's subtitle risk is listed in DRAFT-NOTES-r2 |
| F15 | Overfull boxes reduced from 28 to 8: seven are in Appendix A, from unbreakable `\texttt` identifiers, and one is 7.8 pt in the references. Repository paths are shortened, and the Lean recipe is a code block |
| F16 (title hyphenation) | Not changed: the title is owner decision R1 |
| F17 (bibliography) | One author-year key scheme; one journal pattern; first page only; arXiv version suffix on every arXiv entry; no DOIs except the corpus concept DOI. BH entries carry an author and descriptive titles, without round names or review SHAs. Status line is "DRAFT PRE-PRINT" |
| Nits | All applied: "We model embedded observation by a triple"; "is posited"; "candidate"; "distinct"; 5/9 diagonal and 4/9 off-diagonal; "modelled as"; the bound named; the β sentence; Hardy via Montina; "adopted branch" removed; "At every finite horizon"; full SHA once |

## Cut list

| Cut | Applied | Note |
|---|---|---|
| C1 | Yes | Identifiers moved to Appendix A, except Theorems 1 and 4 (§A.34) and §6.2 (science RC-5 text) |
| C2 | Yes | Attribution as one paragraph |
| C3 | Yes | — |
| C4 | Yes | Per-horizon characterization paragraph cut, which makes science M6 moot |
| C5 | Yes | One sentence for (C1)–(C4) |
| C6 | Yes | — |
| C7 | Yes | Shortened |
| C8 | **No, conflict** | Science RC-2 requires the definition, the [BBS24] citation and the uniform-versus-initialized decomposition statement, so the content is kept. The presentation is compressed into prose |
| C9 | Yes | "Nested traces" (Fubini) dropped |
| C10 | Yes | Decoupling as one paragraph in §5.4 |
| C11 | Yes | Robustness dropped; sensitivity reduced to one value |
| C12 | Yes | ε-gluing paragraph cut; no conclusion rested on it |
| C13 | **No, conflict** | Science RC-7 requires a complete non-claims list, so it is kept as a compact six-item list (one paragraph-length line each). Editorial F5 is noted |
| C14 | Yes | §7 related work deleted. Attributions are at the point of use: B26 Thm 3.3, Sch21, SGD19 and Milz20 in §2.2; Page and Penington in §5; Galvão–Hardy and Montina in §6.3. BLP09, BJA17, RHP14, BD16 and Dou26 are already cited in place |
| C15 | Yes | §6.4 is one paragraph |
| C16 | Yes | — |
| C17 | Yes | — |

## Result

The repository default build is **15 pages**, against 20 for r1, from a fresh `git archive` of `687e885b`.
- `build.sh` reports no dropped glyphs.
- xelatex reports 8 overfull boxes.
- voice_check and claims_check are OK.
