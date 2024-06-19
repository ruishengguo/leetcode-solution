# 412、Fizz Buzz
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            addition = ''
            if i % 3 == 0:
                addition += 'Fizz'
            if i % 5 == 0:
                addition += 'Buzz'
            if addition:
                res.append(addition)
                continue
            res.append(str(i))
        return res
