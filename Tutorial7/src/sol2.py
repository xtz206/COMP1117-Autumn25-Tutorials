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


def processCommand(line):
    tokens = line.strip().split()
    if not tokens:
        return None
    command = tokens[0].upper()
    args = tokens[1:]
    match command:
        case "LS":
            return ls()
        case "MKDIR":
            return mkdir(args[0])
        case "TOUCH":
            return touch(args[0])
        case "FILTER":
            return filter_items(args[0])


def main():
    input_line = input().strip()
    commands = input_line.split("&&")
    results = list(map(processCommand, commands))
    results = [res for res in results if res is not None]
    print(results)


if __name__ == "__main__":
    main()
