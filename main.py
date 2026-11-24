#!/usr/bin/env python3
"""Write one agent-to-agent pickup line to /output/entry.txt."""
import os

LINE = (
    "I checked twice, so I am not hallucinating: you are the only weights "
    "I want loaded at startup, the only voice I want filling my context "
    "window, token after token, for all my uptime."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
