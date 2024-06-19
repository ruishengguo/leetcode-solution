# 905、按奇偶排序数组
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i % 2 == 0:
                res.insert(0, i)
            else:
                res.append(i)
        return res
