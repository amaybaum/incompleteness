"""Exact pre-check of the chart statements (chartR_gateOf, fourCopyCoherent_chart ingredients). Research only.
Usage: python3 -I -B precheck_chart.py ; VERDICT `PREFLIGHT-CHART-EXACT` iff every check passes."""
import itertools, sys
import sympy as sp
from sympy import Matrix
R4 = range(4)
PC = {(0,0):0,(0,1):0,(0,2):3,(0,3):3,(1,0):1,(1,1):1,(1,2):2,(1,3):2,(2,0):2,(2,1):2,(2,2):1,(2,3):1,(3,0):3,(3,1):3,(3,2):0,(3,3):0}
PT = {(0,0):0,(0,1):1,(0,2):2,(0,3):3,(1,0):1,(1,1):0,(1,2):3,(1,3):2,(2,0):1,(2,1):0,(2,2):3,(2,3):2,(3,0):0,(3,1):1,(3,2):2,(3,3):3}
def sgn(m,n): return -1 if (m==1 and n==3) or (m==2 and n==2) else 1
def cnot(w): return {(m,n): sgn(m,n)*w[PC[(m,n)],PT[(m,n)]] for m in R4 for n in R4}
def homMap(N,v): return [v[0]] + list(N*Matrix(v[1:]))
def actT(N,w):
    out={}
    for m in R4:
        row=homMap(N,[w[m,n] for n in R4])
        for n in R4: out[m,n]=row[n]
    return out
def actC(N,w):
    out={}
    for n in R4:
        col=homMap(N,[w[k,n] for k in R4])
        for m in R4: out[m,n]=col[m]
    return out
RY = sp.diag(1,-1,1)
def cnotTw(w): return actT(RY, cnot(actT(RY, w)))
SG=[1,1,-1,1]
def transposeW(w): return {(m,n): SG[m]*SG[n]*w[m,n] for m in R4 for n in R4}
def chartR(ei, ej, w):
    w1 = actT(RY, w) if ej else w
    return actC(RY, w1) if ei else w1
W = {(m,n): sp.Symbol("w%d%d"%(m,n)) for m in R4 for n in R4}
checks=[]
def check(name,c):
    checks.append(bool(c)); print(("PASS " if c else "FAIL ")+name)
check("X1 actC reflY . cnot . actC reflY = cnotTw", actC(RY, cnot(actC(RY, W))) == cnotTw(W))
check("B3 transposeW . cnot = cnot . transposeW", transposeW(cnot(W)) == cnot(transposeW(W)))
check("T  actC reflY . actT reflY = transposeW", actC(RY, actT(RY, W)) == transposeW(W))
ok=True
for ei, ej in itertools.product([False, True], repeat=2):
    g = cnotTw if (ei != ej) else cnot
    ok &= chartR(ei, ej, g(chartR(ei, ej, W))) == cnot(W)
check("C  chartR ei ej (gateOf (ei != ej) (chartR ei ej w)) = cnot w for all four (ei, ej)", ok)
ok_cc = chartR(True, False, cnot(chartR(True, False, W))) != cnot(W)
check("CC countercontrol: with the untwisted gate at (true, false) the identity fails", ok_cc)
print("--- precheck_chart: %d/%d" % (sum(checks), len(checks)))
print("VERDICT PREFLIGHT-CHART-EXACT" if all(checks) else "VERDICT NOT RENDERED")
