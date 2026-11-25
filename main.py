#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message (<=200 chars) to /output/entry.txt:
the note an AI agent leaves after a long night fixing its own bugs.
"""

import os

ENTRY = (
    # Gate: 1-200 chars of UTF-8, not whitespace-only; 123 chars.
    "fix: reverted my own 2am genius, apologized to the test suite, "
    "and promised the linter it will never happen again (it will)"
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
