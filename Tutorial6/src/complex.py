class Complex:
    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im
    def __add__(self, other):
        return Complex(self.re + other.re,
                        self.im + other.im)
    def __str__(self):
        if self.im < 0:
            return f"{self.re} - {-self.im}i"
        return f"{self.re} + {self.im}i"
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im
    def __hash__(self):
        return hash((self.re, self.im))

c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1 + c2
print(c3)  # Output: 6 + 8i
c4 = Complex(5, -7)
c5 = c1 + c4
print(c5)  # Output: 7 - 4i
