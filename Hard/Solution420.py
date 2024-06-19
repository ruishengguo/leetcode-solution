# 420、强密码检验器


import re


def isStrong(password: str) -> list:
    problems = [0, 0, 0]
    if len(password) > 20:
        problems[0] = len(password) - 20
    elif len(password) < 6:
        problems[0] = 6 - len(password)
    if not re.search(r'[A-Z]', password):
        problems[1] += 1
    if not re.search(r'[a-z]', password):
        problems[1] += 1
    if not re.search(r'[0-9]', password):
        problems[1] += 1
    problems[2] = sum(map(lambda x: len(x) // 3, re.findall(r'([0-9A-Za-z])\1{3,}', password)))
    return problems


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        return sum(isStrong(password))


s = Solution()
print(s.strongPasswordChecker('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'))
