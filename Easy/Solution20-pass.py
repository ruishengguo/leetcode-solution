# 20、有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        whole = ["()", "[]", "{}"]
        while s != "":
            any_more = False
            for i in whole:
                if i in s:
                    pos = s.find(i)
                    s = list(s)
                    s.pop(pos)
                    s.pop(pos)
                    s = ''.join(s)
                    any_more = True
            if not any_more:
                return False
        return True
