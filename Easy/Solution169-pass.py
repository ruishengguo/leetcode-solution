# 169、多数元素
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        point = len(nums) // 2
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] > point:
                return i
