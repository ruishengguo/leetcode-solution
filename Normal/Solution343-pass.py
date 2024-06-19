# 343、整数拆分


class Solution:
    def integerBreak(self, n: int) -> int:
        res = 0
        for k in range(2, n + 1):
            if k == n:
                res = max(res, 1)
                return res
            small = n // k
            big = small + 1
            b_n = n - small * k
            s_n = k - b_n
            res = max(res, big ** b_n * small ** s_n)
