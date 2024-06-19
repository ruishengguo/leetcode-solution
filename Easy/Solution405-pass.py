# 405、数字转换为十六进制数


class Solution:
    def toHex(self, num: int) -> str:
        h = '0123456789abcdef'
        if num == 0:
            return '0'
        elif num < 0:
            num = 16 ** 8 + num
        block = 0b1111
        min_b = 1
        res = ''
        while min_b <= num:
            res = h[(num & block) // min_b] + res
            block <<= 4
            min_b <<= 4
        return res
