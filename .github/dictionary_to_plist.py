import plistlib

INPUT_FILE = "dictionary.txt"
OUTPUT_FILE = "dictionary.plist"

def parse_line(line: str) -> tuple[str | None, str | None]:
    """
    Parses a line in the format "<phrase><tab><shortcut><tab>"
    and returns the phrase and shortcut. If the line is not
    in the correct format, returns None for both values.
    """
    parts = line.strip().split('\t')
    if len(parts) == 2:
        return parts[1], parts[0]
    else:
        return None, None

# Read input from a file
input_data = []
with open(INPUT_FILE, 'r', encoding='utf-8') as file:
    for line in file:
        phrase, shortcut = parse_line(line)
        if phrase is not None and shortcut is not None:
            input_data.append((phrase, shortcut))

# Create a list of dictionaries
output_data = [{'phrase': phrase, 'shortcut': shortcut} for phrase, shortcut in input_data]

# Write the plist to a file
with open(OUTPUT_FILE, 'wb') as plist_file:
    plistlib.dump(output_data, plist_file, fmt=plistlib.FMT_XML)
