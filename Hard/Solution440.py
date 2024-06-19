# 440、字典序的第k小数字

class Solution:
    def findKthNumberWith0(self, n, k):
        sub = int('1' * len(n))
        index = len(n)
        if sub > n:
            sub = int('1' * (len(n) - 1))
            index = len(n) - 1


    def findKthNumber(self, n: int, k: int):
        index = len(str(n)) - 1
        first = int(str(n)[0])
        over = n % 10 ** index + 1
        dict_first = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(1, 10):
            if i < first:
                dict_first[i] = (10 ** (index+1) - 1) // 9
            elif i == first:
                dict_first[i] = over + (10 ** (index - 0) - 1) // 9
            else:
                dict_first[i] = (10 ** (index - 0) - 1) // 9
        for i in range(10):
            k -= dict_first[i]
            if k <= 0:
                return i, dict_first[i], k + dict_first[i]


s = Solution()
print(s.findKthNumber(78655678654, 18655678654))
