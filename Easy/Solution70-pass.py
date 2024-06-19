# 70、爬楼梯


class Solution:
    def climbStairs(self, n: int) -> int:
        slow = 1
        fast = 1
        for i in range(n):
            slow, fast = fast, slow + fast
        return fast
