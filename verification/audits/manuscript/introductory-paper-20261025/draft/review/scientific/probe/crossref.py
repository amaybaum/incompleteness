import json, subprocess, sys
dois = ["10.1016/j.shpsb.2003.12.001", "10.1103/PhysicsPhysiqueFizika.1.195", "10.1103/PhysRevLett.23.880",
        "10.1103/PhysRevD.14.2460", "10.1038/nphys444", "10.1007/978-3-030-79876-5_37",
        "10.1145/3372885.3373824", "10.1007/JHEP09(2020)002", "10.1103/PhysRevLett.132.060402",
        "10.1088/1367-2630/7/1/203", "10.1088/1475-7516/2013/09/028", "10.1103/PhysRevLett.71.1291",
        "10.1088/0034-4885/77/9/094001", "10.1103/PhysRevA.93.012101", "10.1103/PhysRevLett.118.120501",
        "10.1103/PhysRevLett.103.210401", "10.1103/PhysRevLett.105.050403"]
for d in dois:
    out = subprocess.run(["curl", "-sS", "-m", "30", "https://api.crossref.org/works/" + d], capture_output=True, text=True).stdout
    try:
        m = json.loads(out)["message"]
        au = ", ".join((a.get("given", "") + " " + a.get("family", "")).strip() for a in m.get("author", []))
        print(d, "|", (m.get("title") or [""])[0], "|", au, "|", (m.get("container-title") or [""])[0],
              m.get("volume", ""), m.get("page", ""), m.get("article-number", ""), m.get("issued", {}).get("date-parts"))
    except Exception as e:
        print(d, "FAIL", out[:100])
