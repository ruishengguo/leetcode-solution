# 342、4的幂


class Solution:
    def isPowerOfN(self, n: int, num: int) -> bool:
        if num == 0:
            return False
        elif num == 1:
            return True
        elif num % n != 0:
            return False
        else:
            return self.isPowerOfN(n, num // n)

    def isPowerOfFour(self, n: int) -> bool:
        return self.isPowerOfN(4, n)
