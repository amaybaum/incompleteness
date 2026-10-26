#!/bin/sh
# usage: mirror.sh file line   (run inside a checkout, or set W to its root)  -> FULL.md line numbers whose full text equals that line
W=${W:-$(git rev-parse --show-toplevel)}
f=$1; n=$2
line=$(sed -n "${n}p" "$W/$f")
m=$(grep -nxF -- "$line" "$W/book/The-Incompleteness-of-Observation-FULL.md" | cut -d: -f1 | tr '\n' ',')
echo "$f:$n -> FULL:${m:-NONE}"
