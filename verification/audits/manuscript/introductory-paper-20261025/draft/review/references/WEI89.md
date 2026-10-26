# First-hand check of Weinberg 1989 (landing gate)

**Object.** `Introduction-r13.md`, sha256 `00f84951409e2dbbf212a90cb49be02608d9e51af4affaf02cd7a31632c27a99`, line 141,
the sentence behind the Weinberg VERIFY marker (line 140).

**Gate.** Owner, 2026-10-26: the paper does not land until Weinberg 1989 is read first-hand and checked. On the same
day the owner supplied a third-party hosted copy and asked that the reviewer "verify the title, publication details,
completeness, and relevant passages against the original", respecting its reuse permissions.

**Copy read.** A scan hosted at isidore.co, 23 pages, sha256
`307cf3fc7b1e1eeba74c3db97b675843a4d86e2c909d87f2870d59404b245d3f`. It is a third-party copy of an APS article
(p. 1 footer: "Copyright ©1988 The American Physical Society"). It was read for verification only. The PDF, its page
images and any extracted text are not committed and not redistributed. This record quotes single sentences and
equations only. The paper cites the publisher's version, never the hosted copy.

**Reader.** The Introduction's final scientific referee, who read the page images. Written by the coordinator from the
referee's report, because the referee's tool refused report files.

## Identity and completeness

S. Weinberg, "The cosmological constant problem", *Rev. Mod. Phys.* **61**, No. 1, pp. 1–23 (January 1989). It is
not the 2000 review "The Cosmological Constant Problems" (astro-ph/0005265).

- **Title page.** Title, author and affiliation (Theory Group, Department of Physics, University of Texas, Austin);
  the abstract; a contents list with sections I–IX on pp. 1–20, Acknowledgments and References on p. 21; footnote
  "Morris Loeb Lectures in Physics, Harvard University, May 2, 3, 5, and 10, 1988."
- **Journal footers.** "Reviews of Modern Physics, Vol. 61, No. 1, January 1989" on p. 1, "Rev. Mod. Phys., Vol. 61,
  No. 1, January 1989" on pp. 2–23.
- **Numbering.** Running head on pp. 2–23; pages 1–23 with no gap or repeat; section starts as listed; references on
  pp. 21–23, ending with Zumino (1975).
- **Scan.** One 1-bit image per page at about 612 dpi, no text layer. All 23 pages are full, upright and legible.
  Equation numbers run continuously where read, (2.1)–(2.11) and (3.1)–(3.9). No sign of alteration or truncation.

## Relevant passages

| Passage | Where |
|---|---|
| "theoretical expectations for the cosmological constant exceed observational limits by some 120 orders of magnitude." | §I, p. 1 |
| The comparison point is an observational upper bound, $\lvert\rho_V\rvert\lesssim10^{-29}\,\mathrm{g/cm^3}\approx10^{-47}\,\mathrm{GeV^4}$. | §III, p. 2, Eq. (3.4) |
| Summing the zero-point energies of all normal modes of a field of mass $m$ up to a wave-number cutoff $\Lambda\gg m$ gives $\langle\rho\rangle\simeq\Lambda^4/16\pi^2$ ($\hbar=c=1$). | §III, p. 2, Eq. (3.5) |
| With $\Lambda\simeq(8\pi G)^{-1/2}$: $\langle\rho\rangle\approx2^{-10}\pi^{-4}G^{-2}=2\times10^{71}\,\mathrm{GeV^4}$, so "the two terms here must cancel to better than 118 decimal places." | §III, p. 3, Eq. (3.6) |
| QCD zero-point energies, $\Lambda_{\rm QCD}^4/16\pi^2\approx10^{-6}\,\mathrm{GeV^4}$: cancellation "to about 41 decimal places". | §III, p. 3 |
| Electroweak Higgs-potential minimum (not a zero-point sum): $\lvert\langle\rho\rangle\rvert\simeq10^6\,\mathrm{GeV^4}$ for $g\sim\alpha^2$, "larger than the bound on $\rho_V$ by a factor $10^{53}$." | §III, p. 3, Eqs. (3.8)–(3.9) |

Arithmetic check: $(8\pi G)^{-1/2}=2.44\times10^{18}\,\mathrm{GeV}$ and $\Lambda^4/16\pi^2=2.2\times10^{71}\,\mathrm{GeV^4}$;
against $10^{-47}\,\mathrm{GeV^4}$ that is $10^{118.3}$.

## Verdict

**SUPPORTED in substance**, by §I and §III, Eqs. (3.4)–(3.6): a zero-point sum with a Planck-scale cutoff, an excess
of some 120 orders of magnitude (118 for Weinberg's convention), and cancellation to that accuracy. There are two
qualifications.

1. Weinberg compares against an observational upper bound, not a measured value. The present measured density,
   about $2.5\times10^{-47}\,\mathrm{GeV^4}$, is of the order of that bound, so the magnitude carries over. The
   sentence therefore says "observational value", which covers both the bound and the measurement.
2. "The exact power depending on the cutoff convention" is not in Weinberg. It is elementary: his convention gives
   $10^{118}$, and $G^{-2}$ against the same density gives about $10^{123}$. The clause stays the paper's own and is
   not attributed to [Wei89].

**Citation applied (r14).** The referee's Option A: "[Wei89, §I; §III, Eqs. (3.4)–(3.6)]" after "observational
value", and "[Wei89, §III]" after the cancellation clause. The convention clause is uncited. The VERIFY marker is
removed. Bibliography: [Wei89] S. Weinberg, "The cosmological constant problem," *Rev. Mod. Phys.* **61**, 1 (1989).
