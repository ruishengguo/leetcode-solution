# 476、数字的补数


class Solution:
    def findComplement(self, num: int) -> int:
        return ((1 << len(bin(num)[2:])) - 1) ^ num
