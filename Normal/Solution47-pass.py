# 47、全排列 II
from typing import List


class TreeNode_n:
    def __init__(self, val=None, branches=None):
        self.val = val
        if not branches:
            self.branches = None
        if branches:
            self.branches = []
            for i in branches:
                if i not in self.branches:
                    self.branches.append(i)
            for i in range(len(self.branches)):
                sub_branches = branches[:]
                sub_branches.remove(self.branches[i])
                self.branches[i] = TreeNode_n(val=self.branches[i], branches=sub_branches)

    def get_list(self):
        if self.branches:
            res = []
            if self.val is not None:
                for i in self.branches:
                    for j in i.get_list():
                        res.append([self.val] + j)
            else:
                for i in self.branches:
                    for j in i.get_list():
                        res.append(j)
            return res
        else:
            return [[self.val]] if self.val is not None else None


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return TreeNode_n(branches=nums).get_list()
