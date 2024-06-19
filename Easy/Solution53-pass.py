# 53、最大子数组和
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def find_max__(lst: List[int]) -> List[int]:
            n = len(lst)
            if n > 2:
                l1 = lst[:n // 2 + 1]
                l2 = lst[n // 2 + 1:]
                l1 = find_max__(l1)
                l1 = max(l1), l1[-1]
                if l1[-1] > 0:
                    l2.insert(0, l1[-1])
                for i in range(1, len(l2)):
                    past = l2[i - 1]
                    if past > 0:
                        l2[i] += past
                max2_ = max(l2)
                return [max(l1[0], max2_), l2[-1]]
            elif n == 2:
                return [lst[0], (lst[0] + lst[1]) if lst[0] > 0 else lst[1]]
            else:
                return [lst[0]]
        return max(find_max__(nums))
