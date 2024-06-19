# 面试题 01.05、一次编辑


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        l1, l2 = len(first), len(second)
        if l1 + 1 == l2:
            type_ = 'delete'
        elif l1 - 1 == l2:
            type_ = 'insert'
        elif l1 == l2:
            type_ = 'change'
        else:
            return False
        index = -1
        for i in range(min(l1, l2)):
            if first[i] != second[i]:
                index = i
                break
        if index == -1:
            return True
        if type_ == 'delete':
            second = second[:index] + second[index + 1:]
            return second == first
        elif type_ == 'change':
            second = second[:index] + first[index] + second[index + 1:]
            return second == first
        else:
            second = second[:index] + first[index] + second[index:]
            return second == first


s = Solution()
print(s.oneEditAway('house', 'horse'))
