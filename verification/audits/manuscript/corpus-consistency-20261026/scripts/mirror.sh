#!/bin/sh
# usage: mirror.sh file line  -> FULL.md line numbers whose full text equals that line
W=/tmp/claude-0/-home-user-incompleteness/57e93868-2ccb-5ebd-afb7-d31826198729/scratchpad/cc2/wt
f=$1; n=$2
line=$(sed -n "${n}p" "$W/$f")
m=$(grep -nxF -- "$line" "$W/book/The-Incompleteness-of-Observation-FULL.md" | cut -d: -f1 | tr '\n' ',')
echo "$f:$n -> FULL:${m:-NONE}"
