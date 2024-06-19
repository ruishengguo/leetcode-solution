# 290、单词规律


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = {}
        reverse_match = {}
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in match:
                match[pattern[i]] = s[i]
            elif match[pattern[i]] != s[i]:
                return False
            if s[i] not in reverse_match:
                reverse_match[s[i]] = pattern[i]
            elif reverse_match[s[i]] != pattern[i]:
                return False
        return True
