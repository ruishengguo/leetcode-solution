# 38、外观数列


def generator():
    initial = '1'
    yield initial
    while True:
        res = ''
        times = 1
        cur = initial[0]
        for i in initial[1:]:
            if i == cur:
                times += 1
            else:
                res += str(times) + cur
                cur = i
                times = 1
        res += str(times) + cur
        initial = res
        yield res


class Solution:
    def __init__(self):
        self.g = generator()
        self.lst = []
        for i in range(30):
            self.lst.append(next(self.g))

    def countAndSay(self, n: int) -> str:
        return self.lst[n - 1]
