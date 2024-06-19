# 4、寻找两个正序数组的中位数
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        while True:
            if len(nums1) + len(nums2) == 2:
                return (sum(nums1) + sum(nums2)) / 2
            elif len(nums1) + len(nums2) == 1:
                return float(sum(nums1) + sum(nums2))
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
                if not nums1 or not nums2:
                    if not nums1:
                        nums2.pop(-1)
                    else:
                        nums1.pop(-1)
                    continue
                if nums1[-1] > nums2[-1]:
                    nums1.pop(-1)
                else:
                    nums2.pop(-1)
            else:
                if nums1:
                    l = len(nums1)
                    if l % 2 == 0:
                        l //= 2
                        return (nums1[l - 1] + nums1[l]) / 2
                    return float(nums1[l // 2])
                l = len(nums2)
                if l % 2 == 0:
                    l //= 2
                    return (nums2[l - 1] + nums2[l]) / 2
                return float(nums2[l // 2])
