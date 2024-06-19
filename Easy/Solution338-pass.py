# 338、比特位计数
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dpi = [0, 1]
        length = 2
        while True:
            if length >= n + 1:
                return dpi[:n + 1]
            else:
                dpi = dpi + list(map(lambda x: x + 1, dpi))
                length *= 2
