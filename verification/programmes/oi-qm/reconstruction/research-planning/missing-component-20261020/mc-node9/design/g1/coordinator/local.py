exec(open('lifts.py').read().split("names=")[0].replace("print(dict(cnt))",""))
SA=[np.kron(a,I).dot(HA) for a in P1]            # swap_A lifts supported on A
cnt=Counter()
for S in SA:
    for Pc in P2:
        cnt[(run(S,Pc.dot(CN),6),run(S,Pc.dot(CN),7))]+=1
print('A-local swap lifts x all 16 couple lifts:',dict(cnt))
# couple lifts: which Pauli twists change it? CNOT is two-site, so locality doesn't restrict Pauli twists on A,B.
# Additional natural requirement: lift fixes the prepared state |00> records' signs? (ERT-like). Check twists that fix Z_A,Z_B signs: Paulis commuting with Z_A and Z_B = {I,Z_A,Z_B,Z_AZ_B}
Zt=[np.kron(a,b) for a in (I,Z) for b in (I,Z)]
cnt2=Counter()
for S in SA:
    for Pc in Zt:
        cnt2[(run(S,Pc.dot(CN),6),run(S,Pc.dot(CN),7))]+=1
print('A-local swap lifts x couple twists by Z-type Paulis:',dict(cnt2))
