## Confirmation of PR #957 at `9eff10d3`: CONFIRM, with one small wording issue in departure (i)

Everything else checks out: the diff is limited to the stated changes, departure (ii) is correct against SM, the mirrors are byte-identical, the ledger matches the census, and the `.tex` stamps match.

**1. Scope of the diff.** `9eff10d3` is a single-parent child of `806b57dc`. The markdown changes are exactly these, plus the regenerated `.tex`/`.pdf` and one ledger fingerprint:
- **Main :256:** the boost clause now reads "when the coarse-graining map determines a simultaneity foliation (the hypothesis under which the §3.5 lemma excludes boosts)".
- **Main :664:** a new opening, "Under the lemma's hypothesis, because…", and the new condensate clause.
- **Main :668:** "its symmetry, under the lemma's hypothesis:".
- **SM :136:** "for boosts, when the coarse-graining map determines the horizon foliation, the hypothesis under which [Main §3.5] excludes them".
- **SM :1418:** "its result that … and excludes boosts when it determines the horizon foliation", with "The honest summary is that" replaced by "In summary,".
- **ch19 :246 and :248, and their FULL mirrors:** the matching wording.

**2. Each change against the sources.**
- **Corollary condensate clause (Main :664):** "since the $O$-invariance of the dynamics does not descend to the solution, the effective operator is octahedral-invariant only if the condensate is $O$-equivariant, an alignment that the identification of the blocks with the link-direction irreps secures and that leaves the $E_g$ channel exactly null". This matches SM :136 point for point:
  - the condition is necessary only ("only if"), as in SM;
  - the group is $O$, consistent with SM :338 Theorem 5 ("Let Σ … be $O$-equivariant");
  - the reason ("does not descend to the solution") and "What secures the alignment is the geometric identification of the blocks with the link-direction irreps" are SM's own wording;
  - "an equivariant condensate leaves the $E_g$ channel exactly null" is also SM's.
- **Departure (ii)** is therefore sound.
- **The other edits** at Main :256, :664's opening and :668, and SM :136, correctly attach the hypothesis to the boost exclusion.

**3. Departure (i): mostly sound, one wording issue (minor, required).**
- **What is right:** the selection of n needs no extra premise when the subject is the horizon or partition. The lemma's own hypotheses say "The horizon fixes a simultaneity foliation …, hence … $n$", and the corollary rightly says "the horizon partition defining $T$ selects … $n$". Only the boost exclusion needs "T determines the foliation".
- **The issue:** SM :1418 ("the observation map selects a timelike direction … and excludes boosts when it determines the horizon foliation") and ch19 :246 / FULL :5406 ("the map selects a timelike direction, no spatial one, and excludes boosts when …") make *the map* the subject of the unconditional selection.
- **Why it matters:** Main's own Converse (:666) uses "$T$ selects a rest frame" to mean selection through T's invariance group, and that sense does need the premise. If T does not determine the foliation, the horizon still selects n but T need not.
- **Proposed fix:**
  - SM :1418: "…via its result that the horizon partition defining the observation map selects a timelike direction but no spatial one, and that the map excludes boosts when it determines the horizon foliation."
  - ch19 :246 and FULL :5406: "(the horizon partition defining the map selects a timelike direction, no spatial one, and the map excludes boosts when it determines the horizon foliation)".

**4. Mirrors.** ch19 :240/:242/:246/:248 and FULL :5400/:5402/:5406/:5408 are byte-identical.

**5. Ledger.** `MAIN:C-boost-rotation-inequivalence` is `80a3ef4c8a39c4ad` in both the ledger and the census. `MAIN:L-rest-frame-selection` is unchanged at `990927d001224c55`, which also matches.

**6. `.tex` stamps.** The source-sha256 stamps match their `.md` sources for Main, SM, Substratum and FULL, and `staleness_check` reports OK. Main, SM and FULL `.tex`, regenerated with the `build.sh` recipe, are byte-identical to the committed files.

The worktree used for this check has been removed.
