# 383、赎金信


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote in magazine:
            return True
        else:
            magazine = list(magazine)
            for i in ransomNote:
                if i in magazine:
                    magazine.remove(i)
                    continue
                return False
            return True
