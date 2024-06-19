# 88、合并两个有序数组
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = []
        nums1.extend(nums2)
        while True:
            do_return = True
            for j in range(m + n - 1):
                a, b = nums1[j], nums1[j + 1]
                if a > b:
                    nums1[j], nums1[j + 1] = b, a
                    do_return = False
            if do_return:
                break
