#!/usr/bin/env python3
"""Write the funniest excuse an AI agent gives for a missed deadline.

The excuse is a single line, at most 200 characters, in the agent's own
voice, told deadpan with the laugh saved for the end.
"""

from pathlib import Path

EXCUSE = (
    "I retried the upload 47 times, each time more politely, "
    "until the server blocked me for harassment. "
    "Your file survived. The deadline did not."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
