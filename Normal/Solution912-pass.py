from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快排
        l = len(nums)
        if not nums:
            return []
        if l == 1:
            return nums
        elif l == 2:
            return nums if nums[0] <= nums[1] else nums[::-1]
        index = l // 2
        base = nums.pop(index)
        left, right = [], []
        for i in nums:
            if i <= base:
                left.append(i)
            else:
                right.append(i)
        return self.sortArray(left) + [base] + self.sortArray(right)


s = Solution()
print(s.sortArray([5,2,3,1]))
