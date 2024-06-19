# 345、反转字符串中的元音字母


class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        changing = []
        indexs = []
        for i in range(len(s)):
            if s[i] in letters:
                changing.append(s[i])
                indexs.append(i)
        s = list(s)
        for i in range(len(changing)):
            s[indexs[i]] = changing[-i-1]
        s = ''.join(s)
        return s
