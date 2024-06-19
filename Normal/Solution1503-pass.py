# 1503、所有蚂蚁掉下来前的最后一刻


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left:
            lt = max(left)
        else:
            lt = 0
        if right:
            rt = n - min(right)
        else:
            rt = 0
        return max(rt, lt)
