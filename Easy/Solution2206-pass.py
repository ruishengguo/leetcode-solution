# 2206、将数组划分成相等数对
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        while nums:
            a = nums.pop(0)
            try:
                nums.remove(a)
            except ValueError:
                return False
        return True
