# 650、只有两个键的键盘


class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        i = 2
        while True:
            if n % i == 0:
                result += i
                n //= i
            else:
                i += 1
            if 2 * i > n:
                if n != 1:
                    result += n
                break
        return result
