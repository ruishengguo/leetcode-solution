# 344、反转字符串
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            a, b = s[i], s[-i - 1]
            if a != b:
                s[i], s[-i - 1] = b, a
