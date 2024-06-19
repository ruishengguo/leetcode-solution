# 946、验证栈序列
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)
            while popped[0] in stack:
                if popped.pop(0) != stack.pop():
                    return False
                if not popped:
                    return True
