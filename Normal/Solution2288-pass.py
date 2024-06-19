class Solution:
    nums = '0123456789'

    def discountPrices(self, sentence: str, discount: int) -> str:
        mul_ = (100 - discount) / 100
        cur = ''
        cur_num = ''
        t_n = ' t'
        for _ in sentence:
            if t_n in ' t':
                if _ == '$' and t_n == ' t':
                    t_n = 'tn'
                elif _ == ' ':
                    t_n = ' t'
                else:
                    t_n = 't'
                cur += _
            else:
                if _ in Solution.nums:
                    cur_num += _
                    t_n = 'n'
                elif _ == ' ' and t_n == 'n':
                    num = str(round(int(cur_num) * mul_, 2))
                    if num[-2] == '.':
                        num += '0'
                    cur += num + ' '
                    t_n = ' t'
                    cur_num = ''
                else:
                    cur += cur_num + _
                    if _ == ' ':
                        t_n = ' t'
                    else:
                        t_n = 't'
                    cur_num = ''
        if t_n == 'n':
            num = str(round(int(cur_num) * mul_, 2))
            if num[-2] == '.':
                num += '0'
            cur += num
        return cur


if __name__ == '__main__':
    s = Solution()
    print(s.discountPrices("there are $1 $2 and 5$ candies in the shop", 50))
