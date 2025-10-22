import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Used time: {(end_time - start_time) * 1000} ms")
        return result
    return wrapper

@timeit
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
print(fib(10))
# Output: Used time: x.xx ms
# 55