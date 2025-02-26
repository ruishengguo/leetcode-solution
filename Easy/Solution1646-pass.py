# 1646、获取生成数组中的最大值


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        res = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[i // 2] + res[i // 2 + 1])
        return max(res)
