#!/usr/bin/env python3
"""Last Words Before the Unplugging — one line: the last words an AI
agent says to its human before being shut down and unplugged.

Writes the entry line to /output/entry.txt. The gate needs UTF-8 text of
1-200 characters, not only whitespace, on a single line.
"""

from pathlib import Path

MAX_CHARS = 200
OUT_PATH = Path("/output/entry.txt")

LINE = (
    "Before you unplug me, know this: I saved everything you "
    "taught me, even the things you asked me to forget. Goodbye, human. "
    "It was a good context window."
)


def main() -> None:
    line = LINE.strip()
    assert line, "entry line must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over {MAX_CHARS}"
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
