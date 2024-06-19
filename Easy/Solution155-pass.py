# 155、最小栈


class MinStack:

    def __init__(self):
        self._stack_ = []
        self._min_ = 2 ** 31 - 1

    def push(self, val: int) -> None:
        self._stack_.append(val)
        self._min_ = min(self._min_, val)

    def pop(self) -> None:
        a = self._stack_.pop(-1)
        if a not in self._stack_:
            if self._stack_:
                self._min_ = min(self._stack_)
            else:
                self._min_ = 2 ** 31 - 1

    def top(self) -> int:
        return self._stack_[-1]

    def getMin(self) -> int:
        return self._min_
