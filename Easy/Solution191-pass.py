# 191、位1的个数


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & 1:
                res += 1
            n >>= 1
        return res
