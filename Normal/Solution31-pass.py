# 31、下一个排列
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        l = len(nums)
        fast, slow = -2, -1
        i = 0
        while True:
            if nums[fast] < nums[slow]:
                i = slow
                f = nums[fast]
                while slow < 0 and nums[slow] > f:
                    slow += 1
                j = slow - 1
                break
            fast -= 1
            slow -= 1
            if fast < -l:
                nums[:] = nums[::-1]
                return
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]
