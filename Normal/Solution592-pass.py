# 592、分数加减运算


class Fraction:
    def __init__(self, p=0, q=1):
        self.q, self.p = q, p

    def __add__(self, other):
        return Fraction(self.q * other.p + self.p * other.q, self.q * other.q)

    def simplify(self):
        import math
        g = math.gcd(self.p, self.q)
        self.p //= g
        self.q //= g

    def expr(self):
        return f"{self.p}/{self.q}"


class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != '-':
            expression = '+' + expression
        expression = tuple(map(lambda x: tuple(x.split('/')), '+-'.join(expression.split('-')).split('+')))[1:]
        initial = Fraction()
        for i in expression:
            initial += Fraction(int(i[0]), int(i[1]))
        initial.simplify()
        return initial.expr()
