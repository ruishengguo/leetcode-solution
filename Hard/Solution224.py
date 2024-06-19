# 224、基本计算器
from typing import List
import re


class I:
    def __init__(self, s: str) -> None:
        self._s = s
        self._cur = -1

    def __next__(self) -> (int, str):
        self._cur += 1
        return self._cur, self._s[self._cur]

    def update_str(self, s: str):
        self._s = s

    def update_cur(self, index=-1):
        self._cur = index

    def hasNext(self):
        return len(self._s) > self._cur + 1


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [0]
        for i in tokens:
            if i in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack.pop()

    def reversed_expr(self, expr: str) -> List[str]:
        res = []
        _ = []
        e = I(expr)
        if '(' in expr:
            left = []
            while e.hasNext():
                i, item = next(e)
                if item == '(':
                    left.append(i)
                elif item == ')':
                    l = left.pop()
                    _.append(self.reversed_expr(expr[l + 1:i]))
                    expr = expr[:l] + '@' + expr[i + 1:]
                    e.update_str(expr)
                    e.update_cur(l)
        e.update_cur()
        nums, cn = re.split(r'[+-]', expr), 1
        punc, cp = re.findall(r'[+-]', expr), 0
        ln, lp = len(nums), len(punc)
        res.append(nums[0])
        if ln == lp:
            res.append(punc[0])
            cp += 1
        while cn < ln:
            res.append(nums[cn])
            res.append(punc[cp])
            cn += 1
            cp += 1
        for i in range(len(res) - 1, -1):
            if res[i] == '@':
                res = res[:i] + _.pop() + res[i + 1:]
        return res

    def calculate(self, s: str) -> int:
        return self.evalRPN(self.reversed_expr(''.join(s.split(' '))))


s = Solution()
print(s.calculate("1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10"))
