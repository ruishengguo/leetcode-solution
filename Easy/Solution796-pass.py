# 796、旋转字符串


class Solution:
    @staticmethod
    def rorate(s):
        return s[1:] + s[0]

    def rotateString(self, s: str, goal: str) -> bool:
        l = len(s)
        for i in range(l):
            if s == goal:
                return True
            s = Solution.rorate(s)
        return False
