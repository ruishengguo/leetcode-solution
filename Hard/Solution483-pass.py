# 483、最小好进制
from typing import List


class Solution:
    def iter(self, n: int, length: int) -> List:
        base = 100000000000
        for i in range(33):
            base = pow((base * n - n + 1), 1 / length)
        if round(base) - round(base, 5) == 0.0:
            return [True, round(base) - (1 if round(base) > 10 ** 16 else 0)]
        else:
            return [False, round(base)]

    def smallestGoodBase(self, n: str) -> str:
        b_n = bin(int(n))[2:]
        if '0' not in b_n:
            return '2'
        for i in range(len(b_n), 1, -1):
            l = self.iter(int(n), i)
            if l[0]:
                num = (l[1] ** i - 1) // (l[1] - 1)
                if int(num) == int(n):
                    return str(l[1])
        return str(int(n) - 1)
