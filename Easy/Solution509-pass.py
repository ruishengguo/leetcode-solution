# 509、斐波那契数


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]
