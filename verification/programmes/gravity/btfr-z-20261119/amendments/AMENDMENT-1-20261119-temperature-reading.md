# BTFR-z amendment 1 (2026-11-19): the a₀(z) scaling and temperature reading under test

**Status of this amendment.** `PREREG.md` (commit `7b51814046c351b0060eb9413dc4d985f08b91b1`,
pushed 2026-11-19T22:35Z) is frozen and is not edited. This amendment was written **after** the
preregistered analysis had been run and its result was known. It therefore adds no test, changes
no rule, prediction, budget or verdict, and states only which reading the frozen test applies to.

**Trigger.** The G3-HOM draft record on PR #1430 (branch `research/g3-hom-20261119`, head
`460562614d57ff4516dfa048ad090e3792c3f43e`, `verification/programmes/gravity/drafts/g3-hom-20261119/RESULT.md`
§3.4, WIP and unreviewed) observes that GR §7.3's a₀ = cH/6 uses the de Sitter temperature H/2π, and
that a different off-de-Sitter temperature changes the predicted a₀(z). The event-horizon reading
differs from the Hubble reading by 0.31 dex at z = 2. That record asks the BTFR-z preregistration
to state which temperature it tests. `PREREG.md` §1 states the scaling a₀(z) = cH(z)/6 and the
instantaneous Hubble horizon c/H(z). It does not name the temperature reading against the
alternatives that `papers/GR.md`:56 itself lists. This amendment closes that gap.

## 1. The reading the preregistered test applies to

The test applies to **GR §7.3 as written**:

- a₀(z) = cH(z)/6, with H(z) the supplied flat background of PREREG §2.1.
- The temperature is the de Sitter (Gibbons–Hawking) form T = ħH/(2πk_B), evaluated with the
  instantaneous H(z). The surface is the Hubble/apparent horizon R_A = c/H(z), whose surface gravity
  is taken to be H, with no Ḣ correction.

Every prediction labelled OI in `PREREG.md`, `results.json` and `RESULT.md` (P_asym, P_vmax) is
for this reading. So is every OI verdict.

The test does **not** apply to the other readings that `papers/GR.md`:56 names for generic FLRW:

- the Hayward–Kodama apparent-horizon temperature T_A = (ħH/2πk_B)|1 + Ḣ/(2H²)|;
- the cosmological event horizon R_E = a∫_t^∞ c dt′/a, with T = ħc/(2πk_B R_E).

`main` adopts neither of them for §7.3. Neither was preregistered here, so no verdict about either
follows from this unit.

## 2. Post hoc description of the other readings (not a test)

`scripts/readings_posthoc.py` takes a₀ ∝ the horizon surface gravity, as in G3-HOM §3.4. It
reads the measured O and σ_O from `results.json` and evaluates each reading at Ω_m = 0.3153 and
at the bins' median redshifts (0.900, 2.228). It uses the asymptotic form and the spherical,
simple-ν forward model of `oi_model.py`. The script's control reproduces G3-HOM's
H₀R_E0 = 1.147 at Ω_m = 0.31, giving 1.1466.

| Reading | a₀(2)/a₀(0) | dex below Hubble at z = 2 | T2 P_asym | z | T2 P_vmax | z | T1 z~0.9 z | T1 z~2.3 z |
|---|---|---|---|---|---|---|---|---|
| Hubble (tested) | 3.033 | 0 | −0.299 | 4.15 | −0.200 | 3.30 | 1.36 | 1.33 |
| Hayward–Kodama apparent horizon | 1.215 | 0.40 | −0.136 | 2.75 | −0.096 | 2.41 | 2.84 | 0.82 |
| Event horizon | 1.472 | 0.31 | −0.116 | 2.58 | −0.092 | 2.38 | 2.29 | 0.44 |

These z values use σ_O only and evaluate the predictions at the median redshifts, so the Hubble
row differs slightly from the preregistered per-galaxy means in `RESULT.md` (T2 z = 4.25 and 3.29
there). The other two rows are recorded so that G3-HOM, or any later unit that adopts a reading,
can preregister its own test. Selecting a reading here because it fits the observed T2 better would
be the adjustable variant that §A.29 rejects. No reading is selected.

**Goal link (§A.47).** Unchanged from `PREREG.md`. This amendment fixes the scope of the existing
test.
