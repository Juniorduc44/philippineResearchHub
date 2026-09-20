#!/usr/bin/env python3
"""Strip a downloaded HTML file to readable text. Usage: python3 scripts/html-to-text.py <html> <out.txt>"""
from html.parser import HTMLParser
from pathlib import Path
import sys


class TextExtractor(HTMLParser):
    skip = {"script", "style", "noscript", "svg"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in self.skip:
            self._skip += 1
        if tag in {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "tr"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.skip and self._skip:
            self._skip -= 1
        if tag in {"p", "div", "li", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._skip:
            return
        text = " ".join(data.split())
        if text:
            self.parts.append(text + " ")


def main():
    if len(sys.argv) != 3:
        print("usage: html-to-text.py <html> <out.txt>", file=sys.stderr)
        sys.exit(2)
    src, dest = Path(sys.argv[1]), Path(sys.argv[2])
    parser = TextExtractor()
    parser.feed(src.read_text(encoding="utf-8", errors="replace"))
    lines = []
    for raw in "".join(parser.parts).splitlines():
        line = " ".join(raw.split())
        if line:
            lines.append(line)
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(dest)


if __name__ == "__main__":
    main()
