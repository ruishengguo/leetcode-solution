# 125、验证回文串


class Solution:
    def isPalindrome(self, s: str) -> bool:
        prefix = ''
        suffix = ''
        for i in s:
            i_id = ord(i)
            if 65 <= i_id <= 90:
                i = i.lower()
                prefix += i
                suffix = i + suffix
            elif 97 <= i_id <= 122 or 48 <= i_id <= 57:
                prefix += i
                suffix = i + suffix
        return prefix == suffix


s = Solution()
print(s.isPalindrome("0P"))
