# 46、全排列
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, nums[::-1]]
        res = []
        for i in nums:
            a = nums[:]
            a.remove(i)
            b = [i]
            for j in self.permute(a):
                res.append(b + j)
        return res


s = Solution()
a = s.permute([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a, len(a), sep='\n')
