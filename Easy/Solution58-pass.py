# 58、最后一个单词的长度


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        length = 0
        for i in s[::-1]:
            if i != " ":
                length += 1
            elif length != 0:
                break
        return length
        '''
        return len(s.split()[-1])

