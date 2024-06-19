# 394、字符串解码
import re


class Solution:
    def decodeString(self, s: str) -> str:
        if '[' not in s:
            return s
        format_, other = re.findall(r'[0-9]*\[+?[a-z]*]', s), re.split(r'[0-9]*\[+?[a-z]*]', s)

        def form(pattern: str) -> str:
            pattern = pattern.split('[')
            times, pattern = int(pattern[0]), pattern[1][:-1]
            return pattern * times

        format_ = map(lambda x: form(x), format_)
        res = other.pop(0)
        for i in format_:
            res += i + other.pop(0)
        return self.decodeString(res)
