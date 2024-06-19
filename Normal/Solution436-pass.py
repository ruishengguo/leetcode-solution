# 436、寻找右区间
from typing import List


class Solution:
    def find_next(self, end: int, lst: List[int]):
        if end > lst[-1]:
            return '-1'
        elif end in lst:
            return end
        else:
            l = len(lst)
            left, right = 0, l - 1
            while True:
                if left + 1 == right:
                    return lst[right]
                mid = (left + right) // 2
                if lst[mid] > end:
                    right = mid
                elif lst[mid] < end:
                    left = mid

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_dict, start = {}, []
        end_dict, end = {}, []

        def find(val):
            if val == '-1':
                return -1
            return start_dict[val]

        for index, item in enumerate(intervals):
            start_dict[item[0]] = index
            start.append(item[0])
            end_dict[item[1]] = index
            end.append(item[1])
        start = sorted(start)
        res = list(map(lambda x: find(self.find_next(x, start)), end))
        return res
