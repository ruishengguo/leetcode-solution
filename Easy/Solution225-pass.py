# 225、用队列实现栈


class MyStack:

    def __init__(self):
        self._s = []

    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        return self._s.pop(-1)

    def top(self) -> int:
        return self._s[-1]

    def empty(self) -> bool:
        return not bool(self._s)
