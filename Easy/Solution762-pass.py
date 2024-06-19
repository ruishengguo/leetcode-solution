# 762、二进制表示中质数个计算置位


class Solution:
    prime = []
    @staticmethod
    def is_prime(i):
        if i in Solution.prime:
            return True
        else:
            if i == 1:
                return False
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    return False
            Solution.prime.append(i)
            return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        from math import log2
        res = 0
        for i in range(left, right + 1):
            num = 0
            max_ = int(log2(i))
            for j in range(max_, -1, -1):
                if 2 ** j < i:
                    i -= 2 ** j
                    num += 1
                elif 2 ** j == i:
                    num += 1
                    break
            if Solution.is_prime(num):
                res += 1
        return res


s = Solution()
print(s.countPrimeSetBits(6, 1000000))

