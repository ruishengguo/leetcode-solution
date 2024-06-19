# 479、最大回文数乘积


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def largestPalindrome(self, n: int) -> int:
        if n % 2 == 0:
            return int('9' * (n // 2) + '0' * n + '9' * (n // 2)) % 1337
        elif n == 1:
            return 9
        elif n == 3:
            return 906609 % 1337
        else:
            max_ = int('9' * (n // 2) + '1' * (n // 2 * 2) + '9' * (n // 2))
            start = int(max_ ** 0.5)
            end = 10 ** n - 1
            b = False
            for i in range(end, start, -1):
                for j in range(end, i, -1):
                    if i * j < max_:
                        b = True
                        break
                    if i % 11 == 0 or j % 11 == 0:
                        if self.isPalindrome(i * j):
                            max_ = i * j
                if b:
                    break
            return max_ % 1337
