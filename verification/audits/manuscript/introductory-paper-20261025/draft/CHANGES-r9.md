# Introduction r9: changes from r8

The scientific confirmation of r8 (`review/scientific/RECHECK-r8.md`) returned ACCEPT WITH NITS. r9 applies its three
nits; every other byte equals r8.

- **N1 (precision), §5.** "equals the Page value $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$" becomes
  "… for factor dimensions $d_B,d_R$, up to the correction term of Theorem A.8". The reviewer suggested
  "up to $\mathcal O(\epsilon)$"; the symbol $\epsilon$ is not defined in this paper and elsewhere names the
  discreteness scale, so the correction is named by its theorem instead.
- **N2, §5.** "timescale ordering does not supply it" gains "[BHa, item F]". This gives §6.2 item 4's decoupling
  non-claims their referent back.
- **N3, bibliography.** The VERIFY comments on BBS24, Cal26, EvEMU11, KP14, tH14 and Vol06 are replaced by
  "Read first-hand: <source location> (draft/review/references/FINDINGS.md, sha256 fa50caae…6ea1): SUPPORTED."
  CT06, Har04 and Sha79 keep their VERIFY markers, since they are unreachable. The Weinberg OWNER gate is unchanged.

Build: 17 pages; the main text ends on p. 12, about 11.8 pages. No overfull boxes and no dropped glyphs.
