# PROV-CORR — provenance-correction coverage ledger

**Status.** Writer's correction ledger for manuscript correction unit PROV-CORR. Independent
exact-head review of `e2c04e8d`: REVISE (minor), answered in "Round 1 revision" below; review of the
revised head pending, and merge is a separate owner decision. Paper corrections only: no
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
| F-3 | ch03:118, FULL:979; Str:903; Sub:375 (audit's related site); round 1: Sub:451, Str:179, GR:683 | GR:482; AUDIT §2.4 Test N | a₀ removed from the class-specific list and from Structure's Level 3 table; Sub:375 states the import as Sub:419 does; dark-sector phenomenology no longer listed among OI's distinguishing predictions | F-3.1–3.6 |
| F-4 | ch09:149, FULL:2564 | GR:547 "normalization comparison open" (ch07 summary table agrees) | "confirmed empirical relation" → "normalization comparison open" | F-4.1 |
| F-5 | ch09:258, FULL:2673 | GR:318, :482; appA:117 | 1/4 and a₀ removed from the "substrate-computable record" | F-5.1 |
| F-6 | ch05:59, :61, FULL:1374, :1376; Sub:88; ch02:120, FULL:750 (round 1: ch05:59, :61 again) | GR:420 "Its use as a physical source is a separate question"; GR:422, :430, :444 | Flatness no longer "structurally explained" or "a structural feature"; ρ_s = ρ_crit stated as the restated flat Friedmann density; Ω_total (inferred) separated from ρ_s; use as a filter conditional on the open source identification | F-6.1–6.6 |
| F-7 | SM:30 | GR:428–430, :440 (ε and σ cancel) | Wrong provenance ("through ε = 2√σ l_P") replaced by the inputs that survive; filter made conditional | F-7.1 |
| F-8 | SM:180, :200, :1424; Sub:157; propagation SM:212, ch05:75, FULL:1390 | GR:430, :440, :444; AUDIT §2.3 | Anthropic rebuttal made conditional on the source identification; "passes exactly", "independently excludes", "framework-internal" removed; ratio attributed to first law, V/A and Friedmann | F-8.1–8.6 |
| F-9 | SM:196 | GR:428–430, :440 | Over-conditioning removed: ε and σ cancel from ST, which uses no calibration | F-9.1 |
| F-10 | GR:470, :510; ch07:260, :262, FULL:2125, :2127; propagation ch07:284, FULL:2149 | GR:478–488 (values contain c, H, G, M_B and the imported factor); AUDIT §2.4 | Conditions on T_dS attached to the entropy-displacement chain; the displayed values stated not to contain ΔS | F-10.1–10.6 |
| F-11 | ch07:262, FULL:2127 | GR:472–476 "the Clausius relation applied to the boundary reservoir" | "Bekenstein bound" → "Clausius relation at T_dS" | F-11.1 |
| F-12 | GR:689 | GR:308, :318–320 | "quantitative consequences specific to it" → the calibration and the count's agreement with the Hawking-temperature 1/4, relations kept | F-12.1–12.2 |
| F-13 | GR:108, :160; ch07:65, :61, FULL:1930, :1926; round 1: GR:32, ch07:12, FULL:1877, Sub:375 | GR:308 "self-consistency condition, not an independent determination"; Sub:179; appB:169 | "ħ is derived, not free" / "derives ħ from G and ε" → ħ fixed as a function of boundary quantities; the relation fixes ε/√σ from measured ħ | F-13.1–13.7 |
| F-14 | Str:904 | GR:318–320; Str:882 (the 1/4 already at Level 1) | Row removed from the Level 3 (OI universality-class) table | F-14.1 |
| F-15 | appA:110 (G9), :115; FULL:5557, :5562; round 1: Sub:375 | GR:454, :545 "uses the supplied baryon fraction" | G9 class C → E, formula shows the supplied Ω_B; count 5 C + 2 L → 4 C + 2 L + 1 E (total 7 unchanged); layer 1 → —; Sub:375's dark-sector clause states the supplied Ω_B and the proposed source identification | F-15.1–15.5 |
| Z-1 | GR:689; ch09:258, FULL:2673; Str:904 | GR:158 "consequences of it, not independent checks of it"; GR:306–308 | Calibration and its rewrite no longer presented as substratum consequences or a substrate-computable record | via F-12.1, F-5.1, F-14.1 |
| Z-2 | GR:108, GR:160; round 1: GR:32, ch07:12, Sub:375 | GR:308; Sub:179 | ħ no longer presented as derived in value | via F-13.1, F-13.2, F-13.5–13.7 |

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
   definition the row meets. Its layer is "—" from round 1 (N3), for the reason given for G6.

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
| #1458 review record (round 1, owner account, 2026-11-20T15:40:38Z) | Round 1 revision | Provenance |
| #1448 comment (round 1, N6) | Overlap note: Str:903 removed by F-3.2; Str:924 stays open there | Provenance |

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

## Round 1 revision (review of `e2c04e8d`, REVISE minor)

The review found three paraphrases not propagated (B1–B3) and five nits (N1–N6, N8). Each is
answered by a propagation row of the same finding; the blocks below quote the head `e2c04e8d` text
and its replacement exactly.

| Item | Rows |
|---|---|
| B1 (Z-2 / F-13): §3 or Section 7.3 "derives" ħ; Sub:375 "determines" ħ and ε "as the unique simultaneous solution" | F-13.5, F-13.6, F-13.7 |
| B2 (F-15 / F-6): Sub:375 dark sector "as a structural feature" | F-15.3 |
| B3 (F-3): Sub:451 lists dark-sector phenomenology among OI's distinguishing predictions | F-3.4; re-grep added Str:179 (F-3.5) and GR:683 (F-3.6) |
| N1, N2 (F-6): ch05:59 comparison wording; ch05:61 "(deficit, requiring an unsourced gravitational contribution)" | F-6.5, F-6.6 |
| N3 (F-15): G9 layer | F-15.4, F-15.5 |
| N4 (F-10): ch07:260 omits G and Step 3's law | F-10.6 |
| N5 (F-12): GR:689 equivalence to the calibration (GR:158) | F-12.2 |
| N6: #1448 overlap | Comment posted on #1448; Str:924 "all consistent with current data" stays open there |
| N7 | Judgments accepted; no change |
| N8: ch03:120, Str:439, :451, :463, :497 | Outside this audit; follow-up candidates only, unchanged |

**Hunks.** Against `e2c04e8d` the revision has 18 `.md` hunks (12 in source files, 6 in FULL), one
per row-site below. Against the base `dca41f64` the unit's `.md` diff has 57 hunks: the 51 above
plus 6 new lines (GR:32, GR:683, Str:179, Sub:451, ch07:12, FULL:1877); every other revision hunk
falls on a line already in the 51. Rebuilt: GR, Structure, Substratum (pages 84, 94, 53) and the
book (489), no dropped glyphs. The SC-42 integration result is unchanged by the revision (its
mirror predicates quote line prefixes that did not change) and reproduces under `-O`; controls
unchanged.

**Re-grep after the revision.** "derives the emergent action scale" 0; "determines the emergent
action scale" 0; "unique simultaneous solution" in `papers/*.md` and `book/*.md` 2 outside FULL, each mirrored there:
ch07:12 ("Section 7.4 fixes … as the unique simultaneous solution of the action-scale relation and
the definition of the Planck length": the Planck length carries the measured ħ, so the clause
states the calibration) and ch02:112 (on the audit's agreeing list; the same sentence says it
"fixes only the ratio $\epsilon/\sqrt{\sigma} = 2\,\ell_P$");
"dark sector corollary as a structural feature" 0; "dark-sector phenomenology" survives at GR:28,
:30 and :637 (tier assignment with its conditions and imported factor stated) and ch06:349 (a
chapter preview naming the topic), none of which lists it as a distinguishing prediction.
Surviving "derive(s) … ħ" wordings: ch07:36 (scope stated in the same sentence: the relation, not
the value; the review accepted it), appC:222–241 (the circularity objection and its answer, which
fix ħ "in terms of ε"), Sub:193, :195 ("fixes the relation"), GR:565 (negative), book/README.md:98
(an appendix-B contents line naming the gap-equation relation).

**F-13.5** — GR:32 (review B1; propagation of F-13 / Z-2)

Before:

```text
§3 derives the emergent action scale $\hbar$ from the classical horizon temperature by thermal self-consistency, the calibration $\hbar=\tau_K/\beta_E$ of §2.3;
```

After:

```text
§3 obtains the relation of the emergent action scale $\hbar$ to the boundary quantities from the classical horizon temperature by thermal self-consistency, the calibration $\hbar=\tau_K/\beta_E$ of §2.3, which fixes $\epsilon/\sqrt{\sigma}$ from the measured $\hbar$;
```

**F-13.6** — ch07:12; FULL:1877 (review B1)

Before:

```text
Section 7.3 derives the emergent action scale $\hbar = c^3 \epsilon^2 / (4G\sigma)$,
```

After:

```text
Section 7.3 obtains the action-scale relation $\hbar = c^3 \epsilon^2 / (4G\sigma)$,
```

**F-13.7** — Sub:375, first clause (review B1)

Before:

```text
this projection determines the emergent action scale $\hbar = c^3 \epsilon^2 / (4G\sigma)$ from thermal self-consistency ([GR, §3]), fixes the discreteness scale $\epsilon = 2\sqrt{\sigma}\, l_p$, for an entropy $\sigma$ per boundary mode ($\epsilon = 2 l_p$ at one nat per mode), as the unique simultaneous solution ([GR, §4]),
```

After:

```text
this projection gives the action-scale relation $\hbar = c^3 \epsilon^2 / (4G\sigma)$ from thermal self-consistency ([GR, §3]), which, with the measured $\hbar$, fixes $\epsilon = 2\sqrt{\sigma}\, l_p$, for an entropy $\sigma$ per boundary mode ($\epsilon = 2 l_p$ at one nat per mode) ([GR, §4]),
```

**F-15.3** — Sub:375, dark-sector clause (review B2; propagation of F-15 and F-6)

Before:

```text
a ~$95\%$ dark sector corollary as a structural feature rather than a new particle species;
```

After:

```text
a nonbaryonic fraction $1-\Omega_B\approx95\%$, using the supplied baryon fraction, on the proposed identification of the boundary energy as its source rather than a new particle species ([GR, §7.2]);
```

**F-3.4** — Sub:451 (review B3; propagation of F-3)

Before:

```text
OI's specific predictions (Cabibbo angle $1/(\pi\sqrt{2})$, Koide ratio $2/3$, dark-sector phenomenology) are real at this level,
```

After:

```text
OI's specific predictions (Cabibbo angle $1/(\pi\sqrt{2})$, Koide ratio $2/3$) are real at this level,
```

**F-3.5** — Str:179 (re-grep under B3: the same list of distinguishing predictions)

Before:

```text
- *Level G3 × Level D predictions* — Cabibbo angle $1/(\pi\sqrt{2})$, Koide ratio $2/3$, dark-sector phenomenology. Distinguishes OI
```

After:

```text
- *Level G3 × Level D predictions* — Cabibbo angle $1/(\pi\sqrt{2})$, Koide ratio $2/3$. Distinguishes OI
```

**F-6.5** — ch05:59; FULL:1374 (review N1)

Before:

```text
inferred under the standard cosmological model — is compared in the framework's gravitational sector developed in Chapter 7 with the thermal energy of the horizon's boundary modes.
```

After:

```text
inferred under the standard cosmological model — enters the framework's gravitational sector developed in Chapter 7 through a comparison of the thermal energy of the horizon's boundary modes with the flat critical density.
```

**F-6.6** — ch05:61; FULL:1376 (review N2)

Before:

```text
at $d = 4$ the ratio is $2/3$ (deficit, requiring an unsourced gravitational contribution).
```

After:

```text
at $d = 4$ the ratio is $2/3$ (deficit).
```

**F-15.4** — appA:110 (G9); FULL:5557 (review N3: layer)

Before:

```text
| G9 | Dark sector budget | $1-\Omega_B \sim 95\%$ (supplied $\Omega_B$) | E | 1 | Partly definitional budget | Ch 7 §7.9 |
```

After:

```text
| G9 | Dark sector budget | $1-\Omega_B \sim 95\%$ (supplied $\Omega_B$) | E | — | Partly definitional budget | Ch 7 §7.9 |
```

**F-15.5** — appA:115; FULL:5562 (review N3: why G6 and G9 have no layer)

Before:

```text
**Summary statistics.** Counts: 4 C + 2 L + 1 E. Total: 7. G11, an open research target, is not counted.
```

After:

```text
**Summary statistics.** Counts: 4 C + 2 L + 1 E. Total: 7. G11, an open research target, is not counted. G6 and G9 have no substratum layer: G6's factor is imported, and G9 uses the supplied baryon fraction.
```

**F-10.6** — ch07:260; FULL:2125 (review N4)

Before:

```text
they are fixed by the imported factor and the measured $H$.
```

After:

```text
they are fixed by the imported factor, $G$ and the measured $H$, with Step 3's deep-regime law.
```

**F-12.2** — GR:689 (review N5, GR:158)

Before:

```text
and the count's agreement with the $1/4$ coefficient fixed by the Hawking temperature and the first law, under the conditions of §8.5(b)).
```

After:

```text
and the count's agreement with the $1/4$ coefficient fixed by the Hawking temperature and the first law, which is equivalent to that calibration, under the conditions of §8.5(b)).
```

**F-3.6** — GR:683 (re-grep under B3: dark-sector phenomenology as falsifying OI's specific representative)

Before:

```text
a measured deviation from the dark-sector phenomenology would falsify OI's specific representative without necessarily refuting the universality class.
```

After:

```text
a measured deviation from the dark-sector phenomenology would falsify the conditional entropy-displacement account of §7.2–§7.3 without necessarily refuting the universality class.
```

