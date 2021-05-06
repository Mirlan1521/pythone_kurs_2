# Пример add
class Fraction:

    def __init__(self, numenator, denumenator):

        self.num = numenator
        self.den = denumenator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        if self.den == otherfraction.den:
            newden = self.den
            newnum = self.num + otherfraction.num
        else:
            newnum = self.num * otherfraction.den + self.den * otherfraction.num
            newden = self.den * otherfraction.den

        return Fraction(newnum, newden)


f1 = Fraction(10, 5)

f2 = Fraction(7, 5)

print(f1 + f2)

#Пример с Multi
class Fraction:

    def __init__(self, numenator, denumenator):
        self.num = numenator
        self.den = denumenator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)


f1 = Fraction(10, 5)

f2 = Fraction(7, 5)

print(f1 * f2)

# Пример с subtract
class Fraction:

    def __init__(self, numenator, denumenator):

        self.num = numenator
        self.den = denumenator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __sub__(self, otherfraction):
        if self.den == otherfraction.den:
            newden = self.den
            newnum = self.num - otherfraction.num
        else:
            newnum = self.num * otherfraction.den - self.den * otherfraction.num
            newden = self.den * otherfraction.den

        return Fraction(newnum, newden)


f1 = Fraction(10, 6)

f2 = Fraction(7, 5)

print(f1 - f2)

