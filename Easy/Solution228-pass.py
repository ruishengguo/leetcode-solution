# 228、汇总区间
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [str(nums[0])]
        temp = ''
        res = []
        for i in range(len(nums) - 1):
            slow = nums[i]
            fast = nums[i + 1]
            if not temp:
                temp = str(slow)
            if fast - slow > 1:
                end = str(slow)
                if temp == end:
                    res.append(temp)
                else:
                    res.append(temp + '->' + end)
                temp = ''
            if i == len(nums) - 2:
                if fast - slow > 1:
                    res.append(str(nums[-1]))
                else:
                    res.append(temp + '->' + str(nums[-1]))
        return res
