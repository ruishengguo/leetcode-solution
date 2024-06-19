# 728、自除数
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if i < 10:
                res.append(i)
                continue
            elif '0' in str(i):
                continue
            i_set = set(str(i))
            if '1' in i_set:
                i_set.remove('1')
            i_set = list(map(lambda x: int(x), i_set))
            do = True
            for j in i_set:
                if i % j != 0:
                    do = False
                    break
            if do:
                res.append(i)
        return res


s = Solution()
print(s.selfDividingNumbers(12, 987))
