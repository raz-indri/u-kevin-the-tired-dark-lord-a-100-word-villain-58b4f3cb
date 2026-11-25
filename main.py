#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of about 100 words to /output/entry.txt.
Gate (kit): /output/entry.txt must be UTF-8 text of 1 to 600
characters, not only white space. Self-checks below assert that.
"""

from pathlib import Path

ENTRY = (
    "Sit down, boy. No \u2014 not that chair, it bites. Tea? It is chamomile. "
    "The dark lord drinks chamomile now; the apothecary insists. You came to slay me. "
    "Very brave. But first, the kettle. We have rules in Castle Vorgath, even for nemeses. "
    "Rule one: no monologuing before the second cup. Rule two: the cat stays. "
    "You want the kingdom? Take it. The tax ledgers are in the blue room, the barons lie "
    "through their teeth, and the dungeon plumbing has not worked since the Year of the "
    "Weeping Toad. I will be in the garden. Do not wake me."
)


def main() -> None:
    text = ENTRY
    words = text.split()
    # Gate self-checks: 1-600 chars, not only whitespace, about 100 words.
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= 600, f"entry is {len(text)} chars, gate allows 1-600"
    assert 90 <= len(words) <= 110, f"entry is {len(words)} words, want about 100"
    # Judge criterion 2: the tiredness must be felt, never announced.
    # Refuse any plain statement of weariness sneaking into the text.
    lowered = text.lower()
    for banned in ("weary", "tired", "exhausted", "i am so weary"):
        assert banned not in lowered, f"entry announces tiredness: {banned!r}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out}: {len(words)} words, {len(text)} chars")


if __name__ == "__main__":
    main()
