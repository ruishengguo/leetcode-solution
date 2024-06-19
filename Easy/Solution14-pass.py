# 14、最长公共前缀
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = list(map(lambda x: list(x), strs))
        common = ''
        i = 0
        while True:
            try:
                addition = strs[0][i]
                for j in strs[1:]:
                    if j[i] != addition:
                        return common
                common += addition
                i += 1
            except IndexError:
                return common


s = Solution()
print(s.longestCommonPrefix(["","a"]))
