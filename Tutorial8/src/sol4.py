def convert_base(n: int, b: int) -> str:
    # Check special cases (You may skip this part)
    if b < 2 or b > 16:
        raise ValueError("Base must be between 2 and 16")
    if n < 0:
        return "-" + convert_base(-n, b)
    
    if n == 0:
        return "0"

    digits = "0123456789ABCDEF"
    if n < b:
        return digits[n]
    return convert_base(n // b, b) + digits[n % b]

print(convert_base(13, 2))
print(convert_base(56, 4))
print(convert_base(1117, 8))
print(convert_base(2019, 16))
