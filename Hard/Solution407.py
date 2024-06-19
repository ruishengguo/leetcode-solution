from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        row = [0] * m
        res = []
        for i in range(n):
            res.append(row[:])
        del row
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res

    def prefMax(self, lst: List[int]) -> List[int]:
        pref_max = [lst[0]]
        for i in range(2, len(lst)):
            pref_max.append(max(lst[i - 1], pref_max[i - 2]))
        return pref_max

    def suffMax(self, lst: List[int]) -> List[int]:
        suff_max = [lst[-1]]
        for i in range(-3, -len(lst) - 1, -1):
            suff_max.insert(0, max(lst[i + 1], suff_max[i + 2]))
        return suff_max

    def trap(self, height: List[int]) -> List[int]:
        suff_max = self.suffMax(height)
        pref_max = self.prefMax(height)
        res = [0]
        for i in range(1, len(height) - 1):
            now = min(pref_max[i - 1], suff_max[i]) - height[i]
            if now > 0:
                res.append(now)
            else:
                res.append(0)
        res.append(0)
        return res

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        mapT = self.transpose(heightMap)
        for index, lst in enumerate(heightMap):
            heightMap[index] = self.trap(lst)
        for index, lst in enumerate(mapT):
            mapT[index] = self.trap(lst)
        row, col = len(heightMap), len(mapT)
        mapT = self.transpose(mapT)
        sum_ = 0
        for i in range(row):
            for j in range(col):
                sum_ += min(mapT[i][j], heightMap[i][j])
        return sum_


s = Solution()
print(s.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))
