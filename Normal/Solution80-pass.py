from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = nums[0]
        count = 1
        index = 1
        try:
            while True:
                if nums[index] != cur:
                    cur = nums[index]
                    count = 1
                    index += 1
                else:
                    if count == 2:
                        while nums[index] == cur:
                            nums.pop(index)
                    else:
                        index += 1
                        count = 2
        except IndexError:
            return index
