# 2126、摧毁小行星


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        for index, m in enumerate(asteroids):
            if m > mass:
                return False
            mass += m
        return True
