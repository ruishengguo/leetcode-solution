# 1837、K 进制表示下的各位数字总和


class Solution:
    def KBase(self, n, base):
        if base == 10:
            return str(n)
        if n < base:
            return str(n)
        else:
            return self.KBase(n // base, base) + str(n % base)

    def sumBase(self, n: int, k: int) -> int:
        res = 0
        for i in self.KBase(n, k):
            res += int(i)
        return res
