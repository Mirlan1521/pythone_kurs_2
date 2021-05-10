class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "i"

    def __add__(self, other):
        summa_re = self.re + other.re
        summa_im = self.im + other.im
        return Complex(summa_re, summa_im)

    def __sub__(self, other):
        minus_re = self.re - other.re
        minus_im = self.im - other.im
        return Complex(minus_re, minus_im)

    def __mul__(self, other):
        re = self.re * other.re - self.im + other.im
        im = self.re * other.im + other.re * self.im
        return Complex(re, im)

    def __truediv__(self, other):
        x = self.re * other.re + self.im * other.im
        y = self.im * other.re - self.re * other.im
        z = other.re ** 2 + other.im ** 2
        real = x / z
        imag = y / z
        return Complex(real, imag)


a = Complex(9, 6)
b = Complex(3, 2)
c = Complex(10, 15)
d = Complex(9, 7)
print(a + b)
print(a - b)
print(c * d)
print(a / b)
print(a + b + c + d)