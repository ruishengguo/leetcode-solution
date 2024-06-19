# 868、二进制间距


class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        n = bin(n)
        gap = -1
        for num in list(n[2:]):
            gap += 1
            if num == '1':
                res = max(res, gap)
                gap = 0
        return res
