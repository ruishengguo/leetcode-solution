# 972、相等的有理数


def break_down(i: int):
    res = []
    initial = 2
    while initial ** 2 <= i:
        if i % initial == 0:
            res.append(initial)
            i //= initial
        else:
            initial += 1
    if i != 1:
        res.append(i)
    return res


def simplify(i1: int, i2: int):
    if i1 % i2 == 0:
        return i1 // i2, 1
    else:
        i2 = break_down(i2)
        r2 = 1
        while i2:
            temp = i2.pop()
            if i1 % temp == 0:
                i1 //= temp
            else:
                r2 *= temp
        return i1, r2


def fraction(num: str):
    num = num.split('.')
    inte = int(num[0])
    if not num[-1] or len(num) == 1:
        return str(inte)
    else:
        if '(' not in num[-1]:
            up = num[-1]
            up, down = int(up), int('1' + '0' * len(up))
            up, down = simplify(up + down * inte, down)
            if down == 1:
                return str(up)
            else:
                return str(up) + '/' + str(down)
        else:
            n, r = num[-1].split('(')
            r = r[:-1]
            down = int('9' * len(r) + '0' * len(n))
            if not n:
                up = int(r) + down * inte
            else:
                up = int(n + r) - int(n) + down * inte
            up, down = simplify(up, down)
            if down == 1:
                return str(up)
            else:
                return str(up) + '/' + str(down)


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        return fraction(s) == fraction(t)
