# 1486、数组异或操作


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start
            start += 2
        return res
