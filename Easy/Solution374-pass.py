# 374、猜数字大小
guessing = 1


def guess(num: int) -> int:
    if num == guessing:
        return 0
    elif guessing > num:
        return 1
    else:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        first, last = 1, n
        while True:
            if first + 1 == last:
                return first if guess(first) == 0 else last
            mid = (first + last) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                last = mid
            else:
                first = mid
