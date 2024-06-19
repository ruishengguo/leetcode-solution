# 9、回文数

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
