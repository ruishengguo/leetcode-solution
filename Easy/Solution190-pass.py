# 190、颠倒二进制位


class Solution:
    def reverseBits(self, n: int) -> int:
        a = str(bin(n))[2:][::-1]
        l = len(a)
        while l < 32:
            a += '0'
            l += 1
        return int(a, 2)


'''
res = 0
for i in range(32):
    res <<= 1
    res += n & 1
    n >>= 1
return res
'''
