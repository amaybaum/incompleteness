"""Run sails at N=8 and save result to file."""
import warnings
warnings.filterwarnings('ignore')
import time
import sys

from sails_correction import compute_sails
from paper_pi_s import compute_pi_s

N, m = 8, 0.05
with open('/tmp/sails_n8_progress.txt', 'w') as f:
    f.write(f"Starting N={N}, m={m} at {time.time()}\n")

t0 = time.time()
pi_s = compute_pi_s(N, m)
with open('/tmp/sails_n8_progress.txt', 'a') as f:
    f.write(f"Pi_s = {pi_s:.4f} at {time.time()-t0:.1f}s\n")

val = compute_sails(N, m, pi_s)
dt = time.time() - t0

with open('/tmp/sails_n8_result.txt', 'w') as f:
    f.write(f"N={N}, m={m}: Pi_s={pi_s:.4f}, sails={val:+.5e}, time={dt:.1f}s\n")

print(f"DONE: sails={val:+.5e}, time={dt:.1f}s")
