# 1137、第N个泰波那契数


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        dp0, dp1, dp2 = 0, 1, 1
        for i in range(n - 2):
            dp0, dp1, dp2 = dp1, dp2, dp0 + dp1 + dp2
        return dp2
