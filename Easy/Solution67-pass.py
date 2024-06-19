# 67、二进制求和


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        while True:
            temp = a & b
            a ^= temp
            b ^= temp
            b |= a
            if temp == 0:
                return str(bin(b))[2:]
            a = temp << 1
