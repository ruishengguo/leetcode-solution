from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.cur = 0
        self.maximum = len(encoding)

    def next(self, n: int) -> int:
        if self.cur >= self.maximum:
            return -1
        elif n > self.encoding[self.cur]:
            self.cur += 2
            return self.next(n - self.encoding[self.cur - 2])
        else:
            self.encoding[self.cur] -= n
            ret = self.encoding[self.cur + 1]
            if self.encoding[self.cur] == 0:
                self.cur += 2
            return ret


r = RLEIterator([3, 8, 0, 9, 2, 5])
for i in [2, 1, 1, 2]:
    print(r.next(i))

