from __future__ import annotations
from typing import List, Union, Tuple

real = Union[int, float]


class Fig:
    @staticmethod
    def range(A: List[List[real]], a: real, b: real) -> List[real]:
        """
        return {A[i][j] | a > A[i][j] > b}
        """
        a_, b_ = [], []
        n = len(A)
        j_a, j_b = 0, n - 1
        for i in range(n):
            while j_a < n and A[i][j_a] >= a:
                j_a += 1
            a_.append(j_a)
            while j_b > -1 and A[n - 1 - i][j_b] <= b:
                j_b -= 1
            b_.insert(0, j_b)
        res = []
        for i in range(n):
            res.extend(A[i][a_[i]:b_[i] + 1])
        return sorted(res)

    @staticmethod
    def rank_minus(A: List[List[real]], a: real):
        """
        A: matrix n * n
        return rank- = |{x | x ∈ A, x < a}|
        """
        n = len(A)
        j, x = 0, 0
        for i in range(n):
            while j < n and A[i][j] >= a:
                j += 1
            x += n - j
        return x

    @staticmethod
    def pick(L: list, k: int):
        """
        returns the Kth item of L, k ∈ [1, |L|]
        """
        return L[k - 1]

    @staticmethod
    def rank_plus(A: List[List[real]], a: real):
        """
        A: matrix n * n
        return rank+ = |{x | x ∈ A, x > a}|
        """
        n = len(A)
        j, x = n - 1, 0
        for i in range(n - 1, -1, -1):
            while j > -1 and A[i][j] <= a:
                j -= 1
            x += j + 1
        return x

    @staticmethod
    def select(A: List[List[real]], k: int):
        n = len(A)
        x, y = Fig.biselect(n, A, k, k)
        return x

    @staticmethod
    def biselect(n: int, A: List[List[real]], k1: int, k2: int) -> Tuple[real, real]:
        if n <= 2:
            return A[k1 // n][k1 % n], A[k2 // n][k2 % n]
        if n % 2 == 0:
            k1_ = n + 1 + k1 // 4
        else:
            k1_ = (k1 + 2 * n + 1) // 4
        k2_ = (k2 + 3) // 4
        n_ = (n + 1) // 2
        A_ = []
        for row in A[::2]:
            A_.append(row[::2])
        a, b = Fig.biselect(n_, A_, k1_, k2_)
        ra_minus = Fig.rank_minus(A, a)
        rb_plus = Fig.rank_plus(A, b)
        L = Fig.range(A, a, b)
        if ra_minus <= k1 - 1:
            x = a
        elif k1 + rb_plus - n * n <= 0:
            x = b
        else:
            x = Fig.pick(L, k1 + rb_plus - n * n)
        if ra_minus <= k2 - 1:
            y = a
        elif k2 + rb_plus - n * n <= 0:
            y = b
        else:
            y = Fig.pick(L, k2 + rb_plus - n * n)
        return x, y


matrix = [[5,  4,  3,  2,  1],
          [10, 8,  6,  4,  2],
          [15, 12, 9,  6,  3],
          [20, 16, 12, 8,  4],
          [25, 20, 15, 10, 5]]
for i in range(12, 25):
    print(Fig.select(matrix, i))
