# 537、复数乘法


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        num2 = num2.split('+')
        num1[1], num2[1] = int(num1[1][:-1]), int(num2[1][:-1])
        num1[0], num2[0] = int(num1[0]), int(num2[0])
        real = num1[0] * num2[0] - num1[1] * num2[1]
        imaginary = num1[0] * num2[1] + num1[1] * num2[0]
        return f'{real}+{imaginary}i'
