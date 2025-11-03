files = ["/home", "/Desktop", "/Documents", "test.txt"]


def ls():
    return sorted(files)


def mkdir(dirname):
    if dirname not in files:
        files.append(dirname)
    return f"Directory '{dirname}' created"


def touch(filename):
    if filename not in files:
        files.append(filename)
    return f"File '{filename}' created"


def filter_items(pattern):
    if pattern == "/":
        return sorted(f for f in files if f.startswith("/"))
    return sorted(f for f in files if f.endswith(pattern) and not f.startswith("/"))


def main():
    tokens = input().strip().split()
    command = tokens[0]
    args = tokens[1:]

    if command == "LS":
        print(ls())
    elif command == "MKDIR":
        print(mkdir(args[0]))
    elif command == "TOUCH":
        print(touch(args[0]))
    elif command == "FILTER":
        print(filter_items(args[0]))


if __name__ == "__main__":
    main()
