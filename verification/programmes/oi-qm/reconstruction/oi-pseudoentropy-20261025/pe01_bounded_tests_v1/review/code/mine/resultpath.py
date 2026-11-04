import sys, time, json
sys.path.insert(0, sys.argv[1])
from pe01 import shard as S
n, fam = int(sys.argv[2]), sys.argv[3]
ctl = S.Controls(); timing = {}
t = time.time()
out = S.shard_family(n, fam, "result", ctl, timing)
print("n=%d %s result-mode family shard: %.1fs" % (n, fam, time.time() - t), {k: round(v, 1) for k, v in timing.items()})
print({k: (v["pass"], v["checks"], v["failures"][:2]) for k, v in ctl.rec.items()})
print("witnesses:", [(w["subclass"], w["K"], w["adv_pred"], w["pred_minus_half"], w["footprint"], w["K_cx"]) for w in out["witnesses"]][:12])
