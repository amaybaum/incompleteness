# Introduction r18: changes against r17 (`papers/Introduction.md` at `a79add6a`)

r18 is one small commit. It applies the two focused re-reviews of r17 at `a79add6a`, both ACCEPT WITH CHANGES: the
scientific recheck (findings sci 1–7) and the editorial and citations recheck (M1–M5, S1–S9, O1–O4). Each change was
checked against its source at the corpus commit `55e3217b`. The cited items of Main, GR and SM are unchanged at `main`
`4449b0d9`. Line numbers are r18's.

## Required

1. **Abstract, L17** (sci 1 = M2). The text now reads "OI places the zero-point sum and the effective cosmological constant at
   different levels of description, and separates conservation of black-hole information from its accessible
   recovery;". r17's "separates the zero-point sum from the gravitational source" read as decoupling, which GR :356
   names as open (G3).
2. **§2.4, L98** (sci 2 = M3). "observed conditional memory $M_k>0$ at an accessible order $k$ forces … at least
   $\varepsilon_{\min}(M_k,|\mathcal C_V|)>0$ from $\pi_H$". Main §3.4, Theorem (physical memory: C2, process form) bounds the
   one-step conditional memory $I(X_{<k};X_{k+1}\mid X_k)=M_k$; Main's contrapositive writes $I^*$ for it. The paper's
   $I^*$ is the past–future maximum, which can exceed $M_k$ (Main :610: $M_1=0$ with a 1-bit past–future term). The
   coupling-step scope and the absence of a mixing hypothesis are unchanged.
3. **§2.5, L114** (sci 3 = M4). The coordinator's text, which is the scientific reviewer's: "Recurrence-cycle indivisibility thus needs only finite
   reversibility and one non-deterministic visible step, and holds also for laws that are Markov on every accessible
   window, so it does not separate them from memory-bearing laws at accessible orders; …". Source: Main §2.3 Scope.
   Under full support, a law with no memory below L gives a divisible family.
4. **§5, L218, H-decouple** (sci 4; also covers S4). "…which is not established: the effective-pure-state theorem [GR, Thm A.7] gives a pure joint
   state of V and B only for times short compared with the D-sector timescale τ_B^D∼1/H, the Hubble time [GR App. A.5],
   far shorter than the evaporation [BHa], and does not establish that V∖R is unentangled with B∪R [GR App. A.7]".
   Source: GR App. A.7, "Theorem A.7 does not establish this … H-decouple is not established here".
5. **§2.5 Corollary, L110** (M5). "Two distinct positive-probability visible histories of equal length with a common
   endpoint". Main §2.3, Theorem (history readback + finite recurrence implies indivisibility) has
   $(x_0,\dots,x_k)\neq(x'_0,\dots,x'_k)$ with $x_k=x'_k$. The memory-witness definition is already equal-length.
6. **[SM], L273** (M1). `[SM] A. Maybaum, "The Standard Model from a Cubic Lattice," papers/SM.md.` It sits in the Corpus list, which is
   pinned at `55e3217b`. The title is SM.md's own title line, and the same title is cited in Main.

## Should-fix

- **S1**
  - "Accessible" is defined at first use, in the (C4) clause (L98): "an order short compared with the recurrence time, as accessible windows are [Main §2.3, Scope]".
  - π_H is glossed as "the model's reference hidden law, toward which a mixing hypothesis would have the hidden state relax between couplings". Main: "the model's reference prior π_H"; the mixing hypothesis reads ε as "the residue of relaxation toward π_H".
  - The (C2) sentence is split in two.
- **S2: Bell–lattice clause** (L186). The dangling clause is gone, and "causal cone" is used throughout. The preparation-indexed coupling graph is defined as "in which a Bell preparation adds bounded-degree long-range edges to the coupling graph". Main §3.3 has "preparation-indexed adjacency … a Bell preparation supplies bounded-degree long edges"; H-Bell is as in Main.
- **S3 / sci 6: observer access** (L214, L216).
  - Access is scoped to the 1,376 count: "for the first count below, it reads the radiation registers as they are emitted".
  - The 32-map count is described as "with a two-bit message occupying both registers and one register read" (BH-01 `checks.py`, AM2).
- **S5: de Sitter identity.** Moved to §4's opening (L190), with "and a Hubble-scale density" and the locator [GR §6.3] (GR :366).
- **S6.** The §3.1 notions paragraph is split into three.
- **S7: abstract recurrence sentence.**
  - The reviewer's wording is not adopted: it drops the explicit "including roots of visible probability zero".
  - "Root" is defined in place instead: "with a row for every initial visible state (root) including roots of visible probability zero".
  - Every scope element of L110/L222 is kept.
- **S8** (L64). "whether such records remain consistent when measurements are omitted [SGD19; Milz20] does not arise for Q_K, which measures at every step."
- **sci 5** (§6, L222).
  - The "Machine-checked" list now names Theorem 3 in its rooted form only.
  - The recurrence-cycle result is listed under "Proved on paper, with Theorem 3 as machine-checked core and the shared-column fact and Γ_L=I as elementary steps".
- **sci 7** (L102, L104). "drawn independently of it" is added to the Γ_t definition and to Theorem 3. The scope wording is now literally identical at L17, L102/L104, L110 and L222.
- **O3.** The references hang-indent by 1.5em inside the existing raw group; the render is clean.
- **S9, font size.** `fontsize: 11pt` is set in the paper's metadata block, next to `geometry: margin=1in`. No other paper and no build file is changed.

## Not applied

| Item | Reason |
|---|---|
| S7, reviewer's wording | drops the explicit zero-probability rows; root defined in place instead |
| O2, Corollary label style "**Corollary** (… [Main §2.3])" | moving the label out of the bold head changes the census slug, and so the coverage ID `INTRODUCTION:C-recurrence-cycle-indivisibility`; IDs are not changed |
| O1, shorten §6's scope copy | the owner requires the scope to be identical at the abstract, §2.5 and §6 |
| O4, drop the stochastic trajectory-law clause | restored in r17 as content cut only for length; it states `realData_traj_stochastic`, listed in Appendix A |

## Layout and rendering

- **11 pt with one-inch margins: 15 pages.** The main text (§§1–6) is about 11.5 pages and ends on p. 12, line 23 of 49. The code note and Appendix A are on p. 12, and the references on pp. 13–15; p. 15 holds a few lines. The page count is 15 rather than the reviewer's measured 14 because r18 adds text (items 2–6, S1–S6).
  - Median line length is about 96 characters (r17 at 10 pt: about 111).
  - Median 3,056 non-space characters per page.
- **Boxes.**
  - 0 overfull boxes and 0 missing characters.
  - At 11 pt the code note's path and 40-character hash first overflowed, by 3pt and then by 30pt. The note is now set in a raw `\begingroup\sloppy … \endgroup` (the same idiom as the existing groups), and the full hash moved to its own sentence.
  - What remains is 7 underfull (loose) lines, all in that one paragraph of code-font paths; they are readable.
- **Renders at 75 dpi:**
  - p. 1, title and abstract;
  - p. 6, the Γ matrices and the card table;
  - p. 10, both field-equation displays;
  - p. 12, the code note, Appendix A's `\small` group and the open problems;
  - p. 14, the references in `\footnotesize`, with the hanging indent.

  All displays are within the margins and the references wrap and separate cleanly.

## Coverage

- No ID changes. L94, the §2.4 Corollary, is byte-identical (`INTRODUCTION:C-unnamed-b596be8a`, b596be8af06bd797).
- **Fingerprints re-affirmed, for statements the required changes touched:**
  - `INTRODUCTION:T-3`: c4966493d9cb60a2 → 67e2d2a4f01999ed (sci 7, "drawn independently of it");
  - `INTRODUCTION:C-recurrence-cycle-indivisibility`: d33c081326f983a5 → 603c7f6d12b01679 (M5, "of equal length").

  Both remain MIRROR rows of Main §2.3.
- **`line` fields:** T-1 53, T-2 79, C-unnamed-b596be8a 94, T-3 104, C-recurrence-cycle-indivisibility 110, T-4 166.

## Checks

- The release gate passes every step except `lean-axioms`, which needs `lake`. That step cannot run here and passes in CI.
- `voice`, `claims`, `duplicate`, `coverage` (134 canonical statements), `staleness` and `mirror` all pass.
- `verification/lean/edge_rigidity_probe.py`: ALL CHECKS PASS.
- Appendix A: all 29 declarations resolve at their stated lines at `17b830bc` and at the head; no name is unlisted or missing.
- Added-lines scans (the §A.32/§A.33 phrase families, caps emphasis, markers, secrets): no hits.
