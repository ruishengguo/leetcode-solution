class Solution:
    def clearDigits(self, s: str) -> str:
        result = ""
        for i in s:
            if i in '0123456789':
                result = result[:-1]
            else:
                result += i
        return result
