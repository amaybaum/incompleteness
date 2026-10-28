## Citations and novelty check: Introduction paper (PR #918)

I checked `papers/Introduction.md` at `edac91c9` (343 lines) against `main` at `55e3217b`. Nothing was edited, committed, pushed or posted. I read the novelty-v5 conclusions first (`novelty-v5/AUDIT.md` §3 and §7, `RECHECK-r4.md`, `draft/review/references/FINDINGS.md` and `WEI89.md`). I verified the bibliography against arXiv API and Crossref metadata only; no PDFs were fetched.

**Summary:** the paper honours novelty-v5 for everything that audit covered. But the corpus pin is stale since the #947–#955 merge, and one open problem is stale with it. Theorem 4 (§3.2) and the §3.3 lift results carry no literature attribution, and novelty-v5 never examined them. Every bibliography entry exists as cited; the only gap is Calvo's journal version.

### MUST-FIX

**M1. The corpus pin is stale (lines 259 and 195).** The references cite the corpus "repository commit `b64919cd`", and line 195 says the Lean sources are identical "at the corpus commit `b64919cd`". The branch has since merged `55e3217b`. Between those two commits `papers/Main.md` changed by 178 lines (#947–#955), and GR, ch01, ch07 and ch18 changed too. Cited targets moved in that window:
- the process-dilation rational class (#948);
- the two forms of (C2) (#953);
- the readback-lemma title, now "accessible conditional memory from readback";
- the new variational Remark (#949, see M2).

`verification/lean-mathlib/` is unchanged between the two commits, so the Lean statement stays true.
- Proposed text: replace `b64919cd` with `55e3217b` (or the landing base) at lines 195 and 259.

**M2. Open problem (2) in §6.3 is answered in Main (line 185).** The paper lists "(2) whether the minimal hidden predictive memory equals $M_t$ once ledger bits that cannot influence the future are quotiented (the fixed-dimension form is false) [Main §3.4]". That was open at `b64919cd` (Main:594 there: "leaving open only the variational VALUE question"). At `55e3217b`, Main:610 "Remark (a variational question)" settles it:
- over deterministic completions the infimum is $I(X_{<t};X_{>t}\mid X_t)$, attained by the canonical predictive quotient;
- it equals $M_t$ exactly when $I(X_{<t};X_{>t+1}\mid X_t,X_{t+1})=0$;
- every bijective completion has $H(X_{<t}\mid X_t)$.

Proposed text: delete item (2) and renumber. Optionally add to §2.4: "Over deterministic completions the least value of $I(X_{<t};H_t\mid X_t)$ is $I(X_{<t};X_{>t}\mid X_t)$, attained by the canonical predictive quotient; it exceeds $M_t$ unless $I(X_{<t};X_{>t+1}\mid X_t,X_{t+1})=0$ [Main §3.4, Remark (a variational question)]." Keep Main's own scope on that sentence: kernel for bijective completions, on paper for the non-injective step.

**M3. Theorem 4 (lines 12, 28, 116–120) is presented without attribution of its standard ingredients, and its novelty was never audited.** novelty-v5 has no entry for the operational-completion characterization. Its sufficiency direction is the measurement-model fact that every Kraus instrument is a unitary on system plus ancilla, followed by ancilla readout, coarse-graining and discard (Stinespring 1955; Kraus 1983; Ozawa 1984). The "five conditions" framing also invites comparison with Hardy's five axioms and the other operational reconstructions. Line 28 ("The results of §3.2–§3.3 are proved in [GR] and [Main]") reads, by contrast with the attributed items before it, as a claim of the corpus's own results. That conflicts with the owner's rule and with "claims no new theorem".
- Proposed text after line 118: "The sufficiency direction rests on the Stinespring dilation and the realization of every finite instrument by a unitary interaction with an ancilla followed by ancilla readout and discard [Sti55; Kra83; Oza84]; for operational reconstructions of finite quantum theory from axioms see [Har01; CDP11; MM11]. The novelty of the characterization and of the independence result has not been assessed."
- Line 28: append "; their novelty has not been assessed."
- New references:
  - [Sti55] W. F. Stinespring, *Proc. AMS* **6**, 211 (1955).
  - [Kra83] K. Kraus, *States, Effects, and Operations*, LNP 190 (Springer, 1983).
  - [Oza84] M. Ozawa, *J. Math. Phys.* **25**, 79 (1984).
  - [Har01] L. Hardy, arXiv:quant-ph/0101012.
  - [CDP11] G. Chiribella, G. M. D'Ariano, P. Perinotti, *Phys. Rev. A* **84**, 012311 (2011).
  - [MM11] Ll. Masanes, M. P. Müller, *New J. Phys.* **13**, 063001 (2011).

### 1. Reference integrity

All 35 external entries exist with the authors, titles, venues, years and arXiv ids given. Checked on arXiv: Bar23, Bar25, Bar26 (arXiv:2608.04354v1, 2026-08-05), BB12 (v5), BBS24, BD16, BJA17, BLP09, Cal26, Dou26 (v3 is current), EGGH26, EvEMU11, GH03, HKLP24, KP14, Milz20, Mon08, Pag93, Pag13, Pen20, RHP14, Sch21, SGD19, tH14 and Vol06. Checked on Crossref: Haw76, Har04 (pp. 267–276), Bel64, CHSH69, Sha79, dMU21 (LNCS, pp. 625–635), Mathlib20 (CPP 2020, pp. 367–381) and Wei89 (pp. 1–23).

Discrepancies and incompleteness:
- **Cal26 (line 291, should-fix):** the journal version is out. Add "*Quantum Stud. Math. Found.* **14**, 2 (2026), doi:10.1007/s40509-026-00415-9" (Crossref, issued 2026-10-24). Keep the arXiv v2 pinpoint: the journal body was not read.
- **tH14 (line 337, optional):** a Springer book version exists, *Fundamental Theories of Physics* 185 (2016), doi:10.1007/978-3-319-41285-6, and Main [1] cites the book. Cite the book with arXiv:1405.1548v3 so the two papers agree.
- **BJA17 (optional, no error):** the arXiv v2 title differs ("…of bijective non-completely-positive-divisible dynamics"). The PRL title given in the paper is correct.
- **Bar25 (optional):** add doi:10.31389/pop.186. "p. 12" (line 60) is arXiv v3 pagination; say so.
- **LP17 (optional):** the 2nd edition (AMS 2017, "with contributions by E. L. Wilmer") has §1.2 "Random Mapping Representation". The audit's "LPW Prop. 1.5, book p. 6" may be the 1st edition. Confirm the numbering against the 2nd edition actually cited.
- **Sch21:** arXiv only; no journal version found.
- **Unverified content (should-fix before release):** CT06, Har04 and Sha79 still carry VERIFY comments.
  - HKLP24's "Thm 4" pinpoint (line 130) is not first-hand: the audit lists [55] as NR (C14 PROVISIONAL). Read it or drop the "Thm 4".
- **Source comments (should-fix):** the HTML comments at lines 281, 291, 295, 303, 307, 313, 335, 337, 339 and 341 carry internal paths, sha256 digests and audit labels. These are process artifacts in a public manuscript (§A.27, §A.28). Move them to the audit record.

### 2. Attribution and novelty against novelty-v5

These items honour the audit:
- **Theorem 1 components** (lines 12, 28, 60): EGGH26 Props. 13/16, LP17 Prop. 1.5 (random mapping), Bar25/23/26 (permutation as unistochastic), Bar26 Thm 3.3 and Sch21 Thm 2 (one-step dilation), SGD19 Eq. (3). Milz20 and SGD19 are described as studying Kolmogorov consistency, as the audit asks.
- **Expository positioning** (line 28): matches §7's "technical perspective / pedagogical review".
- **Withdrawn and candidate items are absent:** C4-old, C12 as a characterization of non-Markovianity, and C8-R (no priority sentence) do not appear.
- **§2.4 bounds** are credited to data processing and Pinsker (C10, C11 and C9 are REFRAMING).
- **Divisibility mechanism:** RHP14 Thm 2.4 and BD16 Prop. 1, with Dou26 Prop. 1 as concurrent.
- **Stochastic-inverse lemma:** BB12.
- **XOR example (B.2):** RHP14 Eq. (15), with Dou26 App. A as concurrent.
- **Backflow measures:** BLP09 as a one-way witness; BJA17 with its bijective scope.
- **Bell/CHSH:** Bel64 and CHSH69.
- **Qubit no-go:** GH03, Mon08, and Hardy as reported in Mon08.
- **Card-game memory:** BBS24.
- **Cosmological alternatives:** EvEMU11, KP14 and Vol06.
- **Black-hole results:** "novelty not established" for BHa/BHb.
- **Birkhoff–von Neumann:** not used in the paper, so nothing to attribute.

Should-fix:
- **S1. Abstract (line 12).** It states the two memory results as "the discriminating content" with no hint that they are elementary. novelty-v5 §7's form is "Two elementary consequences do discriminate. By the data-processing inequality…" and "an elementary combination of finite recurrence with the contraction property … (RHP14; BD16)". Proposed: "…the discriminating content concerns memory: by the data-processing inequality every deterministic completion carries the visible memory in its hidden state, and, by the contraction property of stochastic maps, finite recurrence turns history readback into stochastic indivisibility somewhere in the recurrence cycle on a fixed finite reversible system (each with one step not machine-checked)."
- **S2. Theorem 3 (lines 92–94).** Novelty-v5 classes it KNOWN (C8: the contraction property used once). The header attributes it only to "[Main §2.3]", which states a narrower result: uniform prior, $s=1$, $T$ not a permutation (Main:115–129). The general rooted overlap form is kernel-only (census `manuscript: []`).
  - Proposed header: "**Theorem 3** (recurrence and overlap; an application of [RHP14, Thm 2.4])".
  - Proposed line 94: "…machine-checked in its rooted form; [Main §2.3] proves the uniform-prior case with $s=1$. Doukas states the same overlap-and-return argument concurrently [Dou26, Prop. 1]."
- **S3. §3.3 (lines 124–126).** The non-uniqueness of coherent lifts, deformable by a right action invisible to the visible law, is the familiar freedom of Stinespring dilations and Kraus representations. Main:212 also credits "the lift structure and its divisibility mechanics" to Doukas [22]. Proposed: "Unitary dilations of a channel are unique only up to an isometry on the ancilla [Sti55]; for the lift structure of the stochastic–quantum correspondence see [Dou26]." Optionally cite Barandes's gauge freedom (Bar25), after checking its section.
- **S4. §3.1 Hadamard example (line 106).** The observation that CP-divisible (Markovian) coherent dynamics can yield non-classical, non-divisible fixed-basis statistics is the subject of SGD19 Thms III.1–III.2 and of Milz20 (coherence generation and detection). Proposed after the example: "Coherence-generating Markovian dynamics producing non-classical fixed-basis statistics is studied in [SGD19; Milz20; SEDPH19]." Also cite Milz–Kim–Pollock–Modi 2019 for the CP-divisibility ≠ Markovianity point.
  - [SEDPH19] A. Smirne, D. Egloff, M. G. Díaz, M. B. Plenio, S. F. Huelga, *Quantum Sci. Technol.* **4**, 01LT01 (2019).
  - [MKPM19] S. Milz, M. S. Kim, F. A. Pollock, K. Modi, *Phys. Rev. Lett.* **123**, 040401 (2019), which is Main [10].
- **S5. B.1 (line 228).** The multi-time Markov test is Main's "Pollock et al. [7]" check, without the citation. Add "[PRFPM18]": Pollock, Rodríguez-Rosario, Frauenheim, Paternostro, Modi, *Phys. Rev. Lett.* **120**, 040405 (2018).
- **S6. §5 (line 162).** "For all but an exponentially negligible fraction of initial conditions" is measure concentration. Novelty-v5 C16c says the A.8 step sits "on top of Popescu–Short–Winter". Add "[PSW06; HLW06]":
  - S. Popescu, A. J. Short, A. Winter, *Nature Phys.* **2**, 754 (2006);
  - P. Hayden, D. W. Leung, A. Winter, *Commun. Math. Phys.* **265**, 95 (2006).

Optional:
- Line 136: the parameter-independence / outcome-independence vocabulary is Jarrett (*Noûs* **18**, 569, 1984) and Shimony (1986). Measurement-independence relaxations: Hall, *PRL* **105**, 250404 (2010). Bohm 1952 is the standard deterministic theory with parameter dependence.
- Line 148: the identity between the cutoff mismatch and the de Sitter entropy is known. Cohen–Kaplan–Nelson, *PRL* **82**, 4971 (1999); Padmanabhan, *Phys. Rep.* **380**, 235 (2003).
- Line 160: add Blakley 1979 (AFIPS NCC **48**, 313) beside Sha79, and read Sha79 or soften the line.

### 3. Internal citations against `main` at `55e3217b`

These exist with the cited number and name:
- §1.2 Remarks "status of the early commitments" (Main:62) and "the measure as a realization datum" (:60).
- §1.3 (C1)–(C4) (:70–80).
- §1.5, including the corollary content (:99).
- §2.3 Theorem "history readback + finite recurrence implies indivisibility" (:137); the Pinsker bound is Lemma "accessible conditional memory from readback" (:167).
- §2.4, the six-state model (:178).
- §3.1, the $n^2$ dilation (:208).
- §3.2: Theorem "CP-indivisibility, framework scope" (:326), Remarks "scope: P-indivisibility is not quantum non-Markovianity" (:330), "three notions, kept apart" (:334) and "failure of (C1)" (:286).
- §3.3 H-Bell (:410).
- §3.4: Theorems "finite-horizon process dilation" (:512), "finite-horizon stochastic–reversible–unitary equivalence" (:542) and "unavoidable hidden predictive memory" (:598); Remarks "representation, not explanation" (:632) and "scope: representability, not selection of the relating evolution" (:640); Proposition "finite-substratum operational obstruction — classical-dimension form" (:554); the uncertainty-relation sentence (:588); the Born exponent (:550); gluing (:634).
- §4.5 memory-witness test and BBS (:718).
- GR §2.2 (:52), §3.3 Theorem (:218–220), §6.2 and Level G3 (:356, :581), App. A.1, A.6, A.7 with Thms A.7–A.9 (:811–845), and H-scramble/H-decouple.
- Book §1.11 (ch01:265), §7.6 (ch07:108) and §18.5 (ch18:128).
- No Explainer citation remains.

Broken, mis-aimed or stale:
- **Line 64 (should-fix): wrong target.** "[Main §3.4, Remark (the conditions are diagnostics, not hypotheses)]" (Main:612) is about (C4) coinciding with condition (ii). It is not about Markov laws lying in all three classes. Point to "[Main §3.4, Remark (what this equivalence does and does not say)]" (Main:546: "Markov and memory-bearing laws alike lie in $Q_{\mathrm{fb}}$") or to [Main §1.5].
- **Line 92 (should-fix):** see S2; the target is narrower than the theorem cited.
- **Line 56 (should-fix): wording differs after #948.** Main:512 states the class as laws whose conditional kernels at positive-probability histories are rational. Main:514's response-table extension gives an independent prior for arbitrary real kernels. Proposed: "For a law whose conditional kernels at positive-probability histories are rational, and by the response-table extension for every law, a realization whose hidden prior is independent of $x_0$ also exists [Main §3.4, Theorem (finite-horizon process dilation) and its Extension]".
- **Lines 86 and 185(4) (should-fix): (C2) now has two forms (#953).** Main:76 defines (C2-structural) and (C2-slow); Main:496 makes only "the timescale (slow-bath) form of the C2 necessity direction" conditional on the mixing hypothesis. Proposed for 185: "(4) necessity of the slow-bath form of (C2), (C2-slow), which is conditional on a hidden-sector mixing hypothesis motivated by eigenstate thermalization [Main §2.3, §3.4]". Line 86's "(C2) is a physical-regime premise" still matches Main:72.
- **Line 185(2) (must-fix):** see M2.
- **Line 96 (optional):** "[Main §1.3, the realization clause of (C4)]" resolves to the "Realization —" status note of (C4) at Main:80, the cosmological read-write cycle. That is acceptable. Main states the routed form nowhere, so the kernel declaration is the only anchor for it.
- **Line 134 (optional):** Main:20 names the Born exponent as a frontier item in §3.1, so cite "[Main §3.1, §3.4]".
- **Line 136 (optional):** Main §3.3 after #950 states the hypotheses as "measurement independence plus ontic parameter independence" for a "response-complete deterministic completion". Align "pointwise causal cones and a setting-independent pre-setting ensemble" with that wording.
- **Line 84 (optional):** name the lemma: "[Main §2.3, Lemma (accessible conditional memory from readback); CT06]".
- **Outside the paper, for the owner:** GR §6's heading is "Dissolution of the Cosmological Constant Problem". The paper cites GR §6.2 and says "proposal, not a resolution", a status mismatch under §A.25.

### 4. Missing citations a referee would expect, ranked

1. Stinespring, Kraus, Ozawa; Hardy 2001, CDP 2011, Masanes–Müller 2011, for Theorem 4 (M3). Must-fix.
2. Shalizi–Crutchfield, *J. Stat. Phys.* **104**, 817 (2001), Thm 5 ($E\le C_\mu$), contrasted with Theorem 2 and the capacity bound. novelty-v5 §7 lists this as needed related work. Proposed after line 84: "The asymptotic, stationary analogue for minimal prescient states is $E\le C_\mu$ [SC01, Thm 5]." Should-fix.
3. Island and QES literature, since line 162 mentions islands with no island citation. Almheiri, Engelhardt, Marolf, Maxfield, *JHEP* **12** (2019) 063; Almheiri, Mahajan, Maldacena, Zhao, *JHEP* **03** (2020) 149; review: Almheiri et al., *Rev. Mod. Phys.* **93**, 035002 (2021). Should-fix.
4. Hayden–Preskill, *JHEP* **09** (2007) 120, for recovery from accessible radiation in §5; optionally Harlow, *Rev. Mod. Phys.* **88**, 015002 (2016). Should-fix.
5. PSW06 and HLW06 (S6). Should-fix.
6. Pollock et al. 2018 and Milz–Kim–Pollock–Modi 2019 (S4, S5). Should-fix.
7. Martin, *C. R. Physique* **13**, 566 (2012), for §4 line 140. A referee will note that the Planck-cutoff $\Lambda^4$ estimate breaks Lorentz invariance ($\rho\neq-p$); a Lorentz-invariant regularization gives $m^4\ln$ terms. Padmanabhan 2003 is optional. Should-fix.
8. Spekkens, *PRA* **75**, 032110 (2007), for the epistemic-restriction precedent in §6.2 item 8; optionally Harrigan–Spekkens, *Found. Phys.* **40**, 125 (2010). novelty-v5 marks this pending. Optional.
9. Jarrett 1984 / Shimony 1986 / Hall 2010 (§3.5). Optional.
10. Chiribella–D'Ariano–Perinotti, *PRA* **80**, 022339 (2009), comb realization. This is the one unread area behind novelty-v5's PROVISIONAL mark on Theorem 1's packaging. No novelty is claimed, so it is optional, but it should be read before any packaging claim.
11. Capela et al., *Phys. Rev. Research* **2**, 013350 (2020), the four-time parity version, in B.2. Optional.
12. Leggett–Garg, *PRL* **54**, 857 (1985); optionally Emary–Lambert–Nori, *Rep. Prog. Phys.* **77**, 016001 (2014). One sentence: every-step fixed-basis records are jointly distributed, so they satisfy every Leggett–Garg inequality. That sharpens §6.2 item 1. Optional.
13. Pimenta, arXiv:2505.08785 (Main [14]), with its two-configuration scope. Optional.

Sources (bibliographic lookups only): export.arxiv.org API and api.crossref.org records for the DOIs and arXiv ids above; [Levin–Peres 2nd ed. page](https://pages.uoregon.edu/dlevin/MARKOV); [arXiv:2106.03513](https://arxiv.org/pdf/2106.03513) (listing only, no journal reference found).
