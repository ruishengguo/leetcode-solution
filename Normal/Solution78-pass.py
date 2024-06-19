from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(1 << len(nums)):
            add_ = []
            a = i
            index = 0
            while a != 0:
                if a & 1 == 1:
                    add_.append(nums[index])
                a >>= 1
                index += 1
            result.append(add_)
        return result
