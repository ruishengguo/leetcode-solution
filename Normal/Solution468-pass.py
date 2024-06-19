# 468、验证IP地址


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            queryIP = queryIP.split('.')
            if len(queryIP) != 4:
                return 'Neither'
            try:
                for i in range(4):
                    if int(queryIP[i]) > 255 or int(queryIP[i]) < 0:
                        return 'Neither'
                    elif queryIP[i][0] == '0' and len(queryIP[i]) != 1:
                        return 'Neither'
            except ValueError:
                return 'Neither'
            return 'IPv4'
        elif ':' in queryIP:
            queryIP = queryIP.split(':')
            if len(queryIP) != 8:
                return 'Neither'
            for i in queryIP:
                if 1 <= len(i) <= 4:
                    for char in i:
                        o = ord(char)
                        if not (48 <= o <= 57 or 65 <= o <= 70 or 97 <= o <= 102):
                            return 'Neither'
                else:
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'
