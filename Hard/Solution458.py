# 458、可怜的小猪


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        from math import log
        res = log(buckets, minutesToTest / minutesToDie + 1)
        if res % 1 != 0.0:
            res = int(res) + 1
        else:
            res = int(res)
        return res


s = Solution()
print(s.poorPigs(1000, 15, 15))
