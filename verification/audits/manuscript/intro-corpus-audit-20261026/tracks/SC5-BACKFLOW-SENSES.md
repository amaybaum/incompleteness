# "Backflow" senses across the corpus (SC-5 input; WIP)

Read-only classification at `main` `a5168789`, `papers/*.md` and `book/*.md`. Two senses:
- **CMI** — positive conditional mutual information I(X_<k; X_{k+1} | X_k) > 0, i.e. conditional memory in the
  multi-time law. This is what Main's "Lemma (accessible backflow from readback)" (:167) proves from a (C4) gap.
- **BLP** — Breuer–Laine–Piilo trace-distance revival, which witnesses P-indivisibility of the one-time maps (Main
  :149, Explainer :143, ch01 :103).

Labels: C = CMI, B = BLP, X = conflated (one sense used to conclude the other), A = ambiguous, O = other.

The corpus has 159 occurrences on 125 lines: papers 62 on 55 lines, book chapters 97 on 70 lines. FULL.md has 96
occurrences on 69 lines, every one identical to a chapter line, and none appears only in FULL. book/README.md:90 is the
only book line with no FULL mirror.

## Totals (occurrences)

| file | C | B | X | A | O | total |
|---|---|---|---|---|---|---|
| Main | 14 | 3 | 2 | 0 | 3 | 22 |
| Complexity | 4 | 6 | 4 | 3 | 0 | 17 |
| Explainer | 3 | 2 | 4 | 2 | 0 | 11 |
| GR | 2 | 0 | 1 | 0 | 0 | 3 |
| Substratum | 3 | 0 | 0 | 0 | 0 | 3 |
| Medicine | 1 | 1 | 0 | 0 | 0 | 2 |
| Bioinformatics | 1 | 1 | 0 | 0 | 0 | 2 |
| SM | 0 | 0 | 0 | 1 | 0 | 1 |
| Structure | 0 | 0 | 0 | 1 | 0 | 1 |
| **papers** | **28** | **13** | **11** | **7** | **3** | **62** |
| README | 1 | 0 | 0 | 0 | 0 | 1 |
| appendix-a | 1 | 0 | 0 | 1 | 0 | 2 |
| appendix-b | 3 | 1 | 3 | 0 | 0 | 7 |
| appendix-c | 0 | 0 | 1 | 0 | 0 | 1 |
| ch01 | 1 | 2 | 6 | 1 | 0 | 10 |
| ch05 | 0 | 0 | 1 | 0 | 0 | 1 |
| ch13 | 0 | 2 | 10 | 0 | 0 | 12 |
| ch15 | 0 | 6 | 19 | 10 | 0 | 35 |
| ch16 | 2 | 0 | 0 | 0 | 0 | 2 |
| ch17 | 1 | 1 | 0 | 0 | 0 | 2 |
| ch18 | 2 | 1 | 14 | 0 | 0 | 17 |
| glossary | 1 | 1 | 3 | 2 | 0 | 7 |
| **book** | **12** | **14** | **57** | **14** | **0** | **97** |

**The 𝒩-regime family.** 43 of the 57 book conflations come from the "maximal / intermediate / weak backflow" regime
vocabulary: ch13 ×10, ch15 ×16, ch18 ×14, glossary ×3. It takes the P-indivisibility measure 𝒩 (identified at ch18:78
with the BLP and Rivas–Huelga–Plenio measures), ties it to C3 capacity and τ_S/τ_B, and calls it "memory strength".
Its anchor sentences are ch18:74 = FULL:4892, glossary:115 = FULL:6715, ch15:144 = FULL:4105 and ch13:134 = FULL:3633.

## Per-line labels (chapter line [FULL mirror])
- **Main:** 76 C; 80 C; 149 B; 153 X; 155 C; 163 C (lemma name, and "above" is wrong: the lemma is at :167); 167 C
  (definition); 170 O (probe file); 172 C; 174 C; 196 X; 332 B (guard E10 pins this sentence word for word); 334 C, B;
  508 C ×3; 624 O; 716 C ×2; 738 C; 808 O (title of reference [9]).
- **Complexity:** 17 C; 368 X; 370 C (lemma name); 418 B (its proposed test is history-conditioned, i.e. CMI-type); 420 B;
  422 B; 428 X; 430 B; 461 X; 472 B; 474 C (lemma offered as a tool for P-indivisibility, borderline); 488 B; 490 A ×2;
  498 A; 507 C; 509 X.
- **Explainer:** 143 B ×2; 177 X; 266 C; 351 C; 725 X; 767 A; 826 A; 892 X; 896 X; 928 C.
- **GR:** 20 C; 142 C (lemma name); 589 X.
- **Substratum:** 111 C; 136 C; 262 C (lemma name).
- **Medicine:** 126 C; 423 B.
- **Bioinformatics:** 44 C, B.
- **SM:** 306 A.
- **Structure:** 1280 A.
- **book/README:** 90 C.
- **appendix-a:** 153 [5690] C; 172 [5709] A.
- **appendix-b:** 22 [5789] C (lemma name); 96 [5863] B, X; 420 [6187] X; 422 [6189] C (Lemma B.7.4 name); 424 [6191] C, X.
- **appendix-c:** 104 [6350] X.
- **ch01:** 103 [447] B ×2; 129 [473] X; 133 [477] X; 155 [499] X ×2; 207 [551] A; 217 [561] X; 223 [567] C; 282 [626] X.
- **ch05:** 95 [1424] X.
- **ch13:** 20 [3519] X(N) ×2; 68 [3567] X(N); 80 [3579] B; 124 [3623] B; 134 [3633] X(N) ×3; 136 [3635] X(N);
  138 [3637] X(N); 140 [3639] X(N); 144 [3643] X(N).
- **ch15:** 18 [3979] B; 20 [3981] X(N) ×2; 30 [3991] A; 32 [3993] X; 99 [4060] B; 101 [4062] B; 103 [4064] B;
  112 [4073] X; 122 [4083] B; 126 [4087] X; 130 [4091] B; 132 [4093] A ×2; 136 [4097] A; 138 [4099] A ×2;
  142 [4103] X(N) ×4; 144 [4105] X(N) ×2; 146 [4107] X(N); 152 [4113] X(N) ×6; 154 [4115] X(N); 226 [4187] A;
  244 [4205] A ×2; 256 [4217] A.
- **ch16:** 68 [4298] C ×2.
- **ch17:** 168 [4747] B; 194 [4773] C. :194 contradicts :168, which reserves "genuine information backflow" for
  P-indivisibility.
- **ch18:** 16 [4834] X(N) ×2; 74 [4892] X(N) ×2 (anchor); 76 [4894] X(N); 78 [4896] B, X(N); 80 [4898] X(N);
  84–87 [4902–4905] X(N) ×4 (table); 90 [4908] X(N); 92 [4910] X(N) ×2; 289 [5107] C; 311 [5129] C.
- **glossary:** 29 [6629] X(N); 91 [6691] A (the definition entry); 105 [6705] C, B; 109 [6709] A; 115 [6715] X(N) ×2
  (anchor).

## Citations of the lemma by name
- **As "backflow":** Main:163, :167, :716; Complexity:370, :474; Explainer:892; GR:142, :589; Substratum:262;
  appendix-b:22 [5789], :422 [6189].
- **As "readback lemma":** Main:141, :174, :624 ×2, :733; GR:20.
- **As "accessible-timescale lemma":** Complexity:507; Explainer:173, :177, :1006; ch01:121 [465], :133 [477].
- **As "Lemma B.7.4":** appendix-b:420 [6187].
- **Name citations that draw the P-indivisibility conclusion:** Explainer:177, :892; GR:589; ch01:121, :133;
  appendix-b:420, :424. Complexity:474 is borderline.

## Guard, ledger and code references
- **LEDGER.json:**
  - id `MAIN:L-accessible-backflow-from-readback` (:516), with label, fingerprint `afbdefe369fdd5a0` and probe
    `c4_backflow_probes.py`;
  - the C3 corollary note at :1088 uses the CMI sense.
- **Frozen audit records** cite the lemma id: `f29-followups-20261026/CHANGE-NOTE.md:141` and `review/CONFIRM.md:17`;
  `hbar-theta0-20261026/CHANGE-NOTE.md:9`.
- **`edge_rigidity_probe.py`** never references the lemma name. Its "backflow" hits:
  - :2385 bans 'recurrence alone gives backflow';
  - guard E10 (:8609, mutation test :8780–8781) pins Main:332 verbatim;
  - :8858 and :10794 are message text;
  - guard E7 (:8578) pins "Accessible finite-horizon memory" (Main:334), not the word "backflow".
- **No hits:** the census registry and `tools/`.
- **Code a rename would touch:**
  - `papers/oi_lattice_code/architecture_check.py`:662, 683, 703/706, 948, 1057 (banned-phrase families);
  - `foundations/review3_probes.py`:9 and `run_all_probes.sh`:9;
  - `verification/lean/c3_necessity_probe.py` (CMI) and `partition_coupling_probe.py` (BLP);
  - the docstring in `OIBridge/C3Necessity.lean`:30, :114 (CMI);
  - `verification/README.md`:2087, :2091.

## Renaming schemes (lines to change, FULL mirrors counted separately)
The 89 conflated lines must be rewritten under either scheme: papers 11, chapters 39, FULL 39.

- **(A) "Backflow" reserved for BLP; CMI uses renamed.**
  - Adds the CMI lines: papers 25, chapters 10, FULL 9. That makes **133 lines**, or **161** if the 31 ambiguous lines
    are edited as well.
  - The lemma's title changes, with 11 name-citation lines. The LEDGER id stays, because claim ids are identifiers
    (§A.30); its label and fingerprint are re-affirmed.
- **(B) "Backflow" kept for CMI with an explicit definition; BLP uses renamed "distinguishability revival".**
  - Adds the BLP lines: papers 12, chapters 11, FULL 11, plus the glossary:91 definition and its mirror. That makes
    **125 lines**, or about **151** with the ambiguous lines.
  - Guard E10 pins Main:332 verbatim and needs an amendment.
  - Literature citations keep "BLP information backflow" as an attributed name: Main:149, Explainer:143, ch01:103,
    appendix-b:96 and ch18:78.

Under either scheme, most of the work is the conflated lines, and most of those belong to the 𝒩-regime family.
Rewriting its four anchor sentences settles about 43 occurrences.
