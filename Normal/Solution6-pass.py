# 6、Z 字形变换


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = []
        for i in range(numRows):
            res.append('')
        index = 0
        reverse = False
        for i in s:
            if index == numRows - 1:
                res = res[::-1]
                res[0] += i
                index = 0
                reverse = not reverse
            else:
                res[index] += i
            index += 1
        if reverse:
            res = res[::-1]
        return ''.join(res)
