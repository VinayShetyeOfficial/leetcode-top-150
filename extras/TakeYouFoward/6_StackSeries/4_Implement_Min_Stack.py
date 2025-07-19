# Implement Min Stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> int:
        if not self.stack:
            return None

        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minStack:
            return None

        return self.minStack[-1]


# ----------- Test Driver Code -----------
if __name__ == '__main__':
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print("Full Stack:", stack.stack)
    print(f'Min Stack Value: {stack.getMin()}')
    print(f'Popped Value: {stack.pop()}')
    print()
    print("After Pop Stack:", stack.stack)
    print(f'Top Value: {stack.top()}')
    print(f'Min Stack Value: {stack.getMin()}')

    # Extra simple test cases
    stack.push(-4)
    print()
    print("Pushed -4")
    print("Full Stack:", stack.stack)
    print(f'Top Value: {stack.top()}')
    print(f'Min Stack Value: {stack.getMin()}')
