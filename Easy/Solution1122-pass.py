# 1122、数组的相对排序
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        all_elements = list(range(min(arr1), max(arr1) + 1))
        my_hash = {}
        for i in arr2:
            my_hash[i] = 0
            all_elements.remove(i)
        for i in all_elements:
            my_hash[i] = 0
        del all_elements
        for i in arr1:
            my_hash[i] += 1
        result = []
        for i in my_hash:
            for j in range(my_hash[i]):
                result.append(i)
        return result
