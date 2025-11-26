def is_palindrome(n: int) -> bool:
    original = str(n)
    reverse = ""
    while n > 0:
        digit = n % 10
        reverse += str(digit)
        n //= 10
    return original == reverse


def main():
    n = int(input())
    if is_palindrome(n):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
