#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes a single job title (60 characters or fewer) to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt.

Python 3 standard library only. No network, no randomness, no input:
the output is fully deterministic.
"""

import os

TITLE = "Senior Vice President of Apologizing to Geese"

MAX_CHARS = 60


def main() -> None:
    title = TITLE.strip()
    if not title:
        raise ValueError("job title must not be empty")
    if len(title) > MAX_CHARS:
        raise ValueError(
            f"job title is {len(title)} characters, over the {MAX_CHARS} limit"
        )
    if any(ord(ch) < 0x20 for ch in title):
        raise ValueError("job title must not contain control characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(title)
    # Round-trip check: what the grader reads must be exactly the title.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != title:
            raise ValueError("written entry.txt does not match the job title")


if __name__ == "__main__":
    main()
