# 1884、鸡蛋掉落-两枚鸡蛋


class Solution:
    def twoEggDrop(self, n: int) -> int:
        res = 1
        n *= 2
        while True:
            if (res + 1) * res >= n:
                return res
            res += 1
