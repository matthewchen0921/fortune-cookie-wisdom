#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers entry: "The Silent Review".

Writes one line to /output/entry.txt: a fortune-cookie warning about the
pull request nobody commented on. The joke is the fortune-cookie voice
applied to code review: "Beware ... for silence is the loudest review."
It is true about a developer's day — an empty review usually means nobody
actually read the diff — and it turns on a double meaning: silence is
loud, and a "review" is both the comments on the PR and the judgement
itself. One balanced sentence, landing in a single breath, in the classic
fortune-cookie shape. The line is a warning, not a punchline: it reads
like something cracked open from a cookie, not a slogan.

Invented, not a real incident: no real pull request, reviewer or codebase
appears in it. 78 characters, under the 120-char cap.
"""

import os

LINE = "Beware the pull request with no comments, for silence is the loudest review."

MAX_CHARS = 120


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-120 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    # len() counts characters, not bytes, matching the gate's character cap.
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 120 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.endswith("review."), "the fortune ends on its twist"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
