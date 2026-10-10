# A41 measurement slots (template vocabulary)

Templates use `{slot}` for a measured value and `[[text if true | text if false : flag]]` for a measured
boolean. Numbers are rendered by one frozen function: words below one hundred ("twenty", "forty-three"),
digits from one hundred ("976", "3896"). Sets are rendered as `{1}`, `{1, −1}`. Values measured at D41 are
given for orientation only; they are not pass conditions.

| slot | meaning | value at D41 |
| --- | --- | --- |
| `sig.partitions` | admitted partition structures at SIG, both orientations, strict | 20 |
| `sig.per_form` | per orientation | 10 |
| `sig.p44` / `sig.p82` / `sig.p28` | per orientation by shape | 5 / 2 / 3 |
| `sig.alignments` | valid alignments at SIG, both orientations | 976 |
| `sig.classes_full` | factorization classes, full stabilizer | 70 |
| `sig.classes_tfree` | factorization classes, transpose-free subgroup | 140 |
| `sig.porbits_full` | partition orbits, full stabilizer | 10 |
| `sig.porbits_tfree` | partition orbits, transpose-free subgroup | 20 |
| `sig.strict_eq_relaxed` | flag: strict and relaxed censuses at SIG equal | true |
| `sig.sorted_partitions` / `sig.sorted_porbits` | the sorted-alignment values (act 37's) | 18 / 9 |
| `hull.params` | 4×4 hull parametrizations, all alignments | 31168 |
| `hull.sorted_params` | at the sorted alignments | 492 |
| `hull.distinct_mat` | distinct hulls as matrix families | 3896 |
| `hull.distinct_gauge` | distinct hulls modulo the gauge | 3896 |
| `hull.bijection` | flag: the map matrix-family hull → hull modulo gauge is a bijection | (measured) |
| `hull.dims` | tangent dimensions modulo gauge, as a set | {14} |
| `hull.dF_ok` | flag: every generator in ker DF and D²F vanishing on every generator pair, every distinct hull | true |
| `hull.span` | rank of combined tangent span modulo gauge | 49 |
| `hull.W_in` | distinct hulls whose tangent contains W | 0 |
| `p.partitions` | admitted partition structures at P and at Pu(u5), each | 2 |
| `p.p44` / `p.p82` / `p.p28` | per orientation | 0 / 0 / 1 |
| `p.alignments` | valid alignments of the 2×8 at P, per orientation | 128 |
| `p.no_44_82` | flag: at `P` and at `Pu(u5)`, no 4×4 and no 8×2 partition structure under any alignment, strictly and relaxed | true |
| `w.exclusive` | flag: strictly, only the frozen 2×8 partition per orientation away from u = 1 | true |
| `w.exc_strict` / `w.exc_relaxed` | exceptional sets of act 37's arc | {1} / {1, −1} |
| `w.at1` / `w.m1_strict` / `w.m1_relaxed` | partition structures at u = 1, at u = −1 strict, relaxed | 20 / 2 / 20 |
| `e.exc_strict` / `e.exc_relaxed` | exceptional sets of act 38's arc | {1, −1} / {1, −1} |
| `e.m1` | partition structures at u = −1 | 4 |
| `e.exc_is_pm1` | flag: act 38's exceptional set is {1, −1}, strictly and relaxed | true |
| `e.m1_k4_exchanged` | flag: the 4×4 ones are k4 moved by rows 7↔15 and columns 2↔8 | true |
| `e.sig_only_at_1` | flag: every SIG partition structure admitted along act 38's arc only at u = 1 | true |
| `h3.candidates` | partition candidates of H3 | 46 |
| `h3.nonempty` | nonempty loci (union over alignments), strict | 43 |
| `h3.strict_eq_relaxed` | flag: strict locus = relaxed locus for every candidate | true |
| `h3.flats` / `h3.noncoord` | distinct flats / those not cut out by coordinate characters | 21 / 4 |
| `h3.five_faces` | flag: maximal flats are exactly act 40's five faces | true |
| `h3.maximal` | the maximal flats, as rendered strings (rendered comma-separated) | the five faces: `u1 = −1`, `u1 = 1`, `u2 = 1`, `u3 = −1`, `u3 = 1` |
| `h3.at_one` / `h3.at_mone` | partition structures at (1,1,1) / (−1,−1,−1) | 20 / 4 |
| `h3.sorted_nonempty` | the sorted-alignment value (act 40's) | 30 |
