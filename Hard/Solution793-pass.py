# 793、阶乘函数后k个0


class Solution:
    def __init__(self):
        self.triangles = []
        num = 1
        while num < 10 ** 9:
            self.triangles.append(num)
            num = num * 5 + 1
        self.triangles = tuple(self.triangles)[::-1]

    def preimageSizeFZF(self, k: int) -> int:
        for i in self.triangles:
            if k % i == 0 and k // i == 5:
                return 0
            else:
                k %= i
        return 5
