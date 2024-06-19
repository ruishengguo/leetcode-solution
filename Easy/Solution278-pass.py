# 278、第一个错误的版本
# The isBadVersion API is already defined for you.
bad = 1


def isBadVersion(version: int):
    return version == bad


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if isBadVersion(1):
            return 1
        r1 = 1
        r2 = n
        while True:
            a = (r1 + r2) // 2
            if isBadVersion(a):
                r2 = a
            else:
                r1 = a
            if r2 - r1 == 1:
                if isBadVersion(r2):
                    return r2
                return r1
