import re

with open("insulin_sequence.txt", "r") as original:
    with open("insulin_amino", "w") as new_file:
        while True:
            line = original.readline()
            new_line = re.sub("[(A-Z)|//|(0-9)|\r\n|\s+]", "", line)
            new_file.writelines(new_line)
            if not line:
                original.close()
                new_file.close()
                break
