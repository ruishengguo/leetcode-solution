from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        result = []
        for _ in list(range(k, n + 1)):
            addition = [_]
            for __ in self.combine(_ - 1, k - 1):
                result.append(addition + __)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
