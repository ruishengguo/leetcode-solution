# 1033、移动石子直到连续
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        l1 = [b - a - 1, c - b - 1]
        if l1.count(0) == 2:
            return [0, c - a - 2]
        elif 1 in l1 or 0 in l1:
            return [1, c - a - 2]
        else:
            return [2, c - a - 2]
