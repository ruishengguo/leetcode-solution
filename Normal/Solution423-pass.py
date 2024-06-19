# 423、从英文中重建数字


class Solution:
    def originalDigits(self, s: str) -> str:
        letters = {"e": 0, "g": 0, "f": 0, "i": 0, "h": 0, "o": 0, "n": 0, "s": 0, "r": 0, "u": 0, "t": 0, "w": 0,
                   "v": 0, "x": 0, "z": 0}

        def update(words: str, sub: int) -> None:
            for j in words:
                letters[j] -= sub

        for i in s:
            letters[i] += 1
        res = [''] * 10

        def get_num(char: str, index: int, word: str) -> None:
            temp = letters[char]
            res[index] = str(index) * temp
            update(word, temp)

        get_num('z', 0, 'zero')
        get_num('w', 2, 'two')
        get_num('u', 4, 'four')
        get_num('x', 6, 'six')
        get_num('s', 7, 'seven')
        get_num('g', 8, 'eight')
        get_num('o', 1, 'one')
        get_num('h', 3, 'three')
        get_num('f', 5, 'five')
        get_num('i', 9, 'nine')
        r = ''
        for i in res:
            r += i
        return r
