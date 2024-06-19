# 7、整数反转‘


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        while x % 10 == 0:
            x //= 10
        if x < 0:
            neg = True
            x = -x
        else:
            neg = False
        x = int(str(x)[::-1])
        if neg:
            x = -x
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        else:
            return x
