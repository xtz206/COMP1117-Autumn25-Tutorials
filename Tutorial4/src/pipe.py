with open("data.txt") as file:
    for line in map(
        str.upper,  # convert to uppercase
        filter(
            lambda x: x.strip(),  # remove empty lines
            (l.strip() for l in file),  # remove '\n'
        ),
    ):
        print(line)
        # Prints non-empty lines in uppercase
