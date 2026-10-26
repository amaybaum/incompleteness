# Corrections to the applications audit

The independent review of the r5 design (`../review/r5/REVIEW.md`) found four errors in `AUDIT.md`. `AUDIT.md` is
kept as reviewed; the corrected readings are:

- **§6.2, look-elsewhere count (review R17).** 1/(π√2) and √2/(2π) are the same value, counted twice. Within 1σ
  there are 5 distinct values of the 752 simple forms, not 6. Among forms as simple as 1/(π√2), the chance of a 1σ
  hit for a random target is about 3.5%, before any trials factor. The reading stands: a postdiction with selection.
- **§0 Cabibbo row and §9 "Classification" (review R18).** "Emergent dressing pending" is at SM:849, not SM:851.
- **§9 (review R18).** preface:7 ("The Bekenstein-Hawking factor of 1/4 in black-hole entropy becomes a derivation")
  and ch00:21 ("derivation rather than a postulate") are separate sites with separate wording.
- **§7.1, JUNO (review R11).** "Undetermined" is settled by git dating. The value was compared with data in
  `054eb99a` (2026-04-04). The 4/3 ratio first appears in `77ac23ce` (2026-04-30) and is equivalent to a sum rule
  the value already satisfied (Juno:237). The precision test is therefore a forward test of a postdicted value.
