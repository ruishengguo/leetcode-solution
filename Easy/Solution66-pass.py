# 66、加一
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''        before = digits[:-1]
        last = digits[-1]
        if last == 9:
            try:
                return self.plusOne(before) + [0]
            except IndexError:
                return [1, 0]
        else:
            return before + [last + 1]'''
        return list(map(lambda x: int(x), list(str(int(''.join(list(map(lambda x: str(x), digits)))) + 1))))


def generator():
    y = 0
    while True:
        y = yield y
        print(y)


g = generator()
next(g)
g.send(1)
g.send(1)
g.send(1)
g.send(1)
g.send(1)