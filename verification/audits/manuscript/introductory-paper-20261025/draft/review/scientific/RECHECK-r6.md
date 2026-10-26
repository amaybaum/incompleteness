# Scientific confirmation re-check: Introduction r6

- **Object:** `draft/Introduction-r6.md` at `17aabc3b` on #918, sha256 `fc55c1e3…5183` (verified).
- **Method:** I read the full word diff against r5, and checked the changed sentences against GR:12, :356 and :761,
  Main §4.5 and the BH packages.
- **Read-only.** No repository file was changed. Git ran with `-c gc.auto=0 -c maintenance.auto=false`.

## Verdict: ACCEPT WITH NITS

C1 and C2 are applied verbatim, and no change raises claim strength. One optional nit concerns the gloss
of $\mathcal G_{\mu\nu}$.

## 1. C1 and C2

| Item | Result |
|---|---|
| C1 (§4, sequestering) | Verbatim: "which also renders contributions from phase transitions small [KP14]". This is now at abstract strength |
| C2 (§6.2 item 8) | Verbatim: "What the paper states are the cited theorems and their scopes." |

## 2. Other changes

| Change | Verdict |
|---|---|
| Abstract: the Markov clause is restored as "representability does not distinguish a law with memory from one without" | Correct (Theorem 1; my r5 N3) |
| §1.2: the sentence "Exact operational QM … (§3.2)" is removed | No loss. The qualifier still stands in the abstract ("none implied by OI alone"), §3.2 (Theorem 4 and "OI alone does not imply quantum mechanics"), §6.2 item 2 and the conclusion |
| §1.2 N2 rewording | Applied. No claim changed |
| 't Hooft sentence removed from §2.2 | [tH14] is still cited, with its VERIFY, in §6.2 item 8. No claim depends on the removed sentence |
| The Calvo sentence moved to §3.1 | Unchanged text |
| Theorem 2: "The written proof is in [Main …]; see also [CT06]" | Same citation; the status words are unchanged |
| "With this lemma, on a fixed finite reversible substratum …" | Same claim. The routed versus history-level split is unchanged |
| §3.5: the Born exponent and Bell, split into two sentences | Same content. "Must give up one of the two. The framework keeps measurement independence and adopts …" still states the adopted branch, not a necessity |
| §4: "(the mismatch)", "(§1.1)", "(§§2–3)" | Pointers only |
| §4: "OI's proposal is that the mismatch requires no cancellation, and its content lies in how the two levels couple to geometry" | It is labelled a proposal, and the next paragraph states it is "conditional on that open step". This matches GR:356's "the dissolution is conditional" and does not lean on the overclaimed tail |
| §4: $T^{\rm cl}_{\mu\nu}$ "the classical stress-energy of the substratum"; $\rho_C$ "the energy density of the offset" | Faithful to GR:356 (the offset $C$ under $\Omega_{\rm eff}\to\Omega_{\rm eff}+CI$; the $T^{\rm cl}$ of GR §6.2) |
| §4: $\mathcal G_{\mu\nu}$ "the Einstein tensor" | GR:356 does not define $\mathcal G$. Its point, that the quantum description cannot fix an offset $\rho_C g_{\mu\nu}$, holds for any gravitational operator, and GR:374 calls the Einstein equations "the covariant Level-G3 target, open". Naming $\mathcal G$ the Einstein tensor narrows the illustration but adds no claim about OI. See nit N1 |
| §4: $E_{\mu\nu}[g,\mathrm{OI}]$ "the gravitational side still to be derived"; $\mathcal F[g,T]$ "a scalar functional of the metric and the stress-energy" | Role-only glosses, consistent with GR:12, which calls this the open G3 target. No claim is added |
| §4: $H_{\rm Hub}$ "the Hubble rate" | Correct. The rename avoids a clash with the hidden sector $H$ |
| §5: "Because the dynamics of OI is a bijection observed through a partition (§1.1), two questions separate" | Same content as "Under OI". It states the premise as a premise |
| §5: the accessible-advantage definition moved to its first use | Unchanged definition |
| §5: H-scramble as "equidistribution of the orbit over pure states on an energy shell" | Matches GR A.7's definition (BH-02 REPORT, "H-scramble dependency finding"). Moving it into one sentence changes no scope |
| §5: $t_{\rm evap}$ "the evaporation time", and $\tau_B^D$ "the $D$-sector timescale" [GR App. A.5] | Verbatim GR:761 (Thm A.5: "Let $\tau_B^D$ be the $D$-sector timescale"). Correct, and safer than a gloss with more content |
| §6.2 item 4 trimmed to "the Page curve of [GR App. A] is not established (§5)" | No loss. Every condition (H-scramble, closure over whole cycles, full-product shell, cycle average versus single trajectory, the covariant field equations), plus the GSL and the islands, is still stated in §5 (l.190 and l.192 equivalents). The item keeps the toy-model scope and the three item-F non-claims |
| §6.3: "no experiment distinguishing OI from standard quantum theory, and no memory-witness constraint, is established [Main §4.5]" | Correct and weaker than "can". Main:702–704 says no memory-witness falsifier is established "at present" |
| Conclusion: "because the representation is universal, the discriminating content lies in memory, which every deterministic completion carries in its hidden state" | r4's reviewed sentence. It rests on Theorem 2, whose not-machine-checked step is stated in §2.4 and in the abstract |
| F7 (§6.1) | **It survives unchanged**: "with measurement independence kept, they need ontic parameter dependence …" |

## 3. Nit

**N1 (optional), §4.** For "with $\mathcal G_{\mu\nu}$ the Einstein tensor", write:
> with $\mathcal G_{\mu\nu}$ the gravitational side of the field equations (the Einstein tensor in general relativity)

This keeps the illustration general, as GR:356 leaves it.
