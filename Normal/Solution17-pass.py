# 17、电话号码的字母组合
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        buckets = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']
        for i in digits:
            addition = []
            for j in buckets[i]:
                deep_copy = list(map(lambda x: x + j, res[:]))
                addition += deep_copy
            res = addition
        return res
