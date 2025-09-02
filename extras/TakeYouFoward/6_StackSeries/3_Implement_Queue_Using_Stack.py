# Link: https://takeuforward.org/plus/dsa/problems/implement-queue-using-stack

# Implement Queue using Two Stacks

class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        """Add element x to the end of the queue"""
        self.in_stack.append(x)

    def dequeue(self):
        """Remove element from the front of the queue and return it"""
        if self.isEmpty():
            return None
        self._transfer_if_needed()
        return self.out_stack.pop()

    def peek(self):
        """Get the front element of the queue"""
        if self.isEmpty():
            return None
        self._transfer_if_needed()
        return self.out_stack[-1]

    def isEmpty(self):
        """Check whether the queue is empty"""
        return not self.in_stack and not self.out_stack

    def _transfer_if_needed(self):
        """Transfer elements from in_stack to out_stack if out_stack is empty"""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


# ----------- Test Driver Code -----------
if __name__ == '__main__':
    queue = QueueUsingStacks()

    print("Enqueuing Elements: 10, 20, 30, 40, 50, 60")
    for val in [10, 20, 30, 40, 50, 60]:
        queue.enqueue(val)

    print(f"\nFront Element: {queue.peek()}")
    print(f"Dequeued Element: {queue.dequeue()}")
    print(f"Front Element after Dequeue: {queue.peek()}")
    print(f"Is Queue Empty?: {queue.isEmpty()}")

    print("\nDequeuing remaining elements:")
    while not queue.isEmpty():
        print(f"Dequeued: {queue.dequeue()}")

    print(f"\nIs Queue Empty after all dequeues?: {queue.isEmpty()}")
    print(f"Front Element now: {queue.peek()}")
    print(f"Dequeue when empty: {queue.dequeue()}")


"""
Time Complexity (Amortized):
- enqueue(): O(1)
- dequeue(): O(1) amortized, O(n) worst case when transferring elements
- peek(): O(1) amortized, O(n) worst case when transferring elements
- isEmpty(): O(1)

Space Complexity: O(n), where n is the number of elements in the queue
"""
