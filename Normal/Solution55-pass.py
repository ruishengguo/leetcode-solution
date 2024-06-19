# 55、跳跃游戏
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        if last == 0:
            return True
        dp0 = [0]
        while dp0:
            i = dp0.pop(0)
            for j in range(dp0[-1] if dp0 else i + 1, i + nums[i] + 1):
                if j == last:
                    return True
                if j not in dp0:
                    dp0.append(j)
        return False
