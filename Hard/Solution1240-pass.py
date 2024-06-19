# 1240、铺瓷砖


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        minimum = min(n, m)
        maximum = minimum ^ n ^ m
        num_of_rect = [maximum]
        end = minimum // 2 - 1 if minimum % 2 == 0 else round(minimum / 2)
        for i in range(minimum, end, -1):
            extra_min = minimum - i
            extra_max = maximum - i
            length = i
            if extra_min == 0:
                num_of_rect.append(1 + self.tilingRectangle(extra_max, length))
            else:
                num_of_rect1 = 1
                min_length, max_length = length, length
                while True:
                    if min_length % extra_min == 0:
                        num_of_rect.append(min_length // extra_min + num_of_rect1 +
                                           self.tilingRectangle(extra_max, max_length + extra_min))
                        break
                    else:
                        num_of_rect1 += min_length // extra_min + 1
                        new_side = min_length + extra_max - extra_min * (min_length // extra_min + 1)
                        if max_length < new_side:
                            extra_min, extra_max, min_length, \
                                max_length = max_length, new_side, extra_min * (
                                    min_length // extra_min + 1) - min_length, extra_min
                        else:
                            extra_min, extra_max, min_length, \
                                max_length = new_side, max_length, extra_min, extra_min * (
                                    min_length // extra_min + 1) - min_length
        return min(num_of_rect)
