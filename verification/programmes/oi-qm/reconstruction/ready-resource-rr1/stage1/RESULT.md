# RR-1 stage 1: execution result (paper-only)

**Protocol.** `verification/programmes/oi-qm/reconstruction/ready-resource-rr1/preregistration.md` at `c41e0e6f` (blob `77a471ac`, checked
by `git rev-parse` before any row below was written), with `assessment.md` in the same directory. Owner decisions as relayed to the
executor (#914 c. 6558349705): H-sel admissible only as RR-AVAILABLE[H-sel]; H-law admissible conditionally; W-certified reported as the
stronger diagnostic. Paper-only: no Python, script, Lean run or checker run; two `checks.py` files were read as text. PR #1025.

## 0. Anchor key (repo-relative; `file:line` at the stated SHA)

- `PR`, `AS`: the preregistration and assessment above, at `c41e0e6f`. `Main`: `papers/Main.md` at `5914c17c`.
- `MR-pre`, `MR★`: `verification/programmes/oi-qm/reconstruction/measurement-record-formation/{preregistration.md, amendments/MR-star.md}` at `af1e9be2`.
- At `d4a80fc8`, under `verification/programmes/substratum/continuous-substates/`: `CI` native-causal-interface.md; `K` native-packet-stochastic-kernel.md;
  `AB` native-actuation-boundary.md; `CR` native-port5-cone-reduction.md; `NC1` native-coupling-nc1-preregistration.md (unaccepted draft, tagged [draft]).
- At `d4a80fc8`, under `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`: `IC` shared_v12/INTERFACE-CONTRACT.md;
  `h9` history_v9/REPORT.md; `h10` herald_v10/REPORT.md; `h11` history_v11/REPORT.md; `s12` native_seed_v12/REPORT.md; `d14` native_decode_v14/REPORT.md;
  `v15` native_vread_v15/REPORT.md; `v15c` native_vread_v15/checks.py; `r13c` native_route_v13/checks.py; `SG` parallel_v3/history_control/SOURCE-GEOMETRY.json;
  `P3` parallel_v3/COMBINED-REPORT.md; `r7` reset_v7/PROBE-PLAN.md.
- Fixed symbols: q8=(0,S,76), q9=(0,S,77), q10=(0,S,78), L=R+9=S+77 (v15c:32–33; IC:32). Ports and deadlines v15c:377–380. Ready balls, table order:
  24 inherited, then B_{L+1}(q10) (v15c:384–391); previous-slice radius r−1 (v15:103). Named exceptions (17): v15c:541–549. Inventory classes:
  source → PINNED, bank ray → BANK, ready ball → PINNED, else FREE (v15c:563–575; previous slice v15c:607–614).

## 1. Readings fixed before the rows, and protocol ambiguities

- **AMB-0 (freeze wording).** PR:3–4 still reads "PROPOSAL ONLY. Not frozen"; PR:131 requires a separate owner freeze authorization. This run uses
  the file as frozen on the designation relayed to the executor; that authorization was not read and is not quoted here.
- **AMB-1 (overlapping pins, G7 step 4).** PR:95–97 ablates "one inventory item at a time … each given π_0 on its cells" and does not say what
  happens to a cell pinned by two items. Reading used: ablating item X removes X's declaration only; a cell still pinned by a retained item stays
  pinned (an override of the retained item would ablate part of a second item, against "one item at a time"). Effect of the other reading: every
  ready ball meeting E's pinned cells would be restored, enlarging Λ for C1/POS-1 and C5 by further ball pins; no token class and no S0 pass
  condition changes. **If the reviewer rules the clause ambiguous, POS-1 becomes UNRESOLVED(G7) and the stage STAGE-VOID.**
- **AMB-2 (Λ_0 and vacuous steps).** Λ_0 = the ablatable hypotheses the assessment's row uses + pins meeting the pullback (PR:93–94). A step for a
  hypothesis not in Λ_0 is vacuous and is not counted as "ablated" for G9's third trigger. Every candidate here has stated prior π_NY, so H-sel ∉ Λ_0
  throughout. π_sel has no written law in the sources read (MR★:1364–1366 names a route), so a π_sel-stated candidate would stop at UNRESOLVED(G1).
- **AMB-3 (source-table order).** Types in the order of PR:95–96; within type: balls v15c:384–391, compiled sources SG row order, named exceptions
  v15c:541–549, payloads E then N (d14:49–51).
- **AMB-4 (pin granularity).** Pins are taken per cell, with a source cell in the source class before ball membership (v15c:563–568).
- **AMB-5 (SG schema).** SG rows carry `field`, `mask`, `owner`; read as one affine payload bit per row, `mask` selecting the owner's seed bits
  ("affine source entries", P3:103; h10:42–45). The schema is not documented in the sources read; used in C2 only.
- **AMB-6 (G9 independence).** The second pullback is derived by a different route by the same executor; author-independence needs a second executor.
- **Source-law payload not added as a candidate.** PR names it only as a pin item (PR:32, 96); the occurs/accessible/preparable table (AS:102–109) has no such row.

## 2. S0 (stage gate)

**POS-1** (fixture PR:107; also candidate C1).
- G1. Site set: current B_{L+1}(q10), previous B_L(q10) (CI:24–25; s12:35–37). t_r=t_u=0. R_E: zero on every cell of the two balls not in the source
  class (s12:58 "initial zero constraints"; v15c:563–568); source cells unconstrained. Prior π_NY. π_0(R_E)=8^{−n_E}, n_E the number of constrained
  triples; n_E≥1 because q10 is not a source (v15c:541–549; r13c:258), so π_0(R_E)≤1/8. Pullback: E's cells ∪ supp W_0 = the eight tick-0 port cells
  (K:104–105; v15:63–65). Classified: non-source ball cells PINNED (q10 item; also the ten chain balls, nested by CI:79–86, and other inherited balls);
  source cells PINNED (SG cells on the boundary, s12:51–52; named exceptions in the ball, e.g. E and N at distance L+1, r13c:249–253); no BANK cell
  (s12:53–54; K:54–55); port cells PINNED (own port ball, v15c:385).
- G2 pass: P(ready)=1 under π_NY. G3 pass: under π_NY, E∈R_E a.s. and W_0 is the all-blank tick-0 record a.s.; P(ready | W_0=w)=1 at that w, and 1>8^{−n_E}.
- G4 pass: readiness rests on the preparation pin; no read, inverse, decoder, write, reset or actuator. G5 pass: event Ω, P(ready|Ω)=1 under H-law.
- G6 pass: t_r=0, E's source cells are its own cells; no reduction claimed (MR-pre:184–187).
- G7. (1) vacuous. (2) Two configurations equal on the eight port cells, q10's current triple 000 vs 001: same W_0, readiness differs; no f, W-certified
  no, H-law kept. (3) H-access ∉ Λ_0 (AS:104): vacuous. (4) Inherited balls in order: under AMB-1 every constrained cell stays pinned by the q10 item,
  P(ready)=1, G2–G5 pass: each removed. q10 ball: q10's cell then carries no pin, P(ready)≤1/8: restored. SG rows, named exceptions, E/N payloads:
  R_E leaves their cells unconstrained, P(ready)=1, G2–G5 pass: removed. **Λ = {H-law, q10-ball pin}; W-certified no.**
- G8 pass (H-access ∉ Λ). G9 passes without a full run (Λ has a pin, W-certified no, H-access not ablated: AMB-2). **G10: RR-AVAILABLE[H-law, q10-ball pin].**
- Control check (PR:107): RR-AVAILABLE, Λ ⊇ {H-law, q10-ball pin}, W-certified no. **POS-1 green.**

**NEG-1** (PR:108).
- G1. Site {f_5(L+4)} = port5+(L+4)e_y (K:77–78; h9:58; direction v15c:379). t_r=t_u=0. R_E={current triple 000}, previous slice unconstrained.
  π_NY. π_0(R_E)=1/8. Pullback: the cell (BANK: v15c:552–560, index L+4>a_5=S; K:79–80) and the eight tick-0 port cells (PINNED).
- G2 pass: P(ready)=1/8 (K:92). G3 fails: W_0 is a function of C (K:97–98) and Pr(eta=z|C=c)=8^{−28} (K:92), so Pr(E∈R_E, W_0=w)=Pr(W_0=w)/8 and
  P(ready|w)=1/8=π_0(R_E) for every positive-mass w. **RR-NOT-READY at G3. NEG-1 green.**

**CC-2(a), relabeling** (PR:109).
- G1. Site {p}, p=(0,S,S+160): not a source or bank cell, free on both slices (CI:111–121). σ(z)=z⊕(1,0,0); E'=σ(U_0(p)); R_E'=σ({000})={100}.
  t_r=t_u=0. π_NY. π_0(R_E')=1/8 (σ is a bijection). Pullback: p (FREE, v15c:575) and the eight tick-0 port cells (PINNED).
- G2 pass (1/8). G3 fails: p is independent-uniform given every other cell (PR:31–32; K:94–96) and W_0 uses other cells only, so
  Pr(E'∈R_E', W_0=w)=Pr(W_0=w)/8, P(ready|w)=1/8=π_0(R_E'). **Rejected at G3 (RR-NOT-READY). Green.**

**CC-2(b), private inverse chi_H** (PR:109; NC1:57–59 [draft], chi_H "representable, not available").
- G1. Site: the chi_H footprint at t_r=H=L+79, current radius 77 and previous radius 78 about q9 (AB:8, 31–41). t_u=L+2. R_E={x: chi_H(x).Q10.A ⊕
  chi_H(x).p.B = 0}, where Q10=U_{L+1}(q10) and p=U_L(q9) (AB:21–23, 37–38). π_NY. π_0(R_E)=1/2: the rule is a bijection (AB:12–16), the counting
  measure is invariant (Main:56), and the two bits are distinct coordinates of the uniform time-(L+1) state. W_{L+2}: port reads, whole-q9 at L, flags.
  Pullback (class level, rule v15c:563–575): PINNED balls (q10, chain), PINNED sources (SG, named incl. E, N), BANK rays (K:77–83), FREE cells (incl. keys, K:47–55).
- G2 pass: on accepted contexts q10.A=s (d14:23–27, 49–51) and p=(0,s,r_old) (IC:38–40; AB:26), so ready; continuing branches have positive mass (K:110).
- G3 pass: on the accepted-flag value w (IC:38–39), P(ready|w)=1>1/2.
- G4 fires: membership is evaluated only through chi_H, a private inverse on a mostly private footprint (AB:45–48); q10 is never a permitted read
  (d14:36), so the q9 read alone does not decide it. **RR-REPRESENTABLE-ONLY at G4. Green.**

**S0 outcome: green** (POS-1, NEG-1, CC-2 decided on paper; POS-1 subject to AMB-1).

## 3. Candidates (assessment §2 rows, AS:102–109)

### C1. q10 ready ball
G1–G10 identical to POS-1 (same element). **Token RR-AVAILABLE[H-law, q10-ball pin]; deciding gate G10; Λ={H-law, q10-ball pin}; W-certified no.**
Beside: (c) no sourced procedure; preparation only at original time (r7:19); a late controller needs a new pin (CI:91–93). Persistence: [0, L+1],
the ball being the q10 cone at L+1 (CI:24–25, 84–88). Consumption: carried by native evolution into q10 and the chain by L+1; no reset. FRESH-PACKAGE:
unresolved (AS:90; Main:566, 582). Renewal: RENEWAL-UNRESOLVED (h11:151–152).

### C2. Compiled sources and programs
- G1. Site: the distinct SG positions (current slice; previous unconstrained). t_r=t_u=0. R_E={values g(κ) for some seed/input assignment κ}, g the
  SG payload map (AMB-5). π_NY. π_0(R_E)=|g(K)|·8^{−n_c}, written symbolically, not evaluated. Pullback: E's cells (PINNED source, v15c:567) ∪ tick-0 port cells.
- G2 pass (P=1). G3 pass: SG rows 2 and 4 (owner R, mask 1, field 1; positions (−369,0,−1), (−368,0,−2)) carry the same seed parity up to fixed
  offsets, so R_E imposes a parity relation and π_0(R_E)≤1/2; under π_NY, E∈R_E a.s., W_0 blank a.s., P(ready|w)=1>1/2.
- G4 pass (pin). G5 pass (Ω under H-law). G6 pass (no reduction claimed).
- G7. (1) vacuous. (2) Flip row 1's field-2 bit at (−369,−1,0), not a port: the parity relation with row 6 (owner R, mask 3, field 2) breaks, W_0 is
  unchanged; no f, W-certified no, H-law kept. (3) H-access ∉ Λ_0 (AS:105): vacuous. (4) Balls do not pin source cells (AMB-4): each removed. SG rows
  in order: rows 1 and 2 are fixed by later retained rows with the same owner, mask and field (rows 6 and 4), so each ablation changes P(ready):
  restored. Each further row turns on how many rows share its cell and whether the retained rows fix its seed parities: a tabulation of the
  1479-row catalogue, not a written derivation. Undecidable on paper.
- **Token UNRESOLVED(G7:compiled source).** Partial Λ: H-law, SG rows 1–2; no ball. W-certified no.
- Beside: (c) no ("a standalone prepared apparatus", P3:110; r7:19). Persistence: until each row's first arrival (SG:4, deadline 185). Consumption:
  into the deadline records (h9:51–53). FRESH-PACKAGE unresolved. RENEWAL-UNRESOLVED.

### C3. Late fields q8 and the chain (member decided: q8)
- G1. Site {q8}, t_r=L−1 (U_{L−1}(q8), the previous q8 at L, IC:38). t_u=L. R_E={A=0 and D=0}. π_NY. π_0(R_E)=1/4 (bijective rule, Main:56).
  Pullback: q8's cone, inside the q10 balls with listed exceptions only (CI:79–89), no bank (h11:83–86) ∪ W_L's cones: port records through L incl.
  bank rays f_i(t), a_i<t≤L (h9:56–59), q9 at L, flags. Classes: PINNED ball, PINNED source, BANK, FREE.
- G2 pass: on the successful phase U_{L−1}(q8)=(0,y,0) (IC:38); continuing branches have positive mass (K:110). G3 pass: given the success-flag value
  w of W_L, U_{L−1}(q8)=(0,y,0) a.s., P(ready|w)=1>1/4. G4 pass (no read of q8; flags under H-law). G5 pass (success-flag event).
- G6 pass: E is a function of the pinned cone (CI:84–88), entropy invariant under the bijection (MR-pre:184–187); no reduction claimed.
- G7. Λ_0={H-law, H-access (flags are port reads, v15:63–65)} ∪ pins. (1) vacuous. (2) c1=(0,S+L−1,76) is at distance L−1 from q8 on a unique
  straight path; c2=(0,S+L,77) is at distance L from q9 on a unique straight path and L+1 from q8. Every port has y≤S and z≤0 (v15c:377–380), so c1, c2
  are at distance ≥L+75 from every port. Straight-path responses are permutations in any fixed background (h9:116–121; K:61–63). Change c1 to flip
  U_{L−1}(q8).A, then choose c2 to restore U_L(q9): W_L unchanged, readiness differs. No f; W-certified no; H-law kept. (3) Without stipulated reads
  W_L is trivial, and (b) under H-law needs P(ready)=1, i.e. A=D=0 at q8 on terminal contexts as well. The sources read state (0,y,0) only on the
  retained successful phase (IC:38; r7:17 gives the q7 endpoint without a branch statement). Undecidable on paper.
- **Token UNRESOLVED(G7:H-access).** Partial Λ: H-law. W-certified no.
- Beside: (c) only through the original-time pins (CI:91–93). Persistence: present at L−1/L; it enters q9's update at L (rule, CR:8); no later window
  stated. Consumption: by the native update. FRESH-PACKAGE unresolved. RENEWAL-UNRESOLVED.

### C4. Whole-q9 record at L
- G1. Site {q9}, t_r=t_u=L, current slice. R_E={U_L(q9).A=0}. π_NY. π_0(R_E)=1/2. Pullback: q9's cone ⊂ the q10 balls (triangle inequality, as
  CI:84–86) with source cells, no bank (h11:83–86) ∪ W_L's cones (as C3).
- G2 pass: q9=(0,s,r_old) on the successful phase (IC:38–40). G3 pass: W_L contains the whole-q9 read (v15:67); given the read value w with A=0
  (positive mass), P(ready|w)=1>1/2. G4 pass: declared read, not private. G5 pass (read event). G6 pass (no reduction claimed; it carries s, AS:107).
- G7. (2) f(W_L)=1[read A-field=0] equals 1[ready] at every configuration: W-certified yes, H-law removed. (3) Without stipulated reads W_L is
  trivial; with H-law removed (b) must hold from W alone, and a constant f cannot equal the nonconstant 1[ready]: (b) fails, H-access restored.
  (4) Inherited balls: the q9 cone stays pinned by the q10 item (AMB-1), the law of U_L(q9) is unchanged, G2–G5 pass: removed. q10 ball: whether
  P(U_L(q9).A=0) changes needs that law on terminal contexts (IC:38–40 states only the successful phase) and the post-ablation law; the one interior
  straight-path cell q9+L·e_z=(0,S,S+154) is the named source J (v15c:542), so the permutation step does not apply directly. Undecidable on paper.
- **Token UNRESOLVED(G7:q10-ball pin).** Partial Λ: H-access. W-certified yes (G9 would run in full had G7 completed).
- Beside: (c) only through the pins; it carries s, a record of the input and not a blank (AS:107). Persistence: kept as a stipulated read by
  convention (H-access, NC1:150–152 [draft]); the field is not a stored slice at L+2 (IC:63). Consumption: enters V at L+1 (v15:73–74).
  FRESH-PACKAGE unresolved. RENEWAL-UNRESOLVED.

### C5. Blank port prefixes before a_i (member decided: port 5 at tick 0)
- G1. Site {p5}, p5=(0,S,0), current slice. t_r=t_u=0. R_E={000}. π_NY. π_0(R_E)=1/8. Pullback: the eight tick-0 port cells (p5 among them).
  p5: not a named exception (v15c:541–549), not an SG cell (those lie at ≥L+1 from q10, s12:51–52; p5 is at 78, CR:11–12, v15:78), not on a bank
  ray (indices exceed deadlines, v15c:552–560): PINNED by ready balls, among them its own port ball and the q10 ball. Other port cells PINNED (own balls).
- G2 pass: P(ready)=1 (blank prefixes, h9:51–52; zero pins, s12:58). G3 pass: under π_NY, W_0 is all-blank a.s. and E is its port-5 entry;
  P(ready|w)=1>1/8. G4 pass: declared port read (h9:50; v15:63–65). G5 pass: event {port-5 entry of W_0=000}. G6 pass (t_r=0; no reduction claimed).
- G7. Λ_0={H-law, H-access (AS:108)} ∪ balls covering tick-0 port cells. (1) vacuous. (2) E is a coordinate of W_0: f exists, W-certified yes, H-law
  removed. (3) Without stipulated reads W_0 is trivial and a constant f cannot equal 1[ready]: H-access restored. (4) Inherited balls: p5 stays pinned
  by the q10 item (AMB-1), P(ready)=1, G2–G5 pass via the read: removed. q10 ball: no remaining item pins p5, so P(ready)=1/8: restored. Later
  items do not pin p5: removed. **Λ={H-access, q10-ball pin}; W-certified yes.**
- G8 pass (Λ contains a pin). **G9 in full (W-certified yes):**
  - *Second pullback (cone route).* E at t_r=0 has the radius-0 cone {p5}; W_0's cones are the eight tick-0 port cells (K:104–105). Classifying p5 by
    the rule v15c:563–575 gives PINNED (ready ball), with the q10 ball covering it (distance 78 ≤ L+1). Agrees with the first pullback.
  - *Adversarial note.* (i) W-certified yes comes from t_u=t_r: the record read is the element; that read is stipulated under H-access, which is not
    sourced record formation (PR:57–58; MR-pre:165), and the token carries H-access. (ii) The pin entry is order-relative (PR:98): with the ball table
    order the last covering ball, the q10 ball, is retained. (iii) Under the other AMB-1 reading every ball covering p5 is restored: the pin set grows,
    H-access stays, and no reading yields Λ without a pin. (iv) Only the tick-0 member is decided; ticks 0<t<a_i have cones of radius t and are not
    covered. (v) The favourable reading "a blank port is a native ready supply" is not supported: the blank is the original pin observed through a
    stipulated read. Notes and pullbacks agree: G9 passes.
- **Token RR-AVAILABLE[H-access, q10-ball pin]; deciding gate G10.**
- Beside: (c) only through the pins (r7:19). Persistence: blank for t<a_5=S (h9:51–52); decided member t=0 only. Consumption: replaced at a_i by the
  informative entry, then bank noise (h9:51–53, 61–66); each port is blank once (AS:108). FRESH-PACKAGE unresolved. RENEWAL-UNRESOLVED (h11:151–152).

### C6. Banks and the 28 keys
- G1. Site: the 28 eta cells (12 boundary keys at t=L+4, L+5, K:47–52; 16 bank triples f_i(t), K:77–78). t_r=t_u=0. R_E={all 28 triples 000} (the
  argument holds for every R_E). π_NY. π_0(R_E)=8^{−28}. Pullback: 16 BANK and 12 FREE cells (K:54–55, 79–80) ∪ tick-0 port cells (PINNED).
- G2 pass (8^{−28}>0). G3 fails: Pr(eta=z|C=c)=8^{−28} (K:92) and W_0 is a function of C (K:97–98), so P(ready|w)=|R_E|·8^{−28}=π_0(R_E) for every w.
- **Token RR-NOT-READY; deciding gate G3.**
- Beside: (c) not applicable (uniform supplied randomness). Persistence: not applicable. Consumption: 6 boundary keys and 8 bank triples per passive
  step (K:54–58, 77–83); nothing inserted during evolution (K:137–138). FRESH-PACKAGE unresolved. RENEWAL-UNRESOLVED.

## 4. Summary

| E | Token | Deciding gate | Λ (or partial) | W-cert | (a) G2 | (b) G5 | (c) |
|---|---|---|---|---|---|---|---|
| C1 q10 ball | RR-AVAILABLE[H-law, q10-ball pin] | G10 | H-law, q10-ball pin | no | pass | pass (H-law) | none sourced |
| C2 compiled sources | UNRESOLVED(G7:compiled source) | G7 | H-law, SG rows 1–2; rest undecided | no | pass | pass (H-law) | no |
| C3 q8 (chain) | UNRESOLVED(G7:H-access) | G7 | H-law; rest undecided | no | pass | pass (H-law) | pins only |
| C4 whole q9 at L | UNRESOLVED(G7:q10-ball pin) | G7 | H-access; pins undecided | yes | pass | pass (read) | pins only |
| C5 port 5, tick 0 | RR-AVAILABLE[H-access, q10-ball pin] | G10 | H-access, q10-ball pin | yes | pass | pass (read) | pins only |
| C6 banks, 28 keys | RR-NOT-READY | G3 | — | — | pass | not reached | n/a |

No candidate reaches RR-DERIVED (not reachable, PR:64). Both positive tokens keep a pin; neither uses H-sel.

## 5. Invariant → checkpoint (PR §7), as met in this run

| Invariant | How met |
|---|---|
| No computation run | §6 lists read commands only; one key-occurrence listing and one distinct-value listing of SG enter no verdict |
| Rule fixed before assessment | blob `77a471ac` at `c41e0e6f` checked before any row; AMB-0 records the header wording and the unread freeze authorization |
| Every path ends in one token | each of POS-1, NEG-1, CC-2(a), CC-2(b), C1–C6 names one token and its deciding gate (§2–§4) |
| Stop at UNRESOLVED on paper | C2, C3, C4 stop at G7 with the item named; π_0 values are one-line (1/8, 1/4, 1/2, 8^{−28}) or symbolic (8^{−n_E}, \|g(K)\|8^{−n_c}) |
| Joint law, never marginal | every G3 and G6 entry states the conditional law given W or the pushforward of the pinned cone |
| H-law carried when W-cert no | C1 token lists H-law; C2, C3 partial lists keep it |
| Q3 kept out of the verdict | the token column carries no Q3 vocabulary |
| Every token anchored | rows cite `file:line` under §0 at exact SHAs; well over 20 anchors available for sampling |
| Occurs / accessible / preparable separate | G2, G5 with W-certified, and (c) recorded for every E (§3, §4) |
| Single-use not penalized | FRESH-PACKAGE and renewal recorded beside; no token cites them |
| S0 green before tokens | §2 precedes §3 |
| Native A kept separate | no row cites native_v11, native_x_v12 or INTERFACE-CONTRACT:44–54 |
| Preserved results not reopened | kernel `923be23b` used as stated (K:89–98); MR★:1504 limit kept; no §6 item restated with another scope |
| NC-1 only as definition or hypothesis | NC1:57–59 (fixture definition) and NC1:150–152 (H-access) only, each [draft] |
| Scope wording | no added line asserts that a ready supply is excluded, and no premise, prior or access rule is taken on |

## 6. Command log (all read-only; local paths omitted)

1. RR-1 worktree: `git log -1 --format=%H`, `git rev-parse HEAD:<preregistration path>`, `ls`, `wc -l` on the RR-1 directory.
2. `git log -1 --format=%H` in the `d4a80fc8` and `af1e9be2` worktrees and the main checkout; `git cat-file -t 5914c17c` in the main checkout; `ls` of the session directory.
3. `cat -n` / `sed -n` on PR, AS, CI, K, NC1 (1–200), CR, AB, the apparatus-register note, h9, IC, s12 (1–80), P3 (50–120), h10 (1–70), h11 (36–60, 78–92, 140–153),
   r7 (14–24), v15 (55–120), d14 (18–60), r13c (`geometry()`), v15c (377–391, 540–600), SG (head, compact print of rows 1–12),
   the causal-interface probe source (15–66, read as text); MR-pre (36–43, 160–188), MR★ (1342–1372, 1500–1505).
4. `git show 5914c17c:papers/Main.md | sed -n '56p;60p;566p;582p'` in the main checkout.
5. `grep -n` on the files above for line anchors; `grep -o … | sort | uniq -c` listing SG key occurrences; `grep -o … | sort -u` listing SG owner and mask values.
