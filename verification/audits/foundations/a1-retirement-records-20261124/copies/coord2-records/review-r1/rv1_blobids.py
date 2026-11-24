#!/usr/bin/env python3
"""Compute git blob ids (no object writes) of AGENTS.md for X (=H+D296) and L (=M+D296, Q+D296)."""
import subprocess, hashlib, json
R="<repo>"
def show(c,p): return subprocess.check_output(["git","-C",R,"show",f"{c}:{p}"])
ed=json.loads(show("4c79be642ca631573f06b444903be75ec4f5e2b6","verification/audits/foundations/a1exit-deletion-20261121/edits.json"))
d=[e for e in ed["edits"] if e["id"]=="D296"][0]; old=d["old"].encode(); new=d["new"].encode()
bid=lambda b: hashlib.sha1(b"blob %d\0"%len(b)+b).hexdigest()
for n,c in (("H","53c6601a10419b6b333cc992474272501ab542af"),("M","4fb2c1eed350edf95da2b316abcca93717246589"),("Q","47e23023450fb8fcbd61b5c776a69ba61897f267")):
    b=show(c,"AGENTS.md"); r=b.replace(old,new,1); print(n,"+D296 git blob",bid(r),"sha256",hashlib.sha256(r).hexdigest())
print("T1' AGENTS.md blob",subprocess.check_output(["git","-C",R,"rev-parse","14ac71b4b0a0c0aa2d7068d6799a73f474097060:AGENTS.md"]).decode().strip())
