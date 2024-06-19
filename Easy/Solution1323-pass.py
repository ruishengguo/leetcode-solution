# 1323、6和9组成的最大数字


class Solution:
    def maximum69Number (self, num: int) -> int:
        num_ = str(num)
        index = num_.find('6')
        if index == -1:
            return num
        else:
            num_ = num_[:index] + '9' + num_[index + 1:]
            return int(num_)
