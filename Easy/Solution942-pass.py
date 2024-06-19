# 942、增减字符串匹配
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        prev, post = 0, len(s)
        res = []
        for i in s:
            if i == 'I':
                res.append(prev)
                prev += 1
            else:
                res.append(post)
                post -= 1
        res.append(post)
        return res
