import time


class Base:
    nums = ''

    def __init__(self):
        for i in range(128):
            Base.nums += chr(i)

    def base_128(self, number: int) -> str:
        res = ''
        while number >= 128:
            res = Base.nums[number % 128] + res
            number >>= 7
        res = Base.nums[number] + res
        return res

    def decode_base_128(self, number: str) -> str:
        res = 0
        for i in number:
            res <<= 7
            res += Base.nums.find(i)
        return str(res)


b = Base()


class Codec:

    def _code(self, string: str) -> str:
        res = ''
        for i in string:
            c = str(ord(i))
            res += '0' * (3 - len(c)) + c
        res = int(res)
        return b.base_128(res)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return self._code(longUrl)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = b.decode_base_128(shortUrl)
        shortUrl = '0' * (len(shortUrl) % 3) + shortUrl
        res = ''
        for i in range(len(shortUrl) // 3):
            res += chr(int(shortUrl[i * 3:i * 3 + 3]))
        return res


C = Codec()
a = C.decode(C.encode("https://leetcode.com/problems/design-tinyurl"))
pass
j = 0
print(a)
