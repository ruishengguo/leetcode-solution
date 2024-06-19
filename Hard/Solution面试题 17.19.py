# 面试题 17.19、消失的两个数字
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        remain = 2
        for i in range(1, len(nums) + 3):
            if i in nums:
                nums.remove(i)
            else:
                nums.insert(0, i)
                remain -= 1
                if remain == 0:
                    return nums[:2]
