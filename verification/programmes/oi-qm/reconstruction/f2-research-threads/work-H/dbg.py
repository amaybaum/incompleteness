import numpy as np
S = np.diag([1, 1j]); Hd = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
def canon(U):
    k = np.flatnonzero(np.abs(U.ravel()) > 1e-9)[0]
    ph = U.ravel()[k] / abs(U.ravel()[k])
    V = np.round(U / ph, 8) + 0.0
    V = V.real + 0.0 + 1j * (V.imag + 0.0)
    return V
seen = {canon(np.eye(2, dtype=complex)).tobytes()}; cliff=[np.eye(2,dtype=complex)]; fr=list(cliff)
while fr:
    new=[]
    for U in fr:
        for g in (Hd,S):
            V=g@U; key=canon(V).tobytes()
            if key not in seen: seen.add(key); new.append(V); cliff.append(V)
    fr=new
print(len(cliff))
