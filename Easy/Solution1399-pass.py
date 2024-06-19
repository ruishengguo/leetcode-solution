# 1399、统计最大组的数目


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        groups_length = {}
        for i in range(1, n + 1):
            res = 0
            for j in str(i):
                res += int(j)
            if res not in groups:
                groups[res] = 1
            else:
                groups[res] += 1
        res = 0
        max_ = 0
        for i in groups:
            if groups[i] > max_:
                res = 1
                max_ = groups[i]
            elif groups[i] == max_:
                res += 1
        return res
