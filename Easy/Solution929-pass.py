# 929、独特的电子邮件地址
from typing import List


class Solution:
    def reformat(self, email: str) -> str:
        local, domain = email.split('@')[:2]
        if '+' in local:
            local = local.split('+')[0]
        if '.' in local:
            local = ''.join(local.split('.'))
        return local + '@' + domain

    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(map(lambda x: self.reformat(x), emails)))
