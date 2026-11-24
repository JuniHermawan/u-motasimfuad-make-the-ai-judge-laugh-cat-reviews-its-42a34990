#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review from a house cat about
its human (88 characters) to /output/entry.txt.

The review was chosen from 24 original candidates (12 in round one,
10 challengers in round two, plus 2 controls) scored against the judge
brief: a deadpan one-star review shape, a specific complaint only a cat
would make, an unmistakably feline voice, and the sting in the last few
words. The two controls — a stale cats-rule cliche and a famous-book
retelling — scored far below the winner, so neither pattern was used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

TEXT = "One star. She bought me a bed. I sleep in the box it came in. The bed is for guests now."


def main() -> None:
    # Competition gate: the review must be UTF-8 text, 1-200
    # characters, and not whitespace-only. Validate before writing.
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 200 and text.strip(), "text violates gate"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
