# 937、重新排列日志文件
from typing import List


class Solution:
    def is_bigger(self, s1, s2):
        s1, s2 = s1.split(' '), s2.split(' ')
        s1, identifier1, s2, identifier2 = ' '.join(s1[1:]), s1[0], ' '.join(s2[1:]), s2[0]
        if s1 == s2:
            return identifier1 > identifier2
        else:
            return s1 > s2

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = []
        for i in logs:
            if i[-1] in '0123456789':
                nums.append(i)
        for i in nums:
            logs.remove(i)
        s = [logs[0]]
        for i in logs[1:]:
            found = False
            for index, j in enumerate(s):
                if self.is_bigger(j, i):
                    s.insert(index, i)
                    found = True
                    break
            if not found:
                s.append(i)
        return s + nums
