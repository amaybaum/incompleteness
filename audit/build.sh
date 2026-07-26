#!/bin/sh
# build.sh — canonical regeneration of .tex / .pdf from Markdown sources.
#
# Use this rather than typing pandoc by hand. Five papers were once published with
# .tex/.pdf built without --include-in-header=unicode-fix.tex; xelatex silently
# dropped the glyphs it had no font for (Juno lost over a thousand characters) and
# the output looked fine on inspection. The recipe in AGENTS.md was correct at the
# time and said so twice. A recipe you retype per file can be typed wrong; a loop
# cannot omit a flag that is written into it once.
#
# Usage:
#   ./audit/build.sh        build everything (12 papers + book)
#   ./audit/build.sh SM GR  build only the named papers
#   ./audit/build.sh --book build only the book
#
# Requires pandoc and xelatex. Reports any glyphs xelatex still dropped, per the
# "check the log for Missing character warnings" step in AGENTS.md.

set -u

# Runs from anywhere: resolve this script's directory, then work from the repo root.
# (The script lives in audit/ but all source paths are repo-relative.)
cd "$(dirname "$0")/.." || exit 1

command -v pandoc  >/dev/null 2>&1 || { echo "error: pandoc not found";  exit 1; }
command -v xelatex >/dev/null 2>&1 || { echo "error: xelatex not found"; exit 1; }

PAPER_HDR="papers/unicode-fix.tex"
BOOK_MD="book/The-Incompleteness-of-Observation-FULL.md"
BOOK_HDR="book/unicode-fix.tex"
BOOK_OUT="book/The-Incompleteness-of-Observation-FULL"

status=0
missing_total=0
tmplog=$(mktemp)
trap 'rm -f "$tmplog"' EXIT

report_missing() {
    # $1 = label, $2 = log file. Lists DISTINCT dropped glyphs, which is what
    # tells you what to add to unicode-fix.tex; a bare count does not.
    n=$(grep -c "Missing character" "$2" 2>/dev/null); [ -n "$n" ] || n=0
    if [ "$n" -gt 0 ]; then
        missing_total=$((missing_total + n))
        glyphs=$(grep -o "Missing character: There is no [^ ]*" "$2" \
                 | sed 's/.*no //' | sort -u | tr '\n' ' ')
        printf '     %s dropped glyph(s); distinct: %s\n' "$n" "$glyphs"
    fi
}

build_paper() {
    name=$1
    md="papers/${name}.md"
    [ -f "$md" ] || { echo "  $name: no such source"; status=1; return; }
    printf '  %-15s' "$name"
    pandoc "$md" -s --pdf-engine=xelatex --include-in-header="$PAPER_HDR" \
        -o "papers/${name}.tex" >"$tmplog" 2>&1 || { echo "TEX FAILED"; status=1; return; }
    pandoc "$md" -s --pdf-engine=xelatex --include-in-header="$PAPER_HDR" \
        -o "papers/${name}.pdf" >"$tmplog" 2>&1 || { echo "PDF FAILED"; status=1; return; }
    pages=$(pdfinfo "papers/${name}.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
    echo "ok  ${pages:-?} pages"
    report_missing "$name" "$tmplog"
}

build_book() {
    printf '  %-15s' "book"
    pandoc "$BOOK_MD" -s --toc --toc-depth=3 --pdf-engine=xelatex \
        --include-in-header="$BOOK_HDR" -o "${BOOK_OUT}.tex" >"$tmplog" 2>&1 \
        || { echo "TEX FAILED"; status=1; return; }
    pandoc "$BOOK_MD" -s --toc --toc-depth=3 --pdf-engine=xelatex \
        --include-in-header="$BOOK_HDR" -o "${BOOK_OUT}.pdf" >"$tmplog" 2>&1 \
        || { echo "PDF FAILED"; status=1; return; }
    pages=$(pdfinfo "${BOOK_OUT}.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
    echo "ok  ${pages:-?} pages"
    report_missing "book" "$tmplog"
}

if [ $# -eq 0 ]; then
    for md in papers/*.md; do
        base=$(basename "$md" .md)
        build_paper "$base"
    done
    build_book
elif [ "$1" = "--book" ]; then
    build_book
else
    for n in "$@"; do build_paper "$n"; done
fi

echo
if [ "$missing_total" -gt 0 ]; then
    echo "note: $missing_total dropped glyph(s) total — add the distinct characters"
    echo "      listed above to unicode-fix.tex, then rebuild."
fi
[ "$status" -eq 0 ] && echo "build: OK" || echo "build: FAILED"
exit "$status"
