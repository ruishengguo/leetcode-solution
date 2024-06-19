# 392、判断子序列


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            find = False
            for j in range(len(t)):
                if i == t[j]:
                    t = t[j + 1:]
                    find = True
                    break
            if not find:
                return False
        return True
