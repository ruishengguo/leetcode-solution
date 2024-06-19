# 62、不同路径


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[0] * n]
        for i in range(m - 1):
            dp.append(dp[0][:])
        dp[0][0] = 1
        for i in range(1, n):
            dp[0][i] = 1
        for i in range(1, m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
