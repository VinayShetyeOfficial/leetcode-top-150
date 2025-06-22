# 155. Min Stack (Medium)
# https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack = []      # Main stack to hold all values
        self.minStack = []   # Auxiliary stack to track min at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new min value (either val or previous min)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


"""
✅ Time Complexity:
All operations (push, pop, top, getMin) = O(1)

✅ Space Complexity: O(n)
We use an auxiliary stack (minStack) of same size as stack
"""