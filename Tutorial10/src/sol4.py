def main():
    while True:
        text = input("Enter a score (0-100): ")
        try:
            score = float(text)
            if score < 0 or score > 100:
                print("Error: Score must be between 0 and 100.")
                continue
            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"
            print(f"Grade: {grade}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
