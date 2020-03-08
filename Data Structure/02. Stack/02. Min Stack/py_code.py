class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.supp_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.supp_stack) == 0:
            self.supp_stack.append(x)
        elif x <= self.supp_stack[-1]:
            self.supp_stack.append(x)

    def pop(self) -> None:
        if self.supp_stack[-1] == self.stack[-1]:
            self.supp_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.supp_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
