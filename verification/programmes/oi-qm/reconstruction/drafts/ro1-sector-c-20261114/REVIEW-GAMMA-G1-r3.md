# Focused review of GAMMA-1 unit G1, r3

**Objects.** At PR #1294 commit `9aa84f45cb2e38e94582eeb67935f5e2c25b8728`, in
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`:
- `GAMMA-G1-r3.md` (cited r3:N);
- `RESPONSE-GAMMA-G1-r2.md` (RESP).

r2 is unchanged at blob `44ff0b53`.

**Reviewer.** Independent, non-author. Read-only; hand checks only. No external source was read.

## Verdict: ACCEPT WITH CHANGES

N1, N2, the partly resolved r1 finding 8, NC-γ6 and the CALC-status minor are resolved. Every hand
check below holds. Two small required changes remain, both in the new §7.2 and NC-γ6 text:
- the default reporting of separation by scope pre-answers owner question 6 (R-1);
- C0's separation on X-4 at the data side assumes an unstated property of C0 (R-2).

Neither changes a definition's structure. Confirming them needs only a re-read of the edited
sentences.

## Dispositions

| Item | Status | Where in r3 |
|---|---|---|
| N1, credit quantifier | **RESOLVED**, with R-1 | 784–834, 693–695, 857–893 |
| N2, local statistics | **RESOLVED** | 569–651, 526–527 |
| r1 finding 8 | **RESOLVED** (through N2) | 569–651 |
| NC-γ6, status in its row | **RESOLVED** | 857: "Status at G1: open" |
| M-a, CALC r2 owner acceptance | **RESOLVED** | 58–61, 986. The quotation matches c.6892224647 as I read it |
| M-c, declared quantum reference | **RESOLVED** | 859–864; X-2 and X-3 sources marked NOT READ (G3) |
| A-b, `K_P^∅` | **RESOLVED** | 239–242 |
| A-c, re-point PROVISIONAL | **not applied**, with a reason I accept | 84–86: no U4 revision is accepted |

**Diff from r2 to r3.** Every hunk corresponds to a RESP row or to RESP's "Changes beyond the
findings": the revision note, inputs, labels, `K_P^∅`, the §5.5 `V` row, §5.7, §6, §7.2, the NC-γ6
row and evaluation, G1-F8, AW-hyb, §11 and §12 questions 5 and 6 and the G3 list. I found no
unlisted change.

## N1 re-derived by hand

**C0 at a beam splitter.** One particle per run and no dark process give `P(both) = 0`, so `α = 0`.
**Reference.** A single excitation gives `α = 0`. X-2 therefore does not separate C0, as stated.

**PC-wave.** `P(both) = E[ηtI · ηrI] = η² t r E[I²]` and `P(T) P(R) = η² t r E[I]²`, so
`α = E[I²]/E[I]² ≥ 1`, with equality iff `I` is constant. Correct.

The inequality also holds without the low-click approximation. Exact click probabilities
`1 − e^{−ηtI}` and `1 − e^{−ηrI}` are both increasing in `I`, so for this one-variable comonotone pair
`E[fg] ≥ E[f]E[g]` (Chebyshev), and `α ≥ 1` again. Recording this would remove the regime qualifier
from X-2 (advisory).

**`I_3`.**
- **C0.** `P_{XY} = P_X + P_Y` for one-path masses gives
  `I_3 = P_ABC − 2(P_A + P_B + P_C) + (P_A + P_B + P_C) = P_ABC − ΣP = 0`.
- **PC-wave.** `|f_A + f_B + f_C|²` has only pairwise cross terms, so inclusion–exclusion gives 0,
  **provided the click probability is linear in intensity.** With saturating detection
  (`1 − e^{−ηI}`), `I_3 ≠ 0` in general. State the low-click regime at r3:820–823 as it is stated
  for X-2 (minor M-1).
- **Born reference.** `I_3 = 0`.

So X-3 separates no member. Correct, given M-1.

**Credit for the reference, at the level of laws.**
- C0 is separated by `Δ`: the reference has `(+1/2, −1/2)`, C0 has `Δ ≡ 0`. Under §5.7 check 5,
  C0's a1 ratio against its own one-path sum is `u ≡ 1`.
- PC-wave is separated by X-2: `α ≥ 1` against 0.
- CC4 and CC5 are separated only by (s2) on X-1 and X-2.

So `S(K) ≠ ∅` for every member, as stated.

**No control credits itself.** Put `K` in place of `L`.
- On `o ∈ dom(K)`, (s1) needs `L = K` to agree with the data while `K` is established to disagree.
  Both cannot hold.
- On `o ∉ dom(K)`, `L = K` has no law, so it cannot agree.

Hence `S(K) = ∅` and no member is credited. Correct. The dilation family is excluded earlier,
because it is not available. Correct.

**R-1 (required). Separation by scope is a weakening, and the default pre-answers owner question 6.**
(s2) counts "`K`'s construction gives no law for `o`" as separation. That records the limits of the
declared control, not a disagreement. CC4 and CC5 then constrain nothing: any `L` that agrees with
X-1 or X-2 data separates them. This is the same gap as AW-hyb, applied to members already inside
`𝒦`. The weakening is labelled, not hidden: it is reported as "separated by scope only" and raised
as owner question 6. But r3:806–808 makes the weaker rule the default ("until it is answered, a
credit that needs (s2) … is reported as credited 'with CC4/CC5 separated by scope only'"). Owner
answer Q6 ("compatibility with classical waves alone does not establish quantum coverage") does not
license that default.
- *Required change.* Until question 6 is answered, report such a result as **credit conditional on
  owner question 6**, not as credited, and propagate this to G1-F8 and NC-γ6's "creditable" (r3:879,
  955).
- *Fact for the owner.* Under (s1) alone, even the quantum reference is not creditable on the
  present list. r3:1021–1024 already says this correctly.

**R-2 (required). C0's separation on X-4 at the data side assumes a phase-independent C0 response
(r3:870–872, :881–885).** Schwindt's `V` is a phase scan with the analyzer removed (LIT 1.12).
C0 as defined (r3 §7.1) fixes `r_π` "independent of whether the other path is open and of the
marker", not of a phase setting on one arm. A C0 whose per-path response varies with arm length gives
`V > 0` in a two-path phase scan while staying additive. So "C0 has no fringes at any marking
setting" holds only if:
- `r_π` is declared independent of the phase setting, which is a restriction to state in C0's
  definition, consistent with OCP:35's "Fix the screen response per path"; or
- the separation goes through `Δ`, with one-path counts at the same phase settings, which LIT does
  not record.

At the level of laws, C0 is still separated by `Δ`, as stated.
- *Required change.* Add the phase-independence clause to C0, with its ground, or move C0's data-side
  separation to "waits on G3", as for PC-wave. Also, the quoted Schwindt result "V > 4.4% even though
  L > 99.9%" is far below `v_+`. The separation rests on Schwindt's quantitative `V` (§5.7), not on
  the qualitative rule.

## N2 re-derived by hand

**The 16-cell counterexample.**
- With `c₁ = (0×12, 4, 2, 0, 2)` and `c₂ = (0×12, 0, 2, 4, 2)`, the pair normalizer is
  `n = (0×12, 4, 4, 4, 4)`.
- `J` is cells 13–16 (`n ≥ 0.4`), and `u₁ = (1, ½, 0, ½)`.
- `V_u = 1`, and cell 15 is an interior strict minimum of the run, so fringes are present.
- The total is constant on `J`, so against an envelope-proportional one-path normalizer it is
  absent.
- **Classified fringes and antifringes.** Correct.

**A fringe-free envelope.**
- **Equal channels:** `u ≡ ½`, so it is absent.
- **Shifted partner:** `u = 1/(1 + e(j − δ)/e(j))`. For log-concave `e`, `log e(j − δ) − log e(j)`
  is monotone in `j`, so `u` is monotone and the envelope is absent.
- **sinc² is log-concave on its main lobe:** `(log (sin x/x)²)″ = 2(1/x² − 1/sin² x) < 0` for
  `0 < |x| < π`, since `|sin x| < |x|`.
- **The support floor:** the first side lobe peaks at about 0.047 of the maximum, below `ν = 0.1`,
  so `J` lies in the main lobe for small shifts.

Correct.

**OCP's table.**

| Protocol | Ratio `u` | Classification |
|---|---|---|
| a6, pair | `(1, 0)` | fringes present |
| a6, total, against `c_{a2} + c_{a3} = (½, ½)` | `(1, 1)` | absent |
| a5 | `(½, ½)` | absent |
| a1 | `(2, 0)`, with `V_u = 1` | present |
| a4 | `(1, 1)` | absent |

So a6 is fringes and antifringes, matching OCP:19–24.

**The standard two-slit law.**
- **a1:** `u = 1 + cos θ_j`, with `V_u = 1` and interior extrema, so present.
- **a4 at full marking:** `u ≡ 1`, so absent.
- **`R01`, `R02`:** the pair ratio is `cos²(θ_j/2)`, so present; the total is `∝ e`, so absent.
- **Robustness:** with unequal channel efficiencies the ratio is `Ac/(Ac + Bs)`, which still runs
  from 0 to 1, so `V_u = 1` survives.
- **`R03 = R04`:** absent.

Correct.

**Vacuity countercontrol.**
- **C0:** `u ≡ 1`, a miss against a source showing fringes.
- **In-phase pair:** ratio ½, absent, a miss.
- **Quarter-period pair:** the total gives `u ∈ [1 − √2/2, 1 + √2/2]`, so `V_u = √2/2 ≥ 0.5`. It is
  present, so the pair is not classified fringes and antifringes.

The rules can return misses. Correct.

**Standing of the rules.** They are fixed in advance, use no source value, and fail false and correct
laws symmetrically. They do not beg agreement. A channel with no declared normalizer within `I` is
reported as untested, not as agreeing. That is explicit, and it is the same O11 limit as before. The
§5.5 change, which uses the source's own `V` formula and scan and adds no spatial-to-phase comparison
without `κ_scale`, closes the r2 envelope problem on the quantitative side as well.

## Other items checked

- **`K_P^∅ = η`.** Check 4's marker has `c_L = (L: ηd, ∅: (1 − η)d)` and
  `c_R = (R: ηd, ∅: (1 − η)d)`. Then `Σ|·| = 2ηd` and `Σc = 2d`. Correct.
- **Owner question 6** is new (r3:1021–1024). It correctly states that (s1) alone credits nothing on
  the present list. It names MR-1's T7 as a test outside the list, which VER2 records as conditional
  (not checked here).
- **AW-hyb** (r3:830–834, 956) is a correct statement of the rule's limit. A rule stated member by
  member cannot exclude a hybrid that matches the reference's own pattern.

## Minor and advisory

- **M-1.** State the linear (low-click) detection regime for PC-wave's `I_3 = 0`.
- **Advisory.** Record that `α ≥ 1` holds for any detection probability increasing in `I`
  (comonotone), not only at low click rates.

## Not checked

- VER2's CC4 and CC5 scopes and its T7 entry.
- The external X-2 and X-3 sources, which are NOT READ and G3's to read.
- U4 r2 and r3.

## Confirmation (fixes at `2ffd68ef`)

The G1 r3 file was diffed from `85bfd162` to `2ffd68ef`; it is the only G1 file changed. Every hunk
maps to R-1, R-2, M-1 or the advisory, and nothing else in the file changed.

| Item | Status | Where in the r3 file at `2ffd68ef` |
|---|---|---|
| R-1 | **RESOLVED** | 806–808 report scope-only credit as "credit conditional on owner question 6, not as credited". The same is carried into the NC-γ6 row (862), into the hand evaluation (886–888) and into G1-F8 (968). No unconditional "creditable" remains. Line 888 correctly states that under (s1) alone the reference is not creditable |
| R-2 | **RESOLVED**, by the second option | 877–880 no longer count X-4 for C0, and give the reason. 889–899 make C0's data side wait on G3 (`Δ` or X-1), give the ground for not adding the phase clause, and drop the Schwindt quotation. C0's law-level separation by `Δ` is kept |
| M-1 | **RESOLVED** | 825–828 restrict PC-wave's `I_3 = 0` to linear detection and note that saturating detection gives `I_3 ≠ 0` in general. G1-F8 carries "in the linear detection regime" |
| Advisory | **RESOLVED** | 819–821 state the comonotone Chebyshev bound, with exact Poisson clicks given as an example. It is correct |

No remaining findings. Verdict on G1 r3 with these fixes: **ACCEPT**.
