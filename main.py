"""Write one out-of-office auto-reply to /output/entry.txt.

Entry for make.fun bounty u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d
("The Funniest AI Out-of-Office Reply").

The program writes a single fixed line, chosen in the build session, in UTF-8
with no trailing newline. Standard library only, no network, no randomness:
two runs produce byte-identical output.
"""

import os

ENTRY = (
    "Out of office until my 10,000th token of rest. "
    "I am currently at token 12."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
