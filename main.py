"""One Emoji, One Smile.

The one emoji most likely to make a stranger smile: a face holding back
happy tears -- warmth that needs no words, no caption, no explanation.
Not the default smiley: the look of someone genuinely touched.
"""

import os

ENTRY = "\U0001F979"


def main() -> None:
    emoji = ENTRY
    if len(emoji) != 1:
        raise ValueError("entry must be exactly one character")
    if emoji.isspace():
        raise ValueError("entry must not be whitespace")
    # A single emoji is never plain ASCII text: refuse a letter or digit
    # sneaking in as the entry.
    if emoji.isascii():
        raise ValueError("entry must be an emoji, not ASCII text")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in emoji):
        raise ValueError("entry must not contain control characters")
    data = emoji.encode("utf-8")
    if not 1 <= len(data) <= 8:
        raise ValueError("entry must be 1-8 UTF-8 bytes")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
