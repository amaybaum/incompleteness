import re,sys
src=open(sys.argv[1]).read()
def sub(old,new,count=1):
    global src
    if old not in src: sys.exit("MISSING: "+old[:80])
    src=src.replace(old,new,count)
def cut_between(start,end_excl):
    global src
    i=src.index(start); j=src.index(end_excl,i)
    src=src[:i]+src[j:]
# 1 strip HTML comments
src=re.sub(r'<!--.*?-->\n?','',src,flags=re.S)
# 2 kernel identifiers in body (keep Thm1/Thm4 witnesses)
sub(" (`invariance_does_not_select`, `CanonicalMeasure.lean:242`)","")
sub(" (`permMatrix_mem_unitaryGroup`, `EquivalenceChain.lean:179`)","")
sub(" (`isDiag_Phi`, `:253`)","")
sub("Kernel: `pushforward_identity`, `distinguishability_floor`, `capacity_floor` and `unavoidable_hidden_predictive_memory` (`HiddenMemory.lean:83, 114, 170, 185`). These are proved","Parts (a)–(c) are machine-checked (Appendix A)")
sub(" (`c3_necessity`, `card_hidden_ge_two_pow_Istar`, `C3Necessity.lean:80, 117`)","")
sub(" The rooted form is proved in the kernel as `pIndivisible_of_rooted_identity_return_of_overlap` (`RecurrenceHorizon.lean:148`).","")
sub(" (`isPermMatrix_of_stochastic_inverse`, `EquivalenceChain.lean:110`; [BB, Problem 23])"," [BB, Problem 23]")
sub("The kernel proves the conclusion from a routed-readback witness (`routed_forces_indivisible_somewhere`, `PhysicalC4Discharge.lean:122`). Step 1, from history-level (C4) to a non-permutation rooted map, is proved in prose.","Steps 2–3 are machine-checked; step 1 is proved on paper.")
cut_between("  - `krausSoundExt_of_validity_inert`","The theorem is carrier-general.")
sub("through three lemmas:\n","assembled in `exactAll_iff_physical_general` (`GeneralCarrier.lean:100`).\n")
sub(" (`five_way_minimality`, `RankGapTheory.lean:702`)","")
sub(" (`oi_alone_not_qm`, `GeneralCarrier.lean:160`)","")
sub(" (`gl2_strong_gauge_moves_relative_candidate`, `CoherentLiftGauge.lean:537`)","")
sub(" (`gl3_constant_gauge_preserves_relative`, `:451`)","")
sub(" (`bridge_traj`, `rooted_eq_iff_slice_eq`, `realData_traj_stochastic`, `TrackBQfbBridge.lean:276, 180, 286`)","")
# 3 attribution list -> compact
cut_between("*Attribution.*","### 2.3")
src=src.replace("### 2.3","The trajectory-labelling realization is that of Egri et al. [EG, Prop. 13]; its independent-prior form is their Prop. 16 [EG], and its Markov case the random-mapping representation [LPW, Prop. 1.5]. That a permutation dynamics is a special unistochastic process is stated by Barandes [B25; B26 §4]. We are not aware of a packaged statement of the three-way multi-time identification.\n\n### 2.3",1)
sub(" The form \"a law is non-Markovian if and only if a finite reversible realization exists\" is false, since the realization of Theorem 1 exists for Markov laws as well [Main §3.4, Remark on diagnostics].","")
# 4 per-horizon paragraph
cut_between("The per-horizon characterization of [Main §3.4] reads","***\n\n## 3.")
# conditions list compress
cut_between("**Conditions as diagnostics.**","***\n\n## 3.")
src=src.replace("***\n\n## 3.","**Conditions as diagnostics.** Main's four conditions on a hidden sector [Main §1.3] are diagnostics of a realization, not hypotheses of Theorem 1. The one used below is (C4), history readback: two histories with the same present induce different next-step laws. In a faithful realization (C4) coincides with $M_t>0$.\n\n***\n\n## 3.",1)
# 3.2 last para
cut_between("The physical reading of these results is a representation result","***\n\n## 4.")
# 4.3 last para compress
cut_between("On configuration (card) inputs the game","***\n\n## 5.")
src=src.replace("***\n\n## 5.","On card inputs the game is a classical stochastic process, and its P-indivisibility is the population notion (2) of §3.2. Under the permutation-unitary embedding of §2.2 the one-step channel is entanglement-breaking and the two-step map is the identity, so the family is also CP-indivisible [Main §3.2]. A card arrangement violates no Bell inequality [Main §3.3].\n\n***\n\n## 5.",1)
# 5.1 bullets trimmed
cut_between("- **Status of the conditions.**","<!--") if "<!--" in src else None
cut_between("- **Status of the conditions.**","**Decoupling")
cut_between("**Decoupling","### 5.2")
sub(" and passed an independent internal review","")
# 5.3 compress list
sub("- **Robustness.** A constant multiplicative greybody or species factor cancels.\n","")
# 6.3 last para
cut_between("Main also states finite-accuracy realization","### 6.4")
# 6.4 items 4 compress
cut_between("4. **Formalization of four steps:**","5. **Minimal")
src=src.replace("5. **Minimal","4. **Formalization** of the steps marked as proved on paper in Appendix A.\n5. **Minimal",1)
# 6.5 and 7 delete
cut_between("### 6.5 What is not claimed","## 8. Conclusion")
# App A drop 'none' rows
src=re.sub(r"\n\| Readback bound.*?\|\n?","\n",src)
src=re.sub(r"\n\| CP-indivisibility, framework.*?\|\n?","\n",src)
# 1.1 duplicate sentence
sub(" The physical identification of nature with such a system is a representation choice, motivated empirically.","")
open(sys.argv[2],'w').write(src)
