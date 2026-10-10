"""EXPLORATION ONLY (floating point; certifies nothing).
d = 7: the word G_pi (I (x) L) G_pi with L the 90-degree rotation in the coordinate plane (2, 6)
(hom indices 3 and 7: w1 and z), the analogue of the d = 5 witness plane.  Prints a witness for b5.
"""
import numpy as np
import importlib.util
import os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("x1", os.path.join(here, "x1_jk_flow_float.py"))
x1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x1)
d, n = 7, 8
L = np.eye(d); i, j = 2, 6
L[i, i] = 0; L[j, j] = 0; L[j, i] = 1; L[i, j] = -1
H = np.eye(n); H[1:, 1:] = L
W = x1.gate(d, np.pi) @ np.kron(np.eye(n), H) @ x1.gate(d, np.pi)
m, (x, y, a, b) = x1.minimise(W, d, iters=3000, restarts=30)
print("min", m)
print("x", x.tolist()); print("y", y.tolist()); print("a", a.tolist()); print("b", b.tolist())
