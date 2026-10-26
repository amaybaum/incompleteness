# Scientific review: Introduction r5 (rescoped draft)

- **Object.** `draft/Introduction-r5.md` at `423e83da` on #918, sha256 `c538d9e1…5c24` (verified), together
  with `draft/CHANGES-r5.md`.
- **Design.** OUTLINE-r7, CLAIMS-r7 and DEPENDENCIES-r7.
- **Sources.**
  - Main, GR and the book at `687e885b` (`S/paper/mainwt`).
  - The BH-01 and BH-02 packages.
  - #936 at `b61cbaa9` (`S/bhfix/wt`): DIFF-REVIEW §6 and R1, DIFF-RECHECK N1, and GR:811–851 as corrected there.
  - The kernel (`OIBridge`).
  - arXiv API abstracts for the four new references (`sci-review/dl/r5.xml`).
- **Read-only.** No repository file was changed. Git ran with `-c gc.auto=0 -c maintenance.auto=false`.

## Verdict: ACCEPT WITH CHANGES

Two one-line changes are required:
- **C1** brings a literature sentence back to abstract strength, the VERIFY rule's condition.
- **C2** removes a tension with "claims no new theorem".

On the main questions:
- Every cosmological-constant and black-hole sentence names its open conditions, and none reads as a
  resolution.
- Theorems 1–4 and the Corollary keep their exact statements, hypotheses, status words and §A.34 witnesses.
- F1–F10 are at or below their basis. F7 is right.
- No overclaimed corpus site is leaned on.

***

## 1. Claims against sources

### §4, the cosmological constant

Every sentence states a condition or carries the content of a citation. Checked against GR:12, :356 and
:360, and §6.3:

| r5 | Claim | Source and verdict |
|---|---|---|
| l.159 | about 120 orders of magnitude, depending on the cutoff convention | GR:340 (10¹²² with GR's convention). Standard. Weinberg landing gate O2 is marked |
| l.161 | a uniform shift changes no visible transition probability, so the offset has no content in the visible statistics | GR:356 ("invariant under Ω_eff → Ω_eff + CI (a global phase)"). The "familiar statement" framing is correct and claims no novelty |
| l.163 | open coupling step (Level G3); the two completions differing by ρ_C g_μν; "conditional on that open step" | GR:356 sentences 1–4 and GR:12's ladder. This is the anchor DEPENDENCIES requires, and it stays short of the "never enters / no mechanism needed" overclaim |
| l.165 | under the GR target form $E_{\mu\nu}[g,\mathrm{OI}]=8\pi G(T_{\mu\nu}-\mathcal F g_{\mu\nu})$, with classical stress-energy as the source, the zero-point sum is not a source; the remaining vacuum term is not computed; Λ is an input; $H^2/G$ is the Friedmann normalization | GR:12 (the target form "under which the distinct-descriptions argument becomes a theorem") and GR:360 (initial conditions). This is the conditional form. It correctly does not use GR:366's "the value the framework expects" |
| l.167 | the mismatch equals $S_{\rm dS}$ up to a convention factor, as a dimensional identity; phase transitions are open | Matches `cc.py` and AW-3. It does not lean on GR:581 |
| l.169 | TFE, sequestering and Volovik | Checked against the arXiv abstracts. TFE and Volovik are at abstract strength. **KP14 is slightly above it: see C1** |
| l.171 | "would turn the proposal into a theorem or refute it … reinterprets the problem and does not resolve it" | The correct closing caution |

### §5, black holes

Checked against the BH-01 and BH-02 REPORTs and against #936.

| r5 | Claim | Verdict |
|---|---|---|
| l.182 | conservation by premise; conservation neither implies nor is necessary for accessible recovery | BH-01 claim A (REPORT:17, :36). The bijection is stated as a premise, as it should be |
| l.184 | 1,376 of 40,320; complete access gives exact recovery; $P_{\rm succ}\ge1/\lvert\mathcal U\rvert$; $\lvert\mathcal U\rvert\ge\lvert\mathcal M\rvert$; 32 violators; sufficient, not necessary | BH-01 REPORT:18, :21, :24, :155. Exact |
| l.187 | the Page value enters only via H-scramble, which fails from a definite configuration; the full-product shell gives $S_{\rm Page}$; on a proper shell it "differs in general", with a shell-dependent direction | BH-02 C1 and C6(a)–(c). "Differs in general" is at DIFF-RECHECK N1's corrected strength: it does not say "only when" |
| l.190 | closure of B∪R in a pure joint state, with no coupling to D or V∖R, over whole cycles; timescale ordering does not supply it (≥10⁵⁷); the value is established only on the full-product shell; a fixed-bipartition time average; the single-trajectory curve open; conditional on the covariant field equations; "not resolved" | This is #936 DIFF-REVIEW R1's accepted H-decouple definition, in words, with the label correctly withheld. It also matches GR:811/:843/:851 at `b61cbaa9`, BH-01 item F (lower bound 1.785×10⁵⁷), BH-02 C6(c)–(d) and GR:12's G4. All four of #936's points are carried, and every condition is named |
| l.192 | GSL not derived; QES agreement not established; islands conjectural | Correct |

**§6.2 item 4 and the §6.4 conclusion** restate §5 at or below its strength. They also keep R2-3's three
item-F limits.

### Elsewhere

- **§1–§3** are carried r4 text, reviewed before; the pointers are renumbered correctly.
- **§6.3** "(C4) at the cosmological partition [GR §2.2]" matches GR:52, "(C4) is therefore a named realization
  condition … Not presently [discharged]".
- **§6.2 item 7** ("no prediction of Λ or Ω_Λ") is consistent with l.165.
- **Appendix A** is unchanged. The drafter's identcheck found 0 mismatches.

## 2. Theorems and the Corollary

- **Theorem 1** (l.58–64) is unchanged. The `S_imp_D`, `D_imp_Qfb` and `Qfb_imp_S` inclusions plus the
  compositions meet §A.34.
- **The realization sentence** (l.66): "For a law with rational probabilities, a realization whose hidden
  prior is independent of $x_0$ also exists [Main §3.4, Theorem (finite-horizon process dilation)]; proved on
  paper, with exact probes". The hypothesis is right for the theorem cited: Main:496 states it for a rational
  multi-time law. Main's response-table extension (Main:498) removes rationality, so the sentence understates
  without overclaiming (nit N1). EGGH26 Prop. 13 is correctly attached to the S ⊆ D construction.
- **Theorem 2** (l.88–94): "machine-checked for a joint law" and "time-$t$ identification not machine-checked"
  are kept. The added written-proof citation is correct.
- **The Corollary** (l.96): "proved on paper", with both directions named: forward by Theorem 2(a) in each
  realization, converse by Theorem 2(a) in one realization, supplied by `S_imp_D`. The vanishing criterion is
  labelled "not machine-checked" [CT06]. This meets §A.34.
- **The bounds** (l.98): capacity is machine-checked; Pinsker's bound, "in bits", is proved on paper with
  exact probes. Correct.
- **Theorem 3** (l.106–108) keeps its exact statement and its hypotheses (a bijection of a finite set,
  overlap at s, return at n > s), and says "machine-checked in its rooted form". Dropping the proof sketch
  loses no hypothesis: finite order and overlap are still stated in the theorem and in l.110.
- **The stochastic-inverse lemma** now says "finite square", which matches `Matrix n n`. The readback theorem
  cites Main's title verbatim (Main:137) and keeps the routed-versus-history-level status split from r3.
- **Theorem 4** (l.132–134) is unchanged, with both direction witnesses and "nonempty".
- **§3.3** is unchanged (RC-5).

## 3. F1–F10

| Flag | Verdict |
|---|---|
| F1 | No claim added. The wording is odd, though: the foundation is called one of OI's "two consequences" next to "two applications" (nit N2) |
| F2 | Structural. Correct |
| F3 | Correct citation |
| F4 | Correct: the Born exponent's origin is open (Main §3.4; Bar26 Thm 3.1) |
| F5 | Reviewed r4 text, and needed for D |
| F6 | Exact (BH-01 REPORT:21, :155) |
| F7 | **Confirmed.** "With measurement independence kept, they need ontic parameter dependence" is the correct conditional. A deterministic completion with pointwise cones *and* measurement independence is Bell-local (Main:22, :82), so parameter dependence is needed only given measurement independence. Main:396 records measurement dependence as "recorded, not adopted". Without the clause the sentence would repeat the R2-1 overclaim. "Not accounted for by memory alone" matches Main:82 ("Bell is a separate constraint") |
| F8 | A lead phrase only |
| F9 | At or below N-CC2/4 and N-BH1/3. The condition is named, and the closing sentence says "neither application is a demonstrated resolution" |
| F10 | The identity $\sum_o\sigma_oX\sigma_o=2\operatorname{tr}(X)I$ is correct (my exact probe). It is sourced in ERRATUM-r4 and attributed in an HTML comment |

## 4. Corpus overclaims (DEPENDENCIES-r7)

No sentence leans on a listed site:
- **Cosmological constant.** The draft cites GR §6.2 only for the invariance, the two completions and the
  open coupling step. It uses none of "never enters the stress-energy tensor", "eliminates … entirely" or "the
  value the framework expects". It uses no "dissolves" and no #937 site (ch07:207/:258, ch09:90, GR:32,
  Substratum:324, SM:132, appendix-c:273). The sites listed under §R are not leaned on either.
- **Black holes.** No Page curve is stated as pointwise. A.9 is cited for time averages only. A.8's scope is
  stated in the draft itself. The H-decouple label is withheld. The R11 markers (l.14, 181, 186, 189, 207, 223)
  name the REVIEW verdicts.
- **Main's title** appears only in the bibliography. The text never says "equivalence of quantum mechanics"
  (DEPENDENCIES §B).

## 5. Bibliography and VERIFY markers

The four new entries match their arXiv records. Authors, titles and journal references are correct:
- EvEMU11: *CQG* 28, 225007;
- KP14: *PRL* 112, 091304;
- Vol06: *IJMPD* 15, 1987;
- tH14: arXiv:1405.1548v3.

The draft's sentences against those abstracts:
- **tH14** (l.74): "QM as a tool for a system classical at its core; reconciled with Bell's theorem". At
  abstract strength.
- **EvEMU11:** "leave the observed value of Λ unexplained". At abstract strength ("does not solve … why the
  cosmological constant has the value that is observed").
- **Vol06:** "the ultraviolet zero-point sum does not set the vacuum energy". At abstract strength.
- **KP14:** "extends to the vacuum energy of phase transitions". The abstract says "renders all contributions
  from phase transitions automatically small", so the draft's wording is slightly stronger. See C1.

**Other entries.** They are unchanged from r4 and were verified earlier. [Pag05] was removed together with its
only use. All nine VERIFY markers are present and accurately worded.

## 6. Required changes

**C1** (l.169, at abstract strength under the VERIFY gate). Replace
"and of vacuum-energy sequestering, which extends to the vacuum energy of phase transitions [KP14]" with:
> and of vacuum-energy sequestering, which also renders contributions from phase transitions small [KP14]

**C2** (§6.2 item 8, l.211). Replace "The paper's results are the theorems and their scopes." with:
> What the paper states are the cited theorems and their scopes.

As written, the sentence reads as claiming the theorems as the paper's own results, against "claims no new
theorem" (l.32).

## 7. Nits

- **N1** (l.66). Optionally add Main:498's extension: "; Main's response-table extension removes the
  rationality condition". The sentence is correct as it stands.
- **N2** (l.30). Replace "The paper develops one idea, OI, and two of its consequences: the foundation and its
  quantum-emergence results (§§2–3), and two applications, …" with:
  > The paper develops one idea, OI: its foundation and quantum-emergence results (§§2–3), and two applications, …
- **N3** (abstract). The r4 clause "Each class contains the Markov laws, so neither a reversible realization nor
  a quantum representation distinguishes a law with memory from one without" was cut. Without it, "The
  discriminating content concerns memory" has no stated reason in the abstract. Restoring the clause is optional
  under the length budget; "all finite stochastic laws" implies it.
