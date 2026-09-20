#!/usr/bin/env bash
# Extract text from a PDF into research/extracts. Usage: scripts/extract-pdf.sh <pdf-path> [slug]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PDF="${1:-}"
if [[ -z "$PDF" || ! -f "$PDF" ]]; then
  echo "usage: scripts/extract-pdf.sh <pdf-path> [slug]" >&2
  exit 2
fi
DATE="$(date -u +%Y-%m-%d)"
SLUG="${2:-$(basename "$PDF" | sed 's/\.[Pp][Dd][Ff]$//')}"
OUT="$ROOT/research/extracts/${DATE}-${SLUG}.txt"
mkdir -p "$ROOT/research/extracts" "$ROOT/tools"

VENV="$ROOT/tools/.venv"
if [[ ! -x "$VENV/bin/python" ]]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q pypdf
fi
"$VENV/bin/python" - "$PDF" "$OUT" <<'PY'
import sys
from pathlib import Path
from pypdf import PdfReader
src, dest = Path(sys.argv[1]), Path(sys.argv[2])
reader = PdfReader(str(src))
parts = []
for i, page in enumerate(reader.pages, 1):
    parts.append(f"\n===== PAGE {i} =====\n")
    parts.append(page.extract_text() or "")
dest.write_text("".join(parts), encoding="utf-8")
print(dest)
PY
