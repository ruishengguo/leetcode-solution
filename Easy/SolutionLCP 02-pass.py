# LCP 02、分式化简
import math
from typing import List


class Fraction:
    def __init__(self, p: int, q=1):
        self.p, self.q = p, q

    def __add__(self, other: int):
        return Fraction(self.p + self.q * other, self.q)

    def reverse(self):
        self.p, self.q = self.q, self.p


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        initial = Fraction(cont.pop())
        for i in cont[::-1]:
            initial.reverse()
            initial += i
        g = math.gcd(initial.p, initial.q)
        initial.p //= g
        initial.q //= g
        return [initial.p, initial.q]
