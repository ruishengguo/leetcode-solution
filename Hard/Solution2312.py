# 2312、卖木头块
from typing import List


class Solution:
    def __init__(self):
        self.dictionary = {}
        self.min_ = [1000000, 1000000]
        self.searched = {}

    def search(self, prices: List[List[int]]) -> None:
        self.dictionary = {}
        self.min_ = [1000000, 1000000]
        for i in prices:
            self.min_ = [min(self.min_[0], i[0]), min(self.min_[1], i[1])]
            if i[0] not in self.dictionary:
                self.dictionary[i[0]] = {i[1]: i[2]}
            else:
                self.dictionary[i[0]][i[1]] = i[2]
        self.searched = {}

    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        def sw2(m_: int, n_: int, prices_: List[List[int]]) -> int:
            if m_ < self.min_[0] or n_ < self.min_[1]:
                return 0
            if (m_, n_) in self.searched:
                return self.searched[(m_, n_)]
            max_ = self.dictionary.get(m_, {}).get(n_, 0)
            for i in range(1, m_ // 2 + 1):
                max_ = max(max_, sw2(i, n_, prices_) + sw2(m_ - i, n_, prices_))
            for i in range(1, n_ // 2 + 1):
                max_ = max(max_, sw2(m_, i, prices_) + sw2(m_, n_ - i, prices_))
            self.searched[(m_, n_)] = max_
            return max_

        self.search(prices)
        return sw2(m, n, prices)


s = Solution()
print(s.sellingWood(18, 13, [[4, 4, 9], [2, 3, 22], [18, 10, 8]]))
