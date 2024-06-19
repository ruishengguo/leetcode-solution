# 824、山羊拉丁文


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        elementary = 'aeiouAEIOU'

        def change(s: str, index: int) -> str:
            if s[0] not in elementary:
                s = s[1:] + s[0]
            s += 'ma' + 'a' * index
            return s

        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            sentence[i] = change(sentence[i], i + 1)
        return ' '.join(sentence)
