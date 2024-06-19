# 668、乘法表中第k小的数


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        add_ = m + n
        k -= 1
        lines = int((add_ - (add_ * add_ - 4 * k) ** 0.5) / 2 + 1)
        k -= (add_ - lines + 1) * (lines - 1) - 1
        initial = lines * lines
        ret = initial + lines * (k // 2)
        return ret


s = Solution()
m_ = 5
n_ = 6
for i in range(m_):
    for j in range(1, n_ + 1):
        print(s.findKthNumber(m_, n_, 10), end='\t')
