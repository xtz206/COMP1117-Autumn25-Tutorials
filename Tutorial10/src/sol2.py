def main():
    filename = "users.txt"
    username = input("Enter a username to register: ")
    try:
        with open(filename, "r") as file:
            if username in (line.strip() for line in file):
                print(
                    f"Username '{username}' already exists. "
                    "Please choose another one."
                )
                return
    except FileNotFoundError:
        pass  # File does not exist, proceed to register the user

    with open(filename, "a") as file:
        file.write(username + "\n")
    print(f"User '{username}' registered successfully.")

if __name__ == "__main__":
    main()
