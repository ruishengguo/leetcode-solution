class Solution:
    max_, min_ = (1 << 31) - 1, -(1 << 31)

    def divide(self, dividend: int, divisor: int, ignore_limit=False) -> int:
        if dividend < 0 or divisor < 0:
            if dividend < 0 and divisor < 0:
                result = self.divide(-dividend, -divisor, True)
            elif dividend < 0:
                result = -self.divide(-dividend, divisor, True)
            else:
                result = -self.divide(dividend, -divisor, True)
        else:
            count = 0
            while divisor < dividend:
                divisor <<= 1
                count += 1
            result = 0
            for i in range(count + 1):
                result <<= 1
                if divisor <= dividend:
                    result += 1
                    dividend -= divisor
                divisor >>= 1
        if not ignore_limit:
            if result >= Solution.max_:
                return Solution.max_
            elif result <= Solution.min_:
                return Solution.min_
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.divide(-2147483648, 1))
