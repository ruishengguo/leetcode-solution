# 372、超级次方
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return 1
        a %= 1337
        if a == 0:
            return 0
        index = 0
        res = 1
        for i in b[::-1]:
            temp = a ** i % 1337
            for i in range(index):
                temp **= 10
                temp %= 1337
            index += 1
            res *= temp
            res %= 1337
        return res
