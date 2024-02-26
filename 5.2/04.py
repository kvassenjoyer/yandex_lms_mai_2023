class Fraction:
    # Дроби v0.1

    def __init__(self, *args):
        if len(args) == 1:
            self.num, self.den = map(int, args[0].split("/"))
        elif len(args) == 2:
            self.num, self.den = args[0], args[1]
        self.__reduce()

    def numerator(self, num=None):
        if num is None:
            return self.num
        else:
            self.num = num
            self.__reduce()

    def denominator(self, den=None):
        if den is None:
            return self.den
        else:
            self.den = den
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
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
