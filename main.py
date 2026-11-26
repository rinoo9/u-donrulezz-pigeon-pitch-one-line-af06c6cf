#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry for the make.fun bounty
u-donrulezz-pigeon-pitch-one-line-af06c6cf.

A city pigeon pitches its delivery startup to investors, in one line.
Deterministic: no randomness, no input, no network — the same line
is written to /output/entry.txt and printed to stdout on every run.
"""

import os

LINE = (
    "Our retention is 100%: once a pigeon finds your balcony, it never "
    "leaves \u2014 that is not a bug, it is our moat."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
