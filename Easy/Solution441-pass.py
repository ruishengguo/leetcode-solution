# 441、排列硬币


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((1 + 8 * n) ** 0.5 / 2 - 0.5)
