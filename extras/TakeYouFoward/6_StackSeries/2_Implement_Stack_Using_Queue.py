# Link: https://takeuforward.org/plus/dsa/problems/implement-stack-using-queue

# Implement Stack using Single Queue

from collections import deque

class StackUsingQueue:
    def __init__(self):
        """Initialize an empty queue"""
        self.q = deque()

    def push(self, x):
        """Push element x onto stack"""
        self.q.append(x)
        # Rotate the queue to bring the new element to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        """Removes the element on top of the stack and returns it"""
        if not self.isEmpty():
            return self.q.popleft()
        return None

    def peek(self):
        """Get the top element of the stack"""
        if not self.isEmpty():
            return self.q[0]
        return None

    def isEmpty(self):
        """Check whether the stack is empty"""
        return len(self.q) == 0


# ----------- Test Driver Code -----------
if __name__ == '__main__':
    stack = StackUsingQueue()

    print("Pushing Elements: 10, 20, 30, 40, 50, 60")
    for val in [10, 20, 30, 40, 50, 60]:
        stack.push(val)

    print(f"\nTop Element: {stack.peek()}")
    print(f"Popped Element: {stack.pop()}")
    print(f"Top Element after Pop: {stack.peek()}")
    print(f"Is Stack Empty?: {stack.isEmpty()}")

    print("\nPopping remaining elements:")
    while not stack.isEmpty():
        print(f"Popped: {stack.pop()}")

    print(f"\nIs Stack Empty after all pops?: {stack.isEmpty()}")
    print(f"Top Element now: {stack.peek()}")
    print(f"Pop when empty: {stack.pop()}")


"""
Time Complexity:
- push(): O(n) due to queue rotation
- pop(): O(1)
- peek(): O(1)
- isEmpty(): O(1)

Space Complexity: O(n) for storing elements in the queue
"""
