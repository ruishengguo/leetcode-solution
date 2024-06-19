# 661、图片平滑器

class Solution:
    def imageSmoother(self, img: list) -> list:
        locs = [(-1, -1), (0, -1), (1, -1),
                (-1, 0), (0, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1)]
        lst = []
        for i in range(len(img)):
            lst.append([])
            for j in range(len(img[i])):
                sum_ = 0
                num = 0
                for k in range(9):
                    try:
                        a = img[i+locs[k][0]][j+locs[k][1]]
                    except IndexError:
                        continue
                    else:
                        if i+locs[k][0] < 0 or j+locs[k][1] < 0:
                            continue
                        else:
                            sum_ += a
                            num += 1
                lst[i].append(sum_ // num)
        return lst


s = Solution()
print(s.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
