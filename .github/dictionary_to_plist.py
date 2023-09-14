import plistlib

INPUT_FILE = "dictionary.txt"
OUTPUT_FILE = "generated/dictionary.plist"


def parse_line(line: str) -> tuple[str | None, str | None]:
    """Returns the shortcut and phrase from a line in the format "<shortcut><tab><phrase><tab>".
    If the line is not in the above format, returns None for both values."""
    parts = line.strip().split("\t")
    if len(parts) == 2:
        return parts[0], parts[1]
    else:
        return None, None


# Create a list of dictionaries from the input file
data = []
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        shortcut, phrase = parse_line(line)
        if shortcut is not None and phrase is not None:
            data.append({"phrase": phrase, "shortcut": shortcut})

# Write the plist to a file
with open(OUTPUT_FILE, "wb") as plist_file:
    plistlib.dump(data, plist_file, fmt=plistlib.FMT_XML)
