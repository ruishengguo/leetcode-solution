# 232、用栈实现队列


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop(-1))
        self.stack1.append(x)
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop(-1))

    def pop(self) -> int:
        return self.stack2.pop(-1)

    def peek(self) -> int:
        return self.stack2[-1]

    def empty(self) -> bool:
        return not bool(self.stack2)
