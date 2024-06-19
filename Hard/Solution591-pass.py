# 591、标签验证器
import re


class Solution:
    def isValid(self, code: str) -> bool:
        copy = code
        if re.search(r'</*?[A-Z]*<\!\[CDATA\[.*?]]>[A-Z]*>', code):
            return False
        code = ''.join(re.split(r'<\!\[CDATA\[.*?]]>', code))
        tags = re.findall(r'</*?[A-Z]*>', code)
        if not tags or len(tags) % 2 == 1:
            return False
        else_ = ''.join(re.split(r'</*?[A-Z]*>', code))
        if '<' in else_:
            return False
        stack = []
        for i in tags:
            if list(i).count('<') > 1 or list(i).count('>') > 1:
                return False
            if re.match(r'<[A-Z]*>', i):
                stack.append(i[1:-1])
            elif re.match(r'</[A-Z]*>', i):
                if stack.pop(-1) != i[2:-1]:
                    return False
            else:
                return False
        if stack:
            return False
        if not re.match(rf'^{tags[0]}.*{"</" + tags[0][1:]}$', copy):
            return False
        return True
