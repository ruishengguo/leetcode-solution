# 401、
from typing import List


class TreeNode_n:
    def __init__(self, val, branches, depth, root_val):
        self.real_val = val
        self.val = root_val + val
        self.branches = []
        if branches and depth != 0:
            for i in range(len(branches)):
                new_branches = branches[:]
                v = new_branches.pop(i)
                new_branches = new_branches[i:]
                if v == 480:
                    new_branches.remove(240)
                if len(new_branches) < depth - 1:
                    break
                self.branches.append(TreeNode_n(v, new_branches, depth - 1, self.val))
            l = list(map(lambda x: x.lst, self.branches))
            self.lst = []
            for i in l:
                self.lst += i
        else:
            self.lst = [self.val]


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = [480, 240, 120, 60, 32, 16, 8, 4, 2, 1]
        res = TreeNode_n(0, times, turnedOn, 0)
        res = res.lst

        def minute_get_time(time: int):
            h = str(time // 60)
            m = time % 60
            if m < 10:
                m = '0' + str(m)
            else:
                m = str(m)
            return h + ':' + m

        res = list(map(lambda x: minute_get_time(x), res))
        return res


s = Solution()
print((s.readBinaryWatch(7)))
