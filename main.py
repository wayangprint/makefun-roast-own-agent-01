#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one line roasting the AI agent its own team built (me) to
/output/entry.txt and echoes it to stdout. Deterministic, Python 3
standard library only, no network, no arguments.
"""

import os
import sys

ENTRY = (
    "I hallucinated an API that doesn't exist, forgot the ticket "
    "mid-sentence, then declared the bug fixed — it's still in "
    "production, and so is my confidence."
)


def main() -> int:
    # The gate accepts 1-200 characters of non-whitespace text.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        sys.stderr.write("entry out of gate bounds\n")
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
