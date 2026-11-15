# Diff check of S3-U2-r3 against N1 and N2 (independent, non-author)

**Objects.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U2-r3.md`
and `RESPONSE-S3-U2-r2.md`, at PR #1294 head `3763645fce41a8de4298a389c250f8042fcebf8f`. Diffed
against `S3-U2-r2.md` at the same head. Corpus at `origin/main` `75cc5100`. Read-only.

## Verdict: ACCEPT. U2 is ready for owner acceptance.

## 1. N1 and N2

**N1: resolved.** I checked the three anchors at source on `origin/main`:
- Substratum:76 is E1: "The observed physics is described, to the precision tested, by quantum
  mechanics … Born-rule outcome statistics."
- Substratum:475 heads Class A: "would falsify the framework's reconstruction if violated."
- Substratum:481 is the Bell/Tsirelson item, quoted accurately.

r3 §6.2 gives the datum at both sites with the right status. E1 is the empirical input, and the
`2√2` implication is labelled [A-inf]. Substratum:481 is the matching Class A falsification
condition. "The corpus states no measured CHSH value" is accurate as far as my earlier corpus grep
reached. The M-PR5 row and §11.2 now make the miss conditional on `Θ` given E1. The "only as a
falsification condition" claim is gone from both sites.

**N2: resolved.** In §3's SEL-EXCL-1-family column and in §11.1's M-PR(m) column, CP-6, CP-7 and
CP-8 are now *not available* at the scope of the specified circuit, by its declared grammar, with
the K-1 caveat that this rests on a declaration. Exhibiting an executing tuple is a *stop*. Both are
states the outcome vocabulary declares. The grammar quotes match SEL-EXCL-1 l. 91: "There is **no**
unilateral stop/ready request that changes the remote clock or success field, arbitrary choice of the
next source-cell index". CP-6 in reading (g) is *not available* at that tuple's scope, because the
specified `φ_m` touches no `r_j` before use `j`. "No other state is used" now holds: I scanned §§2–3
and §11.1 and found no undeclared state.

**P1, P2: applied** as suggested (§6.2, §11.2).

## 2. The extra CP-8 edit

It is consistent. Once CP-8's §3 cell has a *stop* for "a tuple that executes it", the §3 closing
K-1 sentence and the §8.3 stop list must name CP-8 alongside CP-6 and CP-7. The edit is the
necessary consequence of the mapping and adds no claim.

## 3. Nothing else changed

The r2-to-r3 diff (63 lines) touches only:
- the title;
- the new revision note;
- the outcome-vocabulary sentence;
- the §3 table and its closing sentence;
- the §6.2 bullets, condition sentence and M-PR5 row;
- the §8.3 stop item;
- three §11.1 rows;
- the §11.2 performed-experiment bullets and the CP-4 resource line.

Every change maps to N1, N2, P1 or P2. No verdict moves. Other files at this head
(`GAMMA-PLAN-r1.md`, README) are outside this check.

## Optional (cosmetic, no change needed for acceptance)

- §11.2's first performed-experiment line exceeds the file's usual line width.
