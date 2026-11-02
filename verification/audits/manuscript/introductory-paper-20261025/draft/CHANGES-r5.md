# Introduction draft r5: changes

## Inputs

- **Source:** design r7, `S/paper/design-r7/{OUTLINE,CLAIMS,DEPENDENCIES}-r7.md`. It is accepted ("ready to draft
  from") by `S/paper/design-r6-review/RECHECK-r7.md`, whose optional nits 1–2 are applied.
- **Baseline:** r4, `Introduction-r4.md`, sha256 `5f9fdcc5…68f6`. It is unchanged.

## Method

- **Built by script.** `S/paper/draft/scripts5/build_r5.py` takes every r4 sentence from the r4 file by line number
  and asserts it is present verbatim. A carried sentence therefore cannot drift.
- **New wording** is a literal string in the script. Each new sentence is listed in §2.
- "rN" below means r4 line N. "rN s1" is sentence 1 of that line.

## 1. Map: r5 paragraph → OUTLINE-r7 item → source

| r5 line | Content | OUTLINE-r7 item | Text source |
|---|---|---|---|
| 1–8 | title block | — | r1–8. The owner's title; hyphenation pending |
| 12 | abstract | Abstract (R16) | r12 s1–3, s5, s6–7 verbatim; s4 reduced to "The Born exponent is not selected."; N-AB1 and N-AB2 verbatim |
| 14 | R11 marker | Abstract | r14, re-pointed to §5 |
| 22–26 | §1.1 | §1.1 | r22–26 verbatim |
| 30 | §1.2 opening | §1.2 | r30 verbatim, section pointers renumbered (§3 → §2.5; §6 → §3.2). **N-INT1 is inserted before r30's last sentence** (Flag F1) |
| 32 | Contributions | §1.2 | OUTLINE text verbatim + r32 from "The components of Theorem 1 …" verbatim, with pointers renumbered (§3 → §2.5; §6.1–§6.2 → §3.2–§3.3) |
| 34, 36 | Conventions; decision-2 marker | §1.2 | r34, r36 verbatim |
| 42 | §2 lead | §2 ("r4:42's lead adds Theorem 3") | **new wording** (F2) |
| 44–64 | §2.1, Theorem 1 and its witnesses | §2, carried | r44–64 verbatim |
| 66 | Realization | §2, S-1 (with C4) | OUTLINE S-1 verbatim |
| 68 | Quantum representation | §2, S-2 | OUTLINE S-2 verbatim |
| 70, 72 | Attribution; Calvo | §2, carried | r70, r72 verbatim |
| 74 | 't Hooft | §2, N-LIT1 | OUTLINE verbatim |
| 76–92 | §2.3; §2.4 setup; Theorem 2 | §2, carried | r74–90 verbatim |
| 94 | Theorem 2 status | §2, S-3 | r92 s1–2 verbatim + "The written proof is [Main §3.4, Theorem (unavoidable hidden predictive memory); CT06]." (F3) |
| 96 | Corollary | §2, S-4 | OUTLINE S-4 verbatim |
| 98 | capacity and Pinsker bounds | §2, carried (nit 8) | r96 verbatim + "(in bits)" |
| 100 | (C1)–(C4) | §2, carried | r98 verbatim |
| 104, 106 | P-divisibility, criterion; Theorem 3 | §2, carried | r108, r110 verbatim |
| 108 | Theorem 3 status | §2, sketch table (r6-recheck nit 2) | OUTLINE text verbatim + r112 last sentence verbatim |
| 110 | stochastic-inverse lemma; readback | §2, S-5 (C5) | r114 s1 with "finite square" (C5) + S-5 verbatim + r114 last sentence verbatim |
| 112 | Appendix B pointer | §2, pointer (r6-recheck nit 4) | OUTLINE verbatim |
| 120–124 | §3.1 | §3.1 | r118 (pointers: §3.1 → §2.5, §4.2 → Appendix B), r120, r122 verbatim |
| 128–136 | §3.2: operational completion, Theorem 4, witnesses, qubit independence | §3.2 | r212–220 verbatim |
| 140, 142 | §3.3 relating evolution | §3.2 | r224, r226 verbatim |
| 146 | §3.4 finite carrier | §3.2 | r230 verbatim |
| 150 | Born exponent | §3.2, "one sentence pointing to r4:78" | **new wording** from register row BORN (F4) |
| 152 | Bell structure | §3.2 | r234 item (5) verbatim, from "a deterministic completion …", capitalized |
| 158 | Weinberg landing gate | §4 item 1 (O2) | OWNER marker |
| 159 | N-CC0 | §4 item 1 | OUTLINE verbatim |
| 161 | N-CC1 + qualifier | §4 item 2 | OUTLINE verbatim |
| 163 | N-CC2, N-CC3 | §4 item 3 | OUTLINE verbatim + "(Level G3 of [GR])" inserted at first use, per the outline's naming rule |
| 165 | N-CC4, N-CC5 | §4 item 4 | OUTLINE verbatim |
| 167 | N-CC6, N-CC7 | §4 items 5–6 | OUTLINE verbatim |
| 169 | N-LIT2 | §4 item 7 | OUTLINE verbatim |
| 171 | N-CC8 (closing caution) | §4 item 8 | OUTLINE verbatim: "Until then the proposal reinterprets the problem and does not resolve it." |
| 177 | BH setting | §5 item 1 (R3) | r172 s1–3 and s5 verbatim |
| 179 | V, B, D | — | **r176 s1 verbatim** (F5) |
| 181 | R11 marker | §5 markers | r178, updated to the R11 REVIEW verdicts |
| 182 | N-BH1 | §5 item 2 | OUTLINE verbatim |
| 184 | counts and endpoint guarantees | §5 item 2 (C2) | C2 text + r181 clauses restored + the [Sha79] sentence from r181 (F6) |
| 186 | R11 marker | §5 markers | r187, updated (ch07:126 s1–2; #936 A.8 shell) |
| 187 | N-BH2 | §5 item 3 (C1) | OUTLINE verbatim |
| 189 | R11 + H-decouple marker | §5 item 4 | r203, updated (GR:811; the H-decouple label pending #936) |
| 190 | N-BH3 | §5 item 4 (R2, C1) | OUTLINE verbatim |
| 192 | N-BH5 | §5 item 5 | OUTLINE verbatim |
| 200 | §6.1 implications | §6.1 (C3) + RECHECK-r7 nit 2 | N-DI1 verbatim + **one Bell sentence** (F7) |
| 204–211 | §6.2 items 1–8 | §6.2 | items 1, 2, 5: r238, r239, r242 verbatim. Item 3: r240 (pointer §3.2 → §3.1). Item 4: OUTLINE (R5 adapted, C1) verbatim. Item 6: r243 (§4.3 → Appendix B). Item 7: OUTLINE verbatim. Item 8: R12 verbatim |
| 215 | §6.3 decisive tests | §6.3, N-DT1 (r6-recheck nit 3) | OUTLINE verbatim |
| 217 | further open problems | §6.3 ("r4 §6.4 (1)–(4) remain") | "Further open problems are: " + r234 items (1)–(4) verbatim (pointer §3.1 → §2.5) (F8) |
| 221 | conclusion, sentences 1–2 | §6.4 | r249 s1 and s3 verbatim (s2, on memory, dropped for length: it restates §2.4–§2.5 and is not a qualification) |
| 223–224 | conclusion, consequences; R11 marker | §6.4 | **new wording** (F9); r251 marker |
| 226–234 | code, data and formal verification | back matter | r254–262 verbatim |
| 236–249 | Appendix A | back matter | r264–277 verbatim, with section pointers renumbered (Theorem 3 and readback §3.1 → §2.5; relating evolution §6.2 → §3.3; Theorem 4 and independence §6.1 → §3.2) |
| 251–290 | Appendix B (B.1, B.2, B.3) | back matter | r132–139, r143, r147–166 verbatim. r162's pointer §3.2 → §3.1. r164 gains the Pauli-twirl identity clause (F10) |
| 292– | References | back matter | r4 list. [Pag05] removed (β is removed). [EvEMU11], [KP14], [tH14] and [Vol06] added, each with a VERIFY |

## 2. Sentences beyond reviewed text or the register (flags)

Each is at or below the strength of its register entry.

| Flag | r5 line | Sentence or change | Basis |
|---|---|---|---|
| F1 | 30 | N-INT1 is inserted before r30's last sentence. r30's (§3.2) pointer sentence and its [Main] pointer sentence are both kept | The outline says N-INT1 "replaces r4:30's last pointer sentence". I kept both r4 pointer sentences, because one carries the operational-completion qualifier and the other carries the citation to the full derivations (owner direction). No claim is added |
| F2 | 42 | "This section defines three classes …, identifies what the coincidence leaves (where a law's memory must sit), and states what finite recurrence does with that memory. Each result is stated with its reference; the proofs are in the cited papers." | Structural; the owner direction (cite, don't re-derive) |
| F3 | 94 | "The written proof is [Main §3.4, Theorem (unavoidable hidden predictive memory); CT06]." | S-3's citation, put as a sentence |
| F4 | 150 | "The origin of the quadratic Born exponent is open: $p=\|U\|^2$ is part of the definition of $\mathsf Q_K$ and is not selected by the correspondence (§2.3) [Main §3.4; Bar26, Thm 3.1]." | Register row BORN; r78; r234's "origin of the quadratic Born exponent" open item. Not a repeat of r78 |
| F5 | 179 | r176 s1 (the V × B × D configuration space), verbatim | Not named in the outline. It is needed because §5 (N-BH3) and §6.2 item 4 use $D$, "the sector beyond the cosmological horizon" and "the rest of the visible sector". Reviewed text |
| F6 | 184 | **C2 merged with r181.** C2 gives "with the joint values U of the unread registers inaccessible, P_succ ≥ 1/\|U\|; 32 non-injective maps … violate this bound". r5 adds three things. (i) It restores r181's definition of $\mathcal M$ and its clause "so zero advantage in a bijective instance requires \|U\| ≥ \|M\|", which the retained [Sha79] sentence ("The bound is the remnant-capacity form …") refers to. (ii) It states the 32-map violation precisely as "violate the bound on $P_{\rm succ}$", because BH-01 REPORT:21 and :155 count violations of $P_{\rm succ}\ge1/2$ (RECHECK-r7 nit 1: :155 cited beside :21). (iii) It adds [BHa] | Reviewed r4 text and BH-01 REPORT:21, :155. No new claim |
| F7 | 200 | "Quantum Bell correlations are not accounted for by memory alone: with measurement independence kept, they need ontic parameter dependence, whose compatibility with operational no-signalling and the continuum limit is the open hypothesis H-Bell (§3.5)." | RECHECK-r7 nit 2 wording, **plus "with measurement independence kept"**. Without that condition, "they need ontic parameter dependence" turns the adopted branch into a necessity, the overclaim R2-1 removed. Register row BELL; r234 (5); Main:22 and :394 |
| F8 | 217 | "Further open problems are: " + r234 (1)–(4) | Lead phrase only |
| F9 | 224 | "Applied to vacuum energy, OI proposes that the zero-point sum of the emergent description is not a gravitational source, conditional on covariant field equations that are not derived; applied to black-hole information, it separates conservation from accessible recovery, while the framework's Page curve is not established. Neither application is a demonstrated resolution of its problem." | Outline §6.4 ("the two consequences as proposals with their conditions; 'neither application is a demonstrated resolution'"). Built from N-CC2, N-CC4, N-BH1, N-BH3 and N-INT1, at or below their strength |
| F10 | 288 | r164 + "by the identity $\sum_o\sigma_oX\sigma_o=2\operatorname{tr}(X)\,I$" | The owner's one exception (the step is not in the corpus). The source is ERRATUM-r4, recorded in an HTML comment beside the paragraph |

**Not a flag:**
- section renumbering of pointers inside carried r4 sentences;
- OWNER marker texts (updated to the R11 review verdicts);
- bibliography entries.

## 3. Markers in r5

- **9 OWNER markers:**
  - R11 at the abstract, §5 (×3, one carrying the H-decouple label pending #936), §6.2 item 4 and §6.4;
  - decision 2 / §A.42 at the Conventions;
  - the Weinberg landing gate at §4;
  - §A.42 retention at the code section.
- **9 VERIFY markers:** [BBS24], [Cal26], [CT06], [Har04], [Sha79], [tH14], [EvEMU11], [KP14], [Vol06].
- **The two approved raw LaTeX lines** are kept. `\begingroup\small\raggedright` sits before the Appendix A bullets,
  and `\endgroup` is the last line. Appendix B and the references sit inside the group.
- **The title** is the owner's; its hyphenation on p. 1 is pending (owner).

## 4. Build and checks

- **Build** (pandoc + xelatex, repository header):
  - 17 pp in all; 0 overfull boxes; 0 missing glyphs; median 2,601 characters per page.
  - The main text runs abstract–§6.4 on pp. 1–12: about 4,800 words, 12.0 rendered pages. That is inside the owner's
    10–12, at its upper edge, and above design r7's estimate of about 11.2 pp.
  - Code and Appendix A are on p. 13, Appendix B on pp. 14–15, and the references on pp. 15–17.
- **Repository checks,** on a fresh `git archive` of `687e885b` with r5 at `papers/Introduction.md`:
  `voice_check`, `claims_check` and `duplicate_check` are OK. `lean_manuscript_census` is OK but vacuous for this
  paper.
- **Identifier check:** `identcheck.py` finds 28 Lean identifiers, 0 unresolved and 0 Appendix A line mismatches.
- **§A.32/§A.33:** see the report. No hits apart from negations, Main's remark title, theorem names and Main's title
  in the bibliography.
