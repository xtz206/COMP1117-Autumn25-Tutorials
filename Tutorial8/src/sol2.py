def combination(n, r):
    if r == 0 or r == n:
        return 1
    if r > n:
        return 0
    return combination(n - 1, r - 1) + combination(n - 1, r)

print(combination(6, 3))
print(combination(8, 1))
