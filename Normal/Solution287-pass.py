# 287、寻找重复数
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return i
