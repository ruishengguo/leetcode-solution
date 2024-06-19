# 2129、将标题首字母大写

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        divide = '['
        title = title.split(' ')
        for i in range(len(title)):
            title[i] = list(title[i])
            split_ = title[i]
            res = ''
            if len(split_) >= 3:
                if split_[0] > divide:
                    split_[0] = split_[0].capitalize()
                res += split_[0]
                split_ = split_[1:]
            for j in split_:
                if j < divide:
                    j = j.lower()
                res += j
            title[i] = res
        return ' '.join(title)
