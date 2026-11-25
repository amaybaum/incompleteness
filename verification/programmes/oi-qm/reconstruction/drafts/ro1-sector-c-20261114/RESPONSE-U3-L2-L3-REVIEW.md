# Response to the independent review of L-2 and L-3

**Object reviewed.** `S3-U3-r2.md`, blob `34ffe55245055ea0e5ca9138223de267785dbe74`, owner-accepted
(#1169 c.6892563291, `amaybaum`, 2026-11-15T09:49:19Z), §§5.1–5.2.
**Review.** `REVIEW-U3-L2-L3.md`, blob `3a81d18dbaaeb77e32be46948723f469d2f7f864`, at
`8a48c795e6b5a0a53c27c1b33ad9ed4776d0ba97` on branch `research/ro1-sector-c-1169-20261114`.
Verdicts: L-2 and L-3 "PROVED AS STATED"; required R1–R3; optional O1–O6.
**Revision.** `S3-U3-r3.md`. r2 is left unchanged. r3 differs from r2 only by the corrections below
and their necessary consequences.

**Writer:** Claude Code. Paper-only: reading and hand reasoning. The literature in the review was
read first-hand by its reviewer; this response cites it as the review gives it and did not re-read
it.

**Label kept.** Both lemmas stay labelled "proposed", and their uses stay marked conditional, until
the owner records a decision on the review. The status lines of §§5.1–5.2 and the header now record
the review's verdicts.

## Required

**R1. "Every … realization" outruns L-2's hypotheses. Applied** at the six listed sites and at three
sites with the same pattern:
- RQ-REU (§3): the hypotheses (k1)–(k5) are named, with "`Δ₄` alone supplies neither (k3)'s pairs
  nor (k4); M-PR5, with budget 1, lies outside (k3)".
- RQ-UPD-1 (§3): restricted to reuse meeting (k1), (k3), (k4), (k5), with the (k4) exposure stated
  (S5 not assumed; Main:416–423).
- §4.1, both sentences; U3-1 (§8); §10.2 RR-1 row; CQ-2 (§10.4): "meeting (k1)–(k5), in particular
  (k3) and (k4)".
- Necessary consequences: §4.4's sub-form route, and §10.3's candidate-restriction and RQ-UPD rows.

**R2. Prior-art status of L-2. Applied.**
- §5.1 gains a "Prior art" paragraph: L-2 is a sharpened special case of A. Valentini, "Signal-locality
  in hidden-variables theories", Phys. Lett. A **297**, 273–278 (2002),
  doi:10.1016/S0375-9601(02)00438-3, arXiv quant-ph/0106098. Sharper in three respects: the first use
  prepares the nonequilibrium subensemble operationally; on it the signal is guaranteed, not generic;
  no quantum-equilibrium law is assumed.
- U3-1's class is ELABORATING against the literature, new only relative to the corpus.
- §1, §5.1 and §10.6 no longer say the literature was not searched; they cite the review's check.
- L-3 is recorded (§1, §5.2) as the Bell-wing analogue of the repeatability-forces-memory argument
  of M. Kleinmann et al., "Memory cost of quantum contextuality", NJP **13**, 113011 (2011), arXiv
  1007.3650, App. A. S. Popescu, PRL **74**, 2619 (1995) is recorded as not accessible.

**R3. The update L-3 forces can be wing-local readback. Applied.**
- §5.2 Scope states the review's construction `λ = (R, C, f_A, f_B)`, which reproduces (1) times (9)
  with each wing reading only its own first record and a preloaded bit. I re-checked it by hand: the
  first use gives (1) at `η*`; at a repeated setting `a₂ = a₁`, `b₂ = b₁`; at a changed setting
  `f_A`, `f_B` are fair and independent of `(R, C)` and of each other; each wing's two-use history
  law does not depend on the remote settings. L-3 is stated as requiring the remote-dependent wing
  to consult its own first record or equivalent information, not a cross-wing or hidden-sector
  update.
- RQ-UPD-2 (i) and its closing sentence (§3) and U3-2 (§8) say readback suffices.
- §10.1's RQ-UPD row is narrowed to "no executed or native source-update process on record". It
  cites the designed construction [OFF] and Main's comb. I checked Main:480–482 at `75cc5100`: the
  intervention-dilation theorem realizes any finite action-labelled family with history-indexed
  responses on one bijection. It is cited at K-4 standing, representable only (U1:819).
- §10.6 reads "an executed or native deterministic realization of QR-1 meeting RQ-UPD-2 (a designed
  one is elementary)".

## Scope notes recorded

- L-2 assumes measurable response maps: added to (k1) (O5).
- L-3 does not need (k1), by dilation: added to §5.2 Scope, and its scope line now reads
  "deterministic or dilated".
- L-3 (b) uses only `|CHSH| > 2`: added to (b).

## Optional

- **O1** (L-2 extended to wing-local noise): **not applied**. It needs a new policy pair in (k3) and a
  new argument, so it is more than one line. L-3's half of O1 is recorded as a scope note.
- **O2** ("or" to "and" in (k3)'s mirror clause): **applied**.
- **O3** (widen L-3 to any Bell-violating table with one-wing repeatability): **partly applied**.
  Only the `|CHSH| > 2` scope note is applied; the widening of the statement is not one line.
- **O4** (name (k3′) at RQ-UPD-2 and U3-2): **applied**.
- **O5** (state measurability once): **applied**, in (k1).
- **O6** (U3-2 to ELABORATING): **applied**, with the Kleinmann et al. relation stated.

## Not changed

§10.7's owner questions keep r2's wording; the owner's answers are recorded in c.6892563291 and are
outside these corrections. No H-RR status, routing target, readiness or authorization changes.
