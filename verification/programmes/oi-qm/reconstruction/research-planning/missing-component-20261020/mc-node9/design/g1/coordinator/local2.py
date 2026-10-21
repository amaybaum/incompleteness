exec(open('lifts.py').read().split("names=")[0].replace("print(dict(cnt))",""))
nm=['I','X','Z','XZ']
S=HA
for i,a in enumerate(P1):
    for j,b in enumerate(P1):
        C=np.kron(a,b).dot(CN)
        print('couple lift',nm[i]+'_A',nm[j]+'_B','·CNOT -> W6',run(S,C,6),'W7',run(S,C,7))
