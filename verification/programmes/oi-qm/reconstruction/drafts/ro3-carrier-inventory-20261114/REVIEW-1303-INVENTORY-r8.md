# Focused confirmation: RO-3 inventory r8 (PR #1303), with RESPONSE-r7, and the "finite deterministic" classification

**Verdict on r8: ACCEPT WITH CHANGES.**

- M1, M2 and M3 are applied.
- Nothing outside the header, the Standing scope bullet and §7 changed.
- Three small corrections remain: N1 to N3.

**On the owner's condition.** With N1 applied, I find no further consumer. The map then meets the
owner's condition ("The A1 map must be complete before it is accepted", #1169 c.6894115930) on two
terms:
- it is complete relative to the recipe of §7.0, rerun at `7ac74a4b`;
- one scope limit is stated: 33 Lean modules that mention neither the substratum nor any dynamics
  token were not read.

I recommend that r8, or its successor, state this plainly instead of leaving it to the review.

**Classification of the 26 "finite deterministic" sites in the papers:**
- **(i) correct as stated:** 15;
- **(ii) overstated:** 0;
- **(iii) ambiguous:** 11.

No paper site states total finiteness as an axiom or as derived. The 11 ambiguous sites state a
finite substratum as the setting of the framework or of its results, without naming the posit. That
is the framing the owner corrected.

## Object, base and limits

- **Reviewed.** `RO3-INVENTORY-r8.md` and `RESPONSE-r7.md`, against my review of r7. That review's
  digest, `8e153d8d…1b402`, matches the one r8 cites.
- **Base.** `main` `7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac`.
- **Limits.** Read-only: `git show`, `git grep` and `diff`. Nothing was built, run, posted or fixed.

## 1. Whether my r7 items are applied, and what else changed

- **Scope of the diff.** Between r7 and r8 the hunks fall only in three places:
  - the header and change list (r8:1–43);
  - the Standing scope bullet (r8:86–89);
  - §7 (r8:928 to the end).

  §0 to §6 are byte-identical apart from line offsets.
- **M1: applied.**
  - Step 3b is added to §7.0.
  - The items placed in rows:
    - GR:70 and GR:28 in AM-22;
    - SM:1225, :1227 and :292 in AM-4;
    - SM:1388 in AM-31;
    - Complexity:374 in AM-20;
    - Sub:94 in AM-3, and GR:861 in AM-33;
    - the framing lines in AM-10.
  - GR:613 is AM-36. The §7.2 entry for GR's universality results is withdrawn.
- **M2: applied.** The nine modules flagged by the discriminator were read.
  - Census 3's four quotient modules are AM-38. I checked `itiRelK` :79, `itiRelInf_iff_orderOf`
    :304, `DomainGlue` :75, `ControlledQuotient` :51 and `CoherentExtension` :251.
  - The five operational-carrier modules (census 4 and 5) go to §7.2.
  - The remaining 33 are named in §7.4 and stated as unread.
- **M3: applied** (§7.0).
- **New finds, verified at source.**
  - AM-37, Struct:1255: "the visible factor of a finite deterministic bijection has zero asymptotic
    entropy rate". The [IR] Bernoulli counterpart is labelled correctly.
  - The §7.2 constructed-carrier entries: Main:214, :433, :480, :524, :552, :578; GR:278;
    Introduction:53; Sub:533; Struct:1273.
  - The false hits: Juno:261, Meth:397 and :401, and appendix-c:230.
- **§7.5 counts.** I reran `(?<!de)finite[ ,]+deterministic`, case-insensitive. It gives 26 paper
  lines, 30 book-chapter lines and 29 FULL lines, as stated.

## 2. Required changes (minor)

### N1: one mirror is missing

`papers/Introduction.md:67` reads: "one fixed finite world eventually repeats itself, so its record is
periodic … a non-periodic pattern has no exact realization for all times by one fixed finite world
[Main §3.4]". It mirrors AM-9 (Main:638).

My check of step 3b's phrase family against r8's citations found only this line uncited, apart from
a bibliography entry (Introduction:212) and a classification (Struct:280).

### N2: AM-10's status is wrong for 11 of its sites

AM-10 says "each is conditional on A1 by its wording". That holds for Main:36, :44, :222 and :718.
It does not hold for the 11 framing sites classified (iii) below, which name neither A1 nor a posit.

Restate AM-10's cell as follows:
- these sites state a finite substratum as the setting without naming the posit;
- they are recorded for the owner's correction (§7.5);
- their status is statements, not theorems.

### N3: AM-36's reason for S4 is stated too strongly

S4 as stated (GR:667) is "a CPTP channel admitting Stinespring dilation". It cites Main §3.2, whose
setup is under A1 (Main:266). S4 itself does not require a finite `C_H`.

The A1-relevant inputs that are actually traced are:
- (U1)'s finite counting (GR:58, AM-22);
- S2's C3, formulated through `|C_H|`;
- GR:613's explicit finite hypothesis.

The finding stands as worded, "the A1-freedom of (U1)–(U3) is not established at source". Its stated
reason should change from "S4 … is itself under A1" to "S4 cites the finite §3.2 construction".

### Aside, not a change to r8

SM:250 writes "a FINITE deterministic bijection". That is capitals used for emphasis in paper prose,
contrary to AGENTS.md §A.33. It is recorded here for the later manuscript unit and has not been
fixed.

## 3. Classification of the "finite deterministic" sites (read in context at `7ac74a4b`)

Criteria:
- **(i) correct as stated.** Finiteness is a hypothesis of a stated result, a class definition, a
  stated proposal, posit or commitment, part of a model's definition, or a constructed carrier.
- **(ii) overstated.** Total finiteness is stated as an axiom or as derived.
- **(iii) ambiguous.** A finite substratum is stated as the framework's setting, its object, or the
  scope of its results, without naming the posit.

### Paper sites (26)

| Site | Class | Reading in context |
|---|---|---|
| Complexity:27 | (iii) | "The companion papers prove that an embedded observer in a finite deterministic system with conditions C1–C4 … admits an exact fixed-basis unitary representation". The results are scoped to a finite system without naming the posit. Main:60 states the law-level result for every finite-horizon law. |
| GR:28 | (i) | Tier 1 holds "for any finite deterministic system meeting the four conditions": a hypothesis that scopes the results. |
| GR:70 | (i) | "the thermal rate ratio from finite deterministic reversible counting". A derivation on the finite shell of GR:58, under H-count (AM-22). |
| GR:613 | (i) | "Let 𝒮 be any finite deterministic substratum …": the hypothesis of the claim. The consistency with GR:669 is AM-36's finding, and is separate from this classification. |
| GR:705 | (i) | "this four-paper synthesis … proposes that the Standard Model and general relativity descend from one finite deterministic construction": stated as a proposal. |
| GR:861 | (i) | "The Page value enters through H-scramble, not through the finite deterministic dynamics": inside A.8 and A.9's stated finite shell. |
| Main:14 | (iii) | "An observer embedded in a finite deterministic system cannot access the complete state." The opening sentence frames the equivalence on a finite system. Main:60 says the axioms do not fix `|S|`, and that the law-level equivalence holds for every finite-horizon law. |
| Main:216 | (i) | "… by structural necessity, conditional on the total-finiteness posit": the posit is named. |
| Main:710 | (iii) | "The present framework's distinguishing feature is that it derives this content from a finite deterministic substratum." The finite substratum is presented as the source of the equivalence, which Main:60 places outside A1. |
| Methodology:337 | (iii) | "The framework's forward direction runs from a finite deterministic construction — a bijection (S, φ) on a finite configuration space — to observed physics": the starting point, unqualified. |
| SM:250 | (i) | "a FINITE deterministic bijection in place of a continuous flow": SM's model, which is a finite torus by definition (SM:294–306). Capitals noted in §2. |
| SM:1388 | (i) | "Any finite deterministic system with energy-conserving dynamics …": the hypothesis of the Corollary. |
| SM:1592 | (iii) | "makes a single claim: the Standard Model and general relativity are projections of one finite deterministic construction": asserted, with no posit named. |
| Structure:21 | (i) | "OI's specific structural class of finite deterministic bijection systems": a class definition, the A1–A6 class. |
| Structure:45 | (iii) | "The starting point is an observer embedded in a finite deterministic system: … every such law admits an exact fixed-basis unitary Born representation". As Main:14. |
| Structure:108 | (iii) | "the framework's distinguishing feature is producing the consequences from a finite deterministic substratum". As Main:710. |
| Structure:377 | (i) | "OI's structural class — the class of finite deterministic bijection systems with bounded coupling …": a class definition. |
| Structure:528 | (i) | "The structural conditions for observer admission [Main §3] are formulated for finite deterministic substrata": accurate about the formulation; C3 is stated through `|C_H|`. |
| Structure:741 | (iii) | "OI's substratum is a finite deterministic bijection on a d=3 cubic lattice": asserted as what the substratum is. Theorem 23 yields "S finite" only given A1. |
| Structure:1255 | (i) | A mathematical statement about finite bijections (AM-37). |
| Structure:1273 | (i) | Constructed: "the visible marginal of a finite deterministic bijection, depending on K". |
| Substratum:14 | (i) | "This paper develops the alternative that they are two projections of a single finite deterministic construction": stated as a proposal, in a paper whose A1 is a named structural assumption (Sub:92, :123). |
| Substratum:16 | (iii) | "the same finite deterministic object supports the visible stochastic/quantum projection …": asserted. |
| Substratum:22 | (iii) | "The underlying object is a finite deterministic bijection (S, φ)": asserted. |
| Substratum:367 | (iii) | "projections of the same finite deterministic construction": the synthesis claim, unqualified as to A1. |
| Substratum:533 | (i) | "every finite adaptive quantum experiment has a finite deterministic realization": constructed. |

**Counts:** (i) 15, (ii) 0, (iii) 11.

The (iii) sites are Complexity:27, Main:14, Main:710, Meth:337, SM:1592, Struct:45, Struct:108,
Struct:741, Sub:16, Sub:22 and Sub:367.

### Book chapter lines (30), grouped by the paper sentence they mirror

| Group (paper sentence) | Class | Book lines |
|---|---|---|
| **B1.** Results scoped to "an observer embedded in a finite deterministic system/universe" (Main:14, Struct:45, Complexity:27) | (iii) | `ch00-introduction.md:59` ("the finite observable law of any observer embedded in a finite deterministic universe has an exact fixed-basis quantum representation"); `ch05-gauge-structure.md:11`; `appendix-c-objections.md:224`; `ch01-observation.md:235`; `ch12-evolution-intelligence.md:211` |
| **B2.** "Starts from / derives from a finite deterministic substratum" (Main:710, Struct:108, Meth:337) | (iii) | `ch00-introduction.md:69`; `ch03-structural-realism.md:22`; `ch03-structural-realism.md:230`; `ch09-universality.md:300`, :314 |
| **B3.** "The substratum / underlying object is a finite deterministic bijection" (Sub:22, Struct:741) | (iii) | `ch00-introduction.md:95` ("Chapter 2 constructs the substratum — the finite deterministic bijection"); `ch12-evolution-intelligence.md:213` ("The framework's substratum is a finite deterministic system") |
| **B4.** The synthesis claim, "projections of one finite deterministic construction" (Sub:16, Sub:367, SM:1592) | (iii) | `ch02-substratum.md:184` (conditional on H-Bell, with the posit not named); `ch03-structural-realism.md:196` |
| **B5.** Universality-class results with a finite substratum as hypothesis (GR:28, GR:613, SM:1388) | (i) | `ch07-gravity.md:14`; `ch09-universality.md:14`, :42, :61, :84, :118 |
| **B6.** The BQP characterization with "a finite deterministic system" as hypothesis (the Computation/Complexity BQP theorem; AM-23) | (i) | `README.md:82`; `ch14-quantum-computing.md:12`, :34, :100, :146 |
| **B7.** Finiteness stated as a commitment or postulate (GR:705, Sub:14) | (i) | `ch09-universality.md:18` ("commitments to a finite deterministic bijection"); `ch09-universality.md:184` ("it postulates a finite configuration space with a deterministic bijection"); `ch19-open-problems.md:214` |
| **B8.** Constructed carriers (Struct:1273, Sub:533) | (i) | `ch01-observation.md:179` |
| **B9.** A.8 and A.9 (GR:861) | (i) | `ch07-gravity.md:149` |

**Book counts:** (i) 16, (ii) 0, (iii) 14.

One wording note on `ch03-structural-realism.md:22`. It reads "what is derived from it: a finite
deterministic substratum … without additional postulates beyond … posit A1 of Chapter 2". Read
alone, "derived" approaches (ii). The same sentence names A1, so it is classed (iii).

**FULL mirrors.** The 29 FULL lines mirror the chapter lines. `README.md:82` has no FULL counterpart,
which accounts for 30 against 29. They take the class of their chapter line.

### What the classification implies

- **No (ii) site.** No site needs correction as an asserted axiom or derivation.
- **The (iii) sites need correction.** That is 11 paper sites and 14 chapter lines, with their FULL
  mirrors. Each states a finite substratum as the setting or object without naming the posit.
  - For the sites in B1, and for Main:14, Struct:45 and Complexity:27, this also narrows the
    law-level result, which Main:60 states for every finite-horizon law.
  - That is the framing the owner corrected at #1169 c.6893456888. A manuscript correction under
    §A.25 would cover these sites. The correction itself is not authorized here.

## Summary

- **r8: ACCEPT WITH CHANGES.**
  - **N1.** Add `Introduction.md:67` to AM-9.
  - **N2.** Restate AM-10's cell for the 11 sites that do not name the posit.
  - **N3.** Reword AM-36's S4 reason.
- **The owner's condition.** With N1 applied, the map is complete relative to the recipe, with the
  33-module scope limit stated.
- **Classification.** Paper sites: (i) 15, (ii) 0, (iii) 11. Book chapter lines: (i) 16, (ii) 0,
  (iii) 14.

## r9 addendum

**Verdict on r9: ACCEPT.**

- **Changes from r8.** The only changes are:
  - the header and change list;
  - AM-9, AM-10 and AM-36;
  - §7.4's first bullet;
  - the new §7.6.

  §0 to §6 and every other row are unchanged; I checked this with `diff`.
- **N1 to N3.**
  - **N1.** AM-9 carries `Introduction.md:67`, quoted correctly.
  - **N2.** AM-10 limits "conditional on A1 by their wording" to Main:36, :44, :222 and :718, and
    records the (iii) sites as not conditional by their wording.
  - **N3.** AM-36 says that S4 does not itself require a finite `C_H` but cites the finite §3.2
    construction. It lists the A1-traced inputs, and its finding is unchanged.
- **§7.6.**
  - It matches §3 of this review: the criteria, every site and its class, the counts, the book groups
    B1 to B9, the FULL rule and the two notes.
  - Counts: papers (i) 15, (ii) 0, (iii) 11; book chapter lines (i) 16, (ii) 0, (iii) 14.
- **§7.4.** It records the finding of this review accurately and leaves acceptance to the owner.

**The owner's condition.** r9 meets the owner's acceptance condition for the map ("The A1 map must
be complete before it is accepted", #1169 c.6894115930) on two terms:
- it is complete relative to the recipe of §7.0, rerun at `7ac74a4b`;
- one scope limit is stated: the 33 unread Lean modules.

Acceptance is the owner's decision.
