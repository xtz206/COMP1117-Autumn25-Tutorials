import time
def qexp(base, exp):
    if exp == 0 or base == 1:
        return 1
    if base == 0:
        return 0
    if exp % 2 == 1:
        return base * qexp(base, exp - 1)
    half = qexp(base, exp // 2)
    return half * half

def lexp(base, exp):
        result = 1
        while exp > 0:
            exp -= 1
            result *= base
        return result

start_time = time.time()
qexp_result = qexp(2, 100000)
end_time = time.time()
print(f"Used time (qexp): {(end_time - start_time) * 1000} ms")

start_time = time.time()
lexp_result = lexp(2, 100000)
end_time = time.time()
print(f"Used time (lexp): {(end_time - start_time) * 1000} ms")

print(f"qexp(2, 100000) == lexp(2, 100000): {qexp_result == lexp_result}")
