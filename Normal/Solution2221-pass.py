# 2221、数组的三角和
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        power = [1]
        for i in range(1, rowIndex+1):
            power.append(i*power[-1])
        result = []
        for i in range(rowIndex+1):
            result.append(power[rowIndex]//(power[i]*power[rowIndex-i]))
        return result

    def triangularSum(self, nums: List[int]) -> int:
        l = len(nums)
        index = self.getRow(l - 1)
        res = 0
        for i in range(l):
            res += nums[i] * index[i]
        return res % 10
