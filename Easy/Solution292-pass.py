# 292、Nim游戏


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
