def main():
    text = input()
    try:
        score = float(text)
        if score < 0 or score > 100:
            print("Error: Score must be between 0 and 100.")
            return
        elif score >= 90:
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
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
