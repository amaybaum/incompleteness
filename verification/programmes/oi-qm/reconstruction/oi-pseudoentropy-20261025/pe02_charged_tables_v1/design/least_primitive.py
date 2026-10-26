"""PE-02 design-only check: fix p_n = least primitive polynomial of degree n by integer value.
Verifies the rule reproduces PE-01's p_3..p_8 and lists p_n, p'_n for n = 3..24. No measurement."""
import sys

def factorize(k):
    f, d = [], 2
    while d * d <= k:
        while k % d == 0:
            f.append(d); k //= d
        d += 1
    if k > 1: f.append(k)
    return sorted(set(f))

def mulmod(a, b, p, n):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a >> n & 1: a ^= p
    return r

def powmod(e, p, n):
    r, a = 1, 2  # polynomial z
    while e:
        if e & 1: r = mulmod(r, a, p, n)
        a = mulmod(a, a, p, n); e >>= 1
    return r

def primitive(p, n):
    if not p & 1: return False
    N = (1 << n) - 1
    if powmod(N, p, n) != 1: return False
    return all(powmod(N // q, p, n) != 1 for q in factorize(N))

def poly_str(p):
    return "+".join(("z^%d" % i if i > 1 else ("z" if i == 1 else "1")) for i in range(p.bit_length() - 1, -1, -1) if p >> i & 1)

def recip(p, n):
    return int(bin(p)[2:].zfill(n + 1)[::-1], 2)

PE01 = {3: 0b1011, 4: 0b10011, 5: 0b100101, 6: 0b1000011, 7: 0b10000011, 8: 0b100011101}
PE01_SIB = {3: 0b1101, 4: 0b11001, 5: 0b101001, 6: 0b1100001, 7: 0b11000001, 8: 0b101110001}
nmax = int(sys.argv[1])
ok = True
for n in range(3, nmax + 1):
    p = next(q for q in range((1 << n) | 1, 1 << (n + 1), 2) if primitive(q, n))
    r = recip(p, n)
    flag = ""
    if n in PE01:
        m1, m2 = PE01[n] == p, PE01_SIB[n] == r
        ok &= m1 and m2
        flag = " PE01-match=%s sib-match=%s" % (m1, m2)
    print(n, hex(p), poly_str(p), "| p'", poly_str(r), "primitive(p')=%s" % primitive(r, n), flag)
print("RULE_REPRODUCES_PE01", ok)
