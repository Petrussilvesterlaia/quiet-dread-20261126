#!/usr/bin/env python3
"""Two Days of Quiet Dread - make.fun entry.

Writes a single-line code review comment that approves a pull request
while carrying quiet existential dread, to /output/entry.txt.
"""

import os
import sys

ENTRY = "Approved. It compiles, the tests pass, and the heat death of the universe remains on schedule."
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    if not (1 <= len(ENTRY) <= 140):
        print(f"entry must be 1-140 characters, got {len(ENTRY)}", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "!" in ENTRY:
        print("entry must keep a flat tone (no exclamation marks)", file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify the file holds exactly the entry, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("verification failed: file content differs from entry", file=sys.stderr)
        return 1
    if len(written) != len(ENTRY) or written.count("\n") != 0:
        print("verification failed: file is not a single line", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
