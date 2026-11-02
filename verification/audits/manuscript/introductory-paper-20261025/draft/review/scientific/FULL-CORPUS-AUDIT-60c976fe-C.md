**Auditor C2: scientific audit of PR #918 (papers/Introduction.md), slice §4, §5, §6, References, and the abstract sentences on these topics**

Target: branch `draft/oi-introductory-paper-20261025` at 60c976fe (main 0d917665 merged in). Line numbers below are Introduction.md at that commit unless another file is named.

## Verdict: BLOCK

The numbers in my slice are correct; I recomputed each one myself. The block has three causes:
- **(B1)** The Page-curve conditional in §5 and §6 is stated without saying that its source theorem has no instance in the setting it counts. This is the audit's required finding R-01 (CON-01), and it has not been applied.
- **(B2)** By owner policy, the Introduction may not be more accurate than the framework it cites while known errors there stay uncorrected. The two corrections it depends on (GR App. A.8; GR §6.2/§8.3 and their mirrors) have no source-correction PR. None of the open PRs #961–#969 touches GR App. A or GR §6.2/§8.3.
- **(B3)** One external citation does not support the statement it is attached to.

Each fix is a text change, and none changes the framework's scientific status.

## Blocking findings

### B1. The Page-curve conditional does not say that Theorem A.8 has no instance in its counted setting (overclaim; audit R-01 / CON-01, required, not applied)

**Introduction.md:298.**
- Current text: "Under them, for all but an exponentially small fraction of initial conditions, the full-cycle average of the radiation's entanglement entropy at each stage's bipartition equals the Page value $S_{\rm Page}(d_B,d_R)$ up to the correction term of Theorem A.8, by measure concentration [Pag93; PSW06; HLW06; GR, Thms A.8–A.9]."
- Source: GR.md:817–841.
  - Theorem A.8 counts initial conditions as configurations on $\Sigma_E$ ("The fraction of initial conditions on $\Sigma_E$ that land on a bad cycle", GR.md:841), with the B|R bipartition aligned to them.
  - GR.md:833–835 and BHb C1/C6(a) prove that H-scramble fails for every bijection in exactly that setting.
  - BHb C2 proves that under any permutation the entanglement at an aligned bipartition satisfies $S(\rho_R)\le H(p_0)$.
  - BHb C6(b): the Page value enters only through H-scramble.
- What is wrong: the quantified conclusion is reported as a conditional result. The reader is not told that, as stated in GR, it is true only vacuously.
- Proposed replacement: "Under them, Theorem A.8 of [GR] gives the Page value $S_{\rm Page}(d_B,d_R)$, up to its correction term, for the full-cycle average of the radiation's entanglement entropy at each stage's bipartition; the Page value enters only through H-scramble [Pag93; PSW06; HLW06; GR, Thms A.8–A.9; BHb, C6(b)]. The theorem counts initial configurations with the bipartition aligned to them, the setting in which H-scramble fails, so as stated it has no instance. Under a bijection the entanglement at an aligned bipartition never exceeds the entropy of the initial configuration distribution [BHb, C2], so a Page value requires an initial superposition over at least $e^{S_{\rm Page}}$ configurations or a bipartition not aligned with them."

**Introduction.md:300.**
- Current text: "What survives is that conditional statement, with all three conditions. H-scramble requires an initial superposition of configurations or a split not aligned with them, and which of these the substratum supplies is open"
- Proposed replacement: "The result is that conditional statement, with all three conditions and no instance among configuration initial states. H-scramble requires an initial superposition of configurations, with configuration-basis entropy at least the Page value, or a split not aligned with them [BHb, C2]; which of these the substratum supplies is open"

**Introduction.md:308.**
- Current text: "the framework's cycle-averaged Page curve holds under H-scramble, H-decouple and with all of $\mathcal C_B\times\mathcal C_R$ one energy shell (§5)"
- Proposed replacement: "the framework's cycle-averaged Page curve is derived under H-scramble, H-decouple and a single energy shell on all of $\mathcal C_B\times\mathcal C_R$, hypotheses with no instance among the configuration initial states that [GR]'s theorem counts (§5)"

**Coupled corpus correction (required by owner policy; no PR exists).** GR App. A.8 needs one of two changes:
- restate the theorem over an ensemble of initial pure states, or over a non-aligned bipartition, and recount the excluded fraction over that ensemble; or
- move the "fails" sentence into A.8 itself, applied to its own counting (CON-01 / OD-9 / PR-E).

The same change must reach book ch07 §7.6, ch19:72 and appendix-a G11, with their FULL.md mirrors. Without it, the corrected Introduction would be more accurate than GR.

### B2. The conditional §4 relies on GR §6.2, which itself asserts the open step unconditionally (inconsistent with the corpus it cites; CON-05 / CON-06; no PR exists)

**Introduction.md:282.**
- Current text: "[GR] calls the G3 coupling theorem and leaves open [GR §6.2, §8.5]"
- GR §6.2 states both positions:
  - GR.md:344: "the metric evolves via Einstein's equations *before* the trace-out … at the classical level, the gravitational field equations never encounter the zero-point sum" (unconditional).
  - GR.md:356: the dissolution is conditional on G3.
- GR.md:573 is also unconditional: "The framework denies that the *absolute* zero-point sum gravitates, because gravity operates at the logically prior classical level (§6.2)."
- §A.25 mirrors with the same problem:
  - book ch07:177 (the same sentence as GR.md:344);
  - Explainer.md:542 (the zero-point sum "is not a source term in Einstein's equations, because those equations operate at the classical level");
  - Explainer.md:548 ("the other predicts the observed value", against GR.md:366, "a normalization, not a prediction");
  - Explainer.md:579 ("The framework denies that the zero-point energy gravitates").
- The Introduction's own text is correct and stays as is. The block is that it cannot land while its cited source contradicts it.
- Required source text:
  - GR.md:344 and ch07:177: "the metric belongs to the classical substratum; its covariant field equations and their source coupling are the open G3 step".
  - GR.md:573: "On the geometry-first proposal (§6.2), conditional on the open coupling step, the absolute zero-point sum does not gravitate".
  - The Explainer sites get the same conditional, and "predicts the observed value" becomes "is consistent with the observed value as a normalization".

### B3. [Pag93] does not support the statement of the information problem (miscitation; audit R-14, required, not applied)

**Introduction.md:288.**
- Current text: "carries the information of what formed it [Haw76; Pag93; Pag13]"
- What Pag93 contains (I read the arXiv text, gr-qc/9305007v2): it is "Average entropy of a subsystem", a result about random states. It does not discuss the black-hole information problem; it only points to Page's separate papers, refs [4] and [5].
- Proposed replacement: "[Haw76; Pag13]". Alternatively, add Page, "Information in black hole radiation", PRL 71, 3743 (1993), after reading it first-hand.
- [Pag93] stays at L298, where it is the right source for $S_{\rm Page}$.

## Optional findings

- **O1. L262** ("exceeds the observed value by some 120 orders of magnitude [Wei89, §III]").
  - The repo's first-hand Weinberg record places "some 120 orders" in §I, p. 1; §III gives "118 decimal places" against an observational *bound*, since Weinberg 1989 predates any measurement.
  - Replace with "exceeds the observational value by some 120 orders of magnitude [Wei89, §I]".
- **O2. L264.** The citation "[Wei89, §I; §III, Eqs. (3.4)–(3.6)]" now follows "the exact power depending on the cutoff convention". The same record says that clause is not Weinberg's. Move the citation to just after "observational value".
- **O3. L282.** "the same step fixes how the energy of electroweak and QCD vacuum transitions gravitates" has no locator. Its source is GR §8.3 (GR.md:583); add [GR §8.3].
- **O4. L270.** "the form [GR] targets": the form is $E_{\mu\nu}[g,\mathrm{OI}]=8\pi G(T_{\mu\nu}-\mathcal F[g,T]g_{\mu\nu})$, in GR's abstract (GR.md:12). Cite [GR, Abstract]. GR's G3 also includes the continuum limit, which L282 omits.
- **O5. L266**, "What OI establishes".
  - That $\Lambda$ belongs to the substratum's gravitational description comes from the framework's geometry-first ordering (GR §6.2, "Ontological commitment"), not from OI alone.
  - That the emergent description is a local lattice QFT with a $1/\epsilon$ cutoff rests on H-local-lift (GR §6.1). This is the ambient-to-native boundary.
  - Suggested wording: "In OI the quantum description, and with it the zero-point sum, is emergent (§§2–3; its identification with a local lattice QFT is conditional on H-local-lift [GR §6.1]), while on the framework's geometry-first ordering the effective cosmological constant belongs to the gravitational description of the substratum [GR §6.2]".
- **O6. L290–L292.**
  - The toy maps are arbitrary bijections and arbitrary maps, not the substratum dynamics, with no energy shell and no coupling chain (BHa REPORT scope; audit R-21). Add "with arbitrary bijections in place of the substratum dynamics".
  - The 60 count needs its layout: "for a one-bit message and one random bit, every register read after one step".
- **O7. L298.**
  - Theorem A.7 gives an *effectively* pure state, up to $O(t/\tau_B^D)$.
  - "far shorter than the evaporation" holds for black holes heavier than about $10^{11}$ kg (GR App. A.7; my computation gives $1.76\times10^{11}$ kg at $H_0=67.4$, Γ = 1).
- **O8. L308.** GR's dependency ladder (GR.md:12) places the Page curve at G4, conditional on G3. L318 says so, but the §6 conditional item could also name it: "and, for a physical black hole, the field equations".
- **O9. L315**, open problem 4, "exact gluing … for recurrent target families".
  - For rooted families, realizability at every time is classified in the kernel: `finiteRootedRealizable_iff_pper` (RootedClassificationAllTime:192). No manuscript states this yet.
  - Write "for recurrent families of multi-time laws" (audit R-09).
- **O10. L316.** "machine checks of the steps of §§2.2–2.5 proved on paper" leaves out §3's paper-only results: the Bell ceiling, the qubit factorization and the Hadamard example (R-27). The open list also leaves out Theorem 4's extension to infinite-dimensional systems (R-10, stage 1).
- **O11. L284.** "OI locates the gravitational source in the substratum microstate" → "OI's proposal locates …".
- **O12. L300.** "What survives" reads as revision narration (§A.33); "The result is" avoids it.
- **O13. L363 / L365** (BHa, BHb entries). Add "not adopted", matching the records' own status lines (audit O-17).
- **O14. Abstract L15.** The open list names the field equations but not the Page-curve conditions. The abstract states no Page curve, so this is not an overclaim. "separates conservation of black-hole information from its accessible recovery" could add "in finite reversible models".

## Claims checked and found correct

**Numbers I recomputed myself (independent exact code, exhaustive over $S_8$ and all 256 self-maps of $\{0,1\}^2$, rational arithmetic):**
- 1,376 of 40,320 bijections give zero accessible advantage. This needs one map at every step and cumulative records, as L290 states; with endpoint-snapshot records the count is 10,944.
- The 60 non-injective maps that recover, against 24 bijective ones.
- The 32 non-injective maps that break the floor (0 bijective).
- The floor $P_{\rm succ}\ge1/|\mathcal U|$: 0 violations over $S_8$, both for one message bit and for two. In the two-bit case the minimum is 1/2, 2,368 maps attain it, and none reaches 1/4. BHa's C2 proof also checks out on reading.
- The 122-digit dimensional identity:
  - $\rho_{\rm Pl}/(H^2c^2/G)=S_{\rm dS}/\pi$ exactly. Numerically: $S_{\rm dS}=2.27\times10^{122}$ at $H_0=67.4$; $\rho_{\rm Pl}/\rho_{\rm crit}=(8/3)S_{\rm dS}$ ($10^{122.8}$); Weinberg's own convention against $\rho_\Lambda$ gives $10^{117.95}$ ($10^{118.35}$ against his $10^{-47}$ GeV⁴ bound).
  - So "up to a numerical factor fixed by the cutoff convention" is correct.
- Theorem A.7's window: $t_{\rm evap}(30M_\odot)\approx1.8\times10^{79}$ s against $\tau_B^D\approx4.6\times10^{17}$ s.

**Sources checked against their cited text:**
- **[Sha79]**, read first-hand: a (k,n) threshold scheme in which k−1 pieces leave D "completely undetermined". This supports "perfect secret sharing, of which Shamir's threshold scheme is the standard example".
- **§4, verified against GR §6.2, §6.3 and §8.5:**
  - the uniform shift $\hat H\to\hat H+C$ changes no visible probability (exact; global phase);
  - the two completions share the substratum, the partition and every visible law;
  - G3 is named and open;
  - $\Lambda$ is a cosmological input;
  - the EvEMU11, KP14 and Vol06 attributions hold.
- **§5, verified against GR App. A.1, A.5, A.6, A.7 and A.8:**
  - the toy layout;
  - the three conditions as GR states them;
  - H-scramble fails for configurations with an aligned bipartition (also BHb C1/C6(a));
  - Thm A.7 scope, with BHa item F now propagated into GR;
  - the single shell, with the proper shell open;
  - the single trajectory open (BHb C6(d));
  - the GSL open (A.6);
  - the island correspondence conjectural.
- **§6, established items:**
  - every Appendix A declaration exists at the cited line at 17b830bc, and OIBridge is unchanged at the head;
  - "cores" of Theorem 2 and the capacity bound matches SC-29's joint-law scoping;
  - Theorem 3 in its rooted form matches its kernel statement;
  - the summary matches the §2–§3 body;
  - the Bell restatement agrees with SC-33's corrected Main.
- **§6, open items:** each is open in the corpus:
  - (C4) at the cosmological cut, GR.md:52;
  - no memory falsifier, Main §4.5;
  - the mixing hypothesis, Main §1.3 and §3.4;
  - (iii)–(v) as the selection principles, GR.md:220;
  - G3, the GSL, the proper shell and the single trajectory.
- **References:**
  - all 52 entries are cited and every cited key is listed, with no duplicates;
  - every internal location resolves at 55e3217b and at the head; the cited GR sections are unchanged between them;
  - the external bibliographic data for the §4–§5 entries are correct.
  - The repository's citation check, `tools/citation_roles_check.py`, passes its self-test but finds 0 manifests. It does not cover paper bibliographies, so the key check above was done by hand.
- **Open source-correction PRs:** none of #961–#969 removes or weakens text that this slice relies on. SC-28 and SC-31 change only GR §6.3's Maldacena paragraph and the book's mirror of it.

## Outside my slice

- **GR.md:366 and ch07:193.** "convention-dependent factor between $1/(96\pi^2)$ and $8/3$" is stated "for any theory with a Planck cutoff". Weinberg's reduced-Planck convention gives $1/(384\pi^4\Omega_\Lambda)\approx3.9\times10^{-5}$, outside that range. The range holds for the framework's $1/\epsilon$ cutoff with σ ≤ 1, not for any Planck cutoff.
- **GR Thm A.5 / A.7 coupling chain.** A.5 assumes V↔B↔D, while A.1 places V between the two horizons, which suggests B↔V↔D (BHa assumption-watch).
- **GR Thm A.7 proof.** It goes from "$\rho_D$ approximately constant" to "$|\Psi\rangle\approx|\psi_{VB}\rangle\otimes|\chi_D\rangle$". A constant marginal does not imply a product.
- **BHb assumption-watch.** The uniform-prior trace-out makes B∪R mixed, against A.7's pure state.
- **Book status wording.** ch07:110 and ch19:72 still say "resolves" / "Resolved at the level of information preservation" (CON-02). The Introduction is faithful to GR here; the book overstates.