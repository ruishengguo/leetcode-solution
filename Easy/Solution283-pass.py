# 283、移动零
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        quantity = 0
        while 0 in nums:
            nums.remove(0)
            quantity += 1
        nums += [0] * quantity
