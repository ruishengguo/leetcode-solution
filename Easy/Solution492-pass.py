# 492、构造矩形
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sq = int(area ** 0.5)
        while True:
            if area % sq == 0:
                return [area // sq, sq]
            sq -= 1
