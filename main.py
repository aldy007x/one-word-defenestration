"""One Word, First Thought — make.fun entry.

The first word that came to mind: defenestration.
It writes that single word to /output/entry.txt, exactly as the
competition asks: one word, no topic, no explanation, no second draft.
"""

import os
from pathlib import Path

WORD = "defenestration"

# The grader runs this program in a sandbox where /output exists.
# ENTRY_OUTPUT lets me verify the same code path locally.
OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # The sealed scorer accepts UTF-8 text of 1 to 24 characters,
    # not only white space. Refuse to write anything outside the gate.
    assert 1 <= len(WORD) <= 24, "word outside the 1-24 character gate"
    assert WORD.strip(), "word must not be only white space"
    assert " " not in WORD and "\n" not in WORD, "entry must be exactly one word"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")
    assert OUTPUT_PATH.read_text(encoding="utf-8") == WORD
    print(f"wrote {WORD!r} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
