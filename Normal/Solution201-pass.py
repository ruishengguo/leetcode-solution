class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left, right = bin(left)[2:], bin(right)[2:]
        if len(left) != len(right):
            return 0
        result = 0
        _0 = False
        for i in range(len(left)):
            result <<= 1
            if _0 == True:
                continue
            if left[i] == right[i]:
                if left[i] == '1':
                    result += 1
            else:
                _0 = True
        return result
