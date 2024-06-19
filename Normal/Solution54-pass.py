# 54、螺旋矩阵
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        res = []
        mode = 0
        while True:
            if mode == 0:
                if left > right:
                    break
                res.extend(matrix[up][left:right + 1])
                up += 1
                mode = 1
            elif mode == 1:
                if up > down:
                    break
                for i in matrix[up:down + 1]:
                    res.append(i[right])
                right -= 1
                mode = 2
            elif mode == 2:
                if left > right:
                    break
                res.extend(matrix[down][left:right + 1][::-1])
                down -= 1
                mode = 3
            else:
                if up > down:
                    break
                for i in matrix[up:down + 1][::-1]:
                    res.append(i[left])
                left += 1
                mode = 0
        return res


s = Solution()
print(s.spiralOrder([[1,  2,  3,  4],
                     [5,  6,  7,  8],
                     [9,  10, 11, 12],
                     [13, 14, 15, 16],
                     [17, 18, 19, 20]]))
