# 367、有效的完全平方数


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        first = 2
        last = num // 2
        while True:
            if last == first:
                return last ** 2 == num
            elif last == first + 1:
                return last ** 2 == num or first ** 2 == num
            else:
                mid = (first + last) // 2
                if mid ** 2 == num:
                    return True
                elif mid ** 2 > num:
                    last = mid
                else:
                    first = mid
