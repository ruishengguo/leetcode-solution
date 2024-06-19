# 442、数组中重复的数据
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        res = []
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                res.append(i)
        return res
