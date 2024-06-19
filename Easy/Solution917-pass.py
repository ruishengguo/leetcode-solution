# 917、仅仅反转字母


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res, end = '', len(s) - 1
        for i in s:
            if i in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                while s[end] not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                    end -= 1
                res += s[end]
                end -= 1
            else:
                res += i
        return res
