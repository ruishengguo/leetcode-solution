# 299、猜数字游戏


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret, guess = list(str(secret)), list(str(guess))
        s, g = [0] * 10, [0] * 10
        A, B = 0, 0
        rem = []
        for i, num in enumerate(secret):
            if num == guess[i]:
                A += 1
                rem.append(num)
            else:
                s[int(num)] += 1
        for i in rem:
            guess.remove(i)
        for i in guess:
            g[int(i)] += 1
        for i in range(10):
            B += min(s[i], g[i])
        return f"{A}A{B}B"
