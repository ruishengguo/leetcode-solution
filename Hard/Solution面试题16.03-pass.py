# 面试题 16.03、交点
from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x1, x2, x3, x4, y1, y2, y3, y4 = start1[0], end1[0], start2[0], end2[0], start1[1], end1[1], start2[1], end2[1]
        common_base = (x1 - x2) * (y4 - y3) - (x4 - x3) * (y1 - y2)
        x_up = x1 * x3 * (y4 - y2) + x1 * x4 * (y2 - y3) + x2 * x3 * (y1 - y4) + x2 * x4 * (y3 - y1)
        y_up = y1 * y3 * (x2 - x4) + y1 * y4 * (x3 - x2) + y2 * y3 * (x4 - x1) + y2 * y4 * (x1 - x3)
        if common_base != 0:
            # line1、line2不平行
            res = [round(x_up / common_base, 6), round(y_up / common_base, 6)]
            if (x1 - res[0]) * (x2 - res[0]) > 0 or (x3 - res[0]) * (x4 - res[0]) > 0:
                return []
            elif (y1 - res[1]) * (y2 - res[1]) > 0 or (y3 - res[1]) * (y4 - res[1]) > 0:
                return []
            return res
        else:
            # line1、line2平行
            if x_up != 0.0:
                # 平行不重合
                return []
            else:
                res_lst = []
                x_min = 2 ** 7
                if (x1 - x3) * (x1 - x4) <= 0 and (y1 - y3) * (y1 - y4) <= 0:
                    res_lst.append(start1)
                    x_min = x1
                if (x2 - x3) * (x2 - x4) <= 0 and (y2 - y3) * (y2 - y4) <= 0:
                    res_lst.append(end1)
                    x_min = min(x_min, x2)
                if (x3 - x1) * (x3 - x2) <= 0 and (y3 - y1) * (y3 - y2) <= 0:
                    res_lst.append(start2)
                    x_min = min(x_min, x3)
                if (x4 - x1) * (x4 - x2) <= 0 and (y4 - y1) * (y4 - y2) <= 0:
                    res_lst.append(end2)
                    x_min = min(x_min, x4)
                if not res_lst:
                    return []
                else:
                    new = []
                    for i in range(len(res_lst)):
                        if res_lst[i][0] == x_min:
                            new.append(res_lst[i])
                    res_lst = new
                    if len(res_lst) == 1:
                        return [round(res_lst[0][0], 6), round(res_lst[0][1], 6)]
                    min_ = 2 ** 7
                    temp = []
                    for i in res_lst:
                        if i[1] < min_:
                            temp = i
                            min_ = i[1]
                    return [round(temp[0], 6), round(temp[1], 6)]
