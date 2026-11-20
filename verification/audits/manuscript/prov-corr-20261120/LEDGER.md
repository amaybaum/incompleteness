# PROV-CORR — provenance-correction coverage ledger

**Status.** Writer's correction ledger for manuscript correction unit PROV-CORR; independent
exact-head review pending, and merge is a separate owner decision. Paper corrections only: no
physical premise is added, no conditional mechanism is promoted or dropped, R1 stays open, and no
§A.23 correctness band moves (bands unchanged: this is consistency work).

**Authorization.** Owner `amaybaum`,
[#1169 comment 7042723597](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7042723597),
2026-11-20T14:58:03Z: "Scope: findings F-1 to F-15 and the circularity flags Z-1 and Z-2 of
`verification/audits/foundations/r1-l8-stage1i-20261120/AUDIT.md`. The objective is that the
manuscripts distinguish accurately what OI derives, imports, calibrates, assumes, and leaves
unresolved." Goal link (§A.47), as recorded there: a consistency correction (§A.25, §A.27, §A.30)
so that the presentation of OI's gravitational and vacuum-energy outputs matches their actual
provenance; not a new result.

**Source.** Findings and anchors: `verification/audits/foundations/r1-l8-stage1i-20261120/AUDIT.md`
§4–§5 (merged in #1457). Base: `main` at `dca41f646d55fdb5e38cbb72fd7ce3a6e00279e1`, whose
`papers/` and `book/` sources are identical to the audit's pin `371acccc`, so every audit line
number is a base line number. Site notation as the audit's PREREG (`GR:n` is line `n` of
`papers/GR.md`; `Str`, `Sub`, `SM`, `chNN`, `appA`, `FULL` likewise). `Main.md` has no site and is
unchanged.

## Coverage summary (one row per finding)

| Id | Sites corrected (base lines; FULL mirrors) | Anchor | Correction | Hunks |
|---|---|---|---|---|
| F-1 | ch09:63, FULL:2478 | GR:482 "taken over from Verlinde's analysis rather than rederived from the substratum" | 1/6 no longer attributed to cubic-lattice geometry; anchor wording used | F-1.1 |
| F-2 | appA:92 (row 23), :108 (G6), :94; FULL:5539, :5555, :5541 | appA:48–50 layer definitions; GR:482 | Layer "0/1" → "—" in both rows; row 23 gains "(factor imported)"; summary clause states no substratum layer | F-2.1–2.3 |
| F-3 | ch03:118, FULL:979; Str:903; Sub:375 (audit's related site) | GR:482; AUDIT §2.4 Test N | a₀ removed from the class-specific list and from Structure's Level 3 table; Sub:375 states the import as Sub:419 does | F-3.1–3.3 |
| F-4 | ch09:149, FULL:2564 | GR:547 "normalization comparison open" (ch07 summary table agrees) | "confirmed empirical relation" → "normalization comparison open" | F-4.1 |
| F-5 | ch09:258, FULL:2673 | GR:318, :482; appA:117 | 1/4 and a₀ removed from the "substrate-computable record" | F-5.1 |
| F-6 | ch05:59, :61, FULL:1374, :1376; Sub:88; ch02:120, FULL:750 | GR:420 "Its use as a physical source is a separate question"; GR:422, :430, :444 | Flatness no longer "structurally explained" or "a structural feature"; ρ_s = ρ_crit stated as the restated flat Friedmann density; Ω_total (inferred) separated from ρ_s; use as a filter conditional on the open source identification | F-6.1–6.4 |
| F-7 | SM:30 | GR:428–430, :440 (ε and σ cancel) | Wrong provenance ("through ε = 2√σ l_P") replaced by the inputs that survive; filter made conditional | F-7.1 |
| F-8 | SM:180, :200, :1424; Sub:157; propagation SM:212, ch05:75, FULL:1390 | GR:430, :440, :444; AUDIT §2.3 | Anthropic rebuttal made conditional on the source identification; "passes exactly", "independently excludes", "framework-internal" removed; ratio attributed to first law, V/A and Friedmann | F-8.1–8.6 |
| F-9 | SM:196 | GR:428–430, :440 | Over-conditioning removed: ε and σ cancel from ST, which uses no calibration | F-9.1 |
| F-10 | GR:470, :510; ch07:260, :262, FULL:2125, :2127; propagation ch07:284, FULL:2149 | GR:478–488 (values contain c, H, G, M_B and the imported factor); AUDIT §2.4 | Conditions on T_dS attached to the entropy-displacement chain; the displayed values stated not to contain ΔS | F-10.1–10.5 |
| F-11 | ch07:262, FULL:2127 | GR:472–476 "the Clausius relation applied to the boundary reservoir" | "Bekenstein bound" → "Clausius relation at T_dS" | F-11.1 |
| F-12 | GR:689 | GR:308, :318–320 | "quantitative consequences specific to it" → the calibration and the count's agreement with the Hawking-temperature 1/4, relations kept | F-12.1 |
| F-13 | GR:108, :160; ch07:65, :61, FULL:1930, :1926 | GR:308 "self-consistency condition, not an independent determination"; Sub:179; appB:169 | "ħ is derived, not free" / "derives ħ from G and ε" → ħ fixed as a function of boundary quantities; the relation fixes ε/√σ from measured ħ | F-13.1–13.4 |
| F-14 | Str:904 | GR:318–320; Str:882 (the 1/4 already at Level 1) | Row removed from the Level 3 (OI universality-class) table | F-14.1 |
| F-15 | appA:110 (G9), :115; FULL:5557, :5562 | GR:454, :545 "uses the supplied baryon fraction" | G9 class C → E, formula shows the supplied Ω_B; count 5 C + 2 L → 4 C + 2 L + 1 E (total 7 unchanged) | F-15.1–15.2 |
| Z-1 | GR:689; ch09:258, FULL:2673; Str:904 | GR:158 "consequences of it, not independent checks of it"; GR:306–308 | Calibration and its rewrite no longer presented as substratum consequences or a substrate-computable record | via F-12.1, F-5.1, F-14.1 |
| Z-2 | GR:108, GR:160 | GR:308; Sub:179 | ħ no longer presented as derived in value | via F-13.1, F-13.2 |

Retained by design: the relation ħ = c³ε²/(4Gσ), ε = 2√σ l_p as its calibration, the ratio
2π/8π and the count's agreement with A/(4l_p²) under the named conditions (GR:308, :318–320, :356);
the entropy-displacement mechanism of GR §7.3 and ch07 §7.9 as a conditional proposal with its
named conditions and imported factor; the ρ_s = ρ_crit calculation and the 2/(d−1) ratio with
their algebra; and the a₀(z) comparisons stated in tension (GR:512–516, :548–549; ch07 §7.9),
which no edit touches.

## No unrelated change

`git diff -U0 dca41f64 -- '*.md'` has 51 hunks: 33 in source files and 18 in `FULL.md`. Each maps
to exactly one block below, and each FULL hunk is the mirror of a chapter hunk (§A.14;
`mirror_check.py`: 0 chapter lines absent from FULL).

| File | Hunks | Ledger blocks |
|---|---|---|
| `papers/GR.md` | 5 (:108, :160, :470, :510, :689) | F-13.1, F-13.2, F-10.1, F-10.2, F-12.1 |
| `papers/SM.md` | 6 (:30, :180, :196, :200, :212, :1424) | F-7.1, F-8.1, F-9.1, F-8.2, F-8.5, F-8.3 |
| `papers/Structure.md` | 1 (:903–904, two rows removed) | F-3.2, F-14.1 |
| `papers/Substratum.md` | 3 (:88, :157, :375) | F-6.3, F-8.4, F-3.3 |
| `book/appendix-a-prediction-status.md` | 5 (:92, :94, :108, :110, :115) | F-2.1, F-2.3, F-2.2, F-15.1, F-15.2 |
| `book/ch02-substratum.md` | 1 (:120) | F-6.4 |
| `book/ch03-structural-realism.md` | 1 (:118) | F-3.1 |
| `book/ch05-gauge-structure.md` | 3 (:59, :61, :75) | F-6.1, F-6.2, F-8.6 |
| `book/ch07-gravity.md` | 5 (:61, :65, :260, :262, :284) | F-13.4, F-13.3, F-10.3, F-10.4 + F-11.1, F-10.5 |
| `book/ch09-universality.md` | 3 (:63, :149, :258) | F-1.1, F-4.1, F-5.1 |
| `book/The-Incompleteness-of-Observation-FULL.md` | 18 (:750, :979, :1374, :1376, :1390, :1926, :1930, :2125, :2127, :2149, :2478, :2564, :2673, :5539, :5541, :5555, :5557, :5562) | mirrors of the chapter hunks above |

Derived files: `papers/{GR,SM,Structure,Substratum}.{tex,pdf}` and
`book/The-Incompleteness-of-Observation-FULL.{tex,pdf}` rebuilt with `sh ./build.sh GR SM
Structure Substratum` and `sh ./build.sh --book` (no dropped glyphs; pages 84, 148, 94, 53 and
489, against 84, 148, 94, 53 and 488 at the base); their `.tex` diffs are the edited paragraphs
and the source stamps. `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json`
regenerated with its checker as `.github/workflows/verify.yml` runs it: the only differences are
mirror-parity predicates naming the edited chapter lines; the controls file is unchanged.

## Judgments

1. **Layer for a₀ (F-2).** None of appendix A's layer definitions (appA:48–58) covers a value made
   of an imported factor and the measured H, so the cell is "—" and the summary clause says so.
   The class (C, coupling map open) is not a finding and is unchanged.
2. **ch09:63 (F-1).** The corrected sentence keeps the entropy-displacement reading at the
   structural-properties level, which ch09:48 and ch09:72 (agreeing sites in the audit) also
   state, and attributes the 1/6 as GR:482 does.
3. **Propagation beyond the audit list.** SM:212 and ch05:75 (FULL:1390) carried "the
   framework-internal concordance calculation" in the same anthropic argument as SM:180 (F-8);
   ch07:284 (FULL:2149) closes the section whose opening sentence F-10 corrects; appA:94 and
   :115 are the summary clause and count that F-2 and F-15 change. ch09:48 and GR:356 restate
   the T_dS conditions for the MOND formulas in the conservative direction and are on the audit's
   agreeing list; they are unchanged.
4. **G9 class (F-15).** E (an explicit empirical input, Ω_B, enters the value) is the class whose
   definition the row meets; its layer (1) was not a finding and is unchanged.

## Re-grep (after correction)

Counted as matching lines in `papers/*.md`, `book/*.md`, `papers/*.tex` and `book/*.tex`: 0 for
each of "arises from the cubic-lattice geometry", "structurally explained rather than fine-tuned",
"a structural feature rather than an initial condition", "passes exactly", "independently
excludes", "defeat the specifically anthropic", "the $1/4$ coefficient, the acceleration scale",
"confirmed empirical relation", "quantitative consequences specific", "inherits H-count and the
horizon conditions", "derived, not free", "derives $\hbar$ from", "framework derives $\hbar$
downstream", "Everything in §7.3", "all of which inherit", "The chain rests on the de Sitter",
"Bekenstein bound applied to a baryonic", "framework-internal concordance", "Holographic $A/4$ at
cosmological", "| C | 0/1 |", "5 C + 2 L", "MOND acceleration scale as $cH/6$ from entropy",
"satisfies $\rho_s / \rho_{\text{crit}} \approx 1$". Surviving legitimate uses (`.md` only, FULL in
parentheses): "substrate-computable record" 2 (1), now listing the Cabibbo magnitude and the Koide
ratio; "normalization comparison open" 5 (2); "taken over from Verlinde" 3 (1); "(factor imported)"
4 (2); "non-anthropic" 1 (0), SM:180, for a comparison that does not invoke observers.

## Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7042723597 | Authorization and goal link | Provenance; quoted with author and time |
| #1457 | The audit whose findings this ledger corrects | Provenance; the audit is on `main` (support on `main`) |
| #873, #1448, #1449 | Accountability; adjacent open Issues | Provenance |

## Before and after, per finding

Each block quotes the exact replaced span and its replacement; where a chapter site has a FULL
mirror the same replacement was applied there.

### F-1

**F-1.1** — ch09:63; FULL:2478 (audit site)

Before:

```text
Similarly, the MOND acceleration scale $a_0 = cH/6$ is determined at the structural-properties level: the dimensional factor $1/6$ arises from the cubic-lattice geometry combined with the $d = 4$ spacetime structure, common to any substratum with these properties.
```

After:

```text
Similarly, the entropy-displacement reading of the MOND acceleration scale $a_0 = cH/6$ sits at the structural-properties level; the dimensional factor $1/6$ is fixed by $d = 4$ together with the volume-vs-area entropy interplay and is taken over from Verlinde's analysis rather than rederived from the substratum (Chapter 7 §7.9).
```

### F-2

**F-2.1** — appA:92 (row 23); FULL:5539 (audit site)

Before:

```text
| 23 | MOND acceleration $a_0$ | $cH/6$ | C | 0/1 | Within quoted systematics | Ch 7 §7.9 |
```

After:

```text
| 23 | MOND acceleration $a_0$ | $cH/6$ (factor imported) | C | — | Within quoted systematics | Ch 7 §7.9 |
```

**F-2.2** — appA:108 (G6); FULL:5555 (audit site)

Before:

```text
| G6 | MOND acceleration $a_0 = cH/6$ | $cH/6$ (factor imported) | C | 0/1 | Within quoted systematics | Ch 7 §7.9 |
```

After:

```text
| G6 | MOND acceleration $a_0 = cH/6$ | $cH/6$ (factor imported) | C | — | Within quoted systematics | Ch 7 §7.9 |
```

**F-2.3** — appA:94; FULL:5541 (summary clause explaining the empty layer cell; necessary consequence of F-2.1–2.2)

Before:

```text
and the MOND formula (coupling map open, factor imported).
```

After:

```text
and the MOND formula (coupling map open, factor imported, no substratum layer).
```

### F-3

**F-3.1** — ch03:118; FULL:979 (audit site)

Before:

```text
the Koide angle as $2/9$ from a cubic-group Casimir; the MOND acceleration scale as $cH/6$ from entropy displacement; the JUNO
```

After:

```text
the Koide angle as $2/9$ from a cubic-group Casimir; the JUNO
```

**F-3.2** — Str:903 (audit site; Level 3 table row removed)

Before:

```text
| MOND scale $a_0 = cH/6$ | Tully-Fisher relation; ongoing tests | [GR §7.3] |
```

After:

```text
(row removed)
```

**F-3.3** — Sub:375 (audit's "related, weaker" site; import stated as at Sub:419)

Before:

```text
and a MOND acceleration scale $a_0 = cH/6$ from entropy displacement at the boundary ([GR, §7]).
```

After:

```text
and a MOND acceleration scale $a_0 = cH/6$ from entropy displacement at the boundary, with its dimensional factor imported ([GR, §7]).
```

### F-4

**F-4.1** — ch09:149; FULL:2564 (audit site)

Before:

```text
| Baryonic Tully-Fisher $v^4 = G M_B \cdot cH/6$ | confirmed empirical relation | Ch 7 §7.9 |
```

After:

```text
| Baryonic Tully-Fisher $v^4 = G M_B \cdot cH/6$ | normalization comparison open | Ch 7 §7.9 |
```

### F-5

**F-5.1** — ch09:258; FULL:2673 (audit site; also Z-1)

Before:

```text
with the invariant list (the Cabibbo magnitude, the Koide ratio, the $1/4$ coefficient, the acceleration scale $a_0 = cH/6$) constituting the substrate-computable record.
```

After:

```text
with the invariant list (the Cabibbo magnitude, the Koide ratio) constituting the substrate-computable record.
```

### F-6

**F-6.1** — ch05:59; FULL:1374 (audit site)

Before:

```text
The cosmological observation that the universe is spatially flat near the critical density — $\Omega_{\text{total}} \approx 1$ — is, in the framework's gravitational sector developed in Chapter 7, a structural feature rather than an initial condition.
```

After:

```text
The cosmological observation that the universe is spatially flat near the critical density — $\Omega_{\text{total}} \approx 1$, inferred under the standard cosmological model — is compared in the framework's gravitational sector developed in Chapter 7 with the thermal energy of the horizon's boundary modes.
```

**F-6.2** — ch05:61; FULL:1376 (audit site)

Before:

```text
The filter selects $d = 3$ as the unique value at which the observed spatial flatness is structurally explained rather than fine-tuned.
```

After:

```text
The ratio comes from the horizon first-law normalization, the area-law entropy and the Friedmann equation, with $\epsilon$ and $\sigma$ cancelling; at $d = 3$ the equality restates the flat Friedmann density, since $\rho_{\text{crit}}$ and the Hubble volume are both computed from $H$. The filter bears on the observed flatness only if the boundary energy is identified with the gravitating density, a source identification that Chapter 7 leaves open.
```

**F-6.3** — Sub:88 (audit site, E7)

Before:

```text
(E7) **Boundary-entropy concordance.** The cosmological parameter inferred from observation under the standard cosmological model satisfies $\rho_s / \rho_{\text{crit}} \approx 1$ (spatial flatness near critical density); it is an inferred quantity, not a directly measured one. In $d$ spatial dimensions, the general-$d$ form of this ratio is $\rho_s / \rho_{\text{crit}} = 2/(d-1)$, which equals unity only for $d = 3$. (Used in Stage 2(a); third forward filter for $d = 3$. See [SM §3.2] and [GR §7.2] for the derivation.)
```

After:

```text
(E7) **Boundary-entropy concordance.** The total density inferred from observation under the standard cosmological model satisfies $\Omega_{\text{total}} \approx 1$ (spatial flatness near critical density); it is an inferred quantity, not a directly measured one. The Hubble-volume mean $\rho_s$ of the horizon thermal energy equals the flat critical density computed from the same $H$ ([GR §7.2]); its comparison with the inferred total density requires the identification of the boundary energy with the gravitational source, which [GR §7.2] leaves open. In $d$ spatial dimensions, the general-$d$ form of this ratio is $\rho_s / \rho_{\text{crit}} = 2/(d-1)$, which equals unity only for $d = 3$. (Used in Stage 2(a); third forward filter for $d = 3$, conditional on that identification. See [SM §3.2] and [GR §7.2] for the derivation.)
```

**F-6.4** — ch02:120; FULL:750 (audit site)

Before:

```text
propagating gravity, stable matter, spatial flatness — together with six structural assumptions
```

After:

```text
propagating gravity, stable matter, near spatial flatness through the conditional comparison of E7 — together with six structural assumptions
```

### F-7

**F-7.1** — SM:30 (audit site)

Before:

```text
it independently excludes $d\geq4$ (§3.2); its coefficient inherits H-count and the horizon conditions of [GR §2, §8.5] through $\epsilon=2\sqrt{\sigma}\,l_P$.
```

After:

```text
conditional on identifying the boundary energy with the gravitational source, it excludes $d\geq4$ (§3.2); its coefficient comes from the horizon first-law normalization, the area-law entropy and the Friedmann equation, with $\epsilon$ and $\sigma$ cancelling ([GR §7.2]).
```

### F-8

**F-8.1** — SM:180 (audit site; the anthropic rebuttal)

Before:

```text
The boundary-entropy concordance below compares the supplied flat Friedmann scale with the calibrated and counted horizon contribution averaged over the Hubble volume ([GR §7.2]). Under those assumptions it equals unity only at d = 3. This filter selects d = 3 without invoking the existence of observers at all. The logical structure is therefore: propagating gravity ($d \geq 3$) and stable matter ($d \leq 3$) together fix $d = 3$, and the circularity worry attaches only to the anthropic-flavored stable-matter step. That worry is answered by the boundary-entropy concordance — a filter that uses those Friedmann and horizon assumptions without the stable-matter premise — which independently excludes $d \geq 4$ by equalling unity only at $d = 3$. A referee who rejects the stable-matter filter as circular is therefore left with propagating gravity plus the boundary-entropy concordance, which still yield $d = 3$: the anthropic step is *substitutable*, not indispensable. This does not make the selection a pure a priori derivation — the concordance filter uses the observed near-flatness, so $d = 3$ remains a self-consistency selection that consumes $d$-dependent emergent physics (§8.3), independently anchored by the observed gauge group — but it does defeat the specifically anthropic form of the circularity objection.
```

After:

```text
The boundary-entropy concordance below compares the supplied flat Friedmann scale with the horizon thermal energy averaged over the Hubble volume ([GR §7.2]). The count's $\epsilon$ and $\sigma$ cancel from it, and its value and $d$-dependence come from the first-law normalization, the ratio of Hubble volume to horizon area and the Friedmann equation. Under those assumptions it equals unity only at d = 3. Its use as a filter requires the identification of the boundary energy with the gravitational source, which [GR §7.2] leaves open; with that identification it selects d = 3 without invoking the existence of observers at all. The logical structure is therefore: propagating gravity ($d \geq 3$) and stable matter ($d \leq 3$) together fix $d = 3$, and the circularity worry attaches only to the anthropic-flavored stable-matter step. With the source identification, propagating gravity plus the boundary-entropy concordance yield $d = 3$ without the stable-matter premise, and the anthropic step is substitutable; without it, the selection rests on propagating gravity and stable matter. In either case the selection is not a pure a priori derivation: the concordance filter uses the observed near-flatness, and $d = 3$ remains a self-consistency selection that consumes $d$-dependent emergent physics (§8.3), independently anchored by the observed gauge group.
```

**F-8.2** — SM:200 (audit site)

Before:

```text
adding concordance sharpens to a consistency check that the framework passes exactly rather than by a numerical coincidence.
```

After:

```text
adding concordance gives a consistency comparison, conditional on the source identification, whose equality at d = 3 is fixed by the first-law normalization, the ratio of volume to area and the Friedmann equation.
```

**F-8.3** — SM:1424 (audit site)

Before:

```text
with the boundary-entropy concordance an additional non-anthropic consistency check that also excludes $d \geq 4$ by equalling unity only at $d = 3$, and so substitutes for the anthropic stable-matter step in the circularity rebuttal of §3.2;
```

After:

```text
with the boundary-entropy concordance an additional consistency comparison that also excludes $d \geq 4$, conditional on identifying the boundary energy with the gravitational source (§3.2);
```

**F-8.4** — Sub:157 (audit site)

Before:

```text
boundary-entropy concordance (E7) gives $\rho_s / \rho_{\text{crit}} = 2/(d-1) = 1$ at $d = 3$ uniquely. The intersection of the first two filters already pins $d = 3$; the third is a sharpening consistency check that the framework passes exactly.
```

After:

```text
boundary-entropy concordance (E7) gives $\rho_s / \rho_{\text{crit}} = 2/(d-1) = 1$ at $d = 3$ uniquely, conditional on identifying the boundary energy with the gravitational source ([GR §7.2]). The intersection of the first two filters already pins $d = 3$; the third is a consistency comparison whose ratio comes from the first-law normalization, the area-law entropy and the Friedmann equation, with $\epsilon$ and $\sigma$ cancelling.
```

**F-8.5** — SM:212 (propagation: paraphrase "framework-internal concordance calculation" in the same anthropic argument)

Before:

```text
The requirement that such an observer exist, combined with the framework-internal concordance calculation, constrains $d$. The observer is not selecting
```

After:

```text
The requirement that such an observer exist, combined with the boundary-entropy concordance calculation, conditional on its source identification, constrains $d$. The observer is not selecting
```

**F-8.6** — ch05:75; FULL:1390 (propagation: book mirror of SM:212)

Before:

```text
The requirement that such an observer exist, combined with the framework-internal concordance calculation, constrains $d$. This is not a standard
```

After:

```text
The requirement that such an observer exist, combined with the boundary-entropy concordance calculation, conditional on its source identification, constrains $d$. This is not a standard
```

### F-9

**F-9.1** — SM:196 (audit site)

Before:

```text
gives $ST/V=dH^2/(8\pi G_d)$, conditional on H-slope, the further conditions of [GR §8.5(b)] and the symmetric detailed-balance rates.
```

After:

```text
gives $ST/V=dH^2/(8\pi G_d)$; $\epsilon$ and $\sigma$ cancel from $ST$, so the value uses the first-law normalization and the area-law entropy and not the calibration of $\epsilon/\sqrt{\sigma}$.
```

### F-10

**F-10.1** — GR:470 (audit site)

Before:

```text
Everything in §7.3 therefore carries those conditions.
```

After:

```text
The entropy-displacement chain of §7.3 therefore carries those conditions; the values of $a_0$ and $v^4$ in Steps 2–3 do not contain Step 1's $\Delta S$ and use $c$, $H$, $G$, $M_B$ and the imported factor.
```

**F-10.2** — GR:510 (audit site)

Before:

```text
the dimensional factor is imported (Step 2); given these, $a_0 = cH/6$ and $v^4 = GM_B \cdot cH/6$ contain no fitted parameter.
```

After:

```text
the dimensional factor is imported (Step 2). The values $a_0 = cH/6$ and $v^4 = GM_B \cdot cH/6$ do not contain $\Delta S$: they are the imported factor applied to the measured $H$, with Step 3's deep-regime law for $v^4$, and contain no fitted parameter.
```

**F-10.3** — ch07:260; FULL:2125 (audit site)

Before:

```text
The argument has four steps, all of which inherit the conditions on the de Sitter temperature (H-count, H-slope, H-frame, H-Hawking, local boost structure at the horizon and the symmetric detailed-balance rate ratio; see [GR §7.3]) and the assumption that a static configuration delivers its full rest energy $Q=M_Bc^2$ as heat to the boundary — a coupling statement belonging to the open G3 map rather than a consequence of C1.
```

After:

```text
The argument has four steps. The entropy-displacement chain inherits the conditions on the de Sitter temperature (H-count, H-slope, H-frame, H-Hawking, local boost structure at the horizon and the symmetric detailed-balance rate ratio; see [GR §7.3]) and the assumption that a static configuration delivers its full rest energy $Q=M_Bc^2$ as heat to the boundary — a coupling statement belonging to the open G3 map rather than a consequence of C1. The values of $a_0$ and of the Tully-Fisher normalization do not contain the displaced entropy of Step 1: they are fixed by the imported factor and the measured $H$.
```

**F-10.4** — ch07:262; FULL:2127 (audit site; first sentence)

Before:

```text
*Step 1: Entropy displacement by baryonic matter (conditional).* The chain rests on the de Sitter temperature
```

After:

```text
*Step 1: Entropy displacement by baryonic matter (conditional).* This step rests on the de Sitter temperature
```

**F-10.5** — ch07:284; FULL:2149 (propagation: closing sentence of the same section, same claim)

Before:

```text
The acceleration scale, crossover and deep-MOND relation require the de Sitter temperature, the open heat input and the imported Verlinde factor.
```

After:

```text
The entropy-displacement account of the acceleration scale, crossover and deep-MOND relation requires the de Sitter temperature, the open heat input and the imported Verlinde factor.
```

### F-11

**F-11.1** — ch07:262; FULL:2127 (audit site; second sentence)

Before:

```text
With these, the Bekenstein bound applied to a baryonic mass $M_B$ in a de Sitter background gives the entropy displaced from the cosmological boundary:
```

After:

```text
With these, the Clausius relation at $T_{\text{dS}}$, applied to a baryonic mass $M_B$ in a de Sitter background, gives the entropy displaced from the cosmological boundary:
```

### F-12

**F-12.1** — GR:689 (audit site; also Z-1)

Before:

```text
and the quantitative consequences specific to it (the fixed $1/4$ coefficient and $\epsilon = 2\sqrt{\sigma}\,l_p$, under the conditions of §8.5(b)).
```

After:

```text
and the relations it supplies between the boundary count and horizon thermodynamics (the calibration $\epsilon = 2\sqrt{\sigma}\,l_p$, fixed by the measured $\hbar$, and the count's agreement with the $1/4$ coefficient fixed by the Hawking temperature and the first law, under the conditions of §8.5(b)).
```

### F-13

**F-13.1** — GR:108 (audit site; also Z-2)

Before:

```text
**Step 1: Uniqueness.** $\hbar$ is derived, not free, conditional on the calibration $a_*=\tau_K/\beta_E$ (§2.3; Step 4) and its named conditions.
```

After:

```text
**Step 1: Uniqueness.** Under the calibration $a_*=\tau_K/\beta_E$ (§2.3; Step 4) and its named conditions, $\hbar$ is fixed as a function of the boundary quantities, with no free coefficient; since $\epsilon/\sqrt{\sigma}$ is not determined independently, the resulting relation fixes $\epsilon/\sqrt{\sigma}$ from the measured $\hbar$, not the value of $\hbar$ (§4).
```

**F-13.2** — GR:160 (audit site; also Z-2)

Before:

```text
the present argument takes $G$ as a parameter of the classical Hamiltonian (Lemma 3) and derives $\hbar$ from $G$ and $\epsilon$.
```

After:

```text
the present argument takes $G$ as a parameter of the classical Hamiltonian (Lemma 3) and expresses $\hbar$ through $G$ and $\epsilon$; since $\epsilon/\sqrt{\sigma}$ is not determined independently, the relation fixes $\epsilon/\sqrt{\sigma}$ from the measured $\hbar$ (§4).
```

**F-13.3** — ch07:65; FULL:1930 (audit site; book mirror of GR:160)

Before:

```text
the present argument takes $G$ as a parameter of the classical Hamiltonian and derives $\hbar$ from $G$ and $\epsilon$.
```

After:

```text
the present argument takes $G$ as a parameter of the classical Hamiltonian and expresses $\hbar$ through $G$ and $\epsilon$; since $\epsilon/\sqrt{\sigma}$ is not determined independently, the relation fixes $\epsilon/\sqrt{\sigma}$ from the measured $\hbar$ (Section 7.4).
```

**F-13.4** — ch07:61; FULL:1926 (audit site)

Before:

```text
and the framework derives $\hbar$ downstream of this counting,
```

After:

```text
and the framework's relation for $\hbar$ comes downstream of this counting,
```

### F-14

**F-14.1** — Str:904 (audit site; Level 3 table row removed; also Z-1)

Before:

```text
| Holographic $A/4$ at cosmological horizon | Structural, conditional on H-slope and the further conditions of [GR §8.5(b)] (theory-level transport; no direct test) | [GR §5] |
```

After:

```text
(row removed)
```

### F-15

**F-15.1** — appA:110 (G9); FULL:5557 (audit site)

Before:

```text
| G9 | Dark sector budget | $\sim 95\%$ | C | 1 | Partly definitional budget | Ch 7 §7.9 |
```

After:

```text
| G9 | Dark sector budget | $1-\Omega_B \sim 95\%$ (supplied $\Omega_B$) | E | 1 | Partly definitional budget | Ch 7 §7.9 |
```

**F-15.2** — appA:115; FULL:5562 (count: necessary consequence of the class change, §A.30)

Before:

```text
**Summary statistics.** Counts: 5 C + 2 L. Total: 7.
```

After:

```text
**Summary statistics.** Counts: 4 C + 2 L + 1 E. Total: 7.
```

