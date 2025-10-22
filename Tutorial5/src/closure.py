def make_multiplier(factor: int):
    def multiply(x):
        return x * factor
    return multiply
double = make_multiplier(2)
print(double(5))  # Output: 10
