class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, value: int) -> None:
        self.st.append(value)

        if not self.minst:
            self.minst.append(value)
        else:
            self.minst.append(min(value, self.minst[-1]))

    def pop(self) -> int:
        if not self.st:
            return -1

        self.minst.pop()
        return self.st.pop()

    def top(self) -> int:
        if not self.st:
            return -1
        return self.st[-1]

    def getMin(self) -> int:
        if not self.minst:
            return -1
        return self.minst[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()