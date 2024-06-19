# 1200、最小绝对差
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        res = []
        min_ = 2 * 10 ** 6
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] < min_:
                min_ = arr[i + 1] - arr[i]
                res = [arr[i:i + 2]]
            elif arr[i + 1] - arr[i] == min_:
                res.append(arr[i:i + 2])
        return res
