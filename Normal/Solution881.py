from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = [0]
        for i in range(1, limit + 1):
            weights.append(people.count(i))
        result = 0
        remain = 0
        for i in range((limit + 1) // 2, limit + 1)[::-1]:
            if i == (limit + 1) // 2:
                if limit % 2 == 0:
                    tot = weights[i] + remain
                    result += round(tot / 2 + .1)
                    remain = 0
                    break
            if weights[i] > remain:
                result += remain
                weights[i] -= remain
                if weights[i] > weights[limit - i]:
                    result += weights[i]
                    remain = 0
                else:
                    result += weights[i]
                    remain = weights[limit - i] - weights[i]
            else:
                result += weights[i]
                remain = remain - weights[i] + weights[limit - i]
        result += round(remain / 2 + .1)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats([3, 2, 2, 2, 3], 6))
