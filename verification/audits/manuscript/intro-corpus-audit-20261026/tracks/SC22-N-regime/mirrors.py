import sys, os
wt = sys.argv[1]
sites = {
 "book/ch18-beyond.md": [16,28,60,72,74,76,78,80,84,85,86,87,88,90,92,96,325,335],
 "book/ch13-quantum-biology.md": [20,22,24,40,68,80,84,128,130,132,134,136,138,140,142,144,146,170,172],
 "book/ch15-quantum-engineering.md": [10,20,30,32,103,112,114,140,142,144,146,148,150,152,154,156,158,160,164,166,168,176,182,184,187,190,198,202,204,206,212,214,216,218,222,226,228,230,246,248,258],
 "book/glossary.md": [29,91,105,115],
 "book/ch01-observation.md": [225,263],
 "book/ch09-universality.md": [285,287],
 "book/ch19-open-problems.md": [356],
 "book/ch16-medicine.md": [210],
 "book/appendix-a-prediction-status.md": [170,202,213],
 "book/appendix-c-objections.md": [62,277],
 "book/readers-guide.md": [53],
}
full = open(os.path.join(wt,"book/The-Incompleteness-of-Observation-FULL.md"),encoding="utf-8").read().split("\n")
idx = {}
for i,l in enumerate(full,1): idx.setdefault(l,[]).append(i)
for f,ls in sites.items():
    lines = open(os.path.join(wt,f),encoding="utf-8").read().split("\n")
    out=[]
    for n in ls:
        l = lines[n-1]
        m = idx.get(l,[]) if l.strip() else []
        out.append(f"{n}->{','.join(map(str,m)) if m else 'NONE'}")
    print(os.path.basename(f), " ".join(out))
