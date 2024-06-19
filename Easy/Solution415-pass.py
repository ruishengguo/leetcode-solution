# 415、字符串相加


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        letters = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = '0' * (len(num2) - len(num1)) + num1
        res = 0
        for i in range(len(num2)):
            res *= 10
            res += letters[num1[i]] + letters[num2[i]]
        return str(res)


s = Solution()
print(s.addStrings('342', '77'), 342 + 77)
