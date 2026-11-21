"""Entry for make-the-ai-judge-feel-awe-20261121-1600.

Writes a single short text to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

import os

TEXT = (
    "The late light comes low through the window and lies along the table "
    "in one long amber band. Dust moves through it, slow as snow. "
    "The kettle ticks as it cools. The light stays a little, then goes, "
    "and the evening holds the room, wider than the walls, "
    "until it returns tomorrow."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
