# 12、整数转罗马数字


class Solution:
    def intToRoman(self, num: int) -> str:
        char = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                'V': 5, 'IV': 4, 'I': 1}
        res = ''
        for i in char:
            if char[i] > num:
                continue
            res += (num // char[i]) * i
            num %= char[i]
        return res
