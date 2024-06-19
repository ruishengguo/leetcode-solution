# 1342、将数字变成 0 的操作次数


class Solution:
    def numberOfSteps(self, num: int) -> int:
        time = 0
        while num != 0:
            if num % 2 == 1:
                time += 1
            num //= 2
            if num != 0:
                time += 1
        return time
