def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    if a < b:
        return b + multiply(a - 1, b)
    return a + multiply(a, b - 1)

a = int(input())
b = int(input())
print(multiply(a, b))
