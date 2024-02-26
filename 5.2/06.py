class Fraction:
    # Дроби v0.3

    def __init__(self, *args):
        if len(args) == 1:
            self.num, self.den = map(int, args[0].split("/"))
        elif len(args) == 2:
            self.num, self.den = args[0], args[1]
        if self.num * self.den < 0:
            self.sign = -1
        else:
            self.sign = 1
        self.num, self.den = abs(self.num), abs(self.den)
        self.__reduce()

    def numerator(self, num=None):
        if num is None:
            return self.num
        if num < 0:
            self.sign *= -1
        self.num = abs(num)
        self.__reduce()

    def denominator(self, den=None):
        if den is None:
            return self.den
        if den < 0:
            self.sign *= -1
        self.den = abs(den)
        self.__reduce()

    def __reduce(self):
        gcd = self.__get_gcd(self.num, self.den)
        self.num = self.num // gcd
        self.den = self.den // gcd

    def __get_gcd(self, a, b):
        a, b = min(a, b), max(a, b)
        while a != b:
            a, b = min(a, b - a), max(a, b - a)
        return a

    def __str__(self):
        return f"{self.sign * self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction('{self.sign * self.num}/{self.den}')"

    def __add__(self, other):
        num = self.sign * self.num * other.den + other.sign * other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.__dict__ = self.__add__(other).__dict__
        return self

    def __neg__(self):
        return Fraction(-1 * self.sign * self.num, self.den)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return other.__add__(self.__neg__())

    def __isub__(self, other):
        self.__dict__ = self.__sub__(other).__dict__
        return self
