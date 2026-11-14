# G3 unit 1, forward correction (r1): Part 2 and requirement (ii) on the evidence of unit 2(a)

**Scope.** This is a paper-only correction record under Issue #873, for PR #1275.

- Authorization: #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU4: "unit 1 is corrected
  forward with a short note or r6 that points to unit 2(a). The record r5 itself is not edited."
- Requirement: PR #1275 review 5898121925 (posted by `amaybaum`, 2026-11-13T21:12:40Z, at
  `1ad01923efda24323217f3a5d9dd30a5c506fd3c`), "Bounded implications": "Unit 1's `(ii-L) as GR:346
  argued` cannot be left as an unconditional source for (DZ): on E/D it is added, on G its exclusion
  needs B_G, and as an added determination restriction it is silent for Z_0 and depends on the §8.3
  branch for the configuration-varying term. GR:400 Reading 1 and the configuration-differential source
  are not banned without the extra conditions. Nor has the corpus selected an offset convention or
  established coupling across general metrics."
- Corrected records: `G3-UNIT1-r5.md` and `NOTES-r5.md` (unchanged since
  `e81e4fb23f4a5abda910cc69e9f79f93e6ae1523`), and the optional note of `CONFIRM-r4.md` D-2.
- Supporting record: `G3-UNIT2A-r3.md`, outcome (C), with `REVIEW-U2A-r1.md` and `CONFIRM-U2A-r2.md`
  (CONFIRMED). All are on branch `research/g3-offset-873-20261113` at
  `1ad01923efda24323217f3a5d9dd30a5c506fd3c`, and they land with this record.

This record derives nothing new. Each corrected statement is scoped exactly as unit 2(a) r3 establishes
it. It adopts no premise, changes no manuscript, runs no computation and makes no claim about the
magnitude of Λ. r5, NOTES-r5 and CONFIRM-r4 are not edited; where a statement below differs from them,
this record states the current position.

**Line references.** "U1r5:n" is `G3-UNIT1-r5.md` line n. "NOTES-r5:n" is `NOTES-r5.md` line n.
"CONFIRM-r4:n" is `CONFIRM-r4.md` line n. "U2Ar3:n" is `G3-UNIT2A-r3.md` line n. Corpus lines refer to
`main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`, as in both units.

**Terms from unit 2(a) r3.** Readings E (order of explanation), D (order of determination) and G (order
of existence or emergence) of GR:346 are defined at U2Ar3:206–231 and assessed at U2Ar3:264–287. (ii-G)
is defined at U2Ar3:260. The bridge premise **B_G** is: a term of the boundary metric's law that is a
function of the emergent class grounds the realized metric, and does not only co-constrain it
(U2Ar3:285–287). Z_0 is GR:362's density estimate as written; Z_I and Z_II are constructed conventions
with a configuration-varying `ρ_Z` (U2Ar3:315–331). The split `ρ_Z = ρ_Z(R₀) + Δρ_Z` into an absolute
part and a configuration-differential part is at U2Ar3:459–463.

**Scope of every corrected statement.** The exact de Sitter class of unit 2(a) §3 and assumption M1
(`n` and `ε` independent of `R`) (U2Ar3:76–78, :670). Support labels are those of both units: [A] exact
algebra or elementary logic, [P] a paper derivation or a reading of a paper argument.

***

## 1. The two-part verdict

| Part | Category | Statement | Support |
|---|---|---|---|
| 1 | Counterexample, for source maps | As U1r5:43–47. Unaffected. | U2Ar3:726 |
| 2 | Conditional on Reading G of GR:346 and B_G (open), for the coupling with physical content | K_cpl^conv violates (DZ) [A]. On Readings E and D, GR:346's argument does not establish (ii-L) and does not exclude a self-consistent fixed point of K_cpl^conv; (ii-L) is then an added premise. On Reading G it excludes the convention-fixed coupling if and only if B_G holds. As an added premise, (ii-L) excludes a K_cpl^conv member only when `ρ_Z` varies with the configuration through the partition and §8.3 is not in force; it is silent under Z_0. | U2Ar3:39–59, :82–90, :495–515, :672–689 |

The category "conditional on (ii-L)" is accurate for Part 2 only in the branch named in the last
sentence of row 2. GR:346 supplies an exclusion of K_cpl^conv only on Reading G, given B_G, and that exclusion is
(ii-G), which is stronger than (ii-L) (U2Ar3:82–85, :678–681).

***

## 2. Corrected statements

### X-1. §0, Part 2: category and conclusion

- **r5.** U1r5:48–49: "**Conditional on (ii-L), for the coupling with physical content.** K_cpl^conv,
  the coupled completion with physical content, violates (DZ) [A]." U1r5:55–57: "(DZ) for the
  convention-fixed offset therefore follows conditional on GR:346's argument (ii-L) [P]. Whether that
  argument holds against self-consistent fixed points is not established: it is a requirement on the
  order of derivation, not a proof that no fixed point exists."
- **Corrected.** "**Conditional on Reading G of GR:346 and the bridge premise B_G (open), for the
  coupling with physical content.** K_cpl^conv, the coupled completion with physical content, violates
  (DZ) [A].
  - On Readings E and D, GR:346's argument does not establish (ii-L), and it does not exclude the
    self-consistent fixed point of K_cpl^conv[Z_I] or K_cpl^conv[Z_II]. On those readings (ii-L) is an
    added premise, and (DZ) for the convention-fixed offset receives no support from GR:346 [A], [P].
  - On Reading G the argument is valid. It excludes the convention-fixed coupling if and only if B_G
    holds, whether or not §8.3 is in force [P].
  - B_G is open. It fails, conditionally, if the boundary law is a coarse-grained consequence of `φ` in
    which the realized metric is grounded in `(S, φ)` directly, and if a derived law's terms do not
    ground its solutions. The first condition is G3 (open); the corpus states no view on the second [P].
  - As an added premise, (ii-L) yields (DZ) for the convention-fixed offset only when `ρ_Z` varies with
    the configuration through the partition and §8.3 is not in force. It is silent under Z_0 [A], [P]."
- **Support.** U2Ar3:39–59, :82–85, :264–287, :495–515, :548–552, :672–681, :684–689; U2A-F1 and
  U2A-F6 (U2Ar3:741, :746).

### X-2. §0, Part 2: what excludes K_cpl^conv

- **r5.** U1r5:50: "It is excluded by (ii-S) and by GR:346 as argued (ii-L)."
- **Corrected.** "It is excluded by (ii-S) in either §8.3 branch, and by the posits P11 and GR:575.
  GR:346's argument excludes it on Reading G given B_G (open), in either §8.3 branch; with §8.3 in
  force that exclusion reaches the absolute part and admits the configuration-differential part.
  GR:346's argument does not exclude it on Readings E and D. (ii-L), as an added premise, excludes a
  K_cpl^conv member only when `ρ_Z` varies with the configuration through the partition and §8.3 is not
  in force."
- **Support.** U2Ar3:76–78, :94–98, :465–477, :678–679, :685–686.

### X-3. §0, Part 2: the corpus's use, and the reading under which K_cpl^conv survives

- **r5.** U1r5:51–54: "It is not admitted by the corpus's use. That use feeds back only a piece that
  GR:400 classes as relative in the sense of §8.3 (GR:573), conditional on that identification." and
  "K_cpl^conv is compatible with OI's results only under (ii-W) applied to absolute emergent
  quantities, a reading no corpus text adopts."
- **Corrected.** "Write `ρ_Z = ρ_Z(R₀) + Δρ_Z`.
  - The corpus's use does not admit the absolute part `ρ_Z(R₀)`: GR:400 Reading 1 fixes the constant
    part by the substratum budget, and GR:575 places absolute emergent levels on the non-gravitating
    side, conditional on §8.3's identification (GR:573).
  - The configuration-differential part `Δρ_Z` of a configuration-varying convention is the same kind
    of piece that GR:400 Reading 1 feeds back. With §8.3 in force it is a classical microstate
    difference, and the corpus's use and (ii-L) admit it. Whether such a part gravitates is the
    question GR:579 leaves open.
  - The exclusion of K_cpl^conv therefore rests on (ii-S), P11 or GR:575, each a posit or a reading the
    corpus does not adjudicate, or on GR:346 on Reading G given B_G. It does not rest on GR:346 on
    Readings E and D. On Reading E requirement (ii) is (ii-W), and it admits the fixed point."
- **Support.** U2Ar3:43–45, :76–78, :94–98, :459–477, :489, :682–683, :690–693, :703–714. The
  Reading 1 stipulation on the constant part is r5's own (U1r5:513–515) and is unaffected.

### X-4. §0, assumption-watch AW-loop

- **r5.** U1r5:71–74: "GR:346 and the wording "emergent vacuum energy" at GR:358, GR:374 and GR:400
  are in apparent tension. GR:400's qualifier reconciles them, conditional on §8.3's identification
  (B5). The reconciliation is not stated at GR:346."
- **Corrected.** "Whether GR:346 is in tension with the wording "emergent vacuum energy" at GR:358,
  GR:374 and GR:400 depends on the reading of GR:346. On Reading E, GR:346 is consistent with the
  feedback stated at GR:358 and GR:374 and with the self-consistent calculation of GR:388 and GR:400
  Reading 1 without §8.3. On Readings D and G the tension stands, and GR:400's qualifier reconciles
  them conditional on §8.3's identification (B5); the reconciliation is not stated at GR:346. B_G
  decides between Readings E and G."
- **Support.** U2Ar3:99–100, :715–720; U2A-F4 (U2Ar3:744).

### X-5. B5: the characterization of (ii-L)

- **r5.** U1r5:478–479: "**Loop reading (ii-L), GR:346 as argued.** No self-consistent loop runs
  through post-partition data. (ii-L) is weaker than (ii-S). It excludes K_cpl^conv and not
  K_cpl^free (below)."
- **Corrected.** "**Loop reading (ii-L).** No self-consistent loop runs through post-partition data:
  no cycle of value dependence passes through an object defined through the partition. "Post-partition"
  is a property of a quantity's route of specification, not of its value; without that qualifier
  (ii-L) would forbid the nonlinearity of the Einstein equation. (ii-L) is weaker than (ii-S).
  - Source. On Reading E GR:346's argument is valid and concludes (ii-W). On Reading D it is unsound,
    because its step N5-D is false as a general principle. On neither reading does it supply (ii-L),
    which is then an added premise. On Reading G it is valid and concludes (ii-G), which is stronger
    than (ii-L); its application to K_cpl^conv needs B_G (open).
  - Reach. As an added premise, (ii-L) excludes a K_cpl^conv member only when `ρ_Z` varies with the
    configuration through the partition and §8.3 is not in force. It is silent under Z_0, and with
    §8.3 in force it excludes neither part of K_cpl^conv. It does not exclude K_cpl^free."
- **Support.** U2Ar3:221–231, :253–262, :264–287, :465–472, :685–689, :726; U2A-F5 (U2Ar3:745).

### X-6. B5: where the loop closes

- **r5.** U1r5:484–486: "For K_cpl^free the loop does not close: the metric fixes the origin's
  coordinate. For K_cpl^conv it closes through the gaps and the mode count: partition → transition
  data → `e_Z` → metric → partition. GR:346 as argued ("no entry point") therefore excludes
  K_cpl^conv."
- **Corrected.** "For K_cpl^free the loop does not close: the metric fixes the origin's coordinate. For
  K_cpl^conv it closes through the gaps and the mode count (partition → transition data → `e_Z` →
  metric → partition) when `e_Z` varies with the configuration through the partition: under Z_I and
  Z_II, and for the emergent vacuum energy of GR:378(i), which is the GR:400 Reading 1 case. Under Z_0,
  GR:362's density estimate as written, `ρ_Z` is constant on the de Sitter family, and the loop does not
  close. Where the loop closes, the implicitly specified fixed point has an entry point in the order of
  explanation, so "no entry point" does not exclude it on Reading E. On Reading D that step is false as
  a general principle. On Reading G the exclusion holds given B_G (open)."
- **Support.** U2Ar3:43–53, :333–338, :388–390, :425–448, :648–653, :694–695; U2A-F2 (U2Ar3:742).

### X-7. B5: skepticism toward the readings that favour decoupling

- **r5.** U1r5:517: "(ii-S) would give (SI) directly. (ii-L) would give (DZ) directly." U1r5:520–522:
  "The force of (ii-L) against self-consistent fixed points is not established. GR:346 is a
  requirement on the order of derivation, not a proof that no fixed point exists. This is what keeps
  Part 2 of the verdict conditional rather than derived."
- **Corrected.** "(ii-S) would give (SI) directly. (ii-L) would give (DZ) only when `ρ_Z` varies with
  the configuration through the partition and §8.3 is not in force." And: "On Readings E and D, on the
  de Sitter class, GR:346's argument does not exclude a self-consistent fixed point of K_cpl^conv. The
  witness of unit 2(a) satisfies (i), (iii), (Adm1)–(Adm3) and (ii-W), and for `n > 0` its fixed point
  is unique for every completion constant in an open interval. On Reading G the exclusion turns on B_G,
  which is open. This is what keeps Part 2 of the verdict conditional rather than derived."
- **Support.** U2Ar3:497–515, :685–689; U2A-F1 (U2Ar3:741).

### X-8. B5: K_cpl^conv's absolute offset, and the node verdict

- **r5.** U1r5:507–510: "K_cpl^conv's `e_Z` is the absolute ground eigenvalue (GR:332, GR:358), which
  GR:575 classes as having no classical counterpart. The corpus's use therefore does not admit
  K_cpl^conv. K_cpl^conv survives only under (ii-W) applied to absolute emergent quantities, and no
  corpus text adopts that reading." U1r5:525–527: "K_cpl^conv is excluded by (ii-S) and by (ii-L). It
  is not admitted by the corpus's use, conditional on the §8.3 identification. It survives only under
  (ii-W) applied to absolute emergent quantities."
- **Corrected.** "K_cpl^conv's `e_Z` is the absolute ground eigenvalue (GR:332, GR:358). Its absolute
  part `ρ_Z(R₀)` is classed by GR:575 as having no classical counterpart, and the corpus's use does not
  admit it, conditional on the §8.3 identification. Its configuration-differential part `Δρ_Z` is the
  kind of piece GR:400 Reading 1 feeds back." And, as the node verdict: "K_cpl^conv is excluded by
  (ii-S), and by P11 or GR:575. GR:346's argument excludes it on Reading G given B_G (open), and not on
  Readings E and D. (ii-L), as an added premise, excludes it only when `ρ_Z` varies with the
  configuration through the partition and §8.3 is not in force."
- **Support.** U2Ar3:76–78, :459–477, :682–683, :690–693.

### X-9. §4, dependency row "Ordering requirement (ii)"

- **r5.** U1r5:541, column "Bearing on the offset": "(ii-S) excludes both coupled completions. GR:346
  as argued (ii-L) excludes K_cpl^conv. The corpus's use does not admit it, conditional on §8.3 (B5,
  AW-loop)."
- **Corrected.** "(ii-S) excludes both coupled completions. GR:346's argument excludes K_cpl^conv on
  Reading G given B_G (open), and not on Readings E and D, where (ii-L) is an added premise that
  excludes K_cpl^conv only when `ρ_Z` varies with the configuration through the partition and §8.3 is
  not in force. The corpus's use does not admit K_cpl^conv's absolute part, conditional on §8.3 (B5;
  AW-loop, X-4)."
- **Support.** U2Ar3:465–472, :672–689.

### X-10. §5, verdict Part 2

- **r5.** U1r5:565–568: "**Conditional on (ii-L), for the coupling with physical content.** (DZ) for
  the convention-fixed offset follows conditional on GR:346's argument (ii-L) [P]. The force of (ii-L)
  against self-consistent fixed points is not established. K_cpl^conv is compatible with OI's results
  only under (ii-W) applied to absolute emergent quantities, a reading no corpus text adopts."
- **Corrected.** The statement of X-1, followed by the last bullet of X-3.
- **Support.** As X-1 and X-3.

### X-11. §5, route R0

- **r5.** U1r5:572–581: "**R0. GR:346 as argued (ii-L): no self-consistent loop through post-partition
  data.** It excludes K_cpl^conv, and (DZ) for the convention-fixed offset follows for the uniform term
  [A, conditional on (ii-L)]. It is weaker than (ii-S) and already suffices against K_cpl^conv. …
  Status: the text of GR:346 as argued. The corpus's use (GR:358, GR:374, GR:400 Reading 1) is
  consistent with it, conditional on §8.3's identification (AW-loop). Its force against
  self-consistent fixed points is not established. Holding it as a premise is a decision under §A.29."
- **Corrected.** "**R0. (ii-L): no self-consistent loop through post-partition data.**
  - As an added premise, it excludes a K_cpl^conv member, and (DZ) for the convention-fixed offset
    follows for the uniform term, only when `ρ_Z` varies with the configuration through the partition
    and §8.3 is not in force [A, conditional on (ii-L)]. In that branch it also excludes GR:400
    Reading 1. It is silent under Z_0, and with §8.3 in force it excludes neither part of K_cpl^conv.
  - It is weaker than (ii-S). It does not exclude K_cpl^free, which is world-equivalent to K_dec with
    Λ₀ left undetermined (the union over Λ₀), the corpus's standing for Λ (GR:162, GR:334, GR:356).
  - The stronger (ii-S) corresponds, for the source, to GR:400's Reading 2.
  - Source: GR:346's argument does not supply (ii-L) on Readings E and D. On Reading G it concludes the
    stronger (ii-G), which excludes K_cpl^conv given B_G (open) in either §8.3 branch: with §8.3 in force
    it excludes the absolute part and admits the configuration-differential part, and without §8.3 it
    also excludes GR:400 Reading 1.
  - Status: GR:342's ontological commitment read in the order of existence is a candidate independent
    motivation for (ii-L) and for (ii-G), conditional on B_G. The corpus's use (GR:358, GR:374, GR:400
    Reading 1) is consistent with GR:346 on Reading E without §8.3, and on Readings D and G conditional
    on §8.3's identification (AW-loop, X-4).
  - Holding (ii-L) or (ii-G) as a premise is a decision under §A.29."
- **Support.** U2Ar3:82–85, :94–98, :465–477, :672–689, :715–720, :829–832.

### X-12. §5, obligation O0

- **r5.** U1r5:630–641: "Status: addressed on paper in B5, pending review. … (ii-S) and GR:346 as argued
  (ii-L) both exclude K_cpl^conv. The corpus's use (GR:358, GR:374, GR:400 Reading 1) does not admit
  K_cpl^conv, conditional on §8.3's identification (GR:573). Remaining: Whether (ii-L) holds against
  self-consistent fixed points. This is a proof question, and it is open. Whether to hold (ii-L) as a
  premise. That is an owner decision under §A.29 (Q7). It removes Reading 1 only if the §8.3
  identification fails (Q8). If (ii-L) is held, (DZ) for the convention-fixed offset follows
  conditionally, and O1 becomes secondary for that question."
- **Corrected.**
  - "Status: addressed on paper in B5 and in unit 2(a) r3 (outcome (C)).
    - K_cpl^free: as U1r5:631–632.
    - (ii-S) excludes K_cpl^conv. GR:346's argument excludes it on Reading G given B_G, and on the de
      Sitter class it does not exclude it on Readings E and D.
    - The corpus's use (GR:358, GR:374, GR:400 Reading 1) does not admit K_cpl^conv's absolute part,
      conditional on §8.3's identification (GR:573)."
  - "Remaining:
    - B_G: whether a term of the boundary metric's law that is a function of the emergent class grounds
      the realized metric or only co-constrains it. It is open. It reduces in part to the status of the
      boundary law under G3 (open) and to a view of laws that the corpus does not state.
    - Whether to hold (ii-L), or (ii-G), as a premise. That is an owner decision under §A.29 (Q7). For
      (ii-L) it removes Reading 1 only if the §8.3 identification fails (Q8)."
  - "If (ii-L) is held, (DZ) for the convention-fixed offset follows only when `ρ_Z` varies with the
    configuration through the partition and §8.3 is not in force, and O1 becomes secondary for that
    question in that branch only."
- **Support.** U2Ar3:54–59, :548–552, :685–689, :721–725, :829–832, :845–846.

### X-13. §5, obligation O1

- **r5.** U1r5:651–652: "For a convention-fixed coupling (K_cpl^conv) it is compatible only under (ii-W)
  applied to absolute emergent quantities, a reading no corpus text adopts (B5)."
- **Corrected.** "For a convention-fixed coupling (K_cpl^conv) it is excluded by (ii-S), P11 or GR:575,
  and by GR:346 on Reading G given B_G (open). On the de Sitter class GR:346 does not exclude it on
  Readings E and D, and (ii-L) as an added premise excludes it only when `ρ_Z` varies with the
  configuration through the partition and §8.3 is not in force (B5; X-8)."
- **Support.** U2Ar3:76–78, :682–689; U2A-F1 (U2Ar3:741).

### X-14. §6, finding F1

- **r5.** U1r5:663: "The non-implication at GR:352 holds relative to the data GR:352 lists. With the
  ordering requirements of the same section (GR:342–348) included, it holds in the two-part form of
  §0: for source maps on (ii-W) and (ii-L), and for the coupling with physical content only if (ii-L)
  lacks force against self-consistent fixed points (open). The λ-families are natural and conserved
  and share every listed datum at `r₀` (B5: K_cpl^free on (ii-W) and (ii-L), excluded by (ii-S);
  K_cpl^conv only under (ii-W) applied to absolute emergent quantities)."
- **Corrected.** "The non-implication at GR:352 holds relative to the data GR:352 lists. With the
  ordering requirements of the same section (GR:342–348) included, it holds for source maps on (ii-W)
  and (ii-L). For the coupling with physical content, on the de Sitter class under M1, GR:346 does not
  settle (DZ) on Readings E and D, which is consistent with GR:352; on Reading G it settles (DZ) for the
  convention-fixed offset given B_G (open). The λ-families are natural and conserved and share every
  listed datum at `r₀` (B5: K_cpl^free on (ii-W) and (ii-L), excluded by (ii-S); K_cpl^conv excluded by
  (ii-S), P11 or GR:575, and by GR:346 on Reading G given B_G)." The rest of F1, its class and its
  support are unchanged.
- **Support.** U2Ar3:76–78, :727–731; U2A-F1 and U2A-F6 (U2Ar3:741, :746).

### X-15. CONFIRM-r4 D-2, optional note

- **CONFIRM-r4.** CONFIRM-r4:92: "GR:352 calls decoupling open at G3, while GR:346 as argued, in the
  same section, would settle (DZ) conditionally." r5 does not carry it (RESPONSE-r4:20).
- **Corrected.** "GR:352 calls decoupling open at G3. GR:346, in the same section, settles (DZ) for the
  convention-fixed offset on Reading G given B_G (open), or with (ii-L) added, `ρ_Z` varying with the
  configuration through the partition, and §8.3 not in force. On Readings E and D it does not settle
  (DZ)."
- **Support.** U2Ar3:685–689, :727–731.

### X-16. §6, finding F8

- **r5.** U1r5:670: "(ii-S) and GR:346 as argued (ii-L) exclude K_cpl^conv. The corpus's use does not
  admit it, because GR:400 Reading 1 feeds back only a piece classed as relative in the sense of §8.3
  (GR:573). That reconciliation of GR:346 with GR:358, GR:374 and GR:400 is conditional on §8.3 and is
  not stated." Class: "ELABORATING (assumption-watch AW-loop: the GR:346 / GR:400 reconciliation is
  conditional on §8.3 and unstated)".
- **Corrected.** The first sentence on K_cpl^free is unchanged. Then: "(ii-S) excludes K_cpl^conv.
  GR:346's argument excludes it on Reading G given B_G (open), and not on Readings E and D. (ii-L), as
  an added premise, excludes it only when `ρ_Z` varies with the configuration through the partition and
  §8.3 is not in force. The corpus's use does not admit its absolute part. GR:400 Reading 1 feeds back
  a configuration-differential piece classed as relative in the sense of §8.3 (GR:573), of the same
  kind as K_cpl^conv's `Δρ_Z`. On Readings D and G, the reconciliation of GR:346 with GR:358, GR:374
  and GR:400 is conditional on §8.3 and is not stated; on Reading E none is needed." Class:
  "ELABORATING (assumption-watch AW-loop: on Readings D and G, the GR:346 / GR:400 reconciliation is
  conditional on §8.3 and unstated)".
- **Support.** U2Ar3:465–477, :672–693, :715–720; U2A-F4 (U2Ar3:744).

### X-17. §6, assumption-watch AW-loop

- **r5.** U1r5:689–694: "GR:346 and the wording "emergent vacuum energy" at GR:358, GR:374 and GR:400
  are in apparent tension. GR:400's own qualifier ("relative … in the sense of §8.3") reconciles them,
  conditional on §8.3's identification of relative emergent effects with classical microstate
  differences (GR:573). That identification is part of the geometry-first proposal. The reconciliation
  is not stated at GR:346."
- **Corrected.** "On Reading E, GR:346 is consistent with the wording "emergent vacuum energy" at
  GR:358, GR:374 and GR:400 without §8.3. On Readings D and G they are in apparent tension, and GR:400's
  own qualifier ("relative … in the sense of §8.3") reconciles them, conditional on §8.3's
  identification of relative emergent effects with classical microstate differences (GR:573). That
  identification is part of the geometry-first proposal. The reconciliation is not stated at GR:346.
  B_G decides between Readings E and G." The epoch-differential caveat (U1r5:695) applies where the
  reconciliation is needed, on Readings D and G, and is otherwise unchanged.
- **Support.** U2Ar3:99–100, :715–720; U2A-F4 (U2Ar3:744).

### X-18. NOTES-r5 §4, verdict row 2

- **NOTES-r5.** NOTES-r5:61: "| 2 | Conditional on (ii-L), for the coupling with physical content | (DZ)
  for the convention-fixed offset follows conditional on GR:346's argument (ii-L). The force of (ii-L)
  against self-consistent fixed points is not established. K_cpl^conv survives only under (ii-W)
  applied to absolute emergent quantities, which no corpus text adopts. |"
- **Corrected.** Row 2 of §1 of this record.
- **Support.** As X-1 and X-3.

### X-19. NOTES-r5 §5, owner question Q7

- **NOTES-r5.** NOTES-r5:82–84: "Should GR:346 as argued (ii-L) be held as a premise under §A.29? Doing
  so excludes K_cpl^conv and gives (DZ) conditionally. It removes GR:400's Reading 1, and the feedback
  stated at GR:358 and GR:374, only if §8.3's identification fails. Otherwise those passages stand."
- **Corrected.** "Should (ii-L), or (ii-G), be held as a premise under §A.29? GR:346's argument does not
  supply (ii-L) on Readings E and D; on Reading G it gives (ii-G), whose application to K_cpl^conv needs
  B_G (open). Holding (ii-L) excludes K_cpl^conv, and gives (DZ), only when `ρ_Z` varies with the
  configuration through the partition and §8.3 is not in force; it is silent under Z_0. It removes
  GR:400's Reading 1, and the feedback stated at GR:358 and GR:374, only if §8.3's identification
  fails. Otherwise those passages stand."
- **Owner record.** #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU2: "(ii-L) stays open as a
  §A.29 candidate. It is conditional on the bridge premise B_G and is not adopted."
- **Support.** U2Ar3:82–85, :685–689, :829–832.

### X-20. NOTES-r5 §5, owner question Q8

- **NOTES-r5.** NOTES-r5:85–87: "The reconciliation of GR:346 with the wording "emergent vacuum energy"
  at GR:358, GR:374 and GR:400 is supplied by GR:400's qualifier "relative … in the sense of §8.3". It
  is conditional on §8.3's identification (GR:573). It is not stated at GR:346."
- **Corrected.** "On Readings D and G, the reconciliation of GR:346 with the wording "emergent vacuum
  energy" at GR:358, GR:374 and GR:400 is supplied by GR:400's qualifier "relative … in the sense of
  §8.3". It is conditional on §8.3's identification (GR:573). It is not stated at GR:346. On Reading E
  no reconciliation is needed." The rest of Q8 is unchanged.
- **Owner record.** #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU3: "no manuscript reading of
  GR:346 is chosen yet. Q8's correction stays deferred."
- **Support.** U2Ar3:715–720, :833–840.

***

## 3. Statements of r5 that stand

Unit 2(a) r3 leaves the following unchanged. Each is cited so that its standing is explicit.

- **Part 1** (U1r5:43–47, :562–564) and every statement about K_cpl^free: it survives (ii-W) and
  (ii-L), (ii-S) excludes it, and it is world-equivalent to K_dec with Λ₀ left undetermined
  (U2Ar3:726).
- **The fine-tuning statement** of U1r5:356–359 (§3.1 (b)). Unit 2(a) extends world-equivalence with
  K_dec to K_cpl^conv[Z_I] and K_cpl^conv[Z_II] on the de Sitter class with the constant left free
  (U2A-F3), and leaves unit 1's statement on the split of the constant unchanged (U2Ar3:91–93,
  :697–708).
- **(DZ) as a property of the source map**, and K_cpl^conv's violation of it [A] (U1r5:226–230,
  :335–337).
- **The reconciliation of Reading 1 through §8.3** (U1r5:496–506), conditional on §8.3, and its
  epoch-differential caveat. Unit 2(a) places it on Readings D and G (X-4, X-17).
- **B1–B4, R1–R3, F2–F7, F9**, and the assumption-watch markers AW-prov, AW-abs and AW-G12.

***

## 4. Limits

- This record restates conclusions of unit 2(a) r3 at their stated scope and derives nothing new. The
  support of each corrected statement is the cited unit 2(a) r3 lines, which rest on hand derivations
  ([A]) and on readings of paper arguments ([P]).
- Every correction is scoped to the exact de Sitter class and to assumption M1. Outside that class no
  claim is made, and the corpus has not established a coupling across general metrics.
- No zero-point convention is selected. Z_I and Z_II are constructed conventions, and no OI premise
  selects Z_0 over them (U2Ar3:654–656).
- The owner decisions quoted in X-19 and X-20 are cited as records; this record does not change them.
