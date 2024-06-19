# 1720、解码异或后的数组
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            first ^= i
            res.append(first)
        return res
