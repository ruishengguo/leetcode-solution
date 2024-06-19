# 2081、k 镜像数字的和
import random
import time


class Solution:
    def KBase(self, n, base):
        if n < base:
            return str(n)
        else:
            return self.KBase(n // base, base) + str(n % base)

    def kMirror(self, k: int, n: int) -> int:
        res = 0
        for i in range(1, 10):
            if i < k or i % k == i // k or k == 2 and i % k == 1:
                res += i
                n -= 1
                if n == 0:
                    return res
        index = 0
        while True:
            next_lst = range(10 ** index, 10 ** (index + 1))
            for i in next_lst:
                p = int(str(i) + str(i)[::-1])
                a = self.KBase(p, k)
                if a[::-1] == a:
                    res += p
                    n -= 1
                    if n == 0:
                        return res
            for i in next_lst:
                for j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    p = int(str(i) + j + str(i)[::-1])
                    a = self.KBase(p, k)
                    if a[::-1] == a:
                        res += p
                        n -= 1
                        if n == 0:
                            return res
            index += 1


s = Solution()
t1 = time.time()
r = s.kMirror(2, 1)
for f in range(2, 31):
    r1 = s.kMirror(2, f)
    print(r1 - r)
    r = r1
print(round(1000 * (time.time() - t1)), 'ms')
