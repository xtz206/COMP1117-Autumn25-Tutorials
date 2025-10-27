class Complex:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return Complex(self.real + other.real,
                        self.imag + other.imag)
    def __str__(self):
        if self.imag < 0:
            return f"{self.real} - {-self.imag}i"
        return f"{self.real} + {self.imag}i"
c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1 + c2
print(c3)  # Output: 6 + 8i
c4 = Complex(5, -7)
c5 = c1 + c4
print(c5)  # Output: 7 - 4i