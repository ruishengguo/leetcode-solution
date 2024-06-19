# 409、最长回文串


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = set()
        res = 0
        for i in s:
            if i not in letters:
                letters.add(i)
            else:
                letters.remove(i)
                res += 2
        if letters:
            res += 1
        return res
