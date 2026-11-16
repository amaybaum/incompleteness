# KM-1 · The horizon orientation factor at GR:104: which ε, and the minimal correction

**Status.** Paper-only check, not yet independently reviewed. Outcome: on GR:104's own premises the crossing-component density of the de Sitter horizon is $\tfrac32$ per squared lattice spacing (re-verified, node 1). The corpus uses $\epsilon$ in two readings: the calibration chain uses it only as the boundary counting length (area per counted mode), and the statements that carry physical numbers beyond the calibration (lattice spacing, lattice scale, Lorentz-violation amplitude, threshold shift) use it as the lattice spacing. GR:104, GR:98, GR:156 and their mirrors join the two by a factor-one identification that fails by $\sqrt{3/2}$. Recommended: Option B (keep $\epsilon$ as the counting length, define it at GR:98/104, name the lattice spacing $\epsilon_{\rm lat}=\sqrt{3/2}\,\epsilon=\sqrt{6\sigma}\,l_p$ where it is meant): 64 edited lines (48 manuscript lines in 13 files plus 16 mirror lines in the FULL book). Proposals only; no manuscript is edited.

**Authority.** Owner `amaybaum`, recorded in [#1169 comment 6925594215](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6925594215) (posted 2026-11-16 18:40 UTC by `amaybaum`): "Owner `amaybaum`, 2026-11-16, in the coordinating session, said "Let's focus on the items related to the most significant physical claims first". Then, in answer to the ranked proposal "run items 1 and 2 now, in parallel", the owner said "Proceed as suggested"." Item 1 of that comment reads: "**KM-1 (κ_m at GR:104).** Resolve whether the horizon orientation factor is 1 or 3/2. Determine which meaning of ε the corpus uses: the lattice spacing, or the area per counted mode. Propose the minimal correction: either the 3/2 factor propagated, or ε defined at GR:104. The finding comes from #1343, now on main. Output is a proposal only. Any manuscript edit needs a separate owner approval." The same comment lists as not authorized: "manuscript, Lean or registry edits; merges; items 3–5 (P7 coupled shell law, arrow of time, SM reconstruction); the ch18:170 note." and records "A1 stays open and unadopted, and A4 is unchanged. Physical source remains NOT PASSED."

**Source pin.** `main` at `d6f07dc45bc74ad6cc4391dc699765bda24cec23`. `GR:n`, `Main:n`, `SM:n`, `Structure:n`, `Substratum:n` are line `n` of `papers/<name>.md`; `chNN:n` is line `n` of `book/chNN-*.md`; `app-c:n` is line `n` of `book/appendix-c-objections.md`; `FULL:n` is line `n` of `book/The-Incompleteness-of-Observation-FULL.md`.

**References and their role (§A.42 item 8).**

| Reference | Classification |
|---|---|
| #1169 comment 6925594215 | Provenance: the authority quoted above. No claim uses its content. |
| `verification/audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md`, node 4.4 and Open question 4 (landed through #1343) | Support on `main` for the statement of the finding. Every step used here (the line-count identity, the planar density, the sphere average) is re-proved and re-enumerated in node 1. #1343 is provenance only; its content is on `main`. |
| SM:346–366 (§4.5, Lemma 6a, H-link, Theorem 6) | Support on `main` for the status of the single-link reading (hypothesis K2). |

## Question

Which meaning of $\epsilon$ does the maintained corpus use where it matters (the lattice spacing, or the area per counted boundary mode), and what is the minimal correction that leaves no false or contradictory statement once GR:104's "a boundary cell on the horizon has exactly one outward-normal link … $\kappa_m=1$" is replaced by the density that its own premises give?

## 0. Productivity test (fixed before node 1)

The check is productive iff it (i) assigns a reading of $\epsilon$ to every load-bearing site, (ii) identifies an option that leaves no false or contradictory statement with every changed number stated, and (iii) either exposes a consequence of the factor not recorded in P7-B node 4.4 or shows that there is none. A result that only restates "$\kappa_m=\tfrac32$ and the factor can be absorbed into a definition" is recorded as a relabelling. Favourable branches (any branch in which an option appears to need few edits) are pressure-tested in node 6.

## Hypotheses

Statuses: **on main** (cited); **proved here**; **posited**; **open**.

| Id | Hypothesis | Status |
|---|---|---|
| K1 | The coupling graph is the nearest-neighbour simple-cubic lattice, spacing $\epsilon_{\rm lat}$. | On main: SM:222, Main:728 (x). |
| K2 | Single-link reading of H-link: the $K=2d$ components are the $2d$ link directions, component $a$ coupling only across link $\hat e_a$ ($\delta=1$). | On main as GR:104's premise. SM:358 records that the reading in which component $a$ reads only $\mathbf n+\hat e_{j(a)}$ "is not a consequence of §4.4, and the claimed $\delta(2d)=1$ minimization proof is not established"; SM:364 records the single-copy clause $m=1$ as "a named bridge rather than a result". Posited; open. |
| K3 | Counting rule: one counted boundary mode per coupled component whose coupling crosses the partition. | On main as GR:104's counting; posited. |
| K4 | The calibrating horizon is exact de Sitter, a sphere of radius $R=c/H$ in the lattice (comoving) frame; first-law area $A=4\pi R^2$. | On main: GR:56 (exact de Sitter, $A=4\pi c^2/H^2$), GR:88 (H-frame, named condition, open). |
| K5 | The cut is the set of lattice sites inside the sphere. | Posited (as in P7-B node 4.4). Other convex cuts change the average within $[1,\sqrt3]$ (P7-B 4.4, scope (2)). |
| K6 | $R\gg\epsilon_{\rm lat}$. | On main: GR:56 ($\epsilon H/c\sim10^{-61}$). |
| K7 | $\sigma=1$ for quoted numbers. | On main: GR:102, an assumption. |
| K8 | U(1) one-loop coefficient $b_1/2\pi\approx0.65$ ($b_1=41/10$). | On main: SM:693. |
| P1 | Crossing-link count of the lattice ball $=6N_2(R^2)$; ratio to $4\pi R^2\to\tfrac32$. | Proved here (node 1), re-proving P7-B 4.4. |
| P2 | Planar crossing density $(\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert)/\epsilon_{\rm lat}^2$; sphere average $\tfrac32$ for every orientation of the lattice. | Proved here (node 1). |
| P3 | On a lattice ball, most boundary sites have more than one crossing link. | Proved here by enumeration (node 1). |
| P4 | Under K1–K6: $\epsilon^2=\tfrac23\epsilon_{\rm lat}^2$ for the counting length; $\epsilon_{\rm lat}=\sqrt{6\sigma}\,l_p$; Lorentz-violation amplitude $2\sigma/15$; threshold $\delta_0\approx10.60$; $G_{\rm eff}(\mathbf n)=3G/(2\lvert\mathbf n\rvert_1)$. | Proved here (exact algebra, nodes 3–4). |

## 1. Re-verification of the factor

**1.1 Line-count identity.** Let $V_R=\{x\in\mathbb Z^3:\lvert x\rvert^2\le R^2\}$ (units $\epsilon_{\rm lat}=1$). For a direction $e_j$ and a lattice line $\ell\parallel e_j$ with transverse coordinates $(y,z)$, $\ell\cap V_R$ is a run of consecutive points (convexity), nonempty iff $y^2+z^2\le R^2$, and a nonempty run has exactly two boundary-crossing edges. Summing over three directions, the cut has $6N_2(R^2)$ edges, $N_2(R^2)=\#\{(y,z)\in\mathbb Z^2:y^2+z^2\le R^2\}=\pi R^2+O(R)$, hence $6\pi R^2+O(R)=\tfrac32\cdot4\pi R^2+O(R)$. The argument holds for any centre of the ball.

**1.2 Planar density.** The $e_j$-links crossing a plane with unit normal $\mathbf n$ are those whose start lies in a slab of thickness $\lvert n_j\rvert$, so the crossing density per unit area is $\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert=\lvert\mathbf n\rvert_1\in[1,\sqrt3]$. Over a sphere, $\frac1{4\pi}\int\lvert\mathbf n\cdot e_j\rvert\,d\Omega=\frac{2\pi}{4\pi}\int_0^\pi\lvert\cos\theta\rvert\sin\theta\,d\theta=\tfrac12$ for every unit vector $e_j$, so the average is $\tfrac32$ whatever the orientation of the lattice relative to the sphere.

**1.3 Enumeration (integer arithmetic; floating point only in the printed ratios).** Script:

```python
import math
from collections import Counter
STEPS = ((1,0,0), (0,1,0), (0,0,1))
NBRS = STEPS + ((-1,0,0), (0,-1,0), (0,0,-1))

def cut_edges(inside, lo, hi):
    # nearest-neighbour edges of Z^3 with exactly one endpoint in the set
    n = 0
    for x in range(lo, hi):
        for y in range(lo, hi):
            for z in range(lo, hi):
                a = inside(x, y, z)
                for dx, dy, dz in STEPS:
                    if a != inside(x+dx, y+dy, z+dz):
                        n += 1
    return n

def isqrt_ceil(R2):
    r = 0
    while r*r <= R2:
        r += 1
    return r

def n2(R2):
    r = isqrt_ceil(R2)
    return sum(1 for y in range(-r, r+1) for z in range(-r, r+1) if y*y + z*z <= R2)

for L in (3, 7, 12):                      # control: axis-aligned cube, expect 6 L^2
    c = cut_edges(lambda x, y, z: 0 <= x < L and 0 <= y < L and 0 <= z < L, -1, L+1)
    print("cube", L, c, c == 6*L*L)

for R2 in (100, 400, 1600):               # ball: expect 6 N2(R^2), ratio to 4 pi R^2 -> 3/2
    r = isqrt_ceil(R2)
    c = cut_edges(lambda x, y, z: x*x + y*y + z*z <= R2, -r-1, r+2)
    print("ball", R2, c, c == 6*n2(R2), round(c/(4*math.pi*R2), 4))

def plane(m, R):
    # e_j-links crossing the plane m.x = 1/2 with start inside a cylinder of radius R about the normal
    mm = sum(t*t for t in m)
    lim = R + 3*max(abs(t) for t in m)
    n = 0
    for x in range(-lim, lim+1):
        for y in range(-lim, lim+1):
            for z in range(-lim, lim+1):
                d = m[0]*x + m[1]*y + m[2]*z
                if mm*(x*x + y*y + z*z) - d*d > R*R*mm:
                    continue
                for j in range(3):
                    if (d <= 0) != (d + m[j] <= 0):
                        n += 1
    return n

for m in ((0,0,1), (1,1,0), (1,1,1), (1,2,3)):   # density per unit area vs |n|_1
    c = plane(m, 40)
    print("plane", m, c, round(c/(math.pi*1600), 4),
          round(sum(abs(t) for t in m)/math.sqrt(sum(t*t for t in m)), 4))

R2, r = 400, 21                            # crossing links per boundary site of the ball
inside = lambda x, y, z: x*x + y*y + z*z <= R2
hist = Counter()
for x in range(-r, r+1):
    for y in range(-r, r+1):
        for z in range(-r, r+1):
            if inside(x, y, z):
                k = sum(1 for d in NBRS if not inside(x+d[0], y+d[1], z+d[2]))
                if k:
                    hist[k] += 1
print("per-site", sorted(hist.items()), sum(k*v for k, v in hist.items()))
```

Run with `python3 -I` (standard library only, about two seconds). Expected output:

```
cube 3 54 True
cube 7 294 True
cube 12 864 True
ball 100 1902 True 1.5136
ball 400 7542 True 1.5004
ball 1600 30150 True 1.4995
plane (0, 0, 1) 5025 0.9997 1.0
plane (1, 1, 0) 7090 1.4105 1.4142
plane (1, 1, 1) 8715 1.7338 1.7321
plane (1, 2, 3) 8059 1.6033 1.6036
per-site [(1, 1728), (2, 1116), (3, 1152), (4, 24), (5, 6)] 7542
```

Controls: the axis-aligned cube gives exactly one crossing link per unit area ($6L^2$), so the counter does not inflate the count; the axis-normal plane gives $1.0$ to within the boundary error of the disc. The ball counts equal $6N_2(R^2)$ exactly, so the identity, not the ratio, carries the claim. The tilted planes reproduce $\lvert\mathbf n\rvert_1$ ($\sqrt2$, $\sqrt3$, $6/\sqrt{14}$) to the disc-boundary error. The per-site histogram for $R^2=400$: of 4026 boundary sites, 1728 have one crossing link and 2298 have two to five.

**Verdict, node 1.** Confirmed: under K1–K6, $\kappa_m=\tfrac32$ in GR:104's notation $\eta=\kappa_m\sigma/\epsilon^2$ with $\epsilon$ the lattice spacing. GR:104's sentence "A boundary cell on the horizon has exactly one outward-normal link crossing the partition" is false per cell as well as on average (P3: 57% of boundary sites of the $R^2=400$ ball have more than one). Classification: CONFIRMING for P1–P2 (P7-B 4.4); ELABORATING for P3.

## 2. Which $\epsilon$ the corpus uses

**2.1 What the calibration chain needs.** In every derivation of the calibration (GR:58, :74–80, :98–102, :140–150, :302–316; ch07:40–55, :73–76, :92–96; appendix-b:202–214) $\epsilon$ enters only through the mode density $\eta=\sigma/\epsilon^2$, i.e. as the counting length: $\epsilon^2=A/N_{\rm modes}$. The results $\hbar=c^3\epsilon^2/(4G\sigma)$, $\epsilon^2=4\sigma l_p^2$, $N_{\rm modes}=A/\epsilon^2=S/\sigma$ and $S=A/(4l_p^2)$ are exact algebra in that reading and do not depend on $\kappa_m$.

**2.2 Where the lattice reading is used.** The following statements use $\epsilon$ as the lattice spacing (cell edge, link length, dispersion parameter, lattice scale), with the value $2\sqrt\sigma\,l_p$ imported from the calibration: the Lorentz-violation dispersion $\omega^2=k^2[1-(k\epsilon)^2/45]$ and its amplitude $4\sigma/45$ (Substratum:482–484, SM:226, :232, :1448, ch04:128); the lattice scale $1/\epsilon=M_{\rm Pl}/(2\sqrt\sigma)$ and the threshold shift $0.65\ln(2\sqrt\sigma)$, $\delta_0\approx10.47$ (SM:693, :711, :1128, :1560, :1562, Structure:1068, :1078, ch06:82); the spacing, range and cell statements (SM:222, :545, :563, :1271, :1448, Structure:789, Substratum:225, :227, :552, ch05:171, ch07:78, ch09:324, ch18:22, :144, :226, ch19:28, app-c:259); Lemma 1's minimal cell (ch01:30–32).

**2.3 Bridge sites.** GR:98 ("$\epsilon$ is defined as the minimal distinguishable scale, so each cell of area $\epsilon^2$ contributes exactly one boundary mode"), GR:104 (one normal link per boundary cell), GR:156 ("one boundary mode per cell of area $\epsilon^2$ is what 'minimal' means"), GR:316 and ch07:40, :94 ("each minimal cell of area $\epsilon^2$"), ch07:59 (mirror of GR:104/156), Substratum:536 ("a count forced by the link-direction structure"), and S3 at GR:665 ("a finite discreteness scale $\epsilon$ that admits identification with the boundary's mode-counting unit") assert that the two readings coincide.

**Verdict, node 2.** The corpus uses both readings and identifies them at the bridge sites. Where it matters numerically: the calibration and the area law use only the counting reading and are unaffected; every statement whose number changes uses the lattice reading. Under K1–K6 the identification fails by $\epsilon_{\rm lat}^2=\tfrac32\epsilon^2$. Classification: NEW relative to P7-B 4.4, whose scope (1) records that under GR:156's reading the factor "moves into the relation between $\epsilon$ and the lattice spacing" without tracing that the lattice-spacing statements carry physical numbers (amplitude, lattice scale, threshold) that change under every option.

### Site inventory

Columns: reading of $\epsilon$ (C = counting length, L = lattice spacing, B = bridge asserting both, N = nominal or order-of-magnitude use, unaffected by an $O(1)$ factor); whether the statement's truth changes under A and B. FULL mirrors of the book lines are listed in node 5.

**(i) Sites that change under both options (L and B).**

| Site | Quote | Reading | A | B |
|---|---|---|---|---|
| GR:98 | "ε is defined as the minimal distinguishable scale, so each cell of area ε² contributes exactly one boundary mode" | B | false; edit | false; edit |
| GR:104 | "exactly one outward-normal link … κ_m = 1 … ε = 2 l_p at σ = 1" | B | false; edit | false; edit |
| GR:156 | "one boundary mode per cell of area ε² is what 'minimal' means" | B | false; edit | false justification; edit |
| GR:160 | "The two are consistent … recovers G_eff = G" | C, local | patch scope; edit | patch scope; edit |
| GR:326 | "a lattice-regularized QFT with UV cutoff at ε = 2√σ l_p" | L | false; edit | false; edit |
| GR:316 | "each minimal cell of area ε² = 4σ l_p²" | B | false; edit | false; edit |
| GR:665 | S3 "discreteness scale ε that admits identification with the boundary's mode-counting unit" | B | edit (identification fails) | edit (restate) |
| GR:669 | "nor its identification with the boundary mode-counting unit, which S3 requires" | B | edit | edit (follows S3) |
| GR:697 | "one boundary-crossing component per cell, A/ε² = S_BH/σ modes" | B | false; edit | false; edit |
| GR:749 | Corollary A.4 "with the same entropy σ per boundary mode … same ħ" | C | needs equal κ_m; edit | needs equal ε; edit |
| SM:222 | "microscopic spacing ε=2√σ l_p" | L | false; edit | false; edit |
| SM:226, :232 | "coefficient 4σ/45 … (4/45 at σ = 1)"; "including the 4σ/45 coefficient" | L | false; edit | false; edit |
| SM:545 | "χ(y + ηε)" | L | true | symbol; edit |
| SM:563 | "range exactly ε" | L | true | symbol; edit |
| SM:693 | "lattice scale is 1/ε = M_Pl/(2√σ) … ln(2√σ) … δ_0 ≈ 10.47" | L | false; edit | false; edit |
| SM:711 | "moves δ_0 by 0.65 ln(2√σ), to δ_0 ≈ 10.47" | L | false; edit | false; edit |
| SM:1128, :1560, :1562 | "lattice scale/cutoff 1/ε = M_Pl/(2√σ)" | L | false; edit | false; edit |
| SM:1271 | "cubic lattice with spacing ε = 2√σ l_P" | L | false; edit | false; edit |
| SM:1448 | "spacing ε = 2√σ l_p … (kε)²/45 … 4σ/45 = 4/45" | L | false; edit | false; edit |
| Structure:789 | "lattice spacing ε = 2√σ l_p" | L | false; edit | false; edit |
| Structure:1068, :1078 | "the lattice scale M_Pl/(2√σ)" | L | false; edit | false; edit |
| Substratum:225, :227 | "(Eε/ħc)² = 4σ(E/M_Pl)²" | L | false; edit | false; edit |
| Substratum:482–484 | "(kε)² … 4σ/45 … ε = 2√σ l_p and kε = 2√σ E/M_Pl … 4/45" | L | false; edit | false; edit |
| Substratum:536 | "one mode per ε² cell … a count forced by the link-direction structure" | B | false; edit | false; edit |
| Substratum:552 | "the lattice spacing ε = 2√σ l_p" | L | false; edit | false; edit |
| ch01:32 | "self-consistency ties ε to the Planck length, ε = 2ℓ_P" (ε = Lemma 1's minimal cell) | L | false; edit | false; edit |
| ch04:128 | "orientation-averaged coefficient is 4/45 … (4σ/45 …)" | L | false; edit | false; edit |
| ch05:171 | "range exactly ε = 2√σ ℓ_P" | L | false; edit | false; edit |
| ch06:82 | "the lattice scale itself being 1/ε = M_Pl/(2√σ)" | L | false; edit | false; edit |
| ch07:40 | "each minimal cell of area ε² contributes one boundary mode" | B | false; edit | false; edit |
| ch07:59 | "a boundary cell has exactly one outward-normal link … forced by the link-direction structure" | B | false; edit | false; edit |
| ch07:65 | mirror of GR:160 | C, local | edit | edit |
| ch07:78 | "partition cell has linear extent 2√σ l_p" | L | false; edit | false; edit |
| ch07:94 | "Each minimal cell of area ε² = 4σ l_p²" | B | false; edit | false; edit |
| ch07:173 | "With the framework's UV cutoff at ε = 2√σ l_p … 1/ε = M_Pl/(2√σ)" | L | false; edit | false; edit |
| ch09:324 | "cubic lattice at ε = 2√σ l_p" | L | false; edit | false; edit |
| ch18:22, :144, :226 | "cubic lattice at ε = 2√σ l_p"; "the lattice spacing ε = 2√σ l_p"; "cubic lattice at discreteness scale ε" | L | false; edit | false; edit |
| ch19:28 | "The lattice at ε = 2√σ l_p" | L | false; edit | false; edit |
| app-c:259 | "the framework's substratum is a lattice at ε = 2√σ l_p" | L | false; edit | false; edit |

**(ii) Sites in the counting reading: true as written under B, false under A.** Each states $\hbar=c^3\epsilon^2/(4G\sigma)$, $\epsilon=2\sqrt\sigma\,l_p$ (or $2l_p$, $\epsilon/\sqrt\sigma=2l_p$, $\epsilon^2=4\sigma l_p^2$), $T_{\rm cl}=c^2\epsilon^2\kappa/(8\pi Gk_B\sigma)$, $\eta=\sigma/\epsilon^2$, $S=\sigma A/\epsilon^2$ or $N_{\rm modes}=A/\epsilon^2=S/\sigma$, with $\epsilon$ named "the discreteness scale" where it is named at all.

| File | Lines |
|---|---|
| GR | 12, 24, 28, 30, 32, 42, 58, 74, 78, 80, 100, 102, 140, 144, 146, 150, 158, 162, 302, 304, 306, 312, 314, 354, 362, 378, 422, 424, 426, 430, 547, 565, 611, 617, 619, 625, 627, 649, 651, 653, 685, 695, 701, 751 |
| SM | 30, 46, 90, 166, 547, 1366, 1394, 1592 |
| Structure | 47, 467 |
| Substratum | 22, 117, 179, 189, 191, 193, 195, 375, 529 |
| Methodology | 339 |
| ch00 | 97 |
| ch02 | 88, 111, 112, 118, 190, 226 |
| ch04 | 204 |
| ch05 | 41 |
| ch06 | 348 |
| ch07 | 12, 14, 16, 36, 41, 53, 55, 61, 63, 71, 73, 74, 76, 82, 86, 90, 92, 93, 96, 193, 251, 252, 254, 305, 307 |
| ch09 | 14, 48, 71, 88, 92 |
| ch12 | 197 |
| ch18 | 146, 158 |
| appendix-a | 117 |
| appendix-b | 16, 169, 196, 202, 203, 211, 214 |
| app-c | 122, 126, 248 |
| glossary | 73 |
| book/README | 98 |

Together with their FULL mirrors: about 120 manuscript lines and 55 FULL lines. GR:362 and ch07:193 quote the mode sum "cut off at $1/\epsilon$" as one of several conventions (ch07:193: "the identification holds up to a convention-dependent numerical factor"), with exact arithmetic for that cutoff. Under A each of these changes ($4G\sigma\to6G\sigma$, $2\sqrt\sigma\to\sqrt{6\sigma}$, $4\sigma l_p^2\to6\sigma l_p^2$, $8\pi G\sigma\to12\pi G\sigma$ in $T_{\rm cl}$, $\sigma/\epsilon^2\to\tfrac32\sigma/\epsilon^2$, $A/\epsilon^2\to\tfrac32A/\epsilon^2$). Under B none changes. GR:619, appendix-b:202 and app-c:126 say "cell of area $\epsilon^2$" or "boundary cell count" without "minimal": under B they read as the counting cell that GR:98 defines.

**(iii) Nominal or order-of-magnitude uses, unaffected under both options.** GR:56 and GR:160 ($O((\epsilon H/c)^2)\sim10^{-122}$), GR:50, GR:90, Main:76, ch01:65 ($A/\epsilon^2\sim10^{122}$), GR:332 ("UV cutoff at $\epsilon^{-1}$"), SM:130, :134, :140–164, :539, :549, :1396 (scalings in $\epsilon$), SM:547 and ch09:254 ("the fundamental scale"), ch18:256 ("at scales of $\epsilon$"), app-c:259's $(\epsilon\kappa/c^2)^2\sim10^{-122}$, appendix-a:113 ($O((k\epsilon)^2)$). A factor $\sqrt{3/2}$ leaves each true.

Not in the manuscript surface and not edited: `verification/programmes/physical-realization/w1-1-20261112/DELTA-REVIEW-W1-1-r3.md:124` ("GR:104 has κ_m = 1, so N_B is unchanged") and `verification/audits/manuscript/corpus-consistency-20261026/AUDIT.md:94,101,116` cite GR:104's $\kappa_m$; the Lean module `OIBridge.lean` (the `faceToLink` map, line 620) identifies the six cube faces with the six links and does not count horizon crossings. These are listed for the reviewer; no claim here depends on them.

## 3. The three options

**3.1 Option A: $\epsilon$ is the lattice spacing; $\kappa_m=\tfrac32$ propagated.** One meaning of $\epsilon$ corpus-wide (consistent with Main's Lemma 1 cell and with every site of 2.2). Replacement rules, applied to every site of inventory (i) and (ii) and their FULL mirrors:

| Current | Option A |
|---|---|
| $\eta=\sigma/\epsilon^2$, $dS=\sigma\,dA/\epsilon^2$, $S=\sigma A/\epsilon^2$ | $\eta=\tfrac32\sigma/\epsilon^2$, $dS=\tfrac32\sigma\,dA/\epsilon^2$, $S=\tfrac32\sigma A/\epsilon^2$ |
| $k_BT_{\rm cl}=c^2\epsilon^2\kappa/(8\pi G\sigma)$; $c^3\epsilon^2H/(8\pi G\sigma)$ | $c^2\epsilon^2\kappa/(12\pi G\sigma)$; $c^3\epsilon^2H/(12\pi G\sigma)$ |
| $\hbar=c^3\epsilon^2/(4G\sigma)$ | $\hbar=c^3\epsilon^2/(6G\sigma)$ |
| $\epsilon=2\sqrt\sigma\,l_p$; $\epsilon=2l_p$ ("twice the Planck length"); $\epsilon/\sqrt\sigma=2l_p$; $\epsilon^2=4\sigma l_p^2$ | $\epsilon=\sqrt{6\sigma}\,l_p$; $\epsilon=\sqrt6\,l_p\approx2.45\,l_p$; $\epsilon/\sqrt\sigma=\sqrt6\,l_p$; $\epsilon^2=6\sigma l_p^2$ |
| $N_{\rm modes}=A/\epsilon^2=A/(4\sigma l_p^2)$ | $N_{\rm modes}=\tfrac32A/\epsilon^2=A/(4\sigma l_p^2)$ |
| $1/\epsilon=M_{\rm Pl}/(2\sqrt\sigma)$; $\ln(2\sqrt\sigma)$; $\delta_0\approx10.47$ | $M_{\rm Pl}/\sqrt{6\sigma}$; $\ln\sqrt{6\sigma}$; $\delta_0\approx10.60$ |
| $4\sigma/45$, $4/45$; $(E\epsilon/\hbar c)^2=4\sigma(E/M_{\rm Pl})^2$ | $2\sigma/15$, $2/15$; $6\sigma(E/M_{\rm Pl})^2$ |
| GR:316, ch07:96: "the factor of 4 in $\epsilon^2=4\sigma l_p^2$ traces to $2\pi/8\pi$" | "the factor 6 in $\epsilon^2=6\sigma l_p^2$ is $4\kappa_m$: the 4 from $2\pi/8\pi$, the $\tfrac32$ from the link density" |

Plus the bridge rewrites of 3.2 with $\epsilon$ in place of $\epsilon_{\rm lat}$. Edited lines: up to 165 manuscript lines in 23 files (inventory (i) and (ii)) plus 73 FULL lines, about 238. The orientation dependence must be stated under A as under B (3.4). Drawback beyond count: the premise-dependent factor $\tfrac32$ (K2, K3, K5) enters every quotation of the calibration, so any change of the open single-link reading (for example the isotropic internal matrix of SM:356, under which every component of a boundary site reads every neighbour) would change all of them again.

**3.2 Option B: $\epsilon$ is the counting length; the lattice spacing is named where meant.** GR:98 defines $\epsilon$ by $\epsilon^2=A/N_{\rm modes}$ (GR:156's reading); GR:104 derives $\epsilon^2=\tfrac23\epsilon_{\rm lat}^2$ under K1–K6; S3 is restated to require that the substratum fix the counting length. All inventory (ii) sites stay true. Does B force edits at the sites using $\epsilon$ as the lattice spacing? Yes: with $\epsilon$ the counting length, each statement of inventory (i) marked L asserts the lattice spacing (or lattice scale, range, cell, dispersion parameter) equal to $2\sqrt\sigma\,l_p$ and is false by $\sqrt{3/2}$; left unedited, they contradict GR:104 as corrected. They take the symbol $\epsilon_{\rm lat}$ (formulas, SM, Substratum) or the value $\sqrt{6\sigma}\,l_p$ in words (book). The symbol $a$ is not available: GR uses $a(t)$ for the scale factor (GR:56) and $a$ for the component index (GR:104). Sites that use $\epsilon$ only as a scale (inventory (iii)) need no edit. Edited lines: 48 manuscript lines in 13 files plus 16 FULL lines, 64 in all (node 5).

**3.3 Option C: a reading under which GR:104 is correct as written.** Candidate: count per face of the lattice-adapted (staircase) boundary. Each boundary plaquette is crossed by exactly one link, so the density per staircase area is $1/\epsilon_{\rm lat}^2$. But the staircase area of the ball is $6N_2\,\epsilon_{\rm lat}^2\approx\tfrac32A$, and the area in the first law and in $S=\eta A$ is the geometric area $A=4\pi R^2$ of the de Sitter horizon (GR:56, :58, :98; K4), a fixed sphere in the comoving frame under H-frame (GR:88). Per geometric area the density stays $\tfrac32/\epsilon_{\rm lat}^2$, and per boundary site it is not one (P3). A cut aligned with lattice planes (cube) gives one per unit area but is not the de Sitter horizon. No reading of GR:56's horizon makes GR:104's sentence true. Option C: none.

**3.4 The orientation dependence (both options).** Under K1–K3 a local planar horizon patch with unit normal $\mathbf n$ has $\eta(\mathbf n)=\sigma\lvert\mathbf n\rvert_1/\epsilon_{\rm lat}^2$. With $\hbar$ calibrated on the sphere ($\bar\eta=\tfrac32\sigma/\epsilon_{\rm lat}^2=\sigma/\epsilon^2$), Jacobson's relation gives $G_{\rm eff}(\mathbf n)=c^3/(4\eta(\mathbf n)\hbar)=3G/(2\lvert\mathbf n\rvert_1)$, from $\tfrac32G$ (axis-normal) to $\tfrac{\sqrt3}{2}G\approx0.87G$ (body-diagonal-normal), and the classical patch temperature $c^2\kappa/(8\pi G\eta(\mathbf n)k_B)$ differs from the KMS temperature $\hbar\kappa/(2\pi ck_B)$ by the factor $\tfrac32/\lvert\mathbf n\rvert_1$. GR:160 (and ch07:65) states consistency with Jacobson's local relation without scope; Corollary A.4 (GR:749) asserts one $\hbar$ for any two horizons with the same $\sigma$, which under K1–K3 holds when the two horizons have the same area average of $\lvert\mathbf n\rvert_1$ (for example two spheres in the lattice frame), not for horizons of other shapes. Both statements require a scope clause under either option; GR:42 concerns de Sitter observers, whose horizons are spheres, and needs none under H-frame. Decision: the dependence must be stated, once at GR:104 where the count is derived, with scope clauses at GR:160, ch07:65 and GR:749. Classification: ELABORATING for $G_{\rm eff}(\mathbf n)$ (P7-B Open question 4); NEW for the temperature mismatch on tilted patches and for Corollary A.4's shape condition.

**Verdict, node 3.** A and B each leave no false statement when fully applied; C does not exist. B's edit set is contained in A's: every B edit is an A edit of the same passage, and A adds the about 175 lines of inventory (ii) with mirrors.

## 4. Changed numerical claims (both options)

| Quantity | Current | Corrected (under K1–K7) |
|---|---|---|
| Lattice spacing | $2\sqrt\sigma\,l_p$ ($2l_p$) | $\sqrt{6\sigma}\,l_p$ ($\sqrt6\,l_p\approx2.449\,l_p$) |
| Lattice scale | $M_{\rm Pl}/(2\sqrt\sigma)$ | $M_{\rm Pl}/\sqrt{6\sigma}$ |
| Quadratic Lorentz-violation amplitude ($\omega^2=k^2[1-c_2(E/M_{\rm Pl})^2]$) | $4\sigma/45\approx0.089\sigma$ | $(k\epsilon_{\rm lat})^2/45=6\sigma/45=2\sigma/15\approx0.133\sigma$ |
| Lattice–continuum suppression | $4\sigma(E/M_{\rm Pl})^2$ | $6\sigma(E/M_{\rm Pl})^2$ (still $\sim10^{-32}$ at LHC energies) |
| U(1) threshold if matched at the lattice scale | $10.02+0.65\ln(2\sqrt\sigma)\approx10.47$ | $10.02+0.65\ln\sqrt{6\sigma}\approx10.60$ ($0.6525\cdot\ln\sqrt6=0.585$) |
| $\kappa_m$ (GR:104 notation, $\epsilon$ = lattice spacing) | $1$ | $\tfrac32$ |

Unchanged: $\hbar=c^3\epsilon^2/(4G\sigma)$ and $\epsilon=2\sqrt\sigma\,l_p$ for the counting length; $S=A/(4l_p^2)$; $N_{\rm modes}=S/\sigma$; every order-of-magnitude statement of inventory (iii). The $\tfrac1{45}$ lattice coefficient of $(k\epsilon_{\rm lat})^2$, $\langle\delta\rangle=\tfrac1{90}$ and the directional ratios $4:1:0$ are in lattice units and unchanged. These values hold on the single-link reading (K2), which is open; the current values rest on the same reading.

## 5. Recommendation and proposed text

**Recommendation: Option B.** Correctness first: both A and B can be made fully consistent, C does not exist. B is preferred because (1) it keeps every statement whose derivation is exact and premise-free in the counting reading (inventory (ii), about 120 lines plus 55 FULL mirrors) unchanged and true; (2) the statements it edits are exactly those whose numbers change under any option, plus the bridge sites; (3) it confines the premise-dependent factor (K2, K3, K5) to one derivation (GR:104) and to the lattice-spacing values, so a later change in the single-link reading touches only those sites; (4) its edit set is a strict subset of A's. B's cost is a second symbol, $\epsilon_{\rm lat}$, and S3's restatement as "the substratum fixes the counting length" rather than "is identified with" it; Main's Lemma 1 is unaffected (Main fixes no value of its $\epsilon$, and Main:222 says only "of the order of the Planck length"). Edited lines under B: 64 (GR 10, SM 12, Structure 3, Substratum 7, book chapters 16, FULL 16).

Proposed text, Option B. In each row the current text is an exact fragment of the line; text outside the fragment is unchanged.

| Site | Current text | Proposed text | Reason |
|---|---|---|---|
| GR:98 | The entropy density is $\eta = \sigma/\epsilon^2$ — one coupled mode per minimal cell, each carrying the dimensionless entropy $\sigma$, in nats. The count rests on Lemma 1: $\epsilon$ is defined as the minimal distinguishable scale, so each cell of area $\epsilon^2$ contributes exactly one boundary mode that couples across the partition. | The entropy density is $\eta = \sigma/\epsilon^2$, where $\epsilon$, the discreteness scale of the boundary count, is defined by $\epsilon^2 = A/N_{\rm modes}$: the horizon area per boundary mode that couples across the partition, each mode carrying the dimensionless entropy $\sigma$, in nats. Its relation to the lattice spacing $\epsilon_{\rm lat}$ is fixed by the link count below. | Definition (B); the minimal-cell argument is false under K1–K6 (node 1). |
| GR:104 | Whole paragraph, from "*Reconciliation with the internal component count.* The counting $\eta = \sigma/\epsilon^2$ is one boundary mode per cell" to "where the link-direction structure fixes it at unity." | *Reconciliation with the internal component count.* The counting $\eta = \sigma/\epsilon^2$ is one boundary mode per area $\epsilon^2$, whereas the substratum carries $K = 2d = 6$ internal components per site ([SM §4.5]). Under H-link with the single-link reading — component $a$ assigned to link direction $\hat e_a \in \{\pm\hat e_1, \ldots, \pm\hat e_d\}$ and coupling only across that one link (the factorization $\delta = 1$, which [SM §4.5, Lemma 6a] records as not a consequence of [SM §4.4]) — the components whose coupling crosses the horizon are one per nearest-neighbour link crossing it. On the cubic lattice of spacing $\epsilon_{\rm lat}$ a planar patch with unit normal $\mathbf n$ is crossed by $(\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert)/\epsilon_{\rm lat}^2$ links per unit area: $1/\epsilon_{\rm lat}^2$ for a patch orthogonal to a lattice axis, $\sqrt3/\epsilon_{\rm lat}^2$ for one orthogonal to a body diagonal. For the de Sitter horizon, a sphere of radius $R \gg \epsilon_{\rm lat}$ in the lattice frame with the sites inside it on the visible side, the area average of $\lvert n_j\rvert$ is $\tfrac12$ for every orientation of the lattice, and the number of crossing links is exactly $6N_2(R^2/\epsilon_{\rm lat}^2)$, with $N_2(r^2)$ the number of integer points in a disc of radius $r$, that is $\tfrac32 A/\epsilon_{\rm lat}^2 + O(R/\epsilon_{\rm lat})$. Writing $\eta = \kappa_m\sigma/\epsilon_{\rm lat}^2$, the spherical horizon has $\kappa_m = \tfrac32$ and $\epsilon^2 = \epsilon_{\rm lat}^2/\kappa_m = \tfrac23\epsilon_{\rm lat}^2$. The Bekenstein-Hawking coefficient is independent of $\kappa_m$: the gap equation gives $\hbar = c^3/(4G\eta)$ and $S = \eta A = A/(4l_p^2)$ with $\kappa_m$ and $\sigma$ cancelling, and the mode count is $N_{\rm modes} = A/\epsilon^2 = S/\sigma$. The component count enters only the lattice spacing: with $\epsilon = 2\sqrt{\sigma}\,l_p$ (§4), $\epsilon_{\rm lat} = 2\sqrt{\kappa_m\sigma}\,l_p = \sqrt{6\sigma}\,l_p$, which is $\sqrt6\,l_p \approx 2.45\,l_p$ at $\sigma = 1$. The density depends on orientation: a local patch with normal $\mathbf n$ has $\eta(\mathbf n) = \sigma(\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert)/\epsilon_{\rm lat}^2$, equal to the spherical value $\sigma/\epsilon^2$ only where $\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert = \tfrac32$; whether the emergent description carries an orientation-independent density is open. (The entropy per mode, $\sigma$, is a separate question: one mode per area $\epsilon^2$ does not establish one nat per mode.) The matching scale $\mu = M_{\text{Pl}}$ of [SM §6.2] is a convention into which this factor does not enter; matching at $1/\epsilon_{\rm lat}$ instead shifts the fitted threshold parameters there ([SM §6.2]). | Root finding (node 1); single-link premise stated with its status (K2); orientation dependence (3.4). |
| GR:156 | **The counting of one mode per cell is definitional.** Given that $\epsilon$ is the minimal distinguishable scale (Lemma 1), "one boundary mode per cell of area $\epsilon^2$" is what "minimal" means: a cell finer than $\epsilon$ would subdivide the minimal scale, while counting fewer modes would require a distinction below $\epsilon$ to group them. | **The counting of one mode per area $\epsilon^2$ is definitional.** With $\epsilon$ defined by $\epsilon^2 = A/N_{\rm modes}$ (§3.1), "one boundary mode per area $\epsilon^2$" is its definition; the substratum enters through the relation of $\epsilon$ to the lattice spacing, $\epsilon^2 = \tfrac23\epsilon_{\rm lat}^2$ on the spherical horizon under the single-link reading (§3.1). | The minimality argument identifies $\epsilon$ with the lattice cell; false under K1–K6. |
| GR:160 | The two are consistent — substituting $\eta = \sigma/\epsilon^2$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ into Jacobson's relation $G_{\text{eff}} = c^3/(4\eta\hbar)$ recovers $G_{\text{eff}} = G$, with $\sigma$ cancelling — but the roles of input and output are reversed. | The two are consistent on the spherical horizon — substituting $\eta = \sigma/\epsilon^2$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ into Jacobson's relation $G_{\text{eff}} = c^3/(4\eta\hbar)$ recovers $G_{\text{eff}} = G$, with $\sigma$ cancelling — but the roles of input and output are reversed. On a planar patch with unit normal $\mathbf n$ the single-link density of §3.1 gives $G_{\text{eff}}(\mathbf n) = 3G/\big(2(\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert)\big)$, between $\tfrac{\sqrt3}{2}G$ and $\tfrac32G$, so the agreement holds for the spherical average and not patch by patch. | 3.4. |
| GR:316 | each minimal cell of area $\epsilon^2 = 4\sigma\,l_p^2$ on the horizon contributes the entropy $\sigma$ of one boundary mode | each area $\epsilon^2 = 4\sigma\,l_p^2$ of the horizon carries one boundary mode of entropy $\sigma$ | Bridge wording (2.3). |
| GR:326 | a lattice-regularized QFT with UV cutoff at $\epsilon = 2\sqrt{\sigma}\,l_p$. | a lattice-regularized QFT with UV cutoff at the lattice spacing $\epsilon_{\rm lat} = \sqrt{6\sigma}\,l_p$ (§3.1). | Lattice reading; value. |
| GR:665 | (*S3*) *Finite discreteness.* The substratum has a finite discreteness scale $\epsilon$ that admits identification with the boundary's mode-counting unit. [Main §1.2]'s Lemma 1 establishes a finite visible configuration space with a finite discreteness scale $\epsilon$; here we additionally require that the discreteness scale appears in the boundary mode count. | (*S3*) *Finite discreteness.* The substratum fixes a finite discreteness scale $\epsilon$ of the boundary count, the horizon area per counted mode being $\epsilon^2$. [Main §1.2]'s Lemma 1 establishes a finite visible configuration space with a finite discreteness scale; here we additionally require that the substratum fix the boundary mode count. For OI's cubic lattice under the single-link reading, $\epsilon^2 = \tfrac23\epsilon_{\rm lat}^2$ on a spherical horizon (§3.1). | Identification fails by $\sqrt{3/2}$ (node 1). |
| GR:669 | supplies neither the discreteness scale $\epsilon$ nor its identification with the boundary mode-counting unit, which S3 requires | supplies neither the discreteness scale $\epsilon$ of the boundary count nor its relation to the substratum's lattice structure, which S3 requires | Follows S3. |
| GR:697 | one boundary-crossing component per cell, $A/\epsilon^2 = S_{\rm BH}/\sigma$ modes | boundary-crossing components at the link density of §3.1, $A/\epsilon^2 = S_{\rm BH}/\sigma$ modes | Bridge (one per cell is false under K1–K6). |
| GR:749 | with the same entropy $\sigma$ per boundary mode, both procedures yield | with the same entropy $\sigma$ per boundary mode and the same discreteness scale $\epsilon$ of the boundary count at each horizon (under the single-link reading of §3.1, the same for horizons that are spheres in the lattice frame), both procedures yield | 3.4. |
| SM:222 | with microscopic spacing $\epsilon=2\sqrt{\sigma}\,l_p$. | with microscopic spacing $\epsilon_{\rm lat}=\sqrt{6\sigma}\,l_p$, $\sqrt{3/2}$ times the boundary counting length $\epsilon=2\sqrt{\sigma}\,l_p$ of [GR §3.1, §4]. | Lattice reading; value. |
| SM:226 | the coefficient $4\sigma/45$ of §6.4 ($4/45$ at $\sigma = 1$) | the coefficient $2\sigma/15$ of §6.4 ($2/15$ at $\sigma = 1$) | Node 4. |
| SM:232 | including the $4\sigma/45$ coefficient | including the $2\sigma/15$ coefficient | Node 4. |
| SM:545 | $\chi(y + \eta\epsilon)$ | $\chi(y + \eta\epsilon_{\rm lat})$ | Symbol (lattice displacement). |
| SM:563 | (NN1, range exactly $\epsilon$) | (NN1, range exactly $\epsilon_{\rm lat}$) | Symbol. |
| SM:693 | the lattice scale is $1/\epsilon = M_{\text{Pl}}/(2\sqrt{\sigma})$ for an entropy $\sigma$ per boundary mode [GR §3.1, §4], and matching at $1/\epsilon$ instead shifts the running term of row $i$ below by $-(b_i/2\pi)\ln(2\sqrt{\sigma})$. The fitted $\delta_0$, $A$ and $B$ of §6.3 absorb that shift; the U(1)-row value of $\delta_0$ moves by $(b_1/2\pi)\ln(2\sqrt{\sigma}) \approx 0.65\ln(2\sqrt{\sigma})$, to $\delta_0 \approx 10.47$ at $\sigma = 1$. | the lattice scale is $1/\epsilon_{\rm lat} = M_{\text{Pl}}/\sqrt{6\sigma}$ for an entropy $\sigma$ per boundary mode [GR §3.1, §4], and matching at $1/\epsilon_{\rm lat}$ instead shifts the running term of row $i$ below by $-(b_i/2\pi)\ln\sqrt{6\sigma}$. The fitted $\delta_0$, $A$ and $B$ of §6.3 absorb that shift; the U(1)-row value of $\delta_0$ moves by $(b_1/2\pi)\ln\sqrt{6\sigma} \approx 0.65\ln\sqrt{6\sigma}$, to $\delta_0 \approx 10.60$ at $\sigma = 1$. | Node 4. |
| SM:711 | matching at the lattice scale $1/\epsilon$ moves $\delta_0$ by $0.65\ln(2\sqrt{\sigma})$, to $\delta_0 \approx 10.47$ at $\sigma = 1$. | matching at the lattice scale $1/\epsilon_{\rm lat}$ moves $\delta_0$ by $0.65\ln\sqrt{6\sigma}$, to $\delta_0 \approx 10.60$ at $\sigma = 1$. | Node 4. |
| SM:1128 | the substratum's lattice scale $1/\epsilon = M_{\mathrm{Pl}}/(2\sqrt{\sigma})$ | the substratum's lattice scale $1/\epsilon_{\rm lat} = M_{\mathrm{Pl}}/\sqrt{6\sigma}$ | Node 4. |
| SM:1271 | cubic lattice with spacing $\epsilon = 2\sqrt{\sigma}\,l_P$ | cubic lattice with spacing $\epsilon_{\rm lat} = \sqrt{6\sigma}\,l_P$ | Node 4. |
| SM:1448 | (the spacing $\epsilon = 2\sqrt{\sigma}\,l_p$ [GR §4] is physical, not a regulator), so there is no $\epsilon \to 0$ limit; $\omega^2 = k^2[1 - (k\epsilon)^2/45 + \ldots] = k^2[1 - (4\sigma/45)(E/M_{\text{Pl}})^2 + \ldots]$; $4\sigma/45 = 4/45$ at $\sigma = 1$; the amplitude $4\sigma/45$ is conditional | (the spacing $\epsilon_{\rm lat} = \sqrt{6\sigma}\,l_p$ [GR §3.1, §4] is physical, not a regulator), so there is no $\epsilon_{\rm lat} \to 0$ limit; $\omega^2 = k^2[1 - (k\epsilon_{\rm lat})^2/45 + \ldots] = k^2[1 - (2\sigma/15)(E/M_{\text{Pl}})^2 + \ldots]$; $2\sigma/15 = 2/15$ at $\sigma = 1$; the amplitude $2\sigma/15$ is conditional | Node 4 (four fragments of one line). |
| SM:1560 | the lattice cutoff $1/\epsilon = M_{\mathrm{Pl}}/(2\sqrt{\sigma})$ | the lattice cutoff $1/\epsilon_{\rm lat} = M_{\mathrm{Pl}}/\sqrt{6\sigma}$ | Node 4. |
| SM:1562 | the substratum lattice scale $1/\epsilon = M_{\mathrm{Pl}}/(2\sqrt{\sigma})$ | the substratum lattice scale $1/\epsilon_{\rm lat} = M_{\mathrm{Pl}}/\sqrt{6\sigma}$ | Node 4. |
| Structure:789 | the lattice spacing $\epsilon = 2\sqrt{\sigma}\,l_p$ | the lattice spacing $\sqrt{6\sigma}\,l_p$ [GR §3.1] | Node 4. |
| Structure:1068 | the lattice scale $M_{\mathrm{Pl}}/(2\sqrt{\sigma})$ | the lattice scale $M_{\mathrm{Pl}}/\sqrt{6\sigma}$ | Node 4. |
| Structure:1078 | the lattice scale $M_{\mathrm{Pl}}/(2\sqrt{\sigma})$ | the lattice scale $M_{\mathrm{Pl}}/\sqrt{6\sigma}$ | Node 4. |
| Substratum:225 | $(E\epsilon/\hbar c)^2 = 4\sigma(E/M_{\text{Pl}})^2$ | $(E\epsilon_{\rm lat}/\hbar c)^2 = 6\sigma(E/M_{\text{Pl}})^2$, with $\epsilon_{\rm lat} = \sqrt{6\sigma}\,l_p$ the lattice spacing ([GR §3.1]), | Node 4. |
| Substratum:227 | $(E\epsilon/\hbar c)^2 = 4\sigma(E/M_{\text{Pl}})^2$ | $(E\epsilon_{\rm lat}/\hbar c)^2 = 6\sigma(E/M_{\text{Pl}})^2$ | Node 4. |
| Substratum:482 | $(k\epsilon)^2$, $(k\epsilon)^4$ | $(k\epsilon_{\rm lat})^2$, $(k\epsilon_{\rm lat})^4$ | Symbol. |
| Substratum:483 | $\frac{(k\epsilon)^2}{45}$, $((k\epsilon)^4)$, $\frac{4\sigma}{45}$ | $\frac{(k\epsilon_{\rm lat})^2}{45}$, $((k\epsilon_{\rm lat})^4)$, $\frac{2\sigma}{15}$ | Node 4. |
| Substratum:484 | after using $\epsilon = 2\sqrt{\sigma}\,l_p$ and $k\epsilon = 2\sqrt{\sigma}\,E/M_{\text{Pl}}$; the coefficient of $(E/M_{\text{Pl}})^2$ is $4/45$ at $\sigma = 1$; $1/45$ of $(k\epsilon)^2$; the coefficient $4\sigma/45$ of $(E/M_{\text{Pl}})^2$; the amplitude $4\sigma/45$ is not yet | after using $\epsilon_{\rm lat} = \sqrt{6\sigma}\,l_p$ and $k\epsilon_{\rm lat} = \sqrt{6\sigma}\,E/M_{\text{Pl}}$; the coefficient of $(E/M_{\text{Pl}})^2$ is $2/15$ at $\sigma = 1$; $1/45$ of $(k\epsilon_{\rm lat})^2$; the coefficient $2\sigma/15$ of $(E/M_{\text{Pl}})^2$; the amplitude $2\sigma/15$ is not yet | Node 4. |
| Substratum:536 | (one mode per $\epsilon^2$ cell, no inherent frequency assignment — a count forced by the link-direction structure of the $K = 2d$ components, [GR §3.1]) | (one mode per area $\epsilon^2$, no inherent frequency assignment, with $\epsilon$ fixed by the link count of the $K = 2d$ components under the single-link reading, [GR §3.1]) | Bridge; "forced" rests on K2 (open). |
| Substratum:552 | the lattice spacing $\epsilon = 2\sqrt{\sigma}\,l_p$ | the lattice spacing $\epsilon_{\rm lat} = \sqrt{6\sigma}\,l_p$ | Node 4. |
| ch01:32 | Chapter 2 will show that self-consistency ties $\epsilon$ to the Planck length, $\epsilon = 2 \ell_P$ at one nat of entropy per boundary mode. | Chapter 2 will show that self-consistency ties the horizon area per boundary mode to the Planck length, $4\ell_P^2$ at one nat of entropy per boundary mode; on the cubic lattice under the single-link reading of Chapter 7 this gives $\epsilon = \sqrt6\,\ell_P$. | ch01's $\epsilon$ is Lemma 1's minimal cell (ch01:30). |
| ch04:128 | orientation-averaged coefficient is $4/45$ at one nat of entropy per boundary mode ($4\sigma/45$ for an entropy $\sigma$ per mode; the amplitude $4\sigma/45$ carries; the $4\sigma/45$ coefficient is not near-term testable | orientation-averaged coefficient is $2/15$ at one nat of entropy per boundary mode ($2\sigma/15$ for an entropy $\sigma$ per mode; the amplitude $2\sigma/15$ carries; the $2\sigma/15$ coefficient is not near-term testable | Node 4. |
| ch05:171 | range exactly $\epsilon = 2\sqrt{\sigma}\,\ell_P$ | range exactly one lattice spacing, $\sqrt{6\sigma}\,\ell_P$ | Node 4. |
| ch06:82 | the lattice scale itself being $1/\epsilon = M_{\text{Pl}}/(2\sqrt{\sigma})$ | the lattice scale itself being $M_{\text{Pl}}/\sqrt{6\sigma}$ | Node 4. |
| ch07:40 | each minimal cell of area $\epsilon^2$ contributes one boundary mode | each area $\epsilon^2$ of the horizon carries one boundary mode | Bridge. |
| ch07:59 | **The counting of one mode per cell, $\eta = \sigma/\epsilon^2$, is definitional — and the internal components do not multiply it.** … This counting is not an independent physical ansatz about the mode density but a consequence of the definition of $\epsilon$ as the minimal distinguishable scale. A cell finer than $\epsilon$ would subdivide the minimal scale; counting fewer modes would require a distinction below $\epsilon$ to group them. … The number of internal *components* per site ($K = 2d = 6$) is physical, but it does not multiply the count either, for a structural reason: the $K = 2d$ components are the $2d$ link directions from a cell, each coupling across exactly one link, and a boundary cell has exactly one outward-normal link crossing the horizon — the other $2d - 1$ are tangential or inward. One crossing link per cell means one coupled boundary mode per cell, forced by the link-direction structure rather than assumed ([GR §3.1]); one mode per cell does not, however, establish one nat per mode. The count of one mode per cell, and with it $\eta = \sigma/\epsilon^2$, is therefore the definition of $\epsilon$ together with a forced consequence of the component structure. | **The counting of one mode per area $\epsilon^2$, $\eta = \sigma/\epsilon^2$, is definitional; the internal components fix its relation to the lattice.** … This counting defines $\epsilon$, the horizon area per boundary mode being $\epsilon^2$, rather than adding an ansatz about the mode density. … The number of internal *components* per site ($K = 2d = 6$) is physical and enters through the link count. On the reading in which the $K = 2d$ components are the $2d$ link directions, each coupling across exactly one link (not derived from the substratum dynamics, [SM §4.5]), a horizon patch with unit normal $\mathbf n$ is crossed by $\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert$ links per square of the lattice spacing: one for a patch orthogonal to a lattice axis, $\tfrac32$ on average over a sphere. On the spherical horizon, therefore, $\epsilon^2$ is two thirds of the squared lattice spacing, and the lattice spacing is $\sqrt{6\sigma}\,l_p$ ([GR §3.1]); one mode per area $\epsilon^2$ does not establish one nat per mode. | Mirror of GR:104 and GR:156; the middle sentences on $q$ and $\sigma$ are unchanged. |
| ch07:65 | The two are consistent — substituting $\eta = \sigma/\epsilon^2$ and $\hbar = c^3 \epsilon^2/(4G\sigma)$ into Jacobson's relation $G_{\text{eff}} = c^3/(4\eta\hbar)$ recovers $G_{\text{eff}} = G$, with $\sigma$ cancelling — but the roles of input and output are reversed. | The two are consistent on the spherical horizon — substituting $\eta = \sigma/\epsilon^2$ and $\hbar = c^3 \epsilon^2/(4G\sigma)$ into Jacobson's relation $G_{\text{eff}} = c^3/(4\eta\hbar)$ recovers $G_{\text{eff}} = G$, with $\sigma$ cancelling — but the roles of input and output are reversed. On a planar patch with unit normal $\mathbf n$ the link density of Section 7.3 gives $G_{\text{eff}}(\mathbf n) = 3G/\big(2(\lvert n_1\rvert+\lvert n_2\rvert+\lvert n_3\rvert)\big)$, so the agreement holds for the spherical average and not patch by patch. | Mirror of GR:160. |
| ch07:78 | The framework's substratum partition cell has linear extent $2\sqrt{\sigma}\, l_p$, which is $2\,l_p$, twice the Planck length, at $\sigma = 1$. | The horizon area per boundary mode is $\epsilon^2 = 4\sigma\,l_p^2$, so $\epsilon$ is $2\,l_p$, twice the Planck length, at $\sigma = 1$; on the single-link reading of Section 7.3 the lattice spacing is $\sqrt{3/2}\,\epsilon = \sqrt{6\sigma}\,l_p$. | Node 4. |
| ch07:94 | Each minimal cell of area $\epsilon^2 = 4\sigma\, l_p^2$ contributes the entropy $\sigma$ of one boundary mode | Each area $\epsilon^2 = 4\sigma\, l_p^2$ of the horizon carries one boundary mode of entropy $\sigma$ | Bridge. |
| ch07:173 | With the framework's UV cutoff at $\epsilon = 2\sqrt{\sigma}\, l_p$, the sum has cutoff at $1/\epsilon = M_{\text{Pl}}/(2\sqrt{\sigma})$ in natural units | With the framework's UV cutoff at the lattice spacing $\sqrt{6\sigma}\, l_p$, the sum has cutoff at $M_{\text{Pl}}/\sqrt{6\sigma}$ in natural units | Lattice reading; value. |
| ch09:324 | the framework's substratum is a cubic lattice at $\epsilon = 2\sqrt{\sigma}\,l_p$ | the framework's substratum is a cubic lattice of spacing $\sqrt{6\sigma}\,l_p$ | Node 4. |
| ch18:22 | the substratum is locally a cubic lattice at $\epsilon = 2\sqrt{\sigma}\,l_p$, with $\sigma$ the entropy of one boundary mode | the substratum is locally a cubic lattice of spacing $\sqrt{6\sigma}\,l_p$, with $\sigma$ the entropy of one boundary mode | Node 4. |
| ch18:144 | treats the lattice spacing $\epsilon = 2\sqrt{\sigma}\,l_p$ as a regulator | treats the lattice spacing $\sqrt{6\sigma}\,l_p$ as a regulator | Node 4. |
| ch18:226 | The substratum is a cubic lattice at discreteness scale $\epsilon = 2\sqrt{\sigma}\,l_p$ (Chapter 7 §7.4). | The substratum is a cubic lattice of spacing $\sqrt{6\sigma}\,l_p$ (Chapter 7 §§7.3–7.4). | Node 4. |
| ch19:28 | The lattice at $\epsilon = 2\sqrt{\sigma}\,l_p$, with $\sigma$ the entropy of one boundary mode, | The lattice of spacing $\sqrt{6\sigma}\,l_p$, with $\sigma$ the entropy of one boundary mode, | Node 4. |
| app-c:259 | the framework's substratum is a lattice at $\epsilon = 2\sqrt{\sigma}\, l_p$. | the framework's substratum is a lattice of spacing $\sqrt{6\sigma}\, l_p$. | Node 4. |
| FULL:367, 1236, 1489, 1595, 1906, 1925, 1931, 1944, 1960, 2039, 2791, 4828, 4950, 5032, 5173, 6486 | Verbatim mirrors of ch01:32, ch04:128, ch05:171, ch06:82, ch07:40, :59, :65, :78, :94, :173, ch09:324, ch18:22, :144, :226, ch19:28, app-c:259 | The same replacement as the chapter line | §A.14 mirror rule. |

Regeneration after any adoption: the `.tex`/`.pdf` of GR, SM, Structure, Substratum and the FULL book (AGENTS.md build recipe).

## 6. Skeptical passes on the favourable branch (B)

1. *Is B a relabelling that hides the factor?* No: every number that the factor changes is changed under B (node 4), and the factor is stated with its premises at GR:104. B only declines to rewrite statements that are exact in the counting reading.
2. *Does B leave "discreteness scale ε" contradicting Main?* Main's Lemma 1 introduces "a discreteness scale" with no value (Main:222: "of the order of the Planck length"); S3 as restated requires the substratum to fix GR's $\epsilon$ and no longer asserts identity with Lemma 1's scale, which P7-B 4.2 shows is independent in any case. The one site that identifies GR's value with Lemma 1's cell, ch01:32, is edited.
3. *Inventory (iii): are the unedited lattice-flavoured sites true?* Each is an order-of-magnitude statement or a cutoff explicitly called a convention; a factor $\sqrt{3/2}$ does not change $10^{-61}$, $10^{-122}$, $10^{-32}$ or "near the Planck scale". GR:326 and ch07:173 name the lattice cutoff with the value $2\sqrt\sigma\,l_p$ and are therefore edited. After that edit ch07:193 and GR:362 still quote the convention "cut off at $1/\epsilon$", with exact arithmetic ($S_{\rm dS}/(96\pi^2\sigma^2)$); if the reviewer prefers them to quote the lattice cutoff, the replacement is "cut off at $M_{\rm Pl}/\sqrt{6\sigma}$ … gives $S_{\rm dS}/(216\pi^2\sigma^2)$" ($(M_{\rm Pl}^4/36\sigma^2)/(16\pi^2)$ against $3H^2M_{\rm Pl}^2/8\pi$, with $S_{\rm dS}=\pi M_{\rm Pl}^2/H^2$), three more lines with the FULL mirror (FULL:2059).
4. *Search for further dependents.* Searched `papers/*.md`, `book/*.md`, `README.md` for $2\sqrt\sigma$, $2\,l_p$, $2\ell_P$, $4G\sigma$, $4\sigma l_p^2$, $4\sigma/45$, $4/45$, $\kappa_m$, "minimal cell", "one mode per", "linear extent", "lattice spacing", "lattice scale", "UV cutoff", "boundary-crossing component", $M_{\rm Pl}/(2\sqrt\sigma)$, $\ln(2\sqrt\sigma)$, $10.47$, $96\pi^2$, $k\epsilon$, $E\epsilon$. No further site. Passes 3 and 4 yield no NEW item.

## Result

The factor at GR:104 is $\tfrac32$ on GR:104's own premises (K1–K6; proved, node 1). The calibration and area law use $\epsilon$ as the counting length and are unaffected; the lattice-spacing statements carry the factor: lattice spacing $\sqrt{6\sigma}\,l_p$, lattice scale $M_{\rm Pl}/\sqrt{6\sigma}$, Lorentz-violation amplitude $2\sigma/15$, matching shift giving $\delta_0\approx10.60$. Recommended correction: Option B, 64 edited lines (proposed text in node 5). The local density depends on the patch orientation, which must be stated at GR:104 and scoped at GR:160, ch07:65 and GR:749.

**Classification of findings (§A.31).** CONFIRMING: P1–P2 (P7-B 4.4). ELABORATING: P3 (per-site count); $G_{\rm eff}(\mathbf n)$. NEW: the lattice-spacing statements carry physical numbers that change under every option (node 2, node 4); the classical/KMS temperature mismatch on tilted patches and Corollary A.4's shape condition (3.4). The productivity test of node 0 is met under (i)–(iii).

## Open questions

1. **Single-link reading (K2).** All corrected values rest on it, as did the current ones; SM:358, :364 record it as unestablished. Under SM §4.4's isotropic internal matrix, where each component reads every neighbour (SM:356), the crossing-component density and hence $\kappa_m$ differ again.
2. **Isotropy.** Whether the emergent description restores an orientation-independent horizon entropy density, removing the patch dependence of $\eta(\mathbf n)$, $G_{\rm eff}(\mathbf n)$ and the classical patch temperature (3.4), is not examined here.
3. **Counting rule (K3) and cut (K5).** Whether horizon modes are counted per crossing component, and whether the visible side is the set of sites inside the sphere, are posits; other convex cuts give area averages in $[1,\sqrt3]$.
4. **Non-spherical horizons.** For a Kerr horizon, or a horizon moving relative to the lattice frame, the area average of $\lvert\mathbf n\rvert_1$ is not $\tfrac32$; the calibration on such horizons is open under K2–K3.
5. **Verification records citing $\kappa_m=1$** (node 2, end): whether a mutable record should note the change, if B is adopted, is for the reviewer and owner.
