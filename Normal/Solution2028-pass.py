# 2028、找出缺失观测数据
from typing import List, Union, Any


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        nums = list(map(lambda x: n * x, [1, 2, 3, 4, 5, 6]))
        all_ = mean * (len(rolls) + n) - sum(rolls)
        if all_ < nums[0] or all_ > nums[-1]:
            return []
        bp = nums[0]
        addition = []
        for i in nums:
            if i == all_:
                base = nums.index(i) + 1
                for j in range(n):
                    addition.append(base)
                bp = i
                break
            elif i > all_:
                base = nums.index(i)
                for j in range(n):
                    addition.append(base)
                bp = nums[base - 1]
                break
        all_ -= bp
        for k in range(all_):
            addition[k] += 1
        return addition


s = Solution()
print(s.missingRolls([3, 2, 4, 3], 4, 2))
