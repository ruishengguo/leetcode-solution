# 273、整数转换英文表示


class Solution:
    nums = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
            '8': 'Eight', '9': 'Nine', '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen',
            '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen', '20': 'Twenty',
            '30': 'Thirty', '40': 'Forty', '50': 'Fifty', '60': 'Sixty', '70': 'Seventy', '80': 'Eighty',
            '90': 'Ninety'}
    sep = (' Doutrigintillion ', ' Untrigintillion ', ' Trigintillion ', ' Novemvigintillion ', ' Octovigintillion ',
           ' Septvigintillion ', ' Sexvigintillion ', ' Quinvigintillion ', ' Quattuorvigintillion ',
           ' Trevigintillion ', ' Douvigintillion ', ' Unvigintillion ', ' Vigintillion ', ' Novemdecillion ',
           ' Octodecillion ', ' Septdecillion ', ' Sexdecillion ', ' Quindecillion ', ' Quattuordecillion ',
           ' Tredecillion ', ' Doudecillion ', ' Undecillion ', ' Decillion ', ' Nonillion ', ' Octillion ',
           ' Septillion ', ' Sextillion ', ' Quintillion ', ' Quadrillion ', 'Trillion', ' Billion ', ' Million ',
           ' Thousand ', '')

    @staticmethod
    def in_thousand(num: str) -> str:
        while len(num) > 0 and num[0] == '0':
            num = num[1:]
        if not num:
            return ''
        if len(num) == 3:
            return Solution.nums[num[0]] + ' Hundred ' + Solution.in_thousand(num[1:])
        elif num in Solution.nums:
            return Solution.nums[num]
        else:
            return Solution.nums[num[0] + '0'] + ' ' + Solution.nums[num[1]]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        parts = []
        num = str(num)
        for i in range((len(num) - 1) // 3 + 1):
            parts.insert(0, num[-3:])
            num = num[:-3]
        parts = list(map(lambda x: Solution.in_thousand(x), parts))
        res = ''
        cur = len(Solution.sep) - 1
        for i in parts[::-1]:
            if not i:
                cur -= 1
                continue
            res = i + Solution.sep[cur] + res
            cur -= 1
        if res[-1] == ' ':
            res = res[:-1]
        return ' '.join(res.split('  '))
