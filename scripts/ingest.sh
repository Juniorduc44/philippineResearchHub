#!/usr/bin/env bash
# Download a URL once into research/inbox. Usage: scripts/ingest.sh <url> <slug>
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INBOX="$ROOT/research/inbox"
mkdir -p "$INBOX"

if [[ $# -lt 2 ]]; then
  echo "usage: scripts/ingest.sh <url> <slug>" >&2
  exit 2
fi
URL="$1"
SLUG="$2"
DATE="$(date -u +%Y-%m-%d)"
BASE="${DATE}-${SLUG}"

# Whole-line fixed-string match so a parent path does not collide with a child URL.
if grep -qsxF -- "- URL: ${URL}" "$INBOX"/*.meta.md "$ROOT/research/INDEX.md" 2>/dev/null; then
  echo "already indexed or meta-logged: $URL" >&2
  grep -lxF -- "- URL: ${URL}" "$INBOX"/*.meta.md "$ROOT/research/INDEX.md" 2>/dev/null || true
  exit 0
fi

TMP="$INBOX/.tmp"
mkdir -p "$TMP"
# -L follows redirects. -f fails on HTTP errors. Filename from header when possible.
HEADERS="$TMP/${BASE}.headers"
BODY="$TMP/${BASE}.body"
curl -fsSL --max-time 45 -D "$HEADERS" -o "$BODY" \
  -A "PhilippineResearchHub/1.0 (local archive; +https://github.com/)" \
  "$URL"

CTYPE="$(grep -i '^content-type:' "$HEADERS" | tail -n1 | tr -d '\r' | awk '{print tolower($2)}' | cut -d';' -f1)"
EXT="bin"
case "$CTYPE" in
  text/html*) EXT="html" ;;
  application/pdf*) EXT="pdf" ;;
  text/plain*) EXT="txt" ;;
  application/json*) EXT="json" ;;
  text/csv*|application/csv*) EXT="csv" ;;
  application/xml*|text/xml*) EXT="xml" ;;
esac
# Honor obvious URL suffixes when the header is generic
if [[ "$EXT" == "bin" ]]; then
  case "$URL" in
    *.pdf*|*.PDF*) EXT="pdf" ;;
    *.html*|*.htm*) EXT="html" ;;
  esac
fi

DEST="$INBOX/${BASE}.${EXT}"
mv "$BODY" "$DEST"
HASH="$(sha256sum "$DEST" | awk '{print $1}')"
BYTES="$(wc -c < "$DEST" | tr -d ' ')"
META="$INBOX/${BASE}.meta.md"
cat > "$META" <<EOF
# ${BASE}

- URL: ${URL}
- Fetched: ${DATE}
- Content-Type: ${CTYPE}
- Bytes: ${BYTES}
- SHA256: ${HASH}
- Inbox: research/inbox/${BASE}.${EXT}
EOF
rm -f "$HEADERS"
rmdir "$TMP" 2>/dev/null || true
echo "$DEST"
echo "$META"
