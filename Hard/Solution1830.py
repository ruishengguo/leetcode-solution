# 1830
from typing import Tuple


class Sort:
    """for test"""

    @staticmethod
    def get_i_j(s: str) -> Tuple[int, int]:
        """for test"""
        i, j, l = 0, 0, len(s)
        for index, item in enumerate(s):
            if index == 0:
                continue
            if s[index] < s[index - 1]:
                i = index
        index, temp = i, s[i - 1]
        for _ in s[i:]:
            if s[index] >= temp:
                j = index - 1
                break
            index += 1
            if index == l:
                j = index - 1
        return i, j

    @staticmethod
    def turn(i: int, j: int, s: str) -> str:
        s = list(s)
        s[i - 1], s[j] = s[j], s[i - 1]
        s[i:] = s[i:][::-1]
        return ''.join(s)

    @staticmethod
    def sort(s: str) -> int:
        times = 0
        while True:
            print(s, end=' ')
            i, j = Sort.get_i_j(s)
            if i == 0:
                return times
            s = Sort.turn(i, j, s)
            times += 1


class Solution:
    def makeStringSorted(self, s: str) -> int:
        pass


print('\nsorting times:', Sort.sort('1110987654321'))

a = 1
a = 2
print(b)

