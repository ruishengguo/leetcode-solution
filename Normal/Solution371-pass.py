# 371、两整数之和


class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return a ^ b
        if a < 0 and b < 0 or a > 0 and b > 0:
            cut = False
        else:
            cut = True
        while True:
            temp = a & b
            if cut:
                a = a & (2 ** 24 - 1)
                b = b & (2 ** 24 - 1)
            a ^= temp
            b ^= temp
            b |= a
            if temp == 0:
                return b
            else:
                a = temp << 1
