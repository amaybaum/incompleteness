# Confirmation re-check: Introduction design r7 (the r6→r7 diff only)

- **Object.** #918 at `03730dec` (`S/pintro/repo`): `design/{OUTLINE,CLAIMS,CHANGES,DEPENDENCIES}-r7.md`.
- **Method.** Read the word diffs against r6 (`git diff --no-index --word-diff`).
  - The committed `review/r6/RECHECK.md` is byte-identical to mine.
  - `SHA256SUMS` verifies clean.
  - New source lines were checked at `687e885b`.
- **Read-only.** No repository file was changed.

## Verdict: ACCEPT WITH NITS (ready to draft from)

C1–C6, nits 1–9 and the Weinberg landing gate are all applied. The three departures are sound. Nothing else in the
diff changes claim strength. Both nits below are optional.

## 1. Items

| Item | r7 | Result |
|---|---|---|
| C1 | N-BH2 s2, N-BH3, §6.2 item 4 (OUTLINE); N-BH2, N-BH3 (CLAIMS); DEPENDENCIES §C | Applied at all six sites. A grep finds no surviving "only when", "holds only" or "only on" in the A.8 sense |
| C2 | OUTLINE §5 item 2; CLAIMS N-BH1 | Applied: the definition of accessible advantage, and the bijectivity condition on both endpoint guarantees |
| C3 | OUTLINE §6.1; CLAIMS N-DI1 | Applied verbatim |
| C4 | register PD; S-1 | Applied: rationality, \|C_V\| ≥ 2, the label corrected to s4 |
| C5 | register SI; r4:114 s1 | Applied, recorded as a restored hypothesis |
| C6 | Page budget and Fit | Applied: ≈ 4,430 words, ≈ 11.2 pp; applications ≈ 2.4 pp; saving ≈ 140 words net; slack ≈ 0.8 pp |
| Nits 1–8 | — | Applied. No `r4:162` remains in OUTLINE-r7. The N-DT1 black-hole clause now carries the covariant field equations, so the R14 claim holds |
| Nit 9 | DEPENDENCIES §A (7 sites), §R (GR:164, ch07:65) | Applied. Each row is sourced to #937 at `5221b53e`, and the quoted text matches the lines at `687e885b` |
| Weinberg gate | OUTLINE §4 item 1; CLAIMS §L; DEPENDENCIES §H | Applied as a landing gate |

## 2. Departures

1. **C2: "32 non-injective maps of {0,1}² violate this bound".**
   - **Correct.** BH-01 REPORT:155 tabulates "maps of `{0,1}^2`, two-bit message, one register read: violations of
     `P_succ >= 1/2`, bijective / non-injective — 0 / 32". REPORT:21 has the count without the domain. `result.json`
     records `nonbij_violate: 32`.
   - The clause is r4's reviewed wording, and it reinforces the bijectivity condition that C2 restored.
   - Splitting the final clause into its own sentence changes nothing.
2. **C1: "is established only for a full-product shell" (N-BH3; §6.2 item 4).**
   - **Correct as a statement about the evidence, with no necessity claim.** "Established" makes it epistemic.
   - It is exactly what DIFF-RECHECK §5 N1 supports. A.8's value is established, under H-scramble and the closure,
     when Σ_E = H_B⊗H_R. It is established for no proper shell, and on proper shells it fails in general (the
     diagonal shell gives H_m − 1).
   - It does not say the value *holds* only there, so it does not exclude a special proper shell whose Haar mean
     coincides with Page's.
   - N-BH2 and DEPENDENCIES carry the complementary "holds … / fails in general" form. The two forms are consistent.
3. **C3: planning note "Bell correlations … need H-Bell".**
   - Accurate in substance, and not paper text.
   - Strictly, quantum Bell values need ontic parameter dependence, given that measurement independence is kept.
     H-Bell is the open hypothesis that this choice is compatible with operational no-signalling and the continuum
     limit (r4:234 (5); Main:22). See nit 2.

## 3. Nothing else changes claim strength

The rest of the diff is:
- budget figures;
- provenance (the pre-scope path, revision headers);
- source additions (BH-01 REPORT:21, :24; DIFF-RECHECK §5 N1);
- N-LIT2 written out, identical to r5's reviewed text;
- the DEPENDENCIES rows.

No permitted sentence other than the C1–C5 targets and nits 2–4 changed wording.

## 4. Nits (optional)

1. **CLAIMS N-BH1 / OUTLINE §5 item 2, source note.** Add BH-01 REPORT:155 beside :21, because :155 names the
   domain ({0,1}², one register read, bound 1/2).
2. **OUTLINE §6.1 planning note.** "they need H-Bell" → "they need ontic parameter dependence, whose compatibility
   with operational no-signalling and the continuum limit is the open hypothesis H-Bell (§3.2, Bell structure)".

A stale label for the record: DEPENDENCIES-r7 §H's #936 row still says "r6's wording holds without it". The file's
header note covers it ("'r6' below refers to the paper design").
