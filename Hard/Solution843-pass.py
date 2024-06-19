# 843、猜猜这个单词
from random import choice
from typing import List


class Master:
    base = "cymplm"
    guesstime = 10
    matchword = ["eykdft", "gjeixr", "eksbjm", "mxqhpk", "tjplhf", "ejgdra", "npkysm", "jsrsid", "cymplm", "vegdgt",
                 "jnhdvb", "jdhlzb", "sgrghh", "jvydne", "laxvnm", "xbcliw", "emnfcw", "pyzdnq", "vzqbuk", "gznrnn",
                 "robxqx", "oadnrt", "kzwyuf", "ahlfab", "zawvdf", "edhumz", "gkgiml", "wqqtla", "csamxn", "bisxbn",
                 "zwxbql", "euzpol", "mckltw", "bbnpsg", "ynqeqw", "uwvqcg", "hegrnc", "rrqhbp", "tpfmlh", "wfgfbe",
                 "tpvftd", "phspjr", "apbhwb", "yjihwh", "zgspss", "pesnwj", "dchpxq", "axduwd", "ropxqf", "gahkbq",
                 "yxudiu", "dsvwry", "ecfkxn", "hmgflc", "fdaowp", "hrixpl", "czkgyp", "mmqfao", "qkkqnz", "lkzaxu",
                 "cngmyn", "nmckcy", "alpcyy", "plcmts", "proitu", "tpzbok", "vixjqn", "suwhab", "dqqkxg", "ynatlx",
                 "wmbjxe", "hynjdf", "xtcavp", "avjjjj", "fmclkd", "ngxcal", "neyvpq", "cwcdhi", "cfanhh", "ruvdsa",
                 "pvzfyx", "hmdmtx", "pepbsy", "tgpnql", "zhuqlj", "tdrsfx", "xxxyle", "zqwazc", "hsukcb", "aqtdvn",
                 "zxbxps", "wziidg", "tsuxvr", "florrj", "rpuorf", "jzckev", "qecnsc", "rrjdyh", "zjtdaw", "dknezk"]

    def guess(self, word: str) -> int:
        res = 0
        if word not in Master.matchword:
            return -1
        for i in range(6):
            if Master.base[i] == word[i]:
                res += 1
        if res == 6 and Master.guesstime >= 1:
            print('You guessed the secret word correctly.')
        else:
            Master.guesstime -= 1
            if Master.guesstime == 0:
                print('Either you took too many guesses, or you did not find the secret word.')
        return res


class Solution:
    def match(self, base: str, matchword: str) -> int:
        res = 0
        for i in range(6):
            if base[i] == matchword[i]:
                res += 1
        return res

    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for i in range(9):
            base = choice(wordlist)
            wordlist.remove(base)
            num = master.guess(base)
            new_list = []
            if num == 6:
                return
            for j in wordlist:
                if self.match(base, j) == num:
                    new_list.append(j)
            wordlist = new_list
        master.guess(wordlist[0])
