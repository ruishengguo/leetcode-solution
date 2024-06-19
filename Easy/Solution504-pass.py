# 504、七进制数


class Solution:
    def KBase(self, n, base):
        neg = False
        if n < 0:
            n = -n
            neg = True
        if n < base:
            return ('-' if neg else '') + str(n)
        else:
            return ('-' if neg else '') + self.KBase(n // base, base) + str(n % base)

    def convertToBase7(self, num: int) -> str:
        return self.KBase(num, 7)
