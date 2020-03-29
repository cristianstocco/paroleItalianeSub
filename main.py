import re

SOURCE_FILE = "sources/660000_parole_italiane.txt"
INPUT_O = " > Write the pattern matching:\n < "
LINE_O = "===== ===== ======= ===== ====="
MATCHES_O = "===== MATCHES ====="
MARGIN_PATTER = "[a-zA-Z]*"

print( LINE_O )
dictionary = open(SOURCE_FILE, 'r')
pattern = raw_input(INPUT_O)

print( MATCHES_O )
read_data = dictionary.read()
if read_data:
    match = re.findall(MARGIN_PATTER + pattern + MARGIN_PATTER, read_data)

    if len( match ) > 0:
        print( match )

dictionary.close()