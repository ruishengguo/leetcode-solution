# 1823、找出游戏的获胜者


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1 if k % 2 == 0 else 2
        res = list(range(1, n + 1))
        res = res[k % n:] + res[0:k % n - 1]
        return res[self.findTheWinner(n - 1, k) - 1]
