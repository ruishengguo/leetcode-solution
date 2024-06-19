# 393、UTF-8 编码验证
import re
from typing import List


class Solution:
    sequence = (r'11110[01]{3}\W10[01]{6}\W10[01]{6}\W10[01]{6}\W', r'1110[01]{4}\W10[01]{6}\W10[01]{6}\W',
                r'110[01]{5}\W10[01]{6}\W', r'0[01]{7}\W')

    def validUtf8(self, data: List[int]) -> bool:
        def codec(s: int):
            s = bin(s)[2:]
            while len(s) < 8:
                s = '0' + s
            return s + ' '

        data = ''.join(list(map(codec, data)))
        for i in Solution.sequence:
            data = ''.join(re.split(i, data))
        return data == ''
