# 303、区域和检索 - 数组不可变
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = [0]
        for i in nums:
            self.sum.append(self.sum[-1] + i)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]
