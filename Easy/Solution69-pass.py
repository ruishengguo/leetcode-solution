# 69、x的平方根


class Solution:
    def mySqrt(self, x: int) -> int:
        # 巴比伦算法
        def generator():
            init = 10
            while True:
                init = (init + x / init) / 2
                yield init
        g = generator()
        inte = [int(next(g))]
        while True:
            next_ = int(next(g))
            if next_ == inte[-1]:
                return next_
            inte.append(next_)
