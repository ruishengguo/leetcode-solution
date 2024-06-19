# 691、贴纸拼词
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        letters, a = {}, set()
        for i in target:
            a.add(i)
            if i not in letters:
                letters[i] = 1
            else:
                letters[i] += 1
        stickers_letters = set()
        for i in stickers:
            s = ''
            for j in i:
                if j in letters:
                    if j in a:
                        a.remove(j)
                    s += j
            if s:
                stickers_letters.add(''.join(sorted(s)))
        if a:
            return -1
        stickers_letters = list(stickers_letters)
        delete = set()
        for index, item in enumerate(stickers_letters):
            for j in stickers_letters[:index] + stickers_letters[index + 1:]:
                if item in j:
                    delete.add(item)
                    break
        for i in delete:
            stickers_letters.remove(i)

        def match(lst: str, targ: str):
            targ = list(targ)
            for i in lst:
                if i in targ:
                    targ.remove(i)
            return ''.join(targ)

        res, targs = 1, [target]
        while True:
            new_targs, min_ = set(), 10
            direct = False
            for i in targs:
                for j in stickers_letters:
                    r = match(j, i)
                    if not r:
                        return res
                    elif len(r) == 1:
                        direct = True
                    elif r != j:
                        new_targs.add(r)
            if direct:
                return res + 1
            res += 1
            targs = new_targs
