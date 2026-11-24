#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.
The word is fixed and deterministic: the same output on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

WORD = "Arsonist"  # the boss who starts the fires, then expects you to put them out


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
