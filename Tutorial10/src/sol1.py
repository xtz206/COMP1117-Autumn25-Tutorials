def main():
    date = input("Enter today's date (YYYY-MM-DD): ")
    entry = input("What's on your mind today? ")
    result = f"[{date}]: {entry}\n"
    with open("diary.txt", "a") as file:
        file.write(result)
    print("Diary entry saved successfully.")

if __name__ == "__main__":
    main()

