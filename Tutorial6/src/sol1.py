def product(n):
    if n == 2:
        return 2
    if n % 2 == 0:
        return n * product(n - 2)
    return product(n - 1)

print(product(int(input())))
