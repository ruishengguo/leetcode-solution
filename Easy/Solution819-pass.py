# 819、最常见的单词
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned.append('')
        paragraph = list(paragraph)
        for i in range(len(paragraph)):
            o = ord(paragraph[i])
            if 65 <= o <= 90:
                o += 32
                paragraph[i] = chr(o)
            elif o != 32 and o < 97 or o > 122:
                paragraph[i] = ' '
        paragraph = ''.join(paragraph).split(' ')
        d = {}
        for i in paragraph:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        max_ = 0
        res = ''
        for i in d:
            if i in banned:
                continue
            if d[i] > max_:
                max_ = d[i]
                res = i
        return res


s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
