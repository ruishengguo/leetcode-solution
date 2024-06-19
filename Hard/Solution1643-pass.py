# 1643、第 K 条最小指令
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = min(m, n) - 1
        b = m + n - 2
        ans = 1
        for i in range(b, b - a, -1):
            ans *= i
        for i in range(1, a + 1):
            ans //= i
        return ans

    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        H, V = destination[1], destination[0]
        res = ''
        for i in range(H + V):
            p = self.uniquePaths(H + 1, V + 1)
            H_ = p * H // (H + V)
            if H_ >= k:
                H -= 1
                res += 'H'
            else:
                k -= H_
                V -= 1
                res += 'V'
        return res
