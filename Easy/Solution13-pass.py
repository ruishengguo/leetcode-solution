# 13、罗马数字转整数

class Solution:
    def romanToInt(self, s: str) -> int:
        letter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
        lst = list(map(lambda x: letter[x], list(s)))
        delete = []
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                delete.append(i)
        for i in list(reversed(delete)):
            lst[i + 1] -= lst[i]
            lst.pop(i)
        return sum(lst)
