import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x % 10 == 0 or x < 0:
            return False
        else:
            times = 0
            new_x = x
            while new_x >= 1:
                new_x //= 10
                times += 1
            for i in range(times // 2):
                if not x // 10 ** i % 10 == x // 10 ** (times - i - 1) % 10:
                    return False
            return True

    def mul(self, n):
        max_ = 0
        for i in range(10 ** (n - 1), 10 ** n):
            for j in range(i, 10 ** n):
                if self.isPalindrome(i * j):
                    print(i, j, i * j, i % 11 == 0 or j % 11 == 0, i // 11 % 11, j // 11 % 11)
                    max_ = max(i * j, max_)
        print(max_)

s = Solution()
s.mul(1)
