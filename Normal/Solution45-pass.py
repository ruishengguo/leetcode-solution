# 45、跳跃游戏 II
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        hash_ = [[0]]
        for i in range(1, l):
            hash_.append([])
        for i in range(l):
            now = min(hash_[i])
            hash_[i] = now
            for j in range(i + 1, i + nums[i] + 1):
                if j >= l:
                    break
                hash_[j].append(now)
        return hash_[-1]
