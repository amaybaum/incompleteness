set -e
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad; R=verification/programmes/oi-qm/reconstruction/round-og-1-orbit-generation; F=0ae3e44ea096b567c4e0339fa642de73ec9d3a80; S1=9723513076df976c60c26b6523be7e97f8fec6c3
cd $S/wt-og1
test "$(git rev-parse HEAD)" = $S1
awk 'length > 120 && !/^\|/ {print "LONG "FNR": "length}' $R/result.md
git add $R/result.md
git -c user.name=Claude -c user.email=noreply@anthropic.com commit -q -F - <<'EOF'
OG-1 stage S2: the result note (candidate E), OG-1-INFRASTRUCTURE-PROVED

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1
EOF
E=$(git rev-parse HEAD); P=$(git rev-parse HEAD^)
echo "E $E parent $P"; [ "$P" = "$S1" ] && echo "parent == S1: yes"
echo "parents count: $(( $(git rev-list --parents -n1 $E | wc -w) - 1 ))"
echo "delta(S1,E): $(git diff --name-status $S1 $E | tr '\t' ' ')"
echo "result blob: $(git rev-parse $E:$R/result.md)"
echo "label line count: $(grep -cF '**Outcome:** `OG-1-INFRASTRUCTURE-PROVED`' $R/result.md)"
echo "cites S1 full SHA: $(grep -cF $S1 $R/result.md); cites run 36966428820: $(grep -c 36966428820 $R/result.md)"
echo "overclaim scan:"; grep -niE "implies the one-system|equivalen|sourc|derive|reconstruct" $R/result.md | cut -c1-150 | sed 's/^/   /'
PYTHONDONTWRITEBYTECODE=1 python3 $R/controls.py check $E --freeze $F | grep -v "^  PASS" || true
PYTHONDONTWRITEBYTECODE=1 python3 $R/controls.py check $E --freeze $F | grep -c "^  PASS"
git status --short | wc -l
