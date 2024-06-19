# 1672、最富有客户的资产总量
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(list(map(lambda x: sum(x), accounts)))
