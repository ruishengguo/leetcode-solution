# 780、到达终点


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        elif sx == tx and sy == ty:
            return True
        else:
            return self.reachingPoints(sx, sy + sx, tx, ty) or self.reachingPoints(sx + sy, sy, tx, ty)

