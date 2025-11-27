def is_palindrome(number: int) -> bool:
    original_number = str(number)
    reversed_number = ""
    while number > 0:
        digit = number % 10
        reversed_number += str(digit)
        number //= 10
    return original_number == reversed_number


def main():
    n = int(input())
    if is_palindrome(n):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
