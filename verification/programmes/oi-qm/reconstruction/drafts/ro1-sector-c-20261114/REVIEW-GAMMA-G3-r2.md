# Focused confirmation review of GAMMA-1 unit G3 r2

**Object.** `GAMMA-G3-r2.md` and `RESPONSE-GAMMA-G3-r1.md`, retained on PR #1294
(`research/ro1-sector-c-1169-20261114`) at `445b47b50`. The local copies match the blobs at that commit
byte for byte (SHA-256 `82fcb31f…cfe` and `754e3bcf…290`). The r1 text at `445b47b5` is unchanged from
`e4ffa3b5` (SHA-256 `0cb8c4ca…e69f`). The retained `REVIEW-GAMMA-G3-r1.md` is the reviewer's file as
written.

**Reviewer.** Claude, the non-author reviewer of r1. The review is read-only: no repository writes, no
posts.

**Method.** I diffed r1 against r2 line by line. Every changed passage was checked against the
finding it answers and against the source, using the copies opened for the r1 review. The one newly
read page, thesis p. 82, was re-read as an image at 100 dpi. I also compared every numeric token in r1
with r2.

## Verdict: ACCEPT

All eleven findings are applied in full, no transcribed number changed, the read statuses are exact, and no
premise or verdict was added. Two optional low-level notes follow in §5. Neither is needed for
acceptance.

## 1. Each r1 finding

| # | Applied? | Check |
|---|---|---|
| 1 Bach cause and normalization | Yes | §3 now quotes the source's cause ("Because of the finite separation of the mask and double-slit …") and its `P₂` counterpart, both verbatim. "Normalized per pattern" is marked [A-inf] in §3, in the §3 table, in §6 row C0 and in G3-F6. |
| 2 Schwindt quotation | Yes | §1.3 quotes the counterfactual Bell sentence and the LHV clause in full; I checked both against arXiv quant-ph/9908072v1. Note 14 is quoted verbatim. "Laser" for the pure-input source is marked [A-inf] in §1.3, §5 and G3-F2, and §1.3 notes that "Laser 670 nm" appears only in Fig. 1(b). |
| 3 Grangier qualifications | Yes | (a) The II-44 chain, the "quelques pour cents" sentence, "α ne diminuerait en fait …" and "en toute rigueur … α_Class ≥ (1 − β₁)(1 − β₂)" are verbatim against p. 82. "Every semi-classical model gives" is replaced by "the thesis uses". (b) The p. 82 form `α ≅ (2x + x²)/(1 + x)²`, II-43 and the p. 149 linking sentence are verbatim. (c) Both sources for `x` are recorded and neither is selected; the Table II-2 values match p. 99. (d) The selected-maximum row is labelled, and §6 requires all seven rows together with the trial count. The p. 81 caption quote is verbatim. |
| 4 C0's `Δ` | Yes | §6 row C0 and G3-F10(a): heralded runs are normalized per trigger, which is G1 §5.3's per-particle normalization, and only the laser runs lack it. §4.2 and G3-F10(b) give the background mapping (`p_AB − p_A − p_B = I_AB − p₀`) and the background invariance of `κ`. Both are recorded as findings against G1, and G1 is not edited. |
| 5 Typing | Yes | Every class table now carries a §5.4 type. The new §2.5 and G3-F11 state that the X-2 data, and the herald-gated single-detector counts, fit none of the four types. The choice is left to G1 or G5. |
| 6 AW-σ | Yes | G3-F5(a) applies G1 §5.7's fallback and states the residual question correctly. (b) The Allan-variance error bars versus the one-SD band are quoted verbatim, here and in §4.2. (c) The deviation is withdrawn, and settlement is required on target-neutral grounds under NC-γ5. |
| 7 AW-bc | Yes | §4.3, §6 and G3-F4(b) state the two idealizations: De Raedt is a 2-D FDTD at 405 nm with a 25 µm iron-index plate and the mask at 50 µm; Sawant is a thin-slit path integral at 810 nm. Both match the sources. The text says they are not a classical-versus-quantum pair. G3-F4(a) treats C0's additivity as declared in G1 §7.1. G3-F4(c) scopes the marker and cross-references H-3 and O11 without adding a stop. |
| 8 Provenance | Yes | The authorization cites #1169 c.6893331779, with the scope and the review requirement as I read them. r2 states honestly that it quotes them through the review. §9 gives G1 r4's review state and adds the r1, review and comment rows. |
| 9 Sorkin | Yes | "Obtained under an adopted extension", with the three source phrases verbatim against arXiv gr-qc/9401003v2. |
| 10 Eberly appendix | Yes | `F = ŝ · E`, `E_h = u_a H_a + u_b H_b` and `E_v = u_a V_a + u_b V_b` match arXiv 1712.10046v1. §5 and §6 now separate the single-photon analyzer-sorted case from the two-photon coincidences. |
| 11 Labels | Yes | The §6 X-3 sentence is marked [A-inf] for G5. The 436 ns arithmetic is recorded as [A-inf] and attributed to the review. |

## 2. No number changed

I compared every numeric token in r1 with r2. Only two r1 tokens are missing or appear less often:
- `0.0073 ± 0.0018` appears once instead of twice. The occurrence removed is the one in G3-F5, which
  was the withdrawn deviation. The Sinha transcription in §4.2 is unchanged.
- "64, 94" is read-status text that became "64, 81–83, 94".

All tables are unchanged: Table II-3, Table II-4, Jacques Table I, Sinha, De Raedt, Sawant, Bach and
Schwindt. The numbers added in r2 all agree with their sources:
- Table II-2 `x` values;
- II-57 gates;
- II-43 and II-44;
- De Raedt's 405 nm, 25 µm and 50 µm;
- Sawant's 810 nm;
- Sinha's 0.003 and 30 million.

## 3. Read statuses

The statuses are exact. The thesis entry is SECTIONS (front matter; pp. 59–64, 81–83, 94–110,
139–150), and the r2 text uses only those pages. The following are all labelled NOT READ:
- the GRA EPL full text;
- Sinha's published version and supporting material;
- the published versions of the arXiv-read items;
- the Eberly 2019 reply and the comment it answers;
- arXiv 1103.0121;
- De Zela, Söllner, Park, Thorn and the AIP proceedings.

Tonomura and Arndt remain ABSTRACT. No claim reaches beyond the pages listed.

## 4. Premises and verdicts

No premise was introduced. G3-F10 and G3-F11 are recorded against G1, leave G1 unedited and choose no
fifth type. The `x` source and the AW-σ rule are left unselected.

No verdict on D-1 or (γ) was introduced. The only "holds" in the X-2 bound passage refers to the
scope of the source's own inequality. The X-3 remark carries [A-inf] for G5. Nothing assumes a finite
total substratum.

## 5. Withdrawal of r1's 4σ figure: correct

Withdrawing the figure is correct, for three reasons:
1. It was a deviation of a datum from the reference value 0, not a comparison under `κ_cmp`.
2. It assumed one resolution of two open ambiguities: which uncertainty component applies, and
   whether the printed `±` is a spread or an uncertainty of the mean.
3. Printing it before AW-σ is settled risks choosing the rule by outcome (K-2, NC-γ5).

The arithmetic itself (0.0073/0.0018 ≈ 4.1) was not wrong. The withdrawal is of its use, and r1 is
retained unchanged as provenance. Because r1 and the r1 review still carry the figure, the operative
guard is G3-F5(c)'s requirement that AW-σ is settled on target-neutral grounds and declared under
NC-γ5. "So that it cannot inform the rule" is better read as "so that r2 does not offer it as input".

**Optional notes (low; not needed for acceptance).**
- G3-F10(a) and §2.5 group Jacques's clock triggers with heralds. A clock trigger marks an excitation
  attempt, not a detected herald. Under G1 §5.3 it corresponds to the no-herald normalization by
  `μ(𝔈_a)`, with one run per trigger, rather than to the herald-executed mass. "Normalizable per gate"
  is correct as written, and G1 or G5 may want the distinction kept when the fifth type is defined.
- II-43 is printed with an overbar on `𝒩`, the mean emission rate; r2 omits the bar.
