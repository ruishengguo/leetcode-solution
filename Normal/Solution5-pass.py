# 5、最长回文子串


class Solution:
    def match(self, s1: str, s2: str) -> str:
        res = ''
        l2 = len(s2)
        for i, c in enumerate(s1):
            if i >= l2 or c != s2[i]:
                break
            res += c
        return res

    def longestPalindrome(self, s: str) -> str:
        pref, suff = '', s
        p_s = []
        for i in s:
            pref = i + pref
            p_s.append(self.match(pref, suff))
            suff = suff[1:]
            p_s.append(self.match(pref, suff))
        max_, res = 0, ''
        for i, rep in enumerate(p_s):
            if i % 2 == 0:
                if len(rep) * 2 - 1 > max_:
                    res, max_ = rep[::-1] + rep[1:], len(rep) * 2 - 1
            else:
                if len(rep) * 2 > max_:
                    res, max_ = rep[::-1] + rep, len(rep) * 2
        return res
