# 1025、除数博弈


class Solution:
    def divisorGame(self, n: int) -> bool:
        return not n & 1
