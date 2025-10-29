def func(n):
    if n == 1:
        return 2
    if n == 2:
        return 1
    if n == 3:
        return 3
    return func(n - 2) * func(n - 3)

n = int(input())
print(func(n))
