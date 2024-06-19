# 933、最近的请求次数
from collections import deque


class RecentCounter:

    def __init__(self):
        self.req = deque()

    def ping(self, t: int) -> int:
        self.req.append(t)
        slow = t - 3000
        while slow > self.req[0]:
            self.req.popleft()
        return len(self.req)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
