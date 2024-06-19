# 2125、银行中的激光束数量
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) == 1:
            return 0
        cur = list(bank[0]).count('1')
        res = 0
        for i in bank[1:]:
            row = list(i).count('1')
            if row == 0:
                continue
            else:
                res += cur * row
                cur = row
        return res
