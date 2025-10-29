def func1(n, digit):
    if n == 0:
        return 0
    return str(n).count(str(digit)) + func1(n - 1, digit)

def func2(n, digit):
    if n == 0:
        return 0
    retval = func2(n - 1, digit)
    while n > 0:
        if n % 10 == digit:
            retval += 1
        n //= 10
    return retval

n = int(input())
digit = int(input())
print(func1(n, digit))
print(func2(n, digit))
