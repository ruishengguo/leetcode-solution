# 面试题 16.07、最大数值


class Solution:
    def maximum(self, a: int, b: int) -> int:
        c = ((a - b) & (2 ** 64)) >> 64
        d = ((b - a) & (2 ** 64)) >> 64
        return c * b + (d + 2 + ~(c | d)) * a
