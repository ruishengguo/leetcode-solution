# 168、 Excel表列名称


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphaBet = ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y"]

        def convert(num):
            if num <= 26:
                return alphaBet[num % 26]
            else:
                next_ = (num - 1) // 26
                return convert(next_) + alphaBet[num % 26]
        return convert(columnNumber)
