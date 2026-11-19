# Focused confirmation of SIGMA12-SCREEN r2 against the review of r1

**Objects.** In `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, at
`fd77e955d6f29491cdf4a83e38f902200aae5d32`:
- `SIGMA12-SCREEN-r2.md`, blob `104bd8d7`, SHA-256 `5d1845af…6e9b753b…c419510` (agrees with the README
  row);
- `RESPONSE-SIGMA12-SCREEN-r1.md`, blob `caa5a973`.

**Baseline.** `REVIEW-SIGMA12-SCREEN-r1.md` (this reviewer), blob `4280293a`.

**Checks.** r1 is unchanged: blob `c32d54c8`, SHA-256 `e805df73…`, the same as r2's revision note
and the README row. I reworded passages of the r1 review at retention, which changes none of its
findings.

**Reviewer.** Independent, non-author, read-only. Every step was re-derived by hand. Git was used only
to read files, take blob ids and diff r1 against r2.

## Verdict: ACCEPT WITH CHANGES (one small required label fix; no re-review needed beyond checking it)

All five required findings are resolved, and so are the optional findings and nits. The new coupling
condition and the side conditions check by hand. Nothing counts under SNR-1. One label in §4
contradicts the sentence two lines above it (F1).

***

## 1. Required findings of r1

| r1 finding | Status | Where in r2 (line numbers) |
|---|---|---|
| R1: G-2 is not general; §3, SG-1, AW-σ1 and blocker 2 overstate | **RESOLVED** | G-1 split by part :121–122; G-2 under (CC), with the countercontrol, :134–149; G-6's own hypotheses :165–168; §3 rows :255–257 and closing paragraph :279–283; blocker 2 :329–330; SG-1 :358; AW-σ1 :363 |
| R2: Y on a side-2 torus | **RESOLVED** | §1 scope and the exception :74; G-1(b) "some side `≥ 3`" :126–129; (CC) "every side `≥ 3`" :142–144; §3 :255–256 |
| R3: G-6 is a second negative | **RESOLVED** (label, F1) | G-6 "Standing" :186–189; §4 J-return row :296; summary :300–305; §5 :322–323, :347–348; SG-5 :362 |
| R4: "would need blank cells" | **RESOLVED** | [A-inf] "may need", stated as open, and made conditional ("If one is needed") :297; AW-σ2 :364; §7 :373–374 |
| R5: blocker list | **RESOLVED** | C-PREP item 3 :332–334; R1 on G-ring and R4 :335–342; SUBSTATE-1 in Inputs :43–44, in Prior screens :93–99, in §4 :294 and :298, as blocker 5 :343–345, in §7 :377 and §8 :384 |

The optional findings O1–O8 and the nits N1–N2 are all applied as the response states. In particular
CURRENT-HANDOFF's location is corrected at :41–42. CALC is now cited as r2, blob `bef634e2`; its review
blob `70eddf2d` is confirmed.

## 2. Diff r1 → r2 against the response

Every substantive change traces to a row of the response. The following edits are not listed there
explicitly. Each is a consequence of a listed finding or a status update, and each is accurate:
- **:3, :5–8.** Status line and revision note.
- **:53.** Label line: "re-derived by the r1 review". This is correct; the r1 review re-derived every
  [proved here] item.
- **:290.** Added: "and only at the disproof's scope and status". This matches U1 §2.3.
- **:270.** Theorem 2(d) row: "beyond G-6's scope". This follows from R3.
- **:315.** §5: "Done, reviewed at r1".
- **:350–352.** Closing: "Y, G-ring and L" and "on Y and G-ring". This follows from O1.
- **:370–377.** §7 updates. These follow from R3, R4 and R5.

Optional: list these in the response as consequential edits.

## 3. Hand re-derivation

- **(CC) on native-Y, every side `≥ 3`.** A proper nonempty `X` on the connected torus has an adjacent
  pair `i ∈ X`, `j ∉ X`. With every side `≥ 3`, the six offsets of `i` are six distinct sites, so `j`
  occurs once in `⊕_{w∼i}`. Then `F(rδ_j)_i = H(r)`, which is nonzero for `r ≠ 0`: `H` is a bijection
  with `H(0) = 0`, inverse `(p,q,r) ↦ (r ⊕ pq, p, q)`. Under the set reading of `∼` the same holds on
  every side. **Holds.**
- **(CC) on the SM ring.** Take `i ∈ X` with `i − 1 ∉ X`; one exists because `X` is proper on a cycle.
  For `y = rδ_{i−1}`: `y_{i+1} = 0` since `i+1 ≠ i−1` (`L ≥ 3`), so `R(i,y) = i+2`; and `y_{i+2} = 0`
  since `i+2 ≠ i−1` (`L ≥ 4`). So `F(y)_i = r + 0 = r ≠ 0` in `ℤ/q`. **Holds.**
- **G-2 under (CC).** `(τs)_X = σ_X(0) = 0`, so the previous slice of `φτs` on `X` is `0`. The
  previous slice of `τφs` on `X` is the current slice of `φs` there, `F(rδ_j)|_X`, which is nonzero
  at `i`. So `τφ ≠ φτ`, and `τ` is no `φ^n`. **Holds.**
- **Countercontrol.** Over `ℤ/2`, with `F|_X ≡ 0` and `X^c` a separate component, `φ` acts on `X`
  as `(x,y) ↦ (y,x)`. So `φ = σ_X ⊕ φ|_{X^c}`, a block swap that is a time shift with `k = 1`, and
  (CC) fails. **Correct.**
- **G-1(b), some side `≥ 3`.** Take `j = v + e` along such an axis. Then `j` occurs once among `v`'s
  offsets, `F(rδ_j)(v) = H(r) ≠ 0`, and so `F ≢ 0`. **Holds.**
- **All sides 2, six-offset reading.** Each neighbour occurs twice, so the XOR cancels and
  `F ≡ H(0) = 0`. In characteristic 2, `φ(x,y) = (y, x) = σ`. **Correct.**
- **Why G-2 needs every side `≥ 3`.** Suppose one side along `e` is 2, and let
  `X = {k : k_e = 0}`. Every edge between `X` and `X^c` runs along `e` and is counted twice, so
  `F(rδ_j)_i = H(0) = 0` for every `i ∈ X`, `j ∉ X`, and (CC) fails for this `X`. So "every side" is
  the right sufficient condition. r2 says only that (CC) "can fail", which is accurate: the lemma is
  not claimed false there.

## 4. SNR-1, the blank premise and the blockers

- **G-6 is uncounted.** It is listed as a proved negative that rests on an assumed carrier
  preparation and does not count: at :186–189, :296, :304–305, :322–323 and :347–348. It is also
  stated to concern transport and return, not recording. Confirmed.
- **The blank premise.** "May need a blank supply" is marked [A-inf] and stated as open at :297, with
  the reason: a reversible conditional gate needs no ancilla. The Lemma R / G-7 consequence is
  conditional. Confirmed.
- **The blocker list.** It now covers member L's update rule, the SM class beyond SM:112, C-PREP,
  the recording screen (R1 on Y at `t ≥ 2`, R1 on G-ring beyond C-5, persistence, R3, R4, R5),
  SUBSTATE-1's member scope, interference-level statements, and review standing. I find nothing
  missing.
- **Nothing counts under SNR-1.** :12–13 and :347–348 say so. The global-reversal "not available"
  is held until review and rests on criterion clauses only.
- **Repo-text rules.** None of the barred words, no machine-local path and no closing keyword occurs
  in r2 or in the response. The MR★ quotation keeps its marked paraphrase.

## Required finding

**F1. The outcome label of the J-return row, :296.** :290 says "Only 'not available' counts under
SNR-1". :296 then labels the J-return form **Not available** and says it does not count. In U1 §2.3,
"Not available" is the outcome that counts. An action whose negative rests on an assumed input takes
the outcome "requires assumed apparatus", or "unsourced". Fix: relabel :296 (both columns) with U1's
outcome for an assumed input, for example "**Requires assumed apparatus**: no J-return before `ℓ/2`
(resp. `L/3`) relative to an assumed carrier preparation (G-6)". Keep the G-6 content and the "does
not count" sentence. Make the same wording change in the :304 bullet if it is read as an outcome
label. Nothing else changes.

## Optional

- **O1.** AW-σ2 :364, "is not a necessary premise … unless sourced". A clearer form: "is not to be
  taken as a necessary premise … unless a source shows it".
- **O2.** :297, "A native gate would be needed". Under G1 this is definitional, since any undo is
  some `φ^n`. Mark it [A-inf], or write "a native conditional operation, of which none isolated is
  found".
- **O3.** Response: add the consequential edits of §2 above.
