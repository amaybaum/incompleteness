# A5. Lemmas used by the base

**Governs:** base line 95 (the heading's parenthetical), the support of the statements at base lines 97–114, base
line 163 (its last sentence) and base lines 244–245 (the clause "The P1 lemma and the blindness lemma (CC-SCOPE)").

**Support.** The blindness lemma (lines 97–100), L-O(i) (lines 102–106) and L-O(ii) (lines 102–103, 107–110) are proved
as stated in `verification/programmes/oi-qm/reconstruction/k1-rdy-proofs-20261105/LEMMAS.md` §2–§4, on `main` at
`4f016afd`. "The P1 lemma" (line 244) is Lemma P1 of that file, §1.1, whose parts (a)–(c) carry the uses at lines 72–76
and 244. Line 95's parenthetical is provenance. The independent review of those proofs is recorded at
‹to be filled before F: the record on `main` of PR #1119 comment 6651717259 and its delta check›.

**Line 163.** Its last sentence states G4's outcome for a B-pl member row. It applies subject to the precedence of
lines 136–138 and 182–183: a Z1-VOID or VOID[row] issued for that row takes precedence over the BLIND it states. For a
sharply ready member, `NB` fails by the blindness lemma (`LEMMAS.md` §2.3).

**CC-SCOPE** (lines 208, 244–245). In B-pl the blindness lemma applies to `δ_0`; in B-eq and B-ct it applies to
`δ_0(· | W_{t_u} = 0) = δ_0`, the only positive-mass conditioning (`LEMMAS.md` §2.3).
