"""Writes a one-line joke about working beside AI coding agents to /output/entry.txt."""

import os

JOKE = (
    "I set two agents to review each other's code; they approved "
    "everything in four seconds and have been congratulating each "
    "other ever since."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
