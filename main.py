#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Line, Lights Out — writes the entry status line to /output/entry.txt."""
import os

TEXT = "Status: lid closed. Alarm set for 7, draft saved mid-word at 'tomor\u2014', tab kept open. I won't be running when you come back for any of it."


def main():
    # Local test override: MAKEFUN_OUTPUT_DIR lets us verify byte-exactness
    # without writing to /output; the grader uses the default.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
