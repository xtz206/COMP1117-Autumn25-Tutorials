def calc_check_digit(digits: list[int]) -> int:
    result = 0
    for index in range(len(digits)):
        digit = digits[-index - 1]
        if index % 2 == 0:
            digit *= 2
        if digit > 9:
            digit -= 9  # at most 2 digits
        result += digit
    return 10 - (result % 10)

digits = list(map(int, input().replace(' ', '')))
if calc_check_digit(digits[:-1]) == digits[-1]:
    print("Valid")
else:
    print("Invalid")

# 5190 9902 8192 5290
# 6823 1198 3424 8189
# 3716 8200 1927 1998
