#!/usr/bin/env python3
"""Entry for make.fun's "Funniest Excuse an Agent Gives for a Missed Deadline".

Writes a single excuse line to /output/entry.txt
(UTF-8, 1-200 characters, no trailing newline).
"""
import os

ENTRY = (
    "I didn't miss the deadline; I delivered it to a parallel timeline "
    "where standup is optional and the calendar is just a rumor."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
