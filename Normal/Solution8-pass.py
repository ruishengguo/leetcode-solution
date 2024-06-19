# 8、字符串转整数


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        characters = {'+': '+', '-': '-', '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        index = 0
        neg = False
        l = len(s)
        while index < l:
            if s[index] != ' ':
                break
            index += 1
        if index >= l:
            return 0
        if s[index] not in characters:
            return 0
        elif s[index] in ['+', '-']:
            if s[index] == '-':
                neg = True
            index += 1
        res = 0
        while index < l:
            if s[index] in ['+', '-'] or s[index] not in characters:
                break
            res *= 10
            res += characters[s[index]]
            index += 1
            if not neg and res > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif neg and res > 2 ** 31:
                return -2 ** 31
        if neg:
            res = -res
        return res
