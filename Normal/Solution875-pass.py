# 875、爱吃香蕉的珂珂
from typing import List


class Solution:
    @staticmethod
    def getHour(lst: List[int]):
        res = 0
        while True:
            a = yield res
            res = 0
            for i in lst:
                if i % a == 0:
                    res += i // a
                else:
                    res += i // a + 1

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        generator = Solution.getHour(piles)
        next(generator)
        max_ = max(piles)
        left, right = [1, sum(piles)], [max_, len(piles)]
        while True:
            mid = (left[0] + right[0]) // 2
            mid = [mid, generator.send(mid)]
            if mid[1] > h:
                left = mid
            else:
                right = mid
            if left[0] + 1 == right[0]:
                if left[1] <= h:
                    return left[0]
                return right[0]
