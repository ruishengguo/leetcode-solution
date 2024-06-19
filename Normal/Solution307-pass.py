# 307、区域和检索 - 数组可修改
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.lst = nums
        self.sums = []
        s = 0
        l = len(self.lst)
        for i in range(l):
            s = s + self.lst[i]
            if i % 100 == 99 or i == l - 1:
                self.sums.append(s)
                s = 0

    def update(self, index: int, val: int) -> None:
        self.sums[index // 100] = self.sums[index // 100] - self.lst[index] + val
        self.lst[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if right - left < 300:
            return sum(self.lst[left:right + 1])
        start = left // 100 + 1
        end = right // 100 - 1
        s = 0
        s = s + sum(self.sums[start:end + 1])
        s = s + sum(self.lst[left:start * 100]) + sum(self.lst[end * 100 + 100:right + 1])
        return s
