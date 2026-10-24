"""C-i verification battery (exact: F2 bitmasks, distributions in Fractions).

V1  The elementary construction (PREREG §4) as an abstract map on (q, p, Q, P):
      Q' = Q + omega(u,h), q' = q + uq P, p' = p + up P, P' = P, for the three nonzero u.
      Checks: bijective; symplectic for the form pairing (q,p) and (Q,P); equals R_u when
      Q = 0 and P is uniform, independent and discarded; countercontrol with P known.
V2  K-SYMP2 inside the lattice conventions of f2.py (Main.md l.290 on two sites, region
      partition R = {site 0}), clean visible site, uniform hidden site, two waiting steps.
V3  The pairing obstruction under the region partition (exact, exhaustive at n <= 4): for
      every graph and every word of update steps and SYMPLECTIC visible maps, a map whose
      designated rows equal the target with Q and P on different sites is not symplectic --
      checked here as the algebraic identity omega(row_Q', row_q') + J(Q', q') = uq (J(Q,P) + 1).
V4  Split-site exposure: under the lattice update, the hidden coordinate of a site whose
      other coordinate is visible enters that visible coordinate after one step
      (v'_x = u_x exactly; u'_x = sum_{z~x} u_z + v_x), for every graph at n <= 4.
"""
from fractions import Fraction
from itertools import product, combinations
from f2 import (compose, apply, is_invertible, is_symplectic, lattice_update, omega, popc,
                identity)

ALL_OK = True


def check(label, cond):
    global ALL_OK
    ALL_OK &= bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")


# ---------------------------------------------------------------- V1
print("V1  elementary construction on (q, p, Q, P)")
# abstract coordinates as a 2-'site' system: site 0 = toy (u0=q, v0=p), site 1 = pointer
# (u1=Q, v1=P); then the symplectic form of f2.py pairs q<->p and Q<->P, as the draft intends.
n = 2
q, Q, p, P = 0, 1, 2, 3


def target(uq, up):
    rows = [0] * 4
    rows[Q] = (1 << Q) | (up << q) | (uq << p)
    rows[q] = (1 << q) | (uq << P)
    rows[p] = (1 << p) | (up << P)
    rows[P] = 1 << P
    return tuple(rows)


def bits(s, i):
    return (s >> i) & 1


def state(qv, pv, Qv, Pv):
    return (qv << q) | (pv << p) | (Qv << Q) | (Pv << P)


for (uq, up) in ((1, 0), (0, 1), (1, 1)):
    T = target(uq, up)
    print(f" u = ({uq},{up})")
    check("bijective (invertible over F2)", is_invertible(T))
    check("symplectic: omega(row_i,row_j) = J_ij for all i,j", is_symplectic(T, n))
    # R_u reproduction: Q = 0, P uniform independent, P discarded.
    good = True
    for (hq, hp) in product((0, 1), repeat=2):
        w = up * hq + uq * hp  # omega(u,h)
        dist = {}
        for Pv in (0, 1):
            s2 = apply(T, state(hq, hp, 0, Pv))
            key = (bits(s2, Q), bits(s2, q), bits(s2, p))
            dist[key] = dist.get(key, Fraction(0)) + Fraction(1, 2)
        # R_u: x ^= omega(u,h), then h ^= r u, r a fresh fair bit
        ref = {}
        for r in (0, 1):
            key = (w & 1, hq ^ (r * uq), hp ^ (r * up))
            ref[key] = ref.get(key, Fraction(0)) + Fraction(1, 2)
        good &= (dist == ref)
        # the displacement is independent of the record: given Q', h' is uniform on h + {0,u}
    check("Q=0, P uniform, P discarded: joint law of (Q', h') equals R_u for all four h", good)
    # countercontrol: P known
    kn0 = all(apply(T, state(hq, hp, 0, 0)) == state(hq, hp, (up * hq + uq * hp) & 1, 0)
              for hq, hp in product((0, 1), repeat=2))
    kn1 = all(apply(T, state(hq, hp, 0, 1)) == state(hq ^ uq, hp ^ up, (up * hq + uq * hp) & 1, 1)
              for hq, hp in product((0, 1), repeat=2))
    check("countercontrol P = 0 known: Q' = omega(u,h), h' = h (read without disturbance)", kn0)
    check("countercontrol P = 1 known: h' = h + u, a known, deterministic shift", kn1)
    # with P known the observer's post-read state is a point mass given (h, record):
    # e.g. a fair h with omega(u,h) recorded and P = 0 known leaves h on a coset of size 2
    # that is unchanged, so a second read of a conjugate functional is undisturbed.

# ---------------------------------------------------------------- V2
print("V2  K-SYMP2 in the lattice conventions")
n = 2
M = lattice_update(n, ((0, 1),))
check("two-site update bijective", is_invertible(M))
check("two-site update symplectic", is_symplectic(M, n))
u0, u1, v0, v1 = 0, 1, 2, 3          # site 0 visible (u0, v0), site 1 hidden (u1, v1)
M2 = compose(M, M)
# record: visible site after each step; prior: visible (0,0), hidden uniform
branches = {}
for (a, b) in product((0, 1), repeat=2):
    s0 = (a << u1) | (b << v1)
    s1 = apply(M, s0)
    s2 = apply(M, s1)
    rec = (bits(s1, u0), bits(s1, v0), bits(s2, u0), bits(s2, v0))
    hid = (bits(s2, u1), bits(s2, v1))
    branches.setdefault(rec, {}).setdefault(hid, Fraction(0))
    branches[rec][hid] += Fraction(1, 4)
print("  after two steps the visible site equals (v1, u1) of the input:",
      all(apply(M2, (a << u1) | (b << v1)) & 0b0101 == ((b << u0) | (a << v0))
          for a, b in product((0, 1), repeat=2)))
worst = min(len(h) for h in branches.values())
check("every record branch has probability 1/4 and hidden support 1 (< 2^1)",
      all(sum(h.values()) == Fraction(1, 4) and len(h) == 1 for h in branches.values()))
print(f"  branches: {len(branches)}; minimum hidden support {worst}; support bound 2^N = 2 broken")
for rec, h in sorted(branches.items()):
    print(f"    record (u0,v0 after step 1; u0,v0 after step 2) = {rec}: hidden (u1,v1) = {list(h)} w.p. {sum(h.values())}")

# ---------------------------------------------------------------- V3
print("V3  pairing obstruction for designated rows equal to the target, Q and P on different sites")
# For a symplectic T, omega(row_i, row_j) = J_ij.  With rows equal to the target:
#   row_Q' = e_Q + up e_q + uq e_p, row_q' = e_q + uq e_P,  J(Q', q') = 0 (different sites).
# omega(row_Q', row_q') = uq*J(Q,P) + uq*J(p,q) = uq*(J(Q,P) + 1)  (J(p,q) = 1).
# Same-site toy pair, Q and P on different sites => J(Q,P) = 0 => value uq; likewise for p' it is up.
# Since u != 0 one of them is 1: no symplectic T has these designated rows.
viol = 0
tot = 0
for nn in (3, 4):
    for Qs in range(1, nn):
        for Ps in range(1, nn):
            if Ps == Qs:
                continue
            for Qc in (Qs, nn + Qs):
                for Pc in (Ps, nn + Ps):
                    for (uq, up) in ((1, 0), (0, 1), (1, 1)):
                        for (qq, pp) in ((0, nn), (nn, 0)):
                            rQ = (1 << Qc) | (up << qq) | (uq << pp)
                            rq = (1 << qq) | (uq << Pc)
                            rp = (1 << pp) | (up << Pc)
                            tot += 1
                            if omega(rQ, rq, nn) == 0 and omega(rQ, rp, nn) == 0:
                                viol += 1
check(f"for all {tot} placements (n = 3, 4) the target rows violate a symplectic pairing", viol == 0)
# and with Q and P on the SAME site (the split pointer) the pairing is consistent:
consist = 0
tot2 = 0
for nn in (2, 3, 4):
    for (uq, up) in ((1, 0), (0, 1), (1, 1)):
        for (Qc, Pc) in ((1, nn + 1), (nn + 1, 1)):
            for (qq, pp) in ((0, nn), (nn, 0)):
                rows = list(identity(2 * nn))
                rows[Qc] = (1 << Qc) | (up << qq) | (uq << pp)
                rows[qq] = (1 << qq) | (uq << Pc)
                rows[pp] = (1 << pp) | (up << Pc)
                tot2 += 1
                consist += is_symplectic(tuple(rows), nn)
check(f"same-site Q,P (split pointer): target extended by identity is symplectic in all {tot2} cases",
      consist == tot2)

# ---------------------------------------------------------------- V4
print("V4  split-site exposure under one update step")
bad = 0
cases = 0
for nn in (2, 3, 4):
    pairs = list(combinations(range(nn), 2))
    for mask in range(1 << len(pairs)):
        edges = tuple(pq for k, pq in enumerate(pairs) if (mask >> k) & 1)
        M = lattice_update(nn, edges)
        for x in range(nn):
            cases += 1
            # v'_x = u_x exactly
            if M[nn + x] != (1 << x):
                bad += 1
            # u'_x = sum_{z~x} u_z + v_x : contains v_x, and otherwise only u's of neighbours
            nb = sum(1 << (b if a == x else a) for (a, b) in edges if x in (a, b))
            if M[x] != (nb | (1 << (nn + x))):
                bad += 1
check(f"for all {cases} (graph, site) cases at n <= 4: v'_x = u_x and u'_x = sum_(z~x) u_z + v_x", bad == 0)
print("  => a site with v_x visible exposes its hidden u_x exactly after one step;")
print("     a site with u_x visible exposes its hidden v_x masked only by its neighbours' u's.")

print("VERIFY:", "ALL PASS" if ALL_OK else "SOME FAIL")
