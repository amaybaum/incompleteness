## Editorial and presentation review: papers/Introduction.md at edac91c9 (PR #918)

Read-only. I made no edits, commits, pushes or comments. I rebuilt the paper in a scratch copy with `sh ./build.sh Introduction` at edac91c9. The result is 17 pages, the build is OK, and no glyphs were dropped. The rebuilt PDF text matches the committed `papers/Introduction.pdf`, and the `.tex` source-sha256 matches the `.md`, so the committed artifacts are current. Line numbers below refer to `papers/Introduction.md`; most paragraphs sit on one line, so a line number points to a whole paragraph. Items marked **[REVISER]** are places where the wording is ambiguous about scope or status; they are passed on for the scientific reviser to check, not proposed as changes.

### 1. Structure vs the brief

**Page map (17 pages, letter size, pandoc default margins):**

| Pages | Content | Approx. length |
|---|---|---|
| p1 to top of p2 | Title and abstract; the abstract runs about 6 lines onto p2 | 279 words |
| p2–3 | §1 | about 1.3 p |
| p3–6 | §2 | about 3.2 p |
| p6–8 | §3 | about 2.5 p |
| p8–10 | §4, cosmological constant | about 1.4 p |
| p10–11 | §5, black holes | about 1.3 p |
| p11–12 | §6 | about 1.8 p |
| p13 | Code section and App. A | about 1 p |
| p14–15 | App. B | about 1.2 p |
| p15–17 | References (40 entries) | about 2.6 p |

The text density is low and even, at roughly 2,400–3,300 characters per page (median about 2,850). There is no table-collapse artefact and no bare `---` rule.

**Mapping to the brief:**

1. **Central idea → §1.** §1.1 opens straight into the triple $(S,\varphi,V)$ and gives no plain-language "why". The motivating sentence ("Hidden states compatible with the same $x$ send it to different futures…") is buried at the end of line 20. *Should-fix:* put it first.
2. **Mathematical foundation and scope → §2 plus §3.2–3.4**, about 4.8 pages. This is the bulk of the paper. §3 is titled "Quantum emergence", but §3.2–3.4 (Theorem 4, the relating evolution, the qubit obstruction) are scope mathematics and belong with item 2.
3. **Physical interpretation → no section.** It is scattered across line 22, §3.1 (the three notions), §3.5 (Bell) and §6.1. *Should-fix:* collect these into one section. This is a reorganization, not new content.
4. **Illustrative examples → only in Appendix B.** The brief places them in the body before the black-hole section. *Should-fix:* promote B.1–B.3 to a body section. This is page-neutral.
5. **Black-hole information → §5.** This fits the brief.
6. **Limitations and open problems → §6**, plus scope statements repeated in every section.
7. **Not in the brief: §4 (cosmological constant, 551 words).** Whether to keep, condense or move it is an owner decision. It is the largest single cut available.

**Cuts toward 12–15 pages (estimates):**
- Condense §4 to about 180 words, or fold it into §6 as one paragraph: −1.0 p.
- Merge §6.1, §6.2 and §6.4 into one "Limitations and open problems" section plus a short conclusion. The 8 items of §6.2 restate the scope sentences of §§2–5, and the statement "Neither application is a demonstrated resolution" appears in the abstract, at line 26 and at line 191: −0.8 p.
- Abstract to about 200 words, which also lets it fit on p1: −0.3 p.
- Move Lean identifiers out of the body (lines 54, 82, 118, 126) into App. A only. Shorten the Main locators that carry full remark titles, e.g. "[Main §1.2, Remark (status of the early commitments)]" becomes "[Main §1.2]": −0.4 p.
- The Contributions paragraph (line 28) and the Attribution paragraph (line 60) duplicate the attribution of Theorem 1; keep it in one place: −0.2 p.
- Tighten §5's long paragraph (line 162): −0.2 p.

Together these give about 14 pages including references. A separate option is `geometry: margin=1in`, which alone gives about 12–13 pages. However, every other paper uses the default geometry, so that is an owner decision (optional).

### 2. Clarity edits by section

**Abstract (line 12)**
- *Should-fix* **[REVISER]**: "(each with one step not machine-checked)" leaves unclear which results "each" covers. Proposed: "(both proved on paper; each has one step without a machine check, §§2.4–2.5)".
- *Should-fix*: "Open are which of conditions (iii)–(v) a physical substratum supplies" uses labels the abstract never defines. Proposed: "Open are which of the last three completion conditions (adjoining an independent system, every composite unitary, fresh-ancilla attachment) a physical substratum supplies".
- *Should-fix*: abstract length. Compress the attribution sentence to "Its components are known (Egri et al.; Barandes); they are combined here into one theorem." Cut the cosmological-constant sentence to one clause.
- *Should-fix*: the abstract says "every deterministic completion carries…" while Theorem 2 says "every faithful realization". Use one term, or define "deterministic completion" as a faithful realization.

**§1**
- *Should-fix*, line 18: open with motivation. Proposed: "An observer inside a closed system registers only part of its configuration. If the whole evolves by a bijection, hidden states compatible with the same visible state send it to different futures, so the visible sector evolves stochastically. This is modelled by a triple…". Then delete the duplicate sentence at the end of line 20.
- *Should-fix*, line 26: the parenthetical "(where the candidate intermediate matrix exists, it has negative entries)" is unclear. Proposed: "(when the earlier transition matrix is invertible, the unique candidate intermediate matrix has a negative entry)". **[REVISER]**: check the scope of this statement.
- *Optional*, line 22: "The incompleteness is inaccessibility of the hidden sector, not…" becomes "Here incompleteness means the hidden sector is inaccessible; it is not the joint unsharpness…".
- *Optional*, line 30: move the definition "(S,φ) is the *substratum*" to §1.1, where $S$ and $\varphi$ are introduced.

**§2**
- *Must-fix*, line 72: the random variables are undefined. Add: "Let $X_t$, $H_t$ be the visible and hidden coordinates at time $t$, $X_{<t}=(X_0,\dots,X_{t-1})$; information is in bits." The total-variation norm is used at line 77 before total variation is named at line 90; define it here.
- *Should-fix*, lines 76–78: the theorem items render as bullets with a second marker "(a)". Render them as a plain (a)/(b)/(c) list and display (b), which currently breaks across lines.
- *Should-fix*, line 84: the indices switch from $t$ to $k$ ($X_{<k}$, $X_k$); use $t$. **[REVISER]**: "conditional past–future information reaches $I^*$" names a quantity that is never defined; say what $I^*$ is. Main §1.3 calls it the per-process bound of §3.4.
- *Should-fix*, line 86: "[Main §1.3] names four conditions…" opens a sentence with a citation. Proposed: "Four conditions on a hidden sector are named in [Main §1.3]: …".
- *Should-fix*, line 96: "routed-readback form of (C4)" is not defined here, and the word "routed" does not occur in Main, so the cited "[Main §1.3, the realization clause of (C4)]" will not show the term to a reader who follows it. Define it in one clause. **[REVISER]**: also check whether the abstract's "turns history readback into indivisibility" claims the history-level (proved-on-paper) form or the routed (machine-checked) form.
- *Optional*, line 98: "Appendix B works examples:" becomes "Appendix B works through three examples:".

**§3**
- *Should-fix*, line 100: the heading wraps to two lines. Proposed: "3. Quantum emergence: scope and open steps". Retitle §3.4 "No fixed finite realization reproduces a qubit" (see the "carrier" item in section 4 below).
- *Should-fix*, line 106: split this paragraph. Give the three notions as a list. Define CP-(in)divisibility at first use ("$\Phi_t=\Psi_{t,s}\circ\Phi_s$ with $\Psi_{t,s}$ CPTP") and define $\Phi_t$. **[REVISER]**: in "for them (2) implies CP-indivisibility", check whether "them" means all diagonal-preserving channels or only the channels obtained by tracing out a permutation unitary.
- *Should-fix*, line 114: one 160-word sentence chain. Split into "An operational theory specifies…", then "It is assumed closed under: (a)…(e)", then "The five completion conditions are: (i)…(v)", the last as an enumerated display. "ancilla level" and "spectator-independent local readout" need a gloss.
- *Should-fix* **[REVISER]**, line 120: "each condition is independent of the other four and of a fixed finite observation process satisfying (C1)–(C4)". It is unclear whether this means one fixed process or every such process.
- *Should-fix*, line 126: move the Lean names to App. A and define "fixed-basis datum", "root-conditioned" and "rooted families". **[REVISER]**: the statement introduced as "conversely" cites `rooted_eq_iff_slice_eq` "(forward direction)". Check that the direction label matches the direction stated (§A.34). Also check whether `gl2_…`/`gl3_…` at line 124 ("both machine-checked") are general statements or specific instances.

**§4**
- *Should-fix*, line 140: "(the mismatch)" is a term defined after a citation. Proposed: "…above the observational value; this discrepancy, here called the mismatch, depends in its exact power on the cutoff convention [Wei89…]".
- *Should-fix*, lines 144 and 146: display the two candidate completions and the target equation instead of running them inline; they currently break across lines on p9. See also the $\mathcal G$ vs $E$ and $T^{\rm cl}$ vs $T$ inconsistencies in section 4 below.
- *Should-fix* **[REVISER]**, lines 142 and 144: "OI's proposal is that the mismatch requires no cancellation" is asserted at line 142 and only made conditional at line 144. Under §A.30 (never assert-then-qualify), state the conditional at its first occurrence.
- *Should-fix*, line 144: "Level G3 of [GR]" is undefined here. Gloss it as "(covariant field equations with conservation and continuum limit)". Also gloss "dependency ladder" (line 162) and "[GR]'s ladder" (line 183).

**§5**
- *Must-fix* **[REVISER]**, line 160: the toy model is never set up. The reader is not told what the message is, what an "emission" or a "register" is, or which map is drawn from the 40,320. "32 non-injective maps … violate the bound on $P_{\rm succ}$" and "These endpoint guarantees are sufficient, not necessary" do not say what they are sufficient for. $P_{\rm succ}$ is undefined, and the message prior is not stated.
- *Should-fix*, line 162: a 450-word paragraph. Split it into setup; the result; the conditions as an enumerated list (H-scramble, H-decouple, single energy shell, time average at a fixed bipartition, field equations); and the remaining open items. **[REVISER]**: the paragraph states "For all but an exponentially negligible fraction … equals the Page value" before "This holds under H-scramble", and then says H-scramble fails in the aligned case. Put the conditions first.
- *Should-fix*, line 162 and line 175: "[GR App. A.7]" (a subsection) and "[GR, Thm A.7]" (a theorem) are easily confused. Thm A.7 is never introduced in this paper but is used at line 175. Name it ("the effective-pure-state theorem [GR, Thm A.7]").
- *Should-fix*, line 162: "$\mathcal C_B\times\mathcal C_R$" uses $\mathcal C_R$ without definition; $R$ is introduced only as a subsystem of $V$.

**§6**
- *Should-fix*: merge §6.1, §6.2 and §6.4 (see the cuts in section 1). §6.2 can shrink to about 4 items that are not already stated where each result is derived.
- *Should-fix* **[REVISER]**, line 185: "ledger bits", "the fixed-dimension form is false", "exact gluing for recurrent target families" and "(C2) necessity" are undefined. Gloss each or cite a locator.
- *Should-fix*, line 183 and line 22: "no memory-witness constraint" and "no test … at the level of memory witnesses" both use "memory witness", which is never defined. Give it one gloss.

### 3. Voice (§A.32/§A.33)

The caps regex outside acronyms finds no hits in rendered prose, and the history-phrase family ("no longer", "now", "corrected", "formerly"…) finds no hits.
- *Must-fix* (§A.27 manuscript voice, §A.28 process leakage), lines 281, 291, 295, 303, 307, 313, 335, 337, 339, 341: HTML comments in the reference list contain internal audit vocabulary and paths ("VERIFY", "AUDIT r4 P3.3", "Read first-hand", "science re-check", "BH-01 package", `verification/audits/.../FINDINGS.md, sha256 …`). They do not render in the PDF, but they are public source. Move them to the audit records. **[REVISER]**: three of them say the cited content was never read: [CT06], [Har04] (cited second-hand via Mon08) and [Sha79].
- *Should-fix* (§A.32 meta-commentary), line 179: "What the paper states are the cited theorems and their scopes." Delete it.
- *Should-fix* (self-assessment / process vocabulary), lines 267 and 269: "internally reviewed" in [BHa]/[BHb]. Proposed: "unpublished; proofs and code at `…/bh01_access_v1/`".
- *Should-fix* (labels a reader cannot resolve), line 162: "[BHa, item F]" and "[BHb, C1, C6(a)–(d)]" point to item labels of unpublished records. Either describe the content, or make sure the records expose those labels.
- *Optional*, line 28: "The paper claims no new theorem or physical result; its contribution is expository." This is acceptable as a scope statement. A more neutral form: "No new theorem is claimed; each result is attributed where stated."
- *Optional*, lines 26, 152, 191 and the abstract: "is not a resolution / does not resolve it" appears four times. These are status statements, not violations, but keep one per application.
- Line 5, "DRAFT PRE-PRINT": this is the corpus convention (GR uses the same line). No change needed.

### 4. Notation and definitions

- *Must-fix*: **Λ** means two things. It is the stochastic divisor in lines 90, 232 and 247 (math `\Lambda`) and the cosmological constant in lines 146, 150 and 178 (raw Unicode Λ). Rename the divisor, e.g. $\Delta_{s,t}$.
- *Must-fix*: **h** also clashes. It is the hidden configuration in §1.1 and B.1, but the *visible* hole card in B.3 (line 236), where the hidden card is $b$. Rename the hole card $x$. B.3 also needs to state the encoding red=0, black=1, which line 249 ($b=1-h$) and line 253 ($|0\rangle\langle0|$) both use.
- *Should-fix*: **p** is overloaded. It is a history at lines 72–77, the Born exponent $|U|^p$ at line 66, the probability $p=|U|^2$, and $p_0$ at line 84. Use $\omega$ (or $x_{<t}$) for histories.
- *Should-fix*: $n$ in "one-step $n^2$-dimensional ancilla dilation" (line 60) is undefined; presumably $n=|\mathcal C_V|$.
- *Should-fix*: the gravitational side is written $\mathcal G_{\mu\nu}$ at line 144 and $E_{\mu\nu}[g,\mathrm{OI}]$ at line 146; the source is $T^{\rm cl}_{\mu\nu}$ at line 144 and $T_{\mu\nu}$ at line 146. The subscript $C$ in $\rho_C$ is unexplained. $\Omega_\Lambda$ is undefined (line 178).
- *Should-fix*: the class $\mathsf Q_K$ is named "fixed-basis Born records", "fixed-basis unitary Born laws" and "fixed-basis statistics". Its objects are called realization, faithful realization, deterministic completion, substratum, carrier (§3.4 heading, line 118) and lift. Fix one term per object.
- *Should-fix*: acronyms and terms used undefined: CP (line 106), CHSH (136), QM (App. A, line 215), TV (used at line 77 before it is defined), "unistochastic" (line 60), $\delta_a$ (line 90), "overlap in a column" (Theorem 3), $\Phi_{t_1}$ (line 106), "spatial coupling graph" (line 136).
- *Optional*: the Corollary at line 82 is set in roman while the theorems are italic; make the theorem style consistent.

### 5. Typesetting / PDF

- No dropped glyphs and no overfull boxes. The microtype "unknown slot" warnings come from the shared header and are benign.
- *Should-fix*: the `\begingroup\small\raggedright` at line 206 is closed only at line 343. Appendix B, including its mathematics and the table, and the References are therefore all set small and ragged-right. Close the group after the App. A list; reopen it for the references if wanted.
- *Should-fix*: the abstract spills onto p2. It fits on p1 once cut to about 200 words.
- *Should-fix*: long inline formulas break across lines: Theorem 2(b) on p5, and the field equations in §4 on p9. Display them.
- *Optional*: two underfull lines. One is in the Attribution paragraph (line 60). The other is at line 195, where the 40-character hash `17b830bcd0ecc…` is plain text while `17b830bc` is in code font elsewhere. Use the short hash in code font for consistency.
- *Optional*: the B.3 table has no caption. "street" and "showdown" are poker terms that are only partly glossed.

### 6. Citations

- All 40 reference keys are cited in the text, and every in-text key resolves to an entry, with no orphans either way. The list is alphabetical by key.
- *Should-fix*: [BHa] has an unquoted lowercase descriptive title, while [BHb] has a quoted title. Make them match.
- *Optional*: locator punctuation is mixed: "[Bar25, p. 12; Bar23 §4.3]", "[GR, Thms A.8–A.9]" vs "[GR App. A.7]". The de facto rule (no comma before §/App., comma before Thm/Prop./p.) could be applied consistently. The key style also varies: [Milz20] and [Mathlib20] use the full name, while the rest use initials or abbreviations plus a 2-digit year.
- I did not check whether the cited Main/GR section and remark locators exist, beyond noting that "routed" is absent from Main.
- Note for the owner, optional: [Main]'s title, "The Equivalence of Quantum Mechanics and Embedded Observation", sits uneasily beside this paper's §6.2 item 1 ("No derivation of quantum mechanics"). The paper's own title, "…to Quantum Observations", could be read as broader than the fixed-basis scope. **[REVISER]**
