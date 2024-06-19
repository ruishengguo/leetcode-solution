# 433、最小基因变化
from typing import List


class Solution:
    def is_available(self, DNA1, DNA2) -> bool:
        difference = 0
        for i in range(8):
            if DNA1[i] != DNA2[i]:
                difference += 1
        if difference <= 1:
            return True
        return False

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        available = set(bank)
        if not bank or end not in bank:
            return -1
        map_ = {}
        for i in bank:
            map_[i] = []
            if self.is_available(i, start):
                map_[i] = ['start']
                continue
            for j in bank:
                if j == i or not self.is_available(j, i):
                    continue
                else:
                    map_[i].append(j)
        pile = {end}
        res = 1
        while True:
            new_pile = set()
            for i in pile:
                if 'start' in map_[i]:
                    return res
                else:
                    for j in map_[i]:
                        if j in available:
                            new_pile.add(j)
                    available.remove(i)
            res += 1
            if not available or pile == new_pile:
                return -1
            pile = new_pile


s = Solution()
print(s.minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))
