# 89、格雷编码
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        nums = {}
        for i in range(n + 1):
            nums[i] = []
        for i in range(2 ** n):
            nums[list(bin(i)).count('1')].append(i)
        index = 0
        res = []
        for i in range(2 ** n):
            res.append(nums[index].pop(0))
            if index != 0:
                if nums[index - 1]:
                    index -= 1
                else:
                    index += 1
            else:
                index += 1
        return res
