# 953、验证外星语词典
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_ = {}
        index = 0
        for i in 'abcdefghijklmnopqrstuvwxyz':
            dict_[order[index]] = i
            index += 1
        words = list(map(lambda x: ''.join(map(lambda y: dict_[y], x)), words))
        return tuple(sorted(words)) == tuple(words)
