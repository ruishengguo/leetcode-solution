# 1689、十-二进制数的最少数目


class Solution:
    def minPartitions(self, n: str) -> int:
        if '9' in n:
            return 9
        elif '8' in n:
            return 8
        elif '7' in n:
            return 7
        elif '6' in n:
            return 6
        elif '5' in n:
            return 5
        elif '4' in n:
            return 4
        elif '3' in n:
            return 3
        elif '2' in n:
            return 2
        elif '1' in n:
            return 1
        return 0
