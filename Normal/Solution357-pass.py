# 357、统计各位数字都不同的数字个数


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        res, addition = 10, 9
        for i in range(9, 10 - n, -1):
            addition *= i
            res += addition
        return res
