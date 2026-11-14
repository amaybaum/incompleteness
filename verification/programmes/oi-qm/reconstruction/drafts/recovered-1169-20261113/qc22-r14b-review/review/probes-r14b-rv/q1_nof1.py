# Reviewer check (generic, synthetic records only): r14b's no-unapproved-F1 predicate as written
# (lines 1752-1756; IMPL-DELTA-r14b A1) against the NOF1 cases (800-803) and one extra case.
ABS = None
def rule(jb, b4, a3, a3b):
    ok_b = jb in (ABS, "skipped") and b4 in (ABS, "skipped")
    return ok_b and (a3 in (ABS, "skipped") or a3b == "success")
cases = [  # (label, jobB, B4, A3, A3b, expected per NOF1)
 ("A3 absent", "skipped","skipped",ABS,ABS,True),
 ("A3 skipped, A3b failure", "skipped","skipped","skipped","failure",True),
 ("A3 failure, A3b success", "skipped","skipped","failure","success",True),
 ("A3 failure, A3b failure", "skipped","skipped","failure","failure",False),
 ("A3 cancelled, A3b failure", "skipped","skipped","cancelled","failure",False),
 ("A3 null, A3b failure", "skipped","skipped","null","failure",False),
 ("A3 success, A3b failure", "skipped","skipped","success","failure",False),
]
for a3 in (ABS,"skipped","failure","success"):
    for a3b in (ABS,"failure","success"):
        cases.append((f"B4 success, A3 {a3}, A3b {a3b}","skipped","success",a3,a3b,False))
bad = 0
for lab,jb,b4,a3,a3b,exp in cases:
    got = rule(jb,b4,a3,a3b)
    if got != exp: bad += 1; print("MISMATCH", lab, got, exp)
print("NOF1 cases", len(cases), "mismatches", bad)
# Extra (not in NOF1): job A present, A1/A2 success, no step named A3 or A3b (renamed steps on a
# recorded-branch commit whose job carries the frozen display name).
print("job A present, A1/A2 success, A3 and A3b absent ->", rule("skipped","skipped",ABS,ABS))
