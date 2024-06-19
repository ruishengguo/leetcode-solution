# 806、写字符串需要的行数
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row = 0
        num = 1
        for i in s:
            row += widths[ord(i) - ord('a')]
            if row > 100:
                row = widths[ord(i) - ord('a')]
                num += 1
        return [num, row]

